# Cascade build questions — plan-ledger stage 7 in cascade mode

The review of an answer to a builder's question follows `stages/review-order.md`. Messages from the builder are still logged in the Coordination log and not relayed to the owner in pieces. For each question, or each group of questions that arrive together:
1. **Answerable from the spec by line:** answer with the line reference and nothing else (unchanged from stage 7), but only when the cited line itself states the answer.
2. **Otherwise** the picture check comes before anything is derived (`stages/cascade-method.md` "The picture check"); look it up and derive it (`stages/cascade-method.md` "Order of work"), with facts (saved in `cascade.records_dir`) naming the existing mechanism that does the job, whole or with the smallest change, or that none exists (`stages/cascade-method.md` "Facts"). Write the answer as derived lines. A build answer states what is wanted, where it lives, which existing mechanism it reuses whole, and the owner's constraints, and nothing below that; everything below that is the builder's to work out, and guarded-change's reviews and real tests are the check on it. If it is non-obvious, run the trio (step b).
3. **Compliance check (step c):** record the answer's lines with their citation and confidence and run the compliance check on them (questions that arrive together are checked together); route failures as step c says; fix the spec wording.
4. **Gap red-team (step d):** spawn `stages/role-gap-redteam.md` as step d says, with the build question's lines as "the level draft" and the candidate build batch as "the candidate batch". Route its findings as step d says, and handle its builder notes as `stages/review-order.md` ("Builder notes") says.
5. **Relay** the answer and the spec line to the builder only after the review that `stages/review-order.md` describes is done and the answer carries a valid provenance tag, or the owner has answered.
6. **Gap or always-to-owner:** hold it for a build batch in the layout of step e (its hard gate applies; the red-team of step 4 audits the candidate batch, and anything added afterwards is tested at assembly), and post it as soon as the builder is blocked on an item in it, with everything accumulated; otherwise at the next milestone. A build batch is worded and checked as a level's batch is (the wording rule of step a and steps c to e of `stages/cascade-levels.md`, applied to the batch text): the assembled text gets a batch check, and step 4's red-team is spawned again on that assembled text (it is not enough that it audited the earlier candidate batch) with the four tests of step d, and the batch is reviewed and posted as "Review and post" in step e says (it is not recorded or stamped). Owner rulings are relayed to the builder as stage 7 says (verbatim, with the timestamp, acknowledged back).
7. **Review:** build-time M lines go on the build batch's review list; H lines are listed by id in the ledger at each milestone.
8. **Pile-up:** update the tally on every derived answer. Before each build batch and at close, run the compliance check over all the build-time derived lines together, because each passes its own check and the pile is what the owner never saw. A `PILING UP` verdict is handled as `stages/cascade-method.md` "Pile-up" says.
A builder's self-resolution reported after the fact is still recorded as `[PROPOSED:<lane> | UNCONFIRMED]` (stage 7) and goes through steps 3 and 4 before it counts as derived.


## Gate record format (enforced by the build_answer_gate hook)

The planning lane's own `send_message` / `SendMessage` to the build lane is checked by the PreToolUse hook `~/.claude/hooks/build_answer_gate.py` (config `build_answer_gate.config.json` beside it). It guards against skipped review steps, not against forgery: the saved record must show the review order ran on this answer, and a review, fix-check or trio line is written only from a cold agent's own transcript (below). Every send is logged in `~/.claude/hooks/build_answer_gate.log.jsonl` (a QUESTION in full). **A file handoff cannot be gated by a send hook:** if the builder is told to read a doc instead, the hook never sees it, and the same steps 3 to 5 still apply.

**First line of every message to the build lane (exact, nothing before it, no blank line first).** One of:
- `GATE: ANSWER <file>#<id>[,<id>...] [<file>#<id>...]` (a build answer; `<file>` is the record file, absolute or `~/...`, under `~/.claude/plans/`, no spaces in the path, at most `max_record_bytes` of the config, 597,800 in the example config)
- `GATE: ACK`, `GATE: MILESTONE`, `GATE: QUESTION` (any body; the hook does not test it. Do not put answer content in these: that is the planning lane's rule, not the hook's.)
- `GATE: OWNER-RULING`: the body holds only `> <the owner's words>` lines. Each `> ` line is a quote and must appear word for word (whitespace aside) in one human-typed turn of the project transcripts (the lines may come from different turns, and one turn may be wrapped over several lines; consecutive lines that together are one turn's multi-line text also pass; a `re:` line applies to every line of its block, so put a short ruling in its own block after a blank line), or in the owner's own answer to an AskUserQuestion (the selected option or the typed text, not the question or the other options the assistant wrote). It is not usable for a peer message or any other tool result. A ruling of 7 characters or fewer ("ok", "yes") must be the whole turn or the whole answer and must be followed by a line `re: <the question it answered, 10 characters or more>`, which must appear in what the assistant showed just before that turn (for a widget answer: in that answer's own question).

A message without one of these first lines is blocked.

**Record file.** For each answer id, an `ANSWER` block holding the answer exactly as it is relayed (no line in it may read as a record marker), then lines the helper below writes. A line is a non-blank line of the block.
- `REVIEWED <id> <sha> BEGIN` ... `REVIEWED <id> <sha> END`: the text a full review saw; its hash must equal `<sha>`.
- `CHECK <id> review1|review2 compliance|redteam <ts> sha=<sha> agent=<A>`: a first or second full review by that reviewer.
- `CHECK <id> fixcheck <ts> lines=<l16>[,<l16>...] agent=<A>`: a fix check of those lines (`<l16>` is the hash of a line as it is now).
- `CHECK <id> trio DONE <ts> sha=<h> agents=<A>,<A>,<A>`, when the answer carries a `TRIO:<name>` tag; `<h>` is the answer's hash, and the question block `TRIO <name> BEGIN` ... `END` is in the same file.

`python3 ~/.claude/hooks/build_answer_gate.py sha <file> <id>` prints the current hash (of the answer block, or, for a trio question block, with `<id>` = the name); `... sha <file> <id> changed` prints `<l16> <line text>` for each line changed since the latest review of each reviewer, or `none`.
`... stamp [--session <id>] <file> <id> review1|review2 compliance|redteam`, `... <id> fixcheck`, `... <id> trio DONE`. The session is `--session`, else the environment variable `CLAUDE_CODE_SESSION_ID`; with neither, `stamp` refuses. **Stamp each review right after it returns, before the answer is edited:** `stamp` needs an agent whose prompt holds the current hash, and writes the `REVIEWED` block from the current text. It refuses a `review2` the send check would deny, and a `fixcheck` unless every line `sha ... changed` prints has a passing fix check.

**Cold-agent proof (what `stamp` needs and the send check re-reads).** Claude Code writes every subagent's transcript under `~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl`. `stamp` refuses unless such a transcript backs the line and records the agent on it; the send check looks it up again. An agent backs a line when: (1) its **prompt** holds the 16-hex hash (a review: the hash `sha` prints; a fix check: each line's hash from `sha ... changed`; a trio: the hash of the question block the answer's `TRIO:<name>` tag cites); (2) it is not a fork; (3) it finished; (4) it got no input after its prompt (a coordinator message, a queued command, a revival: spawn a fresh agent); (5) it did not refuse (an agent whose prompt gave it the result ends with the line `REFUSED`: run a fresh one without the result); and (6) its final message ENDS with the closing lines its prompt names, exactly, nothing after them:
- full review: `<id> hash=<hash> COMPLIANCE: FIRST|SECOND` or `<id> hash=<hash> REDTEAM: FIRST|SECOND` (a first review ends with FIRST, a second with SECOND);
- fix check: `<id> hash=<line hash> FIXCHECK: PASS|FAIL`, one per checked line;
- trio judge: `<id> hash=<hash> TRIO: <its answer>` (the option letter or id only; compared whole, folded for case and spaces).
Each cold agent's prompt holds the hash and names its closing line, never the result it should give.
One agent may carry several hashes (one line each) and both labels of a first review, but the two second reviews are by different agents. FIRST and SECOND for one hash count for neither; PASS and FAIL for one line count as FAIL. A trio stamp needs three distinct judges (the latest three) and a strict majority.

The hook allows an `ANSWER` message only when, for every id in the header: the block exists exactly once; each reviewer (the compliance checker, the gap red-team) has a `review2` line preceded by a `review1` line of that reviewer by another agent that finished before the second one started, and the two `review2` agents differ; each line changed since the reviewed text of either reviewer's latest `review2` has a fix check by an agent that started after that review finished; a trio line with the block's hash exists when the answer carries a `TRIO:<name>` tag; all these lines name cold agents that qualify as above; and the message body is, in header order, `<id>:` then the block text exactly, blocks separated by one blank line, nothing else. Unchanged text passes. The hook does not see the post to the owner that a blocking second review requires. A record with old-format lines (`CHECK <id> compliance|redteam <VERDICT> ...`) and without the new evidence is denied with the steps to re-check.

```gate-record
ANSWER Q1 BEGIN
Q1 (where the wiring test lives): in the existing test module that holds the full-open tests. [RULE: P7 | M, REVIEW]
ANSWER Q1 END
REVIEWED Q1 4c574cc20ee94e56 BEGIN
Q1 (where the wiring test lives): in the existing test module. [RULE: P7 | M, REVIEW]
REVIEWED Q1 4c574cc20ee94e56 END
CHECK Q1 review1 compliance 2026-11-03T16:05:00-05:00 sha=4c574cc20ee94e56 agent=a00000000000001
CHECK Q1 review1 redteam 2026-11-03T16:06:00-05:00 sha=4c574cc20ee94e56 agent=a00000000000002
CHECK Q1 review2 compliance 2026-11-03T16:20:00-05:00 sha=4c574cc20ee94e56 agent=a00000000000003
CHECK Q1 review2 redteam 2026-11-03T16:21:00-05:00 sha=4c574cc20ee94e56 agent=a00000000000004
CHECK Q1 fixcheck 2026-11-03T16:30:00-05:00 lines=f8ee47aabf2780af agent=a00000000000005
```
