---
name: guarded-change
description: A gated change loop where no AI artifact is accepted without an independent cold-subagent red-team, and "done" is proven against measurable criteria. Use when making any non-trivial change (code, plan, or design) and you want spec→plan→red-team→build→red-team→harness discipline. Project specifics come from a per-project config; the loop itself is domain-agnostic.
---

# Guarded Change

The gated change loop's purpose: **no AI-produced artifact reaches "accepted" without an
independent challenge, and "done" is proven against an explicit measurable bar.** This file is
the **router**: each stage's full procedure + the rules that govern it live in `stages/`.
`METHODOLOGY.md` is the orientation/reference spec (why it exists, the config contract).

## Inputs

- **The change request** (from the user, or — when self-checking — a named artifact).
- **A project config** (Layer 2). Look for one (e.g. `guarded-change.*.{md,yaml}` in or near
  the working dir). If none exists and the loop needs stage 0/8, ask for it or help author it
  against the config contract in `METHODOLOGY.md`. Do not invent project metrics.
  **Validate every path a cold reviewer will be handed** (config `redteam_context`, spec
  touched-files, fixtures) — at run start, and again at any later reviewer spawn for paths new
  since; record the result in `decisions.md` (gate 4 cannot pass without it) and surface dead
  paths to the human (METHODOLOGY "Paths are validated, not assumed"; stage-3/4/6 files carry
  the operative rule).

## Loop

Create a change folder `changes/<slug>/` and produce one doc per stage (names in METHODOLOGY
"What a run produces"). **Step numbers below are the canonical stage numbers used everywhere**
(loop, severity table, decisions.md). At every **gate (stages 4, 7, 8)**, append a line to
`decisions.md` (gate by stage number, worst severity, route, rationale+name for any override) —
the iteration cap reads this log. Walk the loop; **at each stage, read that stage's file for
the full procedure + the rules it must apply:**

| # | Stage — one-line purpose | Read |
|---|---|---|
| **0** | Baseline: snapshot current behavior (only if a prior version + config baseline exist; else skip → conformance-only) | → `stages/stage-0.md` |
| **1** | Spec: rich problem definition; declare the expected touched files | → `stages/stage-1.md` |
| **1.5** | Criteria: the checkable, labeled (gating/advisory) accept bar — mandatory | → `stages/stage-1.5.md` |
| **2** | Plan: how + measurement + instrumentation + thresholds | → `stages/stage-2.md` |
| **3** | Red-team the plan: cold review of {1, 1.5, 2} — the assumption-catcher | → `stages/stage-3.md` (+ `stages/charter.md`) |
| **4** | Gate: route by worst finding; freeze criteria on route-to-build | → `stages/stage-4.md` |
| **5** | Build: implement per the plan | → `stages/stage-5.md` |
| **6** | Red-team the code: cold review of code vs {1.5, 2}; mechanical `git diff` | → `stages/stage-6.md` (+ `stages/charter.md`) |
| **7** | Gate: route by worst finding | → `stages/stage-7.md` |
| **8** | Harness: measure → conformance (always) + regression (if baseline) → verdict | → `stages/stage-8.md` |

The **most important gate is stage 3**, not 6 or 8 — the plan-red-team catches a missing
measurement plan or an un-instrumented change *before a line of code is written*. Stages 3 and 6
share the red-team charter in `stages/charter.md` (stage 3 adds the coverage-challenge + label
audit; stage 6 adds the mechanical-diff duty). Gates 4/7/8 each carry the full severity table.
The **iteration cap** (all gates): after 2 bounces at the same gate on the same finding class,
stop and a human breaks the tie (see the gate files).

## Stop-for-human

Pause and ask when: a **blocker** is about to restart the loop; a **major** appears at the
harness (stage 8); **criteria/config are missing**; a **gating criterion cannot be verified
pre-ship** (build a representative harness or get named risk-acceptance — never defer silently);
or an **escalated fidelity finding's owner answer does not disambiguate the flagged axis**
(re-ask the axis rather than resolving it into the recommended option — RAT1, and under
delegation relay the re-ask to the actual human per RAT3; see `stages/stage-4.md`).
Refuse to guess project metrics or acceptance criteria — that's the exact failure this loop
exists to prevent. (Full text in `stages/stage-1.5.md`, `stages/stage-4.md`,
`stages/stage-8.md`.)

**Under delegation, these stops belong to the human, not the runner (RAT3).** If a subagent is
running this loop, every stop above **halts the subagent and returns to its orchestrator as a
human-gate question to relay verbatim** — the subagent does not self-answer or proceed (this half
is enforced here). The orchestrator is expected to **relay to the actual human and relay the
verbatim answer back, never answering as the owner** — a **caller-side** obligation the loop
cannot itself enforce (full statement + the enforceability split in `METHODOLOGY.md`
"Human-in-the-loop"; a fidelity ratification additionally needs the owner's verbatim words +
durable source per `stages/stage-3.md` RAT1).

## Self-check / dogfooding

This skill can be run on its own artifacts: treat `METHODOLOGY.md` + `SKILL.md` + the `stages/`
files as the thing under review, and execute a stage-3 red-team on them (cold subagent, five
lenses, evidence discipline). Skill-file edits are edits to a **position-sensitive assembly**
(these documents are prompts), so the position lens applies. **Non-trivial edits take the full
loop**, not a stage-3 pass alone. Standing self-check criteria for any such run: live copy ==
source copy (`diff`); SKILL.md ↔ METHODOLOGY.md ↔ stage-file consistency on every rule stated in
more than one place; a behavior-preservation criterion for anything moved or removed (see
`stages/stage-1.5.md`). A stage-3 red-team remains the cheap check encouraged after any edit,
however small.
