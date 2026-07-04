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
- **A deferred gating criterion is not a met one.** "Done" requires every *gating* acceptance
  criterion (1.5) to be **empirically verified first**, by exercising the path it governs. A
  gating criterion that is postponed to "live/production," satisfied by a *proxy* that avoids
  that path (a mocked dependency, a disabled flag, an input class that never triggers it), or
  quietly dropped from the results, has **not** been met — deferral silently converts *proven*
  done into *hoped* done. Advisory criteria may be deferred; gating ones may not.
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
- **Shared state has more than one accessor.** When a change **introduces a new unsynchronized
  accessor, or a new read→slow-work→write window, over shared mutable state whose atomicity an
  existing transaction/lock does not already enforce**, correctness depends on *every* accessor
  of that state, not just the one being written. A guard (lock, transaction, queue, CAS) is only
  as strong as its **scope** — the set of accessors it actually covers; a *different*, lock-free
  accessor whose write interleaves in the gap is silently lost (lost update / torn write). This
  is the same blind spot as *Information-preserving is not behavior-preserving*, one level out: a
  review that only asks "is this guard correct?" passes the change, because the defect lives in an
  accessor it never **enumerated**. A guard's mere existence does not settle "already enforced" —
  its scope must be enumerated, not assumed; when it is unclear whether a guard covers *every*
  accessor, treat the state as unguarded. Triggers only where the change alters the concurrency
  structure over shared state — *not* ordinary single-threaded or already-serialized code.
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
Deep enough that the plan and criteria can be derived from it without guessing intent. The spec
also **declares the expected touched files** — that list joins every cold reviewer's context
(see the charter's closed set).

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

**Each criterion is labeled gating or advisory, and defaults to gating.** A **gating** criterion
must be verified (by execution, stage 8) for the change to be accepted; an **advisory** one is
surfaced but does not block. A criterion is advisory *only* by explicit choice with a stated
reason — an unlabeled criterion is gating, so a forgotten label fails safe. (This is the
criterion-level sibling of the gating-vs-advisory distinction drawn for regression *metrics*
under "Regression must be measured on a comparable workload"; the weight there protects against
false regressions, the weight here against unverified completion.)

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

**If the change introduces a new accessor or read-modify-write window over shared mutable state**
(see *Shared state has more than one accessor*), at least one criterion must assert the
**atomicity / no-lost-update** property under a concurrent interleaving — a write by one accessor
is not silently clobbered by another. Name the interleaving and how it is checked (e.g. "an append
by accessor B during accessor A's read→write window survives"). Because real races are
**non-deterministic**, the criterion must be checked **deterministically** — by *injecting* the
competing mutation into the middle of the guarded window (not hoping a live thread race lands
there) — or, where only a live race is possible, over a **stated number of runs with a pass-rate
floor** (treat as the probabilistic rubric above). And, like any representative harness, the
interleaving test must **fail against the unguarded version**; a test that passes with and without
the guard proves nothing. Reasoning that "the lock covers it" is not satisfaction — only the
executed interleaving is.

**Criteria freeze.** When gate 4 routes to build, `1.5-criteria.md` **freezes** and its hash
(or a verbatim copy) is recorded in `decisions.md`. The freeze binds to the route-to-build
version, which must equal the version the stage-3 reviewer read — except for gate-4 in-place
fixes, each traceable to a logged finding, with the criteria diff recorded in `decisions.md`.
Stage 8 verifies the file still matches the recorded version; a divergence is a post-freeze
edit → the affected criteria's PASSes are invalid unless the edit carries a `decisions.md`
entry (change + reason) and a targeted re-red-team of the edited criteria. Any **weakening**
(gating→advisory, a loosened threshold, a narrowed scope) is audited exactly like an advisory
relabel under the charter's label-audit — it needs a legitimate reason or the original stands.

**2 — Plan.** How to build it, complete only when it also names: how each criterion will be
measured; what instrumentation must exist to measure it (and adds it to scope if absent); and
the thresholds that map findings to loop routing.

**If the change introduces a new accessor or read-modify-write window over shared mutable state**
(see *Shared state has more than one accessor*), the plan is incomplete until it **enumerates
every concurrent accessor (reader and writer) of that state and names which the guard covers and
which it does not** — an *accessor │ reader/writer │ synchronized by │ covered by the guard?*
table is the natural form. The gap between "accessors that exist" and "accessors the guard
covers" is where the lost update hides; naming it at plan time (per *Instrument before you build*)
is the cheapest place to catch it — cheaper than the red-team, far cheaper than production.

**3 / 6 — Red-team.** See charter below. Stage 3 reviews spec+criteria+plan; stage 6 reviews
code against criteria+plan. At stage 6 the reviewed diff is generated **mechanically**
(`git diff` against the recorded base, or an equivalent captured command), the command recorded
in `6-redteam-code.md` — a hand-curated file set = the review is un-run for the omitted scope.

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
- **Provenance is part of the review record.** Every cold-review record, wherever in the run it
  occurs (stage 3/6, a targeted post-6 check, a harness-embedded reviewer arm), embeds: (i) the
  verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's
  verbatim output (the author's summary lives in `decisions.md`, separately), (iv) the
  reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it
  read (the charter instructs the reviewer to report these). The charter given is the
  METHODOLOGY charter **core** verbatim — the four lenses + the unconditional discipline
  bullets, plus the coverage-challenge bullet for stage-3 reviews and any conditional lens
  (position / concurrency) whose trigger fires — with task-specific additions quoted
  as such. Reviewer input is a **closed set**: the named stage artifacts + the config's
  `redteam_context` + the spec's touched-files list + carried-forward findings from
  `decisions.md`; any supplementary author-authored context must be quoted in the record as
  such. A record missing any of these = the review is treated as **un-run**. In A/B harness
  arms, author-authored supplementary context is prohibited outright — a leak is a confound
  (see the concurrency-lens C3 attempt-1 record).
- **Challenge criteria coverage (stage 3).** Name the behaviors the change could plausibly
  alter that **no criterion observes** — each named gap needs a concrete scenario and ranks by
  impact. The finding is unmeasured blast radius, not "write more criteria"; precision
  discipline is unchanged. A stage-3 review with no coverage-challenge section (an explicit
  "none found" counts) is incomplete on lens 4 and treated as un-run for that lens.
- **Audit the criterion labels and the stage-8 verification table (the gating guard).** The
  weight on each criterion is itself a claim to challenge, not a given:
  • every criterion marked **advisory** must carry a legitimate reason — challenge any that looks
    like a dodge to avoid verifying a real gate (relabelling a gating criterion advisory is the
    deferral loophole in disguise);
  • every gating `verified = yes` must have exercised the **path the criterion actually governs** —
    challenge any verified against a proxy (a mocked dependency, a disabled flag, a
    non-triggering input class);
  • a route-(a) **"representative" pre-ship harness is a claim about representativeness** —
    challenge whether it truly exercises the governed path (the Option-B smoke was *believed*
    representative and was not);
  • a route-(b) named risk-acceptance must actually be present in `decisions.md` where a gating
    criterion is unverified.
  A gating criterion whose label or verification cannot survive this challenge is treated as
  unverified — the same as if it had been deferred.
- **A clean label-audit must be earned, like a clean factual lens.** A "labels and table look
  fine" verdict is valid only if the review shows, per gating criterion, which governed path it
  confirmed was exercised and what evidence it checked. An unsubstantiated clean label-audit is
  treated as un-run and re-run — the same guard the factual lens already carries above.
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
- **If the change introduces a new accessor or a new read-modify-write window over shared mutable
  state, map the accessors and challenge the guard's scope** (lens 4). This fires only where the
  change *alters* concurrency over shared state — not ordinary single-threaded or
  already-serialized code. Do two things: **(1) enumerate every concurrent reader and writer of
  that state** — including ones the change did not touch (a pre-existing lock-free appender, a
  background tick, a crash-recovery path); **(2) treat the guard's scope as a claim to
  challenge** — not "is the lock correct?" but "*which* accessors does this guard cover, and which
  does it leave out?" A guard's existence is not coverage: an unenumerated lock-free (or
  differently-guarded) accessor of the same state, or a read and write that straddle a slow
  operation during which another accessor can mutate the state, is the finding — ranked by the
  impact of the lost/torn write, not by whether the guarded path itself looks correct.

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

**The reviewer's severity routes.** For findings originating from a cold review (gates 4 and
7; at stage 8, findings from a targeted post-6 check), the gate routes on the **reviewer's**
stated severity — harness measurements at stage 8 route by the table as before. The author may
contest a severity only via a logged `decisions.md` entry; demoting a **blocker or major**
additionally requires the human tie-break (the same authority that breaks iteration-cap ties).
A silent unilateral demotion is a gate violation: the reviewer's routing stands.

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

**Concurrency criteria must be checked by executing an interleaving, not by inspecting the
guard.** Any criterion written under *Shared state has more than one accessor* (stage 1.5) is
satisfied only by **running a concurrent interleaving and observing the write survive** — never by
re-reading the lock/transaction code and reasoning it looks sufficient. Inspecting the guard is
the exact check the scope gap defeats: the guard *is* correct for the accessors it covers. Prefer
a deterministic harness that injects the competing mutation into the read→write window (a live
thread race need not be reproduced by luck); a pure-inspection "verification" of such a criterion
counts as `verified = no`.

**Every gating criterion must be verified by execution before "done" — no deferral, no proxy,
no silent drop.** A gating criterion (1.5) is satisfied only by running a case that exercises
*the actual path it governs* and observing the required behavior. Three dispositions that look
like progress but are **not** satisfaction — each shipped a real regression in practice:
- **Deferral** — "we'll confirm it live / in production." A gating criterion postponed past
  acceptance is unverified; the run is not done.
- **Proxy path** — verifying on a workload that *avoids* the governed path (a mocked dependency,
  a disabled feature flag, an input class that never triggers the behavior). Exercising a
  neighbor is not exercising the criterion. (Cf. *checked by execution, not inspection*, one
  level out: executed, but on the wrong path.)
- **Silent drop** — the criterion simply does not appear in the stage-8 results.

If a gating criterion **genuinely cannot be checked before ship** (needs production, billing, or
a live human/system), the loop has exactly two legal moves:
  (a) **Build a representative pre-ship harness** that exercises the real path cheaply (e.g. a
      scratch fixture asserting the behavior actually fires) and verify against it; or
  (b) **Escalate for named risk-acceptance** — a human explicitly accepts *that specific
      unverified criterion by name*, recorded in `decisions.md` as **"conditionally accepted —
      KNOWN UNVERIFIED RISK: <criterion>."**
Route (b) is the *only* way a gating criterion reaches ship unverified, and it is a conscious,
attributed decision — never a silent fold into "done."

**An unreviewed check is not a check.** Any new or modified executable check whose results
stage 8 will trust, created after the stage-6 review (the harness itself, a route-(a)
representative fixture, a rebuilt probe), gets a **targeted cold check before its results
count** — for representativeness, and, where the check guards a fix, that it fails against the
unguarded version; until then its results are `verified = no`. A defective check found this
way is discarded and rebuilt in place (logged in `decisions.md`), not a loop restart; findings
it raises about the change itself route via the gate-8 severity row. In-place fix diffs at
gates 7/8 are recorded in `decisions.md`, and a stage-8 fix-in-place re-runs the criterion
checks its diff could have invalidated.

`8-harness.md` therefore **must contain a per-criterion verification table**: one row per
criterion with columns *criterion │ gating/advisory │ path exercised │ verified by execution?
│ evidence │ result*. The **evidence** cell of every gating `verified = yes` row cites where
the raw output lives (the command run + an output file/excerpt); for a human-judged-rubric
criterion the pointer is the named judge + where the verdict is recorded. A gating PASS row
with no evidence pointer counts as `verified = no`, and the consumer's citation spot-verify
extends to a sample of evidence cells. Any **gating** row that is not `verified = yes` blocks "done" unless `decisions.md`
carries the matching named risk-acceptance. (Inspection-only "verification" of a gating
criterion counts as `verified = no`.) The table always lists every **gating** criterion;
advisory criteria may be summarized in one line. A run with no gating criteria says so and the
table is trivially short — the artifact scales to the change, not the reverse. For a
probabilistic or human-judged-rubric criterion (see stage 1.5), the "verified" cell records the
observed pass-rate over the stated number of runs (or the named judge's verdict), not a bare
yes/no — reusing the rubric the criterion already declared.

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
- **Paths are validated, not assumed.** Mechanically check every path handed to a cold
  reviewer (`redteam_context`, the spec's touched files, fixture paths) exists and is readable
  — at run start for paths that exist then, and at each cold-reviewer spawn for any path not
  yet validated. Gate 4 may not pass until the run-start validation result is recorded in
  `decisions.md`. A missing/empty path is surfaced to the human before proceeding (fix the
  config, or record a named degraded-review acceptance in `decisions.md`) — a reviewer handed
  dead paths silently degrades to docs-only reasoning, the loop's founding failure.
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

**`decisions.md` — the gate log (append-only).** Each gate (4, 7, 8) appends one entry:
which gate, the worst finding's severity, the route taken, and — for any **human override**
(accepting a major/regression, breaking an iteration-cap tie) — a one-line rationale with a
name. A clean pass-through is a single line. This is not just audit: the **iteration cap
depends on it** — counting "2 bounces at the same gate" and carrying prior findings forward
requires the bounce history to persist. Human acceptance of a known regression is the entry
that matters most ("why did we ship this?" gets a recorded answer). At stage 8, the entry also
records each **gating** criterion's disposition (verified / named risk-accepted) — a gating
criterion may not pass through stage 8 absent from this log.

Together these double as the audit trail and as context for reconstructing the work if lost.

---

## Human-in-the-loop

The skill executes stages 1–7 autonomously (reason, spawn cold reviewers, write docs, edit
code) and runs stage 8 if the config provides the check. It **stops for a human decision** at:
- any **blocker** (the loop is about to restart — confirm direction first),
- any **major** at stage 8 (regression-vs-tradeoff is a judgment call),
- a **gating criterion that cannot be verified pre-ship** (the loop must build a representative
  harness or obtain named risk-acceptance — never defer it silently),
- **missing criteria or config** needed to proceed (it refuses rather than guesses).

Everything else it routes automatically per the severity model, reporting what it did.
