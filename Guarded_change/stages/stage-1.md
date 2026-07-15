# Stage 1 — Spec

**What this stage does:** write a rich problem definition — what needs to be done and why —
deep enough that the plan and criteria can be derived from it without guessing intent.

## Procedure

Write `1-spec.md`: the problem, why, constraints, prior art. Rich enough to derive the rest.
Declare the expected **touched files** — the list joins every cold reviewer's context.

## Rules governing this stage

**Spec = rich problem definition; declares expected touched files (ST1).** A rich problem
definition: what's wrong / wanted, why, constraints, prior art. Deep enough that the plan and
criteria can be derived from it without guessing intent. The spec also **declares the expected
touched files** — that list joins every cold reviewer's context (see the charter's closed
set).

**An escalated fidelity finding is closed by a ratification record, not a bare ruling line
(RAT1).** When an "OWNER MUST RATIFY" fidelity finding is resolved, the spec records a
**ratification record** — the flagged axis + the options presented (verbatim), the owner's
response (verbatim, **with a durable source: the chat-transcript line (acceptable even for a
just-made live ruling) or a timestamped, owner-attributed `decisions.md` entry** — the test is
the owner's *quoted words with a locus*, not the author's paraphrase), and the mapping to the
selected option — **not** a bare `## X (OWNER RULING <date>, option c)`. The cited source is what
makes the ruling **re-confirmable** across autonomous runs and context compactions (a later
reader re-checks the mapping *and the quote against its source* instead of trusting a re-typed
reconstruction) and is what the stage-3 audit (CH11) spot-verifies. A **partial or adjacent**
owner answer is not a ratification — re-ask the flagged axis rather than resolving it into a
recommended option. Full statement in `stages/stage-3.md` (RAT1).
