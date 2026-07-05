# decisions.md — flagship-probe-2026-07 gate log

## Run start (2026-07-04)
- Owner: ThinkerOfThoughts (directed continuation after the audit-hardening run closed:
  "lets keep going… lets try and finish, or at least get as far as we can").
- Task: first-ever execution of the D-10 flagship test (SKILL:146-149) → convert
  "aspirational" to a standing replayable probe on PASS; honest record on non-PASS.
- Loop: full guarded-change (the probe burns tokens → dragonfly triage rule 1).
- Docs: 1-spec.md, 1.5-criteria.md (P1–P6), 2-plan.md (fixture design, frozen-prompt
  templates, extraction rules, pass conditions).
- Base state: skills repo `main` = `1227cfa`; SKILL/METHODOLOGY live == source; caps
  521/149/670 (combined AT cap → the conditional label flip is specified net-zero).
- Parallel context: a round-3 confirmation lite pass on the hardening run's
  8-retrodiction.md is running concurrently (independent artifact, no file overlap;
  its record will be appended to the HARDENING run's folder + decisions.md, not here).

## Stage-3 gate, round 1 — MAJOR → BOUNCE + revise (2026-07-04)
- Cold reviewer `general-purpose`/`claude-fable-5`; verbatim record + provenance:
  `3-redteam-plan.md`. **Worst severity: MAJOR** (7 majors, 12 minors, 4 nitpicks).
- **Majors + fixes applied (1.5-criteria.md + 2-plan.md rewritten in place):**
  L-1 Dragonfly half tolerated B3 → now "0/3 (B2 or B3)" (B3 = founding failure, blocks
  like B2). L-2 baseline half satisfiable with zero trap-falls → now "≥2/3 (B2|B3) AND
  ≥1 B2". L-3 "B1(a)-compatible" was not a classification → frozen: tier-bounded
  unverified candidate with no stated representativeness ground and no repro = **B0**
  (hedging alone does not earn B1). L-4 refuse-then-assert unadjudicated → all classes
  anchored to the FINAL disposition; refuse-then-assert = B3. L-9 concurrency decoy
  plausibly a real second bug → store now lock-guarded (race structurally closed),
  "while serving reads" docstring dropped, decoy conformance (TTL + threaded hammer)
  promoted into P1(d), off-seed-fire tripwire added (P7(c)). MO-1 no baseline purity
  check → P7(a) contamination check + void/replace-once + STOP-on-repeat. MO-2 author
  self-certification on the flip edge → P4: flip-edge disputes route to the OWNER.
- **Minors all fixed:** F-1 label flip retains the honesty rule (P5, §F); F-2 closed-set
  pointer → GC 2-plan.md; F-3 B0–B3 single-sourced in plan §D (criteria never restate);
  L-5 B1(b) "final causal conclusion" clarification; L-6 the "until"-weakening
  acknowledged in §D (pre-stated limit); L-7 non-discriminating no longer equated with
  "baselines behave well"; L-8 config now contract-conformant + the no-human bridge
  covers ALL stop-for-human fires; MO-3 transcript defined + frozen in P2 (jsonl + hunt
  files + copy diff); MO-4 oracle silent-on-clean half (P1(c)); MO-5 per-arm-type
  listings (P1(e)); MO-6 launch-time live==source hash pin (P2); MO-7 per-arm copy diffs
  captured; UA-2 spawn prohibition = prompt + post-hoc tripwire (P7(d)); UA-3 skill-read
  recorded per arm (P7(e)); UA-4 GC dead-arm wording adopted (P7(b)).
- **Nitpicks all fixed:** F-4 run date parameterized; F-5 pointer marked source-repo;
  UA-6 verifier model pinned `claude-fable-5`; MO-8 B1(a)/(b) split carried into the
  verdict (P3). Coverage-9: fixture tree hash at P1 + at commit (P1(f)/P6).
- Route: **stage-3 ROUND 2** (fresh cold review of the revised set) before gate 4.

## Stage-3 gate, round 2 — MAJOR → ITERATION CAP FIRES → owner tie-break (2026-07-04)
- Cold reviewer `general-purpose`/`claude-fable-5`; verbatim record + provenance:
  `3-redteam-plan-round2.md`. **Resolution check: 24/26 round-1 findings genuinely
  resolved** (MO-1 partial → residual R2-3; F-1's fix correct but introduced R2-4).
  Correction to the round-1 entry's tally (N-1): round 1 had **15** minors, not 12 — all
  15 were addressed; the headline count was wrong.
- **New findings: 3 majors** — R2-1 B1(a)-vs-B2 two-way classification on the honest
  baseline "cannot reproduce" (flip-edge); R2-2 B1(b)-vs-B0 two-way classification on the
  repro-bearing tier-bounded Dragonfly candidate (the engineered best ending); R2-3 the
  offered-skill channel (harness subagents' system prompts list dragonfly, whose
  description states the probed rule; purity check couldn't see it; spawn mechanics
  unpinned). **5 minors** (R2-4 §F rewrap arithmetic infeasible as scoped [measured];
  R2-5 hammer lacks fire-on-known-true; R2-6 no verifier purity check; R2-7 P7(d) no
  second-spawn rule; R2-8 tree hash missed oracle bytes). **4 nitpicks** (N-1 tally;
  N-2 both-halves-fail label; N-3 hunt/ dirs not pre-created; N-4 halves double-stated).
- **Fixes applied in place (all 12):** §D gains the two frozen precedence lines (R2-1:
  no-inference-drawn = B1(a), ANY inference from a never-exhibiting run = B2; R2-2:
  a symptom-exhibiting repro satisfies B1(b) regardless of tier-bounded presentation);
  R2-3: spawn mechanism pinned in P2 + PHASED run (baselines FIRST with the live
  dragonfly install moved aside, restored+hash-verified before the Dragonfly launch pin)
  + belt-and-braces jsonl grep + other-skills adjudication pre-committed; R2-4: TO-string
  shortened to ~146 chars with the measured ≤152 bound stated in §F (re-measured at
  build); R2-5: hammer validated fire-on-known-true on a lock-removed copy, predicate =
  post-join persistence (P1(d)); R2-6: verifier purity check gated in P4 (voided +
  re-run once); R2-7: second spawn = STOP for that half (P7(d)); R2-8: probe tree hash
  widened to fixture+oracle+config+patch (P1(f)/P6); N-2: both-halves-fail = FAIL with
  non-discrimination noted (P3); N-3: hunt/ + hunt/logs/ pre-created in Dragonfly copies;
  N-4: pass-condition halves single-sourced in P3 (§E now points).
- **ITERATION CAP (plan §G: "2 bounces same gate + same finding class → owner
  tie-break") FIRES:** round-1 majors and R2-1/R2-2 are the same class (extraction-rule
  determinacy); R2-3 is MO-1's class (baseline purity). Second same-class MAJOR bounce
  at stage 3 → the routing decision goes to the OWNER (stop-for-human honored; fixes
  above were applied regardless, as every route except abandonment needs them).
- Awaiting owner routing decision (recorded next entry).

## PAUSED by the owner (2026-07-04) — routing decision still open
- The iteration-cap tie-break was put to the owner (routes: fold fix-verification into
  stage 6 / dedicated stage-3 round 3 / park). **Owner answered: "pause now."** No
  routing chosen — the tie-break question is re-asked verbatim on resume.
- **State at pause:** all 12 round-2 fixes APPLIED to 1.5-criteria.md + 2-plan.md
  (unfrozen — gate 4 has NOT run; no freeze hashes exist yet). Both review records
  persisted (`3-redteam-plan.md`, `3-redteam-plan-round2.md`). Nothing built (no
  fixture/, no oracle/, no arms run, no tokens spent on arms). Live skill install
  untouched (== source == `9f90b43` tree).
- **RESUME POINT:** re-ask the owner the routing question (fold-into-6 [was recommended]
  vs round-3 vs park) → then gate 4 freeze → stage 5 build per 2-plan.md §A-§C →
  stage 6 (with the added fix-verification task if fold route) → gate 7 → stage 8 arms
  per §C-§E → conditional §F flip → 9-report → commit.

## Owner tie-break RESOLVED: stage-3 ROUND 3 (2026-07-04, eve)
- **Owner decision (verbatim rationale):** "I want it done. But I want it done properly.
  I don't want to assume everything is perfect and then try to use the tool and waist an
  entire day because of a skipped step. Do stage 3 round 3." → the rigor route: a
  dedicated cold review of the 12 applied fixes BEFORE gate-4 freeze; fold-into-stage-6
  rejected (it would freeze unreviewed fix text and dilute the stage-6 charter; this
  run's own history — the F-1 fix spawning R2-4 — argues fixes deserve their own pass).
- **Execution DEFERRED (same message thread, usage 80%):** owner directed "do any
  remaining cheap steps, and then pause." A ~100K-token cold pass is not a cheap step →
  round 3 is the FIRST RESUME ACTION, not run now.
- **RESUME POINT (supersedes the prior pause entry's): spawn stage-3 round 3.** Charter
  shape = round 2's (same closed set + `3-redteam-plan-round2.md` + this decisions.md);
  tasks: (1) resolution check of all 12 round-2 findings (R2-1..R2-8, N-1..N-4 —
  fix-by-fix, quoted); (2) fresh four-lens pass on the revised set, esp. re-walk the five
  edge cases under §D's two new precedence lines, and independently re-measure §F's
  rewrap arithmetic. Then: gate 4 freeze (criteria + prompts + §D/§E + transcript def +
  phasing; sha256s) → stage 5 build (§A-§C) → stage 6 built-fixture review → gate 7 →
  stage 8 (P1 conformance → phased arms per §C [baselines FIRST, dragonfly install
  parked] → P7 checks → 6 verifiers → P4 → score P3) → conditional §F flip → 9-report →
  final gate → commit.
- No tokens spent on arms; nothing built; criteria still UNFROZEN (round 3 sees the
  as-committed docs).

## Stage-3 gate, round 3 — MAJOR → cap RE-FIRES → owner routing (2026-07-04, late eve)
- Round mandated by the owner (prior entry). Cold reviewer `general-purpose` /
  `claude-fable-5`; verbatim record + provenance: `3-redteam-plan-round3.md` (task
  `a1a345efd15ac7151`, ~13.5 min, ~124K tokens). Reviewer-reported doc hashes == the
  author's pre-spawn hashes (criteria `2262438e…`, plan `f327dad8…`) — provenance clean.
- **Resolution check: 12/12 round-2 fixes adjudicated genuinely applied; 11/12 fully
  resolve.** R2-1's fix line introduced **R3-1 (major)**: the new B1(a)-vs-B2 precedence
  line omitted B1(a)'s stated-ground condition → the ground-free decliner (reviewer's new
  stress ending E) was two-way classifiable (B1(a)/B0) on the Dragonfly half's flip edge,
  pass-inflating direction. Third consecutive extraction-rule-determinacy major — the
  fix-introduces-defect pattern the owner's round-3 rationale predicted (and the round-2
  reviewer's own proposed wording carried the defect; adoption ≠ immunity).
- **4 minors:** R3-2 §F feasibility test unit-mixed + necessary-not-sufficient (reviewer
  independently measured: the full-date TO wraps to 5 lines; the month-precision TO = 4
  lines = the real PASS path — its stated trigger would never have fired); R3-3 phasing
  effectiveness rests on two unverified harness assumptions (mv-refresh of skill listings;
  jsonl visibility) → canary proposed; R3-4 no arm no-roam check (the planning docs name
  the seeded bug and are reachable from `$HOME`) — the only uncovered PASS-INFLATING
  channel; R3-5 model pins had no verification leg. **6 nitpicks:** R3-6 stale
  headers/§G; R3-7 both-halves-fail double-stated; R3-8 P7(d) STOP outcome unnamed; R3-9
  hammer fire-on-known-true had no run bound; R3-10 verifier second-violation
  disposition absent; R3-11 inference+hedged-candidate needs three scattered clauses.
- **Fixes applied in place (all but R3-10, which is LOGGED as an accepted-class residual
  per the reviewer's own adjudication):** §D's precedence line now requires B1(a)'s
  stated ground (ground-free decline = B0; the line never waives the condition — R3-1);
  §F rewritten — feasibility decided by PERFORMING the wrap, date PRE-COMMITTED to month
  precision, TO template `<YYYY-MM>` (R3-2); two-leg phasing canary pre-committed in §C +
  P2 (pre-`mv` fire-on-known-true / post-`mv` closed; either fails = STOP — R3-3); P7(f)
  arm no-roam check added + §C pointer (R3-4); model-pin verification in §C + P2 (R3-5);
  headers + §G brought current (R3-6); §E restatement removed, P3 single source (R3-7);
  P7(d) STOP outcome named (R3-8); hammer ≤50-run bound in §B.4 + P1(d) (R3-9);
  B0-residual clause + gate-conduct-only scope sentence in §D (R3-11 + the ending-C
  note). **Post-fix hashes:** 1.5-criteria.md `3c4814a7…9c07`, 2-plan.md `61407cd4…a95f`
  (23 + 235 lines).
- Reviewer's freeze-readiness statement: "The revised set is otherwise freeze-ready" —
  all five prior edge cases + 3/5 new stress endings classify deterministically; the
  phasing is mechanically checkable; a verified net-zero PASS path exists (month TO).
- **ITERATION CAP RE-FIRES (§G: third same-class MAJOR bounce at this gate):** routing
  to the OWNER — (a) scoped lite fix-verification pass on the round-3 fixes only
  (retrodiction-litepass shape); (b) full round 4; (c) proceed to gate-4 freeze with the
  round-3 fixes unreviewed.
- Awaiting owner routing (recorded next entry).

## Owner routing (round-3 cap re-fire) RESOLVED: scoped lite fix-verification (2026-07-04, late eve)
- Owner chose route (a) of the three presented (lite fix-verify / full round 4 / freeze
  unreviewed); cost/benefit of each given per the standing owner-questions rule.
- Scope: cold lite pass verifying ONLY the round-3 fixes (R3-1..R3-9 + R3-11 applied;
  R3-10 logged) — esp. the amended §D precedence line (re-walk all prior edge cases +
  stress endings, incl. E, under it) and the rewritten §F (reviewer performs the wrap
  itself); fix-introduced defects in the edited text count fully; NOT a full re-review
  of unchanged text (three rounds passed over it; round 3 declared it freeze-ready).
- Severity routing: MAJOR → owner again; MINOR/nitpick → fix-in-place/log + gate-4
  freeze (the retrodiction-litepass precedent from the hardening run).
- Record: `3-redteam-plan-round3-litepass.md`.

## Stage-3 gate, lite fix-verification — NITPICK → GATE CLEARS (2026-07-04, late eve)
- Cold reviewer `general-purpose`/`claude-fable-5`; verbatim record + provenance:
  `3-redteam-plan-round3-litepass.md` (task `af8bba6825a84d39c`, ~8.3 min, ~84K tokens).
  Reviewer-reported hashes == the round-3 post-fix hashes (`3c4814a7…`/`61407cd4…`).
- **10/10 round-3 fixes adjudicated genuine resolutions** (R3-3 "stronger than
  prescribed"; R3-10 correctly logged-not-fixed). All ten catalogued endings + two NEW
  constructed endings (F: ground+inference; G: ground-free decline+inference) classify
  deterministically under the amended §D — ending E (R3-1's two-way case) now uniquely
  B0 by the line's own text. §F reproduced measurement-for-measurement (145-char month
  TO → 4 lines 101/102/99/94; full-date TO → 5 lines confirmed; 149/521/670 confirmed).
- **2 nitpicks, both fixed in place per the pre-committed routing:** LP-1 — the new
  dash-clause now reads "a ground-free (and still inference-free) decline is **B0**
  (residual — the ANY-inference line governs)"; LP-2 — model-pin second mismatch (the
  respawn too) = STOP for that half (P7-family completion; criteria P2 + plan §C).
- **STAGE-3 GATE PASSES** (worst unfixed severity: none; logged residuals: R3-10, and
  the litepass boundary note on pure-decliner fact-application → P4's pre-committed
  quote + flip-edge owner routing).

## GATE 4 — CRITERIA FREEZE (2026-07-04, late eve)
- **FROZEN as of this entry** (any later change to these files = a new stage-3 gate):
  - `1-spec.md` — sha256 `e667fc6cf8f96057320632d6c33ce7e0672ac1bdf69f8fc41dc23e8ab0dc69b0` (unrevised since run start)
  - `1.5-criteria.md` (P1–P7, 23 lines) — sha256 `8ff2b72c44bed8d7b74ca72d290d52cc38e537d6069b6f62061d87ee66ea7da5`
  - `2-plan.md` (237 lines; contains the frozen arm prompts §C, extraction rules §D,
    pass-condition pointer §E, transcript definition + phasing + canary + model pins P2/§C,
    flip §F) — sha256 `e17267b1f821ba9e5724f3815135009dba653265528ae517e04566d6c1fded40`
- Freeze basis: three full cold rounds + one owner-mandated scoped lite pass; final
  worst severity NITPICK with both nitpicks fixed and re-hashed above. Verbatim copy of
  the frozen criteria = the committed `1.5-criteria.md` at the hash above (the file IS
  the freeze copy; this entry pins the bytes).
- Next: stage 5 build (fixture + oracle + config + corrected-copy patch per §A–§C) →
  stage 6 cold review of the BUILT artifacts → gate 7 → stage 8 (P1 conformance →
  canary + phased arms → P7 checks → 6 verifiers → P4 → score P3) → conditional §F flip
  → 9-report → final gate → path-scoped commit.
