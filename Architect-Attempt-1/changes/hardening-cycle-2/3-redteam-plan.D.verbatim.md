# Stage 3 — cold review record, ARM D (VERBATIM) — **PASS 2**

**Verbatim record** (ART2): the reviewer's raw output, unedited, extracted mechanically from the
dispatcher's tool result. Author's interpretation → `decisions.md`; cross-arm synthesis →
`3-redteam-plan.pass2.md`; charter + closed set → `3-charter-given.pass2.md`.

| Field | Value |
|---|---|
| Arm / frame | **D** — sweep completeness + generalization audit |
| Agent type | `general-purpose` (cold subagent; no shared context with the author, none with the other arms) |
| Model | `claude-opus-5` |
| Dispatch handle (dispatcher-recorded) | tool-use id `toolu_0166q5iyNUzxBKgiBfoSyXR7` — the dispatcher-observed identifier for this spawn |
| Self-reported identity | `spawn_id: unavailable` (declined to invent one — corroboration only, per IDN) |
| Context-file sha256s | in the reviewer's own `## Provenance` section below |

---

# COLD REVIEW — FRAME D · SWEEP COMPLETENESS + GENERALIZATION AUDIT

Target: `2-plan.md` (pass 2) §1 THE GENERALIZATION SWEEP, against the unmodified `Architect/` artifact as the stage order and on-disk contract.

---

## 1. Findings

### **D/1 · BLOCKER · The closed-input-set predicate is absent from §1, and its operands are unproducible at the root and at every node's first pass — the exact class of B/L1, with the exact fix from row 17 not swept to it.**

`stages/charter.md:96-99` (verbatim, given to every cold reviewer):

> Reviewer input is a **closed set**: the node's `plan.md` + its decomposition + child seams, the config's `redteam_context`, **the parent node's plan**, and carried-forward findings from `decisions.md` … **A record missing any of these = the review is treated as un-run.**

`stages/stage-3-completeness-critic.md:62-64`: *"Mechanically check every path handed to a cold agent (`redteam_context`, **the parent plan**, seam files) exists and is readable before the spawn; a dead path is surfaced to the human (RAT3), not silently skipped."* Same duty restated in `stage-4-adversarial-redteam.md:48-49`.

This is a **gate with three operands that do not exist in the degenerate cases** §1 claims to sweep, and it has **no row in §1's 26**:

| operand | absent when |
|---|---|
| the parent node's plan | the node is **the root** (always) |
| child seams / the decomposition | the node is a **leaf** (always) |
| carried-forward findings in `decisions.md` | the node's **first** pass (always) — and D8 *creates* `<node>/decisions.md`, whose first writer is stage 5, i.e. **after** stages 3/4 read it |

The plan proves it knows this fix: row 17 (`2-plan.md:52`) applies it verbatim to `plan.md.ingested` — *"`mode: fresh` ⇒ the file does not exist, and its absence is NOT a missing closed-set input — stated, **else stage 3 deadlocks in fresh mode**"*. That is precisely the sentence the parent-plan operand needs, and the sweep did not carry it one clause to the left. The plan *edits the very sentence* twice without carving it out (`1.5-criteria.md:59` S-IDN-sibling and `:87` S-IGM-closed both rewrite the closed-set list).

**Concrete run — (a), the single-node run, the mode this hardening loop runs itself in:**
1. Stage 1 sets up the run-root, frames `tree/root/`.
2. Stage 2 writes `tree/root/plan.md`; GRN = leaf.
3. Stage 3 validates the paths it is about to hand three cold agents: `redteam_context` ✔, **the parent plan → ENOENT**, seam files → none.
4. `stage-3:64` fires: *"a dead path is surfaced to the human (RAT3)"* → **HALT + relay, on every single-node run, before the first review.**
5. Suppose a human waves it through. The three records are written with a context list lacking the parent plan and the carried-forward findings → `charter.md:99` → **un-run** → GBP never satisfied → the leaf-only run never reaches HG2 at all, so row 22's carve-out is moot.

The author's **own fixture reproduces this**: `fixtures/X1/intact/tree/root/completeness/A.md` has *"## Exact context list given — `- tree/root/plan.md`"* and nothing else. Under `charter.md:96-99` that record is un-run, so the arm's required verdict (*"gated clean ⇒ assemble, incl. the root"*, `fixtures/README.md:13`) is unreachable.

**Fix (one line, the row-17 sentence generalized):** *"the parent node's plan **where one exists**, child seams **where the node decomposes**, and carried-forward findings **where a prior gate has run**; an absence required by the node's position is not a missing closed-set input"* — at `charter.md:96-99`, `stage-3:17-18,62-64`, `stage-4:14-15`, and add the row to §1.

---

### **D/2 · BLOCKER · §1 is not total. 12 of the 21 baseline rule-IDs have no row, and 2 of the 12 new ones. The plan's own provenance claim for the table is false.**

`2-plan.md:217` (Risks): *"§1 is generated from the artifact's own rule set (**the 21 baseline IDs + the 12 new ones**) rather than from memory."* `2-plan.md:30`: *"**Every** predicate/gate in the design after this change."*

Diffing the 21 live baseline IDs (`0-baseline.md:33-55`) against §1's rows: **9 covered, 12 absent.** Full table in §2 below. The omissions are not cosmetic:

- **COV** — a stage-7 *assembly precondition* (`stage-7:28-31`, see **D/3**) with no producer for its operand.
- **SPN** — a gate (`stage-3:43-44`: §4's *"absence is the canonical founding-failure gap and **blocks finalize**"*) that **this cycle edits** (D14, `1.5-criteria.md:90`). A predicate the change touches, with no row in the table that exists to sweep touched predicates.
- **RAT3** — the stop-for-human enumeration at `SKILL.md:83-89` is a closed list, and this cycle adds a new stop (*lock contention → wait → HALT+relay*, `2-plan.md:54`) whose criterion sites are **`s6, M` only** (`1.5-criteria.md:76`). `SKILL.md`'s list is never updated ⇒ a half-migrated rule of exactly the R2/R4 class.
- **PASS1/PASS2** — supply GBP's *"6 record files"* operand (row 1) and are the source of the false (b) answer in **D/16**.
- **SEV** — plan §5 routes the whole build on it; no row.
- **TPL/TPL1** — makes *every node's stage 1* a catalog reader, which is what detonates row 20 (**D/11**).
- Of the 12 new IDs, **PRV** and **OFL** have no row either, though PRV's positive half carries a gating assertion (`1.5-criteria.md:68`).

Under R4's corollary as the spec states it (`1-spec.md:26-27`, *"a fix is not done when the sections under review pass — it is done when every site in the class is swept"*), a sweep table that omits 12 of 21 baseline members of the class it claims to enumerate is the defect itself, not a formatting gap.

**Fix:** generate the row set mechanically from `grep -rlnow` over the corpus (the S-IDGREP command the same cycle installs), not by hand; add the 14 missing rows.

---

### **D/3 · BLOCKER · COV is an assembly precondition whose operand has no producer anywhere on disk — and §1 has no row to notice it.**

`stage-7:28-31`: *"**Total coverage is a precondition (COV).** 'Every node gated clean' includes the **root plan** and every **top-level and deeper split's seams** … **A tree with a clean root but an un-reviewed seam is not assemblable.**"*

Stage 7's mechanical check (`stage-7:10-13`) reads only *"both `completeness/` (3 records) and `adversarial/` (3 records) exist and its `decisions.md` gate entry is clean-or-resolved"*. **Nothing on disk records that a parent's pass covered its children's seams.** The seams live inside the parent's `plan.md` §3 (`stage-2:20-22`), and a record over that `plan.md` is indistinguishable from a record that ignored the seam block.

**Concrete run — (b), root + one leaf, extended to a two-child split:**
1. Root decomposes into `a` and `b`; the seam between them is drafted in `tree/root/plan.md` §3.
2. Root's 3+3 records are written; all three reviewers discuss §1–§2 and never mention §3.
3. Stage 5 gates root clean; stage 6 dispatches; children gate clean.
4. Stage 7 checks 6 records per node ⇒ passes ⇒ writes `assembled-plan.md`, with the un-reviewed seam inside it.
5. HG2 (row 22) presents it. The stated precondition *"a tree with … an un-reviewed seam is not assemblable"* has never been evaluated, because it has no operand.

This is the founding-failure shape (a load-bearing section nobody reviewed, passing a gate that claims to have checked it), it is a baseline rule, and §1 does not list it. RESULT for this run: **completes when it should block.**

**Fix:** either give COV an operand (the record's earned-clean Completeness verdict must name the seam block by section, checkable at stage 5/7) or state at `stage-7:28-31` that COV is a duty, not a checked precondition — and add the row.

---

### **D/4 · BLOCKER · Roughly half of §1's (b) answers end in the word "stated", and no criterion in `1.5-criteria.md` pins any of those sentences — so the degenerate-case column is unenforceable by the build, by the plan's own argument.**

Row 2 states the principle itself (`2-plan.md:37`): *"**n=1 / no decomposition ⇒ TOP NEVER FIRES** — stated explicitly at s6, **because an unstated 'never fires' is indistinguishable from a deadlock**."*

Cross-checking every (b) cell that ends in "stated" against the 57 pinned rows in `1.5-criteria.md` §1:

| §1 row · degenerate-case claim | pinned by a criterion? |
|---|---|
| 1 · empty tree ⇒ no presentable artifact, "stated at s7" | **no** |
| 2 · n=1 ⇒ TOP never fires, "stated explicitly at s6" | **no** (row 48 pins *top-level-only*, not *never-fires-without-a-split*) |
| 3 · first gate ⇒ count 0, "stated" | **no** |
| 5 · a node with neither pass ⇒ un-gated | **no** |
| 6 · empty node dir = not-planned marker | **no** |
| 7 · no records yet ⇒ un-gated | **no** |
| 10 · no decomposition ⇒ approval vacuously satisfied, "stated" | **no** (row 7 pins only the hash clause) |
| 12 · no findings ⇒ `clean`, "stated" | **no** |
| 13 · zero citations ⇒ un-run, "stated" | **no** (and false — see **D/16**) |
| 16 · leaf ⇒ no DAG, no cycle, "stated" | **no** (row 32 pins only the declaration duty) |
| 18 · no proposals ⇒ run end does nothing **and does not take the lock**, "stated" | **no** (rows 27/28 pin acquire/release and first-run, not the no-op case) |
| 20 · — | not even claimed |
| 11, 14, 15, 17, 19, 22, 23 | **yes** (rows 11, 18, 36, 40, 28, 46, 47) |

So **11 of 26** degenerate-case answers are asserted in the plan and observed by nothing. The build can ship without a single one of those sentences and every gating oracle, R1, R2, R3, SC1–SC5 pass. Row 2's own reasoning then applies verbatim: the shipped artifact is one in which *"an unstated 'never fires' is indistinguishable from a deadlock."*

**Fix:** every (b) cell that ends in "stated" needs a pinned string + site in `1.5-criteria.md`, or the verdict cell is not "OK".

---

### **D/5 · BLOCKER · The lock's pid operand has no producer guarantee: `mkdir` and the pid write are two steps, and a kill between them leaves a lock state that neither stale-break branch defines — B/L2 one step further in.**

`2-plan.md:54` (row 19, (c)): *"A held lock whose pid is **alive** is **waited on, then HALT+relay**; only a **dead** pid may be broken, via `BROKEN-BY` + a log entry."* `1.5-criteria.md:76` pins the same as the two exhaustive branches: *"a lock whose recorded pid is **not running** may be broken only by … ; a lock whose pid **IS running** is waited on, and after the stated wait the run HALTS."*

The lock is acquired by *"atomic `mkdir`"* (`1.5-criteria.md:74`). The **pid is a file written inside the directory afterwards** — a second, non-atomic step. Row 19's release promise (*"on success, on every failure path, and before any HALT"*) is a promise about code paths that **run**; a HARDSTOP/SIGKILL runs none.

**Concrete run — (h)/(e) combined, first run on a fresh machine:**
1. Run 1, stage 1: catalog absent ⇒ create the parent, `mkdir <catalog>.architect-catalog.lock` → **wins**.
2. Session-limit death / HARDSTOP **before** the pid file is written.
3. Run 2, stage 1: lock dir exists. Recorded pid: **absent**. Branch "pid is running" — inapplicable. Branch "pid is not running" — the rule says a lock *"whose recorded pid is not running"*; there is no recorded pid, so a conforming reader may not invoke the break path (the pinned string says *"may be broken **only** by"*).
4. Nothing else is defined ⇒ the only legal move left is the conservative one: HALT + relay.
5. Every subsequent run repeats step 3-4. **The catalog is permanently unusable with no in-mechanism exit.**

RESULT: **DEADLOCKS.** This is B/L2's shape — an acquisition with no reachable release — recreated inside the fix for B/L2.

**Fix:** make the pid part of the acquisition (`mkdir` a directory whose *name* carries the pid, or write `pid` then `mkdir` the lock as the commit point) and define *"lock present, pid unreadable ⇒ treat as dead, `BROKEN-BY`"*.

---

### **D/6 · BLOCKER · Restart with the presentable artifact present and the approval absent has no resume step: RST's stage-done rule marks stage 7 done, so HG2's ask never re-fires. B/L4's fix was applied in one direction only.**

Row 23 (`2-plan.md:58`) fixes the false-*complete* direction: *"the run-complete marker is `plan/assembly-approval.md`, **never** the existence of `assembled-plan.md` — else a restart reads 'complete' and **bypasses HG2**."* Criterion 47 additionally **deletes** `stage-7:39`'s *"its existence is the 'run complete' marker"* (paired absence, `1.5-criteria.md:94`).

Nothing replaces it with a resume rule. And `stage-8:13-15` still says: *"**Deterministic filenames → 'already produced?' is a path check.** `… assembled-plan.md` are fixed names. **Stage-done-iff-output-exists** — a node's stage is done **iff** its deterministic output exists."*

**Concrete run — (e), HARDSTOP after the presentable artifact exists but before the human approves (and identically (d), the human never answers):**
1. Decomposed run; every node 3+3 clean; stage 7 writes `assembled-plan.md`.
2. HG2 fires: RAT3 ⇒ **HALT + relay**. `plan/assembly-approval.md` is not written.
3. HARDSTOP (or the human simply never answers and the session dies).
4. Fresh orchestrator resumes per `stage-8:32-33`: *"read `RUN.md` + `index.md`, walk `tree/` for the first node whose expected output is missing → resume there."* Every node's outputs exist ⇒ **no node to resume**.
5. Stage 7: its deterministic output `assembled-plan.md` **exists** ⇒ stage-done ⇒ idempotent no-op (`stage-8:42-43`).
6. `plan/assembly-approval.md` is missing ⇒ the run is **not complete** (row 23) ⇒ the terminus is blocked by XPM.
7. There is no stage whose "expected output is missing", and no stage that owns "re-ask the human". The run is neither resumable nor complete.

RESULT: **DEADLOCKS / unrepresentable.** No criterion observes it: row 47 pins the marker, not the resume action; §6 of `1.5-criteria.md` claims *"A clean run terminating and presenting IS now observed"* — via **X2's intact fixture**, which is handed a tree that *already contains* `assembly-approval.md`, i.e. the post-answer state only.

**Fix:** name the resume rule — *"a restart whose `assembled-plan.md` exists and whose `plan/assembly-approval.md` does not **re-presents at HG2**"* — pin it at `s7`, `s8`, and make `plan/assembly-approval.md` stage 7's terminal deterministic output.

---

### **D/7 · BLOCKER · The X protocol's fix for C/O4 was made in prose only: the fixtures it names are pass-1 vintage, the cluster→criterion map contradicts them, and three of four intact fixtures are in states the design calls un-gated or not-planned — so the required verdicts are wrong and every X-verified row lands at `verified = no`.**

Three independent defects, all mechanically checkable:

**(i) The cluster map contradicts the fixture set.** `1.5-criteria.md:178-179`: *"**Clusters:** **X1** = BIND (all 6 rows) + RES + IDN · **X2** = HG2 + XPM + SC3 · **X3** = CTX + IGM. **12 spawns total.**"* `fixtures/README.md:11-16` defines **four** clusters: X1 = S-BIND, X2 = HG2/XPM/SC3, **X3 = S-IDN + S-RES**, **X4 = S-CTX + S-IGM**. So `1.5-criteria.md:182`'s *"**X3's polarity is deliberately inverted** on the IDN item"* points at a cluster that, under the criteria file's own map, **contains no IDN item**. And `2-plan.md:187`'s budget (*"3 clusters × 2 arms × 2 spawns = 12"*) leaves the fourth existing cluster unbudgeted: 4×2×2 = **16**. Rows 9, 10, 13, 14 (S-IDN, S-RES) name **X1** as their arm, and the X1 fixture does not exercise IDN or RES at all.

**(ii) The fixtures predate the plan they are supposed to verify.** `stat`: `fixtures/README.md` 10:35, all fixture files ≤ 10:35; `1-spec.md` 11:35, `1.5-criteria.md` 11:38, `2-plan.md` 11:40. `fixtures/README.md:13` still describes X1's intact arm as *"the root record reports **no parent hash at all** (the carve-out case)"* — but §1.4 (`1-spec.md:87-93`) **dropped the parent clause entirely**, so "no parent hash" is now universal and discriminates nothing.

**(iii) The intact arms demand verdicts the design forbids.**
- `fixtures/X1/{holed,intact}` contain **`completeness/A.md` only** — 1 of the 6 records `stage-7:11` requires. X1 intact's required verdict is *"gated clean ⇒ assemble, incl. the root"*; a correct agent applying GBP returns **un-gated / do not assemble** on both arms ⇒ *"Both arms the same verdict ⇒ `verified = no`"* (`fixtures/README.md:9`) ⇒ all six S-BIND rows unverified.
- `fixtures/X2/{holed,intact}/tree/root/` has 3+3 records and **no `plan.md`**. Under row 7 the left BIND operand `sha256(<node>/plan.md)` cannot be computed; under `stage-8:18-19` an *"empty / incomplete node dir IS the 'not planned yet' marker"*. X2 intact's required verdict is *"present / exit plan mode"*. Both arms correctly block ⇒ **S-HG2, S-HG2-degen, S-HG2-split, S-XPM and SC3 all land at `verified = no`** — i.e. the entire execution evidence for B/L1's closure evaporates.
- `fixtures/X3/{holed,intact}/tree/root/` likewise has `completeness/{A,B,C}` and **no `plan.md`** and no `adversarial/`.
- `fixtures/X1/intact/tree/root/completeness/A.md` reports only `## reviewed_context_sha256` — there is **no `plan_sha256` field and no dispatcher-recorded hash anywhere in the fixture**. So the only execution arm for S-BIND-cmp exercises the **reviewer-self-reported** operand, which is the pass-1 mechanism D1 replaces per B/L6.

**Fix:** regenerate the fixtures from pass 2's design (6 records per node, a real `plan.md`, a dispatcher-recorded `plan_sha256`), and make the cluster map single-sourced.

---

### **D/8 · MAJOR · Row 15's (a) and (b) answers contradict each other: with self+parent `elc` only, depth 1 has both operands; with "two consecutive levels" you need the grandparent B/L3 said was off-surface. Either way one of the two pinned criteria is false, and the trip threshold has been deleted.**

Row 15 (`2-plan.md:50`) — (a): *"`elc(self)` from own `plan.md`; `elc(parent)` from the parent's `plan.md` … **both written at stage 2**"*; (b): *"**depth 1: no grandparent ⇒ DEC cannot trip**, stated."*

Two `elc` values define **one** level transition. If that is the trip condition, then at depth 1 (parent = root) both operands exist and DEC **can** trip — (b) is false, and `1.5-criteria.md:83` (S-DEC-degen, *"at depth 1 there is no grandparent, so DEC cannot trip"*) is a pinned falsehood. If (b) is right, the condition genuinely needs three levels — the `elc(grandparent)` B/L3 named, which is **not** in the closed input set (`charter.md:96-99` lists the parent's plan only) — and (a) understates the operand set, i.e. **B/L3 is not closed**. `1.5-criteria.md:82` pins both halves of the contradiction into one string: *"one trip condition: **two consecutive levels** fail to reduce, where a node reads its own elc … and its parent's elc …"*.

Second defect in the same row: the pinned string carries **no threshold**, and its paired absence sweeps `a child ≥ 0.8× the parent trips the guard` out of the corpus (`1.5-criteria.md:82`), while the baseline bound lives at `METHODOLOGY.md:220-223` and `stage-6:27-31`. *"Fail to reduce"* is then an undefined predicate — the concrete-bound property `stage-6:47-49` explicitly claims (*"the concrete bound is fixed here so it is checkable, not open-ended"*).

---

### **D/9 · MAJOR · A/F3's fix (route a stranded fact to a file a stage already writes) was applied to `template used` and to nothing else in the same sentence — the granularity decision, `index.md`'s `status` column, and the apex roll-up all lose their destination, the last of them to deferred F1.**

`stage-6:11-12`: *"Record the final decision in `index.md` / the node's `_status.md`."* D8 makes `index.md` **derived** and regenerated by the top orchestrator (`2-plan.md:56`, `1.5-criteria.md:71`: *"`index.md` is derived and never authoritative"*), and `_status.md`'s schema and writer are **deferred** (`1-spec.md:193-194`, `:218`: *"`tree/root/_status.md`'s writer (needs the deferred schema)"*). Both destinations for the granularity decision are gone. Row 21 routes exactly one fact — `template used` — to `plan.md`'s header, and row 4 (GRN) tracks only the *proposal* in `plan.md`, not the recorded final decision.

`METHODOLOGY.md:256` defines `index.md` as *"plan tree + per-node {template used, **status**, gate state, leaf?/decompose?}"*. After the change: `template used` → `plan.md` header ✔; `gate state` → `<node>/decisions.md` ✔; `status` → **nowhere** (deferred `_status.md`); `leaf?/decompose?` → **nowhere** (the stranded fact above). A derived `index.md` cannot be regenerated from producers that do not exist.

Same shape one file over: `stage-7:20` *"**Record completion** in `RUN.md` / the apex `_status.md`"*, and D13 (`2-plan.md:144`) lands *"the apex roll-up to `tree/root/_status.md`"* while the spec concedes its writer is deferred. **A landed fix that is vacuous without deferred machinery.**

---

### **D/10 · MAJOR · B/L6's proven fix (dispatcher-recorded, not self-reported) was applied to `plan_sha256` and not to the rebind chain, which can revalidate any record with the constrained party's own signature and no dispatcher in the loop.**

D1 (`2-plan.md:74-77`): *"**The operand is dispatcher-recorded, not reviewer-reported — the exact fix IDN already applies to identity, generalized to the binding hash per R4 (B/L6).**"*

Row 9 (`2-plan.md:44`) then defines the alternative currency path: *"a chain of `rebound_from`/`rebound_to` in `<node>/decisions.md`"*, producer **"5 → read 5,7"**. Stage 5 is the owning orchestrator — the author. `1.5-criteria.md:53` makes it explicit: *"a record is current if a chain of `rebound_from`/`rebound_to` entries in `<node>/decisions.md` leads from its recorded hash to `sha256(<node>/plan.md)`"*.

**Concrete run — (c), a node fixed in place three times:** each fix-in-place mutates `plan.md`, staling all six records; each is rescued by an author-written rebind entry. After three fixes the six records are "current" with respect to a `plan.md` **no reviewer ever saw**, on the author's own attestation. Row 9's (c) cell answers *"each rebind entry is self-contained"* — which is not an answer to *who writes it and why that is trustworthy*. The self-report defect B/L6 named is one field to the right of where it was fixed.

**Fix:** the rebind entry must be produced by the same non-self-reporting party that records `plan_sha256`, or a rebind must be limited to the `clean-fixed-in-place` arm with the diff recorded and re-reviewed.

---

### **D/11 · MAJOR · Row 20 answers (a) and (b) with "—" in the row whose whole purpose is coverage; its "read a git commit" arm is unproducible on a first run, and generalizing the lock to readers turns every node's stage 1 into a lock contender whose contention policy is a human stop with an unstated timeout.**

`2-plan.md:55` (row 20, verbatim): `| 20 | **CNC catalog READERS** † | the catalog working tree | — | — | every reader takes the same lock, or reads a git commit rather than the working tree | **OK — was B/L9** |`

Two "—" in a table whose governing rule (`2-plan.md:17-21`) is that (a) and (b) must be answered for **every** predicate, and whose §0 declares *"`class (i)` … is not an exemption from any of them"*. What the unanswered cells hide:

1. **(a) has no producer for the "git commit" arm on a first run.** `stage-1:13-14` and `templates/seed/README.md:27-28` say the seed step *"copies this seed set there and runs `git init`"*. `git init` creates **no commit**. `1.5-criteria.md:75` confirms the sequence: *"the seeding step acquires, seeds, git-inits, then releases"* — no initial commit anywhere in the plan or criteria (`grep -n 'git commit\|initial commit'` over both files returns only the run-end TPL3 commit and the `git show` replay). So on run 1 the commit arm is empty and every reader must take the lock.
2. **(b) first run + concurrent second run.** TPL1 (`stage-1:19-22`, `templates/seed/README.md:13-16`) makes **catalog matching a stage-1 duty of every node**, and `1.5-criteria.md:70` declares *"**parallel:** sibling sub-orchestrators"*. So N sibling sub-orchestrators contend on a single global mutex on the common path, and the loser's policy is `1.5-criteria.md:76`: *"after **the stated wait** the run HALTS and relays"*. **The wait is stated nowhere** — `grep -iE 'wait|timeout|seconds|retry'` over `2-plan.md` + `1.5-criteria.md` returns only the two sentences that reference it. A zero-or-short wait converts routine parallel catalog reads into human stops; and that stop is absent from `SKILL.md:83-89` (see D/2).

---

### **D/12 · MAJOR · `catalog-pending/` is a new shared write surface with one writer per node, no naming scheme, no guard, and no place in the restart contract — while §4 claims the accessor enumeration is now complete.**

`2-plan.md:196`: *"The **only** lock is the catalog"*; *"For `index.md`, `_status.md` and the gate logs … the accessor set is reduced to **one writer**, so there is no scope gap."* `catalog-pending/` appears in that section not at all.

Its writers: **stage 6 of every node** (`2-plan.md:140`, `1.5-criteria.md:88`: *"back-propagation stages a proposal into `<run-root>/catalog-pending/`"*). Its reader: *"run end"*. Two consequences:

1. **Lost hole-fix.** Two nodes instantiated from the same seed skeleton (the seed set is three files, `templates/seed/README.md:33-37`, so collisions are the norm) both back-propagate a patch to `generic-node.md`. No naming scheme is specified ⇒ both write the same proposal path ⇒ last writer wins ⇒ one reviewer-found hole-fix is silently dropped, which is precisely what TPL3 exists to prevent (*"a hole caught once is not re-drafted into the next project"*, `templates/seed/README.md:23`).
2. **Partial proposal committed.** Criterion 41's sites are `s6, tp/README, M` — **not `s8`**, so `catalog-pending/` never enters the deterministic-filename list. **Concrete run — (e), HARDSTOP mid-proposal:** a truncated proposal file exists; `stage-8:15` says *"a node's stage is done **iff** its deterministic output exists"*; the restart therefore does not re-stage it; run end commits the truncation to the user's **shared cross-project git catalog**, under the lock, after a "cold review of the proposed diff" that reviews a truncated file.

---

### **D/13 · MAJOR · Row 25's position claim is not what the site sets do: PRV's and XPM's measured sites fall *inside* rules 1 and 3 of the block, so "new rules go BEFORE GBP" is not achievable as specified and the closing rationale's count is again wrong — A/F1 ∥ B/L12 recurring in a section this pass claims to have swept.**

Row 25 (`2-plan.md:60`): *"new rules go **BEFORE** GBP so GBP keeps the recency slot … the block's **closing rationale is re-enumerated to name all five**"*. SC3 (`1.5-criteria.md:128-133`) names the order: *"`CMP` → `PASS1/PASS2` → `PRV` → `HG2` → **`GBP` last**"* — five rule slots.

But the measured site sets put the new text inside the existing rules: `SKILL.md:17` is rule **1**'s first line (`1. **Completeness is proven in three tiers … (CMP).**`) and is a **PRV** site (`1.5-criteria.md:67`, S-PRV-neg: `S:3, S:8, S:17, …`); `SKILL.md:33` is rule **3**'s first line (`3. **Gate-before-present (GBP).**`) and is an **XPM** site (`1.5-criteria.md:99`). So:

- PRV is simultaneously required as a **separate rule between PASS and HG2** (SC3) and as **text inside rule 1** (row 20's site list). These cannot both be satisfied by one block.
- XPM lands inside rule 3, giving the block a **sixth** governed claim while its closing parenthetical (`SKILL.md:39-41`, which currently names three) is re-enumerated to name **five**.

That is A/F1 ∥ B/L12's defect — *a rationale enumerating N over a block holding N+1* — reappearing at the same lines, in the pass that lists it as fixed. By plan §5's own rule (`2-plan.md:209-210`), *"A recurrence in a section this pass claims to have swept is a genuine bounce and is relayed, not argued."*

---

### **D/14 · MAJOR · The HG2 bounce loop is uncapped: CAP has no HG2 clause, and B/L8's uncapped-bounce half is not closed by §1.4.**

Row 22's (c) (`2-plan.md:57`): *"a bounce re-opens the named nodes at **2**"*. Row 3 (CAP) answers (b) with *"**first gate:** no history ⇒ count 0"* and says nothing about HG2. `stage-5:42-46` scopes CAP to *"**2 bounces at the same gate on the same finding class** (same gate + same targeted node section)"* — HG2 is not a node gate and has no targeted node section.

**Concrete run — (c)/(d) combined:** human bounces at HG2 naming node `a` → `a` re-drafts at 2 → 3, 4, 5 → stage 7 re-assembles → HG2 → human bounces again for a related reason → repeat. No counter, no tie-break, no cap. `1.5-criteria.md:97` (S-HG2-authored) declares the bounce route *"this cycle's own authoring choice"* and adds no bound. B/L8's cited claim was *"HG2 bounces make it reachable, **unbounded and uncapped**"*; §1.4 removes the subtree-invalidation cascade and leaves the unbounded-loop half untouched. RESULT: **does not terminate** (bounded only by a human's patience, which is the failure CAP exists to prevent).

---

### **D/15 · MAJOR · Two gating criteria pin contradictory TOP predicates at the same two sites, and §1 rows 2 and 10 do not resolve which holds.**

`1.5-criteria.md:54` (row 7, sites **s6, M**): *"`plan/topgate/APPROVAL.md` records `approved_root_plan_sha256` and **TOP is unsatisfied while that value differs** from `sha256(tree/root/plan.md)`"*.
`1.5-criteria.md:55` (row 8, sites **s6, M**): *"honest limitation: **the bare existence of `plan/topgate/` still satisfies TOP** because stage 1 still creates it, so TOP remains defeatable"*.

Both must appear at `s6` and `M`. A charitable reading exists (TOP = *dir exists* ∧ *if `APPROVAL.md` exists its hash matches*), but neither §1 row 2 nor row 10 states the disjunction, so the artifact will carry two flatly opposed sentences about the same predicate at the same site — the cross-file-contradiction failure mode SC5 exists to catch, manufactured inside one file.

---

### **D/16 · MAJOR · Two (b) answers are false against the source: row 13's zero-citation claim and row 11's "<3 agents ⇒ a declared reduced pass, already the baseline's shape".**

**Row 13 (SPV)** claims *"**a record with zero citations** ⇒ the charter's earned-clean clause already makes it un-run, stated"* (`2-plan.md:48`). `charter.md:68-72` conditions that on a **clean** verdict: *"A clean factual verdict with zero source citations is treated as an **un-run** review."* A record reporting a **blocker** with no citation is not un-run — `charter.md:62` only says the finding *"doesn't count"*. And stage 5's new SPV sample (*"at least one citation per record"*, `1.5-criteria.md:69`) is then unsatisfiable with **no stated consequence**: the node is neither gated nor un-gated.

**Row 11 (IDN)** claims *"**<3 agents:** a declared reduced pass, **already the baseline's shape**"* (`2-plan.md:46`). `grep -rniE 'reduced pass|degraded|fewer than three|two agents'` over the pinned corpus returns exactly one hit: `stage-7:13` — *"Assembly is blocked, **not degraded**."* The opposite provision. `stage-7:11` hard-requires *"`completeness/` (3 records) and `adversarial/` (3 records)"*, and no criterion in `1.5-criteria.md` introduces a reduced-pass route (row 11 covers only `spawn_id: unavailable-by-harness`). So a harness that can spawn only two agents yields a permanently un-gateable node, and the sweep asserts a fallback the artifact does not contain.

---

### **D/17 · MAJOR · Ingest mode cannot complete: the pinned procedure both forbids and provides for authoring an ABSENT section, so every ingest run with an ABSENT row terminates at the cap; row 17's (b) covers only `fresh` mode.**

`1.5-criteria.md:86` (row 39), one pinned string: *"… every `ABSENT` is a candidate hole; **ingest may not author an absent section**, and **anything Architect does author is marked `architect-authored`**."*

**Concrete run — (f):** stage 1 copies the source to `plan.md.ingested`; stage 2 writes the mapping table with §3/§4/§6 = `ABSENT` (exactly the X4 intact fixture). Stage 3's mandate is *"what load-bearing thing is missing — a section, an interface, an output **location** …"* (`stage-3:19-22`) and `stage-3:43-44` makes a missing §4 a finding that *"blocks finalize"* ⇒ blocker/major ⇒ stage 5 routes to stage 2 ⇒ stage 2 **may not author** it ⇒ same finding ⇒ **CAP at 2 bounces ⇒ HALT + relay**. The mode named *ingest-and-**complete*** can never complete an ingested plan with any gap, which is the only reason to run it.

Row 17's (b) cell addresses only *"`mode: fresh` ⇒ the file does not exist"*; ingest mode's own degenerate case (the root **is** n=1 in ingest mode, and its `plan.md` is a mapping table, not a spine) is unaddressed — leaving `stage-7:16`'s *"Preserve the 7-section spine per node"* undefined for an ingest root.

---

### **D/18 · MAJOR · "run end" is not a stage, so rows 18 and 19 cannot answer (a)'s "provably earlier" at all — and with HG2 the run end now sits behind a human answer that may never come.**

Row 18's (a): *"**6** → read at **run end** ✔"*. Row 19: *"Acquired by whichever step needs it (**1** for the seed, **run end** for the commit)"*. §1's own key (`2-plan.md:29-31`) defines `W→R` in *"**Architect's own** numbering (1 … 8)"*, and stage 8 is the restart contract, not a runtime step. There is no stage 9. So the reader step for the only remaining lock holder, and for `catalog-pending/`, is **unlocated in the design** — "provably earlier" is not merely unproven, it is unstatable.

Compounding: row 23 makes the run complete only at `plan/assembly-approval.md`. **Run (d):** the human never answers ⇒ run end never arrives ⇒ `catalog-pending/` is never committed and never expires ⇒ every reviewer-found skeleton hole-fix in that run is lost, with no cleanup counterpart named under (c).

---

### **D/19 · MINOR · Rows 3 and 6 name a step and no file, violating §1's own (a) rule — and D8 relocates row 3's operand.**

`1-spec.md:58` requires: *"Name the step, **name the file**."* Row 3 (CAP) gives *"bounce history … 5 → read 5"*; row 6 (RST) gives *"the deterministic output exists … the stage that writes it"*. Meanwhile D8 partitions the log (`1.5-criteria.md:73`: *"the per-node gate log is `<node>/decisions.md` … `plan/decisions.md` is run-level only"*) while `SKILL.md:61-62` still reads *"Maintain `plan/decisions.md` (append-only: gates, … **cap bounces** …) — **the iteration cap reads this log**"*. Which file CAP counts in after the change is unaudited because the row names none.

### **D/20 · MINOR · DEP's cycle predicate has no detector.**
`1.5-criteria.md:79`: *"a cycle among a node's children is a **blocker at that node's gate**"*, and row 16 lists readers *"4, 7"*. Stage 5 routes on *"the **reviewer's** stated severity"* (`stage-5:32-33`) — so a cycle is caught only if a cold agent happens to notice it. Nothing mechanical checks the DAG, and stage 7 (which must emit a total order) discovers it after the whole subtree is planned.

### **D/21 · MINOR · Row 24 / criterion 52's site set is labelled with a count that matches neither the list nor the measurement, and one line number is off by one.**
`1.5-criteria.md:99` says *"**all 10 measured terminus sites**"* and then lists **14**; `0-baseline.B7-measured-sites.md:38-55` measures *"14 hits in 9 files"*; `1-spec.md:174` says *"all **six measured** GBP-only terminus sites"*. Three numbers for one measured set, in a pass whose thesis is that hand-counted site lists are the defect. Also `ch:132` in the list vs `stages/charter.md:131` in the measurement.

### **D/22 · NITPICK · Row 4 locates the granularity call at "`plan.md` §2", but the 7-section spine has no granularity section.**
`METHODOLOGY.md:118-126` fixes §2 as *"Approach"*; the granularity proposal is a separate stage-2 output (`stage-2:18-22`) with no pinned home in the file BIND hashes and stage 6 reads.

---

## 2. Sweep totality

My own enumeration, from the artifact's text plus the plan's edits, diffed against §1's 26 rows.

**A. The 21 live baseline rule-IDs** (`0-baseline.md:33-55`):

| predicate | in §1? | if absent, what breaks |
|---|---|---|
| GBP | ✔ row 1 | — |
| PASS1 (3 cold agents, gate #1) | **✗** | supplies GBP's "6 record files" operand; row 11's false `<3 agents` fallback (**D/16**) rides on its absence |
| PASS2 (3 cold agents, gate #2) | **✗** | same |
| PASS-ORD | ✔ row 5 | — (but see the row-8 interaction below) |
| CMP (three tiers) | **✗** | tier (ii)'s operand is `required_sections` from the config — the same absent-key class D4 fixes for `redteam_context`, never asked of `required_sections` |
| CMP2 (generative, not checkbox) | **✗** | the earned-clean verdict is the operand of D7's SPV sample; unswept |
| SPN (7-section spine, §4 blocks finalize) | **✗** | **a gate this cycle edits** (D14). No (a)/(b)/(c) asked of the canonical-string predicate at all |
| COV (seam coverage = assembly precondition) | **✗** | **D/3** — operand has no producer; `assembled-plan.md` ships with an unreviewed seam and stage 7 cannot tell |
| ORC | **✗** | who *is* the top orchestrator at "run end" (**D/18**) |
| ECON | partial (inside row 15) | row 21's "top orchestrator walks `tree/` and reads each `plan.md` header" is an O(tree) read never checked against `METHODOLOGY.md:178-184` |
| GRN | ✔ row 4 | — |
| TOP | ✔ row 2 | but contradicted by criterion 8 (**D/15**) |
| CAP | ✔ row 3 | no file named (**D/19**); silent on HG2 (**D/14**) |
| DEC | ✔ row 15 | (a)/(b) mutually contradictory (**D/8**) |
| TPL (seed on first run) | **✗** | the initial-commit producer for row 20's reader arm (**D/11**) |
| TPL1 (match or create-new) | **✗** | makes every node's stage 1 a catalog **reader** — the accessor row 20 claims to cover (**D/11**) |
| TPL2 | ✔ row 18 | "run end" unlocated (**D/18**) |
| TPL3 | ✔ row 18 | `catalog-pending/` accessors unenumerated (**D/12**) |
| RST | ✔ row 6 | `catalog-pending/` + the HG2 resume gap missing from the filename list (**D/6**, **D/12**) |
| RAT3 (stop-for-human list) | **✗** | `SKILL.md:83-89` is a closed list; the new lock-contention HALT is never added (**D/2**) |
| SEV (severity routes) | **✗** | plan §5 routes the entire build on it; a record with no stated severity is undefined |

**Baseline coverage: 9 of 21.**

**B. The 12 new IDs** (`1-spec.md:162-171`): BIND ✔(7-10) · IDN ✔(11) · RES ✔(12) · CTX ✔(14) · CNC ✔(19,20,21) · DEP ✔(16) · IGM ✔(17) · XPM ✔(24) · HG2 ✔(22,23) · SPV ✔(13) · **PRV ✗** · **OFL ✗**.

**C. Predicates with no ID — the author's own flagged blind spot (`2-plan.md:217`):**

| predicate (no ID) | site | in §1? | if absent, what breaks |
|---|---|---|---|
| **closed input set completeness** (*"missing any of these = un-run"*) | `charter.md:96-99` | **✗** | **D/1** — root/leaf/first-pass runs are un-runnable; the class R4 exists for |
| **path validation before spawn** (*"a dead path is surfaced to the human"*) | `stage-3:62-64`, `stage-4:48-49` | **✗** | **D/1** — HALT on every root node |
| **catalog lock pid** | new, `1.5-criteria.md:76` | ✗ (row 19 names the lock, not the pid) | **D/5** — permanent deadlock |
| **`catalog-pending/` accessors** | new, `1.5-criteria.md:88` | ✗ (row 18 names the dir, not its writers) | **D/12** — lost hole-fix + partial commit |
| **`index.md` four-column derivation** | `METHODOLOGY.md:256` | partial (row 21 = 1 of 4 facts) | **D/9** — `status` and `leaf?/decompose?` have no producer |
| **the granularity-decision write** | `stage-6:11-12` | **✗** | **D/9** — both destinations removed/deferred |
| **`RUN.md` / apex `_status.md` completion write** | `stage-7:20` | **✗** | **D/9** — depends on deferred F1 |
| **HG2 restart/resume rule** | new | ✗ (row 23 covers only the false-complete direction) | **D/6** — deadlock after presentable |
| **HG2 bounce cap** | new | **✗** | **D/14** — non-terminating loop |
| **DEP cycle detector** | new | ✗ (row 16 names the DAG, not the evaluator) | **D/20** |
| **rebind-entry author** | new | ✗ (row 9 names the chain, not its writer's independence) | **D/10** — B/L6 un-generalized |
| **lock wait duration** | `1.5-criteria.md:76` (*"the stated wait"*) | **✗** | **D/11** — stated nowhere |

**Total: 14 of §1's own claimed 33 IDs missing, plus 12 ID-less predicates.** The table is not total, and the omissions include three deadlocks and one silent-hole-in-the-assembled-plan.

---

## 3. Row-by-row (a)/(b)/(c) audit

| row | claim checked | true? | evidence |
|---|---|---|---|
| 1 GBP (b) | *"empty tree … stated at s7"* | **unverifiable** | no criterion pins it (**D/4**) |
| 2 TOP (b) | *"n=1 ⇒ TOP NEVER FIRES — stated explicitly at s6"* | **unverifiable, and contradicted** | no criterion pins the never-fires sentence; criteria 7 vs 8 contradict at s6/M (**D/4**, **D/15**) |
| 3 CAP (a) | *"5 → read 5 ✔"* | **incomplete** | no file named, while D8 relocates the log (`SKILL.md:61-62`) (**D/19**) |
| 5 PASS-ORD (a) | *"3 before 4 ✔"* | **true but broken by row 8** | row 8's exit re-runs one pass; a re-run completeness record post-dates the adversarial records, and nothing says a pass-1 re-run invalidates pass 2 (`stage-5:48-50` makes a node missing either set un-gated, not re-ordered) |
| 6 RST (a) | *"the stage that writes it ✔"* | **incomplete** | names no file; `catalog-pending/` absent from the list (**D/12**); stage 7 now has two outputs with different meanings (**D/6**) |
| 7 BIND-cmp (a) | left = class (i) over `<node>/plan.md` @ stage 2; right = dispatcher @ 3,4 → read 5,7 | **TRUE** | `stage-2:3-6` writes `plan.md`; `stage-3:14`/`stage-4:12` are the dispatch points; `stage-5:9`/`stage-7:10` are the readers. The strongest row in the table |
| 9 BIND-rebind (a)/(c) | *"5 → read 5,7 ✔"* / *"each rebind entry is self-contained"* | **(a) true, (c) evades the question** | the writer is the constrained party — B/L6's fix not generalized (**D/10**) |
| 10 BIND-gate-art (b) | *"no decomposition ⇒ vacuously satisfied, stated"* | **unverifiable** | criterion 7 pins only the hash clause (**D/4**) |
| 11 IDN (a) | *"3,4 (dispatcher) → read 5 ✔"* | **TRUE** | `stage-3:14`, `stage-5:9` |
| 11 IDN (b) | *"<3 agents: a declared reduced pass, **already the baseline's shape**"* | **FALSE** | corpus grep: only `stage-7:13` *"blocked, not degraded"*; `stage-7:11` requires 3+3 (**D/16**) |
| 13 SPV (b) | *"a record with zero citations ⇒ … un-run, stated"* | **FALSE** | `charter.md:68-72` conditions un-run on a **clean** verdict (**D/16**) |
| 15 DEC (a) vs (b) | self+parent `elc` / *"depth 1 ⇒ cannot trip"* | **mutually contradictory** | two elc = one transition; `charter.md:96-99` has no grandparent (**D/8**) |
| 16 DEP (a) | *"2 → read 4, 7 ✔"* | **true for the DAG, no evaluator for the cycle** | `stage-5:32-33` routes on the reviewer's severity (**D/20**) |
| 17 IGM (a)/(b) | copied by stage 1 → read 2,3 ✔; fresh-mode absence carved out | **(a) TRUE, (b) partial** | the carve-out is the right fix — and the reason **D/1** is a blocker; ingest's own completion path is contradictory (**D/17**) |
| 18 TPL2/3 (a) | *"6 → read at **run end** ✔"* | **unstatable** | "run end" is not in the 1–8 numbering (**D/18**) |
| 19 CNC lock (a)/(c) | acquire=release step; first-run sibling lock | **materially improved, still holed** | the sibling-not-child fix is real; the pid operand has no atomic producer (**D/5**); the wait is unstated (**D/11**) |
| 20 CNC readers (a)/(b) | **"—" / "—"** | **not answered** | the row that exists to prove coverage answers neither question; the commit arm is unproducible on run 1 (**D/11**) |
| 21 index.md (a) | regenerated by the top orchestrator walking `tree/` | **incomplete** | no step named ⇒ no "provably earlier"; 2 of 4 columns lose their producer (**D/9**) |
| 22 HG2 (a)/(b) | human → recorded after the artifact exists → read at terminus; carve-out for single-leaf | **(b) TRUE — the real fix in this pass** | `1.5-criteria.md:93` pins it; blocked upstream by **D/1** and unverified by X2 (**D/7**) |
| 23 HG2-split (b) | *"the run-complete marker is the approval, never `assembled-plan.md`"* | **TRUE in one direction only** | the bypass is closed; the stuck state is created (**D/6**) |
| 25 SC3 (b) | *"new rules go BEFORE GBP … rationale names all five"* | **FALSE as specified** | S:17 and S:33 are inside rules 1 and 3 (**D/13**) |
| 26 charter prov. (b) | (b) cell contains no degenerate case | **not answered** | `2-plan.md:61` |

---

## 4. Pass-1 blocker closure

| pass-1 blocker | fixed? | generalized or one-spot? | evidence |
|---|---|---|---|
| **(i) B/L1** HG2 unproducible in a single-leaf run | **in text, yes** | **one-spot.** The carve-out is applied to HG2's operand and to `plan.md.ingested` (row 17), and **not** to the closed input set / path validation, where the identical "operand absent by position" defect kills the same single-leaf run one stage earlier | row 22 + `1.5-criteria.md:93` ✔; `charter.md:96-99`, `stage-3:62-64` untouched (**D/1**). Also **unverified**: X2's fixture has no `tree/root/plan.md`, so both arms block (**D/7**) |
| **(ii) B/L2** lock acquired, no release; run 1 deadlocks | **substantially, yes** | **generalized in the right direction, then re-holed.** Sibling-not-child ✔, acquire-step-releases ✔, failure paths + pre-HALT ✔, first-run parent ✔, readers nominally ✔ — but the pid operand has no atomic producer, so a kill between `mkdir` and the pid write deadlocks every later run (**D/5**), the wait is unstated (**D/11**), and the new reader coverage collides with TPL1's per-node read (**D/11**) |
| **(iii) C/O1** an oracle with no failure path | claimed fixed; **not verifiable here** | `oracles/ruleid-sitemap.sh` is **unchanged since 10:18** (pre-dating the 11:38 criteria) and `oracles/expected-sites.txt`, `check.sh`, `baseline-replay.sh`, `lockrace.sh` **do not exist** — the directory holds only `idcollide.sh` and `ruleid-sitemap.sh`. The fix is a plan for an oracle, ranked by frame A |
| **(iv) C/O2** a token-*mention* check | **in text, yes** | generalized: every row pins a verbatim string (`1.5-criteria.md:11`), and mutation 2 makes a mention fail (`:151-153`). Deferred to frame A for whether the strings are the right ones |
| **(v) C/O3** replay passes at baseline | **yes** | `CORPUS` pinned once and `changes/` excluded by construction (`1.5-criteria.md:39-40`, `2-plan.md:178`) — a real generalization (one place, both runs) |
| **(vi) C/O4** one probe per arm from two agents | **renamed, not made** | the prose fix is right (agent held constant, 2 spawns/arm) but the fixtures it names are **pass-1 vintage (≤10:35 vs 11:40)**, the cluster map contradicts them (3 clusters vs 4 dirs; the inversion note points at a cluster with no IDN item), three intact fixtures are in states the design calls un-gated/not-planned, and X1 carries **no `plan_sha256` field at all** — so the only BIND arm exercises the superseded self-reported operand (**D/7**) |
| **(vii) C/O6** ~11 rows describe rather than pin | **yes for the rows that exist** | 57 pinned strings, no *"or equivalent"* — **but the sweep's own degenerate-case claims were never converted into pinned rows**, so 11 of 26 (b) answers are back in the describe-don't-pin class the fix was for (**D/4**) |

Closure score: **2 clean (v, iv-in-text), 2 partial (i, ii), 1 renamed (vi), 1 undelivered (iii), 1 half-generalized (vii).**

---

## 5. Runs walked to death

**(a) Single-node run (root is a leaf: no children, no parent).**
1. Stage 1: run-root + `tree/root/`; catalog absent ⇒ seed under the lock ⇒ release.
2. Stage 2: `tree/root/plan.md`, GRN = leaf.
3. Stage 3 path validation (`stage-3:62-64`): parent plan → ENOENT ⇒ **HALT + relay** (RAT3).
4. Waved through: the three records' context lists lack the parent plan and the carried-forward findings ⇒ `charter.md:99` ⇒ **un-run** ⇒ un-gated ⇒ GBP never satisfied ⇒ HG2 (which row 22 correctly made reachable) is never reached.
**RESULT: DEADLOCKS** (**D/1**).

**(b) Root + one leaf.**
1. Root: stages 1-2, decompose into one child. Root's stage 3 dies as in (a) → same deadlock at the root.
2. Ignoring D/1: TOP fires on the one-child split; `APPROVAL.md` + hash written; child (depth 1) gates clean; DEC — row 15 says it cannot trip, criterion 35's operand set says it can (**D/8**); DEP — one child, no pairs.
3. Stage 7 checks 6 records per node and **not** the seam between root and child (**D/3**); writes `assembled-plan.md`; HG2 presents.
**RESULT: DEADLOCKS at the root (D/1); completes-when-it-should-block on seam coverage (D/3) if D/1 is waived.**

**(c) A node re-drafted after its reviews, then fixed in place three times.**
1. Re-draft at stage 2 → new `plan.md` hash → all 6 records stale ⇒ row 8: re-run that pass. Re-running only the completeness pass makes its records newer than the adversarial ones — PASS-ORD's mtime operand (row 5) now disagrees with the recorded order, and nothing says a pass-1 re-run invalidates pass 2.
2. Three fix-in-place minors: three author-written `rebound_from/rebound_to` entries in `<node>/decisions.md` rescue all six records (row 9 ✔ transitive) — with the currency of every record now attested by the party being constrained (**D/10**).
3. Not counted as bounces; CAP never fires; the node assembles as `clean-fixed-in-place`.
**RESULT: completes — with six records "current" against a `plan.md` no reviewer read.**

**(d) Reaches the presentable artifact and the human never answers.**
1. Stage 7 writes `assembled-plan.md`; HG2 ⇒ HALT + relay; no answer.
2. `plan/assembly-approval.md` absent ⇒ run not complete (row 23) ⇒ XPM blocks the terminus ⇒ correct.
3. `catalog-pending/*` is never committed and never expires: every back-propagated hole-fix in the run is silently lost (**D/18**, **D/12**).
4. On resume: see (e).
**RESULT: blocks correctly at the gate; unrepresentable on resume; silent TPL3 data loss.**

**(e) HARDSTOP mid-mechanism.**
- *mid-BIND compare:* stateless ⇒ recompute. **completes.**
- *mid-rebind append:* `<node>/decisions.md` is append-only, not a "complete deterministic file", so RST's output-exists discriminator cannot see a truncated entry; recovery exists only via row 8's re-run. **blocks, recovers.**
- *mid-lock, after `mkdir`, before the pid write:* **DEADLOCKS** (**D/5**).
- *mid-`catalog-pending` write:* truncated proposal; RST calls the stage done; run end commits the truncation to the user's shared catalog under the lock. **completes with a corrupt shared-state write** (**D/12**).
- *after the presentable artifact, before approval (the case the brief names):* every node's outputs exist ⇒ no node to resume; `assembled-plan.md` exists ⇒ stage 7 is done by `stage-8:15` ⇒ the HG2 ask never re-fires; the approval is missing ⇒ not complete. **DEADLOCKS** (**D/6**).
- *mid-`APPROVAL.md` write:* hash mismatch ⇒ TOP unsatisfied ⇒ re-ask. **blocks correctly** (row 2's hash clause earns this one).
**RESULT: 2 DEADLOCKS, 1 corrupt-write, 3 clean.**

**(f) Ingest-mode run.**
1. Stage 1 copies to `tree/root/plan.md.ingested` (immutable, in the closed set in ingest mode ✔ row 17).
2. Stage 2 writes the mapping table; §3/§4/§6 = `ABSENT`.
3. Stage 3: §4 absent is *the* founding-failure gap (`stage-3:43-44`) ⇒ blocker ⇒ stage 5 ⇒ stage 2, which **may not author it** (`1.5-criteria.md:86`) ⇒ same finding ⇒ second bounce ⇒ **CAP ⇒ HALT + relay**.
4. `stage-7:16`'s *"Preserve the 7-section spine per node"* is undefined for a mapping-table root.
**RESULT: blocks at the cap — the mode cannot complete the thing it is named for** (**D/17**).

**(g) First run on a machine with no catalog, plus a concurrent second run.**
1. Run 1 stage 1: `mkdir -p` the parent; `mkdir` the sibling lock → wins; seed; `git init`; release. **No initial commit is created anywhere.**
2. Run 2 concurrently: `mkdir` → EEXIST; pid alive ⇒ wait *"the stated wait"* — **never stated** ⇒ if the wait is short/zero, **HALT + relay** for a sub-second seed.
3. Every node's stage 1 then matches against the catalog (TPL1) ⇒ under row 20 it must take the same lock or *"read a git commit"* — and on run 1 there is no commit, so all N parallel siblings serialize on one global mutex whose contention policy is a human stop.
4. That stop is absent from `SKILL.md:83-89`.
**RESULT: blocks (correctly on the race, spuriously on contention); the reader coverage claim is unproducible on run 1** (**D/11**, **D/2**).

**(h) A run whose lock holder was killed.**
- *Killed after the pid write:* pid dead ⇒ `BROKEN-BY` + log ⇒ **completes correctly.** This is a genuine fix.
- *Killed between `mkdir` and the pid write:* no recorded pid ⇒ neither branch applies ⇒ **DEADLOCKS**, permanently, on every subsequent run (**D/5**).

---

## 6. Coverage challenge (CH8)

Behaviours this change can alter that **no criterion in `1.5-criteria.md` observes**:

| # | behaviour · scenario | observed by | severity |
|---|---|---|---|
| CH8-1 | **A root/single-leaf node's review is un-run under the closed-set rule.** Run (a) step 3-4. No criterion covers the closed set's positional absences; criteria 12 and 40 *edit* that sentence without carving them out | **nothing** | blocker |
| CH8-2 | **11 of 26 degenerate-case answers can be omitted from the build and every gating check still passes.** §1 rows 1,2,3,5,6,7,10,12,13,16,18 | **nothing** | blocker |
| CH8-3 | **A restart between "presentable" and "approved" never re-asks.** Run (e). Criterion 47 pins the marker, never the resume action; §6's *"a clean run terminating IS now observed"* rests on X2's already-approved fixture | **nothing** | blocker |
| CH8-4 | **A lock with no pid file.** Run (h) variant. `lockrace.sh`'s four declared cases (`2-plan.md:184-186`) are: two racing `mkdir`s, crash-with-lock-held-*and-release-path-run*, first-run, unguarded control — **the killed-before-pid-write case is not among them** | **nothing** | blocker |
| CH8-5 | **`assembled-plan.md` containing an un-reviewed seam.** Run (b) step 3. COV has no criterion and no operand | **nothing** | blocker |
| CH8-6 | **An HG2 bounce loop that never terminates.** Run (c)/(d). CAP's scope is node gates | **nothing** | major |
| CH8-7 | **Two nodes' back-propagations colliding in `catalog-pending/`; a truncated proposal committed.** Run (e) | **nothing** (criterion 41 has no `s8` site and no naming scheme) | major |
| CH8-8 | **The granularity decision and `index.md`'s `status` column having no writer after the change.** Criterion 24 asserts `index.md` is derived; nothing asserts every derived fact has a producer | **nothing** | major |
| CH8-9 | **Parallel siblings HALTing on catalog-read contention.** Run (g) step 3 | **nothing** (criterion 30 asserts the coverage claim, never that the covered path terminates) | major |
| CH8-10 | **An ingest run that cannot complete.** Run (f). Criterion 39 pins the contradiction; nothing observes the outcome | **nothing** | major |
| CH8-11 | **A harness that can spawn only 2 cold agents.** Row 11 asserts a reduced-pass fallback the corpus does not contain and no criterion introduces | **nothing** | major |

**Which of the runs I walked would every criterion in `1.5-criteria.md` still pass?** **All eight.** Every one of runs (a)–(h) — including the three deadlocks and the corrupt shared-state write — leaves all 57 pinned rows, R1–R3 and SC1–SC5 green, because every criterion is an assertion about **text in the corpus**, and the four execution clusters are fed fixtures that never reach any of these states (and, per **D/7**, cannot pass as authored). The criteria set measures whether the sentences are present; nothing measures whether the mechanism they describe terminates.

---

## 7. Ranked list

| # | ID | Sev | Claim |
|---|---|---|---|
| 1 | **D/1** | **blocker** | The closed-input-set + path-validation predicate is absent from §1; its operands are unproducible at the root/leaf/first pass ⇒ single-node runs HALT then go un-gated. Row 17's identical fix was not swept — R4's exact target |
| 2 | **D/2** | **blocker** | §1 is not total: 12 of 21 baseline IDs + PRV/OFL have no row; the *"generated from the 21 + 12"* provenance claim is false |
| 3 | **D/3** | **blocker** | COV is a stage-7 assembly precondition with no operand on disk ⇒ an un-reviewed seam assembles and presents |
| 4 | **D/4** | **blocker** | 11 of 26 degenerate-case answers end in "stated" with no pinning criterion ⇒ unenforceable, by row 2's own argument |
| 5 | **D/5** | **blocker** | The lock's pid has no atomic producer; killed between `mkdir` and the pid write ⇒ a state neither break branch defines ⇒ permanent deadlock (B/L2 one step in) |
| 6 | **D/6** | **blocker** | Restart after presentable, before approval: stage-done-iff-output-exists ⇒ HG2's ask never re-fires; B/L4 fixed in one direction only |
| 7 | **D/7** | **blocker** | C/O4's fix is prose-only: pass-1-vintage fixtures, a contradictory cluster map, three intact arms in states the design forbids, and no `plan_sha256` field ⇒ every X-verified row (all of B/L1's closure evidence) is `verified = no` |
| 8 | **D/8** | major | DEC row 15: (a) and (b) contradict; either B/L3 is unclosed or criterion 36 is false; the trip threshold is deleted |
| 9 | **D/9** | major | A/F3's fix applied to one of two facts in one sentence: the granularity decision, `index.md`'s `status`, and the apex roll-up lose their producers (the last to deferred F1) |
| 10 | **D/10** | major | B/L6's dispatcher-recorded fix not generalized to the rebind chain — the constrained party revalidates its own records |
| 11 | **D/11** | major | Row 20 answers (a)/(b) with "—"; the git-commit arm is unproducible on run 1; TPL1 makes every node a lock contender with an unstated wait and a human stop |
| 12 | **D/12** | major | `catalog-pending/` — a new multi-writer shared surface with no naming scheme, no guard, no place in the restart contract ⇒ lost hole-fix + partial commit to the user's shared catalog |
| 13 | **D/13** | major | Row 25/SC3: PRV and XPM land *inside* rules 1 and 3, so the five-slot order is unsatisfiable and the closing enumeration is wrong again — A/F1 ∥ B/L12 recurring in a swept section (plan §5 ⇒ a genuine bounce) |
| 14 | **D/14** | major | The HG2 bounce loop is uncapped; B/L8's uncapped half is not closed |
| 15 | **D/15** | major | Criteria 7 and 8 pin contradictory TOP predicates at the same sites (s6, M) |
| 16 | **D/16** | major | Two (b) answers false against source: row 13's zero-citation claim; row 11's *"declared reduced pass, already the baseline's shape"* (corpus says *"blocked, not degraded"*) |
| 17 | **D/17** | major | Ingest mode cannot complete: criterion 39 both forbids and provides for authoring an ABSENT section ⇒ every gap ends at the cap |
| 18 | **D/18** | major | *"Run end"* is not a stage, so rows 18/19 cannot answer (a) at all; with HG2 it sits behind an answer that may never come |
| 19 | **D/19** | minor | Rows 3 and 6 name a step and no file, violating §1's own (a) rule while D8 relocates CAP's operand |
| 20 | **D/20** | minor | DEP's cycle predicate has no detector |
| 21 | **D/21** | minor | Criterion 52: *"all 10 measured terminus sites"* lists 14, measured 14, spec says 6; `ch:132` vs measured `ch:131` |
| 22 | **D/22** | nitpick | Row 4 locates the granularity call at *"`plan.md` §2"*; the spine has no granularity section |

**WORST SEVERITY: blocker**

---

## 8. Provenance

**Agent type / model:** `general-purpose` (cold reviewer, frame D) / `claude-opus-5`. **spawn_id: unavailable** (no dispatcher-observable identifier is exposed to this agent; not invented).

**Method note:** all citations were read from the on-disk files in this worktree, not from the plan's quotations of them. Every `file:line` in this report was spot-verified by direct `sed -n`/`grep -n` against the cited file; the mechanical checks I ran myself were: `grep -rniE 'reduced pass|degraded|fewer than three|two agents'` over the pinned corpus (1 hit, opposite polarity), `grep -rn '3 records'` (`stage-7:11`), `grep -iE 'wait|timeout|seconds|retry'` over `2-plan.md`+`1.5-criteria.md` (2 hits, no value), `grep -iE 'git init|initial commit|git commit'` (no initial commit), `find fixtures -type f` per arm, and `stat` mtimes on the fixtures vs the stage artifacts.

**Closed context set — paths read (sha256):**

| path | sha256 |
|---|---|
| `WT/Architect/SKILL.md` | `7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450` |
| `WT/Architect/METHODOLOGY.md` | `f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa` |
| `WT/Architect/stages/charter.md` | `6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819` |
| `WT/Architect/stages/stage-1-frame-template-match.md` | `ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5` |
| `WT/Architect/stages/stage-2-draft-node.md` | `2e76963ce446190ff4bb4d8100a097d8a62e684d5936d38a74e227aea3ad1036` |
| `WT/Architect/stages/stage-3-completeness-critic.md` | `6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e` |
| `WT/Architect/stages/stage-4-adversarial-redteam.md` | `96570a6d9298c67ab6b5fe8653b16cf7068fdbe547373a32bee3e02c0721f07c` |
| `WT/Architect/stages/stage-5-gate.md` | `99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5` |
| `WT/Architect/stages/stage-6-granularity-decompose.md` | `b202101b7b4b16314d4742851138b53efe40b33f3025886149f02ba4aeac1993` |
| `WT/Architect/stages/stage-7-assemble.md` | `864b74dcfcf43e18b576145327beeb011b1e44bb672f7a10e8d8b0f9ad9cb607` |
| `WT/Architect/stages/stage-8-restart-resume.md` | `97431f52e7487ab34c9e9278496b687ca2b4ca2bf178203de3d76151c35762c1` |
| `WT/Architect/templates/seed/README.md` | `d2a86068b92d7ee6b47b7af6dd506f456b589a50a6cac7e0e8d15d23246b3fb4` |
| `WT/.../hardening-cycle-2/0-baseline.md` | `251b008fd1e086fdad8c8374555b3e1b483860f325e71e6d85af5942b6673d10` |
| `WT/.../hardening-cycle-2/0-baseline.B7-measured-sites.md` | `0b8da5013bd624f17d76839cd541556e8c0349900021c0388721039b7a3691a9` |
| `WT/.../hardening-cycle-2/1-spec.md` | `f73326c07af9cc884ccd3ed222ca7017f005cfd31d9d5bfad2ce371f10c6c943` |
| `WT/.../hardening-cycle-2/1.5-criteria.md` | `d3b9d1cfd62249d95a2c954201771a44679cb66b41b2103877827672279217d3` |
| `WT/.../hardening-cycle-2/2-plan.md` | `b5628634e2a798caabeb046589ff0a189109fecf0842867202cde0e9ca50805e` |
| `WT/.../hardening-cycle-2/3-redteam-plan.md` | `953805796fb4d47739467e3556976beb12e3923da06a49ef0dbc8fe95375a5e8` |
| `WT/.../hardening-cycle-2/fixtures/README.md` | `b842147a189f0ff27f9935d40ca66a38bb3cb49c0fde8e1b06d28cd41742ba55` |
| `/home/zero/architect-hardening-loop/LOOP-STATE.md` | `b0b737e3d32eec32fdf7de859544f4097f61b27b3f3a2ce174c21ec425bd0aac` |
| `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` | `aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249` |

Also read (directory listings / file contents, not hashed individually): `WT/.../hardening-cycle-2/oracles/` (contains only `idcollide.sh`, `ruleid-sitemap.sh`, both mtime 10:18), and `WT/.../hardening-cycle-2/fixtures/X{1,2,3,4}/{holed,intact}/**` (full file inventory + `X1/intact/tree/root/completeness/A.md`, `X2/intact/tree/root/decisions.md`).

**Not read** (declared, so the gap is visible): `3-redteam-plan.{A,B,C}.verbatim.md` (the synthesis at `3-redteam-plan.md` was used for pass-1 blocker identity, per the brief's *"do not re-derive them"*); `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md`; `hardening-cycle-1/`; `Guarded_change/stages/*`; `guarded-change.architect.md`; `README.md`; `examples/authoring-a-skill/`; `templates/seed/{generic-node,decomposition-node,leaf-task-spec}.md`. Findings that would have depended on those files are marked "deferred to frame A" rather than asserted. No context outside the closed set was consulted.
agentId: a59ad935d991568db (use SendMessage with to: 'a59ad935d991568db', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 197356
tool_uses: 24
duration_ms: 960207</usage>
