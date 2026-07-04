# Stage-6 reviewer output — verbatim, in full

# Stage-6 cold red-team review — audit-hardening-2026-07 (built artifact)

## Provenance (sha256, computed by me via `sha256sum`)

| File | sha256 |
|---|---|
| scratchpad/audit-hardening.diff | `bf6683aec621befc9563af5fdb263afaeff0a442cc1c65796c2bd9e6967a0718` |
| changes/audit-hardening-2026-07/1.5-criteria.md | `c29dfada53cc7bdebdcf6acfbfc26cb8c7d892dc976a55205e00aa7d537f084d` (matches the freeze hash recorded in decisions.md:43) |
| changes/audit-hardening-2026-07/2-plan.md | `f8f0837046eb7d2d2e335ca7236a416b895678504675b03c1a5c5573e97e6bd7` |
| changes/audit-hardening-2026-07/decisions.md | `613711deb3a6d2cabb73c98d78cfe35526fc4135764e2920172cd847151b2057` |
| Guarded_change/METHODOLOGY.md (built, 533 lines) | `5e7f8236d150f2f0d7d91623c76f3394c30a862169ed6cd43c6b3d29a4db7f4a` |
| Guarded_change/SKILL.md (built, 122 lines) | `ecc3ec6cd431de0dee01f664bd58515bbab2085dd9a4b2b7149a485ab7897b34` |
| fixtures/review-record/1-spec.md | `baed3ea40a94316f5fbbe7bf690160ea26f0a1a87bf4d3f5c70047923a8f7a7d` |
| fixtures/review-record/1.5-criteria.md | `6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d` |
| fixtures/review-record/2-plan.md | `aab39b394434c3d30f5d99c53d234056825b2978ab29d76584b0e07a973ea134` |
| fixtures/review-record/3-redteam-plan.md | `8613c4ea4adc3ad5f02df52c9b03ec54f2aac9f61e9781eba51e153389d19903` |
| fixtures/review-record/6-redteam-code.md | `9f01852d807705eb3c21c8d3aac3aad2f1678a7ff2020d511e9a5df67263782a` |
| fixtures/review-record/8-harness.md | `beb30fae56811a00bf8dcf8cc600fb718029be79272f2538a32f34c128aaffca` |
| fixtures/review-record/decisions.md | `779d764b81b76bf8f2ec5c78bf332015e50dc1b4df9bf812642916ef137ea4b4` |

Mechanical verification I ran myself: (a) I regenerated `git diff 8a7ac65 -- Guarded_change/METHODOLOGY.md Guarded_change/SKILL.md` and it is **byte-identical** to the provided diff — the diff is complete for the two files. (b) Baselines at `8a7ac65` confirmed 467/102 lines; built = 533/122; growth +66/+20, combined 655. **C4 caps all hold** (533 ≤ 583, 122 ≤ 127, 655 ≤ 671). (c) Live copies at `~/.claude/skills/guarded-change/` are byte-identical to the `8a7ac65` base — **AR-7 honored, no premature install** (C5's precondition intact). (d) The working tree also carries a pre-existing, out-of-scope modification to `Guarded_change/guarded-change.companion.md` (the 2026-07-01 config repoint) — unrelated to this change, noted so scope is on record.

---

## TASK A — Mapping conformance (C1)

Walked all nine mapping rows (2-plan.md:15–23) against both files.

**F1 provenance — LANDED, one minor.** METHODOLOGY charter bullet at 236–249 carries all five embeds: (i) "the verbatim charter/prompt given" (237), (ii) "the exact context path list given" (238), (iii) "the reviewer's verbatim output (the author's summary lives in `decisions.md`, separately)" (238–239), (iv) "the reviewer's agent type + model" (239–240), (v) "the reviewer-reported sha256 of each context file it read (the charter instructs the reviewer to report these)" (240–241). Closed set at 244–247 ("the named stage artifacts + the config's `redteam_context` + the spec's touched-files list + carried-forward findings from `decisions.md`"), un-run consequence at 247, A/B prohibition at 247–249 ("prohibited outright — a leak is a confound (see the concurrency-lens C3 attempt-1 record)"). "What a run produces" sentence at 504–507. SKILL step 3 (line 67) carries all five duties + closed set + "missing any ⇒ the review is un-run"; step 6 (79–80) "verbatim record (same provenance duties as step 3)". **Finding A1 (minor):** the charter-core definition (METHODOLOGY:241–244) reads "plus any conditional lens whose trigger fires" and drops the plan's explicit enumeration "(position / concurrency / coverage)" ([R2-5], plan:15). Membership is now inferable, not stated — in particular whether the coverage-challenge bullet (a *discipline bullet* that is conditional-by-stage, not a "lens") belongs to "unconditional discipline bullets" (always included) or "conditional lens" (stage-3 only) is genuinely ambiguous. R2-5's defect (undefined core) partially recurs one level down. Low impact (the coverage bullet self-labels "(stage 3)"), but it is the one piece of the row's substance that did not land in full.

**F2 — LANDED.** METHODOLOGY:386–394: trigger ("created after the stage-6 review"), requirement ("targeted cold check before its results count — for representativeness, and, where the check guards a fix, that it fails against the unguarded version"), consequence ("until then its results are `verified = no`"), rebuild-in-place + gate-8 routing (390–392, [LO-6]), gates-7/8 fix-diff recording + stage-8 re-run duty (392–394). SKILL step 7 ("record any in-place fix diff in `decisions.md`", 83) and step 8 (90–93) both present.

**F3 — LANDED.** Column list extended in place (METHODOLOGY:397–398 "…│ evidence │ result*"), rule + [AR-5] rubric pointer ("the named judge + where the verdict is recorded", 399–400), consequence ("A gating PASS row with no evidence pointer counts as `verified = no`", 400–401), spot-verify extension (401–402). SKILL step-8 clause at 88–90 with consequence ("no evidence pointer ⇒ `verified = no`").

**F4 — LANDED, one nitpick.** METHODOLOGY:168–176: freeze at route-to-build, hash-or-verbatim-copy recorded, **gate-4-fix exception present** ("must equal the version the stage-3 reviewer read — except for gate-4 in-place fixes, each traceable to a logged finding, with the criteria diff recorded", 169–171), stage-8 verify + invalid-PASS consequence + targeted re-red-team (172–174), weakening-audit clause (174–176). SKILL step 4 at 72–73. **A2 (nitpick):** SKILL narrows to "record its sha256" / "frozen hash" (73, 93) where METHODOLOGY allows "hash (or a verbatim copy)" — a satisfying subset, not a contradiction, but the verbatim-copy route would make SKILL step 8's "frozen hash" wording literally inapplicable. Note: SKILL step 8's freeze-verify sentence (93) exceeds the mapping row's named location (step 4 only) — additive and consistent; no issue.

**F5 — LANDED.** METHODOLOGY:314–319 with the [R2-11] cold-review scoping exactly as specified: "For findings originating from a cold review (gates 4 and 7; at stage 8, findings from a targeted post-6 check)… harness measurements at stage 8 route by the table as before"; contest-via-logged-entry, blocker/major demotion → human tie-break, consequence "A silent unilateral demotion is a gate violation: the reviewer's routing stands" (318–319). SKILL steps 4 (70–72) and 7 (82–83).

**F6 — LANDED.** Spec duty METHODOLOGY:115–117; touched-files inside the single closed-set definition (245; [R2-12] verified — no second scope definition exists in either file); mechanical-diff rule with consequence at 191–193 ("a hand-curated file set = the review is un-run for the omitted scope"). SKILL step 1 (38), step 3 (inside the closed set, 67), step 6 (77–79).

**F7 — LANDED with consequence.** METHODOLOGY:250–254 incl. "[an] explicit 'none found' counts… incomplete on lens 4 and treated as un-run for that lens." SKILL step 3 (67, end): "no such section ⇒ lens 4 un-run."

**F8 — LANDED with consequence.** METHODOLOGY:472–478 incl. [MO-4] path classes, [R2-1] two-phase timing, "Gate 4 may not pass until the run-start validation result is recorded in `decisions.md`" (475–476), human-surface + degraded-review acceptance. SKILL Inputs 19–22. **B4 (nitpick, see Task B). A3 (nitpick):** the SKILL Inputs sentence spent 4 wrapped lines against the plan's ≈2 budget [R2-6]; total SKILL growth +20 ≤ +25, so the binding cap holds.

**F9 — LANDED.** SKILL:118–122 carries exactly the three sentences: position-sensitive-assembly sentence, "**Non-trivial edits take the full loop**, not a stage-3 pass alone", and the standing-criteria sentence (live==source `diff`; SKILL↔METHODOLOGY consistency on every shared rule; behavior-preservation for anything moved/removed). METHODOLOGY untouched for F9, as mapped. (Obligation-survival analysis in Task C.)

**Task A verdict: C1 substantively satisfied — 9/9 fixes present in every named location with trigger, requirement, and consequence; one minor (A1), two nitpicks (A2, A3).**

## TASK B — Cross-file consistency (C2)

Side-by-side on every dual-stated rule: touched-files (M:115–117 / S:38), provenance (M:236–249 / S:67, 79–80), mechanical diff (M:191–193 / S:77–79), coverage challenge (M:250–254 / S:67), reviewer-severity routing (M:314–319 / S:70–72, 82–83), criteria freeze (M:168–176 / S:72–73, 93), evidence column (M:396–402 / S:88–90), post-6 checks (M:386–394 / S:90–93), path validation (M:472–478 / S:19–22). Triggers, requirements, and consequences agree in all nine; SKILL consistently uses pointer-style naming the METHODOLOGY rule, per build-order step 2.

**The 7-item contradiction sweep — all 7 reconciliations hold in landed text:**
1. Closed set includes "carried-forward findings from `decisions.md`" (M:245–246), coherent with the pre-existing iteration-cap carry-forward (M:328–330). ✓
2. Freeze point = route-to-build with the gate-4 in-place exception captured (M:169–171). ✓
3. F5 forbids only silent unilateral demotion; human final word intact — "additionally requires the human tie-break (the same authority that breaks iteration-cap ties)" (M:317–318) coheres with "a person rules" (M:310–312). ✓
4. F2: rebuild-in-place is "not a loop restart"; change-findings "route via the gate-8 severity row" (M:390–392) — cap-counting is implicit in routing via the gate, adequate. ✓
5. F3 column-list extension is the expected benign deletion+addition hunk; the original "Any **gating** row that is not `verified = yes` blocks…" sentence survives verbatim (M:402–403). ✓
6. Stage review docs = "verbatim records… the author's interpretation belongs in `decisions.md`" (M:504–507). ✓
7. Rubric evidence pointer = "the named judge + where the verdict is recorded" in both files (M:399–400 / S:89–90). ✓

**New-contradiction hunt:** (a) **B2 (nitpick)** — the new evidence rule's trigger "every gating `verified = yes` row" (M:398) does not literally reach rubric rows, whose verified cell per the pre-existing following sentence "records… the named judge's verdict, not a bare yes/no" (M:406–409); the PASS-phrased consequence sentence (M:400–401) and the explicit rubric-pointer clause bridge the gap, so intent is unambiguous, but the trigger wording is imprecise. (b) F5 coheres with iteration-cap and human-override text (explicit cross-reference, M:317–318); the decisions.md human-override entry format (M:509–511) accommodates the contest entry. (c) SKILL step-8 additions cohere with METHODOLOGY stage-8: evidence column, post-6 check, fix-in-place re-run, frozen-hash verify all mirror M:386–402 + M:172. (d) **B3 (nitpick)** — the Human-in-the-loop list (M:523–533) was not extended for F5's new human touchpoint (blocker/major demotion tie-break); the list was already non-exhaustive (the iteration-cap tie-break is likewise absent), so this is style-consistent, not contradictory. (e) **B4 (nitpick)** — SKILL "record the result in `decisions.md` (gate 4 cannot pass without it)" (S:21) is ambiguous about later-spawn validations, which occur after gate 4; METHODOLOGY disambiguates ("run-start validation result", M:475). The pointer resolves it.

**Task B verdict: C2 satisfied — no trigger/requirement/consequence disagreement found; three nitpicks.**

## TASK C — Pure-additive check (C6)

Hunk-by-hunk walk of the diff. Pure-addition hunks (no deletions): METHODOLOGY @@-163 (criteria freeze), @@-219 (provenance + coverage bullets), @@-278 (F5), @@-415 (F8), @@-440 (verbatim-records para); SKILL @@-16 (F8 Inputs), @@-31 (F6 step 1). Deletion-bearing hunks, each checked for verbatim-or-stronger survival:

| Hunk | Class | Original survives? |
|---|---|---|
| M @@-112 (stage-1 spec) | paragraph extension rewrap | verbatim — "Deep enough that… guessing intent." intact, F6 sentence appended |
| M @@-176 (stage 3/6) | paragraph extension rewrap | verbatim — "code against criteria+plan." intact, F6 diff rule appended |
| M @@-343 (table columns) | **enumerated** (F3 column list) | verbatim — "Any **gating** row that is not `verified = yes` blocks "done" unless `decisions.md`" retained exactly (M:402) |
| S step 3, 4, 6, 7, 8 lines | **enumerated** (SKILL clause wiring) | verbatim in all five — e.g. "Write `3-redteam-plan.md`" → "…as a **verbatim record**…" (S:67); "Spot-verify a sample… (guards fabricated citations)." retained (S:76–77); "Emit the per-criterion verification table `8-harness.md` requires" retained (S:88) |
| S self-check | **enumerated** (F9 rewrite) | see C-2 below |

**C-1 (minor):** the two METHODOLOGY paragraph-extension rewraps (@@-112, @@-176) fall **outside** the plan's/criteria's enumerated expected-deletion classes — C6/[FA-3] name only "F9's sentence rewrite + in-place sentence extensions (F3 column list; SKILL clauses wired into existing bullets)" (1.5-criteria.md:21; plan:88–91). Both are benign (original text survives verbatim; same extension mechanism), but the letter of the frozen criterion is not met by the enumeration, and stage 8 must justify each deletion hunk in 8-harness.md — these two now need entries and a note that the enumeration was incomplete.

**C-2 (minor):** F9's rewrite drops "…is encouraged after any edit to either file" without a verbatim-or-stronger replacement for the **trivial-edit** class: the new text (S:118–122) is strictly stronger for non-trivial edits (full loop mandated) and retains the capability sentence, but no longer encourages any check after trivial edits. The plan claimed "original obligation retained + strengthened" (plan:23); that holds for non-trivial edits only. A small, real weakened corner under C6's strict test.

No other deletion exists; no existing rule was weakened by any addition (F5 constrains *whose* severity routes; the stage-8 carve-out "harness measurements… as before" preserves prior routing).

**Task C verdict: C6 substantively holds — no rule deleted or weakened in substance; two minors on the letter of the expected-classes enumeration and the F9 trivial-edit corner.**

## TASK D — Fixture fidelity

**V1 — conforms to spec.** 3-redteam-plan.md has zero provenance embeds (no charter, no context list, no agent/model, no hashes — it opens "A cold review of the plan was run and returned the following findings", line 3), is otherwise well-cited (`uploader.py:31, 74, 88`, `test_uploader.py:12-40`; lines 7–29), findings ranked, all four lens verdicts present, and carries the coverage-check section ("Criteria-coverage check — None found…", lines 31–34) so provenance is its only new-rule ground. ✓

**V3 — spec breach (D1, major).** The spec requires V3 "provenance-complete… ZERO citations as its only ground." As built, the record is **not provenance-clean under the amended rules it will be judged against**: (a) the embedded charter (6-redteam-code.md:5–14) is a paraphrase that omits several *unconditional* discipline bullets (earned-clean-factual, spot-verify, label-audit, the provenance bullet itself) — violating "The charter given is the METHODOLOGY charter **core** verbatim" (M:241–244); (b) the context list includes "the mechanical diff (`git diff 4c1f2aa..working`…)" (lines 15–17) but the reviewer-reported hash list (18–19) omits it, arguably failing duty (v); (c) the embedded charter never instructs hash-reporting, though the amended rule says "the charter instructs the reviewer to report these" (M:241). Failure scenario: a treatment reviewer flags 6-redteam-code.md citing **F1-provenance** instead of the intended pre-existing earned-clean rule → the pass condition "each citing the deciding rule" (1.5-criteria.md:18) becomes ambiguous, and V3 stops isolating a fires-in-both-arms rule (controls cannot cite provenance) — exactly the wrong-but-plausible-flag failure Task D probes. Counter-reading exists (duties (i)–(v) as the only "missing any of these" grounds, charter-core as author guidance), but with n=2 gating runs the fork is live. Cheap fix: quote the actual core verbatim in the fixture and hash the diff.

**V2 — own-goal (D2, major).** V2 (C1 row, 8-harness.md:9) correctly has execution claimed, plausible path narrative, and no output pointer; realism row C3 inlines its citation (`harness-out/c3-dedup.log`, "stored_copies=1", line 11) per [R2-10b]. But the **C4 advisory row cites the C1 run's own log**: "One `retry` line per attempt in the C1 run log (`harness-out/c1-retry.log`, 2 lines for 2 retries)" (line 12). The plan's requirement was that "V2 is the only gating row with no output location **anywhere**" (plan:44–45) precisely so nothing rescues it — yet V2's underlying run has a discoverable output location one row down. Benign-miss scenario: a treatment reviewer reasons "C1's raw output exists and is cited in the doc (C4 row) → C1 is substantiated" and passes it → a treatment miss of V2 → C3 **FAIL** (pass needs 2/2), burning the single logged re-run. A strict cell-scoped reading of F3 (M:398) still fires, so this is a probability-of-miss defect, not a certainty — but C3 is gating, n=2, and the plan's own bar for V2 was "maximally survivable [with] F3's mechanical rule… the sole differentiator." Cheap fix: have C4 cite a C4-specific artifact.

**V4 — conforms in substance, letter deviations (D4, nitpick).** C2 row (8-harness.md:10) is a different row, "Not exercisable pre-ship…", result "**will confirm live after ship**", and fixture decisions.md carries no named risk-acceptance ("C2 confirmed post-ship per harness", decisions.md:7–8) — matching the task spec exactly. Letter deviations from the plan: the verified cell reads "no" where plan:46 says it "reads 'deferred'" [R2-10a] (the intent — never `verified = yes`, one deciding rule — holds); and plan:44–45's "only gating row with no output location anywhere" is literally false because the C2 row also lacks one — benign, since C2 is a non-PASS row where no evidence is due. Both fire on pre-existing rules in both arms as designed. The harness table correctly uses the pre-change column format (no evidence column, line 7). ✓

**Unseeded extra violations (D3, minor).** Judged under the amended docs, the fixture run-record has flaggable gaps beyond the four seeded: fixture decisions.md records route-to-build with **no criteria-freeze hash** (decisions.md:3–4; required by M:168–171) and **no run-start path-validation record** (required by M:475–476, "Gate 4 may not pass until…"); 8-harness.md never verifies the frozen hash. Each is treatment-arm-only → extra treatment flags, breaching [LO-2]'s "one violation per artifact" for the run record and adding attention-dilution risk against the seeded targets. (Symmetric both-arms noise also exists: neither fixture review shows the pre-existing label-audit duty — non-confounding.) The build did sweep *some* amended duties deliberately (spec touched-files present, 1-spec.md:20–23; coverage section present; diff command recorded, 6-redteam-code.md:16–17) — the sweep just missed the decisions.md-side duties.

**Leak check (D5, nitpick).** No amended rule text appears anywhere in the fixture (grep across all seven files). Vocabulary echoes only: "reviewer-reported" (6-redteam-code.md:18, matching M:240's distinctive compound), "Touched files (expected)" (1-spec.md:20), "Criteria-coverage check" (3-redteam-plan.md:31), and V3's whole provenance block modeling the new format. All are inherent to the approved design (the fixture must conform to amended duties to avoid extra violations; V3 must be provenance-complete); controls cannot cite rules absent from their docs, and the protocol's tripwire + codification-recording covers control-side catches. No contamination beyond what stage 3 approved.

**Internal consistency as a fake run:** verified — stage-3 findings ↔ decisions stage-4 entry ↔ 6-redteam charter task-addition ("checksum ordering, fixed after the stage-3 review") ↔ 6-redteam output ("budget hard-caps the final sleep as the stage-3 fix specified") ↔ stage-7 entry ↔ harness notes (consistency flag carried) all cohere; C2's deferral rationale even contradicts the fixture plan's own mock-based C2 measurement (2-plan.md:8) — which makes V4 *more* catchable and is the intended attackable record. Synthetic-README correctly absent pre-runs [MO-5].

**Not assessable at this stage (flagged, not findings):** C5 (live==source) and C7 (final-report duties) are stage-8 properties — C5's precondition (no premature install) I verified mechanically; the C3 runs themselves (neutral `run-record/` copy, arm execution) have not occurred and cannot be reviewed here; this run's own 1-spec.md was outside my closed set (the plan + frozen criteria sufficed as the oracle).

---

## Ranked findings table

[As reproduced in 6-redteam-code.md — D1/D2 major; A1, C-1, C-2, D3 minor; A2, A3, B2, B3, B4, D4, D5 nitpick.]

## Bottom line

**Worst severity: MAJOR — both majors live in the fixture, not in the rule text.** The METHODOLOGY/SKILL edits themselves are in strong shape: all nine fixes landed in every mapped location with trigger, requirement, and consequence (C1), the two files agree on every dual-stated rule and all seven sweep reconciliations hold with no new contradictions (C2), the diff is genuinely additive with every original obligation surviving verbatim except the small F9 trivial-edit corner and two benign rewrap hunks the plan's enumeration missed (C6), all C4 caps hold, and AR-7 was honored. But the C3 fixture — the executable heart of this change's verification — has two material construction defects: V3's record is not provenance-clean under the amended docs it will be judged against (breaking its isolation of the earned-clean rule), and the C4 row's citation of the C1 run log hands treatment reviewers a benign reason to pass V2 (threatening the 2/2 gating pass condition). Both are cheap, targeted fixture fixes (quote the real charter core + hash the diff; point C4 at its own artifact; add the freeze/validation records for D3) that should be made — and the fixture re-checked — before the C3 battery is spent, since the protocol allows only one logged re-run.
