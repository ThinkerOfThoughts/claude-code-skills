# Stage 5 — Cold contradiction pass

Spawn ONE cold agent (default model: sonnet, reason: semantic review of documents against documents; opus
only with a stated sonnet-specific shortfall). It receives `stages/common.md` verbatim plus
`stages/role-contradiction.md`, and read access to: the ledger, the spec, the invariants doc, the
`adjacent_goals` sources, and `redteam_context` from the config. It does not receive the transcript and
does not receive your summary of the conversation.

Run it in the foreground of your own turn (a delegated runner must never background a gated check).

**Route by the worst finding:**
- `blocker` (an owner line contradicted; an invariant violated; an unposed mechanism-class fork; an
  INHERITED store treated as decided): fix the sheet/spec or pose the fork (stage 2), bump the sheet
  version if a line changed, re-run the pass.
- `major` (underspecification a builder would resolve two ways; a spec statement with no sheet line): fix
  and re-run.
- `minor`: fix, no re-run needed.
- clean: proceed to stage 6 without asking the owner.

**Iteration cap:** two bounces at this stage on the same finding class → stop and bring the owner the
finding and the two attempts. Record every route in the ledger Decisions log.

> **Cascade mode** (only in cascade mode): also give the agent `stages/role-review-cascade.md`, the principles sheet (required: the pass is invalid without it) and `stages/cascade-method.md`, and tell it to treat a `[RULE:…]` line as the provenance record its mechanism checks ask for, as `stages/cascade-method.md` "Derived lines" explains, while judging every line and spec statement against every principle itself. Its clean result means the sheet and spec meet every principle and prior decision.
