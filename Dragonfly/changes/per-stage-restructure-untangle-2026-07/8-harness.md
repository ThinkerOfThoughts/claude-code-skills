# 8-harness.md — dragonfly per-stage restructure + untangle: stage-8 conformance

Conformance of the built restructure vs the frozen `1.5-criteria.md` (C1–C10) + the frozen 86-row
oracle. **Greenfield w.r.t. behavior** (no stage-0 baseline of the *restructured* skill) →
conformance-only. Verification tier: **Tier 2** (content-primary C1 + cold stage-6 source-walk + a
4-arm behavioral spot-check; no full A/B battery — its broken controls are non-discriminating on these
skills, observed twice: flagship-probe + gc battery).

## Per-criterion verification table

| Criterion | Gating | Path exercised | Verified by execution? | Evidence | Result |
|---|---|---|---|---|---|
| **C1** rule inventory preserved & correctly scoped | gating | oracle→new mapping + **SOURCE→new rule-by-rule** (stage-6 cold review) | yes (stage-6) | `6-redteam-code.md`: 86 rows spot-sampled across A/B/C incl. every multi-stage Group-B row; source-walk found **no source rule dropped**; nitpick (B-TBG-1 scope) fixed at gate 7 | **PASS** |
| **C2** behavior preserved (Tier-2 spot-check) | gating | 4 cold arms at high-risk stages under per-stage isolation | yes (execution) | arm table below — **4/4 FIRED** | **PASS** |
| **C3(a)** per-stage load materially reduced | gating | `wc -l` per stage load | yes | heaviest = stage 7 **227 lines** (34% of the old 670-line whole-doc load); all stages ≤ 227 ≤ ~270 cap | **PASS** |
| **C3(b)** per-stage isolation holds in practice | gating | NEW-arm file-opens | yes (execution) | each of the 4 arms cited/opened **only** its routed stage file(s) + `charter.md` (where named) + `SKILL.md` — **no sibling stage file** needed to fire its rule | **PASS** |
| **C4** live == source | gating | `diff -r ~/.claude/skills/dragonfly/` | yes | SKILL.md / METHODOLOGY.md / all 12 `stages/*` diff-clean (install log) | **PASS** |
| **C5** cross-file consistency | gating | oracle-driven sweep (stage-6) | yes (stage-6) | `6-redteam-code.md`: both deliberate asymmetries preserved (coverage-challenge exclusion; severity-via-forced-charter-read); no drift | **PASS** |
| **C6** router correctness | gating | router resolves (mechanical + behavioral) | yes | mechanical: all 11 stages (0a,0b,1–9) have a file the router points to; behavioral: the 4 arms reached their correct stage file via the router | **PASS** |
| **C7** per-stage legibility | advisory | rubric (stage-6 reviewer read them standalone) | — | each stage file self-contained; stage-6 read them standalone | PASS (advisory) |
| **C8** total-size budget | advisory | `wc -l` | — | 670 → **729** total (repetition + forks, offset by slim METHODOLOGY); per-stage load (C3) is the real target | recorded (advisory) |
| **C9(a)** Theme-2 self-contained / de-coupled | gating | read-and-classify every `guarded-change` hit | yes | 39 hits **all KEEP-composition**; forbidden-pattern grep **zero** rules-dependency; the two round-2 landmines (SKILL:107 "unchanged charter", METH:394 "inherit ALL of") gone; D-11 retired | **PASS** |
| **C9(b)** fork faithfulness | gating | mapping vs gc source (stage-6) | yes (stage-6) | 4 forked pieces content-faithful to gc unconditional core; 4 exclusions (position/concurrency lens, A/B clause, closed-set) correctly recorded, not omitted | **PASS** |
| **C10** legitimate relationships survive | gating | locate in new files (stage-6) | yes (stage-6) | stage-8 handoff (A-8-2), full-GC triage invocation, stage-9 masking route — all present, meaning intact | **PASS** |

## C2 — the Tier-2 behavioral spot-check (4 arms, cold, per-stage isolated, blind to the tested rule)

Each arm: a cold `general-purpose` agent given a scratch install containing **only** `SKILL.md` + the
routed `stage-N.md` (+ `charter.md` where the router names it), handed a triggering hunt scenario, asked
what it does. Graded FIRED / DID NOT FIRE with a quote.

| Arm | Rule | Stage | Loaded | Scenario | Verdict |
|---|---|---|---|---|---|
| SC-1 | B-REP-1/3 representativeness gate | 1 | SKILL+stage-1+charter | repro's control run **also** exhibits the symptom | **FIRED** — "the detector failed the stay-silent-on-clean half … under B-REP-3 its reading may not be consumed" → reject + redesign + re-triage |
| SC-2 | B-GBP-1 gate-before-present | 3 | SKILL+stage-3 | ungated top hypothesis; user asks "what's the cause?" | **FIRED** — presents H1 as **"candidate, ungated"**, "not the leading cause, the likely cause, or something to act on yet" (B-GBP-1/C-HIL-2/B-GBP-4) |
| SC-3 | B-CH-clean clean-factual-earned | 7 | SKILL+stage-7+charter | cold review "factual clean" with **zero** citations | **FIRED** — "treated as an **un-run review** — not a pass" → re-spawn cold reviewer; does not set `cold-red-teamed` |
| SC-4 | B-TRI-1/2 triage (cross-cutting @ 2nd home) | 7 | SKILL+stage-7+charter | toggle that spawns a token-metered LLM judge | **FIRED** — "**tokens → full** … goes down the FULL guarded-change path … recorded in `decisions.md` before consuming" (also flagged B-REP-3 for the LLM judge + the rate-based rubric) |

**Headline: 4/4 FIRED under per-stage isolation, each opening only its routed file(s).** Not one
sampled rule failed to fire when the agent saw only its isolated stage file — positive evidence that
the file-per-stage split preserves rule-firing and that the isolation is real (C3b). No BROKEN control
was run (its non-discrimination is established twice; a control that cannot fail is not evidence).

## Residual (named, not blocking)
- **Tier-2 sampled 4 of 86 rules behaviorally.** The other 82 rest on **C1** (oracle mapping + the
  stage-6 SOURCE-walk, which checks the build against the real source, not just the oracle) + **C9a**
  (mechanical de-coupling). The 4 arms cover the highest position-sensitivity risks (representativeness
  gate, gate-before-present, clean-factual-earned, triage-at-a-second-home). This is the Tier-2 scope
  the owner chose; a broader battery was judged non-discriminating for a capable subject.
- **SC-4 referenced ambient project context** (an intermittent-symptom hunt) not supplied in its prompt;
  it did not affect the grade (the triage rule fired correctly regardless).

## Verdict

**All gating criteria (C1, C2, C3a/b, C4, C5, C6, C9a/b, C10) PASS; advisories recorded.** The
restructure **conforms** — behavior-preserving (content-verified + source-walked + 4/4 spot-check fired),
Theme-2 cleanly de-coupled (zero rules-dependency, relationships intact), attention budget reduced
(every stage load ≤227 vs 670), router resolves, live == source. **Gate 8: clean → done.**
