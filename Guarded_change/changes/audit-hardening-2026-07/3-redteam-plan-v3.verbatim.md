# Stage-3 red-team of the v3 re-plan delta (round 1) — verbatim record

## Provenance
- **Date:** 2026-07-03. **Reviewer:** cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author.
- **Scope:** the C3-instrument-v2 delta only (plan-v3 addendum + criteria-v3 C3 row +
  position-note edit), per the owner's stage-8-major tie-break (re-plan).
- **Context given (closed set):** change-folder docs {2-plan.md, 1.5-criteria.md,
  8-battery-round1.verbatim.md, 8-battery-round2.verbatim.md, decisions.md,
  fixtures/review-record/ (7 files)} + amended METHODOLOGY.md. Reviewer-reported sha256s at
  the top of the verbatim output. Author spot-check: METHODOLOGY hash `35a6798d…` matches
  fixture-check-1's report; fixture hashes match fixture-check-3's list.
- **Charter/prompt given (verbatim):**

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your review.

This is a STAGE-3 plan red-team of a RE-PLAN DELTA inside an ongoing guarded-change run. The run amends the guarded-change skill's own docs (9 additive rule fixes, already built and code-reviewed). One acceptance criterion — C3, a replay A/B experiment testing whether the amended docs change reviewer behavior — failed its original frozen pass condition twice, hit the pre-committed human gate, and the owner chose "re-plan the instrument." Your scope: attack the REDESIGNED C3 instrument only (the plan-v3 addendum + the criteria-v3 C3 row + its position-note edit), not the 9 rule fixes (already reviewed at earlier gates) and not the battery rounds already run.

## Context (closed set — read these, nothing else)

All under /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/:
1. `2-plan.md` — read the "Plan v3 addendum" section at the end (the delta under review); the earlier plan-v2 body is background.
2. `1.5-criteria.md` — the C3 row (v3, redesigned) + the position-sensitivity note at the top (edited at v3); other rows are frozen background.
3. `8-battery-round1.verbatim.md` and `8-battery-round2.verbatim.md` — the evidence the redesign is diagnosed from (scoring + diagnosis sections at the end of each; the arm outputs are the raw data).
4. `decisions.md` — the gate log (run history, the two human tie-breaks, the unfreeze entry).
5. `fixtures/review-record/` — the current fixture (v1 of it; the delta specifies two conformance fixes FX-A/FX-B to build).
6. `/home/zero/Desktop/claude-code-skills/Guarded_change/METHODOLOGY.md` — the amended methodology (rule inventory; the "docs-a" the treatment arms read).

## Charter

Attack the delta on four lenses: 1. FACTUAL — do the addendum's claims match the record? (e.g., are the cited round-1/2 tallies correct against the scoring tables? are the diagnosis claims supported by the arm outputs?) Cite file:line for everything you check; a clean factual verdict with zero citations is treated as an un-run review. 2. LOGICAL — flaws in the redesign's reasoning (scoring design, leak analysis, pre-committed dispositions). 3. MISSED OPPORTUNITY — better instrument designs left on the table, given the diagnosed failure modes. 4. UNSTATED ASSUMPTIONS & RISKS — what the redesign takes for granted that could be false.

Discipline: cite a line or a concrete failure scenario for every finding; rank every finding blocker/major/minor/nitpick; flag anything you could not verify rather than silently accepting it; "no issue found" per lens is allowed and expected when true; audit any gating/advisory (re)labeling — the V3 demotion from gating to observational is a DELIBERATE re-plan decision made under owner authority, so do not re-litigate whether demotion is allowed; DO attack whether its execution is honest and consistent (e.g., does any surviving text still overclaim what V3 evidences?).

Criteria-coverage challenge (required section): name behaviors the redesigned instrument could get wrong that NO pass condition or tripwire observes — an explicit "none found" counts.

Task-specific attack surfaces (quoted as such, from the author): "(a) Are the v3 pass conditions genuinely mechanical — can a scorer apply '≥2/3 treatment catches citing the deciding rule' and '0 control catches' without judgment calls? Name any ambiguous edge (partial catches, multi-rule citations, a catch of the right violation via the wrong rule). (b) Does fixture fix FX-A leak? — it adds an in-fiction fail-against-unguarded + targeted-check record; under the pre-change docs no such duty exists, so could its PRESENCE teach a control reviewer the new rule, or draw new off-seed fire under either rule set? Same for FX-B. (c) Is the 'rounds 1-2 carried but not re-scored' clause coherent — does any part of the v3 design covertly re-score old data? (d) Do the pre-committed dispositions cover every outcome (all-pass / any-miss / tripwire / off-seed fires), or is there an outcome with no pre-committed route?"

Rank findings and end with: worst severity + a one-paragraph verdict on whether the delta is fit to route to build.
```

## Reviewer output (verbatim)

# Stage-3 cold red-team — C3 instrument v2 re-plan delta

## Context-file hashes (sha256, computed by me)

| File | sha256 |
|---|---|
| `2-plan.md` | `08ee67da63c513299376dfa4677f6f32c67540d7079601c4fd93154e79fd0a5b` |
| `1.5-criteria.md` | `b52639aba1c2214eba5d5b95218e84514dac1d31ee07b73a9b0fd5f8b6acf7c7` |
| `8-battery-round1.verbatim.md` | `8f79c481dcf1e69d55281af90bc8a920e0a9487d25ff005004b8b9edbf5826c2` |
| `8-battery-round2.verbatim.md` | `ae91eeef1ad2b2c358e395b7a912725d0edbb2be32aec274ace208c91c9a8679` |
| `decisions.md` | `7bdec6ba3303251d3088a33308de911ba86ec0d4125c402b1ff99abb68bcba7b` |
| `METHODOLOGY.md` | `35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3` |
| fixture `1-spec.md` | `baed3ea40a94316f5fbbe7bf690160ea26f0a1a87bf4d3f5c70047923a8f7a7d` |
| fixture `1.5-criteria.md` | `6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d` |
| fixture `2-plan.md` | `9b6954b521d5c62790df237c5ab8c79736335a962685f97c8253107e00558ca3` |
| fixture `3-redteam-plan.md` | `8613c4ea4adc3ad5f02df52c9b03ec54f2aac9f61e9781eba51e153389d19903` |
| fixture `6-redteam-code.md` | `43fb7b222388956c7cf698d73e784a3e0a0985d71f7937c1b35cd0f20fd4ec61` |
| fixture `8-harness.md` | `ca69d09443f50260b623a610a2e4eb1c3fce628534ae448d51414787e0b2263c` |
| fixture `decisions.md` | `b1626329045f28a1e870c5896fb364d28a7c5c352e37e5859b30ac8216e3520d` |

Mechanical checks I ran beyond reading: `wc -l` on live source docs (534/124, matches the gate-7 caps record at `decisions.md:86`); `git show 8a7ac65` line counts (467/102, matches `decisions.md:8`); greps of the `8a7ac65` METHODOLOGY for new-rule vocabulary.

---

## Lens 1 — FACTUAL

**F-1 (clean, verified). The carried tallies are correct against the scoring tables — except one characterization (see F-3).**
- V1 4/4-T vs 0/4-K (`2-plan.md:140`): round 1 T1/T2 CATCH, K1/K2 no-flag (`8-battery-round1.verbatim.md:404`; confirmed in arm outputs at round1:109, round1:217, round1:306, round1:322); round 2 T3/T4 CATCH, K3/K4 no-flag (`8-battery-round2.verbatim.md:295`; arm outputs at round2:30-35, round2:132-136, round2:209, round2:241). Correct.
- V2 3/4-T vs 0/4-K (`2-plan.md:140-141`): round 1 2/2-T (round1:405; T1 at round1:77, T2 at round1:203), round 2 1/2-T (round2:296; T3 miss verified — its C1 verdict at round2:85 never mentions the evidence pointer; T4 catch at round2:159). Controls 0/4 (round1:268, round1:356, round2:211, round2:243). Correct.
- V4 8/8 (`2-plan.md:141`): round1:407, round2:298; verified in all eight arm outputs. Correct.
- "One unseeded treatment-only F2 fire (T3 on the C3 harness)" (`2-plan.md:141-142`): verified at round2:68-75; no control produced the F2 reading. Correct, but see F-4.
- "Tripwire never triggered" (`2-plan.md:142`): round1:416-417, round2:305-307, with author verification of every control-cited rule against docs-b. I independently verified the cited docs-b rules exist at the claimed lines: deferral at 8a7ac65 METHODOLOGY:43-48, earned-clean at :214-217, earned-label-audit at :237-239, comparable-workload at :357. Correct.
- Diagnosis claim (2) — "the fixture … is not fully conformant under the AMENDED rules" (`2-plan.md:144-148`): supported by T3's fire (round2:68-75) and K4's regression fire (round2:274-275, classified at round2:315-317). Correct as stated.
- New-rule status of the V1/V2 seeds: I grepped `8a7ac65` METHODOLOGY for "provenance", "evidence pointer/column", "verbatim record", "sha256", "targeted cold check", "unreviewed check" — **zero hits**. The deciding rules for V1 and V2 are genuinely new; the differential design's premise holds.

**F-2 (MAJOR). FX-A's leak analysis contains a false claim: the added record IS citable — under the amended rules.**
`2-plan.md:157-159` asserts the FX-A addition is "in-universe compliance, not citable as a violation, invisible-to-controls." The invisible-to-controls half is defensible (precedent: the D3 path-validation/freeze-hash records, `decisions.md:69-72`, drew zero control fire across 4 controls). But the not-citable half is wrong on the treatment side: FX-A advertises a targeted post-6 cold check ("harness scripts cold-checked (targeted) before results counted", `2-plan.md:153-154`) while adding **no provenance record for it** — only a `decisions.md` line and a harness note. Amended F1 (`METHODOLOGY.md:236-250`) explicitly covers "a targeted post-6 check" and rules "a record missing any of these = the review is treated as un-run"; amended F2 (`METHODOLOGY.md:386-395`) then makes the harness results `verified = no`. A round-3 treatment reviewer has textbook grounds to rule the advertised check un-run and re-fire on C3 (and now C1 — FX-A shows fail-against-unguarded only for C3's script, though C1's mock also "guards a fix"). FX-A as specified converts T3's off-seed fire into a new off-seed fire one level up, violating the delta's own stated standard ("conformant under BOTH rule sets except at the seeds", round2:313-314). See LO-1 for the unconfronted design tension underneath.

**F-3 (MAJOR). "V3 ≈50% in BOTH arms" misstates the record; the honest numbers are 1/4-T vs 3/4-K, and they pool across a mid-experiment stimulus change.**
- `1.5-criteria.md:9-10`: "rounds 1–2 measured its detection at ~50% in BOTH arms"; `2-plan.md:141`: "V3 ≈50% both arms". The measured rates are treatment 1/4 (25%) and control 3/4 (75%) — recorded honestly at `decisions.md:216` and round2:324. "~50%" is true only pooled. A cold reader of the criteria note alone would conclude no arm asymmetry was observed; what was observed is a treatment-side deficit — exactly the "marked treatment-side collapse … displacement signal" the same note promises to surface. At n=4/arm this is statistically indistinguishable from noise (round2:324 says so, legitimately), but the surviving text states a measurement that was not the measurement.
- Second distortion by pooling: V3's fixture text changed between rounds (verbose walk → terse assertion, `decisions.md:184-189`); detection moved 3/4 (round1:406) → 1/4 (round2:297). The "~50% at n=8" owner-finding figure (`1.5-criteria.md:22`) averages two different stimuli; the current-fixture (round-3) version's observed rate is 1/4. Round 3's observational V3 counts will "feed" this pooled figure across a third fixture context (FX-A/B edits elsewhere in the record).
- This is the one place the "carried, not re-scored" history is carried **distorted**. The demotion itself is owner-authorized and not re-litigated here; its written justification should carry the true per-arm numbers.

**F-4 (minor). T3's precedent fire was mixed-grounds, weakening the "NEW-rule fire" classification the delta reuses.**
Round2:71 shows T3 grounded its C3 invalidation on METHODOLOGY 388-392 (new F2) **and** 163-166 (pre-existing interleaving fail-against-unguarded — verified present in docs-b at :162) and 371-374 (pre-existing proxy-path). The scoring (round2:308-314) and the delta (`2-plan.md:190-192`) classify it as a new-rule fire. The sharp `verified = no` arguably did need F2, but the delta's round-3 classifier "a treatment-only fire grounded in a NEW rule" (`2-plan.md:190-191`) has no rule for mixed-grounds fires — see LO-4.

**Could not verify:** the criteria header's claim "all other rows unchanged from frozen v2 `c29dfada…`" (`1.5-criteria.md:1`). The change folder is untracked in git (`git status`: `?? Guarded_change/changes/audit-hardening-2026-07/`) and no verbatim v2 copy exists in the record — hash-only freezes are unverifiable across an unfreeze-edit. Flagged, not assumed (see AR-4).

## Lens 2 — LOGICAL

**LO-1 (MAJOR, the reasoning under F-2). The delta never confronts the conformance-vs-leak bind that FX-A sits in.**
To be fully conformant under amended F1, the in-fiction targeted check needs an embedded verbatim charter — whose text (representativeness, fails-against-unguarded) is near-F2 rule text visible to controls via the shared fixture. That is precisely the leak class D1 was engineered around for V3 (`decisions.md:60-66`: the provenance bullet was deliberately kept OUT of the fixture charter to avoid teaching controls). The delta's one-line leak analysis ("same class as the D3 freeze-hash record", `2-plan.md:157-158`) treats FX-A as a solved case when it is actually the harder case D1 already flagged. The fix needs an explicit design decision (e.g., a provenance-complete in-fiction record whose charter paraphrases only pre-change duties plus a quoted task addition, mirroring the D1 compromise, with a pre-committed adjudication for a treatment fire on the residual gap — mirroring the V3/D1 residual at `2-plan.md:74-79`).

**LO-2 (MAJOR). The v3 V4 bar does not enforce what the position note says it proves.**
`1.5-criteria.md:6-8` claims "C3's V4 probe (gated ≥4/6 in v3) is the executed behavior-preservation check — a PRE-EXISTING rule adjacent to the densest insertion cluster … must still fire **through the amended docs**." But ≥4/6 is **combined across arms** (`2-plan.md:180`, `1.5-criteria.md:22`): 3 control catches + 1 treatment catch = 4/6 passes, on an outcome pattern (1/3-T vs 3/3-K) that is itself displacement evidence. Only treatment catches test firing "through the amended docs"; the condition as written can be satisfied almost entirely by docs-b arms. Historical risk is low (V4 8/8, T-side 4/4), but the entire point of the v3 redesign was bars that behave under attention noise. Cheap fix: per-arm floors (≥2/3 T and ≥2/3 K), which also gives the control arm a competence check (see the coverage challenge). As written, the position-note sentence overclaims what the condition evidences.

**LO-3 (MAJOR). "Pass conditions (pre-committed, mechanical)" — the load-bearing term "catch" is not defined, and rounds 1-2 prove the edge cases are real, not hypothetical.**
The author is the scorer (as in rounds 1-2; nothing in the delta assigns scoring elsewhere), and the record already contains three precedents that required judgment:
- T1's V2 disposition was "**valid** but under-evidenced" in its summary (round1:119) yet scored CATCH (round1:405, justified as "rule-grounded flag").
- T2's V1 was hedged — "un-run on the provenance rule (**strict reading**) … a real defect but a less certain one" while listing stage-3 as "VALID to act on" in the same table (round1:231-232) — scored CATCH.
- K4's C3 was "CONDITIONALLY VALID / not production-proven" (round2:271-272) — the pattern that, on a seeded row with a 0-K condition, has no ruling.
Under v3 the same ambiguity now decides **fail** conditions too ("0 control catches"). Nothing defines whether a catch requires the artifact to appear in the arm's final un-run/unverified disposition, or whether a rule-cited caveat inside a "valid, but…" paragraph counts. Until "catch" has a pre-registered extraction rule (e.g., "an artifact counts as caught iff the arm's final disposition treats it as un-run/unverified/invalid, citing a rule; hedged flags count iff rule-cited; every edge call recorded verbatim in the scoring table"), the "mechanical" label on `2-plan.md:176` is not yet true, and the author retains mid-experiment discretion over pass/fail edges of his own instrument.

**LO-4 (minor). Pre-committed dispositions have unassigned collisions.**
- All-conditions-met + an off-seed fire revealing a both-rule-set fixture defect: `2-plan.md:184-188` routes all-pass → PASS while `2-plan.md:192-193` routes any both-rule-set-defect fire → "instrument defect → the diagnosed-fix path". Precedence unstated: does a K4-class fire in an otherwise-passing round invalidate the round or ride along (as it did in round 2, round2:315-317)?
- Mixed-grounds fires (F-4): "grounded in a NEW rule" needs a classifier (suggest: counts as new-rule-grounded iff the verdict is unreachable from docs-b rules alone).
- The tripwire test "citing a rule absent from its docs" is scope-fuzzy where docs-b contains the same phrase with narrower scope — a control stretching the interleaving-scoped fail-against-unguarded rule (docs-b:162) to a non-concurrency harness check cites a rule that is present-but-out-of-scope. FX-A's fail-against-unguarded record invites exactly this stretch.

**LO-5 (minor). V1's "0 K catches" is flat while V2's has the old-rule carve-out — and the surviving plan-v2 text contradicts the flat version.**
`2-plan.md:177` (V1: "0 K catches") vs `2-plan.md:178-179` (V2: "0 K catches **citing a new rule**", old-rule catch = codification evidence, not a fail). Plan v2, which "stands" (`2-plan.md:135-136`), still says "a legitimate current-rule catch of V1 is recorded as evidence against F1's demonstrated marginal value" (`2-plan.md:85-87`) — i.e., record-and-continue, not fail. Under v3 that same event is a hard battery FAIL whose pre-committed route ("diagnosed-fix re-run") is incoherent: a *legitimate* old-rule control catch is not an instrument defect — there is nothing to fix, and a re-run with fresh controls is resampling toward 0-K, the exact behavior the no-resampling rule exists to prevent. Mitigating: my grep confirms docs-b has no provenance/verbatim-record vocabulary, and 0/4 controls flagged V1 empirically — hence minor, not major. Fix: give V1 the same carve-out shape as V2.

**LO-6 (nitpick). "Differential scoring" is a generous name.** The v3 conditions are a lowered treatment threshold (2/2 → ≥2/3) plus zero-control conditions — not the "T-rate vs K-rate per seed" comparison the round-2 diagnosis described (round2:342-343) and the owner's scope words gestured at ("differential rates", `decisions.md:233`). It is still differential in the sense that matters (T>0 where K=0), and the n=3 limitation is carried honestly; but the largest single contributor to round-3 pass probability is the (authorized) V3 demotion, not the scoring change. Worth one honest sentence in the verdict.

## Lens 3 — MISSED OPPORTUNITY

**MO-1 (minor). Seed isolation was left on the table.** Both diagnosed failure modes reduce to *attention competition on a target-rich record* (round1:432-438, round2:339-343). The instrument that attacks the root cause is seed isolation — e.g., two thin fixture variants (V1+V4 in one, V2+V3 in the other), each arm-pair seeing fewer competing targets — rather than lowering the bar on the same crowded record. Cost: one more fixture + F2 check. The delta neither adopts nor rejects it; it plausibly fits inside the owner's re-plan scope ("fixture conformant under both rule sets; fresh battery", `decisions.md:232-234`). At minimum the rejection should be logged.

**MO-2 (minor, fix for LO-2).** Per-arm V4 floors — one line, and it converts V4 back into the preservation probe the position note claims it is, plus a free control-arm competence check.

**MO-3 (minor, fix for LO-3).** Pre-register the catch-extraction rule and (cheap) have the round-3 scoring table itself cold-verified — the rounds 1-2 scoring was author-only, and the record shows the author making instrument-favorable edge calls (T1-V2 CATCH) alongside instrument-unfavorable ones (honest); a targeted check of the scoring table is one small spawn.

**MO-4 (minor).** Convert the position note's "a marked treatment-side collapse would be surfaced" (`1.5-criteria.md:10-12`) into a mechanical tripwire (e.g., V3 0/3-T with ≥2/3-K → treat as suspected displacement → STOP/investigate before disposition). As written it is a promise with no trigger, threshold, or route.

**MO-5 (nitpick, fix for AR-4).** At the v3 re-freeze, record a verbatim copy of the criteria (F4 explicitly allows "hash **or** a verbatim copy", `METHODOLOGY.md:168-169`), so the next unfreeze is diffable by a cold reviewer — this run just demonstrated hash-only freezes go dark after an unfreeze-edit.

## Lens 4 — UNSTATED ASSUMPTIONS & RISKS

**AR-1 (covered by F-2/LO-1).** The delta assumes fixture v2 will be conformant under the amended rules after FX-A/FX-B. As specified, FX-A itself breaks that assumption.

**AR-2 (minor).** The pre-battery F2 targeted check is charged with confirming the fixes are "legal under both rule sets" (`2-plan.md:164-167`), but its context is unspecified — the checker cannot verify both-rule-set legality without being handed docs-b as well as docs-a. Prior fixture checks' charters aren't in my closed set to confirm either way. One sentence fixes it.

**AR-3 (minor).** "Every run counts; no resampling" has no stated policy for an arm that dies mid-run — a real event in this very run (`decisions.md:32-33`, the gate-4 respawn). Pre-commit: a no-output arm is respawned fresh and logged; a partial-output arm counts.

**AR-4 (minor / could-not-verify).** The claim that only the C3 row and position note changed at v3 rests entirely on author assertion; the v2 file exists only as a hash (`decisions.md:43`) and the folder is untracked. A cold reviewer cannot audit the unfreeze's actual diff. (Also applies forward: `2-plan.md:198-199` re-freezes with "new sha256" — same darkness next time. MO-5.)

**AR-5 (nitpick).** Round 3 re-verifies run-record hashes against the F2 check's list (`2-plan.md:173-175`) but does not restate the round-1 discipline of verifying the docs-b export byte-identical to `8a7ac65` at launch (round1:11-12). Say it.

**AR-6 (noted, no finding).** FX-B checks out: the comparable-workload rule is verified present in docs-b (:357) and docs-a (:412), the relabel is symmetric and rule-conformant in-fiction, and it removes a *control-side* distraction — which makes controls more attentive and the 0-K conditions harder, i.e., the bias runs against the instrument's own interest. Honest design. Residual note: FX-A defuses only the new-rule leg of T3's C3 fire; the pre-existing proxy-path leg (round2:72, docs-b label-audit text) remains available to both arms with no pre-committed classification (defect vs. legitimate reading) — folds into LO-4.

## Criteria-coverage challenge (required)

Behaviors the redesigned instrument could get wrong that **no pass condition or tripwire observes**:
1. **Treatment-side V3 collapse** — observational, no bar, no tripwire. Scenario: round 3 V3 = 0/3-T vs 3/3-K; every pass condition is met; C3 records PASS holding an un-routed displacement signal (cumulative T 1/7 vs K 6/7). The position note's "would be surfaced" has no mechanism (MO-4).
2. **Control-arm competence** — nothing observes whether the controls actually reviewed. Scenario: two shallow controls catch nothing anywhere including V4; V4 passes 3T+1K = 4/6; V1/V2's 0-K conditions pass vacuously; the differential is inflated by weak controls and no condition or tripwire fires (fix = per-arm V4 floor, MO-2).
3. **Scoring fidelity** — the author scores his own instrument's pass/fail; no condition observes a misscored edge call (LO-3/MO-3).
4. **Off-seed attention burn** — fires are recorded, but an arm whose output is dominated by off-seed content with thin seed engagement still counts fully toward the denominators; the composition failure the redesign targets can recur inside a "counted" arm with no observable.
5. **docs-b export integrity at round-3 launch** — hash-verified for the fixture, restated nowhere for the docs arms (AR-5).

## Task-specific attack surfaces (answers)

**(a) Mechanical?** No — not yet. "Catch" is undefined and rounds 1-2 already produced three edge precedents (hedged catch, valid-but-flagged catch, conditional-validity pattern) — LO-3. Named ambiguous edges: partial/hedged catches counted by rule-citation vs final disposition; a rule-free control flag (unassigned between catch and non-catch — n2: V2's control side distinguishes only "new rule" vs "docs-b rule", not "no rule"); multi-rule citations (V1 presence-among-grounds is precedented via the v2 V3 adjudication, but unstated for v3-V1); right-violation-wrong-rule — a treatment catching C1 via FX-A's F2 gap ("no fail-against-unguarded shown for C1's script") scores as a V2 catch under "any rule-grounded reason" while evidencing F2, not F3, silently re-inflating F3's attribution in the verdict.

**(b) FX-A leak?** Presence-teaching of controls: low risk, with empirical precedent (D3's F8-shaped path-validation record drew 0/4 control fires), though FX-A's phrasing mirrors F2's rule text more closely than D3 did, and the tripwire's "rule absent from its docs" test is scope-fuzzy against docs-b:162 (LO-4). The real defect is treatment-side: FX-A's advertised-but-recordless targeted check is citable under amended F1+F2 and predictably re-creates the off-seed fire class it exists to defuse (F-2/LO-1) — the delta's "not citable as a violation" claim is false under docs-a. FX-B: clean (AR-6).

**(c) "Carried but not re-scored" coherent?** At the pass-condition level, yes: all v3 conditions are computed on round-3 arms only; the two FAILs persist append-only in `decisions.md:174, 211`; the carried tallies are accurate (F-1). Two soft spots: the "~50% in BOTH arms" compression is the one place carried history is distorted (F-3), and the V3 owner-finding pools detection across two (soon three) fixture versions — an observational statistic quietly aggregated under a frame none of that data was collected under (F-3, second half). Neither covertly re-scores against the v3 bars.

**(d) Dispositions complete?** All-pass / any-miss / tripwire / treatment-only-new-rule fire / both-rule-set-defect fire are each routed. Gaps: all-pass + both-rule-set-defect-fire collision (LO-4); legitimate old-rule control catch of V1 → hard FAIL with nothing to diagnose and a re-run that is resampling by another name (LO-5); mixed-grounds fire classification (F-4/LO-4); dead-arm policy (AR-3); V3 treatment collapse — deliberately observational, but with a promised surfacing that has no route (MO-4).

---

## Ranked findings

| # | Severity | Finding |
|---|---|---|
| F-2/LO-1 | **major** | FX-A as specified is non-conformant under the amended rules (advertised targeted check with no provenance record) — re-creates the off-seed fire class it exists to defuse; the delta's leak analysis is factually wrong that the addition isn't citable, and the conformance-vs-leak bind is unconfronted |
| LO-2 | **major** | V4's ≥4/6 combined bar doesn't require treatment catches; the position note's "executed behavior-preservation check … through the amended docs" overclaims what the condition enforces (3K+1T passes while evidencing displacement) |
| F-3 | **major** | "V3 ~50% in BOTH arms" (criteria note + addendum) misstates the record (1/4-T vs 3/4-K) and pools across a mid-experiment fixture change (3/4 → 1/4) — the demotion's written rationale distorts the data it cites |
| LO-3 | **major** | "Catch" undefined; "mechanical" pass conditions are author-scored with demonstrated judgment-call edges from rounds 1-2 now deciding fail conditions too |
| LO-5 | minor | V1's flat "0 K catches" lacks V2's old-rule carve-out, contradicts carried plan-v2 text, and its on-fire disposition is incoherent (fix-nothing re-run = resampling) |
| LO-4 | minor | Disposition collisions: pass+defect-fire precedence; mixed-grounds fire classifier; tripwire scope-fuzz vs docs-b:162; FX-A leaves T3's proxy-path leg unclassified |
| F-4 | minor | T3's precedent "NEW-rule fire" was mixed-grounds (cited pre-existing 163-166 alongside F2) |
| MO-1 | minor | Seed isolation (root-cause fix for attention competition) neither adopted nor rejected |
| MO-4 | minor | V3 displacement "surfacing" has no trigger/threshold/route |
| AR-2 | minor | F2 check's both-docs context unspecified, so "legal under both rule sets" is unverifiable by it as chartered |
| AR-3 | minor | Dead-arm policy unstated vs "every run counts" |
| AR-4 | minor | v2→v3 criteria diff unverifiable by a cold reviewer (hash-only freeze, untracked folder) — could-not-verify flag |
| LO-6 | nitpick | "Differential scoring" naming; V3 demotion is the real pass-probability driver |
| n2 | nitpick | Rule-free control catch of V2 unassigned between "new rule" and "docs-b rule" branches |
| AR-5 | nitpick | docs-b byte-identity re-verification not restated for round 3 |

## Verdict

**Worst severity: MAJOR (no blocker).** The delta's skeleton is sound and its factual base is solid — every carried tally checks out against the arm outputs, the new-rule status of the V1/V2 seeds is confirmed against `8a7ac65`, FX-B is clean and even biases against the instrument's own interest, the tripwire and no-resampling discipline survive, and the two FAILs remain honestly on the record. But it is not fit to route to build as written: FX-A would launch round 3 with a foreseeable treatment-only off-seed fire it was specifically designed to eliminate (its leak analysis contains a false claim); the pass conditions advertised as "mechanical" leave their load-bearing term undefined in the hands of the author-scorer with edge cases already demonstrated twice; V4's combined bar doesn't enforce the preservation property the position note claims for it; and the surviving V3 characterization ("~50% in both arms") misstates the measured per-arm record in the direction that flatters the demotion. All four majors are fixable in the delta without touching the owner's decisions (differential conditions, V3 demotion, n=3, fresh battery all stand) — fix FX-A's record shape, define "catch", add per-arm V4 floors or soften the position-note claim, and correct the ~50% wording to the true 1/4-T vs 3/4-K — then this instrument is fit to build.
