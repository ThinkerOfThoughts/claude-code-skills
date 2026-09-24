# Stage 1 — Spec: authoring the Architect skill

**Change slug:** `initial-authoring-2026-07`
**Subject:** greenfield authoring of a new skill, `architect`, the fourth sibling in the
gated-discipline family (Dragonfly / Guarded_change / Data-Distiller / **Architect**).
**Source of truth:** `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` (the approved
scope/decision record, sha256 `2b44e6b3…3b89ce629`, recorded in `decisions.md`). This spec
**formalizes** that record for the guarded-change loop; it does not re-decide anything. Where a
design choice is stated below, the plan already settled it — the spec's job is to make each
choice checkable, not to reopen it.

---

## The problem — the founding failure

In a just-finished planning session (designing the Data-Distiller skill), a plan **looked
complete** and had reached the move to exit plan mode before anyone noticed it shipped with **a
whole load-bearing section silently missing** — the run's output-folder structure. Roy caught it
by hand. Nothing in the process would have caught it: the plan read as finished, the model was
confident, and the confidence was mistaken for completeness.

Stated generally: *a plan looked complete but was missing a load-bearing section, and only a
human catch prevented it.* That is the exact failure Architect exists to guard against. It is the
planning-domain instance of the two failure modes the whole family targets — an **unchallenged
judgment** ("this plan is sound") and an **unmeasured gap** (no bar that would have flagged the
missing section) — and the guard is the same shape as the siblings': completeness is **proven,
not asserted**, by a contract-floor plus independent cold critics, before the plan is presentable.

## What Architect is

A **standalone** skill that produces a **plan/design artifact**. It targets **no downstream
contract**: consumers — Dragonfly, Guarded_change, Data-Distiller, a skill that does not exist
yet, direct implementation with no skill, or Roy acting entirely outside a computational context
— ingest the emitted plan and check it against *their own* needs at *their* ingestion point.
Architect owns exactly one thing: **producing a complete, hole-free, adversarially-tested plan and
proving that completeness before the plan is presentable.**

It generalizes on two axes:
- **Domain** — *what* is being planned (a swappable Layer-2 example / config).
- **Scale** — *how big* the thing is. Small → a single low-level pass, then done. Large →
  recursive decomposition into sub-plans, high abstraction first, dividing down until leaves are
  atomic, agent-executable task specs.

It shares the family DNA: router `SKILL.md` + `METHODOLOGY.md` (Layer-1 agnostic core / Layer-2
config contract) + `stages/` (house style: *What this stage does* → *Procedure* → named sub-rules
with stable mnemonic IDs → *Cross-cutting rules*) + a **forked** `charter.md`; twin iteration
caps; stop-for-human under delegation (RAT3).

## What it must do (the settled mechanics, formalized)

These are the plan's Settled-decisions, restated as obligations the built skill must satisfy. Each
maps to one or more acceptance criteria in `1.5-criteria.md`.

1. **Completeness mechanic — the founding-failure gate.** Three tiers: (i) a Layer-1 **universal
   spine** every plan node must fill (the 7 sections below); (ii) a Layer-2 **per-plan-type
   required-section set**; (iii) a **generative completeness critic** that catches load-bearing
   sections *neither list anticipated* — the omitted output-folder section is exactly the kind a
   fixed checklist misses. The contract is the floor; the critic is what actually catches the
   unanticipated gap. Not a checkbox sweep — the critic is generative.

2. **Two distinct cold red-team passes per plan node** (two passes, not one combined):
   - **Completeness-critic** — **3 independent cold agents**, mandate *"what's missing here — a
     section, an interface, an output location, a failure mode, a state/restart story?"*. Runs
     first (is the skeleton whole?). Verbatim record. **Gate #1.**
   - **Adversarial red-team** — **3 independent cold agents**, running the forked charter's
     lenses, mandate *poke holes* (overlooked items, uncovered contingencies, false assumptions,
     better approaches left on the table). Runs second (given it is whole, does it break?).
     Verbatim record. **Gate #2.**
   - **Gate-before-present:** a plan node cannot be finalized / presented / exit-plan-mode'd until
     **both** passes are on record and **clean-or-resolved**. This is the direct gate on the
     founding failure.
   - **Total coverage, run per-owner.** Both passes run at **every node and every altitude**,
     executed by the **(sub-)orchestrator that owns that node** over **its own slice** — the
     node's `plan.md`, its decomposition, and the **seams among its children** — **including the
     top orchestrator on the root plan + the top-level split**. Whole-plan coverage = union of all
     node-level reviews **plus** each orchestrator's review of its own integration seams; a
     contingency living *between* two branches is caught by their common parent's pass, not lost in
     the gap between separate leaf reviews.

3. **Charter fork + a Completeness lens.** Fork the shared charter into Architect's own
   `charter.md` (family precedent: Dragonfly and Data-Distiller each own a forked copy) with a
   **fork-provenance blockquote** naming the source commit and what was carried vs. dropped. Add
   **Completeness** as a standing **sixth lens**. A clean Completeness verdict **must be earned** —
   it names the section-classes it checked and cites where each is covered (or flags the gap) —
   mirroring the charter's "a clean factual lens must be earned with citations."

4. **Recursion / scale / decomposition.** Iterative/recursive, generalizable in scale. Small →
   single pass. Large → decompose top-down. A cold **granularity check** per node (mirroring
   Data-Distiller's sizer) decides *decompose-further* vs. *leaf*; the two red-team passes validate
   the call. A **leaf** = an atomic, agent-executable task spec. **Apply catalog skeletons** when a
   node matches a known situation; **create a new skeleton** when it does not.

5. **Human gate on the top-level decomposition ONLY.** A human approves the first, high-level
   split (the major sub-plans + the **seams/interfaces between them**) before sub-planning
   dispatches. Deeper recursive splits proceed **red-team-gated, autonomous** (avoids gate fatigue
   on large trees). Stop-for-human for blockers / cap / missing-config still fires at any depth.

6. **Template catalog + back-propagation.** The catalog is a **git-tracked directory in
   user-space** (`~/.claude/architect/templates/`): user-space → cross-project reuse; git-tracked →
   audit trail + revertible back-propagation. The Architect repo ships a small generic **seed** set
   (`Architect/templates/seed/`) that populates the catalog on first run. **Back-propagation:** when
   a plan-fix patches a hole in a node that came from a skeleton, the fix is also applied to the
   **skeleton**, captured as a catalog commit. Layer-1/Layer-2 clean: the mechanism
   (skeletonize / match / reuse / propagate) is agnostic core; the catalog **content** is Layer-2
   data living outside the skill's core.

7. **Recursive orchestration / context economy.** Orchestration is **recursive**: the top
   orchestrator owns the root plan and the top-level decomposition, and **at the first major branch
   it delegates each branch to its own sub-orchestrator** (two at a binary first split). This
   recurses — the **orchestration tree mirrors the plan tree** (Data-Distiller's
   coordination-tree == aggregation-tree pattern). Each (sub-)orchestrator holds only **its own
   subtree's** skeleton + inter-node seams + terse child `_status` roll-ups, and reports a terse
   roll-up up to its parent — so **no single orchestrator's context scales with total tree size**,
   only with its own subtree's breadth. Unlike Data-Distiller, **blindness is NOT the goal**
   (planning needs a coherent cross-tree vision) — **context-economy is**: a parent holds its
   children's **seams** (it must, to keep the plan coherent) plus roll-ups, but **not** each
   child's full internal detail.

8. **Disk-as-instrumentation + restart contract** (from Data-Distiller): deterministic filenames
   + empty-dir-as-marker + append-only `decisions.md` → free restart, audit, and gate-enforcement.
   Run-root lives **OUTSIDE** any target repo. Restart contract: stage-done-iff-output-exists;
   trust-files-over-cursor; HARDSTOP mid-stage → re-run that node's current stage fresh.

9. **Twin iteration caps.** A **gate-bounce cap** (2 bounces at the same gate on the same finding
   class → human tie-break) plus a **decomposition/convergence guard** (recursion that is not
   reducing granularity → escalate). Under delegation (RAT3): a subagent hitting a stop **halts and
   relays the question verbatim** to its orchestrator; the orchestrator relays to the actual human
   and relays the answer back. The top-level decomposition gate is a mandatory human stop.

## The plan-artifact contract (what one node contains)

**Universal spine (Layer-1), each a required section:**
1. **Problem / intent** — what this node plans and why.
2. **Approach** — how, at this node's altitude.
3. **Interfaces & seams** — contracts to parent, siblings, children, and any consuming skill/human.
4. **Outputs & artifacts** — deliverables **and their locations** (incl. on-disk/output-folder
   layout — *the section whose silent absence was the founding failure*).
5. **Failure modes & contingencies** — what can go wrong and the fallback.
6. **State / restart story** — for anything long-running or multi-agent, how it resumes without loss.
7. **Verification** — how you'd know this node is done/correct.

Layer-2 adds **per-plan-type** required sections; the **generative critic** catches load-bearing
sections beyond both lists. A leaf node's spine collapses to an atomic, agent-executable task spec.

## On-disk layout (the run tree — modeled on Data-Distiller; run-root OUTSIDE any target repo)

```
<run-root>/
├─ RUN.md               ← self-contained runbook + restart procedure (apex resume)
├─ index.md             ← plan tree + per-node {template used, status, gate state, leaf?/decompose?}
├─ config/
│   └─ planning.md      ← domain + scale context, per-plan-type required sections, catalog pointer, off-limits paths
├─ plan/
│   ├─ decisions.md     ← append-only: gates, top-level-decomposition approval, red-team routes, overrides
│   └─ topgate/         ← the human top-level-decomposition approval artifact (dispatch blocked until it exists)
├─ tree/
│   ├─ _status.md       ← apex roll-up (the top orchestrator's lean surface)
│   └─ <node>/
│       ├─ _status.md         ← terse done-state + one-line roll-up + gate state
│       ├─ plan.md            ← this node's plan (the spine); template-instantiated when matched
│       ├─ completeness/      ← 3 cold-agent completeness-critic records (verbatim; gate #1)
│       ├─ adversarial/       ← 3 cold-agent adversarial red-team records (verbatim; gate #2)
│       └─ <child>/…          ← recurse to leaf task-specs
└─ assembled-plan.md    ← the collated deliverable: root plan + nested sub-plans → leaf task-specs
```

## Constraints (from skill-creator's validator — the build must satisfy)

- `name:` kebab-case, `architect`, ≤64 chars.
- `description:` ≤1024 chars, **NO angle brackets**, deliberately "pushy" for triggering.
- Allowed frontmatter keys only: `{name, description, license, allowed-tools, metadata,
  compatibility}`.
- skill-creator is used **inside** the loop to scaffold + run `quick_validate.py` /
  `package_skill.py` — not as a separate freehand step. The family layout (top-level
  `METHODOLOGY.md` + `stages/` + `charter.md` beyond skill-creator's default `references/` +
  `scripts/`) still validates, because only `SKILL.md` + valid frontmatter is required.

## Expected touched / created files (declared for the cold-reviewer context set)

All under `/home/zero/Desktop/claude-code-skills/Architect/` (the worktree copy at
`.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/`) unless noted. **Created** unless
marked:

- `SKILL.md` — router: `name: architect`; pushy description; inputs; completeness / two-pass
  red-team / gate-before-present rules up front; stage table; self-check/dogfooding note.
- `METHODOLOGY.md` — reference: why it exists; Layer-1/Layer-2 split; the config contract; the
  recursion + lean-orchestrator model; the artifact spine; what a run produces; a Stage index table.
- `stages/*` — one file per stage (house style + mnemonic rule-IDs). Provisional set: frame +
  template-match; draft-plan-node (fill the spine); completeness-critic (3 cold); adversarial
  red-team (3 cold); gate (route by severity); granularity-check → decompose-or-leaf (+ top-level
  human gate); assemble; restart/resume.
- `stages/charter.md` — forked cold-review charter + the Completeness lens + fork-provenance
  blockquote.
- `templates/seed/*` — the seed skeleton catalog + a short doc for the skeletonize / match /
  propagate mechanism and the user-space git-tracked catalog it syncs to.
- `examples/<one-plan-type>/*` — one worked Layer-2 config. Candidate: **"authoring a skill"** (the
  dogfood — Architect could have planned itself), with the Data-Distiller plan available as a
  worked specimen.
- `README.md` — optional, family convention (Data-Distiller ships one).
- **Modified:** none — greenfield; at run start the Architect repo dir holds only the Layer-2
  config (`guarded-change.architect.md`), the `changes/` folder, and empty placeholder dirs
  (`stages/`, `examples/`, `templates/seed/`) that contain no files yet.

The build additionally **writes into the user-space catalog** `~/.claude/architect/templates/`
(seeded on first run) — outside the repo, noted here so the reviewer knows a write target exists
beyond the touched-files list.

## Prior art (the reviewer's source set, priority-ordered)

1. The approved plan (`1-this-is-a-proud-scott.md`) — settles every decision above.
2. `Guarded_change/` — the primary architectural model to mirror (router + METHODOLOGY + stages +
   charter; RAT guards + Fidelity lens).
3. `Dragonfly/` — the charter-FORK precedent (provenance blockquote) + mnemonic rule-IDs.
4. `Data-Distiller/` — closest precedent (gated multi-agent skill; blind-router/static-pyramid
   orchestration; disk-as-instrumentation restart; human cut-gate). Treat its
   `changes/…/{2-plan,1.5-criteria}.md` as the stable decision record.
5. `skill-creator/` — frontmatter constraints + scaffold/validate/package scripts.

## Fidelity note — loaded operational terms (for the stage-3 fidelity lens)

Terms in this spec whose mechanism the build must implement (not a proxy), pinned to the plan:
- **"3 independent cold agents"** = three separately-spawned subagents with no shared context with
  the author and no shared context with each other's reasoning, per pass — not one agent asked
  three times, not a single reviewer.
- **"cold" / "independent"** = the guarded-change charter's meaning: a reviewer with *no shared
  context* with the author (CP1).
- **"generative critic"** = an open-ended "what is missing?" pass, not a checkbox sweep over the
  spine/required-section lists.
- **"recursive orchestration"** = a real sub-orchestrator delegation at each major branch, whose
  own context does not hold sibling subtrees' internals — not a single flat orchestrator looping.
- **"back-propagation"** = a git commit to the user-space skeleton catalog, not an in-memory or
  run-local note.
- **"human gate on top-level decomposition only"** = a hard stop whose approval artifact
  (`plan/topgate/`) must exist on disk before dispatch — deeper splits explicitly do **not** stop.
- **"gate-before-present"** = both passes clean-or-resolved *before* finalize/present/exit-plan-mode
  — a hard precondition, not advisory.

No prior "OWNER MUST RATIFY" fidelity finding is carried into this run (greenfield first pass).
