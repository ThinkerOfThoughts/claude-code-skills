# Stage 2 — Plan (hardening cycle 2, **PASS 3**)

Pass 1 is at `2-plan.v1-superseded.md`; **pass 2 is at `2-plan.v2-superseded.md`**. Neither is rewritten.
Pass 2's §1 headline claimed a sweep over *"every predicate and gate, baseline rules included"* while **15
of 21 baseline IDs had no row** — the claim was false and three live defects were hiding in the remainder.
**The correction lives here, and it is mechanical:** the row set is no longer authored.

## 0. Shape

One coherent edit to **18 existing files**, no new artifact files. Sequenced **definitions → charter →
referencing stages → router → templates/examples → live-copy sync**, so no reference precedes its
definition.

> **⚠ R7 LABEL.** §1 is organised around three questions — **(a) producer, (b) degenerate case,
> (c) counterpart.** That framing is an **ORCHESTRATOR PROPOSAL, not an owner requirement.** R4's ratified
> content is the owner's one sentence: *"if its the same kind of problem that was encountered/fixed in a
> different section, then the fix that was applied in that other section should be applied here; that it
> didn't catch it in the current section in the previous round means nothing."* The framing is a working
> aid for satisfying that sentence and is **never** cited as something the owner requires.

**One rule inside the framing that pass 1 lacked, and it is this runner's own:** **no mutation may be
labelled *"class (i), computed not stored."*** A `mkdir` is a mutation. Pass 1's two blockers were both
`class (i)` used as an **exemption** from the question *"who writes this?"*.

---

## 1. THE GENERALIZATION SWEEP — **GENERATED, AND THE JOIN IS ENFORCED**

This is the auditable coverage, and pass 3 changed **how** it is produced rather than how it reads.

**The row set is not authored.** `oracles/gen-sweep-rows.sh` computes it from the measurement files:

```
$ oracles/gen-sweep-rows.sh | tail -1
TOTAL ROWS REQUIRED: 86
   = 21 live baseline rule IDs      (from oracles/expected-sites.txt, itself GENERATED from the tree)
   + 60 NEW/COOC criteria           (from oracles/criteria.tsv)
   +  5 predicates carrying NO rule ID, listed explicitly in the generator because an ID-driven
        generator is STRUCTURALLY BLIND to them
```

**Only the three answer columns are authored** (`oracles/sweep-answers.tsv`), and
`oracles/gen-sweep-table.sh` joins the two:

```
$ oracles/gen-sweep-table.sh | tail -2
ROWS EMITTED: 86   (generated row set: 86; authored answers: 86)
SWEEP: OK — the row set is generated and every generated row is answered (totality enforced, not asserted)
```

**Totality is enforced, and the enforcement was mutation-tested in both directions** — this is the
mechanism that makes D/2 structurally impossible rather than promised:

```
$ # MUTATION 1: delete the closed-input-set answer (the exact omission that hid 3 of pass 2's 9 blockers)
SWEEP: FAIL — generated rows with NO authored answer: closed-input-set          EXIT=1
$ # MUTATION 2: an authored answer for a predicate that no longer exists
SWEEP: FAIL — authored answers with NO generated row: S-GHOST                   EXIT=1
```

**⚠ THE RESIDUAL, AND A GENERATOR CANNOT STATE IT FOR ITSELF.** The five no-ID predicates
(`closed-input-set`, `stage-done-iff-output-exists`, `path-validation`, `catalog-pending`, `run-end`) are in
the table **only because a human listed them** in the generator. **Three of pass 2's nine blockers lived in
exactly that blind spot.** If a **sixth** such predicate exists — a rule stated in the stage files with no
mnemonic ID and no criterion — **no generator in this cycle will find it, and `SWEEP: OK` will still
print.** Only a reader looking for *predicates* rather than for *IDs* can close that gap, and finding one is
handed to stage 3 as a named task rather than hoped for.

**Verdict vocabulary.** `OK` · `FIXED` (a defect closed in scope this cycle) · `PARTIAL+DECLARED` (one half
fixed, the other named and deferred) · `DECLARED GAP` (a genuine member of the class that falls **outside**
R1's ratified scope — named here, **not** fixed, never silently dropped). **`W→R`** = writer stage → reader
stage in Architect's own numbering (1 frame · 2 draft · 3 completeness pass · 4 adversarial pass · 5 gate ·
6 granularity/decompose · 7 assemble · 8 restart contract).

*The table below is `gen-sweep-table.sh`'s output, verbatim.*

| # | Predicate / gate | source | (a) producer provably earlier? | (b) degenerate: n=1 · root · first run · empty | (c) counterpart / release | verdict |
|---|---|---|---|---|---|---|
| 1 | **GBP** | baseline rule ID | the 6 record files: written by stages 3 and 4, read at 5 and 7. the gate state: written by 5, read by 7. both provably earlier | n=1: a single-leaf root has its own 3+3 records and its own gate, so GBP applies unchanged. empty tree: no nodes, so nothing is presentable and there is no artifact to gate — stated at s7 | no acquire | OK |
| 2 | **PASS1** | baseline rule ID | the three completeness records: written by stage 3's dispatcher, read at 5 | n=1: the root is a node like any other, so PASS1 fires on it. fewer than 3 agents available: a declared reduced pass (S-IDN-DEGR), never un-run | no acquire | OK |
| 3 | **PASS2** | baseline rule ID | the three adversarial records: written by stage 4's dispatcher, read at 5 | same as PASS1, and additionally: PASS2 cannot start before PASS1's set exists (PASS-ORD) | no acquire | OK |
| 4 | **PASS-ORD** | baseline rule ID | the ordering fact is the existence of completeness/ before adversarial/ is dispatched; stage 4 checks it at its own start, and 5 re-reads both sets | a node with neither set is un-gated, not "ordered" — stated at s5. a node with only completeness/ is mid-pass, which is the same un-gated state | no acquire | OK |
| 5 | **CMP** | baseline rule ID | the 7 spine sections + Layer-2 list live in plan.md, written by 2, read by 3. the Layer-2 list comes from the config, written before stage 1 | n=1 / root: unchanged. EMPTY required_sections: tier (ii) becomes vacuous — the same "an absent config key makes the check pass trivially" class as S-CTX-VAC, and nothing states it | no acquire | DECLARED GAP — the class is named (config-key vacuity), the fix is S-CTX-VAC's, and applying it to required_sections is NEW MECHANISM outside R1's ratified scope. Declared, not fixed |
| 6 | **CMP2** | baseline rule ID | the operand is the record's own statement that the generative sweep ran: written by 3, read by 5 via the charter's earned-clean clause | a node with no Layer-2 sections: tier (iii) is then the only tier with content, so CMP2 is MORE load-bearing, not less | no acquire | OK |
| 7 | **SPN** | baseline rule ID | the §4 heading string in plan.md: written by 2 (from the seed skeleton), read by 3 | a leaf task-spec compresses the spine but drops nothing — stated in tp/leaf, and S-SPN pins the one canonical spelling at all 6 measured §4 sites | no acquire | OK |
| 8 | **COV** | baseline rule ID | SPLIT. gate-state half: each node's own recorded gate state, written by 5, read by 7 — a producer now exists (S-COV-PROD). seam-union half: NO producer anywhere on disk; nothing rolls a child's seam finding up to its parent | n=1: there are no seams at all, so the seam half is vacuous and the gate-state half is the whole predicate | no acquire | PARTIAL+DECLARED — gate-state half FIXED (was D/3); seam-union half needs F1's up-flow and is stated at all 4 measured sites by S-COV-LIMIT |
| 9 | **ORC** | baseline rule ID | the orchestration tree is created by the same stage-6 step that creates each child node, so the mirror cannot lag the tree | n=1: no sub-orchestrators exist; the top orchestrator is the only owner — stated | a spawned sub-orchestrator's counterpart is its RETURN, and a sub-orchestrator that dies has no named detector | PARTIAL+DECLARED — the missing death detector is F6's killed-node marker + run-level abort, deferred by R1 and named here |
| 10 | **ECON** | baseline rule ID | not a disk predicate: a context-assembly rule applied at spawn time by stage 6 | n=1: the root's subtree is the whole tree, so ECON is vacuous — stated | no acquire | OK — and ECON's O(children²) parent-seam load is declared out of scope (R1) |
| 11 | **GRN** | baseline rule ID | the proposed leaf-or-decompose call in plan.md §2: written by 2, validated by 3 and 4, executed by 6 | n=1: the root returns leaf, which is the whole point of the scale-down path | no acquire | OK |
| 12 | **TOP** | baseline rule ID | the plan/topgate/ DIRECTORY is created EMPTY by stage 1, so a bare-existence test is self-satisfying — the F5 defect. the approved_root_plan_sha256 field is written by the approval's author before 6 reads it | n=1 / no decomposition: TOP NEVER FIRES — stated explicitly, because an unstated "never fires" is indistinguishable from a deadlock. root: TOP is the root's own gate | no acquire | OK ONLY BECAUSE THE LIMITATION IS STATED — S-F5-LIMIT pins it at all 6 measured topgate sites; S-BIND-GATEART adds the staleness condition. F5's mechanism is deferred |
| 13 | **CAP** | baseline rule ID | the bounce history in the gate log: appended by 5, read by 5 on the next iteration | the first gate has no history, so the count is 0 — stated | no acquire | OK |
| 14 | **DEC** | baseline rule ID | elc(self) from this node's plan.md and elc(parent) from the parent's plan.md, both written at stage 2 and the parent's before this node existed; read at this node's stage 6. within ECON a node already holds its parent's plan | depth 1: there is no grandparent, so DEC cannot trip — stated. the root's own level is never non-reducing | no acquire | OK — was B/L3 (pass 1's formulation needed elc(grandparent), outside the reader's surface) |
| 15 | **TPL** | baseline rule ID | the catalog's existence: stage 1's run-level setup seeds it from templates/seed/ and git-inits it, before TPL1 reads it at stage 1 and TPL2/TPL3 read it at stage 6 | FIRST RUN: the catalog does not exist. the lock must therefore be takeable BEFORE the catalog exists, which is exactly why the lock is the catalog's SIBLING and never inside it (S-CNC-LOCK) | the seeding step acquires the catalog lock and releases it — on success, on every failure path, and before any HALT (S-CNC-LOCK-REL) | FIXED — was B/L2, the first-run deadlock |
| 16 | **TPL1** | baseline rule ID | template: <name> is written into that node's OWN plan.md header by stage 1, the only writer of that file, and read at stage 2 (S-CNC-TMPL) | no match: the recorded value is the explicit token create-new, not an absent key — an absent key would be indistinguishable from an unwritten one | no acquire | FIXED — was A/F3: pass 1 removed index.md's writers and stranded this fact in the deferred _status.md schema |
| 17 | **TPL2** | baseline rule ID | the distilled new skeleton: written at stage 6 after the node is gated clean, read at run end | no create-new node: nothing to distil, so run end does nothing AND MUST NOT TAKE THE LOCK — stated | the catalog commit's counterpart is the lock release (S-CNC-LOCK-REL) | OK |
| 18 | **TPL3** | baseline rule ID | the staged proposal at catalog-pending/<node-path>.md: written at 6, read at run end. the filename is DERIVED FROM THE NODE PATH, so N concurrent proposers cannot collide (S-CNC-PENDING) | no hole-fix: no proposal, and run end does not take the lock. first run: the directory is created by the first proposer | the staged proposal's counterpart is the run-end commit OR an explicit discard; the lock taken to commit is released on every path | FIXED — was D/12 ∥ F/11, which pass 2 recorded as a cycle-3 carry-forward and did not fix |
| 19 | **RST** | baseline rule ID | the deterministic output, written by whichever stage owns it | empty / incomplete node dir IS the "not planned yet" marker (baseline). ONE NAMED EXCEPTION: stage 7 is done only when plan/assembly-approval.md exists, else the presence of assembled-plan.md marks stage 7 done and HG2 never re-fires (S-RST-RESUME) | HARDSTOP's counterpart is the clean re-dispatch, which overwrites the partial file because a partial is not the deterministic name | FIXED — was D/6 |
| 20 | **RAT3** | baseline rule ID | the stop condition is computed at the stage that raises it, over the gate log written by 5 | no delegation: RAT3 is vacuous because the human is present — stated | the halt's counterpart is the orchestrator's RELAYED ANSWER. there is no timeout, so a run can wait indefinitely; that consequence is stated rather than bounded (see run-end) | OK WITH THE UNBOUNDED WAIT STATED |
| 21 | **SEV** | baseline rule ID | the reviewer's stated severity: written by the reviewer at 3/4, read at 5 | a record that states no severity is un-run under the charter's earned-clean clause, NOT clean | no acquire | OK |
| 22 | **S-BIND** | new criterion | the pinned sentence is text; the rule's operands are the dispatcher-recorded plan_sha256 (3,4) and sha256(plan.md) computed now over a file stage 2 wrote | n=1 / root: unchanged — §1.4's narrowing removed the parent clause, so no root special case remains. no records yet: un-gated, which is correct, not a deadlock | no acquire | FIXED |
| 23 | **S-BIND-DISP** | new criterion | the dispatcher writes the hash at spawn, i.e. strictly before the reviewer it constrains produces anything | a harness that exposes no spawn-time hook: then BIND has no valid operand and the pass is declared degraded by the same rule IDN uses — not silently self-reported | no acquire | FIXED — the IDN fix generalized one field over (B/L6) |
| 24 | **S-BIND-ONE** | new criterion | one operand, this node's own plan.md, written by stage 2 | root: structurally fine — no record reports a parent hash, so there is nothing to carve out | no acquire | FIXED |
| 25 | **S-BIND-EXIT** | new criterion | the exit is a re-dispatch by 3 or 4, whose fresh record overwrites the file | a node whose every record is stale is un-gated, not blocked forever: the exit exists at every multiplicity | the stale record's counterpart is the fresh record that replaces it | FIXED — was B/L5 |
| 26 | **S-BIND-REBIND** | new criterion | each rebind entry is written into <node>/decisions.md by stage 5 and dispatcher-recorded | chain of length 0 (no rebind) and chain of length n are the same rule; pass 1's "at most 2" made a node permanently un-gateable | each rebind entry is self-contained | FIXED — was B/L7 |
| 27 | **S-IDN** | new criterion | the dispatcher observes the id at spawn and records it, before the reviewer produces anything | no dispatcher-observable id: spawn_id: unavailable-by-harness, pass declared degraded | no acquire | FIXED |
| 28 | **S-IDN-ASYM** | new criterion | same producer as S-IDN | 3 identical DISPATCHER ids ⇒ un-run. 3 identical SELF-REPORTS, including three "unavailable", ⇒ never un-run. both directions stated, because pass 1's unconditional rule would have made this loop's own reviews un-run | no acquire | FIXED |
| 29 | **S-IDN-DEGR** | new criterion | same producer as S-IDN | this row IS the degenerate case, made non-vacuous: degraded is a recorded status, not an absent field | no acquire | FIXED |
| 30 | **S-RES** | new criterion | gate state + finding lists in <node>/decisions.md, written by 5, read by 7 | no findings ⇒ clean, stated. a demoted major ⇒ clean-demoted, which is distinguishable from clean | no acquire | FIXED |
| 31 | **S-RES-STATES** | new criterion | same producer | all three clean states assemble, so a fixed-in-place node is not stranded — this is what unified RES(a) with BIND | no acquire | FIXED |
| 32 | **S-RES-SWEEP** | new criterion | the short clause is text at all 8 measured clean-or-resolved sites; it points at RES's definition rather than restating it | a site that states clean-or-resolved without RES's definition is the circularity pass 1 shipped; the sweep closes it by measurement, not diligence | no acquire | FIXED — and note the pinned clause is deliberately SHORT because it must be true at 8 sites |
| 33 | **S-CTX** | new criterion | the config author writes redteam_context before stage 1 reads it | absent/empty ⇒ S-CTX-VAC's config error | no acquire | FIXED |
| 34 | **S-CTX-DECONF** | new criterion | both keys come from the config author | a path that is BOTH citable source and off-limits is the interesting case and is stated explicitly | no acquire | FIXED |
| 35 | **S-CTX-VAC** | new criterion | the absence itself is computable at stage 1 over the config file, which the config author wrote | this row IS the degenerate case: path-validation over an absent key checks zero paths and passes trivially, so absence must be an error rather than a pass | no acquire | FIXED |
| 36 | **S-PATHVAL** | new criterion | the path list comes from the config; the CHECK is run by stage 1 at run start and again by whichever stage spawns | first spawn and every later spawn are both covered, so a path that dies mid-run is caught. the recorded result lives in <node>/decisions.md, written by that node's owner | no acquire | FIXED — this gives the no-ID path-validation predicate a producer AND a record |
| 37 | **S-OFL** | new criterion | purely subtractive: it deletes a claim | n/a — nothing is enforced, which is the point being stated | no acquire | FIXED (subtractive) |
| 38 | **S-PRV** | new criterion | purely subtractive at all 4 measured overclaim sites, plus a corpus-wide absence sweep on PROVEN (case-sensitive) and "proven, not asserted" | n/a | no acquire | FIXED (subtractive) |
| 39 | **S-PRV-LIMIT** | new criterion | the limitation is text at the 4 measured tier sites | a run with 1 reviewer instead of 3: the correlation claim gets WORSE, not better, so the limitation is if anything understated | no acquire | FIXED — and it explicitly declines to claim frame diversity fixes the correlation (DIV deferred) |
| 40 | **S-SPV** | new criterion | the citations are written into each record by 3/4; the SAMPLING is stage 5's duty and its result is recorded in <node>/decisions.md | a record with zero citations is already un-run under the charter's earned-clean clause — stated, so the sample size is never zero-by-vacuity | no acquire | FIXED — the duty now has a named owner, replacing "whoever consumes the review" |
| 41 | **S-CNC-DECL** | new criterion | the declaration is text; the facts it declares are structural | n=1: no siblings, so the only parallelism left is the three cold agents within one pass — still real | no acquire | FIXED |
| 42 | **S-CNC-INDEX** | new criterion | index.md is regenerated by the top orchestrator by walking the tree, so its producer is the tree itself | empty tree ⇒ an empty index, not a missing one. a stale index cannot mislead because it is never authoritative | no acquire | FIXED |
| 43 | **S-CNC-TMPL** | new criterion | stage 1 writes the node's plan.md header; it is the only writer of that file | create-new is an explicit recorded value | no acquire | FIXED |
| 44 | **S-CNC-GATELOG** | new criterion | each node's owner writes that node's decisions.md; the top orchestrator writes plan/decisions.md | n=1: the root's own gate log and the run-level log are two files even when one node exists — stated, so the partition does not collapse | no acquire | FIXED — the write-write race is closed by reducing the accessor set to one writer |
| 45 | **S-CNC-LOCK** | new criterion | the lock is created by the step that needs it; the symlink target IS the holder's pid, so lock and owner appear in ONE indivisible step | first run: the lock is the catalog's sibling, so it is takeable before the catalog exists | see S-CNC-LOCK-REL | FIXED — closes D/5's mkdir-then-write-pid window |
| 46 | **S-CNC-LOCK-REL** | new criterion | the acquiring step is the releasing step | a SIGKILLed holder cannot run its own release, so a lock whose target pid is not alive is stale BY DEFINITION and any run may remove it — no trap required | THIS ROW IS THE COUNTERPART: release on the success path, on every failure path, and before any HALT | FIXED — was E/4 (a trap does not run on SIGKILL, and a HARDSTOP is a kill) |
| 47 | **S-CNC-READ** | new criterion | readers are covered by the same lock, or read a git commit instead of the working tree | a reader on the first run, before the catalog exists, reads nothing and takes no lock | the reader's lock is released by the same reader | FIXED — was B/L9 (pass 1's enumeration was writer-only) |
| 48 | **S-CNC-PENDING** | new criterion | written at 6, read only at run end; the filename derives from the node path | no proposals ⇒ the directory may not exist, which is not an error | the staged proposal is either committed or explicitly discarded at run end | FIXED — was D/12 ∥ F/11 |
| 49 | **S-RUNEND** | new criterion | run end is NOT A STAGE, so (a) has no W→R answer; the honest substitute is to name the ACTOR (the top orchestrator) and the TRIGGER (the assembly approval is recorded) | if the human never answers HG2 the approval is never recorded, the run has no end, and catalog-pending/ stays staged. STATED, not bounded | run end's own counterpart is the lock release | PARTIAL+DECLARED — was D/18. The unbounded wait is real; bounding it needs a timeout mechanism that is out of scope |
| 50 | **S-DEP** | new criterion | the child dependency DAG is written into plan.md by 2 and read at 4 and 7 | leaf ⇒ no children ⇒ no DAG and no cycle; the execution order is that one leaf — stated | no acquire | FIXED |
| 51 | **S-DEP-ORDER** | new criterion | stage 7 emits the Execution order section from the per-node DAGs stage 2 wrote | one node ⇒ a one-line order. the composition rule (a child's whole subtree is one unit in its parent's order) is what makes the per-node DAGs compose to a total order over the leaves | no acquire | FIXED — was B/L17 |
| 52 | **S-DEC** | new criterion | elc is self-declared in plan.md by stage 2 | a node that declares no elc: DEC has no operand and cannot trip — the same shape as depth 1, and it must be recorded rather than assumed to be 0 | no acquire | FIXED |
| 53 | **S-DEC-DEGEN** | new criterion | same producer | this row IS the degenerate case: depth 1 has no grandparent, so DEC cannot trip | no acquire | FIXED |
| 54 | **S-IGM** | new criterion | the config author writes mode and ingest_source before stage 1 reads them | no mode key ⇒ the default is fresh, an explicit default rather than an error (unlike redteam_context, whose absence IS an error — the difference is that a default is safe and a vacuous check is not) | no acquire | FIXED |
| 55 | **S-IGM-CLOSED** | new criterion | stage 1 copies the source to plan.md.ingested immutably, before 2 and 3 read it | fresh mode: the file does not exist, and its absence is NOT a missing closed-set input — else stage 3 deadlocks in fresh mode | the copy is immutable; nothing to release | FIXED — was B/L14 |
| 56 | **S-CLOSED-DEGEN** | new criterion | this row IS the producer-ordering fix. the parent plan's producer is the PARENT's stage 2 (absent at the root, always); child seams come from this node's stage 2 (absent at a leaf, always); carried-forward findings come from <node>/decisions.md, WHOSE FIRST WRITER IS STAGE 5 — after stages 3 and 4 read it | root has no parent plan; a leaf has no child seams; a first pass has no carried-forward findings. Without this carve-out the charter's "a record missing any of these = un-run" makes EVERY FIRST PASS AT EVERY NODE un-run — including this hardening loop's own reviews | no acquire | FIXED — was D/1, a live defect, and the operand-with-no-producer class in its purest form |
| 57 | **S-TPL3** | new criterion | the proposal is staged at 6 and committed at run end | no proposal ⇒ no commit and no lock | the staged proposal's counterpart is the commit or an explicit discard | FIXED |
| 58 | **S-RST** | new criterion | the root node's location is fixed by stage 1's run-level setup | n=1: tree/root/ is the only node and is still a node like any other | no acquire | FIXED |
| 59 | **S-RST-RESUME** | new criterion | stage 7 writes assembled-plan.md; the top orchestrator records plan/assembly-approval.md AFTER the human answers, so the terminal fact is written LAST | THE DEGENERATE CASE THIS ROW EXISTS FOR: artifact PRESENT + approval ABSENT. Under bare stage-done-iff-output-exists that state reads as "stage 7 done" and HG2 never re-fires. The named exception makes it "not done" and the resume step is the HG2 ask itself | the ask's counterpart is the recorded approval or a recorded bounce | FIXED — was D/6, closed with the same explicit degenerate-case pattern that closed BIND's root case |
| 60 | **S-SPN** | new criterion | the heading comes from the seed skeleton (stage 1 instantiates) and is read by 3 | all 6 measured §4 sites carry the identical spelling, and 4 wrong spellings are swept to absence corpus-wide | no acquire | FIXED |
| 61 | **S-SLOT** | new criterion | the slot heading ships in all three seed skeletons, so stage 1's instantiation carries it into every plan.md | a config with no required_sections: the slot is present and empty, which is visible — that is strictly better than an absent slot, and it is the reason the heading is unconditional | no acquire | FIXED |
| 62 | **S-HG2** | new criterion | the human answers; the top orchestrator records the answer AFTER the presentable artifact exists, and the terminus reads it | see S-HG2-DEGEN for the single-leaf case | the gate is released by the recorded approval; a bounce re-opens the named nodes at stage 2 | FIXED — was B/L1 |
| 63 | **S-HG2-DEGEN** | new criterion | the presentable artifact is written by 7 (decomposed) or by 2 (single-leaf tree/root/plan.md), both before the terminus | THE CARVE-OUT, generalizing BIND's root carve-out per R4: HG2 applies to WHICHEVER artifact is presentable, so a leaf-only run reaches the gate and can pass it. This is the mode this hardening loop runs itself in | no acquire | FIXED — was B/L1 |
| 64 | **S-HG2-MARKER** | new criterion | the approval is recorded by the top orchestrator after the human answers | restart: the run-complete marker is the APPROVAL, never the existence of assembled-plan.md | no acquire | FIXED — was B/L4, and S-RST-RESUME is the resume step that makes it operative |
| 65 | **S-HG2-LIMIT** | new criterion | the limitation is text at all 7 measured HG2 sites — the union of the assembled-plan and top-level-ONLY anchors | a run with the human present rather than delegated: the approval is still agent-RECORDED, so the limitation holds at every multiplicity | no acquire | FIXED — was F/2. Pass 2 stated it at 2 of 4 sites; the site set is now measured, not chosen |
| 66 | **S-HG2-NOSELF** | new criterion | CO-OCCURRENCE row, not an obligation row: it cannot force the text to be written anywhere. What it forbids is the phrase "self-approved" appearing in any file that does not also carry the duty-not-property sentence | at baseline "self-approved" occurs 0 times, so the row measures 0 sites and FAILS there under the vacuous-site guard — which is exactly why the guard was added | no acquire | FIXED — this is the half a positional row cannot express |
| 67 | **S-HG2-ONLY** | new criterion | text at all 4 measured "top-level ONLY" sites, plus a corpus-wide absence sweep on the now-false phrase "human gate on the top-level split ONLY" | n=1: no decomposition, so the decomposition gate never fires while HG2 still does — the two gates are separated precisely so this case is stateable | no acquire | FIXED — R2's consequence (b) |
| 68 | **S-XPM** | new criterion | both operands (the presentable artifact and the two gate facts) are produced before the terminus | single-leaf: see S-HG2-DEGEN. the pinned clause is SHORT because it must be true at 9 measured sites | no acquire | FIXED |
| 69 | **S-COV-PROD** | new criterion | each node's gate state is written by 5 and read by 7 | empty tree: no nodes, so the conjunction over nodes is vacuously true and there is nothing to assemble — stated at s7 | no acquire | FIXED — was D/3's fixable half |
| 70 | **S-COV-LIMIT** | new criterion | no producer: this row STATES the absence | stated at all 4 measured coverage sites, so the gap is visible wherever total coverage is claimed | no acquire | DECLARED GAP — the seam-union half needs F1's up-flow (deferred by R1). Named at every site rather than fixed |
| 71 | **S-IDGREP** | new criterion | the grep command is text | the -w flag removes HARDSTOP but not ON TOP OF, which is why S-IDGREP-CAV pairs with it | no acquire | FIXED |
| 72 | **S-IDGREP-CAV** | new criterion | text | the phantom class is enumerated and its exclusions are REPORTED by ruleid-sitemap.sh's phantom ledger, not silently dropped | no acquire | FIXED |
| 73 | **S-DESC-HG2** | new criterion | the description is frontmatter, written by this cycle's edit | the anchor "self-checking loop for PLANNING" measures exactly 1 file, so this row cannot drift to another site | no acquire | FIXED — item 12: the corrected description measures 997 chars against the 1024 cap, and quick_validate.py passes |
| 74 | **S-CHARTER-PROV** | new criterion | the blockquote is text, and it is handed to every cold reviewer VERBATIM | the fork-provenance anchor measures exactly 1 file (stages/charter.md), so the claim cannot be satisfied elsewhere | no acquire | FIXED — was A/F6: this cycle edits carried core bullets, so a blockquote saying "DROPPED: nothing" without recording what is ADDED lies to every reviewer |
| 75 | **S-BIND-GATEART** | new criterion | approved_root_plan_sha256 is written by the approval's author; sha256(tree/root/plan.md) is computed over a file stage 2 wrote | no decomposition ⇒ no approval needed ⇒ vacuously satisfied, stated | no acquire | FIXED |
| 76 | **S-F5-LIMIT** | new criterion | no producer: this row STATES the residual defect | stated at all 6 measured topgate sites | no acquire | DECLARED GAP — TOP remains defeatable because stage 1 still pre-creates plan/topgate/. F5's mechanism is deferred by R1; the limitation ships stated |
| 77 | **S-HG2-AUTHORED** | new criterion | this cycle's edit | the bounce route is stated once, at the 3 measured collate sites, and labelled NOT ratified | no acquire | FIXED — RAT2 discipline applied to this cycle's own authoring choice |
| 78 | **S-HG2-FWD** | new criterion | this cycle's edit; the constraint binds FUTURE work | stated at the 3 measured collate sites so a later bottom-up rework cannot silently delete the only whole-plan reader | no acquire | FIXED — R2's consequence (c), recorded as a forward constraint |
| 79 | **S-DEC-CANT** | new criterion | no operand — this row states what DEC CANNOT detect and reassigns that duty to GRN's validation in the adversarial pass | a mis-estimated elc at any depth is invisible to DEC, so the honest statement is depth-independent | no acquire | FIXED |
| 80 | **S-CNC-UNCOV** | new criterion | no producer: this row states an unsupported configuration | two runs sharing one run_root is a config error rather than a race to guard — the declared-uncovered case, kept declared | no acquire | OK (declared uncovered, deliberately) |
| 81 | **S-IDGREP-NAME** | new criterion | text | the two pre-existing violations (DEC, TOP) are named as declared debt rather than exempted silently; new IDs get no grandfathering | no acquire | FIXED |
| 82 | **closed-input-set** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | the five operands and their producers: this node's plan.md (2), its decomposition + child seams (2), the config's redteam_context (config author), THE PARENT NODE'S PLAN (the parent's stage 2 — absent at the root, always), and CARRIED-FORWARD FINDINGS in <node>/decisions.md WHOSE FIRST WRITER IS STAGE 5, i.e. AFTER stages 3 and 4 read it | root: no parent plan. leaf: no child seams. first pass at any node: no carried-forward findings. All three are now "not a missing input" by S-CLOSED-DEGEN. Without it the charter's "a record missing any of these = un-run" makes every first pass un-run at every node | no acquire | FIXED — the live defect D/1 named. Pass 2 applied this exact carve-out to plan.md.ingested (row 17) and nowhere else |
| 83 | **stage-done-iff-output-exists** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | the writer is whichever stage owns the deterministic output | empty node dir = "not planned yet". ONE NAMED EXCEPTION: stage 7, whose done-ness is the recorded assembly approval, not the existence of assembled-plan.md (S-RST-RESUME) | a partial file is not the deterministic name and is overwritten by the clean re-dispatch | FIXED — was D/6 |
| 84 | **path-validation** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | the path LIST comes from the config author; the CHECK runs at stage 1 and again at every later spawn (S-PATHVAL), and its result is recorded in <node>/decisions.md | an ABSENT redteam_context key makes the check pass over zero paths — the vacuity is now a config error that stops the run (S-CTX-VAC) | no acquire | FIXED — both halves: the check has a producer AND its vacuous case is an error |
| 85 | **catalog-pending** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | written at stage 6, read only at run end; one file per node path so N concurrent proposers cannot collide (S-CNC-PENDING) | no proposals ⇒ the directory may not exist, which is not an error; the first proposer creates it | the staged proposal is committed or explicitly discarded at run end, under the lock, which is released on every path | FIXED IN SCOPE — pass 2 recorded this as a cycle-3 carry-forward and left the surface unguarded |
| 86 | **run-end** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | RUN END IS NOT A STAGE, so there is no W→R answer to give. Named instead: ACTOR = the top orchestrator; TRIGGER = plan/assembly-approval.md being recorded | if the human never answers HG2, the approval never exists, the run has no end, and catalog-pending/ stays staged indefinitely. S-RUNEND states this rather than pretending a bound exists | the lock taken at run end is released on the success path, on every failure path, and before any HALT | PARTIAL+DECLARED — was D/18. The unbounded wait is inherent to adding a human gate with no timeout; a timeout is new mechanism, out of scope |

VERDICT TALLY: DECLARED GAP       3
VERDICT TALLY: FIXED              64
VERDICT TALLY: OK                 15
VERDICT TALLY: PARTIAL+DECLARED   4
ROWS EMITTED: 86   (generated row set: 86; authored answers: 86)
SWEEP: OK — the row set is generated and every generated row is answered (totality enforced, not asserted)

### 1.1 What the sweep found — **the tally is generated too**

Pass 3's first draft of this section **typed** the verdict counts and got them wrong (typed 55/20/4/4;
measured 64/15/4/3). A tally that is typed is a tally that drifts, so `gen-sweep-table.sh` now emits it:

```
$ oracles/gen-sweep-table.sh | grep -E 'VERDICT TALLY|ROWS EMITTED|SWEEP:'
VERDICT TALLY: DECLARED GAP       3
VERDICT TALLY: FIXED              64
VERDICT TALLY: OK                 15
VERDICT TALLY: PARTIAL+DECLARED   4
ROWS EMITTED: 86   (generated row set: 86; authored answers: 86)
SWEEP: OK — the row set is generated and every generated row is answered (totality enforced, not asserted)
```

**UNANSWERED: 0 — enforced by the joiner, not asserted.** The 4 `PARTIAL+DECLARED` rows are `COV`, `ORC`,
`S-RUNEND` and `run-end`; the 3 `DECLARED GAP` rows are `CMP` (empty `required_sections`), `S-COV-LIMIT` and
`S-F5-LIMIT`. `S-CNC-UNCOV` is counted `OK` because *two runs sharing one `run_root`* is declared
**unsupported** rather than left as an unguarded race — a deliberate label, noted here so the tally is
readable rather than merely correct.

**Rows whose verdict changed from pass 2:** every one of the 21 baseline IDs (pass 2 had rows for 6 of
them), plus the 5 no-ID predicates (pass 2 had rows for 0 of them). **That is the under-generalization R4
names, measured rather than argued.**

**Three rows carry a defect that was live when this pass started:**
- **`closed-input-set` (row 82) — the sharpest.** The charter says *"a record missing any of these = the
  review is treated as un-run"* over a five-member closed set, and **three of the five cannot exist** in the
  ordinary case: the root has no parent plan, a leaf has no child seams, and **a first pass has no
  carried-forward findings because `<node>/decisions.md`'s first writer is stage 5 — after stages 3 and 4
  read it.** Unfixed, that makes **every first pass at every node un-run, including this hardening loop's
  own reviews.** `S-CLOSED-DEGEN` carves out all three and names the ordering fact. Pass 2 applied this
  exact carve-out to `plan.md.ingested` and **nowhere else** (D/1).
- **`stage-done-iff-output-exists` (row 83) / `RST` (row 19).** One named exception, or HG2 is bypassed by a
  crash (D/6 — item 9).
- **`catalog-pending` (row 85).** Pass 2 recorded this as a cycle-3 carry-forward and left an N-writer
  shared surface with no naming scheme; it is fixed here (`S-CNC-PENDING`) because it is the same class as
  the lock.

---

## 2. The edits, fix by fix

`1.5-criteria.md` §1 pins the exact sentence each site must carry and **generates** the site set. This
section states the substance. **No site list in this section is hand-selected**; each cites the anchor whose
measurement produced it.

**D1 · BIND** — a record is current iff `sha256(<node>/plan.md)` computed **now** equals the
**dispatcher-recorded** `plan_sha256`. The operand is **dispatcher-recorded, not reviewer-reported** — the
exact fix IDN already applies to identity, generalized one field over (B/L6). The reviewer's own reported
hash stays as corroboration; a divergence is itself a finding. **The parent clause is dropped** (§4.1 of the
spec): one operand, no cascade, no root special case. **Stale ⇒ un-run ⇒ re-run that pass**, whose fresh
record overwrites the file. **Immutable** = the author never edits a recorded hash. **Rebind chains are
transitive and unbounded**, and **each rebind entry is itself dispatcher-recorded** (D/10 — pass 2 applied
the dispatcher fix to `plan_sha256` and left the rebind chain revalidatable by the constrained party's own
signature). **Gate artifacts:** `APPROVAL.md` carries `approved_root_plan_sha256`, and **TOP's F5
limitation is stated at all 6 measured topgate sites.**
*Anchors:* `sha256` (ch s3 s4) · `un-gated` (S s5 s7 s8) · `plan/topgate` (M S s1 s6 s8 tp/decomp).

**D2 · IDN** — dispatcher-recorded `spawn_id`; the asymmetry stated **in both directions**;
`unavailable-by-harness` + declared-degraded; the sibling-read ban.
*Anchor:* `3 independent cold agents|three separately-spawned` (M S ch s3 s4).

**D3 · RES** — three arms; five gate states; all three clean states assemble; each assembled section carries
its state + `fixed_findings` + `demoted_findings`. The circularity is closed at all **8 measured**
`clean-or-resolved` files by a deliberately **short** clause pointing at RES's definition — a long sentence
is not honestly repeatable at eight sites, and `S-RES` carries the long form at its defining site.

**D4 · CTX** — first-class `redteam_context:`, priority-ordered; de-conflated from `off_limits_paths`;
**absent/empty ⇒ a config error that stops the run**, because path-validation over an absent key checks zero
paths. **D4a · path-validation** additionally gets a producer and a record: it runs at run start **and at
every later spawn**, and the checked list plus its result go in `<node>/decisions.md`.

**D5 · OFL** *(subtractive)* — `off_limits_paths` is a **prompt-level convention, not an enforced fence**:
nothing intercepts a write, and **nothing catches a stray write to a path the config never declared**. A real
fence must come from outside this skill. *"Naming is the fence"* is swept to absence.
**D5a (F/7):** the overclaim must not be *reintroduced* by another edit — the absence sweep is corpus-wide,
so a row that re-adds it fails the whole family, which is the structural fix for pass 2's delete-then-re-add.

**D6 · PRV** — the subtractive half at all **4 measured** overclaim files; the canonical sentence is
*"The gate raises the cost of shipping a hole. It does not certify its absence."* **The positive half ships
only with its limitation attached at the same site:** what the gate establishes is **attested by the
reviewers themselves and sampled**, not independently proven; tier (iii) asks for a **negative no finite
review can prove**; and **N same-model instances are not N independent minds**, so their blind spots are
**correlated** — and whether frame diversity narrows that is **unsettled by this skill**.

**D7 · SPV** — the spot-verify duty is **stage 5's**, with a stated sample size (≥1 per record, ≥2 per pass),
recorded in `<node>/decisions.md`; a fabricated citation makes that record **un-run**. Replaces
*"whoever consumes the review checks"*, which assigned it to nobody.

**D8 · CNC** — the serial/parallel declaration; `index.md` **derived**, with `template used` routed to the
node's **own `plan.md` header** (stage 1, its only writer); the per-node gate log `<node>/decisions.md` with
`plan/decisions.md` reserved for run-level events; the **catalog lock done properly** — an **atomic symlink
whose target is the holder's pid** (lock and owner in one indivisible step, closing D/5's window), **beside**
the catalog so a first run can take it, **released by the acquiring step on success, on every failure path
and before any HALT**, **self-breaking when the target pid is dead** (a SIGKILLed holder cannot run a trap),
**readers covered**, and **`catalog-pending/` given a per-node naming scheme** so N proposers cannot collide.
Stage 8's false *"no single global cursor"* goes. The declared-uncovered case (two runs, one `run_root`)
stays declared.
**Honest limitation (F/10, F/13):** for `index.md` and the gate logs the guard is **not a lock** but a
reduction to **one writer**. That closes the write-write race and leaves **read-during-write** open, and the
quiescence trigger it would need is deferred F1. `_status.md`'s writer is likewise deferred, so
*"reduced to one writer"* is **not** claimed of it.

**D9 · DEP** — an edge per dependent child pair; a **cycle is a blocker**; stage 7 emits
`## Execution order`; the **composition rule** is stated.

**D10 · DEC/`elc`** — self-declared, not computed; **one** trip condition with the operand readable
**within ECON**; **undefined at depth 1**, stated; and what DEC **cannot** detect reassigned to GRN.

**D11 · IGM** — `mode: fresh | ingest-and-complete` (+ `ingest_source`); immutable copy to
`tree/root/plan.md.ingested`; the spine→locus **mapping table** with `ABSENT` rows as candidate holes; no
silent authoring; `architect-authored` marking; and the file added to the deterministic-filename list **and**
the closed input set, **with its absence in fresh mode stated as not a missing input**.

**D12 · TPL3** — stage-and-propose into `catalog-pending/`; commit **only** at run end, **only** by the top
orchestrator, **only** under the lock, **only after a cold review of the proposed diff**. And **`run end` is
named for what it is** — not a stage but the top orchestrator's last step, triggered by the recorded
approval — **with the consequence stated: if the human never answers, the run has no end.**

**D13 · RST** — root pinned to `tree/root/`; both departures from the approved record **declared**; **and
the resume exception (item 9)**: stage 7 is done **iff** `plan/assembly-approval.md` exists.

**D14 · SPN** — one canonical string, `Outputs & artifacts (with their locations)`, at all **6 measured** §4
files, with 4 wrong spellings swept to absence. *The matcher must flatten wraps* — `SKILL.md:18-19`'s
heading is genuinely wrapped mid-phrase at baseline, so normalization is load-bearing, not decorative.

**D15 · seed slots** — the identical `## Layer-2 required sections (from the config's required_sections)`
heading in **all three** skeletons (anchor: `Seed skeleton…`, which measures exactly those three files).

**D16 · HG2 + XPM** — the second human gate at assembly, with **the carve-out**, **the split fact**, **the
resume step**, and **the honesty seam at every site**: the run-complete marker is the **approval**;
TOP's "ONLY" narrowed to **decomposition** gates at all **4 measured** sites while preserving the
anti-gate-fatigue half; XPM's both-gates clause at all **9 measured** terminus files; *"never
self-approved"* shipped **only** in its duty-not-property form, enforced from both directions; the bounce
mechanics **marked as this cycle's authoring choice, not ratified**; and the **forward constraint** that any
future bottom-up assembly preserve a whole-assembled-plan reader.

**D17 · ID hygiene** — `grep -rnow` over the full corpus; the phantom caveat **plus the ledger that reports
exclusions**; the naming rule with its family stems and its two **declared grandfathered** violations; index
rows for `TPL1`/`TPL2`/`SEV` **and every new ID**; `IGM` not `ING`; `KLB` reserved, not `KIL`.
**F/15, recorded not fixed:** `SKILL.md:103-104`'s mnemonic-ID list is a **stale closed list** governing the
standing self-check. Updating it is in scope (D17 adds the new IDs); making it self-maintaining is not.

**D18 · charter fork-provenance** — the blockquote records what Architect's fork now **ADDS** to the carried
core, so it stays true for the reviewers who read it verbatim.

---

## 3. Measurement + instrumentation — **all of it built and executed before this document existed**

| Instrument | What it does | Executed status |
|---|---|---|
| `oracles/lib-corpus.sh` | the corpus pin, **one literal list**, so `changes/` cannot enter | in use by every oracle |
| `oracles/gen-expected-sites.sh` → `expected-sites.txt` | **generates** R1's ID→file expectation from the tree | 21 rows, matching `0-baseline.md` B2; 2 phantoms reported |
| `oracles/ruleid-sitemap.sh` | R1: MISSING / UNEXPECTED, **exit 1**; **phantom ledger always printed** | clean ⇒ 0; erosion ⇒ 1; drift ⇒ 1 |
| `oracles/criteria.tsv` + `checklib.py` + `check.sh` | positive per-site assertion; **measured** sites; **polarity guard**; **vacuous-site guard** | 60 NEW+COOC / 8 PRESERVE rows |
| `oracles/ere-probe.py` | tunes an anchor **against the measurement** instead of guessing | used for every anchor in `criteria.tsv` |
| `oracles/gen-criteria-table.sh` | emits §1 of `1.5` with the **SITES column generated** | `ROWS EMITTED: 68`, `CRITERIA-TABLE: OK`; mutation ⇒ `VACUOUS-NEW`, exit 1 |
| `oracles/gen-preserve-counts.sh` → `preserve-counts.txt` | **generates** each PRESERVE row's baseline site count | 8 rows, generated against the materialised baseline |
| `oracles/baseline-replay.sh` | **the can-fail self-test for the whole family** | `REPLAY: OK` — 60/60 NEW+COOC fail, 8/8 PRESERVE pass, 0 wrong either way |
| `oracles/idcollide.sh` | the ID naming rule, with **named** exemptions | OK on this cycle's ids; exit 1 on `KIL`/`ING` and on planted `TOPGATE` |
| `oracles/lockrace.sh` | the **executed** lock race incl. the H4 unguarded control | `ALL 4 CASES PASS`; control fails unguarded (45/120 lost) |
| `oracles/gen-sweep-rows.sh` + `sweep-answers.tsv` + `gen-sweep-table.sh` | §1's row set **generated**, the join **enforced** | 86/86; both mutations exit 1 |
| `fixtures/X{1,2,3,4}` | 4 clusters × 2 arms × **2 spawns** = **16** | PENDING BUILD (they run at stage 8) |

## 4. Concurrency (ST2b) — accessors enumerated, **readers included**

The operative rows are §1's `S-CNC-*` family plus D8. Pass 1's enumeration was **writer-only and
undercounted** (B/L9). The **measured** accessor sets: `index.md` has **11 hits across 5 files**, the gate
log **18 across 9**. For `index.md`, `_status.md` and the gate logs the guard is **not a lock** — the
accessor set is reduced to **one writer** — with the read-during-write residual declared (D8). The **only**
lock is the catalog, and its scope covers **six** paths: mid-run writes, run-end writes, concurrent runs, the
**first-run seed**, **readers**, and **`catalog-pending/`**. **`S-CNC-LOCK` is gating and executed** — the
lock is real code, and `lockrace.sh` proves the H4 control fails without it.

## 5. Thresholds → routing

Route on the **reviewer's** severity (SEV3); contest only via a logged entry; **demoting a blocker or major
requires the human tie-break** — under RAT3 that is a **HALT + verbatim relay**, never taken by this runner.
**blocker → stage 1 · major → stage 2 · minor → fix in place · nitpick → log.**

**CAP/SEV4 accounting for this pass, stated up front so it cannot be quietly reinterpreted.** Cycle 2's cap
tripped on class **β** (*the apparatus cannot detect a bad build, and the document says it can*) and **R6
released it for pass 3 only**. Therefore:
- **A class-β finding against pass 3 is a genuine second bounce on a released cap** and is a
  **stop-for-human**, relayed verbatim. It is not re-argued.
- **A class-α finding in a section pass 3 claims to have swept is a genuine bounce** (R4's remedy was
  executed here, so "the reviewers didn't look there" is unavailable as an excuse).
- **A class-α finding in a section pass 3 has NOT swept** would be under-generalization under R4 — but pass 3
  claims to have swept **all 86 rows**, so this category should be empty. **If a reviewer finds a 6th no-ID
  predicate, that is the honest exception**: it is the residual §1 declares, not a hidden bounce.

All criteria are **gating**. The only legal dispositions for an unverifiable one are a representative harness
or a **named risk-acceptance**; under RAT3 the remaining move is **HALT + relay**. **No "declared deferral"
exists in this plan.**

## 6. Risks

| Risk | Contingency |
|---|---|
| **A 6th predicate with no rule ID** | **Not mitigated by any generator, and said so.** §1 declares it; stage 3 is given it as a named task. This is the honest top risk |
| A pinned string is pinned to text that is *wrong* | `check.sh` is **not** a semantic oracle — the pinned strings **are** the text. The stage-3 reviewers are the guard on meaning, and `1.5` §4 says so |
| **A generated file is hand-edited** | SC6: re-running each generator must reproduce its output byte-for-byte modulo the timestamp line |
| 18 files × the new ID set → cross-file contradiction | SC5's recorded per-ID rubric; R2's totality; R3's collision check |
| The corrected description stops triggering | SC1 + SC2, **measured** (997 chars, all four triggers present, `quick_validate.py` clean) |
| 27 chars of description slack is thin | Declared as a known tightness, not a defect. No criterion enforces a reserve |
| An oracle passes at baseline | `baseline-replay.sh` gates the whole family; a row that passes there is `verified = no` |
| **16 arms + 8 oracle mutation sets + 4 lock cases is real runway** | If an arm cannot run, its criterion is `verified = no` and this runner **HALTs and relays** — never folded into "done" |
| The `<node>/decisions.md` partition half-migrates | A CHANGE row with a **measured** 9-file site set, asserted positively per file |
| **The build is 18 files of dense cross-referenced prose and has not started** | Sequenced definitions-first (§0); `check.sh` is runnable after each file, so a half-migration is caught during the build rather than at gate 7 |
