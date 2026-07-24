# Stage 6 — Roll-up / summary

**What this stage does:** produce the run's **deliverables** — one factual summary per set (and an
optional global/cross-set summary) — by having a **blind coordinating node dispatch a cold summary
leaf**. The node never reads the super-lists; the summary leaf does.

**Read `charter.md` (facts + counts, no conclusions), then apply the procedure below. Use the
`briefs/summary-brief.md` template.**

## Procedure

1. **The set node is blind.** To roll up a SET, the coordinating node reads only each child item's
   `_status.md` (done-state + counts) and globs the item dirs for their `superlist.md` **filenames**
   — it **never opens** a `superlist.md`. When all the set's items report `merge: done`, it dispatches
   a **cold summary leaf**.
2. **The summary leaf** (a cold leaf — Opus is typical for the whole-set synthesis) reads **every
   super-list in the set** (`tree/<SET>/<item>/superlist.md` for each item) and writes ONE
   human-readable factual summary directly to `summaries/<SET>_summary.md`:
   - concise but fully human-readable (no shorthand-only lines);
   - **draws NO conclusions and offers NO cause/interpretation** — only verifiable facts present in
     the super-lists;
   - includes **recurrence counts** for repeating issues and notes **agreement levels** (carrying
     the `PCT% (X/N)` denominator) where relevant;
   - organized by phenomenon/theme where natural; notes which items each finding appeared in.
3. **Optional global / cross-set summary.** A blind apex node dispatches a cold leaf that reads the
   set summaries (or, for a by-arm cross-reference, re-groups the super-lists by arm) → a second
   deliverable in `summaries/` (e.g. `global_summary.md`, `<SET>_by-arm_crossref.md`). Facts + counts
   only; **no new interpretation.**
4. **Update `_status.md`** to point at the written summary **by name** (e.g.
   `summary: wrote summaries/<SET>_summary.md`). The apex `tree/_status.md` is the sole
   parent-readable roll-up of the whole run.

## Rules governing this stage

- **Summaries out, super-lists in.** Summary-tier deliverables → `summaries/` (canonical copies the
  leaf writes directly); per-item super-lists stay at their item nodes in `tree/`.
- **Blindness is preserved to the top.** Even the apex never reads a super-list or a summary; the
  human reads the summaries. **Interpretation happens later, with the human** — never in a leaf and
  never in a coordinating node.
- **No conclusions.** A set summary that offers a cause, a verdict, or an interpretation has exceeded
  its mandate → re-dispatch. Facts + counts only.
- **The deliverable is the summaries + the super-lists**, not the coordinator's understanding (the
  coordinator has none — it stayed blind).
