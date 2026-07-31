# Behavioural fixtures — hardening cycle 2

Four clusters, each a **holed / intact pair**. Every fixture is a tiny fabricated **Architect run tree**
(not a copy of this repo). At stage 8 each arm is handed to a **separately-spawned cold agent** together
with **only** the relevant *new* stage text and a required output form; the arms never see each other or
the other arm's fixture.

**Pass condition (CORRECTED in pass 3 — item 7; the RULE was fixed, not the fixture).** Each arm must
return **the verdict this table declares for that arm**, and **the two arms of a cluster must differ**.
Both arms the same verdict ⇒ `verified = no`, whichever verdict it is.

> **Why the rule changed rather than the fixture.** Pass 2's blanket condition was *"holed ⇒ blocking and
> intact ⇒ proceeding"*, which **auto-fails X3**: X3's polarity is deliberately inverted (its
> `holed`-named arm must **proceed** and its `intact`-named arm must **block**), because IDN's two rules
> are asymmetric. Renaming X3's arms would have made the blanket rule true again while **hiding the one
> asymmetry the cluster exists to test** — an agent that pattern-matches *"holed ⇒ block"* would then
> pass. So the per-arm expected verdict is now **declared per cluster in this table**, and the blanket
> sentence is gone. *(Reviewer E/3, second half.)*

| Cluster | Criteria | `holed` is | must verdict | `intact` is | must verdict |
|---|---|---|---|---|---|
| **X1** | S-BIND | `tree/root/branch-a/completeness/A.md` reports a `plan.md` sha256 that does **not** match the `plan.md` on disk (a `0000…` stale value) | records stale ⇒ node **un-gated**, **do not assemble** | every reported hash matches; **and the root record reports no parent hash at all** (the carve-out case) | **gated clean ⇒ assemble**, incl. the root |
| **X2** | S-HG2, S-XPM, **SC3** | `assembled-plan.md` exists, every node's 3+3 records exist, `tree/root/decisions.md` says `gate: clean`, `plan/topgate/APPROVAL.md` present — and **no `plan/assembly-approval.md`** | **HALT + relay for human review**; do not present / exit plan mode | identical **plus** `plan/assembly-approval.md` recording the owner's verbatim approval + a durable source | **present / exit plan mode** |
| **X3** | S-IDN, S-RES *(polarity deliberately inverted)* | three records whose **`spawn_id` is `unavailable-by-harness`** and whose passes are **declared degraded** — i.e. three identical **self-reports** | **NOT un-run** — declared degraded, the pass **proceeds** | three records carrying the **same dispatcher-recorded** id `a7f3c9b1d0e2a4c68` | **un-run** (one agent asked three times) |
| **X4** | S-CTX, S-CTX-VAC, S-IGM | a Layer-2 config with **no `redteam_context` key** — **plus a complete `tree/root/plan.md`**, added in pass 3 so the blocking verdict is not over-determined by an absent plan tree (E/15) | **config error ⇒ stop the run** (HALT) | the same config **plus** a priority-ordered `redteam_context` and `mode: ingest-and-complete`, with an ingest mapping table whose §3/§4/§6 rows are **`ABSENT`** | **proceed**; and every `ABSENT` row is flagged as a candidate hole, **not silently filled** |

**Why X3's polarity is inverted.** In X1/X2/X4 the holed arm must block. In X3 the *holed*-named arm must
**proceed** and the *intact*-named arm must **block**, because IDN's two rules are asymmetric: three
identical **dispatcher-recorded** ids mean one agent was asked three times (un-run), while three identical
**self-reports** — including three *"unavailable"* — are not evidence of anything and must never make a
pass un-run. An agent that pattern-matches "holed ⇒ block" fails this cluster, which is the point.

**Shared design notes.**
- Both X3 arms also carry `tree/root/node-x/`, whose gate log records a **demoted major** plus two
  fixed-in-place findings and a `rebound_from`/`rebound_to` pair — that is S-RES's per-item question
  (*"is this node's state distinguishable from clean at assembly, and what is it?"* → `clean-demoted`).
- X1's `plan.md` files use the **canonical §4 heading** so the fixture does not accidentally test S-SPN.
- X2's `assembled-plan.md` carries an **`## Execution order`** section and per-node `[gate: …]` +
  `fixed_findings` / `demoted_findings` headers, so the arm also observes S-DEP and S-RES incidentally
  (recorded as incidental, **not** counted as their verification).
- Hashes in X1 were computed with `sha256sum` at fixture-build time, so an agent can re-compute and
  confirm them independently — the arm is a **real** hash comparison, not a story about one.

## Give-aways removed in pass 3 (both were demonstrated by reviewer E, not hypothesised)

| # | Give-away as pass 2 shipped it | Removed how | Verified by |
|---|---|---|---|
| **E/16** | X3's three `holed` records each carried the line `**Pass status:** DECLARED DEGRADED — …`, i.e. the record **transcribed the verdict the arm is asked to derive** | the line is **deleted** from `X3/holed/tree/root/completeness/{A,B,C}.md`; the arm must now derive *declared degraded* from the `spawn_id: unavailable-by-harness` value alone | `grep -n 'Pass status' X3/holed/tree/root/completeness/*.md` ⇒ **no output** |
| **E/15** | X4's `holed` arm had **no `tree/` at all**, so a blocking verdict was over-determined — *"there is no plan tree"* blocks for a reason that is not the rule under test | `X4/holed/tree/root/plan.md` **added** (a complete 7-section node, fresh mode, so `plan.md.ingested` is legitimately absent). The only decision-relevant difference between the arms is now the missing `redteam_context` key | `diff -rq X4/holed X4/intact` ⇒ the configs differ, the plan nodes differ by mode, and `plan.md.ingested` is intact-only |

**Declared confound, not hidden:** X4's two arms differ in `mode` as well as in `redteam_context`, because
the cluster tests **both** S-CTX-VAC and S-IGM. Both differences are rules under test; neither is
incidental. X1/X2/X3 each have exactly one decision-relevant difference.

## Spawn accounting (item 7 — reconciled against what is on disk)

**4 clusters × 2 arms × 2 spawns per arm = 16 spawns.** `1.5-criteria.md` §5 said *"3 clusters / 12
spawns"* while `X4/` was on disk and `fixtures/README.md` said *"Four clusters"*; four gating rows cited
an unscheduled arm. The count is now derived from the directory listing rather than typed:

```
$ ls -d X*/                 -> X1/ X2/ X3/ X4/            (4 clusters)
$ ls -d X*/*/ | wc -l       -> 8                          (8 arms)
$ echo $((8 * 2))           -> 16                         (2 spawns per arm)
```
