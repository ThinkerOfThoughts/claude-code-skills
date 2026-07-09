# Stage 4 — Discriminating test (gated)

**What this stage does:** design a test or instrument that *splits* the live hypotheses. Before it
runs, it passes the representativeness gate and the triage — so no conclusion rests on a test that
doesn't test the thing.

**Read `stages/charter.md`** for the full red-team charter — the triage's guarded-change/lite pass each
test is routed through *is* its stage-4 cold review.

## Procedure

- **Design a test/instrument that splits the live hypotheses** (rules at least one in or out) (A-4-1).
- **Register the design as a checkable object (A-4-2).** When the test/instrument is designed, record
  its **parameters** — sample size / number of runs, the **stop rule** (e.g. "100 turns, or +20 on
  first trigger"), scale, and the conditions each arm holds — in **`decisions.md`** (the design-time
  record, alongside the triage result per B-TRI-3 — the observation ledger is for things *examined*,
  not forward-looking design) as the **pre-registered design**. This is the object stage-5's B-REG-1
  checks the executed run against; a design with no registered parameters cannot later be shown to
  have been run faithfully.
- **Before it is run** it passes the **representativeness gate** and the **diagnostic-artifact triage**
  (both below). A result may not be **consumed** until its triage is recorded passed (trust-before-gate,
  below).

## The representativeness gate (mandatory, blocking, non-waivable)

- **A diagnostic artifact is untrusted until a control run is shown to actually exhibit the symptom**
  (B-REP-1). Reject and redesign any whose control does not — non-waivable.
- **The instrument-to-capture path does not escape the gate; it satisfies it differently** (B-REP-2):
  the instrument must be shown to capture the symptom on a run where the symptom is known to have
  occurred before any reading it produces is trusted.
- **A detector/readout is itself a diagnostic artifact** (B-REP-3): anything deciding "the symptom
  occurred" must **fire on a known-true instance AND stay silent on a known-clean one** (ledger row)
  before its readings are consumed.
- **The gate binds again at result-recording (B-REP-4, stage 5):** passing the design-time gate here
  does not discharge it — a "clean" result is re-checked at stage 5 against whether this arm could
  exhibit the symptom at the parameters it actually ran.

## Diagnostic-artifact triage (every repro / test / instrument / toggle / detector)

**Every diagnostic artifact runs through guarded-change before it is trusted** (B-TRI-1), **in priority
order** (B-TRI-2): (1) consumes tokens/credits → **full guarded-change** (overrides size); (2)
multi-file / mutates state / non-obvious → **full guarded-change**; (3) single self-contained read-only
(~≤50 lines, no state) → **guarded-change-lite**; (4) in doubt → **full**. **The result is recorded in
`decisions.md`** — unrecorded = it didn't happen (B-TRI-3).

**guarded-change-lite (C-LITE-1)** is a **single cold red-team pass** using dragonfly's own charter
(`stages/charter.md`) against a one-line intent + a "does exactly X, exercises path P" criterion → fix
→ run. **It keeps the charter AND the provenance record** (C-LITE-2), dropping only the spec / criteria
/ plan / baseline / regression scaffolding; full cases invoke the guarded-change skill directly;
recorded minimally in `decisions.md`.

## Cross-cutting rules governing this stage

**Trust-before-gate ordering (B-TBG-1).** The triage (representativeness gate + cold review) must pass
**before** the artifact is run; and its output may not be **consumed by a later stage** — to eliminate
a hypothesis, advance a gate marker, or inform the human — until that triage is **recorded as passed**
in `decisions.md`. Gate first, then consume; the triage is a precondition of trust, not a later audit.
