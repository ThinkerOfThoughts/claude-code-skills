# decisions.md — dragonfly per-stage restructure (Theme 1) + untangle (Theme 2)

Append-only gate log. Gate (by stage number) · worst severity · route · rationale+name for any override.

---

**Run start (2026-07-06).** Slug `per-stage-restructure-untangle-2026-07`. Dogfooded guarded-change
loop on the dragonfly skill files. Base rev of `Dragonfly/` + `Guarded_change/`: skills repo `main`
(guarded-change restructure live at `3d6889b`; dragonfly forks the finalized gc charter/severity/
rubric from that state). Scope decided in memory `skills-structural-decisions-2026-07`: Themes 1
(per-stage restructure) + 2 (untangle the by-reference coupling), together, dragonfly only, sequenced
after the gc restructure.

**Stage 1 (spec) + 1.5 (criteria) drafted** — `1-spec.md`, `1.5-criteria.md`. Two decisions left OPEN
for the owner at the spec gate before the expensive stages:
- **(A) Theme 3 (incidental-bug ledger)** — recommended DEFER to a separate additive run (this run's
  bar is behavior-preserving; Theme 3 adds behavior). Owner to confirm fold-in vs defer.
- **(B) Verification depth for C2** — Tier 1 (content-only) / **Tier 2 (content-primary + targeted
  behavioral spot-check) [recommended]** / Tier 3 (full A/B battery). Recommendation rests on the
  twice-observed non-discrimination result (flagship-probe + gc battery): a full Tier-3 battery on
  these skills would very likely re-land on named-risk-acceptance leaning on C1, for ~2M tokens.

**Spec gate — owner decisions RESOLVED (2026-07-06, ThinkerOfThoughts):**
- **(A) Theme 3 → DEFER** to a separate additive run. This run = Themes 1+2, behavior-preserving only.
- **(B) Verification depth → TIER 2** (content-primary C1 oracle + cold stage-6 review + a targeted
  behavioral spot-check: router resolves + 2–3 most position-sensitive rules fire under NEW
  isolation). Rationale: Tier-3 battery controls non-discriminating on these skills (flagship-probe +
  gc battery, twice) → ~2M tokens would re-land on named-risk-acceptance leaning on C1. Spec/criteria
  updated to lock Tier 2; C2 frozen to Tier-2 shape at gate 4.

Spec + criteria finalized. → Stage 2: plan (§A file set + per-stage rule mapping + Theme-2 fork plan +
per-stage load budget; §B Tier-2 spot-check design) + build the C1 grep-derived rule oracle.

**Stage 2 built** — `2-plan.md` + `2-rule-oracle.md`. Path validation (gate-4 precondition) recorded:
all 9 stage-3 context paths readable; base rev `3d6889b`; hashes captured.

**GATE 4 — ROUND 1 · worst severity = BLOCKER · route = backward to stage 2/1.5 (fix artifacts), NOT
to stage 1 (direction affirmed by reviewer).** Cold reviewer: general-purpose, `claude-opus-4-8[1m]`;
verbatim record `3-redteam-plan.md`. Findings + dispositions (all accepted, none contested):
- **[BLOCKER] oracle miscount** (78 claimed vs 80 enumerated) → recounted mechanically; now **81**
  (33/31/17) after adding the missing row; count derived by `grep -cE`, not hand-typed.
- **[BLOCKER] A-8-2 missing** (a real C10-gated rule, the stage-8 handoff) → **row added** to Group A
  (SKILL:76-77 / METH:231, stage-set `8`, KEEP).
- **[BLOCKER] C9a removal grep under-inclusive** (6 literals missed SKILL:107/117 + METH:339/344/388/
  394) → **C9a rewritten** as read-confirm of the 4 fork targets + broadened classified grep; criteria
  + plan updated.
- **[MAJOR] over-fork** — plan forked gc's charter "verbatim" incl. the conditional position/concurrency
  lenses + gc-run-specific A/B clause, which current dragonfly does NOT carry (METH:394 inherits only
  *unconditional* bullets) → **fork corrected to unconditional core only; position/concurrency lenses
  EXCLUDED** and recorded as a deliberate divergence (C9b); whether dragonfly should gain them = a
  future additive question (→ `9-report.md`). This is the position-sensitivity blind-spot class caught.
- **[MAJOR] coverage gap** — a wrongly-*added* rule was invisible to every criterion → **C1 gained a
  reverse/anti-oracle check** (scan new files for any normative rule absent from the oracle).
- **[MAJOR] C9b transitivity** (fork source = gc post-restructure, not the old METHODOLOGY dragonfly
  referenced) → **named transitivity assumption recorded** in C9b (gc-old→gc-new verified by gc's own run).
- **[MAJOR] Tier-2 missed cross-cutting-at-second-stage** → **SC-4 arm added** (B-TRI-1 triage at
  stage 7); SC-2 stage-7 GBP residual recorded.
- **[MINOR] stage-7 load floor** → §A.3 now pre-checks stage-7's rule-only floor before the cap binds.
- **[MINOR] mechanical count** → adopted. **[NITPICK] severity fork source** stage-4/6/7 → **stage-8
  SEV table + stage-4/7** (gc stage-6 has no severity table; author-verified).
Iteration-cap tally: gate-4 same-class bounces = **1**. → Re-run stage 3 (round 2) on the fixed
artifacts (carry round-1 findings forward). New pre-freeze hashes: spec `8f163fc8…`, criteria
`33e4cc39…`, plan `4832b9aa…`, oracle `09efa5e6…`.

**GATE 4 — ROUND 2 · worst severity = BLOCKER · ITERATION CAP FIRED → owner tie-break required.**
Cold reviewer: general-purpose, `claude-opus-4-8[1m]`; verbatim record `3-redteam-plan-round2.md`.
Round-1 fixes verified genuinely landed EXCEPT: B-1 [BLOCKER] the recount escaped into `2-plan.md`
(still "78" at :5/:56/:122); B-2 [MAJOR] the broadened C9a grep is still adjacency-anchored → still
misses SKILL:107 + METH:394; B-3 [MAJOR] the "closed-set input" rule is still forked in (not current
dragonfly behavior, not oracle'd — same over-fork class); B-4/B-5 [MAJOR] two more real stage-9 rules
missing from the "complete" oracle (residuals re-check; characterized-handoff verification); plus
[MAJOR] METH:420 by-reference clause not flagged for edit in the C-REF-1 mapping.
**Cap analysis:** the reviewer frames all five as the **same finding classes** as round-1 (count
consistency; C9a completeness; charter over-fork; missing-oracle-rows). Per SEV4 ("2 bounces at the
same gate on the same finding class, regardless of wording → human breaks the tie"), gate-4 same-class
bounces = **2** → **cap fired.** Not silently continuing to round 3. **All findings are real, fixable,
and do NOT challenge the direction** (reviewer re-affirms goal/sequencing/Tier-2/C10). Escalated to
owner with a recommended path (thorough round-3 fix + harden the "no rule lost" guarantee to rest on
build-vs-SOURCE, not solely the hand-oracle; then one final review). **AWAITING OWNER TIE-BREAK.**

**OWNER TIE-BREAK (2026-07-06, ThinkerOfThoughts): → ROUND-3 (rigorous path).** "Fix everything +
harden C1 to rest on source-vs-build + re-derive the oracle's completeness independently, THEN one
final cold plan review; freeze only if clean." Actions taken:
- **B-1** (count escaped into plan) → propagated to **86** everywhere; added a **freeze checklist**
  (count-token grep) that would have caught it.
- **B-2** (C9a grep still adjacency-anchored) → **C9a rewritten as read-confirm + whole-file
  read-and-classify of every `guarded-change` hit** (grep locates, human read classifies — no
  adjacency blind spot); KEEP set enumerated inline (a-e) in the plan.
- **B-3** (closed-set over-fork) → **closed-set-input rule EXCLUDED** from the fork (source grep
  confirms it absent from current dragonfly → exclusion is faithful); recorded as the 4th divergence.
- **B-4/B-5** (2 missing stage-9 rows) → **A-9-6 + A-9-7 added.**
- **METH:420** → C-REF-1 row flagged: "referenced from guarded-change" clause becomes "dragonfly's own charter".
- **C1 hardened** to check build-vs-SOURCE (not just oracle): (i) oracle→new, (ii) SOURCE→new
  rule-by-rule at stage 6, (iii) reverse anti-oracle — so an oracle gap cannot hide a dropped rule.
- **Independent oracle-completeness re-derivation** run (`3-oracle-completeness-round3.md`): cold
  enumerator, ~86 source statements enumerated fresh; verdict **essentially complete, no spurious rows,
  no further load-bearing gaps**; added 3 principle/catch-all rows (B-EVID-1, B-CAUS-1, B-CH-inherit) +
  widened B-TBG-1. Oracle now **86 rows** (35/34/17, mechanically counted).
→ **Round 3 cold plan review** (final; carry rounds 1+2 forward). Per the tie-break, freeze ONLY if
round 3 is clean; another same-class blocker returns to the owner.

**GATE 4 — ROUND 3 · worst severity = MAJOR (NOT blocker) · verbatim `3-redteam-plan-round3.md`.**
Reviewer **certified the frozen oracle complete/correct/correctly-scoped** (86 rows, independently
reconciled across sections prior rounds under-examined; all additions verbatim-verified, none spurious)
and affirmed direction + C1 source-anchoring. Three residual MAJORs, **all plan construction-guidance
drift, none in the oracle, none a blocker** — reviewer's explicit disposition: *"apply the three fixes
→ freeze-ready; a mechanical touch-up, not another full red-team lap."* Applied **fix-in-place** +
mechanically verified:
- **B-1** (§A table omitted A-9-6/A-9-7/B-EVID-1/B-CAUS-1 + false completeness claim) → integrated into
  their §A stage rows; **abbreviation-aware coverage check = 0 genuine gaps across all 86 IDs**; note
  corrected; **freeze-item 5 added** (every oracle ID in a §A row).
- **B-2** (plan:17 stale "closed-set" as included) → moved to EXCLUDES ("provenance record-elements
  only"); verified.
- **B-3** (C9a KEEP allow-list under-inclusive) → added KEEP category **(f) triage/lite-routing
  composition** + changed the pass rule to **composition-vs-rules-dependency** (examples, not a closed
  list); verified.
- Minors: "3 arms"→"4 arms" (verified 0 stale); nitpick transitivity = named-not-re-verified by design.
Cap note: round-3 residuals are **fix-in-place (minor-class disposition per the reviewer)**, not a
same-class *blocker* → the owner's escalation trigger did not fire. **BUT the tie-break said "freeze
only if clean" and round-3 was not clean-at-review → freeze decision surfaced to the owner** (not
self-frozen). Post-fix pre-freeze hashes recomputed below. **AWAITING OWNER FREEZE DECISION.**

**GATE 4 PASSED — FROZEN (owner ThinkerOfThoughts, 2026-07-06: "Freeze + build").** Route: round-3
residual majors fixed-in-place + mechanically verified; owner authorized freeze. Freeze-checklist:
oracle count **86** (mechanical); "86" consistent across criteria/plan/oracle; closed-set absent from
current source; no stale count/arm tokens. **Frozen sha256:**
- `1.5-criteria.md` = `1f3c7684e4118c0903227779259f0cc96817440b345441426ac681bd80f60c33`
- `2-rule-oracle.md` = `cc4d988f6abad9279794187c2a011514a92d7e696ac11eef045632fa0f1ec0a6`
- `2-plan.md` = `ad803c5e432494690b3889fceb0bacbc48fb01ad6a3a65f7a9c4da03a3a3667a`
- `1-spec.md` = `8f163fc8bbb99f9b7decc6872fa51f2d16f993ad71c1eeb7aabb3b96b35cd601`
Gate-4 same-class bounce tally at freeze: 2 blocker rounds (owner tie-broke) + 1 major round
(fix-in-place). → **Stage 5 (build)**: construct the 14 files per §A; then stage-6 code red-team vs the
frozen criteria/oracle (mechanical `git diff`), gate 7, stage-8 Tier-2 harness, install, commit.

**Stage 5 (build) DONE** — 14 files (`5-build.md`). Self-checks: per-stage load ≤223 (33% of 670,
under ~270 cap); C9a de-coupling clean (39 guarded-change mentions all KEEP-composition, zero
rules-dependency). Mechanical diff `6-build.diff` (14 files, +622/−563); original source extracted from
`3d6889b` for the C1 source-walk.

**Stage 6 (code red-team) — verdict CLEAN** (`6-redteam-code.md`). Cold reviewer general-purpose
`claude-opus-4-8[1m]`. C1/C5/C9/C10 all PASS (86 rows spot-sampled + source-walk found no dropped rule;
39 guarded-change hits all KEEP; 4 forked pieces faithful; 4 exclusions recorded; D-11 retired; KEEP
relationships intact). Worst severity = **nitpick** (B-TBG-1 written only at stage-4/5 though oracle
scope `4,5,6,7`; reviewer confirmed source-faithful — never at 6/7 in the original either).

**GATE 7 — worst severity NITPICK → fix-in-place, proceed.** Applied the B-TBG-1 nitpick fix: concise
trust-before-gate statement added to `stage-6.md` + `stage-7.md` (so C1 is unambiguously clean vs the
frozen `4,5,6,7` scope). Fix diff: +4 lines (2 per file), no rule reworded. → **Stage 8 (Tier-2
harness):** C2 4-arm behavioral spot-check + C4 install/diff + per-criterion verification table.

**Stage 8 (Tier-2 harness) — `8-harness.md`.** All gating criteria PASS:
- **C2 behavioral spot-check: 4/4 arms FIRED** under per-stage isolation (SC-1 rep-gate@1, SC-2
  gate-before-present@3, SC-3 clean-factual-earned@7, SC-4 triage-token-burn@7), each opening only its
  routed file(s) → **C3b isolation holds.** No BROKEN control (non-discriminating twice).
- **C1** PASS (stage-6: 86 rows + source-walk, no dropped rule); **C3a** PASS (heaviest load 227 = 34%
  of 670); **C4** PASS (live==source diff clean, installed to `~/.claude/skills/dragonfly/`); **C5**
  PASS; **C6** PASS (router resolves mechanically + behaviorally); **C9a** PASS (39 gc hits all KEEP,
  zero rules-dependency); **C9b** PASS (fork faithful, exclusions recorded); **C10** PASS (relationships
  intact). Advisory C7 PASS, C8 recorded (729 vs 670 by design).
- Residual (named, non-blocking): Tier-2 sampled 4 of 86 rules behaviorally; the other 82 rest on C1
  (oracle + source-walk) + C9a. The owner-chosen Tier-2 scope.

**GATE 8 — clean → DONE.** The restructure conforms: behavior-preserving, Theme-2 de-coupled, attention
budget reduced, live==source. → `9-report.md`, commit, memory update, deferred cleanup (both runs now done).
