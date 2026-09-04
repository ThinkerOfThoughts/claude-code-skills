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

**Refuse to start an un-runnable unit (RTS).** Before proceeding, the spec must answer: *"when
this run finishes, what will I execute, and what tells me it worked?"* If the honest answer is "I
will read the artifact and check it against itself" — no execution, no external oracle — the
**unit of work is wrong**. Either **widen it until it is runnable** (choose a larger unit that can
be executed end-to-end), or **declare it untestable-in-isolation and defer its verification to a
run of the assembled system**. This is the design-time form of the run-level rounds-without-a-run
cap (SEV5, `stages/stage-4.md`): answered honestly up front, the run never enters the trap the cap
catches late. (A unit is "runnable" when its acceptance has an external oracle that can fail — an
executed check against ground truth — not merely a re-reading of the artifact at ever-finer grain,
which a determined reader can always find a fault in.)

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
