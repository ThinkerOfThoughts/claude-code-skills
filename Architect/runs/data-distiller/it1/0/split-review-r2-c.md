# Split review — round 2, reviewer C

**Reviewing:** the proposed division at
`/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/0/split-round-2.md`
(driver plane vs. worker plane, with a non-directional shared interface I1–I10).

**Inputs I actually had:** the task, the granularity floor, the division file, and Architect's own
`stages/{common,divider,node,leaf,combiner,redteam,redteam-split}.md`. **No plan** — correct, the
divider had none either.

**What I did not read, by instruction:** `Data-Distiller/` (off limits) and the sibling reviewers'
`split-review-*.md`. One consequence is flagged as unchecked below (N3).

**Bottom line: the cut is plausible and its diagnosis of round 1 is correct and independently
verified — but the interface it substitutes has three gaps that cannot be executed as written, and
the joint it claims is not the joint it demonstrates.** The division is not yet sound.

---

## Verdict per lens

| Lens | Verdict |
|---|---|
| Factual | **Issues found** — 2 citation-backed errors about the siblings (F11), 1 arithmetic inconsistency (N1). The round-2 claims about `Architect/stages/*` and about the siblings' `stages/` files being the invoking agent's own procedure are **verified correct**. |
| Logical | **Issues found** — F9 (the stated joint's failure sets omit the barrier's own failure mode), F6, F10. |
| Missed opportunity | **Issues found** — F8 (a narrower seam existed and was not weighed; the interface designs inside one half). |
| Unstated assumptions & risks | **Issues found** — F1, F2 (both assume a dispatch channel and a corpus-access route the interface never grants), F7. |
| Fidelity | **Issues found** — F4 (blindness pinned to a proxy), F5 (independence pinned to an assertion). Pinning recorded below. |
| Completeness | **Issues found** — F3 (no producer for the one artifact the barrier rests on), F10. Generative sweep run; what it looked for is recorded below. |

### Fidelity pinning (what each loaded term was pinned to, and whether the division implements *that*)

- **"cold"** → pinned to I2's "no shared context with the dispatcher or with siblings" in
  `stages/common.md`, included verbatim at dispatch. **Implemented** as an instruction; enforcement
  is a dispatch property — see F5.
- **"N independent analysts"** → pinned to sub-task two item 3 (`:222-224`), which requires
  `stages/analyst.md` to *state* what makes them independent. **Proxy.** See F5.
- **"cold verification pass ... re-checks every citation"** → pinned to `stages/verify.md`
  (`:225-227`), "re-opens **every** citation". Re-opening requires corpus access, which I8 denies.
  **Not implementable as scoped.** See F2.
- **"a merge that ranks by how many analysts agreed"** → pinned to `stages/merge.md` (`:228-232`) +
  I7's `agreement_count`. **Implemented.**
- **"blind roll-up ... never reads the findings themselves"** → pinned to I3's "handed
  `manifest.json` and `status.json` paths only" (`:164-166`). **Proxy.** See F4.
- **"decompose ... size them ... pick a per-item strategy"** → pinned to `stages/decompose.md`
  (`:216-219`) + I4 + I6. **Partially implementable** — I4 cannot represent `split`'s output. See F6.
- **"restart and resume from on-disk state"** → pinned to sub-task one item 3 (`:101-107`), "the
  restart/resume decision procedure in full". **Incomplete** — the trust decision has no owned
  write-order rule. See F3b.
- **"seam"** → pinned to I1–I10, "every object that crosses the cut is fixed here by the divider."
  Two of the ten objects do not cross the cut. See F8.

### Generative sweep (completeness) — what I looked for

For each artifact named in I3 I asked: *who creates it, from what inputs, in what order, and who may
read it?* For each dispatched role I asked: *what is it handed at spawn time, and which file has the
authority to say so?* Then: *what does a restart read to decide a file is trustworthy?* and *what
imposes order on the merged plan when `Union` concatenates two half-plans?* The sweep produced F1,
F3, F3b and F10, none of which any of the four questions in `redteam-split.md` asks about directly.

---

## Findings

### F-C1 — **blocker** — the dispatch payload is owned by neither half, and the interface forbids either from inventing it

Every worker file's load-bearing first section is *what it was handed*. That is house shape, not my
preference: `Architect/stages/common.md:13-15` — "**Exactly what your caller passed you.** Your role
file lists them" — and six of Architect's eight stage files carry a `## Your inputs` heading
(`common.md:13`, `leaf.md:16`, `divider.md:11`, `combiner.md:10`, `redteam-plan.md:6`,
`redteam-split.md:9`). The sibling skills put the other half of the same contract in the
*dispatching* file: `Guarded_change/stages/stage-3.md:13-17` requires the spawn to record "the exact
context list (closed set: …)".

The division gives that contract no home:

- Sub-task two is told it "**must not specify how workers are dispatched, in what order, or at what
  fan-out**" (`:243-246`).
- Sub-task one is told it does not write any worker file (`:126-130`).
- I2 (`:149-154`) closes `stages/common.md` to "**exactly these rules**", none of which is an input
  contract — so the natural home is explicitly barred too.
- I1–I10 fix on-disk paths and config keys and never fix a spawn argument list.

**Failure scenario.** The worker-plane planner writes `stages/analyst.md`. It must open one item. It
cannot name a config key (I8 gives it `item_definition` and `off_limits` only), it cannot state "your
caller hands you a `locator`" (that is dispatch), and `common.md` is closed. I7 requires every finding
to carry an `analyst_id` — nothing in the interface tells the analyst where its own `k` comes from.
Meanwhile the driver-plane planner writes `SKILL.md`'s run loop ("per item dispatch analysts → verify
→ merge", `:92-94`) with no interface obligation to state what it passes. The two halves cannot
converge on this, because they never communicate and nothing constrains it.

**Remedy direction (divider's, not either half's):** add an interface object fixing the spawn payload
per role — e.g. *analyst is handed `(manifest entry, k, output path)`; verify is handed `(the N
analyst output paths, manifest entry, output path)`; merge is handed `(the input paths, output path)`*
— or reopen I2 so `common.md` may carry a generic "your inputs" contract.

---

### F-C2 — **blocker** — I8 leaves the worker plane unable to reach the corpus at all, and unable to see the strategy set it is required to choose from

I8 (`:186-188`, restated `:304-306`): "The Layer-2 config key set is `corpus_root`,
`item_definition`, `off_limits`, `concurrency_ceiling`, `analysts_per_item` (N),
`oversize_strategies`. … **Worker-plane files read only `item_definition` and `off_limits`.**"

Two consequences, both fatal as written:

1. **`stages/decompose.md` cannot locate the corpus.** It is the *producer* of I4's `locator`
   (`:168-170`), so it has no locator to start from, and `corpus_root` is withheld. `stages/verify.md`
   is required to "re-open **every** citation" (`:225-227`) — also corpus access. Every corpus-reading
   role in the skill is on the worker side, and the one key that says where the corpus is, is on the
   driver side and not passed (see F-C1).
2. **I6 and I8 contradict each other.** I6 (`:178-180`) says "Which one applies to a given item is
   the **worker plane's rule**; that the allowed set is a config key is the driver plane's" — while
   I8 makes `oversize_strategies` unreadable by the worker plane. Sub-task two item 2 (`:216-219`)
   nevertheless requires `decompose.md` to "choose a strategy from the fixed name set". If a corpus
   config narrows the permitted set, `decompose.md` cannot see the narrowing, so the config key is
   inert.

Neither half may repair this: both are told (`:140-143`, `:258-261`) that if they think an interface
object is wrong they "plan against it anyway" and file a note. So both plans will be built on an
unexecutable premise, and the note goes to plan reviewers who will read I8 as a settled constraint.

---

### F-C3 — **blocker** — `status.json`, the single artifact the blind roll-up rests on, has no named producer; and its counts are uncomputable by the half that would naturally own it

I9 (`:190-193`) shows the divider knew producers must be named: "`<run>/FINDINGS.md` **is written by
a dispatched merge agent** … Neither half may reassign this producer." No equivalent exists for
`status.json` (I3 `:162`, I5 `:171-176`) or for `config.snapshot.md` (I3 `:160`).

It is not merely unstated — it is *unassignable* under the interface as written:

- **The driver cannot write it.** I5 mandates `counts` = "findings produced / findings surviving
  verification / findings in the merged output". Computing those requires opening `analyst-*.md`,
  `verified.md` and `merged.md` — exactly the paths I3 (`:164-166`) forbids a driver-plane agent.
- **No single worker can write it either.** Under the pipeline the division implies, `verify.md`
  knows "produced" and "surviving verification"; `merge.md` knows "in the merged output". Nobody sees
  all three. And sub-task two is told it does not write "the run's control flow" (`:243-246`), which a
  planner may reasonably read as excluding run-state files.

**Failure scenario.** The driver-plane planner writes `stages/node.md` with "read
`<run>/items/<id>/status.json`" and, owning "the on-disk run-state layout" (`:117-119`), specifies the
node as its writer — silently breaking the blindness barrier the same sub-task claims to own "in
full". The worker-plane planner independently has `merge.md` emit a `status.json` with two of the
three counts. `Union` (`Architect/stages/combiner.md:37-64`) preserves both, and the conflict lands
on the plan reviewers, who see two producers for one file and no basis to choose.

**F-C3b — same finding, second limb (would remain after naming a producer): the write-order /
completeness rule for resume is unowned.** Sub-task one item 3 (`:104-106`) requires "the
restart/resume decision procedure **in full** — how a restarted run reads on-disk state and decides
what to redo and what to trust". Its only evidence is `status.json` and `manifest.json` (I3). Whether
that evidence is trustworthy depends on whether `status.json` is written *after* its payload file is
complete — a rule that belongs to the file's writer, who is unassigned. A worker killed mid-write
that had already emitted `status.json` leaves a truncated `merged.md` the driver is instructed to
trust, and no half owns the invariant that prevents it.

---

### F-C4 — **major** — I3's blindness is an instruction dressed as a structure, and I5 and I9 violate it directly

I3 (`:164-166`) claims: "A driver-plane agent is handed `manifest.json` and `status.json` paths only,
never a `analyst-*.md`, `verified.md`, `merged.md` or `FINDINGS.md` path — **this is what makes the
blindness structural rather than an instruction.**" The claim is false, on three counts:

1. **The layout is conventional, so every forbidden path is derivable.** A node that knows
   `<run>` and an `item_id` — both of which it must know — can construct
   `<run>/items/<item_id>/merged.md` by reading I3. Nothing in the arrangement prevents opening it.
   "Not handed a path" is an instruction about dispatch, not a structural barrier. (A structural
   version exists: e.g. findings files live under a directory the node is never given, named by a
   value only workers hold. That is not what I3 says.)
2. **I5 hands the driver a forbidden path inside a permitted file.** `status.json` carries
   `output_path` (`:174`). For an item, that value *is* `merged.md`. The driver reads `status.json`.
   So the driver is handed a `merged.md` path by the interface itself.
3. **I9 requires the driver to hold a `FINDINGS.md` path.** "The driver plane dispatches it, **names
   its path**, and hands that path to the human" (`:191-193`) — while I3 says a driver-plane agent is
   "never [handed] a … `FINDINGS.md` path."

The real invariant the task asks for is *the node never reads finding text*. I5's last sentence
("No field of the status record may carry the text of a finding, a claim, or a citation") is the one
clause that actually enforces something — and it is enforced by whoever writes the record, who is
unassigned (F-C3). As stated, the barrier is co-owned across the cut while sub-task one claims it
"in full and exclusively" (`:117-121`).

---

### F-C5 — **major** — analyst independence is demanded of the half that cannot produce it

Sub-task two item 3 (`:222-224`): `stages/analyst.md` "**Must state what makes the N analysts
genuinely independent rather than nominally so.**" The same sub-task forbids it to "specify how
workers are dispatched, in what order, or at what fan-out" (`:246`).

Independence *is* a dispatch property: N separate spawns, no shared context, none handed another's
output path, N sourced from `analysts_per_item` — which I8 also withholds from the worker plane. A
prompt file can assert independence; it cannot make it true. This reproduces, in a new place, exactly
the class of error round 2 was convened to fix: a guarantee assigned to a half that can only assert
it. Sub-task one's exclusion list (`:126-128`) does not mention independence either, so no half owns
the mechanism.

---

### F-C6 — **major** — I4 cannot express the output of `split`, and nothing maps items to roll-up nodes

I6 (`:178-179`) defines `split` as "divide the item into sub-items **and recurse**". I4 (`:168-170`)
gives a manifest entry `item_id`, `locator`, `size`, `fits`, `strategy` — with no parent/child
relation, no sub-item list, and no way to mark an entry as superseded by its sub-items. So the one
strategy that requires recursion has no representation in the only artifact that records
decomposition.

Second gap in the same object: I3 keys per-item state on `item_id` (`<run>/items/<item_id>/`) and
roll-up state on `node_id` (`<run>/rollup/<node_id>/`), and no interface object states the mapping.
Sub-task one item 3 requires `stages/node.md` to carry "how a node decides between spawning child
nodes and dispatching workers" (`:104`) — that decision reads the manifest, and the manifest cannot
tell it which items belong beneath which node. A restarted run has the same problem: it cannot
reconstruct the tree from the layout.

Both halves are barred from extending I4 (`:140-141`), so this must be fixed here.

---

### F-C7 — **major** — sub-task one is told the worker files' one-line purposes are "fixed below"; they are not

Sub-task one (`:128-130`): "It **may name those files and their one-line purposes (fixed below)** and
rely on the rules the shared interface guarantees they contain." I1 (`:145-147`) fixes only the six
**filenames**. No one-line purposes appear anywhere in I1–I10.

Sub-task one item 1 (`:93-94`) nevertheless requires `SKILL.md` to carry "the **stage/role index
table** listing every file under `stages/` … with a **one-line purpose** and its path", and item 2
requires a *Stage/role index* in `METHODOLOGY.md`. Both siblings do carry exactly such tables
(`Guarded_change/SKILL.md:36-45` and `METHODOLOGY.md:69-80`; `Dragonfly/SKILL.md:41-51` and
`METHODOLOGY.md:74-86`), so the requirement is right — but the driver-plane planner must now invent
purpose lines for five files it will never see, while the worker-plane planner independently writes
what those files actually do. Divergence in the router's index table is the precise failure the
non-directional seam was built to prevent, and it is guaranteed rather than merely risked.

**Remedy:** put the five one-line purposes into I1 verbatim, as the interface already promises.

---

### F-C8 — **major** — the stated joint's two failure sets do not cover the failure the blindness barrier exists to prevent, so the joint does not do the work claimed

The seam section (`:322-327`) is the sole argument that this is a real joint rather than an even
bisection: "Driver-plane files fail by a run that stalls, exceeds its concurrency ceiling, cannot be
resumed, or ends without handing anything over. Worker-plane files fail by an artifact that is
uncited, unverified, interpreted, or **steered**. Those are disjoint failure sets … `stages/node.md`
sits on the driver side despite being a prompt precisely because **everything it can get wrong is in
the first set.**"

That last clause is false. `stages/node.md` is the sole carrier of the blind-roll-up barrier
(`:106-107`, `:119-121`). Its characteristic failure is that a coordinator reads findings and its
expectations steer what its children report — which the division's own taxonomy files under
*steered*, i.e. the **worker** set. The driver set (stall / ceiling / un-resumable / no handover)
contains no member covering "the run terminated cleanly and handed over trustworthy-looking findings
that had been steered." The sets are disjoint only because the barrier's failure mode was omitted
from both.

This does not by itself prove the node belongs elsewhere — it may still belong with the driver. It
means **the justification offered for the cut being a joint does not hold**, and question 4 (real
joint vs. arbitrary cut) is therefore unanswered. `redteam-split.md` is explicit that no later
reviewer re-opens this.

---

### F-C9 — **major** — two of the ten interface objects do not cross the cut: the divider has designed inside a half, and a narrower-seam alternative went unweighed

The interface's premise (`:140`) is "every object **that crosses the cut**". Two do not:

- **I7 — the finding record** (`:183-184`). Its own last clause reads "the driver plane **may not
  read this record at all**." An object one half never touches does not cross the cut. Fixing
  `claim` / `citation` / `analyst_id` / `verified` / `agreement_count` here removes the central
  design decision of the worker plane — what a finding *is* — from the planner assigned to it, and
  places it where no plan reviewer will challenge it (they will read it as a given constraint).
- **I2's "exactly these rules"** (`:149-150`). The `stages/common.md` rule *set* legitimately
  crosses (node.md includes it). Closing it to "exactly" does not — it is a design decision inside
  the worker plane, and it is the clause that blocks the natural fix for F-C1.

More broadly: a ten-object interface fixing four schemas, a directory layout, a config key set, a
name enumeration and a producer assignment is a specification, not a seam. That size is itself
evidence the cut does not run along a joint — a joint has a narrow interface.

**The alternative not weighed** (the three at `:348-370` are round 1's cut, the two-layer cut, and
the blindness-barrier cut): **the per-item pipeline vs. the cross-item run plane** — one half owns
everything that happens *to a single item* (`decompose`'s per-item output, `analyst`, `verify`,
item-level `merge`), the other owns everything that spans items (`node`, roll-up merge, `SKILL`,
`METHODOLOGY`, config, README, install). Its seam is close to a single object: *for each manifest
entry, the item pipeline produces `<run>/items/<id>/merged.md` plus a terse `status.json`; the run
plane consumes only the latter* — which is also, exactly, the blindness barrier. It has a real
counter-argument (`common.md` and `merge.md` would then be shared by both halves), which is why it
needs weighing rather than adopting. It got neither.

---

### F-C10 — **minor** — the worked config instance has no corpus, and the floor requires its content to be specified

Sub-task one item 4 (`:108-112`) requires "a **worked** per-corpus config instance … a concrete
instance for **one real corpus**", citing the siblings. The citation is **correct**:
`Guarded_change/guarded-change.companion.md:1-7` and `Dragonfly/dragonfly.companion.md:1-7` are both
concrete Layer-2 configs for the real project `companion-emergence`, with live paths and notes.

But the task names no corpus, and the divider supplies none. The floor requires each step to be "one
file created … **with the content that goes in it specified**." The driver-plane planner must
therefore invent a corpus and its specifics, which no source can check — while I10 (`:195-196`)
simultaneously makes this the only file allowed to contain any. Fixable in one sentence here (name a
corpus, or authorise an explicitly-labelled synthetic example).

---

### F-C11 — **minor** — two factual errors about the siblings in sub-task one's file specs

- **`:88-89`** — "a **cold-start guard** section (**both siblings' precedent**:
  `Dragonfly/SKILL.md:22`)". `Dragonfly/SKILL.md:22` is indeed `## Before you start: cold-start
  guard` ✓, but `grep -rn "cold-start\|cold start" Guarded_change/` returns **nothing**.
  Guarded_change has no such section. It is one sibling's precedent, not both.
- **`:95-100`** — "`METHODOLOGY.md` … in the section shape **both siblings share**: … *Trigger*;
  *Human-in-the-loop*." `grep -n "^## "` gives Guarded_change/METHODOLOGY.md: Why this exists (18),
  The loop (35), Stage index (67), The two layers (88), The config contract (103), What a run
  produces (154), Human-in-the-loop (198) — **no Trigger section**. Only Dragonfly has one
  (`METHODOLOGY.md:161`). Also "*The method* (**in prose**)" mis-describes both: each renders the
  method as a fenced ASCII stage diagram (`Guarded_change/METHODOLOGY.md:37-54`,
  `Dragonfly/METHODOLOGY.md:47-62`), not prose.

The remaining sibling citations I checked all resolve: `Guarded_change/SKILL.md:25-52` = the Loop
section + table ✓; `Dragonfly/SKILL.md:29-70` = the Loop section ✓;
`Guarded_change/METHODOLOGY.md:103-152` = the config contract with inline annotated skeleton ✓;
`Dragonfly/METHODOLOGY.md:106-131` = the same ✓; `Guarded_change/METHODOLOGY.md:143` does name which
copy of a rule is operative ✓; `Guarded_change/METHODOLOGY.md:88-100` and
`Dragonfly/METHODOLOGY.md:95-102` are both "The two layers" ✓; both siblings carry a `README.md` ✓;
`Guarded_change/stages/stage-1.md:8` ("Write `1-spec.md`: …") and `stage-5.md:7` ("Implement per the
plan …") are both the invoking agent's own procedure, so round 2's withdrawal of the reader-based
joint is **correct** ✓.

---

### F-C12 — **minor** — a third identifier, `unit_id`, is introduced with no mapping

I5 (`:171-172`) keys the status record on `unit_id`. I3 and I4 use `item_id` and `node_id`. Nothing
says `unit_id` is their union, or how a reader tells which kind it holds. The driver's resume logic
(sub-task one item 3) reads exactly these records and must distinguish them.

---

### F-C13 — **minor** — "includes `stages/common.md` verbatim" is ambiguous between two mechanisms with different build orders

Sub-task one item 3 (`:106-107`) says `stages/node.md` "**includes** `stages/common.md` verbatim". I2
(`:149`) says common.md "is included verbatim by every dispatched agent". Architect's own mechanism
is dispatch-time concatenation (`node.md:36`, `:45-53`: "dispatch … on `stages/common.md` +
`stages/divider.md`"), which creates no file-level dependency. A build-time embed would create one —
and `Union` concatenates the two half-plans without renumbering (`combiner.md:66-67`, and "Do not
harmonise wording, renumber for tidiness" at `:63-64`), so the merged plan could order
"create `stages/node.md` embedding `common.md`" before `common.md` exists. One sentence in I2 fixing
the mechanism removes the risk.

---

## Nitpicks

- **N1** — alternative (b)'s count (`:359`) says "roughly 10 files against 4". Under the divider's own
  I1 (six `stages/` files), Layer 1 is `SKILL.md` + `METHODOLOGY.md` + 6 = **8**, and Layer 2 is 2
  files plus 2 non-file activities. The lopsidedness argument survives; the number does not match I1.
- **N2** — the install step (`:114-115`) is not file-shaped under the floor as given ("one file
  created or one coherent edit to one file"). It is executable without further planning, so it is not
  *below* the floor — but the floor as stated has no shape for it, and the floor check (`:344-346`)
  counts "5 files plus an install step" as six. Per `common.md` §3 I record this as a possible
  mis-specification of the floor rather than a defect in the cut.
- **N3 — unchecked by instruction.** The header claim (`:8`) that round 1 drew "2 blockers and 9
  majors" cannot be verified: I was instructed not to read `split-review-r1-*.md`. The disposition
  table (`:374-392`) shows four rows carrying a blocker tag, which need not contradict the count
  (reviewers may have split on severity for one merged finding), but I record the claim as unchecked
  rather than accepting it.

---

## Answers to the four questions

1. **Coverage** — **No.** Three things are owned by neither half: the spawn payload for every worker
   role (F-C1), the producer and write-order of `status.json` and `config.snapshot.md` (F-C3/C3b),
   and the mechanism that makes N analysts independent (F-C5). Corpus access for the corpus-reading
   half is affirmatively withheld (F-C2).
2. **The seam** — **Stated, and its non-directionality is a correct fix for round 1's blocker** (I
   verified `Architect/stages/node.md:50-53`, `leaf.md:16-19` and `combiner.md:37-64` independently;
   the halves are indeed planned concurrently by cold agents, merged by `Union`, which preserves
   rather than resolves conflicts). **But it is not sound:** I3 contradicts I5 and I9 (F-C4), I6
   contradicts I8 (F-C2), I1 does not contain what sub-task one is told it contains (F-C7), and two
   objects in it do not cross the cut (F-C9).
3. **The floor** — **Neither half falls below it.** Five substantial files per side, each a coherent
   whole task; the floor check at `:344-346` is sound apart from N2. No finding of mine is remediable
   only by decomposing below the floor.
4. **Real joint or arbitrary cut** — **Not established.** The accountability-and-failure-mode joint is
   a real improvement on round 1's reader-based joint (which I confirmed was factually false about the
   siblings), but as argued it is falsified by its own taxonomy (F-C8), and the interface's size
   points the other way (F-C9). The cut may still be right; the argument for it is not yet.

**This task is divisible.** I am not filing "indivisible" — the driver/worker distinction is a
plausible joint and both halves clear the floor. The findings above are repairs to the interface and
to the joint's justification, all of which are the divider's to make.
