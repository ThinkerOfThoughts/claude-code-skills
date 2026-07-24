# Stage 7 — Restart / resume

**What this stage does:** it is not a step you "run" so much as the **on-disk state contract** that
makes every other stage survive a session-limit death, a crash, or a compaction. It exists because
the method's motivating run **died mid-merge** and lost nothing that was on disk.

## The state contract

- **All state is on disk.** The corpus, `index.md`, `plan/` (budget, decisions, cut-gate),
  `_prepared/`, `tree/` (with per-node `_status.md`), and `summaries/` are the entire state. Chat
  history is not load-bearing — a fresh coordinator resumes from `RUN.md` + the tree alone.
- **Deterministic filenames → "already produced?" is a path check.** `analysis/A.md`,
  `analysis/A_verified.md`, `superlist.md`, `summaries/<SET>_summary.md` are fixed names.
  **Stage-done-iff-output-exists** — a stage is done for a node **iff** its output file exists.
- **Trust files over any cursor.** If a `_status.md` roll-up disagrees with what is actually on disk,
  the **files win**; `_status.md` is a convenience roll-up, not the source of truth. (There is **no
  single global cursor** to stale-edit — state is per-node, which designs out the stale-cursor-edit
  gotcha entirely.)
- **Node identity = directory path.** A restart reads the node's own dir. An **empty leaf dir IS the
  "not done yet" marker**; the static `tree/` skeleton was created at decompose-time, so the shape is
  already fixed and only leaf contents fill in.
- **HARDSTOP mid-stage → re-run that whole stage fresh** for the affected node. In-flight agents die
  on shutdown (expected); their half-written outputs are ignored because stage-done is an
  output-exists check on the *complete* deterministic file — a partial write is not the final name /
  is overwritten by the clean re-dispatch. **Nothing completed is lost; only the interrupted stage
  re-runs.**

## RUN.md — the apex runbook

`RUN.md` is a **self-contained runbook**: the mission in one paragraph, the hard rules (blindness,
read-only, off-limits, concurrency cap), the key paths, and the **restart procedure** (read
`RUN.md` + `index.md` + walk `tree/` for the first node whose expected output is missing → resume
there). A fresh or post-compaction coordinator continues from `RUN.md` + the tree alone.

## Liveness (advisory — host-specific operational guidance, NOT a gated part of the core)

The **durability** half of restart (resume-from-disk) is core. The **liveness** half depends on the
host's session/usage mechanics and is documented guidance, not an agnostic gated property:
- a **watchdog** to re-kick the session on a usage-reset;
- **hung-agent detection** — periodically check each in-flight agent; one with no completion past a
  threshold (e.g. >30 min) is killed + re-dispatched (its stage re-runs cleanly);
- **pacing** — under usage pressure, serialize dispatch (down to one-at-a-time within the cap)
  rather than running the full budget concurrently.
These are operational conveniences; correctness rests on the on-disk state contract above, which
holds whether or not a watchdog is present.

## Rules governing this stage

- **The disk is the truth.** Any "where am I?" question is answered by walking `tree/` for the first
  missing deterministic output — never by trusting an in-memory cursor or chat scrollback.
- **Idempotent re-dispatch.** Re-running a stage for a node with a complete output is a no-op (the
  output already exists); re-running one with a missing/partial output produces the clean file.
- **Blindness survives restart.** A resuming coordinator reads `_status.md` + filenames, never
  findings — the contract is the same on resume as on first pass.
