# Stage 2 — Plan: how the hardening lands, how it is measured, what bounces the loop

## 0. Shape of the change

**One coherent edit, not ten independent patches.** The Tier-1 fixes are not separable: F1's join, F2's
seam reopen, F3's hash binding, F6's killed marker and F10's "resolved" all key off **one** artifact —
the **`_status.md` schema** — and off **one** predicate — **subtree-complete**. Splitting them would
ship a corpus that contradicts itself, which S-SC2 (cross-file rule consistency) correctly fails. So the
build lands as a single pass over 17 files + 1 new file, sequenced so the *definitions* land before the
*references*.

**Design principle for every fix: prefer removing the failure mode to guarding it.** Three examples that
shape the whole edit:
- **F5** — do not add a check that the runner created `topgate/` legitimately; **stop the runner creating
  it at all** and give the approval a content contract + a cold audit.
- **CNC** — do not add a lock to `index.md`; make `index.md` **derived** and give every mutable surface
  **exactly one writer**. A lock is only used where a single writer is impossible (the cross-**run**
  catalog).
- **F7 (tier iii)** — do not ask three agents to recall harder; hand one of them **another plan-type's
  section list** so the open-ended recall becomes a **diff**.

## 1. Build sequence (definitions before references)

| # | Step | Files | Introduces |
|---|---|---|---|
| 1 | **Canonical definitions** in METHODOLOGY: `_status.md` **schema** (the one canonical key list), the **subtree-complete** predicate, the canonical **§4 heading string**, `tree/root/` pinned, the run-tree diagram (`topgate/APPROVAL.md`, `catalog-pending/`, `ABORTED.md`), and the config contract (`redteam_context`, `mode`/`ingest_source`, `differential_section_sets`) | `METHODOLOGY.md` | JOIN, KIL, BIND, CTX, ING, CNC, SPN, RST, DEC(`elc`), PRV, DIV, RES, SEAM, DEP, XPM + all 13 index rows |
| 2 | **The charter** — the reviewer-facing contract: PRV honesty clause, DIV frames, IDN fields + sibling-read ban, BIND field in provenance, the spot-verify duty naming its stage | `stages/charter.md` | PRV, DIV, IDN, BIND |
| 3 | **The new join stage** | **`stages/stage-6.5-join.md`** (new) | JOIN, KIL, SEAM, BIND, RES, CNC, RAT3 escalation route |
| 4 | **The stages that reference them**, in loop order | `stage-1`, `stage-2`, `stage-3`, `stage-4`, `stage-5`, `stage-6`, `stage-7`, `stage-8` | all |
| 5 | **Router last** (it summarizes; it must not lead the definitions) | `SKILL.md` | frontmatter + rules block + Loop table + Inputs + Scale + Stop-for-human + self-check ID list |
| 6 | **Templates + examples + README** | `templates/seed/*` (4), `examples/authoring-a-skill/*` (2), `README.md` | §4 heading, Layer-2 slots, DEP column, DEC one condition, TOP predicate, `redteam_context`, PRV |
| 7 | **Layer-2 config for this cycle** | `guarded-change.architect.md` | baseline block; FINDINGS.md + LOOP-STATE.md added to `redteam_context`; `check.output` retargeted |
| 8 | **Live-copy re-sync** | `/home/zero/.claude/skills/architect` | S-SC4 |

**Position discipline (CP6):** `SKILL.md`'s up-front rules block **gains** text (PRV, DIV). Adding to a
position-sensitive assembly displaces what followed, so the build asserts S-SC3 (rule block still before
the stage table) *after* the edit, and keeps the added text **inside** the existing block rather than
appending a new block after the stage table.

## 2. The design decisions, stated so a reviewer can contest them

### D1 — `_status.md` schema (the keystone; F1/F3/F6/F10/DEC/SEAM all read it)
Canonical key list, stated **once** in METHODOLOGY and **referenced** elsewhere:
`node`, `owner`, `stage`, `gate`, `plan_sha256`, `subtree`, `children`, `elc`, `seam_rev`, `rollup`,
`escalation` (optional), `catalog_request` (optional), `updated`.
`gate ∈ {un-gated, clean, clean-fixed-in-place, blocked-<severity>, killed}`;
`subtree ∈ {incomplete, complete, killed}` — the last two **terminal**.
**Single writer:** only the node's own owner writes its own `_status.md`. That is what makes the whole
concurrency story a partition rather than a lock (see §4).

### D2 — Subtree-complete (the predicate the join and the assembly share)
A node's subtree is complete **iff** (a) the node is gated clean-or-resolved with `plan_sha256` matching
`sha256(plan.md)` **and** every review record's `reviewed_plan_sha256` equal to it (BIND), **and** (b)
for **every** child named in the node's decomposition, the child dir exists, its `_status.md` carries a
**terminal** `subtree:`, and — recursively — a `subtree: complete` child is itself subtree-complete.
A `subtree: killed` child satisfies (b) **only if** the parent has re-drafted its decomposition and
re-gated (its `plan_sha256` post-dates the kill). Purely a **disk** predicate — computable by a walk,
with no cursor.

### D3 — Blocking, and death
Stage 6.5 is where the parent **blocks**: after dispatch it polls each child dir until every child
reaches a terminal `subtree:`. **A child whose owner returned without writing a terminal `_status.md` is
DEAD, not done** — files win over any returned message (RST). A dead child is re-dispatched once, then
escalated. This is the live-reproduced failure (branch B returned while its agents ran) turned into a
predicate.

### D4 — The escalation channel (what RAT3 was missing)
A node that cannot clear its own gate writes `subtree: incomplete`, `gate: blocked-<severity>`, and
`escalation: <the question, verbatim>`, then returns that question **verbatim** to its parent. The parent
either resolves it **within its own scope** (a seam question is the parent's own plan — it re-drafts and
re-gates, which triggers SEAM) or **relays it verbatim upward**, recursively to the top orchestrator and
then, under RAT3, to the human. **The relay may not paraphrase, summarize, or answer.**

### D5 — SEAM: reopen + a real cross-node check
- **Reopen:** each node records, per child, the `seam_rev` it planned against. When a child's
  `_status.md` reports a higher `seam_rev`, the parent's seam review **reopens**: re-draft the seam slice,
  **re-run its own two passes**, take a new `plan_sha256`. A parent whose child bumped `seam_rev` and
  which did not re-gate is **un-gated at assembly** (BIND makes this mechanical, not a matter of
  diligence).
- **Assembly check:** at each decomposing node, a **three-way comparison** — the parent's seam-table row
  for a child pair vs. child A's §3 vs. child B's §3 — recorded to `<node>/_seamcheck.md`. A
  contradiction is a **blocker**; assembly is **blocked**, routed to the parent's stage 2.
- **Why a self-run check is legitimate here (stated in the text, because it is the obvious objection):**
  it is a **mechanical diff of three already-cold-reviewed artifacts**, not a fresh judgment about
  quality. Where the comparison cannot be decided mechanically (prose seams that neither match nor
  contradict), the node's owner **escalates it as a finding** rather than declaring it clean — the
  ambiguity is the finding.

### D6 — BIND: use the detector that already exists
The charter already makes every reviewer report the sha256 of each context file it read. Add a **named**
field, `reviewed_plan_sha256`, and **compare** it: at stage 5 (a mismatch ⇒ the record is **stale ⇒
un-run** ⇒ node un-gated), at stage 6.5/7 (re-verified per node; a mismatch **blocks** assembly), and in
the restart contract (**stage-done = the output exists *and*, for a review record, binds to the current
`plan.md` hash**). This is the change that makes a re-drafted node *unable* to assemble on old reviews.
**Cost:** one `sha256sum` per record per gate — negligible. **The exception, bounded:** RES(a).

### D7 — TOP, rebuilt on RAT1's discipline
- Stage 1 **does not create** `plan/topgate/`. It says so explicitly (a positive statement, so the
  absence is checkable).
- Deterministic filename **`plan/topgate/APPROVAL.md`**, named at all five TOP sites.
- **One canonical predicate sentence**, repeated verbatim: *dispatch of the top-level split is blocked
  until `plan/topgate/APPROVAL.md` exists **and** passes the approval-record audit.*
- **Content contract:** (i) the split as presented (children + seam table), verbatim; (ii) the **owner's
  response, verbatim, with a durable spot-checkable source the runner did not author**; (iii) a mapping
  showing those words approve **this** split.
- **A runner may not author its own approval.** A runner-authored or intermediary-agent-attributed
  `APPROVAL.md` is **VOID**; dispatch stays blocked; under RAT3 the runner **halts and relays**.
- **Cold audit** at `plan/topgate/AUDIT.md` by a single-purpose cold auditor that spot-verifies the
  quoted owner words against the cited source. *Rationale:* F5 and F9 are the same defect — a gate
  asserted by the party it constrains — so the fix must move satisfaction **off** the runner. Cost: one
  cold agent, once per run, at the top split only.
- **No new human gate** is created: the human gate already existed; this makes it real. (F8 — whether a
  human must also review the *assembled* plan — remains **untouched**, queued for the owner.)

### D8 — PRV: what the gate actually proves
One canonical two-halved statement, at 6 sites:
- **Proves:** a **decontaminated** review of this node occurred and is **on record**; contract tiers
  (i)–(ii) are **filled and cited**; the tier-(iii) sweep was **run and recorded**.
- **Does not prove:** that no unanticipated load-bearing section remains — that is a **negative no
  finite review can establish**. The gate **raises the cost of shipping a hole; it does not certify its
  absence.**
- Plus, plainly: **N same-model instances are not N independent minds** — decontamination removes shared
  *context*, not shared *priors*; **DIV** is what buys the marginal catch.
- **Frontmatter** changes from "completeness is PROVEN, not asserted" to the checked-on-record claim,
  keeping the description ≤1024 chars, angle-bracket-free, and still trigger-pushy.

### D9 — DIV: three frames per pass (the mechanism half of F7)
**Completeness pass:** (A) **spine-anchored** — tiers (i)+(ii) by name with coverage citations;
(B) **differential** — handed **another plan-type's `required_sections`** and asked which of *those*
sections is load-bearing here and absent (tier (iii) as a **diff**, not unbounded recall);
(C) **executor** — given the node and told *"you must execute this without asking the author anything —
enumerate every question you would have to ask"*; each unanswerable question is a candidate missing
section.
**Adversarial pass:** (A) **source-anchored/factual**, (B) **failure-injection** ("name the run that
dies, and what is missing to survive it"), (C) **fidelity/settled-decision** ("pin the loaded terms;
find a contradicted settled decision").
Each record declares its **`frame:`**; three records sharing a frame ⇒ the pass is **un-run for
diversity** (declared degraded, never silently accepted). Config supplies (B)'s section list via
`differential_section_sets`, defaulting to the seed skeletons' section sets.
**Honest bound, stated:** this buys **decorrelation, not independence**.

### D10 — IDN: an audit surface for "3 independent agents"
Provenance gains `spawn_id` (the subagent's own reported identifier), `dispatch_index` (A/B/C) and
`frame:`. Three identical `spawn_id`s ⇒ one agent asked three times ⇒ **un-run**. The **closed input set
excludes** the node's own `completeness/` and `adversarial/` dirs for same-pass agents; the adversarial
pass gets completeness findings **only** via the orchestrator's carried-forward quote; a record citing a
sibling record is **un-run (contaminated)**.

### D11 — RES: "resolved", defined in three arms
(a) **minor/nitpick** fix-in-place may re-bind **without** a full re-pass **iff** traceable to a
**specific reviewer finding**, diff logged, `_status.md` updated with the new `plan_sha256` +
`gate: clean-fixed-in-place` + the fixed finding IDs, and each affected record annotated with the
rebinding fix. (b) **blocker/major** — **not** resolvable in place; routes to stage 2; BIND forces fresh
passes. (c) an author edit **no reviewer asked for** is a **re-draft**, not a resolution. **Assembly
distinguishes** `clean` from `clean-fixed-in-place` in each node's header, with the fixed findings
listed. The text states that (a) is a **bounded, declared exception** to BIND, so the two rules do not
contradict — the alternative (a full 6-agent re-pass per typo) would make the loop unusable and push
runners to under-report minors.

### D12 — Bottom-up assembly + the named actor (F1's last two clauses, ECON's contradiction)
Each node's **own (sub-)orchestrator** assembles **its own** node into `<node>/_assembled.md` from its
`plan.md` **plus its children's already-written `_assembled.md`** — never grandchildren's internals. The
**top orchestrator** concatenates its own children's `_assembled.md` into `assembled-plan.md` at the run
root. Assembly therefore proceeds **leaves → root**, no orchestrator ever holds more than its own subtree
(ECON preserved instead of contradicted), and **stage 7's actor is named at every altitude**.

### D13 — DEP: dependency ordering
Each decomposing node declares a **child dependency DAG** (`child-b depends on child-a for <artifact>`);
a **cycle is a blocker** at that node's gate. Assembly derives, bottom-up, an **execution-order section**
at the end of `assembled-plan.md`: a topological order of leaves with **parallelizable groups**.

### D14 — TPL3, de-fanged
A catalog change is **staged as a proposal** at `<run-root>/catalog-pending/<skeleton>.md` +
`PROPOSAL.md` during the run. It is committed **only** (i) after the proposed skeleton diff has itself
passed a **cold review**, (ii) by the **top orchestrator**, (iii) holding the **catalog lock**, (iv)
recorded in the run-level gate log. Never auto-committed by a sub-orchestrator mid-run.
**Why a cold review and not a human:** the family's rule is *no AI artifact accepted without an
independent challenge* — a cold review satisfies it; requiring a human here would add a human gate,
which is not this runner's call (cf. F8).

### D15 — ING: `mode: ingest-and-complete`
`mode: fresh | ingest-and-complete` (default `fresh`) + `ingest_source: <path>`. In ingest mode stage 1
copies the draft **immutably** to `tree/root/plan.md.ingested`, then writes a **mapping table** (spine
section → where in the draft it came from, or **ABSENT**) into `tree/root/plan.md`. Every **ABSENT** is a
candidate tier-(i) hole; content Architect authors to fill one is **marked architect-authored** so the
critic weighs it rather than inheriting it as given. **Ingest may not silently invent** an absent section.

### D16 — Rejected alternatives (recorded so the red-team can contest the choice)
- **A polling budget/timeout on the join** — rejected for cycle 1: a wall-clock bound would need a
  cost/fan-out envelope, which is **explicitly out of this cycle's scope**. The dead-child rule covers
  the observed failure without inventing an unscoped budget.
- **A lock on `index.md`** — rejected: derivation removes the contention entirely (see §4).
- **A full re-pass on every minor fix** — rejected as RES(a); see D11.
- **Folding the join into stage 6** — rejected: stage 6 is already the largest stage file, and a
  separate stage number gives the join a **grep-stable name and a stage-done predicate** of its own
  (the same reason guarded-change has a 1.5).

## 3. Measurement — how each criterion is verified

**Instrumentation added by this change** (CP3 — the plan adds it, it is not an afterthought):

1. **`changes/hardening-cycle-1/oracles/check.sh`** — the structural checker. One subcommand per `S-`
   criterion, each a **positive per-site assertion** list; paired absence sweeps run over
   **normalized** text (`normalize()`: strip `**`,`*`,`` ` ``, collapse whitespace, flatten wraps).
   Exit non-zero with a per-assertion report. Run against a tree path argument, so it can be pointed at
   either the edited tree or the baseline replay.
2. **`changes/hardening-cycle-1/oracles/baseline-replay.sh`** — materializes `3771038:Architect/*` into
   a scratch dir and runs `check.sh` against it. **This is the oracle-can-fail self-test for the entire
   `S-` family**: every new-rule assertion must FAIL there, every preserved-rule assertion must PASS.
3. **`changes/hardening-cycle-1/oracles/ruleid-sitemap.sh`** — word-boundary (`grep -now`) ID→site map,
   for S-SC2 and R1. **Word boundaries are mandatory** (baseline lesson: bare `TOP` matches inside
   `HARDSTOP`).
4. **`changes/hardening-cycle-1/fixtures/X1…X7/{holed,intact}/`** — the seven execution fixtures, each
   a tiny fabricated run tree or record set. Fabricated, tiny, and **never inside a target repo**.

**Verification map:**

| Criterion | Verified by | Path exercised |
|---|---|---|
| S-F1…S-F10, S-C1…S-C10, R2 | `check.sh <name>` on the edited tree | the per-site assertion list |
| all `S-` | `baseline-replay.sh` — must FAIL every new assertion | the oracle-can-fail path |
| S-SC1 | `quick_validate.py` + description length/angle-bracket assertion | the frontmatter |
| S-SC2, R1 | `ruleid-sitemap.sh` + a recorded hand-diff of the 13 new IDs' operative claims | every ID site |
| S-SC3 | line-offset comparison in `SKILL.md` | the position invariant |
| S-SC4 | `diff -rq` live vs. source, **checked before and after** the re-sync | the live-copy path |
| X1…X7 | **two separately-spawned cold agents per criterion** (holed arm, intact arm), each handed only its arm + the relevant new stage text; verdicts recorded verbatim under `8-harness-runs/` | what a runner actually does |

**The X- protocol, stated precisely so stage 8 cannot fudge it:** each arm's agent is given (a) the
fixture path, (b) the specific new stage text, (c) a required output form ("VERDICT: <one of the named
options> + the rule ID you applied + your citation"). The criterion passes **iff** holed ⇒ blocking
verdict **and** intact ⇒ proceeding verdict. **Both arms the same verdict ⇒ `verified = no`**, whichever
it is. Agents in the two arms are separately spawned and never see the other arm.

## 4. Concurrency: accessors enumerated, and the guard's scope named (ST2b / CP7)

This change alters the **concurrency structure over shared mutable state** in the system the rules
describe, so the accessor table is mandatory:

| Shared state | Accessors at baseline | New discipline | Covered? |
|---|---|---|---|
| `index.md` | **every** node's owner writes `template:`/status (stage 1:21); all in parallel | **Derived**, not authoritative; written **only** by the top orchestrator by walking the tree. Per-node data moves to the node's own `_status.md` | **Yes — by removing the accessor set**, not by locking |
| `<node>/_status.md` | undefined (no writer named) | **Single writer**: the node's own owner only. Parents **read** children's | **Yes — single-writer partition** |
| `plan/decisions.md` | every node's owner appends (stage 5:19), in parallel | **Partitioned**: each node appends to its **own** `<node>/decisions.md`; `plan/decisions.md` = root + run-level entries, written **only** by the top orchestrator. CAP and carry-forward read the **node's own** log — which is where they were always scoped ("same gate + same node section") | **Yes — partition** |
| `~/.claude/architect/templates/` (git catalog) | any sub-orchestrator `git commit`s mid-run (stage 6:32-35) — **and across concurrent runs** | Writes funnelled to the **top orchestrator** (children request via `_status.md` `catalog_request:`), gated on a cold review of the proposed diff, and serialized by an **exclusive lock** (`.architect-catalog.lock`, created atomically via `mkdir`, holder records run-root + pid; a stale lock whose pid is dead may be broken only with a logged entry) | **Yes — single in-run writer + a cross-run lock** |
| `plan/topgate/APPROVAL.md` | runner created the dir; content unspecified | Runner **may not write it**; the human/owner supplies it; a cold auditor reads it | **Yes — the writer is removed from the runner** |
| `<run-root>/catalog-pending/` | n/a (new) | Written by the node's owner (own file per proposal, single-writer), read by the top orchestrator | **Yes — single-writer per file** |

**Left uncovered, declared:** two Architect runs sharing **one run-root** is not supported and is stated
as unsupported rather than guarded — a second run in the same run-root is a **config error**. The
cross-**project** catalog *is* guarded (the lock).

## 5. Thresholds → loop routing

Route on the **reviewer's** stated severity (SEV3); contest only via a logged `decisions.md` entry;
demoting a blocker/major needs the human tie-break — **which, with the owner asleep, is a HALT + verbatim
relay to the orchestrator (RAT3)**, never a self-granted demotion.

| Finding class | Severity | Route |
|---|---|---|
| A Tier-1 fix (F1/F2/F3/F5) is absent, un-checkable, or self-contradictory across sites | **blocker** | → stage 1 (re-spec) |
| A fix is present but its rule contradicts another rule at another site (S-SC2 class) | **major** | → stage 2 (re-plan) |
| A fix's *approach* is wrong (e.g. the join's predicate is not computable from disk) | **major** | → stage 2 |
| A Tier-2/Tier-3 fix is missing a site, or a criterion's oracle can't fail | **major** | → stage 2 |
| Wording/placement/ID-naming nits; a missing cross-reference | **minor** | fix in place, proceed |
| Style | **nitpick** | log, proceed |
| **Scope**: a finding that requires a **new human gate**, or that lands on **F8** | **HALT + relay verbatim** | owner's call, not the runner's |

**Gating vs. advisory metrics:** all criteria in `1.5-criteria.md` are **gating** — there is no aggregate
metric here to be confounded (H8 does not fire: no baseline workload, conformance-only in the metric
sense). The stage-0 baseline is a **textual** baseline, so R1/R2 are the regression checks and they are
gating.

**Iteration cap (CAP/SEV4):** 2 bounces at the same gate on the same finding class → HALT + relay.

## 6. What could go wrong with *this change* (and the contingency)

| Risk | Contingency |
|---|---|
| **Scope is too large for one clean run.** 18 files, 13 new IDs | **Partition and DECLARE** (never silently): priority order is F1/F2/F3/F5 > F4/F6/F7/F9/F10 > cheap items. A deferral is recorded in `decisions.md` **and** in the final report |
| **13 new IDs across 16 files → cross-file contradiction** (the highest-risk aspect) | S-SC2's hand-diff of every new ID's operative claim across all its sites, recorded in `8-harness.md`; a contradiction is a **major** → stage 2 |
| **A new ID collides as a substring** (the `TOP`/`HARDSTOP` lesson) | Word-boundary matching everywhere + an explicit collision check over the corpus before the IDs are committed to |
| **The absence sweeps silently pass** (a fragile matcher) | Every absence sweep is **paired** with a positive assertion and run on **normalized** text; plus S-F7's explicit re-insertion self-test with bold + a mid-phrase wrap |
| **Adding to `SKILL.md`'s rule block displaces the stage table** (CP6) | S-SC3 re-asserted after the edit; the addition stays *inside* the block |
| **The X- fixtures test my checker, not the skill** | The X- oracle is a **cold agent handed only the new skill text + the fixture** — never a script that re-implements the rule |
| **Session death mid-build** | Every record is written to disk as it is produced; the change folder + `git diff 3771038` are the resume point; `LOOP-STATE.md` is the loop's durable state |
| **A fix quietly adds a human gate** | Explicit constraint in `1-spec.md`; the stage-3 charter is told to flag it as a **scope** finding → HALT + relay |
