# Cold split review — iteration 3, node 0, round 1, reviewer A

Reviewing the **proposed division** at
`Architect/runs/data-distiller/it3/0/split-round-1.md`. I hold no plan and was given none.

**Hard fence:** I did **not** read, list, grep, glob or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke
the installed `data-distiller` skill. Every shell command I ran was scoped to
`Guarded_change/`, `Dragonfly/`, or the Architect worktree.

---

## VERDICT — both parts

**Part 1 — what I found.** Six `major` findings, six `minor`, two `nitpick`. Every one of them is
about the **seam text**, not about where the boundary sits. Nothing I found requires the joint to
move; each remedy I name is an edit to §3.2–§3.6 or a sentence added to a sub-task's ownership
list.

**Part 2 — do I object to going forward with this cut? NO. I endorse this cut and I would keep
this joint.**

The boundary is the one the owner's own task statement drew — *"a blind roll-up in which a
coordinating agent reads only a terse per-child status"* — and §1 correctly identifies that P5 is
not a feature sitting on one side of the line but **the assertion that the line exists**. The two
populations have genuinely disjoint inputs (corpus content vs. metadata), disjoint outputs
(evidence vs. bookkeeping), disjoint failure modes (fabricated citation vs. lost/duplicated work)
and disjoint review criteria. That is a real joint, not a bisection for symmetry. **My findings
travel down with the sub-tasks; they are not an objection to proceeding.**

---

## Lens verdicts

| # | Lens | Verdict |
|---|---|---|
| 1 | Factual | **Clean on substance** (claims about the sibling skills check out — evidence below); one `nitpick` (N1) |
| 2 | Logical | **Issues found** — M4, M5, m2, m3 |
| 3 | Missed opportunity | **One issue** — folded into M6's remedy; otherwise clean, and §6's rejection of `Union` as a reconciliation site is correct |
| 4 | Unstated assumptions & risks | **Issues found** — M2, M5, m4 |
| 5 | Fidelity | **One issue, and it is my most serious** — M1 |
| 6 | Completeness | **Issues found** — M6, M2, m5 |

### Lens 1 — Factual: what I consulted, and what checked out

Earned with citations. I opened every source the proposal points its two halves at:

| Claim in the proposal | Checked against | Result |
|---|---|---|
| `Dragonfly/SKILL.md` and `Guarded_change/SKILL.md` are "frontmatter + router table" (§2-B) | `Dragonfly/SKILL.md:1-4` + the stage table at `:39-51`; `Guarded_change/SKILL.md:1-4` + `:34-45` | **Correct** |
| `Dragonfly/METHODOLOGY.md` has "why-it-exists, the loop diagram, the two layers, the config contract, what a run produces" (§2-B) | `Dragonfly/METHODOLOGY.md:22,45,95,106,141` — all five headings present | **Correct** |
| The companion files are "a worked Layer-2 config" and the config is "a YAML block inside markdown" (§2-B, §3.5) | `Dragonfly/dragonfly.companion.md:6ff`; `Guarded_change/guarded-change.companion.md:6ff`; the contract shape at `Guarded_change/METHODOLOGY.md:103-150` | **Correct** |
| `Guarded_change/stages/charter.md`, `stage-3.md`, `Dragonfly/stages/charter.md`, `stage-7.md` are "cold-reviewer prompts with citation discipline and an evidence bar" (§2-A) | `Guarded_change/stages/charter.md:9-30` (cold reviewer, five lenses, "cite line/file"); `Guarded_change/stages/stage-3.md:12-25` (cold subagent spawn + verbatim-record provenance rule); `Dragonfly/stages/stage-7.md:11-18` (each link cites `file:line`/log row) | **Correct** |
| "Additions-only discipline (house rule, **and the sibling skills' own**)" (§3.1) | `Guarded_change/stages/charter.md:1-6`: *"This is the ONE copy of the red-team charter's common core. Stage 3 and stage 6 both read it, then add their stage-specific bullets"* | **Correct as to the discipline** — see N1 as to the file |
| `Union` cannot be a reconciliation site; combiner.md forbids it (§6) | `Architect/stages/combiner.md:6` (*"None of the three is an author…"*) and `:58` (*"A genuine conflict is kept, not resolved."*), against `Architect/stages/divider.md:79-81` which offers "Deferred to `Union`" as legitimate home #2 | **Correct, and the contradiction it names is real.** This is good work by the divider and I confirm it independently |

I found no factual misstatement about the source material. The one thing I could not check is N2.

### Lens 5 — Fidelity: the terms I pinned

| Loaded term | Pinned to | OK? |
|---|---|---|
| "cold" | §3.6 rule 1 — no shared context with caller or siblings | yes |
| "independent" (P2) | §2-A — no shared context, no visibility of a sibling's output | yes |
| "read-only" | §3.6 rule 3 + §2-A ("what read-only concretely forbids") | yes (but see m3) |
| "verification pass" (P3) | §2-A — *a separate cold agent, not the analyst*, with an operational definition of "unverifiable" | yes |
| "agreement-ranked merge" (P4) | §2-A — matching rule + agreement definition + recorded rank | yes |
| "item" | §3.3's six-field record | partly — see M3 |
| "restart/resume" (P7) | §3.2's presence rule (write-`.tmp`-then-rename; existence ⇒ finished) | **no — M4** |
| "blind roll-up" (P5) | §3.4 — "may read this line and nothing else" + §3.2's above-boundary prohibition | **no — M1** |
| "facts, not interpretation" (P8) | §3.6 rule 7 as doctrine; §2-A owns "an enforceable rule rather than an exhortation" | yes |
| "skill" | a directory of markdown prompt files: `SKILL.md` frontmatter + router, `METHODOLOGY.md`, `README.md`, `stages/`, companion config | yes |

### Lens 6 — Completeness: the generative sweep was run

Beyond ticking the eight properties, I asked *"what load-bearing thing does an eight-property
checklist not anticipate?"* and looked specifically for: **the dispatch/fan-out step** (→ M2), **the
run's user-facing deliverable** (→ M6), **an intermediate level between item and corpus** (→ M6),
**failure and retry policy** (→ M4, M5), **path/locator validation** (→ m4), **the human-escalation
story** (→ m5), and **field types on the one wire format** (→ m1). Six of the seven turned up
something.

---

## The four questions

**Q1 Coverage** — the eight-property table in §4 is honest and each property does land on exactly
one owner. What it does not cover is the work that is not a property: **dispatch (M2)**, **the
response to `oversize-deferred` (M5)**, and **the corpus-level output (M6)**.

**Q2 The seam** — stated (thoroughly, §3.1–§3.8), and **self-contained in form** — I checked every
element against the producer/consumer failure `redteam-split.md:43-51` names, and found **no**
element of the shape *"A produces X at plan time and B consumes it"*. The `rule over the merged
plan` device (§3.1) is used correctly and is genuinely executable at build time. **But it is not
self-contained in substance in three places**: A cannot resolve its own write path or the units of
`size`/`locator` without reading a key §3.5 forbids it to read (**M3**) — a producer/consumer
dependency smuggled in through the namespace partition rather than through a file. **Sound?** No,
in the four ways M1/M4/M5/M6 describe.

**Q3 The floor** — **clean, no finding.** The floor is *one file with its content specified*. A
plans ≥3 role-prompt files plus a finding format and a citation format; B plans ≥7 files including
the whole entry surface. Neither half is remotely near the floor and neither is at risk of falling
below it. §5's own floor check is correct.

**Q4 Real joint or arbitrary cut** — **a real joint.** What differs at the boundary: what the agent
reads (corpus content vs. metadata and one-line statuses), what it produces (evidence vs.
bookkeeping), its unit of work (one item vs. the corpus), and its characteristic failure (a
fabricated citation vs. lost or duplicated work on restart). Crucially, the boundary was named by
the owner's task statement before any divider looked at it. I considered two alternative cuts —
by pipeline phase (decompose+analyse | verify+merge+roll-up) and by mechanism-vs-packaging
(`stages/` | entry surface + config) — and both produce a strictly larger and less natural seam.
This cut is better than its alternatives.

---

# Findings

## M1 — `major` — fidelity — the blind coordinator is handed the path it is forbidden to open

**Where:** §3.4, the status line format, field 6.

`findings_path` — *"path to A's merged finding file, **for the human, not for the coordinator**"* —
sits **inside the one line the blind coordinator is permitted to read**. §3.4 then implements
blindness as a prohibition: *"It may not open `findings_path`…"*.

P5 is the property that says a coordinating agent **never sees findings**. §2-B asks B for *"the
structural rule that makes reading anything more a violation rather than a temptation."* The seam
makes that impossible to deliver: it puts the temptation in the coordinator's only input and then
forbids acting on it. That is a **proxy** for the specified mechanism — an exhortation where the
task asked for structure — and it is the same substitution P8 is written to prevent one level down.

**Concrete failure:** B's roll-up plan is written blind. A coordinator holding
`item_042 done 0 17 0 <path>` has an anomaly (zero surviving findings, seventeen dropped), a path
in hand, and a prompt whose only barrier is a sentence. Either it opens the file — P5 breached with
no on-disk trace, because reading leaves none — or B's roll-up renders `findings_path` into its
output table, at which point the corpus-level roll-up is a document of paths into evidence the
roll-up is defined not to have seen.

**Remedy, inside the seam, joint unchanged:** drop `findings_path` from `STATUS` (five fields), and
have the human-facing pointer be derivable structurally — `items/<item_id>/<A's declared
merged-findings filename>` — recorded once in `index.md` or in B's roll-up-adjacent human index.
Then the coordinator is never given the path, and blindness becomes structural.

## M2 — `major` — coverage / unstated assumption — nobody owns dispatch

**Where:** §2-A's opening ("between **being handed** to the method"), §2-B's ownership bullets, §4.

The passive voice is doing load-bearing work. **No half is told it owns the step that spawns A's
per-item pipeline.**

- §2-A owns *"everything that happens to ONE item between being handed to the method and emitting
  its terse status line"* — the handing is outside its scope by construction.
- §2-B's ownership bullets are P1 (decompose/size), P5 (roll-up), P6 (config), P7 (resume), the
  entry surface, and `common.md`. **Dispatch appears in none of them.** §2-B's exclusion list does
  not mention it either.
- §1's table does say B's unit of work is *"the whole corpus, and the tree over it"*, and §4 says
  nothing. But §1 is the joint's justification; **the ownership bullets in §2 are what each half
  will act on.**

This is precisely *"a portion both halves assume the other owns"* (`redteam-split.md:39-41`).

**Concrete failure:** neither plan contains a step creating a dispatcher role-prompt file, or
specifying what arguments an analyst pipeline is invoked with, how many items run concurrently, or
what happens when a child returns nothing. `Union` cannot repair it — *"None of the three is an
author. You do not improve, rewrite, or adjudicate the material."* (`combiner.md:6`). The merged
plan therefore builds a skill in which nothing invokes an analyst, and it will look complete,
because each half's plan is internally coherent.

**Remedy:** one sentence in the seam. *"B owns the dispatch of A's per-item pipeline. B's
dispatcher hands A exactly: the absolute path to `items/<item_id>/`, and `config_path`. A's
pipeline begins on receipt of those two arguments."* (This also discharges half of M3.)

## M3 — `major` — seam self-containment — the item record does not let A locate or size anything

**Where:** §3.3 ("Exactly these fields; A may not require others, B may not omit any") against §3.5
("Neither half reads, documents, or defaults a key in the other's namespace").

Three concrete under-determinations, each of which A must resolve by invention:

1. **A cannot resolve where to write.** A's outputs live at `<run.dir>/items/<item_id>/` (§3.2).
   `run.dir` is a **`run.*`** key — **B's namespace**, which §3.5 forbids A to read. §3.3 carries no
   `item_dir` and no run root. A's plan must name the path its analyst writes to; blind, it will
   invent one.
2. **`locator`'s range has no unit.** *"an absolute path, plus an optional range within it"* — a
   range of what? Bytes, lines, characters, records, JSONL rows? A's analyst prompt must tell an
   agent how to read `<path>[1000:2000]`. B, choosing the unit, and A, interpreting it, are planning
   blind of each other.
3. **`size` is defined by reference to a key A may not read.** *"the item's measured size, in the
   unit the Layer-2 config names"* — that key is `sizing.*`, B's. A's tiering-adjacent logic and its
   own `analysis.*` defaults (e.g. how much an analyst is expected to read) cannot be stated against
   an unknown unit.

This is the producer/consumer failure `redteam-split.md:43-51` warns about, entering through the
namespace partition rather than through a file: *"B will invent it and look locally correct"* — here
it is A that invents, and A's plan will read perfectly.

**Remedy, inside the seam:** add `item_dir` (absolute) to §3.3; fix the range unit and the size unit
**in §3.3 itself** as literal values (e.g. *"`range` is inclusive 1-based **line** numbers or the
literal `whole`"*, *"`size` is in **bytes**, whatever unit `sizing.*` uses for tiering"*), so neither
half derives them from the other.

## M4 — `major` — logical — existence-only resume silently absorbs every failure

**Where:** §3.2's presence rule vs. §3.4's state vocabulary, and §2-B's *"using **only** the presence
rule the seam fixes (§3.2)"*.

§3.2 fixes: *"the existence of a file means the step that produces it finished. **Resume reasons
about existence only.**"* §3.4 fixes: `state ∈ done | partial | failed | oversize-deferred`.

These are incompatible. A `failed` item's `STATUS` file is **complete** — it was written atomically
with `state=failed` — so it exists, so an existence-only resume concludes the item is finished and
skips it.

**Concrete failure:** a run over 200 items loses 30 to a transient tool error; each writes
`STATUS` with `state=failed`. The operator restarts. B's resume, planned exactly as instructed,
reasons about existence, finds 200 `STATUS` files, and re-runs nothing. The run reports complete;
15% of the corpus was never analysed and nothing in the on-disk state distinguishes that outcome
from success. P7 as delivered makes failure **permanent** rather than **recoverable**, which is the
opposite of what "restart and resume" is for. `partial` has the same shape.

**Remedy, inside the seam:** amend §3.2 to *"Resume reasons about **existence, and — for `STATUS`
only — the `state` field**"*, and fix in the seam which states are re-runnable (`failed`, `partial`)
and which are terminal (`done`). Strike "only" from §2-B's P7 bullet. Note this does **not** breach
blindness: `state` is already a field B's coordinator may read (§3.4).

## M5 — `major` — coverage — `oversize-deferred` has an emitter and no consumer, and the over-size strategy straddles the boundary

**Where:** §3.4's state vocabulary vs. §2-B's P1 bullet vs. §2-A's exclusion list.

P1 — *"a strategy for over-size items"* — is **B's**, and §2-B constrains B to read only the corpus's
*shape*: *"paths, sizes, structural boundaries named in the Layer-2 config, never its meaning."*
§3.4 nonetheless gives **A** a state `oversize-deferred`, and §2-A forbids A from touching
decomposition: *"You do not own … the decomposition of a corpus into items."*

So A can declare an item over-size, and **no half is told what happens next.** Re-split? Escalate to
the human? Drop it? B's roll-up is told to read statuses, not to act on them.

**Concrete failure:** a 5 MB single-file log with no headings, no timestamps at line starts, no
structural delimiter the Layer-2 config can name. B, forbidden to read meaning, either splits it at
arbitrary byte offsets — cutting findings and their evidence across the item boundary, so no
analyst ever sees both halves of a fact and every citation to the seam is unverifiable at
verification — or defers it. A, which *can* see the content and could split it sensibly, is
forbidden to. It emits `oversize-deferred`. B counts the state into the roll-up. **The corpus
region is never analysed and the run reports success with a tally.** The task's explicitly named
contingency is half-implemented.

This is also the one place the joint's own premise is an **unstated assumption**: §1 and §2-B assert
that decomposition needs only shape. That is true for a directory of files; it is exactly false for
the single-large-blob case, and the seam contains no home for the content-aware bounding that case
needs.

**Remedy, inside the seam, joint unchanged:** name the consumer. Either (a) delete
`oversize-deferred` and require B's sizing to be conservative enough that A never overflows, with a
stated fallback; or (b) keep it and add one seam clause: *"an item whose `STATUS` reports
`oversize-deferred` is re-decomposed by B's over-size strategy into child items carrying
`parent_item_id`, and the run re-dispatches them; after K re-splits (a `sizing.*` key) the item is
escalated to the human."* Either resolves it; leaving it as-is does not.

## M6 — `major` — completeness — the fixed run skeleton has no corpus-level output and no level above the item

**Where:** §3.2's skeleton, which §3 declares fixed and unchangeable (*"Neither half may change
it."*).

The skeleton is exactly: `index.md`, `decisions.md`, and `items/<item_id>/{item.json, STATUS,
<A's per-item outputs>}`. Two things are therefore structurally excluded, and neither half may add
them.

**(a) There is no corpus-level findings deliverable.** The task's purpose is *"extracting
source-cited factual findings from a corpus"*. What a user gets from a completed run is: a status
roll-up, plus N per-item finding files they must assemble by hand. A owns per-item findings only
(§2-A). B may not read findings (§3.4). Nothing produces the artifact the method exists to produce.
This is **not** required by P5: blindness constrains what a *coordinating agent* may read; a
mechanical, non-agent assembly step (concatenate each item's merged findings under a heading, in
`index.md` order) reads nothing and violates nothing. The seam simply has no slot for it, and both
halves can correctly point at the other.

**(b) There is no level between item and corpus.** §1 says B's unit is *"the whole corpus, **and the
tree over it**"*; the task says *"a terse **per-child** status"*; the premise is *a corpus too large
for one context window*. But §3.2 has exactly one level and §3.4 declares the per-item line *"the
ONLY thing that crosses the boundary upward."* For a 5,000-item corpus the blind coordinator reads
5,000 lines into one context — **the coordinator becomes the scale failure the method was built to
avoid**, and it has nowhere on disk to persist an intermediate aggregate, so a roll-up interrupted
halfway restarts from zero (interacting with M4).

**Underlying both:** it is not stated whether §3.2's skeleton is **exhaustive** or **illustrative**.
If exhaustive, (a) and (b) are foreclosed. If illustrative, both halves may add run-directory files
blind and collide — the failure the fixed skeleton existed to prevent. The seam must say which.

**Remedy, inside the seam:** declare the skeleton exhaustive, and extend it with (i)
`<run.dir>/findings.md`, produced by a mechanical assembly step, assigned to B and written as a rule
over the merged plan (*"one section per item in `index.md` order, each embedding that item's merged
findings file verbatim"* — a rule, not a read), and (ii) an optional group level,
`<run.dir>/groups/<group_id>/STATUS` with the same line schema, so a multi-level blind roll-up is
representable without either half inventing it. **Missed opportunity, same place:** had §3.2 been
written as a *recursive node* skeleton (`nodes/<node_id>/{STATUS, children}`) it would have covered
the flat and nested cases identically at zero extra plan-time cost.

---

## m1 — `minor` — the one wire format has no types and a fragile delimiter

§3.4: *"Whitespace-separated fields, in this order: `<item_id> <state> <n_findings> <n_dropped>
<max_agreement> <findings_path>`"*. Three gaps, all fixable in place:

- **`findings_path` is last and whitespace-delimited.** §3.3 requires `item_id` only to be *"safe as
  a directory name"*, which permits spaces on every filesystem in use. One run directory or one item
  id containing a space and B's parser — written blind, split-on-whitespace, as instructed — mis-reads
  every field after it. Fix: constrain `item_id` to `[A-Za-z0-9._-]+` in §3.3 and declare the final
  field "the remainder of the line."
- **`max_agreement` has no type.** A owns what agreement *is* (P4). If A's merge expresses agreement
  as a fraction, A emits `3/5`; if as a count, `3`. B, planning blind, will write a roll-up that
  sorts or sums it. Fix: *"`max_agreement` is a non-negative integer count of analysts."*
- **No value is defined for a not-yet-run item.** Only `STATUS`'s absence marks that (§3.2), which is
  consistent — but say so, since B's roll-up must render it.

## m2 — `minor` — §3.5 forbids B to write the config it is told to write

§3.5: *"Neither half reads, documents, or defaults a key in the other's namespace."* §3.1 assigns B
`data-distiller.<example>.md` — *"one worked Layer-2 config for a named example corpus."* A worked
example is only worked if it carries values for `analysis.*`, `verify.*`, `merge.*` — A's namespace.
B must therefore either violate §3.5 or ship an example config that cannot run. The
rule-over-merged-plan device (§3.1) resolves the *execution*, but §3.5's prohibition is stated
without that carve-out and B will read it literally. Fix: add *"except in the worked example config
and the `METHODOLOGY.md` contract section, both written as rules over the merged plan."*

## m3 — `minor` — which A role writes `STATUS` is undetermined, and the obvious answer breaks a rule A may not change

§3.6 rule 3 (fixed, and A *"may not restate or modify"* it, §3.1): *"Agents that read corpus content
are read-only: they write nothing except their one named output file."* §3.4: `STATUS` is *"written
by A at the end of its pipeline."* The natural writer is the merge agent — which then writes two
files. A cannot fix this locally: it may only file it as a finding (§3, and it has no channel to B,
who owns `common.md`). Fix in the seam: name the writer explicitly — e.g. *"`STATUS` is written by
A's per-item pipeline driver, which reads only A's merged findings file and never corpus content;
§3.6 rule 3 does not bind it."*

## m4 — `minor` — nobody validates that a `locator` resolves

Both stated house precedents make this an explicit, gate-blocking rule:
`Guarded_change/METHODOLOGY.md:139` — *"**Paths are validated, not assumed.** Every path handed to a
cold reviewer … is mechanically checked to exist and be readable"* — reinforced at
`Guarded_change/SKILL.md:20-24` and `Dragonfly/SKILL.md:20` (*"Validate config paths at hunt start:
dead/unresolvable → stop"*). The division assigns it to neither half: B mints `locator` values from
corpus shape, A consumes them, and the only trace of a dead one is `state=failed` (which M4 then
absorbs). Fix: one clause in §3.3 — *"B validates every `locator` at decomposition time; an item
whose locator does not resolve is not written."*

## m5 — `minor` — no stop-for-human story, and its content spans the boundary

Both siblings carry a **Stop-for-human** section in `SKILL.md` (`Guarded_change/SKILL.md:54-73`,
`Dragonfly/SKILL.md:72-81`) and a **Human-in-the-loop** section in `METHODOLOGY.md`
(`Guarded_change/METHODOLOGY.md:198`, `Dragonfly/METHODOLOGY.md:172`). B owns both files, but most of
the conditions that should trigger a stop are A's knowledge: an item that cannot be read, verification
dropping every finding, N analysts with zero agreement, a config key missing. Neither half is told to
supply them, and it is not listed among §2-B's rule-over-merged-plan steps. Fix: add it to that list —
*"one row per stop condition declared by either half's plan."*

## N1 — `nitpick` — `stages/common.md` has no sibling precedent by that name

§3.1 mandates `stages/common.md`, *"read verbatim by EVERY dispatched agent, before its role file."*
Neither sibling has a `common.md`; both have `stages/charter.md`
(`Guarded_change/stages/charter.md`, 103 lines; `Dragonfly/stages/charter.md`, 90 lines), read at
selected stages — Guarded_change at stages 3 and 6 (`SKILL.md:40,43`), Dragonfly at stages 1, 4 and 7
(`SKILL.md:43,46,49`). The **additions-only discipline** the seam attributes to the siblings is
genuinely theirs (`Guarded_change/stages/charter.md:1-6`); the **file name and its universal scope**
are not. Since the task explicitly asks for a house-style check, either name it `charter.md`, or have
B note the deliberate divergence in `METHODOLOGY.md`.

## N2 — `nitpick`/unchecked — a forward reference I could not verify

§6: *"This is recorded as a contradiction against `divider.md` in the divider's output."* At review
time `Architect/runs/data-distiller/it3/0/` contains only `split-round-1.md`; no divider output
exists there yet. **Reported as unchecked, not as clean.** The contradiction it describes is real —
I verified it independently (`combiner.md:6,58` vs `divider.md:79-81`) — only the claim that it has
been recorded is unverifiable now.

---

## Restating the verdict, so it is not misread

**I do not object to going forward with this cut.** The joint is real, it is the one the owner's
task statement drew, and it is better than the alternatives I could construct. Six majors stand and
should travel down with the sub-tasks — but **every one of them is a defect in the seam's text,
repairable without moving the boundary by one line.** Reading them as disagreement would discard a
reviewer who is telling you the cut is right.
