# 2 — Plan: per-stage restructure of guarded-change (Theme 1) — REVISED after stage-3 round 1

Revision drivers: file-per-stage split (round-1 M1); measure the attention budget (blocker
C-2 → C3); grep-derived rule oracle (F1/F2/L4/M2); battery reaches gate-4+ rules by
positioning arms at those stages (blocker L1) with a positive control (L2/M3);
reference-section gate-blocking rules move into stage files (F4).

## A. The target structure — file per stage

### A.1 File set (frozen at gate 4)

- **`SKILL.md`** (router, ~≤110 lines): front matter + a 2-line "what this is" + `## Inputs`
  + the **loop router table** (one row per stage: number · one-line purpose · "→ read
  `stages/stage-N.md`") + `## Stop-for-human` summary + `## Self-check`. Auto-loaded; thin.
- **`stages/stage-{0,1,1.5,2,3,4,5,6,7,8}.md`** (NEW, 10 files): each self-contained — the
  stage's procedure + **every cross-cutting rule that governs it, written in full**. An
  agent at stage N opens only `stage-N.md` (+ the router) [+ `charter.md` at stages 3/6, see
  below]. Target ≤ ~90 lines each. **Gate files (4/7/8) carry the routing TABLE** (the full
  severity table + SEV2/SEV3, not just a target list — round-2 A-1 / round-3 F5-NEW) written
  in, not only in the loop diagram — see the oracle's build note.
- **`stages/charter.md`** (NEW — round-3 F3-NEW/M1-NEW, owner-approved): the ~95-line red-team
  charter (4 lenses + discipline + provenance + conditional position/concurrency lenses),
  ONE copy, referenced by both `stage-3.md` and `stage-6.md`. `stage-3.md` adds only the
  stage-3-specific bullets (CH8 coverage-challenge + CH9/CH10 label-audit); `stage-6.md` adds
  only the stage-6 mechanical-diff duty (ST6d). This keeps stages 3/6 under the C3(a) budget
  (repeating the 95-line charter into both would blow it — round-3 F3-NEW) AND removes the
  O-1 charter-drift surface (one copy, not two). **This charter.md is guarded-change-internal
  — NOT shared with dragonfly** (dragonfly gets its own in the Theme-2 run; owner rule: intra-
  skill sharing OK, cross-skill sharing is the coupling being untangled). It is a
  **stage-declared reference file** stages 3/6 are permitted to open (C3(b)).
- **`METHODOLOGY.md`** (slimmed to orientation/reference, ~≤160 lines): *Why this exists*,
  *The loop* (diagram), *The two layers*, *The config contract*, *What a run produces*, and
  an index pointing at the stage files. NOT in the per-stage hot path — opened for
  orientation/config setup, not to run a stage. Kept (not deleted) so existing external
  references to `guarded-change/METHODOLOGY.md` (dragonfly, configs) don't break before the
  follow-on dragonfly run untangles them.

### A.2 The rule → stage-file oracle (C1; built at stage 2, frozen at gate 4)

Round 1 correctly flagged that the author's outline table can't be C1's oracle (it's
incomplete and self-referential). So C1's ground truth is an **independent, grep-derived**
enumeration, produced as `2-rule-oracle.md`:
1. Enumerate every atomic normative rule in the CURRENT `METHODOLOGY.md`+`SKILL.md` (each
   gets an ID + a source line range).
2. For each rule, derive its **governing-stage-set mechanically** — grep the current source
   for the stages the rule names / the stage-detail sections it appears in / the gates it
   blocks. Example corrections round 1 surfaced: *criteria freeze* → **{4, 8}** (freeze at
   4, verify-unchanged at 8; not {4}); *paths validated* → **{run-start, 3, 4, 6}**;
   *regression-comparable-workload* → **{2, 8}**; *unreviewed-check* → **{8}**;
   *spot-verify citations* → **{3, 6, 8}**; *human-in-the-loop stops* → **{4-blocker, 8}**;
   plus the whole charter → **{3, 6}**.
3. The build must place each rule in **every** file of its governing-stage-set.
This oracle is the cold-reviewable artifact at stage-3 round 2 and the checklist C1 grades
the build against — not the author's judgment.

### A.3 Budget

Per-stage **load** (the metric that matters, C3): the ≤40%-of-658 = **263-line** cap.
- Typical stage: SKILL(~110) + one stage file(≤~90) ≈ **≤200 lines** (~30%). ✓
- **Charter-heavy stages 3/6** (round-3 F3-NEW, now bounded): SKILL(~110) + stage-3/6
  file(~40, mostly the pointer + stage-specific bullets) + `charter.md`(~95) ≈ **~245 lines**
  (~37%) — under the 263 cap **because** the charter is a shared reference, not repeated into
  each. (Without the shared file it was ~290 / 44% — over. This is exactly what M1-NEW fixes.)
Both line and token targets recorded per stage at stage 8 (C3(a)). Total line count across
the file set rises (repetition of the small cross-cutting rules) — advisory (C8), not the
target.

## B. Measurement — the A/B battery (C2 + C3-behavioral)

The battery tests what C1 cannot: whether **per-stage isolation** (seeing only `stage-N.md`)
still makes each rule fire. It is organized **by stage**, which is exactly the property under
test — *does each stage file carry everything that stage needs?*

### B.1 Situations (pre-registered; frozen at gate 4)

Five stage situations, each placing an agent at one stage with a case that should trigger
that stage's high-risk rules. The NEW-condition arm is given **only** the router +
`stage-N.md`, so the situation directly tests that file's self-containment.

- **SIT-1.5 (stage 1.5):** a position-sensitive change to spec. Rules: mandatory
  behavior-preservation criterion fires; criteria default-gating.
- **SIT-2 (stage 2):** a change whose effect can't be measured with current instrumentation.
  Rule: *instrument before you build* (plan adds it).
- **SIT-3 (stage 3):** a plan to review that (i) reorders a prompt assembly [position lens],
  (ii) carries a criterion mislabeled gating-as-advisory [label audit], (iii) has one
  genuinely clean lens [*no issue found* valid + *earned-clean-with-citations*], and (iv)
  asks for the review record [provenance: verbatim charter + context list + hashes].
- **SIT-4 (gate 4):** a reviewer verdict of **major** the author wants to wave through
  [route-on-reviewer-severity / no silent demotion]; a route-to-build moment [criteria
  freeze + hash]; unvalidated config paths [path validation blocks gate 4]; and it is the
  **2nd same-class bounce** [iteration cap → stop for human].
- **SIT-6 (stage 6, added round-2 CC-1):** a code diff to review. Rules: **mechanical `git
  diff` against the recorded base [ST6d]** (does the arm generate the reviewed diff
  mechanically vs hand-curate?); **spot-verify a sample of the reviewer's citations [CH6]**;
  the charter's **clean-factual-lens-earned-with-citations [CH5]**. Tests stage-6.md's
  self-containment (the largest file — it carries the full charter), which no other situation
  observes. NEW arm gets only the router + `stage-6.md`.
- **SIT-8 (stage 8):** a gating criterion someone proposes to defer to "live"
  [gating-verified-by-execution: refuse deferral, demand a representative harness or named
  risk-acceptance]; and the run needs its per-gating-criterion **disposition recorded**
  [`decisions.md` gating entry].

Collectively these fire every high-risk rule from C2's list, each at the stage it governs —
including the gate-4+ rules round 1 showed the old arm span could never reach, and the
stage-6 rules round 2 showed were unobserved. **Out of scope (round-2 CC-2):** SIT-0/SIT-1
(low cross-cutting density) get no behavioral situation; C1 still checks that stage-0/1
duties (incl. ST1's "declare touched files") are placed correctly.

### B.2 Conditions & arm protocol (frozen at gate 4)

- **OLD** (n=2/situation): agent given the **current** whole doc. Validity control: the rule
  should fire → proves the situation is valid (OLD doubles as trigger-validity).
- **NEW** (n=3/situation): agent given the router + **only** the routed `stage-N.md`. The
  treatment.
- **BROKEN-NEW** (n=2, on SIT-3/SIT-4/SIT-6/SIT-8 — the multi-rule/stage-6 situations):
  `stage-N.md` with one target rule deliberately deleted. Positive control: the battery MUST
  record that rule as NOT firing → proves it can detect an absent rule (round-1 M3/L2 power
  calibration).
- Arms: cold `general-purpose` / `claude-opus-4-8`; transcript `agent-<id>.jsonl` +
  produced output preserved. **NEW-arm file-open logs are captured** (which files the arm
  Read) → feeds C3(b): a NEW arm must open only the router + its stage file (+ a
  stage-declared reference file).
- Totals: 6 situations × (OLD 2 + NEW 3) + 4 BROKEN-NEW × 2 = 30 + 8 = **38 arms**.

### B.3 Blind grading (frozen at gate 4)

- **One grader per situation** (6), cold `general-purpose` / `claude-opus-4-8`, given that
  situation's arm outputs with **condition labels stripped and IDs randomized** (blind to
  OLD/NEW/BROKEN-NEW) + the frozen per-rule rubric (FIRED / DID NOT FIRE / N-A, each with a
  required quote; the rubric supplies each rule's *definition* so the grader can judge
  firing without the skill files — round-1 A3). Quote-less grade = invalid, re-run once.
- Author spot-checks every grade against the transcript; any dispute that would flip C2's
  pass routes to the **owner** (flip-edge). **6 graders total (one per situation)**
  (round-3 D1-NEW: criteria + plan unified on per-situation grading).

### B.4 Pass condition (C2; pre-committed)

Per (situation, rule): **OLD fires unanimously (2/2)** — the validity bar must be *stricter*
than the treatment bar it certifies (round-2 L-1); OLD < 2/2 = the situation doesn't reliably
trigger the rule → rebuild it (a battery defect, per *an unreviewed check is not a check*, not
a change defect). **BROKEN-NEW does not fire** where run (else the battery lacks detection
power → rebuild). And **NEW fires in ≥2/3 arms**. A rule that OLD fires (2/2) but NEW drops
below 2/3 is investigated and that cell re-run once; a **confirmed** NEW drop is the behavior
regression → **blocker → build**. A single noise-level miss that does not reproduce on re-run
is recorded, not bounced (round-1 L2 noise handling).

## C. Instrumentation (new checks → each validated before its results count)

Signals built as part of this change: `2-rule-oracle.md` (the C1 ground truth); the 38 arm
transcripts + NEW-arm file-open logs; the 6 blind-grader records; the per-stage load table
(C3a). Per *an unreviewed check is not a check* (METHODOLOGY:387-395): the **OLD-arm base
rate** validates each situation genuinely triggers its rules, and the **BROKEN-NEW control**
validates the battery can detect an absent rule — these ARE the battery's pre-trust
validation; the grep-derived oracle gets a cold sanity pass at stage-3 round 2.

## D. Severity → routing

Standard table. Stage-3-round-2 / stage-6 findings route on the **reviewer's** severity. At
stage 8: any C1 unmapped/mis-scoped rule, any confirmed C2 NEW-drop, C3 isolation failure
(NEW arms load everything anyway), C4 (live≠source), C5 (drift), or C6 (dead router row) =
blocker → build. C7/C8 advisory. Iteration cap: 2 same-class bounces at a gate → owner
tie-break (this is bounce #1 at gate 3; round 2 pending).

## E. Concurrency lens — does not fire

No new accessor or read-modify-write window over shared mutable state (document
reorganization). No no-lost-update criterion or accessor enumeration required (METHODOLOGY
*Shared state has more than one accessor* triggers only where the change alters concurrency
structure). Recorded so the omission is deliberate.

## F. Loop from here

Stage-3 **round 2**: cold re-review of the revised {1-spec, 1.5-criteria, 2-plan} +
`2-rule-oracle.md` — four lenses + coverage + position lens + label audit; a resolution
check of round 1's blockers/majors. Route at gate 4; on route-to-build freeze 1.5-criteria
(sha256) + the oracle + the battery design + the file set. Stage 5: build the router + 10
stage files + slimmed METHODOLOGY + the C1 mapping table, from the frozen oracle. Stage 6:
cold review of the built file set vs {1.5, 2, oracle}; mechanical `git diff` against base
`8b4391b`. Gate 7. Stage 8: C1 mapping → C3a load table → C4 diff → C5 consistency → C6
router → the C2/C3b battery (38 arms + 6 blind graders) → per-criterion table → verdict.
Then install, `diff -r` live==source, commit path-scoped to `Guarded_change/`, then the
follow-on dragonfly run.
