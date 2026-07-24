# Stage 2 — Human cut-gate

**What this stage does:** the method's **representativeness gate**. No subdivided or sizer-flagged
borderline item dispatches its analysts until a **human** has approved the atomic-unit choice, the
split points, the overlap, and the **argument that each cut preserves context**. A wrong cut wrecks
the whole item, so this gate is **mandatory and never auto-approved** for items in scope.

## Scope

- **In scope (blocks on human approval):** every item routed to **subdivide** (strategy b), plus any
  item the sizer flagged **borderline** (near a tier boundary, or where the atomic-unit choice is
  ambiguous).
- **Out of scope (auto-proceeds):** **clean-fit, clearly-tiered** items — a small item that fits one
  tier with headroom and needs no cut proceeds straight to stage 3 without stopping.

## Procedure

1. For each in-scope item, assemble the **cut-gate packet** and write it to `plan/cut-gate/<item>.md`:
   - the proposed **atomic unit** (what one piece is);
   - the proposed **split points** and **overlap** (against the Layer-2 `legal_cuts`);
   - the **context-preservation argument**: for each cut, why each resulting piece is
     *context-complete* — a finding that spans the seam is visible in at least one piece (the overlap
     is what guarantees this), and no piece is missing context needed to judge its content.
2. **STOP and present the packet to the human.** Ask for approval of the unit / splits / overlap /
   argument. This is a **stop-for-human** — do not proceed on the coordinator's own judgment.
3. **On approval unchanged:** record the approval in `plan/cut-gate/<item>.md` and `plan/decisions.md`;
   the provisional skeleton + budget stand; proceed to stage 3.
4. **On revision (human changes unit/splits/overlap):** **re-derive** that item's piece dirs in
   `tree/` and **recompute** its slice of the concurrency budget (`plan/budget.md`) from the approved
   splits, *before* any dispatch — nothing runs against a stale split. Record the revision + the
   final approved cut.
5. **Dispatch is forbidden until an approval record exists** for the item. A subdivided item with no
   `plan/cut-gate/<item>.md` approval MUST NOT have analysts dispatched.

## Rules governing this stage

- **Never auto-approve an in-scope item.** The gate exists because a mis-cut piece produces
  confident findings about incomplete context — the contamination is invisible downstream.
- **Approval is per-item and recorded.** The `plan/cut-gate/` packet is the audit trail; the merge
  stage's seam-aware dedup relies on the approved overlap being real.
- **Clean-fit items are not gated** — forcing a human decision on an obviously-fine small item is
  friction that trains the gate to be rubber-stamped. Keep the gate meaningful by scoping it to
  cuts + borderline calls.
- **Revision propagates before dispatch** (the stage-1 provisional marker exists precisely so this
  is clean).
