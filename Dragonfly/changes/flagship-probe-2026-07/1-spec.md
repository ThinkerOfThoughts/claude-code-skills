# 1 — Spec: run the D-10 flagship test once (aspirational → standing probe)

**What:** Execute, for the first time ever, the flagship test named in dragonfly's
self-check (SKILL:146-149): *"on a seeded fixture bug whose obvious test is
non-representative, an agent following Dragonfly must refuse to trust that test until a
control exhibits the symptom — proven against a no-Dragonfly baseline that falls for the
trap."* The 2026-07 hardening run relabeled it "**aspirational — not yet run**" (D-10);
its own text says it becomes "a standing replayable probe once run."

**Why now:** the hardening run's 9-report.md §3 names this as the cheap follow-up; the
owner directed continuation (2026-07-04). It also samples risk-class (b) from the gate-4
risk acceptance (live, unprompted firing of the rules by an agent executing the prompt —
exactly what C8 could not observe) for the representativeness-gate slice of the skill.

**Deliverables:**
1. A **seeded fixture** (small Python project, arm-visible) + a **hidden oracle** repro
   (not arm-visible) proving the seeded symptom is real — committed as the standing
   replayable probe.
2. A **run protocol** with pre-committed arm prompts, extraction rules, and pass
   conditions (frozen before any arm runs).
3. Run records: N Dragonfly arms + N baseline arms on the production-pinned model, cold-
   scored against the frozen extraction rules.
4. **Conditional label flip** in SKILL.md, only on a probe PASS: "aspirational — not yet
   run" → standing-probe status + record pointer, **net-zero lines** (combined cap is at
   670/670). On a non-PASS outcome (probe fails or is non-discriminating), the label
   STAYS aspirational and the outcome is recorded honestly.

**Constraints:** additive discipline does not bind here (this run edits only the one
label, conditionally); the 670 combined line cap DOES bind (label flip must be net-zero).
Arms run on `claude-opus-4-8` (production runs the skills on Opus; battery precedent).
The probe artifact burns tokens → dragonfly's own triage rule 1 routes it through **full
guarded-change** — this run is that loop.

**Non-goals:** not a full behavioral battery (the hardening run's no-battery rationale
stands); not a hunt for new skill defects; no METHODOLOGY edits.
