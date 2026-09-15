# Stage 3 — Sheet

The **decision sheet** is the Decisions section of the ledger: numbered sentences with provenance tags,
plus the invariants table and the Open forks list. It is the artifact the owner approves. The builder spec
(stage 4) is derived from it, never the other way round.

**Paste it in chat.** File links are not reliable in the client; the owner reviews what is in the chat.
Paste the sheet verbatim, under a heading with its version number, and ask for approval of that version.
Do not paraphrase it, shorten it, or add commentary between the lines. If it is long, it is long; that is
the cost of the owner reviewing the real thing.

**What approval means.** The owner's reply is recorded in the ledger Approvals section as
`sheet v<N> — <ts> "quote"`. Approval of v<N> covers exactly the lines in v<N>. Any later change to a line
bumps the version and requires a fresh paste of the changed lines (not the whole sheet) and a fresh
approval quote.

**Before pasting**, check: no line is UNCONFIRMED or INHERITED without an explicit "OPEN fork" note; every
direction-carrying line has a confirmation quote for the sentence; every invariant row is filled with the
proving line number; the Owner questions list has no OPEN items. If any check fails, fix it first (stage 1
or 2); do not ask the owner to approve a sheet with known holes.

**After approval**, rotate the Secret token, record the version, proceed to stage 4.
