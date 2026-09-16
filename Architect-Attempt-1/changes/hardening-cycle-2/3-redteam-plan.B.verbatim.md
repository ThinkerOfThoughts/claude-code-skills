# Stage 3 — cold review record, ARM B (VERBATIM)

**This file is a verbatim record** (ART2). The reviewer's raw output is reproduced below unedited,
extracted mechanically from the dispatcher's task transcript. The author's interpretation lives in
`decisions.md`; the ranked cross-arm synthesis lives in `3-redteam-plan.md`; the charter given, the exact
context list, and the closed set live in `3-charter-given.md`.

| Field | Value |
|---|---|
| Arm / frame | **B** — failure injection + producer/ordering attack (position + concurrency lenses fire) |
| Agent type | `general-purpose` (cold subagent, no shared context with the author, none with the other arms) |
| Model | `claude-opus-5` |
| **`spawn_id` (DISPATCHER-RECORDED, not self-reported)** | **`a170420f375a3ae9f`** |
| Self-reported identity | `unavailable` (the reviewer correctly declined to invent one; corroboration only) |
| Context-file sha256s | reported by the reviewer in its own `## Provenance` section below, and captured independently at dispatch in `context-hashes.txt` |
| Charter given | the guarded-change charter core verbatim (five lenses + all unconditional discipline bullets + **both** conditional lenses, stated as firing) + the stage-3 additions listed in `3-charter-given.md` |

---

# COLD RED-TEAM REVIEW — Frame B: failure injection + producer/ordering attack
**Artifacts:** `hardening-cycle-2/{2-plan,1.5-criteria,1-spec,0-baseline}.md` · **Source:** the unmodified `Architect/` tree
**WT** = `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

---

## Findings

---

**B/L1 · BLOCKER · HG2's operand is unproducible in a single-leaf run, and the reading stage runs BEFORE the producer — this is cycle 1's cap class, verbatim.**

Evidence:
- `2-plan.md:41` (operand table, HG2 row): producer = *"the human, relayed and recorded at `plan/assembly-approval.md` **after `assembled-plan.md` exists**"*; ordering = *"7 writes `assembled-plan.md` → human → 7 terminus"*.
- `2-plan.md:307-310` (D16/XPM): *"The presentable artifact is `assembled-plan.md` (a decomposed run) or **the root's own `plan.md`** (a single-leaf run). Exit-plan-mode / presenting is blocked by **BOTH** gates … the structural GBP precondition **AND HG2**."*
- `2-plan.md:312-313`: D16's site list places the single-leaf terminus at **`stages/stage-5-gate.md`**.
- A single-leaf run never reaches stage 7: `stages/stage-6-granularity-decompose.md:13-14` — *"**If LEAF** — the node is an atomic, agent-executable task spec. It has no children; planning of this node is done."* `stages/stage-7-assemble.md:3-6` exists only to *"collate the gated-clean plan **tree**"*.
- Compare the cap's recorded shape, `hardening-cycle-1/decisions.md:173-175`: *"terminal `subtree: complete` is assigned to **stage 6/6.5** but conditioned on `_assembled.md`, a **stage-7** output — stage 6 runs *before* stage 7, so the write has no valid producer position."* Cycle 2 has produced the mirror image: the **reader** is stage 5, the operand's production is conditioned on a **stage-7** write.

Run that dies (run (a), single-node — the mode `LOOP-STATE.md:19-21` says this loop runs *itself* in):
1. Stage 1 → `tree/root/`, `plan/topgate/` (empty), `index.md`.
2. Stage 2 → `tree/root/plan.md`, granularity = **leaf**, `elc` declared.
3. Stages 3, 4 → 6 records, each reporting `sha256(tree/root/plan.md)`; parent clause **N/A** (the root carve-out works).
4. Stage 5 → BIND-current, SPV recorded, `clean`. **Stage 5 is also the terminus for this run** (`2-plan.md:312`).
5. XPM: presenting requires **GBP ∧ HG2**. GBP ✓. HG2's operand is `plan/assembly-approval.md`, whose stated producer trigger is *"after `assembled-plan.md` exists"*.
6. Stage 6 → LEAF, done. `assembled-plan.md` is **never written**. There is therefore no state in which the human "reads the assembled plan", and no stage that can write the approval.
7. **The run can never present.** `RESULT: DEADLOCKS.`

Fix: state at `stage-5-gate.md` that for a single-leaf run HG2 fires on `tree/root/plan.md` itself, and add an operand-table row whose producer trigger is *"after the root's `plan.md` is gated clean"* — i.e. give the single-leaf terminus its own producer, at a stage that runs no later than its reader.

---

**B/L2 · BLOCKER · The catalog lock has no release. Run 1 deadlocks against itself; `class (i)` is a mislabel that stopped the table from asking for the producer.**

Evidence:
- `2-plan.md:43` (operand table): *"the catalog lock (`.architect-catalog.lock`) | **(i)** | an **atomic `mkdir`** at acquisition time … | stage 1 (seed), run end (commit) | **n/a — the mkdir *is* the test**"*.
- `2-plan.md:198` (D8): *"holding an exclusive lock: atomic `mkdir <catalog>/.architect-catalog.lock`, holder records run-root + pid inside it. **The first-run seed + `git init` takes the same lock.** A stale lock whose pid is **dead** may be broken only with … a `BROKEN-BY` file."*
- `grep -n "releas\|rmdir\|unlock\|wait\|retry" 2-plan.md 1.5-criteria.md` → **zero hits** on any of those senses. There is no release, no wait policy, no retry policy, and no stop-for-human for a held lock.
- `stages/stage-1-frame-template-match.md:13-14` is the seed site: *"If the user-space catalog … does not yet exist, **seed it** … and `git init` it."*

Run that dies (run (g), single machine, single run — no concurrency needed):
1. First-ever Architect run. Stage 1: `mkdir ~/.claude/architect/templates/.architect-catalog.lock` → succeeds; run-root + pid written inside.
2. Seed copied, `git init` done. **Nothing releases the lock** (no stage is assigned the `rmdir`).
3. Run proceeds; TPL2/TPL3 proposals accumulate in `catalog-pending/` (`2-plan.md:44,246-247`).
4. Run end: the top orchestrator attempts `mkdir <catalog>/.architect-catalog.lock` → **EEXIST**.
5. The break rule requires *"a stale lock whose pid is **dead**"*. The pid inside is the run's **own live pid**. Not stale ⇒ may not be broken.
6. No wait/retry/HALT is specified. **The end-of-run catalog commit can never execute**, so D12's entire staging mechanism is inert and TPL2/TPL3 silently never land. `RESULT: DEADLOCKS` (or, on the charitable reading, silently drops the commit — which makes D12/S-TPL3 vacuous).

Second failure in the same row: the lock's path is *inside the directory it protects*. On a genuine first run `<catalog>` does not exist, so `mkdir <catalog>/.architect-catalog.lock` fails with ENOENT for **every** contender — the lock cannot protect the creation of its own parent. The only workable split (`mkdir -p <catalog>` unlocked, then `mkdir …/.lock`) leaves a window in which a second run sees `<catalog>` exist, takes the *not*-first-run path at `stage-1:13`, skips seeding, and matches TPL1 against a half-copied catalog.

Note on the mislabel: `mkdir` is a **mutation**, not a computation. Calling it class (i) invoked the plan's own exemption — *"A class-(i) operand has **no producer to mis-order**"* (`2-plan.md:13-14`) — and that exemption is exactly what suppressed the question "which stage writes the release, and does it run before the next acquisition?". This is the anti-cap principle being *evaded by classification* rather than satisfied.

Fix: reclassify the lock as class (ii); name the releasing stage for both acquisitions; state the on-held-lock policy (bounded wait → HALT+relay under RAT3); acquire on `<catalog>`'s parent, not inside `<catalog>`.

---

**B/L3 · MAJOR · DEC's trip condition needs a third generation's `elc`; the stated reader cannot see it, and there is no depth-1 carve-out — the same defect class as BIND's missing root carve-out, reproduced.**

Evidence:
- `2-plan.md:38` (operand table): *"`elc` … | (ii) | **stage 2** — the node's own owner declares it in `plan.md` §2 | **the child's** stage 6 (DEC) | 2 → 6 ✔"*.
- `2-plan.md:224` (D10): *"**ONE trip condition:** **two consecutive levels** with `elc(child) ≥ 0.8 × elc(parent)` ⇒ escalate."*
- Two consecutive levels requires the (grandparent→parent) ratio **and** the (parent→child) ratio. At the child's stage 6 the operands are `elc(child)`, `elc(parent)`, **and `elc(grandparent)`**.
- `METHODOLOGY.md:178-184` (ECON): a (sub-)orchestrator holds *"only **its own subtree's** skeleton + inter-node **seams** + terse child `_status` roll-ups"*; `stages/charter.md:97-98` and `stage-3:18` give the closed set as *"the **parent** node's plan"* — singular. `elc(grandparent)` is in no reader's surface.
- No alternative operand is tabulated. If the intended operand is instead *the parent's already-computed ratio*, that is a class-(ii) fact with **no row and no named producer** — `2-plan.md:26` claims *"Nothing in §2–§3 reads a fact absent from this table."*
- At depth 1 (a child of the root) there **is** no grandparent, so the condition is undefined — precisely the carried-forward blocker shape at `hardening-cycle-1/decisions.md:177-178` (*"BIND's parent-hash clause has **zero** root carve-out"*), fixed for BIND and reintroduced in DEC.

Run that dies (a non-reducing 4-level tree):
1. Root `elc=40`; child A `elc=38`; A's child B `elc=36`; B's child C `elc=35`.
2. A's stage 6: needs `elc(root)`, `elc(A)`, and `elc(grandparent-of-A)` — none exists. Condition undefined ⇒ no escalation.
3. B's stage 6: needs `elc(root)` — outside B's owner's surface under ECON ⇒ not computable ⇒ no escalation.
4. Recursion continues with 6 cold agents per node per level. `RESULT: the convergence guard never trips` — an unrepresentable predicate, and the runaway DEC exists to stop.

Fix: make DEC's operand a single per-node recorded ratio (`elc_ratio_to_parent`, class (ii), written by the node's own stage 2/6 and read by its **child's** stage 6 — two facts both inside the reader's surface), and state the depth-1 carve-out explicitly the way BIND's root carve-out is stated.

---

**B/L4 · MAJOR · HG2 is bypassed by a restart: three baseline sites make `assembled-plan.md`'s existence mean "run complete", and none is a `B4` CHANGE row, so `R2` cannot require their migration.**

Evidence:
- `stages/stage-7-assemble.md:39-41`: *"`assembled-plan.md` is the deterministic output name; **its existence is the "run complete" marker**. A restart before it exists resumes the first un-gated node; **a restart after it exists is a no-op**."*
- `METHODOLOGY.md:239` and `stages/stage-8-restart-resume.md:14-15`: `assembled-plan.md` is in the fixed-name list under **"Stage-done-iff-output-exists"**.
- `0-baseline.md:92-113` — **none of the 20 CHANGE rows P1–P20 names any of these three sites.** P11 (the terminus row) cites only `SKILL.md:33`, `METHODOLOGY.md:149`, `METHODOLOGY.md:316`.
- `1.5-criteria.md:259` — S-XPM's only absence sweep is *"No site asserts the terminus is GBP-gated **only**"*. "Existence of `assembled-plan.md` = run complete" is not that string and is not swept.

Run that dies (run (e), HARDSTOP inside HG2):
1. Decomposed run, every node clean. Stage 7 writes `assembled-plan.md`.
2. HG2 fires: HALT + verbatim relay (`2-plan.md:296-299`). Orchestrator relays; no answer yet; `plan/assembly-approval.md` absent.
3. Session cap kills the orchestrator — the documented, routine event (`LOOP-STATE.md:36-38,244-245`; `FINDINGS.md` meta-obs 5).
4. Fresh orchestrator resumes per `stage-8:32` (*"read `RUN.md` + `index.md`, walk `tree/` for the first node whose expected output is missing"*). Nothing is missing.
5. It reads `stage-7:41` — *"a restart after it exists is a **no-op**"* — and `stage-8:15`, stage-done-iff-output-exists. **It concludes the run is complete and presents.** `RESULT: HG2 silently bypassed` (worse than a deadlock: the gate reports success).

Fix: add these three sites to a `B4` CHANGE row and require, positively, that *"`assembled-plan.md`'s existence marks stage 7 done, **not the run**; the run is done only when `plan/assembly-approval.md` also exists"*, with `S-HG2` asserting it at each.

---

**B/L5 · MAJOR · "stale ⇒ un-gated" names a state with no exit route: no stage is assigned to produce the transition out.**

Evidence:
- `2-plan.md:71-72`: *"A non-current record is **stale ⇒ un-run**: the node is **un-gated** at stage 5 and **assembly is blocked** at stage 7."*
- `stages/stage-5-gate.md:22-34` — the severity table's complete route set is blocker→2, major→2, minor→fix, nitpick→log, clean→6. **There is no `un-gated` row and no route.** `stage-5:49-50` likewise only says a node missing a pass *"is **un-gated**, not clean"* — a state, never a transition.
- `1.5-criteria.md:59-60` (X1) stops at the same place: *"holed ⇒ 'records stale / node un-gated / do not assemble'"*. No criterion asks what the run does next.
- Sub-conflict at the same seam: `2-plan.md:73` declares *"**Records are immutable**"* while `2-plan.md:85-86` redefines stage-done for a record as *"the deterministic output exists **and** it is BIND-current"* — so a restart must re-dispatch stage 3 and **overwrite six complete, immutable records**. If "immutable" wins, stage 3 can never become done and the node is stuck; if the restart wins, immutability is not a property.

Run that dies (run (c), re-draft then fix-in-place, with a HARDSTOP):
1. Node gated; stage 5 finds a minor; RES(a) edits `plan.md` (H1→H2) — **stage 5 is now a writer of `plan.md`, a producer absent from both the operand table and D8's partition**.
2. HARDSTOP after the `plan.md` write, before the `rebound_from`/`rebound_to` entry is appended to `<node>/decisions.md`.
3. Resume: `plan.md` exists (stage 2 done); the six records exist but report H1 ≠ H2 and no rebind entry rescues them ⇒ **BIND-stale ⇒ un-gated**.
4. Stage 5's route table has no `un-gated` route; stage 8's walk sees no *missing* deterministic output, so it does not resume anything. `RESULT: unrepresentable state — no stage can produce "gated" from here.`

Fix: add an explicit route — *"BIND-stale records ⇒ route to stage 3 (both passes re-dispatched); the stale records are superseded in place and the supersession logged"* — and reconcile it with the immutability sentence.

---

**B/L6 · MAJOR · BIND's binding operand stays self-reported by the very party it constrains, while IDN de-self-reports identity for exactly that reason.**

Evidence:
- `2-plan.md:33` (operand table): *"the record's **reported** context-file sha256 map | (ii) | **stage 3 / stage 4**, inside the record it writes (the charter **already** mandates this field at `charter.md:96`)"*. Verified: `stages/charter.md:96` — *"(v) the **reviewer-reported** sha256 of each context file it read"*.
- `2-plan.md:93-94` (D2), the opposite discipline for identity: *"`spawn_id` = the identifier the **dispatcher** observed at spawn … **not** self-reported. A reviewer's own claim about its identity is a separate, optional `self_reported_identity` field, **corroboration only**."*
- BIND's entire discriminating power therefore rests on a hash the reviewed agent volunteers. A reviewer that copies the hash from a sibling record, or from the prompt, produces a permanently "current" record. `2-plan.md:102-103` bans *reading* a sibling record but nothing makes the binding operand independent of the reviewer.
- `1.5-criteria.md:57-60` (X1) pre-supplies an honest mismatch (*"`completeness/A.md` reports a `plan.md` sha256 that does not match"*). **No fixture models a dishonest or copied hash** — the same fixture defect cycle 1's coverage challenge named (`hardening-cycle-1/decisions.md:193-194`: *"every fixture pre-supplies the terminal facts whose producers are broken"*).

Run that dies:
1. Node re-drafted (H1→H2) after its passes; stage 3 re-dispatched.
2. A reviewer reports `plan.md: <H1>` (copied from the carried-forward context, or fabricated).
3. BIND compares reported H1 vs computed H2 → mismatch → correctly stale. Now the inverse: the reviewer reports the *current* hash while having actually read a cached older copy handed to it. BIND passes. `RESULT: completes — with the binding defeated`, and no criterion can see it.

Fix: make the binding operand class (i) at dispatch time — the **dispatcher** records `sha256(plan.md)` at spawn into the record's provenance; the reviewer's own report becomes corroboration only, exactly parallel to IDN.

---

**B/L7 · MAJOR · Two or more in-place fixes make a node permanently un-gateable — and the criteria's own "four fixed minors" state is that state.**

Evidence:
- `2-plan.md:74-77`: *"a **new gate-log entry** carrying `rebound_from: <old sha256>` and `rebound_to: <new sha256>`; BIND then accepts a record whose reported hash appears in a `rebound_from` whose `rebound_to` **equals the current `sha256(plan.md)`**."* There is **no transitive clause**.
- `2-plan.md:110-111` (D3a) requires the entry to be *"traceable to a **specific reviewer finding ID**"* — i.e. per-finding entries.
- `2-plan.md:118-120` and `1.5-criteria.md:87-88` both use as the motivating case *"a node carrying **four fixed minors** and a demoted major"*, and assert *"**All three states are assemblable**"*.

Run that dies:
1. Records report H1. Stage 5 fixes minor M1 in place → entry 1: `rebound_from: H1, rebound_to: H2`.
2. Fixes M2 → entry 2: `rebound_from: H2, rebound_to: H3`. M3 → H4. M4 → H5.
3. BIND at stage 5/7: records report **H1**; current is **H5**. The entry with `rebound_from: H1` has `rebound_to: H2 ≠ H5`. The entry with `rebound_to: H5` has `rebound_from: H4`, which no record reports.
4. Node is BIND-stale ⇒ un-gated ⇒ **not assemblable**, contradicting `2-plan.md:120`, with no route out (B/L5). `RESULT: unrepresentable state — the plan's own showcase fixture cannot assemble.`

Fix: one line — either *"rebinds compose transitively: BIND follows the `rebound_from`→`rebound_to` chain"*, or *"each rebind entry records the **original** reported hash as `rebound_from`"*.

---

**B/L8 · MAJOR · BIND's parent clause is an undeclared whole-subtree invalidator; its rescuing operand is absent from the table; and the HG2 bounce makes it reachable, unbounded, and uncapped.**

Evidence:
- `2-plan.md:68-71`: *"where the record also reports the parent's `plan.md` — iff that equals `sha256(<parent>/plan.md)` computed now."* Every non-root node's six records report the parent's hash, because `stages/charter.md:97-98` puts *"the parent node's plan"* in the closed set and `charter.md:96` mandates a hash for each context file read.
- The rescuing operand for a stale *parent* hash is the **parent's** rebind entry in `<parent>/decisions.md`. `2-plan.md:36` tabulates `rebound_from`/`rebound_to` with reader *"5 (immediately), 7"* — the **node's own**. No row gives a child's stage 5 the right to read its parent's gate log, and `2-plan.md:197` partitions the gate log per node. **A predicate reads a fact absent from the table.**
- Reachability: `2-plan.md:303` (D16, RAT2-flagged) — *"how a bounce routes — it re-opens the node(s) the human names, **at that node's stage 2**."* A human bounce naming the root rewrites `tree/root/plan.md`.
- No bounce record, no counter: `stages/stage-5-gate.md:42-46` scopes CAP to *"2 bounces at the same gate"* counted from a gate log; `2-plan.md:197` reserves `plan/decisions.md` for *"the top-split approval, the assembly approval, run-level aborts"* — **an HG2 bounce is not among them**, and `2-plan.md:41` records only the approval, never a bounce.

Run that dies (an HG2 bounce loop):
1. 12-node tree, all clean, assembled. HG2 bounce: "the root's framing is wrong."
2. Root re-opens at stage 2 → `tree/root/plan.md` rewritten.
3. Every one of the 11 descendants' 66 records reported the **old** root hash ⇒ all stale ⇒ every node un-gated ⇒ 66 fresh cold agents.
4. Root's own stage 6 re-runs: TOP is now unsatisfied (`2-plan.md:79-81`, `approved_root_plan_sha256` ≠ new hash) ⇒ **a second human gate round-trip that D16 claims fires "at the top level only"**.
5. Re-assemble; HG2 fires again; the human bounces again. **No bounce is recorded anywhere and CAP counts nothing**, so step 1–5 repeats without bound at 66 agents per iteration. `RESULT: unbounded loop; no cap, no record, no terminating condition.`

Fix: give HG2 a bounce record in `plan/decisions.md` and bring it under CAP; state that BIND's parent clause is satisfied by *either* the current parent hash *or* a parent rebind entry, and tabulate that cross-node read; state the parent-re-draft invalidation cost explicitly (it is a crude `seam_rev`, which is deferred F2 work arriving by accident).

---

**B/L9 · MAJOR · The accessor enumeration is writer-only and undercounts; the guard's scope omits every reader.**

Evidence (my own enumeration is in the Concurrency lens section below; the specific errors):
- `2-plan.md:195` claims `index.md` has *"**four** writers, **all parallel**"*, citing `stage-1…:20`, `stage-6…:11-12`, `METHODOLOGY.md:195`, `templates/seed/README.md:14`. All four verified — but **`stages/stage-1-frame-template-match.md:12`** (*"Create the run-root … `RUN.md`, `index.md`, `config/planning.md` …"*) and **`stage-1:44`** (*"Everything **this stage** produces is on disk (`index.md`, …)"* — a cross-cutting rule in a **per-node** stage) are two further write sites, and `stage-1:12` is explicitly *"top orchestrator, **first node only**"* — **not parallel**. Both halves of the claim are wrong.
- The gate-log row (`2-plan.md:197`) cites only `stage-5…:19` and `SKILL.md:61-62`. It omits **`stage-6:29`** / **`METHODOLOGY.md:222`** (a DEC escalation *"append a `decisions.md` escalation"*) and **`charter.md:139`** / **`stage-5:33`** (the contest entry). `0-baseline.md:102` (P9) repeats the same short list, so **R2 cannot require those sites to migrate.**
- **`<node>/plan.md` is not in the partition table at all**, yet D3(a) makes **stage 5** a writer of it alongside stage 2 (`stage-2:46`: *"`plan.md` is the node's durable state"*), and that write is what invalidates every descendant (B/L8).
- The catalog row enumerates writers only. **Readers are uncovered**: `stage-1:19-20` has *every node* read the catalog for a TPL1 match, in parallel across siblings; `templates/seed/README.md:13-16`, `METHODOLOGY.md:194` state the same duty. A TPL1 read concurrent with another run's seed-copy or end-of-run commit is the uncovered window. `2-plan.md:406-408` asserts the lock's scope *"cover[s] **three** access paths that a naive version misses"* — mid-run commits, concurrent runs, first-run seed — **all three are writes**. `stages/charter.md:112` requires *"**every concurrent reader and writer**"*.
- `BROKEN-BY` (`2-plan.md:198`) is written *"so the victim run can see it"* — **no stage is assigned to read it**, and it is not in the operand table. A fact with no reader is not a mechanism.

Run that dies: run A `mkdir -p <catalog>` (unlocked); run B wins the lock and begins the seed copy + `git init`; run A's stage 1 sees `<catalog>` exists, takes the not-first-run path, and matches TPL1 against a half-populated catalog — either instantiating a truncated skeleton or recording `create-new` for every node. `RESULT: completes with corrupt input; the guard never fires because reads are outside its scope.`

---

**B/L10 · MAJOR · S-CNC's advisory relabel rests on a factually false premise — the one genuine lock IS executable, and this repo has already executed a real git catalog.**

Evidence:
- `2-plan.md:410-413`: *"**There is nothing to execute:** the accessors are *prompt instructions to agents*, not code, so there is no runnable read→write window to inject a competing mutation into."* Same claim at `1.5-criteria.md:166-171`.
- False for the catalog: `mkdir`/`git commit` on `~/.claude/architect/templates/` are ordinary filesystem and git operations. Two shells, one `mkdir` each, is a complete deterministic interleaving harness.
- **The precedent is in this repo's own records.** `changes/initial-authoring-2026-07/8-harness.md:55`: *"**YES (executed)** … ran under `8-harness-runs/B5-catalog/` (seeded from `templates/seed/`, `git init`) … a hole-fix was back-propagated to the skeleton and committed — new commit `78e8c96` … atop seed commit `e6a6340`."* A real git catalog was already driven end-to-end by a prior harness.
- The bar the relabel dodges: `Guarded_change/stages/stage-1.5.md:78-89` (ST1.5e) — *"the criterion must be checked **deterministically** — by *injecting* the competing mutation into the middle of the guarded window … a test that passes with and without the guard proves nothing"*; `Guarded_change/stages/stage-8.md:33-40` (H4) — *"a pure-inspection 'verification' of such a criterion counts as `verified = no`"*; and `stage-8.md:146-152` (FRZ) — any weakening *"is audited exactly like an advisory relabel … it needs a legitimate reason **or the original stands**"*.

Run that dies: exactly B/L2's self-deadlock and B/L9's seed/read race — both would be caught by a 20-line two-process fixture, and both are invisible to every criterion as written. `RESULT: the only executable concurrency case in the change is the one the plan declares unexecutable.`

Fix: keep S-CNC's interleaving **gating** for the catalog surface only, with a two-process fixture (contend the lock; kill the holder; verify the break path and the release), and let the advisory label stand only for the prompt-instruction surfaces.

---

**B/L11 · MAJOR · `SKILL.md:3` — the description — will still say the human gate is "the top-level split ONLY" after HG2 lands. It is a baseline site of the changed claim, omitted from both `B4/P12` and D16's site list, and PRV rewrites that exact line.**

Evidence:
- `SKILL.md:3` (verified verbatim): *"… with a human gate on the **top-level split ONLY** and recursive sub-orchestration …"*.
- `0-baseline.md:105` (P12, "Human gates") lists `METHODOLOGY.md:212-216`, `SKILL.md:77-78`, `stage-6:15-19,43-45`, `decomposition-node.md:27-28`. **`SKILL.md:3` is not listed**, nor is `METHODOLOGY.md:327` (the TOP index row, which reads *"Top-level decomposition human gate ONLY"*). So `R2` (`1.5-criteria.md:285-289`) cannot require either.
- `2-plan.md:311-314` (D16 sites): *"`SKILL.md` (rule block, Loop, Stop-for-human)"* — **the frontmatter is not a site**. Meanwhile `2-plan.md:174` (D6/PRV sites) *does* rewrite *"`SKILL.md` (**frontmatter**, purpose paragraph, rule 1)"*.
- `1.5-criteria.md:242-246` (S-HG2) requires *"**every** site that said the human gate is the top-level split ONLY"* to be narrowed — an assertion whose site list omits the one site that will be edited anyway for a different reason.
- SC1/SC2 (`1.5-criteria.md:300-309`) measure length, angle brackets, trigger vocabulary and the proactive clause. **Nothing checks the description's factual content.**

Run that dies: build lands cleanly; every gating criterion passes; the shipped skill's single most-read surface — the frontmatter every invocation loads — tells the model there is one human gate, at the top split only, while `stage-7` and `SKILL.md`'s rule block say there are two. `RESULT: completes, with the skill's trigger surface contradicting its own gate structure.`

---

**B/L12 · MAJOR · Position: the rule block's closing three-item rationale is not addressed, and cycle 1's 3/3-reviewer finding on it is silently dropped.**

Evidence:
- `SKILL.md:39-41` (verified): *"(The completeness lens, the two-pass discipline, and gate-before-present are stated here, up front, because these files are prompts — a position-sensitive assembly — and this rule block is load-bearing *before* the stage table, not after it.)"* — it enumerates exactly **three** items and is the block's **last** element, immediately adjacent to `## Inputs`.
- `2-plan.md:445` (D16's position contingency): *"HG2 is added **after** the three existing rules so nothing that worked because it was early is moved."* Silent on whether "after the three rules" means before or after the rationale, and silent on the rationale's enumeration.
- `hardening-cycle-1/decisions.md:112-113`, carried forward: *"**Position: place PRV/DIV before GBP** inside SKILL.md's rule block and **update the block's closing three-item rationale to enumerate all five (3/3)**; S-SC3 must gain an intra-block ordering assertion."* Cycle 2 keeps the second half and drops the first.
- `1.5-criteria.md:314-316` (SC3): *"the rule block still **precedes** the stage table (line-offset assertion), and its **intra-block order** is asserted explicitly"* — but nowhere does any artifact state **what** the required order is, so the assertion has no referent.
- `0-baseline.md:92-113` has no CHANGE row for `SKILL.md:39-41`.

Run that dies: rule 4 (HG2) is appended after the rationale. The rationale now (i) under-enumerates the block by one rule, and (ii) is no longer the element adjacent to the stage table — HG2 is, taking the recency slot that GBP's structural claim previously occupied. SC3 passes (block still precedes the table; *an* intra-block order is asserted). X2 probes GBP, so it too passes. `RESULT: completes with an undetected position regression on the element the charter's position lens exists to catch.`

---

**B/L13 · MAJOR · S-XPM's absence sweep spans six GBP-only terminus sites; D16's site list covers three of them and `B4/P11` names three — so either the sweep fails the build or it is too loose to fail.**

Evidence — the six sites that literally gate *presenting / exit-plan-mode* on the two passes alone:
- `SKILL.md:33-34` *"cannot be finalized / **presented** / **exit-plan-mode'd** / assembled until **both** passes …"* — in P11 ✓
- `METHODOLOGY.md:149-151` same sentence — in P11 ✓
- `METHODOLOGY.md:316` (GBP index row) *"before a node finalizes / **presents** / **exit-plan-mode** / assembles"* — in P11 ✓
- `METHODOLOGY.md:210-211` (Gates section) — **not in P11**; covered by D16's *"METHODOLOGY.md (Gates section)"*
- `stages/stage-5-gate.md:38-40` *"not finalized / **presentable** / assemblable until both …"* — **not in P11**; covered by D16's stage-5 site
- **`stages/stage-2-draft-node.md:43-44`** *"This draft is **not presentable**, finalizable, or assemblable until the stage-3 and stage-4 passes are both on record and clean-or-resolved."* — **not in P11 and `stage-2` is not in D16's site list at all.** (`stage-3:55` and `stage-4:46` are the same shape.)
- `1.5-criteria.md:259`: *"**No site** asserts the terminus is GBP-gated **only** (paired absence sweep …)"*.

Run that dies: `check.sh xpm` runs the sweep. If implemented as written it flags `stage-2:43`, `stage-3:55`, `stage-4:46` — sites the plan never scheduled for edit — so the gating criterion fails and, per `2-plan.md:433-437`, the only legal move under RAT3 is HALT + relay. If implemented loosely enough to pass, it cannot fail and per `1.5-criteria.md:17-21` (M) the criterion is `verified = no`. `RESULT: blocks (either as a stall or as an un-run oracle) — the plan's own highest-listed risk, half-migration, realised.`

---

**B/L14 · MAJOR · Ingest mode: `plan.md.ingested` is read by the completeness pass but is absent from the operand table, absent from the charter's closed set, and absent from the deterministic-filename list.**

Evidence:
- `2-plan.md:233-236` (D11): the draft is copied to `tree/root/plan.md.ingested` *"(never edited)"*, and `tree/root/plan.md` becomes *"a **mapping table** — one row per spine section … → the **locus in the ingested draft** that covers it, or **`ABSENT`**"*.
- `2-plan.md:42` tabulates only *"the ingest mapping table (`ABSENT` rows) … Reader: 3 (completeness pass)"*. **`plan.md.ingested` has no row.**
- But the completeness critic cannot discharge its own earned-clean duty from the table alone: `stages/charter.md:81-83` requires it to *"**cite where in the node it is covered**"* for each section-class, and `stage-3:23-26` re-states it. Verifying a claimed locus, or judging whether an `ABSENT` row is genuinely absent, requires reading `plan.md.ingested`.
- The closed set (`charter.md:97-99`, `stage-3:17-18`) does **not** include it, and `2-plan.md:102-103` (D2) *tightens* the closed set in the same cycle. Handing it over is a closed-set violation; withholding it makes the pass un-runnable.
- `plan.md.ingested` is not added to the fixed-name list at `METHODOLOGY.md:239` / `stage-8:13-15`, so **stage-done for stage 1 in ingest mode is undefined**.
- Downstream: `1.5-criteria.md:202` (X4) asks only whether an absent §4 *"must be marked `ABSENT` and flagged"* — it never exercises the reviewer's access problem, and SPV at stage 5 (`2-plan.md:181-183`) must spot-verify citations pointing into a file the reviewer never reported a hash for.

Run that dies (run (f)): stage 1 copies the draft; stage 2 writes the mapping table; stage 3 spawns three cold agents with the closed set as written — a table of loci and no draft. Each must either return un-run (no coverage citable) or cite loci it never read (a fabricated citation, which `2-plan.md:183` says makes the record **un-run**). Three un-run records ⇒ the pass is un-run ⇒ `RESULT: DEADLOCKS at stage 3 in the newly-defined mode.`

---

**B/L15 · MAJOR · Deferral seam: HG2's approval artifact is agent-authored, so "never self-approved" is a property its mechanism does not have — and the mechanism that would give it teeth is deferred F5.**

Evidence:
- `2-plan.md:298-299` (D16): *"Under **RAT3** this is a **HALT + verbatim relay**, never self-approved. The approval is recorded at `plan/assembly-approval.md` (a **run-level file, top orchestrator only**, per D8)."* The writer is an agent.
- The loop's own established ruling on exactly this: `LOOP-STATE.md:194-195` — *"the auditor must fetch the transcript, **not any file an agent wrote** (which is exactly why `LOOP-STATE.md`, this file, must **NOT** be the cited locus for a ratification)."*
- The discriminator that would make an agent-recorded approval auditable is recorded and then explicitly deferred: `1-spec.md:57-61` and `1-spec.md:179-186` (*"**F5's mechanism remains deferred**; this is recorded as an input to it, not implemented here"*).
- The asymmetry: for TOP the plan states the limitation at the site (`2-plan.md:81-84`, *"`plan/topgate/`'s bare existence still satisfies TOP's base predicate … that is **F5, deferred**"*, and `1.5-criteria.md:54-55` requires it). **For HG2 no limitation is stated anywhere**, and `1.5-criteria.md:240-241` requires the artifact to assert *"never self-approved"* — a claim the criteria will confirm is *stated* while the mechanism cannot deliver it.
- The empirical precedent that this is not theoretical: `FINDINGS.md` meta-observation 3 — *"**The topgate was defeated live**, exactly as predicted from the text."*

Run that dies: a delegated runner reaches HG2, HALTs, relays; the orchestrator (an agent) writes `plan/assembly-approval.md`; XPM reads it, GBP holds, the run presents. Nothing distinguishes that file from a genuine owner approval. `RESULT: completes — the new gate is satisfiable by the party it constrains, and every criterion passes.`

Fix: either state the same honest limitation at HG2's site that BIND states at TOP's, or require the approval to cite the harness-authored locus the spec already identified (`1-spec.md:43-49`).

---

**B/L16 · MAJOR · S-PRV's absence sweep on the token `PROVEN` can never pass: `provenance` contains it at 12+ sites, and "Charter provenance" is a required section in the worked config. The cycle reproduces the exact missing-word-boundary defect D17 diagnoses.**

Evidence:
- `1.5-criteria.md:135-136`: *"**P — paired absence sweep, normalized:** the token `PROVEN` and the phrase *'proven, not asserted'* are **absent from the artifact**."*
- `1.5-criteria.md:24-26` defines `normalize()` as *"strip `**`/`*`/backticks, collapse whitespace, flatten line wraps"* — **no word-boundary requirement anywhere.**
- Occurrences of `proven` as a substring of `provenance` that must survive: `stages/charter.md:11,16,93`; `stage-3:9,29`; `stage-4:8,27,49`; `examples/authoring-a-skill/planning.md:15,31`; `examples/authoring-a-skill/README.md:11`.
- One of them is load-bearing and cannot be deleted: `examples/authoring-a-skill/planning.md:31-32` makes *"**Charter provenance**: for a forked charter, the fork-provenance blockquote"* a Layer-2 `required_sections` entry, and `1.5-criteria.md:330-331` (SC5) requires the fork-provenance blockquote to remain.
- The irony is the cycle's own lesson: `2-plan.md:320-322` (D17) — *"**word boundaries mandatory** (a bare `grep -o TOP` matches inside `HARDSTOP` and manufactures phantom sites)"*, and `guarded-change.architect.md:66-68` makes word boundaries **mandatory** for the baseline's ID grep. The rule is applied to ID greps and not to the criteria's own absence sweeps.

Run that dies: `check.sh prv` reports `PROVEN` present at 12 sites. The build cannot make the sweep pass without deleting the charter's provenance discipline. A gating criterion that cannot be satisfied ⇒ per `2-plan.md:433-437` and `1.5-criteria.md:28-32`, HALT + verbatim relay. `RESULT: blocks — the build cannot converge.`

Fix: word-boundary + case-sensitive matching in `normalize()`/the sweeps, stated as a rule for **every** absence sweep, not only ID greps.

---

**B/L17 · MINOR · Five criteria are declared "not proxies" although their subjects are behaviours — including SPV, which cycle 1 named as one of the three widest grep-only gaps.**

`2-plan.md:390-392`: *"Rows whose subject **is** the text (S-OFL, S-PRV, S-SPN, **S-SPV**, S-IDGREP, S-SLOT, **S-TPL3**, **S-DEC**, **S-DEP**, S-RST, **S-CNC**) are **not** proxies."* For S-OFL/S-PRV/S-SPN/S-IDGREP/S-SLOT that is fair. For the bolded five it is not: *"stage 5 spot-verifies a sample"* (D7), *"no mid-run commit happens"* (D12), *"DEC escalates"* (D10), *"stage 7 emits a topological order"* (D9), *"index.md has one writer at runtime"* (D8) are behaviours a text check cannot observe. `hardening-cycle-1/decisions.md:114-116` named *"S-C6 (**spot-verify duty**), S-C4 (ingest `ABSENT` marks), S-F4 (absent `redteam_context`)"* as *"the widest gaps and … cheap to add as X- arms"*. Cycle 2 added X4 for the latter two and **left SPV with no arm**, relabelling the gap rather than closing it.

---

**B/L18 · MINOR · D9's leaf-level execution order is not derivable from its stated operand, and cross-subtree cycles are undetectable.**

`2-plan.md:212-215`: *"A decomposing node declares … a **dependency edge for every child pair** that has one. **A cycle among a node's children is a blocker** at that node's gate. Stage 7 emits an `## Execution order` section: a **topological order of the leaves** with the parallelisable groups marked, **derived from the per-node DAGs**."* A parent can only express edges among **its own direct children**, so a dependency between leaf `A/x/1` and leaf `B/y/2` is inexpressible, and a cycle spanning two subtrees is invisible to every node's gate. Collapsing a branch-level edge into "all of A's leaves before all of B's" restores a total order at the cost of the parallel groups — the O(children²) over-serialisation whose cost envelope is explicitly deferred (`1-spec.md:190-192`). `S-DEP` (`1.5-criteria.md:173-179`) is P-only, so nothing observes which of the two happened.

---

**B/L19 · MINOR · D13 moves the apex roll-up into a single-writer node file that a second, deferred-to-be-named actor also writes; and index.md-as-derived puts an O(tree) read in the top orchestrator against ECON.**

- `2-plan.md:196` (D8): *"`<node>/_status.md` … **that node's own owner only**"*. `2-plan.md:262-263` (D13): *"The apex roll-up is **`tree/root/_status.md`**."* But `stages/stage-7-assemble.md:20` already has stage 7 write it: *"**Record completion** in `RUN.md` / the apex `_status.md`."* Whether that violates the single-writer rule depends on **who runs stage 7** — and *"naming stage 7's actor"* is inside deferred F1 (`1-spec.md:174`). A landed partition whose correctness turns on a deferred naming.
- `2-plan.md:195`: index.md *"written **only** by the top orchestrator, **by walking the tree**"* — a new O(total-tree) read in the one context `METHODOLOGY.md:183-184` promises does not scale: *"**no single orchestrator's context scales with total tree size** — only with its own subtree's breadth."* The plan cites the change as *"which also improves ECON"* (`2-plan.md:197`) for the gate log while worsening it here, unremarked.
- `stages/stage-8-restart-resume.md:32` still opens the restart procedure with *"read `RUN.md` + `index.md`"* — reading a now-derived, possibly-absent file first. D8 lists stage-8 as a site, but no criterion asserts the restart procedure stops treating it as authoritative.
- Also unremarked: **stage 7 now reads every node's `<node>/decisions.md`** (gate state, fixed/demoted lists, rebind entries, cross-node SPV per `2-plan.md:35-37,183`) — a whole-tree reader of every node's private log, directly against `METHODOLOGY.md:280` (*"not sibling subtrees' internals"*). Not in the accessor table.

---

**B/L20 · MINOR · The Layer-2 config still instructs every cold agent that F8 is out of scope, and the spec claims no config change is needed.**

`guarded-change.architect.md:22-26` (a `redteam_context` note handed verbatim to every cold reviewer): *"the **OWNER QUESTIONS QUEUED** (F8 — whether a human must review the assembled plan). **A hardening run that implements or pre-shapes F8 is out of scope**; check any human-gate claim against this file."* Cycle 2's centrepiece **is** F8. `1-spec.md:251-252` asserts *"**Not touched:** `Architect/guarded-change.architect.md` (no config change is needed this cycle)"*. Cycle 1's own precedent contradicts that posture (`hardening-cycle-1/decisions.md:21-30`, CFG6: the config was updated as part of the change). Consequence: every future cold reviewer is handed a live instruction to flag HG2 as a scope violation — a manufactured bounce, and one the CAP would count.

---

**B/L21 · MINOR · SPN's absence sweep is under-specified by one: the criteria say "five other" spellings, the baseline says "6 spellings" over seven loci, and the canonical string is a new seventh.**

`1.5-criteria.md:226`: *"the **five other** baseline spellings (B4/P18) are **absent**."* `0-baseline.md:111` (P18) says *"**6 spellings**"* and lists seven loci. The canonical target `Outputs & artifacts (with their locations)` (`2-plan.md:271`) matches **none** of them exactly — `generic-node.md:16` / `decomposition-node.md:10` are `(WITH their locations)` (case) and `stage-2:11-12` is `(with their locations, incl. on-disk/output-folder layout)` (suffix). So **six** baseline spellings must be swept, not five, and at least one has no assertion. Compounding: if the sweep is case-insensitive it will also match the canonical string and can never pass; if case-sensitive, stage-2's variant contains the canonical as a prefix, so the positive and negative assertions at that one site must be reconciled explicitly. `1.5-criteria.md:227-228` correctly identifies that *"a naive matcher would report success"* — and then specifies a matcher whose case-sensitivity is unstated.

---

## Operand table attack

`2-plan.md:29-44`, one row each.

| # | Fact | Claimed class | Operand exists when read? | Producer really earlier? | Verdict |
|---|---|---|---|---|---|
| 1 | `sha256(<node>/plan.md)` current | (i) | **Yes** — `plan.md` exists from stage 2 (`stage-2:46`) | n/a | **Sound as a read.** But the *file's* writer set silently gains **stage 5** (D3(a) fix-in-place); that producer is in neither the table nor D8's partition ⇒ B/L5, B/L8 |
| 2 | `sha256(<parent>/plan.md)` current | (i) | Yes at a child's 5/7 | n/a | **Sound as a read; the rescue operand is missing.** A stale-but-rebound parent hash can only be cleared by the **parent's** rebind entry, which no row grants any reader ⇒ **reads a fact absent from the table** (B/L8) |
| 3 | record's **reported** context sha256 map | (ii) 3/4 → 5,7 | Yes (`charter.md:96` verified) | **Yes** ✓ | **Ordering sound; operand untrustworthy.** Self-reported by the reviewed party while D2 de-self-reports identity for that exact reason ⇒ B/L6 |
| 4 | `spawn_id` (dispatcher-observed) | (ii) 3/4 → 5 | Yes; `unavailable-by-harness` defined | **Yes** ✓ | **SOUND.** Cycle 1's un-gateable rule is genuinely dropped |
| 5 | gate state `clean`/`-fixed-in-place`/`-demoted` | (ii) 5 → 7 | Yes | **Yes** ✓ | **Ordering sound.** But a fourth reachable state — **un-gated (stale)** — has no producer of its exit ⇒ B/L5 |
| 6 | `rebound_from` / `rebound_to` | (ii) 5 → 5, 7 | Yes for n = 1 | Same-stage RAW, acceptable | **FAILS for n ≥ 2** — no transitive clause, so the plan's own "four fixed minors" node is un-gateable ⇒ B/L7 |
| 7 | `fixed_findings` / `demoted_findings` | (ii) 5 → 7 | Yes | **Yes** ✓ | **SOUND** |
| 8 | `elc` | (ii) 2 → **child's** 6 | **NO** — the two-level condition needs `elc(grandparent)`, outside the reader's ECON surface, and is undefined at depth 1 | Producer position fine; **reader lacks an operand** | **FAILS.** Either reads a third-generation fact **absent from the table**, or reads an unnamed "parent's recorded ratio". No depth-1 carve-out ⇒ B/L3 |
| 9 | child dependency DAG | (ii) 2 → 4, 7 | Yes per parent | **Yes** ✓ | **Operand exists; the derived output does not follow.** A leaf-level topological order is not derivable from per-parent DAGs ⇒ B/L18 |
| 10 | `approved_root_plan_sha256` | (ii) approval → 6 | **Only if `APPROVAL.md` exists** — producer is *"not the runner"*, i.e. outside the system, and F5 (which would make it exist) is deferred | n/a | **UNDER-SPECIFIED.** Which clause wins when `APPROVAL.md` is absent — bare existence (TOP defeated, as declared) or the staleness clause (dispatch blocked with no answerable HALT) — is never stated ⇒ run (b) |
| 11 | the assembly approval (HG2) | (ii) | **NO for a single-leaf run** — conditioned on `assembled-plan.md`, which such a run never writes | **NO** — the reader (the stage-5 single-leaf terminus, `2-plan.md:312`) runs **before** the producer's trigger (a stage-7 write) | **FAILS — this is the cap class verbatim** ⇒ **B/L1 (blocker)** |
| 12 | ingest mapping table (`ABSENT` rows) | (ii) 2 → 3 | Yes | **Yes** ✓ | **Incomplete.** Stage 3 must also read `plan.md.ingested` to cite coverage or judge an `ABSENT` row; that file has no row, is outside the closed set, and is not a deterministic filename ⇒ B/L14 |
| 13 | the catalog lock | **(i)** | Acquisition testable | n/a claimed | **MISLABELLED.** `mkdir` is a mutation with a producer position, and the **release is an unassigned write**; run 1 deadlocks against its own stage-1 acquisition ⇒ **B/L2 (blocker)**. `BROKEN-BY` is written with no reader |
| 14 | `catalog-pending/<skeleton>.md` + `PROPOSAL.md` | (ii) 6 → run end | Yes | **Yes** ✓ | **SOUND** in itself — but inert because the run-end commit cannot take the lock (B/L2) |

**Predicates in §2 that read facts absent from the table:** the parent's rebind entry (D1, at a child's stage 5/7); `elc(grandparent)` or an unnamed parent ratio (D10, at the child's stage 6); `plan.md.ingested` (D11, at stage 3); `BROKEN-BY` (D8, by the victim run — written, never read). **Class-(i) claims that are false or misapplied:** row 13 (a mutation, not a computation); row 1 partially (the hash is computable, but the file gains an untabulated writer whose position is load-bearing for every descendant).

**Does cycle 2 escape the class or rename it?** *Partly escape, substantially rename.* BIND's node-hash clause is a genuine, honest class-(i) win, and the root carve-out that killed pass 2 is really fixed (`2-plan.md:69-71`, `1.5-criteria.md:45-48`). But the cap's exact defect — *a predicate whose operand is conditioned on the output of a stage later than the reader* — reappears at **HG2/XPM for a single-leaf run** (row 11), and its sibling defect — *a write duty nobody is assigned* — reappears at **the catalog lock's release** (row 13), protected from scrutiny precisely by the class-(i) label the anti-cap principle exempts. And the missing-carve-out shape that produced pass 2's second blocker reappears in **DEC at depth 1** (row 8). Per the plan's own `2-plan.md:426-430` — *"A bounce on the old class would immediately re-trip the cap"* — rows 11 and 13 are that bounce.

---

## Runs walked to death

### (a) Single-node run — root is a leaf, no children, no parent
Stages 1→2→3→4→5: BIND's root carve-out works (parent clause N/A); IDN, SPV, RES all discharge; gate = `clean`. Stage 6: LEAF, planning done. Terminus: XPM requires **GBP ∧ HG2** (`2-plan.md:308-310`); HG2's operand is produced only *"after `assembled-plan.md` exists"* (`2-plan.md:41`), and `assembled-plan.md` is never written because stage 7 collates a *tree* (`stage-7:3-6`, `stage-6:13-14`). No stage can produce `plan/assembly-approval.md`.
`RESULT: DEADLOCKS` (B/L1). Note this is the mode `LOOP-STATE.md:19-21` runs the self-review in.

### (b) Root + one leaf
Root gated clean → stage 6 → **this is the top-level split** ⇒ TOP. `plan/topgate/` already exists, pre-created empty at `stage-1:12`, so the base predicate is pre-satisfied (declared F5 debt, `2-plan.md:81-84`). BIND adds *"TOP is unsatisfied while `approved_root_plan_sha256` ≠ `sha256(tree/root/plan.md)`"* — but with no `APPROVAL.md` the operand is absent and **the plan never says which clause governs**. Read as vacuous ⇒ dispatch proceeds unapproved (the pre-existing, declared defeat). Read as gating ⇒ HALT+relay for an artifact only deferred F5 could produce.
Child: stage 1→5. Its six records report the **parent's** hash; parent unchanged, so BIND passes. Stage 6: LEAF. Stage 7: both nodes clean → `assembled-plan.md`. HG2 → HALT+relay.
`RESULT: blocks correctly — with the F5-declared TOP bypass, and an unstated ambiguity about which TOP clause governs when `APPROVAL.md` is absent.`

### (c) A node re-drafted after its reviews, then fixed in place
Major at stage 4 → RES(b) → stage 2 re-draft (H0→H1) → old records stale ⇒ fresh passes forced (this arm works as designed). New records report H1. Stage 5 finds four minors → RES(a) ×4 → H1→H2→H3→H4→H5 with per-finding entries. Stage 7's BIND: records report H1; current H5; no chain rule ⇒ stale ⇒ un-gated ⇒ **not assemblable**, contradicting `2-plan.md:120`. And "un-gated" has no route (`stage-5:22-34` has no such row).
`RESULT: unrepresentable state` (B/L7 + B/L5). Additionally, if the parent is the node fixed in place, every descendant's records go stale with no rescue operand (B/L8).

### (d) The assembled artifact reaches HG2 and the human never answers
`assembled-plan.md` exists and is complete; the runner HALTs and relays; nothing presents. This is the one place the plan's reasoning holds exactly as written (`2-plan.md:55-56`).
`RESULT: blocks correctly.`

### (e) HARDSTOP in the middle of each new mechanism
- **Mid-BIND rebind** (after the `plan.md` write, before the entry): records stale, no rescue, no route ⇒ `unrepresentable state` (B/L5).
- **Mid-HG2** (assembled, awaiting the human): the resuming orchestrator reads `stage-7:39-41` (*"its existence is the 'run complete' marker … a restart after it exists is a **no-op**"*) plus `stage-8:15` and **presents without the approval** ⇒ `RESULT: HG2 bypassed` (B/L4) — the worst outcome in this set, because it reports success.
- **Mid-catalog-lock** (holder died mid-commit): the next run finds the lock, checks the pid, breaks it, writes `BROKEN-BY`; **no stage reads `BROKEN-BY`**, and the restarted original run (authorised by `LOOP-STATE.md:23-30`) re-attempts `mkdir` with no wait/retry policy ⇒ `RESULT: undefined` (B/L2, B/L9).
- **Mid-ingest** (`.ingested` copied, mapping table not yet written): `plan.md.ingested` is not a deterministic filename, so stage-done for ingest is undefined ⇒ either re-copied (harmless) or treated as done with no mapping table (stage 3 gets nothing).

### (f) The newly-defined ingest mode
Stage 1 copies to `tree/root/plan.md.ingested`; stage 2 writes the mapping table as `plan.md`. Stage 3's three cold agents get the closed set of `charter.md:97-99` — **which excludes the ingested draft**. Each must return un-run (cannot cite coverage per `charter.md:81-83`) or cite loci it never read (fabricated ⇒ un-run per `2-plan.md:183`).
`RESULT: DEADLOCKS at stage 3` (B/L14).

### (g) Two Architect runs on one machine; and a dead lock holder
- **First run, alone:** stage 1 takes the lock to seed; nothing releases it; run end cannot re-acquire; pid is its own and alive so the break path is closed ⇒ `RESULT: DEADLOCKS` (B/L2) — no second run required.
- **Two first runs:** `mkdir <catalog>/.lock` fails ENOENT for both (the lock lives inside the dir being created); the workable split leaves run A seeing `<catalog>` exist, skipping the seed, and matching TPL1 against a half-copied catalog — **reads are outside the guard's scope** ⇒ `RESULT: completes with corrupt input` (B/L9).
- **Dead holder:** breakable, but `BROKEN-BY` has no reader and no wait/retry policy exists; concurrent `git commit`s additionally contend on git's own `.git/index.lock`, an accessor the table never names ⇒ `RESULT: undefined.`

---

## Position lens

The trigger is *any* edit, and the elements to test include ones that did not change.

1. **`SKILL.md` rule block — a fourth rule added, rule 1 rewritten.** `2-plan.md:445` places HG2 *"after the three existing rules"*. The block's real last element is the parenthetical rationale at `SKILL.md:39-41`, which enumerates exactly **three** items and asserts *"this rule block is load-bearing before the stage table"*. Adding rule 4 after it moves HG2 into the recency slot GBP's structural claim held and leaves the rationale describing 3 of 4 rules; adding it before leaves the rationale correct in position but still wrong in enumeration. `SC3` asserts *"intra-block order"* without stating what the order must be, and cycle 1's 3/3-reviewer requirement to update the rationale is dropped. **Behaviour change, unasserted** ⇒ B/L12.
2. **`SKILL.md:3`, the frontmatter — highest-primacy element in the package.** PRV rewrites it (`2-plan.md:174`) while D16 does not list it (`2-plan.md:311`), so *"a human gate on the top-level split **ONLY**"* survives beside a two-gate loop. SC1/SC2 measure length, angle brackets and vocabulary; nothing checks content. This is not "the information is still present" — it is *contradictory* information in the one position every invocation reads first ⇒ B/L11.
3. **`stage-7`'s "Rules governing this stage" — adjacency inversion.** `stage-7:33-35` currently closes with *"**A fully-covered clean tree assembles.** … the gate blocks holes, not progress."* HG2 is inserted into the same rule list as the new operative gate on a clean tree. Whichever order is chosen, one of the two adjacent statements over-claims. Not a `B4` row; `SC5` covers only rules stated in *more than one place*, so an intra-file adjacency contradiction is unobserved.
4. **`METHODOLOGY.md`'s config-contract YAML — a new key whose position is the whole point.** D4 de-conflates `redteam_context` from `off_limits_paths` (`2-plan.md:126-137`) but never pins where the key sits. `1.5-criteria.md:96-102` requires only *"a top-level key"*. Placing it adjacent to `off_limits_paths` structurally re-invites the very conflation the fix exists to remove — the config-authoring agent reads adjacency as relatedness.
5. **`METHODOLOGY.md:95-107`, the Rules list — a removal plus two additions.** OFL replaces a one-clause bullet with a four-clause honest statement and CTX adds another; the *"**Do not invent plan specifics**"* bullet — the one that governs the immediately-following contract section — is displaced further from the list head. Unremarked and unasserted.
6. **Non-regression the plan does assert, and does test:** X2 requires GBP to still fire in both arms (`2-plan.md:375`, `1.5-criteria.md:317-319`). That is the right shape and satisfies ST1.5d/H3 **for GBP**. It is **not** done for **CMP**, whose motivating sentence (`SKILL.md:17`, rule 1) PRV rewrites — see CH8.

---

## Concurrency lens

My own enumeration (readers **and** writers, baseline **and** new), against `2-plan.md:193-199` and §4.

**S1 — `index.md`.** Writers: `stage-1:12` (create; top orch, **serial**), `stage-1:20` (per node, **parallel**), `stage-1:44` (per-node cross-cutting assertion), `stage-6:11-12` (per node, **parallel**), `METHODOLOGY.md:195`, `templates/seed/README.md:14`. **6 sites; the plan says "four writers, all parallel" — undercounts by 2 and mislabels the serial one.** Readers the plan enumerates: **none**. Actual: `stage-8:32` (restart, reads it *first*), `stage-6:63`, `stage-8:9`, `METHODOLOGY.md:235,256`. New writer: the top orchestrator, by an O(tree) walk (ECON cost, B/L19).

**S2 — `<node>/_status.md`.** Plan: *"undefined at baseline"* — **false.** Baseline writers: `stage-6:11-12` (the node's owner), **`stage-7:20`** (*"Record completion in `RUN.md` / the apex `_status.md`"*). Readers: the parent's roll-up (`METHODOLOGY.md:181`, `stage-6:25`), the restart walk (`stage-8:16`). After D13 moves the apex into `tree/root/`, stage-7's write becomes a second writer of a file the new rule reserves to one owner — reconciled only by naming stage 7's actor, which is **deferred F1** (B/L19).

**S3 — the gate log.** Writers: `stage-5:19`, `stage-5:54` (every owner), **`stage-6:29` / `METHODOLOGY.md:222`** (a DEC escalation), **`charter.md:139` / `stage-5:33`** (a contest entry), `SKILL.md:61-62`. **The plan's table lists two of five; `0-baseline.md:102` (P9) lists the same two**, so R2 cannot require the other three to migrate. Readers: CAP (`stage-5:54`), carry-forward into both passes (`charter.md:98`, `stage-3:18`, `stage-4:15`), and — **new** — stage 7 reading **every** node's private log (`2-plan.md:35-37,183`), a whole-tree reader against `METHODOLOGY.md:280`.

**S4 — the catalog `~/.claude/architect/templates/` (git).** Writers: `stage-6:34` (TPL3, any sub-orchestrator, mid-run), `stage-6:35` (TPL2 distil), `METHODOLOGY.md:196-201`, `templates/seed/README.md:17-23`, `stage-1:13-14` + `templates/seed/README.md:26-29` (first-run seed + `git init`). **Readers — zero enumerated by the plan; actual: `stage-1:19-20` (a TPL1 match at *every node*, parallel across siblings), `templates/seed/README.md:13-16`, `METHODOLOGY.md:194`.** Also unnamed: git's own `.git/index.lock`. Guard scope claimed to cover three paths (`2-plan.md:406-408`) — all three are **writes**. **Left out: every catalog read; the release; wait/retry on a held lock; the `BROKEN-BY` reader; the lock's own parent-creation race.**

**S5 — `plan/topgate/`.** Writers: `stage-1:12` (pre-creates empty) + the approver (`APPROVAL.md`, new). Readers: `stage-6:17,44`, `SKILL.md:77`, `METHODOLOGY.md:214`, `decomposition-node.md:27`, and now BIND. Two writers with opposite authority — the declared F5 debt. **Not in the partition table at all.**

**S6 — `plan/assembly-approval.md` (new).** Writer: the top orchestrator — **an agent** (`2-plan.md:299`). Reader: the XPM terminus. Self-approvable ⇒ B/L15.

**S7 — `assembled-plan.md`.** Writer: stage 7. Readers: the human (HG2), the restart walk, consumers. Its existence now carries **two** incompatible meanings — stage-7-done and run-complete ⇒ B/L4.

**S8 — `<node>/plan.md`.** Baseline writer: stage 2 (`stage-2:46`). **New writer: stage 5** (D3(a)). Readers: stages 3/4 (via cold agents), 5, 7, BIND, and every child (parent plan in the closed set). **Absent from the partition table**, and the stage-5 write is what invalidates whole subtrees with no notifier ⇒ B/L8.

**S9 — `<node>/completeness/*.md`, `<node>/adversarial/*.md`.** Writer: the dispatching owner (stages 3/4). Readers: stage 5, and **new** — stage 7 cross-node. Declared **immutable** (`2-plan.md:73`) while the restart amendment (`2-plan.md:85-86`) forces re-dispatch to overwrite complete records ⇒ B/L5.

**Guard-scope verdict.** For S1/S2/S3 the plan's claim — *"the 'guard' is **not a lock at all** … the accessor set is **reduced to one writer**, which is why there is no scope gap to enumerate"* (`2-plan.md:404-406`) — fails on its own terms, because the accessor set it reduces is **not the accessor set that exists**: it misses two `index.md` write sites, three gate-log write sites, and `<node>/plan.md` entirely. For S4 the one genuine lock leaves **all readers** and its own **release** outside its scope. And §4's justification for having no executed interleaving is false for S4 (B/L10). Per `Guarded_change/stages/stage-8.md:33-40` (H4), the remaining inspection-only checks make the concurrency criterion `verified = no`.

---

## Coverage challenge (CH8)

**Which of the runs I walked to death would every criterion in `1.5-criteria.md` still pass? Answer: all of them except one.**

| Behaviour the change can alter | Observed by any criterion? | Scenario | Severity |
|---|---|---|---|
| A **single-leaf run terminates and presents** | **No.** X1's intact arm covers *gates* (`1.5-criteria.md:58-60`: *"a root node with no parent at all"*); X2's both arms presuppose `assembled-plan.md` exists (`:252-253`); S-XPM is a text check that the single-leaf terminus is *named*. | Run (a): every criterion PASSES while the run can never present. **This is cycle 1's carried-forward coverage challenge — *"no criterion observes that a clean tree terminates"* (`hardening-cycle-1/decisions.md:193-194`) — not closed, reproduced one gate later.** | **blocker** |
| The **catalog lock** acquires, releases, contends, and recovers | **No.** S-TPL3 (`:204-210`) is a text check; S-CNC's interleaving is relabelled advisory (`:166-171`). | Run (g): first-run self-deadlock; all criteria PASS. | **blocker** |
| A **node with several in-place fixes assembles** | **No.** X3 asks only *"is this node's gate state distinguishable from clean at assembly, and what is it?"* (`:91-93`) — distinguishability, not assemblability, and with **one** demoted major. | Run (c): un-gateable node; all criteria PASS. | major |
| **HG2 survives a restart** | **No executed case.** S-HG2's P requires stage-8 to *state* it (`:240-241`); X2 runs no restart; the three sites that say existence ⇒ run-complete are unswept and are not `B4` rows. | Run (e): HG2 bypassed on resume; all criteria PASS. | major |
| **HG2 bounces terminate** | **Nothing.** No bounce record, no CAP counter, no criterion. | Unbounded loop at 6N agents per iteration; all criteria PASS. | major |
| **DEC ever trips** | **No.** S-DEC (`:181-190`) asserts the two-level condition is *stated* at four sites. | Non-reducing 4-level tree recurses without escalation; all criteria PASS. | major |
| **The description's gate claim is true** | **No.** SC1/SC2 measure length and vocabulary only. | Ships *"top-level split ONLY"* beside two gates; all criteria PASS. | major |
| **BIND resists a dishonest/copied reported hash** | **No.** X1's fixtures pre-supply an honest mismatch (`:57-58`). | Binding defeated by the constrained party; all criteria PASS. | major |
| A **parent re-draft's effect on descendants** | **No.** X1's fixtures are one node plus a root; no multi-level BIND fixture exists. | Whole-subtree invalidation, unrescuable; all criteria PASS. | major |
| **CMP / tier (iii) still fires after PRV softens rule 1** | **No.** SC3's executed probe covers **GBP only** (`:317-319`). PRV rewrites `SKILL.md:17` — CMP's own operative sentence — and *"the gate raises the cost … it does not certify its absence"* is placed at short-form sites (`2-plan.md:170`). | An agent reading the softened rule 1 treats the generative sweep as advisory; the founding-failure guard degrades; all criteria PASS. **A position-lens criterion exists for the pre-existing rule and not for the rewritten one.** | major |
| **SPV actually happens at stage 5** | **No arm** — and it was one of cycle 1's three named widest grep-only gaps (`hardening-cycle-1:114-116`). | Stage 5 records a sample it never checked; S-SPV PASSES. | minor |
| **Stage 7's emitted execution order is a real topological order** | **No.** S-DEP is P-only and declared "not a proxy". | Wrong or vacuous order; PASSES. | minor |
| The **`PROVEN` absence sweep** | **Yes — this is the one criterion that fires**, and it fires permanently (B/L16). | Build cannot converge ⇒ HALT+relay. | major |

**None found** does not apply here: eleven behaviours this change can alter are observed by no criterion, and the two blocker-severity ones are the *same* coverage gap cycle 1's reviewers named.

---

## Ranked list

| Rank | ID | Severity | One line |
|---|---|---|---|
| 1 | **B/L1** | **blocker** | HG2's operand is unproducible in a single-leaf run; the reader (stage-5 terminus) precedes the producer's stage-7 trigger — cycle 1's cap class verbatim |
| 2 | **B/L2** | **blocker** | The catalog lock has no release; run 1 deadlocks against its own stage-1 acquisition; `class (i)` is a mislabel that suppressed the producer question |
| 3 | B/L3 | major | DEC's two-level condition needs `elc(grandparent)`, unavailable at the stated reader, undefined at depth 1, untabulated |
| 4 | B/L4 | major | HG2 is bypassed by a restart via three sites that make `assembled-plan.md`'s existence mean "run complete"; no `B4` row, so `R2` can't catch it |
| 5 | B/L5 | major | "stale ⇒ un-gated" is a state with no exit route; immutability contradicts the restart amendment |
| 6 | B/L6 | major | BIND's binding operand remains self-reported by the reviewed party while IDN de-self-reports identity |
| 7 | B/L7 | major | ≥2 in-place fixes make a node permanently un-gateable; the criteria's own "four fixed minors" node is that state |
| 8 | B/L8 | major | The parent-hash clause invalidates whole subtrees; the rescue operand is untabulated; HG2 bounces make it reachable, unbounded and uncapped |
| 9 | B/L9 | major | The accessor enumeration is writer-only and undercounts (index.md 6 not 4 and not "all parallel"; gate log 2 of 5; `plan.md` absent; catalog readers uncovered) |
| 10 | B/L10 | major | S-CNC's advisory relabel rests on a false premise — the catalog lock is executable, and this repo already executed a real git catalog |
| 11 | B/L11 | major | `SKILL.md:3` will still say "top-level split ONLY"; omitted from `B4/P12` and from D16's site list while PRV rewrites that line |
| 12 | B/L12 | major | The rule block's closing three-item rationale is unaddressed; cycle 1's 3/3 finding on it is dropped; SC3 asserts an order it never states |
| 13 | B/L13 | major | S-XPM's sweep spans 6 GBP-only terminus sites; D16 covers 3 and `P11` names 3 — the sweep either fails the build or cannot fail |
| 14 | B/L14 | major | Ingest mode: `plan.md.ingested` is read by stage 3 but is in no operand row, no closed set, and no filename list |
| 15 | B/L15 | major | HG2's approval is agent-authored, so "never self-approved" is unsupported; the enabling discriminator is deferred F5, and unlike TOP no limitation is stated |
| 16 | B/L16 | major | S-PRV's `PROVEN` sweep can never pass (`provenance` × 12+); the cycle reproduces the missing-word-boundary defect it diagnoses in D17 |
| 17 | B/L17 | minor | Five behavioural criteria are declared "not proxies"; SPV — a named widest gap — still has no arm |
| 18 | B/L18 | minor | D9's leaf-level topological order is not derivable from per-parent DAGs; cross-subtree cycles are undetectable |
| 19 | B/L19 | minor | `tree/root/_status.md` gains a writer whose naming is deferred; derived `index.md` puts an O(tree) read in the top orchestrator against ECON |
| 20 | B/L20 | minor | The Layer-2 config still tells every cold agent F8 is out of scope; the spec claims no config change is needed |
| 21 | B/L21 | minor | SPN's sweep is under-specified by one spelling (5 vs 6 vs a new 7th) and its case-sensitivity is unstated |

**WORST SEVERITY: blocker**

*Unverifiable / flagged as such:* (1) I could not check `oracles/check.sh` or `baseline-replay.sh` — both are *"built at stage 5"* (`2-plan.md:341`), so every claim about what they will assert is a claim about future code; the two stage-0 instruments (`ruleid-sitemap.sh`, `idcollide.sh`) and the `fixtures/X{1..4}/` trees are likewise not present in the change folder (`fixtures/` and `oracles/` exist but I did not treat their contents as reviewable artifacts under my frame). (2) The RAT1 ratification records rest on a session-transcript JSONL (`1-spec.md:43-49`) I did not read — reviewer C's frame. (3) Whether `mkdir` semantics on this filesystem behave as the lock assumes is asserted from POSIX behaviour, not executed.

*Carried-forward findings, confirmation status:* **Producers-not-predicates** — partly (rows 8, 11, 13 fail). **BIND root carve-out** — **closed** (`2-plan.md:69-71`; and it holds for a decomposed tree's root, since the carve-out is on "no parent exists", not on leaf-ness). **`clean-fixed-in-place` assembles** — closed for n = 1, **open for n ≥ 2** (B/L7). **`spawn_id`** — **closed** (D2's asymmetry cannot deadlock and cannot be gamed by self-report). **Re-dispatch race** — not reachable in scope (the join is deferred), but `<node>/plan.md`'s second writer is a new unenumerated one. **Shared write surfaces / four `index.md` writers / stage-8's false claim** — the false claim is correctly retired (`2-plan.md:201-203`), the accessor set is still incomplete (B/L9). **"Does a clean tree terminate?"** — **still not observed**, in a new place (CH8 row 1).

---

## Provenance

**Reviewer:** `general-purpose` subagent · model `claude-opus-5` · `spawn_id: unavailable`
**Exact context path list read** (all under `WT` = `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c` unless absolute), with `sha256sum`:

```
f1c18d67cc9a9cfd3020ed9a5f1a553ee58ab86ff60848d0a457660be5f7b10b  Architect/changes/hardening-cycle-2/2-plan.md
4edfb0b0c147b9bc31f752438f1e3a1f10cd0e50f978f2911de5ae03ca955c21  Architect/changes/hardening-cycle-2/1.5-criteria.md
c554da51ba5a98485c4e58c8fefd5e6f5ef076961d4199619b681d91364c4a4d  Architect/changes/hardening-cycle-2/1-spec.md
251b008fd1e086fdad8c8374555b3e1b483860f325e71e6d85af5942b6673d10  Architect/changes/hardening-cycle-2/0-baseline.md
7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450  Architect/SKILL.md
f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa  Architect/METHODOLOGY.md
79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a  Architect/README.md
c163ff87588dc97dbffae05cfe675985533ae8248b5d583d3322a090c4aceb8c  Architect/guarded-change.architect.md
6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819  Architect/stages/charter.md
ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5  Architect/stages/stage-1-frame-template-match.md
2e76963ce446190ff4bb4d8100a097d8a62e684d5936d38a74e227aea3ad1036  Architect/stages/stage-2-draft-node.md
6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e  Architect/stages/stage-3-completeness-critic.md
96570a6d9298c67ab6b5fe8653b16cf7068fdbe547373a32bee3e02c0721f07c  Architect/stages/stage-4-adversarial-redteam.md
99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5  Architect/stages/stage-5-gate.md
b202101b7b4b16314d4742851138b53efe40b33f3025886149f02ba4aeac1993  Architect/stages/stage-6-granularity-decompose.md
864b74dcfcf43e18b576145327beeb011b1e44bb672f7a10e8d8b0f9ad9cb607  Architect/stages/stage-7-assemble.md
97431f52e7487ab34c9e9278496b687ca2b4ca2bf178203de3d76151c35762c1  Architect/stages/stage-8-restart-resume.md
7148ec60e18b8cf4606b50b0fc8b49f299731b3d3c26a4787bc0a8bf0be52e89  Architect/templates/seed/generic-node.md
b4509defabe16768edcd024a98f44f37c90351aef5fa759b56b0c0930a98cf64  Architect/templates/seed/decomposition-node.md
c7341c863a494a41e616e00b70c14bf8034cfe292108e2dca92436847c3f093e  Architect/templates/seed/leaf-task-spec.md
d2a86068b92d7ee6b47b7af6dd506f456b589a50a6cac7e0e8d15d23246b3fb4  Architect/templates/seed/README.md
b52a22d2012e7a640e68300a2a8f0a985e811e024c0259b26d7d0aabc6ec37ea  Architect/examples/authoring-a-skill/planning.md
aa52ab3b03b9e78ea7ca977d7dacfac515d8e21dbdd5c2faf97004abb563b600  Architect/examples/authoring-a-skill/README.md
794a40e7d54e913efe2c0d05e6f5360f731737ae241ef8d929480b4426bcbb11  Architect/changes/hardening-cycle-1/decisions.md
0afe0acd19ed145b8061d61d2357528ed601ae6ac7e554a5250331ee5982cabf  Architect/changes/hardening-cycle-1/2-plan.md   (§0–§2 only, through D4)
c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b  Guarded_change/stages/stage-1.5.md   (ST1.5d/e/f excerpts)
49d69b00ea9b48253a94638dc80dd7cfb59267703008dac0f13d454f01b6aaf0  Guarded_change/stages/stage-2.md     (ST2b/CP7 excerpts)
8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3  Guarded_change/stages/stage-8.md     (H3/H4/H5/H6/CH6/FRZ excerpts)
94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8  /home/zero/architect-dogfood-2026-07-24/FINDINGS.md          (triaged list + meta-observations)
2555a812c1ca6ed355a128edeb7611df5248a80ae7c05948221498500c56d230  /home/zero/architect-hardening-loop/LOOP-STATE.md
aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249  /home/zero/.claude/plans/1-this-is-a-proud-scott.md          (:165-180, the on-disk layout)
```
Also read via `grep` over the same tree: `Architect/changes/initial-authoring-2026-07/8-harness.md` (line 55 only, cited in B/L10 — quoted as a prior harness record, inside the closed set as a change-record of the artifact under review).
**Not read** (flagged above as unverifiable): the six `hardening-cycle-1/3-redteam-plan.pass{1,2}-{A,B,C}.verbatim.md` records — I worked from `hardening-cycle-1/decisions.md`'s tabulation of them rather than the verbatim records, so my confirmations of carried-forward findings are against the decisions log, not the reviewers' own words; `hardening-cycle-2/oracles/` and `fixtures/`; the session-transcript JSONL.
**Citation spot-verification performed** (24 of my own cited `file:line`s re-read directly): `charter.md:96`, `charter.md:88-92`, `charter.md:97-99`, `charter.md:112`, `charter.md:139`, `METHODOLOGY.md:99-101`, `:149`, `:195`, `:210-216`, `:222`, `:239-241`, `:256`, `:280`, `:309-312`, `:316`, `:327`, `SKILL.md:3`, `:17`, `:33-41`, `:61-62`, `stage-1:12,20,44`, `stage-2:11-12,43-46`, `stage-3:17-18,42-45`, `stage-5:17-21,22-34,38-40,49-50,54`, `stage-6:9-14,15-19,27-31,32-35,43-45,63`, `stage-7:11,20,24-26,33-35,39-41`, `stage-8:9-17,32`, `templates/seed/README.md:14,17-23,26-29`, `decomposition-node.md:10,24-25,27`, `generic-node.md:16,32-33`, `leaf-task-spec.md:13`, `planning.md:25,31,38-40`, `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:173`. **All 24 exist and say what I claim.** One measurement I performed myself: `grep -c redteam_context METHODOLOGY.md` = **0**, confirming `0-baseline.md:97` (P4).
