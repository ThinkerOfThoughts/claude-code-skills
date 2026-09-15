# Stage 6 — Exit gate: cold drift check, then hand-off

**Precondition:** invariants doc `status` is REVIEWED (owner has approved its lines); sheet approved at its
current version; stage 5 clean.

Spawn ONE fresh cold agent (sonnet, same reasoning as stage 5) with `stages/common.md` verbatim plus
`stages/role-drift.md`. Inputs: the ledger (the sheet with its quotes is the owner record), the spec, the
invariants doc, the adjacent goals. Optionally, if the config names a transcript extract or a
drift-detector run, include it; the drift check does not depend on it.

The agent answers three questions per sheet line and per spec section: does the spec say what the owner's
quote means (not what the tag claims); does any spec mechanism lack an owner-confirmed sheet line; does
the spec, read literally, violate an invariant or defeat an adjacent goal. It also lists every "good to
go" style confirmation in the Approvals section and checks that nothing written after it introduced a
mechanism the approved text did not state.

**Route:** any finding on an owner line, an invariant, or an adjacent goal → owner (paste the finding,
not a summary). Findings only on DERIVED lines → fix and re-run. Clean → hand off.

**Hand-off** to the build lane / guarded-change: the approved sheet version, the spec, the ledger path,
and one line stating that build-time questions which change a mechanism class come back as stage-7 forks.
Record the hand-off in the ledger with the spec's hash or commit. Do not narrate the hand-off to the
owner beyond one line.
