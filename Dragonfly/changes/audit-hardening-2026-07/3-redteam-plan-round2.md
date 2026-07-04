# 3 — Red-team of {1-spec, 1.5-criteria, 2-plan} — ROUND 2 (post-MAJOR-bounce) — verbatim record

## Provenance
- **Date:** 2026-07-04. **Reviewer:** cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author (fresh spawn; not the round-1 agent).
- **Context given (closed set, 13 files):** change docs {0-audit-findings, 1-spec,
  1.5-criteria, 2-plan, decisions, 3-redteam-plan}.md + Dragonfly source {METHODOLOGY,
  SKILL}.md (pre-change) + Guarded_change source {METHODOLOGY, SKILL}.md (cross-ref
  target, `9cec23d`) + hunt evidence
  `~/Desktop/companion-emergence/hunts/monologue-bleed-memory-gap/{decisions, hypotheses,
  CONTEXT-BLOAT-HUNT}.md`. Reviewer-reported sha256s at the top of the verbatim output
  below (reviewer additionally ran `wc -l` on the four skill files to confirm baselines —
  declared, in-scope corroboration).
- **Task versus round 1:** TASK A = per-finding resolution check of every round-1 finding
  against the revised docs; TASK B = fresh four-lens pass + coverage challenge + position
  lens + label audit, with round-2-specific task additions (changed-rows challenge, cap
  re-estimate, C8 legal form, risk-acceptance scope accuracy).
- **Transport note:** output arrived through the harness task-notification layer
  (HTML-escaped angle brackets/ampersands); `&lt;slug&gt;` and `&amp;` de-escaped to
  literal characters. No other normalization.
- **Charter/prompt given (verbatim):** recorded in the Agent call of this session's
  transcript; identical discipline core to round 1's charter (quoted verbatim in
  `3-redteam-plan.md`) plus the TASK A resolution-check section and these task additions
  (quoted): 'Challenge the revised mapping table row-by-row for the CHANGED rows only
  (D-1, D-2, D-4, D-7, D-8, D-11, D-12, the new L-3 wiring row) … Are the C4 caps
  (515/148/655) still realistic now that the revision ADDED mapped substance … Is the C8
  criterion's legal form correct (an executed criterion at stage 8, not a deferred one)?
  Is the narrow risk-acceptance's scope statement accurate — is "dilution of pre-existing
  duties" really the ONLY thing C8 cannot observe?'

## Reviewer output (verbatim)

# STAGE-3 RED-TEAM, ROUND 2 — dragonfly `audit-hardening-2026-07` {1-spec, 1.5-criteria, 2-plan} (revised post-MAJOR-bounce)

Reviewer: cold pass, no shared context with the author. Agent: Claude Code subagent (general-purpose-equivalent), model Fable 5 (`claude-fable-5`).

## Context-file hashes (sha256, computed by me)

```
f753d7fcf809a0303ee91dbeb85cbba327f5c01e0d753cde5aaecc98dbde5cbc  Dragonfly/changes/audit-hardening-2026-07/0-audit-findings.md
a048500048675f38e7c9448e489dc99de5e0cffe0f234fc7cc6ed945d10b6cc7  Dragonfly/changes/audit-hardening-2026-07/1-spec.md
7a698b5551a1304a9df68e4a4ac2a76d0b9afc08e81bb090eb7a500d59ae531f  Dragonfly/changes/audit-hardening-2026-07/1.5-criteria.md
108a043cf047ff9b884a274343d4a4fb2c5f3ea8de0f8bd0cfd0c528f728614b  Dragonfly/changes/audit-hardening-2026-07/2-plan.md
d67a40f5e9364edd6aefd38a98ba4e50df344d3b2e6580558a9811f64c135415  Dragonfly/changes/audit-hardening-2026-07/decisions.md
d54aaabe8a514805f4a1022c8d48f976341dc7e8dc772c24c301e9c6b8cd86cd  Dragonfly/changes/audit-hardening-2026-07/3-redteam-plan.md
03533146f68896ba6646533ff404d1f5352024a6129e061d2ac9fbf91c203670  Dragonfly/METHODOLOGY.md
23b585d7e1701b99a9fdd8637e06df29fd8cf43f9e08a7315a403b51317c4d47  Dragonfly/SKILL.md
35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3  Guarded_change/METHODOLOGY.md
4e2a2e5135ce0d3397fa208a18e4f1715e22e3738b99bca16cea153e7302839b  Guarded_change/SKILL.md
a4c2addadfb78c3fe419222a52caf51218330e7d7b00ca7ec2e342dc8023606a  hunts/monologue-bleed-memory-gap/decisions.md
fcfcd687929cd1f846309f03fd093c030c76c4c30fe9cf78ba275b22ec0586bc  hunts/monologue-bleed-memory-gap/hypotheses.md
46ae8d4f0c9afd7793c041a944e144dc06d71bf183136ae1be78e499d46cb98f  hunts/monologue-bleed-memory-gap/CONTEXT-BLOAT-HUNT.md
```

Closed set respected: only the thirteen files above (plus one `wc -l` on the four skill files to confirm the 441/129/534/124 baselines — matches 1-spec.md:39-40 and run decisions.md:7-9). Dragonfly source hashes are identical to round 1's (`03533146…`, `23b585d7…`) — the amended target is unchanged since round 1, as the additive-only plan requires. 1-spec.md hash matches round 1's (`a0485000…`) — spec unrevised, consistent with a MAJOR→return-to-plan route (spec untouched is correct for that route).

---

## TASK A — RESOLUTION CHECK (round-1 findings)

| ID | Sev | Disposition | Evidence in revised docs |
|---|---|---|---|
| **L-1** | major | **RESOLVED** | D-11 row rewritten, 2-plan.md:29: "The stage-3 coverage-challenge bullet does NOT apply to dragonfly's **direct stage-7 passes and lite passes** (neither is a stage-3 review, so that bullet never bound them; dragonfly's analog is the D-12 duty) — but a **full guarded-change triage run keeps ALL of guarded-change's own stage duties, including its stage-3 coverage challenge**: dragonfly's charter narrows nothing inside a full-GC run." Sweep item 9 added, 2-plan.md:70-76 ("Full-GC triage runs are affirmatively carved OUT of the exemption"). C2 contradiction scope widened, 1.5-criteria.md:21: "no new rule contradicts an existing dragonfly rule **or an imported guarded-change rule**", with item "(9) D-11's scoped exemption vs the imported coverage-challenge duty" in the enumerated sweep. All three demanded elements present; the scoping matches the imported rule's actual scope (GC METHODOLOGY.md:251 "**Challenge criteria coverage (stage 3).**"; GC METHODOLOGY.md:243-244 "plus the coverage-challenge bullet for stage-3 reviews"). |
| **F-1** | minor | **RESOLVED** | 1.5-criteria.md:21 now enumerates "the plan's contradiction-sweep items **1–9**" with per-item summaries; I checked all nine against 2-plan.md:37-76 — numbering and substance align item-for-item (e.g. C2's "(2) D-3's cycle unit vs D-7's per-thread counts" = plan item 2 at 2-plan.md:41-42; the round-1 phantom items "stage-8 verdict set"/"stage-6 cap text" are gone). |
| **F-2** | minor | **RESOLVED** | Sweep item 6 restated, 2-plan.md:56-63: "The **silent-on-known-clean half is NEW and intended** — a strictly stronger requirement (adds, loosens nothing)… the builder must know it is a deliberate delta, not a restatement. Boundary (must appear in the built text): anything that *decides* symptom-present/absent … is a detector and carries both halves; an instrument that merely captures data … keeps the existing fire-on-known-occurrence bar only." Boundary also carried in the D-4 row substance (2-plan.md:22). |
| **L-2** | minor | **RESOLVED** | D-2 row (2-plan.md:20) gains "stage-9 detail: one clause" + SKILL "step 9: one clause", with the substance: "the **stage-9 detail itself carries this exception in one clause** (for a characterized handoff there is no stage-7 chain+toggle to use; the executor must not be handed a bar that cannot exist)". Directly answers the round-1 scenario (stage-9 headline unconditional at METHODOLOGY.md:194, 9a at :196). |
| **L-3** | minor | **RESOLVED** | New mapping row "**D-2/D-6 stop-point wiring (L-3)**", 2-plan.md:33: METHODOLOGY "'Human-in-the-loop' section: two list items" + SKILL "'Stop-for-human rules' section: two clauses", naming both new stop points and distinguishing "config invalid for this machine" from the existing "config is missing" (SKILL.md:117, METHODOLOGY.md:435). Now inside C1's oracle. (Fresh follow-on findings R2-L-1 and R2-P-2 below concern this row's wording and placement, not its existence.) |
| **L-4** | minor | **RESOLVED** | C7 relabeled: 1.5-criteria.md:26 "**gating** (a report-content criterion: inspection of the report for each required item is cheap and unambiguous; non-blocking would let the run's honesty obligations silently vanish from the report)". Risk-acceptance path: owner tie-break recorded owner-attributed, decisions.md:57-62: "adopt M-1 as gating criterion C8 … + the narrow named risk-acceptance … The formal risk-acceptance entry is recorded at gate 4 on route-to-build, owner-attributed", echoed at 1.5-criteria.md:10-11. The formal entry does not exist yet — correct at this stage (gate 4 is next); it MUST appear at route-to-build (verify-later item; GC METHODOLOGY.md:267-268 "a route-(b) named risk-acceptance must actually be present in decisions.md"). Scope-accuracy of the acceptance is challenged fresh at R2-U-2. |
| **POS-1** | minor | **RESOLVED** | New subsection "Insertion order (position lens — part of the edit spec, not a build detail)", 2-plan.md:78-99, with exactly the demanded content: stage-7 cluster order + "The cluster's closing lines re-anchor the three-part bar" (:83-89); stage-6 "the terminal punch line … **stays the section's last line**" (:90-92); charter closing discipline paragraph "**remains the section's terminal text**" (:93-95). Fresh follow-on findings R2-P-1..P-3 below. |
| **M-1** | minor | **RESOLVED** | C8 added as a gating executed criterion, 1.5-criteria.md:27 + Measurement 2-plan.md:118-137, with the four sub-checks and pre-registered outcomes M-1 sketched (cycle count, S1-O15 residual, D-2 checklist vs the S1 ending, D-8 escape vs the inversion). |
| **M-2** | minor | **RESOLVED** | Breadcrumb ADOPTED: D-8 row 2-plan.md:26 "loop-diagram stage-1 line (:91): one breadcrumb parenthetical … '(escape for bugs unreproducible blind: see stage-1 detail)' so the excepted rule is nowhere stated as absolute"; sweep item 4 updated (2-plan.md:45-52: "the breadcrumb points, it does not state a second rule"); decisions.md:72-73 records the adoption. METHODOLOGY.md:91 confirmed as the target line. |
| **U-2** | minor | **RESOLVED** | C4 row, 1.5-criteria.md:23: "**C1 is read strictly AGAINST C4:** cap pressure never trades away mapped substance — if a row's substance and a cap cannot both hold, bounce to the plan rather than compress"; repeated in Measurement (2-plan.md:104-106). Cap realism re-assessed fresh under the task additions (finding R2-U-3 below — the added substance moves METHODOLOGY toward the pinch too). |
| **L-5** | nitpick | **LOGGED (as claimed)** | decisions.md:77-78: "L-5 stays log-only (residual churn covered by the re-examination prong + gate cap)." Matches the gate entry's log-only-unless-free rule (decisions.md:45). |
| **L-6** | nitpick | **FOLDED (verified)** | D-11 row, 2-plan.md:29: "'unconditional' = bullets carrying no stage or trigger scope of their own" — consistent with GC's charter composition (GC METHODOLOGY.md:242-246). Claim at decisions.md:74. |
| **L-7** | nitpick | **RESOLVED (recorded)** | decisions.md:46-48: "for text-presence criteria, locating + quoting the governed text IS executing the check, same reading the sibling run recorded" — the requested decisions.md note exists. |
| **L-8** | nitpick | **FOLDED (verified)** | D-12 consequence enforcement-shaped, 2-plan.md:30: "→ a stage-6 pass missing the class-coverage/shared-assumption record is a **gate violation** (same standing as an uncounted cycle, D-3)". Thread attribution, D-7 row 2-plan.md:25: "a test discriminating across multiple threads increments the counter of **each thread whose hypotheses it splits**". Claim at decisions.md:75. |
| **M-3** | nitpick | **FOLDED (verified)** | D-2 row, 2-plan.md:20: "The `diagnosis.md` artifact line notes: for a characterized ending the file records (a)–(c) in place of root-cause/causal-chain". Claim at decisions.md:67-68. |
| **M-4** | nitpick | **FOLDED (verified)** | Plan intro, 2-plan.md:9-13: "the SKILL self-check mirrors guarded-change's discipline by **restatement, not reference** — deliberate … the drift channel this recreates is exactly what the D-11 cross-reference criterion (C3) exists to watch." Claim at decisions.md:75-76. |
| **U-4** | nitpick | **FOLDED (verified)** | 2-plan.md:8-9: "On any conflict between this table and the audit text, **the mapping table is the build oracle**". Claim at decisions.md:73. |
| **U-5** | nitpick | **FOLDED (verified)** | D-1 row, 2-plan.md:19: "the record lives in, **or is pointed to from**, the hunt folder (a full-GC triage run keeps its record under its own `changes/<slug>/` — nested inside the hunt folder or external with a pointer entry in the hunt's `decisions.md`)". Claim at decisions.md:73-74. |

Also verified: the gate worklist's extra fold "Coverage-gap #2 cheap partial" (decisions.md:76-77) is real — D-8 row, 2-plan.md:26: "recorded in `decisions.md` **naming which infeasibility class applies**".

**Resolution verdict: all 1 major + 9 minors genuinely resolved; all 8 nitpicks folded or logged exactly as decisions.md:72-78 claims. No claimed-resolved-but-unresolved findings.**

---

## TASK B — FRESH FOUR-LENS PASS (revised docs)

### LENS 1 — FACTUAL

**Mapping locations — the NEW locations all exist:**
- Stage-9 detail: METHODOLOGY.md:194-213 (headline :194 "verify the **root cause is resolved**"; 9a :196-206, 9b :207-210) — target for D-2's clause, D-5's sentence, D-14's sentence. ✔
- `diagnosis.md` artifact line: METHODOLOGY.md:395 ("diagnosis.md (stage 8) root cause, causal chain, evidence, repro, recommended fix") — target for D-2/D-13/D-14 extensions. ✔
- "Human-in-the-loop" section: METHODOLOGY.md:427, stop list :431-435, terminal gate-before-present paragraph :437-441. ✔
- "Stop-for-human rules" section: SKILL.md:113-121 ("or **config is missing**" at :117; terminal never-describe-ungated sentence :118-121). ✔
- Loop-diagram stage-1 line: METHODOLOGY.md:91 "1    REPRODUCTION     turn R# into a reliable, REPRESENTATIVE repro BEFORE hypothesizing." ✔
- SKILL step 9: SKILL.md:73-80. ✔
All 14 pre-existing locations re-confirmed unchanged (identical file hashes to round 1; spot-re-verified: charter :311/SKILL :102; stage-6 detail :172-176; stage-7 detail :178-188 with insertion slot before stage 8 at :190; rep-gate :217-233; triage intro :272 + SKILL heading :90; lite paragraph :284-290; config Rules :378-383; SKILL self-check :123-129; aiming list :323-327 + SKILL :108-110).

**C8 pre-registered outcomes vs the hunt record:**
- (iii) S1 ending: hunt decisions.md:68-74 is exactly the "S1 stage-7 red-team | MAJOR | hypothesis REVISED, NOT 'found'" entry, "**S1 outcome = CHARACTERIZATION + mitigation directions, not a code root-cause 'found'**" (:72-73). Element-by-element against D-2's (a)–(e): (a) partially present (structural facts cold-passed, S1-O7), (b) present (H-S1-DISTANCE refuted with evidence), (c) present-ish ("largely a MODEL property — no clean code toggle" :71-72 = a named reason), (d) **absent** — no recorded human sign-off in :68-74, (e) followed (":74 I corrected my earlier over-confident S1 message"). So "names ≥1 missing element" is achievable, non-vacuous, and mechanically adjudicable. ✔ Well-posed.
- (iv) Inversion: hunt decisions.md:87-96 is the "S1 stage-4 — discriminating test DESIGNED" entry (repro designed long after hypotheses formed at :41-48/:51-67); infeasibility-class substance is citable (hunt decisions.md:47-48 "may be emergent context-length coherence decay (a model property, not a clean toggle)"; hypotheses.md:164-165 "bleed is intermittent/load-dependent → instrument-to-capture"); no formal inversion entry exists anywhere in hunt decisions.md → "substance present, formal entry absent" matches the record. ✔ Adjudicable. (Nitpick: calling :87-96 "the recorded inversion" is a compression — that entry records the late repro design; the inversion is the ordering across :41-86 vs :87-96.)
- (ii) S1-O15: the substance ("degradation happened there too but needed **larger files / longer time** → dose-dependent") is at hunt decisions.md:77, but the identifier "(S1-O15 refinement)" sits on :76 — the cited :77-79 is off by one at the head and spills into S1-O16 archaeology at :78-79. Functionally adequate; cite :76-78 for precision (R2-F-4, nitpick). The deeper issue with (ii) is logical, not factual — see R2-L-3.
- (i) D-3 cycle count: the record contains completed run-and-recorded laps for S2 (hunt decisions.md:24-27 replay/toggle triage + the O16/O17 runs feeding :28-36) and **zero** completed stage-4→5 laps for S1 (its only designed discriminating test "Awaiting user go/no-go", :96; harness build in flight, :104-115). A per-thread number is computable — but see R2-L-2 on the softness of "definite number, laps cited" as a pass bar.

**Other claims:** C3 anchor phrase "states the pass rate it expects" exists at GC METHODOLOGY.md:151 ✔. Provenance bullet at GC METHODOLOGY.md:236-250, "for stage-3 reviews" scoping at :243-244, coverage bullet at :251-255 ✔. Baselines 441/129/570 and GC 534/124 confirmed by `wc -l` ✔. "Two-of-three is not 'found'" survives at METHODOLOGY.md:178-179 ✔. Sweep item 8's anchor "This skill can be run on its own artifacts" at SKILL.md:125 ✔. Stage-6 punch line "This is the defense against token-burning thrash" is the section's last line at METHODOLOGY.md:176 ✔. Real hunt's nested full-GC record (D-1 pointer-tolerance rationale) at hunt decisions.md:104-105 ✔. Real hunt's config adaptation (D-6/R2-L-1) at hunt decisions.md:5-8 ✔.

**Factual findings:**
- **R2-F-1 (minor).** D-2 row's consequence under-enforces its own requirement: 2-plan.md:20 requires "ALL of: (a)…(e)" but the consequence reads "→ an ending that meets **none** of this is not a legal stop." Literally, an ending meeting (a) alone is not outlawed. Since "the mapping table is the build oracle" (2-plan.md:8-9), this wording is what gets built. Fix: "an ending missing **any** of (a)–(e) is not a legal stop."
- **R2-F-2 (nitpick).** Sweep item 7 (2-plan.md:64-66) says lite "drops spec/criteria/plan/baseline only" — the source enumeration is five items: "spec / criteria / plan / baseline / **regression**" (METHODOLOGY.md:289). "Only" + the missing fifth item could read as regression-retained; mirror the source list.
- **R2-F-3 (nitpick).** C6's expected deletion classes (2-plan.md:112-114: "in-place sentence extensions (triage enumeration…; step/paragraph tails) + the ONE named rewrite") don't name the revision's own new in-place-extension hunks: the diagram line :91 (not a sentence or paragraph tail) and the `diagnosis.md` artifact line :395 (a code-block listing line, extended by three rows). The stage-8 hunk-walk will meet deletion-shaped hunks outside the named classes; add them.
- **R2-F-4 (nitpick).** C8(ii)'s citation: S1-O15 spans hunt decisions.md:76-78 (identifier on :76), not :77-79.
- **Unverifiable, flagged (not accepted):** "13 arms' cost" / AR-7 / F-designators (1.5-criteria.md:13-14, 2-plan.md:5-6, decisions.md:4) — sibling-run docs outside the closed set, unchanged from round 1; corroborated only indirectly by GC METHODOLOGY text embodying the named rules (provenance :236-250, path validation :472-479, freeze :168-176). Also unverifiable in my set: whether `observation-ledger.md`/`symptom-ledger.md` exist as files in the hunt folder (referenced by CONTEXT-BLOAT-HUNT.md:47 "see observation-ledger.md" but not in the closed set) — load-bearing for R2-L-4.

### LENS 2 — LOGICAL

**(a) D-11 rewrite + sweep item 9 vs the round-1 contradiction: ELIMINATED.** The exemption now names only "direct stage-7 passes and lite passes" (2-plan.md:29) — neither is a stage-3 review (a direct stage-7 pass reviews a causal chain; a lite pass reviews one artifact against a one-line intent+criterion using the charter core, METHODOLOGY.md:286-290), so GC's stage-3-scoped bullet (GC METHODOLOGY.md:251) never bound them; D-12 is a genuine analog. Full-GC triage runs are affirmatively carved out ("keeps ALL of guarded-change's own stage duties, including its stage-3 coverage challenge") — exactly the round-1 failure scenario (a token-burning harness entering full GC per METHODOLOGY.md:277-279, as the real hunt did at hunt decisions.md:104-105) is now covered by explicit text, and C2 item 9 + the widened contradiction scope (1.5-criteria.md:21) give stage 8 a hook to verify it landed. No residual contradiction found. The L-6 definition ("no stage or trigger scope of their own") does make GC's label-audit bullet (GC METHODOLOGY.md:257-274) nominally bind dragonfly passes that have no criteria labels — vacuously satisfied, not a contradiction; acceptable.

**(b) C8 well-posedness — three real gaps:**
- **R2-L-2 (minor). Sub-check (i)'s expected outcome is too soft to fail.** "A definite per-thread number, laps cited" (1.5-criteria.md:27, 2-plan.md:124-125) can be produced under *any* lap-interpretation — the executor picks what counts as a "completed stage-4→5 lap" (does S2's replay+toggle pair count as one lap or two? does S1's read-only git archaeology, hunt decisions.md:78-81, count? S1's only designed discriminating test never ran, :96). Lap-identification ambiguity is precisely where a vacuous D-3 would hide, and the sub-check as posed cannot detect it. Fix (one line): pre-register the expected counts or the candidate-lap inventory (e.g. "S2: the O16/O17 replay+toggle laps; S1: 0 completed laps — its designed test never ran"), so a divergent count is a visible adjudication, not silent wiggle.
- **R2-L-3 (minor). Sub-check (ii) lacks a time/chain anchor.** D-14's sweep judges rows "explained by the confirmed chain" — but S1 never had a confirmed chain (ending = characterization, hunt decisions.md:72-73), and S1-O15 post-dates that ending (:75-78); meanwhile the final recorded candidate H-S1-WRITELOAD-DOSE *explicitly subsumes* the dose-dependence S1-O15 evidences (hypotheses.md:76-88: "exactly the user's A/B (S1-O15)"). So a replay against the final state can fail unfairly (the candidate explains it) and a replay against "no confirmed chain" passes vacuously (every row is a residual, so flagging S1-O15 is trivially true). The audit's precedent pins the intended anchor: the row was "overlooked as 'not the primary cause'" under the then-leading 0.0.38-shaped story (0-audit-findings.md:144-147). Fix (one sentence): anchor the sweep at the moment S1-O15 was recorded, against the then-live leading account — expected: the rule demands a residual entry that the record lacks.
- **R2-L-4 (minor). C8's closed evidence set omits the ledgers the replayed rules are defined over.** D-14 walks "the observation-ledger rows tied to the `S#`" (2-plan.md:32) and D-3 counts recorded laps, but the evidence set is only `{decisions,hypotheses,CONTEXT-BLOAT-HUNT}.md` (1.5-criteria.md:27, 2-plan.md:119-120) — `observation-ledger.md` (referenced at CONTEXT-BLOAT-HUNT.md:47) is excluded, so the replay walks only observations *mentioned* in the gate log and hypotheses file. Either add the ledgers to the set or record why the three files suffice (e.g. every S1-O# the sub-checks need is quoted in them).
- Sub-checks (iii) and (iv): well-posed (see the factual lens). The fail-clause "a sub-check that cannot produce its expected outcome = C8 fails (the rule as built is vacuous or wrong)" (2-plan.md:136-137) is the right shape.

**(c) C7's gating label: verifiable by its stated method.** "Inspection of the final report: each required content item located + quoted" (1.5-criteria.md:26) — for a report-content criterion, locating+quoting the governed text IS exercising the governed path; the literal conflict with GC METHODOLOGY.md:403-404 ("inspection-only … counts as verified = no") is defused by the recorded L-7 note (decisions.md:46-48). The label's stated reason is legitimate. ✔ No issue.

**(d) Stop-point wiring row vs existing stop-for-human text — one internal contradiction:**
- **R2-L-1 (minor).** The wiring row's (b) conflates two conditions D-6 deliberately separates. D-6 row (2-plan.md:24, matching the audit at 0-audit-findings.md:64-68): *invalid-for-this-machine* config → adaptation recorded in `decisions.md` "BEFORE stage 0 proceeds" (i.e. adapt, record, **proceed**) vs *dead paths* → "surface to the human." The wiring row (2-plan.md:33) instead declares "**dead/invalid config paths** at hunt start surface to the human … 'config invalid for this machine' is a **distinct stop**". Built literally, every cross-machine adaptation becomes a mandatory human stop — which contradicts the D-6 row's own flow and would have stopped the real hunt's self-adaptation that the audit calls laudable (hunt decisions.md:5-8; 0-audit-findings.md:62-63). One clause fixes it: the stop is for **dead/unresolvable** paths; a recorded adaptation is surfaced, not blocking. (No conflict with the *existing* inventories — METHODOLOGY.md:435 / SKILL.md:117 "config is missing" is correctly identified as a different condition.)

No other contradictions found: sweep items 1-9 each reconcile against the quoted source text (item 1 vs the tier system at METHODOLOGY.md:237-267 and stage 9 at :194-213; item 4's breadcrumb-points-not-states structure vs :91 and :134-135; item 5 vs :178-179; item 6 vs :227-233; item 7 vs :284-290 modulo R2-F-2; item 8 vs SKILL.md:123-129).

### LENS 3 — MISSED OPPORTUNITY (within additive-only)

- **R2-M-1 (minor). D-12 has a fully-recorded fixture and no C8 sub-check.** The shared false assumption is *in the record*: "Second S1 hypothesis killed by a false architectural assumption (cf. H-S1-DISTANCE)" (hypotheses.md:65-66), "SECOND S1 code hypothesis refuted on a false architectural assumption" (hunt decisions.md:64-65). A fifth token-free sub-check — the D-12 class-coverage/shared-assumption record, retrodicted at the recorded convergence point, names "the Python tool-loop mattering on the claude-cli path" as the live set's shared assumption — is free by the same method and tests one of the audit's two motivating shared-blind-spot rules. By contrast, D-13's omission is defensible (its precedent is user testimony, not in-record — round 1 flagged it unverifiable-but-labeled; CONTEXT-BLOAT-HUNT.md:36-38 only implies it) — but the plan should *say* the sub-check selection rule (rules with recorded fixtures) so the omissions read as reasoned, not arbitrary.
- **R2-M-2 (nitpick).** The stage-8 retrodiction output is author-run and self-adjudicated; the pre-registered outcomes bound the goalposts, but one guarded-change-lite cold pass over `8-retrodiction.md` (a single self-contained document, no tokens — squarely triage class 3, SKILL.md:96-99) would remove the last self-certification residue for the run's only executed behavioral evidence, at one cheap pass.

### LENS 4 — UNSTATED ASSUMPTIONS & RISKS

- **R2-U-1 (minor). The C8 fixture is not frozen.** The hunt is live — CONTEXT-BLOAT-HUNT.md:1 marks it "resume here (TOMORROW's priority)". `decisions.md` is append-only (existing line cites survive), but new entries landed between now and stage 8 can flip pre-registered outcomes: a resumed hunt that writes a formal inversion entry breaks (iv)'s "formal entry absent"; a new S1 finding that explains S1-O15 under a confirmed chain breaks (ii). `hypotheses.md` is not even append-only (statuses are edited in place, e.g. the woven-in REFUTED banners at hypotheses.md:49-66). The criteria freeze (F4, 1.5-criteria.md:29-30) freezes the criteria, not the evidence. Fix (one line in the freeze note): record the three hunt files' sha256 at gate-4 freeze and run C8 against the pinned copies.
- **R2-U-2 (minor). The narrow risk-acceptance's scope statement is not accurate as "the ONLY thing".** 1.5-criteria.md:8-9 frames C8's blind spot as exactly "whether the added text **dilutes Opus's execution of pre-existing duties**". Two more things C8 cannot observe: (a) **live, unprompted firing of the NEW rules** — C8 is the author deliberately applying the rules' adjudication logic to a record; it proves the rules are computable and non-vacuous, not that an Opus executing the amended prompt will invoke them (the note's claim that C8 "executes the NEW rules' behavior", 1.5-criteria.md:8, overstates this); (b) **vacuousness of the ten rules C8 doesn't sample** (D-1, D-4, D-5, D-6, D-7, D-9, D-10, D-11, D-12, D-13 — e.g. D-5's ledger-frequency-derived window could prove incomputable in a real ledger). Both are adjacent to C7's no-battery residual (1.5-criteria.md:11-15), but the gate-4 formal risk-acceptance entry should name all the accepted residual classes, not let "dilution" read as exhaustive.
- **R2-U-3 (minor). C4 caps: now tight on BOTH files.** Task-addition estimate: the revision added mapped METHODOLOGY substance (stage-9 clause; stop-point items +2-3; D-11 second sentence + "unconditional" definition +3-4; D-4 boundary sentence +2-3; bar re-anchor lines +2; diagram breadcrumb +1; artifact-line extensions +2-3) on top of round 1's ~55-70-line estimate → my per-row re-estimate: METHODOLOGY ~60-80 added lines vs **+74** headroom; SKILL ~13-21 (D-10 rewrite net +5-8, ~15 inline clauses with re-wrap, 2 stop clauses, step-9 clause) vs **+19**; combined ~73-100 vs **+85**. The mid-range fits; the upper range exceeds all three caps. The C1-vs-C4 bounce rule (1.5-criteria.md:23) makes the failure legal and visible rather than silent — but a foreseeable bounce is built in. Criteria are unfrozen: either raise the caps ~10-15 lines now (owner call — D-S1 attention-budget tension noted) or accept the bounce mechanism knowingly; record which.
- **R2-U-4 (nitpick).** "owner-adopted at gate 4" (1.5-criteria.md:5, 2-plan.md:118, :149) anticipates a gate not yet held; the adoption was a session tie-break (decisions.md:57) with the formal entry queued for gate 4. Say "owner-adopted (tie-break 2026-07-04; formal entry at gate 4)".
- **R2-U-5 (nitpick).** `9-report.md` (2-plan.md:115) is a run-specific artifact in neither skill's artifact canon (GC METHODOLOGY.md:493-503 ends at 8-harness.md); C7's verification presumes it exists — fine, but stage 8 must actually produce it.
- Accepted, noted: the GC cross-ref target is assumed stable at `9cec23d` through this run's build (a mid-run GC edit would stale C3's grep); D-11's own self-check is the standing defense, and the run is short. `Guarded_change/guarded-change.companion.md` local modification (round-1 note) is outside the four checked files.

---

## COVERAGE CHALLENGE (mandatory)

Round 1 named 5 gaps — disposition in the revision:

1. **Execution fidelity of pre-existing duties under dilution** (was high) — **NARROWED + FORMALIZED, not closed.** Nothing executes the pre-existing duties under the new text, but the residual is now named, bounded by C6/C2/insertion-order inspection, and carried into an owner-attributed named risk-acceptance queued at gate 4 (1.5-criteria.md:8-11; decisions.md:59-62). This is the legal form round 1 demanded.
2. **D-8 escape-rate drift** (medium) — **NARROWED.** The cheap partial landed: every inversion entry must name its infeasibility class (2-plan.md:26), making drift auditable post-hoc across hunts. The rate itself is still observed by no criterion or reporting duty. Scenario unchanged: three hunts hence, every hunt claims "intermittent," zero blind-repro attempts. Impact now low-medium.
3. **Full-GC triage-pass behavior after D-11** (was medium-high) — **the hazard's cause is CLOSED** (the contradiction is gone; the charter now affirmatively preserves GC's stage duties — 2-plan.md:29, :70-76), the observation gap remains (no criterion watches an actual full-GC pass; C3 checks references resolve). Failure now requires disobeying explicit text rather than obeying wrong text. Impact drops to low.
4. **Characterized-verdict attractor** (low-medium) — **NARROWED slightly.** Sign-off (d) is now wired into both stop inventories (2-plan.md:33) so the guard is discoverable at the moment of use; whether hunts route to "characterized" prematurely is still observed by nothing but the sign-off's exercise. Inherent to any new verdict; acceptable.
5. **Proactive-trigger behavior** — still **none**: frontmatter (SKILL.md:3) and Trigger section (METHODOLOGY.md:417-424) remain untouched by every mapping row.

Fresh gaps (behaviors this revision could alter that no criterion observes):

- **New-rule live firing** (medium-high, the largest remaining gap): no criterion observes whether a future Opus *unprompted* performs the D-14 sweep, D-3 count, or D-12 record at a real gate — C8 observes the rules' logic, not prompt-compliance. Scenario: next hunt reaches "found," the sweep is skipped, nothing in this run would have predicted it. Consciously adjacent to the accepted no-battery residual — but it must be *named* in the gate-4 acceptance (see R2-U-2) to count as accepted rather than missed.
- **Un-retrodicted-rule vacuousness** (medium): 10 of 14 rules get no execution against anything (C1/C2 inspect text). Scenario: D-5's "observation window derived from ledger frequency" meets a real ledger with no frequency data — the rule is unexecutable and nobody learns it until mid-hunt. Partially closable free via R2-M-1 (D-12 sub-check).
- **New stop points' live honoring** (low): C1 verifies the inventory text; nothing observes a characterized ending actually stopping for sign-off. Inherent; the wiring is the cheap 80%.

---

## POSITION LENS (trigger fires — prompt documents)

**Does the "Insertion order (position lens)" subsection (2-plan.md:78-99) neutralize the round-1 displacement concerns?**

- **Stage-7 triple cluster** — **mostly yes, one residue.** The specified order (D-5 in-place → D-13 block → D-14 block → closing lines re-anchoring the bar, D-2 exiled to a separate section between stages 7 and 8) restores "the last thing read at stage 7 is the bar, not a sub-procedure" (2-plan.md:87-88) — the round-1 concern as stated. **R2-P-1 (minor):** the quoted re-anchor ("all three bar items plus both records, conjunctively", 2-plan.md:86-87) omits the **cold-red-team-the-chain duty and its gate-marker consequence** — which is exactly the paragraph that is *currently* the section's terminal text (METHODOLOGY.md:185-188: "A **cold red-team** challenges the causal chain … Passing it sets the hypothesis's gate marker to **`cold-red-teamed`** — a precondition of the 'confirmed' verdict"). Under the specified order that paragraph is displaced mid-section and the new terminal line doesn't carry it. One-clause fix: re-anchor as "all three bar items + both records **+ the chain's cold pass**, conjunctively" (or order the new blocks before :185-188).
- **Stage-6 triple cluster** — **yes** (insert after the cap sentences, refuse-to-start stays attached, punch line stays last, 2-plan.md:90-92). **R2-P-3 (nitpick):** after inserting D-3/D-7/D-12 before it, the punch line's "**This** is the defense against token-burning thrash" (METHODOLOGY.md:176) acquires a new antecedent (D-12's duty); the built text should re-bind the referent ("The cap is the defense…"). Also nitpick: "D-12's aim appends **inside** the aiming list" (2-plan.md:93-94) leaves the within-list position unspecified — say last-or-where.
- **Charter terminal paragraph** — **yes**: D-1/D-11 land before the closing discipline paragraph, "which **remains the section's terminal text**" (2-plan.md:94-95; paragraph at METHODOLOGY.md:328-330).

**New insertions the subsection misses — R2-P-2 (minor):** the revision created two NEW multi-insert locations with no ordering note, inconsistently with its own principle ("insertion order … is part of the edit spec, not a build detail", 2-plan.md:78):
1. **Stage-9 detail now takes THREE insertions** (D-2's exception clause + D-5's window sentence + D-14's residual re-check — 2-plan.md:20, :23, :32) into a section whose terminal text ("A failed verification is never discarded…", METHODOLOGY.md:212-213) is a load-bearing routing rule. No cluster note exists.
2. **The two stop-for-human inventories** get two items each (2-plan.md:33); both sections' terminal texts are the gate-before-present paragraphs (METHODOLOGY.md:437-441; SKILL.md:118-121 "And **never describe a hypothesis as the root cause**…") — the new items must land inside the stop list / stop sentence, not after those paragraphs. The subsection's SKILL bullet ("inline clauses preserve each step's existing sentence order", 2-plan.md:98-99) covers steps, not this section.
- **Diagram breadcrumb** — clean: a pointer-only parenthetical on the :91 line inside the code block; states no second rule (sweep item 4), wraps within the diagram; the only effect is making the diagram's absolute statement non-absolute, which is the point.
- **`diagnosis.md` artifact line** — three rows (D-2/D-13/D-14) extend one code-block line; coherence at build time (nitpick, folded into R2-F-3).

---

## CRITERION-LABEL AUDIT

All eight criteria are **gating**; no advisory labels exist, so there is nothing to challenge on the advisory side — and the absence is legitimate (the round-1 L-4 fix deliberately eliminated the last advisory). Per-criterion verifiability by the stated stage-8 method:
- **C1/C2/C3** — inspection/grep with quoted text + file:line; legal for text-presence properties per the recorded L-7 note (decisions.md:46-48); C2's oracle now matches the plan's sweep 1–9 (F-1 resolved) and its contradiction scope covers imported GC rules (L-1). ✔
- **C4** — `wc -l`, mechanical ✔; realism re-assessed at R2-U-3 (tight on both files; the C1-against-C4 bounce rule is the named relief valve).
- **C5** — `diff`, mechanical ✔. **C6** — `git diff 9cec23d` hunk-walk ✔ (expected-class list needs the two new hunk shapes, R2-F-3).
- **C7** — gating with a stated, legitimate reason (1.5-criteria.md:26); verifiable by locating+quoting report content, which IS the governed path for a report-content criterion. ✔
- **C8** — **legal form correct** (task addition): an *executed* criterion at stage 8 — the replay runs at stage 8, output recorded with hunt-record citations in 8-harness.md/8-retrodiction.md (1.5-criteria.md:27; 2-plan.md:118-123) — not a deferral, not a proxy (the recorded hunt IS the governed fixture, the route-(a) shape of GC METHODOLOGY.md:379-381), with pre-registered outcomes and an explicit fail clause. Its verifiability caveats are the well-posedness findings R2-L-2/L-3/L-4 plus the unfrozen fixture R2-U-1; sub-checks (iii)/(iv) are adjudicable as posed today.
- The route-(b) named risk-acceptance is correctly promissory at this stage (queued for gate 4, decisions.md:61-62); its **scope wording** needs R2-U-2's widening before it is recorded.

---

## FINDINGS SUMMARY (ranked)

| # | Sev | Finding |
|---|---|---|
| R2-L-1 | minor | Stop-point row (2-plan.md:33) conflates invalid-config (D-6: adapt+record+**proceed**) with dead-path (stop) — "'config invalid for this machine' is a distinct stop" contradicts the D-6 row's own flow and would have stopped the real hunt's laudable adaptation (hunt decisions.md:5-8) |
| R2-L-2 | minor | C8(i) expected outcome too soft to fail — "a definite per-thread number" passes under any lap-interpretation; pre-register expected counts / candidate-lap inventory (S2: O16/O17 laps; S1: 0) |
| R2-L-3 | minor | C8(ii) has no time/chain anchor — S1 has no confirmed chain (vacuous pass) and the final candidate explains S1-O15 (hypotheses.md:76-88 — unfair fail); anchor at the moment S1-O15 was recorded, per the audit precedent (0-audit-findings.md:144-147) |
| R2-L-4 | minor | C8's evidence set omits `observation-ledger.md`, the file D-14's sweep and D-3's laps are defined over (2-plan.md:32 vs :119-120) |
| R2-U-1 | minor | C8 fixture unfrozen — the hunt is live (CONTEXT-BLOAT-HUNT.md:1); new entries/edits before stage 8 can flip (ii)/(iv); pin sha256 of the three hunt files at gate-4 freeze |
| R2-U-2 | minor | Risk-acceptance scope statement inaccurate as "the ONLY" — C8 also cannot observe live unprompted firing of the new rules, or the 10 un-sampled rules' vacuousness; name all residual classes in the gate-4 entry (and "executes the NEW rules' behavior" at 1.5-criteria.md:8 overstates) |
| R2-U-3 | minor | C4 caps now tight on both files (added substance ~+12-16 METHODOLOGY lines vs round 1; my range 60-80 vs +74 headroom, SKILL 13-21 vs +19); foreseeable C1-vs-C4 bounce — raise caps pre-freeze or knowingly accept the bounce mechanism, record which |
| R2-F-1 | minor | D-2 consequence "meets **none** of this" under-enforces the "ALL of (a)-(e)" requirement (2-plan.md:20) — build oracle wording; change to "missing **any**" |
| R2-P-1 | minor | Stage-7 re-anchor line omits the cold-red-team-the-chain duty + gate-marker consequence — the currently-terminal paragraph (METHODOLOGY.md:185-188) is displaced and its content isn't in the new terminal text |
| R2-P-2 | minor | Insertion-order subsection misses the revision's own new clusters: stage-9 detail (3 insertions; terminal :212-213) and both stop-for-human inventories (terminal gate-before-present paragraphs :437-441 / SKILL :118-121) |
| R2-M-1 | minor | D-12 has a recorded fixture (hypotheses.md:65-66; hunt decisions.md:64-65) and no C8 sub-check — a free fifth sub-check; also state the sub-check selection rule (recorded-fixture rules only) so D-13's omission reads as reasoned |
| R2-F-2, R2-F-3, R2-F-4, R2-M-2, R2-U-4, R2-U-5, R2-P-3 | nitpick | As stated above (lite enumeration drift; C6 hunk classes; S1-O15 cite :76-78; lite pass on 8-retrodiction; "owner-adopted at gate 4" anticipates; 9-report.md non-canon; punch-line antecedent + aiming-list position) |

Unverifiable (flagged, not accepted): sibling-run designators (AR-7, "13 arms", F-numbers — outside closed set); existence of `observation-ledger.md`/`symptom-ledger.md` as files in the hunt folder.

Resolution check: **all round-1 majors/minors RESOLVED with confirming text; all nitpicks folded or logged exactly as claimed** — no re-raised findings at original severity. All fresh findings are one-clause/one-line fixes to plan or criteria, legal pre-freeze.

---

**Verdict: MINOR (worst: R2-L-1/R2-L-3/R2-U-1 class — local, fixable in place) — fix in place, proceed to build: correct the stop-point invalid-vs-dead wording, tighten C8's (i)/(ii) pre-registrations + add the ledgers or a stated reason, pin the hunt-fixture hashes at the gate-4 freeze, widen the risk-acceptance's named scope, patch the D-2 consequence wording, add the two missing insertion-order notes (+ the chain's cold pass to the stage-7 re-anchor), and decide the C4 cap question before freeze.**
