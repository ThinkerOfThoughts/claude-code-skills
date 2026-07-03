# 2 — Plan (v2)

v2 addresses the stage-3 round-1 findings (see `decisions.md`): M-1 (C3 replay redesign),
M-2 (over-fire trigger tightening), m-4 (Edit C determinism), m-5 (stage-2 enumeration
deliverable → new Edit G), m-6 (compress Edit A). Line-refs are against the current
`METHODOLOGY.md` / `SKILL.md`. Below is the **exact proposed wording** so the red-team reviews
real text.

## The trigger condition (shared by all edits — tightened per M-2)

The guard fires **only** when a change **introduces a *new* unsynchronized accessor of shared
mutable state, or a *new* read→modify→write window (especially across a slow or blocking
operation) over state whose atomicity is not already enforced** by an existing
transaction / lock / single-writer discipline. It does **not** fire merely because new code
touches state that many actors already reach — if an existing transaction or lock already
serializes every accessor, there is nothing new to guard. The rare, worth-guarding case is a
change that *alters the concurrency structure* (adds an actor, widens a critical section, splits
a read from its write); ordinary code that reads/writes already-serialized shared state is out
of scope, as is all single-threaded / name-bound code.

## Edit A — METHODOLOGY.md, Core principles (after "Information-preserving is not behavior-preserving") — compressed per m-6

> - **Shared state has more than one accessor.** When a change **introduces a new unsynchronized
>   accessor, or a new read→slow-work→write window, over shared mutable state whose atomicity an
>   existing transaction/lock does not already enforce**, correctness depends on *every* accessor
>   of that state, not just the one being written. A guard (lock, transaction, queue, CAS) is
>   only as strong as its **scope** — the set of accessors it actually covers; a *different*,
>   lock-free accessor whose write interleaves in the gap is silently lost (lost update / torn
>   write). This is the same blind spot as *Information-preserving is not behavior-preserving*,
>   one level out: a review that only asks "is this guard correct?" passes the change, because the
>   defect lives in an accessor it never **enumerated**. Triggers only where the change alters the
>   concurrency structure over shared state — *not* ordinary single-threaded or already-serialized
>   code.

## Edit B — METHODOLOGY.md, red-team charter (new trigger paragraph, sibling to the position-sensitivity one)

> **If the change introduces a new accessor or a new read-modify-write window over shared mutable
> state (see trigger above), map the accessors and challenge the guard's scope** (lens 4). This
> fires only where the change *alters* concurrency over shared state — not ordinary or
> already-serialized code. Do two things: **(1) enumerate every concurrent reader and writer of
> that state** — including ones the change did not touch (a pre-existing lock-free appender, a
> background tick, a crash-recovery path); **(2) treat the guard's scope as a claim to
> challenge** — not "is the lock correct?" but "*which* accessors does this guard cover, and
> which does it leave out?" A lock-free (or differently-guarded) accessor of the same state, or a
> read and write that straddle a slow operation during which another accessor can mutate the
> state, is the finding — ranked by the impact of the lost/torn write, not by whether the guarded
> path itself looks correct.

## Edit C — METHODOLOGY.md, stage 1.5 (new mandatory-criterion paragraph) — pinned to a deterministic/injected harness per m-4

> **If the change introduces a new accessor or read-modify-write window over shared mutable state**
> (see *Shared state has more than one accessor*), at least one criterion must assert the
> **atomicity / no-lost-update** property under a concurrent interleaving — a write by one accessor
> is not silently clobbered by another. Name the interleaving and how it is checked (e.g. "an
> append by accessor B during accessor A's read→write window survives"). Because real races are
> **non-deterministic**, the criterion must be checked **deterministically** — by *injecting* the
> competing mutation into the middle of the guarded window (not hoping a live thread race lands
> there) — or, where only a live race is possible, over a **stated number of runs with a pass-rate
> floor** (treat as the probabilistic rubric under stage 1.5). And, like any representative
> harness, the interleaving test must **fail against the unguarded version**; a test that passes
> with and without the guard proves nothing. Reasoning that "the lock covers it" is not
> satisfaction — only the executed interleaving is.

## Edit D — METHODOLOGY.md, stage 8 (new paragraph, sibling to "Position-dependent criteria must be checked by execution")

> **Concurrency criteria must be checked by executing an interleaving, not by inspecting the
> guard.** Any criterion written under *Shared state has more than one accessor* (stage 1.5) is
> satisfied only by **running a concurrent interleaving and observing the write survive** — never
> by re-reading the lock/transaction code and reasoning it looks sufficient. Inspecting the guard
> is the exact check the scope gap defeats: the guard *is* correct for the accessors it covers.
> Prefer a deterministic harness that injects the competing mutation into the read→write window
> (a live thread race need not be reproduced by luck); a pure-inspection "verification" of such a
> criterion counts as `verified = no`.

## Edit G — METHODOLOGY.md, stage 2 (new plan-completeness clause) — NEW per m-5

Extend the stage-2 "Plan" description so the *cheapest* catch (the plan itself) forces the
enumeration, per "Instrument before you build":

> **If the change introduces a new accessor or read-modify-write window over shared mutable
> state**, the plan is incomplete until it **enumerates every concurrent accessor (reader and
> writer) of that state and names which the guard covers and which it does not** — the gap
> between "accessors that exist" and "accessors the guard covers" is where the lost update hides,
> and naming it at plan time is cheaper than discovering it at review.

## Edit E — SKILL.md, stage 1.5 bullet (operating procedure — one clause, sibling to the position clause)

Append to the stage-1.5 paragraph: **"If the change introduces a new accessor or read-modify-write
window over shared mutable state, add a criterion asserting no-lost-update under a concurrent
interleaving, and require stage 8 to verify it by *executing* that interleaving — injected
deterministically (or over a stated pass-rate), and failing against the unguarded version — see
METHODOLOGY 'Shared state has more than one accessor'."**

## Edit F — SKILL.md, stage 3 bullet (operating procedure — one clause, sibling to the position clause)

Append to the stage-3 paragraph: **"If a change introduces a new accessor or read-modify-write
window over shared mutable state, enumerate every concurrent reader/writer and challenge the
guard's scope (which accessors it covers vs. leaves out) — 'the lock looks correct' is not a clean
verdict when an unenumerated lock-free accessor can mutate the same state."**

## Edit H — SKILL.md, stage 2 bullet (operating procedure — one clause) — NEW per m-5

Append to the stage-2 paragraph: **"If the change touches shared mutable state per the trigger,
the plan must enumerate every concurrent accessor and state which the guard covers vs. leaves
out (METHODOLOGY 'Shared state has more than one accessor')."**

## Measurement / instrumentation

- **C1, C2, C4** — inspection of the edited `METHODOLOGY.md` / `SKILL.md` (read + grep for the
  locations: core principle, stage-2 clause, charter trigger, stage-1.5 rule, stage-8 paragraph,
  and the SKILL.md clauses). The docs are the artifact.
- **C6** — `diff` live vs. source for each changed file → empty.
- **C3 (load-bearing) — true A/B execution.** Instrumentation = a cold-subagent charter carrying
  the new guard text (Edits A–D) **plus the same concurrency-relevant source the real stage-3
  had**: the compaction `2-plan.md` and the code it references (`server.py` cadence-on-a-thread,
  `engine.py` lock-free `ingest_turn`, `supervisor.py` tick). **Treatment** run (guard in
  charter) must independently flag the lock-free writer / lost update. **Control**: the
  documented historical miss (the real stage-3 had that source and did *not* flag it) is the
  paired negative; optionally re-run one stock-charter reviewer to reconfirm. Pass = treatment
  catches it AND control does not — the guard *moves the outcome*.

## Severity → routing thresholds

- **Blocker** (→1): the guard as worded would *not* move the compaction A/B outcome (C3 fails),
  or it changes loop structure / severity model (wrong problem).
- **Major** (→2): it still over-fires on ordinary already-serialized code (C4 hole), materially
  bloats/duplicates the position section, or lands in too few locations to fire (C1 hole).
- **Minor** (fix in place): wording ambiguity, a weak example, a tightenable phrase.
- **Nitpick** (log): style/terminology polish.

Gating criteria: C1, C2, C3, C4, C6. Advisory: C5 (coherence, surfaced not bounced).
