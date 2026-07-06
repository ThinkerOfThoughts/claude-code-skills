# Stage 6 — Convergence gate

**What this stage does:** check that the hunt is narrowing, and stop it if it isn't. The iteration cap
is the defense against token-burning thrash.

## Procedure

- **Are we eliminating hypotheses?** (A-6-1)
- **Iteration cap: after `N` cycles with no hypothesis eliminated (or `N` re-examinations of one area),
  stop and escalate to a human** (A-6-2).
- **`N` comes from the config (Layer-1 default 3); if no `N` is resolvable, Dragonfly refuses to start**
  rather than run without a convergence stop (A-6-3).
- **A cycle = one discriminating test run AND recorded** (a completed stage-4→5 lap) (A-6-4).
- **Each pass appends to `decisions.md`** (A-6-5): the per-`S#`-thread cycle counts + which mechanism
  **classes** the live hypotheses cover / are ruled out + **what assumption the live set shares**
  (explicit "none identified" counts). A pass missing this record is a **gate violation**, like an
  uncounted cycle — the cap must be countable from the log, and cold passes aim at the shared
  assumption too (one found false ranks by impact).
- **Multiple `S#` threads count convergence per-thread** (A-6-6): a test discriminating across threads
  increments each thread whose hypotheses it splits; a thread hitting the cap **escalates alone**;
  threads may split into separate hunts at any gate with a recorded reason — global counting may not
  mask per-thread thrash.

## Cross-cutting rules governing this stage

**Stop-for-human when the convergence gate fires.** Reaching the iteration cap is a stop-for-human: the
hunt halts and a person decides (accept, change the goal, split the thread, or kill it).

**Severity model / iteration cap (from `stages/charter.md`).** The same anti-livelock rule binds any
review gate: after **2 bounces at the same gate on the same finding class**, a human breaks the tie —
distinct from this stage's `N`-cycle convergence cap.

**Trust-before-gate ordering (B-TBG-1).** A test result consumed here to count a cycle or eliminate a
hypothesis may only be used once the producing artifact's **triage is recorded passed** in
`decisions.md` (see stage 5 for the full rule); a reading is never consumed ahead of its cold review.
