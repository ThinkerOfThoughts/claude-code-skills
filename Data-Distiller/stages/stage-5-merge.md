# Stage 5 — Merge

**What this stage does:** a single **merge leaf** per item collapses the verified analysis lists into
one prioritized **super-list**, computing **agreement** and **recurrence**, rendering agreement as
**`PCT% (X/N)`**, and sorting **percentage desc then recurrence desc**. For subdivided items the
merge is **seam-aware**.

**Read `charter.md` (facts-only), then apply the procedure below. Use the `briefs/merge-brief.md`
template.**

## Procedure

1. **One merge leaf per item** (a cold leaf). Inputs = the item's **VERIFIED** lists only
   (`*_verified.md`; ignore their `## Dropped` sections). N = the item tier's analyst count (6 or 3)
   — the merge **denominator**.
2. **Dedup.** Items describing the **same aberration** (same phenomenon at the same source locator,
   even if worded differently) collapse into ONE entry.
3. **For each merged entry compute:**
   - **agreement** = how many of the N analysts flagged it, rendered **`PCT% (X/N)`** — the
     **percentage first**, floored to an integer (1/3→33%, 2/3→66%, 3/3→100%; 1/6→16%, 2/6→33%,
     3/6→50%, 4/6→66%, 5/6→83%, 6/6→100%), then the raw fraction. N is the tier's analyst count.
   - **recurrence** = how many **non-sequential distinct** occurrences of that kind of aberration
     occur across the item (count separated occurrences by source locator; do NOT count one
     continuous incident repeatedly).
4. **Sort** the super-list **by percentage descending, then recurrence descending.**
5. **Seam-aware, for subdivided items.** Inputs are the per-piece super-lists. A finding whose
   locator falls in the **overlap** appears in two adjacent pieces — it is **deduplicated into ONE
   entry** (not double-counted, not dropped), and its recurrence is counted across the whole item,
   not per piece. The approved overlap (stage 2) is what makes a seam-straddling finding visible in
   both pieces so this dedup is possible. **Agreement reconciliation for a seam entry:** each piece
   ran its own tier-sized analyst set, so **N stays the per-piece analyst count** (6 or 3 — pieces
   are not summed into a bigger denominator), and the seam entry's **X = the GREATER of the two
   pieces' flagger counts** (never the sum — a sum could exceed N and produce a nonsensical >100%).
   The percentage is recomputed from that `X/N`. (Rationale: the two pieces are two views of the
   same overlap window; the stronger agreement is the item's agreement for that finding, and the
   denominator is what a single piece's analysts could have flagged.)
6. **Write** `tree/<…>/<item>/superlist.md` (this **stays in `tree/`** — it is a per-item working
   artifact, not a deliverable): a header + a one-line count (total merged; how many at each
   percentage band), then the sorted list, each entry `[PCT% (X/N), recurrence=M] [what] —
   SOURCE(s): [...] — "[snippet]"`. Facts only; no conclusions.
7. **Update `_status.md`** with counts only (e.g. `merge: 9 merged (100%:2, 66%:3, 33%:4)`).

## Rules governing this stage

- **Percentage first, floored, then fraction — always.** The percentage is the **cross-tier
  comparator** (it makes a 6-analyst item comparable to a 3-analyst item); the fraction preserves N.
  Rendering fraction-first or agreement-as-raw-count is wrong (this is the settled decision the
  ported brief must NOT regress to a raw `[agreement=N]` count).
- **The denominator N rides through** merge → summary (a 33% stays legible as 2/6 vs 1/3).
- **Facts only; no conclusions.** The merge leaf ranks and dedups; it does not interpret.
- **The super-list stays in `tree/`** at its item node; only **summary-tier** roll-ups go to
  `summaries/`.
