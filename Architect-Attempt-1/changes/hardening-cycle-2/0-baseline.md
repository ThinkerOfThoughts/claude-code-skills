# Stage 0 — Baseline (hardening cycle 2)

**NOT greenfield.** The Layer-2 config (`guarded-change.architect.md`, "Run 2+") makes a stage-0 baseline
**REQUIRED** and **textual**: the artifact is a prompt assembly, so the baseline is *the current committed
behaviour of the rules being touched*, not a metric run.

**Base commit: `b08f5a9`** (`git rev-parse HEAD` = `b08f5a914b38b6d02549b6feae09cbd3e53ad160`), worktree
clean at run start. Verified: `git diff --stat b08f5a9 3771038 -- Architect/` touches **only**
`changes/` + `guarded-change.architect.md` — so the **artifact content** (`SKILL.md`, `METHODOLOGY.md`,
`README.md`, `stages/`, `templates/`, `examples/`) at `b08f5a9` is **identical to `3771038`**, the base
cycle 1 measured. Cycle 1's baseline record is therefore reusable, and is **re-verified** below rather
than inherited on trust.

`~` = `<WT>/Architect/` where `<WT>` =
`/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`.

---

## B1 — Frozen baseline tree (mechanically recoverable; no prose copy)

```
git -C <WT> show b08f5a9:Architect/<file>       # any baseline file
git -C <WT> diff b08f5a9 -- Architect/          # this change's own diff (stage 6 uses this)
```
Recorded base for the stage-6 mechanical diff: **`b08f5a9`**.

## B2 — Baseline rule-ID site map (word-boundary, phantom-triaged, MECHANICALLY RE-CAPTURED)

Captured by `changes/hardening-cycle-2/oracles/ruleid-sitemap.sh .` at `b08f5a9` (word boundaries are
**mandatory** per the Layer-2 config; the phantom-exclusion list is applied and its exclusions are
**reported**, not dropped).

| ID | Baseline site set |
|---|---|
| **GBP** | METHODOLOGY, SKILL, charter, stages 2,3,4,5,7,8 |
| **PASS1** | METHODOLOGY, SKILL, stage 3 |
| **PASS2** | METHODOLOGY, SKILL, stage 4 |
| **PASS-ORD** | METHODOLOGY, SKILL, stages 3,4,5 |
| **CMP** | METHODOLOGY, SKILL, stage 3 |
| **CMP2** | METHODOLOGY, SKILL, stage 3 |
| **SPN** | METHODOLOGY, SKILL, stages 2,3, templates/seed/{decomposition-node,generic-node,README} |
| **COV** | METHODOLOGY, SKILL, charter, stages 2,3,4,6,7, templates/seed/decomposition-node |
| **ORC** | METHODOLOGY, SKILL, stage 6 |
| **ECON** | METHODOLOGY, SKILL, stages 6,8 |
| **GRN** | METHODOLOGY, SKILL, stages 2,4,6, templates/seed/{decomposition-node,leaf-task-spec} |
| **TOP** | METHODOLOGY, SKILL, stage 6, templates/seed/decomposition-node |
| **CAP** | METHODOLOGY, SKILL, charter, stage 5 |
| **DEC** | METHODOLOGY, SKILL, stage 6, templates/seed/decomposition-node |
| **TPL** | METHODOLOGY, SKILL, stage 1, templates/seed/README |
| **TPL1** | METHODOLOGY, stages 1,2, templates/seed/README |
| **TPL2** | METHODOLOGY, stages 1,6, templates/seed/README |
| **TPL3** | METHODOLOGY, SKILL, stages 1,6, templates/seed/README |
| **RST** | METHODOLOGY, SKILL, stages 1,2,6,7,8 |
| **RAT3** | METHODOLOGY, SKILL, charter, stages 3,5,6 |
| **SEV** | stages 4,5 |

**21 live IDs. METHODOLOGY's cross-file rule index has only 18 rows** — `TPL1`, `TPL2`, `SEV` are live
IDs with **no index row**. Baseline gap; this cycle closes it.

**Phantoms, reported (word boundaries do NOT remove these):**
- `TOP` @ `METHODOLOGY.md:79` and `examples/authoring-a-skill/planning.md:25` — the ordinary English
  phrase **`ON TOP OF`**. `grep -w -- TOP` matches both. Neither is a TOP rule site.
- `TOP` is **NOT** a `stages/stage-8-restart-resume.md` site: the only match there is inside
  **`HARDSTOP`**, which word boundaries *do* remove.
- **Correction to cycle 1's B0.2 caveat, retained here because it is the measurement lesson:** B0.2
  blamed `HARDSTOP` for the `generic-node`/`planning.md` hits and claimed word boundaries fixed it. Both
  halves were wrong — `HARDSTOP` is removed by word boundaries, and the surviving phantom class
  (`ON TOP OF`) is not. Cycle 1's B0.6 corrected this; **this cycle re-verified it mechanically** rather
  than inheriting the claim.

## B3 — The ID naming rule is VIOLATED at baseline (new finding, cycle 1 got this wrong)

`oracles/idcollide.sh .` at `b08f5a9`:
- **exempt-family** (intentional stems): `CMP < CMP2`, `TPL < TPL1/TPL2/TPL3`.
- **grandfathered baseline debt, now visible instead of hidden:** `DEC ⊂ DECOMPOSE / DECOMPOSES` and
  `TOP ⊂ HARDSTOP / TOP-LEVEL`. Both are pre-existing IDs; renaming them is **not in this cycle's
  scope**, so the oracle names them as declared debt.

**Cycle 1's B0.7 claim — *"run at baseline it flags nothing (the baseline IDs pass)"* — is FALSE.** The
baseline corpus violates the config's own ID rule at `DEC` and `TOP`. Recorded as a correction (cycle 1's
own records are not rewritten — see `decisions.md`).

**Can-fail self-test for this oracle:** run with cycle 1's rejected ids →
`COLLISION: KIL ⊂ SKILL`, `ING ⊂ PLANNING`, `ING ⊂ RULING`, exit 1. Run with cycle 2's proposed ids
(`BIND IDN RES CTX CNC DEP IGM PRV XPM HG2 SPV OFL KLB`) → OK, exit 0. **The oracle discriminates.**

## B4 — Baseline operative claim per rule this cycle touches

Citations are `file:line` at `b08f5a9`. "Intends" = PRESERVE or CHANGE (R2 checks every CHANGE row is
migrated at **every** site that stated the old claim).

| # | Rule / claim at baseline | Baseline operative text | This cycle intends |
|---|---|---|---|
| P1 | Review-record ↔ plan binding | charter `charter.md:96` already requires the reviewer-reported **sha256 of each context file**; **no stage compares them**. `stage-8:15` stage-done = output-**exists** only | **CHANGE** — add **BIND** (compare at stages 5 and 7; stage-done for a record adds BIND-current) |
| P2 | Spawn identity in a record | `charter.md:93-99` mandates 5 provenance fields; **no spawn identity**; nothing forbids reading a sibling record in the dir the agent is pointed at | **CHANGE** — add **IDN** (dispatcher-recorded `spawn_id`, declared-degraded value, sibling-read ban) |
| P3 | "clean-or-resolved" | `stage-5:16` "Clean-or-resolved on both passes"; "resolved" **undefined**; `stage-5:14` minor = "fix in place, proceed"; at `stage-7:10-13` a fixed-in-place node is **indistinguishable** from a clean one | **CHANGE** — add **RES** (three arms; `clean` / `clean-fixed-in-place` / `clean-demoted`) |
| P4 | `redteam_context` in the config contract | **zero occurrences** in `METHODOLOGY.md`; charter requires it (`charter.md:29,97`); stages 3/4 hand it to every cold agent (`stage-3:17`, `stage-4:14`); `examples/…/planning.md:38-40` mentions it only *inside* `off_limits_paths` | **CHANGE** — add **CTX** (first-class contract key + example key; de-conflated; absent ⇒ config error) |
| P5 | `off_limits_paths` enforcement claim | `METHODOLOGY.md:99-101` — *"Naming is the fence — no guard catches a stray write the config never declared."* Stated as the guarantee | **CHANGE (subtractive)** — **OFL**: state plainly it is a prompt-level convention, **not** an enforced fence |
| P6 | "completeness PROVEN" | `SKILL.md:3` frontmatter "PROVEN, not asserted"; `SKILL.md:8-9`, `SKILL.md:17`; `METHODOLOGY.md:3-5,40`; `README.md:10,12`; `stage-7:26` — **8 occurrences across 4 files** *(corrected 2026-07-25: the file set is SKILL.md, METHODOLOGY.md, README.md, stage-7 = FOUR. "5" was cycle 1's error, repeated by pass 1, filed by reviewers A/F7 ∥ C/O11 and again by E/12, and measured by three independent reviewers.)* | **CHANGE (subtractive)** — **PRV**: soften to what is proven; state that N same-model instances are not N independent minds |
| P7 | Spot-verify-citations duty | `charter.md:88-92` states the duty as *"whoever consumes the review"* — **assigned to no stage** | **CHANGE** — **SPV**: assigned to stage 5 (+ stage 7 for cross-node claims) |
| P8 | Serial vs parallel | **never stated** anywhere | **CHANGE** — **CNC** declares it |
| P9 | Shared write surfaces | `index.md` written by every owner (`stage-1:20`, `stage-6:11-12`, `METHODOLOGY.md:195`, `templates/seed/README.md:14`); `plan/decisions.md` appended by every owner (`stage-5:19`, `SKILL.md:61-62`); catalog `git commit` by any sub-orchestrator (`stage-6:32-35`). **Zero serialization.** `stage-8:16-17` asserts *"there is no single global cursor to stale-edit"* **while `index.md` is exactly one** | **CHANGE** — **CNC**: `index.md` **derived** (top orchestrator only); per-node gate log `<node>/decisions.md`; catalog lock; the false stage-8 claim corrected |
| P10 | DEC's operand | `METHODOLOGY.md:220-223` + `stage-6:27-31` "estimated leaf count / **work-size** ≥ 0.8× … **two consecutive levels**"; `decomposition-node.md:24-25` "a child ≥ 0.8× the parent trips the guard" (**single** level) → **2 operands, 2 trip conditions**, no persistence site | **CHANGE** — one operand **`elc`** (honestly *self-declared*), ONE trip condition (two levels) |
| P11 | exit-plan-mode terminus | GBP is *named after* it (`SKILL.md:33`, `METHODOLOGY.md:149`, `METHODOLOGY.md:316`); **no stage covers the terminus** | **CHANGE** — **XPM** names the terminus and its gates |
| P12 | Human gates | `METHODOLOGY.md:212-216` / `SKILL.md:77-78` / `stage-6:15-19,43-45` / `decomposition-node.md:27-28` — the human gate is the **top-level split ONLY**; `stage-7` is purely structural, **no human review of the assembled plan** | **CHANGE** — **HG2** (owner-ratified): a **second** human gate at assembly; TOP's "ONLY" narrowed to *decomposition* gates |
| P13 | `mode: ingest-and-complete` | **undefined** — absent from the config contract, `SKILL.md` Inputs, and every stage | **CHANGE** — **IGM** defines it |
| P14 | Seed-skeleton Layer-2 slots | `generic-node.md:32-33` has only an **italic note**, no slot heading; `decomposition-node.md` and `leaf-task-spec.md` have **nothing** — so **3 of 3** skeletons lack a slot and the catalog manufactures tier-(ii) holes | **CHANGE** — an explicit Layer-2 slot heading in **all three** |
| P15 | TPL3 catalog commit | `stage-6:32-35` + `templates/seed/README.md:20-23` — an **unreviewed** skeleton patch is `git commit`ed to a shared cross-project repo **inside the autonomous region** | **CHANGE** — stage-and-propose; one reviewed, locked, top-orchestrator commit at run end |
| P16 | Inter-leaf dependency order | leaves emitted with **no execution order**; `decomposition-node.md:19-22` seam table has **no dependency column** | **CHANGE** — **DEP** (child DAG, cycle = blocker, assembled execution-order section) |
| P17 | Root node location | `METHODOLOGY.md:265-267` shows `tree/_status.md` (apex roll-up) + `tree/<node>/`; the **root plan node's own dir is unpinned** | **CHANGE** — pin **`tree/root/`** (declared departure from the approved layout) |
| P18 | §4 heading string | **6 spellings**: `SKILL.md:18-19` "Outputs & artifacts WITH their locations"; `METHODOLOGY.md:121` "Outputs & artifacts — deliverables **and their locations**"; `METHODOLOGY.md:322` (index row); `stage-2:11-12` "Outputs & artifacts (with their locations, incl. …)"; `stage-3:43` "Outputs & artifacts **with locations**"; `generic-node.md:16` / `decomposition-node.md:10` "Outputs & artifacts (WITH their locations)"; `leaf-task-spec.md:13` "Outputs & their locations (§4)" | **CHANGE** — ONE canonical string, verbatim at every site |
| P19 | METHODOLOGY's "authoritative" ID grep | `METHODOLOGY.md:309-312` — `grep -rln -- <ID> SKILL.md METHODOLOGY.md stages/`: **no word boundaries**, and **`templates/` + `examples/` excluded** although both hold rule sites (see B2) | **CHANGE** — `grep -rlnow` over the full scope + the phantom caveat + the ID naming rule |
| P20 | Cross-file rule index completeness | 18 rows for 21 live IDs (B2) | **CHANGE** — rows for `TPL1`,`TPL2`,`SEV` + every new ID |

## B5 — Baseline live-copy state

`diff -rq /home/zero/.claude/skills/architect <WT>/Architect` at run start — recorded in `decisions.md`.
`live == source` must hold at baseline for the stage-8 self-check criterion to be non-vacuous.

## B6 — What "regression" means for this change

Prompt assembly ⇒ regression = **a baseline rule that stops being stated, or starts being stated
inconsistently, at a site the change did not intend to alter.** Two gating regression checks:

- **R1 — site-set non-erosion.** Every baseline ID in **B2** keeps at least its baseline site set. IDs may
  gain sites; losing one is a regression unless a criterion declares it.
- **R2 — deliberate-change completeness.** For each **CHANGE** row in **B4**, the new claim is stated at
  **every** site that stated the old claim — no half-migrated rule. (This is the §4-heading failure mode,
  generalised.)

Both are computed by `oracles/check.sh` and validated against the baseline tree by
`oracles/baseline-replay.sh` — a checker that passes against the baseline is **not an oracle**.
