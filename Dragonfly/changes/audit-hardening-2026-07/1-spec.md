# 1 — Spec: dragonfly audit-hardening-2026-07

## Problem

A Fable-5 audit of the dragonfly skill (`0-audit-findings.md`) found 14 rule gaps
(D-1..D-14), each evidenced either by a loophole in the text or by a situation the skill's
one real-world performance record — the monologue-bleed/memory-gap hunt — had to handle ad
hoc because no rule existed: author-summarized cold passes (D-1), an improvised
"characterized, not found" ending (D-2), an uncountable convergence gate (D-3), an
ungoverned symptom detector (D-4), unfalsifiable toggle/verification for intermittent
symptoms (D-5), unvalidated config (D-6), broken multi-symptom accounting (D-7), a
silently-inverted repro-first rule (D-8), unauditable lite passes (D-9), a weaker self-check
with an unrun flagship test (D-10), unchecked by-reference coupling to guarded-change
(D-11), nobody challenging the hypothesis-space (D-12), a stage-7 bar satisfiable at a
proximate node (D-13, user-observed), and no evidence-coverage sweep before "found" (D-14,
user-observed).

## Why

Two of these (D-13/D-14) directly reproduce failures the user caught by hand in the
context-bloat hunt — Opus was prepared to accept a relay as the root and to absorb
unexplained ledger rows. The rest close the gap between what the hunt actually needed and
what the skill mandates, so the next hunt doesn't depend on ad-hoc discipline.

## Constraints

- **Additive only.** Strengthen in place; nothing moved/removed beyond in-place sentence
  extensions. D-S1..S3 are flagged for owner sign-off, not built.
- **Opus-mechanical.** Rules must be explicit, countable, checkable from the logs; terse —
  the attention budget (D-S1) is real.
- **Dependency:** D-1/D-9/D-11 assume the guarded-change `audit-hardening-2026-07`
  amendments (landed at `9cec23d`): dragonfly inherits charter/severity/provenance by
  reference. This run verifies the references resolve (C3).
- Live copy (`~/.claude/skills/dragonfly/`) is updated only at stage 8 (post-gate-7),
  mirroring AR-7.

## Touched files (expected)

- `Dragonfly/METHODOLOGY.md` (441 lines at base `9cec23d`)
- `Dragonfly/SKILL.md` (129 lines at base `9cec23d`)

(No config/companion/README edits: D-6 adds validation RULES to the methodology; the
per-project companion file is data, not rules.)
