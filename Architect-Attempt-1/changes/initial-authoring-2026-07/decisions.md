# decisions.md — Architect authoring, run `initial-authoring-2026-07` (append-only)

## Run-start path validation (CFG3 — gate 4 may not pass until this is recorded)

Validated 2026-07-24 at run start. Every path a cold reviewer will be handed
(`redteam_context` + the spec's touched-files) mechanically checked for existence + readability.

`redteam_context` (priority-ordered, from `guarded-change.architect.md`):

| # | Path | Result |
|---|---|---|
| 1 | `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` | OK — exists, readable (sha256 `2b44e6b32d4e5519a8d53ef2cbe0df4c58a0a16cf6abd90873757bb3b89ce629`) |
| 2 | `…/Guarded_change` | OK — exists, readable (dir) |
| 3 | `…/Dragonfly` | OK — exists, readable (dir) |
| 4 | `/home/zero/Desktop/claude-code-skills/Data-Distiller` | OK — exists, readable (dir) |
| 5 | `…/skill-creator/skills/skill-creator/` | OK — exists, readable (dir) |
| 6 | `…/Architect` | OK — exists, readable (dir; empty but for config + changes/) |

Spec touched-files: all **created** (greenfield) except none-modified; no pre-existing target
paths to validate beyond the Architect dir (#6 above), which exists. **No dead/missing paths.**

Degraded-review acceptance: **not needed** — all paths live.

---

## Stage 3 — red-team of {1-spec, 1.5-criteria, 2-plan} — pass 1

Cold reviewer: general-purpose subagent, model claude-opus-4-8. Verbatim record in
`3-redteam-plan.md`. Worst finding: **MAJOR** — the generative-critic mechanic (tier iii) is
behaviorally unverified; B1's oracle exercises the fixed-list floor (spine §4, now anticipated),
and no criterion plants an *off-list* load-bearing hole to discriminate a generative critic from a
checkbox sweep. Route recommended: stage 2.

Supporting minors worth folding in: no behavioral criterion for the convergence/decomposition guard
(twin cap #2, a novel Architect mechanism); no criterion asserts the router's "rules up front"
placement (position lens; DD precedent C9). Disclosed/accepted minors: 3-cold-agent mutual
independence counted not verified (family-wide, B coverage-note §210); B6 context-isolation may need
a stop-for-human in a single-process dry-run (already disclosed); user-space catalog assumed
git-initialized (dry-run uses a scratch catalog). Nitpicks: no declared fan-out cost-bound; no
pass-ordering criterion; spec "empty repo dir" wording imprecise.

## Gate 4 — pass 1 route

Worst severity **MAJOR** → **route to stage 2** (autonomous; not a stop-for-human — blockers stop,
majors route). Bounce 1 of the iteration cap for finding-class "stage-3 / generative-critic
coverage." Criteria NOT frozen (freeze happens only on route-to-build). Fix applied to `2-plan.md`
(+ `1.5-criteria.md`, unfrozen) then re-red-team. Prior findings carried forward to the pass-2
reviewer.

## Stage 2 — amendment (addressing the pass-1 MAJOR + substantive minors)

- **MAJOR fix:** added criterion **B1b** (generative-critic tier — plant an *off-list* load-bearing
  hole neither on the 7-spine nor any Layer-2 required list; the generative critic must flag it;
  intact-twin discrimination) and reframed **B1** explicitly as the fixed-list *floor* replay.
  Added the off-list fixture to `2-plan.md`'s instrumentation table + build deliverables.
- **Minor fixes:** added **B7** (convergence/decomposition guard fires on non-reducing recursion,
  gating, with oracle-can-fail self-test); added **S7** (router rule-block precedes the stage table,
  position-lens placement check, gating). Added a declared dry-run agent-count cost-bound to
  `2-plan.md`; added a pass-ordering assertion to B2; corrected the spec "empty repo dir" wording.
- **Accepted-with-reason (not fixed):** 3-agent mutual independence (family-wide limitation, out of
  scope for conformance — as Data-Distiller); B6 single-process caveat (already routed to
  stop-for-human); git-init of the user-space catalog (a stage-5 build detail, dry-run uses a
  scratch catalog).

## Stage 3 — pass 2 (re-red-team of amended {1-spec, 1.5-criteria, 2-plan})

Fresh cold reviewer (independent of pass 1): general-purpose subagent, model claude-opus-4-8.
Verbatim record in `3-redteam-plan.md` (PASS 2). Confirmed **all 8 pass-1 findings RESOLVED**; the
pass-1 **MAJOR is closed** — B1b now behaviorally discriminates the generative tier from the
fixed-list floor (auditable off-list property + a checkbox-sweep-would-pass self-test), verified by an
independent reviewer. Factual + Fidelity lenses earned-clean; Concurrency lens correctly stood down
(append-only single-writer confirmed true, not assumed). Worst pass-2 finding = **MINOR**.

Pass-2 findings + disposition (each an in-place fix or accepted-with-reason):
- MINOR (B1b fixture must record *why* the off-list section is load-bearing) → **fixed in place**
  (1.5-criteria.md B1b oracle).
- NITPICK (B7 bound numerically unspecified) → **fixed in place** (B7 oracle requires the build to
  declare the concrete bound).
- NITPICK (charter lens-order "load-bearing" is loose) → **fixed in place** (2-plan.md downgraded to
  lens distinctness, covered by S3).
- NITPICK (B1b self-test (b) analytically entailed) → recorded as **optional build hardening**.
- CH8 low-impact notes (Completeness *lens* present-but-not-run; seed first-run bootstrap unchecked;
  granularity-check coldness unverified; RUN.md/index.md production only transitive) → **accepted,
  surfaced to the build** — none gating; defense-in-depth / stage-5 details.

## Gate 4 — pass 2 route  ✅ READY-FOR-BUILD

Worst severity **MINOR** → **fix-in-place, proceed** (all three in-place fixes applied above and
traceable to logged pass-2 findings). No Blocker, no Major → **route = ready-for-build (stage 5)**.
Iteration cap: finding-class "stage-3 / generative-critic coverage" cleared at bounce 1 (not
re-raised at pass 2) — no cap pressure. **Under delegation, this subagent runs the front half only
and STOPS here; the orchestrator takes the frozen artifacts into stage 5 (build).**

**Path-validation prerequisite (CFG3): satisfied** — run-start validation recorded above (all 6
`redteam_context` paths + the Architect dir live; no dead paths). No new paths were introduced at
either reviewer spawn (both reviewers read the same validated set), so no re-validation was owed.

**Criteria freeze (FRZ).** `1.5-criteria.md` is **frozen** at the route-to-build version.
- Frozen sha256: `c0e4d7481aabd175b15b2808cc56b32eb3118948f6ffd284557536b254970b58`
- Note: the pass-2 reviewer read `1.5-criteria.md` at sha
  `8f537952edc3ebd6bd2dec24a69bd6841e164300aea04a247d5cd249d0f686d8`; the frozen version differs by
  exactly the two gate-4 **in-place fixes** logged above (B1b "why load-bearing"; B7 "declare the
  concrete bound") — each traceable to a pass-2 finding, each a strengthening (no weakening,
  gating→advisory, threshold loosening, or scope narrowing), so no targeted re-red-team of the edited
  criteria is owed under FRZ. Stage 8 verifies the file still matches this frozen hash.
- Final artifact hashes at freeze: 1-spec.md `fcf35ea5174e1c5a9dd035e2915a78df64fba4883d6873fdd038a2b96ab5de91`;
  1.5-criteria.md `c0e4d7481aabd175b15b2808cc56b32eb3118948f6ffd284557536b254970b58`;
  2-plan.md `e144e606494c780f63e70700a2ecddcf101ed842da8e7e32e223e4fd492e665f`.

**Stop-for-human at this gate: NONE.** No blocker, no missing criteria/config, no gating criterion
unverifiable-as-written pre-ship (the one candidate — B6 cross-process context isolation — is a
stage-5/8 concern, disclosed and pre-routed to stop-for-human *if* the build's dry-run cannot exercise
it; it is not a stop now), no carried fidelity ratification. RAT3 imposes no halt here.

---

## Stage 5 — build (author the Architect skill files)

Built the skill under `Architect/` per the frozen `{1-spec, 1.5-criteria (c0e4d748…), 2-plan
(e144e606…)}`, mirroring the siblings. Verbatim inventory in `5-build-notes.md`. `quick_validate.py
Architect` → **exit 0** ("Skill is valid!"). Structural self-checks S1–S7 pass by inspection. Mechanical
build diff in `6-build.diff` (base 8d73e5d; 18 files, +1236). **New-path validation (CFG3):** all 18
built files exist + readable — recorded, no dead paths.

**Scope decision surfaced (CP3 fixtures).** `2-plan.md` CP3 designates the behavioral fixtures
(B1/B1b/B2/B3/B4/B5/B6/B7 + twins) as stage-5 deliverables. They were **not** built in this run, because
the orchestrator scoped stage 5 to the skill files and STOP-before-stage-8, framing fixtures/execution
as stage-8 work. This is a genuine divergence between the frozen plan and the orchestrator's operational
partition — **surfaced, not resolved unilaterally** (per CP5: never silently defer a gating path).

## Stage 6 — red-team of the built code — one cold pass

Cold reviewer: fresh `general-purpose` subagent, model claude-opus-4-8, independent of the stage-3
reviewers. Verbatim record in `6-redteam-code.md` (charter given, context list, raw output, agent
type/model, reviewer-reported context-file sha256s). Charter = guarded-change core (five lenses +
earned-clean) + ST6d mechanical-diff duty + position lens (fires) + concurrency (stood down, confirmed
append-only single-writer-per-node). Author spot-verified a sample of cited lines (F1, I2, P1, GBP,
CP3) — all held; **no fabricated citation**. Factual lens earned (fork-provenance sha checked
side-by-side); Fidelity lens **earned-clean** (all seven owner-pinned mechanisms implemented, no
proxies). S1–S7 all PASS.

Findings (worst-first): **1 MAJOR** (CP3 fixtures not built → 8 behavioral criteria un-executable until
built — reviewer routes it to **stop-for-human**), **2 MINOR** (F1: METHODOLOGY "cold check decides" not
implemented — warm-proposed/cold-validated; I2: cross-file index "Sites" column under-lists real sites),
**3 NITPICK** (GBP "physically"; charter "self-authoring stage 6" collision; auto-index missed-opp).

## Gate 7 — route  ⏸ STOP-FOR-HUMAN (MAJOR = CP3 fixtures scope)

Worst severity **MAJOR**. Per SEV1/GATE a major routes backward to stage 5 (build the fixtures) — but
the fixtures-vs-stage-8 partition is exactly the scope question only the human/orchestrator can rule,
so routing to stage 5 would **self-answer** it. Under **RAT3** this is a **stop-for-human**: the runner
**HALTS and relays the question verbatim** to the orchestrator. The MAJOR is **not demoted** (SEV3:
demoting a major needs the human tie-break); the reviewer's routing stands. Iteration cap: bounce **1**
of finding-class "gate-7 / CP3-fixtures-scope" — no cap pressure.

**MINORs — fixed in place (each traceable to a logged reviewer finding, each a strengthening, no
weakening / no criteria change):**
- F1 → `METHODOLOGY.md` GRN reconciled to "orchestrator proposes (mirroring DD's **coordinator-run**
  sizer), the two cold passes validate; coldness enters at validation" — matches stages 2/6 + the DD
  analogy; index GRN row updated.
- I2 → `METHODOLOGY.md` cross-file index: intro now declares the **grep authoritative** (Sites column
  indicative, not exhaustive — the check greps the token); RST/CAP/GRN rows corrected.

**NITPICKs — two fixed (cheap clarity), one logged:** GBP "physically cannot be written" → "the stage-7
assemble step checks … first, so `assembled-plan.md` is not written while any node is un-gated"
(`SKILL.md`); charter "self-authoring stage 6" → "guarded-change self-review — *guarded-change's* stage
6, not Architect's own stage 6". Auto-derived index (missed-opp) logged, **not** fixed (optional
hardening). Re-validated after fixes: `quick_validate.py` exit 0; S7 holds (rule block line 15 < stage
table line 64); no "either pass"; F1 phrasing gone.

**Stop-for-human question relayed to the orchestrator (verbatim):** *"The frozen plan's CP3 designates
the behavioral fixtures (B1/B1b/B2/B3/B4/B5/B6/B7 + intact/reducing twins + the finalize-blocked /
gate-state observables) as stage-5 build deliverables. This run built the skill files only and stopped
before stage 8 (harness), per your stage-5 charter. Should stage 5 build those fixtures now, or are
they part of the stage-8 harness run you have partitioned off? The stage-6 cold reviewer ranks the
omission MAJOR against the frozen plan and routes it to you; the shipped skill files are otherwise
clean-to-MINOR (S1–S7 PASS, fidelity earned-clean, the two MINORs fixed in place)."*

---

## Gate 7 — ORCHESTRATOR RULING on the CP3-fixtures scope-partition (2026-07-24 ~20:15 EDT; orchestrator = main session, Claude)

**Ruling:** PROCEED to stage 8. The CP3 behavioral fixtures (B1/B1b/B2–B7 + intact/reducing twins +
finalize-blocked / gate-state observables) are built as the **first step of the stage-8 harness run**;
the harness then executes the behavioral criteria against them.

**Why this is an ORCHESTRATOR call, not an OWNER call (no RAT3 escalation):** the fixtures' absence is a
product of the orchestrator's own loop-partition — the stage-5 build subagent was chartered to build the
skill FILES and stop before stage 8. Whether the fixtures are authored under a "stage 5" or "stage-8
setup" label changes nothing about the artifact, the design, or owner intent; the substantive
requirement — the fixtures MUST exist and the 8 behavioral gating criteria MUST be executed before
accept — is honored in full, not waived. Ruling on execution-sequencing *within the approved frame* is
the orchestrator's role and substitutes for no owner decision. A genuine owner question would change
scope, design, or the accept bar; this changes none of them.

**Not a criteria change.** Frozen `1.5-criteria.md` untouched (sha `c0e4d748…`). The MAJOR is resolved by
*building the missing instrumentation*, not by relabelling or lowering any criterion.

**Iteration cap.** Closes gate-7 bounce 1 (finding-class "gate-7 / CP3-fixtures-scope"); the resolution
is forward (into stage 8), not a stage-5 re-loop, so no same-gate re-bounce is incurred.

**Carried watch item (this one WOULD escalate).** B6 (cross-process context isolation) and B7's
subjective work-size estimate remain candidate **genuine** stop-for-human items at stage 8 *if the
dry-run cannot verify them pre-ship* — those bear on whether a gating criterion is verifiable before
accept (an owner-facing accept question), unlike this sequencing call. Roy is away this evening; any such
item is queued verbatim under **NEEDS ROY** in the morning summary, never self-answered.

---

## Gate 8 — harness result

**CONFORMANCE: PASS** (see `8-harness.md`). Freeze-verify **MATCH** — on-disk `1.5-criteria.md` sha256
`c0e4d7481aabd175b15b2808cc56b32eb3118948f6ffd284557536b254970b58` == the gate-4 frozen hash; criteria
unchanged since freeze, so every PASS is valid against the frozen bar. **No real skill defect found.**
Gating: **15 verified**, **1 partial (B6)**, **0 failed**; advisory: SC3 (N/A greenfield).
The founding-failure pair passed faithfully with real independent cold agents — **B1** 3/3 flagged the
removed spine §4; **B1b** 3/3 caught the *off-list* section via the generative sweep while each confirmed
all listed sections were physically present (checkbox-sweep-would-pass); **B2** 3/3 at the ROOT caught both
a root-altitude hole and a between-child **seam** hole, proving coverage is not leaf-only. Intact/reducing
twins discriminated in every case. **B5** executed for real (git catalog with a genuine back-propagation
commit `78e8c96`). Orchestrator spot-verified: harness record, freeze hash, fixture tree, and the B5 commit.

## Stage 8 — owner risk-acceptance of the B6 residual (RAT1-style ratification record)

**Flagged axis.** B6 is a **gating** criterion left **PARTIAL**: its restart contract and its
context-economy **dispatch contract** are verified (each sub-orchestrator's handed input excludes sibling
internals and is byte-for-byte invariant when a sibling subtree is enlarged 2→200 nodes), but the
**live-execution** claim — that a really-spawned recursive sub-orchestrator's *working context during
execution* physically excludes sibling-subtree internals (true cross-process context isolation) — was not
exercised. **Options presented to the owner, verbatim:**
> "(a) a heavier live harness that spawns real nested sub-orchestrators and inspects their running context,
> or (b) a named risk-acceptance in `decisions.md`."
(The orchestrator's stated recommendation was (b), with the reasoning that the unexercised part is
essentially measuring a property the subagent execution model already guarantees, while explicitly
declining to self-accept: "it's your accept-bar call, not mine, so I'm not self-accepting it.")

**Owner's response — verbatim.** Roy (owner), this session's chat transcript, 2026-07-24 evening
(durable source: the session transcript line following the stage-8 harness report; the owner also switched
the session model to `claude-opus-5` in the same turn, which timestamps the exchange in the transcript):
> "agreed, option b. Been down the rabbit hole of trying to outsmart the model testing the thing before,
> deminishing returns after the first attempt most of the time"

**Mapping to the flagged axis.** "option b" names one of exactly two presented, mutually-exclusive options
and selects the **named risk-acceptance** route, rejecting the heavier-harness route (a). The rationale
given — diminishing returns on elaborate harnesses that try to out-test the model — is an argument
*against* (a), consistent with selecting (b). The answer is therefore **disambiguating, not partial or
adjacent**: no re-ask is owed under RAT1, and the acceptance was **not** resolved into the author's pick by
default (the owner's words independently select it).

**RISK ACCEPTED — named.** Accepted by: **Roy (owner)**, 2026-07-24. **What is accepted:** shipping
Architect with B6's *live cross-process context-isolation* claim **verified only at the dispatch-contract
level**, not by live introspection of a running sub-orchestrator's context. **Residual risk:** if the
runtime were ever to leak sibling-subtree content into a child orchestrator's context despite a
sibling-excluding input set, the ECON guarantee would be weaker in practice than the criterion asserts;
the restart contract and dispatch-level economy are unaffected (both verified). **Mitigation standing:**
each sub-orchestrator is a separate agent invocation whose context is constructed from its handed input
set, so the property is structural to the execution model; the dispatch-manifest invariance test
(`fixtures/B6-context/dispatch-manifests/`) is the standing regression check. **Revisit trigger:** if a
future run shows a sub-orchestrator referencing sibling-subtree internals it was never handed, B6 is
re-opened and route (a) is built.

**Gate 8 disposition: ACCEPT.** No blocker; no unverified gating criterion without a named acceptance;
criteria freeze intact. B7's noted residual (subjective work-size estimate feeding the convergence guard)
is carried as a non-blocking characterization note, not a gate.
