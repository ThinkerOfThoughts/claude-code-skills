# 6 — Red-team the code — verbatim record

Cold code review of the 14 built files vs the frozen oracle (86 rows) + criteria + the ORIGINAL
pre-build source (the C1 source-walk) + the gc fork source. Mechanical diff generated via
`git add -A Dragonfly/ && git diff --cached -- Dragonfly/SKILL.md Dragonfly/METHODOLOGY.md
Dragonfly/stages/` (→ `6-build.diff`, 14 files, +622/−563).

## Provenance
Reviewer: **general-purpose**, model **claude-opus-4-8[1m]**, read-only + mechanical grep. Read all 14
built files + oracle + criteria + gc charter + orig SKILL/METHODOLOGY (sha256s below). Built-file
hashes (reviewer-reported): SKILL `022f4621…`, METHODOLOGY `44f81a43…`, charter `92737fcc…`,
stage-0a `bc25c595…`, 0b `b7b81320…`, 1 `93931fc3…`, 2 `7bda93a6…`, 3 `5c482527…`, 4 `611db7bd…`,
5 `5bb2a228…`, 6 `428155d8…`, 7 `6798d837…`, 8 `dc8fb484…`, 9 `5c8ef451…`. Oracle `cc4d988f…`,
criteria `1f3c7684…`, gc charter `6b98164d…`, orig SKILL `b5e122ef…`, orig METHODOLOGY `04d1044c…`.
(NB: built SKILL/charter/stage-6/stage-7 hashes above predate the gate-7 nitpick fix-in-place —
B-TBG-1 pointer added to stage-6/7; re-hashed at stage-8 install.)

## Verdict: **CLEAN** (worst severity = nitpick)

C1/C5/C9/C10 all PASS. No dropped rule, no meaning-changed rewording, no mis-scoped cross-cutting rule,
no fork infidelity, no severed KEEP relationship.

## Findings (verbatim highlights)

**[nitpick — fixed at gate 7] B-TBG-1 (trust-before-gate) physically written only in stage-4/5, though
oracle scope is `4,5,6,7`.** Reviewer's own analysis: *"I checked the original source — trust-before-gate
lived only in orig SKILL:61-64 and METHODOLOGY:170-176 (stage 5) + 314-320; it was never physically
stated at stage 6 or 7 in the original either. So the build is behavior-preserving to source… Grading
it a real gap would be holding the build to a stricter standard than the source it must preserve."*
Optional one-line pointer suggested. **→ Applied at gate 7** (concise B-TBG-1 statement added to
`stage-6.md` + `stage-7.md`) so C1 is unambiguously clean vs the frozen `4,5,6,7` scope.

**Factual lens — clean, earned with citations.** Four lenses faithful + domain-adapted (gc charter:19-22
→ df charter:23-26); discipline bullets complete (cite/rank/flag/no-issue/clean-factual/spot-verify/
precision all present + match gc); provenance record-elements (i)-(v) match gc verbatim; severity model
faithful (four levels match gc verbatim; "minor (real but local)" improves on orig METH:411 "minor
(local)"); A-8-3 characterized (a)-(e) present in BOTH stages 7+8; A-9-7 symptom-evidence-only present;
A-1-4 repro-ordering escape present; B-REP-3 detector rule present in all three stages 1/4/7.

**Logical lens — clean.** Both deliberate asymmetries preserved, not "corrected": the coverage-challenge
exclusion (charter:64-67 = orig METH:396-399) and the severity-model-reaches-1/4/7-via-forced-charter-read
(C3 permits opening a stage-declared reference file).

**Position/behavior lens — clean.** Representativeness gate keeps "mandatory, blocking, non-waivable" +
reject-and-redesign at both stages 1/4; gate-before-present tier ladder intact at stage-3 (tier→claim
mapping preserved); the four excluded gc lenses did NOT leak as active rules (grep for position/
concurrency/closed-set/supplementary across built files returns only the recorded-exclusion note at
charter:9-10).

## Disposition
- **C1 — PASS** (86 rows spot-sampled across A/B/C incl. every multi-stage Group-B row; source-walk found
  no source rule dropped). The one nitpick was source-faithful; fixed at gate 7 for oracle-scope cleanliness.
- **C5 — PASS** (both deliberate asymmetries preserved; no drift).
- **C9 — PASS** (39 `guarded-change` hits all KEEP-classified; forbidden-pattern grep zero; 4 forked
  pieces present in full + faithful; 4 exclusions recorded; D-11 retired).
- **C10 — PASS** (stage-8 handoff + full-GC triage invocation + stage-9 masking route present, meaning intact).
- **Not checked here (deferred to stage 8):** C2 behavioral firing (needs execution arms), C3 line/token
  budget, C4 live==source diff.
