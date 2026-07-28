# Stage 3 — Completeness-critic (gate #1)

**What this stage does:** the **first** of the two cold passes over a node's `plan.md` — *is the
skeleton whole?* **3 independent cold agents** review the node aimed at the **Completeness lens**, then
the owning orchestrator routes their worst finding (stage 5). Runs **before** the adversarial pass — you
prove the plan whole before you try to break it.

**Read `stages/charter.md` for the full charter (the six lenses + the earned-clean discipline +
provenance), then apply the completeness-aiming below.** The charter core is given to each reviewer
verbatim.

## Procedure

1. **Spawn 3 independent cold agents (PASS1).** Three **separately-spawned** subagents, each with **no
   shared context with the author and no shared reasoning context with each other**. Not one agent asked
   three times. Each is handed the charter verbatim + the closed input set: this node's `plan.md`, its
   decomposition + child seams, the config `redteam_context` + `domain_context`, the parent node's plan,
   and any carried-forward findings from `decisions.md`.
2. **Aim them at the Completeness lens (CMP).** Primary mandate: *"what load-bearing thing is missing —
   a section, an interface, an output location, a failure mode, a state/restart story, a between-child
   seam?"* Check all three tiers: (i) the 7-section spine, (ii) the Layer-2 `required_sections`, and
   (iii) — decisively — the **generative** sweep: *"what load-bearing section is on **neither** list?"*
3. **Require an earned-clean verdict.** A "no gap" Completeness verdict is valid only if the agent
   **names each section-class it checked** (each spine section + each Layer-2 section, by name) and
   **cites where the node covers it** — and states the generative sweep was run. A clean verdict that
   lists nothing is treated as **un-run** and re-run (charter earned-clean clause).
4. **Record each agent verbatim.** Write three records under the node's `completeness/` (`A.md`, `B.md`,
   `C.md`), each embedding the charter given, the exact context list, the agent's verbatim output, its
   agent type + model, and its reported context-file sha256s (charter provenance). A record missing any
   element = un-run.
5. **Route at stage 5** on the worst finding across the three records.

## Rules governing this stage

**Completeness is generative, not a checkbox sweep (CMP2).** Ticking the spine + the Layer-2 list is
the **floor** (tiers i–ii). The finding this pass most exists to produce is the **unanticipated**
missing section (tier iii) — the founding failure's true shape. An agent that only ticks the two lists
has not run the lens.

**Earned-clean Completeness (CMP / charter).** A clean verdict names the section-classes checked and
cites coverage for each, and states the generative sweep ran. Otherwise re-run.

**Section 4 is load-bearing (SPN).** Every node's Outputs & artifacts **with locations** is checked by
name; its absence is the canonical founding-failure gap and blocks finalize.

## Cross-cutting rules

**Nothing self-certifies.** The node's author never approves it; the review is by cold agents with no
shared context (charter). The owning orchestrator dispatches — including the **top orchestrator on the
root plan** — and does not self-certify (COV).

**Completeness before adversarial (PASS-ORD).** This pass is recorded **before** the stage-4 adversarial
pass at each node — the `completeness/` records precede the `adversarial/` records.

**Gate-before-present (GBP).** The node cannot finalize until this pass **and** the adversarial pass are
clean-or-resolved.

**Review records are verbatim (charter).** `completeness/A–C.md` embed the charter, context list, raw
output, agent type/model, and context-file sha256s; the orchestrator's interpretation goes to
`decisions.md`.

**Paths are validated, not assumed.** Mechanically check every path handed to a cold agent
(`redteam_context`, the parent plan, seam files) exists and is readable before the spawn; a dead path is
surfaced to the human (RAT3), not silently skipped.
