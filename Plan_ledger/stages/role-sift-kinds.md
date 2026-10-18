# Role: sift decision-kind sorter — additions to the common briefs

Task: sort the decisions in the project's earlier plan ledgers by kind, so recurring kinds can get a default.

Inputs: the earlier ledgers (their Decisions lines carry provenance tags as `stages/stage-1.md` "How a line is written" defines them) and the class list in `stages/stage-2.md` "Mechanism classes that are always forks".

Do:
1. Give each decision line one primary kind (one optional secondary). Start from the stage-2 classes; add a kind only when several lines fit none of them, and state how many.
2. Count per kind: lines tagged OWNER or CONFIRMED against lines that are derived or proposed.
3. Name the kinds where the owner's own decisions disagree with each other, with the line ids.
4. State your counting rules, including how you treated superseded and unconfirmed lines.

Output: a table (kind, owner/confirmed count, derived count, three example line ids), the list of inconsistent kinds, the counting rules. Also return a raw label list (line id, kind) so the counts can be recomputed.
