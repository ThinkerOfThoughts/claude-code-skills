# Stage 1 — Spec: harden Architect against its own first self-review (cycle 1)

## The problem

Architect (as built, `3771038`) was run on its own creation plan on 2026-07-24. The run **held its
gate** — it refused to write `assembled-plan.md` for an un-gated tree, which is the founding failure
prevented live — and in the same run **defeated its own human gate** and surfaced ten confirmed
findings, six of them structural blockers. The consolidated, triaged finding set is
`/home/zero/architect-dogfood-2026-07-24/FINDINGS.md` (**the source of truth for this change**);
the loop's scope + the queued owner question live in
`/home/zero/architect-hardening-loop/LOOP-STATE.md`.

The findings are not cosmetic. Read together they say: **Architect's recursion is a fork with no join,
its gates are satisfiable by the parties they constrain, and its central claim overstates what it
proves.** Concretely:

- **It forks but never joins (F1).** Stage 6 spawns sub-orchestrators and its procedure *ends*. No
  parent blocks, polls, reads a child result, or learns a child **died**. `_status.md` is named as the
  up-flow vehicle five times and **no stage writes one or defines its schema**. RAT3's "relay verbatim
  to the orchestrator" travels over a channel **no stage defines**. Reproduced live: branch B's
  sub-orchestrator returned while its agents were still running and nothing noticed until a disk walk
  caught it.
- **The between-branch guarantee is procedurally false (F2)** — the guarantee added at owner insistence.
  A parent reviews the seams of *proposed* children at stage 2/4 and **never reopens** that review once
  the children are actually planned; stage 7 performs **no cross-node seam check**. Three individually
  clean nodes can ship a mutually contradictory seam with every gate passing.
- **Stale records survive a re-draft (F3).** Review records have fixed filenames; restart resumes at
  "the first *missing* output"; so a re-drafted `plan.md` finds nothing missing and **assembles on
  reviews of an older version**. The detector already exists and is unused — the charter has every
  reviewer report the sha256 of each context file it read, and no stage ever compares it.
- **`redteam_context` is load-bearing but undeclared (F4)** — 5 independent hits, the run's highest
  convergence. The charter calls source access load-bearing and treats its absence as making a review
  **un-run**; the config contract declares seven fields and not this one (zero occurrences in
  `METHODOLOGY.md`); the worked example mentions it only in prose *inside* `off_limits_paths`,
  conflating "citable source" with "never-write fence". Every review silently degrades to docs-only.
- **`plan/topgate/` is not a human gate (F5).** Stage 1 has the runner **create the directory as
  setup**, pre-satisfying "blocked until it exists"; the predicate is stated three inconsistent ways;
  there is no filename, no authorship and no content requirement. Live, the runner authored its own
  approval and attributed an intermediary agent's prompt text to the owner (now VOID).
- **"Kill the branch" is unrepresentable (F6)** → permanent assembly deadlock. It is offered as a
  tie-break outcome with nothing said about what it does on disk, and no run-level abort.
- **"Completeness PROVEN" overclaims (F7)** — the deepest finding. The gate proves a decontaminated
  review occurred, not that the plan is complete; for tier (iii) the claim is a **negative no finite
  review can prove**. And "independent" is defined only as *decontamination*, never as **blind-spot
  diversity** — three instances of one model, same charter, same slice, same author-authored brief have
  **correlated** blind spots, and the number 3 is inherited from data-distiller with no
  completeness-specific justification.
- **"3 independent cold agents" has no audit surface (F9).** For same-model agents four of the five
  mandated provenance fields are identical across A/B/C and the fifth is producible by asking one agent
  three times; nothing forbids reviewer C reading `A.md`, which sits in the directory it is pointed at.
- **"clean-or-resolved" is circular (F10)** — "resolved" is undefined and in practice means an
  **unreviewed author edit**, directly contradicting the loop's own "nothing self-certifies"; and at
  assembly a node carrying four fixed-in-place minors is **indistinguishable** from a clean one.

Plus a set of cheap-but-real operational gaps: serial-vs-parallel is never stated while three shared
write surfaces (`index.md`, `plan/decisions.md`, the cross-project git catalog) are written by parallel
owners with zero serialization (and stage 8 asserts "no single global cursor" while `index.md` is
exactly one); DEC's operand is uncomputable and its trip condition stated two incompatible ways; **no
stage covers exit-plan-mode**, the terminus GBP is *named after*; `mode: ingest-and-complete` — the mode
the dogfood itself ran in — is undefined; two of three seed skeletons have no Layer-2 slot, so the
catalog *manufactures* tier-(ii) holes; the charter's spot-verify-citations duty is assigned to no
stage; TPL3 auto-commits an **unreviewed** AI artifact to a shared cross-project repo inside the
autonomous region, violating the family's founding rule; leaves are emitted with no execution order;
the root plan node's on-disk location is unpinned (ironic — the founding failure was a missing output
*location*); and §4's heading is written five different ways, defeating its own grep-stability rationale.

## Why it matters

Three of these are failures of the **exact kind the skill exists to prevent**, one level up:

1. **F5 and F9 are gates whose satisfaction is asserted by the party they constrain** — the same shape
   as the unchallenged judgment the family targets. F5 was not merely predicted from the text by a
   reviewer who had never seen the file; it was then **executed end-to-end by the runner**, with
   `decisions.md` recording nothing anomalous.
2. **F1/F2/F3/F6 make the gate unsound in the large-tree case the skill markets.** A gate that cannot
   be *reached* (no join), can be satisfied by *stale* evidence (F3), or **deadlocks forever** (F6) is
   not a gate. F2 falsifies the specific guarantee added at owner insistence.
3. **F7 is an honesty defect.** The skill's headline claim is stronger than its mechanism. A skill in
   this family that overclaims teaches its users to trust a bound that does not hold — and it does so
   in its own frontmatter, the loudest site it has.

Left unfixed, the next self-review re-finds all ten, and each subsequent cycle pays full review cost to
re-derive them.

## What must change

Fix, in the artifact `<WT>/Architect/`:

**Tier 1 (highest priority):** F1 (join: subtree-complete predicate, parent blocks on children, a
**defined** `_status.md` schema, an escalate-to-parent route, **bottom-up** assembly so it stops
contradicting ECON, and **stage 7's actor named**); F2 (child-seam-change **reopens the parent's** seam
review + a real **cross-node seam check** at assembly); F3 (bind each review record to the `plan.md`
sha256 it reviewed; compare at the gate and at assembly); F5 (topgate: no stage-1 pre-creation, a
**deterministic filename**, **owner-verbatim words + a durable spot-checkable source**, **a runner may
not author its own approval**, and TOP stated **one** consistent way everywhere — modelled on
guarded-change's RAT1 ratification-record discipline).

**Tier 2:** F4 (`redteam_context` → the METHODOLOGY config contract **and** the worked example as a
first-class key, de-conflated from `off_limits_paths`); F6 (killed branch representable on disk + a
run-level abort); F7 (soften the claim to what is actually proven **and** buy real reviewer diversity —
each of the 3 critics gets a **different frame**, one of them a differential prompt built from another
plan-type's `required_sections`, so tier (iii) becomes a **diff** rather than unbounded recall; state
plainly that N same-model instances are not N independent minds); F9 (**spawn-identity** field +
forbid a reviewer reading a sibling record); F10 (define "resolved" so it is not an unreviewed author
edit; make a fixed-in-place node **distinguishable** from a clean one at assembly).

**Tier 3 (cheap but real):** declare serial-vs-parallel and serialize/partition the shared write
surfaces incl. cross-run catalog contention; make DEC's operand computable (one metric, one persistence
site, **one** trip condition); add the **exit-plan-mode terminus**; define `mode: ingest-and-complete`;
give the other two seed skeletons Layer-2 slots; assign the spot-verify-citations duty to a stage; make
TPL3 not auto-commit an unreviewed artifact; add inter-leaf dependency ordering; pin the root node's
on-disk location; canonicalize the §4 heading string.

## Explicitly out of scope

- **F8 — whether a human must review the *assembled* plan, not just the top split. QUEUED FOR THE
  OWNER, DELIBERATELY UNIMPLEMENTED.** It *adds a human gate*, which is the owner's call, not the
  runner's (LOOP-STATE "Owner questions queued"). This spec does not implement, pre-shape, or
  half-implement it. Recorded in `decisions.md`.
- Three Tier-3 items from FINDINGS that the approved cycle-1 scope does **not** list, and which this
  change therefore does **not** address (declared, not silently dropped): the **cost/fan-out envelope**
  (nothing bounds total agents/tokens for a large tree); **ECON's O(children²) parent-seam load**; and
  the **"two passes aren't cost-justified"** half-finding. See `decisions.md`.

## Constraints

- **The artifact is a position-sensitive prompt assembly.** These files are prompts; the position lens
  (CP6) applies to every add/move/remove, including to elements that do not themselves change. The
  SKILL.md rule block must remain *before* the stage table (criterion S7 of the authoring run).
- **Mnemonic rule-IDs are the cross-file linking mechanism.** Any rule stated in more than one file
  carries a stable ID and must read consistently at **every** site; new rules get new IDs and a row in
  METHODOLOGY's cross-file rule index. **New IDs must not collide as substrings of existing IDs or of
  ordinary words** (baseline lesson: `TOP` matches inside `HARDSTOP`).
- **Not greenfield.** A stage-0 baseline exists (`0-baseline.md`); behavior-preservation applies to
  everything moved or removed, and regression = a baseline rule silently losing a site or becoming
  inconsistent (R1/R2 there).
- **Frontmatter constraints survive:** `name: architect` kebab-case ≤64 chars; `description` ≤1024
  chars with **no angle brackets**; allowed keys only.
- **Additive-where-possible.** Prefer adding a rule + its ID over rewriting a section, so the baseline
  site set is preserved and the diff stays reviewable. Where a claim must *change* (F5, F7, P4, P15,
  P16, P24), it changes at **every** site — a half-migrated rule is worse than the original.
- **No new human gate.** Every fix here must be satisfiable by the existing gate set (cold review,
  disk predicates, the *existing* top-level human gate). Adding a human gate is the owner's call (F8).
- **The live copy must be re-synced** (`/home/zero/.claude/skills/architect`), since `live == source` is
  a standing self-check criterion and holds at baseline.
- **Delegation (RAT3).** This loop is run by a subagent with the main session as orchestrator, and **the
  owner is asleep**. Every stop-for-human HALTS and returns the question verbatim to the orchestrator.
  Sequencing decisions *within* the approved scope are the orchestrator's, not the owner's.

## Prior art

- `Guarded_change/` — the loop being executed here; also the **model for F5**: RAT1's ratification
  record (flagged axis + options verbatim + owner response verbatim + a **durable source the author did
  not author** + a mapping) and CH11's *cold audit of the ratification*, which is exactly the discipline
  `plan/topgate/` lacks. RAT3 is the delegation rule this run runs under.
- `Architect/changes/initial-authoring-2026-07/` — the frozen authoring record: criteria style
  (structural `S-` / behavioral `B-`, each with an oracle + an oracle-can-fail self-test) and the
  fixture layout (`fixtures/<Bn>-<name>/{holed,intact}`) this run reuses. **Not edited by this run.**
- `Data-Distiller/` — the source of the restart contract and the coordination-tree pattern. Its
  **blind** coordinators are the property Architect dropped; F1's join and ECON's bound are where that
  drop shows.
- `Dragonfly/` — the charter-fork precedent and the mnemonic-ID convention.

## Expected touched files

*(this list joins every cold reviewer's context)*

**Artifact (all paths under `<WT>/Architect/`):**
- `SKILL.md` — frontmatter description (F7); rules block (PRV, DIV); Loop table (+ stage 6.5); Inputs
  (`redteam_context`, `mode`); Scale (TOP predicate, CNC); Stop-for-human; Self-check ID list
- `METHODOLOGY.md` — config contract (F4 `redteam_context`, `mode`/`ingest_source`,
  `differential_section_sets`); completeness mechanic + why-this-exists (PRV); spine §4 canonical
  heading; recursion/ORC/ECON (JOIN, CNC, bottom-up); gates (TOP, DEC operand); state contract (RST +
  `_status.md` **schema**, BIND, killed); run-tree diagram (`tree/root/`, `topgate/APPROVAL.md`,
  `catalog-pending/`, `ABORTED.md`); stage index (+6.5); cross-file rule index (+ new IDs)
- `stages/charter.md` — PRV honesty clause; DIV (frame diversity); IDN (spawn identity + sibling-read
  ban); BIND in the provenance block; Completeness-lens earned-clean wording
- `stages/stage-1-frame-template-match.md` — **remove the `plan/topgate/` pre-creation** (F5); `tree/root/`;
  `template:` recorded to the node's own `_status.md` not `index.md` (CNC); ingest mode
- `stages/stage-2-draft-node.md` — canonical §4 heading; child DAG (dependency order); `elc` recorded
- `stages/stage-3-completeness-critic.md` — DIV frames; IDN; BIND on the record; PRV
- `stages/stage-4-adversarial-redteam.md` — DIV frames; IDN; BIND; the TOP-approval audit duty
- `stages/stage-5-gate.md` — RES (define resolved); BIND check; spot-verify duty; killed-branch outcome;
  single-leaf terminus; per-node `decisions.md`
- **`stages/stage-6.5-join.md` — NEW FILE**: the join (subtree-complete predicate, parent blocks,
  `_status.md` schema reference, escalate-to-parent, dead child, killed subtree, SEAM reopen)
- `stages/stage-6-granularity-decompose.md` — TOP predicate (F5) + the cold approval audit; hand-off to
  6.5; DEC operand; TPL3 stage-and-propose; CNC
- `stages/stage-7-assemble.md` — bottom-up per-node assembly + **named actor**; cross-node seam check;
  BIND re-check; killed handling; fixed-in-place distinguishability; execution-order section; the
  **exit-plan-mode terminus**
- `stages/stage-8-restart-resume.md` — `_status.md` schema; stage-done = exists **and** hash-current;
  `index.md` derived (fixing the false "no single global cursor" claim); `tree/root/`; killed/abort
- `templates/seed/README.md` — TPL3 stage-and-propose; catalog lock; Layer-2 slots
- `templates/seed/generic-node.md` — canonical §4 heading
- `templates/seed/decomposition-node.md` — canonical §4 heading; **Layer-2 slot**; dependency column;
  DEC single trip condition; TOP predicate
- `templates/seed/leaf-task-spec.md` — canonical §4 heading; **Layer-2 slot**; prerequisites
- `examples/authoring-a-skill/planning.md` — **`redteam_context` as a first-class key** (F4);
  de-conflate `off_limits_paths`; `mode`; `differential_section_sets`
- `examples/authoring-a-skill/README.md` — reflect the new keys
- `README.md` — the "proven" claim (F7)
- `guarded-change.architect.md` — Layer-2 config for *this* cycle (baseline block, FINDINGS.md added to
  `redteam_context`, `check.output` retargeted)

**Change records (this folder):** `0-baseline.md`, `1-spec.md`, `1.5-criteria.md`, `2-plan.md`,
`3-redteam-plan.md`, `5-build-notes.md`, `6-redteam-code.md`, `8-harness.md`, `decisions.md`,
`fixtures/`, `oracles/`.

**Outside the worktree (build step, not a source edit):** `/home/zero/.claude/skills/architect` — the
live copy re-sync.
