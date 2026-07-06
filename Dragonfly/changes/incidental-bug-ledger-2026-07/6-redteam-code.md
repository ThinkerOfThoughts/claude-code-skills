# 6 — Red-team the code — verbatim record

Cold code review of the built diff (`6-build.diff`, base `4372f73`) vs the frozen plan + criteria + the
4 built files in context. Reviewer: **general-purpose**, model **claude-opus-4-8[1m]**, read-only +
mechanical. Mechanical diff: `git diff -- Dragonfly/SKILL.md stage-2.md stage-8.md METHODOLOGY.md`.
**Verdict: CLEAN — safe to harness** (worst = a nitpick that *improves* on the frozen plan).

## Provenance (reviewer-reported hashes)
`6-build.diff` `e4b22f3d…`; `2-plan.md` `90ae5a8b…` (frozen); `1.5-criteria.md` `133f9854…` (frozen);
built `SKILL.md` `b98da925…`, `stage-2.md` `1b26e020…`, `stage-8.md` `8fda136e…`, `METHODOLOGY.md`
`fa9c8baf…`.

## Dispositions (all PASS)
- **T3 additive-only — PASS.** All 4 diff "deletions" confirmed **pure re-wraps** (same words re-flowed
  to fit the added content): METHODOLOGY:123 added "+ incidental" only; SKILL cold-start (2 lines)
  inserted "`incidental-ledger.md`," only; SKILL loop-intro inserted the incidental clause only. **No
  existing rule's wording, meaning, placement, or triggering condition changed.**
- **Faithful to frozen plan — PASS.** Each insertion matches `2-plan.md` §A. (Nitpick: the METHODOLOGY
  artifact line adds "separately-scoped," *tightening* T7 phrase-alignment with SKILL/stage-2/stage-8 —
  a consistency improvement over the frozen text, not a defect.)
- **Position / no dilution — PASS.** The flagship "most important gate is the representativeness gate…"
  paragraph (SKILL:53-58) is **intact**, ends "…escalate to a human.", still directly below the loop
  table, with the new discipline note inserted *after* it, before `## Stop-for-human`. Stage-2 A-2-1/
  A-2-2 and stage-8 A-8-2/A-8-3 byte-unchanged; the new stage-2 bullet *reinforces* (not blurs) the
  observation-ledger boundary; the new stage-8 bullet keeps residuals distinct + "not routed to
  guarded-change" (A-8-2 compose relationship undisturbed).
- **Two-verdict fix — PASS.** stage-8 says "either terminal verdict (found / characterized)", no phantom
  third exit; matches A-8-3. The mid-loop convergence-cap fallback correctly points at the cold-start
  carry-over brief, which genuinely lists `incidental-ledger.md` (SKILL:26) — not vacuous.
- **T7 consistency — PASS.** Name + semantics (log-and-move-on / don't chase / parking lot / out-of-scope
  of S# / when-in-doubt-in-scope) agree across all 4 files.
- **T5 note:** SKILL 91 / stage-2 31 / stage-8 28 — far under the ~270 budget (worst load 237).

→ Gate 7: worst = nitpick → log, proceed. → Stage 8 (Tier-2 conformance: 5 arms + mechanical T3/T5/T6/T7).
