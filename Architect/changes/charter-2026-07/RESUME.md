# RESUME — element 1: THE AGENT PROMPT SET · updated 2026-07-30

## ⚠ 0z. READ THIS FIRST — EVERYTHING BELOW §0z PREDATES THE PASS-4 ADJUDICATION

**On 2026-07-30 a fresh cold runner adjudicated pass 4 and made 18 repairs. Its full record is
`decisions.md`, sections ADJ-0 through ADJ-5** — read those before anything else in this file. Where this
file and ADJ-0..5 disagree, **ADJ-0..5 is current.** Specifically, these statements below are now stale:

- Every **hash** in §6 is superseded. Post-repair hashes are in ADJ-4. Nine files, **1,310 lines**.
- **The harness numbers in §4 are superseded**: now **133/0 (+21 SMOKE)**, **0 undeclared**, **144/0
  mutants**. Verbatim capture: `records/harness-run-2026-07-30.txt`.
- §5's owner queue is superseded by **ADJ-5**, which is a different and shorter list.
- The accept bar was **amended again, under FRZ-3**, because two gating criteria (N-14, N-24) were found
  **factually false against the artifact they gate.**

**Four things a fresh reader must not misread:**

1. **The pass-4 reviewer records did not exist on disk until 2026-07-30.** `ATTEMPT-2-STATE.md` §6e said
   they were in `records/`; they were not. They were recovered from the harness transcripts (ADJ-0).
2. **The owner's original spec is at harness record 1044** — an `attachment` record, 2,278 chars, and the
   admissible source for what the owner actually designed. **His `Divisible` has no red-team loop and his
   `Spawn_leaf` takes no `granularity`.** ⚠ **Record numbers in this project are 1-BASED (record N = line N
   of the session JSONL).** The 2026-07-30 runner briefly reported an off-by-one *in the corpus*; the
   off-by-one was its own, from reading the JSONL into a 0-indexed list. Retracted in `decisions.md` ADJ-2.
   **Read loci with `sed -n 'Np'`, not with a list index.**
3. **There IS an owner ruling that the node loop has no iteration cap** — record **1258**, answering the
   question put at record **1254**. Pass-4 reviewer V ruled the missing cap a blocker without checking it.
   The substance is settled; only the declaration was missing, and that is now closed.
4. ⚠ **PASS 5 RAN AND RETURNED `blocker` (reviewer X, opus).** It demonstrated **two new working
   exploits** against the closed-set apparatus, found a **fourth non-termination route**, and **refuted two
   of the three items the runner had escalated to the owner as design-level** — both were the runner's own
   to fix. All adjudicated and repaired: `decisions.md` **ADJ-8 … ADJ-12**. A new oracle, `sigmatch.py`,
   closes the hole both U and X walked through. **Y and Z were never dispatched.**
5. **The owner answered the halt (record 3119) rather than accepting the risk**, so **element 1 is NOT
   closed** and the closure question is moot. Three rulings implemented: `task` carries source material;
   `Severity` logs filtered minors; "stuck" is defined. See **ADJ-13**.
6. **Pass 6 has not been convened.** Everything in ADJ-8…ADJ-13 is **unreviewed**.

**The original pass-5 framing:** Its prompt is
   `records/stage6g-prompt.md`. **FRZ-3's rows require it** — the run's own protocol says an author who
   amends the bar mid-run and then measures themselves against it must be cold-reviewed.

---

# (historical, written 2026-07-29 — superseded where §0z says so)

**Read this first. It assumes you know nothing.** Project-level entry point is `../../ATTEMPT-2-STATE.md`;
this is the element-level one. The gate log is `decisions.md` — read its last FOUR entries after this file.

---

## 0a. ⚠ THREE OWNER RULINGS LANDED 2026-07-29, AFTER GATE 7. READ THESE FIRST.

**Two of them changed the design spec under this element; one changed how it must be tested.** Everything
below §0a was written before them unless it says otherwise.

### R1 — the testing rule. It supersedes BOTH prior positions on the harness.

> *"if a component can be tested in isolation, it should be. If testing it requires more than three
> iterations of the test mechanism, reconsider if it should be tested in isolation or on a test run of the
> assembled thing."*

**Isolation testing is the DEFAULT, not the fallback.** The count is of **rebuilds of the test mechanism**,
not runs of the test. Past three the rule says **reconsider the venue** — not "stop", and not "repair
again". **The full per-item application is `9-test-venue.md`; read it, it is the answer to Q4.** Both
earlier positions are dead: the orchestrator's *"per-element harnesses are instruments, cut the arms"*
(wrong — isolation is the default) **and this runner's** *"a broken test gets repaired, not deleted"*
(wrong as a general rule — **do not cite record 1449 item 1 for it any more**).

### R2 — the node-path merge is `Union`, not `Consensus`

Owner: *"that should probably be Union rather than Consensus."* Spec **L109**. The two children hold
`division.first()` / `division.second()`, so a 2-of-3 vote would discard half the plan. **`Consensus` now
has exactly one call site** (three leaves, one task, L91). Applied to `node.md`'s loop and rewritten
through `combiner.md`. **Open and unresolved: `Union`'s own declaration at L24 is written for issues only
and now serves plans too.** `combiner.md` states the dual use because the declaration does not — that
mismatch is the owner's to close.

### R3 — a decision log now exists

Owner: *"Why is there no decision log? There should definitely be a decision log."* `Log_decision` /
`Read_decisions` at spec **L36–46** — **append-only, one per run, shared by every node**, the opposite of
`Memo_*`. **This closes the half of the ported severity mechanism that had no destination** (open item 3
below is therefore CLOSED). `node.md` now logs a contested severity **and then** asks the owner.
⚠ **It is agent-writable, so it is still NOT admissible for the owner's words** — `charter-common.md` §6
says so explicitly, because a durable timestamped forgery is more persuasive, not more true.

### R4 — `Union` is GENERALIZED, input-agnostic (same day, after R2)

Owner: *"Union should be generalized to stick the provided inputs together, the only reason its issue
specific is because you wrote the comment for it as such."* **Verified: `Union` is not in the owner's
original spec at all** (record 1044) — it came from the `Combine` split, and *"merges issues"* was an
orchestrator comment. **So the issue-specificity was invented, and the "open item" R2 left is CLOSED.**
`combiner.md` is rewritten so **one rule leads and does not vary with the input**; it warns against
reasoning *"these are issues, so…"*. One specialization is kept — ordering a plan merge along the seam —
**declared as an author decision** and put to the reviewers as a possible RAT2 inflation.

### R5 — a runner decision, not an owner ruling: §5's record rule

**Element (i) changed from "the verbatim prompt you were given" to path + sha256**, verbatim text required
only for prompt parts with no durable file. Made on measured behaviour: **two of three cold agents in the
F1/F2 run refused to paste the prompt back and substituted the hash**, which under §5's own *"missing any
⇒ un-run"* clause invalidated two otherwise-good records. A retyped copy can drift; a hash cannot.
**Declared as a CHANGE in `charter.md`'s provenance, and put to the reviewers as Q-A** — it is the shape of
a goalpost move even if it is not one.

### Consequences for the gate-7 findings

Two blockers were **overtaken by these rulings rather than repaired on their own terms**:
- **O-MAJOR-7** (the `Consensus` repair broke on the stuck-leaf path) is **dissolved by R2**: with `Union`
  on the node path, `Consensus` only ever sees leaves at one task, so a short vector *is* competing
  accounts and 2-of-2 is well defined. The "complementary halves" text that O showed was false is gone.
- **O-BLOCKER-1** (non-termination via the §0 contradiction) is **repaired at the source**: §0 now says
  deciding whether a conditional section applies is the holder's job, **and that a role file doing so is
  not a defect**. `redteam.md` no longer modifies §0. **OOS-14 is withdrawn.**

**The spec is now 131 lines, sha256 `8ad9d620…d107a474`. Lines 1–35 are unchanged; everything from old-L36
down shifted +12.** Only `combiner.md` carried shifted citations and it was rewritten anyway.


## 0. What this element IS

Element 1 of 6. It **used to be** "the red-team charter" — one 237-line file. **The owner re-scoped it** on
2026-07-28 to **"the agent prompt set"**:

> "see if the charter can be sub-divided into different files for different types of agent, i.e. one for
> the red-team, one for the leaf agents, one for the combiner (or whatever its called now), one for the
> node agents, one for the divider, along with one main one that has the information needed by all of them"

and, on being shown the analysis: **"Go for it."**

**This was not a refactor.** Three of the roles — leaf, node, combiner — had **no instructions in any file
in the project**. The re-scope wrote **the half of the skill that did not exist**. The monolith is at
`git show 711932f:Architect/stages/charter.md`.

### The set as it stands: NINE files under `Architect/stages/`, 891 lines

| File | Dispatched? | What it is |
|---|---|---|
| `charter.md` | **NO** | Manifest: fork provenance (CARRIED / CHANGED / **ADDED** / NOT CARRIED / declared gap), the composition rule with its **two clauses** and the **declared-duplication register**, and the B01–B19 allocation table. Never given to an agent. |
| `charter-common.md` | **YES — verbatim, to every role** | The common core, §0–§6. |
| `redteam.md` | YES (**both** reviewer kinds) | Reviewer core: six lenses, earned-clean rules, conditional lenses, RAT1, RAT2. **Names no artifact and states no per-kind input list.** |
| `redteam-plan.md` | YES | Aiming for `Spawn_redteam`: the artifact is the **plan**; floor = what counts as vague; B18 last. |
| `redteam-split.md` | YES | Aiming for the split review inside `Divisible`: the artifact is the **division + seam**, **no plan**; floor = would either half fall below; the four questions; B18 last. |
| `divider.md` | YES | `Divisible`: deriving a split. |
| `combiner.md` | YES | `Consensus`, `Union` (incl. spot-verify), `Severity`. |
| `leaf.md` | YES | Write the plan at the floor. |
| `node.md` | YES | The loop, memo, slot inheritance, human gate, the demotion **permission**. |

**Composition:** an agent's prompt = `charter-common.md` **verbatim** + its role file(s), appended.
Reviewers get **three** files: common + `redteam.md` + an aiming file.

### THE GOVERNING RULE — now two clauses, and mechanically enforced

1. **common → role.** A role file never restates or modifies a rule stated in `charter-common.md`.
2. **role → role.** Role files may share **scaffolding** (composition banner, closed-set section stem,
   section headings) but never a **rule**. A rule in two role files either belongs in the common core (all
   roles can act) or in exactly one of them — unless it is in the **register**.

**Diagnostic for what belongs in common: which roles can *act* on this rule?**

**The register is `oracles/declared-duplications.jsonl`, and it is BOTH the human-readable declaration in
`charter.md` AND the harness's exemption file.** So an undeclared duplication fails the build. Exemptions
are scoped to the **file pair** they were declared for, not granted globally.

---

## 0c. WHAT COMES AFTER THIS ELEMENT — and it is NOT the Data-Distiller run

**Correction, 2026-07-29.** An earlier version of this runner's reasoning proposed stopping element-1
review and *"going to the assembled run"*. **That destination was wrong and is not available.** The
assembled run needs the whole skill; **element 1 is the only one built.** What follows is **element 2**,
the 7-section plan spine (`templates/seed/`), then the Layer-2 config contract, the router `SKILL.md`, the
methodology doc, and only then assembly. The owner's done criteria (record **1572**) is the acceptance test
for the **finished skill**, not the next step after this element.

**This changes what "leave it unrepaired" costs.** Anything not fixed here is inherited by **five more
elements and by the assembled run**, so it must be recorded where the next runner will actually look.
**It is: `../../ATTEMPT-2-STATE.md` §0b**, which lists every finding that leaves this folder, who owns it,
and the six lessons that generalize. **A later runner reads that file, not this one.**

## 1. EXACT LOOP POSITION

| | |
|---|---|
| **Accept bar** | `1.5-criteria-v2.md`, **as amended under FRZ-2** (2026-07-29). |
| **Stage 1 (spec)** | Re-scoped by the owner. |
| **Stage 1.5 (criteria)** | v2, amended under FRZ-2. **The amendment was put to the cold reviewers as Q2** — the FRZ path requires a targeted re-review, not just a log entry. |
| **Stage 2 / gate 4** | ⚠ **SKIPPED, NEVER RUN, AND DELIBERATELY NOT RE-RUN.** See §2. |
| **Stage 5 (build)** | Done, then **repaired** 2026-07-29. Nine files. |
| **Stage 8 (harness)** | **BUILT, EXTENDED, RUN — AND BROKEN BY THE REVIEWERS.** 92/0 · 0 undeclared spans · 87/0 mutants, all reproduced independently by all three — **and all worth much less than they look.** See §4. |
| **Stage 6 → gate 7** | **RE-RUN 2026-07-29** with three cold reviewers **O, P, Q**. |
| **VERDICT** | 🔴 **Pass 3: BLOCKER, 3/3** (R, S, T). **ALL FOUR BLOCKERS SINCE REPAIRED — and the repairs are UNREVIEWED.** Three of the four are verified **behaviourally** (F5/F6), not just textually. **Read `decisions.md`'s last four entries first.** |

> ### THE FOUR PASS-3 BLOCKERS — ALL REPAIRED 2026-07-29. **ALL UNREVIEWED.**
>
> 1. ✅ **The node/floor contradiction — REPAIRED AND BEHAVIOURALLY VERIFIED.** §2 now decides
>    floor-holding **by signature alone**, in three cases: bound / **carrier** (the node) / given none.
>    `node.md` gains a real floor section stating the carrier duty and requiring any branch override to be
>    logged. **F5 dispatched a node against the composed prompt: it identified itself as "the carrier case
>    of §2" by name and reported no defect.** R and S were right about the text they reviewed; T's
>    verified-fixed verdict rested on a distinction that text did not make. **Both are resolved.**
> 2. ✅ **The non-termination path — REPAIRED AT THE CLASS.** The previous fix enumerated one *shape*;
>    R showed the mechanism firing from another. §0 now **severs the path** instead of listing entrances:
>    a prompt-set defect is reported **out of band, never carries a severity, and never counts as
>    `blocker|major` against the work** — so it cannot enter the findings stream that becomes the next
>    task. Stated as a class, *"because a rule written to the cases already seen is a rule that will be
>    defeated by the next one."* **F5 and F6 both reported no spurious defect.**
> 3. ✅ **The seam-ordering specialization — REPAIRED AND VERIFIED.** `combiner.md`'s ordering rule now
>    keys on **what the caller supplied** (a seam is handed to you; it is not a property of the input), so
>    the input-type branch T found is gone — probe `N-37d` asserts its absence. `node.md` no longer
>    attaches *"Owner ruling"* to the runner's own author decision. **F6 dispatched a combiner: it ordered
>    by the caller-stated seam without reasoning about input type.**
> 4. ⚠ **The harness — ANSWERED BY CHANGING VENUE, NOT BY BUILDING AGAIN.** S's append attack is real and
>    reproduced; **no substring probe can catch it**, so more probes of the same kind cannot help. The
>    class is relabelled **IN-PLACE NEGATION** with its limits stated in-file, and **semantic inversion is
>    now a cold-reviewer oracle** — the third time that venue answer has been taken, and it has paid twice
>    (S found the append attack by reading; T verified B01–B19 by hand). **The four gating criteria that
>    had NO probe now have nine**, verified by reproducing T's exact injection: previously 0 probes fired,
>    now 5 do.

### Two findings against the RUNNER'S APPARATUS, not the artifact — both confirmed first-hand

- **The verbatim-record pipeline wrote mid-task fragments under a "VERBATIM final message" header
  (Q-B-2).** `extract_records.py` takes the last assistant message; the runner pointed it at `records/`
  **while all three reviewers were still in flight**. **Q proved it about its own record** — it recognised
  a line it had written several tool-calls in, before reading most of the set. **This is the same class as
  the defect the claim-audit found in `reviewer-F-verbatim.md`, committed again in the tool built to
  prevent it.** *Corrected*: all three records re-extracted after all three agents terminated (O 35,685 /
  P 26,720 / Q 25,138 chars, each ending in its real verdict). **Fix still owed: the tool must refuse to
  write until its subject has terminated.**
- **N-03 has near-zero discriminative power (Q-B-3), and `mutation-test.sh` contains zero N-03 mutants.**
  Reproduced by the runner: **9 of 19 rules also pass against a file they were never claimed to be in;
  B09 passes all eight.** The "strengthening" this run made to that probe **overstates itself in a comment
  the runner wrote into `ruleplace.sh`.**

### Also found, not yet fixed

**Unbounded second non-termination path** — the divider loops until no major|blocker remains, with no cap,
no `Ask_human` (it holds no `node_id`/`depth`), and no return field for a complaint; it sits **below**
`Human_gate`, so the owner never sees it (O-MAJOR-10). **`"or get stuck"` is owner-written, appears three
times, and is defined nowhere** — and the memo covers *crash*, a different failure (O-MAJOR-8). **The
orchestrator has operative duties in every dispatched prompt and no file of its own** (O-MAJOR-9).
**SEV4's iteration cap was dropped silently** while SEV3 was imported from the same file (O-MAJOR-11).
**N-15a, N-20, N-25 are gating with no probe** (O-MAJOR-4 / P-7). **N-10's *"in no other file"* now
collides with N-11 and N-12, and the artifact violates it at three sites** (P-4). **8 of 12 register
entries are unscoped global amnesties — P injected a false closed-set element into two role files and the
oracle reported clean** (P-2). **The register exists in two copies that disagree** (P-3). **Probe IDs
`N-05e`–`N-05h` are each used twice** (O-MINOR-3, confirmed).

### On Q1 and Q2 — the two questions this gate existed to answer

- **Q1 — the decomposition is CORRECT, and O is the only reviewer whose answer is uncontaminated** (it
  pre-registered its derivation to disk before opening `charter.md`; **P read `charter.md` early and
  disqualified its own Q1, which is the honest thing to do**). O independently re-derived the same
  three-reviewer-file structure from the spec. **One omission: the orchestrator has no prompt.**
  ⚠ **O dissolved one of the runner's own test questions**: the *"`Severity` is not marked 'cold agent'"*
  point is worthless, because **every function signature in the spec is agent-written** (record 1044). It
  must stop being offered as evidence.
- **Q2 — FRZ-2's N-10/N-11 amendment is INDEPENDENTLY RIGHT.** Both reviewers concur: the incoherence was
  real, the actability split is principled, the audit trail (v1 byte-identical, original N-11 preserved
  with a superseded marker) is correct. **But the *additions* did not hold the same discipline** — O rules
  **N-21 a transcription of the repair** (written from the shipped text, so it cannot fail against it),
  **N-23(b) licenses the defect** (satisfied by *declaring* a contradiction that is still live), and
  **N-24 asserts a false proposition**. O's summary: *"the amendment discipline held; the addition
  discipline did not."*

**Reviewer identity, read FIRST-HAND from the harness sidecars, not reviewer-reported:**

| Tag | agentId | model | parent | depth | Verdict |
|---|---|---|---|---|---|
| **O** | `a0d1f92f5062b62aa` | `opus` | `a9b39b3c731d2c23a` | 2 | **BLOCKER** |
| **P** | `abe8912b733efac94` | `opus` | `a9b39b3c731d2c23a` | 2 | **BLOCKER** |
| **Q** | `ae53a70b86e824e87` | `sonnet` | `a9b39b3c731d2c23a` | 2 | **BLOCKER** |

**"3 independent cold agents" is therefore a verified fact for this gate**: three distinct ids, one common
parent, `spawnDepth: 2`, **two distinct models**. Prompt: `records/stage6d-prompt.md`.

**Reviewer identity, read FIRST-HAND from the harness sidecars, not reviewer-reported:**

| Tag | agentId | model | parent | depth |
|---|---|---|---|---|
| **O** | `a0d1f92f5062b62aa` | `opus` | `a9b39b3c731d2c23a` | 2 |
| **P** | `abe8912b733efac94` | `opus` | `a9b39b3c731d2c23a` | 2 |
| **Q** | `ae53a70b86e824e87` | `sonnet` | `a9b39b3c731d2c23a` | 2 |

**"3 independent cold agents" is therefore a verified fact for this gate**: three distinct ids, one common
parent, `spawnDepth: 2`, **two distinct models**. Prompt: `records/stage6d-prompt.md`.

---

## 4. THE HARNESS — BUILT, EXTENDED, RUN. **DO NOT REBUILD IT.**

```
$ cd Architect/changes/charter-2026-07
$ ./oracles/ruleplace.sh    ../../stages                                    # 92 passed, 0 failed  ; exit 0
$ ./oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl
                                                                            # 0 undeclared spans  ; exit 0
$ ./oracles/mutation-test.sh ../../stages                                   # 87 as expected, 0   ; exit 0
$ <each with no argument>                                                   # usage              ; exit 2
```

Verbatim output: **`records/harness-run-2026-07-29.txt`**. Exit codes there are captured from each script
**directly, never through a pipe** — the first attempt piped through `head` and recorded a script exiting 2
as `exit=0`, which is this project's own "usage error read as a pass" failure committed while writing the
file that documents it.

| File | What it is |
|---|---|
| `oracles/ruleplace.sh` | Per-**FILE** positive assertions — placement is the only thing this element changed. |
| `oracles/rules.tsv` | The probe table. **AUTHOR-WRITTEN.** Proves the rules it names sit in the files it names; **NOT** evidence the criteria are covered. |
| `oracles/shared_spans.py` | **The NEGATIVE assertion.** Positive per-site probes structurally cannot see a duplication; this is why 76/0 was once returned on a set carrying eight. |
| `oracles/declared-duplications.jsonl` | The register — the same file the manifest publishes and the harness enforces. |
| `oracles/mutation-test.sh` | Deletion / relocation / insertion / control **/ duplication** mutants. |
| `oracles/delete_span.py` | Deletes the minimal line span whose *normalized* join contains an anchor. |
| `oracles/extract_records.py` | Recovers a reviewer's verbatim final message from the harness JSONL, with first-hand identity from the `.meta.json` sidecar. |

### Four defects the extension caught — each had already shipped

1. **`shared_spans.py` did not know about `redteam-plan.md` / `redteam-split.md`**, so duplications in the
   two newest files were invisible. Caught by the per-role kill mutants, **not by reading the script.**
2. **The register was a global amnesty.** Caught by a mutant written to abuse the exemption list.
   Exemptions are now scoped to a `sites` pair.
3. **The N-03 fork-fidelity probe was near-vacuous** — it asserted only *"destination exists and is
   non-empty"*, i.e. **19 probes that pass for any nine non-empty files.** Same class as the two bare
   `exit 0` checkers this project already shipped, and it had been reported as fidelity "verified
   rule-by-rule". **The rule-by-rule verification was done by humans; the oracle was not doing it.**
4. **The exit-code capture bug above.**

### ⚠ WHAT THE HARNESS STILL DOES NOT VERIFY — do not let a restart assume otherwise

- **`rules.tsv` is author-written.** Not evidence of criteria coverage. Only N-03's probe set is generated.
- **The 60% threshold in N-03 is a judgement, not a derivation.** `B15` passes at **2 of 3**.
- ⚠ **EVERY "0 undeclared spans" RESULT BEFORE 2026-07-30 IS NOT COMPARABLE TO ONE AFTER.** Eight of the
  register's twelve entries were **global amnesties** (no `sites` key). Reviewer U rode one to widen
  `leaf.md`'s closed set in a single line, clean through both oracles. Scoping them broke that exploit and
  **exposed nineteen further undeclared spans the amnesties had been hiding.** See `1.5-criteria-v2.md`'s
  closing section and `decisions.md` ADJ-4 #6. **The exemption file is part of the instrument.**
- **`shared_spans.py` cannot see a PARAPHRASE.** Two duplications repaired this run — the floor-is-wrong
  clause in `divider.md` and `leaf.md` — were found by **reading**. **A clean run means no *verbatim*
  restatement survives, not that the composition rule holds.**
- **No behavioural evidence exists for any file.** `fixtures/` is empty.
- **N-14 placement (floor before lenses, B18 last): effect still UNVERIFIED.** Relocation confound; no
  further attempt.
- **N-16 length came out AGAINST the artifact's own justification** and is reported anyway: the composed
  reviewer prompt is **326–344 lines vs the monolith's 237**. `charter.md`'s *"every line a role does not
  need crowds out one it does"* predicts shorter prompts; four of six are not shorter. **The length half of
  the argument is unproven.** The applicability half is unaffected. Full table in `8-harness.md`.

---

## 5. THE OWNER'S QUEUE — all three items ANSWERED 2026-07-29; one new one opened

1. ~~**Does the harness cut stand?**~~ **ANSWERED 2026-07-29 by owner ruling R1** (§0a) — and the answer
   was neither party's. **Isolation testing is the default**, with a three-rebuild threshold on the *test
   mechanism* after which you reconsider the **venue**. Per-item application: **`9-test-venue.md`**.
2. ~~**`Consensus` arity and semantics.**~~ **CLOSED 2026-07-29 by owner ruling R2** (§0a): the node path
   calls **`Union`**, so the category error is gone and `Consensus` has one call site.
3. ~~**The demotion port is half-landable.**~~ **CLOSED 2026-07-29 by owner ruling R3** (§0a). The
   decision log exists (`Log_decision` / `Read_decisions`, spec **L36–46**), so the
   contest-via-a-logged-entry half now has a destination and `node.md` uses it. **The runner deliberately
   did not invent one while it was missing** — that would have been the RAT2 inflation the set itself
   forbids — and the wait was the right call.

**NEW, and it replaces item 2:** **`Union` is declared for issues (spec L24) and now serves plans (L109).**
R2 resolved the *category error* but not the *declaration*. Either L24 must cover both vectors or the two
uses need separating. `combiner.md` states the dual use because the declaration does not. **Owner's design,
owner's call.**

---

## 6. Drift detection — hashes as of 2026-07-29

**Artifact — REPAIRED after gate 7 under the owner rulings of 2026-07-29. These are the POST-repair
hashes; the gate-7 reviewers held the PRE-repair set (`stage6d-prompt.md` §2 lists those).** 982 lines.

| Artifact | sha256 |
|---|---|
| `stages/charter.md` | `223edfd732e47c3406a8031dace6e3b4c358fe298cf1231f413837fe10532020` |
| `stages/charter-common.md` | `34e50db3b0eddac4d1e44e69d75520a40f5d7fc9cf6ee80a9e67dc6977d55eff` |
| `stages/redteam.md` | `c28fcbcf634ee5b781872a6da8776ccddb162ff1c1346750fbc303d02102b838` |
| `stages/redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` |
| `stages/redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` |
| `stages/divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` |
| `stages/combiner.md` | `105ae484f918231c27ca7ab82e305b7f4d631b7593a9d6f7093c3cd166356828` |
| `stages/leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` |
| `stages/node.md` | `8aedc57525efb8d539bf4d347a6859805fae675cd61eefd67837bb84ef1d33d6` |

**Inputs — CHANGED since the previous RESUME, all traced to commit `aa41f64` (the cold claim-audit):**

| Artifact | sha256 | Note |
|---|---|---|
| `~/Documents/Architect.md` (**the spec**, **131 lines**) | `8ad9d620be794047b3606e948e20d3cd70b5413c36b9dd19f0dc97d8d107a474` | **CHANGED AGAIN 2026-07-29 by owner rulings R2 and R3.** L1–35 unchanged; **everything from old-L36 down shifted +12.** Decision log inserted at L36–46; `Memo_*` now L48–49; `Node` L51; leaf merge L91; children L104–105; **node merge L109 is now `Union`**; red-team merge L122. |
| `Guarded_change/stages/charter.md` (fork source, 103 lines, `8d73e5d`) | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` | **UNCHANGED.** |
| `Architect/guarded-change.architect.md` (config) | `3f69afeadda62589d8ff14dcbaf8c3a7da6436732a53d123b506cabe02265efb` | Audit-corrected. Still not amended mid-run. |
| `1.5-criteria.md` (**v1, superseded, was frozen**) | `bb33394b0c5dc74e205c86bedc54cb5a108be3588617e423fef3090dfd362781` | ⚠ **No longer its gate-4 freeze value `1df324c0…`.** The audit **edited a frozen document in place.** Substantively correct, recorded in `aa41f64`, but it is the mechanism the old RESUME told you to treat as a red flag — **so do not re-derive that alarm; it is explained here.** Nothing in this run depends on v1. |

---

## 7. Things known only to this session — written down now or lost

- **The oracle output is only as good as its exit-code capture.** `$?` after a pipe is the *last* command's
  status. The first version of `records/harness-run-2026-07-29.txt` recorded `exit=0` for scripts that
  exited 2, in the file whose whole purpose is proving they exit 2.
- **A mutation test on a NEGATIVE assertion needs a positive control.** Without *"the unmutated set comes
  back clean"*, every kill it reports is meaningless — a permanently-failing instrument kills everything.
- **`ruleplace.sh` normalization deliberately does NOT strip `_`.** Stripping it as an emphasis marker
  destroys every identifier in the spec and produced five false absences. `shared_spans.py` matches it.
- **`shared_spans.py` at n=7 with punctuation stripped is the right sensitivity, empirically.** At n=5 it
  reports section-heading noise; the real rule duplications were all ≥7 words.
- **The reviewer prompt is the run's most reusable by-product.** `records/stage6d-prompt.md` — it leads
  with the *derive-it-yourself* question, freezes nine hashes, declares the supplementary context with its
  reason, and puts the criteria amendment to the reviewers as a self-certification risk.
- **A composition wart was found and deliberately NOT fixed:** the composed reviewer prompt contains **two
  sections headed "What the floor means for you"** (one in `redteam.md`, one in the aiming file). It was
  left alone because reviewers were holding the frozen artifact — **fixing it mid-flight is the exact
  violation this run already self-reported once.** Fix it in the next repair pass.
- **When sources conflict, the owner's spec wins — and the reconciliation is the RUNNER'S job.** A reviewer
  citing a lower-priority source is not thereby right.
- **Nothing committed, nothing installed.** The orchestrator commits. Do not sync to
  `~/.claude/skills/architect/` until attempt 2 is finished as a whole.

## 8. Files in this folder

| File | What it is |
|---|---|
| `RESUME.md` | **This file.** |
| `decisions.md` | **The gate log — read this second.** Last two entries are this run. |
| `1.5-criteria-v2.md` | **The accept bar**, N-01…N-26 + Part C, **as amended under FRZ-2**. |
| `1.5-criteria.md` | v1, superseded. See §6's warning about its hash. |
| `8-harness.md` | The 2026-07-29 runs (past tense, real output), **including F1/F2 — the first behavioural evidence this element has ever had** — headed by what the reviewers proved about the numbers. Plus the archived 2026-07-28 run. |
| `9-test-venue.md` | **The per-item isolation-vs-assembled decision under owner ruling R1** (record **2544**). Read it before proposing any new test. ⚠ Three known defects, all reviewer-confirmed: row A's count is **3, not 2** (`rules.tsv` 72→89→128); the N-03 retirement is **declared but not performed** (its 20 passes still count toward 123); and it **omits the paragraph of record 2544** that bears on F3's venue. |
| `0-baseline.md` | Fork-source rule inventory **B01–B19**, author decisions D1–D14. Still the regression bar. |
| `1-spec.md`, `2-plan.md`, `3-redteam-plan*.md`, `6-redteam-code.md` | **Pre-re-scope.** History. |
| `oracles/` | 7 files. **Real and working.** Do not rebuild — and `mutation-test.sh` is **frozen at 3 iterations** per R1. |
| `fixtures/` | **NO LONGER EMPTY.** `extract-gate/` (the can-fail fixture for the record extractor) and `smoke/` (the composed prompts F1/F2 were run against, verified byte-identical to the live artifact). |
| `records/` | Reviewer prompts and verbatim reviewer records **A–Q**. |
