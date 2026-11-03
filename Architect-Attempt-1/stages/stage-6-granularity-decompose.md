# Stage 6 — Granularity check → decompose-or-leaf

**What this stage does:** for a **gated-clean** node, execute its granularity call — either **leaf**
(done; the node is an atomic task spec) or **decompose** (spawn a sub-orchestrator per child and
recurse). It also enforces the **top-level-only human decomposition gate**, the **convergence guard**,
and **back-propagation** of any hole-fix to the catalog.

## Procedure

1. **Read the granularity call (GRN).** The node's proposed leaf-vs-decompose decision (drafted at
   stage 2, validated by the two passes). Record the final decision in `index.md` / the node's
   `_status.md`.
2. **If LEAF** — the node is an **atomic, agent-executable task spec**. It has no children; planning of
   this node is done. (A small task's root is a leaf: single low-level pass, no forced decomposition.)
3. **If DECOMPOSE and this is the TOP-LEVEL split (TOP)** — **block dispatch** until the human approves
   the first, high-level split (the major sub-plans + the **seams/interfaces between them**). The
   approval artifact must **exist on disk** at `plan/topgate/` before any sub-orchestrator is spawned.
   Under delegation, requesting this approval is a **stop-for-human** (RAT3). Withholding `topgate/`
   keeps dispatch blocked; supplying it releases dispatch.
4. **If DECOMPOSE at a DEEPER split** — proceed **red-team-gated, autonomous**: **no human stop** (the
   gate fires at the top level ONLY, to avoid gate fatigue on large trees). Blockers / cap /
   missing-config still stop-for-human at any depth.
5. **Spawn a sub-orchestrator per child (ORC).** At each branch, delegate each child to its **own
   sub-orchestrator**, which owns that child's subtree. The orchestration tree mirrors the plan tree.
   Each sub-orchestrator holds only **its own subtree's** skeleton + seams + child `_status` roll-ups
   (ECON) — not sibling subtrees' internals, not the whole tree. Each recurses from stage 1 on its node.
6. **Apply the convergence guard (DEC).** Before recursing, check the child granularity against the
   parent: if **two consecutive levels do not reduce granularity** — a child node's estimated leaf
   count / work-size is **≥ 0.8×** its parent's — **escalate** the branch (append a `decisions.md`
   escalation; stop-for-human under delegation) rather than recursing further. A genuinely-reducing
   decomposition (each level produces smaller atomic children) does **not** trip the guard.
7. **Back-propagate hole-fixes (TPL3).** If a finding fixed on this node patched a hole in a section
   that came from a catalog skeleton, apply the same fix to the **skeleton** and commit it to the
   user-space catalog (`git commit` in `~/.claude/architect/templates/`). A create-new node, once gated
   clean, distils a **new** skeleton into the catalog (TPL2).

## Rules governing this stage

**Granularity decides leaf vs. decompose (GRN).** A **leaf** = an atomic, agent-executable task spec —
one agent executes it with no further planning. The decision is a real discrimination: a small task
returns leaf; a large task decomposes. The two passes have already validated the call.

**Top-level human gate ONLY (TOP).** The human approves the **top-level** split before dispatch
(`plan/topgate/` must exist); **deeper** splits proceed red-team-gated without a human stop. Both halves
hold: it fires at the top, it does **not** fire deeper.

**Convergence guard (DEC).** Non-reducing recursion (≥0.8× parent granularity across two consecutive
levels) escalates rather than recursing indefinitely. This is a **novel** Architect cap with no sibling
precedent; the concrete bound is fixed here so it is checkable, not open-ended.

**Recursive orchestration, context economy not blindness (ORC / ECON).** A sub-orchestrator per branch;
each holds only its own subtree + seams + roll-ups. Blindness is **not** the goal (planning needs a
coherent cross-tree vision) — a parent holds its children's **seams** plus roll-ups, but not each
child's full internal detail, so no orchestrator's context scales with total tree size.

**Total coverage (COV).** Every spawned sub-orchestrator red-teams **its own** node (both passes,
stages 3–4) including its children's seams; the top orchestrator did the same on the root + top-level
split. Coverage is the union of all node reviews plus each owner's own-seam review.

## Cross-cutting rules

**Disk is the truth (RST).** Granularity decisions, `topgate/`, escalations, and catalog commits are on
disk. A restart re-reads `index.md` + the tree; a completed node (its `plan.md` + gated records exist)
is **not** re-planned; an interrupted node's current stage re-runs fresh.

**Stop-for-human under delegation (RAT3).** The top-level gate, a convergence escalation, or a blocker
**halts the runner and relays the question verbatim** — never self-answered.
