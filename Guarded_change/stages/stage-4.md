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

**Run-level cap: rounds-without-a-run (anti-proliferation) + in-flight tripwires (SEV5).** SEV4
counts *repetition* (the same finding class recycled) and is structurally blind to *proliferation*
— a run in which every round raises a genuinely **new** class, so the per-class counter resets to 1
each lap and never reaches 2, while the artifact is never once executed. To catch it, maintain a
**second, run-level counter**, blind to finding class and **not reset per gate** (it persists across
gates 4/7/8 for the whole run): increment it on each **backward route (a
bounce)** taken **while the artifact has not yet been executed against an external oracle** (stage-8
conformance not yet reached or not reachable). It does **not** increment on a forward lap — a clean
run that walks 1→8 without bouncing accrues zero — which is why it fires on proliferation without
false-stopping healthy runs. After **2 such rounds-without-a-run**, the loop **stops and a human
breaks the tie** — the same stop-for-human consequence as SEV4 — and the human chooses: **widen the
unit** until it is runnable, **declare it untestable-in-isolation** and defer verification to a run
of the assembled system, or accept/kill. (On the case that motivated this — a fragment taken through
six backward bounces and never run — it fires entering round 3.) The count is read from
`decisions.md` (ART3), like SEV4's. Once the artifact has been executed once, SEV5 stops accruing
(the never-run trap is escaped; later cycling is guarded by SEV4 and the stage-8 major→human-call,
not SEV5). A **BT-dissolve that routes forward** (to build) is not a backward route and does **not**
increment SEV5; a BT-dissolve that still routes backward counts (toward SEV4, and SEV5 while no run
has happened). This is the runtime backstop to stage 1's **RTS** refuse-to-start check
(`stages/stage-1.md`), which asks the same question at design time.

**In-flight tripwires (watch each lap; act before the hard cap).** Earlier-warning signs that a run
is sliding into the proliferation trap: **(a) rounds-without-a-run climbing** (the counter above);
**(b) growth against a fixed design** — the artifact keeps growing across rounds while the design it
implements has not changed; **(c) target-drift in findings** — successive findings migrate from
*"does it work?"* (conformance) toward *"could it be defeated?"* (adversarial fine-grain), the
signature of a fragment graded against itself; **(d) a fragment with no consumer yet** — the unit
under change is a piece of a larger runnable thing with nothing assembled to execute it. When any
tripwire shows, **re-ask the RTS question now** — *what will I execute, and what tells me it
worked?* — and widen or escalate rather than taking another lap; do not wait for the hard cap.

## Other rules governing this gate

**An escalated fidelity finding resolves only on a passing ratification audit (RAT1/RAT2).** A
prior "OWNER MUST RATIFY" finding counts as **resolved** for routing **only if** its ratification
record passes the stage-3 audit — CH11 (the selection maps to the owner's verbatim words,
spot-checked against their cited source, on the flagged axis) and CH12 (the elaboration adds no
unratified operative commitment). If the record is absent, cites no verbatim owner selection or
no durable source for it, rests on a **partial or adjacent** answer, or the elaboration inflates
beyond the ratified option, the finding **stands at its escalated severity** and the loop **stops
for the human to re-ask** the unresolved axis — it is never cleared by the presence of an "OWNER
RULING" line alone. This is the fidelity sibling of *the reviewer's severity routes*: an author
cannot self-clear an escalated fidelity finding by recording their own reading of owner intent.
The recorded ratification is created *after* the stage-3 escalation, between review and build; the
purpose of this gate is to force that ruling back through a **cold audit** rather than let it
reach build **self-certified** — the exact CP1 failure this loop exists to prevent, in the one
place the loop otherwise had no gate. (It is not adding detection the fidelity lens lacks — it is
making the review of the ratification happen at all.) (Interaction with the iteration cap: a
re-ask is already a stop-for-human, so no livelock; if a *second* owner answer is again
non-disambiguating, the cap's human tie-break applies — the correct outcome, not a guard
failure.) Full statement in `stages/stage-3.md` (RAT1/RAT2).

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

**Blocker triage: intrinsic vs self-manufactured — before escalating or re-bouncing (BT).**
Before this gate escalates a **blocker** to the human (stop-for-human, below) **or** routes a
finding *backward* to bounce the same axis again, first triage the blocker: is it **intrinsic to
the problem**, or an **artifact of the runner's own design/implementation choice**? A
**self-manufactured constraint** is a dilemma an incidental design decision created — **dissolvable
by *changing that decision***, not by an owner ruling or another review lap. When a blocker looks
owner-bound, or a finding keeps re-bouncing on the same axis, challenge *"is this inherent to the
problem, or did our own design build it in?"* and try to **dissolve it by revisiting the runner's
own architectural choices before escalating.** Only a blocker that survives this triage — one no
design change of ours dissolves — is a genuine owner-decision (or a genuine iteration-cap
tie-break). **Record the triage outcome in `decisions.md`** (intrinsic → escalated │
self-manufactured → dissolved, naming the design change │ self-manufactured → escalated-anyway, with
the reason it could not be dissolved) — like any override under ART3, so the triage is auditable and
cannot be silently skipped or used to talk a genuine owner-decision out of its stop. This is the
sibling of the *measurement-apparatus* discipline (stop elaborating your own artifact) applied to
the escalation/bounce decision: an escalation or a repeat bounce spent on a constraint *we built* is
the same wasted elaboration one level up. The triage **precedes** the iteration cap and the
stop-for-human and does **not** replace them — a blocker that survives it still escalates, and the
cap still bounds genuine disagreement. And the triage is itself **bounded by the iteration cap**: a
*repeated* self-manufactured-triage-dissolve on the **same axis** counts toward SEV4's "same finding
class" exactly as a re-bounce does — dissolving and retrying is not a free loop, so a runner cannot
livelock by "discovering" a fresh self-manufactured constraint each lap. *(Example: a
candidate-memory queue implemented as a state-column inside the main DB manufactured a "what happens
to a gate-rejected candidate?" values-question that bounced three cold-review rounds and was
escalated to the owner — the owner's separate-store architecture dissolved it entirely; a rejected
candidate is just a discarded queue entry.)*

## Stop for a human at this gate (HIL / SK-STOP)

The skill **stops for a human decision** at: **any blocker** (the loop is about to restart —
confirm direction first); **missing criteria or config** needed to proceed (it refuses rather
than guesses); a **non-disambiguating owner answer** to an escalated fidelity finding (re-ask the
flagged axis, never resolve the answer into a recommended option — RAT1); and the iteration-cap /
blocker-major-demotion tie-breaks above. The **rounds-without-a-run cap (SEV5)** — 2 backward routes
taken while the artifact has never been executed — likewise stops here. Everything else it routes
automatically per the severity model, reporting what it did.
