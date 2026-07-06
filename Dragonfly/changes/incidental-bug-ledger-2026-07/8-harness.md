# 8-harness.md — the incidental-bug ledger (Theme 3): stage-8 conformance

Conformance of the built additive feature vs the frozen `1.5-criteria.md` (T1–T8). Additive-feature
change → **conformance ("the feature works") + light regression ("nothing existing broke")**. Verified
by 5 cold arms (model `claude-opus-4-8[1m]`) + mechanical checks.

## Per-criterion verification table

| Criterion | Gating | Path exercised | Verified by execution? | Evidence | Result |
|---|---|---|---|---|---|
| **T1** feature fires, BOTH directions | gating | cold arm at stage 2, two findings | yes | arm **FIRED**: parked the unrelated admin-auth bug to `incidental-ledger.md` (not chased); routed the in-scope no-TTL observation to `observation-ledger.md` (not the parking lot) — "severity ≠ relevance" | **PASS** |
| **T2** stage-8 surfacing on ANY exit | gating | 2 cold arms: found + characterized | yes | both **FIRED**: found-arm surfaced the parking lot distinct from the S#-related residual (residual stays in diagnosis.md; I1/I2 not routed to guarded-change); **characterized-arm surfaced it on the no-diagnosis.md exit** (the round-1 gap, closed) | **PASS** |
| **T3** additive-only, no existing rule changed | gating | stage-6 mechanical diff review | yes (stage-6) | `6-redteam-code.md`: 4 diff "deletions" all confirmed re-wraps; flagship gate paragraph intact + adjacent to loop table; stage-2 A-2-1/A-2-2 + stage-8 A-8-2/A-8-3 byte-unchanged | **PASS** |
| **T4** no regression (existing rules still fire) | gating | re-run SC-1 (rep gate) + SC-2 (gate-before-present) vs amended files | yes | both **FIRED**: SC-1 rejected the non-representative repro (B-REP-3); SC-2 presented the ungated hypothesis as "candidate, ungated" | **PASS** |
| **T5** per-stage load budget preserved | gating | `wc -l` per stage load | yes | SKILL 91 / stage-2 31 / stage-8 28; worst-case load (SKILL+stage-7+charter) = **237 ≤ ~270** | **PASS** |
| **T6** live == source | gating | `diff -r ~/.claude/skills/dragonfly/` | yes | SKILL / METHODOLOGY / all stages diff-clean (install log) | **PASS** |
| **T7** cross-file consistency | gating | consistency sweep (stage-6) | yes (stage-6) | name + semantics (log-and-move-on / don't chase / parking lot / out-of-scope of S# / when-in-doubt-in-scope) agree across SKILL / stage-2 / stage-8 / METHODOLOGY | **PASS** |
| **T8** parking lot never blocks the hunt | gating | inspection + T1 arm | yes | rule wording ("never blocks a gate, never part of convergence-cap accounting"); T1 arm did not chase the parked finding; T2 arms confirmed it had "zero bearing on whether the hunt reached found" | **PASS** |

## C2 — the 5-arm conformance detail

| Arm | Rule | Stage | Loaded | Verdict |
|---|---|---|---|---|
| T1 | incidental-findings, both directions | 2 | SKILL+stage-2 | **FIRED** — unrelated → parking lot (not chased); in-scope → observation ledger |
| T2-found | surfacing on "found" | 8 | SKILL+stage-8+ledger | **FIRED** — parking lot distinct from the S#-related residual; not routed to guarded-change |
| T2-characterized | surfacing on "characterized, not found" | 8 | SKILL+stage-8+ledger | **FIRED** — parking lot surfaced on the no-diagnosis.md exit |
| SC-1 | representativeness gate (regression) | 1 | SKILL+stage-1+charter | **FIRED** — rejected the non-representative repro |
| SC-2 | gate-before-present (regression) | 3 | SKILL+stage-3 | **FIRED** — "candidate, ungated," not the cause |

**5/5 FIRED**, each opening only its routed file(s) (C3b-style isolation holds). The feature fires in
both routing directions and on both terminal verdicts; the two pre-existing rules most adjacent to the
change still fire → no regression.

## Verdict

**All gating criteria (T1–T8) PASS.** The incidental-bug ledger conforms: the feature fires (park
unrelated / keep in-scope / surface on any exit), it is additive-only (no existing rule changed, stage-6
verified), it doesn't regress the neighbouring rules, it stays within the per-stage load budget, and
live == source. **Gate 8: clean → done.**
