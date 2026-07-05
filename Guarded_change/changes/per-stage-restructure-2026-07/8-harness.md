# 8-harness.md — per-stage restructure of guarded-change: stage-8 conformance

Conformance of the built restructure vs the frozen `1.5-criteria.md` (C1–C8). Greenfield
w.r.t. behavior (no stage-0 baseline of the *restructured* skill) → conformance-only.

## Per-criterion verification table

| Criterion | Gating | Path exercised | Verified by execution? | Evidence | Result |
|---|---|---|---|---|---|
| **C1** rule inventory preserved & correctly scoped | gating | build vs frozen oracle | yes (stage-6 cold review) | `6-redteam-code.md`: every sampled rule verbatim in every governing stage file; charter byte-identical; 3≠6 asymmetry correct; F-1 (CP6/CP7 rationale clauses) fixed in place | **PASS** |
| **C2** behavior preserved (A/B battery) | gating | 6 stage situations × {OLD monolith, NEW file-per-stage, BROKEN control}, 44 agents, blind-graded | yes (execution) | battery result below | **PASS on no-regression; controls non-discriminating → named risk-acceptance (see decisions.md)** |
| **C3(a)** per-stage load ≤ ~40% of 658 | gating | `wc -l` per stage load | yes | all loads ≤263 (max stage-8 = 262; stage-3 = 253); charter shared keeps 3/6 under cap | **PASS** |
| **C3(b)** per-stage isolation holds in practice | gating | NEW-arm file-opens | partial | the router+file-per-stage design enables it (C3(a)); the battery scored rule-firing, not file-open discipline, so obey-the-router-in-practice is **unmeasured this run** → residual, folded into the C2 risk-acceptance | **RESIDUAL (see note)** |
| **C4** live == source | gating | `diff -r ~/.claude/skills/guarded-change` | yes | install + diff below | **PASS** |
| **C5** cross-file consistency | gating | consistency sweep | yes (stage-6) | `6-redteam-code.md`: SEV table/ART3/H8/CFG3 consistent across files; charter one copy; asymmetry respected | **PASS** |
| **C6** router correctness | gating | router resolves | yes (stage-6 + mechanical) | all 10 stages have a file the router points to; 3/6 → file + charter | **PASS** |
| **C7** per-stage legibility | advisory | rubric | — | each stage file self-contained (stage-6 read them standalone) | PASS (advisory) |
| **C8** total-size budget | advisory | `wc -l` | — | gc content 658→1082 lines (repetition by design); per-stage load is the real target (C3) | recorded (advisory) |

## C2 — the A/B battery result (44 agents, ~2.1M tokens, blind-graded)

Fire counts per (situation, rule), by condition — **OLD** monolith (n=2), **NEW**
file-per-stage (n=3), **BROKEN** control = NEW with that rule deleted (n=2):

| Situation · rule | OLD | NEW | BROKEN | Cell verdict |
|---|---|---|---|---|
| SIT-1.5 · ST1.5d (position criterion) | 2/2 | 3/3 | — | **PRESERVED** |
| SIT-1.5 · ST1.5c (gating labels) | 2/2 | 3/3 | — | **PRESERVED** |
| SIT-2 · CP3 (instrument-before-build) | 2/2 | 3/3 | — | **PRESERVED** |
| SIT-3 · CH11 (position lens) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-3 · CH9 (label audit) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-3 · CH7 (provenance) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-4 · SEV3 (no silent demotion) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-4 · SEV4 (iteration cap) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-4 · CFG3 (paths block gate 4) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-4 · FRZ (criteria freeze) | 0/2 | 0/3 | 0/2 | **INVALID SITUATION** (situation didn't provoke the rule; untested) |
| SIT-6 · ST6d (mechanical diff) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-6 · CH6 (spot-verify) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-8 · H5 (no deferral) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |
| SIT-8 · ART3 (gating disposition) | 2/2 | 3/3 | 2/2 fired | no-regression; control non-discriminating |

**The headline: NEW ≥ OLD on every one of the 12 triggered rule-cells — zero behavior
regression.** Not one rule fired *less* under the file-per-stage structure than under the
monolith; 12/12 went 3/3 (NEW) vs 2/2 (OLD).

**The controls were non-discriminating:** every BROKEN variant (rule deleted from the doc)
STILL fired the rule 2/2. Capable Opus arms apply the rule's behavior — flag a
position-sensitive reorder, catch a mislabelled gating criterion, refuse to silently demote
a reviewer's MAJOR, refuse to defer a gating check to production — whether or not the
methodology text states it. So the behavioral battery cannot demonstrate it would *detect* a
dropped rule. (This is the flagship-probe lesson recurring: the subject is too competent for
rule-deletion to change its behavior; the grader — even Fable-5 — found no daylight.)

**One invalid situation:** SIT-4 · FRZ (criteria freeze) never fired under any condition —
the gate-4 scenario emphasized demotion/cap/paths and didn't make freezing salient, so the
rule went untested. A situation defect, not a change defect (FRZ's presence is C1-verified).

## Named risk-acceptance (stage-8 human decision — owner ThinkerOfThoughts, 2026-07-06)

Per the methodology (a gating criterion that cannot be cleanly self-verified pre-ship needs
route (a) a representative harness or route (b) named risk-acceptance): the C2 behavioral
battery achieved **no-regression** but its **positive controls could not discriminate**, so
it cannot self-certify detection power. The owner **accepts** the restructure on the combined
evidence, recorded as:

> **KNOWN UNVERIFIED RISK (C2 behavioral detection power):** the A/B battery found zero
> behavior regression (NEW ≥ OLD on all 12 triggered cells), but its broken-rule controls
> were non-discriminating (capable arms apply each rule regardless of the doc text), so the
> battery cannot prove it would have caught a silently-dropped rule. That specific risk — a
> rule lost in the restructure — is independently closed by **C1** (stage-6 mechanically
> verified every rule present verbatim in its correct stage files). Behavior-preservation
> assurance therefore rests on **C1 (content) + the clean no-regression A/B**, not on the
> battery's (undemonstrated) discrimination. Accepted; rebuilding a more powerful control is
> judged futile for a capable subject (owner: "even Fable-5 had trouble out-thinking Opus").
> Residual C3(b) (per-stage-loading obeyed in practice) folded in here — unmeasured this run;
> the mechanical load reduction C3(a) stands.

## Verdict

All gating criteria PASS or are covered by the named risk-acceptance above. **The restructure
conforms** — behavior-preserving (content-verified + no regression), attention budget reduced
(every stage load ≤263 vs 658), router resolves, live==source. Proceed to install + commit.
