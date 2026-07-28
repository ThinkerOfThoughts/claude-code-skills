# Stage 4 — Adversarial red-team (gate #2)

**What this stage does:** the **second** cold pass over a node's `plan.md` — *given it is whole, does it
break?* **3 independent cold agents** run the **full six charter lenses** with a poke-holes mandate,
then the owning orchestrator routes their worst finding (stage 5). Runs **after** the completeness pass.

**Read `stages/charter.md` for the full charter (the six lenses + the earned-clean discipline +
provenance + the conditional position/concurrency lenses), then apply the adversarial-aiming below.**

## Procedure

1. **Spawn 3 independent cold agents (PASS2).** Three **separately-spawned** subagents, no shared
   context with the author and none with each other. Each handed the charter verbatim + the closed input
   set (this node's `plan.md` + decomposition + child seams, `redteam_context`, the parent plan, and the
   carried-forward completeness findings from `decisions.md`).
2. **Run all six lenses, mandate = poke holes.** Overlooked items, uncovered contingencies, false
   assumptions, better approaches left on the table; Factual (claims vs. source), Logical, Missed
   opportunity, Unstated assumptions & risks, Fidelity (pin the loaded terms), Completeness (backstop the
   stage-3 pass). Fire the **position lens** if the planned artifact is a position-sensitive assembly and
   the **concurrency lens** if the plan alters concurrency over shared state (charter conditional lenses).
3. **Validate the granularity call (GRN).** The node's proposed leaf-vs-decompose decision + its
   decomposition + child seams are **in scope** — a wrongly-declared leaf or an incomplete seam set is an
   adversarial finding here.
4. **Require earned-clean per lens.** Clean Factual → citations; clean Fidelity → pinned terms; clean
   Completeness → named section-classes + coverage. A clean lens with none of these is un-run and re-run.
5. **Record each agent verbatim** under the node's `adversarial/` (`A.md`, `B.md`, `C.md`) with full
   provenance (charter, context list, raw output, agent type/model, context-file sha256s).
6. **Route at stage 5** on the worst finding across the three records (and the carried completeness
   findings).

## Rules governing this stage

**Full six lenses, kept distinct (charter).** The six are parallel attack angles with no precedence
among them; one must not crowd out another. The adversarial pass runs all six; the completeness pass led
with the sixth.

**Coverage is total, run per-owner (COV).** This pass runs at **every node and every altitude**,
executed by the owning (sub-)orchestrator over its own slice — the node's plan, its decomposition, and
the **seams among its children** — **the top orchestrator included on the root plan + top-level split**.

## Cross-cutting rules

**Completeness before adversarial (PASS-ORD).** The `adversarial/` records are written **after** the
node's `completeness/` records — gate #1 precedes gate #2.

**Gate-before-present (GBP).** The node cannot finalize until both passes are clean-or-resolved.

**Nothing self-certifies / review records are verbatim / paths are validated (charter).** Same
provenance and path-validation duties as stage 3.

**The reviewer's severity routes (SEV/charter).** Findings route on the reviewer's stated severity;
demoting a blocker/major needs the human tie-break (stage 5).
