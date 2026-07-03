# 2 — Plan

Mirror the position-sensitivity treatment in the same three load-bearing locations. Below is
the **exact proposed wording** so the red-team reviews real text, not intent.

## Edit A — METHODOLOGY.md, Core principles (after "Information-preserving is not behavior-preserving")

> - **Shared state has more than one accessor.** When a change introduces or modifies
>   **concurrent access to shared mutable state** — state touched by more than one thread,
>   process, async task, signal handler, or writer (an in-memory structure, a file, a DB row, a
>   cache) — correctness depends on *every* accessor, not just the one being written. A guard
>   (lock, transaction, queue, compare-and-swap) is only as strong as its **scope**: the set of
>   accessors it actually covers. The classic failure is a read → slow-work → write sequence
>   whose guard covers writers *like itself* but not a *different, lock-free* accessor of the
>   same state — whose interleaved write is silently lost (lost update / torn write). Reviewing
>   "is this lock correct?" passes such a change blind, because the defect lives in an accessor
>   the review never enumerated. This is *not* ordinary single-threaded or name-bound code — it
>   triggers only where two or more actors genuinely reach the same mutable state.

## Edit B — METHODOLOGY.md, red-team charter (new trigger paragraph, sibling to the position-sensitivity one)

> **If the change introduces or modifies concurrent access to shared mutable state, map the
> accessors and challenge the guard's scope** (lens 4). This triggers only where state is
> reached by more than one thread / process / async task / signal handler / writer — *not*
> ordinary single-threaded code. Do two things: **(1) enumerate every concurrent reader and
> writer of that state** — including ones the change did not touch (an existing lock-free
> appender, a background tick, a crash-recovery path); **(2) treat the guard's scope as a claim
> to challenge** — not "is the lock correct?" but "*which* accessors does this guard cover, and
> which does it leave out?" A lock-free (or differently-locked) accessor of guarded state, or a
> read-modify-write whose read and write straddle a slow operation during which another accessor
> can mutate the state, is the finding — ranked by the impact of the lost/torn write, not by
> whether the guarded path itself looks correct.

## Edit C — METHODOLOGY.md, stage 1.5 (new mandatory-criterion paragraph, sibling to the position one)

> **If the change introduces or modifies concurrent access to shared mutable state** (see
> *Shared state has more than one accessor*), at least one criterion must assert the
> **atomicity / no-lost-update** property under a concurrent interleaving — that a write by one
> accessor is not silently clobbered by another. Name the interleaving and how it is checked
> (e.g. "an append by accessor B during accessor A's read→write window survives"). The criterion
> must **require empirical execution of that interleaving** (carried out at stage 8) and, like a
> representative harness, the interleaving test must **fail against the unguarded version** — a
> test that passes both with and without the guard proves nothing. Reasoning that "the lock
> covers it" is not satisfaction; only the executed interleaving is.

## Edit D — METHODOLOGY.md, stage 8 (new paragraph, sibling to "Position-dependent criteria must be checked by execution")

> **Concurrency criteria must be checked by executing an interleaving, not by inspecting the
> guard.** Any criterion written under *Shared state has more than one accessor* (stage 1.5) is
> satisfied only by **running a concurrent interleaving and observing the write survive** — never
> by re-reading the lock/transaction code and reasoning it looks sufficient. Inspecting the guard
> is the exact check the scope gap defeats (the guard *is* correct for the accessors it covers).
> Where a real thread race is impractical to force deterministically, a representative harness
> that drives the read→write window with an injected concurrent mutation counts; pure inspection
> does not.

## Edit E — SKILL.md, stage 1.5 bullet (operating procedure — one clause, sibling to the position clause)

Append to the stage-1.5 paragraph: **"If the change introduces or modifies concurrent access to
shared mutable state, add a criterion asserting the no-lost-update behavior survives under a
concurrent interleaving, and require stage 8 to verify it by *executing* that interleaving (which
must fail against the unguarded version) — see METHODOLOGY 'Shared state has more than one
accessor'."**

## Edit F — SKILL.md, stage 3 bullet (operating procedure — one clause, sibling to the position clause)

Append to the stage-3 paragraph: **"If a change touches concurrent access to shared mutable
state, enumerate every concurrent reader/writer and challenge the guard's scope (which accessors
it covers vs. leaves out) — 'the lock looks correct' is not a clean verdict when an unenumerated
lock-free accessor can mutate the same state."**

## Measurement / instrumentation

- **C1, C2, C4** — inspection of the edited `METHODOLOGY.md` / `SKILL.md` (read + grep for the
  three locations and the required phrases). No new instrumentation needed; the docs are the
  artifact.
- **C6** — `diff` live vs. source for each changed file.
- **C3 (the load-bearing one)** — **execution via replay.** Instrumentation = a cold-subagent
  prompt carrying *only* the proposed guard text (Edits A–D) + the compaction `2-plan.md`, with
  no access to this change folder or the known answer. Signal = whether it independently names
  the lock-free `ingest_turn` / lost-update. This is run at stage 8; a dry version may also be
  used to sanity-check before build.

## Severity → routing thresholds

- **Blocker** (→1): the guard as worded would *not* surface the compaction race (C3 fails at
  stage 3 in principle), or it changes loop structure/severity model (wrong problem).
- **Major** (→2): it over-fires (would demand concurrency analysis on ordinary code — C4 hole),
  materially bloats/duplicates the position section, or lands in too few of the three locations
  to fire (C1 hole).
- **Minor** (fix in place): wording ambiguity, a weak example, a phrase that could be tightened.
- **Nitpick** (log): style/terminology polish.

Gating criteria: C1, C2, C3, C4, C6. Advisory: C5 (coherence, surfaced not bounced).
