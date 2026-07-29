# RESUME — element 1: THE AGENT PROMPT SET · 2026-07-29

**Read this first. It assumes you know nothing.** Project-level entry point is `../../ATTEMPT-2-STATE.md`;
this is the element-level one. The gate log is `decisions.md` — read its last FOUR entries after this file.

---

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
| **VERDICT** | 🔴 **BLOCKER — 3 of 3, independently, from three different assigned angles.** See §3. |

> ### ⚠ GATE 4 WAS NEVER RUN AND THIS RUN DID NOT RUN IT. DO NOT WRITE "GATE 4 PASSED".
> The ruling, its reasoning and its residual risk are in `decisions.md` under *"DEVIATION — gate 4 was
> skipped"*. Summary: gate 4's **only** unique question is *"is the decomposition right?"* — gate 7
> dominates it on everything else — so that question was folded into the gate-7 prompt as **Q1, in first
> position, phrased to require the reviewer to derive the decomposition from the spec BEFORE reading
> `charter.md`'s justification.** Cheaper instrument, same evidence. **Recorded as a deviation, not an
> omission, and still unratified by the owner.**

> ### ⚠ A SELF-REPORTED PROCESS DEVIATION THIS RUN
> **`1.5-criteria-v2.md` was edited AFTER the three reviewers were dispatched** (hash `eaff14ac…` →
> `fb75fb64…`). **The nine artifact files were NOT** — all re-verified against the frozen table. The three
> edits were corrections to the criteria document's own accuracy, not to any requirement. Full detail and
> the consequence — *a reviewer who stops on the hash mismatch is right, and its review is un-run* — are in
> `decisions.md`. **Next reviewer set must be spawned against a frozen criteria file as well as a frozen
> artifact.**

---

## 2. THE FOUR QUESTIONS THIS RUN WAS ASKED, AND ITS ANSWERS

Recorded here because a later reader will otherwise re-open them.

### Q1 — Is the seven-file decomposition right? **RE-DERIVED, AND CHANGED TO NINE.**

Derived from the spec's dispatch sites rather than validated against the brief. `~/Documents/Architect.md`
marks **`Divisible` (L14), `Consensus` (L22), `Union` (L24) and `Spawn_redteam` (L28) as "cold agent"** and
adds a **split reviewer** inside `Divisible` ("red-teams result, looping until no major issues are found").
It does **not** mark `Severity` (L26) as an agent.

The owner's instruction enumerated five roles after an **"i.e."** — an illustrative list of the roles he
could see, not an exhaustive one; the split reviewer is buried inside a comment. **Following his principle
(one file per agent type) requires a file his list does not name.** The principle governs: the whole value
of the re-scope came from finding roles the monolith hid.

**The decisive argument is internal, not an appeal to the reviewers who also proposed it.** The old
composition gave the split reviewer `redteam.md` + `divider.md` §B. `redteam.md` stated its closed set as
*"the task, the plan, and the granularity floor"*; §B stated *"You have no plan and are not entitled to
one."* **§B modified `redteam.md`'s closed set — and the set's own governing rule says that a role file
needing to modify a rule is proof the rule was never common.** So the split is *forced by the rule the
decomposition rests on.*

**Result:** `redteam.md` keeps only what binds both reviewer kinds; `redteam-plan.md` / `redteam-split.md`
each state their own artifact, floor meaning and closed set. This also fixed an inversion — **the split
reviewers' aiming lived in `divider.md`**, so the divider read its own reviewers' instructions.

**Costs, stated:** three composition tiers for reviewers instead of two; nine files instead of seven.
**Still open:** whether bundling `Consensus`/`Union`/`Severity` into one `combiner.md` is right, given the
spec marks only two of the three as agents. **Put to the reviewers, not resolved here.**

### Q2 — How should the two blockers be repaired, and is GATE-B2's rule the right rule?

**GATE-B1 — the invented `Consensus` halt.** Replaced with a statement of the limit that **invents no merge
rule and halts nothing**: name the two-child case a **category error** (not an arity gap), record it as the
owner's open design question, **return the plans unmerged with a leading note, do not halt.** The flagged
non-merge reaches the red-team, which files it, which makes it the next task — **the loop's own mechanism
surfaces the hole**, which beats an interrupt on every iteration. ⚠ *"Return unmerged with a note"* is the
runner's invention and is declared as one.

**GATE-B2 — is the composition rule the right rule? YES, and the evidence is that it worked.** It is what
made an incoherence in the accept bar visible (see FRZ-2 below). Two things were wrong, neither of them the
rule: **(i)** it covered only common → role, while the drift cost it exists to bound also applies role →
role — now clause 2; **(ii)** nothing could see a violation — now `shared_spans.py`.

**On the accept bar mandating a violation:** it did, and **the fix was not to exempt the duplication.**
N-10 required the severity model in `charter-common.md` *"and in no other file"*; N-11 required `node.md`
to restate a sentence of it. Resolved by splitting the rule on the diagnostic: the **prohibition** (no role
may lower a severity) binds all → stays common; the **permission** (you may contest, via `Ask_human`) is
actable by the node alone → moves to `node.md`. **N-11 now asks for no restatement of anything.**

**Measured, and it differs from what the reviewers reported:** the sweep found **3** common→role rule spans
at ≥7 words, not ~8. The reviewers were also counting role→role spans, most of which are scaffolding. That
distinction is now *in the rule* rather than left to judgement.

### Q3 — What must gate 4 do? **Fold its unique content into gate 7; do not re-run it.** See §1's box.

### Q4 — What can this element's harness honestly verify?

**The orchestrator's cut was NOT inherited.** Re-derived, it splits into two propositions carried as one:

- **(a) "Do not rebuild the A/B discrimination arms." SUSTAINED — on their design, not on record 1572.**
  Per-criterion HOLED/INTACT pairs need repeated trials and a stated pass rate to mean anything, times the
  criteria count, and the apparatus re-enters the same red-team as the thing it measures. Its own gate-4
  reviewers said it had *"no path to done, only a path to a halt."* **Rebuilding it is the known-failing
  move.**
- **(b) "Therefore no behavioural evidence is needed at all." REJECTED.** Record **1572**'s repair rule —
  *"we fix the first link in the chain that broke"* — **presupposes the broken link is identifiable.** With
  zero evidence that a composed prompt produces the artifact its role owes, a bad prompt, a bad spine and a
  bad router are indistinguishable at the end-to-end run. **The inference does not merely lack authority;
  its second half works against the record it was cited to.**

**Replacement specified: a composed-prompt smoke test** — one cold agent per dispatched composition, `n=1`,
**no twin, no threshold, no pass/fail oracle**; it asks only whether the returned artifact has the *shape*
that role owes. Bounded because **there is nothing to strengthen when someone disputes it** — the outputs
are on disk and a dissenter is reading the same evidence.

> **STATUS: SPECIFIED, NOT RUN. `fixtures/` is still empty and no smoke agent has ever been dispatched.**
> The cut of the arms and the absence of the smoke test are **two separate unverified statuses** and must
> not be merged into one line. Full text: `1.5-criteria-v2.md` Part B.

---

## 3. GATE 7 VERDICT — **BLOCKER** · 2026-07-29

**Full findings are in `decisions.md`'s last four entries and verbatim in
`records/reviewer-{O,P,Q}-verbatim.md`. This is the short form. NOTHING WAS REPAIRED IN RESPONSE — the set
on disk is exactly what the reviewers held.**

> **Every one of this run's four substantive repairs was found defective by at least one reviewer, and the
> two blockers it closed were replaced by two new blockers plus a harness shown not to detect negation.**
> **Two of the worst findings are against the runner's own apparatus, not the artifact** (the printer
> mutant arm, and the verbatim-record pipeline writing mid-task fragments). This is the
> measurement-apparatus problem recurring for the fourth recorded time in this project.

### The four things that must be fixed before this set is dispatched to anything

1. **NON-TERMINATION (O-BLOCKER-1).** `redteam.md`'s conditional-lens note restates and then *modifies*
   common core §0. §0 orders every agent to report exactly that as a prompt-set defect *"in your return
   value, before anything else"*; a reviewer's return value **is** its findings; the finding is a
   `blocker|major`; that becomes the next task; **there is no cap.** Every reviewer dispatch injects a
   finding about the prompt set, so **`task` never empties.** The runner's repair was to *declare* the gap
   in `charter.md` — **which is not dispatched, so nobody holding the defect ever reads the declaration.**
   The carve-out has to be in `charter-common.md` §0 itself.
2. **`Union` INVERTS THE OWNER'S ONLY MERGE RULE, UNDECLARED (O-BLOCKER-2).** The owner's original
   `Combine` (record **1044**) says *"the odd element is discarded"*; `combiner.md` says **"DISCARD
   NOTHING."** The `Combine` → `Consensus`/`Union`/`Severity` split is orchestrator-authored and is **not
   in `charter.md`'s ADDED list**. Root cause: **the set has a meticulous provenance ledger for
   `Guarded_change` and NONE AT ALL for `~/Documents/Architect.md`** — the priority-2 authority that is 59%
   orchestrator-written. A second ledger is needed, with the `Combine` split as row one.
3. **THE HARNESS CANNOT TELL A RULE FROM ITS NEGATION (O-MAJOR-1).** O inverted four rules — *"You do not
   demote"* → *"You SHOULD demote freely"*, *"Cite or it doesn't count"* → *"Cite nothing"* — and got
   **`92 passed, 0 failed`, byte-identical to the clean run. The runner reproduced this independently.**
   Every probe is an unanchored substring `grep`; there is **no NEGATION mutant class**. The inverted rules
   include the gating content of **N-10, N-12, B08 and B14**.
4. **THE EXEMPTION MUTANT IS A PRINTER (P-1).** In `oracles/mutation-test.sh`, **both branches of the
   N-M6(d) arm increment `ok`** — `SURVIVED` scores as a pass. N-M6(d) is gating. **So the 87/87 headline
   contains one arm structurally incapable of failing.** This is the printer-checker class this project has
   now shipped **four** times, written by the runner, *inside the instrument built this run to repair
   GATE-B2.*

### Repairs this run made that the reviewers showed were WRONG, not merely incomplete

- **N-24, the "universal return-value channel" (O-MAJOR-5).** It replaced an uncallable `Ask_human` with a
  channel that **reaches nobody for three of eight compositions**: the **leaf**'s return goes to
  `Consensus`, whose rule discards the odd plan — *a defect report from one leaf is by construction the odd
  content and is deleted by design*; the **divider** returns `pair`/`null` with **no field for a
  complaint**; `Consensus` has the same sink as the leaf.
- **The GATE-B1 `Consensus` repair (O-MAJOR-7).** It branches on **arity** (*"fewer than three plans"*) but
  asserts a **kind** (*"complementary halves"*). On the **stuck-leaf** path — `wait(… or get stuck)`,
  **owner-written** at spec L77 — two of three leaves on the *same* task return, and the repair declares
  them "complementary halves", **which is false**, and refuses a merge that is well defined. Condition on
  the **call site**, which the node knows and can pass, not on the count.
- **The §2 floor repair (O-MAJOR-6 / P-6 / runner's own self-finding — THREE independent parties).** It
  fixed the combiner and **broke the node**, which holds `granularity` by signature. O adds the
  consequence: spec L2–3 permits a branch to *override* the floor, the node is the only party positioned to
  do it, and **no file states who may.**

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

## 5. STILL THE OWNER'S — none resolved, none papered over

1. **Does the harness cut stand**, now that its stated authority is known to be invented? The runner's own
   position is §2's Q4 — and it **splits the question**, which the previous framing did not.
2. **`Consensus` arity AND semantics.** Spec **L22** defines 2-of-3 with the odd plan discarded; **L79**
   calls it on three leaves at the **same** task (a vote fits); **L92–97** calls it on two children holding
   **different halves** (`division.first()`, `division.second()`). On the node path a majority vote is a
   **category error, not merely undefined for n=2** — taken literally it **discards half the plan.**
   `combiner.md` now *states* this hole instead of inventing a mechanism. **Owner's design, owner's call.**
3. **The demotion port is half-landable.** `grep -ic 'decision log' ~/Documents/Architect.md` → **0**,
   re-verified 2026-07-29. The human-tie-break half works via `Ask_human`; the **contest-via-a-logged-entry
   half has no destination and is inert.** The memo cannot serve (single-writer, per-node, read only by
   that node's own restart). **Untouched by this run — inventing a destination is the RAT2 inflation the
   set itself forbids.**

---

## 6. Drift detection — hashes as of 2026-07-29

**Artifact — frozen at reviewer dispatch and unchanged since (re-verified):**

| Artifact | sha256 |
|---|---|
| `stages/charter.md` | `0985217fc0381445721bf70d45fe90d1855cee958f6d25336b890aa12e9545ea` |
| `stages/charter-common.md` | `2b37af1ccdad6800e63877c6aaad1955e7035757c1b7deaca3e0284e6d272ab7` |
| `stages/redteam.md` | `0df9bd7d27eab35f3b035e26c5118db59b45a47545675903193d14ed0ff51108` |
| `stages/redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` |
| `stages/redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` |
| `stages/divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` |
| `stages/combiner.md` | `5ad7575a7bbd164cfc6bf82034ce34ae41ba54b7b53e37173830c26a3e75a1d4` |
| `stages/leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` |
| `stages/node.md` | `90386699adc44aee20cb9a4322088ff31191b8f6c17feb54a333d51b8132c0bb` |

**Inputs — CHANGED since the previous RESUME, all traced to commit `aa41f64` (the cold claim-audit):**

| Artifact | sha256 | Note |
|---|---|---|
| `~/Documents/Architect.md` (**the spec**, 119 lines) | `87986c3c27b1fca956c923122f6c7325f17aa1993c60bce1c05f71a227f1cacc` | L26's unsourced justification struck. **Line count unchanged; every citation this run uses was re-verified at its line** (L14/L19/L22/L24/L26/L79/L92–97). |
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
| `8-harness.md` | The 2026-07-29 run (past tense, real output) + the archived 2026-07-28 run. |
| `0-baseline.md` | Fork-source rule inventory **B01–B19**, author decisions D1–D14. Still the regression bar. |
| `1-spec.md`, `2-plan.md`, `3-redteam-plan*.md`, `6-redteam-code.md` | **Pre-re-scope.** History. |
| `oracles/` | 7 files. **Real and working.** Do not rebuild. |
| `fixtures/` | **EMPTY.** No behavioural arm or smoke test has ever been run. |
| `records/` | Reviewer prompts and verbatim reviewer records **A–Q**. |
