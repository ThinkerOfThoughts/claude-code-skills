# Cascade build questions — plan-ledger stage 7 with the mode on

The builder's questions about the plan are answered the same way the plan was made. Messages from the builder are still logged in the Coordination log and not relayed to the owner in pieces. For each question:
1. **Answerable from the spec by line:** answer with the line reference and nothing else (unchanged from stage 7).
2. **Otherwise** look it up and derive it (`stages/cascade-method.md` "Order of work"). If it is non-obvious, run the trio.
3. **Record it** as a derived line with its citation and confidence, run the citation check (questions that arrive together are checked together), fix the spec wording, and relay the answer and the spec line only after the check says DECIDES.
4. **Gap or always-to-owner:** hold it for a build batch, in the layout of `stages/cascade-levels.md` step e, and post it as soon as the builder is blocked on an item in it, with everything accumulated; otherwise at the next milestone. Owner rulings are relayed to the builder as stage 7 says (verbatim, with the timestamp, acknowledged back).
5. **Review:** build-time M lines go on the build batch's review list; H lines are listed by id in the ledger at each milestone.
6. **Pile-up:** update the tally on every derived answer. Before each build batch and at close, run the citation check over all the build-time derived lines together, because each passes its own check and the pile is what the owner never saw. A `PILING UP` verdict is handled as `stages/cascade-method.md` "Pile-up" says.
A builder's self-resolution reported after the fact is still recorded as `[PROPOSED:<lane> | UNCONFIRMED]` (stage 7).
