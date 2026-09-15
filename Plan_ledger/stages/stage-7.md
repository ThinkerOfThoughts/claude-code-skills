# Stage 7 — During the build

The ledger stays ACTIVE while the build runs. Messages from the build lane are logged in the ledger's
Coordination log (timestamp, one-line gist, spec line cited), never relayed into owner-facing messages.

**Routing a build question:**
- Answerable from the spec by line reference → answer with the line reference and nothing else; if the
  builder could not find it, that is a spec defect: fix the spec wording so the next reader finds it.
- A genuine spec gap that does NOT change a mechanism class → resolve, add a `[DERIVED]` or
  `[PROPOSED:<you> | UNCONFIRMED]` line, and tell the owner in the next owner-facing message as one line.
- A gap that DOES change a mechanism class (see the stage-2 list) → it is a fork: pose it (stage 2), bump
  the sheet, then answer the builder. Never answer a mechanism-class question "from the design" on the
  owner's behalf.
- A builder self-resolution reported after the fact → record `[PROPOSED:<lane> | UNCONFIRMED]` and surface
  it on the sheet; it cannot be described to anyone as an owner ruling.

**Owner rulings relayed to the build lane** are quoted verbatim with the timestamp, and the relay is not
delivered until the build lane acknowledges the quote back. Log the ack.

**Milestones only.** The build lane reports stage landings and gate verdicts; the ledger records them.
Everything else stays in the build lane's own files.
