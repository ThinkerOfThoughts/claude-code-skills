# Split review — round 1, reviewer B

Cold split reviewer. I hold the **task**, the **granularity floor**, and the **proposed division**
(`Architect/runs/data-distiller/it3/0/split-round-1.md`). **I hold no plan**, and I have not
inferred one.

**Fence statement:** I did **not** read, list the contents of, grep, glob, or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`, and I did not invoke the installed
`data-distiller` skill. Its name appeared once, as a directory entry, in a listing of its *parent*
(`ls /home/zero/Desktop/claude-code-skills/`) run to check whether `Data-Distiller-impl/` already
exists (it does not). Nothing under the fenced path was opened.

**I did not read `split-review-r1-a.md`** or any other reviewer's output.

---

## Verdict — both parts

**Part 1 — what I found:** seven `major`, five `minor`, three `nitpick`. The seam is unusually
thorough for a round 1 and it correctly refuses the producer/consumer form in the large — but it
has **one internal contradiction** (§3.2 vs §3.4), **one un-fixed value vocabulary** (`tier` /
`size` unit) that reproduces the exact plan-time producer/consumer failure the charter warns
about, **one orphaned remainder** (nothing owns dispatching items to A's pipeline), **one
unowned artifact** (the run's corpus-level output), and **no path to the seam document itself**.

**Part 2 — do I object to going forward with this cut? NO. I do not object.**
The joint is real, it is the one the task statement names, and both halves are far above the
floor. I would keep this cut. Every finding below is fixable **inside the seam text** or by a
sentence in a sub-task, and each is tagged with the half it travels down with. Filing seven
majors is not an objection and must not be read as one.

---

## Findings

| ID | Sev | Question | One line | Travels with |
|---|---|---|---|---|
| S1 | major | coverage | Nothing owns dispatching items to A's pipeline (nor N-analyst independence at dispatch time, nor concurrency) | seam + B |
| S2 | major | seam | §3.2 and §3.4 contradict each other on whether an above-boundary agent may read `item.json` | seam |
| S3 | major | seam / fidelity | `findings_path` hands the blind coordinator the key it is told not to use — a temptation, not a structure | seam + B |
| S4 | major | seam (self-containment) | Neither sub-task carries a **path** to the seam document; every reference is a bare `§3.x` | seam |
| S5 | major | seam (self-containment) | `tier`'s value domain and `size`'s unit are B-defined at plan time and A-consumed — the forbidden form | seam |
| S6 | major | coverage | `oversize-deferred` has no defined consumer behaviour; the over-size control loop crosses the boundary unowned | seam + B |
| S7 | major | coverage | The run's corpus-level output artifact is unowned and absent from the run skeleton | seam + B |
| S8 | minor | joint | B's headline ("no agent ever reads corpus content") contradicts B's own P1 bullet (reads corpus *shape*) | B |
| S9 | minor | seam | A must read `run.dir`, a `B`-namespace key, contradicting §3.5's "neither half reads the other's namespace" | seam + A |
| S10 | minor | seam | Coldness (§3.6 r1) and read-only (§3.6 r3) are fixed in common.md yet assigned to A to author — additions-only collision | seam + A |
| S11 | minor | factual | `stages/common.md` is presented as sibling house style; the siblings have no such file | seam + B |
| S12 | minor | seam | Three ownership resolutions live only in §4, which is the divider's audit, not seam text | seam |
| S13 | nitpick | factual | §6 states in the past tense that something "is recorded" in a divider output file that does not yet exist | — |
| S14 | nitpick | completeness | No aggregate/node-level status format for a multi-level roll-up | B |
| S15 | nitpick | factual | `name: data-distiller-impl` diverges from the skill's eventual name without saying it is deliberate | B |

---

### S1 — `major` — nothing owns turning `index.md` into per-item pipeline runs

**Coverage.** The method's control flow is: decompose → *for each item, run the per-item
pipeline* → roll up. The middle clause has no owner.

- A's headline (line 65) is *"everything that happens to ONE item between **being handed to the
  method** and emitting its terse status line"* — passive. The hander is never named.
- A's exclusion list (lines 108–110) does not name it; B's exclusion list (lines 158–160) does not
  name it; neither ownership list claims it.
- §3.1's file layout (lines 185–186) enumerates exactly five roles — `decomposition/sizing`, `the
  blind roll-up coordinator` (B), `analyst; verification; merge` (A). **There is no role-prompt
  file for a run driver or a per-item pipeline driver.**

**Failure scenario.** The halves are planned blind. Either (i) both planners read the gap the same
way and neither plans a dispatcher — the merged plan builds a skill with an inventory, three
analyst prompts and a coordinator, and no step that connects them; or (ii) both plan one, and
`Union` (which discards nothing and keeps conflicts) yields two incompatible drivers with two
different iteration/concurrency stories. Neither is detectable from inside either half.

**This also swallows part of P2.** *"How independence is enforced (no shared context, no
visibility of a sibling's output)"* (line 71) is assigned to A, but independence is a **dispatch**
property: an analyst's own prompt cannot enforce that its caller did not hand it a sibling's
output. With no owner for dispatch, P2's enforcement mechanism has no home either. Nothing owns
fan-out limits when N analysts × M items is large.

**Not filed as `blocker`** because a competent B planner holding P7 (*"what it re-runs"*, line 130)
and the roll-up will probably plan a driver, so the likely outcome is duplication rather than
absence — and the post-`Union` red-team can see a duplicate. The cheap fix is one seam sentence
assigning the run driver (it is above the boundary: it needs `item.json` and item ordering, and
never a finding).

### S2 — `major` — the seam contradicts itself about `item.json`

- §3.2, line 215: *"No agent above the boundary opens a file under `items/<item_id>/` other than
  `item.json` and `STATUS`."* → above-boundary agents **may** read `item.json`.
- §3.4, line 246: *"B's coordinating agent may read this line and nothing else. It may not open
  `findings_path`, **any other file under `items/<item_id>/`**, or the corpus."* → the coordinator
  **may not** read `item.json`.

**Failure scenario.** B needs an above-boundary agent to read `item.json` for anything that
dispatches, re-runs, or reports locators (see S1, S6, P7). Under §3.4 that agent is forbidden;
under §3.2 it is permitted. B is explicitly forbidden to fix this — line 170: *"A half that
believes a seam element is wrong or missing files that as a finding in its own plan output — it
does not adjust it locally."* So B either files the finding and guesses, or plans a coordinator
that visibly violates a fixed seam rule. Both halves inherit the ambiguity identically, and it
bears directly on P5, the property the joint is built on.

**Fix belongs here, not downstream:** say which above-boundary role may read `item.json` (the
driver) and which may not (the roll-up coordinator).

### S3 — `major` — `findings_path` in the status line defeats P5's mechanism

**Fidelity.** B's brief (line 126) promises *"the structural rule that makes reading anything more
a **violation rather than a temptation**."* The seam then puts `findings_path` — *"path to A's
merged finding file"* (line 244) — **into the one line the coordinator is required to read**, and
follows it with a prohibition on opening it (line 246).

That is the definition of a temptation: the coordinator is handed the exact locator of the
findings and asked not to use it. The blindness property degrades from a structural guarantee to
prompt compliance, which is the weakest form available and the one the task's whole design
(*"a coordinating agent reads only a terse per-child status"*) exists to avoid.

**Failure scenario.** A coordinator agent under pressure to summarise a `state=partial` item has
the path in its context and a plausible reason; nothing but an instruction stops it, and no
artifact records that it looked. B cannot fix this — the STATUS schema is fixed and A "may not add
fields" (line 247), so neither half may remove one either.

**The cheaper structure was available:** `findings_path` is stated to be *"for the human, not for
the coordinator"* — so put it in a human-facing index (B's `index.md`, or a run-level results
file, cf. S7) and keep it out of the coordinator's input entirely. Then the prohibition is
structural: the coordinator never holds a path to any finding.

### S4 — `major` — the sub-tasks name no path to the seam they inherit

**Self-containment, at the document level.** Both sub-tasks list their source material by
**absolute path** — `Guarded_change/`, `Dragonfly/`, named stage files (lines 96–101, 146–152) —
except for the seam, which appears only as *"This seam (§3), which you inherit and may not
renegotiate"* (lines 102, 153). The sub-task bodies then reference `§3.2`, `§3.4`, `§3.5` a dozen
times. **No file path for §3 appears anywhere inside either sub-task.**

**Failure scenario.** `node.md` (lines 86–88) spawns two child nodes with `division.first` and
`division.second` as their `task`. If what is passed is the sub-task blockquote — which is what a
sub-task *is* — every `§` reference dangles, and `common.md` §2 forbids the recipient from hunting
for a substitute source (*"Do not go looking for a substitute source"*). The half then plans
without the item record, the status schema, the presence rule or the namespace partition — i.e.
without the entire seam — and its plan looks locally correct. **The recursion amplifies this:**
each half becomes a node that calls `Divisible` again, and its divider must carry the seam down to
grandchildren; nothing instructs it to.

**Fix:** inline §3 verbatim into both sub-tasks, or give its absolute path
(`.../Architect/runs/data-distiller/it3/0/split-round-1.md`, §3) in each sub-task's source list,
and state that the seam propagates unchanged to every descendant.

### S5 — `major` — `tier` and `size`'s unit are a plan-time producer/consumer dependency

§3.3 fixes the item record's **fields** but not their **value domains**:

- line 226: `size` — *"the item's measured size, **in the unit the Layer-2 config names**"*
- line 227: `tier` — *"the sizing tier this item fell into"*

Both are B's inventions: `sizing.*` is in **B's** namespace (line 257), and §3.5 line 260 says
*"Neither half reads, documents, or defaults a key in the other's namespace."* So A receives a
number in a unit it may not look up and a tier label from a vocabulary it has never seen.

**Failure scenario.** A must decide when an item will not fit an analyst's context (P2), and when
to emit `oversize-deferred` (line 240). To do that it must threshold on `size` or branch on
`tier`. Blind, A invents a tier vocabulary (`small|large`, or `fits|oversize`, or numeric levels)
and writes analyst-selection rules over it; B independently invents another; `Union` keeps both
and the built skill has two vocabularies for one field. This is precisely the failure the aiming
file names — *"a status vocabulary … any artifact one half is told to derive from the other's
plan … B will invent it and look locally correct"* — reproduced one level down, on `tier` instead
of on `state`.

**The divider already had the tool in hand:** it fixed `state`'s domain in the seam (line 240) and
did not fix `tier`'s. Fixing `tier ∈ {fits, oversize}` (or whatever the right pair is) and naming
the size unit costs one line and closes this.

### S6 — `major` — nobody owns what happens after `oversize-deferred`

`state` includes `oversize-deferred` (line 240), so the seam anticipates A discovering at read
time that an item is too big. But:

- A is forbidden to decompose — *"You do not own and must not plan: the decomposition of a corpus
  into items"* (line 108).
- B owns P1's over-size strategy (lines 120–122) but is given no trigger: B's roll-up reads status
  lines, and nothing says a `oversize-deferred` status causes re-decomposition, re-dispatch of the
  children, or anything at all.

**Failure scenario.** A run emits `oversize-deferred` for the three biggest items; the roll-up
faithfully reports them as deferred; those items are never analysed, and the run reports success
with a silent hole in corpus coverage. Alternatively B plans a re-decompose loop and A plans an
internal chunking strategy, and the merged plan has two contradictory over-size mechanisms.

This is the **one property whose control flow genuinely crosses the boundary in both directions**
(B → item → A → status → B → new items → A), and it is the one the seam specifies least. Either
close the loop in the seam (*"on `oversize-deferred`, B's driver re-invokes decomposition on that
item, producing children with `parent_item_id` set, and re-dispatches"*) or delete the state and
declare over-size purely a priori — but decide it here, since both halves inherit it.

### S7 — `major` — the run's corpus-level output is unowned

The task's purpose is *"extracting source-cited factual findings from a corpus"*. Trace the
artifact:

- A produces per-item merged findings under `items/<item_id>/` (§3.2, line 209).
- B's coordinator may not read them (line 246) and its output is *"a rolled-up structure of
  statuses"* (§1, line 44).
- §3.2's run-directory skeleton contains `index.md`, `decisions.md`, and `items/` — **no run-level
  results artifact.**

So no half is told to plan the thing the method exists to emit. **Failure scenario:** the built
skill finishes and hands the user a directory of per-item files plus a status tree, with no
assembled, cited, corpus-level answer, and no step in either plan is missing — the gap is between
them. B will document *"what a run produces"* in `METHODOLOGY.md` (the siblings both carry that
section — `Dragonfly/METHODOLOGY.md:141`, `Guarded_change/METHODOLOGY.md:154`), which means the
gap surfaces as a documentation step with nothing to document.

Note this is resolvable **without breaching blindness**: a run-level results file that is a
mechanical concatenation or index of A's per-item finding files, assembled by a step that no
coordinating agent reads, is still blind. It just needs an owner and a slot in §3.2.

### S8 — `minor` — B's headline forbids what B's P1 bullet requires

Line 117: *"This is the part of the skill in which **no agent ever reads corpus content**."* §1
line 50 restates it: *"on the other side no agent has ever read the corpus."* But line 121–122
says sizing and bounding *"read the corpus's **shape** (paths, sizes, **structural boundaries**
named in the Layer-2 config), never its meaning."* Finding a structural boundary — a message
break, a section header, a record delimiter — requires opening the file.

**Failure scenario.** B plans a decomposer that may only stat paths, so the over-size strategy
degenerates to byte-offset splitting that cuts items mid-record, and every citation in an affected
item inherits a truncated locator. Filed `minor` because B's own P1 bullet contains the
resolution; the headline is the imprecise one. The true boundary is *reads for meaning* vs *reads
for structure*, and saying so would also make the joint's claim more defensible, not less.

### S9 — `minor` — A must read a key in B's namespace

§3.5 line 260: *"Neither half reads, documents, or defaults a key in the other's namespace."*
`run.*` is B's (line 257). But §3.2 line 200 defines the whole run skeleton relative to `run.dir`,
and A writes `STATUS` and its per-item outputs inside it. A therefore must reference `run.dir`.
Harmless if noticed; a literal-minded A planner refuses and invents its own output root, and the
two halves write to different trees. One clause fixes it: *"`run.dir` is named in §3.2 and both
halves may reference it; it remains B's to document and default."*

### S10 — `minor` — coldness and read-only are fixed in common.md and also assigned to A

§3.6 fixes rule 1 (*"Every dispatched agent is **cold** — no shared context with its caller or its
siblings"*, line 269) and rule 3 (*"Agents that read corpus content are **read-only**"*, lines
271–272). §3.1 line 195 forbids a role file from restating a common rule. Yet A is told to own
*"how independence is enforced (no shared context, no visibility of a sibling's output)"* (line
71) and *"what 'read-only' concretely forbids"* (line 73).

The seam disambiguated this pattern **twice** — for citations (rule 4: *"common.md states the
duty, not the format"*) and for facts-not-interpretation (rule 7: *"Its enforcement … is A's"*) —
and did not do it for rules 1 and 3. Say the same thing for them, or A must choose between
violating additions-only and dropping a P2 deliverable.

### S11 — `minor` — `stages/common.md` is given a false sibling pedigree

Line 184 introduces `stages/common.md` as *"read verbatim by EVERY dispatched agent"*, and line
194 calls the additions-only discipline *"(house rule, and **the sibling skills' own**)"*.

Checked: **neither sibling has a `stages/common.md`** (`ls Guarded_change/stages/`,
`ls Dragonfly/stages/`; a grep for `common.md` across both trees returns nothing). What they have
is `stages/charter.md`, and it is read by the **red-team stages only**, not by every dispatched
agent — `Guarded_change/SKILL.md:40,43` and `Dragonfly/SKILL.md:43,46,49` attach it to specific
stages, and `Guarded_change/SKILL.md:49` describes the additions pattern loosely (*"stage 3 adds
the coverage-challenge…"*), never as a prohibition on restating.

The structural decision is fine and probably right, but B is explicitly instructed to check
itself against the siblings for house style (lines 146–152) and will find the claimed precedent
absent. State it as a deliberate improvement on the siblings, and B stops looking.

### S12 — `minor` — ownership resolutions that live only in §4

§4 is the divider's own coverage audit, not seam text, and it carries resolutions that appear
nowhere else — most importantly line 306: *"**A owns obeying the presence rule** for its own
files"*. A's sub-task text never mentions the presence rule, and A's exclusion list tells it not
to plan *"the restart/resume mechanism"* (line 110). A does inherit §3.2 (which states the rule
generally), so this is `minor` rather than `major`, but if the halves receive only their sub-task
plus §3, three of §4's ownership splits (P6, P7, P8) are not actually in force anywhere they can
read. Promote those clauses into §3 or into the sub-task bodies.

### S13 – S15 — `nitpick`

- **S13.** §6 line 342: *"This **is recorded** as a contradiction against `divider.md` in the
  divider's output."* Per `node.md:42` that output is `<run>/<node_id>/divide-<iter>.md`; the
  directory currently holds only `split-round-1.md` and one review. Present-tense claim about a
  file that does not yet exist — unverifiable at review time. (The *substance* of §6 is correct:
  I verified `combiner.md:6` — *"None of the three is an author"* — and `combiner.md:58` — *"A
  genuine conflict is kept, not resolved"*. The tension with `divider.md:79–83`, which offers
  `Union` deferral as a legitimate home, is real and the proposal resolves it the safe way.)
- **S14.** The task says *"per-**child** status"* and §1 line 47 gives B *"the whole corpus, **and
  the tree over it**"*, so the roll-up may be multi-level. §3.4 fixes the per-**item** line and
  says A may not add fields; nothing says B may define an aggregate/node-level status for
  intermediate levels. B owns both ends so it is B-internal, but one clause would prevent B
  reading §3.4 as the only permitted status format.
- **S15.** `name: data-distiller-impl` (line 179) sensibly avoids colliding with the installed
  `data-distiller` skill, but the divergence from the eventual name is never stated as deliberate.

---

## The six lenses

**1. Factual — findings: S11, S13 (S8 partly).** Earned with citations. Verified as **correct**:
every sibling path either sub-task points at exists — `Guarded_change/stages/charter.md`,
`Guarded_change/stages/stage-3.md`, `Dragonfly/stages/charter.md`, `Dragonfly/stages/stage-7.md`,
both `SKILL.md`, both `README.md`, `Dragonfly/METHODOLOGY.md`, `dragonfly.companion.md`,
`guarded-change.companion.md`. The `METHODOLOGY.md` sections B is sent to read all exist as
described: *why this exists*, *the loop*, *stage index*, *the two layers*, *the config contract
(Layer 2)*, *what a run produces* (`Dragonfly/METHODOLOGY.md:22,45,72,95,106,141`). Both siblings'
`SKILL.md` do open with `name`/`description` frontmatter and a router table, as claimed. The
`combiner.md` quotes in §6 are accurate (lines 6 and 58). `Data-Distiller-impl/` does not yet
exist, consistent with the plan creating it. **Wrong:** the sibling pedigree for `stages/common.md`
(S11) and the tense in §6 (S13).

**2. Logical — findings: S1, S2, S6, S8.** The reasoning for the joint is sound and the coverage
table is honest about the three properties that touch both sides. The defects are internal
inconsistencies (S2, S8) and a control-flow clause with no owner (S1, S6), not errors in the
argument for the cut.

**3. Missed opportunity — no finding rises above the alternatives noted here.** Three worth
recording: (a) the alternative joint **"the method (`stages/*`) vs. the envelope (`SKILL.md`,
`METHODOLOGY.md`, `README.md`, config)"** would have needed *no* pre-agreed vocabulary at all —
item record, status schema and tier domain would all be one planner's — at the cost of a thin,
possibly near-floor packaging half; the chosen cut is defensible and I prefer it, but it is the
cut that *forces* §3.3–§3.5 to exist, and that is worth stating in §1. (b) Removing `findings_path`
from `STATUS` buys P5 a structural guarantee for free (S3). (c) The divider fixed `state`'s value
domain in the seam and could have fixed `tier`'s in the same sentence (S5).

**4. Unstated assumptions & risks — findings: S1, S5, S9, S12.** Also assumed without saying so:
that the halves receive §3 at all (S4); that a run directory outside `Data-Distiller-impl/` is
acceptable house style when both siblings keep run artifacts *inside* the skill directory
(`Guarded_change/changes/`, `Dragonfly/hunts/`) — a deliberate and probably correct divergence,
but undeclared; and that `Union` will not need to reconcile anything, which §6 argues well but
which depends on S1/S5/S6 being closed first.

**5. Fidelity — finding: S3.** Terms pinned to mechanisms: **cold** → §3.6 r1, no shared context
with caller or siblings; **read-only** → §3.6 r3, writes nothing but its one named output;
**analyst** → an A-owned role prompt, N of them per item, N defaulted in `analysis.*`;
**verification** → a *separate* cold agent (line 74) that must re-open the corpus to resolve a
citation, hence correctly below the boundary; **agreement-ranked merge** → A-owned matching +
rank, surfaced as `max_agreement` in the status line; **decompose** → measured size, tiers, and
`parent_item_id` children for over-size items; **blind roll-up** → a file-access prohibition
(§3.2, §3.4). Every term pins to a real mechanism except **blindness**, which pins to a prompt
prohibition over a path deliberately placed in the agent's own input — mechanism replaced by
exhortation, on the one property the joint is built from. That is S3.

**6. Completeness — findings: S1, S6, S7, S14.** The structure's own required sections are all
present (joint, sub-tasks, seam, coverage check, floor check, self-containment audit). **Generative
sweep run.** I looked for: the run's terminal artifact (**missing → S7**); the dispatcher/traversal
and its concurrency story (**missing → S1**); the over-size feedback path (**missing → S6**); the
aggregate status format (**thin → S14**); error/abort handling above the boundary — what B's
roll-up does with `state=failed`, retry vs. escalate (**unassigned, but plausibly inside B's
roll-up; not filed**); a human-in-the-loop / stop section (**both siblings have one;
`Dragonfly/METHODOLOGY.md:172`, `Guarded_change/METHODOLOGY.md:198`; lands naturally in B's
entry surface, not filed**); corpus mutation between runs and `index.md` staleness (**inside B's
P1/P7, not filed**); test/eval and installation (**explicitly out of scope, §3.7 — correctly
handled**).

**Also in scope for every lens — was any portion of the task left unaddressed?** All eight
properties P1–P8 are assigned exactly once, and I confirmed each assignment against a named
mechanism rather than against §4's table alone. The unaddressed portions are not properties: they
are the **run driver** (S1), the **over-size return path** (S6) and the **output artifact** (S7).

---

## The four questions, answered directly

**1. Coverage.** P1–P8 are each owned exactly once and the three straddling properties (P6, P7,
P8) are split explicitly rather than left to inference — that part is genuinely well done. But
there are **three orphaned remainders that are not properties**: the run driver (S1), the
over-size return path (S6), and the corpus-level output (S7). No portion is double-claimed by
construction, though S1 is likely to be double-*planned*.

**2. The seam.** **Stated** — yes, in unusual and welcome detail. **Sound** — mostly, with one
internal contradiction (S2). **Self-contained** — **not yet, in two places.** The seam correctly
refuses the producer/consumer form for the item record, the status schema, the presence rule and
common.md, and correctly reframes the router table / stage index / config contract as build-time
rules over the merged plan (a legitimate use of `divider.md`'s third home, and executable given
`node.md:88`'s `Union`). But `tier`'s domain and `size`'s unit are still B-defines-A-consumes at
plan time (S5), and the seam **document itself has no path** in either sub-task (S4). Both are the
named failure class, at a smaller radius than the one the divider already fixed.

**3. The floor.** **Passed.** Neither half is near it. A plans ≥3 role-prompt files plus finding
and citation format references; B plans ≥7 files (`SKILL.md`, `METHODOLOGY.md`, `README.md`, the
worked config, `stages/common.md`, decomposition, roll-up). §5's count is accurate. The floor
passes down unchanged (§3.8). No finding.

**4. Real joint or arbitrary cut?** **Real joint.** What differs across the line: the *input* (corpus
content vs. structure and one-line statuses), the *output* (cited evidence vs. bookkeeping), the
*failure mode* (fabricated citation / smuggled interpretation vs. peeking coordinator / lost or
duplicated work on restart), and the *review criterion* (citation resolvability vs. idempotence).
The boundary is named by the task statement itself in P5, which makes it the one cut whose
existence is not the divider's invention. I would keep this joint. Its one imprecision — the line
is *reads for meaning* vs *reads for structure*, not *reads* vs *does not read* (S8) — narrows the
claim without undermining it.

---

## What I could not check

- The divider's own output file (`divide-<iter>.md`) does not exist yet, so §6's claim that the
  `divider.md`/`combiner.md` contradiction "is recorded" there is unverified (S13).
- Whether `node.md`/the divider passes §3 to each half alongside the sub-task text is not
  determinable from any file I hold; S4 is filed on the basis that the sub-task text does not make
  it so, which is the part under this proposal's control.
- Everything under `/home/zero/Desktop/claude-code-skills/Data-Distiller/` — fenced, not opened,
  and no claim in this review depends on it.
