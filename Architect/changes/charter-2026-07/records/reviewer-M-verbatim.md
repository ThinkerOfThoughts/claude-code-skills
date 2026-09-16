# Reviewer M — VERBATIM record, gate 7 (re-scoped element: the agent prompt set)

**Recovered from the harness transcript, not reviewer-reported.** Source:
`/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775/subagents/agent-a9827224f3a66341f.jsonl`

**First-hand identity from the harness sidecar `agent-a9827224f3a66341f.meta.json`:**
```json
{
  "agentType": "general-purpose",
  "description": "Cold red-team M",
  "toolUseId": "toolu_01Hvceze7SFoUDCCSZtbYSE5",
  "parentAgentId": "ab541478bed036f78",
  "spawnDepth": 2,
  "model": "opus"
}
```
**Prompt given (verbatim, embedded per B15):** `records/stage6c-prompt.md`

---

# COLD REVIEW RECORD — Reviewer M

**Gate 7, re-scoped element 1: the Architect agent prompt set**
**Agent type:** `general-purpose` (Claude Code Agent tool, read-only) — **Model:** `claude-opus-5`

---

## §A — Files read, with reviewer-reported sha256

| Path | sha256 |
|---|---|
| `/home/zero/Documents/Architect.md` | `1d3859546f3faf5a85e7ca7c4be4055c539b80eb86963c4743e481c350cee826` |
| `…/Architect/stages/charter.md` | `91c776b807d9655d23093045163c42798b89f5283673f011055be2f250579951` |
| `…/Architect/stages/charter-common.md` | `83bbb01eb42d291205026ede0f1da7ae2e46e5ca159974fbd77e2f0606bc6905` |
| `…/Architect/stages/redteam.md` | `ccb42a9b429390fab504434fc434e79ff12cdbc209c019b3662f00ad7621dcf3` |
| `…/Architect/stages/divider.md` | `f4dfe178a3e948dc1af935745575a9310fb13e9e8093c080dbd7fa1e9c8daf29` |
| `…/Architect/stages/combiner.md` | `7f69e4a731d28df73177e2e2a3de9b8f54060dce4923d028ffd39eae849c62d0` |
| `…/Architect/stages/leaf.md` | `7192e51aa899e3840a6417a0f374e9cad99c59b8b714b30a222dda45485b3f38` |
| `…/Architect/stages/node.md` | `3ff5b2dc8557f28e7ecc72babc7e17ed813ee75c03e6fbeb7b7f6c529351d668` |
| `…/Guarded_change/stages/charter.md` | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` |
| `…/Guarded_change/stages/stage-3.md` | `16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3` |
| `…/Guarded_change/stages/stage-4.md` (L1–40) | `175061c27bb6980ff76c6358d403299d343c409b2952308ffea7485fff880675` |
| `…/Architect/guarded-change.architect.md` | `42f289a51ed4e5f706d3b70bc8ca47a2e8dc16d2aba4f3f3ac76a02d0cb0429c` |
| `…/charter-2026-07/0-baseline.md` | `4872f951c65351d5180f019ca7298ff5ae2c41cd6d43e9d0a9241e10c2e49b4a` |
| `…/charter-2026-07/1.5-criteria-v2.md` | `8a69267fc72a87c6dfe4eb035590a44bad91eca53561f770944f808335401f1c` |
| `…/charter-2026-07/decisions.md` (tail only) | `14d781c5ff80c67fc435141c77fa1c77dfd0f310345feaab34aed7697ad488b5` |
| `…/charter-2026-07/records/repaired-clauses.md` | `882ca630d553e391c00d7662d834164e6e46d79bf554c7c118999573adf7f4c0` |
| `…/charter-2026-07/records/stage6c-prompt.md` | `affab6a701c24070b01768b776e533185dcbf6361a27295a8f080c1ad1a0fa68` |
| Session transcript `45cb99a2-…-0775.jsonl` (records 1175, 1258, 1449) | `f44ccfc3ee99b0a13ef119e9415abe07c954221846a2536cbbd688954129fc50` |
| `…/Dragonfly/stages/charter.md` (hashed, not read) | `c5d1e2068f35760e373517e243003800c264c64bf3d93d6d8ea6b951990af870` |
| `…/Architect/ATTEMPT-2-STATE.md` (grepped, not read in full) | `5a42e9d4bdadd46c3bed9763c16763aec9a190f6558845789720e45e5cabb40d` |

Supplementary author-authored context, quoted as such: the six artifact files, `stage-3.md`/`stage-4.md`, and the run folder — all declared as supplementary in §5 of the prompt I was given. No other supplementary context was supplied to me.

---

## §B — Findings

### **M-F1 — `blocker` — `Consensus` is instructed to refuse and escalate on the spec's *ordinary* two-child merge path**

`combiner.md:32-35`:
> *"'2-of-3' presumes **three** plans. If you were given fewer than three, **there is no majority to take.** Do not invent a merge rule and do not silently pass one input through as the winner. Report that you cannot take a majority over the vector you were given, name the count, and reach the owner via `Ask_human`."*

`~/Documents/Architect.md:91-97` spawns **exactly two** children and then calls `plan = Consensus(child.get_plans)`. `node.md:55-58` faithfully mirrors this: *"spawn **two child nodes** … and set `plan = Consensus(child plans)`."*

**Consequence:** every divisible node, on every iteration, calls `Consensus` with a vector of 2. Under `combiner.md:32-35` the combiner must refuse to merge and block for the owner. The entire non-leaf half of the tree becomes an owner-blocking error path. The set contradicts itself (`node.md:56` vs `combiner.md:33`) and contradicts the spec, which calls `Consensus` on two plans unconditionally.

The stated limit is correct *as an observation about leaf merges with a dead leaf*; it is wrong as an unconditional rule. The author's disclosure of this as an invention (per my brief) does not cover the case that it fires on the design's normal path — and I could not locate the disclosure anywhere in `changes/charter-2026-07/` or `ATTEMPT-2-STATE.md` (`grep -rn "fewer than three\|two child"` returns nothing there).

---

### **M-F2 — `blocker` — the composition rule is violated as a *pattern*, and two manifest claims about it are false**

`charter.md:71-76` asserts: *"Role files are additions only, and never restate a rule the common core states… nothing is duplicated, so there is nothing to sync."* `charter.md:86-90` declares **one** duplication (B18). Both claims are false. A mechanical sentence/n-gram overlap sweep across the six files finds:

**Restatements of a common rule inside a role file (forbidden by `charter-common.md:18`):**

| # | Common core | Role file restating it |
|---|---|---|
| a | `charter-common.md:70-71` — *"blocker and major become the next task and are re-planned. minor and nitpick are recorded against the plan but not looped on"* | `combiner.md:71-72` — *"They become the next task and are re-planned. `minor` and `nitpick` are recorded against the plan and not looped on"* (8-gram-identical span) |
| b | `charter-common.md:76` — *"A finding one reviewer caught is signal."* | `combiner.md:40` — *"**A finding one reviewer caught is signal**"* (verbatim). Note `1.5-criteria-v2.md` N-19 allocates to `combiner.md` only *"discard nothing, dedup only exact restatements"* — this restatement exceeds even the criteria's own allocation. |
| c | `charter-common.md:100` — *"Everything else is supplementary author-authored context and must be quoted in your record as such."* | `redteam.md:16` **and** `combiner.md:18` — *"Anything else is supplementary and is quoted in your record as such."* (identical sentence in two role files) |

**Role-file clauses that contradict or widen a common rule** (each also filed separately below for its own consequence): M-F3 (`redteam.md:104-117` vs `charter-common.md:22-23`), M-F10 (`combiner.md` has zero floor content vs `charter-common.md:41,56`), M-F13 (`redteam.md:14`/`divider.md:16`/`combiner.md:16` widen `charter-common.md:96`).

Per my brief's rubric — *"One real instance is a `major`; a pattern is a `blocker`"* — six instances across four of the five role files is a pattern. The load-bearing claim of the split ("nothing is duplicated, so there is nothing to sync") does not hold on the shipped text.

---

### **M-F3 — `major` — the set states B19's conditional-inclusion rule but its file structure cannot implement it**

`charter-common.md:22-23` (given verbatim to every agent):
> *"A conditional section is present only when its trigger has already been judged to fire. If you are holding one, you do not re-litigate whether it applies."*

But composition is *`charter-common.md` + the role file* (`charter.md:60-67`), and **both** conditional lenses live inside the single monolithic `redteam.md:104-117`. There is no mechanism to include one and not the other. Every red-team agent therefore holds both, always — and `redteam.md:106` and `:113` then restate the firing conditions inline (*"Fires only where…"*), instructing the reviewer to do exactly the re-litigation `charter-common.md:23` forbids.

This is baseline decision **D8** (`0-baseline.md:263`, *"a conditional lens is stated in the charter with its trigger, and is **given** to a reviewer only when that trigger fires"*) stated but not built. Concrete consequence: a plan node with no shared mutable state ships with a concurrency lens its reviewer is told not to question, findings become the next task (`Architect.md:110`), and there is no backstop cap (owner record **1258**, verified) — the exact regress the floor exists to prevent.

---

### **M-F4 — `major` — `Ask_human` is uncallable by four of the six roles it is offered to**

`Architect.md:18`: `string Ask_human(string _question, string _node_id, int _depth);` — and the spec's own prose frames it as *"The node sends _question to the ORCHESTRATOR."* `charter-common.md:109` faithfully restates the three-argument signature.

`node_id` and `depth` appear in exactly one closed set: `node.md:17`. They are absent from `redteam.md:14`, `divider.md:16`, `combiner.md:15-16`, `leaf.md:26`.

Yet the escape hatch is offered to non-node roles twice:
- `charter-common.md:19-20` — *"file it as a finding (if your role produces findings) or **reach the owner via `Ask_human`** (if it does not)"* — i.e. addressed precisely to leaf and combiner, the two roles that cannot call it;
- `combiner.md:35` — the M-F1 escalation path, from a role with no `node_id`.

**Consequence:** the only remedy the common core offers a non-finding-producing role for a detected prompt-set defect is one it cannot execute. Relatedly, `charter-common.md` §6 (L107–134, 28 lines) is inert for the leaf under the manifest's own allocation diagnostic (`charter.md:78-79`, *"A rule only one role can act on is that role's"*) — and `charter.md:47-48` states the whole rationale for splitting is that *"every line a role does not need is a line that crowds out one it does."*

---

### **M-F5 — `major` — the Completeness lens's earned-clean clause is unsatisfiable as shipped**

`redteam.md:70-74` requires, for a clean lens-6 verdict: *"Name each spine section and each Layer-2 required section **by name**, and for each **cite where in the node it is covered**… A clean verdict that lists no section-classes and cites no coverage is treated as **un-run**."*

Neither the universal spine nor the Layer-2 required-section set is defined anywhere in the set (`grep -rn "spine\|Layer-2" Architect/stages/` returns only `redteam.md:44,45,70,71`), and neither is in the reviewer's closed set (`redteam.md:14-16` = task, plan, floor, config review-context paths). `1.5-criteria-v2.md` N-15a *deliberately* forbids stating spine names ("element 3 does not exist yet"), so this is a knowing gap — but the obligation shipped without the escape.

The set has the correct pattern for exactly this situation in two other places and did not apply it here: `charter-common.md:53-54` (*"If you were given no floor… say **that** — as a **blocker**"*) and `combiner.md:65-67` (*"If you were not given read access to the sources… Say so, and report every citation as **unchecked**"*). This is the run's own D5 ("recurrence means under-generalization") failing against the run.

**Consequence:** every red-team review is mechanically un-run on lens 6, or the reviewer invents a spine — which is the manufactured-finding failure mode entering through the lens most likely to produce them.

---

### **M-F6 — `major` — "get stuck" is a first-class spec state with no handling instruction anywhere in the set**

`Architect.md:77, 95, 108` all read `wait(…working())  // wait for all working agents to either return, **or get stuck**`. `node.md:59` carries the phrase — *"Wait for every agent you spawned to return or get stuck before you merge"* — and it is the **only** occurrence of "stuck" in all six files.

Nothing tells the node what to do with a stuck agent: respawn it, proceed with the survivors, or abort. This is the missing tier-(iii) section the Completeness lens is defined to catch (`redteam.md:41-46` names *"a failure mode, a state/restart story"* explicitly). It is also the input to M-F1: a stuck leaf is precisely how `Consensus` legitimately receives two plans, and the set has no answer for either half.

---

### **M-F7 — `major` — `minor`/`nitpick` findings are "recorded against the plan" with no recording location in the set or the spec**

`charter-common.md:70-71` and `combiner.md:71-72` (*"recorded, not deleted"*) both commit to recording minors. But `Severity` returns only blocker|major (`Architect.md:26`, `combiner.md:70`), and the only persistence in the whole design is `Memo_write(node_id, done, iter, task, plan, division)` (`Architect.md:37`; `node.md:62, 70, 72`) — which has **no findings field**. `1.5-criteria-v2.md` N-11 further removes every reference to a "decision log" because *"Architect has none."*

**Consequence:** a minor finding is unrecoverable the instant `Severity` returns. `combiner.md:72`'s emphatic *"recorded, not deleted"* is a commitment with no mechanism — the same defect class as the fork source's dangling *"(below)"* that this run already fixed once (`charter.md:20-24`). Lens 6 names *"an output **location**"* as a completeness item; this is one.

---

### **M-F8 — `major` — the only role that writes content has no source access, while its own file requires it to cite sources**

`leaf.md:55` — *"**Cite the source for factual premises** and **flag what you could not check**."*
`leaf.md:26` closed set — *"Exactly: the **task**, the **plan** you are to fill out, and the **granularity floor**."* No source paths.

Every other role got a source channel added beyond its signature (`redteam.md:14-16`, `divider.md:16-17`, `combiner.md:15-16`: *"plus the review-context paths named in the run's configuration"*). The leaf, uniquely, did not. `charter-common.md:31-34` (verbatim to the leaf) meanwhile asserts *"you are given **read access to that source**, and using it is load-bearing: text-only work can only catch internal inconsistency, never a plan that is confidently wrong about the world it plans in."*

**Consequence:** the one role that actually produces the artifact is confined to text-only work — the loop's founding failure, reproduced at the leaf. Either the addition is right and the leaf was missed, or the signature bound is right and three role files are wrong (see M-F13); it cannot be both.

---

### **M-F9 — `major` — the split reviewer's assembled prompt contradicts itself on its own closed set**

`charter.md:64` composes the split reviewer as `charter-common.md` + `redteam.md` + `divider.md` §B.

- `redteam.md:14` — *"Exactly: the **task**, the **plan**, and the **granularity floor**"*
- `divider.md:62-63` — *"You have the task, the granularity floor, and the proposed division… **You have no plan and are not entitled to one**"*

The split reviewer is told, inside one prompt, both that the plan is in its closed set and that it is not. `divider.md:19-25` names this exact condition as the dangerous one: *"A divider that believes it holds a plan will split along the plan's structure instead of the task's, which is the seam being wrong for a reason no later reviewer can see."* Under `charter-common.md:18-21` the reviewer is required to file this as a prompt-set defect rather than pick a winner — i.e. the set's first act on a split review is to file against itself.

---

### **M-F10 — `major` — `charter-common.md` §2 tells the combiner it holds a granularity floor it was never given**

`charter-common.md:41` (verbatim to all six roles) — *"**You are given a granularity floor**"* — and `:56` — *"**How the floor binds *your* work is stated in your role file.** It bounds three different things for three different roles, and only your role's version applies to you."*

`grep -n "floor\|granularit" combiner.md` → **zero hits**. `combiner.md:15-16`'s closed set contains no floor. `node.md` names `granularity` only as a value it passes down (`:17, 31, 52-56, 65, 68`) with no operative clause.

So §2's framing is false for two of six roles, and `:53-54`'s remedy (*"say so… as a **blocker** if your role files findings"*) is unavailable to the combiner, which files no findings. By the manifest's own diagnostic (`charter.md:78-79`), §2's *operative* framing belongs in the three role files that act on it; only the definition and safety rationale are common — which is what `charter.md:80-82` claims was done, but the shipped §2 addresses the reader in the second person as a floor-holder throughout.

---

### **M-F11 — `minor` (position) — the divider's prompt ends with 22 lines addressed to a different role**

`divider.md:57-79` (§B) is written in the second person to the **split reviewer** (*"You are reviewing a proposed division of a task"*, `:62`), and only `:58-60` is quoted as a blockquote; `:62-79` is not. The divider receives the whole file, so the most-recent — and terminal — content in the divider's prompt aims at someone else.

Relatedly, `charter.md:87` justifies the B18 duplication as *"It binds only finding-producing roles"* — inaccurate for `divider.md`, half of whose audience is the divider, which returns a split, not findings. On my brief's §7 question: **the declared reason for the duplication is sound in substance** (fork-source B18 is L103, the terminal line; append-composition cannot keep a common rule last; `redteam.md:127` and `divider.md:79` are each verified terminal), but the *scope* clause used to justify it is not accurate as written.

---

### **M-F12 — `minor` — the manifest's CHANGED list under-declares, contrary to its own promise**

`charter.md:15` — *"**CHANGED — each difference stated where a reader of the shipped files can see it**"* — then lists five. At least four operative differences are not among them, all of them recorded in `0-baseline.md` but invisible to a reader of the shipped set:

- **P8 / D4** (`0-baseline.md:228`): the demotion rule is imported from `Guarded_change/stages/stage-4.md` L31–36 — **stage-file, not charter, content** — and the baseline explicitly classes it *"a CHANGE-class addition, not a carry."* Shipped at `node.md:91-99` / `charter-common.md:80-81` with no declaration.
- **P9 / D5** (`0-baseline.md:238`): *"Recurrence means under-generalization"* (`redteam.md:119-123`) is *"Not in the fork source charter, not in `Architect.md`."* Its only textual antecedents are in `Architect-Attempt-1/`, which §5 of my brief declares *"ARCHIVED AND SUPERSEDED. Never a source of authority."* Shipped as flat instruction.
- **P11 / D6** (`0-baseline.md:239`): *"and **no shared reasoning context with your siblings**"* (`charter-common.md:31`) is an author strengthening beyond owner record 55. Undeclared.
- **D11's UNSUBSTANTIATED mark** (`0-baseline.md:266`): the baseline records it as *"the **orchestrator's elaboration**, adopted here and recorded as such rather than reported as owner authority."* Shipped flat at `combiner.md:53-54` and `node.md:101-102` with no such note.

Applying RAT2 to the artifact (my brief §6.6), these are the undisclosed inventions. None is *wrong*; the finding is that `charter.md:15`'s promise is not met, and `charter.md:115`'s *"No rule is in a silent third category"* is true only of B01–B19, not of the set's content as a whole.

---

### **M-F13 — `minor` — three role files widen the closed-set principle the common core states**

`charter-common.md:96-98` — *"**Your input set is bounded by the function that spawned you, not by what anyone chooses to hand you.** … That the bound comes from outside the author is the whole point."*

`redteam.md:14-16`, `divider.md:16-17`, `combiner.md:15-16` each append *"plus the review-context paths named in the run's configuration"*, which appears in **no** signature in `Architect.md` (L14, L22, L24, L26, L28 are all bare `string`/`vector<string>` parameters). `charter.md:25-27` describes the per-role sets as *"bounded by each role's own function signature"* — not accurate for these three. `1.5-criteria-v2.md` N-04 states the gating requirement as *"each list matches its function's signature in `~/Documents/Architect.md`"*; on a literal reading of N-04 the artifact fails it in three files and passes only in `leaf.md` and `node.md`.

I judge the *addition* substantively right (a source-less reviewer is the founding failure) — the finding is that the principle and the practice disagree in the shipped text, and the disagreement is what produced M-F8's asymmetry.

---

### **M-F14 — `minor` (concurrency lens) — `node.md:44`'s "no shared mutable state" claim excludes the work queue**

`node.md:44` — *"Every node writes exactly one path — its own memo — so **there is no shared mutable state to guard**. Keep it that way."*

But the same file has every node **claim and reserve** a place in a shared `work_queue`: `:24` (*"BEFORE you claim a work-queue slot"*), `:31` (*"Claim your slot"*), `:39` (*"reserve your place within it"*), matching `Architect.md:44` (`wait(work_queue)`). The queue is shared, mutated by every node, and is the one piece of cross-node state in the design. `1.5-criteria-v2.md` Part D makes the same absolute claim.

Separately, `node.md:41`'s *"Sibling nodes serialise inside the shared slot"* is an interpretation of `Architect.md:12` (*"reserve their place within that slot"*) stated as flat fact; Part D of the criteria itself warns that the parallel claim about leaves is false, so the run knows this reading is contestable.

Low impact (nodes do not implement the queue), but the sentence pre-emptively closes the concurrency lens over the one accessor set that exists.

---

### **M-F15 — `minor` — `Severity` is told to contest through a channel it does not hold**

`combiner.md:77` — *"that is a severity to contest through the channel the node holds, not to correct in passing."* `charter-common.md:81` says the channel is *"the channel **your role file** names."* The combiner's role file names the node's channel, which the combiner has no address for (`combiner.md:15-16`: it receives a vector and config paths only). The correct instruction is "return it unchanged and say so in your record"; as written it points at an unreachable remedy, the same shape as M-F4.

---

### **M-F16 — `nitpick` / missed opportunity — a five-line mechanical sweep would have caught M-F2 at build time**

The run already builds `oracles/ruleplace.sh` with relocation mutants (N-M2) for *placement*. The composition rule additionally needs an *anti-duplication* assertion: "no normalized sentence of ≥7 words appears in both `charter-common.md` and any role file, except the declared B18 line." I ran exactly that in one pass and it returned M-F2 (a), (b), (c). `1.5-criteria-v2.md`'s "What ships UNVERIFIED" table already promises *"one mechanical duplication sweep"* for N-06 — this finding is that the shipped text does not survive it.

---

## §C — Per-lens verdicts

**1. Factual — ISSUES FOUND (M-F1, M-F2, M-F7, M-F10, M-F12, M-F13, M-F14).**
Source evidence consulted, itemised so the clean sub-verdicts are earned:

- **Fork fidelity, forward direction (`charter.md:96-113`) — CLEAN, verified rule by rule.** B01→`charter-common.md:28-37` ✓; B02→`redteam.md:29` ✓; B03–B06→`redteam.md:32-35` ✓; B07→`redteam.md:36-40`+`78`+`95` ✓; B08→`charter-common.md:84-86` ✓; B09→`charter-common.md:61-74` ✓; B10→`charter-common.md:88-89` ✓; B11→`redteam.md:57-58` ✓; B12→`redteam.md:61-64` ✓; B13→`redteam.md:65-69` ✓; B14→`combiner.md:46-67` ✓; B15→`charter-common.md:94-105` + each role file's input list ✓; B16→`redteam.md:106-112` ✓; B17→`redteam.md:113-117` ✓; B18→`redteam.md:127` + `divider.md:79`, both verified terminal ✓; B19→`charter-common.md:16-23` ✓. Every claimed destination resolves. **No fork-source rule claimed present is absent.**
- **Fork fidelity, reverse direction — CLEAN.** Comparing `Guarded_change/stages/charter.md:10-103` span by span, the only unmatched span is B15's A/B-harness sub-clause (`:77-79`), which is the declared DROP (`charter.md:37-39`). `stage-4.md`'s severity table is imported (M-F12) but is not fork-source charter content.
- **Repaired blocker (a), durable source — CLEAN and internally consistent.** `charter-common.md:131-134` names the harness-authored transcript as *the only* admissible source and names *"a decision log or any other record an agent can write"* as not one. This matches `~/Documents/Architect.md:19` verbatim in substance and **removes** the contradiction that was in `records/repaired-clauses.md` R4 (which admitted *"a timestamped, owner-attributed entry in the run's decision log"*). `redteam.md:83` now defers to §6 (*"see the common core §6 on what counts"*) rather than restating a list, so there is no second, wider definition to conflict with. `charter.md:30-35` declares the narrowing against `stage-3.md:59`. **No self-contradiction found.**
- **Repaired blocker (b), `Union`'s suppression power — CLEAN, and the removal is correct.** `combiner.md:58-60` — *"Marking is not demoting… An UNSUBSTANTIATED finding keeps the severity its reviewer assigned and passes to `Severity` on that severity"* — and `:61-62` *"Marking is not filtering. **Nothing is discarded either way.**"* This is consistent with `Architect.md:24` (`Union` "DISCARDS NOTHING") and `Architect.md:26` (`Severity` is a pure filter). I verified the substitute is coherent with `node.md:101-102` (*"An **UNSUBSTANTIATED** mark on a finding is not a demotion and does not license one"*) and with `node.md:96-98`, which routes any real demotion to `Ask_human` — matching `Architect.md:20` (*"demoting a blocker|major requires the owner… Human_gate cannot carry a severity"*). No residual power to suppress survives anywhere in the set (`grep "does not pass"` → 0 hits).
- **Transcript spot-checks, done at the record index, not inferred.** Record **1449** line 1449 item 3 reads verbatim: *"That \*was\* part of what Combine did, but you said nothing could get discarded, make up your mind."* — matches `0-baseline.md:266`'s quote exactly and ratifies **placement** of the spot-verify duty, nothing about disposition. Item 4 reads *"I don't know what the fuck rat1/2 even ARE."* — matches `0-baseline.md:267`; correctly treated as a non-answer. Record **1175** reads *"…the new charter should also include the definition of three tiered completebess definition"* — ratifies inclusion only, not lens-vs-bullet placement, as `0-baseline.md:250`/D1 states. Record **1258** reads *"I think trust the blocker/major filter, fix it later if it is an issue."* — supports the "no backstop cap" citation. **All four cited owner claims check out at their cited indices; none is inflated in the baseline.**

**2. Logical — ISSUES FOUND (M-F1, M-F3, M-F4, M-F6, M-F9, M-F15).** The set's internal call graph does not close: `node.md` calls `Consensus` in a way `combiner.md` forbids; `charter-common.md` offers an escape hatch four roles cannot invoke; the split reviewer's prompt asserts both P and ¬P about its own inputs.

**3. Missed opportunity — ISSUES FOUND.** (i) Split `redteam.md`'s two conditional lenses into `lens-position.md` / `lens-concurrency.md`, appended only when the trigger fires — this is the one change that makes B19/D8 real rather than asserted (fixes M-F3), and it costs nothing under the existing append-composition. (ii) Extract B18 into a one-line `precision.md` tail fragment appended last to finding-producing prompts — removes the declared duplication *and* the misaimed divider tail (M-F11) without weakening the position argument. (iii) Add the anti-duplication assertion to `ruleplace.sh` (M-F16). (iv) Give `leaf.md` the same config review-context clause its three siblings have (M-F8).

**4. Unstated assumptions & risks — ISSUES FOUND.** Assumed: that `Consensus` will only ever see three plans (false on the spec's own control flow); that a run configuration will place the session transcript in every reviewer's `redteam_context`, without which `redteam.md:78-93`'s RAT1 spot-verify is inert and every recorded owner-ruling becomes "unverified" ⇒ `blocker` under `charter-common.md:65` — note `combiner.md:65-67` states exactly this fallback for code citations and `redteam.md` states no analogue for owner quotes; that a spine/Layer-2 section list exists somewhere (M-F5); that stuck agents never happen (M-F6); that minors have somewhere to be recorded (M-F7); that the work queue is not shared state (M-F14).

**5. Fidelity — ISSUES FOUND (M-F1, M-F4, M-F8, M-F12).** Terms pinned to owner-intent mechanisms in `~/Documents/Architect.md`, with the artifact checked against each:

| Loaded term | Pinned mechanism (owner intent) | Artifact implements it? |
|---|---|---|
| **"3 independent cold agents"** | `Architect.md:72-75, 104-107` — three separate `Spawn_*` calls | ✓ `charter-common.md:36-37`, `leaf.md:9`, `redteam.md:5`, `node.md:52, 65` |
| **`Consensus`** | `Architect.md:22` — 2-of-3 on numbered steps incl. order, odd plan discarded, plans only | ✗ **proxy substituted for the 2-input case** — `combiner.md:32-35` converts it into an owner-blocking refusal (M-F1) |
| **`Union`** | `Architect.md:24` — merge, discard nothing, dedup exact restatements only | ✓ `combiner.md:39-42`, `:61-62` |
| **`Severity`** | `Architect.md:26` — pure filter returning blocker\|major | ✓ `combiner.md:70-77` (*"You filter. You do not re-rank."*) |
| **`Ask_human`** | `Architect.md:18` — `(question, node_id, depth)`, node→orchestrator→owner, verbatim relay | ✗ **offered to roles lacking its arguments** (M-F4) |
| **`Human_gate`** | `Architect.md:16` — blocks at `depth <= gate_depth` (default 2), *before* children spawn, verbatim approve/reject, re-derive on reject | ✓ `node.md:79-89`, and `divider.md:50-53` on the re-derive duty |
| **`Divisible`** | `Architect.md:14` — cold, no plan argument, red-teams its result looping until no major, returns two sub-tasks or null | ✓ `divider.md:6-11, 19-25` |
| **granularity floor** | `Architect.md:1-8` — bounds `Divisible`, `Spawn_leaf`, `Spawn_redteam`, each differently | ✓ decomposed correctly across `divider.md:27-36`, `leaf.md:32-45`, `redteam.md:18-25`; but ✗ the common framing over-reaches to two roles that hold no floor (M-F10) |
| **memo / crash recovery** | `Architect.md:30-37, 41-42` — one writer per node_id, written after the value exists, read only by a restart of the same node | ✓ `node.md:22-36` (including *"Do not re-derive the division you already have"*) |
| **"the source" / read access** | `charter.md`/fork L10-14 — source access is load-bearing | ✗ **not granted to the leaf** while demanded of it (M-F8) |
| **"OWNER RULING"** | `Architect.md:19` — transcript-only admissibility | ✓ `charter-common.md:90-92`, `:131-134`; RAT1/RAT2 inlined at `redteam.md:78-102` matching `stage-3.md:55-81` in substance |

**Ratification audit (required, since the run carries recorded owner rulings):** the two rulings load-bearing for this artifact — record **1449 item 3** (`Union` placement) and record **1175** (three-tier completeness) — were audited as ratification artifacts. Both cite a durable source the author did not author (the harness-authored transcript), both quotes were spot-verified at their cited record indices and match verbatim, and in both cases the baseline correctly restricts the ruling's scope to what the words select (placement; inclusion) and explicitly labels the remainder as author/orchestrator elaboration (`0-baseline.md:266`, `:250`). **The ratification records themselves are sound.** The RAT2 failure is downstream: the elaborations are declared in `0-baseline.md` but not in the shipped set (M-F12).

**6. Completeness of the SET (lens 6 tier iii) — ISSUES FOUND (M-F5, M-F6, M-F7).**
Tier (i)/(ii) sweep against `~/Documents/Architect.md` — every spec entity has a home: granularity (`charter-common.md` §2 + 3 role files), `Spawn_leaf` (`leaf.md`), `Spawn_node` (`node.md`), `Divisible` (`divider.md`), `Human_gate` (`node.md:79-89`), `Ask_human` (`charter-common.md` §6), `Consensus`/`Union`/`Severity` (`combiner.md`), `Spawn_redteam` (`redteam.md`), `Memo_read`/`Memo_write` (`node.md:22-36`), the work queue and slot inheritance (`node.md:38-44`), `gate_depth` (`node.md:81`), `node_id`/`depth` conventions (`node.md:18-20`), the `while` loop and its termination (`node.md:46-77`). **No role, obligation or function in the spec is without a file** — `1.5-criteria-v2.md` N-05 holds on text presence.

Tier (iii) generative sweep — what I looked for: states named in the spec with no handler; commitments made in prose with no mechanism; obligations whose enabling input is never provisioned; and roles whose escape hatch is unreachable. It returned **M-F6** (the "stuck" state), **M-F7** (minor-finding recording location), **M-F5** (spine/Layer-2), and **M-F4** (unreachable escape hatch). Ticking (i) and (ii) was the floor, not the finding.

**7. Position / order sensitivity — ISSUES FOUND (M-F9, M-F11); B18 duplication assessed and substantially upheld.** Three assembled prompts enumerated and tested end-to-end: red-team (`common`+`redteam`) — terminal B18 verified at `redteam.md:127`; divider (`common`+`divider`) — terminal B18 verified at `divider.md:79` but preceded by 22 lines aimed at another role (M-F11); split reviewer (`common`+`redteam`+`divider` §B) — `redteam.md:127`'s B18 is displaced from terminal position by the appended §B (acceptable: §B re-states it terminally), but the assembly produces a self-contradictory closed set (M-F9). Elements that did not themselves change were tested: `charter-common.md` §6 is now the immediate predecessor of every role file's opening line, and for `leaf.md` that places 28 lines of owner-provenance material in the highest-recency slot before a role that can never use it (folded into M-F4).

**8. Concurrency — FIRES WEAKLY; one finding (M-F14).** The artifact does not alter concurrency in any executing system; it *specifies* an execution model. Accessors of the one piece of cross-node shared state, the `work_queue`: every node at `node.md:24, 31, 39` (claim/reserve), plus `Architect.md:44`'s `wait(work_queue)`. `node.md:44`'s blanket "no shared mutable state to guard" does not enumerate them. Memo state is correctly single-writer/single-reader per `Architect.md:30-37` and is genuinely unshared.

---

## §D — What I could NOT check, and why

1. **The owner's re-scope instruction and "Go for it."** Treated as the premise of the run per §3 of my prompt; I did not locate either string in the transcript and make no claim about them.
2. **Owner records 55, 1128, 1148, 1572** cited in `0-baseline.md` and `1.5-criteria-v2.md`. Only 1175, 1258 and 1449 were named in my brief; I checked those three. The other four are **unchecked, not verified** — notably **1572**, which is load-bearing for Part B being cut entirely.
3. **Whether the oracles pass.** `oracles/ruleplace.sh`, `mutation-test.sh`, `delete_span.py`, `rules.tsv` exist (timestamped 19:10–19:12 today) but `8-harness.md` does not. Per `1.5-criteria-v2.md` Part A, **every Part-A result is `verified = no` until the Part-C mutation test has run**. This review is read-only; I executed nothing. So N-01…N-20 are all currently unverified by their own oracle, independent of my findings.
4. **Agent behaviour.** This is a text review of prompts. Whether an agent handed `charter-common.md`+role file *behaves* as if the composition rule bound it is untested and, per the criteria's own "ships UNVERIFIED" table, is deliberately deferred to the end-to-end Data-Distiller run.
5. **`FINDINGS.md`** (`/home/zero/architect-dogfood-2026-07-24/`) and **`Architect-Attempt-1/stages`** — not read. I grepped Attempt-1 only to source `redteam.md:119-123`'s "Recurrence" rule (M-F12); I read none of it as authority.
6. **`Dragonfly/stages/charter.md`** — hashed but not read. I therefore did **not** verify that `charter.md`'s provenance blockquote meets the Dragonfly house shape (config note, `guarded-change.architect.md:53-56`). That claim is **unchecked**.
7. **`decisions.md`** — only the tail (~60 lines) and `Consensus` greps. Earlier gate entries are unread, so I cannot rule out that M-F12's undeclared items are declared somewhere in its body; my finding is specifically that they are not visible in the **shipped** files, which is what `charter.md:15` promises.
8. **Whether M-F1's stated limit was disclosed by the author.** I searched `changes/charter-2026-07/*.md` and `ATTEMPT-2-STATE.md` for it and found nothing. Absence of a grep hit is not proof of absence of a disclosure.

---

## §E — Highest-value finding, and what I most want challenged

**Highest-value finding: M-F1** — `combiner.md:32-35` makes `Consensus` refuse to merge and block for the owner whenever it receives fewer than three plans, but `~/Documents/Architect.md:91-97` and `node.md:55-58` call `Consensus` with **exactly two** child plans on every divisible node, every iteration. This is a self-contradiction inside the shipped set that converts the design's ordinary control flow into an owner-blocking error path, and it is the one finding here that would stop an Architect run dead rather than degrade it.

**What I most want challenged:** M-F1's premise. Specifically: is `Consensus(child.get_plans)` at `Architect.md:97` really the same function as `Consensus(leaves.get_plans)` at `Architect.md:79` — one function with two arities — or did the author intend the two-child merge to be a distinct operation that `combiner.md`'s "2-of-3" section simply does not govern? The spec uses one name and one signature (`Architect.md:22`), and `node.md:53` and `:56` both write `Consensus`, so I read it as one function. If the run intends otherwise, M-F1 collapses to a documentation gap (still ≥ `minor`: nothing in the set says so) and my severity is wrong. I would also welcome a challenge to **M-F2(c)** — whether *"Anything else is supplementary and is quoted in your record as such"* in two role files is a restatement of `charter-common.md:100` or a permissible role-scoped closing of each file's own input list; I judged it a restatement because the sentence is functionally identical and the common core already states it unconditionally, but it is the weakest of the three duplication instances.