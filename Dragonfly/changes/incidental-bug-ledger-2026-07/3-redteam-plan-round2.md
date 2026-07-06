# 3 — Red-team the plan (ROUND 2) — verbatim record

Cold re-review of the round-1-revised {spec, criteria, plan}, carrying round-1 forward. Reviewer:
**general-purpose**, model **claude-opus-4-8[1m]**, read-only. Hashes: spec `a96b933a…`, criteria
`133f9854…`, plan `3544e86e…`, round-1 record `a7f23f90…`, + the 4 touched files + stage-6/stage-7
(context). **Verdict: NOT clean — ONE MINOR** (all five round-1 findings genuinely addressed).

## Part A — round-1 fixes confirmed (all ADDRESSED)
1. **MAJOR anchor** → ADDRESSED. Verified SKILL:52-57 IS the flagship "most important gate" paragraph
   ending "…escalate to a human." at 57; anchoring the block after 57 (before `## Stop-for-human`:59)
   leaves 52-57 intact + still directly below the loop table. Fix does what it claims.
2. **T4 reverse boundary** → ADDRESSED. T1 clause (d) + the two-finding arm (unrelated admin endpoint →
   parking lot; in-scope no-TTL-check → observation ledger) execute both directions.
3. **Characterized-exit** → ADDRESSED. Stage-8 fires on any exit; T2 = found + characterized arms.
4. **Tie-breaker** → ADDRESSED + coherent in SKILL + stage-2 + spec (same wording/routing).
5. **Nitpicks** → ADDRESSED (carry-over brief lists the ledger; arm model recorded).

## Part B — the one new defect (fixed in place at gate 4)
**[MINOR] spec:32-35 & plan:42 — the "any exit" rewording invented a THIRD terminal exit.** Both
enumerated "found / characterized / **convergence-cap escalation carry-over**", but the skill defines
exactly **two** legal terminal verdicts (A-8-3, stage-8:14 + stage-7:41); a convergence-cap hit is a
*stop-for-human* mid-loop (stage-6:26-27), not a stage-8 handoff verdict. Behavior unaffected (the
surfacing rule fires on any non-empty ledger regardless of label; criteria T2 already used the correct
two-verdict model) → **MINOR, not major**. **→ Fixed in place:** spec + plan reworded to "either
terminal verdict (found / characterized)"; the mid-loop-halt case noted as covered by the cold-start
carry-over brief (findings on disk, not lost).

## Reviewer's clears (verbatim highlights)
- **Tie-breaker is well-bounded** — not vacuous (the "clearly-unrelated" bar keeps the parking path
  live; T1's admin-endpoint example parks correctly) and does not collide with the existing "in doubt →
  full" *triage* rules (different object: scope-classification vs. artifact-triage; same conservative
  spirit).
- **Additive-only re-confirmed** at every anchor (flagship 52-57 untouched; new bullets appended; list
  items appended; no existing rule reworded/reordered/diluted).
- **Load budget holds** — with additions, worst stage load ~237 ≤ 270.
- **Label audit: no mislabel.** Coverage: no uncovered alterable behavior beyond the finding-1 text slip.

→ Gate 4 round 2: MINOR → fixed in place → **clean → freeze + build.**
