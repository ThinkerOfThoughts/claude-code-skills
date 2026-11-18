# Review order, what blocks, what a reviewer reads, and the runner

This file states these rules once. They apply in full to build answers, level drafts, and a finished spec (the contradiction pass and the drift check), in both modes.

## The order

Take these steps in order.
1. Planning lists the principles and owner lines that apply to the artifact (the list).
2. One full review of the whole artifact against the list. For an answer or a draft the reviewers are the compliance checker and the gap red-team (`stages/role-compliance-check.md`, `stages/role-gap-redteam.md`). For a spec the full review is one run of the contradiction pass and one run of the drift check.
3. Each finding that blocks (see What blocks) is fixed, and a reviewer checks only the changed lines against that finding (a fix check). Any other finding raised by this first review is fixed with no check.
4. A second full review of the whole artifact against the same list.
5. If the second review raises no blocking finding, Planning fixes its non-blocking findings, the changed lines are fix-checked where Fix checks requires it, and then the artifact is sent (an answer), its lines count toward the level's batch (a draft), or it hands off (a spec).
6. If the second review raises a blocking finding, it is fixed and fix-checked, and the artifact goes to the owner with those findings listed in plain words before it is sent (for a draft, before its lines count). There is no third full review.

## What blocks

A finding blocks only when it changes what the builder builds or contradicts something the owner said. The blocking test alone decides the route.

There are at most two full reviews, never a third. A full review checks the artifact against its list, and a second review that raises no blocking finding is a pass. A fix check, where one is required, covers only the changed lines, and a fix does not trigger a review of the whole artifact. In stage 5, in both modes, the two-bounce limit does not apply.

A reviewer may label a finding by severity in its report. The label does not decide the route.

## What a full review returns

A full review returns a table with one row per entry on the artifact's list, each row `meets`, `violates` or `n.a.`, and then its findings, each marked blocking or not. There is no table over every principle on the sheet, and no PASS, FAIL or HELD per line. A line counts when the order above completes for it. A conflict between two rules that the tie-break order does not settle goes to the owner through the gap rule (`stages/cascade-method.md`, "The gap rule").

## Fix checks

For a build answer, every line changed after the second full review gets a cold fix check, whether or not the finding behind it blocks. For a level draft or a spec, a blocking fix is fix-checked and any other fix is made with no check.

When a fix check fails, the fix is redone once and checked once more. If the second fix check also fails, the item goes to the owner with the finding and both attempted versions. There are at most two fix attempts per finding.

## Text put to the owner

A question or a batch put to the owner gets one full review and fix checks (steps 2 and 3 of The order), no second review. No separate list is written for it: its reviewer checks it against the principles sheet and the decision sheet it is given (see What a reviewer reads). A pile-up stop is a question and gets this review. The picture post and the notice of step 6 are neither a question nor a batch and get no review.

## The whole-job question

A full review of an answer or a draft asks the whole-job question on reuse. Reviewers of answers, drafts and specs do not run the per-operation audit. The trio judges keep it.

## The list for a spec

For a spec, the list is the ledger's approved decision sheet, which both passes read. Planning writes no separate list, and nothing is added to what the passes are given.

## What a reviewer reads

### A build answer

A reviewer of a build answer is given: the artifact, its list with the listed owner lines quoted in it, the principles sheet and the facts file. It may read code only to check the artifact's claim about which existing mechanism it reuses, and it finds that mechanism itself. It is not given the ledger or the transcripts.

### A level draft

A reviewer of a level draft is given what a build answer reviewer is given, and also the whole ledger; not the transcripts.

### The two spec passes

The contradiction pass reads the ledger, the spec, the invariants doc, the adjacent-goal sources and the config's `redteam_context` (`stages/stage-5.md`). The drift check reads the ledger, the answered-messages file, the spec, the invariants doc and the adjacent goals (`stages/stage-6.md`).

### A question or batch

A reviewer of a question or batch put to the owner is given: that text, the principles sheet, the facts file, and from the ledger only the decision sheet (the owner's decided lines with their quotes). Not the rest of the ledger, not the transcripts.

## The origin check

For a build answer or a level draft, a reviewer checks that each cited rule gives the answer and that each quote matches what it is given: the list's quoted lines for an answer, the ledger for a draft. It does not look quotes up in the transcripts.

## The runner

For a build answer or a level draft, Planning hands it and its list to one runner agent. The runner spawns the reviewers and returns to Planning two short plain-words lists: the blocking findings, and the non-blocking ones as one line each. Planning writes the fixes for both and hands back for the fix checks and the second review.

Planning itself spawns the two spec passes and the reviewer of a question or batch.
