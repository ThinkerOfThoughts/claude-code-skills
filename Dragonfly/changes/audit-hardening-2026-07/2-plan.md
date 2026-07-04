# 2 — Plan: dragonfly audit-hardening-2026-07

Additive edits to `Dragonfly/METHODOLOGY.md` + `Dragonfly/SKILL.md`, one mapping row per
finding. Style: terse, mechanical, wired into existing sections (SKILL clauses pointer-style
— name the METHODOLOGY section, don't restate). **Live copy updated only at stage 8**
(post-gate-7); a hard stage-8 bounce reverts live to the `9cec23d` copies.

On any conflict between this table and the audit text, **the mapping table is the build
oracle** (it deliberately enriches audit rows — e.g. D-2's stage-9 clause). Note on D-10's
shape: the SKILL self-check mirrors guarded-change's discipline by **restatement, not
reference** — deliberate, because the self-check must be executable from SKILL.md alone
without opening the sibling skill; the drift channel this recreates is exactly what the
D-11 cross-reference criterion (C3) exists to watch.

## Edit mapping table (C1's oracle)

| Fix | METHODOLOGY location(s) | SKILL location(s) | Substance (trigger → requirement → consequence) |
|---|---|---|---|
| **D-1 provenance** | "The red-team charter (stages 1, 4, 7)" section | "Cold red-team (stages 1, 4, 7)" section | guarded-change's provenance rule (verbatim charter given, exact context list, reviewer's verbatim output, agent type+model, reviewer-reported context hashes) applies to **every dragonfly cold pass** — stage-7 direct passes AND the triage's guarded-change/lite passes at stages 1/4 — the record lives in, **or is pointed to from**, the hunt folder (a full-GC triage run keeps its record under its own `changes/<slug>/` — nested inside the hunt folder or external with a pointer entry in the hunt's `decisions.md`) → a pass missing any element is treated as un-run (the reading it produced may not be consumed) |
| **D-2 "characterized, not found"** | New short block after the stage-7 detail (before stage 8); stage-9 detail: one clause; `diagnosis.md` artifact line: contents-for-characterized clause | Step 8: one sentence; step 9: one clause | A legal terminal verdict short of "found," requiring ALL of: (a) what IS established, each claim cited + cold-red-teamed like any conclusion; (b) which hypotheses were refuted, with evidence; (c) WHY the full bar is unreachable — named reason (model property / cost bound / needs-live-data), not vague; (d) explicit human sign-off; (e) presentation tier stays "characterization" — never "the cause." Handoff may carry mitigation directions **marked as such**; their stage-9 verification is symptom-evidence only (a mitigation verified as a mitigation, no cause-resolution claim) — and the **stage-9 detail itself carries this exception in one clause** (for a characterized handoff there is no stage-7 chain+toggle to use; the executor must not be handed a bar that cannot exist). The `diagnosis.md` artifact line notes: for a characterized ending the file records (a)–(c) in place of root-cause/causal-chain → an ending missing **any** of (a)–(e) is not a legal stop |
| **D-3 cycle definition** | Stage-6 detail: two sentences | Step 6: one clause | A **cycle** = one discriminating test **run and recorded** (a completed stage-4→5 lap); the cycle count and the per-area re-examination tally are appended to `decisions.md` at each stage-6 pass → the cap is countable from the log; an uncounted stage-6 pass is a gate violation |
| **D-4 detector as artifact** | Representativeness-gate section: one paragraph; triage intro line: add "detector/readout" to the enumeration | Representativeness-gate section: one sentence; triage heading enumeration | The **detector/readout** that decides "the symptom occurred" (a classifier, a grep, a bleed detector) is itself a diagnostic artifact: triage applies, AND its validation is part of the representativeness gate — shown to **fire on a known-true instance and stay silent on a known-clean one**, evidenced by an observation-ledger row, BEFORE any reading it produces is consumed. **Boundary:** anything that *decides* symptom-present/absent (classifier, grep, threshold rule) is a detector and carries both halves — the silent-on-known-clean half is a **NEW, strictly-stronger duty**, added deliberately; an artifact that merely captures data for later reading keeps the existing instrument-to-capture bar only → an unvalidated detector's readings are untrusted (same rejection as a control that doesn't exhibit the symptom) |
| **D-5 probabilistic toggle/window** | Stage-7 detail (toggle item): two sentences; stage-9 detail: one sentence | Step 7: one clause; step 9: one clause | For a rate-based/intermittent symptom: the toggle criterion states the **expected rate shift and run count** (guarded-change's probabilistic rubric, by reference); 9a/9b define their **observation window up front** from the symptom's observed ledger frequency (e.g. ~1/session over 5 sessions → 9b window ≥ N sessions, pass = 0 occurrences) → a single flip, or an unstated window, does not satisfy stage 7/9 for a probabilistic symptom |
| **D-6 config validation** | Config-contract Rules: one bullet | Inputs: one sentence | At hunt start, mechanically check every config path (`redteam_context`, `reproduction.logs`, `ledgers.dir`) exists/readable; an invalid-for-this-machine config → the adaptation is itself a `decisions.md` entry (what changed, why) BEFORE stage 0 proceeds; dead paths surface to the human → a hunt may not proceed on unvalidated paths |
| **D-7 per-thread convergence** | Stage-6 detail: two sentences | Step 6: one clause | A hunt carrying multiple `S#` threads counts convergence **per-thread** (D-3's cycle unit, per thread); a test discriminating across multiple threads increments the counter of **each thread whose hypotheses it splits**; a thread hitting the cap **escalates alone**; threads may be split into separate hunts at any gate with a recorded reason → global counting may not mask per-thread thrash |
| **D-8 repro-ordering escape** | Stage-1 detail: two sentences; loop-diagram stage-1 line (:91): one breadcrumb parenthetical | Step 1: one clause | When a faithful repro cannot be built blind (intermittent / load-dependent / emergent), hypotheses MAY be formed first to inform repro/instrument design, PROVIDED the inversion is recorded in `decisions.md` **naming which infeasibility class applies** and every such hypothesis stays `ungated`; the representativeness gate still binds the resulting repro/instrument before any conclusion. The diagram's stage-1 line gains a pointer breadcrumb "(escape for bugs unreproducible blind: see stage-1 detail)" so the excepted rule is nowhere stated as absolute → the inversion is legal only recorded + tier-bound |
| **D-9 lite-pass record** | Triage section (lite paragraph): two sentences | Triage item 3: one clause | A lite pass records, minimally: the artifact reviewed, the one-line intent + criterion, the reviewer's verdict, and where its verbatim output lives (per D-1), in `decisions.md` → an unrecorded lite pass is treated as not having happened (its artifact stays untrusted) |
| **D-10 self-check parity + honest label** | (none — self-check lives in SKILL) | Self-check section: the one named rewrite (obligation retained + strengthened) | Skill-file edits are edits to a **position-sensitive assembly** (these documents are prompts) — the position lens applies; **non-trivial edits take the full guarded-change loop**. Standing self-check criteria: live == source (`diff`); SKILL ↔ METHODOLOGY consistency on every shared rule; behavior-preservation for anything moved/removed; **every named cross-reference into guarded-change resolves** (D-11). The no-Dragonfly-baseline fixture test is relabeled **aspirational — not yet run** until someone runs it once (then it becomes a standing replayable probe) → an unrun flagship check may not be described as an existing safeguard |
| **D-11 coupling check** | Charter section: two sentences naming which inherited bullets bind and how the scoping works | SKILL self-check criterion (inside D-10's list) | The charter section states explicitly: dragonfly cold passes inherit ALL of guarded-change's **unconditional** discipline bullets — "unconditional" = bullets carrying no stage or trigger scope of their own — **including provenance** (D-1). The stage-3 coverage-challenge bullet does NOT apply to dragonfly's **direct stage-7 passes and lite passes** (neither is a stage-3 review, so that bullet never bound them; dragonfly's analog is the D-12 duty) — but a **full guarded-change triage run keeps ALL of guarded-change's own stage duties, including its stage-3 coverage challenge**: dragonfly's charter narrows nothing inside a full-GC run. Self-check: each named cross-reference (charter section, severity model, probabilistic rubric, lite definition) is checked to resolve after any edit to EITHER skill → a severed reference is a self-check failure |
| **D-12 hypothesis-space challenge** | Charter aiming list: one bullet; stage-6 detail: one duty sentence | Step 6: one clause; "Cold red-team" aiming list: one item | At each convergence-gate pass, record: which mechanism **classes** the live hypotheses cover, which are ruled out, and **what assumption the live set shares** (explicit "none identified" counts); cold passes are aimed at the set's shared assumption too — one found false ranks by impact → a stage-6 pass missing the class-coverage/shared-assumption record is a **gate violation** (same standing as an uncounted cycle, D-3) |
| **D-13 depth check (root-or-relay)** | Stage-7 detail: one block; stage-8 detail + diagnosis.md artifact line: extend contents | Step 7: two clauses; step 8: one clause; "Cold red-team" aiming: one item | The root, for dragonfly's purposes, = the **deepest node the project can act on**. For the claimed root, ask "why does this node produce the next?" ONE level further down; "found" requires recording that the next why-down is (a) **answered** with cited evidence, (b) **explicitly out of scope** (model property / third-party / not actionable — named), or (c) **not load-bearing** for a fix that targets the cause rather than the mechanism's surface. The stage-7 cold pass explicitly challenges "**root or relay?**"; `diagnosis.md` states the chain with each level's status → "explains the symptom" at a relay does not satisfy stage 7 |
| **D-14 evidence-coverage sweep** | Stage-7 detail: one block; stage-9 detail: one sentence; diagnosis.md artifact line | Step 7: one clause; step 9: one clause | Before "found": walk the observation-ledger rows tied to the `S#` — each is either **explained by the confirmed chain** (cite how) or recorded as a **residual** (named secondary contributor / open sub-hypothesis, ranked), carried in `diagnosis.md` + the stage-8 handoff, struck only with a recorded reason. "**Found (primary), with named residuals**" is a legal verdict; **silent absorption is not**. Stage 9 re-checks the residuals list — a fix killing the primary does not close an unexplained residual → an unexplained ledger row without a residual entry blocks "found" |
| **D-2/D-6 stop-point wiring (L-3)** | "Human-in-the-loop" section: two list items | "Stop-for-human rules" section: two clauses | Both stop-for-human inventories name the two NEW stop points these fixes create: (a) a **characterized-verdict ending requires explicit human sign-off** (D-2 (d)); (b) **dead/UNRESOLVABLE config paths at hunt start stop for the human** (D-6 — distinct from the existing "config is missing"; an invalid-but-adaptable config is NOT a stop — per the D-6 row it is adapted, recorded in `decisions.md`, and proceeds, surfaced not blocking) → a mandatory stop point absent from the inventory is undiscoverable at the moment of use |

## Contradiction sweep (C2's checklist)

1. **D-2 vs the gate-before-present tiers** — "characterized" is a presentation tier BELOW
   "the cause"; (e) keeps the tier system intact; mitigation directions are marked, never
   cause-claims. And vs stage 9: a characterized handoff verifies mitigations on symptom
   evidence only — no cause-resolution claim to verify.
2. **D-3's cycle unit vs D-7's per-thread counts** — one unit, counted per-thread; D-7
   references D-3's definition, no second unit.
3. **D-5's borrowed rubric vs the guarded-change reference** — by-reference, resolves via C3;
   no restated rubric text (no drift channel).
4. **D-8's escape vs stage-1 "BEFORE hypothesizing" (and the loop diagram)** — the escape is
   an explicit recorded exception to the stage-1 ordering; the stage-1 detail carries the
   full exception, and the diagram's stage-1 line gains ONLY a pointer breadcrumb
   ("(escape …: see stage-1 detail)") — the breadcrumb points, it does not state a second
   rule, so no absolute statement of the excepted rule remains anywhere and diagram/detail
   cannot contradict. Gate-before-present unaffected (hypotheses stay `ungated`); the
   representativeness gate still binds. The detail's exception sentence explicitly says
   "exception to the ordering above, recorded."
5. **D-13/D-14 vs stage-7 "all three, conjunctively"** — both are ADDITIONAL requirements on
   "found" (the bar becomes: three items + depth check recorded + coverage sweep recorded);
   nothing loosened; the "two-of-three is not found" sentence survives verbatim.
6. **D-4 vs the instrument-to-capture bar** — the fire-on-known-true half IS the same
   known-occurrence discipline the intermittent path already carries, now named for
   detectors/readouts generally. The **silent-on-known-clean half is NEW and intended** —
   a strictly stronger requirement (adds, loosens nothing), so no contradiction, but the
   builder must know it is a deliberate delta, not a restatement. Boundary (must appear in
   the built text): anything that *decides* symptom-present/absent (classifier, grep,
   threshold rule) is a detector and carries both halves; an instrument that merely
   captures data for later reading keeps the existing fire-on-known-occurrence bar only.
7. **D-1/D-9 vs lite's "drops the surrounding scaffolding"** — the provenance record is not
   scaffolding; the lite definition keeps charter + provenance record, drops
   spec/criteria/plan/baseline/regression only (the source's full five-item enumeration).
   The lite paragraph's wording must say so explicitly.
8. **D-10's relabel vs "This skill can be run on its own artifacts"** — the rewrite retains
   the stage-3-style red-team obligation (strengthened: full loop for non-trivial edits);
   the flagship-test description survives, honestly labeled.
9. **D-11's scoped exemption vs the imported guarded-change coverage-challenge duty** — the
   exemption names ONLY dragonfly's direct stage-7 passes and lite passes (neither is a
   stage-3 review, so guarded-change's "for stage-3 reviews" bullet never bound them;
   D-12 is dragonfly's analog duty). Full-GC triage runs are affirmatively carved OUT of
   the exemption: the built sentence states they keep ALL of guarded-change's own stage
   duties including its stage-3 coverage challenge, so no reader can construe dragonfly's
   charter as narrowing a full-GC run. No contradiction with the imported rule remains.

## Insertion order (position lens — part of the edit spec, not a build detail)

Multi-block clusters land in a specified order; the section's **terminal text** is chosen,
not incidental:

- **Stage-7 detail (heaviest: D-5 + D-13 + D-14, with D-2's block after the section):**
  D-5's clause extends the toggle item in place; then D-13's depth block, then D-14's sweep
  block. **The cluster's closing lines re-anchor the full bar**: "…only with the depth
  check and the coverage sweep recorded is 'found' declarable — all three bar items plus
  both records **plus the chain's cold-red-team pass (gate marker `cold-red-teamed`)**,
  conjunctively." (The cold-pass paragraph currently terminal at :185-188 is displaced
  mid-section by the new blocks; its duty + gate-marker consequence therefore ride in the
  re-anchor so the section's last words still carry them.) The last thing read at stage 7
  is the bar, not a sub-procedure. D-2's block is a separate section-level insert between
  stage 7 and stage 8, framed as a distinct verdict (never inside the "found" bar).
- **Stage-6 detail (D-3 + D-7 + D-12):** insert after the existing cap sentences, keeping
  the refuse-to-start rule attached to its cap sentence; the terminal punch line **stays
  the section's last line**, with its referent re-bound in a **named micro-rewrite**
  ("This is the defense…" → "**The cap is** the defense against token-burning thrash…")
  since new text now separates it from its antecedent — obligation identical.
- **Charter section (D-1 + D-11 + D-12's aim):** D-12's aim appends as the aiming list's
  **last item** (the list enumerates aims, it is not a priority order); D-1/D-11's
  sentences land before the closing discipline paragraph (spot-verify/severity), which
  **remains the section's terminal text**.
- **Stage-9 detail (D-2's exception clause + D-5's window sentence + D-14's residual
  re-check):** each lands inside the sub-item it governs (D-2's clause at the headline,
  D-5's in 9a/9b's window context, D-14's with the re-check duty); the terminal routing
  rule ("A failed verification is never discarded…", :212-213) **stays the section's last
  text** — nothing inserts after it.
- **Stop-for-human inventories (METHODOLOGY "Human-in-the-loop" + SKILL "Stop-for-human
  rules"):** the two new items land **inside the existing stop list / stop sentence**;
  the gate-before-present paragraphs that close both sections (:437-441 / SKILL :118-121)
  **remain terminal** — nothing inserts after them.
- **Stage-1 detail (D-8):** the exception lands after the ordering rule it excepts
  (general rule first, named exception second). Diagram breadcrumb per the mapping row.
- **SKILL:** inline clauses preserve each step's existing sentence order; the D-10
  self-check rewrite stays the file's final section.

## Measurement

- **C1/C2** — inspection-by-location against this table + the sweep (stage 8, quoted text
  + file:line per row). **C1 is read strictly AGAINST C4:** cap pressure never trades away
  mapped substance — if a row's substance and the cap cannot both hold, bounce to the plan
  rather than compress.
- **C3** — mechanical grep of each named cross-reference against guarded-change source at
  `9cec23d` (charter section title, provenance bullet, severity model, probabilistic rubric
  ["states the pass rate it expects"], lite charter reference), quoted both sides.
- **C4** — `wc -l` (caps 515/148/655; baselines 441/129/570).
- **C5** — `diff` live vs source after install.
- **C6** — `git diff 9cec23d` hunk-walk; expected deletion classes: in-place sentence
  extensions (triage enumeration "+ detector/readout"; step/paragraph tails); the
  loop-diagram :91 line extension (a code-block line gaining the breadcrumb); the
  `diagnosis.md` artifact-line extension (a code-block listing line extended by
  D-2/D-13/D-14); the named rewrite (D-10 self-check, obligation verbatim-or-stronger);
  and the named micro-rewrite (stage-6 punch-line referent re-bind "This is" → "The cap
  is", obligation identical). Any deletion-shaped hunk outside these classes = C6 fail.
- **C7** — final report (9-report.md — a run-specific artifact this run PRODUCES at
  stage 8; it is not in either skill's artifact canon): D-S1..S3, the (narrowed)
  no-battery residual, the D-10 aspirational label, attention spend. **Gating** (a
  report-content criterion — inspection of the report for each required item is cheap and
  unambiguous).
- **C8 (retrodiction — the executed behavioral check; owner-adopted by tie-break
  2026-07-04, formal entry at gate 4)** — token-free replay of the new rules against the
  recorded hunt, executed at stage 8, output recorded with hunt-record citations in a
  dedicated **8-retrodiction.md** (pointed to from 8-harness.md). **Evidence set (pinned):**
  `hunts/monologue-bleed-memory-gap/{decisions, hypotheses, CONTEXT-BLOAT-HUNT,
  observation-ledger, symptom-ledger}.md` — the two ledgers included because D-14's sweep
  and D-3's laps are defined over them; the hunt is LIVE, so the five files are **copied
  into `fixtures/hunt-record/` with sha256s recorded at the gate-4 freeze** and C8 runs
  against the pinned copies only. **Sub-check selection rule:** rules with fully-recorded
  fixtures in the pinned set only (D-3, D-14, D-2, D-8, D-12); D-13's precedent is user
  testimony, not in-record → no sub-check, by rule not by omission. Five sub-checks with
  **pre-registered expected outcomes**:
  (i) **D-3** — cycle count computed from the pinned record against this pre-registered
  candidate-lap inventory: **S2 = the O16 replay-search and O17 toggle runs (hunt
  decisions.md:24-36) — adjudicated as 1 or 2 laps under D-3's built definition, the
  choice stated and justified; S1 = 0 completed stage-4→5 laps** (its only designed
  discriminating test never ran — "Awaiting user go/no-go", hunt decisions.md:96). Any
  lap counted outside this inventory, or any S1 count ≠ 0, = fail;
  (ii) **D-14** — the coverage sweep **anchored at the moment S1-O15 was recorded**
  (hunt decisions.md:76-78), judged against the then-live leading account (the
  0.0.38-shaped story; audit precedent 0-audit-findings.md:144-147) — expected: the sweep
  classifies S1-O15 as unexplained-by-the-then-account → demands a residual entry the
  record lacks. (Not judged against the final H-S1-WRITELOAD-DOSE state, which subsumes
  it, nor against "no confirmed chain", which would pass vacuously.);
  (iii) **D-2** — the characterized-verdict checklist matched against the recorded S1
  ending (hunt decisions.md:68-74) names **≥1 element of (a)–(e)** the ad-hoc ending
  lacked (candidate: (d) — no recorded human sign-off);
  (iv) **D-8** — the escape's conditions adjudicated against the recorded inversion (the
  ordering across hunt decisions.md:41-86 vs :87-96): names the infeasibility class with
  a citation and states whether the required inversion entry exists (expected: substance
  present, formal entry absent — the rule would have demanded one);
  (v) **D-12** — the class-coverage/shared-assumption record retrodicted at the recorded
  convergence point after the second S1 code-hypothesis refutation (hunt
  decisions.md:64-65; hypotheses.md:65-66) — expected: the rule, applied there, names the
  live set's shared architectural assumption (the Python tool-loop mattering on the
  claude-cli path) — non-vacuous exactly where the recorded hunt was class-blind.
  A sub-check that cannot produce its expected outcome = C8 fails (the rule as built is
  vacuous or wrong). **8-retrodiction.md receives one guarded-change-lite cold pass
  (triage class 3 — a single self-contained document) before C8 is scored** — the run's
  only executed behavioral evidence is not self-certified.

## Loop from here (canonical stage order)

- **Stage 3 (round 2 — after the round-1 MAJOR bounce)** — fresh cold review of the
  REVISED {spec, criteria, plan} — full F1 provenance record (`3-redteam-plan-round2.md`
  verbatim), same charter core + coverage challenge + position lens + task additions;
  closed set = round 1's set PLUS `3-redteam-plan.md` (the round-1 record) and this run's
  `decisions.md` (the gate-4 worklist), with the added task: verify each round-1
  major/minor is resolved in the revision (nitpicks: resolved-or-logged).
- **Gate 4** — reviewer's severities; criteria FREEZE with sha256 + verbatim copy at
  route-to-build; record the owner decision (M-1 adopted as C8 + the narrow named
  risk-acceptance, owner-attributed).
- **Stage 5 (build order within the stage)** — edit METHODOLOGY.md per mapping first
  (source only), then SKILL.md (pointer-style clauses referencing the landed METHODOLOGY
  sections).
- **Stage 6** — cold review of the mechanical diff (`git diff 9cec23d`, command recorded;
  verbatim record, same provenance duties). **Gate 7.**
- **Stage 8** — C1–C7 per Measurement, install → C5, 8-harness.md with evidence column,
  criteria-freeze verify, gate → commit+push (one commit).

Thresholds: findings route by the reviewer's stated severity (guarded-change F5); iteration
cap: 2 bounces same gate + same finding class → human tie-break.
