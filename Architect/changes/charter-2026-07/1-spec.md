# Stage 1 — Spec

**Run:** `charter-2026-07`. **Element 1 of 6:** the Architect red-team charter.

## 1. What is wanted

Produce the **shipped** `Architect/stages/charter.md` — the single copy of Architect's cold-review
discipline, read **verbatim** by every cold reviewer Architect dispatches.

Architect is a fourth sibling in the owner's gated-discipline family (dragonfly = diagnose,
guarded-change = change, data-distiller = distill), owning the verb **plan**. Its whole runtime is one
recursive function, `Node(task, plan, granularity, depth, node_id)`, specified in
`/home/zero/Documents/Architect.md`. Within that function the charter is the text that makes a dispatched
cold agent behave the way the loop needs. It is not a stage file, not a router, not a methodology doc.

## 2. Why the charter is the load-bearing element

`~/Documents/Architect.md` L110:

```
task = Severity(Union(redteam.get_issues));
```

The red-team's output **becomes the next task**. Nothing else drives the loop; there is no separate gate
document. So the charter has three duties no other element can take over:

1. **It terminates the loop.** `Severity()` (L22) returns only blocker|major; when nothing survives,
   `task` is empty and `while(task.empty() == false)` (L62) exits. The reviewer's severity assignment
   *is* the termination signal. An unsevered finding is dropped on the floor by `Severity()`, and a
   systematically inflated one prevents exit.
2. **It prevents infinite regress.** `Architect.md` L1–8 states this as a design property, not a style
   note: the granularity floor bounds three things, and the third is `Spawn_redteam` —

   > `Spawn_redteam` — what counts as "vague"  <-- without this one the red-team MANUFACTURES the
   > problem: "you didn't say how to grip the handle" becomes an issue, the issue becomes the next task,
   > and the loop subdivides toward Manual Samuel while every individual agent behaves correctly.

   The owner ratified the need for a maximum-granularity option at transcript record **1128**
   (verbatim): *"There needs to be an option to specify the maximum granularity. in my
   standing->walking->opening the door example, with no maximum granularity it could end up literally
   scripting every step of that (the game Manual Samuel comes to mind)."* The owner separately ruled
   there is **no backstop iteration cap** (record **1258**, verbatim: *"I think trust the blocker/major
   filter, fix it later if it is an issue."*). With no cap, **the floor as stated in the charter is the
   only thing preventing non-termination.**
3. **It is the only place completeness is enforced.** Architect's founding failure was a plan that
   looked complete and shipped with a whole load-bearing section (a run's output-folder structure)
   silently missing, caught by a human at exit-plan-mode. The owner ruled at record **1175** (verbatim):
   *"regarding redteam: Agreed for the most part, but the new charter should also include the definition
   of three tiered completebess definition"*.

## 3. Who reads it — two callers, both must be served

Both are named in `~/Documents/Architect.md`; a charter aimed only at the first is incomplete.

| Caller | Spec | What it reviews | Consumption of findings |
|---|---|---|---|
| **The plan red-team**, `Spawn_redteam(_task, _plan, _granularity)` | L24; spawned ×3 at L104–107 | the node's `plan` against its `task`, at `_granularity` | `Union` (L20) then `Severity` (L22) → becomes the next `task` (L106) |
| **The split review inside `Divisible(_task, _granularity)`** | L14 | a proposed two-way split: does it cover the whole task, is the seam sound, would either half fall below the floor | "red-teams result (looping until no major issues are found)" — L14 |

`Divisible`'s output is additionally subject to `Human_gate` (L16) at every `depth <= gate_depth`
(default 2), **before children spawn**, because "a bad cut corrupts everything beneath it, so approving
after the fact is worthless." Owner ratified depth-scoping at record **1148** (verbatim): *"The layer the
human gates stop at would depend on how granular the plan is going to be, deeper the plan goes the more
humane gates there'd need to be. At least to the second level should be a safe default."*

## 4. Prior art and its standing

| Artifact | Standing in this run |
|---|---|
| `~/Documents/Architect.md` | **AUTHORITATIVE.** Owner-authored. Disagreement with it is a defect in the artifact, not in it. |
| `Guarded_change/stages/charter.md` @ `8d73e5d` (sha256 `0e73bacf…adc590`, verified — see `0-baseline.md` §0.1) | **THE FORK SOURCE and the stage-0 baseline** (103 lines). Its **19** rules (**B01–B19**) are the regression bar. (Pass 1 inventoried 18 and missed the charter-composition rule at L70–74; **B19** was added at gate-4 pass 1 after all three reviewers found it independently, and two pass-2 reviewers each re-derived the inventory against all 103 lines and found no further miss.) |
| `Dragonfly/stages/charter.md` | **FORK PRECEDENT** for the shape of a provenance blockquote that names what was carried and what was "deliberately not carried" (its L8–12). |
| `Architect/stages/charter.md` (current file on disk) | **UNVETTED DRAFT — NO STANDING.** Hand-written freehand in the main session outside any loop, never cold-reviewed. An **input proposal**. Its rules are inventoried as P1–P12 in `0-baseline.md` §0.4; each is adopted or rejected as a decision this run owns, never inherited. |
| `Architect/ATTEMPT-2-STATE.md` | Resume point. **Agent-written ⇒ inadmissible for owner words.** Used only to locate transcript loci, which were then read directly. |
| The session transcript JSONL | Harness-authored ⇒ **the only admissible source for owner words.** Every ruling quoted in this spec was read at its record index. |
| `~/architect-dogfood-2026-07-24/FINDINGS.md` | Evidence about how cold reviewers actually behaved on this artifact. Cited, and one draft claim was checked against it and **failed** (`0-baseline.md` §0.6). |
| `Architect-Attempt-1/stages/` | **ARCHIVED AND SUPERSEDED.** Read only to see what was tried. Its two-pass structure is what attempt 2 replaces. |

## 5. Constraints

**C1 — Scope is the charter, and only the charter.** Not the spine (`templates/seed/`), not the Layer-2
config contract, not `SKILL.md`, not the methodology doc. Attempt 1's worst pass came from a 2-item scope
becoming 13, with 3 of 9 blockers living in rows the expansion created. A defect belonging to another
element is recorded in `decisions.md` as an out-of-scope note and left alone.

**C2 — Fork fidelity is checkable and is checked.** Every baseline rule **B01–B19** either is still stated in
the shipped charter (CARRY), is stated differently with the difference declared (CHANGE), or is named as
dropped **in the provenance blockquote** (DROP). No silent third category. The draft currently fails this
(it silently drops B15's A/B-harness sub-clause while claiming to carry "every unconditional discipline
bullet" — `0-baseline.md` §0.4).

**C3 — The artifact is a prompt, and prompts are a position-sensitive assembly.** The granularity floor
must be readable **before** the reviewer forms a view on what counts as vague, and the completeness lens
must not be positioned so that another lens can absorb it. Position is load-bearing here, so the position
lens (B16) fires on this very change and a behavior-preservation criterion is owed (stage 1.5).

**C4 — Nothing is described in the present tense before it exists and has been run.** Attempt 1's
iteration cap tripped on a criteria document written about four scripts that did not exist. Every claim
about a checker in `2-plan.md`/`8-harness.md` is written after the checker ran, in the past tense, with
its invocation and output pasted.

**C5 — Any list a check depends on is generated, never retyped.** Attempt 1 shipped hand-typed site lists
that disagreed with the measurement file one directory away.

**C6 — Every gating instrument gets its own mutation test.** This project shipped a bare-`exit 0`
"checker" twice, and once "verified" a checker by running it with no arguments and reading the usage error
as a pass. The clean run and the mutated run each get their exact invocation and exact output pasted.

**C7 — No install.** Nothing is synced to `~/.claude/skills/architect/`. Attempt 1 sat installed and
triggerable for an hour after its dogfood found a blocker.

**C8 — No commit.** The orchestrator commits.

**C9 — Owner rulings are re-verified, never inherited (RAT1/RAT2).** Every ruling cited above was read at
its transcript record. Where a recorded ruling is narrower than the design it is offered to support, the
gap is declared as an **author decision** rather than reported as owner authority. This project already
produced one inflation ("means nothing" → cap-bounce immunity the owner never granted,
`ATTEMPT-2-STATE.md` §6); the specific live instance in this run is D1 in `0-baseline.md` §0.5 — record
1175 ratifies *including the three-tier definition* and says nothing about *lens-vs-bullet placement*.

## 6. What the shipped charter must contain

Derived from §2–§4. Each item traces to a source; the criteria document turns these into checkable form.

| # | Content | Source |
|---|---|---|
| S1 | A **provenance blockquote** naming the fork source **and its commit**, stating what was carried and what was **deliberately not carried**. | Dragonfly precedent L8–12; C2 |
| S2 | The **reviewer constitution** — cold, independent, no shared context with the author; read access to the artifact **and** the underlying source; source access load-bearing. | B01 |
| S3 | The **granularity floor**, stated as a safety property, positioned **before** the lenses. | `Architect.md` L1–8, L28; record 1128; C3 |
| S4 | **Six separate lenses**, with the separation rationale. | B02–B07 + record 1175 |
| S5 | The **three-tier completeness definition** — (i) universal spine, (ii) Layer-2 required sections, (iii) generative sweep for what neither list names — with tier (iii) named as the decisive one. | record 1175; founding failure |
| S6 | **Every finding carries a severity**, and an unsevered finding is unusable. | `Architect.md` L26, L28 |
| S7 | The **severity model stated in this file** (blocker/major/minor/nitpick) with the loop meaning: blocker|major become the next task; minor|nitpick are recorded, not looped on. | `Architect.md` L26, L110; closes the fork source's dangling "(below)" (`0-baseline.md` §0.2) |
| S8 | **Union, not majority vote** — file it even if you think you are alone; nothing filed is discarded. **With no unsourced statistic.** | `Architect.md` L24; `0-baseline.md` §0.6 |
| S9 | The **carried discipline bullets** — cite-or-it-doesn't-count, flag-the-unverifiable, no-issue-found-is-valid, earned-clean factual, earned-clean fidelity, spot-verify citations (with a **named consumer**), provenance record + closed set, graded on precision. | B08, B10–B15, B18 |
| S10 | An **earned-clean clause for the completeness lens**. | D2 (author decision, pattern-extended from B12/B13) |
| S11 | The **two conditional lenses** — position/order sensitivity, concurrency — re-aimed at the plan under review. | B16, B17 |
| S12 | **The two callers**, each with its own aiming. | `Architect.md` L14, L28; §3 |
| S13 | **"3 independent cold agents" defined** as three separately-spawned subagents. | record 55; `Architect.md` L104–107; dogfood F9 |
| S14 | The **demotion rule, ported from guarded-change verbatim**: contest a severity **only** via a logged `decisions.md` entry; demoting a **blocker or major** additionally requires the **human tie-break**; a silent unilateral demotion is a **gate violation** and the reviewer's routing stands. Plus SEV2: a borderline/tradeoff call is a **human decision**, surfaced ranked, not an automatic restart. | **Owner-ratified**, record **1449** item 2. Source carried: `stage-4.md` **L34–36** (SEV3) + **L26–28** (SEV2). D10. |
| S15 | **`Union` performs the citation spot-verify**, and a finding whose citation does not resolve is **marked unsubstantiated and does not pass to `Severity` as blocker\|major**. Stated together with B10 ("flag the unverifiable") so the two read as one discipline. | Owner-ratified placement, record **1449** item 3; disposition is the orchestrator's declared elaboration. D11. |
| S16 | **RAT1 and RAT2 stated inline as operative duties** — RAT1: a ratification is audited as an artifact (flagged axis + options verbatim; owner's response verbatim **with a durable source the author did not author**; a mapping showing those words select the recorded option *on the flagged axis*); a ruling built on a **partial or adjacent** answer — especially one resolved into the author's own recommended option — is **not ratified** and the axis is **re-asked, not defaulted**. RAT2: an elaboration introducing operative commitments not present in or entailed by the ratified phrase is **unratified inflation**, untrusted until confirmed. **No pointer to `stages/stage-3.md`.** | D12. Source carried: `Guarded_change/stages/stage-3.md` L55–82 (CH11/CH12). |
| S17 | The **charter-composition rule** — the core is given **verbatim**; each caller's aiming is an **addition, quoted as such**; a **conditional lens is given only when its trigger fires**. | Carried baseline rule **B19** (fork source L70–74), added to the inventory at gate-4 pass 1. D8. |
| S18 | **B18 is the charter's final line.** | D9 (position lens). |

## 7. What it must NOT contain

| # | Exclusion | Why |
|---|---|---|
| X1 | The **"~85% singleton rate"** or any measured recall statistic. | Unsourced. Verified absent from both `FINDINGS.md` and `LOOP-STATE.md`; the convergence counts `FINDINGS.md` does record run the other way (`0-baseline.md` §0.6). |
| X2 | The **UNVETTED DRAFT banner**. | The shipped artifact is the loop's output; the banner marks an input. |
| X3 | Any reference to attempt 1's **two-pass** structure as current. | Replaced by one pass whose findings become the next task (`Architect.md` L102–111). |
| X4 | Content owned by another element — spine section names as normative text, the config contract's field list, router/stage plumbing. | C1 |
| X5 | Present-tense description of any instrument not yet built and run. | C4 |
| X6 | The dogfood's **differential-prompt mechanism** (hand each critic a different plan-type's `required_sections`), and any other motive or mechanism derived from `FINDINGS.md`. | **Owner-ratified exclusion**, record **1449** item 5: *"That thing was for the old version, discard it."* D13. Recorded as **declined**, not overlooked — the escalated question was answered. |
| X7 | Any pointer to a `stages/*.md` file Architect does not have. | S16/D12: the charter is self-contained; `ls Architect/stages/` returns `charter.md` only. Same defect class as the fork source's dangling "(below)". |

## 8. Expected touched files

This list joins every cold reviewer's context (the charter's closed-set rule).

| Path | Change |
|---|---|
| `Architect/stages/charter.md` | **rewritten** — the shipped artifact |
| `Architect/changes/charter-2026-07/0-baseline.md` | new (exists) |
| `Architect/changes/charter-2026-07/1-spec.md` | new (this file) |
| `Architect/changes/charter-2026-07/1.5-criteria.md` | new |
| `Architect/changes/charter-2026-07/2-plan.md` | new |
| `Architect/changes/charter-2026-07/3-redteam-plan.md` | new |
| `Architect/changes/charter-2026-07/6-redteam-code.md` | new |
| `Architect/changes/charter-2026-07/8-harness.md` | new |
| `Architect/changes/charter-2026-07/decisions.md` | new |
| `Architect/changes/charter-2026-07/oracles/*` | new — checker + mutation self-test |
| `Architect/changes/charter-2026-07/fixtures/*` | new — behavioral-arm fixtures |
| `Architect/changes/charter-2026-07/records/*` | new — verbatim cold-review records |

**Explicitly NOT touched:** `Architect/templates/seed/*`, `Architect/examples/*`, `Architect/README.md`,
`Architect/ATTEMPT-2-STATE.md`, `Architect/guarded-change.architect.md`, anything under
`Guarded_change/`, `Dragonfly/`, `Architect-Attempt-1/`, and anything under `~/.claude/skills/`.

## 9. Ratification records

**Pass 1 had none.** Gate-4 pass 1 escalated six findings to the owner; five were answered in a single
turn, and those answers are now **ratification records** owed the full RAT1 treatment. Each is recorded
below in RAT1's own shape — flagged axis, options presented, owner's verbatim response **with a durable
source the author did not author**, and the mapping — because RAT1 is a rule this run is about to inline
into the shipped artifact (S16), and a run that states a discipline it does not practise on its own
rulings has not earned it.

**Durable source for all five: transcript record 1449**, in the harness-authored JSONL
`~/.claude/projects/-home-zero-…/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`. It is **spot-checkable** —
`sed -n '1449p'` — which is what RAT1 requires and what distinguishes this from a re-typed "verbatim" with
no locus. The runner read it at that index directly; it was not taken from the relay.

| # | Flagged axis | Options presented | Owner's verbatim response (record 1449) | Mapping | Verdict |
|---|---|---|---|---|---|
| **R-1** | BL-1: proceed to re-plan, or review direction first? | (a) re-plan and carry on; (b) owner inspects first | *"That wasn't a call that warranted my attention at all, its literally a blatant flaw in a test either you or the agent created, nothing to do with whats actually being created. the answer is obvious, if the experiment is to test where the granularity floor should sit, than the experiment should actually try moving the floor."* | Selects (a) **and rejects the escalation itself** as unwarranted. Prescribes the fix directly. | **Ratified.** → D14, arm B-5 |
| **R-2** | H-A: how does the demotion rule reach a human? | (a) drop it; (b) add a human-interrupt to the spec; (c) reviewer-facing discipline only | *"It gets implemented however it is implemented in guarded-change; that is what the instruction was: copy over the severity mechanism from guarded change."* | Selects **none of the three** — a fourth option (port the source verbatim). **Not** resolved into the runner's recommended (a). Disambiguates the axis. | **Ratified.** → D10 |
| **R-3** | H-B: who spot-verifies citations, given `Union` "discards nothing"? | (a) reviewer self-duty; (b) `Human_gate`; (c) a new spec step; (d) declare unimplementable | *"That \*was\* part of what Combine did, but you said nothing could get discarded, make up your mind."* | Selects **none of the four** — locates the duty at the merge step (`Combine` → `Consensus`+`Union`) and identifies the contradiction as the runner's own misreading. Disambiguates *placement*. | **Ratified on placement.** ⚠ **RAT2:** the *disposition* mechanism is the orchestrator's elaboration, declared at D11, **not** owner authority. |
| **R-4** | H-C: inline RAT1/RAT2, cut the pointer, or is there a stage-file element? | (a) inline ~30 lines; (b) one-line summary; (c) an element I don't know about | *"I don't know what the fuck rat1/2 even ARE."* | **Selects nothing on the flagged axis.** Under RAT1 this is a **non-answer**, not a partial one — and correctly so: RAT1/RAT2 are guarded-change internals, never owner vocabulary. The axis was **not defaulted into the runner's recommendation**; it was reclassified as research owed. | **NOT a ratification.** D12 is an **author/orchestrator decision**, recorded as such. |
| **R-5** | H-F: carry the dogfood's differential-prompt mechanism? | in / out | *"That thing was for the old version, discard it"* | Selects **out**, unambiguously. | **Ratified.** → D13, X6 |

**RAT2 sweep over these five.** Two elaborations were checked for unratified inflation and both are
declared rather than absorbed: **R-3's** disposition rule ("marked unsubstantiated, does not pass as
blocker|major") is not in the owner's words — declared at D11; **R-4** carries no owner authority at all —
declared at D12. Nothing else in D8–D14 claims owner authority it does not have.

**The pre-existing design rulings** quoted in §2–§3 (records 55, 1128, 1148, 1175, 1258, 1274) are not
closures of escalated findings. Each was read at its index during stage 0, and all three cold reviewers
independently re-verified all seven quotes as character-exact. Two reviewers additionally supplied the
**presented options** that pass 1 had asserted-but-not-shown for record 1175 — records **1124** and
**1171**, in which the author twice proposed *folding the sixth lens away*. Those records **strengthen**
D1's independence claim: the owner was twice shown the fold-it option and asked only that the *definition*
survive. **D1 stands, and now shows its work** — see `0-baseline.md` §0.5.

One correction to a pre-existing ruling's citation, from reviewer B-F04: record **55**'s *"option be
should be done by three independent cold agents"* attaches to option (b) of record **51**, which is the
**cold completeness-critic pass** — not the general adversarial red-team, whose three agents come from
**item 6** of the same owner message. S13's generalisation to all red-team spawns is independently
supported by `Architect.md` L104–107 and by item 6, and is cited to those rather than to the wrong half of
record 55.
