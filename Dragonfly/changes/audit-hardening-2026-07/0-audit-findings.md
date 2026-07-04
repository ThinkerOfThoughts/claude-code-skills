# Audit findings — dragonfly (2026-07-03, Fable 5 audit)

Input to a guarded-change run on the dragonfly skill. Sources: full read of `SKILL.md` +
`METHODOLOGY.md` + `dragonfly.companion.md` + the `changes/gate-before-present/` record, and —
critically — the skill's real-world performance record: the monologue-bleed/memory-gap hunt
(`~/Desktop/companion-emergence/hunts/monologue-bleed-memory-gap/{decisions,hypotheses}.md`),
where the loop's gates correctly killed two confident hypotheses (H-S1-DISTANCE,
H-S1-FILEBLOAT) but several situations had to be handled ad hoc because the skill has no rule
for them. Constraints (owner, 2026-07-03): **additive fixes only** (structural flagged, not
built); the executing model is **Opus** — rules must be explicit, mechanical, checkable; don't
bloat. Dependency note: D-1/D-9/D-11 assume the guarded-change `audit-hardening-2026-07`
amendments (provenance rule, evidence column, etc.) are accepted — dragonfly inherits its
charter/severity by reference.

## Ranked findings (additive fixes proposed)

**D-1 — Cold-pass provenance is not required for dragonfly's own passes.** Dragonfly reuses
guarded-change's charter by reference, but nothing says its stage-7 causal-chain red-team or
its triage/lite passes must keep the verbatim record guarded-change now mandates (charter
given, context list, verbatim output, agent type/model, reviewer-reported context hashes).
The hunt's records summarize reviews (e.g. "O18: 6/6 citations verified") — author-summarized,
the exact channel guarded-change F1 just closed. Fix: one sentence in the charter section —
the provenance rule applies to **every dragonfly cold pass** (stage 1/4 via triage, stage 7
direct), recorded in the hunt folder.

**D-2 — No terminal state between "found" and "escalate."** Stage 7's bar is all-or-nothing;
the real hunt ended S1 honestly as "characterization + mitigation directions, not found"
(decisions.md S1 stage-7 entry) — an outcome the methodology neither names nor bounds, so it
was improvised. Undefined honest-partial outcomes invite dishonest ones (a stalled hunt
quietly re-badged as "characterized"). Fix: define **"characterized, not found"** as a legal
stage-8 verdict requiring: (a) what is established, each claim cited and cold-red-teamed like
any conclusion; (b) which hypotheses were refuted (with their evidence); (c) WHY the full bar
is unreachable (model property, cost bound, needs-live-data — named, not vague); (d) explicit
human sign-off; (e) presentation tier stays "characterization" — never "the cause." Handoff
may carry mitigation directions, marked as such.

**D-3 — The convergence gate's "cycle" is undefined.** "After N cycles with no hypothesis
eliminated" (METHODOLOGY stage 6) never defines a cycle, so the cap can't be counted
mechanically — Opus needs a countable unit. Fix: one sentence — a cycle = one discriminating
test **run and recorded** (a completed stage-4→5 lap); the count and the per-area
re-examination tally live in `decisions.md` at each stage-6 pass (the gate is checkable from
the log, like guarded-change's bounce cap).

**D-4 — The symptom detector/readout is an ungoverned artifact.** The representativeness gate
governs repros/tests, but the *detector* that decides "the symptom occurred" (a bleed
detector, a log classifier, a grep) is itself authored code whose false verdict poisons
everything — the hunt had to invent a "detector must flag the real incident first" gate ad
hoc (s1-repro-spec, 2026-07-02). Fix: name the detector/readout explicitly as a diagnostic
artifact — triage applies, AND its validation is part of the representativeness gate: it must
be shown to fire on a known-true instance (and stay silent on a known-clean one), evidenced
by an observation-ledger row, before any reading it produces is consumed.

**D-5 — "Predictably" is unquantified for intermittent symptoms.** The stage-7 toggle and
stage-9 verification assume flip → symptom appears/disappears; for rate-based symptoms (the
common hard case — bleed is one) a single flip proves nothing, and 9b "user confirms
resolved" over an unstated window is unfalsifiable. Fix: for a probabilistic symptom, the
toggle criterion states the expected rate shift and run count (borrow guarded-change's
probabilistic rubric verbatim-by-reference), and 9a/9b define their observation window up
front from the symptom's observed frequency in the ledger (e.g. "occurred ~1/session over 5
sessions → 9b window ≥ N sessions, pass = 0 occurrences").

**D-6 — Config is never validated, and cross-machine adaptation is unruled.** The repo config
was macOS/Hana-specific; this box's hunt adapted it ad hoc (logged, laudably) — but no rule
required validating paths or logging the adaptation. Same class as guarded-change F8. Fix:
at hunt start, mechanically check every config path (`redteam_context`, `reproduction.logs`,
`ledgers.dir`) exists/readable; an invalid-for-this-machine config → the adaptation is itself
a `decisions.md` entry (what changed, why) before stage 0 proceeds; dead paths surface to the
human.

**D-7 — Multi-symptom hunts break the convergence accounting.** The loop is written
single-bug; the real hunt ran S1+S2 in one folder (user's call, worked) — but stage 6 counts
"cycles with no hypothesis eliminated" globally, so progress on S2 can mask S1 thrash. Fix:
when a hunt carries multiple `S#` threads, the convergence count is **per-thread**; a thread
hitting the cap escalates alone. One sentence, plus: symptom threads may be split into
separate hunts at any gate with a recorded reason.

**D-8 — The repro-before-hypotheses ordering gets silently inverted in practice.** Stage 1
demands a repro "BEFORE hypothesizing," but for intermittent/emergent bugs the repro *design*
needs mechanism candidates (the real S1 formed hypotheses first out of necessity; the skill
gave no legal route, so the ordering rule was just... not followed). An always-violated rule
teaches rule-skipping. Fix: an explicit escape — when a faithful repro cannot be built
blind (intermittent, load-dependent, emergent), hypotheses MAY be formed first to inform
repro/instrument design, PROVIDED the inversion is recorded in `decisions.md` and every such
hypothesis stays `ungated` (presentation tiers already enforce the rest); the
representativeness gate still binds the resulting repro before any conclusion.

**D-9 — Lite passes leave no auditable record.** guarded-change-lite is "a single cold
red-team pass … → fix → run" with no named artifact; the hunt's lite passes exist only as
gate-log one-liners. Fix: a lite pass records, minimally: the artifact reviewed, the one-line
intent + criterion, the reviewer's verdict + where its verbatim output lives (per D-1), in
`decisions.md`. Two sentences in the triage section.

**D-10 — Self-check is weaker than guarded-change's, and its flagship test has never run.**
The self-check section (a) doesn't declare skill files a position-sensitive assembly or
require the full loop for non-trivial edits (guarded-change F9 parity), and (b) names a
behavioral no-Dragonfly-baseline fixture test "the test that matters most" — which has never
been executed; an unrun flagship check is exactly the deferred-gating shape the sibling skill
forbids. Fix: (a) mirror guarded-change's strengthened self-check (full loop; standing
criteria: live==source, SKILL↔METHODOLOGY consistency, behavior-preservation on move/remove,
PLUS: every cross-reference into guarded-change still resolves — see D-11); (b) label the
baseline test honestly as **aspirational/not yet run** where it is described, until someone
runs it once (then it becomes a replayable standing probe).

**D-11 — The by-reference coupling to guarded-change is load-bearing and unchecked.**
Dragonfly imports its charter, severity model, and lite definition from guarded-change "as
that hardens" — by design. But nothing verifies the referenced sections still exist/say what
dragonfly assumes after a guarded-change edit (today's hardening added charter bullets — e.g.
provenance now flows in silently, which is desirable but unexamined; a future rename could
sever a reference silently). Fix: a standing self-check criterion (in D-10's list): each
named cross-reference (charter section, severity model, probabilistic rubric) is checked to
resolve after any edit to EITHER skill; plus one sentence in the charter section stating
which inherited bullets bind dragonfly's passes (all unconditional discipline bullets incl.
provenance; the stage-3 coverage-challenge bullet does not apply — dragonfly's analog is D-12).

**D-12 — Nobody challenges the hypothesis-space itself.** Both refuted S1 hypotheses died on
the SAME false architectural assumption (the Python tool-loop mattering on the claude-cli
path) — a shared blind spot no gate was charged with finding; the cold passes each attacked
one hypothesis's chain, never the set. Fix: one charter aim for dragonfly cold passes + one
stage-6 duty — at the convergence gate, record: which mechanism **classes** the live
hypotheses cover, which have been ruled out, and **what assumption the live set shares** (an
explicit "none identified" counts); a cold pass that finds the shared assumption false ranks
it by impact. This is the diagnosis-side sibling of guarded-change's new criteria-coverage
challenge.

**D-13 — The stage-7 bar is satisfiable at a proximate node ("explains the symptom" ≠ "is
the root").** Reproduce-on-demand + chain + toggle can all pass at an intermediate link:
toggling file I/O moves the degradation, so "degradation ← context bloat ← file read/write"
counts as found while the mechanism below (what specifically accumulates, why the budget
doesn't bound it, which op contributes what) stays unexplored — and the fix then targets the
relay, not the root. Precedent (user-observed, context-bloat hunt): Opus was prepared to
accept the bloat-from-file-R/W account and proceed. The methodology says causality runs
root→symptom but never defines when the *root* is reached vs. an intermediate link. Fix: a
**depth check** at stage 7 — the root cause, for dragonfly's purposes, is the **deepest node
the project can act on**. For the claimed root, ask "why does this node produce the next?"
one level further down; declaring "found" requires recording that the next why-down is
(a) answered with cited evidence, (b) explicitly out of scope (model property / third-party
code / not actionable — named, not vague), or (c) not load-bearing for a fix that targets the
cause rather than the mechanism's surface. The stage-7 cold pass explicitly challenges "root
or relay?", and `diagnosis.md` states the chain with each level's status.

**D-14 — "Found" never checks the cause against the full evidence ledger; secondary
contributors get silently absorbed.** The confirmed cause is validated against the repro and
toggle, not against everything observed: ledger rows that predate or fall outside the
confirmed mechanism can remain unexplained with no record. Precedent (user-observed): the
degradation existed on the pre-0.0.38 direct-edit path too (S1-O15) — the 0.0.38-only story
didn't cover it, it was overlooked as "not the primary cause", and the unified dose-dependent
account only emerged on the user's push. Fix: an **evidence-coverage sweep** at stage 7,
before "found": walk the observation-ledger rows tied to the `S#`; each is either explained
by the confirmed chain (cite how) or recorded as a **residual** — a named secondary
contributor / open sub-hypothesis, ranked, carried in `diagnosis.md` and the stage-8 handoff,
and struck only with a recorded reason (same discipline as symptoms). "Found (primary), with
named residuals" is a legal verdict; silent absorption is not. Stage-9 verification re-checks
the residuals list — a fix that kills the primary does not close an unexplained residual.
(D-13 and D-14 are the diagnosis-side siblings of guarded-change's new criteria-coverage
challenge: one guards depth, the other completeness.)

## Flagged structural (NOT built — owner sign-off, separate runs)

**D-S1 — Attention budget.** 441+129 lines and growing; same ceiling argument as
guarded-change S1. The additive fixes above are written terse; a checklist-first restructure
is a future owner decision.

**D-S2 — Unversioned coupling.** The by-reference inheritance from guarded-change is
deliberate and good, but unversioned: guarded-change edits change dragonfly's behavior with
no dragonfly-side review. D-11 adds detection; a structural fix (pinning, or a shared
"charter core" file both import) is a bigger design call.

**D-S3 — The 0a confirmation checkpoint has no timeout/async path.** Stop-for-human at 0a is
right, but in autonomous/overnight contexts the hunt just halts. Possible future: a
provisional-freeze mode (proceed on the restatement, marked unconfirmed; re-confirm at first
human contact). Needs owner judgment on risk — not built.
