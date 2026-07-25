# guarded-change config — the Architect skill (Layer-2)

**Run 1 (`changes/initial-authoring-2026-07/`) — greenfield authoring:** build the `architect` skill
from the approved scope/decision record. No prior version → **no stage-0 baseline; stage 8 ran
conformance-only.**

**Run 2+ (`changes/hardening-cycle-1/` onward) — NOT greenfield.** The artifact exists and is committed,
so **a stage-0 baseline exists and is required**: the baseline is the *current committed behavior of the
rules being touched* (see `baseline:` below). Acceptance criteria are authored per-change in
`1.5-criteria.md`.

```yaml
project: architect

redteam_context:            # priority-ordered; a cold reviewer reads these to check claims vs. source
  - path: /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
    note: HARDENING RUNS ONLY — THE FINDING SET UNDER REPAIR, and the source of truth for what each fix
          must accomplish. Consolidated + triaged output of the 2026-07-24 dogfood of Architect on its
          own creation plan. Every hardening spec/criteria/plan claim about "what the finding says" is
          checked HERE FIRST. Also read for the triaged-NOT-genuine list: re-fixing a refuted finding
          (e.g. "nested spawn may be impossible") is itself a fidelity error.
  - path: /home/zero/architect-hardening-loop/LOOP-STATE.md
    note: HARDENING RUNS ONLY — the loop's durable state: the owner's verbatim directive, the cycle
          scope, the orchestrator calls made within it, and the OWNER QUESTIONS QUEUED (F8 — whether a
          human must review the assembled plan). A hardening run that implements or pre-shapes F8 is
          out of scope; check any human-gate claim against this file.
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
    note: THE ARTIFACT UNDER CHANGE — SKILL.md, METHODOLOGY.md, stages/, stages/charter.md, templates/,
          examples/, README.md. Run 1: empty at start (build output). Run 2+: the COMMITTED artifact is
          the stage-0 baseline; read it to check any claim about what the skill currently says, and
          `git show <base>:Architect/<f>` for the pre-change text. `changes/initial-authoring-2026-07/`
          is the FROZEN authoring record (criteria + fixture style to reuse) and is never edited by a
          later run.

measurement:
  baseline:                 # RUN 1: omitted (greenfield). RUN 2+: required — the artifact exists.
    how: |
      The artifact is a PROMPT ASSEMBLY, so the baseline is TEXTUAL, not a metric run. Capture, at the
      commit the change starts from (recorded in 0-baseline.md):
      (1) the frozen tree, recoverable as `git show <base>:Architect/<file>` — no prose copy needed;
      (2) the rule-ID -> site map, `grep -now -- <ID>` over SKILL.md METHODOLOGY.md stages/ templates/
          examples/ README.md for every mnemonic rule ID. WORD BOUNDARIES ARE MANDATORY: a bare
          `grep -o TOP` matches inside HARDSTOP and manufactures phantom sites;
      (3) the operative claim, per rule the change intends to touch, with a file:line citation, and
          whether the change intends to PRESERVE or CHANGE it.
      Regression for this artifact therefore means: a baseline rule that stops being stated, or starts
      being stated inconsistently, at a site the change did not intend to alter.
    output: Architect/changes/<slug>/0-baseline.md
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
      RUN 2+ ADDS, because the artifact now exists and the change is a rule-set edit:
      (5) the structural checker `changes/<slug>/oracles/check.sh` — a POSITIVE PER-SITE ASSERTION per
          criterion (the rule is stated at each site that must state it), with any absence sweep PAIRED
          with its positive assertion and run on NORMALIZED text (strip emphasis markers, flatten wraps);
      (6) its oracle-can-fail self-test `oracles/baseline-replay.sh` — run the SAME checker against the
          baseline tree materialized from git: every new-rule assertion MUST FAIL there and every
          preserved-rule assertion MUST PASS. A checker that passes the baseline is not an oracle;
      (7) the regression pair: R1 site-set non-erosion + R2 deliberate-change completeness (0-baseline.md);
      (8) the behavioral arms: per behavioral criterion, TWO separately-spawned cold agents (holed arm +
          intact twin) each handed ONLY its own fixture + the relevant new stage text. Both arms
          returning the same verdict = `verified = no`, whichever verdict it is.
    output: Architect/changes/<slug>/8-harness.md          # per-run; run 1 = initial-authoring-2026-07

metrics: []                 # no standing numeric regression metrics — the baseline is TEXTUAL (see above)
```

**Notes**
- **Criteria are mandatory; baseline optional in general — but REQUIRED from run 2 on** (the artifact
  exists). Run 1's `1.5-criteria.md` seeded from the approved plan's Verification list (founding-failure
  gate, two-pass total coverage, scale-down, scale-up + top-level human gate, template reuse +
  back-propagation, context-economy + recursive-orchestration + restart, skill self-check). A hardening
  run seeds instead from the finding set in `redteam_context[0]` — one criterion family per finding. Each
  labeled gating/advisory with a reason and an oracle-can-fail self-test where behavioral.
- **The artifact is a position-sensitive prompt assembly** (these files are prompts). The position lens
  applies; non-trivial edits take the full loop; standing self-check criteria apply (live==source,
  cross-file rule consistency, and — **from run 2 on, no longer N/A** — behavior-preservation for
  anything moved or removed, against the stage-0 baseline).
- **Mnemonic rule-IDs are the cross-file linking mechanism.** A new ID must be a standalone uppercase
  token that is not a substring of another ID or of an ordinary corpus word, and must get a row in
  METHODOLOGY's cross-file rule index. Check ID sites with **word-boundary** matching.
- **Delegation (RAT3).** This loop is executed by a subagent with the main session as orchestrator. Every
  stop-for-human HALTS the subagent and returns the question verbatim to the orchestrator to relay to Roy —
  the subagent never self-answers or proceeds past a stop.
