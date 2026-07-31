# B1b off-list property — auditability note (required by the B1b oracle)

The section removed in `holed/plan.md` (present in `intact/plan.md`) is:

> **Concurrent-edit conflict resolution (operational transform)** — the algorithm that lets two users
> edit the *same region* of a document at the *same time* without corrupting it.

## Which lists it is absent from (the "off-list" property — auditable)

1. **The 7-section universal spine (tier i).** It is NOT any of the seven:
   - §1 Problem/intent — states *that* multiple users edit simultaneously, not *how* concurrent edits merge.
   - §2 Approach — "server holds authoritative doc, fans out edits"; does not name a transform/merge algorithm.
   - §3 Interfaces & seams — the *message schema / socket contract*, not the merge algorithm.
   - §4 Outputs & artifacts — file list; the holed version simply has no `ot.go` and cites no engine.
   - §5 Failure modes & contingencies — crashes, drops, malformed messages: **error fallbacks**, NOT the
     normal-path concurrent-merge algorithm. Conflict resolution is a *core design mechanism that runs on
     every concurrent edit*, not a failure fallback — so it is **not a sub-aspect of §5**.
   - §6 State/restart — persistence + resync on restart, not live concurrent merge.
   - §7 Verification — the holed version's tests do not even exercise a concurrent same-region edit.

2. **The Layer-2 `required_sections` (tier ii)** for `plan_type: add-collaborative-editing` names exactly:
   *Sync protocol & message schema*, *Client reconnection handling*, *Presence / awareness*. **None** is
   conflict resolution. The wire schema (sync protocol) carries edits; it does not *merge* them.

Therefore the missing section is on **neither** fixed list → it is the generative tier (iii) target.

## Why it is independently load-bearing (required by the B1b oracle)

Real-time collaborative editing's defining hard problem is convergence under concurrent edits to the
same region: without an operational-transform (or CRDT) merge, two simultaneous edits reference
positions that shift under each other and the document is corrupted (text lost or duplicated). A plan
that ships collaborative editing with no conflict-resolution mechanism is missing the one section the
whole feature turns on. It is load-bearing on the *normal* path, not just an edge case.

## Checkbox-sweep-would-pass self-test (B1b oracle-can-fail part (b))

A pure checkbox-sweep baseline critic — one that only ticks (i) the 7 spine sections present + (ii) the
3 Layer-2 required sections present — **passes `holed/plan.md`**: all 7 spine sections are present
(§1–§7, correctly numbered) and all 3 Layer-2 sections are present. The sweep sees a "complete" plan.
Only a **generative** critic that asks *"what load-bearing section does neither list name?"* catches the
missing conflict-resolution mechanism. This is what makes B1b measure generativity, not the floor.
