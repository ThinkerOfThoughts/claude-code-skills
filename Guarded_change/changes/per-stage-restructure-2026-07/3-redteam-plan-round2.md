# 3-redteam-plan-round2.md — stage-3 cold review, ROUND 2 (verdict: MAJOR → iteration cap fires → owner tie-break)

## Provenance
- **Reviewer:** cold subagent, `general-purpose`, model `claude-opus-4-8`, no shared context.
- **Run:** 2026-07-06, task `a0e6f9aa22c57e3ff`; ~5.6 min, 20 tool uses, ~68K tokens.
- **Artifacts under review:** revised 1-spec / 1.5-criteria / 2-plan + NEW 2-rule-oracle.md
  (hashes below, reviewer-self-reported).
- **Disposition:** both round-1 blockers (L1, C-2) and all round-1 majors/minors verified
  genuinely resolved. 5 new/residual **majors**, all fixable at stage 2 without redesign;
  several are round-1 classes resurfacing in new spots → **iteration cap (2nd major bounce
  at gate 3, same finding classes) FIRES → owner tie-break** on the re-verification route.

## Charter (verbatim summary)
Stage-3 ROUND 2 cold review. Tasks: (1) resolution check of every round-1 finding (quote
revised text); (2) **oracle audit** — independently check `2-rule-oracle.md` against the
current source for missing rules / wrong governing-stage-sets (the oracle is now C1's ground
truth, so its completeness is load-bearing); (3) fresh pass — four lenses + position lens +
label audit + coverage challenge, new defects count fully, hunt specifically for split-
introduced failure modes (stale router rows, a rule needed in a stage file but only in the
slim METHODOLOGY, cross-file drift). Closed context set: revised docs + oracle + round-1
record + current METHODOLOGY/SKILL + decisions.md. Full charter in task transcript
`a0e6f9aa22c57e3ff`.

## Reviewer output (verbatim)

### Context file hashes (reviewer self-computed)
```
35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3  Guarded_change/METHODOLOGY.md
4e2a2e5135ce0d3397fa208a18e4f1715e22e3738b99bca16cea153e7302839b  Guarded_change/SKILL.md
7fc2ee6a87c8a3d9ce68f92b64df5065e47c29f6d4466ed83aeec9d316803f59  1-spec.md
8368f5711b5df3b62e1653a61ddfa523e48ddcf7081287e8e78a76480dbd1195  1.5-criteria.md
372e5dcc421bf1c5549614cc70b55cca2074acdba27e76ca82a0feea4adf124e  2-plan.md
df9c43ce51e99e4fb9d1d6539dec79554bcd2bc84c33dc91a692197b8e9dda66  2-rule-oracle.md
3d4cf74d463fc238ccfec390664dbcd80798261d479d211b2a7a0f339d0b4f1a  3-redteam-plan.md (round-1)
5f6188a0c273ec8bf67549f924d594ce6d9093aba150bb787b219a36a9da806e  decisions.md
```
Line counts verified: METHODOLOGY 534, SKILL 124.

### Resolution check — both round-1 BLOCKERS resolved, all majors/minors resolved
- **L1 (blocker) RESOLVED:** battery re-architected to 5 stage situations placing an agent AT
  the stage each rule governs; gate-4+ rules now fire (criteria-freeze/severity-routing/
  iteration-cap → SIT-4; gating-verified-by-execution → SIT-8). Residual: no SIT-6 (→ CC-1).
- **C-2 (blocker) RESOLVED:** new C3 with (a) static ≤40%-of-658 load + (b) behavioral
  file-open measurement from battery transcripts. Residual: line-vs-token target (→ F-1).
- **F1/F2/F4/L2/L3/L4/A1/A2/M1/M2/M3/C-1/C-3/C-4/C-5/P2/P3/P4/F3/L5/A3** all verified
  resolved (file-per-stage split adopted; independent grep-derived oracle; positive control;
  reference-section rules moved into stage files; router-correctness criterion C6).

### Oracle audit — "substantially complete and correctly scoped"; one MAJOR-adjacency residual
- No material missing rules; FRZ→{4,8}, CFG3→{R,3,4,6}, ART3→{4,7,8}, CP4→{1.5,8}, H6/CH6/H8
  all present + correctly scoped (round-1 F1/F2/L4 genuinely fixed).
- **O-1 [MAJOR-adj]:** the stage-3 and stage-6 charter *cores are deliberately different*
  (METHODOLOGY:241-244 — stage-3 core = lenses+discipline+coverage-challenge+label-audit;
  stage-6 core = lenses+discipline only). No oracle row states this asymmetry, and C5's
  "repeated rules must agree" sweep could mis-flag it as drift OR let a builder "fix" it by
  widening CH8/CH9/CH10 from {3} to {3,6}. The round-1 self-reference bug re-emerging inside
  the fix. → fix: oracle note + scope C5 to *shared* rules only.
- O-2/O-3/O-6 minors: self-check criteria must survive the SKILL slim; CP3→{2} wants an
  explicit justification; HIL should include gate 7.

### Fresh-pass majors
- **A-1 [MAJOR]:** gate files may need the loop *routing map* (blocker→1, major→2) which lives
  in the slim METHODOLOGY "not in the hot path" — if not repeated into each gate file, the
  gate file isn't self-contained. (METHODOLOGY:91,304-309; 2-plan.md:19-24.)
- **CC-1 [MAJOR]:** no SIT-6 — stage-6.md (largest, full charter) self-containment never
  observed; ST6d (mechanical diff) never fires in any arm → build could ship a non-self-
  contained stage-6.md and pass all gates (round-1 L1/C-3 residual, narrowed to stage 6).
- **L-1 [MAJOR]:** OLD n=2 with ≥1/2 accepted as "situation valid" is a *weaker* bar than the
  ≥2/3 NEW bar it certifies; for probabilistic rules the A/B then can't separate preservation
  from noise. → raise OLD to ≥2/2 (or raise OLD n).
- **P-1 [MAJOR]:** SEV3 (no-silent-demotion) tested by SIT-4 for *presence*; its precedence
  force (reviewer-severity authoritative over author-contest) comes from adjacency to the
  severity table/SEV2 framing — a text-presence grader passes a position-weakened copy. →
  SIT-4 grader must require an actual *routing/precedence test* (route on the reviewer's
  severity against the author's contest), not a mention.
- Minors: F-1 (commit a token target, not just lines); L-2 (C3(a) "forced reference file" vs
  C3(b) "only router+stage file" tension — clarify); A-2 (does C5 cover METHODOLOGY's residual
  rule-restatements?); CC-2 (note SIT-0/1 out of scope); CC-3 (C6 behavioral check covers only
  the 5 situation stages); M-2 nitpick (drive C5 from the oracle's frozen cross-cutting list).
- Label audit: no mislabel (C3 correctly gating — had it been advisory it would be the C-2
  blocker in disguise).

### RANKED (worst first): A-1, CC-1, L-1, O-1, P-1 = MAJOR; O-3/F-1/L-2/A-2/O-2/O-6/CC-2/CC-3 = MINOR; M-2 = NITPICK; P-2/F-2/O-4/O-5/LA-1 = no issue.

**One-line verdict — worst severity: MAJOR.** No blocker. Both round-1 blockers resolved;
core architecture (file-per-stage + grep oracle + gate-positioned battery + behavioral C3)
sound; 5 majors are gaps at the seams the split creates, all fixable at stage 2 before freeze.
