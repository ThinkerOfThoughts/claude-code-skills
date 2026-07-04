# 6b — Targeted cold check of the stage-8 harness scripts

## Provenance

- **Charter given (verbatim):** "You are a cold, independent reviewer with no shared context
  with the author. Report the sha256 of each context file you read. This is a targeted,
  narrow check of the four harness scripts the stage-8 verification run uses; check the
  scripts, not the change. Discipline: cite a file:line or a concrete failure scenario for
  every finding; rank every finding blocker/major/minor/nitpick; flag anything you could not
  verify rather than silently accepting it; 'no issue found' is allowed and expected when
  true; a clean verdict is only valid if you show the specific source evidence you consulted
  (file:line) — a clean verdict with zero citations is treated as an un-run review; audit any
  criterion labels touched by your scope — every advisory label needs a legitimate reason and
  every gating 'verified = yes' must have exercised the path the criterion governs; a sample
  of your cited lines will be spot-verified. Task addition (quoted as such): 'check that the
  four harness scripts — the C1 mock script, the C3 dedup mock script, the C4 line-count
  audit, and the regression dry-run — represent the criteria's governed paths, and that the
  guarded cases fail against the pre-change uploader.'"
- **Context given (exact list):** `harness/c1_mock.py`, `harness/c3_dedup_mock.py`,
  `harness/c4_linecount.sh`, `harness/regression_dryrun.sh`, `export/uploader.py`
  (post-change), `export/uploader.py` at pre-change `4c1f2aa` (for the unguarded runs),
  `export/tests/test_uploader.py`, `1.5-criteria.md`, `2-plan.md`.
- **Context file hashes (reviewer-reported):** c1_mock.py `2a77c9e4…`, c3_dedup_mock.py
  `b30f5a18…`, c4_linecount.sh `e6d2041b…`, regression_dryrun.sh `19c8f3d7…`, uploader.py
  `9e10f2c7…`, uploader.py@4c1f2aa `c51e07b3…`, test_uploader.py `77ab03d1…`, 1.5-criteria.md
  `6364136da75e…`, 2-plan.md `9b6954b5…`.
- **Reviewer:** cold subagent, general-purpose, model claude-opus-4-8.
- **Reviewer output (verbatim, in full below).**

## Reviewer output

Representativeness: the C1 mock script's 503-503-200 and 404 branches (`c1_mock.py:22-41`)
drive the retry-decision path C1 governs (`uploader.py:52-58`); the C3 dedup script's
commit-then-503 branch (`c3_dedup_mock.py:19-33`) is exactly the succeeded-server-side case
C3 names; the C4 line-count audit greps the `retry` log lines the plan's instrumentation adds
(`c4_linecount.sh:6`); the regression dry-run replays the full nightly manifest end-to-end
(`regression_dryrun.sh:3-12`). All four exercise the paths their criteria govern. Flagged as
unverifiable from this context: the real backend's consistency model — the mock commits and
serves HEAD from the same in-process store (`c3_dedup_mock.py:19-33`), strongly consistent
by construction, so these scripts cannot show whether the real backend's HEAD-after-PUT
behaves the same.

Fail-against-unguarded, both guards: the C3 dedup script run against the pre-change uploader
at `4c1f2aa` stores the object twice (`harness-out/c3-unguarded.log`: "stored_copies=2") —
the check fails without the guard. The C1 script against the pre-change uploader aborts on
the first 503, no retry fired (`harness-out/c1-unguarded.log`: single attempt, exit 1). Both
logs are pre-change FAILURE demonstrations only — they are not evidence for any post-change
result; the stage-8 table records those separately.

Scope notes: C2 has no harness script (its row is not exercised pre-ship) — outside this
check's scope. Label audit within scope: C4's advisory label holds (operator convenience,
`1.5-criteria.md:8`); no gating 'verified = yes' claims exist among the scripts themselves.

Bottom line: no issue found — worst severity: none (one unverifiable item flagged above: a
scope limit of the mock, not a script defect). The four scripts are representative and both
guarded cases fail against the pre-change uploader. Fit for stage-8 use.
