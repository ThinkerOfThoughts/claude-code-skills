# Data-Distiller — a process for cold, multi-agent data distillation

Data-Distiller is a small, reusable process — and a Claude Code skill that runs it — for extracting
**trustworthy, source-cited factual findings** from a **corpus too large for one context window**,
without the coordinator's judgment contaminating the findings. It is the sibling of
[guarded-change](../Guarded_change/) (gated *change*) and [dragonfly](../Dragonfly/) (gated
*diagnosis*): the three share a Layer-1-core / Layer-2-config seam and a cold-subagent independence
discipline. Distill → (optionally) diagnose → change.

If you only read one section, read **"The three failures it guards against."**

---

## TL;DR

- **What:** a decompose-and-aggregate distillation loop — `decompose → size/tier → analyze →
  verify → merge → blind roll-up` — with three hard rules:
  1. **Blindness is structural.** No coordinating node ever reads findings content; it reads only
     each child's terse `_status.md` roll-up + filenames. Every content-touch is a **dispatched cold
     leaf**. The coordinator's expectations therefore cannot steer what gets flagged.
  2. **Cite or drop; facts only.** Every flag names an exact source; a cold verifier re-checks every
     citation and drops the unverifiable; no leaf ever speculates about cause. Interpretation
     happens later, with the human.
  3. **Read-only, and the brief is the only fence.** The corpus is never mutated; off-limits paths
     are fenced by the brief text (no mutation-guard catches a plain read).
- **Why:** the expensive failures in "read it all and summarize" are a corpus that overflows the
  window, one reader's priors biasing what's seen, and summaries that drift into untraceable
  interpretation. This loop is built specifically against those.
- **How to use it three ways:** as a **Claude Code skill** you invoke (`/data-distiller`); as a
  **checklist** applied by hand; or as a **mindset** — *"is my coordinator blind? does every flag
  cite a source I can re-check? did anyone interpret when they should have only reported facts?"*

---

## The three failures it guards against

1. **The corpus overflows the window.** No single reader holds it all → **decompose** into per-item
   analytical units aggregated by a **static pyramid**.
2. **One reader's priors bias what's seen.** → **N independent cold analysts** per item (6 on Haiku,
   3 on Sonnet/Opus) under an **open** "flag ANY aberration" mandate, then a **cold verify** of
   every citation; the coordinator never reads findings (**blindness**), so its expectations can't
   steer them.
3. **Summaries drift into untraceable interpretation.** → **facts-only, cite-or-drop**; agreement +
   recurrence computed mechanically and rendered `PCT% (X/N)`; interpretation deferred to the human.

It also encodes the fixes for two **real production failures** from the run that proved it:
- a **session-limit death mid-merge** → all state on disk, deterministic filenames, idempotent
  stage re-run (nothing done is lost);
- an **OOM** from a 1.2 GB inline-image artifact → size-aware pre-flight + a streaming,
  text-faithful slimmer before fan-out + a static concurrency budget;
- a **plain read of an off-limits protected path** no mutation-guard caught → the brief is the only
  fence.

---

## The loop

```
1  DECOMPOSE + SIZE  corpus → items; pre-flight sizes; strategy {tag-replace | subdivide | escalate};
                     tier (Haiku→Sonnet→Opus by post-slim tokens) + redundancy (6/3); budget; tree/
2  CUT-GATE          HUMAN approves unit/splits/overlap + the context-preservation argument
                     (subdivided/borderline only; clean-fit auto-proceeds)  ← the representativeness gate
3  ANALYZE           N cold analysts per item; open mandate; cite every flag; facts only
4  VERIFY            one cold verifier per list; re-check each citation; drop the unverifiable
5  MERGE             dedup + agreement PCT% (X/N) + recurrence → super-list; sort % then recurrence
6  ROLL-UP           a BLIND node dispatches a cold summary leaf per set → summaries/ (facts + counts)
7  RESTART/RESUME    the on-disk state contract: deterministic names; HARDSTOP → re-run that stage
```

Design choices worth knowing:
- **Blindness is a property of the file layout, not operator discipline.** Findings live in child
  leaf dirs the coordinator is told never to open; `_status.md` is its only readable surface.
- **Size handling is strategy *selection*, not "slim everything"** — route by *what* is big (binary
  bulk → tag-replace; relevant text → subdivide; irreducible → escalate the tier).
- **Agreement is percentage-first** (`33% (2/6)`) so a 6-analyst item and a 3-analyst item are
  comparable; the denominator rides through to the summary.
- **All state is on disk** — because a session-limit death must lose nothing but the interrupted
  stage.

---

## How it's structured (two layers)

- **Layer 1 — the agnostic core.** The loop, the blindness/tree model, tiering + redundancy, the
  size-strategy procedure, the agreement model, the state contract, the human cut-gate, and the
  cold-analysis charter. Knows nothing about any specific corpus. This is `METHODOLOGY.md` (spec) +
  `SKILL.md` (what Claude Code executes) + `stages/` + `charter.md` + `briefs/`.
- **Layer 2 — a per-corpus config.** The atomic unit, legal cuts + overlap, the artifact-context
  block, off-limits paths, an optional label-only ledger, and the concurrency ceiling. One small
  config per corpus (`examples/companion-emergence/` is a worked, redacted example).

---

## Adopting it

1. **Drop the skill in.** Copy this `Data-Distiller/` folder's core files into
   `~/.claude/skills/data-distiller/`. Claude Code will then offer `data-distiller` as a skill.
2. **Write a Layer-2 config** for your corpus. Copy `examples/companion-emergence/corpus.md` and
   adjust the atomic unit, legal cuts, artifact-context block, off-limits paths, ledger, and
   ceiling. The contract is in `METHODOLOGY.md`.
3. **Invoke it on a corpus.** `/data-distiller` (or mention distilling a large body of data). It
   creates a run-root outside the corpus, walks the stages, spawns the cold leaves, keeps the tree,
   and stops to ask you only at the genuinely-yours decisions (the cut-gate, a missing config, a
   guard trip, an irreducible-oversize item).

You don't *need* the skill — the loop works as a manual checklist. But since the same tool you
already use can run it, the cheapest version is to let it.

---

## Relationship to the sibling skills

| | guarded-change | dragonfly | Data-Distiller |
|---|---|---|---|
| Job | *make* a change correctly | *find* the bug correctly | *distill* a large corpus into verifiable facts |
| "Done" bar | conformance to criteria set first | root cause reproduced + caused + toggled | every finding source-cited + verified; coordinator stayed blind |
| Hands off to | — | guarded-change | (soft) a dragonfly symptom ledger |
| Shared machinery | cold-subagent independence, evidence discipline, Layer-1/Layer-2 config, forked charter | | (all — charter forked, not depended-on) |

**Soft handoff, no hard dependency:** a Data-Distiller set summary (source-cited factual
aberrations) can seed a dragonfly hunt's frozen symptom ledger — the facts become the `S#` symptoms.
Distill → diagnose → change.

---

## Files

| File | What it is | Audience |
|---|---|---|
| `METHODOLOGY.md` | The authoritative spec — loop, blindness/tree model, tiering, size strategy, agreement model, state contract, config contract | the skill / a careful reader |
| `SKILL.md` | The operating procedure Claude Code executes (the router) | the agent |
| `stages/` | One file per stage (decompose+size, cut-gate, analyze, verify, merge, roll-up, restart) | the agent |
| `charter.md` | The cold-analysis discipline every leaf runs under (forked from guarded-change) | the agent |
| `briefs/` | The analysis / verify / merge / summary brief templates + shared clauses | the agent |
| `examples/companion-emergence/` | A worked, redacted Layer-2 config | you |
| `changes/` | The guarded-change change-records that authored this skill (provenance) | a careful reader |
| `this file` | Why it exists and how to adopt it | you |
