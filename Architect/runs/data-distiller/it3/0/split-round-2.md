# Proposed division — round 2

`Divisible(task, granularity)`, iteration 3, node `0`. Standalone: this file is the whole proposal.

**What changed from round 1.** All three round-1 reviewers endorsed the cut and none objected to
going forward; every one of their 22 `major` findings was a defect in the **seam text**, which is
the divider's own output and not something a blind planner could act on. So the joint is unchanged
and §3 has been rewritten against those findings. The round-1 → round-2 disposition table is §7.

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

The eight properties are **P1–P8** in the order they appear above; every reference uses those
numbers.

---

## 1. The joint

**The cut is the finding boundary — the boundary P5 already names.**

> *"a blind roll-up in which a coordinating agent reads only a terse per-child status"*

Round 1's statement of this joint was *"no agent above the boundary reads the corpus"*, and all
three reviewers were right that it is **false**: B's decomposer must open corpus files to find the
structural boundaries it splits on. The line is not *reads the corpus* — it is **reads for
meaning**:

| | **Below the boundary** | **Above the boundary** |
|---|---|---|
| What the agent reads | corpus content **for meaning** | corpus **shape** (paths, sizes, delimiters), item records, and one-line statuses — **never a finding** |
| What it produces | cited findings — **evidence** | an item inventory and a tree of statuses — **bookkeeping** |
| Its discipline | cold, read-only, cite every finding, facts-not-interpretation | cold, read-only over the corpus, blind to findings, idempotent, resumable |
| Its characteristic failure | a fabricated or unverifiable citation; interpretation smuggled in as fact | a coordinator that peeks at findings; work lost or silently duplicated on restart |
| Its unit of work | **one item** | **the corpus, and the tree over it** |
| Its review criterion | does every citation resolve? | is it blind, and is it idempotent? |

Something genuinely changes at this line. Below it an agent has understood corpus content and its
output is *evidence*; above it no agent has ever seen a finding and its output is *bookkeeping*.
Disjoint inputs, disjoint outputs, disjoint failure modes, disjoint review criteria.

**P5 is not a feature sitting on one side of this line — P5 is the assertion that the line exists
and is not crossed.** That is why the cut is not an arbitrary bisection: the interface was
specified by the owner's own task statement before any divider looked at it, and §3 does nothing
but write that interface down concretely.

**The alternative considered and rejected.** *Method (`stages/*`) vs. envelope (`SKILL.md`,
`METHODOLOGY.md`, `README.md`, config)* has a thinner seam — the item record, the status schema and
the stage numbering would all be internal to one half. It was rejected because its joint is a
**packaging** boundary, not a design one: the envelope half is derivative documentation of a method
it does not own, and nothing about the *method* changes at that line. It is recorded here because
no later reviewer sees the alternatives available at this cut.

---

## 2. The two sub-tasks

**Both sub-task texts below are delivered with §3 (the seam) prepended verbatim** — see §6.

### Sub-task A — the per-item finding pipeline

> **Plan the implementation of Data-Distiller's per-item finding pipeline: everything that happens
> to ONE item from the moment the run driver invokes your pipeline on it to the moment its
> `STATUS` line is written.** This is the part of the skill in which agents read corpus content
> for meaning and produce cited findings.
>
> **You are invoked as:** the run driver (the other half's) calls your pipeline with exactly two
> arguments — the absolute path to the item's node directory, and `config_path` (§3.3). Everything
> else you need is in `item.json` in that directory.
>
> You own, as mechanism and as prompt text:
> - **P2** — N independent cold read-only analysts per item, each citing every finding. Choose and
>   justify N's default; specify how independence is enforced at the point your pipeline dispatches
>   an analyst (no shared context, no visibility of a sibling's output) and what "read-only"
>   concretely forbids an analyst. *(§3.7 rules 1 and 3 state the duty; the enforcement mechanism
>   is yours, and stating it is not restating them.)*
> - **P3** — the cold verification pass that drops unverifiable citations: who runs it (a separate
>   cold agent, never the analyst that produced the finding), what it is given, what "unverifiable"
>   means operationally, and what happens to a dropped finding.
> - **P4** — the agreement-ranked merge: how findings from N analysts are matched, what counts as
>   agreement, and how the rank is computed and recorded.
> - **P8** — facts, not interpretation: the concrete, checkable discipline that keeps analyst,
>   verifier and merge output factual, written into the role prompts as an **enforceable rule
>   rather than an exhortation**.
> - **The finding record and the citation format** — the internal formats of every file you write
>   under a leaf node directory (§3.2) except `STATUS`, whose schema the seam fixes.
> - **Resume *within* an item** (your share of P7): your pipeline, re-invoked on a leaf node
>   directory that already holds some of your outputs, must not redo completed work. Use the
>   presence rule (§3.2). *Resume across items is the other half's.*
> - **Your own Layer-2 config keys**, in the namespaces §3.6 assigns you.
> - **Writing the leaf `STATUS` line** (§3.4) as the last act of your pipeline.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor: one file created
> or one coherent edit to one file, with the content that goes in it specified. The files you plan
> are the role-prompt files under
> `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/` that your phases need
> (stage numbers **2–4**, see §3.1), plus any format-reference file they need.
> **For every file your plan creates, your plan must declare: its exact filename, its stage number
> / position in the pipeline, and a one-line purpose** — the other half's router and stage-index
> steps are written as rules over the merged plan and consume exactly those three things (§3.1).
>
> **Source material you must check yourself against:**
> - `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
>   `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. The closest
>   precedents for what you are writing are `Guarded_change/stages/charter.md`,
>   `Guarded_change/stages/stage-3.md`, `Dragonfly/stages/charter.md`,
>   `Dragonfly/stages/stage-7.md`: cold-reviewer prompts with citation discipline and an evidence
>   bar. Read them for form, not for content to copy.
> - The seam, §3 of this document, prepended to this sub-task and also readable at
>   `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it3/0/split-round-2.md`.
>   You inherit it and may not renegotiate it; if you believe an element is wrong, §3.9 says where
>   that finding goes.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
> output that you did not.
>
> **You do not own** and must not plan: decomposing the corpus into items, the over-size strategy,
> the run driver, the roll-up, resume across items, the Layer-2 config file, `stages/common.md`,
> `SKILL.md`, `METHODOLOGY.md`, `README.md`, or the assembled corpus-level `findings.md`. Those
> are the other half's, and §3 is what you are given about them.

### Sub-task B — the corpus envelope

> **Plan the implementation of Data-Distiller's corpus envelope: everything that turns a corpus
> into items, drives the per-item pipeline over them, rolls their statuses up blind, and makes the
> whole thing an invocable, configurable, restartable Claude Code skill.** This is the part of the
> skill in which no agent ever reads a **finding**. Your decomposer *does* open corpus files — to
> find structural boundaries and measure size — and is a cold, read-only agent while doing so; what
> it must never do is read for meaning or emit a finding.
>
> You own, as mechanism and as prompt text:
> - **P1** — decomposing and sizing the corpus into items, and the strategy for over-size items,
>   including the re-decomposition loop of §3.5. You produce `index.md` and the item records of
>   §3.3, and you **validate every `locator` before writing it** (§3.3).
> - **The run driver** — the role that walks `index.md`, decides which nodes still need work
>   (§3.5), invokes the other half's per-item pipeline on each leaf node with the two arguments
>   §3.3 fixes, and bounds concurrency. The driver may read `index.md`, `item.json` and `STATUS`,
>   and never a finding.
> - **P5** — the blind roll-up: the coordinating role prompt, which is given **the `STATUS` lines
>   of its own children and nothing else** (§3.4), and writes its own node's `STATUS`. The tree may
>   be any depth (§3.2).
> - **P6** — the per-corpus Layer-2 config: the config **file** (one worked example for a named
>   example corpus) and the config **contract** section in `METHODOLOGY.md`. Your own keys live in
>   the namespaces §3.6 assigns you.
> - **P7** — restart and resume **across** nodes: how a restarted run learns what is done, using
>   the presence-and-state rule of §3.5, and what it re-runs. *(Resume within one item is the other
>   half's.)*
> - **The assembled corpus-level output** — `<run.dir>/findings.md` (§3.2): a **mechanical, non-agent
>   assembly step**, written as a rule over the merged plan. No agent reads it, so it does not touch
>   blindness.
> - **The entry surface** — `SKILL.md` (frontmatter + router table), `METHODOLOGY.md`, `README.md`,
>   following the sibling skills' structure.
> - **`stages/common.md`** — the one file every dispatched agent reads before its role file. §3.7
>   fixes the rules it must carry; you write them.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor: one file created
> or one coherent edit to one file, with the content that goes in it specified. Your role-prompt
> files take stage numbers **0–1 and 5–9** (§3.1).
> **For every file your plan creates, your plan must declare: its exact filename, its stage number
> / position in the pipeline, and a one-line purpose.**
> Where a step's content depends on the **full** file or key inventory — the `SKILL.md` router
> table, the `METHODOLOGY.md` stage index, the `METHODOLOGY.md` config-key contract, the worked
> example config, the `Stop-for-human` section, and `findings.md`'s assembly rule — **write that
> step as a rule over the merged plan** (e.g. *"one row per role-prompt file under `stages/`, in
> stage-number order, each row naming the file and its declared one-line purpose"*). A practitioner
> holding the merged plan can execute such a step. **Do not guess the other half's filenames,
> stage numbers, purposes or config keys.**
>
> **Source material you must check yourself against:**
> - `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
>   `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. The closest
>   precedents are `Dragonfly/SKILL.md` and `Guarded_change/SKILL.md` (frontmatter + router table +
>   `Stop-for-human`), `Dragonfly/METHODOLOGY.md` (why-it-exists, the loop diagram, the stage
>   index, the two layers, the config contract, what a run produces, human-in-the-loop),
>   `Dragonfly/dragonfly.companion.md` and `Guarded_change/guarded-change.companion.md` (a worked
>   Layer-2 config), and the sibling `README.md` files.
> - The seam, §3 of this document, prepended to this sub-task and also readable at
>   `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it3/0/split-round-2.md`.
>   You inherit it and may not renegotiate it; if you believe an element is wrong, §3.9 says where
>   that finding goes.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, do not invoke the installed `data-distiller` skill, and state in your
> output that you did not.
>
> **You do not own** and must not plan: what an analyst does with an item's content, the citation
> format, the verification pass, the merge, resume within an item, or any file under a leaf node
> directory other than `item.json` and `STATUS`. Those are the other half's, and §3 is what you are
> given about them.

---

## 3. The seam

**Both halves are planned concurrently and blind to each other. There is no channel between them
and neither may assume one.** Everything in this section is fixed here, stated identically to both
halves, and inherited by everything beneath the cut. **Neither half may change it**; §3.9 says what
to do instead.

### 3.1 Build root, layout, ownership, and stage numbering

Everything is built under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`. Neither
half creates a file outside it. The layout follows the sibling skills, **with one declared
divergence** (`stages/common.md`, see §3.7):

```
Data-Distiller-impl/
  SKILL.md                       B    frontmatter + router table + Stop-for-human
  METHODOLOGY.md                 B    orientation, the two layers, stage index, config contract,
                                      what a run produces, human-in-the-loop
  README.md                      B
  data-distiller.<example>.md    B    one worked Layer-2 config for a named example corpus
  stages/
    common.md                    B    read verbatim by EVERY dispatched agent, before its role file
    stage-0.md … stage-1.md      B    decomposition/sizing; the run driver
    stage-2.md … stage-4.md      A    analyst; verification; merge
    stage-5.md … stage-9.md      B    the blind roll-up, and anything else B needs
```

**Stage numbering is fixed here because neither half can converge on it alone** — A's files sit
*between* B's decomposition and B's roll-up, so the numbering is inherently joint, and the siblings
key their router, stage index and gate log off stage numbers (`Dragonfly/SKILL.md`: *"Step numbers
below are the canonical stage numbers used everywhere"*). **B owns numbers 0–1 and 5–9; A owns
2–4.** Within its own range a half may use letter suffixes as the siblings do (`stage-0a.md`), and
need not use every number.

**The `SKILL.md` frontmatter `name` is `data-distiller-impl`**, matching the directory, and B states
in `README.md` that this deliberately avoids colliding with the separately installed
`data-distiller` skill.

**Per-file declaration obligation (both halves).** Every plan step that creates a file declares the
**filename**, the **stage number / pipeline position**, and a **one-line purpose**. B's
inventory-dependent steps are rules over exactly these three fields.

**Additions-only discipline.** `stages/common.md` holds what *every* dispatched agent needs; a role
file **adds** and never restates or modifies a common rule. Specifying the *enforcement mechanism*
for a common duty in a role file is an addition, not a restatement (§3.7).

### 3.2 The run-directory skeleton, and the presence rule

A run writes under a directory given by the Layer-2 config key `run.dir` (B's to document and
default; both halves may reference the name). Default follows the siblings, which keep run
artifacts inside the skill directory (`Guarded_change/changes/`, `Dragonfly/hunts/`).

**The skeleton is EXHAUSTIVE. Neither half may add a file or directory to it.**

```
<run.dir>/
  index.md                       B    the node inventory produced by decomposition
  decisions.md                   B    append-only run log
  findings.md                    B    the assembled corpus-level output (mechanical, §3.8)
  nodes/<node_id>/
    STATUS                       leaf: A   group: B    one line, schema in §3.4
    item.json                    B    present IFF this node is a LEAF (an item); §3.3
    <A's per-item outputs>       A    leaf only: per-analyst, per-analyst-verified, merged findings
```

**The tree is recursive and any depth.** `<node_id>` is dot-separated (`0`, `0.1`, `0.1.2`), and
directories nest to match. **A node is a LEAF — an item — if and only if it has `item.json`;
otherwise it is a GROUP** whose children are the nodes one level below it. This one skeleton
expresses a flat corpus (all leaves are children of the root) and a nested one identically, which
is what P5's *"per-**child** status"* and *"too large for one context window"* jointly require: a
single coordinator reading one line per item does not fit a corpus this method exists for.

`node_id` and `item_id` match `[A-Za-z0-9._-]+`.

**The presence rule.** *Every file above is written complete or not at all* — write to a `.tmp`
sibling, then rename — so **the existence of a file means the step that produces it finished.**
This is the atomicity P7 depends on; §3.7 rule 3 is written so that obeying it does not forbid the
`.tmp` write.

**Who may read what — this is the blindness mechanism, stated once:**

| Role | May read |
|---|---|
| **B's decomposer** (stage 0) | the corpus (for shape), the config |
| **B's run driver** (stage 1) | `index.md`, any `item.json`, any `STATUS`, the config. **Never a finding.** |
| **B's roll-up coordinator** (stage 5+) | **the `STATUS` lines of its own children, and nothing else.** Not `item.json`, not a finding, not the corpus. |
| **A's roles** (stages 2–4) | the corpus content of their own item, their own item's `item.json`, their own item's earlier outputs, the config |

### 3.3 The item record — what B hands A

`nodes/<node_id>/item.json`, produced by B's decomposition, consumed by A's pipeline. **Exactly
these fields; A may not require others, B may not omit any.** Value domains are fixed here, not
derived from either half's config namespace:

| Field | Meaning and fixed domain |
|---|---|
| `node_id` | this node's dotted id; also its directory name |
| `item_id` | stable item identifier, `[A-Za-z0-9._-]+` |
| `item_dir` | **absolute** path to this node's directory — A never has to resolve `run.dir` |
| `locator` | `{"path": <absolute path>, "lines": [<first>, <last>]}` — **inclusive, 1-based line numbers**, or `"lines": null` for the whole file. **Lines are the unit, fixed here.** |
| `size_bytes` | the item's size in **bytes**. Fixed here as the seam's unit, whatever unit `sizing.*` uses internally for tiering. |
| `tier` | **opaque to A.** A must not branch on it. It exists for B's sizing and for the human. |
| `parent_node_id` | the group node this is a child of; `"0"`'s parent is `null` |
| `config_path` | absolute path to the Layer-2 config in force for this run |

**B validates every `locator` at decomposition time**: a locator that does not resolve to a
readable path and range is **not written as an item**; the failure is recorded in `decisions.md`.
(Both siblings make this an explicit rule — `Guarded_change/METHODOLOGY.md` *"Paths are validated,
not assumed"*; `Dragonfly/SKILL.md` *"Validate config paths at hunt start"*.)

**The invocation contract.** B's run driver invokes A's pipeline with exactly two arguments:
`item_dir` and `config_path`. A's pipeline begins on receipt of those two.

### 3.4 The `STATUS` line — the ONLY thing that crosses the boundary upward

`nodes/<node_id>/STATUS` is **one line**, whitespace-separated, exactly five fields:

```
<node_id> <state> <n_findings> <n_dropped> <max_agreement>
```

- `state` — leaf: `done` | `partial` | `failed` | `oversize`. Group: `done` | `partial` | `failed`.
- `n_findings` — **non-negative integer**: findings surviving verification and merge in this
  subtree
- `n_dropped` — **non-negative integer**: findings dropped by the verification pass (P3)
- `max_agreement` — **non-negative integer count of analysts**: the highest agreement count any
  surviving finding in this subtree reached (P4)
- **A not-yet-run node has no `STATUS` file at all.** Absence is the only "not yet" marker.

**There is deliberately no path field.** Round 1 carried `findings_path` here and all three
reviewers filed it: putting the locator of the findings into the blind coordinator's only input
turns P5 from a structure into an exhortation. The human-facing pointer is derivable
(`nodes/<node_id>/` + A's declared merged-findings filename) and is recorded once in `index.md`
and in `findings.md`; the coordinator never holds it.

- **A leaf's `STATUS` is written by A**, as the last act of its pipeline (§3.7 rule 3 explicitly
  permits this second output).
- **A group's `STATUS` is written by B's roll-up coordinator**, from its own children's `STATUS`
  lines and nothing else. That *is* the blind roll-up: `n_findings` and `n_dropped` sum over
  children, `max_agreement` is the max, and `state` is `done` only if every child is `done`.
- **A may not add fields.** If A needs a field that is not here, that is a finding A files (§3.9),
  not a field A adds.

### 3.5 What each state causes — the control loop, fixed here

Resume, and the driver's per-pass decision, read **file existence and, for `STATUS` only, the
`state` field.** (`state` is already a field above-boundary roles may read, so this costs no
blindness.)

| Observed | What B's run driver does |
|---|---|
| no `STATUS` | run the node: leaf → invoke A's pipeline; group → run the roll-up once all children have `STATUS` |
| `state=done` | **terminal.** Do not re-run. |
| `state=partial` or `state=failed` | **re-run the node.** A's within-item resume (§2-A) means completed sub-steps are not redone. |
| `state=oversize` (leaf) | **re-decompose.** B's over-size strategy runs on that item and emits child nodes with `parent_node_id` set; the node becomes a group; the driver dispatches the children. After `sizing.max_resplits` re-splits the item is **escalated to the human** and left `failed`. |

`oversize` exists because B sizes an item from its shape and A discovers at read time that it does
not fit — the seam closes that loop rather than leaving a state with no consequent.

### 3.6 Layer-2 config — partitioned key namespaces

One config file (§3.1), a YAML block inside markdown, as in the siblings' companion files. The key
namespace is partitioned so neither half needs to see the other's:

- **B owns** `corpus.*`, `sizing.*`, `run.*`, `rollup.*`
- **A owns** `analysis.*`, `verify.*`, `merge.*`

Each half's plan **declares its own keys** — name, meaning, type, default (or "required"). Neither
half reads or defaults a key in the other's namespace, **except** that B's worked example config
and B's `METHODOLOGY.md` contract section are written as **rules over the merged plan** (*"one
entry per key declared by either half's plan, with its declared meaning, type and default"*) — that
is how a worked example can be complete without B inventing A's keys.

`run.dir` is named in §3.2 and both halves may reference it by name; it remains B's to document and
default.

### 3.7 `stages/common.md` — owned by B, contents fixed here

**Precedent note, because the task asks for a house-style check:** neither sibling has a
`common.md`. Both have `stages/charter.md`, a red-team charter read at *specific* stages, not a
universal preamble. The universal-preamble pattern is **Architect's own**
(`Architect/stages/common.md`). This is a deliberate divergence from the siblings and **B states it
as such in `METHODOLOGY.md`.**

B writes it; A may rely on exactly these rules being present, and neither half restates them:

1. Every dispatched agent is **cold** — no shared context with its caller or its siblings.
2. An agent's inputs are **exactly what its caller named**; it does not go looking for substitutes.
3. Every agent is **read-only over the corpus** and writes nothing except the output file(s) its
   role names, each produced via the seam's write-to-`.tmp`-then-rename rule. *(A's merge role
   names two: its merged findings file and the leaf `STATUS`.)*
4. **Every finding names its source.** *(The citation **format** is A's, stated in A's role files;
   common.md states the duty, not the format.)*
5. Output goes to the path the caller named; nothing else the agent says is read.
6. The Layer-2 config path is passed as an argument and is the only source of corpus specifics.
7. **Facts, not interpretation** — the method's governing principle. *(Its **enforcement** in the
   analyst/verify/merge prompts is A's.)*

**Rules 1, 3, 4 and 7 state duties. Specifying the mechanism that enforces one, inside a role file,
is an addition and not a restatement** — this is explicitly permitted, so that A can own P2's
independence enforcement and P8's enforceability without colliding with additions-only.

### 3.8 The assembled corpus-level output

`<run.dir>/findings.md` is the artifact the method exists to emit. It is produced by a
**mechanical, non-agent assembly step owned by B**, written as a rule over the merged plan: *"one
section per leaf node in `index.md` order, each embedding that node's merged findings file
verbatim, with its `STATUS` line as a header."* **No agent reads it**, so blindness is untouched.

### 3.9 If a half thinks the seam is wrong

**File it as a `blocker`/`major` finding in your own plan output. Do not adjust the seam locally
and do not work around it.** Such a finding is **not** adjudicated at `Union` — `Union` merges and
is barred from authoring (`Architect/stages/combiner.md`: *"None of the three is an author… A
genuine conflict is kept, not resolved."*). It surfaces at the node's plan red-team round, and
`Severity` turns it into the next task (`Architect/stages/node.md`, loop steps 3–4).

### 3.10 What neither half owns

- `/home/zero/Desktop/claude-code-skills/Data-Distiller/` — off limits to every agent in this run.
- The sibling skills `Guarded_change/` and `Dragonfly/` — **read for style, never modified.**
- The Architect run's own files under `Architect/`.
- Any real corpus. Only the one worked example config (B) names a corpus, and it is an example.
- Installing or packaging the skill outside `Data-Distiller-impl/`, and any test harness or eval
  for the built skill. Out of scope for both halves.

### 3.11 The floor

The granularity floor passes to both halves **unchanged**, in the words quoted in §0.

---

## 4. Coverage — every property owned exactly once

| | Property | Owner | Why the other half needs no channel |
|---|---|---|---|
| P1 | decompose + size, over-size strategy | **B** | A receives items as §3.3 records with fixed value domains; the re-decomposition loop is closed in §3.5 |
| P2 | N cold read-only analysts, each citing | **A** | B never sees an analyst or a finding |
| P3 | cold verification, drops unverifiable citations | **A** | B sees only `n_dropped` (§3.4) |
| P4 | agreement-ranked merge | **A** | B sees only `max_agreement` (§3.4) |
| P5 | blind roll-up on terse per-child status | **B** | A emits the leaf line; the schema, the tree shape and the read-permission table are fixed in §3.2/§3.4 |
| P6 | per-corpus Layer-2 config | **B** owns the file and the contract; **each half owns its own key namespace** (§3.6) | neither reads the other's namespace; the contract and worked example are rules over the merged plan |
| P7 | restart and resume | **B** owns resume **across** nodes (§3.5); **A** owns resume **within** an item (§2-A) | both use the one presence rule fixed in §3.2 |
| P8 | facts, not interpretation | **A** owns enforcement in the role prompts; **B** owns stating it in `common.md`/`METHODOLOGY.md`/`README.md` | both take it from the task statement, which both hold |
| — | the run driver / dispatch | **B** (§2-B, §3.2 read table) | explicitly assigned; invocation contract fixed in §3.3 |
| — | the assembled corpus-level output | **B** (§3.8) | a rule over the merged plan; no agent reads it |
| — | the entry surface | **B** | inventory-dependent rows are rules over the merged plan (§3.1) |
| — | house style vs. the siblings | **both**, each for its own files | both read the same siblings directly |

**No orphaned remainder** and **no portion both halves assume the other owns.** The three properties
that touch both sides (P6, P7, P8) and the three non-property remainders round 1 left orphaned (the
driver, the over-size return path, the corpus-level output) each carry an explicit ownership line
**in §3**, not merely in this audit table.

---

## 5. Floor check

The floor is *one file with its content specified*. A plans at least three role-prompt files
(stages 2–4) plus its finding and citation formats; B plans at least eight (`SKILL.md`,
`METHODOLOGY.md`, `README.md`, the worked config, `stages/common.md`, decomposition, driver,
roll-up). Both are whole tasks far above the floor, so this is a legitimate division rather than a
task that should have been left undivided. B is roughly twice A's size; evenness is not the test,
and B remains divisible one level down.

---

## 6. Self-containment audit

| Cross-half dependency | Where it is resolved |
|---|---|
| what an item is, and its value domains (`locator` unit, `size` unit, `tier`) | **fixed in the seam**, §3.3 |
| where A writes | **fixed in the seam** — `item_dir`, absolute, in the item record (§3.3) |
| how A is invoked | **fixed in the seam**, §3.3 |
| the status vocabulary, its types, and its delimiter | **fixed in the seam**, §3.4 |
| what each state causes | **fixed in the seam**, §3.5 |
| the run-directory skeleton, the tree shape, the presence rule, who may read what | **fixed in the seam**, §3.2 |
| the shared agent-prompt core | **fixed in the seam**, §3.7 (written by B) |
| stage numbering | **partitioned in the seam**, §3.1 |
| config key names | **namespaces partitioned in the seam**, §3.6 |
| router table, stage index, config contract, worked example, Stop-for-human, `findings.md` | **build-time**: rules over the merged plan, consuming the three declared fields of §3.1 and the declared keys of §3.6 |

**Nothing is deferred to `Union`.** `Union` is not available as a reconciliation site: its own
charter forbids it (`Architect/stages/combiner.md`: *"None of the three is an author. You do not
improve, rewrite, or adjudicate the material."* and *"A genuine conflict is kept, not resolved."*).
This contradicts `divider.md`'s offer of `Union` as a legitimate home for a cross-half dependency;
the contradiction is reported in the divider's output file and is not relied on here.

**No element of this seam has the form "one half produces X at plan time and the other consumes
it."** Every cross-half artifact is either written down in full above, partitioned so neither half
needs the other's, or resolved after the two plans are merged and before anything is built.

**Seam transport.** The seam is only worth anything if both halves hold it identically, so it is not
delivered by pointer: **§3 is prepended verbatim to each sub-task before it is passed to a child
node**, and each sub-task additionally carries the absolute path to this file. **The seam propagates
unchanged to every descendant** — a child node's own divider carries it down with whichever sub-task
it splits further.

---

## 7. Round-1 findings and their disposition

All 22 round-1 `major`s and all 15 `minor`/`nitpick`s were seam-text defects. Disposition:

| Round-1 finding (reviewer IDs) | Fixed at |
|---|---|
| Nothing owns dispatch / the run driver (A-M2, B-S1, C-F2) | §2-B, §3.2 read table, §3.3 invocation contract |
| `findings_path` makes blindness an exhortation (A-M1, B-S3, C-F14) | §3.4 — field removed |
| Item record cannot locate/size; `run.dir` unreachable by A (A-M3, B-S9) | §3.3 `item_dir`, `locator` in lines, `size_bytes`; §3.6 carve-out |
| `tier` domain / `locator` unit unfixed (B-S5, C-F4) | §3.3 — unit fixed; `tier` declared opaque to A |
| Existence-only resume absorbs `failed`/`partial` (A-M4) | §3.5 — resume reads `state` |
| Intra-item resume orphaned (C-F5) | §2-A — A owns resume within an item |
| `oversize` has no consumer (A-M5, B-S6, C-F6) | §3.5 — re-decomposition loop + escalation after `sizing.max_resplits` |
| No corpus-level output (A-M6a, B-S7) | §3.2, §3.8 — `findings.md`, mechanical, B |
| No level above the item; flat skeleton vs. per-*child* roll-up (A-M6b, B-S14, C-F3) | §3.2 — recursive `nodes/<node_id>/`, any depth |
| Skeleton exhaustive or illustrative? (A-M6) | §3.2 — declared **exhaustive** |
| §3.2 vs §3.4 contradiction on `item.json` (B-S2) | §3.2 read table — driver may, coordinator may not |
| Seam has no path; may not travel down (B-S4, C-F9) | §6 — prepended verbatim + absolute path + propagates to descendants |
| Joint stated falsely ("no agent reads the corpus") (B-S8, C-F1) | §1 — restated as the **finding** boundary |
| B's router rule needs order + purpose A never declares (C-F7) | §3.1 — three-field declaration obligation on both halves |
| No `stages/` numbering convention (C-F8) | §3.1 — ranges partitioned, B 0–1 & 5–9, A 2–4 |
| Read-only rule vs. `.tmp` write (C-F10); rules 1/3 vs. A's ownership (B-S10, A-m3) | §3.7 rules 3 and the additions/enforcement clause |
| Status line untyped, whitespace-fragile (A-m1) | §3.4 — integer types, id charset, path field gone |
| Worked example config needs A's keys (A-m2) | §3.6 — explicit carve-out |
| `locator` never validated (A-m4) | §3.3 — B validates at decomposition |
| No Stop-for-human section (A-m5) | §2-B — added to the rule-over-merged-plan list |
| `common.md` has no sibling pedigree (A-N1, B-S11, C-F12) | §3.7 — Architect cited as precedent, divergence declared |
| Ownership resolutions living only in §4 (B-S12) | §3.5, §3.7, §2-A/§2-B — promoted into the seam and sub-tasks |
| Seam amendment path undefined (C-F13) | §3.9 |
| Alternative cut never considered (C-F11) | §1 — named and dismissed with reasons |
| Skill name divergence unstated (B-S15) | §3.1 |
| §6's forward reference in the past tense (A-N2, B-S13) | §6 — reworded |
| Run dir outside the skill directory undeclared (B, unfiled) | §3.2 — default follows the siblings |
