# Stage 2 — Observation ledger

**What this stage does:** record everything examined in an append-only ledger — the anti-thrash spine
that stops the same areas being re-checked and prior findings being forgotten.

## Procedure

- **Record everything examined in `observation-ledger.md` (append-only)** (A-2-1): *what* was checked /
  the *observation* / a *citation* (file:line, log row) / *what it rules in or out*.
- **An area may not be re-examined without first recording why the prior finding is insufficient**
  (A-2-2). This makes re-checking a deliberate, justified act rather than forgetful churn.
- **Incidental findings go to a *separate* ledger.** If while examining you notice a potential bug
  **clearly unrelated to the `S#` set**, record it in `incidental-ledger.md` (append-only: what / where
  file:line-or-component / why suspect) — **not** in the observation ledger (which is for things
  examined *about the current symptom*) — and **do not investigate it** (log-and-move-on; focus
  protection). **When in doubt whether it bears on the `S#` set, treat it as in-scope** — record it in
  the observation ledger and let the stage-7 coverage sweep adjudicate; park only clearly-unrelated
  findings, so a real contributor is never silently lost. It is out of scope of this hunt and carried to
  the stage-8 parking lot.

## Cross-cutting rules governing this stage

**The ledgers are files, append-only (B-LED-1).** The observation ledger is append-only; the symptom
ledger (stage 0b) is frozen. Both live in files in the hunt folder, not conversation context.

**File persistence is load-bearing (B-LED-2).** The cold-start guard *recommends restarting the
session*, which would destroy any in-context ledger — so the ledgers must survive a restart on disk for
the carry-over to be real.

**Evidence over rhetoric (B-EVID-1).** Every conclusion recorded here cites a log row / file:line /
observed result. "Seems like X" is not a finding; "line N logged Y, which only happens when Z" is.

**Verify, don't just cite — especially your own claims and memory (B-VER-1).** Every factual claim
about the code, data, or timeline is **verified against the source** before it enters a ledger or a
conclusion — including (especially) a claim the agent itself just made, and a definition or fact
sitting in a **memory note** that is steering the hunt. Memory is where a convenient-but-wrong
definition ossifies; a memory-encoded claim that drives a decision is re-verified against the source,
not trusted because it is written down. This strengthens B-EVID-1 (cite) to cite-**and-verify**: an
unverified assertion — however confident, however often repeated — is not a finding.
