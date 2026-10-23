# Stage 1 — Spec (hardening cycle 2: the NARROWED cycle)

## 1. The problem

`Architect` (committed at `3771038`; artifact content unchanged at `b08f5a9`) was dogfooded on its own
creation plan on 2026-07-24. The consolidated finding set is
`/home/zero/architect-dogfood-2026-07-24/FINDINGS.md`: 6 structural blockers, an honesty gap (F7–F10),
and ~14 real operational majors.

**Cycle 1 tried to fix all of it and never reached build.** Two full passes (spec → criteria → plan →
3 cold reviewers → gate 4) both returned blocker on **the same finding class** — *a predicate whose
operand has no valid producer* — so the **iteration cap (SEV4) tripped** and the loop stopped for the
owner's tie-break. **No artifact file was edited.** Records: `changes/hardening-cycle-1/`.

**Cycle 2's problem is therefore narrower and different in kind:** land the subset of fixes two
independent cold reviewers **confirmed closed** in cycle 1, plus the newly-ratified F8, plus the
purely-subtractive honesty corrections — and do it **without re-introducing the cap's failure class**.

### 1.1 The root cause, and the design principle that answers it

Cycle 1's diagnosis (LOOP-STATE, pass-2 record): the plan named *predicates* and left their *producers*
unassigned, then — when it did assign them — assigned a write to a stage that runs **before** the stage
producing the operand it depends on. It is a **stage-ordering** problem.

**Cycle 2's governing principle: AN OPERAND IS COMPUTED, NOT STORED.** Every predicate this cycle adds
reads a fact that is either

- **(i) computable on demand** from a file already on disk at the moment of the check
  (`sha256sum <node>/plan.md`) — so there is nothing to write and **nothing to order**; or
- **(ii) written by a named stage that provably runs BEFORE the predicate is read**, stated as
  *writer-stage → reader-stage* with the ordering shown.

**Every fact this cycle introduces is class (i) or class (ii), and §1 of `2-plan.md` is the table that
proves it.** Cycle 1's cap class cannot recur through a class-(i) operand, because such an operand has
no producer to mis-order. **This cycle introduces no join, no terminal subtree status, and no new
up-flow predicate** — those are exactly the deferred work (§4).

---

## 2. OWNER RATIFICATION RECORDS (RAT1) — all three verified against a harness-authored source

**Durable source for all three, spot-verified by this runner before any of it was relied on:** the
**session transcript JSONL**, `~/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
— **harness-authored** (mode `0600`, written by the CLI, not by any agent).

- **Options presented, verbatim:** JSONL record **694**, an `AskUserQuestion` `tool_use` with
  `id: toolu_01Ga2368vabihTBcFVBZEYte`, `timestamp 2026-07-25T14:03:05.318Z`.
- **Owner's response, verbatim:** JSONL record **699**, the `tool_result` **keyed to that same
  `tool_use_id`**, `timestamp 2026-07-25T14:10:24.209Z`:
  > *"Your questions have been answered: "SEV4 tie-break — the iteration cap tripped at gate 4 (2
  > bounces, same class). The loop stops until you break the tie. Which way?"="Accept risk — ship
  > narrower (Recommended)", "F8 (queued since last night, never touched): should a human review the
  > *assembled* plan, not just the top-level split? …"="Yes — human reviews the assembled plan", "My
  > narrowing of your "until nothing surfaces" … Confirm or correct?"="Literal — loop until truly
  > nothing surfaces"."*

**Incidental result worth recording (it is the discriminator F5 needs):** a genuine owner turn is
distinguishable from a harness-injected task-notification — which also appears as `type:"user"` — because
the owner's answer arrives as a **`tool_result` carrying the `tool_use_id` of a specific
`AskUserQuestion`** the assistant issued. A task-notification carries no such key. **F5's mechanism
remains deferred (§4); this is recorded as an input to it, not implemented here.**

### R1 — SEV4 tie-break → **"Accept risk — ship narrower (Recommended)"**
- **Flagged axis:** accept the risk / change the goal / kill the change.
- **Mapping:** selects option 1 unambiguously. The cap is released for a **narrowed** cycle. The
  deferred blockers are **not demoted** — they remain open, moved out of scope (§4).
- **The option's own presented description, verbatim** (this is what bounds the scope, so it is quoted
  rather than paraphrased): *"Cycle 2 ships only the confirmed-closed fixes (BIND over gate artifacts,
  ID renames, RES, redteam_context, §4 heading, seed slots, elc, DEP, CNC, root pin); F1/F2/F5's
  mechanisms defer to a later cycle."*

### R2 — F8 → **"Yes — human reviews the assembled plan"** (a scope ADDITION, newly ratified)
- **Flagged axis:** should a human review the *assembled* plan, not just the top-level split?
- **Mapping:** selects option 1. F8 is **in scope and ratified**; it is no longer a queued question.
- **RAT2 check — the elaboration is ratified, not inflated.** The option's presented description reads,
  verbatim: *"Adds a second human gate at the end. Directly addresses the finding that the founding
  failure WAS caught by a human, yet no human sees anything below the top split. Costs a gate and
  requires the assembly fix to preserve a whole-plan reader."* So all three consequences this cycle
  carries are **inside the ratified text**: (a) a second human gate, at the end; (b) the sites asserting
  the terminus is gate-before-present-gated **only** become false and must be corrected; (c) the
  **forward constraint** that the deferred assembly work must **preserve a whole-assembled-plan
  reader**. Nothing beyond this is claimed as owner-ratified. **Explicitly flagged as NOT ratified and
  authored by this cycle:** what a human *bounce* does mechanically. It is stated in the artifact as this
  cycle's own choice, marked as such.

### R3 — loop-exit semantics → **"Literal — loop until truly nothing surfaces"**
- **Mapping:** selects option 3, the strictest reading — keep cycling while **any** new finding appears,
  including nitpicks, up to the 3-cycle bound. Any earlier narrowing to "no new blocker or major" is
  **superseded and void**.
- **Consequence for this run:** this runner may not treat "only minors surfaced" as a reason to stop
  anything. It is a fact for the orchestrator's loop accounting, not a licence available here.

### 2.1 Scope-authority honesty (RAT2 discipline applied to THIS spec)

`LOOP-STATE.md` calls the broad reading of the owner's directive an *"Interpretation … stated so Roy can
correct it."* **That hedge is authoritative and is carried here.** Cycle 1's spec dropped it and called
the broad reading *"the approved cycle-1 scope"* — an unratified inflation. The superseded phrasing
survives in cycle 1's own records at `changes/hardening-cycle-1/3-charter-given.md:206` and
`changes/hardening-cycle-1/decisions.md:41`; those are records of what was given and decided at the time
and are **not rewritten**. The correction is recorded here and in this cycle's `decisions.md`.

**Three levels of authority are distinguished in this spec, and no item is allowed to drift upward:**

| Level | What it covers here |
|---|---|
| **Owner-ratified** (R1/R2/R3, source above) | ship narrower; the parenthetical fix list in R1's option text; F8/HG2 incl. its three consequences; the literal loop-exit rule |
| **Orchestrator call, within the ratified frame** | the additional in-scope items **not** named in R1's parenthetical list: **IDN**, **SPV**, **IGM**, **TPL3**, **XPM**, and the **subtractive honesty** set (**PRV**-softening, **OFL**) |
| **This runner's own authoring choices** | wording, site placement, the criteria + oracles, and the bounce mechanics of HG2 |

**The orchestrator-call row is declared, not smuggled.** Two of its members deserve the reason stated:
**IDN** *is* in cycle 1's confirmed-closed set (LOOP-STATE: *"`spawn_id` dispatcher-recorded"*), so it
sits inside R1's *"only the confirmed-closed fixes"* even though the parenthetical list omits it.
**PRV** and **OFL** are explicitly recorded in LOOP-STATE as **NOT closed**, so they are *outside* R1's
phrase; they are in scope by orchestrator direction, and the justification is that they are **strictly
subtractive** — they delete a claim the artifact cannot support and add **no mechanism**, so they cannot
exceed the ratified blast radius. Leaving them would be worse than either option the owner was offered:
the artifact would assert a guarantee whose enabling mechanism is *knowingly* deferred. **Flagged for the
owner's correction; it does not bind before then.**

---

## 3. IN SCOPE — exactly this

Grouped as it will be built. Each item names the finding it closes.

### 3A — The confirmed-closed set (ported from cycle 1, then built)

| ID | Fix | Closes |
|---|---|---|
| **BIND** | Bind each review record to the sha256 of the `plan.md` it reviewed; checked at stage 5 and stage 7 **and over the top-level approval artifact**, so a re-drafted split cannot keep its approval. Records **immutable**; a legitimate re-bind is a new `rebound_from`/`rebound_to` entry. **Root carve-out stated:** at the root there is no parent, so the parent clause is **N/A** — a single-node run can gate. Resolves the RES(a)↔BIND contradiction so a `clean-fixed-in-place` node **can** assemble. | F3 |
| **IDN** | `spawn_id` is **dispatcher-recorded**, not self-reported; the unconditional "3 identical ⇒ un-run" rule is dropped (it made gating impossible when the field is unavailable); a **declared-degraded** value exists; sibling-read ban. | F9 |
| **RES** | "clean-or-resolved" de-circularised into three arms; gate state gains **`clean-demoted`** so a fixed-in-place or demoted node is distinguishable from a clean one at assembly. | F10 |
| **CTX** | `redteam_context` becomes a first-class key in the METHODOLOGY config contract **and** in `examples/authoring-a-skill/planning.md`, **de-conflated** from `off_limits_paths`; absent/empty ⇒ a config error that stops the run (not a vacuous path-validation pass). | F4 |
| **CNC** | Serial-vs-parallel declared; every shared write surface partitioned to a single writer (`index.md` **derived**; per-node gate log; catalog lock incl. cross-run and first-run-seed contention); stage 8's false *"no single global cursor"* claim corrected. | Tier-3 concurrency |
| **DEP** | Inter-leaf dependency ordering: a child dependency DAG, a cycle is a blocker, an assembled **Execution order** section, skeleton columns. | Tier-3 |
| **DEC / `elc`** | One operand — **`elc`**, honestly relabelled **self-declared, not computable**; ONE trip condition (two consecutive levels); the single-level contradiction in `decomposition-node.md` removed; what DEC *cannot* detect stated. | Tier-3 |
| **SPV** | The charter's spot-verify-citations duty is assigned to a **named stage** (stage 5; stage 7 for cross-node claims). | Tier-3 |
| **IGM** | `mode: fresh \| ingest-and-complete` defined, with `ingest_source`, an immutable ingest copy, a spine→locus **mapping table** with `ABSENT` rows, and a ban on silently authoring an absent section. | Tier-3 |
| **TPL3** | Back-propagation **stages a proposal**; a commit to the shared cross-project catalog happens only at run end, only by the top orchestrator, only under the lock, **only after a cold review of the proposed diff**. | Tier-3 |
| **RST** | The root plan node's on-disk location **pinned to `tree/root/`**; the apex roll-up moves to `tree/root/_status.md` (a **declared departure** from the approved layout). | Tier-3 |
| **SPN** | The §4 heading canonicalised to **one exact string** at every site (METHODOLOGY, SKILL, stages 2/3, all three seed skeletons). | Tier-3 |
| **(skeleton slots)** | `decomposition-node.md` and `leaf-task-spec.md` gain an explicit **Layer-2 `required_sections` slot**; `generic-node.md`'s italic note is promoted to the same explicit slot (all **3 of 3** lacked one). | Tier-3 |
| **(ID hygiene)** | METHODOLOGY's *"authoritative"* ID grep gains **word boundaries** (`grep -rlnow`) and the **`templates/` + `examples/`** scope; the phantom caveat and the ID-naming rule are stated; index rows added for the live-but-unindexed `TPL1`/`TPL2`/`SEV` and for every new ID. **Colliding IDs are not introduced:** the ingest-mode ID is **`IGM`**, never `ING` (⊂ `PLANNING`/`RULING`), and the killed-node ID reserved for the deferred F6 work is **`KLB`**, never `KIL` (⊂ `SKILL`) — enforced by `oracles/idcollide.sh`, not promised. | A/F1-2 |

### 3B — F8, ratified (R2)

| ID | Fix |
|---|---|
| **HG2** | A **second human gate, at assembly**: the human reads `assembled-plan.md` and approves or bounces it before the run is done. Under RAT3 this is a HALT + verbatim relay, never self-approved. **TOP's "ONLY" is narrowed to *decomposition* gates** — it still does not fire at deeper splits; HG2 is one gate at the end, not a gate per node. |
| **XPM** | The exit-plan-mode terminus is named (`assembled-plan.md`, or the root's `plan.md` for a single-leaf run) and is gated by **both** GBP **and** HG2 — correcting every site that asserts the terminus is gate-before-present-gated **only**. |
| *(forward constraint)* | The plan states that the **deferred** bottom-up-assembly work **must preserve a whole-assembled-plan reader**, since the naive bottom-up design deletes the only one and would strand HG2. |

### 3C — Subtractive honesty (removes claims; adds no mechanism)

| ID | Fix |
|---|---|
| **OFL** | `off_limits_paths` stops being stated as a guarantee. The current text — *"Naming is the fence — no guard catches a stray write the config never declared"* (`METHODOLOGY.md:99-101`) — is replaced by a plain statement that it is a **prompt-level convention, not an enforced fence**: nothing intercepts a write, and **nothing catches a stray write to a path the config never declared**. A run needing a real fence must get it from outside this skill. |
| **PRV** | *"Completeness is PROVEN"* is softened, at **all 8 occurrences across 5 files**, to what is actually established: **a decontaminated review occurred** and **the contract tiers are filled and cited** (with a spot-verified sample). Stated plainly: tier (iii) asks for a **negative no finite review can prove**, and **N same-model instances are not N independent minds** — separate spawns remove shared *context*, not shared *priors*. *"The gate raises the cost of shipping a hole; it does not certify its absence."* **This is the softening half of F7 ONLY** — no diversity mechanism is added, and none is claimed. |
| *(record-keeping)* | The numbers cycle 1 got wrong are corrected **in cycle 2's records** (`0-baseline.md` B2/B3), not by rewriting cycle 1: the corrected count is **21 live IDs vs 18 index rows**; cycle 1's B0.7 claim that the baseline passes `idcollide` is **false** (`DEC`/`TOP` violate it); and the surviving *"approved cycle-1 scope"* phrasing at `hardening-cycle-1/3-charter-given.md:206` + `hardening-cycle-1/decisions.md:41` is noted as superseded (§2.1). |
| *(no illegal escape hatch)* | This cycle's own records carry **no "declared deferral"** route for an unverified gating criterion. `Guarded_change/stages/stage-8.md` permits exactly two moves — a **representative pre-ship harness** or a **named risk-acceptance** — and under RAT3 with the owner not present a risk-acceptance cannot be granted here, so the only legal third move is **HALT + verbatim relay**. Cycle 1's `1.5-criteria.md:416` / `2-plan.md:375-378` contained such a route; it was correctly found illegal and is not reproduced. |

---

## 4. OUT OF SCOPE — deferred by R1; declared, not silently dropped

**None of these is demoted. Each remains an open blocker/major, moved out of this cycle's scope.**

- **F1 — the join / terminal-status producer / stage-ordering rework.** Not implemented. **The diagnosis
  is recorded for the next cycle:** the fix is a per-node stage order that writes the terminal status
  **last** (6 → 6.5 → 7 → *then* write it), **or** splitting `subtree` into `planning-complete`
  (stage 6/6.5) and `assembly-complete` (stage 7). Every attempt to name a producer without fixing the
  order re-bounced. Includes the `_status.md` schema, the escalate-to-parent route, bottom-up assembly,
  naming stage 7's actor, and **F6**'s killed-node marker + run-level abort (which cannot land without
  the schema). **Forward constraint from R2: the assembly rework must preserve a whole-assembled-plan
  reader.**
- **F2 — the seam-reopen detector (`seam_rev`).** Not implemented. Its operand (a recorded per-child
  declared seam hash) is exactly a class-(ii) fact whose producer position was the cap's second
  instance, so it waits for F1's ordering fix.
- **F5 — the topgate ratification mechanism.** Not implemented. **Recorded as now tractable:** the
  **session transcript JSONL is harness-authored** and is the admissible owner locus (an agent-written
  file — *including `LOOP-STATE.md`* — is not), **and this cycle demonstrated the discriminator** the
  caveat asked for (§2: a genuine owner turn is a `tool_result` keyed to an `AskUserQuestion`
  `tool_use_id`; a task-notification is not). **Consequence to state honestly: the stage-1 pre-creation
  of `plan/topgate/` still pre-satisfies TOP's bare-existence predicate**, so TOP remains defeatable
  after this cycle. BIND adds only a *staleness* condition over the approval artifact; it does not close
  F5.
- **DIV — the frame-diversity mechanism.** Not implemented and **not claimed**. Cycle 1's pass-2 version
  was rated *worse* than pass 1's by the reviewer who assessed both. PRV therefore states that whether
  frame diversity narrows correlated blind spots is **unsettled by this skill**, rather than asserting it.
- **The cost / fan-out envelope**, **ECON's O(children²) parent-seam load**, and the **"two passes"
  ruling** (still an unaudited owner ruling with no re-ask path — it stays on the owner queue, it is not
  declared settled).

---

## 5. Constraints

1. **RAT3 / delegation.** This loop runs in a subagent. Every stop-for-human **halts this runner and
   returns the question verbatim** to the orchestrator. No self-answering, no invented owner ruling, and
   **no "declared deferral"** for an unverified gating criterion.
2. **The artifact is a position-sensitive prompt assembly.** The position lens fires on *any* edit
   (add/move/remove). SKILL.md's up-front rule block is load-bearing *before* the stage table; anything
   added to it displaces what worked because of where it sat.
3. **A stage-0 baseline is REQUIRED and textual** (Layer-2, run 2+). Word-boundary matching is
   **mandatory** for every ID grep. Regression = a baseline rule that stops being stated, or starts being
   stated inconsistently, at a site the change did not intend to alter.
4. **Oracles must be shown able to fail** (ST1.5f / H6). A *mention*-check is not a read/write check; a
   checker that passes against the baseline tree is not an oracle. Cycle 1's three new instruments each
   failed their own can-fail test — this cycle mutation-tests every oracle it ships, and reports the
   mutation result.
5. **The skill must still trigger.** `SKILL.md`'s `description` is the trigger surface and PRV edits it.
   ≤1024 chars, no angle brackets, and the plan/design/decompose trigger vocabulary + the
   proactive-suggest clause must survive.
6. **`changes/initial-authoring-2026-07/` and `changes/hardening-cycle-1/` are frozen** and are not
   edited by this run.

---

## 6. Expected touched files (this list joins every cold reviewer's context)

**Artifact (edited):**
```
Architect/SKILL.md
Architect/METHODOLOGY.md
Architect/README.md
Architect/stages/charter.md
Architect/stages/stage-1-frame-template-match.md
Architect/stages/stage-2-draft-node.md
Architect/stages/stage-3-completeness-critic.md
Architect/stages/stage-4-adversarial-redteam.md
Architect/stages/stage-5-gate.md
Architect/stages/stage-6-granularity-decompose.md
Architect/stages/stage-7-assemble.md
Architect/stages/stage-8-restart-resume.md
Architect/templates/seed/README.md
Architect/templates/seed/generic-node.md
Architect/templates/seed/decomposition-node.md
Architect/templates/seed/leaf-task-spec.md
Architect/examples/authoring-a-skill/planning.md
Architect/examples/authoring-a-skill/README.md
```
**Live copy (re-synced at build):** `/home/zero/.claude/skills/architect/`

**Change records + instruments (new):**
```
Architect/changes/hardening-cycle-2/{0-baseline,1-spec,1.5-criteria,2-plan,3-redteam-plan,
                                     5-build-notes,6-build.diff,6-redteam-code,8-harness,decisions}.md
Architect/changes/hardening-cycle-2/oracles/{check.sh,baseline-replay.sh,ruleid-sitemap.sh,idcollide.sh}
Architect/changes/hardening-cycle-2/fixtures/X1..X4/{holed,intact}/
```
**Not touched:** `Architect/guarded-change.architect.md` (no config change is needed this cycle — the
run-2+ block already requires everything this run does), `changes/initial-authoring-2026-07/`,
`changes/hardening-cycle-1/`.

## 7. Prior art

`changes/hardening-cycle-1/` (the capped cycle — its `2-plan.md` D6/D10/D11/D15 text is the confirmed-closed
material this cycle ports); `changes/initial-authoring-2026-07/` (the frozen authoring criteria + fixture
style); `Guarded_change/changes/audit-hardening-2026-07/` (the precedent for a positive-per-site-assertion
oracle plus a baseline replay as its can-fail self-test).
