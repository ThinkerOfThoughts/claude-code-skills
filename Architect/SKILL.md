---
name: architect
description: Turns one large task into a detailed, executable plan by recursively subdividing it to an atomic-step floor, planning each atomic piece with three independent cold agents, red-teaming every plan, and merging the results back up the tree. Use when a task is too big to plan in one pass and you want a plan whose every step is executable without further planning. Proactively SUGGEST this when asked to "plan", "design an implementation of", or "work out how to build" something substantial.
---

# Architect

**Purpose: produce a plan every step of which a competent practitioner can execute without
further planning.** It does that by recursion: divide the task until a piece cannot be divided
without falling below an atomic-step floor, plan that piece with three independent cold agents,
red-team the result, and merge back up.

This file is the **router**. The design is a single recursive function `Node(task, plan,
granularity, depth, node_id)`; each role's prompt is a file in `stages/`. The pseudocode this
implements is `~/Documents/Architect.md`.

## Inputs

- **`task`** — what to plan. **The task carries its own source material**: it names the files,
  directories or docs the plan must be checked against. That pointer travels down the whole tree.
  A task that points at nothing its planners can open is a broken invocation, not a licence for
  an agent to go hunting.
- **`granularity`** — the **atomic-step floor** for the run. One sentence, e.g. *"a step a
  competent practitioner can execute without further planning — roughly one file created, or one
  coherent edit to one file, with its content specified."* It bounds three things: how deep the
  tree goes, how fine a leaf's steps are, and what a reviewer is allowed to call vague. Without
  the third the review manufactures infinite subdivision.
- **`gate_depth`** — the human gate fires at every `depth <= gate_depth`. **Default 2.** Set it
  to `-1` to disable the gate; if you do, record that in `decisions.md`, because the run then has
  no human check on any cut.
- **`plan`** — the plan structure to fill. Defaults to `templates/spine.md`.

## Run

1. Create a run folder `runs/<slug>/` with `decisions.md` (append-only) and `memo/`.
2. **You are the root node**: `depth = 0`, `node_id = "0"`, `task` and `granularity` as given,
   `plan` = the spine. **Read `stages/node.md` and execute it.**
3. What the root node returns is the plan. Write it to `runs/<slug>/plan.md`.

## Roles

| Role | File | Spawned by |
|---|---|---|
| node | `stages/node.md` | the root invocation, or a parent node |
| divider (`Divisible`) | `stages/divider.md` | a node, once per iteration |
| split reviewer | `stages/redteam.md` + `stages/redteam-split.md` | the divider, 3 of them |
| leaf (`Spawn_leaf`) | `stages/leaf.md` | a node, 3 of them, when the task is at the floor |
| plan reviewer (`Spawn_redteam`) | `stages/redteam.md` + `stages/redteam-plan.md` | a node, 3 of them |
| combiner (`Consensus`, `Union`, `Severity`) | `stages/combiner.md` | a node, or the divider |

## How you dispatch an agent

Every dispatched agent is a **fresh subagent with no shared context**. Its prompt is:

```
Read these files in order and follow them. They are your instructions:
  <ABS>/Architect/stages/common.md
  <ABS>/Architect/stages/<role>.md          (+ the aiming file, for reviewers)

Your arguments:
  task:        <the task, verbatim, including what it points at>
  granularity: <the floor, verbatim>
  <role-specific arguments — see the role file>

Write your output to <ABS>/runs/<slug>/<node_id>/<name>.md and return that path plus a
three-line summary. Nothing else you say is read.
```

**Use absolute paths.** Dispatch serially unless you have reason to think parallel is safe —
three agents launched at once is the common cause of a rate-limited run.

## Stop-for-human

Pause and ask when: the **human gate** fires (`depth <= gate_depth`) — present the division and
its seam and wait for a verbatim approve or reject; a node wants to **demote a blocker or
major**; or the task points at sources that do not exist. Everything else runs without you.
