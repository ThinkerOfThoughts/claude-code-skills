# Stage 9 — Fix verification

**What this stage does:** verify the **root cause is resolved**, not merely the symptom suppressed —
because causality runs cause→symptom, and a masked symptom is not a fixed bug.

## Procedure

- **Verify the root cause is resolved, not merely the symptom suppressed** (A-9-1). (For a
  **characterized** handoff there is no stage-7 chain+toggle to use: stage 9 verifies the marked
  mitigations on **symptom evidence only** — no cause-resolution claim is made or verified (A-9-7).)
- **9a — Local** (if locally testable) (A-9-2): using the stage-7 causal chain + toggle, check **both**
  (i) the diagnosed root-cause condition no longer holds, **and** (ii) the symptom is correspondingly
  gone. Route:
  - **Cause gone + symptom gone** → genuinely resolved → proceed to 9b.
  - **Symptom gone but cause still active** → the fix **masked** the symptom → record + back to
    **guarded-change** for a fix that addresses the cause.
  - **Symptom persists** → record `"fix F did not resolve S#"` as new evidence → back to **stage 0**.
    (Dragonfly makes the empirical cause/symptom observations and routes on them; it does not itself
    adjudicate the fix's *code fidelity* — that is guarded-change's domain.)
- **9b — Live** (always when not locally testable, and after a local pass) (A-9-3): the **user** runs
  it live (the user is the final authority). Route: **confirmed resolved → done**; **not resolved →
  record → back to stage 0** with the new information.
- **Rate-based/intermittent symptom → define the observation window up front** from the symptom's
  observed ledger frequency (A-9-4) (e.g. ~1/session over 5 sessions → 9b window ≥ 5 sessions, pass = 0
  occurrences); a single clean run or an unstated window does not satisfy 9a/9b.
- **Re-check the residuals list (A-9-6):** killing the primary does not close an unexplained residual;
  residuals are struck only with a recorded reason.
- **A failed verification is never discarded** (A-9-5): it is recorded as a **new symptom** so the next
  lap starts from fact, not scratch.

## Cross-cutting rules governing this stage

**Causality runs root-cause → symptom, never the reverse (B-CAUS-1).** "Symptom gone" is necessary but
**not sufficient** — a fix can mask a symptom while the cause survives and resurfaces later. "Fixed" is
a claim about the *cause*, which is why 9a checks the cause condition, not just the symptom.

**Stop-for-human at 9b live verification.** The user is the final authority on "resolved"; a
characterized ending's mitigations are verified here on symptom evidence only.

**Evidence over rhetoric (B-EVID-1).** Each resolution/persistence claim cites the run or ledger row
that earned it.
