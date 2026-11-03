# Plan Ledger — methodology and config contract

## Why it exists

A design conversation between a human owner and an AI planner produces a spec that a build lane treats as
the owner's decisions. Five failures, observed in real planning, motivate this skill:

1. **A recommendation became a decision.** A research agent framed the feature one way; the planner
   repeated the framing; the owner answered a one-word option to a question whose premise was inverted;
   the spec shipped the inverse of the owner's design and nobody noticed for a day.
2. **A sub-decision slid in as narration.** The owner approved "build it properly, not a threshold" and
   the planner then wrote a hardcoded constant into the spec four times, framed as the virtue of the new
   design, without ever posing fixed-versus-derived as a choice.
3. **An existing code shape became architecture.** A pre-existing side database was inherited as "where
   the data already lives", a sequencing question was answered against the owner's goal ("keep this PR
   disjoint" defeating "one database"), and no ruling was ever made.
4. **A premise passed as a decision.** The owner ruled that, in that case, mechanism X was the simplest option, on the strength of the planner's explanation of what X covered; the ledger kept the quote and not the explanation. An hour later a proposal about another mechanism said, in passing, that its changes "go
   through the normal queue like everything else"; the owner answered "simplify"; the passing premise
   counted as confirmed, and the spec sent every event, from every process, through the queue. The drift
   check passed both rulings because its record of what the owner meant was the owner's quotes alone.
5. **An owner's description was corrected from a draft.** The owner described how a mechanism worked, phrased as
   a question ("as I understand it the queue holds X, not Y?"). The planner treated it as a question and
   answered by correcting the owner from a draft line that the owner had not written. The description stayed in a log line as a question and never became a
   statement or a decision, so nothing later could be checked against it, and the spec was built on the draft's
   version. Asking the owner to confirm each such description is no cure: they work a design out by describing
   it and asking until the answer falls out, they may have it mixed up with another mechanism, and each
   confirmation request costs attention they are spending on the design.

A transcript-only drift audit passed the first three, because the owner's standing principles were not an
input and because a later "good to go" was read as confirming sub-decisions the proposal never stated. A
later ledger-only drift check passed the fourth, because it read the owner's quotes without the messages
they answered. No check compared the fifth, because the description was in no line the checks compared.

The discipline therefore has five parts: **provenance** on every decision (and, where an answer depends on
what the planner said, that explanation as a `rests on` clause); **sentence-level confirmation**
of anything with a direction; **forks always posed**; **invariants as a checkable file** that cold
reviewers receive; and **owner statements** recorded in the owner's words, as statements and not decisions,
never corrected from a draft, and compared with the spec by the drift check.

## Where it sits among the siblings

`plan-ledger` (decide, with provenance) → `guarded-change` (build, gated) ; `dragonfly` (diagnose) and
`data-distiller` (distill) feed it. Drift-Detector, when built, is the heavy transcript-based audit; the
stage-6 drift check here is the light one that runs on the ledger's quotes and the messages they answered,
plus a search of the owner's messages (the answered-messages file) for statements about the mechanisms the spec
applies, not a full audit of the transcript.

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
cascade:                          # OPTIONAL block; cascade mode needs it; normal mode needs only owner_transcripts, for the answered-messages file
  enabled: true                   # the default mode for a new ledger whose invocation names neither (`/plan-ledger cascade` or `/plan-ledger normal`); false or absent = normal
  principles_path: <path>         # the owner-approved principles sheet (template: stages/principles-sheet-template.md); may be absent on first use
  records_dir: <dir>              # raw outputs of trio judges, compliance checks, red-teams, sift agents, facts files; created on first use
  owner_transcripts: <path>       # where the owner's own past messages can be read (sift; quote verification; the answered-messages file of stages 1 and 6, in either mode)
  redteam:                        # guarded-change files the level red-team reuses by path
    charter: <path to guarded-change stages/charter.md>
    stage3: <path to guarded-change stages/stage-3.md>
models:
  cold_agents: sonnet             # reason stated per spawn; opus only with a named sonnet shortfall
```

## What a run produces

- `<ledger_dir>/<slug>-LEDGER.md` (the state; template in `stages/ledger-template.md`).
- The builder spec (`*-spec.md` or `*-brief.md`), derived from the approved sheet.
- `<ledger_dir>/<slug>-answered.md`: for each owner message of the design conversation (their own AskUserQuestion answers included, as the selected option or typed text), the planner message it answered, verbatim from the transcript (stage 6; also built at a topic wrap-up, stage 1).
- Cold-pass reports appended to the ledger's Decisions log (or a `reports/` folder next to it).
- Issues for any OPEN fork that shipped as a working assumption (stage 8).

## Cascade mode (optional; `/plan-ledger cascade`)

**Why.** In one project a fix approved as 55 owner decisions grew to 247 during the build. Almost all the additions were derived by the planner while answering the builder's questions; each was locally reasonable, and together they were never seen by the owner. The cascade lets a few owner rules, stated once, settle most fine-grained decisions without asking, and checks that they do. Hand-run once, it failed in three ways that the files below are built against: the cold check was skipped, questions the owner's rulings already decided were asked anyway, and an answered question was asked again. A later run added a fourth: a build-time answer named the project's shared module for one operation and nothing for the others, skipped the red-team, and passed its check because the check only tested whether the cited rules decided the line; the builder then hand-wrote the other operations beside the shared module, against two of the owner's principles. The principles are a test an answer must pass, not a justification for it, so the check now tests every answer against every principle and prior decision, and build-time answers take the same full procedure as a level.

**Selecting it.** The mode is called cascade and is chosen per request: `/plan-ledger cascade` turns it on for that ledger, `/plan-ledger normal` turns it off for that ledger, and the config's `cascade.enabled` only sets the default for a new ledger when neither is given. An existing ledger keeps its `mode:` line (one with no `mode:` line takes the config default); an invocation naming the other mode for it stops and tells the owner. Cascade mode needs the config's `cascade` block, and first use with no principles sheet stated or sifted stops and tells the owner. The ledger's `mode:` line records the mode so a resume knows it.

**What it adds.** A principles sheet (principles, a tie-break order, defaults per kind of decision, rulings, an always-to-owner list), built once per project from the owner's statements or from a sift of the owner's past messages. Planning then runs top-down in levels: draft with a cited rule on every line, a trio of cold judges for the non-obvious, a cold compliance check (a pass means the line meets every principle and prior decision, recorded per principle as meets, violates or n.a. with the line that shows it; the rule a line cites records where it came from and never makes it pass), a cold red-team for spec gaps, principle compliance and design checks before the next level, and one owner batch per level. Builder questions at stage 7 go through the same full procedure, red-team included, with no reduced path. The mode lives in its own stage files and in one gated paragraph in each of stages 0, 1, 2, 3, 4, 5, 6, 7 and 8; in normal mode none of it applies, except that the answered-messages file (stages 1 and 6) reads `cascade.owner_transcripts` and the first-use Extract step in either mode.

| File | What it holds |
|---|---|
| `stages/cascade-method.md` | layers, derived-line format, gap rule, pile-up, order of work, trio, compliance (the pass rule and the check), owner answers become rules, standing rules |
| `stages/cascade-first-use.md` | building the principles sheet, including the one-off transcript sift |
| `stages/cascade-levels.md` | the level loop and the owner batch |
| `stages/cascade-build.md` | stage 7 in this mode |
| `stages/cascade-common.md` | rules every cascade role needs and the two review roles do not |
| `stages/principles-sheet-template.md` | the sheet's layout (a filled-in, scrubbed example: `examples/principles-sheet-example.md`; for the invariants doc: `examples/invariants-example.md`) |
| `stages/role-sift-analyst.md`, `role-sift-kinds.md`, `role-sift-synthesis.md`, `role-sift-quotecheck.md` | the sift roles |
| `stages/role-trio-judge.md`, `role-compliance-check.md`, `role-gap-redteam.md` | the level roles |
| `stages/role-review-cascade.md` | the additions the contradiction pass and the drift check read in cascade mode only (principles table, prior decisions, what the spec leaves out) |

**Layout.** `stages/common.md` holds only what every dispatched agent needs (the cold-reviewer core, provenance tags, literal reading, citation, the never-list). The paragraphs only the contradiction pass and the drift check act on (their inputs, the two review-specific sentences of "Read literally", the severity scale, the output shape) sit, byte for byte, at the top of both `role-contradiction.md` and `role-drift.md`, so those roles receive the same sentences as when they were in `common.md`. Cascade roles read `common.md`, `cascade-common.md` and their own role file. The contradiction pass and the drift check read `role-review-cascade.md` after their role file in cascade mode, so their role files stay as they are in normal mode. The guarded-change `charter.md` and `stage-3.md` are reused by path through `cascade.redteam`, never copied. The copy of the review block in two role files is a known cost; splitting it into a shared review file is a possible later change.

**What a cascade run adds to the ledger.** A Cascade block (template in `stages/ledger-template.md`): the sheet pointer, the level order, the mechanism tally, trio results, compliance-check results, the Principles check table and owner batches; the raw agent outputs are in `cascade.records_dir`.

## Conventions the skill relies on

- Skill content is re-attached after a compaction only up to a token budget; the ledger on disk, not the
  session, is the state. A `SessionStart` hook on the `compact` matcher should point the session back at
  any `status: ACTIVE` ledger.
- Spec, brief, ledger and handoff files are covered by a read-before-edit hook so they are never edited
  from memory after a compaction.
- Cold agents run in the foreground of the planner's turn; a delegated runner never backgrounds a gated
  check.
- Model choice for every spawned agent is stated with a reason (default sonnet for document review).
