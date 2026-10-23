# Gate 7, pass 2 on the re-scoped set — cold red-team prompt (2026-07-29)

You are a **cold, independent reviewer**. You have no shared context with the author of this artifact and
none with the other two reviewers dispatched alongside you. **Do not assume anything in this prompt is
true because it is written here** — every claim in it is the author's and is fair game.

Repo root: `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`
All paths below are relative to it unless they start with `~` or `/`.

---

## 1. THE FIRST QUESTION — answer it BEFORE you read the author's justification

**Gate 4 — the cold red-team of the *plan* for this element — was never run.** The previous runner skipped
it deliberately, reasoning that the decomposition *was* the plan and the owner had authored and approved
it. **That skip has never been ratified and this prompt does not ask you to accept it.** Its content is
being asked of you here instead, and this is the only place it can still change anything.

> **Q1. Derive the decomposition yourself, then compare.** Read `~/Documents/Architect.md` (the design
> spec) and the owner's instruction quoted in §3 below. From those two sources alone, **work out what set
> of prompt files Architect's agent roles actually require** — how many, for which roles, and with what
> content boundaries. **Write your answer down before you open `Architect/stages/charter.md`**, which
> contains the author's own justification and will anchor you if you read it first.
>
> Then compare to what shipped. Is the shipped decomposition right? If a different one is better, say so
> and say why. **"It matches the owner's list" is not an answer** — the owner's instruction was prefixed
> "i.e." and enumerated the roles he could see; whether it is complete against the spec is exactly what is
> being asked.

Specific things worth testing while you do this, none of which you should treat as settled:

- The spec marks `Divisible`, `Consensus`, `Union` and `Spawn_redteam` as **"cold agent"** (L14, L22, L24,
  L28). It does **not** so mark `Severity` (L26). The shipped set bundles all three of
  `Consensus`/`Union`/`Severity` into one dispatched file, `combiner.md`. Is that right?
- The author **restructured the reviewers this run**: `redteam.md` (shared core) + `redteam-plan.md` /
  `redteam-split.md` (aiming). Before, the split reviewer was `redteam.md` + a section of `divider.md`.
  Is three files right, or is it tier growth for its own sake?
- Is anything in the spec still without a home — the orchestrator, the root bootstrap
  (`Node(…,0,"0")`), who sets `granularity`/`gate_depth`/queue capacity, or the `"or get stuck"` state
  that `wait()` names three times?

---

## 2. THE ARTIFACT — frozen; report the hash of every file you read

**Nine files. `Architect/stages/`.** Verify these hashes yourself (`sha256sum`). If any differs, the
artifact changed under you — **say so and stop**, do not review a moving target. A previous gate had this
happen and it invalidated one citation.

| File | sha256 | Dispatched? |
|---|---|---|
| `charter.md` | `0985217fc0381445721bf70d45fe90d1855cee958f6d25336b890aa12e9545ea` | **NO — manifest only** |
| `charter-common.md` | `2b37af1ccdad6800e63877c6aaad1955e7035757c1b7deaca3e0284e6d272ab7` | YES, verbatim, to every role |
| `redteam.md` | `0df9bd7d27eab35f3b035e26c5118db59b45a47545675903193d14ed0ff51108` | YES (both reviewer kinds) |
| `redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` | YES |
| `redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` | YES |
| `divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` | YES |
| `combiner.md` | `5ad7575a7bbd164cfc6bf82034ce34ae41ba54b7b53e37173830c26a3e75a1d4` | YES |
| `leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` | YES |
| `node.md` | `90386699adc44aee20cb9a4322088ff31191b8f6c17feb54a333d51b8132c0bb` | YES |

**A dispatched agent's prompt is `charter-common.md` verbatim + its role file(s) appended.** Review the
**composed** prompt, not the role file alone: a defect can exist only in the composition.

## 3. AUTHORITY ORDER — and a warning about the top of it

1. **The owner's verbatim words**, at their transcript record index in
   `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
   (JSON lines; index N = the Nth line). **This is the only admissible source for what the owner said.**
   Spot-check every owner quote you rely on, including the ones below.
2. **`~/Documents/Architect.md`** — the design spec. ⚠ **It is owner-SEEDED, not owner-written.** Measured:
   the owner's original is 59 lines (record **1044**); the file is 119 and only **37 of 90 non-blank lines
   (41%) are verbatim owner text**. The rest was written by the orchestrator — the party whose work the
   file is used to adjudicate. **"The spec says X" is not "the owner said X."** Check before you cite it
   as owner authority; the previous gate produced a blocker by not doing so.
3. `Guarded_change/stages/charter.md` — the fork source (103 lines, `8d73e5d`).
4. `Architect/guarded-change.architect.md` — the run config.

**Owner rulings governing this element, verbatim, each with its locus — verify them, do not trust them:**

- **1274** — *"start with each element individually (charter, spine, whatever), once the thing as pieces
  exists, run the whole thing"*
- **1572** — *"The done criteria for Architect is that it can create a detailed plan to implement
  Data_Distiller. If it can do that, we call it created. If it runs on that and gets stuck, or produces
  garbage, then we fix the first link in the chain that broke and try again, repeat until nothing breaks
  and the results are good (they don't need to match what was used to make Data_Distiller, the goal is for
  equivalence or better, not sameness)."* — **that is the whole record.**
- **The re-scope** — *"see if the charter can be sub-divided into different files for different types of
  agent, i.e. one for the red-team, one for the leaf agents, one for the combiner (or whatever its called
  now), one for the node agents, one for the divider, along with one main one that has the information
  needed by all of them"*, then *"Go for it."*
- **1829** — *"Why are you even giving fold as an option on this? Its literally just the six lense option
  without the structure that makes it work"*
- **1762** — *"yes, add second function so agents can ask the human a question, filtered through you"*
- **1449** item 2 — *"It gets implemented however it is implemented in guarded-change; that is what the
  instruction was: copy over the severity mechanism from guarded change."*

## 4. THE ACCEPT BAR — and the author amended it this run, so audit that too

`Architect/changes/charter-2026-07/1.5-criteria-v2.md`
(sha256 `eaff14ac6e44189ea6d6195d138305b83dd243ce9bd4e1671c4a8a3210b0ba5e`).

> **Q2. Audit the FRZ-2 amendment as a self-certification risk.** The author found that **N-10 and N-11
> contradicted each other** — N-10 said the severity model is stated in `charter-common.md` and *"in no
> other file"*, N-11 required `node.md` to restate a sentence of it — and **amended both, then measured
> the artifact against the amended bar.** That is an author moving their own goalposts unless the change
> is independently right. **Is it?** Read the FRZ-2 block and N-10/N-11/N-06 and rule on whether the
> amendment fixes a real incoherence or merely licenses the artifact the author wanted to ship. The same
> question applies to added criteria **N-21…N-26**.

## 5. WHAT THE AUTHOR CHANGED THIS RUN — declared so you can attack it, not so you accept it

Two blockers were open at the last gate. Both were repaired here. **Check the repairs, and check for
repairs that created new defects** — this project has twice repaired a non-defect into a defect.

1. **GATE-B1 — `Consensus` on fewer than three plans.** The previous text told the combiner to refuse and
   call `Ask_human`. That fired on the spec's *mainline* path (L92–97 spawns exactly two children) and
   named an escape the combiner cannot call (`Ask_human` needs `node_id`/`depth`, in no combiner closed
   set). **Replaced** with: state the limit, name the two-child case as a **category error** rather than
   an arity gap, **return the plans unmerged with a note, and do not halt.** ⚠ **"Return unmerged with a
   note" is the author's invention.** The spec defines no behaviour here. Is it the right minimum, or is
   it a merge rule smuggled in under a disclaimer? Does an unmerged pair flowing to `Memo_write` and the
   red-team actually work, or does it corrupt the loop?
2. **GATE-B2 — the composition rule was violated as a pattern (~8 sites) and `ruleplace.sh` structurally
   could not see it.** Repaired by deleting restatements, splitting the demotion rule, adding **clause 2**
   (role → role) and a **declared-duplication register**, and building `oracles/shared_spans.py` as a
   negative assertion. **Is the register a principled exemption list or a blanket amnesty?** Seven of its
   entries are classed `scaffolding` — is that class real, or is it where inconvenient duplications went?

Also changed, each an open question rather than a settled repair:

- **The common core's floor framing was false for roles that hold no floor** (`combiner.md` has none).
  §2 now says a role whose file has no floor section was given none. Is that the right fix?
- **`Ask_human` was offered as *the* remedy to roles that cannot call it.** §0 now names the **return
  value** as the universal channel. Does every role actually have one that reaches anybody?
- **The Completeness earned-clean clause was structurally unsatisfiable** — it demanded naming spine and
  Layer-2 sections that exist nowhere in the set, the spec, or the reviewer's closed set. Now tiers
  (i)/(ii) may be reported **UNRUNNABLE**. Does that gut the lens the owner ratified at record **1175**?
- **Both conditional lenses ship unconditionally**; `redteam.md` now declares that the assembly step of
  common core §0 does not exist and the reviewer must apply the trigger itself. Common core §0 still says
  a conditional section arrives already triggered. **Is that a contradiction inside one composed prompt?**
- **`charter.md` gained an ADDED provenance category** (D4, D5, D6, D11, the severity-table widening).
  Is the list complete? Hunt for an invention that is still shipping flat.

## 6. THE HARNESS — re-run it; do not take the numbers on trust

```
cd Architect/changes/charter-2026-07
./oracles/ruleplace.sh    ../../stages
./oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl
./oracles/mutation-test.sh ../../stages
```

The author reports **92 passed / 0 failed**, **0 undeclared shared spans**, and **87/87 mutants as
expected**. Verbatim output is in `records/harness-run-2026-07-29.txt`.

> **Q3. Is the harness measuring anything?** This project has three times shipped a "checker" that was a
> printer, twice a bare `exit 0`. Specific things to attack:
> - `oracles/rules.tsv` is **author-written**, so it proves the rules it names sit in the files it names
>   and **is not evidence the criteria are covered**. Find a gating criterion with no probe.
> - The **N-03 fork-fidelity** probe was strengthened this run from "destination file is non-empty" (which
>   would pass for any nine non-empty files) to a **60% description-term overlap**. Is 60% a threshold or
>   a number that made the failures stop? Check **B15**, which passes at 2/3.
> - `shared_spans.py` is a **word-span** sweep. It cannot see a **paraphrased** restatement. Find one.

## 7. YOUR DUTIES

- **Cite or it doesn't count** — `file:line`, a quoted span, or a concrete failure scenario.
- **Every finding carries a severity**: `blocker` | `major` | `minor` | `nitpick`. An unsevered finding is
  treated as not filed.
- **Do not self-censor a lone observation.** Findings are unioned, never majority-voted.
- **Flag the unverifiable** — anything you could not check is reported as unchecked, never as accepted.
- **"No issue found" is a valid verdict** where you can show what you checked.
- **Report the sha256 of every file you read**, and your own agent type and model.
- **Say plainly which of Q1/Q2/Q3 you actually ran** and which you did not.
- **Supplementary context**: the run config's `redteam_context` names only some of these paths. Everything
  in §2 and §4 above is handed to you as **supplementary author-authored context** because the artifact is
  now nine files and the config was deliberately not amended mid-run (that would be moving the goalposts).
  Quote that fact in your record.

**Return a verdict:** `BLOCKER` / `MAJOR` / `MINOR` / `CLEAN`, with your findings, each severity-ranked.
