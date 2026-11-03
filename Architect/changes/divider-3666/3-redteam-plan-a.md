# Stage 3 — cold red-team of {0-baseline, 1-spec, 1.5-criteria, 2-plan}

**Reviewer:** cold subagent dispatched via the Agent tool (`claude` / general-purpose type), no
shared context with the author.
**Model:** claude-opus-5.
**Charter applied:** `~/.claude/skills/guarded-change/stages/charter.md` (five lenses + discipline
+ position lens, which fires here: Architect's stage files are a prompt assembly) and
`stages/stage-3.md` (CH8 coverage challenge, CH9/CH10 label audit, CH11/CH12 ratification audit).

## sha256 of the artifacts under review

| File | sha256 |
|---|---|
| `changes/divider-3666/0-baseline.md` | `813722924453ee4939dd4a5030600e2d35d7be18636b0a151212b34aa6fb648e` |
| `changes/divider-3666/1-spec.md` | `edac3f727a6af1d048106c9fab0c00630c85c8bdc2e4aa0a53cc3e6bf63aad73` |
| `changes/divider-3666/1.5-criteria.md` | `da0bb079ecd0984cfc736f128504972460ddc1ddc8663c631dcdf87c4ec601eb` |
| `changes/divider-3666/2-plan.md` | `ed42d93f0f247904ec1c9a58d6e6452632bef1170c87c785abfd9190cf8201dc` |

## sha256 of the context I actually read (closed set as given)

| File | sha256 |
|---|---|
| `Architect/stages/common.md` | `389358e2b74ee3490b6682847fb8c8034063724fd924f2179341acc5120651d4` |
| `Architect/stages/redteam.md` | `bfdc0cc6aaf39d0cacdfab0788b5a234c0547eafc6d35ff18c62deea87bfb1b5` |
| `Architect/stages/redteam-split.md` | `ffeea71567959a05af19f891168e10145658905a4a072bdac654dd04fe83de13` |
| `Architect/stages/redteam-plan.md` | `4f7bee4c31b53e215f697609c62f7bd253daa80cf508c7db9d9af5f5a7da1111` |
| `Architect/stages/divider.md` | `ebdf30eddf9dc227f895b4d414cc442ae5c230e1c0ee405409dd52a18829c694` |
| `Architect/stages/node.md` | `1a41e11fd2438fc9ac4ee86f16dc97ee7656b687d33a9df749802da478a3a068` |
| `Architect/SKILL.md` | `ffaa1a8440fa829cbd4d4a4401dcd9bcd9d95cf22006ea0a3d5110b50a1c21b9` |
| `Architect/runs/data-distiller/decisions.md` | `2fe87e42e3d8653c2e2a8021759d5ee4a4f4cb6f239399756c35513174b030f9` |
| `~/Documents/Architect.md` | `d36e6942e64528c4a9a89fe79a1125b072264adfef9f43c7a858713ba4591594` |
| `~/Documents/Architect-rulings.md` | `67a0bdd0ea386114b751dff55d96c07f952ddbd353745a38e68f5126b3deea5b` |
| session transcript `…45cb99a2-….jsonl` | 3711 lines; records 3119, 3402, 3438, 3486, 3497, 3628, 3634, 3666 read directly |

Sampled, not read whole: `runs/data-distiller/it3/0/` (directory listing with mtimes and sizes;
heads of `divide-0.md` and `split-round-1.md`).

---

# Findings, ranked

## BLOCKER B1 — the baseline's headline measurement is contradicted by the run artefacts and by the commit it sits on. Every behavioural threshold is calibrated against it.

`0-baseline.md:25-27` states:

> **Measured cost of one division at one node: 12:43 → 14:13 = 90 minutes, 4 divider agents +
> 11 cold split reviews = 15 dispatched agents, and it did not finish.**

Four separate claims, all wrong:

1. **"it did not finish."** `it3/0/divide-0.md` §1, read directly: *"**`Divisible` returns a
   DIVISION** — not `null`, not `FAILED_TO_DIVIDE`."* `decisions.md` log, entry
   `2026-07-31T18:24:35Z`: *"`Divisible` **returned a division**: four rounds, twelve cold
   reviews, 12/12 endorsement, cut at the finding boundary."* `subtask-A.md` and `subtask-B.md`
   exist on disk (14:23).
2. **"11 cold split reviews."** `ls` shows **twelve**: `split-review-r4-c.md`, 37,581 bytes,
   14:22. `0-baseline.md:23` records round 4 as `-r4-{a,b}` and "run parked mid-round" — the
   third review landed nine minutes after the row the baseline froze.
3. **"4 divider agents."** `node.md:41` — *"Dispatch **one** agent on `stages/common.md` +
   `stages/divider.md`"* — one divider per `Divisible` call, running its rounds internally
   (`divider.md:106`, *"look back over **every split you proposed across all four rounds**"*).
   `divide-0.md` §0 confirms from the divider's own voice: *"Every one of the twelve cold split
   reviewers **I dispatched**."* One divider + twelve reviewers = **13** dispatched agents.
4. **"90 minutes."** `decisions.md` puts dispatch at `16:37Z` and return at `18:24:35Z` =
   **107 minutes**; the file mtimes (UTC−4) agree: 12:37 → 14:24.

This is not a stale-file problem. `git log` shows **HEAD is `cf16967`**, whose message says in
terms: *"CORRECTION to what the orchestrator reported: not '70 minutes, 8 reviews, unfinished'.
Divisible COMPLETED — 107 minutes, 12 cold reviews, 4 rounds, division returned"* and
*"Committed as the true baseline for the guarded-change run, which was dispatched against a stale
assumption that the tree was clean."* `0-baseline.md` reproduces the corrected error in a new
numeric form.

**Why it is a blocker and not a nitpick.** The numbers are load-bearing three times over:
- **C13** is written as *"**A division at node 0 returns.** … Baseline: 15 agents / 90 minutes /
  no return"* (`1.5:38`). The thing C13 gates on **already happens today.** The criterion as
  written cannot distinguish the change from the status quo on its headline axis.
- **C13's `≤ 6 dispatched agents`** is calibrated against 15; the true figure is 13.
- **C18's ≥60% on both axes** (`1.5:43`) is arithmetic against `0-baseline.md` by its own text.

**Remedy (no new apparatus):** correct `0-baseline.md` to 13 agents / 107 minutes / **returned a
division**, and rewrite C13's success statement to what the change is actually claimed to buy
(cost, not return).

---

## BLOCKER B2 — removing `redteam.md` does **not** remove the severity model or "cite or it doesn't count". Both live in `common.md`, which the spec keeps. The split reviewer is left holding two contradictory instructions.

`1-spec.md:9-13` is the premise of the whole change:

> `redteam-split.md` is an *aiming file* appended to `redteam.md`, the plan reviewer's charter —
> so a split reviewer inherits the six lenses, **the four-tier severity model**, the earned-clean
> disciplines … and the **"cite or it doesn't count" provenance rule**.

Checked mechanically (`grep -rn` over `Architect/stages/`):

| Claimed to be in `redteam.md` | Actually at |
|---|---|
| six lenses | `redteam.md:20-36` ✓ |
| earned-clean disciplines | `redteam.md:45-50` ✓ |
| **four-tier severity model** (`blocker/major/minor/nitpick` table) | **`common.md:38-52`** — sole occurrence of "nitpick" in the whole `stages/` tree |
| **"cite or it doesn't count"** | **`common.md:60`** — sole occurrence |

`1-spec.md:142` lists `common.md` under **"Not touched."** So after the change the split reviewer
reads `common.md` + `redteam-split.md`, and `common.md` still tells it:

- `common.md:40` — *"Every finding carries one, because the loop filters on it"*
- `common.md:52` — *"**A finding with no severity is unusable.**"*
- `common.md:54` — *"**Findings are merged, never voted on.** Nothing is dropped for being
  unconfirmed by another reviewer"*
- `common.md:60` — *"**Cite or it doesn't count.** Every claim names a `file:line`, a quoted step,
  or a concrete failure scenario."*

against a `redteam-split.md` that (per `2-plan.md:42-43`) has *"No lenses, no severities … "* and
whose verdict is a **vote** (`2-plan.md:22`, *"All three approve → return. Any rejection → cut
again"*; `1.5:24`, the 2-of-3 fallback). **"Findings are merged, never voted on" is the direct
negation of the mechanism the change installs**, and it sits in the file the reviewer reads first
(`common.md:3`, *"Every agent Architect dispatches reads this file first, then its role file"*).

This is structurally identical to the failure `0-baseline.md:32-37` diagnoses as the cause of the
90 minutes — a prompt contradicting itself across two adjacent blocks, with the *older, more
elaborate* rule winning. The change relocates that contradiction from `divider.md` into the
`common.md`/`redteam-split.md` pair and no criterion observes it: **C4's absence sweep is scoped
to `divider.md` and `redteam-split.md` only** (`1.5:16`).

Concrete failure scenario: a split reviewer, told by `common.md:52` that a finding without a
severity is unusable and by `common.md:60` that every claim needs a `file:line`, writes
*"**reject — major**: the seam …"* with citations, at 8 KB. C15 (≤6 KB, 2 of 3) fails, C13's
30-minute clock blows, and the post-run diagnosis lands on the rewrite rather than on `common.md`.

**Remedy (one clause, not new apparatus):** either scope `common.md` §4 and the "cite" bullet to
plan review (`common.md:38` → *"If your role assigns severities…"*), or state in
`redteam-split.md` that a split verdict is approve/reject and carries no severity. Either way,
`common.md` moves out of "Not touched" and C4's sweep must cover the reviewer's whole assembled
context, not two of its three files.

---

## BLOCKER B3 — nothing in the post-change dispatch tells the split reviewer it holds the **task** and the **floor value**. Both of record 3666's questions are unanswerable without them, and the one sentence that supplied them is in the file being removed.

The task-and-floor input declaration for split reviewers is **`redteam.md:11`**:

> Common to both: the **task** and the **granularity floor**.

`redteam-split.md:23` depends on it by reference: *"**One thing beyond the common list**: the
proposed division."* Delete `redteam.md` from the dispatch and "the common list" has no referent.
`common.md:15` does not supply it — it says *"Exactly what your caller passed you. **Your role
file lists them.**"* — and `common.md:27` is conditional: *"**If your role takes a `granularity`
argument**, you hold the run's atomic-step floor."*

The plan's replacement (`2-plan.md:31`) reads: *"**What you are reviewing**: a proposed division —
two sub-tasks and a seam. No plan (C8)."* — the task and the floor are named nowhere in the six
sections of the new `redteam-split.md`.

**And the divider's dispatch instruction does not hand them over either.** `divider.md:96-97`, the
line the change rewrites, says the divider dispatches *"handing each **your two sub-tasks and your
stated seam**"* — no task, no floor. `2-plan.md:21` restates the dispatch without adding them:
*"dispatch three cold agents on `common.md` + `redteam-split.md` (C5)."*

Record 3666's two questions are, verbatim: *"Is this split at a natural seem?"* and *"does it
reduce **the task** past the point of maximum granularity?"* A reviewer holding only two sub-tasks
and a seam **cannot answer either** — "natural" is a property of the seam relative to the task
that was cut, and "past maximum granularity" requires the floor value.

Partial mitigation, which I checked: `SKILL.md:83-86` passes `task:` and `granularity:` in every
dispatch template. So an obedient dispatcher supplies them regardless. But `SKILL.md:81`'s
role-file line and `divider.md:97`'s explicit "handing each …" enumeration are the operative
instruction to the divider, and they override the template's generic slots by specificity.

**No criterion observes this.** C8 asserts the reviewer states it holds **no plan** — the negative
input only. C1 asserts the two questions are stated, not that the reviewer holds what it needs to
answer them.

**Failure scenario, and it is the one C15 rewards.** A reviewer without the task can only inspect
the two sub-tasks for internal coherence. Both look coherent. It approves in one line. C15 (≤6 KB,
2 of 3) **passes**, C13's agent count and clock **pass**, C14 (no sub-floor rejection) **passes** —
and the run has bought a vacuous approval that scores as a clean sweep of the behavioural gates.

**Remedy:** one clause in `2-plan.md`'s `redteam-split.md` §1 ("your inputs: the task, the
granularity floor, and the proposed division") and one in its `divider.md` §5 dispatch line, plus
a C1 sub-assertion. This is restoring a deleted sentence, not adding a guard.

---

## MAJOR M1 — the oracle self-test compares against the wrong commit. `git show d81bc0a:<path>` is not the pre-change file.

`1.5:4-5`: *"self-tested against the frozen pre-change files (`git show d81bc0a:<path>`)"*;
`2-plan.md:71` repeats it. `0-baseline.md:3`: *"Commit at run start:
`d81bc0a9863dbe33becda73c2a0c78675bf5a6a1`."*

Measured: **`git rev-parse HEAD` = `cf169679f7da23c95572148231f47dd0c7faf283`**, and
`git diff --stat d81bc0a` shows the four files under change differ from `d81bc0a` by
`divider.md` 36 lines, `node.md` 31, `SKILL.md` 29, `redteam-split.md` 16. The sha256 table at
`0-baseline.md:9-12` matches the **working tree**, not `d81bc0a` — I hashed both:

| File | `0-baseline.md` says | `git show d81bc0a:` |
|---|---|---|
| `divider.md` | `ebdf30ed…` (= working tree) | `ac25b9ae…` |
| `redteam-split.md` | `ffeea715…` (= working tree) | `119d00ef…` |

`decisions.md` warns about exactly this, in a section headed **"⚠ The working tree is NOT at
`d81bc0a` — read this before starting the guarded-change run"**: *"should treat them as the
baseline, not as `d81bc0a`."*

**Concrete consequence.** `git show d81bc0a:Architect/stages/divider.md | grep -c 'Three places'`
= **0**; the three-destinations apparatus that `1-spec.md:110` and `0-baseline.md:63` name as a
declared DROP was introduced by `cf16967`, not by `0d6c229`. Self-testing a "the apparatus is
gone" assertion against `d81bc0a` tests it against a file that **never contained the apparatus** —
the assertion passes the self-test having discriminated nothing. `1.5:6`'s own rule ("An assertion
that passes both is a printer") is defeated by pointing it at the wrong "both".

**Remedy:** replace `d81bc0a` with `cf16967` everywhere in `1.5` / `2-plan` / `0-baseline`, and
correct `0-baseline.md:3`.

## MAJOR M2 — two of C4's five clauses are printers: the strings do not exist anywhere in Architect's stage files.

`1.5:16` (C4, gating) requires the absence of *"no provenance-record requirement, no closed-set
input enumeration"*; `0-baseline.md:61-62` declares both as DROPs from `redteam-split.md`.

Measured: `grep -rni "provenance|closed set|verbatim record|sha256"` over
`Architect/stages/` returns **zero hits in `redteam-split.md` and zero in `redteam.md`**. Those
concepts are `guarded-change`'s charter (`stages/charter.md`, "Provenance is part of the review
record", "Reviewer input is a **closed set**"), not Architect's. The DROP claim traces to
`Architect-rulings.md:49-50` — an agent-authored gloss on 3666 — not to any Architect file.

By `1.5:6`'s own rule those two clauses are printers and C4 must be recorded `verified = no`
unless narrowed. **Remedy:** delete the two clauses from C4 and from `0-baseline.md`'s DROP list.

## MAJOR M3 — C13's `≤ 6 dispatched agents` scores permitted behaviour as failure.

One divider + three reviewers per round (`node.md:41`; `divider.md:96`). Round 1 = 4 agents.
**Round 2 = 7.** The four-round cap that C7 gates on preserving (`1.5:24`) therefore permits up to
13 agents, while C13 (`1.5:38`, gating) fails at 7. A single rejected first cut — the *designed*
response to a bad seam under 3666 — fails a gating criterion. **Remedy:** set the threshold at
two rounds (≤ 7–8) or state that C13 asserts round-1 convergence and say why that is the bar.

## MAJOR M4 — C13/C18's wall-clock axis is confounded by dispatch mode, which the plan never holds constant.

`SKILL.md:92-93`: *"Dispatch serially unless you have reason to think parallel is safe."* HEAD's
commit message, from the measurement of the same run: *"Serial dispatch — an orchestrator
instruction, not the design's — **accounts for ~50 of the 107 minutes**; the apparatus accounts
for the rest."* C13's `≤ 30 minutes` and C18's wall-clock trend therefore measure a variable this
change does not touch: run iteration 4 in parallel and the threshold is met whatever the prompts
say; run it serially at the baseline's 7 min/review and one round of three reviews plus a
derivation is already ~25 minutes. **Remedy:** state the dispatch mode in `1.5`'s behavioural
preamble and hold it identical to baseline (serial). One line.

## MAJOR M5 — C15 is a gating criterion a correct run can fail, and it pays out on the B3 failure mode.

`1.5:40`: *"At least **2 of the 3** round-1 split reviews are ≤ 6 KB and are accepted rather than
re-run … Probabilistic; one division, three reviewers."* Under 3666 a **rejection with
explanation** is a correct output and has no size bound; two correct rejections of a genuinely bad
round-1 cut fail C15 while the system works as designed. The criterion also cannot distinguish a
short, well-founded approval from the vacuous one-line approval B3 produces. A gating criterion
that the author labels probabilistic at n=1 and whose 6 KB figure has no derivation is not a gate.
**Remedy:** make C15 advisory (its purpose — "short is conforming" — is a trend, and C2 is the
textual gate), or restrict it to reviews that **approved**.

## MAJOR M6 — C13 and C17 are in direct tension, and C17's injection creates the two-writer race the plan declares out of scope.

C13 wants round 1 to converge (see M3). C17 (`1.5:42`) requires *"After round 1 has been written
to `divide-0.md`, a **fresh** divider agent dispatched on the same path resumes at round 2"* — if
C13 succeeds, the run's `divide-0.md` never has a round 2 to resume to and C17 is unverifiable on
that run. Both are gating.

Worse, `2-plan.md:81-83` specifies the injection *"on the same output path"* while the real
divider may still be appending to it: two dividers writing one append-only file. `2-plan.md:102`
declares that case explicitly out of scope: *"any handling for two dividers racing on one path
(the node dispatches one divider per call)"* — the C17 test manufactures the one situation the
design assumes cannot arise, in the live run directory whose artefacts C13/C14/C15/C16 are read
from. **Remedy:** run C17 against a **copy** of `divide-0.md` in a scratch path. No design change.

## MAJOR M7 — the divider memo has a second reader; the plan's own stated test for "the design is wrong" fires.

`2-plan.md:60-62` and `2-plan.md:96`: *"read only by a restart of this call … **Nothing else reads
it. If a reviewer finds a second reader, the design is wrong.**"*

Two other readers exist today and are unchanged by this plan:
- `node.md:50-51` — on `FAILED_TO_DIVIDE`, *"**hand up the divider's output file** — it records
  every split tried and every finding standing. Log the escalation to `<run>/decisions.md`."*
- `divider.md:117-118` — *"On the `FAILED_TO_DIVIDE` path **that record is what the owner will be
  shown**."*

So `divide-<iter>.md` is simultaneously (a) the resume point, (b) the node's escalation payload,
and (c) the owner-facing record. I do **not** think this makes the design wrong — per-round
appends arguably improve (b) and (c) — and I do **not** recommend adding a schema (`2-plan.md:101`
correctly excludes that under record 3497). The finding is that **the claim is false and the
plan's own falsification test has fired**, so the risk row cannot stand as written, and the plan's
§7 must say the file remains readable as an escalation record (i.e. the answer section is still
written, which `2-plan.md:58` does say — good).

Separately on the same item: **I do not find a violation of `node.md:8` ("Do not build a
coordination protocol")**. That rule targets using the filesystem as the *join* between distinct
agents (`node.md:6-9`, *"`return plan` **is** the join … no status file to publish"*). Here the
writer and the reader are the same logical call, which is precisely the shape `node.md:30-31`
sanctions for its own memo. Clean on that sub-question.

## MAJOR M8 — unratified inflation (CH12/RAT2): 3666 does not repeal record 3438's "findings carried forward", but the spec says it does, and the deletion pushes reviewers toward rejection.

`1-spec.md:80-82`:

> 3438's *"findings carried forward"* clause is what 3666 replaces: there is no longer a category
> of standing finding that accompanies an approval.

Record 3438, verified verbatim at transcript line 3438: *"okay, up the attempts to 4, and 2/3
agreement is two of the three reviewers **either endorsing or at least not objecting to going
forward with with their findings carried foward**"*. Record 3666, verified verbatim at line 3666,
contains **no** reference to agreement, to findings, or to what travels down with a sub-task; it
speaks only to what each *instruction* boils down to.

The binary approve/reject verdict **is** entailed by 3666 ("approve; otherwise, reject with
explanation") — I accept that much. What is **not** entailed is the removal of the third channel
3438 created: a reviewer that would keep the joint but has a real observation, whose observation
is *attached to the sub-task it bears on* (`divider.md:34-36`). Under the plan there are exactly
two outlets (`2-plan.md:22-23`): approve, and the observation is lost; or reject, forcing a
re-derivation of a cut the reviewer just said was right. **That is the reviewer-behaviour incentive
the change is trying to remove, re-created in the opposite direction** — and `redteam-split.md:13-15`
records that reading standing findings as disagreement is what *"killed the first two runs"*.

Per CH12 this is an elaboration introducing an operative commitment (a division of responsibility)
absent from the ratified phrase. It ranks major and is **owner-answerable, not author-answerable**.

**Note for the escalation, since it narrows the question:** `1.5:48-49` declares a stop-for-human
for *"reviewers disagreeing about whether 3666 repeals the four-round machinery."* I do **not**
disagree on that axis — see the all-clear at RAT1 below. The trigger as worded would therefore not
fire on this finding. The axis to put to the owner is narrower: *when a split reviewer approves a
cut but has a real observation about the seam, does that observation still travel down with the
sub-task (3438), or is it dropped (the spec's reading of 3666)?*

## MAJOR M9 — C11's oracle contradicts itself between `1.5` and `2-plan`, and the positive half is a printer.

`1.5` places **C11** under the heading *"Textual — regression (the baseline's CARRY list)"* — i.e.
an assertion that must hold before and after (it is `0-baseline.md:53-54`'s regression-bar item 6).
`2-plan.md:72` places it in the opposite group: *"Every C1–C5 **and C11** assertion **must fail**
there and pass on the new files."*

Measured: the pre-change files already state it — `divider.md:60-67` (*"There is no channel between
the halves … spawns both halves **concurrently** … building a channel is forbidden by name"*) and
`redteam-split.md:45-53`. So a positive assertion on the concurrent/blind statement **passes on the
old file** and is a printer by `1.5:6`. Only C11's second half — the *length bound*, `≤ 3 lines per
file on this topic* — can discriminate, and no mechanism is given for measuring "lines on this
topic" in `check.sh`; "this topic" is not a `grep`-able predicate. As written C11 is a gating
criterion with a self-contradictory oracle and no executable discriminator. **Remedy:** state C11
as CARRY (matching `1.5`), and make the discriminating assertion a concrete one — e.g. absence of
the three-destinations block's own strings, which *is* greppable.

## MAJOR M10 — two rules are lost from `redteam.md` that are neither restated nor on the declared DROP list. By `0-baseline.md`'s own rule that is a regression.

`0-baseline.md:57`: *"A CARRY item that stops being stated is a regression. A deliberate DROP must
be named in this run's `2-plan.md`."* `1-spec.md:127-129` claims only one thing needs restating:
*"removing `redteam.md` … removes the floor bound … **That bound** must be restated."*

I enumerated `redteam.md` rule by rule against the plan. Full table in the appendix; two items are
neither restated nor declared:

- **`redteam.md:54`** — *"You are graded on **precision** — are your findings real? — not on how
  many you raise."* No equivalent in `common.md` (checked: `grep -rn "graded on"` returns this line
  only). This is the sole counterweight to the exact dynamic `1-spec.md:14-15` diagnoses as the
  cause of the problem — *"reviewers graded on finding defects find them at whatever grain is
  available."* The change deletes the sentence that says otherwise while citing the behaviour it
  prevents as the motivation. `2-plan.md:35-36` (C2, "a one-line approval is a correct output")
  covers part of it and is the right instinct, but "a short approval is allowed" is weaker than
  "you are not scored on finding count."
- **`redteam.md:43-44`** — *"**Do not self-censor a lone observation.** … File it even if you
  suspect the other two will not."* `common.md:9-11` is a partial backstop (*"do not hedge toward
  an imagined middle"*), and `common.md:54`'s *"Findings are merged, never voted on"* is the other
  half — but that clause is the one B2 shows now contradicts the new voting mechanism. Under
  approve/reject with unanimity required in rounds 1–3, a lone rejection is far **more**
  consequential than a lone finding was, so the rule matters more at the moment it disappears.

Neither appears in `0-baseline.md:59-64`'s DROP list. **Remedy:** either restate them (one line
each in `redteam-split.md`) or name them as deliberate DROPs. This is not new apparatus; it is the
run's own CARRY/DROP bookkeeping applied to two rules it missed.

---

## MINOR m1 — C9 restates a sentence that is already there; the operative guard from `redteam.md` is a different sentence and is not carried.

`2-plan.md:37-39` gives C9's implementing text as *"do not reject for a lack of detail — a
sub-task is not required to be detailed, only to be a coherent whole task above the floor. **This
is the sentence that replaces the guard `redteam.md` used to supply.**"*

That sentence is already in the pre-change `redteam-split.md:32-33` almost verbatim (*"You are not
looking for vagueness — a sub-task is not required to be detailed, only to be a coherent whole task
still above the floor"*). The guard `redteam.md` actually supplied is the imperative at
**`redteam.md:18`**: *"**Do not file a finding whose only remedy is to decompose below the
floor.**"* That is the form C14 tests for (`1.5:39`, *"no rejection whose only remedy is to
decompose below the stated floor"*) — so the behavioural criterion tests a rule the textual
criterion does not require. `common.md:31-34` backstops the rationale but not the imperative.
**Remedy:** use `redteam.md:18`'s wording in C9. One line.

## MINOR m2 — C12's oracle has no reference value.

`1.5:29`: *"`~/Documents/Architect.md` is unchanged … Oracle: `sha256` compare." `0-baseline.md`'s
frozen table (lines 7-12) lists four files, none of them `Architect.md`, and no hash for it appears
in any of the four artifacts. Compare against what? (For the record, its current hash is
`d36e6942e64528c4a9a89fe79a1125b072264adfef9f43c7a858713ba4591594`.) **Remedy:** record it in
`0-baseline.md`.

## MINOR m3 — `node.md:47` still says `FAILED_TO_DIVIDE` means *"**three** rounds ran"*.

C7 (`1.5:24`) asserts the four-round cap in `divider.md` only. `node.md:47` is the node's own
statement of the same contract and says three. Pre-existing (it is at `d81bc0a` too), not caused
by this change — but `node.md` is already in the touched-files list (`1-spec.md:138`) for a
one-line dispatch check, and C6/C7 are this run's return-contract criteria. Cheap to fix while the
file is open; I would not open the file for it alone.

## MINOR m4 — two stale `redteam.md`-for-split-reviewers sites that C5 does not cover.

C5 (`1.5:17`) covers `divider.md`'s dispatch line and `SKILL.md`'s Roles row. Not covered:
- **`SKILL.md:81`** — *"`<ABS>/Architect/stages/<role>.md`   (+ **the aiming file, for
  reviewers**)"*. After the change `redteam-split.md` is standalone (`2-plan.md:29`), so the
  parenthetical is half-wrong for one of the two reviewer kinds.
- **`redteam.md:6-9`** — the table *"| Split reviewer | `redteam-split.md` |"*, in a file
  `1-spec.md:142` declares Not touched. No agent acts wrongly on it (the split reviewer no longer
  reads the file), so the impact is drift, not behaviour — but it is the two-copies-of-one-fact
  pattern, and it is one line.

## MINOR m5 — wrong commit attributed for the three-destinations apparatus.

`1-spec.md:109-111`: *"The clause was already removed in commit `0d6c229`, which replaced it with a
three-destinations apparatus."* Measured: `git show 0d6c229:Architect/stages/divider.md |
grep -c 'Three places'` = **0**; same for `fcf7e4d` and `d81bc0a`; = **1** at `cf16967`. The
apparatus was introduced by `cf16967` (whose message says *"the producer/consumer clause removed
from `divider.md` and replaced with a self-contained-seam rule; matching check in
`redteam-split.md`"*). Same root cause as M1.

## MINOR m6 (lens 3, missed opportunity) — the design cannot attribute its own result.

`0-baseline.md:31-37` isolates a single line as the mechanism of the cost: *"What forced each
re-derivation was `divider.md:97-98`"*, a rule that *"contradicts the same file's own §… six lines
above it, and it is the rule that actually executed."* Deleting those two lines is a
one-line change with the same claimed benefit. The plan rewrites two files wholesale
(`2-plan.md:5-7`, justified on "surviving apparatus load-bearing by inertia" — a reasonable
argument, but an argument, not a measurement), and C13/C18 measure the two together. If iteration 4
comes in at 4 agents / 20 minutes, nothing in the design says how much of that was 3666 and how
much was deleting line 97. Not a blocker — the owner instructed the rewrite — but worth one
sentence in `decisions.md` acknowledging the result is unattributed, rather than letting a future
reader read C13 as evidence for the 3666 rewrite specifically.

---

# CH8 — coverage challenge: behaviours this change can alter that **no** criterion observes

1. **The arguments the divider hands its reviewers.** Scenario in B3. C1 observes that the two
   questions are *stated*; nothing observes that the reviewer is given what it needs to answer
   them, and C15 pays out on the vacuous approval. **Highest-impact gap.**
2. **`common.md`'s severity/citation rules acting on the split reviewer.** Scenario in B2. C4
   sweeps two prompt files; nothing reads the run's own review artefacts for reintroduced
   severity/lens vocabulary. A one-line criterion on the *output* ("no run split-review uses
   blocker/major/minor/nitpick") would observe it, and it is checkable off the same `it4/0/`
   artefacts C14 and C15 already read.
3. **Everything below node 0.** All five behavioural criteria (`1.5:33`, *"the path exercised is …
   iteration 4 … node 0"*) read `it4/0/`. The change alters the divider and split reviewer at
   **every** node. Scenario: node `0.1`'s divider drops the sub-task's source-material pointer —
   regression-bar item 4 / record 3119 — and C10 observes only that `divider.md` *says* to carry it.
   C16 ("at least one child returns a plan or leaf output") passes with a plan built on a
   source-less sub-task.
4. **The `FAILED_TO_DIVIDE` outcome is unscored.** If the leaner reviewers reject four times, C13
   ("produces one of the three answers") **passes** while C16 ("spawns children or leaves")
   **fails** — a correct answer scored as a failure of the change, with no rule saying which reading
   governs. `1.5` should say whether `FAILED_TO_DIVIDE` at node 0 is a pass, a fail, or a re-run.
5. **The owner-facing escalation record.** Item 2 changes `divide-<iter>.md` from one end-of-call
   write to per-round appends. On the `FAILED_TO_DIVIDE` path that file is what the owner is shown
   (`divider.md:117-118`). No criterion reads it for legibility or completeness as an escalation
   payload.
6. **Whether a resumed divider can actually continue.** C17 observes only *which round it starts
   at* (`1.5:42`). `2-plan.md:56` specifies each section as *"the split proposed and the three
   verdicts"* — but `2-plan.md:22` says the next round is cut *"using the reason"* from the
   rejection. If a verdict is recorded without its explanation, the resumed divider starts at round
   2 (C17 passes) having lost the only input that makes round 2 different from round 1. **Remedy:
   `2-plan.md:56` should say "the three verdicts **with their rejection explanations**"** — a
   wording fix to a section spec, not new apparatus.
7. **The plan reviewer's dispatch.** `SKILL.md`'s Roles table is edited; a botched edit to the
   adjacent row (`SKILL.md:71`) breaks plan review. C16 observes it only if the tree gets that deep.
   Low impact — a `check.sh` assertion on the plan-reviewer row costs one line.

# CH9/CH10 — label audit

No criterion is `verified` yet (stage 3, pre-build), so the audit is of the **design** of the
verification table, per gating criterion:

| # | Governed path | Does the stated oracle exercise it? |
|---|---|---|
| C1–C3 | text of the two rewritten files | Yes — positive assertions at named sites; discriminating (the strings are absent pre-change at `cf16967`). |
| C4 | absence of plan-review apparatus **in the split reviewer's context** | **No** — sweeps 2 of the 3 files that context comprises (B2), and 2 of its 5 clauses are printers (M2). |
| C5 | dispatch sites | Partial — misses `SKILL.md:81` and `redteam.md:6-9` (m4). |
| C6, C8, C10 | CARRY text | Yes; the delete-the-line self-test at `2-plan.md:73` is a sound discriminator. |
| C7 | four rounds / 2-of-3 | Yes in `divider.md`; `node.md:47` contradicts and is unobserved (m3). |
| C9 | the floor guard | Asserts the wrong sentence (m1). |
| C11 | producer/consumer residue | Self-contradictory oracle; positive half is a printer (M9). |
| C12 | `Architect.md` unchanged | Sound mechanism, **no reference value recorded** (m2). |
| C13 | division cost | Baseline figures wrong (B1); agent threshold fails permitted behaviour (M3); clock confounded by dispatch mode (M4). |
| C14 | floor bound survives | Sound, and it is the right shape — reads the run's own verdicts, not the prompt. n=1 per reviewer; acceptable, since the alternative is a behavioural harness and record 3497 forbids building one. |
| C15 | short approval conforming | Fails on correct behaviour; rewards B3 (M5). |
| C16 | run gets past the division | Sound; ambiguous on `FAILED_TO_DIVIDE` (CH8 #4). |
| C17 | memo resume | Injection design sound in principle; tension with C13 and two-writer race (M6); observes start-round only, not resumability (CH8 #6). |

**C18's advisory label is legitimate, not a dodge.** `1.5:43` makes the gate C13's absolute
thresholds, and C13's thresholds (≤6 agents, ≤30 min) are **stricter** than C18's ≥60% would be
against the true baseline (13 → ≤5.2 agents is stricter; 107 → ≤42.8 min is looser). C18 is
redundant rather than relabelled-to-avoid; the correct remedy is to fix C13's calibration (B1/M3),
not to promote C18.

**`1.5:50-51`'s claim** — *"C13–C17 are verified by the real run; none is deferred and none is
checked by a proxy"* — is right in principle (route (a), the real skill on the real task, is the
strongest possible answer to the measurement-apparatus problem and I want to say so plainly). It is
wrong in three particulars: C13 against a wrong baseline, C15 against a proxy for review quality
(byte count), and C17 against a proxy for resumability (start round).

# CH11/CH12 — ratification audit

**RAT1 — the ruling this change implements. AUDITED, VALID.**
- *Flagged axis:* what the divider's and the split reviewer's instructions should be.
- *Owner's verbatim words, with durable source I read myself:* transcript line **3666**,
  `type: user` — *"the dividers instruction should boil down to this: Find a natural seem in the
  given task, and split it into two pieces at that seem. The reviewers instruction should boil down
  to: Is this split at a natural seem? If it is, does it reduce the task past the point of maximum
  granularity?  If it is a natural split, and does not reduce past the point of maximum
  granularity, approve; otherwise, reject with explanation."*
- *Spot-check of the spec's quotation:* `1-spec.md:27-31` reproduces it **character-for-character**,
  including the two spellings of "seem" and the double space before "If it is a natural split".
  Clean.
- *Mapping:* the owner's words state the divider's job (find a natural seam, split there) and the
  reviewer's two questions and binary verdict directly. No option-resolution was required; this is
  an instruction, not a selection among author-presented options.

**The worked example is also genuinely the owner's, and the spec under-cites it.** `1-spec.md:33-39`
sources it to `Architect-rulings.md`, an agent-authored file. I found the primary records:
**line 3628** (`type: user`) is the owner giving the four-file / {a,b},{c,d} split verbatim, and
**line 3634** (`type: user`) is the owner's correction: *"the merging would get done automatically
in the second pass of the task.empty() while loop."* The spec's use of it is therefore ratified —
but `2-plan.md:94` leans on it for the single largest accepted consequence of the change ("the real
defects go unraised") while citing only the derived file. **Cite 3628/3634 directly.** Minor, and I
mark it clean on substance.

**RAT2 — elaborations checked against 3666's operative terms** ("natural seam", "the point of
maximum granularity", "approve", "reject with explanation", "boil down to"):

| Elaboration | Verdict |
|---|---|
| Divider's job = find a natural seam, split there (`2-plan.md:13`) | Entailed, verbatim. |
| "maximum granularity" pinned to the run's `granularity` floor (`common.md:27`, `2-plan.md:17`) | Correct pin — "maximum granularity" is the finest permitted, i.e. the floor. Not a proxy. |
| Binary approve / reject-with-explanation (`2-plan.md:33-34`) | Entailed, verbatim. |
| "One-line approval is a correct output" (C2) | Entailed by "approve" being a terminal verdict with no stated form. |
| **Unanimity in rounds 1–3, 2-of-3 after round 4** (`2-plan.md:22-26`) | Not in 3666 — but entailed by **3402** (*"if the third attempt doesn't reach unanimous agreement, go with whichever division plan had 2/3 agreement"*, verified at line 3402) and **3438** (*"up the attempts to 4"*, verified at line 3438). Clean. |
| **"3666 does not repeal the four-round / 2-of-3 / `FAILED_TO_DIVIDE` machinery"** (`1-spec.md:78-82`, `2-plan.md:93`) | **I agree, and this is an earned all-clear on the axis `1.5:48` names.** 3666's text is scoped to what each *instruction boils down to*; it contains no word about attempt counts or return signals, and 3402/3438 are separate rulings on a separate axis. Nothing in 3666 disturbs them. |
| **"3438's *findings carried forward* clause is what 3666 replaces"** (`1-spec.md:80-82`) | **UNRATIFIED INFLATION — see M8.** |
| "The split reviewer stops reading `redteam.md`" (`1-spec.md:66-71`) | A reasonable implementation of "boil down to", but note B2: as an implementation of *"does not produce a severity table"* it is **incomplete**, because the severity table is not in `redteam.md`. |

# Lens summary

- **Lens 1, factual — NOT clean.** B1 (baseline vs `it3/0/` artefacts, `decisions.md`, `cf16967`),
  B2 (`grep` locating the severity table and the cite rule in `common.md`), M1 (`git rev-parse`,
  `git diff --stat`, hash comparison), M2 (`grep` returning zero), m5 (`git show` per commit).
- **Lens 2, logical — NOT clean.** B3, M3, M5, M6, M9, CH8 #4, CH8 #6.
- **Lens 3, missed opportunity — one finding.** m6 (attribution). I deliberately raise nothing else
  here: the plan's restraint at `2-plan.md:98-103` is correct under record 3497 and I am not going
  to ask for apparatus.
- **Lens 4, unstated assumptions/risks — NOT clean.** B2 and B3 are both "the assembled prompt is
  what the reviewer reads, not the file we edited"; M4 (dispatch mode assumed constant); M7 (the
  single-reader assumption, falsified by the plan's own test); plus the CH8 section above.
- **Lens 4, position sub-lens — fires and is partly handled.** The plan deserves credit: it
  correctly identified that removing `redteam.md` is a position-sensitive edit and wrote C9 for it
  (`1-spec.md:125-129`). The defect is that it enumerated **one** displaced element. B3 (the inputs
  line, `redteam.md:11`), M10 (`redteam.md:43-44`, `:54`) and m1 (`redteam.md:18` vs the sentence
  C9 actually asserts) are the rest of the enumeration.
- **Lens 4, concurrency sub-lens — fires once.** M6's two-writer injection on the live
  `divide-0.md`. The memo design itself is single-writer and clean (M7's second half).
- **Lens 5, fidelity — one major.** M8. Otherwise the terms pin correctly; see the RAT2 table. The
  reverse question I was asked to attack — *is the plan keeping apparatus 3666 tells it to cut?* —
  answers **yes, via B2**: the severity model survives in `common.md`, which the plan lists as Not
  touched, and `Architect-rulings.md:49-50`'s gloss on 3666 says in terms that the split reviewer
  *"does not produce a severity table."*

# What I could not check

- Whether `oracles/check.sh` and `oracles/selftest.sh` discriminate as claimed: **they do not
  exist yet** — `ls changes/divider-3666/` shows only the four stage artifacts. Every oracle
  judgement above is on the *specification* of the oracle.
- Whether iteration 4's task string is recoverable verbatim: `2-plan.md:77` says it is *"taken
  verbatim from `runs/data-distiller/decisions.md`"*, but `cf16967`'s message states *"**THE RUN'S
  TASK ARGUMENT WAS NEVER WRITTEN DOWN** — recovered from a divider's paraphrase inside an artifact
  the ledger declares void."* I found the task text at `it3/0/split-round-1.md:9-22` (the divider's
  §0 "verbatim, as received") but did **not** verify a task record in `decisions.md` itself; I
  sampled its tail only. **If it is not in the ledger, C13–C17 are not run on the same task as the
  baseline, and `2-plan.md:77` is false.** The runner should confirm this before stage 8 — it is a
  one-`grep` check and it gates every behavioural criterion.
- The pre-change review artefacts' contents (I read the directory listing, `divide-0.md`'s head and
  `split-round-1.md`'s head only, per the sampling instruction). Claims about the *content* of the
  eleven/twelve reviews in `0-baseline.md:29-31` are unverified by me beyond their sizes and mtimes.

# Appendix — `redteam.md` rule by rule: what the split reviewer loses

| `redteam.md` | Content | Disposition |
|---|---|---|
| 1-10 | "You are a red-team reviewer" + the aiming-file table | Structural; `2-plan.md:29` makes `redteam-split.md` standalone. **Handled.** |
| **11** | *"Common to both: the **task** and the **granularity floor**."* | **SILENTLY LOST — B3.** |
| 13-18 | The floor bounds what you may call vague; *"Do not file a finding whose only remedy is to decompose below the floor."* | Partly restated (C9), but the operative imperative at :18 is not — **m1**. Rationale backstopped by `common.md:31-34`. |
| 20-36 | The six lenses | **Declared DROP** (`0-baseline.md:61`), C4. Correct. |
| 38 | *"was any portion of the task left unaddressed?"* | Dropped with the lenses. Accepted consequence — `2-plan.md:94`, on 3666 + records 3628/3634. Note the loop backstop is real: an orphaned remainder surfaces when the red-team sees the merged result against the original task (`node.md:104-108`). |
| 42 | *"'No issue found' per lens is expected."* | Superseded by C2. **Handled.** |
| **43-44** | *"Do not self-censor a lone observation."* | **UNDECLARED DROP — M10.** Partial backstop `common.md:9-11`, `:54` (but see B2). |
| 45-50 | The three earned-clean clauses | **Declared DROP**, C4. Correct — and `1-spec.md:63-65` is right that they make a one-line approval non-conforming. |
| 51-52 | *"You do not contest severities."* | Moot once severities go — except they do not go (**B2**). |
| **54** | *"You are graded on **precision** … not on how many you raise."* | **UNDECLARED DROP — M10.** No backstop anywhere in `common.md`. |

*(For completeness: the "provenance record" and "closed-set enumeration" that `0-baseline.md:61-62`
declares as DROPs appear in no row above because they appear in no Architect file — M2.)*
