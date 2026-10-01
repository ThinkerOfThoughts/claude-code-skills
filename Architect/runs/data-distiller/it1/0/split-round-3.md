# Proposed division — round 3 (final round)

Round 2 kept the line but overloaded it. All three cold reviewers said the same two things: the
**driver/worker joint is real and should be kept**, and **every defect was in the shared interface**
— which had grown into four record schemas, a directory layout, a config key set, a strategy
enumeration and a producer assignment. One reviewer named the underlying problem exactly: *"a
ten-object interface fixing four schemas, a directory layout, a config key set, a name enumeration
and a producer assignment is a specification, not a seam. A joint has a narrow interface."*

Round 3 keeps the joint and **shrinks the interface instead of patching it**, using one structural
move that removes most of what was crossing:

> **The driver creates and hands down every path and every value a worker needs. No worker file
> names a path, reads a config file, or knows the run layout.**

That single change deletes from the seam: the on-disk directory layout, the Layer-2 config key set,
the finding-record schema, the manifest-entry schema, and most of the status-record schema — all of
which become wholly one half's business. What is left is nine short clauses, none of them a schema.

Round 2's findings and their disposition are recorded at the end of this file.

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

**The cut:** the **driver plane** — the files read by an agent that already holds the run's context
and decides what happens next — versus the **worker plane** — the files handed verbatim to cold
agents whose entire context is that file plus what they were handed at spawn.

---

# SUB-TASK ONE — the driver plane

*(Everything from this heading to the next `# SUB-TASK` heading is this sub-task's text. It is
self-contained: the seam is restated inside it verbatim, because the agent planning this half will
never see the other half's output.)*

Plan the implementation of the **driver plane** of the Data-Distiller skill: the reference and
packaging files, and the files read by the agent that drives a run. **This half decides what
happens, in what order, with what concurrency, and what every dispatched worker is handed.** It is
accountable for a run that terminates, stays inside its ceiling, resumes after a kill, keeps its
coordinators from ever seeing a finding, and hands the human a result.

**Files this half plans. Each plan step is one file created, with the content that goes in it
specified.**

1. **`SKILL.md`** — the router. YAML frontmatter (`name: data-distiller`; a `description` written
   to trigger when a corpus too large for one pass must be distilled into cited, verifiable facts).
   Then: **Inputs** (the corpus and the Layer-2 per-corpus config; what to do when the config is
   absent or its paths are dead); a **cold-start guard** section (precedent: `Dragonfly/SKILL.md:22`
   — Dragonfly only, Guarded_change has none); the **run loop**, in the register of
   `Guarded_change/SKILL.md:25-52` and `Dragonfly/SKILL.md:29-70` — **its first step is the resume
   check**, then validate config, create the run directory, dispatch decomposition, then per item
   dispatch N analysts → verify → merge, then roll up, then hand over; the **stage/role index
   table**, one row per file under `stages/`, using the six paths and the six one-line purposes
   fixed verbatim in S1 below; **Stop-for-human**; the self-check/dogfooding note.
2. **`METHODOLOGY.md`** — the reference spec, in the siblings' section shape: *Why this exists*;
   *The method* — rendered as a fenced stage diagram, as at `Guarded_change/METHODOLOGY.md:37-54`
   and `Dragonfly/METHODOLOGY.md:47-62`, not as prose; *Stage/role index*; *The two layers*;
   *The config contract (Layer 2)* — the annotated key skeleton inline, as at
   `Guarded_change/METHODOLOGY.md:103-152`; *What a run produces* — the full on-disk artifact
   layout, which this half owns outright; *Trigger* (precedent: `Dragonfly/METHODOLOGY.md:161` —
   Dragonfly only); *Human-in-the-loop*.
3. **`stages/node.md`** — the coordinating/roll-up role: the only prompt file in this half, read by
   an agent that dispatches and never analyzes. It carries the recursion (how a node decides
   between spawning child nodes and dispatching workers, and how items are assigned to nodes); the
   **concurrency ceiling — semantics and enforcement**; the **restart/resume decision procedure in
   full** (`SKILL.md`'s run loop points here; this is the operative copy, named as such in the
   manner of `Guarded_change/METHODOLOGY.md:143`); the **spawn payload it hands each worker role**,
   matching S2 below; **the analyst-independence dispatch discipline** of S5; and the
   **blind-roll-up barrier** of S4. It does **not** include `stages/common.md` — a node reads no
   corpus, makes no claims and cites nothing, so none of that file's rules bind it; its own rules
   are written here.
4. **A worked per-corpus config instance**, a top-level file named `data-distiller.<corpus>.md`, in
   the form of `Guarded_change/guarded-change.companion.md` and `Dragonfly/dragonfly.companion.md`
   — a concrete instance pointing at `METHODOLOGY.md` for the contract. The task names no real
   corpus, so **use an explicitly-labelled example corpus and say in the file that it is an
   example**. This is the only file in the whole skill permitted to contain corpus specifics (S8).
5. **`README.md`** — human-facing orientation, as both siblings carry, including the install
   instruction: the skill is installed by being present at `~/.claude/skills/data-distiller/`, and
   the live copy must equal the source copy.

*(The install is documented in file 5 and verified as a step; the granularity floor is phrased in
files, so an install action has no shape under it. It is nonetheless executable without further
planning, so it is not below the floor — noting the floor's shape rather than working beneath it.)*

**This half owns, in full and exclusively:** all control flow (the invoking agent's and a node's);
the entire on-disk run-state layout and every path in it, including the run directory's location
and a `decisions.md`-style gate/decision log in the manner of `Guarded_change/METHODOLOGY.md:175-182`
and `Dragonfly/METHODOLOGY.md:152-153`; restart/resume; the concurrency ceiling; **the whole Layer-2
config contract — the key set, its documentation, and its validation**; the analyst-independence
dispatch discipline; the blind-roll-up barrier; stop-for-human; the trigger and description;
packaging and install. **This half writes procedure and is expected to**; where a rule appears in
more than one of its files, name which copy is operative.

**This half does NOT write** any of the five worker files under `stages/`, and does not specify what
a finding is, how an item is sized or its strategy chosen, how a citation is re-checked, or how
agreement is ranked.

**Source material this half is checked against:** all of
`/home/zero/Desktop/claude-code-skills/Guarded_change/` and all of
`/home/zero/Desktop/claude-code-skills/Dragonfly/`, **including their `stages/` directories**.
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS: do not read, list or grep it.

## THE SEAM — S1–S9, binding on this half, stated identically in the other half

These are the only things that cross the cut. Neither half may rename or re-scope one. **Anything
not fixed here belongs wholly to one half** — in particular the run directory layout, every path,
the Layer-2 config key set, and the fields of the manifest, finding and status records are **not**
fixed here and are not shared. If this half believes a clause is wrong, it plans against it anyway
and states the objection as a note for the plan's reviewers; there is no channel to the other half,
which will never see it.

**S1 — the six files under `stages/`, with the one-line purposes the router must publish verbatim.**
This set is closed.
- `stages/common.md` *(worker plane)* — "The rules every dispatched worker obeys; included verbatim
  ahead of every worker role file."
- `stages/decompose.md` *(worker plane)* — "Split the corpus into analyzable items, size each, and
  choose a strategy for any item that does not fit."
- `stages/analyst.md` *(worker plane)* — "One of N independent cold analysts over a single item;
  every finding carries a re-openable citation."
- `stages/verify.md` *(worker plane)* — "Re-open every citation and drop what does not check out."
- `stages/merge.md` *(worker plane)* — "Rank surviving findings by how many independent analysts
  agreed, and write the unit's status record."
- `stages/node.md` *(driver plane)* — "Coordinate a subtree: dispatch, enforce the ceiling, resume,
  and roll up without ever reading a finding."

**S2 — the spawn payload.** The driver hands every worker exactly the arguments below; each worker
file's inputs section lists exactly the same. No worker file names a path of its own, and **no
worker reads any config file** — every corpus-specific value it needs arrives here.
- **decompose** ← the corpus root; what counts as an analyzable item; what is off-limits; the
  context budget an item must fit inside; the permitted over-size strategy names; its output path.
- **analyst** ← its item's locator (as written in the manifest); its own analyst index *k*; what is
  off-limits; its output path.
- **verify** ← the N analyst output paths for one item; the item's locator; what is off-limits; its
  output path.
- **merge** ← the input paths to merge (an item's verified findings, or the merged outputs of a
  node's children); its output path; the path to write the unit's status record.

**S3 — who writes what, and the two invariants on it.**
- **decompose** writes the **item manifest** to its handed path: a markdown file with one entry per
  analyzable item, each entry beginning with a unique, filesystem-safe item id on its own line,
  followed by that item's locator. Everything else in an entry is the worker plane's business. The
  manifest contains no findings, so a driver-plane agent may read it.
- **analyst** writes one analyst's findings; **verify** writes the verified findings; **merge**
  writes the merged, agreement-ranked findings **and the unit's status record**.
- **Invariant A — the status record.** It states the unit's outcome as one of `complete`, `failed`,
  `partial`, and **carries no finding text, no claim and no citation**. Its other contents are the
  worker plane's business. A driver-plane agent may read it. **It is written only after the unit's
  other outputs are complete and closed** — a unit with no status record is treated by resume as
  incomplete. When a unit fails before `merge` runs, the driver writes the status record itself,
  stating `failed`; writing a failure record requires knowing no findings.
- **Invariant B — the return channel.** Every worker's return value is its output path plus one of
  those three outcome words, and **nothing else** — no claim, no citation, no finding text. This is
  a rule in `stages/common.md` and it is what stops findings reaching a coordinator's context
  through the reply rather than through a file.

**S4 — the blindness barrier.** *No driver-plane agent ever opens an analyst-findings, verified,
merged, or `FINDINGS.md` artifact.* It may create, name, pass and delete those paths — that is
required by S2 — but it reads only the item manifest and status records. This is stated as an
absolute read prohibition rather than as path-withholding, because the driver must construct those
paths to dispatch at all.

**S5 — analyst independence is a dispatch property and a scavenging prohibition.** The driver
spawns the N analysts for an item as N separate cold agents, none of them handed another's output
path, none given any other analyst's result, and none informed of what a sibling found. The worker
side of it: `stages/common.md` forbids a worker to open any file except the paths it was handed at
spawn. Neither rule restates the other; they bind different actors.

**S6 — the terminal deliverable.** `<the run's FINDINGS file>` is written by a dispatched **merge**
agent running `stages/merge.md` at the root of the roll-up. The driver dispatches it, hands the
human its path, and never opens it. It must carry a **coverage note** stating which items were
analyzed by `window` or `sample` and are therefore not fully covered. Neither half may reassign this
producer.

**S7 — the over-size strategy names** are `split`, `window` and `sample`. **`split` is resolved
entirely inside `stages/decompose.md`:** decompose emits the pieces as ordinary manifest entries
with their own item ids, so no recursion, re-dispatch or manifest rewriting happens outside that one
worker. `window` and `sample` are executed by the analyst on a single item. Which strategy applies
to a given item is the worker plane's rule; that the permitted set is a config key, validated and
passed down, is the driver plane's.

**S8 — corpus-agnosticism.** No corpus-specific content appears in any file except the worked config
instance, which is an explicitly-labelled example. This binds both halves.

**S9 — run artifacts are markdown**, as in both siblings, whose run artifacts are markdown without
exception (`Guarded_change/METHODOLOGY.md:154-168`, `Dragonfly/METHODOLOGY.md:141-153`); structured
content may sit in a fenced block inside a markdown file, as both siblings' configs do.

---

# SUB-TASK TWO — the worker plane

*(Everything from this heading to the next `#` heading is this sub-task's text. It is
self-contained: the seam is restated inside it verbatim, because the agent planning this half will
never see the other half's output.)*

Plan the implementation of the **worker plane** of the Data-Distiller skill: the five prompt files
handed **verbatim** to dispatched cold agents. Each such agent's entire context is its file plus the
arguments it was handed at spawn; it does one bounded pass and returns. **This half decides what a
worker must produce and must prove.** It is accountable for every returned artifact being cited,
verified, uninterpreted and independently arrived at — not for the run terminating, resuming, or
staying within its ceiling.

**Files this half plans. Each plan step is one file created, with the content that goes in it
specified.**

1. **`stages/common.md`** — included verbatim ahead of every worker role file. It states what every
   worker shares: cold independence (no shared context with the dispatcher or with siblings);
   read-only over the corpus; enforce the off-limits value it was handed; **open no file except the
   paths handed at spawn** (S5); the output contract — write to the handed path, and return that
   path plus one outcome word and nothing else (S3 Invariant B); cite-or-it-doesn't-count; facts,
   not interpretation; and halt-and-say-so when the handed inputs are unusable. It **may carry more
   than this** — that list is a floor, not a ceiling — and it binds workers only, not coordinators.
2. **`stages/decompose.md`** — split the corpus into analyzable items per the item definition it was
   handed, size each, decide whether it fits the handed context budget, and for any that does not,
   choose a strategy from the permitted names. Resolves `split` itself by emitting the pieces as
   ordinary manifest entries (S7). Writes the item manifest.
3. **`stages/analyst.md`** — one of N independent cold analysts over a single item. Read-only over
   the corpus; a re-openable source citation for every finding; facts, not interpretation. Must say
   what an analyst does when its item's strategy is `window` or `sample`, and how the omission is
   recorded so it survives to the deliverable.
4. **`stages/verify.md`** — re-open **every** citation in the analyst findings it was handed and
   drop what does not check out, recording what was dropped and why. Must say what "the citation
   checks out" means concretely and what to do when nothing survives.
5. **`stages/merge.md`** — rank surviving findings by how many independent analysts agreed, and run
   at **two** levels: per item, across that item's N analysts; and at a roll-up node, across the
   merged outputs of that node's children. Must say what agreement means when two analysts word the
   same claim differently, what ranking means once items are rolled up, the shape of the run's
   `FINDINGS` deliverable including its coverage note (S6), and — at every level — the unit's status
   record (S3).

**Role files are additions only and never restate a rule from `stages/common.md`.** If a role file
needs to modify a common rule, that rule was never common and belongs in the roles.

**This half owns, in full and exclusively:** what each worker is told; the evidentiary discipline
and where each rule sits between `common.md` and a role file; the sizing and strategy-selection
criteria; the verification test; agreement ranking at both levels; the content and shape of every
artifact a worker writes — including **all fields of the finding record, of a manifest entry, and of
the status record beyond the one outcome word** the seam fixes.

**This half does NOT write** `SKILL.md`, `METHODOLOGY.md`, `README.md`, the config instance, or
`stages/node.md`; does not decide dispatch, order, fan-out, concurrency, resume, or the run layout;
and **names no path and reads no config file** — every value and path a worker needs arrives in the
spawn payload fixed in S2 below.

**Source material this half is checked against:** all of
`/home/zero/Desktop/claude-code-skills/Guarded_change/` and all of
`/home/zero/Desktop/claude-code-skills/Dragonfly/`, **including their `SKILL.md` and
`METHODOLOGY.md`** — note especially `Guarded_change/stages/charter.md` and
`Dragonfly/stages/charter.md` as the house precedent for a cold-agent prompt and for finding
discipline. `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is OFF LIMITS: do not read, list
or grep it.

## THE SEAM — S1–S9, binding on this half, stated identically in the other half

These are the only things that cross the cut. Neither half may rename or re-scope one. **Anything
not fixed here belongs wholly to one half** — in particular the run directory layout, every path,
the Layer-2 config key set, and the fields of the manifest, finding and status records are **not**
fixed here and are not shared. If this half believes a clause is wrong, it plans against it anyway
and states the objection as a note for the plan's reviewers; there is no channel to the other half,
which will never see it.

**S1 — the six files under `stages/`, with the one-line purposes the router must publish verbatim.**
This set is closed.
- `stages/common.md` *(worker plane)* — "The rules every dispatched worker obeys; included verbatim
  ahead of every worker role file."
- `stages/decompose.md` *(worker plane)* — "Split the corpus into analyzable items, size each, and
  choose a strategy for any item that does not fit."
- `stages/analyst.md` *(worker plane)* — "One of N independent cold analysts over a single item;
  every finding carries a re-openable citation."
- `stages/verify.md` *(worker plane)* — "Re-open every citation and drop what does not check out."
- `stages/merge.md` *(worker plane)* — "Rank surviving findings by how many independent analysts
  agreed, and write the unit's status record."
- `stages/node.md` *(driver plane)* — "Coordinate a subtree: dispatch, enforce the ceiling, resume,
  and roll up without ever reading a finding."

**S2 — the spawn payload.** The driver hands every worker exactly the arguments below; each worker
file's inputs section lists exactly the same. No worker file names a path of its own, and **no
worker reads any config file** — every corpus-specific value it needs arrives here.
- **decompose** ← the corpus root; what counts as an analyzable item; what is off-limits; the
  context budget an item must fit inside; the permitted over-size strategy names; its output path.
- **analyst** ← its item's locator (as written in the manifest); its own analyst index *k*; what is
  off-limits; its output path.
- **verify** ← the N analyst output paths for one item; the item's locator; what is off-limits; its
  output path.
- **merge** ← the input paths to merge (an item's verified findings, or the merged outputs of a
  node's children); its output path; the path to write the unit's status record.

**S3 — who writes what, and the two invariants on it.**
- **decompose** writes the **item manifest** to its handed path: a markdown file with one entry per
  analyzable item, each entry beginning with a unique, filesystem-safe item id on its own line,
  followed by that item's locator. Everything else in an entry is the worker plane's business. The
  manifest contains no findings, so a driver-plane agent may read it.
- **analyst** writes one analyst's findings; **verify** writes the verified findings; **merge**
  writes the merged, agreement-ranked findings **and the unit's status record**.
- **Invariant A — the status record.** It states the unit's outcome as one of `complete`, `failed`,
  `partial`, and **carries no finding text, no claim and no citation**. Its other contents are the
  worker plane's business. A driver-plane agent may read it. **It is written only after the unit's
  other outputs are complete and closed** — a unit with no status record is treated by resume as
  incomplete. When a unit fails before `merge` runs, the driver writes the status record itself,
  stating `failed`; writing a failure record requires knowing no findings.
- **Invariant B — the return channel.** Every worker's return value is its output path plus one of
  those three outcome words, and **nothing else** — no claim, no citation, no finding text. This is
  a rule in `stages/common.md` and it is what stops findings reaching a coordinator's context
  through the reply rather than through a file.

**S4 — the blindness barrier.** *No driver-plane agent ever opens an analyst-findings, verified,
merged, or `FINDINGS.md` artifact.* It may create, name, pass and delete those paths — that is
required by S2 — but it reads only the item manifest and status records. This is stated as an
absolute read prohibition rather than as path-withholding, because the driver must construct those
paths to dispatch at all.

**S5 — analyst independence is a dispatch property and a scavenging prohibition.** The driver
spawns the N analysts for an item as N separate cold agents, none of them handed another's output
path, none given any other analyst's result, and none informed of what a sibling found. The worker
side of it: `stages/common.md` forbids a worker to open any file except the paths it was handed at
spawn. Neither rule restates the other; they bind different actors.

**S6 — the terminal deliverable.** `<the run's FINDINGS file>` is written by a dispatched **merge**
agent running `stages/merge.md` at the root of the roll-up. The driver dispatches it, hands the
human its path, and never opens it. It must carry a **coverage note** stating which items were
analyzed by `window` or `sample` and are therefore not fully covered. Neither half may reassign this
producer.

**S7 — the over-size strategy names** are `split`, `window` and `sample`. **`split` is resolved
entirely inside `stages/decompose.md`:** decompose emits the pieces as ordinary manifest entries
with their own item ids, so no recursion, re-dispatch or manifest rewriting happens outside that one
worker. `window` and `sample` are executed by the analyst on a single item. Which strategy applies
to a given item is the worker plane's rule; that the permitted set is a config key, validated and
passed down, is the driver plane's.

**S8 — corpus-agnosticism.** No corpus-specific content appears in any file except the worked config
instance, which is an explicitly-labelled example. This binds both halves.

**S9 — run artifacts are markdown**, as in both siblings, whose run artifacts are markdown without
exception (`Guarded_change/METHODOLOGY.md:154-168`, `Dragonfly/METHODOLOGY.md:141-153`); structured
content may sit in a fenced block inside a markdown file, as both siblings' configs do.

---

# The seam, stated once for the record

**What changes at this boundary — the reader's information state.** A driver-plane file is read by
an agent that already holds the run's context, can see the config and the layout, and decides what
happens next. A worker-plane file is read by an agent whose whole world is that file plus a handful
of handed arguments, that does one pass and returns. That difference determines what each file may
assume, which is the strongest form of joint a skill made of prompt files can have — and it is why
`stages/node.md` sits on the driver side despite being a prompt.

Round 2 justified the cut by claiming two "disjoint failure sets" and then listed *steered* on the
worker side, which was self-refuting: steering is what the blind-roll-up barrier prevents, and that
barrier is driver-plane. Corrected: **a driver-plane file fails by a run that stalls, blows its
ceiling, cannot be resumed, hands over nothing — or by a coordinator that reads findings and steers
its children. A worker-plane file fails by an artifact that is uncited, unverified, interpreted, or
copied from a sibling.** Now disjoint, with the barrier's own failure mode inside the driver set.

**What each half produces that the other consumes:** *nothing*. Every crossing object is fixed in
S1–S9 and reaches both halves identically. There is no upward channel and no ordering; the halves
can be planned simultaneously by agents that never communicate — which is what
`Architect/stages/node.md:50-53` and `leaf.md:16-19` actually do, and why round 1's directional
contract was unexecutable.

**What each may assume about the other:** that the other's files exist at the S1 paths, that they
obey S2–S9, and nothing else. No wording, section order or internal structure of the other's files
may be assumed.

**What neither owns:** `/home/zero/Desktop/claude-code-skills/Data-Distiller/`; executing, testing or
evaluating a run of the finished skill against a real corpus; and corpus-specific content outside the
one worked config instance.

**On the interface's size.** Round 2's interface fixed four record schemas, a directory layout and a
config key set. This one fixes **no schema, no layout and no key set** — those became one half's
business the moment the driver was made to hand down every path and value. What remains is a file
list the router must publish, a spawn payload that is two-sided by nature, a producer assignment with
two invariants, and four one-line rules. A seam between halves planned by agents that cannot
communicate cannot be smaller than the set of things both must agree on; this is that set.

**Floor check.** Driver plane: five files. Worker plane: five files. The floor is one file with its
content specified; both halves are five times it, both are coherent whole tasks, and both could
divide again. Neither falls below it.

# Alternatives weighed

**(a) Not dividing at all — returning `null`.** Weighed, and the cost of dividing named: per
`Architect/stages/node.md:44-53`, an undivided task goes to **three** leaves and is merged by
`Consensus` (2-of-3 including order), whereas a divided task goes to **two** children and is merged
by `Union`, which discards nothing and corroborates nothing. Dividing therefore trades away
independent corroboration of every step. Rejected because the halves are five files each — far above
the floor, which is the criterion for `null` — and because a single leaf writing all ten files at the
floor would have to specify ten files' contents in one pass, where the coverage failure that costs
most is exactly the one nothing below a leaf can catch.

**(b) Round 1's cut — the frame vs. all of `stages/`.** Rejected: it orphaned the driver's run loop,
split resume and the ceiling across the cut, and needed a directional contract the execution model
cannot deliver.

**(c) The two-layer cut** — Layer 1 (SKILL, METHODOLOGY, all of `stages/`) vs. Layer 2 (config
contract, worked config, README, install), the seam both siblings name in a section of their own
(`Guarded_change/METHODOLOGY.md:88-100`, `Dragonfly/METHODOLOGY.md:95-102`). Rejected: it is 8 files
against 2, and the config keys are consumed across almost every file of the large half, so the
interface would run through every file rather than along a boundary — a larger seam, not a smaller
one. The small half is packaging, which is a partition rather than a joint.

**(d) The per-item pipeline vs. the cross-item run plane** — one half owning everything that happens
to a single item, the other everything spanning items. Rejected because `stages/merge.md` runs at
both levels and `stages/common.md` binds workers at both, so both files would be co-owned; the cut
adopted here differs precisely in putting the level-spanning decisions (which are dispatch decisions)
wholly in the driver plane while merge's *content* at both levels stays with its single author.

# Round-2 findings and their disposition

| Finding (reviewers) | Severity | Disposition in round 3 |
|---|---|---|
| `status.json` has no producer; counts uncomputable by any single actor (all three) | blocker | S3: `merge` writes the unit's status record; the driver writes a `failed` record when a unit dies before merge. The mandated `counts` field is gone — the status record's contents beyond one outcome word are worker-owned. |
| The spawn payload is owned by neither half (C) | blocker | S2 fixes it per role, two-sided. |
| I8 withheld `corpus_root`/`oversize_strategies` from the only half that reads the corpus; no fit threshold, no run root (all three) | blocker/major | The config key set left the seam entirely. Workers read no config; every value arrives in the S2 payload, including corpus root, item definition, off-limits, context budget and permitted strategies. |
| I3 path-blindness contradicted I5 `output_path` and I9 (A, C) | blocker/major | S4 restates it as an absolute **read** prohibition; the driver may construct and pass those paths, which is what dispatch requires. |
| Analyst independence was an instruction the worker half could only assert (A, B, C) | major | S5 splits it into two non-overlapping rules: a driver dispatch discipline and a worker prohibition on opening anything not handed to it. |
| The worker return summary leaked findings into a coordinator's context (B) | major | S3 Invariant B: the return value is a path plus one outcome word, nothing else. |
| `node.md` had to include a `common.md` written for a role it is not; the cut ran through it (A, B, C) | major | `node.md` does not include `common.md`; `common.md` binds workers only. No file crosses. |
| `split` had no sub-item path, manifest linkage or dispatcher (all three) | major | S7: `split` is resolved inside `decompose`, which emits the pieces as ordinary items. No recursion outside that worker, so no linkage is needed at the seam. |
| The stage-index one-line purposes were promised as "fixed below" and were not (all three) | major | S1 fixes all six verbatim. |
| I2's "exactly these rules" closure blocked needed rules (B, C) | major | `common.md`'s rule list is a floor, not a ceiling, and the file is worker-plane-owned. |
| I7 (finding record) did not cross the cut — the divider designed inside a half (C) | major | Removed from the seam; all finding-record fields are worker-owned. |
| No item→node mapping; nothing reconstructs the tree on resume (C) | major | Item-to-node assignment is a driver decision recorded in the driver's own run state, which the driver owns outright; workers never need it. |
| "Disjoint failure sets" was self-refuting on *steered* (all three) | major/minor | Joint restated on the reader's information state; steering moved into the driver failure set, where its barrier lives. |
| The record of what was *not* analyzed had no route to the deliverable (B) | major | S6 requires a coverage note in the terminal deliverable; `analyst.md` must say how an omission is recorded. |
| Write-order/completeness rule for resume unowned (C) | blocker limb | S3 Invariant A: the status record is written only after the unit's other outputs are closed; a unit without one is incomplete. |
| No `decisions.md`-equivalent gate/decision log (A, B) | minor | Added to the driver plane's owned layout, citing both siblings. |
| Worked config has no corpus, but the floor demands its content (C) | minor | Explicitly-labelled example corpus authorised in file 4. |
| `.json` artifacts departed from the all-markdown house shape (A) | minor | S9: run artifacts are markdown. |
| `unit_id` introduced with no mapping to `item_id`/`node_id` (C) | minor | Field removed from the seam. |
| "Both siblings" false for the cold-start guard and for *Trigger*; "the method in prose" wrong for both (all three) | minor | Corrected in place: both marked Dragonfly-only, and the method is specified as a fenced stage diagram with both siblings' line ranges. |
| Resume placed in `node.md` while the run loop sat in `SKILL.md` (B) | minor | `SKILL.md`'s run loop opens with the resume check and points at `node.md` as the operative copy. |
| "Includes verbatim" ambiguous between dispatch-time concatenation and a build-time embed (C) | minor | Moot: `node.md` no longer includes anything, and S1 describes `common.md` as included ahead of worker role files at dispatch. |
| Two-layer alternative's file count was wrong (C) | nitpick | Corrected to 8 against 2. |
| The install step has no shape under a file-phrased floor (C) | nitpick | Recorded in sub-task one as a note on the floor's shape, not worked beneath. |
| "Indivisible"/`null` never weighed; the `Consensus`→`Union` cost never named (A, B) | minor | Weighed as alternative (a), with the corroboration cost named. |
