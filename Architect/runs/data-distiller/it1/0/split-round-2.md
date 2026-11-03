# Proposed division — round 2

Round 1 (`split-round-1.md`) drew the line between **the frame** (SKILL/METHODOLOGY/config/README)
and **all of `stages/`**, with a one-way contract in which the frame half fixed the vocabulary and
the stages half consumed it. Three cold reviewers returned 2 blockers and 9 majors against it. The
decisive one, verified independently against Architect's own role files: **there is no channel that
can carry a one-way contract.** `Architect/stages/node.md:50-53` spawns both child nodes together
with the same incoming `plan` and merges the results with `Union`; `Architect/stages/leaf.md:19-20`
gives a leaf only `(task, plan, granularity)`. The halves are planned **concurrently, by cold agents
that never see each other's output**, and `Architect/stages/combiner.md` (per reviewer C, `:57-64`)
*preserves* conflicts rather than resolving them. A seam of the form "A fixes it, B consumes it" is
therefore not a seam; it is a guaranteed collision.

This round replaces it with a **non-directional** seam: every object that crosses the cut is fixed
**here, by the divider**, and travels down inside **both** sub-task texts verbatim. Neither half
produces vocabulary for the other; both receive the same vocabulary as a constraint. The line
itself also moves, so that the control-flow rules (resume, concurrency, the blindness barrier) sit
wholly on one side.

Round-1 findings and their disposition are recorded at the end of this file.

---

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

**The cut:** the **driver plane** (the files that define what a run *is*, how it is driven, and
what it owes the human) versus the **worker plane** (the files handed verbatim to dispatched cold
agents that each do one bounded pass and return).

---

# SUB-TASK ONE — the driver plane

*(The text of this sub-task is everything between this heading and the next `# SUB-TASK` heading.
It is self-contained: the shared interface is restated inside it verbatim, because the agent
planning this half will never see the other half's output.)*

Plan the implementation of the **driver plane** of the Data-Distiller skill: the files read by the
agent that *drives* a run, plus the reference and packaging files. These files are accountable for
**the run terminating correctly, staying within its concurrency ceiling, being resumable, and
handing the human a result** — not for the trustworthiness of any individual finding.

**Files this half plans. Each plan step is one file created, with the content that goes in it
specified.**

1. **`SKILL.md`** — the router. YAML frontmatter (`name: data-distiller`, and a `description`
   written to trigger when a corpus too large for one pass must be distilled into verifiable
   facts). Then: the inputs (the corpus + the Layer-2 per-corpus config, and what to do when the
   config is absent); a **cold-start guard** section (both siblings' precedent:
   `Dragonfly/SKILL.md:22`); the **run loop** — the procedure the driving agent executes, in the
   register of `Guarded_change/SKILL.md:25-52` and `Dragonfly/SKILL.md:29-70`: validate the config
   and its paths, create the run directory, dispatch decomposition, then per item dispatch
   analysts → verify → merge, then roll up, then terminate; the **stage/role index table** listing
   every file under `stages/` (the set is fixed in the shared interface below) with a one-line
   purpose and its path; the **stop-for-human** conditions; the self-check/dogfooding note.
2. **`METHODOLOGY.md`** — the reference spec, in the section shape both siblings share: *Why this
   exists*; *The method* (in prose); *Stage/role index*; *The two layers* (corpus-agnostic method
   vs. the Layer-2 per-corpus config); *The config contract (Layer 2)* — the annotated key
   skeleton, inline, as at `Guarded_change/METHODOLOGY.md:103-152` and
   `Dragonfly/METHODOLOGY.md:106-131*`; *What a run produces* — the on-disk artifact layout;
   *Trigger*; *Human-in-the-loop*.
3. **`stages/node.md`** — the coordinating/roll-up role, and the only file in this half that is a
   prompt. It carries: the recursion (how a node decides between spawning child nodes and
   dispatching workers); **the concurrency ceiling, both its semantics and its enforcement point**;
   **the restart/resume decision procedure in full** — how a restarted run reads on-disk state and
   decides what to redo and what to trust; and **the blind-roll-up barrier**: the node reads only
   the status record, at the one path it is handed, and is never handed a findings path. It
   includes `stages/common.md` verbatim (see the shared interface) and does not restate its rules.
4. **A worked per-corpus config instance**, a top-level file in the skill directory, named
   `data-distiller.<corpus-slug>.md` — the house form is a concrete instance for one real corpus,
   as at `/home/zero/Desktop/claude-code-skills/Guarded_change/guarded-change.companion.md` and
   `/home/zero/Desktop/claude-code-skills/Dragonfly/dragonfly.companion.md`, pointing at
   `METHODOLOGY.md` for the contract. The *template* is the METHODOLOGY section, not this file.
5. **`README.md`** — human-facing orientation, as both siblings carry.
6. **The install step** — the skill is installed by being present at
   `~/.claude/skills/data-distiller/`, and the live copy must equal the source copy.

**This half owns, in full and exclusively:** the run's control flow end to end (both the invoking
agent's and a node's); the on-disk run-state layout and the restart/resume decision logic; the
concurrency ceiling's semantics *and* its enforcement; the blind-roll-up barrier — both the
on-disk arrangement that makes it structural and the node procedure that observes it; the config
contract and the worked instance; stop-for-human and human-in-the-loop; the trigger/description;
packaging and install. **This half writes procedure and is expected to** — the "no restatement"
rule from round 1 is withdrawn; where a rule is stated in more than one of this half's files, name
which copy is operative, as `Guarded_change/METHODOLOGY.md:143` does.

**This half does NOT write** `stages/common.md`, `stages/decompose.md`, `stages/analyst.md`,
`stages/verify.md`, or `stages/merge.md`, and does not specify what a finding is, how an item is
sized, how a strategy is chosen, how a citation is re-checked, or how agreement is ranked. It may
name those files and their one-line purposes (fixed below) and rely on the rules the shared
interface guarantees they contain.

**Source material this half is checked against:** all of
`/home/zero/Desktop/claude-code-skills/Guarded_change/` and all of
`/home/zero/Desktop/claude-code-skills/Dragonfly/`, **including their `stages/` directories** — the
sources are not partitioned along this cut. `/home/zero/Desktop/claude-code-skills/Data-Distiller/`
is OFF LIMITS: do not read, list or grep it.

## SHARED INTERFACE — binding on this half, stated identically in the other half

Every object below is fixed by the divider, not produced by either half. **Neither half may rename,
re-scope or silently extend one.** If this half concludes an object is wrong, it plans against it
anyway and states the objection plainly in its plan output as a note — this is a flag for the
plan's reviewers, **not** a message to the other half, which will never see it.

**I1 — the `stages/` file set is closed:** `stages/common.md`, `stages/decompose.md`,
`stages/analyst.md`, `stages/verify.md`, `stages/merge.md` (worker plane), and `stages/node.md`
(driver plane). No other file exists under `stages/`.

**I2 — `stages/common.md` is included verbatim by every dispatched agent** and contains exactly
these rules, so no role file restates them: cold independence (no shared context with the
dispatcher or with siblings); read-only over the corpus; the `off_limits` config value is
enforced; the output-path-and-return contract (write to the path you were handed, return that
path plus a short summary); cite-or-it-doesn't-count; facts, not interpretation; and halt-and-say-so
when the inputs are unusable.

**I3 — the run directory layout.** `<run>/` is the run root.
`<run>/config.snapshot.md` (the resolved config as used);
`<run>/manifest.json` (the item manifest);
`<run>/items/<item_id>/analyst-<k>.md` (analyst *k*'s findings for that item);
`<run>/items/<item_id>/verified.md`; `<run>/items/<item_id>/merged.md`;
`<run>/items/<item_id>/status.json`;
`<run>/rollup/<node_id>/merged.md`; `<run>/rollup/<node_id>/status.json`;
`<run>/FINDINGS.md` (the run's terminal deliverable).
**A driver-plane agent is handed `manifest.json` and `status.json` paths only, never a
`analyst-*.md`, `verified.md`, `merged.md` or `FINDINGS.md` path** — this is what makes the
blindness structural rather than an instruction.

**I4 — the item manifest entry** has at minimum: `item_id`, `locator` (how a worker reaches the
item in the corpus), `size` (measured), `fits` (boolean), `strategy` (present when `fits` is false;
one of the names in I6).

**I5 — the status record** (`status.json`) has at minimum: `unit_id`, `state` (`complete` |
`failed` | `partial`), `counts` (findings produced / findings surviving verification / findings in
the merged output), `output_path`, `error` (one short line). **No field of the status record may
carry the text of a finding, a claim, or a citation.**

**I6 — the over-size strategy names are** `split` (divide the item into sub-items and recurse),
`window` (one worker analyzes sequential windows of the item), `sample` (analyze a stated subset
and record the omission). Which one applies to a given item is the worker plane's rule; that the
allowed set is a config key is the driver plane's.

**I7 — the finding record** has at minimum: `claim`, `citation` (a corpus locator a verifier can
re-open), `analyst_id`, `verified` (set by verify), `agreement_count` (set by merge). The worker
plane may add fields; the driver plane may not read this record at all.

**I8 — the Layer-2 config key set is** `corpus_root`, `item_definition`, `off_limits`,
`concurrency_ceiling`, `analysts_per_item` (N), `oversize_strategies`. The driver plane documents
and validates all of them. Worker-plane files read only `item_definition` and `off_limits`.

**I9 — the terminal deliverable.** `<run>/FINDINGS.md` is written by a dispatched **merge** agent
running `stages/merge.md` at the root of the roll-up. The driver plane dispatches it, names its
path, and hands that path to the human **without reading it**. Neither half may reassign this
producer.

**I10 — corpus-agnosticism.** No corpus-specific content appears in any file except the worked
config instance. This binds both halves.

---

# SUB-TASK TWO — the worker plane

*(The text of this sub-task is everything between this heading and the next `#` heading. It is
self-contained: the shared interface is restated inside it verbatim, because the agent planning
this half will never see the other half's output.)*

Plan the implementation of the **worker plane** of the Data-Distiller skill: the prompt files
handed **verbatim** to dispatched cold agents, each of which does one bounded pass — over the
corpus, or over artifacts a previous pass produced — and returns. The reader of each file is an
agent with no context but that file. These files are accountable for **every returned artifact
being trustworthy**: cited, verified, uninterpreted — not for the run terminating or resuming.

**Files this half plans. Each plan step is one file created, with the content that goes in it
specified.**

1. **`stages/common.md`** — included verbatim by every dispatched agent. Its required rule set is
   fixed in the shared interface below; this half writes the text.
2. **`stages/decompose.md`** — decompose the corpus into analyzable items per the config's
   `item_definition`; measure each item's size; decide whether it fits one context window; and
   when it does not, choose a strategy from the fixed name set and record why. Emits the item
   manifest.
3. **`stages/analyst.md`** — one of N independent cold analysts over a single item. Read-only over
   the corpus; a re-openable source citation for every finding; facts, not interpretation. Must
   state what makes the N analysts genuinely independent rather than nominally so, and what an
   analyst does when its item's strategy is `window` or `sample`.
4. **`stages/verify.md`** — a cold pass that re-opens **every** citation on an item's analyst
   findings and drops the unverifiable, recording what was dropped and why. Must state what "the
   citation checks out" means concretely and what happens when nothing survives.
5. **`stages/merge.md`** — ranks surviving findings by how many independent analysts agreed, and
   runs at **two** levels: **per item**, across the N analysts of that item, and **at a roll-up
   node**, across the merged outputs of that node's children. Must state what agreement means when
   two analysts word the same claim differently, what ranking means once items are rolled up, and
   the shape of `<run>/FINDINGS.md`, which this file's root-level invocation produces.

**Role files are additions only and never restate a rule from `stages/common.md`.** If a role file
needs to modify a common rule, that rule was never common and belongs in the roles.

**This half owns, in full and exclusively:** what each dispatched cold worker is told; the
evidentiary discipline (independence, read-only, cite-or-it-doesn't-count, facts-not-interpretation)
and where each rule sits between `common.md` and a role file; the sizing and strategy-selection
criteria; verification's re-check-and-drop rule; agreement ranking at both levels; and the content
and shape of the run's terminal findings document.

**This half does NOT write** `SKILL.md`, `METHODOLOGY.md`, `README.md`, the config instance,
`stages/node.md`, the install step, the run's control flow, the concurrency ceiling, or the
restart/resume logic — and must not specify how workers are dispatched, in what order, or at what
fan-out. It writes to and reads from the fixed paths below and assumes a driver exists.

**Source material this half is checked against:** all of
`/home/zero/Desktop/claude-code-skills/Guarded_change/` and all of
`/home/zero/Desktop/claude-code-skills/Dragonfly/`, **including their `SKILL.md` and
`METHODOLOGY.md`** — the sources are not partitioned along this cut; note especially
`Guarded_change/stages/charter.md` and `Dragonfly/stages/charter.md` as the house precedent for a
cold-agent prompt and for finding discipline.
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS: do not read, list or grep it.

## SHARED INTERFACE — binding on this half, stated identically in the other half

Every object below is fixed by the divider, not produced by either half. **Neither half may rename,
re-scope or silently extend one.** If this half concludes an object is wrong, it plans against it
anyway and states the objection plainly in its plan output as a note — this is a flag for the
plan's reviewers, **not** a message to the other half, which will never see it.

**I1 — the `stages/` file set is closed:** `stages/common.md`, `stages/decompose.md`,
`stages/analyst.md`, `stages/verify.md`, `stages/merge.md` (worker plane), and `stages/node.md`
(driver plane). No other file exists under `stages/`.

**I2 — `stages/common.md` is included verbatim by every dispatched agent** and contains exactly
these rules, so no role file restates them: cold independence (no shared context with the
dispatcher or with siblings); read-only over the corpus; the `off_limits` config value is
enforced; the output-path-and-return contract (write to the path you were handed, return that
path plus a short summary); cite-or-it-doesn't-count; facts, not interpretation; and halt-and-say-so
when the inputs are unusable.

**I3 — the run directory layout.** `<run>/` is the run root.
`<run>/config.snapshot.md` (the resolved config as used);
`<run>/manifest.json` (the item manifest);
`<run>/items/<item_id>/analyst-<k>.md` (analyst *k*'s findings for that item);
`<run>/items/<item_id>/verified.md`; `<run>/items/<item_id>/merged.md`;
`<run>/items/<item_id>/status.json`;
`<run>/rollup/<node_id>/merged.md`; `<run>/rollup/<node_id>/status.json`;
`<run>/FINDINGS.md` (the run's terminal deliverable).
**A driver-plane agent is handed `manifest.json` and `status.json` paths only, never a
`analyst-*.md`, `verified.md`, `merged.md` or `FINDINGS.md` path** — this is what makes the
blindness structural rather than an instruction.

**I4 — the item manifest entry** has at minimum: `item_id`, `locator` (how a worker reaches the
item in the corpus), `size` (measured), `fits` (boolean), `strategy` (present when `fits` is false;
one of the names in I6).

**I5 — the status record** (`status.json`) has at minimum: `unit_id`, `state` (`complete` |
`failed` | `partial`), `counts` (findings produced / findings surviving verification / findings in
the merged output), `output_path`, `error` (one short line). **No field of the status record may
carry the text of a finding, a claim, or a citation.**

**I6 — the over-size strategy names are** `split` (divide the item into sub-items and recurse),
`window` (one worker analyzes sequential windows of the item), `sample` (analyze a stated subset
and record the omission). Which one applies to a given item is the worker plane's rule; that the
allowed set is a config key is the driver plane's.

**I7 — the finding record** has at minimum: `claim`, `citation` (a corpus locator a verifier can
re-open), `analyst_id`, `verified` (set by verify), `agreement_count` (set by merge). The worker
plane may add fields; the driver plane may not read this record at all.

**I8 — the Layer-2 config key set is** `corpus_root`, `item_definition`, `off_limits`,
`concurrency_ceiling`, `analysts_per_item` (N), `oversize_strategies`. The driver plane documents
and validates all of them. Worker-plane files read only `item_definition` and `off_limits`.

**I9 — the terminal deliverable.** `<run>/FINDINGS.md` is written by a dispatched **merge** agent
running `stages/merge.md` at the root of the roll-up. The driver plane dispatches it, names its
path, and hands that path to the human **without reading it**. Neither half may reassign this
producer.

**I10 — corpus-agnosticism.** No corpus-specific content appears in any file except the worked
config instance. This binds both halves.

---

# The seam, stated once for the record

**What changes at this boundary.** Not the file's reader alone — round 1's reader-based joint was
shown false about the siblings, whose `stages/` files are mostly the *invoking* agent's own
procedure (`Guarded_change/stages/stage-1.md:8`, `stage-5.md:7`). What changes is **what the file
is accountable for, and therefore how it fails.** Driver-plane files fail by a run that stalls,
exceeds its concurrency ceiling, cannot be resumed, or ends without handing anything over. Worker-
plane files fail by an artifact that is uncited, unverified, interpreted, or steered. Those are
disjoint failure sets, they are caught by different checks, and `stages/node.md` sits on the driver
side despite being a prompt precisely because everything it can get wrong is in the first set.

**What each half produces that the other consumes:** *nothing.* That is the point of this round.
Every cross-cutting object is fixed in the shared interface I1–I10 above, which both halves receive
verbatim as a constraint. There is no upward channel, no `CONTRACT-DELTA`, and no ordering between
the halves; they can be planned simultaneously by agents that never communicate, which is what
`Architect/stages/node.md:50-53` and `leaf.md:19-20` actually do.

**What each may assume about the other.** Each half may assume the other's files exist at the paths
in I1, that they obey I2–I10, and nothing else. Neither may assume any wording, section order, or
internal structure of the other's files.

**What neither owns:**
- `/home/zero/Desktop/claude-code-skills/Data-Distiller/` — off limits to both.
- Executing, testing, or evaluating a run of the finished skill against a real corpus.
- Any corpus-specific content outside the one worked config instance (I10).

**Floor check.** Driver plane: 5 files plus an install step. Worker plane: 5 files. The floor is
"one file created, with the content that goes in it specified"; both halves are five times that and
remain coherent whole tasks, so neither falls below it and both could divide again.

# Alternatives weighed

**(a) Round 1's cut — the frame vs. all of `stages/`.** Rejected. It orphaned the driver's own run
loop (owned by neither half, since the invoking agent is not "dispatched" and the frame was barred
from procedure), split restart/resume and the concurrency ceiling across the cut, and required a
directional contract the execution model cannot deliver.

**(b) The two-layer cut — Layer 1 (the corpus-agnostic method: SKILL, METHODOLOGY, all of
`stages/`) vs. Layer 2 (the config contract, the worked config, README, install).** This is the
seam both siblings name in a section of their own (`Guarded_change/METHODOLOGY.md:88-100`,
`Dragonfly/METHODOLOGY.md:95-102`), so it deserved the weighing it did not get in round 1.
Rejected on two grounds. It is lopsided — roughly 10 files against 4 — but more importantly the
config keys are consumed by *almost every file* in the large half, so the interface between the
halves would run through every file rather than along a boundary; the seam gets **larger**, not
smaller. And the small half is packaging, not a plane of the artifact: a packaging/content cut is
a partition, not a joint.

**(c) Cutting at the blindness barrier** — the alternative round 1 rejected. Round 1's stated
reason was wrong and is withdrawn: *"the node never reads findings"* constrains **only** the node,
so it is a one-role rule and splitting the node from the workers does not split it. This round's
cut **is** essentially that cut, corrected — the node goes with the frame rather than alone, so the
half is balanced and the barrier (both its on-disk arrangement and its procedure) sits wholly in
one half.

# Round-1 findings and their disposition

| Finding (reviewer) | Severity | Disposition in round 2 |
|---|---|---|
| No delivery channel for the one-way contract (C-F1) | blocker | Seam made non-directional; I1–I10 fixed by the divider and restated verbatim in both sub-tasks. |
| Invoking agent's run loop owned by neither half (A-F2, B-F3, C-F2) | blocker/major | Driver plane owns the run loop explicitly; `SKILL.md` item 1 names it. |
| Terminal deliverable has no producer (A-F1, B-F4, C-F5) | blocker/major | I9: `stages/merge.md` at the root writes `<run>/FINDINGS.md`; driver dispatches and never reads it. |
| `CONTRACT-DELTA` declared and denied (B-F1, A-F5) | blocker/major | Channel deleted. A half that disputes an interface object plans against it and files a note for the plan's reviewers. |
| Restart/resume and concurrency ceiling split across halves (A-F3, C-F4) | major | Both wholly in the driver plane, in `stages/node.md`. |
| "A restates no procedure" contradicts the house shape (B-F5) | major | Rule withdrawn. The driver plane writes procedure and names the operative copy of any duplicated rule. |
| Source material partitioned along the file cut (B-F2) | major | Both halves are checked against **all** of both siblings, `stages/` included. |
| The `stages/` role set assigned to a half excluded from writing procedure (B-F-A) | major | The set is fixed in I1 by the divider, not produced by either half. |
| Blind roll-up pinned to a schema plus an instruction, not a barrier (B-F-F) | major | I3 makes it structural: driver-plane agents are handed status paths only; I5 forbids finding text in the status record. |
| Item manifest missing from the contract (A-F4) | major | I4. |
| Reader-based joint factually false about the siblings (C-F3, B-F10) | major | Joint restated as accountability-and-failure-mode, not reader. |
| Two-layer alternative unweighed (B-F6, C-F8) | major/minor | Weighed and rejected above, with grounds. |
| Strategy name set unowned (B-F9) | minor | I6. |
| METHODOLOGY section list omits Human-in-the-loop / Trigger (A-F8, B-F12, C-F6) | minor | Both added to the driver plane's `METHODOLOGY.md`; cold-start guard added to `SKILL.md`. |
| Config template vs. instance described incompatibly (A-F9, B-F11) | minor | Settled to the house arrangement: annotated skeleton inside `METHODOLOGY.md`, worked instance as a separate top-level file. |
| Run-state layout was a topic, not a file (C-F7) | minor | Now a section of `METHODOLOGY.md` ("What a run produces") plus I3; the driver plane's count is files only. |
| Corpus-agnosticism unpoliced (A-F10) | nitpick | I10, binding on both halves. |
