# Stage 2 — Plan (PASS 2, revised after gate-4 pass 1)

**Run:** `charter-2026-07`. How the shipped `Architect/stages/charter.md` will be built, how each criterion
in `1.5-criteria.md` will be measured, what instrumentation must exist, and the thresholds that route the
gates.

**Tense notice (C4).** Nothing here has been built. `oracles/check.sh`, `oracles/mutation-test.sh`,
`oracles/rules.tsv`, `oracles/forkdiff.sh` and every fixture are **planned**, described in the future
tense. Their real invocations and outputs appear, in the past tense, only in `8-harness.md`.

---

## 1. Build approach

### 1.1 Authoring order — position is load-bearing and now tested, not asserted

Pass 1 gave a positional rationale for six of eight blocks and **tested none of them**; its one position
criterion was verified by an experiment that never moved anything. Pass 2 fixes the order **and** tests the
two placements that carry behavioral claims.

| # | Block | Why here | Tested by |
|---|---|---|---|
| 1 | Title + **provenance blockquote** — carried / **changed** / deliberately-not-carried | C-01, C-03, C-03b. Head position mirrors the Dragonfly precedent. Kept **compact**: build narrative belongs in the run folder, not in a prompt every reviewer pays for on every spawn (A's missed-opportunity finding). | C-01/C-03/C-03b |
| 2 | **Reviewer constitution** (cold, independent, source access load-bearing) | B01. Establishes *what the reader is* before telling it what to do. | C-11 |
| 3 | **The granularity floor** | **Before the lenses, deliberately** — a reviewer that meets the lenses first has already formed a view on vagueness before being told the bound. | **UNVERIFIED — B-5 cut.** Placement checked (C-17); effect not measured |
| 4 | **The six lenses** (incl. completeness + its three tiers) | C-04, C-05. One contiguous numbered block, so the separation rationale is structurally true rather than merely asserted. | C-04/C-05, B-2 |
| 5 | **Discipline bullets** — carried set + earned-clean (factual, fidelity, completeness) + provenance/closed-set + **`Union` spot-verify** + **charter composition (B19)** | S9, S10, S15, S17. | C-10/C-11/C-12/C-20 |
| 6 | **RAT1 + RAT2, inlined as operative duties** | S16/D12. Immediately after the discipline bullets because the earned-clean **fidelity** bullet is what invokes them; a pointer to `stages/stage-3.md` would dangle (`ls Architect/stages/` = `charter.md`). | C-21, C-22 |
| 7 | **The two conditional lenses**, each **marked conditional with its trigger** | S11 + **B19/D8**: a conditional lens is *given* to a reviewer only when its trigger fires, so the charter must mark them conditional rather than present them as unconditional discipline. Pass 1 carried them unconditionally — an undeclared CHANGE to B19. | C-13, C-20 |
| 8 | **Severity model** — three **separately excisable** sub-blocks: (8a) severity is mandatory, (8b) the four-level table incl. **"unverifiable"** in the blocker cell, (8c) the **demotion rule** + SEV2 | S6, S7, S14. After the findings-producing material: it is what the reviewer does *with* what it found. **Separately excisable** so a B-3 ablation cannot silently confound a demotion-rule ablation (B-F09). | C-07, C-08, B-3 |
| 9 | **The two callers** + the definition of "3 independent cold agents" | S12, S13. Aiming lands adjacent to the reviewer's task framing. | C-14, C-15 — **text only, B-7 cut** |
| 10 | **B18 — "graded on precision, not body count" — as the FINAL LINE** | **D9.** Its position in the fork source (L103, terminal). Pass 1 appended three blocks after the discipline bullets and displaced it; reviewers A-F10 and B-F13 filed that 2/3 under the position lens, whose own worked example is *"an added tail block displaces the old last element."* | **UNVERIFIED — B-6 cut.** Placement checked (C-23); effect not measured |

**No block's position is behaviourally tested — this is a deliberate change at gate-4 pass 2.** Blocks 3 and
10 carry real behavioural claims (the floor is the only thing preventing infinite regress with no backstop
cap, record 1258; B18 is the only counterweight to finding-inflation in a loop where findings become the
next task). But **relocation cannot isolate position** — moving a block changes two-to-three adjacencies,
not one, found 3/3 at pass 2 — and under the owner's done criteria (record **1572**) a per-element harness
is an instrument, not a gate. So every block's position ships as a **stated design decision with its
rationale, explicitly marked unverified**, and the end-to-end Data-Distiller run is what tests it. **No
fourth attempt at isolating position will be built.**

### 1.2 Sourcing rule for every sentence

Authored against `~/Documents/Architect.md` and the frozen fork source. Where a sentence matches the
unvetted draft, that is a **decision recorded in `0-baseline.md`**, not an inheritance: P1/P3/P4/P5/P7/P10
adopted on independent verification; P2 adopted with placement declared as author decision D1; P6/P8/P9/P11
adopted as D2/D4/D5/D6; **P5-stat rejected** (D7); P12 **superseded by D3′**.

### 1.3 The provenance blockquote's content (C-01, C-03, C-03b)

States: fork source path; commit `8d73e5d`; sha256 `0e73bacf…adc590`; what was **carried** (the five
lenses, the unconditional discipline bullets, both conditional lenses, the composition rule); what
**changed and how** — five lenses → six; the severity model now stated **in-file** rather than by a
dangling "(below)"; the closed set restated **per-caller and conditionally**; and what was **deliberately
not carried** — the A/B-harness-arm supplementary-context prohibition, because Architect's design defines
no A/B harness arms. Naming the DROP is what makes C-03 pass and is the precise defect found in the draft;
naming the CHANGEs is C-03b, which pass 1 checked nowhere.

## 2. Instrumentation to be built

### 2.1 `oracles/rules.tsv` — the generated assertion table (C5)

One row per assertion: `id · site · probe-type · pattern · criterion`. **Generated** by a script reading
the intent table out of `0-baseline.md` — never retyped. Invocation and row count pasted. **The row count
is the generator's output, not a number restated in the criteria** (pass 1 hard-coded 17 against a table of
18). Any row with no mechanical form is listed explicitly as **hand-added, with a reason**, so the
hand-typed subset is visible rather than blended in. **Round-trip check (C's M3-b):** the generator asserts
every gating criterion ID in `1.5-criteria.md` appears in ≥1 row, so a criterion cannot go unprobed.

### 2.2 `oracles/forkdiff.sh` — the independent probe (C-02b)

The fix for pass 1's single point of failure. Diffs the shipped charter against the frozen fork source,
strikes every matched rule span, and **lists the residue**. Its evidence comes from **the fork source**,
not from `0-baseline.md`, so it and `check.sh` fail independently. Had it existed in pass 1 it would have
surfaced B19 — the real fork-source rule the inventory missed, which `rules.tsv` could not have caught
because `rules.tsv` is generated *from* the inventory.

### 2.3 `oracles/check.sh` — the structural checker

- **Input:** a charter path. **Will refuse** to run with no argument; **usage exit code distinct from a
  clean pass**, so a no-argument invocation can never be misread as a pass.
- **Normalize first (planned):** it **will** strip `**`/`*`/backtick emphasis and flatten wrapped lines into one logical line per
  paragraph before matching, so a rule wrapping across a line break cannot produce a false absence.
- **Assertions:** one **positive per-site assertion** per `rules.tsv` row. The three absence sweeps run
  **only as pairs** with their positive assertions and are labelled paired in the output.
- **Positional assertions:** `floor_line < first_lens_line` (C-17) and `b18_line == last content line`
  (C-23) — both emitted as **supporting evidence, explicitly marked insufficient**, because H3 forbids
  satisfying a position criterion by inspection.
- **Output:** one line per assertion — PASS/FAIL, assertion id, criterion id — plus a summary count.
  Non-zero exit on any failure.

### 2.4 `oracles/mutation-test.sh` — the oracle-can-fail self-test, rebuilt

Pass 1's "delete the asserted text" strategy was **tautological**: a string probe always fails when its
string is deleted, so the harness would have reported 100% KILLED while proving nothing about whether a
probe checks a **rule** or a **phrase**. **Will be replaced** with **semantic** mutants (C-M1) — negate the rule, swap
its actor, move it out of its governing section, weaken it to a hedge — each of which **must be** KILLED. A
**survivor** would mean the probe matches a phrase, not a rule; the probe **will be** rebuilt in place (logged, H6).
**Insertion** mutants (C-M2) cover the absence sweeps, for which deletion is undefined. A **negative
control** (C-M3) whose expected outcome is `SURVIVED` ensures the harness is observed printing a non-kill
at least once.

**A survived mutant is a checker defect, not a charter defect** — discard and rebuild in place, logged; not
a loop restart.

## 3. Measurement — how each criterion will be verified

| Criterion | Instrument | Path exercised | Evidence recorded |
|---|---|---|---|
| C-01…C-16, C-18a, C-20…C-24 | `check.sh` + `rules.tsv` | the shipped charter's text at each rule's site | per-assertion PASS/FAIL lines, pasted |
| C-02 (fork fidelity, inventory side) | `check.sh`, generated rows | every CARRY/CHANGE rule's site | pasted; part of the **regression arm** |
| C-02b (fork fidelity, independent side) | `forkdiff.sh` | the fork source itself | residue listing, pasted |
| C-06b, C-09b, C-16b | `check.sh` normalized-absence mode | normalized full text | pasted, labelled paired — never reported without their positive partner |
| C-17, C-23 (text halves) | `check.sh` line-order assertions | heading line numbers | pasted line numbers, **marked insufficient** |
| **C-17, C-23, C-14** | **NONE — behavioural verification CUT** | — | `8-harness.md` reports each as **not verified**, with its reason. Never a pass. |
| B-1…B-4 | 2 arms × **n=1** | reviewer behavior | full provenance records, one file per arm |
| C-M1…C-M4 | `mutation-test.sh` | the checker itself, per mutant | **exact invocation** + **exact output**, clean and mutated |
| C-18b, C-19 | reading + `wc` | — | reported as observations |

**H3 and the position criteria — the honest statement.** C-17 and C-23 are position-lens criteria, and H3
says such a criterion is satisfied **only by execution**. **Nothing in this run executes them.** Pass 1
claimed H3 compliance for an experiment that could not vary position; pass 2 built one that varied position
but could not isolate it (3/3). Rather than a third claim, the run now says plainly: **the line-order
assertions check *placement*, not *effect*, and C-17/C-23 ship UNVERIFIED with their rationale stated.**
Under record 1572 that is the correct output — the end-to-end Data-Distiller run is what tests them.

**Ordering constraint (H6).** Part-A results are `verified = no` until `mutation-test.sh` has run and its
output is on disk. `8-harness.md` is written **after** the self-test, and the self-test output is pasted
**before** any Part-A verdict is stated.

## 4. Behavioral-arm protocol — REDUCED AT GATE-4 PASS 2

**Standing rule now in force: when a per-element harness bounces twice, cut it — do not strengthen it.**
Authority: owner's done criteria, transcript record **1572**. A per-element harness is an **instrument, not
a gate**; the end-to-end run producing a detailed Data-Distiller plan is what proves the charter.

- **8 cold agents** — the **four** arms the Layer-2 config mandates (B-1…B-4) × 2 arms × **n = 1**. Down
  from 28. Each a separately spawned subagent, no shared context with this runner or each other.
- **Deleted outright:** the n=2 run count, the within-arm agreement rule, the pass-rate machinery, the
  one-rebuild bound, model pinning, and arms **B-5 / B-6 / B-7**.
- **Each arm receives exactly two things:** its fixture and its charter copy. **Exception, declared:** B-4's
  arms both receive an identical minimal peer-existence statement outside the ablated text, or the ablation
  removes the arm's only reason to believe peers exist and runs backwards.
- **Variable per criterion:** fixture-varying for B-1 and B-2; **charter-ablating** for B-3 and B-4. The
  severity block stays **separately excisable** (mandatory-severity rule / table / demotion rule) so a B-3
  ablation cannot confound a D10 ablation, and the charter pair is **diffed and the diff pasted**.
- **A non-discriminating pair is reported as "did not discriminate"** — not as a pass, and not as a rebuild
  loop. There is no rebuild allowance, because there is no longer a bar a rebuild would be chasing.
- **Records** (`records/<criterion>-<arm>.md`) embed all five provenance elements; existence verified by a
  pasted path check before the run proceeds, extended to the stage-3/6 reviewer records.
- **No diff-against-the-original oracle, ever.** Record 1572: the bar is *"equivalence or better, not
  sameness"*. Nothing in this run compares an Architect output to the artefact a human originally produced.

## 5. Cold-review protocol (stages 3 and 6)

- **Three separately-spawned cold agents** per stage, across **two models**, no shared context.
- **The draft-standing instruction is now stage-scoped**, matching the config as amended at `d044654`:
  before the build this path holds the **unvetted draft with no standing**; after the build it holds
  **this run's output**, reviewed on its merits, and **the banner's presence is the discriminator**. Pass 1
  would have told stage-6 reviewers to discount the very artifact they were reviewing (B-F14); the
  orchestrator fixed the config, and the reviewer prompts follow it.
- Each reviewer receives the charter core verbatim, the stage-3 additions (CH8, CH9/CH10, CH11/CH12), the
  closed-set context list, and the priority-ordered `redteam_context` paths — **now including the Layer-2
  config and the guarded-change stage files** that the artifacts' rule-ID citations resolve to, so a
  reviewer is not forced to choose between an out-of-set read and marking most authority citations
  unverifiable (B-F24; all three pass-1 reviewers hit this and all three declared it, correctly).
- Records are **verbatim** with all five provenance elements. **A sample of every reviewer's citations is
  spot-verified** — pass 1 ran 9 such checks, confirmed 9, and falsified three of the runner's own claims
  in the process. An unearned clean verdict is not accepted.

## 6. Thresholds and routing

Routing is by the **reviewer's** stated severity (SEV3), worst finding first.

| Worst finding | Gate 4 | Gate 7 | Gate 8 |
|---|---|---|---|
| blocker | → stage 1 | → stage 5 | → stage 1 |
| major | → stage 2 | → stage 5 | human call |
| minor | fix in place, proceed | fix in place, proceed | fix, proceed |
| nitpick | log, proceed | log, proceed | log, proceed |

**Escalation standard (set by the orchestrator at gate 4, binding for the rest of this run).** Halt for the
owner **only** when the answer exists nowhere but in his head — a genuinely novel design choice, a scope
change, or accepting a risk in his name. Do **not** halt for: a defect in measurement apparatus this run or
its orchestrator built; anything answerable by reading `Guarded_change/`, `Dragonfly/`, `Data-Distiller/`
or `~/Documents/Architect.md`; a term not yet looked up; or a tension introduced by over-reading a rule.
**Research first, halt only on the residue.** Pass 1 escalated six items; four were research owed, one was
a flaw in a test this run built, and exactly one genuinely needed the owner.

**Iteration cap.** After **2 bounces at the same gate on the same finding class** (same gate number + same
targeted artifact section, regardless of wording), the loop stops and the human breaks the tie. **Current
count: 1 bounce at gate 4** on class {gate 4 · `1.5-criteria.md` position criterion}. A second bounce on
that class trips the cap.

**Harness routing.** A failed **gating** criterion at stage 8 blocks "done". A survived mutant is a checker
defect (rebuild in place, log). A non-discriminating pair is a fixture defect **once** (rebuild, log), then
`verified = no` and surfaced. None is silently folded into a pass.

## 7. Criteria freeze

On gate 4 routing to build, `1.5-criteria.md` freezes and its sha256 is recorded in `decisions.md`. Stage 8
re-checks the file still matches. Gate-4 in-place fixes are traceable to logged findings with diffs
recorded.

## 8. Risks this plan carries, named

| # | Risk | Mitigation |
|---|---|---|
| R1 | The behavioral arms are the expensive, skippable part. | The pass rule makes a partial run worthless by construction: without both arms and both runs there is no verdict, only `verified = no`. |
| R2 | ~~28 arm agents is a large budget.~~ **RESOLVED by cutting the harness** (record 1572). Now 8. Reviewer E's finding — that R2's old mitigation had "no path to done, only a path to a halt" — was correct and is what the cut answers. |
| R3 | `rules.tsv` generation could be a heredoc of retyped rows in disguise. | The generator reads `0-baseline.md`; invocation + row count pasted; non-generated rows listed with reasons; round-trip check against the criteria IDs. |
| R4 | **C-17 and C-23 ship unverified.** | Stated plainly, in `8-harness.md` and in `1.5-criteria.md` Part B, with the reason. Never reported as a pass. The alternative — a fourth attempt at an experiment three reviewers showed cannot discriminate — is the failure mode record 1572 exists to stop. |
| R5 | Scope creep into elements 2–6. | C1; out-of-scope findings recorded in `decisions.md` (OOS-1…OOS-7). The criteria set grew because **the red-team's findings became the next task**, which is the loop working — but C-18a exists to catch the version of this that is drift. |
| R6 | A cold reviewer mis-reads the artifact's standing at stage 6. | §5: stage-scoped instruction, banner as discriminator, matching the amended config. |
| R7 | The severity block's three sub-blocks must stay **separately excisable** or B-3's ablation silently confounds. | Enforced by the pasted charter diff: exactly one rule removed. |
