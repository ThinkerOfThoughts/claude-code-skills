# Stage 1 — Capture

Runs continuously during the design conversation. After every owner message that decides, asks, or
corrects something, update the ledger before replying.

**What counts as a decision.** Any statement that fixes a mechanism, a default, an ordering, a scope, a
storage shape, a cadence, a threshold policy, a name the persona sees, or an acceptance criterion.

**How a line is written.** One numbered line per decision, as a full sentence in the owner's meaning,
followed by exactly one provenance tag:

- `[<OWNER> <ts> "quote"]` — the owner said it. The quote is verbatim (typos included) and the timestamp
  is from the transcript, not estimated.
- `[PROPOSED:<who> | CONFIRMED <ts> "quote"]` — you, an agent, a research report, or a teammate proposed
  it and the owner confirmed THAT SENTENCE (quote the confirmation).
- `[PROPOSED:<who> | UNCONFIRMED]` — proposed, not yet confirmed. Cannot be described anywhere as
  "locked", "decided", "ruled", or "<owner> 2026-…".
- `[INHERITED:<where> | UNEXAMINED]` — the current code/data already does this and nobody has decided to
  keep it.
- `[DERIVED]` — a purely mechanical consequence of a confirmed line; name the line it derives from.

**Direction-carrying decisions (rule 2).** If the sentence contains an ordering, a default, a fallback, a
which-first, or a which-wins, do not record it from a label. Read it back to the owner on its own line in
the form "X runs first; Y runs only when <condition>" (or "the default is X; Y is chosen only when …"),
wait for the owner to confirm the sentence, and record the confirmation quote. If the owner's answer was a
label ("fallback", "b", "option 4"), the line stays UNCONFIRMED until the sentence is confirmed.

**Owner recollections are lookups too.** If the owner says "we decided X earlier" and the ledger says
otherwise, quote the ledger line and ask which stands. Do not agree from politeness and do not overwrite
the ledger from memory. Record the resolution.

**Reframing is a defect.** If an owner question is answered with a different question ("a model swap
doesn't fix this defect" in reply to "are there other models?"), that is an unanswered question. Keep an
`Owner questions` list in the ledger: question (quote), answered at (ts, quote) or OPEN. Close it before
posing anything new.

**Superseded lines** are not edited in place: strike them in the changelog with the date and the line
that replaced them. The Decisions section always shows only the current design.
