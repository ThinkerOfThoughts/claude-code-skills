---
name: dragonfly
description: A gated, self-checking loop for DIAGNOSING bugs — no diagnostic conclusion is accepted without an independent cold-subagent red-team, and "found the bug" is proven by reproduce-on-demand + a causal toggle, never declared. Use when tracking down a bug, glitch, or unintended behavior whose cause is unknown. Sibling of guarded-change (which makes the fix); project specifics come from a per-project config. Proactively SUGGEST this whenever a bug/unintended behavior with an unknown cause is mentioned.
---

# Dragonfly

The gated diagnosis loop's purpose: **no diagnostic conclusion reaches "accepted" without an
independent challenge, and "found the bug" is proven by reproduce-on-demand + a causal toggle.**
Dragonfly *finds* the root cause; **guarded-change** *makes* the fix. This file is the **router**:
each stage's full procedure + the rules that govern it live in `stages/`. `METHODOLOGY.md` is the
orientation/reference spec (why it exists, the config contract, what a run produces).

## Inputs

- **The bug report** — the symptoms as the user states them (and any repro steps they know).
- **A project config** (Layer 2). Look for one (e.g. `dragonfly.*.{md,yaml}` in or near the working
  dir). If none exists, ask for it or help author it against the config contract in `METHODOLOGY.md`.
  Do not invent project specifics (paths, how to reproduce, `redteam_context`). **Validate config paths
  at hunt start:** dead/unresolvable → stop; adaptable → adapt + record + proceed.

## Before you start: cold-start guard

If this is invoked inside an already-long or visibly thrashing session, **recommend a fresh session
first** and emit a carry-over brief pointing at the hunt's files — the frozen symptom ledger, the
observation ledger to date, `hypotheses.md`, and `decisions.md` (the cap's bounce-count + prior
findings), not just the symptoms — prior context loss/thrash poisons the hunt.

## Loop

Create a hunt folder `hunts/<slug>/` and maintain the ledgers as **files** there (`symptom-ledger.md`,
`observation-ledger.md`, `hypotheses.md`; `diagnosis.md` at stage 8; `decisions.md` throughout).
**Step numbers below are the canonical stage numbers** used everywhere (METHODOLOGY, `decisions.md`).
At every gate, append to `decisions.md`: the gate, worst severity, route taken, and a rationale+name
for any human override — the iteration cap reads this log. Walk the loop; **at each stage, read that
stage's file for the full procedure + the rules it must apply:**

| # | Stage — one-line purpose | Read |
|---|---|---|
| **0a** | Translation: restate symptoms as `S#`/repro as `R#`; confirm with the user | → `stages/stage-0a.md` |
| **0b** | Freeze: write the confirmed set into the append-only symptom ledger | → `stages/stage-0b.md` |
| **1** | Reproduction: a reliable, *representative* repro before hypothesizing | → `stages/stage-1.md` (+ `stages/charter.md`) |
| **2** | Observation ledger: append-only record of everything examined | → `stages/stage-2.md` |
| **3** | Hypotheses: ranked, falsifiable, each with a gate marker | → `stages/stage-3.md` |
| **4** | Discriminating test (gated): splits the live hypotheses | → `stages/stage-4.md` (+ `stages/charter.md`) |
| **5** | Run & record: log the result, update statuses, cite | → `stages/stage-5.md` |
| **6** | Convergence gate: are we eliminating hypotheses? iteration cap | → `stages/stage-6.md` |
| **7** | Root-cause confirmation: reproduce + chain + toggle, cold-red-teamed | → `stages/stage-7.md` (+ `stages/charter.md`) |
| **8** | Handoff: emit `diagnosis.md` → guarded-change makes the fix | → `stages/stage-8.md` |
| **9** | Fix verification: the root cause is resolved, not just the symptom | → `stages/stage-9.md` |

The **most important gate is the representativeness gate** (governs stages 1 and 4): a diagnostic
artifact is untrusted until a control run is shown to exhibit the symptom. It is the cheapest catch for
the founding failure — a test that doesn't test the thing. The **diagnostic-artifact triage** routes
every repro/test/instrument/toggle/detector through guarded-change (lite or full) before it is trusted.
The **iteration cap** (config `N`, default 3) stops thrash: `N` cycles with no hypothesis eliminated →
escalate to a human.

## Stop-for-human

Pause and ask when: the **0a restatement needs confirmation**; a **blocker** is about to restart the
loop; the **convergence gate fires**; **stage-9b live verification** is needed (the user is the final
authority on "resolved"); a **characterized ending** needs its sign-off; **config is missing**; or
**config paths are dead/unresolvable** at hunt start (adaptable → adapt + record + proceed). Refuse to
invent project specifics. And **never describe a hypothesis as the root cause** without its stage-7
`cold-red-teamed` pass, nor as the **leading candidate** before its discriminating test is cold-reviewed
(`test-passed`); an ungated hypothesis is presented only as a **candidate** (see `stages/stage-3.md`
"the gate-before-present rule"). Ranking the candidate list is always fine.

## Self-check / dogfooding

This skill can be run on its own artifacts: treat `METHODOLOGY.md` + `SKILL.md` + the `stages/` files as
the thing under review and run a cold stage-3-style red-team on them (four lenses, evidence discipline).
These files are **prompts** (position-sensitive): **non-trivial edits to either take the full
guarded-change loop.** Standing criteria after any edit to these files: live == source (`diff`);
SKILL ↔ METHODOLOGY ↔ stage-file consistency on every shared rule; behavior-preservation for anything
moved/removed. (Dragonfly's charter/severity/rubric/lite are now its **own** — `stages/charter.md`,
forked from guarded-change; there is no live cross-reference to keep resolving.) The flagship test
(**aspirational — not yet run** — an unrun check may not be described as an existing safeguard; a
standing replayable probe once run): on a seeded fixture bug whose *obvious* test is non-representative,
an agent following Dragonfly must **refuse to trust that test** until a control exhibits the symptom.
