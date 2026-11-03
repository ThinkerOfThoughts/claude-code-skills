# Stage 2 — Plan

**REVISED 2026-07-31** after stage-3 review: control commit `cf16967`; the divider-memo mechanism
withdrawn; `common.md` added; the CARRY restatements made explicit.

## The edits

### `Architect/stages/divider.md` — rewritten, 118 → ~40 lines

Order matters; this is a prompt.

1. **The job** — record 3666 as the operative instruction: find a natural seam in the given task
   and split it into two pieces at that seam.
2. **Inputs** — `task` (carrying its source material) and `granularity`. **No plan** (C9).
3. **The floor, one direction only** — neither half may fall below it; if every available split
   puts a half at the floor the task is not divisible → `null` (C7).
4. **What you return** — the two sub-tasks and where the seam is; each sub-task carries the source
   material (C13). One sentence: the halves are planned concurrently and blind, so the seam says
   where the joint is, not what one half hands the other (C14).
5. **The review** — dispatch three cold agents on `common.md` + `redteam-split.md` (C5).
   **Concurrently.** Three approvals → return. Any rejection → cut again at a different seam,
   using the reason. **The "while any `major` stands, re-derive" rule is deleted** — it is what
   produced four re-derivations of a cut every reviewer approved.
6. **The cap and the three answers** (C7, C8) — four rounds; after four, the split with the most
   approvals if it reached 2-of-3; otherwise `FAILED_TO_DIVIDE`, which is **not** `null`.
7. **Your output file.**

### `Architect/stages/redteam-split.md` — rewritten, 62 → ~35 lines, standalone

1. **What you hold** (C10) — the `task`, the `granularity` floor, and the proposed division: two
   sub-tasks and a seam. **No plan** (C9). This is the declaration that used to come from
   `redteam.md:11`; without it a reviewer can approve without knowing what it is judging.
2. **The two questions**, record 3666 (C1).
3. **The verdict** — both hold → approve; otherwise reject, naming which question failed and why
   (C1).
4. **A one-line approval is a correct output** (C2), with the owner's reason: a finding the node's
   next `while` pass handles anyway costs the run and buys nothing.
5. **The floor bound** (C11) — do not reject for missing detail; a sub-task need not be detailed,
   only a coherent whole task above the floor. Replaces `redteam.md:13-18`.
6. **Judged on whether your findings are real, not how many you raise** (C12). Replaces
   `redteam.md:54`.
7. One sentence on the seam not being a handoff (C14).

No lenses, no severities, no earned-clean clauses (C4).

### `Architect/stages/common.md` — one sentence in §4

§4 gains a scoping line naming the roles that produce severities (plan reviewer, combiner, node),
so the split reviewer's approve/reject verdict is not in contradiction with its own common file
(C6). No duplication into role files: `leaf.md:47` already states its own position, and the roles
that act on §4 keep reading it unchanged.

### `Architect/SKILL.md` — Roles table

Split reviewer row → `stages/redteam-split.md`, spawned by the divider, 3 of them, reading
`common.md` + that file. `redteam.md` removed from the row (C5).

## Measurement

**Textual (C1–C15): `oracles/check.sh`, self-tested by `oracles/selftest.sh`.**
One positive per-site assertion per criterion. Absence sweeps (C4 only) are **paired** with the
positive assertions and run on normalised text (strip `**`, backticks, `_`; flatten wraps).
Control = `git show cf16967:<path>`. CHANGE assertions must fail there; CARRY assertions must pass
on both and are self-tested by line deletion on a scratch copy. Any assertion that cannot be made
to fail is reported and its criterion is `verified = no`.

**Behavioural (C16–C24): iteration 4 of the real run.** Not a fixture. Dispatch mode is pinned
concurrent in advance so the attributing metrics — rounds, agents, prose lines — are not confounded
by it. Cost is read from `it4/0/` file sizes, file counts and the divider's own record.

C20 and C21 are read off the run's review artefacts — their verdict text — not off the prompt text.
C23 is read off `it4/memo/0.json` and mtime ordering.

## Risks

| Risk | Handling |
|---|---|
| **The floor guard is lost with `redteam.md`** (position lens: nothing moved, the context shrank). | C11 asserts restatement; **C21 verifies by execution** that no reviewer rejects for sub-floor detail. |
| **A vacuous one-line approval scores as success** on every cost metric. | C20 requires every approval to name what it judged and answer both questions; C10 restates the reviewer's inputs, which is the underlying cause. |
| **`null` or `FAILED_TO_DIVIDE` passes as "the run got further."** | C22 excludes both explicitly and makes them a stop-for-human. |
| **Cheaper reviews are worse reviews** — the real seam findings the it3 reviews raised go unraised. | Accepted **on the owner's instruction**, record 3666 and his worked example: those findings re-enter through the node's next `while` pass. Recorded as an accepted consequence with its owner locus, not as an oversight. **Reviewer B contests the reach of this acceptance** — `it3/0/divide-0.md` §5 G4/G5 report that nothing carries the seam down and a planner has no upward channel to object to it, so some seam defects may not re-enter. **That is a real gap and it is NOT fixed here**: it is a defect in `node.md`'s seam transport, not in the split review, and fixing it inside this change would be the apparatus growth this run exists to reverse. **Logged to `decisions.md` as an open finding against `node.md` for the next iteration.** |
| **The rewrite drops a rule nobody noticed was load-bearing.** | `0-baseline.md` enumerates the CARRY list; C7–C15 assert each. A DROP not on the declared list is a regression. |

## Deliberately not done (record 3497)

No divider-level memo (withdrawn — see `1-spec.md`); no cap on divider output size; no schema for
`divide-<iter>.md`; no handling for two dividers racing on one path; no change to `redteam.md`,
`redteam-plan.md`, `leaf.md`, `combiner.md` or `node.md`; no fix to the seam-transport gap above.
