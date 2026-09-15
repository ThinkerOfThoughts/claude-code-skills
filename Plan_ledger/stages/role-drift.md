# Role: drift check (stage 6) — additions to the common brief

Your job is to decide whether the spec says what the owner meant, using only the owner's quoted words in
the ledger as the record of what was meant.

1. **Meaning check per owner line.** For every `[<OWNER> …]` and `CONFIRMED` line: restate the quote's
   literal meaning in one sentence of your own, then compare it with the spec section that cites the line.
   Report any narrowing, widening, inversion (which runs first, which is the fallback, which is the
   default), or added condition. Pay particular attention to answers that were a single word or a letter:
   the sentence they confirm must be present as a quote, or the line is UNCONFIRMED.
2. **Approval scope.** For every entry in the ledger's Approvals section ("good to go", "send it", a sheet
   version approval): list the mechanisms the approved text stated. Then list every mechanism the spec
   contains that was written after that approval and is not on that list. Each is a finding unless a later
   owner quote confirms it.
3. **Provenance laundering.** Any spec passage or section header attributed to the owner ("<owner>
   2026-…", "ruled", "locked") whose content includes lines tagged PROPOSED, UNCONFIRMED, INHERITED, or a
   teammate self-resolution. Name each.
4. **Owner questions.** Every OPEN item in the ledger's Owner questions list is a major finding: an
   unanswered owner question means the owner decided without an answer they asked for.
5. **Invariants and adjacent goals**, as in the common brief, from the spec's literal text.
6. **Verdict:** CLEAN only if every check above has no finding of severity major or above. Otherwise list
   findings, owner-line findings first.
