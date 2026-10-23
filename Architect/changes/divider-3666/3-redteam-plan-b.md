# Stage 3 — cold red-team of the plan, reviewer B

**Reviewer:** cold `general-purpose` subagent, model `claude-opus-5`. No shared context with the
author or with the parallel reviewer.

## Artifacts reviewed — sha256

| File | sha256 |
|---|---|
| `Architect/changes/divider-3666/0-baseline.md` | `813722924453ee4939dd4a5030600e2d35d7be18636b0a151212b34aa6fb648e` |
| `Architect/changes/divider-3666/1-spec.md` | `edac3f727a6af1d048106c9fab0c00630c85c8bdc2e4aa0a53cc3e6bf63aad73` |
| `Architect/changes/divider-3666/1.5-criteria.md` | `da0bb079ecd0984cfc736f128504972460ddc1ddc8663c631dcdf87c4ec601eb` |
| `Architect/changes/divider-3666/2-plan.md` | `ed42d93f0f247904ec1c9a58d6e6452632bef1170c87c785abfd9190cf8201dc` |

Context consulted: `Architect/stages/{divider,redteam-split,redteam,common,node}.md`,
`Architect/SKILL.md`, `Architect/runs/data-distiller/decisions.md`,
`Architect/runs/data-distiller/it3/0/` (all 19 files stat'd; `divide-0.md` read in full, all 12
`split-review-*.md` verdict blocks read, `split-round-1.md` head read),
`~/Documents/Architect.md` context via `Architect-rulings.md`, `~/Documents/Architect-rulings.md`,
and the session transcript JSONL (records 3610, 3628, 3634, 3666, 3497, 3486, 3438, 3402, 3119, 1258
read directly).

---

# Summary

**Four blockers.** The change's direction is right and the owner did instruct it; nothing below
argues against applying record 3666. What fails is the *evidence and the oracle*: the baseline
measurement is false on disk, the frozen commit is not the pre-change revision, the headline
behavioural criterion cannot distinguish this change from a dispatch-mode change that the run's own
ledger already quantifies, and the criterion meant to prove success is satisfied by the exact
failure that killed iteration 1.

---

# LENS 1 — FACTUAL

## BLOCKER B1 — The baseline's headline measurement is false on disk, and the run's own ledger says so in a section titled "Correction to the number that triggered the ruling"

`0-baseline.md:25-27` states, as measured fact:

> **Measured cost of one division at one node: 12:43 → 14:13 = 90 minutes, 4 divider agents +
> 11 cold split reviews = 15 dispatched agents, and it did not finish.**

`1-spec.md:5` repeats it as the problem statement: *"cost **90 minutes and 15 dispatched agents and
did not finish**"*. `1.5-criteria.md:38` hard-codes it as C13's baseline: *"Baseline: 15 agents / 90
minutes / no return."* `1.5-criteria.md:41` builds C16 on it: *"This is the thing that has never
happened in three iterations."*

**Every one of those figures is wrong.** Measured now, from the same directory:

| Claim | Artifact says | Disk says |
|---|---|---|
| Round-4 reviews | `-r4-{a,b}`, "run parked mid-round" (`0-baseline.md:23`) | **three** — `split-review-r4-c.md`, 37,581 bytes, mtime `14:22:01` |
| Split reviews | 11 | **12** |
| Divider agents | 4 | **1** — `divide-0.md:7` *"the twelve cold split reviewers **I** dispatched"*; §6 *"Files this **call** produced"* |
| Dispatched agents | 15 | **13** |
| Wall clock | 90 min (12:43→14:13) | **107 min** (12:37:13 dispatch → 14:24:35 return) |
| Outcome | "did not finish" | **finished.** `divide-0.md:18`: *"`Divisible` returns a **DIVISION** — not `null`, not `FAILED_TO_DIVIDE`."* `subtask-A.md`/`subtask-B.md` written `14:23:14`; `divide-0.md` written `14:24:35` |

The correct figures are not hard to find — they are in the run's own ledger, which is in this
change's own touched-files list (`1-spec.md:139`). `runs/data-distiller/decisions.md:229-235`:

> ### Correction to the number that triggered the ruling
> The ruling was made on a partial reading — *"~70 minutes and 8 cold reviews, round 3 of 4,
> division still unfinished."* **The division did finish**, at 14:24:35, while the messages were in
> flight. […] **107 minutes (12:37:13 → 14:24:35) and 12 cold split reviews across 4 rounds**

and `decisions.md:366-368`: *"`Divisible` **returned a division**: four rounds, twelve cold reviews,
12/12 endorsement […] **107 minutes.**"*

**Why it is a blocker, not a rounding complaint.** The mechanism is visible in the mtimes:
`0-baseline.md` was written at `14:21:20`, before `split-review-r4-c.md` (`14:22:01`) and before the
division returned (`14:24:35`). It was an honest snapshot of an in-flight run. But `1-spec.md`
(`14:22:15`), `1.5-criteria.md` (`14:23:02`) and `2-plan.md` (`14:23:45`) were written across the
window in which the division completed, and **none was corrected**, while `decisions.md` was
corrected at `14:26:19`. So the four artifacts now under review present a *superseded partial
reading* as the measured premise of the whole change, and the correction that supersedes it is
committed at `HEAD` (`cf16967`, subject line: *"iteration 3 — division COMPLETED, and the numbers
correct the ruling's premise"*).

This project's `Architect-rulings.md:134-140` §"Struck claims" records three prior instances of
exactly this failure class. **Remedy:** re-derive `0-baseline.md` from `decisions.md:223-300` and
propagate to C13, C16 and C18. This is a correction, not a hardening — it is in scope under 3497.

**One part of the baseline verifies clean, and should be recorded as such.** The endorsement claim
is not merely right, it is understated. I read the Part-2 verdict of all twelve reviews: r1-a:20
*"NO. I endorse this cut"*; r1-b:26; r1-c:17-28; r2-a:24; r2-b:23; r2-c:23-24 *"I positively
endorse this joint"*; r3-a:27; r3-b:24; r3-c:23; r4-a:19; r4-b:23; r4-c:25. **12/12, four of four
rounds, zero objections to proceeding.** `0-baseline.md`'s "3/3 endorsed" per round is correct for
rounds 1–3 and understated for round 4.

## BLOCKER B2 — The frozen commit is not the pre-change revision, so `oracles/selftest.sh` will resolve the wrong files

`0-baseline.md:3`: *"Commit at run start: `d81bc0a9863dbe33becda73c2a0c78675bf5a6a1`."*
`2-plan.md:71-72` makes that hash the oracle's control: *"Runs the same checker against the frozen
pre-change files from `git show d81bc0a:<path>`."*

`d81bc0a` is **not** the parent of this change. `HEAD` is `cf169679f7da23c95572148231f47dd0c7faf283`,
and all four files under change differ between them:

```
Architect/stages/divider.md       d81bc0a=ac25b9ae…  HEAD/worktree=ebdf30ed…
Architect/stages/redteam-split.md d81bc0a=119d00ef…  HEAD/worktree=ffeea715…
Architect/stages/node.md          d81bc0a=c64e36a8…  HEAD/worktree=1a41e11f…
Architect/SKILL.md                d81bc0a=3e560ce5…  HEAD/worktree=ffaa1a84…
```

`0-baseline.md` is **internally inconsistent on this point**: its own frozen-hash table (lines 9-12)
records `ebdf30ed…`, `ffeea715…`, `1a41e11f…`, `ffaa1a84…` — the *worktree* hashes, i.e. `HEAD`,
not `d81bc0a`. So the table freezes one revision and line 3 names another.

**The concrete failure.** The self-test is the only guard against printer assertions —
`1.5-criteria.md:5-6`: *"every assertion must **fail** on the old file and **pass** on the new one.
An assertion that passes both is a printer."* Run against `d81bc0a`, C11's assertion is validated
against a `redteam-split.md` that **does not contain the self-containment block at all**:

```
git diff d81bc0a HEAD -- Architect/stages/redteam-split.md
+   **Check self-containment explicitly, because it is the failure this question keeps missing.**
+   The two halves are planned **concurrently, blind to each other**, with no channel …
```

C11 asserts the *rewritten* one-sentence form; against `d81bc0a` it fails because the topic is
absent, not because the wording changed — the assertion is validated for the wrong reason, and could
be a printer against the real pre-change file without the self-test noticing. `1-spec.md:110`
shows the author knew of a later commit (*"already removed in commit `0d6c229`"*), which makes the
stale freeze an oversight rather than a claim, but the oracle is broken either way. This project's
history (per `~/.claude/CLAUDE.md`, Architect attempt 1) is *"twice the 'checker' gating everything
else turned out to be a bare `exit 0` printer"* — this is that failure's supply line.

**Remedy:** freeze `cf16967`, re-hash, and change `2-plan.md:71` accordingly.

## Minor F1 — "six lines above it" is off by ~55 lines

`0-baseline.md:36-37` and `1-spec.md:19-20` both say `divider.md:97-98` contradicts *"the same
file's own §'Agreement is about PROCEEDING, not about being finished' **six lines above it**"*. The
§3438 block is `divider.md:20-36`; the re-derive rule is at `:97-98`. That is ~61 lines, and the
intervening text includes the whole seam apparatus. The contradiction is real (see below) — only
the adjacency is wrong. It matters slightly because "six lines above" implies an obvious editorial
slip, whereas 61 lines apart is why nobody caught it for three iterations.

## Minor F2 — "The cost was entirely apparatus" is contradicted by the ledger and by the plan's own risk table

`1-spec.md:7`: *"The cost was entirely apparatus."* `decisions.md:251-257` measures otherwise:
*"serial dispatch accounts for roughly 50 of the 107 minutes — just under half. **The other half is
the apparatus itself**."* And `2-plan.md:94` concedes the it3 reviews found *"real defects […] seam
gaps, a termination hole"*, which is not "entirely apparatus" either. Half, and half of the
remaining half, is still a strong case; the absolute is not supported.

## Minor F3 — the spec identifies the wrong line in `node.md`

`1-spec.md:138` scopes `node.md` to *"one line, **if** the divider dispatch names the reviewer
files."* It does not: `node.md:41` dispatches *"one agent on `stages/common.md` +
`stages/divider.md`"* — no reviewer files. So that row is a no-op as written, while `node.md` **does**
carry a line that needs changing — see M7.

## THE CAUSAL CLAIM — VERIFIED, and stronger than the artifact claims

`0-baseline.md:31-34` and `1-spec.md:19-20` attribute the four re-derivations to `divider.md:97-98`.
I verified the citation verbatim (`divider.md:97-98`: *"While any `major` or `blocker` stands,
**re-derive** the split and review again."*) and I verified the causation from the divider's own
first-hand account rather than from the author's inference. `divide-0.md:64-70`:

> **Why four rounds ran despite unanimous agreement in round 1.** `divider.md` contains two
> different stopping rules and I applied both […] the **severity** rule (*"While any `major` or
> `blocker` stands, re-derive the split and review again"*) decided *whether the seam text was
> finished*.

and `divide-0.md:G1` reports the contradiction independently, as does `decisions.md:306-310` (*"the
most [significant]… divider's loop condition"*). **This is the author's story and it is also the
divider's, written before the author's, and it is right.** Not a finding — recorded because a clean
factual verdict on the load-bearing causal claim has to be earned.

---

# LENS 2 — LOGICAL / WILL THE STAGE-8 RUN DISCRIMINATE?

## BLOCKER B3 — C13's wall-clock threshold cannot attribute a pass to this change; ~50 of the 107 baseline minutes were an orchestrator dispatch instruction, and iteration 4's dispatch mode is unpinned

`1.5-criteria.md:38`, C13, gating: *"**Threshold: ≤ 6 dispatched agents and ≤ 30 minutes wall
clock** from divider dispatch to returned answer."*

`decisions.md:251-257` — in this reviewer's context set, and the change's own touched file —
measures the confound and names it:

> Serial dispatch of the three reviewers per round was the **orchestrator's** instruction, carried
> over from Wednesday's 529s — **not the design's**. 12 reviews × 7:07 = **85 minutes spent one at a
> time.** Run concurrently, each round costs its slowest reviewer […] ≈ **53 minutes**. **So serial
> dispatch accounts for roughly 50 of the 107 minutes.**

**The failure scenario is not hypothetical, it is the default.** Iteration 4 is run by whoever
executes stage 8. If they dispatch the three reviewers concurrently — the obvious thing to do, and
what `decisions.md` implicitly recommends — then even with **zero** improvement from this change,
one round of three concurrent 7-minute reviews plus a ~4-minute derivation plus the final write
lands at roughly 15 minutes. C13's 30-minute gate passes **on the dispatch-mode change alone**, and
the run is then reported as evidence that record 3666's cut worked. Conversely, if stage 8 dispatches
serially and 3666's cut works perfectly, one round × 3 × 7 min ≈ 25 min — inside the gate but only
just, so a slow reviewer fails a successful change.

Neither `0-baseline.md`, `1.5-criteria.md` nor `2-plan.md` mentions serial dispatch, and nothing
fixes iteration 4's dispatch mode. **A gating criterion whose pass/fail is dominated by an unpinned
variable the artifact never names is not a measurement.** Remedy is cheap and is not hardening: pin
the dispatch mode in `2-plan.md`'s measurement section (matching the baseline's serial mode, or
concurrent with the threshold re-derived against `decisions.md`'s 53-minute concurrent baseline),
and state which.

**Where do 6 and 30 come from?** Nowhere. Neither `1.5-criteria.md` nor `2-plan.md` derives them.
Arithmetically they are the wrong baseline run backwards through C18's 60%: 15 × 0.4 = 6, 90 × 0.33 =
30. Against the *correct* baseline (13 agents, 107 min) C18's own advisory arithmetic no longer
agrees with C13's gate: 6/13 is a 54% reduction, which **fails** C18's *"≥ 60% … on both axes"* while
C13 passes. Two criteria disagreeing about the same run is the tell that the numbers were
reverse-engineered rather than derived.

## BLOCKER B4 — C16 is satisfied by the degenerate `null`, which is the exact iteration-1 failure, and the criterion's own parenthesis blesses it

`1.5-criteria.md:41`, C16, gating: *"**The run gets past the division.** Node 0 spawns children **(or
leaves, on a `null`)** and at least one of them returns a plan or leaf output."*

**The bad outcome that passes.** A rewritten `divider.md` — 35 lines, opening with "find a natural
seam", with the four-round machinery reduced to a mention and the re-derive rule deleted — returns
`null` at node 0 on round 1: *"no seam here that leaves both halves above the floor."* Then:

- **C13 passes**, and passes handsomely: 1 divider + 3 reviewers = 4 agents ≤ 6; ~12 minutes ≤ 30.
  `Divisible` produced "one of the three answers" and "the node acts on it", verbatim as C13 requires.
- **C16 passes** by its own parenthesis: node 0 spawns leaves on the undivided task, a leaf returns
  a leaf output.
- **C14 passes vacuously** — no reviewer filed a rejection, so none filed a sub-floor rejection.
- **C15 is unmeasurable** — if the divider returns `null` without proposing a split there are no
  round-1 reviews to size. Unmeasurable is not failing, and nothing says what to do.
- **C18 passes spectacularly.**

So the change ships, verified, on a run in which **the Data-Distiller task was declared atomic and
three leaves were spawned to plan the whole skill in one pass.** That is not a hypothetical failure
mode: `decisions.md:343` records it as what iteration 1 did — *"the node now spawns three leaves on
the **undivided** [task]"* — and `divider.md:6-7` opens by naming it *"the failure that killed the
first real run"*. `0-baseline.md:47-48` lists keeping `null` and `FAILED_TO_DIVIDE` distinct as
CARRY item 1 precisely because of it.

The criteria set has **no criterion asserting that node 0's division is non-null.** C16's
parenthetical exists to keep `null` legitimate as a design answer, which is correct in general — but
at *node 0 of the Data-Distiller task*, where twelve independent cold reviewers have already
certified a real joint exists (`divide-0.md:31-46`), a `null` is a regression and the criteria call
it a pass.

**Remedy (a correction to the criteria, not a new guard):** C16 should require that node 0 return a
**division**, on the recorded ground that it3 established one exists; a `null` at node 0 is a
stop-for-human, not a pass.

## MAJOR M1 — C13's "≤ 6 dispatched agents" gates against machinery C7 requires the change to keep

Under the design in `2-plan.md:21-26`, one round costs 1 divider + 3 reviewers = **4 agents**; two
rounds cost 7. C13's ≤ 6 therefore permits exactly **one round** and fails any run that uses a
second. Meanwhile C7 (`1.5-criteria.md:24`, gating) requires `divider.md` to retain *"the four-round
cap and the after-four-rounds 2-of-3 fallback"*.

**Failure scenario:** round 1's cut is genuinely not at a natural seam; one reviewer correctly
rejects with an explanation; the divider correctly re-cuts using the reason (`2-plan.md:22`);
round 2 is unanimous. That is the new mechanism *working exactly as designed* — and it fails the
gating criterion at 7 agents. The stage-8 verdict then reads "the change did not meet its
threshold" for a run that demonstrated the change succeeding.

Note also `2-plan.md:22`: *"All three approve → return. **Any rejection** → cut again."* That is
**unanimity per round**, stricter than today's rule, and it makes the one-round budget a demand that
three independent cold agents agree on the first cut. Combined with C13 the criteria set silently
requires a 3/3 first-round approval and calls anything else a failure.

## MAJOR M2 — C15 rewards the failure mode as loudly as the success, and its second clause is unfalsifiable

`1.5-criteria.md:40`, C15, gating: *"At least **2 of the 3** round-1 split reviews are ≤ 6 KB and are
accepted rather than re-run."*

**A file-size floor does not distinguish a correct short approval from a rubber stamp.** The two
outcomes C15 cannot tell apart:

- *Success:* a reviewer reads the cut, checks both questions, finds a real natural seam above the
  floor, writes "Approve. The finding boundary is a real joint; both halves are far above the floor."
  ≈ 300 bytes. **Passes.**
- *Failure:* a reviewer skims, writes "Approve." ≈ 8 bytes. **Passes, and scores better.**

C15 is the only criterion aimed at review *quality*, and it is monotonically maximised by not
reviewing. `1-spec.md:63-65` states the real requirement correctly — *"A one-line approval must be
a correct output, **not a lazy one**"* — and C15 measures only the first half of that sentence.
Meanwhile a 7 KB review that is entirely correct fails the gate.

**And "accepted rather than re-run" can never fail.** Under `2-plan.md:21-22` an approval is
accepted by construction — there is no mechanism by which a divider re-runs an approving reviewer.
The clause that would have made C15 mean something is vacuous.

**Remedy:** C15 should be **advisory** (a size trend line, like C18), with the gating quality
question either dropped — there is no cheap oracle for it and inventing one is exactly this
project's documented pathology — or replaced by something observable: e.g. each approval names which
of the two questions it checked. Note `1.5-criteria.md:3` claims *"All criteria are **gating** unless
marked advisory"* and `:50-51` claims *"C13–C17 are verified by the real run; none is deferred and
none is checked by a proxy"* — under CH9, C15 is a gating criterion verified against a proxy (file
size for review quality) and should not carry that label.

## Minor L1 — C17's injected restart adds a dispatched agent C13 may or may not count

`2-plan.md:81-83` dispatches *"a second, fresh divider agent … on the same output path"* to verify
C17. C13 counts *"dispatched agents … from divider dispatch to returned answer"*. Whether the C17
probe counts against C13's budget of 6 is undefined, and with the budget already at exactly one
round (M1) it is the difference between pass and fail. State it.

## Minor L2 — C12 is a printer by the criteria file's own rule

`1.5-criteria.md:29`, C12, gating: *"`~/Documents/Architect.md` is unchanged … `sha256` compare."*
Nothing in the plan touches that file, so the assertion passes on the pre-change and post-change
state identically. `1.5-criteria.md:5-6` says an assertion that passes both *"is a printer and its
criterion is `verified = no`"*, and `2-plan.md:73`'s delete-the-line self-test cannot be applied to
a whole-file hash. C12 is worth keeping as a tripwire but is mislabelled gating.

---

# LENS 3 — MISSED OPPORTUNITY

## MAJOR M7 — `node.md` still says three rounds where `divider.md` says four; this broke during the run, record 3497 puts it in scope, and the plan does not fix it

`node.md:47`: *"**`FAILED_TO_DIVIDE`** — **three** rounds ran and no split reached 2-of-3
agreement."* `divider.md:102`: *"**Cap: four rounds** (owner ruling, record 3438: 'up the attempts
to 4')."* Record 3438 verbatim (transcript line 3438) is *"okay, up the attempts to 4"* — so
`node.md` is the stale one.

This is not speculative hardening: it **broke during the run being fixed.** `divide-0.md` §5 G2
reports it first-hand (*"`node.md` was not updated with the record-3438 change"*) and
`decisions.md:311` records it (*"`node.md` still says the cap is three rounds; `divider.md` says
four. Record 3438 said four."*). Record 3497 verbatim: *"fix whatever broke during the run, if
multiple things broke at once, then they should all be fixed, **along with any things that broke but
didn't take the run with them**."* This is precisely the last clause. `node.md` is already in the
touched-files list (`1-spec.md:138`) for a change that turns out to be a no-op (F3), so the cost is
one line. **No criterion observes cross-file agreement on the cap** — C7 checks `divider.md` only.

## MAJOR M4 — G4, "nothing carries the seam down", broke during the run, was closed only by the divider improvising, and the plan does not address it

`divide-0.md` §5 G4, filed independently by reviewers across rounds 1, 3 and 4:

> **G4 — nothing carries the seam down.** `divider.md` says *"Everything beneath this cut inherits
> the seam"*, but `node.md` spawns children with `(division.first, plan, granularity, …)` — **only
> the sub-task value travels.** […] **This is fixable by the divider alone** […] **but nothing in
> the apparatus says so**, and a divider that does not think of it produces grandchildren that
> re-derive item schemas and status vocabularies from nothing.

The it3 divider closed it unilaterally (`divide-0.md` §4: inlining the seam into `subtask-A.md` /
`subtask-B.md`) and said plainly that the apparatus does not require this. `decisions.md:316-318`
records it. Under record 3497 it is in scope. It is also *cheaper* after this change, not harder:
one clause in the rewritten `divider.md` §4 saying the returned sub-task strings must contain the
seam text, not a pointer to it.

**Making this worse, the change removes the only rule that policed it.** `redteam-split.md:42-43`
— *"**An unstated seam is at least `major`** — everything below the cut inherits it"* — disappears
with the four questions, and neither `0-baseline.md`'s CARRY list nor its DROP list mentions it (see
M3). After the change nothing requires the seam to be stated and nothing checks that it travels.
**Failure scenario:** divider returns "sub-task A: plan the finding pipeline. Sub-task B: plan the
corpus envelope. Seam: the finding boundary." Both reviewers approve — it *is* a natural seam and
both halves are above the floor, which is the entire test. Two children plan blind against a
three-word seam and invent incompatible run-directory layouts; `Union` (which per `combiner.md`
*"is not an author"* and *"a genuine conflict is kept, not resolved"*) concatenates them. Nothing in
C1–C18 observes it.

---

# LENS 4 — UNSTATED ASSUMPTIONS & RISKS (incl. the position lens)

The position lens **fires**: `1-spec.md:125-129` correctly identifies these files as a
position-sensitive prompt assembly and correctly identifies removing `redteam.md` from the split
reviewer's dispatch as a removal-changes-context event. The identification is right; the enumeration
under it is not complete. Rule-by-rule audit of `redteam.md` follows.

## `redteam.md` rule-by-rule classification

`2-plan.md`'s implicit claim (via `1-spec.md:127-129`) is that **only** the granularity-floor bound
needs restating. Auditing all of `redteam.md` against the plan:

| `redteam.md` | Rule | Classification |
|---|---|---|
| `:11` | *"Common to both: the **task** and the **granularity floor**."* | **Restated** — `common.md` §3 supplies the floor to any role taking `granularity`; `2-plan.md:31` restates the inputs. Clean. |
| `:13-18` | *"You are the only thing standing between this loop and infinite regress… **Do not file a finding whose only remedy is to decompose below the floor.**"* | **WEAKENED — see M5.** |
| `:20-36` | The six lenses | **Declared DROP** — `0-baseline.md:61`, C4. Clean. |
| `:38` | *"**Also in scope for every lens:** was any portion of the task left unaddressed?"* | **SILENTLY LOST — see M3.** |
| `:42` | *"'No issue found' per lens is expected. A clean lens is a real all-clear."* | **Restated and strengthened** by C2 / `2-plan.md:35`. Clean. |
| `:43-44` | *"**Do not self-censor a lone observation.** The merge discards nothing… File it even if you suspect the other two will not."* | **Deliberately obsolete** — under approve/reject there is no merge and a lone rejection blocks (`2-plan.md:22`). Not a loss, but it is not on the declared DROP list either. Nitpick. |
| `:45-50` | The three earned-clean clauses | **Declared DROP** — `0-baseline.md:61`, C4. Clean, and `1-spec.md:63-65` correctly notes they would make a one-line approval non-conforming. |
| `:51-52` | *"You do not contest severities"* | **Moot** — no severities survive. Clean. |
| `:54` | *"You are graded on **precision** — are your findings real? — not on how many you raise."* | **SILENTLY LOST — see M9.** |

Two more losses come from `redteam-split.md` itself (which is rewritten, so its rules need the same
audit and `0-baseline.md` gives them none): Q1 Coverage (`:39-40`) → M3; *"an unstated seam is at
least `major`"* (`:42-43`) → M4. Q4 "real joint or arbitrary cut" (`:55-57`) is adequately carried
by "natural seam" — clean.

## MAJOR M5 — the floor rule is not restated, it is replaced by a weaker sentence that already exists, and C9's oracle cannot detect the difference

`redteam.md:17-18` states an **infinite-regress guard about the remedy of a finding**:

> **Do not file a finding whose only remedy is to decompose below the floor.**

`2-plan.md:37-39` proposes to replace it with:

> **The floor bound** (C9): do not reject for a lack of detail — a sub-task is not required to be
> detailed, only to be a coherent whole task above the floor. This is the sentence that replaces
> the guard `redteam.md` used to supply.

These are different rules. The replacement is about **vagueness of a sub-task**; the original is
about **the remedy of any finding**. A reviewer bound only by the replacement may still reject a
division because the seam does not specify the status vocabulary in detail — a finding whose only
remedy is to decompose the seam below the floor — and is fully compliant.

**Worse, this exact sentence is already in the current file.** `redteam-split.md:31-33`: *"You are
not looking for vagueness — a sub-task is not required to be detailed, only to be a coherent whole
task still above the floor."* So C9's *"positive assertion"* oracle, matching that sentence, **passes
on both the old and the new file** — a printer by `1.5-criteria.md:5-6`. And `2-plan.md:73` classes
C9 among the CARRY assertions that *"must pass on **both**"*, whose self-test is "delete the asserted
line and confirm the assertion fires" — which cannot detect that the *stronger* rule was dropped,
only that the *weaker* one is present. **The one criterion the spec explicitly built to catch this
position-lens regression is blind to it.**

**Remedy:** C9 must assert the remedy-form of the rule (`redteam.md:17-18`'s sentence, or an
equivalent), not the vagueness-form that already exists.

## MAJOR M3 — Coverage is silently lost: on neither the CARRY list nor the DROP list, and no criterion observes it

`redteam.md:38` (*"was any portion of the task left unaddressed?"*) and `redteam-split.md:39-40`
(Q1: *"do the two halves cover the **whole task**, with no orphaned remainder and no portion both
halves assume the other owns?"*) are the same rule stated twice. Record 3666 reduces the reviewer to
two questions, neither of which is coverage. `divider.md:54-55` keeps a coverage duty on the
*divider* (*"Two sub-tasks that together cover the whole task"*), and `2-plan.md`'s §-list for the
rewritten `divider.md` does not carry it either — §1-§7 name the seam, the floor, the source
material, the review, the cap and the memo, and never coverage.

`0-baseline.md:42-58` CARRY list: six items, coverage is not one. `0-baseline.md:59-65` DROP list:
seven items, coverage is not one. `2-plan.md:95` states the rule that catches this — *"A DROP not on
the declared list is a regression"* — and coverage is a DROP not on the declared list.

**Failure scenario.** The it3 task statement has eight numbered properties P1–P8 plus an entry
surface (`SKILL.md`, `METHODOLOGY.md`, `README.md`) and a config. A rewritten divider cuts at the
finding boundary — a genuinely natural seam — but assigns the entry surface to neither half. Both
reviewers check the two questions: natural seam ✓, above the floor ✓ → **approve, correctly, in one
line each.** Two children plan; `Union` concatenates; the merged plan never builds `SKILL.md`, and
nothing detects it until a human reads the output. No criterion in C1–C18 observes coverage.

Whether coverage should be restored is genuinely arguable — record 3666 says "boil down to", and a
cut that orphans a third of the task is arguably not "a natural seam". But the decision has not been
*made*: it is neither carried nor declared dropped, which is the failure `2-plan.md:95` exists to
prevent.

## MAJOR M8 — nothing observes the integrity of the memo file the change introduces; C17 passes even if the resume destroys round 1's record

`2-plan.md:52-57` requires `divide-<iter>.md` be **append-only**, one `## Round N` per completed
round. C17 (`1.5-criteria.md:42`) verifies only *"which round it started at"*.

**Failure scenario.** The injected fresh divider reads `divide-0.md`, correctly resumes at round 2,
and then — as agents given "write your output to this path" routinely do — **writes** the file
rather than appending, or rewrites it wholesale at the end. Round 1's proposal and its three verdicts
are gone. C17 passes ("it started at round 2"). The file is simultaneously the resume point and, per
`divider.md:116-118`, *"the record [that] is what the owner will be shown"* on the `FAILED_TO_DIVIDE`
path — and the 2-of-3-across-all-rounds fallback (`divider.md:106-111`) requires every round's
verdicts to still be there. A second restart after this one resumes from a file that has lost the
data the cap rule reads.

This is not speculative hardening: it is a defect in the **verification of a mechanism this change
introduces**, and `2-plan.md:96` invites exactly this check (*"If a reviewer finds a second reader,
the design is wrong"* — the fallback rule at `divider.md:106` **is** a second reader of the round
records). C17 needs one more observation — after the resume, `## Round 1` is still present and
unmodified — not a new guard.

## MAJOR M9 — "graded on precision, not body count" is dropped, while being the exact pathology the spec diagnoses

`redteam.md:54`: *"You are graded on **precision** — are your findings real? — not on how many you
raise."* Not in the CARRY list, not in the DROP list, not in `2-plan.md`'s §-list for the rewritten
`redteam-split.md`.

`1-spec.md:15` diagnoses the run's failure as *"reviewers graded on finding defects find them at
whatever grain is available"* — i.e. the precision rule failing to hold. Removing the only sentence
that states it, in the change whose problem statement is its failure, is a regression by the spec's
own reasoning. It **broke** (twelve reviews, ~5,270 lines, ~90 findings, `decisions.md:264-269`), so
restating it is a fix under 3497, not hardening. One sentence.

## Minor A1 — item 2's owner authority is asserted without a record; the ratified source exists and is not cited

`1-spec.md:103`: *"the owner ruled the gap be fixed."* No record number, no quote, no locus. Under
the loop's own RAT1 rule an owner ruling recorded without a durable, spot-checkable source is
treated as unverified. **The ruling does exist** — transcript record **3486**, verbatim: *"Good catch
on the division memo thing; add that to the to-fix list for iteration 3, along with whatever pops up
on the restart"* — and it supports item 2. Two caveats worth stating: 3486 says *"iteration 3"* and
this is now iteration 4 (immaterial — iteration 3 was voided before the memo mattered), and 3486
ratifies *"add it to the to-fix list"*, not the divider-memoises-itself **design** at
`1-spec.md:91-100`, which is the author's and should be labelled as such. Cite 3486 and mark the
design as the author's proposal.

## Nitpick A2 — the worked example is cited to an assistant-authored intermediary; the transcript source exists

`1-spec.md:33-39` cites the worked example to `Architect-rulings.md`, which is assistant-authored.
I verified it against the transcript and it is **faithful**: record **3628** is the owner setting up
the four-file merge example verbatim, and record **3634** is the owner's correction verbatim: *"the
merging would get done automatically in the second pass of the task.empty() while loop."* Cite
3628/3634 directly. (Recorded rather than dropped because the same paragraph is the sole support for
the risk acceptance attacked at M6.)

---

# LENS 5 — FIDELITY (record 3666 audited in both directions)

**Record 3666 verified verbatim** from
`…/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl` line 3666, `type: user`. It matches
`1-spec.md:27-31` **exactly**, including the owner's spellings ("seem", the double space before "If
it is a natural split"). Clean.

**Loaded terms pinned.** *"boil down to"* → in the plan, a rewrite-from-scratch of two prompt files
to ~35 and ~30 lines (`2-plan.md:5-9`) — a defensible reading, and 3666's own scope-narrowing form
supports rewrite over edit. *"reject with explanation"* → `2-plan.md:33-34`, *"an explanation of
which question failed and why"*, carried into the next round as the reason (`2-plan.md:22`) —
faithful. *"the point of maximum granularity"* → the run's `granularity` floor as defined in
`common.md:27-29`, checked *"in one direction: would either half fall below it"* — faithful to
`redteam-split.md:30-33`'s existing pin and to 3666's phrasing. *"approve"* → return with no
finding, one line permitted (C2) — faithful. **One term is pinned to a proxy: see M2** (*"a one-line
approval must be correct, not lazy"* is pinned to `≤ 6 KB`, which is a size proxy for a quality
property).

## (a) Is the plan cutting something 3666 did not ask to be cut? — Mostly no, with two exceptions

Removing `redteam.md` from the split reviewer's dispatch is **not** in 3666's text, but it is
entailed: `redteam.md:20-50` is physically where the six lenses and earned-clean clauses live, and
3666 says the reviewer's instruction should boil down to two questions. `1-spec.md:66-71` argues
this correctly. Clean.

The two exceptions are M3 (coverage) and M4 (the unstated-seam rule): both are cut, neither is
required by 3666, and neither is declared. Ranked there.

## (b) Is the plan keeping something 3666 tells it to cut? — GENUINELY AMBIGUOUS, and the ambiguity is resolved asymmetrically in the author's favour

This is an **owner question, not mine and not the author's**, and I am flagging it as one.

3666 is reductive about *both* roles, in parallel clauses of one sentence: *"the **dividers**
instruction should boil down to this: Find a natural seem … and split it into two pieces at that
seem. The **reviewers** instruction should boil down to: [two questions] … approve; otherwise,
reject with explanation."* On a literal reading of the first clause, the divider's whole instruction
is one sentence — which would repeal the four rounds, the 2-of-3 fallback and `FAILED_TO_DIVIDE`
along with everything else.

`2-plan.md:93` resolves this: *"3666 speaks to *instructions*; 3402/3438 settled *rounds*."* That is
a real and reasonable distinction. **But it is applied asymmetrically to the two halves of one owner
sentence.** Record 3438 verbatim (transcript line 3438) is a single sentence:

> "okay, up the attempts to 4, and 2/3 agreement is two of the three reviewers either endorsing or
> at least not objecting to going forward with with their findings carried foward"

`1-spec.md:80-82` reads 3666 as **repealing** the second half of that sentence (*"3438's 'findings
carried forward' clause is what 3666 replaces"*) while **preserving** the first half (*"up the
attempts to 4"* → C7). 3666 mentions neither findings, nor carrying forward, nor rounds, nor
agreement. So the same silence is read as repeal in one direction and as non-interference in the
other, and both readings land on the author's preferred outcome.

**Is the "findings carried forward" reading defensible?** Partly — under a binary approve/reject
there is no "approve with standing findings" category, so the mechanism has nothing to carry. That
is a real entailment. But 3438's carry-forward clause also governs the *divider's* duty
(`divider.md:35-36`: *"attach each standing finding to the sub-task it bears on, so it travels down
with that half"*), which is not entailed away, and its removal is on neither the CARRY nor the DROP
list.

`1.5-criteria.md:48-49` already declares reviewer disagreement on this a stop-for-human. **That is
the right destination but the wrong trigger**: it fires only if reviewers happen to disagree. The
ambiguity is on the face of the owner's own text, and the *asymmetry* of the resolution is visible
without any disagreement. **This should go to the owner now, with both halves stated**: "3666 boils
down the divider's instruction too — does the four-round / 2-of-3 / `FAILED_TO_DIVIDE` machinery from
3402 and 3438 survive it, and does 3438's 'findings carried forward' survive it?" Ranked **major**
under CH11's *"partial or adjacent … re-ask the flagged axis, never resolve it into the author's own
recommended option."*

## MAJOR M6 (RAT2) — the risk acceptance inflates the owner's worked example from task-content findings to seam defects, and the it3 evidence shows the extension is false

`2-plan.md:94` accepts the change's largest risk on owner authority:

> **Cheaper reviews are worse reviews** — the real defects the it3 reviews found (**seam gaps, a
> termination hole**) go unraised. | Accepted **on the owner's instruction**, record 3666 and its
> worked example: **those findings are handled by the node's next `while` pass.**

**The ratified phrase.** Transcript record 3634, verbatim: *"the merging would get done automatically
in the second pass of the task.empty() while loop."* Its operative scope is the specific example at
record 3628: a four-file merge split {a,b}/{c,d}, where the un-deduplicated cross-half result *is the
merged output*, so the red-team sees it against the original task and it **becomes the next task**.

**The elaboration.** `2-plan.md:94` extends that to *"seam gaps, a termination hole"* — the class
actually found in it3. The extension does not hold, and the it3 artefacts say why:

- The round-4 blocker (`divide-0.md:100`), filed independently by **all three** round-4 reviewers, is
  *"no attempt cap on the `leaf, no STATUS` row … the stated termination argument is false"*. It is a
  defect **in the seam**, and `divide-0.md:92` states its status: *"nearly all of these are defects
  in the SEAM … A planner cannot act on them … They are for the node's human gate."*
- `divide-0.md` §5 **G5**, verified against `leaf.md`, `node.md` and `combiner.md`: *"a planner has no
  reliable channel for objecting to a seam its parent fixed… `Consensus` takes 2-of-3 on numbered
  steps and **discards the odd plan** — so a lone planner's objection can be discarded before any
  node or human sees it… **It is a real hole in the design and it should not be closed by wording.**"*

So the mechanism the owner named — the finding re-surfaces as the next task on the next `while` pass
— works for *task content* (the cross-half merge) and demonstrably **does not** work for *seam
defects*, which are the parent node's artifact, inherited downward, unchangeable by any child, with
no channel to object. The plan's acceptance therefore rests on an entailment the owner's words do not
carry, over the exact finding class it3 produced.

**This does not argue against the cut** — 3666 is clear and the owner may well accept losing the
termination hole. It argues that the acceptance is recorded as *ratified* when it is an **unratified
inflation** (CH12/RAT2). **Remedy:** narrow `2-plan.md:94` to what 3634 covers (findings whose
subject matter re-enters as the next task), and record the seam-defect class as an
**author-accepted** risk with its evidence (`divide-0.md:100`, G5) — or put it to the owner. Note
that M4's one-clause fix (the seam must travel in the sub-task string) is the only thing that would
even give a downstream reviewer sight of the seam.

---

# COVERAGE CHALLENGE (CH8) — behaviours this change can alter that no criterion observes

Ranked by impact. Each is a behaviour the change plausibly alters with **no** criterion in C1–C18
observing it.

1. **Coverage of the whole task by the two halves — major.** M3's scenario: natural seam, both
   halves above the floor, entry surface orphaned; both reviewers correctly approve; `Union`
   concatenates two plans that together do not plan the whole task. No criterion.
2. **The seam is stated at all, and travels to the children — major.** M4's scenario: a three-word
   seam passes both questions; children invent incompatible layouts. `redteam-split.md:42-43`'s
   *"an unstated seam is at least `major`"* is deleted; `node.md` passes only the sub-task value
   (G4). No criterion observes seam content or transport.
3. **`null` at node 0 — major.** B4: the degenerate non-division passes C13 and C16 and makes C14
   vacuous and C15 unmeasurable. No criterion requires node 0 to return a division.
4. **Memo integrity across the resume — major.** M8: a resuming divider that rewrites rather than
   appends destroys round 1's verdicts; C17 still passes; the 2-of-3-across-rounds fallback
   (`divider.md:106-111`) then reads a file missing the data it needs.
5. **The reviewer count is still three — major.** `2-plan.md:21` says three; **no criterion asserts
   it**, and C13 rewards fewer. Scenario: the iteration-4 divider, reading a 35-line prompt whose
   surrounding run is about cost, dispatches two reviewers. C13 passes at 3 agents (better than the
   3/3 case); C15 needs *"the 3 round-1 split reviews"* and becomes unmeasurable; 2-of-3 becomes
   2-of-2. Nothing fails.
6. **Cross-file agreement on the round cap — major.** M7: `node.md:47` says three, `divider.md:102`
   says four. C7 checks `divider.md` alone. Scenario: `FAILED_TO_DIVIDE` after four rounds; the node
   reads its own file, expects it after three, and the divergence surfaces as an escalation the node
   describes wrongly to the owner.
7. **Rejection actually changes the cut — minor.** `2-plan.md:22`: *"Any rejection → cut again at a
   different seam, using the reason."* No criterion observes that round 2's seam differs from round
   1's. `node.md:120` already names re-wording the same split as the failure mode
   (*"re-wording the same split is not a [new one]"*). Scenario: reviewer rejects on question 1; the
   divider re-words the same joint; three reviewers approve the re-wording; C13 passes at 7 agents…
   except M1 already fails that run, so this one is partly masked.
8. **`FAILED_TO_DIVIDE` still reaches the owner correctly — minor.** C6 asserts `divider.md` states
   the three answers; nothing observes the node's escalation path (`node.md:48-52`) still working
   after `redteam.md` leaves the dispatch. The iteration-4 run will almost certainly not exercise
   this path, so it is unobserved by construction — flagging it as unmeasured rather than asking for
   a criterion.
9. **The divider's output size — nitpick, and deliberately not a request.** `2-plan.md:100-102`
   declines a cap on divider output, correctly, under 3497. Recorded only so the coverage list is
   honest: the it3 round-4 proposal was 47,376 bytes and nothing observes whether that changes.

---

# What I could not check

- **C13/C15/C16/C17's actual behaviour.** These are verified by running Architect, which has not
  been run. My attack is on whether the thresholds *could* discriminate, not on the outcome.
- **`~/Documents/Architect.md`'s content.** I read `Architect-rulings.md` in full and the pseudocode
  only through the rulings file and the stage prompts; I did not independently verify
  `1-spec.md:143`'s claim that `Divisible`'s signature and both call sites are untouched. C12's
  sha256 compare will settle it mechanically.
- **Whether the parallel reviewer reached the same conclusions.** No contact, by design.
- **The 12 review files in full.** I read all twelve verdict blocks and `divide-0.md` in full
  (~500 KB total in the directory); the per-finding bodies were sampled, not read exhaustively.

---

# Findings, ranked

| # | Severity | Finding |
|---|---|---|
| B1 | **blocker** | Baseline measurement false on disk: 12 reviews not 11, 13 agents not 15, 107 min not 90, and the division **finished**. Corrected figures are in `decisions.md:223-300`, committed at `HEAD`. Propagates to C13, C16, C18. |
| B2 | **blocker** | `0-baseline.md:3` freezes `d81bc0a`, which is not the parent (`HEAD` = `cf16967`); all four files under change differ between them. `2-plan.md:71`'s self-test resolves the wrong files, defeating the printer guard. `0-baseline.md`'s own hash table contradicts its line 3. |
| B3 | **blocker** | C13's 30-minute gate cannot attribute a pass to this change: `decisions.md:251-257` measures ~50 of the 107 baseline minutes as **serial dispatch, an orchestrator instruction, not the design's**, and nothing pins iteration 4's dispatch mode. 6 and 30 are underived; C18's arithmetic against the corrected baseline disagrees with C13. |
| B4 | **blocker** | C16 is satisfied by `Divisible` returning `null` at node 0 — the iteration-1 failure — and its own parenthesis blesses it. That run also passes C13, vacates C14 and makes C15 unmeasurable. No criterion requires node 0 to return a division. |
| M1 | major | C13's ≤ 6 agents permits exactly one round (1 divider + 3 reviewers = 4; two rounds = 7), gating against the four-round machinery C7 requires be kept. A correct 2-round division fails the gate. |
| M2 | major | C15 measures review quality by file size: a bare "Approve." maximises it. Its second clause ("accepted rather than re-run") is unfalsifiable — nothing re-runs an approval. Gating criterion verified against a proxy (CH9). |
| M3 | major | Coverage ("do the halves cover the whole task") is dropped from both `redteam.md:38` and `redteam-split.md:39-40`, is on neither the CARRY nor the DROP list, and no criterion observes it — a regression by `2-plan.md:95`'s own rule. |
| M4 | major | `redteam-split.md:42-43`'s *"an unstated seam is at least major"* is silently dropped, and G4 (*"nothing carries the seam down"*, `divide-0.md` §5, filed by reviewers in rounds 1/3/4, closed only by the divider improvising) is not fixed though record 3497 puts it in scope. |
| M5 | major | The floor guard is **weakened, not restated**: `2-plan.md:37-39` substitutes a vagueness rule for `redteam.md:17-18`'s remedy rule, and the substitute is already verbatim in `redteam-split.md:31-33`, so C9's assertion passes on both files — a printer, and the self-test's CARRY carve-out cannot catch it. |
| M6 | major | RAT2 inflation: `2-plan.md:94` accepts losing "seam gaps, a termination hole" on record 3634's authority, but 3634 covers findings that **re-enter as the next task**; `divide-0.md:92` and G5 establish that seam defects cannot. Narrow the acceptance or put it to the owner. |
| M7 | major | `node.md:47` says three rounds, `divider.md:102` says four (record 3438). Reported first-hand by the it3 divider (G2) and recorded at `decisions.md:311`. In scope under 3497; `node.md` is already a touched file; no criterion observes cross-file agreement. |
| M8 | major | C17 verifies only which round the resumed divider starts at. A resume that rewrites rather than appends destroys round 1's record and still passes, and `divider.md:106-111`'s across-all-rounds fallback is a second reader of that record. |
| M9 | major | `redteam.md:54` (*"graded on precision … not on how many you raise"*) is silently dropped — the one rule stating the pathology `1-spec.md:15` diagnoses as the cause. |
| — | major | **Owner question, not the author's:** 3666's "boil down to" is reductive about the divider too, and `1-spec.md:80-82` reads it as repealing one half of record 3438's single sentence while preserving the other. Ask the owner directly rather than waiting for reviewers to disagree (`1.5-criteria.md:48-49`). |
| A1 | minor | `1-spec.md:103` asserts *"the owner ruled the gap be fixed"* with no record. The ruling is **record 3486**; cite it, and label the memoisation design (`1-spec.md:91-100`) as the author's, since 3486 ratifies only "add it to the to-fix list". |
| F1 | minor | "six lines above it" (`0-baseline.md:36`, `1-spec.md:19`) — the §3438 block ends at `divider.md:36`, the re-derive rule is at `:97`. ~61 lines. |
| F2 | minor | `1-spec.md:7` *"The cost was entirely apparatus"* — `decisions.md:253-257` measures ~half as serial dispatch, and `2-plan.md:94` concedes real defects were found. |
| F3 | minor | `1-spec.md:138`'s `node.md` row is a no-op: `node.md:41` does not name reviewer files. The line that does need changing is `:47` (M7). |
| L1 | minor | C17's injected second divider is an extra dispatched agent; whether it counts against C13's budget of 6 is undefined and, at exactly one round of headroom, decides pass/fail. |
| L2 | minor | C12 (`Architect.md` unchanged) passes identically pre- and post-change — a printer by `1.5-criteria.md:5-6`, unfixable by `2-plan.md:73`'s delete-a-line self-test. Keep as a tripwire, relabel advisory. |
| C5 | minor | No criterion asserts the divider dispatches **three** reviewers; C13 rewards fewer, and C15/2-of-3 both silently assume three. |
| A2 | nitpick | `1-spec.md:33-39` cites the worked example to the assistant-authored `Architect-rulings.md`. Verified faithful against transcript records **3628** and **3634** — cite those. |
| — | nitpick | `redteam.md:43-44` ("do not self-censor a lone observation") is obsoleted by the approve/reject binary but is on neither the CARRY nor DROP list. |

## Label audit (CH9/CH10), per gating criterion

No criterion is yet `verified = yes`, so the audit is of the labels and the intended verification
path. C1–C3, C5, C6, C8, C10 — labels defensible, governed path is textual and the oracle exercises
it. **C4** — defensible, and correctly paired with positive assertions per `2-plan.md:66-68`.
**C7** — gating but incomplete: it governs the round cap and checks only one of the two files that
state it (M7). **C9** — gating, but its oracle does not exercise the path it governs (M5). **C11** —
gating; its must-fail-on-old validation is compromised by B2. **C12** — mislabelled gating (L2).
**C13** — gating; threshold not derived and not attributable (B3), and internally hostile to C7 (M1).
**C14** — gating; vacuous on the `null` path (B4). **C15** — gating but verified against a proxy;
should be advisory (M2). **C16** — gating; satisfiable by the failure it exists to exclude (B4).
**C17** — gating; observes a strict subset of the property it names (M8). **C18** — advisory label
is legitimate (a trend line, with C13 as the absolute gate) — clean, though its arithmetic uses the
wrong baseline (B1).

## Ratification audit (CH11/RAT1)

Three owner-authority claims appear in the artifacts. **Record 3666** (`1-spec.md:27-31`) —
**audited, valid**: quoted verbatim with a durable source (transcript line 3666), spot-verified by
direct read, exact match including the owner's spellings; it selects the reviewer's two-question
form on the flagged axis. **Record 3497** (`1-spec.md:43-45`) — **audited, valid**: verified verbatim
at transcript line 3497; supports the no-speculative-hardening constraint, and additionally supports
M4/M7 as in-scope fixes. **Record 3634's worked example** (`1-spec.md:33-39`) — **quote valid**
(transcript 3628 + 3634, cited only to an intermediary, A2) **but its elaboration is not ratified**
(M6). The un-ratified item is `1-spec.md:103`'s uncited "the owner ruled" (A1), whose real source is
record 3486 and which ratifies less than the spec builds on it.
