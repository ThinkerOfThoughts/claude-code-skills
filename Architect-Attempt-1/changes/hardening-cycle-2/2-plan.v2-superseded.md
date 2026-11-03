# Stage 2 — Plan (hardening cycle 2, **PASS 2**)

Pass 1 is at `2-plan.v1-superseded.md`. Its two blockers (B/L1, B/L2) were both **`class (i)` used as an
exemption**. Pass 2's §1 replaces that table with one that cannot be escaped.

## 0. Shape

One coherent edit to **18 existing files**, no new artifact files. Sequenced **definitions → charter →
referencing stages → router → templates/examples → live-copy sync**, so no reference precedes its
definition.

**Governing discipline: GEN (owner-ratified R4).** *Apply the fix that already worked, generalized across
the class, and sweep every site.* Concretely, three questions must be answered for **every** predicate and
gate in the design — **baseline rules included, not only the ones this cycle adds** — and **`class (i)`
("computed, not stored") is not an exemption from any of them**:

- **(a) Producer:** what step writes the operand, is it **provably earlier** than the reader, and — for a
  class-(i) row — **what file does it compute over and which stage creates that file?**
- **(b) Degenerate case:** is the predicate defined at **n = 1 · the root · the first run · the empty tree**?
- **(c) Counterpart:** does every **acquire/open/begin** have its **release/close/end** named, **including
  on the failure path**?

**No mutation may be labelled class (i).** A `mkdir` is a mutation. That single rule is what pass 1 lacked.

---

## 1. THE GENERALIZATION SWEEP *(required section — this is the auditable coverage)*

Every predicate/gate in the design after this change. **`W→R`** = writer stage → reader stage in
**Architect's own** numbering (1 frame · 2 draft · 3 completeness pass · 4 adversarial pass · 5 gate ·
6 granularity/decompose · 7 assemble · 8 restart contract). Rows marked **† NEW** are added by this cycle;
the rest are **baseline rules swept for the first time** — which is the half both prior cycles skipped.

| # | Predicate / gate | Operand(s) | (a) Producer — provably earlier? | (b) Degenerate case (n=1 · root · first run · empty) | (c) Counterpart / release | Verdict |
|---|---|---|---|---|---|---|
| 1 | **GBP** — both passes clean-or-resolved | 6 record files; gate state | records: **3,4** → read **5,7** ✔ · gate state: **5** → read **7** ✔ | **n=1:** a single-leaf root has its own 3+3 records and its own gate — GBP applies unchanged. **empty tree:** no nodes ⇒ nothing to assemble; the run has no presentable artifact, stated at s7 | n/a (no acquire) | **OK** |
| 2 | **TOP** — top split human-approved | `plan/topgate/` exists (+ †`approved_root_plan_sha256`) | dir: **stage 1** creates it (**the F5 defect — deferred**); the hash: written by the approval's author, before **6** reads it ✔ | **n=1 / no decomposition ⇒ TOP NEVER FIRES** — stated explicitly at s6, because an unstated "never fires" is indistinguishable from a deadlock. **root:** TOP *is* the root's gate | n/a | **OK, with the F5 limitation STATED at the site** |
| 3 | **CAP** — 2 bounces, same class | bounce history | **5** → read **5** ✔ (append then read) | **first gate:** no history ⇒ count 0, stated | n/a | **OK** |
| 4 | **GRN** — leaf vs decompose | the proposed call in `plan.md` §2 | **2** → validated **3,4**, executed **6** ✔ | **n=1:** root returns leaf — the whole point | n/a | **OK** |
| 5 | **PASS-ORD** | record mtimes/existence | **3** before **4** ✔ | a node with neither pass ⇒ un-gated, not "ordered" | n/a | **OK** |
| 6 | **RST stage-done** | the deterministic output exists (†+ BIND-current for a record) | the stage that writes it ✔ | **empty node dir = the not-planned marker** (baseline) | n/a | **OK** |
| 7 | **BIND-cmp** † | `sha256(<node>/plan.md)` **now** vs the **dispatcher-recorded** `plan_sha256` in the record | **class (i) for the left operand — and the row must name its file and creator: it computes over `<node>/plan.md`, created by stage 2.** Right operand: **3,4** (the dispatcher writes it) → read **5,7** ✔ | **n=1 / root:** unchanged — **§1.4's narrowing removed the parent clause, so there is no root special case left to get wrong.** **no records yet:** un-gated, which is correct, not a deadlock | n/a | **OK** |
| 8 | **BIND-stale exit** † | — | — | — | **THE EXIT IS NAMED:** stale ⇒ un-run ⇒ **re-run that pass**; the fresh record **overwrites the file** (RST already says a clean re-dispatch overwrites a partial). Immutability = *the author never edits a recorded hash*, **not** *the file can never be rewritten* | **OK — was B/L5** |
| 9 | **BIND-rebind** † | a chain of `rebound_from`/`rebound_to` in `<node>/decisions.md` | **5** → read **5,7** ✔ | **n≥2 rebinds: the chain is TRANSITIVE and unbounded in length** — pass 1's "at most 2" made a node permanently un-gateable | each rebind entry is self-contained | **OK — was B/L7** |
| 10 | **BIND-gate-art** † | `approved_root_plan_sha256` vs `sha256(tree/root/plan.md)` | class (i) over `tree/root/plan.md` (**stage 2**) vs a field in the approval (**its author**, before **6**) ✔ | **no decomposition ⇒ no approval needed ⇒ vacuously satisfied**, stated | n/a | **OK** |
| 11 | **IDN** † | `spawn_id` in each record | **3,4** (dispatcher) → read **5** ✔ | **no dispatcher id ⇒ `unavailable-by-harness` + declared degraded** — never un-run. **<3 agents:** a declared reduced pass, already the baseline's shape | n/a | **OK** |
| 12 | **RES** † | gate state + finding lists in `<node>/decisions.md` | **5** → read **7** ✔ | **no findings ⇒ `clean`**, stated | n/a | **OK** |
| 13 | **SPV** † | the citations inside each record | **3,4** → read **5** ✔ | **a record with zero citations** ⇒ the charter's earned-clean clause already makes it un-run, stated | n/a | **OK** |
| 14 | **CTX** † | the config key | the **config author**, before stage 1 ✔ | **absent/empty ⇒ config error, stop the run** (that *is* the degenerate case, made non-vacuous) | n/a | **OK** |
| 15 | **DEC** † (amended) | `elc(self)` from own `plan.md`; `elc(parent)` from the parent's `plan.md` | **both written at stage 2**, the parent's **before this node existed** → read at this node's **6** ✔. **Within ECON: a node already holds its parent's plan** | **depth 1: no grandparent ⇒ DEC cannot trip**, stated. **root: never non-reducing** | n/a | **OK — was B/L3 (pass 1 needed `elc(grandparent)`, outside the reader's surface)** |
| 16 | **DEP** † | the child dependency DAG in `plan.md` | **2** → read **4, 7** ✔ | **leaf ⇒ no children ⇒ no DAG, no cycle; execution order = that one leaf**, stated | n/a | **OK** |
| 17 | **IGM** † | `tree/root/plan.md.ingested` | **stage 1** copies it → read **2, 3** ✔; **added to the deterministic-filename list AND the closed input set** | **`mode: fresh` ⇒ the file does not exist, and its absence is NOT a missing closed-set input** — stated, else stage 3 deadlocks in fresh mode | the copy is immutable; nothing to release | **OK — was B/L14** |
| 18 | **TPL2/TPL3** † | `catalog-pending/*` | **6** → read at **run end** ✔ | **no proposals ⇒ run end does nothing AND DOES NOT TAKE THE LOCK**, stated | n/a — but see #19 | **OK** |
| 19 | **CNC catalog lock** † | the lock **directory** | **NOT class (i) — `mkdir` is a MUTATION.** Acquired by whichever step needs it (**1** for the seed, **run end** for the commit); **the acquiring step is the releasing step** | **FIRST RUN:** the catalog does not exist, so **the lock is a SIBLING of the catalog dir, not inside it** (pass 1 put it inside ⇒ ENOENT for every contender), and the seed step creates the parent, acquires, seeds, `git init`s, **releases**. **empty:** no proposals ⇒ never acquired | **RELEASE NAMED: the same step `rmdir`s it — on success, on every failure path, and before any HALT.** A held lock whose pid is **alive** is **waited on, then HALT+relay**; only a **dead** pid may be broken, via `BROKEN-BY` + a log entry | **OK — was B/L2 (run 1 deadlocked against its own acquisition)** |
| 20 | **CNC catalog READERS** † | the catalog working tree | — | — | **every reader takes the same lock, or reads a git commit rather than the working tree** — pass 1's enumeration was **writer-only** | **OK — was B/L9** |
| 21 | **`index.md` derived** † | the tree | regenerated by the **top orchestrator** by walking `tree/` and reading each `<node>/plan.md` **header** | **the `template used` fact has a NAMED DESTINATION: the node's own `plan.md` header, written by stage 1 — the only writer of that file.** Pass 1 removed `index.md`'s writers and routed this fact to the **deferred** `_status.md` schema, stranding it | n/a | **OK — was A/F3** |
| 22 | **HG2** † | `plan/assembly-approval.md` | **the human**, relayed; recorded by the top orchestrator **after** the presentable artifact exists → read at the **terminus** ✔ | **THE CARVE-OUT (generalizing BIND's root carve-out per R4): HG2 applies to whichever artifact is presentable — `assembled-plan.md` for a decomposed run, or `tree/root/plan.md` for a single-leaf run.** So a leaf-only run **reaches** the gate and **can pass** it. **This is the mode this hardening loop runs itself in, so it must work** | the gate is released by the approval; a bounce re-opens the named nodes at **2** | **OK — was B/L1** |
| 23 | **HG2 — the SPLIT FACT** † | `planning-complete` vs `presentable` | **planning-complete** = the node's own gate cleared (**5**). **presentable** = the human approval exists (**after 7**). **The terminal fact is written LAST** — cycle 1's recorded diagnosis, applied here | **restart:** the run-complete marker is **`plan/assembly-approval.md`**, *never* the existence of `assembled-plan.md` — else a restart reads "complete" and **bypasses HG2** | n/a | **OK — was B/L4** |
| 24 | **XPM** † | the presentable artifact + **both** gates | both operands produced before the terminus ✔ | single-leaf: see #22 | n/a | **OK** |
| 25 | **SC3 / rule-block position** † | the block's order | this cycle's edit | **new rules go BEFORE GBP so GBP keeps the recency slot** (cycle 1's confirmed fix, which pass 1 reversed); the block's **closing rationale is re-enumerated to name all five** | n/a | **OK — was A/F1 ∥ B/L12** |
| 26 | **charter fork-provenance** † | the blockquote | this cycle's edit | the blockquote says the core was *"carried whole … DROPPED: nothing"*; this cycle **edits carried core bullets**, so it must record what the fork now **ADDS** — it is handed to every cold reviewer **verbatim**, so a false blockquote lies to every reviewer | n/a | **OK — was A/F6** |

**Rows that changed verdict from pass 1: 7, 8, 9, 15, 17, 19, 20, 21, 22, 23, 25, 26 — twelve.** Ten of
those twelve were **baseline or already-planned rules that pass 1 never asked (a)/(b)/(c) about**, which is
precisely the under-generalization R4 forbids.

---

## 2. The edits, fix by fix

`1.5-criteria.md` §1 pins the exact sentence each site must carry; this section states the substance and the
**measured** site set (`0-baseline.B7-measured-sites.md`). Site lists are **not** hand-selected in this pass.

**D1 · BIND** — a record is current iff `sha256(<node>/plan.md)` computed **now** equals the
**dispatcher-recorded** `plan_sha256` in the record. **The operand is dispatcher-recorded, not
reviewer-reported — the exact fix IDN already applies to identity, generalized to the binding hash per R4
(B/L6).** The reviewer's own reported hash stays in the record as corroboration; a divergence between the
two is itself a finding (the reviewer read something else). **The parent clause is dropped** (§1.4 of the
spec) — one operand, no cascade, no root special case. **Stale ⇒ un-run ⇒ re-run that pass**, whose fresh
record overwrites the file. **Immutable** = the author never edits a recorded hash. **Rebind chains are
transitive and unbounded.** **Gate artifacts:** `APPROVAL.md` carries `approved_root_plan_sha256`; TOP is
unsatisfied while it differs from `sha256(tree/root/plan.md)`. **F5's limitation is stated at that site.**
*Sites:* ch, s3, s4, s5, s6, s7, s8, M, S.

**D2 · IDN** — dispatcher-recorded `spawn_id`; the asymmetry stated in both directions (3 identical
**dispatcher** ids ⇒ un-run; 3 identical **self-reports**, incl. three `unavailable`, **never** un-run);
`unavailable-by-harness` + declared-degraded; sibling-read ban. *Sites:* ch, s3, s4, s5, M.

**D3 · RES** — three arms; the five gate states; all three clean states assemble; each assembled section
carries its state + `fixed_findings` + `demoted_findings`. **The circularity is closed at all 13 measured
`clean-or-resolved` sites**, each pointing at RES's definition. *Sites:* the 13 measured sites + s5, s7, M.

**D4 · CTX** — first-class `redteam_context:` key, priority-ordered `path`/`note`; de-conflated from
`off_limits_paths` (citable source vs. never-write fence; a path may be both); **absent/empty ⇒ a config
error that stops the run**, because path-validation over an absent key checks zero paths. *Sites:* M, S,
s3, ex/planning, ex/README.

**D5 · OFL** *(subtractive)* — `off_limits_paths` is a **prompt-level convention, not an enforced fence**;
nothing intercepts a write; **nothing catches a stray write to a path the config never declared**; a real
fence must come from outside this skill. *"Naming is the fence"* is deleted. *Sites:* M, s1, ex/planning.

**D6 · PRV** — the subtractive half at **all 8 measured occurrences across 4 files** (not 5 — cycle 1's
error, repeated by pass 1, now fixed). The canonical sentence: *"The gate raises the cost of shipping a
hole. It does not certify its absence."* **The positive half ships only with its limitation attached at the
same site** (A/F4): what the gate establishes is **attested by the reviewers themselves and sampled**, not
independently proven; tier (iii) asks for a **negative no finite review can prove**; **N same-model
instances are not N independent minds**, so blind spots are **correlated**; and whether frame diversity
narrows that is **unsettled by this skill** (DIV deferred, not claimed). *Sites:* S:3, S:8, S:17, M:4,
M:40, M's new PRV block, R:10, R:12, s7.

**D7 · SPV** — the spot-verify duty is **stage 5's**, with a stated sample size (≥1 per record, ≥2 per
pass), recorded in `<node>/decisions.md`, and a fabricated citation makes that record **un-run**; stage 7
carries the cross-node half. *Sites:* ch, s5, s7.

**D8 · CNC** — the serial/parallel declaration; `index.md` **derived** with the `template used` fact routed
to the node's **own `plan.md` header** (#21); the per-node gate log `<node>/decisions.md` with
`plan/decisions.md` reserved for run-level events; and the **catalog lock done properly** (#19, #20):
sibling-not-child, acquire-and-release in the same step incl. every failure path and before any HALT,
first-run parent creation, wait-then-HALT on a live pid, `BROKEN-BY` only for a dead one, and **readers
covered**. The declared-uncovered case (two runs, one `run_root`) stays declared. Stage 8's false *"no
single global cursor"* goes. *Sites:* the 9 measured `index.md` files, the measured gate-log sites, s1, s6,
s8, tp/README, M, S, ch.

**D9 · DEP** — a dependency edge per dependent child pair; a **cycle is a blocker**; stage 7 emits
`## Execution order`; **the composition rule is stated** (a child's whole subtree is one unit in its
parent's order; within it the child's own edges apply — which composes to a total order over the leaves,
B/L17). *Sites:* s2, s4, s7, M, tp/decomposition-node, tp/leaf-task-spec.

**D10 · DEC/`elc`** — `elc` **self-declared, not computed**; **one** trip condition, with the operand made
readable **within ECON** (own `plan.md` + the parent's `plan.md`, both written at stage 2); **undefined at
depth 1**, stated; and what DEC **cannot** detect assigned to GRN's validation duty. The single-level
formulation in `decomposition-node.md` goes. *Sites:* M, s2, s6, tp/decomposition-node.

**D11 · IGM** — `mode: fresh | ingest-and-complete` (+ `ingest_source`); immutable copy to
`tree/root/plan.md.ingested`; the spine→locus **mapping table** with `ABSENT` rows as candidate holes; no
silent authoring; `architect-authored` marking; **and `plan.md.ingested` added to the
deterministic-filename list and to the closed input set, with its absence in `fresh` mode stated as not a
missing input**. *Sites:* M, S, s1, s2, s3, s8, ch, ex/planning.

**D12 · TPL3** — stage-and-propose into `catalog-pending/`; commit **only** at run end, **only** by the top
orchestrator, **only** under the lock, **only after a cold review of the proposed diff**; no mid-run commit
anywhere. *Sites:* s6, tp/README, M.

**D13 · RST** — root pinned to `tree/root/`; the apex roll-up to `tree/root/_status.md`. **Departures
DECLARED — both of them** (A/F5 caught that pass 1 declared one and not the other): (i) the approved record
fixes `tree/_status.md` as the apex roll-up; (ii) the approved record puts gate/route entries in
`plan/decisions.md`, and D8 moves the per-node ones to `<node>/decisions.md`. *Sites:* M, s1, s7, s8.

**D14 · SPN** — one canonical string, **`Outputs & artifacts (with their locations)`**, at all measured §4
sites. *Note the matcher must flatten wraps:* `SKILL.md:18-19`'s heading is **wrapped across a line break**
at baseline, which is why the normalization self-test (mutation 4) is a real case.

**D15 · seed slots** — the identical `## Layer-2 required sections (from the config's required_sections)`
heading in **all three** skeletons (`generic-node.md`'s italic note is promoted to it).

**D16 · HG2 + XPM** — the second human gate at assembly, **with the degenerate-case carve-out (#22) and the
split fact (#23)**; the run-complete marker is the **approval**, not `assembled-plan.md`; TOP's "ONLY"
narrowed to **decomposition** gates at all **7 measured** sites while preserving the anti-gate-fatigue half;
XPM's both-gates statement at all **10 measured** terminus sites; **HG2's own limitation stated** (the
approval is agent-authored, so *"never self-approved"* is a **duty the loop states**, not a property its
mechanism enforces — B/L15, the same honesty TOP already carries); the **bounce mechanics marked as this
cycle's authoring choice, not ratified**; and the **forward constraint** on the deferred assembly rework.

**D17 · ID hygiene** — `grep -rlnow` over the full corpus; the phantom caveat; the naming rule with its
family stems and its two **declared grandfathered** violations; index rows for `TPL1`/`TPL2`/`SEV` **and
every new ID**; `IGM` not `ING`; `KLB` reserved, not `KIL`.

**D18 · charter fork-provenance** — the blockquote records what Architect's fork now **ADDS** to the carried
core (the `spawn_id` field, BIND's comparison duty, stage 5 as the named spot-verify consumer, the
node-local gate log), so it stays true for the reviewers who read it verbatim.

---

## 3. Measurement + instrumentation

**`oracles/check.sh <tree> [criterion]`** — one subcommand per `1.5` row; asserts the **pinned string** at
every site in the pinned SITES list on **normalized** text; every absence sweep **paired**. **`CORPUS` is
defined once, at the top, and excludes `changes/`** (C/O3).
**`oracles/expected-sites.txt`** — the ID→file expectation data file R1 compares against.
**`oracles/ruleid-sitemap.sh <tree>`** — now a **checker**: MISSING / UNEXPECTED, **exit 1** (C/O1, C/O2).
**`oracles/idcollide.sh`** — grandfather list corrected (`TOPGATE`/`DECOMPOSITION` removed — C/O8).
**`oracles/baseline-replay.sh`** — same `check.sh`, same pinned corpus, over
`git show b08f5a9:Architect/<file>`. **Every new-rule assertion must FAIL there.**
**`oracles/lockrace.sh`** — the **executed** race for S-CNC-LOCK: two concurrent `mkdir`s (exactly one
wins), a crash with the lock held (release path runs; the next run is not deadlocked), the first-run path
(no catalog dir), and the **unguarded control** (must fail without the lock — H4).
**Behavioural arms:** 3 clusters × 2 arms × **2 spawns** = **12**, agent held constant, fixture the only
variable (`1.5` §5).

## 4. Concurrency (ST2b) — accessors enumerated, **readers included**

The operative table is §1 rows **19, 20, 21, 26** plus D8. Pass 1's enumeration was **writer-only and
undercounted** (B/L9); the measured accessor sets are in `0-baseline.B7-measured-sites.md` — **`index.md`
has 18 accessors across 9 files**, not 4 writers, and the gate log 17 across 4. For `index.md`,
`_status.md` and the gate logs the guard is **not a lock**: the accessor set is reduced to **one writer**,
so there is no scope gap. The **only** lock is the catalog, and its scope now covers **five** paths:
mid-run writes, run-end writes, **concurrent runs**, the **first-run seed**, and **readers** (#20).
**S-CNC-LOCK is GATING and executed** — pass 1's advisory relabel rested on the false premise that nothing
here is executable (B/L10); the lock is a `mkdir`, and `initial-authoring-2026-07/8-harness.md` records this
repo already driving a real git catalog end-to-end.

## 5. Thresholds → routing

Route on the **reviewer's** severity (SEV3); contest only via a logged entry; **demoting a blocker/major
requires the human tie-break** — under RAT3, a **HALT + verbatim relay**, never taken here.
**blocker → 1 · major → 2 · minor → fix in place · nitpick → log.**
**CAP/SEV4 under R4:** a recurrence of a known defect class **in a new section** is **under-generalization**,
not a cap bounce — the ruling prescribes generalizing the proven fix. **A recurrence in a section this pass
claims to have swept is a genuine bounce** and is relayed, not argued. All criteria are **gating**; the only
legal dispositions for an unverifiable one are a representative harness or a **named risk-acceptance**, and
under RAT3 the remaining move is **HALT + relay**. **No "declared deferral" exists in this plan.**

## 6. Risks

| Risk | Contingency |
|---|---|
| **The sweep itself is incomplete — a 27th predicate nobody listed** | §1 is generated from the artifact's own rule set (the 21 baseline IDs + the 12 new ones) rather than from memory; `S-INDEX-complete` asserts the ID set is total, so an unlisted rule with an ID is caught mechanically. **Residual risk stated: a predicate with no ID is invisible to that check** — the stage-3 reviewers are pointed at exactly this gap |
| A pinned string is pinned to text that is *wrong* | The pinned strings **are** the text being written, so `check.sh` cannot disagree with the artifact — which is why the **stage-3 reviewers**, not the checker, are the guard on whether the sentence says the right thing. Stated so the checker is not mistaken for a semantic oracle |
| 18 files × 12 new IDs → cross-file contradiction | SC5's recorded per-ID diff rubric; R2's total-mapping assertion |
| The softened description stops triggering | SC1 + SC2, both measured |
| An oracle passes at baseline | `baseline-replay.sh` gates every `S-` row; a row that passes there is `verified = no` |
| 12 arms + 4 oracle mutations + 4 lock-race cases is real runway | Fixtures are tiny; if an arm cannot run, its criterion is `verified = no` and this runner **HALTs and relays** — never folded into "done" |
| The `<node>/decisions.md` partition half-migrates across ~10 files | It is a CHANGE row with a **measured** 17-hit site set, asserted positively per site (S-CNC-gatelog) |
