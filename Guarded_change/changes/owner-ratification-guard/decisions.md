# decisions.md — owner-ratification guard (append-only gate log)

Self-check run: subject = the guarded-change skill itself. Regression N/A (docs) → stage 8 is
conformance-only. Path validation (run start): all 6 skill-source paths + 3 artifact paths + 2
incident-evidence paths exist and are readable (confirmed by the stage-3 reviewer's sha256 read
of all 11). ✓

## Gate 4 — bounce 1 (stage-3 review of the 3-guard plan)
- **Worst finding severity:** Blocker (LA-1/L-1 — C3 precision criterion is self-contradictory
  against RAT1's own bar).
- **Also:** Major LA-2 (causal toggle not a pass-condition), Major E2 (anchor string mismatch),
  Major P-1 (E1 buries the fidelity lens's lead/tail). High-value Minors: MO-1/CG-1 (verbatim
  provenance unanchored), MO-3/L-2 (RAT3 orchestrator-half unenforceable from skill), CG-3 (RAT2
  over-flag precision untested), P-3 (HIL list grammar), L-3 (re-ask+cap doc), MO-2 (multi-turn).
- **Route:** Blocker → **return to stage 1/1.5** (revise spec + criteria + plan), then re-review.
- **Author disposition (no severity contested — all findings accepted as real and incorporated):**
  1. C3 → reframe precision to a **constructed compliant ratification record** (carries the RAT1
     fields) that must NOT be flagged, + a constructed **legitimate elaboration** not flagged
     (covers CG-3). Drop reliance on the voice ruling as the "clean" specimen; note the voice
     ruling is itself an *under-recorded* ruling the new standard would improve (strengthens
     motivation, not a counterexample).
  2. LA-2 → make the **causal toggle a gating pass-condition** in C1/C2/C14 (PASS only if the
     pre-edit charter/text does NOT raise the finding, or raises it materially weaker).
  3. E2 → fix the quoted anchor to the real `**A clean *fidelity* lens…**` italic-in-bold form.
  4. P-1 → **shrink E1/E2** to compact clauses that (a) keep the memory-note sentence as the
     lens tail and (b) point to stage-3 for the full RAT1/RAT2 statement (canonical-home pattern),
     rather than appending a 6-sentence block that steals the recency slot.
  5. MO-1/CG-1 → add a **provenance requirement** to RAT1: the record cites where the owner's
     words are durably recorded (transcript/decisions.md owner entry) so the quote is
     spot-checkable against a source the author didn't author; add a criterion exercising the
     compaction/reconstruction sub-mode. State the honest residual (raises the bar + makes
     fabrication spot-checkable; cannot fully defeat a lying orchestrator).
  6. MO-3/L-2 → reframe RAT3: the **subagent-half (halt-and-relay + emit the marked human-gate
     packet) is skill-enforceable**; the **orchestrator-half ("never answer as owner") is a
     caller-side operating instruction** (CLAUDE.md / the saved memory), reinforced structurally
     by RAT1's verbatim-provenance spot-check. Stop claiming full "structural closure."
  7. P-3 → rework the HIL additions as proper list items, not "and…" grafts onto a closed list.
  8. L-3, MO-2 → one acknowledging sentence each (cap-interaction; multi-turn exchanges).
- **Iteration cap:** bounce 1 of 2 at gate 4. No human tie-break needed (author accepts all).

## Gate 4 — bounce 2 (re-review of the revised plan)
- **Worst finding severity:** Major (L-NEW-1 — plan Design Summary `2-plan.md:22-23` still
  over-claimed RAT3 "structurally enforced by RAT1", contradicting the softened shipped E10/E11 +
  criterion C15). Confined to **plan prose — does NOT ship.** Plus 2 Minors: MO-NEW-1 (live-source
  clarification), LA-NEW-1 (fixture well-formedness at stage 8).
- **All five prior Blocker/Major findings confirmed RESOLVED** by the bounce-1 cold reviewer
  ("Nothing found that would let an invalid ratification ship through the shipped skill text").
- **Route:** Major → return to plan (in-place). Fixes applied, each traceable to a logged finding:
  1. L-NEW-1 → `2-plan.md` design-summary reworded to "Reinforced (not guaranteed) by RAT1…"
     matching E10 / C15. (Same finding class as MO-3/L-2 from bounce 1, in the plan-summary
     section — different section than the bounce-1 Blocker; not an iteration-cap collision.)
  2. MO-NEW-1 → spec provenance paragraph + E6 now state the live chat-transcript line is an
     acceptable durable source; the test is quoted-owner-words-with-a-locus vs author's paraphrase.
  3. LA-NEW-1 → C3 measurement row now requires `8-conformance.md` to enumerate the compliant
     fixture's RAT1 fields so a mis-built fixture can't silently pass.
- **Iteration cap:** gate-4 lap 2; the recurring MO-3/L-2 concern is now closed in ALL sites
  (shipped + summary). No further backward route on this class expected.
- **Author judgment (logged):** the three fixes are a plan-prose wording reconciliation with the
  already-validated shipped edits + two minor clause adds. Per the loop's "minor → fix in place,
  proceed" and because the bounce-1 reviewer explicitly scoped this as "one-line fix, no
  return-to-spec, shipped edits sound," a THIRD full stage-3 review is not warranted. The
  **stage-6 cold review of the actually-built skill text** is the backstop that independently
  validates the shipped result.
- **GATE 4 → PASS → BUILD (stage 5).**

## Criteria freeze (FRZ) at gate-4 pass
- `1.5-criteria.md` frozen at build-entry. sha256 recorded below; stage 8 re-checks it unchanged.
1.5-criteria.md sha256 at freeze:
  0ffa6ad9af5c5e64f4c383abbd939b2c5b49ad8da78754622fc4a29d029bbf9c

## Gate 6/7 — stage-6 cold review of the built skill text
- Reviewer agentId `ad16ee27…`. Worst severity **Minor** (wording drift: built stage-3 CH11 "A
  stage-3 review that carries…" vs plan "…of a plan that carries…"; meaning preserved, reviewer
  judged built form tighter). **Accepted in place.** One nitpick declined. No Blocker/Major.
- All E1–E11 present, position-safe, cross-file consistent; RAT3 orchestrator-half correctly
  scoped caller-side (never "by construction"); no load-bearing lead displaced.
- **GATE 7 → PASS → stage 8.**

## Gate 8 — conformance (self-check → conformance-only)
- Structural criteria C4/C5/C6/C8/C9/C10/C13/C15 PASS (see `8-conformance.md`). C7 oracle-can-fail
  PASS (RAT markers 0 in pre-edit tree, present post-edit). C3 precision PASS (both charters
  accept the compliant fixtures A/B).
- **Behavioral causal-toggle (C1/C2/C3p/C14): NO DETECTION DELTA — recorded honestly, not marked a
  detection PASS.** Two toggle rounds (constructed fixtures + a seam-targeting incident-style plan)
  both show the pre-edit charter's general fidelity lens catches the fabricated/non-disambiguating
  ruling AND the inflation, same as post-edit. Owner chose the rigorous seam test; it confirmed the
  no-delta result and pinned the real mechanism.
- **Finding (load-bearing):** the guards' value is **procedural, not detective** — the incident was
  a *self-certified ratification that no cold review ever audited*, not a detection miss. The patch
  forces the ratification back through a mandatory cold audit (stage-4 gate E7-A can't pass without
  it; CH11 mandatory audit section; E3 required owner-exchange context) + re-ask routing + RAT3.
  Verified by inspection vs the old skill (which had no such gate) and VALIDATED by the seam test
  (once the audit is mandated, either lens reliably catches the fabrication). Reported as such.
- **Owner disposition (asked twice, per RAT3 dogfooding):** (1) close via the rigorous seam toggle
  [done]; (2) **"Sharpen the framing first"** → added explanatory intent to stage-3 RAT1 +
  stage-4 gate + METHODOLOGY ratification-records: *a recorded ratification is a new
  after-the-escalation artifact that self-certifies nothing (CP1); the gate forces a cold audit,
  it does not add detection.* Framing-only, additive; live==source re-confirmed IDENTICAL; markers
  intact; no operative rule changed (verified by inspection). No re-review warranted for
  explanatory prose aligned with the stage-6-validated conclusion.
- **GATE 8 → conformance PASS (done).** Ready to commit.
