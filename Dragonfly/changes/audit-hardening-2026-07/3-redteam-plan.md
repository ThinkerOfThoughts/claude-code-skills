# 3 — Red-team of {1-spec, 1.5-criteria, 2-plan} — ROUND 1 — verbatim record

## Provenance
- **Date:** 2026-07-03. **Reviewer:** cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author.
- **Context given (closed set):** change docs {0-audit-findings, 1-spec, 1.5-criteria,
  2-plan, decisions}.md + Dragonfly source {METHODOLOGY, SKILL}.md (pre-change) +
  Guarded_change source {METHODOLOGY, SKILL}.md (cross-ref target, `9cec23d`) + hunt
  evidence `~/Desktop/companion-emergence/hunts/monologue-bleed-memory-gap/{decisions,
  hypotheses, CONTEXT-BLOAT-HUNT}.md`. Reviewer-reported sha256s at the top of the verbatim
  output below (12 files; reviewer additionally consulted git metadata of the four skill
  files to verify the `9cec23d` baseline claim — declared, in-scope corroboration).
- **Transport note:** output arrived through the harness notification layer (HTML-escaped
  angle brackets); `&lt;criterion&gt;`/`&amp;` de-escaped to literal characters. No other
  normalization.
- **Charter/prompt given (verbatim):**

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is the STAGE-3 red-team of a guarded-change run: the thing under review is {1-spec.md, 1.5-criteria.md, 2-plan.md} for a change that hardens the DRAGONFLY skill (a bug-diagnosis loop) with 14 additive rule fixes derived from an audit (0-audit-findings.md) and the skill's one real-world hunt record.

Attack the spec+criteria+plan on four separate lenses:
1. FACTUAL — do the plan's claims match the sources? Does each mapping-table location actually exist in the current dragonfly text? Do the audit findings say what the plan says they say? Cite file:line for everything you check; a clean factual verdict is only valid if you show the specific source evidence you consulted (file:line) — a clean factual verdict with zero citations is treated as an un-run review.
2. LOGICAL — flaws in the plan's reasoning: contradictions between proposed rules and existing dragonfly/guarded-change rules; sweep items that don't actually reconcile; criteria that can't verify what they claim to verify.
3. MISSED OPPORTUNITY — better approaches left on the table (within the additive-only constraint).
4. UNSTATED ASSUMPTIONS & RISKS — what is taken for granted that could be false?

Discipline: cite a file:line or a concrete failure scenario for every finding; rank every finding blocker/major/minor/nitpick; flag anything you could not verify rather than silently accepting it; 'no issue found' per lens is allowed and expected when true; audit the criterion labels — every advisory label needs a legitimate reason and every gating criterion must be verifiable by the stated stage-8 method; a sample of your cited lines will be spot-verified.

COVERAGE CHALLENGE (mandatory section): name the behaviors this change could plausibly alter that NO criterion observes — each named gap needs a concrete scenario and ranks by impact; an explicit "none found" counts.

POSITION LENS (trigger fires — these are prompt documents): the additions are insertions into a position-sensitive assembly. Assess displacement/dilution risk for the neighbors of each insertion cluster — note especially that the stage-7 detail receives three additions (D-5, D-13, D-14) and the stage-6 detail receives three (D-3, D-7, D-12); "all info still present" is not a clean verdict for a position-dependent element.

Task additions (quoted as such): 'Challenge the mapping table row-by-row: does each proposed METHODOLOGY/SKILL location exist in the current dragonfly text, does each row's substance carry trigger + requirement + consequence, and would the addition contradict or displace any neighboring rule? Challenge the criteria: are the C4 caps (515/148/655 vs baselines 441/129/570) realistic for the mapped substance? Is the no-battery decision honestly scoped (a C7 advisory residual with rationale, not a disguised deferred gating criterion)? Is C3's cross-reference list complete against every by-reference import the amended text will rely on? Check D-11's claim that the guarded-change stage-3 coverage-challenge bullet should NOT bind dragonfly passes — is the plan's reasoning sound? Verify the plan's contradiction-sweep item 4 (D-8 escape vs the stage-1 ordering and the loop diagram) actually resolves, since the loop diagram at METHODOLOGY.md:91 says "BEFORE hypothesizing" and will NOT be edited.'

Context (closed set — read ONLY these; consult nothing else on disk):
- The change docs: /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/{0-audit-findings.md, 1-spec.md, 1.5-criteria.md, 2-plan.md, decisions.md}
- Dragonfly source (the thing being amended, pre-change): /home/zero/Desktop/claude-code-skills/Dragonfly/{METHODOLOGY.md, SKILL.md}
- Guarded-change source (the cross-reference target, freshly hardened at 9cec23d): /home/zero/Desktop/claude-code-skills/Guarded_change/{METHODOLOGY.md, SKILL.md}
- Real-world evidence the audit cites: /home/zero/Desktop/companion-emergence/hunts/monologue-bleed-memory-gap/{decisions.md, hypotheses.md, CONTEXT-BLOAT-HUNT.md}

End with: one-line verdict — worst severity + route recommendation (blocker → return to spec; major → return to plan; minor → fix in place, proceed to build; nitpick/clean → proceed to build).
```

## Reviewer output (verbatim)

# STAGE-3 RED-TEAM — dragonfly `audit-hardening-2026-07` {1-spec, 1.5-criteria, 2-plan}

Reviewer: cold pass, no shared context with the author. Agent: general-purpose-equivalent (Claude Code subagent), model Fable 5 (`claude-fable-5`).

## Context-file hashes (sha256, computed by me)

```
f753d7fcf809a0303ee91dbeb85cbba327f5c01e0d753cde5aaecc98dbde5cbc  Dragonfly/changes/audit-hardening-2026-07/0-audit-findings.md
a048500048675f38e7c9448e489dc99de5e0cffe0f234fc7cc6ed945d10b6cc7  Dragonfly/changes/audit-hardening-2026-07/1-spec.md
0f60d8c9d5b37cdd0750172ce56273a16f5fc94f37224e8a0657c70fe496e447  Dragonfly/changes/audit-hardening-2026-07/1.5-criteria.md
b9e00c5786bdefb1787d9d8aaad0fc20cc683ab291fbbbe5cfcc3cc637d3e268  Dragonfly/changes/audit-hardening-2026-07/2-plan.md
049add74774395a028a3aee145824be9cf2e0be312937f2a8fdb3f94f3f8c05c  Dragonfly/changes/audit-hardening-2026-07/decisions.md
03533146f68896ba6646533ff404d1f5352024a6129e061d2ac9fbf91c203670  Dragonfly/METHODOLOGY.md
23b585d7e1701b99a9fdd8637e06df29fd8cf43f9e08a7315a403b51317c4d47  Dragonfly/SKILL.md
35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3  Guarded_change/METHODOLOGY.md
4e2a2e5135ce0d3397fa208a18e4f1715e22e3738b99bca16cea153e7302839b  Guarded_change/SKILL.md
a4c2addadfb78c3fe419222a52caf51218330e7d7b00ca7ec2e342dc8023606a  hunts/monologue-bleed-memory-gap/decisions.md
fcfcd687929cd1f846309f03fd093c030c76c4c30fe9cf78ba275b22ec0586bc  hunts/monologue-bleed-memory-gap/hypotheses.md
46ae8d4f0c9afd7793c041a944e144dc06d71bf183136ae1be78e499d46cb98f  hunts/monologue-bleed-memory-gap/CONTEXT-BLOAT-HUNT.md
```

Closed set respected: only the twelve files above plus git metadata of the same four skill files (to verify the plan's `9cec23d` baseline claims).

---

## LENS 1 — FACTUAL

### Mechanical anchors (verified myself)

- `9cec23d` exists, is the skills repo `main` HEAD ("harden guarded-change: land F1–F9 additive fixes, verified by 3-round replay A/B"), and the four skill files in the worktree are **identical** to `9cec23d` (empty `git diff 9cec23d --stat` on all four).
- Line baselines: Dragonfly METHODOLOGY **441** / SKILL **129** (sum 570) at `9cec23d` — matches 1-spec.md:39-40 and 1.5-criteria.md:19. Guarded-change **534/124** — matches run decisions.md:9.
- Note (outside the four files, doesn't affect this run): `Guarded_change/guarded-change.companion.md` is locally modified per `git status`.

### Mapping-table locations, row by row (task addition #1) — **every named location exists**

| Row | Verified anchor |
|---|---|
| D-1 | METHODOLOGY.md:311 `## The red-team charter (stages 1, 4, 7)`; SKILL.md:102 `## Cold red-team (stages 1, 4, 7)` |
| D-2 | stage-7 detail ends METHODOLOGY.md:188, stage 8 begins :190 (insertion slot exists); SKILL.md:71-72 step 8 |
| D-3 | stage-6 detail METHODOLOGY.md:172-176; SKILL.md:63-65 |
| D-4 | rep-gate section METHODOLOGY.md:217-233; triage intro enumeration :272; SKILL.md:82-88 and heading :90 |
| D-5 | toggle item METHODOLOGY.md:183-184; stage-9 detail :194-213; SKILL.md:66-70, 73-80 |
| D-6 | config Rules METHODOLOGY.md:378-382 (fields exist: `redteam_context` :360, `reproduction.logs` :368-369, `ledgers.dir` :371-372); SKILL.md:14-19 Inputs |
| D-7 | stage-6 detail (as D-3); SKILL step 6 |
| D-8 | stage-1 detail METHODOLOGY.md:134-141; SKILL.md:41-45 |
| D-9 | lite paragraph METHODOLOGY.md:284-290; SKILL.md:96-99 triage item 3 |
| D-10 | SKILL.md:123-129 self-check; confirmed **no** self-check section exists in METHODOLOGY (grep) — the "(none)" cell is correct |
| D-11 | charter section :311ff; self-check per D-10 |
| D-12 | aiming list METHODOLOGY.md:323-327; stage-6 detail; SKILL.md:108-110 aiming prose |
| D-13 | stage-7 detail; stage-8 detail :190-192; `diagnosis.md` artifact line :395; SKILL steps 7/8 + aiming |
| D-14 | stage-7 detail; stage-9 detail; artifact line :395; SKILL steps 7/9 |

Substance: all 14 rows carry an explicit trigger → requirement → "→ consequence". Weakest consequence: D-12's ("a hunt may not thrash… without the gate seeing it") is an outcome statement, not an enforcement clause — see L-8.

### Audit claims vs. the hunt record — verified

- D-1 "author-summarized reviews (e.g. 'O18: 6/6 citations verified')" — hunt decisions.md:32-33, exactly that summary form. Dragonfly source contains no provenance/sha256 duty (grep: only "verbatim" at METHODOLOGY.md:288, re the lite charter). Gap real.
- D-2 improvised ending — hunt decisions.md:72-73: "S1 outcome = CHARACTERIZATION + mitigation directions, not a code root-cause 'found'". "characteriz*" absent from both dragonfly files (grep). Gap real.
- D-3 "cycle" undefined — grep: "cycle" appears only at METHODOLOGY.md:103, :173, SKILL.md:63, never defined. Correct.
- D-4 ad-hoc detector gate — hunt decisions.md:93-94: "MANDATORY detector-representativeness gate (must flag the real ~/Downloads/Phoebe incident first)", dated 2026-07-02 as the audit says. "detector/readout" absent from dragonfly (grep). Correct.
- D-5 — "predictably" at METHODOLOGY.md:183, 9b windowless at :209-210; bleed intermittency at hypotheses.md:163-164. Correct.
- D-6 — config adaptation logged at hunt decisions.md:5-8 (macOS/Hana → Linux). Correct.
- D-7 — one hunt, two symptoms: hunt decisions.md:9-10; "thread" absent from dragonfly (grep) → counting is global. Correct.
- D-8 — "BEFORE hypothesizing" at METHODOLOGY.md:91 (diagram) and :134-135 (detail), SKILL.md:41; the real S1 formed H-S1-DISTANCE etc. long before the behavioural repro was even designed (hunt decisions.md:87-96). Correct.
- D-9 — lite definition METHODOLOGY.md:286-288 with no record duty; the hunt's lite pass is a gate-log one-liner (hunt decisions.md:24-27). Correct.
- D-10 — SKILL.md:126-129 contains "The behavioral test that matters most… no-Dragonfly baseline"; no position-assembly or full-loop language (contrast GC SKILL.md:117-124). "Never run": consistent with the total absence of any run record in the closed set, but strictly **unverifiable** — flagged, plausible.
- D-11 — GC provenance bullet exists post-hardening at GC METHODOLOGY.md:237-250; the five elements in the D-1 row match it item-for-item ((i)-(v)); "missing any = un-run" matches :248-249. Correct.
- D-12 — shared false assumption: hypotheses.md:62-66 ("Second S1 hypothesis killed by a false architectural assumption (cf. H-S1-DISTANCE)"), hunt decisions.md:64-66. Correct.
- D-13 — "never defines when the root is reached": correct (METHODOLOGY.md:64-67, :178-188 contain no depth notion). The precedent "Opus was prepared to accept the bloat-from-file-R/W account" is **user testimony, not in any ledger** — honestly labeled "user-observed" in audit/spec; consistent with CONTEXT-BLOAT-HUNT.md:36-38 (the "pin down the SOURCE(S)" reframe implies the shallow account was pushed past). Flagged unverifiable, accepted as labeled.
- D-14 — S1-O15 verified verbatim: hunt decisions.md:77-79 ("degradation happened there too but needed larger files / longer time → dose-dependent"). "Overlooked as 'not the primary cause'" = user testimony, flagged; "unified account emerged on the user's push" is consistent with decisions.md:75-86.

### Factual findings

- **F-1 (minor).** 1.5-criteria.md:17 enumerates C2 sweep items that don't exist in the plan as named: "D-2 vs the stage-8 verdict set" and "D-3's cycle unit vs the stage-6 cap text" — the plan's items 1 and 2 (2-plan.md:29-34) are "D-2 vs the gate-before-present tiers (+stage 9)" and "D-3 vs D-7". C2 is gating and names "the plan's contradiction-sweep items" as its oracle; the two lists must match or stage 8 verifies an ambiguous set. (Also "stage-8 verdict set" doesn't exist in dragonfly pre-change — D-2 *creates* the second verdict.)
- **F-2 (minor).** Sweep item 6 (2-plan.md:46-48) claims "one discipline, no second bar," but D-4 adds "stay silent on a known-clean one," which the existing instrument bar (METHODOLOGY.md:227-233) does **not** contain — that bar is fire-on-known-occurrence only. Strictly stronger, so no contradiction, but the sweep mischaracterizes the delta; the builder should know the false-positive half is new and intended, and whether it also now binds plain instruments (boundary instrument-vs-detector is undefined).
- **Unverifiable, flagged (not accepted silently):** AR-7 (2-plan.md:5-6), AR-1 and "13 arms' cost" (1.5-criteria.md:8-11), F4/F5/F8 designators — all reference the sibling GC run's change docs, outside the closed set. Partially corroborated by `9cec23d`'s commit message ("land F1-F9 … verified by 3-round replay A/B") and by GC METHODOLOGY text embodying them (provenance :237-250, path validation :472-479, criteria freeze :168-176, reviewer-severity routing :315-320).

---

## LENS 2 — LOGICAL

- **L-1 (MAJOR) — D-11's coverage-challenge exemption is unscoped and, as worded, contradicts the charter it imports (task addition #5).** The mapping row (2-plan.md:22) has the charter section state: "the stage-3 coverage-challenge bullet does NOT apply" to "dragonfly cold passes." But dragonfly's charter section *defines* its cold passes to include the stage-1/4 triage passes — "the guarded-change or guarded-change-lite pass each artifact is routed through *is* its cold review" (METHODOLOGY.md:316-319). A token-burning diagnostic artifact routes to **full guarded-change** (METHODOLOGY.md:277-279; the real hunt did exactly this, hunt decisions.md:104-105), and a full-GC run contains a stage-3 review where GC's charter makes the coverage challenge mandatory — "no such section ⇒ lens 4 un-run" (GC METHODOLOGY.md:251-255; charter composition GC METHODOLOGY.md:243-246 scopes the bullet "for stage-3 reviews"). So the sentence as planned exempts a class of passes that the imported rule explicitly binds. The reasoning is **sound for dragonfly's direct stage-7 passes and lite passes** (neither is a stage-3 review, so the bullet never bound them; D-12 is a genuine analog) — it only needs scoping. Compounding it: no gate can catch this later — C2's contradiction scope is "no new rule contradicts an existing **dragonfly** rule" (1.5-criteria.md:17), not an imported GC rule; C3 only checks references *resolve*; the sweep (2-plan.md:29-54) has no D-11 item. Concrete failure: the next hunt's token-burning harness enters full GC; the executor reads dragonfly's charter sentence, omits the coverage challenge from the harness's stage-3 review, and an unmeasured blast-radius gap in a token-burning artifact — the exact D-12-class blind spot this change targets — goes unnamed. Fix: scope the sentence ("does not apply to dragonfly's direct stage-7 and lite passes; a full guarded-change triage run keeps all of guarded-change's own stage duties, including its stage-3 coverage challenge"), add a sweep item 9, and widen C2's contradiction scope to "existing dragonfly rule **or imported guarded-change rule**."
- **L-2 (minor) — D-2's stage-9 reconciliation is asserted, not operationalized.** Sweep item 1 (2-plan.md:31-32) says a characterized handoff verifies mitigations "on symptom evidence only," but the mapping row gives D-2 no stage-9 location; stage 9's headline stays unconditional — "verify the ROOT CAUSE is resolved (not merely the symptom suppressed)" (METHODOLOGY.md:194, SKILL.md:73-74), and 9a instructs "using the stage-7 causal chain + toggle" (METHODOLOGY.md:196), which do not exist for a characterized ending. An Opus executor at stage 9 reads a bar it cannot meet, with the exception housed two sections earlier. Cheap fix: one clause in the stage-9 detail / SKILL step 9 — lines D-5 and D-14 already touch.
- **L-3 (minor) — new stop-for-human points missing from the stop-for-human inventories.** D-2 introduces mandatory human sign-off ((d), 2-plan.md:13) and D-6 introduces "dead paths surface to the human" (2-plan.md:17), but the mapping table touches neither METHODOLOGY "Human-in-the-loop" (:427-435) nor SKILL "Stop-for-human rules" (:113-121) — and "config is missing" (SKILL.md:120) is not the same condition as "config paths invalid." Because **C1's oracle is the mapping table** (1.5-criteria.md:16), a location omitted from the table is invisible to stage 8 — the table's completeness is only checkable here, at stage 3.
- **L-4 (minor) — the no-battery decision: honest disclosure, wrong legal form (task addition #3).** The residual is genuinely disclosed with a real rationale (1.5-criteria.md:3-12) and is *not* a disguised deferred gating criterion in intent. But under the freshly-hardened GC that this run explicitly dogfoods (run decisions.md:4-5), a position-sensitive change **must** carry at least one criterion asserting the position-dependent behavior survives, verified by execution (GC METHODOLOGY.md:141-153, :349-354), and the only legal way such a criterion ships unexecuted is route-(b) **named risk-acceptance recorded in decisions.md** ("conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>", GC METHODOLOGY.md:377-385). This run instead writes **no** position-behavior criterion at all and parks the fact in an advisory reporting duty — so there is nothing for the label-audit to bite on. Two-part fix, in place: (i) make **C7 gating** — its stated verification (inspection of the final report for required content) is cheap, unambiguous, and *is* the governed path for a report-content criterion; the current advisory label means the residuals/relabels can silently vanish from the report without blocking "done", and its stated reason "(reporting duty)" does not explain why non-blocking is safe; (ii) at gate 4, record the owner-attributed named risk-acceptance of the unexecuted position-behavior check in this run's decisions.md.
- **L-5 (nitpick).** D-3's cycle unit ("run and recorded", a completed 4→5 lap) makes design-churn that never completes a lap invisible to the cycle count; residual thrash coverage falls to the re-examination prong (METHODOLOGY.md:173) and the 2-bounce gate cap (:339-341). Acceptably covered; worth one clause if free.
- **L-6 (nitpick).** "ALL of guarded-change's unconditional discipline bullets" (2-plan.md:22) — "unconditional" is an unscoped classifier. Is the label-audit bullet (GC METHODOLOGY.md:256-274) unconditional when a dragonfly pass has no criteria labels? The built sentence should define it (e.g., "bullets carrying no stage or trigger scope") or enumerate.
- **L-7 (nitpick).** C1/C2/C3 are gating and verified by inspection, while GC METHODOLOGY.md:403-404 says "(Inspection-only 'verification' of a gating criterion counts as `verified = no`.)" For doc-content criteria, inspecting the text *is* exercising the governed path — but the dogfooding run should say so once in decisions.md rather than leave the literal conflict standing.
- **L-8 (nitpick).** D-12's consequence isn't enforcement-shaped; attach it to D-3's clause ("a stage-6 pass missing the class/shared-assumption record is a gate violation, like an uncounted pass"). Also D-3/D-7: a test that discriminates across both `S#` threads — which thread's cycle counter increments? One phrase settles it.
- **Sweep item 4 verdict (task addition #6):** it **resolves, with a named residual**. The detail-level exception explicitly saying "exception to the ordering above, recorded" is a legitimate general-rule-plus-named-exception structure, and the SKILL side puts the exception clause adjacent to its ordering sentence (SKILL.md:41). The residual: the unedited diagram line (METHODOLOGY.md:91, "BEFORE hypothesizing") becomes the document's only absolute statement of a now-excepted rule, and it is the first thing the loop teaches — see M-2.

---

## LENS 3 — MISSED OPPORTUNITY (within additive-only)

- **M-1 (minor) — a free retrodiction check was left on the table.** The one real hunt is a fully recorded fixture. A token-free, stage-8-executable check: apply the new rules to the recorded ledgers and confirm each fires where the ad-hoc handling happened — D-3's cycle count computed from hunt decisions.md; D-14's sweep applied to S1's rows flags S1-O15 (hunt decisions.md:77-79) as a residual; D-2's checklist matched against the recorded S1 ending (hunt decisions.md:68-74); D-8's escape matched against the recorded inversion. This is the nearest thing to a behavioral test this change can have without tokens, it directly shrinks the no-battery residual (L-4), and it is exactly the "checkable from the logs" property the spec demands (1-spec.md:29-30).
- **M-2 (minor).** Additive-only does not forbid touching the loop diagram; a one-parenthetical breadcrumb at METHODOLOGY.md:91-93 ("(escape for unreproducible-blind bugs: see stage-1 detail)") removes the only absolute statement of the excepted rule. The plan chose diagram-freeze without stating why.
- **M-3 (nitpick).** The `diagnosis.md` artifact line (METHODOLOGY.md:395) is extended for D-13/D-14 but not D-2 — a characterized handoff's artifact contents stay undefined ("root cause, causal chain…" presumes found).
- **M-4 (nitpick).** D-10 mirrors GC's self-check by restatement, not by reference — recreating the drift channel D-11 exists to detect (partially mitigated by the D-11 cross-ref criterion).

---

## LENS 4 — UNSTATED ASSUMPTIONS & RISKS

- **U-1 (verified clean).** Base assumption `9cec23d` == worktree == live: worktree equality verified by me (empty diff on all four files); live==source recorded at run decisions.md:14.
- **U-2 (minor) — C4 caps (task addition #2): realistic overall, SKILL is the pinch point.** METHODOLOGY: mapped substance estimates to ~55-70 added lines vs +74 headroom — adequate. SKILL: +19 lines must absorb the D-10 rewrite (the current 7-line section plausibly grows to 12-15 with four standing criteria + the relabel) **plus** 13 inline clause insertions whose re-wrapping adds lines. Feasible pointer-style, but the risk is cap pressure quietly compressing mapped substance; C1's substance check is the counterweight — stage 8 should read C1 strictly *against* C4, never trading substance for the cap. Note the combined cap (655) binds before the per-file sum (663) — intentional and fine.
- **U-3 (flagged).** Sibling-run designators (AR-1, AR-7, "13 arms", F-numbers) unverifiable in the closed set — see Factual lens; corroborated only indirectly.
- **U-4 (nitpick).** Nothing states the mapping table beats the audit text on conflict (the table already enriches audit D-2 with the stage-9 sentence). One line — "the table is the build oracle" — removes ambiguity.
- **U-5 (nitpick).** D-1's "the record lives in the hunt folder" vs full-GC triage runs recording under `changes/<slug>/` — satisfiable by nesting (the real hunt nested `changes/s1-repro-harness/` inside the hunt folder, hunt decisions.md:104-105), but the sentence should tolerate a pointer rather than a copy.
- **U-6 (accepted).** The whole change assumes Opus reads a 515-line METHODOLOGY in full per SKILL.md:8 — acknowledged via D-S1/C4; the caps are the control.

---

## COVERAGE CHALLENGE (mandatory)

Behaviors this change could plausibly alter that **no criterion observes**:

1. **Execution fidelity of pre-existing duties under dilution** (high impact, consciously accepted). Scenario: next hunt, stage 7 now carries bar + depth check + coverage sweep + probabilistic window; Opus completes the new blocks and skips the pre-existing citation spot-verify (METHODOLOGY.md:330-331). C2/C6 are inspection; nothing executes anything. This *is* the named no-battery residual — my finding is not "run a battery" but that its legal form is wrong (L-4) and that M-1 would partially observe this gap for free.
2. **D-8 escape-rate drift** (medium). No criterion or reporting duty observes how often the escape is invoked across future hunts; if every hunt claims "intermittent → hypotheses first," repro-first is dead in practice. Scenario: three hunts hence, zero blind-repro attempts on record. Cheap partial: require the recorded inversion entry to name which infeasibility class applies.
3. **Behavior of full-GC triage passes after D-11's sentence lands** (medium-high until L-1 is fixed). No criterion observes an actual full-GC pass; C3 checks only that referenced text exists. Scenario in L-1.
4. **Characterized-verdict attractor** (low-medium). D-2 legalizes an honest-partial ending; whether hunts route there prematurely is guarded only by sign-off (d), whose exercise no criterion observes. Inherent to any new verdict; acceptable.
5. Proactive-trigger behavior: effectively **none** — the SKILL frontmatter description (SKILL.md:3) and Trigger section (METHODOLOGY.md:417-424) are untouched.

---

## POSITION LENS (trigger fires — prompt documents; "all info still present" is not a clean verdict)

- **Stage-7 detail — the heaviest cluster (D-5 + D-13 + D-14, with D-2's block immediately after).** The section (METHODOLOGY.md:178-188) roughly triples. Displaced neighbors: the conjunctive three-part bar (:178-184) currently *is* the section; post-change it becomes the head of a long section whose tail is two new blocks plus D-2's block — the "last thing read before acting at stage 7" shifts from the gate-marker and toggle-triage sentences (:185-188) to D-14/D-2 content. This is dilution at exactly the stage where both user-observed failures live. **The plan specifies no intra-section insertion order for any multi-block cluster** — in a position-sensitive assembly, insertion order within the section is part of the edit spec, not a build detail. Rank: **minor** (plan gap): add one ordering note per cluster; have D-13/D-14 blocks close by re-anchoring the bar ("…recorded — only then is 'found' declarable").
- **Stage-6 detail (D-3 + D-7 + D-12):** ~5 sentences into a 5-line section (:172-176) — doubles it. The additions are mutually coherent counting rules (low contradiction risk), but the terminal punch line ("This is the defense against token-burning thrash", :176) and the refuse-to-start rule risk mid-section burial. Same ordering-note fix; covered by the minor above.
- **Charter section (D-1 + D-11 + D-12 aiming bullet):** appending D-12's aim changes the aiming list's last-item identity (:323-327); the closing discipline paragraph (:330-331) must stay terminal. Nitpick — one placement note.
- **Representativeness-gate section (D-4):** placing detector validation inside the section deliberately inherits "mandatory, blocking, non-waivable" (:217) — intended and good; the instrument paragraph (:227-233) keeps its position. Clean.
- **Stage-1 detail (D-8):** exception lands after the rule it excepts (:134-135) — correct order given sweep item 4's required wording. Clean. Residual: the diagram (see M-2).
- **SKILL step list / triage / config Rules / Inputs:** inline clause extensions, ordering preserved; the self-check rewrite sits at file end and stays last. Clean.

---

## Criterion-label audit

C1-C6 gating: each is verifiable by its stated stage-8 method (inspection/`wc -l`/`diff`/`git diff` — legitimate for text-presence properties, with the L-7 caveat that the run should record why inspection counts as execution here). C1's oracle-completeness defect is L-3; C2's oracle mismatch is F-1; C2's contradiction scope is part of L-1. **C7's advisory label does not survive the audit as-is** (L-4): the stated reason "(reporting duty)" doesn't justify non-blocking for the one criterion carrying the run's honesty obligations; recommend gating. C3's list is **complete** (task addition #4): charter core + discipline bullets incl. provenance (GC METHODOLOGY.md:237-250), severity model (dragonfly imports it wholesale, METHODOLOGY.md:336), probabilistic rubric (GC METHODOLOGY.md:150-153 — the plan's anchor phrase "states the pass rate it expects" exists at :151), lite definition (METHODOLOGY.md:284-290) — I found no further by-reference import the amended text will rely on (D-10's mirror is restatement, not reference; full-GC invocation is the skill itself).

---

## Findings summary (ranked)

| # | Sev | Finding |
|---|---|---|
| L-1 | **major** | D-11 exemption unscoped → contradicts imported GC stage-3 coverage-challenge rule for full-GC triage passes; no sweep item, and C2/C3 as scoped cannot catch it |
| F-1 | minor | C2's enumerated sweep items mismatch the plan's sweep list (gating criterion, ambiguous oracle) |
| F-2 | minor | Sweep item 6 "one discipline, no second bar" mischaracterizes D-4's new silent-on-clean half |
| L-2 | minor | D-2 vs stage-9 headline: exception not carried at stage 9 (no mapping location) |
| L-3 | minor | D-2 sign-off / D-6 dead-path stop points missing from both stop-for-human inventories (invisible to C1) |
| L-4 | minor | No-battery residual: honest, but needs GC-legal form — C7 → gating + route-(b) named risk-acceptance in decisions.md |
| POS-1 | minor | No intra-section insertion ordering specified for the stage-7/stage-6 clusters (bar-dilution risk) |
| M-1 | minor | Free retrodiction check against the recorded hunt not in the measurement plan |
| M-2 | minor | Diagram line 91 left as the only absolute statement of the D-8-excepted rule |
| U-2 | minor | C4 SKILL cap tight against the D-10 rewrite + 13 re-wrapping clause insertions (substance-compression risk) |
| L-5..L-8, M-3, M-4, U-4, U-5 | nitpick | As stated above |

Unverifiable (flagged, not accepted): AR-1/AR-7/"13 arms"/F-designators (sibling-run docs outside closed set); "flagship test never run" (absence-consistent); D-13/D-14 "user-observed" precedent details (testimony, honestly labeled).

---

**Verdict: MAJOR (L-1) — return to plan: scope D-11's coverage-challenge exemption to dragonfly's direct stage-7 and lite passes (full-GC triage passes keep guarded-change's own stage-3 duties), add the matching sweep item, and widen C2's contradiction scope to imported rules; fold the minors (C2 list alignment, D-2 stage-9 clause, stop-for-human locations, C7→gating + named risk-acceptance, cluster insertion-ordering notes) into the same plan touch.**
