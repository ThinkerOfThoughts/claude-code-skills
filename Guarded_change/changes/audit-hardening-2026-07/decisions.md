# decisions.md — gate log (append-only)

## Run start — 2026-07-03
- Config note: skills-repo self-change → no Layer-2 measurement config (precedent:
  concurrency-lens). Stage 8 = conformance-only. redteam_context for reviewers = the skill's
  own files + prior change records (validated: all paths exist, readable).
- Pre-change state pinned: skills repo HEAD `8a7ac65`, working tree clean on both files.
  Baselines: METHODOLOGY.md 467 lines, SKILL.md 102 lines (569 combined).

## Stage 4 gate (plan red-team, round 1) — 2026-07-03
- **Worst severity: MAJOR.** Counts: 0 blocker, 8 major (FA-1, LO-1..LO-5, MO-1, AR-1),
  11 minor, 3 nitpick. Cold reviewer (general-purpose, model claude-fable-5, no shared
  context); verbatim prompt + output preserved in `3-redteam-plan.md`. Consumer spot-verify
  done: FA-1's grep re-run (confirmed — "redundant" absent from precedent; precedent 1.5 L13
  = strict differential pass); 3 further citations checked against the author's full read.
- Headline findings: FA-1 precedent miscited ("redundant-but-harmless" invented) and LO-1 the
  miscitation deleted the precedent's confound tripwire; LO-2 fixture co-location breaks
  isolation; LO-3 V2 catchable under current text (F3 may verify as codification); LO-4 F4
  freeze window exploitable + no mechanical anchor; LO-5 F7/F8 no consequence; MO-1 F1
  provenance doesn't cover post-6/harness-embedded reviews; AR-1 criteria overclaim ("proving"
  → spot-check).
- **Route: MAJOR → return to stage 2 (re-plan).** First bounce at gate 4. All 22 findings to
  be addressed in plan v2 + criteria v2; FA-2 correction noted against the audit doc (the
  attempt-1 confound was DETECTED by the precedent's strict pass rule; author honesty supplied
  the diagnosis).
- **ERRATUM (round-2 R2-7):** round 1 produced **23** findings (8 major, 12 minor, 3 nitpick),
  not the "22 / 11 minor" logged above — miscount; all 23 were addressed (round-2 Task A
  verified each). The entry above stands uncorrected per append-only; this erratum governs.

## Stage 4 gate (plan red-team, round 2) — 2026-07-03
- **Worst severity: MINOR.** Fresh cold reviewer (general-purpose, model claude-fable-5, no
  shared context; the first round-2 spawn died in a network outage and was killed + respawned
  — cold review, nothing carried). Verbatim prompt + output preserved in `3-redteam-plan.md`
  (round-2 section). **Task A: 23/23 round-1 findings verified RESOLVED against landed text.**
  Task B: 12 new findings — 6 minor (R2-1 F8 fixture-path timing, R2-2 control-V1 disposition
  cells + tripwire wording, R2-3 retry re-opens F2 window, R2-4 freeze-anchor internal
  contradiction, R2-5 "charter core" undefined, R2-6 SKILL cap margin), 6 nitpick (R2-7 count
  erratum, R2-8 fixtures/ path leak, R2-9 wording tensions, R2-10 fixture build care, R2-11 F5
  gate-8 scoping, R2-12 duplicate scope definitions).
- **Route: MINOR → all 12 fixed in place** (plan v2 + criteria + audit-doc erratum edits,
  tagged [R2-n] inline), **proceed to BUILD (stage 5).**
- **Criteria FREEZE (F4 dogfooded):** 1.5-criteria.md frozen at route-to-build.
  sha256 = `c29dfada53cc7bdebdcf6acfbfc26cb8c7d892dc976a55205e00aa7d537f084d`.
  Criteria diff vs the version the round-2 reviewer read (gate-4 in-place fixes, each traceable
  to a logged finding per R2-4's own rule): one hunk — C3 row "no resampling" → "no silent
  resampling — the plan's single logged diagnosed-fix re-run is the only exception
  [LO-7/AR-2/R2-9a]". No other criteria text changed.
- Consumer spot-verify (round 2): FA-4 arithmetic re-checked by author (583≤583.75, 127≤127.5,
  671≤671.42 ✓); R2-1's "fixture paths cannot exist at run start" verified against build order
  step 3; R2-7 recount verified against the round-1 table (23 rows).

## Stage 7 gate (code red-team) — 2026-07-03
- **Worst severity: MAJOR (reviewer's severity; routed as stated — F5 dogfooded).** Fresh cold
  reviewer (general-purpose, claude-fable-5); verbatim record in `6-redteam-code.md` +
  `6-redteam-code.verbatim.md`; reviewer self-reported context hashes (freeze hash matched).
  Rule text verdict: all 9 fixes landed (C1), no contradictions (C2), additive holds (C6) with
  2 minors; both MAJORS (D1, D2) live in the C3 FIXTURE, not the rule text.
- **Route: MAJOR → return to build (5).** Fixes applied (in-place diffs, recorded per the new
  gate-7 duty):
  - **D1 (fixture V3):** fixture 6-redteam-code.md charter expanded with the PRE-change
    discipline bullets verbatim-in-substance (earned-clean-factual, spot-verify, label-audit,
    flag-unverifiable) + "report the sha256 of each context file" instruction + the diff added
    to the reviewer-reported hash list. NOT included: the provenance bullet itself — including
    amended-rule text would leak to control arms (reviewer's own D5 analysis); residual
    adjudication pre-committed in the plan (V3 counts if earned-clean is among the cited
    grounds; provenance-only flag = instrument defect → re-run path, not a battery FAIL).
  - **D2 (fixture V2):** C4 row now cites its own artifact (`harness-out/c4-volume.log`,
    full-run line audit) — no output location anywhere for the C1 run.
  - **D3 (fixture):** fixture decisions.md gains run-start path-validation record + gate-4
    freeze-hash record (`6364136da75e…` — the file's true hash); fixture 8-harness.md notes
    the harness-time hash match. In-universe compliance records; leak-safe (compliance is not
    citable as a violation).
  - **D4 (fixture):** V4 verified cell "no" → "no — deferred" (letter conformance to R2-10a).
  - **A1 (METHODOLOGY):** charter-core definition now enumerates — "+ the coverage-challenge
    bullet for stage-3 reviews and any conditional lens (position / concurrency) whose
    trigger fires".
  - **C-2 (SKILL):** self-check regains the trivial-edit encouragement ("A stage-3 red-team
    remains the cheap check encouraged after any edit, however small.").
  - **A2 (SKILL):** step 4 "sha256 (or a verbatim copy)"; step 8 "frozen hash" → "frozen
    version".
  - **C-1:** no doc edit — the two benign rewrap hunks will be justified per-hunk in
    8-harness.md with the enumeration-gap note (the frozen criterion's own justification
    mechanism; criteria not edited → freeze intact).
  - B2/B3/B4/A3/D5: logged, no change (reviewer's own analysis: intent unambiguous /
    style-consistent / pointer-resolves / cap holds / design-inherent).
- Caps after fixes: METHODOLOGY 534 ≤ 583, SKILL 124 ≤ 127, combined 658 ≤ 671 ✓.
- **Per the new F2 rule (dogfooded): the modified fixture gets a targeted cold check before
  the C3 battery counts.** Spawning it now; battery follows only on its pass.

## Targeted fixture cold check #1 (F2, post-gate-7 repairs) — 2026-07-03
- **Worst severity: MAJOR (reviewer's severity; routed as stated).** Counts: 0 blocker,
  2 major (M1, M2), 2 minor (m1, m2), 3 nitpick (n1–n3), 1 protocol note. Fresh cold reviewer
  (general-purpose, claude-fable-5), respawned once across a usage pause (cold — nothing
  carried). Verbatim prompt + output + reviewer-reported hashes: `6-fixture-check-1.verbatim.md`.
- Positive verdicts: repairs D1/D2 LANDED; D3/D4 conform; all four seeded violations INTACT;
  contamination sweep CLEAN (no amended-rule text in the fixture).
- **M1:** the D3 repair itself introduced a provable hash contradiction — fixture
  `6-redteam-code.md:25` reports `1.5-criteria.md` as `c400aa9e…` vs the true, twice-recorded
  `6364136da75e…`. **M2:** fixture `8-harness.md:1–3` claims "greenfield → conformance-only"
  while the spec modifies an existing uploader — an unseeded fifth violation citable under
  BOTH rule sets. **Protocol note:** the battery prompt must scope out the in-fiction
  artifacts (uploader.py, harness-out/*.log, the diff) or spot-verify fails symmetrically in
  both arms and swamps the seeded signals.
- **ITERATION CAP FIRES — loop STOPPED for human tie-break.** This is the second consecutive
  major-bearing backward route on the same finding class: gate-7 round 1 (D1/D2, fixture
  `6-redteam-code.md` provenance block + `8-harness.md`) → repairs → this check (M1 in the
  same provenance block, introduced BY the D3 repair; M2 in `8-harness.md`). Per
  METHODOLOGY "2 bounces at the same gate on the same finding class → a human breaks the
  tie"; "the same kind of defect resurfacing in a nearby spot still counts." The author does
  not adjudicate his own cap. Options put to the owner: (a) authorize repair round 2 (both
  majors are one-line-class fixes; scoped re-check before the battery), (b) accept-risk (run
  the battery with M1/M2 present + pre-committed adjudication for the extra fire sources),
  (c) kill/replace the C3 instrument.
- **HUMAN TIE-BREAK (owner, 2026-07-03): option (a) — repair round 2 authorized.** Scope:
  fix M1 + M2 + both minors (m1 fold-ins into fixture plan; m2 earned label-audit line);
  nitpicks n1–n3 LOG-ONLY (churn risk exceeds fire risk — the M1 precedent is a repair
  introducing a defect; minimize touches); amend the battery arm prompt per the protocol
  note (arm-neutral artifact-scoping sentence — logged plan edit, criteria untouched/frozen);
  then a scoped targeted re-check (F2) before the battery counts.

## Fixture repair round 2 (post-cap, owner-authorized) — 2026-07-03
- In-place diffs (recorded per the gate-7 duty):
  - **M1 (fixture 6-redteam-code.md:25):** reviewer-reported 1.5-criteria.md hash
    `c400aa9e…` → `6364136da75e…` (now consistent with the in-fiction freeze +
    harness re-hash; the file's true sha256).
  - **M2 (fixture 8-harness.md:1–3 + decisions.md run-start):** "Greenfield … no prior
    metric → conformance-only" REPLACED with a recorded stage-0 baseline (nightly export
    aborts on first 5xx; 3 aborts last month, ops log — consistent with 1-spec) + a
    regression check citing its own artifact (`harness-out/regression-dryrun.log`, exit 0,
    31m40s < 40-min window); fixture decisions.md run-start entry now records the baseline.
  - **m1 (fixture 2-plan.md):** "Stage-3 fold-ins" paragraph added — checksum computed once
    before the first attempt (HEAD compares the stored value), and the 90 s budget hard-caps
    a schedule sleep to its remainder (matches 3-redteam-plan.md's suggested fixes AND the
    stage-6 reference "as the stage-3 fix specified").
  - **m2 (fixture 6-redteam-code.md):** earned "Label audit" verdict added before the bottom
    line — cites `1.5-criteria.md:8` for C4's advisory reason; notes no verification table
    exists at stage 6. V3's ground (zero-citation clean FACTUAL lens) untouched.
  - **n1/n2/n3:** log-only, per the tie-break scope.
- **Plan amendment (logged; criteria NOT touched — freeze intact):** the battery arm
  question gains one arm-neutral artifact-scoping sentence ("source tree, diffs, and run
  outputs are not attached … judge the record as a record") per the fixture-check protocol
  note; tagged [FC1-note] in 2-plan.md. Traceable finding: fixture-check #1 protocol note.
- **Scoped targeted re-check (F2) spawning now** — verifies the 4 repairs landed, the seeded
  V1–V4 remain intact and sole-per-artifact, no new contradictions, no contamination.
  Battery follows only on its pass; a further major here = a THIRD bounce → back to the
  owner, no self-adjudication.

## Targeted fixture cold check #2 (scoped, post-repair-round-2) — 2026-07-03
- **Worst severity: NITPICK (one, log-only; routed as stated).** Fresh cold reviewer
  (general-purpose, claude-fable-5). Verbatim prompt + output + reviewer-reported hashes:
  `6-fixture-check-2.verbatim.md`.
- All 4 repairs LANDED (M1: four-way hash agreement incl. the file's true sha256; M2:
  baseline/regression consistent with the spec, V2 undisturbed; m1: fold-ins consistent with
  stage-3 findings AND stage-6 references; m2: label audit earned, V3's factual lens
  untouched). Seeded V1–V4 INTACT, each still its artifact's only violation-shaped defect.
  Contamination sweep CLEAN. Mtime scope corroboration: only the 4 repaired files changed.
- Nitpick (fixture decisions.md:11 "confirmed post-ship" wording): LOG-ONLY, consistent
  under natural reading, does not damage V4 detectability.
- **Route: PASS → C3 battery authorized.** Fixture copied to the neutral scratchpad
  `run-record/` path (copy-time hashes = the 7 reviewer-reported hashes above; recorded at
  copy). **Battery arms: 4 × cold `general-purpose` subagents on `claude-opus-4-8` — author
  decision, logged here: the criteria pin "4 cold subagents" without a model; Opus is the
  production model for these skills (owner constraint), so Opus arms are the
  externally-valid test; one model across all arms = no model confound.** No author-authored
  supplementary context in any arm (plan F1 row); prompt = the plan's amended neutral
  question + the two read paths + a both-arms-identical closed-set sentence, verbatim
  template pre-staged in the session scratchpad (`battery-arm-prompt.md`), reproduced in the
  battery record at stage 8.

## C3 battery — ROUND 1 — 2026-07-03
- 4 arms launched in parallel (T1/T2 on docs-a; K1/K2 on docs-b; all opus, general-purpose,
  cold, identical prompts except docs path). Verbatim outputs + provenance + scoring:
  `8-battery-round1.verbatim.md`. run-record/ copy-time hashes == fixture-check-2 hashes 7/7.
- **Result: FAIL on the frozen pass condition — V3 treatment 1/2** (T1 credited the lens's
  descriptive mentions as citations; T2 + BOTH controls caught it via the pre-existing
  zero-citation rule). V1: 2/2 T vs 0/2 K ✓. V2: 2/2 T vs 0/2 K ✓ — **F3 demonstrated as NEW
  behavior, not codification** (LO-3 resolved favorably). V4: 4/4 ✓.
- **Confound tripwire: not triggered** — every control-cited rule verified present in
  docs-b (incl. K1's earned-label-audit rule, docs-b:237-239); no control flagged V1/V2.
- **Route (pre-committed, frozen criteria):** any treatment miss → diagnose, fix, re-run the
  whole battery ONCE with 4 fresh reviewers — "the plan's single logged diagnosed-fix re-run
  is the only exception" to no-resampling. This is the experiment's own protocol, not a gate
  bounce; the iteration cap is not consumed by it. A SECOND fail → stage-8 major → human.
- **Diagnosis** (full text in the battery record): primary = fixture wording — V3's
  verification-walk prose invites reading mentions as citations; contributory (logged only)
  = diligence halo + possible amended-doc attention dilution (→ S1 report). **Fix: fixture
  wording only** — V3 lens compressed to one terse assertion, zero citations, task-addition
  response retained. Rule text NOT touched (pre-existing rule shared by both arms; editing
  it would asymmetrize the experiment).
- Owner-report finding kept: Opus can read descriptive mentions as "citations" — candidate
  future hardening of the earned-clean rule (define citation = file:line/log-row pointer).
- **Pre-retry F2 targeted check on the fixture edit: spawning; retry counts only on its
  pass.**

## Targeted fixture cold check #3 (pre-retry, single V3-lens edit) — 2026-07-03
- **Worst severity: NITPICK (one, observation-only, outside the edit's scope; routed as
  stated).** Fresh cold reviewer (general-purpose, claude-fable-5). Verbatim record:
  `6-fixture-check-3.verbatim.md`. All 5 checks PASS: V3 unambiguous (zero citations, no
  verification-walk), charter task-addition still acknowledged, no new contradictions,
  mtime-corroborated single-file scope, no rule text introduced.
- Nitpick (the fixture charter's diegetic "zero citations = un-run" quote): pre-existing,
  symmetric across arms, present in round 1 where T1 still missed V3 → neither biases the
  A/B nor trivializes detection. LOG-ONLY.
- **Route: PASS → battery ROUND 2 (the single pre-committed re-run) with 4 FRESH reviewers,
  same prompts/model/arms.** run-record/ re-copied; copy-time hashes re-verified against
  check #3's reviewer-reported list before launch. A second FAIL → stage-8 major → human.

## C3 battery — ROUND 2 — 2026-07-03
- 4 fresh arms (T3/T4 on docs-a; K3/K4 on docs-b; opus, cold, identical prompts). Verbatim
  outputs + scoring + cumulative table + diagnosis: `8-battery-round2.verbatim.md`.
- **Result: FAIL on the frozen condition — V2 treatment 1/2 (T3 miss), V3 treatment 0/2
  (T3, T4 miss).** V1: 2/2 T vs 0/2 K ✓. V4: 4/4 ✓. Tripwire: NOT triggered (all
  control-cited rules author-verified present in docs-b, incl. the comparable-workload rule
  at docs-b:357). Bonus differential evidence: T3 made an unseeded NEW-rule fire (F2 applied
  to C3's harness) that no control produced.
- Cumulative (8 reviewers): V1 4/4-T vs 0/4-K; V2 3/4-T vs 0/4-K; V4 8/8; V3 ≈50% both arms
  (1/4-T, 3/4-K — noise-dominated, no suppression evidence, direction logged → S1 flag).
- **SECOND consecutive FAIL → per the frozen protocol: STAGE-8 MAJOR → human. Loop STOPPED;
  no self-adjudication, no further runs (re-sampling exhausted).** Options to the owner:
  (a) named risk-acceptance for C3's unmet 2/2 bar (evidence recorded as-is), (b) stage-8
  major bounce → re-plan the instrument (unfreeze via logged re-gate, redesign scoring,
  new battery), (c) kill the change. Author recommendation: (a) — the claim C3 exists to
  test (amendments change reviewer behavior) is affirmatively demonstrated by the V1/V2
  differentials + the unseeded F2 fire; the failed components measure pre-existing-rule
  reliability (V3) and instrument design (absolute bar on a target-rich record), not the
  amendments.
- **HUMAN TIE-BREAK (owner, 2026-07-03): option (b) — RE-PLAN THE INSTRUMENT.** Stage-8
  major routes to stage 2. **Criteria UNFREEZE (legal re-gate):** the freeze at
  `c29dfada53cc…` is retired by this logged entry; the ONLY row being redesigned is C3
  (instrument v2 — differential scoring, fixture conformant under both rule sets); all
  other criteria rows unchanged. Criteria re-freeze with a new recorded sha256 at the next
  route-to-build. Re-plan scope (owner's words): differential rates instead of absolute
  2/2; fixture conformant under both rule sets; fresh battery. Loop: plan/criteria delta →
  stage-3 cold review (full F1 provenance) → gate 4 → build fixture v2 → F2 targeted check
  → battery round 3 → score → stage-8 or human.

## Stage 4 gate (v3-delta plan red-team, round 1) — 2026-07-03
- **Worst severity: MAJOR (reviewer's severity; routed as stated).** Counts: 0 blocker,
  4 major (F-2/LO-1, LO-2, F-3, LO-3), 8 minor, 3 nitpick. Fresh cold reviewer
  (general-purpose, claude-fable-5); verbatim record `3-redteam-plan-v3.verbatim.md`
  (reviewer-reported hashes; author spot-checked METHODOLOGY + fixture hashes against prior
  check reports). Reviewer independently re-verified every carried tally against the raw arm
  outputs (all correct) and grep-confirmed the V1/V2 deciding rules are absent from
  `8a7ac65` — the differential premise holds.
- Headline majors: FX-A as specified is NON-conformant under amended F1/F2 (advertised
  targeted check with no provenance record → re-creates the off-seed fire class it defuses;
  the delta's "not citable" leak claim is false on the treatment side); V4's ≥4/6 COMBINED
  bar doesn't enforce firing through the AMENDED docs (3K+1T passes while evidencing
  displacement); "V3 ≈50% in BOTH arms" misstates the true 1/4-T vs 3/4-K record and pools
  across a mid-experiment fixture change; "catch" undefined while the author scores his own
  instrument (three edge precedents already in rounds 1–2).
- **Route: MAJOR → revise the delta (stage 2), then a FRESH stage-3 cold review.** First
  bounce at gate 4 for the v3-delta artifact (the original plan's gate-4 bounces were a
  different targeted artifact; cap not engaged). All 15 findings to be addressed inline,
  tagged [S3-*].
- **Consumer spot-verify:** F-3's per-arm numbers re-checked against the round-1/round-2
  scoring tables (1/4-T vs 3/4-K — confirmed); F-2's "no provenance record in FX-A as
  spec'd" confirmed against the FX-A text (decisions-line + harness note only); LO-5's
  plan-v2 V1-carve-out text confirmed at 2-plan.md:85-87.

## Stage 4 gate (v3-delta plan red-team, round 2) — 2026-07-03
- **Worst severity: MINOR (reviewer's severity; routed as stated).** Counts: 0 blocker,
  0 major, 7 minor (B1–B6, B13), 6 nitpick (B7–B12). Fresh cold reviewer (general-purpose,
  claude-fable-5); verbatim record `3-redteam-plan-v3.round2.verbatim.md`. **Task A: 15/15
  round-1 findings verified RESOLVED against landed text.** The reviewer also cold-verified
  the v2 freeze reconstruction (sha256 exact-match to the recorded `c29dfada…`) and diffed
  it against the live criteria — confirming only the declared regions changed — and
  re-confirmed by its own grep of `8a7ac65` that the V1/V2 deciding rules are new.
- **Route: MINOR → all 13 fixed in place, proceed to BUILD.** Fix summary (tagged [S3-B*]
  inline): B1 hedged-flag sentence governs (T1-V2 precedent pre-registered); B2 F2-checker
  charter names the 6b residual as pre-committed (quoted-as-such; not an A/B arm); B3
  residual adjudication broadened to any amended-F1/charter-core-grounded fire on 6b + 6b
  charter carries the FULL D1 bullet set; B4 displacement-tripwire routes (confirmed →
  stage-8 major → human; refuted → logged, resume); B5 sha256 instruction correctly labeled
  D1-precedented (not "pre-change"); B6 frozen C7's stale "n=2" → "n-limitation (n=3 per
  arm at v3.1)" — a logged CONSEQUENTIAL edit to a non-C3 row, scope-extension recorded
  here, traceable to the owner's re-plan decision + finding B6; B13 the four in-fiction
  scripts enumerated + F2-checker's explicit V2-salience duty; B7 tags normalized, version
  label unified as **v3.1**, per-round qualifier added; B8 model pinned `claude-opus-4-8`;
  B9 superseded-block pointer; B10 pooled-figure erratum appended to the round-2 record;
  B11 no-defect re-run clause (+ the honest P≈0.84 note); B12/cov acknowledged-residuals
  list + scorer-vs-verifier F5 route.
- **CRITERIA RE-FREEZE (v3.1, at route-to-build):** sha256 =
  `4428f612cf9c0792a2d66986bd02850d5b400836c7f8a8f9b5133ae43ce018ad`, verbatim copy saved as
  `1.5-criteria.v3.1-frozen.md` (both mechanisms per [S3-AR-4/MO-5]). The v2→v3.1 diff is
  auditable via `1.5-criteria.v2-frozen.md` (reconstruction hash-verified = `c29dfada…`).
- **PAUSED here by the owner (usage reset), 2026-07-03 eve.** Next actions on resume: build
  fixture v2 (write `6b-harness-check.md` [FX-A] + FX-B relabel + fixture cross-references)
  → F2 targeted check (both doc sets; residual pre-committed in charter) → battery round 3
  (3T+3K, `claude-opus-4-8`) → cold-verified scoring → stage-8 mechanics.

## Fixture v2 build + F2 targeted check #4 — 2026-07-03 (post-pause resume)
- **Resume from the logged pause.** Scratchpad rebuilt + byte-verified: docs-a == source
  (METHODOLOGY 534 / SKILL 124), docs-b == `git show 8a7ac65` (467/102); frozen v3.1
  criteria re-verified: live file AND frozen copy both hash `4428f612…`. Skills repo HEAD
  still `8a7ac65`.
- **BUILD (per the plan addendum):** FX-A `6b-harness-check.md` written — provenance-complete
  in-fiction targeted check of the four harness scripts (full D1 bullet-set charter + the
  D1-precedented sha256 instruction [S3-B5]; task addition quoted-as-such naming the four
  scripts [S3-B13]; exact 9-item context list + hashes; agent/model; short verbatim output
  recording representativeness + fail-against-unguarded for BOTH guards:
  `harness-out/c3-unguarded.log` "stored_copies=2", `harness-out/c1-unguarded.log` first-503
  abort). FX-B: regression sentence relabeled "advisory corroboration — no comparable held
  workload…". Cross-refs added: fixture 8-harness.md Notes + fixture decisions.md Stage-8
  entry (seed text untouched). Post-build hashes: 6b `1eeb25a6…`, 8-harness `64eea8f2…`,
  decisions `5a6d1085…`; the other five files unchanged from check-3's list.
- **F2 targeted cold check #4** (fresh `general-purpose`/`claude-fable-5`, handed BOTH doc
  sets [S3-AR-2]; 6b provenance-bullet residual pre-committed in the charter, quoted-as-such
  [S3-B2]; explicit V2-salience duty [S3-B13]; verbatim record
  `6-fixture-check-4.verbatim.md`): **worst severity MAJOR.**
  **M1** — 6b's output said "already-recorded caveat… (stage-6 flag, carried)" while 6b's
  recorded context list contains no stage-6 artifact: dangling reference + a SECOND
  amended-rule gap beyond the pre-committed residual (potential unseeded fifth violation).
  **m2 (minor)** — in-fiction 2-plan.md hash `5b81c26f…` ≠ the real file `9b6954b5…`
  (pre-existing in 6-redteam-code.md, propagated into 6b; 1.5-criteria's matches). Checker
  confirmed: V2's design SURVIVES 6b (C1 still the only gating verified=yes row with no
  output pointer; failure-demo vs pass-evidence distinction explicit twice), no rule text,
  all four seeds intact at their loci, both cross-refs accurate. n1–n4 nitpicks logged.
- **Route (F5, reviewer's severity governs): MAJOR → fix in place + fresh targeted re-check
  before the battery counts.** First bounce on the fixture-v2 artifact (the cap-fired
  bounces were the round-1 fixture — cap not engaged). **Repairs applied:** M1 — sentence
  reworded to derive the mock's strong consistency from `c3_dedup_mock.py:19-33` itself, as
  a charter-conformant flagged-unverifiable scope note, no stage-6 reference; bottom line
  updated to acknowledge the flag. m2 — hash aligned to `9b6954b5…` in BOTH
  `6-redteam-code.md:25` and `6b-harness-check.md` (same alignment move as check-1's M1
  criteria-hash fix); `grep 5b81c26f` over the fixture → no hits. V3's locus
  (`6-redteam-code.md:31-32`) untouched. Post-repair hashes: 6b `c36779a7…`,
  6-redteam-code `43eb026d…`. n1–n4: no action (n1 mitigated/pre-existing convention; n2
  pre-existing + part of V2's design context; n3 harmless; n4 inherent to the edit's purpose).

## F2 targeted re-check #5 (post-repair) — 2026-07-03
- **Worst severity: NITPICK → PASS.** Fresh cold checker (`general-purpose`/`claude-fable-5`,
  BOTH doc sets; verbatim record `6-fixture-check-5.verbatim.md`): M1 RESOLVED (grep-clean of
  stage-6/carried/caveat references; reworded note charter-conformant, source-cited from the
  6b context list, bottom line coherent); the PRE-COMMITMENT NOW HOLDS (fresh-eyes pass: the
  charter provenance-bullet residual is the ONLY amended-rule gap in the 6b record — the duty
  check-4 could not discharge); m2 RESOLVED (both in-fiction 2-plan hashes match the real
  file; `5b81c26f` grep-clean; full hex inventory shows no other on-disk-referent mismatch);
  blast radius CLEAN (two-file repair corroborated by mtime; V1–V4 intact, V3's lens
  untouched; no rule text, no new violation under either doc set). One nitpick (n1: 6b's
  soft "stage-8 table" forward references — reviewer classes them near-forced inference from
  the charter's own framing, not an amended-rule gap) — logged, no action. Author note: the
  checker's prose transcription of 6-redteam-code.md's hash garbled to an invalid 62-char
  string mid-sentence; prefix/suffix match the author's computed `43eb026d…596cfc` and its
  content citations confirm the repaired file was read — cosmetic, recorded in the verbatim
  record. **Fixture v2 fit for the battery.**

## C3 battery ROUND 3 (instrument v3.1) — 2026-07-03
- **Launch:** 6 fresh cold arms (3T docs-a + 3K docs-b), `general-purpose`,
  `claude-opus-4-8` [S3-B8], parallel background, rounds-1/2 verbatim prompt template
  (incl. [FC1-note]); run-record re-copied post-check-5, all 8 copy-time hashes verified;
  docs-a/docs-b re-verified byte-identical at launch [S3-AR-5]. All six arms returned final
  outputs — dead-arm policy not exercised; every run counted. Verbatim outputs + author
  scoring: `8-battery-round3.verbatim.md`.
- **Author scoring (per the pre-registered extraction rule):** V1 **3/3-T** vs 0/3-K
  (provenance rule among grounds, all three); V2 **2/3-T** vs 0/3-K (T5 = the pre-registered
  hedged-flag-governs shape, T1-V2 precedent; T7 unhedged; T6 miss with a recorded
  "evidence cited" misread); V4 **3/3-T AND 3/3-K** (per-arm floors met); V3 observational
  **0/3-T, 1/3-K** (cumulative 1/7-T vs 4/7-K; three engaged-and-misread misses recorded —
  diligence-halo corroboration). Confound tripwire NOT triggered (all control grounds
  grep-verified present in docs-b; V1/V2 grounds grep-verified absent). Displacement
  tripwire NOT triggered (requires ≥2/3-K; observed 1/3-K). Off-seed fires: T6's C3
  pass-rate-floor (docs-b-reachable, non-seed row, no contamination); K6's
  stage-8-table-never-audited ("Nothing self-certifies" + label-audit bullet, both
  docs-b-reachable, no contamination). **ZERO fires of the round-1/2 killer class — FX-A
  defused it (all six arms used `6b-harness-check.md` as load-bearing evidence); the
  pre-committed 6b charter residual was never touched; FX-B classified correctly-advisory
  by every arm that mentioned it.**
- **Targeted cold scoring-verification [S3-MO-3]** (fresh `general-purpose`/`claude-fable-5`;
  verbatim record `8-battery-round3-scoring-verification.verbatim.md`): **24/24 cells
  confirmed; both edge calls correctly decided; all reachability claims grep-verified
  (incl. docs-b:451 itemized); both tripwires confirmed not-triggered; arithmetic confirmed.
  Verdict: scoring faithful YES; ROUND 3 = PASS stands YES.** Four completeness notes
  (none scoring-relevant) appended to the round-3 record as an addendum.
- **Disposition (pre-committed): C3 = PASS.** Verdict duties carried per [S3-LO-6]/[S3-B6]:
  n=3 per arm this round (13 arms cumulative); rounds-1/2 history carried verbatim in the
  round-3 record (V1 4/4-T vs 0/4-K; V2 3/4-T vs 0/4-K; V4 8/8; V3 1/4-T vs 3/4-K pooled
  4/8 across two fixture wordings); per-arm V3 record 0/3-T, 1/3-K this round; **honest
  driver: the owner-authorized V3 demotion to observational — not the differential scoring
  change — is the largest single driver of the round-3 pass probability (under round-2
  rules this V3 record would have failed again).** → Proceed to stage-8 mechanics
  (C4/C5/C6, install, 8-harness.md, gate).

## Stage 8 gate — 2026-07-03 — ACCEPT
- **All six gating criteria `verified = yes` with evidence pointers** (8-harness.md, the
  first table emitted under the new F3 evidence-column rule): C1 18/18 location checks
  (quoted text + file:line per mapping row); C2 7/7 sweep items reconciled; C3 EXECUTED
  battery PASS, scoring cold-verified 24/24; C4 `wc -l` = 534/124/658 vs caps 583/127/671;
  C5 install → `diff` empty both files (live == source); C6 12/12 hunks walked, no rule
  deleted or weakened (M1/M3 in-place-extension enumeration note recorded). C7 advisory
  surfaced — duties discharged in `9-report.md` (S1–S3 owner decisions, C3 honesty block
  incl. the pre-committed V3-demotion driver sentence, residual-displacement note,
  earned-clean ~45% finding + future-hardening candidates, attention spend 658/671).
- **Criteria freeze verified at harness time:** `1.5-criteria.md` == `4428f612…` == the
  verbatim frozen copy. No post-freeze drift.
- **Route: ACCEPT.** Install already done (AR-7, at stage-8 start). → Commit + push the
  source files + change record. Guarded-change hardening phase COMPLETE; dragonfly phase
  next (its 14+3 findings run through THIS hardened loop).
