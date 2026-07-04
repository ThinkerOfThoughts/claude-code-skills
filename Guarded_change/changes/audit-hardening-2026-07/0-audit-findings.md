# Audit findings — guarded-change (2026-07-03, Fable 5 audit)

Input to this guarded-change run. A full cold read of `SKILL.md` + `METHODOLOGY.md` +
`guarded-change.companion.md` + the `changes/` records (concurrency-lens, and the
gating-enforcement + position-sensitivity records via the memory lessons), hunting for
loopholes, over/under-specified rules, and structural weaknesses. Constraint from the user:
**additive fixes only** (structural rework is flagged, not built), and the skill runs on
**Opus** — rules must be explicit, mechanical, and checkable, not judgment-dependent, and must
not materially bloat the documents.

The meta-pattern of every past shipped miss: *a check existed but was not actually exercised,
or was exercised on the wrong thing, by an actor whose blind spot it shared.* The findings
below are the remaining unguarded channels of that same shape.

---

## Ranked findings (additive fixes proposed)

**F1 — Review provenance is unaudited (prompt-rigging / context-starving / summary-drop).**
The author of the artifact under review also (a) authors the cold reviewer's prompt, (b)
selects what context it gets, and (c) transcribes its findings into the stage doc. All three
channels can neuter independence while looking procedurally compliant — a softened charter, a
starved (or answer-leaking) context set, or findings dropped in summarization leave no trace.
Precedent: the concurrency-lens C3 attempt-1 confound — an author-authored "helpful context"
note leaked the guard's own work product to both arms and invalidated the harness; it was
caught only by author honesty, not by any rule. Fix: stage-3/6 docs must embed (i) the
verbatim charter/prompt given, (ii) the exact context paths given, (iii) the reviewer's
verbatim output (author summary goes in decisions.md, separate). The charter given must be the
METHODOLOGY charter text, not a paraphrase. Reviewer input is closed-set: the named stage
artifacts + config `redteam_context` + carried-forward findings from `decisions.md`; any
author-authored supplementary context beyond that must be flagged as such in the stage doc
(visible to the next gate), and is prohibited outright inside A/B harness arms (leak = confound).

**F2 — Post-review artifacts are trusted un-reviewed (the trust-before-gate gap).**
Anything created or modified *after* stage 6 reaches "done" with zero independent eyes: the
stage-8 harness itself, a route-(a) "representative pre-ship harness" built at stage-8 time,
and in-place minor fixes at gates 7/8. The charter's representativeness challenge lives at
stage 6 — it cannot fire on a harness that does not exist yet. Precedent: C3 attempt-1 (a
defective harness produced a confounded result); the Option-B smoke (a non-representative
harness "verified" a gating criterion). Fix: any *new or modified executable check* whose
results stage 8 will trust, if it did not exist at stage-6 review time, gets a targeted cold
check (representativeness + does-it-fail-on-the-unguarded-version where applicable) before its
results count; in-place fix diffs at gates 7/8 are recorded in `decisions.md`; a stage-8
fix-in-place re-runs the criteria checks its diff could have invalidated.

**F3 — Stage-8 PASS claims are exempt from the evidence discipline.**
"Cite or it doesn't count" binds reviewer findings, but the author's own PASS verdicts in the
verification table need no evidence pointer — a table can assert `verified = yes` with nothing
behind it, and nothing requires raw harness output to be preserved. Fix: the per-criterion
table gains an **evidence** column: each gating `verified = yes` row cites where the raw output
lives (command + output file/transcript location, or inline excerpt). A gating PASS row with no
evidence pointer counts as `verified = no`. (Extends the existing citation spot-check: the
consumer spot-verifies a sample of evidence pointers too.)

**F4 — Criteria are mutable after the gate that approved them (goalpost-moving).**
Nothing freezes `1.5-criteria.md` once stage 4 passes. A criterion can be quietly reworded,
loosened, or relabeled when it becomes inconvenient at build/harness time, and stage 8 then
verifies against the moved goalposts. Fix: after a clean/proceed gate 4, `1.5-criteria.md` is
frozen; any edit requires a `decisions.md` entry naming the change + reason, and the edited
criteria get a targeted re-red-team. Any *weakening* (gating→advisory, threshold loosened,
scope narrowed) is treated exactly like an advisory relabel under the existing label-audit —
it must carry a legitimate reason and survives challenge or the original stands.

**F5 — Severity is assigned by the reviewer but routed by the author, and demotion is silent.**
The gates route "by worst finding," but the author interprets the review and writes the
severity into `decisions.md` — a blocker/major can be silently demoted to "minor, fixed in
place" and no rule notices. Fix: routing severity is the *reviewer's* stated severity. The
author may contest a severity only via a logged `decisions.md` entry stating the disagreement;
demoting a **blocker or major** additionally requires the human tie-break (same authority that
breaks iteration-cap ties) — never a silent unilateral demotion. (Upgrading severity or
accepting the reviewer's word needs no ceremony.)

**F6 — The reviewer's context set can miss the change's own files.**
`redteam_context` is standing per-project config; a change touching files outside those
entrypoints leaves the cold reviewer reading the *wrong* source, silently degrading the
factual lens to reasoning-from-the-artifact. Also, stage 6's "code diff/files" is
hand-assembled by the author — an omitted file is invisible. Fix: the spec (stage 1) must
declare the expected touched-files list; reviewer scope at 3/6 = stage artifacts + config
`redteam_context` + that list. At stage 6 the reviewed diff is generated mechanically (e.g.
`git diff` against the recorded base, or a stated file list captured by command, recorded in
the stage doc) — complete by construction, not curated.

**F7 — No criteria-coverage challenge (the class-generator gap).**
Each shipped miss (position-sensitivity, concurrency) produced a new hazard-specific lens —
patching instance classes one postmortem at a time. The *generator* rule is missing: nobody is
charged with asking "what behavior could this change plausibly alter that **no criterion
measures**?" Fix: add a charter item (stage 3, lens-4 adjacent): the reviewer names behaviors
the change could plausibly alter that the criteria do not observe — each named gap needs a
concrete scenario and ranks by impact (precision discipline unchanged; "more criteria" is not
the goal, unmeasured blast radius is the finding). This makes *novel* hazard classes findable
without waiting for their postmortem.

**F8 — The config is never validated at run time (stale-context rot).**
`redteam_context` paths rot (real precedent: the companion config pointed at a deleted install
until manually repointed 2026-07-01). A cold reviewer handed dead paths silently degrades to
docs-only reasoning — the loop's founding failure, reintroduced by config rot. Fix: at run
start, mechanically check each `redteam_context` path exists and is readable; any
missing/empty path is surfaced to the human before proceeding (fix the config or accept
degraded review by name in `decisions.md`).

**F9 — Self-check is under-specified ("encouraged", stage-3-only, no standing criteria).**
SKILL's dogfooding section only "encourages" a stage-3 red-team after edits. But skill files
ARE prompts — a position-sensitive assembly by the METHODOLOGY's own definition (an LLM's
compliance with a rule depends on where/how it appears) — and every real skill edit to date
warranted the full loop. Fix: skill-file edits are declared position-sensitive-assembly edits
(the position lens applies); non-trivial edits take the full loop; standing self-check
criteria named in the section: (a) live copy == source copy (diff), (b) SKILL.md ↔
METHODOLOGY.md consistency on every rule both state, (c) behavior-preservation for anything
moved/removed.

## Flagged structural (NOT built — needs owner sign-off, separate run each)

**S1 — Attention-budget ceiling on Opus.** The documents grow with every patch (467+102 lines
and climbing); each new hazard lens dilutes attention on the others, and mid-document rule
compliance degrades in long prompts. At some size the marginal rule *costs* more compliance
than it adds. Candidate rework: a short mandatory checklist (per-stage, one screen) up front
with the full spec as reference appendix; per-lens trigger index. Fixes above are written
terse to respect this.

**S2 — SKILL/METHODOLOGY dual-maintenance.** The same rules stated twice; every change edits
both and drift is a standing hazard (mitigated today by ad-hoc consistency criteria, F9 makes
that standing). Candidate rework: single source of truth with SKILL.md reduced to pure
operating procedure + pointers.

**S3 — decisions.md integrity rests on convention.** Append-only is asserted, not enforced;
the same author writes it. Low priority in a self-trusting workflow; a mechanical guard
(hash-chain or git-commit-per-gate) only matters if the loop is ever run adversarially.

---

## Erratum (stage-3 round-1 finding FA-2, 2026-07-03)

F1's claim that the C3 attempt-1 confound was "caught only by author honesty, not by any rule"
is half-true: detection came from the precedent's **strict pass condition firing** (control
caught the bug → "treatment catch AND control miss" not met, `concurrency-lens/decisions.md`
stage-8 attempt 1); author honesty supplied the *diagnosis* (leak, not benign redundancy). The
lesson stands, sharpened: the strict differential pass condition WAS the confound tripwire,
and its tripwire *function* (anomalous control catches force an investigation, never a silent
disposition) must be preserved in any replay-A/B design [reworded per round-2 R2-9b].
