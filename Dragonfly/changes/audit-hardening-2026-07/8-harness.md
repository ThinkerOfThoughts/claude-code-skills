# 8-harness.md — stage-8 verification record: dragonfly audit-hardening-2026-07

**Verifier:** the run author (`claude-fable-5`), 2026-07-04. **Evidence discipline:** every
criterion row carries its evidence inline (quote + file:line, or verbatim command output) —
an unreviewed check is not a check. For the text-presence criteria (C1, C2, C3, C6's
hunk-walk, C7) **inspection is the execution** (the L-7 reading recorded in the sibling
guarded-change run); the mechanical criteria (C4, C5, the C6 diff identity) quote command
output run fresh on 2026-07-04 (post-resume — the pause did not stale the evidence).
Line numbers cite the BUILT files: METHODOLOGY.md sha256
`04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065`, SKILL.md
`b5e122ef0aa9fad91642c7540f9c56c9351024e933910ba82a7f3274239a2527`.

## Freeze verification (mechanical) — intact

Run 2026-07-04 (post-resume), all hashes match the gate-4 freeze entry in `decisions.md`:

```
$ sha256sum 1.5-criteria.md 2-plan.md fixtures/hunt-record/*.md
0ba8cfc59f3fd0b63f3b0e5b0e1f282ee87b206d6ff8bc20b3c4591cbc00e130  1.5-criteria.md
15ab47d6c5dfb526323a043a0e068f51ede2f6d130fb037f0d673b3c563ce523  2-plan.md
46ae8d4f0c9afd7793c041a944e144dc06d71bf183136ae1be78e499d46cb98f  fixtures/hunt-record/CONTEXT-BLOAT-HUNT.md
a4c2addadfb78c3fe419222a52caf51218330e7d7b00ca7ec2e342dc8023606a  fixtures/hunt-record/decisions.md
fcfcd687929cd1f846309f03fd093c030c76c4c30fe9cf78ba275b22ec0586bc  fixtures/hunt-record/hypotheses.md
6459716bedf8c614416b1a64db2031a0eb3f33891ad25925521a1eab29727925  fixtures/hunt-record/observation-ledger.md
2d9d16ff61ece109aa0e490debbf8d7ea0b2b7189935ad6f10dc366e28fe41c6  fixtures/hunt-record/symptom-ledger.md
```

## C4 — bloat caps (gating, mechanical): **PASS**

Frozen caps (cited from the FROZEN CRITERIA, 1.5-criteria.md C4 row — NOT the plan's
superseded Measurement line, per the stage-7 carried note): METHODOLOGY ≤ 525, SKILL ≤ 152,
combined ≤ 670.

```
$ wc -l METHODOLOGY.md SKILL.md
  521 METHODOLOGY.md
  149 SKILL.md
  670 total
```

521 ≤ 525 ✓, 149 ≤ 152 ✓, 670 ≤ 670 ✓ (combined exactly at cap — zero headroom; any future
fix must be net-zero lines, recorded at the stage-7 gate). C1-against-C4: no mapped substance
was traded for the caps — the stage-6 cold review adjudicated **every** author compression
substance-safe except 3 findings, all fixed net-zero (6-redteam-build.md; stage-7 gate entry).

## C5 — live == source (gating, mechanical): **PASS**

```
$ diff ~/.claude/skills/dragonfly/METHODOLOGY.md METHODOLOGY.md
$ diff ~/.claude/skills/dragonfly/SKILL.md SKILL.md
(both empty)
```

## C6 — pure-additive (gating, mechanical + inspection): **PASS**

Current `git diff 9cec23d -- Dragonfly/METHODOLOGY.md Dragonfly/SKILL.md` sha256
`8902d663d419bba056f146e7c959fa242c6a6348c8d1d60ed13f0a704d0871b3`, byte-identical to the
recorded `6-build.diff` (verified by `diff` of the two, empty). The full hunk-by-hunk
adjudication (20 hunks vs the 15 mapping rows) is the stage-6 cold reviewer's, in
`6-redteam-build.md` — independently executed, not self-certified. Deletion-line census
(this walk): 25 `-` lines (24 content + 1 blank), each in one of the 5 expected classes
frozen in the plan's Measurement section:

1. **In-place sentence extensions** (original re-emitted verbatim with an extension) — 18
   lines: toggle item tail (M:200), triage intro enumeration + heading "+ detector/readout"
   (M:326, M:324), lite-paragraph tail (M:344), stop-list item re-emit (M:514), and the SKILL
   step/paragraph tails (S:21, S:47, S:74-75, S:97-98, S:107-109, S:121-123, S:130-131).
2. **Loop-diagram :91 line extension** — 1 line (the stage-1 diagram line gaining the
   breadcrumb "(escape for bugs unreproducible blind: see stage-1 detail)", M:91-92).
3. **`diagnosis.md` artifact-line extension** — 1 line (code-block listing line extended by
   D-2/D-13/D-14: "per-level depth-check status … named residuals; characterized: (a)–(c)
   instead", M:472-473).
4. **The named D-10 rewrite** (obligation verbatim-or-stronger) — 4 lines (SKILL self-check
   section; the stage-3-style red-team obligation retained, strengthened to "non-trivial
   edits to either take the full guarded-change loop", S:139-149) + the stage-8 handoff
   re-emit whose obligation sentences survive verbatim ("Hand to **guarded-change** for the
   fix. Dragonfly does **not** author the fix.", M:231 — restored at stage 7 after the
   review caught its deletion).
5. **The named stage-6 punch-line micro-rewrite** — 1 line ("This is the defense…" → "The
   cap is the defense against token-burning thrash.", M:192 — referent re-bind, obligation
   identical).

No deletion-shaped hunk outside the classes; no existing rule deleted or weakened.

## C1 — every fix in every load-bearing location (gating, inspection): **PASS**

Walk of all 15 mapping rows (2-plan.md table = the oracle). Per row: the landed text's
load-bearing phrase (trigger → requirement → **consequence**) + location.

- **D-1 provenance** — M:388-394: "applies to **every dragonfly cold pass** — direct stage-7
  AND the triage's guarded-change/lite passes at stages 1/4: the record carries the verbatim
  charter, the exact context list, the reviewer's verbatim output, the agent type + model,
  and the reviewer-reported context hashes; it lives in, or is pointed to from, the hunt
  folder (a full-GC triage run keeps its own `changes/<slug>/` record, nested or external,
  with a pointer in the hunt's `decisions.md`). Missing any element = the pass is
  **un-run** — its reading may not be consumed." SKILL:122-123: "Every pass carries the
  **provenance record** (verbatim charter, context list, verbatim output, agent+model,
  reviewer hashes) in/pointed from the hunt folder; missing any = un-run." ✓
- **D-2 characterized** — M:221-227 (block between stages 7 and 8): "requiring ALL of:
  (a) what IS established, each claim cited and cold-red-teamed … (b) which hypotheses were
  refuted, with evidence; (c) WHY the full bar is unreachable — a named reason … (d)
  **explicit human sign-off**; (e) presentation tier stays 'characterization' … Missing
  **any** of (a)–(e) → not a legal stop." Stage-9 clause M:234-235: "For a **characterized**
  handoff there is no stage-7 chain+toggle to use: stage 9 verifies the marked mitigations
  on **symptom evidence only**." Artifact line M:472-473: "characterized: (a)–(c) instead".
  SKILL step 8 :78-79: "'**Characterized, not found**' = the only other legal ending — ALL
  of (a)–(e) incl. **human sign-off** (METHODOLOGY)." SKILL step 9 :88: "Characterized →
  symptom-evidence only". ✓
- **D-3 cycle definition** — M:182-185: "A **cycle** = one discriminating test **run and
  recorded** — a completed stage-4→5 lap; the cycle count and per-area re-examination tally
  are appended to `decisions.md` at each stage-6 pass (cap countable from the log; an
  uncounted pass is a gate violation)." SKILL step 6 :68-69: "A **cycle** = a test run
  **and recorded**; per-`S#`-thread cycle counts + the class-coverage/shared-assumption
  record appended to `decisions.md` each pass, else gate violation (METHODOLOGY)." ✓
- **D-4 detector as artifact** — M:281-287: "Anything that *decides* 'the symptom occurred'
  (a classifier, a grep, a threshold rule) is a detector, subject to this gate and the
  triage: BEFORE any reading it produces is consumed, it must be shown to **fire on a
  known-true instance AND stay silent on a known-clean one**, evidenced by an
  observation-ledger row (the silent-on-clean half is a deliberate, strictly stronger duty;
  an artifact that merely captures data for later reading carries only the
  instrument-to-capture bar above). An unvalidated detector's readings are untrusted."
  Triage intro M:326 enumerates "repro / test / instrument / toggle / detector/readout".
  SKILL rep-gate :96-98: "A **detector/readout** (anything deciding 'symptom occurred')
  must fire on a known-true instance AND stay silent on a known-clean one (ledger row)
  before its readings are consumed (METHODOLOGY)." SKILL triage heading :100 enumerates
  "(every repro/test/instrument/toggle/detector)". ✓ (Boundary sentence present — sweep
  item 6 below.)
- **D-5 probabilistic toggle/window** — M:200-202: "For a rate-based/intermittent symptom
  the toggle criterion states the **expected rate shift and run count** up front
  (guarded-change's probabilistic rubric, by reference); a single flip does not satisfy
  it." M:253-255: "9a/9b define their **observation window up front** from the symptom's
  observed ledger frequency (e.g. ~1/session over 5 sessions → 9b window ≥ 5 sessions,
  pass = 0 occurrences); a single clean run or an unstated window does not satisfy them."
  SKILL step 7 :74-75: "rate-based → it pre-states rate shift + run count"; step 9 :88:
  "rate-based → window set up front". ✓
- **D-6 config validation** — M:456-459: "every config path (`redteam_context` entries,
  `reproduction.logs`, `ledgers.dir`) is mechanically checked to exist/be readable BEFORE
  stage 0 proceeds — no hunt on unvalidated paths. Invalid-but-adaptable → adapt + record
  it as its own `decisions.md` entry (what changed, why) + proceed; dead/unresolvable →
  **stop for the human**." SKILL Inputs :19-21: "Validate config paths at hunt start:
  dead/unresolvable → stop; adaptable → adapt+record+proceed." ✓
- **D-7 per-thread convergence** — M:185-188: "Multiple `S#` threads count convergence
  **per-thread** (same unit; a test discriminating across threads increments each thread
  whose hypotheses it splits); a thread hitting the cap **escalates alone**; threads may
  split into separate hunts at any gate with a recorded reason — global counting may not
  mask per-thread thrash." SKILL step 6 :68-69 ("per-`S#`-thread cycle counts", above). ✓
- **D-8 repro-ordering escape** — M:142-146: "**Repro-ordering escape (an exception to the
  ordering above, recorded):** when a faithful repro cannot be built blind (intermittent /
  load-dependent / emergent), hypotheses MAY be formed first to inform repro/instrument
  design, PROVIDED the inversion is recorded in `decisions.md` **naming the infeasibility
  class**, and every such hypothesis stays `ungated`; the representativeness gate still
  binds … — legal only recorded + tier-bound." Diagram breadcrumb M:92: "(escape for bugs
  unreproducible blind: see stage-1 detail)." SKILL step 1 :46-47: "**Escape:** repro
  impossible blind → hypotheses may inform design; inversion recorded + class named; they
  stay `ungated` (METHODOLOGY stage 1)." ✓
- **D-9 lite-pass record** — M:346-348: "A lite pass records, minimally: the artifact, the
  one-line intent + criterion, the verdict, and where the verbatim output lives, in
  `decisions.md`; unrecorded = treated as not having happened (artifact untrusted)."
  SKILL triage item 3 :109: "recorded in `decisions.md` — unrecorded = didn't happen." ✓
- **D-10 self-check parity + honest label** — SKILL:139-149 (the one named rewrite; no
  METHODOLOGY location, per the mapping row): "These files are **prompts**
  (position-sensitive): **non-trivial edits to either take the full guarded-change loop**.
  Standing criteria after any edit to these files **or to guarded-change**: live == source
  (`diff`); SKILL ↔ METHODOLOGY consistency on every shared rule; behavior-preservation for
  anything moved/removed; every named guarded-change cross-reference … resolves — severed
  = failure. The flagship test (**aspirational — not yet run** — an unrun check may not be
  described as an existing safeguard; a standing replayable probe once run) …" ✓
- **D-11 coupling check** — M:394-399: "Cold passes inherit ALL of guarded-change's
  **unconditional** discipline bullets (those with no stage or trigger scope of their own),
  provenance included. The stage-3 coverage-challenge bullet does NOT apply to dragonfly's
  **direct stage-7 and lite passes** (neither is a stage-3 review; the analog is the
  shared-assumption aim above) — but a **full guarded-change triage run keeps ALL of
  guarded-change's own stage duties, including its stage-3 coverage challenge**: dragonfly
  narrows nothing inside a full-GC run." SKILL self-check :144-145: "every named
  guarded-change cross-reference (charter, severity model, probabilistic rubric, lite
  definition) resolves — severed = failure." ✓
- **D-12 hypothesis-space challenge** — M:188-191: "Each pass also records which mechanism
  **classes** the live hypotheses cover, which are ruled out, and **what assumption the
  live set shares** (explicit 'none identified' counts) — cold passes aim at the shared
  assumption too, one found false ranks by impact; a pass missing this record is a **gate
  violation**, like an uncounted cycle." Charter aim M:386: "**What assumption does the
  live hypothesis set share, and is it true?** (aimed at the set)". SKILL step 6 :68-69
  (clause quoted at D-3) + SKILL cold-red-team aims :121: "what assumption does the live
  hypothesis set share?" ✓
- **D-13 depth check** — M:207-212: "The root = the **deepest node the project can act
  on**. For the claimed root, ask 'why does this node produce the next?' ONE level down;
  'found' requires recording that this why-down is (a) **answered** with cited evidence,
  (b) **explicitly out of scope** (model property / third-party / not actionable — named),
  or (c) **not load-bearing** … The stage-7 cold pass explicitly challenges '**root or
  relay?**' — 'explains the symptom' at a relay does not satisfy stage 7." SKILL step 7
  :75: "'Found' also needs the recorded **depth check** (root or relay?)"; step 8 :78:
  "per-level depth status"; cold-red-team aims :121: "root or relay — deepest actionable
  node?" ✓
- **D-14 evidence-coverage sweep** — M:213-217: "Before 'found': every observation-ledger
  row tied to the `S#` is either **explained by the confirmed chain** (cite how) or
  recorded as a **residual** (named secondary contributor / open sub-hypothesis, ranked),
  carried in `diagnosis.md` + the stage-8 handoff, struck only with a recorded reason.
  '**Found (primary), with named residuals**' is legal; **silent absorption is not** — an
  unexplained row without a residual entry blocks 'found'." Full-bar re-anchor M:218-219:
  "Only with the depth check and coverage sweep recorded is 'found' declarable — all three
  bar items + both records + the chain's cold-red-team pass (gate marker `cold-red-teamed`),
  conjunctively." Stage-9 recheck M:255-256: "Stage 9 also re-checks the **residuals
  list**: killing the primary does not close an unexplained residual." SKILL step 7 :75:
  "+ **coverage sweep** (METHODOLOGY stage 7)"; step 8 :78: "named residuals"; step 9 :88:
  "residuals re-checked". ✓
- **L-3 stop-point wiring** — M:512: "a **characterized-verdict ending** (its explicit
  human sign-off — requirement (d))"; M:515: "**dead/unresolvable config paths** at hunt
  start (≠ missing config; adaptable ones proceed)." SKILL stop rules :129-131: "a
  **characterized ending** needs its sign-off; **config is missing**; or **config paths
  are dead/unresolvable** at hunt start (adaptable → adapt+record+proceed)." ✓

All 15 rows: fix present in every named location, substance (trigger + requirement +
**consequence**) intact. No row's substance was traded against C4 (see C4 row).

## C2 — cross-file + intra-file consistency (gating, inspection): **PASS**

The stage-6 cold reviewer independently verified all 9 sweep items on the built text
(6-redteam-build.md §sweep); this walk re-states each reconciliation with the built cites:

1. **D-2 vs gate-before-present + stage 9** — "characterized" is tier (e), below "the
   cause" (M:225-226); mitigations "marked as such … symptom evidence only — no
   cause-resolution claim" (M:226-227, M:234-235). No tier bypass. ✓
2. **D-3 unit vs D-7 counts** — one unit, "Multiple `S#` threads count convergence
   **per-thread** (same unit…)" (M:185-186). No second unit. ✓
3. **D-5 vs borrowed rubric** — "(guarded-change's probabilistic rubric, by reference)"
   (M:202); no restated rubric text → no drift channel. Resolves under C3 below. ✓
4. **D-8 escape vs stage-1 ordering + diagram** — detail carries the full exception
   ("an exception to the ordering above, recorded", M:142); the diagram line carries ONLY
   the pointer breadcrumb (M:92); no absolute statement of the excepted rule remains;
   hypotheses stay `ungated` (M:145) so gate-before-present is unaffected. ✓
5. **D-13/D-14 vs the conjunctive bar** — additional requirements; "'Found' requires **all
   three**, conjunctively (two-of-three is not 'found')" survives verbatim (M:194-195);
   the re-anchor makes the widened bar explicitly conjunctive (M:218-219). ✓
6. **D-4 vs instrument-to-capture** — the boundary sentence is in the built text: "the
   silent-on-clean half is a deliberate, strictly stronger duty; an artifact that merely
   captures data for later reading carries only the instrument-to-capture bar above"
   (M:285-286). Strictly stronger, loosens nothing. ✓
7. **D-1/D-9 vs lite's scaffolding-drop** — "**The provenance record is not scaffolding** —
   lite keeps the charter AND the provenance record …, dropping only the five-item doc set
   above" (M:344-346); the five-item enumeration "(spec / criteria / plan / baseline /
   regression)" survives at M:342. ✓
8. **D-10 relabel vs the self-run sentence** — "This skill can be run on its own artifacts"
   survives (SKILL:139); the red-team obligation is retained and strengthened
   (SKILL:140-142); the flagship test survives, labeled "**aspirational — not yet run**"
   (SKILL:146-147). ✓
9. **D-11 scoped exemption vs the imported coverage-challenge duty** — the GC bullet is
   stage-3-scoped at source (GC:243 "plus the coverage-challenge bullet for stage-3
   reviews", GC:251 "**Challenge criteria coverage (stage 3).**"); dragonfly exempts only
   "direct stage-7 and lite passes" and affirmatively carves out full-GC runs ("dragonfly
   narrows nothing inside a full-GC run", M:399). No contradiction with the import. ✓

**Carried notes (recorded here per the stage-7 gate):**
- **Verdict-scoping reading:** "the only other legal terminal verdict" (M:221) is read as
  scoping **claims-carrying endings** — a human-directed abort at the convergence cap
  (M:511) ends the hunt by human authority without a diagnostic verdict, and that remains
  legal; "found" and "characterized" are the only endings that may carry diagnostic claims.
- **Vacuous GC import:** under the built definition of "unconditional" (M:395), GC's
  label-audit bullets (GC:256-274) import into dragonfly passes where no criterion labels
  exist — vacuously satisfied there, active the moment a pass reviews labeled criteria
  (e.g. a full-GC triage run). No contradiction; noted so the import is not mistaken for
  drift.
- **SKILL compression note:** SKILL step 8's pointer reads "**human sign-off**" for width;
  the (d) requirement's full "**explicit human sign-off**" wording lives at the
  authoritative D-2 block (M:225) and the stop inventory (M:512). Pointer ≠ weakening
  (SKILL defers to METHODOLOGY by construction, SKILL:8-9).

## C3 — cross-reference resolution (gating, mechanical + inspection): **PASS**

Each named by-reference import, quoted both sides, against guarded-change at `9cec23d`
(working-tree GC files verified byte-identical to `9cec23d` by the stage-6 reviewer):

1. **Charter core** — dragonfly: "guarded-change's unchanged stage-3/6 reviewer charter
   (four lenses + evidence discipline)" (M:340-341); "Reuse guarded-change's four-lens
   charter + evidence discipline (see `guarded-change/METHODOLOGY.md`)" (SKILL:118). GC:204:
   "## The red-team charter (stages 3 and 6)". Resolves — the section exists, stages match. ✓
2. **Provenance bullet** — dragonfly names five elements (M:390-391: verbatim charter /
   exact context list / reviewer's verbatim output / agent type + model / reviewer-reported
   context hashes). GC:238-240: "(i) verbatim charter/prompt given, (ii) the exact context
   path list given, (iii) the reviewer's verbatim output …, (iv) the reviewer's agent
   type + model, and (v) the reviewer-reported sha256 of each context file". Same five,
   same order. ✓
3. **Severity model** — dragonfly: "Identical to guarded-change (see its METHODOLOGY)"
   (M:409). GC:302: "## Severity model and gate routing". Resolves. ✓
4. **Probabilistic rubric** — dragonfly: "states the **expected rate shift and run count**
   up front (guarded-change's probabilistic rubric, by reference)" (M:201-202). GC:151:
   "the criterion states the pass rate it expects and the number of runs that establishes";
   GC:163 names it "(treat as the probabilistic rubric above)". Says what dragonfly
   assumes. ✓
5. **Lite definition / coverage-challenge scoping** — dragonfly's lite keeps the GC charter
   by reference (M:338-344, "defined **by reference**, not paraphrase"); the D-11 scoping
   claim ("the stage-3 coverage-challenge bullet … never bound them") matches the GC
   source's own scoping (GC:243, GC:251 — quoted under sweep item 9). ✓

## C8 — retrodiction (gating, executed): **PASS**

The run's executed behavioral check. Full replay record with pinned-record citations:
`8-retrodiction.md` (final hash `85b7391f…9d56be`). Executed token-free against the pinned
fixtures (hashes verified unchanged — freeze section above — and independently re-computed
by both cold reviewers). All five pre-registered sub-checks produced their frozen expected
outcomes: (i) D-3 lap inventory — S2 = 2 laps (choice justified), S1 = 0 **earned** via
explicit adjudication of the two candidate smoke runs (S1-O18 gate-failed anchor run,
S1-O21 latency-repro/anchor-unmet — observation-ledger.md:360-379, :413-427), no laps
outside the inventory (five-file run-marker grep, 2 hits); (ii) D-14 sweep at the S1-O15
anchor flags it unexplained-by-the-then-account and demands a residual entry the record
lacks (grep: no D-14-shaped residual disposition anywhere in the pinned record); (iii) D-2
checklist names (d) — no recorded human sign-off — genuinely absent through decisions.md
end-of-file; (iv) D-8 escape — infeasibility class cited (decisions.md:47-48,
hypotheses.md:163-164), formal inversion entry absent = the pre-registered verdict;
(v) D-12 names the shared architectural assumption (Python tool-loop mattering on the
claude-cli path) non-vacuously, with the frozen wording's live-set/refuted-pair label
mismatch flagged in the record.

**Scored per the frozen criterion — no self-certification:** guarded-change-lite cold pass
round 1 = **MAJOR** (sub-check (i) rested on "S1's test never ran," refuted by the pinned
observation ledger — the reviewer caught the author walking only the gate log; the
founding-failure class the skill exists to prevent, caught by the loop applied to its own
evidence) → full re-adjudication; round 2 (of the revision) = **MINOR, "the C8 PASS claim
survives,"** 7/7 round-1 findings genuinely resolved. Verbatim review records:
`8-retrodiction-litepass.md`, `8-retrodiction-litepass-round2.md`; disposition + post-review
fix-in-place list: decisions.md ("Stage 8 RESUMED — C8 scored"). A genuine rule-design
residual surfaced by the retrodiction (token-burning gate-rejected runs invisible to the
cycle counter alone) is carried to 9-report.md.

## C7 — report contents (gating, inspection): **PASS**

`9-report.md` inspected for each required item:

- **D-S1..S3 remain unbuilt, carried for owner decision** — report §1 ("NOT built, yours
  to decide (each would be its own run)"; all three named with their rationale). Unbuilt
  is independently established by the C6 walk: the diff contains only the 15 mapping-row
  additions, no restructure/pinning/async-path change. ✓
- **The no-battery residual, named, with rationale + what evidence exists instead
  (narrowed by C8)** — report §2 ("**No replay A/B battery was run for dragonfly** — a
  deliberate, owner-visible scope decision … What was run instead — the owner-adopted …
  **C8 retrodiction** … narrows the no-battery residual but does not close it"), including
  the three owner-accepted risk classes (a)/(b)/(c) verbatim from the gate-4 entry. ✓
- **The D-10 flagship-test relabel (aspirational until first run — not run by this
  change)** — report §3 ("**This run did not run it** — the relabel is the fix"), quoting
  the built label at SKILL:146-147. ✓
- **The C4 cap raise** — report §4 (raised once pre-freeze 515/148/655 → 525/152/670,
  rationale R2-U-3, built at combined cap with the net-zero consequence recorded). ✓
- **The retrodiction's cycle-counter residual** — report §5 (token-burning gate-rejected
  qualification runs invisible to the cycle counter alone; covered by the re-examination
  prong + harness GC; candidate future fix named), plus the (v) frozen-wording lesson. ✓
- **Attention-budget spend** — report §6 (per-file table, baselines/built/caps, +17.5%
  combined at cap, "next hardening pass CANNOT be additive"). ✓

## Verdict

**All eight criteria PASS — C1, C2, C3, C7 (gating, inspection), C4, C5, C6 (gating,
mechanical), C8 (gating, executed + independently cold-reviewed twice). The change is
DONE against its frozen criteria.** Residuals and owner items live in `9-report.md`; the
final gate entry is in `decisions.md`.
