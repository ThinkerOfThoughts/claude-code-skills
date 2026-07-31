# Sub-task A — as returned by Divisible(task, granularity), iteration 3, node 0

**This file IS the sub-task string.** Section 1 is the seam, inherited verbatim and identically by
both halves; section 2 is your half. The seam is not negotiable — see its clause "If a half thinks
the seam is wrong". Provenance, for the node and the human only: `Architect/runs/data-distiller/it3/0/split-round-4.md`
(it holds the divider's deliberations and the other half's brief — **a planner does not open it**).

---

# PART 1 — THE SEAM (identical in both halves)

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

# PART 2 — YOUR HALF

### Sub-task A — the per-item finding pipeline

**Plan the implementation of Data-Distiller's per-item finding pipeline: everything that happens
to ONE item from the moment the run driver dispatches your pipeline entry agent on it to the
moment that item's `STATUS` line is written.** This is the part of the skill in which agents read
corpus content for meaning and produce cited findings.

**How you are invoked (fixed, §3.3):** the other half's run driver dispatches **one** agent on
**`stages/stage-2.md`** — your pipeline entry — with **one** argument: `item_dir`, the absolute
path to the item's node directory. Everything else you need is in `item_dir/item.json`. **That
entry agent owns all further fan-out inside the item** — spawning the N analysts, the verifier,
and the merge. The driver dispatches nothing else for that item, and may re-dispatch it.

You own, as mechanism and as prompt text:
- **P2** — N independent cold read-only analysts per item, each citing every finding. Choose and
  justify N's default; specify how independence is enforced **at your entry agent's dispatch
  point** (no shared context, no visibility of a sibling's output), how fan-out is bounded, and
  what "read-only" concretely forbids an analyst. *(§3.7 rules 1 and 3 state the duty; the
  enforcement mechanism is yours, and stating it is an addition, not a restatement.)*
- **P3** — the cold verification pass that drops unverifiable citations: who runs it (a separate
  cold agent, **never the analyst that produced the finding**), what it is given, what
  "unverifiable" means operationally, and what happens to a dropped finding.
- **P4** — the agreement-ranked merge: how findings from N analysts are matched, what counts as
  agreement, and how the rank is computed and recorded.
- **P8** — facts, not interpretation: the concrete, checkable discipline that keeps analyst,
  verifier and merge output factual, written into the role prompts as an **enforceable rule
  rather than an exhortation**.
- **The finding record and the citation format** — the internal formats of every file you write
  under a leaf node directory except `STATUS`, whose schema §3.4 fixes. **Diagnostic detail for a
  `partial` or `failed` item goes in a file of your own under the node directory** — you do not
  write the run log (§3.7 rule 3).
- **Your acceptance bound.** Declare a config key `analysis.max_item_bytes` — the largest
  `size_bytes` your pipeline accepts. Handed a larger item, your entry agent writes
  `state=failed` rather than analysing it badly. **You do not own the over-size strategy** —
  splitting over-size items is decomposition-time work and is the other half's (§3.5).
- **Resume *within* an item** (your share of P7): re-dispatched on a node directory that already
  holds some of your outputs, your pipeline must not redo completed work, and **must be able to
  finish the item and replace its `STATUS`** (§3.4 — `STATUS` is replaceable by its owner).
  Re-dispatch must be safe and idempotent. *Resume across nodes is the other half's.*
- **Your own Layer-2 config keys**, in the namespaces §3.6 assigns you.
- **Writing and, on a later pass, replacing the leaf `STATUS` line** (§3.4).

**Your deliverable is a plan** — a sequence of steps at the granularity floor: one file created
or one coherent edit to one file, with the content that goes in it specified. Your role-prompt
files live under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/` at stage
numbers **2–4**, bound at phase level by §3.1: **2 = pipeline entry + analysts, 3 = verification,
4 = merge.**

**Your plan must declare** (§3.1) — these are consumed by the other half's build-time rules, so
omitting any of them leaves a step in the merged plan unexecutable:
1. for every file it creates: **filename**, **stage number / phase**, **one-line purpose**;
2. every config key it defines: **name, meaning, type, default (or "required")**;
3. **the filename of your merged-findings file** — the one file per item carrying the final ranked
   findings (the other half's `index.md` and `findings.md` steps are rules over this name);
4. your **stop-for-human conditions**, as a list of one-line conditions;
5. nothing about the other half.

**Source material you must check yourself against:**
- `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
  `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. Closest
  precedents: `Guarded_change/stages/charter.md`, `Guarded_change/stages/stage-3.md`,
  `Dragonfly/stages/charter.md`, `Dragonfly/stages/stage-7.md` — cold-reviewer prompts with
  citation discipline and an evidence bar. Read them for form, not for content to copy.
- The seam — **PART 1 of this document**, above. It is here in full; you need no other
  file for it, and you must not go looking for one (the divider's working notes and the
  other half's brief are deliberately not given to you). You inherit the seam and may not
  renegotiate it; §3.9 says what to do if you think it is wrong.

**⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
output that you did not.

**You do not own** and must not plan: decomposing the corpus into items, the over-size strategy,
the run driver, the roll-up, resume across nodes, the run log, the Layer-2 config file,
`stages/common.md`, `SKILL.md`, `METHODOLOGY.md`, `README.md`, or `findings.md`.
