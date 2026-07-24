# Stage 3 — Analysis

**What this stage does:** dispatch **N independent cold analysts** per item to comb the data and
**flag ANY aberrant behavior**, each flag citing an exact source, facts only. The analysts are the
sole judges of the data; the coordinator is blind.

**Read `charter.md` for the cold-analysis discipline (given to every leaf verbatim), then apply the
procedure below. Use the `briefs/analysis-brief.md` template.**

## Procedure

1. **N by tier (redundancy).** **Haiku items → 6 analysts (A–F); Sonnet/Opus items → 3 (A–C).** A
   subdivided item's Haiku-sized pieces each get **6** analysts. Dispatch them as **independent cold
   leaves** (`general-purpose`, write-capable, run in background) — they work alone, do not
   coordinate, and each writes to its own file `tree/<…>/<item>/analysis/<LETTER>.md`.
2. **Fill the brief** (`briefs/analysis-brief.md`) from `index.md` for this item: the shared
   **artifact-context block** (Layer-2 slot), the item's artifact paths, the **degraded** note, the
   **read-only + off-limits + do-the-work** clauses, and — if a Layer-2 ledger exists — the
   **label-only** prior-knowledge pointer (redacted copy).
3. **Respect the concurrency cap.** Never exceed `plan/budget.md`; **serialize within the cap** (if
   the budget is below the item's analyst count, dispatch in waves).
4. **Each analyst** combs its item turn-by-turn and flags anything off/inconsistent/unexpected/wrong
   — liberally — and for each flag states WHAT (a verifiable fact) + a SPECIFIC SOURCE (`file:locator`)
   + a verbatim snippet, with **no cause speculation**. A no-flags result must **state the coverage
   swept** (charter rule 4).
5. **On completion**, update the item node's `_status.md` with counts + filenames only (e.g.
   `analysis: 6/6 done — A:7 B:5 C:9 D:6 E:8 F:4 flagged`). The coordinator reads **only** this — it
   never opens an `analysis/*.md`.

## Rules governing this stage

- **Open mandate, no priming.** The analysts get an **open** "flag ANY aberration" mandate; the ONLY
  prior-knowledge source is the optional label-only ledger. Do NOT single out target phenomena or
  inject definitions from chat/memory (charter rule 6). Over-flagging is expected — the cold verify
  stage is the designed filter.
- **Blindness holds.** Findings go to FILES; the analyst's final chat message is a **terse
  confirmation only** (never pastes findings). A leaf that returns findings upward has broken the
  contract → re-dispatch.
- **Read-only + off-limits.** Every dispatch prompt carries the read-only clause and the exact
  off-limits paths (the brief is the only fence — charter rule 8).
- **An outlier over-flagger** (e.g. 48 vs a typical ~10) is **not** trusted or discarded wholesale —
  it is flagged to its verifier for a rigorous per-item re-check (the verify stage is the filter).
