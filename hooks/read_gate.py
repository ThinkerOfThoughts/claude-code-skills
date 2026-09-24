#!/usr/bin/env python3
"""Read-before-edit gate for spec/brief/ledger/handoff files.

Two modes, selected by argv[1]:

  mark   PostToolUse hook (matcher "Read|Bash"). Records that a gated file was just read,
         so a later edit of it is allowed. Never blocks; never prints to stdout.

  check  PreToolUse hook (matcher "Edit|Write|MultiEdit"). Denies editing a gated file that
         has not been read in THIS session since the LAST compaction (or at all), per the
         global rule "before quoting/editing a file, re-read the relevant part now."

Gated files are matched on basename only (case-sensitive glob): *-brief.md, *-spec.md,
*-LEDGER.md, *-HANDOFF.md.

State lives under ~/.claude/hooks-state/<session_id>/:
  read/<sha1(abs path)>   epoch time of the most recent read of that file, this session
  compacted               epoch time compact_reinject.py last ran, this session

Conventions: stdlib only, defensive parsing. This hook must NEVER block on its own
failure — any exception anywhere falls back to silent allow (exit 0, no output).
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import re
import sys
import time


GATED_PATTERNS = ("*-brief.md", "*-spec.md", "*-LEDGER.md", "*-HANDOFF.md")

DENY_REASON_TEMPLATE = (
    "read-gate: {basename} is a spec/brief/ledger/handoff file and has not been read in "
    "this session since the last compaction (or at all). Read the relevant part of the "
    "file first (Read tool, or cat/sed via Bash), then retry the edit. Rule: never edit or "
    "quote a file from memory."
)

# A loose "looks like a markdown path" token matcher for scanning Bash commands: a run of
# non-whitespace/quote characters ending in ".md".
_MD_TOKEN_RE = re.compile(r"""[^\s"'`]+\.md""")


def _read_stdin_json() -> dict:
    raw = sys.stdin.read()
    if not raw:
        return {}
    data = json.loads(raw)
    return data if isinstance(data, dict) else {}


def _is_gated(path: str) -> bool:
    basename = os.path.basename(path)
    return any(fnmatch.fnmatchcase(basename, pat) for pat in GATED_PATTERNS)


def _resolve(path: str, cwd: str) -> str:
    path = os.path.expanduser(path)
    if not os.path.isabs(path):
        base = cwd or os.getcwd()
        path = os.path.join(base, path)
    return os.path.normpath(path)


def _state_dir(session_id: str) -> str:
    return os.path.expanduser(os.path.join("~/.claude/hooks-state", session_id or "unknown"))


def _marker_path(session_id: str, abs_path: str) -> str:
    digest = hashlib.sha1(abs_path.encode("utf-8", "surrogateescape")).hexdigest()
    return os.path.join(_state_dir(session_id), "read", digest)


def _write_marker(session_id: str, abs_path: str) -> None:
    marker = _marker_path(session_id, abs_path)
    os.makedirs(os.path.dirname(marker), exist_ok=True)
    with open(marker, "w", encoding="utf-8") as f:
        f.write(str(time.time()))


def _read_float(path: str) -> float | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return float(f.read().strip())
    except Exception:
        return None


def _extract_md_paths_from_command(command: str) -> list[str]:
    if not isinstance(command, str):
        return []
    return _MD_TOKEN_RE.findall(command)


def _deny(basename: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": DENY_REASON_TEMPLATE.format(basename=basename),
        }
    }


def mode_mark() -> int:
    data = _read_stdin_json()
    session_id = data.get("session_id") or "unknown"
    cwd = data.get("cwd") or ""
    tool_name = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        tool_input = {}

    candidate_paths: list[str] = []
    if tool_name == "Read":
        fp = tool_input.get("file_path")
        if isinstance(fp, str) and fp:
            candidate_paths.append(fp)
    elif tool_name == "Bash":
        command = tool_input.get("command")
        candidate_paths.extend(_extract_md_paths_from_command(command))

    for raw_path in candidate_paths:
        abs_path = _resolve(raw_path, cwd)
        if _is_gated(abs_path):
            _write_marker(session_id, abs_path)

    return 0


def mode_check() -> int:
    data = _read_stdin_json()
    session_id = data.get("session_id") or "unknown"
    cwd = data.get("cwd") or ""
    tool_input = data.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        tool_input = {}

    file_path = tool_input.get("file_path")
    if not isinstance(file_path, str) or not file_path:
        return 0  # nothing to gate on; allow

    basename = os.path.basename(file_path)
    if not _is_gated(file_path):
        return 0  # allow silently: not a gated pattern

    abs_path = _resolve(file_path, cwd)

    if not os.path.exists(abs_path):
        return 0  # allow: new file being created (e.g. a fresh Write)

    marker = _marker_path(session_id, abs_path)
    read_time = _read_float(marker) if os.path.exists(marker) else None

    if read_time is None:
        print(json.dumps(_deny(basename)))
        return 0

    compacted_path = os.path.join(_state_dir(session_id), "compacted")
    compacted_time = _read_float(compacted_path) if os.path.exists(compacted_path) else None

    if compacted_time is None or read_time >= compacted_time:
        return 0  # allow: read since last compaction (or no compaction recorded)

    print(json.dumps(_deny(basename)))
    return 0


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "mark":
        return mode_mark()
    elif mode == "check":
        return mode_check()
    else:
        # Unknown mode: fail open, do nothing.
        return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Spec: both modes must never crash the tool call — fall back to allow.
        sys.exit(0)
