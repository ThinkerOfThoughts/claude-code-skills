# Split review — round 3, reviewer A (cold, independent)

**Under review:** `Architect/runs/data-distiller/it3/0/split-round-3.md` — the proposed division of the
Data-Distiller planning task into sub-task A (per-item finding pipeline) and sub-task B (corpus envelope).

**Fence compliance:** I did **not** open, read, list, glob, grep or otherwise access
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did **not** invoke the
installed `data-distiller` skill. I read no file named `split-review-*.md`. I read no plan, because none
exists and none was given to me — I judged the cut against the shape of the task.

**What I did read:** the three Architect stage files naming my charter; `Architect/stages/divider.md`,
`node.md`, `leaf.md`, `combiner.md` (to check §3.9's and §6's citations about `Union`, `leaf.md:47` and the
spawn mechanics); the sibling skills `Guarded_change/` and `Dragonfly/` (SKILL.md, METHODOLOGY.md,
stages/, directory listings) to check §3.1/§3.2/§3.3/§3.7's factual claims; and split-round-3.md itself.
I did **not** read split-round-1.md or split-round-2.md — I reviewed round 3 on its own merits and treated
§7 as claims.

---

## VERDICT — the two parts

**Part 1 — what I found:** two `blocker`s, two `major`s, three `minor`s, two `nitpick`s. **All of them are
defects in the seam text (§3), not in the joint.** Both blockers are the same class of defect round 2
already hit once and the divider already partially spotted: a `STATUS` field/state whose lifecycle nobody
can execute. They are fixable by editing §3.4/§3.5 without touching the boundary.

**Part 2 — do I object to going forward with this cut? NO. I do not object.**

The joint is real and I would keep it. `P5` — *"a blind roll-up in which a coordinating agent reads only a
terse per-child status"* — is not a feature that happens to sit on one side of a line; it is the owner's own
assertion that the line exists. Cutting anywhere else would put the blindness boundary *inside* one half,
where nothing downstream could check it. Concretely different on each side: what is read (corpus content
for meaning vs. corpus shape and one-line statuses), what is produced (cited evidence vs. bookkeeping), the
characteristic failure (a fabricated citation vs. a coordinator that peeks), and the review criterion (does
every citation resolve vs. is it blind and idempotent). That is four independent axes changing at one
boundary — not a bisection for symmetry.

Round 2's structural failure — a producer/consumer seam — appears to me to be **genuinely resolved**, not
papered over. I checked this specifically (see Lens 5 and Lens 6). Carry my findings down with the halves.

---

## Findings

### F1 — `STATUS` is write-once, so every retry path in §3.5 is unreportable and the run can never reach `done` — **blocker**

§3.2's skeleton marks `STATUS` **WRITE-ONCE**; §3.2 prose repeats *"`STATUS` is never overwritten."*
§2-A tells A: *"Writing the leaf `STATUS` line (§3.4) as the last act of your pipeline."* §3.4 defines
leaf `partial` as *"the pipeline completed some phases and could not complete the rest… **Re-runnable.**"*
§3.5 row 3 then says on `state=partial` and `RUN < run.max_attempts` → *"increment `RUN` and re-dispatch."*

**Failure scenario (leaf).** Item `0.3` runs; analysts and verification complete, merge does not. A writes
`STATUS` = `0.3 partial 12 4 0`. The driver re-dispatches. A resumes, completes the merge, and must now
record `done` — but `STATUS` exists and is write-once, so it cannot. The node reports `partial` forever
despite being complete, and `n_findings`/`max_agreement` stay stale at their mid-pipeline values. The
verification-and-merge counts that §3.4 defines as the *only* upward signal are permanently wrong.

**Failure scenario (group), same defect one level up.** §3.5 row 1: *"group → run the roll-up once every
child has a `STATUS`."* That precondition is satisfied the moment a `partial` child writes its line — before
the retry has even been dispatched. The roll-up runs, writes the group `STATUS` = `partial` (write-once),
and the children then finish. §3.4's group rule *"`done` — every child is `done`"* can never subsequently be
applied. So a single retry anywhere in the tree pins the root at `partial` permanently, and §3.4's
`done` state is unreachable for any run that was not perfect on the first pass. That is the whole method's
completion signal.

**The alternative reading is worse, not better.** If one tries to rescue this by having A never write
`partial` (writing `STATUS` only when terminal), then §3.5 row 1 governs — *"no `STATUS` → leaf → increment
`RUN` and dispatch"* — and that row contains **no cap check**; the cap is tested only on the
`partial`/`failed` row. Dispatch would then be unbounded, contradicting §3.5's own closing claim *"Every path
terminates."* Both readings break, so this is not an ambiguity a planner can resolve locally.

The divider saw the adjacent instance of this — §3.5's cap row explicitly says *"write nothing to `STATUS`
(it is write-once and already exists)"* — and did not notice that the *succeeding* retry and the *group
roll-up* have the same problem. Note that the divider's own challengeable note in §3.5 justifies write-once
on the grounds that mutation *"is what produced three of round 2's majors"*; that motivation is sound, but
the current text buys immutability at the cost of the state machine, and the trade needs re-deriving rather
than defending.

### F2 — the leaf state `escalated` has no producer; §3.4 and §3.5 directly contradict each other — **blocker**

§3.4: *"`escalated` — **terminal, do not re-run**, and the human is told. **Written when the attempt cap in
§3.5 is reached.**"* §3.5, the cap row: *"**If `RUN ≥ run.max_attempts` → write nothing to `STATUS`** … the
driver records the exhaustion in `decisions.md` and **treats the node as `escalated`** for roll-up and
termination purposes."*

So §3.4 says a line is written and §3.5 says no line is written. Worse, the only two candidate writers are
both disqualified: `STATUS` at a leaf is A's per §3.2's skeleton, but A is not listed as a reader of `RUN`
in §3.2's read table and therefore cannot know the attempt count; and the driver, which does hold `RUN`, is
told by §3.5 not to write. **No agent can produce a leaf `escalated`.**

**Failure scenario.** Leaf `0.3` fails three times and exhausts `run.max_attempts`. Its `STATUS` still reads
`0.3 failed 0 0 0`. The roll-up coordinator for group `0`, which §3.2 restricts to *"the `STATUS` lines of
its own children, and nothing else"*, sees `failed` — a re-runnable state — and applies §3.4's group rule
*"`escalated` — at least one child is `escalated` and no child is re-runnable"*, which does not fire. The
group rolls up `partial`. So group `escalated` is also unreachable, and the fact that a chunk of the corpus
was abandoned is **invisible everywhere above the driver** — including in the root status a human reads.
The driver's *"treats the node as `escalated`"* is a driver-internal notion with no representation in the
one vocabulary the seam says crosses the boundary upward (§3.4's title: *"the ONLY thing that crosses the
boundary upward"*).

This is structurally the same defect as round-2's C-F3/A-F1/B-M4 (*"nobody assigned to produce
`state=oversize`"*), which §7 records as fixed by deleting `oversize`. Deleting that state did not remove
the pattern; it reappeared on `escalated`.

### F3 — the seam's own transport is asserted, not mechanised, and it demonstrably cannot propagate past one level — **major**

§2 opens *"Both sub-task texts below are delivered with §3 (the seam) prepended verbatim — see §6"*, and §6
concludes *"§3 is **prepended verbatim to each sub-task before it is passed to a child node**… **The seam
propagates unchanged to every descendant** — a child node's own divider carries it down with whichever
sub-task it splits further."*

Nothing performs either step. `Architect/stages/node.md:85-88` is the only spawn site, and it reads:
*"spawn **two child nodes** … with `(division.first, plan, granularity, depth + 1, node_id + ".1")`"* — it
passes the division's sub-task through verbatim and has no prepend step, no seam argument, and no knowledge
that a seam is a separate object. `divider.md:38-42` gives a divider *"The **task** and the **granularity
floor**"* and nothing else. So:

- **At level 1**, prepending happens only if the divider itself wrote §3 into the sub-task strings. It did
  not: §2-A and §2-B are blockquotes that reference §3 by *section number* (§3.1, §3.3, §3.4, §3.5, §3.6,
  §3.7, §3.8, §3.9 — nine distinct cross-references in §2-A alone). Whoever assembles `division.first` must
  perform an operation the seam names but no charter instructs. This is partially mitigated: both sub-tasks
  carry the absolute path to split-round-3.md and `common.md` §2 permits opening what a task points at. So
  a level-1 planner can recover the seam — but only by reading a section-numbered document whose §2 refers
  to *the other half's* sub-task, which is precisely the blind-planning contamination the cut exists to
  prevent.
- **At level 2 and below**, the mitigation fails outright. When B (larger, and §5 concedes it *"remains
  divisible one level down"*) is split, its child divider produces *new* sub-task texts. Nothing in
  `divider.md` tells that divider it inherited a seam, and its output will contain its own §3 with its own
  numbering. §6's claim that the seam *"propagates unchanged to every descendant"* has no carrier.

**Remedy that stays inside the seam:** state §3's content inline inside each sub-task text rather than by
cross-reference, and add an explicit clause obliging any descendant divider to reproduce the inherited seam
verbatim at the head of its own seam. §5 makes this urgent, not hypothetical, because it *plans* on B being
re-divided.

### F4 — a corpus region that decomposition cannot bring within the size bound vanishes from `findings.md` without trace — **major**

§3.5: *"**An item that cannot be brought within the bound is not emitted as a leaf**: it is recorded in
`index.md` and `decisions.md` and escalated to the human at decomposition time."* §3.8's assembly rule is
quantified over **leaf nodes**: *"One section per leaf node in `index.md` order"*, with three cases — leaf
with a merged-findings file, leaf with a `STATUS` and no file, leaf with no `STATUS` (`NOT RUN`).

A region that is never emitted as a leaf matches none of the three cases, so it contributes **no section at
all**. §3.8 calls `findings.md` *"the artifact the method exists to emit."* A reader of that artifact cannot
tell that part of the corpus was never analysed. For a method whose entire purpose is trustworthy extraction
from a corpus too large to read directly, an output that silently omits a region is worse than one that
reports failure — the reader's only check on coverage is the artifact itself.

The human is stopped at decomposition time, which limits the blast radius but does not fix it: the run can
be resumed or the escalation acknowledged, and `findings.md` is still assembled later with the hole
undisclosed. This is a seam defect, not B's planning latitude, because §3.8's assembly rule and §3.5's
non-emission rule are both fixed in the seam and are inconsistent with each other.

**Remedy inside the seam:** either give non-emitted regions a fourth §3.8 case, or require them to be
emitted as leaves with `state=escalated` (which F2 must make producible anyway).

### F5 — nothing requires decomposition to cover the corpus exhaustively or without overlap — **minor**

`P1` is *"decompose and size the corpus into items"*. §3.3 fixes the item record's fields and value domains
and requires per-item `locator` validation (*"a locator that does not resolve to a readable path and range
is **not written as an item**"*), but no clause anywhere requires the union of all `locator`s to cover the
corpus, or requires them to be disjoint. A decomposer that drops the tail of a file, or emits two items over
the same line range (double-counting `n_findings` and inflating `max_agreement` up the roll-up), satisfies
every stated rule. This is B's to plan, so it travels down as a finding against B rather than against the
joint — but it is worth stating in B's sub-task text because the size/tier framing of §3.5 makes it easy to
plan sizing without ever planning coverage.

### F6 — the seam's enumeration of `SKILL.md` omits a section both siblings carry — **minor**

The task says *"Check it against the sibling skills … for house style and structure."* §3.1's layout line
and §2-B both scope `SKILL.md` as *"frontmatter + router table + Stop-for-human"*. Both siblings have a
fourth top-level section: `Guarded_change/SKILL.md:75` and `Dragonfly/SKILL.md:83` are both
`## Self-check / dogfooding`. `Dragonfly/SKILL.md:22` additionally carries `## Before you start: cold-start
guard`. §3.1 forbids adding top-level *files*, not sections, so B is not blocked — but the seam's
three-element enumeration reads as exhaustive and a blind planner is likely to take it that way. One clause
("this enumerates the minimum, not the maximum; match the siblings' section set") closes it.

### F7 — §5 defers B's imbalance to B's own `Divisible` without checking that a sub-cut of B is feasible under the now-binding seam — **minor**

§5: *"**B is roughly twice A's size and is arguably two design concerns** … B **remains divisible one level
down** — its own `Divisible` call is where that gets resolved."* This is a reasonable disposition of
round 2's A-F10, but it is asserted without a feasibility check, and round 3 made the check harder by
tightening §3.1 to *"BINDING at phase level"* and §3.2's skeleton to *"EXHAUSTIVE. Neither half may add a
file or directory to it."* B's plausible sub-cut — corpus-to-items machinery (stages 0, 1, `index.md`,
`item.json`) versus entry surface (`SKILL.md`, `METHODOLOGY.md`, `README.md`, the worked config,
`common.md`) — puts `stages/common.md` and the config-contract section on the entry-surface side while §3.7
fixes their content in terms the machinery side owns, and puts §3.8's concatenation step (B's *"final stage
file"*) ambiguously. Combined with F3, a divider one level down has neither the seam text nor a statement of
which seam clauses are still binding on it. Naming, in the seam, that the whole of §3 binds every
descendant regardless of how B is further cut would cost one sentence.

### F8 — *"letter-suffixed files … as the siblings do"* is true of one sibling only — **nitpick**

§3.1: *"each half may add letter-suffixed files within its own phases (`stage-0a.md`, as the siblings do)"*.
`Dragonfly/stages/` does contain `stage-0a.md` and `stage-0b.md`. `Guarded_change/stages/` uses a *numeric*
sub-stage — `stage-1.5.md` — which is surfaced as a first-class row in that skill's router
(`Guarded_change/SKILL.md`, the `| **1.5** |` row). So the rule as written forbids the pattern one of the
two named house-style references actually uses. Harmless, but the parenthetical overstates the precedent.

### F9 — `index.md`'s per-node findings pointer sits in mild tension with §3.4's own rationale — **nitpick**

§3.4 removes `findings_path` with a strong argument: *"putting the locator of the findings into the blind
coordinator's only input turns P5 from a structure into an exhortation."* §2-B then requires `index.md` to
carry a per-node findings pointer, and §3.2's read table lets B's run driver read `index.md`. The driver is
not the coordinator and *"holding an address"* is not *"reading a finding"*, so blindness is not actually
breached — but the seam relies on that distinction without ever stating it, and it is exactly the
distinction a planner under pressure will blur. One clarifying sentence in §3.2's driver row would settle it.

---

## The four questions

**1. Coverage — clean, with F4 and F5 attached.** I checked §4's table against P1–P8 independently rather
than accepting it. Each of the eight has exactly one named owner, and the three cases where ownership is
genuinely split (P6 config, P7 resume, P8 facts-not-interpretation) are split along a stated line rather
than left ambiguous: P6 by key namespace (§3.6), P7 by within-item vs. across-node (§2-A/§2-B, both keyed to
the single presence rule in §3.2), P8 by duty-vs-enforcement (§3.7's closing clause). I also swept for
task elements *outside* the eight properties: the build root, the run driver, the corpus-level output, the
entry surface, degenerate corpora, the house-style check against the siblings, and the off-limits fence —
all present and owned. **No orphaned remainder found and no portion both halves assume the other owns**, with
the exception recorded as F4 (a corpus region that falls out of both halves' output rules) and the weaker
F5.

**2. The seam — stated, sound with two blockers, self-contained.** *Stated:* yes, at length and concretely —
§3 fixes the layout, the run-directory skeleton, the item record's fields and value domains, the invocation
target/arity/argument, the five-field status line, the control loop, the config namespaces, `common.md`'s
rule set, the assembly rule, and the objection path. *Sound:* not yet — F1 and F2 make the retry and
escalation paths unexecutable. *Self-contained:* **yes, and I checked this as the priority item**, because it
is the failure my aiming file says this question keeps missing. I looked for anything of the form *"A
produces X at plan time and B consumes it"* and found four candidates, all of which turn out to be legitimate
build-time reframings under `divider.md:83-86` rather than plan-time channels:

- A's **merged-findings filename** — consumed by B's `index.md` and `findings.md` steps. B never needs the
  name at plan time; §2-B instructs B to write those steps as rules (*"naming that node's merged-findings
  file as declared in the merged plan"*), and §3.1 item 3 obliges A to declare it. A practitioner holding the
  merged plan can execute both. Legitimate.
- A's **config keys** — consumed by B's `METHODOLOGY.md` contract and the worked example. Same structure:
  §3.6 makes both a rule over the merged plan (*"one entry per key declared by either half's plan"*).
  Legitimate. The one key B genuinely needs by name at plan time — `analysis.max_item_bytes`, for the
  invariant in §3.5 — is **named in the seam text itself** rather than derived. That is the correct move.
- A's **stop-for-human conditions** — §3.1 item 4 plus a rule in §2-B. Legitimate.
- A's **file inventory** for `SKILL.md`'s router table and `METHODOLOGY.md`'s stage index — §3.1 fixes stage
  numbers *2 = pipeline entry + analysts, 3 = verification, 4 = merge* in the seam, so B does not have to
  guess; the letter-suffixed additions are covered by the rule form. Legitimate.

Everything else that could have been a channel is written down in full in §3 (item record, status vocabulary,
skeleton, read-permission table, `common.md` rules) or partitioned so neither half needs the other's
(config namespaces, stage numbers). §6's closing claim — *"No element of this seam has the form 'one half
produces X at plan time and the other consumes it'"* — I independently believe to be true. F3 is a separate
defect: not a channel, but a failure to *deliver* the seam that everything above depends on.

I also checked §6's claim of a charter contradiction and confirm it: `divider.md:80-82` offers deferral to
`Union` as *"named reconciliation work"*, while `combiner.md:6` says *"**None of the three is an author.** You
do not improve, rewrite, or adjudicate the material"* and `combiner.md:39` gives `Union` one rule, *"Stick the
inputs together into one. DISCARD NOTHING."* The divider is right not to rely on option 2, and right that
§3.9 uses `Union` only as transport, which `combiner.md:39-41` does guarantee.

**3. The floor — clean.** The floor is *one file created or one coherent edit to one file, with the content
specified.* A owns at minimum `stages/stage-2.md`, `stage-3.md`, `stage-4.md` plus the finding-record and
citation-format content that goes inside them, and must choose and justify N, define independence
enforcement, define operational unverifiability, and define agreement matching — several files' worth of
specified content, comfortably above one file. B owns at minimum nine artifacts. **Neither half falls below
the floor**, so this is not a task that should have been left undivided. I applied the floor as given and did
not file any finding whose only remedy is decomposition beneath it — in particular, I did not fault §2-A for
leaving N, the citation format or the agreement metric unspecified, because specifying those *is* A's
planning work.

**4. Real joint or arbitrary cut — a real joint.** Set out in Part 2 of the verdict above. The decisive test
for me: the boundary is named by the task statement itself (`P5`) before any divider looked at it, and the
divider's framing — *"P5 is not a feature sitting on one side of this line — P5 is the assertion that the
line exists and is not crossed"* — is correct. The rejected alternative (method vs. envelope) is recorded
with a reason that holds: an envelope half is derivative documentation of a method it does not own, and
nothing about the method changes at that line. I could not construct a better cut. Moving the run driver
below the boundary would put a role that must traverse the whole tree inside the half that is scoped to one
item; moving the entry surface above A would make A's own mechanism documented by an agent that cannot see
it.

---

## The six lenses

**1. Factual — one finding (F8, nitpick); otherwise clean, earned by citation.** I checked every external
citation in the document against its source. Correct: `Guarded_change/SKILL.md:27` (`changes/<slug>/`);
`Guarded_change/SKILL.md:28` (*"Step numbers below are the canonical stage numbers used everywhere"* — round
2's misattribution to Dragonfly is genuinely fixed, and the same convention does independently appear in
`Dragonfly/SKILL.md` at the equivalent line); `Dragonfly/SKILL.md:31` (`hunts/<slug>/`, cited as a documented
convention and not as an on-disk directory — round 2's A-F14 is genuinely fixed; `Dragonfly/` on disk
contains `changes/`, not `hunts/`); `Dragonfly/METHODOLOGY.md:143` (*"One folder per hunt, e.g.
`hunts/<slug>/`"*, under `## What a run produces (artifacts)`); `Guarded_change/METHODOLOGY.md:139`
(*"Paths are validated, not assumed"*); `Dragonfly/SKILL.md:19` (*"Validate config paths at hunt start"*,
wrapping to line 20); `Dragonfly/stages/charter.md:1` (*"# The red-team charter (shared by stages 1, 4, 7)"*
— §3.7's characterisation as a charter read at *specific* stages is exactly right);
`Architect/stages/common.md:3`; `Architect/stages/leaf.md:47` (*"You do not file findings — your output is a
plan, and severities are for reviewers"* — §3.9's premise holds); and both `combiner.md` quotes.
Also verified as existing: every precedent file §2-A and §2-B point their planners at
(`Guarded_change/stages/charter.md`, `stage-3.md`, `Dragonfly/stages/charter.md`, `stage-7.md`,
`Dragonfly/METHODOLOGY.md`'s seven claimed sections, both `*.companion.md` files, both `README.md` files).
§3.7's claim that **neither sibling has a `common.md`** is true — both have `stages/charter.md` and no
`common.md` — and the universal-preamble pattern being Architect's own is also true.

**2. Logical — F1, F2, F4.** All three are internal contradictions or gaps in the seam's own state machine
and output rules, independent of any source. The rest of the sequencing holds: §3.5's termination argument
(*"each node is either terminal or has a strictly increasing `RUN` bounded by `run.max_attempts`"*) is valid
*given* F1 and F2 fixed, and the presence rule (§3.2, write-to-`.tmp`-then-rename with exactly two named
exemptions) is a coherent basis for resume.

**3. Missed opportunity — F7, plus one observation.** The observation: §3.5's cross-half invariant
`sizing.max_item_bytes ≤ analysis.max_item_bytes` is documented in `METHODOLOGY.md` but never *checked* at
run time by anyone. B's decomposer reads the config and is the natural place to assert it and stop; the seam
could say so in one clause and convert a documentation promise into a mechanism. I have not filed this as a
separate finding because §2-A's fallback (A writes `state=failed` on an over-size item) makes the
consequence bounded rather than silent — but it is a cheap improvement left on the table.

**4. Unstated assumptions & risks — F3, F5, F9.** The load-bearing unstated assumption is F3's: the entire
document assumes an actor that concatenates §3 onto each sub-task and re-emits it at every level of descent,
and that actor is not in any charter. Secondary: F5 (decomposition covers the corpus), and the assumption
that `run.max_attempts` counting *dispatches* rather than *failures* is the right meter — a leaf that makes
real progress on each of three partial passes is capped identically to one that fails three times, which
§3.5 does not acknowledge.

**5. Fidelity — clean, earned by pinning each loaded term.** I pinned every operational term in the eight
properties to the concrete mechanism the seam gives it, and checked that the mechanism implements the term
rather than proxying it:
- *"decompose and size"* → §3.3's `item.json` with a validated `locator` (`{path, lines}`, inclusive
  1-based) and `size_bytes`; §3.5's recursive split along config-named structural boundaries. A mechanism.
- *"strategy for over-size items"* → §3.5, decomposition-time recursive resplit bounded by
  `sizing.max_resplits`. This is the round-3 change and it is the right call: the task's phrasing sits inside
  the decompose-and-size clause, so a decomposition-time mechanism is the faithful reading, not a convenient
  one.
- *"N independent cold analysts"* → `common.md` rule 1 (cold = no shared context with caller or siblings)
  plus §2-A's requirement that A specify enforcement *at its entry agent's dispatch point*. Named as a
  required mechanism, not an exhortation.
- *"read-only"* → `common.md` rule 3, plus §3.2's read-permission table which enumerates per role what may
  be read and written. Structural.
- *"citing every finding"* → `common.md` rule 4 states the duty; §2-A owns the format. Split correctly.
- *"cold verification pass that drops unverifiable citations"* → §2-A P3: a **separate cold agent, never the
  analyst that produced the finding**, with the drop count surfaced as `n_dropped` in §3.4. The
  never-the-producer clause is what makes this the mechanism rather than a proxy.
- *"agreement-ranked merge"* → §2-A P4 plus `max_agreement` as a defined integer over analyst counts, with
  the empty case pinned to `0` in §3.4.
- *"blind roll-up… reads only a terse per-child status"* → §3.2's read-table row restricting the coordinator
  to *"the `STATUS` lines of its own children, and nothing else"*, plus §3.4's five fields and the
  **deliberate absence of any path field**. This is the strongest fidelity result in the document: blindness
  is enforced by there being nothing to peek *at*, not by telling an agent not to peek.
- *"per-corpus Layer-2 config"* → §3.6, one file, partitioned namespaces, contract section, worked example.
- *"restart and resume from on-disk state"* → §3.2's presence rule plus `RUN` plus `STATUS`-absence as the
  only *"not yet"* marker. A real mechanism — F1 and F2 are defects *in* it, not evidence that it is a proxy.
- *"facts, not interpretation"* → `common.md` rule 7 states it; §2-A requires it be written into role prompts
  *"as an **enforceable rule** rather than an exhortation"*. This is the term I judged closest to a proxy,
  because the seam gives no test for what counts as enforceable — but specifying it is A's planning work
  above the floor, so I have not filed it.

**6. Completeness — F1, F2, F3, F4, F6; generative sweep run.** Checklist first: §3 covers layout,
ownership, run-directory skeleton, presence rule, read permissions, item record, invocation contract, status
schema, control loop, config, shared agent core, corpus-level output, objection path, exclusions and the
floor. Then the sweep — *"what load-bearing section does that list not anticipate?"* I looked for: **an
output location** (found: `<run.dir>/findings.md`, §3.8 — present, but incomplete per F4); **a restart
story** (present, §3.2/§3.5 — but broken per F1/F2); **a failure mode for every state in §3.4's domain**
(this is where F1 and F2 came from); **the seam's own delivery and propagation mechanism** (absent — F3, and
this is the item the checklist most conspicuously does not anticipate, because a seam document naturally
audits its *content* and not its *transport*); **a coverage guarantee for the decomposition** (absent — F5);
**house-style completeness of the entry surface against the siblings** (F6); **concurrency semantics for
`decisions.md` appends and parallel leaf dispatch** (present — §3.2's `O_APPEND` one-complete-line-at-a-time
exemption plus §2-B's *"bounds concurrency"*; adequate); **what happens to the run when the human is stopped
for** (present in outline via `decisions.md` and the escalation, adequate at this level); **who creates the
build root directory** (not stated, but below the floor to file); and **the ordering dependency between the
two halves' plan steps after `Union`** (checked and found to be a non-issue: every inventory-dependent step
is written as a rule evaluated against the merged plan, so no step needs to run before another half's step
exists).

---

## Note on §7

I treated §7's disposition table as claims. I spot-verified the three round-2 items whose fixes are
externally checkable and all three hold: the misattributed `Guarded_change/SKILL.md:28` quote, the
`Dragonfly/hunts/` path-vs-convention correction, and the softened frontmatter-`name` claim. I did not
assume anything §7 omits is sound — F1, F2, F3, F4, F5, F6, F7 and F9 are all findings against the round-3
text as it stands, and F2 in particular is the round-2 *"nobody produces this state"* defect recurring on a
different state after the state it was originally filed against was deleted.
