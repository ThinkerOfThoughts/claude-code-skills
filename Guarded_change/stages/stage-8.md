# Stage 8 — Harness

**What this stage does:** measure actual behavior, then check conformance (always) and
regression (if a baseline exists), and route by severity. "Done" is proven here, not declared.

## Procedure

Run the config's `measurement.check`, then apply the rules below: **conformance (always)** and
**regression (only if a stage-0 baseline exists)**, emitting the per-criterion verification
table, re-checking the frozen criteria, and writing `8-harness.md` with a verdict routed by
severity (blocker → 1; major → human call; minor → fix, proceed; clean → done).

## The two checks + per-criterion verification duties

**Conformance (absolute, always runs) — H1.** Measured behavior vs. the acceptance criteria
(1.5). *Did it do what we said it should?* Works for brand-new code because it needs no prior
version.

**Regression (relative, only if a stage-0 baseline exists) — H2.** Measured behavior vs. the
pre-change baseline, on everything *other* than the new behavior. *Did we break a neighbor?* A
net-new feature still gets **both**, aimed differently: conformance on the feature, regression
on the surrounding system that already existed. A truly greenfield project (no prior version of
anything) runs conformance-only.

**Position-dependent criteria must be checked by execution, not inspection — H3 (fires only for
a criterion written under the position lens at stage 1.5).** Any such criterion is satisfied
only by **running its isolating case and observing the behavior occur** — never by re-reading
the assembled prompt/config to confirm the text is present. Text-presence is the exact check
that the position change defeats, so a harness that "verifies" such a criterion by inspection
has not run it. This is the cheapest reliable catch for the whole class and is why the criterion
is mandated up front: stage 3 reasons about it, but only stage 8 can prove it fired.

**Concurrency criteria must be checked by executing an interleaving, not by inspecting the
guard — H4 (fires only for a criterion written under the concurrency lens at stage 1.5).** Any
such criterion is satisfied only by **running a concurrent interleaving and observing the write
survive** — never by re-reading the lock/transaction code and reasoning it looks sufficient.
Inspecting the guard is the exact check the scope gap defeats: the guard *is* correct for the
accessors it covers. Prefer a deterministic harness that injects the competing mutation into the
read→write window (a live thread race need not be reproduced by luck); a pure-inspection
"verification" of such a criterion counts as `verified = no`.

**Every gating criterion must be verified by execution before "done" — no deferral, no proxy,
no silent drop — H5.** A gating criterion (1.5) is satisfied only by running a case that
exercises *the actual path it governs* and observing the required behavior. Three dispositions
that look like progress but are **not** satisfaction — each shipped a real regression in
practice:
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

**An unreviewed check is not a check — H6.** Any new or modified executable check whose results
stage 8 will trust, created after the stage-6 review (the harness itself, a route-(a)
representative fixture, a rebuilt probe), gets a **targeted cold check before its results
count** — for representativeness, and, where the check guards a fix, that it fails against the
unguarded version; until then its results are `verified = no`. A defective check found this way
is discarded and rebuilt in place (logged in `decisions.md`), not a loop restart; findings it
raises about the change itself route via the gate-8 severity row. In-place fix diffs at gates
7/8 are recorded in `decisions.md`, and a stage-8 fix-in-place re-runs the criterion checks its
diff could have invalidated.

**Per-criterion verification table — H7.** `8-harness.md` **must contain a per-criterion
verification table**: one row per criterion with columns *criterion │ gating/advisory │ path
exercised │ verified by execution? │ evidence │ result*. The **evidence** cell of every gating
`verified = yes` row cites where the raw output lives (the command run + an output file/excerpt);
for a human-judged-rubric criterion the pointer is the named judge + where the verdict is
recorded. A gating PASS row with no evidence pointer counts as `verified = no`, and the
consumer's citation spot-verify extends to a sample of evidence cells. Any **gating** row that
is not `verified = yes` blocks "done" unless `decisions.md` carries the matching named
risk-acceptance. (Inspection-only "verification" of a gating criterion counts as `verified =
no`.) The table always lists every **gating** criterion; advisory criteria may be summarized in
one line. A run with no gating criteria says so and the table is trivially short — the artifact
scales to the change, not the reverse. For a probabilistic or human-judged-rubric criterion
(see stage 1.5), the "verified" cell records the observed pass-rate over the stated number of
runs (or the named judge's verdict), not a bare yes/no — reusing the rubric the criterion
already declared.

**Regression must be measured on a comparable workload, or it is advisory only — H8.** Global
aggregate metrics (mean cost, mean tool-calls) computed over whatever happened to run will move
whenever the *new behavior* legitimately exercises the system more — producing a **false
regression** indistinguishable from a real one. A regression metric is only **gating** if either
(a) it's measured on a fixed/replayed held workload comparable to the baseline's, or (b) the new
behavior can be excluded from the aggregate. A metric that can't isolate the change's own
contribution is reported as **advisory** (surfaced, not auto-bouncing). The plan (stage 2) names
which metrics are gating vs. advisory and how the comparable workload is obtained.

**Spot-verify the citations themselves (CH6, consumer duty at stage 8).** Whoever consumes the
review checks a sample of the cited file:lines / log rows actually exist and say what's claimed;
at stage 8 this spot-verify extends to a sample of the verification table's evidence cells.
Citations are the one guard defending the loop's founding failure; a fabricated citation would
defeat it, so the guard itself must be spot-checked (cheap: verify a few, not all).

## Core principles + freeze + severity + gate log this stage enforces

**A bar, set first (CP4).** "Done" is defined as measurable acceptance criteria *before*
implementation, so completion is verified, not declared.

**A deferred gating criterion is not a met one (CP5).** "Done" requires every *gating* acceptance
criterion (1.5) to be **empirically verified first**, by exercising the path it governs. A
gating criterion that is postponed to "live/production," satisfied by a *proxy* that avoids that
path (a mocked dependency, a disabled flag, an input class that never triggers it), or quietly
dropped from the results, has **not** been met — deferral silently converts *proven* done into
*hoped* done. Advisory criteria may be deferred; gating ones may not.

**Information-preserving is not behavior-preserving (CP6, position lens; fires only in a
position-sensitive assembly).** In a position-sensitive assembly a change can keep every piece
of content and still change behavior, when an element's effect depends on its *position* rather
than its mere presence (recency, precedence, "before/after some input," adjacency). A check that
only asks "is every piece still present?" passes such a change blind: the content survives, the
behavior does not. (The stage-8 operative form is H3 — position-dependent criteria checked by
execution; the full lens statement is in `stages/charter.md` / stage 1.5.)

**Shared state has more than one accessor (CP7, concurrency lens; fires only where the change
alters concurrency structure over shared state).** When a change introduces a new unsynchronized
accessor, or a new read→slow-work→write window, over shared mutable state whose atomicity an
existing transaction/lock does not already enforce, correctness depends on *every* accessor of
that state, not just the one being written. A guard is only as strong as its **scope** — a
lock-free accessor whose write interleaves in the gap is silently lost. (The stage-8 operative
form is H4 — concurrency criteria checked by executed interleaving; the full lens statement is
in `stages/charter.md` / stage 1.5.)

**Criteria freeze — stage 8 verifies unchanged (FRZ).** Stage 8 verifies `1.5-criteria.md`
still matches the version whose hash was recorded in `decisions.md` at gate 4; a divergence is a
post-freeze edit → the affected criteria's PASSes are invalid unless the edit carries a
`decisions.md` entry (change + reason) and a targeted re-red-team of the edited criteria. Any
**weakening** (gating→advisory, a loosened threshold, a narrowed scope) is audited exactly like
an advisory relabel under the charter's label-audit — it needs a legitimate reason or the
original stands.

**Severity model and gate routing (SEV1).**

| Severity | Meaning | Stage 4 (plan) | Stage 7 (code) | Stage 8 (harness) |
|---|---|---|---|---|
| **Blocker** | wrong problem / will not work / unverifiable | → 1 | → 5 | → 1 |
| **Major** | sound goal, materially wrong approach | → 2 | → 5 | → 1 or 2 (human call) |
| **Minor** | real but local; fixable in place | fix → proceed | fix → proceed | fix → proceed |
| **Nitpick** | style/clarity; optional | log → proceed | log → proceed | log → proceed |

**Borderline/tradeoff is a human decision (SEV2).** The severity threshold is what stops the
loop from thrashing on marginal findings. A borderline regression that's an acceptable tradeoff
is a **human decision**, not an automatic restart — the loop surfaces it ranked; a person
rules.

**The reviewer's severity routes (SEV3).** For findings originating from a cold review (gates 4
and 7; at stage 8, findings from a targeted post-6 check), the gate routes on the **reviewer's**
stated severity — harness measurements at stage 8 route by the table as before. The author may
contest a severity only via a logged `decisions.md` entry; demoting a **blocker or major**
additionally requires the human tie-break (the same authority that breaks iteration-cap ties).
A silent unilateral demotion is a gate violation: the reviewer's routing stands.

**Iteration cap (anti-livelock) (SEV4).** A blocker/major that routes *backward* is bounded:
after **2 bounces at the same gate on the same finding class**, the loop **stops and a human
breaks the tie** (accept the risk, change the goal, or kill the change). **"Same finding class"
= same gate (by stage number) + same targeted artifact section, regardless of wording** — so a
rephrased objection, or the *same kind* of defect resurfacing in a nearby spot (e.g. "this
metric isn't measurable from the logs" raised against a different metric field), still counts
toward the cap. This prevents livelock-by-rephrasing, where each lap nominally raises a
"different" finding that is really the same unresolved disagreement. Each backward route
carries the prior review's findings forward (via `decisions.md`) so the next reviewer confirms
they were addressed rather than re-deriving. Without this, a hard disagreement can cycle
1→3→1→3 (or 5→7→5→7) indefinitely, paying full review cost each lap.

**`decisions.md` — the gate log, append-only (ART3).** Each gate (4, 7, 8) appends one entry:
which gate, the worst finding's severity, the route taken, and — for any **human override** — a
one-line rationale with a name. This is not just audit: the **iteration cap depends on it**. At
stage 8, the entry also records each **gating** criterion's disposition (verified / named
risk-accepted) — a gating criterion may not pass through stage 8 absent from this log.

## Stop for a human (HIL / SK-STOP)

The skill **stops for a human decision** at: **any major at stage 8** (regression-vs-tradeoff is
a judgment call); a **gating criterion that cannot be verified pre-ship** (build a representative
harness or obtain named risk-acceptance — never defer it silently); **any blocker** about to
restart the loop (confirm direction first); and **missing criteria or config** needed to
proceed. Refuse to guess project metrics or acceptance criteria — that's the exact failure this
loop exists to prevent.
