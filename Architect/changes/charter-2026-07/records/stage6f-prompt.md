# Gate 7, pass 4 — TARGETED cold red-team (2026-07-29)

You are a **cold, independent reviewer**, no shared context with this artifact's author or with the two
reviewers dispatched alongside you. **Nothing here is true because it is written here** — every claim is
the author's, including the author's account of what it repaired and of what earlier reviewers found.

Repo root: `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

**This round is TARGETED.** Three full rounds have already run (records `reviewer-{A..T}-verbatim.md`).
Your scope is **(1)** the repairs made since pass 3 and **(2)** the pass-3 findings the author chose not to
repair. **You are not asked to re-derive the whole artifact — but you are not forbidden from filing
anything you find.**

---

## 1. THE ARTIFACT — verify every hash. If one differs, say so and stop.

`Architect/stages/`, nine files, 1,138 lines.

| File | sha256 |
|---|---|
| `charter.md` (manifest, **not dispatched**) | `223edfd732e47c3406a8031dace6e3b4c358fe298cf1231f413837fe10532020` |
| `charter-common.md` (verbatim to every role) | `49cce9a462561def83e0c6ccaab14c2f2089bd1783461ce8f694b93a78591756` |
| `redteam.md` | `c28fcbcf634ee5b781872a6da8776ccddb162ff1c1346750fbc303d02102b838` |
| `redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` |
| `redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` |
| `divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` |
| `combiner.md` | `105ae484f918231c27ca7ab82e305b7f4d631b7593a9d6f7093c3cd166356828` |
| `leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` |
| `node.md` | `6dd47d449efda4e5396f1d66eb6f916fe335996cf29168ce843f0d74202a88cb` |

A dispatched prompt is `charter-common.md` **verbatim** + role file(s). **Review the composed prompt.**

## 2. AUTHORITY — and a standing warning

1. **The owner's words**, at their record index in
   `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`.
   **The only admissible source.** ⚠ **Read the WHOLE record around any quote.** Twice in this run a quote
   presented as a ruling turned out to be part of a longer message whose omitted part mattered.
   Loci: **1274**, **1572**, **1762**, **1829**, **1449** (items 1 and 2), **1977**/**1994**,
   **2524 item 2** (node merge, *hedged*), **2524 item 3** (decision log), **2544** (testing rule),
   **2680** (`Union` generalized).
2. **`~/Documents/Architect.md`** — 131 lines, sha256
   `8ad9d620be794047b3606e948e20d3cd70b5413c36b9dd19f0dc97d8d107a474`. ⚠ **Owner-SEEDED, not
   owner-written** — the owner's original is 59 lines (record **1044**); **every function signature in the
   file is agent-written.** *"The spec says X"* is not *"the owner said X."*
3. `Guarded_change/stages/charter.md` (fork source) · `changes/charter-2026-07/0-baseline.md` (B01–B19).

## 3. SCOPE A — the repairs. Each closed a pass-3 blocker; check whether it closed the CLASS.

| # | Repair | The specific thing to attack |
|---|---|---|
| 1 | **§0 rewritten to sever the non-termination path.** A prompt-set defect is now reported **out of band**, never carries a severity, never counts as `blocker\|major`. Stated as a class. | R showed the previous fix was written to one *shape* and the mechanism fired from another. **Is the class fix actually closed, or is there a third route into the findings stream?** Does "out of band" have a real destination for every role? |
| 2 | **§2 floor rewritten to three cases** — bound / **carrier** (node) / given none, decided **by signature alone**. `node.md` gains a carrier section requiring any branch override to be logged. | R and S ruled this a live blocker; T ruled it fixed. **Rule for yourself.** Check `Spawn_node`'s signature. Is "carrier" a real category or a relabelling that dissolves the contradiction verbally? |
| 3 | **`combiner.md`'s ordering rule made input-agnostic** — it keys on *what the caller supplied* (a seam), not on input type. | T held the file *"cannot be executed consistently as written."* **Can it now?** Is "a seam is handed to you, not a property of the input" a real distinction or a restatement of the same branch? |
| 4 | **`node.md` de-attributed** — the owner-ruling sentence stops at *"`Union` keeps both"* and carries the **hedge**. | T found the author's own decision cited as the owner's. **Is anything else in the set attributed to the owner that isn't his?** |
| 5 | **N-03's retirement PERFORMED** — those probes now print `SMOKE`, and their 21 results are **removed from the gating count** (headline dropped 134 → 122). | S found it declared but not done. **Is it done now?** Does anything still describe it as fidelity verification? |
| 6 | **IN-PLACE NEGATION relabel.** S's append attack is reproduced in the file header; the class is **not extended**; semantic inversion is declared a **cold-reviewer** oracle. | **Is declaring it a cold-reviewer oracle a real venue decision or an excuse not to fix it?** |
| 7 | **Nine probes added for N-15a / N-20 / N-25**, which were gating with **zero** coverage. | Verified by reproducing T's injection (0 probes fired before, 5 now). **Find another gating criterion with no probe.** |
| 8 | **Liveness pin replaced** — `charter.md` pins the spec by **six claims each with its `grep`**, hash demoted to *"observed, not a freeze"*. | **Do the six checks actually cover what the set relies on?** Name something it relies on that no row covers. |

## 4. SCOPE B — the ten pass-3 findings the author did NOT repair

**Each is open by choice.** Confirm, refute, or re-rank — and say whether leaving it is defensible given
that **elements 2–6 do not exist yet and will inherit it.**

| Finding | Author's stated reason for not repairing |
|---|---|
| **O-BLOCKER-2** — no provenance ledger for divergences from the design spec (only for guarded-change) | Not addressed. The `Union` content question was settled by the owner; **the missing ledger was not.** |
| **P-2** — 8 of 12 register entries have no `sites` key, so they are global amnesties. P injected a false closed-set element into two role files and the oracle reported clean | Not addressed |
| **P-3** — the register exists in two copies that disagree (`charter.md`'s table vs the JSONL) | Not addressed |
| **P-4 / S-08** — N-10's *"stated in no other file"* is gating, collides with N-11/N-12, and is untested against six of seven files | Not addressed |
| **O-MAJOR-5, as S re-ranked it** — the *"return value"* remedy is an **affirmative falsehood** for leaf (its return goes to `Consensus`, which discards the odd plan), divider (`pair`/`null`, no field), and `Consensus` | Not addressed — **and repair #1 above now routes prompt-set defects through that same channel.** Attack that interaction. |
| **S-13** — `Ask_human` is described to all six roles in the common core and callable by **one**; the five that cannot call it are never told | Not addressed |
| **O-MAJOR-9** — the orchestrator has operative duties in every dispatched prompt and **no prompt of its own** | Assigned to element 4 |
| **O-MAJOR-10** — the divider's self-review loop is unbounded: no cap, no `Ask_human`, no return field, and it sits **below** `Human_gate` | Not addressed |
| **O-MAJOR-11** — SEV4's iteration cap dropped silently while SEV3 was imported from the same file | Not addressed |
| **S-14 / S-15 / S-16** — *"No rule is in a silent third category"* is a false claim given the SEV4 drop; the register exempts the exact string §2's floor test turns on; the manifest's register is 1 row against the JSONL's 12 | Not addressed |

## 5. THREE AUTHOR JUDGEMENTS PUT TO YOU DIRECTLY

> **Q-A. The closed-set citation rule.** `charter-common.md` §5 now says *nothing in your prompt may
> require you to open a source outside your closed set*, that a citation to something you were not given is
> **"provenance for a later auditor, not an instruction to you"**, and that a genuinely missing source is a
> **config defect — "do not go looking."**
>
> This was written because two of six roles were observed leaving their closed set in real dispatches (one
> searched the filesystem; one opened the design spec to check a citation **the author's own repair had put
> in its role file**). **Attack it:** is *"provenance, not instruction"* a distinction an agent can actually
> act on, or a licence to cite anything and disclaim responsibility for it? Does *"do not go looking"*
> leave a role unable to do its job with no way out? Should spec access instead be **added** to every
> closed set — and what would that cost?

> **Q-B. The author's argument for stopping full review rounds is an ADMITTED EXTENSION of owner record
> 2544, and the author wrote the counter-argument itself.** Read `decisions.md`'s entry *"AN EXTENSION OF
> THE OWNER'S RULE THAT IS MINE, NOT HIS"*. It concedes 2544 is about **test mechanisms**, not review
> rounds, and that **three rounds each returning novel blockers is evidence the gate is NOT saturated** —
> which argues for continuing. It then rests on narrower ground: the owner's **size** bound from the same
> record, and the claim that most remaining findings **belong to elements that do not exist yet**.
> **Rule on it.** Is the narrower ground sound, or is the author stopping because it benefits from
> stopping?

> **Q-C. Single-model evidence.** All smoke dispatches to date ran on one model. A second-model replication
> of the node arm was dispatched alongside you. **Independent of its result: how much weight can `n=1`
> per role carry, and has the author over-relied on it anywhere?** Specifically, repairs 1, 2 and 3 above
> are claimed *"verified behaviourally"* on the strength of two dispatches.

## 6. THE HARNESS — re-run it, and try to break it

```
cd Architect/changes/charter-2026-07
./oracles/ruleplace.sh    ../../stages        # author: 122 passed / 0 failed, + 21 SMOKE not counted
./oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl   # 0 undeclared
./oracles/mutation-test.sh ../../stages       # slow, several minutes; author: 138 as expected / 0
```

**Known and self-declared holes — test them rather than accept them:** `rules.tsv` is author-written and is
not evidence the criteria are covered; **no substring probe can catch an inversion that APPENDS** (S proved
it; the author declined to build a fifth mechanism); `shared_spans.py` cannot see paraphrases.

## 7. DUTIES

Cite or it doesn't count (`file:line`). Every finding carries `blocker`|`major`|`minor`|`nitpick`; unsevered
⇒ not filed. Do not self-censor a lone observation. Flag the unverifiable as unchecked, never as accepted.
Report the **path and sha256** of every file you read (you need not paste this prompt back — its path and
hash suffice), plus your agent type and model. **State which of Q-A/Q-B/Q-C you ran and which you did not.**
Everything in §§1–6 is **author-authored supplementary context**; quote that fact in your record.

**Return a verdict:** `BLOCKER` / `MAJOR` / `MINOR` / `CLEAN`.
