# decisions.md — gate log (append-only)

## Run-start path validation (2026-07-09)
All reviewer-context paths validated readable (change artifacts + charter/stage-1/2/3/5/7 + SKILL +
METHODOLOGY). No dead paths. Pre-checks: 4 new rule IDs (B-VER-1/B-TIME-1/B-FID-1/B-COST-1) absent
pre-change ✅ (C6); no numbered "(lens N)" cross-reference exists that appending lens 5 could break ✅.

## Gate 4 — 2026-07-09 — worst = MAJOR → revise → BUILD (stage-6 is the independent re-check)
- Stage-3 cold review (agent a1a478287): Factual & Logical CLEAN (count surface exactly 6, IDs
  collision-free, anchors real, twin claim true, homes cohere). MAJOR: E1b earned-clean fidelity
  guard observed by no criterion → could ship broken green. MINOR M1: dragonfly fidelity lens omits
  the GC twin's spot-check-pins clause. MINOR M2: E6 anchor splits triage flow.
- Resolutions: C3b added (gates E1b + E1c aim + E1e pins); E1e added (twin-parity spot-check-pins
  clause, near-verbatim from the already-reviewed+shipped GC charter); E6 anchor moved after C-LITE.
- Routing: revisions are additive/mechanical + the novel E1e text is near-verbatim from a
  cold-reviewed shipped source → proceed to build; stage-6 cold-reviews the BUILT bytes incl.
  E1b/E1c/E1e presence+correctness as the independent check. Iteration cap: 1 bounce at gate 4 (1/2).
- Criteria C1–C10 + C3b FROZEN at route-to-build.

## Gate 7 (stage-6 code review) — 2026-07-09 — worst = CLEAN → stage 8
- Stage-6 cold review (agent a7553c689) verdict CLEAN, no findings. MAJOR from gate 4 genuinely
  closed: E1b earned-clean guard + E1c aim + E1e spot-check-pins all present + non-vacuous. Diff =
  plan exactly; all 6 count swaps landed; lenses 1–4 + existing rules byte-unchanged; live==source.

## Gate 8 (harness) — 2026-07-09 — CONFORMANCE-ONLY — verdict PASS
- All 12 gating criteria (C1–C10 + C3b) verified on built tree (see 8-harness.md). C5 self-test
  fires 4/4 on baseline pre-images. R-A/R-B/R-C live in source + installed. Loop complete.
