# Stage 7 — Gate (code)

**What this stage does:** route the loop by the stage-6 reviewer's worst finding, and record
the gate decision. (Stages 1–7 run autonomously; a blocker here routes to build, not a human
restart.)

## Procedure

Route by worst finding: **blocker/major → return to build (5)**; **minor → fix in place,
proceed**; **nitpick → log, proceed**; **clean → harness (8).** Route on the reviewer's
severities (as at gate 4); record any in-place fix diff in `decisions.md`. Bounded by the
iteration cap (below).

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

**`decisions.md` — the gate log, append-only (ART3).** Each gate (4, 7, 8) appends one entry:
which gate, the worst finding's severity, the route taken, and — for any **human override**
(accepting a major/regression, breaking an iteration-cap tie) — a one-line rationale with a
name. A clean pass-through is a single line. This is not just audit: the **iteration cap
depends on it** — counting "2 bounces at the same gate" and carrying prior findings forward
requires the bounce history to persist. Human acceptance of a known regression is the entry
that matters most ("why did we ship this?" gets a recorded answer).
