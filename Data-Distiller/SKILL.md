---
name: data-distiller
description: A cold, multi-agent method for extracting trustworthy source-cited factual findings from a corpus too large for one context window — decompose → size/tier → N independent cold analysts → cold verify → agreement-ranked merge → blind roll-up, where coordinating nodes never read findings and every leaf is read-only and cites every flag. Use when you must distill a large body of logs/transcripts/data into verifiable facts (not interpretation) without a single reader's priors biasing the result. Corpus specifics come from a per-corpus Layer-2 config. Proactively SUGGEST this when asked to sift/audit/distill a corpus that won't fit in one pass.
---

# Data-Distiller

The cold multi-agent distillation method's purpose: **extract trustworthy, source-cited factual
findings from a corpus too large for one context window — without the coordinator's judgment
contaminating the findings.** This file is the **router**: each stage's full procedure lives in
`stages/`, the shared cold-analysis discipline in `charter.md`, and the orientation/reference spec
(the config contract, the tree/agreement/tiering models) in `METHODOLOGY.md`.

## The three rules that govern everything — read first

1. **Blindness (structural).** A coordinating node reads **ONLY** each *direct* child's
   `_status.md` (terse done-state + one-line roll-up + counts) and **globs child dir/filenames**. It
   **NEVER** opens `analysis/*`, `*_verified.md`, `superlist.md`, or `*_summary.md`. Findings live in
   child leaf dirs the node is told never to open — so its expectations can't steer them. Every
   content-touch (analysis, verify, merge, summary) is a **dispatched cold leaf**, not the
   coordinator.
2. **Read-only corpus.** The corpus is **never mutated**. No leaf copies, moves, renames, deletes,
   `chmod`s, or writes into it; databases/large files are inspected **in place, read-only** (never
   `cp` out first). All run output goes to a **run-root OUTSIDE the corpus**; `_prepared/` holds the
   only transformed copies (originals untouched).
3. **Off-limits paths are fenced by the brief, not by any guard.** The Layer-2 `off_limits_paths`
   are named to leaves as text-only context that must **never be opened or grep'd, even to verify a
   citation** — a mutation-guard does NOT catch a plain read, so **the brief is the only fence**.
   Agent-facing ledger copies are **redacted** of live/off-limits paths.

## Inputs

- **The corpus** — the (large, read-only) body of data to distill.
- **A Layer-2 corpus config** (`data-distiller.*.{md,yaml}` in/near the working dir, or
  `config/corpus.md` in the run-root). Declares the atomic analyzable unit, legal cut points +
  overlap, the shared artifact-context block, the off-limits paths, an optional label-only
  prior-knowledge ledger, and the concurrency ceiling. If none exists, help author one against the
  config contract in `METHODOLOGY.md`. **Do not invent corpus specifics** (what an item is, what is
  off-limits, what is legitimately in-context).
- **An optional prior-knowledge ledger** (label-only; redacted agent-facing copy).

## Loop

Create a **run-root OUTSIDE the corpus** with the layout in `METHODOLOGY.md` ("What a run
produces"). Walk the stages; **at each stage, read that stage's file for the full procedure + the
rules it applies.** Maintain `plan/decisions.md` (append-only: gates, tier calls, human overrides,
guard-trips).

| # | Stage — one-line purpose | Read |
|---|---|---|
| **1** | Decompose + size: corpus → items; pre-flight sizes; pick strategy {tag-replace \| subdivide \| escalate}; tier + redundancy; concurrency budget; build the static `tree/` | → `stages/stage-1-decompose-size.md` |
| **2** | Human cut-gate: approve unit/splits/overlap + the context-preservation argument for subdivided/borderline items; clean-fit items auto-proceed | → `stages/stage-2-cut-gate.md` |
| **3** | Analysis: N cold analysts per item (6 Haiku / 3 Sonnet-Opus), open mandate, cite every flag, facts only | → `stages/stage-3-analysis.md` (+ `charter.md`) |
| **4** | Verify: one cold verifier per analysis list; re-check each citation; drop the unverifiable | → `stages/stage-4-verify.md` (+ `charter.md`) |
| **5** | Merge: dedup + agreement `PCT% (X/N)` + recurrence → `superlist.md` (seam-aware if subdivided); sort percentage desc then recurrence desc | → `stages/stage-5-merge.md` (+ `charter.md`) |
| **6** | Roll-up / summary: a blind node dispatches a cold summary leaf per set → `summaries/`; optional global summary | → `stages/stage-6-rollup-summary.md` (+ `charter.md`) |
| **7** | Restart / resume: the on-disk state contract; deterministic filenames; HARDSTOP → re-run that stage fresh | → `stages/stage-7-restart-resume.md` |

**Tiering + redundancy (full model in `METHODOLOGY.md`):** tier by post-slim token size (cheapest
fit + a density ceiling; prefer subdivide + cheapest fit; Opus is the reserve). **Haiku items → 6
analysts; Sonnet/Opus items → 3.** One cold verifier per analysis list.

**Concurrency:** a **static budget** computed at decompose-time caps in-flight agents to the Layer-2
ceiling; dispatch **serializes within the cap** (no reactive scaling). This is the OOM/usage
headroom, planned not reactive.

## The blind-node contract (one paragraph)

A coordinating node's entire readable surface is `_status.md` files + directory listings. It
dispatches leaves, waits, then reads each direct child's `_status.md` (done-state + counts) to know
whether to proceed — it **never** opens a findings file to "check the work." The leaves cite and
self-record (see `charter.md` provenance); the node routes on counts and filenames. If you find
yourself wanting to open a `superlist.md` or `*_summary.md` as the coordinator, **stop** — that read
is the contamination the method exists to prevent; dispatch a leaf (e.g. the summary leaf) instead.

## Stop-for-human

Pause and ask when: the **cut-gate** is reached for a subdivided/borderline item (approve
unit/splits/overlap + the context-preservation argument — the representativeness gate, never
auto-approved); a **Layer-2 config or off-limits set needed to proceed is missing**; a **guard trip
or a line-crossing** needs an owner call (e.g. an agent grep'd near an off-limits path); or an item
is **genuinely irreducible-oversize** and even the Opus reserve can't fit it (escalate the decision,
don't silently truncate). Refuse to invent corpus specifics — that's the exact contamination this
method prevents.

## Self-check / dogfooding

These skill files are **prompts** (a position-sensitive assembly). Non-trivial edits take the full
**guarded-change** loop, not a freehand pass. Standing self-check criteria after any edit: live copy
== source (`diff`); SKILL ↔ METHODOLOGY ↔ stage-file ↔ brief consistency on every rule stated in
more than one place (the agreement format `PCT% (X/N)`, the blindness rule, the 6/3 redundancy
counts, the read-only/off-limits clauses, the size trichotomy, the layout names); behavior-
preservation for anything moved or removed. The initial authoring run's change-records are under
`changes/initial-authoring-2026-07/`.

## Composition

Standalone. Forks its charter from guarded-change (`charter.md`) rather than depending on it live.
**Soft handoff (no hard dependency):** a distillation output — a set summary of source-cited factual
aberrations — can seed a **dragonfly** symptom ledger (the facts become the `S#` symptoms a hunt
freezes), just as dragonfly hands a confirmed diagnosis to guarded-change. Distill → (optionally)
diagnose → change.
