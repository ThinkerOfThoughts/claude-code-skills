# Cold split review — round 4, reviewer A

Reviewing the **proposed division** at
`Architect/runs/data-distiller/it3/0/split-round-4.md`. I hold no plan and was given none.

**Fence compliance: I did not read, list, grep, glob or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke
the installed `data-distiller` skill.** I read the two sibling skills, the Architect stage files,
and the round-4 proposal only. I did not read any `split-review-*.md`, and I did not read rounds
1–3.

---

## VERDICT — the two parts

**Part 1 — what I found.** One `blocker`, one `major`, six `minor`, two `nitpick`. All of them are
seam-text defects. None of them is an argument against the joint.

**Part 2 — do I object to going forward with this cut? NO. I endorse it.** The cut is along a real
joint that the owner's own task statement named (P5), the two halves have disjoint inputs, outputs,
failure modes and review criteria, both are far above the floor, and the seam is — with the
exceptions below — genuinely self-contained rather than producer/consumer. **I would keep this
joint.** My findings travel down with the sub-tasks; they do not withhold agreement.

---

## Findings

### F1 — `blocker` — the driver table has no attempt cap for a leaf with **no** `STATUS`, so the run driver does not terminate on the exact failure `RUN` exists to detect

§3.5's control table, leaf rows, verbatim:

| Node | Observed | What B's run driver does |
|---|---|---|
| leaf | no `STATUS` | increment `RUN`; dispatch A's entry agent (§3.3) |
| leaf | `state=partial` or `failed` | if `RUN < run.max_attempts` → … Else → **replace `STATUS` with `escalated`** … |

The cap lives **only** on the second row, and that row cannot be reached without a `STATUS` file
already existing. §3.4 states: *"A node with no `STATUS` file has not finished. Absence is the only
'not yet' marker."*

**Concrete failure.** A's pipeline entry agent is dispatched on leaf `0.3` and dies — context
exhaustion, a tool error, the harness killing it — **before** writing any `STATUS`. On the driver's
next pass the node still matches row 1 (`no STATUS`), unconditionally. The driver increments `RUN`
and dispatches again. It dies again. `RUN` climbs to 4, 40, 400; row 1 keeps matching, because
`run.max_attempts` is consulted nowhere on that row. **The loop never terminates and never
escalates**, and each turn burns a fresh agent.

Three things make this load-bearing rather than pedantic:

1. §3.2 write rule 4 introduces `RUN` for precisely this case: *"Its presence means 'this node has
   been attempted', which is what distinguishes **never started** from **started by a run that
   died**."* The one scenario `RUN` was added to handle is the one the table does not cap.
2. §3.5's **termination argument** is therefore false: *"the cap converts any non-terminal node into
   `escalated`"* — it does not, for a leaf that never produced a `STATUS`. The argument's premise
   holds only for nodes that already wrote a line.
3. The **group** rows *do* have the cap (`group | every child terminal, RUN ≥ run.max_attempts,
   still no STATUS | write STATUS = escalated`). Round 3 filed the missing group cap as a `major` and
   §7 records it fixed. The identical defect was left on the leaf side. The asymmetry is visible in
   the table itself.

**Remedy** (one row, inside the seam, so both halves inherit it identically): `leaf | no STATUS,
RUN ≥ run.max_attempts | write STATUS = <node_id> escalated 0 0 0, append to decisions.md, stop for
the human.` This is B-executable and needs nothing from A.

Severity `blocker` rather than `major`: the seam asserts a termination proof it does not have, and a
non-terminating dispatch loop is not a degradation of the built skill, it is the built skill hanging.
It also *contradicts a settled element* of the seam (§3.5's own termination argument).

---

### F2 — `major` — the cross-half size invariant is a plan-time agreement between two independently-defaulted numbers, and the seam fixes neither number

§3.5: *"A declares `analysis.max_item_bytes` and B declares `sizing.max_item_bytes`; **the seam's
invariant is `sizing.max_item_bytes ≤ analysis.max_item_bytes`**, stated by B in `METHODOLOGY.md`'s
config contract as a rule over the merged plan."*

The seam fixes both **names** (good) and the **relation** (good), but neither half is given a
**value**, and the two halves choose their defaults **concurrently and blind**. §3.1's declaration
obligation requires each half to declare *"name, meaning, type, default (or 'required')"* — so both
will emit a number.

**Concrete failure.** B, reasoning about decomposition, defaults `sizing.max_item_bytes: 400000`.
A, reasoning about what an analyst agent can hold, defaults `analysis.max_item_bytes: 120000`. Both
plans are locally correct and neither planner can see the other. At merge, `Union` produces a plan
containing both numbers; `Union` is **barred from authoring** (`Architect/stages/combiner.md:6` —
*"None of the three is an author. You do not improve, rewrite, or adjudicate the material."*), and
§6 of this proposal explicitly declines to defer anything to `Union` for that reason. B's
`METHODOLOGY.md` contract rule and B's worked example config then faithfully transcribe both
declared defaults **and** the invariant they violate. Nobody in the pipeline is instructed to
reconcile them. The skill ships out of the box in a state where every decomposed item exceeds A's
acceptance bound and A's entry agent writes `state=failed` on all of them — after which F1's
missing cap or the `partial`/`failed` cap escalates the entire run.

This is the failure class `redteam-split.md` names, in a form the usual test misses: neither half
*invents* the other's artifact, so §6's audit line — *"No element of this seam has the form 'one half
produces X at plan time and the other consumes it'"* — is literally true and still does not cover
this. The dependency is a **conjunction constraint** over two independently authored values, and
`divider.md` is explicit that *"anything that must be **agreed at plan time** belongs"* in the seam
text, *"stated by you, not derived by either half."* A relation without an anchor is not agreed.

**Remedy, in order of preference:**
1. **Collapse the two keys into one.** Fix in the seam: *"there is one bound,
   `analysis.max_item_bytes`; A declares it with a default; B's `sizing.max_item_bytes` is not a
   separate key — B's decomposer reads `analysis.max_item_bytes`."* This makes the invariant
   unfalsifiable by construction and costs B nothing, since §3.6 already lets both halves reference
   `run.dir` by name across the partition. (See also L3 below.)
2. Or **state the number in the seam**: *"both defaults are `N` bytes; neither half may choose
   another default."*

Severity `major`, not `blocker`: the goal and mechanism are right and the remedy is a clause, but a
load-bearing plan-time agreement is missing and nothing downstream can supply it.

---

### F3 — `minor` — §3.5's group rows overlap with no stated precedence

Two rows both match the state *(every child terminal, no `STATUS`, `RUN ≥ run.max_attempts)`*:

- `group | every child terminal, no STATUS | increment RUN; dispatch the roll-up`
- `group | every child terminal, RUN ≥ run.max_attempts, still no STATUS | write STATUS = escalated`

A driver implemented as first-match-wins over the table in written order never reaches the cap row —
reproducing F1's non-termination for groups. The remedy is one clause ("rows are evaluated in order,
most specific first" — or, better, add the `RUN <` guard to the first row so the rows are disjoint).
Local and fixable in place, hence `minor`, but it is the same latent shape as F1 and should be fixed
in the same edit.

---

### F4 — `minor` — the "EXHAUSTIVE skeleton" leaves B's optional stages 6–9 with no legal output location

§3.2: *"The skeleton is EXHAUSTIVE. Neither half may add a file or directory to it, except that A's
per-item outputs inside a leaf node directory are A's to name and number."*

§3.7 rule 3: *"Every agent is read-only over the corpus and writes nothing except the output file(s)
its own role file names."*

§3.1 grants B `stage-6.md … stage-9.md`, *"optional; B's to use or leave unused."*

If B uses one — say a stage-6 agent that audits `index.md` before the driver starts, or a
sizing-rationale writer — its role file must name an output file, and every legal name is already
taken by the skeleton. B's only outlet is `decisions.md`, which is a one-line-append log. The
exception clause was written for A and not extended to B. B can dodge this by leaving 6–9 unused, so
it is `minor`, but the seam currently makes a granted affordance unusable.

**Remedy:** extend the exception — *"…except that A's per-item outputs inside a leaf node directory
are A's to name, and B may add run-level files declared in its plan under the declaration obligation
(§3.1), which no agent below the boundary may read."*

---

### F5 — `minor` — decomposition has no place in the control loop, and its restart contradicts `item.json` immutability

§3.2: *"`item.json` is never written twice and never deleted."* §3.5's driver table has rows only for
leaf and group nodes; **there is no row for the state "`index.md` is absent"** — i.e. the run died
during or before decomposition. §3.2 write rule 1 guarantees `index.md` is never seen partial, but it
does not guarantee that the `item.json` files written before the crash are consistent with the
`index.md` a re-run decomposition will write.

**Concrete failure.** A run dies after the decomposer has written `nodes/0.1/item.json` and
`nodes/0.2/item.json` but before `index.md` lands. On restart the driver sees no `index.md` and
re-runs stage 0. The decomposer must either rewrite those two `item.json` files — forbidden by §3.2 —
or detect and adopt them, which no seam clause describes, and which risks adopting records whose
`locator`s belong to a different sizing decision.

B owns stage 0, stage 1 and P7-across-nodes, so B can resolve this **internally** — which is why this
is `minor` and not a self-containment failure. But the seam's absolute *"never written twice"* forbids
the natural fix (idempotent rewrite), so B inherits a contradiction rather than a free hand.
**Remedy:** soften rule to *"`item.json` is never deleted and never changed once `index.md` exists;
before `index.md` exists, decomposition may rewrite it"*, and add a driver row for `index.md` absent.

---

### F6 — `minor` — A's per-item filenames are unconstrained in a directory holding three of B's fixed names

§3.2 gives A free naming inside a leaf node directory (*"A's per-item outputs … are A's to name and
number"*) while `item.json`, `RUN` and `STATUS` live in that same directory and belong to B. Nothing
forbids A from declaring, say, a `RUN`-named diagnostic file or a `status.json` that shadows the
contract. A is blind to how load-bearing those three names are beyond what §3.3/§3.4 say. **Remedy:**
one clause — *"A may not use the names `item.json`, `RUN`, `STATUS`, nor any `*.tmp` sibling of
them."*

---

### F7 — `minor` — the namespace partition does not say which half owns corpus-shape facts an analyst needs

§3.6 gives B `corpus.*` and A `analysis.*`. P6 requires the method be corpus-agnostic with specifics
in Layer-2. B's decomposer needs the corpus's structural boundaries; A's analysts plausibly need
corpus-specific facts too — what a citable unit is called, what the source's addressing convention
looks like, what counts as a distinct source. Blind, A will declare those under `analysis.*` while B
declares overlapping ones under `corpus.*`, and B's worked example config (§3.6, a rule over the
merged plan) will faithfully print **both**, describing the same corpus twice, possibly
inconsistently, with nothing saying which one an agent should believe.

**Remedy:** one seam clause assigning corpus-descriptive facts to `corpus.*` and stating that A's
role prompts may read `corpus.*` read-only for describing the source (A already reads the config via
`config_path`, §3.3), reserving `analysis.*` for A's method parameters (N, thresholds, bounds).

---

### F8 — `minor` — root `escalated` collapses run-level signal

§3.4: group `escalated` iff *"at least one child is escalated"*, and §3.5 emits an unsplittable
over-size item as a leaf with `escalated`. On a large corpus, **one** item nobody could split turns
the root node's status to `escalated`, indistinguishable from a wholesale run failure. The `escalated`
state's own definition is *"terminal, do not re-run, and the human is told"* — so the human is told
the same thing for one unsplittable file as for a collapsed run.

`n_findings`/`n_dropped` still carry counts, and `findings.md` carries the header-only section, so
nothing is lost — only the top line's discriminating power. `minor`. A sixth `STATUS` field
(`n_escalated_leaves`, summed by the roll-up, computable from children's lines alone and carrying no
address) would fix it without touching blindness.

---

### F9 — `nitpick` — the seam's transport is more robust than §6 admits, and the sub-task text contradicts the fallback

§6 reports honestly that neither `divider.md` nor `node.md` implements "prepend §3 verbatim" — I
confirmed this: `node.md` passes only `(division.first, plan, granularity, depth+1, node_id + ".1")`
and nothing in either file mentions a seam-prepend step. But both sub-task texts **also carry the
absolute path** to `split-round-4.md` in their "Source material" block, and `common.md:19` tells every
dispatched agent *"Opening what your task points at is part of your job."* Since the path lives inside
the `division.first` / `division.second` strings that `node.md` demonstrably does pass, **transport is
in practice guaranteed by the path, not by the prepend.**

The residual defect is textual: both sub-tasks say the seam *"is prepended to this sub-task"*, so a
half that receives it un-prepended holds a statement contradicted by its own inputs, and §3's *"If you
divide your sub-task further, prepend this seam text verbatim"* is then an instruction to prepend text
it does not have. **Remedy:** re-word to *"the seam is at §3 of the file named below; read it first —
it may also have been prepended to this sub-task"*, which makes the path the primary channel and the
prepend the optimisation.

---

### F10 — `nitpick` — no schema/version marker on `STATUS` or `item.json`

Both are cross-half wire formats with fixed field counts (§3.3, §3.4). Neither carries a version
field, so a future revision of either half cannot be detected by the other at run time. Not worth a
seam change now; recorded because no later reviewer sees this cut.

---

## The four questions, answered directly

**1. Coverage — clean.** I walked P1–P8 against §4 and against the two sub-task texts independently
of §4's own table. Every property has exactly one named owner; the two split properties (P6, P7) are
partitioned along a stated line (namespace / within-item vs across-node) rather than shared. I looked
specifically for the two named failure shapes:

- *Orphaned remainder:* I swept for load-bearing work named in neither half — the run log, the
  assembled output, `stages/common.md`, the entry surface, degenerate corpora, escalation, the
  invocation itself, house-style conformance. All are assigned in §2 or §4. The only orphan I found
  is F4's: an output location for B's optional stages.
- *Both-assume-the-other:* the candidates are `stages/common.md` (B writes, A relies — §3.7 fixes the
  contents, so A relies on text, not on B's judgment), the merged-findings filename (A declares, B
  writes a rule over it — build-time, legitimate per `divider.md`'s third home), and the size bound
  (**F2 — this one is genuinely unowned at plan time**).

**2. The seam — stated: yes, in full, §3.1–§3.11. Sound: yes, except F1. Self-contained: yes, except
F2.** I tested every entry in §6's audit table against the two sub-task texts rather than against
§6's own claims. The producer/consumer patterns that killed earlier rounds are genuinely absent: the
item record's value domains are fixed (§3.3) rather than derived from B's config namespace; the
invocation target, arity and argument are fixed rather than negotiated; the `STATUS` schema is fixed
with a deliberate *absence* of a path field; stage numbering is fixed because it is inherently joint;
config namespaces are partitioned, not merged. The remaining cross-half items are correctly reframed
as build-time rules over the merged plan (`divider.md`'s third legitimate home), and I checked that
each is executable by a practitioner holding both plans: the router table, the `Stop-for-human`
section, the stage index, the config contract, `index.md`'s findings pointer and `findings.md`'s
assembly rule all consume only fields the declaration obligation guarantees. The **loop diagram** is
the one I expected to fail this test and it does not — §3.1's phase binding (2 = entry + analysts,
3 = verification, 4 = merge) gives B the control flow it would otherwise have to guess. That binding
is doing real work and should not be softened.

**3. The floor — clean, no finding.** The floor is *one file with its content specified*. A plans at
minimum `stage-2.md`, `stage-3.md`, `stage-4.md` plus its finding/citation/diagnostic formats; B plans
at minimum nine files. Neither half is a single file. Neither half is at or below the floor, so the
division is legitimate and the task should not have been left undivided. §5's own note that B is
roughly twice A and remains divisible one level down is correct and is not an objection — evenness is
not the test, and B's own `Divisible` call is where that resolves.

**4. Real joint, not an arbitrary cut — clean, and this is the strongest part of the proposal.**
What differs across the boundary, concretely and not merely by symmetry: what the agent reads (corpus
content *for meaning* vs. corpus *shape* and one-line statuses), what it produces (cited evidence vs.
bookkeeping), its discipline (cite-every-finding + facts-not-interpretation vs. blind + idempotent +
resumable), its characteristic failure (a fabricated citation vs. a peeking coordinator or lost work),
its unit of work (one item vs. the corpus and the tree), and its review criterion (do citations
resolve vs. is it blind and idempotent). That is six independent axes changing at one line. The line
is also **not the divider's invention** — P5 in the owner's task statement asserts exactly this
boundary exists and is not crossed, so the division is cutting where the specification already cut.
The rejected alternative (method vs. envelope) is recorded with its reason, and the reason is right:
it is a packaging boundary at which nothing about the method changes.

---

## The six lenses

### 1. Factual — **CLEAN** (earned; citations checked below)

I resolved every line-anchored citation in the proposal against the actual files:

| Cited in the proposal | What is actually at that line | Verdict |
|---|---|---|
| `Guarded_change/SKILL.md:28` — *"Step numbers below are the canonical stage numbers used everywhere"* | exact match | ✅ |
| `Guarded_change/SKILL.md:27` — `changes/<slug>/` | *"Create a change folder `changes/<slug>/`…"* | ✅ |
| `Dragonfly/SKILL.md:19` — *"Validate config paths at hunt start"* | exact match (wraps from :18) | ✅ |
| `Dragonfly/SKILL.md:31` — `hunts/<slug>/` | *"Create a hunt folder `hunts/<slug>/`…"* | ✅ |
| `Dragonfly/METHODOLOGY.md:143` — run artifacts in the skill dir | *"One folder per hunt, e.g. `hunts/<slug>/`:"* | ✅ |
| `Guarded_change/METHODOLOGY.md:139` — *"Paths are validated, not assumed"* | exact match | ✅ |
| `Dragonfly/stages/charter.md:1` — a charter read at *specific* stages | *"# The red-team charter (shared by stages 1, 4, 7)"* | ✅ |
| `Architect/stages/common.md:3` — universal preamble is Architect's own pattern | *"Every agent Architect dispatches reads this file first…"* | ✅ |
| `Architect/stages/leaf.md:47` — *"You do not file findings…"* | exact match | ✅ |
| `combiner.md` — *"None of the three is an author…"* | `combiner.md:6`, verbatim | ✅ |
| `combiner.md` — *"2-of-3 on numbered steps, INCLUDING ORDER"* + odd plan discarded | `combiner.md:22`, verbatim | ✅ |
| `combiner.md` — *"it is handed to a planner that cannot fix it… forever"* | present at `combiner.md:~82` | ✅ |

I also checked the proposal's non-line-anchored factual claims:

- §3.7's *"neither sibling has a `common.md`"* — **confirmed**: `ls Guarded_change/stages` and
  `ls Dragonfly/stages` show `charter.md` and numbered stages only, no `common.md`. The claimed
  divergence is real and B is correctly told to state it.
- §3.1's *"the siblings key their router, stage index and gate log off stage numbers"* — **confirmed**
  in both `SKILL.md` files.
- §6's *"neither `divider.md` nor `node.md` provides a mechanism"* for seam transport — **confirmed**;
  `node.md` passes `(division.first, plan, granularity, depth+1, node_id + ".1")` and nothing more.
  (See F9 — the mitigation is stronger than stated.)
- §6's *"this contradicts `divider.md`'s offer of `Union` as a legitimate home"* — **confirmed**;
  `divider.md` lists *"Deferred to `Union` as named reconciliation work"* as home 2 while
  `combiner.md:6` bars `Union` from authoring. The proposal is right not to rely on it, and right
  that this is an apparatus defect rather than a defect of this division.
- §3.10's ruling that a test harness is out of scope — **supported by the sources**: neither sibling
  ships a harness or eval directory (`ls` of both skill roots shows only `SKILL.md`,
  `METHODOLOGY.md`, `README.md`, a companion config, `stages/` and a run folder). I do **not** file a
  finding against that clause; the ruling is correct on the evidence and the task asks for a plan to
  build the skill.

**Unchecked, flagged rather than accepted:** §7's arithmetic about round 3 (*"4 blockers, 13 majors,
12 minor/nitpick"*, and *"all three reviewers endorsed the cut"*) I could **not** verify — the
`split-review-*.md` files are out of bounds for me by instruction, and I did not open rounds 1–3. I
treated every §7 row as a claim and reviewed §3 on its own text; F1 was found by reading §3.5 directly,
not by trusting the row that says the group cap was added.

### 2. Logical — **F1** (`blocker`), **F3** (`minor`), **F5** (`minor`)

The reasoning is otherwise tight, and two pieces of it are notably good: the *no node ever changes
kind* rule (§3.2), which eliminates the whole class of "a leaf becomes a group mid-run" states that
round 2 apparently needed; and the decision to make the over-size strategy purely decomposition-time,
which removes the only cross-boundary control signal the design would otherwise need. The termination
argument (§3.5) is the right thing to have written down — it is what made F1 findable.

### 3. Missed opportunity — **one, folded into F2**

`sizing.max_item_bytes` should not exist. The seam already permits cross-namespace *reference* by
name for `run.dir` (§3.6). Applying the same move to the size bound — one key, `analysis.max_item_bytes`,
declared by A, read by B's decomposer — deletes the invariant, deletes the `METHODOLOGY` clause that
documents it, deletes F2 entirely, and removes one of the two numbers the halves must independently
guess. It is strictly less seam text for strictly more safety. I record it here because §1's
alternatives paragraph is right that no later reviewer sees the options available at this cut.

No other genuinely better division was left on the table. I considered a three-way split
(decomposition / pipeline / envelope) and it is worse: it would put a second blind seam between B's
decomposer and B's driver, which currently share an owner and therefore need no seam at all.

### 4. Unstated assumptions & risks — **F4, F6, F7, F8**; plus the assumption underlying F1

The load-bearing unstated assumption is F1's: that a dispatched pipeline agent always returns having
written a `STATUS`. Every other row of §3.5 is written in the awareness that agents die; that one row
is not.

A second, milder one: §3.3 says the driver *"waits for the agent to return"* while §2-B says the
driver *"bounds concurrency"* — jointly fine (bounded parallel waits), but the seam never says a node
has at most one live agent at a time. Since only one role owns each file, no corruption follows, so I
do not file it; recording it as an observation.

### 5. Fidelity — **CLEAN** (earned; terms pinned below)

I pinned each loaded operational term to the concrete mechanism the division assigns it and checked
the mechanism implements *that*, not a proxy:

| Term | Pinned to |
|---|---|
| **cold** | `stages/common.md` rule 1 (§3.7): no shared context with caller or siblings — plus A's obligation (§2-A/P2) to specify the *enforcement* at its entry agent's dispatch point. Not a proxy: the duty and its enforcement are both assigned, to different files, with §3.7's closing clause resolving the additions-only collision. |
| **decompose** | B's stage 0: split along config-named structural boundaries into node directories, recursively, bounded by `sizing.max_resplits`; emit `item.json` per leaf. A real mechanism, not "identify items". |
| **item / sized** | §3.3's fixed record with `locator = {path, lines[first,last]}`, inclusive 1-based, and `size_bytes` in bytes. The unit is fixed *in the seam*, which is what stops it being a proxy. |
| **N independent analysts** | A's entry agent fans out to N sub-agents, each with no shared context and no sibling visibility, N defaulted and justified by A. |
| **cites every finding** | `common.md` rule 4 states the duty; the citation **format** is A's, in A's role files. Format-vs-duty split is stated, so neither is orphaned. |
| **verify** | a **separate cold agent, never the analyst that produced the finding** (§2-A/P3), with an operational definition of "unverifiable" and a stated fate for a dropped finding, surfaced as `n_dropped`. This is the mechanism, not a self-check proxy. |
| **agreement-ranked merge** | A matches findings across the N analysts, computes an agreement count, records the rank; the count is surfaced upward as `max_agreement` (§3.4). |
| **blind roll-up** | stage-5 agent whose read permission (§3.2 table) is *"the `STATUS` lines of its own children, and nothing else"* — explicitly not `item.json`, `RUN`, `decisions.md`, the corpus, or a finding — and §3.4's deliberate **omission of any path field**, so the coordinator never holds an address for a finding. This is the sharpest fidelity result in the document: blindness is enforced by what the schema *lacks*, not by an instruction not to look. |
| **restart / resume** | on-disk only: file presence (§3.2 rule 1), `RUN`'s integer, and `STATUS.state`; split into across-node (B) and within-item (A). Real state, no in-memory assumption. |
| **facts, not interpretation** | `common.md` rule 7 states the principle; A owns its enforcement in the analyst/verify/merge prompts *"as an enforceable rule rather than an exhortation"* (§2-A/P8). The proposal explicitly names the exhortation failure mode and assigns the fix. |
| **Layer-2 config** | one markdown-embedded YAML file, partitioned namespaces, one worked example for a named example corpus; agents receive its path via arguments or `item.json.config_path` (§3.7 rule 6). |

No term resolved to a proxy. The one place a proxy was possible — P5's blindness degrading into "the
coordinator is told not to read findings" — is the one place the design is structural.

### 6. Completeness — **F1, F4, F5, F6** (checklist + generative sweep both run)

Required-sections check: the division states its joint, its two sub-tasks, a seam, a coverage
argument, a floor check, a self-containment audit, and its disposition of prior findings. All present.

**Generative sweep — I asked "what load-bearing section does that list not anticipate?" and looked
specifically for:** (a) a **termination** story for every node kind and every crash point → found F1
and F3; (b) an **output location** for every role either half may create → found F4; (c) a **restart**
story for the phase that runs *before* the loop the restart story covers → found F5; (d) a **namespace
collision** surface where two owners write into one directory → found F6; (e) a **default-value**
consistency story wherever the seam states a relation between two independently authored values →
found F2; (f) the **degenerate corpora** (empty; single below-threshold item) → assigned to B in §2-B,
covered; (g) **who creates the run directory and node directories** → B-internal, covered by
ownership; (h) **what a half does when it disagrees with the seam** → §3.9, present, with its limit
stated honestly rather than promised away; (i) **an escape for a corpus that changes between runs** →
out of scope for this task, correctly absent.

---

## Standing observations that are not findings against this cut

- **`node.md` and `divider.md` disagree on the round cap.** `divider.md` says *"four rounds ran and no
  split reached 2-of-3"* for `FAILED_TO_DIVIDE`; `node.md` says *"three rounds ran and no split
  reached 2-of-3 agreement."* This is an Architect apparatus inconsistency, not a defect in this
  division, and it does not affect my verdict. Recorded so it is not lost.
- **The two apparatus gaps the proposal flags in its preamble** (no guaranteed seam transport; no
  guaranteed upward channel for a lone `SEAM-OBJECTION` past `Consensus`) are both real — I confirmed
  each against `node.md` and `combiner.md:22`. The proposal is right to state them rather than paper
  over them, and right that they are Architect's problem. F9 notes that the first is less severe than
  claimed.

---

## Summary of severities

| # | Severity | Finding |
|---|---|---|
| F1 | **blocker** | §3.5 has no attempt cap for a leaf with no `STATUS`; driver never terminates on a died-before-writing dispatch, and §3.5's termination argument is false |
| F2 | **major** | the `sizing.max_item_bytes ≤ analysis.max_item_bytes` invariant is a plan-time agreement over two independently-defaulted numbers, neither fixed in the seam and neither fixable downstream |
| F3 | minor | §3.5 group rows overlap; row precedence unstated |
| F4 | minor | the "exhaustive skeleton" leaves B's optional stages 6–9 with no legal output file |
| F5 | minor | resumed decomposition contradicts *"`item.json` is never written twice"*; no driver row for `index.md` absent |
| F6 | minor | A's per-item filenames unconstrained in a directory holding B's `item.json`/`RUN`/`STATUS` |
| F7 | minor | namespace partition does not assign corpus-descriptive facts an analyst needs |
| F8 | minor | root `escalated` on any single escalated leaf collapses run-level signal |
| F9 | nitpick | sub-task text asserts a prepend that nothing implements; the absolute path is the real transport and should be named as such |
| F10 | nitpick | no schema/version marker on `STATUS` or `item.json` |

**Restated for the divider, because the two parts are separable: I do NOT object to going forward
with this cut.** F1 and F2 are seam-text edits inside a joint I would keep. If they are not fixed, they
travel down with sub-task B (F1, F3, F5) and with both halves (F2) and are the planners' to carry.
