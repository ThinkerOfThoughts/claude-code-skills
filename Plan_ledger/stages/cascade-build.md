# Cascade build questions — plan-ledger stage 7 in cascade mode

A builder's question is answered by the full procedure used for a level (`stages/cascade-levels.md` steps b to e), because an answer to it is a design line and is held to the same pass rule: it meets every principle and prior decision (`stages/cascade-method.md` "Compliance"). There is no reduced path: nothing is skipped because the question is small, urgent, or from the builder, and no step has a build-time exemption. Messages from the builder are still logged in the Coordination log and not relayed to the owner in pieces. For each question, or each group of questions that arrive together:
1. **Answerable from the spec by line:** answer with the line reference and nothing else (unchanged from stage 7), but only when the cited line itself states the answer, including every operation the answer needs (read, write, delete, ...). A line that is silent on any of them is not an answer: go to step 2 and fix the spec wording afterwards.
2. **Otherwise** look it up and derive it (`stages/cascade-method.md` "Order of work"), with facts (saved in `cascade.records_dir`) naming the existing shared mechanism for each operation the answer needs. Write the answer as derived lines, each operation naming its shared mechanism or stating that none exists. If it is non-obvious, run the trio (step b).
3. **Compliance check (step c):** record the answer's lines with their citation and confidence and run the compliance check on them (questions that arrive together are checked together); route failures as step c says; fix the spec wording.
4. **Gap red-team (step d):** spawn `stages/role-gap-redteam.md` as step d says, with the build question's lines as "the level draft", the candidate build batch as "the candidate batch", and the changes to earlier lines since their last red-team. Route its findings as step d says.
5. **Relay** the answer and the spec line to the builder only after the latest compliance check says PASS with a valid provenance tag and the latest red-team is clean (or its findings are fixed and re-checked), or the owner has answered.
6. **Gap or always-to-owner:** hold it for a build batch in the layout of step e (its hard gate applies; the red-team of step 4 audits the candidate batch, and anything added afterwards is tested at assembly), and post it as soon as the builder is blocked on an item in it, with everything accumulated; otherwise at the next milestone. Owner rulings are relayed to the builder as stage 7 says (verbatim, with the timestamp, acknowledged back).
7. **Review:** build-time M lines go on the build batch's review list; H lines are listed by id in the ledger at each milestone.
8. **Pile-up:** update the tally on every derived answer. Before each build batch and at close, run the compliance check over all the build-time derived lines together, because each passes its own check and the pile is what the owner never saw. A `PILING UP` verdict is handled as `stages/cascade-method.md` "Pile-up" says.
A builder's self-resolution reported after the fact is still recorded as `[PROPOSED:<lane> | UNCONFIRMED]` (stage 7) and goes through steps 3 and 4 before it counts as derived.


## Gate record format (enforced by the build_answer_gate hook)

The planning lane's own `send_message` / `SendMessage` to the build lane is checked by the PreToolUse hook `~/.claude/hooks/build_answer_gate.py` (registered in `~/.claude/settings.json`; config `build_answer_gate.config.json` beside it). It is a guard against skipped review steps, not against deliberate forgery: it checks that the saved records say the steps were done for the exact text being sent, and it does not check that a cold agent really ran. Every send is logged in `~/.claude/hooks/build_answer_gate.log.jsonl` (a QUESTION in full). **A file handoff cannot be gated by a send hook:** if the builder is told to read a doc instead, the hook never sees it, and the same steps 3 to 5 still apply.

**First line of every message to the build lane (exact, nothing before it, no blank line first).** One of:
- `GATE: ANSWER <file>#<id>[,<id>...] [<file>#<id>...]` (a build answer; `<file>` is the record file, absolute or `~/...`, under `~/.claude/plans/`, at most 25 000 bytes, no spaces in the path)
- `GATE: ACK`, `GATE: MILESTONE`, `GATE: QUESTION` (any body; the hook does not test it. Do not put answer content in these: that is the planning lane's rule, not the hook's.)
- `GATE: OWNER-RULING`: the body holds only `> <the owner's words>` lines. Each quote must appear word for word (whitespace aside) in one human-typed turn of the project transcripts, or in the owner's own answer to an AskUserQuestion (the selected option or the typed text, not the question or the other options the assistant wrote). It is not usable for a peer message or any other tool result. A ruling of 7 characters or fewer ("ok", "yes") must be the whole turn or the whole answer and must be followed by a line `re: <the question it answered, 10 characters or more>`, which must appear in what the assistant showed just before that turn (for a widget answer: in that answer's own question).

A message without one of these first lines is blocked.

**Record file.** For each answer id, an `ANSWER` block holding the answer exactly as it is relayed, then one `CHECK` line per step. The last line per id and step decides. A `CHECK` line counts only when its `sha` equals the hash of the block as it is now, so any edit to the answer makes every earlier check stale and each step is re-run on the new text. Write the lines with the helper, which computes the hash and the time:

`python3 ~/.claude/hooks/build_answer_gate.py sha <file> <id>` prints the current hash.
`python3 ~/.claude/hooks/build_answer_gate.py stamp <file> <id> compliance PASS|FAIL|HELD`, `... redteam CLEAN|MINOR|MAJOR|BLOCKER`, `... trio DONE`.

The hook allows an `ANSWER` message only when, for every id in the header: the record file exists; the block exists exactly once; the compliance line is `PASS`; the red-team line is `CLEAN` or `MINOR` (a `MAJOR` or `BLOCKER` is still open); a trio line exists when the answer carries a `TRIO:<name>` tag; and the message body is, in header order, `<id>:` then the block text exactly, blocks separated by one blank line, nothing else.

```gate-record
ANSWER Q1 BEGIN
Q1 (where the wiring test lives): the new test goes in the existing test module that holds the neighbouring full-open tests, not in a new module. [RULE: P7 (reuse the existing test block) | TRIO:Tq | M, REVIEW]
ANSWER Q1 END
CHECK Q1 compliance PASS 2026-11-03T16:05:00-05:00 sha=21a6f9033a60dbfe
CHECK Q1 redteam MINOR 2026-11-03T16:12:00-05:00 sha=21a6f9033a60dbfe
CHECK Q1 trio DONE 2026-11-03T16:02:00-05:00 sha=21a6f9033a60dbfe
```

Run `stamp` for a step only after the step has been run on the current text (steps 3, 4 and the trio in step 2 above).
