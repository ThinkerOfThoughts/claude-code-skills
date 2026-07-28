# Architect — attempt 2 (rebuild in progress)

**State: partially demolished, deliberately.** Attempt 1 was built, shipped, dogfooded, and then spent
three hardening passes failing at the same gate. The owner wrote out the skill's central logic as ~60 lines
of pseudocode (`~/Documents/Architect.md`), and the comparison was decisive: attempt 1 had implemented a
**recursive function as a filesystem protocol**, and nearly every blocker was a bug in that protocol rather
than in the method.

Attempt 1 is preserved in full at **`../Architect-Attempt-1/`** (and in git history at `3771038`, `b08f5a9`,
`8efdca1`). Per the owner: it is deleted once attempt 2 works.

## The core being rebuilt around

A single recursive function. `Node(task, plan)` claims a work-queue slot, asks a cold agent whether the task
is `Divisible`, then either spawns **3 leaf agents** (if atomic) or **2 child nodes** (if not), waits for
them, and merges. It then spawns **3 cold red-teamers**, and their findings — unioned, then filtered to
blocker/major — **become the next iteration's task**. When nothing survives that filter, the loop ends and
the plan is returned.

Why this beats attempt 1:
- **`return plan` IS the join.** No subtree-complete predicate, no `_status` schema, no producer/consumer
  ordering problem — the class of bug that tripped the iteration cap twice cannot be expressed.
- **Slot inheritance** — a child inherits its parent's queue slot, so siblings serialize and only leaf
  triples run concurrently. The entire shared-mutable-state problem disappears.
- **Termination is the red-team going quiet**, not a gate table.
- **`Consensus` for plans, `Union` for issues.** Majority-vote is right for plans (one coherent plan out) and
  wrong for findings: measured across attempt 1's runs, ~85% of findings were caught by exactly one reviewer,
  and several single-reviewer findings were the most valuable of the round.
- **A granularity floor**, set per run and threaded down: *"a step a competent practitioner can execute
  without further planning."* It bounds three things — how deep `Divisible` goes, how fine a leaf writes its
  steps, and **what the red-team is allowed to call "vague."** The third is the one that matters: without it
  the red-team manufactures the problem, because "you didn't say how to grip the handle" becomes an issue,
  the issue becomes the next task, and the loop subdivides forever while every agent behaves correctly.
  Attempt 1 tried to *detect* runaway decomposition after the fact (a convergence guard whose operand turned
  out to be uncomputable); declaring the floor up front is the version that works.

## What is here, and why it survived

| Kept | Why |
|---|---|
| `stages/charter.md` | The cold-review discipline (lenses, cite-or-it-doesn't-count, a clean verdict must be *earned*) is method, not plumbing. **Needs trimming:** its separate sixth "Completeness" lens folds into the single red-team mandate. |
| `templates/seed/*.md` | The 7-section plan spine is the floor a leaf fills in — the founding failure was a silently missing section, and `task`-coverage alone would not have caught it. |
| `examples/authoring-a-skill/` | The shape of a per-project Layer-2 config. |

## What was removed

`SKILL.md`, `METHODOLOGY.md`, and all eight `stages/stage-*.md` — the 8-stage pipeline **was** the disk
coordination model. Also `changes/` (three guarded-change run folders) and `guarded-change.architect.md`:
attempt-1 provenance, preserved in the archive.

## Open, before attempt 2 is authored

1. **The human gate.** The owner agreed one is needed and called it "layer specific" — it is absent from the
   pseudocode, which may mean it belongs in the per-project config rather than the core. Unresolved.
2. **Crash-recovery state.** Required (a VM crash or usage cap must not force a rebuild from scratch), but
   absent from the pseudocode. The shape that avoids attempt 1's failure: **memoize, don't coordinate** —
   each node writes `{iteration, task, plan, division}` after computing it, keyed by its position; a restart
   returns the memo instead of re-running. One writer per key, written after the fact, read only on resume.
3. **One red-team pass or two.** The pseudocode has a single red-team whose mandate covers vagueness, missing
   `task` coverage, missing contingencies, and load-bearing things neither `task` nor `plan` mentions. The
   owner earlier ratified *two distinct passes* (completeness, then adversarial). The pseudocode supersedes
   it in spirit; not confirmed.

**The installed copy at `~/.claude/skills/architect/` is still attempt 1** and still works for single-pass
plans. That drift from this directory is intentional for now — replacing a working tool with a half-built one
would be worse. Re-sync when attempt 2 is ready.
