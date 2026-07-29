# Reviewer F (general-purpose, sonnet) — stage-3 pass 2, VERBATIM

> **RE-EXTRACTED 2026-07-28.** The previous contents of this file were titled "verbatim" and were a
> **condensed paraphrase** — 21,962 chars against the agent's actual 28,855, with 218 of 338 twelve-word
> windows absent. Caught by a cold claim-audit. Recovered programmatically from the harness-authored
> subagent transcript `subagents/agent-a065997726e646162.jsonl` (last assistant message), not retyped.
> Extraction command is in `6-redteam-code.md`.

---

## Context files read + sha256

| Path | sha256 | Extent read |
|---|---|---|
| `/home/zero/Documents/Architect.md` | `986512f56876531b1e8596c89208dadefd8bf47517d725d56d5a0269c58bb78b` | full (115 L) |
| `Guarded_change/stages/charter.md` | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` | full (103 L) — grep re-run independently, matches `0-baseline.md` §0.2 exactly |
| `Guarded_change/stages/stage-3.md` | `16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3` | full |
| `Guarded_change/stages/stage-4.md` | `175061c27bb6980ff76c6358d403299d343c409b2952308ffea7485fff880675` | full |
| `Guarded_change/stages/stage-1.5.md` | `c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b` | full |
| `Guarded_change/stages/stage-8.md` | `8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3` | full |
| `Architect/guarded-change.architect.md` | `42f289a51ed4e5f706d3b70bc8ca47a2e8dc16d2aba4f3f3ac76a02d0cb0429c` | full |
| `Dragonfly/stages/charter.md` | `c5d1e2068f35760e373517e243003800c264c64bf3d93d6d8ea6b951990af870` | full |
| `Architect/stages/charter.md` | `6a1981f3fd4db5a496ed23928b90ca8b575c30d5afb3765f792e09d543a19212` | full — **UNVETTED DRAFT banner present**, confirming this is the pre-build draft, no standing |
| `Architect/ATTEMPT-2-STATE.md` | `1d27d50f2281051cfaa7fc46f603f70248c33fef05683e570504e8b6f4807269` | full |
| `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md` | `94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8` | full |
| `Architect/changes/charter-2026-07/0-baseline.md` | `b22b251bdc1d320680a6abe38cc8454122bddefc24465b6fa888d16646f24dee` | full |
| `Architect/changes/charter-2026-07/1-spec.md` | `e45da3352220dd3729808e1cee20515f8cefeb55f1e49ab4f0bfcdd60627fe5f` | full |
| `Architect/changes/charter-2026-07/1.5-criteria.md` | `d070b714ee0322c850f5309716bbce11de9225f8578872e3b5d61468c3e2120f` | full |
| `Architect/changes/charter-2026-07/2-plan.md` | `f01093d2a003405433966e3d2345ed0490e55dad4dad433b2f7e652b239c73ca` | full |
| `Architect/changes/charter-2026-07/decisions.md` | `34a0def184875510aa17452af010fae7eb2b4422c6eb8b67c59acdf7bf80e10c` | full |
| `…/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl` | `eb769686c4f19bb7fdf81a4a492c99848d0f52872c82b8fb56088c452ff26910` | partial — records 51, 55, 784, 789, 1124, 1128, 1148, 1171, 1175, 1188, 1209, 1258, 1274, 1449 read directly by index (1534 lines total) |
| `Architect-Attempt-1/stages` | — | directory listing only (superseded, per closed-set instructions) |

**Read outside the strict closed set, disclosed as such (needed to check citations the artifacts make to it):**

| Path | sha256 | Extent |
|---|---|---|
| `Architect/changes/charter-2026-07/records/reviewer-A-verbatim.md` (pass-1 record) | `b4224fc8e69b826c9f7eb9b3bac5e26d69c2803acc9f063c9d29ddb4765b6308` | partial (~120 L of 60K chars) |
| `Architect/changes/charter-2026-07/records/reviewer-B-verbatim.md` (pass-1 record) | `b13bb7fe06f921fe77573d24fdea5dfa4d4e6b058f15792e6298740ff0df6384` | partial (~40 L of 62K chars) |
| `Architect/changes/charter-2026-07/records/reviewer-C-verbatim.md` (pass-1 record) | `fa20f1fd67f301c3f6edb1ade5e8135b7436dc217698c39765de15560b5b41f8` | partial (~50 L of 28K chars) |
| `Architect/changes/charter-2026-07/records/stage3-prompt.md` (pass-1 prompt) | `ae556a4a579bf84b46aa5401a53f5fc764bb3b9b41d9ab19bc0e068931d55b73` | hash-check only |

I did **not** read the pass-1 reviewer records in full (they total ~150K characters). I relied on the carried-forward summary in my own prompt plus these partial samples plus independent re-derivation against primary sources. This is disclosed as a limit on how deeply I re-verified pass-1's *original* findings versus how deeply I verified this pass's *claimed fixes* against primary sources (which I did fully, independently, for every item in the carried-forward list).

---

## Lens 1 — Factual

**No blocking factual defects found on the core claims I could check exhaustively.** Verified directly against primary sources:
- `Guarded_change/stages/charter.md` is 103 lines (`wc -l`), matches sha `0e73bacf…adc590` at three locations claimed in `0-baseline.md` §0.1 — confirmed by my own `sha256sum`.
- My own re-run of `grep -n -E "^[0-9]+\.|^- \*\*|^The reviewer is graded" Guarded_change/stages/charter.md` reproduces `0-baseline.md` §0.2's output line-for-line, and I independently read every non-bulleted span (L1–18, L34–35, L79–80, L100–103) for missed rules — I found none beyond B01–B19. **B01–B19 is complete against the fork source**, as claimed.
- `Architect.md` L14: `Divisible(string _task, string _granularity)` — confirmed 2-arg, and all three call sites (L58, L83, L107) pass only `(task, granularity)`, never a plan. D3′'s premise is accurate.
- All seven pre-existing owner quotes (records 55, 1128, 1148, 1175, 1258, 1274, and 1188) verify character-exact against the transcript at their cited indices.
- Record 1449's five items verify character-exact.
- Dragonfly's precedent (`Dragonfly/stages/charter.md` L8–12) contains **no sha256**, only a commit ref — confirms C-01's attribution correction (B-F19) is accurate.
- The "means nothing" quote ATTEMPT-2-STATE.md §6 warns about is real, but its transcript locus is **record 789** (the tool-result carrying the user's free-text answer), not **784** (the assistant's `AskUserQuestion` call that record 784 actually is — I read it directly: it's a `tool_use` block, not owner text). This citation is off by five records. It doesn't affect anything in the artifacts under review (none of them cite 784/789 directly), but it's a defect in a file this run is instructed to use for locating loci, so I flag it as a nitpick against `ATTEMPT-2-STATE.md` itself, not against the artifacts under review.
- B-F04's correction (record 55's "option be" → record 51's option (b), the completeness-critic pass, not the general red-team) is verified accurate: record 51 §"2." lists candidates (a)/(b)/(c) for the completeness mechanic, and record 55 item 2 answers "option be." Record 55 item 6 separately specifies "three independent cold agents" for the adversarial stage. C-15's citation is sound.

**F-1 (minor).** `1-spec.md` §9's claim that records **1124 and 1171** show the author "**twice** proposed folding the sixth lens away" overstates record 1171. Record 1124 explicitly proposes it ("needs trimming: its separate sixth Completeness lens folds into the single red-team mandate"). Record 1171, which I read in full, is substantively about crash recovery and closes with a description of attempt-1's charter shape, ending only "worth keeping from it: the discipline bullets… and the severity ranking. **The rest of the charter is trimmable**" — a general remark, not a second explicit fold-the-lens-away proposal. This doesn't change any operative outcome (D1 is correctly declared author-owned regardless, not owner-ratified either way), but it inflates the evidentiary basis offered for D1's "independence" narrative in `1-spec.md` §9's closing paragraph.

## Lens 2 — Logical

**L-1 (major). The claim in `2-plan.md` §4 that B-5/B-6 vary "the only variable" — position — is false; relocating a block changes two adjacencies, not one.** §4 states: *"charter-varying for B-3, B-4 (rule ablation) and B-5, B-6 (block relocation, not deletion — so no text is lost and the only variable is position)."* But B-5 relocates the granularity-floor block from **between** the constitution block and the lens block to **after** the lens block. This changes (a) what now immediately follows the constitution block (the lenses, not the floor) and (b) what now immediately follows the lens block (the floor, not the discipline-bullet block) — **two** adjacency relationships change, not one. If the HOLED/INTACT arms differ, the design cannot attribute the difference specifically to "floor before vs. after the lenses" as opposed to "constitution now directly abuts the lenses" or "lenses no longer directly abut the discipline bullets." This is exactly the failure mode the charter's own position-lens bullet warns about ("an added tail block displaces the old last element… a removal changes a neighbor's adjacency") — applied here to the harness that is supposed to be *testing* that lens, not just the artifact under test. B-6 has a milder version of the same issue (inserting B18 into the discipline-bullet list changes that list's internal ordering too), but is more contained since it doesn't touch a third block's boundary.

**L-2 (major, statistical power). `n=2` with hard within-arm agreement is likely underpowered for exactly the probabilistic effects `stage-1.5.md`'s own ST1.5d anticipates**, and the design compounds this by pinning the two within-arm runs to **different models** (`1.5-criteria.md` Part B, "Model pinning"). ST1.5d states: *"Where the effect is probabilistic (recency/precedence usually shift a rate, not flip a switch), the criterion states the pass rate it expects and the number of runs that establishes it… rather than relying on a single probe."* B-5/B-6/B-7 do neither — they require **exact** agreement across **two different models** in **two** runs, with no stated pass-rate floor. A real but partial effect (say, one that fires 60–80% of the time) will very plausibly show up as within-arm disagreement under this design — indistinguishable, by construction, from "no effect." The plan's own framing (`2-plan.md` §8 R4, "B-5 and B-6 may return 'no effect.' That is a real result, not a failure") is honest about the *outcome* but doesn't address that the *design itself* cannot tell a genuine null from an underpowered probabilistic positive. This is the same class of gap as pass-1's B-F08 (n=1), only partially closed: n went from 1 to 2, but ST1.5d's own prescribed remedy (a stated pass-rate over a stated number of runs) was not adopted.

**L-3 (minor).** `2-plan.md` §1.1 table row 6 places RAT1/RAT2 (a wholly new block, absent from the fork source) between the discipline bullets and the conditional lenses. Under the position lens's own rule that inserted elements are in scope even when the elements around them "did not themselves change," no criterion checks whether this insertion changes the earned-clean-fidelity bullet's (block 5's) effective adjacency to the conditional lenses it used to sit closer to. See CH8 below — this overlaps with a coverage gap, not a distinct logical flaw, but it's worth flagging under both.

## Lens 3 — Missed opportunity

**M-1 (minor).** `oracles/forkdiff.sh` (C-02b) derives its residue independently of `0-baseline.md`'s inventory, which is the point — but nothing cross-checks that the residue is *exactly* the one declared DROP (the A/B-harness sub-clause). A trivial addition — assert the residue set equals `{B15's A/B-harness sub-clause}` exactly, not just "each residue line is named or a finding" — would make C-02b self-verifying against C-03 rather than two independently-worded checks that happen to agree.

**M-2 (minor).** The plan never considers replaying pass-1's exact prompt/fixtures against the pass-2 charter as a regression check that *only* the claimed-fix content changed. Given how large this document is getting (30 gating criteria, 7 behavioral arms, 4 mutation classes), a "nothing else moved" diff-based check against the pass-1 draft would be cheap insurance against an accidental second regression riding along with the intended fix — the exact failure mode this project has repeatedly produced (D5, D14).

## Lens 4 — Unstated assumptions & risks

**Position lens — fires, as the prompt notes, and see L-1/L-3 above and the coverage-challenge below.**

**Concurrency lens — the revised stand-down is correct; verified independently.** I checked `Architect.md` L10 ("leaf agents… operate in **paralell** within that slot"), L12 (node-level slot reservation), and L26–33 (memo one-writer-per-node rule) myself, independent of `1.5-criteria.md` Part D's own re-derivation. The corrected reasoning holds: Architect's own execution model has no shared-mutable-state accessor uncovered by the memo rule, and the earlier "slot inheritance serialises siblings" premise (corrected in `0-baseline.md` B17) was indeed wrong at the lines it used to cite. **No fidelity issue on this point; clean, earned with citation.**

**A-1 (major — see Lens 5, this is the same finding cross-filed).** The demotion rule's "human tie-break" assumes a human-reachability mechanism inside Architect's own shipped runtime that I could not confirm exists.

## Lens 5 — Fidelity

Terms pinned: **"human"** (in the demotion rule's "human tie-break") → the owner, reached by whatever mechanism Architect's own `Node()` loop provides for stopping and asking him. **"reviewer"** → a cold subagent per `Spawn_redteam`/`Divisible`'s split review, pinned correctly throughout. **"charter given"** → the core-verbatim-plus-additions composition (B19/S17), correctly pinned and tested (C-20). **"ratification"** → an artifact per RAT1, correctly pinned in S16/C-21 with the audit machinery this section itself performs.

**F5-1 (major). D10's claim that the demotion rule's "human tie-break" is reachable "via the RAT3 delegated-runner halt path" substitutes a mechanism the owner never confirmed exists in Architect's own runtime, and the ratification record overstates what was actually ratified.** `Architect.md`'s only human-facing primitive is `Human_gate` (L16), which fires **specifically for division/split review** at `depth <= gate_depth` — nothing in the pseudocode provides a general "stop the loop, relay to the owner, resume" hook for an arbitrary severity-demotion dispute. **RAT3** — the mechanism D10 invokes — is documented only in `Architect/guarded-change.architect.md`'s Notes section ("This loop runs in a subagent; the main session is orchestrator…") and is explicitly a property of *this guarded-change build run* (the meta-process constructing the charter), not a property Architect.md attributes to its own shipped `Node()` loop. Once Architect is built and running as a skill (elements 4–6), a cold reviewer inside `Spawn_redteam` who wants to contest a severity has no RAT3 to invoke — that scaffold belongs to the orchestrator/subagent relationship of *this* run, not to Architect's own execution model.

The owner's record-1449 item 2 answer — *"It gets implemented however it is implemented in guarded-change; that is what the instruction was: copy over the severity mechanism from guarded change"* — settles **what text** the demotion rule should contain (port it verbatim). It does not settle **whether a human is reachable** from inside Architect's own runtime when that text is exercised. `1-spec.md` §9 and `decisions.md`'s Gate-4 entry mark this "**Ratified**" and state it "**resolves A-F4/B-F11**" (the pass-1 finding that "no mechanism exists to reach the human"), but the mechanism gap A-F4/B-F11 originally flagged is not actually closed by an answer about wording. Per the charter's own RAT1 rule — *"An owner answer that is partial or adjacent… is **not** a ratification: the loop re-asks the flagged axis"* — this reads as a partial answer resolved into the runner's own convenient reading, which is precisely what CH11 exists to catch, and precisely the asymmetry the run's own §9 RAT2 sweep caught for **R-3** (self-flagged) but missed for **R-2/D10** (not self-flagged). `decisions.md`'s own closing claim, *"Nothing else in D8–D14 claims owner authority it does not have,"* is directly contradicted by this instance.

This is a load-bearing contingency for a **gating** criterion (C-08/S14): if no mechanism exists, the demotion rule is a policy statement a reviewer/author cannot actually execute end-to-end, which is exactly the class H5/ST1.5a-b exist to prevent from reaching "done" silently.

## Pass-1 fix audit — required section

| Pass-1 finding | Claimed fix | Verdict |
|---|---|---|
| C-17 tested the fixture, not the position (BLOCKER, 2/3) | Arm B-5, relocates the floor block | **Fix is real in direction (now varies position, not fixture) but methodologically confounded** — see L-1: relocation changes two adjacencies, so a differing result cannot be cleanly attributed to "floor position" alone. Not a relabeling, but not clean either — **major residual**. |
| Fork-source composition rule (B19) missing, 3/3 | B19 added + independent forkdiff probe C-02b | **Closed.** Independently re-verified B01–B19 completeness against the fork source myself; B19's text and citation (L70–74) check out exactly. |
| Mutation test tautological | Semantic + insertion mutants (Part C) | **Closed, sound design.** Negate/swap-actor/move-section/hedge mutants correctly target "does the probe check a rule or a phrase," and C-M2's insertion-mutant fix for absence sweeps is the correct mutant shape (deletion is undefined for an absence check). |
| Arms n=1, unbounded self-rebuild | n=2, within-arm agreement, one-rebuild bound | **Rebuild bound: closed, real constraint.** **n=2/agreement design: not closed** — see L-2, likely underpowered for a probabilistic effect, and doesn't adopt ST1.5d's own prescribed remedy (stated pass-rate over N runs). |
| D3's closed set gave `Divisible` an input its signature can't supply, 3/3 | D3′, conditional per-caller | **Closed, genuinely.** Verified `Divisible`'s 2-arg signature myself; D3′ correctly drops the parent's-plan input and derives the seam from what `Divisible`/`Human_gate` actually produce. Not a dodge. |
| C-18's advisory reason covered 1/3 sub-clauses, 3/3 | Split into C-18a (gating)/C-18b (advisory) | **Closed for C-18 itself.** But see F-2 below — the identical defect class (a partial sub-clause claimed as full coverage) has recurred in C-14/B-7, unfixed. |
| CHANGE class's "difference declared" half unchecked | C-03b | **Closed**, checkable positive assertion added, correctly distinguished from C-03's DROP check. |
| B18's terminal position displaced, 2/3 | D9 + arm B-6 | **Direction correct, same confound as B-5** (see L-1) — B-6 also relocates rather than deletes and shares the "only variable is position" overstatement, though less severely. |
| `Divisible` caller had zero behavioral verification, 3/3 | Arm B-7 | **Partially closed.** B-7 tests only the "coverage of the whole task" sub-clause of C-14's four claimed sub-properties (coverage, seam soundness, below-floor, real-joint-vs-arbitrary-cut) — see F-2, the same "claims full, delivers partial" pattern C-18 was fixed for elsewhere in this same pass. |

## Coverage challenge (CH8) — required section

**CH8-1 (major).** **RAT1/RAT2 — the newest, highest-stakes addition to the charter (it exists specifically to prevent the exact self-certification failure this project already produced) — has zero behavioral verification.** Every other load-bearing new/changed duty (floor, completeness, severity, union, `Divisible` caller) gets a HOLED/INTACT arm; RAT1/RAT2 gets only text-presence checking (C-21, checked by `check.sh`/mutation). No fixture tests whether a reviewer given the shipped charter actually catches a fabricated or inflated "OWNER RULING" (e.g., a fixture plan citing an owner quote that doesn't disambiguate the flagged axis, the way R-2/D10 above arguably does) versus a reviewer given the charter without RAT1/RAT2. This is the same gap class C-14 had before B-7 was added (3/3 finding: "a charter that only aims the first caller is incomplete" / zero behavioral verification for a load-bearing duty) — recurring, per D5's own "recurrence means under-generalization" principle, in exactly the addition most motivated by this project's actual failure history.

**CH8-2 (minor).** No criterion tests whether adding "unverifiable" back into the blocker-severity definition (C-07, fixing A-F15) actually changes a reviewer's classification behavior for a genuinely-unverifiable-but-plausible claim — only text presence is checked.

**CH8-3 (minor).** No criterion checks whether the RAT1/RAT2 block's insertion (a wholly new block, not in the fork source) changes the effective behavior of the blocks now adjacent to it differently than before — see L-3.

## Label audit (CH9/CH10) — required section

Per-criterion spot-check of gating labels and their claimed verification path:

- **C-02/C-02b (fork fidelity):** gating, verified against the real governed path (generated table + independently-derived diff residue against the actual fork source, not a proxy). **Clean.**
- **C-17/C-23 (position):** gating; the plan explicitly and correctly declares the line-order text check "supporting evidence only, insufficient" and routes the real verification to B-5/B-6. This is exactly the CH9 discipline done right — **except** the executed halves themselves carry the L-1 confound above, so the *label* is honest but the *instrument behind it* is weaker than claimed.
- **C-14 (both callers):** **F-2 (major).** Labeled gating, "verified" text claims an "executed half" (B-7) that in fact exercises only the coverage sub-clause of the four properties C-14 asserts (coverage, seam soundness, floor violation, arbitrary-cut detection). This is a proxy-path problem in CH9's own terms — "verified against a proxy… an input class that never triggers" the other three sub-properties — of the identical shape pass 1 found and fixed for C-18 (partial sub-clause coverage claimed as a full pass), now unfixed for C-14 in this same document.
- **C-18b, C-19 (advisory):** both carry legitimate, concrete reasons (element 3 doesn't exist yet; no defensible pre-build length threshold) — not dodges. **Clean.**
- **C-08 (demotion rule):** labeled gating; text-verified against `stage-4.md` L26–28/L34–36, which I confirmed matches. But see F5-1 — the criterion's practical *executability* (a human is actually reachable) rests on an unverified mechanism assumption, which the label audit alone (text presence) cannot surface. This is exactly why CH9 exists ("every gating verified=yes must exercise the path the criterion actually governs") — here the governed path (a human tie-break firing inside Architect's own runtime) is never exercised by anything in Part A or Part B.

## Ratification audit (CH11/CH12) — required section

All five records (R-1…R-5) read at transcript record 1449, character-exact, spot-verified by me independently (not just re-trusting the artifacts' transcription).

| # | Axis actually disambiguated? | My verdict |
|---|---|---|
| R-1 (BL-1) | Owner's answer bypasses the (a)/(b) framing but substantively prescribes proceeding + fixing the test — reasonably read as selecting (a). | **Ratified**, mapping defensible. |
| R-2 (H-A / D10) | Owner's answer settles **what text** to port, not **whether a human is reachable** from Architect's own runtime — a different, narrower axis than what A-F4/B-F11 actually flagged (mechanism existence). | **NOT adequately ratified on the mechanism-reachability axis** — see F5-1. `1-spec.md`/`decisions.md` overstate this as fully resolving A-F4/B-F11. |
| R-3 (H-B / D11) | Owner's answer settles placement (Union performs the duty); disposition mechanism correctly self-flagged as the orchestrator's own elaboration, not owner authority. | **Correctly and conservatively self-classified.** Not convenient — the more self-serving move would have been to claim the disposition too. |
| R-4 (H-C / D12) | Owner's answer is a genuine non-answer ("I don't know what the fuck rat1/2 even ARE"); correctly reclassified as author/orchestrator research, not owner ruling. | **Correctly and conservatively self-classified.** Same observation as R-3 — the honest path was taken here. |
| R-5 (H-F / D13) | Unambiguous "discard it." | **Cleanly ratified.** |

**The asymmetry is the finding.** R-3 and R-4 both received the conservative, self-critical treatment the charter's own RAT2 discipline demands (own elaboration flagged, not smuggled in as owner authority). **R-2 did not receive the same scrutiny** — its elaboration (RAT3-reachability) is structurally the same kind of move (an operative claim beyond what the owner's words support) and was not caught by the run's own RAT2 sweep, which claims completeness ("nothing else in D8–D14 claims owner authority it does not have"). That claim is false as I've verified it.

## Unverifiable claims I could not check

- `decisions.md`'s "9 of 9 [pass-1] citations confirmed" spot-verify — I did not re-run those 9 checks myself; I independently verified a different, overlapping sample (fork-source completeness, transcript quotes, `Divisible` signature, Dragonfly's no-sha256) and found no discrepancies in what I checked, but I cannot vouch for the specific 9 pass-1 ran.
- The full text of `reviewer-A/B/C-verbatim.md` beyond the excerpts I sampled — I cannot independently confirm every pass-1 finding's original wording matches the carried-forward summary in my prompt with full fidelity, only that the summary's claims track what I did read of the samples.
- Whether `oracles/check.sh`, `oracles/mutation-test.sh`, `oracles/forkdiff.sh`, and `oracles/rules.tsv` will actually behave as designed — none of this instrumentation exists yet (correctly, per C4's tense discipline); I evaluated the *design* on paper only.

## Findings table

| # | severity | lens | artifact:line | finding | why it matters |
|---|---|---|---|---|---|
| 1 | major | Fidelity | `0-baseline.md` D10 / `1-spec.md` §9 R-2 / `decisions.md` Gate-4 | D10's claim that the demotion rule's "human tie-break" is reachable "via the RAT3 delegated-runner halt path" substitutes a mechanism belonging to this build's meta-process for one Architect's own runtime (`Architect.md`, whose only human hook is `Human_gate` at gate_depth) does not provide; the owner's record-1449 answer ratifies wording, not reachability. | A gating criterion (C-08) whose governed path may not exist in the shipped skill; the ratification record overstates what was actually settled, and the run's own "nothing else claims owner authority it doesn't have" summary is false on this point. |
| 2 | major | Logical | `2-plan.md` §4, arms B-5/B-6 | "The only variable is position" is false for a block relocation — moving the floor block changes two adjacency relationships (constitution↔lenses and lenses↔discipline), not one; a differing arm result can't be cleanly attributed to the intended variable. | B-5 is the executed half of the pass-1 blocker fix (C-17); if the confound is real, C-17 is still not cleanly verified even after the claimed fix. |
| 3 | major | Logical / ST1.5d | `1.5-criteria.md` Part B | n=2 with hard within-arm agreement across two different models, no stated pass-rate floor, is likely underpowered to distinguish a real probabilistic effect from noise — contrary to ST1.5d's own prescribed remedy for probabilistic effects. | All 7 behavioral arms (the load-bearing, expensive verification apparatus) share this weakness; a real but partial effect will likely register as "unstable"/`verified=no` indistinguishable from a genuine null. |
| 4 | major | CH8 / coverage | `1.5-criteria.md` C-21 | RAT1/RAT2, the addition most directly motivated by this project's own self-certification failure history, has zero behavioral verification — text-presence only, unlike every other load-bearing new duty (floor, completeness, severity, union, `Divisible` caller). | Recurrence of the exact defect class (3/3, "a charter that only aims the first caller is incomplete") that B-7 was built to fix for a different criterion, now unfixed for a more consequential one. |
| 5 | major | CH9/CH10 label audit | `1.5-criteria.md` C-14, `2-plan.md` §1.1 row 9 | C-14's claimed "executed half" (B-7) tests only one of the four sub-properties C-14 asserts (coverage; not seam soundness, floor violation, or arbitrary-cut detection) — the identical "partial sub-clause claimed as full" pattern pass 1 found and fixed for C-18, recurring unfixed here. | A gating criterion's verified=yes claim is broader than what its own instrument actually exercises. |
| 6 | minor | Factual | `1-spec.md` §9 (closing paragraph) | Cites records 1124 **and** 1171 as two instances of the author proposing to fold the completeness lens away; record 1171 (read in full) only vaguely says "the rest of the charter is trimmable," it does not explicitly re-propose the fold. | Overstates the evidentiary basis for D1's "shown twice, still declared author-owned" narrative; doesn't change D1's (correct) disposition as an author decision either way. |
| 7 | nitpick | — | `Architect/ATTEMPT-2-STATE.md` §6 | The "means nothing" quote's locus is record 789 (the user's free-text answer), not 784 (the assistant's `AskUserQuestion` tool call, which I read directly and confirmed is not owner text). | Not cited by any artifact under review, but a defect in a file this run treats as a locus-finder; worth a one-line fix. |

## Worst severity

**major**