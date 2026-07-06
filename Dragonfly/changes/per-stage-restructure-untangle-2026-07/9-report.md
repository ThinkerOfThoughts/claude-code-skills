# 9-report.md — dragonfly per-stage restructure (Theme 1) + guarded-change untangle (Theme 2): outcome

## What shipped

The dragonfly skill is reorganized from two topic-organized files (`SKILL.md` 149 + `METHODOLOGY.md`
521 = 670 lines, all in view at every stage) into a **file-per-stage** layout, **and** its runtime
dependency on guarded-change is severed:

- `SKILL.md` — an **81-line router** (auto-loaded): the loop table pointing each stage at its file.
- `stages/stage-{0a,0b,1,2,3,4,5,6,7,8,9}.md` — one self-contained file per stage (procedure + every
  cross-cutting rule that governs it, written in full).
- `stages/charter.md` — dragonfly's **own** red-team charter (75 lines), forked from guarded-change's
  unconditional core, shared by stages 1/4/7.
- `METHODOLOGY.md` — slimmed to 178 lines of orientation/reference (why / the loop / two layers / config
  contract / artifacts / trigger / HIL), kept so external references don't break.

**Theme 1 (attention budget, D-S1):** at any stage an agent loads the router + one stage file (+ charter
at 1/4/7) — **≤227 lines vs the old 670** (~34%), so a single rule can't be diluted by 600 lines of the
other ten stages.

**Theme 2 (the D-S2 untangle, "a bug getting fixed"):** dragonfly no longer borrows guarded-change's
charter / severity model / rate-based rubric / lite definition **by reference**. All four are now stated
in full in dragonfly's own files; the five-plus cross-references are gone; the D-11 cross-reference
self-check is retired. The legitimate composition relationships remain: dragonfly still **hands the fix
to guarded-change** (stage 8), still **routes an expensive diagnostic artifact into a full guarded-change
run** (triage), still routes a masked-symptom fix **back to guarded-change** (stage 9). Dragonfly no
longer *tracks* guarded-change's future charter edits — the intended behavior change.

## Outcome — accepted, behavior-preserving

Driven through the full guarded-change loop (dogfooded on itself): 3 stage-3 plan-review rounds + an
independent oracle-completeness re-derivation, a stage-6 code review, and a stage-8 Tier-2 harness.

- **The plan phase was hard-won.** Round 1 (BLOCKER: oracle miscount, a missing rule, an under-inclusive
  de-coupling grep, a charter over-fork) and round 2 (BLOCKER: the fixes were themselves incomplete —
  count didn't propagate, grep still adjacency-bugged, one over-fork piece missed, two more missing
  rules) fired the **iteration cap**. The owner tie-broke → the rigorous path: fix everything, re-anchor
  the "no rule lost" guarantee on **build-vs-source** (not the hand-oracle alone), and **independently
  re-derive the oracle's completeness**. That independent pass certified the 86-row inventory complete
  (no spurious rows, no further load-bearing gaps). Round 3 came back MAJOR (3 mechanical plan-drift
  items), all fixed-in-place; the owner authorized freeze.
- **No behavior regression.** Stage 6 (cold code review vs the frozen oracle + the original source):
  CLEAN — every rule present + correctly scoped, no meaning-changed rewording, the fork faithful, the
  KEEP relationships intact. Stage 8 (Tier-2 spot-check): **4/4 arms fired** the highest-risk rules
  under per-stage isolation, each opening only its routed file — positive evidence the split preserves
  rule-firing.
- **Theme-2 verified clean:** every one of 39 `guarded-change` mentions in the built files is a
  legitimate composition mention; zero rules-dependency phrasings survive.

## Residuals / follow-ups (not blocking)

- **Theme 3 — the incidental-bug ledger — is deferred** to its own additive run (owner decision at the
  spec gate). This run was behavior-*preserving* only; the ledger adds behavior and gets its own
  "the-feature-works" bar. It fits dragonfly's existing ledger structure.
- **Tier-2 behavioral coverage is 4 of 86 rules.** The other 82 rest on C1 (oracle mapping + the
  stage-6 source-walk) + C9a (mechanical de-coupling). The owner chose Tier 2 over a full A/B battery
  because the battery's broken controls are non-discriminating on these skills (flagship-probe + gc
  battery, twice) — ~2M tokens to re-learn a known lesson.
- **The four recorded fork-exclusions are a possible future additive question:** whether dragonfly's
  cold review *should* gain guarded-change's position lens, concurrency lens, or the closed-set-input
  rule is a behavior *addition*, out of scope for this preservation run — surfaced here, not decided.
- **Total line count rose** 670 → 729 (repetition + forks) — by design; per-stage *load*, not total, is
  the target (advisory C8).
- **The gate-7 nitpick** (B-TBG-1 written at stage-4/5 but scoped `4,5,6,7`) was fixed by adding a
  concise trust-before-gate statement at stage-6/7 — a legibility improvement over the original source,
  which never stated it there either.

## Sequencing

This is the second and final slice of the two-skill restructure initiative (guarded-change Theme 1
shipped first, `3d6889b`). Both skills are now file-per-stage; dragonfly is additionally self-contained.
The temporary allowlist + battery scratch dirs are now due for cleanup (both runs done — see cleanup
memory).
