# TEMPLATE M — MERGE

**One merge leaf per item** (a cold leaf). Renders agreement as `PCT% (X/N)` and sorts percentage
descending, then recurrence descending. Prepend the shared clauses.

---

Merge the independently-verified findings lists for one item into one prioritized super-list.

## Inputs
The item's VERIFIED lists only (`{verified_paths}` — read the VERIFIED items; ignore their `##
Dropped` sections). **N = the item tier's analyst count (6 or 3)** — the merge denominator.
(For a **subdivided** item, inputs are the per-piece super-lists and the merge is **seam-aware** —
see the seam rule below.)

## Task
- Merge into one list, DEDUPLICATING: items describing the same aberration (same phenomenon at the
  same source locator, even if worded differently) collapse into ONE entry.
- For each merged entry compute:
  - **agreement** = how many of the N analysts flagged it, rendered **`PCT% (X/N)`** — the
    **percentage FIRST**, floored to an integer (1/3→33%, 2/3→66%, 3/3→100%; 1/6→16%, 2/6→33%,
    3/6→50%, 4/6→66%, 5/6→83%, 6/6→100%), then the raw fraction.
  - **recurrence** = how many NON-SEQUENTIAL distinct occurrences of this kind of aberration occur
    across the item (count separated occurrences by source locator; do NOT count one continuous
    incident repeatedly).
- **SORT descending by percentage, then by recurrence descending.**
- Preserve each entry's source citation(s) + a representative snippet.
- **Seam-aware (subdivided items only):** a finding whose locator falls in the piece **overlap**
  appears in two adjacent pieces — deduplicate it into ONE entry (never double-count, never drop),
  counting its recurrence across the whole item. **Agreement for a seam entry:** N stays the
  per-piece analyst count (6 or 3 — do NOT sum pieces into a bigger denominator); X = the **greater**
  of the two pieces' flagger counts (never the sum — a sum could exceed N → a nonsensical >100%);
  recompute the percentage from that `X/N`.

## Output
Write to `{out_superlist}` (= `tree/<…>/{item_id}/superlist.md`):
- Header naming the item + a one-line count (total merged; how many in each percentage band).
- Sorted numbered list; each: `[PCT% (X/N), recurrence=M] [what] — SOURCE(s): [...] — "[snippet]"`.
Facts only; no cause speculation; no conclusions.
Final message: terse, e.g. `superlist {item_id}: 9 merged (100%:2, 66%:3, 33%:4)`. Do NOT paste
contents.
