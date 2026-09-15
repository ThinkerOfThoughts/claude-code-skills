# Plan Ledger — keeping a spec honest about who decided what

Plan Ledger is a small discipline, and a Claude Code skill that runs it, for the planning phase of
AI-assisted work: the stretch where a human owner and an AI planner talk a design through and the AI
writes the spec a build lane will follow. It is the sibling of [guarded-change](../Guarded_change/)
(build), [Dragonfly](../Dragonfly/) (diagnose) and [Data-Distiller](../Data-Distiller/) (distill).

## The failure it guards against

A spec written by an AI planner ends up containing decisions the owner never made, written in the same
voice as the decisions the owner did make. Three real instances from one feature's planning:

- A research agent's recommendation ("add semantic search as the fallback for keyword misses") became the
  spec's default. The owner's design was the opposite. The owner answered a one-word option to a
  question whose premise was inverted, and the spec shipped backwards for a day.
- The owner approved "build the relevance decision properly, not a threshold". The planner then wrote a
  hardcoded constant into the spec, four times, described as the virtue of the new design. Fixed versus
  derived was never posed as a choice. The constant shipped.
- A pre-existing side database was inherited as "where the data already lives". Nobody ever decided
  that. The spec's "keep this change disjoint from the neighbouring migration" rule reproduced exactly
  the fragility that migration existed to remove.

An audit that re-derived the design from the transcript passed all three, because the owner's standing
principles were not an input, and because a later "good to go" was read as approving sub-decisions the
proposal never stated.

## The four rules

1. **Provenance on every decision.** Each line of the decision sheet carries the owner's own quote and
   timestamp, or a tag saying who proposed it and whether the owner confirmed that sentence, or a tag
   saying the code already does it and nobody has decided. Only the first two count as decisions.
2. **Directions are confirmed as sentences.** Anything with an ordering, a default, or a fallback is read
   back as "X runs first; Y runs only when …" and the owner confirms the sentence, never a label.
3. **Forks are always posed.** A choice of mechanism class inside an approved direction (fixed vs derived,
   side store vs on-row, sync vs background, constant vs tunable, which is primary …) is put to the owner,
   named plainly, even when the planner has a preferred answer.
4. **Invariants are a file.** The owner's standing architecture rules live in a short checkable document
   that every cold reviewer receives and reports against.

## The loop

`setup → capture → forks → sheet (pasted in chat, approved by version) → spec (derived from the sheet,
current design only) → cold contradiction pass → cold drift check → hand-off → build-time forks route
back → close`. Details in `SKILL.md` (router) and `stages/`.

## Using it

- As a skill: `/plan-ledger` at the start of any planning conversation, and again after a compaction (the
  ledger file is the state; the session is not).
- As a checklist by hand: for every line in your spec, can you point at the owner's words that decided
  it? If not, is it a fork you should ask about, or a thing the code already did that nobody chose?
- It needs a per-project config (`plan-ledger.<project>.md`) naming the invariants doc, the ledger
  directory, the inherited stores and the adjacent goals. See `METHODOLOGY.md`.
