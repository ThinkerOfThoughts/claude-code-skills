# Hooks

Reference implementations of the Claude Code hooks that back these skills, plus a
standalone git-workflow guard. Each is stdlib-only Python and reads the hook event as JSON on
stdin. All fail open (never crash the tool they gate) except `build_answer_gate.py`, which fails
closed for the lane it gates (a crash on a message addressed to that lane denies it). Wire them in
`~/.claude/settings.json` (see snippet below).

| Hook | Event(s) | What it does |
|------|----------|--------------|
| `read_gate.py` | `PreToolUse` (Edit/Write/MultiEdit) + `PostToolUse` (Read/Bash) | **Read-before-edit gate** for `*-brief.md` / `*-spec.md` / `*-LEDGER.md` / `*-HANDOFF.md`. Denies editing one of these that has not been read in this session since the last compaction, so a spec/ledger/handoff is never edited (or quoted) from stale memory. Backs the **plan-ledger** skill. |
| `compact_reinject.py` | `SessionStart` (matcher `compact`, and a second entry `startup\|resume`) | **Post-compaction re-injection.** A compaction drops the standing rules a session was following; this prints a short reminder block back into context and flags any `status: ACTIVE` ledger so the session re-invokes plan-ledger and re-reads it. It also records when the compaction happened, which `read_gate.py` uses to require a *post-compaction* re-read. It also prints one line, while the overnight-run presence marker `~/.claude/hooks-state/overnight-run-active` exists, pointing the session back into the **overnight-run** skill: on `compact` after the reminder block, on `startup` and `resume` alone (no reminder block and no compaction marker, nothing if the marker is absent); `clear`, any other source, and a session with `OVERNIGHT_EGGTIMER_PING=1` in its environment get nothing. Tests: `test_compact_reinject.py`. Backs the **plan-ledger** skill and the **overnight-run** skill. |
| `branch_guard.py` | `PreToolUse` (Bash) | **Branch-target guard.** Stops fix-work from landing on the wrong branch: denies branch **creation** (showing the repo's open PRs, so a fix that belongs in an open PR isn't stacked on a new branch) and denies cross-branch commit/file **moves** (cherry-pick / rebase --onto / format-patch\|am / cross-ref extraction). It denies to the *agent* and is cleared per-command by re-issuing with a `BRANCH_GUARD_ACK="<reason>"` prefix. Routine commits, rebases onto an upstream, listing and status are not flagged. Standalone — not tied to a skill. |
| `build_answer_gate.py` (+ `build_answer_gate.sh`) | `PreToolUse` (`send_message` / `SendMessage`) | **Cold-check gate for answers sent to a build lane.** A planning lane may relay a build answer only when its record file shows (1) a cold **second full review** of the answer by **both** reviewers of the pair (the compliance checker and the gap red-team), each following a cold **first** full review of the same answer by that reviewer, and (2) a cold **fix check on every line changed since the second review**; text the second review saw, with nothing changed since, is allowed as it is (and a trio when the answer cites one). Any edit therefore no longer voids every earlier check; it needs a fix check on the lines it changed. **Record format:** `REVIEWED <id> <sha> BEGIN` ... `END` holds the text a full review saw (one block per distinct sha, written by `stamp`; its hash must equal the sha the review lines cite); `CHECK <id> review1\|review2 compliance\|redteam <ts> sha=<sha> agent=<A>`; `CHECK <id> fixcheck <ts> lines=<l16>,... agent=<A>`; the trio line as before. A line is a non-blank line of the block ("the same answer" is the same record id), its hash is the module's `text_hash` of it, and the changed lines are the lines of the current block outside the equal runs of a difflib diff of the reviewed text against it (a moved line is changed; a deletion changes the lines on each side of it; blank-line edits are invisible). Each line must be backed by a cold subagent's own transcript, written by Claude Code under `<project>/<session>/subagents/`, and the send check re-reads it: the agent is a non-fork of this session, its prompt holds the 16-hex hash (a review: the hash of the text it reviewed; a fix check: the hash of each line it checked), it received no input after its prompt, and it ended its final message with the closing lines: `<id> hash=<block hash> COMPLIANCE: FIRST\|SECOND` or `REDTEAM: FIRST\|SECOND` (a full review, no pass verdict; the id must be this answer's), `<id> hash=<line hash> FIXCHECK: PASS\|FAIL` (one per checked line), `<id> hash=<question hash> TRIO: <answer>` (a trio judge; three judges and a majority, unchanged). Order: the latest second review of each reviewer has an earlier first review of that reviewer by a different agent that finished before the second one started (a missing start time fails closed), the two reviewers' second reviews are different agents, and a fix check counts only when its agent started after the second review finished. A review is stamped right after it returns, before the answer is edited. **Not enforced:** that an answer whose second review blocked went to the owner first (the hook cannot see that post), how many full reviews ran or how many fix attempts a finding took, edits that only change blank lines, and a second review stamped again on edited text (the latest one decides and its text becomes the baseline). A record in the old format (`CHECK <id> compliance\|redteam <VERDICT> ... sha=...`) is not read: the send is denied with a message saying how to re-check. An agent whose prompt tells it the result should end with `REFUSED` (one sentence in its role brief) and never qualifies. It guards against skipped checks, not against a hand-forged transcript file. Backs the **plan-ledger** skill's cascade mode (`Plan_ledger/stages/cascade-build.md`). Tests: `test_build_answer_gate.py` + `test_fixtures/`. Config: copy `build_answer_gate.config.example.json` to `build_answer_gate.config.json` beside the script and fill in the lane ids. |
| `narration_guard.py` | `Stop` (declared in the overnight-run skill's frontmatter, not settings.json) | **Narration guard for unattended runs.** While the presence marker `~/.claude/hooks-state/overnight-run-active` exists, blocks the stop once (a deterrent, not a filter) when the turn wrote any text other than the one fixed placeholder line and neither the turn's starting prompt nor a message that arrived mid-turn was typed by the owner; the block reason tells the model to put owner items on the morning list and end the turn with the placeholder line and nothing else (the placeholder is defined once in the hook and quoted in the skill's `stages/common.md`). Imports `plain_human_text` from `build_answer_gate.py` (keep the two side by side), reads the transcript backwards from its end, and fails open on any error. Tests: `test_narration_guard.py` (synthetic transcripts only). Backs the **overnight-run** skill. |

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
      },
      {
        "matcher": "startup|resume",
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
out. Stamping: `python3 ~/.claude/hooks/build_answer_gate.py stamp [--session ID] <record> <id> review1|review2 compliance|redteam`,
`... <id> fixcheck` (writes one line per fix-check agent for the lines `sha <record> <id> changed` lists) and `... <id> trio DONE`;
`sha <record> <id>` prints the block hash (the hash to hand a reviewer) and `sha <record> <id> changed` the changed lines;
the session comes from `--session` or `CLAUDE_CODE_SESSION_ID`. `stamp` applies the send check's order and distinct-agent conditions and
refuses to append past `max_record_bytes`. The old `compliance|redteam` kinds are refused. Run the tests with
`python3 test_build_answer_gate.py`.)

## Notes / defaults you may want to adjust

- `compact_reinject.py` (the `compact` source) looks for active ledgers in `~/.claude/plans/*-LEDGER.md` and the
  session cwd; point it at your own `ledger_dir` if it differs. Its reminder block encodes a
  particular set of working rules — edit `REMINDER_BLOCK` to match yours. The `startup|resume`
  entry is only needed for the overnight-run skill; without the run marker it prints nothing.
- `read_gate.py`'s gated globs (`*-brief.md`, `*-spec.md`, `*-LEDGER.md`, `*-HANDOFF.md`) are
  set in `GATED_PATTERNS`.
- `branch_guard.py` applies to every git repo. To scope it, gate on the origin remote at the
  top of `main()`. The open-PR list needs `gh` authenticated; without it the branch-creation
  gate still fires, just without the list.
- `build_answer_gate.py` needs its config (lane ids, `transcript_glob` of your project's session
  transcripts, `allowed_record_dirs`); see the example file. Every `CHECK` line written without an
  agent id is rejected at send, and records in the old format need re-checking by fresh cold agents.
  `max_record_bytes` (default 597,800, derived in the module from an assumed 20 ids per record file, answers of at most
  3,000 bytes and 30 lines, 4 reviewed texts, 4 review lines, at most 2 fix attempts per line and a trio) bounds the
  whole-file read made at every send; it was 25,000 before the second-review condition. The default applies only when
  the key is absent: a config copied from the old example still carries 25,000, which a record with several answers
  and their reviewed texts can exceed (`stamp` then refuses and the send is denied as too large), so raise or remove
  the key in an existing `build_answer_gate.config.json`.
