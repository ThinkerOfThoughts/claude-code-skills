# 3 — Red-team of the plan (verbatim record)

## Provenance
- **Reviewer:** cold `general-purpose` subagent, no shared context (agentId a86083c3c1c4daf22),
  Claude Opus 4.8. Charter: four lenses + discipline + mandatory coverage-challenge; the seven
  verification foci in the spawn prompt (archived in the run transcript).
- **Context:** 3 change artifacts + dragonfly source (stage-1/2/3/4/5/6, SKILL, METHODOLOGY) +
  tree-wide grep. Paths validated (decisions.md).

## Verdict: **MAJOR** (route back to spec/plan)

### Factual
- **Rep-gate-scope surface = exactly 2 sites** (SKILL L53, METHODOLOGY L64); related "stages 1/4/7"
  mentions describe the triage/charter set, not the gate's scope → not made stale. CLEAN.
- **Rule IDs collision-free**, scheme-conformant (B-REP-4 continues B-REP-N; B-REG/B-TARGET new
  prefixes like B-COST/B-FID). CLEAN.
- **MAJOR — B-REG-1 references an artifact the skill never produces.** "pre-registered design / stop
  rule / sample size / as-designed" appear NOWHERE in source; stage-4 (A-4-1) is a single
  unparameterized line ("design a test that splits the live hypotheses"). B-REG-1 at stage-5 checks
  "match the pre-registered design from stage 4," but stage-4 never registers one → **vacuously
  satisfiable** ("nothing registered → nothing deviated"). The plan edits stage-5/2/6/SKILL/
  METHODOLOGY but NOT stage-4.
- **MINOR — "named layer/bug" target-node vocabulary not in source.** Only S# and "live hypothesis"
  are defined nodes; "layer" only appears as the Layer-1/2 config architecture. Prefer "a specific
  S# or a live hypothesis."

### Logical
- **B-TARGET-1 vs incidental-findings: no direct contradiction** (different objects — a *finding* vs
  a *step*; the composition sentence + C4 hold). But **MINOR residual: tie-break directions
  disagree** — the incidental rule resolves doubt toward **inclusion** ("in doubt → in-scope, never
  dropped"); B-TARGET-1 resolves toward **exclusion** ("do not pull it"). Side-by-side in stage-2, an
  operator could read "symptom property → park it" as licence to park a step that would trace to the
  cause. Mirror the inclusion tie-break.
- **MINOR — B-REP-4 fallback loophole:** "(or the design established reachability)" re-admits the
  assertion-level trust the gate forbids; bind it to a ledger-evidenced control (B-REP-3 pattern).
- **Stage-6 tie-in: logically correct, coheres** with B-TBG-1. CLEAN.

### Missed-opportunity
- **MAJOR (same root as the factual MAJOR) — B-REG-1 needs a stage-4 home** to *create* the
  registration it checks; the change touches everything but stage-4.
- MINOR — point B-REP-4's fallback at B-REP-3's evidence discipline. MINOR — add a stage-4 pointer
  that the gate also binds at result-time (B-REP-4).

### Unstated-assumptions + COVERAGE-CHALLENGE
- Assumption stage-4 produces a parameterized design — false (the MAJOR).
- **MINOR — "same-or-weaker parameters" assumes a total order;** real arms vary on multiple axes
  (length AND volatility AND compaction-state); "weaker on length, stronger on load" is undefined.
  Add a partial-order clause.
- Coverage gaps (no criterion observes): (1) B-REG-1's referent existence; (2) tie-break-direction
  consistency; (3) B-REP-4 fallback evidence-tier; (4) stage-4 body coherence.

## Resolutions applied (this revision pass — route back to plan)
- **MAJOR:** B-REG-1 restructured to span **stage-4 (register the design's parameters/stop-rule/
  conditions as the pre-registered design) + stage-5 (check as-run matches, else record + re-scope)**.
  New edit **E0** adds the stage-4 registration obligation; stage-4 added to touched files. New
  criterion **C2b** verifies stage-4 produces the referent.
- **MINOR node-vocab:** B-TARGET-1 reworded to "a specific `S#` or a live hypothesis" (dropped
  layer/bug).
- **MINOR tie-break:** B-TARGET-1 gains an in-doubt→**inclusion** clause ("in doubt whether a step
  attributes a share, take it and mark the row uncertain") to match its sibling rule; C4 extended to
  check the tie-break direction agrees.
- **MINOR fallback:** B-REP-4 fallback bound to "a control run **in the ledger**" (B-REP-3 evidence
  tier); C1 extended to check the fallback requires evidence, not assertion.
- **MINOR multi-axis:** B-REP-4 gains a partial-order clause (every varied axis must be same-or-
  weaker; axes that trade off ⇒ does not qualify ⇒ untrusted-negative).
- **MINOR stage-4 pointer:** E0 also adds a one-line "gate binds again at result-time (B-REP-4)".
- Independent re-check: a focused **stage-3 round-2** cold review of the revised B-REG-1
  (stage-4+5) + the refinements (the stage-4 content is genuinely new design → warrants a cold pass,
  not just stage-6).

---

# Round 2 — re-review of revised plan (verbatim record)

## Provenance
Cold `general-purpose` subagent, no shared context (agentId a001519c7fd85ca91), Claude Opus 4.8.
Focused on whether the round-1 fixes hold + anything newly introduced. Context: revised artifacts +
stage-2/4/5/6, SKILL, METHODOLOGY + grep. Paths validated.

## Verdict: **MINOR** (fix-and-proceed — no further bounce)
Round-1 MAJOR (B-REG-1 vacuous referent) **fully closed**: A-4-2 collision-free (sole existing id is
A-4-1), placed after A-4-1 in stage-4 Procedure; E1b references it + "no registered design is itself
the defect"; grep confirms "pre-registered/stop-rule/sample-size" exist only in the new edits with
A-4-2 as sole producer. All 4 round-1 MINORs verified HELD: B-TARGET-1 tie-break now splits two
disjoint antecedents (confirmed-drift ⇒ don't pull; doubt ⇒ pull + mark uncertain) — latching path
closed; B-REP-4 fallback bound to ledger evidence (old "design established reachability" survives
only as plan Risks prose, not rule body); multi-axis clause present; node vocab now "S# or a live
hypothesis" (layer/bug gone).

Two NEW MINORs (both fixed this pass):
- **E3 "decrement the convergence budget"** invents a counter stage-6 lacks (the cap counts cycles UP
  toward N; an untrusted run still IS a cycle per A-6-4, it just isn't an *elimination*). **RESOLVED:**
  E3 reworded — "still counts as a cycle (A-6-4), but may not be recorded as an elimination or as
  narrowing (A-6-1)."
- **A-4-2 wrote the registration to the observation ledger** whose stage-2 contract is "things
  examined," not forward-looking design. **RESOLVED:** A-4-2 now registers to **`decisions.md`**
  (design-time record, alongside the triage per B-TRI-3); only the *deviation* (a finding) stays in
  the observation ledger. Removes the latent C10 ledger-contract divergence.
