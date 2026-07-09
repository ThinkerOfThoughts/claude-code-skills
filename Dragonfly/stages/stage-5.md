# Stage 5 — Run & record

**What this stage does:** run the discriminating test, record its result, and update hypothesis
statuses — but only *consume* the result once the artifact's triage is recorded passed.

## Procedure

- **Run the test; record the result in the observation ledger; update hypothesis statuses; cite the
  evidence** (A-5-1). A confirmed/refuted status is a claim — it cites the run that earned it.

## Cross-cutting rules governing this stage

**Trust-before-gate ordering (B-TBG-1).** A result may **not be consumed** by a later stage — to
eliminate a hypothesis, advance a gate marker, or inform the human — until the producing artifact's
**triage is recorded as passed** in `decisions.md`. Consuming a reading before its cold review is
recorded is the trust-before-gate slip; the triage is a precondition of trust, not a later audit. (The
same precedence binds any later stage that consumes this reading — 6, 7 — not only stage 5.)

**Evidence over rhetoric (B-EVID-1).** The recorded result cites the run / log row / file:line that
earned it. "Seems like X" is not a finding.

**A surprising resource signal is a tell, not just a number (B-COST-1).** When a run's cost, token
burn, latency, or call-count comes back **surprising** (much higher/lower/different than the design
implies), treat it as a **fidelity question** — "does my implementation match the intended design?" —
and investigate the surprise before recording the result as trusted. The surprise is often the first
evidence that the instrument is the wrong *kind* of thing (see B-FID-1); reporting the number without
asking why is how a mismatched instrument's readings get consumed. (Motivating case: a ~$31 run cost
exposed a stateless-`claude -p` instrument standing in for a specified agent.)

**A negative result is untrusted until its arm is shown able to exhibit the symptom at these
parameters (B-REP-4).** A "clean / no-symptom" result may **not eliminate a hypothesis** unless the
producing arm was shown to **exhibit the symptom under the same-or-weaker parameters** (length, scale,
load, conditions) than the run that came back clean — "clean at 7 turns" is trusted only if that arm
exhibited the symptom at ≤7 turns, **evidenced by an observation-ledger row** (a control run, per
B-REP-3), not by a design assertion. **Parameters are not a single axis:** every axis the arm varies
(length AND volatility AND state) must be same-or-weaker; if the arm is weaker on one axis but stronger
on another it does **not** qualify — record it as untrusted-negative. Otherwise record it as an
**untrusted-negative**: it neither eliminates a hypothesis nor counts toward convergence. This is the
representativeness gate (B-REP-1) applied at result-recording, not only at design — a control that
could not have produced the symptom proves nothing by its absence.

**As-run must match as-designed, or the deviation is recorded and the result re-scoped (B-REG-1).**
Before a result is trusted, check that the test's **executed parameters** (sample size, stop rule,
scale, conditions) match the **pre-registered design registered at stage 4 (A-4-2, in `decisions.md`)**.
If they diverge (the registered design said 100 turns / +20-on-trigger and the run used 7–13), record
the deviation in the observation ledger (it is a finding about the run) and **re-scope what the result
can support** before consuming it — a result gathered under different parameters than designed does not
answer the question the design posed. **A run with no registered design to compare against is itself
the defect** (A-4-2 was skipped) — it is not a pass by default. Silent drift from the registered design
is a trust defect, not a detail.
