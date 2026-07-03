# 1 — Spec: shared-state-concurrency guard for guarded-change

## Problem

The guarded-change loop forces reasoning about exactly one *behavior-preserving* hazard
class — **position-sensitive assembly** (order/adjacency is semantic). It has a matching
guard in three load-bearing places: a Core Principle, a red-team charter lens trigger, and a
mandatory stage-1.5 criterion checked by execution at stage 8.

It has **no equivalent guard for concurrent access to shared mutable state.** A change that
introduces a read-modify-write over state that more than one actor touches can ship a
lost-update / torn-write data-loss race, and every gate can pass it — because the gates reason
about the actor *in front of them* (is this lock correct?) and never enumerate the *other*
actors touching the same state, nor challenge whether the guard's **scope** covers them.

## Evidence (the run that shipped the race uncaught)

`~/Desktop/Planning_Dir/changes/timed-conversation-compaction/` — a full guarded-change run
(stage 3 ×2 rounds, stage 6, stage 8, all gates passed) that shipped a data-loss race the
human caught afterward.

- **The design** (`2-plan.md`): `compact_conversation` = acquire `O_EXCL` lock
  `active_conversations/<sid>.compacting` → read snapshot of the buffer → **slow**
  `provider.generate` summarization (seconds) → `rewrite_session_atomic` (temp + fsync +
  `os.replace`). The lock guards **compaction re-entrancy only.**
- **The gate reasoned about concurrency — but only inside the lock's scope.**
  `3-redteam-plan.md` finding **R-1**: a stale-lock reap could let *two compactors* run and
  race `os.replace` + duplicate-append the archive. That is compaction-vs-compaction. The
  reviewer was concurrency-aware and still scoped its whole analysis to the actor it was
  looking at.
- **The missed actor:** `ingest_turn` (the chat-append path) is **lock-free**. A turn
  appended during the read→summarize→rewrite window is **clobbered** by the rewrite of the
  stale snapshot — a classic lost update. `ingest_turn` appears in those gate docs only for
  *provenance* (byte-stability, `close_session`), **never as the concurrent race actor**: no gate
  ever asked "what *else* writes this buffer, and does the lock cover it?" (`6-redteam-code.md`
  L93-97 even declares the lock race "sound … Clean," reasoning only about compaction-vs-tick.)
- **Caught post-hoc**, by the human, after the loop finished, and only *then* gated — fixed as
  commit `b7e7880` / criterion **C13** (re-read the buffer immediately before rewrite; rebuild
  the retained set from *current* turns by identity minus the archived ones — shrinks the window
  from seconds to microseconds). **No *in-loop* gate (stage 3 ×2, 6, 8) surfaced it**; it entered
  the record only afterward (the compaction run's `decisions.md` + C13 + `HANDOFF.md`).

## Why this belongs in Layer 1

It is the loop's founding failure mode in a new coat: an **unchallenged assumption** (the
lock's scope) producing an **unmeasured regression** (silent lost update). And it is
*structurally identical* to the position-sensitivity lesson already baked in: a check that
only inspects the element in front of it passes a change whose defect lives in an actor /
element it never enumerated. The fix should mirror that treatment, not invent a new shape.

## Goal

Add a domain-agnostic guard to **Layer 1** (`METHODOLOGY.md` + `SKILL.md`) that, when a change
**introduces or modifies concurrent access to shared mutable state**, forces the reviewer to:

1. **Enumerate every concurrent accessor** (reader/writer) of that state — threads, processes,
   async tasks, signal handlers, ret+ multiple writers to a file / DB row / in-memory structure.
2. **Treat the guard's *scope* as a claim to challenge** — not "is the lock correct?" but
   "*which* accessors does this lock/guard cover, and which does it silently leave out?" A
   lock-free accessor of guarded state is the finding.
3. Carry a **mandatory criterion** that the atomicity / no-lost-update behaviour is verified by
   **executing a concurrent interleaving** that *fails against the unguarded version*
   (representativeness) — never by reasoning about the lock.

Placed in the same three locations as the position guard so it actually fires: Core Principle,
red-team charter lens, stage-1.5 criterion + stage-8 execution requirement.

## Constraints / non-goals

- **Domain-agnostic.** Layer 1 knows no project, language, or concurrency primitive. Name the
  *class* (shared mutable state + >1 accessor), not `O_EXCL` or threads specifically.
- **Precision — must not over-fire.** Like the position lens ("*not* ordinary code whose
  behavior is name- not position-bound"), this triggers **only** when a change introduces or
  modifies concurrent access to shared mutable state — not on ordinary single-threaded code.
  A guard that turns every review into a concurrency audit is a failure, not a success.
- **Proportionate.** Roughly the size/shape of the existing position-sensitivity treatment; no
  bloat, no duplication of it.
- **No structural change** to stages, gates, severity model, or the two-layer split.
- **Not** re-fixing the compaction bug (already fixed). This is a methodology guard only.
- Applies **identically to both copies** — the live `~/.claude/skills/guarded-change/` and the
  source `~/Desktop/claude-code-skills/Guarded_change/` — or the installed skill won't carry it
  (the dragonfly note's "edit skill AND source" lesson).
