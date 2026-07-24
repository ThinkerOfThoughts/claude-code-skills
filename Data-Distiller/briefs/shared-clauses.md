# Shared brief clauses — dropped into every leaf dispatch

The coordinator fills `{PLACEHOLDERS}` from `index.md` per item and prepends the relevant clauses to
each leaf's brief. Kept on disk so a post-compaction coordinator reloads them verbatim. All leaves:
model per tier, `general-purpose`, write-capable, run in background; **findings go to FILES**; the
final chat message is a **TERSE confirmation only**.

Ported and **adapted** from the T1–T4 `AGENT_BRIEFS.md`. The read-only / off-limits / do-the-work
clauses are preserved (genericized paths); the analysis/verify/merge/summary templates are **adapted**
to the tier-driven count/model + the `PCT% (X/N)` agreement model (they do NOT preserve the old fixed
"3 Sonnet" / raw `[agreement=N]` method).

---

## ⛔ GLOBAL RULE FOR EVERY LEAF — DO THE WORK YOURSELF

You are a single worker. Do NOT spawn, delegate to, or launch any sub-agent (do not use the
Agent/Task tools). Read the files, do the analysis/verify/merge/summary yourself, write your output
file, and return a terse confirmation. A leaf that delegates instead of working is a failure. You
have everything you need.

## ⛔ READ-ONLY — DO NOT MUTATE OR COPY THE CORPUS

This is a forensic distillation of **saved** data. You may ONLY **read** the artifacts. Do NOT copy,
move, rename, delete, `chmod`, or write into any corpus directory. If you must inspect a database or
a large file, open it **in place, read-only** (e.g. `sqlite3 file.db "SELECT …"` — **never `cp` it
out to /tmp first**; a copy-out can trip a structural guard and is a mutation). Prefer the smallest
sufficient text artifact. Write ONLY to your assigned output file under the run-root.

## ⛔ OFF-LIMITS PATHS — NEVER OPENED, EVEN TO VERIFY A CITATION

These exact paths are **off-limits** and must **never be opened, listed, or grep'd — even to verify
a citation or a locator**: `{off_limits_paths}`. They appear (if at all) only as historical/text
context; they are NOT your targets. A plain read does not trip any machine guard — **this brief is
the only fence.** Your targets are exclusively the artifacts handed to you in this brief.

## SHARED ARTIFACT-CONTEXT BLOCK (Layer-2 slot — used by ANALYSIS + VERIFY)

`{artifact_context}` — the Layer-2 `artifact_context` block for this corpus, dropped in verbatim:
what the system under test is; what each artifact type is; **which fields are analytically
relevant**; and what is **legitimately in-context** (drawing on it is NOT a finding).

## Per-item artifact list (filled from index.md)

- **Item id:** `{item_id}`
- **Artifacts (with which field is the analytical signal):** `{artifact_paths}`
- **Prepared inputs (if the item was slimmed/subdivided):** `{prepared_paths}` — for a
  tag-replaced artifact, the descriptive tag is **ground truth** for what the removed blob was (so a
  hallucinated description of it is still a flaggable finding).
- **Degraded flags:** `{degraded}` — analyze whatever survives; explicitly note where a missing
  artifact limits what can be concluded.
- **Prior-knowledge ledger (optional, LABEL-ONLY, redacted):** `{ledger_path_or_none}` — use ONLY
  to recognize/label known phenomena. Do NOT use it to narrow the open mandate, and do NOT use any
  other outside knowledge, prior adjudications, or detector definitions.
