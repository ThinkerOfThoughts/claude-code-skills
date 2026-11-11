#!/usr/bin/env python3
"""SessionStart hook (matchers "compact" and "startup|resume"): re-inject rules that decay across a compaction.

A context-window compaction silently drops the standing rules a session was following —
"answer the literal question first," "quote don't recite," "read the handoff doc" — because
those live in earlier turns that compaction summarizes away. This hook fires only on the
"compact" source and prints a short plain-text reminder block to stdout, which
Claude Code adds as plain-text context (SessionStart's stdout-injection contract; see
https://code.claude.com/docs/en/hooks.md). It also scans for any ACTIVE plan_ledger run and
flags it, and drops a marker file recording when this compaction happened, so the sibling
read_gate.py hook (PreToolUse/PostToolUse) can tell whether a gated file was re-read AFTER
the most recent compaction rather than only "at some point in the session."

The hook branches on the input's `source`. `compact`, or no usable `source`: the reminder block,
plus the overnight-run line when the run marker exists. `startup` and `resume`: only the
overnight-run line, and only while the marker exists; no `compacted` marker is written. `clear`
and any other source: nothing. `OVERNIGHT_EGGTIMER_PING=1` in the environment: nothing, so the
egg timer's own `claude -p` ping starts fast.

Accepted edges (overnight run): while the run marker exists, any session started or resumed in
any project also gets the run line; a marker left behind by a crash keeps printing it until the
owner lane deletes the marker.

Conventions: stdlib only, defensive parsing, never raise out of main().
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
import time


REMINDER_BLOCK = """[post-compaction re-injection — a compaction just happened; the rules below are the ones that decay]
1. Answer the owner's question FIRST, in its own message. One question per message. When data was asked for, give the data, not a summary of it.
2. No relay/status traffic from sibling lanes in owner-facing messages; it goes in the handoff/ledger file.
3. Claims about the past (what was said/decided/why, by you or the owner) are LOOKUPS: quote the transcript or file, or mark the claim unverified.
4. Before quoting or editing any file, re-read the relevant part now; your pre-compaction memory of it is stale.
5. Read the project handoff doc IN FULL and quote its `## Secret:` token before substantive work (global handoff rule)."""

OVERNIGHT_MARKER = "~/.claude/hooks-state/overnight-run-active"
RUN_LINE = "an overnight run is on: read your handoff doc in full and invoke the overnight-run skill again"

ACTIVE_STATUS_RE = re.compile(r"^status:\s*ACTIVE\s*$", re.IGNORECASE | re.MULTILINE)


def _read_stdin_json() -> dict:
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def _find_active_ledgers(cwd: str) -> list[str]:
    found: list[str] = []
    patterns = [os.path.expanduser("~/.claude/plans/*-LEDGER.md")]
    if cwd:
        patterns.append(os.path.join(cwd, "*-LEDGER.md"))
    seen = set()
    for pattern in patterns:
        try:
            for path in glob.glob(pattern):
                if path in seen:
                    continue
                seen.add(path)
                try:
                    with open(path, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                except Exception:
                    continue
                if ACTIVE_STATUS_RE.search(content):
                    found.append(path)
        except Exception:
            continue
    return found


def _touch_compacted_marker(session_id: str) -> None:
    try:
        session_id = session_id or "unknown"
        state_dir = os.path.expanduser(os.path.join("~/.claude/hooks-state", session_id))
        os.makedirs(state_dir, exist_ok=True)
        marker_path = os.path.join(state_dir, "compacted")
        with open(marker_path, "w", encoding="utf-8") as f:
            f.write(str(time.time()))
    except Exception:
        # Never let marker bookkeeping block session start.
        pass


def _run_marker_exists() -> bool:
    try:
        return os.path.exists(os.path.expanduser(OVERNIGHT_MARKER))
    except Exception:
        return False


def main() -> int:
    if os.environ.get("OVERNIGHT_EGGTIMER_PING") == "1":
        return 0
    data = _read_stdin_json()
    source = data.get("source") if isinstance(data.get("source"), str) else ""
    if source in ("startup", "resume"):
        if _run_marker_exists():
            print(RUN_LINE)
        return 0
    if source not in ("", "compact"):
        return 0
    cwd = data.get("cwd") if isinstance(data.get("cwd"), str) else ""
    session_id = data.get("session_id") if isinstance(data.get("session_id"), str) else ""

    lines = [REMINDER_BLOCK]

    try:
        active = _find_active_ledgers(cwd)
    except Exception:
        active = []

    if active:
        lines.append(
            "6. ACTIVE plan_ledger run(s): "
            + ", ".join(active)
            + ". Re-invoke the plan-ledger skill and read the ledger IN FULL; quote its Secret token."
        )
    else:
        lines.append("6. No active plan_ledger run found.")

    if _run_marker_exists():
        lines.append(RUN_LINE)

    print("\n".join(lines))

    _touch_compacted_marker(session_id)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Never crash a SessionStart hook; fail open with no output.
        sys.exit(0)
