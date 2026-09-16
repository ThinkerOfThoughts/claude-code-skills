# Proposed division — round 4 (final round; the cap is four)

`Divisible(task, granularity)`, iteration 3, node `0`. Standalone: this file is the whole proposal.

**What changed from round 3.** All three round-3 reviewers again endorsed the cut; none objected to
going forward. Their blockers converged on **one defect I introduced in round 3**: making `STATUS`
write-once in order to kill mutation. Write-once and "re-run a `partial` leaf" cannot both hold — a
successful re-run has nowhere to record itself, so `done` is unreachable after any hiccup and P7's
resume is inert. Round 4 replaces write-once with **replace-atomically-by-the-owner**, and closes
the cluster of termination and escalation gaps that came with it. **The joint is unchanged, for the
fourth round running.**

**Two things this round does NOT paper over**, because they are defects in Architect's own apparatus
rather than in this division, and my caller asked for them plainly:

- **The seam has no guaranteed transport.** §6 says the seam is prepended verbatim to each
  sub-task. Nothing in `divider.md` or `node.md` instructs that; `node.md` passes only
  `division.first` / `division.second` to child nodes. The division's return value states it as an
  instruction, and it is reported as a gap in `divide-0.md`.
- **A leaf has no guaranteed upward channel for objecting to a seam its parent fixed.**
  `combiner.md`'s `Consensus` takes 2-of-3 on steps and **discards the odd plan**, so a lone
  planner's objection can be discarded before any human or node sees it. §3.9 states this honestly
  rather than promising a channel that does not exist, and it is reported as a gap in `divide-0.md`.

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
> and the merge. The driver dispatches nothing else for that item, and may re-dispatch it.
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
>   under a leaf node directory except `STATUS`, whose schema §3.4 fixes. **Diagnostic detail for a
>   `partial` or `failed` item goes in a file of your own under the node directory** — you do not
>   write the run log (§3.7 rule 3).
> - **Your acceptance bound.** Declare a config key `analysis.max_item_bytes` — the largest
>   `size_bytes` your pipeline accepts. Handed a larger item, your entry agent writes
>   `state=failed` rather than analysing it badly. **You do not own the over-size strategy** —
>   splitting over-size items is decomposition-time work and is the other half's (§3.5).
> - **Resume *within* an item** (your share of P7): re-dispatched on a node directory that already
>   holds some of your outputs, your pipeline must not redo completed work, and **must be able to
>   finish the item and replace its `STATUS`** (§3.4 — `STATUS` is replaceable by its owner).
>   Re-dispatch must be safe and idempotent. *Resume across nodes is the other half's.*
> - **Your own Layer-2 config keys**, in the namespaces §3.6 assigns you.
> - **Writing and, on a later pass, replacing the leaf `STATUS` line** (§3.4).
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor: one file created
> or one coherent edit to one file, with the content that goes in it specified. Your role-prompt
> files live under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/` at stage
> numbers **2–4**, bound at phase level by §3.1: **2 = pipeline entry + analysts, 3 = verification,
> 4 = merge.**
>
> **Your plan must declare** (§3.1) — these are consumed by the other half's build-time rules, so
> omitting any of them leaves a step in the merged plan unexecutable:
> 1. for every file it creates: **filename**, **stage number / phase**, **one-line purpose**;
> 2. every config key it defines: **name, meaning, type, default (or "required")**;
> 3. **the filename of your merged-findings file** — the one file per item carrying the final ranked
>    findings (the other half's `index.md` and `findings.md` steps are rules over this name);
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
>   `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it3/0/split-round-4.md`.
>   You inherit it and may not renegotiate it; §3.9 says what to do if you think it is wrong.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
> output that you did not.
>
> **You do not own** and must not plan: decomposing the corpus into items, the over-size strategy,
> the run driver, the roll-up, resume across nodes, the run log, the Layer-2 config file,
> `stages/common.md`, `SKILL.md`, `METHODOLOGY.md`, `README.md`, or `findings.md`.

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
> - **The run driver** — walks `index.md`, decides which nodes still need work (§3.5), dispatches
>   the other half's pipeline entry agent on each leaf node exactly as §3.3 fixes, dispatches the
>   roll-up on each group node, bounds concurrency, and maintains every node's `RUN` file. It may
>   read `index.md`, any `item.json`, any `STATUS`, any `RUN`, `decisions.md`, and the config —
>   **never a finding**.
> - **P5** — the blind roll-up: the coordinating role prompt, given **the `STATUS` lines of its own
>   children and nothing else** (§3.4), writing its own node's `STATUS`. The tree may be any depth.
> - **P6** — the per-corpus Layer-2 config: the config **file** (one worked example for a named
>   example corpus) and the config **contract** section in `METHODOLOGY.md`. Your keys live in the
>   namespaces §3.6 assigns you.
> - **P7** — restart and resume **across** nodes: how a restarted run learns what is done, using
>   the presence-and-state rule of §3.5 and the `RUN` files, and what it re-runs.
> - **The run log** `decisions.md` — the append-only record (§3.2). Only your roles write it.
> - **The assembled corpus-level output** — `<run.dir>/findings.md` (§3.8): a **deterministic
>   file-concatenation step, not a dispatched agent**.
> - **The entry surface** — `SKILL.md` (frontmatter + router table + `Stop-for-human`),
>   `METHODOLOGY.md`, `README.md`, following the sibling skills' structure.
> - **`stages/common.md`** — the one file every dispatched agent reads before its role file. §3.7
>   fixes the rules it must carry; you write them.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor. Your role-prompt
> files take stage numbers **0–1 and 5–9**, bound at phase level by §3.1: **0 = decomposition and
> sizing, 1 = the run driver, 5 = the blind roll-up**; 6–9 are yours to use or leave unused.
>
> **Your plan must declare** the same things §2-A lists (items 1, 2 and 4 apply to you; item 3 is
> A's; you declare nothing about A).
>
> **Steps written as rules over the merged plan.** Where a step's content depends on the **full**
> file, key, filename or stop-condition inventory, write it as a rule, not a guessed list — a
> practitioner holding the merged plan can execute such a rule. **Do not guess the other half's
> filenames, stage numbers, purposes, config keys, merged-findings filename or stop conditions.**
> This applies to, at least: the `SKILL.md` router table; the `SKILL.md` `Stop-for-human` section
> (*"one row per stop condition declared by either half's plan"*); the `METHODOLOGY.md` stage
> index; the `METHODOLOGY.md` **loop diagram** and **"what a run produces"** sections; the
> `METHODOLOGY.md` config-key contract (including the §3.5 size invariant); the worked example
> config; `index.md`'s per-node findings pointer (*"…naming that node's merged-findings file as
> declared in the merged plan"*); and `findings.md`'s assembly rule (§3.8).
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
>   `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it3/0/split-round-4.md`.
>   You inherit it and may not renegotiate it; §3.9 says what to do if you think it is wrong.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
> output that you did not.
>
> **You do not own** and must not plan: what an analyst does with an item's content, the citation
> format, the verification pass, the merge, fan-out within an item, resume within an item, or any
> file under a leaf node directory other than `item.json`, `RUN` and `STATUS`.

---

## 3. The seam

**Both halves are planned concurrently and blind to each other. There is no channel between them
and neither may assume one.** Everything here is fixed, stated identically to both halves, and
inherited by everything beneath the cut. **Neither half may change it**; §3.9 says what to do
instead. **If you divide your sub-task further, prepend this seam text verbatim to both of your own
sub-tasks.**

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

### 3.2 The run-directory skeleton, the write rules, and who may read what

A run writes under a directory given by the Layer-2 config key `run.dir` (B's to document and
default; both halves may reference the name). The siblings document run artifacts as living inside
the skill directory (`Guarded_change/SKILL.md:27` — `changes/<slug>/`; `Dragonfly/SKILL.md:31` and
`Dragonfly/METHODOLOGY.md:143` — `hunts/<slug>/`); B's default follows that convention.

**The skeleton is EXHAUSTIVE. Neither half may add a file or directory to it**, except that A's
per-item outputs inside a leaf node directory are A's to name and number.

```
<run.dir>/
  index.md                       B    the node inventory produced by decomposition
  decisions.md                   B    append-only run log — ONLY B's roles write it
  findings.md                    B    the assembled corpus-level output (§3.8)
  nodes/<node_id>/
    item.json                    B    present IFF this node is a LEAF (an item); §3.3. IMMUTABLE.
    RUN                          B    the driver's per-node attempt counter; MUTABLE
    STATUS                       leaf: A (+B, see §3.4)   group: B    one line, §3.4. REPLACEABLE.
    <A's per-item outputs>       A    leaf only: per-analyst, per-analyst-verified, merged findings,
                                      and A's own diagnostic file for a partial/failed item
```

**The tree is recursive and any depth.** `<node_id>` is dot-separated (`0`, `0.1`, `0.1.2`) and
directories nest to match. **A node is a LEAF — an item — if and only if it has `item.json`;
otherwise it is a GROUP** whose children are the nodes one level below it. One skeleton expresses a
flat corpus and a nested one identically, which is what P5's *"per-**child** status"* and *"too
large for one context window"* jointly require: a single coordinator reading one line per item does
not fit a corpus this method exists for.

`node_id` and `item_id` match `[A-Za-z0-9._-]+`.

**No node ever changes kind.** A node is created as a leaf or as a group by decomposition and stays
that way. `item.json` is never written twice and never deleted. This is what removed round 2's
`oversize` state, whose only purpose was to make a leaf become a group mid-run.

**The three write rules:**

1. **Write-complete-or-not-at-all (the presence rule).** Every file except `decisions.md` is
   written to a `.tmp` sibling and renamed into place, so **a reader never sees a partial file.**
   *Presence means "a complete version of this file exists" — it does NOT by itself mean the node is
   finished; the `state` field says that.*
2. **`STATUS` is REPLACEABLE by its owner**, atomically, by the same `.tmp`+rename. Round 3 made it
   write-once and all three reviewers filed the consequence as a blocker: a re-run leaf could never
   record its success, so `done` was unreachable after any hiccup and P7's resume was inert.
   Replacement is safe precisely because nothing else about a node mutates.
3. **`decisions.md` is append-only**: each writer appends one complete line at a time (an atomic
   `O_APPEND` write). Its existence means "the run started". **Only B's roles write it** — A has no
   path to it and does not need one (§2-A: A's diagnostics go in its own per-item file).
4. **`RUN`** is a small mutable file holding one integer: how many times the driver has run this
   node. The driver increments it **before** each dispatch. Its presence means "this node has been
   attempted", which is what distinguishes *never started* from *started by a run that died*.
   **Every node has one — leaf and group alike.**

**Who may read what — this is the blindness mechanism, stated once:**

| Role | May read | May write |
|---|---|---|
| **B's decomposer** (stage 0) | the corpus (for shape), the config | `index.md`, `item.json`, a leaf's `STATUS` **with `escalated` only** (§3.5), appends to `decisions.md` |
| **B's run driver** (stage 1) | `index.md`, any `item.json`, any `STATUS`, any `RUN`, `decisions.md`, the config. **Never a finding.** | any `RUN`, a node's `STATUS` **with `escalated` only** (§3.5), appends to `decisions.md` |
| **B's roll-up coordinator** (stage 5) | **the `STATUS` lines of its own children, and nothing else.** Not `item.json`, not `RUN`, not `decisions.md`, not a finding, not the corpus. | its own node's `STATUS` |
| **A's roles** (stages 2–4) | their own item's corpus content, their own `item.json`, their own item's earlier outputs, the config | their own item's outputs, and their own leaf's `STATUS` |
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
idempotent and lets it finish a partially-completed item and replace its `STATUS`.

### 3.4 The `STATUS` line — the ONLY thing that crosses the boundary upward

`nodes/<node_id>/STATUS` is **one line**, whitespace-separated, exactly five fields:

```
<node_id> <state> <n_findings> <n_dropped> <max_agreement>
```

| Field | Domain |
|---|---|
| `state` | leaf: `done` \| `partial` \| `failed` \| `escalated`.  group: `done` \| `escalated`. |
| `n_findings` | non-negative integer: findings surviving verification and merge in this subtree |
| `n_dropped` | non-negative integer: findings dropped by the verification pass (P3) |
| `max_agreement` | non-negative integer count of analysts: the highest agreement count any surviving finding in this subtree reached. **`0` when there are no surviving findings.** |

**A node with no `STATUS` file has not finished. Absence is the only "not yet" marker.** A `STATUS`
may be **replaced** by its owner (§3.2 rule 2); replacement is the mechanism by which a re-run leaf
records its success.

**Leaf states — written by A** (except `escalated`, below):
- `done` — the pipeline completed: analysts, verification and merge all ran and a merged-findings
  file exists. **Terminal.**
- `partial` — some phases completed, the rest could not; the three integers describe what exists.
  **Re-runnable.**
- `failed` — no merged-findings file could be produced (unreadable item, an item larger than
  `analysis.max_item_bytes`, a tool failure). The integers are `0 0 0`. **Re-runnable.**
- `escalated` — **terminal, do not re-run**, and the human is told. **Written by B, not A**, in
  exactly two situations (§3.5): the decomposer could not size an item down, or the driver reached
  the attempt cap. A never writes it and never needs to know the cap.

**Group states — written by B's roll-up, from its children's `STATUS` lines and nothing else:**
- `done` — every child is `done`.
- `escalated` — at least one child is `escalated`.

There is deliberately no group `partial`: **the driver runs a group's roll-up only once every child
is terminal** (`done` or `escalated`), so those two values are exhaustive. This also keeps the
coordinator's decision computable from children's lines alone — round 3's version needed `RUN` and
`decisions.md`, which the coordinator is forbidden to read.

`n_findings` and `n_dropped` sum over children; `max_agreement` is the max over children (`0` if
none).

**There is deliberately no path field.** Round 1 carried `findings_path` and all three reviewers
filed it: putting the locator of the findings into the blind coordinator's only input turns P5 from
a structure into an exhortation. The human-facing pointer lives in `index.md` and `findings.md`
(§3.8); the coordinator never holds an address for a finding.

**A may not add fields.** If A needs one, §3.9 says what to do.

### 3.5 The control loop — over-size, resume, escalation, and termination

**The over-size strategy is decomposition-time work and lives entirely in B (stage 0).** Given a
candidate item larger than `sizing.max_item_bytes`, B's decomposer splits it along the structural
boundaries the Layer-2 config names into child nodes, recursively, until every leaf is within the
bound or `sizing.max_resplits` is exhausted.

**An item that cannot be brought within the bound is still emitted as a leaf node** — with its
`item.json`, and with its `STATUS` written immediately by the decomposer as
`<node_id> escalated 0 0 0`. **Nothing vanishes:** it appears in `index.md`, it is counted by the
roll-up, and `findings.md` carries a header-only section for it (§3.8). The driver sees a terminal
state and never dispatches A on it. The escalation is appended to `decisions.md`.

**The bound must be one A's pipeline can actually take.** A declares `analysis.max_item_bytes` and B
declares `sizing.max_item_bytes`; **the seam's invariant is `sizing.max_item_bytes ≤
analysis.max_item_bytes`**, stated by B in `METHODOLOGY.md`'s config contract as a rule over the
merged plan's declared keys (§3.6). At run time, A's entry agent handed a larger item writes
`state=failed` rather than analysing it badly. No state crosses the boundary to trigger a re-split,
and no node ever changes kind.

**Resume and the driver's per-pass decision** read file existence, `RUN`'s integer, and — for
`STATUS` only — the `state` field. (`state` is already a field above-boundary roles may read, so
this costs no blindness.)

| Node | Observed | What B's run driver does |
|---|---|---|
| leaf | no `STATUS` | increment `RUN`; dispatch A's entry agent (§3.3) |
| leaf | `state=partial` or `failed` | if `RUN < run.max_attempts` → increment `RUN`, re-dispatch (A's within-item resume avoids redoing work and may replace `STATUS` with `done`). Else → **replace `STATUS` with `escalated`** (integers preserved from the observed line), append to `decisions.md`, stop for the human. |
| leaf | `state=done` or `escalated` | **terminal.** Do nothing. |
| group | any child not terminal | do nothing yet — work the children first |
| group | every child terminal, no `STATUS` | increment `RUN`; dispatch the roll-up (§3.4) |
| group | every child terminal, `RUN ≥ run.max_attempts`, still no `STATUS` | **write `STATUS` = `escalated`**, append to `decisions.md`, stop for the human |
| group | has a `STATUS` | **terminal.** Do nothing. |

`run.max_attempts` is B's key.

**Termination argument.** Every node is in exactly one of: terminal (`done`/`escalated`), or
attempted at most `run.max_attempts` times. `RUN` strictly increases before each dispatch and is
bounded, and the cap converts any non-terminal node into `escalated`. Leaves are handled before
their parents (a group is only run when its children are terminal), and the tree is finite, so the
driver reaches a state where every node is terminal.

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
3. Every agent is **read-only over the corpus** and writes nothing except the output file(s) its own
   role file names, each produced via write-to-`.tmp`-then-rename. **`decisions.md` is the one
   append-only file, and only the roles whose role file names it may append to it.**
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

### 3.9 If a half thinks the seam is wrong — and the honest limit of that path

**Do not adjust the seam locally, and do not work around it. Do not file it as a finding** — the
planners beneath this cut are leaves, and `Architect/stages/leaf.md:47` is explicit: *"You do not
file findings — your output is a plan, and severities are for reviewers."*

**Do this instead:** write a clearly-labelled **`SEAM-OBJECTION`** section at the head of your plan
output, naming the seam clause and what breaks, **and** state the consequence inside every plan step
it affects, as an assumption or limitation of that step.

**The honest limit, stated rather than papered over.** There is **no guaranteed** channel from a
leaf to the node that fixed this seam. Three leaves' plans go to `Consensus`, which takes *"2-of-3
on numbered steps, INCLUDING ORDER"* and **discards the odd plan** (`Architect/stages/combiner.md`),
so a lone planner's `SEAM-OBJECTION` can be discarded before anyone sees it. It survives when two of
three planners raise it — which is the case where the seam is genuinely broken rather than
misread — and that is why the objection must also appear inside the affected steps, where it is
content two planners can independently produce. `Union` (the node-path combiner) does discard
nothing, so an objection that survives `Consensus` does reach the parent. **This gap is in
Architect's apparatus, not in this division, and it is reported as such in the divider's output.**

An objection must **never** be turned into a task for the child that raised it: a child cannot
change a seam its parent fixed, so such a task would return unchanged forever (`combiner.md`: *"it
is handed to a planner that cannot fix it, and it comes back to you next iteration unchanged,
forever."*).

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
| P5 | blind roll-up on terse per-child status | **B** | A emits the leaf line; schema, tree shape, read table and the group-state rule are fixed in §3.2/§3.4 |
| P6 | per-corpus Layer-2 config | **B** owns the file and the contract; **each half owns its own key namespace** (§3.6) | neither reads the other's namespace; contract, example and the size invariant are rules over the merged plan |
| P7 | restart and resume | **B** owns resume across nodes, `RUN` and the attempt cap (§3.5); **A** owns resume within an item and idempotent re-dispatch, including replacing its `STATUS` | both use the write rules fixed in §3.2 |
| P8 | facts, not interpretation | **A** owns enforcement in the role prompts; **B** owns stating it in `common.md`/`METHODOLOGY.md`/`README.md` | both take it from the task statement, which both hold |
| — | the run driver / dispatch | **B** | invocation target, arity and argument fixed in §3.3 |
| — | the run log `decisions.md` | **B** only | A writes its diagnostics into its own per-item file |
| — | escalation | **B** only (decomposer or driver), via the one `escalated` state | A never needs to know the cap |
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
2–4) plus its finding, citation and diagnostic formats; B plans at least nine (`SKILL.md`,
`METHODOLOGY.md`, `README.md`, the worked config, `stages/common.md`, stages 0, 1, 5, and the
concatenation step). Both are whole tasks far above the floor, so this is a legitimate division
rather than a task that should have been left undivided.

**B is roughly twice A's size and is arguably two design concerns** (the corpus-to-items machinery,
and the skill's entry surface). Evenness is not the test, and B **remains divisible one level down**
— its own `Divisible` call is where that gets resolved, with the seam carried down (§3, first
paragraph, and §6).

---

## 6. Self-containment audit

| Cross-half dependency | Where it is resolved |
|---|---|
| what an item is, and its value domains | **fixed in the seam**, §3.3 |
| where A writes | **fixed in the seam** — `item_dir`, absolute, in the item record |
| **what B dispatches, how many times, with what argument** | **fixed in the seam**, §3.3 |
| who owns fan-out inside an item | **fixed in the seam**, §3.3 — A's entry agent |
| the status vocabulary, its types, its states' meanings, who writes each | **fixed in the seam**, §3.4 |
| mutability of every file | **fixed in the seam**, §3.2 three write rules |
| what each state causes, escalation, and termination | **fixed in the seam**, §3.5 (with a termination argument) |
| the over-size trigger | **eliminated** — over-size is decomposition-time only (§3.5) |
| the run log, and A's lack of a path to it | **fixed in the seam** — only B writes `decisions.md`; A's diagnostics are its own file (§3.2, §3.7 rule 3) |
| the run-directory skeleton and who may read what | **fixed in the seam**, §3.2 |
| the shared agent-prompt core | **fixed in the seam**, §3.7 (written by B) |
| stage numbering and phase binding | **partitioned and bound in the seam**, §3.1 |
| config key names | **namespaces partitioned in the seam**, §3.6 |
| the size-bound invariant between the halves' two keys | **stated in the seam** (§3.5), **documented by a build-time rule** (§3.6) |
| A's merged-findings filename | **declaration obligation** (§3.1) + **build-time rules** in B's `index.md` and `findings.md` steps |
| stop-for-human conditions | **declaration obligation** (§3.1) + a build-time rule in B's `SKILL.md` step |
| router table, stage index, loop diagram, what-a-run-produces, config contract, worked example | **build-time**: rules over the merged plan, consuming only declared fields |
| what a half does if the seam is wrong | **stated in the seam with its honest limit**, §3.9 |

**Nothing is deferred to `Union` for reconciliation.** `Union` merges and is barred from authoring
(`Architect/stages/combiner.md`: *"None of the three is an author. You do not improve, rewrite, or
adjudicate the material."*). This contradicts `divider.md`'s offer of `Union` as a legitimate home
for a cross-half dependency; the contradiction is reported in the divider's output and not relied on
here.

**No element of this seam has the form "one half produces X at plan time and the other consumes
it."** Every cross-half artifact is written down in full above, partitioned so neither half needs
the other's, or resolved after the two plans are merged and before anything is built.

**Seam transport.** §3 is **prepended verbatim to each sub-task before it is passed to a child
node**, and each sub-task additionally carries the absolute path to this file; §3's first paragraph
instructs each half to do the same if it divides further. **Neither `divider.md` nor `node.md`
provides a mechanism for this** — `node.md` passes only the sub-task value — so the division's
return value states it as an explicit instruction to the node, and the gap is reported in the
divider's output.

---

## 7. Round-3 findings and their disposition

Round 3 stood at 4 `blocker`s (two reviewers filed the same one), 13 `major`s and 12
`minor`/`nitpick`s across the three reviews. All were seam-text defects; all three reviewers
endorsed the cut.

| Round-3 finding | Fixed at |
|---|---|
| **blocker (all three)** — `STATUS` write-once vs. re-running `partial`/`failed`: success can never be recorded, `done` unreachable, P7 inert | §3.2 write rule 2 — `STATUS` is **replaceable by its owner**, atomically |
| **blocker** — leaf `escalated` has no producer; A cannot read `RUN` | §3.4 + §3.5 — `escalated` is **written by B** (decomposer or driver), never by A |
| **major** — group nodes have no attempt counter or cap; the termination claim was false for them | §3.2 — every node has `RUN`; §3.5 — group rows in the driver table + an explicit termination argument |
| **major** — group `escalated` depended on `RUN`/`decisions.md`, which the roll-up may not read | §3.4 — group state is computed from children's `STATUS` lines alone; group domain reduced to `done`/`escalated`; the roll-up runs only when all children are terminal |
| **major** — an unsplittable over-size item is neither leaf nor group and vanishes from `findings.md` | §3.5 — emitted **as a leaf** with `item.json` and a decomposer-written `escalated` `STATUS`; counted and reported |
| **major** — `SEAM-OBJECTION` traverses `Consensus`, which discards the odd plan | §3.9 — the limit is **stated honestly**, the objection must also appear in the affected steps, and the gap is reported in the divider's output rather than papered over |
| **major** — A is obliged to append to `decisions.md` with no path to it | §3.2 / §3.7 rule 3 — **only B writes the run log**; A's diagnostics go in its own per-item file |
| **major** — the seam's prepend-and-propagate transport is asserted but instructed nowhere in `node.md`/`divider.md`, and cannot survive B's re-division | §3 first paragraph (propagate on re-division) + §6 (stated as an instruction in the return value) + **reported as an apparatus gap** in the divider's output |
| minors and nitpicks | carried forward against the sub-tasks they bear on; recorded in the divider's output |
