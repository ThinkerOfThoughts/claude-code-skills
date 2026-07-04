# 9 — Final report: dragonfly audit-hardening-2026-07 (the C7 record)

**To the owner (ThinkerOfThoughts).** The run is COMPLETE and PASSED: all 14 additive fixes
(D-1..D-14, + the L-3 stop-point wiring) are built into `Dragonfly/METHODOLOGY.md` +
`Dragonfly/SKILL.md`, installed live, and verified against the frozen criteria C1–C8
(evidence: `8-harness.md`; gate log: `decisions.md`). This report carries the items the
frozen C7 criterion obligates the run to put in front of you — the honesty items that must
not silently vanish from the record.

## 1. Structural findings — NOT built, yours to decide (each would be its own run)

- **D-S1 — Attention budget.** The two files are now 521+149 = 670 lines (baselines
  441+129 = 570) and growing with every hardening pass; the same prompt-attention ceiling
  argument as guarded-change's S1. This run's fixes are written terse and pointer-style,
  and growth was capped (≤ +18%), but the trend line points at a **checklist-first
  restructure** eventually — a future owner decision, deliberately out of scope here
  (additive-only constraint).
- **D-S2 — Unversioned coupling to guarded-change.** Dragonfly inherits its reviewer
  charter/severity model/rubric/lite definition from guarded-change **by reference** —
  deliberate and good, but unversioned: a guarded-change edit changes dragonfly's behavior
  with no dragonfly-side review. This run added **detection** (D-11: the self-check now
  fires on any edit to either skill and requires every named cross-reference to resolve —
  SKILL:142-146; and this run's C3 verified all five references against guarded-change at
  `9cec23d`). The structural fix — version pinning, or a shared "charter core" file both
  skills import — is a bigger design call, not made here.
- **D-S3 — The 0a confirmation checkpoint has no timeout/async path.** Stop-for-human at
  0a is correct, but in an autonomous/overnight context the hunt simply halts. Possible
  future: a provisional-freeze mode (proceed on the restatement, marked unconfirmed;
  re-confirm at first human contact). Needs your judgment on the risk trade — not built.

## 2. The no-battery residual (named), and what evidence exists instead

**No replay A/B battery was run for dragonfly** — a deliberate, owner-visible scope
decision made at gate 4. Rationale: the sibling guarded-change run had just measured this
amendment class's behavioral effect at 13 arms' cost, and dragonfly's amendments govern
*hunt conduct*, which has no cheap synthetic-record analog. What was run instead — the
owner-adopted (gate-4 tie-break, 2026-07-04) **C8 retrodiction**: the new rules' adjudication
logic executed token-free against the PINNED real hunt record
(`fixtures/hunt-record/`, sha256s frozen at gate 4), with five pre-registered expected
outcomes, scored only after its own record survived independent cold review (round 1 =
MAJOR → revised; round 2 = MINOR, PASS survives — `8-retrodiction-litepass*.md`). C8
proves the sampled rules are **computable and non-vacuous on real data**; it narrows the
no-battery residual but does not close it. What C8 cannot observe = the three
**owner-accepted risk classes** (recorded at gate 4, accepted by you):

- **(a) Dilution of pre-existing duties** by the added text (these files are prompts;
  position-sensitive) — bounded by inspection only: the C6 pure-additive walk, C2
  neighbor-text checks, and the plan's insertion-order spec (terminal text per section
  chosen deliberately). Not behaviorally measured.
- **(b) Live, unprompted firing of the new rules** by an Opus executing the amended
  prompt — C8 is the author applying the rules' logic deliberately, not prompt-compliance.
  The first real hunts under the hardened skill are the actual test; watch the early ones.
- **(c) Vacuousness of the rules C8 does not sample** — D-1, D-4, D-5, D-6, D-7, D-9,
  D-10, D-11, D-13 (e.g. D-5's ledger-frequency window meeting a ledger with no frequency
  data). Their first live invocations are their first executions.

## 3. The D-10 relabel — the flagship test is now honestly labeled

The SKILL self-check's flagship test (seeded fixture bug with a non-representative obvious
test; a Dragonfly-following agent must refuse to trust it, proven against a no-Dragonfly
baseline) is now labeled "**aspirational — not yet run** — an unrun check may not be
described as an existing safeguard; a standing replayable probe once run" (SKILL:146-147).
**This run did not run it** — the relabel is the fix (the old text presented it as an
existing safeguard). Running it once, ever, converts it to a standing probe; that is a
cheap future run if you want it.

## 4. The C4 cap raise (recorded, not silent)

The criteria froze with caps **525/152/670** — raised once, pre-freeze, from the round-1
515/148/655 after the round-2 re-estimate showed mapped substance (~60-80 METHODOLOGY
lines, 13-21 SKILL lines) would foreseeably bounce the build (R2-U-3). The raise covers
the estimate's upper range while bounding growth ≤ +18%. Built result: 521/149/**670 —
combined exactly at cap, zero headroom**. Operational consequence, recorded at the
stage-7 gate: **any future fix to these two files must be net-zero lines** or it breaches
the gating cap; the stage-7 fix-in-place round was executed net-zero to hold it. (The
cap-vs-substance rule held: no mapped substance was traded — the stage-6 reviewer
adjudicated every compression, and the 3 that crossed the line were fixed.)

## 5. A rule-design residual the retrodiction exposed (new information, not from the audit)

Re-adjudicating sub-check (i) on the full pinned record surfaced a real edge in D-3 as
built: **token-burning, gate-rejected qualification runs do not enter the cycle count**
(a cycle = a completed stage-4→5 lap; a run that fails its representativeness anchor
completes no lap). The pinned record contains exactly this class: two SPENT-TOKENS smoke
runs (S1-O18, S1-O21) that eliminated no hypothesis. The burn IS visible to the built
rules — the per-area **re-examination prong** of the stage-6 cap and the harness's own
full guarded-change triage cover it — but **the cycle counter alone would not fire on
this thrash class**. Not a defect in what was built (nothing was loosened); a named gap
in what the counter alone measures. If it bites in practice, the candidate fix is a
one-line widening of the stage-6 tally (count gate-rejected token-spending runs in the
re-examination tally explicitly) — a future, separately-gated change.

Related, smaller: the round-2 lite pass found C8's own frozen wording for sub-check (v)
mislabeled the derived assumption ("the live set's" vs the refuted pair's — the
pre-registration's own precedent citation points at the refuted pair). Flagged in
`8-retrodiction.md` rather than silently relabeled; lesson for future pre-registrations —
guard-rail wording gets the same care as the outcomes.

## 6. Attention-budget spend (D-S1 ledger)

| File | Baseline (`9cec23d`) | Built | Cap | Spend |
|---|---|---|---|---|
| METHODOLOGY.md | 441 | 521 | 525 | +80 (+18.1%) |
| SKILL.md | 129 | 149 | 152 | +20 (+15.5%) |
| **Combined** | **570** | **670** | **670** | **+100 (+17.5%), at cap** |

Spend by shape: ~14 line-budget-heavy blocks (stage-7 cluster D-5/D-13/D-14 + the D-2
block + the stage-6 cluster D-3/D-7/D-12 + the charter D-1/D-11 block are the big four);
SKILL took pointer-style clauses only. The next hardening pass CANNOT be additive at this
cap — it must be net-zero or preceded by the D-S1 restructure decision.

## 7. Run integrity notes (for the record)

- The loop caught its own author twice this session: the round-2 stage-3 review caught the
  plan's D-11 scoping hole (MAJOR), and the round-1 lite pass caught the C8 record's
  incomplete ledger walk (MAJOR — the founding-failure class, caught by the process
  applied to its own evidence). Both were re-adjudicated and re-reviewed, not patched over.
- A usage pause (2026-07-04, ~96%) split stage 8; the round-1 lite-pass verbatim was
  persisted post-hoc from the session transcript (transport note in
  `8-retrodiction-litepass.md`; gap recorded in `decisions.md`). All hashes were
  re-verified after resume; the pinned fixtures were additionally cross-verified by both
  cold reviewers independently.
- The commit is path-scoped to `Dragonfly/` — the unrelated working-tree modification
  `Guarded_change/guarded-change.companion.md` (a per-project config repoint) is
  deliberately excluded.
