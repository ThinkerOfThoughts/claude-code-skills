# Stage 0b — Freeze

**What this stage does:** write the confirmed symptom set into the append-only symptom ledger, so
symptoms can never be silently forgotten mid-hunt.

## Procedure

- **Write both the user's original wording AND the confirmed numbered restatement into
  `symptom-ledger.md`** (A-0b1) — a file, not conversation context.
- **The symptom set is now frozen.** A symptom is **struck only with a recorded reason** (A-0b2); it is
  never silently dropped.

## Cross-cutting rules governing this stage

**The ledgers are files, append-only (B-LED-1).** The symptom ledger is **frozen** (symptoms struck
only with a recorded reason); the observation ledger (stage 2) is **append-only**. Both are written to
files in the hunt folder, **not** held only in conversation context — so amnesia and thrashing are
mechanically prevented, not merely discouraged.
