# 3-redteam-plan-round3.md — stage-3 cold review, ROUND 3 (full re-review; verdict: MAJOR)

## Provenance
- **Reviewer:** cold subagent, `general-purpose`, model `claude-opus-4-8`, no shared context.
- **Run:** 2026-07-06, task `ae1da4c6d3f15db37`; ~7.9 min, 20 tool uses, ~81K tokens.
- **Round mandated by owner** (round-2 cap tie-break → "full round 3").
- **Disposition:** 13/14 round-2 fixes genuinely resolved; **O-6's fix is defective**
  (F2-NEW). 2 new majors (F2-NEW, F3-NEW), 7 minors, 1 missed-opp. Reviewer's own
  same-class read: **NOT a third bounce of the same objection — two NEW majors the deeper
  pass exposed**; core architecture sound. No blocker.

## Charter (verbatim summary)
Stage-3 ROUND 3 full re-review. Tasks: (1) resolution check of every round-2 finding
(A-1,CC-1,L-1,O-1,P-1 + minors) — genuinely fixed, not reworded, **and no fix-introduced
defect**; (2) independent oracle re-audit vs current source (missing rules / wrong
governing-stage-sets, incl. the new build-notes); (3) full fresh pass — 4 lenses + position
+ label audit + coverage + split-introduced failure modes. Closed context: revised docs +
oracle + round-1/2 records + current METHODOLOGY/SKILL + decisions.md. Full charter in task
transcript `ae1da4c6d3f15db37`.

## Reviewer output (verbatim)

### Context hashes (reviewer self-computed)
```
35a6798d…10e3  METHODOLOGY.md      4e2a2e51…839b  SKILL.md
7fc2ee6a…3f59  1-spec.md           6a7b9d7b…6c19  1.5-criteria.md
a523f812…97a3  2-plan.md           46cea423…6798  2-rule-oracle.md
3d4cf74d…4f1a  3-redteam-plan.md (r1)   ce936527…5e67f  3-redteam-plan-round2.md (r2)
```
Line counts: METHODOLOGY 534, SKILL 124.

### Resolution check
- **A-1 RESOLVED** (oracle build-note + plan A.1: routing targets in each gate file).
- **CC-1 RESOLVED** (SIT-6 added; BROKEN-NEW includes SIT-6). Residual → F3-NEW.
- **L-1 RESOLVED** (OLD unanimous-2/2, strictly stricter than the ≥2/3 NEW bar).
- **O-1 RESOLVED in form** (asymmetry stated; C5 scoped to own-set). Residual → F1-NEW
  (CH9/CH10 {3}-scoping is an author inference, not grep-derived; source tags only CH8
  "(stage 3)").
- **P-1 RESOLVED** (C2 precedence-grading rule: an outcome, not a mention).
- **O-2/O-3/L-2/A-2/CC-2/CC-3/M-2 RESOLVED.** **O-6 fix DEFECTIVE → F2-NEW.**

### Oracle re-audit
- **F2-NEW [MAJOR]:** HIL wrongly widened to {4,7,8,1.5} (my O-6 fix). Source (METHODOLOGY:
  524-535, esp. 526 "stages 1–7 … autonomously") — no HIL trigger fires at gate 7 (a
  blocker@7 → build, not restart). C1 grades against the frozen oracle → would certify the
  widened rule. **Fix: HIL → {4,8,1.5}, drop 7.** (The human-tie-break-at-7 idea O-6 reached
  for is already covered by SEV4 iteration cap → {4,7,8}, a different rule.)
- **F1-NEW [MINOR]:** CH9/CH10 {3}-scoping inferred, not grep-derived → mark it inferred.
- Otherwise complete + correctly scoped (FRZ→{4,8}, CFG3→{R,3,4,6}, ART3→{4,7,8}, ST6d→{6},
  SEV3→{4,7,8} all re-verified). No missing atomic rule.

### Fresh pass
- **F3-NEW [MAJOR]:** the gating C3(a) budget (≤40%×658 = 263 lines/stage load) is NOT shown
  achievable for **stage-3.md / stage-6.md** — the reviewer charter alone is **95 lines**
  (METHODOLOGY:204-298); written in full into stage-3.md + its governing core principles
  (CP1/2/6/7/8 ≈ 34) + CFG2/CFG3/ART2/CP4/CP5 + the procedure ⇒ plausibly 160-200+ lines →
  load = SKILL(~110)+stage-3(~180) ≈ **290 > 263 cap**. Plan A.1 admits 3/6 "will be the
  largest" yet keeps "≤~90 lines each"; A.3 budgets only the average stage. → the change
  could FAIL its own primary criterion at the two red-team stages after the full build +
  38-arm battery spend. **Partially reopens round-1 A1/A2 (does the load actually shrink) in
  a new spot.** Fix at stage 2: (a) bound+budget 3/6 specifically and confirm under cap, or
  (b) **M1-NEW: a single `charter.md` reference file both stage-3.md & stage-6.md point at**
  (stage-3 adds only CH8/CH9/CH10) — resolves F3-NEW AND removes the O-1 charter-drift
  surface; trades a small C3(b) self-containment softening (C3(b) already permits a
  stage-declared reference file), or (c) relax C3(a) for 3/6 with a stated reason + re-freeze.
- **F4-NEW [MINOR]:** FRZ's stage-8 verify-unchanged half unexercised by any SIT (C1
  placement + C4 diff backstop it).
- **F5-NEW [MINOR]:** confirm SEV1's *table* (not only the routing target list) co-locates
  with SEV3 in each gate file, preserving the adjacency P-1 protects.
- **D1-NEW [MINOR]:** grader-count drift (fix-introduced): criteria says "per arm output"
  (⇒38), plan says "per situation (6)", plus a stale "~5". Unify on per-situation × 6.
- **CH-A [MINOR]:** SEV3/FRZ behaviorally exercised at only one of their governing stages
  (same text — low risk).
- **M1-NEW [MINOR opp]:** the shared `charter.md` (above) — fixes F3-NEW + O-1 drift at once.
- **Label audit: no mislabel** (C1–C6 gating, C7/C8 advisory with legit reasons; C3 correctly
  gating). **Position lens:** change correctly treated position-sensitive; F5-NEW is the one
  adjacency to confirm. **Coverage:** blast radius spanned conditional on F3-NEW fixed.

### RANKED: F2-NEW (MAJOR), F3-NEW (MAJOR); F1-NEW/F4-NEW/F5-NEW/D1-NEW/CH-A/A1-NEW (MINOR);
M1-NEW (minor opp).

**One-line verdict — worst severity: MAJOR.** No blocker. F2-NEW (fix-introduced HIL
over-scoping C1 would certify) + F3-NEW (gating attention budget not shown achievable for the
charter-heavy stages 3/6). Both fixable at stage 2 before gate-4 freeze; core architecture
sound.
