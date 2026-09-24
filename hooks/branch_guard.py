#!/usr/bin/env python3
"""Branch-target guard — stop fix-work from landing on the wrong branch.

The failure this prevents: you have an open (unmerged) draft PR, you notice a defect in it,
and you fix the defect on a NEW branch stacked on top instead of committing the fix INTO the
PR's own branch. That is the entire point of a branch: to do the work in. The stray branch
then has to be folded back later — surgery that should never have been needed. A fix for an
open PR belongs in that PR's branch from the start.

This guard triggers the AGENT (not a human) to check the branch target, and it BLOCKS by
default. A non-blocking warning, or one that asks a human to confirm, is worthless: given the
volume of git operations an agent runs, a human gets flooded and rubber-stamps, and the agent
sails past a soft warning. So it mirrors a read-before-edit gate: DENY the action and feed the
reasoning back to the model; the agent clears the gate only by a deliberate re-issue once it
has actually verified the target.

  FRONT-LINE  — on branch CREATION, deny and show the repo's open PRs, forcing the agent to
                confirm this branch is genuinely NEW work, not a fix that belongs IN one of
                those PRs.
  BACKSTOP    — on a cross-branch commit/file MOVE (cherry-pick / rebase --onto /
                format-patch | am / cross-ref file extraction), deny and surface the red flag:
                if this is folding a fix back into the branch it should have started on, the
                fix was on the wrong branch. That question should never need to arise.

CLEARING THE GATE (the deliberate agent confirmation): re-run the SAME command with an
acknowledgment env-var prefix stating why, e.g.
    BRANCH_GUARD_ACK="new work, not a fix for any open PR" git checkout -b <name>
    BRANCH_GUARD_ACK="sanctioned fold, already diagnosed" git cherry-pick <sha>
git ignores the unknown env var, so behaviour is unchanged and the ack is auditable in the
command. The ack is per-command: the agent must consciously re-issue after checking.

Only branch creation and cross-branch moves trip it — routine commits, `git rebase <branch>`
onto an upstream, listing, status, etc. are NOT flagged, so it stays quiet despite applying to
every git repo. The FRONT-LINE open-PR list comes from `gh pr list` in the command's cwd (gh
infers the repo); an empty/unavailable list is fine — the gate still fires, just without a list.

Wire it as a PreToolUse hook on the Bash matcher (see hooks/README.md). Conventions: stdlib
only, defensive parsing, and it must NEVER crash a git command — any exception falls back to
silent allow.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys


# The agent's deliberate acknowledgment that clears the gate for one command.
_ACK_RE = re.compile(r"\bBRANCH_GUARD_ACK=")

# FRONT-LINE: this command CREATES a new branch.
_BRANCH_CREATE_RES = (
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?checkout\s+(?:[^&|;]*\s)?-[bB]\b"),
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?switch\s+(?:[^&|;]*\s)?-[cC]\b"),
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?worktree\s+add\b[^&|;]*\s-[bB]\b"),
)
# `git branch <name>` that is a creation (not -d/-D/-m/-M/--list/-a/-r/--merged/--contains…).
_BRANCH_PLAIN_RE = re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?branch\s+(?P<rest>[^&|;]*)")
# capture the created name after -b/-c/-B/-C for the message (best-effort).
_CREATED_NAME_RE = re.compile(
    r"\b(?:checkout|switch)\s+(?:[^&|;]*\s)?-[bBcC]\s+(?P<name>[^\s&|;]+)"
)

# BACKSTOP: this command MOVES commits/files across branches.
_CROSS_MOVE_RES = (
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?cherry-pick\b"),
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?rebase\s+[^&|;]*--onto\b"),
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?format-patch\b"),
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?am\b"),
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?restore\s+[^&|;]*--source\b"),
    # git checkout/switch <ref> -- <path>  (pull files out of another ref)
    re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?(?:checkout|switch)\s+[^&|;]*\s--\s"),
)

_ACK_HINT = (
    " To proceed once you have CHECKED and confirmed the target is correct, re-run the same "
    'command with an acknowledgment prefix stating why, e.g. BRANCH_GUARD_ACK="<reason>" '
    "<your git command>."
)


def _read_stdin_json() -> dict:
    raw = sys.stdin.read()
    if not raw:
        return {}
    data = json.loads(raw)
    return data if isinstance(data, dict) else {}


def _is_plain_branch_create(command: str) -> bool:
    m = _BRANCH_PLAIN_RE.search(command)
    if not m:
        return False
    rest = m.group("rest").strip()
    if not rest:
        return False  # bare `git branch` = list
    first = rest.split()[0]
    if first.startswith("-"):
        return False  # a flag (list/delete/move/copy) = not a creation
    return True  # `git branch <name> [<start-point>]` = creation


def _open_prs(cwd: str) -> list[str]:
    """Best-effort open-PR list for the cwd's repo (gh infers it); [] on any failure."""
    try:
        env = dict(os.environ, GH_PAGER="cat")
        out = subprocess.run(
            ["gh", "pr", "list", "--state", "open",
             "--json", "number,headRefName,title"],
            capture_output=True, text=True, timeout=6, cwd=cwd or ".", env=env,
        )
        rows = json.loads(out.stdout or "[]")
    except Exception:
        return []
    lines = []
    for r in rows if isinstance(rows, list) else []:
        try:
            lines.append(f"  #{r['number']}  [{r['headRefName']}]  {r['title']}")
        except Exception:
            continue
    return lines


def _deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))


def main() -> int:
    data = _read_stdin_json()
    if (data.get("tool_name") or "") != "Bash":
        return 0
    tool_input = data.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        return 0
    command = tool_input.get("command")
    if not isinstance(command, str) or "git" not in command:
        return 0
    # Deliberate agent acknowledgment clears the gate for this command.
    if _ACK_RE.search(command):
        return 0
    cwd = data.get("cwd") or ""

    # BACKSTOP first (a cross-move is the more dangerous, more specific signature).
    if any(rx.search(command) for rx in _CROSS_MOVE_RES):
        _deny(
            "BACKSTOP — cross-branch commit/file move detected. STOP and check: if you are "
            "folding a fix back into the branch it should have started on, that fix was on "
            "the WRONG branch — this is exactly the structural error this guard exists to "
            "catch. A fix for an open draft PR belongs IN that PR's branch from the start; it "
            "should never need to be moved back. Only proceed if this cross-branch move is "
            "genuinely intended (e.g. a sanctioned fold you have already diagnosed)." + _ACK_HINT
        )
        return 0

    # FRONT-LINE: branch creation.
    creating = any(rx.search(command) for rx in _BRANCH_CREATE_RES) or _is_plain_branch_create(command)
    if creating:
        m = _CREATED_NAME_RE.search(command)
        newname = m.group("name") if m else "the new branch"
        prs = _open_prs(cwd)
        pr_block = ("\nOpen PRs in this repo right now:\n" + "\n".join(prs)) if prs else ""
        _deny(
            f"FRONT-LINE — creating a new branch ({newname}). STOP and check the target: if "
            f"this branch's work FIXES or REVISES an open PR, it does NOT belong on a new "
            f"branch — do the work IN that PR's branch (that is the entire point of a branch, "
            f"to do the work in). Only proceed if this is genuinely NEW, independent "
            f"work.{pr_block}" + _ACK_HINT
        )
        return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Never crash a git command on the guard's own failure — fall back to allow.
        sys.exit(0)
