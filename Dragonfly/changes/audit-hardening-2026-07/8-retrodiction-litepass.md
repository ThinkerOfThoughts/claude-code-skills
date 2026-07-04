# 8-retrodiction-litepass.md — round-1 lite cold pass of the C8 retrodiction record

**What this is:** the guarded-change-LITE cold review (single pass, stage-3/6 charter core:
four lenses + evidence discipline) of `8-retrodiction.md` as required by frozen criterion C8
("scored only after the retrodiction record itself passes a guarded-change-lite cold review").
This is the ROUND-1 pass. **Verdict: MAJOR — the C8 PASS claim did not survive as written.**
`8-retrodiction.md` was subsequently REVISED in place (round 2; its header points here);
the round-2 lite pass is recorded in `8-retrodiction-litepass-round2.md`.

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model `claude-fable-5`, no shared context.
- **Run:** 2026-07-04, 15:45–15:54 UTC (session `723b134a…`, task `adb0737a39a51bc81`).
- **Form:** guarded-change-lite (single cold pass; intent + checkable criterion in the charter
  below; closed context set enumerated in the charter; reviewer self-reported sha256s).
- **Document under review:** `8-retrodiction.md` at its ROUND-1 state, sha256
  `17d87d5dbb84c0f13e39ac415b141fb562b7cd44ce55aff1785d543917a2e8c5`. ⚠️ That hash is
  deliberately STALE relative to the current file — the round-2 revision (same filename,
  in place) was made in response to this review. The round-1 content this review quotes is
  recoverable from the transcript if ever needed; the findings below quote its defects.
- **Transport note:** this record was written AFTER the fact. The pass ran and its verdict was
  consumed (revision executed) on 2026-07-04, but a usage pause hit before this file was
  written; the charter and reviewer output below were recovered VERBATIM from the session
  transcript (`~/.claude/projects/-home-zero-Desktop-companion-emergence/`
  `723b134a-ce22-49fd-bc1a-355927741422/subagents/agent-adb0737a39a51bc81.jsonl`) on resume,
  same day. No edits beyond this framing header. The gap is recorded in `decisions.md`
  ("Stage 8 IN PROGRESS — PAUSED").

## Disposition (recorded in decisions.md)

MAJOR + 3 minors + 3 nitpicks → `8-retrodiction.md` revised in place (round 2): S1-O18/S1-O21
explicitly adjudicated as non-laps with citations (S1 = 0 now EARNED, not asserted); the false
grep claim corrected; the (iv) "honored in substance" aside corrected against decisions.md:53;
the (v) counterfactual dropped and the derivation grounded at observation-ledger.md:292-294;
the nitpicks addressed (framing notes added). C8 stays UNSCORED until the round-2 lite pass.

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a GUARDED-CHANGE-LITE cold pass (single review pass, guarded-change's stage-3/6 charter core: four lenses + evidence discipline) of ONE document: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/8-retrodiction.md

INTENT (one line): the document claims to execute five pre-registered "retrodiction" sub-checks — replaying five newly-built dragonfly rules against a pinned real-hunt record — and reports all five PASS.

CRITERION (checkable): every citation in 8-retrodiction.md resolves in the pinned record at the cited lines and says what the document claims; every adjudication follows from the cited text rather than narrative assertion; every pre-registered expected outcome (as frozen in criterion C8 of 1.5-criteria.md) is genuinely met as stated — including the outcomes' own guard-rails (sub-check (i): S2 count ∈ {1,2} with the 1-vs-2 choice actually justified, S1 = 0, no laps outside the O16/O17 inventory; (ii): the anchor is really "the moment S1-O15 was recorded" and the then-live leading account is correctly identified from the record; (iii): the named missing element is genuinely absent from the record; (iv): the infeasibility-class citations exist and no formal inversion entry exists; (v): the shared assumption is genuinely stated/derivable at the anchor point); and no sub-check consumes evidence outside the pinned fixture set.

Four lenses: FACTUAL (spot-verify EVERY line-number citation into the pinned files — quote what is actually there), LOGICAL (does each adjudication follow? is any pass vacuous or circular — e.g. does the document assume the rule fired because the audit said it should?), MISSED OPPORTUNITY (a cheap check the document skipped), UNSTATED ASSUMPTIONS (what is taken for granted). Discipline: cite file:line for every claim you verify or dispute; rank findings blocker/major/minor/nitpick; "no issue found" per lens is allowed when true; a clean verdict with zero citations = un-run review.

Context (closed set — read ONLY these):
- The document under review: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/8-retrodiction.md
- The pinned record it cites: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/fixtures/hunt-record/{decisions.md, hypotheses.md, CONTEXT-BLOAT-HUNT.md, observation-ledger.md, symptom-ledger.md}
- The frozen criteria with the pre-registered outcomes: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/1.5-criteria.md (criterion C8)
- The built rules being replayed: /home/zero/Desktop/claude-code-skills/Dragonfly/METHODOLOGY.md (stages 1, 6, 7, the characterized block, the coverage sweep)
- The audit (for the precedents the pre-registrations reference): /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/0-audit-findings.md

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, per-sub-check verification with quotes, lenses, findings). End with: one-line verdict — worst severity + whether the C8 PASS claim survives (survives / does not survive).
```

---

## Reviewer output (verbatim)

# Cold review — 8-retrodiction.md (guarded-change-lite pass, four lenses)

## Context-file hashes (sha256, computed by reviewer)

```
17d87d5dbb84c0f13e39ac415b141fb562b7cd44ce55aff1785d543917a2e8c5  8-retrodiction.md (document under review)
0ba8cfc59f3fd0b63f3b0e5b0e1f282ee87b206d6ff8bc20b3c4591cbc00e130  1.5-criteria.md
f753d7fcf809a0303ee91dbeb85cbba327f5c01e0d753cde5aaecc98dbde5cbc  0-audit-findings.md
04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065  METHODOLOGY.md
a4c2addadfb78c3fe419222a52caf51218330e7d7b00ca7ec2e342dc8023606a  fixtures/hunt-record/decisions.md
fcfcd687929cd1f846309f03fd093c030c76c4c30fe9cf78ba275b22ec0586bc  fixtures/hunt-record/hypotheses.md
46ae8d4f0c9afd7793c041a944e144dc06d71bf183136ae1be78e499d46cb98f  fixtures/hunt-record/CONTEXT-BLOAT-HUNT.md
6459716bedf8c614416b1a64db2031a0eb3f33891ad25925521a1eab29727925  fixtures/hunt-record/observation-ledger.md
2d9d16ff61ece109aa0e490debbf8d7ea0b2b7189935ad6f10dc366e28fe41c6  fixtures/hunt-record/symptom-ledger.md
```

Note: the document's own quoted sha for 1.5-criteria.md (`0ba8cfc5…00e130`, 8-retrodiction.md:6-7) matches my computed hash. The fixture-pinning verification itself is delegated to 8-harness.md (outside my closed set) — not checked here.

## Per-sub-check verification

### (i) D-3 cycle count — expected outcome NOT genuinely established

**Rule quote verified:** METHODOLOGY.md:182-183 — "A **cycle** = one discriminating test **run and recorded** — a completed stage-4→5 lap"; per-thread counting at METHODOLOGY.md:186-188. Matches the document's statement.

**Citations that verify:**
- decisions.md:28 — "Reproduce-on-demand (O16)" present, as cited (doc cites :28-29). ✓
- hypotheses.md:31 — "Confirm: replay shows detailed-06-19 NONE in top-5, confab at rank 2 (O16); toggle to relevance" — exact; the O17 half continues at :32 ("ranking surfaces the real memory at rank 1 and drops the confab (O17)"). ✓
- decisions.md:26 — "one cold red-team pass each" (doc cites :25-26). ✓
- decisions.md:95-96 — "Awaiting user go/no-go" spans exactly those lines. ✓
- decisions.md:103 — "Spec updated; still awaiting go/no-go." ✓
- decisions.md:68, :59, :75, :78-81 — S1-O7, S1-O13, "S1 stage 2 — new observation + archaeology", the S1-O16 archaeology — all present at the cited lines. ✓
- The 2-not-1 adjudication is genuinely justified from the definition's unit (two artifacts, two recorded observations, two confirm legs) and considers the alternative. ✓

**The failure:** the document claims S1's designed test "was **never run**" (8-retrodiction.md:39-41) and "the only run-and-recorded tests in the record are O16/O17" (8-retrodiction.md:48-49, "walked every decisions.md entry"). Both claims are contradicted by the pinned record:

- decisions.md:104 — "**S1 → guarded-change ENTERED (user "go", 2026-07-02)** | — | full guarded-change under…" — the "awaiting go/no-go" state the document cites at :103 is superseded by the *very next entry* in the same pinned file. The document stops reading at :103.
- observation-ledger.md:360-362 — "**[S1-O18]** SMOKE ANCHOR RUN #1 (SPENT TOKENS — real claude-cli via in-process bridge, sonnet, throwaway persona 'iris') … all 6 Arm-A turns ran the real read_file→record_monologue→propose_write rework loop".
- observation-ledger.md:413-414 — "**[S1-O21]** SMOKE RUN #2 (incident-scale ~41.6K seed, growing-doc, 12 turns, sonnet — SPENT TOKENS) | **LATENCY symptom REPRODUCED…**".

These are runs of the S1 harness, run **and recorded** — recorded exactly where METHODOLOGY stage 5 says lap results are logged ("run; log result in the observation ledger", METHODOLOGY.md:103, 170). Whether they count as completed stage-4→5 *laps* is adjudicable both ways (they are labeled smoke/anchor runs inside the harness's guarded-change; run #1's own row records "C2 anchor-repro NOT met → STOP-FOR-HUMAN", observation-ledger.md:376-377 — i.e., a failed representativeness anchor, arguably not a completed discriminating lap; run #2 records "the objective symptom is reproduced-on-demand", observation-ledger.md:421-422 — awfully lap-like). The document performs **neither** adjudication: it never mentions S1-O18/S1-O21 at all, and rests S1 = 0 on a factual premise ("never run") the pinned record refutes. The pre-registered guard-rails — "S1 = 0" and "no laps outside the O16/O17 inventory" (1.5-criteria.md:32) — are therefore asserted, not established. If the smoke runs count, S1 ≠ 0, and C8's own frozen terms make that a fail.

The lap-inventory sweep also confined itself to decisions.md while the rule's unit is defined by where stage 5 records runs — the sweep walked the wrong (or only one) ledger.

**(i) as written: PASS not earned.**

### (ii) D-14 sweep at the S1-O15 anchor — survives, with one false evidence claim

- Anchor verified: decisions.md:77 — "(S1-O15 refinement) degradation happened there too but needed **larger files / longer time** → dose-dependent, not qualitative" (doc cites :76-78, quote at :77-78). ✓
- Then-live leading account verified: decisions.md:70-71 — "Leading account is now **H-S1-EMERGENT** (context-length coherence decay, self-reinforcing within-session)" — and this is the immediately preceding entry (:68-74) before the S1-O15 entry (:75-86) in the append-only log. ✓
- Final-state subsumption verified: hypotheses.md:85 — "exactly the user's A/B (S1-O15)". ✓ Dose-contrast citations verified: hypotheses.md:82 "**fast, on small files**", :84-85 "**much higher threshold** (large files / long sessions)" (doc cites 82-85). ✓
- The adjudication (generic context-length decay accommodates "longer time" but not the file-size dose axis) follows from the cited text; the anchor non-vacuousness argument (final state explains it; no-chain is trivially residual) is sound. ✓
- New-candidate folding verified: decisions.md:81 — "New unifying candidate **H-S1-WRITELOAD-DOSE** recorded" (doc cites :81-83). ✓
- **FALSE claim:** "grep: 'residual' appears nowhere in the pinned decisions.md or hypotheses.md" (8-retrodiction.md:84-85). My grep: **hypotheses.md:167 — "residual context-length coherence decay is a model property"** (also observation-ledger.md:212). True for decisions.md only. The substantive conclusion survives — that occurrence is a caveat inside the refuted H-S1-DISTANCE entry, not a D-14-shaped per-row explained-or-residual disposition — but the stated grep result is factually wrong.

**(ii): expected outcome genuinely met; supporting evidence claim defective (minor).**

### (iii) D-2 checklist vs the S1 ending — survives, fully verified

- Rule verified: METHODOLOGY.md:221-227 — "Missing **any** of (a)–(e) → not a legal stop", located between stages 7 and 8. ✓
- Fixture quotes verified: decisions.md:68 ("**S1 stage-7 red-team** | **MAJOR** | hypothesis REVISED, NOT 'found'"), :72-73 ("**S1 outcome = CHARACTERIZATION + mitigation directions, not a code root-cause 'found'**"). ✓
- (a) "structural facts hold" — decisions.md:69. ✓ (b) DISTANCE refuted :68-70; FILEBLOAT "DEAD CODE on Phoebe's claude-cli provider" — decisions.md:60 (doc cites :59-62). ✓ (c) "largely a MODEL property — no clean code toggle" — decisions.md:71. ✓ (e) "I corrected my earlier over-confident S1 message to the user" — decisions.md:74. ✓ Contrast example "**User adjudication** | — | re-scoped" — decisions.md:22. ✓
- **(d) absence independently confirmed:** I scanned every decisions.md entry from :68 through :114. The subsequent user interactions (:75 user-supplied A/B, :97 spec refinements, :104 "go" for the repro) are engagement with the *continuing* hunt; none records sign-off of the characterized verdict. The named missing element is genuinely absent. ✓
- Framing nitpick: ":68-74" is called "the recorded S1 ending" (inherited verbatim from frozen C8) though the S1 thread demonstrably continues through :114. This actually *strengthens* the (d) adjudication (the characterization never became a signed-off terminal state), but the document never flags it.

**(iii): PASS genuinely earned.**

### (iv) D-8 escape vs the recorded inversion — survives, with one overclaimed aside

- Rule verified: METHODOLOGY.md:142-146 — escape requires the inversion recorded in decisions.md "**naming the infeasibility class**" + hypotheses stay `ungated`. ✓
- Ordering fixture verified: hypotheses worked/refuted across :41-86; "**S1 stage-4 — discriminating test DESIGNED**" only at decisions.md:87. ✓ (":45-50" for "H-S1-DISTANCE analyzed" is loose — those lines are the code-fidelity gate + "Structural analysis proceeded on it"; the analysis itself lives in hypotheses.md/S1-O5/O6. Nitpick.)
- Infeasibility-class citations verified: decisions.md:47-48 — "part of S1 may be emergent context-length coherence decay (a model property, not a clean toggle)"; hypotheses.md:163-164 — "bleed is intermittent/load-dependent → instrument-to-capture, not a clean offline toggle" (spans exactly those lines). ✓
- Formal-entry absence independently confirmed: no decisions.md entry records the stage-1 ordering inversion as such — the :45-48 gate entry flags the class but never states "repro ordering inverted". ✓ Verdict "substance present, formal entry absent" = exactly the pre-registered outcome. ✓
- Tier-marker citations verified: hypotheses.md:97-98 ("**GATE MARKER: ungated.** … Present as a strengthened *candidate*, never the cause"); decisions.md:84 ("marked `ungated`; NOT presented as the cause"). ✓
- **Overclaim:** "(The tier discipline half was honored in substance: the informing hypotheses stayed `ungated` …)" ignores a recorded counter-instance inside the inversion window: decisions.md:53 — "**H-S1-FILEBLOAT was presented as 'leading' WITHOUT a cold red-team or repro/toggle** — a gate-before-present slip". A hypothesis formed before the repro design did NOT honor the tier discipline (it was presented as leading while ungated). The pre-registered outcome for (iv) does not depend on this parenthetical, but as written it misrepresents the record.

**(iv): expected outcome genuinely met; the "honored in substance" aside is wrong (minor).**

### (v) D-12 at the post-second-refutation convergence point — core survives, narrative overreaches

- Rule verified: METHODOLOGY.md:188-191 — each stage-6 pass records classes covered / ruled out / "what assumption the live set shares". ✓
- Anchor quotes verified: decisions.md:62 — "SECOND S1 code hypothesis refuted on a false architectural assumption"; hypotheses.md:65-66 — "Second S1 hypothesis killed by a false architectural assumption (cf. H-S1-DISTANCE)"; :66 — "Do not resurrect without a claude-cli-aware mechanism". ✓
- Class inventory checks out against the record (DISTANCE refuted, FILEBLOAT refuted, EMERGENT live, WRITECONTENT-IMITATION "from the S1-O13 red-team" — hypotheses.md:68). ✓
- Shared assumption: **derivable** at the anchor — decisions.md:60-61 / hypotheses.md:62-64 state FILEBLOAT's dead-code fact, and hypotheses.md:65-66 flags the pattern. But "The record states this false shared assumption **in so many words**" overstates: the cited lines state FILEBLOAT's *own* assumption plus a cross-reference; the pair-wide "host-side path" umbrella is a derivation, whose best in-record support (observation-ledger.md:293-294 — "that's the real bleed surface, **not brain-side prompt assembly**") the document does not cite. Nitpick.
- **Logical overreach:** "D-12's record at the FIRST convergence pass (after H-S1-DISTANCE's refutation) would have put 'what does the live set share?' on the table one refutation earlier" does not follow from the record: at that point the live set was H-S1-EMERGENT (a model-property account); the host-side assumption only re-entered the live set when H-S1-FILEBLOAT was formed later on the user's push (hypotheses.md:55-60). Compounding this, under sub-check (i)'s own adjudication S1 completed zero laps — so no stage-6 pass would ever have fired on S1 at all, making every "convergence point" in (v) a counterfactual construct (acceptable, since the pre-registration chose the anchor, but the "one refutation earlier" claim stacks a second counterfactual the record does not license). The core pre-registered outcome — the rule, applied at the anchor, names the live set's shared architectural assumption non-vacuously — is nonetheless met.

**(v): expected outcome genuinely met; the added counterfactual narrative is unsupported (minor).**

### Evidence-set discipline

All citations in the document resolve into the five pinned fixture files, METHODOLOGY.md (the rules), and 1.5-criteria.md. No out-of-fixture evidence consumed. ✓ The C8 (ii) precedent reference (0-audit-findings.md:144-147) resolves: "the degradation existed on the pre-0.0.38 direct-edit path too (S1-O15) — the 0.0.38-only story didn't cover it". ✓

## Four lenses

**FACTUAL.** Of ~30 line-number citations spot-verified, 28 resolve exactly as claimed (quotes above). Three factual defects: (F1, major) sub-check (i)'s "never run" / "only run-and-recorded tests in the record are O16/O17" contradicted by decisions.md:104 and observation-ledger.md:360, :413; (F2, minor) the "residual appears nowhere" grep claim false at hypotheses.md:167; (F3, minor) the "(iv) informing hypotheses stayed ungated" aside contradicted by decisions.md:53.

**LOGICAL.** No sub-check is circular — each computes the rule's adjudication from record text rather than assuming the rule fired (the (ii) anchor-sensitivity demonstration is genuinely good practice). Two defects: (L1 = F1's consequence, major) sub-check (i)'s conclusion follows from an incomplete read, not from the record — the candidate laps that would break the pre-registered guard-rail were never adjudicated; (L2, minor) (v)'s "one refutation earlier" counterfactual doesn't follow (assumption not in the live set at that pass; and no S1 convergence pass exists under (i)'s own lap count — an unflagged internal tension between sub-checks (i) and (v)).

**MISSED OPPORTUNITY.** (M1) The cheapest skipped check is the one that would have caught the major finding: a grep of the observation ledger for run markers ("SPENT TOKENS", "RUN") when compiling the (i) lap inventory — stage 5 names that ledger as where runs are recorded, and it surfaces S1-O18/S1-O21 instantly. (M2) (ii) could have cheaply also tested S1-O15 against the co-live ungated candidate (H-S1-WRITECONTENT-IMITATION, hypotheses.md:68-74, "NO bloat story" :73), closing the "judged against the wrong then-live account" hole — the result would have held.

**UNSTATED ASSUMPTIONS.** (U1) That decisions.md alone registers laps — while the built rule's stage-5 half logs results to the observation ledger; this assumption is what makes the (i) walk look complete. (U2) That decisions.md file order = chronological order when identifying the "then-live leading account" (the self-audit at :52 already references the S1-O7 refutation that the :68-74 entry only later records — entry order is not strictly chronological; the (ii) anchor logic silently relies on file order). (U3) That ":68-74 = the recorded S1 ending" despite the thread continuing to :114 — inherited from frozen C8, never flagged. (U4) That the smoke/anchor runs bear on no sub-check — never stated, never argued.

## Ranked findings

1. **MAJOR — sub-check (i):** "S1 designed test never run; only run-and-recorded tests in the record are O16/O17" is refuted by the pinned record (decisions.md:104; observation-ledger.md:360-379, 413-427). The pre-registered guard-rails "S1 = 0" and "no laps outside the inventory" are asserted on a false premise; two candidate laps exist in the fixture and were never adjudicated. (i)'s PASS is unearned as written; if the runs count as laps, C8's frozen terms make it a fail. Re-adjudication (explicitly classifying S1-O18/S1-O21 — e.g., as gate-failed anchor runs inside the harness's guarded-change, not completed discriminating laps) could plausibly rescue S1 = 0, but that argument is absent from the document.
2. **MINOR — sub-check (ii):** the supporting claim "grep: 'residual' appears nowhere in the pinned decisions.md or hypotheses.md" is false (hypotheses.md:167; also observation-ledger.md:212). Substantive conclusion (no D-14-shaped per-row residual entry) survives on other grounds.
3. **MINOR — sub-check (iv):** "the informing hypotheses stayed `ungated` — honored in substance" ignores the recorded H-S1-FILEBLOAT presented-as-leading-while-ungated slip (decisions.md:53) inside the inversion window. The pre-registered outcome is unaffected.
4. **MINOR — sub-check (v):** the "one refutation earlier" counterfactual is unsupported (live set at the first refutation lacked the assumption, hypotheses.md:55-60) and sits in unflagged tension with (i)'s zero-lap adjudication (no S1 stage-6 pass would exist).
5. **NITPICK — (iv):** "H-S1-DISTANCE analyzed at :45-50" is imprecise (those lines are the code-fidelity gate/resolution).
6. **NITPICK — (v):** "states this false shared assumption in so many words" overstates the cited lines; the strongest in-record support (observation-ledger.md:293-294) goes uncited.
7. **NITPICK — (ii)/(iii):** the ":68-74 = recorded S1 ending" framing (inherited from C8) is never reconciled with the thread continuing to :114.

Sub-checks (ii), (iii), (iv), (v): expected outcomes genuinely met (with the noted evidence defects). Sub-check (i): expected outcome not established from the record as executed.

**Verdict: worst severity MAJOR (sub-check (i) rests on a record claim the pinned fixture refutes — S1-O18/S1-O21 candidate laps unadjudicated) — the C8 PASS claim does not survive as written.**
