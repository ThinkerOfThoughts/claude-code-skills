# 8-retrodiction-litepass-round2.md — round-2 lite cold pass of the C8 retrodiction record

**What this is:** the ROUND-2 guarded-change-lite cold review of the REVISED `8-retrodiction.md`
(revision made in response to the round-1 MAJOR — see `8-retrodiction-litepass.md`). Tasks:
(1) resolution check of all 7 round-1 findings; (2) fresh four-lens pass on the revised
document. **Verdict: worst severity MINOR — the C8 PASS claim SURVIVES.** All 7 round-1
findings adjudicated genuinely resolved (the MAJOR "earned, not reworded around").

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model `claude-fable-5`, no shared context.
- **Run:** 2026-07-04 (post-resume, same day as round 1), task `ac3cd976effd9cdae`, session
  `723b134a…`; ~10.5 min, 14 tool uses.
- **Form:** guarded-change-lite, round 2 (single cold pass; same intent + criterion as round 1;
  closed set = round 1's set + the round-1 record; two ordered tasks: resolution check, then
  fresh pass — new defects introduced by the revision count fully).
- **Document under review:** `8-retrodiction.md` at its ROUND-2 (revised) state, sha256
  `66f9173ceca1e81fc18867f7e1d16e58e3996e653e961217e3c6cc40eabeca2b`.
- **Disposition (recorded in decisions.md):** MINOR + 5 nitpicks → fix-in-place per the
  severity model (minor routes forward with in-place fixes, no re-bounce); C8 **SCORED: PASS**
  on this verdict. ⚠️ The in-place fixes were applied AFTER this review ran, so the reviewed
  hash above is deliberately stale relative to the final file — the post-review fix-in-place
  list + final hash live in the decisions.md stage-8 entry (same pattern as the stage-7
  fix-in-place round).

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a GUARDED-CHANGE-LITE cold pass, ROUND 2 (single review pass, guarded-change's stage-3/6 charter core: four lenses + evidence discipline) of ONE document: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/8-retrodiction.md

This document was reviewed once before (round 1, verdict MAJOR + 3 minors + 3 nitpicks) and has been REVISED in place in response. The round-1 review record (charter + full verbatim findings) is at: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/8-retrodiction-litepass.md — read it.

INTENT (one line): the document claims to execute five pre-registered "retrodiction" sub-checks — replaying five newly-built dragonfly rules against a pinned real-hunt record — and reports all five PASS.

CRITERION (checkable): every citation in 8-retrodiction.md resolves in the pinned record at the cited lines and says what the document claims; every adjudication follows from the cited text rather than narrative assertion; every pre-registered expected outcome (as frozen in criterion C8 of 1.5-criteria.md) is genuinely met as stated — including the outcomes' own guard-rails (sub-check (i): S2 count ∈ {1,2} with the 1-vs-2 choice actually justified, S1 = 0, no laps outside the O16/O17 inventory; (ii): the anchor is really "the moment S1-O15 was recorded" and the then-live leading account is correctly identified from the record; (iii): the named missing element is genuinely absent from the record; (iv): the infeasibility-class citations exist and no formal inversion entry exists; (v): the shared assumption is genuinely stated/derivable at the anchor point); and no sub-check consumes evidence outside the pinned fixture set.

Your tasks, in order:
1. RESOLUTION CHECK — for each round-1 finding (1 MAJOR, 3 minors, 3 nitpicks, as ranked in the round-1 record), verify the revision genuinely resolves it (not merely reworded around it). For the MAJOR specifically: the revision must explicitly adjudicate S1-O18 and S1-O21 against the cycle definition (METHODOLOGY.md stage 6) with citations into the pinned record, and S1 = 0 must now be EARNED from that adjudication, not asserted. Quote the revised text and check its citations resolve.
2. FRESH PASS — re-run the four lenses on the revised document as a whole (FACTUAL: spot-verify line-number citations into the pinned files, including the NEW citations added by the revision — quote what is actually there; LOGICAL: does each adjudication follow? any circularity? any new internal tension introduced by the revision?; MISSED OPPORTUNITY: a cheap check the document still skips; UNSTATED ASSUMPTIONS: what is taken for granted). New defects introduced by the revision count fully.

Discipline: cite file:line for every claim you verify or dispute; rank findings blocker/major/minor/nitpick; "no issue found" per lens is allowed when true; a clean verdict with zero citations = un-run review.

Context (closed set — read ONLY these):
- The document under review (revised): /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/8-retrodiction.md
- The round-1 review record: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/8-retrodiction-litepass.md
- The pinned record it cites: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/fixtures/hunt-record/{decisions.md, hypotheses.md, CONTEXT-BLOAT-HUNT.md, observation-ledger.md, symptom-ledger.md}
- The frozen criteria with the pre-registered outcomes: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/1.5-criteria.md (criterion C8)
- The built rules being replayed: /home/zero/Desktop/claude-code-skills/Dragonfly/METHODOLOGY.md (stages 1, 6, 7, the characterized block, the coverage sweep)
- The audit (for the precedents the pre-registrations reference): /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/0-audit-findings.md

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, resolution check per round-1 finding with quotes, per-sub-check verification, lenses, ranked findings). End with: one-line verdict — worst severity + whether the C8 PASS claim survives (survives / does not survive).
```

---

## Reviewer output (verbatim)

# Cold review — 8-retrodiction.md, ROUND 2 (guarded-change-lite pass, four lenses + resolution check)

## Context-file hashes (sha256, computed by reviewer)

```
66f9173ceca1e81fc18867f7e1d16e58e3996e653e961217e3c6cc40eabeca2b  8-retrodiction.md (document under review, revised)
0bcb4ba04f36bc559a2ab41468b1557baee910b1f33fefef0865b5e41a763097  8-retrodiction-litepass.md (round-1 record)
0ba8cfc59f3fd0b63f3b0e5b0e1f282ee87b206d6ff8bc20b3c4591cbc00e130  1.5-criteria.md
f753d7fcf809a0303ee91dbeb85cbba327f5c01e0d753cde5aaecc98dbde5cbc  0-audit-findings.md
04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065  METHODOLOGY.md
a4c2addadfb78c3fe419222a52caf51218330e7d7b00ca7ec2e342dc8023606a  fixtures/hunt-record/decisions.md
fcfcd687929cd1f846309f03fd093c030c76c4c30fe9cf78ba275b22ec0586bc  fixtures/hunt-record/hypotheses.md
46ae8d4f0c9afd7793c041a944e144dc06d71bf183136ae1be78e499d46cb98f  fixtures/hunt-record/CONTEXT-BLOAT-HUNT.md
6459716bedf8c614416b1a64db2031a0eb3f33891ad25925521a1eab29727925  fixtures/hunt-record/observation-ledger.md
2d9d16ff61ece109aa0e490debbf8d7ea0b2b7189935ad6f10dc366e28fe41c6  fixtures/hunt-record/symptom-ledger.md
```

All five fixture hashes match those the round-1 reviewer reported (8-retrodiction-litepass.md:75-79) — the pinned record is unchanged between rounds. The document's own quoted sha for 1.5-criteria.md (`0ba8cfc5…00e130`, 8-retrodiction.md:6-7) matches my computed hash. The document's hash differs from the round-1 state (`17d87d5d…`, litepass:17) as expected for an in-place revision. Fixture-pinning-vs-gate-4 verification remains delegated to 8-harness.md (outside my closed set) — not checked here, same as round 1.

## TASK 1 — Resolution check, per round-1 finding

**R1-MAJOR — sub-check (i): S1-O18/S1-O21 unadjudicated, S1 = 0 asserted on the false premise "never run" (litepass:169).** **RESOLVED — genuinely, not reworded around.**
- The revision explicitly adjudicates both candidate laps against the cycle definition. S1-O18: "NOT a completed lap. It was a harness-qualification run inside the triage's guarded-change (entered at decisions.md:104-105) whose own representativeness anchor **failed**" (8-retrodiction.md:53-56). Citations resolve: decisions.md:104-105 = "**S1 → guarded-change ENTERED (user \"go\", 2026-07-02)** | — | full guarded-change under `hunts/…/changes/s1-repro-harness/`" ✓; observation-ledger.md:376-377 (within the cited :375-377) = "this configuration did NOT reach the bleed-producing regime → **C2 anchor-repro NOT met → STOP-FOR-HUMAN**" ✓; observation-ledger.md:361-362 = "verdict NO_BLEED but UNDERPOWERED → inconclusive (does NOT refute H-S1-WRITELOAD-DOSE)" ✓; hypotheses.md:91 = "Confirm (behavioural DOSE-RESPONSE, NOT yet done)" ✓ — no status was updated, independently confirmed (no S1-O17…O21 reference exists anywhere in hypotheses.md).
- S1-O21: "NOT a completed lap, same class" (8-retrodiction.md:63) with observation-ledger.md:413-414 = "**LATENCY symptom REPRODUCED; bleed still NO_BLEED**" ✓ and :419 = "compaction never fired → still didn't reach the deepest regime" ✓. The classification of the latency repro as "a stage-1-shaped repro achievement for the latency readout" (:65-66), not a lap for S1's frozen symptom, is sound: the frozen symptom ledger defines S1 as monologue bleed (symptom-ledger.md:20-42); latency appears nowhere in the frozen S# set. "It split no live hypotheses, and no status in the pinned hypotheses.md consumes it" (:68-69) — independently confirmed.
- The adjudication is genuinely rule-derived, not narrative: METHODOLOGY:182-183 defines a cycle as "one discriminating test **run and recorded** — a completed stage-4→5 lap"; METHODOLOGY:165-166 requires a stage-4 test to pass the representativeness gate "Before it is run"; METHODOLOGY:266-268 rejects an artifact "whose control does not exhibit the symptom"; METHODOLOGY:172-176 forbids consuming a reading before the triage is recorded passed. Both runs were the gate-qualification (anchor) runs themselves and both failed the anchor — they precede any stage-4→5 lap. The record confirms the smoke runs were anchor-seeking by design: "Minimal first pass now anchors on the incident-equivalent condition (big-history × A × large file) to satisfy the representativeness gate before walking the dose down" (decisions.md:101-103); S1-O18 ran only Arm-A turns (observation-ledger.md:364-365), i.e. the single anchor arm, not the discriminating A/B/C design — so ":the designed protocol itself never ran" (:73-74) is accurate on the record.
- The stale frozen parenthetical (":96 awaiting", superseded by decisions.md:104) is now explicitly corrected rather than leaned on (:73-78), and the revision carries an honest residual: "the cycle counter alone would not have fired on this class of thrash. Carried to 9-report.md as a named residual" (:86-91). S1 = 0 is now EARNED.

**R1-minor 2 — (ii) false grep claim "'residual' appears nowhere in decisions.md or hypotheses.md" (litepass:170).** **RESOLVED.** Revised claim: "the word 'residual' occurs only at hypotheses.md:167 … and observation-ledger.md:212 (the same caveat) — neither is a per-row explained-or-residual disposition" (8-retrodiction.md:127-131). My grep of all five pinned files (`grep -rni "residual"`) returns exactly two hits: hypotheses.md:167 and observation-ledger.md:212. The corrected claim is verifiably true across the whole pinned record.

**R1-minor 3 — (iv) "tier discipline honored in substance" ignored decisions.md:53 (litepass:171).** **RESOLVED.** Revised text scopes the honored window and records the violation: "honored for the archaeology/WRITELOAD-DOSE window … but the record also contains one recorded VIOLATION inside the inversion window: 'H-S1-FILEBLOAT was presented as \"leading\" WITHOUT a cold red-team or repro/toggle — a gate-before-present slip' (decisions.md:53), self-caught only by a user-prompted audit (:51-58)" (8-retrodiction.md:205-209). Citations resolve: decisions.md:53-54 says exactly that ✓; the honored-window citations hypotheses.md:97-98 ("**GATE MARKER: ungated.** … Present as a strengthened *candidate*, never the cause") ✓ and decisions.md:83-84 ("marked `ungated`; NOT presented as the cause") ✓. The added inference "that slip is exactly what D-8's stays-`ungated` condition binds" is sound against METHODOLOGY:144-146.

**R1-minor 4 — (v) unsupported "one refutation earlier" counterfactual + unflagged tension with (i) (litepass:172).** **RESOLVED.** The "one refutation earlier" claim is deleted; in its place an honesty flag: "since S1 completed zero laps — sub-check (i) — no actual S1 stage-6 convergence pass ever fired; the anchor is the analytically chosen point the frozen pre-registration names, a counterfactual replay by design" (8-retrodiction.md:250-253). The (i)/(v) internal tension is now explicit, not hidden.

**R1-nitpick 5 — (iv) "H-S1-DISTANCE analyzed at :45-50" imprecise (litepass:173).** **RESOLVED.** Now "the code-fidelity gate + structural-analysis entries at :45-50 — H-S1-DISTANCE's analysis itself lives at hypotheses.md:149-171" (8-retrodiction.md:185-186). hypotheses.md:149-171 is exactly the H-S1-DISTANCE entry ✓.

**R1-nitpick 6 — (v) "in so many words" overstated; observation-ledger.md:293-294 uncited (litepass:174).** **RESOLVED.** Now: "The strongest in-record statement of the pair-wide umbrella is the S1-O13 ledger row itself … (observation-ledger.md:292-294) — the umbrella is a derivation grounded there, not stated verbatim as a pair-property" (8-retrodiction.md:241-245). The quote resolves at observation-ledger.md:292-294 ✓.

**R1-nitpick 7 — ":68-74 = recorded S1 ending" never reconciled with the thread continuing to :114 (litepass:175).** **RESOLVED.** Framing note added: "the S1 thread in fact continues through decisions.md:114. This **strengthens** the (d) adjudication — the characterization never became a signed-off terminal state at any later point either" (8-retrodiction.md:167-170). Verified: decisions.md runs to line 114; the post-:74 entries (:75 user A/B, :97 spec refinements, :104 "go") are continued hunting, none a sign-off of the characterized verdict.

All seven round-1 findings: genuinely resolved.

## TASK 2 — Fresh pass on the revised document

### Per-sub-check verification against the frozen guard-rails (1.5-criteria.md:32)

**(i)** S2 ∈ {1,2} with the choice justified ✓ — count = 2, justified from the definition's unit with the alternative considered (8-retrodiction.md:42-47); citations resolve (decisions.md:28-29 "Reproduce-on-demand (O16)"; hypotheses.md:31-32 confirm legs O16/O17; decisions.md:25-26 "one cold red-team pass each"). S1 = 0 ✓ earned (resolution check above). No laps outside the O16/O17 inventory ✓ — I independently swept all five pinned files for run markers (`grep -n "SPENT TOKENS\|RUN #\|SMOKE"`): only S1-O18 (observation-ledger.md:360) and S1-O21 (:413), both adjudicated. CONTEXT-BLOAT-HUNT.md references runs only by pointer (S1-O21, "harness smoke" — CONTEXT-BLOAT-HUNT.md:13,24), records none. **PASS stands.**

**(ii)** Anchor is genuinely the S1-O15 moment ✓ (decisions.md:76-78: "(S1-O15 refinement) degradation happened there too but needed **larger files / longer time**"). Then-live leading account correctly identified ✓ — the immediately preceding entry: "Leading account is now **H-S1-EMERGENT**" (decisions.md:70-71). Adjudication follows from cited text (the dose-contrast at hypotheses.md:82-85: "**fast, on small files**" vs "**much higher threshold** (large files / long sessions)"); the demanded-residual absence is now verifiably true (grep, above); anchor non-vacuousness argument (final state subsumes it, hypotheses.md:85 "exactly the user's A/B (S1-O15)") ✓. **PASS stands.**

**(iii)** All five elements re-verified at the cited lines: (a) decisions.md:69-70 "structural facts hold"; (b) :68-70 + :59-62 "DEAD CODE on Phoebe's claude-cli provider"; (c) :71-72 "largely a MODEL property — no clean code toggle" = METHODOLOGY:224's named class; (d) genuinely absent — I re-scanned :68-114; the only human-adjudication-shaped entries (:22 "User adjudication" re-scope, :75, :97, :104 "go") engage the continuing hunt, none signs off the characterized ending; (e) :74 "I corrected my earlier over-confident S1 message". Rule verified at METHODOLOGY:221-227. **PASS stands.**

**(iv)** Infeasibility-class citations exist ✓ — decisions.md:47-48 ("emergent context-length coherence decay (a model property, not a clean toggle)"), hypotheses.md:163-164 ("bleed is intermittent/load-dependent → instrument-to-capture, not a clean offline toggle"). No formal inversion entry exists ✓ — no decisions.md entry records the ordering inversion as such; "S1 stage-4 — discriminating test DESIGNED" appears only at :87. Verdict "substance present, formal entry absent" = the pre-registered outcome verbatim. Rule verified at METHODOLOGY:142-146. **PASS stands.**

**(v)** The named assumption is genuinely stated/derivable at the anchor ✓ — decisions.md:59-62 ("the accumulation mechanism is DEAD CODE on Phoebe's claude-cli provider … SECOND S1 code hypothesis refuted on a false architectural assumption"), hypotheses.md:62-66 (incl. the pattern flag "cf. H-S1-DISTANCE" and the guard at :66), observation-ledger.md:292-294 (the umbrella's grounding). It matches the audit precedent verbatim: "Both refuted S1 hypotheses died on the SAME false architectural assumption (the Python tool-loop mattering on the claude-cli path)" (0-audit-findings.md:115-117). **PASS stands, with the finding-1 defect below.**

**Evidence-set discipline:** every citation in the revised document resolves into the five pinned fixtures, METHODOLOGY.md, or 1.5-criteria.md; the litepass filenames in the header are provenance pointers, not consumed evidence. No out-of-fixture evidence consumed ✓.

### FACTUAL lens

~35 line citations spot-verified, including all citations new in the revision; all resolve with the quoted content (quotes above), with two range imprecisions: (F1, nitpick) the (v) quote "the accumulation mechanism … is DEAD CODE" is cited as decisions.md:60-61 but spans :59-60; (F2, nitpick) the frozen parenthetical is quoted non-verbatim — 8-retrodiction.md:74-75 renders 1.5-criteria.md:32's "(designed test never ran, :96)" as "(its only designed discriminating test never ran — 'Awaiting user go/no-go', :96)", splicing decisions.md:95-96's text into what is presented as the frozen criterion's words (semantics preserved; both halves are real record/criteria text). No false factual claim found — the round-1 false grep claim is corrected to a claim my own grep confirms.

### LOGICAL lens

- **(L1, minor — the one real fresh defect)** Sub-check (v)'s body correctly derives "**Shared assumption of the refuted pair**, named" (8-retrodiction.md:234-235), but the outcome-check relabels it: "the rule, applied at the anchor, names **the live set's** shared architectural assumption ✓ (the Python tool-loop mattering on the claude-cli path)" (:247-249). At the anchor the live set is {H-S1-EMERGENT, H-S1-WRITECONTENT-IMITATION} — and neither holds the named assumption: EMERGENT is a model property (decisions.md:70-71) and WRITECONTENT-IMITATION was born precisely by relocating the mechanism to the subprocess context (hypotheses.md:68-74). The rule as built also demands the live-set line explicitly ("what assumption the live set shares (explicit 'none identified' counts)", METHODOLOGY:189-190), which the replayed record omits. The slippage is inherited from the frozen wording itself — C8 says "names the live set's shared architectural assumption" while its own anchor citations (hypotheses.md:65-66) and precedent (0-audit-findings.md:115-117) unambiguously point at the refuted pair's assumption — so the executed content matches the pre-registration's evident intent and (v) is non-vacuous either way; but a revision that flags three other frozen-wording problems (:73-78, :167-170, :250-253) leaves this sibling unflagged and checks the box under the wrong label.
- (i)'s adjudication stacks three grounds (gate-failed anchor, eliminates-nothing, no-status-updated) of which only the first is criterial — a post-gate discriminating test that eliminates nothing is still a cycle (that is exactly what the stage-6 cap counts, METHODOLOGY:178-180). Harmless: the criterial ground suffices, and the document's own residual note (:86-91) shows it understands the distinction. Not ranked beyond this note.
- No circularity: each sub-check computes the rule's adjudication from record text; no sub-check assumes the rule fired because the audit said it should. The (i)↔(v) cross-dependency is now explicitly flagged (:250-253) rather than latent.

### MISSED OPPORTUNITY lens

- (M1, nitpick) The extra-inventory sweep's stated evidence ("both ledgers walked", 8-retrodiction.md:82-83) is narrower than its claim's scope ("every run-and-recorded test in the pinned record" — five files); a one-line grep across all five fixtures for run markers would have closed it. I ran it: only S1-O18/S1-O21 surface; conclusion unaffected. (The two-ledger scope is defensible as rule-derived — METHODOLOGY:170,182-184 name those as the only recording surfaces — but the cheap check was skipped, and this guard-rail is the one that failed in round 1.)
- (M2, nitpick, carried from round-1 M2, still skipped) (ii) never tests S1-O15 against the co-live ungated candidate H-S1-WRITECONTENT-IMITATION (hypotheses.md:68-74, "NO bloat story" :73) — it would have held (an imitation-bleed account explains no degradation-dose axis), closing the last "wrong then-live account" hole for free.
- (M3, nitpick) The load-bearing premise of the MAJOR's repair — "a stage-4→5 lap requires the representativeness gate passed before the test's reading counts" (:60-61) — is a faithful paraphrase but carries no METHODOLOGY citation, in a document that cites every other criterial rule. The support exists (METHODOLOGY:165-166, 172-176, 263-268); it should be pointed at.

### UNSTATED ASSUMPTIONS lens

- (U1) That pre-registered *outcomes* bind while pre-registered *rationales/framings* may be corrected in flight without re-freezing — used three times (:73-78, :167-170, :250-253), never stated as a policy. All three corrections are documented and run against the author's convenience, so the practice is honest, but it is a standing assumption.
- (U2, carried from round-1 U2, still unstated) That decisions.md file order ≈ chronology when identifying "then-live" and "the inversion window" (decisions.md:52 references the S1-O7 refutation that the :68-74 entry records later). (ii)'s conclusion is robust to it — the :75-86 entry postdates :68-74 in the append-only log either way.
- (U3) That 8-harness.md's fixture-unchanged verification holds (8-retrodiction.md:4-5) — outside my closed set, unverifiable here; mitigated by my hash match against the round-1 reviewer's independently computed hashes.
- (U4) That "S1's frozen symptom" = bleed, not latency, for the S1-O21 adjudication — implicitly assumed but verifiable and true (symptom-ledger.md:20-42 freezes S1 as monologue bleed; latency is absent from the frozen set). Verified, not a defect.

## Ranked findings (round 2)

1. **MINOR — sub-check (v):** the outcome-check claims the replay "names the live set's shared architectural assumption" (8-retrodiction.md:247-249) while the body derives, correctly, the **refuted pair's** shared assumption (:234-235); the live set at the anchor (hypotheses.md:68-74; decisions.md:70-71) does not hold the named assumption, and the D-12 rule's own live-set line (METHODOLOGY:189-190, "'none identified' counts") is absent from the replayed record. Inherited from the frozen wording's slippage vs its own precedent (0-audit-findings.md:115-117); the executed content matches the pre-registration's evident intent, so (v)'s PASS survives — but the mismatch is unflagged.
2. **NITPICK — sub-check (i):** the frozen parenthetical is quoted non-verbatim (:74-75 vs 1.5-criteria.md:32), splicing decisions.md:95-96's text into the "quote".
3. **NITPICK — sub-check (i):** the criterial premise "gate passed before the test's reading counts" (:60-61) is uncited (supported by METHODOLOGY:165-166, 172-176, 263-268).
4. **NITPICK — sub-check (i):** the extra-inventory sweep's stated scope ("both ledgers", :82-83) is narrower than the claim's five-file scope; independently verified true by grep, conclusion unaffected.
5. **NITPICK — sub-check (ii):** "at comparable session lengths" (:119-120) is an interpolation not present in S1-O15's text (decisions.md:77-78); the adjudication survives on the record's own contrast (hypotheses.md:82-85).
6. **NITPICK — sub-check (v):** quote-range off by one (":60-61" for decisions.md text spanning :59-60).

Resolution check: 7/7 round-1 findings genuinely resolved (MAJOR earned, not reworded around; the corrected grep claim independently re-verified true). Fresh pass: sub-checks (i)–(iv) PASS genuinely earned on the pinned record; (v) PASS earned in substance with one unflagged label mismatch (finding 1). No sub-check consumes out-of-fixture evidence; no sub-check is vacuous or circular.

**Verdict: worst severity MINOR (the (v) live-set/refuted-pair label mismatch, inherited from the frozen wording and unflagged) — the C8 PASS claim survives.**
