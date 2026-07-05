# 3-redteam-plan.md — stage-3 cold review (verdict: BLOCKER → return to stage 1/2)

## Provenance
- **Reviewer:** cold subagent, `general-purpose`, model `claude-opus-4-8`, no shared context.
- **Run:** 2026-07-06, task `a21f65e02f00844d6`; ~5 min, 16 tool uses, ~60K tokens.
- **Artifacts under review:** 1-spec.md, 1.5-criteria.md, 2-plan.md (hashes below, reviewer-self-reported).
- **Verdict:** BLOCKER (L1 + coverage C-2). Route: gate 4 → return to stage 1/2; blocker
  restart → stop for owner direction (done: file-per-stage redesign decision).

---

## Charter (verbatim, as sent)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a guarded-change STAGE-3 cold review (four lenses + evidence discipline + coverage challenge + the POSITION lens + label audit) of the planning docs for a change that restructures the **guarded-change skill's own files**. The change ("Theme 1 / per-stage restructure"): reorganize `Guarded_change/METHODOLOGY.md` + `Guarded_change/SKILL.md` so content is laid out BY the loop's discrete stages (0,1,1.5,2,3,4,5,6,7,8), each stage section self-contained, with cross-cutting rules REPEATED into every stage they govern (not a separate always-on "spine"); SKILL.md becomes a thin per-stage router. Motivation: an attention-budget ceiling on Opus (the topic-organized docs force the whole 658-line set into view to run one stage). It is explicitly a REORGANIZATION, not a rewrite — no rule's wording/meaning/trigger should change.

CRITICAL: these are PROMPT files — a position-sensitive assembly. This change is exactly the class the skill's own core principle *Information-preserving is not behavior-preserving* warns about: moving/duplicating rules can change behavior while every word survives. Your review must treat behavior-preservation as the central risk.

[documents under review + closed-set context list as sent: 1-spec/1.5-criteria/2-plan; current METHODOLOGY.md + SKILL.md; decisions.md]

[Four separate lenses: FACTUAL (check the §A.2 distribution table against the current source for silent narrowing/omissions), LOGICAL (C1 decidability; C2 battery — do the 5 scenarios force every high-risk rule to fire; does the arm span make each rule manifest; is NEW≥OLD sound and is n=3 enough; does the battery exercise per-stage loading), MISSED OPPORTUNITY, UNSTATED ASSUMPTIONS (does a thin router actually reduce load). POSITION LENS (mandatory — rules whose effect depends on where they sit). LABEL AUDIT. COVERAGE CHALLENGE (mandatory). Evidence discipline: cite file:line, rank each finding, no-issue-per-lens allowed, clean factual needs citations, flag the unverifiable. Output verbatim as the review record; end with one-line worst-severity verdict.]
```

(Charter core = the METHODOLOGY four-lens + discipline + coverage-challenge + position-lens
bullets; task additions quoted above. Full prompt in the session transcript for task
`a21f65e02f00844d6`.)

---

## Reviewer output (verbatim)

This confirms a structural finding: the plan keeps "The config contract" and "What a run produces" as **always-on reference sections**, but these sections contain **stage-active, gate-blocking rules** — "Paths are validated" (which **blocks gate 4** and is active at every reviewer spawn / stages 3, 6) and the "decisions.md gate log" rule (which the **iteration cap depends on**, and which mandates a stage-8 gating-disposition entry). Leaving these in a "read as needed" bucket means the very rules the restructure is supposed to bring into per-stage view for stages 3/4/6/8 stay in a section the agent is *not* prompted to load per-stage — reintroducing the miss-under-load problem the change exists to solve, and not covered by C1's table (they aren't in it) or C2's battery.

I have enough to write the complete review. Let me assemble it.

---

# STAGE-3 COLD REVIEW — per-stage restructure of the guarded-change skill (Theme 1)

## Context file hashes (self-computed)

| File | sha256 |
|---|---|
| `Guarded_change/METHODOLOGY.md` | `35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3` |
| `Guarded_change/SKILL.md` | `4e2a2e5135ce0d3397fa208a18e4f1715e22e3738b99bca16cea153e7302839b` |
| `changes/per-stage-restructure-2026-07/1-spec.md` | `06b95c02ed58a6a6c0f1b8911c2491a0e2a7b35221fadfac9543f635b044b149` |
| `changes/per-stage-restructure-2026-07/1.5-criteria.md` | `dfa9f16426ded60cf922b0a1a4ba181564f8abd98af12f78266aabdb3492d2b2` |
| `changes/per-stage-restructure-2026-07/2-plan.md` | `65d1d6b81e68c86039b6e658dd1dc33594b7a4da467e0fefd8d709b4aab91f5c` |
| `changes/per-stage-restructure-2026-07/decisions.md` | `2832d9b7aec4cec143e8f31b03ee6730b350413457efe15539d4d7a991fd9de9` |

Line counts verified: `METHODOLOGY.md` 534, `SKILL.md` 124.

[FULL LENS-BY-LENS REVIEW — verbatim, see the ranked findings table below for the
consolidated set; the per-lens prose is preserved in the task transcript
`a21f65e02f00844d6`. Key content reproduced:]

**LENS 1 — FACTUAL:** F1 [MAJOR] §A.2 maps "Criteria freeze" to stage 4 only; METHODOLOGY:172
gives it a stage-8 verify-unchanged duty — a silent narrowing. F2 [MAJOR, cumulative] table
omits cross-cutting rules: paths-validated (473-479, blocks gate 4), unreviewed-check
(387-395), spot-verify-citations (232-235), regression-comparable-workload (412-420),
stage-6 mechanical-diff (191-193), human-in-loop (524-535); and C1's oracle is that same
incomplete table (self-referential). F3 [MINOR] "A bar, set first" is cross-stage (1.5→8),
mapped to 1.5 only. F4 [MAJOR] reference-section rules (path-validation, decisions.md
gate-log) stay always-on, defeating the per-stage goal for gate-blocking rules.

**LENS 2 — LOGICAL:** L1 [BLOCKER] the arm span (stop at stage 3, charter-not-execute) makes
4 of C2's 8 rules — criteria-freeze, severity-routing, iteration-cap, gating-verified-by-
execution — impossible to fire in any arm; grading collapses to text-presence for them,
un-running C2's core purpose. L2 [MAJOR] n=3 with no per-rule base-rate/power justification
can't separate a real fire-rate drop from sampling noise; "no downward tolerance" → both
false blockers and masked real drops. L3 [MAJOR] per-stage loading is enforced only by prose;
a diligent NEW arm reads the whole file → the A/B is null by construction while "passing."
L4 [MAJOR] C1's "correctly scoped" has no independent ground-truth stage-set per rule; its
only oracle is the incomplete §A.2 table. L5 [MINOR] S3's concurrency rule's real
manifestation (executed interleaving, stage 8) is unreachable by the arm span.

**LENS 3 — MISSED OPPORTUNITY:** M1 [MAJOR opp] a physical section-split (file-per-stage,
`stage-3.md`…) enforces per-stage loading by the filesystem — resolves L3/L4, makes C1
decidable per-file, makes the A/B non-null. M2 [MAJOR opp] derive C1's ground truth by
grepping the current source's stage cross-references NOW, as a frozen stage-1.5 oracle —
surfaces F1/F2 before the build. M3 [MINOR opp] a deliberately-broken NEW variant as a
positive control calibrates n and proves the battery can catch a known-removed rule.

**LENS 4 — UNSTATED ASSUMPTIONS:** A1 [MAJOR] "thin router reduces load" is unvalidated and
may invert — the harness auto-loads SKILL.md in full; detail merely moves to a longer
METHODOLOGY (~780 lines) the agent may read whole. A2 [MAJOR] "repetition costs no attention"
holds only if per-stage loading holds; if it fails, the 780-line file is strictly worse than
today's 534 — and no criterion measures loaded tokens (C6 measures lines, which rise by
design). A3 [MINOR] blind grader stripped of skill files may under-detect subtle firings in
both arms. A4 cost stated, sufficiency asserted.

**POSITION LENS:** P1 the position lens itself is adequately targeted (S1, arm reaches stage 3).
P2/P3/P4 [MAJOR] earned-clean-label guard, no-silent-demotion (precedence-adjacent to the
severity table), and cap↔gate-log coupling derive force from sibling adjacency; per-stage
isolation could weaken them and C2 can't make them fire (arms never reach the gates).

**LABEL AUDIT:** no mislabel (C5/C6 correctly advisory; C1–C4 correctly gating). The concern
is a MISSING gating criterion (attention budget), not a misweighted one.

**COVERAGE CHALLENGE:** C-1 [MAJOR] no scenario forces the label-audit to fire. C-2 [BLOCKER]
the change's primary motivation (attention/loaded-token budget) is unmeasured by any
criterion; the change could regress it and pass all gates. C-3 [MAJOR] gate-4-and-later
firings (freeze-verify, routing, cap, stage-8 execution) unobserved. C-4 [MED] reference-
section rule firings unobserved. C-5 [MED] router indirection correctness (does §N point right
and carry §N's duties) not checked by C4's static sweep.

**One-line verdict — worst severity: BLOCKER** (L1: C2's arm span cannot fire ~half its
registered rules, collapsing the mandatory behavior-preservation criterion to text-presence;
and C-2: the change's own primary motivation, the attention budget, is unmeasured). Route:
gate 4 → return to stage 1/2 to (a) extend the C2 arm span past the gates its rules fire at
or replace text-presence grading for gate-4+ rules, (b) enforce per-stage loading mechanically
(M1) or measure loaded tokens (C-2), and (c) correct/complete the §A.2 distribution table and
give C1 an independent grep-derived oracle (F1/F2/L4/M2).
