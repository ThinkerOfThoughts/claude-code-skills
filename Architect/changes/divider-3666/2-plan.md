# Stage 2 — Plan

## Shape of the change

Two files are rewritten from scratch rather than edited. Both are short after the change, and an
edit-in-place would leave the surviving apparatus load-bearing by inertia — the thing this run is
removing. `SKILL.md` and `node.md` take one-line dispatch corrections.

### `Architect/stages/divider.md` — target ~35 lines

Sections, in order (order matters; this is a prompt):

1. **The job**, record 3666 verbatim as the operative instruction: find a natural seam in the
   given task and split it into two pieces at that seam.
2. **Inputs**: `task` (carrying its source material) and `granularity`. **No plan** (C8, C10).
3. **The floor, one direction only**: neither half may fall below it. If every available split
   puts a half at the floor, the task is not divisible → `null` (C6).
4. **What you return** — the two sub-tasks and where the seam is; each sub-task carries the
   source material (C10). One sentence: the halves are planned concurrently and blind, so the
   seam says where the joint is, not what one half hands the other (C11).
5. **The review**: dispatch three cold agents on `common.md` + `redteam-split.md` (C5). All
   three approve → return. Any rejection → cut again at a different seam, using the reason.
   **Not** "while any major stands" — that rule is deleted; it is what produced four
   re-derivations of a cut every reviewer approved.
6. **The cap and the three answers** (C6, C7): four rounds; after four, the split with the most
   approvals if it reached 2-of-3; otherwise `FAILED_TO_DIVIDE`, which is **not** `null`.
7. **Your output file, written as you go** (C17) — see below.

### `Architect/stages/redteam-split.md` — target ~30 lines, standalone

1. **What you are reviewing**: a proposed division — two sub-tasks and a seam. No plan (C8).
2. **The two questions**, record 3666 verbatim (C1).
3. **The verdict**: both hold → approve; otherwise reject **with an explanation of which
   question failed and why** (C1).
4. **A one-line approval is a correct output** (C2), with the reason from the owner's worked
   example: a finding the node's next `while` pass handles anyway costs the run and buys nothing.
5. **The floor bound** (C9): do not reject for a lack of detail — a sub-task is not required to
   be detailed, only to be a coherent whole task above the floor. This is the sentence that
   replaces the guard `redteam.md` used to supply.
6. One sentence on the seam not being a handoff (C11).

No lenses, no severities, no earned-clean clauses, no provenance record, no closed-set
enumeration (C4).

### `Architect/SKILL.md` and `Architect/stages/node.md`

Roles table row: split reviewer → `stages/redteam-split.md`, spawned by the divider, 3 of them.
`node.md`'s divider dispatch line is checked and corrected if it names reviewer files.

### The divider memo (item 2, C17)

`divider.md` §7 instructs: **open `<run>/<node_id>/divide-<iter>.md` before round 1.**

- If it exists, read it. It holds one `## Round N` section per completed round. Resume at the
  first round not present. Do not re-run a round already recorded.
- After **each** round completes — the split proposed and the three verdicts — **append** its
  `## Round N` section. Do not hold the record until the end.
- When the answer is decided, append the answer section.

Single writer (this call), written after the value exists, read only by a restart of this call.
Same discipline as the node memo, one level down. **No new shared state and no coordination
protocol**: the file already existed; it is now written earlier and read at start.

## Measurement

**Textual (C1–C12): `oracles/check.sh`.** One positive per-site assertion per criterion, plus
paired absence sweeps on normalised text (strip `**`/`` ` ``/`_`, flatten line wraps) — never an
absence sweep alone.

**Oracle self-test: `oracles/selftest.sh`.** Runs the same checker against the frozen pre-change
files from `git show d81bc0a:<path>`. Every C1–C5 and C11 assertion **must fail** there and pass
on the new files; C6–C10 and C12 are CARRY assertions and must pass on **both** — for those the
self-test instead deletes the asserted line from a scratch copy and confirms the assertion fires.
Any assertion that cannot be made to fail is reported and its criterion is `verified = no`.

**Behavioural (C13–C17): iteration 4 of the real run.** Not a fixture. The task, granularity and
`gate_depth` are taken verbatim from `runs/data-distiller/decisions.md`; `it4/` is a fresh attempt
directory with its own `memo/`. Cost is read from file mtimes and the count of dispatched agents,
against `0-baseline.md`'s 15 agents / 90 minutes.

C17 is checked by **injecting the restart**: once `divide-0.md` holds a completed `## Round 1`,
a second, fresh divider agent is dispatched on the same output path with the same arguments, and
its output is read for which round it began at. A live crash is not waited for.

C14 and C15 are read off the run's own artefacts — verdict text and file size — not off the
prompt text.

## Risks and how each is handled

| Risk | Handling |
|---|---|
| **The floor guard is lost with `redteam.md`.** Position-lens: nothing moved, but the reviewer's *context* lost the paragraph that bounds vagueness. | C9 asserts it is restated; C14 verifies by execution that no reviewer rejects for sub-floor detail. |
| **3666 read as repealing the round machinery**, collapsing `Divisible` to one round and losing `FAILED_TO_DIVIDE`. | C6/C7 assert both survive. 3666 speaks to *instructions*; 3402/3438 settled *rounds*. Reviewer disagreement here is a declared stop-for-human. |
| **Cheaper reviews are worse reviews** — the real defects the it3 reviews found (seam gaps, a termination hole) go unraised. | Accepted **on the owner's instruction**, record 3666 and its worked example: those findings are handled by the node's next `while` pass. The loop, not the split review, is the mechanism. Recorded as an accepted consequence, not an oversight. |
| **The rewrite drops a rule nobody noticed was load-bearing.** | `0-baseline.md`'s CARRY list is enumerated and each item has a criterion (C6–C12). A DROP not on the declared list is a regression. |
| **The divider memo makes the divider's output file two things** — a record for the owner and a resume point. | Same file, one writer; the resume reader is a restart of the same call. Nothing else reads it. If a reviewer finds a second reader, the design is wrong. |

## What is deliberately not done

No guard is added for anything that has not happened (record 3497). Specifically not added: a cap
on divider output size, a schema for `divide-<iter>.md`, a checksum on the resume file, any
handling for two dividers racing on one path (the node dispatches one divider per call), and any
change to `common.md`, `redteam.md` or `redteam-plan.md` — the plan reviewer keeps its apparatus,
because 3666 is about the *split* review.
