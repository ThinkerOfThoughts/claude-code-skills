# 3 — Red-team the plan (ROUND 1) — verbatim record

Cold stage-3 review of {1-spec, 1.5-criteria, 2-plan} against the 4 current dragonfly files the plan
touches. Reviewer: **general-purpose**, model **claude-opus-4-8[1m]**, read-only. Context hashes:
spec `ca730644…`, criteria `e361143f…`, plan `4e171811…`, SKILL `022f4621…`, stage-2 `7bda93a6…`,
stage-8 `dc8fb484…`, METHODOLOGY `44f81a43…` (+ stage-6/stage-7 read as corroborating context).
**Verdict: MAJOR** (1) + 4 minor + 3 nitpick — "not clean, all addressable in plan text without
re-scoping."

## Findings + dispositions (all accepted, fixed in place)

- **[MAJOR] SKILL insertion anchor mis-described** (plan:12 / spec:37 "after the loop table") — the
  region between the loop table and `## Stop-for-human` holds the flagship "**most important gate**"
  paragraph (SKILL:52-57); inserting "after the loop table" would bury it. **→ Fixed:** anchor the
  discipline block **after SKILL:57** ("…escalate to a human."), before `## Stop-for-human`, so the
  flagship paragraph stays adjacent to the table. (Spec:37 didn't carry the bad phrasing; plan did.)
- **[MINOR] T4 one-directional** — no-regression re-runs stages 1/3 arms, but the edited stages are 2/8;
  nothing checked the *reverse* boundary (an in-scope observation still lands in the observation ledger,
  not mis-routed to the parking lot). **→ Fixed:** T1 now presents BOTH an unrelated bug and an in-scope
  observation, asserting each routes correctly (T1 clause (d) + the T1 arm's two-finding scenario).
- **[MINOR] Characterized-exit drop** — surfacing was wired to the diagnosis.md path only; a
  "characterized, not found" / escalation ending (where the hunt didn't nail its symptom — arguably
  where parked findings matter most) could drop the parking lot. **→ Fixed:** stage-8 surfacing bullet
  reworded to fire on ANY exit; T2 now has found + characterized sub-arms.
- **[MINOR] No "when in doubt" tie-breaker** — strict "don't chase" could park a real contributor,
  defeating the coverage sweep. **→ Fixed:** added "when in doubt, treat as in-scope (record in
  observation ledger, let the stage-7 coverage sweep adjudicate) — park only clearly-unrelated
  findings" to the SKILL discipline + stage-2 mechanics + spec behavior.
- **[NITPICK] Cold-start carry-over brief** omits the new ledger. **→ Fixed:** plan adds
  `incidental-ledger.md` to the SKILL:22-27 carry-over list.
- **[NITPICK] Arm model unspecified.** **→ Fixed:** plan §B records the arm model with each grade.

## Reviewer's coverage-challenge / label-audit (verbatim highlights)
- Coverage gaps = the two boundary/exit gaps above (now covered by the T1/T2 fixes). All other
  alterable behaviors observed (T3 additive, T5 budget, T6 live==source, T7 consistency, T8 non-blocking).
- Label audit: **no mislabel**; T5 "arguably advisory kept gating" is a defensible disclosed choice;
  T3 + T8 correctly gating (they guard the additive/focus-protecting core promise).
- Verified as earned: the "residual is `S#`-related by definition" premise is true (stage-7.md:32-37,
  A-7-5); the load budget holds with wide margin (worst stage load 227 ≤ 270); "never blocks the cap"
  is consistent with stage-6 (a cycle = a discriminating test run+recorded; an incidental log is neither).

→ Gate 4 round 1: MAJOR → back to stage 2 (plan fixed in place), then round-2 re-review (the tie-breaker
+ characterized-exit add NEW text worth a cold look). See `decisions.md`.
