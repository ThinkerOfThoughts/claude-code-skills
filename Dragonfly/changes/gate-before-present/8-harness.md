# 8 — Harness (conformance-only; no stage-0 baseline)

Prose-methodology change → no measurable prior metric → conformance-only. Inspection criteria
verified by locating the text (stage 6, cited); C5 verified by the discrimination replay.

## Per-criterion verification table

| # | Criterion | Gating? | Path exercised | Verified by execution? | Result |
|---|---|---|---|---|---|
| **C1** | Rule in all load-bearing locations | gating | Located: METHODOLOGY core-principle L49, "## The gate-before-present rule" section L235, stage-3 marker L150, Human-in-the-loop L435; SKILL stage-3 L51, stage-5 L59, stop-for-human L117 | yes — text located | **PASS** |
| **C2** | Forbids leading/likely/probable/most-likely-cause label until cold pass; names "candidate, ungated"; permits ranked list | gating | METHODOLOGY L244 (label list incl. "most-likely," added at stage 7), L242 "candidate, ungated," L252 "Rank is not endorsement … allowed and expected" | yes | **PASS** |
| **C3** | Per-hypothesis gate marker (`ungated/test-passed/cold-red-teamed`) distinct from status; stage-7 "confirmed" tied to `cold-red-teamed` | gating | METHODOLOGY L150-156 (marker, "distinct from that status"); stage-7 L185-186 back-reference; Edit E run-artifact line | yes | **PASS** |
| **C4** | Trust-before-gate ordering — output not consumed until triage recorded passed; precondition, not audit | gating | METHODOLOGY L164-170 (stage 5, reframed) + L258-264 (rule section, "a precondition of trust, not a later audit"); SKILL L59-61 | yes | **PASS** |
| **C5** | REPLAY (discrimination): cold judge classifies V=violation, A1=compliant, A2=compliant from rule text alone | gating | Cold judge given only the rule text + 3 neutral scenarios (root-cause claim at `test-passed`; honest "leading candidate" at `test-passed`; ranked list) | yes — judge run | **PASS** — V=VIOLATES, A1=COMPLIES, A2=COMPLIES, all three correct, each citing the deciding clause. Rule discriminates exactly at the tier boundary; catches the violation, doesn't over-fire. |
| **C6** | No contradiction with open/confirmed/refuted, the stage-7 three-part bar, the representativeness gate, or "form/rank freely" latitude | advisory | Stage-6 cold review: marker "distinct from that status"; stage-7 bar deferred to; no drift after the tier fix | (advisory) | PASS |
| **C7** | Live == source both files | gating | `diff` METHODOLOGY.md + SKILL.md | yes — both empty | **PASS** |

## Verdict

All **gating** criteria (C1–C5, C7) **PASS**; advisory C6 PASS. No stage-0 baseline → no
regression check. C5 is a clean, unambiguous discrimination pass (unlike a stochastic
majority-vote — the rule is a crisp decision procedure, and a single cold judge classified all
three scenarios correctly with cited clauses). **Stage-8 result: CLEAN → done.** Both copies carry
the rule identically.

## Would it have prevented the documented slip?

Yes. H-S1-FILEBLOAT was presented as the "leading" cause with **no** test, repro, or toggle — i.e.
`ungated`. Every location of the rule forbids presenting an `ungated` hypothesis as the leading
cause; the stage-3 reviewer confirmed this and the C5 judge confirmed the tier logic. The secondary
trust-before-gate slip (`replay_search.py` output consumed before its cold review was recorded) is
now forbidden by the stage-5 + rule-section ordering clause (consume only after the triage is
recorded passed in `decisions.md`).
