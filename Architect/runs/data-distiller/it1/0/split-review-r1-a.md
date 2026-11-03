# Split review — round 1, reviewer A

**Reviewing:** `Architect/runs/data-distiller/0/split-round-1.md` (proposed division of "Plan the
implementation of the Data-Distiller skill" into sub-task A "the frame" and sub-task B
"`stages/`").

**Inputs I actually had:** the task, the granularity floor, the proposed division. **No plan**
(correctly — the divider had none either). I judged the cut against the shape of the task and
against the two sibling skills the task names.

**Off-limits honoured.** I did not read, list or grep
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`. (I listed its parent
`/home/zero/Desktop/claude-code-skills/` once, which shows only the directory's existence — a fact
the task statement itself supplies. I went no further in.)

**Source material consulted** (all citations below are from these):
`Guarded_change/SKILL.md`, `Guarded_change/METHODOLOGY.md`, `Guarded_change/README.md`,
`Guarded_change/guarded-change.companion.md`, `Guarded_change/stages/` (listing),
`Dragonfly/SKILL.md`, `Dragonfly/METHODOLOGY.md`, `Dragonfly/dragonfly.companion.md`,
`Dragonfly/stages/` (listing).

**Verdict on the division: DIVISIBLE, but not at this seam as written.** The joint is real and the
rejection of the obvious alternative is sound (see "What holds up"). The cut is defeated by one
orphaned load-bearing element and by three seam defects, all repairable without changing where the
line falls.

---

## Findings

| # | Severity | Lens | One line |
|---|---|---|---|
| F1 | **blocker** | Completeness / Coverage | No half owns the step that produces the run's final findings deliverable, and the division's own rules forbid either half from adding it. |
| F2 | **major** | Coverage / Logical | The top-level run procedure (the siblings' `## Loop`) is assigned to neither half, and A's two statements of its own prohibition contradict each other on whether A may write it. |
| F3 | **major** | Coverage | Restart/resume decision logic is claimed by **both** halves. |
| F4 | **major** | Completeness (seam) | The seam's 5-item contract omits the decomposition/item-manifest record schema — the one record every role and the resume path depend on. |
| F5 | **major** | Unstated assumptions | `CONTRACT-DELTA:` is an upward channel with no named receiver and no stated reconciliation step. |
| F6 | minor | Missed opportunity | A third placement of the line (run-state + contract below the cut) is not considered and would resolve F3 and F7. |
| F7 | minor | Logical | The stated joint ("read once, documentation and vocabulary") does not describe two of A's five artifacts. |
| F8 | minor | Factual | "Matches the section shape of" the sibling METHODOLOGY files, but the enumeration drops the section both siblings end on. |
| F9 | minor | Factual | The template-vs-instance exclusion in "what neither owns" is mis-grounded in the sibling shape. |
| F10 | nitpick | Fidelity | Corpus-agnosticism is asserted as a property of the method but assigned to no half as a checkable constraint on B's files. |

---

### F1 — blocker — nothing produces the run's output

`split-round-1.md:92-103` enumerates B's `stages/` files exhaustively: common core,
decompose-and-size, analyst, verify, merge, node. **None of them emits the run's answer.**

- "merge" is per-item — the task defines it as ranking *one item's* surviving findings by how many
  of that item's N analysts agreed (`split-round-1.md:16`, `:102`).
- the node is **blind by construction** — "never reads the findings themselves, only the terse
  per-child status" (`:102-103`). A blind agent cannot author a findings report.
- A's side has only "**what a run produces** (the on-disk artifact layout)" (`:60`) — a *layout*,
  and A "must not restate a procedure, only point at it" (`:142`).

So the deliverable named in the task's own first sentence — "extracting trustworthy, source-cited
factual findings" (`:7-9`) — has no producer.

What makes this a blocker rather than something the executors will paper over: `:108-109` states B
"introduces no new artifact name, config key, record field, or `stages/` file", and `:142` bars A
from writing procedure. **The division as written forbids either half from repairing it.** Each
half will read the other's scope statement and conclude the deliverable is the other's.

Both siblings have exactly this element and produce it from a *named stage*, not from a layout:
Dragonfly emits `diagnosis.md` at stage 8 (`Dragonfly/SKILL.md:50`, `Dragonfly/METHODOLOGY.md:150-152`),
guarded-change emits `8-harness.md` with the verdict (`Guarded_change/SKILL.md:45`,
`Guarded_change/METHODOLOGY.md:167`). The house shape the task points at has a terminal,
agent-authored artifact. This division has none.

**Remedy (either is fine, but the division must pick one and say so):** (a) add a terminal
roll-up/report role to B's `stages/` list and to A's contract item 1; or (b) declare explicitly
that the deliverable *is* the on-disk merged-findings set with no assembly step, and say which half
specifies its shape. Silence is the failure — this is a load-bearing design decision that both
halves will otherwise assume the other made.

### F2 — major — the top-level run procedure is unassigned, and A's prohibition self-contradicts

A's `SKILL.md` bullet (`:52-56`) lists: frontmatter, inputs, "the stage/role index table", the
stop-for-human conditions, the self-check note — and claims this "Matches the sibling shape at
`Guarded_change/SKILL.md` and `Dragonfly/SKILL.md`".

It does not. In both siblings the index table sits *inside* a `## Loop` section that carries real
top-level procedure, not just an index:

- `Guarded_change/SKILL.md:27` — "Create a change folder `changes/<slug>/` and produce one doc per
  stage"; `:29-31` — what to append to `decisions.md` at every gate; `:51-52` — the iteration cap.
- `Dragonfly/SKILL.md:31-33` — "Create a hunt folder `hunts/<slug>/` and maintain the ledgers as
  **files** there"; `:60-70` — the whole incidental-findings procedure.

For Data-Distiller that section is where "read the config, create the run directory, decompose,
then start the tree" would live. The invoking agent is **not a dispatched agent**, so B's scope —
"the prompt files that dispatched cold agents read verbatim at run time" (`:88-89`) — excludes it.

And A's scope states the prohibition twice, incompatibly:

- narrow, at `:77-78`: "This half does NOT write the procedure body of any **dispatched-agent
  role**" — which *permits* A to write the invoking agent's procedure;
- broad, at `:142`: "A must not restate a procedure, only point at it" — which forbids it.

**Failure scenario:** A's author reads `:142`, writes an index-only SKILL.md; B's author reads
`:88-89`, writes six dispatched-agent prompts. The combined plan has eleven files and no statement
of what the human-invoked agent does first, second, third. Nothing downstream detects this, because
each half is internally complete against its own brief.

**Remedy:** assign the top-level control flow explicitly (A is the natural owner, since it owns
`SKILL.md`), and collapse the two prohibition statements into one wording.

### F3 — major — restart/resume is claimed by both halves

- A owns "**the on-disk run-state layout and restart/resume semantics** … and **how a restarted run
  decides what to redo and what to trust**" (`:66-67`). That last clause is decision logic — a
  procedure.
- B's node role "**resumes from on-disk state**" (`:103`), and the node is the agent that must
  execute exactly that logic.

This is the mirror of the failure question 1 warns about: not a portion each assumes the other
owns, but a portion **each half is told it owns**. Two independent authors will each specify it,
in different words, and the combined plan will carry two descriptions of one mechanism — the drift
hazard the additions-only rule at `:105-107` exists to prevent, reintroduced at the seam.

Contrast the concurrency ceiling, which the division splits *correctly*: A owns "the
concurrency-ceiling semantics" (`:75`), B's node "enforces" it (`:103`). Semantics above, enforcement
below. Resume needs the same treatment, or needs to move wholly into one half (see F6).

### F4 — major — the item manifest is missing from the seam contract

The seam enumerates what A produces for B (`:129-134`): stages file list, on-disk names and layout,
the per-child status schema, the finding-record schema, the config key set.

The record that carries **the decomposition itself** is absent — the item list, each item's measured
size, and the per-item strategy chosen when an item does not fit (`:11-13`, `:96-97`). That record is:

- the **output** of B's decompose-and-size role,
- the **input** the node needs to know what children to spawn and how many,
- the **input** every analyst needs to know which item it was given,
- and the **state** a restarted run reads to decide what is done (F3's mechanism has nothing to read
  without it).

A is told it owns "the on-disk run-state layout" (`:66`, `:130`), which necessarily contains the
manifest — yet A's own ownership list (`:71-75`) names the status-record schema and the
finding-record schema and stops. **Failure scenario:** A specifies directory names and two record
schemas; B's decompose role invents a manifest format; B's node role reads it; the resume story A
wrote refers to a structure A never defined. Combined, the plan's contract section and its
procedures disagree about what is on disk.

**Remedy:** add the item/manifest record schema as contract item 6, including the size field and the
strategy field.

### F5 — major — `CONTRACT-DELTA:` has no receiver

`:108-111` and `:138` establish that B's only upward channel is a `CONTRACT-DELTA:` line on any step
it cannot write inside A's contract. Nothing states **who consumes it**, whether A's plan is
amended, or whether an unreconciled delta blocks anything.

Because the halves are planned by independent agents (that is the point of the split), a delta
raised in B's document lands where A's author will never see it. The observable result is a combined
plan whose contract section is contradicted by a later step, with no marker saying which won.

**Failure scenario:** F1's terminal report role is exactly the delta B would raise. B writes
`CONTRACT-DELTA: needs stages/report.md`, A's contract item 1 still lists six stage files, and the
plan ships claiming an exhaustive index that is not exhaustive.

**Unchecked, and I am flagging it rather than assuming either way:** Architect may have a combining
role charged with reconciliation. My inputs do not include it and my role file confines me to what
the task points at, so I did not read Architect's own stage files to find out. If such a receiver
exists, the fix is one sentence in the seam naming it and saying a delta must be reconciled into A's
contract before the plan is considered whole. If it does not, the channel is decorative.

### F6 — minor — the third placement of the line was not considered

`:150-163` considers exactly one alternative (cutting at the blind-roll-up barrier) and rejects it
well. A third option is not mentioned: keep the cut where it is but move **run-state layout +
restart/resume** (A's bullet at `:66-67`) down into B, leaving A as pure packaging/orientation
(`SKILL.md`, `METHODOLOGY.md`, config, README, install) plus the naming contract.

This resolves F3 outright (one owner for resume), makes the stated joint literally true (F7), and
costs only that METHODOLOGY's "what a run produces" section points at B's layout instead of stating
it — which is what both siblings' METHODOLOGY already does for operative rules
(`Guarded_change/METHODOLOGY.md:180-181`: "The operative form of this rule lives in the gate/harness
stage files"). I am not asserting this is the better option; it is the option the analysis owed a
paragraph and did not get.

### F7 — minor — the stated joint does not describe A's contents

The seam's justification (`:122-127`) is: above the cut, files are "read **once, by the invoking
agent** … they are documentation and vocabulary"; below, they are prompts read verbatim mid-run.

Two of A's five artifacts do not fit that description. The **per-corpus config** (`:62-64`) is read
at run time and its contents bind dispatched agents — what is off-limits constrains every analyst,
the concurrency ceiling constrains the node. The **run-state layout** (`:66-67`) is not documentation
at all; it is the operational contract the node executes against.

**Failure scenario:** A's author, correctly following the seam's characterisation of their half as
"documentation and vocabulary" and its licence that "reference spec may restate for orientation",
writes the run-state layout in the register of prose orientation — approximate, illustrative — and B
inherits an under-specified structure it is forbidden to extend (`:108-109`). The real distinction
is *contract-and-packaging vs. procedure*, which is a fine joint; it is just not the one written
down.

### F8 — minor — the METHODOLOGY section list drops the siblings' closing section

`:58-61` claims A's `METHODOLOGY.md` "Matches the section shape of `Guarded_change/METHODOLOGY.md`
and `Dragonfly/METHODOLOGY.md`". Mapping the enumerated sections against the sources:

| A's enumeration (`:58-61`) | GC | DF |
|---|---|---|
| why it exists / what failure it prevents | `:18` Why this exists | `:22` Why this exists |
| the method in prose | `:35` The loop | `:45` The loop |
| the stage/role index | `:67` Stage index | `:72` Stage index |
| the two layers | `:88` The two layers | `:95` The two layers |
| the config contract | `:103` The config contract (Layer 2) | `:106` The config contract (Layer 2) |
| what a run produces | `:154` What a run produces | `:141` What a run produces |
| *(absent)* | **`:198` Human-in-the-loop** | **`:172` Human-in-the-loop** |

Both siblings end on Human-in-the-loop, and both carry the paired `## Stop-for-human` in SKILL.md
(`Guarded_change/SKILL.md:55`, `Dragonfly/SKILL.md:72`). A's SKILL.md bullet does include
"stop-for-human conditions" (`:55`), so this is a gap in one file rather than an orphaned concern —
hence minor. It matters for this skill specifically: a recursive blind-roll-up run has real stop
conditions (corpus will not decompose, an item does not fit under any strategy, config missing,
concurrency exhausted) and no half is told to enumerate them.

### F9 — minor — template vs. instance, against the sibling shape

A owns "a **worked per-corpus config template/example** file" (`:62`), and the seam's "what neither
owns" list excludes "Authoring a per-corpus config **instance** for any specific real corpus (A owns
only the template/example)" (`:146-147`).

In both siblings the shipped artifact *is* an instance, not a template: `guarded-change.companion.md:1`
— "# guarded-change config — companion-emergence (Layer 2)", and `dragonfly.companion.md:1` — the
same for Dragonfly. Both are configs for one real project, living in the skill directory, and both
point at METHODOLOGY for the contract (`guarded-change.companion.md:3-4`). The *template* in the
house shape is the "config contract (Layer 2)" section of METHODOLOGY, not a separate file.

As written, the exclusion at `:146-147` could be read as forbidding the one artifact both siblings
actually ship. Either the exclusion should be narrowed ("no config for a corpus outside this run's
scope") or A's bullet should say the example may be a concrete worked instance.

### F10 — nitpick — corpus-agnosticism is unowned as a check

The task requires "the method itself stays corpus-agnostic" (`:20`). A owns the config contract
(`:75`), which is the *mechanism* — but nothing in either half's brief makes "no corpus specifics
appear in any `stages/` file" a constraint B's plan is written against. It is the kind of invariant
that is cheap to state up front and expensive to retrofit.

---

## Lens verdicts

**1. Factual — findings (F2, F8, F9).** Earned with citations: I checked every "matches the sibling
shape" claim against the sources. **Confirmed true:** YAML frontmatter with `name` and `description`
(`Guarded_change/SKILL.md:1-4`, `Dragonfly/SKILL.md:1-4`); both siblings carry a `README.md`
(directory listings) and a per-project Layer-2 config at the skill root; `stages/charter.md` exists
in both (`Guarded_change/stages/`, `Dragonfly/stages/`), so B's stated source material resolves;
METHODOLOGY carries a config-contract section and a "what a run produces" section in both
(`Guarded_change/METHODOLOGY.md:103,154`; `Dragonfly/METHODOLOGY.md:106,141`); a run folder inside
the skill directory (`changes/`, `hunts/`) is the house pattern. **Found false or incomplete:** the
SKILL.md shape claim (F2) and the METHODOLOGY shape claim (F8), and the config-instance premise (F9).

**2. Logical — findings (F2, F7).** The A→B ordering ("fixes it before the other half writes a line",
`:71-72`) is a genuine strict dependency and is stated, which I count as correct rather than as a
defect. The internal contradiction between `:77-78` and `:142` is the sequencing flaw. The seam's
stated rationale not matching its own contents is the second.

**3. Missed opportunity — finding (F6).** The one alternative considered was considered well; a
second, cheaper one was not.

**4. Unstated assumptions & risks — finding (F5).** The load-bearing unstated assumption is that
*someone* reconciles a `CONTRACT-DELTA`. Secondary and folded into F1: the assumption that "what a
run produces" as a layout is the same thing as producing it.

**5. Fidelity — finding (F10); otherwise clean, earned by pinning.** Terms pinned to concrete
mechanisms in the division: **"cold agent"** → B's common-core file, "shares no context with
siblings", read-only over the corpus (`:93-95`) — real mechanism, not a proxy. **"N independent
analysts"** → independence enforced by the common core plus per-item parallel dispatch (`:98-99`);
mechanism present. **"blind roll-up"** → enforced structurally by the node reading only the
status record, whose schema is a single contract item (`:132`) and whose two procedures both sit in
B (`:102-103`, `:160-162`); this is the division's strongest move and I confirm it is the mechanism,
not a proxy for it. **"verify"** → a separate cold pass that re-checks each citation and drops the
unverifiable, its own file (`:100`). **"merge"** → agreement-count ranking, its own file (`:101`) —
but see F1, it is per-item only. **"decompose"** → a real sizing-and-strategy step, its own file
(`:96-97`). **"resume"** → present but double-owned (F3). **"corpus-agnostic"** → mechanism is the
Layer-2 config (`:62-64`, `:75`); the invariant is unpoliced (F10).

**6. Completeness — findings (F1, F4, F8).** Checklist floor: the division's own required parts are
all present (two sub-tasks, an explicit seam, a what-neither-owns list, an alternative considered and
rejected, a floor check). **Generative sweep run.** I asked what load-bearing section the four
questions do not anticipate, and looked for: (a) a producer of the run's terminal deliverable — **hole
found, F1**; (b) the schema of every record that crosses a role boundary, not just the two named —
**hole found, F4**; (c) the top-level control flow distinct from any dispatched role — **hole found,
F2**; (d) stop-for-human / escalation conditions — **thin, F8**; (e) an ordering/dependency statement
between the halves — **present** (`:71-72`); (f) a return path for the seam's own escape hatch —
**hole found, F5**; (g) failure modes of the method itself (an item that fits no strategy, zero
surviving findings after verify, all N analysts disagreeing) — **not assigned to either half**, but I
judge this to sit below the split reviewer's remit and inside B's procedure design, so I raise it
here as a note rather than as a finding; (h) an install/packaging step — **present** (`:68-69`).

**Was any portion of the task left unaddressed?** Yes — the terminal deliverable (F1) and the
top-level procedure (F2). Every other bullet of the task statement maps to a named owner; I checked
all eight defining properties individually.

---

## The four questions

**1. Coverage — FAIL.** Seven of the task's eight defining properties have a clean owner. The
deliverable those properties exist to produce has none (F1). Separately, the top-level procedure has
none (F2), and one portion — resume — has two (F3).

**2. The seam — stated, partly unsound.** The seam *is* stated, and stated unusually well: a
five-item contract, an explicit direction of flow, an explicit what-each-may-assume, and an explicit
what-neither-owns. It fails on three specifics: a missing contract item (F4), a return channel with
no receiver (F5), and a rationale that does not describe half its own contents (F7).

**3. The floor — PASS, no finding.** The floor is "one file created or one coherent edit to one
file, with the content specified". A is ~5 files, B is ~6; both are coherent whole tasks well above
one file. The floor check at `:166-169` is correct as far as it goes, and I confirm it independently:
neither half is at or below the floor, and the parent task (≈11 files) is clearly above it, so
splitting was warranted rather than gratuitous. **The floor is not the wrong floor for this task** —
"one file with its content specified" is exactly the unit a skill-authoring plan produces.

**4. Real joint or arbitrary cut — REAL JOINT, mislabelled.** Something genuinely changes at this
boundary: above it, files are authored for a reader who has other context and reads them to orient;
below it, files are authored for a reader who has *nothing but that file* and executes it. That
difference dictates a different authoring register (siblings' METHODOLOGY restates for orientation,
`Guarded_change/METHODOLOGY.md:180-181`; role prompts may not restate at all, `:105-107`), so the cut
is not symmetry-driven. The label put on the joint is wrong for two of A's artifacts (F7), and the
better label is contract-and-packaging vs. procedure.

## What holds up (so the repair does not throw it away)

- **The rejection of the blind-roll-up cut (`:150-163`) is correct and is the best reasoning in the
  document.** "The node never reads findings, only the status record" is one rule two roles must act
  on; splitting it across halves leaves neither able to state it. Putting the barrier's *schema* in
  the contract and both *procedures* in one half is the right resolution, and it survives every
  finding above. Do not re-open this.
- **The what-neither-owns list (`:144-148`) is a discipline most divisions skip**, and it correctly
  keeps the off-limits directory and run-evaluation out of scope for both.
- **The `CONTRACT-DELTA` idea is right even though its plumbing is missing** (F5) — an explicit,
  greppable marker beats silent contract drift.
- **The semantics-above / enforcement-below treatment of the concurrency ceiling** (`:75` vs `:103`)
  is the pattern F3 should be repaired into.

## Recommended disposition

Round 2 on the same joint. The line falls in a defensible place; what needs re-deriving is what sits
on each side of it. Minimum repairs: assign the terminal deliverable (F1), assign the top-level
procedure and reconcile A's two prohibitions (F2), give resume one owner (F3), add the item-manifest
schema to the contract (F4), name the delta's receiver (F5).
