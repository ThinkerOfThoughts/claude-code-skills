# Split review — round 4, reviewer C (cold, independent)

**Under review:** `Architect/runs/data-distiller/it3/0/split-round-4.md` — a proposed *division*, not a
plan. I hold no plan and was given none.

**Fence compliance:** I did **not** open, read, list, grep, glob or otherwise access
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke the
installed `data-distiller` skill. I did not read any `split-review-*.md` file, and I did not read
`split-round-1/2/3.md` — this review is of round 4 on its own merits.

**What I did read:** the round-4 proposal in full; `Architect/stages/{common,redteam,redteam-split,
divider,node,combiner,leaf}.md`; and, for the factual lens, `Guarded_change/{SKILL,METHODOLOGY}.md`,
`Dragonfly/{SKILL,METHODOLOGY}.md`, `Dragonfly/stages/charter.md`, and directory listings of both
siblings and their `stages/`.

---

## VERDICT — two parts, both needed

**Part 1 — what I found.** 3 `major`, 9 `minor`, 2 `nitpick`, 0 `blocker`. Every one is a defect in
the **seam text**, not in the choice of joint. The most serious is a termination hole in §3.5's driver
table that is the *same class* of defect §7 claims to have fixed for group nodes, left unfixed for
leaves.

**Part 2 — do I object to going forward with this cut? NO. I endorse it.**
The joint is real, it is the boundary the owner's own task statement drew (P5), each half is a
coherent whole task far above the floor, and the seam is self-contained in the sense
`redteam-split.md` §2 demands — I found **no** clause of the form *"A produces X at plan time and B
consumes it."* Every cross-half dependency is fixed in the seam, partitioned by namespace, or
correctly reframed as a build-time rule over the merged plan. **Carry my findings forward against the
sub-tasks they bear on and proceed.**

---

## The four questions

### Q1 — Coverage: do the two halves cover the whole task?

**Yes.** I walked P1–P8 independently of §4's table and found no orphan and no portion both halves
assume the other owns:

| Property | Owner per seam | My check |
|---|---|---|
| P1 decompose + size + over-size | B (§3.5, decomposition-time only) | owned; degenerate corpora explicitly assigned (§2-B) |
| P2 N cold analysts | A, incl. all fan-out (§3.3) | owned; B dispatches one agent and never sees an analyst |
| P3 cold verification | A | owned; `n_dropped` is the only upward trace |
| P4 agreement-ranked merge | A | owned; `max_agreement` is the only upward trace |
| P5 blind roll-up | B | owned; A emits the leaf line, schema fixed §3.4 |
| P6 Layer-2 config | B owns file + contract; namespaces partitioned §3.6 | owned; contract is a build-time rule, not a channel |
| P7 restart/resume | B across nodes, A within an item | owned on both sides; write rules shared §3.2 |
| P8 facts-not-interpretation | A enforcement, B statement | owned; both hold the task statement |
| "check against the siblings" | both, each for its own files (§4) | owned; both sub-tasks name concrete precedent files, and all of them exist |

Non-property remainders are also assigned: run driver (B), run log (B), escalation (B), assembled
`findings.md` (B), entry surface (B), `stages/common.md` (B). I looked specifically for the classic
orphans — *who creates the run directory*, *who declares the run finished*, *who triggers `findings.md`* —
and all three fall inside B, so they are intra-half, not seam gaps. **Q1 clean.**

### Q2 — The seam: stated? sound? self-contained?

**Stated:** yes, at unusual length (§3.1–§3.11) and identically to both halves.

**Self-contained:** yes, and I checked this the way `redteam-split.md` insists. I enumerated every
artifact one half needs from the other and classified it:

- *Fixed in the seam text:* item record and its value domains (§3.3), invocation target/arity/argument
  (§3.3), `STATUS` schema and state semantics (§3.4), write rules and read permissions (§3.2), the
  control loop and escalation (§3.5), `common.md`'s seven rules (§3.7), stage numbering (§3.1).
- *Partitioned so neither needs the other:* config key namespaces (§3.6).
- *Correctly reframed as build-time rules over the merged plan* (divider.md's third legitimate home):
  the router table, `Stop-for-human`, stage index, loop diagram, what-a-run-produces, config contract,
  worked example, `index.md`'s findings pointer, `findings.md` assembly, and the size invariant. These
  are executable by a practitioner holding the merged plan, and the merged plan is itself red-teamed at
  the parent node (`node.md` step 3), so a rule that fails to resolve is catchable before build.

I searched specifically for the failure mode named in my aiming file — *"a file index, a config key
set, a status vocabulary, any artifact one half is told to derive from the other's plan"* — and each
of those three is fixed in the seam text, not derived. §6's claim on this point is accurate.

**Sound:** mostly, with the exceptions below — findings **C-1** (termination), **C-6**, **C-7**.

### Q3 — The floor: would either half fall below it?

**No.** Floor = *one file created or one coherent edit to one file, with the content specified.*
A plans ≥3 role-prompt files (stages 2–4) plus finding/citation/diagnostic formats; B plans ≥9 files
(`SKILL.md`, `METHODOLOGY.md`, `README.md`, the worked config, `stages/common.md`, stages 0/1/5, the
concatenation step). Both are multi-file whole tasks, an order of magnitude above the floor. The floor
passes down unchanged (§3.11). **Q3 clean — no blocker against the division.**

### Q4 — Real joint or arbitrary cut?

**Real joint.** §1's table names what differs on each side and I independently confirm each row is a
genuine difference, not a restatement: *inputs* differ (corpus content read for meaning vs. corpus
shape and one-line statuses), *outputs* differ (evidence vs. bookkeeping), *characteristic failures*
differ (a fabricated citation vs. a coordinator that peeks / work lost on restart), and *review
criteria* differ (does every citation resolve vs. is it blind and idempotent). The decisive point is
correct and worth restating: **P5 is not a feature on one side of the line — P5 is the assertion that
the line exists and is not crossed.** A cut that ran anywhere else would put P5's boundary *inside* a
half, where nothing downstream could check it.

The rejected alternative (method vs. envelope) is recorded with its reason, which is what §1 owes a
reviewer who cannot see the alternatives. I add one more unconsidered alternative below (C-14), and
explain why I do **not** think it unseats this joint.

---

## Findings

### C-1 — `major` — §3.5's driver table has no attempt cap for a leaf that never writes a `STATUS`; the stated termination argument is false for that case

*(lenses: logical, completeness)*

§3.5's table, first row: `leaf | no STATUS | increment RUN; dispatch A's entry agent (§3.3)`. There is
**no guard on `RUN`** in that row, and **no row** for `leaf | no STATUS | RUN ≥ run.max_attempts`.
Compare the group rows, which do have exactly that guard: `group | every child terminal, RUN ≥
run.max_attempts, still no STATUS | write STATUS = escalated`.

**Failure scenario, concrete:** A's entry agent is dispatched on leaf `0.3`, and crashes (or is killed,
or returns without writing anything) before writing `STATUS` — the exact case §3.2 rule 4 says `RUN`
exists to distinguish (*"started by a run that died"*). The driver re-observes `0.3`: still no
`STATUS`, so row 1 fires again — increment `RUN`, dispatch again. `RUN` climbs past
`run.max_attempts` and nothing reads it. The node never becomes terminal, its parent group never
rolls up, and the run does not stop for the human. `escalated`'s two situations (§3.4) — *"the
decomposer could not size an item down, or the driver reached the attempt cap"* — cannot be reached
here, because the row that would recognise the cap does not exist.

§3.5's own termination argument is therefore unsound as written: *"`RUN` strictly increases before
each dispatch and is bounded, and the cap converts any non-terminal node into `escalated`"* — the cap
converts a `partial`/`failed` leaf and a stuck group, but not a silent leaf.

This is the **same defect class** §7 records as a round-3 `major` (*"group nodes have no attempt
counter or cap; the termination claim was false for them"*), fixed for groups and left open for
leaves. P7 (restart and resume) is one of the eight defining properties, so this is a load-bearing
contingency, not a corner.

**Remedy (fits in the seam, one row):** add `leaf | no STATUS, RUN ≥ run.max_attempts | write STATUS =
escalated 0 0 0, append to decisions.md, stop for the human`, and rewrite the termination argument to
quantify over *"a node with no STATUS"* rather than over states.

**Related, same nub, no separate finding:** §3.3 fixes that the driver *"waits for the agent to
return"* with no time bound. An A entry agent that **hangs** rather than dying is outside the attempt
cap entirely — `RUN` is incremented *before* dispatch, so the driver never gets another pass. The
remedy row above does not cover it. Either the seam bounds the wait, or it states plainly that a hung
agent is a human-recovered condition.

### C-2 — `major` — §3.3 hard-codes lines as the only locator unit, which is in direct tension with P6 (corpus-agnosticism), and neither half may change it

*(lenses: fidelity, unstated assumptions)*

§3.3: `locator` is `{"path": <absolute path>, "lines": [<first>, <last>]}` — *"inclusive, 1-based line
numbers, or `"lines": null` for the whole file. **Lines are the unit, fixed here.**"*

P6 is *"a per-corpus Layer-2 config so the method stays corpus-agnostic."* The mechanism the seam
gives for corpus-specificity is the Layer-2 config, but the **addressing unit** is lifted out of the
config and frozen in the seam. Any corpus whose items are not line-addressable — a directory of PDFs,
a set of binary logs, audio transcripts stored as JSON objects, database rows, a corpus of images with
sidecar text — has exactly two expressions available: whole-file (`"lines": null`), which defeats
sizing for any file that is itself over-size, or nothing. §3.5's over-size strategy then has no
sub-file boundary to split on, so every such item routes to `escalated` and the method degrades to
"cannot handle this corpus."

This is a **fidelity** finding, not a taste one: the seam implements a proxy (line-range addressing)
for the mechanism the task specified (a method that stays corpus-agnostic via config). And it is
unfixable below the cut — §3.9 forbids either half from adjusting it, and a lone planner's
`SEAM-OBJECTION` can be discarded by `Consensus` (§3.9's own admission).

**Remedy:** make `locator` a discriminated range — e.g. `{"path", "unit": "lines"|"bytes"|"records",
"range": [first, last] | null}` with `unit` fixed per run by a B-owned config key, `lines` the default.
That is still fully specified at plan time, still gives A one format to parse, and restores the
property. If the divider prefers to keep it simple, the alternative remedy is to **state the
restriction as an accepted limitation** the seam imposes on P6, so it is a known scope cut rather than
an unnoticed contradiction.

### C-3 — `major` — the seam-transport gap is not purely an apparatus gap; `divider.md` puts it on the divider, and the divider has a mechanism it did not use

*(lenses: factual, completeness)*

§6 ("Seam transport") and the preamble both state that the seam has *"no guaranteed transport"* and
that *"neither `divider.md` nor `node.md` provides a mechanism for this."* The `node.md` half of that
is factually correct — `node.md:86-88` spawns children with `(division.first, plan, granularity,
depth + 1, node_id + ".1")` and passes nothing else, so a seam living *outside* `division.first`
does not travel.

But `divider.md` **does** address it, in its "Deriving a split" section: *"Each sub-task must carry the
source material it points at, the way your own task did."* Carrying is the divider's job, and the
divider holds the one lever that makes it unconditional: **make `division.first` literally be §3's text
followed by §2-A's text, and `division.second` be §3's text followed by §2-B's text, in the returned
value.** Then `node.md` transports the seam whether or not it knows it is doing so, no apparatus change
is needed, and no node has to comply with an instruction.

As round 4 stands, §2's parenthetical (*"Both sub-task texts below are delivered with §3 prepended
verbatim — see §6"*) is a claim about something outside the document, and §6 downgrades it to *"the
division's return value states it as an instruction to the node."* An instruction a node may not
follow is exactly the class of thing this seam is otherwise scrupulous about refusing. **The mitigation
that already exists** — each sub-task also carries the absolute path to `split-round-4.md`, and
`common.md` §2 tells every agent that opening what its task points at is part of its job — is real and
is why this is `major` and not `blocker`. But it makes the seam's reachability depend on a planner
choosing to open a file, and §7 lists this as disposed.

**Remedy:** inline §3 into both returned sub-task strings, and change §6 to say the transport is
guaranteed by construction. Keep the apparatus report — the *re-division* case (§3, first paragraph)
genuinely does rely on an instruction, since B's own divider must choose to propagate.

### C-4 — `minor` — the seam reaches deep into B-internal design, which only B can act on, and §3.9 gives no reliable way for B to repair it

*(lenses: logical, unstated assumptions)*

§3.5's entire driver table, `RUN`'s increment discipline, `run.max_attempts`, both escalation triggers
and the group-state rule are things **only B can act on** — A never reads `RUN`, never writes
`escalated`, and never sees a group. The only genuinely cross-half facts in §3.5 are two: *re-dispatch
of the same leaf is safe*, and *the size invariant*. Everything else is B's design, frozen in a
document B may not renegotiate.

The cost is not hypothetical — **C-1 demonstrates it.** A B planner who notices the missing cap row
cannot fix it: §3.9 forbids adjusting or working around the seam and forbids filing it as a finding,
leaving only a `SEAM-OBJECTION` that §3.9 itself admits `Consensus` may discard. A defect in B's own
control loop is thus harder to fix than one in B's own files, for no seam-related reason.

I am filing this `minor` rather than `major` because the over-specification does not break the
division and is defensible as a deliberate belt-and-braces choice after three rounds of control-loop
churn. But it is worth stating for whoever inherits this: **the diagnostic for what belongs in a seam
is "which halves can act on it", and §3.5 mostly fails it.**

### C-5 — `minor` — `tier` is a mandated field no role in the method may act on

*(lens: unstated assumptions / completeness)*

§3.3 requires `tier` in every `item.json` and says *"**opaque to A.** A must not branch on it. It
exists for B's sizing and for the human."* But B's sizing happens **at decomposition time, before
`item.json` is written** (§3.5), so B does not read it back either; and the roll-up coordinator is
forbidden to read `item.json` at all (§3.2 read table). The result is a required field with **no
consumer anywhere in the method** — only "the human", who per §3.2 may read everything anyway.

Concretely this forecloses the obvious use: a tiered analysis policy (a bigger or denser item gets more
analysts, or a different reading discipline). §3.6 gives A the `analysis.*` namespace but §3.3 denies A
the one per-item signal it would key such a policy off.

**Remedy:** either drop `tier`, or name its consumer and lift the "A must not branch on it"
prohibition, deciding deliberately whether tier-sensitive analysis is in or out of scope.

### C-6 — `minor` — §3.5 contradicts itself about how much of `STATUS` the driver reads

*(lens: logical)*

§3.5: *"Resume and the driver's per-pass decision read file existence, `RUN`'s integer, and — for
`STATUS` only — the `state` field. (`state` is already a field above-boundary roles may read, so this
costs no blindness.)"* Four lines later, the same section's cap action reads: *"**replace `STATUS`
with `escalated`** (integers preserved from the observed line)."* Preserving the integers requires
reading them.

No blindness is actually breached — the three integers are aggregate counts, not findings, and §3.2's
read table already grants the driver *"any `STATUS`"*. But the seam is the document both halves
inherit as authoritative, and a self-contradicting clause in it is a clause each half will resolve
differently. **Remedy:** delete the parenthetical narrowing, or restate it as *"the driver reads the
whole line but branches only on `state`."*

### C-7 — `minor` — a `partial` leaf's counts can overstate what `findings.md` actually contains

*(lens: logical)*

§3.4 defines `n_findings` as *"findings surviving verification **and merge**"* and defines `partial`
as *"some phases completed, the rest could not; the three integers describe what exists."* §3.8's
assembly rule says *"a leaf with a `STATUS` but no merged-findings file contributes a header-only
section recording its state."*

**Failure scenario:** A's pipeline runs analysts and verification on leaf `0.2`, then fails during
merge. If A reads "the integers describe what exists" as licensing `n_findings = 7`, the roll-up sums
7 into the corpus total the human reads, while `findings.md` carries a header-only section for `0.2`
and contains none of them. The corpus headline count then exceeds the corpus artifact, with nothing
flagging the discrepancy. If instead A reads the `and merge` clause strictly, `n_findings` must be `0`
whenever no merged file exists — but then the "integers describe what exists" sentence is misleading,
and a `partial` leaf is indistinguishable from `failed` in its numbers.

Both readings are available to a blind A planner and only one is right. **Remedy:** state it in one
line — e.g. *"`n_findings` and `max_agreement` are non-zero only when a merged-findings file exists;
otherwise `partial` reports `0 0 0` with `n_dropped` optionally non-zero."*

### C-8 — `minor` — bytes is fixed as the sizing unit for a property that is actually about context-window fit

*(lens: unstated assumptions)*

§3.3 fixes `size_bytes` as *"the seam's unit"*; §3.5's invariant `sizing.max_item_bytes ≤
analysis.max_item_bytes` and A's own acceptance bound are both byte-denominated. But the property being
protected is the task's *"too large for one context window"*, which is measured in tokens, and the
bytes-per-token ratio varies by roughly 3× between dense structured data and prose. A bound tuned on a
prose corpus will admit an item that overflows on a JSON one, and vice versa.

§3.3 does allow B to size in whatever unit it likes internally and report bytes, so B can compensate.
**A cannot** — A's only acceptance bound is in bytes, so A's last-line-of-defence check
(§2-A, *"handed a larger item, your entry agent writes `state=failed`"*) is the imprecise one.

**Remedy:** state the rationale (bytes are deterministic and need no tokenizer) as an explicit accepted
approximation, and either permit A a second token-denominated bound in its own `analysis.*` namespace,
or note that the worked example config must document a corpus-appropriate bytes/token assumption.

### C-9 — `minor` — both sub-tasks point their (blind) planners at a file that contains the other half's sub-task and the divider's own deliberations

*(lens: unstated assumptions / risks)*

§2-A and §2-B each say the seam is *"also readable at .../split-round-4.md"*. That file is this whole
document: it contains §2-A **and** §2-B in full, §1's rejected alternative, §5's remark that B *"is
arguably two design concerns"* and *"remains divisible one level down"*, and §7's round-3 disposition
table. Meanwhile §3's opening sentence tells each planner *"Both halves are planned concurrently and
blind to each other."*

The blindness is not actually breached in the load-bearing sense — the other half's *plan* (filenames,
config keys, stop conditions, merged-findings filename) does not exist yet and is not in this file, so
the "invent it and look locally correct" failure is still prevented. The risks are softer and real: a
planner that has read the other half's brief may plan up to, or across, the boundary; and a planner
reading §5 and §7 may treat the divider's meta-commentary — including its self-reported apparatus
gaps — as instruction.

**Remedy:** point each half at a **seam-only** extract (§3 alone, at its own path), not at the full
proposal. This costs one file and removes the ambiguity entirely. Note this becomes moot for the seam
text itself if C-3's remedy is adopted, but the *pointer* should still not resolve to the full
document.

### C-10 — `minor` — B must write `METHODOLOGY.md`'s narrative sections about A's phases, and the seam neither licenses nor bounds that

*(lens: completeness — from the generative sweep)*

§2-B's "steps written as rules over the merged plan" list is careful and covers the *inventory*-shaped
sections: router table, `Stop-for-human`, stage index, loop diagram, what-a-run-produces, config
contract, worked example, `index.md` pointer, `findings.md`. It does **not** cover
`METHODOLOGY.md`'s prose sections — the sibling precedent B is told to follow
(`Dragonfly/METHODOLOGY.md`) leads with why-it-exists, the two layers, and human-in-the-loop, and any
useful version of those must describe what the analysts, the verifier and the merge *are*. Yet §2-B's
"you do not own" list forbids B from planning *"what an analyst does with an item's content, the
citation format, the verification pass, the merge."*

A blind B planner facing that either guesses A's mechanisms (the failure the seam exists to prevent),
or writes those sections so thinly that `METHODOLOGY.md` fails the house-style check the task asks for.
§4's P8 row implies the resolution — *"both take it from the task statement, which both hold"* — but
that licence is stated for P8 only and never generalised.

**Remedy:** one clause in §3.1 or §2-B: *"B describes A's phases at the level of the task statement's
eight properties and no deeper; any statement about A's mechanism is written as a rule over the merged
plan."*

### C-11 — `minor` (missed opportunity) — one further alternative cut is unconsidered, and recording it costs nothing

*(lens: missed opportunity)*

§1 records one rejected alternative (method vs. envelope). A second was available and is not mentioned:
**give the run driver to A** — A takes stages 1–4 (driver + pipeline), B takes decomposition, roll-up
and the entry surface. Its attraction is that the tightest coupling in the whole seam is
driver↔entry-agent, and moving it inside one half would delete §3.5's entire driver table, `RUN`, the
attempt cap and both escalation triggers from the seam — which is exactly the over-specification C-4
identifies, and would have made C-1 an intra-half bug that B's own planners could fix.

**I do not think it unseats this cut,** and I want that on the record for whoever reads only my
findings: the driver reads statuses and never a finding, so it sits unambiguously *above* the boundary
§1 defines. Moving it below would put P5's line inside a half and make the joint incoherent — which is
a stronger objection than the seam-size saving is a benefit. But the option should be *recorded and
refused* rather than unmentioned, for the same reason §1 gives for recording the first alternative:
*"no later reviewer sees the alternatives available at this cut."*

### C-12 — `nitpick` — "The three write rules" introduces four

§3.2 reads *"**The three write rules:**"* and then lists items 1–4; §6's audit table repeats *"§3.2
three write rules"*. The fourth (`RUN`) is load-bearing for §3.5's resume logic, so the miscount is
cosmetic but sits in the one document both halves treat as authoritative.

### C-13 — `nitpick` — "may not add a top-level file" is stricter than the siblings the task points at

§3.1: *"may not move a phase to a different number, and may not add a top-level file."* The layout does
provide for the companion config, which is the sibling pattern
(`Dragonfly/dragonfly.companion.md`, `Guarded_change/guarded-change.companion.md`). But
`Guarded_change/` also carries a top-level `FRAMEWORK-FEEDBACK.md`, so "no top-level additions" is a
tighter rule than house style actually observes. Harmless unless a half has a genuine reason for one
(a feedback file, a `CHANGELOG`); if so, §3.9's no-workaround rule makes it a `SEAM-OBJECTION` over
something trivial. Consider *"may not add a top-level file **that any stage file references**."*

---

## The six lenses — verdict for each

### 1. Factual — **findings: C-3, C-13** (and every other citation checked resolved)

I verified the seam's source citations rather than accepting them. All of the following resolve and
say what is claimed:

- `Guarded_change/SKILL.md:27` — *"Create a change folder `changes/<slug>/`"* ✔ (supports §3.2's
  run-artifacts-inside-the-skill-directory convention)
- `Guarded_change/SKILL.md:28` — *"**Step numbers below are the canonical stage numbers used
  everywhere**"* ✔ (supports §3.1's argument that stage numbering is joint)
- `Guarded_change/METHODOLOGY.md:139` — *"**Paths are validated, not assumed.**"* ✔ (supports §3.3's
  locator validation)
- `Dragonfly/SKILL.md:19` — *"**Validate config paths at hunt start**"* ✔ (same)
- `Dragonfly/SKILL.md:31` — *"Create a hunt folder `hunts/<slug>/`"* ✔
- `Dragonfly/METHODOLOGY.md:143` — *"One folder per hunt, e.g. `hunts/<slug>/`"* ✔
- `Dragonfly/stages/charter.md:1` — *"# The red-team charter (shared by stages 1, 4, 7)"* ✔ — and §3.7's
  characterisation of it as *"read at specific stages, not a universal preamble"* is exactly right
- `Architect/stages/common.md:3` — *"Every agent Architect dispatches reads this file first"* ✔
- `Architect/stages/leaf.md:47` — *"You do not file findings — your output is a plan, and severities
  are for reviewers."* ✔ (§3.9's premise holds)
- `Architect/stages/combiner.md:22` — *"2-of-3 on numbered steps, INCLUDING ORDER. The odd plan is
  discarded."* ✔ and `:6` *"None of the three is an author."* ✔ — so §3.9's honest limit and §6's
  observation that `divider.md`'s "defer to `Union`" offer contradicts `combiner.md` are **both
  correct catches**, and I confirm the contradiction independently (`divider.md`, home #2, vs.
  `combiner.md:6`).
- §3.7's claim *"neither sibling has a `common.md`"* ✔ — verified by listing both `stages/`
  directories; both have `charter.md`, neither has `common.md`.
- §3.1's claim that letter-suffixed stage files are the sibling convention ✔ —
  `Dragonfly/stages/stage-0a.md`, `stage-0b.md`; `Guarded_change/stages/stage-1.5.md`.
- Every precedent file named in §2-A and §2-B exists: `Guarded_change/stages/{charter,stage-3}.md`,
  `Dragonfly/stages/{charter,stage-7}.md`, both `SKILL.md`s, `Dragonfly/METHODOLOGY.md`, both
  companion configs, both `README.md`s. ✔

The one factual defect is **C-3**: §6 says *"neither `divider.md` nor `node.md` provides a mechanism"*
for seam transport. The `node.md` half is correct (`node.md:86-88` passes only
`division.first`/`.second`); the `divider.md` half is **not** — `divider.md` states *"Each sub-task
must carry the source material it points at, the way your own task did."* **C-13** is a lesser factual
mismatch against house style.

**Verdict: not clean — C-3 (`major`), C-13 (`nitpick`). Everything else checked resolves.**

### 2. Logical — **findings: C-1, C-6, C-7** (also C-4)

C-1 is a real gap in the state machine's case analysis, and it falsifies §3.5's own termination
argument. C-6 is an internal contradiction within one section. C-7 is a genuine ambiguity that two
blind planners can resolve incompatibly.

Things I checked and found sound: `escalated` has exactly one producer (B) and two triggers, both
named; no node changes kind, which is what makes `STATUS` replacement safe (§3.2 rule 2's reasoning is
correct — replacement is safe *because* nothing else about a node mutates); group states are genuinely
exhaustive given the "roll up only when all children are terminal" rule, and that rule is what makes
the group state computable from children's lines alone; the leaf ordering (children before parents) is
stated and the tree is finite. The round-3 write-once/re-run contradiction §7 claims to fix **is**
fixed — §3.2 rule 2 and §3.4's *"replacement is the mechanism by which a re-run leaf records its
success"* close it, and I could construct no remaining path where a successful re-run has nowhere to
record itself. **Verdict: not clean — see above.**

### 3. Missed opportunity — **finding: C-11**

The driver-with-A alternative should be recorded and refused. I also considered and found **no**
better cut than the one proposed: a "role prompts vs. state machine" cut is the rejected packaging
alternative in different clothes, and any cut that leaves P5's boundary inside one half is strictly
worse. **Verdict: one minor finding; the chosen joint remains the best on the table.**

### 4. Unstated assumptions & risks — **findings: C-2, C-5, C-8, C-9** (also C-4)

Beyond those four: the seam assumes the Layer-2 config is stable for the life of a run —
`config_path` is captured per item and `item.json` is immutable, so a config edited between a crash
and a resume silently changes `analysis.max_item_bytes` and can flip previously-analysable items to
`failed`. §3.2's immutability rules make the *decomposition* side of this safe, so I am not filing it
separately, but it is the kind of thing B's P7 planning should state. I also checked the assumption
that structural boundaries always exist to split on — §3.5 handles its failure explicitly via the
decomposer-written `escalated` leaf, which is a genuinely good fix and is the right shape (nothing
vanishes; it is counted and reported). **Verdict: not clean — see above.**

### 5. Fidelity — **finding: C-2**; every other loaded term pinned to a concrete mechanism

Per my charter I pinned each loaded operational term to the mechanism the division gives it:

| Term | Pinned to | Mechanism or proxy? |
|---|---|---|
| **cold** | §3.7 rule 1 (no shared context with caller or siblings) + A owns enforcement *"at your entry agent's dispatch point"* (§2-A) | mechanism — enforcement is located at a named dispatch point, not asserted |
| **read-only** | §3.7 rule 3 + A owns *"what read-only concretely forbids an analyst"* (§2-A) | mechanism |
| **decompose** | B stage 0: split along config-named structural boundaries, recursively, to `sizing.max_item_bytes` / `sizing.max_resplits`, emitting validated `item.json` records (§3.3, §3.5) | mechanism |
| **verify** | a separate cold agent, **never the analyst that produced the finding**, with A defining "unverifiable" operationally (§2-A) | mechanism — the "never the producer" constraint is the load-bearing half and it is in the seam-adjacent sub-task, not left to taste |
| **agreement-ranked merge** | A: matching rule, agreement definition, rank computed and recorded; `max_agreement` surfaced upward (§2-A, §3.4) | mechanism |
| **blind** | **structural**: §3.4's five fields contain no path; §3.2's read table forbids the coordinator everything but children's `STATUS` lines; §3.4 records that round 1's `findings_path` was removed precisely because *"putting the locator of the findings into the blind coordinator's only input turns P5 from a structure into an exhortation"* | mechanism — this is the strongest fidelity point in the document |
| **restart / resume** | presence rule + `RUN` + `state`, with a driver decision table and no coordination protocol (§3.2, §3.5) | mechanism, defective in one case (C-1) |
| **facts, not interpretation** | §3.7 rule 7 states the duty; A owns writing it *"as an enforceable rule rather than an exhortation"* (§2-A) | **duty stated, mechanism correctly deferred to A** — this is the one term whose mechanism does not exist yet, and deferring it is right: it is wholly inside A's half, and the sub-task text names the standard it must meet |
| **corpus-agnostic** | §3.6 Layer-2 config + §3.3 locator | **proxy — see C-2.** The config carries corpus specifics but the *addressing unit* is frozen at "lines", so agnosticism holds only for line-addressable corpora |

**Verdict: not clean — C-2 (`major`). Eight of nine terms pin to real mechanisms.**

### 6. Completeness — **findings: C-1, C-3, C-10**; generative sweep run

I ticked the structure's own required sections first (the joint, the two sub-tasks, the seam, coverage,
floor check, self-containment audit — all present, plus a round-3 disposition), then ran the sweep:
*"what load-bearing section does that list not anticipate?"* What I looked for, and what each turned
up:

- **A build-order section for the merged plan** — looked for it; **no hazard.** The deliverables are
  markdown files with no compile order, and the only run-time ordering constraint (`findings.md` is
  assembled last) is stated in §3.8. No finding.
- **A duplicate/conflicting-step section** — looked for it; **no hazard.** §3.1's phase binding and
  §3.2's exhaustive skeleton give every file exactly one writer, so `Union` cannot receive two plans
  for the same file. No finding.
- **How the roll-up discovers who its children are**, given it may not read `index.md` — B-internal
  (driver and roll-up are both B's), so not a seam gap. No finding.
- **What the merged plan owes `METHODOLOGY.md`'s prose** — **gap → C-10.**
- **Whether the seam's transport is a mechanism or an instruction** — **gap → C-3.**
- **Whether every state in §3.4 has a producer *and* every observable has a driver row** — the
  producer side is complete; the observable side is not → **C-1.**
- **An acceptance/definition-of-done for the built skill** — §3.10 excludes any harness or eval as a
  *challengeable divider ruling*. I considered objecting and **do not**: the task says "plan the
  implementation", neither sibling ships a self-test, and B's worked example config plus
  `METHODOLOGY.md`'s "what a run produces" give a practitioner enough to tell a correct run from a
  broken one. **I explicitly endorse §3.10's ruling** so the next reader knows it was examined rather
  than skipped.
- **§3.9's escape path** — present, and unusually, *honest about its own limit*. I checked its premises
  against `combiner.md` and `leaf.md` and both hold. It is not a channel, and the document does not
  pretend otherwise. No finding beyond C-4's observation that its unreliability now matters more
  because §3.5 froze so much B-only design.

**Verdict: not clean — C-1, C-3, C-10. Sweep run; the items above are what it looked for.**

---

## Was any portion of the task left unaddressed?

**No.** All eight properties, the build root, and the house-style check against both siblings are
assigned (Q1 above). The sibling check in particular is done properly: both sub-tasks name specific
precedent files rather than gesturing at the directories, all of those files exist, and §3.7 flags the
one deliberate *divergence* from house style (`common.md`, which neither sibling has) and requires B to
say so in `METHODOLOGY.md`. That is the right handling of a divergence in a task that asked for a style
check.

---

## Standing findings, for carry-forward

| # | Severity | Bears on | One line |
|---|---|---|---|
| C-1 | major | seam §3.5 → **B** | no attempt cap for a leaf that never writes `STATUS`; termination argument false for that case |
| C-2 | major | seam §3.3 → **both** | lines fixed as the only locator unit, contradicting P6's corpus-agnosticism |
| C-3 | major | seam transport → **divider** | §6 misreads `divider.md`; inline §3 into the returned sub-task strings |
| C-4 | minor | seam §3.5 → **B** | seam over-scopes into B-only design with no reliable repair path |
| C-5 | minor | seam §3.3 → **both** | `tier` has no consumer |
| C-6 | minor | seam §3.5 → **B** | contradicts itself on how much of `STATUS` the driver reads |
| C-7 | minor | seam §3.4/§3.8 → **A** | `partial` counts can overstate `findings.md` |
| C-8 | minor | seam §3.3/§3.5 → **both** | bytes proxies tokens with no stated rationale; A cannot compensate |
| C-9 | minor | §2-A/§2-B pointers → **divider** | planners pointed at a file containing the other half's brief |
| C-10 | minor | §2-B → **B** | `METHODOLOGY.md` prose about A's phases is neither licensed nor bounded |
| C-11 | minor | §1 → **divider** | driver-with-A alternative unrecorded (and, I agree, correctly refused) |
| C-12 | nitpick | §3.2/§6 | "three write rules", four listed |
| C-13 | nitpick | §3.1 | "no top-level additions" stricter than the siblings |

**Objection to going forward: NONE. The joint is right and I would keep it.** These findings travel
down with the sub-tasks; C-1, C-2 and C-3 want fixing in the seam text before or as the division is
returned, since all three are unfixable from below.
