# 5 — Build record

Built the 14-file set per `2-plan.md` §A (frozen at gate 4). **Reorganization + fork, not rewrite** —
every rule relocated from the current `Dragonfly/SKILL.md` + `METHODOLOGY.md` into its per-stage file;
the four borrowed pieces forked into dragonfly's own `stages/charter.md` + stage files.

## Files built
- `SKILL.md` — 81-line router (was 149): front matter (description unchanged) + inputs + cold-start
  guard + loop router table (each stage → `stages/stage-N.md`; 1/4/7 also load `charter.md`) +
  stop-for-human + self-check (**D-11 cross-reference clause removed**, replaced by "charter is now its
  own").
- `stages/charter.md` — 75 lines: dragonfly's forked red-team charter (four lenses + discipline +
  diagnosis aiming + provenance record-elements + B-CH-inherit + severity model + coverage-challenge
  exclusion). **Excludes** gc's position/concurrency lenses, A/B clause, closed-set rule (per C9b).
- `stages/stage-{0a,0b,1,2,3,4,5,6,7,8,9}.md` — 11 self-contained stage files.
- `METHODOLOGY.md` — 178 lines (was 521): orientation/reference (why / loop / two layers / config
  contract / artifacts / trigger / HIL). C-REF-1's "referenced from guarded-change" clause rewritten
  to "dragonfly's own charter" (round-2 METH:420 fix).

## Build self-checks (formal verification at stage 8)
- **C3a load budget:** per-stage load (SKILL + stage [+ charter for 1/4/7]) — heaviest = **stage 7 at
  223 lines** (33% of the old 670-line whole-doc load); all stages ≤ 223 ≤ ~270 cap. PASS.
- **C9a de-coupling:** `grep -in guarded-change` over the built files → every mention classified
  **KEEP composition** (sibling framing / stage-8 handoff / triage+lite invocation / masking route /
  fork-provenance note / full-GC-keeps-gc-duties); **zero rules-dependency phrasings** (grep for
  inherit/reuse/by-reference/Identical/referenced-from/see-METHODOLOGY/pointer-back = empty). PASS.
- **C8 total size:** 729 lines total (was 670) — rose slightly (repetition + forks), offset by the
  slim METHODOLOGY. Advisory; per-stage load (C3) is the real target.
- **C1 (rule inventory) + C4 (live==source) + C5/C6/C9b/C10** — verified at stage 8 (harness) after
  the stage-6 cold code review.

## Mechanical diff (for stage 6)
Base rev `3d6889b` (frozen). The build modifies `SKILL.md` + `METHODOLOGY.md` (tracked) and adds
`stages/*.md` (new). Reviewed diff generated mechanically: `git add -A Dragonfly/ && git diff --cached
-- Dragonfly/SKILL.md Dragonfly/METHODOLOGY.md Dragonfly/stages/` (command recorded in
`6-redteam-code.md`).
