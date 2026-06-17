---
name: guarded-change
description: A gated change loop where no AI artifact is accepted without an independent cold-subagent red-team, and "done" is proven against measurable criteria. Use when making any non-trivial change (code, plan, or design) and you want spec→plan→red-team→build→red-team→harness discipline. Project specifics come from a per-project config; the loop itself is domain-agnostic.
---

# Guarded Change

Execute the gated change loop defined in `METHODOLOGY.md` (read it in full before running —
it is the authoritative spec; this file is the operating procedure). The loop's purpose:
**no AI-produced artifact reaches "accepted" without an independent challenge, and "done" is
proven against an explicit measurable bar.**

## Inputs

- **The change request** (from the user, or — when self-checking — a named artifact).
- **A project config** (Layer 2). Look for one (e.g. `guarded-change.*.{md,yaml}` in or near
  the working dir). If none exists and the loop needs stage 0/8, ask for it or help author it
  against the config contract in `METHODOLOGY.md`. Do not invent project metrics.

## Procedure

Create a change folder `changes/<slug>/` and produce one doc per stage (names in
METHODOLOGY "What a run produces"). **Step numbers below are the canonical stage numbers used
everywhere (METHODOLOGY loop, severity table, decisions.md).** At every **gate (stages 4, 7,
8)**, append a line to `changes/<slug>/decisions.md`: gate (by stage number), worst severity,
route taken, and a rationale+name for any human override. The iteration cap reads this log to
count same-gate bounces (keyed by stage number) and carry prior findings into the next review.
Then walk the loop:

**0. Baseline** — only if a prior version exists *and* the config defines `measurement.baseline`.
   Run it, store metrics in `0-baseline.md`. Otherwise note "greenfield / no baseline → stage 8
   conformance-only" and skip.
**1. Spec** — write `1-spec.md`: the problem, why, constraints. Rich enough to derive the rest.
**1.5. Criteria** — write `1.5-criteria.md`: a *checkable* accept bar. Each criterion is either
   **automated** (true/false or numeric from instrumentation) **or** a **human-judged rubric**
   (named judge + written scale + pass definition) — see METHODOLOGY stage 1.5. **Mandatory.**
   If you cannot state checkable criteria in *either* form, stop and resolve with the user — the
   loop may not pass stage 3 without them.
**2. Plan** — write `2-plan.md`: how, **plus** measurement, instrumentation (add to scope if a
   needed signal is absent), and severity→routing thresholds + which metrics are gating vs.
   advisory. A plan missing these is incomplete.
**3. Red-team the plan** — spawn a **cold subagent** (no shared context; `general-purpose` or
   `Explore`). Give it read access to `{1-spec, 1.5-criteria, 2-plan}` AND the priority-ordered
   `redteam_context` paths. Charter it with the four lenses + evidence discipline from
   METHODOLOGY ("The red-team charter"): cite line/file or a concrete scenario, rank each finding
   (blocker/major/minor/nitpick), flag anything unverifiable, "no issue" per lens allowed; a
   clean *factual* verdict needs source citations. Write `3-redteam-plan.md`.
**4. Gate** — route by worst finding: **blocker → return to 1** (confirm direction first);
   **major → return to 2**; **minor → fix in place, proceed**; **nitpick → log, proceed**;
   **clean → build (5).** Bounded by the iteration cap (below).
**5. Build** — implement per the plan, including any instrumentation the plan added.
**6. Red-team the code** — spawn a fresh **cold subagent** with the code diff/files + `{1.5, 2}` +
   `redteam_context`. Same charter, aimed at code-vs-plan/criteria. Spot-verify a sample of the
   reviewer's cited file:lines actually exist (guards fabricated citations). Write `6-redteam-code.md`.
**7. Gate** — **blocker/major → return to build (5)**; **minor → fix in place, proceed**;
   **nitpick → log, proceed**; **clean → harness (8).**
**8. Harness** — run the config's `measurement.check`. Then:
   - **Conformance (always):** measured behavior vs. `1.5-criteria.md`. Pass/fail per criterion.
   - **Regression (only if a stage-0 baseline exists):** measured vs. baseline on the config
     `metrics`, applying each metric's `direction` + `regression_threshold`.
   Apply each metric's gating-vs-advisory status (advisory metrics are surfaced, not bounced —
   see METHODOLOGY "Regression must be measured on a comparable workload"). Write `8-harness.md`
   with a verdict. **Blocker → return to 1.** A **major** is a human call — restart at 1 *or*
   re-plan at 2 (tradeoff vs. revision); surface it ranked, don't auto-route. **Minor → fix,
   proceed; clean → done.**

**Iteration cap (all gates):** after **2 bounces at the same gate (same stage number) on the
same finding class**, stop and a human breaks the tie. "Same finding class" = same gate + same
targeted artifact section, regardless of wording (so a rephrased or relocated-but-equivalent
objection still counts). See METHODOLOGY "Iteration cap".

## Stop-for-human rules

Pause and ask when: a **blocker** is about to restart the loop; a **major** appears at the
harness; or **criteria/config are missing**. Refuse to guess project metrics or acceptance
criteria — that's the exact failure this loop exists to prevent.

## Self-check / dogfooding

This skill can be run on its own artifacts: treat `METHODOLOGY.md` + `SKILL.md` as the thing
under review, and execute a stage-3 red-team on them (cold subagent, four lenses, evidence
discipline). That is the cheapest validation the methodology gets and is encouraged after any
edit to either file.
