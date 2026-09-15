---
name: plan-ledger
description: A recording-and-gating discipline for human-led design conversations — every decision in a spec carries provenance (the owner's own words, or a tagged proposal awaiting confirmation), direction-carrying choices are confirmed as full sentences, mechanism-class forks are always posed, the spec is checked against the project's design invariants, and nothing hands off to a build until a cold contradiction pass and a cold drift check are clean. Use whenever planning or specifying a change with a human owner (before guarded-change builds it). Sibling of guarded-change (build), dragonfly (diagnose), data-distiller (distill).
---

# Plan Ledger

Purpose: **a spec may contain only decisions the owner actually made, in the owner's meaning, checked
against the project's standing design invariants.** The founding failures: an agent recommendation became
the spec default and inverted the owner's design; a sub-decision (a hardcoded constant) slid in as narration
under an approved direction; a pre-existing code shape was inherited as architecture with no ruling at all;
and a transcript-only audit passed all three because the owner's standing principles were never a
checkable input. This file is the **router**; the procedures and prompts live in `stages/`.
`METHODOLOGY.md` is the reference (why, the config contract, what a run produces).

## Inputs

- **The design conversation** with the owner (this skill runs in the session the owner talks to).
- **A project config** (Layer 2): `plan-ledger.*.md` in or near the working dir. It names the
  `invariants_path`, the `ledger_dir`, `inherited_stores`, `adjacent_goals`, and the build hand-off. If
  none exists, help author it against `METHODOLOGY.md`; do not invent project specifics.
- **The invariants doc** at `invariants_path` (template: `stages/invariants-template.md`). If missing,
  seed it from the owner's recorded rulings, mark every line "for owner review", and get it reviewed
  before the exit gate.

## Cold-start / resume

The ledger is the state; the session is not. On invocation, or after any compaction: read the ledger IN
FULL, quote its `## Secret:` token in your first message, and continue from `Open forks`. If the ledger is
stale relative to the conversation, reconcile from the transcript by quotation, never from memory.

## Loop

Create `<ledger_dir>/<slug>-LEDGER.md` from `stages/ledger-template.md`. Rotate its Secret token on every
material update. Stage numbers are canonical (ledger, METHODOLOGY, decisions log inside the ledger).

| # | Stage — purpose | Read |
|---|---|---|
| **0** | Setup: config, invariants doc, ledger created, `status: ACTIVE` | `stages/stage-0.md` |
| **1** | Capture: every decision as a full sentence with a provenance tag | `stages/stage-1.md` |
| **2** | Forks: mechanism-class choices are posed, never narrated | `stages/stage-2.md` |
| **3** | Sheet: the decision sheet is pasted in chat verbatim and approved by version | `stages/stage-3.md` |
| **4** | Spec: derived from the approved sheet; current design only; changelog separate | `stages/stage-4.md` |
| **5** | Cold contradiction pass on sheet + spec + invariants | `stages/stage-5.md` (+ `stages/common.md`, `stages/role-contradiction.md`) |
| **6** | Exit gate: cold drift check, then hand-off to the build | `stages/stage-6.md` (+ `stages/common.md`, `stages/role-drift.md`) |
| **7** | During build: teammate questions route back through the ledger | `stages/stage-7.md` |
| **8** | Close: as-built line, ledger `status: CLOSED` | `stages/stage-8.md` |

## The five rules the router enforces on every turn

1. **Provenance or it is not a decision.** Every ledger line carries one tag: `[OWNER <ts> "quote"]`
   (owner's own words; use the owner's name from config), `[PROPOSED:<who> | CONFIRMED <ts> "quote"]`,
   `[PROPOSED:<who> | UNCONFIRMED]`, `[INHERITED:<where> | UNEXAMINED]`, or `[DERIVED]` (a pure
   mechanical consequence of a confirmed line, named). Nothing hands off while any mechanism-class line
   is UNCONFIRMED or INHERITED. An agent's recommendation, a research report's framing, a teammate's
   self-resolution, and an existing table in the code are all PROPOSED or INHERITED, never OWNER.
2. **Direction-carrying decisions are confirmed as a sentence.** If the decision contains an ordering,
   a default, a fallback, a which-first or a which-wins, read it back on its own line in the form
   "X runs first; Y runs only when <condition>" and record the owner's confirmation of that sentence.
   A label ("fallback", "option 4", "b") never confirms a direction.
3. **Unposed forks are forbidden.** Any mechanism-class choice inside an approved direction is posed
   (stage 2), even when you have a preferred answer, and named plainly by mechanism ("a hardcoded
   constant of -9.25 pinned to this model"), never by virtue ("a trustworthy floor"). The class list is in
   `stages/stage-2.md`. A "good to go" on a proposal confirms only what the proposal stated.
4. **The sheet is what the owner approves; the spec is derived from it.** The sheet is pasted in chat
   verbatim (files are not reliably opened); approval is recorded against a sheet version. Anything in
   the spec that is not on the approved sheet is a fork under rule 3. The spec holds the current design
   only; superseded text moves to the ledger changelog.
5. **Invariants are checked, not remembered.** Every sheet and spec carries an invariants table (one row
   per invariant: holds / violates / n.a., with the line that proves it). Cold passes receive the
   invariants doc and the `adjacent_goals` as inputs and report per invariant.

## Owner-facing output

Owner questions get their own message, answer first, data not summary. Relay and status traffic with
sibling lanes goes in the ledger's Coordination log, never in owner-facing messages. Questions to the
owner go through AskUserQuestion, one question per call, options written as full sentences with the
current default stated and a "none of these" option.

## Stop-for-human

Stop and ask when: a mechanism-class fork is open (stage 2); the sheet needs approval (stage 3); the
contradiction pass or the drift check returns a finding that touches an owner line or an invariant
(stages 5 and 6; a clean pass auto-advances); the invariants doc is missing or unreviewed; config is
missing; or a teammate's build question changes a mechanism class (stage 7). Refuse to resolve any of
these by inference, including "the owner would obviously want X".

## Self-check

The skill's own files are prompts (position-sensitive); non-trivial edits take the guarded-change loop.
Standing criteria: installed copy == repo copy (`diff`); SKILL ↔ METHODOLOGY ↔ stage files consistent
on every shared rule; `stages/common.md` is included verbatim by every dispatched agent and role files
never restate a common rule.
