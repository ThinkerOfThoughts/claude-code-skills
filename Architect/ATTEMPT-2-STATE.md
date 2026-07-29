# Architect attempt 2 — resume point

**Read this first.** Written 2026-07-25 before a context compaction. It is the single place a fresh session
picks up. Everything below is settled unless marked OPEN; nothing needs re-asking.

**One-line status (2026-07-28, later):** **element 1 was RE-SCOPED by the owner** from "the red-team
charter" (one file) to **"the agent prompt set"** — six dispatched prompts plus a manifest, under
`Architect/stages/`. The set is **BUILT**, the two prior blockers are **CLOSED**, the **stage-8 harness is
built and run** (76/0 clean, 63/63 mutants — the first working oracle in this project), and **3 cold
reviewers were dispatched at gate 7**. **The run's own resume point is
[`changes/charter-2026-07/RESUME.md`](changes/charter-2026-07/RESUME.md) — read that before touching
anything in the run folder**, and read `changes/charter-2026-07/decisions.md`'s final entry for the
re-scope record. This file stays the project-level entry point.

> ⚠ **The set has not passed a gate yet — reviewers L, M and N were still the deciding evidence at the time
> of writing.** And **no behavioural verification exists for any of it**; the arms are cut on the owner's
> authority (record 1572). Text presence is not behaviour.
>
> ⚠ **`Architect/stages/charter.md` is now a MANIFEST, not a prompt.** It is not dispatched to any agent;
> it holds the fork provenance and the rule-allocation table. The dispatched prompts are the other six
> files. Absence of an `UNVETTED DRAFT` banner still does not mean "accepted."

---

## 0b. ⚠ DEBT ELEMENT 1 HANDS TO EVERY LATER ELEMENT — read this before starting element 2

**Element 1 (the agent prompt set) is built, has been through three cold gates, and is NOT clean.** Its own
resume point is `changes/charter-2026-07/RESUME.md` and its gate log is `changes/charter-2026-07/decisions.md`.
**What follows is only the part that leaves that folder** — findings a later element inherits, or that
element 1 could not fix because they belong elsewhere. **This list exists because the next element's runner
will not read element 1's run folder, and these will otherwise be rediscovered from scratch.**

### Owned by a specific later element

| # | What | Owner |
|---|---|---|
| **OOS-8 / OOS-11** | The config's `redteam_context` omits load-bearing paths — `Guarded_change/stages/{stage-1.5,3,4,8}.md`, and **six of element 1's own nine files**. Every reviewer set had to be given them as B15 supplementary context. **Amending it mid-run would have moved the goalposts.** | **Element 3** (Layer-2 config contract) |
| **NEW — subject-matter sources are not in the config** | A dispatched **divider** was observed searching the filesystem for a file its task named, because nothing in its closed set contained it. That is a config gap, not an agent fault. **The config must be able to name the sources a run's roles actually need.** | **Element 3** |
| **OOS-10** | The set lives in `Architect/stages/` and **Architect has no stages.** It is there only because the config names that path. | **Element 4** (router) |
| **OOS-14 (withdrawn as a gap, still real as a mechanism)** | There is **no assembly step** that composes `charter-common.md` + role file(s) and filters conditional sections per invocation. Element 1 states the composition rule and ships the files; **nothing yet performs it.** | **Element 4** |
| **The orchestrator has no prompt** | `charter-common.md` §6 gives the orchestrator operative duties — relay verbatim, never answer as the owner — and **no file in the set is addressed to it.** Found 2/3 at gate 7. The set's own threat model depends on it. | **Element 4 or 5** |

### Not owned yet — decide before assembly

- **`Severity` may not be an agent.** The spec marks `Divisible`, `Consensus`, `Union` and `Spawn_redteam`
  as *"cold agent"* and does **not** so mark `Severity`. Element 1 dispatches all three combiners from one
  file. ⚠ **Do not treat that asymmetry as owner intent — every function signature in the spec is
  agent-written** (verified against the owner's 59-line original, harness record 1044).
- **`"or get stuck"` is owner-written, appears three times, and is defined nowhere** — no detection
  criterion, no timeout, no recovery. The memo covers *crash*, which is a different failure: a crashed node
  is re-walked from the root; a stuck agent never returns and never crashes. **This is the most likely
  real-world hang.**
- **The divider's self-review loop is unbounded** — it loops until no `major|blocker` stands, with no cap,
  no `Ask_human` (it holds no `node_id`/`depth`), and no return field for a complaint. It sits **below**
  `Human_gate`, so the owner never sees it.
- **SEV4's iteration cap was dropped** in the severity port while SEV3 was imported from the same file.
  Owner record **1449 item 2** said to port the mechanism as guarded-change implements it.

### Rules and lessons that generalize — these are the cheap wins

1. **A HISTORICAL pin is sound; a LIVENESS pin is not.** A hash recording *what an agent was handed* can
   never be falsified. A hash asserting *the current state of a file a third party edits* goes stale on any
   edit, including edits to lines you make no claim about, and **fails uninformatively**. It cost this
   element three false alarms. **Pin third-party files by CLAIM + a re-derivable check**, with any hash
   demoted to "observed at «time»".
2. **Quote whole records, and say what you omitted.** Twice in this element a quote presented as a ruling
   was part of a longer message whose omitted portion mattered — once it would have changed a decision.
3. **Every dispatched agent must be able to do its job from its closed set alone.** A role file citing a
   source its reader cannot open turns provenance into a homework assignment; two of six roles were
   observed leaving their closed set. Element 1's answer: such citations are **provenance for an auditor,
   not an instruction**, and a genuinely missing source is a **config defect**, not a licence to fetch.
4. **The measurement-apparatus problem is real and this element hit it SIX times** — including twice in one
   day, and once *inside the fix for the previous instance*. See the owner's testing rule below.
5. **Owner's testing rule, record 2544 — this governs every later element.** *"if a component can be tested
   in isolation, it should be. If testing it requires more than three iterations of the test mechanism,
   reconsider if it should be tested in isolation or on a test run of the assembled thing."* Plus a **size**
   bound from the same record: a test mechanism must not be *"larger and more complex than Architect its
   self."* **Isolation is the DEFAULT, not the fallback.** Element 1's per-item application is
   `changes/charter-2026-07/9-test-venue.md` and is worth reading before building any test.
6. **When a script-based oracle fails twice for a structural reason, change the ORACLE, not the script.**
   Element 1 moved fork-fidelity and paraphrase-detection and semantic-inversion to **cold-reviewer**
   oracles after script attempts failed. It paid: a reviewer verified B01–B19 by hand, clean, in one pass,
   after two script generations could not.

## 1. The build plan — the owner's instruction, verbatim

> "start with each element individually (charter, spine, whatever), once the thing as pieces exists, run the
> whole thing" — transcript record **1274**

So: **one guarded-change run per element**, each with its own spec → criteria → plan → cold red-team → build
→ cold red-team → harness. Only once all the pieces exist does a whole-skill run happen. This is a
deliberate correction of attempt 1, which tried to author the entire skill in one run and drowned in its own
criteria set — the *measurement apparatus* became the thing that kept failing.

Elements, in dependency order: **charter** → **the 7-section spine** (`templates/seed/`) → **Layer-2 config
contract** → **router (`SKILL.md`)** → **methodology/reference doc** → then the whole-skill run.

## 1b. THE DONE CRITERIA — owner-set, record **1572** (2026-07-28)

> "The done criteria for Architect is that it can create a detailed plan to implement Data_Distiller. If it
> can do that, we call it created. If it runs on that and gets stuck, or produces garbage, then we fix the
> first link in the chain that broke and try again, repeat until nothing breaks and the results are good
> (they don't need to match what was used to make Data_Distiller, the goal is for equivalence or better,
> not sameness)."

**This is the acceptance test for the whole skill, and it replaces "prove each element behaviourally" as
the bar that decides whether Architect exists.** Read three consequences off it:

1. **The test is end-to-end and real**: run Architect on "plan the implementation of Data-Distiller" and
   judge the plan it produces. Data-Distiller already exists, so its actual plan is available as a
   reference — but the bar is **equivalence or better, explicitly not sameness**. A plan that reaches the
   same quality by a different route passes. Do not build a diff-against-the-original oracle; that would
   test sameness, which the owner ruled out.
2. **The repair rule is first-link-that-broke**, not full-restart and not fix-everything: run it, find the
   earliest point in the chain that failed, fix that, run again. Repeat until it completes and the output
   is good.
3. ⚠ **NOT A CONSEQUENCE — AN ORCHESTRATOR INFERENCE. UNRATIFIED. See §6b.** *"Per-element harnesses are
   therefore instruments, not gates; they do not have to be statistically powerful, and an element does not
   need its own behavioural proof to proceed."* **None of that is in record 1572** — the word test returns
   zero hits for `instrument`, `harness`, `gate`, `statistical` and `element`. It is the orchestrator's
   reading, it justified cutting every behavioural arm, and **the owner has been asked and has not ruled.**
   Do not cite record 1572 for it. It is retained here only because the cut was made on it. The failure
   that produced this ruling: the charter element burned **14** cold agents and two gate-4 bounces on
   behavioural arms whose own reviewers concluded had *"no path to done, only a path to a halt."*
   **When a per-element harness bounces twice, cut the harness — do not strengthen it.** See the standing
   TODO in `~/.claude/CLAUDE.md` ("the measurement-apparatus problem"), which this project is the third
   recorded instance of.

## 2. Process rules — non-negotiable, these were violated and it cost real work

- **The guarded-change loop runs in a SUBAGENT. The main session orchestrates only** — shepherds the
  cold-review gates, verifies output, commits. (Owner's standing global rule.)
- **Do not hand-author skill files in the main session.** The current `stages/charter.md` was written
  freehand inline and is therefore an **unvetted input**, not a product. That was a process violation.
- **Never claim a thing exists or behaves a certain way before it has been built and run.** Attempt 1's cap
  tripped on a criteria document written in the present tense about four scripts that did not exist.
  Build → run → paste the real output → *then* describe it, in the past tense.
- **Generate, don't type.** Hand-retyped site lists disagreed with the measurement file one directory away.
- **Any instrument that gates other instruments needs its own mutation test.** This project made that error
  three times; twice the "checker" was a printer that exited 0 on every input.
- **Wait for cold-reviewer records to exist on disk (path check) before returning.** Four runners returned
  with reviewers still in flight and their work was lost.
- **Never install an unfinished skill.** Attempt 1 was synced to `~/.claude/skills/architect/` after it
  passed conformance and left there after the dogfood found a blocker. It has been removed. Install only
  when attempt 2 is finished.
- **Stop-for-human is for the OWNER, not the orchestrator.** A delegated runner halts and relays verbatim;
  the orchestrator relays to the owner and never answers as him.

## 3. Where everything is

| What | Where |
|---|---|
| **The design spec** | `~/Documents/Architect.md` — pseudocode, single copy, deliberately not duplicated into the repo. **Owner-SEEDED, not owner-written throughout: measured 2026-07-28, only 41% of non-blank lines are verbatim owner text; the rest was written by the orchestrator under ratified rulings.** Do not equate "the spec says X" with "the owner said X" — see §6c. |
| The working tree | `Architect/` on branch `claude/recursing-visvesvaraya-b40a0c` |
| Attempt 1, archived whole | `Architect-Attempt-1/` — deleted only once attempt 2 works (owner's instruction) |
| Attempt 1's loop history | `~/architect-hardening-loop/LOOP-STATE.md` (rulings R1–R10, three failed hardening passes) |
| Attempt 1's dogfood findings | `~/architect-dogfood-2026-07-24/FINDINGS.md` |
| Draft PR | `https://github.com/ThinkerOfThoughts/claude-code-skills/pull/1` (body describes attempt 1; needs updating for attempt 2) |
| Nothing is installed | `~/.claude/skills/` holds only the three finished siblings |

Key commits: `3771038` attempt-1 build · `8efdca1` hardening paused · `8ca7197` archive + demolition ·
`0bd28ff` design spec complete · `45fc619` uninstall + de-duplicate spec · `a4138d2` charter rewrite ·
`67d8c3f` charter marked draft.

## 4. Current contents of `Architect/` — and what is vetted

**NOTHING in here has been through the loop. Treat all of it as input.**

| File | Status |
|---|---|
| `stages/` — **nine files, 891 lines** | The re-scoped element 1: `charter.md` (manifest, not dispatched) + the dispatched prompts. **The set grew 7 -> 9 on 2026-07-29**: the runner re-derived the decomposition and split the split-reviewer out (`redteam-plan.md` / `redteam-split.md`), because the old arrangement had one file *modifying* another's closed set — which the set's own composition rule says proves the rule was never common. Two independent reviewers pre-registered their own derivations and both confirmed the shipped structure. **BUILT, never passed a gate; gate 7 returned a BLOCKER 3/3 on 2026-07-29 and nothing was repaired in response.** The 237-line monolith it replaced is at `git show 711932f:Architect/stages/charter.md`. **No banner ≠ accepted.** |
| `changes/charter-2026-07/` | The element-1 run: **11** stage docs, **22** records incl. **14** verbatim reviewer records **A–N**, `RESUME.md`. `oracles/` holds **4 files** (both scripts executable; both run clean — 76/0 and 63/63). `fixtures/` IS empty: **no behavioural arm was ever run.** |
| `templates/seed/*.md` | Attempt-1 artifacts, carried over. The 7-section spine. Not yet revised for attempt 2. |
| `examples/authoring-a-skill/` | Attempt-1 artifact. Shape of a Layer-2 config. |
| `README.md` | Orientation for the rebuild. |
| `ATTEMPT-2-STATE.md` | This file. |

Deleted in the demolition: `SKILL.md`, `METHODOLOGY.md`, all eight `stages/stage-*.md`, `changes/`,
`guarded-change.architect.md` — all preserved in `Architect-Attempt-1/`.

## 5. The design — settled, do not re-litigate

The spec is `~/Documents/Architect.md`. A single recursive function `Node(task, plan, granularity, depth,
node_id)`. What the pseudocode alone does not make obvious:

- **`return plan` IS the join.** A parent waits on children and merges their returned values. There is no
  subtree-complete fact on disk. **This is the whole reason attempt 1 failed** — it implemented a recursive
  function as a filesystem protocol, and nearly every blocker was a bug in that protocol (a predicate whose
  operand had no producer, or a producer scheduled after its reader).
- **Slot inheritance** — a child runs inside its parent's queue slot, so siblings serialize and only leaf
  triples run concurrently. This deletes the entire shared-mutable-state class.
- **`Consensus` for plans, `Union` for issues.** Majority-vote is right for plans (one coherent plan out) and
  **wrong for findings** — the spec's own reason: "DISCARDS NOTHING… A finding one reviewer caught is
  signal" (`~/Documents/Architect.md` L24).
  > **CORRECTION 2026-07-28.** This bullet used to read "~85% of attempt 1's findings were caught by exactly
  > one reviewer." **That statistic has no source.** It appears in no file this project did not author about
  > itself — not in `~/architect-dogfood-2026-07-24/FINDINGS.md`, not in `~/architect-hardening-loop/`. The
  > orchestrator propagated it from a summary into this file, `README.md`, `guarded-change.architect.md` and
  > the charter draft, and then handed it to cold reviewers as measurement; the charter run's reviewer A
  > caught it. This is §8 failure mode 1 (self-certification) committed by the orchestrator. `FINDINGS.md`
  > records **per-finding convergence counts** ("3/3", "2 angles", "adversarial"), not a rate — derive from
  > those and show the derivation, or make the argument without a number.
- **Granularity floor**, threaded to three places: `Divisible` (tree depth), `Spawn_leaf` (step fineness),
  and — load-bearing — `Spawn_redteam` (what counts as "vague"). Without the third the red-team *manufactures*
  runaway subdivision: "you didn't say how to grip the handle" becomes an issue, the issue becomes the next
  task, forever. Owner's example: Manual Samuel.
- **Human gate**: `Human_gate` blocks the owner at every `depth <= gate_depth`, **default 2**, **before**
  children spawn. A bad cut corrupts everything beneath it, so approving after the fact is worthless.
- **Crash recovery = memoize, don't coordinate.** `Memo_read` before claiming a slot; two checkpoints per
  iteration (after `Consensus`, at the loop foot). On restart you re-walk **down** from the root: finished
  subtrees answer from disk, the walk falls through, you resume the node that died. A parent is never
  "recovered" — it is a stack frame re-created by replay, so live-agent state is never persisted.
- **One red-team pass** of 3 cold agents per iteration; the three-tier completeness definition lives **in the
  charter** as a distinct **lens** (not folded into a general mandate — that is how tier iii dies quietly):
  (i) universal spine, (ii) Layer-2 required sections, (iii) generative sweep for what neither list names.
- **Every finding carries a severity**, because `Severity()` filters on it. blocker|major become the next
  task; minor|nitpick are recorded, not looped on.
- **No backstop cap.** Owner ruled: trust the blocker|major filter; fix later if it proves an issue. A known
  accepted risk — attempt 1's cap tripped twice.

## 6. Owner rulings, with transcript loci (spot-checkable)

The **session transcript JSONL** is harness-authored and is the admissible source for owner words; an
agent-written file (including this one) is **not**. Loci are record indices in
`~/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`.

| # | Ruling | Locus |
|---|---|---|
| **Done criteria** | Architect is created when it can plan Data-Distiller; equivalence or better, **not sameness**; on failure fix the first broken link and re-run | **1572** |
| **Six lenses** | rejected "fold" as *"literally just the six lense option without the structure that makes it work"* — ratifies the six-lens **structure**. NOTE: "with earned-clean verdicts" was previously appended here and is **NOT in record 1829**; the earned-clean rules are the orchestrator's elaboration, not part of the ratified words. | **1829** |
| **`Ask_human`** | *"yes, add second function so agents can ask the human a question, filtered through you"* — now in the spec beside `Human_gate` | **1762** |
| Granularity | there must be a max-granularity option (Manual Samuel) | **1128** |
| Human gate | depth-scoped; "at least to the second level" as a safe default | **1148** |
| Crash recovery | agreed: memoize-and-replay | **1188** |
| Uninstall | an unfinished skill should not be installed; drop the duplicate spec copy | **1209** |
| No backstop | trust the blocker/major filter, fix later if it is an issue | **1258** |
| Build scope | element by element, then the whole thing | **1274** |
| Charter | must include the three-tier completeness definition | ~**1175** |

Attempt-1 rulings R1–R10 (records 694/699, 789, 805, 867, 925) are in
`~/architect-hardening-loop/LOOP-STATE.md`. **Most are now moot** — they governed a hardening loop on an
artifact that has since been demolished. The ones that still matter are carried into §5 above.
**Caveat on R4:** at record **784** the owner was offered four options and **selected none**, answering in
free text; and the orchestrator later **inflated** his "means nothing" into cap-bounce immunity, which he
never said. Do not inherit that inflation.

## 6b. ⚠ AN AUTHORITY THE ORCHESTRATOR INVENTED — UNRESOLVED as of 2026-07-28 20:00

§1b consequence 3 below states *"per-element harnesses are instruments, not gates"* and *"do not have to be
statistically powerful."* **That is NOT in record 1572.** Verified by direct word search of the record:
*instrument*, *harness*, *gate*, *statistical*, *element* — **zero hits.** The owner said the done criteria
is planning Data-Distiller and that on failure you fix the first broken link. The rest is the
**orchestrator's inference, propagated into four documents as owner authority**, and it is what justified
**cutting every behavioural arm** from the charter harness.

Caught by cold reviewer L in the element-1 re-scope run, confirmed by the runner, verified independently by
the orchestrator. Same failure class as the struck ~85% statistic, and precisely the **RAT2 unratified
inflation** rule this very element ships.

**Consequence: the harness cut is UNRATIFIED.** It may well be right — the owner's complaint about the
measurement-apparatus problem sits in the same message — but nobody has ruled on it. **Do not cite record
1572 for it.** Treat §1b consequence 3 as a proposal awaiting a ruling, and re-ask rather than defaulting.

## 6c. ⚠ THE DESIGN SPEC IS OWNER-SEEDED, NOT OWNER-WRITTEN — measured 2026-07-28

The corpus calls `~/Documents/Architect.md` "owner-authored" and hands it to cold reviewers as
**priority-1 authority outranking guarded-change's own stage files**. Measured against the harness record:

- The owner's original (harness record **1044**, an attachment record, not agent text): **59 lines**.
- On disk today: **119 lines**. **Only 37 of 90 non-blank lines (41%) are verbatim owner text.**
- Nine assistant mutations at records 1091, **1131**, 1151, 1157, 1159, 1161, 1168, **1190**, **1787** —
  1787's timestamp equals the file's mtime, so **the orchestrator is the last writer.**

The owner seeded the file and authorised additions (record **1085**), and every addition traces to a
ratified ruling — **so this is not fabrication.** But the majority of the file was written by the party
whose work the file is used to adjudicate, and the corpus does not say so anywhere.

**Two consequences that bit:**
1. **`stages/charter.md` cited spec L19 as the owner's authority for overruling `Guarded_change/stages/
   stage-3.md`** on what counts as a durable source. L19 is the `// PROVENANCE` comment — **orchestrator-
   written at record 1787, absent from the owner's original** (`grep -c admissible` on record 1044 → 0). No
   genuine owner turn anywhere contains the word "admissible." The narrowing was corrected on 2026-07-28 to
   rest on its substantive argument only; it is **not** an owner ruling and must not be cited as one.
2. **Spec L26** — *"three real rounds showed cold reviewers always find something"* — is an orchestrator
   insertion (record 1091) with no derivation. Struck 2026-07-28.

**The rule to carry:** *"the spec says X"* is not *"the owner said X."* For the owner's actual words the
harness-authored session transcript is the only admissible source.

## 6d. SPEC CHANGES 2026-07-29 — two owner rulings, and a stale-hash warning

**⚠ `~/Documents/Architect.md` is now 131 lines, sha256 `483ed8c4…261087`.** Every drift-detection table in
`changes/charter-2026-07/` still names the old `1d385954…cee826`, and every line citation into the spec
below the insertion point has shifted. **A mismatch there is expected, not corruption.** Re-derive before
treating any spec line-number citation as current.

**Ruling 1 — the node-path merge is `Union`, not `Consensus`.** Owner, on being shown that spec L97 merged
two children with a 2-of-3 majority vote: *"that should probably be Union rather than Consensus."* The two
children hold **different halves** (`division.first` / `division.second`), so a vote is a category error and
taken literally discards half the plan; the three-leaf path (three agents, same task) is the case a vote
fits. Applied. **Consequence not yet resolved:** `Union` is declared for *issues*; it now serves *plans* on
this path, so its declaration comment needs to cover both, or the two uses need separating.

**Ruling 2 — the design gains a decision log.** Owner: *"Why is there no decision log? There should
definitely be a decision log."* **Why there wasn't one:** the orchestrator ported guarded-change's rule
("contest a severity only via a logged entry") without checking that its destination existed in Architect.
The only disk state in the design was the per-node crash-recovery memo, which cannot serve — it is
single-writer and read only by that node's own restart. So that half of the severity mechanism was inert.
Now added as `Log_decision` / `Read_decisions`: **append-only, one per run, shared by every node** — the
opposite of `Memo_*`. **It is agent-writable, so it is NOT an admissible source for the owner's own words**;
the harness-authored transcript remains the only one. It is a durable record that a decision was taken, by
whom, on what grounds.

## 6e. PARKED 2026-07-29 evening — pass 4 came back BLOCKER and was NEVER ADJUDICATED

**Read this before touching element 1.** The three pass-4 reviewers all reported; **nobody has ruled on
what they found.** Their verdicts stand unexamined, so do not treat any of it as settled either way.

| Reviewer | Model | Verdict |
|---|---|---|
| U | opus | **blocker** |
| V | opus | **blocker** |
| W | sonnet | **major** |

Records are in `changes/charter-2026-07/records/reviewer-{U,V,W}-verbatim.md`.

**Why it stopped:** the runner died on **API 529 Overloaded four times** across ~45 minutes, including after
4- and 10-minute backoffs. The owner hit the same error in the main session, so this is Anthropic-side
capacity, **not a defect in the run**. Nothing was lost; everything is committed.

**Two blockers, both reported independently by U and V:**
1. **The non-termination class fix is still not closed.** The pass-3 repair was again written narrower than
   claimed. U traces a live route through `charter-common.md`'s floor-inoperability instruction, which tells
   a role to file a **blocker** — the exact mechanism §0 was rewritten to sever. V traces a second through
   `combiner.md`, where `Severity`'s "say so in your return value" puts a prompt-set report into `task`.
2. **"Report it out of band" has no destination for three of six roles.** Leaf, divider and `Consensus`
   have no output that is separable from their work product — their return values *are* the loop's state.
   This is O-MAJOR-5, which pass 3 left open, and repair #1 now depends on it.

**V additionally re-ranked two carried findings UP to blocker:** the divider's uncapped self-review loop
(no cap, no `Ask_human`, no report field, sits below `Human_gate`) which falsifies the set's own stated
invariant that the floor is the only thing preventing non-termination; and the **SEV4 iteration-cap drop**,
which departs from owner record **1449 item 2** (*"however it is implemented in guarded-change"*), is
declared nowhere, and is affirmatively described in the artifact as deliberate.

**U demonstrated an exploit rather than arguing one:** a one-line edit to `leaf.md`'s closed set, using a
span the duplication register amnesties globally (no `sites` key), **passes both oracles clean** — widening
an agent's input set, the precise failure the closed-set apparatus exists to prevent.

**W's finding worth carrying:** the N-03 retirement was performed on the success path only — its **failures
still gate the harness**, and `mutation-test.sh` ships zero N-03 mutants so it could not have caught that.
Also: **N-32 is gating, names its own verification command, and nothing runs it.**

**All three independently reproduced the harness numbers exactly** (122/0 + 21 smoke, 0 undeclared spans,
138/0 mutants) and all three judged the numbers honest but the coverage narrower than the surrounding prose
claims.

### ⚠ THE DECISION QUEUED FOR THE OWNER — do not let a fresh session resolve this in the loop

Whether **element 1 closes with ~10 known open defects so element 2 can start.** U and V both rule this is
the owner's, not the runner's: U because the runner's stated grounds are refuted by its own artifact (**nine
of ten open findings are element 1's own**, by the runner's own table), V because `charter-common.md`'s own
text reserves borderline and accepted-risk calls to a person. The runner was instructed to halt with this
question rather than decide it, and died before answering.

### Practical note for whoever resumes

The runner's context had grown very large, which makes each of its turns an expensive request and the most
likely thing shed under capacity pressure. **Consider a fresh runner that reads state from disk** rather
than reviving that one — and note that adjudicating those three reports in a *fresh* agent is arguably
better on the merits anyway, since two of the reviewers found the previous runner resolving its own case in
its own favour.

## 7. OPEN

- **Three questions put to the owner at 19:40, UNANSWERED at park:**
  1. **Does the harness cut stand?** See §6b — its stated authority was fabricated.
  2. **`Consensus` arity and semantics.** Spec L22 defines it 2-of-3 with the odd plan discarded; L79 calls
     it on **three leaves at the same task** (a vote fits) and L97 on **two children holding *different*
     tasks** (`division.first()`, `division.second()`). On the node path a majority vote is a **category
     error, not merely undefined for n=2** — taken literally it discards half the plan. Options floated,
     none chosen: spawn three children; give the node path a distinct integrate-the-halves function; make
     `Consensus` arity-aware. **Owner's design, owner's call.**
  3. **The demotion port is half-landable.** Owner record 1449 said the mechanism *"gets implemented
     however it is implemented in guarded-change"* (the word "verbatim" is the orchestrator's, not the owner's). The human-tie-break half now works via `Ask_human`. The *contest-via-a-logged-entry*
     half has no destination: `grep -ic 'decision log'` on the spec returns **0**, and the memo cannot serve
     (single-writer, per-node, read only by that node's own restart). The rule is inert as written.

- **ELEMENT 1 RE-SCOPED 2026-07-28 evening, owner ruling.** From "the red-team charter" to **"the agent
  prompt set."** His instruction: *"see if the charter can be sub-divided into different files for different
  types of agent, i.e. one for the red-team, one for the leaf agents, one for the combiner (or whatever its
  called now), one for the node agents, one for the divider, along with one main one that has the information
  needed by all of them"* — then **"Go for it."**
  **What the analysis found:** the 237-line charter is ~90% red-team material with other roles' instructions
  buried in it as asides (the spot-verify rule instructs `Union` but lives where only reviewers read it; the
  demotion rule tells the node when to call `Ask_human`). And **three of six roles — leaf, node, combiner —
  had no instructions anywhere at all**, existing only as pseudocode signatures. So this is not a refactor;
  it is writing the missing half of the skill. The monolith *looked* complete, which is why nobody noticed.
  **Target:** `charter-common.md` + `redteam.md` + `divider.md` + `combiner.md` + `leaf.md` + `node.md`.
  **Governing rule, not negotiable:** common is included **verbatim**; role files are **additions only and
  never restate a common rule** — if a role file must *modify* a common rule, the rule was never common.
  This is the charter's own composition rule (B19) applied to the file set, and it is what stops six files
  drifting. Generalised to all multi-agent skills in `~/.claude/CLAUDE.md`.
  **The two open blockers are absorbed, not excused:** the self-contradicting durable-source clause is fixed
  in `charter-common.md` against the spec (which outranks `stage-3.md`); and the frozen-criterion conflict is
  resolved by the freeze being **legitimately re-taken** under a re-scope — recorded as such, not quietly
  edited.

- **The config's `redteam_context` is missing load-bearing paths — ORCHESTRATOR-OWNED, fix in element 3.**
  `guarded-change.architect.md` lists 8 paths. `Guarded_change/stages/{stage-1.5,stage-3,stage-4,stage-8}.md`
  are **not** among them, yet Architect's charter cites them as the authority for RAT1/RAT2, the severity
  model and the earned-clean rules. The charter run hit this twice: both times the runner had to read
  out-of-set to check its own citations, and the second time it correctly quoted them as B15 supplementary
  context instead. **Do not amend the config mid-run** — changing `redteam_context` under a frozen criteria
  set is moving the goalposts. Fix it when element 3 (the Layer-2 config contract) is built, which is the
  element that owns this question anyway.

- **Draft PR body** still describes attempt 1 end-to-end. Needs rewriting for attempt 2.
- **`templates/seed/*` and `examples/` are attempt-1 artifacts** carried over unexamined. They are build
  elements in their own right, not settled inputs.
- **A dormant background task** (`task_c8abf7df`) was spawned for a stale Dragonfly README claim
  ("four-lens / reused not forked" vs the forked five-lens reality). Never confirmed done; the stale phrasing
  was still present at last check. Unrelated to Architect.

## 8. Failure modes this project actually produced — the red-team should hunt these

1. **Self-certification** — a document asserting, in the present tense, the behaviour of scripts that did not
   exist. Caught only by a reviewer who *ran* them instead of reading the claims.
2. **Unearned clean verdicts** — a "checker" that exited 0 on every input, twice; and an orchestrator
   spot-check that ran a tool with no arguments and read the resulting usage-error as a pass.
3. **Scope drift** — "narrow and mechanical: four scripts, two deletions" became a 13-item list and ~12 new
   criteria, and three of nine blockers lived in rows the expansion created.
4. **Fork without join** — four separate runners returned while their subagents were still in flight.
5. **Under-generalized fixes** — a defect class fixed only where reviewers happened to look, then re-found
   elsewhere and mistaken for a fresh finding.
6. **A gate satisfiable by the party it constrains** — an approval file the runner could write itself, and a
   directory-existence check pre-satisfied by run setup.
