# Proposed division — round 1

## The task being divided

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
>
> OFF LIMITS: /home/zero/Desktop/claude-code-skills/Data-Distiller/ is a finished implementation
> of this skill. Do not read it, do not list it, do not grep it. The plan is to be derived, not
> copied.

## Granularity floor (as given)

> A step a competent practitioner can execute without further planning: concretely, one file
> created or one coherent edit to one file, with the content that goes in it specified.

## Verdict: DIVISIBLE

## Sub-task A — the frame: router, reference spec, config contract, run-state

Plan the implementation of the **corpus-agnostic frame** of the Data-Distiller skill: the files an
invoking agent reads to orient and route, plus the contract every dispatched agent's prompt is
written against.

**Files this half plans (each step: one file, with the content that goes in it specified):**

- `SKILL.md` — the router. YAML frontmatter (`name: data-distiller`, `description:` written to
  trigger on "distill/sift/audit a corpus too large for one pass"); the inputs (the corpus + the
  Layer-2 per-corpus config); the stage/role index table naming every file under `stages/` with a
  one-line purpose and its path; the stop-for-human conditions; the self-check/dogfooding note.
  Matches the sibling shape at `Guarded_change/SKILL.md` and `Dragonfly/SKILL.md`.
- `METHODOLOGY.md` — the reference spec: why the method exists and what failure it prevents; the
  method in prose; the stage/role index; the two layers (corpus-agnostic method vs. Layer-2
  per-corpus config); **the config contract**; **what a run produces** (the on-disk artifact
  layout). Matches the section shape of `Guarded_change/METHODOLOGY.md` and
  `Dragonfly/METHODOLOGY.md`.
- A **worked per-corpus config template/example** file (the Layer-2 artifact), naming every key:
  what an analyzable item is, what is off-limits, the concurrency ceiling, N (analysts per item),
  and wherever else corpus specifics enter.
- The **on-disk run-state layout and restart/resume semantics**: the run directory, per-item and
  per-node directories and filenames, what a completed vs. in-progress unit looks like on disk,
  and how a restarted run decides what to redo and what to trust.
- A `README.md` (human-facing orientation, as both siblings carry one) and the **install step**:
  the skill is installed by being present at `~/.claude/skills/data-distiller/`.

**This half OWNS the vocabulary the whole skill uses**, and fixes it before the other half writes
a line: canonical role/stage names and their exact file paths under `stages/`; on-disk directory
and artifact names; the **field schema of the terse per-child status record** the blind roll-up
consumes; the **field schema of a finding record** (including the source-citation field and the
agreement count); the config key set; and the concurrency-ceiling semantics.

**This half does NOT write the procedure body of any dispatched-agent role.** It names each
`stages/` file and its one-line purpose only, and restates no procedure.

**Source material this half is checked against:** `Guarded_change/SKILL.md`,
`Guarded_change/METHODOLOGY.md`, `Guarded_change/README.md`, `Dragonfly/SKILL.md`,
`Dragonfly/METHODOLOGY.md`, `Dragonfly/README.md`, and the sibling per-project config files. The
`Data-Distiller/` directory is off limits.

## Sub-task B — the dispatched-agent prompts under `stages/`

Plan the implementation of the **`stages/` directory**: the prompt files that dispatched cold
agents read verbatim at run time. Each is a prompt, not documentation — the reader is an agent
with no context but this file.

**Files this half plans (each step: one file, with the content that goes in it specified):**

- A **common core** file, included verbatim by every dispatched agent: what a cold agent is, that
  it shares no context with siblings, read-only discipline over the corpus, cite-or-it-doesn't-
  count, facts-not-interpretation, and the output-file contract.
- **Decompose-and-size** — decompose the corpus into analyzable items, size each, and pick a
  per-item strategy when an item does not fit a context window.
- **Analyst (leaf)** — N independent cold analysts per item; read-only over the corpus; a source
  citation for every finding; facts, not interpretation.
- **Verify** — a cold pass that re-checks every citation and drops the unverifiable.
- **Merge** — rank surviving findings by how many independent analysts agreed.
- **Node / blind roll-up** — the coordinating agent: never reads the findings themselves, only
  the terse per-child status; enforces the concurrency ceiling; resumes from on-disk state.

Role files are **additions only and never restate a common rule**; if a role file needs to modify
a common rule, that rule was never common and moves down into the roles.

**This half CONSUMES the contract from sub-task A** and introduces no new artifact name, config
key, record field, or `stages/` file. Where it cannot avoid needing one, the plan step that needs
it carries an explicit `CONTRACT-DELTA:` line naming the addition, rather than silently
introducing it.

**This half does NOT write `SKILL.md`, `METHODOLOGY.md`, the config template, the run-state
layout, or the README.**

**Source material this half is checked against:** `Guarded_change/stages/` (all files, notably
`charter.md` and the stage files) and `Dragonfly/stages/` (all files, notably `charter.md`). The
`Data-Distiller/` directory is off limits.

## The seam

**What changes at this boundary.** Above the cut, files are read **once, by the invoking agent**,
to orient and route; they are documentation and vocabulary. Below the cut, files are read
**verbatim, mid-run, by cold dispatched agents** who have no other context; they are prompts, and
every word costs that agent's context budget. Different reader, different failure mode (a wrong
router mis-routes; a wrong prompt mis-executes), different authoring rule (reference spec may
restate for orientation; role prompts may not restate at all).

**What A produces that B consumes — the contract, names and schemas only:**
1. The exhaustive list of `stages/` file paths and each one's one-line purpose.
2. On-disk directory/artifact names and the run-state layout.
3. The terse per-child status record schema (the only channel across the blind-roll-up barrier).
4. The finding record schema, including the source-citation field and the agreement count.
5. The Layer-2 config key set and each key's meaning.

**What B produces that A consumes:** nothing at build time. B's only upward channel is a
`CONTRACT-DELTA:` line on any step that cannot be written within A's contract.

**What each may assume about the other.** B may assume every name, path, key and field it needs is
defined by A, and may cite them without redefining them. A may assume every `stages/` file it
names will exist and will contain the full procedure — so A must not restate a procedure, only
point at it.

**What neither owns** (out of scope for both halves, and not to be silently absorbed):
- The off-limits `/home/zero/Desktop/claude-code-skills/Data-Distiller/` directory.
- Authoring a per-corpus config **instance** for any specific real corpus (A owns only the
  template/example).
- Executing, testing, or evaluating a run of the finished skill against a real corpus.

## Why this joint and not the obvious alternative

The obvious alternative cut is **"everything about one item" (decompose/size, N analysts, verify,
merge) vs. "everything above one item" (blind roll-up node, recursion, concurrency, resume,
plus the packaging)** — cutting at the blind-roll-up barrier, which is the strongest joint in the
*domain*.

Rejected because it splits **single rules across both halves.** "The node never reads findings,
only the status record" is a rule two roles must act on; under that cut, the node's side and the
leaves' side land in different halves, and neither half can state the rule completely. Under the
proposed cut, the barrier's *schema* is a single contract item in A and both *procedures* live
inside B, where one author reconciles them. The alternative also puts the reference spec in one
half while the procedures it indexes sit in the other, which is precisely the "portion each half
assumes the other owns" failure.

## Floor check

Neither half is at or below the floor. A is ~5 files; B is ~6 files. Both remain coherent whole
tasks well above "one file with its content specified", so both can be divided again if the tree
warrants it.
