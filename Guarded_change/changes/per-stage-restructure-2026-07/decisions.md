# decisions.md — per-stage-restructure-2026-07 (guarded-change) gate log

## Run start (2026-07-06)
- **Owner:** ThinkerOfThoughts. Directed: restructure both skills per the three
  structural decisions (memory `skills-structural-decisions-2026-07`); this run = the
  guarded-change slice (Theme 1). "Yes, lets start."
- **Loop:** full guarded-change, **dogfooding** — the artifact under review IS the skill's
  own source. Per the self-check section, `METHODOLOGY.md` + `SKILL.md` are the thing under
  review; non-trivial skill edits take the full loop (this is one).
- **Change class:** position-sensitive assembly (prompt files) → the position lens fires at
  stages 1.5 / 3 / 6 / 8; behavior-preservation criterion is mandatory and must be verified
  by execution.
- **redteam_context (dogfooding):** the current pre-restructure skill files
  (`Guarded_change/METHODOLOGY.md`, `Guarded_change/SKILL.md`) + this run's stage docs.
  (The project config `guarded-change.companion.md` points at the companion-emergence brain
  and is NOT the relevant context here — the source under review is the skill itself.)
- **Path validation (run start):** all reviewer-context paths exist and are readable —
  `Guarded_change/METHODOLOGY.md` (534 lines), `Guarded_change/SKILL.md` (124), this change
  folder. ✓ (re-checked at each reviewer spawn for any new path.)
- **Base state:** skills repo `main` = `8b4391b`; live == source for guarded-change
  (standing self-check). Caps: gc 534+124 = 658 (this run relaxes them by design).

## Coupling evidence (for the follow-on dragonfly run; recorded now while surveyed)
Two kinds of dragonfly→guarded-change reference exist (grep of `Dragonfly/{SKILL,METHODOLOGY}.md`):
- **Workflow handoff (legitimate — KEEP):** "sibling of guarded-change", "hand the fix to
  guarded-change", "back to guarded-change" — SKILL:3,11,77,84; METHODOLOGY:7,9,109,111,231,242,246.
- **Rules dependency (the bug — UNTANGLE in the follow-on run):** lite "defined **by
  reference**, not paraphrase, so it inherits guarded-change's charter as that hardens"
  (METHODOLOGY:338-344); "Reuse guarded-change's four-lens charter … see
  `guarded-change/METHODOLOGY.md`" (SKILL:117-118, METHODOLOGY:377-378); "guarded-change's
  probabilistic rubric, by reference" (METHODOLOGY:202); "Provenance (inherited,
  unconditional) … inherit ALL of guarded-change's …" (METHODOLOGY:388-398); "the red-team
  charter (referenced from guarded-change)" (METHODOLOGY:420); self-check "every named
  guarded-change cross-reference [must resolve]" (SKILL:142-144).

## Stage-3 gate round 3 (full re-review) — MAJOR → F2+minors fixed; F3 held for owner design call (2026-07-06)
- Cold reviewer `general-purpose`/`claude-opus-4-8`; verbatim record `3-redteam-plan-round3.md`
  (task `ae1da4c6d3f15db37`). **13/14 round-2 fixes genuinely resolved**; reviewer's own
  same-class read: **NOT a third bounce of the same objection — two NEW majors the deeper
  pass exposed**; core architecture sound; no blocker. (So the iteration cap does not fire a
  3rd time on independent judgment.)
- **F2-NEW [MAJOR] — FIX-INTRODUCED: my round-2 O-6 fix (HIL→gate 7) was wrong** (source:
  stages 1–7 autonomous; no HIL trigger at 7). **FIXED:** oracle HIL reverted to {4,8,1.5} +
  build-note. The tie-break-at-7 intuition is covered by SEV4 (a different rule).
- **F3-NEW [MAJOR] — the gating C3(a) attention budget is not shown achievable for the
  charter-heavy stages 3/6.** The reviewer charter alone is 95 lines; repeated in full into
  both stage-3.md and stage-6.md, those two files' load (~290 lines) exceeds the 263-line cap
  → the change could FAIL its own primary criterion at the two red-team stages after the full
  build + 38-arm battery. **HELD for owner** — the fix is a design choice touching the "no
  spine" decision: (A) a shared `charter.md` both stage-3/6 point at [M1-NEW; also removes the
  O-1 drift surface], or (B) keep full repetition + relax C3(a) for 3/6 with a stated reason.
- **Minors FIXED in place:** F1-NEW (oracle note: CH9/CH10 {3}-scoping is inferred);
  F5-NEW (SEV1 *table*, not just targets, co-locates in gate files); D1-NEW (grader count
  unified: 6, one per situation); F4-NEW/CH-A noted (FRZ/SEV3 exercised at one governing
  stage — same text, C1-placement-backed).
- Frozen docs still UNfrozen (gate 4 has not run). Awaiting owner on F3 → then gate 4.

## F3 RESOLVED by owner: shared `charter.md` (Option 1) (2026-07-06)
- **Owner's conditional:** "shared between two stages of a single skill → option 1; shared
  between guarded-change and dragonfly → option 2." The charter is shared between
  guarded-change's OWN stage 3 and stage 6 → **Option 1 (shared file).** Intra-skill sharing
  is fine; the no-spine / no-cross-skill-sharing principle is preserved (this `charter.md` is
  guarded-change-internal; dragonfly gets its own in the Theme-2 run).
- **Applied:** plan §A.1 adds `stages/charter.md` (one copy, referenced by stage-3.md +
  stage-6.md; 3 adds CH8/CH9/CH10, 6 adds ST6d); §A.3 budget shows 3/6 now ~245 lines / ~37%
  (under the 263 cap) vs ~290 / 44% if repeated; oracle O-1 note updated (one copy → drift
  surface gone); C3(b) permits charter.md as the stage-declared reference at 3/6.
- **Next:** a TARGETED fix-verification cold pass (F2 + F3 + the round-3 minors only — not a
  4th full round, per the owner's "quick targeted check" steer) → then gate 4 freeze +
  battery-cost checkpoint.

## Stage-3 gate — CLEARS (targeted fix-verification = MINOR) (2026-07-06)
- Cold reviewer `general-purpose`/`claude-opus-4-8`; verbatim record
  `3-redteam-plan-round3-litepass.md` (task `a58312e0774095a09`). **All 5 round-3 findings
  (F2/F3/F1/F5/D1) verified genuinely resolved, no fix-introduced defect; budget arithmetic
  independently re-confirmed (stages 3/6 = 245 lines / 37% < 263 cap).** 1 MINOR (S-1: a stale
  cross-cutting sentence still said the charter is repeated) → **FIXED in place** (oracle
  cross-cutting statement now carries an explicit charter EXCEPTION).
- **STAGE-3 GATE PASSES** after rounds 1 (BLOCKER) → 2 (MAJOR) → 3 (MAJOR) → targeted pass
  (MINOR). Worst remaining severity: none unfixed. The plan/criteria/oracle are freeze-ready.
- **NEXT = GATE 4 (freeze) — but the expensive stage-8 battery (38 arms + 6 graders) lies
  beyond it; per the owner agreement, the battery COST is checkpointed with the owner before
  freeze+build.** Awaiting that go.

## Stage-3 gate round 2 — MAJOR → ITERATION CAP FIRES → owner tie-break (2026-07-06)
- Cold reviewer `general-purpose`/`claude-opus-4-8`; verbatim record `3-redteam-plan-round2.md`
  (task `a0e6f9aa22c57e3ff`). **Both round-1 blockers (L1, C-2) verified genuinely resolved;
  all round-1 majors/minors resolved; the grep-derived oracle audited "substantially complete
  and correctly scoped."** Core architecture (file-per-stage + oracle + gate-positioned
  battery + behavioral C3) declared sound.
- **5 majors, all fixable at stage 2 (no redesign):** A-1 (gate files need the routing map,
  which sat only in the slim METHODOLOGY); CC-1 (no SIT-6 → stage-6.md self-containment +
  ST6d unobserved); L-1 (OLD n=2 @≥1/2 is a weaker validity bar than the ≥2/3 NEW bar it
  certifies); O-1 (stage-3≠stage-6 charter asymmetry unstated → C5 could mis-flag/mis-fix —
  the round-1 self-reference bug re-emerging inside the fix); P-1 (SEV3 no-silent-demotion
  tested by presence, not a precedence/routing outcome). Plus 8 minors + 1 nitpick.
- **ITERATION CAP (§ severity model) FIRES:** 2nd major bounce at gate 3; several round-2
  majors are round-1 classes resurfacing in new spots (O-1 ← round-1 F2/L4 self-reference;
  CC-1 ← round-1 L1/C-3 battery coverage; L-1 ← round-1 L2 battery power; P-1 ← round-1 P3
  position-guard adequacy) — "same kind of defect in a nearby spot" per the cap definition.
  → the re-verification routing goes to the **OWNER** (fixes applied regardless, as every
  non-abandonment route needs them).
- **All 5 majors + actionable minors APPLIED in place** (frozen docs untouched — gate 4 has
  not run): oracle build-notes for O-1/A-1/O-3/O-2 + HIL→{4,7,8,1.5} (O-6); C2 gains SIT-6
  coverage + the P-1 precedence-grading rule; C3(a) gains a token target (F-1) + C3(b)
  clarifies stage-declared reference files (L-2); C5 scoped to own-set + oracle-driven +
  respects the O-1 asymmetry + covers METHODOLOGY restatements (A-2); C6 notes the CC-3
  behavioral/mechanical split; plan §B gains SIT-6 (38 arms / 6 graders) + OLD unanimous-2/2
  validity bar (L-1).
- **Owner routing RESOLVED: FULL ROUND 3** (chosen over scoped fix-check / proceed) — the
  thorough route, consistent with the standing rigor-over-cost preference. A complete cold
  re-review of the whole revised set + a resolution check of the round-2 fixes + a hunt for
  fix-introduced defects. If round 3 returns MAJOR on the same classes = 3rd same-class
  bounce → back to the owner. Spawned: `general-purpose`/`claude-opus-4-8`, task recorded
  next entry.

## Re-plan + Stage-3 round 2 spawned (2026-07-06)
- **Owner direction:** file-per-stage split adopted (spec decision C). Revised in place:
  1-spec.md (file-per-stage goal + touched files + decisions resolved), 1.5-criteria.md
  (added C3 attention-budget gate [round-1 C-2 fix]; C1 vs grep-derived oracle; C2 battery
  reaches gate-4+ rules + positive control; C6 router correctness), 2-plan.md (§A file set +
  oracle method; §B 5 stage-situations × OLD/NEW/BROKEN-NEW = 31 arms + 5 blind graders),
  and NEW `2-rule-oracle.md` (independent rule→governing-stage map, C1's ground truth; ~45
  rules; F1/F2/F4 corrections made explicit).
- **Stage-3 round 2** spawned: `general-purpose`/`claude-opus-4-8`, task `a0e6f9aa22c57e3ff`
  — resolution check of all round-1 findings + oracle-completeness audit + fresh pass.
  Awaiting verdict.

## Stage-3 gate round 1 — BLOCKER → return to stage 1/2 (2026-07-06); STOP for owner direction
- Cold reviewer `general-purpose`/`claude-opus-4-8`; verbatim record `3-redteam-plan.md`
  (task `a21f65e02f00844d6`). Worst severity **BLOCKER** (2 blockers, ~13 majors).
- **Blocker L1:** C2's arm span (arms stop at stage 3) cannot fire 4 of its 8 registered
  rules — criteria-freeze, severity-routing, iteration-cap, gating-verified-by-execution —
  which only manifest at gate 4+/stage 8; grading collapses to text-presence for them,
  un-running the mandatory behavior-preservation criterion on half its list.
- **Blocker C-2:** the change's PRIMARY MOTIVATION (attention/loaded-token budget) is
  measured by NO criterion; the restructure could *worsen* it (≈780 lines, per-stage
  loading only honor-system) and still pass every gate.
- **Root design flaw the review exposed (A1/L3/M1):** the "thin router + reorganize within
  the same two files" design does NOT actually enforce per-stage loading — a diligent agent
  reads the whole (now longer) METHODOLOGY, so the change may regress the very attention
  budget it targets, and the A/B battery would be null. Reviewer's fix (M1): **split
  METHODOLOGY into per-stage FILES** the router points at, so the filesystem enforces
  loading and it becomes measurable.
- Other majors carried forward: F1 silent narrowing (criteria-freeze 4→also 8); F2/L4/M2
  §A.2 table incomplete + C1's oracle self-referential → grep-derive the ground-truth
  stage-set as a frozen stage-1.5 oracle; F4/P4 gate-blocking reference-section rules stay
  always-on; L2 n=3 underpowered; C-1 no label-audit scenario; P2/P3/P4 adjacency-dependent
  guards unmeasured.
- **Route:** BLOCKER → return to stage 1/2. Blocker-about-to-restart = stop-for-human →
  the file-per-stage redesign is a direction change put to the OWNER before re-planning.
  (Iteration-cap note: this is bounce #1 at gate 3.)

## Stage 1 — spec written; OWNER GATE RESOLVED (2026-07-06)
- `1-spec.md` + `1.5-criteria.md` written. Two decisions put to the owner:
- **(A) Scope/sequencing → GUARDED-CHANGE FIRST, dragonfly after.** This run = guarded-change
  Theme 1 only; dragonfly (Themes 1+2) is a separate sequenced run, copying gc's finalized
  per-stage layout.
- **(B) Verification depth → TIER 3 (full A/B battery).** Owner chose the gold standard over
  the recommended Tier 2 — consistent with the standing rigor-over-cost preference
  (memory `owner-questions-cost-benefit`). C2 updated to Tier 3; the battery (scenarios,
  arm protocol, blind grading) is designed in `2-plan.md` and frozen at gate 4. Big spend
  lands at stage 8 (battery execution), well behind gates 4 and 7.
