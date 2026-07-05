# Stage 0 — Baseline

**What this stage does:** snapshot the current measurable behavior of an existing system, so
stage 8 can check for regressions against it.

## Procedure

**Baseline** — only if a prior version exists *and* the config defines `measurement.baseline`.
Run the project's baseline-capture (from config) and store the measured metrics in
`0-baseline.md`. Otherwise note "greenfield / no baseline → stage 8 conformance-only" and skip.

## Rules governing this stage

**Baseline only when modifying an existing system (ST0).** Run the project's baseline-capture
(from config) and store the measured metrics. Greenfield projects skip this; stage 8 then
runs conformance-only.

**Criteria are mandatory; baseline is optional (CFG5).** No criteria → the loop won't pass
stage 3. No baseline → stage 8 runs conformance-only and says so.
