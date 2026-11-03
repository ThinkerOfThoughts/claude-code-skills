# Stage 1 — Capture

Runs continuously during the design conversation. After every owner message that decides, asks,
corrects something, or describes how a mechanism works, update the ledger before replying.

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

**A ruling that rests on an explanation.** Many owner answers mean something only beside what the planner
said: "in that case", "if so", "ok then", "simplify", a yes, a no, an option letter. When the owner's words
are such an answer, the OWNER or CONFIRMED line also records the explanation, after its tag: `rests on:
[<who> <ts> "words"]`, the planner's words the answer depends on, copied verbatim from the transcript,
including any sentence that says how far the mechanism reaches (which events, which processes, which paths,
which cases). The clause is not a provenance tag (the line still carries exactly one). The line decides what
the owner's answer names or accepts and no more; everything else the planner said in the clause is context
that limits how far the line reaches, never a decision. A label alone still confirms no direction (the
read-back rule below applies). Check every later line and every spec statement against the `rests on`
clauses as against any prior decision.

**Direction-carrying decisions (rule 2).** If the sentence contains an ordering, a default, a fallback, a
which-first, or a which-wins, do not record it from a label. Read it back to the owner on its own line in
the form "X runs first; Y runs only when <condition>" (or "the default is X; Y is chosen only when …"),
wait for the owner to confirm the sentence, and record the confirmation quote. If the owner's answer was a
label ("fallback", "b", "option 4"), the line stays UNCONFIRMED until the sentence is confirmed.

**Owner recollections are lookups too.** If the owner says "we decided X earlier" and the ledger says
otherwise, quote the ledger line and ask which stands. Do not agree from politeness and do not overwrite
the ledger from memory. Record the resolution. This covers claims about what was decided; a recollection of
how a mechanism works is an owner statement (below), and nothing is asked about it at that moment, whichever line
it disagrees with; a message that does both is treated as a statement.

**Reframing is a defect.** If an owner question is answered with a different question ("a model swap
doesn't fix this defect" in reply to "are there other models?"), that is an unanswered question. Keep an
`Owner questions` list in the ledger: question (quote), answered at (ts, quote) or OPEN. Close it before
posing anything new.

**Owner statements.** Anything the owner says about how a mechanism works, typed or given in their own
AskUserQuestion answer (the selected option or the typed text, never the assistant's question or the options it wrote that were not
selected), goes in the ledger's Owner statements section as an entry: their words verbatim (typos kept), the transcript timestamp,
and a one-line note of what they were working through. Descriptions, half-remembered descriptions and
questions that carry a description ("as I understand it, X does Y, not Z?") all count. An entry is a
statement, not a decision: it has no provenance tag and is never a sheet line, so a detail the owner has
misremembered cannot become the design by itself (a decision the owner makes is still written as a sheet line
under the rules above; the entry does not replace it). Ask for no read-back or confirmation of it when it is
made: the owner often works a design out by describing it and asking until the answer falls out, and each
confirmation request costs attention they are spending on the design.

When a statement disagrees with a line that is not the owner's (any line not tagged OWNER or CONFIRMED, or a draft
line with no tag), say in one line where that version came from, read from the line's tag and the ledger and not from memory ("the
draft says X, from a judge vote, not from you"), and carry on; if the statement was a question, that line is its
answer and closes its Owner questions entry. Never correct the owner
from such a line, and ask nothing about the disagreement at that moment. Name the line on the entry
(`Disagrees with: S<n>`, or the draft line's id; whatever its tag) and mark it OPEN. A disagreement with an owner line is logged and
surfaced the same way.

When the topic the owner was on wraps up (they have decided it, or move to another subject), before posing the
next thing: if the topic touched a mechanism the owner described, run the drift check's owner-statements check
(one fresh sonnet agent in the foreground, given `stages/common.md` verbatim, `stages/role-drift.md`, the ledger and the sheet and draft text on that
mechanism, told to run item 6 only) scoped to that mechanism, with the answered-messages file as `stages/stage-6.md` builds it. Then surface every OPEN disagreement on the topic, yours and the check's,
each as an owner question (one per call) in the form "while working out <X>, you said <A>; the spec says <B>,
which came from <Y>" ("the spec" meaning whichever draft, sheet or spec text applies the mechanism), followed by
the owner's words and the planner message they were answering. Add to the Owner statements section any statement the check found that it lacks, then
record the owner's answer on the entry; a sheet line changes only by the rules above.

**Superseded lines** are not edited in place: strike them in the changelog with the date and the line
that replaced them. The Decisions section always shows only the current design.

> **Cascade mode** (only in cascade mode): a decision derived from the principles sheet or from an earlier owner line is written as `stages/cascade-method.md` "Derived lines" says, with a `[RULE:…]` tag that is not an ownership tag, and goes through `stages/cascade-levels.md` before it counts. A derived line that goes beyond an owner line's `rests on` clause is treated as changing something the owner said directly (gap condition 3).
