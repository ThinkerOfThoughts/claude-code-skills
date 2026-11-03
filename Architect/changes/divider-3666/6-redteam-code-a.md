# Stage 6 — cold red-team of the built change (reviewer A)

**Reviewer:** agent type `general-purpose`, model `claude-opus-5`. Cold — no shared context with
the author.

**Charter given:** `/home/zero/.claude/skills/guarded-change/stages/charter.md` (five lenses +
discipline + provenance + spot-verify + conditional position/concurrency lenses) plus
`/home/zero/.claude/skills/guarded-change/stages/stage-6.md` (mechanical-diff duty), plus the
task-specific additions quoted in the dispatch brief (six named attack surfaces; the record-3497
no-speculative-hardening constraint).

**Reviewed diff generated mechanically (ST6d).** Commands run, recorded verbatim:

```
git -C <root> status
git -C <root> diff cf16967 --stat
git -C <root> diff cf16967 -- Architect/stages/ Architect/SKILL.md
git -C <root> diff -- Architect/changes/divider-3666/1.5-criteria.md \
                      Architect/changes/divider-3666/2-plan.md
```

Untracked additions accounted separately: `Architect/changes/divider-3666/decisions.md`,
`Architect/changes/divider-3666/oracles/{check.sh,selftest.sh}`.

## sha256 of every file read

| File | sha256 |
|---|---|
| `Architect/stages/divider.md` | `848a75a8df525138c94c95f3b06e0c3902ea04511a4db1da27c3e6869e47857e` |
| `Architect/stages/redteam-split.md` | `9bf568004ec11887923d6553fe52cbd773a37853dc8cf323d244e7d8f547083b` |
| `Architect/stages/common.md` | `005063473c1ec2d99c37b98b1083bf9f3487d6eb669e946ed802558ee7b6e2f6` |
| `Architect/stages/node.md` | `c791431bf08eb6f53ae27a79206eca1f1d033256124fc862d0ceb2bd81191ed9` |
| `Architect/SKILL.md` | `3cec4cf8b1786ae773bab29d821f1e8cbc5dd178a44d01ac3212310a814891ab` |
| `/home/zero/Documents/Architect.md` | `d36e6942e64528c4a9a89fe79a1125b072264adfef9f43c7a858713ba4591594` |
| `Architect/stages/node.md` @ `cf16967` (control) | `1a41e11fd2438fc9ac4ee86f16dc97ee7656b687d33a9df749802da478a3a068` |

Also read (not hashed): `0-baseline.md`, `1-spec.md`, `1.5-criteria.md`, `2-plan.md`,
`decisions.md`, `oracles/check.sh`, `oracles/selftest.sh`, `stages/redteam.md`,
`/home/zero/Documents/Architect-rulings.md`, transcript records 3119/3402/3438/3497/3666,
`runs/data-distiller/it3/0/*`, `runs/data-distiller/it3/memo/`.

---

## Diff hunk accounting — every hunk

| # | File | Hunk | Planned? | Verdict |
|---|---|---|---|---|
| 1 | `SKILL.md` | Roles row: split reviewer → `redteam-split.md` only, "3 of them, concurrently" | yes (2-plan.md:53-56) | conforms (C5b) |
| 2 | `SKILL.md` | "Dispatch a set of siblings concurrently" paragraph replacing "Dispatch serially unless…" | **NO** — neither `1-spec.md`'s touched-files row nor `2-plan.md`'s SKILL.md section mentions it | **F10** |
| 3 | `common.md` | §4 scoping sentence | yes | conforms (C6); see **F9** for §5 |
| 4 | `divider.md` | full rewrite 118 → 58 lines | yes | conforms; see **F7** |
| 5 | `node.md` | `three rounds` → `four rounds` (line 47) | **NO** — `1-spec.md:169` and `2-plan.md:87` both list `node.md` as not touched; `1.5-criteria.md` C15 gates on its sha256 | **F2** |
| 6 | `redteam-split.md` | full rewrite 62 → 60 lines | yes | conforms; see **F4**, **F5**, **F8** |
| 7 | `1.5-criteria.md` | rewritten (51 → 90 lines) | yes | see **F1**, **F11** |
| 8 | `2-plan.md` | revised (104 → 88 lines) | yes | conforms |
| 9 | untracked | `decisions.md` | yes | see **F8** |
| 10 | untracked | `oracles/check.sh`, `oracles/selftest.sh` | yes | oracle is REAL — see below |

Hunks against `cf16967` that were committed at `a415a20` and are in scope by the recorded base:
`0-baseline.md`, `1-spec.md`, `3-redteam-plan-a.md`, `3-redteam-plan-b.md` (all read).

---

## The oracle — verdict: REAL, not a printer

Both scripts run by me, from the worktree root:

- `bash oracles/check.sh <copy-dir-of-the-five-built-files>` → **32 assertions, all pass, exit 0.**
- `bash oracles/selftest.sh` → **SELF-TEST PASS, exit 0.** Part 1: all 13 CHANGE assertions FAIL on
  the `cf16967` control (control exit 1). Part 2: all 21 CARRY line-deletion mutants fire. Part 2b:
  `C4b` and `C4e` — the two refutations that cannot fail on the control, honestly excluded from
  Part 1 with a stated reason (`selftest.sh:39-41`) — fire on insertion.

Every assertion is a positive per-site match against normalised text, and every one has been
demonstrated able to fail. I found **no printer** among the 32. The C4 absence sweep is genuinely
paired with C1–C3 positives as `2-plan.md:61` claims. This is the strongest measurement apparatus
I have seen in this project's change folders, and I want that on the record.

Gaps in coverage (not printers — simply unasserted):

- **C15 has no assertion at all** (see **F2**) although `2-plan.md:60` says *"Textual (C1–C15):
  `oracles/check.sh`."*
- C4's criterion text (`1.5-criteria.md:27`) says *"no blocker/major/minor/nitpick vocabulary"*;
  `check.sh:69-70` greps only `(blocker|nitpick)`. Defensible (major/minor are ordinary English)
  but the criterion overstates what is checked.
- C7's first return value ("a division") is unasserted; only `null` and `FAILED_TO_DIVIDE` are.

---

# Findings

## F1 — **BLOCKER** — C22 and C23 are mutually unsatisfiable; every passing run fails one of them

**Lens: logical.** `1.5-criteria.md:66` (C23, gating):

> `it4/memo/0.json` exists, holds `done:false, iter:0` and a `division` field carrying one of the
> three explicit answers, and **its mtime is before any child-node or leaf artefact in `it4/`**

`1.5-criteria.md:65` (C22, gating): node 0 *"spawns two child nodes and at least one returns."*

But the memo at `<run>/memo/<node_id>.json` is **rewritten** later in the same node's life.
`node.md:99`: *"**2. Checkpoint.** Write the memo: `{done: false, iter, task, plan, division}`"* —
and step 2 comes **after** step 1 has spawned both children and waited (`node.md:86-88, 95`). Same
path, same file.

**Failure scenario, concrete:** iteration 4 runs exactly as designed. Checkpoint 0 writes
`it4/memo/0.json` at T0. Children spawn, write artefacts into `it4/0.1/` and `it4/0.2/` at T1…Tn.
Step 2 rewrites `it4/memo/0.json` at Tn+1. At inspection, `0.json`'s mtime is Tn+1 — **after** every
child artefact. C23's mtime clause fails. If the loop reaches step 5 (`node.md:110`, `iter = iter +
1`), C23's `iter:0` clause fails too. So C22 passing **guarantees** C23 failing, and C23 can only
pass on a run that died before step 2 — which fails C22.

This is the criteria file, which this diff modified, and both criteria are gating with a declared
stop-for-human. It will halt gate 8 on a successful run.

**Remedy is a criterion edit, not apparatus:** C23 must be read off a *snapshot* taken at
checkpoint-0 time (copy `memo/0.json` the moment it first appears), or restated as "a memo with
`iter:0` and a non-empty `division` existed before any child artefact", evidenced from the run log
rather than from a live mtime.

## F2 — **BLOCKER** — the build violates gating criterion C15, and the oracle cannot see it

**Lens: factual.** `1.5-criteria.md:43` (C15, gating):

> `~/Documents/Architect.md` unchanged (`sha256`); `redteam.md`, `redteam-plan.md`, `leaf.md`,
> `combiner.md`, **`node.md` unchanged (`sha256`)**.

Measured:

```
node.md @ cf16967 : 1a41e11fd2438fc9ac4ee86f16dc97ee7656b687d33a9df749802da478a3a068
node.md built     : c791431bf08eb6f53ae27a79206eca1f1d033256124fc862d0ceb2bd81191ed9
```

`node.md:47` was changed `three rounds` → `four rounds`. `1-spec.md:169` lists `node.md` under
**"Not touched"**; `2-plan.md:87` lists it under **"Deliberately not done"**. `decisions.md:29`
records the edit as *"Fixed in place during the build — one stale word, inside a file this change
already touches for the dispatch line"* — but this change touches no dispatch line in `node.md`
(`node.md:41` still dispatches the divider on `common.md` + `divider.md`, unchanged), so that
justification is itself false.

The edit is *correct on the merits* — `node.md:47` genuinely contradicted record 3438. The defect is
that a **gating criterion was violated and three documents left asserting the opposite**, and
`check.sh` contains **no C15 assertion**, so the oracle reports `overall: PASS` on a build that
fails one of its own gates. That is the measurement apparatus certifying a violation — the exact
failure class this loop exists to catch.

**Remedy:** either revert `node.md` and re-scope, or (better) amend C15 to exempt `node.md:47` with
its reason, update `1-spec.md:169` / `2-plan.md:87`, and add the C15 sha assertion to `check.sh`.

## F3 — **MAJOR** — checkpoint 0 memoises `FAILED_TO_DIVIDE`, but a restart then silently skips the escalation and takes the division branch

**Lens: logical. This is one of the two never-cold-reviewed fixes I was asked to review (4a).**

`node.md:70-71` (checkpoint 0): *"**Memoise `FAILED_TO_DIVIDE` too.** It is an escalation, not a
failure to compute: a restart should re-present the owner's question."*

But the memo-read rule that governs restarts, `node.md:21-23`, says:

> **exists but not done** → you died after `Divisible` returned. Take `iter`, `task`, `plan` and
> `division` from it and **resume at the top of the loop**. **Do not re-derive a division you
> already have** — do not call `Divisible` at all, whichever of the three answers the memo holds.

"The top of the loop" is `node.md:78`, step 1, which has exactly **two** branches: *"Division is
null"* → leaves, and *"Division is non-empty"* → gate + spawn two children with `division.first` /
`division.second`. There is no `FAILED_TO_DIVIDE` branch inside the loop. The escalation text lives
at `node.md:47-52`, inside the `## Divisible` section, which is only reached from the **absent**
memo branch (`node.md:24`).

**Failure scenario:** node 0 exhausts four rounds; checkpoint 0 writes
`{done:false, iter:0, …, division:"FAILED_TO_DIVIDE"}` as instructed; the node dies before it
escalates. On restart the memo exists and is not done, so per `:21-23` the node resumes at the top
of the loop without calling `Divisible`. `"FAILED_TO_DIVIDE"` is not `null`, so it takes the
*"Division is non-empty"* branch, gates on a non-existent division, and spawns two children on
`division.first`/`division.second` that do not exist. The owner's question is never re-presented —
the precise outcome `:70-71` claims to prevent. Checkpoint 0 states its intent and the mechanism
above it does not implement it.

**Remedy is one clause in an existing branch, not new apparatus:** `node.md:21-23` gains *"— unless
`division` is `FAILED_TO_DIVIDE`, in which case re-present the escalation at `## Divisible` and do
not enter the loop."*

Two related checks that came out **clean**, recorded so the lens is earned: (i) checkpoint 0 does
*not* conflict with the human gate — it writes before the gate, and a restart re-enters step 1
which gates before spawning, so no double-spawn; (ii) it does *not* conflict with `SKILL.md`'s
layout — `node.md:26-28` and `SKILL.md:46-51` agree that `<run>` is `runs/<slug>/it<N>/`, and
C23's `it4/memo/0.json` matches. Note for the record: **checkpoint 0 has never executed** —
`runs/data-distiller/it3/memo/` is empty on disk, and `git log` shows the string `Checkpoint 0`
first appears in `node.md` at `cf16967`, i.e. after it3 ran. Iteration 4 is its first exercise.

## F4 — **MAJOR** — C20 is gating but nothing in the built artifact instructs the behaviour it requires; the file licenses exactly the shape C20 fails

**Lens: logical / fidelity.** C20 (`1.5-criteria.md:63`, gating):

> **No approval is vacuous.** Every approving review **names the two sub-tasks and the seam it
> judged and answers both of 3666's questions.**

`redteam-split.md:33-36` says the opposite of a requirement:

> **A one-line approval is a correct output** … If the cut is at a real joint and both halves are
> above the floor, **"approve" and a sentence saying why is the whole review.**

Nothing in the concatenated pair tells the reviewer an approval must *name* the two sub-tasks, or
must *state* an answer to question 2. Question 1 alone carries *"Name what differs on each side"*
(`:21`); question 2 (`:23-24`) carries no output instruction at all. `common.md` §6 asks only for
*"a three-line summary."*

**Failure scenario:** a reviewer returns `"Approve — the seam is real and both halves are well above
the floor."` That is *literally conforming* to `redteam-split.md:35` and fails C20 on two of its
three clauses. A run of three such reviewers passes C17 (1 round), C18 (4 agents), C19 (~200 lines),
C21 (no rejections) and C22 (children spawn) — **five of six behavioural gates** — while being the
degenerate rubber-stamp outcome. C20 is the only thing standing between a bad outcome and a pass,
and the artifact does not cause it.

This answers attack 6 directly: **yes, a bad outcome can pass**, and the mechanism is precisely this
gap.

**Remedy, one clause, not apparatus:** `redteam-split.md:35` becomes *"'approve', the two sub-tasks
and the seam you judged in one line each, and a sentence saying why, is the whole review."* That
keeps the review short *and* makes it non-vacuous — it is a specification of the one-line approval,
not an addition to it.

## F5 — **MAJOR** — `redteam-split.md:37-39` asserts to the reviewer a fact this run's own record says is false, and it retires the one split-review finding class that was ever load-bearing

**Lens: factual / fidelity.** The file's justification for the short review, `:36-39`:

> everything below this cut is planned and then red-teamed against the original task, and
> **anything the cut leaves undone comes back as the next task on the node's next pass.**

That is true for defects **in the work** — the owner's dedup example, where the merged result is
red-teamed against the parent task at `node.md:101-108`. I checked it and it holds at every node.
It is **false for defects in the seam text**, and this run's own documents say so:

- `decisions.md:41-46`, **OPEN FINDING carried out of this run**: *"`it3/0/divide-0.md` §5 G4:
  nothing carries the seam down. `divider.md` says everything beneath the cut inherits the seam;
  `node.md` passes only `division.first` / `division.second` to child nodes. G5: a planner has no
  upward channel to object to a seam its parent fixed."* Verified at `it3/0/divide-0.md:188` and
  `:197`.
- `2-plan.md:81` concedes it: *"Reviewer B contests the reach of this acceptance … some seam defects
  may not re-enter. **That is a real gap and it is NOT fixed here.**"*

So the plan knows the claim over-reaches, and the built prompt states the over-reaching version to
the reviewer **as a fact**, as the reason not to raise things. That is unratified inflation of
record 3666: the owner's worked example was about a cross-half *dedup* — work — not about a seam
contract.

**What it costs, with the citation.** The single historically load-bearing split-review finding in
this project is `it3/0/split-review-r1-a.md:175-195`, **M3 `major`** — a producer/consumer
dependency *"smuggled in through the namespace partition rather than through a file"*, where half A
cannot resolve its own write path, `locator`'s unit or `size`'s unit without reading a key §3.5
forbids it to read. The same reviewer wrote at `:20`: *"**Part 2 — do I object to going forward with
this cut? NO. I endorse this cut and I would keep [it]**"*, and at `:97-104` graded Q3 (floor)
*"clean"* and Q4 *"a real joint."*

Run that same reviewer against the **built** `redteam-split.md`: question 1 passes (real joint,
coverage fine), question 2 passes (nowhere near the floor), so `:28` compels **approve**, and there
is no channel for M3. The change therefore retires the exact finding the dispatch brief's attack 4b
names as the way the contradiction re-enters — *through mechanism, not wording*.

I am **not** asking for the self-containment sub-check back; `1-spec.md:70-81` declares that DROP
and the owner ordered it. The finding is narrower and its remedy is a deletion, not an addition:
**`redteam-split.md:37-39`'s assurance is over-broad and should be narrowed to the owner's own
case** — *"a defect in the work below the cut comes back as the next task"* — so the reviewer is not
told, falsely, that seam-text defects self-heal. Leaving the sentence as written also means the next
reader has no signal that `decisions.md`'s OPEN FINDING is live.

## F6 — **MAJOR** — `~/Documents/Architect-rulings.md` still records record 3438's carry-forward mechanism as live, and now contradicts the built `divider.md`

**Lens: factual (source-vs-artifact); ratification audit.** `Architect-rulings.md` §"`Divisible` —
four rounds, three outcomes" states:

> Agreement is about **proceeding**, not about being finished. Open findings travel down as findings
> and do not withhold it; only an objection to proceeding does.

The built `divider.md:37` replaces that with binary counting: *"**Three approvals → return the
division.** Any rejection → cut again"*, and `:43` *"the one with the most approvals, provided it
reached **2-of-3**."* There is no carry-forward channel anywhere in either built file.

I audited the ratification per the charter. Record 3438 is verbatim as quoted (transcript line 3438,
checked directly): *"up the attempts to 4, and 2/3 agreement is two of the three reviewers either
endorsing or at least not objecting to going forward **with with their findings carried foward**"*.
Record 3666 is verbatim as quoted at `1-spec.md:37-41` (checked character-for-character). **3666 does
not mention findings, carrying forward, or agreement.** The runner's resolution
(`1.5-criteria.md:76-89`) — that 3666's positive enumeration of outputs displaces the third channel
while leaving the attempt count untouched — is a *reasonable* reading and is honestly flagged
upward, so I do not overturn it.

The finding is the **drift**, not the reading: `Architect-rulings.md` is described in its own header
as the provenance authority (*"Anything that is history, justification, an owner-ruling locus … 
belongs here"*), it lives outside the repo, it was **not** in `1-spec.md`'s touched-files table, and
it now asserts a mechanism the code no longer implements. Whichever way the owner rules, one of the
two must move and neither did. The next agent that reads the rulings file will re-import
carry-forward as a live requirement.

**Remedy:** one line under that heading recording that 3666 is read as displacing the carry-forward
clause, with the escalation still open. No apparatus.

## F7 — **MAJOR** — the divider names no output path for its three split reviewers, so `common.md` §6 has no path and C19/C20 have no files to be read off

**Lens: unstated assumptions.** `divider.md:34-35`:

> Dispatch **three** cold agents **concurrently** on `common.md` + `redteam-split.md`, handing each
> the task, the granularity floor, and your two sub-tasks with the seam.

No output path. But `common.md:70` tells every dispatched agent *"Write it to the path your caller
named"*, and `common.md:21-23` tells it that a **missing argument** means *"say so plainly at the
head of your output and do the best bounded work you can."* So the very first thing three split
reviewers do is flag a missing argument — the opposite of the short clean approval this change
wants.

Contrast `node.md`, which names a path for **every** agent it dispatches: `divide-<iter>.md` (`:42`),
`leaf-{1,2,3}-<iter>.md` (`:82`), `rt-{1,2,3}-<iter>.md` (`:103`). The divider is the only dispatcher
in Architect that does not, and this diff rewrote that exact section.

**Why it now bites harder than it did before.** `2-plan.md:69`: *"Cost is read from `it4/0/` file
sizes, file counts and the divider's own record"* — that is C19 (gating). `2-plan.md:71`: *"C20 and
C21 are read off the run's review artefacts — their verdict text"* — both gating. If the reviews do
not land at predictable paths under `it4/0/`, three gating criteria are unmeasurable. In it3 the
files exist (`it3/0/split-review-r{1..4}-{a,b,c}.md`) only because a human orchestrator assigned the
names; a dispatched divider agent has no such instruction.

This is **pre-existing, not a regression** — the `cf16967` `divider.md` omitted it too — but the
measurement now depends on it. **Remedy:** append to `:35` *"…and an output path
`<run>/<node_id>/split-review-r<round>-{a,b,c}.md`."*

## F8 — **MINOR** — `0-baseline.md` and `decisions.md` declare "coverage" a DROP; the built file retains it

**Lens: factual.** `0-baseline.md:78` lists among "Declared DROPs" *"the **coverage** question"*, and
`decisions.md:27` records *"coverage and 'an unstated seam is at least major' silently lost —
**Accepted as DROPs, now declared**."* But `redteam-split.md:21-22` retains it inside question 1:

> And do the two halves cover the whole task, with no orphaned remainder?

It is also absent from `2-plan.md`'s seven-item content list for that file. The retention is
*good* — I would keep it — but the DROP list is now false about the artifact it describes, and the
DROP list is the whole regression bar (`0-baseline.md:58-59`: *"A CARRY item that stops being stated
is a regression; a DROP must be declared here or in `2-plan.md`."*). A wrong ledger is the thing that
makes the next run's baseline wrong, which is the failure this run already bounced on once.

Full CARRY/DROP audit against the built file, since the brief asked for it item by item — everything
else checks out: six lenses DROP ✓ absent; *"an unstated seam is at least `major`"* DROP ✓ absent;
self-containment sub-check DROP ✓ (residue = `:54-55`, one sentence, per C14); severity assignment
DROP ✓ absent; *"do not self-censor a lone observation"* DROP declared with reason ✓ absent;
*"graded on precision, not volume"* CARRY ✓ `:57-60`; earned-clean DROP ✓ absent; *"last reader of
this cut"* DROP ✓ — and inverted at `:36-37` (*"You are not the last line of defence"*); `redteam.md:11`
task+floor CARRY ✓ `:6-10`; `redteam.md:13-18` floor bound CARRY ✓ `:47-52`. **No silent regression
found.**

## F9 — **MINOR** — `common.md` §4's scoping sentence resolves §4 only; §5's second bullet still contradicts the new role

**Lens: logical.** Read as the dispatched pair, `common.md` + `redteam-split.md`:

§4's new sentence (`common.md:40-42`) does its job — it names the bound roles (plan reviewer,
combiner, node) and explicitly exempts *"a verdict on a proposed division"*, which matches
`redteam-split.md`'s `## Your verdict` heading. The `2-of-3` counting no longer collides with
*"Findings are merged, never voted on"* (`:58`), and the absent severities no longer collide with
*"A finding with no severity is unusable"* (`:56`). **C6 is genuinely satisfied.**

§6 is fine and is in fact a useful brevity anchor (*"a three-line summary"*), modulo F7's missing
path.

**§5 is not covered.** `common.md:66`: *"**Flag what you could not check** as unchecked rather than
accepting it silently."* A split reviewer's output vocabulary is approve/reject with an explanation —
there is no unchecked-items channel, and this bullet is the one remaining hook that invites an
enumerated list rather than a sentence. `common.md:64-65` (*"Cite or it doesn't count"*) is
compatible — question 1's *"Name what differs on each side"* **is** the citation — so §5's first
bullet is not a finding.

**Remedy:** either extend §4's exemption sentence to cover §5's second bullet, or add four words to
`redteam-split.md:31`. Small either way.

## F10 — **MINOR** — unplanned `SKILL.md` hunk reverses a stated operational safeguard with no source

**Lens: unstated assumptions.** Hunk 2 replaces

> **Use absolute paths.** Dispatch serially unless you have reason to think parallel is safe —
> three agents launched at once is the common cause of a rate-limited run.

with an instruction to dispatch siblings concurrently by default. `1-spec.md:158-167`'s touched-files
table gives `SKILL.md` exactly one change — *"Roles table: split reviewer reads `common.md` +
`redteam-split.md`"* — and `2-plan.md:53-56` likewise. This paragraph is neither.

I could not find any owner source for it in either direction: `grep -i 'serial|concurrent|rate.limit|parallel'`
over `~/Documents/Architect.md` and `~/Documents/Architect-rulings.md` returns nothing. So the
*prior* instruction was also unsourced and the reversal replaces one unsourced default with another;
the reversal is well-reasoned (`1.5-criteria.md:51-55` needs dispatch mode pinned so C17/C18/C19 are
unconfounded) and I am not contesting the merits. The finding is that it is **undeclared** — it
changes run-wide behaviour for leaves and plan reviewers too, not just split reviewers, and it
retires a stated failure-mode warning without recording that it did.

**Remedy:** add the row to `1-spec.md`'s touched-files table and a line to `2-plan.md`. Documentation
only.

## F11 — **MINOR** — C17/C18 gate against the four-round machinery C8 requires be kept

**Lens: logical. Attack 6, the "can a good outcome fail" half — yes.** C17 (`:60`) requires **≤ 2
rounds**; C18 (`:61`) requires **≤ 7 agents** = divider + two rounds of three.

`decisions.md:23` shows this argument was already run and accepted once — reviewer A moved the agent
cap from ≤6 to ≤7 because *"≤6 agents forbids a second round, gating against the four-round machinery"*
— but the round count was not reconsidered alongside it. A run in which the divider's first cut is
genuinely wrong, the reviewers correctly reject it, the second cut is also wrong, and round 3 settles
it is **3 rounds / 10 agents**: behaving exactly as C8's preserved four-round cap intends, and failing
two gating criteria. Under the old regime a rejection was rare (12/12 endorsed); under the new one,
rejection is the *designed* response to a bad cut, so 3-round runs become more likely, not less.

Cost is a spurious stop-for-human, not a bad ship, hence minor. **Remedy:** state C17/C18 as ≤ 3
rounds / ≤ 10 agents, or mark the excess advisory with the round count as the gate.

## F12 — **NITPICK** — `SKILL.md:88`'s dispatch template omits the attempt directory

`SKILL.md:88`: *"Write your output to `<ABS>/runs/<slug>/<node_id>/<name>.md`"* — no `it<N>/`,
contradicting `SKILL.md:46` (*"`<run>` in every stage file means the attempt directory
`runs/<slug>/it<N>/`"*) and `node.md:26-28`. Pre-existing and untouched by this diff, but it sits four
lines above hunk 2 and it is the template every dispatched agent is handed. If followed literally,
artefacts land outside `it4/` and C19's and C23's file-location assumptions break.

---

# Lens summary

| Lens | Verdict |
|---|---|
| **Factual** | **Issues: F2, F5, F6, F8.** Earned — sha256 measured both revisions of `node.md`; all five transcript records (3119/3402/3438/3497/3666) read directly from the harness JSONL and confirmed verbatim against `1-spec.md`; `0-baseline.md`'s numbers independently re-derived on disk (`wc -l it3/0/split-review-*.md` = 5,272; proposals 347/546/643/677; 12/12 files containing an endorsement; `it3/memo/` empty); G4/G5 confirmed at `it3/0/divide-0.md:188,197`; M3 read at `it3/0/split-review-r1-a.md:175-195`. |
| **Logical** | **Issues: F1, F3, F4, F9, F11.** |
| **Missed opportunity** | **No issue.** The change is a deletion under an explicit no-hardening constraint (record 3497); every improvement I can name is either an addition the owner forbade or is already logged as an open finding (`decisions.md:41-46`). Every remedy I propose above is a clause edit or a documentation line, none is new apparatus. |
| **Unstated assumptions & risks** | **Issues: F7, F10.** |
| **Fidelity** | **Issues: F4, F5, F6.** Terms pinned: **"natural seam"** → `divider.md:7-9` + `redteam-split.md:19-22`, a place where material / kind of work / thing produced changes — matches 3666, not a proxy. **"approve / reject with explanation"** → `redteam-split.md:28-31`, binary verdict + named failing question — matches 3666. **"maximum granularity"** → the run's `granularity` floor argument, one direction only (`divider.md:19`, `redteam-split.md:23-24`, `common.md:25-36`) — matches. **"2-of-3 agreement"** → **PROXY**: 3438 defines it as *endorsing or not objecting, findings carried forward*; the build implements *two of three binary approvals*. Flagged upward by the runner (`1.5-criteria.md:76-89`) and I do not overturn the reading, but the ratification record (`Architect-rulings.md`) still carries the old mechanism — **F6**. **"the loop handles it anyway"** → **PROXY**: pinned by the owner to a defect in the *work* (the dedup example, `Architect-rulings.md` §3666); the build generalises it to seam-text defects, which the run's own OPEN FINDING says are not transported — **F5**. |
| **Position sensitivity** (fires: prompt assembly, `redteam.md` removed from the dispatch) | **No issue beyond F9.** I read `common.md` + `redteam-split.md` as the concatenated pair a dispatched agent receives. Both rules lost with `redteam.md` are restated (`redteam.md:11` → `:6-10`; `redteam.md:13-18` → `:47-52`), and `redteam.md:54` → `:57-60`. On the rubber-stamp axis I counted five pro-approval statements (`:33`, `:35-36`, `:36-37`, `:39-40`, `:47-52`) against one balance clause — but the balance clause occupies the **final** section (`:57-60`), the strongest recency position, so the assembly is not mis-ordered. The essay risk is genuinely gone: the only remaining hook is `common.md:66` (F9). |
| **Concurrency** | **Does not fire.** No shared mutable state, no new read-modify-write window. The memo has one writer and one reader (`node.md:31`) and this change does not add an accessor. F1 concerns mtime *observation*, not a race. |

# What I could not check

- **All behavioural criteria (C16–C24).** Iteration 4 has not run; `runs/data-distiller/it4/` does
  not exist. F1, F4 and F11 are predictions about that run derived from the artifact text, not
  observations of it.
- **Whether the owner intends 3666 to repeal 3438's carry-forward clause.** Escalated by the runner
  and still open; I audited the ratification and found the reading defensible but unratified (F6).
- **Whether the prior serial-dispatch instruction (F10) traced to an owner instruction.** Absent from
  both `~/Documents` sources; I did not sweep the full 3,600-record transcript for it.
- **`stages/redteam-plan.md`, `leaf.md`, `combiner.md`** — read only for the cross-references cited
  above (`leaf.md:47`), not audited.
