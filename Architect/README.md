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
| `stages/charter.md` | The cold-review discipline (lenses, cite-or-it-doesn't-count, a clean verdict must be *earned*) is method, not plumbing. **Now an UNVETTED DRAFT** rewritten for the one-pass loop — authored freehand outside guarded-change, so it is an *input* to attempt 2's build, not an output. Completeness stays a **distinct lens**: dissolving it into a general mandate is how the generative tier dies quietly. |
| `templates/seed/*.md` | The 7-section plan spine is the floor a leaf fills in — the founding failure was a silently missing section, and `task`-coverage alone would not have caught it. |
| `examples/authoring-a-skill/` | The shape of a per-project Layer-2 config. |

## What was removed

`SKILL.md`, `METHODOLOGY.md`, and all eight `stages/stage-*.md` — the 8-stage pipeline **was** the disk
coordination model. Also `changes/` (three guarded-change run folders) and `guarded-change.architect.md`:
attempt-1 provenance, preserved in the archive.

## Settled since the redesign

1. **The human gate is depth-scoped.** `Human_gate` blocks for the owner at every `depth <= gate_depth`,
   **default 2**, and fires **before children spawn** — a bad cut corrupts everything beneath it, so approving
   after the fact is worthless. Deeper/finer plans warrant more gated levels. On reject the split is
   re-derived and re-presented.
2. **One red-team pass, with the three-tier completeness definition moved INTO the charter.** The separate
   completeness pass goes away, so the charter must carry the tiers explicitly or coverage is lost silently:
   (i) the **universal spine** (the 7 sections every node fills); (ii) **Layer-2 required sections** for this
   plan-type; (iii) the **generative tier** — load-bearing things *neither* list anticipated. Tier (iii) is
   what catches the founding failure and is exactly what dies if completeness is left implicit in an "etc."
   The red-team must also **assign a severity** to each finding, because `Severity()` filters on it.

3. **No backstop on the loop.** The owner ruled: trust the blocker|major filter to terminate it, and fix
   that later if it proves to be a problem. So there is deliberately **no** "same class survives N iterations
   → stop" cap. (Attempt 1's cap tripped twice, so this is a known, accepted risk rather than an oversight.)
4. **Crash recovery: memoize, don't coordinate** — now in the spec. `Memo_read` is called **before** the node
   claims a work-queue slot (a finished subtree should cost nothing), a partial memo resumes the loop exactly
   where it stopped, and two checkpoints per iteration — one after `Consensus`, one at the loop foot — cap the
   worst-case loss at a single red-team round. `node_id` is threaded so children get stable ids (`0.1`, `0.2`,
   …) across restarts.

## The spec

The design spec lives at **`~/Documents/Architect.md`** — owner-authored, single copy, deliberately **not**
duplicated into this repo. Attempt 2 is authored against it. (A snapshot was briefly kept here and removed:
two copies of a spec is the drift problem this project spent a day on.)

## Why the recovery model is not attempt 1's

**Memoize, don't coordinate.** `Memo_read(node_id)` at the top of `Node`, `Memo_write(node_id, iter, task,
plan, division)` at each iteration. On restart you **re-walk down from the root**, not up from the crash
point: a completed node returns its memo instantly, the walk falls through it, and you arrive at the
in-flight node and resume it there. The parent is never "recovered" — it is an ordinary stack frame
re-created by the replay, so **nothing needs reattaching and live-agent state is never persisted**.
One writer per key, written after the value exists, read only by a restart of that same node.
*What is lost in a crash:* whatever was in flight and had not returned (a leaf triple, a red-team round).
The memo write points set that granularity — loop-foot only loses a full iteration; also writing after
`Consensus` loses only the red-team round.
*Contrast with attempt 1,* where disk was the **coordination** mechanism: a parent learned its children were
done by reading a file another stage was supposed to write, which generated "which stage writes this fact,
and when?" — the question that tripped the iteration cap twice, because the answer kept being "a stage that
runs after the one reading it."

**Nothing is installed.** `~/.claude/skills/architect/` was removed on 2026-07-25: attempt 1 had been synced
there after it passed stage-8 conformance, and left there after the dogfood found a blocker in its recursive
path — so an unfinished skill sat live and triggerable. Install only when attempt 2 is actually finished.
