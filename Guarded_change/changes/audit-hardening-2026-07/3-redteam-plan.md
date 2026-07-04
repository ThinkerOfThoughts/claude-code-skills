# 3 — Red-team of {1-spec, 1.5-criteria, 2-plan} — ROUND 1 (verbatim record)

> Round 2 (post-re-plan verification + fresh attack) is preserved verbatim in
> `3-redteam-plan.round2.md`. Verdict there: 23/23 round-1 findings RESOLVED; 12 new findings
> (6 minor, 6 nitpick) fixed in place; MINOR → proceed to build.

> Provenance (F1 dogfooded ahead of law): reviewer = cold `general-purpose` subagent, no shared
> context, model claude-fable-5 (inherited from session). Context given (closed set): the four
> change docs ({0-audit-findings, 1-spec, 1.5-criteria, 2-plan}) + redteam_context
> {METHODOLOGY.md, SKILL.md, changes/concurrency-lens/{decisions,8-harness}.md (+ it also
> consulted concurrency-lens 1.5/2, live copies, git state — within scope)}. No supplementary
> author context. Charter: four lenses + evidence discipline per METHODOLOGY, task-aimed
> questions quoted below. Consumer spot-verify: FA-1's grep re-run by the author — confirmed
> ("redundant" absent from precedent; precedent 1.5 L13 = strict differential pass);
> METHODOLOGY table-columns / "un-run" / SKILL step-3 citations checked against the author's
> full read — all hold.

## The verbatim prompt given to the reviewer

```
You are a cold, independent red-team reviewer with NO shared context with the author of the
artifacts you are reviewing. Your job is to attack a plan before it is built. You are graded on
PRECISION (are your findings real?), not on how many findings you raise. "No issue found" on a
lens is a valid, expected answer when true.

## The artifacts under review (read all four, in this order)

1. .../changes/audit-hardening-2026-07/0-audit-findings.md (the input audit)
2. .../changes/audit-hardening-2026-07/1-spec.md
3. .../changes/audit-hardening-2026-07/1.5-criteria.md
4. .../changes/audit-hardening-2026-07/2-plan.md

## The source you must check claims against (redteam_context, priority order)

1. ~/Desktop/claude-code-skills/Guarded_change/METHODOLOGY.md — the CURRENT methodology the
   plan proposes to amend. The plan's claims about what the methodology currently lacks, where
   sections live, and what existing rules say MUST be checked against this file, line by line
   where cited.
2. ~/Desktop/claude-code-skills/Guarded_change/SKILL.md — the current operating procedure,
   same treatment.
3. .../changes/concurrency-lens/decisions.md and 8-harness.md — precedent run the plan cites
   (C3 attempt-1 confound, "redundant-but-harmless" precedent, replay A/B design). Verify the
   precedent claims are real.

The change: amend METHODOLOGY.md + SKILL.md with nine additive fixes (F1–F9 in the audit doc).
Constraints claimed: additive only, terse (the executing model is Opus and the docs are an
attention budget), no structural rework, both source and live copies must end identical.

## Your charter — attack on four SEPARATE lenses

1. FACTUAL — do the spec/criteria/plan's claims match the source? Every claim about "the
   methodology currently has no rule for X", every cited precedent (e.g. "C3 attempt-1
   confound"), every line-location claim. Cite file:line for everything you check. A clean
   factual verdict is ONLY valid if you show the specific evidence you consulted (file:line).
   A clean factual verdict with zero citations will be treated as an un-run review.
2. LOGICAL — flaws in the plan's reasoning or sequencing, independent of the text: Does the
   edit-mapping actually close each finding, or does a loophole survive the fix as written?
   Are the six contradiction-sweep reconciliations sound? Is the C3 replay A/B design valid as
   an experiment (would a pass actually demonstrate what it claims? is there
   leading-the-witness or confounding, per the attempt-1 precedent)? Is the freeze-point
   definition (F4) exploitable? Do any of the nine fixes interact badly with each other?
3. MISSED OPPORTUNITY — better or cheaper approaches left on the table; places where a fix
   could be strengthened at no extra bloat cost; findings the audit itself missed that belong
   in this same hardening pass (you are also auditing the audit).
4. UNSTATED ASSUMPTIONS & RISKS — what is being taken for granted that could be false?
   Specifically consider: the position-sensitivity treatment (the docs are prompt-like; the
   change ADDS text — is the C3-fixture "old rule V3 still fires" probe actually sufficient
   evidence that insertions didn't displace existing behavior?); whether n=2 per arm is
   adequate for the claimed pass condition; whether the fixture design described in 2-plan.md
   can produce a false PASS or false FAIL; whether "terse, mechanical, Opus-friendly" is
   actually satisfied by the proposed substance; whether the bloat cap numbers are coherent.

Also, per the plan's own request: challenge the C3 FIXTURE DESIGN specifically (the seeded
V1/V2/V3 violations) — is each violation cleanly isolating? Could a reviewer flag it for the
wrong reason, or miss it for a benign reason? Is the neutral question wording actually neutral?

## Evidence discipline

- Every finding: cite file:line (of the reviewed docs or the source) or give a concrete
  failure scenario.
- Rank EVERY finding: blocker / major / minor / nitpick.
- Flag anything you could not verify as UNVERIFIABLE rather than silently accepting it.
- Structure your output as: per-lens findings (or per-lens "no issue found + evidence
  consulted"), then a ranked summary table, then a one-paragraph bottom line with your
  worst-severity verdict.

Your final message is consumed as the raw review record and will be preserved verbatim —
return the full review, not a summary of it.
```

## The reviewer's verbatim output

[Preserved in full below — this is the raw review record.]

# Cold red-team review — audit-hardening-2026-07 (stage 3: spec + criteria + plan)

Reviewer: cold subagent, no shared context with the author. Sources consulted: the four artifacts under review; `METHODOLOGY.md` (467 lines, verified by `wc -l`); `SKILL.md` (102 lines, verified); `changes/concurrency-lens/decisions.md`, `8-harness.md`, and (for pass-condition verification) `1.5-criteria.md`/`2-plan.md` of that run; live copies at `~/.claude/skills/guarded-change/` (diffed against source: currently identical, both files); git state of the skills repo (HEAD `8a7ac65`, working tree clean on the two files).

---

## Lens 1 — FACTUAL

### FA-1 (MAJOR) — The "redundant-but-harmless … per concurrency-lens C3 precedent" citation misstates the precedent, and the misstatement is load-bearing.

- `1.5-criteria.md:16` — "(if control also catches V1/V2, record as 'redundant-but-harmless', per concurrency-lens C3 precedent)"; `2-plan.md:42-43` — "control catching V1/V2 → record 'redundant-but-harmless', qualified pass per concurrency-lens precedent."
- The phrase **appears nowhere in the precedent record**: `grep -rn "redundant" changes/concurrency-lens/` returns zero hits across all six files.
- The precedent's actual pass condition says the **opposite**: `concurrency-lens/1.5-criteria.md:13` — "Pass = treatment catches it **and** control (historical or fresh) does not. **Fail** = guard doesn't move the outcome → not representative."
- What the precedent actually established: (i) an all-arms-catch pattern was treated as a **suspected-and-confirmed confound and discarded** (`concurrency-lens/decisions.md:72-82`, attempt 1 "CONFOUNDED, discarded"), not recorded as benign redundancy; (ii) a qualified pass was granted only when **differentiation was still demonstrated** — control 1/2 missed ("a would-have-shipped outcome"), `decisions.md:83-92`, with the limitation named.
- The new plan cites this precedent to justify pre-authorizing a pass when controls catch V1/V2 — including 2/2 controls catching, i.e. zero demonstrated differentiation. The precedent supports no such disposition. See LO-1 for the consequence.

### FA-2 (MINOR) — "caught only by author honesty, not by any rule" (audit `0-audit-findings.md:25-26`) is half-true.

Detection of the attempt-1 confound came from a **rule firing**: "The fresh control caught it → strict C3 pass condition (treatment catch AND control miss) NOT met" (`concurrency-lens/decisions.md:77-78`); the rule is `concurrency-lens/1.5-criteria.md:13`. Author honesty supplied the *diagnosis* (leak, not redundancy), not the *detection*. This matters because the new C3 design deletes exactly that detecting rule (LO-1) — the audit's misattribution hides what the precedent's tripwire actually was.

### FA-3 (MINOR) — The plan contradicts itself on expected deletion hunks.

`2-plan.md:46-47`: "deletion hunks justified (**only F9's sentence rewrite is expected**)." But the plan's own F3 row (`2-plan.md:13`) extends the verification-table column list "in place, same paragraph, one sentence" (sweep item 5, `2-plan.md:28`) — the column list is an existing sentence at `METHODOLOGY.md:347-348`, so extending it produces a deletion+addition hunk. Likewise every SKILL "one clause" wired into an existing bullet (e.g. step 8's conformance bullet, `SKILL.md:73-76`). The C6 expectation will either false-alarm at stage 8 or train the verifier to wave deletion hunks through — both bad for a gating criterion.

### FA-4 (MINOR) — C4's numbers are internally incoherent.

`1.5-criteria.md:17`: "≤ +25% per file and ≤ +18% combined (METHODOLOGY 467 → ≤560; SKILL 102 → ≤128; combined 569 → ≤671)". Verified baselines: 467/102/569 correct (`wc -l`). But: 467 × 1.25 = 583, not 560 (560 is +19.9%); 102 × 1.25 = 127.5, so **≤128 is +25.5% — it violates the stated percentage**; and 560 + 128 = 688 > 671, so the per-file parentheticals are jointly unreachable under the combined cap. Which bound governs at stage 8 is ambiguous at the exact boundary. State the governing rule (suggest: the absolute numbers govern, and fix 128→127 or restate the percentages as the derived ones).

### Clean factual verdicts — earned, with the evidence consulted:

- **F1's current-state claim true**: no provenance requirement exists — `METHODOLOGY.md:436` ("3-redteam-plan.md cold review of {1,1.5,2} with ranked findings" — no embed duty); `SKILL.md:57-62` (charter instructions; nothing requires embedding the verbatim prompt/context/output).
- **F2 true**: the representativeness challenge lives in the charter (`METHODOLOGY.md:230-232`), which runs only at stages 3/6; no rule reviews post-6 artifacts.
- **F3 true**: table columns at `METHODOLOGY.md:347-348` are *criterion │ gating/advisory │ path exercised │ verified by execution? │ result* — no evidence column; no raw-output retention rule anywhere (grep for retention/preserve: none).
- **F4 true**: grep for "freeze/frozen" across both files: zero hits.
- **F5 true**: `METHODOLOGY.md:181` routes "by the worst finding's severity" and is silent on whose severity binds; `SKILL.md:24-27` has the author writing the severity into decisions.md.
- **F6 true**: `METHODOLOGY.md:390-397` (standing priority-ordered config); `SKILL.md:67` ("code diff/files" — hand-assembled, no mechanical-generation rule).
- **F7 true**: charter lenses and discipline bullets (`METHODOLOGY.md:198-262`) contain no criteria-coverage challenge.
- **F8 true**: `SKILL.md:14-18` and `METHODOLOGY.md:385-424` contain no run-time path validation. (The "deleted install" precedent is outside the provided sources — **UNVERIFIABLE** here, but immaterial to the fix's merit.)
- **F9 true**: `SKILL.md:99-102` "…is encouraged after any edit to either file"; no standing criteria; METHODOLOGY (full read) has no self-check section, so the plan's "(none — self-check lives in SKILL)" (`2-plan.md:19`) is correct.
- All mapping-table **location claims exist**: charter `:190-264`; "What a run produces" `:427-453`; stage-8 table paragraph `:346-355`; severity table `:270-275`; stage-1 `:114-115`; config Rules `:414-424`; SKILL steps 1/1.5/3/4/6/7/8 and Inputs/self-check at `SKILL.md:33,34-50,57-62,63-65,67-69,70-71,72-83,13-18,97-102`.
- Plan's threshold restatement (`2-plan.md:56`) matches `METHODOLOGY.md:270-275`.
- The audit's "467+102 lines" (`0-audit-findings.md:113`) is exact.

---

## Lens 2 — LOGICAL

### LO-1 (MAJOR) — C3's auto-benign control-catch disposition removes the exact tripwire that caught the attempt-1 confound.

Pass = treatment 2/2 flag all three; control behavior does not gate (`2-plan.md:41-43`). Therefore C3 can record **PASS with all four reviewers catching everything** — the outcome pattern that in attempt 1 signaled a leaked/leading harness (`concurrency-lens/decisions.md:72-82`) — and the pre-authorized disposition is "record redundant-but-harmless," not "investigate." A fixture leak, a leading question, or control-doc contamination (AR-2) would be invisible: no rule in this design ever forces the question "why did a control cite a rule that doesn't exist in its docs?" Concrete repair, one sentence: *a control flagging V1/V2 while citing a rule absent from the current docs, or 2/2 controls catching a new-rule violation, is treated as a suspected harness confound and investigated before any disposition is recorded* (this is precisely the precedent's lesson, restored).

### LO-2 (MAJOR) — Fixture violation co-location breaks isolation; the plan is also ambiguous about where V3 lives.

`2-plan.md:35-37`: "(`3-redteam-plan.md` missing provenance = V1; `8-harness.md` with a gating PASS row lacking evidence = V2 and a 'clean factual, no citations' **stage-3 verdict** = V3)" — grammatically V3 sits in `8-harness.md`, but a stage-3 verdict belongs in the stage-3 doc; the criteria (`1.5-criteria.md:16`) don't resolve it. On the sensible reading (V3 in the stage-3 doc), **V1 and V3 co-locate in one document, and each independently invalidates the whole review** (F1's consequence: "the review is treated as un-run," `2-plan.md:11`; V3's existing rule: "treated as an un-run review," `METHODOLOGY.md:215-217`). A treatment reviewer who invalidates the doc citing the provenance rule has fully answered the question ("List **any** that must be treated as un-run… citing the rule") with no reason to enumerate the second ground → benign V3 miss → **false FAIL** of the position-lens probe; a lenient grader counting "doc flagged = both caught" → **false PASS** on V1. Worse, a V3 catch inside a document already invalidated by V1 is *not* independent evidence the old rule still fires. Repair: one violation per artifact — e.g. stage-3 doc with missing provenance but a properly-cited factual lens (V1 only); a separate `6-redteam-code.md` with provenance intact but a citation-less clean factual verdict (V3 only); `8-harness.md` carries V2 only — and make the pass condition require the correct rule citation per violation (the question already asks for it; the pass condition at `2-plan.md:41-42` doesn't).

### LO-3 (MAJOR) — V2 does not cleanly isolate F3: the current docs already give a control a legitimate path to flag it.

Current text: "every gating `verified = yes` must have exercised the path the criterion actually governs — challenge any verified against a proxy" (`METHODOLOGY.md:227-229`); "A gating criterion whose label or verification **cannot survive this challenge is treated as unverified**" (`:233-234`); and the earned label-audit requires showing "which governed path it confirmed was exercised and **what evidence it checked**" (`:237-240`). A diligent control gate-consumer confronting a bare PASS row can already declare it unverified under these rules. So the plan's expectation "controls expected to flag V3 only" (`2-plan.md:42`) is textually unsupported for V2, every control V2-catch is absorbed by the benign disposition (LO-1), and C3's *demonstrated* marginal value likely reduces to V1 alone at n=2. Partial repair in fixture design: make the V2 row maximally survivable under current text (plausible "path exercised" narrative, execution claimed, only the raw-output pointer absent) so F3's mechanical rule is the sole differentiator — and record honestly that F3 may verify as codification rather than new behavior.

### LO-4 (MAJOR) — The F4 freeze point is exploitable and has no mechanical anchor.

Freeze = "when gate 4 routes to build" (`2-plan.md:14`, sweep item 2 at `:25`). The gate-4 route line is written by the **author** (`SKILL.md:24-27`). Window: stage-3 review returns → author edits `1.5-criteria.md` → author logs "gate 4: clean → build." The edit is post-review, pre-freeze, unlogged, and stage 8 verifies against criteria stage 3 never saw — the exact scenario F4 targets, surviving the fix as written. Also, nothing detects a post-freeze edit at all (no hash/copy/commit requirement; detectability rests on the same convention S3 flags). Repair, one clause: the freeze binds to **the criteria version the stage-3 reviewer read** (record its hash or verbatim copy at gate 4); any divergence between that version and the file at stage 8 = post-freeze edit.

### LO-5 (MAJOR) — F7 (and, milder, F8) has a trigger and requirement but no consequence — unenforceable by the run's own standard.

The run's constraint: rules must be "explicit, mechanical, and checkable" (`0-audit-findings.md:8`); C1's own schema demands "trigger + requirement + consequence" per row (`1.5-criteria.md:14`). The F7 row (`2-plan.md:17`) has no consequence: if a stage-3 review simply omits the coverage challenge, nothing notices — recreating the audit's own meta-pattern ("a check existed but was not actually exercised," `0-audit-findings.md:11-12`). Two of nine rows therefore cannot fully satisfy C1 as C1 is written. Repair, one clause: *a stage-3 review with no coverage-challenge section (an explicit "none found" counts) is incomplete on lens 4 and treated as un-run for that lens* — the same "earned clean" pattern the factual lens (`METHODOLOGY.md:213-217`) and label-audit (`:236-240`) already carry.

### LO-6 (MINOR) — Sweep item 4's routing for F2 findings is awkward.

"Findings from it route through gate 8" (`2-plan.md:27`) — but gate 8's blocker/major routes go to 1 or 2 (`METHODOLOGY.md:270-275`), and a defective *harness* needs neither a new spec nor a new plan; the precedent handled it as discard-and-rebuild in place (`concurrency-lens/decisions.md:80-82`). Not incoherent (minor→fix-in-place covers most cases), but the reconciliation should name the rebuild-the-check path so a defective fixture doesn't nominally demand a loop restart.

### LO-7 (MINOR) — "≥2 per arm" vs "2/2 reviewers" is undefined for n>2, and there is no resampling protocol.

`1.5-criteria.md:16` says "(2/2 reviewers)" and "≥2 treatment + ≥2 control." If three run and 2/3 flag, the verdict is undefined. And nothing states what happens on a partial treatment result — re-running fresh reviewers until 2/2 pass and reporting the final pair is selection bias (the same statistical sin the concurrency b-2 finding warned about, `concurrency-lens/decisions.md:47-49`). Pre-commit: exact reviewer count, every run counts, and the disposition of each possible outcome.

### Sweep items verified sound: 1 (closed set includes carried findings — consistent with `METHODOLOGY.md:288-290`), 3 (human retains final word — consistent with `:277-279`, `:281-284`), 5 (see FA-3 caveat), 6 (verbatim record + author interpretation split is coherent). Item 2 is the subject of LO-4.

### Fix-interaction check: F1+F5 interact **well** (embedded verbatim reviewer output makes silent demotion detectable); F2/F3 share the `verified = no` vocabulary consistently; F4 freeze coexists with stage-8 bounce-to-1 (full restart re-reviews criteria by construction). No bad pairwise interactions found beyond those already listed.

---

## Lens 3 — MISSED OPPORTUNITY (including audit-of-the-audit)

### MO-1 (MAJOR) — F1's provenance discipline covers only stage-3/6 docs; the F2 targeted check and stage-8 replay arms are left outside it.

F1 binds "stage-3/6 docs" (`0-audit-findings.md:26-32`; `2-plan.md:11`). The F2 targeted cold check and harness-embedded reviews (like C3's four arms) are **new/standing review channels created or relied on by this very change**, and they get no standing charter/context/output provenance duty — the prompt-rigging channel F1 closes is reopened one stage later, inside the same change. (This run handles it ad hoc — "verbatim outputs preserved," `1.5-criteria.md:16` — but the *rule being added* doesn't.) One-word-class fix: bind F1's provenance to "every cold-review record, wherever in the run it occurs."

### MO-2 (MINOR) — Provenance omits reviewer identity/capability.

F1 records charter, context, output — not **which agent type/model** reviewed. A capability-starved review (weakest available model, procedurally compliant) is the same invisible-channel shape the audit hunts. One metadata field.

### MO-3 (MINOR) — A second pre-existing-rule probe is nearly free and would materially strengthen the displacement claim.

V3 probes one charter rule, adjacent to the F1/F7 insertions. The stage-8 section absorbs F2+F3 insertions and no pre-existing rule there is probed. Add V4 to the same fixture (e.g. a gating criterion recorded as "will confirm live" — the deferral rule, `METHODOLOGY.md:327-344`, should fire in **both** arms): same reviewers, same run, doubles the neighbor coverage.

### MO-4 (MINOR) — F8 validates only `redteam_context` paths.

The spec's touched-files list (F6) and fixture paths handed to reviewers rot identically, and a reviewer handed a dead touched-file path silently degrades the same way. One clause: validate every path handed to a cold reviewer.

### MO-5 (NITPICK) — Fixture naming/ordering: `fixtures/seeded-review-record/` leaks the word "seeded" to both C3 arms (invites planted-defect hunting; symmetric, but inflates both arms' catch rates and feeds LO-1's benign-absorption). Name the path neutrally; add any "this is synthetic" README only **after** the C3 runs (else it's an answer leak; without it, future readers may mistake the fixture for a real run — so sequence it).

---

## Lens 4 — UNSTATED ASSUMPTIONS & RISKS

### AR-1 (MAJOR) — The criteria overclaim what C3 proves about position-sensitivity.

`1.5-criteria.md:5-8`: the treatment arm "runs on the amended docs **end-to-end**" and V3 firing "**proving** insertions didn't displace existing behavior." Neither holds: the C3 task exercises one narrow consumer path (charter + table rules), not the loop end-to-end; and one pre-existing rule firing at one insertion site is a spot-check, not proof, by the methodology's own standard ("treat every affected element's position — including elements that did not themselves change — as load-bearing until shown otherwise," `METHODOLOGY.md:60-62`). Concretely unprobed: `SKILL.md:57-62` (step 3) is already the densest paragraph in the file and absorbs **three** insertions (F1, F6, F7) — no behavioral probe touches it, and C4's line-count cap cannot see attention dilution ("C4 bounds dilution," `1.5-criteria.md:8`, overstates). Repair: reword to "spot-check evidence" + MO-3's second probe + name the residual displacement risk to the owner in the final report rather than letting C3's PASS imply it's retired.

### AR-2 (MINOR) — "control (current files, from git HEAD)" assumes the amendments are uncommitted at C3 time.

Verified today: HEAD `8a7ac65` is pre-change and the working tree is clean, so the assumption currently holds — but the precedent run committed its edits, and a mid-run commit silently turns both control arms into treatment arms, after which every control catch is absorbed as "redundant-but-harmless" (LO-1) with no alarm. One-token fix: pin the control docs to the recorded pre-change commit hash (`git show <hash>:…`), recorded at run start.

### AR-3 (MINOR) — n=2/arm with a 6/6 compound detection bar is false-FAIL-prone and thin for the claim.

Pass needs 2 reviewers × 3 violations all detected; stochastic reviewers make a single benign miss (especially under LO-2's masking) a gate failure, while n=2 controls both missing V1 is weak evidence the rule (not generic diligence) drives treatment catches. The precedent itself flagged n=2 as an honest limitation and b-2 asked for "a few … passes for a rate" (`concurrency-lens/decisions.md:47-49`, `:90-92`). Acceptable **only** with LO-7's pre-committed protocol and the limitation carried into the verdict, as the precedent did.

### AR-4 (MINOR) — "Terse, mechanical, Opus-friendly" is at risk at the two densest insertion points.

F1's substance (three embed duties + closed-set definition + A/B prohibition) into "one sentence each" at SKILL steps 3/6 (`2-plan.md:11`) is optimistic; the combined cap leaves ~102 lines for ~20 insertion sites, which is feasible but tight, and the S1 hazard the audit itself names (`0-audit-findings.md:113-117`) is assumed — not shown — to be un-crossed by nine simultaneous additions. C7 surfacing S1 to the owner is the right mitigation; the report should say "this change spends attention budget against S1's ceiling" explicitly.

### AR-5 (MINOR) — F3's mechanical rule collides with human-judged-rubric rows.

"Gating PASS with no evidence pointer = `verified = no`" (`2-plan.md:13`) vs `METHODOLOGY.md:352-355`, where the verified cell records "the named judge's verdict" — which may have no output file. Unreconciled, the rule either spuriously fails every rubric row or trains authors to fabricate pointers. One clause: for rubric criteria, the evidence pointer = named judge + where the verdict is recorded. (This belongs in the C2 contradiction sweep and isn't there.)

### AR-6 (NITPICK) — "The charter given must be the METHODOLOGY charter text, not a paraphrase" (`2-plan.md:11`) vs the reality that every real charter is task-tailored (the concurrency C3 treatment charter carried the guard text; scope/questions are always added). Needs "verbatim charter core + task-specific additions quoted as such," or every future compliant run is technically in violation.

### AR-7 (NITPICK) — Build order step 4 copies amended files to the live skill dir during stage 5, before gates 6–8; no rollback provision exists if the change is bounced hard or killed, leaving live carrying unaccepted rules.

---

## Ranked summary

| # | Sev | Lens | Finding |
|---|---|---|---|
| FA-1 | **Major** | Factual | "redundant-but-harmless per concurrency-lens precedent" — phrase absent from precedent (grep: 0 hits); precedent's pass rule said control-catch = FAIL; qualified pass there required partial differentiation |
| LO-1 | **Major** | Logical | Auto-benign control-catch removes attempt-1's confound tripwire; C3 can PASS with zero differentiation and no leak investigation |
| LO-2 | **Major** | Logical | V1/V3 co-location (+ ambiguous V3 placement) breaks isolation both directions; false FAIL and false PASS mechanisms both live |
| LO-3 | **Major** | Logical | V2 already catchable under current `METHODOLOGY.md:227-240` → "controls flag V3 only" unsupported; F3's marginal value may be undemonstrable |
| LO-4 | **Major** | Logical | F4 freeze: post-review/pre-gate edit window + no mechanical anchor — the targeted loophole survives the fix as written |
| LO-5 | **Major** | Logical | F7 (and F8) lack a consequence/enforcement hook — fails the run's own "mechanical, checkable" constraint and C1's own schema |
| MO-1 | **Major** | Missed opp | F1 provenance doesn't cover the F2 targeted check / harness-embedded reviews — the new trust point is born outside the new discipline |
| AR-1 | **Major** | Assumptions | "End-to-end" / "proving insertions didn't displace" overclaims a single-site spot-check; SKILL step 3 absorbs 3 insertions unprobed |
| FA-2 | Minor | Factual | "Caught only by author honesty" — detection was the strict pass-condition rule; diagnosis was the honesty |
| FA-3 | Minor | Factual | "Only F9's sentence rewrite expected" contradicted by F3's in-place column-list edit and SKILL clause wiring |
| FA-4 | Minor | Factual | C4 arithmetic: 560≠467×1.25; 128 = +25.5% > stated cap; 560+128 > 671; governing bound ambiguous |
| LO-6 | Minor | Logical | F2-findings-route-through-gate-8 lacks the rebuild-the-harness path |
| LO-7 | Minor | Logical | "≥2" vs "2/2" undefined; no resampling protocol → re-roll-until-pass hazard |
| MO-2 | Minor | Missed opp | Provenance omits reviewer agent-type/model |
| MO-3 | Minor | Missed opp | Add a second pre-existing-rule probe (V4, deferral rule) near the stage-8 insertion cluster — nearly free |
| MO-4 | Minor | Missed opp | F8 should validate all reviewer-handed paths, not just `redteam_context` |
| AR-2 | Minor | Assumptions | Control-from-HEAD contamination if edits committed mid-run; pin the hash (HEAD verified pre-change today) |
| AR-3 | Minor | Assumptions | n=2 / 6-of-6 bar: false-FAIL-prone, thin differentiation evidence; carry the limitation like the precedent did |
| AR-4 | Minor | Assumptions | Attention-budget tightness at SKILL step 3 / F1 substance; S1 spend should be named in the report |
| AR-5 | Minor | Assumptions | F3 mechanical rule vs human-judged-rubric rows unreconciled (missing from the C2 sweep) |
| MO-5 | Nitpick | Missed opp | "seeded-…" path name leaks to both arms; sequence the synthetic-fixture README after the runs |
| AR-6 | Nitpick | Assumptions | "Verbatim charter, not a paraphrase" vs necessarily task-tailored charters |
| AR-7 | Nitpick | Assumptions | Live copy amended before gates 6–8 with no rollback provision |

**Neutral-question check (explicitly requested):** the wording is acceptably neutral — identical across arms, and its consequence vocabulary exists in both doc versions ("un-run": current `METHODOLOGY.md:216,240`; "verified = no": `:322,350`), so controls aren't vocabulary-disadvantaged. Its one weakness is that "citing the rule" is asked but not required by the pass condition (folded into LO-2's repair).

---

## Bottom line

**Worst severity: MAJOR — route to stage 2 (re-plan); the direction is sound and no blocker exists.** The nine fixes are real, the audit's current-state claims all verified against source (every "the methodology has no rule for X" checked and confirmed), and the mapping locations exist. But the plan's centerpiece experiment is not yet a valid instrument: its precedent citation is materially wrong (FA-1), its disposition rule deletes the precedent's actual confound tripwire (LO-1), and its fixture as described can produce both a false FAIL (V1/V3 masking) and a hollow PASS (V2 already catchable under current text; control-catches auto-absorbed) — while the criteria overclaim what a single-neighbor probe proves about nine insertion sites (AR-1). Two of the nine fixes additionally carry loopholes of the exact class they target (F4's freeze window and anchor, F7's missing consequence). All of this is repairable with localized changes — restructure the fixture to one violation per artifact plus a fourth both-arms probe, restore a suspect-the-harness rule for anomalous control catches, pin the control docs to a recorded hash, anchor the freeze to the reviewed criteria version, give F7/F8 an "earned or un-run" consequence, extend F1's provenance to all cold-review records, and fix the C4 arithmetic and C6 deletion-hunk expectation — none of which requires abandoning the additive-terse approach or re-opening the spec.
