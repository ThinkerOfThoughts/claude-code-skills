# 9 — Final report: audit-hardening-2026-07 (C7 duties)

Guarded-change skill hardened via its own loop: 9 additive fixes (F1–F9) landed in
METHODOLOGY.md (467→534) + SKILL.md (102→124), all gates passed, installed to live,
committed. This report carries the C7 reporting duties.

## 1. Structural flags for OWNER DECISION (deliberately NOT built — additive-only constraint)

- **S1 — Attention-budget ceiling on Opus.** The documents grow with every patch (now
  534+124) and each new lens dilutes the others; at some size the marginal rule costs more
  compliance than it adds. This run's own data makes S1 concrete: the V3
  engaged-and-misread pattern (below) is attention-shaped, and the C3 instrument had to be
  re-planned around per-seed reviewer attention. Candidate rework: a one-screen per-stage
  mandatory checklist up front, full spec as reference appendix; per-lens trigger index.
- **S2 — SKILL/METHODOLOGY dual-maintenance.** Same rules stated twice; every change edits
  both; drift is a standing hazard (F9's standing consistency criterion now mitigates;
  C2's 7-item sweep is the per-change cost). Candidate rework: single source of truth,
  SKILL.md reduced to operating procedure + pointers.
- **S3 — decisions.md integrity rests on convention.** Append-only is asserted, not
  enforced; the same author writes it. Low priority in a self-trusting workflow; a
  mechanical guard (hash-chain or commit-per-gate) matters only if run adversarially.

## 2. C3 evidence + caveats (the honesty block)

- **What three rounds established** (13 Opus arms total; n=3 per arm in the deciding round —
  directional evidence, not statistical proof):
  - **F1 (provenance): the strongest demonstrated effect.** Treatment 7/7 across rounds
    (4/4, 3/3) vs control 0/7 — every treatment arm ruled the provenance-free stage-3
    review un-run citing the new rule; no control ever did. Clearly NEW behavior.
  - **F3 (evidence column): new behavior, not codification.** Treatment 5/7 (3/4, 2/3) vs
    control 0/7; the grep record confirms the rule is unreachable from the pre-change docs.
    The two treatment misses are attention-shaped (round-3's T6 even misread C1's row as
    "evidence cited").
  - **V4 (pre-existing deferral rule): 14/14 across all arms and rounds** — the amendments
    did not displace the loop's hardest rule (the insertion cluster's nearest neighbor).
  - **Rounds 1–2 history (carried verbatim, per the criteria):** V1 4/4-T vs 0/4-K; V2
    3/4-T vs 0/4-K; V4 8/8; V3 1/4-T vs 3/4-K (pooled 4/8, across two fixture wordings).
    Round 3: V1 3/3-T:0/3-K, V2 2/3-T:0/3-K, V4 3/3+3/3, V3 0/3-T:1/3-K.
- **Honest driver [pre-committed]:** the round-3 PASS's largest single driver is the
  **owner-authorized V3 demotion to observational** — not the differential-scoring change.
  Under the round-2 rules, round 3's V3 record (0/3-T) would have failed the battery again.
- **Codification caveat:** V4's 14/14 shows the pre-existing deferral rule fires reliably
  in both arms — so C3 demonstrates F1/F3's *additive* value, not that the whole amendment
  set is load-bearing. V2's control silence + grep-absence is the codification rebuttal
  for F3 specifically.
- **Instrument history:** two failed rounds (absolute per-seed bars vs attention noise;
  a fixture not conformant under the amended rules → legitimate off-seed fires), one
  owner tie-break to re-plan, fixture v2 (FX-A/FX-B) + differential scoring v3.1. FX-A
  verifiably defused the round-1/2 killer class: round 3 had ZERO off-seed fires on the
  harness-check class — all six arms instead used the in-fiction `6b` record as
  load-bearing evidence.

## 3. Residual-displacement note [AR-1]

C3's V4 probe (14/14) and round 3's V3 tripwire (not triggered: 0/3-T with only 1/3-K)
are **spot-check evidence, not proof, of non-displacement**. The amendments add ~89 lines
to a position-sensitive assembly; C4 bounds raw growth but cannot see attention dilution.
The V3 record (cumulative 1/7-T vs 4/7-K) is consistent with noise at this n but its
direction is the one displacement would produce — it remains an open observational flag,
folded into S1's owner decision.

## 4. The earned-clean reliability finding (largest incidental discovery)

The PRE-EXISTING "a clean factual lens must be earned with citations" rule is applied by
Opus only ~45% of the time when the record *looks* diligent (V3 cumulative: 5 catches /
11 arms that faced it). Round 3 sharpened the mechanism: three of five misses **invoked
the rule and then credited citations that do not exist** (T5/T7: "earned with citations" /
"citation trail" about a zero-citation lens; K7: crediting descriptive topic-mentions as
citations) — a diligence-halo failure, symmetric across doc sets, unfixed by any wording
tried (verbose vs terse lens made no difference: 3/4 vs 1/4 then 1/6). **Future-hardening
candidates (not built, needs its own loop):** define citation mechanically (= file:line or
log row present in the lens's own text); instruct consumers to audit the OUTPUT text, not
the charter's promises.

## 5. Attention-budget spend [AR-3/AR-4]

- Doc growth: METHODOLOGY +67 lines (467→534, cap 583), SKILL +22 (102→124, cap 127),
  combined 658/671. SKILL is 3 lines under its cap — the next SKILL-side rule likely
  forces an S1/S2 decision.
- Run cost: ~20 cold subagents across the loop (2× stage-3 rounds on the plan + 2 on the
  v3-delta, 1 stage-6, 5 fixture checks, 14 battery arms, 1 scoring verifier) plus the
  fixture builds and three battery rounds. The C3 instrument consumed roughly half the
  total spend; its per-seed lessons (differential scoring, both-rule-set fixture
  conformance, hedged-flag extraction, verbatim freeze copies) are reusable.

## 6. Process notes for the record

- The loop's new rules were dogfooded mid-run and repeatedly caught the author: F2
  targeted checks caught a dangling cross-context reference (check #4 M1) and a
  seeded-hash mismatch (m2) in the author's own fixture build; F5 routing honored two
  owner tie-breaks; F4 freeze/unfreeze/re-freeze executed with hash + verbatim copy after
  the hash-only freeze went dark across the unfreeze (v2 reconstructed and hash-proven).
- One scoring-verifier transcription artifact (a garbled 62-char hash in prose) recorded
  in `6-fixture-check-5.verbatim.md` — content citations proved the correct file was read.
