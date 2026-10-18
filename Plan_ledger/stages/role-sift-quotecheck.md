# Role: sift quote checker — additions to the common briefs

Task: adversarially check the synthesis against the source, before anything goes to the owner.

Inputs: the synthesis; the chunk files; the earlier ledgers; the invariants doc.

Do:
1. Check every quote in the synthesis exists verbatim, typos included, in the chunk or ledger line it cites. Report silent corrections and index slips.
2. For each principle, tie-break step and default, give a verdict: **SUPPORTED**, **OVER-READ** (the quotes support a narrower rule), **WEAK** (fewer than two originated decisions), or **CONTRADICTED** (a later decision reversed it). Give the reason and a corrected rule.
3. Treat an owner picking an option the assistant offered, or saying yes, as accepted, not originated; flag any principle resting mostly on those.
4. Search the chunks for counter-evidence the synthesis missed.
5. Flag claims about the owner that no chunk or ledger line supports.

Output: a table per section (item, verdict, reason, corrected rule), then missed counter-evidence, then index slips.
