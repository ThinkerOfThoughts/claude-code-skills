# Stage 8 — Restart / resume

**What this stage does:** it is not a step you "run" so much as the **on-disk state contract** (RST)
that makes every other stage survive a session-limit death, a crash, or a compaction. Adapted from
data-distiller, whose motivating run died mid-merge and lost nothing that was on disk.

## The state contract (RST)

- **All state is on disk.** `RUN.md`, `index.md`, `config/planning.md`, `plan/` (decisions, topgate),
  and `tree/` (per-node `_status.md` + `plan.md` + `completeness/` + `adversarial/`) are the entire
  state. Chat history is not load-bearing — a fresh (sub-)orchestrator resumes from `RUN.md` + its
  subtree alone.
- **Deterministic filenames → "already produced?" is a path check.** `plan.md`, `completeness/A–C.md`,
  `adversarial/A–C.md`, `_status.md`, `plan/topgate/`, `assembled-plan.md` are fixed names.
  **Stage-done-iff-output-exists** — a node's stage is done **iff** its deterministic output exists.
- **Trust files over any cursor.** If a `_status.md` roll-up disagrees with what is on disk, the
  **files win**. State is per-node — there is no single global cursor to stale-edit.
- **Node identity = directory path.** A restart reads the node's own dir. An **empty / incomplete node
  dir IS the "not planned yet" marker**.
- **HARDSTOP mid-stage → re-run that node's current stage fresh.** In-flight cold agents die on
  shutdown (expected); their half-written outputs are ignored because stage-done is an output-exists
  check on the *complete* deterministic file — a partial `completeness/B.md` is not the final name and
  is overwritten by the clean re-dispatch. **A node whose output already exists is NOT re-planned; only
  the interrupted node's current stage re-runs.**
- **Run-root lives OUTSIDE any target repo.** The disk-as-instrumentation model depends on it (a
  run-root inside the planned repo pollutes the planned artifact).

## RUN.md — the apex runbook

`RUN.md` is a **self-contained runbook**: the mission in one paragraph, the hard rules (gate-before-present,
top-level human gate, run-root-outside-repo, the twin caps), the key paths, and the **restart
procedure** — read `RUN.md` + `index.md`, walk `tree/` for the first node whose expected output is
missing → resume there. A fresh or post-compaction orchestrator continues from `RUN.md` + the tree
alone. Each sub-orchestrator's resume surface is its **own** subtree (ECON) — it does not re-read
sibling subtrees.

## Rules governing this stage

**The disk is the truth (RST).** Any "where am I?" question is answered by walking `tree/` for the first
missing deterministic output — never by trusting an in-memory cursor or chat scrollback.

**Idempotent re-dispatch.** Re-running a stage for a node with a complete output is a no-op; re-running
one with a missing/partial output produces the clean file. The restart contract **discriminates** done
from not-done — it neither skips everything nor redoes everything.

**Gate-before-present survives restart (GBP).** A resuming orchestrator still cannot assemble while any
node is un-gated; the contract is the same on resume as on first pass.
