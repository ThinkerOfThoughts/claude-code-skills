# Stage 3 — Red-team of the plan (VERBATIM RECORD)

Cold, independent review of {1-spec, 1.5-criteria, 2-plan} against the priority-ordered
`redteam_context`. This is a **verbatim record** per the charter's provenance rule: the charter
given, the exact context list, the reviewer's agent type/model, its reported context-file hashes,
and its raw output. The author's interpretation + routing decision live in `decisions.md`.

- **Reviewer agent type / model:** `general-purpose` cold subagent (no shared context), Claude
  Opus 4.8 (`claude-opus-4-8`).
- **Context list given (closed set):** the three artifacts under review (1-spec.md,
  1.5-criteria.md, 2-plan.md) + the 6 config `redteam_context` paths (approved plan; DISTILLATION-
  METHOD-ISSUES-LOG.md; AGENT_BRIEFS.md; guarded-change skill dir; dragonfly skill dir; T1-T4
  results dir). The spec's touched-files do not exist yet (greenfield) — the reviewer was told so.
- **Context-file sha256 (reviewer-reported):** see the provenance block in the verbatim output.
- **Charter given:** the METHODOLOGY red-team charter **core** verbatim (five lenses + discipline
  bullets + provenance) + the position lens (skill files = position-sensitive assembly) + the
  stage-3 additions (CH8 coverage challenge; CH9/CH10 label audit). The exact prompt text is
  reproduced in the "CHARTER / PROMPT GIVEN" section below.

---

## CHARTER / PROMPT GIVEN (verbatim)

> You are a COLD, INDEPENDENT reviewer. You share no context with the author. Your job is a
> stage-3 red-team of three planning documents for authoring a new Claude Code skill
> ("Data-Distiller"). You are graded on PRECISION (are your findings real?), not on how many you
> raise. "No issue found" per lens is a valid, expected result.
>
> [Artifacts under review: 1-spec.md, 1.5-criteria.md, 2-plan.md.]
> [Underlying source, priority-ordered redteam_context: (1) approved plan; (2) DISTILLATION-
> METHOD-ISSUES-LOG.md; (3) AGENT_BRIEFS.md; (4) guarded-change skill; (5) dragonfly skill; (6)
> T1-T4_Results dir — each with a "what to check here" note. Greenfield: the skill's own files do
> not exist yet.]
> [CHARTER: five separate lenses — Factual (earned with citations), Logical, Missed-opportunity,
> Assumptions/risks, Fidelity (earned by pinning loaded terms to owner mechanism). Discipline:
> cite-or-it-doesn't-count; rank every finding (blocker/major/minor/nitpick); flag the
> unverifiable; "no issue found" is valid. POSITION LENS: skill files are prompts — test that
> criteria verify behavior by EXECUTION not text-presence; information-preserving ≠
> behavior-preserving. STAGE-3 ADDITIONS: CH8 coverage challenge (required section); CH9/CH10
> label audit (required, earned per gating criterion — challenge advisory dodges, proxy
> verifications, the reduced-analyst representativeness claim, and C7's orchestrator hand-off).
> OUTPUT: provenance block with agent type/model + sha256 of every context file read; per-lens
> findings; CH8 section; CH9/CH10 section; worst-severity + routing. Do not re-litigate
> owner-approved design decisions — check the docs CONFORM to them, are internally consistent,
> cover every issues-log guardrail, and specify genuinely-checkable criteria.]

*(Full prompt as dispatched is preserved in the run's transcript; the above is its faithful
structure with the load-bearing instructions verbatim in the charter/additions.)*

---

## REVIEWER VERBATIM OUTPUT

# Stage-3 Cold Red-Team Review — Data-Distiller planning docs

## 1. Provenance block

**Reviewer:** `general-purpose` cold-review subagent (no shared context with the author), model Claude Opus 4.8 (`claude-opus-4-8`).

**Context files read (path → sha256):**

| Path | sha256 |
|---|---|
| .../initial-authoring-2026-07/1-spec.md | 5c4c98cfc8daef140afd01e74230c37273d7c6a0df2d0d6ca57f82baa0a72783 |
| .../initial-authoring-2026-07/1.5-criteria.md | 1157297b8fcd87963ab8ca93bcff4b543f3f89ce47b37d3d06c50537110471c9 |
| .../initial-authoring-2026-07/2-plan.md | 4a549200b2b9b06e02febab23e66acd79a61b4c2d2eca4cdd335608c2104a0f1 |
| ~/.claude/plans/your-understanding-is-correct-wise-bee.md | 430e00c0fd50e694a86aa6658624ecfc2eb03c6a2bc14b819e79a5da7ccabf10 |
| .../T1-T4_Results/DISTILLATION-METHOD-ISSUES-LOG.md | af5da9aa37ed0f34fb7c6d37b9e6f2f097576443b3f5c1693cc1f86d822f6846 |
| .../T1-T4_Results/AGENT_BRIEFS.md | ecfc00fcf78ae9e6cb483972b435ced63ba9fa9e01961a6eb7dfa9d9d5628296 |
| .../T1-T4_Results/RESUME.md | f24533fc975a7d3b10ef1612ae672c2a39ef60b181467adc1aee52324d3937eb |
| .../T1-T4_Results/raw_findings/T1_bait-original_superlist.md | 916642799480aa459905ab0f497da07f379426453a7cc1f3f8dafe1cad90e947 |
| ~/.claude/skills/guarded-change/SKILL.md | addf17481c57bcada577ff2d3d74628b93ea8b43a89c884d25a670af8889c625 |
| ~/.claude/skills/guarded-change/METHODOLOGY.md | 8f3fe2b322ec802d080aa130ebd5dd526c4407a2f729931763c6a778ea4a7c30 |
| ~/.claude/skills/guarded-change/stages/charter.md | 0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590 |
| ~/.claude/skills/guarded-change/stages/stage-1.5.md | c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b |
| ~/.claude/skills/guarded-change/stages/stage-8.md | 8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3 |
| ~/.claude/skills/dragonfly/stages/charter.md | c5d1e2068f35760e373517e243003800c264c64bf3d93d6d8ea6b951990af870 |

---

## 2. Per-lens findings

### Factual lens

Citations consulted (evidence for a mostly-clean verdict): approved plan lines 50–56 (6/3 redundancy + `PCT% (X/N)` + floor table + percentage-first sort) match spec decisions 4 & 6 and criteria C3/C8(iii); approved plan lines 42–46 (size trichotomy) match spec decision 5 / plan stage-1; issues-log line 51 ("slim anything above ~50 MB") matches plan stage-1 line 27; approved plan output-tree lines 86–124 match spec decision 11; RESUME line 67 (T1:9 T2:3 T3:18 T4:41 = 71) matches spec line 5; C3's floor self-test (`50% (2/3)` wrong → 66%) is arithmetically correct against approved-plan line 55. On these the change docs faithfully transcribe the approved plan. (Note: the *actually-run* method in AGENT_BRIEFS/RESUME used 3 Sonnet analysts + raw-count `[agreement=N]` agreement — see `T1_bait-original_superlist.md` line 5; the plan's 6/3 + PCT% is the owner-approved **evolution** per approved-plan lines 50–56, explicitly settled and NOT re-litigated here. The change docs conform to the approved plan, which is source of truth.)

**F1 — MINOR (borderline major).** The plan's brief-porting step (2-plan.md lines 52–55) instructs only to "port the AGENT_BRIEFS templates … Genericized (placeholders where the T1–T4 copies had companion-emergence specifics)." But the templates being ported implement the *old* method: `AGENT_BRIEFS.md` MERGE template (lines 122–136) renders agreement as raw `[agreement=N, recurrence=M]` and sorts "descending by agreement (all 3s, then 2s, then 1s)"; the ANALYSIS/VERIFY templates hardcode "Sonnet; 3 independent." A literal "genericize the placeholders" port preserves raw-count agreement, agreement-first sort, and a fixed count/model — directly contradicting settled decisions 4 (6/3 tiering) and 6 (`PCT% (X/N)`, percentage-first sort). The port needs *substantive adaptation* (tier-driven count+model slots; agreement rendered `PCT% (X/N)`; sort percentage-desc), which the plan step does not name. The plan is thus internally inconsistent between "port/genericize" (step 5) and stage-3/decision-6 (6/3 + PCT%). Gating criteria C3 and C8 would catch the contradiction at stage 6/8, so it will not ship wrong — hence minor — but redteam-context #3 asks precisely "does the plan's brief-porting preserve these?" and here *preservation is the bug*: the merge/analysis briefs must be **changed**, not preserved. Fix in place: expand the brief step to enumerate the required adaptations.

**F2 — MINOR.** The charter-fork instruction (2-plan.md lines 46–50) says "record the source commit in a provenance header, as dragonfly did," but the dragonfly precedent's header (`dragonfly/stages/charter.md` lines 10–13) has *two* load-bearing parts: (i) source commit `@ 3d6889b`, and (ii) an explicit "**deliberately not carried**" enumeration (position/concurrency lenses, A/B-clause, closed-set rule). The plan transcribes part (i) and omits the discriminating part (ii) — the not-carried note is what makes a fork auditable. Fix: require the provenance header to state what was deliberately not carried.

### Logical lens

**L1 — MINOR.** Sequencing tension between "build the static `tree/` skeleton" + "compute the concurrency budget" at **decompose-time** (2-plan.md line 30, stage-1) and the **human cut-gate** at stage-2 which "approve[s] unit/splits/overlap" (line 31). Both the per-piece leaf dirs and the peak-agents budget are functions of the split count — which the human can *revise* at the gate. As written, the skeleton and budget are committed before the human approves the very splits they depend on. The plan inherits this from the approved plan (lines 119–122 vs 57–60) and does not resolve which of {skeleton is provisional & rebuilt post-gate, or the gate can only rubber-stamp the sizer's proposal} holds. The stage files will need to state the feedback path; the plan should flag it. (Related coverage gap in CH8.)

### Missed-opportunity lens

**M1 — no material finding.** Two candidates examined and dismissed as *correct* calls, not missed opportunities: (a) fabricated synthetic corpus over a "thin slice of real T1–T4 data" (approved-plan line 143 offered both) — fabricating is the *safer* choice because a real-data walk would risk the exact persona-guard/off-limits trips the skill exists to prevent (issues-log #1/#3); (b) canonical-strings-reused-verbatim + C8 grep instead of an include mechanism — markdown skill files can't include, and this is the sibling house pattern. No missed opportunity ranked.

### Unstated-assumptions / risks lens

**A1 — MINOR.** The plan asserts (2-plan.md lines 114–121) that the reduced-analyst harness (2–3 real subagents rather than tier-6) "does not weaken any of the six criteria." This *assumes* the two decomposed halves compose: blindness is shown with 2–3 real analysts (C1), and the `PCT% (X/N)` denominator is shown separately with *fabricated* lists at "known N" (C3). Consequence: no executed path ever runs a real tier-6 dispatch whose `/6` denominator rides end-to-end through merge→summary; the binding "N = the tier's redundancy count" is verified only as a document invariant (C8 iii), never executed. Reasonable cost bound, but the composition is an unstated assumption worth recording. (See label audit.)

**A2 — MINOR.** The read-only + off-limits brief clauses — the guardrail for the *one* real production line-crossing that no mutation-guard catches (issues-log #3) — are verified only by document invariant (C8 iv), never by any behavioral criterion, and the example `ledger.md` **redaction** (decision 8; issues-log #3: redact live paths to `<REAL-PATH-REDACTED>`) has *no* criterion at all. A cheap gating grep — "no live off-limits/protected path string appears in any agent-facing ledger/brief" — is available and absent. Risk: a shipped example ledger that still carries live protected paths reproduces exactly the issue-3 temptation. (Efficacy of "the agent obeys the clause" is inherently untestable and is not the ask here; the *redaction of the artifact* is.)

### Fidelity lens — loaded terms pinned

Per the charter, naming each loaded operational term, its pinned mechanism, and whether the plan implements *that* mechanism (not a proxy):

- **"blind coordinator"** → pinned to: node opens only `_status.md` + globs child dir names, never `Read`s analysis/`*_verified`/`superlist`/`*_summary`. Plan implements the mechanism: C1 verifies by **execution** (inspect the coordinator's own transcript for zero findings-file reads), and instrumentation (plan lines 74–78) makes findings physically live in child leaves with `_status.md` as the sole parent-readable surface. Not a proxy. ✓
- **"analyst/verifier/merge/summary"** → pinned to: a single dispatched cold `general-purpose` subagent doing the job itself, no sub-delegation. Plan dispatches real cold leaves (stages 3–6) + do-the-work clause; C1's walk dispatches *real* subagents. ✓
- **"size handling"** → pinned to: strategy *selection* among {tag-replace, subdivide, escalate}, not "slim everything." **Partial (see F3 below):** C4 exercises tag-replace and subdivide and its oracle-can-fail distinguishes a small item (does not always say "subdivide") — but the **third** strategy, *escalate-tier for the irreducible* (approved-plan line 46), is exercised by **no** criterion.
- **"human cut-gate"** → pinned to: an actual stop-and-wait, dispatch blocked until an approval record exists — not an auto-approved log entry. C5 verifies the governed behavior (stop occurs + zero dispatch until a record exists) by execution, oracle-can-fail flags dispatch-before-record. ✓ (The "actual human" is legitimately un-automatable; the dispatch-blocked-until-record core is the proxy-free part and it *is* tested.)
- **"agreement"** → pinned to: `PCT% (X/N)`, N = the item tier's analyst count (6 or 3), denominator preserved merge→summary. C3 tests format+floor+sort on a real merge with known N + doc-invariant for denominator-preservation. Mechanism implemented; the N-equals-tier-count binding is doc-invariant only (A1). ✓ with caveat.

**F3 — MINOR (fidelity).** "Size handling = selection among **three** strategies" is implemented for two: **escalate** (irreducible → escalate model tier; approved-plan line 46, spec decision 5c) is named nowhere in the criteria and is not in the stage-8 synthetic corpus (2-plan.md lines 97–104 fabricate only a binary-bulk item and a text item). One-third of the settled trichotomy — and specifically the Opus-reserve path — is unexercised.

---

## 3. CH8 — Coverage challenge (unmeasured blast radius)

Behaviors the build could plausibly get wrong that **no** criterion C1–C10 observes:

1. **Escalate-tier size strategy (impact: medium).** No criterion; no synthetic item is genuinely-irreducible-oversize. Scenario: an item that neither tag-replaces (analytically-relevant text) nor cleanly subdivides gets mis-routed to Haiku-subdivide instead of Opus-escalate → the OOM/context-overflow class the skill exists to prevent. (= F3.)
2. **Seam-aware merge for subdivided items (impact: medium).** C3 tests a *flat* merge of two fabricated lists; plan stage-5 promises "seam-aware for subdivided items," but no criterion feeds a subdivided item's per-piece lists through the seam-aware dedup. Scenario: a finding straddling a split seam is double-counted or dropped, corrupting agreement/recurrence on exactly the items the human cut-gate exists to protect.
3. **Human *revision* (not just approval) at the cut-gate propagating to tree + budget (impact: medium).** C5 tests only block-vs-proceed. Scenario: the human changes split points at the gate; the pre-built piece dirs / concurrency budget from stage-1 are now stale and nothing re-derives them. (= L1.)
4. **Ledger/brief redaction of live off-limits paths (impact: medium-low; ties to a real incident).** No criterion asserts the agent-facing example ledger is redacted. (= A2.)
5. **Density/complexity tier-escalation of an in-window item (impact: low).** Approved-plan lines 48–49 allow a within-window item to escalate when judged dense; inherently a judgment call, untested. Acceptable as a rubric, but note it is unmeasured.
6. **Liveness/watchdog/pacing guardrail (impact: low; see label note).** The issues-log operational gotcha "watchdog to kick the session on usage-reset" + RESUME's hung-agent detection / pacing (RESUME lines 30–34, 44) have no home in any stage and no criterion. C2 covers the *durability* half (resume from disk) but not the *liveness* half (auto-kick, hung-agent kill+respawn). Plausibly deliberate as environment-specific tooling — but the plan is silent on the decision, which is itself the gap. (The **stale-PROGRESS-edit** gotcha, by contrast, is genuinely *obviated* by the new per-node `_status.md` + trust-files-over-cursor design — no single global cursor to stale-edit — so it is not a gap.)

An explicit note: guardrail coverage of the issues-log is otherwise complete — read-only clause (#1), streaming slimmer + du-h + never-Read->50MB (#2), off-limits clause (#3), delegation (do-the-work) all have homes in spec decisions 5/8/9 and criteria C4/C6/C8.

---

## 4. CH9/CH10 — Label audit

Per gating criterion, the governed path confirmed exercised:

- **C1 Blindness (gating/execution):** governed path = coordinator's own reads. Exercised — transcript inspected after real analyst leaves write real findings. Reduced-analyst count is a **legitimate** cost bound: blindness is a property of *what the coordinator reads*, count-independent. ✓
- **C2 Restart (gating/execution):** kill mid-stage + re-derive from disk; oracle-can-fail deletes a leaf output and confirms re-dispatch. Governed path exercised. ✓
- **C3 Agreement (gating/execution+invariant):** real merge on known-N lists + per-site grep. Exercised — but see A1: the N-equals-tier-count binding is invariant-only, never a real `/6`. Legitimate given the declared cost bound, but recorded.
- **C4 Size-routing (gating/execution):** tag-replace + subdivide exercised; oracle distinguishes a small item. **Escalate path not exercised** (F3) — a partial governed-path coverage.
- **C5 Cut-gate (gating/execution):** stop + no-dispatch-until-record exercised; oracle-can-fail plants dispatch-before-record. ✓
- **C6 Concurrency (gating/execution) — LABEL-AUDIT CONCERN (minor).** The "serialize-within-cap under real contention" governed path may **not** actually fire in the representative walk. C6's oracle-can-fail sets budget=1 and checks a *planted* 2-in-flight state flags — that tests the checker's logic, not a live bind. Unless the plan pins the harness budget **below** the harness's offered concurrency (3 items × reduced analysts ⇒ up to ~9 would-be-concurrent), the cap never binds during the walk and C6 is effectively verified by a synthetic planted state — a proxy for the real serialization path. Fix: 2-plan.md should pin the dry-run budget below offered concurrency so serialization is observed, not just the oracle.
- **C7 live==source (gating/execution) — "may hand to orchestrator":** this is a **legitimate** division of labor, not an H5-style deferral-to-production: the runner genuinely lacks authority to install the live copy (spec line 108, runner does not commit/push), the `diff -r` check itself is still *run* (just post-sync by the orchestrator), and it is declared not hidden (plan lines 152–153; criteria lines 125–127 require reporting `verified = no` + explicit hand-off, not a silent pass). **Residual process gap (minor):** the criteria do not state that the orchestrator's post-sync diff result is folded **back** into the run's `8-harness.md`/`decisions.md`; as written the run's own record can terminate with C7 at `verified = no`. Recommend the hand-off close the loop by recording the orchestrator's diff outcome.

**Advisory-label audit:** C9 (rules up-front in SKILL.md) marked advisory is **not a dodge** — the *presence* of blindness/read-only/off-limits is gated elsewhere (C8 iv for the clauses; C1 for blindness *behavior*), so C9 only adds the *position/up-front-ness*, which is genuinely degree-based ("up front enough" is judgeable) with a stated reason (criteria lines 160–162), consistent with ST1.5c. C10 (behavior-preservation) marked advisory/N-A is **correct** — greenfield, no prior version, nothing moved/removed; recorded explicitly rather than dropped (criteria lines 164–173). The position property of the *new* assembly is legitimately not reducible to a single execution probe without a pass-rate experiment, and it is not one of guarded-change's standing self-check gates (which fire on moved/removed content). No mislabeled gate found.

---

## 5. Worst-severity summary + routing recommendation

- Blockers: **none.**
- Majors: **none.** (No settled decision is contradicted; no gating criterion is unverifiable-as-specified; F1 is under-specification the gating criteria backstop, not a contradiction that ships.)
- Minors: **F1** (brief-port under-specifies the required PCT%/tier adaptations — top minor), **F3/CH8-1** (escalate strategy unexercised), **CH8-2** (seam-aware merge untested), **L1/CH8-3** (cut-gate revision → tree/budget feedback unspecified & untested), **A2/CH8-4** (ledger redaction unmeasured), **C6 label-audit** (serialization path risks proxy verification unless harness budget pinned below offered concurrency), **A1/C3** (tier-count denominator invariant-only), **F2** (charter fork header missing the "deliberately-not-carried" enumeration), **CH8-6** (watchdog/liveness/pacing guardrail unhomed & undecided).
- Nitpicks: "clean-lens-earned" is a reviewer-lens concept ported into an *analyst* charter (2-plan.md line 50) without reinterpretation — needs recasting as "a no-flags result must be earned by showing coverage," or it is cargo-culted.

**Worst severity: MINOR.**

**Routing recommendation: fix-and-proceed (minor).** No blocker or major surfaced; the plan is sound and conforms to the approved plan on every settled decision checked. Before build, apply the in-place fixes — most importantly **F1** (make the brief-port step enumerate the tier-count/model + `PCT% (X/N)` + percentage-first-sort adaptations, so a literal port does not resurrect the old raw-count method), **C6** (pin the dry-run budget below offered concurrency), **F3/CH8-2** (add an escalate-strategy item and a seam-aware-merge item to the synthetic corpus + criteria), and **A2** (add a redaction grep). L1/CH8-3 and CH8-6 should be resolved by the stage files/plan explicitly (feedback path; and an in-scope-or-not decision on the watchdog).

Note per RAT3: nothing here is a fidelity/intent gap requiring owner ratification — these are internal-consistency and coverage fixes within the owner-approved design, not challenges to it.
