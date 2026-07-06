# Stage 0a — Translation

**What this stage does:** restate the user's reported symptoms in precise technical terms and confirm
the restatement before anything is frozen. A misunderstanding caught here is free; caught at stage 7 it
is a wasted session.

## Procedure

Take the symptoms **as the user reported them** (their words, however loosely stated) and:
- **Restate them in precise technical terms as discrete numbered items `S1`, `S2`, …** (A-0a1) — so
  every aspect has a stable handle later stages can reference unambiguously.
- **Capture any user-provided reproduction steps as `R1`, `R2`, …** (A-0a1).
- **End at a confirmation checkpoint (stop-for-human):** show the numbered restatement (+ repro steps)
  back to the user; it must be **confirmed or corrected before proceeding** to the freeze (A-0a2).

## Cross-cutting rules governing this stage

**Stop-for-human at the 0a confirmation checkpoint (C-HIL-1).** The symptom restatement must be
confirmed by the user before the ledger is frozen. This is the cheapest correction point in the loop.
