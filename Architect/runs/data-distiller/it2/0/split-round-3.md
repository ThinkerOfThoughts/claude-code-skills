# Proposed division — round 3

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

**Cut between the method and the package.** Sub-task **A** plans everything under
`Data-Distiller-impl/stages/` — the prompt files a **dispatched agent** reads verbatim and
executes, which together *are* the method. Sub-task **B** plans everything else in the build —
`SKILL.md`, `METHODOLOGY.md`, `README.md`, the Layer-2 config template, and the install step — the
files that let the skill be **found, invoked, configured, oriented-to and installed**. The seam is
a named, one-directional interface: A's plan ends with a `## Declarations` section, and that
section is B's only input from A.

This line is the source material's own. `Guarded_change/METHODOLOGY.md:8–11` states it: the
per-stage procedure and its rules "now live in `stages/` (one file per stage, plus the shared
red-team charter `stages/charter.md`); `SKILL.md` is the router that walks the loop and points at
those files. This file is opened for orientation and config setup — not to run a stage."

**Note on what that citation does and does not support.** It establishes that `METHODOLOGY.md` is
not executed. It does **not** establish that `SKILL.md` is inert — `SKILL.md` *is* executed, by
the invoking session (`Guarded_change/SKILL.md:25–32` is imperative: "Create a change folder …
append a line to `decisions.md` … Walk the loop"). The joint is therefore **who executes the
file** (a dispatched agent vs. the invoking session), not "executed vs. not". Seam clause S8 is
built on that corrected ground, and the blindness invariant is bound onto the invoking session
there rather than assumed away.

## Sub-task A — the method: every file under `Data-Distiller-impl/stages/`

**Plan every file under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/`** — the
prompts a dispatched agent reads verbatim and acts on. A decides the method: what each agent is
told to do, in what order, under what constraints, and **how many files there are and where their
boundaries fall.** A is free to structure them as pipeline stages, as agent roles, or as a mix;
nothing in this division presumes the siblings' linear `stage-0 … stage-9` shape, which comes from
a method one session walks in order, whereas this method is a tree of concurrent agents.

In scope:

- **The core that every dispatched agent reads first** — coldness and independence, read-only over
  the corpus, cite-every-finding, facts-not-interpretation, where output goes, what a returned
  status must contain. Role files add to it and never restate it.
- **Decomposition, sizing and the over-size strategy.** How a corpus is cut into analyzable items,
  how an item is sized against a context budget, and — the case the skill exists for — the rule
  that **picks and executes** a strategy when an item does not fit in one pass. Picking and
  executing are both A's, so the hardest case has one owner end to end. If the chosen strategy is
  recursive subdivision, A owns the state that recursion needs (see S6).
- **The analyst stage.** N independent cold analysts per item; read-only; a source cited for every
  finding; facts not interpretation.
- **The verification stage.** A cold pass that re-checks every citation and drops the unverifiable.
- **The merge stage.** Rank surviving findings by how many independent analysts agreed; emit the
  item's findings artifact and the item's terse status.
- **The coordinating-node stage.** How a node drives its children, enforces the blindness rule
  (reads only a terse per-child status, never the findings), observes the concurrency ceiling at
  the point of spawn, and rolls status upward.
- **The terminal roll-up stage** and the run's corpus-level deliverable. The task forbids findings
  to a **coordinating** agent; A must decide and state whether the terminal assembly is a
  coordinating agent under that reading, and therefore whether the corpus-level result is
  synthesized from findings or is a manifest over them. **This is a method question, and the
  method is entirely A's** — but its answer crosses the seam, so it is a required Declaration
  (S3e), not a private decision.
- **Re-entry and resume semantics inside the tree.** The instruction that *consults* a completion
  marker is a prompt an agent executes, so it is A's: what a node does when re-entered over
  children that are partly complete, what an item does when 3 of 5 analysts have returned, and how
  re-dispatch is prevented from double-counting in the agreement rank. B owns only the run-level
  entry point, not this.
- **Failure and retry semantics** — an analyst returning nothing, verification dropping every
  citation for an item, an unanalyzable item — expressed as permitted status values plus a
  retry/abandon rule in the relevant file.
- **Pinning "coordinating".** Both a node above an item and the per-item merger have children.
  The task's word is "coordinating". A owns deciding how far the blindness rule reaches, and
  states the answer.

Out of scope for A: `SKILL.md`, `METHODOLOGY.md`, `README.md`, the config template file, the
install step, and the *shape* of the Layer-2 config contract. A declares the config keys it needs;
it does not author the contract, and A's files never name the config file's path or filename
convention (S7).

Source material A must be checked against:
`/home/zero/Desktop/claude-code-skills/Guarded_change/stages/` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/stages/`, as the shape of a per-stage prompt file.
**A caveat A must be given rather than discover:** `stages/charter.md` in both siblings is **not**
a core read by every dispatched agent — it is a **red-team charter shared by a subset of stages**
(`Guarded_change/stages/charter.md:1`, "shared by stages 3 and 6";
`Dragonfly/stages/charter.md:1`, "shared by stages 1, 4, 7"). It is the nearest structural
analogue for a verbatim-included shared file, but its *content* is red-team material — five lenses,
severity model, provenance — most of which does not apply to an analyst or a verifier. **No
sibling ships a core read by every dispatched agent, so A is designing that file without a worked
example and should not inherit red-team shape into it.**
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits.

## Sub-task B — the package: router, reference spec, config, install

**Plan every other file of the build**, and the step that installs the skill. B owns how the skill
is found, invoked, configured, oriented-to, installed, and checked for internal consistency.

In scope:

- **`SKILL.md`** — the router. YAML frontmatter (`name`, `description`; the description is the
  trigger text, so it carries when to use the skill and when to suggest it); the inputs (the
  corpus, the Layer-2 config, what to do when the config is missing); the run-start procedure; the
  **run-level entry point** — on invocation, locate the config, locate or create the run folder,
  and enter the method at the file A's Declarations name as the entry stage, **handing over to A's
  files rather than restating their mechanics**; the file-index table; and the stop-for-human
  conditions.
- **`METHODOLOGY.md`** — the orientation/reference spec: why the method exists and the failure
  modes it guards; the pipeline diagram; the two-layer split; the config contract; and **what a
  run produces** — written from A's Declarations (S3c/S3d), not from B's own invention.
- **`README.md`** — human-facing orientation (both siblings ship one).
- **The Layer-2 config contract and a shipped template/example config file** at the build's top
  level (the siblings' `guarded-change.companion.md` / `dragonfly.companion.md` occupy this slot):
  the contract's shape, defaults, validation rules, and the rule that no corpus specifics appear
  anywhere outside it. It must contain every key A declares; B may add keys the *router* needs.
- **Installation.** How the built skill reaches `~/.claude/skills/<name>/`. **The task fixes the
  build location but not `<name>`** — it states only the pattern. B chooses and justifies the
  installed name, and the install step must **check for and refuse to overwrite an existing
  directory at that path**: `~/.claude/skills/` already contains a `data-distiller` directory, so
  a naive copy would destroy an existing artifact as an unplanned side effect. B may verify this
  by listing `~/.claude/skills/`; B may not read
  `/home/zero/Desktop/claude-code-skills/Data-Distiller/`.
- **The composition check** (S10) — the standing self-check criteria for the assembled skill, on
  the model of `Guarded_change/SKILL.md:81–83` ("live copy == source copy (`diff`); SKILL.md ↔
  METHODOLOGY.md ↔ stage-file consistency on every rule stated in more than one place"). This cut
  deliberately states some rules in more than one place — the blindness property (S8), the
  concurrency ceiling (S9), the run-directory layout (S6) — so someone must own checking them
  against each other, and it is B, who touches the assembled directory last.

Out of scope for B: the content of any file under `stages/`; the analyst, verification, merge,
node, roll-up, decomposition, sizing, over-size, resume-inside-the-tree and failure procedures; the
blindness rule's formulation; the findings-artifact format.

Source material B must be checked against: `/home/zero/Desktop/claude-code-skills/Guarded_change/`
— `SKILL.md:1–4` (frontmatter), `SKILL.md:13–24` (inputs), `SKILL.md:25–52` (router + stage index),
`SKILL.md:54–73` (stop-for-human), `SKILL.md:75–85` (self-check); `METHODOLOGY.md:67–84` (stage
index), `:88–101` (two layers), `:103–151` (config contract), `:154–196` (what a run produces) —
and `/home/zero/Desktop/claude-code-skills/Dragonfly/` (the same files, second example).
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits.

## The seam

**S1. The partition is by path, stated as a default so it is total.** **Any path under
`Data-Distiller-impl/stages/` is A's. Any other path in, or produced by, the build is B's** —
including a third subdirectory neither half anticipated, and including the installed copy at
`~/.claude/skills/<name>/`. No file is planned by both, and no path falls to nobody.

**S2. Information flows A → B through one named carrier, and A is planned first.** **A's plan ends
with a section headed `## Declarations`**, containing the five labelled tables in S3. **That
section is B's sole input from A** — B does not read the rest of A's plan, and does not open A's
planned files, to write its own. There is one narrow return channel, and only one: S10's mismatch
report. There is no negotiation over method.

**S3. What `## Declarations` must contain.** Five tables. Each is a required output of sub-task A;
A's plan is incomplete without them.

- **(a) File index.** One row per file A plans: path, and an **index-grade line** — not a bare
  purpose, but the content-level summary B's tables need. Calibration:
  `Guarded_change/METHODOLOGY.md:73` reads *"checkable, labeled accept bar; position/concurrency
  criteria; self-check criteria"*. One row is marked as the **entry file** the router hands over
  to. B writes `SKILL.md`'s and `METHODOLOGY.md`'s index tables from this table alone.
- **(b) Config keys.** Every Layer-2 key A's files read, with a meaning and a value type. B's
  contract must contain every one; B may not drop or rename any, and may add only keys the router
  itself needs.
- **(c) Artifact inventory.** Every file the method writes into the run directory: path (relative
  to the skeleton in S6), name, and one line on contents — including the per-item findings
  artifact, the per-item status, the run log, any node-level state, and the corpus-level
  deliverable. This is what `METHODOLOGY.md`'s "what a run produces" is written from; the sibling
  section it is modelled on (`Guarded_change/METHODOLOGY.md:154–196`) is exactly such an inventory.
- **(d) Status vocabulary and completion markers.** The permitted status values, the run-level
  outcome states they aggregate into, and — per unit of work — the on-disk marker that means
  "finished, do not re-run".
- **(e) Resolved method decisions that B must state.** At minimum: whether the corpus-level result
  is a synthesis or a manifest, and how far the blindness rule reaches. B states these in
  `METHODOLOGY.md`; B does not decide them.

**S4. B may not paraphrase a mechanic it does not own.** Where B's router must refer to method
behaviour — resume, blindness, concurrency — it **points at A's file** and reproduces only what
S3's Declarations state. B never writes a step that reads a run artifact other than one S3(c)
marks as status.

**S5. Resume is split by kind, not by level.** A owns every instruction that *consults* on-disk
state, at any depth: the node's check-markers-before-spawn rule, partial-item re-entry, and
double-count prevention in the agreement rank. B owns the run-level entry point only — find or
create the run folder, hand over to the entry file — plus the human-facing account of resume in
`METHODOLOGY.md`, written from S3(d).

**S6. A minimum run-directory skeleton, rooted, which A may extend downward.** Fixed here so S2's
one-directional flow is not spoiled by B owning a layout A must write into — but stated as a
**minimum**, not a freeze, because the layout is a consequence of the method and the method is A's.

- **Rooting:** `runs/` is rooted at **the invoking session's working directory**, not inside the
  installed skill. The siblings root theirs at the skill's own directory
  (`Guarded_change/SKILL.md:27`, `Dragonfly/SKILL.md:31`), which works because the skill sits in
  the project under change; Data-Distiller is installed at `~/.claude/skills/<name>/` and runs
  against an arbitrary read-only corpus, so inheriting that would make every run mutate the
  installed skill.
- **Minimum shape:** `runs/<run-slug>/` per run; `runs/<run-slug>/items/<item-id>/` per top-level
  analyzable item; an append-only run log at the run folder's root.
- **A may add depth and add siblings** — nested sub-items beneath an over-size item, node-level
  state, a corpus-level deliverable at the run root — and **may not rename or relocate the levels
  above.** Every addition appears in S3(c), so B documents the layout A actually built.

**S7. Config reaches a dispatched agent by being handed down, not read.** Only B's router locates
the config file (the siblings' glob, `Guarded_change/SKILL.md:16–18`, is B's territory). A's files
**name keys and receive their values in the dispatch prompt**; they never name the config's path
or filename convention. This is what keeps S2 one-directional in fact and not just in claim.

**S8. The blindness invariant is A's to formulate, and binds the invoking session too.** Both the
constrained agent (the node) and the agent defining the terse status (the merge) are A's files, so
the rule is authored and enforced in one half. But the invoking session executes `SKILL.md` and is
itself the topmost coordinating agent, so containment-by-authorship is not sufficient on its own:
**A's formulation must be written to bind any driver of the method, including the invoking
session, and B's router must obey it** — B writes no step that opens a findings artifact, and per
S4 refers to A's file rather than restating the rule. `METHODOLOGY.md` says the property exists and
why; it does not restate the rule in B's words.

**S9. Concurrency: one key, one enforcement point, on opposite sides, deliberately.** B's contract
holds the ceiling key and the template gives an example value. A's node file carries the
check-before-spawn rule, because the only spawn sites are in A's files (verified: neither sibling's
`SKILL.md` contains a dispatch step; the operative reviewer-spawn rule lives in the stage files,
`Guarded_change/METHODOLOGY.md:79`). B writes no enforcement instruction; A sets no value.

**S10. B owns the composition check, and it is the one B → A channel.** After both halves are
planned, B checks that its consumed Declarations still match A's plan and that every rule stated in
more than one place agrees across the files. **If a Declaration changed after B consumed it, or is
insufficient to write a section B owns, B raises a mismatch report against the Declarations and
B's dependent sections are re-derived.** The channel carries mismatches only — B does not propose
method, and A does not answer with a change to B's documents.

**S11. What neither half owns.** The corpus, and any example corpus — the skill is corpus-agnostic
and no corpus is in scope. The build location, which the task fixes. Reading
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`, forbidden to both.

## Why this is a real joint, not a bisection

Four things genuinely change at this boundary:

- **Who executes the file.** A's files are consumed **verbatim by a dispatched agent** as
  instructions. B's `SKILL.md` is consumed **by the invoking session**; `METHODOLOGY.md` and
  `README.md` are not executed at all ("opened for orientation and config setup — not to run a
  stage", `Guarded_change/METHODOLOGY.md:11`).
- **The failure mode of getting it wrong.** A bad file under `stages/` makes every dispatched agent
  do the wrong thing on every run. A bad `SKILL.md` frontmatter means the skill never triggers and
  is never run at all — the frontmatter *is* the trigger text (`Guarded_change/SKILL.md:3`,
  `Dragonfly/SKILL.md:3`). Different failures, caught by different checks.
- **What must be corpus-agnostic vs. what names the corpus.** B owns the one place corpus
  specifics may live. A's files must contain none, and by S7 cannot even locate the file that does.
- **The authorship discipline.** A's files are a multi-role prompt set — a core included verbatim
  plus additions-only role files (the discipline evidenced by `stages/charter.md` being shared
  across stages with per-stage additions, `Guarded_change/SKILL.md:49–50`). B's documents carry no
  such constraint.

**The alternative considered and rejected.** The other real joint available is *per-item leaf
pipeline* (decompose/size/analyst/verify/merge) vs. *tree + package* (node, roll-up, state, resume,
`SKILL.md`, `METHODOLOGY.md`, config, install). It is more balanced in volume. It is rejected
because it would put **the blindness invariant on the seam**: the node that must not read findings
would be on one side and the merge that defines the terse status it reads on the other, so the
task's central property would be defined by one half and enforced by the other, with each able to
satisfy its own brief while the property fails. S8's containment is the reason to prefer this cut,
and it is worth the imbalance.

**On the imbalance itself.** A is the larger half — by the nearest measurable analogue,
`Guarded_change/stages/` is roughly twice the volume of that skill's top-level documents — and A
holds the open method questions. That is not a defect of the cut: the four questions do not require
balance, both halves clear the floor, and if A is divided again the audience line still holds
beneath it.

## Why both halves are above the floor

The floor is one file with its content specified. A must decide **how many files there are, where
their boundaries fall, and what goes in each** — at minimum a shared core, decomposition/sizing,
analyst, verification, merge, coordinating node, and terminal roll-up — plus the over-size
strategy, the reach of "coordinating", and re-entry semantics. B must decide the content and
section structure of `SKILL.md`, `METHODOLOGY.md`, a config contract plus template, `README.md`,
an install step with a collision check, and the composition-check criteria. Neither half is a
single file whose content is already specified; neither is executable without further planning.
Neither falls below the floor.
