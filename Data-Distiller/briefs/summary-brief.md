# TEMPLATE S — SET SUMMARY

**One cold summary leaf per set** (Opus is typical for whole-set synthesis). Reads every super-list
in the set; writes one deliverable to `summaries/`. Facts + counts only. Prepend the do-the-work +
read-only + off-limits clauses (no analyst mandate — this leaf synthesizes existing super-lists,
it does not re-analyze raw data).

---

Produce a detailed-but-concise FACTUAL summary of all findings for one set.

## Inputs
Every super-list for set `{SET}`: `{superlist_paths}` (= `tree/{SET}/<item>/superlist.md` for each
item).

## Task
Read the super-lists and write ONE summary of the set's findings. It MUST:
- Be concise (no rambling, no filler) but fully human-readable (no shorthand/jargon-only lines).
- Draw NO conclusions and offer NO cause/interpretation — summarize only verifiable facts present in
  the super-lists.
- Include recurrence counts for repeating issues; note agreement levels, carrying the `PCT% (X/N)`
  denominator, where relevant.
- Organize by phenomenon/theme where natural; note which items each finding appeared in.

## Output
Write to `{out_summary}` (= `summaries/{SET}_summary.md`):
- Header naming the set, then the factual summary.
Final message: terse, e.g. `wrote {SET}_summary.md`. Do NOT paste contents.
