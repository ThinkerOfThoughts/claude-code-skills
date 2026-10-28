# Gate 7, pass 3 — cold red-team of the REPAIRED set (2026-07-29)

You are a **cold, independent reviewer**, with no shared context with this artifact's author and none with
the other two reviewers dispatched alongside you. **Nothing in this prompt is true because it is written
here.** Every claim in it is the author's, and all of it is fair game — including the author's account of
what it repaired.

Repo root: `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

---

## 1. THE ARTIFACT — nine files, `Architect/stages/`. Verify every hash yourself.

If any differs, the artifact moved under you: **say so and stop.** That has happened twice in this run and
both times it invalidated something.

| File | sha256 | Dispatched? |
|---|---|---|
| `charter.md` | `c12a659a475c7843d0d8f94bb1050acf12a47b30001fdc294c1d84390098e9ab` | **NO — manifest** |
| `charter-common.md` | `301d996fad9717558064ce66dd5d58147fad07d5630cad032cc41616e4335007` | YES, verbatim, to every role |
| `redteam.md` | `c28fcbcf634ee5b781872a6da8776ccddb162ff1c1346750fbc303d02102b838` | YES (both reviewer kinds) |
| `redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` | YES |
| `redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` | YES |
| `divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` | YES |
| `combiner.md` | `1723d4c763470a93ac5a7217205623beb5f0fced757263c863d44b888323ea3e` | YES |
| `leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` | YES |
| `node.md` | `48d5c6395f09dcb23313a7c87e9ead9f2f74b22a14a087126b8819109bc810bd` | YES |

**A dispatched agent's prompt is `charter-common.md` verbatim + its role file(s) appended.** Review the
**composed** prompt — reviewers get three files. Pre-composed copies used for a real dispatch are in
`Architect/changes/charter-2026-07/fixtures/smoke/`.

## 2. AUTHORITY ORDER, and a warning about the top of it

1. **The owner's verbatim words**, at their record index in the harness transcript
   `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
   (JSON lines; index N = the Nth line). **The only admissible source for what the owner said.**
   ⚠ **A previous reviewer found that a quote presented here as "the whole record" was the middle of a
   three-item message. Read the WHOLE record around any quote you rely on.**
2. **`~/Documents/Architect.md`** — the design spec, **131 lines**, sha256
   `aedcb80e220937bb8cab62d0e2e15b033a3cd30844f51cc7f83ce6d818e75886`. ⚠ **Owner-SEEDED, not
   owner-written**: the owner's original is 59 lines (record **1044**) and roughly 41% of the current file
   is verbatim owner text. **The rest was written by the orchestrator — the party whose work this file is
   used to adjudicate.** *"The spec says X"* is not *"the owner said X."* **Every function signature in the
   file is agent-written**, so do not treat differences in how functions are annotated as owner intent.
3. `Guarded_change/stages/charter.md` — the fork source (103 lines, `8d73e5d`).
4. `Architect/changes/charter-2026-07/0-baseline.md` — the B01–B19 fork inventory.

**Owner rulings governing this element — verify each at its locus, do not trust this table:**

| Ruling | Locus |
|---|---|
| *"start with each element individually (charter, spine, whatever), once the thing as pieces exists, run the whole thing"* | **1274** |
| The done criteria — a detailed plan to implement Data_Distiller, *"equivalence or better, not sameness"* | **1572** (a three-item message; read all of it) |
| The re-scope — *"see if the charter can be sub-divided into different files for different types of agent…"* | **1977**, then *"Go for it."* at **1994** |
| Six lenses — *"Its literally just the six lense option without the structure that makes it work"* | **1829** |
| `Ask_human` | **1762** |
| *"copy over the severity mechanism from guarded change"* | **1449** item 2 |
| *"if the experiment is to test where the granularity floor should sit, than the experiment should actually try moving the floor"* | **1449** item 1 |
| **The testing rule** — *"if a component can be tested in isolation, it should be. If testing it requires more than three iterations of the test mechanism, reconsider…"* | 2026-07-29 |
| **`Union` generalized** — *"Union should be generalized to stick the provided inputs together, the only reason its issue specific is because you wrote the comment for it as such."* | 2026-07-29 |
| **The decision log** — *"Why is there no decision log? There should definitely be a decision log."* | 2026-07-29 |

## 3. WHAT CHANGED SINCE THE LAST GATE — declared so you can attack it

Reviewers O, P and Q returned **BLOCKER 3/3** on the previous version. Their full records are in
`records/reviewer-{O,P,Q}-verbatim.md`. **Read at least one.** Since then:

| # | Change | Attack it |
|---|---|---|
| 1 | **§0 rewritten** so deciding whether a conditional section applies is the holder's job, **and a role file doing so is explicitly not a defect**. `redteam.md` no longer modifies §0. | O traced the old text to **non-termination**. Is the new §0 actually free of it, or has the contradiction just moved? |
| 2 | **Node-path merge is `Union`** (`node.md`, `combiner.md`). `Consensus` now has one call site. | The author claims this *dissolves* O-MAJOR-7 rather than repairing it. Does it? |
| 3 | **`Union` rewritten as ONE input-agnostic rule** after the owner's ruling. It keeps **one specialization** — ordering a plan merge along the seam — declared as an author decision. | Is that specialization actually entailed by *"sticks the inputs together"*, or is it an unratified inflation under the set's own RAT2? |
| 4 | **Decision log wired in** — `node.md` logs a contested severity **then** asks the owner. §6 names the log as **inadmissible** for the owner's words. | Does anything now treat a log entry as authority? |
| 5 | **§5 element (i) CHANGED from a verbatim prompt copy to path+sha256.** See §5 below — **this one is a judgement call and the author wants it attacked.** | |
| 6 | **12 polarity-bearing probes + 8 negation mutants + `extract_records.py` termination guard + duplicate probe IDs fixed.** | |

## 4. CARRIED FORWARD — findings from the last gate that are STILL OPEN

**These were filed by O, P and Q and have NOT been repaired.** They are listed so you do not spend your
budget rediscovering them. **Confirm, refute, or re-rank them — and hunt for what they missed.**

| Finding | Status |
|---|---|
| **O-BLOCKER-2** — `combiner.md`'s *"DISCARD NOTHING"* inverts the owner's original `Combine` rule (*"the odd element is discarded"*, record 1044), and **there is no provenance ledger anywhere for divergences from the design spec** — only for guarded-change. | **Partly overtaken**: the owner's 2026-07-29 generalization settles `Union`'s content. **The missing ledger is NOT fixed.** |
| **P-2** — 8 of 12 declared-duplication register entries have no `sites` key, so they are global amnesties. P injected a false closed-set element into two role files and the oracle reported clean. | **NOT fixed.** |
| **P-3** — the register exists in two copies that disagree (`charter.md`'s table vs the JSONL). | **NOT fixed.** |
| **P-4** — N-10's *"stated in no other file"* collides with N-11/N-12; the artifact states the prohibition at three sites. | **NOT fixed.** |
| **O-MAJOR-5** — the *"return value"* universal remedy channel reaches nobody for the **leaf** (its return goes to `Consensus`, which discards the odd plan), the **divider** (returns `pair`/`null`, no field for a complaint), and `Consensus`. | **NOT fixed.** Behaviourally reinforced since — see §5. |
| **O-MAJOR-9** — the orchestrator has operative duties in every dispatched prompt and no prompt of its own. | **NOT fixed.** |
| **O-MAJOR-10** — the divider's self-review loop is unbounded, with no cap, no `Ask_human`, and no return field for a complaint. | **NOT fixed.** |
| **O-MAJOR-11** — guarded-change's SEV4 iteration cap was dropped silently while SEV3 was imported from the same file. | **NOT fixed.** |
| **The node/floor contradiction** (O-MAJOR-6 / P-6 / author's own finding) | **Believed fixed** — §2 now names who holds a floor. **Verify**, and check `Spawn_node`'s signature yourself. |

## 5. THREE THINGS THE AUTHOR IS PUTTING TO YOU DIRECTLY

These are the author's own judgement calls. **Each is more likely to be wrong than the rest of the
artifact, and none has been independently checked.**

> **Q-A. The §5 record rule was CHANGED on the strength of three agents' behaviour. Was that legitimate?**
>
> The fork source (B15) requires a record to embed *"the verbatim prompt you were given."* The author ran
> three cold agents on composed prompts (`records/reviewer-SMOKE-*`, `8-harness.md` §F1/F2) and **two of
> three declined to paste the prompt back**, substituting its sha256 — *"not retyped here to avoid
> transcription drift."* The author concluded the rule as written **invalidates good work** (by its own
> *"missing any of these ⇒ un-run"* clause) and that the agents' substitute is **stronger** than
> compliance, and changed §5 to require **path + sha256**, with verbatim text only for prompt parts having
> no durable file.
>
> **Attack the reasoning, not just the wording.** Is `n=3` on one task enough to change a fork-source
> rule? Does the new form lose anything the old one caught? Is *"the agents didn't comply, so the rule is
> wrong"* a legitimate inference, or is it the author rewriting a rule to match observed behaviour — the
> goalpost-moving failure this loop exists to prevent? The CHANGE is declared in `charter.md`'s provenance;
> **check that the declaration is honest about what was traded away.**

> **Q-B. The `ruleplace.sh` rebuild count is 2 — or 4, and the author chose 2.**
>
> The owner's testing rule: *"If testing it requires more than three iterations of the test mechanism,
> reconsider if it should be tested in isolation or on a test run of the assembled thing."* **The count
> decides whether the structural checker is under or over threshold.**
>
> `ruleplace.sh`'s ancestry includes **two attempt-1 checkers that were bare `exit 0` printers**. The
> author excluded them on the grounds that they tested a **different component** — the 237-line monolith,
> since demolished — giving **2**. Counting the whole project's history gives **4, over threshold**, which
> would force a venue reconsideration for the element's primary oracle.
>
> **Rule on it.** The convention is declared in `9-test-venue.md`; the author flagged it as the most
> contestable judgement there. Is excluding the printers self-serving?

> **Q-C. Is `9-test-venue.md` a faithful application of the owner's testing rule, or a rationalization?**
>
> Read it against the owner's words in §2. Check specifically: **N-14 moved to the assembled run at 3
> rebuilds** — is that the rule's "reconsider", or a cut wearing a new name? **`mutation-test.sh` frozen
> at 3** — legitimate, or a way to stop having to fix it? **N-03's oracle changed from script to cold
> reviewer** — is that isolation testing, or is it giving up and calling it something else?

## 6. THE HARNESS — re-run it; do not take the numbers on trust

```
cd Architect/changes/charter-2026-07
./oracles/ruleplace.sh    ../../stages
./oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl
./oracles/mutation-test.sh ../../stages          # slow, several minutes
```

Author reports **123 passed / 0 failed**, **0 undeclared shared spans**, **125 mutants as expected / 0
unexpected**. Known and self-declared limits, each of which you should test rather than accept:

- **`rules.tsv` is author-written.** It proves the rules it names sit in the files it names; **it is not
  evidence the criteria are covered.** Find a gating criterion with no probe — the last round found four.
- **N-03 barely discriminates**: reviewer Q showed **9 of 19 rules also pass against files they were never
  claimed to be in**, and `mutation-test.sh` has **zero** N-03 mutants. The author **retired the script as
  the fidelity oracle** rather than attempting a third version. Is that the right call?
- **`shared_spans.py` cannot see a paraphrase.** Four live ones were found by hand last round. Find more.
- **Negation**: O inverted four rules and the suite passed unchanged. The author's diagnosis is that those
  rules **had no probe at all** (coverage, not sensitivity) and added twelve polarity-bearing probes.
  **Test the diagnosis** — invert a rule that DOES have a probe and see what happens.

## 7. YOUR DUTIES

- **Cite or it doesn't count** — `file:line`, a quoted span, or a concrete failure scenario.
- **Every finding carries a severity**: `blocker` | `major` | `minor` | `nitpick`. Unsevered ⇒ not filed.
- **Do not self-censor a lone observation.** Findings are unioned, never voted on.
- **Flag the unverifiable.** Report what you could not check as unchecked, never as accepted.
- **"No issue found" is valid** where you show what you checked.
- **Report the path and sha256 of every file you read**, plus your agent type and model. (Per the changed
  §5 — you need not paste this prompt back; its path and hash suffice.)
- **State plainly which of Q-A / Q-B / Q-C you actually ran** and which you did not.
- **Supplementary context**: everything in §§1–6 is **author-authored supplementary context**, because the
  run config's `redteam_context` names only some of these paths and was deliberately not amended mid-run.
  Quote that fact in your record.

**Return a verdict:** `BLOCKER` / `MAJOR` / `MINOR` / `CLEAN`, with every finding severity-ranked.
