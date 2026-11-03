# Stage 1 — Spec

**REVISED 2026-07-31** after stage-3 review (`3-redteam-plan-a.md`, `3-redteam-plan-b.md`) and an
orchestrator correction. Two changes of substance: the baseline was false and is re-derived in
`0-baseline.md`; and **the scope is now item 1 alone**, because items 2 and 3 were already applied
at commit `cf16967` by the run that produced them. Both are stated explicitly below rather than
silently re-scoped.

## The problem

Iteration 3's division at node 0 **completed**: 107 minutes, 13 dispatched agents, 12 cold split
reviews across four rounds, ~7,500 lines of prose, to cut one task in two. **Every one of the 12
reviews, in every one of the four rounds, endorsed the cut.** Across all three iterations of the
run, no reviewer has ever objected to where the line was drawn; all ~90 findings landed on the
divider's *seam description*.

So the defect is not correctness. It is that the apparatus prices a division as if it were a plan.

The apparatus is literally borrowed. `redteam-split.md` is an *aiming file* appended to
`redteam.md`, the **plan** reviewer's charter — so a split reviewer inherits the six lenses, the
earned-clean disciplines and the "last reader of this cut" framing, and from `common.md` the
four-tier severity model. A division is two sub-tasks and a joint. Graded on six lenses it
produces 21–47 KB reviews, because reviewers graded on finding defects find them at whatever
grain is available.

And the over-complication is self-perpetuating. `divider.md:97-98` — *"While any `major` or
`blocker` stands, re-derive the split and review again"* — contradicts that same file's
§"Agreement is about PROCEEDING, not about being finished" (record 3438) six lines above, and it
is the rule that executed: four re-derivations of a cut nobody objected to.

## The owner's instruction — transcript record 3666, verbatim

Source: `~/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
line 3666, `type: user`. Read directly 2026-07-31; both stage-3 reviewers independently verified it
character-for-character.

> the dividers instruction should boil down to this: Find a natural seem in the given task, and
> split it into two pieces at that seem. The reviewers instruction should boil down to: Is this
> split at a natural seem? If it is, does it reduce the task past the point of maximum
> granularity?  If it is a natural split, and does not reduce past the point of maximum
> granularity, approve; otherwise, reject with explanation.

`Architect-rulings.md` records the worked example given alongside it (primary loci: records 3628
and 3634, found by reviewer A): merge four files of unsorted numbers into one sorted deduplicated
file, split {a,b} / {c,d}. Dedup within each half does not dedup across halves — a true finding.
**The owner's correction: the cross-half merge is handled on the next pass of
`while(task.empty() == false)`**, because the plan red-team sees the merged result against the
original task and it becomes the next task. **A split review that reports what the loop already
handles is pure cost.**

## The scope rule — transcript record 3497, verbatim

> and it was never meant to be one iteration per fix. it was meant to be fix whatever broke
> durring the run, if multiple things broke at once, then they should all be fixed, along with any
> things that broke but didn't take the run with them

Fix everything that broke; **speculative hardening — a guard for something that has not happened —
stays out.**

## Scope, stated explicitly

The brief named three items. Two are already applied at `cf16967`, verified by reading the files:

- **Item 2, `Divisible` outside the memoised region — ALREADY FIXED.** `node.md:54-74` now carries
  a **checkpoint 0**: the memo is written the instant `Divisible` returns, before the gate and
  before any spawn, with `division` stored as one of the three explicit answers so *"never
  computed"* and *"the answer was `null`"* stay distinguishable, and `FAILED_TO_DIVIDE` memoised
  as an escalation rather than a failure to compute. **Not re-fixed here.** It has never been cold
  reviewed, so it goes into this run's stage-6 review scope.
- **Item 3, the producer/consumer seam — ALREADY FIXED.** `divider.md:60-88` no longer asks for a
  directional contract; it states the seam must be self-contained and gives three destinations for
  a cross-half dependency. **Not re-fixed here.** Two things must be said about it, though:
  1. The run's own finding is that removal did not make the failure impossible — the divider's
     round-1 seam smuggled the dependency back through a *namespace rule* rather than a sentence,
     and a cold reviewer caught it. **The shape re-enters through mechanism, not wording.**
  2. This change **deletes the three-destination apparatus** as part of item 1, so the question is
     whether the contradiction returns. It does not fully evaporate, and this spec does not claim
     it does: 3666 asks for *a natural seam*, which describes a joint rather than an interface, so
     the shape that caused the contradiction is no longer requested — but nothing in 3666 forbids
     a divider writing a directional contract anyway. **The residue is one sentence in each file.**
     No taxonomy, no severity, no reviewer sub-check.

**A design proposed in the first draft is withdrawn.** That draft added a second, divider-level
memo (append each round to `divide-<iter>.md`; a restart resumes at the first missing round).
Reviewer A found that the file already has a **second reader** — `node.md:50-51` and
`divider.md:117-118` hand it up to the node and the owner on `FAILED_TO_DIVIDE` — which breaks the
single-reader discipline the design claimed, and reviewer A/B both found the injection test would
put two writers on a live file. With checkpoint 0 already in place and item 1 collapsing the
division to roughly one round of short reviews, **a second memo mechanism is a guard for a
death-during-division that has not happened since checkpoint 0 landed** — record 3497 excludes it.
Withdrawn, and recorded here rather than dropped silently.

**So this run's change is item 1: rewrite `divider.md` and `redteam-split.md` to record 3666** —
plus the dispatch and context corrections that rewrite forces, plus cold review of the two
unreviewed fixes above.

## What item 1 requires

### 1a. The two files

The divider's job: **find a natural seam in the task and cut there.** The split reviewer's job:
**two questions, then approve, or reject with an explanation.**

1. Is this split at a natural seam?
2. If it is — does it reduce the task past the point of maximum granularity?

Both hold → **approve**. Otherwise → **reject with explanation.**

**A one-line approval must be a correct output, not a lazy one.** The current file's earned-clean
clauses make a short clean verdict literally non-conforming; under 3666 it is the expected shape
of an approval. Stated, or the inherited habit re-imports the cost.

### 1b. The split reviewer stops reading `redteam.md`

`redteam.md` is where the six lenses, the earned-clean clauses and the "graded on precision"
counterweight physically live. Leaving it in the dispatch re-imports everything this change
removes. Split reviewers read `common.md` + `redteam-split.md`. `divider.md:96` and `SKILL.md`'s
Roles table both name the trio today and must both change.

**Two rules the split reviewer loses with it, found by both reviewers, and what happens to each:**

- **`redteam.md:11`, *"Common to both: the task and the granularity floor."*** This is the
  reviewer's statement of what it holds. Both of 3666's questions are unanswerable without the
  task and the floor, and a reviewer that does not know it holds them can return a **vacuous**
  one-line approval that this change's own criteria would otherwise score as success. **CARRY —
  restated in `redteam-split.md`.**
- **`redteam.md:13-18`, the floor bound on what may be called vague** — the infinite-regress
  guard, and a safety property, not a style rule. **CARRY — restated in `redteam-split.md`.**
- `redteam.md:54`, *"graded on precision, not on how many you raise"* — **CARRY**, as one clause;
  it is the direct counterweight to the dynamic this change exists to kill.
- `redteam.md:43-44`, *"do not self-censor a lone observation"* — **DROP, declared.** It exists
  because plan findings are `Union`ed and a lone finding survives. A split verdict is not
  `Union`ed; it is counted. There is nothing for a lone observation to survive into.
- The six lenses — **DROP, declared.** This is the change.

### 1c. `common.md`'s severity model must be scoped

Found by reviewer A (blocker B2) and correctly: the four-tier severity model, *"a finding with no
severity is unusable"* and *"findings are merged, **never voted on**"* live in **`common.md`**
(`:38-56`), which every dispatched agent reads first and which the split reviewer keeps reading.
Against a `redteam-split.md` that returns approve/reject with no severities and is counted 2-of-3,
those are flat contradictions in the reviewer's own context.

The fix is **one scoping sentence in `common.md` §4**, naming the roles that produce severities.
Not a rewrite of `common.md`, and not a duplicated copy in the role files: the roles that act on
§4 are the plan reviewer, the combiner and the node, and `leaf.md:47` already says *"severities
are for reviewers."* Stating §4's actual scope is not modifying it.

## Constraints

- **Nothing installed, nothing committed.** The orchestrator commits.
- No speculative hardening (record 3497).
- Architect's stage files are a **position-sensitive assembly** — they are prompts, concatenated
  in a stated order. Removing `redteam.md` from the split reviewer's dispatch does not move any
  text, and still deletes two rules from that reviewer's context. The position lens applies and
  is why 1b enumerates rule by rule instead of asserting "nothing moved."

## Expected touched files

| File | Change |
|---|---|
| `Architect/stages/divider.md` | rewritten, 118 → ~40 lines |
| `Architect/stages/redteam-split.md` | rewritten, 62 → ~35 lines, standalone (no longer appended to `redteam.md`) |
| `Architect/stages/common.md` | one scoping sentence in §4 |
| `Architect/SKILL.md` | Roles table: split reviewer reads `common.md` + `redteam-split.md` |
| `Architect/runs/data-distiller/decisions.md` | ledger entry; iteration 4 opened |
| `Architect/changes/divider-3666/*` | this run's own artefacts |

**Not touched:** `redteam.md`, `redteam-plan.md`, `leaf.md`, `combiner.md`, `node.md`,
`templates/spine.md`, and `~/Documents/Architect.md` — `Divisible`'s signature, return contract
and both call sites are unchanged by this run.
