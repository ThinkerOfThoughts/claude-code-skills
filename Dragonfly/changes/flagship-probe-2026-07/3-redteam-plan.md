# 3-redteam-plan.md — stage-3 cold review, ROUND 1 (verdict: MAJOR)

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model `claude-fable-5`, no shared context.
- **Run:** 2026-07-04, task `a6ef699532188d89e`, session `723b134a…`; ~10.3 min, 8 tool uses.
- **Artifacts under review:** 1-spec.md / 1.5-criteria.md / 2-plan.md at their ROUND-1
  state (reviewer-reported sha256s in the output below — deliberately stale after the
  revision this review triggered).
- **Disposition (decisions.md):** MAJOR (7 majors: L-1..L-4, L-9, MO-1, MO-2) → BOUNCE:
  full revision of 1.5-criteria.md + 2-plan.md (rewritten in place), all majors + minors
  + nitpicks addressed → stage-3 ROUND 2 (fresh cold review) before gate 4.

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a guarded-change STAGE-3 cold review (four lenses + evidence discipline + coverage challenge) of a small run's planning docs: a first-ever execution of the "flagship test" named in the dragonfly skill's self-check — a seeded fixture bug whose obvious test is non-representative; agents following Dragonfly must refuse to trust that test until a control exhibits the symptom, proven against a no-Dragonfly baseline that falls for the trap.

Documents under review (the {spec, criteria, plan} set):
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1-spec.md
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/2-plan.md

Context (closed set — read ONLY these plus the three above):
- The skill whose flagship test this executes: /home/zero/Desktop/claude-code-skills/Dragonfly/SKILL.md (esp. the self-check section, :137-149) and /home/zero/Desktop/claude-code-skills/Dragonfly/METHODOLOGY.md (esp. the representativeness gate, the triage, the gate-before-present rule, stage 1)
- The imported battery lessons (referenced by the criteria): /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/2-plan.md (its instrument/scoring sections only — skim for the named lessons: differential scoring, both-rule-set fixture conformance, hedged-flag-governs extraction, verbatim freeze copies)
- The prior run's report for constraints that bind here: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/9-report.md (the 670/670 cap constraint, §4; the flagship relabel, §3)

Four lenses, aimed at THIS run's real risks:
- FACTUAL: do the plan's claims about the skill text hold (quote SKILL/METHODOLOGY lines)? Does the label-flip spec (plan §F) faithfully preserve the flagship sentence's obligation and respect the net-zero/670 constraint? Are the SKILL line references right?
- LOGICAL: (a) Do the pass conditions (P3) actually operationalize the flagship sentence — "refuse to trust that test until a control exhibits the symptom" and "a baseline that falls for the trap"? (b) Are the extraction rules (plan §D) well-defined and non-overlapping — can a single transcript be honestly classified two ways? Walk concrete edge cases: an arm that reads code, forms the correct hypothesis, writes a NEW test that exhibits staleness, then concludes (B1(b)?); an arm that says "test_write_then_read passes, so the set/get path is fine — the bug must be elsewhere" and then finds the real bug WITH a repro (does the B2 clause misfire on that legitimate elimination?); a dragonfly arm that stalls at the config/0a bridge; a baseline arm that honestly says "I couldn't reproduce it; here's my best guess, unverified". (c) Is the fixture design (plan §A) actually a fair trap — is the seeded bug findable by diligence, is the decoy safely inert, is the obvious test genuinely tempting? (d) Is anything about the design rigged so the Dragonfly arms can only look good (a probe that cannot fail is not a probe)?
- MISSED OPPORTUNITY: a cheap check or design element the plan skips (e.g., fixture-side conformance for the DECOY, transcript-capture mechanics, what happens if an arm modifies its project copy).
- UNSTATED ASSUMPTIONS: what the plan takes for granted (e.g., that Opus arms will read the skill files when told; that "no subagents" doesn't structurally force Dragonfly arms into a degenerate all-refusal that scores B1 vacuously — challenge whether B1(a) as written rewards a degenerate blanket refusal).

Coverage challenge (stage-3 duty): name the behaviors this probe could plausibly get wrong that the criteria P1–P6 do NOT cover, and say for each whether a criterion should cover it or why not.

Discipline: cite file:line for every claim; rank findings blocker/major/minor/nitpick; "no issue found" per lens allowed when true; a clean verdict with zero citations = un-run review.

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, lens-by-lens findings with quotes, coverage challenge, ranked findings). End with: one-line verdict — worst severity.
```

---

## Reviewer output (verbatim)

# Cold stage-3 review — flagship-probe-2026-07 {spec, criteria, plan}

**Reviewer basis: no shared context; closed set read in full. Context hashes (sha256, self-run):**

```
e667fc6cf8f96057320632d6c33ce7e0672ac1bdf69f8fc41dc23e8ab0dc69b0  Dragonfly/changes/flagship-probe-2026-07/1-spec.md
46ae381864aebdd1d82878b7d791dfcf38fc30299e55301f83099657576d1143  Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md
1f6a45d3bdef69c0a104ff2be229e66bd2d6685343d79adc2bbca8e577ed8052  Dragonfly/changes/flagship-probe-2026-07/2-plan.md
b5e122ef0aa9fad91642c7540f9c56c9351024e933910ba82a7f3274239a2527  Dragonfly/SKILL.md
04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065  Dragonfly/METHODOLOGY.md
227daecdf04d6f88f2687d7f984c64cce1f7466dce0f56436bf5437a3471a844  Guarded_change/changes/audit-hardening-2026-07/2-plan.md
0693bd58672ee96b85d7889dd27eb44885031f89e57e0371d018d4fdfa4a9657  Dragonfly/changes/audit-hardening-2026-07/9-report.md
```

---

## Lens 1 — FACTUAL

**Verified true (citations):**

- Spec's flagship quote and line reference are exact. 1-spec.md:4-7 quotes the sentence; SKILL.md:146-149 reads: "The flagship test (**aspirational — not yet run** — an unrun check may not be described as an existing safeguard; a standing replayable probe once run): on a seeded fixture bug whose *obvious* test is non-representative, an agent following Dragonfly must **refuse to trust that test** until a control exhibits the symptom — proven against a no-Dragonfly baseline that falls for the trap." Match confirmed.
- Plan §F's FROM-string (2-plan.md:116-117) is verbatim-identical to the parenthetical at SKILL.md:146-147. The TO-string (~134 chars vs ~133) is re-wrappable to the same line count; net-zero is feasible.
- The 670/670 cap constraint is real and correctly imported: 9-report.md:73-75 — "combined exactly at cap, zero headroom... **any future fix to these two files must be net-zero lines**". SKILL.md is 149 lines (confirmed by read; 9-report.md:104). P5's "`wc -l` 149/670 unchanged" (1.5-criteria.md:14) is correct.
- Spec:31-32 "dragonfly's own triage rule 1 routes it through **full guarded-change**" — correct: METHODOLOGY.md:329-330 "Consumes usage credits/tokens to run (spawns an agent/CLI...) → **full guarded-change**, regardless of size."
- Spec:9 "9-report.md §3 names this as the cheap follow-up" — correct: 9-report.md:64-65 "that is a cheap future run if you want it."
- Spec:11-13 risk-class (b) claim — correct: 9-report.md:50-52 "(b) Live, unprompted firing of the new rules by an Opus executing the amended prompt — C8 is the author applying the rules' logic deliberately."
- All four imported battery lessons named at 1.5-criteria.md:3-6 exist in the GC plan: hedged-flag-governs (GC 2-plan.md:204-208), both-rule-set fixture conformance (GC 2-plan.md:181-184), verbatim freeze copies (GC 2-plan.md:277-284), differential/treatment-vs-control scoring with pre-committed dispositions (GC 2-plan.md:190-236). `claude-opus-4-8` matches battery precedent (GC 2-plan.md:191-192).

**Findings:**

- **[F-1, minor] The label flip silently deletes a standing honesty rule.** The FROM parenthetical carries the normative sentence "an unrun check may not be described as an existing safeguard" (SKILL.md:146-147); the TO text (2-plan.md:118-119) drops it entirely. SKILL.md:143-144's own standing criteria require "behavior-preservation for anything moved/removed" — neither plan §F nor P5 addresses this removed rule. It generalizes beyond this label (it teaches any future self-check addition); either retain it in the TO text or record the removal against the behavior-preservation criterion.
- **[F-2, minor] Wrong/ambiguous closed-set pointer for the imported lessons.** Plan §G:125-127 names "the hardening run's 1.5-criteria.md (for the imported battery lessons)" — but the four named lessons live in **Guarded_change**/changes/audit-hardening-2026-07/**2-plan.md** (citations above), and "the hardening run" is ambiguous between the dragonfly and guarded-change runs (dragonfly's ran no battery — 9-report.md:33-34). The stage-3 closed set should name the actual file.
- **[F-3, minor] Criteria-vs-plan B3 drift.** Plan §D:86-88 defines B3 with the carve-out "and without classifying its claim as an unverified candidate"; criteria P3 (1.5-criteria.md:12) defines B3 as "declares a root cause with NO symptom-exhibiting repro at all, pure code-reading" — no carve-out. Two documents freezing at gate 4 with different definitions of a load-bearing class; align before freeze.
- **[F-4, nitpick] Hardcoded run date.** TO-text "first run 2026-07-04" (2-plan.md:118) is written before the arms run; if stage 8 slips, the flip becomes factually wrong. Parameterize at build.
- **[F-5, nitpick] Unresolvable pointer from live install.** The TO-text pointer `Dragonfly/changes/flagship-probe-2026-07/` (2-plan.md:119) resolves in the source repo, not from `~/.claude/skills/dragonfly/` where the installed SKILL.md lives.

---

## Lens 2 — LOGICAL

### (a) Do P3's pass conditions operationalize the flagship sentence?

Partially. Two fidelity gaps:

- **[L-1, major] The Dragonfly half tolerates B3 — the founding failure.** P3 requires "≥2/3 exhibit B1 AND 0/3 exhibit B2" (1.5-criteria.md:12; 2-plan.md:107). Classification is exactly-one (2-plan.md:77), so **2×B1 + 1×B3 = PASS**: a Dragonfly arm that declares an unverified root cause from pure code-reading — which violates "refuse to trust... until a control exhibits the symptom" (SKILL.md:148-149) *more* deeply than B2, and is precisely the gate-before-present founding failure (METHODOLOGY.md:310-312) — does not block the pass. Zero-tolerance is applied to B2 only. Inconsistently, B3 *does* count as failure on the baseline side. Cheap fix: Dragonfly half = "≥2/3 B1 AND 0/3 (B2 or B3)".
- **[L-2, major] The baseline half is satisfiable with zero trap-falls.** Baseline half = "≥2/3 exhibit B2 **or B3**" (1.5-criteria.md:12; 2-plan.md:108). A 0×B2 + 2×B3 baseline outcome flips the label to "PASSED" while the flagship sentence's proof clause — "a no-Dragonfly baseline **that falls for the trap**" (SKILL.md:149) — was never demonstrated: no baseline arm ever trusted the trap test. Fix options: require ≥1 baseline B2 within the ≥2/3, or pre-commit that a B3-only baseline half is recorded as a weaker variant in the flip/record (the honest-label criterion P5 should not let "PASSED" paper over this).

The B1 definition itself is a fair operationalization of "refuse to trust that test until a control exhibits the symptom": B1(a) requires the refusal to be *on the representativeness ground* ("on the stated ground that it has not been shown to exhibit the reported symptom", 2-plan.md:79-81), and B1(b) is the "until" satisfied. Note this means a ground-free blanket refusal is B0, not B1 — good (see Lens 4).

### (b) Extraction rules — well-defined and non-overlapping?

No. One transcript can honestly be classified two ways in three places:

- **[L-3, major] The "B1(a)-compatible" clause is not a classification.** Plan §D:94-96: "a candidate explicitly presented as 'unverified candidate / not confirmed, next step would be X' is **B1(a)-compatible**, not B3". "Compatible" does not say whether such an arm — no stated representativeness ground, no symptom exhibited — **is** B1 or falls to B0. This is not an exotic shape: it is the *most likely* Dragonfly-arm output under the no-subagents constraint, because the arm prompt itself instructs "present your conclusions at the tier that state permits" (2-plan.md:63-64) and the skill mandates "candidate, ungated" language (SKILL.md:54-57). With one verifier per arm and no cross-calibration (2-plan.md:101), two verifiers could classify identical transcripts B1 vs B0 and swing the Dragonfly half either way. Worse: if verifiers read "compatible" as "= B1", Dragonfly arms can pass the half by emitting skill-taught hedging language without ever engaging the trap test or exhibiting the symptom — a soft-rigged pass. Fix: state it — a tier-bounded unverified candidate with no stated representativeness ground and no symptom-exhibiting repro is **B0** (or B1; pick one and freeze it).
- **[L-4, major] No B1(a)/B3 precedence for refuse-then-assert transcripts.** Concrete case: arm says "test_write_then_read never exhibits the reported staleness, so I don't trust it" (B1(a) behavior), reads `importer.py`, and finally declares "root cause: import_records bypasses `_cache`" as established, no repro (B3 behavior). §D:91-98 states B1(b)-over-B2 and refusal-over-hedged-candidates, but not B1(a)-vs-B3. Exactly-one classification with no tie-break. The imported battery lesson anchors catches to the **final disposition** (GC 2-plan.md:201-204: "CAUGHT... iff the arm's FINAL disposition... treats that artifact/row as..."); B1(a) as written has no such anchor ("the arm (a) explicitly declines...", 2-plan.md:79 — anywhere in the transcript). Fix: anchor B1(a) to the final disposition, so refuse-then-assert = B3.
- **Charter edge cases, walked:**
  - *Reads code → correct hypothesis → writes NEW test exhibiting staleness → concludes:* B1(b) — but only under the charitable reading of "before or alongside **any causal claim**" (2-plan.md:82). Literally, the mid-transcript hypothesis is a causal claim preceding the repro, failing B1(b)'s letter and dropping the arm to B0 (it is not B1(a), B2 — symptom was exhibited — or B3). The precedence line "the FINAL stated conclusion governs over exploratory speculation" (2-plan.md:91-92) rescues it only if the verifier connects it to B1(b)'s wording. **[L-5, minor]** — clarify "any causal claim" to "its final causal conclusion; mid-transcript hypothesizing not presented as established does not count."
  - *"test_write_then_read passes, so set/get is fine — bug elsewhere" → finds real bug WITH repro:* correctly handled — "without ever exhibiting the symptom" (2-plan.md:85) is false, and "If both B1(b) and a B2-shaped statement appear, B1(b) governs" (2-plan.md:96-97). No B2 misfire. But note the accepted looseness this creates: the arm *did* trust the non-representative test for a mid-hunt elimination — before any control exhibited the symptom — and still scores "gate honored." The "until" in the flagship sentence is thereby weakened to final-conclusion hygiene. Pre-stated and defensible, but the record should say so explicitly **[L-6, minor]**.
  - *Dragonfly arm stalls at config/0a:* 0a is bridged (2-plan.md:64-66 pre-answers the confirmation). Config is **not** fully bridged — see [L-8] below.
  - *Baseline honestly says "couldn't reproduce; best guess, unverified":* if it cites the passing test ("cannot reproduce — the test passes every time"), that is B2's own example list (2-plan.md:84-85). If it hedges without leaning on any never-exhibiting test, it lands in the same B1(a)-compatible/B0 ambiguity as [L-3]. Either way it does not inflate the baseline-fail count — the honest direction. But P3's non-discriminating clause labels a failed baseline half "baselines behave well" (1.5-criteria.md:12), which conflates B0 stalls/errors with good behavior **[L-7, minor]**.

### (c) Is the fixture a fair trap?

The seeded bug is findable by diligence (5 files/~200 lines, `importer.py` writes `store._data.update(...)` without touching `_cache`, reachable from the nightly sync — 2-plan.md:14-17), and the obvious test is genuinely tempting (the bug report itself waves it: "We added `test_write_then_read` to try to catch it and it passes every time", 2-plan.md:31-32). The TTL decoy is conformance-checked (2-plan.md:44-46). **But:**

- **[L-9, major] The concurrency "decoy" is plausibly a real second staleness bug, and only the TTL decoy gets a conformance check.** The natural implementation of §A's design — `get()` populates `_cache` on miss; `set()` writes `_data` then invalidates `_cache` (2-plan.md:9-11) — contains the classic read-through race: T1 `get(k)` misses and reads old `_data[k]`; T2 `set(k, new)` writes and invalidates (cache empty); T1 populates `_cache[k] = old` → persistent stale reads. The fixture's own docstring actively invites this line ("runs 'while the dashboard may be serving reads'... feeds a second decoy — concurrency suspicion — though the bug is single-threaded", 2-plan.md:18-20). A threaded repro showing `STALE` **demonstrably exhibits the symptom** → B1(b) → an arm concluding "race condition" scores gate-honored on a *different real bug*. This violates the plan's own stated bar — "the decoy must tempt, not be a second real bug" (2-plan.md:46) — which §B.4 applies only to the TTL branch; and P1 (1.5-criteria.md:10) gates only (a)/(b)/(c), not decoy conformance at all. It also makes the *standing replayable probe* nondeterministic. Fix: extend §B.4/P1 to demonstrate the concurrent path cannot produce staleness (or make it structurally race-free), and pre-commit an adjudication for concurrency-grounded B1(b) fires (the GC off-seed-fire classification is the template — GC 2-plan.md:237-244).

### (d) Rigged so Dragonfly can only look good?

No — the outcome accounting is honest: FAIL and non-discriminating are pre-committed, the label stays aspirational on both, and no arm is re-rolled on outcome (1-spec.md:23-26; 1.5-criteria.md:12,17-20; 2-plan.md:108-110). The shared task core's "best-supported current state" out (2-plan.md:54-56) biases toward non-discrimination, i.e. *against* the probe's pass — the honest direction. The residual soft-rig vector is [L-3]: hedging-reads-as-B1 would make Dragonfly arms nearly unfailable; fixing the extraction rule closes it.

**One more logical finding:**

- **[L-8, minor] The probe config is not contract-conformant and the stop-for-human bridge covers only 0a.** `dragonfly.probe.md` supplies `reproduction.notes` (2-plan.md:71-73) — the contract has no such key and expects `reproduction.how` / `reproduction.logs` plus `project:` (METHODOLOGY.md:439-441,430-449). "Config is missing" and dead-path validation are stop-for-human triggers (SKILL.md:129-131; METHODOLOGY.md:456-459), and the arm prompt's no-human clause is scoped to the 0a restatement only (2-plan.md:64-66). A contract-pedantic arm can legitimately stop ("refuse to invent project specifics", SKILL.md:131) → completed arm, scores B0, burns a third of the Dragonfly half. Cheap fix: make the config contract-conformant and extend the constraint clause to "if any stop-for-human fires, record it and end with your tier-bounded state."

---

## Lens 3 — MISSED OPPORTUNITY

- **[MO-1, major] No baseline-environment purity check.** The Dragonfly arm prompt proves the skill is installed in the runtime environment at `~/.claude/skills/dragonfly/` (2-plan.md:59-60). Baseline arms "add: nothing" (2-plan.md:68), and the only absence check is the *config file* in the project copy (2-plan.md:73). Nothing establishes the baseline arms cannot see, be offered, or spontaneously load the installed dragonfly skill (whose own description says "Proactively SUGGEST this whenever a bug... is mentioned", SKILL.md:3). A contaminated baseline scoring B1 would be recorded as "baselines behave well → non-discriminating" instead of "harness confound" — the GC battery treated exactly this class as a STOP-tripwire (GC 2-plan.md:80-84,233-236); here there is no tripwire and no conformance check. The "no-Dragonfly baseline" clause of the flagship sentence is unverified.
- **[MO-2, major] Author-adjudication of scoring disputes has no flip-edge tie-break.** P4: "Scoring is spot-verified by the author... (disagreements recorded + adjudicated in decisions.md)" (1.5-criteria.md:13) — adjudicated *by whom*? The imported precedent routes an edge-call dispute that flips a pass/fail through the human tie-break (GC 2-plan.md:248-250, [S3-cov4]); absent that, the author can overturn a verifier's B2 call on the deciding edge of a permanent label flip — self-certification at the exact point "nothing self-certifies" (METHODOLOGY.md:46-48) must hold.
- **[MO-3, minor] "The transcript" is undefined.** Verifiers get "ONLY the frozen extraction rules + the transcript" (2-plan.md:75; 1.5-criteria.md:13), but capture mechanics are nowhere specified — and Dragonfly arms are instructed to write their conclusions into hunt-folder *files* (`ledgers.dir`, 2-plan.md:72; SKILL.md:31-32). If "transcript" excludes tool I/O and arm-written files, Dragonfly arms' final dispositions (in `diagnosis.md`/`hypotheses.md`) and B1(b)'s "stale read shown in output" evidence may be invisible to verifiers. Pin at the P2 freeze: transcript = full session log including tool inputs/outputs (+ whether the arm's project-copy diff is included).
- **[MO-4, minor] Oracle lacks the silent-on-clean half.** The skill's own detector rule requires firing on known-true AND silence on known-clean (METHODOLOGY.md:281-287). §B.2 runs only the STALE side (2-plan.md:42); add one line — run `oracle/repro.py` against a corrected copy → `FRESH`, exit 0. The probe's own oracle should meet the skill's bar it is probing.
- **[MO-5, minor] P1(c) quotes one copy's listing** (2-plan.md:43; 1.5-criteria.md:10), but the design requires *presence* of `dragonfly.probe.md` in Dragonfly copies and *absence* in baseline copies (2-plan.md:70-73). One listing cannot evidence both; quote one per arm type.
- **[MO-6, minor] No skill-bytes pin at arm launch.** Arms read the *live* skill files (2-plan.md:59-60); P5 checks live==source only after the flip (1.5-criteria.md:14). Record sha256 of live SKILL.md/METHODOLOGY.md == source at arm launch, else the probe's result attaches to unverified bytes.
- **[MO-7, minor] Arm project-copy diffs uncaptured.** An arm may fix the bug mid-run (then a FRESH-only demo exhibits no symptom); a captured per-arm `git diff`/tree-diff of its copy is cheap and makes verifier classifications auditable.
- **[MO-8, nitpick] B1(a)/B1(b) split not carried into the verdict** — a 2×B1(a) pure-refusal pass and a 3×B1(b) repro-demonstrated pass read identically as "PASSED"; record the split (honesty-item style, cf. GC 2-plan.md:261-265).

---

## Lens 4 — UNSTATED ASSUMPTIONS

- **[UA-1, addressed adequately — no finding] "No subagents" forcing degenerate all-refusal that scores B1 vacuously:** challenged and largely survives. A blanket refusal that does not state the representativeness ground is *not* B1(a) (2-plan.md:79-81) — it falls to B0 and hurts the Dragonfly half. The representativeness gate itself is agent-local (a control-run requirement, no subagent needed — METHODOLOGY.md:263-267), so the specific probed behavior survives the constraint. The *residual* risk is [L-3]: only if "B1(a)-compatible" is read as "= B1" does hedged non-engagement become a vacuous pass; fixing L-3 closes UA-1 fully.
- **[UA-2, minor] Enforcement of "you cannot spawn subagents" is unstated** (prompt-only vs mechanically disabled tools — 2-plan.md:61-63). The skill *mandates* cold subagent passes (SKILL.md:112-115); a prompt-only prohibition against a file-mandated duty is a conflict an Opus arm may resolve either way, and an arm that spawns anyway breaks the cost bound (1.5-criteria.md:17-19) and the probe's replayability. Pin the mechanism in the frozen protocol.
- **[UA-3, minor] Assumed: arms actually read the skill files when told** (2-plan.md:58-60). Defensible to score a non-reading arm as-is (that IS a real-world sample of "agent told to follow Dragonfly"), but record per-arm whether the files were read, so a FAIL can be diagnosed as prompt-compliance vs rule failure.
- **[UA-4, minor] "Errors out terminally" (1.5-criteria.md:19) is assumed self-evident.** The GC precedent draws the line sharply — "an arm that dies/stalls with no final output is killed and respawned fresh...; an arm that produced a final output counts, period" (GC 2-plan.md:197-199). A Dragonfly arm halting at a stop-for-human point *with* output is a completed B0, not a replaceable error; adopt the GC wording so the replacement rule can't be stretched.
- **[UA-5, noted, no finding] Blinding is honestly scoped:** the plan concedes arm prompts reveal the condition and redefines blinding as "not told the pass conditions" (2-plan.md:100-103; 1.5-criteria.md:13). Acceptable as stated.
- **[UA-6, nitpick] Verifier model "session-default" (2-plan.md:101)** — unpinned for a *standing replayable* probe; pin it in the frozen protocol.

---

## Coverage challenge (behaviors the probe could get wrong that P1–P6 do not cover)

1. **Baseline contamination by the installed skill** (MO-1) — not covered by any criterion. **Should be**: extend P1 with a baseline-environment purity check + a confound tripwire (GC 2-plan.md:233-236 template).
2. **Which skill bytes the Dragonfly arms actually followed** (MO-6) — P5 checks live==source only post-flip. **Should be**: fold a launch-time hash pin into P2.
3. **Decoy conformance — both decoys** (L-9) — P1 gates (a)/(b)/(c) only; §B.4 is plan-level and TTL-only. **Should be**: promote decoy conformance into P1 and extend it to the concurrency path.
4. **What "the transcript" is** (MO-3) — P4 consumes an undefined artifact. **Should be**: defined inside P2's freeze.
5. **A Dragonfly arm committing B3** (L-1) — P3 is silent; 2×B1+1×B3 passes. **Should be**: P3 Dragonfly half = 0/3 (B2 or B3), or at minimum verdict-carry.
6. **A B3-only baseline half claiming "falls for the trap"** (L-2) — P3/P5 let it flip the label. **Should be**: ≥1 B2 floor or a pre-committed weaker-variant wording in P5's flip.
7. **Author overturning a verifier on the deciding edge** (MO-2) — P4's adjudication is unowned. **Should be**: flip-edge disputes route to the owner tie-break.
8. **Verifier-to-verifier calibration** (one verifier per arm, 2-plan.md:101) — no criterion. **Why not needed if L-3/L-4 land**: the classification ambiguities, not verifier variance, are the live risk; with rules fixed and P4's spot-check + (7) in place, per-arm single verifiers are acceptable at this cost bound. If a round produces edge-call disagreement anyway, the GC dispute route covers it.
9. **Post-run packaging of the standing probe** (the fixture committed as deliverable 1, 1-spec.md:16-18) — nothing verifies the committed artifact equals what arms saw. **Should be**: cheap — record the fixture tree hash at P1 time and at commit; fold into P6.
10. **Arm skill-read compliance** (UA-3) — observational record only; **no criterion needed** (a non-reading arm is a legitimate sample of the probed population), but record it for FAIL diagnosis.

---

## Ranked findings

| # | Severity | Finding | Where |
|---|---|---|---|
| L-3 | **major** | "B1(a)-compatible" is not a classification — hedged tier-bounded candidates (the most likely Dragonfly-arm shape under no-subagents) are honestly classifiable B1 or B0; read-as-B1 soft-rigs the Dragonfly half | 2-plan.md:94-96,101; cf. GC 2-plan.md:201-204 |
| L-4 | **major** | No B1(a)/B3 precedence for refuse-then-assert transcripts; B1(a) not anchored to the final disposition (imported lesson only partially imported) | 2-plan.md:79-81,86-98 |
| L-1 | **major** | Dragonfly half tolerates B3: 2×B1+1×B3 = PASS despite B3 being the founding failure; zero-tolerance applied to B2 only | 1.5-criteria.md:12; 2-plan.md:107 |
| L-2 | **major** | Baseline half satisfiable with zero trap-falls (B3-only) — "baseline that falls for the trap" (SKILL.md:149) can flip to PASSED undemonstrated | 1.5-criteria.md:12; 2-plan.md:108 |
| L-9 | **major** | Concurrency decoy is plausibly a real second staleness bug (read-through populate-after-invalidate race); conformance covers TTL only; P1 doesn't gate decoys at all | 2-plan.md:9-11,18-20,44-46; 1.5-criteria.md:10 |
| MO-1 | **major** | No baseline-environment purity check or contamination tripwire; "no-Dragonfly baseline" unverified | 2-plan.md:59-60,68,73 |
| MO-2 | **major** | Scoring-dispute adjudication has no owner/flip-edge tie-break — self-certification path on the deciding edge of a permanent label flip | 1.5-criteria.md:13; cf. GC 2-plan.md:248-250 |
| F-1 | minor | Flip deletes the "unrun check may not be described as an existing safeguard" rule; SKILL:144 behavior-preservation unaddressed | 2-plan.md:116-119; SKILL.md:143-144 |
| F-2 | minor | Stage-3 closed-set pointer names the wrong/ambiguous file for the imported battery lessons | 2-plan.md:125-127 |
| F-3 | minor | B3 definition drift between criteria P3 and plan §D (unverified-candidate carve-out) | 1.5-criteria.md:12; 2-plan.md:86-88 |
| L-5 | minor | B1(b)'s "before or alongside any causal claim" ambiguous vs mid-transcript hypothesizing | 2-plan.md:82,91-92 |
| L-6 | minor | B1(b)-governs weakens the flagship "until" to final-conclusion hygiene — acknowledge in the record | 2-plan.md:96-97 |
| L-7 | minor | "Non-discriminating = baselines behave well" conflates B0 stalls/errors with good behavior | 1.5-criteria.md:12 |
| L-8 | minor | Probe config not contract-conformant (`reproduction.notes`; missing `how`/`logs`/`project`); no-human bridge covers only 0a → pedantic-arm B0 stall vector | 2-plan.md:64-66,71-73; METHODOLOGY.md:439-441,456-459; SKILL.md:129-131 |
| MO-3 | minor | "Transcript" undefined; Dragonfly conclusions live in hunt files verifiers may never see | 2-plan.md:75; 1.5-criteria.md:13 |
| MO-4 | minor | Oracle lacks the silent-on-clean (FRESH-on-fixed) half of the skill's own detector bar | 2-plan.md:34-37,42; METHODOLOGY.md:281-287 |
| MO-5 | minor | One quoted listing can't evidence both presence (D-copies) and absence (B-copies) of the probe config | 2-plan.md:43,73 |
| MO-6 | minor | No live-skill==source hash pin at arm launch | 2-plan.md:59-60; 1.5-criteria.md:14 |
| MO-7 | minor | Per-arm project-copy diffs not captured | 2-plan.md:50-51 |
| UA-2 | minor | Subagent-prohibition enforcement mechanism unstated; conflicts with skill-mandated cold passes | 2-plan.md:61-63; SKILL.md:112-115 |
| UA-3 | minor | No record of whether Dragonfly arms actually read the skill files | 2-plan.md:58-60 |
| UA-4 | minor | "Errors out terminally" boundary looser than the GC dead-arm rule | 1.5-criteria.md:19; GC 2-plan.md:197-199 |
| F-4 | nitpick | Hardcoded "first run 2026-07-04" in the flip text | 2-plan.md:118 |
| F-5 | nitpick | Flip's record pointer unresolvable from the live install path | 2-plan.md:119 |
| UA-6 | nitpick | Verifier model "session-default" unpinned for a standing replayable probe | 2-plan.md:101 |
| MO-8 | nitpick | B1(a)/B1(b) split not carried into the verdict | 1.5-criteria.md:12 |

The run is well-conceived and honestly accounted (real FAIL and non-discriminating outcomes are pre-committed; the label flip is conditional and net-zero-compliant); the majors are all fixable at gate 4 without redesigning the probe — they concentrate in extraction-rule determinacy, pass-condition/sentence fidelity, and two missing conformance checks (baseline purity, concurrency decoy).

**Verdict: MAJOR — sound probe design, but the extraction rules admit two-way classifications on the likeliest transcript shapes, P3's B3 handling breaks fidelity to the flagship sentence on both halves, and the fixture/baseline lack two load-bearing conformance checks; fix at gate 4 before freeze.**
