# decisions.md — gate log for `divider-3666`

Append-only. One entry per gate.

---

**GATE 4 (plan) — 2026-07-31.** Worst finding: **blocker** (4 distinct, from two independent cold
reviewers: `3-redteam-plan-a.md`, `3-redteam-plan-b.md`). **Route: → stage 1, one bounce.**
Rationale: the reviewers were right and the loop's own iteration cap is not in play — this is the
first bounce, on a finding class (false baseline) that no rewording can recur under, because the
baseline is now re-derived from committed disk state.

Dispositions:

| Finding | Severity | Disposition |
|---|---|---|
| A-B1 / B-B1 — baseline measurement false (90 min/15 agents/"did not finish"; truth: 107 min, 13 agents, 12 reviews, 1 divider, division **returned**, 12/12 endorsement) | blocker | **Accepted.** `0-baseline.md` rewritten from `decisions.md` §"Correction to the number that triggered the ruling" and `it3/0/` on disk. The first version was captured at 14:21 while the division was in flight. The orchestrator independently issued the same correction. |
| B-B2 — frozen commit `d81bc0a` is the wrong revision; HEAD is `cf16967` | blocker | **Accepted.** Baseline and oracle control both moved to `cf16967`. Note: the working tree at first capture already held the `cf16967` contents, so the file *readings* in the spec were correct; the commit label and the behavioural numbers were not. |
| A-B2 — `common.md` §4's severity model and "findings are merged, never voted on" contradict an approve/reject split reviewer; `common.md` was on the not-touched list | blocker | **Accepted.** `common.md` §4 gains one scoping sentence. New criterion C6. |
| A-B3 — the new `redteam-split.md` never tells the reviewer it holds the `task` and the floor (that declaration is `redteam.md:11`, which it stops reading); a vacuous approval then passes every cost metric | blocker | **Accepted.** New criteria C10 (textual) and C20 (behavioural, verified by execution). |
| B-B3 — C13's 30-minute gate cannot attribute a pass: ~50 of the baseline's 107 min were serial dispatch, an orchestrator instruction | blocker | **Accepted.** Dispatch mode pinned concurrent in advance; wall clock demoted to advisory (C24); the gating metrics are rounds (C17), agents (C18) and prose lines (C19), none confounded by dispatch mode. |
| B-B4 — C16 blessed a `null` return, the iteration-1 failure shape | blocker | **Accepted.** C22 excludes `null` and `FAILED_TO_DIVIDE` explicitly and makes both a stop-for-human. |
| A — ≤6 agents forbids a second round, gating against the four-round machinery | major | **Accepted.** Threshold ≤7 (C18). |
| A — two of C4's five absence clauses are printers (those strings appear nowhere in Architect) | major | **Accepted.** Both removed rather than kept as decoration. |
| A / B — C17's restart injection creates two writers on a live file; the divider's output file already has a **second reader** (`node.md:50-51`, `divider.md:117-118` hand it up on `FAILED_TO_DIVIDE`) | major | **Accepted, and the mechanism withdrawn entirely.** The divider-level memo was a guard for a death-during-division that has not happened since checkpoint 0 landed — record 3497 excludes it. Replaced by C23, which verifies the *already-applied* checkpoint 0 by execution. |
| A / B — `redteam.md:54` "graded on precision, not volume" and `:43-44` "do not self-censor a lone observation" lost undeclared | major | **Accepted.** `:54` CARRY (C12); `:43-44` DROP, declared with its reason (a split verdict is counted, not `Union`ed). |
| B — coverage and "an unstated seam is at least major" silently lost | major | **Accepted as DROPs, now declared** in `0-baseline.md`. On the owner's instruction: 3666 enumerates the reviewer's questions exhaustively. |
| B / A — the risk-acceptance ("seam findings re-enter via the next `while` pass") over-reaches: `it3/0/divide-0.md` §5 G4/G5 report nothing carries the seam down and a planner has no upward channel | major | **Partly accepted. Not fixed here.** It is a defect in `node.md`'s seam transport, not in the split review; fixing it inside this change is the apparatus growth this run reverses. Logged below as an open finding for the next iteration. |
| B — `node.md`'s three-vs-four round contradiction (`node.md:47` says "three rounds") | minor | **Fixed in place** during the build — one stale word, inside a file this change already touches for the dispatch line. Recorded. |
| A — `2-plan.md` claimed iteration 4's task comes verbatim from `decisions.md` while a commit message says the task was never written to the ledger | major | **Checked and not upheld.** `runs/data-distiller/decisions.md` §"Run configuration" now records the task verbatim, reconstructed 2026-07-31 and declared authoritative. The commit message described the state *before* that reconstruction. |

**The one thing put to the owner rather than resolved silently:** both reviewers asked whether
3666's silence repeals 3438's *"with their findings carried foward"* while the same silence leaves
3438's *"up the attempts to 4"* standing. **Resolved by the runner with grounds** (see
`1.5-criteria.md`, last section): 3666 enumerates the reviewer's outputs positively — *"approve;
otherwise, reject with explanation"* — so the third channel is displaced by text, not by silence,
while the attempt count is not mentioned at all. Surfaced upward for the owner to overturn.

---

**OPEN FINDING carried out of this run — not fixed here.** `it3/0/divide-0.md` §5 G4: *nothing
carries the seam down*. `divider.md` says everything beneath the cut inherits the seam; `node.md`
passes only `division.first` / `division.second` to child nodes. G5: a planner has no upward
channel to object to a seam its parent fixed (`combiner.md`'s `Consensus` discards the odd plan).
Both are `node.md`/`combiner.md` defects found during iteration 3. In scope under record 3497 for
*a* run; out of scope for *this* one, whose change is the split apparatus.

---

**GATE 7 (code) — 2026-07-31.** Worst finding: **blocker** (3 distinct, from two independent cold
reviewers: `6-redteam-code-a.md`, `6-redteam-code-b.md`). **Route: fix in place → stage 8.**
Rationale: two of the three blockers were defects in *this run's own criteria and apparatus*, not
in the artifact — a criterion that gated against success and a criterion the oracle never
implemented. Those are the runner's to repair, not a rebuild. The third is escalated, below, and
does not block the run because both readings produce identical behaviour on the path the run will
take.

| Finding | Sev | Disposition |
|---|---|---|
| A-F1 / B-M4 — C22 and C23 mutually unsatisfiable: `node.md:99/110/112` rewrite `memo/0.json` after children return, so the mtime ordering C23 demanded can never hold on a run that passes C22 | blocker | **Accepted, criterion repaired.** C23 is now an observation at the moment checkpoint 0 fires, with the file contents pasted into `8-harness.md`. The apparatus was gating against success. |
| A-F2 / B-M2 — the build violates C15 (`node.md` changed) and `check.sh` implements no C15 at all, so the oracle reported PASS on a self-violation. `decisions.md`'s justification ("a file this change already touches for the dispatch line") was itself false — no dispatch line in `node.md` changed | blocker | **Accepted, and the false justification withdrawn.** `node.md` is now a **declared touched file** with its permitted diff enumerated hunk by hunk in C15. |
| B-B1 — the runner's repeal of record 3438's *"with their findings carried foward"* is unratified and asymmetric: 3438's carry-forward governs what the **divider returns**, the same clause-scope as *"up the attempts to 4"*, and 3666 is exactly as silent about both. Applied symmetrically the runner's own test preserves carry-forward | blocker | **ESCALATED TO THE OWNER — not resolved here.** See below. **The run proceeds** because on the expected path (three approvals in round 1) the two readings are behaviourally identical; they differ only on a mixed 2-of-3 outcome. `divider.md` now records **every rejection's reason verbatim**, so nothing is destroyed under either reading. |
| A-F3 — checkpoint 0's `FAILED_TO_DIVIDE` memo defeats its own escalation: the memo-read rule resumes at the top of the loop, whose only branches are null / non-empty, so a restart takes the division branch and spawns children on a `division.first` that does not exist | major | **Accepted, fixed.** One clause added to `node.md`'s memo-read rule. A real defect in one of the two never-cold-reviewed prior fixes — found because it was put in review scope. |
| A-F4 / B-M3 — C20 (no vacuous approval) is gating with **nothing in the artifact causing it**; three rubber stamps pass five of six behavioural gates | major | **Accepted, fixed in the artifact.** `redteam-split.md` now requires an approval to name the seam judged and state both halves are above the floor: *"an approval that does not say what it approved is not an approval, it is a silence."* |
| A-F5 — `redteam-split.md` told the reviewer *"anything the cut leaves undone comes back as the next task"*, which this run's own OPEN FINDING (G4: nothing carries the seam down) says is false for seam-text defects | major | **Accepted, narrowed** to *"anything the **WORK** leaves undone"*. The remedy is a sentence, not a restored sub-check. |
| B-M1 / A-F8 — the coverage lens is a declared DROP but the built file retains it, folded into question 1 | major / minor | **Accepted; the LEDGER was wrong, not the file.** Coverage is now a declared **CARRY**, on definitional grounds: halves that leave a remainder are not a split of that task, so 3666's question 1 is unanswerable without it. `0-baseline.md` corrected. |
| B-M5 — on the 2-of-3 path the rejecting reviewer's reason is produced and discarded, while `node.md:51` promises the owner "every finding standing" | major | **Accepted, fixed.** `divider.md`'s output section now requires every rejection's reason verbatim. |
| A-F7 — the divider names no output path for its three reviewers, while `common.md:70` tells them to write "to the path your caller named" — and C19/C20/C21 are read off files nothing instructs into existence | major | **Accepted, fixed.** `divider.md` now names `<run>/<node_id>/split-review-<round>-{a,b,c}.md`. |
| A-F11 / B-M3 — C17 (≤2 rounds) and C18 (≤7 agents) gate against the four-round machinery C8 preserves: a legitimate 3-round run fails two gates | major | **Accepted, criteria repaired.** C17 now asserts what the change actually fixes — **no round is re-run without a stated rejection** — and rounds/agents are reported as numbers. Re-derivation *without* rejection was the defect; re-derivation *with* one is the design working. |
| A-F6 — `~/Documents/Architect-rulings.md` still records 3438's carry-forward as live and now contradicts the built `divider.md` | major | **Deliberately NOT fixed.** Editing the owner's rulings file to match the runner's contested reading would launder the escalated question into the record as settled. It stays as it is until the owner answers B-B1. |
| B-m1 — both files overshoot their declared size targets (divider 61 vs ~40; redteam-split 63 vs ~35) | minor | **Acknowledged, targets not met.** The reviewer's own measurement is the honest one: the divider fell 118→61 lines and 1207→483 words; `redteam-split.md` fell 62→63 lines but the split reviewer's **total prompt** fell by `redteam.md`'s 54 lines. What it *asks* shrank; the file did not. Recorded rather than hidden. |
| B-m4 — a floor rejection had no route to `null` | minor | **Accepted, fixed** — one clause in `divider.md`'s review section. |
| A-F12 / B-n — `SKILL.md`'s dispatch template omitted `it<N>/` | nitpick | **Fixed.** |
| A-F9 — `common.md` §5's "flag what you could not check" has no channel in an approve/reject verdict | minor | **Not fixed.** A rejection is that channel. Recorded. |
| A-F10 / B-m2 — the `SKILL.md` serial→concurrent hunk is undeclared scope | minor | **Accepted as in-scope under record 3497 and now declared.** ~50 of the baseline division's 107 minutes were serial dispatch; that broke during the run. Reviewer B checked it independently and found it contradicts nothing (the design was always concurrent; the only recorded 529s were provider-side capacity). |

---

## ⚠ OPEN OWNER QUESTION — escalated, run not blocked

**Four independent cold reviewers across two gates raised it; the runner resolved it once and
stage-6 reviewer B overturned that resolution with a better argument.**

Record **3438**: *"up the attempts to 4, and 2/3 agreement is two of the three reviewers either
endorsing or at least not objecting to going forward with with their findings carried foward"*.

Record **3666** replaces the reviewer's instruction with *"approve; otherwise, reject with
explanation"* — and says nothing about either the attempt count or the carried-forward findings.

The runner read that silence **asymmetrically**: repealing carry-forward, preserving four
attempts. Reviewer B's objection is that both clauses live in one sentence and govern the same
thing — what the divider returns — so the same silence cannot repeal one and preserve the other.
Applied symmetrically, the runner's own test preserves carry-forward.

**What turns on it:** whether a reviewer who would keep the cut but has a real observation has
anywhere to put it. Under the runner's reading it has only *approve and lose it* or *reject and
force a re-derivation*. Under reviewer B's, the observation travels down with the sub-task.

**Why the run proceeds anyway:** on the expected path — three approvals in round one — the two
readings are behaviourally identical. They diverge only on a mixed outcome after four rounds.
`divider.md` now records every rejection's reason verbatim under either reading, so the run
destroys nothing the owner might want back.

---

**GATE 8 (harness) — pending: the run.**
