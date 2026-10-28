# divide-0 — node 0, iter 0

**Answer returned: a division.** Three approvals in round 1 (a, b, c). One round ran; the four-round
cap was not approached.

**Off-limits fence honoured.** `/home/zero/Desktop/claude-code-skills/Data-Distiller/` was not read,
listed, grepped or otherwise opened by me, and the fence was stated verbatim in the prompt of every
one of the three agents I dispatched. All three confirmed in writing that they honoured it and that
they dispatched no further agents (or passed the fence on). Nothing in this file derives from that
directory.

---

## Where the seam is

**Between the executable method — the per-role prompt files that carry the procedure — and the
skill's entry, contract and orientation layer.**

The joint is observable on disk in both sibling skills: `Dragonfly/SKILL.md:8-11` and
`Guarded_change/SKILL.md:7-10` each declare themselves a **router** whose procedures are deferred to
a physically separate `stages/` directory, with `METHODOLOGY.md` holding the orientation/reference
spec and the config contract. Across that boundary the material differs (imperative role prompts vs.
explanatory reference prose), the kind of work differs (designing a multi-agent protocol vs.
specifying a config contract, a router table and orientation docs), and the thing produced differs
(the method as executed vs. the skill's interface to whoever invokes and configures it).

**Shared vocabulary fixed by the seam itself**, so the two halves can be planned blind: the pipeline
runs **decompose/size → N cold analysts → cold verify → agreement-ranked merge → blind roll-up**,
with restart/resume from on-disk state throughout; role prompt files live under `stages/`.

### Correction to the seam's wording (from reviewers a and b; does not change the cut)

I originally labelled the seam as *"files a dispatched agent reads verbatim mid-run"* vs. *"files a
human or the invoking session reads."* Two reviewers checked that against the siblings and it is
**false as a statement about who reads what**: in `Guarded_change`, the `stages/*.md` files are read
by the **driving session** as it walks the loop (`Guarded_change/SKILL.md:31-33` — *"at each stage,
read that stage's file for the full procedure"*), and only `stages/charter.md` is handed to
dispatched cold reviewers (`Guarded_change/stages/charter.md:1-4`; `SKILL.md:40,43`). Both reviewers
found the file placement right and the label wrong, and approved. The seam is therefore stated above
by **role in the artifact** (executable procedure vs. entry/contract/orientation), not by reader
identity. Recorded here so the wrong label is not inherited downstream as a placement rule.

The sub-tasks below are reproduced **exactly as reviewed and approved**; the phrase "reads verbatim
while a distillation run executes" in sub-task A is subject to the correction above.

---

## Sub-task A — the runtime prompt files

Plan the implementation of the **runtime prompt files** of the Data-Distiller skill at
`/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/` — the markdown files a dispatched
agent reads verbatim while a distillation run executes. This covers: the shared common/charter
file every dispatched agent reads first, and the per-role prompt files implementing the method —
corpus decomposition and item sizing including the strategy for over-size items; the N independent
cold read-only analysts per item, each citing every finding; the cold verification pass that drops
unverifiable citations; the agreement-ranked merge; the blind roll-up in which a coordinating
agent reads only a terse per-child status; and the discipline by which each role reads and writes
on-disk run state so a run can be restarted and resumed. "Facts, not interpretation" is the
standing constraint these prompts must enforce on the agents that read them.

Source material: sibling skills `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/` (in particular their `stages/` directories and
`stages/charter.md`) for house style and structure.
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits: do not read, list, grep or
otherwise open it, and say so in your output.

Granularity floor: one file created or one coherent edit to one file, with the content that goes
in it specified.

## Sub-task B — the entry, contract and orientation layer

Plan the implementation of the **entry, contract and orientation layer** of the Data-Distiller
skill at `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/` — the files read by a human
or by the invoking session rather than by a dispatched agent mid-run. This covers: the skill
directory scaffolding; `SKILL.md` with its frontmatter (name, triggering description) and the
router that names each phase of the method and when to read it; `METHODOLOGY.md` giving the
rationale for the method, the **per-corpus Layer-2 config contract** that keeps the method
corpus-agnostic (what a config must supply, what it may not), the **on-disk run-state layout** and
what restart and resume mean against it, and what a completed run produces; `README.md`; the
companion file; and at least one worked example Layer-2 corpus config demonstrating the contract.

Source material: sibling skills `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/` (in particular their top-level `SKILL.md`,
`METHODOLOGY.md`, `README.md` and `*.companion.md`) for house style and structure.
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits: do not read, list, grep or
otherwise open it, and say so in your output.

Granularity floor: one file created or one coherent edit to one file, with the content that goes
in it specified.

## Coverage

All eight defining properties land: properties 1–5 and 8 (decompose/size, N analysts, verify,
merge, blind roll-up, facts-not-interpretation) are enforced in A's runtime prompts; properties 6
and 7 (Layer-2 config, restart/resume from on-disk state) have their contract and layout specified
in B and are exercised by the roles in A. Nothing is orphaned: every file the skill directory will
contain belongs to exactly one half.

**Floor check.** Neither half is at or below the floor: A is on the order of six to eight prompt
files and B six documents, each still requiring planning before a practitioner could execute it.

---

## Rounds, splits proposed, and reviewer verdicts

**Splits proposed: one.** The split above (executable method / entry-contract-orientation layer).

**Round 1 — three approvals, division returned.**

| Reviewer | Verdict | Report |
|---|---|---|
| a | **approve** | `<run>/0/split-review-1-a.md` |
| b | **approve** | `<run>/0/split-review-1-b.md` |
| c | **approve** | `<run>/0/split-review-1-c.md` |

(`<run>` = `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/it4/`)

**Rejections: none.** There is therefore no verbatim rejection record to reproduce, and no
`FAILED_TO_DIVIDE` path was taken.

**Non-blocking notes the reviewers recorded** (carried forward, not acted on as rejections):
- a and b: the seam's *label* misstated who reads sibling `stages/*.md` — corrected above; both
  judged the file placement correct regardless.
- b: the config / run-state coupling across the seam (B specifies the layout, A's roles use it) is
  the owner's cross-half-dedup case — checked against the original task on the node's next pass, not
  a split-time defect.
- c: B's router will name A's phases; covered by the shared vocabulary fixed at the seam.
