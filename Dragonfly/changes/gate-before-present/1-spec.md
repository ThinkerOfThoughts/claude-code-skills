# 1 — Spec: close the "gate-before-present" loophole in Dragonfly

## Problem

Dragonfly's founding rule is **"nothing self-certifies"** — a diagnostic artifact is untrusted
until an independent cold pass challenges it. But the loop enforces this for **artifacts** (repros,
tests, instruments, toggles, and the stage-7 causal chain) and **not** for the thing the human
actually acts on: **a hypothesis presented as the likely cause.** There is no rule forbidding the
agent from telling the user "H-X is the leading / probable root cause" *before* H-X has passed any
cold gate. So an author-generated, self-certified hypothesis can be leaned on as a conclusion — the
exact failure the loop exists to prevent, relocated from the artifact to the narrative.

## Evidence

Memory note `dragonfly-gate-before-present-slip.md` (2026-07-02 monologue-bleed/memory-gap hunt):

- **H-S1-FILEBLOAT** was presented to the user as the **"leading"** S1 root-cause account **before
  it went through the dragonfly gates** — no cold red-team of its causal chain, no repro, no
  toggle. When finally cold-red-teamed (at the user's insistence) it was **REFUTED — BLOCKER**: its
  mechanism was dead code on the `claude-cli` provider.
- Same hunt, **H-S1-DISTANCE** — a confident-looking structural story from the agent's own
  code-reading — was likewise demolished by the cold red-team (MAJOR).
- **Two** hypotheses in one hunt, both looked "leading," both false, both from unreliable structural
  code-reasoning about an unfamiliar runtime. Had FILEBLOAT been acted on, the fix would have
  targeted dead code.
- **Secondary (trust-before-gate ordering):** `replay_search.py`'s output was **consumed at stage 5
  before its cold review**, which only arrived folded into the stage-7 red-team. The artifact's
  reading was trusted before the artifact was gated — the triage is meant to happen *before* trust,
  not retroactively.

## Why this belongs in Layer 1

"Nothing self-certifies" already covers artifacts; the hole is that a **hypothesis** (also an
author-produced artifact) is exempt from it at the exact moment it matters — when it is offered to
the human as the answer. And the loop already *has* the gates (stage-7 causal-chain red-team; the
per-artifact triage); it simply never says **"do not present a conclusion the gate hasn't cleared,"**
nor tracks, per hypothesis, whether a cold pass has happened. This is the same family as
guarded-change's own patched loopholes (deferred-gating-criterion, position-sensitivity,
shared-state-concurrency): *a gate that exists but is not required to fire before the thing is
relied upon.*

## Goal

Domain-agnostic Layer-1 additions to `METHODOLOGY.md` + `SKILL.md`:

1. **Gate-before-present rule.** A hypothesis may **not** be labeled to the human as
   "leading / likely / probable / most-likely cause" (or otherwise presented as a conclusion to act
   on) until it has passed its cold red-team. Until then it is explicitly **"candidate, ungated."**
   The user may of course be shown the ranked candidate list — ranking by plausibility is fine — but
   *rank is not endorsement*, and no candidate is described as the answer pre-gate.
2. **Per-hypothesis gate-coverage marker in `hypotheses.md`.** Extend the hypothesis record beyond
   `open/confirmed/refuted` with an explicit **gate status** — e.g. `ungated` → `test-passed`
   (its stage-4/5 discriminating test ran and was cold-reviewed) → `cold-red-teamed` (stage-7 causal
   chain passed a cold pass). "Confirmed" (the stage-7 three-part bar) requires `cold-red-teamed`.
   The marker makes "has a cold pass happened for this hypothesis?" a recorded fact, not a memory.
3. **Trust-before-gate ordering rule.** An artifact's *output/reading* may **not** be consumed by a
   later stage until the artifact's triage (representativeness gate + cold review) is **recorded as
   passed**. Gating is a precondition of trust, not a retroactive audit.

## Constraints / non-goals

- **Domain-agnostic.** No project specifics. Mirrors the existing gate/charter machinery; reuses
  its severity model and cold-pass definitions.
- **Do not gate ordinary internal reasoning.** The agent must still form and rank hypotheses freely
  and think out loud in its own working notes; the rule bites only on **presenting a hypothesis to
  the human as a conclusion / likely cause.** Ranking a candidate list is allowed and expected.
- **Proportionate**, consistent with the loop's existing stage detail; no restructuring of stages.
- **Consistency:** the new marker must not contradict the existing `open/confirmed/refuted` status
  or the stage-7 three-part "found" bar; it refines them.
- Edit **both** copies (live `~/.claude/skills/dragonfly/` + source
  `~/Desktop/claude-code-skills/Dragonfly/`), or the installed skill won't carry it.
