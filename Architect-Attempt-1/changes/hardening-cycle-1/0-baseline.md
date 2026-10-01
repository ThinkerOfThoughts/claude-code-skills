# Stage 0 — Baseline (hardening cycle 1)

**This run is NOT greenfield.** The initial authoring run (`changes/initial-authoring-2026-07/`) was
greenfield and ran conformance-only. This run *modifies an existing artifact*, so a stage-0 baseline
exists and is required: the baseline is **the current committed behavior of the rules being touched**,
at `Architect @ 3771038` (`git rev-parse HEAD` = `3771038dd6e2bbf466f2e26e15e13a82d70116da`, worktree
clean at run start).

`~` below = `<WT>/Architect/` where `<WT>` =
`/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`.

## B0.1 — Frozen baseline tree

The baseline is recoverable mechanically, so no prose copy is needed:

```
git -C <WT> show 3771038:Architect/<file>          # any baseline file
git -C <WT> diff 3771038 -- Architect/             # the change's own diff (stage 6 uses this)
```

Recorded base for the stage-6 mechanical diff: **`3771038`**.

> ## ⚠ B0.2 IS SUPERSEDED BY **B0.6** — read B0.6, not B0.2
> The pass-1 capture below was **wrong in both directions** and was caught by all three stage-3
> reviewers (A/F1-1, B/F-1+F-2, C/F1-1 — 3/3 convergence). It is retained unedited as the record of what
> the gate caught. **The authoritative baseline site map for R1/R2 is B0.6.**

## B0.2 — Baseline rule-ID site map (SUPERSEDED — see B0.6)

Every rule stated in more than one file carries a mnemonic ID; the ID *is* the cross-file linking
mechanism, so the baseline that matters for behavior-preservation is **which files state which rule**.
Captured mechanically at run start (`grep -rlo -- <ID> SKILL.md METHODOLOGY.md stages/ templates/
examples/ README.md`):

| ID | Baseline site set (files stating it) |
|---|---|
| **GBP** | SKILL, METHODOLOGY, charter, stages 2,3,4,5,7,8 |
| **PASS1** | SKILL, METHODOLOGY, stage 3 |
| **PASS2** | SKILL, METHODOLOGY, stage 4 |
| **PASS-ORD** | SKILL, METHODOLOGY, stages 3,4,5 |
| **CMP** | SKILL, METHODOLOGY, stage 3 |
| **CMP2** | SKILL, METHODOLOGY, stage 3 |
| **SPN** | SKILL, METHODOLOGY, stages 2,3, templates/seed/{README,generic-node,decomposition-node} |
| **COV** | SKILL, METHODOLOGY, charter, stages 2,3,4,6,7, templates/seed/decomposition-node |
| **ORC** | SKILL, METHODOLOGY, stage 6 |
| **ECON** | SKILL, METHODOLOGY, stages 6,8 |
| **GRN** | SKILL, METHODOLOGY, stages 2,4,6, templates/seed/{decomposition-node,leaf-task-spec} |
| **TOP** | SKILL, METHODOLOGY, stages 6,8, templates/seed/decomposition-node, examples/…/planning |
| **CAP** | SKILL, METHODOLOGY, charter, stage 5 |
| **DEC** | SKILL, METHODOLOGY, stage 6, templates/seed/decomposition-node |
| **TPL** | SKILL, METHODOLOGY, stages 1,2,6, templates/seed/README |
| **TPL3** | SKILL, METHODOLOGY, stages 1,6, templates/seed/README |
| **RST** | SKILL, METHODOLOGY, stages 1,2,6,7,8 |
| **RAT3** | SKILL, METHODOLOGY, charter, stages 3,5,6 |

**Measurement caveat found while capturing the baseline (carries into the stage-8 oracle):** a bare
`grep -o -- TOP` matches inside **`HARDSTOP`** (…S-**TOP**), which is why the raw capture listed
`templates/seed/generic-node.md` and `examples/…/planning.md` as TOP sites. The stage-8 rule-ID
oracle **must use word-boundary matching** (`grep -now -- <ID>` / `\bID\b`); the two files above are
**not** baseline TOP sites. This is a live instance of ST1.5f's "a fragile matcher makes an absence
check silently wrong."

## B0.3 — Baseline behavior of each rule this change touches

Stated as the *operative claim at baseline*, so stage 8 can assert the change either preserved it or
changed it **deliberately and everywhere**. (Citations are `file:line` at `3771038`.)

| # | Rule / claim at baseline | Baseline text (operative) | Change intends |
|---|---|---|---|
| P1 | Fan-out terminus (stage 6) | `stage-6…:23-26` — parent spawns a sub-orchestrator per child; procedure ends at step 7. Nothing blocks, polls, joins, or learns of child death. | **Change**: add stage 6.5 join (JOIN) |
| P2 | `_status.md` | named 5× (`METHODOLOGY:236,267,270,280`; `stage-6:11`; `stage-8:9`) as the up-flow vehicle; **no schema, no writer named** | **Change**: define the schema + single-writer rule |
| P3 | Escalation channel | `stage-5:58` / `stage-6:66` RAT3 — "halts the runner and relays the question verbatim" over a channel no stage defines | **Change**: define it (`_status.md` `escalation:` + parent relay) |
| P4 | Assembly direction | `stage-7:14` — "**Collate top-down**", assembler unnamed; the walker holds the whole tree | **Change**: bottom-up, per-node, owner-named |
| P5 | Killed branch | `stage-5:44` offers "kill the branch" as a cap outcome; **no on-disk representation, no run-level abort**; `stage-7:10-13` demands every node gated and offers only "resume that node" | **Change**: `subtree: killed` + `_killed.md` + `plan/ABORTED.md` |
| P6 | Parent seam review | `stage-2:20-22` + `stage-4:37-39` — the parent reviews seams among *proposed* children at stage 2/4; **never reopened**; `stage-7` has **no** cross-node seam check | **Change**: SEAM (reopen + assembly-time check) |
| P7 | Review-record ↔ plan binding | charter provenance (`charter:96`) already requires reviewer-reported context-file sha256; **no stage compares them**; `stage-8:15` stage-done = output-**exists** only | **Change**: BIND (compare at 5, 6.5, 7) |
| P8 | `redteam_context` in the config contract | **zero occurrences** in `METHODOLOGY.md`; charter requires it (`charter:29,97`); stages 3/4 hand it to every agent; `examples/…/planning.md:40` mentions it only *inside* `off_limits_paths` | **Change**: add to contract + example as a first-class key |
| P9 | TOP predicate | stated **3 inconsistent ways**: `stage-1:11` creates `plan/topgate/` (empty) as setup; SKILL:77 / METHODOLOGY:215 "blocked until `plan/topgate/` exists"; `stage-6:17` "the approval artifact must exist on disk at `plan/topgate/`". **No filename, no authorship or content requirement.** | **Change**: one predicate, `APPROVAL.md`, owner-verbatim + durable source, no self-authored approval, cold audit |
| P10 | Completeness claim | frontmatter `SKILL.md:3` "completeness is PROVEN, not asserted"; `METHODOLOGY:3-5,41`; `README:10,12`; `stage-7:26` "completeness is **proven, not asserted**" | **Change**: soften to what is proven (PRV) |
| P11 | Reviewer independence | `charter:127-129` "3 independent cold agents" = 3 separately-spawned subagents, no shared context. **Diversity of frame: not required anywhere.** | **Change**: add DIV (3 distinct frames) |
| P12 | Review-record provenance | `charter:93-99` 5 fields (charter, context list, verbatim output, agent type+model, context sha256s). **No spawn identity; nothing forbids reading a sibling record** that sits in the dir the agent is pointed at | **Change**: add IDN (spawn identity + sibling-read ban) |
| P13 | "clean-or-resolved" | `stage-5:16,38-40` — "resolved" undefined; a minor is "fix in place, proceed"; at `stage-7:10-13` a fixed-in-place node is **indistinguishable** from a clean one | **Change**: RES (define resolved; distinguish at assembly) |
| P14 | Serial vs parallel | **never stated** anywhere | **Change**: declare (CNC) |
| P15 | Shared write surfaces | `index.md` written by every node's owner (`stage-1:21`); `plan/decisions.md` appended by every owner (`stage-5:19`); catalog `git commit` by any sub-orchestrator (`stage-6:32-35`). **Zero serialization.** `stage-8:17` asserts "no single global cursor" while `index.md` is exactly one | **Change**: partition to single-writer + catalog lock; make `index.md` derived |
| P16 | DEC operand | `METHODOLOGY:220-223` + `stage-6:27-31` "estimated leaf count / **work-size** ≥ 0.8× … two consecutive levels"; `decomposition-node.md:24-25` "a child ≥ 0.8× the parent trips the guard" (**single** level) → 2 operands, 2 trip conditions, no persistence site | **Change**: one operand (`elc`), one trip condition, persisted in `_status.md` |
| P17 | exit-plan-mode | GBP is *named after* it (`SKILL:33`, `METHODOLOGY:149`); **no stage covers the terminus** | **Change**: add the terminus to stage 7 (+ single-leaf case at 5) |
| P18 | `mode: ingest-and-complete` | **undefined** — not in the config contract, not in SKILL Inputs, not in any stage | **Change**: define the mode + `ingest_source` |
| P19 | Seed skeleton Layer-2 slots | `generic-node.md:32-34` has one; `decomposition-node.md` + `leaf-task-spec.md` have **none** | **Change**: add slots to both |
| P20 | Spot-verify-citations | `charter:88-92` states the duty as "whoever consumes the review" — **assigned to no stage** | **Change**: assign to stage 5 (+ stage 7 for the seam check) |
| P21 | TPL3 catalog commit | `stage-6:32-35` + `templates/seed/README:20-23` — an **unreviewed** skeleton patch is `git commit`ed to a shared cross-project repo inside the autonomous region | **Change**: stage-and-propose; one reviewed, locked, top-orchestrator commit |
| P22 | Inter-leaf dependency order | leaves are emitted with **no execution order**; `decomposition-node.md:19-22` seam table has no dependency column | **Change**: child DAG + assembled execution-order section |
| P23 | Root node location | `METHODOLOGY:265-272` shows `tree/_status.md` (apex roll-up) + `tree/<node>/`; the **root plan node's own dir is unpinned** | **Change**: pin `tree/root/` |
| P24 | §4 heading string | 5 variants: `SKILL:21` "Outputs & artifacts WITH their locations"; `METHODOLOGY:123` "Outputs & artifacts — deliverables **and their locations**"; `stage-2:11-12` "Outputs & artifacts (with their locations, incl. on-disk/output-folder layout)"; `generic-node:16` / `decomposition-node:10` "Outputs & artifacts (WITH their locations)"; `leaf-task-spec:13` "Outputs & their locations (§4)" | **Change**: one canonical heading string |

## B0.4 — Baseline live-copy state

`diff -rq /home/zero/.claude/skills/architect <WT>/Architect` at run start: identical except
`changes/` and `guarded-change.architect.md` (neither ships). So **live == source** holds at baseline
and is a real (not vacuous) criterion for stage 8: the build must re-sync the live copy.

## B0.5 — What "regression" means for this change

The artifact is a **prompt assembly**, so regression = **a baseline rule that stops being stated, or
starts being stated inconsistently, at a site the change did not intend to alter.** Two gating
regression checks follow from B0.2/B0.3 and are written as criteria at stage 1.5:
- **R1 (site-set non-erosion)** — every baseline rule-ID keeps at least its baseline site set (IDs may
  gain sites; losing one is a regression unless the criteria declare it).
- **R2 (deliberate-change completeness)** — for each of P1–P24 marked *Change*, the new claim is stated
  at **every** site that stated the old claim (no half-migrated rule) — the F5/§4-heading failure mode
  generalized.

---

# B0.6 — CORRECTED baseline rule-ID site map (pass 2; AUTHORITATIVE for R1/R2)

**Why this section exists.** All three stage-3 reviewers independently falsified B0.2. Recaptured with
`grep -rlw -- <ID>` over `SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/` at `3771038`,
then **hand-triaged for phantoms**, which is the step B0.2 skipped.

**The two error classes B0.2 committed — both now fixed, and both promoted into oracles:**
1. **Phantom sites from substring matching.** B0.2 listed `stages/stage-8-restart-resume.md` as a `TOP`
   site; it is not — the only match is inside **`HARDSTOP`** (`stage-8:20`). B0.2's own "measurement
   caveat" *misdiagnosed* this: it blamed `HARDSTOP` for the `generic-node`/`planning` hits and claimed
   word boundaries fixed it. In fact **`grep -w -- TOP` still matches the ordinary English phrase
   `ON TOP OF`** at `METHODOLOGY.md:79` and `examples/authoring-a-skill/planning.md:25` — a phantom class
   word boundaries do **not** remove. (`planning.md` therefore *is* a word-boundary TOP hit, but a
   **phantom** one, not a rule site.) Reviewer B additionally found `SPN`/`CMP`/`PASS1`/`PASS2` @
   `charter.md` listed in B0.2 and absent under word-boundary matching.
2. **Conflated ID families.** B0.2 folded `TPL1`/`TPL2` into `TPL` and omitted `SEV` entirely, so three
   live IDs sat outside both regression criteria while the change edits their files (A/F3-3, B/F-3).

| ID | CORRECTED baseline site set (word-boundary, phantom-triaged) |
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
| **TOP** | METHODOLOGY, SKILL, stage 6, templates/seed/decomposition-node — **NOT stage 8** (`HARDSTOP` phantom); the `examples/…/planning.md` hit is the **`ON TOP OF` phantom**, not a site |
| **CAP** | METHODOLOGY, SKILL, charter, stage 5 |
| **DEC** | METHODOLOGY, SKILL, stage 6, templates/seed/decomposition-node |
| **TPL** | METHODOLOGY, SKILL, stage 1, templates/seed/README |
| **TPL1** | METHODOLOGY, stages 1,2, templates/seed/README |
| **TPL2** | METHODOLOGY, stages 1,6, templates/seed/README |
| **TPL3** | METHODOLOGY, SKILL, stages 1,6, templates/seed/README |
| **RST** | METHODOLOGY, SKILL, stages 1,2,6,7,8 |
| **RAT3** | METHODOLOGY, SKILL, charter, stages 3,5,6 |
| **SEV** | stages 4,5 |

**21 baseline IDs** (not 18). `TPL1`, `TPL2`, `SEV` have **no row** in `METHODOLOGY.md`'s cross-file rule
index at baseline — a real baseline gap this change closes.

## B0.7 — Two measurement lessons promoted from prose caveat into gating oracles

B0.2's failure was that it recorded the lesson as a **comment** and then trusted a matcher that did not
implement it. Pass 2 does not repeat that: each lesson becomes a check with its own can-fail self-test.

1. **`ORACLE-SITEMAP`** — an ID's site set is computed with word-boundary matching **and** an explicit
   phantom-exclusion list (`ON TOP OF`, `HARDSTOP`), with the excluded hits *reported* rather than
   silently dropped. Self-test: it must report `stage-8` as a non-site for `TOP` and must report the two
   `ON TOP OF` hits as excluded phantoms.
2. **`ORACLE-IDCOLLIDE`** — for **every** ID in `METHODOLOGY.md`'s cross-file rule index, assert the token
   is **not a substring of any other uppercase token in the corpus**. Run at baseline it flags nothing
   (the baseline IDs pass); run against the pass-1 ID set it flags **`KIL` ⊂ `SKILL`** and
   **`ING` ⊂ `PLANNING`/`RULING`** — which is its can-fail self-test, and is how the two colliding IDs
   were caught and renamed (`KIL`→`KLB`, `ING`→`IGM`). This converts A/F3-2 from a promise into an
   instrument that protects cycles 2 and 3 for free.

## B0.8 — Baseline claims B0.3 got wrong (corrected; the substance of each row still holds)

Reviewer A checked all 24 rows line by line and found **no fabricated citation**. Corrections:
`P2` — `_status.md` occurs **13×**, not 5×, and the cited lines drift (actual: `METHODOLOGY:181,239,240,
266,268,280`; `stage-6:25`; `stage-7:20`; `stage-8:14,16`); `P9` — `METHODOLOGY:215`→**214**,
`stage-1:11`→**12**; `P10` — the overclaim is at **8 occurrences across 5 files**, adding
**`SKILL.md:8-9`** and **`SKILL.md:17`** (`METHODOLOGY:41`→**40**); `P15` — `stage-1:21`→**20**, and the
`index.md` writer set is **four** sites, not one: `stage-1:20`, **`stage-6:11-12`**,
**`METHODOLOGY:195`**, **`templates/seed/README:14`**; `P19` — `generic-node` has only the italic
**note**, no slot **heading**, so **3 of 3** skeletons fail S-C5's bar, not 2 of 3 (`:32-34`→`:32-33`);
`P24` — `SKILL:21`→**18-19**, `METHODOLOGY:123`→**121**, and the §4 heading has **6** distinct spellings
once prose sites are counted (`stage-3:43`, `METHODOLOGY:322`), not 5; `P17` — add `METHODOLOGY:316`
(the GBP index row also names exit-plan-mode).

**One departure from an owner-approved layout, now declared** (A/F4-2): the approved scope/decision
record `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:173` fixes **`tree/_status.md`** as the apex
roll-up. Pinning the root node to `tree/root/` moves it. This is a deliberate change to an
owner-approved on-disk layout, recorded in `decisions.md`, and it is made **because** the join and
assembly predicates need a root that is a node like any other (a special-cased root is how B/L-7's
orphan and B/L-9's ordering defects enter). The apex roll-up still exists, at `tree/root/_status.md`.
