# guarded-change config — Data-Distiller authoring

Layer-2 config for running the `guarded-change` loop to AUTHOR the Data-Distiller skill.
This is a **greenfield** change (no prior version) → stage 0 baseline is skipped; stage 8 runs
**conformance-only**. Acceptance criteria are per-change and live in the change's `1.5-criteria.md`
(seeded from the approved plan's Verification checklist — see redteam_context #1).

```yaml
project: data-distiller (skill authoring)

redteam_context:            # priority order — cold reviewer reads these to check claims vs source
  - path: /home/zero/.claude/plans/your-understanding-is-correct-wise-bee.md
    note: APPROVED PLAN — source of truth for spec/criteria/plan + the settled design decisions.
          The build must conform to this; owner-approved decisions are NOT to be re-litigated.
  - path: /home/zero/Desktop/Dragonfly_Case_study/T1-T4_Results/DISTILLATION-METHOD-ISSUES-LOG.md
    note: the load-bearing gotchas each = a guardrail the skill must encode (persona-guard read-only
          trip; OOM streaming slimmer; guard-doesn't-catch-reads; delegation/restart/stale-edit/pacing).
  - path: /home/zero/Desktop/Dragonfly_Case_study/T1-T4_Results/AGENT_BRIEFS.md
    note: the brief templates actually used (analysis/verify/merge/summary + shared artifact-context
          block + global do-the-work rule + read-only clause) — to port into stages/brief templates.
  - path: /home/zero/.claude/skills/guarded-change/
    note: architecture to MIRROR — SKILL.md router + METHODOLOGY.md (Layer-1/Layer-2 + config contract)
          + stages/ + charter.md. Fork charter.md from here (as dragonfly did).
  - path: /home/zero/.claude/skills/dragonfly/
    note: second architecture exemplar (per-stage stages/, companion config example, README).
  - path: /home/zero/Desktop/Dragonfly_Case_study/T1-T4_Results/
    note: orchestration/state exemplars (PROGRESS.md, RESUME.md, test_index.md) + example deliverables
          (T*_summary.md, raw_findings/*_superlist.md) — for the state-contract + brief/summary shapes.
          READ-ONLY: never mutate anything under Dragonfly_Case_study/.

measurement:
  # greenfield — no baseline block
  check:                    # REQUIRED for stage 8; conformance-only
    how: |
      Conformance check against 1.5-criteria.md (seeded from the plan's Verification checklist):
      (a) STRUCTURE — SKILL.md/METHODOLOGY.md/stages/charter/brief-templates/example-config all present
          and internally consistent (every rule stated in >1 place agrees); live copy == source (diff
          ~/.claude/skills/data-distiller vs repo Data-Distiller).
      (b) DOGFOOD DRY-RUN — walk the skill against a tiny fabricated synthetic corpus and confirm the
          six plan criteria are demonstrable: blindness (coordinator/interior transcripts hold no
          findings content), deterministic restart (kill mid-stage → resume, no rework), agreement
          renders `PCT% (X/N)` sorted by percentage then recurrence, size-strategy routing (binary-bulk
          → tag-replace; text-bulk → subdivide), human cut-gate fires on a subdivided item, concurrency
          never exceeds the static budget.
    output: Data-Distiller/changes/initial-authoring-2026-07/8-harness.md

metrics: []                 # greenfield, conformance-only — no standing regression metrics yet
```

Notes:
- **Criteria are mandatory** and are authored in `1.5-criteria.md` from the plan's Verification section
  (6 items), each labeled gating/advisory. No baseline → stage 8 says "conformance-only".
- **Read-only corpus:** the T1–T4 archive is reference only; the build never writes under
  `Dragonfly_Case_study/`. The skill's own output goes in `Data-Distiller/`.
