# 3 — Red-team ROUND 2 (verbatim record)

> Provenance: reviewer = cold `general-purpose` subagent, no shared context, model
> claude-fable-5 (inherited). NOTE: the first round-2 spawn stalled/died in a network outage
> after reading only part of its context; it was killed and a fresh cold reviewer respawned
> with the identical prompt — no findings or partial output from the dead spawn were carried
> or consumed. Context given (closed set): the six change docs (decisions.md,
> 3-redteam-plan.md [round-1 verbatim], 0-audit-findings.md, 1-spec.md, 1.5-criteria.md v2,
> 2-plan.md v2, + 2-plan.v1-superseded.md) + redteam_context {METHODOLOGY.md, SKILL.md,
> concurrency-lens/{decisions,8-harness,1.5-criteria}.md}. No supplementary author context.
> The verbatim prompt differs from round 1 (it is a disposition-check + fresh-attack charter);
> it is recorded below, then the reviewer's verbatim output.

## The verbatim prompt given to the reviewer

```
You are a cold, independent red-team reviewer with NO shared context with the author. This is
ROUND 2 of a stage-3 plan review inside a guarded-change run: a prior cold reviewer returned
MAJOR, the author re-planned, and your job is to (a) verify every round-1 finding was actually
addressed in the revised docs — confirm against the text, don't take the author's word — and
(b) attack anything NEW the revision introduced. You are graded on PRECISION. "Resolved" and
"no new issue" are valid verdicts when true, but must be earned with citations.

## Artifacts under review (read in this order)

1. .../decisions.md — the gate log (round-1 route + what was promised)
2. .../3-redteam-plan.md — round-1's verbatim findings (FA-1..4, LO-1..7, MO-1..5, AR-1..7).
   This is your checklist.
3. .../0-audit-findings.md — the audit input (now carries an erratum addressing FA-2)
4. .../1-spec.md
5. .../1.5-criteria.md — REVISED (v2)
6. .../2-plan.md — REVISED (v2; v1 preserved at 2-plan.v1-superseded.md for diff if useful)

## Source to check claims against (redteam_context, priority order)

1. /home/zero/Desktop/claude-code-skills/Guarded_change/METHODOLOGY.md (current, pre-change)
2. /home/zero/Desktop/claude-code-skills/Guarded_change/SKILL.md (current, pre-change)
3. .../changes/concurrency-lens/decisions.md, 8-harness.md, 1.5-criteria.md (the precedent
   round 1 said was miscited — verify the v2 docs now cite it correctly)

## Your tasks

TASK A — Round-1 disposition check. For EACH of the 22 round-1 findings (8 major: FA-1, LO-1,
LO-2, LO-3, LO-4, LO-5, MO-1, AR-1; 11 minor: FA-2, FA-3, FA-4, LO-6, LO-7, MO-2, MO-3, MO-4,
AR-2, AR-3, AR-4, AR-5; 3 nitpick: MO-5, AR-6, AR-7): state RESOLVED / PARTIALLY RESOLVED /
NOT RESOLVED, citing the exact v2 text (file + section/line) that resolves it or fails to. Do
not mark resolved on the author's say-so — check the actual wording closes the loophole round
1 described.

TASK B — Fresh attack on the revision, four lenses (factual / logical / missed opportunity /
unstated assumptions & risks). Focus fire on: (1) the redesigned C3 protocol —
one-violation-per-artifact fixture (V1/V2/V3/V4 placement, incl. V2+V4 sharing 8-harness.md as
separate rows — is the author's "no masking, judged row-wise" argument sound?), the restored
confound tripwire, the pre-committed outcome dispositions including the one-retry rule — can
it still produce a false PASS or false FAIL? (2) the F4 freeze-hash mechanism — actually
airtight now, or still gameable? (3) the F7/F8 consequences — enforceable as written? (4)
whether the nine mapping-table substances are still terse enough to plausibly land within C4's
caps (METHODOLOGY ≤583, SKILL ≤127, combined ≤671 from 467/102/569). (5) any NEW contradiction
the v2 additions create with the current METHODOLOGY/SKILL text.

Evidence discipline: cite file:line or a concrete failure scenario for every finding; rank
every finding blocker/major/minor/nitpick; flag anything unverifiable; a clean factual verdict
needs the citations you consulted. End with: a per-finding disposition table (TASK A), ranked
new findings (TASK B), and a one-paragraph bottom line with worst severity.

Your final message is consumed as the raw review record and preserved verbatim — return the
full review.
```

## The reviewer's verbatim output

All artifacts, sources, and the precedent record have been read in full; mechanical checks (git state, line counts, phrase greps, v1→v2 diff) are done. Here is the full round-2 review.

---

# Cold red-team review — audit-hardening-2026-07, stage 3 ROUND 2 (verify round-1 dispositions + attack the revision)

Reviewer: cold subagent, no shared context with the author. Sources consulted: the six artifacts under review (decisions.md, 3-redteam-plan.md, 0-audit-findings.md, 1-spec.md, 1.5-criteria.md v2, 2-plan.md v2, plus 2-plan.v1-superseded.md via diff); `METHODOLOGY.md` (467 lines, verified `wc -l`); `SKILL.md` (102 lines, verified); `changes/concurrency-lens/{decisions.md, 1.5-criteria.md, 8-harness.md}`; git state of the skills repo (HEAD `8a7ac65` = "dragonfly: add the gate-before-present rule", working tree clean on both files — the pinned pre-change state in decisions.md:7-8 is accurate). Mechanical checks run: `wc -l` (467/102/569 confirmed), `grep -rn "redundant"` over the v2 operative docs (zero hits outside decisions.md's historical description of the round-1 finding), `grep "end-to-end|proving"` over 1.5/2-plan v2 (all apparent hits are the substring "proven" inside "provenance" — the AR-1 overclaim phrases are gone), and a full v1↔v2 plan diff.

---

## TASK A — Round-1 disposition check

**A note before the table (see also R2-7 below):** the round-1 record contains **23** findings, not 22 — lens counts 4 FA + 7 LO + 5 MO + 7 AR = 23; the ranked summary table (3-redteam-plan.md:224-248) has 8 major + **12** minor + 3 nitpick rows. decisions.md:11 says "8 major, 11 minor, 3 nitpick" (= 22) and 2-plan.md:4 says "All 22 round-1 findings addressed." The enumeration in my own charter lists 12 IDs under "11 minor." I therefore checked all **23**. Every one is addressed; the count in the gate log is wrong (nitpick, R2-7).

| # | R1 sev | Disposition | Evidence |
|---|---|---|---|
| **FA-1** | Major | **RESOLVED** | "redundant-but-harmless" is absent from 1.5 v2 and 2-plan v2 (grep: only decisions.md:14,16 as historical record of the finding itself). The precedent is now cited for what it actually established: "Confound tripwire (restored — the precedent's actual lesson [FA-1/LO-1])" (2-plan.md:60-62), which matches `concurrency-lens/decisions.md:76-81` (control caught → strict pass NOT met → confound investigated → discarded) and `concurrency-lens/1.5-criteria.md:13`. No disposition anywhere pre-authorizes a pass on control-catch. |
| **FA-2** | Minor | **RESOLVED** | Erratum appended to 0-audit-findings.md:131-139: detection = "the precedent's **strict pass condition firing**," honesty = diagnosis. Verified against `concurrency-lens/decisions.md:77-78` ("The fresh control caught it → strict C3 pass condition (treatment catch AND control miss) NOT met") — accurate. (Residual wording tension in the erratum's last sentence → R2-9b.) |
| **FA-3** | Minor | **RESOLVED** | C6 now expects "F9's sentence rewrite + in-place sentence extensions (F3 column list; SKILL clauses wired into existing bullets)" with a per-hunk verbatim-or-stronger survival rule (1.5:21; 2-plan.md:73-76) — the round-1 contradiction ("only F9… expected," v1 L46-47) is gone. (Possible enumeration gap for an F6 charter-sentence extension → R2-10b, nitpick.) |
| **FA-4** | Minor | **RESOLVED** | 1.5:19: "absolute numbers govern, all three must hold [FA-4]: METHODOLOGY ≤ 583, SKILL ≤ 127, combined ≤ 671 (baselines 467/102/569 at `8a7ac65`)." Arithmetic re-verified: 583 ≤ 467×1.25 (583.75); 127 ≤ 102×1.25 (127.5); 671 ≤ 569×1.18 (671.42). No stated percentages remain to contradict; 583+127=710 > 671 is now coherent because "all three must hold" makes the combined cap explicitly binding. Governing rule unambiguous. |
| **LO-1** | Major | **RESOLVED** | The tripwire is restored essentially verbatim to round-1's prescribed repair: "a control flagging V1 or V2 *while citing a rule absent from its (pre-change) docs*, or 2/2 controls catching a new-rule violation, = suspected harness confound → STOP, investigate, no disposition recorded until resolved" (2-plan.md:60-64; 1.5:18). The auto-benign absorption is gone; control-V2 catches are affirmatively recorded as codification evidence, "not absorbed silently" (2-plan.md:64-66). (Two disposition holes remain at the edges → R2-2, new minor.) |
| **LO-2** | Major | **RESOLVED** | One violation per artifact, exactly per round-1's repair including the proposed layout: V1→fixture `3-redteam-plan.md` (2-plan.md:41-42), V3→fixture `6-redteam-code.md` (:43-44), V2→`8-harness.md` (:45-49), V4 a different row of the same file (:50-53). V3's placement ambiguity is gone. Pass condition now requires "each citing the deciding rule" for V1/V3/V4 (2-plan.md:59; 1.5:18) — the citation requirement round 1 asked for. V2's "any rule-grounded reason" is a justified deviation given LO-3's codification concession. Row-wise soundness for V2+V4 assessed under TASK B(1) — sound. |
| **LO-3** | Major | **RESOLVED** | V2 redesigned "maximally survivable under current text so F3's mechanical rule is the sole differentiator" (2-plan.md:45-47) = round-1's partial repair verbatim; honest recording that "F3 may verify as *codification*… C3's demonstrated marginal value may rest on V1" (2-plan.md:47-49); control-V2 catch → codification evidence (:64-66); caveat carried to the final report (2-plan.md:96; 1.5 C7). |
| **LO-4** | Major | **RESOLVED** (as prescribed) | F4 row: hash-or-verbatim-copy recorded in decisions.md at route-to-build, "the freeze binds to the criteria version the stage-3 reviewer read," stage 8 verifies file == recorded version, divergence = post-freeze edit → affected PASSes invalid absent logged entry + targeted re-red-team (2-plan.md:18); dogfooded in 1.5:24-26 (sha256 at the gate). This is round-1's repair implemented literally. However, the v2 **sweep item 2 addition** creates a new internal contradiction with the "version the reviewer read" clause → R2-4 (new minor, distinct from the round-1 finding). |
| **LO-5** | Major | **RESOLVED** | F7 consequence: "a stage-3 review with no coverage-challenge section (an explicit 'none found' counts) is incomplete on lens 4 and treated as un-run for that lens [LO-5]" (2-plan.md:21) — round-1's repair verbatim, following the existing earned-clean pattern (METHODOLOGY:213-217, 237-240). F8 consequence: "gate 4 may not pass until the validation result is recorded in decisions.md [LO-5]" (2-plan.md:22). C1's schema updated to demand consequence per row, naming F7/F8 (1.5:16). |
| **LO-6** | Minor | **RESOLVED** | F2 row: "A defective check found this way is **discarded and rebuilt in place** (logged in decisions.md), not a loop restart; findings it raises about the change itself route via gate 8's severity table [LO-6]" (2-plan.md:16); sweep item 4 (:30). Matches the precedent's actual handling (`concurrency-lens/decisions.md:80-82`). |
| **LO-7** | Minor | **RESOLVED** | "exactly 2 treatment + 2 control; every run counts; no resampling [LO-7]" (2-plan.md:54; 1.5:18) + pre-committed outcome dispositions incl. a single bounded, logged, diagnose-then-fix retry with 4 fresh reviewers, second FAIL → stage-8 major → human (2-plan.md:67-70). The n>2 ambiguity is gone ("exactly"). (The retry itself carries two residuals → R2-3 minor, R2-9a nitpick.) |
| **MO-1** | Major | **RESOLVED** | F1 now binds "**Every cold-review record, wherever in the run it occurs** (stages 3/6, a targeted post-6 check, a harness-embedded reviewer arm) [MO-1]" (2-plan.md:15) — the exact "one-word-class fix" round 1 named. Dogfooded in C3's verification column ("verbatim outputs preserved with full provenance," 1.5:18). |
| **MO-2** | Minor | **RESOLVED** | Embed duty "(iv) the reviewer's agent type + model [MO-2]" (2-plan.md:15); C3 provenance includes "agent type/model" (1.5:18). |
| **MO-3** | Minor | **RESOLVED** | V4 = "gating criterion dispositioned 'will confirm live after ship'" probing the pre-existing deferral rule near the stage-8 insertion cluster, both arms (2-plan.md:50-53) — round-1's exact suggestion (deferral rule, METHODOLOGY:325-344). |
| **MO-4** | Minor | **RESOLVED** | F8 validates "**every path handed to a cold reviewer** (config `redteam_context`, spec touched-files, fixture paths) [MO-4]" (2-plan.md:22). (The merge introduced a timing incoherence → R2-1, new minor.) |
| **MO-5** | Nitpick | **RESOLVED** | Renamed `fixtures/review-record/` ("neutral name"), synthetic-README "added only after the runs [MO-5]" (2-plan.md:39-40) — both halves of the round-1 ask. (Residual: the parent dir `fixtures/` still leaks syntheticness → R2-8, nitpick.) |
| **AR-1** | Major | **RESOLVED** | 1.5:3-10 rewritten: V3+V4 are "**spot-check evidence, not proof**, of non-displacement [AR-1]; the residual risk is named in the final report. C4 bounds raw growth only — it cannot see attention dilution." Grep confirms "end-to-end"/"proving" are gone. The unprobed SKILL step-3 triple-insertion is named to the owner verbatim (2-plan.md:97-98). Second probe added (MO-3). |
| **AR-2** | Minor | **RESOLVED** | Control docs "exported from git `8a7ac65`" (2-plan.md:55-56; 1.5:18); baselines pinned "at `8a7ac65`" (1.5:19). HEAD verified = `8a7ac65`, tree clean — the pin is real and currently accurate. |
| **AR-3** | Minor | **RESOLVED** | "n=2 limitation carried into the verdict verbatim [AR-3]" (1.5:18; 2-plan.md:67-68, 96); the bounded retry addresses the false-FAIL propensity; pre-committed protocol per LO-7. Mirrors the precedent's honest-limitation handling (`concurrency-lens/decisions.md:90-92`). |
| **AR-4** | Minor | **RESOLVED** | Reporting duty: "This change spends attention budget against S1's ceiling; S1–S3 surfaced for owner decision [AR-4]" (2-plan.md:99-100); C7 carries it (1.5:22) — exactly the mitigation round 1 endorsed. (My independent cap-margin analysis → R2-6.) |
| **AR-5** | Minor | **RESOLVED** | F3 row: "for a human-judged-rubric criterion the evidence pointer = the named judge + where the verdict is recorded [AR-5]" (2-plan.md:17); added to the sweep as item 7 (:33); consistent with METHODOLOGY:352-355 ("the named judge's verdict"). |
| **AR-6** | Nitpick | **RESOLVED** | "The charter = the METHODOLOGY charter core verbatim **plus task-specific additions quoted as such** [AR-6]" (2-plan.md:15) — round-1's suggested wording adopted. (The inherited "charter core" definitional gap → R2-5, new minor.) |
| **AR-7** | Nitpick | **RESOLVED** | "Live copy is updated only after gate 7 passes… if stage 8 bounces hard, live is reverted to the `8a7ac65` copies [AR-7]" (2-plan.md:8-9); build step 4 "**Do NOT install to live yet**" (:89); step 6 installs post-gate-7 with revert provision (:91-92); C5 timed accordingly (1.5:20; 2-plan.md:72). |

**Task A verdict: 23/23 RESOLVED** — every round-1 repair was implemented, most verbatim, and I found no finding closed on say-so alone: each has landed text I could cite.

---

## TASK B — Fresh attack on the revision

### Focus area (1): the redesigned C3 protocol

**The V2+V4 row-wise argument is sound.** The masking mechanism in LO-2 was rule-driven: V1's provenance rule invalidates the *whole review*, giving a reviewer a benign reason to stop enumerating. No analogous whole-doc rule exists for a harness table: V2's consequence is row-scoped (`verified = no` for that row — METHODOLOGY:349-350 and the new F3 rule) and V4's is row-scoped (deferred gating row ≠ met — METHODOLOGY:327-334); the neutral question demands per-item enumeration ("List any… citing the rule that decides each," 2-plan.md:57-58); and the two rows' deciding rules are disjoint *provided the fixture is built so V4's row does not claim `verified = yes`* (else F3's evidence rule double-fires on V4 and "the deciding rule" becomes ambiguous — R2-10a). Flagging one row supplies no rule-grounded reason to skip the other. The argument holds.

**The restored confound tripwire is faithful to the precedent's function** (detection by rule, per the erratum), and STOP-before-disposition closes the round-1 absorption hole. Remaining edges are disposition-completeness, not confound-blindness — see R2-2.

**Can it still produce a false PASS / false FAIL?** No high-severity channel found. Residual channels, all bounded: (a) a hollow-ish PASS if a control legitimately flags V1 with a stretched-but-real current rule and nothing records it (R2-2) — the stated claim ("new rules fire through amended docs; old rules still fire") remains true, so this is an honesty-recording gap, not a false verdict, given AR-1's downgrade to spot-check; (b) the one-retry rule is mild pass-side selection (best-of-two batteries) but is pre-committed, logged, bounded at one, and the first FAIL stays in the record — acceptable *except* that the "fix" preceding the retry is an unreviewed post-6 modification (R2-3); (c) false FAIL from stochastic misses is exactly what the retry exists to absorb, with a human catching a second FAIL. The instrument is now valid for the (correctly narrowed) claim it certifies.

### Focus area (2): the F4 freeze-hash — mostly airtight, one self-inflicted contradiction

The hash mechanically anchors stage 8 to the gate-4 version and makes post-freeze edits detectable — the round-1 window (edit between review and gate log) is closed *as prescribed*. Two residuals: the internal contradiction R2-4 (below), and the fact that the hash is author-recorded with no reviewer-attested link to what the reviewer actually read — but full adversarial integrity of decisions.md is explicitly S3, flagged and out of scope by owner decision (0-audit-findings.md:125-127), so I do not count that as a plan defect; a one-line cheap strengthening is offered inside R2-4.

### Focus area (3): F7/F8 consequences — enforceable

F7: presence/absence of a coverage-challenge section is mechanically checkable; "treated as un-run for that lens" inherits the existing earned-clean re-run convention (METHODOLOGY:213-217) — enforceable as written. F8: "gate 4 may not pass until the validation result is recorded" is checkable against the gate log (and was dogfooded this run — decisions.md:5-6 "validated: all paths exist, readable"). Enforceable, but the trigger timing is incoherent for fixture paths — R2-1.

### Focus area (4): C4 cap plausibility

Headroom: METHODOLOGY +116, SKILL +25, combined +102. METHODOLOGY's ~9 insertions (one bullet/block/clause each, F1's the largest) plausibly cost ~40-55 lines — comfortable. SKILL is the pinch: ~13 payload sentences across steps 1/3/4/6/7/8, Inputs, and a 3-sentence self-check rewrite must fit in +25 wrapped lines, and F1's "one sentence each" at steps 3/6 must carry four embed duties + charter-verbatim rule + closed set + A/B prohibition — see R2-6. Verdict: plausible, not comfortable; combined cap is not the binding risk, SKILL's is.

### Focus area (5): new contradictions vs. current METHODOLOGY/SKILL

The seven sweep items cover the real collision points; AR-5's reconciliation is consistent with METHODOLOGY:352-355; F4-vs-bounce, F2-vs-iteration-cap, F5-vs-human-authority all check out against METHODOLOGY:270-291 and SKILL:85-88. Remaining frictions are wording-level: F5's unscoped "gates route on the reviewer's stated severity" at gate 8 (R2-11) and two non-identical reviewer-scope statements from F1 vs F6 (R2-12). The one *internal* v2 contradiction is R2-4.

### Ranked new findings

**R2-1 (MINOR — logical/temporal).** F8's trigger is "**At run start**, mechanically check every path handed to a cold reviewer (… fixture paths)" (2-plan.md:22), but fixture paths do not exist until build step 3 (2-plan.md:88) — at run start they *cannot* be validated; this run's own start-of-run validation (decisions.md:5-6) predates the fixture and could not have covered it. The v1 rule (redteam_context only, at run start) was coherent; bolting MO-4's wider list onto the unchanged timing broke it. Also, the consequence anchors only at gate 4, which fires before the fixture exists — nothing validates the paths handed to the stage-8 C3 arms. Repair (one clause): validate at run start *and at each cold-reviewer spawn for any path not yet validated*.

**R2-2 (MINOR — logical).** C3's pre-committed dispositions are not exhaustive on control-V1 catches. (a) A *single* control legitimately flagging V1 by stretching a real current rule — e.g., arguing the record cannot demonstrate the reviewer had the source access METHODOLOGY:192-196 makes load-bearing, so its verdicts are UNVERIFIABLE — trips no wire (real rule cited, only 1/2) and triggers no recording duty; it is silently compatible with PASS while gutting F1's demonstrated marginal value — which the plan itself concedes is C3's main value (2-plan.md:48-49). The codification-honesty row exists for V2 (2-plan.md:64-66) but was not extended to V1. (b) The tripwire clause "2/2 controls catching **a** new-rule violation" (2-plan.md:62-63) is ambiguous between *the same* violation and *any* new-rule violation each (one catches V1, the other V2) — ambiguity in a STOP condition. (c) After a tripwire STOP resolves to "not a confound, just diligent controls," the resumption disposition is undefined. Repair: one sentence extending the codification-style recording to control-V1 catches + disambiguate "2/2 … a new-rule violation" + name the post-investigation re-entry.

**R2-3 (MINOR — logical, F2-shaped).** The one-retry rule re-opens the exact window this change closes. "diagnose (fixture wording vs rule wording), fix, re-run" (2-plan.md:68-70) modifies either the fixture or the amended docs *after* the stage-6 verbatim re-check that the plan says "clos[es] the F2 window for this run" (2-plan.md:78-80), and the retried result counts with no targeted cold check stated. A botched or leading fixture "fix" (e.g., making V1 blatant) yields a PASS on a weakened, unreviewed instrument. The new F2 rule itself — in force in the amended docs stage 8 runs under — would mandate the targeted check, but a pre-committed protocol should not rely on the executor noticing that; say it: *a pre-retry fixture fix gets the F2 targeted cold check before the retry counts; a pre-retry rule-wording fix re-runs C1/C2/C4/C6 per the fix-in-place rule.*

**R2-4 (MINOR — internal contradiction).** The freeze binding is stated two incompatible ways. F4's row and 1.5:24-26 bind the freeze "to the criteria version **the stage-3 reviewer read**"; sweep item 2 says "gate-4 in-place criterion fixes **precede it** and are captured by the recorded hash [LO-4]" (2-plan.md:28) — so whenever a gate-4 minor fix touches 1.5, the recorded hash is the *post-fix* version, and the "version the reviewer read" clause is false. Worse, gate-4 in-place fix diffs are recorded nowhere: F2's fix-diff duty covers gates 7/8 only (2-plan.md:16), so a criteria edit labeled "gate-4 minor fix" can exceed its finding and be frozen as-if-reviewed. Repair (one clause): the hash binds to the route-to-build version, which must equal the reviewer-read version *except for gate-4 in-place fixes each traceable to a logged finding, with the criteria diff recorded in decisions.md*. Cheap strengthening while there: have the cold reviewer state the sha256 of each context file it read in its verbatim output — reviewer-attested, author-independent, one charter line (the rest of the integrity question is S3, out of scope by owner decision).

**R2-5 (MINOR — checkability).** "The METHODOLOGY charter **core** verbatim" (2-plan.md:15) — "charter core" is defined nowhere in either doc (charter section = METHODOLOGY:190-264, including conditional lenses that fire only sometimes). The run's own constraint is rules that are "explicit, mechanical, and checkable" (0-audit-findings.md:8); "core" is a judgment word, so F1's verbatim-charter check — part of the headline fix — cannot be mechanically verified. Repair: define it in the F1 text (e.g., the four lenses + the unconditional discipline bullets; conditional lenses included when their trigger fires).

**R2-6 (MINOR — unstated assumption).** SKILL's cap margin is the plan's tightest unexamined number: ≤127 leaves **+25 wrapped lines** for ~13 payload sentences (steps 1, 3×3, 4×2, 6×2, 7×2, 8×2, Inputs, + F9's 3-sentence rewrite), and SKILL's existing style wraps dense sentences over 3+ lines (cf. step 3, SKILL.md:57-62). F1's "one sentence each" at steps 3/6 carrying four embed duties + charter rule + closed set + A/B prohibition is only feasible pointer-style ("per METHODOLOGY 'Provenance is part of the review record'"). C4 is gating, so a breach at stage 8 = FAIL → replan. Repair: pre-assign per-fix SKILL line budgets in the build step, and state the pointer-style preference for SKILL clauses explicitly.

**R2-7 (NITPICK — factual, gate log).** The finding count is wrong in the load-bearing record: round 1 produced **23** findings (4 FA + 7 LO + 5 MO + 7 AR; 8 major + **12** minor + 3 nitpick — count the table at 3-redteam-plan.md:224-248), but decisions.md:11 says "11 minor" (total 22) and 2-plan.md:4 says "All 22 round-1 findings addressed." All 23 *are* addressed (Task A), so impact is cosmetic — but a miscount in the append-only gate log of a change about record integrity should be corrected by an erratum entry.

**R2-8 (NITPICK — MO-5 residual).** The neutral rename kept the parent directory `fixtures/` (2-plan.md:39, 88), which announces syntheticness to both arms as loudly as "seeded" did. Symmetric; with the tripwire restored the main cost flips from false-benign absorption to spurious STOP/investigate noise (planted-defect hunting inflating 2/2-control catches). Cheap: hand reviewers a copied neutrally-named path.

**R2-9 (NITPICK — wording tensions).** (a) 1.5:18 "every run counts, **no resampling**" sits next to the plan's pre-committed retry (2-plan.md:68-70); 1.5 delegates to "the plan-v2 protocol" so no real conflict, but say "no *silent* resampling; the single diagnosed-fix re-run is the only exception." (b) The erratum's final sentence — "the strict differential pass condition IS the confound tripwire and **must be preserved in any replay-A/B design**" (0-audit-findings.md:137-139) — overstates: the v2 C3, per round-1's own LO-1 repair, deliberately does *not* use a differential pass condition (it preserves the tripwire *function*); a literal reader finds v2 non-compliant with its own audit doc. Reword to "its tripwire function must be preserved."

**R2-10 (NITPICK — fixture build care, unstated).** (a) V4's row must not read `verified = yes` — else the F3 evidence rule double-fires on it and "the deciding rule" in the pass condition (2-plan.md:59) becomes ambiguous, jeopardizing V4's citation requirement; "dispositioned 'will confirm live'" implies this but the build spec should state it. (b) Whether realism (non-violation) gating rows carry evidence pointers is unspecified: pointer-less rows make treatment flag *every* row under the new F3 rule (harmless to the pass condition, but it dilutes V2's "sole differentiator" isolation), while pointer-carrying rows are anachronistic in a pre-change-format doc that controls read. Decide and record. (c) Relatedly, treatment reviewers' deciding rule for V2 should be captured: if 2/2 flag V2 citing only *old* challenge-text, that is codification evidence from the treatment side too — the record has the data (verbatim outputs), only the interpretation is un-pre-committed.

**R2-11 (NITPICK — scoping vs current docs).** F5's substance "Gates route on the **reviewer's** stated severity" (2-plan.md:19) is unscoped, and the METHODOLOGY landing spot (after the routing table, which covers gates 4/7/**8**) textually reaches gate 8, where findings originate from the author's own harness and no reviewer severity exists (except F2 targeted checks). Build wording should scope to findings originating from a cold review.

**R2-12 (NITPICK — near-duplicate scope statements).** F1's closed set is "named stage artifacts + config `redteam_context` + spec touched-files + carried-forward findings" (2-plan.md:15); F6's scope clause is "artifacts + config redteam_context + touched files" (2-plan.md:20) — no carried findings. Two non-identical definitions of reviewer scope landing in the same docs is a C2-sweep-shaped hazard the sweep doesn't list; make F6's clause reference F1's closed set.

---

## Bottom line

**Worst severity: MINOR — gate 4 may route fix-in-place and proceed to build.** Every one of the round-1 findings (in fact 23, not the logged 22 — R2-7) is genuinely resolved in the v2 text, most by implementing round 1's prescribed repair verbatim, and I verified each against the landed wording rather than the author's disposition tags: the precedent is now cited for its actual lesson with the tripwire restored (FA-1/LO-1), the fixture isolates one violation per artifact with a sound row-wise argument for V2+V4 co-location, the freeze has a mechanical hash anchor, F7/F8 carry enforceable consequences, the C4 arithmetic is coherent with an unambiguous governing rule, and the criteria no longer overclaim what C3 proves. The redesigned C3 can no longer produce the round-1 false-PASS/false-FAIL modes; what remains are edge-of-protocol gaps, all localized and one-sentence-fixable: F8's run-start timing is impossible for fixture paths (R2-1), the control-V1 outcome and tripwire wording leave small undisposed cells (R2-2), the one-retry rule quietly re-opens the F2 window it sits inside (R2-3), the freeze's "version the reviewer read" clause contradicts sweep item 2's gate-4-fix allowance with no diff-recording duty (R2-4), "charter core" is unchecked-able as written (R2-5), and the SKILL line cap is tight enough to warrant per-fix budgets before build (R2-6). No blocker, no major, no unaddressed round-1 finding.
