# Split review — round 1, reviewer A

Reviewing the proposed division in
`Architect/runs/data-distiller/it2/0/split-round-1.md` (the "cut along the blind-roll-up line").

**Inputs I had:** the proposed division + the task + the floor (all in `split-round-1.md`), and the
source material `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/`. **There is no plan and I did not look for one.**
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` was not read, listed or grepped.

**Unchecked, declared:** I cannot check the division against the finished implementation (off
limits, correctly). Every "who owns X" finding below is derived from the division's own text plus
the task text; where the division is silent I say *unowned*, not *wrong*.

Line references of the form `:NN` are into `split-round-1.md` unless another file is named.

---

## Findings

### BLOCKER 1 — Nothing in either half produces the run's actual deliverable

**Lens: completeness / coverage.**

The task's purpose is "extracting trustworthy, source-cited factual findings from a corpus"
(`:14–15`). Trace where a finding can end up under this division:

- A's outputs are exactly two, enumerated at `:71–73`: "the per-item findings artifact" and "the
  terse per-item status line."
- B's coordinating agent "reads only terse per-child status, never the findings, and rolls child
  statuses upward" (`:94–96`), and B's out-of-scope explicitly excludes "the findings-artifact
  format" (`:110–111`).
- Seam 2 (`:123–131`) makes reading the findings artifact prohibited to B outright: "**B reading the
  findings artifact is the one thing that would void the blind-roll-up property.**"

So the run terminates with N per-item findings files on disk and a tree of status lines above them,
and **no half plans the stage that assembles a corpus-level result.** A cannot (it is scoped to
"what happens to ONE analyzable item", `:55–57`, and is out-of-scope for "the tree of coordinating
agents"). B is forbidden. This is an orphaned remainder of the whole task, not a detail.

Note the escape the division did not take: the task's invariant is narrower than the division
assumes — it forbids **a coordinating agent** from reading findings (`:22–24`), not every agent
above the item. A terminal, non-coordinating assembly/roll-up agent is compatible with the stated
invariant. The division closes that door by treating the blind line as total, and then nobody owns
what is behind it.

**Failure scenario:** both halves are planned and built exactly as specified; the skill runs to
completion on a corpus; the user asks "what did it find?" and the answer is "open the 340 per-item
findings files yourself." The defining output of the skill was planned by neither half.

**Remedy direction (not below the floor):** name an owner for the corpus-level output — either a
third seam item assigning a terminal assembly stage, or an explicit statement that the per-item
artifacts *are* the deliverable and that B's `METHODOLOGY.md` "what a run produces" says so.

---

### BLOCKER 2 — Sizing and the over-size strategy are placed in A, but their input and their consequence are both B's

**Lens: coverage / logical.**

A's first in-scope bullet (`:60–62`) gives A "**Sizing and per-item strategy.** How an item's size
is measured against a context budget, and the rule that picks a strategy when the item does not
fit." Two things break against that.

**(a) Double ownership of the size measure.** Seam 1 (`:121–126`) has B's decomposition emit a
handle containing "an identifier, a locator into the corpus, and **a size measure**", and says A
"needs at least the locator and the size measure, and B must supply them." So B *produces* the size
measure while A *defines how size is measured*. Nothing in the seam says whether B implements A's
measurement rule (a cross-seam content dependency the seam does not list as a channel) or whether B
measures by its own rule and A's sizing rule is dead text. Both planners can satisfy their own half
and produce incompatible numbers.

**(b) The over-size strategy has no owner for its execution.** The task's bullet is "Decompose the
corpus into analyzable items, size them, **and pick a per-item strategy when an item does not fit**"
(`:16–17`). A owns *picking* the strategy. But for an item that does not fit, the plausible
strategies all reach back across the seam: sub-divide the item (A is forbidden — "A never decides
how the corpus is cut", `:124`), or run more agents over parts of it under the tree (A is
out-of-scope for "the tree of coordinating agents", `:76`, and seam 5 says "A does not schedule",
`:147`). B, meanwhile, is out-of-scope for "the analyst/verifier/merge procedures themselves"
(`:110–111`) and is never told a strategy exists.

**Failure scenario:** decomposition emits an item whose size measure exceeds the budget. A's stage
file says "pick strategy S". S requires creating sub-items and fanning the tree over them. A's plan
may not specify that (B owns the tree); B's plan does not know S exists. The single hardest case —
the one the skill exists for, "a corpus too large to fit in one context window" (`:13`) — falls in
the gap between the halves.

**Remedy direction:** either move sizing + the too-large rule wholly to B's side (it is a property
of how the corpus is cut, and B already emits the size measure), or add a seam item making the
over-size strategy an explicit A→B channel: A names the permitted strategies and their triggering
condition; B owns executing each one.

---

### MAJOR 1 — The cut's founding premise (blind line == item boundary) is asserted, not derived, and conflicts with the task's wording

**Lens: fidelity / unstated assumptions.**

`:171–174` justifies the joint: "Below the line, agents read the corpus and produce findings. Above
it, agents are forbidden the findings and see only status. That is the task's own named invariant."

Pin the term. The task says (`:22–24`): "a **coordinating** agent never reads the findings
themselves, only a terse **per-child** status." The predicate is *coordinating*, not *above the
item*. Under this division, A owns "the *dispatch of the N analysts for this item*" (`:65`) and "the
merge... and emit the item's findings artifact" (`:68–69`). Whatever agent dispatches N children,
collects their outputs and merges them **is a coordinating agent with per-child outputs** — and
under A's scope it reads those children's findings directly. The division therefore places a
coordinating agent on the reading side of its own "blind line" and still calls the line "the task's
own named invariant."

This is the premise the entire cut rests on. If the invariant is meant to hold at *every* level
where an agent has children (analyst-level included), the blind line is not at the item boundary and
this seam is in the wrong place; the merge would then have to be a non-coordinating role and the
per-item dispatcher would be blind too. The division never considers this reading and offers no
argument against it.

**Failure scenario:** the built skill's per-item dispatcher/merger reads all N analysts' raw findings
and steers the merge with its own expectations — precisely the failure the invariant exists to
prevent ("so its expectations cannot steer them", `:24`) — and every downstream reviewer passes it,
because the split doc told them the invariant is satisfied by construction.

---

### MAJOR 2 — The common-to-all-dispatched-agents file spans the seam; as written it is either duplicated or contested

**Lens: completeness / logical. Breaks the division's own seam 7.**

A is given "**Whatever is common to the agents this half dispatches** (analyst, verifier, merger), as
a role-split common file if the sibling skills' shape warrants one" (`:70–71`). But **B dispatches
agents too**: "The prompt file that decomposes a corpus into analyzable items" (`:92–93`) and "The
prompt file(s) for a coordinating agent" (`:94–96`). The material that is genuinely common — cold
and independent, cite-every-claim, read-only over the corpus, where output is written, how a status
line is returned — is common to *all* of them, not to A's three.

The sibling shape confirms the file is a whole-skill artifact, not a half's: `Guarded_change`'s
`stages/charter.md` opens "This is the ONE copy of the red-team charter's common core" and is shared
by stages 3 and 6 (`Guarded_change/stages/charter.md:1–5`, `Guarded_change/SKILL.md:40,43,49–50`);
Dragonfly's is shared by stages 1, 4 and 7 (`Dragonfly/SKILL.md:43,46,49`).

Seam 7 (`:154–159`) requires every file to be planned by exactly one half. Under the division as
written the outcomes are: A writes a common file that B's agents also need (B then either restates
it — the drift the house shape exists to prevent — or silently depends on a file it does not own),
or both halves write one and there are two copies of one core.

**Failure scenario:** A's common file states the read-only-over-the-corpus and cite-every-flag rules;
B's decomposition and node prompts, planned independently, restate them in different words; the two
drift on the first edit, and the "cold, independent" property is defined twice with two different
meanings.

---

### MAJOR 3 — The seam has bidirectional information flow with no ordering rule and no arbiter

**Lens: logical / completeness. This is the seam's soundness, question 2.**

Collect the dependencies the seam itself creates:

| Direction | What must be known first | Cited |
|---|---|---|
| B → A | the item handle's fields | seam 1, `:121–126` |
| A → B | the status schema (fields + permitted values) | seam 3, `:132–138` |
| A → B | the completion markers B must place and resume from | seam 4, `:140–143` |
| A → B | the config keys B's contract must contain | seam 6, `:149–152` |
| A → B | the file list + one-line purposes for B's stage index | seam 7, `:154–159` |

Seam 1 is also internally circular in miniature: "B defines the handle's fields; A declares which of
those fields it needs... and B must supply them."

The division never says whether the two halves are planned sequentially (and in which order),
concurrently against a frozen interface, or iteratively — nor who adjudicates when A's declared
config keys and B's contract disagree, or when A's status schema and B's aggregation disagree. For
two *independent cold* planners this is load-bearing: both cannot go second.

**Failure scenario:** A and B are planned in parallel. A writes its analyst stage assuming a handle
field `byte_range`; B's decomposition emits `offset`+`length`. Neither planner is wrong under its
own brief, no gate compares them, and the mismatch surfaces only at build time — after the split has
been passed and, per the aiming file, is no longer re-opened.

---

### MAJOR 4 — The blindness invariant is *defined* by A and *enforced* by B, with no constraint flowing back

**Lens: unstated assumptions & risks / logical.**

Seam 3 (`:132–138`) gives A the status schema — explicitly "**what a coordinating agent is allowed
to know about an item**" — and gives B the transport and the aggregation. Seam 2 (`:128–131`)
obliges *B* to state the prohibition on reading findings. The rule against widening the channel is
written one-directionally: "if **B** needs a fact about an item that the status schema does not
carry, that is a change to A's schema."

Nothing constrains A. A can specify a status schema with a `summary` field, a `top_findings` list, or
a free-text `notes` field and be fully compliant with its brief, and B — which authors and enforces
the blindness rule — has no stated authority to refuse it. The word "terse" appears (`:72–73`,
`:96`) but as a description, not as a checkable constraint with an owner.

**Failure scenario:** A's status schema includes `headline: <one sentence characterising the item's
findings>` — defensible as "terse". Every coordinating agent now reads a distilled version of the
findings, its expectations are steered exactly as the task forbids (`:24`), and the plan is
internally consistent so nothing downstream flags it.

**Remedy direction:** make the blindness constraint a stated obligation *on A's schema* (e.g. B's
blindness rule specifies what a status field may not be, and A's schema must satisfy it), so the
property is enforced against its author rather than only against its consumer.

---

### MAJOR 5 — "A dispatches the N analysts" and "B enforces the concurrency ceiling" cannot both be true without breaching file-set disjointness

**Lens: logical.**

A's scope includes "the *dispatch of the N analysts for this item*" (`:65`). Seam 5 (`:145–147`)
says "A specifies that N independent analysts run per item and that N comes from config. B specifies
the global ceiling on concurrent agents and how it is enforced across items. **A does not schedule**;
B does not set N."

A ceiling on simultaneously-running agents is enforced at the point of spawn. The only point of
spawn for analysts is inside the file A owns. So either (i) the ceiling-checking behaviour is written
into A's dispatch file — which is B's rule living in A's file, breaching seam 7 (`:154–155`, "no file
is planned by both"); or (ii) A dispatches freely and B's ceiling is unenforceable for the agents
that constitute nearly all of the run's concurrency. The division does not choose, and "dispatch"
versus "schedule" is never distinguished.

**Failure scenario:** config sets the ceiling to 8 and N to 5. Four items become ready at once. A's
file says "dispatch N analysts"; B's file says "no more than 8 agents at once" but owns no code path
at the spawn site. 20 analysts launch.

---

### MAJOR 6 — The install step names a skill directory the division elsewhere says neither half may choose, and that name is already occupied

**Lens: factual / unstated risk.**

B's scope ends with "the step that puts the skill at `~/.claude/skills/data-distiller/`" (`:108`).
Seam 8 says "Neither half decides the skill's *name* or top-level directory (**both are fixed by the
task**: `Data-Distiller-impl/`, installed at `~/.claude/skills/`)" (`:161–163`).

Check that against the task text: it fixes the build location, "`/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/`"
(`:37`), and states only the *pattern* "A skill is installed by being present at
`~/.claude/skills/<name>/`" (`:36`). It does **not** fix `<name>`. So the division (a) asserts a
constraint the task does not contain, and (b) contradicts itself by choosing `data-distiller` at
`:108` while saying at `:161` that neither half chooses.

The risk this hides is concrete: a skill named `data-distiller` is **already installed** in this
environment (it appears in the harness's available-skills listing, with a description matching this
method). An install step that writes to `~/.claude/skills/data-distiller/` overwrites the installed
copy of the very implementation the task declares off limits — destroying the artifact the run is
supposed to be independent of, and doing it as a side effect nobody planned.

**Failure scenario:** B's plan is executed, the install step runs, and `~/.claude/skills/data-distiller/`
is replaced by the freshly-built `Data-Distiller-impl` — silently, because both the division and the
plan describe it as a fixed, uncontroversial constant.

---

### MINOR 1 — Seam 7 overstates how thin the sibling stage-index relationship is

**Lens: factual.**

Seam 7 (`:156–159`) says B writes stage-index entries for A's files "from **the file names and
one-line purposes A publishes**, not from A's content — the same relationship
`Guarded_change/METHODOLOGY.md:67–84` has with its own `stages/` files."

The cited range is correct as a locator (the stage-index table is exactly
`Guarded_change/METHODOLOGY.md:67–84`). But its "What it covers" column is content-level, not a bare
purpose: e.g. `:73` — "checkable, labeled accept bar; position/concurrency criteria; self-check
criteria"; `:76` — "route by severity; criteria freeze; path-validation blocks gate 4". `SKILL.md:34–45`
is the same. Writing entries of that quality requires knowing what is *in* the stage file, not just
its name.

Fixable in place: require A to publish an index-grade line per file (the column content B needs),
rather than "a one-line purpose".

### MINOR 2 — A's out-of-scope list contradicts the seam in three places

**Lens: logical.**

A's out-of-scope (`:76–77`) excludes "restart/resume", "the config file's contract", and "the on-disk
directory layout". But seam 4 (`:140–143`) requires A to declare completion markers (part of resume);
seam 6 (`:149–152`) requires A to declare its config keys and meanings; seam 2 (`:126–128`) requires A
to define a filename convention relative to the item's directory. A planner reading its own scope
section and skimming the seam will omit all three. Align the out-of-scope wording with the seam.

### MINOR 3 — Failure semantics for an item are unowned

**Lens: completeness (generative sweep).**

Neither half is assigned what happens when an analyst fails or returns nothing, when the verification
pass drops *every* citation for an item, or when an item turns out to be unanalyzable. Seam 3 lets A
express such a state as a permitted status value and B aggregate it, but no bullet on either side
requires either half to define the states or the retry/abandon policy. In a run over a corpus too
large for one context, partial failure is the normal case, not the exception.

### MINOR 4 — A cleaner cut was available and is not weighed

**Lens: missed opportunity.**

The division picks a **runtime visibility invariant** (who may see findings) as an **authorship**
boundary. Blockers 1–2 and Majors 2, 4 and 5 are all instances of the same mismatch: files and
constraints do not partition along a runtime property. An alternative that does partition cleanly —
and matches the siblings' own file structure — is **the pipeline prompt files (`stages/`, plus the
common core) versus the package and run mechanics (`SKILL.md`, `METHODOLOGY.md`, `README.md`, the
config contract + template, run-directory layout, restart/resume, concurrency, install)**. That cut
makes seam 7's "index written from published purposes" exactly the relationship it cites, keeps every
dispatched-agent prompt on one side, and leaves one seam (the stage list + the config keys) instead of
eight. The division should at least say why it was rejected.

### NITPICK 1 — The floor argument leans on unexplained file counts

`:180–188` justifies both halves being above the floor with "on the order of four to six files" and
"six to eight". The conclusion is right (see the floor verdict below) and does not need the numbers;
as written they read as measurements when they are estimates.

---

## Verdict per lens

**1. Factual — findings raised (MAJOR 6, MINOR 1).** Earned with citations. What I checked against
source: the stage-index table is at `Guarded_change/METHODOLOGY.md:67–84` (correct, but see MINOR 1);
"the two layers" + the config contract are at `:88–152` (correct — `:88–101` two layers, `:103–151`
contract); "What a run produces" is at `:154–196` (correct). The YAML-frontmatter router claim holds:
`Guarded_change/SKILL.md:1–4` and `Dragonfly/SKILL.md:1–4` both carry `name`/`description`. The
house shape claim holds: both skills have `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/` with
`charter.md` + `stage-*.md`, and a top-level `*.companion.md` Layer-2 config example — so B's
"shipped template/example config file" and conditional `README.md` are both warranted by the shape,
not inventions. Dragonfly's METHODOLOGY carries the same section set (`Dragonfly/METHODOLOGY.md`
headers at 22/45/72/95/106/141), confirming it as a second example. The one factual defect is the
install-name claim (MAJOR 6) and the one overstatement is MINOR 1.

**2. Logical — findings raised (BLOCKER 2, MAJOR 3, MAJOR 5, MINOR 2).** The recurring shape is a
responsibility named on one side whose enabling condition or consequence sits on the other, with no
channel declared for it.

**3. Missed opportunity — finding raised (MINOR 4).** An authorship-aligned cut was available.

**4. Unstated assumptions & risks — findings raised (MAJOR 1, MAJOR 4, MAJOR 6).** The load-bearing
unstated assumption is that a runtime visibility invariant partitions a file set; the load-bearing
unstated risk is that the party who defines the blindness channel is not the party constrained by it.

**5. Fidelity — finding raised (MAJOR 1).** Terms pinned to the mechanism the division assigns them:
*decompose* → B's decomposition prompt file emitting item handles (`:92–93`); *analyst* → A's prompt
file dispatched N times per item, read-only, cite-per-finding (`:63–65`); *verify* → A's separate
cold pass that re-checks every citation and drops the unverifiable (`:66–67`) — a real re-check, not
a proxy; *merge* → A's rank-by-number-of-agreeing-analysts rule (`:68–69`) — matches the task's
mechanism; *config* → B's Layer-2 contract + shipped template, keys declared by A (`:97–99`,
`:149–152`) — matches the sibling mechanism; *blind roll-up* → status-only channel with the findings
prohibited above the line (`:94–96`, `:128–138`) — **this is the one that fails the pin**: the
division's "coordinating agent" is pinned to "agent above the item boundary", whereas the task pins
it to "agent that has children and reads their status", which includes A's own per-item dispatcher.
See MAJOR 1.

**6. Completeness — findings raised (BLOCKER 1, MAJOR 2, MINOR 3).** Generative sweep run. What I
swept for beyond the division's own sections: the run's terminal output (→ BLOCKER 1); the shared
common file for dispatched agents (→ MAJOR 2); failure/retry semantics (→ MINOR 3); planning order
and conflict arbitration between the halves (→ MAJOR 3); the entry point and invocation path
(covered — B's `SKILL.md` router); the install step (covered, but see MAJOR 6); an example corpus
(explicitly excluded by seam 8, and correctly so — the task requires corpus-agnosticism); the
skill's own self-check section (present in both siblings' `SKILL.md`, so it falls inside B's
`SKILL.md` scope and is not orphaned).

**Was any portion of the task left unaddressed?** Yes — the corpus-level result (BLOCKER 1) and the
execution of the over-size strategy (BLOCKER 2). Everything else in the task's eight defining-property
bullets (`:16–28`) maps to a named owner.

## Verdict per the four split questions

**1. Coverage — FAILS.** Two orphaned remainders (BLOCKER 1, BLOCKER 2b) and one portion each half
can assume the other owns (BLOCKER 2a, the size measure; MAJOR 2, the common file; MAJOR 5, ceiling
enforcement at the spawn site).

**2. The seam — STATED, but not sound.** The seam is unusually well stated — eight numbered items,
including an explicit "what neither half owns" — and that is the division's real strength; this is
not an unstated-seam case. But it is unsound in four specific ways: bidirectional flow with no
ordering (MAJOR 3), a one-directional widening rule that leaves the invariant's author unconstrained
(MAJOR 4), a disjointness claim (seam 7) that seams 5 and A's common-file bullet both violate
(MAJOR 2, MAJOR 5), and a "fixed by the task" claim in seam 8 that the task does not contain
(MAJOR 6).

**3. The floor — PASSES. No finding.** The floor is "one file created or one coherent edit to one
file, with the content specified". Half A must decide the content of, at minimum, a sizing/strategy
rule, an analyst role file, a verification stage and a merge stage; half B must decide `SKILL.md`,
`METHODOLOGY.md`, a decomposition stage, a node/roll-up stage, state/resume, and a config template.
Each half is a multi-file body of work whose content is not yet determined, so neither is a single
atomic step and neither falls below the floor. **The floor is right for this task and I am not
working beneath it:** none of my findings asks for decomposition below one-file granularity — every
one asks for an ownership or channel decision at the seam.

**4. Real joint or arbitrary cut — a real joint, but placed one level off.** Something genuinely
changes at this boundary and the division names it correctly at `:169–178`: the unit of work changes
(one item vs. the corpus and the tree over it), and what is parameterised by the Layer-2 config
changes. This is not a bisection for symmetry. But the third and headline difference — what an agent
may see — does *not* change at the boundary the division drew, because A's own per-item dispatcher and
merger sit below the line while behaving as coordinating agents (MAJOR 1). The joint is real; the
line is drawn one level below where the invariant actually lives.

**"Indivisible" is not my finding.** This task is divisible, and something close to this cut can
work. The defects above are ownership and channel decisions the division did not make, not evidence
that no cut exists.

## Findings summary

| # | Severity | Lens | One line |
|---|---|---|---|
| B1 | **blocker** | completeness/coverage | No half owns the corpus-level output; the run ends at N per-item files. |
| B2 | **blocker** | coverage/logical | Sizing sits in A while the size measure is produced by B and the over-size strategy can only be executed by B. |
| M1 | **major** | fidelity/assumptions | "Blind line == item boundary" is asserted, not derived; A's own per-item dispatcher/merger is a coordinating agent that reads findings. |
| M2 | **major** | completeness | The common-to-dispatched-agents file spans the seam; B dispatches agents too. |
| M3 | **major** | logical | Seam flows both ways with no ordering rule and no arbiter; both halves cannot go second. |
| M4 | **major** | assumptions/logical | A authors the status schema that defines blindness; only B is constrained from widening it. |
| M5 | **major** | logical | The concurrency ceiling is enforceable only at a spawn site inside a file A owns. |
| M6 | **major** | factual | Install target `~/.claude/skills/data-distiller/` is chosen at `:108`, disclaimed at `:161`, not fixed by the task, and already occupied. |
| m1 | minor | factual | Seam 7 understates what the sibling stage index actually carries. |
| m2 | minor | logical | A's out-of-scope list contradicts seams 2, 4 and 6. |
| m3 | minor | completeness | Item-level failure/retry semantics unowned. |
| m4 | minor | missed opportunity | A package-vs-stages cut partitions the file set cleanly; not weighed. |
| n1 | nitpick | — | Floor argument's file counts are estimates presented as measurements. |
