# Plan Ledger — keeping a spec honest about who decided what

Plan Ledger is a small discipline, and a Claude Code skill that runs it, for the planning phase of
AI-assisted work: the stretch where a human owner and an AI planner talk a design through and the AI
writes the spec a build lane will follow. It is the sibling of [guarded-change](../Guarded_change/)
(build), [Dragonfly](../Dragonfly/) (diagnose) and [Data-Distiller](../Data-Distiller/) (distill).

## The failure it guards against

A spec written by an AI planner ends up containing decisions the owner never made, written in the same
voice as the decisions the owner did make. Five real instances from real planning:

- A research agent's recommendation ("add semantic search as the fallback for keyword misses") became the
  spec's default. The owner's design was the opposite. The owner answered a one-word option to a
  question whose premise was inverted, and the spec shipped backwards for a day.
- The owner approved "build the relevance decision properly, not a threshold". The planner then wrote a
  hardcoded constant into the spec, four times, described as the virtue of the new design. Fixed versus
  derived was never posed as a choice. The constant shipped.
- A pre-existing side database was inherited as "where the data already lives". Nobody ever decided
  that. The spec's "keep this change disjoint from the neighbouring migration" rule reproduced exactly
  the fragility that migration existed to remove.
- An owner ruled that, in that case, mechanism X was the simplest option, on the strength of the planner's explanation of what X covered; the ledger kept only the owner's words. An hour later a proposal about another mechanism said in
  passing that its changes "go through the normal queue like everything else"; the owner answered
  "simplify", and the spec then applied X to every event, from every process.
- An owner described, as a question, how a queue worked. The planner treated it as a question and corrected
  the owner from a draft line that the owner had not written. The description stayed in a log line as a question, never became a statement or a decision, and the
  spec was built on the draft's version.

An audit that re-derived the design from the transcript passed the first three, because the owner's
standing principles were not an input, and because a later "good to go" was read as approving
sub-decisions the proposal never stated. A later drift check passed the fourth because it read the owner's
quotes without the messages they answered. No check compared the fifth, because the description was in no line
the checks compared.

## The five rules

1. **Provenance on every decision.** Each line of the decision sheet carries the owner's own quote and
   timestamp, or a tag saying who proposed it and whether the owner confirmed that sentence, or a tag
   saying the code already does it and nobody has decided. Only the first two count as decisions. An answer
   that depends on what the planner just said also records those words (a `rests on` clause).
2. **Directions are confirmed as sentences.** Anything with an ordering, a default, or a fallback is read
   back as "X runs first; Y runs only when …" and the owner confirms the sentence, never a label.
3. **Forks are always posed.** A choice of mechanism class inside an approved direction (fixed vs derived,
   side store vs on-row, sync vs background, constant vs tunable, which is primary …) is put to the owner,
   named plainly, even when the planner has a preferred answer. A "go" on a proposal confirms only the
   mechanism claims put on their own lines.
4. **Invariants are a file.** The owner's standing architecture rules live in a short checkable document
   that every cold reviewer receives and reports against.
5. **Owner statements are recorded, not corrected.** Whatever the owner says about how a mechanism works, a question or a half-remembered description included, is logged in their words with its
   transcript time, as a statement and not a decision, and no confirmation is asked for. A draft line that
   disagrees is not the owner's: the planner says where it came from, logs the disagreement and surfaces it
   when the topic wraps up. The drift check compares the spec with every statement, transcripts included.

## The loop

`setup → capture → forks → sheet (pasted in chat, approved by version) → spec (derived from the sheet,
current design only) → cold contradiction pass → cold drift check → hand-off → build-time forks route
back → close`. Details in `SKILL.md` (router) and `stages/`.

## Optional: principles cascade

For plans with many fine-grained decisions, `/plan-ledger cascade` turns on a mode for that ledger, and the ledger keeps it (the project config's `cascade.enabled` sets the default for a new ledger) in which a few owner-approved rules (a principles sheet, built once per project, optionally by sifting the owner's past messages) settle most decisions. Each design line cites the rule it derives from, a cold agent checks that each line meets every principle and prior decision (the rule a line cites says where it came from; it never makes the line pass), three cold judges settle the non-obvious ones, a cold red-team checks each level, and the owner is asked one batch per level: only what the rules cannot settle, plus the lower-confidence lines, with the rest listed for objection. The same procedure answers the builder's questions. In normal mode nothing changes. See `METHODOLOGY.md`, `stages/cascade-*.md`, `stages/role-*.md` and `stages/principles-sheet-template.md`.

## Using it

- As a skill: `/plan-ledger` at the start of any planning conversation, and again after a compaction (the
  ledger file is the state; the session is not).
- As a checklist by hand: for every line in your spec, can you point at the owner's words that decided
  it? If not, is it a fork you should ask about, or a thing the code already did that nobody chose?
- It needs a per-project config (`plan-ledger.<project>.md`) naming the invariants doc, the ledger
  directory, the inherited stores and the adjacent goals. See `METHODOLOGY.md`.
- Starters: `examples/` holds a filled-in, privacy-scrubbed principles sheet and invariants doc from a real
  project, to adapt rather than adopt as-is (blank templates are in `stages/`).
