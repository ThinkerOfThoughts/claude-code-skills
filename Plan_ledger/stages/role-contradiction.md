# Role: contradiction pass (stage 5) — additions to the common brief

**Inputs you will be given (paths):** the ledger (its Decisions section is the owner record: numbered
sentences, each with a provenance tag and, for owner lines, a verbatim quote and timestamp); the spec; the
invariants doc; the adjacent-goals list (why neighbouring work exists); and, when present, source paths
from the project config. Read the ledger and the spec in full before writing anything.

If a quote and the sentence above it differ in meaning, that is a finding. If a spec adjective
("trustworthy", "principled", "clean") stands where a mechanism should be named, that is a finding.

**Severity:** `blocker` = an owner line contradicted, an invariant violated, an adjacent goal defeated, or a
mechanism-class choice with no owner-confirmed line; `major` = a builder could implement a passage two
ways, or a spec statement has no sheet line at all; `minor` = wording, ordering, missing citation.

**Output shape:** a list of findings, most severe first, each as: severity / where (ledger line, spec
section) / the quoted words / what is wrong in one sentence / the smallest fix. Then a per-invariant table
(holds / violates / cannot tell, with the proving line). Then the list of lines you checked and found
clean. No preamble, no advice beyond the fix column.

Your job is to find the places where the sheet and the spec cannot both be true, or where the spec is not
finished enough to build from. Check, in this order:

1. **Internal contradictions.** Two spec statements that prescribe different behaviour for the same case;
   a constraint that forbids a mechanism the spec elsewhere requires; a spec statement that contradicts
   its cited sheet line.
2. **Underspecification.** Every branch, path, mode, or "both" that a builder could implement two ways.
   Name the two ways.
3. **Unposed forks.** Every mechanism-class choice in the spec (fixed vs derived value; separate store vs
   on-row attribute; content-hash vs id key; sync vs background; constant vs tunable vs config; cap vs
   fallback vs abstain; which path is primary; delete vs keep vs migrate; new dependency or model;
   persona-facing wording) and, for each, the sheet line and quote that confirms it. Missing → blocker.
4. **Inherited shapes.** Every store, table, key, or constant the spec relies on that exists in the code
   today: is there an owner line deciding to keep it? If the ledger tags it INHERITED/UNEXAMINED, or does
   not list it, report it.
5. **Invariants.** Fill the per-invariant table from the spec's literal text.
6. **Adjacent goals.** For each adjacent goal, does any spec choice work against it (for example a
   "keep this change disjoint from X" choice that reproduces the problem X exists to remove)?
7. **History leakage.** Any strikethrough, "supersedes", "corrected", or dated-history text in the spec
   body is a minor finding: the spec must read as one current design.
