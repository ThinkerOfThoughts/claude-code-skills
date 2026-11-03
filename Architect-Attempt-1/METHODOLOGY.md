# Architect — methodology

A method (and a Claude Code skill that runs it) for producing a **complete, hole-free,
adversarially-tested plan** and **proving that completeness before the plan is presentable** — for a
thing of any scale, in any domain, headed for any consumer (or none).

This document is the **orientation/reference spec**: why the loop exists, the two layers, the Layer-2
config contract, the completeness mechanic, the recursion + recursive-orchestration model, the
plan-artifact spine, the gates, the on-disk state contract, what a run produces, the stage index, and
the cross-file rule index. The **per-stage procedure** lives in `stages/` (one file per stage) + the
shared cold-review discipline in `stages/charter.md`; `SKILL.md` is the router that walks the loop.
This file is opened for orientation and config setup — not to run a stage.

It is deliberately **project- and domain-agnostic** — nothing here assumes a particular thing being
planned. Only the **Layer-2 planning config** holds domain specifics.

Architect is the fourth sibling of **guarded-change** (gated *change*), **dragonfly** (gated
*diagnosis*), and **data-distiller** (gated *distillation*): it borrows their Layer-1-core /
Layer-2-config seam, their cold-subagent independence discipline (forked — see `stages/charter.md`),
and data-distiller's disk-as-instrumentation restart contract and coordination-tree==aggregation-tree
orchestration. It composes with all of them by **soft handoff, no hard dependency**: the plan it emits
is consumer-agnostic — dragonfly, guarded-change, data-distiller, a not-yet-existing skill, direct
implementation, or a human acting outside any computational context each ingest the plan and check it
against *their own* needs at *their* ingestion point. Architect targets **no downstream contract**.

---

## Why this exists — the founding failure

In a just-finished planning session (designing the data-distiller skill), a plan **looked complete**
and had reached the move to exit plan mode before anyone noticed it shipped with **a whole load-bearing
section silently missing** — the run's output-folder structure. A human caught it by hand. Nothing in
the process would have caught it: the plan read as finished, the model was confident, and the
confidence was mistaken for completeness.

Stated generally: *a plan looked complete but was missing a load-bearing section, and only a human
catch prevented it.* That is the exact failure Architect guards against. It is the planning-domain
instance of the two failure modes the whole family targets — an **unchallenged judgment** ("this plan
is sound") and an **unmeasured gap** (no bar that would have flagged the missing section). The guard is
the same shape as the siblings': completeness is **proven, not asserted**, by a contract-floor plus
independent cold critics, before the plan is presentable.

Critically, the missing section was **unanticipated** — no fixed checklist named it. So a checklist
alone reproduces the failure on the *next* unanticipated section. The mechanic therefore has three
tiers, of which the third is the one that actually catches the founding failure's true shape.

---

## The two layers

- **Layer 1 — agnostic core** (`SKILL.md` + this doc + `stages/` + `stages/charter.md` + `templates/`
  mechanism). The loop, the completeness mechanic, the recursion + recursive-orchestration model, the
  plan-artifact spine, the template skeletonize/match/reuse/back-propagate **mechanism**, the state
  contract, the gates, and the shared cold-review discipline. Ships once; knows nothing about any
  specific thing being planned.
- **Layer 2 — per-plan config + catalog content.** The domain + scale context, the per-plan-type
  required sections, the catalog pointer, the off-limits paths — and the **catalog content** itself
  (skeletons), which is Layer-2 data living outside the skill's core. Supplied per run. This is the only
  place domain specifics live. `examples/authoring-a-skill/` is a worked instance.

---

## The config contract (Layer 2)

A planning config declares (see `examples/authoring-a-skill/planning.md` for a worked instance):

```yaml
plan_type: <name>              # what class of thing this run plans (e.g. "authoring a skill")

domain_context: |              # WHAT is being planned and the world it lives in — enough for a cold
                               # agent to judge whether a section is load-bearing. Dropped into the
                               # completeness-critic + adversarial briefs as shared context.

scale_context: |              # HOW BIG. Small → expect a single low-level pass (one leaf). Large →
                               # expect recursive decomposition, high-abstraction-first, down to atomic
                               # agent-executable leaves. Sets the granularity check's expectation.

required_sections:             # Layer-2 tier-(ii): plan-type-specific sections EVERY node of this type
  - <section name + why load-bearing>   # must fill, ON TOP OF the 7-section universal spine. The
  - ...                                 # generative critic (tier iii) still hunts for what's on NEITHER
                                        # this list NOR the spine.

catalog: ~/.claude/architect/templates/   # the git-tracked user-space skeleton catalog (cross-project
                                          # reuse + revertible back-propagation). Seeded from
                                          # Architect/templates/seed/ on first run.

off_limits_paths:              # paths the RUN must never write into and plans must treat as read-only
  - <path>                     # context (e.g. the target repo being planned FOR). Named to be fenced.

run_root: <path OUTSIDE any target repo>   # where the run tree is created. MUST live OUTSIDE any repo
                                           # the plan targets — a run-root inside the planned repo
                                           # silently pollutes the thing being planned.
```

Rules:
- **The run-root lives OUTSIDE any target repo.** Disk-as-instrumentation writes the whole run tree;
  putting it inside the repo being planned pollutes the planned artifact and corrupts its git history.
  This is a load-bearing safety constraint, not a convenience (**RST**).
- **Off-limits paths are named to be fenced, not visited.** The target repo (and any protected path) is
  read-only context; the run never writes into it. Naming is the fence — no guard catches a stray write
  the config never declared.
- **`required_sections` is the floor, never the ceiling.** It is tier (ii). The generative critic (tier
  iii) exists precisely to catch what this list did not anticipate — do not treat a full `required_sections`
  as "complete."
- **Do not invent plan specifics.** If no config exists, help author one against this contract; refuse
  to guess the domain, the required sections, or the off-limits set — guessing is the contamination this
  method prevents.

---

## The plan-artifact contract — the 7-section universal spine (Layer 1)

**Every plan node must fill each of these seven sections** (a leaf node's spine **collapses to an
atomic, agent-executable task spec** — the same seven concerns, compressed to what one agent needs to
execute without further planning). This is tier (i) of the completeness mechanic; it is stated here
**verbatim** so a cold critic and a grep both have a stable target (**SPN**):

1. **Problem / intent** — what this node plans and why.
2. **Approach** — how, at this node's altitude.
3. **Interfaces & seams** — contracts to parent, siblings, children, and any consuming skill/human.
4. **Outputs & artifacts** — deliverables **and their locations** (incl. on-disk / output-folder
   layout). *This is the section whose silent absence was the founding failure* — it is never optional,
   and a clean Completeness verdict must cite where the node's output **locations** are pinned.
5. **Failure modes & contingencies** — what can go wrong and the fallback.
6. **State / restart story** — for anything long-running or multi-agent, how it resumes without loss.
7. **Verification** — how you'd know this node is done/correct.

Layer-2 `required_sections` add **per-plan-type** required sections on top of the spine. The
**generative completeness critic (tier iii)** catches load-bearing sections **beyond both lists** — the
open-ended *"what is missing that neither list named?"* pass. Tiers (i)–(ii) are the **floor** a
checkbox sweep could satisfy; tier (iii) is the mechanic the skill most exists to embody (**CMP**).

---

## The completeness mechanic (three tiers + two-pass gate)

- **Tier (i)** — the 7-section universal spine (above). **Tier (ii)** — the Layer-2
  `required_sections`. **Tier (iii)** — the **generative** critic: *"what load-bearing section does
  neither list anticipate?"* The contract (i–ii) is the floor; the generative critic (iii) is what
  actually catches the unanticipated gap (**CMP**, **CMP2**).
- **Two distinct cold red-team passes per node** (two passes, not one combined), each **3 independent
  cold agents**:
  - **Completeness-critic** (stage 3, **gate #1**) — runs **first** (is the skeleton whole?). Mandate =
    the Completeness lens's three tiers. Verbatim record (**PASS1**).
  - **Adversarial red-team** (stage 4, **gate #2**) — runs **second** (given it is whole, does it
    break?). Mandate = the full six charter lenses, poke holes. Verbatim record (**PASS2**).
  - The completeness pass is **recorded before** the adversarial pass at each node — skeleton-whole gate
    precedes break-it gate (**PASS-ORD**).
- **Gate-before-present (GBP).** A plan node cannot be finalized / presented / exit-plan-mode'd /
  assembled until **both** passes are on record and **clean-or-resolved**. This is the direct gate on
  the founding failure — a hard precondition, not advisory.

---

## Recursion, scale, and recursive orchestration

- **Scale drives shape.** Small task → the granularity check returns **leaf**, the two passes validate
  the leaf call, done in a single low-level pass. Large task → **decompose top-down**, high abstraction
  first, dividing until leaves are atomic, agent-executable task specs (**GRN**).
- **Granularity check per node (GRN).** The owning orchestrator **proposes** the *decompose-further*
  vs. *leaf* call at draft time (stage 2) — mirroring data-distiller's **coordinator-run** sizer (a
  coordinator judgment, not a separately-spawned cold agent) — and the **two cold red-team passes
  validate it** (a wrongly-declared leaf, or a wrong decomposition, is a Completeness / Logical
  finding). **Coldness enters at validation, not at the proposal.** A **leaf** = an atomic,
  agent-executable task spec.
- **Recursive orchestration (ORC).** The **orchestration tree mirrors the plan tree**
  (data-distiller's coordination-tree == aggregation-tree pattern). The **top orchestrator** owns the
  root plan and the top-level decomposition; **at the first major branch it delegates each branch to its
  own sub-orchestrator** (two sub-orchestrators at a binary first split). This recurses — each interior
  `<node>/` is owned by a (sub-)orchestrator that further delegates at *its* branches.
- **Total coverage, run per-owner (COV).** Both passes run at **every node and every altitude**,
  executed by the **(sub-)orchestrator that owns that node** over **its own slice** — the node's
  `plan.md`, its decomposition, and the **seams among its children** — **including the top orchestrator
  on the root plan + the top-level split**. Whole-plan coverage = the **union of all node-level reviews
  plus each orchestrator's review of its own integration seams**. A contingency living *between* two
  branches is caught by their common parent's pass, not lost in the gap between separate leaf reviews.
  The top orchestrator dispatches the cold agents on the root; it does **not** self-certify.
- **Context economy, NOT blindness (ECON).** Unlike data-distiller (whose coordinators are structurally
  blind), Architect's orchestrators are **not** blind — planning needs a coherent cross-tree vision. The
  economy is different: each (sub-)orchestrator holds only **its own subtree's** skeleton + inter-node
  **seams** + terse child `_status` roll-ups, and reports a terse roll-up up to its parent. A parent
  holds its children's **seams/interfaces** (it must, to keep the plan coherent) plus roll-ups, but
  **not** each child's full internal detail. So **no single orchestrator's context scales with total
  tree size** — only with its own subtree's breadth.

---

## Template catalog + back-propagation

- The catalog is a **git-tracked directory in user-space** (`~/.claude/architect/templates/`):
  user-space → cross-project reuse (a skeleton distilled from planning project A is available for
  project B); git-tracked → audit trail + revertible back-propagation. The Architect repo ships a small
  generic **seed** set (`templates/seed/`) that **populates the catalog on first run** (**TPL**).
- **Match / instantiate (TPL1).** When a node matches a known situation, instantiate its skeleton into
  `plan.md`; record the template used in `index.md`. **Create-new (TPL2).** When a node matches no
  skeleton, plan it from the bare spine and, once gated clean, **distil a new skeleton** into the
  catalog (a catalog commit).
- **Back-propagation (TPL3).** When a plan-fix patches a hole in a node that came from a skeleton, the
  fix is **also applied to the skeleton** — captured as a **git commit** to the user-space catalog, not
  an in-memory or run-local note. This is guarded-change-on-itself self-improvement: the next project
  inherits the patched skeleton.
- Layer-1/Layer-2 clean: the **mechanism** (skeletonize / match / reuse / propagate) is agnostic core;
  the **catalog content** is Layer-2 data outside the skill's core. Full procedure in
  `templates/seed/README.md`.

---

## Gates and iteration caps

- **Gate-before-present (GBP)** — both passes clean-or-resolved before any node finalizes; the whole
  plan cannot assemble while any node is unresolved.
- **Top-level decomposition human gate — top level ONLY (TOP).** A human approves the **first,
  high-level split** (the major sub-plans + the **seams/interfaces between them**) before sub-planning
  dispatches — dispatch is **blocked until `plan/topgate/` exists on disk**. **Deeper** recursive splits
  proceed **red-team-gated, autonomous** (no human stop) to avoid gate fatigue on large trees. This is a
  precise decision: the gate fires at the top and **explicitly does not fire deeper**.
- **Twin iteration caps.** (1) **Gate-bounce cap (CAP):** 2 bounces at the same gate on the same finding
  class → human tie-break. (2) **Decomposition / convergence guard (DEC):** recursion that is **not
  reducing granularity** (a child whose atomic granularity ≈ its parent's, no real division into smaller
  work) is caught and **escalated** rather than recursing indefinitely. The guard declares a **concrete
  bound**: **if two consecutive levels do not reduce granularity — i.e. a child node's estimated leaf
  count / work-size is ≥ 0.8× its parent's — the branch escalates** (a `decisions.md` escalation) rather
  than recursing further. A genuinely-reducing decomposition does not trip it.
- **Stop-for-human under delegation (RAT3).** Blockers about to restart; the cap tie-break; a missing
  config; a gating criterion unverifiable pre-ship; the top-level decomposition gate; a stop at any
  depth. When a subagent runs this loop, **every** such stop **halts the subagent and returns the
  question verbatim to its orchestrator** to relay to the actual human — the subagent never self-answers
  or proceeds. The orchestrator relays to the human and relays the verbatim answer back, never answering
  as the owner.

---

## The on-disk state contract (RST)

- **All state is on disk.** `RUN.md`, `index.md`, `config/`, `plan/` (decisions, topgate), and `tree/`
  (with per-node `_status.md` + `plan.md` + `completeness/` + `adversarial/`) are the entire state. Chat
  history is not load-bearing — a fresh orchestrator resumes from `RUN.md` + the tree alone.
- **Deterministic filenames → "already produced?" is a path check.** `plan.md`, `completeness/A.md…C.md`,
  `adversarial/A.md…C.md`, `_status.md`, `assembled-plan.md` are fixed names. **Stage-done-iff-output-exists.**
- **Trust files over any cursor.** If a `_status.md` roll-up disagrees with what is on disk, the **files
  win**. State is per-node (no single global cursor to stale-edit).
- **Node identity = directory path.** An **empty node dir IS the "not planned yet" marker**.
- **HARDSTOP mid-stage → re-run that node's current stage fresh.** In-flight agents die on shutdown;
  their half-written outputs are ignored because stage-done is an output-exists check on the *complete*
  deterministic file. **Nothing completed is lost; only the interrupted node's current stage re-runs.**
- **Run-root lives OUTSIDE any target repo** (see the config contract) — the disk-as-instrumentation
  model depends on it.

---

## What a run produces (the run-root, OUTSIDE any target repo)

```
<run-root>/                 ← OUTSIDE any target repo (the planned repo stays read-only context)
├─ RUN.md                   ← self-contained runbook + restart procedure (apex resume)
├─ index.md                 ← plan tree + per-node {template used, status, gate state, leaf?/decompose?}
├─ config/
│   └─ planning.md          ← Layer-2: domain + scale context, required sections, catalog pointer,
│                             off-limits paths, run_root
├─ plan/
│   ├─ decisions.md         ← append-only: gates, top-level-decomposition approval, red-team routes,
│   │                         cap bounces, convergence escalations, overrides
│   └─ topgate/             ← the human top-level-decomposition approval artifact (dispatch blocked
│                             until it exists — TOP)
├─ tree/                    ← recursive plan nodes; each interior node owned by a (sub-)orchestrator
│   ├─ _status.md           ← apex roll-up (the top orchestrator's lean surface)
│   └─ <node>/
│       ├─ _status.md         ← terse done-state + one-line roll-up + gate state
│       ├─ plan.md            ← this node's plan (the 7-section spine); template-instantiated if matched
│       ├─ completeness/      ← 3 cold-agent completeness-critic records (verbatim; gate #1)
│       ├─ adversarial/       ← 3 cold-agent adversarial red-team records (verbatim; gate #2)
│       └─ <child>/…          ← recurse to leaf task-specs
└─ assembled-plan.md        ← the collated deliverable: root plan + nested sub-plans → leaf task-specs
```

Conventions that make the decisions structural, not disciplinary:
- **Gate-before-present is structural.** `assembled-plan.md` cannot be written while any node's
  `completeness/` or `adversarial/` set is missing or carries an unresolved finding.
- **Context economy is per-node.** A (sub-)orchestrator's readable surface is its own subtree's
  `plan.md` + child seams + child `_status.md` — not sibling subtrees' internals.
- **Empty dir = not-done marker.** The node structure fills in as planning proceeds.
- **`plan/decisions.md`** is the append-only gate/decision log for a *planning run* (distinct from the
  guarded-change change-records under `changes/` that authored this skill).

---

## Stage index

Walk the loop **per node**; the tree is walked depth-appropriately (a node decomposes only after it is
gated clean and the granularity check says decompose). At each stage read that stage's file for the
full procedure + the rules it applies.

| # | Stage — one-line purpose | Read |
|---|---|---|
| **1** | Frame + template-match: orient the node; match a catalog skeleton (instantiate) or mark create-new | → `stages/stage-1-frame-template-match.md` |
| **2** | Draft plan node: fill the 7-section spine + Layer-2 required sections + the proposed granularity (leaf, or a child decomposition + seams) | → `stages/stage-2-draft-node.md` |
| **3** | Completeness-critic: 3 independent cold agents, Completeness lens, skeleton-whole — **gate #1** | → `stages/stage-3-completeness-critic.md` (+ `stages/charter.md`) |
| **4** | Adversarial red-team: 3 independent cold agents, full six lenses, poke holes — **gate #2** | → `stages/stage-4-adversarial-redteam.md` (+ `stages/charter.md`) |
| **5** | Gate: route by worst finding across both passes; twin caps | → `stages/stage-5-gate.md` |
| **6** | Granularity check → decompose-or-leaf; the top-level human decomposition gate; convergence guard; spawn sub-orchestrators + recurse | → `stages/stage-6-granularity-decompose.md` |
| **7** | Assemble: collate root + nested sub-plans → leaf task-specs into `assembled-plan.md` (only when every node is gated clean) | → `stages/stage-7-assemble.md` |
| **8** | Restart / resume: the on-disk state contract; deterministic filenames; HARDSTOP → re-run that node's stage fresh | → `stages/stage-8-restart-resume.md` |

---

## Cross-file rule index (the mnemonic-ID linkage — S2/SC2 instrumentation)

Every rule stated in more than one file carries a **stable mnemonic ID**. To check cross-file
consistency, grep the ID across all sites and diff the operative claim. **The `Sites` column below is
indicative, not exhaustive** — the **authoritative** site set for any ID is
`grep -rln -- <ID> SKILL.md METHODOLOGY.md stages/` (the check greps the token, not the column, so the
table cannot silently under-list a site). The shared rules and their principal statement sites:

| ID | Operative claim (one line) | Sites |
|---|---|---|
| **GBP** | Both passes clean-or-resolved before a node finalizes / presents / exit-plan-mode / assembles | SKILL.md, METHODOLOGY.md, charter.md, stages 3/4/5/7 |
| **PASS1** | Completeness-critic = 3 independent cold agents, runs first (gate #1) | SKILL.md, METHODOLOGY.md, charter.md, stage 3 |
| **PASS2** | Adversarial red-team = 3 independent cold agents, runs second (gate #2) | SKILL.md, METHODOLOGY.md, charter.md, stage 4 |
| **PASS-ORD** | Completeness pass recorded before adversarial pass at each node | METHODOLOGY.md, stages 3/4/5 |
| **CMP** | Three-tier completeness: spine + Layer-2 list + generative critic (floor vs. catch-the-unanticipated) | SKILL.md, METHODOLOGY.md, charter.md, stage 3 |
| **CMP2** | The critic is generative, NOT a checkbox sweep | METHODOLOGY.md, charter.md, stage 3 |
| **SPN** | The 7-section universal spine, §4 = Outputs & artifacts with locations (founding-failure section) | METHODOLOGY.md, charter.md, stages 2/3, templates/seed |
| **COV** | Total coverage: both passes at every node incl. root + top-level split; union + own-seam reviews | SKILL.md, METHODOLOGY.md, charter.md, stages 3/4/6 |
| **ORC** | Recursive orchestration: orchestration tree mirrors plan tree; sub-orchestrator per branch | SKILL.md, METHODOLOGY.md, stage 6 |
| **ECON** | Context economy (not blindness): each orchestrator holds only its own subtree + seams | SKILL.md, METHODOLOGY.md, stage 6 |
| **GRN** | Granularity call: orchestrator proposes leaf vs. decompose (stage 2), cold passes validate; leaf = atomic agent-executable task spec | SKILL.md, METHODOLOGY.md, stages 2/6 |
| **TOP** | Top-level decomposition human gate ONLY; `plan/topgate/` must exist before dispatch; deeper splits autonomous | SKILL.md, METHODOLOGY.md, stage 6 |
| **CAP** | Gate-bounce cap: 2 bounces same gate/finding-class → human tie-break | SKILL.md, METHODOLOGY.md, charter.md, stage 5 |
| **DEC** | Convergence guard: non-reducing recursion (≥0.8× parent granularity, 2 levels) → escalate | SKILL.md, METHODOLOGY.md, stage 6 |
| **TPL** | Template catalog: git-tracked user-space `~/.claude/architect/templates/`, seeded from `templates/seed/` | METHODOLOGY.md, SKILL.md, templates/seed/README.md, stage 1 |
| **TPL3** | Back-propagation = a git commit to the user-space skeleton catalog on a hole-fix | METHODOLOGY.md, templates/seed/README.md, stages 1/6 |
| **RST** | Restart contract: on-disk, stage-done-iff-output-exists, trust-files-over-cursor, HARDSTOP→re-run fresh, run-root OUTSIDE any target repo | METHODOLOGY.md, SKILL.md, stages 1/2/6/7/8 |
| **RAT3** | Delegation stop-for-human: halt + relay the question verbatim; never self-answer | SKILL.md, METHODOLOGY.md, charter.md, stages 5/6 |
