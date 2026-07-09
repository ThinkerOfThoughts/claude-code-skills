# decisions.md — gate log (append-only)

## Run-start path validation (CFG3) — 2026-07-09
All reviewer-context paths validated readable (see stage-3 record). No dead paths.
- Change artifacts: 1-spec.md, 1.5-criteria.md, 2-plan.md — OK
- Skill source (source-of-truth for claim-checking): stages/charter.md, SKILL.md, METHODOLOGY.md,
  stages/stage-3.md, stages/stage-6.md, stages/stage-1.5.md — OK

## Gate 4 (round 1) — 2026-07-09 — worst = BLOCKER → route back to criteria/plan
- **BLOCKER F1:** C5's grep oracle cannot detect a stale `charter.md:16` ("four **separate**
  lenses" — markdown emphasis defeats the length bound) NOR SKILL.md:66-67 ("four\nlenses" — line
  wrap defeats a line-based grep). Author-reproduced both. C5 is a broken oracle for 2 of its 7
  target locations. → redesign C5 to a positive per-location post-state assertion + a
  markdown/wrap-robust negative sweep; empirically self-test it against a deliberately-stale tree.
- MINOR L1 (C6 table-row parenthetical), M1 (extend spot-verify bullet to cover fidelity pins),
  G1 (broaden C4 to cover stage-3.md's `(lens 4)` tokens), G2 (closed by the C5 positive fix) —
  folded into the same revision pass.
- Route: revise 1.5-criteria.md + 2-plan.md, then re-run stage-3 (round 2) focused on the new
  oracle's robustness. First bounce at this gate (iteration cap: 1/2).
- Design decisions 1 (unconditional lens) & 2 (append at pos 5) survived the red-team CLEAN → frozen.

## Gate 4 (round 2) — 2026-07-09 — worst = MINOR → route to BUILD; criteria FROZEN
- Round-2 cold review confirmed the round-1 BLOCKER (C5 broken oracle) genuinely closed —
  reviewer built stale trees for both hard cases (charter:16 emphasis, SKILL wrap) and both C5
  halves caught each. 3 MINORs (E2b wrap-quote, self-test not operationalized, grep -Pzo
  portability) fixed in-place, no bounce.
- Path re-validation: all reviewer-context paths still readable (round-2 reviewer confirmed).
- Criteria C1–C9 FROZEN at route-to-build. Iteration cap: gate 4 saw 1 blocker-bounce (1/2), now clean-enough.

## Gate 7 (stage-6 code review) — 2026-07-09 — worst = CLEAN → proceed to stage 8
- Stage-6 cold review (agent a9e2987c) verdict CLEAN: diff = plan exactly (E1/E2/E2b + 7 count
  edits, nothing stray/missing), C4 position-preservation earned CLEAN (lenses 1–4 byte-unchanged,
  all (lens 4) tokens still resolve to lens 4), lens content complete, cross-doc consistent, C7 in
  sync. One MINOR/advisory: plan prose undercounted "six" vs true seven count sites → FIXED in
  2-plan.md (build was already correct). No bounce.
- Build slip caught + fixed pre-gate: METHODOLOGY.md "four→five" silently did not land on first
  attempt; the mechanical diff + C5 positive-per-location assertion caught it, re-applied + re-synced.

## Gate 8 (harness) — 2026-07-09 — CONFORMANCE-ONLY (no baseline) — verdict PASS
- All 9 gating criteria (C1–C9) empirically verified on the built tree (see 8-harness.md).
- C5 self-test: negative sweep FIRES 5/5 on pre-change baseline, 0 STALE on built tree → oracle proven.
- No advisory criteria; no regression arm. Fidelity lens LIVE in source + installed. Loop complete.
