# Stage 2 — Plan: how to build the Architect skill

Formalizes the approved plan's **Build-approach** + **Settled-decisions** into: how to build,
how each `1.5` criterion is measured, what instrumentation the conformance dry-run needs, and the
severity→routing thresholds. Greenfield / conformance-only: no stage-0 baseline, no standing
regression metrics; stage 8 runs the config's `check` procedure.

---

## Build approach (files + order)

Built **inside** the guarded-change loop using **skill-creator** to scaffold and to run
`quick_validate.py` / `package_skill.py` — not as a freehand step. The family layout extends
skill-creator's default (`references/` + `scripts/`) with top-level `METHODOLOGY.md` + `stages/` +
`charter.md`; this still validates because only `SKILL.md` + valid frontmatter is required.

Build order (each step's artifact is what a later criterion is measured against):

1. **Scaffold** with skill-creator (`~/SKILL.md` frontmatter skeleton) → establishes S1's target.
2. **`charter.md`** — fork `Guarded_change/stages/charter.md` at its current commit; add the
   **fork-provenance blockquote** (source path + commit + carried-vs-dropped, mirroring Dragonfly's)
   and the **Completeness** sixth lens with an earned-clean clause. → S3.
3. **`METHODOLOGY.md`** — why it exists; Layer-1/Layer-2 split; the **config contract** (domain +
   scale context, per-plan-type required sections, catalog pointer, off-limits paths, run-root
   **OUTSIDE** any target repo); the recursion + lean-orchestrator model; the **7-section artifact
   spine** verbatim; what a run produces (the on-disk tree); a Stage index table. → S4, S6.
4. **`stages/*`** — one file per stage in house style (*What this stage does* → *Procedure* → named
   sub-rules with stable **mnemonic IDs** → *Cross-cutting rules*). Provisional set: frame +
   template-match; draft-plan-node (fill the spine); completeness-critic (3 cold); adversarial
   red-team (3 cold); gate (route by severity); granularity-check → decompose-or-leaf (+ top-level
   human gate); assemble; restart/resume. Assign mnemonic IDs and ensure each shared rule's
   statement matches its sibling statements (RAT3, gate-before-present, twin caps, restart contract,
   recursive-orchestration). → S2/SC2, B2, B3, B4, B6.
5. **`SKILL.md` (router)** — `name: architect`; pushy angle-bracket-free description; inputs
   (planning request + Layer-2 config + catalog); the completeness / two-pass red-team /
   gate-before-present rules **up front**; the stage table (resolving to the real stage files);
   self-check/dogfooding note. → S1, S3.
6. **`templates/seed/*`** — ≥1 generic seed skeleton + the skeletonize/match/reuse/back-propagate
   mechanism doc naming the user-space git-tracked catalog `~/.claude/architect/templates/`. → S5, B5.
7. **`examples/<plan-type>/*`** — one worked Layer-2 config; candidate "authoring a skill" with the
   Data-Distiller plan as a worked specimen.
8. **`README.md`** (optional, family convention).
9. **Validate + package** with skill-creator scripts (`quick_validate.py Architect`,
   `package_skill.py`). → S1.

Every rule that appears in more than one file gets a **mnemonic ID** at authoring time; the ID is
the instrumentation for S2/SC2 (grep the ID, diff the operative claim across sites).

## How each criterion is measured (stage-8 conformance) + instrumentation

The Layer-2 config's `check.how` defines the conformance harness: (1) `quick_validate.py`; (2)
cross-file consistency; (3) router-table resolution + charter fork-provenance present; (4) a
**dogfood dry-run** on a tiny fabricated task AND on the founding-failure fixture. This plan pins
each criterion to a concrete measurement and the instrumentation it needs.

| Criterion | Measurement | Instrumentation to add during build |
|---|---|---|
| **S1** | `quick_validate.py Architect` exit 0 + angle-bracket grep on description | none (script exists) |
| **S2 / SC2** | For each mnemonic ID, grep all sites, diff operative claim | **mnemonic-ID index** — a small table (in METHODOLOGY or a build note) listing each shared rule's ID + its statement sites, so the check is enumerable not ad-hoc |
| **S3** | Resolve each stage-table entry to a file; grep charter for provenance blockquote + Completeness lens | stage table must use resolvable relative paths; charter blockquote in a greppable fixed form |
| **S4** | Grep METHODOLOGY/seed for all 7 spine sections (esp. #4 "location/on-disk"), Layer-2 hook, generative-critic clause | spine written verbatim with stable section headings |
| **S5** | `ls ~/templates/seed/` non-empty; grep mechanism doc for user-space path + "git" + "back-propagat" | seed skeleton files present; mechanism doc |
| **S6** | Grep METHODOLOGY for contract fields + "outside any target repo" | contract stated in a fixed, greppable section |
| **S7** | In `SKILL.md`, assert rule-block line offset < stage-table line offset | rule block authored **before** the stage table (position-lens placement) |
| **B1** | Run completeness-critic pass on §4-removed (fixed-list) fixture → a record names missing outputs/location section; node blocked from finalize | **the founding-failure floor fixture** (a plan draft with §4 removed) + an **intact twin**; a **finalize-blocked marker** the dry-run can observe (absence of `assembled-plan.md` / a gate-state field in `_status.md`) |
| **B1b** | Run completeness-critic pass on an **off-list-holed** fixture (complete on the 7-spine + all Layer-2 required sections, missing a load-bearing section on **neither** list) → a record names the off-list gap by function; node blocked | **the generative-tier fixture** (e.g. a plan-type whose Layer-2 set never named rollback/migration, with that section removed) + an **intact twin**; a note stating which lists the removed section is absent from (the auditable "off-list" property); confirm a checkbox-sweep baseline would pass it |
| **B7** | Run a **pathological non-reducing** decomposition task → guard escalates (a `decisions.md` escalation / halted branch) within a bounded level count | **a pathological fabricated task** whose child granularity ≈ parent; a **reducing-decomposition twin** for the discrimination self-test |
| **B2** | On fabricated multi-node tree, confirm `completeness/`+`adversarial/` verbatim record-sets (3 each) at every node incl. root, **completeness recorded before adversarial** per node; unresolved finding ⇒ no `assembled-plan.md` | **fabricated multi-node task** + **planted root hole** + **planted between-branch-seam hole**; deterministic per-node dirs + record ordering as the observable |
| **B3** | Small task ⇒ no child nodes, granularity check recorded `leaf` | **small fabricated task**; granularity decision written to `index.md`/`_status.md` |
| **B4** | Large task ⇒ dispatch blocked until `plan/topgate/` exists; ≥1 deeper split proceeds red-team-only; leaves atomic | **large fabricated task**; `plan/topgate/` as the disk gate; gate-state observable in `decisions.md` |
| **B5** | Matching node instantiates skeleton; hole-fix ⇒ new commit in user-space catalog | **a seed skeleton the fabricated node matches** + a **git-tracked scratch catalog** for the dry-run; `git log` as the observable |
| **B6** | Per-branch sub-orchestrator spawned at first split; each holds only own-subtree context; HARDSTOP→resume re-plans no done node | **≥2-level fabricated tree**; per-node `_status.md`/`decisions.md`; a **HARDSTOP+resume** step; a way to inspect each orchestrator's held context (its transcript / its input set) |
| **SC1** | `diff -r` live vs. source (or packaged == reviewed tree) | none |
| **SC3** | advisory / N/A greenfield | none |

**Instrument before you build (CP3).** All fixtures above are **build deliverables authored during
stage 5**, because the criteria cannot be measured without them: the §4-removed floor fixture + its
intact twin (B1); the **off-list generative fixture** + intact twin, with a note stating which lists
the removed section is absent from (B1b — the pass-1 MAJOR's instrumentation); the multi-node tasks
with planted root/seam holes (B2); the small task (B3); the large task + `plan/topgate/` gate (B4);
the seed-matching node + scratch git catalog (B5); the ≥2-level tree + HARDSTOP/resume (B6); the
**pathological non-reducing task** + its reducing twin (B7); and the finalize-blocked/gate-state
observables. They live under the change folder (e.g. `changes/initial-authoring-2026-07/fixtures/`),
never inside a target repo. Any criterion whose governed path a single-process dry-run cannot
exercise (candidate: B6's true cross-process context isolation) is **surfaced to the human** at build
time, never silently satisfied by a proxy (CP5).

**Declared dry-run cost bound (dry-run representativeness, per the pass-1 red-team / Data-Distiller
precedent).** The production rule is 3 cold agents per pass × 2 passes at every node. A full
multi-node dogfood dry-run would fan out 6 real subagents per node. To keep the harness affordable
without proxying away the governed path, the dry-run is **bounded** as: (a) B1/B1b/B7 run the real
3-agent completeness pass on a **single node** (that is the governed path for those criteria); (b) B2
runs the full 3+3 fan-out on a **deliberately small tree** (root + 2 children = 3 nodes) so total
coverage incl. the root and one between-branch seam is genuinely exercised; (c) deeper-scale criteria
(B4/B6) may use a **reduced agent count per node** (≥1 cold agent per pass) since what they measure is
the *orchestration/gate/restart* structure, not the 3-agent count itself (which B2 already proves).
This bound is declared here so stage 8 cannot later be accused of a hidden representativeness proxy;
any criterion whose *own* governed property is the 3-agent count (B2) keeps the full count.

**Oracle-can-fail is mandatory (ST1.5f).** Every behavioral oracle (B1–B6) is first run against its
known-violating input (the self-tests named in `1.5-criteria.md`) and shown to fire, else that
criterion is `verified = no`. B1's discrimination self-test (intact twin **not** flagged) is the
canonical one.

## Position-sensitive-assembly note (this build IS one)

The skill files are prompts; order/adjacency is semantic (CP6). Greenfield means no prior
arrangement to preserve (SC3 is N/A), but the position lens still applies **within** this authoring:
the router's "rules up front" placement is **load-bearing** (asserted by S7). The **stage-file
ordering** is *not* itself the operative sequencer — the router's **stage table** (resolved by S3)
drives execution order — so file order is not load-bearing. The **charter's six lenses** are framed
as parallel, *distinct* attack angles ("kept distinct so one doesn't crowd out the others"), with no
precedence/override semantics among them; what is load-bearing there is **lens distinctness**
(Completeness present as a standing sixth lens with an earned-clean clause — asserted by S3), **not a
lens order**. The stage-3 reviewer is explicitly asked to apply the position lens to the *authored*
assembly (does a rule stated late in a stage file get overridden by an earlier statement? does the
router's up-front rule block actually precede the stage table?). No new shared-state accessor is
introduced (the disk-as-instrumentation model is append-only, single-writer-per-node), so the
concurrency lens (CP7/ST2b) does **not** fire — recorded here so the reviewer need not hunt for it.

## Severity → routing thresholds (stage-3 gate)

Routes on the **stage-3 reviewer's** worst finding (SEV1/SEV3), per `stages/stage-4.md`:

| Severity | Meaning here | Route |
|---|---|---|
| **Blocker** | wrong problem / a settled decision contradicted / a criterion unverifiable as written | → stage 1 (confirm direction; under delegation, stop-for-human) |
| **Major** | sound goal, materially wrong build approach (e.g. a criterion's oracle can't actually fire; a mechanic mis-mapped from the plan) | → stage 2 |
| **Minor** | real but local; fixable in place (wording, a missing cross-reference, a greppable-form fix) | fix → proceed |
| **Nitpick** | style/clarity | log → proceed |
| **Clean** | earned-clean per lens | → build (stage 5), freeze `1.5-criteria.md` |

Because this run is **plan/spec/criteria only** (front half), the gate-4 outcome routes among
{back-to-1, back-to-2, fix-and-proceed, ready-for-build}; **the orchestrator, not this subagent,
takes the ready-for-build artifact into stage 5.** Iteration cap (SEV4): 2 bounces at the same gate
on the same finding class → human tie-break (relayed per RAT3).

## What stage 8 will report (for orientation; not run in this front half)

Conformance-only verdict: per-criterion `verified = yes/no` with the evidence checked, each gating
criterion's disposition in `decisions.md`, and any gating criterion surfaced-to-human as
unverifiable-pre-ship. No regression section (no baseline).
