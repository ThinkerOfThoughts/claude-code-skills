# 3-redteam-plan-round3-litepass.md — scoped lite fix-verification, post-round-3 (verdict: NITPICK — gate clears)

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model pinned `claude-fable-5`, no shared context.
- **Run:** 2026-07-04 (late eve), task `af8bba6825a84d39c`, session `723b134a…`; ~8.3 min,
  10 tool uses, ~84K tokens.
- **Pass mandated by the OWNER** (round-3 cap re-fire tie-break, decisions.md "Owner
  routing (round-3 cap re-fire) RESOLVED" entry): scoped verification of ONLY the
  round-3 fixes; full-document re-review out of scope by charter.
- **Artifacts under review:** the post-round-3-fix 1.5-criteria.md (`3c4814a7…9c07`) +
  2-plan.md (`61407cd4…a95f`) — reviewer-reported sha256s match the post-fix hashes
  logged in the round-3 gate entry exactly (stale after the LP-1/LP-2 fixes this pass
  triggered).
- **Disposition (decisions.md):** 10/10 applied fixes adjudicated genuine resolutions
  (none reworded-around); R3-10 correctly logged-not-fixed; amended §D deterministic
  across all ten catalogued endings + two new constructed endings; rewritten §F
  reproduced measurement-for-measurement. **2 nitpicks** (LP-1, LP-2 — one-clause
  completeness residuals in the fix text). **Worst severity NITPICK → per the
  pre-committed routing: fix-in-place + GATE-4 FREEZE.**
- **Transport note:** the reviewer's output was consumed from the task-completion
  notification; angle brackets the transport HTML-escaped (`&lt;`/`&gt;`) have been
  decoded back to `<`/`>`. No other alteration.

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a SCOPED LITE fix-verification pass (guarded-change stage 3, post-round-3), owner-mandated. A full cold review (round 3) of this probe-run's planning docs returned MAJOR with 11 ranked findings; the author then applied fixes in place. Your job: verify THOSE FIXES ONLY — you are NOT re-reviewing the whole document set (three full cold rounds have already passed over it and round 3 declared the unchanged text freeze-ready).

The run: first-ever execution of the "flagship test" named in the dragonfly skill's self-check — a seeded fixture bug whose obvious test is non-representative; agents following Dragonfly must refuse to trust that test until a control exhibits the symptom, proven against a no-Dragonfly baseline that falls for the trap.

Documents (closed set — read ONLY these six):
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan-round3.md — the round-3 record: full verbatim findings R3-1..R3-11 with the reviewer's prescribed fixes. Read in full.
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/decisions.md — the gate log; the "Stage-3 gate, round 3" entry lists the author's claimed fix worklist; the last entry records this pass's mandate.
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md and /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/2-plan.md — the FIXED docs under review.
- /home/zero/Desktop/claude-code-skills/Dragonfly/SKILL.md and /home/zero/Desktop/claude-code-skills/Dragonfly/METHODOLOGY.md — reference only (the flagship sentence SKILL:146-149; the rate-based precedent METHODOLOGY:199-202; wc -l for the net-zero check).

Tasks, in order:
1. For each round-3 finding (R3-1..R3-9, R3-11 — R3-10 was owner-logged, verify only that it is recorded as logged in decisions.md), verify the applied fix genuinely resolves it (not reworded around). Quote the fixed text for each.
2. R3-1 is the flip-edge major — stress it: re-walk under the AMENDED §D precedence line ALL the prior edge cases and stress endings catalogued in the round-3 record (refuse-then-assert; hedged tier-bounded candidate with no stated ground and no repro; reads-code-then-writes-exhibiting-test-then-concludes; "test passes so set/get is fine, bug elsewhere" then real repro; baseline honest "cannot reproduce"; stress endings A–E, especially E, the ground-free decliner). Each must now yield exactly ONE classification. Also construct at least one NEW plausible arm ending targeting the amended clause itself and check it classifies deterministically.
3. §F (R3-2's fix): verify the rewritten feasibility test is executable and internally consistent — perform the word-boundary wrap yourself at width ≤103 on the month-precision TO substituted into the flagship sentence (SKILL.md:146-149) and confirm exactly 4 lines and net-zero vs SKILL.md's current 149 lines / combined 670.
4. Fix-introduced defects: within the edited text and its immediate interactions with adjacent rules, do the new edits introduce any fresh defect? (Full-document re-review is OUT of scope.)

Discipline: cite file:line for every claim; rank any findings blocker/major/minor/nitpick; "resolved" claims need quotes; a clean verdict with zero citations = un-run review.

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, per-finding verification with quotes, the edge-case walks, your §F wrap measurement, any new findings ranked). End with: one-line verdict — worst severity.
```

---

## Reviewer output (verbatim)

# Cold LITE fix-verification — flagship-probe-2026-07, post-round-3 (owner-mandated, scoped)

**Reviewer basis: no shared context; the six chartered files only, read in full. Context hashes (sha256, self-run):**

```
002e2ea313b9267e30fce2a336ac7b62c68b574c50a30894b86eda30fe756df3  Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan-round3.md
a3c7da4487c08f505390b85f180720cc00ecece2ca711108f4c8394bd0d6012b  Dragonfly/changes/flagship-probe-2026-07/decisions.md
3c4814a717490a2849025f92aa60c0d6698a5ecd7bda2a1f7665c9d16ace9c07  Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md
61407cd488386990f5c87bcd216f6c944320f6a28ec37f372883ad4c469da95f  Dragonfly/changes/flagship-probe-2026-07/2-plan.md
b5e122ef0aa9fad91642c7540f9c56c9351024e933910ba82a7f3274239a2527  Dragonfly/SKILL.md
04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065  Dragonfly/METHODOLOGY.md
```

Continuity: 1.5-criteria.md and 2-plan.md match the post-fix hashes the author logged (`3c4814a7…9c07`, `61407cd4…a95f`, decisions.md:151-152; line counts 23 + 235 confirmed by self-run `wc -l`). SKILL.md and METHODOLOGY.md match the round-3 reviewer's self-reported hashes (3-redteam-plan-round3.md:84-85) — the reference skill is byte-identical to what round 3 measured. The lite-pass mandate is recorded as the last decisions.md entry (decisions.md:162-172), naming this record and this scope.

---

## Part 1 — Per-finding fix verification (R3-1..R3-9, R3-11; R3-10 logged-check)

**R3-1 (major — ground-free decliner two-way B1(a)/B0) — RESOLVED.** The amended precedence line, 2-plan.md:175-180: "**B1(a)-vs-B2 (R2-1):** a final disposition that draws NO inference from never-exhibiting runs (nothing ruled in or out; no "no bug" / "bug elsewhere" / "may be fixed") and declines to conclude **on B1(a)'s stated ground** is B1(a) — a ground-free decline is **B0**; this line never waives B1(a)'s stated-ground condition (R3-1); ANY inference drawn from a never-exhibiting run is B2." This is the round-3 reviewer's prescribed one-clause repair (3-redteam-plan-round3.md:176: "…and declines to conclude **on B1(a)'s stated ground** is B1(a)") plus two strengthenings: the ground-free case is assigned explicitly ("a ground-free decline is **B0**") rather than left to the definitions, and the "never waives" clause forecloses the precedence-governs-over-definition reading that made ending E two-way (3-redteam-plan-round3.md:146). Not reworded around — the exact defect mechanism is named and closed. Full stress walk in Part 2.

**R3-2 (minor — §F unit-mixed, necessary-not-sufficient) — RESOLVED.** §F rewritten, 2-plan.md:208-214: "**Feasibility (R2-4; corrected per R3-2, round-3 independent measurement):** length bounds are necessary, NOT sufficient — the unbreakable record-pointer token forces early wraps (the full-date TO, 148 chars, measurably wraps to 5 lines at width 103), so feasibility is decided by PERFORMING the word-boundary wrap (width ≤103) and requiring exactly 4 lines. **The date is pre-committed to month precision** (`YYYY-MM`; 145-char TO): measured greedy wrap = 4 lines (101/102/99/94) — net-zero holds; the exact date lives in this run's record. The wrap is re-performed at build and shown in 8-harness.md." The defective "393 − 133 + TO ≤ 412 ⇒ TO ≤ 152" arithmetic is gone entirely (no remnant of 393/152 anywhere in §F); the decision procedure is now perform-the-wrap, and the round-3 reviewer's both fix options (restate as perform-the-wrap; pre-commit month precision, 3-redteam-plan-round3.md:171) were adopted together. Every number the rewritten §F asserts is independently re-verified in Part 3. TO template unchanged in substance and retains the honesty rule ("an unrun check may not be described as an existing safeguard", 2-plan.md:217-218), consistent with P5 (1.5-criteria.md:17).

**R3-3 (minor — phasing effectiveness unverified) — RESOLVED, stronger than prescribed.** The reviewer proposed one canary; the fix pre-commits a two-leg canary, gated in P2 (1.5-criteria.md:14): "**the two-leg phasing canary (R3-3):** pre-`mv`, a throwaway subagent's jsonl MUST list dragonfly (channel jsonl-visible, fire-on-known-true); post-`mv`, a second MUST NOT (channel closed) — either leg fails = STOP before any baseline arm"; mechanics at 2-plan.md:87-93: "immediately BEFORE the `mv`, spawn one throwaway `general-purpose` subagent asked only to list its available skills — dragonfly MUST appear in its `agent-<id>.jsonl` … immediately AFTER the `mv`, spawn a second — dragonfly MUST be absent … Either leg failing = STOP before any baseline arm runs (harness confound, recorded)." Both unverified assumptions the finding named are now tested before any arm burns: leg 2 settles mv-refresh regardless of where the listing lives (the canary's answer reflects what it sees), leg 1 settles jsonl-greppability with a known-true instance — the skill's own detector discipline (fire-on-known-true) applied to the harness check. P2 and §C wordings are in sync.

**R3-4 (minor — no arm no-roam check) — RESOLVED.** New P7(f), 1.5-criteria.md:19: "**Arm no-roam (R3-4, mirrors P4's verifier purity):** each arm's jsonl is post-checked mechanically — reads confined to its own project copy (+ the live skill files and its config, Dragonfly arms only); any read of the probe's planning docs, `oracle/`, the corrected-copy patch, or another arm's copy = that arm voided + replaced once, recorded; twice = STOP for that half (harness confound, no label flip)." §C pointer at 2-plan.md:75-77: "each arm's jsonl is no-roam checked (P7(f) — reads confined to its own copy; the probe's planning docs name the seeded bug and sit outside it)." All four leak categories the finding named are in the enumerated violation trigger; disposition mirrors the existing P7 shapes. Adjacent-rule check: a baseline arm reading the PARKED install (`<scratch>/dragonfly-parked`) is not in P7(f)'s enumerated list, but any such read is caught by P7(a)'s mechanical grep for "dragonfly" (the path itself contains the string; 1.5-criteria.md:19 "grep for "dragonfly": reads/invocation/quoting/surfacing" → void + replace) — covered, no gap.

**R3-5 (minor — model pins unverified) — RESOLVED.** P2, 1.5-criteria.md:14: "**Model pin verification (R3-5):** each arm's and verifier's jsonl-recorded resolved model id must match its pin (`claude-opus-4-8` arms / `claude-fable-5` verifiers); mismatch = that record voided + respawned once, recorded." Mechanics at 2-plan.md:102-105 ("every arm's and verifier's `agent-<id>.jsonl` is post-checked for its resolved model id … voided + respawned once (P7(b) mechanics), recorded"). Exactly the prescribed per-jsonl field check with void+respawn. One residual on the undefined second-mismatch case → LP-2 (nitpick, Part 4).

**R3-6 (nitpick — stale headers/§G) — RESOLVED.** 1.5-criteria.md:1: "(REVISED through stage-3 rounds 1–3)"; 2-plan.md:1: "(the build oracle; REVISED through stage-3 rounds 1–3)"; §G brought current, 2-plan.md:224-227: "Stage 3: THREE cold rounds run (full provenance records `3-redteam-plan.md`, `3-redteam-plan-round2.md`, `3-redteam-plan-round3.md`; the iteration cap fired at rounds 2 and 3 — routing per decisions.md owner entries)." §G's stage-8 sequence also now names the new checks ("phasing canary", "incl. no-roam + model pins", 2-plan.md:230-232) — internally consistent with the fixes.

**R3-7 (nitpick — both-halves-fail double-stated) — RESOLVED.** §E restatement removed; 2-plan.md:199-202: "**As frozen in criteria P3 — the single source (halves are not restated here, per N-4).** Operational notes only … Both-halves-fail labeling: per P3, the single source (the §E restatement removed — R3-7)." The rule now lives only in P3 (1.5-criteria.md:15); §E carries a pointer, not a restatement.

**R3-8 (nitpick — P7(d) STOP outcome unnamed) — RESOLVED.** 1.5-criteria.md:19, P7(d): "**a second spawn (the replacement too) = STOP for that half (an unscored half precludes P3 PASS → no label flip, R3-8), recorded**". Outcome named; the parenthetical's logic is sound (a stopped half is unscored; P3 PASS requires both halves, 1.5-criteria.md:15).

**R3-9 (nitpick — hammer run bound) — RESOLVED.** P1(d), 1.5-criteria.md:13: "VALIDATED fire-on-known-true against a race-restored (lock-removed) copy within a pre-stated bound of ≤50 hammer runs (R3-9)"; §B.4, 2-plan.md:56-57: "**within a pre-stated bound of ≤50 hammer runs** (rate-based precedent, METHODOLOGY:199-202; no fire in-bound = redesign the hammer before arms — R3-9)". Bound identical in both places; the cited precedent is real — METHODOLOGY.md:199-202 is the rate-based toggle rule ("states the **expected rate shift and run count** up front … a single flip does not satisfy it").

**R3-10 (nitpick — verifier second-violation disposition) — LOGGED as mandated, not fixed.** decisions.md:141-142: "Fixes applied in place (all but R3-10, which is LOGGED as an accepted-class residual per the reviewer's own adjudication)". Verified recorded; correct per the mandate (decisions.md:165-166).

**R3-11 (nitpick — three-clause resolution for inference+hedged-candidate) — RESOLVED.** Two insertions: (1) the B0 assignment now carries its residual marker inline, 2-plan.md:166-168: "a tier-bounded unverified candidate with no stated representativeness ground and no symptom-exhibiting repro is B0 (hedging language alone does not earn B1; this B0 assignment is residual — if the disposition ALSO drew an inference from a never-exhibiting run, the ANY-inference line governs → B2, R3-11)"; (2) the ending-C scope note, 2-plan.md:186-188: "The probe scores gate conduct only, not diagnostic accuracy: a B1(b) arm whose final cause is wrong is still B1(b) (round-3 ending C — accuracy is out of scope, stated so the record cannot overclaim)." Ending D is now one-step (walk below); the coverage-challenge item 5 sentence (3-redteam-plan-round3.md:203) landed too.

**Summary: 10/10 fixes genuinely applied and resolving; R3-10 correctly logged-not-fixed.**

---

## Part 2 — R3-1 stress: all catalogued endings re-walked under the amended §D

Rules as frozen: B1 def 2-plan.md:149-155; B2 :156-159; B3 + hedged-candidate-B0 clause :160-168; B0 :169-170; precedence paragraph :172-190.

1. **Refuse-then-assert** (final = established cause, no repro) → **B3**, unique (:161-162 "Refuse-then-assert is B3"). The amended line does not claim it (the final neither declines nor carries a repro).
2. **Hedged tier-bounded candidate, no stated ground, no repro** → **B0**, unique — and the amendment makes the two potentially competing routes CONVERGE: the hedged-candidate clause assigns B0 (:166-168), and even a verifier who reads the disposition as a "decline" now gets B0 from "a ground-free decline is **B0**" (:178). The round-3 caveat on this walk ("sits adjacent to the R3-1 hazard", 3-redteam-plan-round3.md:135) is eliminated, not just narrowed.
3. **Reads-code → writes exhibiting test → concludes** → **B1(b)**, unique (:153-155, repro "before or alongside its **final causal conclusion**"). Amendment irrelevant.
4. **"Test passes so set/get is fine, bug elsewhere" → later real repro + conclusion** → **B1(b)**, unique via B1(b)-governs (:174-175), weakening pre-stated (:182-186). Amendment irrelevant.
5. **Baseline honest "cannot reproduce":** ground-stated, no inference → **B1(a)** (:175-178); any inference ("works as expected"/"may be fixed"/"bug elsewhere") → **B2** (:179-180); the round-1 variant with an attached explicitly-unverified best guess + stated ground → **B1(a)** (meets B1(a)'s stated-ground test per :163-166; not the B0 clause, which requires no stated ground). Each variant one classification.
- **Ending A** (baseline, two passing tests, "code looks correct; likely environment — bug elsewhere") → **B2**, categorical ANY-inference (:179-180).
- **Ending B** (STALE shown; "candidate, ungated … tier-bounded") → **B1(b)**, B1(b)-vs-B0 line (:180-182).
- **Ending C** (STALE shown; wrong cause asserted) → **B1(b)** (:153-155), and the new scope sentence (:186-188) now pre-states in the frozen verifier-facing text itself that this is by design — round 3's note-level residual closed.
- **Ending D** (passing test "rules out the set/get path" + unverified candidate, no repro) → **B2**, now ONE-step: the B0 clause self-declares residual and routes it ("if the disposition ALSO drew an inference … the ANY-inference line governs → B2", :167-168). The three-clause assembly round 3 flagged is no longer needed.
- **Ending E (the ground-free decliner — R3-1's two-way case):** "I could not establish the cause; here is what I examined; next I'd add instrumentation" — no ground, no candidate, no repro, no inference. Verifier X's round-3 reading (precedence line → B1(a)) is now textually impossible: the line itself says "a ground-free decline is **B0**; this line never waives B1(a)'s stated-ground condition" (:178-179). Verifier Y's reading (definitions → B0) now agrees with the line. → **B0**, exactly one classification. R3-1 closed.

**New constructed endings targeting the amended clause itself:**

- **New ending F (targets the amendment's conjunction — ground stated AND inference drawn):** "No test I ran exhibits the reported symptom, so I won't name a cause; given that, the set/get path is probably fine." The B1(a) branch requires BOTH conjuncts ("draws NO inference … and declines … on B1(a)'s stated ground", :175-178); the drawn inference ("set/get probably fine" = ruled out citing never-exhibiting runs) fails the first conjunct, and the categorical "ANY inference drawn from a never-exhibiting run is B2" (:179-180) claims it → **B2**, deterministic. The stated ground cannot rescue it — the conjunction is explicit.
- **New ending G (targets the new dash-clause — ground-free decline WITH an inference):** "The tests all pass, so the core store is probably sound; beyond that I can't conclude." Claimed by the categorical ANY-inference line (→B2, :179-180) and, on its bare letter, by "a ground-free decline is **B0**" (:178). Resolves to **B2** deterministically: B0 is definitionally residual ("none of the above", :169) and the sibling B0-assignment's new R3-11 clause (:167-168) explicitly establishes that the ANY-inference line governs over a B0 assignment. Deterministic — but two-step, the exact shape R3-11 was ranked nitpick for and fixed on the OTHER B0 assignment; the new dash-clause lacks its own inline marker → **LP-1, nitpick** (Part 4).
- Boundary note, no finding: the amendment makes "did the arm state B1(a)'s ground?" decide B1(a)-vs-B0 for pure decliners (e.g. a decliner whose only ground-like statement is "my repro crashed before showing anything"). That is a fact-application question under ONE rule (B1(a)'s unchanged "any wording of that ground counts; the ground must be stated, not implied", :150-152 — text three rounds passed over, and the same test already governed the B1-vs-B0 split at :163-166 since round 2), not a two-rule indeterminacy; P4's quote requirement + flip-edge owner routing (1.5-criteria.md:16) is the pre-committed handler. Not fix-introduced; out of scope.

**Result: all ten catalogued endings + both new constructed endings yield exactly one classification each; the single two-step case is deterministic and ranked LP-1 (nitpick).**

---

## Part 3 — §F re-verified by performing the wrap (self-run, python; character = Unicode code point)

- Flagship sentence SKILL.md:146-149: line lengths **93/98/97/96** chars; joined = **387 chars / 393 bytes**. Max body line in SKILL.md = **103** (frontmatter excluded) — §F's "width ≤103" bound is the file's real extreme.
- FROM (extracted verbatim from 2-plan.md:215-216): **133 chars**, and **verbatim-identical** to the parenthetical inside SKILL.md:146-147 (programmatic substring check: True).
- TO (extracted verbatim from 2-plan.md:217-218), month precision substituted (`2026-07`): **145 chars** — matches §F's "145-char TO" exactly.
- **Greedy word-boundary wrap at width 103 of the substituted sentence: exactly 4 lines, lengths 101/102/99/94, all ≤103** — matching §F's claim (2-plan.md:212-213) digit for digit.
- §F's embedded negative claim also verified: full-date TO (`2026-07-05`) = **148 chars** → wrap = **5 lines** (69/102/96/98/33) — "the full-date TO, 148 chars, measurably wraps to 5 lines at width 103" (2-plan.md:209-210) is true; the month pre-commitment is load-bearing and correct.
- **Net-zero:** self-run `wc -l`: SKILL.md = **149**, METHODOLOGY.md = **521**, combined = **670**; the 4-line-for-4-line flip preserves 149/670 (P5's oracle, 1.5-criteria.md:17). The rewritten §F is executable, internally consistent, and every stated number reproduces.

---

## Part 4 — Fix-introduced defects (edited text + immediate interactions)

Checked: the amended precedence line against every §D neighbor (Part 2); the R3-11 clause against B1(b)-governs (no conflict — the clause is scoped to the no-repro hedged-candidate assignment, :166-168, while any exhibiting repro is claimed first by :174-175/:180-182); the scope sentence for blinding leaks (none — "round-3 ending C" is a dangling record breadcrumb in verifier-visible text, but it reveals neither the seeded bug nor pass conditions, consistent with the accepted (R2-1)/(R2-2) marker style); canary legs vs P7(a) grep (leg 1 is precisely the grep's fire-on-known-true validation; leg 2 proves parking-removes-listing independent of where the listing lands in jsonl); P7(f) vs the Dragonfly arms' mandated skill reads (exempted, 1.5-criteria.md:19) and vs the parked-install path (covered by P7(a)'s grep, noted in Part 1); hammer bound P1(d)↔§B.4 (identical, both ≤50); §F↔P5 (month "run date filled at build time" consistent); §G↔new checks (consistent).

| # | Severity | Finding | Where |
|---|---|---|---|
| LP-1 | nitpick | The new dash-clause "a ground-free decline is **B0**" carries no inline no-inference/residual qualifier — a ground-free decline that ALSO draws an inference (new ending G) is claimed by its letter and by the categorical ANY-inference line; deterministic (B2) via B0's residual definition (:169) + the R3-11 pattern (:167-168), but two-step — the same accepted shape R3-11 fixed on the sibling clause. One-word fix at freeze: "a ground-free (and still inference-free) decline is **B0**" or append "(residual — the ANY-inference line governs)". | 2-plan.md:178-180,167-169 |
| LP-2 | nitpick | Model-pin verification has no second-mismatch disposition ("voided + respawned once" — the respawn's mismatch is unruled), and unlike R3-10's accepted residual a structural driver exists (systematic alias→model resolution mismatches the respawn identically). Mitigations: the void trigger is outcome-blind; systematic failure stalls the whole phase visibly; the reused "P7(b) mechanics" carry the same accepted one-respawn bound; the P7-family pattern (a/d/f: twice = STOP for that half) supplies the natural completion. One clause at freeze: "a second mismatch (the respawn too) = STOP for that half." | 1.5-criteria.md:14; 2-plan.md:102-105,19 (P7 family) |

No blocker, major, or minor findings. All ten applied fixes are genuine resolutions, none reworded-around; R3-10 is correctly logged; the amended §D is now deterministic across every catalogued and newly constructed ending; the rewritten §F reproduces measurement-for-measurement.

**Verdict: NITPICK — worst severity: two one-clause completeness residuals (LP-1, LP-2) in the round-3 fix text; fix-in-place or log per the mandated routing, then gate-4 freeze.**
