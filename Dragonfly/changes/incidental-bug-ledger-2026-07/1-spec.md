# 1 — Spec: the incidental-bug ledger (dragonfly Theme 3)

## The problem

Dragonfly hunts keep surfacing **unrelated** potential bugs as a side effect of examining the codebase
(the flagship probe, the gc-battery arms, and both restructure runs each turned up incidental findings).
Today there is nowhere to put them: either the agent **chases** one — breaking the hunt's focus and
burning the convergence budget on a bug that isn't the symptom under investigation — or it **drops** it
and the observation is lost. Neither is good. The append-only ledger structure the skill already uses
(symptom / observation / hypotheses / decisions) has no "parking lot" for out-of-scope findings.

## The goal

Add an **incidental-bug ledger** — a running log where the hunt records any incidental potential bug it
notices **without acting on it** (log-and-move-on, to protect the hunt's focus), surfaced in the final
handoff as a **parking lot for future investigation**. This is **additive**: a new artifact + a concise
cross-cutting discipline, fitting dragonfly's existing ledger structure. It does not change how the hunt
diagnoses its actual symptom.

## The behavior (what "done" looks like)

During any stage, if the agent notices a **potential bug clearly unrelated to the frozen `S#` symptom
set**, it:
1. **Records it** in `incidental-ledger.md` (what / where — file:line or component / why it looks
   suspect) — an append-only parking lot, distinct from the observation ledger (which is for things
   examined *about the current symptom*);
2. **Does NOT investigate or chase it** — log-and-move-on; the hunt's focus and convergence budget stay
   on the `S#` under investigation. **Tie-breaker:** when it's unclear whether a finding bears on the
   `S#` set, treat it as **in-scope** (record it in the observation ledger and let the stage-7 coverage
   sweep adjudicate) — park **only clearly-unrelated** findings, so focus protection never silently
   drops a real contributor;
3. **Surfaces it at stage 8** — on **either** terminal verdict (a "found" `diagnosis.md` **or** a
   "characterized, not found" handoff — the skill's only two legal endings), the handoff lists the
   incidental ledger as a parking lot of out-of-scope findings for future, separately-scoped
   investigation (never mixed into the diagnosed root cause or its residuals, which are `S#`-related by
   definition). (If a hunt instead **halts mid-loop** at the convergence-cap stop-for-human and never
   reaches stage 8, the parked findings are not lost — they are on disk and named in the cold-start
   carry-over brief.)

## Proposed placement (the design decision — red-team + owner steer)

The discipline is "notice anywhere → don't chase → park it," so it must be *in view at every stage* but
must not bloat the per-stage load the restructure just optimized (≤227 lines/stage). Proposed:

- **`SKILL.md`** — add `incidental-ledger.md` to the Loop's ledger list + a **concise always-loaded
  discipline line** ("notice an unrelated bug → park it in the incidental ledger, don't chase it").
  SKILL is loaded at *every* stage, so the always-applies discipline is always in view with **zero
  per-stage repetition** — the cheapest reliable placement.
- **`stages/stage-2.md`** (observation ledger — the natural recording home) — the full recording
  mechanics: what to record, and that the incidental ledger is **separate from** the observation ledger
  (an unrelated-bug observation goes to the parking lot, not the S#-observation record).
- **`stages/stage-8.md`** (handoff) — surface the incidental ledger as a parking lot in the report.
- **`METHODOLOGY.md`** — add `incidental-ledger.md` to the "what a run produces" artifacts list + the
  config `ledgers.dir` note.

**Alternatives (for the red-team to weigh):** (a) repeat the full rule into every examination stage (1,
2, 4, 5, 7) — most literal "any stage," but heavier and pressures the load budget; (b) single home at
stage-2 only — lightest, but not in view when a bug is noticed at stage 7. The proposal (SKILL
always-loaded discipline + stage-2 mechanics + stage-8 surfacing) is the middle path.

## Constraints

1. **Additive, not behavior-changing to the hunt.** No existing rule's wording, meaning, placement, or
   triggering condition changes. The diff to the touched files is purely additive (this is verifiable
   mechanically at stage 6).
2. **Position-sensitivity still applies** (these are prompts): the added text must not *dilute* or
   reorder existing rules — even additive text can shift an existing rule's effect. Stage-6 checks the
   neighbours of each insertion.
3. **Per-stage load budget preserved.** Every stage's load stays ≤ ~270 lines (the restructure's C3a
   cap). Mechanical check.
4. **Live == source** after build (`diff` clean).
5. **The incidental ledger is a parking lot, NOT a to-do the hunt must clear.** Logging an incidental
   bug never blocks the hunt, never triggers convergence-cap accounting, and is never chased — that is
   the whole point (focus protection). It is explicitly *out of scope* of the `S#` set.

## Scope

- **This run:** the incidental-bug ledger only. Dragonfly only; no guarded-change change.
- **Not in scope:** any change to how the hunt diagnoses its symptom; auto-triaging or ranking the
  incidental findings (they are a raw parking lot); a guarded-change handoff of incidental bugs (they
  are for *future* separately-scoped hunts, surfaced not routed).

## Owner decisions (RESOLVED at the spec gate, 2026-07-06)
- **(A) Placement → SKILL-discipline + stage-2-mechanics + stage-8-surfacing.** The always-loaded
  SKILL discipline line puts "notice → park → don't chase" in view at every stage with zero per-stage
  repetition; stage-2 holds the recording mechanics; stage-8 surfaces the parking lot.
- **(B) Process weight → LEAN loop.** One stage-3 cold red-team → build → one stage-6 code review →
  stage-8 conformance. No battery, no multi-round. Scaled to a small additive change.
