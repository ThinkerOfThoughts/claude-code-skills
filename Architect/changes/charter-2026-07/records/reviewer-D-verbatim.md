I have completed my independent review. Here it is.

---

## Context files read + sha256

**In-set (the closed set as given):**

| # | Path | sha256 |
|---|---|---|
| 1 | `/home/zero/Documents/Architect.md` | `986512f56876531b1e8596c89208dadefd8bf47517d725d56d5a0269c58bb78b` |
| 2 | `<wd>/Guarded_change/stages/charter.md` | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` |
| 3 | `<wd>/Guarded_change/stages/stage-3.md` | `16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3` |
| 4 | `<wd>/Guarded_change/stages/stage-4.md` | `175061c27bb6980ff76c6358d403299d343c409b2952308ffea7485fff880675` |
| 5 | `<wd>/Guarded_change/stages/stage-1.5.md` | `c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b` |
| 6 | `<wd>/Guarded_change/stages/stage-8.md` | `8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3` |
| 7 | `<wd>/Architect/guarded-change.architect.md` | `42f289a51ed4e5f706d3b70bc8ca47a2e8dc16d2aba4f3f3ac76a02d0cb0429c` |
| 8 | `<wd>/Dragonfly/stages/charter.md` | `c5d1e2068f35760e373517e243003800c264c64bf3d93d6d8ea6b951990af870` |
| 9 | `<wd>/Architect/stages/charter.md` (**UNVETTED DRAFT** — banner confirmed present at L3–6, so I am holding the draft) | `6a1981f3fd4db5a496ed23928b90ca8b575c30d5afb3765f792e09d543a19212` |
| 10 | `<wd>/Architect/ATTEMPT-2-STATE.md` | `1d27d50f2281051cfaa7fc46f603f70248c33fef05683e570504e8b6f4807269` |
| 11 | `…/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl` (transcript, 1534 lines) | `eb769686c4f19bb7fdf81a4a492c99848d0f52872c82b8fb56088c452ff26910` |
| 12 | `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md` | `94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8` |

**Artifacts under review:**

| Path | sha256 |
|---|---|
| `Architect/changes/charter-2026-07/0-baseline.md` | `b22b251bdc1d320680a6abe38cc8454122bddefc24465b6fa888d16646f24dee` |
| `…/1-spec.md` | `e45da3352220dd3729808e1cee20515f8cefeb55f1e49ab4f0bfcdd60627fe5f` |
| `…/1.5-criteria.md` | `d070b714ee0322c850f5309716bbce11de9225f8578872e3b5d61468c3e2120f` |
| `…/2-plan.md` | `f01093d2a003405433966e3d2345ed0490e55dad4dad433b2f7e652b239c73ca` |
| `…/decisions.md` | `34a0def184875510aa17452af010fae7eb2b4422c6eb8b67c59acdf7bf80e10c` |
| `…/records/stage3-pass2-prompt.md` (my charter) | `62a6781b79935d4392d65a32a3520e653d9422cc0c9ebbf2060203d355b5d4fa` |

**OUT-OF-SET reads — declared per the charter's closed-set rule.** The prompt names **RAT3** as a load-bearing mechanism (attack #5) but lists no file that defines it. Item 12 of the closed set (`Architect-Attempt-1/stages`) I did not read. I read, out of set:

| Path | sha256 | Why |
|---|---|---|
| `<wd>/Guarded_change/METHODOLOGY.md` (L200–230 only) | `8f3fe2b322ec802d080aa130ebd5dd526c4407a2f729931763c6a778ea4a7c30` | canonical RAT3 statement — required to check D10's claim |
| `<wd>/Guarded_change/SKILL.md` (L55–75 only) | `addf17481c57bcada577ff2d3d74628b93ea8b43a89c884d25a670af8889c625` | RAT3 operative form |

I also ran `ls Architect/stages/`, `ls Architect/templates/seed/`, and `wc -l` on three files (directory/metadata reads, not document content). No other source was used.

---

## Lens 1 — Factual

**Not clean.** Earned with citations below; several claims are confirmed correct, three are wrong.

**Confirmed correct (spot-verified against source):**
- Fork source is **103** lines (`wc -l`). §0.1's correction holds.
- `stage-4.md` **L34–36** is exactly the SEV3 demotion clause; **L26–28** is SEV2. D10/S14's source citations are faithful in substance.
- `stage-3.md` **L55–82** is exactly CH11 (L55–72) + CH12 (L74–81). D12/C-21's citation resolves.
- Dragonfly `charter.md` **L8–12** names commit `3d6889b`, states four deliberate drops, and contains **no sha256**. C-01's corrected attribution (B-F19) is accurate.
- `ls Architect/stages/` returns `charter.md` only. D12's justification holds.
- `Architect/templates/seed/` exists with four files. C-18a's mechanizability claim holds.
- **Record 1449 is character-exact** for all five quotes, including the asterisks in item 3. Records 1128, 1148, 1175, 1258, 1274, 55 all verify character-exact.
- The **B-F04 correction is right**: record 55's *"option be should be done by three independent cold agents"* attaches to record **51**'s decision #2, option (b) = the *cold completeness-critic pass*; the general adversarial red-team's three agents come from record 55 **item 6**. Verified by reading 51 and 55.
- C-22's claim that the fork source has **three** dangling cross-file references is correct: L33 (`stages/stage-3.md`), L37 (`(below)`), L79 (`the concurrency-lens C3 attempt-1 record`).
- `FINDINGS.md` L60–68 = F4, L89–99 = F7, L106–110 = F9, L123–124 = the concurrency-stand-down-on-a-false-premise record. All cited accurately.

**Wrong:**

**D-F01 (major).** `0-baseline.md` **L265** (D10) asserts the ported demotion rule's human is *"reached through the delegated-runner halt path (RAT3)."* **RAT3 is a guarded-change rule about a subagent running guarded-change** — `METHODOLOGY.md` L212–225 states it in two halves and says explicitly of the subagent half *"(The subagent* is *running this skill, so this half is binding here.)"*; `SKILL.md` L66 repeats *"If a subagent is running this loop…"*. It is the path **this build run** used to reach Roy. It is **not** a mechanism inside Architect. `grep -n -iE "charter|assembl|prompt|lens|conditional" /home/zero/Documents/Architect.md` returns **zero hits**; the only human call in the file is `Human_gate(pair<string> _division, string _task, int _depth)` (L16), which takes a **division**, fires only at `depth <= gate_depth` (L79, default 2), and **cannot receive a severity** — while `Spawn_redteam` (L24) runs at *every* node at *every* depth. `decisions.md` does not exist in Architect's design at all. So the shipped charter will state two mechanisms (a logged `decisions.md` entry; a human tie-break on demotion) that Architect provides neither of. This is the **substitution of a convenient pre-existing implementation** the fidelity lens names. Detail in the pass-1 audit below.

**D-F11 (minor).** `0-baseline.md` **L252** (D3): *"the word 'charter' does not occur anywhere in `Architect.md`'s **103 lines**."* The word-absence claim is **true** (verified). The line count is **wrong** — `wc -l /home/zero/Documents/Architect.md` = **115**. 103 is the *fork source's* count, transposed. This is a re-occurrence of the exact class §0.1 already corrected ("104 lines" → 103), in the document whose authority rests on machine-generated numbers (C5), and D5 says a recurrence means the fix was under-generalized.

**D-F12 (minor).** `1-spec.md` **L71** still reads *"Its **18** rules (**B01–B18**) are the regression bar"* and **L86** (constraint C2) still reads *"Every baseline rule **B01–B18**…"* — after B19 was added and §6 **S17** requires it. The anti-drift fix ("the criteria document now reads the count from this table rather than restating it, so the two cannot drift again", `0-baseline.md` L177–179) was applied to `1.5-criteria.md` C-02 only. C2, the run's **fork-fidelity constraint**, therefore excludes B19 by enumeration: a build satisfying C2 as written need not carry B19. This is A-F13's defect resurfacing one document over — under-generalization again (D5).

---

## Lens 2 — Logical

**D-F03 (major).** `2-plan.md` **L29** (block 7) places both conditional lenses in the shipped charter, always present, each marked conditional with its trigger. `1.5-criteria.md` **C-20** (L63, gating) simultaneously requires the charter to state *"a conditional lens is **included only when its trigger fires**."* Both criteria pass on text presence, and the artifact ships **self-contradictory**: it asserts a composition rule that is false of the very document the reader is holding. Worse, the rule has no implementer. In guarded-change, `stage-3.md` L6–9 is the assembler that performs the selection. Architect has **no assembler** — `Architect.md` contains zero occurrences of "charter", "prompt", "lens", "assembl", or "conditional", and `Spawn_redteam(_task,_plan,_granularity)` (L24) describes no composition step. This is the **same defect class D12 exists to kill** (a rule pointing at machinery Architect does not have), created by the pass-2 fix for the B19 miss. Note the fork source's own conditional bullets are written **self-triggering** ("*If* the change touches a position-sensitive assembly…", L80) — reviewer-side evaluation, which Architect *can* do; it is the assembly-side clause that has no actor.

**D-F04 (major).** `0-baseline.md` **L253** (D3′) restates the closed set as *"…plus **whatever review-context paths your caller supplies**."* That is not a closed set — it is an open delegation. B15's enforcement teeth are the pairing *"any supplementary author-authored context must be **quoted in the record as such**"* + *"a record missing any of these ⇒ **un-run**"* (fork source L74–79). Under D3′'s phrasing, anything the caller hands over is in-set **by definition**, so no context can ever be the "supplementary author-authored context" that must be quoted — the un-run sanction becomes unreachable. `1.5-criteria.md` **C-11** (L52) checks "positive assertion per element", which passes on the vague text. Pass 1's D3 failed by asserting an input a 2-arg signature cannot supply; D3′ correctly drops the parent's plan, but resolves the residue **by making the set open**, which is a different defect at the same rule. This is the "dodge by vagueness" the prompt asks about, and my answer is: on the parent's-plan half, no dodge — genuinely fixed; on the review-context half, yes.

**D-F07 (major).** `decisions.md` **L224–228** and `2-plan.md` **L191–193** track the iteration cap for **exactly one** finding class: `{gate 4 · 1.5-criteria.md position criterion}`. SEV4 (`stage-4.md` L38–48) defines the class as *"same gate (by stage number) + same targeted artifact section, regardless of wording"* and requires counting per class — and pass 1 produced **seventeen** findings across at least eight distinct artifact sections. Concrete failure: my finding D-F05 below is a second bounce at gate 4 on the class `{gate 4 · 1.5-criteria.md Part B arm run-count/pass rule}` (pass 1 = B-F08, "n=1 with an unbounded self-administered rebuild"). Under SEV4 that **trips the cap** and stops the loop for a human tie-break — but the log has no counter for it, so the trip is invisible and the loop would route to stage 2 unbounded. The cap's own anti-livelock guarantee depends on `decisions.md` (`stage-4.md` L89–95: *"the **iteration cap depends on it**"*) and the log implements one-seventeenth of it.

**D-F17 (minor).** `1.5-criteria.md` **C-02b** (L40) and `2-plan.md` **§2.2** (L70–74) describe `forkdiff.sh` as *"diff the shipped charter against the frozen fork source, strike out every matched rule span, and **list the residue**. Every residue line is either an Architect addition named in the provenance blockquote, or a finding."* That sentence describes only the **shipped-only** residue direction (additions). The baseline's own regression definition is the *other* direction — *"Regression = a **CARRY rule that stopped being stated**"* (`0-baseline.md` L15). `2-plan.md` L72–74 claims *"Had it existed in pass 1 it would have surfaced B19"*, which is true **only** in the fork-only direction. The instrument's stated contract does not include the direction that implements the regression bar it is being built to serve.

**D-F18 (minor).** `2-plan.md` **§8 R4** (L212): if B-5/B-6 return "no effect", *"C-17/C-23 would then be reported as unsupported design claims and the block order revisited — not quietly passed."* But C-17 and C-23 are **gating** and, per `2-plan.md` L118–119, *"satisfied **only** by B-5 and B-6"*. A gating criterion at `verified = no` blocks "done" (H5/H7, `stage-8.md` L42–53, L86–100). So the actual route is a stop-for-human / named risk-acceptance, not "revisit the block order." The plan names the risk and then mis-routes it.

---

## Lens 3 — Missed opportunity

1. **Make B19 implementable instead of contradictory.** D3′ already establishes that the caller supplies review context. The two conditional lenses could be delivered as a **caller-supplied appendix** rather than stated in the core — which makes *"included only when its trigger fires"* literally true of the assembled prompt and dissolves D-F03 at no cost in carried substance.
2. **Split the replication and model axes in Part B.** The current design (2 runs, 2 models, 1 run per cell) achieves neither replication nor model-control (D-F05). A 2×2 (two models × two runs each, 4 agents/arm) at the same total budget for **four** criteria instead of seven would produce an answer that can distinguish "no effect", "effect", and "effect, model-dependent" — the third being the most likely truth and the one the current design can only report as `verified = no`.
3. **Give `forkdiff.sh` the fork-only direction as its primary output** (D-F17) — it is the cheaper half and the one that implements the regression bar.
4. **Pin the relocation destination in B-5/B-6** (D-F15) as a line index in the diff, not prose.

---

## Lens 4 — Unstated assumptions & risks

*(Position lens fires and is exercised in the coverage challenge below; concurrency lens — I challenged the revised Part D premise and it holds: `Architect.md` L26–33's one-writer-per-node memo rule is correctly cited and does bound Architect's own model, and this run's per-arm record paths are genuinely distinct. No finding.)*

**D-F05 (major).** `1.5-criteria.md` **L75–91**. The pass rule is *n = 2, both runs within an arm must agree, and the arms must differ*; **L88–89** then pins *"Each arm's two runs use **two different models**"*. Consequences the plan does not state:
- Each `(arm, model)` cell holds **exactly one run**. Run-to-run variance and model variance are therefore **inseparable** — the stated purpose ("so a HOLED/INTACT difference cannot be a model difference") is not achieved.
- Requiring within-arm agreement **across two different models** converts the stability check into a **model-invariance** check. A real position effect that model A exhibits and model B does not is recorded as "instability" ⇒ `verified = no`. The design is structurally biased toward false negatives, and cannot represent "effect present, model-dependent" at all.
- `stage-1.5.md` **ST1.5d L72–75** governs exactly this case: *"Where the effect is probabilistic (recency/precedence usually shift a **rate**, not flip a switch), the criterion states **the pass rate it expects and the number of runs that establishes it**… rather than relying on a single probe."* Part B states **no pass rate**. n=2 with a unanimity rule is not a rate. The pass-1 blocker was a position criterion whose arm did not vary the position; the pass-2 arm varies the position but the *statistic* still cannot establish the probabilistic effect ST1.5d says this is.

**D-F06 (major).** The rebuild bound (`1.5-criteria.md` **L82–86**; `2-plan.md` **L134–136**) bounds **rebuilding the fixture/charter**. It does not bound **re-spawning the runs**. Cold agents are nondeterministic; nothing in Part B or §4 requires that every run performed be recorded, and the record path scheme `records/<criterion>-<arm>-<run>.md` (`2-plan.md` **L150**) has **no generation slot** — a re-spawn of B-5/HOLED/run-1 writes to the same path and overwrites its predecessor. Concrete scenario: B-5 returns "arms agree" (position inert, killing the fix for pass 1's blocker); the runner re-spawns run 1 of each arm rather than declaring a rebuild; the third sample discriminates; `decisions.md` shows zero rebuilds and four records. This is attempt-1 failure mode #6 (`ATTEMPT-2-STATE.md` §8.6, *"a gate satisfiable by the party it constrains"*) surviving intact in the very clause written to kill it. The bound is a real constraint on the **artifact** and a **formality** on the **sampling**.

**D-F15 (minor).** `1.5-criteria.md` **L106** specifies B-5's HOLED arm as the charter *"with the floor block **moved to after the six lenses**."* The **destination is not pinned**. "After the six lenses" spans blocks 5–10 of `2-plan.md` §1.1. If the floor lands at the tail it also displaces B18, and B-5 silently becomes a B-6 ablation — confounding the two arms that jointly carry the blocker fix. Separately, `1.5-criteria.md` **L97–98** requires *"Where a **deletion** changes a neighbour's adjacency, that is stated in the record as a known confound"* — the duty is scoped to deletions, but a **relocation disturbs adjacency at two sites** (origin and destination) and is therefore strictly more adjacency-disruptive than a deletion. The hygiene rule exempts exactly the arms (B-5, B-6) that need it most.

**D-F16 (minor).** Constraint C4 (`1-spec.md` L97–100) binds `2-plan.md`, and both documents open with tense notices claiming compliance (`1.5-criteria.md` L5–8; `2-plan.md` L7–9). Both then describe unbuilt instruments in the **present tense**: `1.5-criteria.md` **L136** (*"`oracles/mutation-test.sh` **generates** mutants"*), **L148–150** (*"**It refuses** to run with no argument and **returns** a usage exit code"*), **L138** (*"The mutant set **includes** ≥1 mutant"*); `2-plan.md` **L70–71** (*"**Diffs** the shipped charter…, **strikes** every matched rule span, and **lists** the residue"*), **L78–79** (*"**Refuses** to run with no argument"*). Attempt-1's iteration cap tripped on exactly this (`1-spec.md` L98–99), and it is `ATTEMPT-2-STATE.md` §8 failure mode #1.

---

## Lens 5 — Fidelity

**Not clean.** Loaded operational terms pinned:

| Term (where it appears) | Mechanism it must be pinned to | Does the plan implement *that*? |
|---|---|---|
| **"the human tie-break"** (S14, `1-spec.md` L140; C-08, L48) | a human able to receive and rule on a *severity* inside Architect's loop | **NO** — `Architect.md`'s only human call is `Human_gate(division, task, depth)` L16, which takes a split and fires only at `depth <= gate_depth`. D-F01. |
| **"a logged `decisions.md` entry"** (S14) | a gate log in Architect | **NO** — no such artifact in `Architect.md`. D-F01. |
| **"the two callers"** (S12) | `Spawn_redteam` L24 and `Divisible` L14 | **YES** — both named, both aimed (C-14), and B-7 finally gives the second caller execution. Correct. |
| **"granularity floor"** (S3) | `Architect.md` L1–8's three bounds: Divisible depth, Spawn_leaf step size, Spawn_redteam vagueness | **PARTLY** — bound (3) gets B-1/B-5; bound (1) gets **nothing** behavioral. D-F08. |
| **"3 independent cold agents"** (S13) | three separately-spawned subagents, `Architect.md` L100–103 | **YES**, and D6's "none with each other" strengthening is correctly declared author-owned. |
| **"the charter is given verbatim / a conditional lens only when its trigger fires"** (S17) | an assembler that composes the reviewer's prompt | **NO** — no such component exists in `Architect.md`. D-F03. |
| **"`Union` performs the citation spot-verify"** (S15) | `Union` (`Architect.md` L20) | **Placement yes** — but the *disposition* has no actor and no appeal path. D-F10. |
| **"the reviewer's severity routes"** (S14/SEV3) | `Severity()` L22 consuming a reviewer-assigned severity | **YES** — `Architect.md` L22/L24 support this half. |

**D-F10 (major).** S15/D11/**C-12** (`1.5-criteria.md` L53, gating) ships a rule that *"a finding whose citation does not resolve is **marked unsubstantiated and does not pass to `Severity` as blocker|major**."* This is a change to **loop-termination semantics**: `Architect.md` L106 (`task = Severity(Union(...))`) is the loop's only driver, so a finding demoted below blocker|major is silently removed from the next task. The author correctly declares this disposition an **unratified elaboration** (RAT2, `1-spec.md` L199). But it still ships as a gating criterion, and **no criterion observes its false-negative behavior**. Concrete scenario: a reviewer files a genuine blocker citing `Architect.md L24`; the resolver expects the absolute path `/home/zero/Documents/Architect.md`; the citation does not resolve; the blocker is marked unsubstantiated and never becomes a task. With D-F01 unfixed there is **no human in the path** to contest it, and per D-F01 the demotion rule that would govern this is inert. C-12 checks only that the sentence is present.

---

## Pass-1 fix audit — required section

| Pass-1 finding | Claimed fix | Does it close? |
|---|---|---|
| **BLOCKER (2/3)** — C-17's executed half varied the fixture, not the position | arm **B-5**, relocating the floor block | **CLOSED, with a caveat.** B-5 genuinely varies the property C-17 governs: HOLED = floor after the lenses, INTACT = floor before. The relocation *does* change adjacency at two sites, but C-17 makes no recency-vs-adjacency distinction, so the arm tests exactly what the criterion asserts. Owner-prescribed at record 1449 item 1, verified verbatim. **Caveat:** destination unpinned (D-F15, minor), and the *statistic* still cannot establish a probabilistic effect (D-F05, major). |
| **Charter-composition rule missing from inventory (3/3)** | **B19** + independent probe **C-02b** | **CLOSED as an inventory fix**, and C-02b is the right structural answer (the checker's probe set no longer shares a source with the claim). **But the carry created a new defect** — D-F03 (major): the rule as stated has no implementer and contradicts block 7. And C-02b's residue direction is stated one-way (D-F17, minor). |
| **Mutation test tautological** | semantic + insertion mutants (Part C) | **CLOSED.** C-M1's four mutant shapes (negate / swap actor / move out of governing section / weaken to hedge) genuinely distinguish "probe matches a rule" from "probe matches a phrase"; C-M2 correctly identifies **insertion** as the defined mutant for an absence sweep, refuting B's "no possible mutant shape" claim; C-M3's negative control forces the harness to be observed printing a non-kill. This is the strongest fix in the pass. |
| **Arms n=1, unbounded self-administered rebuild** | n=2, within-arm agreement, one-rebuild bound | **NOT CLOSED — relabelled.** n=2 with cross-model within-arm agreement cannot establish a probabilistic effect and biases to false negatives (D-F05); the bound constrains fixture rebuilds but not re-sampling (D-F06). Filed at the original severity (major). **This is a second bounce at gate 4 on the class `{gate 4 · 1.5-criteria.md Part B arm run-count/pass rule}` and trips the SEV4 cap.** |
| **D3 granted `Divisible` an input its 2-arg signature cannot supply (3/3)** | **D3′** | **HALF CLOSED.** The parent's plan is genuinely dropped, the reasoning is correct, and the seam is correctly justified as derivable from `Divisible`'s own return (L14) and already presented by `Human_gate` (L16). But the review-context half is resolved by making the set **open** (D-F04, major). |
| **C-18's advisory reason covered 1 of 3 sub-clauses (3/3)** | split into C-18a (gating) / C-18b (advisory) | **MOSTLY CLOSED.** Two-thirds correctly promoted to gating. C-18b's remaining reason does not survive its sibling's own argument (D-F14, minor). |
| **CHANGE class's "difference declared" half checked nowhere** | **C-03b** | **CLOSED.** C-03b requires the provenance blockquote to state, per CHANGE rule, what differs — and `2-plan.md` §1.3 (L49–55) enumerates the three CHANGEs concretely. Correct fix. |
| **B18's terminal position displaced (2/3)** | **D9** + arm **B-6** | **CLOSED in intent.** D9 is correctly declared an author decision under the position lens, and B-6 tests it by execution rather than assertion. Inherits D-F05/D-F06/D-F15. |
| **`Divisible` caller had zero behavioral verification (3/3)** | arm **B-7** | **PARTLY CLOSED.** B-7 exercises **one** of C-14's four aiming clauses (whole-task coverage). The other three — seam soundness, *neither half below the floor*, real joint vs. arbitrary cut — remain text-presence only. D-F08 (major). |

**Verdict on the fix set:** six of nine genuinely closed; one (n=2/rebuild bound) relabelled rather than removed; two (B19 carry, D3′) closed one defect and opened another.

---

## Coverage challenge (CH8) — required section

Behaviors this change could plausibly alter that **no criterion observes**:

**D-F08 (major) — the floor's *depth-bounding* duty is behaviorally unverified.** `Architect.md` **L3–4** names three things the floor bounds and says *"all three are needed"*; **(1) is `Divisible` — how deep the tree goes.** B-1 and B-5 test bound (3) (`Spawn_redteam` vagueness). B-7 tests only orphaned-remainder coverage. **No criterion observes whether the charter's `Divisible` aiming actually makes a split-reviewer reject a half that falls below the floor.** Scenario: the shipped charter's `Divisible` aiming is worded so the split-reviewer approves a division whose second half sits below the floor; `Divisible` returns it (L14 returns after its red-team goes quiet); `Node()` recurses (L88–89); the subtree over-decomposes; with **no backstop cap** (record 1258, verified) this is the Manual Samuel non-termination path record **1128** exists to prevent. C-14 checks the sentence is present. Blast radius: loop termination.

**D-F09 (major) — dilution is tested for exactly one rule.** D9 (`0-baseline.md` L264) accepts the premise that *"the charter **adds** four aggression-licensing sections"* and that this dilutes a rule by displacement, and builds **B-6** for B18. The premise generalizes: the charter roughly doubles the fork source (103 lines → the draft is already 163, and the plan adds a ~30-line RAT block, a severity table, a callers block and a composition rule). **No criterion observes whether any *other* carried rule loses efficacy in the longer document.** Scenario: B12/B13's earned-clean duties (the guards against rubber-stamping — the loop's founding failure) now sit mid-document behind the RAT block; a reviewer reaching them skips the pin-the-terms step; **C-02 passes** because the text is present — which is precisely the *"all the information is still present"* verdict the position lens declares **not** a clean verdict (fork source L88–90). C-19, which measures length, is **advisory** and observes no behavior. Per CH8 this is unmeasured blast radius; the honest remedy is to declare it, not to build twenty arms.

**D-F03 (also a coverage gap) — no criterion observes a conditional lens *standing down*.** Every arm tests a rule firing. Nothing tests a reviewer correctly *not* firing the position or concurrency lens on a plan with no position-sensitive assembly. In a loop where findings become the next task with no cap (L106, record 1258), a **false-firing** conditional lens is a non-termination path with the same shape as finding-inflation — the risk B-6 exists to measure for B18.

**D-F10 (also a coverage gap)** — the `Union` spot-verify disposition's false-negative behavior, above.

**Fragmentation of the discipline block — noted, not filed separately.** The fork source states B08–B19 as **one contiguous list** (L36–L101) terminating immediately before B18 (L103). `2-plan.md` §1.1 splits it across blocks 5, 6, 7 and 8, inserting ~30 lines of RAT between the discipline bullets and the conditional lenses. §1.1 (L34–38) declares the eight untested placements *"ordinary editorial judgement"* — yet rows 2, 8 and 9 give **behavioral** reasons for their positions (*"Establishes what the reader is before telling it what to do"*; *"After the findings-producing material: it is what the reviewer does with what it found"*; *"Aiming lands adjacent to the reviewer's task framing"*). A behavioral reason for a placement **is** a position claim. This is BL-1's shape at lower stakes. I record it as part of D-F09 rather than as a separate finding, since the remedy is the same: either delete the behavioral rationales or declare the blast radius.

---

## Label audit (CH9/CH10) — required section

**Not clean.** Per gating criterion, the governed path I confirmed would be exercised and the evidence checked:

| Criterion(s) | Governed path | Would the planned verification exercise it? | Evidence I checked |
|---|---|---|---|
| C-01, C-03, C-03b, C-04, C-05, C-06a, C-07, C-09a, C-10, C-11, C-13, C-15, C-16a, C-21 | **text presence at a named site** — for these, text presence *is* the governed path | **Yes.** Positive per-site assertion on normalized text is the correct instrument, and C-M1's semantic mutants make the probes rule-checking rather than phrase-matching. | `2-plan.md` §2.3 L76–88; `1.5-criteria.md` Part C L134–139; ST1.5f `stage-1.5.md` L40–48 |
| C-02 + C-02b | fork fidelity | **Yes for C-02**; **partially for C-02b** — residue direction stated one-way (D-F17) | `0-baseline.md` §0.3; `2-plan.md` §2.2 L68–74 |
| C-06b, C-09b, C-16b | absence | **Yes** — paired + normalized + insertion mutants (C-M2). Correctly designed. | `1.5-criteria.md` L137; `stage-8.md` H6 L78–84 |
| **C-08** (demotion rule) | **a human tie-break actually reachable on a severity dispute** | **NO — proxy.** Verified only by text presence against `stage-4.md` L34–36. The governed path cannot be exercised because it does not exist (D-F01). CH9 names this exactly: *"an inspection standing in for an execution."* | `Architect.md` L16, L22, L24, L79; grep for `decisions`/`orchestrat`/`halt` in `Architect.md` = 0 relevant hits |
| **C-12** (`Union` spot-verify) | a citation actually failing to resolve and the finding actually being withheld from `Severity` | **NO — proxy.** Text presence only; no arm, no fixture, no false-negative observation (D-F10). | `1.5-criteria.md` L53; `Architect.md` L20, L22, L106 |
| **C-14** | four aiming clauses for `Divisible` | **PARTIAL** — B-7 exercises one of four; the floor clause (the safety-critical one) is text-only (D-F08). | `1.5-criteria.md` L55, L108; `Architect.md` L3–4, L14 |
| **C-17, C-23** | reviewer behavior under a *varied* position | **Yes on the variable, no on the statistic** — B-5/B-6 now vary position (blocker fix good), but the pass rule cannot establish a probabilistic effect (D-F05) and the destination is unpinned (D-F15). | `1.5-criteria.md` L59, L66, L75–91, L106–107; ST1.5d `stage-1.5.md` L62–75; H3 `stage-8.md` L25–31 |
| **C-20** | the composition rule being true of the assembled prompt | **NO — the rule is false of the artifact that states it** (D-F03). Text presence passes regardless. | `2-plan.md` L29; `1.5-criteria.md` L63; `Architect.md` grep = 0 hits for assembly vocabulary |
| C-18a, C-22, C-24 | absence over a known vocabulary | **Yes** for C-18a and C-24. **C-22 narrower than its own claim** — it sweeps `stages/*.md` and "(below)"-style referents, but the charter's tier-(i) duty points at *"the universal spine"*, an **unbuilt sibling element** (element 2). C-22's *"Fixes the class, not the instance (D5)"* does not cover that instance. Partially mitigated by C-18a's "by role" phrasing. **Minor** (D-F13's sibling; I fold it here rather than filing separately). | `1.5-criteria.md` L60, L65; fork source L33, L37, L79; `Architect/guarded-change.architect.md` build table L23 |
| C-M1…C-M4 | the checker's own ability to fail | **Yes.** Correctly rebuilt. | `1.5-criteria.md` L134–150 |
| B-1…B-7 | reviewer behavior | **Yes on the variables**; **no on the sampling design** (D-F05, D-F06) | `1.5-criteria.md` L75–108; `2-plan.md` §4 |

**Advisory labels challenged (2 of 26):**
- **C-19 (length).** Reason: *"no defensible numeric threshold exists pre-build and there is no baseline reviewer-cost measurement; inventing one would be the guessed metric this loop refuses."* **Legitimate** — this is exactly `stage-1.5.md` ST1.5a's degraded mode used honestly, and the number is still reported.
- **C-18b (no Layer-2 config field list).** **D-F14 (minor) — the reason does not survive its sibling's argument.** Stated reason: *"element 3's config contract does not exist, so a mechanical bar would measure against an unwritten sibling."* But C-18b is an **absence sweep over the charter's own text**, not a check against the sibling — and the criteria doc justifies its sibling C-18a as *"absence sweeps over a **known vocabulary**, mechanizable today against `Architect/templates/seed/` which exists on disk"* (L60). The identical argument is available: `Architect/guarded-change.architect.md` is a Layer-2 config, is on disk, is in this run's closed set, and enumerates the field vocabulary (`redteam_context`, `measurement`, `baseline`, `check`, `metrics`). The spine's *normative* section list is element 2 and equally unbuilt, yet C-18a was promoted to gating. The asymmetry is unjustified, and it carves a third off *"the **only** criterion guarding the project's #1 named historical failure mode"* (L60).

---

## Ratification audit (CH11/CH12) — required section

I read record **1449** directly (`sed -n '1449p'` → JSON `message.content`) and, additionally, the **escalation that record 1449 answers** — record **1445**, the orchestrator's message to Roy. Reading 1445 is what RAT1 requires and what §9 does not do: RAT1 demands *"the flagged axis + **the options presented, verbatim**"* (`stage-3.md` L58–59).

**Spot-verified owner quotes (≥2 required; I did 7):** records **1449** (all five items, character-exact including the asterisks in item 3), **1128**, **1148**, **1175**, **1258**, **1274**, **55** — all character-exact against `decisions.md` L41–47 and `1-spec.md` §2–§3. Record **51** read to confirm the B-F04 correction. **Zero fabricated quotes. The owner's *words* are recorded honestly throughout.**

**D-F02 (major) — the options are paraphrased, not verbatim, and for R-2 the paraphrase strips the axis.**

`1-spec.md` §9 (L186–188) claims each record is *"in RAT1's own shape — flagged axis, options presented, owner's verbatim response…"*. The responses are verbatim. The **options are compressed paraphrases** of record 1445. Compare:

- **R-2 as recorded** (`1-spec.md` L198): *"(a) drop it; (b) add a human-interrupt to the spec; **(c) reviewer-facing discipline only**"*
- **R-2 as actually presented** (record 1445): *"**(c)** keep it as reviewer-facing discipline **with no human actor named**"* — preceded by the framing sentence *"But `Architect.md` gives exactly one human call — `Human_gate(division, task, depth)` — which takes a split, fires only at depth ≤ 2, and can't receive a severity. **With no backstop cap, there's no path for a severity dispute to reach you at all.**"*

The clause the paraphrase drops — *"with no human actor named"* — **is the flagged axis**. The escalation's question was not "what text should the rule be", it was "**is there any path for a severity dispute to reach you**". The owner's answer, *"It gets implemented however it is implemented in guarded-change; that is what the instruction was: copy over the severity mechanism from guarded change,"* selects **what text to port**. It says nothing about the reachability of the human. Under RAT1 that is the textbook **adjacent answer**: *"a ruling built on a **partial or adjacent** owner answer that does not disambiguate the presented options… is **not ratified**; the axis must be **re-asked**, not defaulted"* (`stage-3.md` L63–66). §9 instead records it as *"**Ratified.** Disambiguates the axis."*

**CH12/RAT2 on R-2's elaboration.** D10 (`0-baseline.md` L265) then adds an operative commitment absent from and not entailed by the owner's words: *"the human named is the same human the loop already stops for, reached through the delegated-runner halt path (RAT3)."* This is **unratified inflation**, and it is also **false** (D-F01): RAT3 binds a subagent running *guarded-change* (`METHODOLOGY.md` L214–217, *"The subagent* is *running this skill, so this half is binding here"*), which Architect's `Spawn_redteam` agents are not. The claim *"**Resolves** the pass-1 finding A-F4/B-F11"* is therefore unsupported, and `1.5-criteria.md` C-08 (L48) repeats it as settled.

Per `stage-4.md` L52–69, an escalated fidelity finding *"counts as **resolved** for routing **only if** its ratification record passes the stage-3 audit"*; where the elaboration inflates, *"the finding **stands at its escalated severity** and the loop **stops for the human to re-ask** the unresolved axis."* **H-A stands at major and the axis must be re-asked**, in the form the owner was never actually shown: *"guarded-change's demotion rule requires a `decisions.md` entry and a human tie-break; Architect has neither. Do you want (i) a human interrupt added to `Architect.md`, (ii) the rule shipped as reviewer-facing discipline with the absence of a human actor stated plainly, or (iii) something else?"*

**Answering the prompt's pointed question about R-3 and R-4:**

- **R-4 is correctly and conservatively classified.** *"I don't know what the fuck rat1/2 even ARE"* selects nothing on the flagged axis (record 1445 item 4 offered inline / one-line-summary / an-element-I-don't-know-about). Treating it as a **non-answer** and D12 as an author decision claims *less* authority than the author could have. This is the run doing RAT1 correctly, against its own interest. **No finding.**
- **R-3's self-classification is honest on the part it flags and slightly overstated on the part it does not.** The ⚠ RAT2 declaration on the disposition mechanism is correct and creditable. But the *placement* mapping does one silent step more than the owner's words: the owner named **`Combine`**, and the author's own parenthetical concedes `Combine` *"later split into `Consensus` + `Union`"* — **two** functions, **both** of them merge steps (`Architect.md` L18 `Consensus` merges plans; L20 `Union` merges issues). "The duty stayed with the merge step" is an author inference. It is a *well-supported* inference (citations attach to findings, and findings flow through `Union`), but §9 records it as the owner's words selecting the option. **Minor**, folded into D-F02: declare it as an inference.
- **The convenient self-classification is neither R-3 nor R-4 — it is R-2**, which is the only one of the five recorded as fully "Ratified / disambiguates the axis" while resting on an answer adjacent to the axis, and the only one carrying a resolution claim the source contradicts.

**R-1 and R-5 audit clean.** R-1: the owner's words prescribe the fix directly (*"the experiment should actually try moving the floor"*) and reject the escalation; the mapping to "proceed, and here is the fix" is sound, and D14's escalation-standard consequence is a legitimate reading of *"That wasn't a call that warranted my attention at all."* R-5: *"That thing was for the old version, discard it"* against record 1445 item 5's *"In or out?"* — unambiguous **out**; X6/D13 correctly record it as **declined, not overlooked**, and §0.6's withdrawal of the F7 prop is the honest consequence.

**Pre-existing rulings (55, 1128, 1148, 1175, 1258, 1274):** all verified character-exact. The self-raised RAT2 finding on **1175** (the ratification covers *including the three-tier definition*, not *lens-vs-bullet placement*) is **correct**, and D1's declaration as author-owned is right. `decisions.md` L56–57's additional observation — that at record 55 the owner wrote *"not sure what you mean by lens though"* — is verified and genuinely strengthens the case for keeping D1 author-owned.

---

## Unverifiable claims I could not check

1. **Every Part-A and Part-C result.** `oracles/check.sh`, `mutation-test.sh`, `forkdiff.sh`, `rules.tsv` and all fixtures do not exist; both documents declare this. I audited their *designs*, not their behavior. Correctly `verified = no` per H6 by the plan's own ordering constraint.
2. **The pass-1 reviewer records.** `records/reviewer-{A,B,C}-verbatim.md` and `3-redteam-plan.md` are **not in my closed set**, so I could not confirm that the carried-forward finding list is complete or that finding IDs (A-F3, B-F08, C-FID-1, …) are labelled as the reviewers wrote them. I audited each claimed fix against **source**, which is the stronger check, but I cannot certify that no pass-1 finding was dropped from the carry-forward. Given SEV4 requires carrying prior findings forward *"so the next reviewer confirms they were addressed rather than re-deriving"*, this omission from the closed set is worth fixing for pass 3.
3. **Model availability for the pinning scheme.** `1.5-criteria.md` L88 requires two distinct models per arm. I cannot verify the runner can actually spawn two models, nor which two.
4. **Whether `templates/seed/`'s current contents are element 2's output or attempt-1 residue.** The config's build table (L23) says element 2 is *"not started"*, yet the directory holds four files. C-18a's mechanizability rests on this directory; I confirmed it exists but not what it represents.
5. **The 28-agent budget's feasibility.** Stated plainly (a virtue), but I have no basis to judge affordability, and R2 correctly identifies quiet reduction as the risk.

---

## Findings table

| # | severity | lens | artifact:line | finding | why it matters |
|---|---|---|---|---|---|
| D-F01 | **major** | 5 / 1 | `0-baseline.md`:265; `1.5-criteria.md`:48 | D10's *"reached through the delegated-runner halt path (RAT3)"* is false — RAT3 binds a subagent running **guarded-change** (`METHODOLOGY.md` L214–217), not Architect. `Architect.md` has no `decisions.md`, no gate, and one human call (`Human_gate`, L16) that takes a division, fires at `depth<=gate_depth` only, and cannot receive a severity. | Pass-1 A-F4/B-F11 is **not closed**; the charter ships a rule with no actor — the proxy substitution the fidelity lens exists to catch. |
| D-F02 | **major** | 5 (CH11/CH12) | `1-spec.md`:198 | R-2's "options presented" are paraphrased, not verbatim; the paraphrase strips record 1445's *"with no human actor named"* — **the flagged axis**. The owner's answer selects *what text to port*, not *how the human is reached*: an adjacent answer recorded as "Ratified / disambiguates the axis". | RAT1 requires re-ask, not default (`stage-3.md` L63–66); `stage-4.md` L52–69 says the finding stands at its escalated severity. The run inlines RAT1 as a shipped duty (S16) while failing it on its own record. |
| D-F03 | **major** | 2 / 5 | `2-plan.md`:29; `1.5-criteria.md`:63 | C-20 mandates *"a conditional lens is included only when its trigger fires"* while block 7 ships both unconditionally; and `Architect.md` has **zero** occurrences of charter/prompt/lens/assembl — no assembler exists to perform the selection. | The artifact ships self-contradictory, and re-creates the exact defect class D12 was written to eliminate. |
| D-F04 | **major** | 2 | `0-baseline.md`:253 | D3′'s *"plus whatever review-context paths your caller supplies"* makes the closed set **open**, so nothing can ever be the "supplementary author-authored context" that B15 requires be quoted as such. | Neuters B15's un-run sanction — one of the two enforcement teeth of a CARRY rule. C-11 passes on the vague text. |
| D-F05 | **major** | 4 | `1.5-criteria.md`:75–91 | n=2 with **cross-model** within-arm agreement gives 1 run per (arm,model) cell, so model and run variance are inseparable; requiring cross-model agreement biases hard to false negatives; ST1.5d (`stage-1.5.md` L72–75) requires a stated **pass rate**, which Part B does not give. | The pass-1 n=1 finding is relabelled, not removed. **Second bounce at gate 4 on class `{gate 4 · 1.5-criteria.md Part B run-count/pass rule}` — trips SEV4.** |
| D-F06 | **major** | 4 | `1.5-criteria.md`:82–86; `2-plan.md`:150 | The one-rebuild bound constrains fixture/charter rebuilds but not **re-spawning runs**; the record path `<criterion>-<arm>-<run>.md` has no generation slot, so a re-run overwrites its predecessor. | Attempt-1 failure mode #6 (`ATTEMPT-2-STATE.md` §8.6) survives inside the clause written to kill it — the gate is still satisfiable by the party it constrains. |
| D-F07 | **major** | 2 | `decisions.md`:224–228; `2-plan.md`:191–193 | The cap tracks **one** finding class; SEV4 requires per-class counting and pass 1 produced 17 findings across ≥8 sections. | The cap depends on the log (`stage-4.md` L89–95). D-F05 trips an untracked class, so the trip is invisible and the loop routes unbounded. |
| D-F08 | **major** | 4 (CH8) | `1.5-criteria.md`:55,108 | `Divisible`'s *"neither half below the floor"* duty — bound **(1)** of the three `Architect.md` L3–4 says are all needed — has **zero** behavioral verification; B-7 exercises only coverage. | A split-reviewer that approves a below-floor half over-decomposes the tree; with no backstop cap (1258) this is the Manual Samuel path record 1128 exists to prevent. |
| D-F09 | **major** | 4 (CH8) | `0-baseline.md`:264; `1.5-criteria.md`:62 | D9 accepts that four added sections dilute a rule and tests exactly one (B18/B-6). No criterion observes dilution of any other carried rule in a charter that roughly doubles the fork source; C-19 (length) is advisory and observes no behavior. | C-02's presence check is the *"all the information is still present"* verdict the position lens declares invalid. Blast radius includes B12/B13, the anti-rubber-stamp guards. |
| D-F10 | **major** | 5 (CH8) | `1.5-criteria.md`:53 | C-12's unsubstantiated-citation rule changes loop-termination semantics (a finding demoted below blocker\|major never becomes a task, `Architect.md` L106) and no criterion observes its **false-negative** behavior; with D-F01 unfixed there is no appeal path. | An unratified elaboration (declared as such at D11) ships as a gating rule that can silently discard a real blocker. |
| D-F11 | minor | 1 | `0-baseline.md`:252 | *"`Architect.md`'s **103** lines"* — the file is **115**; 103 is the fork source's count. (The word-absence claim itself is true.) | Recurrence of the class §0.1 already corrected (104→103), in a C5 document whose authority is machine-generated numbers. D5: recurrence means under-generalization. |
| D-F12 | minor | 1 / 2 | `1-spec.md`:71,86 | §4 and constraint **C2** still read *"18 rules (B01–B18)"* after B19 was added; §6 S17 requires B19. | C2 is the run's fork-fidelity constraint and excludes B19 by enumeration. A-F13's defect one document over — the anti-drift fix was applied only to `1.5-criteria.md` C-02. |
| D-F13 | minor | 1 | `0-baseline.md`:97 (B15) | B01–B19 still misses fork source **L69–70**'s *"(the charter instructs the reviewer to report these)"* — an operative duty on the charter, not just on the record. | A charter stating "the record embeds the reviewer-reported sha256" without instructing reviewers to report them yields records missing element (v) ⇒ every review un-run. C-11 passes either way. Same omission-from-a-paraphrase class as B19. |
| D-F14 | minor | CH9 | `1.5-criteria.md`:61 | C-18b's advisory reason (*"would measure against an unwritten sibling"*) does not survive C-18a's own argument: the check is an absence sweep over the **charter**, and a field vocabulary exists on disk in this run's closed set (`guarded-change.architect.md`). | Carves a third off *"the only criterion guarding the project's #1 named historical failure mode"* on a reason its sibling refutes. |
| D-F15 | minor | 4 | `1.5-criteria.md`:97–98,106 | B-5's relocation destination is unpinned ("after the six lenses" spans blocks 5–10); if the floor lands at the tail it also displaces B18, confounding B-5 with B-6. The confound-declaration duty is scoped to **deletions**, though relocation disturbs adjacency at **two** sites. | The hygiene rule exempts exactly the two arms that carry the blocker fix. |
| D-F16 | minor | 1 | `1.5-criteria.md`:136,148–150; `2-plan.md`:70–71,78–79 | Present-tense description of unbuilt instruments, directly under tense notices claiming future/conditional compliance with C4. | C4 exists because attempt 1's iteration cap tripped on exactly this; `ATTEMPT-2-STATE.md` §8 failure mode #1. |
| D-F17 | minor | 2 | `1.5-criteria.md`:40; `2-plan.md`:70–74 | `forkdiff.sh`'s residue is specified one-way (shipped-only additions). The regression bar is the **fork-only** direction (*"a CARRY rule that stopped being stated"*, `0-baseline.md` L15). | The claim *"had it existed in pass 1 it would have surfaced B19"* is true only in the unspecified direction. |
| D-F18 | minor | 2 | `2-plan.md`:212 vs 118–119 | R4 says a "no effect" result means *"the block order revisited — not quietly passed"*, but C-17/C-23 are **gating** and satisfied only by B-5/B-6; `verified = no` on a gating criterion blocks "done" (H5/H7). | The named contingency has no route in §6's table; the real route is stop-for-human / named risk-acceptance. |
| D-F19 | nitpick | 1 | `1-spec.md`:140; `1.5-criteria.md`:48 | SEV2 is cited as `stage-4.md` **L26–28**; the sentence runs to **L29** (*"rules."*). | Substance is faithful; the range truncates mid-sentence in a run whose discipline is exact citation. |

---

## Worst severity

**MAJOR.**

No blocker. The pass-1 blocker (BL-1) is genuinely closed — B-5 varies the position, exactly as the owner prescribed at record 1449 item 1, and the same apparatus was correctly extended to C-23 and C-14. The mutation-test rebuild (Part C) and C-02b are strong, structurally correct fixes. Nothing here says the run is aimed at the wrong problem.

But ten majors stand, three of them re-derivations rather than new ground:

- **D-F01 + D-F02** are the pass-1 H-A finding surviving intact behind a false resolution claim and a ratification record that fails RAT1 on the axis it claims to have settled. Per `stage-4.md` L52–69 this is a **stop-for-human re-ask**, not a route to stage 2.
- **D-F05 + D-F06** are the pass-1 B-F08 finding relabelled. Per SEV4 this is a **second bounce at gate 4 on the class `{gate 4 · 1.5-criteria.md Part B arm run-count/pass rule}`, which trips the iteration cap** — and D-F07 shows the log has no counter that would notice.
- **D-F03 + D-F04** are new defects created by the pass-2 fixes for B19 and D3.

Two of the three stop conditions that fired at gate-4 pass 1 have therefore fired again on different classes. My reading of the correct route is: **stop for the human**, on two independent grounds (the RAT1 re-ask of H-A's axis; the SEV4 cap trip on Part B), rather than a third automatic bounce to stage 2.

I note for the record that I audited the claimed fixes against **source** rather than against the pass-1 reviewer records, which were not in my closed set — see "Unverifiable claims" item 2. Adding `records/reviewer-{A,B,C}-verbatim.md` to the pass-3 closed set would let the next reviewer confirm the carry-forward is complete, which SEV4 requires and which I could not.
