# Architect's agent prompt set — manifest and provenance

**This file is not dispatched to any agent.** It records what the set is, how the files compose, and what
the set carries from its fork source. Agents read `charter-common.md` plus their role file, and nothing
else from this directory.

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
>   (`charter-common.md` §6), because `~/Documents/Architect.md` **L19** states it is *"the only admissible
>   source"* for the owner's actual words, and because any agent-writable record — a decision log
>   included — re-admits the forgery that clause was written against. Where the two sources conflict, the
>   owner's spec wins.
>
> **DELIBERATELY NOT CARRIED:** the fork source's **A/B-harness-arm supplementary-context prohibition** —
> Architect's design defines no A/B harness arms, so the rule would have no referent. The general rule it
> specialises (supplementary author-authored context must be quoted in the record as such) **is** carried.
>
> Self-contained copy, not a live dependency.

---

## Why the set is six files and not one document

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
| Red-team reviewer | `Spawn_redteam` | `redteam.md` |
| Divider | `Divisible` | `divider.md` |
| Split reviewer | inside `Divisible` | `redteam.md` + `divider.md` §B |
| Combiner | `Consensus` / `Union` / `Severity` | `combiner.md` |
| Leaf | `Spawn_leaf` | `leaf.md` |
| Node | `Spawn_node` | `node.md` |

## The composition rule — the thing that keeps six files from drifting

**`charter-common.md` is included verbatim by every role. Role files are additions only, and never restate
a rule the common core states.**

**If a role file needs to *modify* a common rule, that is the signal the rule was never common** — it moves
down into the roles that can act on it. This is the fork source's own composition rule (B19) applied to the
file set. It is not "keep them in sync"; nothing is duplicated, so there is nothing to sync.

**The diagnostic for what belongs in the common core:** *which roles can **act** on this rule?* A rule only
one role can act on is that role's, wherever it currently sits. The granularity floor is the worked example
— the spec binds it to **three** roles (`Divisible`, `Spawn_leaf`, `Spawn_redteam`) and it binds each of
them differently, so the **definition and the safety rationale** are common and the three **operative
clauses** are one per role file.

### The one declared duplication

**B18 ("graded on precision") is stated in both `redteam.md` and `divider.md` §B, each as that file's final
line.** It binds only finding-producing roles, so it is not common; and its **position is load-bearing**
(it is the fork source's final line, and it is the precision counterweight to a prompt that spends its
length licensing aggression). Under append-composition a common placement cannot stay last. Duplication is
the lesser cost, and it is declared here rather than left to be discovered.

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
| **B18** graded on precision | `redteam.md`, `divider.md` §B (declared duplication, above) |
| **B19** charter composition | `charter-common.md` §0 |

**No rule is in a silent third category:** every one of B01–B19 has a destination above, and the single
DROP is B15's A/B-harness sub-clause, named in the provenance blockquote.
