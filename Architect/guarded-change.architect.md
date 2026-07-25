# guarded-change config — authoring the Architect skill (Layer-2)

Greenfield authoring run: build the `architect` skill from the approved scope/decision record.
No prior version → **no stage-0 baseline; stage 8 runs conformance-only.** Acceptance criteria are
authored per-change in `1.5-criteria.md`, seeded from the approved plan's **Verification** section.

```yaml
project: architect

redteam_context:            # priority-ordered; a cold reviewer reads these to check claims vs. source
  - path: /home/zero/.claude/plans/1-this-is-a-proud-scott.md
    note: THE APPROVED SCOPE/DECISION RECORD — source of truth for every settled decision, the
          plan-artifact spine, the on-disk layout, the recursion/orchestration model, and the
          Verification list that seeds the criteria. Any spec/criteria/plan claim is checked here first.
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Guarded_change
    note: PRIMARY architectural model to mirror — SKILL.md (router) + METHODOLOGY.md (Layer-1 core /
          Layer-2 config contract) + stages/ (house style) + stages/charter.md (the shared red-team,
          five lenses + earned-clean discipline). Latest on this branch (RAT guards + Fidelity lens).
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Dragonfly
    note: The charter-FORK precedent (its stages/charter.md forks guarded-change's unconditional core
          via a provenance blockquote) + stage-file house style + mnemonic rule-IDs as the cross-file
          linking mechanism. Architect forks its charter the same way and adds a Completeness lens.
  - path: /home/zero/Desktop/claude-code-skills/Data-Distiller
    note: Closest precedent (a gated multi-agent skill authored via guarded-change). Its per-corpus
          Layer-2 config shape, blind-router/static-pyramid orchestration, disk-as-instrumentation
          restart contract, and human cut-gate are the patterns Architect adapts (recursive
          orchestration; top-level-only human decomposition gate). Its SKILL/METHODOLOGY are freshly
          built and may be mid-build — treat its `changes/…/{2-plan,1.5-criteria}.md` as the stable
          decision record.
  - path: /home/zero/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/
    note: skill-creator — scaffold + validate/package. Frontmatter constraints the build must satisfy:
          name kebab-case (`architect`, <=64 chars); description <=1024 chars, NO angle brackets,
          deliberately "pushy" for triggering; allowed frontmatter keys only
          {name, description, license, allowed-tools, metadata, compatibility}. Used INSIDE the loop
          to scaffold + run quick_validate.py / package_skill.py — not as a separate freehand step.
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect
    note: The artifact under construction — the build output (SKILL.md, METHODOLOGY.md, stages/,
          charter.md, templates/, examples/). Empty at run start except this config + the changes/ folder.

measurement:
  # baseline: omitted — greenfield, no prior version. Stage 8 is conformance-only.
  check:                    # REQUIRED for stage 8
    how: |
      Conformance = structural validation + a dogfood dry-run against the 1.5 criteria:
      (1) `python quick_validate.py Architect` passes (valid frontmatter, allowed keys, name/description
          constraints);
      (2) SKILL.md <-> METHODOLOGY.md <-> stage-file consistency on every rule stated in more than one
          place (mnemonic-ID cross-file check);
      (3) the router's stage table resolves to real stage files; charter fork-provenance blockquote present;
      (4) a dogfood dry-run: walk the built skill on a tiny fabricated planning task AND on the
          founding-failure fixture (a plan draft with the output-folder section removed) and confirm the
          completeness-critic pass flags the missing output-location section before the plan is presentable.
      Gating criteria that cannot be verified pre-ship by a representative dry-run are surfaced to the human
      (orchestrator), never silently deferred.
    output: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/changes/initial-authoring-2026-07/8-harness.md

metrics: []                 # greenfield / conformance-only — no standing regression metrics yet
```

**Notes**
- **Criteria are mandatory; baseline optional.** The `1.5-criteria.md` seeds from the approved plan's
  Verification list (founding-failure gate, two-pass total coverage, scale-down, scale-up + top-level human
  gate, template reuse + back-propagation, context-economy + recursive-orchestration + restart, skill
  self-check). Each labeled gating/advisory with a reason and an oracle-can-fail self-test where behavioral.
- **The artifact is a position-sensitive prompt assembly** (these files are prompts). The position lens
  applies; non-trivial edits take the full loop; standing self-check criteria apply (live==source,
  cross-file rule consistency, behavior-preservation N/A greenfield).
- **Delegation (RAT3).** This loop is executed by a subagent with the main session as orchestrator. Every
  stop-for-human HALTS the subagent and returns the question verbatim to the orchestrator to relay to Roy —
  the subagent never self-answers or proceeds past a stop.
