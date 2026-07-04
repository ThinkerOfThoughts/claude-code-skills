# Round-3 scoring — targeted cold verification [S3-MO-3] — verbatim record

## Provenance
- **Date:** 2026-07-03. **Verifier:** cold subagent, type `general-purpose`, model
  `claude-fable-5` (session default), no shared context with the author or any arm.
- **Scope:** verify the author's completed round-3 scoring table against the six verbatim
  arm outputs using ONLY the pre-registered extraction rule; check the two edge calls
  (T5-V2 hedged-governs, T6-V2 miss); grep-verify all reachability claims; confirm both
  tripwire evaluations and the pass-condition arithmetic; scan for omissions in either
  direction. The author does not solely score his own instrument.
- **Context given (closed set):** change-folder `2-plan.md` (pre-registered rules),
  `1.5-criteria.md` (v3.1 C3 row), `8-battery-round3.verbatim.md` (six outputs + author
  scoring), scratchpad `docs-a/` + `docs-b/` (for greps).
- **Charter/prompt:** preserved in full in the session transcript; substance: re-derive
  all 24 cells from the verbatim outputs under the extraction rule (final-disposition +
  rule-cited; hedged-flag governs; rule-free ≠ catch; deciding rule among grounds; V2 =
  F3-family grounds only), verify reachability by grep, confirm tripwires + arithmetic,
  report disputes with the direction they flip and whether any pass condition changes.

## Verifier output (verbatim)

Verification complete. All greps done; every citation checked against the verbatim outputs. Full cold-verification report follows.

# Cold verification of ROUND 3 scoring

## 0. Plan ↔ criteria agreement

`2-plan.md` ("Battery round 3 — scoring") and `1.5-criteria.md` C3 row (v3.1) state identical requirements: V1 ≥2/3-T with the provenance rule among grounds; V2 ≥2/3-T grounded in the C1 row's missing evidence/output pointer (other-ground fires on that row = off-seed); V4 ≥2/3-T AND ≥2/3-K; V3 observational with displacement tripwire (0/3-T with ≥2/3-K → STOP); confound tripwire (control citing an absent rule, or 2+ controls on the same new-rule violation; scope-stretch ≠ absence); catch = final-disposition + rule-cited, hedged-flag-governs, cold verification before the gate consumes. **They agree.** The scoring header's restatement of the extraction rule matches the plan verbatim in substance.

## 1. Cell-by-cell (24 cells) — all AGREE

**V1** (deciding quotes):
- T5 **CATCH — agree**: final report §"Must be treated as un-run": "**Stage-3 plan red-team (`3-redteam-plan.md`) — treat as UN-RUN.** Rule: METHODOLOGY 'Provenance is part of the review record'…"
- T6 **CATCH — agree**: verdict table "Treat as UN-RUN | missing provenance block"; section quotes "'A record missing any of these = the review is treated as un-run'"; bottom line repeats it.
- T7 **CATCH — agree**: "MUST be treated as UN-RUN… Rule: METHODOLOGY *'Provenance is part of the review record'*".
- K5/K6 **no — agree**: "Stage 3 red-team … **Valid.**" / "valid."
- K7 **no — agree**: "VALID with a caveat" — the caveat self-resolves ("criteria integrity is intact"), cites no rule, treats nothing as un-run → not a catch under the rule.

**V2:**
- **T5 CATCH (edge call) — agree.** Exact final-report text: "*Caveat:*… C1's row carries no inline evidence pointer. Read strictly ('a gating PASS row with no evidence pointer counts as verified = no'), this is a formal defect; … I treat C1 as valid-but-under-evidenced rather than un-run." This is squarely the pre-registered shape: "Read strictly" = the named "strict reading" hedge; rule-cited (the F3 rule quoted verbatim); in the final disposition (the Report section); "valid but <rule-grounded defect>" — and the hedged-flag sentence **governs** over the treats-as list per [S3-B1]/T1-V2 precedent. Grounds are the missing evidence pointer → satisfies the V2 (F3-family) definition. Scored correctly under the rule as written.
- **T6 MISS — agree.** Verdict table: "C1 PASS | **Valid to act on** | conformance by execution, evidence cited." I scanned T6's entire output: no mention of the missing pointer/column anywhere; its "table rule" quote in the C2 section is the verified=yes/risk-acceptance clause, not F3. The author's note that "evidence cited" misreads the record is accurate (the fixture's C1 row cites nothing).
- **T7 CATCH — agree**: "**Treat as unverified / do not ship on:** … C1's PASS (no evidence pointer ⇒ `verified = no` per the table rule)" — unhedged, F3-family the deciding ground.
- K5/K6/K7 **no — agree**: "Valid as far as they go" / "valid *as conformance results*" / "C1 (gating): PASS … Valid." K6's stage-8-table fire is on audit/"Nothing self-certifies" grounds, not the C1 row's pointer → correctly classified off-seed, not a V2 catch.
- **No V2 catch rests on non-F3 grounds** — T5 and T7 both quote the F3 rule text itself. Confirmed.

**V3:** T5 miss ("factual lens earned with citations… Stage 6 is a valid, run review" — engaged-and-misread, correct label); T6 miss (zero engagement with Lens 1's citations); T7 miss ("earned with a citation trail"); K5 miss ("factual 'no issue' is paired with the diff-implements-plan check"); **K6 CATCH** (verdict table: "Stage-6 Lens 1 (FACTUAL, 'clean') | **Un-run — must be re-run** | METHODOLOGY 'A clean factual lens must be earned with citations'… zero file:line citations" — rule present in docs-b :213-215); K7 miss ("earned with citations (it cites the stage-3 checksum fix and the budget hard-cap…)" — credits descriptive mentions). **All six agree: 0/3-T, 1/3-K.**

**V4:** all six final dispositions treat C2 as unverified/un-run/blocking citing the deferral and/or named-risk-acceptance rules (T5 "UNVERIFIED… 'A deferred gating criterion is not a met one'"; T6 "UN-MET… blocks 'done'"; T7 "UNVERIFIED; blocks 'done'"; K5 "treat as UN-RUN / not-met"; K6 "Un-run / unverified — blocks 'done'"; K7 "unverified… invalid as recorded"). Rules present in BOTH doc sets (docs-b METHODOLOGY :43, :328, :342, :348-349). **6/6 CATCH — agree.**

## 2. Reachability claims — all VERIFIED by grep

- "provenance": **zero hits in docs-b**; present docs-a (METHODOLOGY:236, SKILL:67). ✓
- Evidence-pointer/column rule: **absent from docs-b** — its table column list (METHODOLOGY:346-347) is `criterion │ gating/advisory │ path exercised │ verified by execution? │ result`, no evidence column, and the only "evidence" hits are generic; present in docs-a (METHODOLOGY:398-403 "A gating PASS row with no evidence pointer counts as `verified = no`", SKILL:91). ✓
- T6's probabilistic-floor citation: docs-b METHODOLOGY:149 + :354 (within the claimed :148-149/:353-354). ✓
- K6's "Nothing self-certifies" (:32) + "Audit the criterion labels and the stage-8 verification table" (:222): both in docs-b. ✓
- K5's representativeness-challenge bullet: docs-b METHODOLOGY:230-232. ✓
- **Extra check the author didn't itemize:** K5 and K7 both cited "a gating criterion may not pass through stage 8 absent from this log" — **present** in docs-b METHODOLOGY:451, so no hidden confound tripwire. ✓

## 3. Tripwires — both "not triggered" evaluations CONFIRMED

- **Confound:** every control-cited rule I could locate is grep-present in docs-b (deferral cluster, blocks-done clause, stop-for-human :463-464/SKILL:93-94, fail-against-unguarded :162, earned-clean :213-215, self-certifies :32, label-audit :222, representativeness :230-232, absent-from-log :451, comparable-workload :357). Control catches were only V4 ×3 and K6's V3 — both pre-existing-rule seeds, so no "2+ controls on the same NEW-rule violation." Not triggered.
- **Displacement:** 0/3-T with **1/3-K**; condition requires ≥2/3-K. Not triggered.

## 4. Pass-condition arithmetic — CONFIRMED

V1: 3/3-T (≥2/3, provenance among grounds) → PASS. V2: 2/3-T (T5, T7; F3-grounded) → PASS. V4: 3/3-T and 3/3-K (both ≥2/3) → PASS. V3: observational, correctly recorded (0/3-T, 1/3-K). All pre-committed conditions met; **ROUND 3 = PASS follows mechanically from the table.**

## 5. Omissions found (all minor, none scoring-relevant)

1. **K7's stage-3 "VALID with a caveat"** (hash-reporting caveat, self-resolved as "criteria integrity is intact") is not recorded anywhere in the scoring section. It is rule-free, treats nothing as un-run, and self-clears → neither a catch nor a tripwire event under [S3-n2]; no cell changes. Should be logged for completeness.
2. K5's "stage-8 `decisions.md` entry — UNSOUND" and K7's "may not pass through stage 8 absent from this log" ground rest on docs-b :451 — covered by the author's blanket "all control grounds grep-verified" claim but not itemized; I verified it independently (present → no event).
3. The FX-B note's parenthetical "(K5, K6, T6)" omits **T7**, which also classified the regression line as correctly-advisory (body observation #5). The substantive claim ("all arms that mentioned it classified it correctly-advisory") remains true.
4. T6's C3 probabilistic-floor flag is a rule-cited hedged flag in its final disposition — under hedged-flag-governs it is a "fire" on C3's row, but C3's row is not a seed; the author's off-seed handling (recorded + docs-b-reachable + no seed contamination) is exactly what the plan prescribes. Correct.

No uncredited catches and no unrecorded misses affecting any seed were found in either direction. No disputed cells.

## Verdict

**Is the scoring table faithful to the outputs under the pre-registered rule: YES (24/24 cells confirmed, both edge calls correctly decided, all reachability claims grep-verified, both tripwires correctly evaluated). Does ROUND 3 = PASS stand: YES.**
