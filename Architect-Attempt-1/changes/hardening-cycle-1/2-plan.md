# Stage 2 — Plan (PASS 2)

Pass 1 is at `2-plan.v1-superseded.md`. This pass keeps the fixes' *direction* (the reviewers endorsed it)
and rebuilds their *mechanics* around `PRD`: **no predicate without a producer.**

## 0. Shape

One coherent edit: 19 existing files + 2 new paths. The Tier-1 fixes are inseparable — they all read one
artifact (`_status.md`) and one predicate (subtree-complete). Sequenced **definitions → charter → new
stage → referencing stages → router → templates/examples → config → live-copy sync**, so a reference never
precedes its definition.

**Three design principles, each earned from a gate-4 finding:**
1. **Remove the failure mode, don't guard it.** The runner cannot write `APPROVAL.md` because the path is
   **fenced**; `index.md` needs no lock because it is **derived**; "did the seam change" needs no judgment
   because it is a **hash**.
2. **Prefer induction to recursion.** A direct child's `subtree: complete` is *trusted* because its owner
   ran the same predicate. This is what makes ECON true rather than asserted (pass 1's recursion made the
   root's check an O(tree) walk — the very ECON violation the fix claimed to close).
3. **An unavailable audit surface is declared, never fatal.** Pass 1's "3 identical `spawn_id`s ⇒ un-run"
   made gating impossible when the field was unavailable. Degradation is **declared in the record**.

---

## 1. `PRD` ASSIGNMENT TABLE — every fact, its producer, its reader *(required section)*

`W` = the **only** writer permitted. Single-writer-per-file is what makes the concurrency story a
partition, not a lock.

### 1a. `<node>/_status.md` — writer: **that node's own owner, only**

| Fact | Written by | Trigger | Read by |
|---|---|---|---|
| `node`, `owner`, `owner_dispatch_seq` | **stage 1** | node dir creation | join, restart walk |
| `template` | **stage 1** | template match/create-new decided | derived `index.md`, TPL3 |
| `stage` | **every stage** | on entry | restart walk |
| `granularity: leaf\|decompose\|undecided` | **stage 2** proposes → **stage 6** finalizes | draft / granularity execution | DEC, derived `index.md`, assembly |
| `elc` (self-declared int) | **stage 2** | draft | DEC at the child's stage 6 |
| `plan_sha256` | **stage 2** on every `plan.md` write; **stage 5** on a RES(a) rebind | plan written / rebind | BIND at 5, 6.5, 7 |
| `seam_sha256` = `sha256(normalize(§3 + the decomposition seam table))` | **stage 2** on every `plan.md` write | plan written | **parent's** stage 6.5 (SEAM reopen test) |
| `gate: un-gated\|clean\|clean-fixed-in-place\|clean-demoted\|blocked-<sev>\|killed` | **stage 5** | gate routed | join, assembly, `PRV` |
| `fixed_findings[]` | **stage 5** | a RES(a) fix-in-place | assembly header, rebind audit |
| `demoted_findings[]` (`<id> demoted by <name> per <durable source>`) | **stage 5** | a human tie-break demotion | assembly header |
| `rebound_from[] / rebound_to` | **stage 5** | a RES(a) rebind | BIND (the discriminator) |
| `escalation: <question verbatim>` | **stage 5** | a blocker / cap tie / missing config unresolvable here | parent's stage 6.5 → relay |
| `subtree: incomplete\|complete\|killed\|escalated` | **stage 6 (LEAF branch)**, **stage 6.5 (DECOMPOSE)**, **stage 5 (→`escalated`)** | see §2 | parent's join, assembly |
| `children.<c>.dispatched_at`, `.dispatch_seq` | **stage 6** | immediately **before** dispatching `<c>` | this node's join (dead test) |
| `children.<c>.declared_seam_sha256` | **stage 2** (initial) / **stage 6.5** (on accepting a re-plan) | own plan written / reopen resolved | SEAM reopen test |
| `children.<c>.subtree` (observed) | **stage 6.5** | each poll | subtree-complete |
| `children.<c>.killed_handled_at` | **stage 6.5** | the parent re-drafts + re-gates after a kill | subtree-complete (KLB) |
| `rollup` | **stage 6** (leaf) / **stage 6.5** (decomposing) | terminal status written | parent (ECON surface) |
| `catalog_request` | **stage 6** | a TPL2/TPL3 proposal staged | top orchestrator at run end |
| `updated` | every write | every write | restart walk |

### 1b. Every other fact

| Fact / file | Written by | Trigger | Read by |
|---|---|---|---|
| `<node>/plan.md` | **stage 2** (that node's owner) | draft / re-draft | passes 3-4, BIND, assembly |
| `<node>/completeness/{A,B,C}.md`, `<node>/adversarial/{A,B,C}.md` — **IMMUTABLE once written** | **stages 3 / 4** (the dispatching owner writes the record; the reviewer's output is embedded verbatim) | pass completes | stage 5, BIND, assembly |
| `reviewed_context_sha256{}` (path→hash map) **inside** a record | **stage 3/4**, from the reviewer's own report | record written | **BIND** at 5, 6.5, 7 |
| `spawn_id` **inside** a record | **stage 3/4** — the **dispatcher** records the id it observed at spawn | spawn returns | `IDN` at stage 5 |
| `frame` + the **embedded verbatim prompt** inside a record | **stage 3/4** | dispatch | `DIV` at stage 5 |
| `<node>/decisions.md` (per-node gate log) | **stage 5** (that node's owner) | every gate | CAP, carry-forward, rebind audit |
| `<node>/rebind/<n>.md` (cold rebind audit) | **stage 5** | a RES(a) rebind | BIND / `RES` |
| `<node>/_join.md` (**stage 6.5's deterministic output**) | **stage 6.5** | join clears | restart walk (stage-done for 6.5) |
| `<node>/_seamcheck.md` | **stage 7** | assembly of a decomposing node | assembly |
| `<node>/_assembled.md` | **stage 7** (that node's owner) | its subtree assembled | its **parent's** stage 7 |
| `<node>/_killed.md` — `killed_at`, child path, why, **authority** (tie-break name, or the relayed owner answer verbatim + durable source), the gate not passed | **stage 5** (the killed node's owner) or the **parent** if the node never existed | kill decided | parent's stage 6.5 |
| `tree/<…>/_orphan-<name>/` (archived child dir) | **stage 2** | a re-draft drops a declared child | restart walk + assembly **skip** `_orphan-*` |
| `index.md` — **DERIVED, never authoritative** | **top orchestrator only**, by walking the tree | on demand | humans |
| `plan/decisions.md` — root + run-level only | **top orchestrator only** | run-level events | CAP at root |
| `plan/topgate/APPROVAL.md` | **NOT the runner** — see §3 D7. Path is in `off_limits_paths` | owner approval exists | TOP predicate, auditor |
| `plan/topgate/AUDIT.md` (+ `audited_approval_sha256`) | a **single-purpose cold auditor** | at dispatch of the top split | TOP predicate |
| `plan/ABORTED.md` (+ `plan/ABORTED-AUDIT.md`) | **NOT the runner** — same authorship contract as APPROVAL | a recorded human/owner abort decision | every stage: the run ends |
| `catalog-pending/<skeleton>.md` + `PROPOSAL.md` | **stage 6** (the proposing node's owner, own file) | TPL2/TPL3 | top orchestrator at run end |
| `~/.claude/architect/templates/` (git) | **top orchestrator only**, holding `.architect-catalog.lock` | run end, after a cold review of the proposed diff | future runs |

**Nothing in §2–§3 reads a fact absent from this table.** That is the check `PRD` imposes on this plan.

---

## 2. The join, made decidable

### D1 — `_status.md` schema
The canonical key list is §1a, stated **once** in `METHODOLOGY.md` as a fenced block (so "stated once and
referenced, not re-specified divergently" is mechanically checkable) and **referenced** from stage 6.5 and
stage 8. `subtree` has **four** values; `complete`, `killed` and `escalated` are **TERMINAL**.

### D2 — subtree-complete, by INDUCTION over direct children
A node is **subtree-complete** iff:
- (a) `gate ∈ {clean, clean-fixed-in-place, clean-demoted}`, **and** every one of its 6 records is
  **BIND-current** (§D6), **and**
- (b) its own `_assembled.md` exists *(this is what orders assembly — see D12)*, **and**
- (c) for **every** child named in its **current** decomposition (orphans excluded by name):
  `children.<c>.subtree == complete` **and** `child.seam_sha256 == children.<c>.declared_seam_sha256`;
  **or** `children.<c>.subtree == killed` **and** `children.<c>.killed_handled_at == this.plan_sha256`.
- `escalated` is **terminal but NOT complete** — assembly blocks on it and it must be resolved or killed.

**Direct children only.** *Stated in the text, because it is the load-bearing reason:* a child's
`subtree: complete` was written by an owner that ran **this same predicate** over its own children, so
trusting it is trusting a check that **was run**, not a claim that was made — and that is what keeps the
predicate **O(children), not O(tree)**, which is what makes ECON *true* rather than asserted.

### D3 — Terminal-status producers (the blocker pass 1 shipped)
- **stage 6, LEAF branch** writes `subtree: complete` — *a childless node is vacuously subtree-complete* —
  after its own stage 7 has written `_assembled.md`. **This is the fix for "root + one leaf deadlocks."**
- **stage 6.5** writes `subtree: complete` for a decomposing node once (a)–(c) hold.
- **stage 5** writes `subtree: escalated` when it cannot clear the node.
- **stage 5 / the parent** writes `killed`.

### D4 — Dead vs. escalated vs. in-flight, on disk only
**Precedence rule, stated first and explicitly: a status carrying `escalation:` is NEVER dead.**
A child is **dead** iff `children.<c>.dispatched_at` is set **and** the child's `_status.md` is absent, or
its `subtree` is non-terminal **and** its `updated` predates `dispatched_at` (the dispatched owner never
wrote anything). A dead child is **re-dispatched once** (with an incremented `dispatch_seq`), then
escalated.
**After a restart there are no in-flight children by construction** — RST already says in-flight cold
agents die on shutdown — so a resuming parent re-dispatches every non-terminal child **idempotently**
(stage-done predicates make completed work a no-op). **That is the join's terminating condition, and it
needs no wall-clock budget** (the cost envelope is out of scope).
**Fencing token:** `dispatch_seq` is a monotonic integer the parent increments before each dispatch and
hands to the child; the child stamps `owner_dispatch_seq` on every write, and **a write whose
`owner_dispatch_seq` is lower than the value already in the file is DISCARDED** — the writer is a
superseded owner. This closes the 2/3-major "re-dispatch creates a second writer" finding without a lock.

### D5 — Escalation channel (`RAT3`'s missing wire)
`stage 5` writes `escalation: <question verbatim>` + `subtree: escalated` (terminal) and returns. The
parent's stage 6.5 reads it and either **resolves it within its own scope** (a seam question is the
parent's own plan → re-draft → SEAM) or **relays it verbatim upward** — recursively to the top
orchestrator, then under RAT3 to the human. **The relay may not paraphrase, summarize, or answer.**

### D6 — `BIND`, on the hashes the charter already collects
Records carry **`reviewed_context_sha256{}`** — a **path→sha256 map** for every context file read
(the charter already requires this), **including this node's `plan.md` and the parent's `plan.md`**.
A record is **current** iff
`reviewed_context_sha256[<node>/plan.md] == plan_sha256` **and**
`reviewed_context_sha256[<parent>/plan.md] == parent.plan_sha256`,
**or** the node carries a **valid RES(a) rebind record** (D11) whose `rebound_from` contains the record's
value and whose `rebound_to == plan_sha256`. Checked at **stage 5** (mismatch ⇒ record **stale ⇒ un-run**
⇒ node **un-gated**), at **stage 6.5** and **stage 7** (mismatch ⇒ assembly **blocked**).
**Records are immutable** — the author never rewrites a reported hash. *This is what makes X2 and X7 agree
on one verdict per disk state: the discriminator is the presence of a valid rebind record, not the hash.*
Restart contract amends to: **stage-done = the deterministic output exists AND, for a review record, it is
BIND-current.**
**BIND covers the gate artifacts too:** `APPROVAL.md` carries `approved_root_plan_sha256` +
`approved_root_seam_sha256`; `AUDIT.md` carries `audited_approval_sha256`. A post-approval change to the
root's split therefore **re-fires the existing human gate** (not a new one) — which under RAT3 is a
HALT + relay.

### D7 — `SEAM`: a hash, a reopen, a bounded cascade, and a real assembly check
- **Detector (mechanical, no judgment):** `seam_sha256 = sha256(normalize(§3 slice + the decomposition
  seam table))`. **Reopen fires iff `child.seam_sha256 != parent.children.<c>.declared_seam_sha256`** —
  an **equality** test on two recorded strings. The node cannot self-certify whether its own seam changed.
- **Reopen:** the parent re-drafts its seam slice, **re-runs its own two passes**, takes a new
  `plan_sha256`, and sets `children.<c>.declared_seam_sha256` to the child's new value.
- **Propagation, stated (pass 1 left it silent):** the parent's re-draft **recomputes its own
  `seam_sha256`; if that changed, its own parent reopens.** So one genuine seam change costs at most
  **O(depth)** re-gates.
- **Termination:** (i) a reopen fires only on an **actual hash change**, and re-drafting to *satisfy* a
  seam need not change the seam again, so a converging tree converges; (ii) a reopen at the same node on
  the same child pair counts as a **bounce at gate 5** under the existing **CAP**, so 2 → human tie-break
  (under RAT3, HALT + relay). **No new envelope is invented; the residual worst case is declared.**
- **While a reopen is pending** the parent **does not** re-dispatch running children; it finishes its own
  re-gate first, then resumes the join. Children handed a superseded parent plan are caught by **BIND**
  (their records bind to the old parent hash) and re-run — which is the correct outcome, not a race.
- **Assembly check (stage 7):** at each decomposing node, a **three-way comparison** — the parent's
  seam-table row for a child pair vs. child A's §3 vs. child B's §3 — recorded to `<node>/_seamcheck.md`.
  A contradiction is a **blocker**; assembly **blocked**; route to the parent's stage 2. **Why a self-run
  check is legitimate here (stated, because it is the obvious objection):** it is a **mechanical diff of
  three already-cold-reviewed artifacts**, not a fresh quality judgment. Where the comparison cannot be
  decided mechanically, the owner **raises it as a finding** — the ambiguity *is* the finding, never a
  clean verdict.

### D8 — `KLB` (killed) + the abort, both with authorship contracts
`_killed.md` records **`killed_at`**, the child path, why, the **authority**, and the gate not passed. The
parent records `children.<c>.killed_handled_at = <its own plan_sha256 at the re-gate>` — so D2(c) compares
**two recorded strings**, never an implied event order (pass 1's sha256 "post-dates" test was not
disk-computable). If the parent **cannot** re-draft without the child, it escalates — it does not abort.
**`plan/ABORTED.md` gets the SAME authorship contract as `APPROVAL.md`:** authored only on a recorded
human/owner decision (under RAT3, only after a relay whose answer is recorded verbatim with a durable,
fetchable source the runner did not author); content = the killed subtree, the authority, the gate not
passed; **a runner-authored `ABORTED.md` is VOID** and the correct action remains HALT + relay; it is
cold-audited at `plan/ABORTED-AUDIT.md`. *Without this, the F6 fix installs a dissolve-any-gate button.*

### D9 — `TOP`, with the admissible author stated POSITIVELY
- Stage 1 **does not create** `plan/topgate/`, and says so explicitly.
- `plan/topgate/` **and the cited owner-source locus are listed in `off_limits_paths`** — the run may not
  write there. *The runner cannot forge the approval because the path is fenced.*
- Deterministic filename **`plan/topgate/APPROVAL.md`**; **one canonical predicate sentence**, repeated
  verbatim at all five TOP sites: *dispatch of the top-level split is blocked until
  `plan/topgate/APPROVAL.md` exists, binds to the current root `plan_sha256` + `seam_sha256`, and passes
  the approval-record audit.*
- **Content contract:** (i) the split as presented (children + seam table), verbatim; (ii) the **owner's
  response verbatim with a durable locus the auditor can independently fetch and read**; (iii) a mapping
  showing those words approve **this** split.
- **ADMISSIBLE AUTHOR, positively:** *`APPROVAL.md` may be written by **any party other than the runner** —
  the owner directly, or an orchestrator/intermediary acting as **transcriber** — **provided** the record
  cites a **durable locus in the owner's own exchange** that the runner did not author and that the
  auditor can **independently fetch and confirm the quote in**. An orchestrator-written record **with** a
  real fetchable owner locus is **admissible**; one **without** is **VOID**, and dispatch stays blocked.*
  That distinction is the whole content of the fix — pass 1 said only who may *not* write it, which is the
  exact ambiguity F5 was defeated through.
- **The RAT1 clause pass 1 dropped, restored:** *a **partial or adjacent** owner answer is **not** an
  approval — the axis is **re-asked**, never resolved into the runner's own recommended split.*
- **Cold audit** at `plan/topgate/AUDIT.md`: a single-purpose cold auditor **fetches the cited locus**,
  confirms the quote appears there, confirms the mapping selects **this** split, and reports the
  `audited_approval_sha256`. Cost: one agent, once, at the top split only.

### D10 — `IDN`: a dispatcher-recorded audit surface, with a declared-degraded fallback
`spawn_id` = **the identifier the dispatcher observed at spawn** (recorded by the orchestrator into the
node's own `decisions.md` and copied into the record's provenance). `self_reported_identity` is a separate
**optional corroboration** field. **Three identical *dispatcher-recorded* ids ⇒ one agent asked three
times ⇒ un-run.** **Three "unavailable" *self-reports* are NOT evidence of one agent** (this run's own
reviewers: 2 of 3 reported "unavailable"), and if the harness exposes **no** dispatcher id at all the pass
is **declared degraded in the record** — never un-run, because an unavailable audit surface is a
limitation to declare, not a reason no plan can ever gate.
**Sibling-read ban:** the closed input set **excludes** the node's own `completeness/` and `adversarial/`
dirs for same-pass agents; the adversarial pass receives completeness findings **only** via the
orchestrator's carried-forward quote in the node's `decisions.md`; a record citing a sibling record is
**un-run (contaminated)**.

### D11 — `RES`: "resolved", in three arms, with immutable records and a cold check
(a) **minor/nitpick fix-in-place** may re-bind **without** a full re-pass iff: traceable to a **specific
reviewer finding ID present in the node's `decisions.md`**; the diff logged; `_status.md` records
`rebound_from` ∪= {old hash}, `rebound_to = new hash`, `fixed_findings`, `gate: clean-fixed-in-place`;
**and one single-purpose cold agent confirms the diff lies within the cited finding's scope**
(`<node>/rebind/<n>.md`). *The cold check is what moves satisfaction off the runner — the same logic D9
accepts for TOP; without it, RES(a) is an author asserting its own compliance, which is the defect class
this whole change exists to close.* **At most 2 rebinds per pass-generation**; a third forces fresh passes.
(b) **blocker/major** — **not** resolvable in place; routes to stage 2; BIND forces fresh passes.
(c) an author edit **no reviewer asked for** is a **re-draft**, not a resolution.
**Distinguishable at assembly:** `gate` distinguishes `clean` / `clean-fixed-in-place` / **`clean-demoted`**
(F10's second half — a *demoted* blocker/major now has a value and a `demoted_findings` list naming who
demoted it and the durable source), and each assembled node's header carries its gate state + both lists.

### D12 — Bottom-up assembly, ordered, actor named at every altitude
Each node's **own (sub-)orchestrator** runs its stage 7: it writes `<node>/_seamcheck.md` (if
decomposing) and `<node>/_assembled.md` from its own `plan.md` **plus its children's already-written
`_assembled.md`** — never grandchildren's internals. Because `_assembled.md` is **part of the terminal
condition** (D2b), a child cannot report `complete` before its own section exists, which is what
**orders** the bottom-up walk (pass 1 had no ordering guarantee). The **top orchestrator** concatenates
its own children's `_assembled.md` into `assembled-plan.md`.
**A mid-tree stage 7's GBP scope is its OWN SUBTREE**; the whole-tree check is retained **only at the
root** — stated, because whole-tree scope at mid-tree would make bottom-up assembly impossible under ECON.
**Orphans:** a child dir not in the **current** decomposition is archived as `_orphan-<name>/` at the
re-draft (with a `decisions.md` entry), and **both the restart walk and assembly skip `_orphan-*`**.

### D13 — `DIV`: frames with disjoint mandates AND disjoint inputs
**Completeness pass:**
- **A — spine-anchored.** Input: the node's plan + the config's `required_sections`. Mandate: name every
  spine + Layer-2 section and cite coverage. **Forbidden from tier (iii).**
- **B — differential.** Input: the node's plan + **a section list this plan-type did NOT declare**.
  Source order: (1) config `differential_section_sets`; (2) another plan-type's `required_sections` in the
  catalog; (3) **`templates/seed/section-sets/`** — real non-spine Layer-2 lists shipped for this purpose.
  **If no non-spine list is obtainable, frame B is DECLARED DEGRADED in the record and the pass is a
  2-frame pass — never silently the spine.** Mandate: which of *those* sections is load-bearing here and
  absent. **Forbidden from re-checking tiers (i)–(ii).** *This is the fix for pass 1's collapse: its
  declared default was "the seed skeletons' section sets", which **are** the 7-section spine, so frame B
  became a duplicate of frame A (3/3 major).*
- **C — executor.** Input: **the node's plan ONLY** (no config, no section list — a genuinely different
  input set). Mandate: *"you must execute this without asking the author anything — enumerate every
  question you would have to ask."* Each unanswerable question is a candidate missing section.

**Adversarial pass:** A source-anchored/factual · B failure-injection ("name the run that dies, and what
is missing to survive it") · C fidelity/settled-decision.

**Oracle for diversity is the embedded prompt, not the label** (pass 1 checked a self-declared `frame:`,
which is the same worthless audit surface F9 names): the records already embed the **verbatim prompt
given**, so the check is a **diff of the embedded prompt blocks**. Identical prompts ⇒ pass **un-run for
diversity**.
**Honest bound:** this buys **decorrelation, not independence**. **Evidence, cited in METHODOLOGY rather
than asserted:** this change's own stage-3 pass overlapped on **12 of ~80** findings, and each frame found
blockers no other frame reached — frame B alone found 4 of 5.

### D14 — `PRV`: what the gate establishes, labelled by strength
- **Mechanically checked:** records exist for both passes with the required provenance, and each is
  **BIND-current** to the text it reviewed.
- **Checked to the extent the surface exists:** the reviewers had no shared context and **disjoint
  frames** — evidenced by distinct dispatcher-recorded ids and differing embedded prompts; **not** proof of
  independent priors.
- **Sampled:** each record asserts it checked the spine + Layer-2 sections and cites coverage; the gate
  **spot-verifies a sample** (≥1 citation per record set, ≥2 per pass).
- **Attested only:** that the tier-(iii) generative sweep was run.
- **NOT established:** that no unanticipated load-bearing section remains (a **negative no finite review
  can prove**); that the reviewers' priors were independent (**N same-model instances are not N independent
  minds** — decontamination removes shared *context*, not shared *priors*); that an un-spot-checked
  citation is real.
- **The gate raises the cost of shipping a hole. It does not certify its absence.**
Frontmatter changes from "completeness is PROVEN, not asserted" to the checked-on-record claim (≈134 chars
of headroom; **S-SC1 must be run, not assumed**), and **a criterion must observe that the skill still
triggers** — the description is the trigger surface.

### D15 — the remaining Tier-3 items
**`CNC`** — declared: **parallel** = sibling sub-orchestrators + the 3 agents within a pass; **serial** =
a node's own stages. Surfaces per §1: `index.md` **derived** (top orchestrator only), `_status.md`
**single-writer + fencing token**, `decisions.md` **partitioned per node**, catalog **top-orchestrator-only
+ an exclusive `.architect-catalog.lock`** (atomic `mkdir`; holder records run-root + pid; a stale lock
with a dead pid may be broken only with an entry in **both** the breaker's `plan/decisions.md` **and** a
`BROKEN-BY` file inside the lock dir, so the victim run can see it). **First-run seed + `git init` also
takes the lock.** Stage 8's false "no single global cursor" claim is replaced: `index.md` is **derived, not
authoritative**; the per-node `_status.md` files are.
**`DEC`** — one operand: **`elc`**, a **self-declared** integer (labelled honestly as such, not
"computable"); persisted in `_status.md`; parent's value read from the parent's file. **ONE trip
condition:** two consecutive levels with `elc(child) >= 0.8 * elc(parent)`. Stated plainly: **DEC detects a
decomposition its own owner does not believe is reducing; it cannot detect a mis-estimate** — GRN's
validation duty in the adversarial pass is what covers mis-estimation.
**`XPM`** — the exit-plan-mode terminus: the presentable artifact is `assembled-plan.md` (decomposed run)
or the root's `plan.md` (single-leaf run), and exit-plan-mode is blocked by the **same GBP predicate as
assembly**.
**`IGM`** — `mode: fresh | ingest-and-complete` (default `fresh`) + `ingest_source`. Ingest copies the
draft **immutably** to `tree/root/plan.md.ingested`, writes a **mapping table** (spine section → source
locus, or **ABSENT**) into `tree/root/plan.md`; every ABSENT is a candidate tier-(i) hole; content
Architect authors is **marked architect-authored** so the critic weighs it. **Ingest may not silently
invent** an absent section.
**`DEP`** — each decomposing node declares a **child dependency DAG**; a **cycle is a blocker** at its
gate; assembly emits an **execution-order section** (topological order + parallel groups) derived
bottom-up; the templates gain a dependency column / prerequisites line.
**`CTX`** — `redteam_context` becomes a first-class contract key with priority-ordered `path`/`note`,
**de-conflated** from `off_limits_paths` (citable source vs. never-write fence; a path may be both), plus
**non-vacuous validation**: absent or empty ⇒ a **config error that stops the run**.
**`TPL3`** — stage-and-propose; committed only after a **cold review of the proposed diff**, only by the
**top orchestrator**, only under the **lock**, recorded in the run-level log.
Plus: **`SPN`** §4 canonical heading string declared once and used verbatim everywhere; **`RST`** root
pinned to **`tree/root/`**; `TPL1`/`TPL2`/`SEV` get index rows; `METHODOLOGY`'s "authoritative ID grep"
extended to `templates/` + `examples/`; IDs `KLB`/`IGM` replace the colliding `KIL`/`ING`.

---

## 3. Measurement — instrumentation this change adds (CP3)

1. **`oracles/check.sh`** — one subcommand per `S-` criterion; **positive per-site assertions**; any
   absence sweep **paired** with its positive assertion and run on **normalized** text
   (`normalize()`: strip `**`/`*`/backticks, collapse whitespace, flatten wraps). Takes a tree path, so it
   runs against either the edited tree or the baseline replay.
2. **`oracles/baseline-replay.sh`** — materializes `3771038:Architect/*` into a scratch dir and runs the
   same checker. **The oracle-can-fail self-test for the whole `S-` family**: every new-rule assertion must
   FAIL there; every preserved-rule assertion must PASS.
3. **`oracles/ruleid-sitemap.sh`** — word-boundary ID→site map **with an explicit phantom-exclusion list**
   (`ON TOP OF`, `HARDSTOP`) whose exclusions are **reported, not silently dropped**. Self-test: reports
   `stage-8` as a non-site for `TOP` and the two `ON TOP OF` hits as excluded.
4. **`oracles/idcollide.sh`** — for **every** ID in `METHODOLOGY`'s index, assert the token is **not a
   substring of any other uppercase token in the corpus**. Self-test: run against the pass-1 ID set, it
   must flag `KIL` and `ING`. *(This is the instrument that caught them; pass 1 had only a promise.)*
5. **`fixtures/X1…X8/{holed,intact}/`** — eight tiny fabricated fixtures, clustered per mechanism so one
   arm exercises several criteria via a **per-item verdict table**.

**Verification map:** `S-*`/`R*` → `check.sh` + `baseline-replay.sh`; `S-SC1` → `quick_validate.py` +
length/angle-bracket assertion; `S-SC2`/`R1` → `ruleid-sitemap.sh` + `idcollide.sh` + a recorded hand-diff
of every new ID's operative claim; `S-SC3` → line-offset **and intra-block order** assertion; `S-SC4` →
`diff -rq` **before and after** the sync; `X1…X8` → two separately-spawned cold agents per criterion.

**The X- protocol, pinned so stage 8 cannot fudge it:** each arm's agent gets (a) its fixture, (b) the
relevant **new** stage text, (c) a required output form (`VERDICT: <named option>` + the rule ID applied +
its citation, per item). The criterion passes **iff** holed ⇒ blocking verdict **and** intact ⇒ proceeding
verdict. **Both arms the same verdict ⇒ `verified = no`.** Arms are separately spawned and never see each
other.

## 4. Concurrency (ST2b) — accessors enumerated, guard scope named

| Shared state | Accessors at baseline (all four `index.md` writers now listed) | New discipline | Covered? |
|---|---|---|---|
| `index.md` | `stage-1:20`, **`stage-6:11-12`**, **`METHODOLOGY:195`**, **`templates/seed/README:14`** — every owner, in parallel | **derived**; top orchestrator only; per-node data → `_status.md` | **yes — the accessor set is removed** |
| `<node>/_status.md` | undefined at baseline | single writer + **`dispatch_seq` fencing token** (kills the re-dispatch race) | **yes** |
| `<node>/decisions.md` / `plan/decisions.md` | every owner appended one file | **partitioned**; run-level file = top orchestrator only | **yes** |
| catalog git repo | any sub-orchestrator, mid-run, **and concurrent runs**; **plus the first-run seed + `git init`** | top-orchestrator-only + **lock** (incl. the seed path); break requires an entry in the breaker's log **and** a `BROKEN-BY` file in the lock dir | **yes** |
| `plan/topgate/APPROVAL.md` | runner created the dir | runner **fenced out** (`off_limits_paths`) | **yes** |
| `_killed.md`, `ABORTED.md`, `_seamcheck.md`, `_assembled.md`, `_join.md`, `AUDIT.md`, `catalog-pending/*`, `rebind/*` | n/a (new) | each single-writer per §1b | **yes** |
| **Declared uncovered:** two runs sharing **one run-root** | — | unsupported; a **config error** | declared, not guarded |

## 5. Thresholds → routing

Route on the **reviewer's** severity (SEV3); contest only via a logged entry; **demoting a blocker/major =
HALT + verbatim relay** (owner asleep). Blocker → 1 · major → 2 · minor → fix in place · nitpick → log.
A finding that requires a **new human gate**, or lands on **F8** → **HALT + relay**. All criteria are
**gating**; a criterion that cannot be verified is `verified = no` and takes either a **named
risk-acceptance** (unavailable under RAT3 with the owner asleep — so in practice) a **declared deferral**,
recorded in `decisions.md` and the report. **CAP:** a 2nd bounce at gate 4 on the pass-1 finding class →
human tie-break.

## 6. Risks specific to this pass

| Risk | Contingency |
|---|---|
| 21 files + 15 new IDs → cross-file contradiction (highest risk) | `S-SC2`'s hand-diff of every new ID across all sites, recorded in `8-harness.md`; a contradiction is **major** → stage 2 |
| A new predicate again lacks a producer | `PRD`'s assignment table is a **required section** and `S-PRD` asserts every `_status.md` key in the canonical block has a named writing stage **at the stage file that writes it** |
| Absence sweeps silently pass | paired + normalized + the re-insertion self-test (bold + mid-phrase wrap) |
| Adding to SKILL.md's rule block displaces GBP | `PRV`/`DIV` placed **before** GBP; the closing rationale updated; `S-SC3` gains an **intra-block order** assertion |
| The softened description stops triggering the skill | `S-SC5`: a trigger check — the description must still contain the plan/design/decompose trigger vocabulary and the proactive-suggest clause |
| 16 agent arms is a lot of runway | fixtures are tiny and clustered; if an arm cannot run it is `verified = no` + **declared deferral**, never folded into "done" |
