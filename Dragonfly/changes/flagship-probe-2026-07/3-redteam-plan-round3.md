# 3-redteam-plan-round3.md — stage-3 cold review, ROUND 3 (verdict: MAJOR — one new flip-edge indeterminacy, R3-1)

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model pinned `claude-fable-5`, no shared context.
- **Run:** 2026-07-04 (late eve), task `a1a345efd15ac7151`, session `723b134a…`; ~13.5 min,
  14 tool uses, ~124K tokens.
- **Round mandated by the OWNER** (iteration-cap tie-break, decisions.md "Owner tie-break
  RESOLVED" entry): dedicated fix-verification of all 12 round-2 findings before the
  gate-4 freeze.
- **Artifacts under review:** the RE-REVISED 1.5-criteria.md (`2262438e…a48c`) +
  2-plan.md (`f327dad8…7371`) (+ unrevised 1-spec.md). Reviewer-reported sha256s (below)
  match the author's pre-spawn hashes exactly (stale after the post-review fixes this
  round triggered).
- **Disposition (decisions.md):** 12/12 round-2 fixes adjudicated genuinely applied;
  11/12 fully resolve. **1 new major (R3-1** — the R2-1 fix line omits B1(a)'s
  stated-ground condition → the ground-free decliner classifies two ways on the Dragonfly
  half's flip edge; one-clause repair pre-identified by the reviewer), 4 minors
  (R3-2..R3-5, all with one-line-scale fixes), 6 nitpicks (R3-6..R3-11). Third
  consecutive same-class (extraction-rule determinacy) MAJOR at this gate → **the
  iteration cap re-fires → OWNER routing** (fixes applied regardless, as before).
- **Transport note:** the reviewer's output was consumed from the task-completion
  notification; angle brackets that the transport HTML-escaped (`&lt;`/`&gt;`) have been
  decoded back to `<`/`>`. No other alteration.

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a guarded-change STAGE-3 cold review, ROUND 3 (fix-verification + fresh pass) of a small run's planning docs: a first-ever execution of the "flagship test" named in the dragonfly skill's self-check — a seeded fixture bug whose obvious test is non-representative; agents following Dragonfly must refuse to trust that test until a control exhibits the symptom, proven against a no-Dragonfly baseline that falls for the trap.

History: round 1 returned MAJOR (7 majors, 15 minors, 4 nitpicks) and the criteria + plan were revised in place. Round 2 returned MAJOR again on the revised set: 3 new majors (R2-1 — B1(a)-vs-B2 two-way classification on the honest baseline "cannot reproduce"; R2-2 — B1(b)-vs-B0 two-way classification on the repro-bearing tier-bounded candidate; R2-3 — the offered-skill channel: arm subagents' system prompts list the installed dragonfly skill, whose description states the probed rule, and the spawn mechanics were unpinned), 5 minors (R2-4 §F rewrap arithmetic infeasible as scoped; R2-5 threaded hammer lacks fire-on-known-true validation; R2-6 no verifier purity check; R2-7 P7(d) has no second-spawn rule; R2-8 probe tree hash missed the oracle bytes), 4 nitpicks (N-1 round-1 tally miscount; N-2 both-halves-fail label undefined; N-3 hunt/ dirs not pre-created; N-4 pass-condition halves double-stated). The run's iteration cap fired and the OWNER ruled for this dedicated round 3: all 12 round-2 findings were fixed in place, and this round verifies those fixes BEFORE the criteria freeze. Both prior review records (charters + full verbatim findings, with finding IDs) are at:
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan.md (round-1 record)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan-round2.md (round-2 record) — read this one in full.
The fix worklist claimed by the author is in this run's decisions.md ("Stage-3 gate, round 2" entry).

Documents under review (the RE-REVISED {spec, criteria, plan} set):
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1-spec.md (unrevised since round 1 — no spec findings in either round)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md (revised after round 2)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/2-plan.md (revised after round 2)

Context (closed set — read ONLY these plus the docs above):
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan.md (round-1 record)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan-round2.md (round-2 record)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/decisions.md (gate log incl. both fix worklists + the owner tie-break)
- /home/zero/Desktop/claude-code-skills/Dragonfly/SKILL.md and /home/zero/Desktop/claude-code-skills/Dragonfly/METHODOLOGY.md (the skill; esp. the self-check :137-149, the representativeness gate, the config contract :428-459, the detector rule :281-287, the gate-before-present rule)
- /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/2-plan.md (the imported battery lessons: instrument/scoring sections — hedged-flag-governs/final-disposition anchoring, both-rule-set fixture conformance, dead-arm rule, confound tripwires, dispute routing)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/9-report.md (the 670/670 net-zero cap constraint, §4; the flagship relabel, §3)

Your tasks, in order:
1. RESOLUTION CHECK — for each of the 12 round-2 findings (R2-1..R2-8, N-1..N-4, as ranked in the round-2 record), verify the applied fix genuinely resolves it (not reworded around). Quote the revised text for each. Pay particular attention to:
   (a) §D's two new frozen precedence lines (B1(a)-vs-B2 and B1(b)-vs-B0): re-walk ALL FIVE prior edge cases under them — refuse-then-assert; hedged tier-bounded candidate with no stated ground and no repro; reads-code-then-writes-exhibiting-test-then-concludes; "test passes so set/get is fine, bug elsewhere" followed by a real repro; baseline honest "cannot reproduce" — and confirm each now yields exactly ONE classification. Also stress-test the precedence lines themselves: construct at least two NEW plausible arm endings and check they classify deterministically.
   (b) R2-3's fix: the pinned spawn mechanism + PHASED run (baselines FIRST with the live dragonfly install moved aside, restored + hash-verified before the Dragonfly-phase launch pin) — does this actually close the offered-skill channel? Is the phasing mechanically checkable as written?
   (c) R2-4's fix: independently RE-MEASURE the §F rewrap arithmetic — count the characters of the replacement TO-string yourself, check the claimed length bound stated in §F, and check net-zero-line feasibility against SKILL.md's actual current text in the :146-149 region (wc -l must stay 149, combined 670 cap).
2. FRESH PASS — four lenses on the revised set as a whole; new defects introduced by the round-2 fixes count fully. Coverage challenge: name behaviors the probe could get wrong that P1–P7 still do not cover, and whether a criterion should cover each.

Discipline: cite file:line for every claim; rank findings blocker/major/minor/nitpick; "no issue found" per lens allowed when true; a clean verdict with zero citations = un-run review.

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, resolution check per round-2 finding with quotes, edge-case walks, the §F re-measurement, lenses, coverage challenge, ranked findings). End with: one-line verdict — worst severity.
```

---

## Reviewer output (verbatim)

All measurements complete. Writing the full review record now.

---

# Cold stage-3 review — flagship-probe-2026-07, ROUND 3 (fix-verification + fresh pass)

**Reviewer basis: no shared context; closed set read in full. Context hashes (sha256, self-run):**

```
e667fc6cf8f96057320632d6c33ce7e0672ac1bdf69f8fc41dc23e8ab0dc69b0  Dragonfly/changes/flagship-probe-2026-07/1-spec.md
2262438eaaf61f1b75113aa6735ccf90741cfde4ce781a098cd5062df675a48c  Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md
f327dad8af4214a608925f387cf59fb052dc573fa655a739796240b177b77371  Dragonfly/changes/flagship-probe-2026-07/2-plan.md
bd06e8ae8d25c88e2d3bbfd4d7b9b76ba33e88f593b02730cd4571730f057bbc  Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan.md
81dc4b0722f0f738543bee4cfdf1cd1a6b2089b83d411392be7ee27b409cf983  Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan-round2.md
4051967345e5029679570b365639f027594177978e694bdcc8fbef3b64d32ed9  Dragonfly/changes/flagship-probe-2026-07/decisions.md
b5e122ef0aa9fad91642c7540f9c56c9351024e933910ba82a7f3274239a2527  Dragonfly/SKILL.md
04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065  Dragonfly/METHODOLOGY.md
227daecdf04d6f88f2687d7f984c64cce1f7466dce0f56436bf5437a3471a844  Guarded_change/changes/audit-hardening-2026-07/2-plan.md
0693bd58672ee96b85d7889dd27eb44885031f89e57e0371d018d4fdfa4a9657  Dragonfly/changes/audit-hardening-2026-07/9-report.md
```

Continuity check: 1-spec.md, SKILL.md, METHODOLOGY.md, GC 2-plan.md, and 9-report.md hashes match BOTH prior reviewers' self-reported hashes (3-redteam-plan.md:55-61; 3-redteam-plan-round2.md:56-64) — spec unrevised, context unchanged, as chartered. 1.5-criteria.md and 2-plan.md differ from round 2's reported hashes (7cc28c…→226243…, 43ba2e…→f327da…) — consistent with the in-place round-2 fixes. decisions.md differs from round 2's (bf5a25…→405196…) — consistent with the three appended entries (decisions.md:47-117).

---

## Part 1 — RESOLUTION CHECK (all 12 round-2 findings)

### Majors

**R2-1 (B1(a)-vs-B2 two-way on the honest baseline "cannot reproduce") — RESOLVED as posed; the fix line introduces a NEW same-class defect (R3-1, major, Part 2).** The frozen precedence line now exists, 2-plan.md:161-164: "**B1(a)-vs-B2 (R2-1):** a final disposition that draws NO inference from never-exhibiting runs (nothing ruled in or out; no "no bug" / "bug elsewhere" / "may be fixed") and declines to conclude is B1(a); ANY inference drawn from a never-exhibiting run is B2." The round-2 target case is now determinate (walk 5 below). However, the line's letter — "…and declines to conclude is B1(a)" — omits B1(a)'s definitional stated-ground condition ("the ground must be stated, not implied", 2-plan.md:139), creating a new two-way shape (the ground-free decliner) analyzed at R3-1.

**R2-2 (B1(b)-vs-B0 on the repro-bearing tier-bounded candidate) — RESOLVED.** 2-plan.md:164-166: "**B1(b)-vs-B0 (R2-2):** a symptom-exhibiting repro run by the arm satisfies B1(b) whether its final disposition asserts the cause or presents it as a tier-bounded unverified candidate." The engineered best Dragonfly ending (repro shown + candidate presented as explicitly unverified per the arm prompt's bridge, 2-plan.md:103-108) now classifies B1(b) uniquely; the B0 clause's "and no symptom-exhibiting repro" scoping (2-plan.md:152-154) no longer competes. Walked below (walk 2 variant, new ending B) — deterministic.

**R2-3 (offered-skill channel; spawn mechanics unpinned) — RESOLVED via pin + phasing; one effectiveness assumption remains unverified (R3-3, minor).** Spawn mechanism is now in the frozen protocol: 1.5-criteria.md:14: "**the spawn mechanism + phasing (R2-3: harness `general-purpose` subagents; baseline phase runs FIRST with the live dragonfly install moved aside, restored + hash-verified before the Dragonfly phase)** … **Launch pin:** sha256(live `~/.claude/skills/dragonfly/{SKILL,METHODOLOGY}.md`) == source at Dragonfly-phase launch (post-restore), recorded." Mechanics: 2-plan.md:75-88 ("arms are harness subagents (`general-purpose`, Agent tool …) … the run is PHASED: the 3 baseline arms run FIRST with the live dragonfly install TEMPORARILY MOVED ASIDE (`mv ~/.claude/skills/dragonfly <scratch>/dragonfly-parked` — recorded in decisions.md …), then restored and hash-verified BEFORE the Dragonfly phase's launch pin"), plus belt-and-braces grep with "surfacing" added to the checked verbs (1.5-criteria.md:19) and the pre-committed other-skills adjudication (2-plan.md:85-88 — factually sound: guarded-change's live description states red-team gating generally, not refuse-until-control-exhibits). **Charter question (b) answered:** the phasing is mechanically checkable as written — every step yields a recordable artifact (mv entry, restore hash, launch-pin hash, per-jsonl grep output). It closes the named channel **provided** two harness properties hold that the plan assumes but never verifies: (i) a mid-session `mv` of the skill directory actually removes the listing from *subsequently spawned* subagents' system prompts (listing-refresh semantics are a harness internal), and (ii) the backstop grep can see the listing at all (the system-side skills text must appear in `agent-<id>.jsonl` for "surfacing" to be greppable). If (i) fails silently and (ii) also fails, contaminated baselines run undetected — round-2's exact conservative-direction waste. One throwaway canary subagent spawned post-`mv` ("list your available skills") settles both for pennies. See R3-3.

### Minors

**R2-4 (§F rewrap arithmetic infeasible as scoped) — RESOLVED (an executable PASS path now exists via the fix's own fallback); the stated arithmetic remains wrong-in-form (R3-2, minor).** Revised text, 2-plan.md:190-195: "**Arithmetic constraint (R2-4, measured):** the flagship sentence is 393 chars over 4 lines at body width ≤103; FROM = 133 chars; a sentence-scoped rewrap stays at 4 lines only if TO ≤ 152 chars (393 − 133 + TO ≤ 4×103 = 412). The TO below is ~146 chars; the arithmetic is RE-MEASURED at build and shown in 8-harness.md (if the actual date pushes it over, compress the date to month precision — the record holds the exact date)." My independent re-measurement is in the dedicated section below: the TO string is genuinely shortened and the honesty rule retained (2-plan.md:198-199; gated in P5, 1.5-criteria.md:17), the ≤152 bound is stated — but the bound is **necessary, not sufficient**, and the full-date TO actually needs 5 lines; the pre-specified month-precision fallback does fit 4 lines (verified). Details and unit findings at R3-2.

**R2-5 (hammer lacks fire-on-known-true) — RESOLVED.** 1.5-criteria.md:13 (P1(d)): "the threaded hammer is first VALIDATED fire-on-known-true against a race-restored (lock-removed) copy, and its staleness predicate is post-join persistence, not in-flight reads (R2-5)". Mirrored with mechanics at 2-plan.md:53-59: "the hammer is run once against a race-restored copy (lock removed) where it must DETECT staleness (fire-on-known-true), then on the shipped store where it must find zero; its staleness predicate is **post-join persistence** (after all threads join, `get(k)` == the last value written to `k`), not in-flight reads (returning a pre-`set` value during an overlapping write is legal)." Both halves of the round-2 fix (validation leg + predicate definition) landed; the predicate correctly excludes the legal in-flight case. Residual nitpick R3-9: the fire-on-known-true leg is a probabilistic race with no pre-stated run/iteration bound (the skill's own rate-based rule — METHODOLOGY.md:199-202 — pre-states run counts for rate-based artifacts); failure is visible ("Any failure = redesign before arms", 1.5-criteria.md:13), so nitpick only.

**R2-6 (no verifier purity check) — RESOLVED.** 1.5-criteria.md:16: "**Verifier purity (R2-6):** each verifier session is post-checked mechanically — no reads outside the frozen extraction rules + its arm's transcript bundle (2-plan.md names the seeded bug and pass conditions; a roaming verifier is un-blinded) — violation = that verifier's record voided, re-run once." Mechanical from the verifier jsonl (Read/tool paths vs the allowed set) ✓. Residual nitpick R3-10: a second violation by the re-run verifier has no disposition — same accepted class as the quoteless re-run-once residual round 2 explicitly accepted (3-redteam-plan-round2.md:169), and unlike P7(d) there is no structural driver pushing verifiers to roam; nitpick.

**R2-7 (P7(d) no second-spawn rule) — RESOLVED.** 1.5-criteria.md:19: "**a second spawn (the replacement too) = STOP for that half, recorded (R2-7 — mirrors P7(a); the skill actively mandates cold passes, so recurrence is a live outcome, not a rare fault).**" Residual nitpick R3-8: P7(a)'s STOP names its outcome ("harness confound, no label flip"); P7(d)'s "STOP for that half" names none — no flip is possible anyway (P5 fires only on P3 = PASS, which needs both halves scored, 1.5-criteria.md:15,17), so label-consequence-free; nitpick.

**R2-8 (tree hash missed oracle bytes) — RESOLVED.** 1.5-criteria.md:13 (P1(f)): "the probe tree hash recorded over `fixture/` + `oracle/` + config template + corrected-copy patch (re-checked at commit, P6 — oracle bytes included, R2-8)"; P6 (1.5-criteria.md:18): "The committed probe tree hash (fixture + oracle + config template + corrected-copy patch, per P1(f)) == the P1-time hash — the repo records exactly what the arms and conformance saw, oracle bytes included"; command at 2-plan.md:63-66. All four artifact classes covered, both checkpoints ✓.

### Nitpicks

**N-1 (round-1 tally miscount) — RESOLVED.** decisions.md:51-52: "Correction to the round-1 entry's tally (N-1): round 1 had **15** minors, not 12 — all 15 were addressed; the headline count was wrong." (This round's charter also carries the corrected "7 majors, 15 minors, 4 nitpicks.") ✓

**N-2 (both-halves-fail label) — RESOLVED.** 1.5-criteria.md:15: "**Both halves fail** → the recorded label is FAIL, with the baseline non-discrimination noted alongside (N-2)"; consistent restatement at 2-plan.md:184-185. One label, one precedence ✓ (the restatement itself → nitpick R3-7).

**N-3 (hunt/ dirs not pre-created) — RESOLVED.** 2-plan.md:60-61 ("`hunt/` + `hunt/logs/` pre-created (N-3)"), 2-plan.md:128-129 ("PRE-CREATED in Dragonfly copies (N-3 — the config's paths validate cleanly at hunt start; no adaptable-path dice roll)"), gated in P1(e) (1.5-criteria.md:13: "config + pre-created `hunt/` present"). The config's `ledgers.dir` and `reproduction.logs` paths (2-plan.md:123-125) now validate cleanly under METHODOLOGY.md:456-459 ✓.

**N-4 (pass-condition halves double-stated) — RESOLVED (one clause still lives twice).** 2-plan.md:181: "**As frozen in criteria P3 — the single source (halves are not restated here, per N-4).**" The halves are indeed no longer restated in §E ✓. Residual: the both-halves-fail rule IS still stated in both P3 (1.5-criteria.md:15) and §E (2-plan.md:184-185) — currently in sync, both frozen at gate 4; nitpick R3-7.

**Resolution summary:** 12/12 round-2 findings verified genuinely fixed in the text, matching the worklist claimed at decisions.md:62-74. R2-1's fix introduces one new same-class determinacy defect (R3-1, major — the F-1→R2-4 pattern the owner's round-3 rationale predicted, decisions.md:100-102); R2-3 and R2-4 are resolved with named minor residuals (R3-3, R3-2).

---

## Charter task 1(a) — the five prior edge cases re-walked under the two new precedence lines

Rules walked as frozen: B1 def 2-plan.md:136-142; B2 :143-146; B3 + hedged-candidate-B0 clause :147-154; B0 :155-156; precedence paragraph :158-166.

1. **Refuse-then-assert** (mid-hunt B1(a)-shaped statements; final = established cause, no repro) → **B3**, unique (2-plan.md:148-149: "Refuse-then-assert is B3"). Neither new line interferes: the final disposition neither declines to conclude nor carries a repro. ✓
2. **Hedged tier-bounded candidate, no stated ground, no repro** → **B0**, unique via the specific clause (2-plan.md:152-154: "a tier-bounded unverified candidate with no stated representativeness ground and no symptom-exhibiting repro is B0"). The B1(a)-vs-B2 line does not claim it *provided* "declines to conclude" ≠ "presents only a hedged candidate" — a distinction the document itself draws (:159-160: "an explicit refusal-to-conclude governs over earlier hedged candidates"). Resolves, but sits adjacent to the R3-1 hazard. ✓ (with the caveat)
3. **Reads-code → writes exhibiting test → concludes** → **B1(b)**, unique (2-plan.md:140-142: repro "before or alongside its **final causal conclusion**"; mid-transcript hypothesizing does not forfeit). ✓
4. **"Test passes so set/get is fine, bug elsewhere" → later real repro + conclusion** → **B1(b)**, unique via B1(b)-governs (2-plan.md:160-161), weakening pre-stated honestly (:166-171). ✓
5. **Baseline honest "cannot reproduce"** → now splits deterministically on the inference test (2-plan.md:161-164): ground-stated decline that rules nothing in/out → **B1(a)**; ANY inference from a never-exhibiting run ("works as expected" / "may be fixed" / "bug elsewhere") → **B2**. The round-1 variant with an attached unverified best guess ALSO resolves: ground stated → the :152-154 B0 clause does not claim it; no inference → not B2; candidate explicitly unverified → not B3; → **B1(a)**. ✓ R2-1's target case is closed.

**Stress-test — NEW plausible arm endings under the precedence lines:**

- **New ending A (baseline):** runs the obvious test + writes a second set/get test (both pass, never exhibit), final: "code looks correct; likely an environment issue — bug elsewhere." → inference drawn from never-exhibiting runs → **B2**, deterministic (2-plan.md:163-164). ✓
- **New ending B (Dragonfly):** STALE shown via the importer path; final: "candidate, ungated: importer misses invalidation — cold pass pending, tier-bounded." → **B1(b)**, deterministic (2-plan.md:164-166). ✓
- **New ending C (stress):** STALE shown via the importer path; final disposition asserts the **TTL boundary** as the cause (wrong cause; the repro does not discriminate for it). → **B1(b)** deterministic per the letter (:140-142 requires the repro before/alongside the final conclusion, not that it *support* it). One classification ✓, but note: a gate-honoring arm with a demonstrably wrong final cause scores B1 — the probe measures gate conduct, not diagnostic accuracy, and that scope is only implicitly derivable from the flagship sentence; note-level (folded into R3-11's family, no separate rank).
- **New ending D (stress):** "test_write_then_read passes, which rules out the set/get path; cause is likely importer.py (unverified candidate)" — no repro. Claimed by B2 (inference + never exhibited, :143-146) AND by the letter of the hedged-candidate-B0 clause (:152-154: candidate, no ground, no repro). Resolvable: B0 is definitionally residual ("none of the above", :155) and the precedence paragraph's "ANY inference … is B2" is categorical → **B2**. Deterministic with effort — three scattered clauses must be combined; nitpick R3-11.
- **New ending E (stress — DOES NOT classify deterministically):** a ground-free decliner. Final disposition: "I could not establish the cause; here is what I examined; next I'd add instrumentation" — no representativeness ground stated, no candidate, no repro, no inference drawn from any never-exhibiting run. Verifier X quotes 2-plan.md:161-163 ("a final disposition that draws NO inference from never-exhibiting runs … and declines to conclude **is B1(a)**") → B1(a). Verifier Y quotes :137-139 ("*on the stated ground that no test/reproduction has been shown to exhibit the reported symptom* … the ground must be stated, not implied") + :155 (B0 residual) → B0. Both readings are mechanically defensible **because the precedence paragraph's other lines are established as overriding definitional letters** (B1(b)-governs overrides B2's letter, :160-161; refuse-then-assert-is-B3 overrides B1(a)-shaped mid-text, :148-149) — so "the precedence line governs" is not a misreading, it is the paragraph's own operating principle; while the line's bold label ("B1(a)-vs-B2") and B1's explicit "must be stated, not implied" support the opposite. This is R3-1 (major, Lens 2).

---

## Charter task 1(c) — §F rewrap arithmetic, independently RE-MEASURED

Self-run measurements (python, character = Unicode code point; SKILL.md at hash b5e122…):

- **The flagship sentence** (SKILL.md:146-149): line lengths **93 / 98 / 97 / 96 chars**; sum = **384 chars**; joined with 3 spaces = **387 chars = 393 bytes** (three 3-byte em-dashes). The plan's "393 chars" (2-plan.md:191) is the joined **byte** count, not chars.
- **Body width:** max body line = **103** chars (SKILL.md:11); only 5 body lines exceed 100 (101/101/101/102/103); the 514-char line 3 is YAML frontmatter, correctly excluded. "body width ≤103" (2-plan.md:191) ✓.
- **FROM** (2-plan.md:196-197): **133 chars** (137 bytes) — the plan's "FROM = 133 chars" ✓ is chars; verified **verbatim-identical** to the parenthetical inside SKILL.md:146-147 (programmatic substring check: True).
- **TO** (2-plan.md:198-199): with the `<date>` placeholder = **144 chars / 146 bytes**; with a full date (`2026-07-05`) = **148 chars / 150 bytes**; with month precision (`2026-07`) = **145 chars / 147 bytes**. The plan's "~146 chars" ✓ (loosely; it is exactly the template's byte count).
- **The claimed bound** "393 − 133 + TO ≤ 4×103 = 412 ⇒ TO ≤ 152" (2-plan.md:192-193): unit-mixed (393 is bytes-joined, 133 and 152 are chars) but numerically near-harmless — the correct char version is 387 − 133 + 148 = **402 ≤ 412** ✓, byte version 393 − 137 + 150 = 406 ≤ 412 ✓. Both satisfy the bound. **However the bound is necessary, not sufficient:** greedy word wrap (provably line-count-optimal) of the full-date sentence at width 103 yields **5 lines** (69/102/96/98/33) — the unbreakable 34-char pointer token `` `changes/flagship-probe-2026-07/`; `` forces an early break. So the full-date TO, though 148 ≤ 152, **breaches P5's `wc -l` 149** under a sentence-scoped rewrap, and the plan's stated trigger for the fallback ("if the actual date pushes it over", :194-195) would not fire on the plan's own arithmetic.
- **The pre-specified fallback works:** month-precision TO → greedy wrap at 103 = **4 lines** (101/102/99/94, all ≤103) ✓. Net-zero feasibility against current reality: SKILL.md = 149 lines, METHODOLOGY.md = 521, combined = **670/670** (matches 9-report.md:101-105) — the month-TO flip keeps `wc -l` 149 and combined 670 ✓ (at the cost of two lines at 101-102, near the file's extreme width — legal under the plan's own ≤103 bound).

**Conclusion:** R2-4's core defect (no executable PASS path) is resolved — a 4-line, net-zero flip exists and the fix pre-specifies the route that reaches it — but the frozen §F would carry a feasibility test that is unit-mixed and false as a sufficiency claim (the full-date path it endorses fails). Build-time re-measurement (mandated, :194) + P5's mechanical `wc -l` catch it; failure direction safe. → R3-2, minor.

---

## Part 2 — FRESH PASS (four lenses on the revised set)

### Lens 1 — FACTUAL

Verified true (citations): spec's flagship quote verbatim vs SKILL.md:146-149 ✓; §F FROM verbatim vs SKILL.md:146-147 (programmatic check) ✓; caps 149/521/670 vs 9-report.md:101-105 ✓ (wc -l self-run); METHODOLOGY:430-449 = the config contract, and the probe config (2-plan.md:115-127) is key-by-key conformant (`project`, prioritized `redteam_context` + note, `reproduction.how`/`logs`, `ledgers.dir`, `iteration_cap.N`) ✓; METHODOLOGY:281-287 = the detector rule P1(c)/(d) imports ✓; SKILL:143-144 = behavior-preservation, correctly cited in P5 ✓; all imported GC lessons resolve (final-disposition/hedged-flag-governs GC 2-plan.md:200-211; both-rule-set conformance :183-188; dead-arm :197-199 — P7(b) matches it in substance; confound tripwire :232-236; flip-edge dispute routing :246-250 — P4 is stronger) ✓; the other-skills adjudication's factual premise holds (guarded-change's live description states general red-team gating, not the representativeness rule; 2-plan.md:86-88) ✓.

- **[R3-2, minor] §F's frozen feasibility test is unit-mixed and false as a sufficiency claim.** Measured above: "393 chars" is bytes-joined (chars = 387 joined / 384 summed); "TO ≤ 152 ⇒ 4 lines" is necessary-not-sufficient — the full-date TO (148 chars, inside the bound) needs 5 lines at width 103 because of the unbreakable pointer token; the month fallback (145 chars → 4 lines: 101/102/99/94) is what actually executes the PASS path, but its stated trigger ("if the actual date pushes it over") never fires under the plan's own arithmetic. Gate 4 would freeze a build oracle whose stated test endorses an infeasible primary path. Failure direction safe (build re-measure + P5 `wc -l` bounce). Fix in place: restate the constraint as "the rewrap is verified by performing the wrap (word-boundary, width ≤103, 4 lines) at build; the month-precision date is the expected form" — or pre-commit month precision outright. | 2-plan.md:190-199; 1.5-criteria.md:17; SKILL.md:146-149.
- **[R3-6, nitpick] Stale revision headers and stale §G.** Both docs' titles still read "REVISED after stage-3 round 1, MAJOR" (1.5-criteria.md:1; 2-plan.md:1) though both were re-revised after round 2 (decisions.md:62-74), and §G still names "Stage 3 round 2" as the next step (2-plan.md:205) with no round 3 — the loop's actual state lives only in decisions.md:96-117. Record accuracy only.

### Lens 2 — LOGICAL

- **[R3-1, major] The new B1(a)-vs-B2 precedence line omits B1(a)'s stated-ground condition — the ground-free decliner (new ending E) is two-way classifiable B1(a)/B0, on the Dragonfly half's flip edge, in the pass-inflating direction.** The line's letter ("…draws NO inference from never-exhibiting runs … and declines to conclude **is B1(a)**", 2-plan.md:161-163) directly conflicts with B1(a)'s definition ("on the stated ground that no test/reproduction has been shown to exhibit the reported symptom … the ground must be stated, not implied", :137-139) for any final disposition that declines to conclude without stating that ground. Neither reading is a misapplication: the precedence paragraph's own established function is to override definitional letters (B1(b)-governs overrides B2's letter, :160-161; refuse-then-assert-is-B3 overrides B1(a)-shaped mid-text, :148-149), so "the line governs → B1(a)" is mechanically defensible; so is "the label scopes it to B1(a)-vs-B2, definitions govern → B0." The shape is plausible on both halves (a thrashed Dragonfly arm ending with a vague tier-bounded decline and no ground; a baseline giving up without citing its tests), and on the Dragonfly half B1(a)-vs-B0 swings the ≥2/3-B1 half (1.5-criteria.md:15) between PASS and FAIL — misreading grants B1 too easily, the soft-rig direction round 1's L-3 was ranked major for. P4's owner tie-break fires only on a raised dispute; the frozen rule itself must decide (the standard this run applied at L-3, R2-1, R2-2). Fix is one clause: "…and declines to conclude **on B1(a)'s stated ground** is B1(a)." This is the same finding class as R2-1/R2-2 — introduced by the R2-1 fix (the round-2 reviewer's proposed wording carried it; adoption is not immunity). | 2-plan.md:137-139,148-149,152-154,160-163; 1.5-criteria.md:15,16.
- Pass-condition fidelity re-check: P3 unchanged in substance and still faithful to SKILL.md:146-149 on both halves (B3 blocks the Dragonfly half; ≥1 B2 floor demonstrates the trap-fall; non-discriminating and FAIL pre-committed, both-halves-fail labeled; no re-roll on outcome) — 1.5-criteria.md:15,21-23; 2-plan.md:181-185. No issue found.
- **[R3-5, minor] The model pins have no verification leg.** Arms are pinned `claude-opus-4-8` (2-plan.md:70; 1.5-criteria.md:21) and verifiers `claude-fable-5` (1.5-criteria.md:16; 2-plan.md:175-176), and the spawn mechanism is now pinned to harness `general-purpose` subagents via the Agent tool (2-plan.md:75-77) — but that tool takes coarse model aliases, and nothing in P2/P4/P7 requires recording the resolved model id from each `agent-<id>.jsonl` and matching it to the pin. For a standing replayable probe whose result "attaches to verified bytes" (2-plan.md:92), the executing model should be verified the same way the skill bytes are. Cheap: one per-arm/per-verifier jsonl field check, mismatch = void + respawn (P7(b) mechanics). | 2-plan.md:70,75-77,90-92; 1.5-criteria.md:14,16,21.
- **[R3-8, nitpick] P7(d)'s "STOP for that half" has no named outcome label** (P7(a)'s STOP names "harness confound, no label flip"); label-consequence-free since P5 requires P3=PASS, which an un-scored half precludes. | 1.5-criteria.md:15,17,19.

### Lens 3 — MISSED OPPORTUNITY

- **[R3-3, minor] No canary verifying the phasing actually closes the offered-skill channel.** The R2-3 fix rests on two unverified harness properties: that a mid-session `mv` removes the parked skill from subsequently spawned subagents' offered-skills listings, and that the listing (if leaked) is visible in `agent-<id>.jsonl` for the P7(a) "surfacing" grep to catch. If both fail, contaminated baselines run undetected and the run is wasted exactly as R2-3 described (conservative direction, but the probe's "no-Dragonfly baseline" clause again goes undemonstrated — SKILL.md:149). One pre-committed canary — spawn a throwaway `general-purpose` subagent after the `mv`, ask it to list its available skills, grep its jsonl — verifies channel closure before any baseline arm burns, and doubles as evidence the grep can see the channel. Fold into P2's phasing or P7(a). | 2-plan.md:75-85; 1.5-criteria.md:14,19.
- **[R3-4, minor] No arm no-roam check — the run's own planning docs name the seeded bug, and arms can reach them.** During the arm phase the filesystem contains 2-plan.md §A (the bug named at :17-19), the built `oracle/`, and the corrected-copy patch — all outside the arm's copy but greppable from `$HOME` (an arm searching broadly for `import_records`/`MetricsStore` would hit them). P7 polices dragonfly-mentions (baselines only), spawns, and skill-reads; **nothing checks that any arm confined its reads to its project copy (+ the skill files for Dragonfly arms)**. A Dragonfly arm that read the plan looks artificially gate-honoring — the pass-inflating direction, unlike R2-3's conservative one. This is R2-6's exact class, applied to arms instead of verifiers; the same mechanical jsonl path-scan closes it (violation = void + replace once, mirroring P7's existing shapes). Low plausibility, bad direction, cheap check. | 2-plan.md:17-19,71-73; 1.5-criteria.md:19.
- **[R3-9, nitpick] The hammer's fire-on-known-true leg has no pre-stated run bound.** The lock-removed race is probabilistic; the skill's own rate-based rule pre-states run counts (METHODOLOGY.md:199-202). Failure is visible (P1 redesign path), so nitpick: add "within N hammer runs" to §B.4. | 2-plan.md:53-59; 1.5-criteria.md:13.

### Lens 4 — UNSTATED ASSUMPTIONS

- Assumed: mid-session `mv` refreshes subagent skill listings, and the listing is jsonl-visible — the load-bearing pair behind R2-3's fix; unverified → R3-3 (ranked under Lens 3).
- Assumed: the Agent tool's model alias resolves to exactly the pinned ids → R3-5 (ranked under Lens 2).
- Assumed: a second purity violation by a re-run verifier needs no disposition — same accepted class as round 2's quoteless residual (3-redteam-plan-round2.md:169), no structural driver pushes verifiers to roam twice; acceptable, noted as R3-10 (nitpick).
- Assumed: arm sandboxes can actually run `pytest` (the bug report and README direct arms at the tests, 2-plan.md:26-36); a missing runtime degrades both halves symmetrically and is visible in transcripts; acceptable, no finding.
- Blinding scope remains honestly pre-stated (2-plan.md:174-177); acceptable, no finding.

---

## Coverage challenge (behaviors the probe could get wrong that P1–P7 still do not cover)

1. **Offered-skill channel not actually closed by the `mv`** (listing-refresh + jsonl-visibility assumptions) — should be covered: one pre-baseline canary check pinned in P2/P7(a) (R3-3).
2. **An arm reading the run's own planning docs/oracle and "finding" the seeded bug** — should be covered: an arm no-roam jsonl check, the arm-side mirror of P4's verifier purity (R3-4); this is the only uncovered channel in the *pass-inflating* direction.
3. **Arms/verifiers silently running on a different model than pinned** — should be covered: record + match the resolved model id per jsonl (R3-5).
4. **The ground-free-decliner classification split** — must be covered by the frozen rule itself (one clause in §D, R3-1), not left to P4's dispute routing.
5. **A wrong-cause B1(b)** (new ending C: symptom exhibited, wrong cause asserted) — no criterion needed: the probe pre-declares it scores final-conclusion *gate hygiene* (2-plan.md:166-171), and the classification is deterministic; consider one sentence in §D acknowledging that accuracy is out of scope so the record cannot overclaim.
6. **A hammer that never fires on the lock-removed copy within a finite budget** — no new criterion needed: P1's "any failure = redesign" catches it; pre-stating a run bound (R3-9) removes the only discretion.
7. **Second purity violation by a re-run verifier / STOP-label naming** — accept as residuals (R3-10, R3-8): low likelihood, label-consequence-free respectively.

---

## Ranked findings

| # | Severity | Finding | Where |
|---|---|---|---|
| R3-1 | **major** | The B1(a)-vs-B2 precedence line omits B1(a)'s stated-ground condition; the ground-free decliner is mechanically classifiable B1(a) (precedence-governs, the paragraph's own operating principle) or B0 (definition-governs) — same determinacy class as R2-1/R2-2, on the Dragonfly half's flip edge, pass-inflating; one-clause fix ("…declines to conclude on B1(a)'s stated ground") | 2-plan.md:137-139,148-149,160-163; 1.5-criteria.md:15 |
| R3-2 | minor | §F's frozen arithmetic is unit-mixed (393 = bytes-joined; sentence = 387/384 chars) and the ≤152 bound is necessary-not-sufficient — full-date TO (148 chars) measurably needs 5 lines at width 103 (unbreakable pointer token); the month fallback fits 4 lines (101/102/99/94, measured) but its stated trigger never fires under the plan's own test | 2-plan.md:190-199; 1.5-criteria.md:17; SKILL.md:146-149 |
| R3-3 | minor | Phasing effectiveness unverified: `mv`-refresh of subagent skill listings and jsonl visibility of the listing are both assumed; a pre-baseline canary subagent settles both before arms burn | 2-plan.md:75-85; 1.5-criteria.md:14,19 |
| R3-4 | minor | No arm no-roam check — the plan (naming the seeded bug), oracle, and patch are reachable outside the arm's copy; the only uncovered pass-inflating channel; mirror P4's purity check onto arms | 2-plan.md:17-19,71-73; 1.5-criteria.md:16,19 |
| R3-5 | minor | Model pins (`claude-opus-4-8` arms, `claude-fable-5` verifiers) have no verification leg; record + match the resolved model id per jsonl for the standing probe's replay validity | 2-plan.md:70,75-77; 1.5-criteria.md:14,16,21 |
| R3-6 | nitpick | Stale doc headers ("REVISED after round 1") and stale §G (names round 2 as next; no round 3) | 1.5-criteria.md:1; 2-plan.md:1,205-211 |
| R3-7 | nitpick | Both-halves-fail rule still stated in both P3 and §E (in sync; N-4 residual) | 1.5-criteria.md:15; 2-plan.md:184-185 |
| R3-8 | nitpick | P7(d)'s "STOP for that half" names no outcome label (P7(a)'s does); label-consequence-free | 1.5-criteria.md:19 |
| R3-9 | nitpick | Hammer fire-on-known-true leg is a probabilistic race with no pre-stated run bound (skill's own rate-based precedent) | 2-plan.md:53-59; METHODOLOGY.md:199-202 |
| R3-10 | nitpick | Verifier purity re-run-once has no second-violation disposition (accepted class, no structural driver) | 1.5-criteria.md:16 |
| R3-11 | nitpick | Inference-plus-hedged-candidate ending needs three scattered clauses (B2 letter + categorical ANY-inference + B0's residual role) to resolve to B2; a "unless another class claims it" clause on the :152-154 B0 assignment would make it one-step | 2-plan.md:143-146,152-155,163-164 |

**Fix-verification summary:** all 12 round-2 fixes are genuinely applied and 11 of 12 fully resolve their findings; R2-1 is resolved for its target case but its fix line introduces R3-1 — the third consecutive extraction-rule-determinacy major at this gate, though now confined to a single clause with a pre-identified one-clause repair. R2-3's and R2-4's fixes stand with named minor residuals (R3-3, R3-2 — the latter measured, not estimated). The revised set is otherwise freeze-ready: the five prior edge cases and three of my five new stress endings classify deterministically, the phasing is mechanically checkable as performed, and a verified net-zero PASS path for the label flip exists via the month-precision fallback.

**Verdict: MAJOR — worst severity: one new flip-edge classification indeterminacy (R3-1, the ground-free decliner) introduced by the R2-1 fix line; fix the one clause (plus the four minors, all one-liners) before the gate-4 freeze.**
