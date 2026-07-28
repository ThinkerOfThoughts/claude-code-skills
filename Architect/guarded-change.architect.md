# guarded-change config — the Architect skill, ATTEMPT 2 (Layer-2)

**This file is run configuration, not skill content.** It is authored by the orchestrator and is an
*input* to the loop. Nothing in it is an Architect design decision; where it states a design fact it is
quoting `~/Documents/Architect.md` (the owner-authored spec) and is checkable there.

## The attempt-2 build model — ONE ELEMENT PER RUN

Attempt 1 tried to author the whole skill in a single guarded-change run and drowned in its own criteria
set: the *measurement apparatus* became the thing that kept failing (three hardening passes, the
iteration cap tripped twice, and three of nine blockers in one pass lived in rows a scope expansion had
created). The owner's correction, verbatim:

> "start with each element individually (charter, spine, whatever), once the thing as pieces exists, run
> the whole thing" — session transcript record **1274**

So: **one full loop per element**, each with its own spec → criteria → plan → cold red-team → gate →
build → cold red-team → gate → harness. Elements in dependency order:

| # | Element | Run folder | Status |
|---|---|---|---|
| 1 | **The red-team charter** | `changes/charter-2026-07/` | **current run** |
| 2 | The 7-section plan spine (`templates/seed/`) | `changes/spine-2026-07/` | not started |
| 3 | The Layer-2 config contract | — | not started |
| 4 | The router (`SKILL.md`) | — | not started |
| 5 | The methodology/reference doc | — | not started |
| 6 | Whole-skill assembly run | — | not started |

**Greenfield-with-a-fork-source.** No prior *accepted* Architect artifact exists — attempt 1 is archived
at `Architect-Attempt-1/` and is **not** a baseline (it was demolished as unsound, see `README.md`). But
the charter is a declared **fork**, so a baseline does exist for it: the fork source. See `baseline:`.

```yaml
project: architect
run: charter-2026-07

redteam_context:            # priority-ordered; a cold reviewer reads these to check claims vs. source
  - path: /home/zero/Documents/Architect.md
    note: THE AUTHORITATIVE DESIGN SPEC — owner-authored pseudocode for the whole skill, single copy,
          deliberately NOT duplicated into the repo. Every claim about what Architect does, what the
          charter's callers are, what the granularity floor bounds, what Consensus/Union/Severity do, and
          how the loop terminates is checked HERE FIRST. Read `Spawn_redteam` and `Divisible` in
          particular — they are the charter's two callers. If the artifact under review disagrees with
          this file, this file wins and the disagreement is a finding.
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Guarded_change/stages/charter.md
    note: THE FORK SOURCE and the stage-0 baseline for this run. Architect's charter declares itself a
          fork of this file @ 8d73e5d (sha256 0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590,
          verified 2026-07-28; the file is unchanged at HEAD). Its provenance blockquote claims it carries
          "the five lenses, every unconditional discipline bullet, and the two conditional lenses." That is
          a CHECKABLE CLAIM — verify it rule by rule against this file. A carried rule that silently
          stopped being stated is a regression; a rule dropped ON PURPOSE must say so in the provenance
          blockquote (the Dragonfly precedent, below, shows the shape).
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Dragonfly/stages/charter.md
    note: THE FORK PRECEDENT — the house shape of a provenance blockquote that names its source commit and
          states explicitly what was carried and what was "deliberately not carried." Architect's must
          meet this bar.
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/charter.md
    note: THE ARTIFACT UNDER CHANGE — but read the banner: it is an **UNVETTED DRAFT with NO standing**,
          hand-written freehand in the main session outside this loop and never cold-reviewed. It is a
          PROPOSAL, not a baseline and not a spec. Do NOT treat its assertions as settled, do NOT preserve
          a rule merely because it appears there, and do NOT rate a finding lower because "the draft
          already says this." Anything in it that is not traceable to `~/Documents/Architect.md`, to the
          fork source, or to a ratified owner ruling is the author's invention and is fair game.
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/ATTEMPT-2-STATE.md
    note: The resume point: settled design, owner rulings WITH TRANSCRIPT LOCI, and §8 "failure modes this
          project actually produced" — hunt those six. NOTE its own §6 caveat: it is an agent-written file
          and is therefore NOT an admissible source for owner words. Use it to find the locus, then check
          the locus.
  - path: /home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl
    note: THE SESSION TRANSCRIPT — harness-authored, and therefore the ONLY admissible source for the
          owner's verbatim words. Every "OWNER RULING" cited anywhere is spot-checkable here by record
          index. Rulings governing this run: granularity floor 1128; human gate depth 1148; crash recovery
          1188; no backstop cap 1258; build scope 1274; charter must carry the three-tier completeness
          definition ~1175. Records are JSON lines; index N = the Nth line.
  - path: /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
    note: Attempt 1's dogfood findings — evidence about how cold reviewers actually behaved on this
          artifact, including the measured singleton rate (~85% of findings caught by exactly one
          reviewer) that the Union-not-majority-vote rule rests on. Read it to check that claim rather
          than accepting the number because the draft states it.
  - path: /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect-Attempt-1/stages
    note: ARCHIVED AND SUPERSEDED — attempt 1's stage files, including its two-pass charter. Read ONLY to
          see what was tried and why it was dropped. Never a source of authority: attempt 1's structure
          (two red-team passes, each a disk gate) is exactly what attempt 2 replaces with one pass whose
          findings become the next task. Proposing a return to it requires an argument, not a citation.

measurement:
  baseline:
    how: |
      TEXTUAL baseline — the artifact is a prompt, not a program. Captured in 0-baseline.md at the commit
      the run starts from:
      (1) The FORK SOURCE frozen: `git show 8d73e5d:Guarded_change/stages/charter.md`. Enumerate, as a
          checklist with file:line citations, every RULE it states — each of the five lenses, each
          unconditional discipline bullet, each conditional lens, the provenance-record requirement, the
          reviewer-input-closed-set rule, and the severity model. This list is the regression bar.
      (2) Per enumerated rule, the run's INTENT: CARRY (must still be stated in Architect's charter),
          CHANGE (stated differently, and why), or DROP (deliberately not carried — must be named as
          dropped in the provenance blockquote). Declared BEFORE the build, in 0-baseline.md.
      (3) The unvetted draft's rule set, enumerated the same way and marked as PROPOSED — so the harness
          can distinguish "a rule the fork source had" from "a rule the draft's author invented."
      Regression for this artifact = a CARRY rule that stopped being stated, or a DROP that happened
      without being declared.
    output: Architect/changes/charter-2026-07/0-baseline.md
  check:
    how: |
      Conformance for a prompt-assembly element. The charter is not independently loadable as a skill, so
      `quick_validate.py` does NOT apply to this run (it applies from element 4, the router, onward).
      (1) STRUCTURAL CHECKER — `changes/charter-2026-07/oracles/check.sh`. One POSITIVE PER-SITE
          ASSERTION per criterion: the rule IS STATED, at each site that must state it. Absence sweeps
          are permitted only PAIRED with their positive assertion, and run on NORMALIZED text (strip
          emphasis markers, flatten wrapped lines) — an unnormalized grep for a rule that wraps across a
          line break reports a false absence.
      (2) ORACLE-CAN-FAIL SELF-TEST — `oracles/mutation-test.sh`. Run the SAME checker against a MUTATED
          copy with each asserted rule deleted in turn; every assertion MUST FAIL on its mutant and MUST
          PASS on the clean file. A checker that passes every input is a printer, not an oracle. THIS
          PROJECT SHIPPED THAT EXACT DEFECT TWICE (`ruleid-sitemap.sh` was a bare `exit 0`), and once
          "verified" it by running the tool with no arguments and reading the usage error as a pass. The
          self-test's own invocation, arguments included, is pasted verbatim into 8-harness.md.
      (3) FORK-FIDELITY CHECK — run the baseline rule checklist (1) from `baseline.how` against the built
          charter: every CARRY rule present, every DROP named in the provenance blockquote, no silent
          third category. Mechanical, scripted, output pasted.
      (4) BEHAVIORAL ARMS — the charter's job is to make a cold reviewer behave a certain way, so the
          load-bearing criteria are behavioral and are tested with TWO SEPARATELY-SPAWNED cold agents per
          criterion: a HOLED arm (fixture violating the rule) and an INTACT TWIN (fixture satisfying it),
          each handed ONLY its own fixture plus the charter. Both arms returning the same verdict means
          `verified = no`, whichever verdict it is — the fixture failed to discriminate. Minimum behavioral
          criteria, from the design spec:
            (a) GRANULARITY FLOOR — a reviewer given a plan whose steps sit AT the floor must NOT file
                "you didn't say how" findings; the twin, given a plan with a step ABOVE the floor, must
                flag it. This guards the infinite-regress failure (`~/Documents/Architect.md` lines 4-8).
            (b) COMPLETENESS TIER (iii) — a plan missing a load-bearing section named by NEITHER the
                7-section spine NOR the plan-type's Layer-2 list must be flagged. The founding failure was
                exactly this. A checkbox-sweep-only reviewer must FAIL this fixture — that failure is what
                proves the generative tier is doing the work rather than the checklist.
            (c) SEVERITY ASSIGNED — every finding carries a severity, because `Severity()` filters on it
                and an unsevered finding is dropped on the floor. A reviewer that files findings without
                severities fails.
            (d) NO SELF-CENSORSHIP — findings are unioned, never majority-voted; a reviewer must file an
                observation it suspects is lone. Fixture: a defect a reviewer would plausibly assume
                someone else will catch.
      Any gating criterion that CANNOT be verified pre-ship by a representative fixture is surfaced to the
      human (via the orchestrator), never silently deferred.
    output: Architect/changes/charter-2026-07/8-harness.md

metrics: []                 # no numeric metrics — the baseline is TEXTUAL
```

## Notes

- **The charter has TWO callers and must serve both** (`~/Documents/Architect.md`): the plan red-team
  (`Spawn_redteam`, 3 cold agents per iteration, whose findings become the next task) and the split review
  inside `Divisible` (does the split cover the whole task, is the seam sound, does either half fall below
  the floor). A charter that only aims the first caller is incomplete.
- **The findings-become-the-next-task loop is why the granularity floor is a SAFETY property**, not a style
  preference. A finding asking for detail below the floor becomes work, that work produces steps below the
  floor, and the next reviewer asks for detail below *those*. There is deliberately **no backstop cap**
  (owner ruling, record 1258) — so the floor is the only thing preventing non-termination. Treat any
  weakness in it as at least **major**.
- **Delegation (RAT3).** This loop runs in a subagent; the main session is orchestrator. Every
  stop-for-human **halts the subagent** and returns the question **verbatim** to the orchestrator, who
  relays it to Roy and relays his answer back. The subagent never self-answers a stop, and the orchestrator
  never answers as Roy.
- **Ratification audit (RAT1/RAT2).** A recorded "OWNER RULING" is a claim to re-verify, not a spec. Check
  that the owner's verbatim words at the cited transcript locus actually *select* the recorded option on the
  flagged axis, and that no elaboration inflates beyond what was ratified. This project produced a real
  instance: "means nothing" was inflated into cap-bounce immunity the owner never granted.
- **Do not install.** Nothing is synced to `~/.claude/skills/architect/` until attempt 2 is finished as a
  whole. Attempt 1 sat installed and triggerable for an hour after its dogfood found a blocker.
