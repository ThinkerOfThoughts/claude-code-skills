# Stage 4 — Verify

**What this stage does:** for each analysis list, a **cold verifier** independently re-checks every
cited source against the data and **drops the unverifiable**. This is the designed filter for
over-flagging and confabulated locators.

**Read `charter.md` (cite-or-drop discipline), then apply the procedure below. Use the
`briefs/verify-brief.md` template.**

## Procedure

1. **One cold verifier per analysis list.** 6 analyses → 6 verifiers; 3 → 3. Each verifier is an
   **independent cold leaf** with **no stake** in the list it checks; it did not write it. It reads
   ONE analyst's list + the item's artifacts + (for reference) the label-only ledger.
2. For **each** numbered flag, go to the cited source and decide:
   - **VERIFIED** — the cited source exists and genuinely shows the claimed **verifiable fact**;
   - **DROPPED** — the source doesn't exist, the locator is too vague/wrong to confirm, the data does
     not actually show the claimed thing, or the item is **cause-speculation** rather than a fact.
   The verifier **adds no new findings**, softens nothing, embellishes nothing — facts only.
3. **Write** `tree/<…>/<item>/analysis/<LETTER>_verified.md`: the header, a numbered list of
   **VERIFIED items only** (each preserving its description + confirmed source + snippet), then a
   `## Dropped` section (each dropped item's original number + a one-line reason).
4. **Update `_status.md`** with counts only (e.g. `verify: A 5 kept/2 dropped; B 4 kept/1 dropped;
   …`). The coordinator reads only counts + filenames.

## Rules governing this stage

- **Cite-or-drop is absolute.** A flag whose locator can't be confirmed is dropped, not kept "just
  in case." Citations are the guard the whole method rests on.
- **Independence.** The verifier has no stake — it neither defends nor pads the analyst's list.
- **Spot-verify.** The verifier is itself the spot-verify of the analyst's citations (charter rule
  5); its `## Dropped` section is the evidence it did the check, not a rubber stamp.
- **Facts only.** Cause-speculation that slipped past an analyst is dropped here — the verify stage
  is the last facts-only filter before merge.
