# decisions.md — gate log (append-only)

## Stage 4 gate (plan red-team) — 2026-07-02
- **Worst severity: MINOR.** Cold reviewer (general-purpose, no shared context) consulted the
  dragonfly docs + the slip note. Factual lens clean (earned): confirmed the loop genuinely lacks
  the rule today (METHODOLOGY.md:46 lists covered artifacts, omits *hypothesis*; stage 3 gives
  status but no presentation constraint), and the slip evidence matches the note. Confirmed the
  rule WOULD have blocked FILEBLOAT (it was fully `ungated`) and integrates without contradicting
  open/confirmed/refuted.
- **Findings (all minor, fix-in-place):**
  - **L1** — at the `test-passed` tier, the stage-4 cold pass red-teams the *test artifact*
    (representativeness/confabulation), NOT the causal story; that is only challenged at stage 7.
    So "the hypothesis passed its cold red-team" over-promises for a `test-passed` "leading" claim.
    → Fold honest claim-tiers into Edit B: `test-passed` = rivals ruled out by a representative
    test (present as "leading candidate, causal chain not yet independently challenged"); "the root
    cause" requires `cold-red-teamed` (stage 7).
  - **L2** — Edits F/I say only "cold red-team" (reads as the stricter stage-7 sense), diverging
    from Edit B's tiering. → Name the tier in F/I (marker off `ungated`).
  - **M1** — trust-before-gate (Edit D/H) largely restates an existing stage-4 pre-run triage
    requirement; the genuine new content is the *recorded-in-decisions.md* auditability. → Reframe
    Edit D as making the existing precondition explicitly recorded, not implying the loop currently
    permits the slip.
  - **R1** — C5's violation scenario is near-verbatim the example written into Edit B → tests
    recall, not discrimination. → Make C5's violation a DIFFERENT fact pattern (passed repro but no
    causal red-team, presented as "the cause") so it tests the rule's discriminating force.
  - (nitpick) "most-likely cause" vs "most plausible so far" are near-synonyms; the real anchor is
    "conclusion to act on" — keep that substantive framing (already present). Logged.
- **Route:** MINOR → fix in place, proceed to BUILD (stage 5). All four folded into build wording.

## Stage 7 gate (code red-team) — 2026-07-02
- **Worst severity: MINOR.** Fresh cold reviewer verified all 9 edits (A–I) LANDED in the right
  sections; the three stage-4 fixes (L1 honest tiers, L2 tier-naming, M1 reframe) all confirmed
  present; C1–C4, C7 satisfiable with quoted text; C6 no contradiction (marker "distinct from"
  status; stage-7 bar deferred to). C7 re-confirmed live==source.
- **Findings:** (minor) SKILL edits G/I tied the phrase "leading *cause*" to the `test-passed`
  tier, whereas METHODOLOGY reserves all "cause" language for `cold-red-teamed` and grants
  `test-passed` only "leading *candidate*" → **fixed in place** (G/I reworded to "leading
  candidate" / "the cause" only at `cold-red-teamed`). (nitpick) "most-likely" absent from the
  label list → **added** to Edit A + B. (nitpick) stage-7 detail didn't reference the marker →
  **added** a back-reference ("passing it sets the marker to `cold-red-teamed` — precondition of
  'confirmed' and of presenting as the root cause"). All re-synced to source.
- **Route:** MINOR → fix in place, proceed to HARNESS (stage 8).

## Stage 8 harness + verdict — 2026-07-02
- Conformance-only (no baseline). Inspection criteria C1,C2,C3,C4,C7 PASS (stage-6 cites + diff).
- **C5 discrimination replay (execution):** cold judge given only the rule text + 3 neutral
  scenarios → **V=VIOLATES, A1=COMPLIES, A2=COMPLIES, all correct**, each citing the deciding
  clause. Rule discriminates exactly at the tier boundary; catches the root-cause-without-cold-pass
  violation and does not over-fire on ranked/leading-candidate discussion.
- Advisory C6 PASS (no contradiction after the tier fix).
- **Stage 8 gate: CLEAN → DONE.** Would have prevented the documented FILEBLOAT slip (it was
  `ungated`) and the secondary trust-before-gate slip. Both copies (live + source) identical.
  Change accepted.
