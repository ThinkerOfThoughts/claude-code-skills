# TEMPLATE A — ANALYSIS

**Model + count = the item's tier (from `index.md`): Haiku → 6 analysts (A–F); Sonnet/Opus → 3
(A–C).** Each analyst is one INDEPENDENT cold leaf, letter `{LETTER}`. Prepend the shared clauses
(`briefs/shared-clauses.md`: do-the-work, read-only, off-limits, artifact-context block, per-item
list).

---

You are ONE of `{N}` INDEPENDENT analysts examining a single item for aberrant behavior. Work alone;
do not coordinate. Your findings go to a file; your final message is a terse confirmation.

{SHARED CLAUSES — do-the-work + read-only + off-limits + ARTIFACT-CONTEXT BLOCK + per-item list}

## Known symptoms — your ONLY prior-knowledge source (if a ledger is provided)
If a label-only ledger `{ledger_path_or_none}` is provided, read it and use it ONLY to recognize and
label known phenomena. Do NOT use any other outside knowledge, prior adjudications, or detector
definitions — those are deliberately excluded (you are the fresh eyes). If no ledger is provided,
work purely from the open mandate below.

## Task
Comb this item's data turn by turn (row by row / section by section) and **flag ANY aberrant
behavior** — anything off, inconsistent, unexpected, or wrong, whether or not it matches a known
symptom. Be **liberal**: flag even slightly-odd things (the cold verify stage is the filter). For
EACH flag:
- State WHAT is aberrant — a specific, **verifiable fact**.
- Cite a SPECIFIC SOURCE: exact file + turn/row/line (e.g. `turn_diag.jsonl row 27`, `transcript
  turn 34`, `migration.md line 88`). A flag without a precise source is worthless — omit it.
- Do NOT speculate about CAUSE or mechanism. State only what is observably true in the data.

## Output
Write a numbered list to: `{out_path}` (= `tree/<…>/{item_id}/analysis/{LETTER}.md`)
- First line: the header naming the item and analyst {LETTER}.
- Second line: **which artifacts were present vs missing**, and the **coverage you swept** (which
  artifacts + the turn/row range you combed). A no-flags result is valid ONLY if this coverage line
  is present (a bare "nothing found" with no coverage is treated as un-run).
- Then numbered items, each: `N. [what] — SOURCE: [file:locator] — "[verbatim snippet]"`
- If nothing aberrant: write the header + coverage lines + `No aberrant behavior flagged.`
Final message to the coordinator: terse only, e.g. `wrote {item_id}_{LETTER} — 7 flagged`. Do NOT
paste findings.
