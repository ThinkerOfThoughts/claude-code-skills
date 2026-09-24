# Hooks

Reference implementations of the Claude Code hooks that back these skills, plus a
standalone git-workflow guard. Each is stdlib-only Python, fails open (never crashes the
tool it gates), and reads the hook event as JSON on stdin. Wire them in
`~/.claude/settings.json` (see snippet below).

| Hook | Event(s) | What it does |
|------|----------|--------------|
| `read_gate.py` | `PreToolUse` (Edit/Write/MultiEdit) + `PostToolUse` (Read/Bash) | **Read-before-edit gate** for `*-brief.md` / `*-spec.md` / `*-LEDGER.md` / `*-HANDOFF.md`. Denies editing one of these that has not been read in this session since the last compaction, so a spec/ledger/handoff is never edited (or quoted) from stale memory. Backs the **plan-ledger** skill. |
| `compact_reinject.py` | `SessionStart` (matcher `compact`) | **Post-compaction re-injection.** A compaction drops the standing rules a session was following; this prints a short reminder block back into context and flags any `status: ACTIVE` ledger so the session re-invokes plan-ledger and re-reads it. It also records when the compaction happened, which `read_gate.py` uses to require a *post-compaction* re-read. Backs the **plan-ledger** skill. |
| `branch_guard.py` | `PreToolUse` (Bash) | **Branch-target guard.** Stops fix-work from landing on the wrong branch: denies branch **creation** (showing the repo's open PRs, so a fix that belongs in an open PR isn't stacked on a new branch) and denies cross-branch commit/file **moves** (cherry-pick / rebase --onto / format-patch\|am / cross-ref extraction). It denies to the *agent* and is cleared per-command by re-issuing with a `BRANCH_GUARD_ACK="<reason>"` prefix. Routine commits, rebases onto an upstream, listing and status are not flagged. Standalone — not tied to a skill. |

## Why these gate the *agent*, and block

The failure modes they guard against (editing a spec from memory; stacking a fix on a new
branch instead of the PR's own) are things an autonomous agent does silently and at volume.
A non-blocking warning gets sailed past; a hook that asks a *human* to confirm floods the
human until they rubber-stamp. So each of these DENIES the tool call and feeds the reasoning
back to the model, which then either does the right thing or clears the gate by a deliberate,
auditable step (re-reading the file; re-issuing with `BRANCH_GUARD_ACK`).

## Wiring (`~/.claude/settings.json`)

Copy the scripts to `~/.claude/hooks/` (or point the commands at wherever you keep them) and
add:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command", "command": "python3 ~/.claude/hooks/read_gate.py check", "timeout": 10 }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "python3 ~/.claude/hooks/branch_guard.py", "timeout": 12 }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Read|Bash",
        "hooks": [
          { "type": "command", "command": "python3 ~/.claude/hooks/read_gate.py mark", "timeout": 10 }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          { "type": "command", "command": "python3 ~/.claude/hooks/compact_reinject.py", "timeout": 10 }
        ]
      }
    ]
  }
}
```

Hook config is snapshotted at session start, so a change here arms for **new** sessions; an
already-running session picks it up only on restart.

## Notes / defaults you may want to adjust

- `compact_reinject.py` looks for active ledgers in `~/.claude/plans/*-LEDGER.md` and the
  session cwd; point it at your own `ledger_dir` if it differs. Its reminder block encodes a
  particular set of working rules — edit `REMINDER_BLOCK` to match yours.
- `read_gate.py`'s gated globs (`*-brief.md`, `*-spec.md`, `*-LEDGER.md`, `*-HANDOFF.md`) are
  set in `GATED_PATTERNS`.
- `branch_guard.py` applies to every git repo. To scope it, gate on the origin remote at the
  top of `main()`. The open-PR list needs `gh` authenticated; without it the branch-creation
  gate still fires, just without the list.
