# 3 — Red-team the plan (ROUND 3, FINAL freeze gate) — verbatim record

Cold stage-3 review (round 3) of the round-3-revised artifacts, carrying rounds 1+2 + the completeness
pass forward. Fresh cold agent, no shared context. Owner-authorized final lap (post-cap tie-break).

## Context + provenance
Reviewer: **general-purpose**, model **claude-opus-4-8[1m]**, read-only + mechanical grep/wc.
Reviewer-reported context hashes matched the author-recorded round-3 set (1-spec `8f163fc8…`,
1.5-criteria `1f3c7684…`, 2-plan `8361454c…`, 2-rule-oracle `cc4d988f…`, 3-redteam-plan `9d373742…`,
round2 `e2cb63b9…`, completeness `c5edc4c5…`, Dragonfly/SKILL `b5e122ef…`, METHODOLOGY `04d1044c…`,
gc charter `6b98164d…`, gc stage-8 `d737f1bc…`, stage-4 `4ea889d5…`, stage-7 `070a966a…`).
**Verdict: MAJOR — do not freeze yet (3 mechanical plan-drift majors; oracle certified sound).**

## Reviewer's verbatim output (key sections)

> ## PART A — confirmation of prior-round resolution
> | # | Finding | Verdict |
> |---|---|---|
> | Round-2 B-1 count escaped into plan | **ADDRESSED** — grep count = 86, "86" identical in criteria/plan, no stray 78/80/81/83 in a live C1 instruction |
> | Round-2 B-2 C9a adjacency grep | **ADDRESSED** — now read-confirm + whole-file read-and-classify; would catch SKILL:107 + METH:394 |
> | Round-2 B-3 closed-set over-fork | **ADDRESSED (source) / see B-2 (plan)** — excluded + recorded; source grep empty; **caveat plan:17 still lists closed-set as included** |
> | Round-2 B-4/B-5 missing stage-9 rows | **ADDRESSED (oracle)** — A-9-6/A-9-7 verbatim-verified, scope 9; **but absent from plan stage-9 mapping row → B-1** |
> | Round-2 METH:420 | **ADDRESSED** — C-REF-1 flags the rewrite |
> | Round-3 additions (B-EVID-1, B-CAUS-1, B-CH-inherit, B-TBG-1 widen) | **ADDRESSED — all real, correctly scoped, not spurious**; B-CH-inherit "dissolves post-fork" note sound; **but B-EVID-1/B-CAUS-1 absent from plan stage rows → B-1** |
> | C1 source-anchoring (ii) | **ADDRESSED — well-specified, removes the failure mode** |
>
> ## PART B
> **[MAJOR] 2-plan.md:56 — false completeness claim; §A mapping table omits A-9-6, A-9-7, B-EVID-1, B-CAUS-1 from their governing-stage rows.** plan:56 asserts every row appears; `grep 'A-9-6\|A-9-7' 2-plan.md`=empty, stage-9 row lists only A-9-1..5; B-EVID-1/B-CAUS-1 only in the addendum note, not the stage rows. The §A table is the builder's construction guide. **Mitigant (why not blocker):** C1's ground truth is the frozen oracle (complete) + C1(ii) source-walk, so a dropped rule is caught at stage 8, not lost at acceptance. **Fix:** integrate the 4 IDs into their §A rows + a freeze item; correct plan:56.
> **[MAJOR] 2-plan.md:17 — §A charter file-table lists "provenance/closed-set" as INCLUDED, contradicting the round-2 B-3 exclusion.** Same-doc contradiction (operative §A.2/mapping/C9b/freeze-item-3 all correct). Documentation defect. **Fix:** delete "/closed-set" at plan:17.
> **[MAJOR] plan:148-154 / criteria:137 — the C9a KEEP allow-list (a)-(e) is not exhaustive.** Full source inventory (45 `guarded-change` hits) surfaces legitimate composition mentions matching none of (a)-(e): METH:73-74 "diagnostic artifacts get guarded-change"; METH:140/166 + SKILL:116 "the triage's guarded-change/lite pass IS the cold review"; METH:343 "invoke the guarded-change skill directly"; METH:246 "guarded-change's domain"; **triage rule 3 → lite** (KEEP (c) named only rules 1&2). An under-inclusive allow-list forces a strict reviewer to bucket ~6 legitimate hits as defects → false C9a failure. **Mitigant:** "reviewer classifies" backstop. **Fix:** add category (f) triage/lite-routing composition, or make the pass rule composition-vs-dependency.
> **[MINOR] freeze checklist has no §A-table-vs-oracle coverage check** → add one. **[MINOR] plan:160 "3 arms" contradicts the 4-arm (SC-1..4) table** → "4 arms". **[NITPICK] transitivity assumption rests on gc's own restructure (named-not-re-verified by design; unverifiable-by-me).**
>
> ## Coverage / label / position
> - Oracle certified: "the frozen oracle is complete, correct, and correctly scoped (86 rows, independently reconciled across sections the prior rounds under-examined; all round-2/round-3 additions verbatim-verified with correct scope, none spurious)."
> - Independent spot-checks of cold-start guard, config contract, trigger, stage-2 ledger, shared-assumption, detector duties, confirmed-verdict — **all reconciled cleanly to oracle rows with correct scope.**
> - Differential B-AIM per-stage scoping (1/4 vs 7) in a co-located charter — **handled correctly** (a real position-sensitivity, handled well). B-PROV-2 coverage-challenge exclusion — correctly a deliberate asymmetry, not drift.
> - Labels {C1,C2,C3,C4,C5,C6,C9,C10} gating + {C7,C8} advisory consistent; only concern C9a's KEEP under-inclusiveness (→B-3).
>
> ## OVERALL VERDICT
> **MAJOR — do NOT freeze yet.** The substance is close and prior findings genuinely resolved: the frozen oracle is complete/correct/correctly-scoped; C1 source-anchoring is the right structural fix; direction, sequencing, Tier-2, KEEP/C10 framing, exclusion decisions all sound. Three MAJORs remain, all in the plan's construction guidance / one gating-check spec, not the oracle: (1) §A table omits 4 rows + false completeness claim; (2) plan:17 stale "closed-set" word; (3) C9a KEEP list under-inclusive. **None is a blocker** — the oracle-anchored C1 gate + source-walk mean no rule can be lost at acceptance. All three are cheap localized text fixes. **Recommendation:** apply the three fixes, then this is freeze-ready — best treated as a mechanical touch-up rather than another full red-team lap. As written, not clean; I do not certify freeze.

## Author disposition (2026-07-06)
All three MAJORs + both minors **applied and mechanically verified** (grep evidence in `decisions.md`):
§A mapping now carries A-9-6/A-9-7/B-EVID-1/B-CAUS-1 (abbreviation-aware check: **0 genuine gaps** across
all 86 IDs); plan:17 closed-set moved to EXCLUDES; C9a KEEP gained category (f) + a composition-vs-
dependency classification rule (no longer a closed allow-list); freeze-item 5 added; "3 arms"→"4 arms".
Per the reviewer's explicit disposition ("apply the three fixes → freeze-ready; mechanical touch-up, not
another lap") the fixes are routed **fix-in-place**. Freeze decision surfaced to the owner (the "freeze
only if clean" bar) — see `decisions.md`.
