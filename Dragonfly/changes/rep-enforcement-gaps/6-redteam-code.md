# 6 — Red-team of the built change (verbatim record)

## Provenance
Cold `general-purpose` subagent, no shared context (agentId ab3f20181452f49e1), Claude Opus 4.8.
Mechanical diff regenerated off base c8db6fa. Context: built files (stage-2/4/5/6, SKILL,
METHODOLOGY) + criteria + plan + base blobs + live tree. Paths validated.

## Verdict: **MINOR** — one stale accept-bar line (now fixed); build itself CLEAN.

- **Factual (earned):** every planned edit present verbatim in the right section — E0a A-4-2
  (stage-4:13-19, after A-4-1, writes decisions.md), E0b B-REP-4 pointer (stage-4:34-36), E1a B-REP-4
  (stage-5, all 5 rubric elements incl. ledger-evidenced + multi-axis + untrusted-negative), E1b
  B-REG-1 (stage-5, incl. no-registration-is-a-defect), E2 B-TARGET-1 (stage-2, all 6 elements), E3
  tie-in (stage-6), E4a/E4b (SKILL scope + pointer), E5 (METHODOLOGY scope). IDs collision-free in
  base (0 hits each). Scope: "governs stages 1, 4, and 5" 1 hit each; "governs stages 1 and 4" 0 live
  hits. C9 live==source exit 0.
- **Logical:** round-1 MAJOR closed non-vacuously (A-4-2 creates the referent; B-REG-1 nails the
  skip-registration loophole shut). Round-2 fixes landed: stage-6 tie-in uses cycle/elimination vocab
  (no "decrement/budget"); A-4-2 → decisions.md (not observation ledger), consistent with A-2-1. C4
  composition holds: "do not pull it" scoped to confirmed drift; doubt routes to pulling.
- **Position/behavior (C8):** exactly 3 deletions = 2 scope-word swaps + 1 re-flowed SKILL incidental
  sentence tail (pointer appended). No existing rule body altered; A-4-2 inserted without displacing
  the "Before it is run" bullet; all numbered cross-refs resolve.
- **MINOR (doc-consistency, not a build defect):** C2b in 1.5-criteria.md said "observation ledger"
  where the as-built (correct) destination is decisions.md — accept-bar text was stale. **RESOLVED:**
  C2b corrected to `decisions.md`.
- Coverage-challenge: verified bytes/positions/deletions/ID-collision against the base blob +
  live==source, not just greps; pointer targets all resolve. Nothing else uncovered.
