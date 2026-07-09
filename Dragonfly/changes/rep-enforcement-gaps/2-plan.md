# 2 — Plan (verbatim proposed text)

## E0 — `stages/stage-4.md` (NEW, per red-team MAJOR — create the referent B-REG-1 checks)

### E0a — registration obligation, append to stage-4 "Procedure" (after A-4-1)
> - **Register the design as a checkable object (A-4-2).** When the test/instrument is designed,
>   record its **parameters** — sample size / number of runs, the **stop rule** (e.g. "100 turns, or
>   +20 on first trigger"), scale, and the conditions each arm holds — in **`decisions.md`** (the
>   design-time record, alongside the triage result per B-TRI-3 — the observation ledger is for things
>   *examined*, not forward-looking design) as the **pre-registered design**. This is the object
>   stage-5's B-REG-1 checks the executed run against; a design with no registered parameters cannot
>   later be shown to have been run faithfully.

### E0b — result-time-gate pointer, append to stage-4's representativeness-gate block
> - **The gate binds again at result-recording (B-REP-4, stage 5):** passing the design-time gate
>   here does not discharge it — a "clean" result is re-checked at stage 5 against whether this arm
>   could exhibit the symptom at the parameters it actually ran.

## E1 — `stages/stage-5.md`, append two rules to "Cross-cutting rules governing this stage"

### E1a — B-REP-4 (result-time representativeness gate)
> **A negative result is untrusted until its arm is shown able to exhibit the symptom at these
> parameters (B-REP-4).** A "clean / no-symptom" result may **not eliminate a hypothesis** unless the
> producing arm was shown to **exhibit the symptom under the same-or-weaker parameters** (length,
> scale, load, conditions) than the run that came back clean — "clean at 7 turns" is trusted only if
> that arm exhibited the symptom at ≤7 turns, **evidenced by an observation-ledger row** (a control
> run, per B-REP-3), not by a design assertion. **Parameters are not a single axis:** every axis the
> arm varies (length AND volatility AND state) must be same-or-weaker; if the arm is weaker on one
> axis but stronger on another it does **not** qualify — record it as untrusted-negative. Otherwise
> record it as an **untrusted-negative**: it neither eliminates a hypothesis nor counts toward
> convergence. This is the representativeness gate (B-REP-1) applied at result-recording, not only at
> design — a control that could not have produced the symptom proves nothing by its absence.

### E1b — B-REG-1 (as-run vs as-designed conformance)
> **As-run must match as-designed, or the deviation is recorded and the result re-scoped (B-REG-1).**
> Before a result is trusted, check that the test's **executed parameters** (sample size, stop rule,
> scale, conditions) match the **pre-registered design registered at stage 4 (A-4-2, in
> `decisions.md`)**. If they diverge (the registered design said 100 turns / +20-on-trigger and the
> run used 7–13), record the deviation in the observation ledger (it is a finding about the run) and
> **re-scope what the result can support** before consuming it — a result gathered under different parameters than designed does not answer the question the
> design posed. **A run with no registered design to compare against is itself the defect** (A-4-2
> was skipped) — it is not a pass by default. Silent drift from the registered design is a trust
> defect, not a detail.

## E2 — `stages/stage-2.md`, append to "Cross-cutting rules governing this stage"

### B-TARGET-1 (frozen-target attribution / anti-drift)
> **Every step attributes a share to a named frozen-target node — or it is drift (B-TARGET-1).**
> Before any investigative step, name which frozen-target node it attributes a share to — a specific
> `S#` or a live hypothesis (`hypotheses.md`) — **re-reading the frozen symptom + hypothesis ledgers
> to do it, not reconstructing the target from memory** (reconstruction is where the target gets
> quietly distorted; cf B-VER-1). A step that instead investigates a property of a **symptom** or of
> a **mitigation/bandaid** — real and nearby, and seductive *because* it is — does not attribute a
> share to the root-cause target: it is **drift**. Park it in the incidental-ledger and **do not pull
> it**. Record the attribution as a marker on the step's observation-ledger row (the named target, or
> "parked — no target"); a row that can name no target is the tell. **In doubt whether a step
> attributes a share, take it and mark the row's attribution `uncertain`** — resolve doubt toward
> pulling, never toward parking, so a real cause-tracing step is never lost (the same inclusion
> tie-break the incidental-findings rule uses). This **composes with** the incidental-findings rule
> rather than replacing it: that rule asks "is a *newly-noticed finding* related to the `S#` set?"
> (in doubt → in-scope, never dropped); B-TARGET-1 asks "does the *step I am about to take* advance
> the frozen root-cause target?" — a step can be on-topic yet still be drift onto a symptom/mitigation
> property; both rules resolve doubt toward inclusion.

## E3 — `stages/stage-6.md`, append to "Cross-cutting rules governing this stage"
> **Untrusted results do not count as eliminations (B-REP-4 / B-REG-1).** A cycle that produced an
> **untrusted-negative** (B-REP-4) or a result whose registered-design deviation is unresolved
> (B-REG-1) has **not eliminated a hypothesis** — it still counts as a *cycle* (it ran and was
> recorded, A-6-4), but it may **not be recorded as an elimination or as narrowing** (A-6-1).
> Otherwise a non-representative or off-design run manufactures false convergence.

## E4 — `SKILL.md`
### E4a — rep-gate scope (L53)
- `(governs stages 1 and 4):` → `(governs stages 1, 4, and 5 — the result-time gate B-REP-4):`
### E4b — B-TARGET-1 pointer, appended to the "Incidental findings." paragraph
> **Drift is distinct from an incidental finding:** even an on-topic step is drift if it attributes
> to a property of a *symptom* or a *mitigation* rather than a share of the frozen root-cause target —
> before each step, name the target node it advances (re-reading the frozen ledgers), or park it
> (B-TARGET-1, stage 2).

## E5 — `METHODOLOGY.md`, rep-gate scope (L64)
- `(governs stages 1 and 4) —` → `(governs stages 1, 4, and 5) —`

## E6 — sync source → installed for every edited file (stage-4, stage-5, stage-2, stage-6, SKILL, METHODOLOGY).

## Measurement (stage-8 conformance)
Per C1–C10. Rule presence: grep the 3 new IDs at their homes + the stage-6 tie-in. Scope: positive
grep `governs stages 1, 4, and 5` (1 hit each in SKILL/METHODOLOGY) + negative `grep -rn 'governs
stages 1 and 4'` → 0. Position/behavior: `git diff` shows only additions + the 2 scope-word swaps +
stage-6 cold enumeration (C8). Sync: `diff -r` (C9).

## Instrumentation / thresholds
None to add. Standard severity: blocker → spec; major → plan; minor → fix-and-proceed; clean →
build. Iteration cap 2/gate.

## Risks
- **A1 — B-TARGET-1 contradicting the incidental "in doubt → in-scope" rule.** Mitigated by the
  explicit composition sentence (C4) and by keeping the existing rule's text byte-unchanged (C8).
- **A2 — scope-word surface incompleteness.** Only 2 sites ("governs stages 1 and 4"); C6 uses a
  positive-per-site assert + a negative sweep so a missed site shows.
- **A3 — rule-ID collision.** C7 greps the 3 IDs absent pre-change (already pre-checked: absent).
- **A4 — B-REP-4 "same-or-weaker parameters" ambiguity.** The rule names the concrete test (exhibited
  at ≤ the clean-run's parameters) + the fallback ("design established the symptom is reachable
  there"); the red-team should challenge whether that is operable.
