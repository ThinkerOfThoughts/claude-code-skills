# Split review — round 2, reviewer B

Reviewing the proposed division in `Architect/runs/data-distiller/0/split-round-2.md` (driver plane
vs. worker plane). I hold the task and the granularity floor. **I hold no plan** and have judged the
cut against the shape of the task, not against any plan organisation. I did not read
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` (off limits) and did not read any sibling
reviewer's `split-review-*.md`.

**Verdict on the division: DIVISIBLE at approximately this joint, but not yet sound.** The joint
itself (accountability-for-termination vs. accountability-for-trustworthiness) is real — see Q4. The
shared interface I1–I10 that carries it is not: it has one orphan with no owner, and several closed
sets that forbid both halves from supplying what the interface itself requires.

---

## Summary of findings

| # | Severity | One line |
|---|---|---|
| B-F1 | **blocker** | `status.json` — the object the whole blind roll-up and the whole resume story rest on — has no writer in either half. |
| B-F2 | **major** | I8's closed six-key config set is unusable: `decompose` may not read `corpus_root`, there is no key for the fit threshold, and no key for where a run is written. |
| B-F3 | **major** | I2's *"contains exactly these rules"* closure contradicts sub-task two's own ownership grant and forecloses rules the interface needs. |
| B-F4 | **major** | The worker's return summary is an unpoliced channel from findings straight into a driver-plane agent's context; the blindness is structural only on disk. |
| B-F5 | **major** | `stages/node.md` (half one) must include verbatim a `common.md` (half two) written for a role the node is not, and may not modify it. |
| B-F6 | **major** | The `split` over-size strategy straddles the cut: sub-item creation, manifest mutation and re-dispatch are owned by neither half. |
| B-F7 | **major** | Half one is told the worker files' one-line purposes are "fixed below". They are not fixed anywhere, and half one must publish them in two index tables. |
| B-F8 | **major** | What was *not* analyzed has no route to the deliverable: `sample` must "record the omission" and no interface object carries it. |
| B-F9 | minor | "Both siblings' precedent" is false for the cold-start guard, and the shared METHODOLOGY section shape includes a Dragonfly-only section. |
| B-F10 | minor | Restart/resume is placed "in full" in `stages/node.md` while the invoking agent's run loop lives in `SKILL.md`. |
| B-F11 | minor | The "disjoint failure sets" argument is false on its own terms — "steered" is listed as a worker-plane failure while the anti-steering barrier is wholly driver-plane. |
| B-F12 | minor | "Indivisible" was not weighed among the alternatives, and the real cost of dividing (three-leaf `Consensus` traded for two-child `Union`) is never named. |

---

## The four questions

### Q1 — Coverage

Mapping each of the task's eight defining properties to an owner: decompose/size/strategy → half two
(`stages/decompose.md`); N cold analysts → half two (`analyst.md`) dispatched by half one; cold
verification → half two (`verify.md`); agreement-ranked merge → half two (`merge.md`); blind roll-up
→ half one (`node.md` + I3/I5); per-corpus config → half one (I8, METHODOLOGY skeleton, worked
instance); restart/resume → half one (`node.md`); facts-not-interpretation → half two
(`common.md`, I2). The "skill invokable by name" framing property → half one (`SKILL.md`
frontmatter + the install step). Every property has a nominal owner.

Three things fall through anyway: **B-F1** (the status record has no writer), **B-F6** (the `split`
strategy's mechanism), and **B-F8** (the omission record). Each is a case of the pattern the
round-2 rewrite was meant to eliminate — an object that crosses the cut and that the divider named
without assigning a producer.

### Q2 — The seam

The seam **is** stated, at length, and non-directionality is a genuine repair of round 1's defect —
I confirmed independently that `Architect/stages/node.md:50-53` spawns both children with the same
incoming `plan` and merges with `Union`, that `Architect/stages/leaf.md:18-20` gives a leaf only
`(task, plan, granularity)`, and that `Architect/stages/combiner.md:57-61` keeps conflicts rather
than resolving them. There is no channel for a directional contract, and this round does not need
one.

But the seam is not sound. Its load is carried entirely by I1–I10, and I1–I10 contain: an object
with no producer (B-F1), two **closed sets** that cannot supply what the halves are required to do
with them (B-F2 on I8, B-F3 on I2), a cross-role file assignment that is incoherent for the role
that must consume it (B-F5), and a promise of content that is not delivered (B-F7). The seam is
also leaky in the one place the task cares most about (B-F4).

### Q3 — The floor

**No finding.** The floor is "one file created or one coherent edit to one file, with the content
that goes in it specified." Half one is five files plus an install step; half two is five files.
Both are several times the floor and both are coherent whole tasks. Neither half falls below it,
and neither is at it, so both can divide again. The divider's floor check is correct as stated.

### Q4 — Real joint or arbitrary cut?

**Real joint, imperfectly argued.** Something genuine changes at this boundary and I can name it
without relying on the divider's phrasing: the driver-plane files are read by an agent that
*already holds the run's context and decides what happens next*; the worker-plane files are read by
an agent whose entire context is that file plus a handed path, that does one pass and cannot
observe anything else in the run. That is a difference in the *reader's information state*, and it
determines what each file may assume — which is the strongest form of a joint a prompt-file skill
can have.

The divider's own argument for the joint is weaker than the joint is. It claims two "disjoint
failure sets" and then lists **"steered"** on the worker side (`split-round-2.md:326`) — steering is
exactly what the blind-roll-up barrier prevents, and that barrier is assigned wholly to the driver
side (`:117-121`). The sets are not disjoint by the divider's own enumeration (**B-F11**). The
correction is available and cheap: the property is not "which failure set" but "what the reader can
see."

I also confirmed the divider's factual grounds for *abandoning* round 1's reader-based joint:
`Guarded_change/stages/stage-5.md:7` ("Implement per the plan, including any instrumentation the
plan added.") and `Guarded_change/stages/stage-1.md:8` are the invoking agent's own procedure, not
prompts for a dispatched agent. That claim checks out.

---

## The six lenses

### 1. Factual — NOT CLEAN (one minor)

Citations I opened and confirmed: `Dragonfly/SKILL.md:22` is indeed `## Before you start:
cold-start guard`; `Guarded_change/SKILL.md:25-52` is the `## Loop` section through the iteration
cap; `Dragonfly/SKILL.md:29-70` is its `## Loop` through the incidental-findings rule;
`Guarded_change/METHODOLOGY.md:103-152` is `## The config contract (Layer 2)` with the annotated
YAML skeleton inline, and `Dragonfly/METHODOLOGY.md:106-131` likewise;
`Guarded_change/METHODOLOGY.md:88-100` and `Dragonfly/METHODOLOGY.md:95-102` are both `## The two
layers`; `Guarded_change/METHODOLOGY.md:143` does name which copy of a rule is operative
("...lives written-in-full in `stages/stage-3.md`, `stages/stage-4.md`, and `stages/stage-6.md`");
`Guarded_change/guarded-change.companion.md` and `Dragonfly/dragonfly.companion.md` both exist and
both are worked instances pointing at METHODOLOGY for the contract
(`dragonfly.companion.md:3-4`); `Guarded_change/stages/charter.md:1-14` and
`Dragonfly/stages/charter.md:1-12` are both cold-agent prompts; both siblings carry a top-level
`README.md`. The alternatives-weighed section's lopsidedness claim for the two-layer cut is
consistent with what I see on disk.

**B-F9 — minor — two "both siblings" claims are one-sided.**
`split-round-2.md:87` calls the cold-start guard "both siblings' precedent" and cites only
`Dragonfly/SKILL.md:22`. `grep -rn "cold-start" Guarded_change/` returns **no matches** anywhere in
Guarded_change — the guard is Dragonfly-only. Likewise `split-round-2.md:95-100` gives the
METHODOLOGY section shape as what "both siblings share" and includes *Trigger*:
`Dragonfly/METHODOLOGY.md:161` has `## Trigger`, and `Guarded_change/METHODOLOGY.md` has no such
heading and no occurrence of the word. Neither is a reason to drop the section from Data-Distiller's
`METHODOLOGY.md`, but half one will be handed the claim as a premise and cannot check it against a
partitioned source list — it can, because the sources are not partitioned, which is the round-1 fix
working. Fix the attribution, keep the sections.

### 2. Logical — NOT CLEAN

**B-F6 — major — the `split` strategy straddles the cut and neither half owns its mechanism.**
I6 defines `split` as *"divide the item into sub-items and recurse."* Sub-task two owns
strategy-selection but is barred from specifying "how workers are dispatched, in what order, or at
what fan-out" (`:246`). Sub-task one's `node.md` carries "the recursion (how a node decides between
spawning child nodes and dispatching workers)" (`:104`) — that is the *roll-up* tree's recursion,
not item subdivision. Concretely unanswered by both halves: who creates the sub-items when a
manifest entry says `strategy: split`; whether a second `decompose` pass is dispatched on that item
or the first pass already emitted the sub-items; whether `<run>/manifest.json` is rewritten and by
whom; and how a sub-item is related to its parent, since I4's entry has no parent field and I3's
`<run>/items/<item_id>/` layout is flat with no nesting. **Failure scenario:** an item is 10× a
context window; decompose marks it `split`; the driver reads `strategy: split` from the manifest and
has no procedure for it, while `decompose.md` was told selection is its job and dispatch is not.
The run stalls on that item, or the item is silently analyzed whole and the "does not fit" property
is unimplemented. Restart makes it worse: a resumed run reading a manifest that may or may not have
been rewritten cannot tell which state it is in.

**B-F10 — minor — resume is placed in the file that may not be the one running on restart.**
Sub-task one item 3 puts "the restart/resume decision procedure **in full**" in `stages/node.md`
(`:105-107`), while item 1 puts "the run loop — the procedure the driving agent executes" in
`SKILL.md` (`:90-94`) and lists no resume step among `SKILL.md`'s sections. The ownership line
(`:117-118`) distinguishes "both the invoking agent's and a node's" control flow, so the two are not
the same agent. A run restarted by re-invoking the skill enters through `SKILL.md`, which as
specified walks a fresh run loop. Repairable wholly inside half one, hence minor — but as written
the sub-task points its planner the wrong way.

**B-F11 — minor — the seam's "disjoint failure sets" argument is self-refuting.** See Q4. The joint
survives; the argument for it needs replacing, and since the sub-task texts do not carry the
argument, the cost is that a plan reviewer inherits a joint with no valid justification on record.

### 3. Missed opportunity — NOT CLEAN

**Move `stages/common.md` to the driver plane.** This is the cheapest available repair and it
dissolves two of my majors at once. `common.md` is the one file both planes are accountable for: it
is included verbatim by `node.md` (half one, `:107`) *and* by all five worker files (half two,
`:215`). Its rule set is already fixed by the divider (I2), so half two's authorship of it adds no
information the interface does not already contain — but half two's brief (`:206-210`) describes its
readers as agents that do "one bounded pass over the corpus... and return", which is not the node.
Placing `common.md` with `node.md` puts the file with the half that must reason about *both* its
readers, and lets I2 be relaxed from a closed list to a floor (see B-F3). Counts stay balanced at
6/4 files or, if `README.md` moves the other way, 5/5.

**B-F12 — minor — "indivisible" is absent from the alternatives.** Three alternatives are weighed
(`:348-370`) and none of them is *not dividing*. The redteam-split brief treats "this task is
indivisible" as a live answer, and the divider's own floor check only establishes that the halves
*can* divide, not that the whole *must*. The unnamed cost is specific: `Architect/stages/node.md:44-53`
gives a floor task to **three** leaves and takes `Consensus` (2-of-3 including order,
`combiner.md:20-24`), but gives a divided task to **two** children and takes `Union`, which
"DISCARD[S] NOTHING" and never counts (`combiner.md:37-41`). Dividing therefore buys parallelism at
the price of *all* corroboration on the whole-task plan: no step of the final plan will ever have
been independently written twice. For an 11-file artifact that is plausibly the right trade — I am
not claiming the task is indivisible — but it is a trade the alternatives section never states, and
the round-3 budget is one round.

### 4. Unstated assumptions & risks — NOT CLEAN

**B-F4 — major — the return channel defeats "structural" blindness.**
I3 (`:164-166`, restated `:282-284`) claims blindness is structural because "a driver-plane agent is
handed `manifest.json` and `status.json` paths only." I5 (`:175-176`) forbids finding text in the
status record. Both concern **on-disk** artifacts. But I2 (`:152-153`) fixes the worker's contract
as *"write to the path you were handed, **return that path plus a short summary**"* — and the
recipient of that return value is the agent that dispatched the worker, which on the driver's own
control flow (`SKILL.md`, `:92-94`: "per item dispatch analysts → verify → merge") is a driver-plane
agent. **Failure scenario:** an analyst returns "wrote `analyst-2.md`; the strongest finding is that
the vendor was notified on 3 March, cited at log line 41,022." That is a claim and a citation
arriving in the coordinator's context, unpoliced, by the contract's own words. The node's
expectations are now steered by exactly the mechanism the task's blind-roll-up property exists to
prevent. Neither half owns the fix: I5's prohibition is scoped to `status.json`, half two writes the
return contract but is told nothing about blindness, and half one is barred from changing I2.

**B-F5 — major — `node.md` must include verbatim a file written for a role it is not.**
Sub-task one (`:107`): `stages/node.md` "includes `stages/common.md` verbatim... and does not
restate its rules." Sub-task two (`:206-210`) tells the author of `common.md` that it is writing for
"dispatched cold agents, each of which does one bounded pass — over the corpus, or over artifacts a
previous pass produced — and returns." I2's fixed rules include *"cold independence (no shared
context with the dispatcher or with siblings)"*, *"read-only over the corpus"*,
*"cite-or-it-doesn't-count"* and *"facts, not interpretation"*. A node **is** a dispatcher, never
touches the corpus, and produces no findings to cite. Two cold agents will resolve this
incompatibly and cannot consult each other: half two writes a worker-only `common.md` (its brief
says nothing about coordinators) and half one includes it verbatim in a coordinator prompt it may
not modify. The unstated assumption is that "every dispatched agent" and "every worker" are the same
set; the division itself makes them different.

**Unstated and worth flagging: whether the invoking agent reads `common.md` at all.** I2 binds
"every dispatched agent." The root driver is invoked by a human, not dispatched. Nothing says
whether the off-limits enforcement and read-only rules bind it. Half one owns its control flow, so
it can decide — but the interface is silent where it sounds complete.

### 5. Fidelity — NOT CLEAN

Pinning each loaded term in the task to the concrete mechanism this division assigns:

| Term | Pinned to | Verdict |
|---|---|---|
| "decompose … size … pick a per-item strategy" | `stages/decompose.md` emitting I4 manifest entries with `size`, `fits`, `strategy` from I6's name set | selection pinned; **execution of `split` unpinned — B-F6** |
| "N independent cold analyst agents" | N = `analysts_per_item` (I8); N dispatched agents each writing `<run>/items/<id>/analyst-<k>.md` (I3); independence argued in `analyst.md` (`:222-224`) | pinned, but the layout co-locates siblings' outputs and I2 is closed against a "do not read your siblings' files" rule — see B-F3 |
| "read-only over the corpus" | a rule in `common.md` (I2) | pinned |
| "cites a source for every finding" | I7 `citation` = "a corpus locator a verifier can re-open" | pinned — the re-openability requirement is the real mechanism, not a proxy |
| "a cold verification pass that re-checks every citation" | `stages/verify.md`, dispatched cold under `common.md`, re-opens **every** citation, drops the unverifiable, writes `verified.md` | pinned |
| "ranks … by how many independent analysts agreed" | I7 `agreement_count`, set by `merge.md`; half two must state agreement-across-wording and roll-up semantics | pinned |
| "blind roll-up … only a terse per-child status" | I3 path-handling + I5 field prohibition + node procedure | **proxy, not mechanism — B-F4** (on-disk only) and **unwritable — B-F1** |
| "per-corpus configuration file … method stays corpus-agnostic" | I8 key set + I10 + METHODOLOGY skeleton + worked instance | **key set cannot carry the job — B-F2** |
| "restart and resume from on-disk state" | `node.md` reads `status.json`/`manifest.json` and decides what to redo | **rests on an unwritten file — B-F1**; misplaced — B-F10 |
| "facts, not interpretation" | a rule in `common.md` (I2) | pinned |
| "a skill … invokable by name" | `SKILL.md` YAML `name: data-distiller` + presence at `~/.claude/skills/data-distiller/` + live==source | pinned |

The two that are proxies rather than mechanisms are the blind roll-up (a path-handling convention
with an open return channel) and resume (a procedure over a file nobody writes).

### 6. Completeness — NOT CLEAN

I checked the structure's own required sections — both sub-task texts have scope, an exclusion list,
a file list, a source-material list with the off-limits restriction, and a verbatim I1–I10 — all
present in both.

**The generative sweep.** I asked: *what load-bearing thing does an interface of ten fixed objects
plus two file lists not anticipate?* I looked for (a) an object named in the interface with no
producer; (b) a set declared closed that its consumers cannot live inside; (c) a piece of content
promised by one half's text and supplied nowhere; (d) a record of what the run did **not** do; (e)
an audit/decision log, since both siblings have one. Four of the five hit.

**B-F1 — blocker — `status.json` has no writer.**
I5 (`:172-176`) fixes the status record's fields, including `counts` = "findings produced / findings
surviving verification / findings in the merged output". I3 makes it exist at
`<run>/items/<item_id>/status.json` and `<run>/rollup/<node_id>/status.json`. **No file in either
half's list is assigned to write it.** Half two's five files are enumerated with their outputs
(`decompose.md` "Emits the item manifest"; the rest write findings/verified/merged artifacts) and
`status.json` appears in neither the file list nor the ownership paragraph (`:237-241`). Half one
claims "the on-disk run-state layout" (`:118`) and reads the status record (`:106-107`), but is
forbidden by I3 from being handed any findings path — so it has no source for `counts`, which can
only be known by reading `analyst-*.md`, `verified.md` and `merged.md`.

The only escape is the worker's return summary carrying counts upward — and I2 declares `common.md`
"contains **exactly** these rules", a list with nothing about reporting counts. So the escape is
also closed. **Failure scenario:** every item completes; `<run>/items/*/status.json` is never
written by anyone; the node has nothing to read; the roll-up cannot proceed and a restarted run
cannot tell a finished item from an unstarted one. Two of the task's eight defining properties —
blind roll-up and resume-from-on-disk-state — are unimplementable, and this is invisible to both
planners because each can reasonably read the other as the owner. This is the round-1 blocker class
(an object crossing the cut with no producer) recurring on a different object.

**B-F2 — major — I8's closed config key set cannot support what the halves must do with it.**
I8 (`:186-188`) fixes the Layer-2 keys as `corpus_root`, `item_definition`, `off_limits`,
`concurrency_ceiling`, `analysts_per_item`, `oversize_strategies`, requires half one to "document
and validate all of them", and restricts worker-plane files to reading "only `item_definition` and
`off_limits`". Three concrete failures:

1. **`decompose.md` cannot reach the corpus.** It is a worker-plane file, so by I8 it may read
   `item_definition` and `off_limits` — but not `corpus_root`. It cannot enumerate a corpus whose
   root it may not read. Nothing in either half's text says the driver hands a resolved root down as
   an argument, and I3's `config.snapshot.md` would be the worker reading config keys by another
   route, which I8 forbids.
2. **There is no key for "fits".** I4 requires a measured `size` and a boolean `fits`, and half two
   must "decide whether it fits one context window" (`:217`). The threshold is model- and
   corpus-specific — exactly the class of value I10 and "the method stays corpus-agnostic" say
   belongs in Layer 2 — and I8 has no key for it. Half two must hardcode a number into a
   corpus-agnostic prompt file and half one cannot add the key.
3. **There is no key for where a run is written.** `<run>` is used throughout I3 and never defined.
   `Dragonfly/METHODOLOGY.md:122-123` makes `ledgers.dir` a config key precisely so the artifacts
   survive a session restart (`:133`), and `dragonfly.companion.md:33-35` instantiates it. Resume is
   a named property of this task; the run root is the first thing a resume needs.

Secondary observation in the same lens: both siblings' config contracts carry a **priority-ordered
`redteam_context`** whose stated reason is that *"a cold subagent cannot read a large tree
exhaustively"* (`Guarded_change/METHODOLOGY.md:110-113,135-138`; `Dragonfly/METHODOLOGY.md:111-114,
128-130`). Data-Distiller's founding premise is a corpus too large for one context window analyzed
by cold subagents — the same problem, in a stronger form. I8 has no analogue and is closed against
one.

**B-F3 — major — I2's "exactly these rules" closure contradicts sub-task two and forecloses needed
rules.** I2 (`:149-154`) says `common.md` "contains **exactly** these rules". Sub-task two (`:238-239`)
grants that half ownership of "the evidentiary discipline (independence, read-only,
cite-or-it-doesn't-count, facts-not-interpretation) **and where each rule sits between `common.md`
and a role file**." I2 has already decided where all four sit. The half is handed a decision and
told it owns it. Concretely foreclosed by the closure: a rule that an analyst must not open its
siblings' co-located `<run>/items/<id>/analyst-<k>.md` files (the layout puts them in one directory
and I3 is the divider's, not half two's); a rule that the returned summary carries no claim text
(B-F4); a rule that the returned summary carries counts (B-F1). Role files are "additions only"
(`:234`), which is a partial escape for the first of these but not for the second and third, since
the return contract is a common rule. Either I2 becomes a **floor** ("at minimum these rules") or
those three rules must be added to it by the divider.

**B-F7 — major — content promised by the interface and not supplied.** Sub-task one (`:129-130`):
half one "may name those files and their one-line purposes **(fixed below)** and rely on the rules
the shared interface guarantees they contain." I1 (`:145-147`) fixes only the six **filenames** and
a plane label. No one-line purposes appear anywhere in I1–I10. Yet half one must write
`SKILL.md`'s "stage/role index table listing every file under `stages/` … with a one-line purpose
and its path" (`:93-94`) and `METHODOLOGY.md`'s *Stage/role index* (`:97`) — both user-facing, both
in the house shape (`Guarded_change/SKILL.md:34-45`, `Guarded_change/METHODOLOGY.md:67`). Half two's
own one-line descriptions exist (`:215-232`) but live only in sub-task two, which half one never
sees. **Failure scenario:** `SKILL.md`'s index says `verify.md` — "re-check citations"; half two's
`verify.md` also owns "what happens when nothing survives" and the drop record; the two descriptions
diverge, and the `Union` combiner keeps both without flagging it (`combiner.md:37-41` dedups only
exact restatements). This is the same class as B-F1: an object crossing the cut that the round-2
thesis says is fixed here, and is not.

**B-F8 — major — the record of what was *not* analyzed has no route to the deliverable.**
I6 defines `sample` as "analyze a stated subset and **record the omission**". Where? I7's finding
record has no field for it and `verify.md` "re-opens every citation and **drops the unverifiable**"
— an omission note is not a citable claim, so it is at risk of being dropped by the very pass meant
to make the output trustworthy. I5 forbids the status record from carrying claim text, and its
`counts` are counts of findings only. `<run>/FINDINGS.md` is produced by `merge.md` at the root
(I9), which sees merged findings, not coverage. So a run that sampled 5% of its largest item can
hand the human a `FINDINGS.md` with no indication of it. Half two "must state … what an analyst
does when its item's strategy is `window` or `sample`" (`:224`) but owns no channel that survives
verify and merge; half one is accountable for "handing the human a result" (`:80`) but may not read
findings and has no coverage artifact to hand over instead. Related and from the sweep's item (e):
I3's layout has **no `decisions.md`-equivalent**, though both siblings make one load-bearing
(`Guarded_change/METHODOLOGY.md:175-180`, `Dragonfly/SKILL.md:33`) — which is also the natural home
for a coverage record, for which items were throttled by the ceiling, and for what a resume chose to
redo.

---

## What I could not check

- Whether `Architect/stages/combiner.md` line numbers cited by round-1's reviewer C (`:57-64`) match
  what I read — I read the file and confirmed the *substance* (conflicts preserved, nothing
  discarded) at `:37-41` and `:57-64`; I did not verify reviewer C's exact span, and per the brief I
  did not open any `split-review-*.md`.
- The round-1 disposition table is the divider's claim. I spot-verified two rows against the
  sources (the reader-based-joint row, via `Guarded_change/stages/stage-1.md:8` and
  `stage-5.md:7`; and the source-material-partitioning row, which both sub-tasks now honour) and
  found both accurate. I did not verify the remaining rows.
- I did not open `/home/zero/Desktop/claude-code-skills/Data-Distiller/` in any way.

## If only three things are fixed in round 3

B-F1 (assign a writer to `status.json`, which most likely means adding a counts-and-no-claims clause
to I2's return contract), B-F2 (open I8, or at minimum add a corpus-root hand-down, a fit threshold,
and a run root), and B-F5 (move `stages/common.md` to the driver plane, which also relaxes B-F3).
B-F4 rides along with the I2 repair; B-F6, B-F7 and B-F8 each need an interface object that does not
exist yet.
