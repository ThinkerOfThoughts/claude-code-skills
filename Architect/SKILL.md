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

1. Create the run folder and, inside it, an **attempt** folder:

   ```
   runs/<slug>/
     decisions.md          append-only ledger, ONE per run, SHARED by every attempt
     it<N>/                one attempt: it1, it2, …  <-- this is what stage files call <run>
       memo/               <node_id>.json, one per node
       <node_id>/          each node's own artifacts
       plan.md             what the root node returned, when it returns
   ```

   **`<run>` in every stage file means the attempt directory `runs/<slug>/it<N>/`.** The one
   exception is `<run>/decisions.md`, which always resolves **up** to the shared ledger at
   `runs/<slug>/decisions.md` — the ledger spans attempts on purpose; everything else must not.
   A memo is addressed by `node_id`, and the root's `node_id` is `"0"` in every attempt, so
   **attempts that shared a `memo/` would read each other's memos as their own** and skip
   `Divisible` on the strength of a superseded result.

2. **Record the invocation in `decisions.md` before you start**: `task` **verbatim, including what
   it points at**, `granularity` verbatim, `gate_depth` with your reason if it is not the default,
   and which `plan` template you used. The task is the carrier of all source material for the whole
   tree; a run whose ledger does not hold it cannot be resumed by anyone who was not there. *(A
   resumed run on 2026-07-31 had to recover the task from a divider's paraphrase inside an artifact
   the ledger had declared void — the only thing about that restart that could not simply be read.)*
3. **You are the root node**: `depth = 0`, `node_id = "0"`, `task` and `granularity` as given,
   `plan` = the spine. **Read `stages/node.md` and execute it.**
4. What the root node returns is the plan. Write it to `runs/<slug>/it<N>/plan.md`.

## Roles

| Role | File | Spawned by |
|---|---|---|
| node | `stages/node.md` | the root invocation, or a parent node |
| divider (`Divisible`) | `stages/divider.md` | a node, once per iteration |
| split reviewer | `stages/redteam-split.md` | the divider, 3 of them, concurrently |
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

Write your output to <ABS>/runs/<slug>/it<N>/<node_id>/<name>.md and return that path plus a
three-line summary. Nothing else you say is read.
```

**Use absolute paths.** **Dispatch a set of siblings concurrently** — three split reviewers, three
leaves, three plan reviewers. They are independent by construction and serialising them multiplies
the round's wall clock by three for nothing: on the Data-Distiller run it cost ~50 of one
division's 107 minutes. If the API starts returning rate-limit errors, back off and retry; that is
a response to an observed error, not a default.

## Stop-for-human

Pause and ask when: the **human gate** fires (`depth <= gate_depth`) — present the division and
its seam and wait for a verbatim approve or reject; a node wants to **demote a blocker or
major**; or the task points at sources that do not exist. Everything else runs without you.
