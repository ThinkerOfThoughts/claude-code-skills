# Split review — round 3, reviewer A

Reviewing the proposed division in
`Architect/runs/data-distiller/0/split-round-3.md` against the task and the granularity floor
as given. I hold no plan and did not look for one. I did not read, list or grep
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`, and I did not read any sibling
`split-review-*.md`.

**Bottom line: the joint is real and I would keep it. Two `major` findings stand against the
interface — both are one-clause repairs to S2/S3, and both concern the same missing thing: the
spawn payload carries no invocation context, so a worker cannot tell which of several positions
it was dispatched into.** I am filing them as `major` because neither half can repair them —
both halves are forbidden to re-scope S2 — and because each has a concrete failure scenario that
reaches the run's deliverable or its termination.

---

## Verdicts by lens

| Lens | Verdict |
|---|---|
| 1. Factual | **Clean**, with one nitpick (N1). Citation audit below. |
| 2. Logical | **One finding** — F1. |
| 3. Missed opportunity | **One observation**, folded into F1/F2 (the single clause that repairs both). Not filed separately. |
| 4. Unstated assumptions & risks | **Three findings** — F2, F4, F5. |
| 5. Fidelity | **Clean except as noted in F1.** Terms pinned below. |
| 6. Completeness | **Two findings** — F3, F6. Generative sweep run; what it looked for is listed below. |

### Factual — what I consulted

Every `file:line` the division cites, checked against the file:

| Cited | Checked | Result |
|---|---|---|
| `Dragonfly/SKILL.md:22` cold-start guard, "Dragonfly only" | read both SKILL.md | **Correct.** `Dragonfly/SKILL.md:22` is `## Before you start: cold-start guard`; `grep -i cold-start Guarded_change/SKILL.md Guarded_change/METHODOLOGY.md` returns nothing. |
| `Guarded_change/SKILL.md:25-52`, `Dragonfly/SKILL.md:29-70` — run-loop register | read | **Correct.** Both are the `## Loop` section including the stage-index table. |
| `Guarded_change/METHODOLOGY.md:37-54`, `Dragonfly/METHODOLOGY.md:47-62` — fenced stage diagram | read | **Correct.** Both are fenced blocks, not prose. |
| `Guarded_change/METHODOLOGY.md:103-152` — annotated key skeleton inline | read | **Correct.** `## The config contract (Layer 2)` with an inline annotated YAML skeleton + rules. |
| `Dragonfly/METHODOLOGY.md:161` *Trigger*, "Dragonfly only" | `grep -n '^## '` on GC METHODOLOGY | **Correct.** GC's sections are Why / The loop / Stage index / The two layers / The config contract / What a run produces / Human-in-the-loop — no *Trigger*. |
| `Guarded_change/METHODOLOGY.md:154-168`, `Dragonfly/METHODOLOGY.md:141-153` — run artifacts all markdown | read both blocks | **Correct.** Every artifact listed in both is `.md`. |
| `Guarded_change/METHODOLOGY.md:88-100`, `Dragonfly/METHODOLOGY.md:95-102` — two-layer seam in a section of its own | read | **Correct.** |
| `Guarded_change/METHODOLOGY.md:143` — naming the operative copy | read | **Correct.** "lives written-in-full in `stages/stage-3.md`…" is the naming manner claimed. |
| `Guarded_change/METHODOLOGY.md:175-182`, `Dragonfly/METHODOLOGY.md:152-153` — `decisions.md` precedent | read | **Substantively correct, both ranges off by a line or two** — see N1. |
| `guarded-change.companion.md` / `dragonfly.companion.md` as the worked-config precedent; both siblings carry `README.md` | `ls` | **Correct.** |
| `Architect/stages/node.md:44-53` — `Consensus` (3 leaves) vs `Union` (2 children) | read | **Correct**, and `combiner.md:20-41` confirms the two rules and that `Union` discards nothing. |
| `Architect/stages/node.md:50-53`, `leaf.md:16-19` — halves planned by non-communicating agents | read | **Correct.** Children are spawned with `(division.first|second, plan, granularity, …)` and waited on; a leaf's inputs are task/plan/floor only. No channel exists. |

The file-count claim in alternative (c) ("8 files against 2") is consistent with the ten-file
set the division itself enumerates.

### Fidelity — terms pinned

- **"cold analyst agent"** → a separately spawned agent whose entire context is
  `stages/common.md` + `stages/analyst.md` + the S2 arguments (sub-task two, opening paragraph).
  Real mechanism, not a proxy — but see **F3**, which is about how that composition happens.
- **"independent"** → S5, and it is pinned to *two* mechanisms that bind different actors: N
  separate spawns with no sibling output paths (driver), and a prohibition on opening any file
  not handed at spawn (worker). This is the strongest clause in the seam.
- **"cold verification"** → a separately dispatched `verify` worker that re-opens every citation
  (S2, sub-task two file 4). Cold by `common.md`'s no-shared-context rule. Not a proxy.
- **"blind roll-up"** → S4 (absolute read prohibition on findings artifacts) *plus* S3 Invariant
  B (return value is a path and one word). Invariant B is the one that matters: the reply channel
  is the proxy risk, and it is closed explicitly.
- **"ranks by how many independent analysts agreed"** → `merge` counting agreement. **This is the
  one term I could not pin to a working mechanism** — see F1.
- **"resume from on-disk state"** → status records + Invariant A's write-order rule + the
  driver's own run state. Mechanism present; F1 attacks its correctness, not its existence.
- **"read-only over the corpus"** → an instruction in `common.md`. In a skill made of markdown
  prompt files that is the only available mechanism and both siblings do the same
  (`Guarded_change/stages/charter.md:9-14`), so I am not filing it — recording that it is
  instruction-enforced, not permission-enforced, and that neither half is asked to restrict tools
  at spawn.

### Completeness — the generative sweep

Beyond the structure's own checklist, I swept for: an unowned failure mode (→ F1); an
invocation that cannot be distinguished from another (→ F2); the mechanism by which a prompt
file actually reaches the agent it governs (→ F3); an argument in the interface with no
consumer (→ F4); a unit or encoding two non-communicating halves must agree on (→ F5, N2); a
document that must describe what it does not own (→ F6); a completeness marker for the one
stage that has no merge (`decompose` — covered, the driver owns its own run state and may record
it); a retry/failure cap (covered — driver owns termination); the human handover (covered, S6);
config-absent and dead-path handling (covered, sub-task one file 1); install verification
(covered, file 5).

---

## Findings

### F1 — `major` — the status record's third value has no defined meaning and no actor who can produce it; the agreement denominator is unrecoverable

*Lenses: logical, fidelity, unstated assumptions.*

S3 Invariant A fixes the outcome as **one of `complete`, `failed`, `partial`** and fixes two
producers: `merge` writes it for a unit that merged; the driver writes `failed` for a unit that
died before merge. **Nothing defines `partial`, and no actor is positioned to write it.**

- `merge` cannot detect a partial unit. Per S2, `merge` receives "the input paths to merge (an
  item's verified findings, or the merged outputs of a node's children)" — and at the item level
  that is a **single** file, because S2 gives `verify` the N analyst paths and one output path.
  So `merge` is handed no N, no dispatched-count, and at item level not even a path count. It
  cannot distinguish "5 analysts, all returned" from "5 dispatched, 3 returned".
- The driver *can* detect it, but S3 authorises the driver to write a status record only "when a
  unit fails before `merge` runs".
- Both halves are barred from repairing this: "Neither half may rename or re-scope one."

**Failure scenario 1 (non-terminating resume).** The driver-plane planner writes node.md's
resume procedure and must give `partial` a meaning; the natural one is "some children did not
complete — re-dispatch." The worker-plane planner writes merge.md and must give `partial` a
meaning; the natural one, given sub-task two file 3 requires `analyst.md` to record `window`/
`sample` omissions and S6 requires a coverage note, is "this unit's coverage was incomplete."
Neither planner can see the other. On the first resume, every windowed item is re-dispatched,
re-merged, re-marked `partial`, and re-dispatched again. The run does not terminate — and
"Restart and resume from on-disk state" is a named defining property of the task.

**Failure scenario 2 (false corroboration).** Five analysts are dispatched for an item; two die.
`verify` is handed three paths, `merge` is handed `verify`'s one output, and ranks a finding as
agreed by three analysts with no record that the denominator was five. S6's coverage note covers
only `window`/`sample`, so the degradation reaches the deliverable invisibly. The task's
"ranks surviving findings by how many independent analysts agreed" is implemented as a numerator
with no denominator — and trustworthy corroboration is the skill's entire purpose.

**Repair (one clause, and it is the same clause as F2's).** Add to S2's `merge` payload the
count of workers dispatched for the unit, and define `partial` in S3 — or delete `partial` from
the enumeration and let the coverage note carry incompleteness. Either fixes it; leaving a
three-valued enumeration with one undefined value on the resume path does not.

### F2 — `major` — the terminal deliverable's producer cannot know it is the terminal producer

*Lenses: unstated assumptions, completeness.*

S6: "`<the run's FINDINGS file>` is written by a dispatched **merge** agent running
`stages/merge.md` **at the root of the roll-up**… It must carry a **coverage note**." Sub-task
two file 5 tells `merge.md` to specify "the shape of the run's `FINDINGS` deliverable including
its coverage note (S6)".

`merge` runs at three positions — per item, at an intermediate roll-up node, and at the root —
and **S2's payload is identical at all three**: input paths, output path, status-record path. A
root invocation over two children's merged outputs is byte-for-byte indistinguishable from a
mid-tree invocation over two children's merged outputs. So the one requirement S6 places on one
specific invocation has no trigger.

The obvious escape — key off the output path being named `FINDINGS.md` — is closed by the
division itself: the worker plane "**names no path and reads no config file**" (sub-task two)
and does not know the run layout (driver-owned, S-preamble), so `merge.md` may not be written to
recognise a path form it is not permitted to know.

**Failure scenario.** The worker-plane planner reads "runs at **two** levels" (sub-task two file
5) and writes `merge.md` accordingly: item-level output shape and roll-up output shape. The
driver dispatches the root merge with the standard payload. The run produces a roll-up-shaped
merged file and no FINDINGS deliverable with a coverage note — the artifact the human is handed,
and the only route by which "which items were not fully covered" reaches a reader, per S6 and
per round 2's finding #14 which S6 was written to close.

There *is* a resolution inside one half — the worker plane could decide every merged output is
deliverable-shaped and carries a coverage note, leaving the driver to hand over the root path.
That works. But nothing requires it, sub-task two's own wording points away from it, and the
driver half cannot verify it, because verifying it means reading a findings artifact (S4).

**Repair.** The same clause as F1: give S2's `merge` payload one field naming the invocation
(`item` / `rollup` / `root`), or state in S6 that every merged output carries the deliverable
shape and coverage note and the root one is simply the last.

### F3 — `minor` — no actor is instructed to compose `common.md` ahead of a worker role file

*Lens: completeness (this is what the generative sweep caught).*

S1 describes `stages/common.md` as "included verbatim ahead of every worker role file" — passive
voice, no actor. Trace the actor:

- The worker half states the property (file 1) but "does not decide dispatch" and does not write
  `SKILL.md` or `stages/node.md`, so it cannot implement it.
- The driver half's content list for `stages/node.md` is: the recursion, the ceiling, the resume
  procedure, "the **spawn payload it hands each worker role**, matching S2", the independence
  discipline, the blindness barrier. Prompt composition appears nowhere, and S2 is framed as a
  closed list — "The driver hands every worker **exactly the arguments below**."

The house precedent puts this instruction squarely on the driver side: in the sibling skill the
*driver-read* stage file is what carries it — `Guarded_change/stages/stage-3.md:8`, "The charter
core is given to the reviewer verbatim." The analogous sentence has no home in this division.

If it is dropped, none of `common.md`'s rules bind anyone — cold independence, read-only, S3
Invariant B's return channel, and S5's worker-side scavenging prohibition all become inert text,
and S5 explicitly leans on the worker side ("The worker side of it: `stages/common.md`
forbids…").

I considered `major` and settled on `minor`: the driver half must publish S1's purpose line
verbatim in its stage index, so a competent driver-plane planner is likely to wire it, and a hole
this visible in the merged plan is catchable by the plan red-team that follows. **Repair:** one
line in S2 — "each worker's prompt is `stages/common.md` concatenated ahead of its role file;
the driver composes it."

### F4 — `minor` — the analyst index `k` is fixed in the interface with no stated purpose

*Lens: unstated assumptions.*

S2 hands `analyst` "its own analyst index *k*". Nothing says what it is for, and the worker half
owns "what each worker is told". Two readings, with different consequences:

- `k` is decorative (used to label output). Then it is redundant — the driver already hands the
  output path — and the seam carries an argument with no consumer.
- `k` is a diversity seed, i.e. `analyst.md` varies its behaviour by `k` ("analyst 1 reads
  chronologically, analyst 2 by author"). That is a substantive method choice: it means the N
  analysts are not N runs of one method, which changes what "how many independent analysts
  agreed" measures, and the driver's `METHODOLOGY.md` — written by the other half — would
  describe the method wrongly.

The task says "N independent cold analyst agents per item" and does not authorise differentiating
them. **Repair:** state in S2 what `k` is for, or drop it.

### F5 — `minor` — "the context budget an item must fit inside" has no fixed unit

*Lens: unstated assumptions.*

S2 hands `decompose` "the context budget an item must fit inside", and the budget's *value*
originates in a config key the driver half owns and documents; the *measurement* against it is
worker-owned ("the sizing and strategy-selection criteria", sub-task two). Neither half is bound
to a unit and neither can see the other. The driver documents `context_budget: 100000` meaning
tokens; `decompose.md` measures bytes; every item is mis-classified in the same direction and
either nothing is ever split or everything is. **Repair:** one phrase in S2 fixing the unit, or
requiring the value to be handed with its unit.

### F6 — `minor` — `METHODOLOGY.md` must describe worker behaviour it does not own, and no reconciliation is assigned

*Lens: completeness.*

`METHODOLOGY.md` is a driver file and, per the sibling shape it is told to follow, contains a
*method* section (a fenced stage diagram, `Guarded_change/METHODOLOGY.md:37-54`) and a stage-index
table whose column is "What it covers" (`Guarded_change/METHODOLOGY.md:69-80`). Both are summaries
of what the stage files do — here, five files the driver half does not own and its planner will
never see. S1 pins the six one-line purposes verbatim, which covers the index table; it does not
cover the diagram or the method narrative.

Nothing in the division assigns reconciliation, and the merge that follows is explicitly barred
from performing it: `Architect/stages/combiner.md:62-64` — "Do not harmonise wording… When two
items are close but not identical, keep both."

I am filing this `minor`, not `major`, for two reasons. The residual surface is small once S1
pins the purposes. And the sibling skills' own standing self-check criterion — "SKILL.md ↔
METHODOLOGY.md ↔ stage-file consistency on every rule stated in more than one place"
(`Guarded_change/SKILL.md:82-84`; `Dragonfly/SKILL.md:88-89`), which sub-task one file 1 must
carry — is a forward obligation on future edits, not a claim about this build, so writing it does
not commit the driver half to a check it cannot perform.

### N1 — `nitpick` — two `decisions.md` citations overshoot by a line or two

`Guarded_change/METHODOLOGY.md:175-182` — the `decisions.md` paragraph is 175-180; 182 is the
first line of the unrelated *Ratification records* paragraph. `Dragonfly/METHODOLOGY.md:152-153`
— `decisions.md` is line 153; 152 is the tail of `incidental-ledger.md`. The precedent claimed is
correct in both; only the ranges are loose.

### N2 — `nitpick` — the manifest entry's shape is under-specified for the party that must parse it

S3 fixes "a unique, filesystem-safe item id on its own line, followed by that item's locator" and
assigns everything else in an entry to the worker plane. But the **driver** must extract each
locator to build the `analyst` payload (S2: "its item's locator (as written in the manifest)"),
so the driver is parsing a format the other half owns. Whether the locator is bare or labelled,
and whether the worker may insert a size line between the id and the locator, is open. I am
filing this as a nitpick rather than higher because the consumer is an LLM agent reading
markdown, not a parser, and such a reader tolerates the variation.

---

## The four questions

**1. Coverage.** Ten files, five and five, no orphan and no double-claim. I checked each defining
property of the task against an owner: decompose/size/strategy → worker file 2 + S7; N cold
analysts → worker file 3 + driver dispatch + S5; cold verification → worker file 4; agreement-
ranked merge → worker file 5 (**degraded by F1**); blind roll-up → S4 + S3 Invariant B; per-corpus
config → driver, wholly; restart/resume → driver + Invariant A (**degraded by F1**); facts-not-
interpretation → worker file 1. Testing a real run is declared owned by neither — declared out,
not forgotten, and outside "plan the implementation". **No coverage finding.**

**2. The seam.** Stated, and stated identically inside both halves — which is the right move given
that neither planner sees the other's text. It is genuinely narrower than round 2's: no schema, no
layout, no key set. My two `major` findings are both against the *same* gap in it, and it is a
gap that shrinking created: driving every path and value down through the payload made the payload
the only channel, and the payload carries no invocation context. That is the price of the round-3
move, and it costs one field to pay.

**3. The floor.** Five files per half, each step "one file created, with the content that goes in
it specified" — five times the floor on both sides, and each half is itself divisible. **Neither
half falls below it. No finding.** The division's own note that a file-phrased floor gives the
install action no shape is correct and correctly handled — recorded rather than worked beneath.

**4. Real joint or arbitrary cut?** **Real.** What differs across the boundary is what a file's
reader knows when it reads it, and that is not a symmetry argument — it determines what each file
may assume, which is the only thing a prompt file has. The house shape independently exhibits the
same two kinds: `Guarded_change/SKILL.md:32` has the driving agent *read* each stage file, while
`Guarded_change/stages/stage-3.md:8` says the charter "is given to the reviewer verbatim." One
kind is read by an agent that holds the run; the other is handed to one that holds nothing. The
corrected failure sets are now genuinely disjoint, with steering on the driver side where its
barrier lives. **No finding.**

## On alternatives

(a)–(d) are weighed with the cost of dividing named honestly (`Consensus` → `Union`, i.e. losing
per-step corroboration). I could not construct a better cut. Every alternative I tried either
re-created round 1's directional contract, co-owned a file, or produced a seam that ran through
more files rather than between them. **If this division is rejected on F1 and F2, the right next
move is to repair S2 and S3 — not to look for a different boundary.**
