# Split review — round 2, reviewer C

Reviewing the proposed division in
`Architect/runs/data-distiller/it2/0/split-round-2.md` against the task and the granularity floor
quoted at its head.

**Inputs received and usable.** No missing or dead paths. I opened
`/home/zero/Desktop/claude-code-skills/Guarded_change/` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/` to check the division's factual claims, and
`~/.claude/skills/` to check the install-collision claim. I did not open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`, and there is no plan; I did not look for
one.

**Overall:** the cut is a real joint and I would not call this task indivisible. Both halves are
comfortably above the floor. The defects are all in the **seam**, not in the choice of joint:
three of them are load-bearing.

---

## Findings

### F1 — Resume-from-disk is split so that the enforcing half belongs to nobody — `major`

*(coverage; unstated assumptions)*

"Restart and resume from on-disk state" is one of the eight defining properties the task
enumerates (`split-round-2.md:26`). The division assigns two pieces of it and leaves out the
third:

- **S5** (`:175–178`): "A publishes, per stage, the on-disk marker that means 'this unit is
  finished and need not be re-run'." — A produces the marker vocabulary.
- **S5** again: "B writes the router's top-level resume paragraph … **A does not write the resume
  paragraph.**" — B writes the top-level prose.

Nobody is assigned the instruction that **consults** a marker: the line in a stage file that tells
a coordinating node, on restart, to check each child's marker and skip the finished ones before
spawning. That instruction is a prompt an agent executes, so **S8** (`:201–202`) puts it out of B's
reach by construction — "B writes no prompt any agent executes." And A's in-scope list (`:67–93`)
never mentions it: the coordinating-node bullet (`:82–84`) covers driving children, blindness,
concurrency and rolling status upward, and the only failure-handling bullet (`:91–93`) is about
*failure and retry* — "when an analyst returns nothing, when verification drops every citation" —
which is a different contingency from *this node already ran and half its children are done*.

**Failure scenario.** A plans seven stage files, each declaring its completion marker as S5
requires. B writes `SKILL.md`'s top-level resume paragraph against that list, as S5 requires. A run
is interrupted after two of five items complete. On re-invocation the router correctly identifies
the run folder and hands control to the coordinating-node stage — whose file contains no
instruction to read markers, because writing one was neither in A's scope nor permitted in B's. The
node re-spawns all five items. Both halves executed their sub-task exactly as specified and the
skill has no working resume.

**Remedy that stays inside the cut:** add to A's scope, explicitly, the check-marker-before-spawn
rule (it is A's by S8's own logic — it is a prompt), and reword S5 so the asymmetry is stated:
A owns markers *and their consultation*; B owns only the human-facing account of what resume does.

---

### F2 — S6 freezes a run-directory skeleton with no slot for two artifacts A is required to plan, and no channel to change it — `major`

*(logical; seam soundness)*

S6 (`:180–191`) fixes the run-directory skeleton unilaterally, deliberately, "so that S2's
one-directional flow is not spoiled by B owning a layout A must write into," and closes it: "Neither
may change its shape unilaterally." The skeleton is exactly three things: `runs/<run-slug>/`,
`runs/<run-slug>/items/<item-id>/`, and an append-only run log at the run folder's root.

Two artifacts A is required to plan have no place in it.

1. **The corpus-level deliverable.** A's terminal roll-up bullet (`:86–90`) requires A to decide
   "whether the corpus-level result is assembled from findings or is a manifest over them." Either
   answer produces a corpus-level artifact. The skeleton has a per-item folder and a log; it has no
   named location for a run-level result. A can improvise one at the run-folder root, but S6 says A
   only "names files inside this skeleton," and B is documenting "what a run produces" from the
   skeleton it was handed — so B's `METHODOLOGY.md` will document a run layout that omits the
   run's actual output.

2. **Intermediate node state.** A's coordinating-node bullet (`:82–84`) describes a node that
   "drives its children" and "rolls status upward" — i.e. a tree of nodes, potentially more than one
   level deep, which is the only reason the roll-up needs to be *rolled*. A flat
   `items/<item-id>/` gives an intermediate node nowhere to record its child list, its rolled-up
   status, or (per F1) its own completion marker. This is not hypothetical: it is the same structure
   that makes the blindness rule non-trivial, since a node reading terse child statuses must have
   somewhere to read them from.

**Why the freeze makes it worse rather than better.** The layout is a *consequence* of the method,
and the method is entirely A's — the division says so itself (`:89–90`: "it is a question about the
method, and the method is entirely A's"). S6 inverts that for the one structural decision the
method most constrains. And the escape hatch is illusory: "neither may change its shape
unilaterally" implies a bilateral change, but S2 (`:160–162`) states "Nothing flows B → A" and
"There is no negotiation to arbitrate," and B is planned after A. There is no bilateral channel.
So A, on discovering the skeleton cannot hold its artifacts, has no stated recourse.

**Remedy:** either (a) demote S6 to a *minimum* skeleton A may extend but not contradict, with the
extension published to B as a fourth declaration; or (b) keep the freeze and widen it now to
include a run-level deliverable slot and a node-state slot. (a) is the one that preserves S2.

---

### F3 — The seam's three declarations have no named carrier: "A publishes" is pinned to nothing — `major`

*(fidelity; completeness)*

The whole seam is three declarations (S3 stage index, S4 config keys, S5 completion markers), each
phrased as "A publishes …" and "B consumes exactly those and nothing else" (`:52–53`). **No
location, artifact, or format is named for any of them.** There is no `declarations.md`, no
required section of A's plan, nothing.

This is not a stylistic gap. S3 (`:168`) says B "does not open A's files to write" the stage-index
tables. That instruction is unexecutable as written unless B has some *other* thing to read. Two
readings, both bad:

- **B reads A's plan document.** Then S3's restriction does no work at all — the plan is where the
  content of A's files is specified, so B is reading A's files' content by another name, and the
  claimed information-hiding is nominal. It also means B must extract three different declaration
  types from a document not required to segregate them, with no guarantee they are consolidated or
  complete. A plan can fully specify seven stage files and never once emit an *index-grade line*
  in S3's calibrated sense.
- **B reads a separate declarations artifact.** Then that artifact is a required output of A that
  A's scope section (`:61–106`) never asks for. A will not produce it.

The aiming file treats an unstated seam as at least `major` because everything below the cut
inherits it. Here the seam's *content* is stated well — S3's calibration against
`Guarded_change/METHODOLOGY.md:73` is genuinely good and I verified that line reads exactly
"checkable, labeled accept bar; position/concurrency criteria; self-check criteria" — but its
*carrier* is absent, and the carrier is what makes a one-directional seam mechanical rather than
aspirational.

**Remedy:** name the artifact and make it a required output of sub-task A — e.g. A's plan ends with
a `Declarations` section containing three labelled tables (stage index, config keys, completion
markers), and B's sub-task states that this section is B's sole input from A.

---

### F4 — `Guarded_change/stages/charter.md` is mis-cited as the example of "the common core every dispatched agent reads" — `minor`

*(factual)*

A's first in-scope bullet (`:69–71`) is "The common core every dispatched agent reads first," and
the source pointer A is handed for it (`:103–105`) is "`Guarded_change/stages/`
(`charter.md` as the **shared-core example**)."

`charter.md` is not that, in either sibling. Its own first line is `# The red-team charter (shared
by stages 3 and 6)` (`Guarded_change/stages/charter.md:1`), and line 3 says "Stage 3 and stage 6
both read it." `Guarded_change/METHODOLOGY.md:83` confirms it is "shared by stages 3 and 6 in
`stages/charter.md`," and `SKILL.md:40,43` are the only two stage rows that cite it. Dragonfly's is
the same pattern with a different subset: `# The red-team charter (shared by stages 1, 4, 7)`
(`Dragonfly/stages/charter.md:1`), confirmed by `Dragonfly/METHODOLOGY.md:89` ("shared by stages
1/4/7"). A grep for `charter.md` across both skills' stage files returns hits only from those
stages.

So it is a **shared role file for one role that spans several stages** — not a core every dispatched
agent reads. Neither sibling has the latter. A pointed at `charter.md` as the model for an all-agent
core will find a red-team charter and is likely to inherit red-team-shaped material (five lenses,
severity model, provenance) into Data-Distiller's analyst/verifier/merge core, where most of it does
not apply.

**Remedy:** relabel the pointer honestly — "the nearest sibling analogue is the red-team charter,
shared by a *subset* of stages; no sibling ships a core read by every dispatched agent, so A is
designing this without a worked example." That is a materially different instruction and it is
fixable in one edit.

---

### F5 — S1's "the partition is by path, and it is mechanically checkable" has three cases it cannot decide — `minor`

*(completeness; logical)*

S1 (`:156–158`) claims a total partition: A owns everything under `Data-Distiller-impl/stages/`, B
owns everything at the top level of `Data-Distiller-impl/`, "a path decides which half owns it." It
is not total:

- **A third subdirectory.** `Data-Distiller-impl/templates/`, `examples/`, or any other directory a
  planner might reasonably want is neither top-level nor under `stages/`. Since A is planned first
  and A's scope is bounded to `stages/`, such a path falls to nobody by the stated rule.
- **The installed copy.** B's install step (`:134–140`) produces files at
  `~/.claude/skills/<name>/`, outside both regions. B plainly owns it — the scope prose says so —
  but S1's rule does not reach it, so the "mechanically checkable" claim is overstated.
- **`runs/`** — see F6.

**Remedy (one line):** restate S1 as a default rather than an enumeration — "any path under
`stages/` is A's; **any other path in or produced by the build is B's**" — which decides all three
cases and keeps the mechanical check.

---

### F6 — S6 never says where `runs/` is rooted — `minor`

*(unstated assumptions)*

S6 derives the skeleton from the siblings' `changes/<slug>/` (`Guarded_change/SKILL.md:27`, which I
verified reads "Create a change folder `changes/<slug>/`") and `hunts/<slug>/`
(`Dragonfly/SKILL.md:31`, verified: "Create a hunt folder `hunts/<slug>/`"). Both citations are
accurate. But in both siblings those folders sit **inside the skill's own source directory** — I
confirmed `Guarded_change/changes/` and `Dragonfly/changes/` both exist on disk.

Data-Distiller differs in a way that makes inheriting that silently wrong: it is corpus-agnostic, it
is installed to `~/.claude/skills/<name>/` (B's install step), and it runs against an arbitrary
corpus elsewhere. Writing run state into the installed skill directory would mean every run mutates
the installed skill, and reinstalling would collide with run history. The division does not state
whether `runs/` is rooted at the skill directory, the working directory, or the corpus. B documents
the layout and points the router at it; A writes files into it. Both need the answer and neither is
given it.

**Remedy:** state the rooting in S6 alongside the shape, since S6 already claims to fix the layout
so neither half must decide it.

---

### F7 — One-directional seam with no re-sync rule, against a stage list the division itself calls open — `minor`

*(logical; unstated assumptions)*

S2 orders A first and forbids B → A flow. The division then states, in its floor argument
(`:230–231`), that "the number and boundaries of those files are themselves still open." B's
`SKILL.md` and `METHODOLOGY.md` stage-index tables (`:121`, `:125`) are written from A's published
index. If A's plan is subsequently revised — by its own reviewers, by a further split of A, or by a
bounce — B's tables silently go stale, and S2's "no negotiation to arbitrate" means there is no
stated path back.

This is the ordinary cost of a one-directional seam and I do not think it invalidates the choice.
But the division nowhere states the obligation it creates: *if A's declarations change after B is
planned, B's dependent sections are re-derived.* One sentence closes it.

---

### F8 — Two small internal inconsistencies in the seam's own key-ownership rule — `nitpick`

*(logical)*

- S4 (`:171–174`) says "A publishes every Layer-2 key its stage files read … B may add keys the
  router itself needs." But B's scope (`:130–133`) pre-declares four keys "at minimum," including
  **"the analyst count N."** N is read by A's analyst stage, not by the router, so under S4 it is
  A's to declare and B's list pre-empts it. Harmless in effect (the contract must contain A's keys
  anyway), but it is the seam contradicting itself in the same document. Note the other three
  come from the task's own text (`:24–25`) and are fine.
- S7 (`:194`) says "B's contract **declares** the ceiling key," using the same verb S4 reserves for
  A's side of the seam. Reword one of them.

---

## Lens verdicts

**1. Factual — one issue (F4).**
Earned: I opened `Guarded_change/{SKILL.md, METHODOLOGY.md, stages/charter.md}` and
`Dragonfly/{SKILL.md, METHODOLOGY.md, stages/charter.md}`, listed both skill directories and both
`stages/` directories, and grepped both trees for `charter.md`. Verified **correct**: the
`METHODOLOGY.md:8–11` quotation is verbatim (line 11 reads exactly "This file is opened for
orientation and config setup — not to run a stage."), quoted twice and accurately both times;
`SKILL.md:1–4` is the frontmatter, `:13–24` Inputs, `:26–52` the loop/stage-index, `:54–73`
Stop-for-human; `METHODOLOGY.md:67–84` is the stage index, `:88–101` the two layers, `:103–151` the
config contract, `:154–196` what a run produces; `METHODOLOGY.md:73` reads exactly as quoted;
`Guarded_change/SKILL.md:27` and `Dragonfly/SKILL.md:31` say what is claimed; both siblings ship a
`README.md` and a top-level `*.companion.md`, so the claims at `:127–128` and `:130–131` hold.
Verified **correct and load-bearing**: the install-collision claim at `:137–140` — `ls
~/.claude/skills/` returns `data-distiller`, `dragonfly`, `guarded-change`, so a naive copy would
indeed destroy an existing directory. That is a good catch by the divider and I confirmed it
without reading inside `Data-Distiller/`. Only F4 fails.

**2. Logical — issues (F2, F5, F7, F8).**
The A-first ordering follows soundly from the one-directional flow. The failure is internal
consistency of the seam: S6 freezes a layout that A's own required decisions overflow while
removing the channel to fix it (F2); S1's partition is claimed total and is not (F5); the seam
states no re-sync obligation (F7) and contradicts itself twice on key ownership (F8).

**3. Missed opportunity — no issue.**
I considered two alternatives and reject both. *Cut by pipeline layer* (per-item pipeline vs.
corpus-level orchestration + package) would put the blindness invariant on the seam, splitting the
node from the merge that defines the terse status it reads — strictly worse than S8, which keeps
both in one half. *Cut method vs. everything-else* is the same cut with a vaguer boundary. I also
weighed the halves' obvious asymmetry — A carries seven-plus files and at least two open design
questions (`:86–90`, `:95–97`) against B's four documents and one (`:137`) — and concluded it is not
a defect: the joint is real regardless of load, both halves clear the floor, and if A is re-split
later the audience line still holds beneath it. Not filed.

**4. Unstated assumptions & risks — issues (F1, F6, F7).**
The largest is F1: the division assumes resume falls out of "markers published" plus "resume
paragraph written," and the enforcing instruction between them is assumed rather than assigned.
F6 assumes the siblings' run-folder rooting transfers to an installed, corpus-agnostic skill.

**5. Fidelity — one issue (F3).**
Terms pinned. **"Division"** → two sub-tasks, each a coherent whole task, plus a stated interface;
implemented at `:61–107` and `:154–207`. **"Seam"** → nine numbered clauses covering partition,
direction, three declarations, shared skeleton, and unowned residue; concrete, not a gesture.
**"Above the floor"** → pinned to the floor's own words: "one file created … with the content that
goes in it specified," and argued at `:226–235` by showing each half must still *decide* content
across multiple files. Correctly applied. **"Blind roll-up"** → pinned at S8 to an authorship
containment (rule-writer and status-definer in the same half) rather than a runtime check; that is
the right mechanism for a *division* to guarantee, since a division cannot enforce runtime behaviour.
**"Coordinating agent"** → deliberately left unpinned and assigned to A (`:95–97`); legitimate,
because it is a method question and A owns the method. The failure is **"publishes"** (S3/S4/S5):
used as the seam's load-bearing verb and pinned to no artifact, location or format — the proxy is
"A will have written it down somewhere," which is not the mechanism the one-directional seam needs.
Hence F3.

**6. Completeness — issues (F3, F5).**
Checklist floor: the structure's required parts are all present — both sub-tasks scoped with
explicit out-of-scope lists, source material named per half, the seam, a real-joint argument, a
floor argument, and an explicit statement of what neither half owns (S9). That is more complete than
the four questions demand.
**Generative sweep, run.** I asked what load-bearing section the four questions do not anticipate,
and looked specifically for: (a) a carrier artifact for the seam's declarations — **missing, F3**;
(b) a residue rule for paths neither region names — **missing, F5**; (c) an ordering statement —
present (S2); (d) a re-sync rule if the first-planned half changes — **missing, F7**; (e) a slot in
the frozen skeleton for each artifact the halves must produce — **missing, F2**; (f) an owner for
each of the task's eight enumerated defining properties — seven are cleanly owned, resume is
**not, F1**; (g) an explicit unowned-residue statement — present (S9), and it correctly parks the
corpus, the build location and the off-limits directory.

**Task portions left unaddressed:** none by the division as a whole. All eight defining properties
appear on one side or the other; the coverage defect is F1's *within*-property split, not an omitted
property.

---

## Summary of severities

| # | Finding | Severity |
|---|---|---|
| F1 | Resume: marker-consulting instruction assigned to neither half | **major** |
| F2 | Frozen run-directory skeleton lacks slots A needs; no channel to change it | **major** |
| F3 | The seam's three declarations have no carrier artifact | **major** |
| F4 | `charter.md` mis-cited as the all-dispatched-agent common core | minor |
| F5 | By-path partition is not total (third subdir, installed copy, `runs/`) | minor |
| F6 | `runs/` rooting unstated | minor |
| F7 | No re-sync rule if A's declarations change after B is planned | minor |
| F8 | S4/S7 internal inconsistency on who declares a config key | nitpick |

**On the four questions:** *Coverage* — one defect (F1), otherwise total. *The seam* — stated in
unusual detail, but unsound in three places (F1, F2, F3). *The floor* — no issue; both halves are
clearly above it and the argument at `:226–235` is correct. *Real joint* — no issue; the four
differentiators at `:211–224` are genuine, the audience line is the source material's own
(`Guarded_change/METHODOLOGY.md:11`, verified verbatim), and the cut is not a bisection for
symmetry.

**Unchecked:** whether A's seven-file stage list is the right decomposition of the method — that is
A's planning work, not the division's, and I did not judge it. I could not check anything against
`Data-Distiller/`, which is off limits to me as it is to both halves.
