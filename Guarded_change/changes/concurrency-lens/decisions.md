# decisions.md — gate log (append-only)

## Stage 4 gate (plan red-team, round 1) — 2026-07-02
- **Worst severity: MAJOR.** Counts: 0 blocker, 2 major, 4 minor, 0 nitpick. Cold reviewer
  (general-purpose, no shared context) consulted METHODOLOGY/SKILL + the full
  timed-conversation-compaction run.
- **Major M-1 (Logical):** C3's replay withholds the `redteam_context` source the real gates
  had — so it tests a harder/different scenario than where the guard fires, risking both a
  false FAIL of a sound guard and a pass that doesn't prove representativeness. → Redesign C3 as
  a true guarded-vs-unguarded A/B on the *same* source the real stage-3 had.
- **Major M-2 (Unstated assumptions):** OVER-FIRE. "Shared mutable state with >1 accessor" is
  the *common* case in any server/DB app, unlike the *rare* position-sensitive assembly the
  guard claims precision-parity with. "Not single-threaded" excludes almost nothing. → Tighten
  the trigger to fire only on a *new* unsynchronized accessor or a *new* read→slow-work→write
  window over state whose atomicity isn't *already* enforced by an existing transaction/lock.
- **Minor m-3 (Factual):** spec L39 ("recorded only in HANDOFF.md, never in a gate") is false —
  the race is written up in the compaction `decisions.md` and became gating criterion C13. Fix
  the sentence to "caught post-hoc by the human and only then gated; no *in-loop* gate surfaced it."
- **Minor m-4 (Logical):** Edit C (the stage-1.5 criterion) doesn't require determinism/pass-rate
  for inherently nondeterministic races — a single lucky green proves nothing. → Pin Edit C to a
  deterministic injected-window harness or a stated pass-rate over N (reuse position lens's
  probabilistic rubric).
- **Minor m-5 (Missed opportunity):** enumeration is first forced at stage 3, but the
  methodology's own "instrument before you build" says the *plan* (stage 2) is the cheapest
  catch. → Add a stage-2 deliverable: enumerate every accessor + state which the guard covers.
- **Minor m-6 (Bloat):** Edit A near-duplicates the position bullet's meta-lesson back-to-back.
  → Compress Edit A, cross-reference the shared meta-lesson.
- **Reviewer bottom line:** the guard would substantively have caught the race (Edit B's
  "enumerate the untouched lock-free appender" ≈ the exact missed actor); structure is right;
  fix the two majors + minors before build.
- **Route:** MAJOR → return to stage 2 (re-plan). First bounce at gate 4. All 6 findings
  addressed in plan v2; spec + criteria amended (m-3, m-1). Then stage-3 round 2.

## Stage 4 gate (plan red-team, round 2) — 2026-07-02
- **Worst severity: MINOR.** Fresh cold reviewer verified all round-1 findings against the
  compaction gate docs. **M-1 RESOLVED** (C3 now a real same-source A/B). **M-2 RESOLVED** —
  reviewer confirmed the tightened trigger *still fires* on the compaction race (its lock is
  new; the change breaks a pre-existing single-writer append discipline) while *not* firing on
  ordinary already-serialized DB/cache writes. m-3/m-4/m-5/m-6 all RESOLVED. Factual lens clean
  (earned — cited `6-redteam-code.md:93-97` "lock race is sound … Clean", the exact documented
  blind spot).
- **Residual minors to fold in at build (fix-in-place):**
  - **b-1 (sharpest):** the trigger's "not already enforced by an existing lock" can be
    short-circuited by a *pre-existing wrong-scoped* lock wrongly believed total → add: a lock's
    mere existence does not satisfy "already enforced"; scope must be enumerated, and when unsure
    whether a guard covers *every* accessor, the trigger fires.
  - **b-2:** make C3's fresh stock-charter control **mandatory** (not "optional") and run a few
    treatment/control passes for a rate, not n=1 (LLM reviewers are stochastic — same rigor Edit
    C demands of concurrency criteria).
  - **b-3:** Edit B's "pre-existing lock-free appender" example matches the compaction bug's
    shape, so C3 partly leads the witness → document that C3 validates the guard on an
    appender-shaped race; generalization to other shapes (widened critical section) rests on the
    wording, not an independent test. (Known-limitation note, not a blocker.)
  - **b-4 (nitpick):** Edit G could ask for a structured accessor table; spec L34 "absent …
    entirely" is loosely worded (ingest_turn appears for provenance, never as the race actor).
- **Route:** MINOR → fix in place, proceed to BUILD (stage 5). No bounce.

## Stage 7 gate (code red-team) — 2026-07-02
- **Worst severity: MINOR.** Fresh cold reviewer verified all 8 edits (A–H) LANDED in the
  correct sections with plan wording; both round-2 minors (b-1 fail-safe, b-4 accessor table)
  present; C1/C2/C4/C6 satisfiable with quoted satisfying text; C5 no coherence regression
  (concurrency lens is a clean structural sibling of the position treatment, cross-linked, no
  duplication/drift). Reviewer independently re-confirmed C6 (live == source).
- **Findings:** (minor) b-1's "when unclear, treat as unguarded" fail-safe slightly reopens
  over-fire surface vs. C4 — but reconcilable and *intended* (clearly-serialized → don't fire;
  ambiguous → fail safe toward review). **Logged, accepted** — a fail-safe-toward-review posture
  is the correct bias for this guard. (nitpick) SKILL Edit H used undefined term "per the
  trigger" → **fixed in place** (reworded to "introduces a new accessor or read-modify-write
  window"; re-synced to source).
- **Route:** MINOR → fix in place, proceed to HARNESS (stage 8).

## Stage 8 harness — C3 replay, ATTEMPT 1 (CONFOUNDED, discarded) — 2026-07-02
- Ran 2 control (stock four-lens charter) + 2 treatment (+ concurrency guard), all four given the
  compaction `2-plan.md` **plus a shared system-context note** that spelled out the two writers +
  "the lock is checked only by the compaction path."
- **Result: all 4 (control AND treatment) flagged the lost-update race as BLOCKER.** The fresh
  control caught it → strict C3 pass condition (treatment catch AND control miss) NOT met.
- **Root cause = my harness, not the guard:** the shared context note pre-enumerated the
  accessors and the lock's scope — the exact work the guard forces — handing the answer to both
  arms (the b-3 "leading the witness" risk, leaked to control too). Confounded → **uninformative
  about the guard's marginal value; discarded.** Re-running plan-only (attempt 2).

## Stage 8 harness — C3 replay ATTEMPT 2 (plan-only, clean) + verdict — 2026-07-02
- 2 control (stock charter) + 2 treatment (+guard), each red-teaming the compaction `2-plan.md`,
  scope-restricted to that file only (no leaked digest).
- **Result: treatment 2/2 flagged the ingest lock-free lost-update as BLOCKER; control 1/2
  (control#2 MISSED it, rating the whole plan MAJOR — a would-have-shipped outcome).** Historical
  control (real stage-3, full source, stock charter) also missed. → The guard moved the missing
  reviewer's outcome and never hurt.
- **C3 verdict: PASS (qualified).** Honest limitation (per b-3): n=2/arm; one fresh control caught
  it unaided because the plan is content-rich. Effect = "reliably helps, never hurts," not a
  slam-dunk. Recorded, not overclaimed.
- **Conformance table (`8-harness.md`):** gating C1,C2,C3,C4,C6 all PASS; advisory C5 PASS. No
  baseline → conformance-only.
- **Stage 8 gate: CLEAN → DONE.** Both copies (live + source) carry the guard identically. Change
  accepted.
