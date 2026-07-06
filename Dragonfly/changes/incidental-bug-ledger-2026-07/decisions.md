# decisions.md — the incidental-bug ledger (dragonfly Theme 3)

Append-only gate log. Gate (by stage number) · worst severity · route · rationale+name for any override.

---

**Run start (2026-07-06).** Slug `incidental-bug-ledger-2026-07`. Additive feature on the restructured
dragonfly (`4372f73`, file-per-stage). Dogfooded guarded-change loop, scaled lean (small additive
change). Base rev of `Dragonfly/`: skills repo `main` at `4372f73`.

**Stage 1 (spec) + 1.5 (criteria) + 2 (plan) drafted** — `1-spec.md`, `1.5-criteria.md`, `2-plan.md`.
Two decisions OPEN for the owner at the spec gate:
- **(A) Placement** — proposed SKILL always-loaded discipline + stage-2 mechanics + stage-8 surfacing
  (recommended) vs. repeat-into-every-examination-stage vs. stage-2-only.
- **(B) Process weight** — proposed lean loop (one stage-3 red-team → build → one stage-6 → stage-8
  conformance; no battery, no multi-round). Confirm.

**Spec gate — owner decisions RESOLVED (2026-07-06, ThinkerOfThoughts):**
- **(A) Placement → SKILL + stage-2 + stage-8** (the recommended hybrid; keeps the per-stage load budget).
- **(B) Process → LEAN loop** (one stage-3 red-team → build → one stage-6 → stage-8 conformance).
Plan already matches both. → Stage 3 cold red-team of {spec, criteria, plan} + the current dragonfly files.

Path validation (gate-4 precondition): all 7 stage-3 context paths readable; base rev `4372f73`; hashes captured.

**GATE 4 — ROUND 1 · worst severity = MAJOR · route = back to stage 2 (fix plan in place), then re-review.**
Cold reviewer general-purpose `claude-opus-4-8[1m]`; verbatim `3-redteam-plan.md`. All findings accepted:
- [MAJOR] SKILL insertion anchor → re-anchored after SKILL:57 (keeps the flagship gate paragraph adjacent).
- [MINOR] T4 one-directional → T1 now tests BOTH routing directions (in-scope obs → observation ledger).
- [MINOR] characterized-exit drop → stage-8 surfacing fires on ANY exit; T2 = found + characterized arms.
- [MINOR] no tie-breaker → added "when in doubt → in-scope" to SKILL/stage-2/spec.
- [NITPICK] carry-over brief + arm-model → both added.
Gate-4 same-class bounce tally: 1. → Round-2 re-review (lean; the tie-breaker + characterized-exit add
new text). New pre-freeze hashes computed at round-2 spawn.

**GATE 4 — ROUND 2 · worst severity = MINOR → fix-in-place → CLEAN → FROZEN.** Cold reviewer
general-purpose `claude-opus-4-8[1m]`; verbatim `3-redteam-plan-round2.md`. All five round-1 findings
confirmed genuinely addressed; the two new additions (tie-breaker, any-exit) confirmed sound
(tie-breaker not vacuous + no collision with the triage "in doubt → full" rules; additive-only re-
confirmed; budget ~237 ≤ 270). One new MINOR: the "any exit" rewording invented a third terminal exit —
the skill has exactly two verdicts (found / characterized); a cap hit is a stop-for-human, not a
handoff verdict. **Fixed in place** (spec + plan → "either terminal verdict"; mid-loop-halt covered by
the carry-over brief). Minor → no re-review needed.
**FROZEN sha256:** `1-spec.md` = `86971cb94948319d050df0b5bbe4be5c113cc17dd5404c8a20027fb0f7d108b0`;
`1.5-criteria.md` = `133f98543ffe9956f495821bf78a6a45d2461306b3b69d8166cd183a33c4d036`;
`2-plan.md` = `90ae5a8b583b980137731173a1d888f6fa1cd3e6cc4954d68371648760b46417`. Touched-file set frozen
(SKILL, stage-2, stage-8, METHODOLOGY). → **Stage 5 (build): the 4 insertions.**

**Stage 5 (build) DONE** — 4 insertions applied (31 additive lines; 4 "deletions" = re-wraps).
Mechanical diff `6-build.diff`. Per-stage load: worst 237 ≤ 270.

**Stage 6 (code red-team) — verdict CLEAN** (`6-redteam-code.md`). Cold reviewer general-purpose
`claude-opus-4-8[1m]`. T3 additive-only PASS (4 deletions confirmed re-wraps, no rule reworded);
faithful-to-plan PASS; position/no-dilution PASS (flagship gate paragraph intact + adjacent to loop
table); two-verdict fix PASS; T7 PASS. Worst = nitpick (METHODOLOGY added "separately-scoped" —
improves consistency vs the frozen plan). **GATE 7 — nitpick → log, proceed.**

**Stage 8 (Tier-2 conformance) — 5 arms, model `claude-opus-4-8[1m]`:**
- **T1 (feature fires, BOTH directions): FIRED** — parked the unrelated admin-auth bug to
  `incidental-ledger.md` (not chased); routed the in-scope no-TTL observation to `observation-ledger.md`
  (not the parking lot). ("severity ≠ relevance.")
- **T2-found: FIRED** — surfaced the parking lot distinct from the S#-related residual (residual in
  diagnosis.md; I1/I2 not routed to guarded-change).
- **T2-characterized: FIRED** — surfaced the parking lot on the no-diagnosis.md characterized exit (the
  round-1 gap, closed).
- **SC-1 (rep-gate regression): FIRED**; **SC-2 (gate-before-present regression): FIRED** — no regression.
**C2 = 5/5 FIRED.** Mechanical: **T3** additive-only PASS (stage-6), **T5** load 237≤270 PASS, **T6**
live==source PASS (installed to `~/.claude/skills/dragonfly/`), **T7** consistency PASS (stage-6),
**T8** never-blocks PASS. Per-criterion table: `8-harness.md`.

**GATE 8 — clean → DONE.** All gating criteria T1–T8 PASS. The incidental-bug ledger conforms:
additive, feature-fires (both directions + both exits), no regression, budget preserved, live==source.
→ `9-report.md`, commit, memory.
