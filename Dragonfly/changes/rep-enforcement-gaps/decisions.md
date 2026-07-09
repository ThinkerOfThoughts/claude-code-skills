# decisions.md — gate log (append-only)

## Run-start path validation (2026-07-09)
All reviewer-context paths validated readable (change artifacts + stage-2/4/5/6 + SKILL +
METHODOLOGY). No dead paths. Pre-checks: new IDs B-REP-4/B-REG-1/B-TARGET-1 absent pre-change ✅ (C7);
rep-gate scope surface = exactly 2 sites (SKILL L53, METHODOLOGY L64) ✅.

## Gate 4 (round 1) — 2026-07-09 — worst = MAJOR → revise → stage-3 round 2
- Stage-3 cold review (agent a86083c3): Factual (scope surface=2, IDs collision-free) & stage-6
  tie-in CLEAN. MAJOR: B-REG-1 checks a "pre-registered design from stage 4" that stage-4 never
  produces (vacuously satisfiable) — change touched everything but stage-4. MINORs: B-TARGET-1
  tie-break excludes while sibling includes; B-REP-4 fallback re-admits assertion-trust; layer/bug
  vocab absent; same-or-weaker not a total order.
- Resolutions: E0 adds stage-4 A-4-2 (register the design) + result-time pointer; C2b added; B-REG-1
  reworded (referent + no-registration-is-a-defect); B-TARGET-1 node-vocab fixed + inclusion
  tie-break; B-REP-4 fallback bound to ledger evidence + multi-axis clause; C1/C4 extended.
- Route: revisions include NEW design (stage-4 A-4-2) → focused stage-3 round-2 cold review before
  build. Iteration cap: 1 bounce at gate 4 (1/2).

## Gate 4 (round 2) — 2026-07-09 — worst = MINOR → route to BUILD; criteria FROZEN
- Round-2 cold review (agent a001519c) confirmed round-1 MAJOR fully closed + all 4 MINORs held.
  2 new MINORs (E3 budget-vocab; A-4-2 ledger home) fixed in-place: E3 reworded to A-6-4/A-6-1
  vocab; A-4-2 registration moved to decisions.md (deviation stays in observation ledger). No bounce.
- Criteria C1–C10 + C2b FROZEN. Iteration cap: 1 blocker/major-class bounce at gate 4 (1/2).
- Route to build; stage-6 cold-reviews the built bytes as the independent check.

## Gate 7 (stage-6 code review) — 2026-07-09 — worst = MINOR (stale criteria line) → fixed → stage 8
- Stage-6 cold review (agent ab3f20181): build CLEAN — diff=plan exactly, round-1 MAJOR closed
  non-vacuously (A-4-2 referent), both round-2 fixes landed, position/behavior preserved, live==source.
  Sole finding: C2b criteria line said "observation ledger" vs as-built "decisions.md" → criteria
  corrected (doc staleness, not a build defect). No bounce.

## Gate 8 (harness) — 2026-07-09 — CONFORMANCE-ONLY — verdict PASS
- All 12 gating criteria (C1–C10 + C2b) verified on built tree (see 8-harness.md). Rep-enforcement
  gaps live in source + installed. Loop complete.
