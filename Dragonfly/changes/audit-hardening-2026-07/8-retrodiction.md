# 8 — C8 retrodiction: the new rules replayed against the pinned hunt record

**Executed:** 2026-07-04, by the author (token-free — document analysis only), against the
PINNED fixture copies in `fixtures/hunt-record/` (sha256s recorded at the gate-4 freeze;
verified unchanged at execution — see 8-harness.md). All citations below are into the pinned
copies. Pre-registered expected outcomes: frozen criteria C8 (1.5-criteria.md, sha256
`0ba8cfc5…00e130`). **This record receives a guarded-change-lite cold pass before C8 is
scored** (per the frozen criterion).

**REVISION (round 2, same day):** the round-1 lite pass returned **MAJOR** — sub-check (i)
rested on a false premise ("S1's test never ran"): the author had walked only decisions.md
+ hypotheses.md, while the pinned **observation ledger** (the surface where stage 5 records
runs) contains two token-spending smoke runs, S1-O18 and S1-O21, that were never
adjudicated. This revision re-executes (i) on the full pinned record with both candidate
laps explicitly classified, and repairs the round-1 pass's three minor evidence defects in
(ii)/(iv)/(v) + nitpicks. Round-1 lite record: `8-retrodiction-litepass.md`; round 2 (of
this revision): `8-retrodiction-litepass-round2.md`.

**SCORED (round-2 lite pass, same day): worst severity MINOR — the C8 PASS claim
survives; all 7 round-1 findings adjudicated genuinely resolved ("the MAJOR earned, not
reworded around"). C8 = PASS.** The round-2 MINOR (the (v) frozen-wording label mismatch)
+ 5 nitpicks were then fixed IN PLACE in this document per the severity model (minor
routes forward, no re-bounce) — so the reviewed hash in the round-2 record
(`66f9173c…beca2b`) is deliberately stale relative to this final file; the fix list +
final hash are in the decisions.md stage-8 entry.

Evidence set: `fixtures/hunt-record/{decisions, hypotheses, CONTEXT-BLOAT-HUNT,
observation-ledger, symptom-ledger}.md`. Sub-check selection rule (frozen): rules with
fully-recorded fixtures only — D-3, D-14, D-2, D-8, D-12; D-13 has no sub-check (its
precedent is user testimony, not in-record — excluded by rule, not omission).

---

## (i) D-3 — cycle count computed from the record vs the pre-registered lap inventory

**Rule as built:** "A **cycle** = one discriminating test **run and recorded** — a completed
stage-4→5 lap" (METHODOLOGY stage 6), counted per `S#` thread.

**Pre-registered inventory:** S2 = the O16 replay-search and O17 toggle runs (hunt
decisions.md:24-36), adjudicated as 1 or 2 laps with the choice justified; S1 = 0 completed
laps. Any lap outside the inventory, or S1 ≠ 0, = fail.

**Computation:**
- **S2 = 2 laps.** Two distinct discriminating tests were designed, gated, run, and
  recorded: (1) `replay_search.py` — its run is recorded as O16, cited in the stage-7
  pre-check "Reproduce-on-demand (O16)" (decisions.md:28-29) and in H-S2-RECENCY's confirm
  line "replay shows detailed-06-19 NONE in top-5, confab at rank 2 (O16)"
  (hypotheses.md:31); (2) `toggle_relevance.py` — its run is recorded as O17, "toggle to
  relevance ranking surfaces the real memory at rank 1 and drops the confab (O17)"
  (hypotheses.md:31-32). **Adjudication 2-not-1, justified:** the built unit is per test
  run-and-recorded; the record shows two artifacts (each with its own lite cold pass —
  "one cold red-team pass each", decisions.md:25-26), two separately recorded observations
  (O16, O17), each independently updating H-S2-RECENCY's status (confirm cites them as
  separate legs: replay ∧ toggle). The alternative (one lap: "replay+toggle as a single
  discriminating unit") fails the definition's own words — two runs, two records.
- **S1 = 0 COMPLETED laps — earned by adjudicating the candidate runs, not by "never
  ran."** The walk covers decisions.md AND the observation ledger (stage 5 records run
  results in the observation ledger — METHODOLOGY stage 5 — so a lap inventory confined to
  the gate log is incomplete; round 1 of this record made exactly that error). The full
  candidate set:
  - **S1-O18 (smoke anchor run #1, SPENT TOKENS)** — NOT a completed lap. It was a
    harness-qualification run inside the triage's guarded-change (entered at
    decisions.md:104-105) whose own representativeness anchor **failed**: "this
    configuration did NOT reach the bleed-producing regime → **C2 anchor-repro NOT met →
    STOP-FOR-HUMAN**" (observation-ledger.md:375-377), verdict "NO_BLEED but UNDERPOWERED
    → inconclusive (does NOT refute H-S1-WRITELOAD-DOSE)" (observation-ledger.md:361-362).
    Under the built rules a stage-4→5 lap requires the representativeness gate passed
    before the test's reading counts (METHODOLOGY:165-166 — gate + triage "Before it is
    run"; :172-176 — no consumption before the triage is recorded passed; :263-268 — an
    artifact whose control does not exhibit the symptom is rejected); a gate-failed
    qualification run eliminates nothing
    and updates no hypothesis status — and none was updated (H-S1-WRITELOAD-DOSE's confirm
    still reads "behavioural DOSE-RESPONSE, NOT yet done", hypotheses.md:91).
  - **S1-O21 (smoke run #2, SPENT TOKENS)** — NOT a completed lap, same class. It
    reproduced the objective latency symptom ("LATENCY symptom REPRODUCED; bleed still
    NO_BLEED", observation-ledger.md:413-414) — a stage-1-shaped repro achievement for the
    latency readout — but "still didn't reach the deepest regime" (observation-ledger.md:
    419) for the named bleed symptom, i.e. the anchor for S1's frozen symptom was again
    not met; it split no live hypotheses, and no status in the pinned hypotheses.md
    consumes it.
  - **The designed discriminating test itself** (the A/B/C dose-response protocol,
    `s1-repro-spec.md`) never ran as designed: the smoke runs were its anchor-seeking
    precursors ("Next knob: …", observation-ledger.md:424-427). **Scope correction to the
    frozen pre-registration's parenthetical:** the frozen words are "(designed test never
    ran, :96)" (1.5-criteria.md:32); the :96 reference is to "Awaiting user go/no-go"
    (decisions.md:95-96). That rationale is accurate for the designed protocol but stale
    as a record summary — decisions.md:104 records "S1 → guarded-change ENTERED (user
    'go', 2026-07-02)", superseding :96's "awaiting," and the two smoke precursors
    DID run. The pre-registered OUTCOME (S1 completed-lap count = 0) holds on the full
    record; the parenthetical's rationale needed this correction to be earned.
  - The S1 cold red-teams (S1-O7 at decisions.md:68-69; S1-O13 at decisions.md:59) are
    triage/stage-7-style cold passes of causal *stories*, not test runs; the git
    archaeology (S1-O16) is a stage-2 observation entry (decisions.md:75-81). Not laps.
- **Laps outside the inventory:** none — every run-and-recorded test in the pinned record
  is either O16/O17 (counted) or S1-O18/S1-O21 (adjudicated non-laps above). Evidence:
  both recording-surface ledgers walked row-by-row, AND a run-marker grep across all five
  pinned files (`grep -n "SPENT TOKENS\|RUN #\|SMOKE" *.md`) returns exactly two hits —
  observation-ledger.md:360 (S1-O18) and :413 (S1-O21); CONTEXT-BLOAT-HUNT.md references
  runs only by pointer, records none.

**Residual observation for the C7 report (a real edge the retrodiction exposed):** two
token-spending runs that eliminated no hypothesis do not enter D-3's cycle count (both
failed their representativeness anchor — they are gate-rejected qualification runs). The
burn IS visible to the built rules — the re-examination prong and the harness's own
guarded-change loop cover it — but the cycle counter alone would not have fired on this
class of thrash. Carried to 9-report.md as a named residual, not silently absorbed.

**Pre-registered outcome check:** S2 ∈ {1,2} with choice justified ✓ (2, justified);
S1 = 0 completed laps ✓ (earned via explicit adjudication of both candidate runs);
no extra-inventory laps ✓. **The rule is computable and non-vacuous on the real record —
a definite per-thread count with cited laps. (i) PASS (round 2).**

---

## (ii) D-14 — the coverage sweep anchored at the moment S1-O15 was recorded

**Rule as built:** every observation-ledger row tied to the `S#` is either **explained by
the confirmed chain** (cite how) or recorded as a **residual** — an unexplained row without
a residual entry blocks "found" (METHODOLOGY stage 7).

**Pre-registered anchor:** the moment S1-O15 was recorded (hunt decisions.md:76-78), judged
against the **then-live leading account** — NOT the final H-S1-WRITELOAD-DOSE state (which
subsumes it: "exactly the user's A/B (S1-O15)", hypotheses.md:85), and NOT "no confirmed
chain" (vacuous). Expected: the sweep classifies S1-O15 as unexplained-by-the-then-account
→ demands a residual entry the record lacks.

**Replay:** At the anchor, the then-live leading account was **H-S1-EMERGENT** — installed
as leading by the immediately preceding stage-7 entry: "Leading account is now
**H-S1-EMERGENT** (context-length coherence decay, self-reinforcing within-session)"
(decisions.md:70-71). S1-O15's content: on the OLD direct-edit path (≤v0.0.31),
"degradation happened there too but needed **larger files / longer time** → dose-dependent,
not qualitative" (decisions.md:77-78). Judged against H-S1-EMERGENT: generic
context-length decay accommodates "longer time" but **does not explain the file-size dose
axis** — why degradation onset on the old path scaled with *file size* (the
session-length-comparability framing is this replay's inference, not S1-O15's text; the
asymmetry itself is the record's, and it is what later motivated the dose account,
hypotheses.md:82-85: propose_write "fast, on small files" vs the old path's "much higher
threshold (large files / long sessions)"). So at the anchor, S1-O15 is
**unexplained-by-the-then-account** → D-14 demands a residual entry (named secondary
contributor / open sub-hypothesis, ranked). **The record lacks one:** the entry instead
folds S1-O15 directly into forming a NEW ungated candidate (H-S1-WRITELOAD-DOSE,
decisions.md:81-83) — good hunting, but no explained-or-residual disposition per row was
ever recorded; nothing in the pinned record carries a D-14-shaped residual list — the word
"residual" occurs only at hypotheses.md:167 ("residual context-length coherence decay is a
model property", a caveat inside the refuted H-S1-DISTANCE entry) and
observation-ledger.md:212 (the same caveat) — neither is a per-row explained-or-residual
disposition.

**Pre-registered outcome check:** the sweep, applied at the anchor, flags S1-O15 as
unexplained and demands a residual entry the record lacks ✓ — and the anchor choice
demonstrably matters (against the final state the candidate explains it; against no-chain
everything is trivially residual). **Non-vacuous exactly as pre-registered. (ii) PASS.**

---

## (iii) D-2 — the characterized-verdict checklist vs the recorded S1 ending

**Rule as built:** "characterized" requires ALL of (a)–(e); missing any → not a legal stop
(METHODOLOGY, between stages 7 and 8).

**Fixture:** the S1 ending entry, "S1 stage-7 red-team | MAJOR | hypothesis REVISED, NOT
'found' … **S1 outcome = CHARACTERIZATION + mitigation directions, not a code root-cause
'found'**" (decisions.md:68-74).

**Element-by-element:**
- **(a) what IS established, cited + cold-red-teamed:** substantially present — "structural
  facts hold" through the S1-O7 cold pass (decisions.md:69-70); the established structural
  claims were independently challenged.
- **(b) refuted hypotheses, with evidence:** present — H-S1-DISTANCE's escalation mechanism
  refuted by the S1-O7 cold pass (decisions.md:68-70); H-S1-FILEBLOAT refuted by the
  S1-O13 cold pass ("DEAD CODE on Phoebe's claude-cli provider", decisions.md:59-62).
- **(c) WHY the full bar is unreachable, named reason:** present — "largely a MODEL
  property — no clean code toggle" (decisions.md:71-72) = the rule's own "model property"
  class.
- **(d) explicit human sign-off:** **ABSENT.** No recorded sign-off of the characterized
  ending exists in decisions.md:68-74 or anywhere after it — the route column reads
  "hypothesis REVISED, NOT 'found'" with no human-adjudication line (contrast the hunt's
  actual stop-for-human entries, which record adjudication explicitly, e.g. "User
  adjudication | — | re-scoped", decisions.md:22).
- **(e) presentation tier stays characterization:** followed — "I corrected my earlier
  over-confident S1 message to the user" (decisions.md:74).

Framing note (round 2): ":68-74 = the recorded S1 ending" is the frozen pre-registration's
framing; the S1 thread in fact continues through decisions.md:114. This **strengthens** the
(d) adjudication — the characterization never became a signed-off terminal state at any
later point either (the :75-114 entries are continued hunting, not sign-off).

**Pre-registered outcome check:** names ≥1 missing element ✓ — exactly the pre-registered
candidate, **(d)**. The rule, had it existed, would have forced a stop-for-human the ad-hoc
ending skipped. **(iii) PASS.**

---

## (iv) D-8 — the escape's conditions vs the recorded inversion

**Rule as built:** hypotheses MAY inform repro/instrument design first PROVIDED the
inversion is recorded in `decisions.md` **naming the infeasibility class** and each
hypothesis stays `ungated` (METHODOLOGY stage 1).

**Fixture:** the inversion is the ordering across decisions.md:41-86 (hypotheses formed,
worked, refuted: the code-fidelity gate + structural-analysis entries at :45-50 —
H-S1-DISTANCE's analysis itself lives at hypotheses.md:149-171 — H-S1-FILEBLOAT at :51-67,
the stage-7 revision at :68-74, H-S1-WRITELOAD-DOSE formed at :75-86) **versus** :87-96
(the discriminating repro **designed** only afterward: "S1 stage-4 — discriminating test
DESIGNED" at :87; the designed protocol itself never ran — see sub-check (i)).

**Adjudication:**
- **Infeasibility class, named with citations:** the record carries the substance —
  *emergent / intermittent / load-dependent*: "part of S1 may be emergent context-length
  coherence decay (a model property, not a clean toggle)" (decisions.md:47-48); "bleed is
  intermittent/load-dependent → instrument-to-capture, not a clean offline toggle"
  (hypotheses.md:163-164). A blind repro genuinely could not be built first: the repro
  design that finally emerged **needed** the hypotheses' content (dose axes, arm design,
  incident-equivalent anchoring — decisions.md:88-103 derive directly from
  H-S1-WRITELOAD-DOSE's confirm/refute structure, hypotheses.md:91-96).
- **Does the required formal inversion entry exist?** **NO.** No decisions.md entry
  records "repro ordering inverted because <class>" — the inversion is visible only by
  reading the entry sequence. (The tier-discipline half, corrected in round 2: honored for
  the archaeology/WRITELOAD-DOSE window — "GATE MARKER: ungated … Present as a strengthened
  *candidate*, never the cause" (hypotheses.md:97-98); "marked `ungated`; NOT presented as
  the cause" (decisions.md:83-84) — but the record also contains one recorded VIOLATION
  inside the inversion window: "H-S1-FILEBLOAT was presented as 'leading' WITHOUT a cold
  red-team or repro/toggle — a gate-before-present slip" (decisions.md:53), self-caught
  only by a user-prompted audit (:51-58). That slip is exactly what D-8's stays-`ungated`
  condition binds — further evidence the rule is non-vacuous here.)

**Pre-registered outcome check:** class named with citation ✓; verdict on the record
entry = **substance present, formal entry absent** ✓ — exactly as pre-registered; the rule
would have demanded the entry the record lacks. **(iv) PASS.**

---

## (v) D-12 — the class-coverage/shared-assumption record at the post-second-refutation convergence point

**Rule as built:** each convergence-gate pass records which mechanism classes the live
hypotheses cover, which are ruled out, and what assumption the live set shares
(METHODOLOGY stage 6).

**Fixture anchor:** the moment the second S1 code hypothesis died: "SECOND S1 code
hypothesis refuted on a false architectural assumption" (decisions.md:62); "Second S1
hypothesis killed by a false architectural assumption (cf. H-S1-DISTANCE)"
(hypotheses.md:64-66).

**Replay — the record D-12 would have produced there:**
- *Classes covered by the then-live/just-dead set:* prompt-structure erosion
  (H-S1-DISTANCE — refuted), host-side Python tool-loop accumulation (H-S1-FILEBLOAT —
  refuted), model-emergent context decay (H-S1-EMERGENT — live), subprocess-context
  imitation (H-S1-WRITECONTENT-IMITATION — live, born from the refutation itself,
  hypotheses.md:68-74).
- *Shared assumption of the refuted pair, named:* **that the host-side (Python) prompt/
  tool-loop path is where S1's mechanism lives — i.e. the Python tool-loop matters on
  Phoebe's claude-cli provider.** The false assumption is stated for FILEBLOAT itself and
  flagged as a pattern at the death of the second hypothesis: "the accumulation mechanism
  … is DEAD CODE on Phoebe's `claude-cli` provider" (decisions.md:59-60 /
  hypotheses.md:62-64); "killed by a false architectural assumption (cf. H-S1-DISTANCE)"
  (hypotheses.md:65-66); guard "Do not resurrect without a claude-cli-aware mechanism"
  (hypotheses.md:66). The strongest in-record statement of the pair-wide umbrella is the
  S1-O13 ledger row itself: "file I/O + monologue + reasoning all accumulate in the
  **claude SUBPROCESS's own context** … that's the real bleed surface, not brain-side
  prompt assembly" (observation-ledger.md:292-294) — the umbrella is a derivation
  grounded there, not stated verbatim as a pair-property.

**Pre-registered outcome check:** the rule, applied at the anchor, names the shared
architectural assumption ✓ (the Python tool-loop mattering on the claude-cli path) —
non-vacuously, exactly where the recorded hunt was class-blind: the hunt articulated the
shared assumption only AFTER paying for it twice. **Frozen-wording flag (round-2 lite
pass, finding 1):** C8's frozen text says "the **live set's** shared architectural
assumption," but what is derivable at the anchor — and what C8's own anchor citations
(hypotheses.md:65-66) and precedent (0-audit-findings.md:115-117, "Both **refuted** S1
hypotheses died on the SAME false architectural assumption") point at — is the **refuted
pair's** shared assumption, as the replay above derives. The live set at the anchor
({H-S1-EMERGENT, H-S1-WRITECONTENT-IMITATION}) does not hold it; under the built rule the
record's live-set line there would read "**none identified**" (which the rule explicitly
counts, METHODOLOGY:189-190) alongside the refuted-pair lesson. The executed content
matches the pre-registration's evident intent (the precedent it cites), and (v) is
non-vacuous under either label; the mismatch is the frozen wording's, flagged here rather
than silently relabeled. (Honesty flag, round 2: since S1 completed zero laps — sub-check
(i) — no actual S1 stage-6 convergence pass ever fired; the anchor is the analytically
chosen point the frozen pre-registration names, a counterfactual replay by design.)
**(v) PASS (round 2, with the frozen-wording flag).**

---

## Verdict

All five sub-checks produced their pre-registered expected outcomes with pinned-record
citations. No sub-check was vacuous (each fires on a definite feature of the real record
that the ad-hoc hunt handled without the rule). Scored per the frozen criterion only
after the guarded-change-lite cold review of this record: round 1 = MAJOR → revised;
round 2 (of the revision) = MINOR, "the C8 PASS claim survives," 7/7 round-1 findings
genuinely resolved (`8-retrodiction-litepass-round2.md`). **C8 = PASS (scored
2026-07-04).**
