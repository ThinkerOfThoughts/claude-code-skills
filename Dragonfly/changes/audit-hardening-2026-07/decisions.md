# decisions.md — gate log (append-only): dragonfly audit-hardening-2026-07

## Run start — 2026-07-03
- **Loop:** the HARDENED guarded-change (skills repo `main` = `9cec23d`, F1–F9 live) —
  this run dogfoods the new rules end-to-end.
- **Path validation (F8) recorded — 13/13 OK, 0 dead** (mechanical `-r` check, this
  session): Dragonfly source {METHODOLOGY.md 441, SKILL.md 129, dragonfly.companion.md,
  README.md}; `0-audit-findings.md`; live `~/.claude/skills/dragonfly/{METHODOLOGY,SKILL}.md`;
  guarded-change source {METHODOLOGY.md 534, SKILL.md 124} (cross-reference target, D-11);
  hunt evidence `~/Desktop/companion-emergence/hunts/monologue-bleed-memory-gap/{decisions.md,
  hypotheses.md, CONTEXT-BLOAT-HUNT.md}`; `changes/gate-before-present/` (prior self-change
  record).
- **Stage-0 baseline:** docs-only change; no metric baseline → stage 8 conformance-only.
  Pre-change state recorded: live == source, both files identical (`diff` empty); base for
  the mechanical stage-6/8 diff = `9cec23d`.
- **Owner constraints (carried from the task):** additive fixes only — D-S1..S3 flagged,
  NOT built; executing model is Opus → rules explicit/mechanical/checkable; don't bloat;
  commit+push on pass.

## Stage 4 gate (plan red-team, round 1) — 2026-07-03
- **Worst severity: MAJOR (reviewer's severity; routed as stated).** Counts: 1 major (L-1),
  10 minor (F-1, F-2, L-2, L-3, L-4, POS-1, M-1, M-2, U-2 + the label-audit's C7 call
  folded into L-4), 8 nitpick (L-5..L-8, M-3, M-4, U-4, U-5). Fresh cold reviewer
  (`general-purpose`/`claude-fable-5`); verbatim record with full provenance:
  `3-redteam-plan.md`. Reviewer verified all 14 mapping locations exist, all audit claims
  against the hunt record, C3's cross-ref list complete, and the `9cec23d` baseline.
- **Route: MAJOR → return to plan (stage 2).** Criteria NOT frozen (freeze binds only at
  route-to-build; criteria edits from F-1/L-4 are legal pre-freeze). Revision to fold, next
  session: **L-1** scope the D-11 exemption (direct stage-7 + lite passes only; full-GC
  triage runs keep ALL of guarded-change's own stage duties incl. its stage-3 coverage
  challenge) + add sweep item 9 + widen C2's contradiction scope to imported GC rules;
  **F-1** align C2's enumerated sweep items with the plan's list; **F-2** restate sweep
  item 6 honestly (silent-on-clean half is NEW and intended; define the
  instrument-vs-detector boundary); **L-2** D-2 gets a stage-9 mapping location (one
  clause); **L-3** add METHODOLOGY "Human-in-the-loop" + SKILL "Stop-for-human rules" rows
  to the mapping (D-2 sign-off; D-6 dead-path/invalid-config); **L-4** C7 → GATING + queue
  the owner-attributed named risk-acceptance for the unexecuted position-behavior check
  (OWNER DECISION at next gate 4 — alternative: adopt M-1 as a new criterion, which
  shrinks what needs accepting); **POS-1** add intra-section insertion-order notes per
  cluster (D-13/D-14 close by re-anchoring the three-part bar; stage-6 keeps its terminal
  punch line last); **M-1** add the token-free retrodiction check against the recorded hunt
  to Measurement (candidate new gating criterion); **M-2** decide diagram breadcrumb (one
  parenthetical at :91) or record why frozen; **U-2** note the SKILL cap pressure rule
  (C1 substance is read strictly AGAINST C4 — never trade substance for the cap).
  Nitpicks: log-only unless free during the touch (L-6 define "unconditional bullets";
  L-7 record the inspection-counts-as-execution note in decisions.md — done here: for
  text-presence criteria, locating + quoting the governed text IS executing the check,
  same reading the sibling run recorded; L-8 enforcement-shape D-12's consequence + thread
  attribution phrase; M-3 characterized-handoff diagnosis.md contents; M-4 note the
  restatement-vs-reference choice; U-4 "the mapping table is the build oracle" line;
  U-5 pointer-tolerant record location).
- **PAUSED here by the owner (bedtime / usage 75%), 2026-07-03 night.** Next on resume:
  revise 2-plan.md + 1.5-criteria.md per the above → fresh stage-3 cold review (round 2)
  → gate 4 (owner tie-break queued: L-4 risk-acceptance OR M-1-as-criterion) → build.

## Stage 2 revision (post-bounce) — 2026-07-04
- **Owner tie-break RESOLVED (asked + answered this session, owner = ThinkerOfThoughts):
  adopt M-1 as gating criterion C8** (token-free retrodiction of the new rules against
  the recorded hunt, four sub-checks with pre-registered expected outcomes) **+ the narrow
  named risk-acceptance** for what C8 cannot observe (dilution of pre-existing duties under
  the added text — bounded by inspection C6/C2/insertion-order notes, not executed). The
  formal risk-acceptance entry is recorded at gate 4 on route-to-build, owner-attributed.
- **2-plan.md revised:** L-1 → D-11 row rewritten (exemption scoped to direct stage-7 +
  lite passes; full-GC triage runs affirmatively keep ALL guarded-change stage duties incl.
  its stage-3 coverage challenge) + new sweep item 9; F-2 → sweep item 6 restated
  (silent-on-clean = NEW + intended; detector-vs-instrument boundary defined, boundary also
  added to the D-4 row substance); L-2/M-3 → D-2 row gains stage-9-detail + SKILL-step-9 +
  diagnosis.md-contents locations; L-3 → new mapping row "D-2/D-6 stop-point wiring" (both
  stop-for-human inventories); POS-1 → new "Insertion order (position lens)" subsection
  (stage-7 cluster closes by re-anchoring the three-part bar; stage-6 punch line stays
  terminal; charter discipline paragraph stays terminal); M-1 → C8 added to Measurement;
  M-2 → diagram breadcrumb ADOPTED (D-8 row + sweep item 4 updated — pointer only, no rule
  text in the diagram); U-4 → "the mapping table is the build oracle" line; U-5 → D-1
  record-location made pointer-tolerant; L-6 → "unconditional" defined in the D-11 row;
  L-8 → D-12 consequence enforcement-shaped + D-7 thread-attribution phrase; M-4 →
  restatement-vs-reference note added to the plan intro. Coverage-gap #2 cheap partial
  also folded: D-8's inversion record must name the infeasibility class. L-5 stays
  log-only (residual churn covered by the re-examination prong + gate cap).
- **1.5-criteria.md revised:** F-1 → C2's sweep list now enumerates the plan's items 1–9
  verbatim-aligned; L-1 → C2 contradiction scope widened to imported guarded-change rules;
  L-4 → C7 relabeled GATING with the label reason; C8 added (gating, executed); U-2 →
  C1-read-against-C4 rule in the C4 row; position note rewritten (C8 = the executed
  evidence; narrow residual named). Caps unchanged (515/148/655) — the C1-vs-C4 bounce
  rule is the guard against substance compression.
- Criteria remain UNFROZEN (pre-route). Next: stage-3 cold review round 2 (closed set =
  round 1's + 3-redteam-plan.md + this decisions.md; added task: verify each round-1
  major/minor resolved) → gate 4.

## Stage 4 gate (plan red-team, round 2) — 2026-07-04
- **Worst severity: MINOR (reviewer's severity; routed as stated) → fix in place,
  PROCEED TO BUILD.** Counts: 11 minor (R2-L-1..L-4, R2-U-1..U-3, R2-F-1, R2-P-1, R2-P-2,
  R2-M-1), 7 nitpick (R2-F-2..F-4, R2-M-2, R2-U-4, R2-U-5, R2-P-3). Fresh cold reviewer
  (`general-purpose`/`claude-fable-5`, not the round-1 agent); verbatim record with full
  provenance: `3-redteam-plan-round2.md`. **Resolution check: all round-1 majors+minors
  verified RESOLVED, all nitpicks folded/logged exactly as claimed — no re-raises.**
- **Fix-in-place applied before this entry (all pre-freeze, per the route):** R2-F-1 D-2
  consequence "missing ANY of (a)–(e)"; R2-L-1 stop-point row split (dead/unresolvable =
  stop; invalid-but-adaptable = adapt+record+proceed, surfaced not blocking); R2-P-1
  stage-7 re-anchor now carries the chain's cold pass + gate-marker consequence; R2-P-2
  insertion-order notes added for the stage-9 cluster + both stop-for-human inventories
  (terminal texts stay terminal); R2-P-3 stage-6 punch-line referent re-bind = a second
  NAMED micro-rewrite ("This is"→"The cap is") + D-12's aim = aiming list's last item;
  R2-L-2 C8(i) candidate-lap inventory pre-registered (S2 = O16/O17, 1-or-2 justified;
  S1 = 0); R2-L-3 C8(ii) anchored at S1-O15's recording moment vs the then-live account;
  R2-L-4 evidence set + both ledgers; R2-M-1 fifth sub-check (v) D-12 + the selection
  rule (recorded-fixture rules only; D-13 excluded by rule); R2-M-2 8-retrodiction.md
  gets a guarded-change-lite cold pass before C8 is scored; R2-F-2 lite five-item drop
  list; R2-F-3 C6 expected-hunk classes + the two new shapes + the micro-rewrite; R2-F-4
  S1-O15 cite :76-78; R2-U-4 "owner-adopted (tie-break 2026-07-04; formal entry at
  gate 4)"; R2-U-5 9-report.md marked run-produced.
- **C4 cap decision (R2-U-3, author decision under the owner's don't-bloat constraint,
  recorded as the reviewer required):** caps RAISED pre-freeze 515/148/655 →
  **525/152/670** — covers the round-2 upper estimate (~521/150/670) instead of building
  in a foreseeable C1-vs-C4 bounce; growth still bounded ≤ +18% combined; the
  bounce-not-compress rule stays as the relief valve. Surfaced in the C7 report.
- **OWNER RISK-ACCEPTANCE (route-(b), named, recorded at route-to-build):** the owner
  (ThinkerOfThoughts; tie-break decision given in-session 2026-07-04 via direct question,
  option "Adopt M-1 + narrow acceptance") accepts as KNOWN UNVERIFIED RISK the three
  residual classes C8 cannot observe (scope per R2-U-2, not "dilution only"):
  (a) dilution of Opus's execution of PRE-EXISTING duties under the added text — bounded
  by inspection only (C6 + C2 + insertion-order notes); (b) live UNPROMPTED firing of the
  new rules by an Opus executing the amended prompt — C8 executes the rules' adjudication
  logic by hand, it does not measure prompt-compliance; (c) vacuousness of the rules C8
  does not sample (D-1, D-4, D-5, D-6, D-7, D-9, D-10, D-11, D-13). Rationale: the
  sibling run just measured this amendment class at 13 arms' cost; dragonfly's amendments
  govern hunt conduct with no cheap synthetic-record analog; C8 + inspection is the
  best available evidence short of a battery, and the residuals are named for the next
  run rather than hidden.
- **C8 FIXTURE PINNED at this gate (R2-U-1):** five hunt files copied to
  `fixtures/hunt-record/`; sha256:
  `46ae8d4f…6cb98f` CONTEXT-BLOAT-HUNT.md, `a4c2adda…23606a` decisions.md,
  `fcfcd687…0586bc` hypotheses.md, `6459716b…727925` observation-ledger.md,
  `2d9d16ff…8e41c6` symptom-ledger.md. The three the round-2 reviewer hashed match its
  reported values — the pinned fixture is byte-identical to what the reviewer adjudicated.
  C8 runs against these copies only.
- **CRITERIA FREEZE (F4) at route-to-build:** 1.5-criteria.md sha256 =
  `0ba8cfc59f3fd0b63f3b0e5b0e1f282ee87b206d6ff8bc20b3c4591cbc00e130` (38 lines);
  2-plan.md (the build oracle) sha256 =
  `15ab47d6c5dfb526323a043a0e068f51ede2f6d130fb037f0d673b3c563ce523` (201 lines).
  Verbatim frozen copy of the criteria follows:

```markdown-frozen-criteria
# 1.5 — Criteria: dragonfly audit-hardening-2026-07

Position-sensitivity note (the lens fires): SKILL.md + METHODOLOGY.md are prompt-like
documents — a position-sensitive assembly. The change **adds** rules (never moves/removes),
so the hazard is displacement/dilution of neighboring rules. This run's **executed**
behavioral evidence is **C8** (owner-adopted by tie-break 2026-07-04; formal entry at
gate 4): a token-free retrodiction that executes the new rules' **adjudication logic**
against a pinned real-hunt record, with pre-registered expected outcomes — it proves the
sampled rules are computable and non-vacuous on real data. What C8 canNOT observe (all
three named in the gate-4 risk-acceptance): (a) whether the added text **dilutes Opus's
execution of pre-existing duties** — bounded by inspection only (C6 pure-additive walk +
C2 neighbor-text checks + the plan's insertion-order notes); (b) **live, unprompted
firing of the new rules** by an Opus executing the amended prompt (C8 is the author
applying the rules' logic deliberately, not prompt-compliance); (c) **vacuousness of the
rules C8 does not sample** (D-1, D-4, D-5, D-6, D-7, D-9, D-10, D-11, D-13 — e.g. D-5's
ledger-frequency window meeting a ledger with no frequency data). **No replay A/B battery
is run for dragonfly** — a deliberate, owner-visible scope decision (C7 carries it as a
named residual, with the rationale: the sibling guarded-change run just measured this
amendment class's behavioral effect at 13 arms' cost, and dragonfly's amendments govern
hunt conduct, which has no cheap synthetic-record analog). Concurrency lens: does not
fire (prose edits, single actor).

| # | Criterion | Gating? | How verified (stage 8) |
|---|---|---|---|
| **C1** | Every finding D-1..D-14 has its fix present in **every load-bearing location** named in the plan's mapping table, with the row's full substance (trigger + requirement + **consequence**) | gating | Inspection-by-location: locate exact text per mapping row; quote it + file:line evidence pointer |
| **C2** | **Cross-file + intra-file consistency:** every rule stated in both files agrees on trigger/requirement/consequence; no new rule contradicts an existing dragonfly rule **or an imported guarded-change rule**; the plan's contradiction-sweep items **1–9** — (1) D-2 vs the gate-before-present tiers + stage 9, (2) D-3's cycle unit vs D-7's per-thread counts, (3) D-5 vs the borrowed probabilistic rubric, (4) D-8's escape vs the stage-1 ordering + the loop diagram, (5) D-13/D-14 vs the stage-7 conjunctive "found" bar, (6) D-4 vs the instrument-to-capture bar (silent-on-clean half = new + boundary stated), (7) D-1/D-9 vs the lite scaffolding-drop, (8) D-10's relabel vs the self-run sentence, (9) D-11's scoped exemption vs the imported coverage-challenge duty — each explicitly reconciled with quoted text | gating | Inspection: side-by-side per sweep item, quoted text + file:line |
| **C3** | **Cross-reference resolution (D-11 operationalized for this run):** every by-reference import from guarded-change named in the amended text (charter core + discipline bullets incl. provenance, severity model, probabilistic rubric, lite definition) resolves against guarded-change at `9cec23d` — the referenced section exists and says what the dragonfly text assumes | gating | Mechanical+inspection: grep the referenced anchor in guarded-change source; quote both sides |
| **C4** | **Bloat caps (absolute, all three must hold):** METHODOLOGY ≤ 525 lines, SKILL ≤ 152 lines, combined ≤ 670 (baselines 441/129/570 at `9cec23d`). *Caps raised pre-freeze from 515/148/655 per the round-2 re-estimate (R2-U-3: mapped substance grew to ~60-80/13-21 lines vs +74/+19 headroom — a foreseeable bounce was built in); the raise covers the estimate's upper range while still bounding growth ≤ +18%.* **C1 is read strictly AGAINST C4:** cap pressure never trades away mapped substance — if a row's substance and a cap cannot both hold, bounce to the plan rather than compress | gating | Mechanical: `wc -l` before/after, command output in 8-harness.md |
| **C5** | **Live == source** for both files after the stage-8 install | gating | Mechanical: `diff` per file, empty output quoted |
| **C6** | **Pure-additive:** `git diff 9cec23d` shows no existing rule deleted or weakened; deletion-shaped hunks only where an original sentence is re-emitted verbatim with an in-place extension (or an explicitly named rewrite whose obligation survives verbatim-or-stronger), each justified hunk-by-hunk | gating | Mechanical+inspection: `git diff` reviewed hunk-by-hunk in 8-harness.md |
| **C7** | D-S1..S3 remain unbuilt; final report carries: D-S1..S3 for owner decision, the **no-battery residual** (named, with rationale and what evidence exists instead — now narrowed by C8), the D-10 flagship-test relabel (aspirational until first run — not run by this change), and the attention-budget spend | **gating** (a report-content criterion: inspection of the report for each required item is cheap and unambiguous; non-blocking would let the run's honesty obligations silently vanish from the report) | Inspection of the final report: each required content item located + quoted |
| **C8** | **Retrodiction (the executed behavioral check; owner-adopted by tie-break 2026-07-04, formal entry at gate 4):** the new rules replayed token-free against the **pinned** hunt record (five files copied to `fixtures/hunt-record/` at the gate-4 freeze, sha256s recorded — the live hunt cannot flip the outcomes): `{decisions, hypotheses, CONTEXT-BLOAT-HUNT, observation-ledger, symptom-ledger}.md`. Sub-check selection rule: rules with fully-recorded fixtures only (D-13's precedent is user testimony → no sub-check, by rule). Five sub-checks, pre-registered expected outcomes: (i) D-3 cycle count vs the pre-registered candidate-lap inventory — **S2 = the O16/O17 replay+toggle runs (hunt decisions.md:24-36), adjudicated 1-or-2 laps with the choice justified; S1 = 0** (designed test never ran, :96); any lap outside the inventory or S1 ≠ 0 = fail; (ii) D-14 sweep **anchored at the moment S1-O15 was recorded** (hunt decisions.md:76-78), judged against the then-live leading account (audit precedent 0-audit-findings.md:144-147) — flags S1-O15 as unexplained → demands a residual entry the record lacks; (iii) D-2 checklist vs the recorded S1 ending (hunt decisions.md:68-74) names ≥1 missing element of (a)–(e) (candidate: (d), no recorded sign-off); (iv) D-8 escape vs the recorded inversion (the ordering across hunt decisions.md:41-86 vs :87-96) — infeasibility class named with citation + verdict on the required record entry (expected: substance present, formal entry absent); (v) D-12 record retrodicted at the post-second-refutation convergence point (hunt decisions.md:64-65; hypotheses.md:65-66) — names the live set's shared architectural assumption. Any sub-check unable to produce its expected outcome = fail (the rule as built is vacuous or wrong) | gating | Executed at stage 8: replay output with pinned-record citations in a dedicated 8-retrodiction.md (pointed to from 8-harness.md), which receives **one guarded-change-lite cold pass before C8 is scored** (no self-certification) |

Freeze note (F4): these criteria freeze when gate 4 routes to build; sha256 + verbatim copy
recorded in decisions.md at the gate. **The C8 fixture freezes with them:** the five hunt
files are copied to `fixtures/hunt-record/` and their sha256s recorded in the same gate
entry — C8 runs against the pinned copies only (the live hunt cannot flip the
pre-registered outcomes).
```

- Route: **BUILD (stage 5)** — METHODOLOGY.md per the mapping table + insertion-order
  subsection first, then SKILL.md (pointer-style). Then stage 6 (mechanical diff vs
  `9cec23d`, cold review) → gate 7 → stage 8 (C1–C8 + install + freeze verify) →
  commit+push.

## Stage 7 gate (build red-team) — 2026-07-04
- **Worst severity: MINOR (reviewer's severity; routed as stated) → fix in place, PROCEED
  TO STAGE 8.** Counts: 3 minor (D-11 trigger narrowed; "for the fix" deletion outside C6
  classes; SKILL step-8 semicolon misparse), 5 nitpick. Fresh cold reviewer
  (`general-purpose`/`claude-fable-5`); verbatim record with full provenance:
  `6-redteam-build.md`. Reviewer regenerated the diff (byte-identical to the saved copy),
  independently confirmed the criteria/plan freeze hashes intact, verified all 20 hunks
  against the 15 mapping rows, all 9 sweep items on the BUILT text, every C3 cross-ref
  against GC at `9cec23d` (quoted both sides), and the full insertion-order spec.
  **Every author compression adjudicated: substance-safe except the 3 findings.**
- **Fix-in-place applied (net-zero lines, verified 521/149/670 after):** Finding 2 →
  restored "Hand to **guarded-change** for the fix." (hunk back inside the ext class);
  Finding 3 → SKILL step-8 reordered — the `diagnosis.md` depth-status/residuals clause
  now attaches to the handoff sentence, the characterized sentence stands alone (the
  misparse channel is gone; "explicit human sign-off" compressed to "**human sign-off**"
  in the SKILL pointer for width — the (d) requirement's full "explicit human sign-off"
  wording lives at METHODOLOGY's D-2 block; noted for the C2 record); Finding 1 → the
  self-check trigger now reads "Standing criteria after any edit to these files **or to
  guarded-change**" (the GC-side drift channel is back in the built text; freed the line
  inside the self-check section itself rather than the reviewer's suggested stop-list
  repack — same net-zero effect) + nitpick 5 folded ("every shared rule").
- **Post-fix state:** `wc -l` = 521/149/670 (caps 525/152/670 — all hold, combined at cap);
  regenerated `6-build.diff` sha256 `8902d663…0871b3`; built METHODOLOGY `04d1044c…26f065`,
  SKILL `b5e122ef…9a2527`.
- **Carried to stage 8:** cite the FROZEN CRITERIA (not the plan's stale Measurement line)
  for the C4 caps (nitpick 4); record the "terminal verdict = claims-carrying ending"
  scoping reading in the C2 record (nitpick 7); record the vacuous-import note on GC
  label-audit bullets (consistency nitpick); the commit is PATH-SCOPED to `Dragonfly/`
  (nitpick 8 — `Guarded_change/guarded-change.companion.md` working-tree modification must
  not ride).
- Route: **STAGE 8** — C8 retrodiction (pinned fixture) + lite cold pass on its record →
  C1–C7 per Measurement → install → freeze verify → commit+push.

## Stage 8 IN PROGRESS — PAUSED by the owner (usage 94%), 2026-07-04
- **Done this session before the pause:** C8 retrodiction executed round 1
  (8-retrodiction.md) → **round-1 lite cold pass = MAJOR** (sub-check (i) rested on "S1
  test never ran" — refuted by pinned observation-ledger rows S1-O18/S1-O21, never
  adjudicated; author had walked only the gate log, not the ledger stage 5 records runs
  in; + 3 minor evidence defects in (ii)/(iv)/(v)). **8-retrodiction.md REVISED in place
  (round 2, this session):** (i) re-executed on the full pinned record — S1-O18 (anchor
  FAILED, gate-rejected qualification run) and S1-O21 (latency repro, bleed anchor still
  unmet, no status consumed it) explicitly adjudicated NON-laps; S1 = 0 completed laps
  EARNED; frozen parenthetical scope-corrected (designed protocol never ran; its smoke
  precursors did); new residual for the C7 report (token-burning gate-rejected runs are
  invisible to the cycle counter alone — re-examination prong + harness GC cover them);
  (ii) grep claim corrected (hypotheses.md:167 / observation-ledger.md:212 — neither
  D-14-shaped); (iv) the tier-discipline aside corrected (decisions.md:53 recorded
  violation acknowledged — strengthens D-8's non-vacuousness); (v) "in so many words" →
  derivation grounded at observation-ledger.md:292-294; unsupported "one refutation
  earlier" counterfactual dropped; no-lap tension flagged. C8 remains UNSCORED (scoring
  waits for the round-2 lite pass, per the frozen criterion).
- **⚠️ Round-1 lite-pass verbatim record NOT yet persisted** (pause hit first): the full
  verdict + provenance (reviewer `general-purpose`/`claude-fable-5`; 9 reported sha256s;
  8-retrodiction.md round-1 hash `17d87d5d…a2e8c5`) lives verbatim in this session's
  transcript (session 723b134a…, task adb0737a…). **FIRST RESUME ACTION: write
  `8-retrodiction-litepass.md` from it** (the revised 8-retrodiction.md header already
  points to that filename), THEN spawn the round-2 lite pass (closed set = round 1's +
  the round-1 record; task: resolution check of the MAJOR + 3 minors + fresh pass).
- **Mechanical stage-8 evidence already banked this session (for 8-harness.md):**
  C4 = 521/149/670 vs frozen caps 525/152/670 ✓ (cite the CRITERIA file, not the plan's
  stale line); C5 = installed to live `~/.claude/skills/dragonfly/`, both diffs empty ✓;
  freeze verify = criteria `0ba8cfc5…`, plan `15ab47d6…`, all 5 fixture hashes unchanged ✓;
  C6 = all 24 deletion-shaped lines in the final 6-build.diff (`8902d663…`) classify into
  the 5 expected classes ✓; C3 greps = GC:204 charter / GC:238-240 provenance elements /
  GC:151 pass-rate + :163 rubric name / GC:243+251 coverage-challenge scoping ✓; C1/C2
  anchor line numbers pulled (METHODOLOGY :92,142,182,192,201,207,213,218,221,230,234,
  253,256,281,326,346,385-386,388-399,456,472,512,515; SKILL :19-20,46,68,74-75,78,88,
  96-100,109,120-123,129-131,142-146).
- **REMAINING on resume (in order):** (1) write the round-1 litepass record; (2) round-2
  lite pass → score C8; (3) write 8-harness.md (C1 15-row walk + C2 sweep record incl.
  the two carried notes [verdict-scoping reading; vacuous GC label-audit import] + C3-C6
  evidence above + C8); (4) 9-report.md (C7: D-S1..S3 owner decisions, narrowed no-battery
  residual + the 3 named risk-acceptance classes, D-10 aspirational label, cap raise,
  cycle-counter residual from the retrodiction, attention spend); (5) final gate entry;
  (6) commit PATH-SCOPED to Dragonfly/ + push (SSH, sandbox off; exclude
  Guarded_change/guarded-change.companion.md).
- Live copies currently = built source (installed pre-gate; a hard stage-8 bounce reverts
  live to the `9cec23d` copies — revert path unchanged).

## Stage 8 RESUMED — C8 scored (2026-07-04, post-pause)
- **Round-1 lite-pass record persisted:** `8-retrodiction-litepass.md` (recovered verbatim
  from the session transcript per the pause entry — charter + reviewer output unedited;
  transport note in the file header). Reviewed round-1 hash `17d87d5d…a2e8c5` (stale by
  design — the file was revised in response).
- **Round-2 lite cold pass (D-9 record):** artifact = the REVISED `8-retrodiction.md`
  (hash at review `66f9173c…beca2b`); intent/criterion = same as round 1 (five
  pre-registered sub-checks genuinely met, citations resolve, no out-of-fixture evidence)
  + resolution check of all 7 round-1 findings; reviewer `general-purpose`/
  `claude-fable-5`, cold, closed set = round 1's + the round-1 record; verbatim output +
  provenance: `8-retrodiction-litepass-round2.md`. **Verdict: worst severity MINOR — "the
  C8 PASS claim survives"; 7/7 round-1 findings genuinely resolved ("MAJOR earned, not
  reworded around"); (i)–(iv) PASS earned, (v) PASS in substance with one unflagged
  frozen-wording label mismatch (live set vs refuted pair — inherited from C8's frozen
  text, whose own precedent citation points at the refuted pair).**
- **Route (severity model): MINOR → fix in place, proceed. C8 = PASS (scored).** Fixes
  applied to 8-retrodiction.md after the review (final hash `85b7391f…9d56be`): the (v)
  outcome check now flags the frozen-wording mismatch explicitly (names the assumption
  under the precedent's label, notes the live-set line would read "none identified" per
  METHODOLOGY:189-190) — flagged, not silently relabeled; + 5 nitpicks (criterial premise
  now cites METHODOLOGY:165-166/172-176/263-268; frozen parenthetical quoted verbatim and
  separated from the decisions.md splice; lap-inventory sweep now states the first-hand
  five-file run-marker grep [2 hits: observation-ledger.md:360, :413]; "comparable session
  lengths" marked as replay inference, not S1-O15 text; quote range :60-61 → :59-60).
- **Fixture pins re-verified at execution AND independently by both lite reviewers** (all
  5 sha256s match the gate-4 freeze; round-2 reviewer cross-checked round-1's reported
  hashes — pinned record unchanged between rounds).
- Remaining: 8-harness.md C8+C7 rows + verdict; 9-report.md; final gate; path-scoped
  commit+push.

## FINAL GATE — stage 8 complete, run PASSED (2026-07-04)
- **All eight frozen criteria PASS** (evidence: `8-harness.md`, sha256 recorded below):
  C1 15-row walk (every fix in every load-bearing location, substance intact); C2 (9 sweep
  items reconciled + the 3 carried notes recorded: verdict-scoping reading, vacuous GC
  label-audit import, SKILL "human sign-off" compression); C3 (all 5 cross-references
  resolve against GC at `9cec23d`, quoted both sides); C4 (521/149/670 vs frozen caps
  525/152/670 — combined AT cap, zero headroom); C5 (live == source, both diffs empty);
  C6 (diff == recorded `8902d663…0871b3`, all 25 deletion lines in the 5 expected
  classes); C7 (report inspected item-by-item); C8 (PASS — scored on the round-2 lite
  verdict, see prior entry).
- **C7 report:** `9-report.md` — D-S1..S3 owner decisions, no-battery residual + 3
  risk-acceptance classes, D-10 aspirational relabel, C4 cap raise + net-zero consequence,
  the retrodiction's cycle-counter residual + (v) frozen-wording lesson, attention spend
  (+100 lines combined, +17.5%, at cap).
- Artifact hashes at close: 8-harness.md + 9-report.md hashes in the shell record;
  8-retrodiction.md final `85b7391f…9d56be`; built METHODOLOGY `04d1044c…26f065`, SKILL
  `b5e122ef…9a2527`; freeze pins verified intact post-resume.
- **Route: DONE → commit PATH-SCOPED to `Dragonfly/` + push** (exclude
  `Guarded_change/guarded-change.companion.md`). Live install stands (== source).
