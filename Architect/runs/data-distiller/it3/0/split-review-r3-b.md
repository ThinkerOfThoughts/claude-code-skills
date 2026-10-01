# Split review — round 3, reviewer B (cold)

Reviewing the **proposed division** at
`Architect/runs/data-distiller/it3/0/split-round-3.md`. I hold no plan and was given none.

**Off-limits declaration.** I did **not** read, list, grep, glob or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke
the installed `data-distiller` skill. I read the two sibling skills
(`Guarded_change/`, `Dragonfly/`) and the Architect stage files, both of which are in scope. I did
not read any `split-review-*.md`. I did not read `split-round-1.md` or `split-round-2.md`; I judged
round 3 on its own text, and treated §7's disposition claims as claims.

---

## VERDICT — the two parts

**Part 1 — what I found.** One `blocker`, six `major`s, three `minor`s, one `nitpick`. **Every one
of them is a defect in the seam text (§3), not in the joint.** The pattern of round 2 repeats
exactly: the cut is right and the contract written across it is not yet sound. Three of my findings
(F1, F2, F4) are the *same class* round 2 bounced — "a state in the vocabulary with no producer, or
a transition the rules forbid" — surviving in new clothing after the `oversize` removal. §7's claim
that this class is disposed of does not hold.

**Part 2 — do I object to going forward with this cut?** **No. I do not object. I endorse the
joint and would keep it.** The finding boundary is the boundary the task statement itself draws
(P5), the two sides differ in inputs, outputs, failure modes and review criteria, and the divider's
rejected alternative (method vs. envelope) is correctly rejected as a packaging line. My findings
travel down with the sub-tasks and with the seam; none of them is a reason to re-cut.

---

## The four questions, answered directly

**1. Coverage.** P1–P8 each have exactly one owner and I found no property both halves assume the
other owns. One genuine orphan: **corpus content that decomposition could not bring within the size
bound leaves the node tree entirely** (F4). One near-orphan: **the `escalated` state has no
producer** (F2).

**2. The seam — stated, sound, self-contained.** **Stated:** yes, in unusual and commendable
detail. **Self-contained:** yes for the artifacts §6 audits — I looked specifically for the
producer/consumer form redteam-split warns about and the item record, the invocation contract, the
STATUS schema, the skeleton, the stage numbering and the config namespaces are all genuinely fixed
in the seam rather than derived. Two exceptions survive: the **numeric size-bound agreement** (F5)
is a plan-time cross-half agreement stated as an invariant but never fixed to a value or resolved
by a build-time rule, and **`decisions.md`** is a file both halves write with no fixed location for
A and no fixed line format (F8). **Sound:** no — F1, F2, F3, F4 are soundness defects in the
control loop.

**3. The floor.** No finding. A plans at least three role-prompt files plus its finding and
citation formats; B plans at least nine files. Both are whole tasks far above *"one file created,
with the content that goes in it specified."* Neither half falls below the floor and the division
is legitimate on this ground.

**4. Real joint or arbitrary cut?** **Real joint.** What differs across it: what the agent reads
(content-for-meaning vs. shape and one-line records), what it produces (evidence vs. bookkeeping),
its characteristic failure (a fabricated citation vs. a coordinator that peeks / lost work on
restart), its unit of work (one item vs. the corpus and the tree), and its review criterion (do
citations resolve vs. is it blind and idempotent). §1's table is not decoration — I checked each row
against §3's mechanisms and each holds. **P5 is the assertion that this line exists**, so a divider
cutting anywhere else would have had to cut *through* a task-stated invariant.

---

## Findings

### F1 — `blocker` — `STATUS` is write-once, so the entire re-dispatch/resume path is inert (P7)

**Where.** §3.2 (*"`STATUS` is never overwritten"*), §3.4 (*"**WRITE-ONCE**"*, `partial` is
*"**Re-runnable.**"*), §3.5 driver table row 3 (*"`state=partial` or `state=failed` → if `RUN <
run.max_attempts` → increment `RUN` and re-dispatch"*), §3.5 divider's note (which explicitly
rejects allowing one `STATUS` replacement), §2-A (*"**Writing the leaf `STATUS` line** (§3.4) as the
last act of your pipeline"*).

**The defect.** A leaf writes `partial`. The driver re-dispatches it. A's pipeline resumes, finishes
the remaining phases — **and cannot record that it finished**, because its last act is to write a
write-once file that already exists. The observed state can never change. The driver therefore
re-dispatches exactly `run.max_attempts` times, observes `partial` every time, and escalates a node
that succeeded on attempt 2.

**It is worse than a lost update.** §3.2's presence rule says *"the existence of a file means the
step that produces it finished"* and §2-A tells A to resume *"using the presence rule (§3.2)."* A
re-dispatched pipeline applying that rule to its own final output sees `STATUS` present, concludes
its last step is done, and **returns immediately having done nothing.** So `partial` is not merely
unrecordable-as-improved; it is a fixed point. Every `partial` and every `failed` leaf inevitably
burns the full attempt budget and escalates, whatever actually happens on re-run.

**Why it is a `blocker` and not a `major`.** P7 — *"restart and resume from on-disk state"* — is one
of the eight defining properties. As written, the mechanism the seam specifies for it cannot
achieve its stated purpose, and **neither half may fix it**: §3.9 forbids adjusting the seam
locally, and the write-once rule is stated three times and defended once. A defect that the halves
are explicitly barred from repairing and that disables a named property is not a finding the
planners below can carry.

**Note the trade the divider was making.** The `oversize` removal was right and mutation *is* what
produced round 2's majors — but the fix over-reached from *"nothing changes kind"* (correct, and
sufficient) to *"nothing is ever rewritten"* (too strong, and it took P7 with it). See F12 for a
resolution that keeps both.

### F2 — `major` — `escalated` is in the state domain with no producer; the blind roll-up cannot represent terminal failure

**Where.** §3.4 (*"`escalated` — **terminal, do not re-run**… Written when the attempt cap in §3.5
is reached"*) vs. §3.5 driver table row 3 (*"If `RUN ≥ run.max_attempts` → **write nothing to
`STATUS`**… instead the driver records the exhaustion in `decisions.md` and **treats the node as
`escalated`***").

**The defect.** Nobody ever writes `escalated` to a leaf. §3.4 says A writes the leaf states, and A
cannot: `run.max_attempts` is in `run.*`, B's namespace, which §3.6 forbids A to read. §3.5 says
the driver deliberately writes nothing. So the leaf's on-disk `STATUS` says `partial` or `failed`
forever, and the escalation exists **only in `decisions.md`.**

**The consequence lands squarely on P5.** §3.2's read table gives B's roll-up coordinator *"the
`STATUS` lines of its own children, and nothing else. Not `item.json`, not `RUN`, not
`decisions.md`."* The roll-up therefore cannot see the escalation, so §3.4's group rule
(*"`escalated` — at least one child is `escalated`"*) can never fire at any level. **The group
`escalated` state is unreachable too, and the root of a run that gave up reports `partial`** — the
same string a run still in progress reports. The blind coordinator's one job is to summarise a
subtree it may not look into, and the vocabulary it was given cannot express "this subtree is
finished and failed."

This is round 2's *"nobody assigned to produce `state=oversize`"* (C-F3 / A-F1 / B-M4, per §7)
recurring at a different state. §7 records that class as fixed by removing `oversize`; removing the
state removed the instance, not the class.

### F3 — `major` — the driver's no-`STATUS` row is uncapped, so §3.5's termination claim is false in exactly the case `RUN` was introduced for

**Where.** §3.5 driver table row 1: *"no `STATUS` | leaf → increment `RUN` and dispatch A's entry
agent (§3.3)"* — unconditional, with no reference to `run.max_attempts`. Two paragraphs later:
*"**Every path terminates**: each node is either terminal or has a strictly increasing `RUN` bounded
by `run.max_attempts`."*

**The defect.** The cap is consulted only on the row keyed to `state=partial or failed`, which
**presupposes a `STATUS` exists.** If A's entry agent dies before writing `STATUS` — the case §3.2
introduces `RUN` to detect (*"which distinguishes *never started* from *started by a run that
died*"*) — the driver falls through to row 1 on every pass and re-dispatches forever. `RUN`
increments, is never read, and the node never becomes terminal.

**Failure scenario, concretely.** Item `0.3` is unreadable in a way that makes A's entry agent
crash rather than return. Pass 1: no `STATUS`, `RUN`→1, dispatch, crash. Pass 2: no `STATUS`,
`RUN`→2, dispatch, crash. …forever. Node `0`'s roll-up is gated on *"once every child has a
`STATUS`"*, so the group never rolls up, the run never terminates, and `findings.md` — whose §3.8
rule has a case for *"a leaf with no `STATUS`"* — is never assembled because nothing reaches the
final stage. The seam asserts termination it does not implement, and B, planning blind, will
implement the table rather than the assertion.

### F4 — `major` — corpus that decomposition cannot bring within the bound leaves the tree, and is reported as success or not reported at all

**Where.** §3.5: *"**An item that cannot be brought within the bound is not emitted as a leaf**: it
is recorded in `index.md` and `decisions.md` and escalated to the human at decomposition time."*
Against §3.2 (*"A node is a **LEAF** — an item — if and only if it has `item.json`; otherwise it is
a **GROUP** whose children are the nodes one level below it"*), §3.4's group rules, and §3.8's three
assembly cases.

**The defect.** The seam creates a third kind of `index.md` entry — recorded, but neither a leaf nor
a group with children — and then defines nothing over it. Both readings of *"not emitted as a
leaf"* fail:

- **If B creates a node directory without `item.json`**, it is a GROUP by §3.2's iff-rule, with zero
  children. §3.5 row 1: *"group → run the roll-up once every child has a `STATUS`"* — **vacuously
  satisfied**. §3.4: *"`done` — every child is `done`"* — **vacuously true**. The node rolls up
  `done` with `0 0 0`, its parent sums it in, and **a run that never analysed part of the corpus
  reports `done` at the root.**
- **If B creates no node directory**, the content is absent from the tree entirely. §3.8's assembly
  rule is *"one section per **leaf node** in `index.md` order"* with three cases, none of which
  covers a non-leaf entry, so the un-analysed content **contributes nothing to `findings.md`** and
  leaves no trace in the run's terminal artifact.

Either way, the one failure mode that most threatens a distillation method — *content silently not
distilled* — is invisible in both the roll-up and the assembled output. It survives only in
`decisions.md`, which §3.2 bars the roll-up from reading.

**Not fixable inside one half despite B owning both ends.** B owns stage 0 *and* stage 5, so it
might seem B can define a convention. It cannot: §3.2's leaf/group iff-rule, §3.2's *"the skeleton
is **EXHAUSTIVE**"*, §3.4's group state rules and §3.8's assembly rule are all seam text, and §3.9
forbids B from adjusting any of them. A defect the owning half is barred from repairing belongs in
the seam.

### F5 — `major` — the size-bound invariant is a plan-time cross-half agreement with no fixed value and no build-time resolution

**Where.** §3.5: *"A declares `analysis.max_item_bytes` and B declares `sizing.max_item_bytes`; **the
seam's invariant is `sizing.max_item_bytes ≤ analysis.max_item_bytes`**, and B states that invariant
in `METHODOLOGY.md`'s config contract as a rule over the merged plan's declared keys (§3.6)."*

**The defect.** Stating an invariant is not satisfying it. The two halves choose their two defaults
**concurrently and blind**, from disjoint namespaces neither may read. §3.6's build-time rule
produces a worked example config carrying *"one entry per key declared by either half's plan, with
its declared meaning, type and default"* — so it faithfully transcribes whatever pair of numbers
the two halves happened to pick, **including a pair that violates the invariant.** The seam
provides no rule for that case. A practitioner holding the merged plan reaches a documented
invariant that the documented defaults break, and must invent a number — the precise
"B invents it and looks locally correct" failure redteam-split flags.

**Failure scenario.** A, reasoning about context windows, defaults `analysis.max_item_bytes` to
120 000. B, reasoning about clean structural boundaries in logs, defaults `sizing.max_item_bytes` to
400 000. Merged: decomposition emits leaves up to 400 KB, A's entry agent writes `state=failed` on
every one of them (§2-A, *"your acceptance bound"*), and **an out-of-the-box run distils nothing.**
Compounded by F1 and F2, every such leaf then burns its attempt budget and escalates silently.

**This is cheap to fix in the seam** — fix the numeric bound outright, or state it as a build-time
rule with a resolution (*"if the declared defaults violate the invariant, `sizing.max_item_bytes`
takes A's declared `analysis.max_item_bytes` value"*), which a practitioner holding the merged plan
can execute. Both belong in §3, not in either half.

### F6 — `major` — §3.9's `SEAM-OBJECTION` transport assumes `Union` all the way up; `Consensus` sits between the objecting leaf and the first `Union`, and discards the odd plan

**Where.** §3.9: *"write a clearly-labelled `SEAM-OBJECTION` section at the head of your plan
output… `Union` discards nothing (`Architect/stages/combiner.md`: *'Stick the inputs together into
one. DISCARD NOTHING.'*), so it travels upward unmodified to the node that owns this seam."* §6
repeats it: *"§3.9 uses `Union` only as a **transport** (discard-nothing), which its charter does
guarantee."*

**The defect.** The recipients of these two sub-tasks are **child nodes**, not leaves
(`node.md:85–88`: *"Division is non-empty: … spawn **two child nodes**"*), and a node *"never
write[s] plan content"* (`node.md:35`). The `SEAM-OBJECTION` can therefore only be authored much
further down, by a leaf, and its first merge upward is **not** `Union` — it is `Consensus`
(`node.md:80–84`: division-is-null nodes dispatch three leaves and merge with `Consensus`).
`Consensus` is the opposite rule: `combiner.md:22` — ***"2-of-3 on numbered steps, INCLUDING ORDER.
The odd plan is discarded."***

So a seam objection survives **only if two of three independently-dispatched cold leaves write
substantially the same objection at the same point in their sequences.** A correct objection raised
by one leaf — the likeliest case, since it is exactly the lone-observation case the design
elsewhere protects — is deleted before it reaches any `Union`. §3.9 is the seam's only escape hatch
and it is unreliable in the case it exists for. Round 2 bounced §3.9 once (per §7: *"§3.9's
amendment path unexecutable and non-terminating"*); the replacement has a different defect, not
none.

**Secondary, same clause.** §3.9's *"**Do not file it as a finding**"* binds the halves, but the
seam is prepended to each sub-task, so it becomes part of the `task` handed to every
`redteam-plan.md` reviewer beneath the cut — and those reviewers **do** file findings, which
`Severity` turns into the next task. A seam defect found below therefore still returns to a planner
that cannot fix it. §3.9 forecloses the channel it names without foreclosing the one it fears.

### F7 — `major` — `locator` fixes lines as the only unit, narrowing P6's corpus-agnosticism

**Where.** §3.3: *"`locator` | `{"path": <absolute path>, "lines": [<first>, <last>]}` — **inclusive,
1-based line numbers**, or `"lines": null` for the whole file. **Lines are the unit, fixed here.**"*

**The defect.** P6 exists so *"the method stays corpus-agnostic"* — corpus specifics are supposed to
live in the Layer-2 config. The seam instead fixes the addressing unit for all corpora at line
numbers, in the one place neither half may change (§3.9). A corpus of PDFs, of binary or
column-oriented data, of database rows, or of anything where the meaningful sub-unit is not a line
range cannot be expressed as an item, and no Layer-2 config can rescue it: `locator` is a seam field
with a fixed domain, and §3.3 says *"A may not require others, B may not omit any."* Note the seam
already does the corpus-agnostic thing one field over — `size_bytes` is fixed as **bytes**, *"the
seam's unit, whatever unit `sizing.*` uses internally"* — so the pattern for getting this right is
present in the same table.

**Why `major` rather than `minor`.** It is a defining property of the task, narrowed by a
constraint that is arbitrary (a `{"path", "unit", "range"}` shape with `unit` drawn from a small
fixed enum costs the seam one line and settles just as much cross-half ambiguity), and the half
that would discover the problem — B, the decomposer — is the half forbidden to change it.

### F8 — `minor` — A must append to `<run.dir>/decisions.md`, which the seam tells A it never has to resolve, and whose line format is fixed nowhere

**Where.** §3.7 rule 3 obliges every agent, A's included, to append to `decisions.md`; §3.2's read
table gives A's roles *"appends to `decisions.md`"*. But §3.3 states of `item_dir`: *"**absolute**
path to this node's directory — **A never has to resolve `run.dir`**"*, and the item record carries
no `run_dir` and no `decisions_path`. §3.2 and §3.6 do let A reference `run.dir` by name from the
config, so a path is technically obtainable — but the seam's own summary of A's needs asserts the
opposite, and A is planned blind and may take it at face value.

**Failure scenario.** A's planner, reading *"A never has to resolve `run.dir`"*, plans its log
append to `item_dir/decisions.md`, creating a per-item file that violates §3.2's *"the skeleton is
**EXHAUSTIVE**. Neither half may add a file or directory to it."* Separately: both halves append to
one human-readable log with **no agreed line format**, so the run log interleaves two conventions.
Nothing consumes `decisions.md` mechanically (the roll-up may not read it; the driver's decision
table never keys on it), which is why this is `minor` rather than `major` — but it is a shared
artifact written by both halves, and by the seam's own standard that makes it seam business.

**Cheap fix:** add `run_dir` (absolute) to the item record beside `item_dir`, and fix the
`decisions.md` line shape in §3.2 in one sentence.

### F9 — `minor` — the execution model is unstated: does the invoking session walk `SKILL.md`'s router, or is there a top-level driver agent?

**Where.** §3.2's read table treats *"B's run driver (stage 1)"* as a role with read permissions,
and §3.3 says it *dispatches* agents; §3.8 says `findings.md` is produced by a *"deterministic
file-concatenation step — a shell command or script in B's final stage file, NOT a dispatched
agent"* — executed by an unnamed actor. Both siblings are session-driven: `Guarded_change/SKILL.md:27`
and `Dragonfly/SKILL.md:31` have the **invoking session** create the run folder and walk the
numbered stages.

**Why it matters at the seam and not just inside B.** If the session walks the router, then the
"driver" is the session and §3.2's read-permission row for it is a rule the session must self-apply
— a materially weaker guarantee than a cold dispatched agent, and P5's blindness is the property the
whole cut is built on. It is `minor` because A is unaffected (§3.3 fixes A's invocation regardless)
and B can settle it internally, but the seam's blindness table quietly assumes an answer it does not
state.

### F10 — `minor` — resume never re-validates locators, though the corpus may have changed between runs

**Where.** §3.3: B *"validates every `locator` at decomposition time"*; §3.2: `item.json` is
**IMMUTABLE**; §3.5's resume table reads only file existence, `RUN`, and `state`.

**Failure scenario.** A run decomposes a 2 GB log directory, dies, and is restarted a day later
after the logs rotated. Every `item.json` is immutable and validated-once, so the driver
re-dispatches A on items whose line ranges now address different content. A's analysts cite
`file:line` positions that were true at decomposition time and are not true now, and the
verification pass (P3) — which drops *unverifiable* citations — will happily verify them against
the current file. The method's core guarantee, source-cited findings, degrades silently. `minor`
because a one-line seam addition (record a cheap corpus fingerprint per item and have the driver
re-check on resume) fixes it and neither half is blocked meanwhile.

### F11 — `minor` (missed opportunity) — the write-once/mutable dichotomy is a false one, and a third option dissolves F1 and F2 together

§3.5's divider note frames the choice as write-once versus *"allowing exactly one `STATUS`
replacement… rejected because it reintroduces mutation."* There is a third shape the seam never
considers: **`STATUS` as write-once per attempt** — `STATUS.<n>` written once by attempt `n`, with
"the node's status" defined as the highest-`n` file present. Nothing is ever overwritten, the
presence rule is untouched, nothing changes kind, and both F1 (a successful re-run can record
itself) and F2 (the driver can write a terminal `escalated` line at exhaustion without rewriting
anything) disappear. I raise it as a missed opportunity rather than prescribing it — the point is
that the seam rejected mutation and then paid for it in P7 without noticing there was a third
option.

### F12 — `nitpick` — "as the siblings do" overstates the letter-suffix precedent

§3.1: *"each half may add letter-suffixed files within its own phases (`stage-0a.md`, as the
siblings do)"*. `Dragonfly/stages/` does (`stage-0a.md`, `stage-0b.md`). `Guarded_change/stages/`
does not — it uses a decimal, `stage-1.5.md`. "As one sibling does" is the accurate claim. The
permission itself is fine and I am not contesting it.

---

## The six lenses — a verdict for each

### 1. Factual — **clean, earned**

I checked every `file:line` citation in §3 against the source. All resolve and all say what is
claimed:

| Cited | Verified |
|---|---|
| `Guarded_change/SKILL.md:28` — *"Step numbers below are the canonical stage numbers used everywhere"* | exact, line 28 |
| *"the same convention holds in `Dragonfly/SKILL.md`"* | true — `Dragonfly/SKILL.md:33` carries the same sentence |
| `Guarded_change/SKILL.md:27` — `changes/<slug>/` | exact |
| `Dragonfly/SKILL.md:31` — `hunts/<slug>/` | exact |
| `Dragonfly/METHODOLOGY.md:143` — `hunts/<slug>/` under "What a run produces" | exact |
| `Guarded_change/METHODOLOGY.md:139` — *"Paths are validated, not assumed"* | exact |
| `Dragonfly/SKILL.md:19` — *"Validate config paths at hunt start"* | exact |
| §3.7's *"neither sibling has a `common.md`"* | true — `ls` of both `stages/` dirs shows `charter.md` + `stage-*` only |
| `Dragonfly/stages/charter.md:1` — a charter read at *specific* stages | exact: *"The red-team charter (shared by stages 1, 4, 7)"* |
| `Architect/stages/common.md:3` — the universal-preamble pattern is Architect's own | exact |
| `Architect/stages/leaf.md:47` — *"You do not file findings…"* | exact, line 47 |
| `Architect/stages/combiner.md` — *"Stick the inputs together into one. DISCARD NOTHING."* / *"None of the three is an author…"* | exact, lines 39 and 6 |

§7's claim that round 2's misattributed quote is now correctly attributed to
`Guarded_change/SKILL.md:28` holds. The only inaccuracy I found is F12, a nitpick. **The divider's
sourcing is unusually careful and I want that recorded, since a clean factual lens otherwise reads
as an absence of effort.**

### 2. Logical — **F1, F2, F3, F4, F6**

All five are internal contradictions between seam clauses, not disagreements with a source: a rule
that forbids the write another rule requires (F1); a state whose stated producer is barred from
producing it (F2); a stated termination property the stated table does not implement (F3); an entity
the taxonomy creates and then defines nothing over (F4); a transport guarantee that names the wrong
combiner (F6).

### 3. Missed opportunity — **F7, F11**

The alternative cut (method vs. envelope) is considered and correctly rejected, and recording it was
right — §1's *"no later reviewer sees the alternatives available at this cut"* is exactly the
reasoning I would want. What is left on the table is inside the seam, not at the joint: a
corpus-agnostic locator shape (F7) and a non-mutating way to let status advance (F11).

### 4. Unstated assumptions & risks — **F8, F9, F10**

Also noted and **not** filed, because each checks out: that a dispatched agent may itself dispatch
(A's entry agent owns fan-out, §3.3) — both siblings spawn cold sub-agents from within a stage, so
the assumption is sound; that `node_id`'s charset excludes whitespace, which is what makes §3.4's
whitespace-separated five-field line parseable — §3.2 fixes `[A-Za-z0-9._-]+`, so it holds; that
concurrent leaf pipelines appending to one `decisions.md` do not interleave partial lines — §3.2's
atomic `O_APPEND` exemption covers it.

### 5. Fidelity — **clean; terms pinned below**

I pinned each loaded operational term to a concrete mechanism and checked the mechanism implements
the task's thing rather than a proxy:

| Term (task wording) | Pinned to | Verdict |
|---|---|---|
| **cold** | §3.7 rule 1 — no shared context with caller **or siblings** | real; matches the sibling charters' bar |
| **N independent analysts, each citing** | A's entry agent's dispatch point; independence enforcement at dispatch; §3.7 rule 4 fixes the duty, A fixes the format | real; the seam correctly declines to fix N and puts enforcement where the dispatch happens |
| **cold verification that drops unverifiable citations** | §2-A: a separate cold agent, **never the analyst that produced the finding**; surfaced as `n_dropped` | real, not a proxy — the "never the producer" clause is the load-bearing half and it is present |
| **agreement-ranked merge** | A's stage 4; rank surfaced as `max_agreement`, an integer count of analysts | real |
| **blind roll-up on a terse per-child status** | §3.2 read table row 5 (children's `STATUS` lines **and nothing else**) + §3.4's five-field line with **no path field** | **the strongest pinning in the document.** Removing `findings_path` is what turns P5 from an exhortation into a structure — a coordinator that holds no address for a finding cannot peek. §3.4's own note on this is correct. |
| **decompose and size** | B stage 0; `item.json` with validated `locator` and `size_bytes` | real, but see F7 on the locator unit and F4 on the un-splittable case |
| **facts, not interpretation** | §3.7 rule 7 states the duty; A owns *enforcement as a checkable rule rather than an exhortation* (§2-A, P8) | real — the sub-task text explicitly names the exhortation failure mode and forbids it |
| **restart and resume from on-disk state** | §3.2 presence rule + `RUN` + §3.5 table | **the one term whose mechanism does not implement it** — see F1 and F3 |

### 6. Completeness — **generative sweep run; F2, F4, F5 are its output**

Checklist pass first: the division has its joint (§1), its two sub-tasks (§2), a stated seam (§3), a
coverage argument (§4), a floor check (§5) and a self-containment audit (§6). All present.

Then the sweep — *"what load-bearing section does that list not anticipate?"* I asked it in five
directions:

1. **Every state in §3.4's domain — who writes it, and who acts on it?** → produced **F2**
   (`escalated`: no writer, and unreachable for groups in consequence).
2. **Every entity §3.2's taxonomy can produce — is it defined?** The taxonomy is
   leaf-iff-`item.json`, else group. → produced **F4** (the un-splittable item is neither, and rolls
   up vacuously `done` or vanishes).
3. **Every quantity two halves must agree on numerically, not just structurally** → produced **F5**
   (the seam fixes `size_bytes` as a *unit* everywhere and never fixes the *value* of the one bound
   that must match across the cut).
4. **Every terminal artifact — is it reachable?** `findings.md`'s assembly rule (§3.8) has three
   cases and is genuinely complete over leaves; but F3 means the final stage may never be reached
   at all, and F4 means non-leaf entries contribute nothing.
5. **Every escape hatch — does it actually carry?** → produced **F6**.

What the sweep found *present* and I want on record, because their absence would each have been a
`major`: `decisions.md`'s exemption from the presence rule; the in-flight-vs-never-started
distinction; the degenerate corpora (empty; single below-threshold item) assigned to B; the
`max_agreement`-over-the-empty-set definition; the group-state rules for both `n_findings` and
`max_agreement`; and the write-permission column on the read table. §7 claims these as round-2
fixes and, unlike the state-with-no-producer class, they hold up.

---

## Summary of severities

| # | Severity | One line |
|---|---|---|
| F1 | **blocker** | `STATUS` write-once makes every re-dispatch a no-op; P7's resume mechanism is inert and every `partial` leaf escalates regardless of outcome |
| F2 | major | `escalated` has no producer; the blind roll-up can never express terminal failure at any level |
| F3 | major | the no-`STATUS` driver row ignores the attempt cap, so §3.5's termination claim fails for a crashed pipeline |
| F4 | major | an un-splittable item leaves the tree: vacuous `done` or silent absence from `findings.md` |
| F5 | major | `sizing.max_item_bytes ≤ analysis.max_item_bytes` is a plan-time agreement with no fixed value and no build-time resolution |
| F6 | major | `SEAM-OBJECTION` rides `Union`, but `Consensus` (odd plan discarded) sits below it |
| F7 | major | `locator` fixes lines as the only unit, narrowing P6's corpus-agnosticism in a place no config can reach |
| F8 | minor | A must append to `<run.dir>/decisions.md` while §3.3 asserts A never resolves `run.dir`; no line format fixed |
| F9 | minor | execution model (session-walks-router vs. driver agent) unstated, though blindness rests on it |
| F10 | minor | resume never re-validates locators against a corpus that may have changed |
| F11 | minor | missed: `STATUS.<n>` write-once-per-attempt dissolves F1 and F2 without reintroducing mutation |
| F12 | nitpick | "as the siblings do" — only Dragonfly uses letter suffixes |

**I do not object to going forward with this cut.** All twelve findings are seam-text defects that
travel down with the sub-tasks; the joint is the one the task itself names and I would keep it.
