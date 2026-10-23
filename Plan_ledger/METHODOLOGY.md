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
cascade:                          # OPTIONAL block; cascade mode needs it
  enabled: true                   # the default mode for a new ledger whose invocation names neither (`/plan-ledger cascade` or `/plan-ledger normal`); false or absent = normal
  principles_path: <path>         # the owner-approved principles sheet (template: stages/principles-sheet-template.md); may be absent on first use
  records_dir: <dir>              # raw outputs of trio judges, citation checks, red-teams, sift agents, facts files; created on first use
  owner_transcripts: <path>       # where the owner's own past messages can be read (sift; quote verification)
  redteam:                        # guarded-change files the level red-team reuses by path
    charter: <path to guarded-change stages/charter.md>
    stage3: <path to guarded-change stages/stage-3.md>
models:
  cold_agents: sonnet             # reason stated per spawn; opus only with a named sonnet shortfall
```

## What a run produces

- `<ledger_dir>/<slug>-LEDGER.md` (the state; template in `stages/ledger-template.md`).
- The builder spec (`*-spec.md` or `*-brief.md`), derived from the approved sheet.
- Cold-pass reports appended to the ledger's Decisions log (or a `reports/` folder next to it).
- Issues for any OPEN fork that shipped as a working assumption (stage 8).

## Cascade mode (optional; `/plan-ledger cascade`)

**Why.** In one project a fix approved as 55 owner decisions grew to 247 during the build. Almost all the additions were derived by the planner while answering the builder's questions; each was locally reasonable, and together they were never seen by the owner. The cascade lets a few owner rules, stated once, settle most fine-grained decisions without asking, and checks that they do. Hand-run once, it failed in three ways that the files below are built against: the cold citation check was skipped, questions the owner's rulings already decided were asked anyway, and an answered question was asked again.

**Selecting it.** The mode is called cascade and is chosen per request: `/plan-ledger cascade` turns it on for that run, `/plan-ledger normal` turns it off for that run, and the config's `cascade.enabled` only sets the default for a new ledger when neither is given. An existing ledger keeps its `mode:` line; an invocation naming the other mode for it stops and tells the owner. The ledger's `mode:` line records the mode so a resume knows it.

**What it adds.** A principles sheet (principles, a tie-break order, defaults per kind of decision, rulings, an always-to-owner list), built once per project from the owner's statements or from a sift of the owner's past messages. Planning then runs top-down in levels: draft with a cited rule on every line, a trio of cold judges for the non-obvious, a cold citation check, a cold red-team for spec gaps and design checks before the next level, and one owner batch per level. Builder questions at stage 7 go through the same procedure. The mode lives in its own stage files and in one gated paragraph in each of stages 0, 1, 2, 3, 5, 6, 7 and 8; in normal mode none of it applies.

| File | What it holds |
|---|---|
| `stages/cascade-method.md` | layers, derived-line format, gap rule, pile-up, order of work, trio, citation check, owner answers become rules, standing rules |
| `stages/cascade-first-use.md` | building the principles sheet, including the one-off transcript sift |
| `stages/cascade-levels.md` | the level loop and the owner batch |
| `stages/cascade-build.md` | stage 7 in this mode |
| `stages/cascade-common.md` | rules every cascade role needs and the two review roles do not |
| `stages/principles-sheet-template.md` | the sheet's layout |
| `stages/role-sift-analyst.md`, `role-sift-kinds.md`, `role-sift-synthesis.md`, `role-sift-quotecheck.md` | the sift roles |
| `stages/role-trio-judge.md`, `role-citation-check.md`, `role-gap-redteam.md` | the level roles |

**Layout.** `stages/common.md` holds only what every dispatched agent needs (the cold-reviewer core, provenance tags, literal reading, citation, the never-list). The paragraphs only the contradiction pass and the drift check act on (their inputs, the two review-specific sentences of "Read literally", the severity scale, the output shape) sit, byte for byte, at the top of both `role-contradiction.md` and `role-drift.md`, so those roles receive the same sentences as when they were in `common.md`. Cascade roles read `common.md`, `cascade-common.md` and their own role file. The guarded-change `charter.md` and `stage-3.md` are reused by path through `cascade.redteam`, never copied. The copy of the review block in two role files is a known cost; splitting it into a shared review file is a possible later change.

**What a cascade run adds to the ledger.** A Cascade block (template in `stages/ledger-template.md`): the sheet pointer, the level order, the mechanism tally, trio results, citation-check results and owner batches; the raw agent outputs are in `cascade.records_dir`.

## Conventions the skill relies on

- Skill content is re-attached after a compaction only up to a token budget; the ledger on disk, not the
  session, is the state. A `SessionStart` hook on the `compact` matcher should point the session back at
  any `status: ACTIVE` ledger.
- Spec, brief, ledger and handoff files are covered by a read-before-edit hook so they are never edited
  from memory after a compaction.
- Cold agents run in the foreground of the planner's turn; a delegated runner never backgrounds a gated
  check.
- Model choice for every spawned agent is stated with a reason (default sonnet for document review).
