# 1 — Spec: dragonfly Run 2 — representativeness-enforcement gaps

## Source
Memory `dragonfly-next-iter-representativeness-enforcement.md`, section "Representativeness-
enforcement gaps (2026-07-07)" + its 2026-07-08 refinement of gap #3. Second of the two themed
dragonfly runs (Run 1 = R-A/R-B/R-C, committed `c8db6fa`). The skill HAS the design-time
representativeness gate (B-REP-1) but it did not fire when the S1 hunt ran T-series arms at 7–13
turns and recorded "NO_BLEED" against a 100-turn design. Three gaps to close.

## The three gaps and the fix each gets

### G1 — the gate is design-time, not result-time → `B-REP-4` (stage-5)
B-REP-1 makes an artifact untrusted until a control exhibits the symptom, but **nothing binds that
check to the moment a NEGATIVE/"clean" result is RECORDED.** An arm produced "no symptom" and was
logged as eliminating a hypothesis without ever having shown it CAN exhibit the symptom at the run
parameters used. **Fix:** a negative result is **auto-untrusted** (cannot eliminate a hypothesis)
unless that arm was shown to exhibit the symptom under the **same-or-weaker parameters**
(length/scale/load/conditions). "Clean at 7 turns" must cite an exhibited instance at ≤7 turns, or
be marked **untrusted-negative**. This puts the representativeness gate at **stage-5 result-
recording**, not only stage-1/4 design.

### G2 — test-as-run vs test-as-designed drift is undefended → `B-REG-1` (stage-5)
The pre-registered design (stage-4) had a stop rule (100 turns / +20-on-trigger); the executed run
used 7–13 and nothing flagged the mismatch. **Fix:** a stage-5 checkpoint that a test's **executed**
parameters (sample size / stop rule / conditions) match its **pre-registered design** (stage-4),
else the deviation is recorded and the result **re-scoped** before it is trusted.

### G3 — operator-drift is undefended → `B-TARGET-1` (stage-2, + SKILL pointer)
The skill assumes it is run stage-by-stage; it has no cheap tripwire for coasting on the artifacts
(the [[work-within-skill-framework]] failure). **Per the 2026-07-08 refinement:** the drift is NOT
mainly "skipping the gate" — it is **latching onto a plausible, real, ADJACENT thread that feels
like progress but is a property of a *symptom* or a *mitigation*, not the root** (seductive
*because* real and nearby). **Fix (the guardrail that helps):** before ANY investigative step, check
it against the **frozen root-cause TARGET** — "does this step **attribute a share** of the disease
(per the named hypothesis/layers/bugs), or is it a property of a symptom / mitigation?" If the
latter → **incidental-ledger** item, do not pull it. Two supports: (a) keep the frozen target
**literally in front** — re-read the frozen symptom + hypothesis ledgers each step, do NOT
reconstruct from memory (reconstruction is where it gets distorted; cf `B-VER-1`); (b) a **per-step
target-check marker** on the observation-ledger row naming which frozen-target node the step
attributes to — a row that names none is drift.

## Design decisions (for the plan to justify, the red-team to challenge)

- **D1 — B-REP-4 & B-REG-1 both home at stage-5** (run & record), the moment a result is recorded
  and about to be consumed; both flow to stage-6 (an untrusted/off-design result may NOT count as a
  hypothesis elimination for the convergence cap — a one-line pointer added at stage-6).
- **D2 — B-REP-4 extends "the representativeness gate" to also bind at stage-5.** So the two
  "governs stages 1 and 4" statements (SKILL L53, METHODOLOGY L64) become "governs stages 1, 4,
  and 5". (2-site consistency surface — handled robustly.)
- **D3 — B-TARGET-1 homes at stage-2** (with the incidental-findings discipline), the ledger-write
  point where the per-step marker naturally attaches; a concise pointer is added to SKILL's
  "Incidental findings" paragraph. It **composes with, does not contradict,** the existing
  incidental rule: that rule asks "is a newly-noticed *finding* related to the `S#` set?" (in doubt →
  in-scope); B-TARGET-1 asks "does the *step I'm about to take* advance the frozen root-cause
  target?" — a step can be on-topic yet still be drift onto a symptom/mitigation property. The spec
  makes the composition explicit in the rule text so the two do not appear to conflict.
- **D4 — new rule IDs** (collision-checked absent): `B-REP-4`, `B-REG-1`, `B-TARGET-1`.

## Expected touched files (source + installed mirror)
0. `stages/stage-4.md` — **(added after round-1 red-team)** add `A-4-2`: register the design's
   parameters/stop-rule/conditions as the **pre-registered design** (the referent `B-REG-1` checks)
   + a one-line pointer that the rep gate binds again at result-time (`B-REP-4`).
1. `stages/stage-5.md` — add `B-REP-4` (result-time rep gate) + `B-REG-1` (as-run vs as-designed).
2. `stages/stage-2.md` — add `B-TARGET-1` (frozen-target attribution + per-step marker, with the
   composition note vs incidental-findings).
3. `stages/stage-6.md` — one-line pointer: untrusted-negative (B-REP-4) / unresolved-deviation
   (B-REG-1) does NOT count as a hypothesis elimination for the convergence cap.
4. `SKILL.md` — "governs stages 1 and 4" → "1, 4, and 5" (L53); concise B-TARGET-1 pointer in the
   "Incidental findings" paragraph.
5. `METHODOLOGY.md` — "governs stages 1 and 4" → "1, 4, and 5" (L64).

**Not touched:** the charter (no lens change this run — the fidelity lens already shipped in Run 1);
`dragonfly.companion.md`; guarded-change. No "four/five lens" count change this run.
