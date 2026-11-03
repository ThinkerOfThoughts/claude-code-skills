# Stage 7 — Assemble

**What this stage does:** collate the gated-clean plan tree into the single deliverable
`assembled-plan.md` — the root plan + nested sub-plans → leaf task-specs. This is the only stage that
produces the presentable artifact, and it **cannot run while any node is un-gated** (GBP made
structural).

## Procedure

1. **Verify every node is gated clean (GBP).** Walk `tree/`. For **every** node confirm both
   `completeness/` (3 records) and `adversarial/` (3 records) exist and its `decisions.md` gate entry is
   **clean-or-resolved**. If **any** node is missing a pass or carries an unresolved finding, **do not
   assemble** — resume that node's loop. Assembly is blocked, not degraded.
2. **Collate top-down.** Write `assembled-plan.md`: the root `plan.md`, then each sub-plan nested under
   its parent, down to leaf task-specs, with each node's **seams** carried so a consumer can see the
   contracts between branches. Preserve the 7-section spine per node.
3. **State the deliverable is consumer-agnostic.** The assembled plan targets **no downstream contract**
   — a header notes that a consumer (dragonfly / guarded-change / data-distiller / direct
   implementation / a human) checks it against *their own* ingestion needs.
4. **Record completion** in `RUN.md` / the apex `_status.md`.

## Rules governing this stage

**Assembly is gate-before-present made structural (GBP).** `assembled-plan.md` physically cannot be
written while any node's pass set is missing or unresolved. The presentable artifact is the proof that
every node cleared both gates — completeness is **proven, not asserted**.

**Total coverage is a precondition (COV).** "Every node gated clean" includes the **root plan** and
every **top-level and deeper split's seams** — a between-branch contingency caught by a parent's pass is
part of the union that makes coverage total. A tree with a clean root but an un-reviewed seam is not
assemblable.

**A fully-covered clean tree assembles.** The coverage requirement does not deadlock a clean tree:
when every node has both passes clean-or-resolved, assembly proceeds — the gate blocks holes, not
progress.

## Cross-cutting rules

**Disk is the truth (RST).** `assembled-plan.md` is the deterministic output name; its existence is the
"run complete" marker. A restart before it exists resumes the first un-gated node; a restart after it
exists is a no-op.
