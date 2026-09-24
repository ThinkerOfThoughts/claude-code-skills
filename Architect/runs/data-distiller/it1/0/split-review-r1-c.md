# Split review — round 1, reviewer C

**Reviewing:** the proposed division at `Architect/runs/data-distiller/0/split-round-1.md`
(sub-task A = the frame; sub-task B = `stages/`; seam = "read once by the invoking agent" vs.
"read verbatim mid-run by dispatched cold agents").

**Inputs I held:** the task, the granularity floor, the proposed division. No plan (correctly —
the divider had none either).

**What I could not check / did not read:** `/home/zero/Desktop/claude-code-skills/Data-Distiller/`
(off limits, honoured — not read, listed or grepped); no other reviewer's output in the runs
directory. I did read the Architect role files I was pointed at (`stages/common.md`,
`stages/redteam.md`, `stages/redteam-split.md`) and, to check the seam's executability, the
Architect role files that describe how a division is executed (`stages/node.md`,
`stages/divider.md`, `stages/leaf.md`, `stages/combiner.md`) — flagged here because a reviewer
opening files the task did not name is a departure worth declaring.

**The floor is right for this task** and I applied it as given. I have not filed anything whose
only remedy is decomposition below it.

---

## Findings

### F1 — `blocker` — The seam is directional, but nothing delivers it. B cannot consume A's contract.

The division's load-bearing mechanism is a one-way contract: sub-task A "**OWNS the vocabulary the
whole skill uses**, and fixes it before the other half writes a line" (split-round-1.md:71–75), and
"**B may assume every name, path, key and field it needs is defined by A, and may cite them without
redefining them**" (split-round-1.md:140–141).

There is no channel that carries A's contract to B.

- `Architect/stages/node.md:50–53`: on a non-empty division the node spawns **both** child nodes
  together — `(division.first, plan, …)` and `(division.second, plan, …)` — with the **same
  incoming `plan`**, then "Wait for both". `.1`'s return value is not routed into `.2`; both are
  merged afterwards by `Union`.
- `Architect/stages/leaf.md:19–20`: a leaf's inputs are "the **task**, the **plan** structure to
  fill, and the **granularity floor**." Nothing else.

So the agents planning B are cold, concurrent with A, and will never see a single name A chose.
Concretely, B's half then fails in one of two ways:

1. **It falls short of the floor.** The floor requires "one file created … **with the content that
   goes in it specified**." A step reading *"create `stages/analyst.md`, instructing the analyst to
   emit findings in the record schema defined in `METHODOLOGY.md`"* does not specify the content —
   the executor must go read a file that the other half is still specifying. Every one of B's six
   files needs at least an output path, an artifact name and a record schema, so this is not an
   edge case; it is B's whole half.
2. **Or B invents a parallel vocabulary**, and `Union` preserves the collision by design:
   `Architect/stages/combiner.md:62–64` — "Do not harmonise wording… When two items are close but
   not identical, keep both"; `:57–61` — a genuine conflict "is kept, not resolved". The merged
   plan then contains two incompatible schemas for the finding record and the per-child status
   record, and the seam that was supposed to prevent exactly that has instead guaranteed it.

The `CONTRACT-DELTA:` escape hatch (split-round-1.md:108–111) is aimed the wrong way. It handles
B needing a **new** name A did not define. The actual failure is B needing an **existing** name it
cannot read — for which the hatch offers nothing, and under which every step in B would carry a
delta line, which is the same as having no contract.

This is a `blocker` under the seam question: the interface is stated but unsound, and sub-task B
as written ("This half CONSUMES the contract from sub-task A", :108) cannot be executed.

*Direction, not a required remedy:* a division planned by non-communicating concurrent halves needs
a **non-directional** seam — each half self-contained in the names it must write down — or the
schema-bearing decisions all placed on one side of the cut (see F8).

### F2 — `blocker` — Orphaned remainder: the invoking agent's own run procedure belongs to neither half.

Sub-task B is scoped by reader: "the prompt files that **dispatched cold agents** read verbatim at
run time. Each is a prompt, not documentation — **the reader is an agent with no context but this
file**" (split-round-1.md:88–90). Sub-task A "does **NOT** write the procedure body of any
dispatched-agent role… and **restates no procedure**" (split-round-1.md:77–78).

Nothing in either scope owns the procedure the **invoking** agent executes: find and validate the
Layer-2 config, create the run directory, kick off decomposition, walk the stages, enforce the stop
conditions, and hand the result to the human. That agent is not "dispatched", so B excludes it by
definition; and it is procedure, so A excludes it by rule.

This is not a hypothetical omission — in both source skills it is a large, explicitly-named section:

- `Guarded_change/SKILL.md:25–52` — "## Loop": create `changes/<slug>/`, produce one doc per stage,
  append to `decisions.md` at every gate, the stage table, the iteration cap.
- `Dragonfly/SKILL.md:29–70` — "## Loop": create `hunts/<slug>/`, maintain the ledgers as files,
  the stage table, the incidental-findings rule.

A's enumerated `SKILL.md` contents (split-round-1.md:52–56) are frontmatter, inputs, the stage/role
index table, stop-for-human, and the self-check note. **The Loop is absent from the list.**

The same rule also contradicts itself inside A: A is told to write `METHODOLOGY.md`'s "**the method
in prose**" (:59) while "restat[ing] no procedure" (:78). One of those has to give, and which one
gives determines whether the run's control flow exists anywhere in the merged plan.

### F3 — `major` — The joint that justifies the cut is factually false about the source material.

The seam's whole claim to be a real joint rather than an arbitrary bisection is:

> "Above the cut, files are read **once, by the invoking agent**… Below the cut, files are read
> **verbatim, mid-run, by cold dispatched agents** who have no other context" (:122–125).

In the two skills named as the house shape, `stages/` files are **predominantly the invoking
agent's own procedure**, addressed to it in the imperative:

- `Guarded_change/stages/stage-1.md:8` — "Write `1-spec.md`: the problem, why, constraints…"
- `Guarded_change/stages/stage-2.md:8` — "Write `2-plan.md`: how, **plus** measurement…"
- `Guarded_change/stages/stage-5.md:7` — "Implement per the plan, including any instrumentation…"
- `Dragonfly/stages/stage-7.md:6` — "at stage 7 **you spawn a cold reviewer directly**"
- `Dragonfly/METHODOLOGY.md:97` — Layer 1 is "**this doc + the skill + the stage files**", i.e. the
  stage files sit in the agnostic core beside `METHODOLOGY.md` and `SKILL.md`, not in a separate
  dispatched-prompt category.

Exactly one file in each skill is a cold-agent prompt — `stages/charter.md` — and even it is not
dispatched standalone; the invoking agent reads it *into* a dispatch from stage 3/6
(`Guarded_change/stages/stage-3.md:6,15`; `Guarded_change/stages/charter.md:3–5` "Stage 3 and stage
6 both read it, then add their stage-specific bullets").

Data-Distiller is genuinely more multi-agent than either sibling, so more of its `stages/` files
will be dispatched — but not all of them, and the root/invoking agent's file is precisely the
counterexample. Since B's **scope is defined by this reader claim**, a false claim mis-scopes B,
which is the mechanism that orphans F2's remainder. The cut may still be the right cut; the stated
reason for it is not the reason.

### F4 — `major` — Restart/resume and the concurrency ceiling are single rules split across both halves — the divider's own stated disqualifier.

The division rejects the alternative cut because it "splits **single rules across both halves**…
neither half can state the rule completely" (:158–163). The proposed cut does this twice:

| Rule | A holds | B holds |
|---|---|---|
| Restart/resume | "what a completed vs. in-progress unit looks like on disk, and **how a restarted run decides what to redo and what to trust**" (:66–67) | node "**resumes from on-disk state**" (:103) |
| Concurrency ceiling | "the **concurrency-ceiling semantics**" (:75) | node "**enforces the concurrency ceiling**" (:103) |

"How a restarted run decides what to redo and what to trust" is not a schema — it is the decision
procedure the node role executes, which A is explicitly forbidden to write (:77–78). Either A
writes procedure (violating its own rule) or A writes a layout with no decision rule and B writes a
decision rule against a layout it cannot see (F1 again).

Restart-and-resume is one of the eight defining properties in the task statement, so this is
load-bearing, not cosmetic.

### F5 — `major` — Nothing owns the run's terminal, human-facing output.

Generative sweep result. The blind roll-up means **no coordinating node may ever read findings**, so
the top of the tree is structurally incapable of authoring the distilled result. Yet:

- B's merge role is stated per-item — "rank surviving findings by how many independent analysts
  agreed" (:104–105) — with no statement of whether merge runs once per item, or recursively to the
  root, or once at the end.
- A owns only the artifact **layout** — "what a run produces (the on-disk artifact layout)" (:60),
  "the run directory, per-item and per-node directories and filenames" (:66) — i.e. A can name a
  path for a final report but cannot name its producer, because producers are procedure.
- The seam's five contract items (:130–134) do not include *which role emits the run's final
  findings document, at what level of the tree, and where it lands*.

This is the "portion each half assumes the other owns" failure applied to the skill's **entire
deliverable**: the source-cited factual findings the user actually asked for. A merged plan can
satisfy both sub-tasks as written and still produce a skill that computes findings and never hands
them over.

### F6 — `minor` — A's `METHODOLOGY.md` section list does not in fact match the sibling section shape it claims to match.

A claims its `METHODOLOGY.md` sections "Match the section shape of `Guarded_change/METHODOLOGY.md`
and `Dragonfly/METHODOLOGY.md`" (:60–61) and lists: why it exists / the method in prose / the
stage-role index / the two layers / the config contract / what a run produces.

Both siblings additionally carry **"## Human-in-the-loop"** — `Guarded_change/METHODOLOGY.md:198`,
`Dragonfly/METHODOLOGY.md:172` — and Dragonfly carries **"## Trigger"** (`:161`). Human-in-the-loop
is where the owner's role and the enforceability split are stated; for a skill whose findings are
meant to be trustworthy, who may accept an unverifiable finding is not a decorative section.

### F7 — `minor` — A's item 4 names no file, duplicates item 2, and inflates the floor-check count.

A's list is headed "**Files** this half plans (each step: one file, with the content that goes in it
specified)" (:50). Item 4 (:66–67) is "The on-disk run-state layout and restart/resume semantics" —
a topic, not a file — and it overlaps item 2's "**what a run produces** (the on-disk artifact
layout)" (:60). Two planners will resolve this differently: one folds it into `METHODOLOGY.md`, the
other creates a `RUN-STATE.md` that exists in neither sibling, and `Union` keeps both.

Consequently the floor check's "A is ~5 files" (:168) over-counts; A is four. **This does not change
the floor verdict** — see the floor section below.

### F8 — `minor` — A stronger alternative cut was not considered.

The division weighs exactly one alternative (:152–163), and it is a weak one (cutting *at* the
blind-roll-up barrier, which does split a two-role rule). Unconsidered, and better on three counts:

> **Half 1 — orchestration + frame:** `SKILL.md`, `METHODOLOGY.md`, the config template, the
> run-state layout, and the node / blind-roll-up role, including concurrency and resume.
> **Half 2 — the finding pipeline:** the common core, decompose-and-size, analyst, verify, merge.

It cures F4 (resume, ceiling and the node procedure sit together), shrinks F1's contract from
"the whole vocabulary" to config keys plus output paths (every finding-schema decision lands in half
2, whose roles are the only ones that touch findings), and cures F2 (the invoking agent's loop and
the root node are unambiguously in half 1). It is not obviously correct and I am not asserting it is
the right cut — but it is on the table and was not weighed, and I am the last reader who sees the
alternatives.

---

## The floor — no finding

**Neither half falls below the granularity floor**, so the floor is not grounds against this
division. A is four to five files (see F7); B is six. Both remain coherent whole tasks well above
"one file created, with the content that goes in it specified", and both could divide again. The
division's own floor check (:166–169) reaches the right verdict, on a slightly wrong count.

The task is **not** indivisible.

---

## Lens verdicts

**1. Factual — issues found: F3, F6** (and the citations under F2). Source evidence consulted:
`Guarded_change/SKILL.md` (frontmatter, Inputs, Loop, Stop-for-human, Self-check),
`Guarded_change/METHODOLOGY.md` (section headings; "What a run produces" body),
`Guarded_change/README.md` (headings), `Guarded_change/guarded-change.companion.md` (headings),
`Guarded_change/stages/` (charter + stage-1/2/3/5 openings, full file list),
`Dragonfly/SKILL.md`, `Dragonfly/METHODOLOGY.md` (headings; "The two layers"; "The config
contract"), `Dragonfly/README.md`, `Dragonfly/dragonfly.companion.md`, `Dragonfly/stages/`
(stage-2, stage-7 openings, full file list). **Verified true:** both siblings carry a `README.md`
(:68); both carry `SKILL.md` + `METHODOLOGY.md` + `stages/` + a per-project config file, and the
frontmatter carries `name` and `description` (`Guarded_change/SKILL.md:1–4`,
`Dragonfly/SKILL.md:1–4`); both `SKILL.md` files carry a stage index table with a path per row and a
stop-for-human section and a self-check/dogfooding section, as A claims (:52–56). **Not verified:**
the seam's reader claim (F3) and the METHODOLOGY section-shape claim (F6).

**2. Logical — issues found: F1, F7.** The reasoning defect is a sequencing assumption (A completes
and informs B) imposed on a structure that runs the halves concurrently and merges without
reconciling.

**3. Missed opportunity — issue found: F8.**

**4. Unstated assumptions & risks — issues found: F1, F5.** The two unstated assumptions are (a)
that a producer→consumer ordering exists between the halves, and (b) that some role, somewhere,
assembles and emits the final result.

**5. Fidelity — issues found: F4** (and F3). Loaded terms pinned to concrete mechanisms:
*cold agent* → B's common-core file, verbatim-included (:93–96) — pinned;
*decompose* → B's decompose-and-size file, producing a sized item list plus a per-item strategy
(:97) — pinned; *N independent analysts* → B's analyst file, with `N` a Layer-2 config key owned by
A (:63, :98–99) — pinned, though it crosses the seam (F1);
*verify* → B's verify file: re-check every citation, drop the unverifiable (:100) — pinned to the
mechanism, not a proxy; *agreement ranking* → A's finding-record `agreement count` field plus B's
merge role (:74, :104) — pinned; *blind roll-up* → A's terse per-child status schema as the sole
channel, plus B's node procedure of never opening findings files (:73, :102–103, :132) — pinned to
the mechanism rather than to a promise, and both acting roles land in B, which is the division's
genuine strength; *read-only* and *facts-not-interpretation* → B's common core (:94–96) — pinned;
*restart and resume* → **not cleanly pinned**, split between A's layout and B's node (F4).

**6. Completeness — issues found: F2, F5.** The **generative sweep was run**. Against the structure's
own required parts (the two sub-task statements, the seam's produces/consumes/assumes/neither-owns
quadrants, the joint justification, the floor check) nothing is formally missing — all are present.
The sweep then asked what load-bearing section that list does not anticipate, looking specifically
for: (a) an actor with no owner — found, the invoking agent (F2); (b) an output with no producer —
found, the terminal findings document (F5); (c) a rule with two actors on opposite sides — found,
resume and the ceiling (F4); (d) a failure mode with no home — partially covered, A holds
stop-for-human, but "an item that cannot be sized", "verification drops everything", and "an analyst
returns nothing" have no stated owner and I did not file separately since they are plan-level;
(e) an install/live-copy story — covered by A (:68–69); (f) a run directory location — covered by A
(:66).

**Any portion of the task left unaddressed:** yes — see F2 (the run's control flow) and F5 (the
deliverable).

---

## Summary of findings by severity

| # | Severity | Finding |
|---|---|---|
| F1 | **blocker** | The A→B contract has no delivery channel; B's half cannot be planned at the floor, or produces a colliding vocabulary that `Union` preserves. |
| F2 | **blocker** | The invoking agent's run procedure (the sibling `SKILL.md` "Loop") is owned by neither half. |
| F3 | **major** | The reader-based joint that justifies the cut and scopes B is factually false about `Guarded_change/stages/` and `Dragonfly/stages/`. |
| F4 | **major** | Restart/resume and the concurrency ceiling are single rules split across the halves — the divider's own stated disqualifier. |
| F5 | **major** | No half owns the role that emits the run's final human-facing findings document. |
| F6 | `minor` | A's `METHODOLOGY.md` section list omits "Human-in-the-loop" (both siblings) and "Trigger" (Dragonfly). |
| F7 | `minor` | A's item 4 names no file, duplicates item 2, and inflates the "~5 files" count. |
| F8 | `minor` | A stronger alternative cut (orchestration+frame vs. finding pipeline) was never weighed. |
