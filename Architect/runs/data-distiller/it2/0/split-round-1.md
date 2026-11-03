# Proposed division — round 1

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

**Cut the task along the blind-roll-up line** — the invariant the task itself names. Everything
that happens *to one analyzable item* and produces that item's findings is one half; everything
that decides *what the items are*, drives the coordinating tree that must never read those
findings, and packages the whole thing as an installable skill is the other. The seam is the
blindness boundary itself: a terse per-item status line crosses it, and the findings never do.

## Sub-task A — the per-item analysis pipeline (below the blind line)

**Plan the files of `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/` that specify what
happens to ONE analyzable item**, from the moment a well-formed item handle is in hand to the
moment that item's findings artifact and its terse status line exist on disk.

In scope:

- **Sizing and per-item strategy.** How an item's size is measured against a context budget, and
  the rule that picks a strategy when the item does not fit in one pass.
- **The analyst role.** The prompt file(s) that make N independent cold analysts per item: their
  read-only constraint over the corpus, the requirement that every finding names a source, and
  the facts-not-interpretation constraint. Also: the *dispatch of the N analysts for this item*.
- **The cold verification pass.** The prompt file that re-checks every citation an analyst
  produced and drops the unverifiable.
- **The merge.** The rule and prompt file that rank surviving findings by how many independent
  analysts agreed, and emit the item's findings artifact.
- **Whatever is common to the agents this half dispatches** (analyst, verifier, merger), as a
  role-split common file if the sibling skills' shape warrants one.
- **The two outputs of this half**: the per-item findings artifact (format and content), and the
  terse per-item status line (its schema — fields and permitted values).

Out of scope for A: how the corpus is cut into items; the tree of coordinating agents; the
concurrency ceiling; the on-disk directory layout; restart/resume; the config file's contract;
`SKILL.md`; `METHODOLOGY.md`; installation.

Source material A must be checked against: `/home/zero/Desktop/claude-code-skills/Guarded_change/`
(especially `stages/charter.md` and the `stages/stage-*.md` files, as the house shape for a
role/stage prompt file) and `/home/zero/Desktop/claude-code-skills/Dragonfly/` (same, second
example). `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits.

## Sub-task B — decomposition, coordination, and the skill package (at and above the blind line)

**Plan the remaining files of `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`**: the
ones that turn a corpus into items, drive the coordinating tree over them under a blindness rule
and a concurrency ceiling, survive restart, and ship as an installable skill.

In scope:

- **Corpus decomposition.** The prompt file that decomposes a corpus into analyzable items and
  emits well-formed item handles.
- **The coordinating node / blind roll-up.** The prompt file(s) for a coordinating agent: it
  reads only terse per-child status, never the findings, and rolls child statuses upward. The
  blindness rule and its enforcement live here.
- **Concurrency.** The global ceiling on simultaneously-running agents and how it is enforced.
- **On-disk state, restart and resume.** The run directory layout, what marks each unit of work
  complete, and the rules for resuming a partially-completed run.
- **The Layer-2 per-corpus config.** The config contract (what an analyzable item is for this
  corpus, what is off-limits, the concurrency ceiling, the analyst count N) plus a shipped
  template/example config file.
- **`SKILL.md`** — the router, with YAML frontmatter (`name`, `description`), the input list, and
  the stage-index table that points at every stage file including A's.
- **`METHODOLOGY.md`** — the orientation/reference spec: why the method exists, the pipeline
  diagram, the two-layer split, the config contract, and what a run produces.
- **Anything else needed to install and orient** — the `README.md` if the house shape warrants
  one, and the step that puts the skill at `~/.claude/skills/data-distiller/`.

Out of scope for B: the content of any file A owns; the analyst/verifier/merge procedures
themselves; the findings-artifact format.

Source material B must be checked against: `/home/zero/Desktop/claude-code-skills/Guarded_change/`
(`SKILL.md` for the router shape and frontmatter; `METHODOLOGY.md` lines 67–84 for the stage-index
table, lines 88–152 for the two-layer split and config contract, lines 154–196 for "what a run
produces") and `/home/zero/Desktop/claude-code-skills/Dragonfly/` (same files, second example).
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits.

## The seam

**1. The item handle — B produces, A consumes.** B's decomposition emits an *item handle*: an
identifier, a locator into the corpus, and a size measure. A may assume a well-formed handle
exists and is stable; A never decides how the corpus is cut. B defines the handle's fields; A
declares which of those fields it needs (it needs at least the locator and the size measure), and
B must supply them.

**2. The findings artifact — A owns it entirely, and B must never read it.** A defines its
format, its content, and its filename convention *relative to the item's own directory*. B owns
where that directory sits (seam item 4). **B reading the findings artifact is the one thing that
would void the blind-roll-up property**, so B's plan must state the prohibition, not merely
refrain.

**3. The status line — A defines the schema, B defines the transport. This is the only channel
across the seam.** A specifies the fields and permitted values of the terse per-item status (what
a coordinating agent is allowed to know about an item). B specifies where a status line is
written, how a parent collects its children's, and how statuses aggregate upward. Neither half may
widen this channel unilaterally: **if B needs a fact about an item that the status schema does not
carry, that is a change to A's schema, not a licence for B to read the findings.**

**4. Completion markers — A declares, B places.** A states, for each unit of work it owns, what
on-disk marker means "this is finished and need not be re-run." B owns the directory layout those
markers live in and the resume logic that reads them. A does not design the layout; B does not
invent A's completion conditions.

**5. Concurrency — B owns scheduling; A owns the per-item fan-out.** A specifies that N
independent analysts run per item and that N comes from config. B specifies the global ceiling on
concurrent agents and how it is enforced across items. A does not schedule; B does not set N.

**6. Corpus-agnosticism — a shared constraint, with authorship on B.** Both halves must keep all
corpus specifics out of the method files and in the Layer-2 config. B authors the config contract.
**A declares its config requirements as a list of keys with meanings** (at minimum: N, the
off-limits set, and whatever the sizing rule needs) and B's contract must contain them.

**7. File-set disjointness.** Every file in `Data-Distiller-impl/` is planned by exactly one half;
no file is planned by both. `SKILL.md` and `METHODOLOGY.md` are B's. B writes their stage-index
entries for A's files from **the file names and one-line purposes A publishes**, not from A's
content — the same relationship `Guarded_change/METHODOLOGY.md:67–84` has with its own
`stages/` files. A must therefore publish, as part of its output, the list of files it plans with
a one-line purpose each.

**8. What neither half owns.** Neither half decides the skill's *name* or top-level directory
(both are fixed by the task: `Data-Distiller-impl/`, installed at `~/.claude/skills/`). Neither
half may read `/home/zero/Desktop/claude-code-skills/Data-Distiller/`. Neither half plans the
corpus that will actually be distilled — the skill is corpus-agnostic and no example corpus is in
scope.

## Why this is a real joint, not a bisection

Three things genuinely change at this boundary:

- **What an agent is allowed to see.** Below the line, agents read the corpus and produce
  findings. Above it, agents are forbidden the findings and see only status. That is the
  task's own named invariant ("a coordinating agent never reads the findings themselves"),
  and it is a property *of the boundary*, not of either side.
- **What the unit of work is.** Below: one item. Above: the whole corpus and the tree over it.
- **What varies per corpus.** Above the line, nearly everything is parameterised by the Layer-2
  config (what an item is, what is off-limits, the ceiling). Below it, the procedure is fixed and
  the config supplies only scalars.

## Why both halves are above the floor

The floor is one file with its content specified. A plans on the order of four to six files (a
sizing/strategy stage, an analyst role file, a verification stage, a merge stage, plus a
common-to-dispatched-agents file if the sibling shape warrants it) — several files, each needing
content decided. B plans on the order of six to eight (`SKILL.md`, `METHODOLOGY.md`, a
decomposition stage, a node/roll-up stage, a state/resume stage, a config template, plus README
and install). Neither is a single file; neither is executable without further planning; so
neither falls below the floor.
