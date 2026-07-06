# Stage 8 — Handoff

**What this stage does:** emit the diagnosis artifact and hand the fix to guarded-change. Dragonfly
finds the bug; it does **not** author the fix.

## Procedure

- **Write `diagnosis.md`** (A-8-1): the root cause, the causal chain **with each level's depth-check
  status**, the **named residuals**, the representative repro, and the recommended fix.
- **Hand `diagnosis.md` to guarded-change to make the fix. Dragonfly does NOT author the fix itself**
  (A-8-2). This is the legitimate workflow handoff — a compose relationship, not a rules dependency:
  dragonfly diagnoses, guarded-change makes the fix, and dragonfly then verifies it at stage 9.
- **Surface the incidental-bug ledger as a parking lot — on either terminal verdict** (a "found"
  `diagnosis.md` **or** a "characterized, not found" handoff). If `incidental-ledger.md` is non-empty,
  the handoff lists it as **out-of-scope findings for future, separately-scoped investigation** — kept
  **distinct** from the diagnosed root cause and its named residuals (which are `S#`-related by
  definition). It is surfaced, **not** routed to guarded-change (each incidental bug is a future hunt of
  its own, if pursued). (If a hunt halts mid-loop at the convergence-cap stop-for-human without reaching
  stage 8, the parked findings are on disk + in the cold-start carry-over brief — not lost.)

## "Characterized, not found" — the only other legal terminal verdict (A-8-3)

If the hunt ends short of "found," it may end ONLY as "characterized," requiring ALL of: (a) what IS
established (each claim cited + cold-red-teamed); (b) which hypotheses were refuted, with evidence;
(c) WHY the full bar is unreachable — a named reason; (d) **explicit human sign-off**; (e) presentation
tier stays "characterization," never "the cause." Mitigation directions may ride the handoff **marked
as such** (verified at stage 9 on symptom evidence only — no cause-resolution claim). Missing any of
(a)–(e) → not a legal stop.
