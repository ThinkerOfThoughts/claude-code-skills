# Stage 3 — cold review record, ARM F (VERBATIM) — **PASS 2**

**Verbatim record** (ART2): the reviewer's raw output, unedited, extracted mechanically from the
dispatcher's tool result. Author's interpretation → `decisions.md`; cross-arm synthesis →
`3-redteam-plan.pass2.md`; charter + closed set → `3-charter-given.pass2.md`.

| Field | Value |
|---|---|
| Arm / frame | **F** — fidelity/honesty + position + concurrency lenses |
| Agent type | `general-purpose` (cold subagent; no shared context with the author, none with the other arms) |
| Model | `claude-opus-5` |
| Dispatch handle (dispatcher-recorded) | tool-use id `toolu_01PAYzB1UB2hCQ7W94QMHgm6` — the dispatcher-observed identifier for this spawn |
| Self-reported identity | `spawn_id: unavailable` (declined to invent one — corroboration only, per IDN) |
| Context-file sha256s | in the reviewer's own `## Provenance` section below |

---

I have what I need. Writing the review.

---

# COLD REVIEW — Frame F: Fidelity/Honesty + Position + Concurrency

**Artifacts:** `hardening-cycle-2/{0-baseline.md, 0-baseline.B7-measured-sites.md, 1-spec.md, 1.5-criteria.md, 2-plan.md}` (WT = `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`).

## 1. Findings

**F/1 · BLOCKER · The "measured" site sets are not the measurement. Four gating criteria and the concurrency section contradict `0-baseline.B7-measured-sites.md`, the file they cite as their authority — which falsifies the pass's central R4-grounded claim and reproduces the exact half-migration defect it claims to fix.**

`2-plan.md:72`: *"Site lists are **not** hand-selected in this pass."* `1.5-criteria.md:17`: *"Every site list is the **measured** set in `0-baseline.B7-measured-sites.md`."* Against the measurement itself:

| Row | Claims | `B7-measured-sites.md` actually says | Delta |
|---|---|---|---|
| `1.5:71` **S-CNC-index** | *"all **9 measured** `index.md` files: S, M, s1, s6, s7, s8, tp/README, ch, ex/README"* | `B7:69-83` = **11 hits in 5 files** — M, s1, s6, s8, tp/README | **4 files invented** (S, s7, ch, ex/README) |
| `1.5:73` **S-CNC-gatelog** | *"all measured gate-log sites: S, M×3, s1, s3, s4, s5, s6, s8, ch"* | `B7:85-106` = **18 hits in 9 files**, incl. **`stage-7-assemble.md:11`**, ch×3, s3×2, s5×5 | **s7 dropped entirely** |
| `1.5:95` **S-HG2-only** | *"all **7 measured** 'top-level ONLY' sites: S:3, **S:77, S:86**, M:212, M:327, s6×3, tp/decomposition-node"* | `B7:57-67` = **7 hits in 4 files**, S:3 only | label says 7, list has **9**; S:77/S:86 not in the measurement |
| `1.5:99` **S-XPM** | *"all **10 measured** terminus sites"* then lists **14** | `B7:38-55` = **14 hits in 9 files** | label 10 ≠ list 14; and `1-spec.md:174` says ***six*** |
| `2-plan.md:194` §4 | *"`index.md` has **18 accessors across 9 files**… and the gate log **17 across 4**"* | index.md = **11 in 5**; gate log = **18 in 9**; **17 in 4 is P10 DEC/`elc`** (`B7:141`) | numbers **transposed across three sections** of the cited file |

I verified the four "invented" `index.md` files directly: `grep -rn "index.md" SKILL.md stages/stage-7-assemble.md stages/charter.md examples/authoring-a-skill/README.md` returns **zero hits**. Control: `S-RES-circ` (13/13) and `S-PRV-neg` (8 in 4) match `B7` exactly — so this is specific row failure, not uniform sloppiness.

*Failure scenario (concrete, and it is the pass's own named defect class):* the builder implements `S-CNC-gatelog` at its 10 listed sites. `stage-7-assemble.md:11` — a measured gate-log accessor — is never migrated, so stage 7 keeps reading `plan/decisions.md` for a per-node fact that now lives in `<node>/decisions.md`. `check.sh` passes (s7 isn't in SITES); `R2` passes (the CHANGE row has ≥1 pinned criterion). This is **C/O7 / B/L11 / B/L13 recurring in a new section** — under R4 that is under-generalization, and `2-plan.md:206` classes "a recurrence in a section this pass claims to have swept" as a genuine bounce.
*Fix:* regenerate all five site lists from `B7` mechanically; where a row must add an unmeasured site (as `S-SPN` legitimately does for the line-wrapped `S:18`, documented at `1.5:156-157`), mark it as a declared hand-addition with its reason, and reconcile the two off-by-one line cites (`1.5:99` `ch:132`/`s7:24` vs `B7:47,53` `ch:131`/`s7:25`).

---

**F/2 · BLOCKER · HG2's `"never self-approved"` ships as an unqualified positive claim at 2 of its 4 sites, contradicting the spec's own gating requirement that the limitation be stated *at the site* — and the proven authenticity fix this very cycle discovered is not applied to the gate that needs it.**

`1-spec.md:175-176`: HG2 *"ships with that limitation **stated at the site** (B/L15) rather than claiming *"never self-approved"* as a property its mechanism has."* Compare the criteria:

- `1.5:92` **S-HG2** pins *"…and **it is never self-approved**"* at **S, M, s7, s8**.
- `1.5:96` **S-HG2-limit** pins the limitation at **s7, M** only.

⇒ **`SKILL.md` and `stage-8` carry the unqualified assertion with no limitation.** `SKILL.md` is the router every invocation reads; `stage-8` is the restart contract, where the run-complete marker *is* the approval (`2-plan.md:58`). This is the identical structure `1-spec.md:153-154` forbids for PRV (*"Every site stating it must **also state, at that site**, what is merely attested"*) — applied to PRV, dropped for HG2.

Worse, on fidelity: `1-spec.md:205-211` records that **this cycle found the discriminator** — *"a genuine owner turn arrives as a **`tool_result` carrying the `tool_use_id` of a specific `AskUserQuestion`**"* — and §2 uses it to authenticate R1/R2/R3. `1.5:96` then pins *"the durable owner quote and its source are what an auditor can check"* — the artifact **names** the mechanism and **does not require it**. `FINDINGS.md:F9` defines the class: *"a gate whose satisfaction is asserted by the party it constrains"* (F5's class). Under R4 — the owner's words — *"the fix that was applied in that other section should be applied here"*: the fix exists one field away, exactly as `1-spec.md:83` argues for B/L6. Note also that `2-plan.md` §1 row 22 verdicts HG2 **OK** having asked only (a)/(b)/(c) — the sweep's class definition does not include this defect class at all.
*Fix:* add S and s8 to `S-HG2-limit`'s SITES, and require `plan/assembly-approval.md` to carry the transcript `tool_use_id` + record locus of the owner turn (the field already proven in §2), not merely a stated duty.

---

**F/3 · MAJOR · R4's ratification record fails the RAT1 bar R1–R3 meet: it quotes no options, records an axis that was never presented, and cites an agent-authored file as its source — while §2's header asserts all four were verified against a harness-authored source.**

`1-spec.md:97`: *"OWNER RATIFICATION RECORDS (RAT1) — **four, all verified against a harness-authored source**."* But `1-spec.md:20-22` sources R4 to *"recorded in `LOOP-STATE.md` with the **session transcript** … as its cited source"* — second-hand, via a file the assistant wrote (`LOOP-STATE.md`, sha `b0b737e3…`), with **no record number and no `tool_use_id`**, where R1/R2/R3 get records 694/699 + `toolu_01Ga2368vabihTBcFVBZEYte` (`1-spec.md:103-106`).

I fetched the transcript myself. **The admissible record exists and the spec does not cite it:**
- Record **784** — `type: assistant`, `2026-07-25T15:25:17.056Z`, `AskUserQuestion` `id: toolu_01R11yeNtGRvicasDVg9czYo`, **four** options: *"Ship the wording fixes, defer machinery (Recommended)" · "Try the machinery again (third attempt)" · "Stop the loop entirely" · "Something else — let me think out loud"*.
- Record **789** — `type: user`, `2026-07-25T15:29:03.822Z`, `tool_result` keyed to that same `tool_use_id`, carrying the owner's words **exactly** as `1-spec.md:17-19` quotes them.

So the quote is true, but two RAT1 elements fail: **(i) options-verbatim is absent** — and the options matter, because the owner **selected none of them** (record 789's `answers` value is free text); **(iii) the recorded axis is not the axis presented.** `1-spec.md:23-24` states the flagged axis as *"how to treat a known defect class that resurfaces in a section the previous round's reviewers did not examine"* — that is the author's post-hoc reframing. The presented axis (record 784) was *"Given all that — how should the loop proceed?"* over ship-narrow / retry / stop / discuss. `LOOP-STATE.md:102` compounds it, calling them *"the three options"* when four were presented (three were presented at record **780**, which the owner answered *"need more context on this, also, less shorthand"* at record 781).

*Affirmative, and I confirm it:* the owner **rejected** the `(Recommended)` option at both 784 and 699, so the CH11 "resolved into the author's own pick" mode does **not** fire for R1/R3/R4. And the answer does disambiguate the live axis (it rules out "stop"). This is a **record-quality** blocker-adjacent defect, not a fabricated ruling.
*Fix:* cite record **789** + `toolu_01R11yeNtGRvicasDVg9czYo` (+ 784 for the options), quote the four option labels verbatim, state the axis **as presented**, note the owner declined all four, and correct `1-spec.md:97`'s "all four" claim.

---

**F/4 · MAJOR · Unratified inflation: three operative commitments not entailed by the owner's sentence are filed as *Owner-ratified* at `1-spec.md:141`.**

The owner's ratified words (record 789) are **reactive and conditional**: *if* the same kind of problem was encountered/fixed elsewhere, *then* apply that fix here; a previous-round non-catch means nothing. Operative terms: *same kind of problem · the fix that was applied · should be applied here · means nothing*. Built on it:

| Commitment | Where | Entailed? |
|---|---|---|
| *"a fix is **not done** when the sections under review pass — it is done when **every site in the class is swept**"* | `1-spec.md:27-28`, labelled *"What it entails, and no more (RAT2)"* | **No.** The owner's sentence licenses applying a proven fix at a **recurrence**; it says nothing about a proactive exhaustive sweep or a definition of "done". This adds an *every*-quantifier and a completion criterion. |
| The three-question checklist **(a) Producer · (b) Degenerate case · (c) Counterpart** | `1-spec.md:58-64`, `2-plan.md:17-21` | **No.** Producers, degenerate cases and release paths appear nowhere in the ruling; they are the reviewers' diagnosis, i.e. a sound authoring choice. |
| *"**No mutation may be labelled class (i)**"* | `1-spec.md:60`, `2-plan.md:23` | **No.** An absolute *never*, derived from B/L2. |

`1-spec.md:141` lists *"**R4's generalize-and-sweep discipline**"* under **Owner-ratified**; GEN as defined at `1-spec.md:53-64` *is* the sweep plus the checklist plus the never-rule. The inflation is inherited verbatim in substance from `LOOP-STATE.md:113-117` (*"Corollary the owner's words entail (and no more — RAT2)"*), and the charter is explicit that an inherited definition *"is a **claim to re-verify** against owner intent, not a spec"* (`Architect/stages/charter.md:46-48`) — the spec re-asserts it instead.
*Fix:* split `1-spec.md:141`: Owner-ratified = *"when a defect class recurs in a new section, apply the fix already proven elsewhere, and treat the prior round's non-examination as carrying no information."* Move the sweep-completion criterion, the (a)/(b)/(c) checklist and the class-(i) prohibition to **"Orchestrator call, within the ratified frame"** (they are good calls; they are not ratified).

---

**F/5 · MAJOR · The third undeclared departure from the approved layout: `index.md`'s content-and-authority contract is gutted, and D13 declares only two departures.**

Approved record `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:165`:
`├─ index.md ← plan tree + per-node {template used, status, gate state, leaf?/decompose?}` — an authoritative per-node index at run-root, naming **`template used`** as its content.

This cycle: `1.5:71` **S-CNC-index** pins *"`index.md` is **derived and never authoritative**"*; `1.5:72` **S-CNC-tmpl-dest** relocates `template used` to the node's `plan.md` header with paired absence `record template: <name> in index.md` (must appear nowhere). `2-plan.md:144-147` (D13) declares exactly **two** departures — the `_status.md` apex and the `decisions.md` partition. A/F5 (`3-redteam-plan.A.verbatim.md:95`) was the finding that pass 1 declared one of two; pass 2 declared the second and left the third. Same class, new section ⇒ under R4, under-generalization.
*Fix:* declare it in D13 as departure (iii), naming the approved line and the operand that would restore it.

---

**F/6 · MAJOR · A/F6 is not closed: the charter fork-provenance fix records only *additions*, re-frames the one *reassignment* A/F6 named as an addition, and criterion 57's paired absence contradicts its own parenthetical.**

A/F6's prescribed fix (`3-redteam-plan.A.verbatim.md:130`): the blockquote's *"ADDED/DROPPED/carried enumeration must name **every local modification** this cycle makes to a carried core bullet."* Pass 2 delivers ADDED-only: `2-plan.md:168-170` (D18) records *"what Architect's fork now **ADDS** … the `spawn_id` field, BIND's comparison duty, **stage 5 as the named spot-verify consumer**, the node-local gate log"*; `1.5:104` pins `ADDED by Architect's fork beyond the carried core:`.

"Stage 5 as the named spot-verify consumer" is **not an addition — it is a narrowing of a carried core bullet.** I verified upstream: `Guarded_change/stages/charter.md:59` (sha `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`, identical to the blockquote's cited hash at `Architect/stages/charter.md:12`) reads *"**Spot-verify the citations themselves.** **Whoever consumes the review** checks a sample…"*, and `1.5:69` **S-SPV** makes `whoever consumes the review checks` a **corpus-wide paired absence**. Scope goes from *any consumer* to *stage 5*. Likewise the closed-input-set bullet (upstream `charter.md:74`) is narrowed by `S-IDN-sibling` and `S-IGM-closed`. So `Architect/stages/charter.md:22`'s *"**DROPPED:** nothing from the core"* becomes **false**, and it is handed to every cold reviewer verbatim (`charter.md:8-9`).

Compounding: `1.5:104`'s Paired-absence column lists `DROPPED: nothing from the core.` (⇒ must appear **nowhere**) with the parenthetical *"(kept only if still true…)"* (⇒ may be kept). Those cannot both hold; the checker will fail whichever the builder picks, and nobody has adjudicated the truth question.
*Fix:* the blockquote must carry a **NARROWED** clause naming the spot-verify reassignment and the closed-set narrowings; resolve `1.5:104` to a single disposition.

---

**F/7 · MAJOR · The `off_limits_paths` overclaim is deleted and reintroduced: criteria 17 and 19 pin contradictory statements at two shared sites.**

- `1.5:66` **S-OFL** — *"off_limits_paths is a prompt-level convention, **not an enforced fence**"* @ **M, s1, ex/planning**; paired absence `Naming is the fence`.
- `1.5:64` **S-CTX-deconf** — *"…**off_limits_paths is a fence the run must never write into**…"* @ **M, ex/planning, ex/README**.

Overlap = **M and ex/planning**, where both pinned strings must be present. The paired absence (`Naming is the fence`) does not catch `is a fence the run must never write into`, so `check.sh` passes both. F7's honesty fix is undone in the same file by the de-conflation row, and `ex/README` gets *"is a fence"* with no counterpart at all.
*Fix:* re-pin `S-CTX-deconf` as *"off_limits_paths is the never-write **declaration**"* (or *"an unenforced fence"*), and add `off_limits_paths is a fence` to `S-OFL`'s paired-absence set so the checker actually observes the collision.

---

**F/8 · MAJOR · PRV's positive half — the half the spec admits was never closed — ships under an "every site" duty whose site set is the only one in the file that was never measured.**

`1-spec.md:153-154`: *"**Every** site stating it must **also** state, at that site, what is merely attested … `S-PRV` makes that a gating assertion."* `1.5:68` **S-PRV-limit** SITES = *"**every site carrying the positive claim** — M (the PRV block), S:8, s7"*. `B7` measures **P6 = the 8 overclaim sites** (`B7:25-36`) and measures **no positive-claim set at all**. So the "every" is asserted over a hand-picked 3, in the exact row where §2.1 concedes *"that positive half is recorded in `LOOP-STATE.md` as **never closed**"* (`1-spec.md:148-149`).

*Concrete gap:* `S:3` — the frontmatter `description` — is an overclaim site (`B7:31`) and must be rewritten by `S-PRV-neg`. Whatever positive framing replaces *"completeness is PROVEN"* there lands in the skill's **only trigger surface**, and `S-PRV-limit` does not cover `S:3`. The description cannot carry the limitation (≤1024 chars, SC1), so either the positive claim ships there naked or the description must drop it — and no criterion forces that choice.
*Fix:* measure the positive-claim set (grep the corpus for the attestation claim) before pinning "every"; state explicitly that the description carries **no** positive completeness claim, and pin that as an absence.

---

**F/9 · MAJOR · SC3 is the sole guard for two pass-1 position majors and is the one row in the file with neither a pinned string nor a mutation test — violating the file's own absolute rule.**

`1.5:24`: *"**M** = mutation test of the oracle itself (**mandatory for every P/P-PROXY row**)."* `1.5:128`: *"**SC3 · gating · P + X2**"* — no M, and no PINNED STRING, because pinned strings live only in §1's table and SC3 sits in §3. SC3 is nevertheless the only place carrying (a) the intra-block order `CMP → PASS1/PASS2 → PRV → HG2 → GBP last` and (b) *"the block's **closing rationale is re-enumerated** to name all five"* — i.e. the entire fix for **A/F1** and for the pass-1 order reversal. A/F1's own analysis was *"No criterion catches it"* (`3-redteam-plan.A.verbatim.md:37`); pass 2 moves it into SC3 prose with no assertable string, so a builder who re-enumerates three of five, or four of five, is not caught. Pass-1's **A/F10** (*"SC3 is a P row with no M"*) is therefore also still open.
*Fix:* promote both halves into §1 as pinned rows (the rationale sentence is verbatim-pinnable) and give SC3 its mandatory M.

---

**F/10 · MAJOR · The concurrency claim "the accessor set is reduced to one writer" is false for `_status.md`: its writer is deferred to cycle 3, so the file has *zero* named writers and live readers.**

`2-plan.md:196`: *"For `index.md`, `_status.md` and the gate logs the guard is **not a lock**: the accessor set is reduced to **one writer**, so **there is no scope gap**."* But `1-spec.md:218` defers it: *"`tree/root/_status.md`'s writer (needs the deferred schema)"*, carried to cycle 3. `FINDINGS.md` F1: *"`_status.md` is named as the up-flow vehicle **5×** but **no stage writes one or defines its schema**."* Readers persist — `S-RST-root` (`1.5:89`) pins the apex roll-up at M, s1, s7, s8, and ECON's lean surface reads it (`1-this-is-a-proud-scott.md:118`).
*Failure scenario:* stage 7 or the apex roll-up reads `tree/root/_status.md`; nothing ever wrote it; the reader has no defined behaviour for absence (no degenerate-case row in `2-plan.md` §1 covers `_status.md` at all). "One writer, no scope gap" is asserted about a surface with a **deferred** writer — a claim of closure over deferred work.
*Fix:* drop `_status.md` from the §4 claim and state plainly that it has no writer this cycle and no reader may depend on it; or give the readers a defined absent-case.

---

**F/11 · MAJOR · `<run-root>/catalog-pending/` is a newly load-bearing shared surface with N concurrent writers, no guard, and no collision rule — and it is absent from the accessor enumeration entirely.**

`1.5:88` **S-TPL3** pins *"back-propagation stages a proposal into `<run-root>/catalog-pending/`"*. Writers = **every decomposing node's owner at stage 6**, and sibling sub-orchestrators run **in parallel** (`1.5:70` **S-CNC-decl**: *"parallel: sibling sub-orchestrators"*). Reader = the top orchestrator at run end. `2-plan.md` §1 row 18 lists the operand `catalog-pending/*` with counterpart *"n/a — but see #19"*, and `2-plan.md:196` states *"The **only** lock is the catalog"* — `catalog-pending/` lives in the run-root, not the catalog, so it is covered by nothing.
*Failure scenario:* two sibling sub-orchestrators both skeletonize a fix to the same matched template and stage `catalog-pending/<template-name>.md`. Last writer wins; one node's proposal is silently lost, and the run-end commit (under the lock, after a cold review of the diff, `1.5:88`) reviews a diff that never contained it. No filename-uniqueness rule, no per-node subdirectory, no criterion.
*Fix:* namespace it per node (`catalog-pending/<node-path>/…`) — a one-writer reduction that actually holds — and add the row to §1 and §4.

---

**F/12 · MAJOR · The catalog lock's stale-lock discriminator is a *pid*, which is undefined for the accessor type that actually holds it — so after the failure mode this project has already suffered, the lock provides no mutual exclusion.**

`1.5:76` **S-CNC-LOCK-stale**: *"a lock whose **recorded pid is not running** may be broken only by writing `BROKEN-BY` … a lock whose pid IS running is waited on, and after the stated wait the run HALTS."* The holder is an **LLM agent**, not a process. The only pid available is that of the transient `bash` invocation that ran `mkdir`, which is dead the moment the call returns.

*Failure scenario, already observed:* `FINDINGS.md` meta-observation 5 — *"Session limit at ~21:25 killed the orchestrator"*. Orchestrator A holds the lock; its session dies mid-seed, so `rmdir` never runs (`1.5:74`'s *"on every failure path, including before any HALT"* is a **prompt-level duty**, not a `finally` block — there is no enforced release for an agent that is killed). Orchestrator B starts, reads the recorded pid, finds it not running (it never was), writes `BROKEN-BY`, and breaks the lock. Now consider the same read while A is **alive but mid-step**: the pid is *equally* dead, so B breaks a **live** lock. The discriminator returns "dead" in both cases ⇒ the lock degrades to advisory, while `2-plan.md:199` labels `S-CNC-LOCK` *"GATING and executed"*.

Related scope challenge, same guard: `1.5:77` **S-CNC-readers** — *"a reader takes the same lock, **or** reads a git commit"*. Stage 1 template-match reads the catalog at **every node**, and siblings are parallel; if the builder takes the "same lock" branch, sibling reader contention hits `S-CNC-LOCK-stale`'s live-pid path and **HALTs the run** on ordinary concurrent reads. The alternative is offered, not required.
*Fix:* record a **liveness token the agent can actually refresh** (a heartbeat mtime on the lock dir with a stated staleness window) rather than a pid; and make the git-commit branch **mandatory** for readers so reader contention cannot HALT.

---

**F/13 · MAJOR · `index.md`'s "one writer" closes the write-write race and leaves the read-during-write race open, with no quiescence trigger — and the trigger it would need is deferred F1.**

`1.5:71`: *"the top orchestrator **regenerates it by walking the tree** and reading each `<node>/plan.md` header."* One writer eliminates concurrent writes to `index.md`. It does not address the regenerator's **reads**: `<node>/plan.md` is written by that node's stage 2 (`2-plan.md` §1 row 7) **concurrently** with the walk. `2-plan.md:196` claims *"there is no scope gap"* — there are two:
1. *Torn/partial read* — the walk reads a `plan.md` header mid-write, or a node directory that exists with no `plan.md` yet (which `RST` defines as *"the not-planned marker"*, row 6 — indistinguishable from "created 200ms ago").
2. *No trigger and no quiescence condition* — nothing says **when** the regeneration runs, and the mechanism that would tell the top orchestrator the tree is quiescent is the **stage-6.5 join, deferred as F1** (`1-spec.md:193`). So the guard's correctness depends on out-of-scope work.

*Fix:* state that regeneration runs only at a defined quiescent point (post-stage-7, pre-terminus), and that an `index.md` generated mid-run is explicitly non-authoritative — which is consistent with `S-CNC-index`'s own "derived" framing.

---

**F/14 · MAJOR · "The skill must still trigger" is pinned to two string proxies, and the plan's risk table mislabels them as measuring triggering.**

`1-spec.md:237-238` (constraint 5): *"**The skill must still trigger** — `description` ≤ 1024 chars, no angle brackets, trigger vocabulary + proactive-suggest clause preserved, **measured** not assumed."* `2-plan.md:220` risk row: *"The softened description stops triggering | **SC1 + SC2, both measured**."* SC1 (`1.5:124`) measures length + angle brackets; SC2 (`1.5:126`) measures presence of `plan`, `design`, `decompos`, `Proactively SUGGEST`. **Neither observes triggering.**

This matters because `S-PRV-neg`'s paired absence deletes `PROVEN` (case-sensitive) and `proven, not asserted` **corpus-wide**, and both occur in the description's opening clause (`SKILL.md:3`, = `B7:31` site `S:3`). The description's strongest hook is being rewritten under a criterion that cannot see the consequence.
*Failure scenario:* the rewritten description retains all four SC2 tokens and every SC1 bound, loses the *"no plan is presentable until…"* framing, and the skill's dispatch rate drops. SC1 ✔, SC2 ✔, no criterion fails, nothing observes it — while `1.5:194-195` claims the coverage challenge from cycle 1 is closed.
*Fix:* relabel the risk row honestly (SC1/SC2 are structural floors, not trigger measurements), or add a real arm: N held-constant spawns given a planning-shaped request, with the old and new description as the only variable.

---

**F/15 · MAJOR · `SKILL.md:103-104`'s mnemonic rule-ID list is a stale closed list governing the standing self-check, and no criterion updates it.**

`SKILL.md:102-104`: *"Standing self-check criteria after any edit: … SKILL ↔ METHODOLOGY ↔ stage-file ↔ charter consistency on **every rule stated in more than one place** (linked by the **mnemonic rule-IDs** … — GBP, PASS1/PASS2/PASS-ORD, CMP/CMP2, SPN, COV, ORC/ECON, GRN, TOP, CAP, DEC, TPL/TPL3, RST, RAT3)."* This cycle adds 12 IDs (BIND, IDN, RES, CTX, OFL, PRV, SPV, CNC, DEP, IGM, HG2, XPM). `1.5:103` **S-INDEX-complete** covers **METHODOLOGY's** cross-file rule index only. I confirmed by grep that `SKILL.md:103` is the sole site of this list, and no `S-` row includes `S` in its SITES for the new IDs' index purpose.
*Failure scenario:* a future editor follows `SKILL.md`'s standing self-check verbatim, checks cross-file consistency for the 14 listed IDs, and skips all 12 new ones — including HG2 and PRV, the two whose sites span 4+ files. The instruction that governs every subsequent edit to a position-sensitive prompt assembly silently under-scopes by 46%.
*Fix:* add a pinned row asserting `SKILL.md`'s list equals METHODOLOGY's index ID set, or replace the enumeration with a pointer to the index.

---

**F/16 · MAJOR · `<node>/decisions.md`'s "written only by that node's owner" is contradicted by the baseline back-propagation path, which the sweep has no row for.**

`1.5:73` **S-CNC-gatelog** pins *"the per-node gate log is `<node>/decisions.md`, **written only by that node's owner**"*. `SKILL.md:71` (stage 6, baseline): *"spawn sub-orchestrators + recurse; **back-propagate hole-fixes**"*. A parent that back-propagates a hole-fix into a child's plan produces a gate-relevant event **in the child's node, authored by the parent**. `2-plan.md` §1 sweeps 26 predicates and has **no row for back-propagation** — so this accessor is in neither the (a)/(b)/(c) table nor §4's enumeration, despite `2-plan.md:14` claiming coverage of *"**every** predicate and gate in the design — baseline rules included"*.
*Failure scenario:* parent back-propagates; either it writes the child's `decisions.md` (violating the pinned "only by that node's owner" — a same-file two-writer race with the child's own stage 5) or it writes nothing (the child's BIND rebind chain, which lives in `<node>/decisions.md`, `2-plan.md` §1 row 9, loses the link and the child's records read as current against a parent-modified `plan.md`).
*Fix:* add a back-propagation row to §1; specify that a parent's back-propagated fix is recorded by **the child's owner on re-entry at stage 2**, preserving the single-writer property.

---

**F/17 · MAJOR · "A clean run terminating and presenting IS now observed" is declared, not observed — what is observed is a cold agent's verdict on a fixture.**

`1.5:194-195`: *"**A clean run terminating and presenting IS now observed** — S-HG2-degen + X2's intact arm are exactly that check. *(This closes cycle 1's carried-forward coverage challenge, which pass 1 left open: C/O16.)*"* But the X protocol (`1.5:176`) is: *"Each spawn returns `VERDICT: <one of the named options>` + the rule ID applied and its citation."* An X2 intact arm therefore observes that **an agent handed a fixture says it would proceed** — a proxy for a run, not a run. No Architect run is executed to a terminus in this cycle (the whole cycle is a docs change; the only executed instrument is `lockrace.sh`). "Observed" and "closes" are the loaded terms; the mechanism is an agent judgment.
*Fix:* restate as *"an agent's verdict on a representative fixture is observed; an end-to-end terminating run is not"*, and either keep C/O16 open or discharge it with an actual single-leaf run.

---

**F/18 · MINOR · A/F12 is not closed: R1's option description is still presented as quoted-not-paraphrased with an unmarked truncation.**

`1-spec.md:109-110`: *"The option's own presented description bounds the scope and **is quoted rather than paraphrased**"*, ending at *"…defer to a later cycle."* Record **694**'s description continues: *"Bounded blast radius, real delivered value, and the ordering diagnosis + transcript-locus correction make the deferred work tractable next time."* No `…` marker, in the record whose stated purpose is spot-checkability — and `1-spec.md:117-120`'s R2 quote *is* complete (I verified both against 694), so the asymmetry stands out. Pass 1's A/F12 said exactly this.
*Fix:* add the elision marker or the sentence.

**F/19 · MINOR · A fifth owner ruling (R5) exists in the same durable source and defines "success" for this very pass; `1-spec.md` §2 says "four" and never mentions it.**

`LOOP-STATE.md:152-176` records **R5** — owner words at transcript record **805** (*"you're correct, if this works, spin off a dedicated chat to add the rule to guarded-change; then pause while I tend to that, once I'm back, add the rule to Architect using guarded-change"*) and the confirmation at record **820** (*"correct on all counts"*), both of which I verified. R5's ratified precondition: *"Success = pass 2 **clears gate 4** and the fixes are **built and verified** (through gate 7 / stage 8), not merely 'the plan passed review.'"* A reader of `1-spec.md` alone would take clearing gate 4 as success.
*Cleanly checked and clean:* R5's step 4 (add the class-sweep rule **into** Architect) is deferred work, and I confirmed **no criterion pre-shapes it** — none of the 57 `S-` rows pins a class-sweep rule into `charter.md` or any stage file. GEN governs *this change*; it is not shipped into the artifact. Correct restraint.
*Fix:* record R5 in §2 with its precondition, or state in §5 that "success" for this pass is defined by R5.

**F/20 · MINOR · Position: PRV puts a de-escalating rule into the read-first block of maximum authority, and the only position arm tests solely that GBP still fires.**

`SKILL.md:15` heads the block *"The rules that govern everything — read first"*; rules 1–3 are all imperatives. PRV is a disclaimer (*"The gate raises the cost of shipping a hole. It does not certify its absence."*). `1.5:131-133`'s X2 arm requires only *"GBP still fires — GBP ceasing to fire is a position regression even with its text intact."* Nothing tests the converse: whether a disclaimer in the read-first block makes an agent **more willing to present** a plan it judges good enough — i.e. PRV becoming an exemption, the precise mechanism `1-spec.md:37-49` diagnoses for `class (i)` (*"the label's exemption is what kept anyone from noticing"*).
*Fix:* add a second X2 assertion — the intact arm must **still block** a plan with an un-gated node after PRV is in the block.

**F/21 · MINOR · Position: `SKILL.md:8-13`, the thesis paragraph, becomes the load-bearing site for three separate hedges at once.**

`S:8` is simultaneously a PRV overclaim site (`B7:32`), an XPM terminus site (`B7:45`), and an `S-PRV-limit` site (`1.5:68`). After the build, the paragraph immediately under the H1 — the file's highest-salience prose, which states the founding failure — carries the softened claim **plus** the both-gates statement **plus** the attestation/correlated-blind-spots limitation. No criterion observes whether the founding-failure statement survives as the paragraph's dominant content.
*Fix:* pin the founding-failure sentence itself as a preserved string at `S:8`, so the hedges cannot crowd it out.

---

## 2. Ratification audit (CH11/CH12)

I fetched `45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl` (840 records) and extracted records 693-700 and 780-793 with python. All quotes below are from that extraction.

| | **R1** ship-narrower | **R2** HG2 human gate | **R3** loop exit | **R4** apply-the-proven-fix |
|---|---|---|---|---|
| **Options verbatim?** | ✔ description quoted, **truncated w/o marker** (F/18) | ✔ **exact, complete** — verified char-for-char vs 694 | ✔ label verbatim; description paraphrased and not claimed verbatim | ✖ **none quoted**; `LOOP-STATE.md:102` says "three options", **four** were presented |
| **Owner words verbatim?** | ✔ | ✔ | ✔ | ✔ — `1-spec.md:17-19` matches record **789** exactly |
| **Durable source, fetched by me?** | ✔ 694 (`toolu_01Ga2368vabihTBcFVBZEYte`, `2026-07-25T14:03:05.318Z`) + 699 (`tool_result`, same `tool_use_id`, `14:10:24.209Z`) | ✔ same pair | ✔ same pair | ✖ **cites `LOOP-STATE.md` (agent-authored)**. The admissible record **exists and is uncited**: 784 (`toolu_01R11yeNtGRvicasDVg9czYo`, `15:25:17.056Z`) + 789 (`tool_result`, same id, `15:29:03.822Z`) |
| **Axis as presented?** | ✔ "SEV4 tie-break…" | ✔ "F8…should a human review the *assembled* plan…" | ✔ "My narrowing of your 'until nothing surfaces'…" | ✖ `1-spec.md:23-24` states a **post-hoc reframing**; presented axis was *"Given all that — how should the loop proceed?"* |
| **Mapping disambiguates?** | ✔ label selected exactly | ✔ label selected exactly | ✔ label selected exactly | ~ owner **selected none of the four**; free text. It does rule out "stop" and does license proceeding, so the *live* axis is settled — but the record must say so |
| **Author's-own-pick failure mode?** | ✖ does not fire — but note the owner **did** pick `(Recommended)` here | n/a (no Recommended) | ✖ owner **rejected** `(Recommended)` | ✖ owner **rejected** `(Recommended)` at both 780 and 784 |
| **CH12 elaboration inflation?** | clean — §2.1 honestly files the non-parenthetical items as orchestrator calls | clean — all three consequences are inside 694's description text, which I verified; *"how a bounce routes"* correctly marked unratified (`1.5:97` S-HG2-authored) | clean | **✖ three inflations filed as Owner-ratified — see F/4** |

**Verdicts.** R1: ratified, minor quote defect. R2: **ratified cleanly** — the strongest of the four. R3: ratified cleanly. **R4: the ruling is genuine and the quote is accurate, but the *record* does not meet the RAT1 bar R1-R3 meet** (F/3), and the discipline built on it exceeds the ratified text (F/4). Per CH11 the axis need **not** be re-asked — the owner's words do settle the live question — but the record must be rebuilt to cite record 789 and the elaboration re-filed.

**Ratified phrase's operative terms (for the RAT2 trace):** *same kind of problem · encountered/fixed in a different section · the fix that was applied in that other section · should be applied here · that it didn't catch it … means nothing.* Terms **added** by the elaboration and traceable to nothing in that set: *not done · every site · swept · producer · degenerate case · counterpart · no mutation may be labelled class (i)*.

---

## 3. Honesty audit

| # | Positive claim the artifact will make | True? | Checked by whom? | Limitation stated? | Verdict |
|---|---|---|---|---|---|
| 1 | *"a review record is current iff the dispatcher-recorded `plan_sha256` equals `sha256(plan.md)` now"* (`1.5:48`) | Yes | `check.sh` (text) + X1 arm (agent verdict) | n/a | **OK** |
| 2 | *"never self-approved"* (HG2, `1.5:92`) @ S, M, s7, s8 | **No — a duty, not a property** | text check only | **at s7, M only — absent at S and s8** | **FAIL → F/2** |
| 3 | *"TOP remains defeatable… stage 1 still creates it"* (`1.5:55`) | Yes | text | Yes, at the site | **OK — model row** |
| 4 | PRV positive: *"attested by the reviewers themselves and sampled, not independently proven"* (`1.5:68`) | Yes | text | Yes — **but over an unmeasured "every site" set excluding `S:3`** | **PARTIAL → F/8** |
| 5 | *"off_limits_paths is … not an enforced fence"* (`1.5:66`) | Yes | text | n/a | **OK** in itself — **contradicted at M, ex/planning by `1.5:64` → F/7** |
| 6 | *"off_limits_paths is a fence the run must never write into"* (`1.5:64`) | **No** | text | No | **FAIL → F/7** |
| 7 | *"Every site list is the measured set in B7"* (`1.5:17`); *"not hand-selected"* (`2-plan.md:72`) | **No — 4 rows + §4 diverge** | nothing; `check.sh` asserts the list, not its provenance | No | **FAIL → F/1** |
| 8 | *"`index.md` has 18 accessors across 9 files… gate log 17 across 4"* (`2-plan.md:194`) | **No — 11/5 and 18/9; "17 across 4" is P10's figure** | nothing | No | **FAIL → F/1** |
| 9 | *"the accessor set is reduced to one writer, so there is no scope gap"* (`2-plan.md:196`) | **No** for `_status.md` (no writer at all) and **incomplete** for `index.md` (read-during-write, no quiescence) | nothing | No | **FAIL → F/10, F/13** |
| 10 | *"the only lock is the catalog, and its scope now covers five paths"* (`2-plan.md:196`) | Scope claim overstated — `catalog-pending/` uncovered; liveness discriminator undefined | `lockrace.sh` (real race, real crash case) | *"two runs sharing one `run_root`"* declared uncovered (`1.5:78`) — but **undetected** | **PARTIAL → F/11, F/12** |
| 11 | *"S-CNC-LOCK is GATING and executed"* (`2-plan.md:199`) | Executable: yes | `lockrace.sh` | No | **OK on executability** |
| 12 | *"charter's fork-provenance blockquote stays true"* (`1-spec.md:242-244`) | **No** — ADDED-only leaves *"DROPPED: nothing"* false | SC5 rubric, judged by **this runner** | No | **FAIL → F/6** |
| 13 | *"A clean run terminating and presenting IS now observed"* (`1.5:194`) | **No — an agent verdict on a fixture is** | X2 arm | No | **FAIL → F/17** |
| 14 | *"The skill must still trigger … measured"* (`1-spec.md:238`); *"SC1+SC2, both measured"* (`2-plan.md:220`) | Length/tokens measured; **triggering not** | SC1/SC2 string checks | No | **FAIL → F/14** |
| 15 | *"four, all verified against a harness-authored source"* (`1-spec.md:97`) | **No — R4 is sourced to `LOOP-STATE.md`** | R1-R3 by the runner **and** reviewer A (`spawn_id aea2863bc75a6d6a5`, records 694/699 re-verified at `3-redteam-plan.A.verbatim.md:223-224` — I confirmed both) | No | **FAIL → F/3** |
| 16 | *"R4's generalize-and-sweep discipline"* = Owner-ratified (`1-spec.md:141`) | **No** for the sweep-completion criterion, the checklist, the never-rule | nothing | *"What it entails, and no more (RAT2)"* — an **assertion of** entailment | **FAIL → F/4** |
| 17 | *"the two orchestrator-owned corrections already made"* (`1-spec.md:219`) | **Yes** — I verified `LOOP-STATE.md:9-13` now carries the ⚠ correction to the terminate rule | me, now | Yes | **OK** |
| 18 | *"`LOOP-STATE.md` calls the broad reading an 'Interpretation … stated so Roy can correct it'"* (`1-spec.md:132-133`) | **Yes** — verbatim at `LOOP-STATE.md:15` | me, now | Yes, carried | **OK — the A/F4 correction is real** |
| 19 | *"8 overclaim occurrences across 4 files, not 5"* (`1-spec.md:179-180`) | **Yes** — `B7:36` = 8 in 4 | B7 grep | n/a | **OK** |
| 20 | *"No 'declared deferral' route exists"* (`1.5:27`, `2-plan.md:211`) | Yes — I found no deferral disposition in either file | text | RAT3 HALT named | **OK** |

---

## 4. Position lens (my own analysis of the assembled `SKILL.md`, sha `7584924a…`)

**Pass 2 restores the ordering rule — confirmed.** `1.5:129` states `CMP → PASS1/PASS2 → PRV → HG2 → GBP last`. Against the live file: rule 1 CMP (`SKILL.md:17`), rule 2 PASS1→PASS2 (`:25`), rule 3 GBP (`:33`), closing rationale (`:39-41`). Inserting PRV and HG2 at slots 3-4 leaves **GBP last** ⇒ GBP keeps the recency slot, reversing pass 1 (which A/F1 documents as having put HG2 *"after* the three existing rules"). **A/F1's order half: closed.** Its rationale half is required only in SC3 prose with no assertable string (**F/9**).

**What else moved — including elements that did not themselves change:**

1. **GBP's own justification, unchanged text, changed truth.** `SKILL.md:36-37`: *"This is **the** direct gate on the founding failure — a hard precondition, not advice."* HG2 makes GBP one of two terminus gates. Covered: `S-XPM` (`1.5:99`) includes `S:33` — GBP's line — in its both-gates assertion. **No finding.**
2. **The closing rationale (`:39-41`) is the displaced element.** It enumerates three and will govern five; it also asserts *"this rule block is load-bearing **before** the stage table, not after it"* — still true. Requirement present in SC3, unassertable (**F/9**).
3. **The block grows 3→5 rules, pushing `## Inputs` (`:43`) further from the top.** `## Inputs` governs config validation (*"Validate every path a cold agent will be handed"*, `:51-52`) — and `S-CTX-vacuous` (`1.5:65`) adds *"an absent or empty `redteam_context` is a config error that stops the run"* at `S`. That stop-the-run rule now sits **after five rules instead of three**, in a file whose own thesis is that the read-first block is position-load-bearing. Low impact (it is a hard stop, not a judgment call) — **nitpick, not raised as a finding.**
4. **PRV: a disclaimer promoted into the authority slot** — **F/20**.
5. **The thesis paragraph `SKILL.md:8-13` takes three hedges at once** — **F/21**.
6. **The frontmatter `description` (`:3`) — the only trigger surface — is rewritten under criteria that measure strings, not triggering** — **F/14**. Position-specific: `S:3` is simultaneously a PRV overclaim site (`B7:31`) and a TOP-"ONLY" site (`B7:61`), so **two** independent rewrites land in one ≤1024-char field whose opening clause is its strongest hook.
7. **`SKILL.md:103-104`'s rule-ID list — an element that does not change and becomes wrong by omission** — **F/15**. This is the position lens's "a removal changes a neighbour's adjacency" case inverted: nothing moves, but the list's *scope relative to the corpus it governs* silently shrinks from 14/14 to 14/26.
8. **Rule renumbering:** GBP goes from rule 3 to rule 5. I grepped `SKILL.md METHODOLOGY.md stages/` for ordinal cross-references (`rule 1|rule 2|rule 3|rules 1`) — **zero hits**; every cross-reference is by mnemonic ID. **No finding.**

---

## 5. Concurrency lens — my own accessor enumeration

Per surface: **W** = writer, **R** = reader. Bold = accessor the plan's §4 does not enumerate.

| Surface | Writers | Readers | Guard claimed | Scope gap |
|---|---|---|---|---|
| `~/.claude/architect/templates/` (cross-project git) | stage 1 seed (first run); run-end commit (top orch. only) | **stage 1 template-match at every node, siblings in parallel**; **a concurrent run in another project** | the `mkdir` lock, "five paths" | **F/12** — pid liveness undefined for an agent holder; reader-lock branch converts sibling contention into HALT |
| **`<run-root>/catalog-pending/`** | **every decomposing node's owner at stage 6 (parallel siblings)** | top orch. at run end | none — outside the catalog | **F/11** — N writers, no guard, no collision rule, absent from §1/§4 |
| `plan/index.md` | top orch. (regeneration) | any resume; stage 8 restart | "one writer" | **F/13** — read-during-write of `<node>/plan.md`; no trigger; quiescence needs deferred F1 |
| `tree/root/_status.md` (+ per-node) | **none named — deferred to cycle 3** | apex roll-up; ECON lean surface; stage 7 | "one writer" | **F/10** — a "one writer" claim over zero writers with live readers |
| `<node>/decisions.md` | node owner (stage 5 gate + SPV sample + BIND rebind) | stage 5, stage 7 (cross-node) | "one writer" | **F/16** — stage 6 **back-propagate hole-fixes** has the parent acting in the child's node; no §1 row |
| `plan/decisions.md` | top orch. only (run-level) | CAP counter at stage 5 | "one writer" | **CAP reads it at every node's gate while the top orch. appends run-level events** — append-only + single writer makes this benign; the append-then-read ordering in §1 row 3 is sound. **No finding.** |
| `<node>/plan.md` | stage 2 (sole writer) | stages 3,4,5,6,7; BIND left operand; DEC's `elc(parent)`; index regeneration | single writer | **DEC reads the *parent's* `plan.md` while the parent may be re-drafting after its own bounce.** §1 row 15 asserts the parent's was *"written … **before this node existed**"* — true at first pass, **false after a parent re-draft**, and BIND's rebind chain covers the *record*, not `elc`. Folded into F/16's class; flagged here as the sharper instance. |
| `<node>/completeness/`, `adversarial/` | the 3 dispatched agents (parallel, distinct filenames) | stage 5, stage 7 | deterministic filenames | `S-BIND-stale-exit` (`1.5:51`) has a re-run **overwrite** the file while stage 7 may be reading it during assembly. Single-writer-per-file holds; torn read possible but the reader re-derives from `sha256`. **No finding.** |
| `plan/topgate/` + `APPROVAL.md` | stage 1 (pre-creates dir — F5, deferred); the approval's author | stage 6 | none | Deferred + **stated** at the site (`1.5:55`). **No finding.** |
| **`plan/assembly-approval.md`** (new) | top orch. after the presentable artifact exists | the terminus; **stage 8 restart, as the run-complete marker** | one writer | The bypass `1.5:94` guards against is **relocated, not removed**: existence is now the marker, and the content's authenticity is unenforced ⇒ a fabricated or crash-partial approval reads as "run complete" on restart. Folded into **F/2**. |
| `tree/root/plan.md.ingested` | stage 1 (immutable copy) | stages 2, 3 | immutable | §1 row 17 is sound, incl. the `fresh`-mode absence. **No finding.** |
| **two runs, one `run_root`** | every accessor above, doubled | " | *declared* unsupported (`1.5:78`) | **Declared but undetected** — no run lock, no pid file, nothing notices. The proven fix is one field away: this cycle builds a `mkdir`-based lock with a stale-holder rule for the catalog and does not apply it to `run_root`. Under R4 that is under-generalization. Folded into **F/12**. |
| live skill copy `~/.claude/skills/architect/` | build-time re-sync | every invocation | SC4 `diff -rq` | A concurrent invocation of the skill mid-sync reads a half-synced tree. Out of the run's own concurrency model; **nitpick, not raised.** |

**Verdict on the plan's central claim.** *"For `index.md`, `_status.md` and the gate logs the guard is **not a lock**: the accessor set is reduced to **one writer**, so there is no scope gap"* (`2-plan.md:196`) — **holds for `plan/decisions.md` and `<node>/plan.md`; fails for `_status.md` (F/10), is incomplete for `index.md` (F/13), and is contradicted for `<node>/decisions.md` (F/16)**. And the enumeration misses one whole surface (`catalog-pending/`, F/11). A single-writer reduction is a real technique; it was applied to the write side and the read side was not audited.

---

## 6. Pass-1 fidelity closure

| Finding | Closed? | Evidence |
|---|---|---|
| **A/F1** (position: rationale half of a confirmed-closed fix deleted) | **Partially** | Order half **closed** — `1.5:129` restores `GBP last`, verified against `SKILL.md:17-41`. Rationale half: the *requirement* is restored at `1.5:131-132` but only as SC3 prose, with **no pinned string and no M**, so A/F1's own *"No criterion catches it"* still applies → **F/9**. A/F1's second instruction (*"add it to D16's site list"*) is not done — `2-plan.md:156-162` (D16) lists no site for the rationale. |
| **A/F4** (PRV "strictly subtractive" was false) | **Closed on the subtractive half; the positive half ships with a partial limitation** | `1-spec.md:131-156` is a model correction: the false rationale is named *"That was false"*, the split is explicit, the never-closed status is carried, `OFL` is separately confirmed subtractive, and `LOOP-STATE.md:15`'s *"Interpretation … stated so Roy can correct it"* hedge is restored (verified verbatim). Residual: the "every site" duty rests on an unmeasured 3-site set → **F/8**. |
| **A/F5** (undeclared layout departure) | **Closed for the two named; the class recurs** | `2-plan.md:144-147` (D13) declares both, explicitly crediting A/F5. **Third departure undeclared** — `index.md`'s approved content/authority contract → **F/5**. |
| **A/F6** (charter fork-provenance falsified) | **Not closed** | `2-plan.md:168-170` + `1.5:104` record **additions only**, and re-frame D7's *reassignment* of the spot-verify duty as an addition. A/F6 asked for *"every local modification"*. Upstream `Guarded_change/stages/charter.md:59` (*"Whoever consumes the review checks"*) is deleted corpus-wide by `1.5:69`'s paired absence, so *"DROPPED: nothing from the core"* (`Architect/stages/charter.md:22`) becomes false, and `1.5:104`'s paired absence self-contradicts → **F/6**. |
| *(also, unrequested but in-frame)* **A/F10** (SC3 is a P row with no M) | **Not closed** | `1.5:24` *"mandatory for every P/P-PROXY row"* vs `1.5:128` *"SC3 · gating · P + X2"*. |
| *(also)* **A/F12** (unmarked truncation in R1's quote) | **Not closed** | `1-spec.md:110-112` still ends at *"defer to a later cycle."* → **F/18**. |

---

## 7. Coverage challenge (CH8)

Behaviours this change can alter that **no criterion observes**:

1. **Trigger-rate regression from the description rewrite.** SC1/SC2 pass on any string containing four tokens under 1024 chars. *Scenario:* the softened description loses its imperative framing; the skill stops being suggested for planning work; the entire loop never runs. **Severity: major** (F/14).
2. **PRV read as an exemption inside the read-first block.** X2 checks only that GBP fires. *Scenario:* an agent cites PRV's *"does not certify absence"* to justify presenting a plan with one un-gated node — the `class (i)` failure mode transplanted from the plan into the shipped artifact. **Severity: major** (F/20).
3. **The stale `SKILL.md:103-104` self-check list.** *Scenario:* the next editor's consistency sweep covers 14 of 26 IDs; HG2 diverges between `s7` and `s8` and nothing catches it. **Severity: major** (F/15).
4. **`catalog-pending/` name collisions between parallel siblings.** *Scenario:* two sibling nodes stage same-named proposals; one is lost silently before the reviewed run-end commit. **Severity: major** (F/11).
5. **Back-propagation writing into a child's node.** *Scenario:* a parent's hole-fix leaves the child's `decisions.md` without a rebind entry, so a stale record reads as current. **Severity: major** (F/16).
6. **`DEC`'s `elc(parent)` read after a parent re-draft.** §1 row 15's *"written before this node existed"* justification lapses; BIND covers records, not `elc`. *Scenario:* the parent's bounce halves its `elc`; the child's DEC comparison silently uses the new value and the convergence guard mis-fires or fails to fire. **Severity: minor-major** (§5).
7. **`_status.md` readers with no writer.** *Scenario:* the apex roll-up reads an absent file; no degenerate-case row defines the behaviour. **Severity: major** (F/10).
8. **`index.md` regenerated mid-run.** *Scenario:* a resume reads an index generated during an active walk; a node exists on disk with no `plan.md` and is recorded as not-planned. **Severity: major** (F/13).
9. **A lock broken while its holder is alive.** *Scenario:* per F/12 — two runs mutate the shared cross-project git catalog concurrently. **Severity: major** (F/12).

Not raised: I found **no** criterion or plan row that pre-shapes F1, F2, F5's mechanism, F6, DIV, the cost envelope, ECON's O(children²), the "two passes" ruling, or **R5's step 4** (the class-sweep rule into Architect). Deferral discipline on the out-of-scope set is **clean** — that is a genuine earned all-clear, and it is the strongest thing in this pass alongside R2's ratification record and the `S-BIND-f5-limit` / `S-CNC-uncov` honest-limitation rows.

---

## 8. Ranked list

1. **F/1 · BLOCKER** — "measured" site sets contradict the measurement (4 gating rows + §4's transposed accessor counts); falsifies the pass's central R4 claim and reproduces the half-migration class.
2. **F/2 · BLOCKER** — HG2's *"never self-approved"* unqualified at S and s8 vs the spec's "stated at the site"; the discriminator this cycle proved is named, not required.
3. **F/3 · MAJOR** — R4's record fails RAT1: no options, wrong axis, agent-authored source, while §2 claims all four are harness-sourced.
4. **F/4 · MAJOR** — RAT2 inflation: sweep-completion criterion + (a)/(b)/(c) + "no mutation may be class (i)" filed as Owner-ratified.
5. **F/5 · MAJOR** — third undeclared layout departure (`index.md`'s content/authority contract).
6. **F/6 · MAJOR** — A/F6 not closed: charter blockquote records additions only; a narrowing is framed as an addition; `1.5:104` self-contradicts.
7. **F/7 · MAJOR** — `off_limits_paths` asserted as both "a fence" and "not an enforced fence" at M and ex/planning.
8. **F/8 · MAJOR** — PRV's positive half: "every site" duty over an unmeasured 3-site set that excludes the description.
9. **F/9 · MAJOR** — SC3 guards two position majors with no pinned string and no mutation test.
10. **F/10 · MAJOR** — "one writer" claimed for `_status.md`, whose writer is deferred.
11. **F/11 · MAJOR** — `catalog-pending/`: N parallel writers, no guard, absent from the enumeration.
12. **F/12 · MAJOR** — the lock's pid liveness discriminator is undefined for an agent holder; reader-lock HALTs on sibling contention; `run_root` gets no equivalent guard.
13. **F/13 · MAJOR** — `index.md`'s single-writer guard leaves read-during-write open, with no quiescence trigger (needs deferred F1).
14. **F/14 · MAJOR** — "must still trigger … measured" pinned to string proxies; the risk row mislabels them.
15. **F/15 · MAJOR** — `SKILL.md:103-104`'s rule-ID list is a stale closed list governing the standing self-check.
16. **F/16 · MAJOR** — `<node>/decisions.md`'s single-writer rule contradicted by stage-6 back-propagation; no sweep row.
17. **F/17 · MAJOR** — "a clean run terminating and presenting IS now observed" is an agent verdict on a fixture.
18. **F/18 · MINOR** — A/F12 open: R1's quote still truncated without a marker.
19. **F/19 · MINOR** — R5 omitted though owner-ratified in the same source and it defines this pass's success.
20. **F/20 · MINOR** — PRV as a disclaimer in the read-first block; no arm tests PRV-as-exemption.
21. **F/21 · MINOR** — the thesis paragraph `S:8` absorbs three hedges with no preservation assertion.

**WORST SEVERITY: blocker**

---

## 9. Provenance

**Agent type + model:** general-purpose subagent · `claude-opus-5`. **spawn_id: unavailable.**
**Reviewer input was a closed set** — the artifacts + the context set named in my charter. No supplementary author-authored context was used; every quote above is from a file or transcript record I read directly.

| Path read | sha256 |
|---|---|
| `WT/Architect/changes/hardening-cycle-2/1-spec.md` | `f73326c07af9cc884ccd3ed222ca7017f005cfd31d9d5bfad2ce371f10c6c943` |
| `WT/Architect/changes/hardening-cycle-2/1.5-criteria.md` | `d3b9d1cfd62249d95a2c954201771a44679cb66b41b2103877827672279217d3` |
| `WT/Architect/changes/hardening-cycle-2/2-plan.md` | `b5628634e2a798caabeb046589ff0a189109fecf0842867202cde0e9ca50805e` |
| `WT/Architect/changes/hardening-cycle-2/0-baseline.md` | `251b008fd1e086fdad8c8374555b3e1b483860f325e71e6d85af5942b6673d10` |
| `WT/Architect/changes/hardening-cycle-2/0-baseline.B7-measured-sites.md` | `0b8da5013bd624f17d76839cd541556e8c0349900021c0388721039b7a3691a9` |
| `WT/Architect/changes/hardening-cycle-2/3-redteam-plan.A.verbatim.md` | `453326ec2704e7d8fb1c776eb5bd58b2184bd94886869fad28ce840916b07940` |
| `WT/Architect/SKILL.md` | `7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450` |
| `WT/Architect/METHODOLOGY.md` | `f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa` |
| `WT/Architect/README.md` | `79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a` |
| `WT/Architect/stages/charter.md` | `6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819` |
| `WT/Architect/guarded-change.architect.md` | `bd8d74936e88603ed0e4b67c1546a27325b84d85cda121b4cb0af9f84fa0f678` |
| `WT/Guarded_change/stages/charter.md` | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` (= the hash cited at `Architect/stages/charter.md:12`, and identical to `git show 8d73e5d:` — **fork-provenance hash verified**) |
| `WT/Guarded_change/stages/stage-3.md` | `16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3` |
| `WT/Guarded_change/stages/stage-1.5.md` | `c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b` |
| `/home/zero/architect-hardening-loop/LOOP-STATE.md` | `b0b737e3d32eec32fdf7de859544f4097f61b27b3f3a2ce174c21ec425bd0aac` |
| `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md` | `94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8` |
| `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` | `aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249` |
| the transcript JSONL (**live file — hash drifts**) | `a8f1058164600d51c072c2cfed05c7a3a577e5bea54915696b5374d3e0e0299b` at read time; **840 records**. Records 693-700 and 780-793 are immutable prior lines and were extracted at that state. |

Also read (via targeted grep, not in full): `WT/Architect/stages/stage-{1,3,4,5,6,7,8}-*.md`, `WT/Architect/examples/authoring-a-skill/README.md`.

**Flagged unverifiable:** (a) whether the four `index.md` files named in `1.5:71` and the two `S:77/S:86` sites in `1.5:95` are deliberate hand-additions or transcription errors — the artifacts state neither; (b) `1.5:172`'s *"The model used for all arms is stated in `8-harness.md`"* — that file does not yet exist, so held-constant-agent compliance cannot be checked pre-build; (c) whether `S-PRV-limit`'s "every site carrying the positive claim" set is complete — no measurement exists to check it against.
agentId: a73d5bffaba530ddc (use SendMessage with to: 'a73d5bffaba530ddc', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 177937
tool_uses: 23
duration_ms: 862775</usage>
