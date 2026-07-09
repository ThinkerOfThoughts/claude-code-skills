# Stage 3 — Hypotheses

**What this stage does:** form a ranked list of falsifiable candidate root causes, each with a gate
marker that governs how it may be presented to the human.

## Procedure

- **A ranked list of candidate root causes in `hypotheses.md`, each falsifiable** (A-3-1): it names the
  observation that would **confirm** it AND the one that would **refute** it, and carries a status
  (open / confirmed / refuted).
- **No hypothesis is held without a discriminating test** that could distinguish it from its rivals
  (A-3-2).
- **Each hypothesis carries a gate marker** (A-3-3), distinct from its status:
  `ungated` → `test-passed` (its stage-4/5 discriminating test has run and been cold-reviewed — this
  certifies the *test*, not yet the causal story) → `cold-red-teamed` (its stage-7 causal chain has
  passed a cold pass). The marker records, as a fact rather than a memory, what independent challenge
  has actually fired for this hypothesis.

## The gate-before-present rule (mandatory)

A hypothesis may be **formed and ranked freely** — think out loud in the working notes and keep a
ranked candidate list. What is gated is **how a hypothesis is presented to the human**, and the gate
has tiers matching what has actually been independently challenged:

- **`ungated`** (no cold pass yet): present it only as a **"candidate, ungated."** Never as the leading
  / likely / probable / most-likely cause, and never as a conclusion to act on (B-GBP-1).
- **`test-passed`** (its stage-4/5 discriminating test has run and been cold-reviewed): that cold pass
  certifies the **test artifact** — representative, un-confabulated, ruled a rival in or out — **not**
  the causal story. It may be presented as the **"leading / best-supported candidate so far,"** but
  must carry that its **causal chain has not yet been independently red-teamed** — it is not yet "the
  cause" (B-GBP-2).
- **`cold-red-teamed`** (its stage-7 causal chain has passed a cold pass): only now may it be presented
  as **the root cause** ("confirmed" additionally needs the stage-7 three-part bar) (B-GBP-3).

**Rank is not endorsement (B-GBP-4).** Showing the ranked candidate list, and saying which is most
*plausible so far*, is allowed and expected. The forbidden move is calling an **ungated** hypothesis
the cause, or presenting any hypothesis as a **conclusion to act on** before its tier permits. The
motivating slip: a hypothesis was presented as the "leading" cause with no cold red-team, no repro, no
toggle — and the cold pass, when finally run, refuted it as dead code.

## The timeline rule (B-TIME-1, mandatory)

A root cause **cannot post-date its symptom.** If a symptom exists in the past, its root cause exists
in the past. So for every candidate: establish (a) the symptom's **first-appearance** version/point
and (b) the candidate factor's **introduction** version/point — both cited — and **discard as *root*
any factor introduced after the symptom first appeared.** Such a factor may still be an
**exacerbating/amplifying** contributor (rank it as one, not as root). Establishing the two points is
part of forming the hypothesis — a candidate whose timeline is unestablished stays `ungated` and may
not be ranked as leading.

## Cross-cutting rules governing this stage

**Never present an ungated hypothesis as the likely/leading cause (C-HIL-2).** Candidate (`ungated`) →
leading candidate (`test-passed`) → root cause (`cold-red-teamed`); ranking the candidate list is
always fine. (This is the gate-before-present rule restated as a stop-for-human duty.)

**Evidence over rhetoric (B-EVID-1).** Every hypothesis's confirm/refute prediction and its ranking
cite the observations behind them; "seems like X" is not a finding.

**Verify, don't just cite (B-VER-1).** A hypothesis's confirm/refute predictions, its ranking, and any
timeline point (B-TIME-1) are **verified against source**, not asserted from memory — including claims
the agent just made or ones carried in a memory note. (Full rule at stage 2.)
