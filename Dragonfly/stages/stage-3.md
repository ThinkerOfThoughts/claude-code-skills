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

**The gate binds a side-diagnosis too (B-LOUD-1, presentation half).** The gate-before-present tiers
govern **any** diagnosis surfaced in the hunt — including a fast **side-diagnosis** made in passing,
off the frozen `S#` target (e.g. "why is it slow?") — not only the frozen `S#` hypotheses. A
side-diagnosis is **not exempt** from reproduce → measure → **toggle** → conclude because it is quick
or off the critical hunt path: an untoggled side-diagnosis is `ungated` and may not be presented or
acted on as the cause. (Distinct from a parked *incidental finding*, which is an unrelated bug you do
**not** chase at all; here you have actually made a diagnosis. The author-side observation half — the
log-salience trap, the loudest log line is a correlation, verify the critical path before attributing
— is at stage 2; the convergence-gate backstop is at stage 6.)

## The timeline rule (B-TIME-1, mandatory)

A root cause **cannot post-date its symptom.** If a symptom exists in the past, its root cause exists
in the past. So for every candidate: establish (a) the symptom's **first-appearance** version/point
and (b) the candidate factor's **introduction** version/point — both cited — and **discard as *root*
any factor introduced after the symptom first appeared.** Such a factor may still be an
**exacerbating/amplifying** contributor (rank it as one, not as root). Establishing the two points is
part of forming the hypothesis — a candidate whose timeline is unestablished stays `ungated` and may
not be ranked as leading.

## The design-intent rule (B-DES-1, for an empty/absent-input symptom)

When the symptom is a component **failing on an empty or absent input**, do NOT form the root
hypothesis as "make the empty case stop firing." Read the component's **stated design intent** (its
docstring / the plan or spec it implements) and the **shape of its OTHER inputs**, then ask what the
operation is **supposed** to produce. The content is often **present but mis-routed**, not missing: if
a sibling input carries the expected content **non-empty**, "the empty slot fired" is a **relay** (a
symptom/mitigation-shaped attribution — cf. B-TARGET-1), and the real root sits **upstream** (a
mis-route, or a missing branch that sent the content to the wrong place). A hypothesis that would have
the design produce *less* than its documented purpose (a slot that should be filled staying empty) is
suspect on its face; establish the design intent as part of forming it. (Motivating case: a compaction
tier folded with an EMPTY new-messages slot → refusal; the tell skipped was that the existing-memory
slot was NON-EMPTY — a graduated prior mis-routed into a fold prompt with an empty transcript, i.e. a
missing prompt-branch upstream, not an "empty case" to suppress. The fix-direction half of B-DES-1 — a
recommended fix must not contradict the module's documented purpose — is at stage 8.)

## Cross-cutting rules governing this stage

**Never present an ungated hypothesis as the likely/leading cause (C-HIL-2).** Candidate (`ungated`) →
leading candidate (`test-passed`) → root cause (`cold-red-teamed`); ranking the candidate list is
always fine. (This is the gate-before-present rule restated as a stop-for-human duty.)

**Evidence over rhetoric (B-EVID-1).** Every hypothesis's confirm/refute prediction and its ranking
cite the observations behind them; "seems like X" is not a finding.

**Verify, don't just cite (B-VER-1).** A hypothesis's confirm/refute predictions, its ranking, and any
timeline point (B-TIME-1) are **verified against source**, not asserted from memory — including claims
the agent just made or ones carried in a memory note. (Full rule at stage 2 — including **B-GT-1**: a
hypothesis resting on a quantity *derived* from the data must have that quantity re-derived from the
actual ground-truth records, not a proxy schedule/config/aggregate, before it is ranked as leading.)
