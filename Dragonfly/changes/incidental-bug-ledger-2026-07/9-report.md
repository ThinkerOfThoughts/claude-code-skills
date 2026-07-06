# 9-report.md — the incidental-bug ledger (dragonfly Theme 3): outcome

## What shipped

Dragonfly gains an **incidental-bug ledger** — an append-only parking lot where a hunt records any
potential bug it notices that is **unrelated to the symptom under investigation**, **without chasing
it** (focus protection), surfaced at the handoff for future, separately-scoped hunts. Additive, four
touched files:

- **`SKILL.md`** — a concise always-loaded "Incidental findings" discipline (park clearly-unrelated
  findings, don't chase, **when in doubt treat as in-scope**), anchored after the flagship gate
  paragraph; `incidental-ledger.md` added to the ledger list + the cold-start carry-over brief.
- **`stages/stage-2.md`** — the recording mechanics: incidental findings go to the *separate*
  `incidental-ledger.md`, not the observation ledger; the when-in-doubt→in-scope tie-breaker.
- **`stages/stage-8.md`** — surface the parking lot on **either** terminal verdict (found *or*
  characterized), distinct from the diagnosed root cause + its S#-related residuals, not routed to
  guarded-change.
- **`METHODOLOGY.md`** — `incidental-ledger.md` in the artifacts list + the config `ledgers.dir` note.

## Why (the motivation)

Dragonfly hunts kept surfacing unrelated bugs as a side effect of examining the code (the flagship
probe, the gc-battery arms, both restructure runs). With no parking lot, the agent either chased them
(breaking focus, burning the convergence budget on a non-symptom bug) or dropped them (losing the
observation). The ledger gives out-of-scope findings a home without pulling the hunt off its `S#`.

## Outcome — accepted, additive & non-regressing

Driven through a **lean** guarded-change loop (owner-scaled to a small additive change): 2 stage-3
plan-review rounds + a stage-6 code review + a stage-8 5-arm conformance harness.

- **The plan review earned its keep** even here: round 1 (MAJOR) caught a position error (the insertion
  anchor would have buried the "most important gate" paragraph) plus the reverse-routing boundary, the
  characterized-exit drop, and the missing "when in doubt → in-scope" tie-breaker; round 2 caught a
  factual overreach (a phantom third terminal exit — the skill has exactly two verdicts). All fixed.
- **Stage 6: CLEAN** — the build is faithful and genuinely additive-only (all diff "deletions"
  confirmed re-wraps; the flagship paragraph intact and adjacent to the loop table; no neighbouring
  rule diluted).
- **Stage 8: 5/5 arms FIRED** — the feature fires in **both** routing directions (park the unrelated
  bug / keep the in-scope observation) and on **both** terminal verdicts (found + characterized); and
  the two pre-existing rules most adjacent to the change (representativeness gate, gate-before-present)
  still fire → no regression. Live == source; per-stage load 237 ≤ 270.

## Residuals / follow-ups (not blocking)

- **Ledger scope is deliberately raw.** The parking lot is a surfaced list, not triaged/ranked and not
  routed to guarded-change — each incidental bug is a future hunt of its own if pursued. (One arm noted
  a security-severity incidental would warrant prominent flagging to the human at handoff — a fine
  judgment call the surfacing rule already permits, not a rule gap.)
- **The first real hunts under the amended skill are the true test** of whether agents log-and-move-on
  in practice (the 5 arms are strong evidence, but they are prompted at the trigger point). Watch the
  early ones.

## Sequencing

This completes the three-theme skills initiative: guarded-change Theme-1 restructure (`3d6889b`),
dragonfly Themes-1+2 restructure+untangle (`4372f73`), and now dragonfly Theme-3 incidental-bug ledger.
Both skills are file-per-stage; dragonfly is self-contained and now carries the parking lot.
