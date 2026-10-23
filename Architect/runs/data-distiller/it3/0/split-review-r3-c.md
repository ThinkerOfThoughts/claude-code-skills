# Split review — round 3, reviewer C

Cold, independent review of the proposed division in
`Architect/runs/data-distiller/it3/0/split-round-3.md`. I hold **no plan** and judged the cut
against the shape of the **task**, not against any plan's organisation.

**Fence compliance: I did not open, read, list, grep, glob or otherwise access
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke
the installed `data-distiller` skill.** I read only `split-round-3.md`, the Architect stage files
(`common.md`, `redteam.md`, `redteam-split.md`, `divider.md`, `node.md`, `leaf.md`,
`combiner.md`), and the two sibling skills `Guarded_change/` and `Dragonfly/`. I did not read
`split-round-1.md` or `split-round-2.md`, and I read no `split-review-*.md`.

---

## VERDICT — the two parts the divider needs

**Part 1 — what I found.** One `blocker`, five `major`s, three `minor`s, one `nitpick`. **All ten
are defects in the seam text (§3) or in the sub-task texts that quote it — none is a defect in the
joint.** Two of them (F3, F5) are round-2 findings that §7 records as fixed and which I find are
not fixed; they have moved rather than closed.

**Part 2 — do I object to going forward with this cut? NO. I endorse the joint and I would keep
it.** The finding boundary is a real joint: P5 in the task statement asserts the line exists, and
§1's table shows genuinely disjoint inputs, outputs, failure modes and review criteria on each
side. The rejected alternative (method vs. envelope) is correctly rejected and correctly recorded.
Filing a blocker is not my objection — I am not withholding agreement.

**One caveat the divider must not read as an objection but must act on.** The standard disposition
— "findings travel down with the sub-tasks and are fixed by the planners below" — **does not work
for any of F1–F6.** Every one of them lives in §3, and §3's own preamble says *"Neither half may
change it"*; §3.9 forbids a planner from even filing it. So these must be fixed in a re-derived §3
before dispatch, not carried down. That is a round-4 re-derivation of the seam text with the joint
held fixed, which is exactly what round 3 was relative to round 2.

---

## The four questions

**1. Coverage — near-complete; one orphan.** §4's ownership table is thorough and I could not find
a portion both halves assume the other owns. The one orphan is **F4**: an over-size item that
cannot be brought within the bound is removed from the leaf set (§3.5) and then belongs to no
category the rest of the seam defines. **F8** is a softer orphan (corpus immutability across a
resume).

**2. The seam — stated: yes. Self-contained: yes. Sound: no (F1–F6).**

I checked self-containment adversarially and independently, because `redteam-split.md` says it is
the failure this question keeps missing. **I looked for any clause of the form "A produces X at
plan time and B consumes it" and found none.** Specifically I traced each of the six cross-half
artefacts that could plausibly have that shape:

| Candidate | Where it actually resolves | Legitimate? |
|---|---|---|
| A's merged-findings **filename**, consumed by B's `index.md` and `findings.md` steps | §3.1 declaration obligation item 3 + §2-B/§3.8 written as **rules over the merged plan** | Yes — `divider.md:83-86`, build-time dependency |
| A's **config keys**, needed by B's worked example and contract | §3.6 namespace partition + rule over merged plan | Yes |
| A's **stop-for-human conditions**, needed by B's `SKILL.md` | §3.1 item 4 + explicit rule in §2-B | Yes |
| the **status vocabulary** | written out in full in §3.4 | Yes — fixed in seam |
| the **invocation target / arity / argument** | written out in full in §3.3 | Yes — fixed in seam |
| **stage numbering** | partitioned and bound at phase level in §3.1 | Yes — fixed in seam |

None of these requires either half to see the other's plan at plan time. §6's own audit claim
holds up under my independent check. §6 is also right, and right to say so, that `Union` cannot be
a reconciliation venue (`combiner.md`: *"None of the three is an author"*), and right that this
contradicts `divider.md:80-82` — I confirm that contradiction exists and that this proposal does
not lean on it.

**3. The floor — clean, no finding.** A plans at least `stages/stage-2.md`, `stage-3.md`,
`stage-4.md` plus its finding-record and citation formats; B plans at least `SKILL.md`,
`METHODOLOGY.md`, `README.md`, the worked config, `stages/common.md`, `stage-0.md`, `stage-1.md`,
`stage-5.md`, and the concatenation step. Both are coherent whole tasks many files above *"one file
created, with the content that goes in it specified."* Neither half falls below the floor, so this
is a legitimate division and not a task that should have been left undivided. I hold the floor
correct for this task and am not proposing a change to it.

**4. Real joint or arbitrary cut — real joint.** What differs across the line, concretely: below
it an agent reads corpus content *for meaning* and emits a cited finding, and its review criterion
is *"does every citation resolve?"*; above it an agent reads paths, sizes, item records and
five-field status lines, emits bookkeeping, and its review criterion is *"is it blind, and is it
idempotent?"*. The characteristic failures are disjoint (fabricated citation vs. a coordinator that
peeks / work silently duplicated on restart). This is not a bisection for symmetry — §5 concedes B
is roughly twice A's size and defers B's further cut one level down, which is the correct response
to unevenness rather than a reason to move the joint.

---

## Findings

### F1 — `blocker` — `STATUS` is write-once, so a re-dispatched item can never record that it succeeded; P7's resume is inert

*(logical; fidelity)*

The seam makes `STATUS` immutable in three places — §3.2 skeleton (`STATUS … WRITE-ONCE`), §3.2
prose (*"`STATUS` is never overwritten"*), §3.4 (*"exactly five fields, **write-once**"*) — and
simultaneously defines two leaf states as re-runnable: §3.4 *"`partial` … **Re-runnable.**"* and
*"`failed` … **Re-runnable, up to the attempt cap.**"*, with §3.5's driver table re-dispatching on
both. §2-A tells A to write the `STATUS` line *"as the last act of your pipeline."*

**Failure scenario.** Leaf `0.3`: the N analysts complete, the run dies before merge. A writes
`0.3 partial 0 0 0`. The driver sees `partial`, `RUN`(=1) `< run.max_attempts`, increments `RUN`
and re-dispatches. A's within-item resume correctly skips the analysts, runs verification and
merge, and produces the merged-findings file. **A now has nothing it may write.** `STATUS` exists
and is write-once. §3.5 confirms the divider intends exactly this, in the parallel case: *"write
nothing to `STATUS` (it is write-once and already exists)"*.

Consequences, all concrete: `0.3` is permanently `partial` carrying `0 0 0` while a full set of
merged findings sits on disk; §3.4's group rule *"`done` — every child is `done`"* means `0.3`'s
parent, and transitively the root, can never reach `done`; §3.8's `findings.md` assembly still
picks up the file, so the corpus output and the status tree disagree; and every re-dispatch up to
the attempt cap burns a full pipeline whose result cannot be recorded. **`state=done` is
unreachable for any item that ever hiccupped once** — i.e. for exactly the case P7 ("restart and
resume from on-disk state") exists to serve.

This is round 2's mutation fix over-applied: making `item.json` immutable and nodes kind-stable was
right; extending write-once to the one file whose entire purpose is to report changing progress is
not. The fix is confined to §3.2/§3.4 — e.g. `STATUS` is written by the tmp-rename rule and is
last-write-wins (the presence rule still holds: the file is always complete), with only `done` and
`escalated` terminal; or non-terminal progress moves into `RUN` and `STATUS` is written once, at
the end. Either is a seam edit. **This does not touch the joint.**

### F2 — `major` — group nodes have no attempt counter and no cap; §3.5's termination claim is false for them

*(logical; completeness)*

§3.2 defines `RUN` as *"the number of times **the driver has dispatched this node**"*, incremented
*"before each dispatch."* §3.5's driver table, row *"no `STATUS`"*, splits: *"leaf → increment
`RUN` and dispatch A's entry agent (§3.3). **group → run the roll-up once every child has a
`STATUS`.**"* — the group branch names no increment. §3.5 then asserts: *"**Every path
terminates**: each node is either terminal or has a strictly increasing `RUN` bounded by
`run.max_attempts`."*

**Failure scenario.** Group node `0.2` has three children, all with `STATUS`. The roll-up agent is
dispatched and fails to return (tool error, or it dies between reading its children and renaming
its own `STATUS.tmp`). No `STATUS` is written for `0.2`. On the driver's next pass, `0.2` still
matches *"no `STATUS`"* and *"every child has a `STATUS`"*, so the roll-up is dispatched again —
with nothing incremented, nothing capped, and no escalation possible, because the only escalation
trigger in §3.5 is `RUN ≥ run.max_attempts`. The run loops on `0.2` indefinitely. §3.4 also gives
groups no `failed` state (*"group: `done` | `partial` | `escalated`"*), so B has no state to write
even if it detected the condition.

Both the counter and the cap are seam text (§3.2, §3.5), so B cannot fix this within its own half.

### F3 — `major` — group `escalated` is not computable from what the roll-up is permitted to read; a permanently stuck subtree rolls up as `partial` (= re-runnable) forever

*(logical; fidelity; this is round 2's C-F2/A-F3 recurring, and §7 records it as closed)*

§3.4 defines the group states by reference to a property the roll-up cannot observe: *"`escalated`
— at least one child is `escalated` **and no child is re-runnable**"*, with *"`partial` — anything
else."* §3.5 puts the exhaustion fact in exactly two places: *"the driver records the exhaustion in
`decisions.md` and **treats the node as `escalated`** for roll-up and termination purposes."* §3.2's
read table then forbids the roll-up coordinator both of them by name: *"the `STATUS` lines of its
own children, and nothing else. Not `item.json`, **not `RUN`, not `decisions.md`**, not a finding,
not the corpus."*

**Failure scenario.** Leaf `0.1` fails repeatedly and exhausts `run.max_attempts`; its `STATUS`
still reads `0.1 failed 0 0 0` (the driver is told to write nothing). Leaf `0.2` reads
`0.2 done 5 1 3`. The roll-up for node `0` is handed those two lines. No child's state field is
`escalated`, so §3.4's `escalated` clause does not fire; the `done` clause does not fire; the rule
falls through to *"`partial` — anything else."* Node `0` is written as `0 partial 5 1 3`. But §3.4
defines `partial` as the re-runnable state, so **the corpus-level status of a run that is
permanently dead reports "keep going."** A human or a wrapper reading the root `STATUS` — the only
artefact P5's blindness makes authoritative — is told the wrong thing.

§7 records this as fixed: *"No terminal failure state; `failed` means re-run forever (C-F2, A-F3) →
§3.4 `escalated` + §3.5 `RUN`/`run.max_attempts`."* The leaf half of the fix works. The group half
does not, because the terminality fact was placed in `RUN` and `decisions.md`, which are precisely
the two files P5's blindness mechanism removes from the coordinator. The fix must be a fifth-field
change or a state change visible in the `STATUS` line itself — seam work, and it interacts with F1
(if `STATUS` becomes rewritable, the driver can simply write `escalated` on exhaustion and this
finding dissolves).

### F4 — `major` — an over-size item that cannot be split is removed from the leaf set and then belongs to no category the seam defines; it rolls up as `done` or vanishes

*(completeness; coverage — this is the one orphaned remainder I found)*

§3.5: *"An item that cannot be brought within the bound **is not emitted as a leaf**: it is
recorded in `index.md` and `decisions.md` and escalated to the human at decomposition time."*

§3.2 admits exactly two kinds of node: *"A node is a LEAF — an item — **if and only if** it has
`item.json`; **otherwise it is a GROUP** whose children are the nodes one level below it."* There
is no third kind, and the seam is explicit that the skeleton is exhaustive and neither half may add
to it. So the escalated item is one of two things, and both are broken:

- **If B creates a node directory for it** (natural — it is *"recorded in `index.md`"*), it has no
  `item.json`, therefore it is a GROUP, therefore a group with **zero children**. §3.5's driver
  table says *"group → run the roll-up once every child has a `STATUS`"* — vacuously satisfied. The
  roll-up is handed zero `STATUS` lines and applies §3.4: *"`done` — **every** child is `done`"* —
  vacuously true over the empty set. **The item the decomposer escalated to the human is written
  `done 0 0 0` and propagates `done` upward.** The one condition the human was told about is the
  one the status tree reports as success.
- **If B creates no node directory for it**, then §3.8's assembly rule — *"One section per **leaf
  node** in `index.md` order"*, with its three cases all predicated on being a leaf — emits nothing
  for it. The over-size content is **absent from `findings.md` with no marker at all**, which is
  worse than the `NOT RUN` case §3.8 was careful to define.

Nothing in §2-B, §3.2, §3.4, §3.5 or §3.8 disambiguates, and B cannot fix it — the leaf/group IFF,
the group-state rules and the assembly rule are all seam text. The seam needs either a third node
kind with a defined `STATUS` (e.g. the decomposer writes `<id> escalated 0 0 0` directly), or an
explicit statement that such an item is emitted as a leaf whose `STATUS` decomposition pre-writes.

### F5 — `major` — the `SEAM-OBJECTION` transport does not survive `Consensus`; §3.9 is not executable as described

*(factual; logical; this is round 2's C-F5/A-F6/B-M7, which §7 records as closed)*

§3.9 instructs a half that thinks the seam is wrong to *"write a clearly-labelled `SEAM-OBJECTION`
section at the head of your plan output"*, and justifies its survival with: *"`Union` discards
nothing (`Architect/stages/combiner.md`: 'Stick the inputs together into one. DISCARD NOTHING.'),
so it travels upward unmodified to the node that owns this seam."*

The `leaf.md:47` citation is accurate — I verified it verbatim (*"You do not file findings — your
output is a plan, and severities are for reviewers."*). **The transport half is wrong.** Per
`node.md:85-88`, a division's two halves are handed to **child nodes**, not to leaves. A child node
whose own `Divisible` returns `null` dispatches **three leaves** and merges with **`Consensus`**,
not `Union` (`node.md:81-84`: *"dispatch three leaves … Then `plan = Consensus(the three leaf
plans)`"*). And `combiner.md` is unambiguous about what `Consensus` does: *"**2-of-3 on numbered
steps, INCLUDING ORDER. The odd plan is discarded.**"*

**Failure scenario.** One of the three leaves planning half B notices that §3.3's item record gives
A no way to reach `decisions.md` (F6) and writes a `SEAM-OBJECTION` at the head of its plan. The
other two do not. `Consensus` discards the odd plan; the objection is gone before it reaches any
`Union`. Even in the two-of-three case, a `SEAM-OBJECTION` is a prose section, not a numbered step
at a matching sequence position, so `Consensus` has **no rule under which it is carried** — the
combiner is explicitly barred from authoring one (*"You do not improve, rewrite, or adjudicate"*).
The first hop above a leaf is `Consensus`, and §3.9 assumes it is `Union`.

**Second-order, and it re-opens the non-termination half of the round-2 finding.** Suppose an
objection does reach a child node's merged plan. That node then red-teams the plan
(`node.md:101-108`), the plan reviewers see a section describing a defect, findings become
`task = Severity(issues)`, and the node loops on a task about a seam its own charter forbids it to
change — precisely what `combiner.md` warns of: *"it is handed to a planner that cannot fix it, and
it comes back to you next iteration unchanged, forever."*

A workable form is to name the transport that actually exists: the child **node**, not the leaf,
is the escalation point, and node.md's `FAILED_TO_DIVIDE`/escalation path or `decisions.md` is
where a seam objection has to land. That is seam text, and it interacts with nothing in the joint.

### F6 — `major` — A is obliged to append to `decisions.md`, has no path to it, and §3.3 forbids adding the field that would give it one

*(completeness; logical)*

§3.2's read table, row *"A's roles (stages 2–4)"*, Writes column: *"their own item's outputs, the
leaf `STATUS`, **appends to `decisions.md`**"*. §3.7 rule 3 carves out the same duty for every
dispatched agent: *"except appends to `decisions.md`, which every role may make one complete line at
a time."* `decisions.md` lives at `<run.dir>/decisions.md` (§3.2 skeleton).

A's entry agent receives **one** argument (§3.3: *"exactly ONE argument: `item_dir` (absolute)"*),
and §3.3's field list is closed: *"**Exactly these fields; A may not require others**, B may not
omit any."* No field carries `run.dir`, `decisions.md` or anything from which they can be safely
derived. §3.3 states the opposite as a design intent — *"`item_dir` … so **A never has to resolve
`run.dir`**"* — which is false the moment A is given a write duty against a run-level file.

Derivation is not a reliable escape, because **§3.2 contradicts itself about directory nesting**:
the skeleton writes `nodes/<node_id>/` (one directory literally named `0.1.2`, from which `run.dir`
is two levels up), while the prose says *"`<node_id>` is dot-separated (`0`, `0.1`, `0.1.2`) and
**directories nest to match**"* (three directories, from which `run.dir` is four levels up). A's
planner, blind to B's, picks one; B's decomposer picks the other; the paths do not meet. The same
ambiguity independently affects B's driver walk, `index.md` ordering and §3.8's assembly, though
those at least all sit inside one half.

Fix in the seam: add `run_dir` (or `decisions_path`) to §3.3's field list, **or** drop A's
`decisions.md` duty and route A's run-log lines through its own item directory. Also pick one
nesting convention and state it once.

### F7 — `minor` — B's run driver has global read of the tree; the seam argues P5's blindness for the roll-up only and never addresses the driver

*(unstated assumptions & risks)*

P5 says *"a coordinating agent reads only a terse per-child status."* §3.2's read table gives B's
run driver *"`index.md`, any `item.json`, any `STATUS`, any `RUN`, `decisions.md`, the config"* —
the whole tree, not one child's line. **I am not filing this as a fidelity failure**, and I think
the divider's reading is the right one: §1 pins the boundary at *"reads for meaning, and emits or
sees a finding"*, the driver honours *"**Never a finding**"*, and a driver that could not see the
tree could not drive it. But the seam nowhere states *which* coordinating agent P5 constrains, and
B's `METHODOLOGY.md` will have to explain to a reader why one coordinator reads everything and
another sees five fields. Add one sentence to §3.2 fixing the interpretation, and instruct B to
state it in `METHODOLOGY.md` — otherwise B's planner may over-restrict the driver, or a later
reviewer of the built skill reads the driver as a P5 violation.

### F8 — `minor` — nobody owns corpus immutability across a resume, which silently invalidates citations

*(unstated assumptions & risks; completeness)*

§3.3's `locator` is an absolute path plus *"inclusive, 1-based line numbers"*, captured at
decomposition time and validated then (*"B validates every `locator` at decomposition time"*).
§3.5's resume path re-dispatches leaves on a later pass, potentially much later. Nothing in §3.3,
§3.5, §3.2 or either sub-task assigns anyone the duty of detecting that the corpus changed in
between.

**Failure scenario.** Item `0.4` is analysed; three analysts' outputs cite `data/log-07.txt:412`.
The run dies. A line is prepended to `log-07.txt`. The run resumes; A's within-item resume (§2-A:
*"must not redo completed work; it uses the presence rule"*) trusts the existing analyst outputs
and runs only verification and merge. The verifier (P3) now resolves `:412` against shifted content
— it either drops correct findings or, worse, confirms citations that now point at different text.
The method's central guarantee (P3 + "source-cited") fails silently and the `STATUS` line reports
success.

The cheap fix is a `size_bytes`-plus-`mtime` or content-hash field in `item.json` with a stated
re-validation rule, or an explicit stated assumption that the corpus is frozen for the run's
duration, recorded in `METHODOLOGY.md`. Because it touches §3.3's closed field list and spans P3
and P7, it is seam work rather than a planner detail — hence filed rather than left.

### F9 — `minor` — `locator` fixes lines as the only addressing unit, narrowing "corpus-agnostic", and no half is told to document the limit

*(completeness; fidelity)*

§3.3: *"`{"path": …, "lines": [<first>, <last>]}` … **Lines are the unit, fixed here.**"* Fixing the
unit in the seam is the right call for self-containment and I am not asking for it to be
parameterised. But P6 requires *"a per-corpus Layer-2 config so the method stays
corpus-agnostic"*, and §2-B tells B's decomposer to split *"along the structural boundaries the
Layer-2 config names"* — for a corpus of PDFs, images, a mailbox, a database, or JSONL records
addressed by record id, the decomposer can find those boundaries but the seam has no way to write
them down. The built skill will therefore claim corpus-agnosticism it does not have. Add to §3.3
(or to B's `METHODOLOGY.md` obligations in §2-B) a one-line scope statement: this method addresses
line-addressable text corpora, and a non-line-addressable corpus is out of scope for this
implementation.

### F10 — `nitpick` — "letter-suffixed files … as the siblings do" over-generalises one sibling

*(factual)*

§3.1: *"each half may add letter-suffixed files within its own phases (`stage-0a.md`, as the
siblings do)"*. Only Dragonfly does this — `Dragonfly/stages/` contains `stage-0a.md` and
`stage-0b.md`. `Guarded_change/stages/` uses a **decimal**: `stage-1.5.md`. Since the seam grants
only the letter form, a planner checking house style against `Guarded_change/stages/` will find a
convention the seam forbids. Say "as Dragonfly does", or permit both forms.

---

## The six lenses — a verdict for each

### 1. Factual — one `nitpick` (F10); otherwise clean, and earned

I opened and checked every `file:line` the proposal cites. All of the following resolve and say
what is claimed:

- `Guarded_change/SKILL.md:28` — *"**Step numbers below are the canonical stage numbers used
  everywhere**"* ✓ (§3.1's quote is verbatim and correctly attributed; §7 records this as the fix
  for round 2's C-F13 misattribution to `Dragonfly/SKILL.md`, and the fix is real — the equivalent
  Dragonfly line is at `Dragonfly/SKILL.md:34`, worded differently.)
- `Guarded_change/SKILL.md:27` — `changes/<slug>/` ✓
- `Dragonfly/SKILL.md:31` — `hunts/<slug>/` ✓ and `Dragonfly/METHODOLOGY.md:143` — *"One folder per
  hunt, e.g. `hunts/<slug>/`"* ✓. Both are **documentation of a convention**, not an on-disk path
  claim, which is what §7 says was required to close round 2's A-F14. Real fix.
- `Dragonfly/SKILL.md:19` — *"**Validate config paths at hunt start**"* ✓
- `Guarded_change/METHODOLOGY.md:139` — *"**Paths are validated, not assumed.**"* ✓
- `Dragonfly/stages/charter.md:1` — *"# The red-team charter (shared by stages 1, 4, 7)"* ✓, and
  `Guarded_change/stages/charter.md:1` reads *"(shared by stages 3 and 6)"* — §3.7's claim that both
  siblings have a `charter.md` read at *specific* stages is accurate for both.
- §3.7's claim that **neither sibling has a `common.md`** ✓ — `ls` of both `stages/` directories
  confirms it (`Guarded_change/stages/`: charter, 0, 1, 1.5, 2–8; `Dragonfly/stages/`: charter,
  0a, 0b, 1–9). The universal-preamble pattern being Architect's own ✓ —
  `Architect/stages/common.md:3`: *"Every agent Architect dispatches reads this file first, then its
  role file."*
- `Architect/stages/leaf.md:47` — *"You do not file findings — your output is a plan, and severities
  are for reviewers."* ✓ verbatim (the §3.9 conclusion drawn from it is wrong for a different
  reason — see F5).
- `Architect/stages/combiner.md` — *"Stick the inputs together into one. DISCARD NOTHING."* ✓;
  *"None of the three is an author. You do not improve, rewrite, or adjudicate the material."* ✓;
  *"A genuine conflict is kept, not resolved."* ✓; *"it is handed to a planner that cannot fix it,
  and it comes back to you next iteration unchanged, forever."* ✓
- §2-A's precedent list — `Guarded_change/stages/stage-3.md` is *"Stage 3 — Red-team the plan …
  independent cold review"* ✓ and `Dragonfly/stages/stage-7.md` is root-cause confirmation *"after
  the causal chain has passed a direct cold red-team"* ✓. Both are genuine cold-reviewer prompts
  with an evidence bar, as described.
- §2-B's precedent list — every named `Dragonfly/METHODOLOGY.md` section exists: *Why this exists*
  (:22), *The loop* (:45, and it is genuinely a **diagram** — a fenced 0a–9 block), *Stage index*
  (:72), *The two layers* (:95), *The config contract (Layer 2)* (:106), *What a run produces
  (artifacts)* (:141), *Human-in-the-loop* (:172) ✓. `Dragonfly/dragonfly.companion.md` and
  `Guarded_change/guarded-change.companion.md` are genuine worked Layer-2 configs with a YAML block
  inside markdown ✓, which is what §3.6 asserts about config format.
- §3.1's `name: data-distiller-impl` and §7's note that B-n1 (*"matching the directory" overstates
  the precedent*) was softened ✓ — `Dragonfly/` → `name: dragonfly`, `Guarded_change/` →
  `name: guarded-change`; neither matches its directory literally, and §3.1 no longer claims it
  does.

**§7's disposition claims, checked as claims.** The round-2 blocker (invocation target/arity) **is**
genuinely closed by §3.3. The `oversize` removal **is** genuine and is the right call — but it
leaves F4. Two entries are **not** closed despite being recorded as closed: C-F2/A-F3 (see F3) and
C-F5/A-F6/B-M7 (see F5).

### 2. Logical — F1, F2, F3, F4, F5, F6

Five of the six are the same shape: a rule stated in one section of the seam is contradicted or
made unexecutable by a rule in another section of the seam. F1 (write-once vs. re-runnable), F2
(cap defined for leaves, termination claimed for all), F3 (state defined over facts the reader may
not read), F4 (an entity outside the exhaustive taxonomy), F6 (a write duty with no path, plus a
self-contradictory nesting rule). F5 is a mis-modelled control flow. None is a flaw in the cut.

### 3. Missed opportunity — no finding

I looked for a better joint and did not find one. The recorded alternative (method vs. envelope) is
correctly rejected for the reason given — it is a packaging boundary and the envelope half is
derivative documentation of a method it does not own. I also considered *"all dispatched agent
prompts" vs. "all documentation and config"* (splits P5's roll-up prompt from the `METHODOLOGY.md`
that explains it, and gives one half no coherent design concern) and *"decomposition + pipeline"
vs. "orchestration + surface"* (puts the sizing bound and the acceptance bound on opposite sides,
re-creating the cross-half key invariant this proposal is careful to bound). Both are worse. §5's
handling of the size imbalance — acknowledge it, keep the joint, let B's own `Divisible` cut it —
is the correct move and matches `divider.md`'s framing that evenness is not the test.

### 4. Unstated assumptions & risks — F7, F8

Also flagged as **unchecked**: the proposal assumes A's within-item resume can be made idempotent
from the presence rule alone (§3.3: *"Re-dispatch of the same leaf is **safe**"*). Whether that
holds depends on A's per-item file layout, which A has not planned yet, so I could not check it. It
is a reasonable assumption and I am not filing it — but it is an assumption the seam asserts as a
fact, and if A's plan turns out to need a partial-write marker, the exhaustive-skeleton rule (§3.2:
*"Neither half may add a file or directory to it"*) forbids one. Recording it here rather than
losing it.

### 5. Fidelity — clean, earned by pinning every loaded term

Each operational term in the task, and the concrete mechanism the seam pins it to:

| Term | Pinned to | Verdict |
|---|---|---|
| **cold** | §3.7 rule 1 — *"no shared context with its caller or its siblings"*, plus §3.7 rule 2 | mechanism, not proxy |
| **read-only** | §3.7 rule 3 — writes nothing but its named outputs via tmp-rename; §2-A additionally makes A state *"what 'read-only' concretely forbids an analyst"* | mechanism |
| **decompose** | B's stage 0: split along config-named structural boundaries, emit `item.json` per leaf, validate every `locator` before writing | mechanism |
| **N independent analysts** | A's entry agent's dispatch point; §2-A requires *"no shared context, no visibility of a sibling's output"* and a justified default N | mechanism |
| **verify / unverifiable** | A's stage 3: a separate cold agent, **explicitly never the analyst that produced the finding**, with an operational definition of "unverifiable" and a stated fate for dropped findings | mechanism |
| **agreement-ranked merge** | A's stage 4, with `max_agreement` pinned in §3.4 to *"non-negative integer count of **analysts**"* — agreement is analyst-count, not similarity score | mechanism |
| **blind roll-up** | §3.2 read table (children's `STATUS` lines and nothing else) + §3.4's five-field line + the **deliberate absence of a path field**, justified at §3.4: *"putting the locator of the findings into the blind coordinator's only input turns P5 from a structure into an exhortation"* | **the strongest pin in the document** |
| **terse per-child status** | five whitespace-separated fields with fixed domains, §3.4 | mechanism |
| **Layer-2 config / corpus-agnostic** | one YAML-in-markdown file per the siblings' companion pattern, namespaces partitioned §3.6 | mechanism (narrowed — F9) |
| **restart and resume from on-disk state** | the presence rule + `RUN` + `STATUS` absence as the only "not yet" marker | mechanism, but **broken** — F1, F2 |
| **facts, not interpretation** | §3.7 rule 7 states the duty; §2-A requires A to write it into role prompts *"as an **enforceable rule** rather than an exhortation"*, and §3.7's closing paragraph resolves the additions-only collision | mechanism, correctly separated from duty |

No term is implemented by a proxy. The additions-only discipline (§3.1, §3.7 closing) is the one
place where a fidelity slip was likely — a common-file duty being restated as a role-file
mechanism — and it is explicitly handled.

### 6. Completeness — F4, F6, F8, F9; generative sweep run

Required-section check first: the proposal has the joint, both sub-tasks, a stated seam, a coverage
table, a floor check, a self-containment audit and a disposition table — the structure
`redteam-split.md` implies is all present.

**Generative sweep — what load-bearing thing does the eight-property list itself not anticipate?**
I swept for: an output **location** for every artefact (covered — §3.2 skeleton is exhaustive and
every file has a named writer); a **restart story** (covered but broken, F1/F2); a **termination**
proof (claimed at §3.5 and false for groups, F2); a **failure mode** for every state in §3.4's
domain (covered for leaves, incomplete for groups, F3); the **degenerate inputs** — empty corpus,
single-item corpus (covered, §2-B), zero surviving findings (covered, §3.4's `0`), an
**unsplittable** item (**not covered — F4**); the **human interface** (covered — stop-for-human
declaration obligation + §3.5's escalation); an **argument channel** for every file an agent must
touch (**not covered — F6**); **input stability** over the run's lifetime (**not covered — F8**);
the **addressing model's** applicability (**narrowed silently — F9**); a **test harness / eval**
(deliberately out of scope at §3.10, labelled challengeable — I agree with the ruling; the task
asks for a plan to build the skill and the siblings ship no harness of their own); **concurrency
bounds and cost** (owned by B's driver, §2-B); **`.tmp` cleanup after a death** (harmless under the
presence rule — not filed); the **`SEAM-OBJECTION` escalation path** (present but mis-modelled,
F5).

---

## Summary table

| # | Severity | Lens(es) | Where | One line |
|---|---|---|---|---|
| F1 | **blocker** | logical, fidelity | §3.2, §3.4, §3.5 | `STATUS` write-once makes every re-dispatch unrecordable; `done` unreachable after any `partial` |
| F2 | major | logical, completeness | §3.2, §3.5 | groups have no `RUN` increment and no cap; "every path terminates" is false for them |
| F3 | major | logical, fidelity | §3.2, §3.4, §3.5 | group `escalated` depends on `RUN`/`decisions.md`, which the roll-up may not read |
| F4 | major | completeness, coverage | §3.2, §3.5, §3.8 | an unsplittable over-size item is neither leaf nor group; rolls up `done` or vanishes |
| F5 | major | factual, logical | §3.9 | `SEAM-OBJECTION` rides `Consensus` first, which discards it |
| F6 | major | completeness, logical | §3.2, §3.3, §3.7 | A must append to `decisions.md` with no path to it; nesting rule self-contradictory |
| F7 | minor | assumptions | §3.2 | driver's global read vs. P5's wording is never addressed |
| F8 | minor | assumptions, completeness | §3.3, §3.5 | no owner for corpus drift across a resume; citations silently invalidated |
| F9 | minor | completeness, fidelity | §3.3 | line-only `locator` narrows "corpus-agnostic"; no half told to state the limit |
| F10 | nitpick | factual | §3.1 | "as the siblings do" — only Dragonfly uses letter suffixes |

**Restating the verdict, because the divider needs it unambiguous: I do not object to going
forward with this cut. Keep the joint.** F1–F6 are seam-text defects that no blind planner can act
on and that §3's own preamble forbids either half from changing, so they need a round-4
re-derivation of §3 with the joint held fixed. F7–F10 can ride down with the sub-tasks.
