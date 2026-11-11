#!/usr/bin/env python3
"""Stop hook for unattended overnight runs: block once when a turn nobody reads wrote text.

Reads the Stop hook event as JSON on stdin. While the presence marker
~/.claude/hooks-state/overnight-run-active exists, it blocks the stop once (the reason
is S1 below) when the turn wrote any text and neither the turn's starting prompt nor a
message that arrived during the turn was typed by the owner. In any other case it
prints nothing and exits 0 (allows the stop). On any error it also allows the stop.

Turn start: the last `user` entry that is a prompt (origin human, peer or
task-notification; not a tool result, not a skill load or other isMeta entry that is
not a peer message, not a compaction summary). The final message is taken from the
hook input's `last_assistant_message` (the transcript may not hold it yet at Stop time);
the turn's earlier text comes from the transcript. The transcript is read backwards in
fixed-size chunks until the turn's start is found, because it can be over 100 MB and
this runs on every Stop.

The block comes after the text is written, so it is a deterrent, not a filter: it
cannot take back text already shown.

Accepted edges (owner, L2-13):
- A scheduled-task turn may count as owner-typed under the gate's test, if it does.
- A run that dies without ending leaves the presence marker, so this hook stays on in
  sessions that invoked the skill until the next run's start deletes it or the owner does.
- Each block costs one model call.
- No hook reads usage or context use.
- An owner-started turn whose message the gate's owner-typed test rejects (text
  starting with "<", image-only content, slash-command wrappers) counts as not
  owner-typed, so such a turn is blocked if it wrote text.
- A user entry with origin human whose raw content carries a cross-session-message or
  task-notification wrapper (open or closed) counts as not owner-typed, even when the
  gate's test returns text for it. Other wrappers the gate strips (system-reminder,
  scheduled-task) are not checked here.
- A user entry whose origin kind is none of human, peer or task-notification (for
  example a channel message) is not a turn start, so the scan passes it and uses an
  earlier turn's start.
- A user entry that has no `origin` at all and carries a text prompt is treated as a
  turn start typed by the owner (fails open).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

MARKER = "~/.claude/hooks-state/overnight-run-active"
CHUNK = 64 * 1024

# S1 (overnight-run skill L3-6): the block reason, verbatim.
S1 = ("overnight: nobody is reading; put owner items on the morning list in the handoff doc "
      "(another lane: send them to the owner lane) and end the turn with nothing")


def read_back_lines(path, chunk=CHUNK):
    """Yield the lines of a file as bytes, last line first. A line longer than one chunk is
    joined across chunks."""
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        pos = f.tell()
        carry = b""
        while pos > 0:
            n = min(chunk, pos)
            pos -= n
            f.seek(pos)
            buf = f.read(n) + carry
            parts = buf.split(b"\n")
            carry = parts[0]
            for line in reversed(parts[1:]):
                if line.strip():
                    yield line
        if carry.strip():
            yield carry


def _content(d):
    m = d.get("message")
    return m.get("content") if isinstance(m, dict) else None


def _has_text(d):
    c = _content(d)
    if isinstance(c, str):
        return bool(c.strip())
    if isinstance(c, list):
        return any(isinstance(b, dict) and b.get("type") == "text"
                   and isinstance(b.get("text"), str) and b["text"].strip() for b in c)
    return False


def _is_tool_result(d):
    c = _content(d)
    return (isinstance(c, list) and bool(c)
            and all(isinstance(b, dict) and b.get("type") == "tool_result" for b in c))


def _origin_kind(d):
    o = d.get("origin")
    return o.get("kind") if isinstance(o, dict) else None


RELAY_MARKERS = ("<cross-session-message", "<task-notification")


def _has_relay_wrapper(d):
    """True when the entry's raw content carries a cross-session or task-notification
    wrapper, open or closed (compared lower-case). The gate's owner-typed test strips a
    closed wrapper and keeps the text around it, so it cannot see this on its own."""
    try:
        raw = json.dumps(_content(d), ensure_ascii=False).lower()
    except Exception:
        return False
    return any(m in raw for m in RELAY_MARKERS)


def is_turn_start(d):
    """A user entry that is a prompt: typed (human), a cross-session message (peer) or a
    task notification; origin-less text prompts also count (see the docstring)."""
    if d.get("type") != "user" or d.get("isSidechain") or d.get("isCompactSummary"):
        return False
    if _is_tool_result(d):
        return False
    kind = _origin_kind(d)
    if kind == "peer":
        return True
    if d.get("isMeta"):
        return False
    if kind in ("human", "task-notification"):
        return True
    return kind is None and d.get("origin") is None and _has_text(d)


def is_mid_turn_owner_message(d):
    """An owner message that arrived during the turn: an attachment entry whose attachment
    is a queued_command with commandMode "prompt" and origin kind "human"."""
    if d.get("type") != "attachment" or d.get("isSidechain"):
        return False
    a = d.get("attachment")
    if not isinstance(a, dict) or a.get("type") != "queued_command":
        return False
    if a.get("commandMode") != "prompt":
        return False
    o = a.get("origin")
    if not isinstance(o, dict):
        o = d.get("origin")
    return isinstance(o, dict) and o.get("kind") == "human"


def scan_turn(path, owner_typed, chunk=CHUNK):
    """Walk the transcript backwards to the turn's start. Returns (start_found,
    start_owner_typed, mid_turn_owner, wrote_text)."""
    mid_owner = False
    wrote = False
    for raw in read_back_lines(path, chunk):
        try:
            d = json.loads(raw)
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        t = d.get("type")
        if t == "assistant" and not d.get("isSidechain"):
            if _has_text(d):
                wrote = True
        elif t == "attachment":
            if is_mid_turn_owner_message(d):
                mid_owner = True
        elif t == "user" and is_turn_start(d):
            if _origin_kind(d) is None and d.get("origin") is None:
                typed = True
            else:
                typed = owner_typed(d) is not None and not _has_relay_wrapper(d)
            return True, typed, mid_owner, wrote
    return False, False, mid_owner, wrote


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    if not isinstance(data, dict):
        return 0
    if not os.path.exists(os.path.expanduser(MARKER)):
        return 0
    if data.get("stop_hook_active"):
        return 0
    path = data.get("transcript_path")
    if not isinstance(path, str) or not os.path.isfile(path):
        return 0
    from build_answer_gate import plain_human_text
    found, start_owner, mid_owner, wrote = scan_turn(path, plain_human_text)
    if not found:
        return 0
    last = data.get("last_assistant_message")
    if isinstance(last, str) and last.strip():
        wrote = True
    if wrote and not start_owner and not mid_owner:
        print(json.dumps({"decision": "block", "reason": S1}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BaseException:
        sys.exit(0)
