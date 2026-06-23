# Guarded Change — methodology

A gated loop for making changes (to code, plans, or designs) where **no AI-produced
artifact reaches "accepted" without an independent challenge**, and where **"done" is
proven against an explicit, measurable bar** — not asserted by the thing that produced it.

This document is the spec. The `guarded-change` skill *executes* it; a per-project config
*parameterizes* it. It is deliberately **project- and domain-agnostic** — nothing here
assumes a particular language, app, or metric.

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

## Core principles

- **Nothing self-certifies.** The author of an artifact never approves it. Review is done by
  a reviewer with *no shared context* with the author (a cold subagent), so it doesn't
  inherit the author's blind spots.
- **Evidence over rhetoric.** Every criticism cites a line/file or a concrete failure
  scenario. Where data exists, an argument from the data beats an argument from reasoning.
  "Seems fragile" is not a finding; "line N does X, which fails when Y" is.
- **Instrument before you build.** If a change's effect can't be measured, the plan is
  incomplete. The measurement and any new instrumentation are part of the plan, not an
  afterthought. (This is the rule that would have made missing telemetry impossible.)
- **A bar, set first.** "Done" is defined as measurable acceptance criteria *before*
  implementation, so completion is verified, not declared.
- **Information-preserving is not behavior-preserving.** In a **position-sensitive assembly**
  — one where order or adjacency is itself semantic: prompt assembly, precedence/override
  lists, middleware/pipeline stages, CSS-like last-wins rules — *not* ordinary code whose
  behavior is name- not position-bound — a change can keep every piece of content and still
  change behavior, when an element's effect depends on its *position* rather than its mere
  presence (recency, precedence, "before/after some input," adjacency). A check that only asks
  "is every piece still present?" passes such a change blind: the content survives, the
  behavior does not. The trap is not only *moving* an element: **adding** one can displace the
  element that worked *because it was last*, and **removing** one can change a neighbor's
  adjacency to the input it governs — so a diff in which "nothing moved" is not exoneration.
  (E.g. a directive whose compliance depends on appearing *before* the input it governs; a
  block that works *because* it is last.) When a change moves, reorders, adds, or removes
  anything in such an assembly, treat every affected element's *position* — including elements
  that did not themselves change — as load-bearing until shown otherwise.
- **"No issue found" is a valid result.** Reviewers are graded on precision, not body count.
  This removes the pressure to manufacture faults that makes aggressive review untrustworthy.

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

---

## Stage detail

**0 — Baseline.** Only when modifying an existing system. Run the project's baseline-capture
(from config) and store the measured metrics. Greenfield projects skip this; stage 8 then
runs conformance-only.

**1 — Spec.** A rich problem definition: what's wrong / wanted, why, constraints, prior art.
Deep enough that the plan and criteria can be derived from it without guessing intent.

**1.5 — Criteria.** The bar against which "done" is checked. Each criterion must be
**checkable**, by one of two means:
- **Automated** — true/false or a number from instrumentation — e.g. "resolves a named folder
  + approximate filename in ≤2 tool calls, with no parent-directory traversal."
- **Human-judged rubric** — for qualities not reducible to a metric (e.g. "the persona reads
  as less repetitive"). Allowed *only* as an explicit rubric: a named human judge, a written
  scale, and what counts as pass. "Works well" with no rubric and no judge still fails review.

This degraded mode exists because some changes (especially to subjective/emergent behavior)
genuinely cannot be reduced to a metric pre-build; the loop must not force a fake number.
Criteria are the **conformance oracle** for stage 8 and are **mandatory** — without them (in
either form) the loop refuses to proceed past stage 3, because completion would be
unverifiable.

**If the change touches a position-sensitive assembly** (moves, reorders, adds, or removes
content — see *Information-preserving is not behavior-preserving*), at least one criterion must
assert that the *behavior* which depended on the arrangement is preserved — not merely that
the content still appears somewhere. "Every block's text still survives in the assembled
output" is a content check; it cannot catch a position-sensitive element (see
*Information-preserving is not behavior-preserving*). Name the behavior and how it's checked
(e.g. "directive D still fires on the input class it governs," tested on a case that exercises
*only* that path. The criterion must **require empirical execution on that case** (carried out at stage 8) — not
satisfaction by re-inspecting the assembled text, which a reviewer can wrongly *reason* looks
fine. Where the effect is probabilistic (recency/precedence usually shift a *rate*, not flip a
switch), the criterion states the pass rate it expects and the number of runs that establishes
it (treat as a human-judged rubric per above if no clean numeric floor exists), rather than
relying on a single probe.

**2 — Plan.** How to build it, complete only when it also names: how each criterion will be
measured; what instrumentation must exist to measure it (and adds it to scope if absent); and
the thresholds that map findings to loop routing.

**3 / 6 — Red-team.** See charter below. Stage 3 reviews spec+criteria+plan; stage 6 reviews
code against criteria+plan.

**4 / 7 — Gates.** Route by the worst finding's severity (see severity model).

**5 — Build.** Implement per the plan.

**8 — Harness.** Measure, then check conformance (always) and regression (if baseline
exists). See below.

---

## The red-team charter (stages 3 and 6)

Run by a **cold, independent reviewer** — a subagent with no shared context with the author,
given read access to **both the artifact under review and the underlying source** (code,
data, prior docs) named in the project config's `redteam_context`. Code/data access is
load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
confidently wrong about how the system actually behaves.

The reviewer attacks on four **separate** lenses (kept distinct so one doesn't crowd out the
others):

1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
3. **Missed opportunity** — better approaches or optimizations left on the table.
4. **Unstated assumptions & risks** — what's being taken for granted that could be false.

Discipline that makes aggressive review trustworthy:
- **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
- **Rank every finding** by severity (below).
- **Flag the unverifiable.** Any claim the reviewer could not check against the source is
  reported as such — not silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear,
  not "didn't look hard enough."
- **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens
  is only valid if the review shows specific source evidence it actually consulted
  (file:line, log rows). A clean factual verdict with zero source citations is treated as an
  un-run review and re-run — this is the guard against the reviewer reasoning from the
  artifact alone and rubber-stamping it (the failure this whole loop targets).
- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
  cited file:lines / log rows actually exist and say what's claimed. Citations are the one
  guard defending the loop's founding failure; a fabricated citation would defeat it, so the
  guard itself must be spot-checked (cheap: verify a few, not all).
- **If the change touches a position-sensitive assembly, test for position/order sensitivity**
  (lens 4). This triggers only where order/adjacency is itself semantic — prompt assembly,
  precedence/override lists, pipeline/middleware stages — *not* ordinary code whose behavior is
  name- not position-bound (don't flag every rename or function-extraction). Within such an
  assembly the trigger is *any* edit — move, reorder, **add, or remove** — and the elements to
  test include ones that **did not themselves change** (an added tail block displaces the old
  last element; a removal changes a neighbor's adjacency). For each such element ask: does its
  effect depend on *where* it sits — relative to other content (recency, adjacency, precedence)
  or to an input it governs (before/after)? If yes, "all the information is still present" is **not** a clean
  verdict for that element; the finding is the *behavior* change, and it ranks by impact, not
  by whether any text was lost.

The reviewer is graded on **precision** (are its findings real?), not on how many it raises.

---

## Severity model and gate routing

| Severity | Meaning | Stage 4 (plan) | Stage 7 (code) | Stage 8 (harness) |
|---|---|---|---|---|
| **Blocker** | wrong problem / will not work / unverifiable | → 1 | → 5 | → 1 |
| **Major** | sound goal, materially wrong approach | → 2 | → 5 | → 1 or 2 (human call) |
| **Minor** | real but local; fixable in place | fix → proceed | fix → proceed | fix → proceed |
| **Nitpick** | style/clarity; optional | log → proceed | log → proceed | log → proceed |

The severity threshold is what stops the loop from thrashing on marginal findings. A
borderline regression that's an acceptable tradeoff is a **human decision**, not an automatic
restart — the loop surfaces it ranked; a person rules.

**Iteration cap (anti-livelock).** A blocker/major that routes *backward* is bounded: after
**2 bounces at the same gate on the same finding class**, the loop **stops and a human breaks
the tie** (accept the risk, change the goal, or kill the change). **"Same finding class" =
same gate (by stage number) + same targeted artifact section, regardless of wording** — so a
rephrased objection, or the *same kind* of defect resurfacing in a nearby spot (e.g. "this
metric isn't measurable from the logs" raised against a different metric field), still counts
toward the cap. This prevents livelock-by-rephrasing, where each lap nominally raises a
"different" finding that is really the same unresolved disagreement. Each backward route
carries the prior review's findings forward (via `decisions.md`) so the next reviewer confirms
they were addressed rather than re-deriving. Without this, a hard disagreement can cycle
1→3→1→3 (or 5→7→5→7) indefinitely, paying full review cost each lap.

---

## Stage 8 in detail — two different checks

- **Conformance (absolute, always runs).** Measured behavior vs. the acceptance criteria
  (1.5). *Did it do what we said it should?* Works for brand-new code because it needs no
  prior version.
- **Regression (relative, only if a stage-0 baseline exists).** Measured behavior vs. the
  pre-change baseline, on everything *other* than the new behavior. *Did we break a neighbor?*

A net-new feature still gets **both**, aimed differently: conformance on the feature,
regression on the surrounding system that already existed. A truly greenfield project (no
prior version of anything) runs conformance-only.

**Position-dependent criteria must be checked by execution, not inspection.** Any criterion
written under *Information-preserving is not behavior-preserving* (stage 1.5) is satisfied only
by **running its isolating case and observing the behavior occur** — never by re-reading the
assembled prompt/config to confirm the text is present. Text-presence is the exact check that
the position change defeats, so a harness that "verifies" such a criterion by inspection has
not run it. This is the cheapest reliable catch for the whole class and is why the criterion is
mandated up front: stage 3 reasons about it, but only stage 8 can prove it fired.

**Regression must be measured on a comparable workload, or it is advisory only.** Global
aggregate metrics (mean cost, mean tool-calls) computed over whatever happened to run will
move whenever the *new behavior* legitimately exercises the system more — producing a **false
regression** indistinguishable from a real one. A regression metric is only **gating** if
either (a) it's measured on a fixed/replayed held workload comparable to the baseline's, or
(b) the new behavior can be excluded from the aggregate. A metric that can't isolate the
change's own contribution is reported as **advisory** (surfaced, not auto-bouncing). The plan
(stage 2) names which metrics are gating vs. advisory and how the comparable workload is
obtained.

---

## The two layers

- **Layer 1 — agnostic core (this doc + the skill).** The loop, gates, severity model,
  red-team charter, stage-doc templates. Ships once; knows nothing about any specific project.
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
  there. This keeps "independence" from degrading into "skimmed whatever fit in context."
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

**`decisions.md` — the gate log (append-only).** Each gate (4, 7, 8) appends one entry:
which gate, the worst finding's severity, the route taken, and — for any **human override**
(accepting a major/regression, breaking an iteration-cap tie) — a one-line rationale with a
name. A clean pass-through is a single line. This is not just audit: the **iteration cap
depends on it** — counting "2 bounces at the same gate" and carrying prior findings forward
requires the bounce history to persist. Human acceptance of a known regression is the entry
that matters most ("why did we ship this?" gets a recorded answer).

Together these double as the audit trail and as context for reconstructing the work if lost.

---

## Human-in-the-loop

The skill executes stages 1–7 autonomously (reason, spawn cold reviewers, write docs, edit
code) and runs stage 8 if the config provides the check. It **stops for a human decision** at:
- any **blocker** (the loop is about to restart — confirm direction first),
- any **major** at stage 8 (regression-vs-tradeoff is a judgment call),
- **missing criteria or config** needed to proceed (it refuses rather than guesses).

Everything else it routes automatically per the severity model, reporting what it did.
