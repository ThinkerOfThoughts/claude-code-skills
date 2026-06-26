---
name: dragonfly
description: A gated, self-checking loop for DIAGNOSING bugs — no diagnostic conclusion is accepted without an independent cold-subagent red-team, and "found the bug" is proven by reproduce-on-demand + a causal toggle, never declared. Use when tracking down a bug, glitch, or unintended behavior whose cause is unknown. Sibling of guarded-change (which makes the fix); project specifics come from a per-project config. Proactively SUGGEST this whenever a bug/unintended behavior with an unknown cause is mentioned.
---

# Dragonfly

Execute the gated diagnosis loop defined in `METHODOLOGY.md` (read it in full before running — it
is the authoritative spec; this file is the operating procedure). The loop's purpose: **no
diagnostic conclusion reaches "accepted" without an independent challenge, and "found the bug" is
proven by reproduce-on-demand + a causal toggle.** Dragonfly *finds* the root cause; **guarded-change**
*makes* the fix.

## Inputs

- **The bug report** — the symptoms as the user states them (and any repro steps they know).
- **A project config** (Layer 2). Look for one (e.g. `dragonfly.*.{md,yaml}` in or near the working
  dir). If none exists, ask for it or help author it against the config contract in `METHODOLOGY.md`.
  Do not invent project specifics (paths, how to reproduce, redteam_context).

## Before you start: cold-start guard

If this is invoked inside an already-long or visibly thrashing session, **recommend a fresh
session first** and emit a carry-over brief pointing at the hunt's files — the frozen symptom
ledger, the observation ledger to date, `hypotheses.md`, and `decisions.md` (the cap's bounce-count
+ prior findings), not just the symptoms — prior context loss/thrash poisons the hunt.

## Procedure

Create a hunt folder `hunts/<slug>/` and maintain the ledgers as **files** there (`symptom-ledger.md`,
`observation-ledger.md`, `hypotheses.md`; `diagnosis.md` at stage 8; `decisions.md` throughout).
**Step numbers below are the canonical stage numbers** used in METHODOLOGY and `decisions.md`. At
every gate, append to `decisions.md`: the gate, worst severity, route taken, and a rationale+name
for any human override. Then walk the loop:

**0a. Translation** — restate the user's reported symptoms in precise technical terms as numbered
   items `S1, S2, …`; capture user-provided repro steps as `R1, R2, …`. **Show the numbered
   restatement back to the user and get confirmation/correction before proceeding** (stop-for-human).
**0b. Freeze** — write the original wording + confirmed restatement into `symptom-ledger.md`. The
   symptom set is frozen; a symptom is struck only with a recorded reason.
**1. Reproduction** — turn `R#` into a reliable, **representative** repro **before** hypothesizing.
   Apply the **representativeness gate** (below) to the repro itself: a repro that doesn't
   demonstrably reproduce a named `S#` is not a repro. Intermittent → instrument-to-capture (which
   carries its own evidentiary bar — it is not an escape from the gate). The repro is a diagnostic
   artifact → **triage** it.
**2. Observation ledger** — record everything examined in `observation-ledger.md` (append-only):
   what / observation / citation (file:line, log row) / what it rules in or out. **Do not
   re-examine an area without first recording why the prior finding is insufficient.**
**3. Hypotheses** — in `hypotheses.md`, a ranked list, each **falsifiable**: the observation that
   would confirm it AND the one that would refute it; status open/confirmed/refuted. No hypothesis
   without a discriminating test.
**4. Discriminating test (gated)** — design a test/instrument that splits the live hypotheses.
   Before running it: pass the **representativeness gate** and the **triage**.
**5. Run & record** — run; record the result in the observation ledger; update hypothesis statuses;
   cite the evidence.
**6. Convergence gate** — are we eliminating hypotheses? **Iteration cap**: after `N` cycles with
   no hypothesis eliminated (or `N` re-examinations of one area), **stop and escalate to a human**.
   `N` comes from the config (Layer-1 default **3**); if no `N` is resolvable, refuse to start.
**7. Root-cause confirmation** — declare "found" only with **all three**: (a) reproduce-on-demand;
   (b) a cited causal chain root→symptom; (c) a **toggle** (flipping the cause makes the symptom
   appear/disappear predictably). **Cold red-team the causal chain** here directly (at stages 1 & 4
   the cold pass happens via triage; stage 7's is explicit — see below). The toggle is a diagnostic
   artifact → triage.
**8. Handoff** — write `diagnosis.md` (root cause, causal chain, evidence, repro, recommended fix)
   and hand to **guarded-change** to make the fix. **Do not author the fix yourself.**
**9. Fix verification** — verify the **root cause is resolved**, not merely the symptom suppressed
   (causality runs cause→symptom; a masked symptom is not a fixed bug):
   - **9a Local** (if testable): using the stage-7 chain + toggle, check **both** the cause
     condition is gone **and** the symptom is gone. *Cause+symptom gone* → 9b. *Symptom gone but
     cause still active* → masking → back to **guarded-change**. *Symptom persists* → record
     `"fix F did not resolve S#"` → back to **stage 0** (do not adjudicate the fix's code fidelity).
   - **9b Live** (always when not locally testable, and after a local pass): the **user** runs it.
     *Confirmed resolved* → **done**. *Not resolved* → record → back to **stage 0**.

## The representativeness gate (mandatory, blocking, non-waivable)

A diagnostic artifact (stage-1 repro or stage-4 test) is **untrusted until a control run is shown
to actually exhibit the symptom.** Reject and redesign any whose control does not. The
instrument-to-capture path for intermittent bugs satisfies this differently (the instrument must be
shown to capture the symptom on a known occurrence) — it does not bypass it. This is the cheapest
catch for the founding failure (a test that doesn't test the thing); it is not waivable.

## Diagnostic-artifact triage (every repro/test/instrument/toggle)

Run each through guarded-change before trusting it, in priority order:
1. **Consumes tokens/credits to run** (agent/CLI/LLM-API call) → **full guarded-change** (overrides
   size — a wrong token-burning test is expensive twice).
2. Else multi-file / mutates state / non-obvious correctness → **full guarded-change**.
3. Else single self-contained read-only script (~≤50 lines, no state) → **guarded-change-lite**
   (a single cold red-team pass of the artifact — guarded-change's unchanged stage-3/6 charter,
   minus the spec/criteria/plan scaffolding — against a one-line intent + "does exactly X, exercises
   path P" criterion → fix → run).
4. In doubt → **full**.

## Cold red-team (stages 1, 4, 7)

A **cold subagent** (`general-purpose` or `Explore`, no shared context) challenges the artifact +
the priority-ordered `redteam_context`. **At stages 1 and 4 this happens via the triage** (the
guarded-change/lite pass each repro/test is routed through *is* its cold review); **at stage 7 you
spawn one directly** for the causal chain. Reuse guarded-change's four-lens charter + evidence
discipline (see `guarded-change/METHODOLOGY.md`), aimed at: *does the test reproduce the named
symptom or a neighbor? are any identifiers/paths/calls confabulated? does the causal chain follow
from the cited evidence?* Spot-verify a sample of the reviewer's cited file:lines exist. Route by
the severity model.

## Stop-for-human rules

Stop and ask when: the **0a restatement needs confirmation**; a **blocker** is about to restart the
loop; the **convergence gate fires**; **stage 9b live verification** is needed (the user is the
final authority on "resolved"); or **config is missing**. Refuse to invent project specifics —
that is the failure this loop exists to prevent.

## Self-check / dogfooding

This skill can be run on its own artifacts: treat `METHODOLOGY.md` + `SKILL.md` as the thing under
review and run a cold stage-3-style red-team on them (four lenses, evidence discipline). The
behavioral test that matters most: on a seeded fixture bug whose *obvious* test is
non-representative, an agent following Dragonfly must **refuse to trust that test** until a control
exhibits the symptom — proven against a no-Dragonfly baseline that falls for the trap.
