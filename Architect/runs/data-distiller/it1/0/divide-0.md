# Divisible(task, granularity) — return value: `null`

**Task:** Plan the implementation of the Data-Distiller skill (full statement carried in
`split-round-3.md`).
**Granularity floor as given:** *"A step a competent practitioner can execute without further
planning: concretely, one file created or one coherent edit to one file, with the content that goes
in it specified."*

## RETURN: `null`

**Not because the task is at the floor.** Every round produced two halves of five files each,
against a floor of one file, and **all nine cold reviewers across three rounds independently
returned "the floor is clean, neither half falls below it, this task is divisible."** No reviewer in
any round filed an indivisibility finding.

`null` is returned under the divider's **three-round cap**: a `blocker` and several `major` findings
stood after the third round. Per `stages/divider.md`, the cap is reached and `null` is the required
answer. The node should now spawn leaves on the undivided task; the standing findings below are the
substance that should reach whatever comes next.

---

## Rounds run

| Round | Split proposed | Reviewers | Result |
|---|---|---|---|
| 1 | **The frame** (SKILL/METHODOLOGY/config/README) vs. **all of `stages/`**, with a one-way contract: the frame half fixes the vocabulary, the stages half consumes it | 3 cold, dispatched one at a time | **2 blockers, 9 majors** |
| 2 | **Driver plane** vs. **worker plane**, with a non-directional shared interface I1–I10 fixed by the divider and restated verbatim inside both sub-tasks | 3 cold | **3 blockers, ~7 majors** — every one against the interface; all three reviewers said keep the joint |
| 3 | Same joint; interface rebuilt around one structural move — *the driver creates and hands down every path and value; no worker names a path or reads a config* — reducing the seam to nine clauses containing no record schema, no directory layout and no config key set | 3 cold | **1 blocker, 6 majors** — again all against the seam; all three reviewers again said keep the joint |

Files: `split-round-{1,2,3}.md`, `split-review-r{1,2,3}-{a,b,c}.md`, all in this directory.

**Round 1's decisive blocker, verified independently against Architect's own role files rather than
taken on the reviewer's word:** `Architect/stages/node.md:50-53` spawns both child nodes together
with the same incoming `plan` and merges by `Union`; `Architect/stages/leaf.md:16-19` gives a leaf
only `(task, plan, granularity)`; `Architect/stages/combiner.md` preserves conflicts rather than
resolving them. **The halves are planned concurrently by cold agents that never see each other's
output.** A seam of the form *"half A fixes the vocabulary, half B consumes it"* is therefore not a
seam — it is a guaranteed vocabulary collision that `Union` preserves by design. Rounds 2 and 3 were
both non-directional in consequence: everything crossing the cut is fixed by the divider and reaches
both halves identically.

---

## The joint that survived all three rounds

Recorded because it is the durable result of this run, and because whatever plans this task next
will face the same question.

**Driver plane** — `SKILL.md`, `METHODOLOGY.md`, `stages/node.md`, the worked per-corpus config
instance, `README.md` — the files read by an agent that already holds the run's context, the config
and the layout, and decides what happens next. Accountable for: a run that terminates, stays inside
its concurrency ceiling, resumes after a kill, keeps coordinators from ever seeing a finding, and
hands the human a result.

**Worker plane** — `stages/common.md`, `stages/decompose.md`, `stages/analyst.md`,
`stages/verify.md`, `stages/merge.md` — the files handed verbatim to cold agents whose entire
context is that file plus a handful of arguments, each doing one bounded pass and returning.
Accountable for: every returned artifact being cited, verified, uninterpreted, and independently
arrived at.

**What changes at the boundary — the reader's information state.** A worker-plane file is handed to
a process with no other context, so it may assume nothing and must be self-sufficient; a driver-plane
file is read by a process holding the config, the layout and the run's history, so it may refer
outward freely. That is a hard constraint on authoring, not a label. Two round-3 reviewers confirmed
the same two kinds exist in the house shape independently: `Guarded_change/SKILL.md:32` has the
driving agent *read* each stage file, while `Guarded_change/stages/stage-3.md:8` says the charter
*"is given to the reviewer verbatim."*

Three earlier framings were tried and are recorded as wrong, so they are not re-tried:
- **"Files read once by the invoking agent vs. prompts read verbatim mid-run"** (round 1) — factually
  false about the siblings, whose `stages/` files are predominantly the *invoking* agent's own
  procedure (`Guarded_change/stages/stage-1.md:8`, `stage-5.md:7`).
- **"Two disjoint failure sets"** (round 2) — self-refuting: it listed *steered* on the worker side,
  but steering is what the blind-roll-up barrier prevents and that barrier is driver-plane.
- **"The node never reads findings, so cutting at the barrier splits a two-role rule"** (round 1's
  reason for rejecting the cut that rounds 2 and 3 then adopted) — wrong: the rule constrains only
  the node, so it is a one-role rule and splitting node from workers does not split it.

Alternatives weighed and rejected with grounds, across the rounds: the two-layer Layer-1/Layer-2 cut
(8 files against 2, and the config keys thread through every file of the large half, so the seam gets
*larger*); the per-item-pipeline vs. cross-item-run-plane cut (`merge.md` and `common.md` end up
co-owned); and not dividing at all (rejected on the floor criterion, which is the stated test).

---

## Findings still standing at the cap

These are the reason for `null`. All are against **the seam**, not the boundary — a point all three
round-3 reviewers made unprompted and in the same words.

### Blocker

**B1 — the two workers that actually read the corpus are never handed the corpus root.** *(r3-c F1.)*
The round-3 seam moved config out of the interface by having the driver hand every value down in the
spawn payload, and it declares that payload exhaustive: *"the driver hands every worker exactly the
arguments below."* The corpus root appears only in `decompose`'s payload. But `analyst` reads the
corpus, and `verify` must *re-open every citation* in it. Both are handed a per-item locator and no
root. Either the locator is required to be independently resolvable — a real constraint on its
content that no clause states — or the two roles cannot reach the corpus at all. Round 2's config
blocker was closed for one role of three.

### Majors

**M1 — the item locator is the seam's busiest object and its only unspecified one.** *(r3-b MAJ-1;
overlaps r3-c F4.)* The seam fixes line-level placement for the item id and gives the locator no
delimiter, no label, no extent and no content requirement — while that one string carries four
loads: the driver's extraction target, the only available channel for the per-item `window`/`sample`
strategy (which the analyst is required to act on but which the payload omits), `verify`'s only
corpus address, and the origin of the deliverable's coverage note. The driver plane must parse a
format the seam assigns to the worker plane, and the two planners never meet.

**M2 — the status record has two producers, one of which is forbidden to know its shape; and
`partial` is defined on one side of the cut and consumed on the other.** *(r3-b MAJ-2; r3-a F1;
r3-c F3.)* The seam gives `merge` the record and also has the driver write it when a unit dies early,
while assigning its contents to the worker plane — violating the seam's own rule that anything not
fixed belongs wholly to one half. Separately, `partial` is fixed as a vocabulary word with no
predicate: the worker plane will define when it is emitted, the driver plane will define what to do
on reading it, and the plausible independent definitions ("coverage was incomplete" vs. "not
finished, re-dispatch") produce a run that never terminates.

**M3 — `decompose` has no completion signal, so resume cannot trust the manifest.** *(r3-b MAJ-3.)*
The write-order invariant that makes resume sound — *the status record is written only after the
unit's outputs are closed* — is attached to `merge`, and `decompose` has no merge above it. After a
kill, the driver finds a manifest and has no way to distinguish a complete one from one truncated
mid-write. Both escapes carry unstated preconditions: always re-running `decompose` requires item
ids stable across re-runs (the seam requires only that they be unique and filesystem-safe); never
re-running it is the truncation bug.

**M4 — the terminal deliverable's producer cannot know it is the terminal producer.** *(r3-a F2.)*
`merge` runs at three positions and the payload is identical at all three, so the one requirement
placed on the root invocation — produce the deliverable, carry the coverage note — has no trigger.
The obvious escape (recognise the output path's name) is closed by the same round-3 move that
removed paths from the worker plane.

**M5 — a unit that fails before `merge` leaves no trace in the deliverable.** *(r3-c F2.)* The
payload is exhaustive, the driver is read-prohibited on findings artifacts, and `merge` is the fixed
sole producer — so a partially-failed run hands the human a findings file that silently overstates
its coverage. Same defect class as the round-2 finding about un-analyzed content, recurring on
failure rather than on sampling.

### Notable minors (recorded, not looped on)

The context budget crosses the seam with no unit fixed, so the driver may document tokens while
`decompose` measures bytes; *"terse"* — a word in the task's own statement of the blind roll-up — is
bound nowhere, and the half accountable for the barrier does not own the record the barrier is blind
to; no actor is instructed to compose `common.md` ahead of a worker role file, which would leave all
of its rules inert; the analyst index `k` is fixed in the payload with no stated purpose; and the
stated joint does not describe `README.md` or `METHODOLOGY.md`, which sit on the driver side because
they are not worker prompt files rather than because of their reader.

One factual correction to my own round-3 text, filed by r3-b (M-1) and accepted: **dividing does not
trade away `Consensus` corroboration, it defers it.** Each child is a *node*, not a leaf; it runs the
same loop and bottoms out in three leaves merged 2-of-3. My alternative-(a) cost accounting
overstated the price of dividing.

---

## What this run establishes for whatever plans this task next

1. **The task is divisible on the floor criterion.** Nine cold reviewers said so; none dissented.
   `null` here is a cap outcome, not a floor outcome, and it should not be read as evidence that a
   single planner is the right shape.
2. **The driver/worker joint is sound and should be reused, not re-derived.** Every round-3 reviewer
   said keep it; two said explicitly that if the division is rejected the right next move is to
   repair the seam clauses, not to look for a different boundary.
3. **Every standing finding is a seam finding, and a single planner writing all ten files has no
   seam.** The locator's format, the status record's shape and ownership, `decompose`'s completion
   signal, and the root-merge trigger all become one author's internal-consistency problem — which is
   where they are cheapest. So the undivided leaf task inherits the *substance* of these findings as
   design questions it must answer, not as a defect it must repair.
4. **If the cut is re-attempted at a later iteration**, the repairs named by reviewers are small and
   local: hand the corpus root to `analyst` and `verify` (or state the locator must be independently
   resolvable); delimit the locator and declare it the carrier for anything per-item the worker plane
   needs downstream — one reviewer's alternative, a manifest *directory* with one file per item, the
   filename as the id and the whole content as the locator, would delete the format agreement
   entirely; give the status record one owner or one fixed minimal shape and define `partial`; extend
   the write-order invariant to `decompose` and require stable item ids; and add one field naming the
   merge invocation (`item` / `rollup` / `root`).
5. **Do not re-propose a directional seam.** It is unexecutable under this execution model, for the
   reasons verified above.
