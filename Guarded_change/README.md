# Guarded Change — a process for AI-assisted changes (for the companion-emergence dev)

This is a short handoff describing a small, reusable process — and a Claude Code skill that
runs it — for making non-trivial changes (code, plans, designs) without two specific failure
modes slipping through. It's written to be adopted by anyone using Claude Code; the
companion-emergence config is included as a worked example, not because the process is
specific to it.

If you only read one section, read **"The two failures it guards against"** — the rest is how.

---

## TL;DR

- **What:** a gated loop — `spec → criteria → plan → red-team → build → red-team → harness` —
  with two hard rules: (1) nothing an AI produces is accepted on that same AI's say-so; an
  **independent, cold reviewer** challenges it. (2) "done" is checked against a **measurable
  bar written before building**, not declared afterward.
- **Why:** the most expensive AI-assisted mistakes aren't bad code — they're *confident
  reasoning that was never challenged* and *changes whose effect nothing measured*. This loop
  is built specifically against those two.
- **How to use it three ways:**
  1. As a **Claude Code skill** you invoke (`guarded-change`) — it runs the loop for you,
     spawning the cold reviewers itself.
  2. As a **checklist** you apply by hand to any change, with or without an agent.
  3. As a **mindset**: "who challenged this, and what number proves it's done?"

---

## The two failures it guards against

Both of these are real patterns, not hypotheticals — they're drawn from the 0.0.38
investigation, and they're worth naming because they're easy to fall into and hard to see from
the inside.

**1. The unchallenged decision.** An AI gives a confident assessment ("this caching change
isn't worth it / would hurt"), and that assessment is accepted because it sounds rigorous. The
problem isn't that the model was necessarily wrong — it's that *the same model that proposed
the conclusion also graded it*. Nothing independent pushed back. When you ask one Claude
session "is my plan sound?", you tend to get a sympathetic reviewer that inherited your
framing. The fix is structural: the reviewer must be a **fresh session with no shared
context** and **read access to the actual source/data**, charted to *disagree* and to *cite
evidence* — not to reassure.

**2. The unmeasured regression.** A change ships, behavior degrades somewhere, and nothing
flags it — because no one decided *before building* what "correct" meant or what signal would
reveal a regression. The 0.0.38 file-tool behavior was only diagnosable because a log happened
to exist (and partly *didn't* — there were gaps we had to flag). The rule that prevents this:
**instrument before you build.** If you can't state how you'll measure the change's effect, the
plan isn't finished yet.

The loop below is just these two rules made into steps.

---

## The loop

```
0    BASELINE    (if a prior version exists) snapshot current measurable behavior
1    SPEC        what needs doing and why — rich enough to derive the rest
1.5  CRITERIA    the measurable definition of "done" — set BEFORE building
2    PLAN        how — and HOW you'll measure it, what to instrument, what bounces the loop
3    RED-TEAM    a cold, independent reviewer attacks {spec, criteria, plan}   ← most important
4    GATE        blocker→back to 1 │ major→back to 2 │ minor→fix & go │ clean→build
5    BUILD       implement
6    RED-TEAM    a cold reviewer checks the code against {criteria, plan}
7    GATE        blocker/major→back to build │ minor→fix & go │ clean→harness
8    HARNESS     measure reality → conformance (vs criteria) + regression (vs baseline)
                 bounce by severity, or done
```

The **stage-3 plan review is the highest-leverage step** — it catches a missing measurement
plan or an un-instrumented change *before any code is written*, which is the cheapest place to
catch a regression. Stages 6 and 8 are backstops.

A few deliberate design choices worth knowing:

- **"No issue found" is a valid review result.** Reviewers are graded on *precision*, not body
  count — so there's no pressure to manufacture nitpicks, which is what usually makes
  "aggressive review" untrustworthy.
- **Citations are mandatory, and spot-checked.** A clean factual verdict with no source
  citations is treated as a review that didn't actually run — that's the specific guard against
  a reviewer reasoning from the document alone and rubber-stamping it.
- **There's an iteration cap.** If the same finding bounces the loop twice at the same gate, it
  stops and a human decides — so a genuine disagreement can't livelock by getting rephrased
  each lap.
- **Some things can't be reduced to a number, and that's allowed.** Criteria can be a
  *human-judged rubric* (named judge + written scale + what counts as pass) for subjective
  qualities like persona feel — but "works well" with no rubric still fails review.

---

## How it's structured (two layers)

- **Layer 1 — the agnostic core.** The loop, the reviewer charter, the severity model. Knows
  nothing about any specific project. This is `METHODOLOGY.md` (the spec) + `SKILL.md` (what
  Claude Code executes).
- **Layer 2 — a per-project config.** What "correct" and "regression" mean *here*, how to
  capture a baseline, how to measure a build, and the thresholds. One small file per repo.

"Harness" just means *an empirical check against a defined bar* — for companion-emergence
that's diffing the telemetry JSONL logs; for another project it'd be a test suite, a latency
benchmark, or an eval set. Only Layer 2 knows which.

---

## Adopting it (you use Claude Code, so this is the short path)

1. **Drop the skill in.** Copy the `guarded-change/` folder (`METHODOLOGY.md` + `SKILL.md`)
   into your `~/.claude/skills/`. Claude Code will then offer `guarded-change` as a skill.
2. **Write a Layer-2 config** for your checkout. The companion example
   (`guarded-change.companion.md`) is a complete, commented template — copy it and adjust the
   paths/metrics. The config contract is documented at the bottom of `METHODOLOGY.md`.
3. **Invoke it on a change.** Point it at a change request; it creates a `changes/<slug>/`
   folder, walks the stages, spawns the cold reviewers itself, and stops to ask you only at the
   decisions that are genuinely yours (a blocker about to restart the loop, a regression-vs-
   tradeoff judgment, or missing criteria — it refuses to invent those rather than guess).

You don't *need* the skill — the loop works as a manual checklist too. But since the same tool
you already use can run it, the cheapest version is to let it.

---

## The companion-emergence config — and an honest caveat

`guarded-change.companion.md` is the worked example, and dogfooding it surfaced something worth
flagging to you directly, because it's exactly the kind of thing the process is meant to catch:

- **Regression is advisory-only today**, because there's no fixed replay workload — metrics
  computed over "whatever turns happened to run" can't isolate one change's contribution from
  normal variation. The config says so plainly rather than pretending the numbers gate.
- **Two tool-log metrics are marked BLOCKED**, not live, because the tool log's `request_id`
  is only stamped on ~41% of rows (it's gated on an env var set only on the MCP-subprocess
  path — `audit.py:153-155` / `provider.py:930`), and `record_monologue` bookkeeping rows
  inflate the counts. A metric computed over a non-random 41% *looks* like coverage while
  silently lying. The config records the gap and the exact instrumentation that would unblock
  it (stamp a correlation key on *all* tool rows + tag tool-vs-bookkeeping rows) rather than
  reporting a number it can't stand behind.

That second point is itself a small example of "instrument before you build" and of the loop's
iteration cap firing: the measurability problem came up twice, so it was escalated to a human
decision instead of being patched a third time. The takeaway isn't "the logs are bad" — it's
that the process *names* what it can't measure instead of guessing, which is the whole point.

---

## Files

| File | What it is | Audience |
|---|---|---|
| `METHODOLOGY.md` | The authoritative spec — loop, reviewer charter, severity model, config contract | the skill / a careful reader |
| `SKILL.md` | The operating procedure Claude Code executes | the agent |
| `guarded-change.companion.md` | The companion-emergence Layer-2 config (worked example/template) | you |
| `this file` | Why it exists and how to adopt it | you |

Questions worth carrying into any change, even if you never run the skill: *Who challenged
this, independently? What number proves it's done — and was that number defined before I
started building?*
