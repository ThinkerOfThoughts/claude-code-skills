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

**Every step attributes a share to a named frozen-target node — or it is drift (B-TARGET-1).** Before
any investigative step, name which frozen-target node it attributes a share to — a specific `S#` or a
live hypothesis (`hypotheses.md`) — **re-reading the frozen symptom + hypothesis ledgers to do it, not
reconstructing the target from memory** (reconstruction is where the target gets quietly distorted; cf
B-VER-1). A step that instead investigates a property of a **symptom** or of a **mitigation/bandaid** —
real and nearby, and seductive *because* it is — does not attribute a share to the root-cause target:
it is **drift**. Park it in the incidental-ledger and **do not pull it**. Record the attribution as a
marker on the step's observation-ledger row (the named target, or "parked — no target"); a row that can
name no target is the tell. **In doubt whether a step attributes a share, take it and mark the row's
attribution `uncertain`** — resolve doubt toward pulling, never toward parking, so a real cause-tracing
step is never lost (the same inclusion tie-break the incidental-findings rule uses). This **composes
with** the incidental-findings rule rather than replacing it: that rule asks "is a *newly-noticed
finding* related to the `S#` set?" (in doubt → in-scope, never dropped); B-TARGET-1 asks "does the
*step I am about to take* advance the frozen root-cause target?" — a step can be on-topic yet still be
drift onto a symptom/mitigation property; both rules resolve doubt toward inclusion.
