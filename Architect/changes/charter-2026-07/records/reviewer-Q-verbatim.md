# Reviewer Q — VERBATIM final message

**Extracted from the harness transcript, not re-typed.** Everything below the rule is the
agent's own final message, byte for byte.

| Field | Value | Source |
|---|---|---|
| agentId | `ae53a70b86e824e87` | harness |
| agentType | `general-purpose` | `agent-ae53a70b86e824e87.meta.json` |
| model | `sonnet` | `agent-ae53a70b86e824e87.meta.json` |
| parentAgentId | `a9b39b3c731d2c23a` | `agent-ae53a70b86e824e87.meta.json` |
| spawnDepth | `2` | `agent-ae53a70b86e824e87.meta.json` |
| transcript | `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775/subagents/agent-ae53a70b86e824e87.jsonl` | harness |
| chars | 25138 | measured |

**These identity fields are FIRST-HAND** — read from the harness's own sidecar, not from
anything the reviewer said about itself.

---

# Reviewer Q — Final Cold Red-Team Record

**Agent type:** general-purpose (Claude Code subagent, dispatched via the `Agent` tool)
**Model:** Claude Sonnet 5 (`claude-sonnet-5`)

## What I ran

- **Q1 (decomposition fidelity):** RUN. Derived the decomposition from `~/Documents/Architect.md` and the owner's re-scope instruction (transcript line 1977 + "Go for it" at line 1994) *before* reading `charter.md`'s own justification, then compared.
- **Fork fidelity B01–B19, both directions:** RUN, in full — read the fork source, the baseline's rule inventory, and cross-checked every claimed destination against the actual file content, plus ran adversarial tests against wrong destinations.
- **Q2 (FRZ-2 self-certification audit):** RUN.
- **Q3 (harness attack):** RUN, including re-executing all three oracle scripts and constructing my own adversarial tests of the N-03 probe (not just accepting the prompt's B15 hint).
- **Declared-duplication register audit:** RUN.
- **Owner-quote spot-checks:** RUN for records 1274, 1572, 1829, 1762, 1449, 1175, 1258, and the re-scope instruction (1977) + "Go for it" (1994) — all verified against the transcript JSONL directly, all confirmed accurate as quoted (see hash of the transcript file below).
- **NOT run:** exhaustive manual re-derivation of every one of the ~90 individual `rules.tsv` probes by hand (I verified the mechanism and spot-checked representative ones instead, which I judge stronger evidence than eyeballing); I did not dispatch the "composed-prompt smoke test" the author describes as "SPECIFIED, NOT RUN" — it doesn't exist, so there was nothing to run.

**Supplementary context, as required by §7:** the run config's `redteam_context` names only some of the paths I was handed. Everything in the prompt's §2 and §4 (the file table, `0-baseline.md`, `1.5-criteria-v2.md`) was supplementary author-authored context handed to me because the config was deliberately not amended mid-run. I quote this per the prompt's own instruction.

---

## VERDICT: BLOCKER

---

## Files read, with sha256 (all computed by me, independently, via `sha256sum`)

| File | sha256 | Matches prompt's declared value? |
|---|---|---|
| `Architect/stages/charter.md` | `0985217fc0381445721bf70d45fe90d1855cee958f6d25336b890aa12e9545ea` | YES |
| `Architect/stages/charter-common.md` | `2b37af1ccdad6800e63877c6aaad1955e7035757c1b7deaca3e0284e6d272ab7` | YES |
| `Architect/stages/redteam.md` | `0df9bd7d27eab35f3b035e26c5118db59b45a47545675903193d14ed0ff51108` | YES |
| `Architect/stages/redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` | YES |
| `Architect/stages/redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` | YES |
| `Architect/stages/divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` | YES |
| `Architect/stages/combiner.md` | `5ad7575a7bbd164cfc6bf82034ce34ae41ba54b7b53e37173830c26a3e75a1d4` | YES |
| `Architect/stages/leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` | YES |
| `Architect/stages/node.md` | `90386699adc44aee20cb9a4322088ff31191b8f6c17feb54a333d51b8132c0bb` | YES |
| `Guarded_change/stages/charter.md` | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` | matches prompt's §3 fork-source claim |
| `Architect/changes/charter-2026-07/0-baseline.md` | `4872f951c65351d5180f019ca7298ff5ae2c41cd6d43e9d0a9241e10c2e49b4a` | (no declared hash to check against) |
| `Architect/changes/charter-2026-07/1.5-criteria-v2.md` | `fb75fb64e534005409d2dc793b56d25ebba44fc4ed515fe2884ad8994a28a761` | **NO — see BLOCKER-1** |
| `~/Documents/Architect.md` | `87986c3c27b1fca956c923122f6c7325f17aa1993c60bce1c05f71a227f1cacc` | (no declared hash) |
| `Architect/changes/charter-2026-07/oracles/declared-duplications.jsonl` | `2db1c385322239cb13c5b720bfe61aa60efb413f5fe7d849ad979f1f0369978a` | (no declared hash) |
| `Architect/changes/charter-2026-07/oracles/ruleplace.sh` | `26576da079c3642ea5e24405e037252f098f457341d8d5b75acf9f1564788f4f` | (no declared hash) |
| `Architect/changes/charter-2026-07/oracles/shared_spans.py` | `91db7fcd57c2068c1975c160c9863b82ab71f6014199792d1ce12816f94f26b4` | (no declared hash) |
| `Architect/changes/charter-2026-07/oracles/mutation-test.sh` | `40fa3f57087122db1a13bf776e0e76581f19f1da5b88477d82d2763657fcd3c8` | (no declared hash) |
| `Architect/changes/charter-2026-07/oracles/rules.tsv` | `f1476822a10782fbe0b2141c5d8ff6070d04672a095fa0bb69d09029ee84c13c` | (no declared hash) |
| `Architect/changes/charter-2026-07/records/harness-run-2026-07-29.txt` | `3909b7129b01df7587813962b08bbcfbd43eb0b06ea071e5b7829819d63fbd7f` | (no declared hash) |
| `Architect/changes/charter-2026-07/8-harness.md` | `909244fa7d29078b1f0c6d185d73aa84e9ef49a83a115deaa205297e5e5a9e21` | (no declared hash) |
| `Architect/changes/charter-2026-07/records/reviewer-O-verbatim.md` | `00e13ca73948122661e9ebc6d25857721b0bbf9af1c3f85826cdc63493829aa9` | (no declared hash) |
| `Architect/changes/charter-2026-07/records/reviewer-P-verbatim.md` | `067b2a4e38e88bec0a757a6772bcf7dcdcce5af3e8af88f584fd940d8527af52` | (no declared hash) |
| `Architect/changes/charter-2026-07/records/reviewer-Q-verbatim.md` | `50e3345f0dbcbf03004e1b4a738b3cc74a007916915e4007ca4754cc395be9d6` | (no declared hash) |
| `Architect/changes/charter-2026-07/records/stage6d-prompt.md` (this prompt) | `edbe10665f743d740876f41040b4a80ad9ac38b79b463ea0c21bca7dad73225f` | — |
| Owner transcript `45cb99a2-...jsonl` | `53341143da17647463adaa2a80fcc6b89d627b4cb3049eae1c6d08b02d4324a1` | — |

The nine dispatched-set files in §2's table **all matched**. The mismatch is isolated to the accept bar (§4), detailed below.

---

## BLOCKER findings

### B-1 — The accept bar changed after this gate was dispatched, and is uncommitted

`1.5-criteria-v2.md`'s live sha256 is `fb75fb64e534005409d2dc793b56d25ebba44fc4ed515fe2884ad8994a28a761`. The prompt declares `eaff14ac6e44189ea6d6195d138305b83dd243ce9bd4e1671c4a8a3210b0ba5e`. **Neither matches the committed `HEAD` version either** (`git show HEAD:...` → `e08e93eb29e0107af6e1ce3ef890940aeae50a055ea18c403598b2d45089aaa8`) — three distinct hashes for the same "frozen" file. `git status` shows the file `M`odified against `HEAD`, uncommitted, mtime `12:40:05`, three and a half minutes *after* the prompt itself was written (`12:36:30`). `git diff HEAD` shows the FRZ-2 block, the N-06/N-10/N-11 amendments, and N-21…N-26 were all added in this uncommitted delta — i.e. **the exact material Q2 asks me to audit was written after the prompt that asked me to audit it, and is not the version anyone else can reproducibly re-read.** `git status` additionally shows six of the nine stage files, plus `8-harness.md`, `decisions.md`, `oracles/mutation-test.sh`, `oracles/ruleplace.sh`, and `oracles/rules.tsv` all dirty against `HEAD`, alongside several untracked new files (`declared-duplications.jsonl`, `extract_records.py`, `shared_spans.py`, `redteam-plan.md`, `redteam-split.md`). The nine stage-file hashes I independently verified happen to match the prompt's table, so that specific freeze held — but the run as a whole is being conducted from an uncommitted, actively-edited working tree, and the one file this gate is specifically asked to audit for self-certification risk is the one whose hash doesn't even match the prompt that names it.

### B-2 — The cold-reviewer verbatim record pipeline captured mid-task fragments, not final verdicts, and I can prove it for my own record

`records/reviewer-Q-verbatim.md` (this run's own extraction target for me) contains, as its "VERBATIM final message… byte for byte":

> *"Matches the sha256 claimed in charter.md's provenance blockquote. Now let's read the baseline file that assigns B01–B19 IDs."*

That sentence is not my final message — it is a line I wrote several tool-calls into this very review, mid-task, before I had read `charter-common.md`, before I had read any of the six role files, and long before this final message existed. This is a first-hand, self-verifiable fact: I did not write that as a verdict, and the file claims I did, "extracted from the harness transcript, not re-typed." The same pattern holds for the other two reviewers dispatched this pass:

- `reviewer-O-verbatim.md`: *"Harness reproduces the author's 92/0. Now the other two oracles and the N-03 threshold logic."* (93 chars, mid-task)
- `reviewer-P-verbatim.md`: *"The no-arg exit code needs re-measuring (my pipe masked it), and the exemption file shows a rule-level duplication. Let me check both."* (134 chars, mid-task)

All three files were written by `extract_records.py` (untracked, mtime `12:41:21`) at essentially the same instant, for all three reviewers, while none of the three had plausibly finished. **The extraction pipeline that this project's own instruments rely on to produce a durable first-hand record of a cold reviewer's verdict is instead recording torn-out scratch fragments.** Any later stage (a gate-8 merge, an orchestrator summary, a future audit citing "reviewer Q found X") that trusts these three files as ground truth is citing fabricated non-verdicts. This is not a hypothetical — it is directly, mechanically verifiable by anyone who diffs the file against my actual transcript, and I am reporting it because I am the one participant who can verify it about themselves with certainty.

### B-3 — N-03, the probe carrying this entire gate's priority-1 obligation, has demonstrably near-zero discriminative power

The prompt asks specifically whether the 60% threshold is real measurement or a number tuned to stop failures, and points at B15 (2/3 = 66.7%). I went further and tested whether the *same* word list that passes a rule's *claimed, correct* destination also passes *wrong* destinations. Method: `oracles/ruleplace.sh`'s N-03 probe derives its "description terms" from `charter.md`'s own allocation-table cell for each B-rule (words >3 chars), then greps each word (bare substring match, case-insensitive) against the claimed file, requiring ≥60% hit rate. I ran the identical word lists against **all nine files**, not just the claimed one:

```
B09 "rank every finding" — ALL EIGHT files score ≥60% (charter-common.md, redteam.md,
    redteam-plan.md, redteam-split.md, divider.md, combiner.md, leaf.md, node.md — every one PASSES)
B01 "cold independent source access" — passes charter-common.md (correct) AND redteam.md,
    combiner.md (both WRONG, 75% each)
B14 "spot verify the citations" — passes combiner.md (correct, 100%) AND redteam.md
    (WRONG, 100%); charter-common.md also passes at 66% though not the sole claimed destination
B08 "cite doesnt count" — passes charter-common.md (correct) AND redteam.md, combiner.md (WRONG)
B15 "provenance record closed set" — passes charter-common.md (correct, 2/3) AND ALSO redteam.md,
    combiner.md, node.md (all WRONG, also 2/3)
```

This is not a coincidental near-miss confined to B15. For a majority of the rules I sampled, the probe would have returned the identical PASS verdict had `charter.md`'s allocation table named the *wrong* file. The reason is structural, not incidental: all nine files share one design's vocabulary (task, plan, floor, closed set, finding, severity, role…), so a 2-4-word description drawn from any rule's own summary is close to guaranteed to appear somewhere in most of the other eight files regardless of whether the underlying rule actually lives there. **This directly falsifies the harness's own comment** at `oracles/ruleplace.sh:95-98`, which claims the word-overlap approach is an improvement over "destination file is non-empty" — my experiment shows it is barely distinguishable from that in practice.

Compounding this: I grepped `oracles/mutation-test.sh` for `N-03` — **zero hits**. The mutation self-test exercises N-02, N-05, N-09, N-10, N-11, N-12, N-13, N-17, N-18, N-19, N-21…N-24, and the duplication (N-26) mutants, but **never generates a relocation or insertion mutant for N-03 itself** — the one check this gate names as priority 1 is the one check the harness's own self-validation never touches. The "87/87 mutants as expected" figure (which I reproduced — see below) provides zero evidence about N-03's soundness.

I did also reproduce the reported harness numbers exactly, for the record: `ruleplace.sh` → **92 passed, 0 failed** (reproduced verbatim); `shared_spans.py ... --exempt-file declared-duplications.jsonl` → **0 undeclared shared spans** (reproduced); `mutation-test.sh` → **87 mutants behaving as expected, 0 unexpected** (reproduced). The numbers are real and not fabricated — the finding is that one of the three instruments producing them (N-03) is not measuring what it claims to.

---

## MAJOR findings

### M-1 — A paraphrased composition-rule violation exists and is invisible to `shared_spans.py` (Q3, bullet 3)

`charter-common.md` §3: *"A silent unilateral demotion is a violation… **No role may quietly lower one.**"* (line 91) — stated as binding every role.

`combiner.md`, under `Severity`: *"You filter. You do not re-rank. **You do not raise a severity, you do not lower one**, and you do not drop a finding because you doubt it… If a severity looks wrong to you, that is a severity to contest through the channel the node holds, not to correct in passing."* (lines 97-100)

This is a paraphrase of the same prohibition FRZ-2's own note says explicitly *"binds every role and stays common"* — yet it is restated, in different words, in a role file. I ran `shared_spans.py` at n=7 over the live set; it reports 0 undeclared spans, and this pair does not appear even among the *exempted* spans, confirming the exact-word-span matcher cannot see it (the wording differs too much for a 7-word run to match). This is exactly the defect class GATE-B2 says it fixed (~8 undetected composition-rule violations); the fix's own instrument cannot see this one because it is phrased differently, not because it doesn't exist.

### M-2 — `Severity` is dispatched as a full cold agent despite the spec conspicuously not marking it one (Q1)

`~/Documents/Architect.md` tags `Divisible` (L14), `Consensus` (L22), `Union` (L24), and `Spawn_redteam` (L28) `// cold agent`. `Severity` (L26) carries no such tag and is described only as a filter: *"returns only the blocker|major issues... This is what makes the while() terminate."* `combiner.md` nonetheless frames Severity identically to Consensus/Union: *"Three separate cold roles… You were spawned as exactly one of them."* This burns a full cold-agent dispatch (its own composed prompt, agent type, model, closed set, provenance record) on what the spec frames as mechanical filtering, and I derived this concern independently before reading the artifact (my own Q1 decomposition flagged the same asymmetry). Neither `charter.md`'s manifest nor the FRZ-2 additions (N-21…N-26) address it, despite the review prompt naming it explicitly. I could not find anywhere in the nine files a justification for promoting Severity to agent status; it may be right (a filter still needs *some* executor and "the node does it inline" was never specified either), but it is undefended and untested.

### M-3 — `redteam.md` textually contradicts `charter-common.md` §0, inside every single composed reviewer prompt this element ships

`charter-common.md` §0: *"A conditional section is present only when its trigger has already been judged to fire. If you are holding one, you do not re-litigate whether it applies."* … *"If your role file appears to contradict this file, that is a defect in the prompt set — say so in your return value, before anything else."*

`redteam.md` (lines 121-126): *"That guarantee does not yet hold for these two [conditional lenses]... So the trigger test below is yours to apply."*

By the composition rule's own terms, this is a defect requiring self-report on every single dispatch of both reviewer kinds — not a hypothetical edge case but a standing feature of every composed prompt this set currently produces. `charter.md` acknowledges the underlying gap ("DECLARED GAP," attributed to the not-yet-built router, OOS-14) but frames it as a future mechanism's absence, not as the live, self-flagged internal contradiction it actually is inside the shipped artifact today.

### M-4 — `node.md` never operationalizes "get stuck," though it is node's own responsibility and the prompt names this by name (Q1)

`node.md` line 59: *"Wait for every agent you spawned to return **or get stuck** before you merge."* This restates the spec's `wait()` comment verbatim without ever defining what "stuck" means, how a node detects it, or what a node does differently for a stuck child (proceed with fewer plans? retry? escalate via `Ask_human`?). This is squarely node's job — it's the role executing this exact `wait()` three times in the loop — and I found no resolution anywhere in the nine files or in `charter.md`'s manifest, and no OOS declaration naming it as intentionally deferred.

### M-5 — GATE-B1's "return unmerged with a note" fix hands the plan reviewer an artifact its own closed-set language doesn't anticipate

`redteam-plan.md`: *"Exactly one thing beyond the common list: **the plan**."* (singular). On the two-child path, `combiner.md`'s GATE-B1 repair may now hand the reviewer two unmerged plans plus an explanatory note instead. Nothing in `redteam-plan.md` acknowledges this shape or instructs the reviewer that an unmerged pair is itself at minimum a finding — the design relies on the reviewer noticing this via its general lenses. Plausible, but unverified, and the prompt raises this exact question by name ("does it corrupt the loop?").

### M-6 — Four gating criteria have no probe anywhere, and are absent from the run's own disclosure table

`1.5-criteria-v2.md` marks **N-15** (its N-15a half), **N-20**, **N-25**, and **N-26** as gating. I grepped every oracle script and `8-harness.md` for each ID: **zero hits for N-15, N-20, N-25, N-26.** N-20 ("no dogfood-derived content") I hand-verified would substantively pass (grepped the nine files for "dogfood"/"differential-prompt"/"FINDINGS.md" — no hits) — but the harness never says so; it is simply never counted, positive or negative, inside the "92 passed" figure. N-26's underlying check (`shared_spans.py`) genuinely runs and does what N-26 describes, but nothing traces the ID to the run in `8-harness.md`. Critically, the document's own honesty mechanism — the *"What ships UNVERIFIED, stated plainly"* table (after line 180) — lists N-05, N-06, N-09, N-13, N-14 as text-only/unverified, but **does not mention N-15, N-20, N-25, or N-26 at all**, and (per B-3 above) does not mention N-03 either. A reader trusting that table's completeness would materially undercount what's actually unverified.

---

## MINOR findings

### m-1 — B01's scope was silently broadened without being declared a CHANGE

`charter-common.md` §1 states "cold, independent… no shared reasoning context with your siblings" for **every role**, where the fork source's B01 was reviewer-specific. This is a defensible generalization given Architect's whole-system "cold agent" design, but `charter.md`'s CARRIED list doesn't name it as a change, unlike other, smaller reinterpretations it does call out (e.g. B01 is just listed under CARRIED alongside verbatim items).

### m-2 — The declared-duplication register is broader than `charter.md` tells a reader it is, and the prompt's own count of it is wrong

`oracles/declared-duplications.jsonl` has **10** `"class": "scaffolding"` entries (mechanically counted: `grep -c`), not 7 as this review prompt states (§6, bullet 3) — and this discrepancy predates the prompt (the file's mtime, 12:27, is before the prompt's, 12:36:30, so this isn't a moving-target artifact; the prompt's count is simply wrong). Independent of that miscount: `charter.md` lines 146-148 tells a reader the register exempts exactly **two** categories ("the role-file composition banner, and the opening stem of each role's … section"), but the live register in fact exempts at least eight distinct spans beyond those two (the aiming-file banner, the floor-heading string, the "What you do not do" heading, the review-context-paths clause, the stem's closing clause, "two sub-tasks and the stated seam," and a cross-reference phrase). Most of these read as defensible structure on individual inspection, but one — *"plus the review-context paths named in the run's configuration"* (line 10) — states *what a role holds*, which is substantive content (part of the B15/closed-set discipline), not obviously "structure" under either of `charter.md`'s two named categories. A reader relying on `charter.md`'s own prose account of the register — rather than opening the JSONL — would materially undercount what it actually exempts. This is the closest concrete answer I have to "is it a principled list or where inconvenient duplications went": on the numbers, the register has grown well past what the human-readable manifest documents, and at least one entry sits at the boundary the manifest's own two-category definition doesn't clearly cover.

---

## Q1 — my derived decomposition vs. the shipped one

Derived independently, before opening `charter.md`, from `~/Documents/Architect.md`'s function signatures (`Spawn_leaf`→leaf, `Spawn_node`→node, `Spawn_redteam`→reviewer with two distinct invocation contexts, `Divisible`→divider with a self-red-team of the split, `Consensus`/`Union`/`Severity`→ one owner-named "combiner" bucket) plus the owner's "i.e." enumeration (which I treated as illustrative, not exhaustive, per the prompt's own instruction): **six roles, matching what shipped** (leaf, node, plan-reviewer, split-reviewer, divider, combiner). I independently concluded the reviewer 3-way split (`redteam.md` + two aiming files) is justified rather than tier-growth-for-its-own-sake, because the two closed sets are genuinely different (plan vs. division, and the split reviewer is explicitly "entitled to no plan") — this matches what shipped and I found no defect in the split itself, only in what the split's shared core (`redteam.md`) says about a mechanism that doesn't exist (M-3 above).

Where my derivation and the shipped set diverge in substance rather than form: **Severity's agent-status (M-2)** and **the undefined "stuck" state (M-4)** are real, unresolved gaps I identified before reading the artifact's own reasoning and found unaddressed after reading it. The root-bootstrap `Node(...,0,"0")` question and who sets `granularity`/`gate_depth`/queue capacity I judge **legitimately out of scope** for an agent-prompt-set element (these are Layer-2/run-config concerns per the spec's own framing, "Set once per run (Layer-2)") — `charter.md` doesn't explicitly declare this OOS, but I don't think it needs to; I flag this only as a nitpick-level transparency gap, not a finding.

---

## Q2 — the FRZ-2 amendment

Read on its own terms (independent of B-1's hash problem): the diagnosis is sound and the fix follows the set's own stated diagnostic consistently. N-10/N-11 were genuinely contradictory (N-10 said the severity model lives "in no other file," N-11 required `node.md` to restate a sentence of it) — this is a real incoherence, not a manufactured one, and I verified it by reading the *original* N-11 wording still preserved in the document (superseded, not deleted) against N-10's actual text. The repair — the *prohibition* stays common (bound to every role, so it belongs in `charter-common.md`), the *permission to contest* moves to `node.md` (only node holds `node_id`/`depth`) — applies the composition rule's own "which roles can act on this" diagnostic correctly and I could not find a self-serving deviation in it. N-21…N-26 are reasonably scoped repairs of gate-7's actual named blockers, not scope-inflation. My reservation about Q2 is entirely procedural, not substantive: **this amendment is the exact content whose hash doesn't match what I was told to expect (B-1)**, so while I judge the amendment itself principled, I cannot certify that what I read is the version that will actually ship, or the version any other reviewer read.

---

## Summary

Three blockers: an accept bar that changed after dispatch and matches neither the prompt nor `HEAD`; a verbatim-record extraction pipeline caught red-handed writing mid-task fragments as "final messages" (provable first-hand for my own record); and the fork-fidelity probe carrying this gate's stated priority-1 obligation shown, by direct adversarial testing, to pass rules against files they were never claimed to be in. Six major findings span an undetected paraphrased composition-rule violation, an unresolved Severity-as-agent question, a self-flagged-but-unresolved prompt-internal contradiction, an undefined failure mode in node's own loop, an unverified robustness question in the GATE-B1 repair, and four gating criteria with no probe and no disclosure. Two minor findings concern under-declared scope broadening and a declared-duplication register that is materially wider than its own manifest's prose says it is.