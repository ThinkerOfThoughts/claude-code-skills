# Cascade first use — build the principles sheet (once per project)

Run from the stage-0 hook, before stage 1. If the file at `cascade.principles_path` exists and records the owner's approval, load it and stop here. If it exists without approval, continue at "Wording rounds". If it is absent, ask the owner one ordinary question with these options: the owner states the principles; sift the owner's past messages (needs `cascade.owner_transcripts`); neither (then the mode cannot run: stop and tell the owner, and do not fall back to normal mode silently).

## From the owner's statements
Write each principle as one sentence with the owner's quote beside it. Also ask for the tie-break order, the defaults and the always-to-owner list; where the owner gives none, leave that part empty (a conflict between principles then falls under gap condition 2). Then go to "Wording rounds".

## From a transcript sift
Run these in order; every agent is spawned as `stages/cascade-method.md` "Spawning and records" says and returns text, which you save.
1. **Extract.** From `cascade.owner_transcripts`, write the owner's own messages into chunk files. Each record holds the timestamp, the source, the tail of the preceding assistant message (so one-word answers can be read) and the owner's text verbatim, typos kept. Take only what the owner typed: skip tool results, injected reminders, hook text, other agents' messages and compaction summaries. Number the records from 1 within each chunk and name the chunk in each record. Size chunks so one analyst can read a chunk in full. Create `cascade.records_dir` if it is absent and write the extraction method there.
2. **Analyse.** One `stages/role-sift-analyst.md` agent per chunk, independent.
3. **Sort kinds.** One `stages/role-sift-kinds.md` agent over the project's earlier plan ledgers in `ledger_dir` (skip if there are none; the kinds then come from stage 2's class list and the analyses). It reads ledgers, not the transcript, so it can run beside step 2.
4. **Synthesise.** One `stages/role-sift-synthesis.md` agent over the analyses, the kinds table and the invariants doc.
5. **Quote-check.** One `stages/role-sift-quotecheck.md` agent over the synthesis, the chunks, the ledgers and the invariants doc.
6. **Draft the sheet.** Build the sheet from the synthesis, applying the quote check's corrected rules; leave out what it marked WEAK or CONTRADICTED unless you put it to the owner as a question.

## Wording rounds
Paste the whole sheet in chat, verbatim, with its template layout. The owner replies item by item. Reword; split an item the owner calls two things stuck together (`P8` becomes `P8a`, `P8b`); turn two rules that point both ways into a ruling `R<n>` with the owner's words; re-paste only the changed lines. Repeat until the owner approves, and write the approval into the sheet's status line with the owner's quote. The tie-break order, the defaults for recurring decision kinds, and the always-to-owner list are part of the sheet and are approved the same way. Start the always-to-owner list with three stage-2 classes: a line of the invariants doc, a persona-facing string, and a new dependency, model or service.

## Reuse
The sheet stays at `cascade.principles_path` and later plans in the project load it. A plan may name a different sheet in its ledger. Read the sheet in full before editing it; additions come only through `stages/cascade-method.md` "Owner answers become rules".
