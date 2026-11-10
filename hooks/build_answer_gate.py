#!/usr/bin/env python3
"""build_answer_gate: PreToolUse hook that stops the planning lane from relaying a build answer to the build lane
unless each review step has a saved record showing a pass. An ACCIDENT guard (review steps skipped by mistake), not a
defence against an agent that deliberately forges records.

Modes (argv[1]):
  hook (default)  PreToolUse JSON on stdin. Exit 0 = allow (prints nothing), 10 = deny (JSON on stdout). Any other exit
                  code, a timeout or a missing python is a crash; the shell wrapper build_answer_gate.sh decides (deny if
                  the input looks addressed to the gated lane, else allow).
  sha <record> <id>                              print the current hash of an answer block
  stamp [--session ID] <record> <id> <kind> <result>   append a CHECK line (computes hash and time)
Test-only flags: --config P --log P --needles P --registry-glob P --scan-budget SECONDS --inject-error

EVIDENCE RULE (compliance, redteam and trio stamps). A stamp is written only when a cold agent's transcript, written by Claude Code under
<projects>/<slug>/<session>/subagents/agent-<id>.jsonl (or .../workflows/*/agent-<id>.jsonl), backs it, and the send check re-reads that
transcript. The cold agent QUALIFIES when: its spawn prompt (line 1 of its file) holds the 16-hex hash (compliance/redteam: the answer block's
hash; trio: the hash of the question block `TRIO <name> BEGIN/END` that the answer's TRIO:<name> tag cites, in the same record file); it is not a
fork (.meta.json isFork / agentType fork); it finished (no tool_use after its last user entry and the last text entry has stop_reason end_turn;
a file without stop_reason values does not qualify); it received no input after its prompt (a coordinator message, a queued_command, a revival);
and the final message does not hold a `REFUSED` line. Its verdict is the block of exact lines at the very end of its final message:
  [<id> ]hash=<hash> COMPLIANCE: PASS|FAIL|HELD      [<id> ]hash=<hash> REDTEAM: CLEAN|MINOR|MAJOR|BLOCKER      [<id> ]hash=<hash> TRIO: <answer>
or the bare `COMPLIANCE: <V>` / `REDTEAM: <V>` when the prompt holds exactly one 16-hex token. You may stamp the agent's own verdict or a worse one
(PASS<HELD<FAIL; CLEAN<MINOR<MAJOR<BLOCKER). Any one qualifying agent suffices; the CHECK line records the latest as ` agent=<id>`.
A trio stamp needs three distinct qualifying judges (the latest three) and a strict majority on the same answer (case/space-folded); the CHECK
line records ` agents=<id>,<id>,<id>`; the send check re-counts. SESSION: the send check uses `session_id` of the hook input; stamp uses
--session, else env CLAUDE_CODE_SESSION_ID; none -> stamp refuses. The session's directory is found through config `transcript_glob`
(the file <session>.jsonl and the directory of that name beside it).
WHAT IT PROVES: a transcript Claude Code wrote shows a non-fork, uninterrupted agent of this session, handed the hash in its prompt, ended with
that verdict. The send check also re-hashes the file text, so the text the hash names is the text sent. It does not prove the agent judged
well, and an agent that ignores the REFUSED sentence of its role brief still passes. Out of scope: a hand-written transcript file (deliberate forgery). Install note: CHECK lines without agent= / agents= are rejected at send.

Header grammar and record convention: ~/.claude/skills/plan-ledger/stages/cascade-build.md ("Gate record format") and the
change records in ~/.claude/hooks/changes/build-answer-gate/.
LIMIT: this hook sees only send_message / SendMessage. A file handoff (writing a doc the builder will read) cannot be
gated by a send hook.
"""
import datetime
import glob
import hashlib
import json
import os
import re
import stat
import sys
import time
from collections import deque

HERE = os.path.dirname(os.path.realpath(__file__))
DEFAULT_CONFIG = os.path.join(HERE, "build_answer_gate.config.json")
DEFAULT_LOG = os.path.join(HERE, "build_answer_gate.log.jsonl")
DEFAULT_NEEDLES = os.path.join(HERE, "build_answer_gate.needles")
DEFAULT_REGISTRY_GLOB = "~/.claude/sessions/*.json"
TOOLS = ("mcp__ccd_session_mgmt__send_message", "SendMessage")
SHAPE_RE = re.compile(r"local_[0-9a-f]{8}-|uds:/")
ASCII = re.ASCII

ID = r"[A-Za-z0-9][A-Za-z0-9._-]{0,40}"
TS = r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?(?:Z|[+-]\d\d:\d\d)"
RE_BEGIN = re.compile(rf"ANSWER ({ID}) BEGIN", ASCII)
RE_END = re.compile(rf"ANSWER ({ID}) END", ASCII)
AGENT = r"[A-Za-z0-9]{6,40}"
RE_COMP = re.compile(rf"CHECK ({ID}) compliance (PASS|FAIL|HELD) ({TS}) sha=([0-9a-f]{{16}})(?: agent=({AGENT}))?", ASCII)
RE_RT = re.compile(rf"CHECK ({ID}) redteam (CLEAN|MINOR|MAJOR|BLOCKER) ({TS}) sha=([0-9a-f]{{16}})(?: agent=({AGENT}))?", ASCII)
RE_TRIO = re.compile(rf"CHECK ({ID}) trio (DONE) ({TS}) sha=([0-9a-f]{{16}})(?: agents=({AGENT}(?:,{AGENT})*))?", ASCII)
RE_TBEGIN = re.compile(rf"TRIO ({ID}) BEGIN", ASCII)
RE_TEND = re.compile(rf"TRIO ({ID}) END", ASCII)
RE_HEX16 = re.compile(r"(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])")
RE_SESSION = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{7,80}")
VERDICTS = "PASS|FAIL|HELD|CLEAN|MINOR|MAJOR|BLOCKER"
RE_VLINE = re.compile(rf"(?:({ID}) )?hash=([0-9a-f]{{16}}) (COMPLIANCE|REDTEAM): ({VERDICTS})", ASCII)
RE_BARE = re.compile(rf"(COMPLIANCE|REDTEAM): ({VERDICTS})", ASCII)
RE_TLINE = re.compile(rf"(?:({ID}) )?hash=([0-9a-f]{{16}}) TRIO: (\S.*)", ASCII)
VERDICT_ORDER = {"compliance": ("PASS", "HELD", "FAIL"), "redteam": ("CLEAN", "MINOR", "MAJOR", "BLOCKER")}
KIND_LABEL = {"compliance": "COMPLIANCE", "redteam": "REDTEAM"}
RE_ANS_HDR = re.compile(rf"GATE: ANSWER(?: [^ ]+#{ID}(?:,{ID})*)+", ASCII)
SIMPLE_KINDS = {"GATE: ACK": "ACK", "GATE: MILESTONE": "MILESTONE", "GATE: QUESTION": "QUESTION"}
SHORT_RULING = 7
MIN_QUESTION_CHARS = 10
TRIO_RE = re.compile(r"\b(?:TRIO\s*:\s*|[Tt][Rr][Ii][Oo]:)([A-Za-z0-9._-]+)", ASCII)
RE_MARKER = re.compile(rf"(?:ANSWER {ID} (?:BEGIN|END)|TRIO {ID} (?:BEGIN|END)|CHECK {ID} (?:compliance|redteam|trio)\b.*)", ASCII)
WRAPPERS = ("cross-session-message", "system-reminder", "task-notification", "scheduled-task",
            "pasted_content", "command-message", "command-name", "command-args", "local-command-[A-Za-z-]+")
RE_WRAP_BLOCK = re.compile(r"<(" + "|".join(WRAPPERS) + r")(?:\s[^>]*)?>.*?</\1>", re.S)
RE_WRAP_OPEN = re.compile(r"<(?:" + "|".join(WRAPPERS) + r")\b")
STAMP_CMD = "python3 ~/.claude/hooks/build_answer_gate.py stamp"
ACCEPTED_FORMS = ("Accepted first lines (exact, first line only): "
                  "`GATE: ANSWER <file>#<id>[,<id>] [<file>#<id>...]` | `GATE: ACK` | `GATE: MILESTONE` | "
                  "`GATE: OWNER-RULING` | `GATE: QUESTION`. Format: ~/.claude/skills/plan-ledger/stages/cascade-build.md "
                  "(\"Gate record format\"). Limit: this hook sees only send_message/SendMessage; a file handoff "
                  "(a doc the builder is told to read) cannot be gated by a send hook and still needs the same steps.")


class Opts:
    config = DEFAULT_CONFIG
    log = DEFAULT_LOG
    needles = DEFAULT_NEEDLES
    registry_glob = DEFAULT_REGISTRY_GLOB
    inject_error = False
    scan_budget = None
    session = None


# ---------------------------------------------------------------- small helpers
def expand(p):
    return os.path.expanduser(p)


def norm_text(s):
    lines = [l.rstrip() for l in s.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def text_hash(s):
    return hashlib.sha256(norm_text(s).encode("utf-8")).hexdigest()[:16]


def sha16(s):
    return hashlib.sha256(s.encode("utf-8", "replace")).hexdigest()[:16]


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def norm_target(s):
    s = s.strip()
    s = re.sub(r"\s*\[[^\]]*\]\s*$", "", s)
    return s.strip().casefold()


# ---------------------------------------------------------------- config / registry / targets
def load_config(path):
    with open(path, "rb") as f:
        cfg = json.loads(f.read().decode("utf-8"))
    if not isinstance(cfg, dict):
        raise ValueError("config is not a JSON object")
    gt = cfg.get("gated_targets")
    if not isinstance(gt, list) or not gt or not all(isinstance(t, dict) and isinstance(t.get("id"), str) and t["id"]
                                                    for t in gt):
        raise ValueError("config.gated_targets must be a non-empty list of {id,title}")
    cfg.setdefault("aliases", [])
    cfg.setdefault("gated_senders", [])
    cfg.setdefault("allowed_record_dirs", ["~/.claude/plans"])
    cfg.setdefault("transcript_glob", "~/.claude/projects/*/*.jsonl")
    cfg.setdefault("max_record_bytes", 25000)
    cfg.setdefault("ruling_scan_budget_s", 20)
    return cfg

def read_registry(pattern):
    out = []
    for p in sorted(glob.glob(expand(pattern))):
        try:
            with open(p, "rb") as f:
                d = json.loads(f.read().decode("utf-8"))
            if isinstance(d, dict):
                out.append(d)
        except Exception:
            continue
    return out


def entry_keys(e):
    keys = []
    for k in ("hostSessionId", "sessionId", "name", "messagingSocketPath"):
        v = e.get(k)
        if isinstance(v, str) and v.strip():
            keys.append(v)
    sock = e.get("messagingSocketPath")
    if isinstance(sock, str) and sock.strip():
        keys.append("uds:" + sock)
    return keys


def resolve_set(items, aliases, reg):
    """items: list of {id,title}. Returns (members, idlike): normalised address strings of everything that
    names these lanes, directly or through the session registry."""
    base = set()
    idlike = set()
    for t in items:
        for k in ("id", "title"):
            v = t.get(k)
            if isinstance(v, str) and v.strip():
                base.add(norm_target(v))
        if isinstance(t.get("id"), str) and t["id"].strip():
            idlike.add(norm_target(t["id"]))
    for a in aliases or []:
        if isinstance(a, str) and a.strip():
            base.add(norm_target(a))
    members = set(base)
    for e in reg:
        ks = entry_keys(e)
        if any(norm_target(k) in base for k in ks):
            for k in ks:
                members.add(norm_target(k))
            for k in ("hostSessionId", "sessionId", "messagingSocketPath"):
                v = e.get(k)
                if isinstance(v, str) and v.strip():
                    idlike.add(norm_target(v))
            if isinstance(e.get("messagingSocketPath"), str):
                idlike.add(norm_target("uds:" + e["messagingSocketPath"]))
    return members, idlike


def is_gated(target, members, idlike):
    t = norm_target(target)
    if not t:
        return False
    if t in members:
        return True
    if len(t) >= 8 and any(len(g) >= 8 and g.startswith(t) for g in members):
        return True
    return any(i in t for i in idlike if len(i) >= 8)


def shape_gated(target, reg):
    t = norm_target(target)
    if not t:
        return False
    if SHAPE_RE.search(t) or t.startswith("uds:"):
        return True
    known = set()
    for e in reg:
        for k in entry_keys(e):
            known.add(norm_target(k))
    return t in known


def gated_looking_raw(raw, cfg, reg, members=None, idlike=None):
    """Does this raw hook input look addressed to the build lane? Used only on error paths (fail closed): the target
    fields are tested with the same matcher as the normal gate, and a raw text scan covers unparseable input."""
    low = raw.casefold()
    if cfg is not None and members is None:
        members, idlike = resolve_set(cfg["gated_targets"], cfg["aliases"], reg)
    try:
        d = json.loads(raw)
    except Exception:
        d = None
    ti = d.get("tool_input") if isinstance(d, dict) else None
    if isinstance(ti, dict):
        tv = [ti.get(k) for k in ("to", "recipient", "session_id") if ti.get(k) is not None]
        if all(isinstance(v, str) for v in tv):
            # clean string targets: decide on the targets alone (message text that merely mentions the lane is not a send to it)
            return any(is_gated(v, members, idlike) if cfg is not None else shape_gated(v, reg) for v in tv)
    if cfg is None:
        if SHAPE_RE.search(low):
            return True
        for e in reg:
            for k in entry_keys(e):
                if len(k) >= 8 and norm_target(k) in low:
                    return True
        return False
    return any(len(m) >= 8 and m in low for m in members) or any(len(i) >= 8 and i in low for i in idlike)


def _ere_escape(x):
    return re.sub(r"([.^$*+?()\[\]{}|\\])", r"\\\1", x)


def needle_lines(members, idlike):
    """What the shell wrapper can match when the script itself crashes. Every needle is an ERE anchored on a target field
    ("to", "recipient", "session_id"), so message text that merely mentions the lane never matches: id-like addresses
    (and the long id prefixes the gate also accepts) anywhere inside the field, names, titles and aliases as the whole
    field. Residual: a bare 8..13 character prefix of a local_ id is gated by the script but not by the wrapper."""
    out = set()
    for m in members | idlike:
        if m in idlike and len(m) >= 8:
            subs = {m}
            if m.startswith("local_") and len(m) >= 14:
                subs.add(m[:14])
            if re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", m):
                subs.add(m[:8])
            for x in subs:   # the id (or a long prefix of it) anywhere inside a target field
                out.add('re:"(to|recipient|session_id)" *: *"[^"]*%s' % _ere_escape(x))
        elif m not in idlike and len(m) >= 3:
            out.add('re:"(to|recipient|session_id)" *: *" *%s *(\\[[^]"]*\\])? *"' % _ere_escape(m))
    return sorted(out)


def write_needles(path, members, idlike):
    try:
        data = "\n".join(needle_lines(members, idlike)) + "\n"
        try:
            with open(path, "r", encoding="utf-8") as f:
                if f.read() == data:
                    return
        except OSError:
            pass
        tmp = "%s.tmp%d" % (path, os.getpid())
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(data)
        os.replace(tmp, path)
    except Exception:
        pass


# ---------------------------------------------------------------- log
def append_log(path, rec):
    try:
        line = (json.dumps(rec, ensure_ascii=False) + "\n").encode("utf-8", "replace")
        fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        try:
            os.write(fd, line)
        finally:
            os.close(fd)
    except Exception:
        pass


# ---------------------------------------------------------------- shared scan helpers (owner-ruling scan and evidence scan)
class ScanTimeout(Exception):
    pass


class Deadline:
    def __init__(self, seconds):
        self.seconds = seconds
        self.t_end = time.monotonic() + seconds

    def expired(self):
        return time.monotonic() > self.t_end


def scan_budget(cfg):
    return Opts.scan_budget if Opts.scan_budget is not None else cfg["ruling_scan_budget_s"]


def newest_first(files):
    return sorted(files, key=lambda f: (os.path.getmtime(f) if os.path.exists(f) else 0), reverse=True)


def iter_lines(path):
    """Raw lines (bytes) of a REGULAR file; a FIFO, directory or other special file yields nothing. Raises OSError on read errors."""
    if not stat.S_ISREG(os.stat(path).st_mode):
        return
    with open(path, "rb") as f:
        for line in f:
            yield line


def iter_json_lines(path):
    """Parsed JSON objects (dicts) of a regular JSONL file; unparseable lines (a half-written tail) are skipped."""
    for line in iter_lines(path):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if isinstance(d, dict):
            yield d


# ---------------------------------------------------------------- record parsing
def parse_record(text):
    """Returns dict(blocks={id:[text,...]}, struct=[(id,msg)], checks={(id,kind):[dict,...]},
    malformed=[(lineno,id|None,line)])."""
    R = {"blocks": {}, "struct": [], "checks": {}, "malformed": [], "trioq": {}}
    cur = None
    buf = []
    tcur = None
    tbuf = []
    for n, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip()
        if tcur is not None:
            m = RE_TEND.fullmatch(line)
            if m and m.group(1) == tcur:
                R["trioq"].setdefault(tcur, []).append("\n".join(tbuf))
                tcur = None
            else:
                tbuf.append(raw)
            continue
        if cur is None:
            m = RE_TBEGIN.fullmatch(line)
            if m:
                tcur, tbuf = m.group(1), []
                continue
            m = RE_BEGIN.fullmatch(line)
            if m:
                cur, buf = m.group(1), []
                continue
            m = RE_END.fullmatch(line)
            if m:
                R["struct"].append((m.group(1), "line %d: ANSWER %s END without BEGIN" % (n, m.group(1))))
                continue
            if line.startswith("CHECK "):
                _parse_check(R, n, line)
        else:
            m = RE_END.fullmatch(line)
            if m:
                if m.group(1) == cur:
                    R["blocks"].setdefault(cur, []).append("\n".join(buf))
                else:
                    R["struct"].append((cur, "line %d: ANSWER %s BEGIN closed by END of %s" % (n, cur, m.group(1))))
                cur = None
                continue
            if RE_MARKER.fullmatch(line):
                R["struct"].append((cur, "line %d: marker line inside the ANSWER %s block: %r" % (n, cur, line[:80])))
            buf.append(raw)
    if cur is not None:
        R["struct"].append((cur, "ANSWER %s BEGIN has no END" % cur))
    if tcur is not None:
        R["trioq"].setdefault(tcur, []).append("\n".join(tbuf) + "\n<no END>")   # hash cannot match a closed block
    return R


def _parse_check(R, n, line):
    toks = line.split(" ")
    ident = toks[1] if len(toks) > 1 and re.fullmatch(ID, toks[1], ASCII) else None
    for kind, rx in (("compliance", RE_COMP), ("redteam", RE_RT), ("trio", RE_TRIO)):
        m = rx.fullmatch(line)
        if m:
            R["checks"].setdefault((m.group(1), kind), []).append(
                {"n": n, "result": m.group(2), "ts": m.group(3), "sha": m.group(4), "line": line,
                 "agent": m.group(5) if kind != "trio" else None,
                 "agents": m.group(5).split(",") if kind == "trio" and m.group(5) else None})
            return
    R["malformed"].append((n, ident, line))


def resolve_record_path(path, cfg):
    """Returns (realpath, error)."""
    if not (path.startswith("/") or path.startswith("~/")):
        return None, "path must be absolute or start with ~/"
    if ".." in path.split("/"):
        return None, "path contains a .. component"
    real = os.path.realpath(expand(path))
    allowed = [os.path.realpath(expand(d)) for d in cfg["allowed_record_dirs"]]
    if not any(real == a or real.startswith(a + os.sep) for a in allowed):
        return None, "resolves to %s, outside the allowed record dirs %s" % (real, cfg["allowed_record_dirs"])
    return real, None


def load_record(path, cfg):
    """Returns (text, error). Reads the file once."""
    real, err = resolve_record_path(path, cfg)
    if err:
        return None, err
    try:
        st = os.stat(real)
        if not stat.S_ISREG(st.st_mode):
            return None, "not a regular file"
        if st.st_size > cfg["max_record_bytes"]:
            return None, "larger than %d bytes; split the record" % cfg["max_record_bytes"]
        with open(real, "rb") as f:
            data = f.read(cfg["max_record_bytes"] + 1)
        if len(data) > cfg["max_record_bytes"]:
            return None, "larger than %d bytes" % cfg["max_record_bytes"]
        return data.decode("utf-8"), None
    except UnicodeDecodeError:
        return None, "not valid UTF-8"
    except OSError as e:
        return None, "unreadable (%s)" % e.strerror


# ---------------------------------------------------------------- cold-agent evidence (stamp and send check)
def session_dirs(cfg, session):
    """The `subagents` directories of this session: beside the file <session>.jsonl matched by config `transcript_glob`."""
    if not isinstance(session, str) or not RE_SESSION.fullmatch(session):
        return []
    out = []
    for p in glob.glob(expand(cfg["transcript_glob"])):
        if os.path.basename(p) == session + ".jsonl":
            d = os.path.join(p[:-len(".jsonl")], "subagents")
            if os.path.isdir(d) and d not in out:
                out.append(d)
    return out


def agent_files(dirs):
    fs = []
    for d in dirs:
        e = glob.escape(d)
        fs += glob.glob(os.path.join(e, "agent-*.jsonl")) + glob.glob(os.path.join(e, "workflows", "*", "agent-*.jsonl"))
    return newest_first(fs)


def agent_path(dirs, agent_id):
    if not re.fullmatch(AGENT, agent_id or ""):
        return None
    for d in dirs:
        e = glob.escape(d)
        for pat in (os.path.join(e, "agent-%s.jsonl" % agent_id), os.path.join(e, "workflows", "*", "agent-%s.jsonl" % agent_id)):
            m = glob.glob(pat)
            if m:
                return m[0]
    return None


def _entry_text(e):
    m = e.get("message")
    return content_text(m.get("content") if isinstance(m, dict) else None)


def _epoch(ts, fallback):
    try:
        return datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
    except Exception:
        return fallback


def norm_answer(s):
    return re.sub(r"\s+", " ", s).strip().casefold()


_AGENT_CACHE = {}


def read_agent(path, hashes):
    """(info, reason). info is None when the agent's prompt does not hold any wanted hash (or the file is unusable). Otherwise info holds the
    agent id, the verdicts and trio answers of its final block, and reason is None when the agent QUALIFIES (see the module docstring) or a
    sentence saying why not."""
    key = (path, tuple(sorted(hashes)))
    if key in _AGENT_CACHE:
        return _AGENT_CACHE[key]
    try:
        res = _read_agent(path, hashes)
    except Exception as e:   # one odd file must not take the hook down
        res = (None, "unreadable (%s)" % type(e).__name__)
    _AGENT_CACHE[key] = res
    return res


def _read_agent(path, hashes):
    aid = os.path.basename(path)[len("agent-"):-len(".jsonl")]
    first = next(iter_lines(path), None)
    if first is None:
        return None, "empty or not a regular file"
    if not any(h.encode() in first for h in hashes):
        return None, "prompt lacks the hash"
    d = json.loads(first)
    m = d.get("message") if isinstance(d, dict) else None
    if not (isinstance(d, dict) and d.get("type") == "user" and isinstance(m, dict) and m.get("role") == "user"):
        return None, "line 1 is not the user prompt"
    prompt = _entry_text(d) or ""
    hexes = set(RE_HEX16.findall(prompt))
    if not any(h in hexes for h in hashes):
        return None, "prompt lacks the hash"
    info = {"agent": aid, "hexes": hexes, "verdicts": {}, "trio": {}, "tail": [], "ts": 0.0}
    try:
        mp = path[:-len(".jsonl")] + ".meta.json"
        if stat.S_ISREG(os.stat(mp).st_mode):       # a FIFO here must not hang the hook
            with open(mp, "rb") as f:
                meta = json.loads(f.read().decode("utf-8"))
            if isinstance(meta, dict) and (meta.get("isFork") is True or meta.get("agentType") == "fork"):
                return info, "it is a fork (it inherits the planner's context, so it is not a cold agent)"
    except (OSError, ValueError):
        pass
    buf, tool, stop, last_ts, inbound, n = [], False, None, None, False, 0
    for e in iter_json_lines(path):
        n += 1
        if n == 1:
            continue
        if isinstance(e.get("timestamp"), str):
            last_ts = e["timestamp"]
        t = e.get("type")
        if t == "user":
            mm = e.get("message")
            c = mm.get("content") if isinstance(mm, dict) else None
            if isinstance(c, list) and c and all(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                buf, tool, stop = [], False, None
            elif e.get("isMeta") is True and not e.get("origin"):
                pass   # harness-injected skill text, not input from anyone
            else:
                inbound = True
        elif t == "attachment":
            a = e.get("attachment")
            if isinstance(a, dict) and a.get("type") == "queued_command":
                inbound = True
        elif t == "assistant":
            mm = e.get("message")
            c = mm.get("content") if isinstance(mm, dict) else None
            for b in (c if isinstance(c, list) else []):
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "text" and isinstance(b.get("text"), str):
                    buf.append(b["text"])
                    stop = mm.get("stop_reason", e.get("stop_reason"))
                elif b.get("type") == "tool_use":
                    tool = True
    info["ts"] = _epoch(last_ts or "", os.path.getmtime(path))
    lines = [l.strip() for l in "\n".join(buf).split("\n") if l.strip()]
    info["tail"] = lines[-3:]
    if inbound:
        return info, "it received input after its prompt (a coordinator message, a queued command or a revival), so it is no longer the cold check"
    if tool or not buf:
        return info, "it has no final message yet (unfinished)"
    if stop != "end_turn":
        return info, "its final text entry has stop_reason %r, not 'end_turn' (an unknown counts as not finished)" % (stop,)
    if "REFUSED" in lines:
        return info, "it refused (its prompt told it the verdict): run a fresh cold agent"
    i = len(lines)
    while i > 0 and (RE_VLINE.fullmatch(lines[i - 1]) or RE_BARE.fullmatch(lines[i - 1]) or RE_TLINE.fullmatch(lines[i - 1])):
        i -= 1
    for line in lines[i:]:
        mm = RE_VLINE.fullmatch(line)
        if mm:
            h, label, v = mm.group(2), mm.group(3), mm.group(4)
        else:
            mm = RE_BARE.fullmatch(line)
            if mm and len(hexes) == 1:
                h, label, v = next(iter(hexes)), mm.group(1), mm.group(2)
            else:
                mm = RE_TLINE.fullmatch(line)
                if mm and mm.group(2) in hexes:
                    a = norm_answer(mm.group(3))
                    prev = info["trio"].get(mm.group(2), a)
                    info["trio"][mm.group(2)] = a if prev == a else ""   # two different answers for one hash: counts for nothing
                continue
        kind = label.lower()
        if h not in hexes or v not in VERDICT_ORDER[kind]:
            continue
        cur = info["verdicts"].get((h, label))
        if cur is None or VERDICT_ORDER[kind].index(v) > VERDICT_ORDER[kind].index(cur):
            info["verdicts"][(h, label)] = v
    return info, None


def scan_agents(cfg, session, hashes):
    """Every qualifying agent of the session whose prompt holds one of the hashes. Returns (agents, stats). Raises ScanTimeout."""
    dirs = session_dirs(cfg, session)
    stats = {"dirs": dirs, "files": 0, "hits": 0, "why": []}
    if not dirs:
        return [], stats
    dl = Deadline(scan_budget(cfg))
    out = []
    for i, p in enumerate(agent_files(dirs)):
        if i % 25 == 0 and dl.expired():
            raise ScanTimeout(dl.seconds)
        stats["files"] += 1
        info, reason = read_agent(p, hashes)
        if info is None:
            if reason and reason.startswith("unreadable"):
                stats["unreadable"] = stats.get("unreadable", 0) + 1
            continue
        stats["hits"] += 1
        if reason:
            stats["why"].append("%s: %s" % (info["agent"], reason))
        else:
            out.append(info)
    return out, stats


def lookup_agent(cfg, session, agent_id, h):
    """Send-time check of one recorded agent: (info, reason) as read_agent, or (None, why it cannot be found)."""
    dirs = session_dirs(cfg, session)
    if not dirs:
        return None, "no transcript directory for session %r under transcript_glob (nothing to verify against)" % (session,)
    p = agent_path(dirs, agent_id)
    if p is None:
        return None, "no agent transcript with id %s in this session" % agent_id
    info, reason = read_agent(p, [h])
    if info is None:
        return None, "agent %s: %s %s" % (agent_id, reason, h)
    return info, (("agent %s: %s" % (agent_id, reason)) if reason else None)


def rank(kind, v):
    return VERDICT_ORDER[kind].index(v)


def no_evidence_message(h, kind, stats, session):
    if kind == "trio":
        need = "`<id> hash=%s TRIO: <answer>`" % h
    else:
        lab = KIND_LABEL[kind]
        need = "`<id> hash=%s %s: <VERDICT>` (or the bare `%s: <VERDICT>` when its prompt holds only that one hash)" % (h, lab, lab)
    return ("no qualifying cold agent for hash %s in session %s (searched %s; %d agent files, %d whose prompt holds the hash). A cold agent must be "
            "spawned with the hash in its prompt and must end its final message with %s. %s"
            % (h, session, ", ".join(stats["dirs"]) or "no subagents directory (check transcript_glob in the config)", stats["files"], stats["hits"],
               need, (("Not qualifying: " + "; ".join(stats["why"][:5]) + ". ") if stats["why"] else "")
               + (("%d agent files were unreadable. " % stats["unreadable"]) if stats.get("unreadable") else "")))


def verify_agent_line(cfg, session, h, kind, c, where, used):
    """Send-time errors for the latest compliance/redteam CHECK line c (already sha- and result-checked)."""
    if not c.get("agent"):
        return ["%s: the %s line %d carries no agent id (written by hand, or before the cold-agent evidence rule). Stamp it from a cold agent's "
                "final lines." % (where, kind, c["n"])]
    if not session:
        return ["%s: cannot verify the %s cold check: the hook input has no usable session_id" % (where, kind)]
    info, reason = lookup_agent(cfg, session, c["agent"], h)
    if reason:
        return ["%s: the %s line %d names %s" % (where, kind, c["n"], reason)]
    v = info["verdicts"].get((h, KIND_LABEL[kind]))
    if v is None:
        return ["%s: agent %s has no `hash=%s %s: <VERDICT>` line in its final message (its last lines: %r)"
                % (where, c["agent"], h, KIND_LABEL[kind], info["tail"])]
    if rank(kind, c["result"]) < rank(kind, v):
        return ["%s: the %s line %d says %s but agent %s said %s (a stamp may be the agent's verdict or a worse one)"
                % (where, kind, c["n"], c["result"], c["agent"], v)]
    used.append("%s:%s:%s" % (c["agent"], kind, c["result"]))
    return []


def trio_question(rec, name):
    """(hash, error) of the question block `TRIO <name> BEGIN ... END` of the record."""
    qs = rec["trioq"].get(name, [])
    if len(qs) != 1 or qs[0].endswith("\n<no END>"):
        return None, ("the record needs exactly one closed `TRIO %s BEGIN` ... `TRIO %s END` question block for the TRIO:%s tag (found %d)"
                      % (name, name, name, len(qs)))
    if not norm_text(qs[0]):
        return None, "the TRIO %s question block is empty" % name
    return text_hash(qs[0]), None


def trio_majority(answers):
    """answers: list of normalised answers of the three judges. -> the strict-majority answer or None."""
    for a in set(answers):
        if a and answers.count(a) * 2 > len(answers):
            return a
    return None


def verify_trio_line(cfg, session, rec, name, c, where, used):
    qh, err = trio_question(rec, name)
    if err:
        return ["%s: %s" % (where, err)]
    agents = c.get("agents")
    if not agents or len(agents) != 3 or len(set(agents)) != 3:
        return ["%s: the trio line %d needs agents=<id>,<id>,<id> (three distinct cold judges); it was written by hand or before the evidence rule. "
                "Stamp it from the judges' final lines." % (where, c["n"])]
    if not session:
        return ["%s: cannot verify the trio: the hook input has no usable session_id" % where]
    answers = []
    for a in agents:
        info, reason = lookup_agent(cfg, session, a, qh)
        if reason:
            return ["%s: the trio line %d names %s" % (where, c["n"], reason)]
        ans = info["trio"].get(qh)
        if not ans:
            return ["%s: judge %s has no `hash=%s TRIO: <answer>` line in its final message (its last lines: %r)" % (where, a, qh, info["tail"])]
        answers.append(ans)
    if trio_majority(answers) is None:
        return ["%s: the three judges named by the trio line %d have no majority answer (%r)" % (where, c["n"], answers)]
    used.append("trio:%s" % ",".join(agents))
    return []


# ---------------------------------------------------------------- answer checks
KIND_STEP = {"compliance": "compliance check (stages/role-compliance-check.md)",
             "redteam": "gap red-team (stages/role-gap-redteam.md)",
             "trio": "trio (stages/role-trio-judge.md)"}


def check_one_id(rec, path, ident, text, tok_trio, cfg=None, session=None, used=None):
    """Errors for one (file,id): the compliance PASS, the red-team with no open MAJOR, and the trio line (when the
    answer cites one) must each carry the hash of the CURRENT answer block."""
    errs = []
    h = text_hash(text)
    for (ln, mid, line) in rec["malformed"]:
        if mid == ident:
            errs.append("%s#%s: malformed CHECK line %d: %r. Use the stamp command; the grammar is in cascade-build.md."
                        % (path, ident, ln, line[:100]))
    for kind in ["compliance", "redteam"] + (["trio"] if tok_trio else []):
        lines = rec["checks"].get((ident, kind), [])
        c = lines[-1] if lines else None
        fix = "%s %s %s %s ..." % (STAMP_CMD, path, ident, kind)
        n0 = len(errs)
        if c is None:
            errs.append("%s#%s: no %s line for the current text (hash %s). Run the %s step, then `%s`."
                        % (path, ident, kind, h, KIND_STEP[kind], fix))
        elif c["sha"] != h:
            errs.append("%s#%s: the answer text changed since the %s check (line %d has sha=%s, current hash is %s). "
                        "Re-run the check on the current text." % (path, ident, kind, c["n"], c["sha"], h))
        elif kind == "compliance" and c["result"] != "PASS":
            errs.append("%s#%s: latest compliance result is %s (line %d); fix the answer and re-check until PASS"
                        % (path, ident, c["result"], c["n"]))
        elif kind == "redteam" and c["result"] in ("MAJOR", "BLOCKER"):
            errs.append("%s#%s: latest gap red-team result is %s (line %d), still open; fix and re-run it"
                        % (path, ident, c["result"], c["n"]))
        if len(errs) == n0 and c is not None and used is not None:
            where = "%s#%s" % (path, ident)
            if kind == "trio":
                errs.extend(verify_trio_line(cfg, session, rec, tok_trio, c, where, used))
            else:
                errs.extend(verify_agent_line(cfg, session, h, kind, c, where, used))
    return errs


def check_answer(cfg, header_pairs, body, session=None, used=None):
    errs = []
    texts = []
    recs = {}
    for path in dict.fromkeys(p for p, _ in header_pairs):
        text, err = load_record(path, cfg)
        if err:
            errs.append("record file %s: %s" % (path, err))
        else:
            recs[path] = parse_record(text)
    for path, ident in header_pairs:
        rec = recs.get(path)
        if rec is None:
            texts.append(None)
            continue
        for (sid, msg) in rec["struct"]:
            if sid == ident:
                errs.append("%s#%s: %s" % (path, ident, msg))
        blocks = rec["blocks"].get(ident, [])
        if len(blocks) != 1:
            errs.append("%s#%s: %s (expected exactly one `ANSWER %s BEGIN` ... `ANSWER %s END` block)"
                        % (path, ident, "no ANSWER block" if not blocks else "%d ANSWER blocks" % len(blocks), ident, ident))
            texts.append(None)
            continue
        if not norm_text(blocks[0]):
            errs.append("%s#%s: the ANSWER block is empty" % (path, ident))
            texts.append(None)
            continue
        texts.append(blocks[0])
        m = TRIO_RE.search(blocks[0])
        errs.extend(check_one_id(rec, path, ident, blocks[0], m.group(1) if m else None, cfg, session, used if used is not None else []))
    if all(t is not None for t in texts):
        expected = "\n\n".join("%s:\n%s" % (i, norm_text(t)) for (p, i), t in zip(header_pairs, texts))
        got = norm_text(body)
        if got != expected:
            errs.append("message body does not equal the checked answer block (body hash %s, checked hash %s). The body "
                        "must be, in header order, `<id>:` then the ANSWER block text exactly, blocks separated by one "
                        "blank line, nothing else." % (text_hash(got), text_hash(expected)))
    return errs


# ---------------------------------------------------------------- owner-ruling relay
def norm_turn(s):
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    return "\n".join(l.strip() for l in s.split("\n")).strip()


def norm_flat(s):
    return re.sub(r"\s+", " ", s).strip()


def content_text(c):
    """The text of a message content: the string itself, or the text blocks joined by a newline; None when there is none."""
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        t = [b.get("text") for b in c if isinstance(b, dict) and b.get("type") == "text" and isinstance(b.get("text"), str)]
        return "\n".join(t) if t else None
    return None


def plain_human_text(d):
    """The text of a human-typed user turn, or None for anything else (tool results, peer/system injections, wrappers)."""
    if d.get("type") != "user" or d.get("isMeta") or d.get("isSidechain"):
        return None
    o = d.get("origin")
    if not (isinstance(o, dict) and o.get("kind") == "human"):
        return None
    m = d.get("message")
    c = m.get("content") if isinstance(m, dict) else None
    if isinstance(c, list):
        if not all(isinstance(b, dict) and b.get("type") in ("text", "image") for b in c):
            return None
        c = content_text(c)
        if c is None:
            return None
    if not isinstance(c, str):
        return None
    t = c.strip()
    if t.startswith("<"):
        return None
    t = RE_WRAP_BLOCK.sub(" ", t)
    if RE_WRAP_OPEN.search(t):
        return None
    return t


def assistant_strings(d):
    """The text the owner was shown by an assistant entry: its text blocks and AskUserQuestion inputs (not other tool inputs)."""
    out = []
    m = d.get("message")
    c = m.get("content") if isinstance(m, dict) else None
    if isinstance(c, str):
        return [c]
    if not isinstance(c, list):
        return out

    def walk(v):
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, dict):
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
    for b in c:
        if isinstance(b, dict):
            if b.get("type") == "text" and isinstance(b.get("text"), str):
                out.append(b["text"])
            elif b.get("type") == "tool_use" and b.get("name") == "AskUserQuestion":
                walk(b.get("input"))
    return out


def note_ask_ids(line, ids):
    """Add the ids of the AskUserQuestion tool_use blocks on one assistant transcript line to the set ids."""
    try:
        d = json.loads(line)
    except Exception:
        return
    m = d.get("message") if isinstance(d, dict) else None
    c = m.get("content") if isinstance(m, dict) else None
    if isinstance(c, list):
        for b in c:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "AskUserQuestion" \
                    and isinstance(b.get("id"), str):
                ids.add(b["id"])


def widget_answers(line, ask_ids):
    """The owner's answers in one transcript line that is the result of an AskUserQuestion call: a list of
    (question text, answer text). Empty for anything else. Only the harness-written `toolUseResult.answers` values count (a
    selected option label, typed text, or each selection of a multi-select), never the question, the options the assistant
    wrote, the previews, or the result's content string. Only when the entry is a user entry that is not meta and not a side
    chain, and every tool_result block in it belongs to an AskUserQuestion tool_use seen earlier in the same transcript
    (ask_ids) and is not an error (a declined question)."""
    try:
        d = json.loads(line)
    except Exception:
        return []
    if not isinstance(d, dict) or d.get("type") != "user" or d.get("isMeta") or d.get("isSidechain"):
        return []
    tur = d.get("toolUseResult")
    ans = tur.get("answers") if isinstance(tur, dict) else None
    m = d.get("message")
    c = m.get("content") if isinstance(m, dict) else None
    if not isinstance(ans, dict) or not isinstance(c, list):
        return []
    results = [b for b in c if isinstance(b, dict) and b.get("type") == "tool_result"]
    if not results or not all(isinstance(b.get("tool_use_id"), str) and b["tool_use_id"] in ask_ids and not b.get("is_error")
                              for b in results):
        return []
    out = []
    for q, a in ans.items():
        if not isinstance(q, str):
            continue
        for v in (a if isinstance(a, list) else [a]):
            if isinstance(v, str):
                out.append((q, v))
    return out


def quote_ok(nq, nt):
    """nq, nt normalised. A ruling of SHORT_RULING characters or fewer must equal the whole turn."""
    if not nq:
        return False
    if len(nq) <= SHORT_RULING:
        return nq == nt
    return nq in nt


def verify_rulings(blocks, cfg):
    """blocks: list of (quote, question|None); a quote of several lines is the consecutive `> ` lines of one block, joined by
    a newline. One pass over the transcripts, newest file first, stopping when every block is satisfied or the time budget is
    spent. A quote is found in a plain human-typed turn or in the owner's answer to an AskUserQuestion (widget_answers);
    nowhere else. A block is satisfied when the whole block is one turn's text (a real multi-line quote), or when every one of
    its lines is found by itself (R3: each `> ` line is a quote; a turn wrapped over several lines, or two turns on adjacent
    lines, both pass). Returns list of error strings."""
    pending = {}     # item id -> (normalised quote, normalised question|None)
    groups = []      # per block: (whole item id, [line item ids]); the line list is empty for a one-line block
    for q, re_ in blocks:
        nre = norm_flat(re_) if re_ else None
        whole = len(pending)
        pending[whole] = (norm_turn(q), nre)
        lines = []
        if "\n" in q:
            for l in q.split("\n"):
                lines.append(len(pending))
                pending[len(pending)] = (norm_turn(l), nre)
        groups.append((whole, lines))
    found = {}
    recent = deque(maxlen=60)   # assistant entries since the last plain human-typed turn
    budget = scan_budget(cfg)
    dl = Deadline(budget)
    timed_out = False
    files = newest_first(glob.glob(expand(cfg["transcript_glob"])))

    def satisfied(g):
        whole, lines = g
        return whole in found or (bool(lines) and all(i in found for i in lines))

    def all_done():
        return all(satisfied(g) for g in groups)

    def try_match(nt, ctx_fn):
        """Mark every pending item that the turn/answer text nt satisfies. ctx_fn() gives the normalised text its `re:`
        question must appear in."""
        ctx = []
        for i, (nq, nre) in pending.items():
            if i in found or not quote_ok(nq, nt):
                continue
            if nre is None and len(nq) <= SHORT_RULING:
                continue
            if nre is not None:
                if not ctx:
                    ctx.append(ctx_fn())
                if len(nre) < MIN_QUESTION_CHARS or nre not in ctx[0]:
                    continue
            found[i] = True

    def typed_ctx():
        ctx = []
        for rl in recent:
            try:
                ctx.extend(assistant_strings(json.loads(rl)))
            except Exception:
                pass
        return norm_flat("\n".join(ctx))

    for p in files:
        recent.clear()
        ask_ids = set()
        try:
            for n, line in enumerate(iter_lines(p)):
                if n % 2000 == 0 and dl.expired():
                    timed_out = True
                    break
                if b'"toolUseResult"' in line and b'"answers"' in line:
                    for q, a in widget_answers(line, ask_ids):
                        try_match(norm_turn(a), lambda q=q: norm_flat(q))
                    if all_done():
                        break
                    continue
                if b'"type":"assistant"' in line:
                    recent.append(line)
                    if b'"AskUserQuestion"' in line:
                        note_ask_ids(line, ask_ids)
                    continue
                if b'"kind":"human"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if not isinstance(d, dict):
                    continue
                t = plain_human_text(d)
                if t is None:
                    continue
                try_match(norm_turn(t), typed_ctx)
                recent.clear()
                if all_done():
                    break
        except OSError:
            continue
        if timed_out or all_done():
            break
    errs = []
    for g, (q, re_) in zip(groups, blocks):
        if satisfied(g):
            continue
        if g[1]:
            # name the first line of the block that no turn holds, not the first 60 characters of the whole block
            miss = [i for i in g[1] if i not in found]    # never empty here: all lines found would satisfy the block
            q = q.split("\n")[g[1].index(miss[0])]
        nq = norm_turn(q)
        if timed_out:
            errs.append("OWNER-RULING quote %r: the transcript scan did not finish within %d s (cold disk cache?), so the "
                        "quote could not be confirmed. The files read so far are cached now: send the relay again."
                        % (q[:60], budget))
        elif len(nq) <= SHORT_RULING and not re_:
            errs.append("OWNER-RULING quote %r is %d characters or fewer: add a `re: <the question it answered>` line "
                        "right after it (the question must appear in the assistant output just before that turn)"
                        % (q[:30], SHORT_RULING))
        elif re_:
            errs.append("OWNER-RULING quote %r with question %r: no human-typed turn or AskUserQuestion answer contains "
                        "this quote (a short ruling must be the whole turn or answer) right after assistant output "
                        "containing that question (or, for an answer, in that answer's own question); the question must "
                        "be at least %d characters" % (q[:60], re_[:60], MIN_QUESTION_CHARS))
        else:
            errs.append("OWNER-RULING quote %r: no human-typed turn or AskUserQuestion answer in the project transcripts "
                        "contains this text"
                        % q[:60])
    return errs


def check_owner_ruling(body, cfg):
    errs = []
    blocks = []
    cur = []
    for l in body.split("\n"):
        s = l.rstrip()
        if not s.strip():
            if cur:
                blocks.append(("\n".join(cur), None))
                cur = []
            continue
        if s.startswith("> "):
            cur.append(s[2:].strip())
        elif s.startswith("re: ") and cur:
            blocks.append(("\n".join(cur), s[4:].strip()))
            cur = []
        else:
            errs.append("OWNER-RULING allows only `> ` quote lines and `re: ` question lines; got %r" % s[:60])
    if cur:
        blocks.append(("\n".join(cur), None))
    if not blocks and not errs:
        errs.append("OWNER-RULING needs at least one `> quote` line (short rulings also a `re: question` line)")
    for q, re_ in blocks:
        if len(norm_turn(q)) <= SHORT_RULING and not re_:
            errs.append("OWNER-RULING quote %r is %d characters or fewer: add a `re: <the question it answered>` line "
                        "right after it (the question must appear in the assistant output just before that turn)"
                        % (q[:30], SHORT_RULING))
    if errs:
        return errs
    return verify_rulings(blocks, cfg)


# ---------------------------------------------------------------- the decision
def build_deny(reason, cap=6000):
    if len(reason) > cap:
        reason = reason[:cap] + " ...(truncated)"
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                   "permissionDecisionReason": "build_answer_gate: " + reason}}


def decide(raw, inject_error=False):
    """Returns (verdict, reason, logrec). verdict in allow|deny."""
    rec = {"ts": now_utc().isoformat(timespec="milliseconds"), "tool": None, "target": None, "header": None,
           "kind": None, "verdict": "allow", "reason": "", "session": None, "message_sha": None}
    cfg, cfg_err = None, None
    try:
        cfg = load_config(Opts.config)
    except Exception as e:
        cfg_err = "%s: %s" % (type(e).__name__, e)
    reg = read_registry(Opts.registry_glob)
    members = idlike = None
    if cfg is not None:
        members, idlike = resolve_set(cfg["gated_targets"], cfg["aliases"], reg)
        write_needles(Opts.needles, members, idlike)
    if inject_error:
        raise RuntimeError("injected error")
    try:
        d = json.loads(raw)
    except Exception:
        d = None
    if not isinstance(d, dict):
        return _malformed(rec, raw, cfg, reg, members, idlike, "hook input is not a JSON object")
    rec["tool"] = d.get("tool_name") if isinstance(d.get("tool_name"), str) else None
    ti = d.get("tool_input")
    sender = d.get("session_id")
    rec["session"] = sender if isinstance(sender, str) else None
    if rec["tool"] not in TOOLS or not isinstance(ti, dict):
        return _malformed(rec, raw, cfg, reg, members, idlike, "unknown tool or tool_input is not an object")
    tvals = [ti.get(k) for k in ("to", "recipient", "session_id") if k in ti and ti.get(k) is not None]
    if any(not isinstance(v, str) for v in tvals):
        return _malformed(rec, raw, cfg, reg, members, idlike, "a target field is not a string")
    rec["target"] = ti.get("to") if isinstance(ti.get("to"), str) else (tvals[0] if tvals else None)
    if cfg is not None:
        gated = any(is_gated(v, members, idlike) for v in tvals)
    else:
        gated = any(shape_gated(v, reg) for v in tvals)
    # `message` is the text the recipient gets. `content` is added by the harness (in logged transcripts it is a
    # truncated preview of `message`), so it is only a fallback when `message` is absent.
    msg = ti.get("message")
    if msg is None:
        msg = ti.get("content")
    if isinstance(msg, str):
        rec["message_sha"] = sha16(msg)
        rec["header"] = msg.split("\n", 1)[0][:200]
    if not gated:
        rec["reason"] = "not a gated target"
        return "allow", rec["reason"], rec
    if cfg is None:
        rec["reason"] = "config unusable: " + cfg_err
        return _deny(rec, "the gate config %s is unusable (%s). The target looks like a session address, so the send "
                          "is blocked until the config is repaired." % (Opts.config, cfg_err))
    sset = cfg.get("gated_senders") or []
    if sset:
        smem, sid = resolve_set(sset, [], reg)
        if isinstance(sender, str) and sender.strip() and not (norm_target(sender) in smem or norm_target(sender) in sid):
            rec["reason"] = "sender is not a gated sender"
            return "allow", rec["reason"], rec
    if not isinstance(msg, str):
        return _deny(rec, "the message field is missing or not a string; send text with a first-line `GATE:` header. "
                          + ACCEPTED_FORMS)
    if msg == "" and ti.get("notify_when_idle") is True:
        rec["kind"] = "NOTIFY"
        rec["reason"] = "empty idle notification"
        return "allow", rec["reason"], rec
    first, _, body = msg.partition("\n")
    errs = []
    if RE_ANS_HDR.fullmatch(first):
        rec["kind"] = "ANSWER"
        pairs = []
        for tok in first.split(" ")[2:]:
            f, _, idpart = tok.rpartition("#")
            for i in idpart.split(","):
                pairs.append((f, i))
        if len(set(pairs)) != len(pairs) or len({i for _, i in pairs}) != len(pairs):
            errs.append("an answer id is listed twice in the header")
        elif len(pairs) > 20:
            errs.append("more than 20 ids in one header")
        else:
            used = []
            errs = check_answer(cfg, pairs, body, sender if isinstance(sender, str) else None, used)
            if used:
                rec["agents"] = used
    elif first in SIMPLE_KINDS:
        rec["kind"] = SIMPLE_KINDS[first]
        if rec["kind"] == "QUESTION":
            rec["message"] = msg   # a decision can hide in a question: keep the full text
    elif first == "GATE: OWNER-RULING":
        rec["kind"] = "OWNER-RULING"
        errs = check_owner_ruling(body, cfg)
    else:
        errs = ["the first line %r is not a valid gate header. " % first[:80] + ACCEPTED_FORMS]
    if errs:
        return _deny(rec, "blocked %s to the build lane. %d problem(s): " % (rec["kind"] or "message", len(errs)) +
                     " || ".join(errs) + ("" if any("Accepted first lines" in e for e in errs) else " || Reminder: " + ACCEPTED_FORMS))
    rec["reason"] = "ok"
    return "allow", "ok", rec


def _deny(rec, reason):
    rec["verdict"] = "deny"
    rec["reason"] = reason[:1500]
    return "deny", reason, rec


def _malformed(rec, raw, cfg, reg, members, idlike, why):
    if gated_looking_raw(raw, cfg, reg, members, idlike):
        return _deny(rec, "malformed hook input (%s) that mentions the gated lane; blocked." % why)
    rec["reason"] = "malformed input, not gated-looking: " + why
    return "allow", rec["reason"], rec


def hook_main():
    raw = sys.stdin.buffer.read().decode("utf-8", "replace")
    try:
        verdict, reason, rec = decide(raw, Opts.inject_error)
    except BaseException as e:
        rec = {"ts": now_utc().isoformat(timespec="milliseconds"), "tool": None, "target": None, "header": None,
               "kind": None, "verdict": "allow", "reason": "", "session": None}
        try:
            cfg = load_config(Opts.config)
        except Exception:
            cfg = None
        try:
            looks = gated_looking_raw(raw, cfg, read_registry(Opts.registry_glob))
        except BaseException:
            looks = bool(SHAPE_RE.search(raw))
        if looks:
            verdict, reason = "deny", "hook error (%s: %s) on a message that looks addressed to the gated lane; " \
                                      "blocked (fail closed)." % (type(e).__name__, e)
            rec["verdict"], rec["reason"] = "deny", "hook error: %s: %s" % (type(e).__name__, e)
        else:
            verdict, reason = "allow", "hook error on a non-gated message"
            rec["reason"] = "hook error (ungated): %s: %s" % (type(e).__name__, e)
    append_log(Opts.log, rec)
    if verdict == "deny":
        sys.stdout.write(json.dumps(build_deny(reason)))
        sys.stdout.flush()
        return 10
    return 0


# ---------------------------------------------------------------- helper modes
def _one_block(path, ident):
    cfg = load_config(Opts.config)
    text, err = load_record(path, cfg)
    if err:
        return None, None, "error: %s" % err
    blocks = parse_record(text)["blocks"].get(ident, [])
    if len(blocks) != 1:
        return None, None, "error: expected exactly one ANSWER %s block, found %d" % (ident, len(blocks))
    return text, blocks[0], None


def cmd_sha(args):
    text, block, err = _one_block(args[0], args[1])
    if err and len(args) > 1:       # not an ANSWER id: maybe a trio question block `TRIO <name> BEGIN ... END`
        try:
            cfg = load_config(Opts.config)
            qtext, qerr = load_record(args[0], cfg)
            qh, qerr2 = trio_question(parse_record(qtext), args[1]) if not qerr else (None, qerr)
        except Exception:
            qh = None
        if qh:
            print(qh)
            return 0
    if err:
        print(err)
        return 1
    print(text_hash(block))
    return 0


def _refuse(msg):
    print("refused: " + msg)
    return 1


def cmd_stamp(args):
    if len(args) < 4:
        print("usage: stamp [--session ID] <record> <id> <compliance|redteam|trio> <RESULT>   (session: --session, else env CLAUDE_CODE_SESSION_ID)")
        return 2
    path, ident, kind, result = args[:4]
    text, block, err = _one_block(path, ident)
    if err:
        print(err)
        return 1
    h = text_hash(block)
    ts = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    if kind == "trio":
        tm = TRIO_RE.search(block)
        if not tm:
            print("error: this answer has no TRIO:<name> tag")
            return 1
        line = "CHECK %s trio %s %s sha=%s" % (ident, result, ts, h)
        m = RE_TRIO.fullmatch(line)
    elif kind == "compliance":
        line = "CHECK %s compliance %s %s sha=%s" % (ident, result, ts, h)
        m = RE_COMP.fullmatch(line)
    elif kind == "redteam":
        line = "CHECK %s redteam %s %s sha=%s" % (ident, result, ts, h)
        m = RE_RT.fullmatch(line)
    else:
        print("error: kind must be compliance|redteam|trio")
        return 2
    if not m:
        print("error: the line would be malformed (results: compliance PASS|FAIL|HELD, redteam CLEAN|MINOR|MAJOR|BLOCKER, "
              "trio DONE): %s" % line)
        return 1
    cfg = load_config(Opts.config)
    env_session = os.environ.get("CLAUDE_CODE_SESSION_ID")
    session = Opts.session or env_session
    if not session:
        return _refuse("no session id: pass --session <id> or run inside the Claude Code session (env CLAUDE_CODE_SESSION_ID); the stamp "
                       "needs a cold agent's transcript of this session")
    if Opts.session and env_session and Opts.session != env_session:
        sys.stderr.write("warning: --session differs from CLAUDE_CODE_SESSION_ID; the send check uses the sending session's own id\n")
    if kind == "trio":
        qh, qerr = trio_question(parse_record(text), tm.group(1))
        if qerr:
            return _refuse(qerr)
        try:
            agents, stats = scan_agents(cfg, session, [qh])
        except ScanTimeout as e:
            return _refuse("the evidence scan did not finish within %d s (cold disk cache?); run it again, the files read are cached now" % e.args[0])
        judges = sorted((a for a in agents if a["trio"].get(qh)), key=lambda a: a["ts"])[-3:]
        if len(judges) < 3:
            return _refuse("a trio needs three distinct qualifying judges; found %d. %s" % (len(judges), no_evidence_message(qh, "trio", stats, session)))
        if trio_majority([a["trio"][qh] for a in judges]) is None:
            return _refuse("the three judges have no majority answer: %r" % [a["trio"][qh] for a in judges])
        line += " agents=" + ",".join(a["agent"] for a in judges)
        m = RE_TRIO.fullmatch(line)
    else:
        try:
            agents, stats = scan_agents(cfg, session, [h])
        except ScanTimeout as e:
            return _refuse("the evidence scan did not finish within %d s (cold disk cache?); run it again, the files read are cached now" % e.args[0])
        label = KIND_LABEL[kind]
        cand = [(a, a["verdicts"][(h, label)]) for a in agents if (h, label) in a["verdicts"]]
        if not cand:
            return _refuse(no_evidence_message(h, kind, stats, session))
        ok = [a for a, v in cand if rank(kind, v) <= rank(kind, result)]
        if not ok:
            return _refuse("every qualifying agent gave a better verdict than %s (%s): a stamp may be the agent's verdict or a worse one"
                           % (result, ", ".join("%s said %s" % (a["agent"], v) for a, v in cand)))
        line += " agent=%s" % max(ok, key=lambda a: a["ts"])["agent"]
        m = (RE_COMP if kind == "compliance" else RE_RT).fullmatch(line)
    if not m:
        return _refuse("internal: the stamped line would be malformed: %s" % line)
    real = os.path.realpath(expand(path))
    with open(real, "a", encoding="utf-8") as f:
        if not text.endswith("\n"):
            f.write("\n")
        f.write(line + "\n")
    print("stamped: " + line)
    return 0


def main(argv):
    args = []
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--config":
            Opts.config = argv[i + 1]; i += 2
        elif a == "--log":
            Opts.log = argv[i + 1]; i += 2
        elif a == "--needles":
            Opts.needles = argv[i + 1]; i += 2
        elif a == "--registry-glob":
            Opts.registry_glob = argv[i + 1]; i += 2
        elif a == "--scan-budget":
            Opts.scan_budget = float(argv[i + 1]); i += 2
        elif a == "--inject-error":
            Opts.inject_error = True; i += 1
        elif a == "--session":
            Opts.session = argv[i + 1]; i += 2
        else:
            args.append(a); i += 1
    mode = args[0] if args else "hook"
    if mode == "hook":
        return hook_main()
    if mode == "sha":
        return cmd_sha(args[1:])
    if mode == "stamp":
        return cmd_stamp(args[1:])
    print("unknown mode %s" % mode)
    return 2


if __name__ == "__main__":
    try:
        rc = main(sys.argv)
    except BaseException as e:  # a crash must never look like an allow: exit code 70 = crash for the wrapper
        sys.stderr.write("build_answer_gate crash: %s: %s\n" % (type(e).__name__, e))
        rc = 70
    sys.exit(rc)
