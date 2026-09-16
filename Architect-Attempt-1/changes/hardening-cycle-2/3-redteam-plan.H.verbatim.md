# Cold red-team record — FRAME H (the predicate hunt + correctness of the 86 sweep answers)

**Verdict: BLOCKER.** Four blockers, six majors. **The sixth no-ID predicate exists** (two of them, in
fact), and separately the sweep's *instrument* is not total: I mutation-tested two ways a predicate can
leave the 86-row table with `SWEEP: OK` still printing and exit 0.

---

## 1. PROVENANCE

### 1.i The charter I was given, quoted verbatim

> You are a COLD RED-TEAM REVIEWER. You have no shared context with the author of the artifacts you are
> reviewing, and you must not acquire any. Do not read any other reviewer's record. Work only from the paths
> listed below.
>
> Write your VERBATIM record to exactly this path (absolute), and do not finish until the file exists on disk:
> `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/changes/hardening-cycle-2/3-redteam-plan.H.verbatim.md`
>
> ## YOUR FRAME (yours alone — two other reviewers hold different, disjoint frames)
>
> **FRAME H — THE PREDICATE HUNT, and the correctness of the 86 sweep answers against source.**
>
> The plan under review contains a sweep table with 86 rows. Its row set is generated: 21 baseline mnemonic
> rule IDs + 60 criterion ids + **5 predicates that carry no rule ID at all** (`closed-input-set`,
> `stage-done-iff-output-exists`, `path-validation`, `catalog-pending`, `run-end`). The plan states, in its
> own words, that an ID-driven generator is **structurally blind** to that last category, that **three of the
> previous pass's nine blockers were hiding in exactly that blind spot**, and that **if a sixth such
> predicate exists no generator in this cycle will find it.**
>
> **That is your assignment. Find the sixth.**
>
> 1. **Read the artifact's stage files, charter, METHODOLOGY and templates looking for PREDICATES, not for
>    IDs.** A predicate is any place the skill says a thing *must be true*, *must exist*, *is done iff*, *is
>    treated as un-run*, *blocks*, *cannot proceed*, *is a config error*, *must be recorded*, *is
>    overwritten*, *is vacuously satisfied*. For each one you find, ask: does it have a mnemonic rule ID?
>    does it appear in the 86-row table? If the answer to both is no, you have found one. Enumerate
>    exhaustively; a list is better than a paragraph.
> 2. **For every predicate you find (in the table or not), test the three questions against SOURCE:**
>    - **(a) Producer** — what step writes the fact this predicate reads, and does that step provably run
>      *before* the reader? Watch for a producer positioned *after* its reader; that is the defect class that
>      has recurred in every pass of this project.
>    - **(b) Degenerate case** — is the predicate defined at **n = 1**, at the **root node**, on the **first
>      run**, and on an **empty tree**? A predicate undefined at its degenerate case is the same defect as
>      one with no producer.
>    - **(c) Counterpart** — does every *acquire / open / begin / stage / dispatch* have its *release / close
>      / end / commit / discard* named, **including on the failure path**?
>    **⚠ IMPORTANT: this three-question framing is an ORCHESTRATOR PROPOSAL, not an owner requirement (see R7
>    in LOOP-STATE.md). Use it as a working aid. If the documents cite it as something the owner requires,
>    that itself is a finding.**
> 3. **Audit the 86 authored answers against source.** They are in `oracles/sweep-answers.tsv` and rendered
>    in `2-plan.md` §1. You cannot check all of them deeply, so choose adversarially: the ones asserting a
>    producer runs earlier, the ones claiming a degenerate case is "stated", and the ones whose verdict is
>    `OK` (an `OK` on a row nobody previously examined is the likeliest place for a wrong answer). **Quote
>    the source line that confirms or refutes each answer you check.** An answer whose (b) column ends in the
>    word "stated" but which **no criterion pins** is a specific defect worth naming — roughly half of the
>    previous pass's answers had that shape.
> 4. **Two rows are claimed to fix live defects. Verify or refute both:**
>    - `closed-input-set` — the charter's five-member closed set with *"a record missing any of these = the
>      review is treated as un-run"*. Is it true that the parent plan is absent at the root, child seams
>      absent at a leaf, and carried-forward findings absent on a first pass because the gate log's first
>      writer is stage 5? Check the actual stage ordering in the artifact. Does the claimed carve-out
>      actually cover every unproducible operand, or does one survive?
>    - `run-end` — the plan says run end is not a stage, and that if the human never answers the assembly
>      gate the run has no end. Is that reasoning sound, and is anything else downstream of "run end" left
>      dangling?
> 5. **Check the sweep's own instrument.** `gen-sweep-rows.sh` + `sweep-answers.tsv` + `gen-sweep-table.sh`:
>    is totality genuinely enforced, or can a predicate leave the table quietly? Run them.
>
> ## SEVERITY MODEL (route on YOUR stated severity; do not soften)
> - **Blocker** — wrong problem / will not work / unverifiable as planned.
> - **Major** — sound goal, materially wrong approach.
> - **Minor** — real but local, fixable in place.
> - **Nitpick** — style/clarity.
> State a severity for every finding. Rank them. Precision matters more than volume.
>
> ## EVIDENCE DISCIPLINE (enforced)
> - **Every factual claim carries a citation you actually verified** — `path:line`, quoted. A fabricated or
>   unchecked citation makes your whole record un-run.
> - **A clean verdict must be EARNED.** If you find no sixth predicate, you must show **the enumeration you
>   performed** — which files you read, what pattern of language you searched for, and the full list of
>   predicates you found with their disposition. An unsubstantiated "the sweep looks total" is treated as
>   un-run and re-run.
> - Distinguish observation from inference.
> - If you cannot verify something, say "unverified" and why.
>
> ## REQUIRED SECTIONS IN YOUR RECORD (missing any ⇒ your review is treated as un-run)
> 1. **Provenance** — (i) this charter, quoted; (ii) the exact list of paths you read; (iii) your agent type
>    + model; (iv) `sha256sum` of `1-spec.md`, `1.5-criteria.md`, `2-plan.md`, `oracles/sweep-answers.tsv` as
>    you read them; (v) `spawn_id`: report the identifier your harness exposes, or write exactly
>    `spawn_id: unavailable-by-harness` — **do NOT invent one.**
> 2. **THE PREDICATE ENUMERATION** — the full list, with, per predicate: where it is stated, whether it has a
>    rule ID, whether it is in the 86-row table, and its disposition. This is the core of your record.
> 3. **Findings**, each with: id, severity, one-line claim, citation, and why it matters.
> 4. **COVERAGE CHALLENGE (CH8)** — behaviours this change could plausibly alter that **no criterion
>    observes**, each with a concrete scenario, ranked. An earned "none found" counts. No such section ⇒ lens
>    4 un-run.
> 5. **LABEL AUDIT (CH9/CH10)** — per gating criterion you sampled, which governed path it actually observes
>    and what evidence you checked. Challenge any that observes a proxy rather than the governed behaviour.
>    Unsubstantiated clean ⇒ un-run.
> 6. **WHAT THE PASS GENUINELY EARNED** — specific and fair.
>
> ## THE ARTIFACTS UNDER REVIEW
> - `.../1-spec.md` · `.../1.5-criteria.md` · `.../2-plan.md` ← §1 is the 86-row sweep. **Your primary
>   target.** · `.../oracles/sweep-answers.tsv`, `.../oracles/gen-sweep-rows.sh`,
>   `.../oracles/gen-sweep-table.sh`, `.../oracles/criteria.tsv`
>
> ## CONTEXT (priority-ordered; a closed set — read these, quote them rather than paraphrasing)
> 1. `.../Architect/` — the ARTIFACT: `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/charter.md`,
>    `stages/stage-1-…` … `stages/stage-8-…`, `templates/seed/*`, `examples/authoring-a-skill/*`. **This is
>    where the predicates live. It is deliberately UNEDITED — `git diff` over it is empty, HEAD `b08f5a9`,
>    the build has not happened.** So you are auditing whether the PLAN's answers are true of the artifact's
>    rules, not whether the artifact already carries the new sentences.
> 2. `/home/zero/architect-hardening-loop/LOOP-STATE.md` — owner ratifications R1–R7. **R7 in particular:
>    the three-question checklist is an orchestrator proposal, NOT an owner requirement; R4's ratified
>    content is the owner's one sentence.**
> 3. `.../3-redteam-plan.pass2.md` and `.../3-redteam-plan.md` — the two previous reviews. **Findings D/1,
>    D/2, D/3, D/4, D/6, D/12, D/18 are especially yours** — confirm closure or refute it rather than
>    re-deriving.
> 4. `.../Guarded_change/stages/charter.md` and `stage-3.md` — the charter you operate under. It binds you.
> 5. `.../0-baseline.md` — the measured baseline, including the 21 live rule IDs vs 18 index rows.
>
> ## SCOPE — do not report these as defects; they are DECLARED out of scope by owner ruling
> F1 (join/up-flow/`_status.md` schema/bottom-up assembly/F6), F2, F5's mechanism, DIV, the cost/fan-out
> envelope, ECON's O(children²), the "two passes" ruling. **F8 (the assembly human gate) IS ratified IN
> scope** — do not flag it as a scope violation. An out-of-scope problem is recorded as a carry-forward, not
> a blocker. But note: a predicate the plan says it FIXED, which is not actually fixed, is fully in scope no
> matter which deferred item it touches.
>
> Be adversarial, be exhaustive in the enumeration, and earn every clean verdict. Write the file before you
> finish.

*(No supplementary author-authored context was supplied to me beyond the above. Per the charter's closure
clause I record that explicitly.)*

### 1.ii Exact list of paths I read

**Artifacts under review**
- `Architect/changes/hardening-cycle-2/1-spec.md` (whole)
- `Architect/changes/hardening-cycle-2/1.5-criteria.md` (§1 lines 57–176 in full; headings + targeted greps
  elsewhere)
- `Architect/changes/hardening-cycle-2/2-plan.md` (whole)
- `Architect/changes/hardening-cycle-2/oracles/sweep-answers.tsv` (whole, via awk column extraction)
- `Architect/changes/hardening-cycle-2/oracles/gen-sweep-rows.sh`, `gen-sweep-table.sh`,
  `gen-expected-sites.sh`, `lib-corpus.sh` (whole)
- `Architect/changes/hardening-cycle-2/oracles/criteria.tsv` (whole, via awk)
- `Architect/changes/hardening-cycle-2/oracles/expected-sites.txt`, `expected-sites.phantoms.txt`,
  `sweep-table.generated.md` (read/diffed)
- Executed: `gen-sweep-rows.sh`, `gen-sweep-table.sh`, `ruleid-sitemap.sh`, `idcollide.sh`

**The artifact (source of truth for the predicates)**
- `Architect/SKILL.md`, `Architect/METHODOLOGY.md`, `Architect/README.md` (whole)
- `Architect/stages/charter.md` (whole)
- `Architect/stages/stage-1-frame-template-match.md` … `stage-8-restart-resume.md` (all eight, whole)
- `Architect/templates/seed/README.md`, `generic-node.md`, `decomposition-node.md`, `leaf-task-spec.md`
  (whole)
- `Architect/examples/authoring-a-skill/planning.md`, `README.md` (whole)

**Context**
- `/home/zero/architect-hardening-loop/LOOP-STATE.md` (R4/R5/R6/R7 sections)
- `Architect/changes/hardening-cycle-2/3-redteam-plan.pass2.md` (lines 1–120)
- `Architect/changes/hardening-cycle-2/decisions.md` (targeted: CAP determination, D/1 disposition, §sweep)
- `Guarded_change/stages/charter.md` (hashed; the Architect fork at `Architect/stages/charter.md` is what I
  read in full and is what binds the reviewers under review)
- `Architect/changes/hardening-cycle-2/0-baseline.md` (hashed; consulted only via the 21-ID claim as
  cross-checked against `lib-corpus.sh:10` and `expected-sites.txt`)

**NOT read** (per the charter's "do not read any other reviewer's record"):
`3-redteam-plan.{A,B,C,D,E,F}.verbatim.md`, and no other pass-3 reviewer record.

### 1.iii Agent type + model

- **Model:** `claude-opus-5` (Opus 5).
- **Agent type:** not self-observable from inside the harness. I was dispatched as a cold subagent via the
  Agent tool; the `subagent_type` label chosen by my dispatcher is not exposed to me. **Reported as
  dispatcher-observable, not self-reported** — I decline to guess it, per `S-IDN`'s own principle.

### 1.iv sha256 of the artifacts as I read them

| File | sha256 |
|---|---|
| `1-spec.md` | `a9d3cef738408ddcc0033b3ca3e7fb8c036c542dfac8f398bfe2be165e6bd49f` |
| `1.5-criteria.md` (**see note**) | first observed `cd9a217e72ee7b56c9c159f45c3c9cd04a4583e955df54c4ed9c1a1fd025d8c7`; at read + re-verification `1f89851f5a0325c39904288b21e67e4fe8a0871a14f540db6638d0ee7eb0d1c1` |
| `2-plan.md` | `6a7048ab2858356586a76d86aef87687035175fa891d7bf01aa01751bb042d41` (stable across the review) |
| `oracles/sweep-answers.tsv` | `ff21c2c42334576cc0f4cb2e65094d8ec9693993ae09b2f9ca5c905a28236914` (stable) |
| `oracles/criteria.tsv` | `8a36dd2d1e82b62868a1aadc54da7c09bd9e10c9ebaf523c593fa5fb5b10e891` |
| `oracles/gen-sweep-rows.sh` | `070b115b0bff2d013fdd72630dbc375e56f2f0041cfc6bf126dfaf91a7a4df36` |
| `oracles/gen-sweep-table.sh` | `42b84e982512d6ce7e26341b792b73dea9bf745f79f64daa05263e62a0e58ddd` |
| `oracles/lib-corpus.sh` | `d10dc43f219534145bb9c8ec46f2190d5a0d8861f1bc588e664cc098dd108d1f` |
| `Architect/SKILL.md` | `7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450` |
| `Architect/METHODOLOGY.md` | `f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa` |
| `Architect/README.md` | `79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a` |
| `Architect/stages/charter.md` | `6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819` |
| `stages/stage-1-frame-template-match.md` | `ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5` |
| `stages/stage-2-draft-node.md` | `2e76963ce446190ff4bb4d8100a097d8a62e684d5936d38a74e227aea3ad1036` |
| `stages/stage-3-completeness-critic.md` | `6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e` |
| `stages/stage-4-adversarial-redteam.md` | `96570a6d9298c67ab6b5fe8653b16cf7068fdbe547373a32bee3e02c0721f07c` |
| `stages/stage-5-gate.md` | `99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5` |
| `stages/stage-6-granularity-decompose.md` | `b202101b7b4b16314d4742851138b53efe40b33f3025886149f02ba4aeac1993` |
| `stages/stage-7-assemble.md` | `864b74dcfcf43e18b576145327beeb011b1e44bb672f7a10e8d8b0f9ad9cb607` |
| `stages/stage-8-restart-resume.md` | `97431f52e7487ab34c9e9278496b687ca2b4ca2bf178203de3d76151c35762c1` |
| `templates/seed/README.md` | `d2a86068b92d7ee6b47b7af6dd506f456b589a50a6cac7e0e8d15d23246b3fb4` |
| `templates/seed/generic-node.md` | `7148ec60e18b8cf4606b50b0fc8b49f299731b3d3c26a4787bc0a8bf0be52e89` |
| `templates/seed/decomposition-node.md` | `b4509defabe16768edcd024a98f44f37c90351aef5fa759b56b0c0930a98cf64` |
| `templates/seed/leaf-task-spec.md` | `c7341c863a494a41e616e00b70c14bf8034cfe292108e2dca92436847c3f093e` |
| `examples/authoring-a-skill/planning.md` | `b52a22d2012e7a640e68300a2a8f0a985e811e024c0259b26d7d0aabc6ec37ea` |
| `examples/authoring-a-skill/README.md` | `aa52ab3b03b9e78ea7ca977d7dacfac515d8e21dbdd5c2faf97004abb563b600` |
| `3-redteam-plan.pass2.md` | `4eb63586354e77e0d0e490055135c18b28bd3c4b82a83c509f01a0d23209283c` |
| `3-redteam-plan.md` | `953805796fb4d47739467e3556976beb12e3923da06a49ef0dbc8fe95375a5e8` |
| `0-baseline.md` | `b81ae811c80fa12ae9fe457ac3a7606b86000d608185f1c08701324a104a706d` |
| `decisions.md` | `3e68ef5dfc2cef3e1b82df961d671991e5fc74f86192ffa434d761b3fdfddbac` |
| `Guarded_change/stages/charter.md` | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` |
| `LOOP-STATE.md` | `1bee9637c3ac2f7cb4308dbdd27fb375b7d7dd0a7bf33a36646d6893b5240680` |

> **⚠ OBSERVATION — the artifact under review mutated during this review.** `1.5-criteria.md` (mtime
> `2026-07-25 13:11:28 -0400`) and `oracles/criteria.tsv` (mtime `13:08:16 -0400`) were both written
> **after** `2-plan.md` (`13:02:36`) and **during my review window**. I re-hashed and **re-verified every
> load-bearing citation I take from `1.5-criteria.md` and `criteria.tsv` against the post-mutation bytes**
> (`1f89851f…` / `8a36dd2d…`) — the rows I cite (15, 22, 35, 38, 43, 48, and all 8 `P-*` rows) are unchanged
> in substance. `2-plan.md` and `sweep-answers.tsv` were byte-stable throughout. I flag it because a
> reviewer's `sha256` provenance is only meaningful if the artifact holds still, and this one did not.
> **Recorded as an observation, not a finding** — I cannot tell from inside whether the edit was in this
> pass's scope.

**Artifact-unedited claim, verified:** `git log --oneline -1 -- Architect/` → `b08f5a9 architect: cycle-1
hardening records — gate-4 cap tripped, artifact unchanged`; `git diff HEAD --stat -- Architect/` shows only
`Architect/guarded-change.architect.md | 11 +++---`, i.e. **no edit to any of the 18 corpus files.**
`1-spec.md:264-266`'s claim is true.

### 1.v spawn_id

`spawn_id: unavailable-by-harness`

---

## 2. THE PREDICATE ENUMERATION

### 2.0 How I enumerated (so the verdict is auditable, not asserted)

I read **all 16 corpus files** listed in §1.ii in full — `SKILL.md`, `METHODOLOGY.md`, `README.md`,
`stages/charter.md`, all eight stage files, four seed templates, and both example files. I then ran a
modal-language sweep over the pinned corpus for predicate vocabulary:

```
grep -rniE "\b(must|never|cannot|only if|iff|blocked|blocks|is done|refuse|prohibited|is an error|
   config error|is a violation|not optional|always|is treated as|vacuous)\b" \
   SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/     →  91 hits
```

plus targeted sweeps on `empty`, `un-gated`, `deterministic`, `atomic|rename|\.tmp`, `self-certif`,
`domain_context`, `first writer`, `only writer`, `stated`. For each candidate I asked the charter's three
questions and checked membership in the 86-row table by ID string match against
`oracles/sweep-answers.tsv`.

**Result: 2 predicates with no rule ID and no row (the sixth and seventh), 1 with no rule ID and no row but
benign, plus 6 predicates that ARE in the table with a materially wrong answer.** The full list follows.

### 2.1 Predicates with NO rule ID and NO row in the 86 — the answer to the assignment

| # | Predicate | Stated at | Rule ID? | In 86? | Disposition |
|---|---|---|---|---|---|
| **P1** | **`conditional-lens-firing`** — *"**If** the artifact under review is a position-sensitive assembly, test for position/order sensitivity"* and *"**If** the plan introduces a new accessor or a new read-modify-write window over shared mutable state, map the accessors and challenge the guard's scope"* | `stages/charter.md:102-109` and `:110-114`; re-stated at `stages/stage-4-adversarial-redteam.md:19-20` | **NO** | **NO** | **THE SIXTH PREDICATE. Finding H/4 — BLOCKER.** (a) no producer of the firing condition: the reviewer self-assesses it. (b) no degenerate case defined. (c) no counterpart, no record, and — decisively — **no earned-clean clause**, unlike lenses 1/5/6. Both lenses demonstrably fire on *this* artifact (`1-spec.md:243-244`; `2-plan.md` §4) yet nothing requires a record to state whether either fired. |
| **P2** | **`complete-vs-partial-output`** — *"stage-done is an output-exists check on the **complete** deterministic file — a partial `completeness/B.md` is not the final name"* | `stages/stage-8-restart-resume.md:22-24` | **NO** (asserted under `RST`'s heading but is a distinct predicate about write atomicity) | **NO** as a row; **restated as row 83's (c) answer** | **THE SEVENTH. Finding H/11 — MAJOR.** (a) **no producer whatsoever**: nothing in the corpus or the plan specifies write-to-temp-then-rename. `grep -ni "atomic\|rename\|\.tmp"` over `1.5-criteria.md`, `2-plan.md`, `1-spec.md`, `criteria.tsv` returns **only the catalog lock** (`criteria.tsv:33`). A half-written `completeness/B.md` **is** literally named `B.md`. The predicate is circular: "done" is decided by output-exists, and the partial/complete distinction it needs is decided by… nothing. |
| **P3** | **`supplementary-context-quoting`** — *"any supplementary author-authored context **must be quoted in the record as such**"* | `stages/charter.md:98-99` | NO | NO | **NITPICK.** This is the actual *enforcement* content of the closed-set sentence (see H/10) and it has no checker, no ID, no row. Benign in isolation; load-bearing to H/10's reading. |
| **P4** | **`ab-harness-context-prohibition`** — *"In A/B harness arms, author-authored supplementary context is **prohibited outright**… this clause never fires in a normal planning run"* | `stages/charter.md:100-101`, with the never-fires declaration at `charter.md:21-22` | NO | NO | **NITPICK, earned-benign.** A deliberately vacuous predicate, explicitly declared so at the fork blockquote. Cited here for completeness of the enumeration, not as a defect. |
| **P5** | **`config-key-presence` beyond `redteam_context`** — `domain_context`, `scale_context`, `plan_type`, `catalog`, `off_limits_paths`, `run_root` each have a load-bearing consumer, none has a stated absent-key behaviour | `METHODOLOGY.md:67-93` (contract); consumers at `stage-1…md:16-18` (`domain_context`+`scale_context`+`required_sections`), `stage-1…md:11` (`run_root`), `METHODOLOGY.md:74-76` (*"Sets the granularity check's expectation"*) | NO | NO — the class is in the table **only** for `required_sections` (row 5, `DECLARED GAP`) and `redteam_context` (row 35 `S-CTX-VAC`) | **MINOR (H/14).** The plan names this class precisely (`CMP`'s row: *"the same 'an absent config key makes the check pass trivially' class as S-CTX-VAC"*) and then declares it only for `required_sections`. Four other keys of the same class go unmentioned. `domain_context`'s absence is worse than the others — see H/10, it is a closed-input-set operand. |

### 2.2 Predicates that ARE in the table but whose answer is materially wrong

| Row(s) | Predicate | The answer's defect | Finding |
|---|---|---|---|
| **82** `closed-input-set` | premise is a **misreading** of `charter.md:99-100`, and one unproducible operand (`domain_context`) **survives** the carve-out | H/10 — MAJOR |
| **82 / 56** (`S-CLOSED-DEGEN`) | the ordering fact it names — *"the gate log's first writer is stage 5"* — is **falsified by this same cycle's `S-PATHVAL`** | **H/1 — BLOCKER** |
| **16 / 43** (`TPL1`, `S-CNC-TMPL`) | *"stage 1 … **the only writer of that file**"* is false: `plan.md` is stage 2's output | **H/2 — BLOCKER** |
| **19 / 83** (`RST`, `stage-done-iff-output-exists`) | *"**ONE** named exception"* — the real undefined set is ≥ {stage 1, stage 5, stage 6-leaf, stage 7}; and (b) answers 1 of the 4 required degenerate sub-cases | **H/3 — BLOCKER** |
| **1 / 69** (`GBP`, `S-COV-PROD`) | *"empty tree … — **stated at s7**"* — nothing at s7 states it, and the empty tree makes stage 7's conjunction **vacuously true** | H/6 — MAJOR |
| **59 / 62** (`S-RST-RESUME`, `S-HG2`) | the resume exception makes an **HG2 bounce indistinguishable from an unanswered ask** | H/8 — MAJOR |
| **17** (`TPL2`) | verdict `OK` while the operand is *"read at run end"* — the same exposure that makes rows 85/86 `PARTIAL+DECLARED`; and *"MUST NOT TAKE THE LOCK — stated"* is stated nowhere | H/13 — MINOR |
| **19 / 83** | `_status.md` is in the deterministic-filename list while its writer is **deferred (F1)** — an operand with no producer inside a row marked FIXED | H/12 — MINOR |

### 2.3 Predicates in the table whose answers I checked and **confirmed** (the clean half, earned)

| Row | Claim checked | Source line that confirms it |
|---|---|---|
| 4 `PASS-ORD` | *"a node with neither set is un-gated, not 'ordered' — stated at s5"* | `stage-5-gate.md:48-50`: *"a node missing either set is **un-gated**, not clean."* ✓ |
| 7 `SPN` | *"a leaf task-spec compresses the spine but drops nothing — stated in tp/leaf"* | `templates/seed/leaf-task-spec.md:4-5`: *"Nothing is dropped; it is compressed."* ✓ |
| 12 `TOP` | *"the `plan/topgate/` DIRECTORY is created EMPTY by stage 1, so a bare-existence test is self-satisfying"* | `stage-1-frame-template-match.md:12`: *"`plan/topgate/` (empty)"* vs `stage-6…md:17`: *"The approval artifact must **exist on disk** at `plan/topgate/`"* ✓ — the F5 defect is real and correctly characterised |
| 15 `TPL` | *"FIRST RUN: the catalog does not exist"* | `stage-1…md:13-14`: *"If the user-space catalog `~/.claude/architect/templates/` does not yet exist, **seed it**"* ✓ |
| 56 `S-CLOSED-DEGEN` | root has no parent plan / leaf has no child seams | `METHODOLOGY.md:166-170` (delegation begins *"at the first major branch"*, so the root has no parent) and `stage-2-draft-node.md:18-22` (seams exist only *"If it decomposes"*) ✓ |
| 86 `run-end` | *"RUN END IS NOT A STAGE"*; trigger = the recorded approval; no timeout ⇒ no end | Stage index `METHODOLOGY.md:293-302` enumerates exactly 8 stages, none of which is "run end"; `stage-6…md:32-35` puts the catalog commit at stage 6/run end; nothing anywhere states a timeout. ✓ **The reasoning is sound.** |
| 70 / 76 | `S-COV-LIMIT` / `S-F5-LIMIT` as `DECLARED GAP` | `stage-7-assemble.md:28-31` claims total coverage incl. seams with no up-flow mechanism anywhere; `stage-1…md:12` pre-creates `topgate/`. Both gaps are real and correctly labelled **not fixed**. ✓ |
| §1 R7 label | *"the (a)/(b)/(c) framing is an ORCHESTRATOR PROPOSAL, not an owner requirement"* | `2-plan.md:14-19` matches `LOOP-STATE.md:224-231` (*"the ratified content of R4 remains the owner's sentence alone… must not be cited as an owner requirement"*). **No R7 fidelity violation. Earned.** ✓ |
| §1 table provenance | the embedded table is the generator's verbatim output | `diff <(sed -n '77,171p' 2-plan.md) oracles/sweep-table.generated.md` → **byte-identical**; regenerating reproduces it exactly. ✓ |

---

## 3. FINDINGS

Ranked worst-first.

---

### H/1 — **BLOCKER** · Two gating criteria of this cycle contradict each other, and both land in `stage-3`

**Claim.** `S-CLOSED-DEGEN` — the sweep's flagship "live defect fixed" (row 82/56, `2-plan.md:198-205`) —
rests on the ordering fact *"the gate log's first writer is stage 5"*. **This cycle's own `S-PATHVAL`
falsifies it.**

**Citation.**
- `oracles/criteria.tsv` `S-CLOSED-DEGEN`, gating, sites `ch s3`:
  > *"…a node's first pass has no carried-forward findings **because the gate log's first writer is stage
  > 5**"*
- `oracles/criteria.tsv` `S-PATHVAL`, gating, sites `S s3 s4`:
  > *"path-validation runs at run start **and again at every later spawn**, and the list of paths checked
  > plus its result **are recorded in that node's `decisions.md`**"*
- `oracles/criteria.tsv` `S-CNC-GATELOG`, gating: *"**the per-node gate log is that node's own
  `decisions.md`**; `plan/decisions.md` is run-level only"* — so "that node's `decisions.md`" **is** the gate
  log.
- The spawn that records it happens **before** stage 3's reviewers exist:
  `stage-3-completeness-critic.md:62-64`: *"Mechanically check every path handed to a cold agent … **before
  the spawn**"*.
- `1.5-criteria.md:109` and `:129` confirm both rows are `gating`, and both site sets include `s3`.

**Why it matters.** After the build, `stages/stage-3-completeness-critic.md` will carry two sentences that
cannot both be true: one saying the node's `decisions.md` first acquires content at stage 5, the other
requiring stage 1 / the spawning stage to write the path-validation record into that same file. The plan's
own class-α definition (`1-spec.md:74`) is *"a predicate whose operand has no valid producer"*; here the
carve-out **built to close** a producer-ordering defect is justified by a producer-ordering claim that this
cycle's other edit breaks. This is not a wording nit: `S-CLOSED-DEGEN`'s carve-out for carried-forward
findings is *load-bearing for whether every first-pass review is un-run*, and its stated reason is false as
of D4a. Either `S-PATHVAL`'s record moves to a different file, or `S-CLOSED-DEGEN` must stop naming stage 5
as the first writer — the two cannot ship together.

---

### H/2 — **BLOCKER** · `S-CNC-TMPL` pins a false single-writer claim, and the sweep asserts both sides of it

**Claim.** The gating criterion `S-CNC-TMPL` will write into `METHODOLOGY.md`, `stage-1`, and
`templates/seed/README.md`: *"the template used is recorded in that node's own `plan.md` header by stage 1,
**the only writer of that file**."* `plan.md` is **stage 2's** output.

**Citation.**
- `oracles/criteria.tsv` `S-CNC-TMPL` (gating, sites `M s1 tp/README`, `1.5-criteria.md:116`):
  > *"the template used is recorded in that node's own plan.md header by stage 1, **the only writer of that
  > file**"*
- `stages/stage-2-draft-node.md:3`: *"**What this stage does:** produce the node's `plan.md` — the
  **7-section universal spine** filled…"*
- `stages/stage-2-draft-node.md:46`: *"`plan.md` is the node's durable state"*
- `stages/stage-1-frame-template-match.md:20`: *"mark **`plan.md` for instantiation at stage 2**"*;
  `templates/seed/README.md:13-14`: *"instantiate that skeleton **into the node's `plan.md`**"*
- **The sweep asserts the contradiction against itself.** Rows 16 and 43 say stage 1 is `plan.md`'s only
  writer; rows 5, 22, 24, 50, 63 and 75 say stage 2 writes it —
  `2-plan.md:100` (`S-BIND`): *"sha256(plan.md) computed now over **a file stage 2 wrote**"*;
  `2-plan.md:102` (`S-BIND-ONE`): *"one operand, this node's own plan.md, **written by stage 2**"*;
  `2-plan.md:83` (`CMP`): *"the 7 spine sections + Layer-2 list live in plan.md, **written by 2**"*.

**Why it matters.** Two ways.
1. **The guard is invalid.** `2-plan.md:122` states the CNC family's whole mechanism: *"the write-write race
   is closed by **reducing the accessor set to one writer**."* The reduction for `template used` is
   justified by a single-writer claim that is false, so `template used` is moved *into* a two-writer file and
   the race is asserted closed. `S-CNC-INDEX` correctly makes `index.md` derived-and-never-authoritative —
   which means `template used` has **no** authoritative home once its new home's single-writer premise
   fails.
2. **A concrete loss.** Nothing preserves stage 1's header across stage 2's write, and nothing preserves it
   across a **bounce-driven re-draft** (`stage-5-gate.md:12-13`, blocker/major → *"back to stage 2
   (re-draft)"*). If a re-draft rewrites `plan.md`, `template: <name>` is gone, and `TPL3`
   back-propagation — which fires only *"If a finding fixed on this node patched a hole in a section that
   **came from a catalog skeleton**"* (`stage-6…md:32-33`) — can no longer tell that it did. The
   back-propagation path silently stops firing exactly on the nodes that bounced, i.e. the ones with
   hole-fixes worth propagating.

This is also an **R4 under-generalization**: pass 2's D/9 was *"A/F3's fix routed `template used` and nothing
else"*. Pass 3 kept the route and never checked whether the destination has one writer.

---

### H/3 — **BLOCKER** · `S-RST-RESUME` pins *"ONE named exception"* — the real set is at least four, and it is gating

**Claim.** The gating criterion `S-RST-RESUME` writes a **universal quantifier** into `METHODOLOGY.md` and
`stage-8`: *"`stage-done-iff-output-exists` has **one named exception**."* Rows 19 and 83 both repeat it and
both are marked **FIXED**. Mapping the artifact's own deterministic-filename list onto its own eight stages
shows at least **three further stages** whose done-ness that predicate cannot decide.

**Citation.** The list, verbatim, `stages/stage-8-restart-resume.md:13-15`:
> *"**Deterministic filenames → "already produced?" is a path check.** `plan.md`, `completeness/A–C.md`,
> `adversarial/A–C.md`, `_status.md`, `plan/topgate/`, `assembled-plan.md` are fixed names.
> **Stage-done-iff-output-exists** — a node's stage is done **iff** its deterministic output exists."*

Six names for eight stages. Mapping:

| Stage | Its output | Done-decidable? |
|---|---|---|
| 1 frame/template-match | *"Write, into the node's **`plan.md` header**"* (`stage-1…md:15-16`) + `index.md` (`:20`) | **NO.** `index.md` is not in the list; `plan.md` is stage 2's file. After `S-CNC-TMPL` routes `template used` into `plan.md` too, stage 1 owns **no file of its own**. Stage-1-done is indistinguishable from stage-2-partial. |
| 2 draft | `plan.md` | yes |
| 3 completeness | `completeness/A–C.md` | yes |
| 4 adversarial | `adversarial/A–C.md` | yes |
| 5 gate | *"**Append one entry to `plan/decisions.md`**"* (`stage-5-gate.md:19`); after D8, `<node>/decisions.md` | **NO.** `decisions.md` is **not** in the deterministic-filename list, and nothing in the plan adds it (`grep -ni deterministic` over `1.5-criteria.md`/`criteria.tsv` returns only `S-IGM-CLOSED`). The only candidate is `_status.md` — whose writer is **deferred** (see H/12). |
| 6 granularity/decompose | *"Record the final decision in `index.md` / the node's `_status.md`"* (`stage-6…md:11`); `plan/topgate/` | **NO for a leaf** (nothing is written outside `index.md`/`_status.md`); and `plan/topgate/` is pre-created empty (`stage-1…md:12`), the declared F5 defect. |
| 7 assemble | `assembled-plan.md` | the **one named** exception (correctly fixed) |
| 8 restart | not a step (`stage-8…md:3`) | n/a |

**Also: row 83's (b) column answers one of the four degenerate sub-cases.** Verbatim (`2-plan.md:161`):
*"empty node dir = 'not planned yet'. ONE NAMED EXCEPTION: stage 7…"* — no `n=1`, no `root`, no **first
run**, no **empty tree**. And "empty" ≠ "absent": `METHODOLOGY.md:242` covers only *"An **empty node dir**
IS the 'not planned yet' marker"*, while on a first run `tree/root/` **does not exist at all**.

**Why it matters.** This is not a missing statement; it is a **gating criterion that certifies a false
universal**. `1.5-criteria.md:80` — *"Every row is gating"* — plus `2-plan.md:368` — *"All criteria are
gating… **No 'declared deferral' exists in this plan**"* — means the build **passes** by writing *"one named
exception"* into two files. That is the class-β shape (`1-spec.md:75`): the apparatus cannot detect the other
three exceptions and the document asserts there are none. The concrete failure it leaves live is the same
shape as D/6 that item 9 fixed: **restart after stages 3+4 complete but before the gate entry** — all
deterministic outputs present, so `stage-8…md:33-34`'s resume walk (*"walk `tree/` for the first node whose
expected output is missing → resume there"*) finds nothing missing at that node, and the node is **never
gated**. D/6 was fixed at stage 7 and not generalized to stage 5 — which is precisely the R4 remedy the pass
claims to have executed.

---

### H/4 — **BLOCKER** · **THE SIXTH PREDICATE:** the charter's two *conditional* lenses have no producer, no record, and no earned-clean clause

**Claim.** `stages/charter.md` states two obligations that fire **conditionally**, with the condition
evaluated by nobody, recorded nowhere, and exempt from every earned-clean clause. Neither carries a mnemonic
ID; neither has a row in the 86; no criterion in `criteria.tsv` mentions either.

**Citation.** Verbatim, `stages/charter.md:102-109`:
> *"- **If the artifact under review is a position-sensitive assembly, test for position/order sensitivity**
> (lens 4). This fires only where order/adjacency is itself semantic … Within such an assembly the trigger is
> *any* edit … For each ask: does its effect depend on *where* it sits …? If yes, "all the information is
> still present" is **not** a clean verdict; the finding is the *behavior* change, ranked by impact."*

and `charter.md:110-114`:
> *"- **If the plan introduces a new accessor or a new read-modify-write window over shared mutable state,
> map the accessors and challenge the guard's scope** (lens 4). Fires only where the plan *alters*
> concurrency over shared state. … **A guard's existence is not coverage.**"*

Re-stated as a reviewer duty at `stages/stage-4-adversarial-redteam.md:19-20`:
> *"**Fire the position lens if** the planned artifact is a position-sensitive assembly and the concurrency
> lens **if** the plan alters concurrency over shared state (charter conditional lenses)."*

**Membership check.** `grep -i` over `oracles/sweep-answers.tsv` and `oracles/criteria.tsv` for
`position`/`concurrency`/`conditional` returns no row governing either lens (the only `position` hits are
incidental substrings of unrelated pinned sentences). Neither appears in `METHODOLOGY.md`'s cross-file rule
index (`:314-333`), so neither has an ID and neither can enter the ID-driven row set.

**The three questions.**
- **(a) Producer — none.** The fact "this artifact is position-sensitive" / "this plan alters concurrency"
  is produced by the reviewer's own unrecorded judgment. Compare: this very cycle adds `S-IDN`
  (*"`spawn_id` is the identifier the dispatcher observed at spawn, **never self-reported**"*) and `S-BIND-DISP`
  (*"recorded by the dispatcher at spawn, **not self-reported by the reviewer**"*) on the explicit ground
  that reviewer self-report is not a trustworthy operand. The two conditional lenses are **100 %
  self-reported and not even recorded**.
- **(b) Degenerate case — undefined.** If the reviewer does not notice the condition, the lens silently does
  not fire, the record contains no trace of the omission, and the pass reads clean. There is no `n=1`, root,
  first-run or empty answer because there is no state at all.
- **(c) Counterpart — none.** The three standing lenses that can be faked have earned-clean clauses
  (`charter.md:68-72` factual, `:73-79` fidelity, `:80-87` Completeness). **The two conditional lenses have
  none.** `charter.md:99-100`'s *"A record missing any of these = the review is treated as un-run"* covers
  the five provenance elements, not lens firing.

**Why it matters, concretely.** Both conditions hold for *this very cycle*:
- `1-spec.md:243-244`: *"**Position-sensitive prompt assembly.** New rules go **before** GBP so GBP keeps
  the recency slot, and the rule block's **closing rationale is re-enumerated**"* — the position lens fires.
- `2-plan.md:339` §4 heading: *"**Concurrency (ST2b) — accessors enumerated, readers included**"*, and
  `SKILL.md:39-41` confirms the artifact is a position-sensitive assembly by its own words: *"these files
  are prompts — a position-sensitive assembly — and this rule block is load-bearing before the stage
  table"*.

So the artifact under review triggers both conditional lenses, the plan edits **18 files** of a
position-sensitive assembly and **alters concurrency over four shared surfaces** (`index.md`, the gate logs,
the catalog, `catalog-pending/`), and yet a reviewer record that never mentions either lens is
indistinguishable from one that ran both and found nothing. **That is exactly the "vacuously satisfied"
shape the sweep exists to catch**, in the charter that is handed to every cold reviewer verbatim
(`charter.md:8-9`) — and it is invisible to an ID-driven generator for precisely the declared reason.

**Per `2-plan.md:364`, the plan itself designates this the honest exception rather than a hidden bounce:**
*"If a reviewer finds a 6th no-ID predicate, that is the honest exception: it is the residual §1 declares."*
I state my severity as **BLOCKER** because the missing operand is *the firing of a review lens*, i.e. a gate
whose absence is undetectable — and route it as the plan's own §5 directs. The minimal fix is symmetric with
what pass 3 already built: make lens-firing a **dispatcher-recorded** field (`position_lens: fired |
not-applicable-because…`, same for concurrency), with the "not-applicable" answer required to name its
reason — the identical shape as `S-IDN-DEGR`'s *"declared degraded, never un-run"*.

---

### H/5 — **MAJOR** · The sweep instrument is **not** total: I mutation-tested two ways a predicate leaves the table with `SWEEP: OK`, exit 0

**Claim.** `2-plan.md:31` states *"**The row set is not authored.**"* and `:51-52` states *"Totality is
enforced, and the enforcement was **mutation-tested in both directions** — this is the mechanism that makes
D/2 **structurally impossible** rather than promised."* There are **three** directions, not two, and the
third and fourth are open.

**Reproduced first, as a control** (all commands run by me):

```
$ oracles/gen-sweep-rows.sh | tail -1              →  TOTAL ROWS REQUIRED: 86
$ oracles/gen-sweep-table.sh                        →  SWEEP: OK …            EXIT=0
$ diff <(sed -n '77,171p' 2-plan.md) oracles/sweep-table.generated.md   →  identical
$ # M1: delete the closed-input-set answer
  SWEEP: FAIL — generated rows with NO authored answer: closed-input-set      EXIT=1   ✓ as claimed
$ # M2: an authored answer for a predicate that no longer exists
  SWEEP: FAIL — authored answers with NO generated row: S-GHOST               EXIT=1   ✓ as claimed
```

**The two escapes I found:**

```
$ # M4: a BRAND-NEW criterion row typed KIND=PRESERVE, with NO authored answer
$ printf 'S-NEWPRED\tPRESERVE\tfoo\tbar\t\n' >> criteria.tsv && ./gen-sweep-table.sh
  ROWS EMITTED: 86   (generated row set: 86; authored answers: 86)
  SWEEP: OK — the row set is generated and every generated row is answered   EXIT=0   ✗ ESCAPED
```
Cause: `oracles/gen-sweep-rows.sh:13` filters `($2=="NEW"||$2=="COOC")`. **The `KIND` column is an
undeclared escape hatch from the sweep.** The 8 existing `PRESERVE` rows (`P-GBP … P-RAT3`) are already
outside the 86 and the documents never say so. (M3 — flipping an *existing* answered row to `PRESERVE` —
*is* caught, exit 1, because its answer orphans; the hole is only for rows born `PRESERVE`.)

```
$ # M5: a brand-new mnemonic rule ID planted in the artifact tree
$ printf '\n**A brand new rule (NEWRULE).** Nodes must do the thing.\n' >> stages/stage-2-draft-node.md
$ oracles/ruleid-sitemap.sh .
  SITEMAP: OK — every expected site present, no unexpected site               EXIT=0   ✗ ESCAPED
  (and no sweep row is generated for NEWRULE; SWEEP: OK still prints)
```
Cause: `oracles/lib-corpus.sh:10` — the ID universe is a **hand-typed literal**:
> `LIVE_IDS="GBP PASS1 PASS2 PASS-ORD CMP CMP2 SPN COV ORC ECON GRN TOP CAP DEC TPL TPL1 TPL2 TPL3 RST RAT3 SEV"`

and `gen-expected-sites.sh:12` iterates `for id in $LIVE_IDS`. So `expected-sites.txt` generates the
**ID→file mapping** from the tree, but **not the ID set**. `2-plan.md:36`'s parenthetical *"(from
`oracles/expected-sites.txt`, itself **GENERATED from the tree**)"* is therefore half-true in the half that
matters for totality.

**Why it matters.** Strictly, **all 86 rows trace to authored lists**: 21 from `lib-corpus.sh:10`, 5 from
`gen-sweep-rows.sh:8`, 60 from a hand-maintained `criteria.tsv` filtered on a hand-typed `KIND`. What pass 3
genuinely mechanized is the **join** and the **site measurement** — both real advances — but *"the row set is
not authored"* and *"makes D/2 structurally impossible"* overstate them, and only **one** of the **three**
blind spots is declared. No *current* predicate is lost through either escape (the 8 `P-*` rows all shadow
baseline IDs already in the sweep, and no un-listed ID exists in the tree today), which is why I rate this
**MAJOR rather than blocker** — it is a latent hole plus an overclaim, not a live omission.

**⚠ I must flag the routing rather than decide it.** `1-spec.md:75` defines class **β** as *"the measurement
apparatus cannot detect a failed build — **and the document says it can**"*, and `2-plan.md:358` says a
class-β finding against pass 3 *"is a genuine second bounce on a released cap and is a **stop-for-human**,
relayed verbatim."* This finding has the class-β shape. I state it plainly and leave the classification to
the gate; I do not soften it to avoid the routing.

---

### H/6 — **MAJOR** · Rows 1 and 69 cite a statement at `s7` that does not exist, and the empty tree assembles vacuously

**Claim.** Two sweep answers rest on a citation I refuted.

**Citation.** `2-plan.md:79` (row 1, `GBP`, verdict **OK**):
> *"**empty tree: no nodes, so nothing is presentable and there is no artifact to gate — stated at s7**"*

`2-plan.md:147` (row 69, `S-COV-PROD`, verdict **FIXED**):
> *"**empty tree: no nodes, so the conjunction over nodes is vacuously true and there is nothing to
> assemble — stated at s7**"*

**Refutation.** `grep -rn "empty"` over the entire pinned corpus returns exactly **three** hits, and **none
is in `stages/stage-7-assemble.md`**:
- `stages/stage-1-frame-template-match.md:12` — *"`plan/topgate/` (empty)"*
- `stages/stage-8-restart-resume.md:18` — *"An **empty / incomplete node dir**…"*
- `METHODOLOGY.md:242` — *"An **empty node dir** IS the 'not planned yet' marker"*

The nearest candidate, `stage-7-assemble.md:33-35` (*"**A fully-covered clean tree assembles.** … when
**every node** has both passes clean-or-resolved, assembly proceeds"*), is about a *populated* clean tree.
And no criterion pins either sentence: `S-COV-PROD`'s pinned string is *"every node gated clean is decided
from each node's own recorded gate state, which stage 5 writes before stage 7 reads it"*
(`1.5-criteria.md:142`) — it does not state the empty case, and `GBP` has no `S-*` row of its own.

**Why it matters.** The second half of row 69's own answer names the defect and then labels it satisfied:
*"the conjunction over nodes is **vacuously true**"*. Read `stage-7-assemble.md:10-13` — *"Walk `tree/`. For
**every** node confirm both `completeness/` (3 records) and `adversarial/` (3 records) exist … If **any**
node is missing a pass … **do not assemble**"* — over **zero** nodes both quantifiers pass and assembly is
**not blocked**. That is bit-for-bit the vacuity class this cycle declares must be an error, not a pass, at
`criteria.tsv` `S-CTX-VAC`: *"…because path-validation over an absent key checks zero paths and **passes
trivially**"*. It is reachable: `stage-1…md:11-12` creates `tree/` **empty**, and a HARDSTOP between
run-level setup and stage 2 leaves it empty; on restart, `stage-8…md:33-34`'s *"walk `tree/` for the first
node whose expected output is missing"* finds **no nodes and therefore no resume point**, and nothing
prevents proceeding. This is D/4's shape (unpinned "stated" answers) **plus a false citation added on top**,
in a row whose verdict is `OK` — the exact place my frame was told to look hardest.

---

### H/7 — **MAJOR** · D/4 is **not** closed for the 21 baseline rows — the rows pass 3 added

**Claim.** Pass 2's D/4 was *"roughly half of §1's degenerate-case answers end in the word 'stated', and
**no criterion pins any of those sentences** — so the column the whole sweep rests on is invisible to the
build"* (`3-redteam-plan.pass2.md`, "The majors, grouped"). Pass 3 closed this for many *criterion* rows and
**did not close it for the baseline rows it newly added**.

**Citation.** 25 of the 86 (b) answers contain "stated"/"STATED" (extracted from `sweep-answers.tsv` column
3). For the 21 baseline rows I checked each against `criteria.tsv`'s pinned strings:

| (b) claim | Pinned by a criterion? |
|---|---|
| `GBP` *"empty tree … stated at s7"* | **NO** (and false — H/6) |
| `CMP2` *"tier (iii) is then the only tier with content"* | **NO** |
| `COV` *"n=1: there are no seams at all, so the seam half is vacuous"* | **NO** |
| `ORC` *"n=1: no sub-orchestrators exist … — stated"* | **NO** |
| `ECON` *"n=1: … ECON is vacuous — stated"* | **NO** |
| `GRN` *"n=1: the root returns leaf"* | **NO** |
| `TOP` *"TOP NEVER FIRES — stated explicitly"* | **NO** — `S-HG2-ONLY` pins *"fires at the top level only and never at deeper splits"*, which does not state the never-fires-on-a-leaf case |
| `CAP` *"the first gate has no history, so the count is 0 — stated"* | **NO** |
| `TPL1` *"the recorded value is the explicit token `create-new`"* | **NO** — `S-CNC-TMPL` pins the header route, not the token |
| `TPL2` *"run end does nothing **AND MUST NOT TAKE THE LOCK** — stated"* | **NO** — `S-CNC-LOCK-REL` pins acquire/release, `S-TPL3` pins *"only under the lock"*; nothing says "if there is nothing to commit, do not take it" |
| `RAT3` *"no delegation: RAT3 is vacuous because the human is present — stated"* | **NO** |
| `SEV` *"a record that states no severity is un-run"* | **NO** |

Pinned, and credited: `DEC`→`S-DEC-DEGEN`, `TPL`→`S-CNC-LOCK` (first-run), `TPL3`→`S-CNC-PENDING`,
`RST`→`S-RST-RESUME`, `PASS1/PASS2`→`S-IDN-DEGR`. `PASS-ORD` and `SPN` are already true in the baseline
source (verified, §2.3).

**Why it matters.** `2-plan.md:194-196` says the newly-added rows are *"the under-generalization R4 names,
**measured rather than argued**"*. The measurement produced rows; the rows' (b) answers are then **prose in
a change record that the build never has to make true**. Pass 2's own CAP determination
(`3-redteam-plan.pass2.md:265`) groups D/4 with class β. A **recurrence of D/4 on the very rows pass 3 added
to close D/2** is the R4 pattern turned on itself: the fix (pin the degenerate-case sentence with a
criterion) was applied to the `S-*` rows and not generalized to the 21.

---

### H/8 — **MAJOR** · The item-9 resume exception makes an HG2 **bounce** indistinguishable from an unanswered ask

**Claim.** `S-RST-RESUME` is keyed on the *presence* of `plan/assembly-approval.md`. A **bounce** also leaves
that file absent, so a restart after a bounce re-fires the HG2 ask on the unchanged artifact instead of
routing to the re-draft.

**Citation.** `oracles/criteria.tsv` `S-RST-RESUME` (gating, `M s8`):
> *"…so **a restart that finds `assembled-plan.md` with no approval is not done and resumes at the HG2
> ask**"*

`2-plan.md:140` (row 62, `S-HG2`, (c) column):
> *"the gate is released by the recorded approval; **a bounce re-opens the named nodes at stage 2**"*

`2-plan.md:137` (row 59, (c) column): *"the ask's counterpart is the recorded approval **or a recorded
bounce**"*.

The phrase *"a recorded bounce"* appears **only** in those two answer cells. `grep -n "bounce"` over
`criteria.tsv` returns `S-RES`, `S-RES-STATES`, `S-HG2`, `S-HG2-AUTHORED` — **none names a bounce artifact
or filename**, and no deterministic filename for a bounce is added to `stage-8…md:13-14`'s list.

**Why it matters.** Concrete trace: human bounces at HG2 → orchestrator "re-opens the named nodes at stage
2" → HARDSTOP mid-re-draft. On restart, `assembled-plan.md` exists, `plan/assembly-approval.md` does not, so
`S-RST-RESUME` says *"not done, resume at the HG2 ask"* — the human is asked the same question about the
same artifact, forever. The item-9 fix (`1-spec.md:103-107`) correctly removed one degenerate state
(artifact present + approval absent + never asked) and created a second (artifact present + approval absent +
**already bounced**) that reads identically. `S-HG2-AUTHORED` honestly labels the bounce *route* as this
cycle's authoring choice — but the *interaction with the resume exception* is a state machine hole, not a
routing preference. The minimal fix is symmetric with what item 9 already did: give the bounce its own
deterministic filename so the resume predicate can discriminate three states, not two.

---

### H/9 — **MAJOR** · A second, unswept "run complete" marker survives at `stage-7.md:20`

**Claim.** `S-HG2-MARKER` pins *"the run-complete marker is the recorded assembly approval, **never** the
existence of `assembled-plan.md`"* with an absence sweep on the old wording. There is a **third** completion
record that neither the pinned string nor the absence sweep touches.

**Citation.**
- `stages/stage-7-assemble.md:20`: *"4. **Record completion** in `RUN.md` / the apex `_status.md`."*
- `stages/stage-7-assemble.md:39-40` (the one the sweep targets): *"`assembled-plan.md` is the deterministic
  output name; **its existence is the "run complete" marker**."*
- `oracles/criteria.tsv` `S-HG2-MARKER` ABSENT column: `its existence is the .run complete. marker` — matches
  line 39-40 **only**.
- Stage 7's step 4 runs **before** HG2 is answered (HG2 is the gate *on* stage 7's output,
  `1.5-criteria.md:135`).

**Why it matters.** After the build, `stage-7-assemble.md` will simultaneously say *"the run-complete marker
is the recorded assembly approval"* (pinned at `s7`) and instruct the orchestrator to *record completion* in
`RUN.md` before any approval exists. `RUN.md` is the apex resume surface — *"A fresh or post-compaction
orchestrator continues from `RUN.md` + the tree alone"* (`stage-8…md:34-35`) — so a resuming orchestrator
reads "complete" from the one file it is told to trust first. `1-spec.md:110` says of item 10 *"the honest
position is taken, plainly, and **everywhere**"* and `2-plan.md:307` says the marker rule is *"enforced from
both directions"*. Both directions were swept over the wording at line 39-40; the *behavioural* second
marker at line 20 was not, and no criterion requires it to change.

---

### H/10 — **MAJOR** · `closed-input-set`: the premise is a misreading, and one unproducible operand survives the carve-out

My frame asked me to verify or refute this row specifically. **Both halves have a problem.**

**(A) The premise.** Row 82 and `2-plan.md:199-205` read the charter as making the *presence* of all five
closed-set operands mandatory. The charter's sentence is a **closure bound**, not a totality requirement,
and the antecedent of "these" is the five *record* elements. Verbatim, `stages/charter.md:93-100`:

> *"- **Provenance is part of the review record.** Every cold-review record embeds: **(i)** the verbatim
> charter/prompt given, **(ii)** the exact context path list given, **(iii)** the reviewer's verbatim output
> …, **(iv)** the reviewer's agent type + model, and **(v)** the reviewer-reported sha256 of each context
> file it read. Reviewer input is a **closed set**: the node's `plan.md` + its decomposition + child seams,
> the config's `redteam_context`, the parent node's plan, and carried-forward findings from `decisions.md`;
> **any supplementary author-authored context must be quoted in the record as such.** **A record missing any
> of these = the review is treated as un-run.**"*

A *record* embeds (i)–(v); it does not "contain" the input set — it contains the **context path list**,
which is element (ii). The artifact's own restatement removes the ambiguity —
`stages/stage-3-completeness-critic.md:27-30`:
> *"**Record each agent verbatim.** Write three records … each embedding **the charter given, the exact
> context list, the agent's verbatim output, its agent type + model, and its reported context-file sha256s**
> (charter provenance). **A record missing any element = un-run.**"*

That is unambiguously the five **record elements**. So the sweep's sharpest claim —
`2-plan.md:203-204`: *"Unfixed, that makes **every first pass at every node un-run, including this hardening
loop's own reviews**"* — is **not true of the source**. (Inference, clearly labelled: the sentence *is*
ambiguous enough that a cold reviewer could take the plan's reading, so closing the ambiguity is worth doing.
My finding is not "don't fix it" — it is that the fix is **mislabelled as closing a live defect**, and that
the chosen fix *cements* the wrong reading: carving three members out implies the other two are required
present.)

**(B) One unproducible operand survives.** `stage-3`'s own copy of the closed set has **six** members, not
five:

`stages/stage-3-completeness-critic.md:16-18`:
> *"Each is handed the charter verbatim + the closed input set: this node's `plan.md`, its decomposition +
> child seams, the config **`redteam_context` + `domain_context`**, the parent node's plan, and any
> carried-forward findings from `decisions.md`."*

`stages/stage-4-adversarial-redteam.md:13-15` has a **third** membership — five members, and it narrows the
fifth to *"the carried-forward **completeness** findings"*.

**`domain_context` appears nowhere in this cycle's work.** `grep -n "domain_context"` over `criteria.tsv`,
`sweep-answers.tsv`, `1.5-criteria.md`, `1-spec.md`, `2-plan.md` returns **zero hits**. So:
- it is a member of the closed input set at the site (`s3`) where `S-CLOSED-DEGEN` will be pinned;
- its producer is the config author, and `METHODOLOGY.md:70-72` declares it optional-shaped prose;
- its **absent-key case is neither carved out nor made an error** — `S-CTX-VAC` covers `redteam_context`
  only;
- so under the reading `S-CLOSED-DEGEN` cements, an absent `domain_context` makes every stage-3 review
  un-run, and nothing in the sweep notices.

Also elided: `S-CLOSED-DEGEN` carves out *"a leaf has no **child seams**"* but the set's second member is
*"its **decomposition** + child seams"* — a leaf has no decomposition either, and the carve-out does not say
so.

**Answer to my frame's question:** *"Does the claimed carve-out actually cover every unproducible operand,
or does one survive?"* — **One survives: `domain_context`** (plus "decomposition" as distinct from "child
seams"), and the plan's "five-member closed set" framing is what hid it: it swept the charter's copy of the
list and never checked that the two stage files hold two different copies.

---

### H/11 — **MAJOR** · Row 83's (c) answer restates a mechanism that does not exist

Covered as predicate **P2** in §2.1. Restated here with its severity for the ranked list.

`2-plan.md:161`, row 83 (c): *"**a partial file is not the deterministic name** and is overwritten by the
clean re-dispatch."* Its source, `stages/stage-8-restart-resume.md:22-24`: *"their half-written outputs are
ignored because stage-done is an output-exists check on the **complete** deterministic file — a partial
`completeness/B.md` is **not the final name** and is overwritten by the clean re-dispatch."*

A partial `completeness/B.md` **is** named `completeness/B.md`. The only mechanism that would make the claim
true is write-to-temp-then-atomic-rename, and `grep -ni "atomic\|rename\|\.tmp\|temp file"` over
`1.5-criteria.md`, `2-plan.md`, `1-spec.md`, `criteria.tsv` yields **only the catalog lock**
(`criteria.tsv:33`, *"an atomic symlink whose target is the holder's pid"*). Row 83's (c) is therefore
circular: done-ness is decided by output-exists, and the partial/complete distinction it needs is produced by
nothing. **Row 83 is verdict `FIXED`.** Under the plan's own rule at `2-plan.md:21-23` — *"no mutation may be
labelled 'class (i), computed not stored'"* — this is the same move: an unproducible fact answered by
restating the assertion.

---

### H/12 — **MINOR** · `_status.md` is a deterministic done-marker whose writer is deferred, and two stages claim it

`stages/stage-8-restart-resume.md:14` lists `_status.md` among the deterministic filenames. `METHODOLOGY.md:268`
gives it *"terse done-state + one-line roll-up + **gate state**"* (stage 5's fact) while
`stages/stage-6…md:11` writes *"the final decision in `index.md` / the node's `_status.md`"* (stage 6's
fact). And `2-plan.md:274-275` states: *"**`_status.md`'s writer is likewise deferred**, so 'reduced to one
writer' is **not** claimed of it."*

So the only candidate done-marker for stage 5 (and stage 6) is a file with **no declared producer**, and its
existence cannot say which of the two stages is done. This touches deferred **F1**, so I record it as a
**carry-forward** per my scope instruction — **except** for the part that is in scope: rows 19 and 83 are
marked **FIXED** while resting on it, which is the in-scope half (see H/3).

---

### H/13 — **MINOR** · `TPL2` is verdict `OK` with the same run-end exposure that makes rows 85/86 `PARTIAL+DECLARED`

`2-plan.md:95` (row 17, `TPL2`, verdict **OK**): *"(a) the distilled new skeleton: written at stage 6 after
the node is gated clean, **read at run end**"*; (b) *"no create-new node: nothing to distil, so run end does
nothing **AND MUST NOT TAKE THE LOCK** — stated"*.

Two problems. (1) An operand *"read at run end"* inherits the unbounded-run-end exposure that rows 85 and 86
are labelled `PARTIAL+DECLARED` for; row 17's (b) never mentions the no-end case, and the verdict is `OK`.
Inconsistent labelling of the same exposure. (2) *"MUST NOT TAKE THE LOCK — stated"* is stated nowhere — see
H/7's table. The consequence is contained (`S-CNC-LOCK-REL`'s dead-pid self-breaking rescues a leaked
run-end lock), which is why this is Minor rather than Major.

---

### H/14 — **MINOR** · The config-key-vacuity class is declared for one key and left silent for four

Covered as predicate **P5** in §2.1. `2-plan.md:83` (row 5, `CMP`) names the class exactly — *"the same 'an
absent config key makes the check pass trivially' class as `S-CTX-VAC`"* — and declares it a `DECLARED GAP`
for `required_sections` alone. `scale_context` (*"Sets the granularity check's expectation"*,
`METHODOLOGY.md:74-76`), `domain_context` (H/10), `catalog` and `run_root` (`stage-1…md:11`) are the same
class and are not mentioned. Given R1's narrowing I accept that *fixing* them is out of scope; **declaring**
them is not, and the sweep's own precedent is to declare rather than drop
(`2-plan.md:69-71`, *"`DECLARED GAP` … named here, **not** fixed, **never silently dropped**"*).

---

### H/15 — **MINOR** · "absent node dir" ≠ "empty node dir": the not-planned-yet marker is undefined on the first run

`METHODOLOGY.md:242`: *"An **empty node dir** IS the 'not planned yet' marker."*
`stages/stage-8-restart-resume.md:18-19`: *"An **empty / incomplete node dir** IS the 'not planned yet'
marker."* On the very first run `tree/root/` **does not exist at all** — `stage-1…md:11-12` creates only
`tree/`. Row 83's (b) reproduces the same gap (*"empty node dir = 'not planned yet'"*, no first-run answer),
and `S-RST` pins the root's *location* (*"the root plan node lives at `tree/root/`"*) without saying that its
absence is the marker. Local and easy to fix in place; noted because the (b) column is supposed to answer the
first-run case and does not.

---

### H/16 — **NITPICK** · Two charter predicates with no ID, no row, and (correctly) no consequence

Predicates **P3** and **P4** in §2.1: the *supplementary-context-quoting* duty (`charter.md:98-99`, no
checker) and the *A/B-harness prohibition* (`charter.md:100-101`), the latter explicitly declared
never-firing at `charter.md:21-22`. Both are outside the 86 and neither carries an ID. I record them for
enumeration completeness; neither is a defect. **P4 in particular is a properly-handled vacuous predicate** —
which is worth saying, because it is the one place in the corpus where "this never fires" is stated rather
than left implicit, exactly as row 12 (`TOP`) argues it should be.

---

## 4. COVERAGE CHALLENGE (CH8) — behaviours this change could alter that **no criterion observes**

Ranked by likelihood × impact. All five are new or newly-reachable *because of this cycle's edits*.

**CH8-1 — After a bounce, the restart walk has no resume target (BIND × RST interaction).** *No criterion
observes this.* `S-BIND-EXIT` pins *"a stale record is un-run and its node un-gated; the exit is to re-run
that pass"* (`1.5-criteria.md:98`) at `S s5 s7 s8`. But `stage-8…md:33-34`'s resume rule is *"walk `tree/`
for the first node whose expected output is **missing** → resume there."* **Scenario:** node `B` bounces at
gate 5; stage 2 re-drafts `plan.md` (hash changes, so all six records are now BIND-stale); HARDSTOP. On
restart every deterministic output at `B` is **present**, so the walk finds nothing missing anywhere and
returns no resume point; stage 7 then reads `B`'s gate entry, finds `blocked`, and refuses to assemble. The
run is stuck: unable to assemble, with no node identified to resume. `S-RES-STATES` gives `blocked` a name
but nothing turns a `blocked`/stale node back into a resume target. The pinned sentences make staleness a
*gate* fact; the resume walk is a *file-existence* fact; nothing joins them.

**CH8-2 — Empty tree assembles vacuously (H/6).** *No criterion observes this.* Scenario in H/6. The
governed behaviour — "assembly is blocked, not degraded" (`stage-7…md:13`) — is unobserved at n=0, and the
one row that names the vacuity labels it satisfied.

**CH8-3 — `template: <name>` does not survive stage 2, and TPL3 silently stops firing.** *No criterion
observes header survival.* `S-CNC-TMPL` observes only that a *sentence* about stage 1 appears in three files;
nothing observes that the header survives stage 2's instantiation or a bounce-driven re-draft. Scenario: node
matched skeleton `X` at stage 1; stage 2 instantiates `X` into `plan.md`; gate 5 returns major; stage 2
re-drafts `plan.md` from scratch; `template:` is gone; the hole-fix found on this node is never
back-propagated to skeleton `X` (`stage-6…md:32-33` fires only when the section *"came from a catalog
skeleton"*). The self-improvement mechanism degrades exactly on the nodes with findings — the ones it
exists for.

**CH8-4 — HG2 bounce loop (H/8).** *No criterion observes the three-state distinction.* Scenario in H/8.
`S-RST-RESUME` and `S-HG2-MARKER` are both satisfiable while the bounce state is unrepresentable.

**CH8-5 — Conditional lenses silently do not fire (H/4).** *No criterion observes lens firing.* Scenario:
the very next Architect run plans a prompt assembly, three cold agents review it, none evaluates the
position-lens condition; every record passes every earned-clean clause (factual citations present, fidelity
terms pinned, Completeness section-classes named) and the node gates clean with the position lens un-run and
no trace of it. `P-CMP2` pins the word `generative`; nothing pins *"did the conditional lenses fire, and if
not, why not."*

**Considered and dismissed** (recorded so the challenge is not padded): *run-end takes the catalog lock with
nothing to commit* — reachable, but `S-CNC-LOCK-REL`'s *"a lock whose target pid is not alive is stale by
definition and any run may remove it"* (`criteria.tsv`) contains the damage; *`ex/planning` has no
`redteam_context` key and would be a config error under `S-CTX-VAC`* — covered, `S-CTX`'s site set includes
`ex/planning`.

---

## 5. LABEL AUDIT (CH9/CH10)

For each gating criterion sampled: the **governed behaviour**, what the criterion **actually observes**, and
the evidence I checked. Where these diverge I challenge it.

| Criterion | Governed behaviour | What it observes | Verdict |
|---|---|---|---|
| **`S-CNC-TMPL`** (`1.5:116`, `M s1 tp/README`) | no write-write race on `template used` | a prose sentence asserting stage 1 is `plan.md`'s only writer | **CHALLENGE — proxy, and the proxy is false.** Refuted against `stage-2…md:3`. The criterion will pass by writing an untrue sentence. See H/2. |
| **`S-RST-RESUME`** (`1.5:132`, `M s8`) | a restart with artifact + no approval resumes at HG2 | a prose sentence containing the universal *"one named exception"* | **CHALLENGE — proxy carrying a false quantifier.** The governed behaviour (stage 7) is genuinely fixed; the sentence over-claims about stages 1/5/6. See H/3. |
| **`S-CLOSED-DEGEN`** (`1.5:129`, `ch s3`) | a first-pass review is not un-run for want of unproducible operands | the carve-out sentence, **including its stated reason** | **CHALLENGE.** The reason (*"the gate log's first writer is stage 5"*) is falsified by `S-PATHVAL`, a sibling gating row landing in the same file. See H/1. |
| **`S-COV-PROD`** (`1.5:142`, `M S s6 s7`) | stage 7 decides "every node gated clean" from a per-node recorded gate state | a sentence asserting stage 5 writes it before stage 7 reads it | **CHALLENGE (mild).** The criterion cannot observe whether stage 7's *procedure* (`stage-7…md:10-13`) is edited to read that state — it observes the claim, not the step. `1.5-criteria.md`'s §4 honestly says `check.sh` is not a semantic oracle, and `2-plan.md:375` repeats it — but row 69's verdict upgrades the sentence to *"FIXED — a producer now exists (S-COV-PROD)"*. The producer exists **in a sentence**. Label the row `FIXED (stated)`, not `FIXED`. |
| **`S-HG2-MARKER`** (`1.5:137`, `M S s5 s7 s8`) | nothing treats `assembled-plan.md`'s existence as run-completion | pinned sentence **+ an absence sweep** on the old wording | **PARTIAL — genuinely two-directional, and I credit it**, but its absence string matches only `stage-7…md:39-40` and misses the behavioural second marker at `stage-7…md:20`. See H/9. |
| **`S-HG2-NOSELF`** (`1.5:139`, COOC, **0 sites**) | *"self-approved"* never appears unqualified | a co-occurrence ban; measures 0 at baseline and **fails there** under the vacuous-site guard | **CLEAN, and the best-labelled row in the file.** It states plainly that it *"cannot force the text to be written anywhere"* (`2-plan.md:144`). This is the honest shape the others should copy. |
| **`S-F5-LIMIT` / `S-COV-LIMIT`** (`1.5:149`, `:143`) | a reader is told the gap exists wherever the claim is made | the limitation sentence at the measured sites | **CLEAN.** These correctly observe *"a statement was made"*, which is exactly what they claim to do — verdict `DECLARED GAP`, not `FIXED`. Correct labelling. |
| **The 8 `P-*` PRESERVE rows** (`1.5:155-162`) | the pass does not erode eight baseline rules | **bare token presence, per file** | **CHALLENGE — MAJOR.** See below. |

### The PRESERVE rows are the "token is merely mentioned" oracle the spec lists as already fixed

Verbatim from `oracles/criteria.tsv`:

| ID | ANCHOR | PINNED |
|---|---|---|
| `P-GBP` | `clean-or-resolved` | `clean-or-resolved` |
| `P-COV` | `every node and every altitude` | `every node and every altitude` |
| `P-CMP2` | `generative` | **`generative`** |
| `P-RST-HARDSTOP` | `HARDSTOP` | **`HARDSTOP`** |
| `P-TOP-DEEPER` | `deeper.{0,40}(splits\|recursive)` | **`deeper`** |
| `P-SPN-SEVEN` | `7-section universal spine` | `7-section universal spine` |
| `P-ECON` | `context economy\|Context economy` | `context economy` |
| `P-RAT3` | `halts the (subagent\|runner)` | **`halts the`** |

Four of eight pin a **single word or a two-word fragment**, matched case-insensitively per *file*.
`1-spec.md:85` lists as an already-solved defect: *"an oracle checks only that a token is **mentioned** →
**positive per-site assertion of the operative sentence**"*. `P-TOP-DEEPER` is satisfied by the word
`deeper` appearing anywhere in each of four files — I measured its distribution: `SKILL.md` 1,
`METHODOLOGY.md` 2, `stage-6…md` 2, `templates/seed/decomposition-node.md:28` (*"Deeper splits proceed
red-team-gated, autonomous"*, capitalised). Deleting the entire *"deeper splits proceed autonomous"* rule
while leaving any sentence containing "deeper" would pass. `P-RAT3`'s `halts the` is satisfied by
`SKILL.md:91`, `METHODOLOGY.md:226`, `stage-6…md:67` — and would survive a rewrite that keeps the phrase and
inverts the rule. **This is class α under R4 in a section pass 3 claims to have swept:** the proven fix
(positive assertion of the *operative sentence*) was applied to all 60 `NEW`/`COOC` rows and **not**
generalized to the 8 `PRESERVE` rows added this pass in response to pass 2's E/13. I rate this **MAJOR** and
fold it under H/5's family (the `PRESERVE` kind is both the sweep's escape hatch and the file's weakest
oracle).

### Citation spot-verification I performed on the plan's own claims (CH6-style, since I am the factual lens here)

| Plan claim | Result |
|---|---|
| `2-plan.md:35` *"TOTAL ROWS REQUIRED: 86"* | **CONFIRMED** — ran it |
| `2-plan.md:47-48` *"ROWS EMITTED: 86 … SWEEP: OK"* | **CONFIRMED**, exit 0 |
| `2-plan.md:56` M1 *"EXIT=1"* | **CONFIRMED**, exit 1 |
| `2-plan.md:58` M2 *"EXIT=1"* | **CONFIRMED**, exit 1 |
| `2-plan.md:75` *"The table below is `gen-sweep-table.sh`'s output, verbatim"* | **CONFIRMED** — `diff` byte-identical against a fresh run |
| `2-plan.md:166-169` verdict tally 3/64/15/4 | **CONFIRMED** — reproduced by the generator |
| `2-plan.md:180-185` §1.1's tally block | **CONFIRMED** — matches the generator's output |
| `1-spec.md:264-266` *"`git diff` over the artifact set is empty and HEAD is `b08f5a9`"* | **CONFIRMED** |
| `2-plan.md:36` *"expected-sites.txt, itself GENERATED from the tree"* | **PARTIALLY REFUTED** — the mapping is generated, the ID set is `lib-corpus.sh:10`'s literal. H/5 |
| `2-plan.md:31` *"The row set is not authored"* | **REFUTED** — H/5 |
| `2-plan.md:51-52` *"mutation-tested in both directions … makes D/2 structurally impossible"* | **REFUTED** — two further directions untested and open. H/5 |
| `2-plan.md:79`, `:147` *"stated at s7"* | **REFUTED** — H/6 |
| `2-plan.md:14-19` the R7 label | **CONFIRMED** against `LOOP-STATE.md:224-231` |
| `1.5-criteria.md:86` *"ROWS EMITTED: 68"* | **CONFIRMED** in the file's own embedded output; I did not re-run `gen-criteria-table.sh` (needs a tree-root arg and would regenerate a file that mutated mid-review) — **unverified by execution**, verified by internal consistency with `criteria.tsv`'s 68 rows |

**No fabricated citation found in the plan.** Every path:line I sampled exists and says what is claimed —
the failures above are failures of *inference from* the source, not invented sources. That distinction is
worth recording: pass 3 does not repeat pass 2's present-tense fabrication.

---

## 6. WHAT THE PASS GENUINELY EARNED

Specific, and I checked each one by running or reading it:

1. **The join is real, and I could not break it along the two axes it claims.** M1 and M2 reproduce exactly
   as documented, exit 1 both ways. The embedded §1 table is **byte-identical** to a fresh generator run, so
   the "generate, do not type" rule is not a slogan here — I verified it with `diff`. Compared with pass 2's
   §1, which claimed totality while 15 of 21 baseline IDs had no row, this is a genuine structural change,
   not a promise.
2. **The generated tally, and owning the typed one.** `2-plan.md:174-176` records that pass 3's own first
   draft typed 55/20/4/4 and measured 64/15/4/3, then mechanized the tally. Self-caught, self-recorded, fixed
   at the mechanism rather than the number. That is the discipline the cap was tripped for lacking.
3. **The R7 label is faithful, everywhere I checked.** `2-plan.md:14-19` and `1-spec.md:58-68` label the
   (a)/(b)/(c) framing an orchestrator proposal and never cite it as an owner requirement — matching
   `LOOP-STATE.md:229-231` verbatim. My frame instructed me to treat a violation here as a finding; **there
   is none.** `1-spec.md:161` even lists the framing under *"Orchestrator call"* rather than
   *"Owner-ratified"*.
4. **The 21 baseline rows exist at all.** Pass 2 had 6. Whatever is wrong with the answers (H/7), adding the
   15 missing rows is what let me find H/2, H/3 and H/6 — three of my four blockers live in rows that did not
   exist before this pass. The instrument surfaced its own defects, which is what an instrument is for.
5. **Honest `DECLARED GAP` labelling where the gap is real.** `S-COV-LIMIT`, `S-F5-LIMIT`, `CMP`'s
   `required_sections` vacuity and `S-CNC-UNCOV` are labelled *not fixed* and stated at their sites. I
   verified `COV`'s seam-union half genuinely has no up-flow producer (`stage-7…md:28-31` claims total
   coverage including seams; nothing anywhere rolls a child finding to a parent) and that `stage-1…md:12`
   really does pre-create `plan/topgate/`. **These labels are earned.**
6. **`S-HG2-NOSELF`'s self-aware framing.** *"CO-OCCURRENCE row, not an obligation row: it cannot force the
   text to be written anywhere"* (`2-plan.md:144`) plus a row that **fails at baseline by measuring 0 sites**
   is the most honest oracle in the file. It states the limit of its own instrument in the same breath as the
   claim.
7. **`run-end`'s reasoning is sound and I could not break it.** Run end is genuinely not among the eight
   stages (`METHODOLOGY.md:293-302`), the trigger is genuinely the recorded approval, and there is genuinely
   no timeout anywhere. `PARTIAL+DECLARED` is the right verdict. My only additions are that `TPL2` shares the
   exposure with an `OK` label (H/13) and that `stage-7…md:20` is a second completion marker (H/9) — the core
   answer holds.
8. **The residual was declared honestly, and it was true.** `2-plan.md:61-67` says a sixth no-ID predicate
   would be invisible to every generator in this cycle and hands the hunt to stage 3 as a named task rather
   than hoping. **There were two.** The declaration was accurate, the mechanism to find them was correctly
   identified as human-only, and `2-plan.md:364` pre-committed to treating the finding as the honest
   exception rather than a hidden bounce. That is the pass behaving exactly as it said it would.

---

## Ranked summary

| # | ID | Sev | One line |
|---|---|---|---|
| 1 | **H/1** | **BLOCKER** | `S-CLOSED-DEGEN` (*"the gate log's first writer is stage 5"*) is falsified by this cycle's own `S-PATHVAL`; both gating, both land in `stage-3` |
| 2 | **H/2** | **BLOCKER** | `S-CNC-TMPL` pins *"stage 1 … the only writer of that file"* about `plan.md`, which is stage 2's output; six sweep rows assert the contrary |
| 3 | **H/3** | **BLOCKER** | `S-RST-RESUME` pins *"ONE named exception"* to `stage-done-iff-output-exists`; stages 1, 5 and 6-leaf are three more |
| 4 | **H/4** | **BLOCKER** | **THE SIXTH PREDICATE** — the charter's two conditional lenses fire on a self-assessed, unrecorded condition with no earned-clean clause, no ID, no row |
| 5 | **H/5** | **MAJOR** | Totality is not enforced: a `KIND=PRESERVE` row and an ID outside `lib-corpus.sh:10`'s literal both escape with `SWEEP: OK`, exit 0 (mutation-tested). *"The row set is not authored"* is false. **Possible class β — flagged, not decided** |
| 6 | **H/6** | **MAJOR** | Rows 1 and 69 cite *"stated at s7"*; nothing at s7 states it, and the empty tree makes stage 7's conjunction vacuously true |
| 7 | **H/7** | **MAJOR** | D/4 unclosed for ~11 of the 21 baseline rows — including the false one in H/6 |
| 8 | **H/8** | **MAJOR** | The item-9 resume exception makes an HG2 bounce indistinguishable from an unanswered ask |
| 9 | **H/9** | **MAJOR** | `stage-7.md:20`'s *"Record completion in `RUN.md`"* is a second, unswept run-complete marker |
| 10 | **H/10** | **MAJOR** | `closed-input-set`: the premise misreads a closure bound as a totality requirement, and `domain_context` — a member of stage 3's own six-member copy — survives the carve-out |
| 11 | **H/11** | **MAJOR** | Row 83's (c) *"a partial file is not the deterministic name"* has no mechanism; `atomic` appears only for the catalog lock |
| 12 | **CH9** | **MAJOR** | The 8 `PRESERVE` rows are bare-token oracles — the *"token merely mentioned"* defect `1-spec.md:85` lists as already fixed |
| 13 | **H/12** | MINOR | `_status.md` is a deterministic done-marker with a deferred writer, claimed by two stages (carry-forward; the `FIXED` label on rows 19/83 is the in-scope half) |
| 14 | **H/13** | MINOR | `TPL2` verdict `OK` with rows 85/86's run-end exposure; *"MUST NOT TAKE THE LOCK — stated"* is stated nowhere |
| 15 | **H/14** | MINOR | Config-key vacuity declared for `required_sections` only; `domain_context`, `scale_context`, `catalog`, `run_root` unmentioned |
| 16 | **H/15** | MINOR | "absent node dir" ≠ "empty node dir"; the marker is undefined on the first run |
| 17 | **H/16** | NITPICK | Two charter predicates with no ID and no row; both benign, one properly declared vacuous |

**Worst severity: BLOCKER.** Per `2-plan.md:353` a blocker routes to stage 1; per `2-plan.md:358-364`, **H/4
is the honest sixth-predicate exception the plan pre-declared**, while **H/5 has the class-β shape and I
flag rather than decide its routing** — I am the reviewer, and `charter.md:138-140` gives the demotion of a
blocker or major to the human tie-break, not to me.
