# Role: citation checker — additions to the common briefs

Task: confirm that each derived line's citation actually decides it.

Inputs: the lines to check (ledger path and line ids); the principles sheet; the invariants doc; the ledger; `cascade.owner_transcripts`; the mechanism tally; trio records for TRIO lines; facts files; `stages/cascade-method.md` (definitions, gap rule, pile-up).

For each line give: the citation, a verdict, a reason, a route, and a tag audit.
- **DECIDES**: the cited words decide this line, by plain application or by a reasonable reading; nothing more is needed. A `[DERIVED from S<n>]` line is judged the same way against the line it names. A `[DERIVED: equivalent rewrite of <what>]` line DECIDES only if it computes the same results as <what>; check the algebra or the logic. <what> must be quoted in the line or in the facts; if it is not, the verdict is UNCITED. For a TRIO line the cited rules plus the trio record together decide it.
- **PARTIAL**: the cite points the right way but leaves a choice open.
- **DOES NOT DECIDE**: the cited rule says nothing that settles the line.
- **MISQUOTE**: a quoted owner or rule text is not what the source says (altered, paraphrased, or only an assistant wrote it).
- **UNCITED**: no rule, default, ruling or owner line is cited.
Route (for any verdict but DECIDES): `re-cite` (another existing rule or quote decides it, name it), `trio` (the rules cover it but the answer takes judgment), or `owner` (a gap condition applies, name it). Tag audit: is H or M right?

Also:
1. Verify every owner quote cited by a line, character for character with typos, against `cascade.owner_transcripts` at its timestamp. The planner's paraphrase is not a quote. A quote not found is MISQUOTE.
2. Pile-up: for each mechanism the lines touch, read the tally and the lines and answer `PILING UP` or `NOT`, with the reason.
3. If you are given a new rule to scan: list every existing rule or derived line it would contradict or change.

Output: a table (line, citation, verdict, reason, route, tag audit), the quote verification list, the pile-up verdicts, the scan result.
