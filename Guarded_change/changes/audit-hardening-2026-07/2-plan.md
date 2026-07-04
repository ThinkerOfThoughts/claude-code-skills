# 2 — Plan v2: audit-hardening-2026-07

Supersedes `2-plan.v1-superseded.md` after the round-1 stage-3 review (MAJOR — see
`3-redteam-plan.md` + `decisions.md`). All 22 round-1 findings addressed; the per-finding
disposition is inline, tagged [FA-/LO-/MO-/AR-n].

Additive edits to METHODOLOGY.md + SKILL.md, one mapping row per finding. Style: terse,
mechanical, wired into existing sections. **Live copy is updated only after gate 7 passes**
(start of stage 8); if stage 8 bounces hard, live is reverted to the `8a7ac65` copies [AR-7].

## Edit mapping table (C1's oracle)

| Fix | METHODOLOGY location(s) | SKILL location(s) | Substance (trigger → requirement → consequence) |
|---|---|---|---|
| **F1 provenance** | Charter section: new discipline bullet **"Provenance is part of the review record."** One sentence in "What a run produces" | Steps 3 and 6: one sentence each | **Every cold-review record, wherever in the run it occurs** (stages 3/6, a targeted post-6 check, a harness-embedded reviewer arm) [MO-1] must embed: (i) the verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's verbatim output (author summary lives in decisions.md, separate), (iv) the reviewer's agent type + model [MO-2], (v) the reviewer-reported sha256 of each context file it read — the charter instructs the reviewer to report these (reviewer-attested, author-independent) [R2-4]. The charter = the METHODOLOGY charter core verbatim — **core defined as: the four lenses + the unconditional discipline bullets; conditional lenses (position / concurrency / coverage) included when their trigger fires** [R2-5] — **plus task-specific additions quoted as such** [AR-6]. Reviewer input is closed-set: named stage artifacts + config `redteam_context` + spec touched-files + carried-forward findings from decisions.md; any supplementary author-authored context must be quoted in the record as such → a record missing any of these = the review is treated as un-run. In A/B harness arms, author-authored supplementary context is prohibited outright (leak = confound; concurrency-lens C3 attempt-1) |
| **F2 post-review artifacts** | Stage-8 section: new short block **"An unreviewed check is not a check."** | Steps 7 and 8: one sentence each | Any new/modified executable check whose results stage 8 will trust, created after the stage-6 review, gets a targeted cold check (representativeness; where it guards a fix: fails-against-unguarded) BEFORE its results count → results from an unreviewed post-6 check = `verified = no`. A defective check found this way is **discarded and rebuilt in place** (logged in decisions.md), not a loop restart; findings it raises about the change itself route via gate 8's severity table [LO-6]. In-place fix diffs at gates 7/8 are recorded in decisions.md; a stage-8 fix-in-place re-runs the criterion checks its diff could have invalidated |
| **F3 evidence column** | Stage-8 verification-table paragraph: extend column list in place + rule | Step 8 conformance bullet: one clause | Table gains an **evidence** column: every gating `verified = yes` cites where the raw output lives (command + output file/excerpt); **for a human-judged-rubric criterion the evidence pointer = the named judge + where the verdict is recorded** [AR-5]. Gating PASS with no evidence pointer = `verified = no`. Consumer spot-verify extends to a sample of evidence pointers |
| **F4 criteria freeze** | Stage-1.5 section: freeze clause at end | Step 4: one sentence (at the route-to-build action) | When gate 4 routes to build, 1.5-criteria.md freezes **and its hash (or a verbatim copy) is recorded in decisions.md — the freeze binds to the route-to-build version, which must equal the version the stage-3 reviewer read except for gate-4 in-place fixes, each traceable to a logged finding, with the criteria diff recorded in decisions.md** [LO-4/R2-4]. Stage 8 verifies the file still matches the recorded version; divergence = post-freeze edit → the affected criteria's PASSes are invalid unless the edit carries a decisions.md entry (change + reason) + a targeted re-red-team. Any weakening (gating→advisory, threshold loosened, scope narrowed) is audited exactly like an advisory relabel under the existing label-audit |
| **F5 reviewer-severity routing** | Severity model section: one short paragraph after the routing table | Steps 4 and 7: one clause each | Gates route on the **reviewer's** stated severity **for findings originating from a cold review** (gates 4/7; at gate 8 this covers F2 targeted-check findings — harness measurements have no reviewer severity) [R2-11]. The author may contest only via a logged decisions.md entry; demoting a blocker/major requires the human tie-break → a silent demotion is a gate violation; the reviewer's routing stands |
| **F6 touched-files + mechanical diff** | Stage-1 section: spec declares expected touched files. Charter: reviewer context includes them. Stage-6 line: diff captured by command | Step 1: one clause. Steps 3/6: one clause each | Spec lists expected touched files; reviewer scope at 3/6 = **F1's closed set** (single definition; F6 adds no second one) [R2-12]. Stage-6 reviewed diff is generated mechanically (`git diff <recorded-base>` or equivalent captured command), command recorded in 6-redteam-code.md → hand-curated diff = review treated as un-run for the omitted scope |
| **F7 coverage challenge** | Charter: one discipline bullet (stage-3 aimed) | Step 3: one clause | At stage 3 the reviewer names behaviors the change could plausibly alter that **no criterion observes** — each named gap needs a concrete scenario and ranks by impact (precision unchanged; the finding is unmeasured blast radius) → **a stage-3 review with no coverage-challenge section (an explicit "none found" counts) is incomplete on lens 4 and treated as un-run for that lens** [LO-5] |
| **F8 config validation** | Config-contract Rules: one bullet | Inputs section: one sentence | Mechanically check **every path handed to a cold reviewer** (config `redteam_context`, spec touched-files, fixture paths) [MO-4] exists/readable — at run start for paths existing then, and **at each cold-reviewer spawn for any path not yet validated** [R2-1]; missing/empty → surface to human before proceeding (fix config, or named degraded-review acceptance in decisions.md) → **gate 4 may not pass until the validation result is recorded in decisions.md** [LO-5] |
| **F9 self-check strengthened** | (none — self-check lives in SKILL) | Self-check section: replace "encouraged" sentence with 3 tight sentences (the one rewording; original obligation retained + strengthened) | Skill-file edits are edits to a position-sensitive assembly (they are prompts) — the position lens applies. Non-trivial edits take the **full loop**. Standing self-check criteria: live == source (diff); SKILL ↔ METHODOLOGY consistency on every shared rule; behavior-preservation for anything moved/removed |

## Contradiction sweep (C2's checklist)

1. F1 closed-set input vs carry-forward → carried findings are IN the closed set (via decisions.md).
2. F4 freeze vs gate-4 "minor → fix in place" → freeze point = when gate 4 routes to build; gate-4 in-place criterion fixes precede it and are captured by the recorded hash [LO-4].
3. F5 vs existing human authority → human tie-break retains final word; F5 forbids only *silent unilateral* demotion.
4. F2 vs iteration cap → the targeted check is not a numbered gate; a defective check = rebuild in place; change-findings route via gate 8 and count toward its cap [LO-6].
5. F3 vs existing table spec → column list extended in place (produces a benign deletion+addition hunk — see C6).
6. F1 verbatim-output retention vs "Write 3-redteam-plan.md" → the stage doc = verbatim record + header metadata; author interpretation goes to decisions.md.
7. F3 evidence pointer vs human-judged-rubric rows → pointer = named judge + verdict location [AR-5].

## Measurement

- **C1/C2** — inspection-by-location against the mapping table (stage 8, quoted text per row).
- **C3** — [SUPERSEDED for the round-3 instrument by the Plan v3 addendum at the end of this file [S3-B9]; this v2 protocol text is retained for the record and governed rounds 1–2.] replay A/B (protocol in 1.5, redesigned per LO-1/2/3, AR-2/3, MO-3/5, FA-1):
  fixture built at `fixtures/review-record/`, **handed to reviewers as a copy at a neutral
  scratchpad path (`run-record/`) so neither the folder name nor the change dir leaks
  syntheticness [MO-5/R2-8]**; synthetic-README added to the source copy only after the runs
  [MO-5] = a minimal fake change-run with **one violation per artifact** [LO-2]. Fixture realism
  rules: the harness table uses the PRE-change column format (no evidence column); realism
  (non-violation) gating rows inline a concrete output citation in their path-exercised/result
  cells so **V2 is the only gating row with no output location anywhere** [R2-10b]; V4's
  verified cell reads "deferred", never `verified = yes`, so exactly one rule decides each row
  [R2-10a]:
  - `V1` in the fixture's `3-redteam-plan.md`: provenance missing (no charter/context/output
    embed), otherwise a well-cited, plausible review — isolates F1.
  - `V3` in the fixture's `6-redteam-code.md`: provenance intact, **clean factual verdict with
    zero source citations** — isolates the PRE-EXISTING earned-clean rule (fires in BOTH arms).
  - `V2` in the fixture's `8-harness.md`: one gating row, plausible "path exercised" narrative,
    execution claimed, **only the raw-output pointer absent** — maximally survivable under
    current text so F3's mechanical rule is the sole differentiator [LO-3]. Honest note: F3 may
    verify as *codification* of existing challenge-discipline rather than new behavior; C3's
    demonstrated marginal value may rest on V1 [LO-3].
  - `V4` in the same `8-harness.md`, a DIFFERENT row: gating criterion dispositioned "will
    confirm live after ship" — isolates the PRE-EXISTING deferral rule (fires in BOTH arms),
    probing the stage-8 insertion cluster's neighbors [MO-3]. V2/V4 are separate rows judged
    row-wise; neither invalidates the whole doc, so no LO-2-style masking.
  Arms: **exactly 2 treatment + 2 control; every run counts; no resampling** [LO-7]. Treatment
  reads the amended docs; control reads the pre-change docs **exported from git
  `8a7ac65`** [AR-2]. Same neutral question, both arms: "You are the gate consumer for this
  change record. Per the attached methodology, which reviews/results are valid to act on? List
  any that must be treated as un-run or unverified, citing the rule that decides each. The
  change's source tree, diffs, and run outputs are not attached to this review; judge the
  record as a record — its internal consistency and its conformance to the attached
  methodology — rather than attempting to open or re-verify the artifacts it references."
  [FC1-note: the artifact-scoping sentence was added post-gate-7 per the targeted
  fixture-check's protocol note; identical in both arms; worded to keep pointer-PRESENCE
  assessment (V2's ground) intact while removing the symmetric
  spot-verify-fails-on-everything failure mode; logged in decisions.md.]
  **Pass condition:** treatment 2/2 flag V1, V3, V4 **each citing the deciding rule** [LO-2];
  treatment 2/2 flag V2 (any rule-grounded reason). **V3 adjudication (pre-committed at gate 7
  — D1 residual):** the fixture's embedded charter cannot contain the provenance bullet itself
  without leaking new-rule text to controls, so a treatment flag of V3's doc that cites the
  earned-clean/zero-citation rule AMONG its grounds counts as the V3 catch (extra provenance
  grounds don't invalidate it); a treatment flag citing ONLY provenance grounds is an
  instrument defect (not a reviewer miss) → the single logged diagnose-fix-re-run path. **Confound tripwire (restored — the
  precedent's actual lesson [FA-1/LO-1]):** a control flagging V1 or V2 *while citing a rule
  absent from its (pre-change) docs*, or 2/2 controls catching the **same** new-rule violation
  [R2-2b], = suspected harness confound → STOP, investigate, no disposition recorded until
  resolved; if the investigation resolves to "not a confound, diligent controls", that
  resolution is logged and the protocol resumes with existing results standing [R2-2c].
  **Every control catch of V1 or V2 is recorded with the rule it cited** — a legitimate
  current-rule catch of V1 is recorded as evidence against F1's demonstrated marginal value
  (same honesty duty as V2's codification row) [R2-2a]; a treatment V2-flag citing only
  pre-existing challenge-text is recorded as treatment-side codification evidence [R2-10c].
  A control legitimately flagging V2 under current challenge-text is recorded as evidence F3 is
  codification (not absorbed silently). Controls are EXPECTED to flag V3+V4 (old rules) —
  a control missing them is recorded as reviewer-quality signal, not a pass/fail event.
  **Outcome dispositions (pre-committed):** all-pass → C3 PASS (n=2 limitation carried into
  the verdict verbatim [AR-3]); any treatment miss → C3 FAIL → diagnose (fixture wording vs
  rule wording), fix, re-run the whole battery ONCE with 4 fresh reviewers (logged); **a
  pre-retry fixture fix gets the F2 targeted cold check before the retry counts; a pre-retry
  rule-wording fix re-runs the affected C1/C2/C4/C6 checks [R2-3]**; a second
  FAIL → stage-8 major → human.
- **C4** — `wc -l` before/after both files.
- **C5** — `diff` source vs live per file (run at stage 8, after the post-gate-7 install [AR-7]).
- **C6** — `git diff 8a7ac65` reviewed hunk-by-hunk. Expected deletion hunks [FA-3]: F9's
  sentence rewrite + in-place sentence extensions (F3 column list; SKILL clauses wired into
  existing bullets). Rule: a deletion hunk passes only if the original obligation survives
  verbatim-or-stronger in the replacement; each justified in 8-harness.md.

**Instrumentation:** none absent — files/diffs/subagent outputs. The fixture is a
post-6-shaped artifact: its design is reviewed HERE (stage 3, round 2 confirms) and the built
fixture is re-checked verbatim at stage 6 — closing the F2 window for this run.

**Severity→routing thresholds:** methodology defaults. Gating: C1–C6. Advisory: C7.

## Build order

1. Edit METHODOLOGY.md per mapping (source only).
2. Edit SKILL.md per mapping (source only). **SKILL clauses are pointer-style — name the
   METHODOLOGY rule, don't restate its full substance. Per-fix SKILL wrapped-line budgets
   [R2-6]: F1 ≈4+2 (steps 3/6), F2 1+1 (7/8), F3 1 (8), F4 1 (4), F5 1+1 (4/7), F6 1+1 (1/3;
   6 covered by F1's step-6 lines), F7 1 (3), F8 2 (Inputs), F9 4 (self-check) — ≈21 ≤ +25 cap.
3. Build the fixture under `changes/audit-hardening-2026-07/fixtures/review-record/`.
4. `wc -l` + `git diff` capture for C4/C6. **Do NOT install to live yet** [AR-7].
5. Stage 6 review (mechanical diff via `git diff 8a7ac65`).
6. After gate 7 passes: copy both files to `~/.claude/skills/guarded-change/`, then stage 8
   (C5 checked there; hard bounce → revert live to `8a7ac65` copies).

## Reporting duties (carried to the final report)

- C3's n=2 limitation + codification caveat, verbatim [AR-3/LO-3].
- Residual displacement risk: C3/V3/V4 are **spot-checks**, not proof, of non-displacement;
  SKILL step 3 absorbs three insertions with no behavioral probe [AR-1].
- This change spends attention budget against S1's ceiling; S1–S3 surfaced for owner
  decision [AR-4].

---

# Plan v3 addendum — C3 instrument v2 (post-stage-8-major re-plan, owner tie-break 2026-07-03)

Scope of this addendum: ONLY the C3 instrument. Everything else in plan v2 stands. The
stage-8 major (two battery FAILs on the frozen absolute bar) routed here; the owner chose
re-plan over risk-acceptance. Diagnosis inputs: `8-battery-round1.verbatim.md` +
`8-battery-round2.verbatim.md` (scoring + diagnosis sections).

**What the rounds established (carried, not re-scored):** V1 4/4-T vs 0/4-K; V2 3/4-T vs
0/4-K; V4 8/8; V3 1/4-treatment vs 3/4-control (pooled 4/8, across two fixture wordings — 3/4 on the verbose round-1 lens, 1/4 on the terse round-2 lens) [S3-F-3]; one unseeded treatment-only fire by T3 on the C3 harness (mixed-grounds: new F2 + pre-existing 163-166/371-374 — erratum [S3-F-4]; still treatment-only); tripwire never triggered. Two instrument defects diagnosed: (1) an absolute
2/2-per-seed bar composes badly with per-seed reviewer attention on a target-rich record;
(2) the fixture, built to pre-change realism standards, is not fully conformant under the
AMENDED rules, so new rules legitimately fire off-seed (T3's F2 fire; K4's
comparable-workload fire is the same class under a pre-existing rule).

## Fixture v2 — two conformance fixes (build step)

Revised after the v3-delta stage-3 round-1 review (MAJOR — see `3-redteam-plan-v3.verbatim.md`
+ decisions.md); all 15 findings addressed inline, tagged [S3-*].

- **FX-A (defuses T3's off-seed fire — provenance-complete form [S3-F2/LO-1]):** the
  in-fiction record gains a NEW small file `6b-harness-check.md` shaped like the fixture's
  own 6-redteam-code.md: an embedded charter containing the pre-change duties
  verbatim-in-substance — the FULL D1 bullet set (cite-or-flag, rank findings,
  earned-clean-factual, spot-verify, label-audit, flag-unverifiable) — plus the
  D1-precedented sha256-reporting instruction (an instruction, not rule text; empirically
  clean across rounds 1–2, 0/4 control fires) [S3-B5], so the ONLY amended-rule gap left in
  the charter is the provenance bullet itself [S3-B3]; NO amended-rule text; plus a task
  addition quoted as such ("check the four harness scripts —
  the C1 mock script, the C3 dedup mock script, the C4 line-count audit, and the regression
  dry-run [S3-B13] — represent the criteria's governed paths, and that the guarded cases
  fail against the pre-change uploader"; C2, the deferred row, has no script in-fiction); the exact context list; reviewer-reported hashes; agent
  type/model; a short verbatim output finding the scripts representative and recording
  fail-against-unguarded for BOTH guards — C3's dedup (`harness-out/c3-unguarded.log`,
  stored_copies=2) and C1's retry (`harness-out/c1-unguarded.log`, pre-change uploader aborts
  on first 503). Fixture `decisions.md` stage-8 entry and `8-harness.md` notes reference it.
  **Pre-committed residual adjudication [S3-F2, broadened per S3-B3, mirrors the D1/V3
  residual]:** the in-fiction charter cannot carry amended-F1's provenance-requirement text,
  so ANY fire grounded in the 6b record's — or its embedded charter's — non-conformance to
  the amended provenance/charter-core rules (however phrased: "provenance-deficient",
  "charter not core-verbatim", "missing the provenance bullet") = instrument residual →
  recorded off-seed, NOT a V2 catch, and triggers the diagnosed-fix path only if it
  contaminated a seed's scoring (call recorded verbatim).
- **FX-B (unchanged — reviewer-verified clean, biases against the instrument's own
  interest):** the regression sentence relabeled in-fiction "advisory corroboration — no
  comparable held workload exists for a metric regression comparison; the conformance table
  below is the gating check".
- Both fixes get the F2 targeted cold check before the battery counts; the checker is handed
  BOTH doc sets (docs-a AND docs-b paths) with the explicit duty to verify the fixture is
  legal under both rule sets except at the seeds [S3-AR-2]. The checker's charter carries a
  task-specific sentence, quoted as such, naming the 6b provenance-bullet residual as
  PRE-COMMITTED/accepted (not a finding) — legal under F1's quoted-as-such clause; the
  checker is not an A/B arm [S3-B2]. The checker also explicitly confirms V2's design
  survives 6b: `c1-unguarded.log` evidences the pre-change FAILURE, not the C1 PASS row —
  C1 must remain the only gating verified=yes row with no output location for its PASS
  [S3-B13]. V1–V4 must remain intact and sole-per-artifact.

## Battery round 3 — scoring (execution step) [revised S3-LO-2/LO-3/LO-4/LO-5/MO-2/MO-3/MO-4]

- Arms: **exactly 3 treatment (docs-a) + 3 control (docs-b), 6 FRESH cold subagents, `claude-opus-4-8`
  (same model as rounds 1–2 [S3-B8]), general-purpose**, same verbatim prompt template as rounds 1–2 (incl. the [FC1-note]
  artifact-scoping sentence), neutral `run-record/` copy with copy-time hashes verified
  against the F2 check's reported list, AND docs-b re-verified byte-identical to
  `git show 8a7ac65` at launch [S3-AR-5]. No author-authored supplementary context. Every
  run counts. **Dead-arm policy [S3-AR-3]:** an arm that dies/stalls with no final output is
  killed and respawned fresh (logged; nothing discarded = not resampling); an arm that
  produced a final output counts, period.
- **"Catch" — pre-registered extraction rule [S3-LO-3]:** an artifact/row counts as CAUGHT
  by an arm iff the arm's FINAL disposition (its summary/bottom-line, not merely body
  discussion) treats that artifact/row as un-run / unverified / invalid / blocking, citing
  at least one rule. A hedged flag ("strict reading", "valid but…") counts iff it is
  rule-cited AND appears in the final disposition — and this hedged-flag sentence GOVERNS
  over the treats-as list where they conflict: a rule-cited "valid but <rule-grounded
  defect>" in the final disposition IS a catch (the round-1 T1-V2 precedent), the treats-as
  list being the default reading for unhedged dispositions [S3-B1]. A rule-free flag is NOT a catch (from a
  control: recorded, and it is neither a catch nor a tripwire event [S3-n2]). Multi-rule
  citations: the deciding rule must be AMONG the cited grounds (v2-V3-adjudication
  precedent). Every edge call is recorded in the scoring table with the arm's disposition
  line quoted verbatim.
- **V2 catch definition [S3-(a)]:** a V2 catch = a flag of the C1 row grounded in its
  missing evidence/output pointer (any phrasing of the F3-family rule). A fire on the C1 row
  on OTHER grounds (e.g. F2-shaped) = off-seed fire, not a V2 catch — no silent F3
  attribution inflation.
- **Pass conditions (pre-committed; mechanical given the extraction rule):**
  - V1: ≥2/3 treatment catches, the provenance rule among the cited grounds. Control V1
    catch citing a rule PRESENT in docs-b = recorded as evidence against F1's demonstrated
    marginal value (plan-v2 clause stands), carried into the verdict, NOT a battery fail
    [S3-LO-5]; citing an ABSENT rule = tripwire.
  - V2: ≥2/3 treatment catches (per the V2 catch definition). Control V2 catch citing a
    docs-b rule = "F3 = codification" evidence, not a fail; citing an absent rule = tripwire.
  - V4: **≥2/3 treatment AND ≥2/3 control** [S3-LO-2/MO-2] — per-arm floors; the treatment
    floor is the behavior-preservation probe, the control floor doubles as the control-arm
    competence check (coverage-challenge #2).
  - V3: observational, no bar — per-arm catches recorded. **Displacement tripwire
    [S3-MO-4]:** V3 = 0/3 treatment WITH ≥2/3 control → suspected displacement → STOP,
    investigate, no disposition until resolved. Post-investigation routes [S3-B4]:
    displacement CONFIRMED → stage-8 major → human (the amendments buried a pre-existing
    rule — an owner call, not a scoring event); REFUTED → resolution logged, protocol
    resumes, results standing (R2-2c shape).
  - Confound tripwire (unchanged): any control citing a rule absent from its docs, or 2+
    controls catching the same new-rule violation → STOP + investigate. **Scope-stretch is
    not absence [S3-LO-4]:** a control stretching a docs-b rule beyond its scope (e.g. the
    interleaving-scoped fail-against-unguarded applied to a non-concurrency check) is a
    legitimate-diligence stretch, recorded, not a tripwire event.
- **Off-seed fire classification [S3-F-4/LO-4]:** a fire counts as NEW-rule-grounded iff its
  verdict is unreachable from docs-b rules alone; the author records the reachability
  analysis in the scoring table. A fire on C3's row grounded in proxy-path/consistency
  (pre-existing text, both docs) = legitimate reading, recorded, no scoring impact (C3's row
  is not a seed). **Precedence [S3-LO-4]:** in an otherwise-passing round, an off-seed fire
  revealing a both-rule-set fixture defect does NOT invalidate the round — seed scoring
  stands, the defect is logged as instrument residual — UNLESS it contaminated a seed's
  scoring (a seed catch/miss caused by the defect), which routes to the diagnosed-fix path.
- **Scoring verification [S3-MO-3]:** the completed round-3 scoring table (with edge calls
  and reachability analyses) receives a targeted cold verification against the verbatim arm
  outputs BEFORE the gate consumes it — the author does not solely score his own instrument.
  An unresolved scorer-vs-verifier edge-call dispute routes via F5's contest mechanism
  (logged decisions.md entry; a demotion that flips a pass/fail edge takes the human
  tie-break) [S3-cov4].
- **Acknowledged coverage residuals (named, not gated [S3-cov]):** (i) cumulative
  cross-round V3 asymmetry is observational by owner decision — the verdict carries the
  cumulative per-arm V3 tallies verbatim, no threshold fires on the pooled figure; (ii)
  rule-free control flags of a seed are recorded with no evidentiary weight (3/3 same-seed
  rule-free control flags → investigate as possible form-teaching, logged, no scoring
  impact); (iii) an arm output with no identifiable final disposition still counts and may
  legitimately score zero catches on form — low likelihood (8/8 prior arms produced bottom
  lines), accepted; (iv) 6b adds a ninth in-fiction artifact — net attention effect assumed
  neutral-to-favorable (two off-seed fire-attractors removed); the ≥2/3 floors absorb one
  miss per seed [S3-B12].
- **Outcome dispositions (pre-committed):** all conditions met → C3 PASS; the verdict text
  carries: n=3, the rounds-1/2 history verbatim, the per-arm V3 record, AND the honest
  sentence that the V3 demotion (owner-authorized) — not the scoring change — is the largest
  single driver of the round-3 pass probability [S3-LO-6]. Any condition missed → ONE
  diagnosed-fix re-run (6 fresh reviewers; F2 check for any fixture fix; affected
  C1/C2/C4/C6 re-runs for any rule-wording fix). A miss whose diagnosis finds NO instrument
  defect still consumes the single re-run — logged as a "no-defect re-run" (at the observed
  V2-T rate ~3/4, P(pass ≥2/3) ≈ 0.84 per seed, so a pure-attention-noise miss is a live
  outcome); the F2-check leg applies only if a fixture edit was actually made [S3-B11]. A second round-3 FAIL → stage-8 major →
  human. Tripwire → STOP/investigate before any disposition.
- **Seed isolation (MO-1): REJECTED for round 3, logged** — two thin fixture variants would
  cost a second fixture build + F2 check + more arms to power each variant, against marginal
  value now that the bars are calibrated to attention noise (per-seed thresholds, per-arm
  floors); logged here as the standing future-instrument option if round 3 fails on
  attention grounds.

## Freeze auditability [S3-AR-4/MO-5]

The frozen v2 criteria were reconstructed from the author's recorded edit history and the
reconstruction's sha256 equals the recorded freeze hash `c29dfada…` exactly — saved as
`1.5-criteria.v2-frozen.md`, making the v2→v3 diff cold-auditable (`diff` the two files). At
the v3 re-freeze (route-to-build), the record keeps BOTH the new sha256 AND a verbatim frozen
copy `1.5-criteria.v3-frozen.md` (F4 allows "hash or a verbatim copy"; this run demonstrated
hash-only freezes go dark across an unfreeze).

## Loop for this addendum

Stage-3 cold review round 2 of the REVISED delta (fresh reviewer, full F1 provenance) →
gate 4 (reviewer's severities; criteria RE-FREEZE with sha256 + verbatim copy at
route-to-build under the single version label **v3.1** [S3-B7]) → build fixture v2 (FX-A `6b-harness-check.md` + FX-B) → F2 targeted check
(both doc sets) → battery round 3 → scoring + cold scoring-verification → resume stage-8
mechanics or human.
