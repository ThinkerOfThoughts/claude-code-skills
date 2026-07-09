# Stage 7 — Root-cause confirmation

**What this stage does:** declare "found" only against a falsifiable, executed bar — reproduce +
cited chain + toggle — after the causal chain has passed a direct cold red-team.

**Read `stages/charter.md`** for the full red-team charter. Unlike stages 1/4 (where the cold pass
happens via the triage), **at stage 7 you spawn a cold reviewer directly** for the causal chain.

## Procedure

**"Found" requires all three, conjunctively (two-of-three is not "found") (A-7-1):**
1. **Reproduce-on-demand** — the symptom can be produced at will via the stage-1 repro.
2. **A cited causal chain root → symptom** — each link cites evidence (file:line / log row), not
   reasoning alone.
3. **A toggle** — flipping the suspected cause makes the symptom appear/disappear *predictably*; this
   is what proves causality rather than correlation. **For a rate-based/intermittent symptom the toggle
   criterion states the expected rate shift and run count up front** (the rate-based rubric — a single
   flip does not satisfy it).

- **Cold red-team the causal chain directly here** (A-7-2): is it confabulated? does it actually follow
  from the cited evidence? Passing it sets the hypothesis's gate marker to **`cold-red-teamed`** — a
  precondition of the "confirmed" verdict *and* of presenting it as the root cause (B-GBP-3).
- **The toggle is a diagnostic artifact → triage** it (below).

**Depth check — root or relay? (A-7-4).** The root = the **deepest node the project can act on.** For
the claimed root, ask "why does this node produce the next?" ONE level down; "found" requires recording
that this why-down is (a) **answered** with cited evidence, (b) **explicitly out of scope** (model
property / third-party / not actionable — named), or (c) **not load-bearing** for a fix targeting the
cause. The stage-7 cold pass explicitly challenges "**root or relay?**" — "explains the symptom" at a
relay does not satisfy stage 7.

**Timeline sibling — root, or a post-dating amplifier? (A-7-4 / B-TIME-1).** A node cannot be the root
if it was introduced *after* the symptom first appeared; the stage-7 cold pass challenges the claimed
root's introduction point against the symptom's first-appearance point (both cited). A post-dating
node is at most an amplifier — "found" names it as such, never as root.

**Evidence-coverage sweep (A-7-5).** Before "found": every observation-ledger row tied to the `S#` is
either **explained by the confirmed chain** (cite how) or recorded as a **residual** (named secondary
contributor / open sub-hypothesis, ranked), carried in `diagnosis.md` + the stage-8 handoff, struck
only with a recorded reason. "**Found (primary), with named residuals**" is legal; **silent absorption
is not** — an unexplained row without a residual entry blocks "found."

Only with the depth check and coverage sweep recorded is "found" declarable — all three bar items +
both records + the chain's `cold-red-teamed` pass, conjunctively.

## "Characterized, not found" — the only other legal terminal verdict (A-8-3)

A hunt may end short of "found" ONLY as "characterized," requiring ALL of: (a) what IS established, each
claim cited and cold-red-teamed like any conclusion; (b) which hypotheses were refuted, with evidence;
(c) WHY the full bar is unreachable — a named reason (model property / cost bound / needs-live-data);
(d) **explicit human sign-off**; (e) presentation tier stays "characterization" — never "the cause."
Mitigation directions may ride the handoff **marked as such** (stage-9-verified on symptom evidence
only). Missing **any** of (a)–(e) → not a legal stop.

## Diagnostic-artifact triage (the toggle / any detector) — and detector validation

**The toggle runs through the triage before it is trusted** (B-TRI-1), **in priority order** (B-TRI-2):
tokens → full; multi-file/mutates/non-obvious → full; single read-only ≤50 lines → **guarded-change-lite**;
in doubt → full. **Recorded in `decisions.md`** (B-TRI-3). **guarded-change-lite** is a single cold pass
using dragonfly's own charter against a one-line intent + "does X, exercises path P" criterion → fix →
run, keeping charter + provenance (C-LITE-1, C-LITE-2). **A detector/readout** deciding "the symptom
occurred" must **fire on a known-true instance AND stay silent on a known-clean one** before its
readings are consumed (B-REP-3). The instrument/toggle also passes the **fidelity check (B-FID-1)** —
the mechanism the owner specified, not a convenient proxy (full rule at stage 1).

## Cross-cutting rules governing this stage

**Causality runs root-cause → symptom, never the reverse (B-CAUS-1).** A symptom is an *effect*;
symptom-gone is necessary but **not sufficient**. "Found" is a claim about the *cause* — which is why
the toggle (not mere symptom-disappearance) is required.

**Evidence over rhetoric (B-EVID-1).** Every link of the chain cites a file:line / log row, not
reasoning alone; an asserted link is not a link.

**Trust-before-gate ordering (B-TBG-1).** A reading consumed here — to advance a hypothesis's gate
marker to `cold-red-teamed` or to confirm a chain link — may only be used once the producing artifact's
**triage is recorded passed** in `decisions.md` (see stage 5 for the full rule).
