# 9-report.md — per-stage restructure of guarded-change: outcome

## What shipped

The guarded-change skill is reorganized from two topic-organized files (SKILL 124 +
METHODOLOGY 534 = 658 lines, all in view at every stage) into a **file-per-stage** layout:

- `SKILL.md` — a 73-line **router** (auto-loaded): the loop table pointing each stage at its file.
- `stages/stage-{0,1,1.5,2,3,4,5,6,7,8}.md` — one self-contained file per stage, carrying that
  stage's procedure + every cross-cutting rule that governs it (written in full).
- `stages/charter.md` — the ~78-line red-team charter, shared by stage-3 and stage-6 (one copy).
- `METHODOLOGY.md` — slimmed to 193 lines of orientation/reference (why / the loop / two
  layers / config contract / artifacts), kept so external references don't break.

**Net effect (the goal):** at any stage an agent loads the router + one stage file (+ charter
at 3/6) — **≤262 lines vs the old 658** (~40% or less), so a single rule can't be diluted by
600 lines of the other nine stages. This addresses the S1/D-S1 attention-budget ceiling.

## Outcome — accepted, behavior-preserving

Driven through the full guarded-change loop (dogfooded on itself): 3 stage-3 review rounds +
a targeted pass (blocker → major → major → clean), a stage-6 code review (minor, fixed), and
a stage-8 A/B behavior battery (44 agents).

- **No behavior regression.** The battery ran 6 realistic situations at 6 stages through the
  old monolith vs the new structure, blind-graded: the new structure fired **every** rule at
  least as reliably as the old (12/12 triggered cells: new 3/3 vs old 2/2). Nothing fired less.
- **Content verified.** Stage 6 mechanically confirmed every rule is present verbatim in its
  correct stage files (the charter byte-identical; the deliberate stage-3≠stage-6 asymmetry
  correct).
- **Honest caveat (owner-accepted named risk).** The battery's deliberately-broken controls
  couldn't discriminate — a capable Opus arm applies each rule whether or not the doc states
  it, so the behavioral test can't *prove* it would catch a dropped rule. That specific risk is
  independently closed by the content-check; preservation rests on content-verified + the clean
  no-regression A/B. Accepted; a stronger control is judged futile for so capable a subject.

## Residuals / follow-ups (not blocking)

- **C3(b) unmeasured:** the mechanical load reduction is proven (files are small), but whether
  an agent *in practice* obeys the router and opens only its stage file was not cleanly measured
  this run — the battery scored rule-firing, not file-open discipline. Worth a cheap check
  sometime, or trust the router.
- **Total line count rose** 658 → 1082 (repetition of cross-cutting rules into each stage) — by
  design; per-stage *load*, not total, is the target (advisory C8).
- **One battery situation (SIT-4·criteria-freeze) was inert** — the scenario didn't provoke the
  rule, so it went untested behaviorally (its presence is content-verified). A stronger SIT-4
  in any future re-run.
- **Battery-orchestration lesson:** arms running the methodology spawned their own cold-review
  sub-agents (unbounded) and — with cwd = the live repo — wrote real `changes/<slug>/` folders,
  which deadlocked on write-permission prompts mid-run. A future battery should sandbox the arm
  cwd and forbid file writes (output inline) + bound sub-agent spawning.

## Sequencing

Owner directed: **pause here.** The follow-on dragonfly run (Theme 1 restructure + Theme 2
untangle) is deferred until an owner side quest that needs the restructured guarded-change is
done. Temporary allowlist + battery scratch dirs remain until then (see cleanup memory).
