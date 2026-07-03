# 2 — Plan

Add the gate-before-present rule as a first-class blocking rule (a sibling of the
representativeness gate), plus a per-hypothesis gate marker and a trust-before-gate ordering rule,
in the load-bearing locations so each fires. Exact proposed wording below.

## Edit A — METHODOLOGY.md, Core principles (new bullet, right after "Nothing self-certifies")

> - **A conclusion is gated before it is presented, not after.** "Nothing self-certifies" applies
>   to the *hypothesis you hand the human*, not only to scripts and toggles. A hypothesis is an
>   author-produced artifact; until it has passed its cold red-team it may be **ranked** among
>   candidates but never **presented as the leading / likely / probable cause** — the moment a
>   conclusion is leaned on, the gate must already have fired. Presenting an ungated hypothesis as
>   the answer is the founding failure (a self-certified conclusion acted on) wearing the narrative
>   instead of the code. Symmetrically, an artifact's *reading* is trusted only after its triage has
>   passed — gating precedes trust, it does not audit it retroactively.

## Edit B — METHODOLOGY.md, "## The gate-before-present rule" (NEW dedicated section, placed right after "## The representativeness gate")

> ## The gate-before-present rule (mandatory)
>
> A hypothesis may be **formed and ranked freely** — the agent thinks out loud in its working notes
> and keeps a ranked candidate list. But a hypothesis may **not be presented to the human as the
> "leading / likely / probable / most-likely cause,"** nor as a conclusion to act on, **until it has
> passed its cold red-team** (its stage-4/5 discriminating test run *and* cold-reviewed, and — for a
> declared root cause — the stage-7 causal-chain cold pass). Until then its status to the human is
> explicitly **"candidate, ungated."**
>
> **Rank is not endorsement.** Showing the user the ranked candidate list, and saying which is most
> *plausible so far*, is allowed and expected — that is not the same as calling one the cause. The
> line the rule draws is between *"these are the live candidates, top one still ungated"* (allowed)
> and *"the cause is X"* / *"X is the leading root cause"* (forbidden until X's cold pass is
> recorded). The motivating slip: a hypothesis was presented as the "leading" cause with no cold
> red-team, no repro, no toggle — and the cold pass, when finally run, refuted it as dead code.
>
> **Trust-before-gate ordering.** The same precedence governs artifacts: an artifact's output/reading
> may not be **consumed by a later stage** until that artifact's triage (representativeness gate +
> cold review) is **recorded as passed**. A reading trusted before its gate is a conclusion drawn
> from an uncertified instrument — gate first, then consume.

## Edit C — METHODOLOGY.md, stage 3 detail (extend "**3 — Hypotheses.**")

Append to the stage-3 paragraph:

> Each hypothesis also carries a **gate-coverage marker**, distinct from its confirm/refute status:
> `ungated` → `test-passed` (its stage-4/5 discriminating test has run and been cold-reviewed) →
> `cold-red-teamed` (its stage-7 causal chain has passed a cold pass). The marker records, as a
> fact rather than a memory, whether an independent challenge has actually fired for this
> hypothesis. It gates two things: a hypothesis may not be **presented to the human as a likely
> cause** while `ungated` (see *The gate-before-present rule*), and the stage-7 **"confirmed"** verdict
> requires `cold-red-teamed`.

## Edit D — METHODOLOGY.md, stage 5 detail (extend "**5 — Run & record.**")

Append:

> A result may not be **consumed by a later stage** (to eliminate a hypothesis, advance the gate
> marker, or inform what the human is told) until the producing artifact's triage is **recorded as
> passed** in `decisions.md`. Consuming a reading before its gate is the trust-before-gate slip;
> the triage is a precondition of trust, not a later audit.

## Edit E — METHODOLOGY.md, "What a run produces" (update the `hypotheses.md` line)

> hypotheses.md         ranked falsifiable hypotheses: confirm/refute prediction, status
>                       (open/confirmed/refuted), AND gate marker (ungated/test-passed/cold-red-teamed)

## Edit F — METHODOLOGY.md, Human-in-the-loop (new list item)

> - it **never presents an ungated hypothesis as the likely/leading cause** — a hypothesis is
>   "candidate, ungated" to the human until its cold red-team is recorded (see *The gate-before-present
>   rule*); ranking candidates is fine, endorsing one pre-gate is not.

## Edit G — SKILL.md, stage 3 bullet (operating procedure)

Append to the stage-3 paragraph:

> Each hypothesis carries a **gate marker** (`ungated → test-passed → cold-red-teamed`) alongside
> its status. **Do not present a hypothesis to the user as the leading/likely/probable cause while
> it is `ungated`** — it is "candidate, ungated" until its cold red-team is recorded (ranking the
> candidate list is fine); see METHODOLOGY "The gate-before-present rule".

## Edit H — SKILL.md, stage 5 bullet (operating procedure)

Append:

> A result may not be consumed by a later stage (eliminate a hypothesis, advance the gate marker,
> or inform the user) until the producing artifact's triage is recorded passed — gate before trust.

## Edit I — SKILL.md, Stop-for-human rules (extend the list)

Append to the stop-for-human sentence:

> …; and **before any hypothesis is described to the user as the likely/leading cause** (it must
> have a recorded cold red-team first — until then present it only as an ungated candidate).

## Measurement / instrumentation

- **C1, C2, C3, C4** — inspection of the edited docs (read + grep for each location and the required
  phrases: the label list, "candidate, ungated," the `ungated/test-passed/cold-red-teamed` marker,
  the ordering clause).
- **C7** — `diff` live vs source for each changed file → empty.
- **C5 (load-bearing) — execution replay.** A cold subagent is given *only* the new rule text (Edits
  A + B) plus two neutral scenario descriptions: (violation) "the agent told the user H-X is the
  *leading root cause*; at that point H-X had no cold red-team, no repro, no toggle"; (compliant
  control) "the agent showed the user a ranked candidate list, called the top one the *most
  plausible so far but not yet gated*, and did not call any the cause; it then ran H-top's
  discriminating test and cold review before endorsing it." Pass = judges the first a VIOLATION and
  the second COMPLIANT. Two-sided: a rule that over-fires would wrongly flag the control.

## Severity → routing thresholds

- **Blocker** (→1): the rule as worded would not flag the FILEBLOAT slip (C5 violation-side fails),
  or it changes the loop's stage structure/severity model.
- **Major** (→2): it over-fires — bans legitimate ranked-candidate discussion (C5 control-side
  fails) — or the gate marker contradicts the existing status/"found" bar (C6), or it lands in too
  few locations to fire (C1).
- **Minor** (fix in place): wording ambiguity, a tightenable phrase.
- **Nitpick** (log): style/terminology.

Gating: C1, C2, C3, C4, C5, C7. Advisory: C6.
