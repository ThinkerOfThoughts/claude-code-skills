# Role: contradiction pass and drift check in cascade mode — additions to your role file

Read this after `stages/common.md` and your role file (`role-contradiction.md` or `role-drift.md`), only when the planner tells you the run is in cascade mode. Normal-mode runs never receive it. It adds to your role file and replaces nothing in it, except where stated.

Inputs, in addition to yours: the principles sheet (required) and `stages/cascade-method.md`, section "Compliance", read in full. If the principles sheet is missing or unreadable, your whole result is the single line `MISSING: <path>`, in place of the output shape in your role file.

Your clean result (the contradiction pass's list of lines checked and found clean; the drift check's CLEAN) is judged as `stages/review-order.md` says ("What blocks"; the list: "The list for a spec"). A `[RULE:…]` tag records where a line came from; judge each line and each spec statement yourself, and do not take a line's tag or an earlier compliance record as having passed it.

Checks, added to those in your role file:
1. **Principles table.** After the invariants table, give the table of `stages/review-order.md` ("What a full review returns"; the list: "The list for a spec"). A `meets` row gives the ledger line or spec section and the words that show it; an `n.a.` row names what you checked. A departure the sheet's tie-break order requires is `meets (tie-break <id>)`; a conflict it does not settle is `conflict: <ids>`, a major finding routed as gap condition 2 after the mechanism test. A violated principle, default, ruling or tie-break entry is a blocker, whichever rule the line cites.
2. **Prior decisions.** Every OWNER and CONFIRMED line, and every ruling and default on the sheet that bears on the spec: `meets` or `violates`, with the words. A line that follows an owner line departing from a principle is `meets (owner line S<n>)` with `batch candidate: gap condition 3`; do not test owner lines against the principles.
3. **What the spec leaves out.** Ask the whole-job question (`stages/cascade-method.md` "The whole job") of each spec statement that prescribes how code or data is handled. Wording, process and policy statements are `n.a.`, naming those you checked.
4. **Verdict (drift check).** In place of item 7 of your role file: CLEAN or not as `stages/review-order.md` says ("What blocks"), over every check in your role file and above.
