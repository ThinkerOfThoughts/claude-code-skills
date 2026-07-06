# 3 — Red-team the plan (ROUND 2) — verbatim record

Cold stage-3 review (round 2) of the REVISED {1-spec, 1.5-criteria, 2-plan, 2-rule-oracle}, carrying
round-1 findings forward (`3-redteam-plan.md`). Fresh cold agent, no shared context.

## Context + provenance
Reviewer: **general-purpose**, model **claude-opus-4-8[1m]**, read-only. Reviewer independently
recomputed all counts + hashes. Reviewer-reported context hashes (round-2, post-fix):
1-spec `8f163fc8…`, 1.5-criteria `33e4cc39…`, 2-plan `4832b9aa…`, 2-rule-oracle `09efa5e6…`,
3-redteam-plan `9d373742…`, Dragonfly/SKILL `b5e122ef…`, Dragonfly/METHODOLOGY `04d1044c…`,
gc charter `6b98164d…`, gc stage-8 `d737f1bc…`, gc stage-4 `4ea889d5…`, gc stage-7 `070a966a…`.
(Also read `decisions.md`, flagged out-of-set.) Verdict: **BLOCKER**.

## Reviewer's verbatim output

> # COLD RED-TEAM REVIEW RECORD (ROUND 2) — dragonfly per-stage restructure + untangle (Themes 1+2)
>
> ## PART A — did the round-1 fixes land?
>
> | # | Round-1 finding | Verdict | Citation |
> |---|---|---|---|
> | 1 | Oracle miscount → 81 (33/31/17) | **ADDRESSED in oracle / see B-1** | oracle+criteria correct (my count: 33/31/17=81); **but `2-plan.md` still says "78" at :5, :56, :122** → B-1 |
> | 2 | Missing A-8-2; A-7-3 phantom | **ADDRESSED** | A-8-2 at oracle:53 (SKILL 76-77/METH 231, stage `8`, KEEP); A-7-3 disclaimed at oracle:130 |
> | 3 | C9a under-inclusive grep | **PARTIALLY — repeat** | now read-confirm + classified grep, but the revised pattern set **still misses SKILL:107 and METH:394** → B-2 |
> | 4 | Over-fork position/concurrency | **PARTIALLY — repeat** | pos/concurrency + A/B excluded & recorded; **but the "closed-set input" rule is STILL forked in** → B-3 |
> | 5 | Coverage gap → anti-oracle C1 check | **ADDRESSED as written / partly defeated by B-3** | criteria:36-40 reverse check present; premises violated by B-3 (plan authorizes an un-oracled add) |
> | 6 | C9b transitivity | **ADDRESSED** | criteria:139-143 names it |
> | 7 | Tier-2 cross-cutting@2nd-stage | **ADDRESSED** | SC-4 (plan:155); SC-2 stage-7 residual (plan:159-162) |
> | 8 | load-floor / mechanical count / severity source | **ADDRESSED** | plan:106-109; oracle:142; severity → gc stage-8:143-174 (verified) |
>
> ## PART B — new-defect hunt
>
> **[BLOCKER] 2-plan.md:5, :56, :122 — the oracle-recount did NOT propagate to the plan; it still says "78 rules" in three load-bearing places**, including the operative C1 build instruction (":122 every one of 78 rows present + correctly scoped"). A builder following the plan builds a 78-row mapping table against an 81-row frozen oracle and drops 3 rows (A-8-2 among them). This is the round-1 miscount BLOCKER *relocated*, not eliminated. **Fix:** all three → "81" (then the recount); add `grep '\b78\b'` = empty to the freeze checklist.
>
> **[MAJOR] 2-rule-oracle.md Group A — a real, twice-stated stage-9 rule is missing: the stage-9 residuals re-check** (SKILL:88 "residuals re-checked"; METH:255-256 "Stage 9 also re-checks the residuals list: killing the primary does not close an unexplained residual"). No A-9-* row covers it (A-9-1..5 verified at oracle:55-59); not A-7-5 (creates residuals) nor A-8-1 (carries them). Identical class to round-1's A-8-2. C1 (graded against the oracle) cannot detect if the build drops it from stage-9.md. **Fix:** add A-9-6 (SKILL:88/METH:255-256, stage `9`); recount to 82.
>
> **[MAJOR] 2-rule-oracle.md Group A — a second missing stage-9 rule: the characterized-handoff stage-9 verification clause** (SKILL:88 "Characterized → symptom-evidence only"; METH:234-235 "stage 9 verifies the marked mitigations on symptom evidence only — no cause-resolution claim"). A-8-3 covers the characterized *verdict bar* at 7/8, not *how stage 9 verifies* a characterized handoff. Not in any A-9 row. **Fix:** add it as a stage-9 row; recount.
>
> **[MAJOR] 2-plan.md:137-138 / 1.5-criteria.md:124-129 — the revised broadened C9a grep still misses two of the six survivors it was named to catch.** Applied to source: `guarded-change's (charter|rubric|severity|provenance)` requires the keyword *immediately* after — SKILL:107 "guarded-change's **unchanged** stage-3/6 charter" has "unchanged" intervening → no match. `inherits? guarded-change` requires adjacency — METH:394 "inherit **ALL of** guarded-change's" → no match. The plan sets "Zero surviving rules-dependency hits = pass" (:139), so the grep is a pass gate with two blind spots. Read-confirm backstops the 4 fork targets, but the grep half's claim to cover the named misses is false. **Fix:** anchor patterns on `guarded-change` (`inherit.*guarded-change`, `guarded-change'?s?.*(charter|rubric|severity|provenance|discipline|unchanged)`), or make C9a a whole-file read-and-classify of every `guarded-change` hit and drop the literal-list pass condition.
>
> **[MAJOR] METHODOLOGY.md:420 (C-REF-1) — a by-reference phrasing lands in a file the plan maps as unchanged, with no recorded edit.** METH:420 "the red-team charter (**referenced from guarded-change**)" must be rewritten by Theme 2. C9a's `referenced from guarded-change` pattern will flag it (good), but the mapping (plan:54) routes C-REF-1 into slim METHODOLOGY unchanged and the oracle's C-REF-1 row (oracle:115) isn't flagged HOME=byref → mapping and C9a disagree. **Fix:** note in the C-REF-1 mapping/oracle row that the "referenced from guarded-change" clause becomes "dragonfly's own charter".
>
> **[MAJOR] 2-plan.md:69 / 1.5-criteria.md:119 — the fork imports the "closed-set input" rule, NOT current dragonfly behavior and NOT an oracle row → the same new-normative-rule class as round-1, on the piece the fix missed, and an *unrecorded* C9b divergence.** Current dragonfly's provenance (B-PROV-1, oracle:85; SKILL:122-123/METH:388-395) spells out only "verbatim charter, exact context list, verbatim output, agent+model, hashes" — no "reviewer input is a closed set / supplementary context quoted" rule (grep of SKILL+METH empty). Round-1 named the closed-set rule in the same breath as the A/B clause as "content dragonfly never had"; the revision excluded A/B but kept closed-set as a fork target. Absent from the 81-row oracle; not in the C9b "only permitted" divergence list → an unrecorded, un-oracled behavior addition. **Interaction:** the anti-oracle C1 check should catch it, but the plan *authorizes* it as intended fork content → the guard is defeated by the artifact it guards. **Fix:** decide explicitly — (i) EXCLUDE closed-set from the fork (match dragonfly's provenance exactly) + record the exclusion; or (ii) accept it, add a B-PROV oracle row, record as a permitted divergence (no longer pure preservation for that rule).
>
> **[MINOR] freeze checklist should mechanically assert the single count token appears identically in oracle+criteria+plan** (`grep -rn '\b78\b'` empty outside the round-1 record). Kills the count-drift class.
>
> **[MINOR] stage-9 oracle rows (A-9-1..5) are the least complete in the inventory** (B-4/B-5) — re-walk METH:233-259 + SKILL:88 line-by-line before freezing.
>
> **[NITPICK] 2-plan.md:135 cites 9-report.md as the KEEP-list source, which doesn't exist yet** (stage-8 artifact). Fine for a plan gate, but the C9a KEEP set is not yet operable — ensure the stage-8 harness enumerates it (sibling framing, A-8-2 handoff, full-GC triage invocation, "guarded-change makes the fix", fork-provenance note).
>
> ## Coverage-challenge result
> - The closed-set-rule addition (B-3) is observed by no criterion that would flag it wrong (C1-forward checks presence; C9b passes — it IS in gc source; C1-reverse defeated because the plan authorizes it). Round-2 coverage gap.
> - The two missing stage-9 rules are observed by no criterion (not in oracle; no Tier-2 arm at stage 9). Silent drop passes every gate.
> - Stage-7 GBP (B-GBP-3) unobserved by any arm — but now a *recorded* residual → acceptable-by-disclosure.
>
> ## Label-audit result
> - C1/C9/C10/C3/C4/C5/C6 correctly gating; C7/C8 advisory — appropriate.
> - C9a's gating label rests on a grep with two blind spots (B-2); effective strength below label outside the 4 fork targets. Anchor the grep on `guarded-change` to earn the label.
>
> ## Overall verdict
> **BLOCKER.** Round-1's fully-fixed items are genuinely addressed. But the recount escaped into the plan (B-1, BLOCKER); the C9a grep still misses 2 named lines (B-2); the closed-set rule is still over-forked (B-3); and two more real stage-9 rules are missing from the "complete" oracle (B-4/B-5) — the highest-value finding, proving the inventory is still incomplete. Direction, sequencing, Tier-2, KEEP/C10 framing, and the anti-oracle concept remain sound. Do not pass gate 4 until: the plan's "78"s → the recount; the two stage-9 rows added + count re-derived; C9a grep anchored on `guarded-change` (or full read-and-classify); the closed-set fork explicitly decided; METH:420 noted for edit.

## Iteration-cap note
Round-2 findings are, by the reviewer's own framing, the **same finding classes** as round-1 (count
consistency; C9a completeness; charter over-fork; missing oracle rows). Per the severity model's
iteration cap ("2 bounces at the same gate on the same finding class → a human breaks the tie"), the
cap has **fired at gate 4**. → Escalated to the owner (see `decisions.md`).
