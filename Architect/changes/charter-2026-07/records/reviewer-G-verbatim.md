# Reviewer G — stage-6 cold review, VERBATIM

**Recovered from the harness-authored subagent transcript**, not re-typed:
`~/.claude/projects/…/subagents/agent-aa4584fe421867261.jsonl` (final assistant message).

**Harness-authored provenance** (`agent-aa4584fe421867261.meta.json`) — first-hand, not reviewer-reported:

| field | value |
|---|---|
| `agentType` | `general-purpose` |
| `description` | `Stage-6 cold review G` |
| `model` | **`opus`** |
| `parentAgentId` | `a415bc52b9d9f3550` |
| `spawnDepth` | `2` |
| `toolUseId` | `toolu_01A3TEMc5Hnh6gxzzpQxBAWz` |

---

## Context files read + sha256

Verified with `sha256sum` in the working directory.

| File | sha256 |
|---|---|
| `Architect/stages/charter.md` (artifact, 215 L) | `523bf3a24b9a1279790473ffb5d5904a74424d9cacf2800f2f657baffc446085` |
| `Architect/changes/charter-2026-07/1.5-criteria.md` | `1df324c0d4d3c971c9a3a56232ebf872c757bfb22d35cc26808ded359918912c` |
| `Architect/changes/charter-2026-07/2-plan.md` | `ed3b274284d5064a0e29d13ad8c34f12e522c16c3e897a6ab4a0845585623a38` |
| `Architect/changes/charter-2026-07/0-baseline.md` | `4872f951c65351d5180f019ca7298ff5ae2c41cd6d43e9d0a9241e10c2e49b4a` |
| `Architect/changes/charter-2026-07/decisions.md` | `61a91fa1c1e5af16d8099328464d32457cb3753af6dbc758840f903b377b8a42` |
| `Architect/changes/charter-2026-07/records/build-diff.txt` | `ff7ff3c66a8da03d1f8d66da12800e0df0ebaf777c7aec990a729b29083f540a` |
| `Architect/changes/charter-2026-07/records/stage6-prompt.md` | `5f7819ae546338130a10eea7887e5ef672189e59f6585fb890a1907d2a9a4358` |
| `Guarded_change/stages/charter.md` (fork source, 103 L) | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` |
| `Dragonfly/stages/charter.md` | `c5d1e2068f35760e373517e243003800c264c64bf3d93d6d8ea6b951990af870` |
| `Architect/guarded-change.architect.md` | `42f289a51ed4e5f706d3b70bc8ca47a2e8dc16d2aba4f3f3ac76a02d0cb0429c` |
| `Guarded_change/stages/stage-3.md` (read L45–89 only) | `16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3` |
| `Guarded_change/stages/stage-4.md` | `175061c27bb6980ff76c6358d403299d343c409b2952308ffea7485fff880675` |
| `/home/zero/Documents/Architect.md` (119 L) | `1d3859546f3faf5a85e7ca7c4be4055c539b80eb86963c4743e481c350cee826` |
| session transcript `45cb99a2-…-0775.jsonl` (1857 lines) | `842967e5032665d407ce0b0f2ea9fcef8873fbbfc5dc39dec41b10df69690105` |

**Banner check:** no `UNVETTED DRAFT` banner. Head block after the title is the provenance blockquote (L6). I am reviewing this run's output on its merits.

**Criteria hash:** the prompt's `a1e6ff0a…` is indeed not the value. The current hash is `1df324c0d4d3c971c9a3a56232ebf872c757bfb22d35cc26808ded359918912c`, which **matches** the FRZ record pasted in `decisions.md` L529. The criteria file is unmodified since freeze.

**Fork-source identity re-verified independently:** `git show 8d73e5d:Guarded_change/stages/charter.md | sha256sum` → `0e73bacf…adc590`, 103 lines. The blockquote's commit + sha claims are true. Dragonfly's precedent blockquote (L8–12) does name a commit and "deliberately not carried" and contains **no** sha256 — C-01's B-F19 attribution correction is accurate.

**Sources used outside the prompt's list:** none, except `git show` on the repo itself (identity verification of the fork source) and `ls`/`grep` over the run folder. Note that `Guarded_change/stages/stage-3.md`, `stage-4.md`, and the run-folder artifacts I was handed are **not** among the config's 8 `redteam_context` paths (`grep -c "^  - path:"` → 8) — see finding **F8**.

---

## Mechanical diff walk — required section

119 insertions / 67 deletions, 8 hunks. Per hunk: what asked for it, and what rode along.

| Hunk | Change | Asked for by | Ride-along? |
|---|---|---|---|
| 1 (L1–23) | `UNVETTED DRAFT` banner deleted | C-16a/C-16b | no |
| 1 | Blockquote rewritten into CARRIED / CHANGED / DELIBERATELY NOT CARRIED | C-01, C-03, C-03b; `2-plan.md` §1.3 | **yes — see F5**: the CHANGED list declares the *closed set* (B15/D3′), not B19, which C-03b's own parenthetical names |
| 2 (L27–43) | floor = "this review… passed to *this* invocation… a branch may have set finer" | C-06a (B-F18) | no |
| 2 | "If you were given no floor, or the floor… is not operable… file *that* as a blocker" | C-06a (A-F12) | no |
| 3 (L45–48) | "**Return a verdict for each.**" added | **no criterion** | yes — but traces to R-6's flagged axis (record 1825: "its own auditable verdict"). Sourced, uncovered. Not filed separately. |
| 4 (L54–59) | lens-5 ratification prose collapsed to "audit it under **RAT1** and **RAT2** below" | C-21, D12 | no |
| 4 (L62) | "the **7 sections**" → "the sections" | C-18a (tier (i) by role, not count) | no |
| 5 (L80–82) | "~85%" statistic deleted; replaced with "the merge step discards nothing…" | C-09b (delete), C-09a (replacement, `Architect.md` L24) | no |
| 5 (L85–86) | "You are graded on **precision** … not on body count" **removed** from the "No issue found" bullet | C-23 / D9 covers the *move to last*, **not the removal from here** | **yes — see F6** |
| 6 (L91–94) | fidelity earned-clean → "show the **RAT1 audit** was done" | C-21 | no |
| 6 (L95–99) | "each of the 7 spine sections" → "each spine section" | C-18a | no |
| 6 (L100–108) | `Union` named as spot-verify consumer; UNSUBSTANTIATED clause; C-08/C-12 carve-out | C-12, C-12b (D11) | **yes on the disposition mechanism — see F3** |
| 6 (L109–116) | "**and you are instructed to report those hashes**"; closed set restated per-caller | C-11 (B15 element (v)), C-11/D3′ | **yes — see F2**, the restatement is unbounded |
| 6 (L117–119) | charter-composition bullet (B19) | C-20, D8 | no |
| 6 (L121–135) | **RAT1** section | C-21 | no |
| 6 (**L136–146**) | **"Spot-verify the owner-quote… `origin.kind` = coordinator/peer…"** | **NO CRITERION.** Grep of the frozen `1.5-criteria.md` and `2-plan.md` for `origin` returns only the unrelated "originally produced" line. Authorised only by `decisions.md` L510–521, written in the same gate entry as the freeze | **YES — F1, the largest un-asked-for addition in the diff (11 lines)** |
| 6 (L148–155) | **RAT2** section | C-21 | no |
| 6 (L157–169) | conditional lenses moved out of the discipline bullets into their own "**included only when the trigger fires**" section | C-13, C-20, D8 | no |
| 7 (L180) | "or is **unverifiable**" added to the blocker cell | C-07 (A-F15); matches `stage-4.md` L19 | no |
| 7 (L185–186) | "**Borderline is a human decision**" added | C-08 (SEV2, `stage-4.md` L26–29) | no |
| 7 (L188–191) | demotion rule rewritten, `Ask_human` named | C-08 (SEV3, `stage-4.md` L31–36) | **partial regression — see F4** |
| 8 (L215) | B18 appended as the final line | C-23, D9 | no |

Remaining hunk content is line-rewrapping with no semantic change (verified by reading each `-`/`+` pair).

---

## Regression check vs B01–B19 — required section

Every rule checked at its site in the shipped charter, against `0-baseline.md` §0.2's cited fork-source lines.

| ID | Intent | Stated in shipped charter | Verdict |
|---|---|---|---|
| B01 | CARRY | L23–26 | ✓ present. `redteam_context` locus dropped ("the underlying source **it makes claims about**") — declared in §0.3 B01 |
| B02 | CHANGE | L47–48 | ✓ separation rationale present; five→six declared in blockquote |
| B03–B06 | CARRY | L50–53 | ✓ |
| B07 | CARRY | L54–59 | ✓ incl. proxy/untrusted, "memory note", OWNER RULING-as-claim; ratification + inflation duties carried into RAT1/RAT2 |
| B08 | CARRY | L75–77 | ✓ plus the plan-shaped example |
| B09 | CHANGE | L77–79 + L171–183 | ✓ table in-file (dangling "(below)" closed); declared |
| B10 | CARRY | L83–84 | ✓ |
| B11 | CARRY | L85–86 | ✓ |
| B12 | CARRY | L87–90 | ✓ |
| B13 | CARRY | L91–94 | ✓ |
| B14 | CARRY | L100–108 | ✓ with named consumer `Union` |
| B15 | CARRY + 1 DROP | L109–116 | ✓ five elements (i)–(v), quote-supplementary rule, missing-any⇒un-run. **Closed set present but operatively defeated — F2.** DROP **declared** at L16–18 ✓ |
| B16 | CARRY | L159–165 | ✓ incl. "not by whether any text was lost" |
| B17 | CARRY | L166–169 | ✓ substance; **ranking clause dropped — F7 (nitpick)** |
| B18 | CARRY + POSITION | L215, terminal | ✓ last content line |
| B19 | CARRY | L117–119 | ✓ all three clauses stated |

**Result: no CARRY rule stopped being stated. The single declared DROP (B15's A/B-harness-arm sub-clause) is named as dropped in the provenance blockquote. No rule fell into a silent third category.** The regression bar is met. Two qualifications, filed as F2 and F7.

---

## Lens 1 — Factual

Claims checked against `Architect.md` (priority 1), the fork source, `stage-3.md`/`stage-4.md`, and the transcript.

**Confirmed correct:**
- L202–204 "When nothing survives the filter, the node is done and its plan is returned. The red-team going quiet *is* the completion condition — there is no separate gate" — `Architect.md` L66 `while(task.empty()==false)`, L110 `task = Severity(Union(...))`, L117–118. ✓
- L205–210 split review inside `Divisible`, "loops until no major issue remains" — L14 verbatim ("red-teams result (looping until no major issues are found)"). ✓ Human gate at depth ≤ `gate_depth` — L16, L83. ✓
- L189–191 "demoting a **blocker or major** additionally requires the **human tie-break** — reached by `Ask_human`, which blocks for the owner from any depth" — `Architect.md` L18 ("BLOCKS for the human owner FROM ANY DEPTH") and L20 ("This is the channel the severity path uses: demoting a blocker|major requires the owner"). ✓
- L100–101 `Union` as the merge step — L24. ✓ L80–82 union-not-majority-vote — L24 "DISCARDS NOTHING… A finding one reviewer caught is signal." ✓
- L30–32 the floor is "the floor passed to *this* invocation, which a branch may have set finer than the run's default" — `Architect.md` L1–3 ("Set once per run (Layer-2), threaded down so a branch can override it"). ✓ Not the proxy "the run's floor".
- L212–213 "3 independent cold agents" = three separately-spawned subagents — record **55 item 6** verbatim: *"An addition to the self test, an adversarial stage where three independent cold agents try to poke holes in the plan"*; `Architect.md` L104–107 spawns 3. ✓ I also verified the criteria's B-F04 correction: record **51** decision #2 option **(b)** is *"a **cold completeness-critic pass**"*, so record 55 item 2's "option be" is indeed a different referent. The correction is accurate.
- L171–183 severity model — matches `stage-4.md` L17–22 including "unverifiable" in the blocker cell (L19). ✓
- L185–186 SEV2 — `stage-4.md` L26–29. ✓
- **L138–146 `origin.kind`** — I verified this against the harness on disk rather than accepting it. `grep -o '"origin":{[^}]*}'` over the transcript returns `{"kind":"coordinator"}` (177 across project transcripts), `{"kind":"peer","from":"general-purpose","senderTaskId":"a6a1a85615ff8a062",…}`, `{"kind":"human"}`, `{"kind":"task-notification"}`. The peer form carries a **real** id (`senderTaskId`) plus an agent-**type** `from` label; a probe agent at that record confirms replying to the type label fails (*"No agent named 'general-purpose' is reachable"*) and that it resolved the id from `…/subagents/agent-a6a1a85615ff8a062.meta.json`. A second probe reports the coordinator message *"carried NO from= label"*. The `origin` object is present in `subagents/agent-*.jsonl`, so a subagent can read it about itself. **Every factual claim in the paragraph is confirmed.** One imprecision: it is presented as a two-value field; `human` and `task-notification` also occur (F9, nitpick).

**Factual defects found:** none in the artifact's claims about the source. The factual problems in this review are coverage/ratification problems (F1, F3), not false claims.

---

## Lens 2 — Logical

**F2 (major) — the closed set is self-nullifying, and the run knows it.** L112–116: *"Reviewer input is a **closed set**: the task you were given, the plan you were given, the granularity floor you were given, **plus whatever review-context paths your caller supplies** … Any supplementary author-authored context must be quoted in the record as such. A record missing any of these = the review is treated as **un-run**."*

The caller of `Spawn_redteam` is the node that authored the plan under review. If *whatever the author supplies* is by definition inside the closed set, then "supplementary author-authored context" has an empty extension — nothing can ever be it, so the quote-as-such obligation and its un-run penalty can never bind. The fork source's version (L74–77) is bounded by lists fixed **outside** the author: "the named stage artifacts + the config's `redteam_context` + the spec's touched-files list + carried-forward findings from `decisions.md`". That boundedness is what gives the rule teeth, and the restatement removes it.

This is not a novel objection: `decisions.md` L264–266 records it as pass-2 finding **D-F04/E-F6**, 2/3, in the list of *"five of nine claimed pass-1 fixes [that] MOVED their defect rather than removing it."* It appears in **no** "Fixes applied" table at any later gate, and C-11 was frozen without addressing it. It ships unclosed and unmentioned in the run's own list of what ships unverified.

**F4 (minor) — the demotion rule loses the one thing that made it executable.** C-08 requires (gating, "ported **verbatim**", per-clause positive assertion, D10 owner-ratified at record 1449 item 2): *"contest a severity **only** via a logged `decisions.md` entry … a silent unilateral demotion is a **gate violation** and the reviewer's **routing** stands."* Source `stage-4.md` L34–36 says exactly that. Shipped L188–191 says *"contested **only** via a logged entry"* and *"the reviewer's **severity** stands."*

Dropping `decisions.md` is defensible (Architect has no such file; C-22 sweeps dangling pointers) — but the result names **no log at all**, and `Architect.md` offers no persistence except `Memo_write` (L37), which is per-node and read only by that node's restart. So the contest half of the rule has no home and cannot be complied with, and the deviation from "ported verbatim" is nowhere declared. Under a literal C-08 per-clause probe, two clauses do not match.

**F5 (minor) — C-03b's third CHANGE declaration is not the one that shipped.** C-03b names three CHANGE-intent rules whose difference must be declared in the blockquote: *"B02 five→six lenses; B09 severity model stated in-file; **B19 restated per-caller**."* The shipped blockquote's CHANGED paragraph declares B02 ✓, B09 ✓, and *"The **closed set** is restated conditionally and per-caller"* — which is **B15/D3′**, not B19. B19 (the charter-composition rule) is listed under **CARRIED** with no difference stated, even though its text was re-aimed from "stage-specific additions" to "your caller's aiming". Either the artifact misses a required declaration, or C-03b mislabels B15 as B19 — and `0-baseline.md` §0.3 gives B19 intent **CARRY**, which contradicts C-03b calling it a CHANGE rule. `2-plan.md` §1.3 agrees with the artifact, so the criteria parenthetical is the odd one out. Flagged either way: a frozen gating criterion and the artifact do not line up.

---

## Lens 3 — Missed opportunity

**No issue found that I would file.** Two observations offered without severity, since neither is a defect:

- The charter is 215 lines and every cold reviewer pays for it on every spawn. `2-plan.md` block 1 explicitly kept the blockquote compact for this reason, then the build added ~50 lines of RAT1/RAT2/`origin.kind` prose after it. C-19 (length, ADVISORY) has this covered as a reported measurement, and D12 accepted the ~30-line cost knowingly, so it is a recorded tradeoff, not an oversight.
- RAT1's `origin.kind` block is written as reviewer instruction but is really harness documentation. If the six planned elements ever gain a shared "how this harness works" doc, it would live better there — but Architect has no such file today (`ls Architect/stages/` = `charter.md` only), so inlining was the only option available, exactly as D12 reasoned for RAT1/RAT2.

---

## Lens 4 — Unstated assumptions & risks

**Position lens — FIRES (as the prompt states), and I judge the text against the plan's claims.**

Placement claims verified as *text*: the floor heading is L28, the first lens is L50, so `floor_line < first_lens_line` ✓ (C-17). B18 is L215 and is the last content line ✓ (C-23). The full 10-block order in `2-plan.md` §1.1 is realised in sequence: provenance (L6) → constitution (L23) → floor (L28) → six lenses (L45) → discipline bullets (L73) → RAT1/RAT2 (L121/L148) → conditional lenses (L157) → severity model (L171) → the two callers (L198) → B18 (L215). **The text does realise the placement claims the plan makes.** Their *effect* is unverified, which is disclosed in `1.5-criteria.md` Part B and `2-plan.md` §1.1 and is not something I re-litigate.

**F6 (minor) — something the build displaced that no criterion covers.** The position rule's own worded trigger is *"any edit — move, reorder, add, or **remove**"*, and *"a removal changes a neighbour's adjacency."* The build did not merely move the precision instruction to the tail; it **deleted its former occurrence** inside the "No issue found per lens is allowed" bullet (diff L106). In the draft those two ideas sat adjacent: *a clean lens is a real all-clear* immediately followed by *you are graded on precision*. That adjacency is the pairing that licenses a reviewer to file nothing. D9 and C-23 assert and check only that B18 is **last**; nothing in the criteria or the plan addresses the removal from L85–86. By the run's own reasoning — that placement has behavioural consequence, which is why D9 exists at all — this is a second, undeclared positional change riding inside a criterion that covers only the first. It ships unverified and, unlike C-17/C-23, unlisted.

**F10 (nitpick) — the conditional lenses' adjacency did survive.** Checked because the trigger includes untouched elements: in the draft the two conditional bullets were the last items before `## Severity model`; after the build they are the last items of a separate marked section, still immediately before `## Severity model`. No adjacency lost there.

**Concurrency lens — the author asserts it does not fire. I challenge and agree it does not.** The artifact is a single markdown file written once by one builder; there is no shared mutable state, no new accessor, and no read-modify-write window introduced by this change. `git status` shows one modified path. The *run* spawns concurrent agents, but each writes a distinct record path and `decisions.md` writes are serialised after joins (`1.5-criteria.md` Part D). Architect's own model has no shared mutable state by the memo's one-writer-per-node rule (`Architect.md` L30–37) — I re-verified the corrected premise: L10 does say leaf agents *"operate in **paralell** within that slot"*, so the stand-down does **not** rest on sibling serialisation. **Stand-down upheld on the corrected premise.**

**F8 (minor) — my own dispatch may make this review un-run under the rule being shipped.** The config lists exactly **8** `redteam_context` paths (`grep -c "^  - path:"` → 8). My prompt hands me `Guarded_change/stages/stage-3.md` and `stage-4.md`, which are not among them — the same two of the five files that constituted pass-2 violation **E-F7**, after which the runner recorded (`decisions.md` L396): *"Rule for any further pass: stay inside the config's 8 paths, **or quote the supplementary context in the record as B15 requires**. The rule I am shipping is the rule I follow."* My prompt introduces them under "Source you check claims against" without a B15 supplementary-context declaration. Remedy is cheap — quote them as such in this review's record — but if it is not done, C-11's own "missing any of these = un-run" applies to this record.

**F9 (nitpick) — `origin.kind` is described as a two-value field.** L139–141 presents `coordinator` or `peer`. Measured, the field also takes `human` and `task-notification`. Not load-bearing (a `human` origin would be *stronger* evidence, not weaker), but a reviewer told to expect two values and seeing a third has been given an incomplete instrument description.

---

## Lens 5 — Fidelity

Terms pinned, each to its concrete mechanism in the owner's spec, with the artifact's implementation checked against *that* mechanism rather than a convenient stand-in.

| Loaded term | Pinned mechanism (owner intent) | Artifact implements that? |
|---|---|---|
| "3 independent cold agents" | three **separately-spawned** subagents, `Architect.md` L104–107 loop over `Spawn_redteam`; record 55 item 6 | ✓ L212–213 explicitly forecloses the proxy ("not one agent asked three times") |
| "granularity floor" | the `_granularity` argument of `Spawn_redteam` (L28), a Layer-2 constant threaded down and branch-overridable (L1–3) | ✓ L30–32 pins to the invocation's floor, not the run's — the proxy the draft used |
| "human" / "human tie-break" | `Ask_human` (L18), blocks from any depth, orchestrator relays verbatim; L20 names the severity path | ✓ L189–191. The available proxy was `Human_gate` (L16), which takes a division and cannot carry a severity; the run explicitly rejected it |
| "the artifact under review" | the `plan` string passed to `Spawn_redteam` (L28) | ✓ L23–26, L50–53 aim at the plan node |
| "completion condition" | `while(task.empty()==false)` exit at L66, `task = Severity(Union(...))` L110 | ✓ L202–204 — the loop's real exit, not "a gate passes" |
| "seam" | derivable from `Divisible`'s two returned sub-tasks (L14); what `Human_gate` presents (L16) | ✓ L114–115 |
| "cold" | no shared context with the author; **and none with each other** is D6, an author strengthening | ✓ carried, and declared as the author's in §0.5 D6 |
| "union" | `Union()` L24 — "merges issues, DISCARDS NOTHING; dedups only exact restatements" | **✗ — F3 below** |

**F3 (major) — `Union` is given a power the owner's spec does not give it, and the run's own record says so.** L100–108 assigns `Union` a disposition mechanism: *"A finding whose cited file:line does not resolve is marked UNSUBSTANTIATED and **does not pass forward as blocker|major**."* Mechanically that is `Union` overriding a severity — but `Architect.md` L24 defines `Union` as merge + dedup only, and `Severity()` (L26) is the function that filters on severity.

The ratification behind this is record **1449 item 3**, verbatim (I read it at its index): *"That \*was\* part of what Combine did, but you said nothing could get discarded, make up your mind."* That selects **where the duty lives**. It says nothing about the disposition. `0-baseline.md` D11 states this itself: *"⚠ **RAT2 declaration:** the owner ratified *where the duty lives* … he did **not** specify the disposition mechanism. 'Marked unsubstantiated, does not pass as blocker|major' is the **orchestrator's elaboration**."*

The charter now inlines RAT2 as a shipped operative duty (L148–155): an elaboration introducing operative commitments — *"a mechanism, an 'only/every/never', a division of responsibility"* — not entailed by the ratified phrase is **unratified inflation, untrusted until the owner confirms it (ranks ≥ major)**. By the artifact's own rule, its own D11 elaboration ranks ≥ major, and the axis was declared rather than re-asked — while this same run re-asked two other axes (D1, the second human primitive) and got answers both times.

**Counter-reading, stated so you can weigh it:** *"make up your mind"* is plausibly read as the owner delegating the resolution. If so, D11 is authorised and this is not inflation. That makes it exactly what the charter's L185–186 calls a **borderline** — surfaced ranked for a person to rule on, not resolved by the loop. I surface it at major, per RAT2's own floor, and flag the counter-reading rather than resolving it.

**Fidelity is not clean**, so the earned-clean burden does not apply — but the pins above are given in full regardless, as the charter requires.

---

## Ratification audit (RAT1/RAT2) — required section

I read both loci directly in the harness-authored transcript. **Four owner-quotes spot-verified** (two required).

**R-6 — lens structure. Locus: record 1829.**
- Options presented, record **1825**, verbatim as read: *"three options: six distinct lenses, fold but keep a required completeness verdict, or fold entirely and accept that a skipped completeness check is undetectable."* ✓ **Exact match** to `decisions.md` L435–436.
- Owner's response, record **1829**, verbatim as read: *"okay, the lense thing: Why are you even giving fold as an option on this? Its literally just the six lense option without the structure that makes it work"* ✓ **Exact match**.
- **Mapping — I audited it rather than accepting it.** The owner rejects "fold" categorically ("why are you even giving fold as an option"), which covers **both** fold variants, leaving "six distinct lenses" as the only surviving option. The axis is disambiguated. **RATIFIED.**
- **The recorded framing defect does not undermine the ratification.** `decisions.md` L446–452 records that two of three options were the same option. I disagree with the runner's *reasoning* there — the owner's words say fold **is** six-lens *minus* the structure, i.e. strictly weaker, which is the opposite of "the same option" — but the disagreement is immaterial to the outcome: on either reading fold is rejected and six lenses is selected. RAT1's "partial or adjacent answer" trigger does **not** fire; correcting an option set's framing while ruling on the substantive axis is not evasion. **The framing defect is real, recorded, and non-undermining.**
- **Interest check.** The ratified outcome runs against the orchestrator's own prior position (he proposed the fold at 1124 and re-argued it at 1794). A ruling that overturns the recorder's own preference is not a resolved-into-the-author's-pick risk. **No inflation.**
- **Elaboration check (RAT2).** The ratified phrase's operative terms are "six distinct lenses" and "the structure that makes it work". The artifact ships six numbered lenses with a per-lens verdict (L48) and an earned-clean Completeness clause (L95–99). The earned-clean clause is claimed **nowhere** as owner authority — it is declared author decision **D2** in §0.5 and appears as C-10 without an owner citation. Correctly declared. **No inflation found.**

**R-7 — the second human primitive. Locus: record 1762 item 2.**
- Options presented, record **1758**, verbatim as read: *"whether you want a second function in your spec — something like an ask-the-human call any node can make — or whether severity disputes ride some other way. Your file, your call."* ✓ **Exact match**.
- Owner's response, record **1762**, verbatim as read: *"yes, add second function so agents can ask the human a question, filtered through you for obvious reasons."* ✓ **Exact match**.
- **Mapping.** "yes, add second function" selects option 1 directly; "filtered through you" specifies the orchestrator as relay. **DISAMBIGUATES. RATIFIED.**
- **Elaboration check (RAT2) — I went further than the record.** `Architect.md` L18–20 is not owner-typed prose: I traced it to an `Edit` tool call by the orchestrator at **transcript line 1787** (`old_string` = the `Human_gate` line, `new_string` = `Human_gate` + the new `Ask_human` block). So the spec text the charter cites as owner authority is the orchestrator's **elaboration** of "yes, add second function". Auditing it against the ratified option: "BLOCKS FROM ANY DEPTH" is entailed (the owner himself framed depth-reachability as the question at record 1572 item 3); "filtered through you" → the orchestrator-relay comment is direct; and **L20's binding of `Ask_human` to the severity path is entailed by the option as presented at 1758**, which explicitly framed the alternative as "or whether severity disputes ride some other way". **No unratified inflation.** The charter's L189–191 rests on ratified ground.
- Worth recording, though not filed: `decisions.md` L516 says `origin.kind` *"is now owner-spec at `Architect.md` L19"*. L19 was written by the orchestrator at transcript line 1787, not by the owner. The *content* is factually correct (I measured it, see Lens 1), so no false claim reaches the charter — but calling an orchestrator-authored line "owner-spec" is the label RAT1's own text warns against, in the record that justifies shipping F1.

---

## Unverifiable claims I could not check

- **Whether the Part-A criteria actually pass.** `oracles/` and `fixtures/` are **empty directories**; `check.sh`, `mutation-test.sh`, `rules.tsv`, `forkdiff.sh` and `8-harness.md` do not exist. This is expected at stage 6 (they are stage-8 work), and per H6 every Part-A result is `verified = no` until the self-test runs. I verified criteria satisfaction by reading, not by oracle. **Nothing in the run currently reports any Part-A criterion as passing**, so nothing is claimed-verified-but-isn't.
- **Whether the four surviving arms (B-1…B-4) discriminate.** Not run yet. Correctly not claimed.
- **Whether the placements (C-17, C-23) have behavioural effect.** Cut by design on record 1572's authority; disclosed in `1.5-criteria.md` Part B and `2-plan.md` §1.1. I did not re-litigate the cut. **Audit result on the reduction: of the five criteria that ship unverified or text-only (C-17, C-23, C-14, C-10, C-21), every one is text-present in the artifact, and none is reported anywhere as behaviourally verified. Nothing is claimed as passing that is not.** The exception is the `origin.kind` block, which ships unverified and is *not* on that list — F1.
- **Whether every future Architect cold reviewer can execute the `origin.kind` duty.** L143 says *"you are the one who must look"*, which requires filesystem read access to `~/.claude/projects/…/subagents/`. Neither `Architect.md` nor the charter grants, mentions, or bounds that capability, and `Spawn_redteam(_task,_plan,_granularity)` (L28) carries no tooling contract. It degrades gracefully via B10 ("flag the unverifiable"), so I rank the gap minor rather than major — but a reviewer with no shell cannot perform a duty the charter states unconditionally. Folded into **F1**.

---

## Findings table

| # | severity | lens | file:line | finding | why it matters |
|---|---|---|---|---|---|
| **F1** | major | 2 / 4 | `Architect/stages/charter.md`:136–146 | The 11-line `origin.kind` spot-verification block was added with **no criterion asking for it**. `grep -i origin` over the frozen `1.5-criteria.md` and `2-plan.md` returns only "originally produced"; the authority is `decisions.md`:510–521, written in the same gate entry that froze the criteria. It also imposes a duty ("you are the one who must look") requiring filesystem access no spec grants. | It is normative reviewer-facing text in a prompt every cold reviewer reads verbatim, and it is the single largest un-asked-for change in the diff. Nothing in the accept bar can probe it, and it is **absent from the run's own list of the five things that ship unverified** — so it is unverified content that is not disclosed as unverified, which is the exact discriminator stage 6 was told to check. (Its factual content I confirmed correct against the harness — the defect is coverage, not truth.) |
| **F2** | major | 2 | `Architect/stages/charter.md`:112–116 | The closed set ends "plus **whatever review-context paths your caller supplies**", which makes author-supplied context in-set by construction — so "any supplementary author-authored context must be quoted as such" and its un-run penalty can never bind. The fork source (`Guarded_change/stages/charter.md`:74–77) bounds the set by lists fixed outside the author. | B15's operative guard is defeated while appearing carried. This is recorded as pass-2 finding **D-F04/E-F6** (2/3) at `decisions.md`:264–266, appears in **no** later "Fixes applied" table, and C-11 was frozen without addressing it. The runner committed exactly this violation itself at pass 2 (E-F7) — the rule that would have caught it is the one being weakened. |
| **F3** | major | 5 | `Architect/stages/charter.md`:104–105 | "does not pass forward as blocker\|major" gives `Union` a severity-override power `Architect.md`:24 does not grant (merge + dedup only; `Severity()` at L26 is the filter). Owner record **1449 item 3** ratifies *where* the duty lives, not the disposition — `0-baseline.md` D11 says so explicitly ("the **orchestrator's elaboration**"). | The charter inlines RAT2 (L148–155) as a shipped duty ranking unratified inflation **≥ major, untrusted until the owner confirms**. Its own D11 elaboration meets that definition and was declared rather than re-asked, in a run that re-asked two other axes successfully. Counter-reading ("make up your mind" delegates) is plausible — which makes it a **borderline for the owner to rule on**, per L185–186, not something the loop should settle. |
| **F4** | minor | 2 | `Architect/stages/charter.md`:188–189 | C-08 (gating, "ported **verbatim**") requires "a logged **`decisions.md`** entry" and "the reviewer's **routing** stands"; shipped text says "a logged entry" and "the reviewer's **severity** stands". Source: `Guarded_change/stages/stage-4.md`:34–36. | The contest half of the demotion rule now names no log, and `Architect.md` offers no persistence but `Memo_write` (L37, per-node, read only by that node's restart) — so the rule cannot be complied with. Dropping `decisions.md` is defensible under C-22, but the deviation from "ported verbatim" is undeclared and two clauses fail a literal C-08 probe. |
| **F5** | minor | 1 | `Architect/stages/charter.md`:13–15 | C-03b names three CHANGE rules whose difference must be declared: B02, B09, **B19 restated per-caller**. The blockquote declares B02, B09, and the **closed set** (B15/D3′) — B19 is listed under **CARRIED** with no difference stated, though its text was re-aimed from "stage-specific additions" to "your caller's aiming". `0-baseline.md` §0.3 also gives B19 intent CARRY, contradicting C-03b. | Either a frozen gating criterion is unmet or it mislabels its own rule ID. C-03b exists precisely because pass 1 "checked 'difference declared' nowhere" — leaving its third instance ambiguous reproduces the ambiguity one level up. Cheap to fix in either document. |
| **F6** | minor | 4 (position) | `Architect/stages/charter.md`:85–86 | The build removed the precision clause from the "No issue found per lens is allowed" bullet (build-diff L106) as well as adding it at L215. C-23/D9 cover only "B18 is last"; nothing covers the removal, whose own rule says "a removal changes a neighbour's adjacency". | The pairing of *a clean lens is a real all-clear* with *you are graded on precision* is what jointly licenses filing nothing; that adjacency is gone. By D9's own premise — position has behavioural effect — this is a second positional change shipping unverified and, unlike C-17/C-23, unlisted as such. |
| **F7** | nitpick | 1 | `Architect/stages/charter.md`:166–169 | B17's ranking clause — "ranked by the impact of the lost/torn write, not by whether the guarded path itself looks correct" (`Guarded_change/stages/charter.md`:100–101) — is dropped, while B16's exactly parallel ranking clause ("ranked by impact, not by whether any text was lost") is kept at L165. | Asymmetric compression of two CARRY rules that were symmetric in the source. The rule is still stated so C-02 is met; but the reason B16 kept its clause applies equally to B17. |
| **F8** | minor | 4 | `Architect/changes/charter-2026-07/records/stage6-prompt.md`:60–61 | My context list includes `Guarded_change/stages/stage-3.md` and `stage-4.md`, which are **not** among the config's 8 `redteam_context` paths (`grep -c "^  - path:" Architect/guarded-change.architect.md` → 8), and the prompt does not declare them as B15 supplementary context. These are two of the five files of pass-2 violation E-F7. | `decisions.md`:396 records the pledge: *"stay inside the config's 8 paths, **or quote the supplementary context in the record as B15 requires**. The rule I am shipping is the rule I follow."* If this record does not quote them as such, C-11's "missing any of these = un-run" applies to this very review. Remedy is one paragraph in the record. |
| **F9** | nitpick | 1 | `Architect/stages/charter.md`:139–141 | `origin.kind` is described as taking `coordinator` or `peer`. Measured across the project's transcripts it also takes `human` (1011) and `task-notification` (23). | A reviewer given a two-value description and seeing a third value has an incomplete instrument. Not load-bearing — a `human` origin is stronger evidence, not weaker. |
| **F10** | nitpick | 1 | `Architect/stages/charter.md`:209–210 | "the human gate sits **here** too" reads as though `Human_gate` is called inside `Divisible`. `Architect.md`:83 calls it from `Node()` after `Divisible` returns; `Divisible` (L14) red-teams and returns sub-tasks only. | Both concern the same division and both precede child spawn, so the substance is right and the reviewer never calls `Human_gate` — but the charter is the one document a reviewer reads about the loop it is inside. |

---

## Worst severity

**major** — three of them: **F1** (11 lines of normative content no frozen criterion asked for, shipping unverified and unlisted), **F2** (the closed set's boundedness is gone, defeating B15's supplementary-context guard — a known 2/3 pass-2 finding that ships unclosed), and **F3** (`Union` is granted a severity-override the owner's spec does not define, on an elaboration the run itself declares unratified, in violation of the RAT2 duty this very artifact inlines).

**No blocker.** The artifact is not solving the wrong problem, is executable as written, and — critically for stage 6 — **the regression bar is met**: every CARRY/CHANGE rule B01–B19 is still stated, the single DROP is declared in the provenance blockquote, nothing fell into a silent third category, and nothing is reported as verified that is not. The deliberate reduction is honestly disclosed; my findings are about the three things that escaped the disclosure, not about the reduction.