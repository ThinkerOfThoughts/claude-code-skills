# Stage 6 — Exit gate: cold drift check, then hand-off

**Precondition:** invariants doc `status` is REVIEWED (owner has approved its lines); sheet approved at its
current version; stage 5 clean.

Spawn ONE fresh cold agent (sonnet, same reasoning as stage 5) with `stages/common.md` verbatim plus
`stages/role-drift.md`. Inputs: the ledger (the sheet with its quotes is the owner record), the
answered-messages file, the spec, the invariants doc, the adjacent goals. Make the answered-messages file
before spawning: for every owner message in the design conversation (from the ledger's `created:` date to now, with the
`[<OWNER> …]` lines, CONFIRMED lines and Owner statements entries among them, whatever their date), an entry holding the owner message's timestamp,
the planner message it answered (normally all the planner's text since the owner's previous message, and the
earlier message too if the owner's words refer back to one) and that message's timestamp; an owner message
with no planner message before it gets the entry `none: owner spoke first`. Make it as the Extract step of
`stages/cascade-first-use.md` makes its records (only what the owner typed, plus the owner's own AskUserQuestion answers, each with the planner's text before it, from `cascade.owner_transcripts`, which stage 6 reads in either mode; absent: stop and ask for it), keeping all of that text, not its tail, copied verbatim from the transcript (for an AskUserQuestion answer the planner's text includes the question and all its options, kept in full in the planner half; the owner half holds only the selected option or the typed text); by script or by a read-only agent, never from
memory, and save it next to the ledger as `<slug>-answered.md`. If one agent cannot read the file in full, split
it into chunks as that Extract step sizes its chunks and run `stages/role-drift.md` item 6 once per chunk with a fresh
agent, and merge the findings yourself; the agent that runs the other checks reads only the entries its owner lines key to. Optionally, if the config names a
drift-detector run, include it; the drift check does not depend on it.

The agent answers three questions per sheet line and per spec section: does the spec say what the owner's
quote means, read against the message it answered (not what the tag claims); does any spec mechanism lack an
owner-confirmed sheet line; does the spec, read literally, violate an invariant or defeat an adjacent goal.
It also compares the spec with every owner statement about a mechanism the spec applies, those in the ledger's
Owner statements section and any it finds in the answered-messages file that the section lacks (`stages/role-drift.md`
item 6). It also lists every "good to go" style confirmation in the Approvals section and checks that nothing written
after it introduced a mechanism the approved text did not state.

**Route:** any finding on an owner line, an invariant, or an adjacent goal → owner (paste the finding, not a
summary). A disagreement between the spec and an owner statement goes to the owner too, before the hand-off, in
the form item 6 of the role file gives, and the owner's answer is recorded on the entry; a statement the section
lacks is added to it and the check re-run, not sent to the owner. Findings only on DERIVED lines → fix and re-run. Clean → hand off. A finding that an owner line
has no answered message is fixed by adding the message and re-running, not sent to the owner.

**Hand-off** to the build lane / guarded-change: the approved sheet version, the spec, the ledger path,
and one line stating that build-time questions which change a mechanism class come back as stage-7 forks.
Record the hand-off in the ledger with the spec's hash or commit. Do not narrate the hand-off to the
owner beyond one line.

> **Cascade mode** (only in cascade mode): also give the agent `stages/role-review-cascade.md`, the principles sheet (required: the pass is invalid without it) and `stages/cascade-method.md`, and tell it to treat a `[RULE:…]` line as a provenance record, as `stages/cascade-method.md` "Derived lines" explains, while judging every line against every principle itself (its CLEAN means the sheet and spec meet every principle and prior decision); the precondition "sheet approved" means the principles sheet is approved and every level's batch has its Approvals entry, and a finding on a RULE line alone routes like one on a DERIVED line.
