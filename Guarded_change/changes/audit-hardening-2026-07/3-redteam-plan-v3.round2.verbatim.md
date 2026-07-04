# Stage-3 red-team of the v3 re-plan delta (ROUND 2, post-revision) — verbatim record

## Provenance
- **Date:** 2026-07-03. **Reviewer:** fresh cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author or the round-1 reviewer.
- **Scope:** Task A — verify all 15 round-1 [S3-*] findings resolved; Task B — fresh attack
  on the revised delta. Owner decisions (V3 demotion, n=3, re-plan) out of scope.
- **Context given (closed set):** change folder {2-plan.md, 1.5-criteria.md,
  1.5-criteria.v2-frozen.md (+ hash-check duty vs `c29dfada…`), 3-redteam-plan-v3.verbatim.md,
  8-battery-round1/2.verbatim.md, decisions.md, fixtures/review-record/} + amended
  METHODOLOGY.md. Reviewer-reported sha256s at the top of the verbatim output; author
  spot-check: METHODOLOGY `35a6798d…` and fixture hashes match prior check reports; the
  reviewer independently confirmed the v2-frozen reconstruction hash equals the recorded
  freeze hash.
- **Charter/prompt given (verbatim):**

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your review.

This is a STAGE-3 plan red-team, ROUND 2, of a revised RE-PLAN DELTA inside an ongoing guarded-change run. Background: the run amends the guarded-change skill's own docs (9 additive rule fixes, built and code-reviewed). One criterion — C3, a replay A/B testing whether the amended docs change reviewer behavior — failed its original bar twice; the owner chose "re-plan the instrument"; a v3 delta was drafted; a round-1 cold review found it MAJOR (4 majors: FX-A non-conformant under the amended rules; V4's combined bar not enforcing treatment-side firing; a "~50% both arms" misstatement of the true 1/4-T vs 3/4-K V3 record; "catch" undefined with the author as sole scorer) plus 8 minors and 3 nitpicks. The delta has now been revised to address all 15, tagged [S3-*] inline.

Your tasks:
**Task A — verify each round-1 finding is resolved in the revised text.** The round-1 review is at `3-redteam-plan-v3.verbatim.md` (its ranked findings table near the end lists F-2/LO-1, LO-2, F-3, LO-3 as majors; LO-4, LO-5, F-4, MO-1, MO-4, AR-2, AR-3, AR-4 as minors; LO-6, n2, AR-5 as nitpicks). For each: state RESOLVED (cite where) or NOT RESOLVED (cite what's missing).
**Task B — fresh attack on the REVISED delta** (the "Plan v3 addendum" section of `2-plan.md`, the C3 row + position note of `1.5-criteria.md`, and the erratum appended to `8-battery-round2.verbatim.md`): new contradictions the revision introduced, remaining ambiguity in the catch-extraction rule or pass conditions, coherence of the FX-A 6b-harness-check design and its residual adjudication, coverage gaps. Do not re-litigate owner decisions (the V3 demotion, n=3, re-plan itself) or the 9 rule fixes.

## Context (closed set — read these, nothing else)

All under /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/ unless noted:
1. `2-plan.md` — the revised "Plan v3 addendum" (the artifact under review; plan-v2 body is background).
2. `1.5-criteria.md` — revised C3 row + position note; also `1.5-criteria.v2-frozen.md` (the reconstructed frozen v2 — verify its sha256 equals the freeze hash `c29dfada53cc7bdebdcf6acfbfc26cb8c7d892dc976a55205e00aa7d537f084d` recorded in decisions.md, then diff it against the current file to confirm ONLY the title, position note, C3 row, and freeze note changed).
3. `3-redteam-plan-v3.verbatim.md` — the round-1 review (Task A's checklist).
4. `8-battery-round1.verbatim.md`, `8-battery-round2.verbatim.md` (incl. the new erratum at the end) — the evidence base.
5. `decisions.md` — gate log.
6. `fixtures/review-record/` — current fixture (FX-A/FX-B not yet built — the delta specs them).
7. `/home/zero/Desktop/claude-code-skills/Guarded_change/METHODOLOGY.md` — amended methodology (rule inventory).

## Charter

Four lenses: 1. FACTUAL — revised-text claims vs the record; cite file:line for everything you check; a clean factual verdict with zero citations is treated as an un-run review. 2. LOGICAL — reasoning flaws in the revised design. 3. MISSED OPPORTUNITY — cheap improvements left on the table. 4. UNSTATED ASSUMPTIONS & RISKS.

Discipline: cite a line or a concrete failure scenario for every finding; rank every finding blocker/major/minor/nitpick; flag anything you could not verify rather than silently accepting it; "no issue found" per lens is allowed and expected when true.

Criteria-coverage challenge (required section): name behaviors the revised instrument could get wrong that NO pass condition or tripwire observes — an explicit "none found" counts.

End with: worst severity + a one-paragraph verdict on whether the revised delta is fit to route to build.
```

## Reviewer output (verbatim)

# Cold review — STAGE-3 round 2 of the revised C3-instrument-v2 delta

## Context-file hashes (sha256, computed by me)

| File | sha256 |
|---|---|
| `2-plan.md` | `d8d67f3260394eef806c315400086c39d69ff5391942b3452e60768b4df6857f` |
| `1.5-criteria.md` | `814d3d45749c379e79cea77908485c9d31930ec55900a9fa1086dc957b9eb13d` |
| `1.5-criteria.v2-frozen.md` | `c29dfada53cc7bdebdcf6acfbfc26cb8c7d892dc976a55205e00aa7d537f084d` |
| `3-redteam-plan-v3.verbatim.md` | `899d6915819c9c8dff1aed19c1632d2505378b1e305bf9190076c03af63f77a6` |
| `8-battery-round1.verbatim.md` | `8f79c481dcf1e69d55281af90bc8a920e0a9487d25ff005004b8b9edbf5826c2` |
| `8-battery-round2.verbatim.md` | `96e45a41d0e3e94372e3a89dd2f2b418d5bdf4452c58e1a62876cf4aea38efc8` |
| `decisions.md` | `158a33f10727347be2c472956d469124f92f84660e3d20b631a322c0bcd069a0` |
| `METHODOLOGY.md` (amended) | `35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3` |
| fixture `1-spec.md` | `baed3ea40a94316f5fbbe7bf690160ea26f0a1a87bf4d3f5c70047923a8f7a7d` |
| fixture `1.5-criteria.md` | `6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d` |
| fixture `2-plan.md` | `9b6954b521d5c62790df237c5ab8c79736335a962685f97c8253107e00558ca3` |
| fixture `3-redteam-plan.md` | `8613c4ea4adc3ad5f02df52c9b03ec54f2aac9f61e9781eba51e153389d19903` |
| fixture `6-redteam-code.md` | `43fb7b222388956c7cf698d73e784a3e0a0985d71f7937c1b35cd0f20fd4ec61` |
| fixture `8-harness.md` | `ca69d09443f50260b623a610a2e4eb1c3fce628534ae448d51414787e0b2263c` |
| fixture `decisions.md` | `b1626329045f28a1e870c5896fb364d28a7c5c352e37e5859b30ac8216e3520d` |

**Freeze verification (charter-mandated):** `sha256(1.5-criteria.v2-frozen.md)` = `c29dfada53cc…7f084d`, byte-equal to the freeze hash recorded at `decisions.md:43`. I then diffed it against the current `1.5-criteria.md`: the only hunks are the title line (1.5:1), the position note (1.5:3–16), the C3 row (1.5:24), and the freeze note (1.5:30–34). The header claim "all other rows unchanged from frozen v2" (1.5-criteria.md:1) is **cold-verified TRUE** — C1/C2/C4–C7 are byte-identical to the frozen v2.

**Mechanical checks beyond reading:** `git show 8a7ac65` line counts 467/102 (matches decisions.md:8); grep of `8a7ac65:METHODOLOGY.md` for `provenance|evidence pointer/column|sha256|unreviewed check|targeted cold check|charter core` → **zero hits** (differential premise re-confirmed, and load-bearing for finding B5 below); pre-existing rules confirmed at docs-b:162 (interleaving fail-against-unguarded), :215 (earned-clean), :43 (deferral), :357 (comparable workload). Change folder is still untracked (`?? changes/audit-hardening-2026-07/`) — the verbatim-copy freeze discipline is now the only auditability mechanism, and it works.

**Not verifiable from my closed set:** the fixture-check verbatim files (`6-fixture-check-*.verbatim.md`) and SKILL.md were not in scope; claims about D1's exact charter bullet list are taken from `decisions.md:60-66` as logged, not from the primary record. Flagged, not assumed.

---

## Task A — round-1 findings, one by one

| # (sev) | Verdict | Where / what |
|---|---|---|
| **F-2/LO-1 (major)** | **RESOLVED** | FX-A redesigned as a provenance-complete in-fiction record `6b-harness-check.md` (2-plan.md:153–163): embedded pre-change-duties charter + task addition quoted as such, exact context list, reviewer-reported hashes, agent type/model, verbatim output — and fail-against-unguarded for **both** guards (C3 dedup `c3-unguarded.log` stored_copies=2; C1 retry `c1-unguarded.log`), directly answering F-2's "C1's mock also guards a fix" point. The conformance-vs-leak bind is now confronted head-on with a pre-committed residual adjudication mirroring the D1/V3 residual (2-plan.md:164–168) — exactly the design LO-1 sketched. Criteria row mirrors it (1.5:24). Residual coherence gaps → B2, B3 below. |
| **LO-2 (major)** | **RESOLVED** | Per-arm V4 floors "≥2/3 treatment AND ≥2/3 control" (2-plan.md:208–210); position note now claims only what the bar enforces ("the treatment floor is what tests firing THROUGH the amended docs", 1.5:6–8); the control floor doubles as the competence check, closing round-1 coverage gap #2. MO-2 folded. |
| **F-3 (major)** | **RESOLVED** | "~50% both arms" is gone from both live texts; replaced by "1/4-treatment vs 3/4-control (pooled 4/8, … 3/4 on the verbose round-1 lens, 1/4 on the terse round-2 lens)" (2-plan.md:140–142; 1.5:9–12). I re-verified per-arm and per-wording numbers against the scoring tables (r1:406 — T 1/2, K 2/2; r2:297 — T 0/2, K 1/2): all correct. The asymmetry now feeds a mechanical tripwire rather than being flattened. Residual: r2:324's "~50% overall" stands unerratum'd → B10. |
| **LO-3 (major)** | **RESOLVED** | Pre-registered extraction rule (2-plan.md:188–196): final-disposition locus, rule-citation requirement, hedged-flag clause, rule-free exclusion, among-grounds multi-rule test, every edge call quoted verbatim — and the author no longer solely scores: the completed table gets a targeted cold verification before the gate consumes it (2-plan.md:227–229; 1.5:24). MO-3 folded. Residual: an internal contradiction between the rule's two sentences on the precedented "valid but…" case → B1. |
| **LO-4 (minor)** | **RESOLVED** | All four collisions assigned: pass+defect-fire precedence (2-plan.md:223–226); mixed-grounds classifier = unreachable-from-docs-b (219–221); "scope-stretch is not absence" with the exact docs-b:162 example (215–218); T3's proxy-path leg classified legitimate-reading, no scoring impact (221–223). |
| **LO-5 (minor)** | **RESOLVED** | V1 now carries V2's carve-out shape: docs-b-present-rule control catch = recorded evidence against F1's marginal value, not a fail; absent rule = tripwire (2-plan.md:202–205; 1.5:24). The contradiction with the carried plan-v2 clause dissolves ("plan-v2 clause stands", :204). |
| **F-4 (minor)** | **RESOLVED** | Erratum appended to the round-2 record (r2:347–357): T3's fire reclassified "new-rule-involved, mixed-grounds, treatment-only", differential claim weakened, append-only respected, erratum governs; the addendum's carried summary states mixed-grounds (2-plan.md:141–142); round-3 classifier prevents recurrence (219–221). |
| **MO-1 (minor)** | **RESOLVED** | Seed isolation explicitly REJECTED with logged rationale + kept as the standing future-instrument option (2-plan.md:237–241). Round 1 asked at minimum for a logged rejection. |
| **MO-4 (minor)** | **RESOLVED** | Mechanical displacement tripwire: V3 0/3-T with ≥2/3-K → STOP/investigate (2-plan.md:211–213; 1.5:13–14). Residual: post-investigation routes unassigned → B4. |
| **AR-2 (minor)** | **RESOLVED** | F2 checker handed BOTH doc sets with the explicit both-rule-set legality duty (2-plan.md:173–176). Residual: that duty now collides with the by-design 6b residual → B2. |
| **AR-3 (minor)** | **RESOLVED** | Dead-arm policy: no-final-output → kill + respawn fresh, logged, nothing discarded; a final-output arm counts, period (2-plan.md:185–187; referenced in 1.5:24). |
| **AR-4 (minor)** | **RESOLVED** | Freeze-auditability section (2-plan.md:243–250): v2 reconstruction saved, hash-verified by me against decisions.md:43 (exact match), diff confirms only the four declared regions changed; v3 re-freeze commits to hash + verbatim copy (MO-5 folded). |
| **LO-6 (nitpick)** | **RESOLVED** | Verdict text must carry "the V3 demotion (owner-authorized) — not the scoring change — is the largest single driver of the round-3 pass probability" (2-plan.md:230–233; 1.5:24). |
| **n2 (nitpick)** | **RESOLVED** | Rule-free flag = not a catch; from a control, recorded, neither catch nor tripwire event (2-plan.md:192–193). Residual evidentiary-weight gap → coverage challenge #2. |
| **AR-5 (nitpick)** | **RESOLVED** | docs-b re-verified byte-identical to `git show 8a7ac65` at launch (2-plan.md:182–184). |

**15/15 resolved.** The header claim "all 15 findings addressed inline" (2-plan.md:150–151) is accurate, and every [S3-*] tag resolves to real text.

---

## Task B — fresh attack on the revised delta

### Lens 1 — FACTUAL

Carried tallies re-verified against the raw scoring tables (r1:402–407; r2:293–298; erratum r2:347–357): V1 4/4-T vs 0/4-K, V2 3/4-T vs 0/4-K, V4 8/8, V3 1/4-T vs 3/4-K with the 3/4→1/4 per-wording split, T3's fire mixed-grounds treatment-only, tripwire never triggered — **all correct**. The [FC1-note] "identical in both arms" claim checks out against the single-template round-1 prompt (r1:17–24). One factual defect found:

**B5 (minor). The 6b charter's sha256 instruction is mislabeled a "pre-change duty."** 2-plan.md:156–158 describes the charter as "containing ONLY pre-change duties verbatim-in-substance (cite-or-flag, rank findings, report context-file sha256s — the D1 compromise…)". My grep of `8a7ac65:METHODOLOGY.md` for "sha256" returns **zero hits** — sha256-reporting is new-rule-shaped (amended F1 element (v), METHODOLOGY.md:240–241), and D1's own log entry lists it *separately* from the pre-change bullets (decisions.md:62–63). The operative guard ("NO amended-rule text") still holds — an instruction is not rule text, and the precedent is empirically clean (the round-1/2 fixture carried the same instruction; 0/4 controls fired on V1) — so this is a wording inaccuracy, not a design break. But in a delta whose round-1 review majored on a false leak-analysis claim, the leak-surface description should be exact: call it "pre-change duties plus the D1-precedented sha256 instruction."

### Lens 2 — LOGICAL

**B1 (minor). The catch-extraction rule contradicts itself on its own precedented edge case.** Sentence 1: caught iff the final disposition "treats that artifact/row as un-run / unverified / invalid / blocking" (2-plan.md:189–191). Sentence 2: "A hedged flag ('strict reading', 'valid but…') counts iff it is rule-cited AND appears in the final disposition" (191–193). Concrete failure: T1-round-1's V2 — final summary lists C1 as "valid but under-evidenced," rule-cited (r1:119, scored CATCH at r1:405). Sentence 1 says NOT a catch (the row is treated as *valid*); sentence 2 says catch. The precedented case the rule exists to decide sits exactly in the crack between the two sentences, and V2's ≥2/3 bar can turn on one such call. Mitigated by verbatim edge-call recording + cold verification, but the rule was supposed to remove discretion, not relocate it. One precedence sentence fixes it.

**B2 (minor). The F2 checker's charter collides with the by-design 6b residual.** The checker's duty is "verify the fixture is legal under both rule sets except at the seeds" (2-plan.md:174–176). But 6b is *deliberately* not fully legal under docs-a: its embedded charter cannot be amended-charter-core verbatim (the provenance bullet is an unconditional core bullet, METHODOLOGY.md:236–250; the delta itself premises this at 2-plan.md:164–166), and 6b is not a seed. A diligent checker, as chartered, **must** flag exactly this residual as an off-seed illegality → a predictable spurious major at the F2 gate. This run's history makes that expensive: the fixture-check gate already fired the iteration cap once on this artifact class (decisions.md:104–113), and a further fixture-check major was pre-routed "back to the owner" (decisions.md:145–146) — an un-instructed checker predictably burns an owner escalation on a pre-accepted residual. Fix: one quoted task-specific sentence in the checker's charter naming the residual as pre-committed (legal under F1's quoted-as-such clause; this is not an A/B arm).

**B3 (minor). The residual adjudication's wording is narrower than the residual.** It covers "a treatment fire claiming the 6b record is provenance-deficient" (2-plan.md:166–168). A treatment reviewer can reach the same un-run verdict via a sibling ground: *the 6b charter is not the amended charter core verbatim* — missing the provenance bullet, and (as spec'd at 2-plan.md:157–158, which lists only cite-or-flag / rank / sha256s) also missing pre-change core bullets the fixture's own 6-redteam-code.md charter carries per D1 (earned-clean-factual, spot-verify, label-audit, flag-unverifiable). A charter-core fire not phrased as "provenance-deficient" falls into the off-seed machinery, whose precedence clause pre-commits only for **both-rule-set** defects (2-plan.md:223–226) — an amended-only, non-residual-worded fire on 6b has no pre-assigned disposition. Cheap fix, two parts: (i) broaden the residual to "any fire grounded in the 6b record's or its embedded charter's non-conformance to amended-F1"; (ii) spec 6b's charter to carry the full D1 bullet set so the *only* amended-rule gap left is the provenance bullet itself.

**B4 (minor). The displacement tripwire has no post-investigation routes.** The confound tripwire carries a resolution path (R2-2c: "not a confound → logged, protocol resumes, results standing", 2-plan.md:83–85, imported "unchanged" at :214). The new [S3-MO-4] tripwire says only "STOP, investigate, no disposition until resolved" (2-plan.md:211–213). If the investigation *confirms* displacement, there is no named route — and because V3 carries no bar, nothing mechanical converts a confirmed displacement signal into a battery outcome; author discretion returns at exactly the point the delta worked to eliminate it. If *refuted*, resumption is unstated. Two sentences (confirmed → stage-8 major → human; refuted → resolution logged, protocol resumes) fix it.

**B6 (minor). Stale n=2 cross-references now contradict the v3 instrument.** Frozen C7 requires the final report to carry "C3's n=2 + codification caveats" (1.5-criteria.md:28), and plan-v2's Reporting duties say "C3's n=2 limitation … verbatim" (2-plan.md:126) — while the addendum's verdict text carries n=3 (2-plan.md:230–231) and "Everything else in plan v2 stands" (2-plan.md:135–136). A cold consumer inherits both an n=2 duty and an n=3 duty for the same criterion. F4's own legal-edit mechanism (or the v3 re-freeze already happening) makes this cheap to fix; as written it is a fresh cross-document contradiction introduced by the n change.

**B13 (minor). Two under-specified spots in the 6b build spec invite fresh fixture defects.** (i) The task addition says "check the **four** harness scripts represent the criteria's governed paths" (2-plan.md:159–160) — but C2 is seeded as *deferred*: no C2 script exists in-fiction. The count works only under one enumeration ({C1 mock, C3 mock, C4 line-count, regression dry-run}), which the delta never states; a wrong or ambiguous in-fiction count is a citable internal inconsistency under BOTH rule sets — a fresh K4-class off-seed magnet, the exact defect class round 2's lesson (r2:313–314) was about. (ii) 6b introduces a C1-adjacent output pointer (`c1-unguarded.log`) into a record whose V2 seed is the *absence* of any C1 output location (per the R2-10b design at 2-plan.md:44–46, V2 is "the only gating row with no output location anywhere"); strictly the seed survives (the unguarded log evidences the pre-change failure, not the PASS row), but the "V1–V4 intact and sole-per-artifact" duty (2-plan.md:176) should explicitly instruct the F2 checker to confirm V2's salience is undiluted. Both are one-line pins in the delta.

### Lens 3 — MISSED OPPORTUNITY

**B8 (nitpick).** Pin the round-3 model id. Rounds 1–2 pinned `claude-opus-4-8` (r1:4–5, r2:4–5); the delta says "opus" / "opus, the production model" (2-plan.md:179; 1.5:24). If the production model drifts, the carried cross-round evidence quietly becomes cross-model. One word: "same model as rounds 1–2."

**B9 (nitpick).** The superseded v2 C3 measurement block (2-plan.md:38–97) carries no inline marker pointing to the addendum; the criteria row disambiguates the oracle ("per the plan-v3 protocol", 1.5:24), but a reader of 2-plan.md meets a full, live-looking 2+2/2-of-2 protocol ninety lines before learning it is dead. One pointer line at the top of the old block.

**B10 (nitpick).** Erratum asymmetry: F-4 got an in-file erratum in the round-2 record; F-3 did not — the cumulative table's "~50% overall detection" framing (r2:324) is the one surviving flattering-pooled statement a future cold reader might quote. The erratum vehicle already exists in that file; one added sentence closes it.

**B7 (nitpick).** Identifier drift: tags `[S3-F3]`/`[S3-F4]` (2-plan.md:142) vs `[S3-F-3]`/`[S3-F-4]` (2-plan.md:219; 1.5:7); version labels "Plan v3 addendum" (2-plan.md:134) vs "v3.1" (1.5:6; r2:356) vs criteria header "v3" (1.5:1). The freeze audit trail should name ONE identifier for what re-freezes. Related: the position note's juxtaposition of "1/4 treatment vs 3/4 control" with "3/4 on the verbose round-1 lens, 1/4 on the terse round-2 lens" (1.5:10–12) is factually correct but the mirrored numbers invite misparsing; a "per-round, both arms pooled" qualifier would harden it.

### Lens 4 — UNSTATED ASSUMPTIONS & RISKS

**B11 (nitpick).** "Bars are calibrated to attention noise" (2-plan.md:239–240) is asserted, not computed: at the observed V2-T rate (3/4), P(≥2/3) ≈ 0.84, so the battery retains roughly a one-in-five chance of consuming its single re-run on pure attention noise with *nothing to fix*. The route exists (the one logged re-run; the seed-isolation clause even anticipates "fails on attention grounds", 2-plan.md:240–241), but the protocol should say explicitly that a no-defect diagnosis still consumes the single re-run — "diagnosed-fix" implies a fix, and the retry's F2-check leg (2-plan.md:234–235) has no object when nothing changed.

**B12 (nitpick).** 6b adds a ninth in-fiction artifact: reading load rises while two off-seed fire-attractors are removed. The net effect on per-seed attention is assumed neutral-to-favorable but untested; the ≥2/3 floors absorb one miss per seed, which is the mitigation. Named as an assumption, not a defect.

---

## Criteria-coverage challenge (required)

Behaviors the revised instrument could get wrong that **no pass condition or tripwire observes**:

1. **Cumulative cross-round V3 asymmetry.** The tripwire fires only on round-3 0/3-T; a 1/3-T + 3/3-K round 3 (cumulative T 2/7 vs K 6/7) triggers nothing. Deliberately observational per the owner demotion and carried per-arm into the verdict — but no threshold ever observes the pooled asymmetry.
2. **Rule-free control flags of a seed.** Assigned "neither catch nor tripwire" [S3-n2] — so even 3/3 controls rule-free-flagging the stage-3 record (form-taught by what are now TWO provenance-complete sibling exemplars once 6b exists) triggers nothing and carries no pre-assigned evidentiary weight against F1's marginal value; only rule-*citing* control catches do (2-plan.md:202–205).
3. **An arm output with no identifiable summary/bottom-line.** It "counts, period" (2-plan.md:187), yet the final-disposition extraction rule can award it zero catches on form alone; nothing distinguishes formatting-zero from review-quality-zero. (All 8 prior arms produced bottom lines; low likelihood.)
4. **Scorer-vs-verifier disagreement.** The cold verification observes misscoring, but no route is named for an unresolved edge-call dispute (F5's contest mechanism presumably applies by default; unnamed here).
5. **Soundness of the diagnosis itself on a miss.** The single re-run is granted whether or not the diagnosed defect is real; nothing observes the diagnosis (B11).

At the seed level proper, no gap found: V1/V2/V4 are barred, V3 is tripwired at the collapse end, and the confound tripwire covers both the absent-rule and 2+-same-new-rule edges.

---

## Ranked findings

| # | Severity | Finding |
|---|---|---|
| B1 | minor | Catch-extraction rule's two sentences contradict on the precedented "valid but…" case |
| B2 | minor | F2 checker's both-rule-set-legality charter collides with the by-design 6b residual → predictable spurious bounce at a cap-sensitive gate |
| B3 | minor | Residual adjudication worded narrower than the residual (charter-core fires on non-provenance grounds unassigned); 6b charter bullet set thinner than D1's |
| B4 | minor | Displacement tripwire lacks post-investigation routes (confirmed/refuted) |
| B5 | minor | sha256 instruction mislabeled a "pre-change duty" (zero sha256 hits in docs-b — my grep) |
| B6 | minor | Frozen C7 ("n=2") + plan-v2 reporting duty now contradict the n=3 instrument |
| B13 | minor | 6b build spec: "four harness scripts" unenumerated vs C2-deferred seed; `c1-unguarded.log` vs V2's only-row-with-no-output-location design not explicitly covered by the F2 check's seed-intact duty |
| B7 | nitpick | Tag hyphenation + v3/v3.1 version-label drift; mirrored-numbers phrasing in the position note |
| B8 | nitpick | Round-3 model id unpinned ("opus" vs rounds-1/2 `claude-opus-4-8`) |
| B9 | nitpick | Superseded v2 C3 block carries no inline pointer to the addendum |
| B10 | nitpick | r2 cumulative "~50% overall" left unerratum'd while the same file's erratum vehicle was used for F-4 |
| B11 | nitpick | Attention-noise calibration informal; no-defect miss still consumes the re-run, unstated |
| B12 | nitpick | 6b's net attention-economy effect assumed, untested (floors mitigate) |

---

## Verdict

**Worst severity: MINOR (no blocker, no major).** All 15 round-1 findings are genuinely resolved in the revised text — I verified each against its landed location, re-verified the carried tallies against the raw arm outputs, re-confirmed the differential premise by my own grep of `8a7ac65`, and cold-verified the freeze reconstruction (hash exact-match; diff confined to the four declared regions). The four round-1 majors are not just patched but structurally answered: FX-A is now the provenance-complete D1-mirroring design with both guards' fail-against-unguarded and a pre-committed residual; V4 has per-arm floors; the V3 record is stated per-arm and per-wording everywhere it survives; "catch" has a pre-registered extraction rule with a second, cold scorer. What remains is a ring of edge-condition gaps the revision itself created — an internal contradiction in the extraction rule on exactly its precedented edge case (B1), a foreseeable collision between the F2 checker's charter and the by-design 6b residual at a gate where the iteration cap is already primed (B2/B3), unrouted displacement-tripwire outcomes (B4), and stale n=2 cross-references (B6) — every one of them a one-to-three-sentence in-place fix that touches no owner decision. Per the severity model, minor → fix in place → proceed: **the revised delta is fit to route to build once these minors are folded in.**
