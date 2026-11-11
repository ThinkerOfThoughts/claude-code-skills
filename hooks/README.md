# Hooks

Reference implementations of the Claude Code hooks that back these skills, plus a
standalone git-workflow guard. Each is stdlib-only Python and reads the hook event as JSON on
stdin. All fail open (never crash the tool they gate) except `build_answer_gate.py`, which fails
closed for the lane it gates (a crash on a message addressed to that lane denies it). Wire them in
`~/.claude/settings.json` (see snippet below).

| Hook | Event(s) | What it does |
|------|----------|--------------|
| `read_gate.py` | `PreToolUse` (Edit/Write/MultiEdit) + `PostToolUse` (Read/Bash) | **Read-before-edit gate** for `*-brief.md` / `*-spec.md` / `*-LEDGER.md` / `*-HANDOFF.md`. Denies editing one of these that has not been read in this session since the last compaction, so a spec/ledger/handoff is never edited (or quoted) from stale memory. Backs the **plan-ledger** skill. |
| `compact_reinject.py` | `SessionStart` (matcher `compact`) | **Post-compaction re-injection.** A compaction drops the standing rules a session was following; this prints a short reminder block back into context and flags any `status: ACTIVE` ledger so the session re-invokes plan-ledger and re-reads it. It also records when the compaction happened, which `read_gate.py` uses to require a *post-compaction* re-read. Backs the **plan-ledger** skill. |
| `branch_guard.py` | `PreToolUse` (Bash) | **Branch-target guard.** Stops fix-work from landing on the wrong branch: denies branch **creation** (showing the repo's open PRs, so a fix that belongs in an open PR isn't stacked on a new branch) and denies cross-branch commit/file **moves** (cherry-pick / rebase --onto / format-patch\|am / cross-ref extraction). It denies to the *agent* and is cleared per-command by re-issuing with a `BRANCH_GUARD_ACK="<reason>"` prefix. Routine commits, rebases onto an upstream, listing and status are not flagged. Standalone — not tied to a skill. |
| `build_answer_gate.py` (+ `build_answer_gate.sh`) | `PreToolUse` (`send_message` / `SendMessage`) | **Cold-check gate for answers sent to a build lane.** A planning lane may relay a build answer only when its record file shows a compliance PASS and a red-team result with no open MAJOR/BLOCKER for the exact answer text (and a trio when the answer cites one). Each of those `CHECK` lines must be backed by a cold subagent's own transcript, written by Claude Code under `<project>/<session>/subagents/`: `stamp` refuses a verdict unless a non-fork agent of this session, whose prompt holds the answer's 16-hex hash and which received no input after its prompt, ended its final message with `<id> hash=<hash> COMPLIANCE: PASS\|FAIL\|HELD` (or `REDTEAM: CLEAN\|MINOR\|MAJOR\|BLOCKER`); a trio needs three such judges on the question block's hash and a majority. The send check re-reads the recorded agent, so a hand-written `CHECK` line is rejected. An agent whose prompt tells it the verdict should end with `REFUSED` (one sentence in its role brief) and never qualifies. It guards against skipped checks, not against a hand-forged transcript file. Backs the **plan-ledger** skill's cascade mode (`Plan_ledger/stages/cascade-build.md`). Tests: `test_build_answer_gate.py` + `test_fixtures/`. Config: copy `build_answer_gate.config.example.json` to `build_answer_gate.config.json` beside the script and fill in the lane ids. |
| `narration_guard.py` | `Stop` (declared in the overnight-run skill's frontmatter, not settings.json) | **Narration guard for unattended runs.** While the presence marker `~/.claude/hooks-state/overnight-run-active` exists, blocks the stop once (a deterrent, not a filter) when the turn wrote text and neither the turn's starting prompt nor a message that arrived mid-turn was typed by the owner; the block reason tells the model to put owner items on the morning list and end the turn with nothing. Imports `plain_human_text` from `build_answer_gate.py` (keep the two side by side), reads the transcript backwards from its end, and fails open on any error. Tests: `test_narration_guard.py` (synthetic transcripts only). Backs the **overnight-run** skill. |

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

```json
{ "matcher": "mcp__ccd_session_mgmt__send_message|SendMessage",
  "hooks": [ { "type": "command", "command": "sh ~/.claude/hooks/build_answer_gate.sh", "timeout": 35 } ] }
```

(`build_answer_gate.py` ships as a `PreToolUse` entry for the matcher above. Use the `.sh`
wrapper: it denies a message addressed to the gated lane if the script itself crashes or times
out. Stamping: `python3 ~/.claude/hooks/build_answer_gate.py stamp [--session ID] <record> <id> compliance|redteam|trio <RESULT>`;
the session comes from `--session` or `CLAUDE_CODE_SESSION_ID`. Run the tests with
`python3 test_build_answer_gate.py`.)

## Notes / defaults you may want to adjust

- `compact_reinject.py` looks for active ledgers in `~/.claude/plans/*-LEDGER.md` and the
  session cwd; point it at your own `ledger_dir` if it differs. Its reminder block encodes a
  particular set of working rules — edit `REMINDER_BLOCK` to match yours.
- `read_gate.py`'s gated globs (`*-brief.md`, `*-spec.md`, `*-LEDGER.md`, `*-HANDOFF.md`) are
  set in `GATED_PATTERNS`.
- `branch_guard.py` applies to every git repo. To scope it, gate on the origin remote at the
  top of `main()`. The open-PR list needs `gh` authenticated; without it the branch-creation
  gate still fires, just without the list.
- `build_answer_gate.py` needs its config (lane ids, `transcript_glob` of your project's session
  transcripts, `allowed_record_dirs`); see the example file. After installing the evidence rule,
  every `CHECK` line written without an agent id is rejected at send: existing records need
  re-checking by fresh cold agents.
