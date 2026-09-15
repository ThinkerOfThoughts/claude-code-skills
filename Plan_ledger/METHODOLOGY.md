# Plan Ledger — methodology and config contract

## Why it exists

A design conversation between a human owner and an AI planner produces a spec that a build lane treats as
the owner's decisions. Three failures, all observed in one feature's planning, motivate this skill:

1. **A recommendation became a decision.** A research agent framed the feature one way; the planner
   repeated the framing; the owner answered a one-word option to a question whose premise was inverted;
   the spec shipped the inverse of the owner's design and nobody noticed for a day.
2. **A sub-decision slid in as narration.** The owner approved "build it properly, not a threshold" and
   the planner then wrote a hardcoded constant into the spec four times, framed as the virtue of the new
   design, without ever posing fixed-versus-derived as a choice.
3. **An existing code shape became architecture.** A pre-existing side database was inherited as "where
   the data already lives", a sequencing question was answered against the owner's goal ("keep this PR
   disjoint" defeating "one database"), and no ruling was ever made.

A transcript-only drift audit passed all three, because the owner's standing principles were not an
input and because a later "good to go" was read as confirming sub-decisions the proposal never stated.

The discipline therefore has four parts: **provenance** on every decision; **sentence-level confirmation**
of anything with a direction; **forks always posed**; and **invariants as a checkable file** that cold
reviewers receive.

## Where it sits among the siblings

`plan-ledger` (decide, with provenance) → `guarded-change` (build, gated) ; `dragonfly` (diagnose) and
`data-distiller` (distill) feed it. Drift-Detector, when built, is the heavy transcript-based audit; the
stage-6 drift check here is the light one that runs on the ledger's quotes and does not need the
transcript.

## Config contract (Layer 2) — `plan-ledger.<project>.md`

```yaml
project: <name>
owner_tag: <NAME>                 # the word used in [<OWNER> ts "quote"] tags
invariants_path: <path>           # the project's design-invariants doc (template: stages/invariants-template.md)
ledger_dir: <dir>                 # where <slug>-LEDGER.md files live (must survive session restarts)
inherited_stores:                 # existing data stores / tables / caches a spec may be tempted to reuse
  - path_or_name: <…>
    note: <what it is, what keys it>
adjacent_goals:                   # why neighbouring work exists; a spec must not defeat these
  - source: <issue / doc / ruling>
    goal: <one sentence>
redteam_context:                  # read paths for the cold agents (priority order, with notes)
  - path: <…>
    note: <…>
build_handoff:                    # who builds and with what
  lane: <session or person>
  guarded_change_config: <path>
models:
  cold_agents: sonnet             # reason stated per spawn; opus only with a named sonnet shortfall
```

## What a run produces

- `<ledger_dir>/<slug>-LEDGER.md` (the state; template in `stages/ledger-template.md`).
- The builder spec (`*-spec.md` or `*-brief.md`), derived from the approved sheet.
- Cold-pass reports appended to the ledger's Decisions log (or a `reports/` folder next to it).
- Issues for any OPEN fork that shipped as a working assumption (stage 8).

## Conventions the skill relies on

- Skill content is re-attached after a compaction only up to a token budget; the ledger on disk, not the
  session, is the state. A `SessionStart` hook on the `compact` matcher should point the session back at
  any `status: ACTIVE` ledger.
- Spec, brief, ledger and handoff files are covered by a read-before-edit hook so they are never edited
  from memory after a compaction.
- Cold agents run in the foreground of the planner's turn; a delegated runner never backgrounds a gated
  check.
- Model choice for every spawned agent is stated with a reason (default sonnet for document review).
