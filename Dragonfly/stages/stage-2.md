# Stage 2 — Observation ledger

**What this stage does:** record everything examined in an append-only ledger — the anti-thrash spine
that stops the same areas being re-checked and prior findings being forgotten.

## Procedure

- **Record everything examined in `observation-ledger.md` (append-only)** (A-2-1): *what* was checked /
  the *observation* / a *citation* (file:line, log row) / *what it rules in or out*.
- **An area may not be re-examined without first recording why the prior finding is insufficient**
  (A-2-2). This makes re-checking a deliberate, justified act rather than forgetful churn.

## Cross-cutting rules governing this stage

**The ledgers are files, append-only (B-LED-1).** The observation ledger is append-only; the symptom
ledger (stage 0b) is frozen. Both live in files in the hunt folder, not conversation context.

**File persistence is load-bearing (B-LED-2).** The cold-start guard *recommends restarting the
session*, which would destroy any in-context ledger — so the ledgers must survive a restart on disk for
the carry-over to be real.

**Evidence over rhetoric (B-EVID-1).** Every conclusion recorded here cites a log row / file:line /
observed result. "Seems like X" is not a finding; "line N logged Y, which only happens when Z" is.
