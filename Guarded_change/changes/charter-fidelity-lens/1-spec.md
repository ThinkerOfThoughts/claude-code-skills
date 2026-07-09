# 1 — Spec: add a FIDELITY lens to the red-team charter

## Problem

The red-team charter (`stages/charter.md`, shared by stages 3 and 6) attacks an artifact on
four separate lenses — **Factual, Logical, Missed-opportunity, Unstated-assumptions** — plus the
conditional position/concurrency checks. Between them they establish whether an artifact is
*correct / complete / robust / representative*. **None of them asks whether the artifact is the
right KIND of thing** — i.e. whether it implements the **mechanism the owner actually
specified**, or a plausible/convenient **proxy** for it.

An artifact can pass every existing lens and still be the wrong kind of thing.

### The concrete failure that motivates this (owner-reported, 2026-07-08)

The owner mandated: *drive the simulated human ("Bob") via an **AGENT**.* The build implemented
Bob as a headless `claude -p` one-shot and ran a whole build+run cycle that way. That instrument
went through a **full cold red-team** which found and fixed real bugs (2 BLOCKERs among them) —
yet the red-team never questioned whether "Bob via headless `claude -p`" was even the right
*kind* of instrument. `claude -p` is **stateless** (reloads the full system prompt every call →
most of an ~$8/100-turn cost) and **amnesiac** (only a re-sent window; forgets older turns); a
real Agent-tool subagent holds continuous context (cheaper + remembers). **Correctness was
green; fidelity was red, and no lens looked.**

Two aggravating factors the lens must defend against:
- A **prior-session memory note** had encoded the false equivalence "the inline `claude -p` call
  IS a Bob agent," and the build was made *to that convenient, already-existing definition*
  rather than to the owner's actual mechanism. A definition sitting in a memory note or a prior
  artifact is an **unverified claim that silently steers the build**, not a spec.
- The **surprising cost signal** (~$31 for a run) was the thing that finally exposed the
  mismatch — a resource surprise is a *tell* that the implementation may not match the intended
  design, not merely a number to report. (This last point is primarily a triage/dragonfly-side
  concern; captured here for completeness, addressed in dragonfly R-C.)

## Why now / prior art

Queued in memory `guarded-change-next-iter-tweaks.md` as the single item, to be folded in via a
dedicated guarded-change-on-itself session (this run). It is the **guarded-change-side companion
of dragonfly R-C** (the dragonfly next-iter list carries the triage/hunt-side version). The
existing "a clean *factual* lens must be earned with citations" discipline is the structural
template: a lens paired with an earned-clean guard so a reviewer cannot rubber-stamp it.

## Scope / intent

Add a **fifth lens — Fidelity** — to the charter's shared core (so it runs at **both** stage 3,
where it asks "does the *planned* instrument implement the specified mechanism?", and stage 6,
where it asks "does the *built* thing implement it, or a proxy?"). The lens must:

1. **Pin loaded operational terms to their concrete mechanism.** For each loaded term in the
   spec/owner request ("agent", "drive", "human", "reproduce", "replace", etc.), name the
   concrete mechanism the owner meant.
2. **Flag proxy substitution as UNTRUSTED.** An artifact that substitutes a convenient or
   pre-existing implementation for the specified mechanism is untrusted until the owner confirms
   the substitution.
3. **Treat an inherited definition as a claim, not a spec.** A definition encoded in a prior
   artifact or a memory note that drives the build must be re-verified against owner intent.
4. Carry an **earned-clean guard** (mirroring the factual lens): a "no fidelity issue" verdict is
   valid only if the review names the loaded terms and the mechanism each was pinned to.

## Key design decision (for the plan to justify, the red-team to challenge)

**Unconditional 5th lens, not a conditional one.** Position and concurrency are *conditional*
(they fire on a mechanically-detectable structural trigger — "touches a prompt assembly", "adds a
shared-state accessor"). Fidelity's failure mode is **failure to notice that a term is loaded** —
which is not mechanically detectable, and is exactly what failed in the Bob case. A conditional
trigger ("fires when a loaded term is present") would re-introduce the noticing-gap the lens
exists to close. Therefore Fidelity is an **unconditional core lens**, always asked; a change
with no loaded terms earns a cheap clean verdict ("terms map directly to the build") under the
existing "no issue found per lens is allowed and expected" rule.

**Append at position 5** (leave lenses 1–4 and the `(lens 4)` tags on the position/concurrency
discipline bullets untouched) — the lenses are explicitly non-hierarchical ("separate ... so one
doesn't crowd out the others"), so order is not semantic and appending minimises churn/risk.

## Expected touched files

Source tree `~/Desktop/claude-code-skills/Guarded_change/` **and** the installed mirror
`~/.claude/skills/guarded-change/` (kept in sync):

1. `stages/charter.md` — add lens 5 to the numbered list; add the earned-clean fidelity
   discipline bullet; update the two internal count words ("four **separate** lenses" @ ~L16;
   "the four lenses + the unconditional discipline" @ ~L46).
2. `METHODOLOGY.md` — L82 count word ("four lenses + discipline + provenance …").
3. `SKILL.md` — L66 count word ("cold subagent, four lenses, evidence discipline").
4. `stages/stage-3.md` — L6 and L15 count words.
5. `stages/stage-6.md` — L6 count word.

**Not touched:** `README.md` and `guarded-change.companion.md` do **not** enumerate the lenses or
state the count (verified: their only lens reference is the *factual-verdict* discipline), so they
are not consistency surfaces. The `dragonfly` skill has its own separate charter (no shared rules
— Theme-2 decision) and is out of scope for this run (dragonfly R-C is the next, separate change).
