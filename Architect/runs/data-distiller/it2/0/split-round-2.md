# Proposed division — round 2

## The granularity floor (verbatim, as given to the divider)

> A step a competent practitioner can execute without further planning: concretely, one file
> created or one coherent edit to one file, with the content that goes in it specified.

## The task (verbatim, as given to the divider)

> Plan the implementation of the Data-Distiller skill.
>
> WHAT DATA-DISTILLER MUST BE — a Claude Code skill (a directory of markdown prompt files,
> invokable by name) implementing a cold, multi-agent method for extracting trustworthy,
> source-cited factual findings from a corpus too large to fit in one context window. Its
> defining properties:
>  - Decompose the corpus into analyzable items, size them, and pick a per-item strategy when an
>    item does not fit.
>  - N independent cold analyst agents per item; each is read-only over the corpus and cites a
>    source for every finding.
>  - A cold verification pass that re-checks every citation and drops the unverifiable.
>  - A merge that ranks surviving findings by how many independent analysts agreed.
>  - A blind roll-up: a coordinating agent never reads the findings themselves, only a terse
>    per-child status, so its expectations cannot steer them.
>  - A per-corpus configuration file supplies corpus specifics (what an analyzable item is, what
>    is off-limits, the concurrency ceiling); the method itself stays corpus-agnostic.
>  - Restart and resume from on-disk state.
>  - Facts, not interpretation.
>
> SOURCE MATERIAL — these are what the plan must be checked against:
>  - /home/zero/Desktop/claude-code-skills/Guarded_change/ — a working sibling skill. Its
>    SKILL.md, METHODOLOGY.md and stages/ show the house shape: a SKILL.md router carrying YAML
>    frontmatter (name, description), a METHODOLOGY.md reference spec, one file per stage under
>    stages/, and a per-project config file.
>  - /home/zero/Desktop/claude-code-skills/Dragonfly/ — a second working sibling skill in the
>    same shape.
>  - A skill is installed by being present at ~/.claude/skills/<name>/.
>  - The skill is to be built at /home/zero/Desktop/claude-code-skills/Data-Distiller-impl/ .
>
> OFF LIMITS: /home/zero/Desktop/claude-code-skills/Data-Distiller/ is a finished implementation
> of this skill. Do not read it, do not list it, do not grep it. The plan is to be derived, not
> copied.

---

## The cut, in one sentence

**Cut along the audience of the file** — the line the house shape already draws. Sub-task A plans
the files that are **read verbatim by a dispatched agent as its prompt** (everything under
`stages/`, including the common core every dispatched agent reads). Sub-task B plans the files
that are **read for orientation, routing and setup by whoever invokes the skill** (`SKILL.md`,
`METHODOLOGY.md`, `README.md`, the Layer-2 config template) plus the install step. The seam is a
small, one-directional interface: A publishes a stage index, a config-key list, and a completion
marker per stage; B consumes exactly those and nothing else.

This line is not invented for the split. `Guarded_change/METHODOLOGY.md:8–11` states it in the
source material's own words: the per-stage procedure and its rules "now live in `stages/` (one
file per stage, plus the shared red-team charter `stages/charter.md`); `SKILL.md` is the router
that walks the loop and points at those files. **This file is opened for orientation and config
setup — not to run a stage.**"

## Sub-task A — the method's operative prompt files (`Data-Distiller-impl/stages/`)

**Plan every file under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/`** —
the prompts a dispatched agent reads verbatim and acts on. A owns the *method*: what each agent is
told to do, in what order, under what constraints.

In scope — one file per stage of the pipeline, plus the shared core:

- **The common core** every dispatched agent reads first (coldness and independence, read-only
  over the corpus, cite-every-finding, facts-not-interpretation, where output goes, what a
  returned status must contain). Role files add to it and never restate it.
- **Decomposition, sizing and per-item strategy.** How a corpus is cut into analyzable items,
  how an item is sized against a context budget, and — the hardest case, the one the skill exists
  for — the rule that picks and *executes* a strategy when an item does not fit in one pass.
  A owns both picking and executing, so the strategy has one owner end to end.
- **The analyst stage.** N independent cold analysts per item; read-only; a source cited for
  every finding; facts not interpretation.
- **The verification stage.** A cold pass that re-checks every citation and drops the
  unverifiable.
- **The merge stage.** Rank surviving findings by how many independent analysts agreed; emit the
  item's findings artifact and the item's terse status line.
- **The coordinating-node stage.** How a node drives its children, enforces the blindness rule
  (it reads only a terse per-child status, never the findings), observes the concurrency ceiling
  at the point of spawn, and rolls status upward.
- **The terminal roll-up stage.** Whatever produces the run's corpus-level deliverable from the
  per-item findings artifacts. The task's invariant forbids findings to a **coordinating** agent;
  A must decide — and state — whether the terminal assembly is a coordinating agent under that
  reading, and therefore whether the corpus-level result is assembled from findings or is a
  manifest over them. **This is an open design question A must resolve, not a gap in the cut**:
  it is a question about the method, and the method is entirely A's.
- **Failure and retry semantics per stage** — what happens when an analyst returns nothing, when
  verification drops every citation for an item, when an item is unanalyzable — expressed as
  permitted status values plus a retry/abandon rule in the relevant stage file.

A also decides, as a consequence of the above, whether the blindness rule binds only nodes above
the item or also the per-item merger that reads N analysts' outputs. Both agents have children;
the task's word is "coordinating". A owns pinning that term.

Out of scope for A: `SKILL.md`, `METHODOLOGY.md`, `README.md`, the config template file, the
install step, and the *shape* of the Layer-2 config contract. A declares the config keys it needs;
it does not author the contract.

Source material A must be checked against: `/home/zero/Desktop/claude-code-skills/Guarded_change/stages/`
(`charter.md` as the shared-core example; `stage-*.md` as the per-stage prompt shape) and
`/home/zero/Desktop/claude-code-skills/Dragonfly/stages/` (same, second example).
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits.

## Sub-task B — the package: router, reference spec, config and install

**Plan every file at the top level of
`/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`**, and the step that installs the
skill. B owns *orientation, routing and setup*: how the skill is found, invoked, resumed and
configured.

In scope:

- **`SKILL.md`** — the router. YAML frontmatter (`name`, `description` — the description is the
  trigger text, so it carries when to use the skill and when to suggest it); the input list
  (the corpus, the Layer-2 config, and what to do when the config is missing); the run-start
  procedure; the **top-level resume instruction** (on invocation, if a run folder exists, read
  the run log and continue from the first incomplete unit); the stage-index table pointing at
  every file A plans; and the stop-for-human conditions.
- **`METHODOLOGY.md`** — the orientation/reference spec: why the method exists and the failure
  modes it guards; the pipeline diagram; the two-layer split (agnostic core vs. per-corpus
  config); the config contract; **what a run produces** — the run-directory layout, the artifacts,
  and the run-level outcome states.
- **`README.md`** — human-facing orientation, if the house shape warrants one (both siblings
  ship one).
- **The Layer-2 config contract, and a shipped template/example config file** at the top level
  (the siblings' `guarded-change.companion.md` / `dragonfly.companion.md` occupy this slot). The
  contract must contain every key A declares — at minimum what an analyzable item is for this
  corpus, what is off-limits, the concurrency ceiling, and the analyst count N — with the rule
  that no corpus specifics appear anywhere outside it.
- **Installation.** How the built skill reaches `~/.claude/skills/<name>/`. **The task fixes the
  build location but not `<name>`** (it states only the pattern). B chooses and justifies the
  installed name, and the install step must **check for and refuse to overwrite an existing
  directory at that path** — a `data-distiller` skill is already installed in this environment,
  so a naive `cp -r` to `~/.claude/skills/data-distiller/` would destroy an existing artifact as
  an unplanned side effect. B may verify the collision by listing `~/.claude/skills/`; B may not
  read `/home/zero/Desktop/claude-code-skills/Data-Distiller/`.

Out of scope for B: the content of any file under `stages/`; the analyst, verification, merge,
node or roll-up procedures; the blindness rule's formulation; the findings-artifact format; the
sizing and over-size strategy.

Source material B must be checked against: `/home/zero/Desktop/claude-code-skills/Guarded_change/`
— `SKILL.md:1–4` (frontmatter), `SKILL.md:13–24` (inputs), `SKILL.md:26–52` (router + stage
index), `SKILL.md:54–73` (stop-for-human); `METHODOLOGY.md:67–84` (stage index),
`METHODOLOGY.md:88–101` (two layers), `METHODOLOGY.md:103–151` (config contract),
`METHODOLOGY.md:154–196` (what a run produces) — and
`/home/zero/Desktop/claude-code-skills/Dragonfly/` (the same files, second example).
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits.

## The seam

**S1. The partition is by path, and it is mechanically checkable.** Every file A plans is under
`Data-Distiller-impl/stages/`. Every file B plans is at the top level of
`Data-Distiller-impl/`. No file is planned by both; a path decides which half owns it.

**S2. Information flows A → B only.** The three declarations below are A's outputs and B's
inputs. Nothing flows B → A, so **A is planned first** and B is planned against A's published
declarations. There is no negotiation to arbitrate.

**S3. Declaration 1 — the stage index.** A publishes, for each file it plans: the filename, and
an **index-grade line** — not a bare purpose, but the content-level summary B's tables need
(`Guarded_change/METHODOLOGY.md:73` is the calibration: *"checkable, labeled accept bar;
position/concurrency criteria; self-check criteria"*). B writes `SKILL.md`'s and
`METHODOLOGY.md`'s stage-index tables from these lines and does not open A's files to write them.

**S4. Declaration 2 — the config keys.** A publishes every Layer-2 key its stage files read, each
with a meaning and a value type. B authors the contract's shape, defaults, validation rules and
template, and the contract must contain every key A declared. B may add keys the router itself
needs; B may not drop or rename one of A's.

**S5. Declaration 3 — completion markers.** A publishes, per stage, the on-disk marker that means
"this unit is finished and need not be re-run". B writes the router's top-level resume paragraph
and `METHODOLOGY.md`'s "what a run produces" against that list. B does not invent completion
conditions; A does not write the resume paragraph.

**S6. Both halves inherit this run-directory skeleton; neither chooses it.** It is fixed here, so
that S2's one-directional flow is not spoiled by B owning a layout A must write into. Derived from
the siblings' `changes/<slug>/` (`Guarded_change/SKILL.md:27`) and `hunts/<slug>/`
(`Dragonfly/SKILL.md:31`):

- `runs/<run-slug>/` — one folder per distillation run;
- `runs/<run-slug>/items/<item-id>/` — one folder per analyzable item, holding that item's
  findings artifact and status;
- an append-only run log at the run folder's root.

A names files inside this skeleton and states what each contains. B documents the skeleton in
`METHODOLOGY.md` and points the router at it. Neither may change its shape unilaterally.

**S7. Concurrency has one key and one enforcement point, on opposite sides, and that is
deliberate.** B's contract declares the ceiling key and the template gives it an example value.
A's coordinating-node stage file states the check-before-spawn rule, because the only spawn sites
are in A's files. B never writes an enforcement instruction; A never sets the value.

**S8. The blindness invariant is wholly A's.** Both the agent constrained by it (the node) and
the agent whose output feeds it (the merge, which defines the terse status) are A's files, so the
rule is authored and enforced in one half and no cross-seam widening is possible. B states in
`METHODOLOGY.md` that the property exists and why; B does not formulate the rule and cannot
weaken it, because B writes no prompt any agent executes.

**S9. What neither half owns.** The corpus itself, and any example corpus — the skill is
corpus-agnostic and no corpus is in scope. The build location
(`/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`), which the task fixes. Reading
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`, which is forbidden to both.

## Why this is a real joint, not a bisection

Four things genuinely change at this boundary:

- **The reader.** A's files are consumed **verbatim, by a dispatched agent, as instructions it
  must execute**. B's files are consumed **by the invoking session, for orientation and routing**.
  `Guarded_change/METHODOLOGY.md:11` draws exactly this line: that file "is opened for orientation
  and config setup — not to run a stage."
- **The failure mode of getting it wrong.** A bad stage file makes an agent do the wrong thing
  on every run. A bad `SKILL.md` or `README.md` makes the skill fail to trigger, or misorient a
  human — a discovery and setup failure, not a method failure.
- **What must be corpus-agnostic vs. what names the corpus.** B owns the one place corpus
  specifics may live (the Layer-2 contract and template). A's files must contain none.
- **The authorship discipline that applies.** A's files are a multi-role prompt set: a common
  core included verbatim plus additions-only role files, which is a constraint on how they are
  written. B's files have no such constraint.

## Why both halves are above the floor

The floor is one file with its content specified. A must decide the content of, at minimum, a
common core, a decomposition/sizing stage, an analyst stage, a verification stage, a merge stage,
a coordinating-node stage and a terminal roll-up stage — and the number and boundaries of those
files are themselves still open, which is planning work, not execution. B must decide the content
of `SKILL.md`, `METHODOLOGY.md`, a config template, probably `README.md`, and the install step,
each of which is a document whose sections are not yet determined. Neither half is a single file
whose content is already specified; neither is executable without further planning. Neither falls
below the floor.
