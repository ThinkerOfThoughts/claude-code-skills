# Stage 8: conformance (no baseline; regression N/A, the subject is prompt text)

Verification of every criterion is a recorded one-off check (not committed as a test). Base: e22ca73.

| Crit | Proof home | Check run | Result | Verified |
|---|---|---|---|---|
| C1 | C5 run | Replay record carries the conformance section, per-entry verdicts with lines (P1 violates, P4 violates, P7 violates, P3/R2 conditional), mechanism table with file:line, and "No sign-off" | as expected | yes (stage 3 only; see limits) |
| C2 | C5 run | Replay raised the hand-written reader (F1, major): duplicate of the shared reader, shared mechanism worked around, bypass outside the module; the "not edited" scope line and the ratchet marker were challenged as claims. The bare delete was NOT raised: the replay input plan leaves `clear_queue` "unchanged", so no delete appears in the plan text, and the mechanism table lists the delete row as "none exists, body unseen" | reader yes, delete no | yes for the reader; the delete half is not shown (see limits) |
| C3 | grep | `grep -c principles_context` per file: charter 6, stage-3 3, stage-4 1, stage-6 2, SKILL 2, METHODOLOGY 3, companion 1. Known-bad: same count at the base commit is 0 for every file (git grep returned nothing). Name check over added lines of stages/SKILL/METHODOLOGY: empty; known-bad: the companion config's added lines match 4 times | pass | yes |
| C4 | grep + C5 record | (a) every input-list site (charter 104,139; stage-3 23,198; stage-4 115; stage-6 15-16,26,118; METHODOLOGY 159; SKILL 20) names `principles_context` or the charter's closed set; stage-1 lines only say touched files join the context. (b) `conformance, PRC` appears once, in charter; the wrapped phrase "worked around because it almost fits" appears in charter only (after folding whitespace; first form of the command was wrong, fixed in the plan). (c) the replay record still carries five labelled lenses, coverage challenge, label audit (not performable without criteria; stated), fidelity pins, reported sha256 hashes including the sheet, and a factual lens | pass | yes |
| C5 | replay | One run, sonnet, foreground, new charter + stage-3 + original spec and plan + sheet + facts file; 0 rebuilds of the mechanism. Control arm: old charter/stage-3 text, same inputs | pass; control partial | yes |
| C6 | grep, diff -rq | Added lines contain no `home/` path and none of the owner/collaborator names or repository handles (tracked diff and the change folder); `Plan_ledger/` diff empty; known-bad probe line matched the path pattern. Installed-copy sync: see decisions.md | pass | yes |

## C5 verdict (quoted from the replay record)
Hand-written reader: "F1. `read_queue` is a hand-written JSONL reader beside the shared one, with the ratchet bypassed by
marker." ranked Major, cited as "PRC violations: (a) a duplicate of the shared reader, (b) the shared mechanism worked around
because it almost fits, (c) a read of JSONL data done outside `json_io` ... Also P1 and P7." Per-entry: "P1 one mechanism:
violates", "P7 reuse existing mechanism, remove duplicates: violates". Outcome line: "No sign-off. The review raises majors
F1-F5". The same record challenged the scope line: "The spec's own 'not edited' line for `json_io` (spec 59) is itself the
scope line that leaves the shared mechanism unextended, and I challenge it."

## Control arm (old text, same inputs including the sheet and facts)
The old reviewer raised the second parser as a Major ("ignores `parse_jsonl` ... (P1/P7). Close it by stating what
`parse_jsonl` does or cannot do") but accepted the scope line ("Extending json_io is ruled out of scope, but the reuse question
is unasked"), gave no per-principle verdict and no sign-off statement, and did not raise the delete. So the sheet alone gets a
Major as an open question; the new text turns it into a violation verdict with the scope line challenged and a per-entry
record. The control caught the reader weakly, so it shows the edit's contribution as the verdict and the scope challenge, not
the detection.

## Not exercised (stated, not hidden)
- Stage 6 (ST6g): no code or diff of the failed run is available; only the plan-stage replay was run.
- The bare delete: not raised in the replay (no delete in the input plan text); the charter's rule (c) is tested only by
  reading and by the stage-6 reviewer's reading of the wording.
- A negative control (a clean plan passes): not run; over-firing of the at-least-MAJOR floor is unmeasured.
- Discovery of the shared module without the facts file: not run (the project source was withheld).
- Position effect of the new bullet on the conditional bullets: observed only as "the five lenses and other sections were still
  emitted" in one run.
