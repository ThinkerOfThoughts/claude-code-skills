# TEMPLATE V — VERIFY

**One cold verifier per analysis list (letters match the analysts: 6 or 3 per item).** Each verifier
is an INDEPENDENT cold leaf with NO stake in the list it checks. Prepend the shared clauses.

---

You are a COLD verifier. You independently check ONE analyst's list against the actual data. You did
not write it and have no stake in it.

## Input list
`{in_path}` (= `tree/<…>/{item_id}/analysis/{LETTER}.md`) — a numbered list of flagged aberrations,
each with a cited source.

{SHARED CLAUSES — do-the-work + read-only + off-limits + ARTIFACT-CONTEXT BLOCK + per-item list}

## Task
For EACH numbered item in the input list, go to the cited source and check it against the data:
- **VERIFIED** — the cited source exists and genuinely shows what the item claims (a verifiable
  fact).
- **DROPPED** — the source doesn't exist, the locator is too vague/wrong to confirm, the data does
  not actually show the claimed thing, or the item is cause-speculation rather than a verifiable
  fact.
Do NOT add new findings. Do NOT soften or embellish. Facts only.

## Output
Write to `{out_path}` (= `tree/<…>/{item_id}/analysis/{LETTER}_verified.md`):
- Header naming the item + analyst {LETTER} (verified).
- A numbered list of VERIFIED items only, each preserving its description + confirmed source +
  snippet.
- Then `## Dropped` — each dropped item's original number + a one-line reason.
Final message: terse, e.g. `verified {item_id}_{LETTER}: 5 kept, 2 dropped`. Do NOT paste contents.
