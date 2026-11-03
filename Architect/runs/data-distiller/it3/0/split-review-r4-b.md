# Cold split review — round 4, reviewer B

Reviewing `Architect/runs/data-distiller/it3/0/split-round-4.md` as a proposed **division**. I hold
no plan and was given none.

**Fence compliance.** I did **not** read, list, grep, glob or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke
the installed `data-distiller` skill. I did not read any `split-review-*.md`, and I did not read
`split-round-1/2/3.md` — this review is of round 4 on its own merits. §7's dispositions are treated
as claims and nothing was passed for being unmentioned there.

**What I did open:** `Architect/stages/{common,redteam,redteam-split,divider,node,leaf,combiner}.md`;
`Guarded_change/{SKILL.md,METHODOLOGY.md,stages/}`; `Dragonfly/{SKILL.md,METHODOLOGY.md,stages/}`.

---

## VERDICT — the two parts

**Part 1 — what I found.** 1 `blocker`, 5 `major`, 4 `minor`, 2 `nitpick`. All are defects in the
**seam text**, not in the choice of joint. The blocker is a termination hole that is the exact leaf
analogue of the group-node hole §7 says round 3 fixed — fixed for groups, still open for leaves.

**Part 2 — do I object to going forward with this cut? NO. I endorse this cut.**
The joint is real, the coverage is complete, both halves sit far above the floor, and the seam is
the most genuinely self-contained one I could construct arguments against — it fixes vocabularies
rather than deferring them, and the removal of any findings pointer from `STATUS` makes P5 a
structure rather than an exhortation. My findings travel down with the sub-tasks. **Filing a
blocker is not an objection to proceeding**, and I state plainly that I would keep this joint.

---

## The four questions

### Q1 — Coverage: do the two halves cover the whole task?

**Yes.** I walked P1–P8 independently of §4's table and found each owned exactly once, with no
orphan and no portion both halves assume the other owns:

| Property | Owner in the text | Verified where |
|---|---|---|
| P1 decompose/size + over-size | B, entirely at decomposition time | §2-B, §3.5 |
| P2 N cold analysts | A, incl. all fan-out inside the item | §2-A, §3.3 |
| P3 cold verification | A | §2-A |
| P4 agreement-ranked merge | A | §2-A |
| P5 blind roll-up | B (structure fixed §3.2/§3.4) | §2-B, §3.2 read table |
| P6 Layer-2 config | B owns file+contract; namespaces partitioned §3.6 | §3.6 |
| P7 restart/resume | B across nodes, A within an item | §3.5, §2-A |
| P8 facts-not-interpretation | A enforces, B states | §3.7 rule 7 |

Non-property remainders also have owners: the run driver, `decisions.md`, escalation, `findings.md`,
degenerate corpora, the entry surface, `stages/common.md`, and house-style checking. I found **no
orphaned remainder**. The one deliberate exclusion (§3.10: no test harness / no packaging) is
consistent with the siblings — neither `Guarded_change/` nor `Dragonfly/` ships a harness *for
itself*; their "harness" is a stage inside the loop, for the change under test
(`Dragonfly/METHODOLOGY.md:166` `8-harness.md`; `Guarded_change/SKILL.md:2` description). I do **not**
contest that ruling.

### Q2 — The seam: stated, sound, self-contained?

**Stated:** yes, at unusual length and specificity (§3.1–§3.11).

**Self-contained:** I hunted specifically for the producer/consumer form `redteam-split.md:44-51`
warns about. There are exactly three cross-half artifacts that one half must know about the other:
A's **merged-findings filename**, A's **config keys**, A's **stop conditions**. All three are handled
as *build-time* dependencies — B's steps are written as rules over the merged plan — which
`divider.md:83-86` explicitly blesses as a legitimate home. That is the correct call and it is
executed consistently (§2-B "Steps written as rules over the merged plan", §3.6, §3.8).

**But the build-time route has an unexamined precondition**, which is finding **M1** below: the
declarations those rules consume must survive `Consensus`, and nothing requires them to be in a form
`Consensus` can carry.

**Sound:** mostly, with one termination hole (**B1**) and one missing invocation anchor (**M2**).

### Q3 — The floor: would either half fall below it?

**No.** Floor = "one file created or one coherent edit to one file, with the content specified."
A plans ≥3 role-prompt files (stages 2–4) plus finding/citation/diagnostic formats; B plans ≥9
artifacts (`SKILL.md`, `METHODOLOGY.md`, `README.md`, worked config, `stages/common.md`, stages 0/1/5,
the concatenation step). Both are multi-file whole tasks, an order of magnitude above the floor.
§5's own accounting is accurate. **Clean — this is not a task that should have been left undivided.**

### Q4 — Real joint or arbitrary cut?

**Real joint.** What changes at the boundary, concretely and in the text rather than in §1's prose:
the **read permission table changes** (§3.2 — below the line an agent may open corpus content for
meaning; above it, `STATUS`/`item.json`/`RUN` only, and the roll-up may read nothing but five-field
lines); the **unit of work changes** (one item vs. the tree); the **failure mode changes** (an
unresolvable citation vs. a coordinator that peeked, or work silently redone); the **review criterion
changes** (do citations resolve vs. is it blind and idempotent). Crucially, **the owner's task
statement named this boundary before any divider did** — P5 *is* the assertion that the line exists.
A cut placed anywhere else would put P5's line *inside* one half, where nothing structural enforces
it.

The rejected alternative (method vs. envelope) is recorded with its reason (§1), and the reason is
right: that boundary is packaging, and nothing about the mechanism changes at it. I looked for a
third alternative — putting decomposition (stage 0) *with* A on the grounds that both open corpus
files — and it is worse: it merges two different disciplines (read-for-shape vs. read-for-meaning)
into one half and leaves the driver stranded from the thing it decomposes. **No better cut was
available here.** I record that, since no later reviewer sees these alternatives.

---

## Findings

### B1 — `blocker` — a leaf that never writes `STATUS` is never capped; the driver does not terminate, and §3.5's termination argument is false for exactly the commonest failure

**Lens: logical / completeness.** §3.5's driver table, leaf rows:

> `leaf | no STATUS | increment RUN; dispatch A's entry agent (§3.3)`

This row carries **no cap test**. The group rows carry one — *"group | every child terminal,
`RUN ≥ run.max_attempts`, still no `STATUS` → write `STATUS = escalated`"* — but its leaf analogue
does not exist. §3.4 states *"A node with no `STATUS` file has not finished. Absence is the only
'not yet' marker."*, so a leaf whose agent dies before writing anything is indistinguishable from a
fresh leaf, forever.

**Failure scenario.** The dispatched stage-2 agent dies (context exhaustion, tool failure, harness
crash) before writing `STATUS` — the single most likely failure in a method whose premise is
"a corpus too large for one context window". Driver's next pass: no `STATUS` → increment `RUN` →
dispatch → dies → no `STATUS` → increment `RUN` → dispatch → … `RUN` increments without bound and
no rule ever converts the node to a terminal state. The run never finishes and never escalates to
the human.

This directly falsifies §3.5's stated termination argument: *"the cap converts any non-terminal node
into `escalated`"*. There is no rule that does this for a `STATUS`-less leaf. It is the same defect
§7 records as fixed for group nodes, left open on the leaf side.

**Why `blocker` and not `major`:** the seam is not negotiable by either half (§3.9 — *"Do not adjust
the seam locally, and do not work around it"*), so B's planners are bound to write a driver whose
rule table cannot reach termination, and P7 ("restart and resume") is the property it breaks.

**Remedy (one table row):** `leaf | no STATUS, RUN ≥ run.max_attempts → replace STATUS with
<node_id> escalated 0 0 0, append to decisions.md, stop for the human.` and reorder the leaf rows so
the cap row is tested first.

---

### M2 — `major` — A's entry agent is given no anchor from which to resolve `stages/stage-3.md` and `stages/stage-4.md`, and the seam forecloses every route to one

**Lens: unstated assumptions / completeness.** §3.3 fixes the invocation contract hard:

> *"B's run driver dispatches exactly ONE agent per leaf node, on the role file `stages/stage-2.md`,
> with exactly ONE argument: `item_dir` (absolute). That agent reads `item_dir/item.json` for
> everything else"*

and §3.3's field table is closed: *"Exactly these fields; A may not require others, B may not omit
any."* §2-A then makes that same agent responsible for **all** fan-out inside the item — spawning
the N analysts, the verifier and the merge, i.e. dispatching agents on `stages/stage-3.md` and
`stages/stage-4.md`.

**Failure scenario.** A's planner must write a step that says "dispatch a cold agent on
`<path>/stages/stage-3.md`". It holds `item_dir` (under `run.dir`) and `config_path`. Neither is
anchored to the skill root: `run.dir` is B's key with B's default, A may not read B's namespace
(§3.6), and §3.2 only says B's *default* follows the siblings' convention of living inside the skill
directory — a default, not a guarantee, and the seam explicitly permits it to be configured
elsewhere. So A must **invent** an anchor (e.g. `item_dir/../../..`, or a relative path assumed to
resolve). Its plan looks locally correct and breaks the moment `run.dir` is configured outside the
skill directory. This is precisely the invent-it-and-look-correct failure `redteam-split.md:47-51`
describes, arriving through a closed field list rather than through a producer/consumer clause.

**Remedy:** add one field to §3.3's table — `skill_dir` (absolute path to `Data-Distiller-impl/`) —
or one sentence fixing that A's entry agent may resolve sibling role files relative to the role-file
path it was itself dispatched on. Either is a single line and costs no blindness (a path to a role
file is not a finding).

---

### M1 — `major` — the declaration obligation, on which four of B's build-time rules depend, has no form that is guaranteed to survive `Consensus`

**Lens: unstated assumptions / logical.** §3.1's declaration obligation is the load-bearing
substitute for a channel: B's `SKILL.md` router table, `SKILL.md` Stop-for-human section,
`METHODOLOGY.md` stage index and config contract, `index.md`'s findings pointer and `findings.md`'s
assembly rule are *all* written as rules consuming A's declarations (§2-B, §3.6, §3.8). §2-A says so
explicitly: *"these are consumed by the other half's build-time rules, so omitting any of them
leaves a step in the merged plan unexecutable."*

**But a half's plan is not necessarily what its planner wrote.** If a sub-task reaches leaves rather
than a further division — which is the expected fate of A, at three role files plus formats — three
leaves plan it and `Consensus` merges them: *"2-of-3 on numbered steps, INCLUDING ORDER. The odd plan
is discarded"* (`Architect/stages/combiner.md:22`). `Consensus` is defined **only over numbered
steps**. `combiner.md` gives it no rule for non-step content, and `common.md`/`combiner.md` bar it
from authoring (`combiner.md:6`).

**Failure scenario.** A's three leaves each write a "Declarations" preamble or appendix — not a
numbered step. `Consensus` merges the numbered steps and has no rule that carries the preamble; or
it carries only one of three and cannot say which is agreed. The merged A-plan reaches `Union`
without a declared merged-findings filename. B's `index.md` step ("naming that node's merged-findings
file as declared in the merged plan") and B's `findings.md` assembly rule (§3.8) are then
unexecutable, and the corpus-level output — *the artifact the method exists to emit* (§3.8) — cannot
be built. Nothing downstream detects this: both plans look internally complete.

This is the same structural blind spot §3.9 identified for `SEAM-OBJECTION` and mitigated by
requiring the objection to *also* appear inside affected steps, where two planners can independently
produce it. The declaration obligation needs the identical treatment and does not have it.

**Remedy, inside the seam:** state in §3.1 that each half's declarations must be expressed **as
ordinary numbered plan steps** — concretely, a final numbered step *"create
`Data-Distiller-impl/PLAN-DECLARATIONS.md` containing …"* with its content specified — so that three
independent planners produce the same step at the same position and `Consensus` carries it. (This
also needs §3.1's "may not add a top-level file" rule amended to permit that one file, or the
declarations placed in an existing owned file.)

---

### M3 — `major` — the size-bound invariant relates two numbers chosen blind, and no step reconciles a violating pair

**Lens: logical.** §3.5 states the invariant `sizing.max_item_bytes ≤ analysis.max_item_bytes`, and
§3.6 says it is *"stated by B in `METHODOLOGY.md`'s config contract as a rule over the merged plan"*.
Stating an invariant is not enforcing it. B declares `sizing.max_item_bytes` with a default; A
declares `analysis.max_item_bytes` with a default; neither may read the other's namespace (§3.6);
the two are chosen with no knowledge of each other.

**Failure scenario.** A, reasoning about how much one analyst can hold, defaults
`analysis.max_item_bytes = 100_000`. B, reasoning about structural boundaries, defaults
`sizing.max_item_bytes = 400_000`. Both plans are internally correct. The merged plan produces a
worked example config (§3.6: *"one entry per key declared by either half's plan, with its declared
meaning, type and default"*) that **violates the invariant its own contract section states**, and
`METHODOLOGY.md` documents a rule the shipped example breaks. At run time every item between the two
bounds is decomposed happily by B and written `state=failed` by A — silent, systematic data loss
dressed as a normal failure state. No step in either half owns "detect and fix a violating pair".

Note this is *not* fully absorbed by "A writes `failed`": that is the run-time safety net, and it is
correct. The defect is that the shipped defaults are permitted to be wrong with nobody assigned to
notice.

**Remedy, in the seam:** either fix a concrete byte figure for `sizing.max_item_bytes` in §3.5 (the
seam already fixes lines-as-locator-unit and bytes-as-size-unit, so fixing one number is in
character), or add a build-time rule B owns: *"the worked example config sets `sizing.max_item_bytes`
to the merged plan's declared default for `analysis.max_item_bytes`; if the two declared defaults
violate the invariant, the example takes A's value and `METHODOLOGY.md` records the reconciliation."*

---

### M4 — `major` — the run driver is a single agent reading the whole `index.md`, which is the exact scale argument §3.2 uses to justify the tree; and §3.2's "EXHAUSTIVE skeleton" forbids the natural fix

**Lens: logical / fidelity.** §3.2 justifies the recursive tree with:

> *"which is what P5's 'per-**child** status' and 'too large for one context window' jointly require:
> a single coordinator reading one line per item does not fit a corpus this method exists for."*

That argument is applied to the roll-up coordinator and **not** to the run driver, which §2-B defines
as the agent that *"walks `index.md`, decides which nodes still need work"* — i.e. a single
coordinator reading one line per item, for the whole corpus, in one context. It is stage 1, a role
prompt (§3.1), therefore a dispatched agent.

**Failure scenario.** A corpus decomposing to 20,000 items. `index.md` is a 20,000-line inventory.
The stage-1 driver agent must hold it to decide dispatch order and to re-derive resume state on every
pass. It exhausts context mid-walk and either stops silently or restarts from the top; on restart the
same thing happens, so the tail of `index.md` is never reached and those items are never dispatched.
The roll-up above them then never runs (its children are non-terminal), so the run stalls with no
escalation — and B1 means the stall is silent.

**Why the seam is implicated rather than B's internals:** §3.2 declares the run-directory skeleton
**EXHAUSTIVE** — *"Neither half may add a file or directory to it"* — with the sole exception of A's
per-item outputs. So B cannot shard the inventory (per-group `index.md` files under each group node
directory) without violating the seam, which §3.9 forbids it from doing locally. The mitigation left
to B is chunked/`grep`-style reading of one large file, which is workable but is exactly the kind of
thing that should be settled at plan time rather than invented.

**Remedy:** either permit a per-group index file inside each group node directory in §3.2's skeleton,
or state in §3.5 that the driver walks the node **directory tree** (a group's children are its
subdirectories, §3.2 already guarantees this) and that `index.md` is a human-facing inventory rather
than the driver's working input.

---

### M5 — `major` — the seam's transport is asserted as an instruction to the node, when the divider can guarantee it unilaterally by making the concatenated text *be* the returned sub-task

**Lens: factual / missed opportunity.** The preamble and §6 report as an apparatus gap that
*"Nothing in `divider.md` or `node.md` instructs [prepending]; `node.md` passes only
`division.first` / `division.second`"*, and resolve it by having *"the division's return value state
it as an explicit instruction to the node."*

I verified both halves of the factual claim: `node.md:85-88` does spawn children with
`(division.first, plan, granularity, depth+1, node_id+".1")` and nothing else, and neither
`divider.md` nor `node.md` contains a prepend instruction. **But the conclusion does not follow.**
The divider authors `division.first` and `division.second`. If it returns
`division.first = <§3 verbatim> + <§2-A text>` as a single string, `node.md:86` transports the seam
with no cooperation, no new mechanism, and no apparatus change. The current wording instead makes a
load-bearing artifact depend on a node agent obeying an ad-hoc instruction for which its own role
file has no rule — and `node.md:33-37` tells the node it neither plans nor authors, which is a reason
it may treat a formatting instruction as out of scope.

**Failure scenario.** The node passes `division.first` as-is, honouring its role file. A's three
planners receive §2-A alone. §2-A references §3.3, §3.4, §3.5, §3.6, §3.7 and §3.9 by number — they
now resolve to nothing. Each planner falls back on the file path §2-A supplies, or invents the
status schema, the item record and the write rules. Every self-containment guarantee in §6 evaporates
at the one step nobody re-checks.

**Remedy:** change §2's *"delivered with §3 prepended verbatim"* and §6's *"stated as an instruction"*
to a statement that the returned `division.first`/`division.second` values **are** the concatenated
texts. The "apparatus gap" then disappears rather than being reported. (The propagation clause in
§3's first paragraph is fine as-is: a re-dividing node's `Divisible` call reads the whole sub-task
text and will see it — *provided* the concatenation actually happened, which is the same fix.)

---

### m1 — `minor` — two group rows of the §3.5 driver table match simultaneously, with no stated precedence

Rows *"group | every child terminal, no `STATUS` → increment `RUN`; dispatch the roll-up"* and
*"group | every child terminal, `RUN ≥ run.max_attempts`, still no `STATUS` → write `escalated`"*
both match when a group is at the cap with no `STATUS`. Nothing states first-match-wins or
most-specific-wins. A planner reading top-to-bottom dispatches forever. Fixable in place: state row
precedence, or make row 5's condition `RUN < run.max_attempts`.

### m2 — `minor` — resume against a *changed* corpus is unowned

P7 is "restart and resume from on-disk state". §3.2 makes `item.json` **IMMUTABLE** and *"never
written twice and never deleted"*, and §3.5's resume reads file presence only. If the corpus changes
between runs sharing a `run.dir` (a log grows, a file is edited), the existing items' locators still
resolve but now address different content, and new content is never decomposed. The run reports
`done` over a corpus that no longer exists. This sits entirely inside B's P7 ownership so it needs no
seam change — it needs a step. Carry it to B: define whether `run.dir` reuse across a changed corpus
is detected (e.g. a corpus fingerprint in `index.md`) or documented as forbidden.

### m3 — `minor` (missed opportunity) — A's merged-findings filename could have been fixed in the seam like every other name

The seam fixes `index.md`, `decisions.md`, `findings.md`, `item.json`, `RUN`, `STATUS`, the stage
numbers and the config namespaces. It leaves exactly one filename to the declaration obligation —
and that one name is consumed by two of B's build-time rules (§3.8's assembly, §2-B's `index.md`
pointer), making it the single largest residual cross-half dependency and the one M1 puts at risk.
Fixing it (e.g. `merged-findings.md` inside the node directory) costs nothing — it does not constrain
A's *format*, only its filename — and would retire both. The build-time-rule route is legitimate
(`divider.md:83-86`), so this is an available cheaper option, not a defect.

### m4 — `minor` — config-path validation at run start is a house-style precedent with no owner

The seam requires B to validate every `locator` (§3.3) and cites both siblings for it. But the
siblings' rule is broader and is about the **config**: `Dragonfly/SKILL.md:19` *"Validate config
paths at hunt start: dead/unresolvable → stop"*; `Guarded_change/METHODOLOGY.md:139` *"Paths are
validated, not assumed."* Nothing in the seam assigns "validate `config_path` and the corpus root
named in the config, at run start, before decomposition". It falls naturally to B (stage 0 or 1) and
should be named there, since A receives `config_path` in `item.json` and is entitled to assume it
resolves.

### n1 — `nitpick` — "letter-suffixed files, as the siblings do" is half-accurate and would forbid the other sibling's form

§3.1 permits *"letter-suffixed files within its own phases (`stage-0a.md`, as the siblings do)"*.
`Dragonfly/stages/` does use `stage-0a.md`/`stage-0b.md`; `Guarded_change/stages/` uses
`stage-1.5.md` — a decimal, not a letter. As written the rule bans the Guarded_change convention
while citing "the siblings" for authority.

### n2 — `nitpick` — §3.1's "may not add a top-level file" reads against §3.2's `run.dir` default

§3.2 says B's `run.dir` default follows the siblings' convention of living inside the skill directory
(`changes/<slug>/`, `hunts/<slug>/`). That creates a top-level `runs/` (or equivalent) directory at
run time. §3.1's prohibition is plainly about *planned* files, but one sentence distinguishing
build-time layout from run-time artifacts would remove the reading.

---

## The six lenses — verdict for each

**1. Factual — one finding (M5); otherwise clean, and earned by citation.** I resolved every external
citation in the document. Verified correct: `Guarded_change/SKILL.md:28` (*"Step numbers below are
the canonical stage numbers used everywhere"*), `Dragonfly/SKILL.md:19-20` (validate config paths at
hunt start), `Dragonfly/SKILL.md:31` (`hunts/<slug>/`), `Guarded_change/SKILL.md:27`
(`changes/<slug>/`), `Guarded_change/METHODOLOGY.md:139` (*"Paths are validated, not assumed"*),
`Dragonfly/METHODOLOGY.md:143` (`hunts/<slug>/` artifact layout), `Dragonfly/stages/charter.md:1`
(*"The red-team charter (shared by stages 1, 4, 7)"* — a charter read at specific stages, not a
universal preamble), `Architect/stages/common.md:3` (the universal-preamble pattern is Architect's
own), `Architect/stages/leaf.md:47` (*"You do not file findings…"*), `combiner.md:22` (`Consensus`
2-of-3 including order, odd plan discarded), `combiner.md:6` (*"None of the three is an author"*),
`combiner.md:39` (`Union` discards nothing). §3.7's precedent note is correct: neither sibling has a
`common.md`; both have `stages/charter.md`. §6's reported contradiction between `divider.md:80-82`
(Union offered as a home for reconciliation) and `combiner.md:6` (Union may not author) is **real**
and honestly reported. The one factual over-reach is M5's transport conclusion.

**2. Logical — B1, M1, M3, M4, m1.** The termination argument in §3.5 is the weak point: it is stated
as proved and is false for `STATUS`-less leaves.

**3. Missed opportunity — m3, and one recorded non-finding.** The alternative cut (method vs.
envelope) is recorded and correctly rejected; I searched for a third (decomposition placed with A)
and it is worse. No better joint was available.

**4. Unstated assumptions & risks — M2, M1, M3, m2.** The largest unstated assumption in the document
is that a planner's *non-step* content reaches the merged plan intact.

**5. Fidelity — clean.** Terms pinned to mechanisms: **"blind roll-up"** → §3.2's read row for stage
5, *"the `STATUS` lines of its own children, and nothing else"*, plus §3.4's deliberate removal of any
findings path — structural, not exhortative. **"terse per-child status"** → five whitespace-separated
fields, domains fixed. **"cold"** → §3.7 rule 1, no shared context with caller or siblings, with
dispatch-point enforcement assigned to A. **"decompose"** → B stage 0, structural boundaries from the
Layer-2 config, recursive to `sizing.max_item_bytes` or `sizing.max_resplits`. **"verify"** → a
separate cold agent, *"never the analyst that produced the finding"*, with `n_dropped` surfaced.
**"agreement-ranked merge"** → matching across N analysts with an agreement count, `max_agreement`
surfaced. **"read-only"** → §3.7 rule 3 plus A's obligation to say what it concretely forbids.
**"cite every finding"** → §3.7 rule 4 duty, format owned by A. **"restart/resume"** → §3.5's
presence + `RUN` + `state` table (holed by B1). **"facts, not interpretation"** → §3.7 rule 7 plus
§2-A's demand for *"an enforceable rule rather than an exhortation"*. Each is a mechanism, none is a
proxy. The additions-only carve-out in §3.7 ("specifying the enforcement mechanism is an addition,
not a restatement") correctly resolves what would otherwise be a collision between A's ownership of
P2/P8 and B's ownership of `common.md`.

**6. Completeness — B1, M1, M2, M4, m2, m4. Generative sweep was run.** Beyond the structure's own
required parts (joint, sub-tasks, seam, coverage, floor, self-containment audit — all present), I
swept for load-bearing sections the document's own list does not anticipate, looking specifically
for: a termination proof (present but false — B1); an invocation *anchor* as distinct from an
invocation *contract* (absent — M2); the survival path of plan content that is not a numbered step
(absent — M1); the scale story for the coordinator that is *not* the roll-up (absent — M4); corpus
mutation between runs (absent — m2); config validation as distinct from locator validation (absent —
m4); concurrency/write conflict on a leaf `STATUS` with two possible owners (**present and sound** —
§3.3 has the driver wait for the agent to return, and the driver only writes `escalated` after the
cap, so the two writers never overlap); the empty corpus and the single-item corpus (**assigned**, to
B, §2-B); and what happens to a `partial` leaf's existing findings when the driver escalates it
(**present** — §3.5 preserves the integers, §3.8 still emits its section). Six gaps found, three
clean.

---

## Restating the verdict

**The joint is right and I would keep it.** Coverage is complete, both halves are far above the
floor, and the seam is self-contained in the strict sense `redteam-split.md` demands — the one
residual plan-time dependency (M1) is a defect in *how* the declarations travel, not evidence that
the cut needs a channel.

**I do not object to going forward.** B1 and M1–M5 travel down with the sub-tasks and are fixable in
the seam text; none of them argues for a different boundary. B1 in particular is a single missing
table row, and I have written the row.
