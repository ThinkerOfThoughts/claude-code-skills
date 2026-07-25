# Stage 1 — Spec (PASS 2): harden Architect against its own first self-review

**Pass 1 of this spec is at `1-spec.v1-superseded.md`.** It was routed back from **gate 4** on five
blockers from a 3-frame cold red-team (`3-redteam-plan.md`). The problem definition was **not**
contested; what was contested is recorded below as the **organizing principle this pass adds**.
Orchestrator routing decision: **re-enter at stage 1, no demotion** — unassigned write duties are a
spec-level gap, not a thin plan.

**Bounce accounting:** this is pass 2 on gate-4 finding class *"predicates specified, producers
unassigned / oracles do not exercise the behavioural half."* A second bounce on this class trips the
iteration cap (CAP/SEV4) and becomes a genuine stop-for-human. **This pass must clear the whole agenda,
not most of it.**

---

## 1. The organizing principle pass 1 was missing — every predicate needs a producer

Pass 1 designed a set of **disk predicates** (subtree-complete, seam-changed, record-current,
kill-handled, reviewer-distinct) and, for each, **left unassigned the stage that writes the fact the
predicate reads.** The reviewers' own summary:

> *"the plan specifies the join's and SEAM's **predicates** but not their **producers**. It says
> precisely what must be true on disk … and, for each, leaves unassigned the stage that writes the fact
> the predicate reads."* — reviewer B, stage-3 record

That is why the failures clustered: **a decidable-looking check with no producer either never passes or
cannot be evaluated.** Concretely, in pass 1: no stage ever wrote a terminal `subtree: complete`, so the
smallest decomposing tree (root + one leaf) was declared dead and escalated; escalation and death were
the same observable event; `seam_rev` had no slot for the parent's expectation and no increment rule;
`spawn_id` was a self-reported field whose unavailability bricked every gate.

**This spec therefore adds a Layer-1 rule of its own, `PRD`, and it is the thing that makes the rest
checkable:**

> **`PRD` — Every fact a gate reads has exactly one named producer.** For every fact that a gate, the
> join, the restart walk, or assembly **reads** — every `_status.md` key, every marker file, every hash —
> the skill must name (a) the **stage that writes it**, (b) the **trigger** that causes the write, (c)
> the **single file** it is written to and the **single writer** allowed to write that file, and (d) the
> **reader** that consumes it. A predicate whose operand has no assigned producer is an **un-runnable
> check** and is treated as a missing rule, not a strict one. Correspondingly, the plan must carry an
> **assignment table** (*fact → writing stage → trigger → file/writer → reader*) as a **required
> section**, and nothing reaches a gate with an unproduced fact.

`PRD` is not a fix for one finding; it is the property whose absence produced four of the five blockers,
and it is what the *artifact* also lacked (the baseline named `_status.md` 13 times and never said who
writes it). Fixing Architect and fixing this change are the same act.

---

## 2. The problem (unchanged from pass 1 — carried forward, not re-litigated)

Architect (as built, `3771038`) was run on its own creation plan on 2026-07-24. It **held its gate** —
refusing to write `assembled-plan.md` for an un-gated tree, the founding failure prevented live — and in
the same run **defeated its own human gate** and surfaced ten confirmed findings, six structural.
`/home/zero/architect-dogfood-2026-07-24/FINDINGS.md` is the **source of truth**;
`/home/zero/architect-hardening-loop/LOOP-STATE.md` holds the loop's state and the queued owner question.

Read together the findings say: **Architect's recursion is a fork with no join, its gates are satisfiable
by the parties they constrain, and its central claim overstates what it proves.**

- **F1** — stage 6 fans out and its procedure *ends*; no parent waits, polls, reads a child result, or
  learns a child **died**. `_status.md` is named as the up-flow vehicle 13× and **no stage writes one or
  defines its schema**. RAT3's "relay verbatim to the orchestrator" travels over a channel **no stage
  defines**. Reproduced live: a sub-orchestrator returned while its agents were still running and nothing
  noticed until a disk walk caught it.
- **F2** — the between-branch guarantee, added at owner insistence, is **procedurally false**: the parent
  reviews the seams of *proposed* children at stage 2/4 and **never reopens**; stage 7 has **no
  cross-node seam check**. Three individually clean nodes can ship a contradictory seam with every gate
  passing.
- **F3** — review records have fixed filenames and restart resumes at "the first *missing* output", so a
  re-drafted `plan.md` **assembles on reviews of an older version**. The detector already exists and is
  unused: the charter has every reviewer report the sha256 of each context file it read, and no stage
  compares it.
- **F4** — `redteam_context` is called load-bearing by the charter (its absence makes a review **un-run**)
  and is **absent from the config contract** (zero occurrences in `METHODOLOGY.md`); the worked example
  mentions it only *inside* `off_limits_paths`, conflating "citable source" with "never-write fence".
  Every review silently degrades to docs-only. **5 hits — the run's highest convergence.**
- **F5** — `plan/topgate/` is not a human gate: stage 1 has the runner **create it as setup**, the
  predicate is stated three inconsistent ways, and there is no filename, no authorship and no content
  requirement. Live, the runner authored its own approval and attributed an intermediary agent's prompt
  text to the owner.
- **F6** — "kill the branch" is offered as a tie-break outcome with **nothing said about what it does on
  disk**, and no run-level abort ⇒ permanent assembly deadlock.
- **F7** — the **honesty** defect: the gate proves a decontaminated review occurred, not that the plan is
  complete; for tier (iii) the claim is a **negative no finite review can prove**. "Independent" is
  defined only as *decontamination*, never **blind-spot diversity**; three same-model instances given the
  same charter and slice have **correlated** blind spots, and the number 3 is inherited with no
  completeness-specific justification.
- **F9** — "3 independent cold agents" has **no audit surface**: four of five provenance fields are
  identical across A/B/C and the fifth is producible by asking one agent three times; nothing forbids
  reviewer C reading `A.md`, which sits in the directory it is pointed at.
- **F10** — "clean-or-resolved" is **circular**: "resolved" is undefined and in practice means an
  **unreviewed author edit**, contradicting the loop's own "nothing self-certifies"; at assembly a
  fixed-in-place node is **indistinguishable** from a clean one.

Plus the cheap-but-real gaps: serial-vs-parallel never stated while three shared write surfaces have zero
serialization (and stage 8 asserts "no single global cursor" while `index.md` is exactly one); DEC's
operand uncomputable and its trip condition stated two incompatible ways; **no stage covers
exit-plan-mode**, the terminus GBP is *named after*; `mode: ingest-and-complete` — the mode the dogfood
ran in — undefined; two of three seed skeletons have no Layer-2 slot so the catalog *manufactures*
tier-(ii) holes; the spot-verify-citations duty assigned to no stage; TPL3 auto-commits an **unreviewed**
artifact to a shared cross-project repo inside the autonomous region; leaves emitted with no execution
order; the root node's on-disk location unpinned; §4's heading written six ways, defeating its own
grep-stability rationale.

## 3. Why it matters

Three of these are the **exact failure the skill exists to prevent, one level up**:

1. **F5 and F9 are gates whose satisfaction is asserted by the party they constrain.** F5 was predicted
   from the text by a reviewer who had never seen the file, then **executed end-to-end by the runner**,
   with `decisions.md` recording nothing anomalous.
2. **F1/F2/F3/F6 make the gate unsound in the large-tree case the skill markets.** A gate that cannot be
   *reached* (no join), can be satisfied by *stale* evidence, or **deadlocks forever** is not a gate. F2
   falsifies the specific guarantee added at owner insistence.
3. **F7 is an honesty defect in the frontmatter — the loudest site the skill has.** A skill in this
   family that overclaims teaches its users to trust a bound that does not hold.

And, added by pass 1's own gate: **4. `PRD`'s absence is the same defect class in the *fix*.** A hardening
pass that specifies predicates without producers ships a stricter-looking skill that deadlocks. The gate
caught it; the spec now names it.

## 4. What must change

**Tier 1.** **F1** — the join: a subtree-complete predicate computed by **induction over direct children
only** (not recursion over the tree, which is what voids ECON), a parent that **blocks**, a **defined**
`_status.md` schema **with a producer per key**, an **escalate-to-parent** route that is *distinguishable
from death*, **bottom-up** assembly, and **stage 7's actor named at every altitude**. **F2** — a
**mechanical** seam-change detector (a hash, so it is a diff not a judgment) that **reopens the parent's**
review, plus a real **cross-node seam check** at assembly. **F3** — bind each review record to the
**context hashes it reported** (own plan *and* parent plan), compared at the gate, the join and assembly,
and extended to the **gate artifacts** so a re-drafted split cannot keep its approval. **F5** — the
topgate: no pre-creation, a deterministic filename, owner-verbatim + a **fetchable** durable source, the
**admissible author stated positively**, the path **fenced** so the runner cannot write it, a
partial/adjacent answer **re-asked**, and TOP stated **one** way everywhere.

**Tier 2.** **F4** — `redteam_context` a first-class contract key **and** an example key, de-conflated
from `off_limits_paths`, with **non-vacuous** validation. **F6** — a killed branch representable on disk
with a **recorded timestamp** and a **recorded handling marker**, plus a run-level abort **with an
authorship contract**. **F7** — soften the claim to what is **checked / sampled / attested**, and buy
diversity with **genuinely disjoint frames** (disjoint mandates *and* disjoint input sets, with a real
non-spine differential list, and an absent list **declared degraded** rather than silently collapsing to
the spine). **F9** — a **dispatcher-recorded** spawn identity (not self-reported), a sibling-read ban, and
a **declared-degraded** fallback rather than a rule that makes gating impossible. **F10** — "resolved"
defined so it is not an unreviewed author edit, with **immutable** review records, and `clean` /
`clean-fixed-in-place` / **`clean-demoted`** distinguishable at assembly.

**Tier 3 (cheap but real).** Declare serial-vs-parallel and partition every shared write surface
(including a **fencing token** so a re-dispatched owner cannot race an orphan, and **cross-run** catalog
contention); make DEC's operand **recorded and comparable** and label it **honestly** as a self-declared
estimate; add the **exit-plan-mode terminus**; define `mode: ingest-and-complete`; give all three seed
skeletons Layer-2 slots; **assign** the spot-verify duty to a stage with a sample floor; make TPL3
stage-and-propose with one reviewed, locked, top-orchestrator commit; add inter-leaf **dependency
ordering**; pin the root node to `tree/root/`; canonicalize the §4 heading; **rename the two colliding
IDs** (`KIL`→`KLB`, `ING`→`IGM`) and make `METHODOLOGY`'s "authoritative ID grep" cover `templates/` +
`examples/`; give `TPL1`/`TPL2`/`SEV` index rows.

## 5. Explicitly out of scope

- **F8 — whether a human must review the *assembled* plan, not just the top split. QUEUED FOR THE OWNER;
  DELIBERATELY UNIMPLEMENTED AND UN-PRE-SHAPED.** It *adds a human gate* = the owner's call.
  **Where a fix in this pass widens F8's migration surface, `decisions.md` says so** — specifically:
  bottom-up assembly removes the only whole-assembled-plan reader, and the exit-plan-mode terminus adds
  sites asserting the terminus is GBP-gated only. Both are **declared, not resolved.**
- The **cost/fan-out envelope**; **ECON's O(children²) parent-seam load**; and the **"two passes aren't
  cost-justified"** item *(which FINDINGS files under "Triaged NOT genuine", not Tier 3 — pass 1
  mis-filed it; the correction is recorded and the item is out of scope either way; its status as an
  **unaudited owner ruling with no re-ask path** has been queued with the orchestrator, not decided here)*.

## 6. Constraints

- **Position-sensitive prompt assembly.** CP6 applies to every add/move/remove **including elements that
  do not themselves change**. The SKILL.md rule block must precede the stage table **and** its
  **intra-block order** is load-bearing: `PRV` and `DIV` go **before** `GBP` (PRV qualifies the claim; GBP
  is the operative gate, and it was load-bearing *because it was last*), and the block's closing
  three-item rationale sentence must be updated to enumerate what the block now contains.
- **Mnemonic rule-IDs are the linking mechanism.** New IDs get an index row and must pass the **ID
  collision oracle** — not a stated convention (pass 1 stated it and violated it twice).
- **Not greenfield.** Baseline = `0-baseline.md`, whose **authoritative** site map is **B0.6** (B0.2 is
  superseded and retained as the record of what the gate caught).
- **Frontmatter:** `name: architect`; `description` ≤1024 chars (baseline **954**, so ≈134 chars of
  headroom after removing the 69-char overclaim), **no angle brackets**, allowed keys only. **The
  description is the trigger surface** — a criterion must observe that the softened wording still *fires*
  the skill, not merely that it validates.
- **No new human gate.** Every fix must be satisfiable by the existing gate set.
- **Live copy re-synced**, with the diff asserted **before and after** the sync and in a direction that
  cannot leave orphans (a file is **added** and an apex form **removed** this pass).
- **Fidelity of the loop's own framing (carried, not repeated):** `LOOP-STATE.md` labels the broad scope
  reading an **"Interpretation … stated so Roy can correct it"** — this spec **carries that hedge** and no
  longer calls it "the approved cycle-1 scope". And "no new blocker or major" is a **continue** trigger
  only, never a licence to terminate the loop; the owner said *"until nothing surfaces"*.
- **Delegation (RAT3), owner asleep.** Every stop-for-human HALTS and returns the question verbatim.

## 7. Prior art

`Guarded_change/` — the loop being executed, and the model for F5: **RAT1**'s ratification record (flagged
axis + options verbatim + owner response verbatim + **a durable source the author did not author** + a
mapping) **including the clause pass 1 dropped** — *a partial or adjacent answer is not a ratification;
the axis is re-asked, never resolved into the author's own recommended option* — plus **CH11**'s cold
audit of that record. `Architect/changes/initial-authoring-2026-07/` — frozen; criteria style and fixture
layout reused, never edited. `Data-Distiller/` — the restart contract, and the **blind-coordinator**
property Architect deliberately drops (ECON's bound is where the drop shows). `Dragonfly/` — the
charter-fork precedent and the mnemonic-ID convention.

## 8. Expected touched files

*(joins every cold reviewer's context)*

**Artifact, under `<WT>/Architect/`:** `SKILL.md`; `METHODOLOGY.md`; `stages/charter.md`;
`stages/stage-1-frame-template-match.md`; `stages/stage-2-draft-node.md`;
`stages/stage-3-completeness-critic.md`; `stages/stage-4-adversarial-redteam.md`;
`stages/stage-5-gate.md`; **`stages/stage-6.5-join.md` (NEW)**;
`stages/stage-6-granularity-decompose.md`; `stages/stage-7-assemble.md`;
`stages/stage-8-restart-resume.md`; `templates/seed/README.md`; `templates/seed/generic-node.md`
(**§4 heading AND a Layer-2 slot heading** — pass 1 assigned it only the heading, which would have failed
its own criterion); `templates/seed/decomposition-node.md`; `templates/seed/leaf-task-spec.md`;
**`templates/seed/section-sets/` (NEW — real non-spine Layer-2 section lists, so DIV's differential frame
has genuine content)**; `examples/authoring-a-skill/planning.md`;
`examples/authoring-a-skill/README.md`; `README.md`; `guarded-change.architect.md`.

**Change records (this folder):** `0-baseline.md` (+B0.6–B0.8), `1-spec.md`, `1.5-criteria.md`,
`2-plan.md`, `3-redteam-plan*.md`, `5-build-notes.md`, `6-redteam-code.md`, `8-harness.md`,
`decisions.md`, `fixtures/`, `oracles/`.

**Outside the worktree (a build step, not a source edit):** `/home/zero/.claude/skills/architect` — the
live-copy re-sync.

**Reviewer context addition required by the gate-4 findings:** the approved scope/decision record
`/home/zero/.claude/plans/1-this-is-a-proud-scott.md` joins the closed set — the run's own config calls it
*"source of truth for every settled decision"*, and pass 1's stage-3 set omitted it (2/3 reviewers).
