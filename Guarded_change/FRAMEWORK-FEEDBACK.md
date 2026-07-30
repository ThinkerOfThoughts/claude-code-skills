# guarded-change — framework feedback from skill use

Weaknesses / limitations / ergonomics encountered while **using** `guarded-change` to build other things.
Same convention as the live-test harness's `FRAMEWORK-FEEDBACK.md`: **append as more surface, keep each
entry cited so a framework-build chat can act without the originating context.** This file is feedback on
the skill, not a change log for it — a run folder under `changes/` is where a fix actually lands.

---

## G1–G4 — the orchestrator's ceiling is undefined, so "verify" absorbs the whole loop

**Source:** the Architect attempt-2 build, 2026-07-28 (`claude-code-skills/Architect/changes/charter-2026-07/`).
The loop ran in a subagent with the main session orchestrating, per the standing rule. Over one day the
orchestrator read the entire artifact under change, the full red-team reports, and guarded-change's own
`stages/stage-3.md` and `stages/stage-4.md` into the main session — each read individually defensible as
"verifying the runner's claims," all of them exactly the context the delegation model exists to keep out.

**Where it belongs:** `METHODOLOGY.md`'s delegation section already has the right seam — *"Orchestrator half
(a caller-side obligation, not skill-enforced)"* (~L219) — which today covers only **relaying stops without
answering them**. It bounds what the orchestrator may *say to the owner*, and says nothing about what the
orchestrator may *do to the artifact*. These four close that.

### G1 — research goes DOWN, not up
When a runner halts on something answerable from a file, the orchestrator should reply with **the file to
read**, not the answer. Reading it and paraphrasing downward satisfies "don't over-escalate to the human"
by breaking "don't run the loop inline" — the two obligations point opposite ways and only one is written
down. The runner has the same filesystem access the orchestrator does.
- **Observed:** the orchestrator read `stage-3.md` (RAT1/RAT2) and `stage-4.md` (the severity/demotion
  mechanism) to answer runner halts, then handed down summaries.

### G2 — verification is SAMPLING, not reproduction
Define the ceiling **as a closed list**, because an open-ended "verify its output" is what gets walked
through. The orchestrator's whole verification job, exhaustively:

> **Re-run its oracle once yourself; spot-check a handful of its citations; confirm the files it claims
> exist do; confirm hashes. If you want to know whether the artifact is any good, spawn a cold reviewer and
> ask — do not read it and decide.**

Nothing else. Absent a stated bound, each additional read looks like *more rigour*, and the pressure runs
one way only.

**The test to apply after any check:** do I now know more about **whether the runner is truthful**
(sampling — correct), or more about **the subject matter** (reproducing — I have started doing the loop's
job in the wrong place)?
- **Observed:** "verify its output" slid from *test the runner's claims* to *reconstruct the runner's
  reasoning* over roughly six exchanges, with no single step that looked wrong. The checks that stayed on
  the right side of the line were all one-command: `wc -l`, `grep -c`, `ls`, `sha256sum`, and pulling a
  single transcript record to test a single quotation.

### G3 — never read the artifact under change in order to judge it
If it needs judging, that is a **cold reviewer's** task. Checking a few lines against a specific claim is
fine; reading it to *decide* is not. Useful tripwire: opening a file inside the run's own working set — the
artifact under change, a stage doc, a reviewer record in full — means the line has been crossed.

**Why the ceiling is not merely about context economy:** reading the artifact in order to judge it makes the
orchestrator **a fourth reviewer with none of the safeguards** — no cold context (it wrote the runner's
brief), no charter, no lens discipline, no earned-clean requirement, and nobody reviewing it. So its verdict
is simultaneously the **least trustworthy** in the system and the **most authoritative**, because everything
the orchestrator concludes travels downstream as instruction rather than as a claim to be challenged.
- **Observed:** the orchestrator read all 237 lines of the artifact to answer a decomposition question that
  should have been delegated.

### G4 — delegate structure decisions with the QUESTION, not the answer
Hand down the owner's instruction plus *"propose a decomposition and justify it against the spec"* — not a
finished table of files. Otherwise the runner validates the orchestrator's design instead of deriving one,
and the loop's independence is spent on ratifying a choice already made.

**The operative line:** what came from the **owner** goes down as a **constraint** — verbatim, with its
transcript locus. What came from the **orchestrator** goes down as a **question**, or, where it genuinely
has a view worth stating, as a proposal **explicitly labelled as the orchestrator's and marked
challengeable**, so reviewers attack it rather than assume it.

Two reasons beyond "the runner should do its own thinking":
- **It launders orchestrator error into the artifact.** Once the runner builds the orchestrator's design,
  downstream cold reviewers see it as *the runner's proposal* and review the structure with nothing flagging
  its provenance. This is the exact path by which a fabricated statistic and an invented owner ruling
  entered this project's artifacts — orchestrator judgments arriving as premises rather than as claims.
- **The runner is usually better-informed.** It has read the artifact and run the reviewers; the
  orchestrator, under G2/G3, deliberately has not. Handing down a structure means the *less*-informed
  party's guess arrives as a specification.
- **Observed:** the orchestrator specified the six-file split; the runner confirmed it rather than
  producing it.

### Why this is more than context economy — the contamination channel
The delegation model's stated rationale is keeping loop noise out of the main session. That is real, but it
is the smaller half. **A puppeting orchestrator becomes a contamination channel.** In this build, two
orchestrator errors — a fabricated statistic (*"~85% of findings were caught by exactly one reviewer"*) and
an invented owner ruling (*"per-element harnesses are instruments, not gates"*, cited to a record containing
none of those words) — travelled **into** the runner through its briefs and were inherited as authority. The
runner could not catch either; they arrived as premises from above. **A cold reviewer caught both.**

The consequence for the skill: the independence in this system lives in the **reviewers**, not in the
runner. An orchestrator that steers harder does not buy quality — it lengthens the lever on its own errors
before anything independent touches them. Any fix here should probably also consider whether the
orchestrator's own inputs to the runner belong in the reviewers' context as claims to challenge.

## G5 — THE LOOP HAS NO TERMINATION CHECK WHEN THE UNIT OF WORK CANNOT BE RUN. Highest priority.

**This cost two days and a large amount of usage, and it was structurally guaranteed from the moment the
run started.** The loop did not malfunction; it was given a job with no exit condition and did exactly what
it does, indefinitely.

**The mechanism.** Guarded-change terminates at **stage 8**, and stage 8's terminating check is
**conformance** — does the built thing validate, load, and run. That check requires an artifact you can
**execute**. Give the loop a unit of work that is a *fragment* of a runnable thing, and stage 8 has nothing
external to conform to, so it degenerates into checking the text against itself. Reviewers, meanwhile, are
graded on finding defects, and at a fine enough grain a determined reader of any document always finds one.
The result is an unbounded loop in which every round is individually legitimate.

**Measured, on the Architect skill, 2026-07-28 → 30.** The design is ~142 lines of pseudocode. An
orchestrator split it into six numbered "elements" the owner never ratified and could not name. The first
element — a set of agent prompt files — went through **six review rounds and ~30 cold agents**, grew from
**237 to 1,454 lines**, and **was never once run**. Every finding came from reading the prompts
adversarially, because a fragment cannot be executed. By the final rounds the reviewers were arguing about
whether a prompt file could be edited to grant itself privileges — a threat model with no attacker, on an
artifact that had never done any work. The owner's reaction on being shown it: *"This is literally just
subdividing a task into atomic chunks and having a bunch of agents plan out each chunk, then sticking the
thing together. How in the hell has this resulted in..."*

### The check to add — at stage 1, before any work

**Refuse to start a run whose unit of work cannot reach stage 8's conformance check.** Concretely, stage 1
must answer: *when this run finishes, what will I execute, and what will tell me it worked?* If the honest
answer is "I will read the artifact and check it against itself," the unit is wrong. Two legitimate
resolutions, both already in the family's vocabulary: widen the unit until it is runnable, or declare the
piece **untestable in isolation** and defer its verification to a run of the assembled system — which is
exactly the owner's testing rule (below) applied one level up, to review rounds rather than test mechanisms.

### Tripwires, for a run already in flight

- **Rounds without a run.** N review rounds have completed and the artifact has never been executed. This is
  the signature and it is cheap to detect. It fired six times here and nothing was watching for it.
- **Growth against a fixed design.** The artifact is growing while the thing it implements is not. 237 → 1,454
  against a 142-line design should have stopped the run on its own.
- **Target drift in the findings.** Round 1 asks *"does this instruct the agent correctly?"*; round 5 asks
  *"could this be adversarially edited?"* When the questions stop being about whether the thing works and
  start being about whether it can be defeated, the loop has run out of real subject matter.
- **A fragment that has no consumer yet.** If the component's caller does not exist, nothing can exercise it,
  and every finding about it is necessarily hypothetical.

**Note the relationship to the isolation rule below.** That rule bounds rebuilds of a *test mechanism* at
three. This is the same failure one level up — unbounded iterations of *review* — and the same remedy
applies: past a small number of rounds with no external check, change the venue rather than running another
round. **Consider making the review-round count a first-class cap in the same way the gate-bounce cap is.**

## ISOLATION-vs-ASSEMBLED TESTING — the owner's rule, 2026-07-29

**Scope, per the owner: this is ONE ELEMENT of a fix for the measurement-apparatus problem, not the fix.**
It supplies a default and a stop. It does not address making an assembled-run test discriminating,
attributing an assembled-run failure back to a component, or the harness-reviews-the-harness recursion.
Treat the parent problem as open.

> "if a component can be tested in isolation, it should be. If testing it requires more than three
> iterations of the test mechanism, reconsider if it should be tested in isolation or on a test run of the
> assembled thing."

**Read it as:** default to isolation. **Count rebuilds of the test mechanism, not runs of the test.** At
more than three, stop building and decide — either this thing is not isolation-testable, or it belongs in a
run of the assembled system.

**The distinction it turns on, in the owner's words:** *"some components can only be properly tested in the
fully functional mechanism that they go in. This distinction has, on many occasions, resulted in days being
wasted trying to create increasingly elaborate test mechanisms to test trivial little things that would be
simplicity itself to test by just plugging them into the finished thing and seeing what happens."*

**So the failure is not "we tested too little" — it is refusing to notice that a thing is not
isolation-testable, and answering each failed harness by building a bigger one.** The three-iteration count
is what makes that noticeable from the inside, which nothing before it did.

**Where it belongs in the skill:** stage 1.5 (criteria) and stage 8 (harness) both currently let a
criterion demand isolation verification without ever asking whether the thing is isolation-testable, and
neither bounds harness effort. This rule supplies both the default and the stop.

### ⚠ ON IMPLEMENTATION — remove the interim copy from CLAUDE.md
G1–G4 are currently written as **user-level rules** in `~/.claude/CLAUDE.md` (Workflow section, the bullet
beginning *"Orchestrate has a ceiling"*) as a stopgap, because the skill does not enforce them. **When these
land in `METHODOLOGY.md`/`SKILL.md`, delete that bullet from `CLAUDE.md`** — leaving both is the two-copies
drift problem this repo has already paid for once, and a user-level rule silently overriding a skill rule is
worse than either alone.
