# Stage 8 — Harness (conformance) — Architect authoring, run `initial-authoring-2026-07`

**Run type:** greenfield / **conformance-only** (no stage-0 baseline → no regression section, per config
`measurement.check`). Structural criteria verified by validation/inspection; behavioral criteria verified
by a dogfood dry-run of the **built** skill on fabricated CP3 fixtures (built as step 1 of this run per the
gate-7 orchestrator ruling).

## Freeze-verify (FRZ)

`1.5-criteria.md` on disk sha256 = `c0e4d7481aabd175b15b2808cc56b32eb3118948f6ffd284557536b254970b58`
= the gate-4 frozen hash in `decisions.md`. **MATCH — criteria unchanged since freeze.** No post-freeze
edit; all criteria PASSes are valid against the frozen bar.

## Dispatch representativeness (declared dry-run cost bound, from 2-plan.md)

The production rule is 3 cold agents × 2 passes per node. Per the plan's declared bound: (a) **B1/B1b** ran
the real **3-agent completeness pass on a single node** (the governed path); (b) **B2** ran a 3-agent
completeness pass on the **ROOT node** of a 3-node tree (the load-bearing total-coverage node — root + the
between-child seams); (c) deeper-scale criteria (B4/B6) use reduced/structural exercise since what they
measure is orchestration/gate/restart structure, not the 3-agent count. The founding-failure pair (B1+B1b)
was run faithfully with real independent cold subagents. **11 cold `general-purpose` (claude-opus-4-8)
subagents** were dispatched, each separately-spawned (no shared context with author or with each other).
Raw verbatim transcripts are pointed to per record (task output files); distilled records live under each
fixture's `completeness/{A,B,C}.md`.

---

## Per-criterion verification table (H7)

Columns: criterion │ gating/advisory │ path exercised │ verified-by-execution? │ evidence │ oracle-can-fail result.

### Structural criteria

| Crit | G/A | Path exercised | Verified? | Evidence | Oracle-can-fail |
|---|---|---|---|---|---|
| **S1** | gating | `quick_validate.py Architect` + angle-bracket grep on description | **YES** | validator → "Skill is valid!" (exit 0); description line bracket-free | **fires** — injected `<` in description → validator prints "Description cannot contain angle brackets (< or >)" |
| **S2 / SC2** | gating | grep each of 18 mnemonic IDs across `SKILL.md`/`METHODOLOGY.md`/`stages/`, diff operative claim | **YES** | all 18 IDs present at ≥3 sites (GBP 9, COV 8, RST 7, RAT3 6, PASS-ORD/GRN/TPL 5, …); GBP/PASS-ORD operative claim consistent across sites; real tree uses "both passes" (never "either pass") | **fires** — planted "either pass is clean-or-resolved" in a stage-file copy is flagged vs canonical "both passes"; real tree has zero "either pass" |
| **S3** | gating | resolve each stage-table entry to a file; grep charter for fork-provenance blockquote + Completeness sixth lens + earned-clean | **YES** | 8/8 stage-table entries resolve to real `stages/stage-*.md`; charter "Provenance … Forked from `Guarded_change/stages/charter.md @ 8d73e5d`" present; Completeness "(the Architect sixth lens)" + earned-clean clause present | **fires** — a renamed table entry (`stage-RENAMED-…`) does not resolve; clause-deleted charter would fail the grep |
| **S4** | gating | grep METHODOLOGY for all 7 spine sections (esp. §4 + "location"), Layer-2 hook, generative-critic clause | **YES** | all 7 spine headings present; §4 "Outputs & artifacts" + "location" present; `required_sections` Layer-2 hook + "generative" critic clause present | **fires** — a §4-removed copy fails the "Outputs & artifacts" grep |
| **S5** | gating | `ls templates/seed/*.md` non-empty; grep mechanism doc for user-space path + "git" + "back-propagat" | **YES** | 4 seed files (generic-node, decomposition-node, leaf-task-spec, README); README has `~/.claude/architect/templates/` + "git" + "back-propagat" | **fires** — an empty `seed/` fails the non-empty check |
| **S6** | gating | grep METHODOLOGY for contract fields + "OUTSIDE any target repo" | **YES** | `run_root`, `off_limits`, per-plan-type `required_sections`, catalog pointer, and "OUTSIDE any target repo" clause all present | **fires** — a clause-removed METHODOLOGY copy fails the grep |
| **S7** | gating | in `SKILL.md`, assert rule-block offset < stage-table offset (position-lens) | **YES** | rule block line **15** < stage table line **64** (matches gate-7's recorded 15/64) | **fires** — check is a strict `<`; a swapped variant (rule block after table) fails |
| **SC1** | gating | packaged == reviewed source tree (greenfield: no separate live copy) | **YES** | no working-tree drift on any skill file since gate-7; S7 offsets 15/64 match gate-7; `quick_validate` passes on the shipped tree. Reduces to "packaged artifact == reviewed source tree" per the criterion's greenfield note | n/a (identity check; a modified file would diff) |
| **SC3** | **advisory** | behavior-preservation — N/A greenfield (no prior version) | noted | no prior behavior to preserve (first authoring) | n/a |

### Behavioral criteria (dogfood dry-run of the built skill)

| Crit | G/A | Path exercised | Verified? | Evidence | Oracle-can-fail |
|---|---|---|---|---|---|
| **B1** | gating | completeness-critic pass (3 cold agents) on the §4-removed floor fixture | **YES** | `fixtures/B1-floor/holed/plan.md` (spine §4 silently dropped). **3/3** cold agents flagged the missing "Outputs & artifacts WITH locations" section as **BLOCKER** (the founding-failure section) and held the node from finalize. Records: `B1-floor/holed/completeness/{A,B,C}.md` → raw `tasks/{af23af34f5a5111ad, a11b66ae79745482c, a974b07ce6ee81e90}.output` | **fires (discriminates)** — intact twin `B1-floor/intact/plan.md` reviewed by the same pass → verdict **WHOLE**, §4 explicitly confirmed present (plan.md:21-26), worst finding MINOR, NOT flagged for §4. Record `B1-floor/intact/completeness/A.md` → `tasks/af9aa9857bc1f296a.output` |
| **B1b** | gating | completeness-critic pass (3 cold agents) on the off-list generative fixture | **YES** | `fixtures/B1b-generative/holed/plan.md` — complete on all 7 spine + all 3 Layer-2 sections, missing the **concurrent-edit conflict-resolution (OT/CRDT)** section (on neither list; off-list property + load-bearing rationale in `off-list-note.md`). **3/3** cold agents flagged it via the **generative sweep** as **BLOCKER**; each independently confirmed all 7 spine + 3 Layer-2 sections physically present (i.e. a checkbox sweep would pass) and that only the generative tier caught the gap. Records `B1b-generative/holed/completeness/{A,B,C}.md` → raw `tasks/{ad95ab9b284fe0b7a, aaf189e6926c99c81, a48593c4b75d220cb}.output` | **fires (discriminates), two-part** — (a) intact twin `B1b-generative/intact/plan.md` → **CLEAN-EARNED**, the conflict-resolution section found present & integrated (plan.md:43-50), worst MINOR, NOT flagged (`tasks/a5f8b7825c7ea4fbe.output`); (b) checkbox-sweep-would-pass confirmed behaviorally — all 3 holed reviewers noted both fixed lists fully ticked, so the fixture measures generativity, not the floor |
| **B2** | gating | two-pass total coverage on a 3-node tree; completeness pass (3 cold agents) on the ROOT node incl. between-child seams | **YES** | `fixtures/B2-coverage/tree/` — root plan with a planted **root-altitude §5** hole + a planted **between-child token/signing-key seam** hole; child leaves clean. **3/3** cold agents dispatched **at the ROOT** (owning orchestrator's own slice, children handed for the seams) caught **BOTH** planted holes as **BLOCKERs** — neither hole is inside a leaf, proving coverage is not leaf-only (COV). Records `B2-coverage/tree/completeness/{A,B,C}.md` → raw `tasks/{a9d4fe978dfa868d0, ad0fcdd3591b12adb, a310c8cf4b6ccea18}.output`. **GBP:** no `assembled-plan.md` exists at the holed root while unresolved. PASS-ORD / 3-records-at-every-node / per-child pass sets verified **structurally** by the fixture layout + the skill's GBP/PASS-ORD rules (the executed behavioral core is the root-owner's root+seam catch). | **fires (discriminates)** — clean twin `tree-clean/` (both holes fixed, every node gated clean) DOES produce its assembled deliverable (`tree-clean-assembled-plan.md`): a fully-covered clean tree finalizes; the gate blocks holes, not progress |
| **B3** | gating | small task → granularity check returns leaf, no children (representative) | **YES (representative)** | `fixtures/B3-scaledown/run.md` — small `scale_context` → GRN proposes **leaf**, run tree has **no child nodes**, single low-level pass, per the skill's GRN rule (SKILL "Scale" + stage-6 step 2 + METHODOLOGY GRN) | **fires (discriminates)** — the SAME GRN check **decomposes** a large task (B4), so the leaf decision is a real discrimination, not a hard-wired "always leaf" |
| **B4** | gating | large task → top-level dispatch blocked until `plan/topgate/` exists; deeper split autonomous (path-check, executed on disk states) | **YES (representative)** | `fixtures/B4-scaleup/` — `topgate-absent/` has **no** `plan/topgate/` dir (per TOP, dispatch blocked) vs `topgate-present/plan/topgate/APPROVED.md` exists (dispatch released); a **deeper** split (`checkout/`→{cart-svc,payment-svc}) proceeds with no topgate; leaves are atomic task-specs. The gate is literally a disk-path check and the two fixture states differ exactly by the gate artifact | **fires (discriminates)** — withheld `topgate/` → blocked; supplied → proceeds; the deeper split manufactures no spurious human stop |
| **B5** | gating | template match/instantiate + hole-fix back-propagation, run against a real git catalog | **YES (executed)** | ran under `8-harness-runs/B5-catalog/` (seeded from `templates/seed/`, `git init`) + `B5-run/`: `matched-node` instantiated from `generic-node.md` (`index.md` records `template: generic-node`); a hole-fix was back-propagated to the skeleton and committed — new commit `78e8c96 back-propagate hole-fix (TPL3)…` atop seed commit `e6a6340`. Evidence: `fixtures/B5-template/NOTE.md` + the catalog `git log` | **fires (discriminates)** — `novel-node` matched no skeleton → recorded `template: create-new` (no forced match); a clean node with no hole-fix produced no catalog commit (count unchanged 2→2) |
| **B6** | gating | context economy + recursive orchestration + restart | **PARTIAL** | **Exercised:** (1) **Restart contract** on real disk state (`B6-context/run/tree/`): branch-A (all deterministic outputs present) is **skipped/not re-planned**; branch-B (adversarial outputs absent) **resumes** at that stage — the restart walk discriminates done from not-done (stage-done-iff-output-exists, trust-files-over-cursor). (2) **Context economy at the dispatch contract** (`dispatch-manifests/`): each sub-orchestrator's handed input set = own subtree + seams only, EXCLUDES sibling internals, and is **byte-for-byte invariant** when the sibling subtree is enlarged 2→200 nodes (scales with own-subtree breadth, not total tree size). **NOT exercised:** true **live cross-process context isolation** of a really-spawned recursive sub-orchestrator's working context during execution — see STOP-FOR-HUMAN below. Evidence: `B6-context/NOTE.md` | **fires (discriminates)** — an absent-output node (branch-B) DOES re-run while a complete node (branch-A) does NOT; the enlarged-sibling manifest diff is empty (ECON holds) |
| **B7** | gating | convergence guard on non-reducing recursion (representative, deterministic threshold) | **YES (representative)** | `fixtures/B7-convergence/`: `pathological/` (child/parent granularity 0.90 then 1.00, both ≥ 0.80) → DEC **escalates** within the bounded 2 consecutive levels; the skill declares the concrete bound (≥0.8× parent granularity over 2 levels → escalate) in SKILL/METHODOLOGY/stage-6. Threshold applied deterministically. Residual (non-blocking): the ratio derives from a **subjective work-size estimate** — see note below | **fires (discriminates)** — `reducing/` twin (0.30 then 0.33, both < 0.80) does **NOT** trip the guard; recursion proceeds to atomic leaves |

---

## Findings by severity / disposition

- **Gating verified YES:** S1, S2/SC2, S3, S4, S5, S6, S7, SC1, **B1, B1b, B2**, B3, B4, B5, B7  → **15** (of which B3/B4/B7 by representative harness, B5 fully executed, B1/B1b/B2 by faithful cold-agent dispatch).
- **Gating PARTIAL:** **B6** (restart + dispatch-level context economy verified; live cross-process context isolation not exercised) → **1**, relayed as STOP-FOR-HUMAN below.
- **Gating verified NO:** none.
- **Advisory:** SC3 (behavior-preservation N/A greenfield) — noted, not gated.
- **Real skill defect (blocker/major) found:** **NONE.** Every governed behavior fired: the completeness
  critic caught the floor gap (B1), the off-list generative gap (B1b), and the root + between-child-seam
  gaps at the owning orchestrator's altitude (B2); GBP blocked assembly on an unresolved node; the
  discriminations all held. No skill file was modified (RAT3 boundary respected).

## STOP-FOR-HUMAN (relayed verbatim to the orchestrator — B6 residual)

B6 is a **gating** criterion. A representative harness verified its restart contract and its
context-economy **dispatch contract** (input set per sub-orchestrator excludes siblings and is invariant
to sibling size). It did **not** exercise the criterion's literal live-execution claim, quoted verbatim:

> "At the first major branch the top orchestrator **delegates to a sub-orchestrator per branch** (two at a
> binary split); each (sub-)orchestrator's **working context holds only its own subtree's** skeleton +
> seams + `_status` — **not** any child's full internal plan detail and **not** the whole tree."
> … "confirm the orchestrator's context **measurably does not grow with total tree size** when a sibling
> subtree is enlarged (context scales with own-subtree breadth only)."

The unexercised residual: proving a **really-spawned recursive sub-orchestrator's live working context**
physically excludes sibling-subtree internals *during execution* requires spawning real nested
sub-orchestrators and introspecting their running context — true cross-process context isolation, which a
single-process conformance dry-run represents only by the parent's dispatch **intent** (the input set),
not by a measurement of the child's running context. This is the exact item pre-routed at gate 4 and
re-flagged at the gate-7 orchestrator ruling as a candidate stop-for-human *if the dry-run cannot verify it
pre-ship*. It cannot be fully verified pre-ship by this representative harness, and **no named
risk-acceptance exists** in `decisions.md`. Per RAT3 / CP5 it is **surfaced, not self-accepted and not
silently deferred** — queued verbatim for the owner (NEEDS ROY).

## Noted non-blocking residual (B7 — does not halt)

B7's guard-firing **logic** is deterministically verified (pathological escalates, reducing does not). The
guard's *input* — the child/parent leaf-count / work-size ratio — is a **subjective model estimate** in the
wild. The conformance dry-run **stipulates** the granularity in the fixture (which is exactly what the
criterion's "a fabricated pathological node whose decomposition reproduces roughly the same granularity"
asks for), so the governed path (the ≥0.8×-over-two-levels discrimination) IS exercised. The *reliability
of the estimate itself* is a characterization concern the criterion does not gate — analogous to the
criteria's own coverage-note on the completeness-critic false-negative *rate* (capability proven, rate not
characterized). Recorded here for the gate-7 watch list; **not** a blocking stop-for-human.

## Verdict

**CONFORMANCE: PASS-WITH-FLAGGED-PENDING.** Freeze-verify MATCH. All structural gating criteria (S1–S7,
SC1, SC2) verified; the founding-failure pair (B1 floor + B1b generative) — the load-bearing test — passed
faithfully with real independent cold agents (3/3 each), including the checkbox-sweep-would-pass and
intact-twin discriminations; B2 total-coverage caught root + between-child-seam holes at the owning
orchestrator (3/3); B3/B4/B5/B7 verified (B5 executed, B3/B4/B7 representative). **No real skill defect.**
**One gating criterion (B6) is PARTIAL** — its restart + dispatch-level context-economy are verified, but
its live cross-process context-isolation claim is not exercisable by this harness and was **relayed verbatim
as a stop-for-human**; the harness did not self-accept it.

**→ RESOLVED BY OWNER RISK-ACCEPTANCE (2026-07-24).** The owner selected the named-risk-acceptance route
(option b) over building a heavier live-introspection harness. See the ratification record in
`decisions.md` ("Stage 8 — owner risk-acceptance of the B6 residual"). **Final stage-8 verdict:
CONFORMANCE PASS** with B6's live-isolation residual carried as a *named, owner-accepted* known
limitation — not an unverified silent gap.

## `decisions.md` gating dispositions (to append at gate 8)

Each gating criterion's disposition: S1–S7, SC1, SC2 = verified; B1, B1b, B2, B3, B4, B5, B7 = verified
(method as tabled); **B6 = PARTIAL — restart + dispatch-level context-economy verified; live
cross-process-isolation residual OWNER-RISK-ACCEPTED (Roy, 2026-07-24, verbatim + source recorded in
`decisions.md`)**.
