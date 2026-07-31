# Stage 1 — Spec (hardening cycle 2, **PASS 2**)

Pass 1 is at `1-spec.v1-superseded.md`. It was bounced at gate 4 (7 blockers; 3 cold reviewers on disjoint
frames; records at `3-redteam-plan.{A,B,C}.verbatim.md`, synthesis at `3-redteam-plan.md`). **No artifact
file was edited in pass 1.**

Pass 2 keeps pass 1's **scope** (the owner ratified it) and its confirmed-good core (BIND's node clause,
IDN, RES for n=1, OFL, `elc`, the ratification records). It **replaces pass 1's governing principle**,
because gate 4 showed that principle had become an exemption rather than a discipline.

---

## 1. The problem, restated after two bounces

Both prior bounces have **one shape**, and the owner has now named it:

> **R4 — owner ruling, 2026-07-25, verbatim:** *"if its the same kind of problem that was
> encountered/fixed in a different section, then the fix that was applied in that other section should be
> applied here; that it didn't catch it in the current section in the previous round means nothing."*
>
> *Durable source:* recorded in `LOOP-STATE.md` with the **session transcript** (harness-authored) as its
> cited source. *Flagged axis:* how to treat a known defect class that resurfaces in a section the previous
> round's reviewers did not examine. *Mapping:* it settles that axis directly — such a recurrence is
> **neither a fresh discovery nor a repeat failure**; it is **evidence the earlier fix was applied too
> narrowly**, and the remedy is to **apply the fix that already worked, generalized across the class**.
> *What it entails, and no more (RAT2):* a fix is **not done when the sections under review pass** — it is
> done when **every site in the class is swept**. It does **not** license new scope, a new mechanism, or a
> per-section invention.

**This dissolves the cap question pass 1 relayed.** The gate-4 blockers are not "the same class twice"
counting toward a cap, nor "a new class" excusing a fresh count — they are **under-generalization**, and the
ruling prescribes the fix rather than a tie-break. Recorded so no later reader re-opens it.

### 1.1 Pass 1's governing principle, and exactly how it failed

Pass 1's principle was *"an operand is computed, not stored"* — classify every fact a predicate reads as
**(i) computable on demand** or **(ii) written by a named stage that provably runs earlier**. All three
reviewers endorsed the principle. **It failed because `class (i)` became an exemption.** The plan said *"a
class-(i) operand has no producer to mis-order"*, and two rows used that sentence to escape the question
*"who writes this?"*:

- the **catalog lock** was labelled class (i) — *"the `mkdir` **is** the test"* — which suppressed *who
  releases it*; the first run **deadlocks against its own acquisition** (B/L2);
- **HG2's approval** was called producible *"after `assembled-plan.md` exists"*, but a **single-leaf run
  never writes that file**, so a leaf-only run can never present — **and that is the mode this hardening
  loop runs itself in** (B/L1).

A `mkdir` is a **mutation**, not a computation. The label was wrong, and the label's exemption is what kept
anyone from noticing.

### 1.2 Pass 2's governing discipline (replaces it)

**GEN — apply the proven fix, generalized, and sweep the whole class.**

Every fix in this pass is required to answer, and `2-plan.md` §1 answers them in **one auditable table over
every predicate and gate in the design — baseline rules included, not only the ones this cycle adds**:

- **(a) Producer** — is the operand produced by a **provably earlier** step? Name the step, name the file.
  **`class (i)` is NOT an exemption from this question:** a class-(i) row must name **the file it computes
  over** *and* **the stage that creates that file**. **No mutation may be labelled class (i).**
- **(b) Degenerate case** — is the predicate defined at **n = 1, the root node, the first run, and the
  empty tree**? A predicate undefined at its degenerate case is the *same* defect as one with no producer.
- **(c) Counterpart step** — does every **acquire / open / begin** have its **release / close / end**
  named, **including on the failure path**?

**GEN's second half is the part both prior cycles skipped:** for each defect found, sweep the design for
**other members of the same class** and fix those in the same pass. The sweep is reported as a table so its
**coverage is auditable**, not asserted.

### 1.3 The proven fixes being generalized (not reinvented)

R4's instruction is to reuse what already worked in this project. Each blocker maps to an existing,
reviewer-confirmed fix:

| Blocker | The proven fix being generalized | Where it already worked |
|---|---|---|
| **B/L1** HG2 unproducible in a single-leaf run | an explicit **degenerate-case carve-out**, plus cycle 1's recorded diagnosis: **write the terminal fact last, or split the fact** | BIND's root carve-out — reviewers A and B confirmed it CLOSED for the identical defect at the root |
| **B/L2** lock acquired, never released; run 1 deadlocks | **name the counterpart step** (who releases, when, on the failure path) **and define the first-run case** | the same (b)+(c) shape as the carve-out |
| **C/O1** `ruleid-sitemap.sh` cannot fail | **assert against an expected set, then exit non-zero** | its sibling `idcollide.sh`, which **earns** can-fail: mutation-tested, non-zero exit, explicit exempt classification |
| **C/O2** R1 is a token-**mention** check · **C/O6** ~11 rows *describe* rather than *pin* | **positive per-site assertion of the operative sentence, verbatim-pinned** — swept across **all** rows, not the 11 flagged | the initial authoring run's cross-file check |
| **C/O3** the replay passes at baseline | **pin the corpus and exclude `changes/`** | the same authoring-run check |
| **C/O4** one probe per arm from two different agents | **hold the agent constant; vary only the fixture** | prescribed by this cycle's own reviewer C |
| **B/L6** BIND's operand is self-reported by the reviewed party | **dispatcher-recorded, not self-reported** | **IDN** — the same fix, in the same records, confirmed closed. R4 in its purest form: the fix exists one field away |

### 1.4 One narrowing pass 2 makes deliberately

**BIND's parent-`plan.md` clause is DROPPED.** Pass 1 bound a record to *both* its node's and its parent's
`plan.md`. Reviewer B showed (B/L8) this invalidates **whole subtrees** on any unrelated parent edit, and
the operand that would rescue it — a hash of the parent's **seam slice only** — is **F2, deferred**. BIND
therefore binds a record to **the node's own `plan.md`**, full stop. Consequences, all good: the
subtree-invalidation cascade disappears; the root case becomes **structural** rather than special-cased (no
record reports a parent hash, so there is nothing to carve out); and one predicate leaves the design.
**Declared as a narrowing, with the deferred operand named.**

---

## 2. OWNER RATIFICATION RECORDS (RAT1) — four, all verified against a harness-authored source

**Durable source for R1/R2/R3, spot-verified by this runner and independently re-verified by cold reviewer
A (`spawn_id aea2863bc75a6d6a5`) before either relied on it:** the **session transcript JSONL**
(`~/.claude/projects/-home-zero-…-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`) — **harness-authored**
(mode `0600`, written by the CLI, not by any agent).
- **Options presented, verbatim:** record **694**, `AskUserQuestion` `tool_use`
  `id: toolu_01Ga2368vabihTBcFVBZEYte`, `2026-07-25T14:03:05.318Z`.
- **Owner's response, verbatim:** record **699**, the `tool_result` **keyed to that same `tool_use_id`**,
  `2026-07-25T14:10:24.209Z`.

**R1 — SEV4 tie-break → "Accept risk — ship narrower (Recommended)".** Ship the confirmed-closed fixes;
F1/F2/F5's mechanisms defer. The option's own presented description bounds the scope and is quoted rather
than paraphrased: *"Cycle 2 ships only the confirmed-closed fixes (BIND over gate artifacts, ID renames,
RES, redteam_context, §4 heading, seed slots, elc, DEP, CNC, root pin); F1/F2/F5's mechanisms defer to a
later cycle."* The deferred blockers are **not demoted** — they remain open, moved out of scope (§4).

**R2 — F8 → "Yes — human reviews the assembled plan"** (a ratified scope **addition**). The option's
presented description, verbatim: *"Adds a second human gate at the end. Directly addresses the finding that
the founding failure WAS caught by a human, yet no human sees anything below the top split. Costs a gate and
requires the assembly fix to preserve a whole-plan reader."* **All three consequences this cycle carries are
inside that text** — (a) a second human gate at the end; (b) the sites asserting the terminus is
gate-before-present-gated **only** become false and must be corrected; (c) the **forward constraint** that
the deferred assembly work preserve a **whole-assembled-plan reader**. *Not entailed, and therefore marked
in the artifact as this cycle's own authoring choice:* **how a bounce routes**.

**R3 — loop exit → "Literal — loop until truly nothing surfaces".** Keep cycling while **any** new finding
appears, including nitpicks, to the 3-cycle bound. Any earlier narrowing is void. *Affirmative evidence
against the CH11 failure mode, noted by reviewer A: the owner **rejected** the author's `(Recommended)`
option here, so these selections are not the author's own picks echoed back.*

**R4 — recurrence of a known defect class in a new section → "apply the fix that already worked,
generalized".** Full record at §1. Its authorized corollary and its limits are stated there.

### 2.1 Scope-authority honesty (RAT2 applied to this spec) — **corrected after A/F4**

`LOOP-STATE.md` calls the broad reading of the owner's original directive an *"Interpretation … stated so
Roy can correct it."* **That hedge is authoritative and is carried here.** Cycle 1's spec dropped it; the
superseded phrasing survives in cycle 1's own records at `hardening-cycle-1/3-charter-given.md:206` and
`hardening-cycle-1/decisions.md:41` — records of what was given at the time, **not rewritten**; the
correction lives here.

| Level | Covers |
|---|---|
| **Owner-ratified** | R1's narrowing + its parenthetical fix list · R2 (HG2) + its three consequences · R3 · **R4's generalize-and-sweep discipline** |
| **Orchestrator call, within the ratified frame** | the in-scope items **not** in R1's parenthetical list: `IDN`, `SPV`, `IGM`, `TPL3`, `XPM`, and the subtractive `PRV`/`OFL` |
| **This runner's authoring choices** | wording, site placement, the criteria + oracles, HG2's bounce mechanics, and the §1.4 narrowing |

**Correction forced by reviewer A (A/F4), recorded rather than defended.** Pass 1 admitted `PRV` to scope on
the rationale that it is *"strictly subtractive — it deletes a claim and adds no mechanism."* **That was
false.** PRV deletes an overclaim **and adds a positive claim** (*"a decontaminated review occurred and the
contract tiers are filled and cited"*) — and that positive half is recorded in `LOOP-STATE.md` as **never
closed** (*"the PRV-positive-half major"*). So:
- PRV's **subtractive half** (delete *"PROVEN"* / *"proven, not asserted"*) stays in scope on the stated
  orchestrator authority.
- PRV's **positive half** is **not** claimed as subtractive and **not** claimed as closed. Every site
  stating it must **also state, at that site, what is merely attested by the constrained party**. The
  positive half ships **with its limitation attached, or not at all** — `S-PRV` makes that a gating
  assertion.
- `OFL` remains genuinely subtractive (A confirmed).

---

## 3. IN SCOPE — pass 1's set, unchanged, plus the generalization duty

**3A — the confirmed-closed set.** `BIND` (node clause, **dispatcher-recorded operand**, gate artifacts,
immutability + **transitive** rebind; parent clause dropped per §1.4) · `IDN` · `RES` (extended to **n ≥ 2
rebinds** and a named exit from *stale ⇒ un-gated*, per B/L7 + B/L5) · `CTX` · `CNC` (lock acquire **and
release**, first-run case, lock **outside** the protected dir, and the accessor enumeration corrected to
include **readers**) · `DEP` (+ the leaf-order composition rule) · `DEC`/`elc` (operand made readable
within ECON; undefined at depth 1, stated) · `SPV` · `IGM` (+ `plan.md.ingested` in the
deterministic-filename list **and** the closed input set) · `TPL3` · `RST` (root pin) · `SPN` (one §4
heading) · seed-skeleton Layer-2 slots · ID hygiene (word-boundary grep, `templates/`+`examples/` scope,
phantom caveat, naming rule, index rows for `TPL1`/`TPL2`/`SEV` + every new ID; `IGM` not `ING`, `KLB`
reserved not `KIL`).

**3B — F8, ratified.** `HG2` (with the **degenerate-case carve-out** and the **split fact**) + `XPM` (all
**six measured** GBP-only terminus sites) + the forward constraint. HG2's approval is **agent-authored**, so
it ships with that limitation **stated at the site** (B/L15) rather than claiming *"never self-approved"* as
a property its mechanism has.

**3C — subtractive honesty.** `OFL` · `PRV` (subtractive half in scope; positive half only with its
limitation) · record-keeping corrections (**8 overclaim occurrences across 4 files**, not 5 — a verbatim
repeat of cycle 1's finding, now fixed; 21 live IDs vs 18 index rows; cycle 1's B0.7 false) · **no
*"declared deferral"* route anywhere**.

**3D — new in pass 2, required by R4.** The **generalization sweep** (`2-plan.md` §1) over **every**
predicate and gate in the design, baseline rules included; and **measured** site lists replacing pass 1's
hand-selected ones (C/O7, B/L11, B/L13, A/F1 were all half-migrations R2 structurally could not see). Also
in scope because they are the same class: `charter.md`'s **fork-provenance blockquote** must stay true
(A/F6), and the rule block's **closing rationale** must be re-enumerated (A/F1 ∥ B/L12).

---

## 4. OUT OF SCOPE — deferred by R1; declared, not dropped. **None is demoted.**

**F1** (join / terminal-status producer / stage-ordering rework, incl. the `_status.md` schema,
escalate-to-parent, bottom-up assembly, stage 7's actor, and **F6**'s killed-node marker + run-level abort).
*Diagnosis recorded for cycle 3:* write the terminal fact **last** (6 → 6.5 → 7 → then write), or **split
`subtree`** into `planning-complete` (6/6.5) + `assembly-complete` (7). **Forward constraint from R2: the
assembly rework must preserve a whole-assembled-plan reader.** *Consequence this pass must live with,
stated:* because the schema is deferred, **`index.md` may not be emptied of its writers** — pass 1 removed
them and stranded `template used` with no destination (A/F3). Pass 2 routes that fact to a file a stage
**already** writes, not to a deferred schema.

**F2** (seam-reopen detector). Its operand — a hash of the parent's **seam slice** — is exactly what BIND's
dropped parent clause needed (§1.4).

**F5** (topgate ratification mechanism). **Now tractable, recorded:** the transcript JSONL is
harness-authored and is the admissible owner locus (an agent-written file — *including `LOOP-STATE.md`* —
is not), **and this cycle found the discriminator**: a genuine owner turn arrives as a **`tool_result`
carrying the `tool_use_id` of a specific `AskUserQuestion`**; a harness task-notification, which also
appears as `type:"user"`, carries no such key. **Honest consequence: TOP remains defeatable after this
cycle** — stage 1 still pre-creates `plan/topgate/`, so its bare-existence predicate is still
self-satisfying. BIND adds a staleness condition only.

**DIV** (frame diversity) — not implemented, **not claimed**; `PRV` states the question is unsettled by this
skill. **The cost/fan-out envelope**; **ECON's O(children²)** parent-seam load; the **"two passes"** ruling
(an unaudited owner ruling; stays on the owner queue, **not** declared settled).

**Carried forward to cycle 3, recorded not fixed:** leaf-level ordering beyond the composition rule;
`tree/root/_status.md`'s writer (needs the deferred schema); and the two orchestrator-owned corrections
already made (`guarded-change.architect.md`'s F8 note; `LOOP-STATE.md`'s stale terminate rule) — **noted as
done, not redone**.

---

## 5. Constraints

1. **RAT3.** Every stop-for-human **halts this runner and returns the question verbatim**. No
   self-answering, no invented ruling, **no "declared deferral"** for an unverified gating criterion — the
   only legal moves are a representative pre-ship harness or a **named risk-acceptance**, and under RAT3 the
   latter cannot be granted here, so the third move is **HALT + relay**.
2. **Position-sensitive prompt assembly.** Pass 1 got this wrong in the direction cycle 1 had already
   fixed: new rules go **before** GBP so GBP keeps the recency slot, and the rule block's **closing
   rationale must be re-enumerated** to match its actual contents.
3. **Textual stage-0 baseline required**; word-boundary ID matching mandatory; the checker's **corpus is
   pinned and excludes `changes/`**.
4. **Oracles must be shown able to fail**, and *"a checker that prints is not a checker that checks."* Each
   shipped oracle carries its mutation result.
5. **The skill must still trigger** — `description` ≤ 1024 chars, no angle brackets, trigger vocabulary +
   proactive-suggest clause preserved, **measured** not assumed.
6. **Frozen history.** `changes/initial-authoring-2026-07/` and `changes/hardening-cycle-1/` are frozen, and
   so are pass 1's own records (`*.v1-superseded.md`, the three verbatim reviewer records,
   `3-redteam-plan.md`).
7. **`charter.md`'s fork-provenance blockquote must stay true** (A/F6): it says the core was *"carried
   whole … DROPPED: nothing"*, and this cycle edits carried core bullets, so it must record what Architect's
   fork now **adds** — or it lies to every cold reviewer that reads it verbatim.

## 6. Expected touched files (joins every cold reviewer's context)

18 artifact files: `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/charter.md`,
`stages/stage-{1,2,3,4,5,6,7,8}-*.md`,
`templates/seed/{README,generic-node,decomposition-node,leaf-task-spec}.md`,
`examples/authoring-a-skill/{planning,README}.md` — plus the live copy
`/home/zero/.claude/skills/architect/` (re-synced at build), and this cycle's records + instruments
(`oracles/{check.sh,baseline-replay.sh,ruleid-sitemap.sh,idcollide.sh,expected-sites.txt}`,
`fixtures/X{1,2,3}/`). **`guarded-change.architect.md` was corrected by the orchestrator, not by this run.**

## 7. Prior art

`3-redteam-plan.{A,B,C}.verbatim.md` (pass 1's three cold reviews — the direct input to this pass);
`changes/hardening-cycle-1/` (the confirmed-closed material); `changes/initial-authoring-2026-07/` (the
pinned-corpus cross-file check being generalized per R4);
`Guarded_change/changes/audit-hardening-2026-07/` (positive-per-site assertion + baseline replay).
