---
name: architect
description: A gated, self-checking loop for PLANNING — no plan is presentable until its completeness is PROVEN, not asserted. Every plan node fills a 7-section spine, then two distinct cold-subagent passes (a completeness-critic that hunts the load-bearing section no checklist anticipated, then an adversarial red-team) must clear before the plan finalizes or exits plan mode. Scales from a single small pass to recursive decomposition into atomic agent-executable leaves, with a human gate on the top-level split ONLY and recursive sub-orchestration that keeps each owner's context to its own subtree. Use when designing, architecting, scoping, planning, or breaking down any non-trivial task, feature, migration, refactor, or system before building. Plan specifics come from a per-plan config; the loop itself is domain-agnostic. Proactively SUGGEST this whenever a plan, design, or decomposition is being drafted and a missing load-bearing piece would be costly.
---

# Architect

The gated planning loop's purpose: **no plan reaches "presentable" until its completeness is proven —
by a contract-floor plus independent cold critics — not asserted.** This guards the founding failure: a
plan that *looked complete* but shipped with a whole load-bearing section (the output-folder layout)
silently missing, caught only by a human. This file is the **router**: each stage's full procedure + the
rules that govern it live in `stages/`; `METHODOLOGY.md` is the orientation/reference spec (why it
exists, the config contract, the recursion + orchestration model, what a run produces).

## The rules that govern everything — read first

1. **Completeness is proven in three tiers, and the third is the point (CMP).** Every plan node fills
   (i) the **7-section universal spine** (Problem/intent · Approach · Interfaces & seams · **Outputs &
   artifacts WITH their locations** · Failure modes & contingencies · State/restart story ·
   Verification) and (ii) the plan-type's **Layer-2 required sections**. Then (iii) a **generative
   completeness critic** hunts the load-bearing section that is on **neither** list — because the
   founding failure was an **unanticipated** missing section. Tiers (i)–(ii) are the floor a checkbox
   sweep satisfies; tier (iii) is the mechanic this skill exists for. **It is generative, not a checkbox
   sweep (CMP2).**
2. **Two distinct cold red-team passes per node, in order (PASS1 → PASS2).** A **completeness-critic**
   pass (**3 independent cold agents**, "what's missing?") runs **first** (is the skeleton whole?);
   an **adversarial red-team** pass (**3 independent cold agents**, full six charter lenses, "poke
   holes") runs **second** (given it's whole, does it break?). "3 independent cold agents" = three
   separately-spawned subagents, no shared context with the author and none with each other — not one
   agent asked three times. Both passes run at **every node and every altitude**, including the top
   orchestrator on the root plan + the top-level split, each owner over its own slice incl. child seams
   (**total coverage, COV**). The completeness records precede the adversarial records (**PASS-ORD**).
3. **Gate-before-present (GBP).** A plan node cannot be finalized / presented / exit-plan-mode'd /
   assembled until **both** passes are on record and **clean-or-resolved**. The stage-7 assemble step
   checks every node's on-disk `completeness/`+`adversarial/` sets first, so `assembled-plan.md` is not
   written while any node is un-gated. This is the direct gate on the founding
   failure — a hard precondition, not advice.

(The completeness lens, the two-pass discipline, and gate-before-present are stated here, up front,
because these files are prompts — a position-sensitive assembly — and this rule block is load-bearing
*before* the stage table, not after it.)

## Inputs

- **The planning request** — what is to be planned, and roughly how big.
- **A Layer-2 planning config** (`architect.*.{md,yaml}` near the working dir, or `config/planning.md`
  in the run-root). Declares the plan-type, the domain + scale context, the per-plan-type required
  sections, the catalog pointer, the off-limits paths, and the run-root (**OUTSIDE any target repo**).
  If none exists, help author one against the config contract in `METHODOLOGY.md`. **Do not invent plan
  specifics** (the domain, the required sections, the off-limits set). **Validate every path a cold
  agent will be handed** at run start and at each later spawn; a dead path is surfaced to the human, not
  silently skipped.
- **The template catalog** — the git-tracked user-space `~/.claude/architect/templates/`, seeded from
  `templates/seed/` on first run.

## Loop

Create a **run-root OUTSIDE any target repo** with the layout in `METHODOLOGY.md` ("What a run
produces"). Walk the stages **per node** (a node decomposes only after it is gated clean and the
granularity check says decompose); **at each stage, read that stage's file for the full procedure + the
rules it applies.** Maintain `plan/decisions.md` (append-only: gates, top-level-decomposition approval,
red-team routes, cap bounces, convergence escalations, overrides) — the iteration cap reads this log.

| # | Stage — one-line purpose | Read |
|---|---|---|
| **1** | Frame + template-match: orient the node; match a catalog skeleton (instantiate) or mark create-new | → `stages/stage-1-frame-template-match.md` |
| **2** | Draft plan node: fill the 7-section spine + Layer-2 required sections + the proposed granularity (leaf, or a child decomposition + seams) | → `stages/stage-2-draft-node.md` |
| **3** | Completeness-critic: 3 independent cold agents, Completeness lens, skeleton-whole — **gate #1** | → `stages/stage-3-completeness-critic.md` (+ `stages/charter.md`) |
| **4** | Adversarial red-team: 3 independent cold agents, full six lenses, poke holes — **gate #2** | → `stages/stage-4-adversarial-redteam.md` (+ `stages/charter.md`) |
| **5** | Gate: route by worst finding across both passes; gate-bounce cap | → `stages/stage-5-gate.md` |
| **6** | Granularity check → decompose-or-leaf; top-level human decomposition gate; convergence guard; spawn sub-orchestrators + recurse; back-propagate hole-fixes | → `stages/stage-6-granularity-decompose.md` |
| **7** | Assemble: collate root + nested sub-plans → leaf task-specs into `assembled-plan.md` (only when every node is gated clean) | → `stages/stage-7-assemble.md` |
| **8** | Restart / resume: the on-disk state contract; deterministic filenames; HARDSTOP → re-run that node's stage fresh | → `stages/stage-8-restart-resume.md` |

**Scale.** A **small** task's root returns **leaf** at the granularity check (GRN) — a single low-level
pass, no forced decomposition. A **large** task **decomposes recursively** to atomic agent-executable
leaves; the **top-level** split hits the **human gate** (`plan/topgate/` must exist before dispatch —
TOP), while **deeper** splits proceed red-team-gated, autonomous. Orchestration is **recursive** (ORC):
each branch gets its own sub-orchestrator holding only its own subtree + seams (context economy, not
blindness — ECON). **Twin caps:** the gate-bounce cap (CAP) + the convergence guard (DEC: non-reducing
recursion, ≥0.8× parent granularity across two levels → escalate).

## Stop-for-human

Pause and ask when: a **blocker** is about to re-draft a node; the **top-level decomposition gate** is
reached (`plan/topgate/` approval — never auto-approved); a **gate-bounce cap** tie must be broken; the
**convergence guard** escalates; **config or off-limits set is missing**; or a **gating criterion cannot
be verified pre-ship** (build a representative check or get named risk-acceptance — never defer
silently). Refuse to invent plan specifics.

**Under delegation (RAT3).** When a subagent runs this loop, **every** stop above **halts the subagent
and returns the question verbatim to its orchestrator** to relay to the actual human — the subagent
never self-answers or proceeds. The orchestrator relays to the human and relays the verbatim answer
back, never answering as the owner.

## Self-check / dogfooding

These skill files are **prompts** (a position-sensitive assembly). Non-trivial edits take the full
**guarded-change** loop (spec → criteria → cold red-team → build → cold red-team → harness), not a
freehand pass; the initial authoring run's change-records are under `changes/initial-authoring-2026-07/`.
Standing self-check criteria after any edit: live copy == source (`diff`); SKILL ↔ METHODOLOGY ↔
stage-file ↔ charter consistency on every rule stated in more than one place (linked by the **mnemonic
rule-IDs** in METHODOLOGY's cross-file rule index — GBP, PASS1/PASS2/PASS-ORD, CMP/CMP2, SPN, COV,
ORC/ECON, GRN, TOP, CAP, DEC, TPL/TPL3, RST, RAT3); behavior-preservation for anything moved or removed.
Architect could have planned itself — `examples/authoring-a-skill/` is the dogfood config.

## Composition

Standalone; forks its charter from guarded-change (`stages/charter.md`) rather than depending on it
live. **Soft handoff, no hard dependency:** the plan it emits is consumer-agnostic — dragonfly,
guarded-change, data-distiller, a not-yet-existing skill, direct implementation, or a human outside any
computational context each ingest it and check it against their own needs. Plan → (optionally) change /
diagnose / distill.
