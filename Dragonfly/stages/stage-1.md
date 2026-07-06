# Stage 1 — Reproduction

**What this stage does:** turn the reported repro steps into a reliable, **representative**
reproduction *before* any hypothesizing. The repro is a diagnostic artifact, so it is red-teamed (via
the triage) before it is trusted.

**Read `stages/charter.md`** for the full red-team charter (four lenses + discipline + provenance +
severity) — the triage's guarded-change/lite pass each repro is routed through *is* its stage-1 cold
review.

## Procedure

- **Turn the `R#` steps into a reliable, *representative* repro BEFORE hypothesizing** (A-1-1).
- **A "reproduction" that doesn't demonstrably reproduce a named `S#` is not a reproduction** (A-1-2)
  and may not anchor the hunt.
- **Intermittent → instrument-to-capture** (A-1-3): a genuinely un-reproducible bug routes to
  instrument-to-capture, which carries its own evidentiary bar (below); "label it intermittent" is not
  an escape.
- The repro is a **diagnostic artifact → triage** it (below) before trusting it.

**Repro-ordering escape (an exception, recorded) (A-1-4).** When a faithful repro cannot be built blind
(intermittent / load-dependent / emergent), hypotheses MAY be formed first to inform repro/instrument
design, **provided** the inversion is recorded in `decisions.md` **naming the infeasibility class**,
and every such hypothesis stays `ungated` (B-GBP-1); the representativeness gate still binds the
resulting repro/instrument before any conclusion.

## The representativeness gate (mandatory, blocking, non-waivable)

- **A diagnostic artifact is untrusted until a control run is shown to actually exhibit the symptom**
  (B-REP-1). Reject and redesign any whose control does not. This is the cheapest catch for the
  founding failure (a test that doesn't test the thing); it is not waivable.
- **The instrument-to-capture path does not escape the gate; it satisfies it differently** (B-REP-2):
  the instrument must be **shown to capture the symptom on a run where the symptom is known to have
  occurred** (replayed against a recorded failing trace, or validated on a forced/seeded instance)
  before any reading it produces is trusted.
- **A detector/readout is itself a diagnostic artifact** (B-REP-3): anything that *decides* "the
  symptom occurred" (a classifier, a grep, a threshold rule) must be shown to **fire on a known-true
  instance AND stay silent on a known-clean one** (evidenced by an observation-ledger row) before any
  reading it produces is consumed.

## Diagnostic-artifact triage (every repro / test / instrument / toggle / detector)

**Every diagnostic artifact runs through guarded-change before it is trusted** (B-TRI-1). The triage
decides which form, **in priority order** (B-TRI-2):
1. **Consumes tokens/credits to run** (spawns an agent/CLI, hits an LLM API) → **full guarded-change**
   (overrides size — a wrong token-burning test is expensive twice).
2. Else **multi-file / mutates state / non-obvious correctness** → **full guarded-change**.
3. Else **single self-contained read-only script (~≤50 lines, no state)** → **guarded-change-lite**.
4. **In doubt → full.**

**The triage result is recorded in `decisions.md`** — unrecorded = it didn't happen, the artifact stays
untrusted (B-TRI-3).

**guarded-change-lite (C-LITE-1)** is a **single cold red-team pass of the artifact** — using
dragonfly's own charter (`stages/charter.md`: four lenses + evidence discipline) — against a one-line
intent + a checkable "does exactly X and exercises path P" criterion → fix → run. **It keeps the
charter AND the provenance record** (C-LITE-2), dropping only the surrounding scaffolding (spec /
criteria / plan / baseline / regression). Full cases invoke the guarded-change skill directly. A lite
pass records, minimally, the artifact, the one-line intent + criterion, the verdict, and where the
verbatim output lives, in `decisions.md`.
