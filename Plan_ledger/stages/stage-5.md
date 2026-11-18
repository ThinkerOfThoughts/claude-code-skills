# Stage 5 — Cold contradiction pass

Spawn ONE cold agent (default model: sonnet, reason: semantic review of documents against documents; opus
only with a stated sonnet-specific shortfall). It receives `stages/common.md` verbatim plus
`stages/role-contradiction.md`, and read access to: the ledger (its `rests on` clauses included), the spec,
the invariants doc, the `adjacent_goals` sources, and `redteam_context` from the config. It does not receive
the transcript and does not receive your summary of the conversation.

Run it in the foreground of your own turn (a delegated runner must never background a gated check).

**Routes and limits:** as `stages/review-order.md` says. A fix that changes a sheet line bumps the sheet version. Record every route in the ledger Decisions log.

> **Cascade mode** (only in cascade mode): also give the agent `stages/role-review-cascade.md`, the principles sheet (required: the pass is invalid without it) and `stages/cascade-method.md`, and tell it to treat a `[RULE:…]` line as the provenance record its mechanism checks ask for, as `stages/cascade-method.md` "Derived lines" explains, while judging each line and spec statement itself. Each text of this stage that goes to the owner (`stages/review-order.md`, `SKILL.md` "Stop-for-human") is recorded as one `ANSWER` block of its own and stamped as "Record, stamp, post" in step e of `stages/cascade-levels.md` says, and is posted verbatim.
