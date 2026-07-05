# Stage 4 — Gate (plan)

**What this stage does:** route the loop by the stage-3 reviewer's worst finding, freeze the
criteria on the way to build, and record the gate decision.

## Procedure

Route by worst finding: **blocker → return to 1** (confirm direction first); **major → return
to 2**; **minor → fix in place, proceed**; **nitpick → log, proceed**; **clean → build (5).**
Bounded by the iteration cap (below). Route on the **reviewer's** severities — contest only via
a logged entry; demoting a blocker/major needs the human tie-break. On route-to-build:
**freeze `1.5-criteria.md`** and record its sha256 (or a verbatim copy) in `decisions.md`. Gate
4 may not pass until the run-start path-validation result is recorded in `decisions.md`.

## Severity model and gate routing (SEV1)

| Severity | Meaning | Stage 4 (plan) | Stage 7 (code) | Stage 8 (harness) |
|---|---|---|---|---|
| **Blocker** | wrong problem / will not work / unverifiable | → 1 | → 5 | → 1 |
| **Major** | sound goal, materially wrong approach | → 2 | → 5 | → 1 or 2 (human call) |
| **Minor** | real but local; fixable in place | fix → proceed | fix → proceed | fix → proceed |
| **Nitpick** | style/clarity; optional | log → proceed | log → proceed | log → proceed |

**Gates route by the worst finding's severity (GATE).**

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

## Other rules governing this gate

**Criteria freeze (FRZ).** When gate 4 routes to build, `1.5-criteria.md` **freezes** and its
hash (or a verbatim copy) is recorded in `decisions.md`. The freeze binds to the route-to-build
version, which must equal the version the stage-3 reviewer read — except for gate-4 in-place
fixes, each traceable to a logged finding, with the criteria diff recorded in `decisions.md`.
Stage 8 verifies the file still matches the recorded version; a divergence is a post-freeze
edit → the affected criteria's PASSes are invalid unless the edit carries a `decisions.md`
entry (change + reason) and a targeted re-red-team of the edited criteria. Any **weakening**
(gating→advisory, a loosened threshold, a narrowed scope) is audited exactly like an advisory
relabel under the charter's label-audit — it needs a legitimate reason or the original stands.

**Paths are validated, not assumed — blocks gate 4 (CFG3).** Mechanically check every path
handed to a cold reviewer (`redteam_context`, the spec's touched files, fixture paths) exists
and is readable — at run start for paths that exist then, and at each cold-reviewer spawn for
any path not yet validated. Gate 4 may not pass until the run-start validation result is
recorded in `decisions.md`. A missing/empty path is surfaced to the human before proceeding
(fix the config, or record a named degraded-review acceptance in `decisions.md`) — a reviewer
handed dead paths silently degrades to docs-only reasoning, the loop's founding failure.

**`decisions.md` — the gate log, append-only (ART3).** Each gate (4, 7, 8) appends one entry:
which gate, the worst finding's severity, the route taken, and — for any **human override**
(accepting a major/regression, breaking an iteration-cap tie) — a one-line rationale with a
name. A clean pass-through is a single line. This is not just audit: the **iteration cap
depends on it** — counting "2 bounces at the same gate" and carrying prior findings forward
requires the bounce history to persist. Human acceptance of a known regression is the entry
that matters most ("why did we ship this?" gets a recorded answer).

## Stop for a human at this gate (HIL / SK-STOP)

The skill **stops for a human decision** at: **any blocker** (the loop is about to restart —
confirm direction first); **missing criteria or config** needed to proceed (it refuses rather
than guesses); and the iteration-cap / blocker-major-demotion tie-breaks above. Everything else
it routes automatically per the severity model, reporting what it did.
