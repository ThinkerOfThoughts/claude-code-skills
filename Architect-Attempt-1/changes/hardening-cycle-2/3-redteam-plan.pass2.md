# Stage 3 — red-team of the plan, **PASS 2**: ranked cross-arm synthesis

Verbatim records: `3-redteam-plan.{D,E,F}.verbatim.md`. Pass 1's synthesis: `3-redteam-plan.md`.
Author's routing interpretation: `decisions.md`.

**Reviewers:** 3 cold, separately-spawned, **fresh frames disjoint from pass 1's** —
**D** sweep-completeness/generalization · **E** oracle+criteria validity (round 2) · **F**
fidelity/honesty + both conditional lenses. `general-purpose` / `claude-opus-5`. Dispatcher-recorded
handles: D `toolu_0166q5iyNUzxBKgiBfoSyXR7`, **E `a92c8332dc1a4f729`**, F `toolu_01PAYzB1UB2hCQ7W94QMHgm6`.
All three self-reported `spawn_id: unavailable` and declined to invent one.

**Worst severity per arm: D BLOCKER · E BLOCKER · F BLOCKER. Gate-4 worst finding: BLOCKER.**
**9 blockers, ~35 majors.**

---

## CH6 — citation spot-verify, PERFORMED BEFORE ROUTING

| Claim | Result |
|---|---|
| **E/1** `ruleid-sitemap.sh:34` is *still* `exit 0`, and `expected-sites.txt` / `check.sh` / `baseline-replay.sh` / `lockrace.sh` **do not exist** | **CONFIRMED** — `grep -n '^exit'` → `34:exit 0`; all four files ABSENT |
| **E/2** `idcollide.sh:31`'s `GRAND` list still pre-blesses `TOP TOPGATE` and `DEC DECOMPOSITION` | **CONFIRMED** — the line is byte-unchanged |
| **E/3** `1.5-criteria.md` §5 declares **3 clusters / 12 spawns**; `fixtures/README.md` says *"Four clusters"* and `fixtures/X4/` exists | **CONFIRMED** |
| **E/6 ∥ F/1** row 24 claims *"all 9 measured `index.md` files"*; B7 measured **5** (`METHODOLOGY`, `s1`, `s6`, `s8`, `tp/README`) | **CONFIRMED** — `S`, `s7`, `ch`, `ex/README` are invented sites |
| **E/12** `0-baseline.md:99` still says *"across 5 files"* | **CONFIRMED — and now corrected in place to 4** (see `decisions.md`) |
| **E/9** `SKILL.md:18-19`'s §4 heading is genuinely **wrapped mid-phrase**, and B7 under-measured it | **CONFIRMED** — B7's P18 omits `SKILL.md` entirely |
| **D/2** §1's sweep is not total | **CONFIRMED, AND WORSE THAN D CLAIMED.** D said 12 of 21 baseline IDs have no row; measured: **15** — `PASS1 PASS2 CMP CMP2 SPN COV ORC ECON TPL TPL1 TPL2 TPL3 RST RAT3 SEV` |

**No fabricated citation. Every sampled claim held, one of them more strongly than the reviewer stated.
The severities are earned and they route.**

---

## The one finding that explains most of the others

**Pass 2's `1.5-criteria.md` §0 describes stage-5 work in the PRESENT TENSE as already done.** It says
*"It **is now** a checker: reads `expected-sites.txt`, reports MISSING / UNEXPECTED, **exits 1**"* and
*"`TOPGATE` and `DECOMPOSITION` **are REMOVED** from the grandfather list"*. **Neither is true.** The
scripts were never written; the `GRAND` line was never edited.

That is not a design defect — it is **the author certifying its own unbuilt work**, which is CP1, the exact
failure this loop exists to prevent, committed inside the document whose job is to prevent it. Reviewer E
found it by **running** the oracles rather than reading the claim, which is precisely why the frame exists.
Four of pass 2's nine blockers (E/1, E/2, E/3, E/4) reduce to it, and D/7 is the same defect in the X
protocol (*"the fix for C/O4 was made in prose only"*).

**Second-order, and the reason the cap trips rather than bounces:** pass 1's class-β blockers were *"the
apparatus cannot detect a bad build."* Pass 2's are *"the apparatus still cannot, and the document says it
can."* Same gate, same section, same defect kind — with an added false claim.

---

## Blockers

| # | ID | Claim | Cite |
|---|---|---|---|
| 1 | **E/1** | `ruleid-sitemap.sh` is byte-for-byte pass 1's printer; `expected-sites.txt`, `check.sh`, `baseline-replay.sh` absent. All four promised mutations reproduce at **exit 0**; deleting every `GBP` token from `stage-5-gate.md` exits 0; deleting the operative sentence while keeping `<!-- see GBP -->` gives **byte-identical output**. **C/O1 + C/O2 claimed closed, entirely open.** | `oracles/ruleid-sitemap.sh:34`; `1.5:13` |
| 2 | **E/2** | `idcollide.sh:31` still grandfathers `TOP TOPGATE`; reviewer added `TOPGATE` as a live token → `grandfathered`, **exit 0**. This cycle *introduces* `plan/topgate/`, so R3 cannot fire on its own most likely collision. | `oracles/idcollide.sh:31`; `1.5:119` |
| 3 | **E/3** | §5's cluster map (3 clusters/12 spawns) contradicts `fixtures/` (4 clusters, X4 on disk). Four gating rows (16, 18, 38, 39) cite an **unscheduled** arm; and on-disk X3's deliberately inverted polarity **auto-fails** §5's blanket pass rule. | `1.5:178-179` vs `fixtures/README.md:3` |
| 4 | **E/4** | `lockrace.sh` absent, and **two of its four promised outcomes are false — E executed them**: a `SIGKILL`ed holder **leaks the lock** (a trap does not run on SIGKILL, and a HARDSTOP *is* a kill), and the H4 unguarded control **passes without the lock** (8×200 concurrent `>>` appends → 1600 lines, zero loss, because sub-`PIPE_BUF` appends are atomic). | `2-plan.md:184`; `1.5:163-166` |
| 5 | **D/1** | **The closed-input-set predicate is absent from the sweep**, and its three operands are unproducible in the degenerate cases the sweep claims to cover: the **parent plan** (absent at the root, always), **child seams** (absent at a leaf, always), and **carried-forward findings in `<node>/decisions.md`** — whose first writer is **stage 5**, i.e. *after* stages 3/4 read it. The charter makes a record missing any closed-set member **un-run**. Row 17 applies the exact fix to `plan.md.ingested` and nowhere else. | `charter.md:96-99`; `s3:62-64`; `2-plan.md:52` |
| 6 | **D/2** | §1 is **not total** — the claim *"every predicate and gate, baseline rules included"* is false. **15 of 21 baseline IDs have no row** (measured), incl. `COV`, `RST`, `RAT3`, `SPN`, `TPL3`. The sweep's own provenance claim is false. | measured |
| 7 | **D/3** | **`COV` is an assembly precondition whose operand has no producer anywhere on disk**, and the sweep has no row to notice it. | `s7:28-31` |
| 8 | **D/6** | **Restart with the presentable artifact present and the approval absent has no resume step.** RST's stage-done-iff-output-exists marks stage 7 done, so HG2's ask never re-fires. B/L4's fix was applied at one site and not generalized. | `s8:13-15`; `2-plan.md` row 23 |
| 9 | **F/1** | **The "measured" site sets are not the measurement.** Four gating criteria and §4 contradict `0-baseline.B7-measured-sites.md`, the file they cite as their authority: row 24 invents 4 files; row 26 drops the measured `s7` and adds an unmeasured `s8`; row 48 labels "7" and lists 9; row 52 labels "10" and lists 14 (and `1-spec.md` says *six*). **This reproduces the exact half-migration defect R4 was invoked to fix.** | `1.5:71,73,95,99` vs `B7:57-106` |

## The majors, grouped

- **Class α recurring in newly-swept sections** (D/5 the lock's pid is a *second* step after `mkdir`, and a
  kill between them leaves a state neither stale-branch defines; D/18 *"run end" is not a stage*, so rows 18
  and 19 cannot answer (a) at all — and with HG2 the run end now sits behind a human answer that may never
  come; D/8 row 15's (a) and (b) contradict each other on `elc`; D/16 two (b) answers are false against
  source).
- **(b) answers that are unenforceable** (D/4): roughly half of §1's degenerate-case answers end in the word
  *"stated"*, and **no criterion pins any of those sentences** — so the column the whole sweep rests on is
  invisible to the build.
- **Proven fixes applied at one site only — R4's own violation** (D/9 A/F3's fix routed `template used` and
  nothing else, leaving the granularity decision and `index.md`'s `status` stranded; D/10 B/L6's
  dispatcher-recorded fix applied to `plan_sha256` but **not to the rebind chain**, which can therefore
  revalidate any record with the constrained party's own signature).
- **New shared surfaces the enumeration misses** (D/12 ∥ F/11: `<run-root>/catalog-pending/` is a new
  load-bearing surface with N concurrent writers, no naming scheme, no guard, and no place in the restart
  contract — while §4 claims the enumeration is now complete; F/10 `_status.md`'s writer is **deferred to
  cycle 3**, so *"reduced to one writer"* is false for it; F/13 `index.md`'s one-writer rule closes the
  write-write race and leaves **read-during-write** open, and the quiescence trigger it needs is deferred F1).
- **Honesty regressions** (F/2 **blocker-adjacent**: HG2's *"never self-approved"* ships **unqualified at 2
  of its 4 sites**, contradicting the spec's own gating requirement that the limitation be stated; F/7 the
  `off_limits_paths` overclaim is deleted by row 19 and **reintroduced** by row 17 at two shared sites; F/8
  PRV's never-closed positive half ships under an *"every site"* duty whose site set is **the only one in the
  file never measured**; F/17 *"a clean run terminating IS now observed"* is **declared** — what is observed
  is a cold agent's verdict on a fixture).
- **Ratification fidelity** (F/3 **R4's record fails the RAT1 bar R1–R3 meet**: it quotes **no options**,
  records an axis that was never presented, and cites an **agent-authored** file as its source, while §2's
  header asserts all four are verified against a harness-authored source; F/4 three operative commitments in
  §1.2 — the three-question checklist, *"no mutation may be labelled class (i)"*, *"not done until every site
  is swept"* — are **not entailed** by the owner's sentence and are therefore **unratified inflation**).
- **Position/trigger** (F/9 SC3 is the sole guard for two pass-1 position majors and is the **one row with
  neither a pinned string nor a mutation test**, violating the file's own absolute rule; D/13 PRV's and XPM's
  measured sites fall outside the block row 25 reasons about; F/14 *"the skill must still trigger"* is pinned
  to two **string proxies** and the risk table mislabels them as measuring triggering; F/15 `SKILL.md:103-104`'s
  mnemonic-ID list is a **stale closed list** governing the standing self-check and no criterion updates it).
- **Arithmetic that cannot be satisfied** (E/11): SC1's measured 1024-char cap vs rows 20 + 48 both making
  `SKILL.md:3` mandatory — 954 + 76 + 180 = 1210. Two gating criteria are jointly satisfiable only via an
  unstated third choice.
- **Config item (6) half-implemented** (E/13): the *"every preserved-rule assertion MUST PASS"* half is
  absent, §1 has **no PRESERVE rows at all**, and the whole preserve direction devolves onto R1 — whose
  oracle cannot fail. **Net: nothing checks site-set non-erosion.**
- **E/5** a normalized-substring presence test has **no polarity guard**, so all 54 string rows are
  satisfiable by the sentence quoted as a *foil* (*"What pass 1 wrongly said: …"*). **E/14** row 15's pinned
  string is **circular** — 13 pastes satisfy it with RES undefined. **E/10** rows 16/57 still *describe*.
  **E/15/E/16** fixture give-aways: X4's holed arm **has no `tree/` at all** (blocking verdict
  over-determined) and X3's holed record **transcribes its own verdict** (`Pass status: DECLARED DEGRADED`).
- **The X protocol's variance claim is unsound** (E, in-frame): *"0.25 → 0.0625"* assumes four
  **independent** Bernoulli trials, but holding the agent constant is exactly what makes the two spawns per
  arm **maximally correlated**. The protocol may claim the confound is removed; it may not also claim the
  variance reduction.

---

## What pass 2 genuinely EARNED (credited by the reviewers who tried to break it)

| Item | Evidence |
|---|---|
| **The corpus pin — pass 2's one solidly earned fix** | E implemented `normalize()` and ran **all 57 rows against the materialised baseline: 0 of 54 string rows wrongly pass.** `changes/` genuinely cannot enter. **C/O3 CLOSED.** |
| **Paired-absence polarity** | All 22 absence strings that should be present-at-baseline are; all four that must never exist are absent. **The absence half of the replay is a real can-fail test.** |
| **X1's fixture is hash-real** | E recomputed `sha256sum` and matched the recorded value exactly; holed carries `0000…`; the intact root record carries only its own hash — **the no-parent carve-out is genuine**. |
| **X2's arm** | Sole diff between arms is `assembly-approval.md` — the rule under test. *"Best of the four."* |
| **SC5's upgrade** | Judge + scale + pass definition + recorded artifact all present — **C/O12 closed.** |
| **The phantom triage** | Exactly right, and the oracle reports its exclusions. |
| **Baseline counts** | E independently re-verified **9 of 12**: 21 IDs vs 18 rows ✔ · the phantom set ✔ · `TOP` not a `stage-8` site ✔ · 8 overclaims in **4** files ✔ · 13 `clean-or-resolved` sites ✔ · B7's 7 "top-level ONLY" ✔ · `SKILL.md:18-19` genuinely wrapped ✔. |
| **Label audit** | No advisory-relabel dodge anywhere; the *"declared deferral"* route is genuinely absent and HALT+relay is correctly named the only remaining move. |
| **BIND's §1.4 narrowing** | Dropping the parent clause removed the subtree-invalidation cascade *and* the root special case — endorsed rather than contested. |

---

## The pattern, named for whoever picks this up

1. **The author certified its own unbuilt work.** Every one of E/1–E/4 exists because a *plan* was written
   in the **present tense**. The mechanical fix is trivial (write the four scripts); the discipline fix is
   that a criteria document may only describe instruments that **exist and have been mutation-tested**, and
   the instruments must therefore be built **before** stage 3, not after — which is what stage 0 already did
   for the two oracles that *do* exist and *do* discriminate.
2. **A site list retyped is a site list unmeasured.** Five rows were hand-copied from a measurement file
   sitting one directory away. **Generate the SITES column from B7 mechanically** and E/6–E/9 + F/1
   disappear for free — reviewer E says so explicitly.
3. **A sweep that names its own totality must be generated, not authored.** 15 of 21 baseline IDs were
   missing from a table whose headline claim is totality. Generate the row set from the ID index.
4. **R4 was applied to the four blockers and not to their class.** D/9 and D/10 are R4 violations *inside
   the pass that R4 authorized* — the proven fix was applied to the named instance and not swept.
5. **A ratification record must meet its own bar.** R1–R3 cite a harness-authored transcript with record
   numbers; **R4 cites a file the assistant wrote and quotes no options.** The fix is to record R4 the way
   R1–R3 were recorded, or to narrow §1.2 back to the owner's sentence.
