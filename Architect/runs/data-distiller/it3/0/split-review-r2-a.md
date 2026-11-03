# Split review — round 2, reviewer A

Cold, independent review of the **proposed division** in `split-round-2.md`. I hold no plan and was
given none.

**Hard fence, stated as required:** I did **not** open, read, list, grep, glob or otherwise access
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did **not**
invoke the installed `data-distiller` skill. I also did not open any `split-review-*.md`. I did read
`split-round-2.md` (in full), the Architect stage files (`common.md`, `redteam.md`,
`redteam-split.md`, `divider.md`, `node.md`, `combiner.md`, `leaf.md`), and the sibling skills
`Guarded_change/` and `Dragonfly/`. I did **not** read `split-round-1.md`; I reviewed round 2 on its
own merits and treated §7's "fixed at" column as a claim, not as evidence.

---

## VERDICT — the two parts

**Part 1 — what I found.** Six `major`, six `minor`, two `nitpick`. Every one of them is a defect in
the **seam text (§3)**, which is the divider's own output. None of them is a defect in the choice of
joint. Four of the six majors are the same shape: **the seam fixes a *signature* or an *invariant*
but not the *name* or the *transition* that a blind half actually needs**, and both halves will fill
the gap plausibly and incompatibly.

**Part 2 — do I object to going forward with this cut? No. I do not object.**
The joint is real, it is the boundary the task statement itself names (P5), coverage of P1–P8 is
complete with each property owned exactly once, and neither half falls below the floor. **I endorse
this cut.** My findings travel down with the sub-tasks, or are fixed in §3 before dispatch; they are
not a reason to re-derive the joint. I explicitly do not want a third round spent moving the
boundary.

---

## The four questions, answered directly

**1. Coverage — do the halves cover the whole task?** Yes. P1–P8 each have exactly one owner, the
three properties that straddle (P6, P7, P8) are split along a stated line rather than left joint, and
the three non-property remainders (the run driver, the corpus-level output, the entry surface) each
carry an ownership line inside §3 rather than only in the §4 audit table. I found **no orphaned
remainder among the eight properties** and **no portion both halves assume the other owns**. The gaps
I did find (findings 1, 4, 5) are not unowned *work* — they are owned work whose cross-half *name* or
*trigger* was never written down.

**2. The seam — stated, sound, self-contained?** Stated: yes, extensively and identically to both
halves, with a real transport mechanism (§6: prepended verbatim, plus an absolute path, plus
propagation to descendants). Sound: mostly, with the control-loop exceptions in findings 1–3.
**Self-contained: not fully.** Findings 4 and 5 are genuine residual producer/consumer-at-plan-time
dependencies of the exact form `redteam-split.md` warns about — B is told to invoke and to embed
artifacts of A's whose *names* nothing fixes, while §2-B simultaneously forbids B from guessing them
and does not list those steps among the rule-over-merged-plan steps. §6's claim that "**no element of
this seam has the form 'one half produces X at plan time and the other consumes it'**"
(`split-round-2.md:503`) is **overstated** — it is true of the item record, the STATUS schema, the
config namespaces and the stage numbering, and false of A's pipeline entry point and A's
merged-findings filename.

**3. The floor — would either half fall below it?** No, and this is a clean check. A plans at minimum
three substantial role-prompt files (stages 2–4) plus a format reference; B plans at minimum eight.
Both are whole tasks far above *"one file created or one coherent edit to one file, with the content
that goes in it specified."* The imbalance (B ≈ 2–3× A) is not a floor problem and §5 is right that
evenness is not the test. **No blocker against the division on floor grounds.**

**4. Real joint or arbitrary cut?** **Real.** Something concrete changes at the line, and §1's table
names it correctly: below the line an agent has read corpus content *for meaning* and its output is
*evidence*; above the line no agent has ever seen a finding and its output is *bookkeeping*. The
inputs, outputs, characteristic failures and review criteria are disjoint on the two sides. Round 1's
formulation ("no agent above reads the corpus") was false and the round-2 restatement to the
**finding** boundary is the correct repair — B's decomposer demonstrably must open corpus files, and
§2-B now says so in its own words (`split-round-2.md:148-150`). Critically, **P5 is not a feature
sitting on one side of this line — it is the assertion that the line exists**, so the interface was
fixed by the owner's task statement before any divider looked at it. That is the opposite of an
arbitrary bisection. The rejected alternative (method vs. envelope) is correctly characterised as a
packaging boundary; recording it was right, since no later reviewer sees it.

One honest qualification, filed as `minor` (F10 below): **B is not a single coherent design half.**
It is "everything above the finding boundary" (decomposition, driver, roll-up) *plus* the
documentation envelope (`SKILL.md`, `METHODOLOGY.md`, `README.md`, the worked config). The blindness
criterion classifies the docs correctly — trivially, since no agent and no finding is involved — but
it does not *motivate* putting them there. This weakens the joint for B without invalidating it, and
it is why B remains obviously divisible one level down.

---

## The six lenses

### Lens 1 — Factual: **findings, but the sourcing is largely sound**

I checked every external citation in §1–§3 that a half will act on. Verified correct:

- `Dragonfly/SKILL.md:34` — *"Step numbers below are the canonical stage numbers used everywhere"* —
  quoted accurately (§3.1 elides the parenthetical `(METHODOLOGY, decisions.md)`; fair).
- `Dragonfly/SKILL.md:20` — *"Validate config paths at hunt start"* ✔ (§3.3).
- `Guarded_change/METHODOLOGY.md:139` — *"Paths are validated, not assumed"* ✔ (§3.3).
- `Architect/stages/combiner.md:6` — *"None of the three is an author…"* and `combiner.md:58` — *"A
  genuine conflict is kept, not resolved"* ✔ (§3.9, §6).
- `Architect/stages/node.md:101-108` — loop steps 3–4, red-team then `Severity` → next task ✔ (§3.9).
- §3.7's precedent claim: **neither sibling has a `common.md`; both have `stages/charter.md`** ✔
  (directory listings). `Architect/stages/common.md` exists and is a universal preamble ✔. The
  declared divergence is honest and correctly attributed.
- §3.1's letter-suffix claim ✔ (`Dragonfly/stages/stage-0a.md`, `stage-0b.md`;
  `Guarded_change/stages/stage-1.5.md`).
- §2-B's `METHODOLOGY.md` section list ✔ — `Dragonfly/METHODOLOGY.md` headings are exactly
  why-it-exists / the loop / stage index / the two layers / the config contract / what a run produces
  / human-in-the-loop.
- §2-B's `SKILL.md` claim (frontmatter + router table + `Stop-for-human`) ✔ against both siblings.
- §3.6's config format claim ✔ — both companion files are a YAML block inside markdown.
- §2-A's named precedents all exist: `Guarded_change/stages/charter.md`, `stage-3.md`,
  `Dragonfly/stages/charter.md`, `stage-7.md` ✔.
- §6's reported contradiction between `divider.md:79-83` (offering `Union` as a legitimate home for a
  cross-half dependency) and `combiner.md:6,58` (forbidding `Union` to author or adjudicate) is
  **real**; I confirm it independently, and the decision not to rely on `Union` is correct.

Factual defect: **F14** below (`Dragonfly/hunts/`).

### Lens 2 — Logical: **findings F2, F3, F6**

The control loop of §3.5 is where the reasoning breaks, and F6 is a routing contradiction with a role
file the halves' own planners will read.

### Lens 3 — Missed opportunity: **one, folded into F4/F5**

The seam went to great length to fix value *domains* (`locator` unit, `size_bytes`, `tier` opacity,
integer types, id charsets) and then did not spend the two lines that would fix the two *filenames*
that actually cross the boundary at build time. Fixing "A's pipeline entry point is
`stages/stage-2.md`" and "A's per-item merged-findings file is named `<X>` under the node directory"
in §3.3/§3.2 costs nothing and closes both F4 and F5 outright. That is a cheaper repair than any
rule-over-merged-plan wording.

### Lens 4 — Unstated assumptions & risks: **findings F1, F9, F12**

The load-bearing unstated assumption is **that A can tell an item is over-size.** The whole §3.5
`oversize` loop — round 2's headline repair — rests on it, and nothing gives A the criterion.

### Lens 5 — Fidelity: **clean, earned by pinning**

Each loaded operational term, pinned to the concrete mechanism the division assigns it:

| Term | Pinned to |
|---|---|
| **cold** | §3.7 rule 1 — no shared context with caller or siblings; enforcement at dispatch is A's (§2-A) |
| **independent** (P2) | A's dispatch-point mechanism: no shared context, no visibility of a sibling's output (§2-A) |
| **read-only** | §3.7 rule 3 — writes nothing but the role's named outputs, via `.tmp`-then-rename |
| **decompose** (P1) | B's stage-0 role producing `index.md` + `item.json` records, with `locator` validated at write time (§3.3) |
| **verify** (P3) | a separate cold agent, never the analyst that produced the finding; operational definition of "unverifiable" is A's (§2-A) |
| **agreement-ranked merge** (P4) | A's matching + rank rule; surfaces upward only as the integer `max_agreement` (§3.4) |
| **blind roll-up** (P5) | §3.2 read table + §3.4 — the coordinator's *entire* input is one five-field line per child; the `findings_path` field was removed precisely so blindness is structural rather than exhortative |
| **terse per-child status** | five whitespace-separated typed fields, §3.4 |
| **restart/resume** (P7) | §3.2 presence rule (write-complete-or-not-at-all) + §3.5 `state` dispatch table |
| **facts, not interpretation** (P8) | §3.7 rule 7 states the duty; A owns the enforceable-rule form in the analyst/verify/merge prompts |
| **Layer-2 config** (P6) | one YAML-in-markdown file, namespaces partitioned §3.6 |

**This division implements the mechanisms, not proxies for them.** The strongest evidence is §3.4's
deliberate removal of `findings_path`: the seam gave up a convenience so that blindness would be a
property of the interface rather than a rule an agent is asked to obey. Note also that A's own
intra-item pipeline is *below* the line, so an unblinded A-side sequencer is correct rather than a
fidelity breach — and §3.7's parenthetical (A's merge role names two outputs) keeps the counting that
produces `n_findings`/`n_dropped`/`max_agreement` on the correct side of the boundary. **Clean.**

### Lens 6 — Completeness: **findings F1–F5, F7–F13; generative sweep was run**

Structural checklist (does the seam state ownership, layout, invocation, status vocabulary, resume,
config, escape hatch, floor, out-of-scope, transport?): all present.

**Generative sweep — what load-bearing section does that checklist not anticipate?** I looked
specifically for: (a) the *reverse* direction of every stated one-way interface — B→A is fixed by
§3.3, A→B by §3.4, but **A→B at build time** (names, not values) is nowhere, → F4, F5; (b) every
*state transition* the state table implies but does not license, → F2; (c) every loop in §3.5 without
a bound, → F3; (d) the *detection* half of every strategy whose *response* is owned, → F1; (e) the
fate of a finding filed through the escape hatch, → F6; (f) degenerate inputs (zero items, zero
children), → F12; (g) whether the §3.1 layout, unlike §3.2's skeleton, was ever declared exhaustive,
→ F11.

---

## Findings

### F1 — `oversize` detection is A's duty, but A is given no criterion and is barred from the namespace that holds one — `major`

§3.4 puts `oversize` in the **leaf** state domain, and §3.5 explains why: *"`oversize` exists because
B sizes an item from its shape and A discovers at read time that it does not fit"*
(`split-round-2.md:370-371`). A writes the leaf `STATUS` (§2-A, `split-round-2.md:111`), so **A is the
agent that must decide an item is over-size.** But §2-A's "You do not own" list explicitly includes
*"the over-size strategy"* (`split-round-2.md:138`), and §3.6 partitions `sizing.*` to B with the rule
*"Neither half reads or defaults a key in the other's namespace"* (`split-round-2.md:381-382`). A is
therefore told to emit a state whose trigger condition it is told it does not own and whose natural
configuration key it may not read. `size_bytes` is in the item record but no threshold is.

**Failure scenario:** A plans "an analyst emits `oversize` when the item does not fit its context" and
declares an `analysis.max_item_bytes` key with its own default. B plans `sizing.max_item_bytes` and a
decomposer that never produces an item above it, and writes the re-split loop assuming `oversize` is
rare. The merged plan has two independent size thresholds in two namespaces, both defaulted, neither
aware of the other; if A's is the larger, `oversize` never fires and the §3.5 loop — round 2's
headline repair — is dead code. Both halves look locally correct.

**Remedy, in the seam:** one line in §3.3 or §3.6 — either name the single key that governs and
carve it out of the partition the way `run.dir` is carved out (§3.6, `split-round-2.md:387-388`), or
state the operational trigger ("A emits `oversize` when an analyst cannot read the item's `locator`
range in one pass") and say which half defaults it.

### F2 — the `oversize` → re-decompose transition requires two operations the seam's own invariants forbid — `major`

§3.5 row 4: *"re-decompose. B's over-size strategy runs on that item and emits child nodes with
`parent_node_id` set; **the node becomes a group**"* (`split-round-2.md:368`). Three seam invariants
stand in the way, and none of them is relaxed:

1. §3.2: *"`item.json` — present **IFF** this node is a LEAF"* and *"A node is a LEAF — an item — if
   and only if it has `item.json`; otherwise it is a GROUP"* (`split-round-2.md:274,281-282`). Turning
   the node into a group therefore requires **deleting `item.json`**. Nothing in the seam authorises
   deletion of anything, and §3.2 is declared exhaustive as to what may exist.
2. §3.2's presence rule: *"Every file above is written complete or not at all… the existence of a file
   means the step that produces it finished"* (`split-round-2.md:288-289`). The node's `STATUS`
   already exists and says `oversize`; it must now be **rewritten** to a group state
   (`done|partial|failed`, since `oversize` is leaf-only per §3.4). The presence rule reads as
   write-once — it is the entire basis of P7 resume — and no clause distinguishes "rewritten" from
   "not yet written".
3. §3.4: *"A not-yet-run node has no `STATUS` file at all. **Absence is the only 'not yet' marker**"*
   (`split-round-2.md:341`). A node mid-re-decomposition is neither absent nor in a legal group state.

**Failure scenario:** B plans the re-split to delete `item.json` and truncate `STATUS`; a red-team
round below the cut correctly files it as a violation of the inherited seam; §3.9 forbids B to fix the
seam locally, so the finding cannot be cleared by the half that received it. Alternatively B plans
conservatively — leaves `item.json` in place — and every later pass reads the node as a leaf whose
`STATUS` is `oversize` and re-decomposes it again, until `sizing.max_resplits` escalates a node that
was in fact successfully split. Note also that A's partial per-item outputs written before it
discovered the item was over-size now sit under a *group* directory, which §3.2's skeleton does not
contemplate.

**Remedy, in the seam:** §3.5 states the transition explicitly as a licensed exception — the order of
operations, that `item.json` is removed (or that a `group` marker supersedes it), and that a node's
`STATUS` may be replaced exactly once on this path.

### F3 — the `partial`/`failed` re-run has no bound; only `oversize` got one — `major`

§3.5 row 3: *"`state=partial` or `state=failed` → **re-run the node**"* (`split-round-2.md:367`), with
no cap, no attempt counter and no escalation. Row 4 gives `oversize` a bound
(`sizing.max_resplits` → escalate to the human), which shows the divider knew loops need bounds and
bounded only one of the two.

**Failure scenario:** an item whose `locator` path became unreadable after decomposition (permissions
change, a log rotated away). A's pipeline runs, fails deterministically, writes `state=failed`. The
driver observes `failed` and re-runs. Forever, at whatever concurrency the driver allows. Nothing in
§3.5 stops it and neither half can add a bound without either amending the seam (forbidden, §3.9) or
inventing an attempt counter — for which the exhaustive skeleton of §3.2 provides no file (see F9).

**Remedy:** give row 3 the same shape as row 4 — a config-keyed retry bound in `run.*` or `sizing.*`,
then escalate and leave `failed`.

### F4 — B's run driver must name A's pipeline entry point, which nothing fixes and B is forbidden to guess — `major`

§3.3 fixes the **invocation signature**: *"B's run driver invokes A's pipeline with exactly two
arguments: `item_dir` and `config_path`"* (`split-round-2.md:324-326`). It does not fix the
**target**. B must write a driver *prompt* — at plan time, blind — that says what to dispatch. §2-B
forbids exactly this: *"**Do not guess the other half's filenames, stage numbers, purposes or config
keys.**"* (`split-round-2.md:188`). And §2-B's enumeration of steps that may be written as rules over
the merged plan — router table, stage index, config contract, worked example, `Stop-for-human`,
`findings.md` (`split-round-2.md:183-186`) — **does not include the driver.** §3.1's range partition
(A owns 2–4) gets close but is explicitly non-binding on which numbers A uses: *"need not use every
number"* (`split-round-2.md:246`).

This is the residual producer/consumer dependency `redteam-split.md` warns about, at the one point
where the two halves actually meet at run time. It is recoverable at build time only because a
practitioner holding the merged plan can look A's entry point up — but B's *plan text* will contain
either a guess or a dangling reference, and §6's blanket claim that no such element exists
(`split-round-2.md:503-504`) is false here.

**Remedy:** one sentence in §3.1 or §3.3 — *"A's pipeline entry point is `stages/stage-2.md`"* — or
add the driver step to §2-B's rule-over-merged-plan list with the rule stated.

### F5 — A's merged-findings filename is consumed by two B artifacts, and no clause obliges A to declare it — `major`

§3.4 asserts the human-facing pointer *"is derivable (`nodes/<node_id>/` + **A's declared
merged-findings filename**)"* and *"is recorded once in `index.md` and in `findings.md`"*
(`split-round-2.md:345-347`). §3.8's assembly rule likewise says *"each embedding **that node's merged
findings file** verbatim"* (`split-round-2.md:420-421`). Both presuppose a declaration that the seam
never creates:

- §3.1's three-field obligation is scoped to plan-created source files — *"**Every plan step that
  creates a file** declares the filename, the stage number / pipeline position, and a one-line
  purpose"* (`split-round-2.md:252-254`). A's per-item outputs are **run-time artifacts written by
  agents**, not files any plan step creates; they have no stage number and no pipeline position, so
  the obligation does not reach them.
- §2-A gives A *"the **internal formats** of every file you write under a leaf node directory"*
  (`split-round-2.md:105-106`) — formats, not names.
- §3.2's skeleton names the category only: `<A's per-item outputs>` (`split-round-2.md:276`).

The `index.md` case is the sharper of the two: `index.md` is written **at run time by B's decomposer**,
whose prompt B authors blind, so the filename must appear in B's prompt text — and §2-B's
rule-over-merged-plan list does not include `index.md` either.

**Failure scenario:** A names it `merged-findings.md`; B's `findings.md` assembly step and B's
decomposer prompt both say `findings.md` (the obvious guess, and colliding with the corpus-level
name). Neither plan is internally wrong; the assembled skill emits an empty `findings.md` — the
artifact §3.8 calls *"the artifact the method exists to emit"*.

**Remedy:** fix the filename in §3.2's skeleton, or extend the §3.1 declaration obligation explicitly
to run-time outputs under a node directory.

### F6 — §3.9's escape hatch instructs the halves' planners to do what `leaf.md` forbids, and routes into a loop that cannot clear it — `major`

§3.9: *"**File it as a `blocker`/`major` finding in your own plan output.**… It surfaces at the node's
plan red-team round, and `Severity` turns it into the next task"* (`split-round-2.md:425-429`). Two
problems, both checkable against the Architect role files the halves' agents actually run under:

1. **`leaf.md:47` states: "You do not file findings — your output is a plan, and severities are for
   reviewers."** The seam therefore instructs the one role that writes plan content to violate its own
   charter. A compliant leaf will not file the finding at all.
2. Even if a leaf does write it, three leaves are merged by `Consensus`, which is *"2-of-3 on numbered
   steps, INCLUDING ORDER. **The odd plan is discarded.**"* (`combiner.md:22`). A seam objection is not
   a numbered step and, written by one of three cold leaves, has no second endorser — it is discarded
   silently.
3. Where it *does* survive (the node path, via `Union`), `Severity` makes it *"the next task"*
   (`node.md:108`) for a node **that may not change the seam** (§3.9 forbids local adjustment, and the
   seam came from the parent's divider). The child re-plans, cannot clear the finding, and the finding
   returns unchanged next iteration — `combiner.md:80-83` describes exactly this non-termination mode
   for anything handed to a planner that cannot fix it.

**Failure scenario:** A's planner notices F1 (no `oversize` criterion), follows §3.9, and the objection
either never gets written (leaf.md), gets voted away (Consensus), or pins the child node in a loop it
cannot exit. The seam's only defect-reporting channel does not reach anyone able to act.

**Remedy:** route seam objections to the **node that owns the division** — i.e. state in §3.9 that the
finding is written into the plan output as a clearly marked *seam objection* addressed to the parent
node, and that the parent's red-team round (not the child's) is where it is adjudicated. This finding
travels down with **both** sub-tasks.

### F7 — a group's non-`done` state is undefined — `minor`

§3.4 fixes only the positive case: *"`state` is `done` only if every child is `done`"*
(`split-round-2.md:354`). When some child is `partial` and another `failed`, whether the group is
`partial` or `failed` is unstated. B owns both the roll-up prompt and the driver, so this costs no
cross-half agreement and is fixable in place — hence `minor`, not `major`. It matters only because
§3.5 dispatches on the group's own `state`.

### F8 — a leaf's `partial`/`failed` has no trigger, and the three integers have no meaning in those states — `minor`

A writes `STATUS` *"as the last act of its pipeline"* (§2-A, `split-round-2.md:111`), so a crashed
pipeline writes nothing and is covered by absence. It is therefore unstated what a *completed* A
pipeline observes that makes it write `partial` or `failed` rather than `done`, and what
`n_findings`/`n_dropped`/`max_agreement` mean when it does (zero? partial counts? the fields are typed
non-negative integers with no null). The roll-up sums them regardless of child state
(`split-round-2.md:353-354`), so a `failed` child's placeholder integers propagate into the corpus-level
totals.

### F9 — the exhaustive skeleton leaves no in-progress marker, and neither half may add one — `minor`

§3.2 declares the skeleton *"EXHAUSTIVE. Neither half may add a file or directory to it."*
(`split-round-2.md:266`) and §3.4 makes absence of `STATUS` *"the only 'not yet' marker"*
(`split-round-2.md:341`). Together these make "never started", "in flight right now" and "died
mid-pipeline" indistinguishable, and foreclose the standard remedies (a lock file, an attempt
counter — see F3). This is benign under the design the seam evidently intends (one driver process,
restart only after death) and I am not claiming it breaks that design; the finding is that the seam
**forecloses the remedy without stating the assumption that makes it unnecessary**, and §3.9 bars B
from adding one if it turns out to be needed. State the single-driver assumption in §3.2.

### F10 — B is not a single coherent design half — `minor`

§1 rejects the method/envelope alternative because *"the envelope half is derivative documentation of
a method it does not own"* (`split-round-2.md:70-71`), yet B as constituted **is** that envelope
(`SKILL.md`, `METHODOLOGY.md`, `README.md`, the worked config) bolted onto a genuine design half
(decomposition, driver, roll-up). The finding-blindness criterion classifies the docs onto B's side
correctly but only trivially — no agent, no finding — so it does not *motivate* the placement. This is
not an objection: the placement is right on other grounds (the docs are inventory-dependent and B owns
the inventory rules), and B remains divisible one level down. It is recorded because §1's argument for
the joint is weaker for B's half than §1 claims.

### F11 — §3.1's layout is never declared exhaustive or illustrative, unlike §3.2's skeleton — `minor`

§3.2's skeleton was explicitly declared exhaustive; §3.1's layout was not, and it is the one that
governs the built skill. This is load-bearing because §2-A licenses A to plan *"any format-reference
file they need"* (`split-round-2.md:119`) and §3.1's layout has no slot for a non-stage file. If A
puts it under `stages/`, B's inventory rules capture it as a role-prompt file it is not (*"one row per
role-prompt file under `stages/`"*, `split-round-2.md:187-188`), and it lands in the router table.
If A puts it elsewhere, B's rules miss it entirely. Declare §3.1 exhaustive-or-illustrative, and say
where a non-stage reference file goes.

### F12 — degenerate corpora are unowned — `minor`

Zero items (an empty or fully-filtered corpus) and a group with zero children have no owner and no
defined `STATUS`. §3.5's table has no row for "decomposition produced nothing", and §3.8's assembly
rule (*"one section per leaf node"*) silently produces an empty `findings.md` indistinguishable from
the F5 failure.

### F13 — §2-B's `Stop-for-human` instruction is not executable as literally written — `minor`

§2-B lists `Stop-for-human` among steps that must be *"written as a rule over the merged plan"*
(`split-round-2.md:183-186`). The merged plan's declared fields are filename, stage number, purpose
(§3.1) and config keys (§3.6) — **none of which carries stop-conditions**, so there is no inventory to
write a rule over. In practice B can write the section from the seam alone (missing config, dead
locators §3.3, `sizing.max_resplits` escalation §3.5), all of which are B's; the defect is that the
instruction as given points at data that does not exist. Say instead that B writes it from the seam's
own escalation points.

### F14 — `Dragonfly/hunts/` is cited as a precedent path and does not exist on disk — `nitpick`

§3.2 justifies the `run.dir` default with *"the siblings, which keep run artifacts inside the skill
directory (`Guarded_change/changes/`, `Dragonfly/hunts/`)"* (`split-round-2.md:263-264`).
`Guarded_change/changes/` exists. **`Dragonfly/hunts/` does not** — Dragonfly's on-disk run directory
is `Dragonfly/changes/`, while `hunts/<slug>/` is the name its own documentation uses
(`Dragonfly/SKILL.md:31`, `Dragonfly/METHODOLOGY.md:143`, `Dragonfly/dragonfly.companion.md:34`). The
substantive claim — siblings keep run artifacts inside the skill directory — survives either way; the
citation is to a documented convention, not to a path.

### F15 — the roll-up coordinator's read permission is stated too tightly to write its own output — `nitpick`

§3.2: the coordinator may read *"the `STATUS` lines of its own children, **and nothing else**"*
(`split-round-2.md:299`), yet §3.4 requires it to write *its own node's* `STATUS`, which needs its own
`node_id` and output path. These arrive as arguments rather than reads, so there is no real conflict —
but the absolutism is what makes the row valuable, and a half-sentence (*"its own node_id and output
path are passed as arguments"*) preserves it without the apparent contradiction.

---

## Lens verdicts, summarised

| Lens | Verdict |
|---|---|
| 1. Factual | **Findings** — F14. Otherwise clean and earned: every quoted source above was opened and checked; the `divider.md` ↔ `combiner.md` contradiction §6 reports is confirmed independently. |
| 2. Logical | **Findings** — F2, F3, F6. |
| 3. Missed opportunity | **One**, folded into F4/F5: two fixed filenames in the seam would close both, more cheaply than any rule-over-merged-plan wording. |
| 4. Unstated assumptions & risks | **Findings** — F1, F9, F12. |
| 5. Fidelity | **Clean, earned** — eleven loaded terms pinned to concrete mechanisms in the table above; the removal of `findings_path` is the decisive evidence that P5 is implemented structurally rather than as an exhortation. |
| 6. Completeness | **Findings** — F1–F5, F7–F13. Generative sweep run; the seven things it looked for are enumerated above. |

**Any portion of the task left unaddressed?** No portion of the *task* is unaddressed by the division.
The house-style-check instruction is assigned to both halves for their own files and both are pointed
at the correct precedent files (verified). The off-limits directive is propagated verbatim into both
sub-tasks.

---

## Restatement of the verdict

**I endorse this cut and do not object to going forward.** The joint is the one the task statement
itself names; something real changes at it; coverage is complete; neither half falls below the floor.
Six `major`s stand — all of them defects in §3's text, five of them fixable by adding one or two
sentences to the seam before dispatch, and all of them of the kind that travel down with the
sub-tasks. **None of them is a reason to move the boundary.** If they are carried rather than fixed,
carry **F1, F2, F3, F5, F9, F11, F12, F13** with sub-task B, **F1, F5, F11** with sub-task A, and
**F4** and **F6** with **both**.
