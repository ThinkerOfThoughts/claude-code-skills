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
