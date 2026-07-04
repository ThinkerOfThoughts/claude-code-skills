# 1 — Spec: audit-hardening-2026-07

## Problem

A full audit of the guarded-change skill (`0-audit-findings.md`, 2026-07-03) found nine
remaining unguarded channels, all instances of the loop's own meta-pattern — *a check existed
but was not actually exercised, or was exercised on the wrong thing, by an actor whose blind
spot it shared*:

- **F1** — the author writes the reviewer's prompt, picks its context, and transcribes its
  findings; all three channels can neuter independence invisibly (precedent: C3 attempt-1
  confound in `changes/concurrency-lens/decisions.md`).
- **F2** — anything built/modified after stage 6 (the stage-8 harness itself, route-(a)
  fixtures, in-place fixes) is trusted with zero independent review (precedent: C3 attempt-1;
  the Option-B non-representative smoke).
- **F3** — the author's stage-8 PASS claims carry no evidence obligation (reviewers must
  "cite or it doesn't count"; the verification table doesn't).
- **F4** — `1.5-criteria.md` is mutable after the gate that approved it (silent goalpost-moving).
- **F5** — the author routes gates and can silently demote a reviewer's blocker/major.
- **F6** — the reviewer's context (standing config) can miss the change's own touched files;
  the stage-6 diff is author-curated, so an omitted file is invisible.
- **F7** — no one is charged with challenging criteria *coverage* ("what could this change
  break that no criterion observes?") — hazard classes are only patched post-postmortem.
- **F8** — `redteam_context` paths are never validated at run time; a dead path silently
  degrades review to docs-only reasoning (precedent: config pointed at a deleted install).
- **F9** — the self-check section is "encouraged"-only, stage-3-only, with no standing criteria.

Full statements + proposed fixes: `0-audit-findings.md` (authoritative input).

## Why

Each past shipped miss (position-sensitivity, Option-B deferral, compaction race) was this
same shape; F1–F9 are the residual channels found by looking for siblings rather than waiting
for the next postmortem. F1/F2/F3 in particular defend the loop's two founding guarantees
(independent challenge; proven done) at points where they can currently be bypassed without
leaving a trace.

## Constraints

1. **Additive only.** No restructuring, no removals, no relocation of existing rules
   (owner decision 2026-07-03). S1–S3 in the findings doc are flagged, not built.
2. **Opus attention budget.** The executing model is Opus: edits must be terse, mechanical,
   and checkable; growth is bounded (see 1.5 C4). Prefer one-sentence rules wired into
   existing sections over new essays.
3. **Both copies.** Source (`~/Desktop/claude-code-skills/Guarded_change/`) and live
   (`~/.claude/skills/guarded-change/`) must end identical.
4. **No weakening.** No existing rule loses force; pure addition (checked by diff).

## Touched files (expected — F6 dogfooded)

- `~/Desktop/claude-code-skills/Guarded_change/METHODOLOGY.md`
- `~/Desktop/claude-code-skills/Guarded_change/SKILL.md`
- `~/.claude/skills/guarded-change/METHODOLOGY.md` (sync copy)
- `~/.claude/skills/guarded-change/SKILL.md` (sync copy)
- `changes/audit-hardening-2026-07/*` (run docs)

## Prior art

- `changes/concurrency-lens/` — the template for skill-on-itself runs, including the
  execution-verified replay criterion (C3 there) and the confounded-harness lesson.
- Memory lessons: position-sensitivity, deferred-gating, concurrency blind spot,
  spike-representativeness — the patched classes whose *generator* F7 addresses.
