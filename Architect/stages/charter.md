# Architect's agent prompt set — manifest and provenance

**This file is not dispatched to any agent.** It records what the set is, how the files compose, and what
the set carries from its fork source. An agent reads `charter-common.md` plus the role file(s) named for
it in the table below, and nothing else from this directory.

> **Provenance.** Forked from `Guarded_change/stages/charter.md @ 8d73e5d` (sha256
> `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`).
>
> **CARRIED:** the five lenses; every unconditional discipline bullet (cite-or-it-doesn't-count, rank every
> finding, flag the unverifiable, "no issue found" is valid, earned-clean factual, earned-clean fidelity,
> spot-verify the citations, the provenance record + closed set, graded on precision); both conditional
> lenses (position, concurrency); and the charter-composition rule.
>
> **CHANGED — each difference stated where a reader of the shipped files can see it:**
> - **Five lenses → six.** Completeness is added as a lens, with its three tiers and an earned-clean clause
>   (`redteam.md`). Owner record **1175** ratifies the inclusion of the three-tier definition; the
>   lens-vs-bullet placement is an author decision (D1).
> - **The severity model is stated in-file** rather than by a cross-file reference (`charter-common.md`
>   §3). The fork source says "rank every finding by severity **(below)**" and contains no table — the
>   referent lives in `Guarded_change/stages/stage-4.md`. Architect has no stage files and `Severity()`
>   consumes severities directly, so the dangling pointer is closed. **An unsevered finding is additionally
>   treated as not filed**, because `Severity()` filters on severity and an unsevered finding is dropped on
>   the floor.
> - **The closed set is stated per-role**, bounded by each role's own function signature
>   (`charter-common.md` §5 states the principle; each role file states its own list), because Architect's
>   roles take different arguments.
> - **The composition rule (B19) is re-aimed** from guarded-change's stage-specific additions to this set's
>   common-core-plus-role-file structure (`charter-common.md` §0).
> - **NARROWED — the durable source for an owner quote.** `Guarded_change/stages/stage-3.md` L59 admits
>   several durable sources. Architect admits **only the harness-authored session transcript**
>   (`charter-common.md` §6). **CAUTION ON THE AUTHORITY FOR THIS.** It was justified by
>   `~/Documents/Architect.md` **L19** stating the transcript is *"the only admissible source"* — but L19 is
>   the `// PROVENANCE` comment, which is **orchestrator-written (transcript record 1787) and absent from
>   the owner's original**. So this narrowing rests on the *substantive* argument only: any agent-writable
>   record — a decision log included — re-admits the forgery the clause was written against. That argument
>   may well be right, but it is **not an owner ruling**, and it must not be cited as one.
>
> - **CHANGED — the provenance record's element (i), from a verbatim copy to a hash.** The fork source
>   requires the record to embed *"the verbatim prompt you were given"* (B15). `charter-common.md` §5 now
>   requires the **path and sha256 of every file the prompt was composed from**, plus verbatim text only
>   for parts with no durable file. **This is a change made on measurement, not on preference:** handed the
>   old wording, two of three cold agents **declined to paste the prompt back** and substituted the hash
>   unprompted, which under the old rule made their records *un-run*. A re-typed copy can drift; a hash
>   cannot. The rule's purpose — that "the prompt given" is reproducible by a third party — is better
>   served by the new form, and the escape for file-less text keeps the coverage the old form had.
>
> **ADDED — rules with no fork-source ancestor, each an author decision and none of them owner rulings.**
> They were previously shipped flat, indistinguishable from carried material; that is corrected here.
> Full reasoning per item is in `changes/charter-2026-07/0-baseline.md` §0.5.
> - **D4 — the demotion rule** (`node.md`). Imported from guarded-change's **SEV3**, which is *stage-file*
>   content there (`Guarded_change/stages/stage-4.md` L31–36), **not** charter content. Owner record
>   **1449** item 2 instructed that the severity mechanism be implemented as guarded-change implements it;
>   **the import is that instruction, the choice of destination file is the author's.**
> - **D5 — "recurrence means under-generalization, not thrash"** (`redteam.md`). No fork-source ancestor
>   and none in the design spec. Author decision, evidenced by this project's own history.
> - **D6 — "and no shared reasoning context with each other"** appended to the definition of *3 independent
>   cold agents* (`charter-common.md` §1). The owner's words define independence no further; this
>   strengthening is the author's.
> - **D11 — the `UNSUBSTANTIATED` mark** (`combiner.md`). Record **1449** item 3 ratifies **where the
>   spot-verify duty lives** and nothing more. **The mark itself, its name, and the rule that it travels
>   with the finding are the author's elaboration** — declared here under RAT2 rather than reported as
>   owner authority. The clause that once made a marked finding *not pass to `Severity` as blocker|major*
>   was removed as an unratified inflation; see `1.5-criteria-v2.md`'s FRZ note.
> - **The severity table's trigger clauses** (`charter-common.md` §3). Record **1449** item 2 said to copy
>   guarded-change's mechanism. The table states **three trigger clauses beyond** `Guarded_change/stages/
>   stage-4.md` L17–22 — including promoting *"omits a load-bearing element of the task"* to **blocker**.
>   **That is a widening, not a copy**, and it is declared rather than presented as the ported mechanism.
>
> **DELIBERATELY NOT CARRIED:** the fork source's **A/B-harness-arm supplementary-context prohibition** —
> Architect's design defines no A/B harness arms, so the rule would have no referent. The general rule it
> specialises (supplementary author-authored context must be quoted in the record as such) **is** carried.
>
> **RESOLVED 2026-07-29 — the conditional-inclusion contradiction.** §0 previously promised that a
> conditional section reaches an agent only once its trigger has fired, and `redteam.md` then declared
> that untrue and told the reviewer to apply the trigger itself. Cold reviewer **O** showed that was not a
> documentation gap but a **non-termination bug**: §0 also orders every agent to report a role-file/core
> contradiction as a prompt-set defect *"in your return value, before anything else"*; a reviewer's return
> value **is** its findings; `Severity` passes it; and `node.md` has no cap — so `task` never empties.
> The declaration that was supposed to defuse it lived **here, in a file no agent is given.** Fixed at the
> source: **§0 now states that a conditional section names its own trigger and the holder applies it**, and
> says explicitly that a role file doing so is *not* a defect. `redteam.md` no longer modifies §0.
> **OOS-14 is withdrawn** — there is no longer a gap to defer.
>
> **TRACKING THE DESIGN SPEC — by CLAIM plus a re-derivable check, not by a hash of the whole file.**
>
> **Why not a hash.** `~/Documents/Architect.md` is owned and edited by a third party *during* this run. A
> whole-file hash pinned here is a claim about a file this set does not control: it goes stale on **any**
> edit, including edits to lines this set makes no claim about, and it then fails **uninformatively** — a
> reader sees a mismatch and cannot tell whether anything they rely on moved. That happened three times in
> this run, and the pin was wrong while every claim around it was sound. **So each claim below carries the
> command that verifies it.** A spec edit invalidates a row **only when it touches what the row asserts.**
>
> | What this set relies on | Re-derivable check | Expected |
> |---|---|---|
> | The node-path merge is `Union` | `grep -c 'plan = Union(child.get_plans)' ~/Documents/Architect.md` | `1` |
> | The leaf merge is `Consensus` | `grep -c 'plan = Consensus(leaves.get_plans)' ~/Documents/Architect.md` | `1` |
> | `Union` is input-agnostic | `grep -c 'INPUT-AGNOSTIC' ~/Documents/Architect.md` | `1` |
> | A decision log exists | `grep -c 'Log_decision' ~/Documents/Architect.md` | `1` |
> | The node is given `granularity` | `grep -c 'Spawn_node(string task, string plan, string granularity' ~/Documents/Architect.md` | `1` |
> | The floor bounds three things | `grep -c 'It bounds THREE things' ~/Documents/Architect.md` | `1` |
>
> **Observed at 2026-07-29: 131 lines, sha256 `8ad9d620be794047b3606e948e20d3cd70b5413c36b9dd19f0dc97d8d107a474`.**
> That is a **timestamped observation, NOT a freeze** — do not halt on a mismatch; run the checks instead.
>
> **This distinction is general and is worth carrying:** a hash recording *what an agent was handed* (§5)
> is a **historical** pin and is sound, because nothing later can falsify a fact about the past. A hash
> asserting the current state of a file someone else owns is a **liveness** pin and is not. The two look
> identical and behave oppositely.
> - **The node-path merge is `Union`, not `Consensus`** (**L109**), **owner record 2524 item 2** — and
>   **the ruling is hedged in the original**: *"that should **probably** be Union rather than Consensus."*
>   It is recorded with its qualifier because RAT1 requires the confirming turn to be captured as it was. The two children hold `division.first()` / `division.second()`, so a
>   2-of-3 vote would discard half the plan. `combiner.md` is rewritten accordingly: `Consensus` now has
>   **one** call site (three leaves, one task, **L91**), and `Union` has **two** — plans at L109, issues at
>   L122.
> - **`Union` is GENERALIZED — input-agnostic** (**owner record 2680**). The declaration at **L24** now
>   reads *"sticks the provided inputs together into one, DISCARDS NOTHING, dedups only exact
>   restatements"* and names both call sites. The owner: *"Union should be generalized to stick the
>   provided inputs together, the only reason its issue specific is because you wrote the comment for it
>   as such."* **Verified: `Union` does not appear in the owner's original spec at all** (harness record
>   1044, 59 lines) — it came from the `Combine` split, and *"merges issues"* was an orchestrator comment,
>   **never a design constraint.** `combiner.md` accordingly states **one rule that does not vary with the
>   input**, and explicitly warns against reasoning *"these are issues, so…"*. **The one specialization it
>   keeps — ordering a plan merge along the divider's seam — is declared there as an author decision**,
>   because the declaration is silent on order and `Consensus` treats order as content.
> - **A decision log now exists** (**L36–46**): `Log_decision` / `Read_decisions`, **append-only, one per
>   run, shared by every node** — the opposite of `Memo_*`. **Owner record 2524 item 3**, the same message
>   as the merge ruling: *"Why is there no decision log? There should definitely be a decision log."* This closes the half of the ported severity mechanism that
>   had no destination, so `node.md` now logs a contested severity **and** asks the owner, in that order.
>   **It is agent-writable and is therefore still NOT admissible for the owner's words** — `charter-common.md`
>   §6 says so explicitly, because a durable timestamped forgery is more persuasive, not more true.
>
> Self-contained copy, not a live dependency.

---

## Why the set is seven dispatched files and not one document

Every dispatched agent reads its prompt **verbatim**, so every line a role does not need is a line that
crowds out one it does. The single 237-line predecessor was a red-team prompt with other roles' duties
embedded as asides, and two of those asides were **unreachable by the role they bound**:

- the **spot-verify** duty instructed **`Union`** but lived in the reviewer's prompt, which `Union` never
  reads;
- the **demotion** rule told the **node** when to call `Ask_human`, in the same place.

Three roles — **leaf**, **node**, and **combiner** — had no instructions in any file. Splitting the set is
therefore not a refactor of the charter; it is writing the half of the skill that did not exist.

## The files, and who reads what

| Role | Spawned by | Prompt = `charter-common.md` + … |
|---|---|---|
| Plan reviewer | `Spawn_redteam` | `redteam.md` + `redteam-plan.md` |
| Split reviewer | inside `Divisible` | `redteam.md` + `redteam-split.md` |
| Divider | `Divisible` | `divider.md` |
| Combiner | `Consensus` / `Union` / `Severity` | `combiner.md` |
| Leaf | `Spawn_leaf` | `leaf.md` |
| Node | `Spawn_node` | `node.md` |

**Why the two reviewers are three files and not one.** They share the lenses, the discipline and the
ratification audits, and they differ in the one place a reviewer must not be wrong about: **the closed
set.** The plan reviewer holds a plan; the split reviewer holds a division and **explicitly no plan**. The
previous arrangement composed the split reviewer as `redteam.md` + a section of `divider.md`, so the
appended section had to **modify** `redteam.md`'s stated input list — and by the composition rule below,
**a role file needing to modify a rule is the proof that the rule was never common to both.** So the input
list moved down into two thin aiming files and `redteam.md` kept only what genuinely binds both. This also
removes an inversion: the split reviewers' aiming used to live in the **divider's** file, where the divider
read it and its actual readers reached it only by composition.

## The composition rule — the thing that keeps the set from drifting

**`charter-common.md` is included verbatim by every role. Role files are additions only, and never restate
a rule the common core states.**

**If a role file needs to *modify* a common rule, that is the signal the rule was never common** — it moves
down into the roles that can act on it. This is the fork source's own composition rule (B19) applied to the
file set.

It is **not** "keep them in sync." It has two clauses, and the second was missing until gate 7:

1. **Common → role.** A role file never restates or modifies a rule stated in `charter-common.md`. The
   common core is appended verbatim directly above it, so a restatement adds nothing and can only drift.
2. **Role → role.** Two role files may share **scaffolding** — the composition banner, the stem of the
   closed-set section — because that is structure rather than rule, and each states a *different* list
   under it. They may not share a **rule**. A rule stated in two role files either belongs in the common
   core (if every role can act on it) or belongs to exactly one of them (if not); the only exception is a
   duplication **declared in the register below**.

**The diagnostic for what belongs in the common core:** *which roles can **act** on this rule?* A rule only
one role can act on is that role's, wherever it currently sits. The granularity floor is the worked example
— the spec binds it to **three** roles (`Divisible`, `Spawn_leaf`, `Spawn_redteam`) and it binds each of
them differently, so the **definition and the safety rationale** are common and the **operative clauses**
are one per role file. It is also the worked example of the *negative* case: the combiner is given no floor
by its signature, so `charter-common.md` §2 now says plainly that a role whose file has no floor section
was given none — the earlier text told every role it had one.

### The declared-duplication register — mechanically enforced, not a promise

Any duplication not in this register is a defect. **The register is the exemption file read by
`oracles/shared_spans.py`** (`changes/charter-2026-07/oracles/declared-duplications.jsonl`), so an
undeclared duplication fails the harness rather than waiting to be noticed by a reader.

| Duplicated span | Sites | Why it is allowed |
|---|---|---|
| **B18, "graded on precision"** | `redteam-plan.md`, `redteam-split.md` — each the file's **final line** | It binds only finding-producing roles, so it is not common; and its **position is load-bearing** — it is the fork source's final line and the precision counterweight to a prompt that spends its length licensing aggression. Under append composition the last file wins the last line, and the two reviewers end with different aiming files, so no single placement can be last for both. |

**Scaffolding, excluded by clause 2 and named here so the exclusion is not silent:** the role-file
composition banner, and the opening stem of each role's *"Your inputs (the closed set of §5)"* section.
Neither states a rule; each is followed by a list that differs per role.

## Where each fork-source rule now lives

Baseline IDs are `changes/charter-2026-07/0-baseline.md` §0.2.

| Fork rule | Now in |
|---|---|
| **B01** cold + independent + source access | `charter-common.md` §1 |
| **B02** lenses kept separate | `redteam.md` (six lenses) |
| **B03** lens 1, Factual | `redteam.md` |
| **B04** lens 2, Logical | `redteam.md` |
| **B05** lens 3, Missed opportunity | `redteam.md` |
| **B06** lens 4, Unstated assumptions & risks | `redteam.md` |
| **B07** lens 5, Fidelity | `redteam.md` (lens 5, RAT1, RAT2) |
| **B08** cite or it doesn't count | `charter-common.md` §4 |
| **B09** rank every finding | `charter-common.md` §3 |
| **B10** flag the unverifiable | `charter-common.md` §4 |
| **B11** "no issue found" is valid | `redteam.md` |
| **B12** earned-clean factual | `redteam.md` |
| **B13** earned-clean fidelity | `redteam.md` |
| **B14** spot-verify the citations | `combiner.md` (`Union`) — **the relocation this split exists for** |
| **B15** provenance record + closed set | `charter-common.md` §5 + each role file's input list |
| **B16** conditional: position/order | `redteam.md` |
| **B17** conditional: concurrency | `redteam.md` |
| **B18** graded on precision | `redteam-plan.md`, `redteam-split.md` (declared duplication, above) |
| **B19** prompt-set composition | `charter-common.md` §0 |

**No rule is in a silent third category:** every one of B01–B19 has a destination above, and the single
DROP is B15's A/B-harness sub-clause, named in the provenance blockquote.
