# 1 — Spec: per-stage restructure (Theme 1) + untangle the guarded-change coupling (Theme 2) of the dragonfly skill

## The problem

Two structural findings from the dragonfly hardening run (`changes/audit-hardening-2026-07/9-report.md`),
both deferred there as "yours to decide, each its own run," now decided by the owner (2026-07-06,
memory `skills-structural-decisions-2026-07`):

- **D-S1 — Attention budget.** `Dragonfly/METHODOLOGY.md` (521) + `SKILL.md` (149) = **670 lines,
  combined *exactly at* the hardening run's frozen cap, zero headroom.** They are organized **by
  topic** (core principles, the representativeness gate, the triage, the charter, the severity
  model, the gate-before-present rule, the config contract), so an agent running any single stage
  of the hunt must hold the whole document in view and locate the rules that apply to where it
  actually is. This is the same Opus attention-budget ceiling flagged as **S1** for guarded-change:
  past some size each added rule dilutes the others, and a rule that gets *missed* costs more than
  it adds. The hardening report's own note: "the next hardening pass CANNOT be additive at this cap."

- **D-S2 — Unintended runtime coupling to guarded-change.** Dragonfly inherits guarded-change's
  **reviewer charter, severity model, probabilistic (rate-based) rubric, and guarded-change-lite
  definition *by reference*.** The D-11 self-check named these as five cross-reference sites, but the
  actual by-reference **surface is broader** (round-1 review: e.g. `SKILL:107,117,118,144`;
  `METH:202,338,339,344,377-378,388,394,409,420` — inherit/reuse/using/pointer-back phrasings a
  literal five-site grep misses). The full removal surface is enumerated in `2-plan.md` §B / C9a; this
  spec does not rely on an exact site count. The D-11 self-check polices resolution ("every named
  guarded-change cross-reference resolves — severed = failure"). The hardening report called the
  coupling "deliberate and good, but unversioned." **The owner's ruling (2026-07-06) reframes it:** the
  *authoring* reuse of guarded-change's review machinery was intended; a *runtime rules-dependency*
  (dragonfly's behavior silently changing when guarded-change's doc text changes, with no
  dragonfly-side review) **was never the intention.** So this is not a design trade to weigh — it is
  **a bug getting fixed.**

## The goal

**Theme 1 — per-stage loading.** Reorganize dragonfly **by the loop's discrete stages** (0a, 0b, 1,
2, 3, 4, 5, 6, 7, 8, 9) so that, at any stage, only that stage's content need be in view. Mechanism:
**file-per-stage** (the design guarded-change's restructure proved out and shipped —
`Guarded_change/stages/`): the per-stage content splits into one file per stage
(`Dragonfly/stages/stage-*.md`), and `SKILL.md` becomes a thin **router** that at each stage directs
the agent to open *that stage's file*. Cross-cutting rules that govern more than one stage (the
representativeness gate, the triage, the charter, the gate-before-present rule, trust-before-gate
ordering, provenance, the severity model, the ledger append-only rule) are **repeated in full into
each stage they govern** (owner decision: no separate always-on "spine") — per-stage loading means
only one copy is ever in view, so the repetition costs no attention. The filesystem enforces the
isolation (the agent physically opens only the current stage's file) and makes it measurable.

**Theme 2 — untangle the coupling (the bug fix).** Give dragonfly its **own self-contained copies**
of the four pieces it currently borrows by reference — the **reviewer charter**, the **severity
model**, the **probabilistic/rate-based rubric**, and the **guarded-change-lite definition** — forked
from guarded-change's *finalized post-restructure* form (`Guarded_change/stages/charter.md`, and the
SEV1–4 table in `stages/stage-8.md` + `stage-4/7.md` routing for the severity model). Then **remove
the by-reference wording across the full surface** (enumerated in `2-plan.md` §B / C9a) **and retire
the D-11 cross-reference self-check** (nothing left to "resolve"), keeping only a light `forked from
guarded-change <rev>` provenance note. **The fork takes guarded-change's charter *unconditional core*
only — the conditional position/concurrency lenses are NOT current dragonfly behavior and are
excluded** (round-1 review; see constraints + `1.5-criteria.md` C9b). Themes 1 and 2 interact well: self-contained docs
would normally be *bigger* (worse for the attention budget), but per-stage loading means the
duplication is never all in view at once, so it costs nothing at runtime.

## The critical distinction (what Theme 2 removes vs. what it must preserve)

The untangle is **narrow and surgical**. Dragonfly and guarded-change are siblings that *compose*,
and two relationships between them are legitimate and MUST survive unchanged:

1. **The stage-8 workflow handoff** — dragonfly diagnoses, then hands the confirmed diagnosis to
   guarded-change to make the fix, and verifies the fix at stage 9. This is a workflow handoff, not
   a rules dependency. **KEEP.**
2. **The full-guarded-change triage invocation** — dragonfly's diagnostic-artifact triage routes an
   expensive/multi-file/state-mutating artifact into a *full guarded-change run* (it invokes the
   guarded-change skill as a tool, exactly as a user would; that run then keeps all of
   guarded-change's own stage duties, including its stage-3 coverage challenge). This is a
   tool-invocation, not a doc-text dependency. **KEEP** (including `METHODOLOGY.md:398-399`, which
   correctly says a full-GC triage run keeps guarded-change's duties — of course it does; it *is* a
   guarded-change run).

What Theme 2 removes is only the **rules-by-reference**: dragonfly's charter/severity/rubric/lite
*definitions* pointing at guarded-change's doc text instead of stating them in dragonfly's own files.
After the fix, `guarded-change-lite` (as dragonfly invokes it) uses **dragonfly's own** forked
charter; the direct stage-7 cold pass uses **dragonfly's own** charter. A naive "delete every
guarded-change mention" would break relationships (1) and (2) — the spec calls this out so the plan
and the reviewer guard against it.

## Scope and sequencing

- **THIS run — dragonfly, Themes 1 + 2** (per-stage restructure **and** the coupling untangle,
  together). They are entangled: the untangle *creates* dragonfly's own charter/severity/rubric/lite
  content, and the restructure *places* that content into the per-stage files — doing them in one run
  avoids restructuring by-reference stubs and then immediately rewriting them. Sequenced **after**
  guarded-change's restructure (done, live, `3d6889b`) precisely so dragonfly forks the **finalized**
  guarded-change charter/severity/rubric, and so the untangle reviews cleanly against a settled source.

- **Theme 3 (incidental-bug ledger) — PROPOSED SEPARATE follow-on run, not this one.** Theme 3 adds a
  *new behavior* (a running log where a hunt records incidental unrelated bugs it notices without
  acting on them, surfaced in the final report). This run's entire acceptance bar is
  **behavior-PRESERVING** (Themes 1+2 change organization and coupling, not what any hunt does).
  Folding an additive feature into a preservation run muddies both bars — the battery/oracle would
  have to distinguish "rule correctly preserved" from "rule correctly added." Recommendation: ship
  Theme 3 as its own small additive guarded-change run afterward (its bar is "the feature works,"
  not "nothing changed"). **← owner decision at the spec gate (fold in vs. defer).**

## Touched files (this run)

- `Dragonfly/SKILL.md` — reduced to a thin per-stage **router** + inputs + cold-start guard +
  stop-for-human summary + self-check (the D-11 cross-reference clause removed from the self-check).
- `Dragonfly/stages/stage-{0a,0b,1,2,3,4,5,6,7,8,9}.md` — **NEW**: one self-contained file per stage
  (procedure + every cross-cutting rule that governs it, in full).
- `Dragonfly/stages/charter.md` — **NEW**: dragonfly's own forked red-team charter (four lenses +
  evidence discipline + provenance + the diagnosis-specific aiming + the direct-pass coverage-challenge
  *exclusion*), shared by the cold-pass stages (1, 4, 7). Forked from `Guarded_change/stages/charter.md`,
  content-faithful, with dragonfly's aiming folded in.
- `Dragonfly/METHODOLOGY.md` — reduced to orientation/reference (why this exists, the loop diagram,
  the two layers, the config contract, what a run produces), mirroring guarded-change's slimmed
  METHODOLOGY. Kept so external references don't break.
- `Dragonfly/changes/per-stage-restructure-untangle-2026-07/*` — this run's artifacts.

The **exact final file set** is fixed in `2-plan.md` §A and frozen at gate 4. No change to
guarded-change's files, to either config, or to any `changes/` history in this run.

## Constraints

1. **Behavior-preserving above all.** These files are prompts — a *position-sensitive assembly*. The
   sibling methodology's core principle (*Information-preserving is not behavior-preserving*) warns
   that moving/adding/removing content in such an assembly can change behavior while every word
   survives. This restructure does exactly that kind of motion (relocating rules, repeating
   cross-cutting ones into each stage, forking the borrowed pieces into local copies), so
   behavior-preservation is the central risk. The acceptance bar (1.5) asserts it and verifies it by
   the tier chosen below.
2. **No rule lost, no rule mis-scoped.** Every atomic normative rule in the current files appears in
   the new structure, in every stage it governs. A rule silently narrowed (always-on → one-stage) or
   dropped is a behavior change.
3. **Forked pieces are content-faithful.** Dragonfly's own charter/severity/rubric/lite copies must
   be faithful to the guarded-change source they replace (same rules, same effect), so any hunt
   behaves identically whether a rule was reached by-reference (before) or from dragonfly's own copy
   (after). **The one intended behavior change:** dragonfly stops *tracking* guarded-change's future
   edits (the point of the untangle) — faithfulness is measured against **current** guarded-change
   (`Guarded_change` at this run's recorded base rev), not against a promise to stay in sync.
4. **The legitimate handoff/invocation relationships survive** (see "The critical distinction"):
   the stage-8 handoff to guarded-change and the full-GC triage invocation are unchanged.
5. **Line caps relaxed by design.** The current 670 combined is a symptom of the topic-organized
   shape at the additive cap; per-stage repetition of cross-cutting rules raises total line count on
   purpose. The new bar is *per-stage load*, not total. The plan (stage 2) states the new budget.
6. **Live == source after build.** The installed copy under `~/.claude/skills/dragonfly/` equals the
   repo source at the end (`diff -r` clean), per the standing self-check.
7. **SKILL ↔ METHODOLOGY ↔ stage-file consistency.** Any rule stated in more than one place still agrees.

## Verification depth — the open decision (owner, at the spec gate)

How behavior-preservation (C2) is proven. The guarded-change restructure ran **Tier 3 (a full 44-agent
A/B battery, ~2.1M tokens)** — and its **headline empirical result was that the battery could not
discriminate**: every deliberately-broken control (rule deleted from the doc) *still fired the rule*,
because a capable Opus arm applies each rule whether or not the text states it (even a Fable-5 grader
found no daylight). That non-discrimination is now a **twice-observed** result on these exact skills:
the flagship-probe found the same thing (capable arms don't fall for the non-representative-test trap
even with no dragonfly), and the gc battery confirmed it. The gc run closed via **named
risk-acceptance leaning on the C1 content-check**, not on the battery's (undemonstrated) detection power.

Given that direct evidence, the tiers and their honest cost/benefit:

- **Tier 3 — full A/B battery (~1.5–2M tokens).** Mirrors gc: situations × {OLD, NEW, BROKEN} ×
  blind graders. *Benefit:* execution evidence that NEW ≥ OLD (catches a gross regression — a whole
  stage's rules vanishing). *Cost:* ~2M tokens and the orchestration risk (the gc battery deadlocked
  for 67 min). *Known limit:* we have two prior results saying the controls will again be
  non-discriminating, so it will very likely re-land on the same "lean on C1" acceptance — paying ~2M
  tokens to re-learn a known lesson. The gross-regression it can catch, C1 catches more cheaply.
- **Tier 2 — content-primary + targeted behavioral spot-check (~200–400K tokens). ← recommended.**
  C1 (grep-derived rule oracle → every rule verbatim in its correct stage files) + a cold stage-6
  mechanical review + a **small** behavioral check: a handful of arms confirming the router resolves
  and that the 2–3 most position-sensitive rules (the representativeness gate; gate-before-present;
  the charter's cite-or-it-doesn't-count) still fire under NEW isolation. Leans on the lesson gc
  taught: for a capable subject the *content* check is the real assurance; a small behavioral check
  confirms the router + isolation work without the 44-agent theater.
- **Tier 1 — content-only (~50–100K tokens).** C1 + cold stage-6 review, no behavioral arms at all.
  *Cheapest;* relies entirely on the mechanical rule-inventory + cold read — zero execution evidence
  that an isolated stage file still fires its rules.

I recommend **Tier 2**: it spends where the evidence says spending buys something (content fidelity +
router/isolation working) and does not spend ~2M tokens re-confirming a non-discrimination result we
already have twice. The chosen tier sets C2's shape and is frozen at gate 4.

## Owner decisions (RESOLVED at the spec gate, 2026-07-06)

- **(A) Theme 3 scope → DEFER.** The incidental-bug ledger ships as its own small additive run
  afterward; THIS run stays purely behavior-preserving (Themes 1+2). No Theme-3 behavior is
  introduced here (C1 enforces "no new normative rule").
- **(B) Verification depth → TIER 2** (content-primary + targeted behavioral spot-check). C1 grep
  oracle is the primary preservation evidence; a small behavioral check confirms the router resolves
  and the 2–3 most position-sensitive rules still fire under NEW isolation. Chosen over Tier 3
  because the full battery's broken-rule controls are non-discriminating on these skills (observed
  twice: flagship-probe + gc battery), so ~2M tokens would re-land on the same C1-lean. C2 in
  `1.5-criteria.md` is fixed to the Tier-2 shape and frozen at gate 4.

(Themes 1+2 together, dragonfly, sequenced after guarded-change: already decided in memory —
`skills-structural-decisions-2026-07`. The file-per-stage mechanism + shared-charter pattern are
inherited from the proven guarded-change run.)
