# Stage 1 — Spec (hardening cycle 2, **PASS 3**)

Pass 1 is at `1-spec.v1-superseded.md`; **pass 2 is at `1-spec.v2-superseded.md`**. Neither is rewritten:
they are records of what was specified at the time, and pass 2's false present-tense claims survive there
verbatim as the evidence for why the cap tripped. **The correction lives here.**

Pass 3 is authorized by **owner ruling R6** and is scoped *"narrow and mechanical."* It keeps pass 2's
**scope** (owner-ratified) and its confirmed-good core, and it replaces pass 2's **discipline of record**.

---

## 0. THE ONE RULE OF PASS 3, and what it changed about the order of work

> **No criterion, table, or prose may assert the behaviour of any script, file, or edit before that thing
> exists and has been executed.** Build → run → paste the real command output → *then* describe it, **in
> the past tense**.

Pass 2 tripped the iteration cap by doing the exact inverse: `1.5-criteria.md:13` said *"It **is now** a
checker … **exits 1**"* about `ruleid-sitemap.sh` while the script was byte-for-byte pass 1's printer, and
`1.5:119` said *"`TOPGATE` and `DECOMPOSITION` **are REMOVED**"* while the `GRAND` line was unedited.
Reviewer E found both by **running** the oracles instead of reading the claims. That is CP1
self-certification — the author approving its own unbuilt work — committed inside the document whose job is
to prevent it.

So pass 3 **inverted the order of work**: every instrument was built and executed **before** any document
described it, and the real command output was captured first, to
**`5-instrument-evidence.md`**. A second, weaker corollary follows and is enforced mechanically:

> **Generate, do not type.** Every SITES column and every sweep row is produced by a script from the
> measurement files, and the generating command is recorded next to the output.

## 0.1 A correction to pass 3's own first attempt, recorded rather than quietly fixed

Pass 3's earlier runner wrote `ruleid-sitemap.sh`'s header comment to say phantom hits are *"excluded and
**REPORTED**, never silently dropped."* **That was false as shipped.** The caller discarded the reporting
path with `got=$(measure "$id" 2>/dev/null)`, so the orchestrator's independent run produced **zero**
phantom lines. The claim was true of `gen-expected-sites.sh` and false of the checker. Fixed by giving the
checker a **phantom ledger** that is always printed (2 exclusions, matching the generator's 2), and
re-mutation-tested afterwards. Evidence: `5-instrument-evidence.md` §A1.

---

## 1. The problem, restated after three passes

Three bounces, two shapes, and the owner has named both.

> **R4 — owner ruling, verbatim** *(harness-authored session transcript, record **789**,
> `tool_use_id toolu_01R11yeNtGRvicasDVg9czYo`)*:
> *"if its the same kind of problem that was encountered/fixed in a different section, then the fix that
> was applied in that other section should be applied here; that it didn't catch it in the current section
> in the previous round means nothing."*
>
> **The ratified content of R4 is that sentence and nothing more.** It settles that a known defect class
> resurfacing in a section the previous round's reviewers did not examine is **neither a fresh discovery
> nor a repeat failure** — it is **evidence the earlier fix was applied too narrowly** — and the remedy is
> to **apply the fix that already worked, generalized across the class**.

> **R7 — owner ruling, verbatim** *(transcript record **867**,
> `tool_use_id toolu_01UToKNMx5K1itQdsxtmydbK`, an `AskUserQuestion` result)*: on whether the
> three-question sweep checklist derived from R4 should be ratified, the owner selected
> **"Keep it as a proposal for now."**
>
> **⚠ THEREFORE, EVERYWHERE IN THIS CYCLE'S DOCUMENTS: the three-question (a)/(b)/(c) sweep framing is an
> ORCHESTRATOR PROPOSAL, not an owner requirement.** It may be *used* as a working aid — it is what §1 of
> `2-plan.md` is organised around — but it is **never** cited as something the owner requires, and its fate
> is decided in the R5 spin-off chat where the rule gets its own red-team. Pass 2's `1.5` §1.2 asserted
> three operative commitments derived from R4's sentence; reviewer F/4 called that unratified inflation and
> **R7 confirms F/4 was right**.

### 1.1 The two defect classes, and their status entering pass 3

| Class | One-line shape | Status |
|---|---|---|
| **α** | *a predicate whose operand has no valid producer, or is undefined at a degenerate case* | Recurring. Pass 3's answer is the **86-row generated sweep** (`2-plan.md` §1) whose totality is **enforced by a joiner that exits 1 on any unanswered row**, not asserted in a headline |
| **β** | *the measurement apparatus cannot detect a failed build — and the document says it can* | This is what tripped the cap. Pass 3's answer is §0's rule plus **every instrument built, executed and mutation-tested before this document was written** |

### 1.2 The proven fixes being generalized (not reinvented)

| Defect | The proven fix generalized | Where it already worked |
|---|---|---|
| HG2's approval unproducible in a single-leaf run | an explicit **degenerate-case carve-out** + **write the terminal fact last** | BIND's root carve-out, confirmed CLOSED by two reviewers |
| **Restart with the artifact present and the approval absent has no resume step** (D/6) | the **same** explicit degenerate-case pattern, applied to `stage-done-iff-output-exists` | as above — see item 9 below |
| lock acquired, never released; run 1 deadlocks | name the **counterpart step** + define the **first-run** case | the same (b)+(c) shape |
| `ruleid-sitemap.sh` cannot fail | assert against an expected set, then **exit non-zero** | `idcollide.sh`, which earns can-fail |
| an oracle checks only that a token is *mentioned* | **positive per-site assertion of the operative sentence** | the authoring run's cross-file check |
| replay passes at baseline | **pin the corpus, exclude `changes/`** | the same authoring-run check |
| test arms = one probe from two different agents | **hold the agent constant, vary only the fixture** | reviewer C's own prescription |
| a **site list retyped is a site list unmeasured** (F/1) | **generate the SITES column from the measurement** | new in pass 3: `gen-criteria-table.sh` |
| a **sweep that names its own totality** (D/2: 15 of 21 baseline IDs had no row) | **generate the row set, then enforce the join** | new in pass 3: `gen-sweep-rows.sh` + `gen-sweep-table.sh` |

### 1.3 The four document edits pass 3 owed, and what each one turned out to be

**Item 7 — the cluster map.** `1.5` §5 claimed **3 clusters / 12 spawns**; `fixtures/` holds **4**, and
four gating rows cited an unscheduled arm. Reconciled to **4 clusters × 2 arms × 2 spawns = 16**, with the
count *derived from `ls -d X*/*/`* rather than typed. **X3's inverted polarity: the RULE was fixed, not the
fixture** — pass 2's blanket *"holed ⇒ block and intact ⇒ proceed"* auto-fails X3, whose `holed`-named arm
must **proceed** because IDN's two rules are asymmetric. Renaming X3's arms would have made the blanket
rule true again while **hiding the one asymmetry the cluster exists to test**. The expected verdict is now
declared **per cluster, per arm**, and the pass condition is *"each arm returns its declared verdict **and**
the two arms differ."* Two fixture give-aways reviewer E *demonstrated* were also removed (E/15, E/16) —
see `fixtures/README.md`.

**Item 9 — the restart resume step.** `stage-done-iff-output-exists` marks stage 7 done as soon as
`assembled-plan.md` exists, so a restart with **artifact present + approval absent** reads "done" and
**HG2 never re-fires** — the human gate R2 ratified is bypassed by a crash. Fixed with the same explicit
degenerate-case pattern that closed BIND's root case: **one named exception** to
`stage-done-iff-output-exists`, and the resume step *is* the HG2 ask (`S-RST-RESUME`).

**Item 10 — the HG2 honesty seam.** *"Never self-approved"* shipped **unqualified at 2 of its 4 sites**,
contradicting the spec's own requirement. **The honest position is taken, plainly, and everywhere:** the
approval record is written by an agent, so *never self-approved* is a **duty this loop states, not a
property its mechanism enforces.** Two rows enforce it from both directions — `S-HG2-LIMIT` puts the
qualification at all **7 measured** HG2 sites, and `S-HG2-NOSELF` is a **co-occurrence** row that forbids
the phrase *"self-approved"* appearing in any file that does not carry the qualification. The bare claim is
**gone from `S-HG2`'s pinned string**.

**Item 12 — the `SKILL.md` description budget.** Reviewer E/11's arithmetic (954 + 76 + 180 = 1210 against
a 1024 cap) rested on pass 2 reading its own criterion at **line** granularity. `check.sh`'s obligation is
**per FILE**: a row whose SITES set contains `S` is satisfied by the sentence appearing anywhere in
`SKILL.md`, so neither long sentence was ever owed *inside the description*. What the description genuinely
owes is a **correction** — it currently asserts *"completeness is **PROVEN**, not asserted"* (the overclaim
PRV deletes) and *"a human gate on the top-level split **ONLY**"* (false since R2 added a second gate).
Both are handled subtractively by corpus-wide absence sweeps, and the positive replacement is pinned by
`S-DESC-HG2` at the one file its anchor measures. **Measured, not projected: the corrected description is
997 chars (27 under the cap) and `quick_validate.py` reports `Skill is valid!`** — run on a scratch copy,
because the artifact is deliberately unedited before gate 4. Evidence: `5-instrument-evidence.md` §A4.

---

## 2. OWNER RATIFICATION RECORDS (RAT1)

**Durable source for R1/R2/R3:** the **harness-authored** session transcript JSONL (mode `0600`, written by
the CLI, not by any agent) — options at record **694** (`toolu_01Ga2368vabihTBcFVBZEYte`,
`2026-07-25T14:03:05.318Z`), the owner's selections at record **699**, the `tool_result` keyed to that same
`tool_use_id`. Spot-verified by pass 2's runner and independently re-verified by cold reviewer A.

| # | Ruling | Owner's verbatim selection |
|---|---|---|
| **R1** | SEV4 tie-break → ship narrower | *"Accept risk — ship narrower (Recommended)"* |
| **R2** | F8 → a human reviews the assembled plan (**scope addition**) | *"Yes — human reviews the assembled plan"* |
| **R3** | loop exit → literal | *"Literal — loop until truly nothing surfaces"* |
| **R4** | recurrence of a class in a new section | the one sentence quoted in §1 (record 789) |
| **R6** | how cycle 2 ends after the self-certification cap | *"Authorize pass 3 — narrow and mechanical"* — the owner **declined** the orchestrator's recommendation |
| **R7** | R4's three-question checklist | *"Keep it as a proposal for now"* |

**Honest labels on the two later records.** **R4's record does not meet the bar R1–R3 meet** (F/3): it
quotes no option labels and originally cited an agent-authored file. Its locus is now pinned to transcript
record **789** and it is spot-checkable — but the asymmetry is recorded, not argued away. **R6 was relayed
to this runner by the orchestrator with its record number and `tool_use_id`; this runner did not
independently fetch it.** *Relayed ratification* is the honest label and it is used.

### 2.1 Scope-authority honesty (RAT2 applied to this spec)

`LOOP-STATE.md` calls the broad reading of the owner's original directive an *"Interpretation … stated so
Roy can correct it."* **That hedge is authoritative and is carried here.** Cycle 1's spec dropped it; the
superseded phrasing survives in cycle 1's own frozen records, which are **not rewritten**.

| Level | Covers |
|---|---|
| **Owner-ratified** | R1's narrowing + its parenthetical fix list · R2 (HG2) + its three consequences · R3 · **R4's one sentence** · R6's pass-3 authorization + its scope · R7 |
| **Orchestrator call, within the ratified frame** | the in-scope items not in R1's parenthetical list: `IDN`, `SPV`, `IGM`, `TPL3`, `XPM`, the subtractive `PRV`/`OFL` — **and the (a)/(b)/(c) sweep framing, which R7 leaves a proposal** |
| **This runner's authoring choices** | wording, site placement, the criteria + oracles, HG2's bounce mechanics, the anchor discipline, the §1.4 narrowing |

**PRV's two halves, kept apart (A/F4).** The **subtractive** half (delete *"PROVEN"* / *"proven, not
asserted"*) is in scope. The **positive** half is recorded in `LOOP-STATE.md` as **never closed**, so it
ships **with its limitation attached at the same site, or not at all** (`S-PRV`, `S-PRV-LIMIT`). `OFL`
remains genuinely subtractive.

---

## 3. IN SCOPE

**3A — the confirmed-closed set.** `BIND` (node clause, **dispatcher-recorded** operand, gate artifacts,
immutability + **transitive** rebind; parent clause dropped per §4.1) · `IDN` · `RES` (n ≥ 2 rebinds; a
named exit from *stale ⇒ un-gated*) · `CTX` · `CNC` (lock acquire **and** release, first-run case, lock
**beside** the catalog, **readers** included, **and `catalog-pending/` given a naming scheme**) · `DEP`
(+ the composition rule) · `DEC`/`elc` · `SPV` · `IGM` · `TPL3` · `RST` (root pin **+ the resume
exception**) · `SPN` · seed-skeleton Layer-2 slots · ID hygiene.

**3B — F8, ratified (R2).** `HG2` with the **degenerate-case carve-out**, the **split fact**, the
**resume step** (item 9) and the **honesty seam at every site** (item 10) + `XPM` at all **9 measured**
terminus sites + the forward constraint that any future bottom-up assembly preserve a whole-plan reader.

**3C — subtractive honesty.** `OFL` (stop claiming `off_limits_paths` is an enforced fence) · `PRV`
(soften *"completeness PROVEN"* to **what is actually proven** — that a decontaminated review occurred and
the contract tiers are filled and cited — and state plainly that **N same-model instances are not N
independent minds**) · the record-keeping corrections · **no *"declared deferral"* route anywhere**.

**3D — the measurement discipline itself.** The **generated** 86-row sweep, the **generated** SITES
columns, the **enforced** join, and the vacuous-site guard.

---

## 4. OUT OF SCOPE — declared, not dropped. **None is demoted.**

**F1** (join / terminal-status producer / stage-ordering rework, the `_status.md` schema,
escalate-to-parent, bottom-up assembly, stage 7's actor, and **F6**'s killed-node marker + run-level
abort). *Diagnosis recorded:* write the terminal fact **last**, or split `subtree` into
`planning-complete` + `assembly-complete`. **Forward constraint from R2 stands.**

**F2** (seam-reopen detector) · **F5's mechanism** · **DIV** · the **cost/fan-out envelope** ·
**ECON's O(children²)** · the **"two passes"** ruling (an unaudited owner ruling; stays on the owner queue,
**not** declared settled).

**Recorded for F5, not implemented — and pass 2's discriminator is WRONG, so do not ship it.** Pass 2
recorded *"a genuine owner turn is a `tool_result` carrying the `tool_use_id` of a specific
`AskUserQuestion`."* **Measured counter-example: the owner's R5 directive and his "correct on all counts"
are plain free-text user turns, not `tool_result`s at all**, so that rule would classify the owner's own
directives as non-genuine — while harness task-notifications **also** arrive as `type:"user"` entries. A
correct discriminator needs **three** cases: (i) `AskUserQuestion` results, (ii) genuine free-text owner
turns, (iii) harness-injected notifications.

**Declared gaps inside the sweep (named at their sites, not fixed).** `COV`'s **seam-union** half has no
up-flow producer (`S-COV-LIMIT`); `TOP` remains **defeatable** because stage 1 still pre-creates
`plan/topgate/` (`S-F5-LIMIT`); `ORC` has **no sub-orchestrator death detector** (F6); **`run end` has no
timeout**, so a run whose HG2 ask is never answered has no end (`S-RUNEND`); and an **empty
`required_sections`** makes CMP's tier (ii) vacuous — the same config-key-vacuity class as `S-CTX-VAC`, but
fixing it is new mechanism outside R1's scope, so it is a **DECLARED GAP** in the sweep table.

**The residual pass 3 cannot close, stated because a generator cannot state it.** The sweep's row set is
21 baseline IDs + 60 criteria + **5 predicates that carry no rule ID** (`closed-input-set`,
`stage-done-iff-output-exists`, `path-validation`, `catalog-pending`, `run-end`). An ID-driven generator is
**structurally blind** to those five, so they are listed explicitly in `gen-sweep-rows.sh`. **Three of pass
2's nine blockers were hiding in exactly that blind spot. If a SIXTH such predicate exists, no generator in
this cycle will find it** — only a human or a cold reviewer reading the stage files for predicates rather
than for IDs will. That is the honest residual and it is handed to stage 3 as a named task.

### 4.1 One narrowing carried from pass 2, deliberately

**BIND's parent-`plan.md` clause is DROPPED.** Binding a record to its parent's plan invalidated whole
subtrees on any unrelated parent edit, and the operand that would rescue it — a hash of the parent's
**seam slice** — is F2, deferred. Reviewers **endorsed** the narrowing: it removed the cascade *and* the
root special case.

---

## 5. Constraints

1. **RAT3.** Every stop-for-human **halts this runner and returns the question verbatim**. No
   self-answering, no invented ruling, **no "declared deferral"** — H5's only legal dispositions are a
   representative pre-ship harness or a **named risk-acceptance**, and under RAT3 the latter cannot be
   granted here, so the third move is **HALT + relay**.
2. **Position-sensitive prompt assembly.** New rules go **before** GBP so GBP keeps the recency slot, and
   the rule block's **closing rationale is re-enumerated** to match its actual contents.
3. **Textual stage-0 baseline; word-boundary ID matching; the corpus is pinned and excludes `changes/`** —
   in **one** place (`oracles/lib-corpus.sh`, a literal list, not a glob).
4. **Every shipped oracle carries its executed mutation result.** *A checker that prints is not a checker
   that checks*, and **a test that fails on good input and bad input alike discriminates nothing.**
5. **The skill must still trigger** — `description` ≤ 1024 chars, no angle brackets, trigger vocabulary +
   proactive-suggest clause preserved, **measured**.
6. **Frozen history.** `changes/initial-authoring-2026-07/`, `changes/hardening-cycle-1/`, and passes 1
   and 2's own records (`*.v1-superseded.md`, `*.v2-superseded.md`, the six verbatim reviewer records,
   `3-redteam-plan.md`, `3-redteam-plan.pass2.md`) are frozen.
7. **`charter.md`'s fork-provenance blockquote must stay true** (A/F6) — it is handed to every cold
   reviewer verbatim, so a blockquote that says *"DROPPED: nothing"* without recording what the fork now
   **ADDS** lies to every reviewer.

## 6. Expected touched files

**18 artifact files** — `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/charter.md`,
`stages/stage-{1..8}-*.md`, `templates/seed/{README,generic-node,decomposition-node,leaf-task-spec}.md`,
`examples/authoring-a-skill/{planning,README}.md` — plus the live copy
`/home/zero/.claude/skills/architect/` (re-synced at build), and this cycle's records + instruments.
**Nothing under `Architect/` outside `changes/` has been edited yet** — `git diff` over the artifact set is
empty and HEAD is `b08f5a9`. **`guarded-change.architect.md` was corrected by the orchestrator, not by
this run.**

## 7. Prior art

`3-redteam-plan.{A,B,C,D,E,F}.verbatim.md` (six cold reviews); `changes/hardening-cycle-1/`;
`changes/initial-authoring-2026-07/` (the pinned-corpus cross-file check being generalized);
`Guarded_change/changes/audit-hardening-2026-07/` (positive-per-site assertion + baseline replay).
