# Stage 2 — Plan

**What this stage does:** define how to build the change — complete only when it also specifies
measurement, instrumentation, and thresholds.

## Procedure

Write `2-plan.md`: how, **plus** measurement (how each criterion will be verified),
instrumentation (add to scope if a needed signal is absent), and severity→routing thresholds +
which metrics are gating vs. advisory. A plan missing these is incomplete. If the change
introduces a new accessor or read-modify-write window over shared mutable state, the plan must
enumerate every concurrent accessor and state which the guard covers vs. leaves out.

## Rules governing this stage

**Instrument before you build (CP3).** If a change's effect can't be measured, the plan is
incomplete. The measurement and any new instrumentation are part of the plan, not an
afterthought. (This is the rule that would have made missing telemetry impossible.)

**Plan = how + measurement + instrumentation + thresholds (ST2a).** How to build it, complete
only when it also names: how each criterion will be measured; what instrumentation must exist
to measure it (and adds it to scope if absent); and the thresholds that map findings to loop
routing.

**Concurrency change → plan enumerates every accessor + which the guard covers (ST2b, fires
only when the change introduces a new accessor or read-modify-write window over shared mutable
state).** The plan is incomplete until it **enumerates every concurrent accessor (reader and
writer) of that state and names which the guard covers and which it does not** — an *accessor │
reader/writer │ synchronized by │ covered by the guard?* table is the natural form. The gap
between "accessors that exist" and "accessors the guard covers" is where the lost update hides;
naming it at plan time (per *Instrument before you build*) is the cheapest place to catch it —
cheaper than the red-team, far cheaper than production.

**Shared state has more than one accessor (CP7, concurrency lens; fires only where the change
alters concurrency structure over shared state).** When a change **introduces a new
unsynchronized accessor, or a new read→slow-work→write window, over shared mutable state whose
atomicity an existing transaction/lock does not already enforce**, correctness depends on
*every* accessor of that state, not just the one being written. A guard (lock, transaction,
queue, CAS) is only as strong as its **scope** — the set of accessors it actually covers; a
*different*, lock-free accessor whose write interleaves in the gap is silently lost (lost
update / torn write). This is the same blind spot as *Information-preserving is not
behavior-preserving*, one level out: a review that only asks "is this guard correct?" passes
the change, because the defect lives in an accessor it never **enumerated**. A guard's mere
existence does not settle "already enforced" — its scope must be enumerated, not assumed; when
it is unclear whether a guard covers *every* accessor,
treat the state as unguarded. Triggers only where the change alters the concurrency structure
over shared state — *not* ordinary single-threaded or already-serialized code.

**Regression must be measured on a comparable workload, or it is advisory only (H8).** Global
aggregate metrics (mean cost, mean tool-calls) computed over whatever happened to run will
move whenever the *new behavior* legitimately exercises the system more — producing a **false
regression** indistinguishable from a real one. A regression metric is only **gating** if
either (a) it's measured on a fixed/replayed held workload comparable to the baseline's, or
(b) the new behavior can be excluded from the aggregate. A metric that can't isolate the
change's own contribution is reported as **advisory** (surfaced, not auto-bouncing). The plan
(stage 2) names which metrics are gating vs. advisory and how the comparable workload is
obtained.

**A needed-but-absent signal → the plan adds the instrumentation (CFG6).** If a change needs a
signal the project doesn't yet expose, the **plan (stage 2) adds the instrumentation** — and
the config's `metrics`/`check` are updated as part of that change.
