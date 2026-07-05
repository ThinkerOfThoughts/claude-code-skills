# Guarded Change — methodology

A gated loop for making changes (to code, plans, or designs) where **no AI-produced
artifact reaches "accepted" without an independent challenge**, and where **"done" is
proven against an explicit, measurable bar** — not asserted by the thing that produced it.

This document is the **orientation/reference spec**: why the loop exists, the loop diagram,
the two layers, the config contract, and what a run produces. The **per-stage procedure and
the rules that govern each stage now live in `stages/`** (one file per stage, plus the shared
red-team charter `stages/charter.md`); `SKILL.md` is the router that walks the loop and points
at those files. This file is opened for orientation and config setup — not to run a stage.

It is deliberately **project- and domain-agnostic** — nothing here assumes a particular
language, app, or metric.

---

## Why this exists

AI-assisted development has two recurring, expensive failure modes:

1. **Unchallenged decision.** A judgment ("X isn't worth doing", "this plan is sound") is
   accepted on one model's reasoning and never red-teamed. The model sounds confident; the
   confidence is mistaken for correctness.
2. **Unmeasured regression.** Code behavior degrades and nothing flags it, because nobody
   defined — *before building* — what "correct" means or what to measure. The regression is
   only catchable if the right signal happened to be logged.

This loop guards against both: every stage's output is challenged by an **independent**
reviewer (mode 1), and every change carries its own **measurement plan and acceptance
criteria** defined up front (mode 2).

---

## The loop

```
0    BASELINE      (if a prior version exists) snapshot current measurable behavior
1    SPEC          rich problem definition — what needs to be done and why
1.5  CRITERIA      measurable definition of "correct/done" — the bar stage 8 checks
2    PLAN          how to build it. INCOMPLETE unless it also specifies:
                     • measurement — how the criteria (1.5) will be verified
                     • instrumentation — what must be logged/exposed to measure it (add if absent)
                     • thresholds — what severity of finding bounces the loop vs. proceeds
3    RED-TEAM      independent cold review of {1, 1.5, 2} — the assumption-catcher
4    GATE          blocker → 1 │ major → 2 │ minor → fix-and-proceed │ clean → 5
5    BUILD         implement
6    RED-TEAM      independent cold review of the code against {1.5, 2}
7    GATE          blocker/major → 5 │ minor → fix-and-proceed │ clean → 8
8    HARNESS       measure actual behavior, then:
                     • CONFORMANCE (always): actual vs. acceptance criteria (1.5)
                     • REGRESSION (only if a stage-0 baseline exists): actual vs. baseline
                   bounce by severity → 1 │ clean → done
```

The **most important gate is stage 3**, not 6 or 8. Because 1.5, instrumentation, and
thresholds all live upstream of the build, the plan-red-team catches a missing measurement
plan or an un-instrumented change *before a line of code is written* — the cheapest possible
place to catch a regression. Stages 6 and 8 are backstops.

The loop diagram above is **orientation**. The operative routing table (which severity routes
where, at each gate) lives written-in-full in each gate file — `stages/stage-4.md`,
`stages/stage-7.md`, `stages/stage-8.md` — not here.

---

## Stage index — where each stage's detail lives

| Stage | File | What it covers |
|---|---|---|
| 0 — Baseline | `stages/stage-0.md` | baseline only if a prior version + config baseline exist |
| 1 — Spec | `stages/stage-1.md` | rich problem def; declares expected touched files |
| 1.5 — Criteria | `stages/stage-1.5.md` | checkable, labeled accept bar; position/concurrency criteria; self-check criteria |
| 2 — Plan | `stages/stage-2.md` | how + measurement + instrumentation + thresholds; accessor enumeration |
| 3 — Red-team plan | `stages/stage-3.md` + `stages/charter.md` | cold review of {1,1.5,2}; coverage challenge + label audit |
| 4 — Gate | `stages/stage-4.md` | route by severity; criteria freeze; path-validation blocks gate 4 |
| 5 — Build | `stages/stage-5.md` | implement per the plan |
| 6 — Red-team code | `stages/stage-6.md` + `stages/charter.md` | cold review of code vs {1.5,2}; mechanical `git diff` |
| 7 — Gate | `stages/stage-7.md` | route by severity |
| 8 — Harness | `stages/stage-8.md` | conformance + regression; per-criterion verification table; freeze verify |

The **red-team charter** (four lenses + discipline + provenance + the conditional
position/concurrency lenses) is shared by stages 3 and 6 in `stages/charter.md`. The **severity
model** and the **stage-8 verification detail** live in the gate/harness stage files.

---

## The two layers

- **Layer 1 — agnostic core (this doc + the skill + the stage files).** The loop, gates,
  severity model, red-team charter, stage-doc templates. Ships once; knows nothing about any
  specific project.
- **Layer 2 — per-project config.** What "correct" and "regression" mean here, how to capture
  a baseline, how to measure the build, and the thresholds. Supplied per repo. This is the
  only place project specifics live.

"Harness" therefore means **an empirical check against a defined bar**, not any particular
script. For one project that's diffing telemetry logs; for another it's a test suite, a
latency benchmark, or an eval set. The check command lives in Layer 2.

---

## The config contract (Layer 2)

A project supplies a config so the skill can run stages 0 and 8. Minimum shape:

```yaml
project: <name>

redteam_context:          # paths the cold reviewer MUST read to check claims vs. source.
                          # LISTED IN PRIORITY ORDER — first entries are the entrypoints to
                          # read first; a cold subagent cannot read a large tree exhaustively,
                          # so order matters and each entry may carry a "why/what to look for".
  - path: <most-relevant-source>
    note: <what to check here first>
  - path: <secondary>
    note: <...>

measurement:
  baseline:               # OPTIONAL — omit for greenfield; enables stage-0 + regression
    how: <command to run | manual procedure description>
    output: <where measured metrics land>
  check:                  # REQUIRED for stage 8 — measures the current build
    how: <command to run | manual procedure description>
    output: <where measured metrics land>

metrics:                  # standing project metrics used for REGRESSION
  - name: <metric>
    source: <file/field or how to extract>
    direction: lower_is_better | higher_is_better | stable
    regression_threshold: <e.g. "+10%">   # bounce if worse than this vs. baseline
```

Rules:
- **`redteam_context` is priority-ordered.** Because a cold subagent can't exhaustively read a
  large codebase, list the most relevant entrypoints first with a short note on what to check
  there. This keeps "independence" from degrading into "skimmed whatever fit in context." (The
  operative reviewer-spawn form of this rule lives in `stages/stage-3.md` / `stages/stage-6.md`.)
- **Paths are validated, not assumed.** Every path handed to a cold reviewer
  (`redteam_context`, the spec's touched files, fixture paths) is mechanically checked to exist
  and be readable — at run start and at each reviewer spawn. **Gate 4 may not pass until the
  run-start validation result is recorded in `decisions.md`.** The full operative rule (and its
  gate-4 block) lives written-in-full in `stages/stage-3.md`, `stages/stage-4.md`, and
  `stages/stage-6.md`.
- **Acceptance criteria (1.5) are per-change**, authored in the change's spec — *not* in this
  config. The config holds standing measurement/regression setup that's stable across changes.
- **Criteria are mandatory; baseline is optional.** No criteria → the loop won't pass stage 3.
  No baseline → stage 8 runs conformance-only and says so.
- If a change needs a signal the project doesn't yet expose, the **plan (stage 2) adds the
  instrumentation** — and the config's `metrics`/`check` are updated as part of that change.

---

## What a run produces (artifacts)

One folder per change, e.g. `changes/<slug>/`:

```
0-baseline.md       (if applicable) measured pre-change metrics
1-spec.md           problem definition
1.5-criteria.md     measurable acceptance bar
2-plan.md           how + measurement + instrumentation + thresholds
3-redteam-plan.md   cold review of {1,1.5,2} with ranked findings
   ...build...
6-redteam-code.md   cold review of code vs {1.5,2}
8-harness.md        conformance + regression results, verdict
decisions.md        append-only gate log (see below)
```

The review docs (`3-redteam-plan.md`, `6-redteam-code.md`, and any targeted post-6 check
record) are **verbatim records** — each embeds the charter given, the exact context list, and
the reviewer's raw output per the charter's provenance rule; the author's interpretation
belongs in `decisions.md`.

**`decisions.md` — the gate log (append-only).** Each gate (4, 7, 8) appends one entry: which
gate, the worst finding's severity, the route taken, and — for any **human override** — a
one-line rationale with a name. This is not just audit: the **iteration cap depends on it**.
Human acceptance of a known regression is the entry that matters most. At stage 8, the entry
also records each **gating** criterion's disposition. The operative form of this rule lives in
the gate/harness stage files (`stages/stage-4.md`, `stages/stage-7.md`, `stages/stage-8.md`).

Together these double as the audit trail and as context for reconstructing the work if lost.

---

## Human-in-the-loop

The skill executes stages 1–7 autonomously (reason, spawn cold reviewers, write docs, edit
code) and runs stage 8 if the config provides the check. It **stops for a human decision** at
any blocker (loop about to restart), any major at stage 8, a gating criterion that cannot be
verified pre-ship, and missing criteria or config. The full stop conditions live in
`stages/stage-1.5.md`, `stages/stage-4.md`, and `stages/stage-8.md`; everything else routes
automatically per the severity model, reporting what it did.
