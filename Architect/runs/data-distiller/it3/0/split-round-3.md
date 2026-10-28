# Proposed division — round 3

`Divisible(task, granularity)`, iteration 3, node `0`. Standalone: this file is the whole proposal.

**What changed from round 2.** All three round-2 reviewers again endorsed the cut; none objected to
going forward. One `blocker` and fourteen distinct `major`s stood, **every one of them a defect in
the seam text**, which is the divider's own output and not something a blind planner could act on.
The joint is unchanged. §3 is re-derived. Disposition table in §7.

The largest change: **the `oversize` state is gone.** Three of round 2's majors and the mutation
problem underneath them all came from a state that let A discover at read time what B had sized
wrongly, forcing a node to change kind mid-run. The task says *"decompose and size the corpus into
items, **with a strategy for over-size items**"* — that strategy is a **decomposition-time**
mechanism, and it is now stated as one. Nothing mutates.

---

## 0. The task being divided (verbatim, as received)

> Plan the implementation of the Data-Distiller skill — a Claude Code skill (a directory of
> markdown prompt files) implementing a cold, multi-agent method for extracting source-cited
> factual findings from a corpus too large for one context window. Eight defining properties:
> decompose and size the corpus into items, with a strategy for over-size items; N independent
> cold read-only analysts per item, each citing every finding; a cold verification pass that
> drops unverifiable citations; an agreement-ranked merge; a blind roll-up in which a
> coordinating agent reads only a terse per-child status; a per-corpus Layer-2 config so the
> method stays corpus-agnostic; restart and resume from on-disk state; facts, not interpretation.
> To be built at /home/zero/Desktop/claude-code-skills/Data-Distiller-impl/.
> Check it against the sibling skills
> /home/zero/Desktop/claude-code-skills/Guarded_change/ and
> /home/zero/Desktop/claude-code-skills/Dragonfly/ for house style and structure.
> /home/zero/Desktop/claude-code-skills/Data-Distiller/ is OFF LIMITS: do not read, list, grep or
> otherwise open it, and state in your output that you did not.

**Granularity floor (verbatim):** *"A step a competent practitioner can execute without further
planning: concretely, one file created or one coherent edit to one file, with the content that
goes in it specified."*

The eight properties are **P1–P8** in the order they appear above.

---

## 1. The joint

**The cut is the finding boundary — the boundary P5 already names.**

> *"a blind roll-up in which a coordinating agent reads only a terse per-child status"*

The line is not *reads the corpus* — B's decomposer must open corpus files to find the structural
boundaries it splits on. The line is **reads for meaning, and emits or sees a finding**:

| | **Below the boundary** | **Above the boundary** |
|---|---|---|
| What the agent reads | corpus content **for meaning** | corpus **shape** (paths, sizes, delimiters), item records, one-line statuses — **never a finding** |
| What it produces | cited findings — **evidence** | an item inventory and a tree of statuses — **bookkeeping** |
| Its discipline | cold, read-only, cite every finding, facts-not-interpretation | cold, read-only over the corpus, blind to findings, idempotent, resumable |
| Its characteristic failure | a fabricated or unverifiable citation; interpretation smuggled in as fact | a coordinator that peeks at findings; work lost or silently duplicated on restart |
| Its unit of work | **one item** | **the corpus, and the tree over it** |
| Its review criterion | does every citation resolve? | is it blind, and is it idempotent? |

Disjoint inputs, disjoint outputs, disjoint failure modes, disjoint review criteria. **P5 is not a
feature sitting on one side of this line — P5 is the assertion that the line exists and is not
crossed.** The interface was specified by the owner's own task statement before any divider looked
at it; §3 does nothing but write it down concretely.

**The alternative considered and rejected.** *Method (`stages/*`) vs. envelope (`SKILL.md`,
`METHODOLOGY.md`, `README.md`, config)* has a thinner seam — the item record, the status schema and
the stage numbering would all be internal to one half. Rejected because its joint is a **packaging**
boundary, not a design one: the envelope half is derivative documentation of a method it does not
own, and nothing about the method changes at that line. Recorded because no later reviewer sees the
alternatives available at this cut.

---

## 2. The two sub-tasks

**Both sub-task texts below are delivered with §3 (the seam) prepended verbatim** — see §6.

### Sub-task A — the per-item finding pipeline

> **Plan the implementation of Data-Distiller's per-item finding pipeline: everything that happens
> to ONE item from the moment the run driver dispatches your pipeline entry agent on it to the
> moment that item's `STATUS` line is written.** This is the part of the skill in which agents read
> corpus content for meaning and produce cited findings.
>
> **How you are invoked (fixed, §3.3):** the other half's run driver dispatches **one** agent on
> **`stages/stage-2.md`** — your pipeline entry — with **one** argument: `item_dir`, the absolute
> path to the item's node directory. Everything else you need is in `item_dir/item.json`. **That
> entry agent owns all further fan-out inside the item** — spawning the N analysts, the verifier,
> and the merge. The driver dispatches nothing else per item.
>
> You own, as mechanism and as prompt text:
> - **P2** — N independent cold read-only analysts per item, each citing every finding. Choose and
>   justify N's default; specify how independence is enforced **at your entry agent's dispatch
>   point** (no shared context, no visibility of a sibling's output), how fan-out is bounded, and
>   what "read-only" concretely forbids an analyst. *(§3.7 rules 1 and 3 state the duty; the
>   enforcement mechanism is yours, and stating it is an addition, not a restatement.)*
> - **P3** — the cold verification pass that drops unverifiable citations: who runs it (a separate
>   cold agent, **never the analyst that produced the finding**), what it is given, what
>   "unverifiable" means operationally, and what happens to a dropped finding.
> - **P4** — the agreement-ranked merge: how findings from N analysts are matched, what counts as
>   agreement, and how the rank is computed and recorded.
> - **P8** — facts, not interpretation: the concrete, checkable discipline that keeps analyst,
>   verifier and merge output factual, written into the role prompts as an **enforceable rule
>   rather than an exhortation**.
> - **The finding record and the citation format** — the internal formats of every file you write
>   under a leaf node directory except `STATUS`, whose schema §3.4 fixes.
> - **Your acceptance bound.** Declare a config key `analysis.max_item_bytes` — the largest
>   `size_bytes` your pipeline accepts. If your entry agent is handed a larger item it writes
>   `state=failed` with the reason in `decisions.md` rather than analysing it badly. **You do not
>   own the over-size strategy** — splitting over-size items is decomposition-time work and belongs
>   to the other half (§3.5).
> - **Resume *within* an item** (your share of P7): your pipeline, re-dispatched on a node directory
>   that already holds some of your outputs, must not redo completed work; it uses the presence rule
>   (§3.2). **Re-dispatch must therefore be safe and idempotent.** *Resume across nodes is the other
>   half's.*
> - **Your own Layer-2 config keys**, in the namespaces §3.6 assigns you.
> - **Writing the leaf `STATUS` line** (§3.4) as the last act of your pipeline.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor: one file created
> or one coherent edit to one file, with the content that goes in it specified. Your role-prompt
> files live under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/` at stage
> numbers **2–4**, bound at phase level by §3.1: **2 = pipeline entry + analysts, 3 = verification,
> 4 = merge.**
>
> **Your plan must declare** (§3.1) — these five things are consumed by the other half's build-time
> rules, so omitting any of them leaves a step in the merged plan unexecutable:
> 1. for every file it creates: **filename**, **stage number / phase**, **one-line purpose**;
> 2. every config key it defines: **name, meaning, type, default (or "required")**;
> 3. **the filename of your merged-findings file** — the one file per item that carries the final
>    ranked findings (the other half's `index.md` and `findings.md` steps are rules over this name);
> 4. your **stop-for-human conditions**, as a list of one-line conditions;
> 5. nothing about the other half.
>
> **Source material you must check yourself against:**
> - `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
>   `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. Closest
>   precedents: `Guarded_change/stages/charter.md`, `Guarded_change/stages/stage-3.md`,
>   `Dragonfly/stages/charter.md`, `Dragonfly/stages/stage-7.md` — cold-reviewer prompts with
>   citation discipline and an evidence bar. Read them for form, not for content to copy.
> - The seam, §3 of this document, prepended to this sub-task and also readable at
>   `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it3/0/split-round-3.md`.
>   You inherit it and may not renegotiate it; §3.9 says what to do if you think it is wrong.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
> output that you did not.
>
> **You do not own** and must not plan: decomposing the corpus into items, the over-size strategy,
> the run driver, the roll-up, resume across nodes, the Layer-2 config file, `stages/common.md`,
> `SKILL.md`, `METHODOLOGY.md`, `README.md`, or the assembled corpus-level `findings.md`.

### Sub-task B — the corpus envelope

> **Plan the implementation of Data-Distiller's corpus envelope: everything that turns a corpus
> into items, drives the per-item pipeline over them, rolls their statuses up blind, and makes the
> whole thing an invocable, configurable, restartable Claude Code skill.** This is the part of the
> skill in which no agent ever reads a **finding**. Your decomposer *does* open corpus files — to
> find structural boundaries and measure size — and is a cold, read-only agent while doing so; what
> it must never do is read for meaning or emit a finding.
>
> You own, as mechanism and as prompt text:
> - **P1** — decomposing and sizing the corpus into items, **and the strategy for over-size items,
>   which runs entirely at decomposition time** (§3.5). You produce `index.md` and the item records
>   of §3.3, and you **validate every `locator` before writing it**. You define behaviour for the
>   degenerate corpora: an empty corpus, and a corpus that is a single below-threshold item.
> - **The run driver** — the role that walks `index.md`, decides which nodes still need work
>   (§3.5), dispatches the other half's pipeline entry agent on each leaf node exactly as §3.3
>   fixes, bounds concurrency, and maintains each node's `RUN` file. The driver may read
>   `index.md`, any `item.json`, any `STATUS`, any `RUN`, `decisions.md`, and the config — **never a
>   finding**.
> - **P5** — the blind roll-up: the coordinating role prompt, which is given **the `STATUS` lines
>   of its own children and nothing else** (§3.4), and writes its own node's `STATUS`. The tree may
>   be any depth (§3.2).
> - **P6** — the per-corpus Layer-2 config: the config **file** (one worked example for a named
>   example corpus) and the config **contract** section in `METHODOLOGY.md`. Your own keys live in
>   the namespaces §3.6 assigns you.
> - **P7** — restart and resume **across** nodes: how a restarted run learns what is done, using
>   the presence-and-state rule of §3.5 and the `RUN` file, and what it re-runs. *(Resume within
>   one item is the other half's, and re-dispatch of a leaf is safe.)*
> - **The assembled corpus-level output** — `<run.dir>/findings.md` (§3.8): a **deterministic
>   file-concatenation step, not a dispatched agent**.
> - **The entry surface** — `SKILL.md` (frontmatter + router table + `Stop-for-human`),
>   `METHODOLOGY.md`, `README.md`, following the sibling skills' structure.
> - **`stages/common.md`** — the one file every dispatched agent reads before its role file. §3.7
>   fixes the rules it must carry; you write them.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor: one file created
> or one coherent edit to one file, with the content that goes in it specified. Your role-prompt
> files take stage numbers **0–1 and 5–9**, bound at phase level by §3.1: **0 = decomposition and
> sizing, 1 = the run driver, 5 = the blind roll-up**; 6–9 are yours to use or leave unused.
>
> **Your plan must declare** the same five things §2-A lists (items 1, 2 and 4 apply to you; item 3
> is A's; you declare nothing about A).
>
> **Steps written as rules over the merged plan.** Where a step's content depends on the **full**
> file, key, filename or stop-condition inventory, write it as a rule, not as a guessed list — a
> practitioner holding the merged plan can execute such a rule. **Do not guess the other half's
> filenames, stage numbers, purposes, config keys, merged-findings filename or stop conditions.**
> This applies to, at least: the `SKILL.md` router table; the `SKILL.md` `Stop-for-human` section
> (*"one row per stop condition declared by either half's plan"*); the `METHODOLOGY.md` stage
> index; the `METHODOLOGY.md` **loop diagram** and **"what a run produces"** sections; the
> `METHODOLOGY.md` config-key contract; the worked example config; `index.md`'s per-node findings
> pointer (*"…naming that node's merged-findings file as declared in the merged plan"*); and
> `findings.md`'s assembly rule (§3.8).
>
> **Source material you must check yourself against:**
> - `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
>   `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. Closest
>   precedents: `Dragonfly/SKILL.md` and `Guarded_change/SKILL.md` (frontmatter + router table +
>   `Stop-for-human`), `Dragonfly/METHODOLOGY.md` (why-it-exists, the loop diagram, the stage index,
>   the two layers, the config contract, what a run produces, human-in-the-loop),
>   `Dragonfly/dragonfly.companion.md` and `Guarded_change/guarded-change.companion.md` (a worked
>   Layer-2 config), and the sibling `README.md` files.
> - The seam, §3 of this document, prepended to this sub-task and also readable at
>   `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it3/0/split-round-3.md`.
>   You inherit it and may not renegotiate it; §3.9 says what to do if you think it is wrong.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
> output that you did not.
>
> **You do not own** and must not plan: what an analyst does with an item's content, the citation
> format, the verification pass, the merge, fan-out within an item, resume within an item, or any
> file under a leaf node directory other than `item.json`, `RUN` and (as a reader) `STATUS`.

---

## 3. The seam

**Both halves are planned concurrently and blind to each other. There is no channel between them
and neither may assume one.** Everything here is fixed, stated identically to both halves, and
inherited by everything beneath the cut. **Neither half may change it**; §3.9 says what to do
instead.

### 3.1 Build root, layout, ownership, stage numbering, and the declaration obligation

Everything is built under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`. Neither
half creates a file outside it. **This layout is BINDING at phase level** — each half may add
letter-suffixed files within its own phases (`stage-0a.md`, as the siblings do) but may not move a
phase to a different number, and may not add a top-level file:

```
Data-Distiller-impl/
  SKILL.md                       B    frontmatter + router table + Stop-for-human
  METHODOLOGY.md                 B    orientation, the loop, the two layers, stage index,
                                      config contract, what a run produces, human-in-the-loop
  README.md                      B
  data-distiller.<example>.md    B    one worked Layer-2 config for a named example corpus
  stages/
    common.md                    B    read verbatim by EVERY dispatched agent, before its role file
    stage-0.md                   B    decomposition and sizing (incl. the over-size strategy)
    stage-1.md                   B    the run driver
    stage-2.md                   A    THE PIPELINE ENTRY: dispatched once per item by the driver;
                                      owns all fan-out inside the item, incl. the N analysts
    stage-3.md                   A    verification
    stage-4.md                   A    merge
    stage-5.md                   B    the blind roll-up
    stage-6.md … stage-9.md      B    optional; B's to use or leave unused
```

**Stage numbering is fixed here because neither half can converge on it alone** — A's phases sit
*between* B's decomposition and B's roll-up, so the numbering is inherently joint, and the siblings
key their router, stage index and gate log off stage numbers (`Guarded_change/SKILL.md:28`: *"Step
numbers below are the canonical stage numbers used everywhere"*; the same convention holds in
`Dragonfly/SKILL.md`).

**The `SKILL.md` frontmatter `name` is `data-distiller-impl`.** B states in `README.md` that this
deliberately avoids colliding with the separately installed `data-distiller` skill.

**The declaration obligation (both halves).** Each half's plan declares: (1) for every file it
creates — filename, stage number/phase, one-line purpose; (2) for every config key it defines —
name, meaning, type, default or "required"; (3) *A only* — the filename of its merged-findings
file; (4) its stop-for-human conditions as one-line entries. **B's build-time rules consume exactly
these.** Neither half declares anything about the other.

**Additions-only discipline.** `stages/common.md` holds what *every* dispatched agent needs; a role
file **adds** and never restates or modifies a common rule. Specifying the *enforcement mechanism*
for a common duty inside a role file is an addition, not a restatement (§3.7).

### 3.2 The run-directory skeleton, the presence rule, and who may read what

A run writes under a directory given by the Layer-2 config key `run.dir` (B's to document and
default; both halves may reference the name). The siblings document run artifacts as living inside
the skill directory (`Guarded_change/SKILL.md:27` — `changes/<slug>/`; `Dragonfly/SKILL.md:31` and
`Dragonfly/METHODOLOGY.md:143` — `hunts/<slug>/`); B's default follows that convention.

**The skeleton is EXHAUSTIVE. Neither half may add a file or directory to it.**

```
<run.dir>/
  index.md                       B    the node inventory produced by decomposition
  decisions.md                   B    append-only run log (see the append exemption below)
  findings.md                    B    the assembled corpus-level output (§3.8)
  nodes/<node_id>/
    item.json                    B    present IFF this node is a LEAF (an item); §3.3. IMMUTABLE.
    RUN                          B    the driver's per-node bookkeeping; MUTABLE (see below)
    STATUS                       leaf: A   group: B    one line, §3.4. WRITE-ONCE.
    <A's per-item outputs>       A    leaf only: per-analyst, per-analyst-verified, merged findings
```

**The tree is recursive and any depth.** `<node_id>` is dot-separated (`0`, `0.1`, `0.1.2`) and
directories nest to match. **A node is a LEAF — an item — if and only if it has `item.json`;
otherwise it is a GROUP** whose children are the nodes one level below it. One skeleton expresses a
flat corpus and a nested one identically, which is what P5's *"per-**child** status"* and *"too
large for one context window"* jointly require: a single coordinator reading one line per item does
not fit a corpus this method exists for.

`node_id` and `item_id` match `[A-Za-z0-9._-]+`.

**Nothing ever changes kind.** A node is created as a leaf or as a group by decomposition and stays
that way. `item.json` is never deleted; `STATUS` is never overwritten. This is what makes the
presence rule mean something, and round 2's `oversize` state — the only thing that required a node
to change kind mid-run — is gone (§3.5).

**The presence rule.** *Every file above is written complete or not at all* — write to a `.tmp`
sibling, then rename — so **the existence of a file means the step that produces it finished.**
**Two exemptions, and only two:**
- **`decisions.md`** is append-only: each writer appends one complete line at a time (an atomic
  `O_APPEND` write), and its existence means "the run started", not "the run finished".
- **`RUN`** is the one mutable file: it holds a single integer, the number of times the driver has
  dispatched this node. The driver increments it **before** each dispatch. Its presence means "this
  node has been attempted", which is what distinguishes *never started* from *started by a run that
  died*.

**Who may read what — this is the blindness mechanism, stated once:**

| Role | May read | Writes |
|---|---|---|
| **B's decomposer** (stage 0) | the corpus (for shape), the config | `index.md`, `item.json`, appends to `decisions.md` |
| **B's run driver** (stage 1) | `index.md`, any `item.json`, any `STATUS`, any `RUN`, `decisions.md`, the config. **Never a finding.** | `RUN`, appends to `decisions.md` |
| **B's roll-up coordinator** (stage 5) | **the `STATUS` lines of its own children, and nothing else.** Not `item.json`, not `RUN`, not `decisions.md`, not a finding, not the corpus. | its own node's `STATUS` |
| **A's roles** (stages 2–4) | their own item's corpus content, their own `item.json`, their own item's earlier outputs, the config | their own item's outputs, the leaf `STATUS`, appends to `decisions.md` |
| **The human** | everything | — |

### 3.3 The item record, and the invocation contract

`nodes/<node_id>/item.json`, produced by B's decomposition, consumed by A's pipeline. **Exactly
these fields; A may not require others, B may not omit any.** Value domains are fixed here, not
derived from either half's config namespace:

| Field | Meaning and fixed domain |
|---|---|
| `node_id` | this node's dotted id; also its directory name |
| `item_id` | stable item identifier, `[A-Za-z0-9._-]+` |
| `item_dir` | **absolute** path to this node's directory — A never has to resolve `run.dir` |
| `locator` | `{"path": <absolute path>, "lines": [<first>, <last>]}` — **inclusive, 1-based line numbers**, or `"lines": null` for the whole file. **Lines are the unit, fixed here.** |
| `size_bytes` | the item's size in **bytes**. The seam's unit, whatever unit `sizing.*` uses internally. |
| `tier` | **opaque to A.** A must not branch on it. It exists for B's sizing and for the human. |
| `parent_node_id` | the node this is a child of; `null` at the root |
| `config_path` | absolute path to the Layer-2 config in force for this run |

**B validates every `locator` at decomposition time**: a locator that does not resolve to a readable
path and range is **not written as an item**; the failure is appended to `decisions.md`. Both
siblings make this explicit — `Guarded_change/METHODOLOGY.md:139` *"Paths are validated, not
assumed"*; `Dragonfly/SKILL.md:19` *"Validate config paths at hunt start"*.

**The invocation contract — target, arity and argument, all fixed:**

> **B's run driver dispatches exactly ONE agent per leaf node, on the role file
> `stages/stage-2.md`, with exactly ONE argument: `item_dir` (absolute).** That agent reads
> `item_dir/item.json` for everything else, including `config_path`. **All fan-out inside the item
> — the N analysts, the verifier, the merge — belongs to that agent, not to the driver.** The
> driver dispatches nothing else for that item and waits for the agent to return.

Re-dispatch of the same leaf is **safe**: A's within-item resume (§2-A) makes the pipeline
idempotent, so a driver that cannot tell "in flight in a dead run" from "never finished" may simply
re-dispatch.

### 3.4 The `STATUS` line — the ONLY thing that crosses the boundary upward

`nodes/<node_id>/STATUS` is **one line**, whitespace-separated, exactly five fields, **write-once**:

```
<node_id> <state> <n_findings> <n_dropped> <max_agreement>
```

| Field | Domain |
|---|---|
| `state` | leaf: `done` \| `partial` \| `failed` \| `escalated`.  group: `done` \| `partial` \| `escalated`. |
| `n_findings` | non-negative integer: findings surviving verification and merge in this subtree |
| `n_dropped` | non-negative integer: findings dropped by the verification pass (P3) |
| `max_agreement` | non-negative integer count of analysts: the highest agreement count any surviving finding in this subtree reached. **`0` when there are no surviving findings.** |

**A node with no `STATUS` file has not finished. Absence is the only "not yet" marker.**

**What the leaf states mean** (A writes these):
- `done` — the pipeline completed: analysts, verification and merge all ran and a merged-findings
  file exists. **Terminal.**
- `partial` — the pipeline completed some phases and could not complete the rest; the three integers
  describe what does exist. **Re-runnable.**
- `failed` — the pipeline could not produce a merged-findings file at all (unreadable item, an item
  larger than `analysis.max_item_bytes`, a tool failure). The three integers are `0 0 0`.
  **Re-runnable, up to the attempt cap.**
- `escalated` — **terminal, do not re-run**, and the human is told. Written when the attempt cap in
  §3.5 is reached.

**What the group states mean** (B's roll-up writes these, from children's lines only):
- `done` — every child is `done`.
- `escalated` — at least one child is `escalated` and no child is re-runnable. **Terminal.**
- `partial` — anything else.
`n_findings` and `n_dropped` sum over children; `max_agreement` is the max over children (`0` if the
group has no findings).

**There is deliberately no path field.** Round 1 carried `findings_path` and all three reviewers
filed it: putting the locator of the findings into the blind coordinator's only input turns P5 from
a structure into an exhortation. The human-facing pointer lives in `index.md` and `findings.md`
(§3.8); the coordinator never holds an address for a finding.

**A may not add fields.** If A needs one, §3.9 says what to do.

### 3.5 The control loop — the over-size strategy, resume, and the attempt cap

**The over-size strategy is decomposition-time work and lives entirely in B (stage 0).** B's
decomposer, given a candidate item larger than `sizing.max_item_bytes`, splits it along the
structural boundaries the Layer-2 config names into child nodes, recursively, until every leaf is
within the bound or `sizing.max_resplits` is exhausted. **An item that cannot be brought within the
bound is not emitted as a leaf**: it is recorded in `index.md` and `decisions.md` and escalated to
the human at decomposition time.

**The bound must be one A's pipeline can actually take.** A declares `analysis.max_item_bytes` and B
declares `sizing.max_item_bytes`; **the seam's invariant is `sizing.max_item_bytes ≤
analysis.max_item_bytes`**, and B states that invariant in `METHODOLOGY.md`'s config contract as a
rule over the merged plan's declared keys (§3.6). At run time, A's entry agent handed a larger item
writes `state=failed` rather than analysing it badly. No state crosses the boundary to trigger a
re-split, and no node ever changes kind.

**Resume and the driver's per-pass decision** read file existence, `RUN`'s integer, and — for
`STATUS` only — the `state` field. (`state` is already a field above-boundary roles may read, so
this costs no blindness.)

| Observed at a node | What B's run driver does |
|---|---|
| no `STATUS` | leaf → increment `RUN` and dispatch A's entry agent (§3.3). group → run the roll-up once every child has a `STATUS`. |
| `state=done` | **terminal.** Do not re-run. |
| `state=partial` or `state=failed` | if `RUN < run.max_attempts` → increment `RUN` and re-dispatch; A's within-item resume means completed sub-steps are not redone. **If `RUN ≥ run.max_attempts` → write nothing to `STATUS`** (it is write-once and already exists); instead the driver records the exhaustion in `decisions.md` and **treats the node as `escalated`** for roll-up and termination purposes, and stops for the human. |
| `state=escalated` | **terminal.** Do not re-run. |

`run.max_attempts` is B's key. **Every path terminates**: each node is either terminal or has a
strictly increasing `RUN` bounded by `run.max_attempts`.

*(Divider's note, challengeable: the driver treating an attempt-exhausted node as `escalated`
without rewriting `STATUS` is what keeps `STATUS` write-once. The alternative — allowing exactly one
`STATUS` replacement — was rejected because it reintroduces mutation, which is what produced three
of round 2's majors.)*

### 3.6 Layer-2 config — partitioned key namespaces

One config file (§3.1), a YAML block inside markdown, as in the siblings' companion files. The key
namespace is partitioned so neither half needs to see the other's:

- **B owns** `corpus.*`, `sizing.*`, `run.*`, `rollup.*`
- **A owns** `analysis.*`, `verify.*`, `merge.*`

Each half's plan **declares its own keys** — name, meaning, type, default (or "required"). Neither
half reads or defaults a key in the other's namespace, **except** that B's worked example config and
B's `METHODOLOGY.md` contract section are written as **rules over the merged plan** (*"one entry per
key declared by either half's plan, with its declared meaning, type and default"*), which is how a
worked example can be complete without B inventing A's keys. The cross-namespace invariant
`sizing.max_item_bytes ≤ analysis.max_item_bytes` (§3.5) is stated in that contract section by the
same rule.

`run.dir` is named in §3.2 and both halves may reference it by name; it remains B's to document and
default.

### 3.7 `stages/common.md` — owned by B, contents fixed here

**Precedent note, because the task asks for a house-style check:** neither sibling has a
`common.md`. Both have `stages/charter.md`, a red-team charter read at *specific* stages
(`Dragonfly/stages/charter.md:1`), not a universal preamble. The universal-preamble pattern is
**Architect's own** (`Architect/stages/common.md:3`). This is a deliberate divergence from the
siblings and **B states it as such in `METHODOLOGY.md`.**

B writes it; A may rely on exactly these rules being present, and neither half restates them:

1. Every dispatched agent is **cold** — no shared context with its caller or its siblings.
2. An agent's inputs are **exactly what its caller named**; it does not go looking for substitutes.
3. Every agent is **read-only over the corpus** and writes nothing except the output file(s) its
   role names, each produced via the seam's write-to-`.tmp`-then-rename rule — **except** appends to
   `decisions.md`, which every role may make one complete line at a time.
4. **Every finding names its source.** *(The citation **format** is A's, stated in A's role files;
   common.md states the duty, not the format.)*
5. Output goes to the path the caller named; nothing else the agent says is read.
6. The Layer-2 config path reaches the agent through its arguments or its item record, and is the
   only source of corpus specifics.
7. **Facts, not interpretation** — the method's governing principle. *(Its **enforcement** in the
   analyst/verify/merge prompts is A's.)*

**Rules 1, 3, 4 and 7 state duties. Specifying the mechanism that enforces one, inside a role file,
is an addition and not a restatement** — so A can own P2's independence enforcement and P8's
enforceability without colliding with additions-only.

### 3.8 The assembled corpus-level output

`<run.dir>/findings.md` is the artifact the method exists to emit. It is produced by a
**deterministic file-concatenation step — a shell command or script in B's final stage file, NOT a
dispatched agent.** No agent reads its content, so blindness is untouched. B writes the step as a
rule over the merged plan:

> *"One section per leaf node in `index.md` order. A leaf with a merged-findings file contributes
> that file's contents verbatim under a header carrying its `STATUS` line. A leaf with a `STATUS`
> but no merged-findings file contributes a header-only section recording its state. A leaf with no
> `STATUS` contributes a header-only section marked `NOT RUN`."*

### 3.9 If a half thinks the seam is wrong

**Do not adjust the seam locally, and do not work around it. Do not file it as a finding** — the
planners beneath this cut are leaves, and `Architect/stages/leaf.md:47` is explicit: *"You do not
file findings — your output is a plan, and severities are for reviewers."*

**Instead: write a clearly-labelled `SEAM-OBJECTION` section at the head of your plan output**,
naming the seam clause and what breaks. `Union` discards nothing (`Architect/stages/combiner.md`:
*"Stick the inputs together into one. DISCARD NOTHING."*), so it travels upward unmodified to the
node that owns this seam, and it is that node's to act on. It is **not** adjudicated at `Union`
(*"None of the three is an author… A genuine conflict is kept, not resolved."*), and it must **not**
be turned into a task for the child that raised it — a child cannot change a seam its parent fixed,
so such a task would return unchanged forever (`combiner.md`: *"it is handed to a planner that
cannot fix it, and it comes back to you next iteration unchanged, forever."*).

### 3.10 What neither half owns

- `/home/zero/Desktop/claude-code-skills/Data-Distiller/` — off limits to every agent in this run.
- The sibling skills `Guarded_change/` and `Dragonfly/` — **read for style, never modified.**
- The Architect run's own files under `Architect/`.
- Any real corpus. Only the one worked example config (B) names a corpus, and it is an example.
- Installing or packaging the skill outside `Data-Distiller-impl/`, and any test harness or eval for
  the built skill. *(Divider's ruling, challengeable: the task asks for a plan to build the skill and
  does not ask for a harness. If a reviewer thinks a harness is in scope, that is a finding against
  this clause, not against the joint.)*

### 3.11 The floor

The granularity floor passes to both halves **unchanged**, in the words quoted in §0.

---

## 4. Coverage — every property owned exactly once

| | Property | Owner | Why the other half needs no channel |
|---|---|---|---|
| P1 | decompose + size, over-size strategy | **B**, entirely at decomposition time (§3.5) | A receives items as §3.3 records with fixed value domains; nothing triggers decomposition from below |
| P2 | N cold read-only analysts, each citing | **A**, including all fan-out inside the item (§3.3) | B dispatches one agent on one fixed file and never sees an analyst |
| P3 | cold verification, drops unverifiable citations | **A** | B sees only `n_dropped` (§3.4) |
| P4 | agreement-ranked merge | **A** | B sees only `max_agreement` (§3.4) |
| P5 | blind roll-up on terse per-child status | **B** | A emits the leaf line; schema, tree shape and read-permission table fixed in §3.2/§3.4 |
| P6 | per-corpus Layer-2 config | **B** owns the file and the contract; **each half owns its own key namespace** (§3.6) | neither reads the other's namespace; contract, example and the cross-namespace invariant are rules over the merged plan |
| P7 | restart and resume | **B** owns resume across nodes and the `RUN`/attempt cap (§3.5); **A** owns resume within an item and idempotent re-dispatch | both use the one presence rule fixed in §3.2 |
| P8 | facts, not interpretation | **A** owns enforcement in the role prompts; **B** owns stating it in `common.md`/`METHODOLOGY.md`/`README.md` | both take it from the task statement, which both hold |
| — | the run driver / dispatch | **B** | invocation target, arity and argument fixed in §3.3 |
| — | the assembled corpus-level output | **B** (§3.8) | a deterministic concatenation rule over the merged plan; no agent reads it |
| — | degenerate corpora | **B** (§2-B, P1) | decomposition-time |
| — | the entry surface | **B** | inventory-dependent sections are rules over the merged plan (§2-B) |
| — | house style vs. the siblings | **both**, each for its own files | both read the same siblings directly |

**No orphaned remainder** and **no portion both halves assume the other owns.** Every state in
§3.4's domain has a named producer and a named consequent in §3.5; every file in §3.2's skeleton has
a named writer and a read-permission row.

---

## 5. Floor check

The floor is *one file with its content specified*. A plans at least three role-prompt files (stages
2–4) plus its finding and citation formats; B plans at least nine (`SKILL.md`, `METHODOLOGY.md`,
`README.md`, the worked config, `stages/common.md`, stages 0, 1, 5, and the concatenation step).
Both are whole tasks far above the floor, so this is a legitimate division rather than a task that
should have been left undivided.

**B is roughly twice A's size and is arguably two design concerns** (the corpus-to-items machinery,
and the skill's entry surface). Evenness is not the test, and B **remains divisible one level
down** — its own `Divisible` call is where that gets resolved, with the seam carried down (§6).

---

## 6. Self-containment audit

| Cross-half dependency | Where it is resolved |
|---|---|
| what an item is, and its value domains (`locator` unit, `size` unit, `tier`) | **fixed in the seam**, §3.3 |
| where A writes | **fixed in the seam** — `item_dir`, absolute, in the item record |
| **what B dispatches, how many times, with what argument** | **fixed in the seam**, §3.3 — file `stages/stage-2.md`, once per leaf, one argument |
| who owns fan-out inside an item | **fixed in the seam**, §3.3 — A's entry agent |
| the status vocabulary, its types, its states' meanings | **fixed in the seam**, §3.4 |
| what each state causes, and termination | **fixed in the seam**, §3.5 |
| the over-size trigger | **eliminated** — over-size is decomposition-time only (§3.5) |
| the run-directory skeleton, mutability, the presence rule, who may read what | **fixed in the seam**, §3.2 |
| the shared agent-prompt core | **fixed in the seam**, §3.7 (written by B) |
| stage numbering and phase binding | **partitioned and bound in the seam**, §3.1 |
| config key names | **namespaces partitioned in the seam**, §3.6 |
| the size-bound invariant between the halves' two keys | **stated in the seam** (§3.5) and **documented by a build-time rule** (§3.6) |
| A's merged-findings filename | **declaration obligation** (§3.1 item 3) + **build-time rules** in B's `index.md` and `findings.md` steps |
| stop-for-human conditions | **declaration obligation** (§3.1 item 4) + a build-time rule in B's `SKILL.md` step |
| router table, stage index, loop diagram, what-a-run-produces, config contract, worked example | **build-time**: rules over the merged plan, consuming only declared fields |
| what a half does if the seam is wrong | **fixed in the seam**, §3.9 — a `SEAM-OBJECTION` section that rides `Union` upward |

**Nothing is deferred to `Union` for reconciliation.** `Union` merges and is barred from authoring
(`Architect/stages/combiner.md`: *"None of the three is an author. You do not improve, rewrite, or
adjudicate the material."*). This contradicts `divider.md`'s offer of `Union` as a legitimate home
for a cross-half dependency; that contradiction is reported in the divider's output file and is not
relied on here. §3.9 uses `Union` only as a **transport** (discard-nothing), which its charter does
guarantee.

**No element of this seam has the form "one half produces X at plan time and the other consumes
it."** Every cross-half artifact is written down in full above, partitioned so neither half needs
the other's, or resolved after the two plans are merged and before anything is built.

**Seam transport.** §3 is **prepended verbatim to each sub-task before it is passed to a child
node**, and each sub-task additionally carries the absolute path to this file. **The seam propagates
unchanged to every descendant** — a child node's own divider carries it down with whichever sub-task
it splits further.

---

## 7. Round-2 findings and their disposition

Round 2 stood at 1 `blocker`, 14 distinct `major`s (reviewers A/B/C, whose IDs are used below), and
17 `minor`/`nitpick`s. All were seam-text defects.

| Round-2 finding | Fixed at |
|---|---|
| **blocker** — invocation fixes arguments but not target or arity (C-F1, A-F4, B-M3) | §3.3 — one agent, `stages/stage-2.md`, one argument, fan-out is A's |
| No terminal failure state; `failed` means re-run forever (C-F2, A-F3) | §3.4 `escalated` + §3.5 `RUN`/`run.max_attempts` |
| Nobody assigned to *produce* `state=oversize`; A barred from `sizing.*` (C-F3, A-F1, B-M4) | `oversize` **removed**; over-size is decomposition-time (§3.5); A declares its own `analysis.max_item_bytes` |
| oversize→group breaks the IFF-leaf invariant; needs cross-half `STATUS` overwrite (C-F4, A-F2, B-M1) | §3.2 — nothing ever changes kind; `item.json` immutable, `STATUS` write-once |
| §3.9's amendment path unexecutable (`leaf.md:47`) and non-terminating (C-F5, A-F6, B-M7) | §3.9 rewritten — `SEAM-OBJECTION` rides `Union` upward to the parent |
| A's merged-findings filename consumed by two B artifacts, never declared (A-F5, C-F6, B-m1) | §3.1 declaration obligation item 3; `index.md` added to B's rule list |
| `Stop-for-human` not expressible as a rule over three fields (B-M5, A-F13) | §3.1 declaration obligation item 4; explicit rule in §2-B |
| §3.8's "non-agent" assembly names no executor (B-M6) | §3.8 — deterministic concatenation step, explicitly not a dispatched agent |
| No on-disk place for run bookkeeping under an exhaustive skeleton (B-M2, A-F9, C-F10) | §3.2 — `RUN`, the one mutable file, plus the in-flight/never-started distinction |
| `METHODOLOGY.md` loop and "what a run produces" outside B's rule list (C-F7) | §2-B — both added |
| §3.1 layout binding or illustrative? (C-F8, A-F11) | §3.1 — declared **binding at phase level** |
| Group non-`done` state undefined (A-F7); leaf `partial`/`failed` meaning (A-F8) | §3.4 — every state defined for both kinds |
| `decisions.md` append-only vs. the presence rule; absent from the read table (C-F9, B-m2) | §3.2 — explicit append exemption + read-table rows; §3.7 rule 3 carve-out |
| §3.8 undefined for an incomplete run (C-F11) | §3.8 — three cases stated |
| Degenerate corpora unowned (A-F12, B-m4) | §2-B — B's P1 defines them |
| `max_agreement` undefined over the empty set (C-F12) | §3.4 — `0` |
| Roll-up read permission too tight to write its own output (A-F15) | §3.2 read table now has a Writes column |
| `config_path` duplicated as field and argument (B-m5) | §3.3 — one argument only; `config_path` comes from `item.json` |
| B is not a single coherent design half (A-F10) | §5 — acknowledged; B remains divisible one level down |
| Test harness out of scope (B-m3) | §3.10 — kept out of scope, now labelled a challengeable divider's ruling |
| `Dragonfly/hunts/` cited as an on-disk path (A-F14) | §3.2 — cites the documented convention, not a directory |
| Quote misattributed to `Dragonfly/SKILL.md` (C-F13) | §3.1 — `Guarded_change/SKILL.md:28` |
| `name` "matching the directory" overstates the precedent (B-n1) | §3.1 — claim softened |
