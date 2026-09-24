# Proposed division — round 1

`Divisible(task, granularity)`, iteration 3, node `0`. This file is the whole proposal: the joint,
the two sub-tasks, and the seam. It is what the three cold split reviewers are handed.

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

The eight properties are numbered **P1–P8** below in the order they appear above, and every
reference in this document uses those numbers.

---

## 1. The joint

**The cut is the corpus-content boundary — the same boundary P5 already names.**

The method has two structurally different agent populations, and the task statement itself says
so: *"a blind roll-up in which a coordinating agent reads only a terse per-child status."*

| | **Below the boundary** | **Above the boundary** |
|---|---|---|
| What the agent reads | corpus **content** | structure, metadata, and one-line statuses — **never a finding, never the corpus** |
| What it produces | cited findings about content | an item inventory, and a rolled-up structure of statuses |
| Its discipline | read-only, cold, cite every finding, facts-not-interpretation | blind, stateful, idempotent, resumable |
| Its characteristic failure | a fabricated or unverifiable citation; interpretation smuggled in as fact | a coordinator that peeks at findings; work lost or silently duplicated on restart |
| Its unit of work | **one item** | **the whole corpus, and the tree over it** |

Something genuinely changes at this line: on one side of it an agent has read the corpus and its
output is *evidence*; on the other side no agent has ever read the corpus and its output is
*bookkeeping*. The two sides have disjoint inputs, disjoint outputs, disjoint failure modes and
disjoint review criteria. The blindness property (P5) is not a feature located on one side — **it
is the statement that this boundary exists and is not crossed.**

This is why the cut is not an arbitrary bisection: the interface between the halves was specified
by the owner's own task statement before any divider looked at it, and §3 below does nothing but
write that interface down concretely.

---

## 2. The two sub-tasks

### Sub-task A — the per-item finding pipeline

> **Plan the implementation of Data-Distiller's per-item finding pipeline: everything that happens
> to ONE item between being handed to the method and emitting its terse status line.** This is the
> part of the skill in which agents read corpus content.
>
> You own, as mechanism and as prompt text:
> - **P2** — N independent cold read-only analysts per item, each citing every finding. You choose
>   and justify N's default, how independence is enforced (no shared context, no visibility of a
>   sibling's output), and what "read-only" concretely forbids.
> - **P3** — the cold verification pass that drops unverifiable citations: who runs it (a separate
>   cold agent, not the analyst), what it is given, what "unverifiable" means operationally, and
>   what happens to a dropped finding (dropped, or kept and marked — decide and say).
> - **P4** — the agreement-ranked merge: how findings from N analysts are matched to each other,
>   what counts as agreement, and how the rank is computed and recorded.
> - **P8** — facts, not interpretation: the concrete, checkable discipline that keeps analyst,
>   verifier and merge output factual, written into the role prompts as an enforceable rule rather
>   than as an exhortation.
> - **The finding record and the citation format** — the internal formats of everything under
>   `items/<item_id>/` in the seam's run-directory skeleton (§3.2), except the status file, whose
>   schema the seam fixes.
> - **Your own Layer-2 config keys**, in the namespaces the seam assigns you (§3.5).
> - **Emitting the seam's per-item status line** (§3.4) at the end of your pipeline.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor, each one file
> created or one coherent edit to one file, with the content that goes in it specified. The files
> you plan are the role-prompt files under
> `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/` that your three phases need,
> plus any format-reference file you decide they need. **Your plan must declare the exact filename
> of every file it creates**, because the other half's router step is written as a rule over the
> merged plan's file list (§3.1).
>
> **Source material you must check yourself against:**
> - `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
>   `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. The closest
>   precedents for what you are writing are `Guarded_change/stages/charter.md`,
>   `Guarded_change/stages/stage-3.md`, `Dragonfly/stages/charter.md` and
>   `Dragonfly/stages/stage-7.md`: cold-reviewer prompts with citation discipline and an
>   evidence bar. Read them for form, not for content to copy.
> - This seam (§3), which you inherit and may not renegotiate.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, and state in your output that you did not.
>
> **You do not own** and must not plan: the decomposition of a corpus into items, the roll-up, the
> Layer-2 config file itself, `stages/common.md`, `SKILL.md`, `METHODOLOGY.md`, `README.md`, or the
> restart/resume mechanism. Those are the other half's, and the seam is what you are given about
> them.

### Sub-task B — the corpus envelope

> **Plan the implementation of Data-Distiller's corpus envelope: everything that turns a corpus
> into items, rolls their statuses up blind, and makes the whole thing an invocable, configurable,
> restartable Claude Code skill.** This is the part of the skill in which no agent ever reads
> corpus content.
>
> You own, as mechanism and as prompt text:
> - **P1** — decomposing and sizing the corpus into items, and the strategy for over-size items.
>   Sizing and bounding read the corpus's *shape* (paths, sizes, structural boundaries named in the
>   Layer-2 config), never its meaning. You produce the item records defined in §3.3.
> - **P5** — the blind roll-up: the coordinating role prompt, which is given the per-item status
>   lines of §3.4 **and nothing else**, and the structural rule that makes reading anything more a
>   violation rather than a temptation.
> - **P6** — the per-corpus Layer-2 config: the config **file** (one worked example, for a named
>   example corpus) and the config **contract** section in `METHODOLOGY.md`. Your own keys live in
>   the namespaces the seam assigns you (§3.5).
> - **P7** — restart and resume from on-disk state: how a restarted run learns what is already
>   done, using only the presence rule the seam fixes (§3.2), and what it re-runs.
> - **The entry surface** — `SKILL.md` (frontmatter `name`/`description`, and the router table),
>   `METHODOLOGY.md`, `README.md`, following the sibling skills' structure.
> - **`stages/common.md`** — the one file every dispatched agent reads before its role file. The
>   seam fixes the rules it must carry (§3.6); you write them.
>
> **Your deliverable is a plan** — a sequence of steps at the granularity floor, each one file
> created or one coherent edit to one file, with the content that goes in it specified. **Your
> plan must declare the exact filename of every file it creates.** Where a step's content depends
> on the full file inventory — the `SKILL.md` router table, the `METHODOLOGY.md` stage index, the
> `METHODOLOGY.md` config-key contract — **write that step as a rule over the merged plan** (e.g.
> *"one row per role-prompt file under `stages/`, in pipeline order, each row naming the file and
> its one-line purpose"*). A practitioner holding the merged plan can execute such a step; do not
> attempt to guess the other half's filenames or keys.
>
> **Source material you must check yourself against:**
> - `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
>   `/home/zero/Desktop/claude-code-skills/Dragonfly/` — house style and structure. The closest
>   precedents for what you are writing are `Dragonfly/SKILL.md` and `Guarded_change/SKILL.md`
>   (frontmatter + router table), `Dragonfly/METHODOLOGY.md` (why-it-exists, the loop diagram, the
>   two layers, the config contract, what a run produces), `Dragonfly/dragonfly.companion.md` and
>   `Guarded_change/guarded-change.companion.md` (a worked Layer-2 config), and the sibling
>   `README.md` files.
> - This seam (§3), which you inherit and may not renegotiate.
>
> **⛔ `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS** — do not read, list,
> grep or otherwise open it, and state in your output that you did not.
>
> **You do not own** and must not plan: what an analyst does with an item's content, the citation
> format, the verification pass, the merge, or any file under `items/<item_id>/` other than the
> status file. Those are the other half's, and the seam is what you are given about them.

---

## 3. The seam

**Both halves are planned concurrently and blind to each other. There is no channel between them
and neither may assume one.** Everything in this section is fixed here, stated identically to both
halves, and inherited by everything beneath the cut. **Neither half may change it.** A half that
believes a seam element is wrong or missing **files that as a finding in its own plan output** —
it does not adjust it locally.

### 3.1 Build root, layout, and who owns which file

Everything is built under `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`. Neither
half creates a file outside it. The layout follows the sibling skills:

```
Data-Distiller-impl/
  SKILL.md                       B    frontmatter (name: data-distiller-impl) + router table
  METHODOLOGY.md                 B    orientation, the two layers, config contract, what a run produces
  README.md                      B
  data-distiller.<example>.md    B    one worked Layer-2 config for a named example corpus
  stages/
    common.md                    B    read verbatim by EVERY dispatched agent, before its role file
    <B's role-prompt files>      B    decomposition/sizing; the blind roll-up coordinator
    <A's role-prompt files>      A    analyst; verification; merge
```

**Role-prompt filenames are each half's own to choose and to declare in its plan.** Any step whose
content is a function of the full inventory — the router table, the stage index, the config
contract — is written **as a rule over the merged plan**, not as a guessed list. This is
executable: the two plans are merged before anyone builds anything.

**Additions-only discipline (house rule, and the sibling skills' own):** `stages/common.md` holds
what *every* dispatched agent needs; a role file **adds** and never restates or modifies a common
rule. If a half finds it needs to modify a common rule, that is a finding, not an edit.

### 3.2 The run-directory skeleton, and the presence rule

A run of the built skill writes under a directory given by the Layer-2 config key `run.dir`:

```
<run.dir>/
  index.md                   B    the item inventory produced by decomposition
  decisions.md               B    append-only run log
  items/<item_id>/
    item.json                B    the item record (§3.3)
    STATUS                   A    exactly one line, the schema in §3.4
    <A's per-item outputs>   A    per-analyst output, per-analyst verified output, merged findings
```

**The presence rule — this is what makes P7 possible without a channel:** *every file above is
written complete or not at all* (write to a `.tmp` sibling, then rename), so **the existence of a
file means the step that produces it finished.** Resume reasons about existence only. **No agent
above the boundary opens a file under `items/<item_id>/` other than `item.json` and `STATUS`.**

### 3.3 The item record — what B hands A

`items/<item_id>/item.json`, produced by B's decomposition, consumed by A's pipeline. Exactly
these fields; A may not require others, B may not omit any:

| Field | Meaning |
|---|---|
| `item_id` | stable identifier, derived from the locator; safe as a directory name |
| `locator` | where the content is: an absolute path, plus an optional range within it |
| `size` | the item's measured size, in the unit the Layer-2 config names |
| `tier` | the sizing tier this item fell into |
| `parent_item_id` | the item this was split out of; empty unless produced by the over-size strategy |
| `config_path` | absolute path to the Layer-2 config in force for this run |

### 3.4 The per-item status line — the ONLY thing that crosses the boundary upward

`items/<item_id>/STATUS` is **one line**, written by A at the end of its pipeline, read by B's
roll-up. Whitespace-separated fields, in this order:

```
<item_id> <state> <n_findings> <n_dropped> <max_agreement> <findings_path>
```

- `state` ∈ `done` | `partial` | `failed` | `oversize-deferred`
- `n_findings` — findings surviving verification and merge for this item
- `n_dropped` — findings dropped by the verification pass (P3)
- `max_agreement` — the highest agreement count any surviving finding reached (P4)
- `findings_path` — path to A's merged finding file, **for the human, not for the coordinator**

**B's coordinating agent may read this line and nothing else.** It may not open `findings_path`,
any other file under `items/<item_id>/`, or the corpus. **A may not add fields**; if A needs a
field that is not here, that is a finding A files, not a field A adds.

### 3.5 Layer-2 config — partitioned key namespaces

One config file (§3.1), a YAML block inside markdown, as in the sibling skills' companion files.
**The key namespace is partitioned so the halves cannot collide and neither needs to see the
other's keys:**

- **B owns** `corpus.*`, `sizing.*`, `run.*`, `rollup.*`
- **A owns** `analysis.*`, `verify.*`, `merge.*`

Each half's plan **declares its own keys** — name, meaning, type, default (or "required"). Neither
half reads, documents, or defaults a key in the other's namespace. B's config-contract section in
`METHODOLOGY.md` and B's worked example config are written as a rule over the merged plan's
declared keys (§3.1).

### 3.6 `stages/common.md` — owned by B, contents fixed here

B writes it; A may rely on exactly these rules being in it, and neither half restates them in a
role file:

1. Every dispatched agent is **cold** — no shared context with its caller or its siblings.
2. An agent's inputs are **exactly what its caller named**; it does not go looking for substitutes.
3. Agents that read corpus content are **read-only**: they write nothing except their one named
   output file.
4. **Every finding names its source.** (The *format* of a citation is A's, stated in A's role
   files — common.md states the duty, not the format.)
5. Output goes to the path the caller named; nothing else the agent says is read.
6. The Layer-2 config path is passed as an argument, and is the only source of corpus specifics.
7. **Facts, not interpretation** — stated as the method's governing principle. (Its *enforcement*
   in the analyst/verify/merge prompts is A's.)

### 3.7 What neither half owns

- `/home/zero/Desktop/claude-code-skills/Data-Distiller/` — off limits to every agent in this run.
- The sibling skills `Guarded_change/` and `Dragonfly/` — **read for style, never modified.**
- The Architect run's own files under `Architect/`.
- Any real corpus. The skill is corpus-agnostic; only the one worked example config (B) names a
  corpus, and it is an example.
- Installing or packaging the skill anywhere outside `Data-Distiller-impl/`, and any test harness
  or eval for the built skill. Out of scope for both halves.

### 3.8 The floor

The granularity floor passes to both halves **unchanged**, in the words quoted in §0.

---

## 4. Coverage check — every property is owned exactly once

| | Property | Owner | The other half's stake, and why it is not a channel |
|---|---|---|---|
| P1 | decompose + size, over-size strategy | **B** | A receives items as §3.3 records; the record is fixed here, not derived from B's plan |
| P2 | N cold read-only analysts, each citing | **A** | B never sees an analyst or a finding |
| P3 | cold verification, drops unverifiable citations | **A** | B sees only `n_dropped` in §3.4 |
| P4 | agreement-ranked merge | **A** | B sees only `max_agreement` in §3.4 |
| P5 | blind roll-up on terse per-child status | **B** | A emits the §3.4 line; its schema is fixed here |
| P6 | per-corpus Layer-2 config | **B** owns the file + the contract section; **each half owns its own key namespace** (§3.5) | neither reads the other's namespace; the contract section is a rule over the merged plan |
| P7 | restart and resume from on-disk state | **B** owns the resume mechanism; **A owns obeying the presence rule** for its own files | the presence rule is fixed here (§3.2), so neither half derives it from the other |
| P8 | facts, not interpretation | **A** owns enforcement in the role prompts; **B** owns stating it as doctrine in `common.md`/`METHODOLOGY.md`/`README.md` | both take it from the task statement, which both hold |
| — | house style vs. the sibling skills | **both**, each for its own files | both read the same sibling skills directly |
| — | the entry surface (`SKILL.md`, `METHODOLOGY.md`, `README.md`) | **B** | inventory-dependent rows are written as rules over the merged plan (§3.1) |

**No orphaned remainder** and **no portion both halves assume the other owns**: P6, P7 and P8 are
the three that touch both sides, and each is split by an explicit ownership line above rather than
left to be inferred.

---

## 5. Floor check

Neither half is anywhere near the floor. The floor is *one file with its content specified*; A
plans at least three role-prompt files plus its finding and citation formats, and B plans at least
seven files including the whole entry surface. Both are comfortably whole tasks above the floor,
so this is a legitimate division rather than a task that should have been left undivided.

---

## 6. Self-containment audit of this seam

Checked against the three permitted homes for a cross-half dependency:

| Dependency | Where it is resolved |
|---|---|
| what an item looks like | **fixed in the seam** (§3.3) |
| the status vocabulary | **fixed in the seam** (§3.4) |
| the run-directory skeleton and the presence rule | **fixed in the seam** (§3.2) |
| the shared agent-prompt core | **fixed in the seam** (§3.6), written by B |
| config key names | **namespaces partitioned in the seam** (§3.5); neither half reads the other's |
| the router table, stage index, config contract | **build-time**: written as rules over the merged plan (§3.1) |

**Nothing is deferred to `Union`.** `Union` is not available as a reconciliation site: its own
charter forbids it (`Architect/stages/combiner.md`: *"None of the three is an author. You do not
improve, rewrite, or adjudicate the material."*, and *"A genuine conflict is kept, not
resolved."*). This is recorded as a contradiction against `divider.md` in the divider's output; it
is not relied on here.

**No element of this seam has the form "one half produces X at plan time and the other consumes
it."** Every cross-half artifact is either written down in full above, or resolved after the two
plans are merged and before anything is built.
