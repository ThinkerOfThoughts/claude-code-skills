# 1 — Spec: per-stage restructure of the guarded-change skill (Theme 1)

## The problem

The guarded-change skill's two files grow with every hardening pass — now
`METHODOLOGY.md` 534 + `SKILL.md` 124 = 658 lines. They are organized **by topic**
(core principles, the charter, the severity model, stage-8 detail, the config contract),
so an agent running any single stage must hold the whole document in view and locate the
rules that apply to where it actually is. On Opus this is the attention-budget ceiling
flagged as **S1** in `changes/audit-hardening-2026-07/9-report.md`: past some size each
added rule dilutes the others, and a rule that gets *missed* costs more than it adds. The
hardening run saw this concretely — some review misses were attention-shaped (the reviewer
engaged with the doc but misread a rule under load).

## The goal

Reorganize the skill **by the loop's discrete stages** so that, at any stage, only that
stage's content need be in view. The loop already runs as a sequence of numbered stages
(0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8); the documents should be shaped the same way.

**Owner decision (2026-07-06):** cross-cutting rules that apply at more than one stage are
**repeated into each stage's instructions**, not factored into a separate always-on
"spine." Each stage section stands alone — its own rules plus every overarching rule that
governs it. Per-stage loading means only one copy is ever in view, so the repetition costs
no attention.

**Mechanism — file-per-stage (revised after stage-3 round 1, which found the softer design
would not work).** The per-stage content is split into **one file per stage**
(`stages/stage-0.md` … `stages/stage-8.md`), and `SKILL.md` becomes a thin **router** that,
at each stage, directs the agent to open *that stage's file*. The split matters: a single
reorganized `METHODOLOGY.md` plus a "read section N" instruction is honor-system — a
diligent agent reads the whole (now longer, because of the repeated rules) file anyway, so
the attention-budget win would not actually land, and could invert (round-1 blockers L3/A1/
C-2). Splitting into files makes per-stage loading **enforced by the filesystem** (the agent
physically opens only the current stage's file) and **measurable** (which file it opened =
what got loaded). Stage-active rules currently living in "reference" sections (path
validation, which blocks gate 4; the `decisions.md` gate-log duties the iteration cap
depends on) move **into the stage files that enforce them**, not into an always-on bucket
(round-1 F4). Purely-reference material (the config-contract yaml shape, the two-layers
framing) stays as a small reference file the relevant stage points at.

This is a **reorganization, not a rewrite**: no rule's wording, meaning, or triggering
condition changes. The same rules, producing the same behavior, relocated into per-stage
files and (for cross-cutting rules) duplicated across the stages they govern.

## Scope and sequencing

This initiative covers both skills and two themes. This run is deliberately **only the
first slice**, because each slice is already a large position-sensitive change and
combining them multiplies the blast radius and the verification burden:

- **THIS run — guarded-change, Theme 1 only.** Restructure `Guarded_change/SKILL.md` +
  `Guarded_change/METHODOLOGY.md` into per-stage form.
- **Follow-on run (separate guarded-change invocation) — dragonfly, Themes 1 + 2.**
  Restructure dragonfly the same way **and** untangle its unintended runtime dependency on
  guarded-change (dragonfly currently inherits guarded-change's charter / severity model /
  probabilistic rubric / lite-pass definition / provenance rule *by reference* — see the
  greps in this run's `decisions.md`; owner's original intent was an *authoring* reference,
  not a live dependency). Sequenced **after** this run so dragonfly copies guarded-change's
  charter/rubric from their finalized per-stage form, and so the untangling reviews cleanly
  against a settled source.

*Proposed for owner confirmation at the spec gate.* If you'd rather do dragonfly first, or
both in one run, say so.

## Touched files (this run)

- `Guarded_change/SKILL.md` — reduced to a thin per-stage **router** + inputs +
  stop-for-human summary + self-check.
- `Guarded_change/stages/stage-{0,1,1.5,2,3,4,5,6,7,8}.md` — **NEW**: one self-contained
  file per stage (procedure + every cross-cutting rule that governs it, in full).
- `Guarded_change/METHODOLOGY.md` — reduced to orientation (why this exists + the loop
  diagram) + pointers to the stage files and the config-contract reference; OR retired in
  favor of `SKILL.md` carrying orientation (decided at build time, recorded).
- `Guarded_change/config-contract.md` (or a kept METHODOLOGY reference section) — the
  Layer-2 config yaml shape + two-layers framing, as reference.
- `Guarded_change/changes/per-stage-restructure-2026-07/*` — this run's artifacts.

The **exact final file set** is fixed in `2-plan.md` §A and frozen at gate 4. No change to
dragonfly's files, to either config, or to any `changes/` history in this run.

## Constraints

1. **Behavior-preserving above all.** These files are prompts — a *position-sensitive
   assembly*. The methodology's own core principle (*Information-preserving is not
   behavior-preserving*) warns that moving, adding, or removing content in such an assembly
   can change behavior while every word survives. This restructure does exactly that kind
   of motion (relocating rules, repeating cross-cutting ones into each stage), so
   behavior-preservation is the central risk, and the acceptance bar (1.5) must assert it
   and verify it **by execution**, not by confirming the text still appears somewhere.
2. **No rule lost, no rule mis-scoped.** Every atomic rule in the current files must appear
   in the new structure, in every stage it governs (cross-cutting rules in *all* their
   stages; stage-specific rules in the right stage). A rule silently narrowed from
   always-on to one-stage, or dropped, is a behavior change.
3. **Line caps relaxed by design.** The current combined cap (658) is a symptom of the
   topic-organized shape; per-stage repetition of cross-cutting rules will raise total line
   count on purpose. The new bar is *per-stage-section* legibility, not total lines. The
   plan (stage 2) states the new budget.
4. **Live == source after build.** The installed copy under `~/.claude/skills/guarded-change/`
   must equal the repo source at the end (`diff` clean), per the standing self-check.
5. **SKILL ↔ METHODOLOGY consistency.** Any rule both files state must still agree.

## Owner decisions (resolved 2026-07-06)

- **(A) Scope/sequencing → GUARDED-CHANGE FIRST.** This run = guarded-change only; dragonfly
  (Themes 1+2) is a separate sequenced run after.
- **(B) Verification depth → TIER 3 (full A/B battery).** Behavior-preservation is proven by
  running situations through the old vs new structure and comparing whether each rule still
  fires (design in `2-plan.md` §B).
- **(C) Structure mechanism → FILE-PER-STAGE split** (after stage-3 round 1's blocker):
  per-stage files enforced by the filesystem, not a single reorganized file + honor-system
  router. See "The goal" above.
