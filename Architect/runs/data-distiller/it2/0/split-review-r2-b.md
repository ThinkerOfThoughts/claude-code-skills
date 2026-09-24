# Split review — round 2, reviewer B

Reviewing the proposed division in
`Architect/runs/data-distiller/it2/0/split-round-2.md` (all `split-round-2.md:N` citations below
refer to that file).

**Inputs I had:** the proposed division, the task verbatim, the granularity floor verbatim, and
the source material (`Guarded_change/`, `Dragonfly/`). No plan, as expected. I did not open
`Data-Distiller/`. Nothing was missing from my inputs.

**Bottom line:** the cut is a *real joint* and I endorse the axis. Three of the four differences
it names at the boundary hold up against the source. It fails on the seam's contents, not on the
axis: one artifact the seam freezes is structurally incompatible with the task, the A→B
declaration set is narrower than B's own stated scope requires, and the seam's argument that the
blindness invariant cannot cross the cut rests on a claim the source material contradicts.

---

## Findings

### F1 — `blocker` — S6 freezes a flat, two-level run skeleton that cannot hold the recursive decomposition the task requires, and forbids either half from fixing it

S6 (`split-round-2.md:185–188`) fixes the run-directory skeleton as exactly two levels:

> - `runs/<run-slug>/` — one folder per distillation run;
> - `runs/<run-slug>/items/<item-id>/` — one folder per analyzable item, holding that item's
>   findings artifact and status;
> - an append-only run log at the run folder's root.

and closes with **"Neither may change its shape unilaterally"** (`:191`).

But the task and the division's own A-scope both describe a structure of arbitrary depth:

- the task: *"pick a per-item strategy when an item does not fit"*, and *"a coordinating agent
  never reads the findings themselves, only a terse **per-child** status"* — a **roll-up**
  (`split-round-2.md:20`, `:22`);
- A's scope: *"the rule that picks and **executes** a strategy when an item does not fit in one
  pass"* (`:73–75`), and *"How a node drives **its children** … and rolls status **upward**"*
  (`:83–84`). "Upward" is only meaningful at depth ≥ 2.

A flat `items/<item-id>/` has no location for an intermediate node — neither its own status, nor
the mapping from it to its children.

**Failure scenario.** Decomposition sizes item `I7`, finds it does not fit, and A's over-size
strategy splits it into `I7a`, `I7b`, `I7c` under a coordinating node. That node must (a) record
its own completion marker for S5, (b) record the child→parent mapping so status can roll upward,
and (c) survive a restart. The skeleton offers only sibling folders under `items/`, so on resume
the router can see that `I7a`–`I7c` are complete but has nowhere to learn that `I7` is their
parent, that `I7`'s own merge has not run, or that `I7` ever existed as a unit. The obvious repair
— add a level, or nest sub-items — is precisely what S6 forbids to both halves.

This compounds with B's resume text, which is written in linear terms: *"read the run log and
continue from the first incomplete unit"* (`:121–122`). In a tree with a concurrency ceiling there
is no "first incomplete unit"; there is a frontier of ready units, and readiness depends on
parent/child relations the skeleton does not record.

**Remedy is not mine to specify**, but note it is not a one-clause fix: the run-state model is the
thing S6 was written to freeze, and both halves depend on it.

### F2 — `major` — the declared A→B interface (S3/S4/S5) is narrower than B's assigned scope, and S2 provides no back-channel

S2 (`:160–162`) makes the flow strictly one-directional — *"Nothing flows B → A … There is no
negotiation to arbitrate"* — and S3/S4/S5 declare exactly three things A hands B: the stage index,
the config keys, the completion markers. B's own in-scope list requires at least four more things
that only A knows:

1. **The run-log line schema.** B must write *"read the run log and continue from the first
   incomplete unit"* (`:121–122`) and document the run in `METHODOLOGY.md` (`:125–127`). S6 says
   *"A names files inside this skeleton and states what each contains"* (`:190`) — so the run
   log's format is A's. It is not among the three declarations. B either invents a schema A will
   not write, or opens A's files, which S3 explicitly forbids (*"does not open A's files"*, `:168`).
2. **The artifact list.** B's `METHODOLOGY.md` must cover *"what a run produces — the
   run-directory layout, **the artifacts**, and the run-level outcome states"* (`:125–127`), while
   B's out-of-scope list puts *"the findings-artifact format"* on A's side (`:143–144`). This is a
   contradiction inside B's own scope with no declaration bridging it. The sibling this is modelled
   on is the concrete counter-example: `Guarded_change/METHODOLOGY.md:154–196` enumerates every
   artifact file by name and one-line content — content that, under this cut, lives only in A.
3. **Run-level outcome states.** B must document them (`:127`); A owns *"permitted status values
   plus a retry/abandon rule"* per stage (`:93`). Undeclared.
4. **The terminal-roll-up resolution.** The division hands A an explicitly open design question —
   *"whether the corpus-level result is assembled from findings or is a manifest over them"*
   (`:88–89`) — and defends it as *"an open design question A must resolve, not a gap in the cut"*
   (`:89`). That defence only holds if the resolution stays inside A. It does not: the answer
   *is* what `METHODOLOGY.md`'s "what a run produces" must state, and what `SKILL.md` must route to.
   S3's channel is a per-file *index-grade line*, calibrated against
   `Guarded_change/METHODOLOGY.md:73` (which I verified reads exactly *"checkable, labeled accept
   bar; position/concurrency criteria; self-check criteria"*). A line at that grain does not carry
   "the corpus-level deliverable is a manifest, not a synthesis."

**Failure scenario.** A resolves the roll-up as a manifest and defines a run log of one line per
item transition. B, planned afterward against three declarations that mention none of this, writes
a `METHODOLOGY.md` describing a synthesized corpus-level report and a resume rule that scans
`items/*/` for a status file. Both halves are internally consistent, both conform to the seam as
written, and the assembled skill has a router that cannot resume and a reference spec that
describes a deliverable the method does not produce. Because S2 forbids B→A flow and names no
arbitration, nothing in the division detects this.

### F3 — `major` — S8's ground is false: `SKILL.md` **is** executed, by the topmost coordinating agent, so B can weaken the blindness invariant

S8 (`:198–202`) argues the blindness rule cannot be widened across the seam, concluding: *"B does
not formulate the rule and **cannot weaken it, because B writes no prompt any agent executes**."*

The source material contradicts the premise. `Guarded_change/SKILL.md:25–32` is imperative
instruction to the invoking session:

> Create a change folder `changes/<slug>/` and produce one doc per stage … At every **gate (stages
> 4, 7, 8)**, append a line to `decisions.md` … Walk the loop; **at each stage, read that stage's
> file for the full procedure + the rules it must apply:**

`SKILL.md` is executed; `METHODOLOGY.md` is not. The division's own supporting citation says only
the latter: `Guarded_change/METHODOLOGY.md:11` — *"This file is opened for orientation and config
setup — not to run a stage"* — where **"this file" is `METHODOLOGY.md`**. The same source, two
lines earlier, describes `SKILL.md` as *"the router that **walks the loop**"* (`METHODOLOGY.md:10`).
The division stretches a citation about one file to cover both (`:216–219`, and the "reader"
bullet at `:213–215`).

The consequence is not cosmetic. In a skill run, the **invoking session is the topmost
coordinating agent** — the one the task's blindness property most needs to bind — and B writes its
instructions: *"the run-start procedure; the **top-level resume instruction**"* (`:120–121`).

**Failure scenario.** A, exercising its right to name files inside the skeleton (S6, `:190`),
places each item's completion marker as a trailer inside that item's findings artifact. B, writing
the resume paragraph it owns, writes: *"on invocation, if a run folder exists, open each
`items/<id>/findings.md` and continue from the first without a completion trailer."* The invoking
session now reads findings before dispatching the next round of children — the exact steering the
blindness property exists to prevent — and every rule S8 relies on has been honoured: A authored
the invariant, B never touched a `stages/` file, the path partition (S1) is intact. Nothing in the
seam forbids it, because S8 assumed B's output is inert.

Note that I checked and am **not** filing the analogous objection to S7: *"the only spawn sites are
in A's files"* is supported by the siblings, where `SKILL.md` carries no spawn instruction and the
operative reviewer-spawn rule lives in the stage files (`Guarded_change/METHODOLOGY.md:79`;
`grep` for `spawn` over both `SKILL.md`s returns only references, no dispatch step). S7 stands.

### F4 — `minor` — the cut is real but low-yield: it separates the hard half from the easy half rather than dividing the hard half

Measured against the nearest analogue: `Guarded_change/stages/*.md` totals 68,889 bytes;
`SKILL.md` + `METHODOLOGY.md` + `README.md` + `guarded-change.companion.md` totals 37,295 — roughly
2:1 in A's favour by volume. On top of that, A holds every open question the division names (the
over-size strategy `:73–75`, the "coordinating" pin `:95–97`, the terminal roll-up `:88–90`),
while B's four documents have two complete worked examples each to derive from. B is close to a
leaf; A will need the same decomposition it needed before this cut.

A cut *inside* the method — e.g. the per-item pipeline (decompose/size/analyst/verify/merge)
against the tree, state and orchestration layer (node, roll-up, completion markers, resume) —
would have divided the hard part and would still have had a stateable seam (the per-item findings
artifact and status line). The division does not consider any alternative axis, so nothing
downstream will.

This does not make the chosen cut wrong; it is a real joint. It buys less than it appears to.

### F5 — `minor` — the run-directory skeleton's **root** is unspecified

S6 fixes the shape (`:185–188`) but not what `runs/` is relative to. The siblings root theirs at
the invoking session's CWD (`Guarded_change/SKILL.md:27`, `Dragonfly/SKILL.md:31` — both bare
relative paths), which is natural when the CWD is the project under change. Data-Distiller is
corpus-agnostic and runs against a read-only corpus that may be anywhere. "Where output goes" is
an explicit item of A's common core (`:69–70`) and "the run-directory layout" is an explicit item
of B's `METHODOLOGY.md` (`:126`) — so both halves will state it independently, on the one artifact
S6 exists to keep from diverging.

### F6 — `minor` — "one file per stage of the pipeline" imports a linear-loop frame; A's own list is half roles

`:67` scopes A as *"one file per stage of the pipeline, plus the shared core"*, and S3 asks A for a
*"stage index"*. But A's own enumeration mixes pipeline stages (decomposition, analyst,
verification, merge) with **agent roles** that recur at every level (*"The coordinating-node
stage"* `:83`, and the common core itself). The siblings' numbered `stage-0 … stage-9` shape comes
from a method one session walks in order; this method is a tree of concurrent agents. The division
leaves A free to choose its file boundaries (`:229–230`), which is right — but it has already fixed
B's table as a *stage* index, so the vocabulary is decided across the seam before the structure is.

### F7 — `minor` — neither half owns verification that the assembled, installed skill works

S9 enumerates what neither half owns (`:204–207`) and lists only the corpus, the build location,
and the off-limits directory. B owns *"Installation"* (`:134–140`) but is scoped to *how the built
skill reaches* `~/.claude/skills/<name>/`, with the collision refusal — not to checking that what
arrived is complete or triggers. The nearest source analogue treats this as a standing obligation:
`Guarded_change/SKILL.md:81–83` names *"live copy == source copy (`diff`); SKILL.md ↔
METHODOLOGY.md ↔ stage-file consistency on every rule stated in more than one place"* as self-check
criteria. This cut *creates* rules stated in more than one place by design (the blindness property
per S8, the concurrency ceiling per S7, the skeleton per S6), and assigns nobody to check them
against each other. I flag this at `minor` rather than higher because the task says "plan the
implementation" and does not name a verification step, so this may be out of scope by design — but
if so, S9 should say so, since S9 is the list a reader will trust.

### F8 — `nitpick` — one citation range starts one line late

`:147` cites `SKILL.md:26–52` as "router + stage index". The section heading `## Loop` is at
`Guarded_change/SKILL.md:25`; line 26 is blank. Every other line citation in the division checks
out exactly (see the factual verdict below).

---

## The six lenses

### 1. Factual — **issues found (F3, F8)**; the rest of the citation set verified clean

I opened the source material and checked every line citation the division makes. Verified
**accurate**: `Guarded_change/METHODOLOGY.md:8–11` (quote is verbatim, including *"This file is
opened for orientation and config setup — not to run a stage"*); `:73` (the calibration quote is
character-exact); `:67–84` (stage index section); `:88–101` (two layers); `:103–151` (config
contract); `:154–196` (what a run produces); `Guarded_change/SKILL.md:1–4` (frontmatter),
`:13–24` (inputs), `:54–73` (stop-for-human); `Dragonfly/SKILL.md:31` (*"Create a hunt folder
`hunts/<slug>/`"*).

Verified **true**, non-obviously: both siblings ship a `README.md` (`:128`); both ship a top-level
companion config (`guarded-change.companion.md`, `dragonfly.companion.md`, `:130–131`); and the
install-collision claim at `:137–140` is correct — `ls ~/.claude/skills/` returns
`data-distiller  dragonfly  guarded-change`, so a naive `cp -r` would indeed overwrite a live
artifact. That is a genuine catch and I want it recorded as verified rather than merely repeated.

The one factual defect is **F3**: `METHODOLOGY.md:11`'s "this file" refers to `METHODOLOGY.md`, and
the division applies it to `SKILL.md` too, contradicting `METHODOLOGY.md:10` and
`SKILL.md:25–32`. **F8** is a one-line range slip.

### 2. Logical — **issues found (F2, F6)**

The ordering argument (A first, then B) follows correctly from S2's one-directionality. The defect
is that one-directionality is asserted as sufficient without checking that the three declarations
carry everything B needs — they do not (F2) — and there is no arbitration path when they fall
short, which S2 presents as a feature. F6 is a smaller sequencing flaw: B's table vocabulary is
fixed before A decides whether its files are stages or roles.

### 3. Missed opportunity — **issue found (F4)**

The 2:1 volume asymmetry plus the concentration of every open question in A. No alternative axis is
considered anywhere in the document, and per my aiming file no later reviewer will see one.

### 4. Unstated assumptions & risks — **issues found (F1, F5)**

The load-bearing unstated assumption is that the corpus decomposition is **one level deep** — that
is what S6's skeleton encodes, against a task and an A-scope that both describe children, roll-up
and re-splitting of over-size items (F1). Secondary: that the run root is obvious (F5).

Two assumptions I checked and found **sound**: that the house shape's file inventory transfers
(verified against both siblings' directory listings), and that A's stage files are the only spawn
sites (S7 — verified, see the note under F3).

### 5. Fidelity — **one issue (F3); the remaining terms pin cleanly**

Pinning each loaded operational term to the concrete mechanism the division gives it:

| Term | Pinned to | Verdict |
|---|---|---|
| **divide / cut** | two scoped sub-tasks, each "plan every file under path P", plus a nine-clause seam | real mechanism, not a proxy |
| **seam** | S1 path partition + S3/S4/S5 named declarations + S6 frozen skeleton | real mechanism — but under-populated (F2) |
| **sub-task** | a whole planning job over a file set, not a fragment | sound |
| **granularity floor** | "one file with its content specified", applied only in the direction "would either half fall below it" | correctly aimed |
| **"coordinating agent"** (blindness) | **deliberately not pinned by the divider**; explicitly delegated to A (`:95–97`) | legitimate deferral — the term governs A's files. But its *consequences* cross the seam (F2 item 4), and the seam's protection of it is a proxy: S8 substitutes "B writes no prompt any agent executes" for "no coordinating agent reads findings", and the substitute is false (F3) |
| **verification** (the task's cold citation re-check) | A's verification stage (`:78–79`) | correctly placed, not conflated with review of the plan |

### 6. Completeness — **issue found (F7)**; generative sweep run

Required-structure check first: the division has the cut, both sub-tasks with in-scope and
out-of-scope lists, per-half source material, a nine-clause seam, a joint-not-bisection argument,
and a floor argument. Nothing structurally absent.

**Generative sweep** — I asked what load-bearing section a checklist of "two halves + a seam" would
not anticipate, and looked specifically for: an output/run-state **location** (→ F1, F5); a
**restart story** across the cut (→ F1, F2 item 1); a **failure mode** for the seam itself, i.e.
what happens when A's declarations turn out to be wrong or insufficient while B is being planned
(→ F2 — there is none, and S2 rules one out by design); a **verification** that the two halves
compose (→ F7); an **ordering/blocking contingency** — what B does if A halts unresolved on the
terminal-roll-up question (nothing states it; folded into F2 item 4 rather than filed separately);
and an **arbitration owner** for anything S9 forgot (S9 is a closed list with no catch-all — this
is why I raised F7's scope ambiguity against S9 specifically).

---

## The four questions

**1. Coverage.** All eight of the task's defining properties are assigned to exactly one half, and
I could not find a portion both halves assume the other owns *by path*. The remainder that is
orphaned is not a pipeline property but the connective tissue: the artifact list, the run-level
outcome states, the run-log schema (F2), and end-to-end verification (F7).

**2. The seam.** Stated, at unusual length and with a mechanically checkable partition — S1 is a
genuine strength and I want that recorded. It is nonetheless **unsound in three places**: an
incomplete declaration set (F2), a false safety argument for the blindness invariant (F3), and a
frozen skeleton that cannot represent the run (F1).

**3. The floor.** **Clean.** A must determine the content and boundaries of at least seven prompt
files, none of whose content is yet specified; B must determine the content of four or five
documents plus an install step. Neither is "one file created or one coherent edit to one file,
with the content that goes in it specified". Neither half falls below the floor, and the
division's own argument at `:226–235` is correct. I filed nothing whose remedy is to decompose
below the floor.

**4. Real joint or arbitrary cut.** **A real joint.** Three of the four differences it names hold
against the source: the failure mode of getting it wrong (a bad stage file corrupts every run; a
bad `SKILL.md` frontmatter means the skill never triggers — the descriptions at
`Guarded_change/SKILL.md:3` and `Dragonfly/SKILL.md:3` are the trigger text, confirming the
distinction); the corpus-agnostic/corpus-naming line (the companion file is the only place project
specifics live, `Guarded_change/METHODOLOGY.md:88–101`); and the authorship discipline (a shared
core plus role additions is evidenced by `stages/charter.md` being shared across stages 3 and 6
with per-stage additions, `Guarded_change/SKILL.md:49–50`, and passed *verbatim* per
`Guarded_change/stages/charter.md:71–74`). The fourth — "the reader" — is **overstated** in the
direction that matters: B's `SKILL.md` is also executed, by the session (F3). The axis survives;
the argument built on the overstatement does not.

**This task is not indivisible.** I am not filing that finding. The cut should be kept and its
seam repaired.

---

## What I could not check

- Whether the seam's declarations are sufficient **in practice** — that is only observable once A
  is actually planned, which does not exist yet. F2 is argued from B's stated scope against S3/S4/S5
  as written, not from an A artifact.
- Whether `Data-Distiller/` (off limits, not opened) resolves any of these differently. Nothing in
  this review depends on it.
- Round 1 of this split and its findings: I was instructed to read no other file under
  `Architect/runs/`, so I do not know which of the above were already raised, already fixed, or
  already rejected. Any overlap is independent re-derivation, not confirmation.
