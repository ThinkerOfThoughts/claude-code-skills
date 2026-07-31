# Split review — round 3, reviewer B

Reviewing: `Architect/runs/data-distiller/0/split-round-3.md` (the proposed division of "Plan the
implementation of the Data-Distiller skill" into a **driver plane** and a **worker plane**).

Inputs I was given and used: the task, the granularity floor, the proposed division. **No plan
exists and I was given none** — I judged the cut against the shape of the task, not against any
plan. I did not read `Data-Distiller/` and did not read any sibling `split-review-*.md`.

**Overall: the joint is real and I would keep it. Three `major` findings stand, all of them in the
same place — the seam's remaining crossing objects are named but not given semantics.** Round 3's
structural move (driver hands down every path and value) genuinely deleted the schemas, the layout
and the config key set from the interface. What it did not do is finish the two objects that still
cross in both directions: **the item locator** and **the status record**. Both are now carrying more
load than round 2's explicit schemas did, with less specification.

---

## Verdict by lens

| Lens | Verdict |
|---|---|
| Factual | 1 minor (M-1). Citations otherwise check out — table below. |
| Logical | 1 major (MAJ-3), 1 minor (M-4). |
| Missed opportunity | 1 minor (M-2). |
| Unstated assumptions & risks | 1 minor (M-6). |
| Fidelity | 1 minor (M-3). Terms pinned — list below. |
| Completeness | 2 major (MAJ-1, MAJ-2), 1 minor (M-5), 3 nitpicks. Generative sweep run — see below. |

Answering the four aiming questions directly:

1. **Coverage** — every named property of the task is assigned. One element is orphaned: the
   *predicate* for the status record's outcome word (MAJ-2).
2. **The seam** — stated, and far better than round 2's. Unsound on two crossing objects (MAJ-1,
   MAJ-2).
3. **The floor** — **clean.** Five files per half against a floor of one file with its content
   specified. Neither half is near it. No blocker here.
4. **Real joint or arbitrary cut** — **real joint.** Something concrete differs across it (below).

---

## Findings

### MAJ-1 — `major` — The item locator is the seam's busiest object and its only unspecified one

`split-round-3.md:179-183` (S3) fixes the manifest as *"one entry per analyzable item, each entry
beginning with a unique, filesystem-safe item id on its own line, followed by that item's locator.
Everything else in an entry is the worker plane's business."*

Note the asymmetry: the seam went to the trouble of fixing **line-level placement for the item id**
and gave the locator nothing — no delimiter, no label, no statement that it is a single line, no
statement of what it must contain. Yet by the time you trace the rest of S2/S6/S7, that one
unspecified string is carrying **four separate loads**:

1. **It is the driver's extraction target.** S2 (`:170-171`) hands the analyst *"its item's locator
   (as written in the manifest)"*. The driver-plane planner must write, into `stages/node.md`, an
   instruction for pulling the locator out of an entry whose format the seam declares to be *"the
   worker plane's business."* S3 says the entry continues after the locator, so the locator's **end**
   is undefined. A worker planner is free to write a multi-line locator (path + line range + note)
   or a labelled field among several labelled fields; a driver planner reading only S3 will most
   likely write "take the line after the id." **These two halves never see each other, so nothing
   reconciles them** — and every analyst, verify and merge dispatch depends on the result.
2. **It is the only channel for the item's over-size strategy.** S7 (`:216-220`) puts `window` and
   `sample` execution in the analyst, and sub-task two's file 3 (`:260-261`) requires
   `stages/analyst.md` to *"say what an analyst does when its item's strategy is `window` or
   `sample`, and how the omission is recorded."* But **`strategy` is not in the analyst's S2
   payload** (`:170-171`: locator, index *k*, off-limits, output path), and S2 declares itself
   exhaustive — *"the driver hands every worker exactly the arguments below."* The analyst is
   therefore required to act on a value the seam says it is not handed. The only route left is
   inside the locator — and **nothing in the seam says so.** The worker planner may notice and route
   it there; it may equally write "your item's strategy" as an input it does not have.
3. **It is the only corpus address `verify` gets.** S2 (`:174-175`) hands verify the item's locator
   and no corpus root (only `decompose` gets the corpus root, `:170`). So the locator must be
   self-sufficient for re-opening a citation — which is a real constraint on its content that the
   seam does not state.
4. **It is what makes the coverage note reachable.** S6 (`:209-214`) requires the terminal
   deliverable to name which items were `window`/`sample`. That chain begins at load 2 above. If the
   strategy never reaches the analyst, the coverage note has nothing to report and **the deliverable
   silently claims full coverage of items that were sampled** — a wrong-answer failure, not a crash.

**Failure scenario, concretely.** Worker plane writes decompose.md to emit entries as
`## <item-id>` / `- source: <path>` / `- strategy: window` / `- size: 412kB`. Driver plane writes
node.md to *"take the item id from the entry's first line and the locator from the line that
follows."* Every analyst is dispatched with the string `- source: <path>`, the strategy is dropped,
and S6's coverage note reports nothing omitted.

**Why this is `major` and not `minor`:** the remedy is small (fix the locator's delimitation and
state that it is the carrier for anything per-item the worker plane needs downstream), but the
missing thing is a load-bearing contingency on the **only artifact that crosses the cut in both
directions**, and neither half can supply it unilaterally without becoming the divergence.

### MAJ-2 — `major` — The driver is required to author an artifact whose shape the other half owns, and `partial` is defined on one side of the cut and consumed on the other

Two limbs, same object.

**(a) Shape ownership contradicts producer assignment.** S3 Invariant A (`:186-191`) says the status
record's *"other contents are the worker plane's business"* — and, three lines later, *"When a unit
fails before `merge` runs, **the driver writes the status record itself**, stating `failed`."*
Sub-task two's ownership list (`:277-279`) confirms the worker plane owns *"all fields … of the
status record beyond the one outcome word the seam fixes."*

So the driver-plane planner must specify, in `stages/node.md`, how to write a file whose format is
explicitly assigned to a half it cannot see. This is a direct violation of the division's own
governing rule at `:148-149`: *"Anything not fixed here belongs wholly to one half."* The status
record's shape is **not** wholly one half's business — it has two producers and one of them is
forbidden to know the format.

The best case is that the driver writes a minimal record carrying only the outcome word, and the
worker's `merge` writes a richer one. Then the run's on-disk state contains two shapes of the same
record, and the driver's own resume logic — which reads them (S4, `:197-201`) — must accept both.
Neither planner is told this.

**(b) `partial` has no predicate.** S3 fixes the vocabulary `complete | failed | partial` and stops.
Nothing says when `merge` emits `partial`; nothing says what the driver does on reading it. The
worker plane will define the emission rule (it writes the record); the driver plane will define the
reaction (it owns *"all control flow"*, `:128`). `complete` and `failed` are self-evident enough to
survive independent definition. **`partial` is not.**

**Failure scenario.** Worker plane defines `partial` as "some of this node's children failed; the
merge below reflects only the survivors." Driver plane, reasoning from the word alone, defines its
reaction as "a partial unit is not finished — re-dispatch it." The re-dispatched unit's children
fail identically and it returns `partial` again. The run does not terminate — against the exact
property sub-task one is made accountable for (`:80-81`, *"a run that terminates"*).

### MAJ-3 — `major` — `decompose` has no completion signal, so resume cannot trust the manifest

S3 Invariant A closes the write-order hole for units: *"It is written only after the unit's other
outputs are complete and closed — a unit with no status record is treated by resume as
incomplete."* The round-2 disposition table (`:468`) records this as the fix for the reviewer
finding *"Write-order/completeness rule for resume unowned."*

**It does not cover `decompose`.** S3 assigns the status record to `merge` (`:184-185`), and
`decompose` writes only the manifest. `decompose` is the first thing the run does and there is no
`merge` above it. So after a kill:

- The driver finds a manifest file on disk. Invariant A gives it **no way to tell a complete
  manifest from one truncated mid-write** — the completeness protocol it relies on applies only to
  units that end in a merge.
- Invariant B (`:192-195`) is no help: the return value that would have told the driver `decompose`
  finished lives in the dead process's context, which is precisely the state resume has lost.
- S4 (`:197-201`) permits the driver to read the manifest, so it can inspect it — but "does this
  markdown file look finished?" is not a completeness test, and the driver cannot know what a
  finished entry looks like anyway (see MAJ-1).

The two escapes both have unstated preconditions. **Escape 1 — always re-run `decompose` on
resume.** Then item ids must be *deterministic across re-runs*, or the fresh manifest's ids will not
match the status records already on disk and every completed item is re-analyzed or, worse,
orphaned. S3 requires ids to be *"unique, filesystem-safe"* and says nothing about stability.
**Escape 2 — never re-run `decompose` if a manifest exists.** That is the truncation bug above.

Either way a load-bearing contingency for the task's *"Restart and resume from on-disk state"* is
missing, and it sits exactly where the seam's two halves meet.

### M-1 — `minor` — "Dividing trades away independent corroboration of every step" is false

Alternative (a) (`:424-431`) states: *"an undivided task goes to **three** leaves and is merged by
`Consensus` … whereas a divided task goes to **two** children and is merged by `Union` … **Dividing
therefore trades away independent corroboration of every step.**"*

The first clause is accurate; the inference is not. Per `Architect/stages/node.md:41-53`, each child
is a **node**, not a leaf — it runs the same loop, calls `Divisible` on its half, and if that returns
`null` it dispatches *three* leaves and merges by `Consensus` (`node.md:45-49`). Corroboration is
therefore **deferred one level, not surrendered**. Every step of actual plan content is still
written by three cold leaves and voted 2-of-3.

Severity is `minor` because the error is in a rejected alternative's cost accounting and does not
flip the conclusion — it *overstates* the cost of dividing, which argues for (a), and (a) was
rejected anyway on the floor criterion. But it is a false claim about the execution model, standing
in the record as the reason a real alternative was priced.

### M-2 — `minor` — A manifest *directory* was not weighed, and would delete MAJ-1 outright

Four alternatives are weighed (`:422-448`), all of them alternative *cuts*. None is an alternative
*seam mechanism* for the one artifact that crosses. The obvious one, entirely in the spirit of round
3's own move: **have `decompose` write one file per item into a handed directory, with the filename
as the item id and the file's entire content as the locator.** The driver already hands down every
path (`:14-15`), so handing a directory instead of a file path costs nothing at the seam. Then:

- extraction becomes `listdir` + `read whole file` — no format agreement needed at all;
- the id/locator split is carried by the filesystem, not by a line-placement convention;
- the worker plane may put whatever it likes in the file (including the strategy) and the driver
  passes the file's content through opaquely, which is what S2 already claims to do.

Round 3's thesis is that the interface shrinks when the driver hands down structure. This is that
same move applied one object further, and it is the difference between a seam with a format
agreement in it and a seam with none.

### M-3 — `minor` — "Terse" is in the task and is not bound anywhere in the seam

Task: *"a coordinating agent never reads the findings themselves, only a **terse** per-child
status."* S3 Invariant A bans *"no finding text, no claim and no citation"* and hands everything
else to the worker plane. That is a good ban, but it is not the same property. A status record
reading "unit complete; 14 findings, 9 of them about authentication timeouts, 3 dropped at verify"
carries no finding text and arguably no claim, and would steer a coordinator's subsequent dispatch
decisions.

The structural oddity is the one the fidelity lens exists to catch: **sub-task one is made
accountable for the blind-roll-up barrier (`:130`) but sub-task two designs the record the barrier
is supposed to be blind to.** The half that owns the guarantee does not own the object.

### M-4 — `minor` — Resume granularity is unit-level only; the driver's sub-unit signal is file existence

Because the status record is written only at the unit level (S3, `:184-185`) and S4 forbids the
driver to open any findings artifact, the driver's only sub-unit resume evidence is **whether a path
exists**. Existence cannot distinguish a complete analyst output from a truncated one — the exact
distinction Invariant A was written to provide, provided only at the unit boundary.

The consequence is bounded and the driver owns the decision (re-dispatch the whole item, which is
correct and merely wasteful), so this is `minor` rather than a limb of MAJ-3 — but a driver planner
reading S3 may well believe Invariant A gives it a finer signal than it does.

### M-5 — `minor` — The stated joint does not describe two of the driver half's five files

The joint is stated as *"the reader's information state"* (`:383-388`): a driver-plane file is read
by an agent holding the run's context; a worker-plane file by a cold agent whose whole world is that
file plus its arguments.

That is a genuine and well-chosen property, and it correctly explains why `stages/node.md` is on the
driver side despite being a prompt. It does **not** describe `README.md` (`:118-120`), whose reader
is a human, or `METHODOLOGY.md` (`:96-102`), which both siblings describe as opened for orientation
and config setup rather than to run anything (`Guarded_change/METHODOLOGY.md:11`,
`Dragonfly/METHODOLOGY.md:10-11`). Those two are on the driver side because they are not worker
prompt files.

The cut is still real — the worker set has a sharp defining property and that is enough for a joint.
But the stated justification over-claims, and the division rejected alternative (c) partly on the
grounds that *"the small half is packaging, which is a partition rather than a joint"* (`:442`)
while placing that same packaging inside the driver half without comment.

### M-6 — `minor` — The context budget crosses the seam without a unit

S2 hands `decompose` *"the context budget an item must fit inside"* (`:170`). The worker plane must
write, in `decompose.md`, a rule that computes an item's size and compares it to that value — so
this is the one payload argument that is not passed through opaquely but **arithmetically compared
against a locally computed quantity.** Its unit (tokens? bytes? lines?) is fixed nowhere, and the
driver plane owns the config key that supplies it (`:130-131`).

Driver documents `context_budget: 150000` meaning tokens; `decompose.md` measures bytes; every item
is judged over-size and the whole corpus goes to `window`/`sample`. `minor` because one clause in S2
fixes it and the downstream plan red-team sees both halves unioned, so it is catchable — but it is
the same class as MAJ-1 and the two should be repaired together.

### N-1 — `nitpick` — S4 names a concrete filename the driver is supposed to own

S4 (`:197-198`) prohibits opening *"an analyst-findings, verified, merged, or `FINDINGS.md`
artifact"*, while S6 (`:209`) writes the same object as the placeholder `<the run's FINDINGS file>`
precisely because the driver owns all paths. One of the two is wrong; S6's form is the right one.

### N-2 — `nitpick` — Three citations overshoot by a line

- `Dragonfly/SKILL.md:29-70` for the run loop — line 29 is blank; `## Loop` is line 30.
- `Dragonfly/METHODOLOGY.md:152-153` for the `decisions.md` precedent — the `decisions.md` line is
  153; 152 is the tail of `incidental-ledger.md`.
- `Guarded_change/METHODOLOGY.md:175-182` for the same — the `decisions.md` paragraph is 175-180;
  182 begins **Ratification records**.

All three point at the right section. Noted for the record only.

### N-3 — `nitpick` — "unit" is used nine times at the seam and never defined

S3 and S6 turn on *"the unit's status record"*, *"a unit with no status record"*, *"when a unit
fails"*. From S2's merge payload it is inferable that a unit is an item or a roll-up node, so this is
not a blocking ambiguity — but it is the seam's central noun and it is undefined in a document that
defines `split`, `window` and `sample`.

---

## Factual lens — evidence consulted (earning the verdict)

| Claim in `split-round-3.md` | Checked against | Result |
|---|---|---|
| Cold-start guard at `Dragonfly/SKILL.md:22`, "Dragonfly only" | `Dragonfly/SKILL.md:22`; `Guarded_change/SKILL.md` headings | ✅ exact; GC has no such section |
| Run loop `Guarded_change/SKILL.md:25-52` | file | ✅ `## Loop` at 25, section ends 52 |
| Run loop `Dragonfly/SKILL.md:29-70` | file | ⚠ off by one (`## Loop` at 30) — N-2 |
| Method as fenced diagram, `GC/METHODOLOGY.md:37-54`, `DF/METHODOLOGY.md:47-62` | both files | ✅ both are fenced blocks at exactly those ranges |
| Config skeleton `GC/METHODOLOGY.md:103-152` | file | ✅ `## The config contract (Layer 2)` 103, section ends 152 |
| *Trigger* at `DF/METHODOLOGY.md:161`, "Dragonfly only" | headings of both | ✅ `## Trigger` at 161; GC has no Trigger section |
| Naming the operative copy, `GC/METHODOLOGY.md:143` | file | ✅ "lives written-in-full in `stages/stage-3.md` …" |
| `decisions.md` precedent `GC/METHODOLOGY.md:175-182`, `DF/METHODOLOGY.md:152-153` | both | ⚠ minor overshoot — N-2; content correct |
| Two layers `GC/METHODOLOGY.md:88-100`, `DF/METHODOLOGY.md:95-102` | headings | ✅ both exact |
| "run artifacts are markdown without exception" `GC:154-168`, `DF:141-153` | both artifact blocks | ✅ every listed artifact is `.md` in both |
| Config instance form `guarded-change.companion.md`, `dragonfly.companion.md` | `ls` of both skills | ✅ both exist; `data-distiller.<corpus>.md` matches `GC/SKILL.md:17`'s glob |
| `Guarded_change/stages/charter.md`, `Dragonfly/stages/charter.md` as cold-agent precedent | `ls` | ✅ both exist |
| Both siblings carry `README.md` | `ls` | ✅ |
| Undivided → 3 leaves + `Consensus`; divided → 2 children + `Union` (`node.md:44-53`) | `Architect/stages/node.md:41-58` | ✅ as to the immediate node; ❌ as to the inference drawn — M-1 |
| Halves plannable simultaneously without communicating (`node.md:50-53`, `leaf.md:16-19`) | both | ✅ via `node.md:50-53`; `leaf.md:16-19` is the leaf's inputs section and does not support the claim |

## Fidelity lens — terms pinned

| Loaded term in the task | Pinned to | Proxy or mechanism? |
|---|---|---|
| "decompose the corpus … size them … pick a per-item strategy" | `stages/decompose.md`, a dispatched worker writing a manifest; S7 resolves `split` inside it | mechanism ✅ |
| "N independent cold analyst agents" | S5: N separate cold spawns, none handed a sibling's path, plus `common.md`'s open-only-what-you-were-handed rule — **two non-overlapping rules binding two different actors** | mechanism ✅ — this is the strongest clause in the seam |
| "read-only over the corpus" | `stages/common.md` rule (sub-task two, file 1) | mechanism ✅ |
| "cites a source for every finding" | `common.md` cite-or-it-doesn't-count + analyst.md's re-openable citation | mechanism ✅ |
| "a cold verification pass that re-checks every citation" | `stages/verify.md`, itself a dispatched cold worker under `common.md`; brief requires it to define what "checks out" means | mechanism ✅ |
| "ranks by how many independent analysts agreed" | `stages/merge.md`; attribution carried by the analyst index *k* handed in S2 | mechanism ✅ (the *k* in the payload is what makes it computable) |
| "blind roll-up … only a terse per-child status" | S4 absolute read prohibition + S3 Invariant B closing the **reply** channel + Invariant A's content ban | mechanism ✅ on blindness; **"terse" unbound — M-3** |
| "a per-corpus configuration file … method stays corpus-agnostic" | driver-owned Layer-2 contract + S8's single-exception rule | mechanism ✅ |
| "restart and resume from on-disk state" | S3 Invariant A's write-ordering + driver's resume procedure in `node.md` | mechanism ✅ for units, **absent for `decompose` — MAJ-3** |
| "facts, not interpretation" | `common.md` rule | mechanism ✅ |

Invariant B deserves explicit credit: closing the **return-value** channel is the difference between
a real blindness barrier and a proxy for one, and round 2 did not have it.

## Completeness lens — the generative sweep

Beyond the four aiming questions, I asked what load-bearing thing the division's own structure does
not anticipate, and looked for: an artifact with no producer; an artifact with two producers; a
crossing value with a name but no semantics; a failure mode with no owner; a resume story with a
hole; the terminal deliverable's route to the human; anything the task names that no file covers.

Found: **two producers for one artifact** (MAJ-2a), **a crossing enum with no predicate** (MAJ-2b),
**a resume hole at the one stage Invariant A does not reach** (MAJ-3), **a crossing string with four
loads and no specification** (MAJ-1), **a crossing scalar with no unit** (M-6).

Swept clean: the terminal deliverable has a named producer, a named reader and a stated route to the
human (S6); the concurrency ceiling, stop-for-human, the gate/decision log, the trigger, packaging
and install are all assigned (`:126-133`); every named property of the task maps to at least one
file; `stages/common.md` no longer crosses the cut, so no file is co-owned; and there is no upward
channel or ordering dependency between the halves, which matches the concurrent-cold-agent execution
model at `Architect/stages/node.md:50-53`.

## The floor

**Clean, in the direction I am asked to check it.** The floor is one file created with its content
specified. Driver plane: five files. Worker plane: five files. Neither half falls below it, and
sub-task one's note at `:122-124` — that an install *action* has no shape under a file-phrased floor,
and is recorded rather than worked beneath — is the correct handling, not a violation.

I record without filing a finding that both halves could divide again, so the tree may go two or
three levels deeper on this branch. That is the execution model's business, not a defect in the cut.

## Real joint

**Real, not arbitrary.** What differs across the boundary, concretely: a worker-plane file is
**handed verbatim to a process with no other context**, so it may assume nothing and must be
self-sufficient; a driver-plane file is read by a process that already holds the config, the layout
and the run's history, so it may refer outward freely. That is a hard constraint on authoring, not a
label. The corrected failure sets at `:392-395` are genuinely disjoint now, and moving *steered* to
the driver side is right — the barrier that prevents steering is driver-plane, so the failure to
maintain it must be too.

---

## What I could not check

- I did not read `Data-Distiller/`, so I cannot say whether either half's file list matches a working
  implementation. Every judgment above is derived from the task, the seam and the two siblings.
- I did not read the other round-3 reviews, so I do not know whether these findings are shared.
- The round-2 findings table (`:450-479`) is the divider's own account of what prior reviewers said.
  I treated it as a claim, not as fact, and did not use it as evidence for anything. Its dispositions
  for the status record (`:454`) and the write-order rule (`:468`) are the two I checked against the
  round-3 text directly, and both are where MAJ-2 and MAJ-3 come from.

## If the loop ends here

Should these three majors stand and the divider return `null`, the resulting undivided task is not a
bad outcome: **all three findings are seam findings, and a single planner writing all ten files has
no seam.** The locator's format, the status record's shape and `decompose`'s completion signal all
become one author's internal consistency problem, which is where they are cheapest. If instead they
are repaired and the cut survives, the repairs are small and localized — delimit the locator and
declare it the per-item carrier; give the status record one owner or one fixed minimal shape and
define `partial`; extend Invariant A's write-ordering to `decompose`. **The cut itself I would keep
either way.**
