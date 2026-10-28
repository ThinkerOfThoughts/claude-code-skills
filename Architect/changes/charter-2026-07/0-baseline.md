# Stage 0 — Baseline (TEXTUAL)

**Run:** `charter-2026-07` · element 1 of 6 (the red-team charter) · config
`Architect/guarded-change.architect.md`.

This run is **not** greenfield. Architect's charter declares itself a **fork**, so the fork source is the
baseline and the regression bar. Per the config's `measurement.baseline.how`, this document captures three
things, all captured **before** any build:

1. the fork source frozen at its declared commit, with **every rule it states** enumerated and cited;
2. per enumerated rule, this run's **intent** — CARRY / CHANGE / DROP — declared before the build;
3. the **unvetted draft's** rule set, enumerated the same way and marked **PROPOSED**, so the harness can
   tell "a rule the fork source had" from "a rule the draft's author invented."

**Regression for this artifact** = a CARRY rule that stopped being stated, or a DROP that happened without
being declared in the provenance blockquote.

---

## 0.1 Frozen fork source — identity verified, not assumed

Commands run and their verbatim output:

```
$ cd /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c
$ sha256sum Guarded_change/stages/charter.md
0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590  Guarded_change/stages/charter.md
$ git show 8d73e5d:Guarded_change/stages/charter.md | sha256sum
0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590  -
$ sha256sum /home/zero/.claude/skills/guarded-change/stages/charter.md
0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590  /home/zero/.claude/skills/guarded-change/stages/charter.md
$ diff Guarded_change/stages/charter.md /home/zero/.claude/skills/guarded-change/stages/charter.md && echo "IDENTICAL"
IDENTICAL
```

**Result.** The config's asserted sha256 `0e73bacf…adc590` matched, at `8d73e5d` **and** at HEAD **and** in
the installed copy. All three are byte-identical, so "the fork source" is unambiguous. Line citations below
are into `Guarded_change/stages/charter.md` at that hash (**103** lines).

Fork **precedent** (`Dragonfly/stages/charter.md`) cites `3d6889b`; `git cat-file -t 3d6889b` returned
`commit`, so that reference resolves. Dragonfly is read here only for the **shape** of a provenance
blockquote that names what was carried and what was "deliberately not carried" (its lines 8–12).

> **CORRECTION (gate-4 pass 1, reviewers A-F22 / B-F22, confirmed).** An earlier version of this section
> said the fork source was "(104 lines)". `wc -l Guarded_change/stages/charter.md` returns **103**, and
> §0.2's own pasted grep ends at `103:The reviewer is graded…`. Corrected above. Every L-citation into the
> file was independently re-checked and is unaffected. Recorded rather than silently patched, because it
> was the one number in an identity-verification section that had not been machine-generated — a small
> instance of exactly the failure constraint C5 exists to prevent.

## 0.2 Rule inventory of the fork source — generated, not hand-typed

The rule-bearing lines were located mechanically; each rule's substance was then read at the cited lines.

```
$ grep -n -E "^[0-9]+\.|^- \*\*|^The reviewer is graded" Guarded_change/stages/charter.md
19:1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
20:2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
21:3. **Missed opportunity** — better approaches or optimizations left on the table.
22:4. **Unstated assumptions & risks** — what's being taken for granted that could be false.
23:5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a
36:- **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
37:- **Rank every finding** by severity (below).
38:- **Flag the unverifiable.** Any claim the reviewer could not check against the source is
40:- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear,
42:- **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens
47:- **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict
59:- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
65:- **Provenance is part of the review record.** Every cold-review record, wherever in the run it
80:- **If the change touches a position-sensitive assembly, test for position/order sensitivity**
91:- **If the change introduces a new accessor or a new read-modify-write window over shared mutable
103:The reviewer is graded on **precision** (are its findings real?), not on how many it raises.
```

Two rule-bearing spans carry no bullet marker and were added by reading the file: the reviewer-constitution
paragraph (L10–14) and the lens-separation sentence (L16–17). The header (L1–6) is guarded-change **plumbing**
("shared by stages 3 and 6", "Verbatim from METHODOLOGY") — it states no review rule and is not inventoried.

### The regression bar — 18 rules

| ID | Rule (fork source) | Cite | Kind |
|---|---|---|---|
| **B01** | Reviewer is **cold and independent** — a subagent with no shared context with the author — with read access to **both the artifact and the underlying source** named in the config's `redteam_context`. Source access is load-bearing: docs-only review catches only internal inconsistency. | L10–14 | constitution |
| **B02** | The lenses are **separate**, "kept distinct so one doesn't crowd out the others." | L16–17 | constitution |
| **B03** | Lens 1 **Factual** — artifact vs. source; cite line/file. | L19 | lens |
| **B04** | Lens 2 **Logical** — flaws in plan/reasoning/sequencing, independent of the code. | L20 | lens |
| **B05** | Lens 3 **Missed opportunity** — better approaches left on the table. | L21 | lens |
| **B06** | Lens 4 **Unstated assumptions & risks**. | L22 | lens |
| **B07** | Lens 5 **Fidelity** — mechanism vs. **proxy**; pin each loaded operational term; a substituted implementation is **untrusted** until the owner confirms; a definition inherited from a prior artifact, a **memory note**, or a recorded **"OWNER RULING"** is a *claim to re-verify*, audited as a ratification artifact + checked for unratified inflation. | L23–33 | lens |
| **B08** | **Cite or it doesn't count** — each finding names a line/file or a concrete failure scenario. | L36 | discipline (uncond.) |
| **B09** | **Rank every finding** by severity. | L37 | discipline (uncond.) |
| **B10** | **Flag the unverifiable** — an unchecked claim is reported as such, never silently accepted. | L38–39 | discipline (uncond.) |
| **B11** | **"No issue found" per lens is allowed and expected** — a clean lens is a real all-clear. | L40–41 | discipline (uncond.) |
| **B12** | **A clean *factual* lens must be earned with citations** — zero source citations ⇒ treated as **un-run** and re-run. | L42–46 | discipline (uncond.) |
| **B13** | **A clean *fidelity* lens must be earned by pinning the terms** — name the loaded terms, state each pinned mechanism, show the artifact implements *that*; plus, where a recorded owner-ruling is in play, show the **ratification-record audit** (options + owner's verbatim words + durable source cited, mapping confirmed on the flagged axis, elaboration traced). Un-pinned clean ⇒ un-run. | L47–58 | discipline (uncond.) |
| **B14** | **Spot-verify the citations themselves** — the review's **consumer** checks a sample of cited file:lines exist and say what's claimed (a few, not all); extends to term→mechanism pins on a clean fidelity lens. | L59–64 | discipline (uncond.) |
| **B15** | **Provenance is part of the review record** — every record embeds (i) verbatim charter/prompt, (ii) exact context path list, (iii) reviewer's verbatim output, (iv) agent type + model, (v) reviewer-reported sha256 of each context file. Reviewer input is a **closed set**; supplementary author-authored context must be **quoted as such**; missing any element ⇒ **un-run**. Sub-clause: in **A/B harness arms** author-authored supplementary context is **prohibited outright** (a leak is a confound). | L65–79 | discipline (uncond.) |
| **B16** | **Conditional — position/order sensitivity** (lens 4): fires only in a position-sensitive assembly; trigger is *any* edit incl. add/remove; elements that did not change are in scope; "all the information is still present" is **not** a clean verdict; the finding is the behavior change, ranked by impact. | L80–90 | discipline (cond.) |
| **B17** | **Conditional — concurrency** (lens 4): fires only where the change alters concurrency over shared mutable state; (1) enumerate every concurrent reader and writer incl. untouched ones; (2) treat the **guard's scope** as a claim to challenge. A guard's existence is not coverage. | L91–101 | discipline (cond.) |
| **B18** | The reviewer is graded on **precision**, not on how many findings it raises. | L103 | discipline (uncond.) |
| **B19** | **Charter composition** — what "the charter given" (provenance element (i)) must consist of: the charter **core verbatim** — the lenses + the unconditional discipline bullets — **plus the stage-specific additions, plus any conditional lens *whose trigger fires***, with task-specific additions **quoted as such**. | L70–74 | discipline (uncond.) |

> **B19 ADDED at gate-4 pass 1 — this rule was MISSED by the first inventory (M-01).** All three cold
> reviewers found it independently (A-F2, B-F02, C-F1-a — **3/3**, the highest convergence of the pass) and
> the runner re-verified it by pasting `sed -n '70,76p'` of the fork source (`3-redteam-plan.md`). It sat
> *inside* the line range B15 already cited, which is exactly why it slipped: an omission from an operative
> paraphrase is invisible to a line-range check.
>
> **Why this was the most dangerous single miss in the run.** `2-plan.md` §2.1 generates `oracles/rules.tsv`
> **from this document**. A rule absent from the inventory is therefore absent from the checker's probe set,
> so the fork-fidelity regression arm would have been blind to it **by construction** — the claim and its
> oracle sharing one source. Reviewer A filed that structural point separately (A-F3). The fix is
> two-part and both parts are now in the plan: add B19 here **and** add a second, independently-derived
> probe (a mechanical fork-diff) so the checker's coverage is not defined by the inventory's coverage.
>
> **B19 also has live consequences for the shipped charter**, beyond fork fidelity. It is the fork source's
> only statement that (a) the charter is delivered **verbatim**, and (b) a **conditional lens is included
> only when its trigger fires**. The pass-1 plan placed both conditional lenses in the charter
> unconditionally (`2-plan.md` §1.1 block 6) — an undeclared CHANGE to a rule that had no intent at all.
> Resolved at D8 below.

**Noted defect in the fork source** (inherited, not to be inherited): B09 says "Rank every finding by
severity **(below)**" — but `Guarded_change/stages/charter.md` contains **no severity table**; the referent
lives in `stages/stage-4.md` L17–22, a different file. The dangling "(below)" is tolerable in guarded-change
because its reviewers are dispatched by stage files that carry the table. It is **not** tolerable in
Architect, where this charter is the one document every reviewer reads verbatim and `Severity()`
(`~/Documents/Architect.md` L26) consumes the result. See B09's CHANGE intent.

## 0.3 Declared intent per baseline rule — CARRY / CHANGE / DROP

Declared **before** the build. Authority column: where the intent comes from. `Architect.md` = the
owner-authored design spec `/home/zero/Documents/Architect.md`.

| ID | Intent | Detail + authority |
|---|---|---|
| B01 | **CARRY** | Restated for Architect's callers (the reviewer reviews a plan node, not a code diff). "Underlying source" ⇒ the source the plan makes claims about. Source-access-is-load-bearing kept verbatim in substance. Dogfood F4 (`FINDINGS.md` L60–68) is the evidence this must stay explicit. |
| B02 | **CHANGE** | Six lenses, not five. The separation rationale is carried **and strengthened** (it is the stated reason completeness is a lens rather than a mandate bullet). Owner ratified the *inclusion* of the three-tier completeness definition (record **1175**); the *lens-vs-bullet* placement is an **author decision** — see §0.5 D1. |
| B03 | **CARRY** | Wording adapted: "code/data" ⇒ "source (code, data, prior docs)". |
| B04 | **CARRY** | "independent of the code" ⇒ "independent of the source". |
| B05 | **CARRY** | — |
| B06 | **CARRY** | — |
| B07 | **CARRY** | Substance carried whole, incl. the ratification-artifact duty and the inflation check. Example term list re-aimed at planning ("agent", "human", "leaf", "decompose", "review"). |
| B08 | **CARRY** | Plus a plan-shaped example of an acceptable citation. |
| B09 | **CHANGE** | Strengthened **and** made self-contained: (a) the severity **table is stated in the charter**, closing the fork source's dangling "(below)"; (b) an **unsevered finding is treated as not filed**, because `Severity()` filters on severity (`Architect.md` L26, L28) and an unsevered finding is dropped on the floor. |
| B10 | **CARRY** | — |
| B11 | **CARRY** | — |
| B12 | **CARRY** | — |
| B13 | **CARRY** | — |
| B14 | **CARRY** | Plus a named **consumer**: in Architect the consumer is `Union()`/`Severity()` and the node that calls them (`Architect.md` L24, L26, L110). Dogfood tier-3 (`FINDINGS.md` L133) recorded that this duty was assigned to **no stage** in attempt 1; naming the consumer is the fix. |
| B15 | **CARRY (with one declared DROP)** | The five embedded elements, the closed set, the quote-supplementary-context rule and the missing-any⇒un-run rule all carry. The **A/B-harness-arm prohibition sub-clause is DROPPED** — Architect's design has no A/B harness arms (`Architect.md` defines `Spawn_redteam`/`Divisible`/`Consensus`/`Union`/`Severity`; no arm-based harness exists). Per the Dragonfly precedent this DROP **must be named in the provenance blockquote**. The closed set is re-specified for Architect's inputs — see §0.5 D3. |
| B16 | **CARRY** | Re-aimed at the plan under review rather than a code diff. |
| B17 | **CARRY** | Re-aimed: fires where **the plan** alters concurrency over shared mutable state. The *plans Architect reviews* can plan concurrent systems, so the lens is live regardless of Architect's own execution model. **(Premise corrected — see below.)** |
| B18 | **CARRY, and CARRY ITS POSITION** | Substance unchanged. **Position is now load-bearing and declared:** in the fork source B18 is the document's **final line** (L103). Reviewers A-F10 and B-F13 (2/3) filed its displacement as a position-lens finding — the precision counterweight losing tail recency in a charter that *adds* four aggression-licensing sections, in a loop where findings become the next task (`Architect.md` L110) and there is no backstop cap (record 1258). Intent: B18 **stays last**. See D9. |
| **B19** | **CARRY** | The composition rule carries, restated for Architect's two callers: the core is given verbatim, each caller's aiming is added and **quoted as an addition**, and a conditional lens is included **only when its trigger fires**. Drives D8. |

> **CORRECTION to B17's premise (gate-4 pass 1, reviewer B-F17, confirmed).** An earlier version of this
> row asserted "slot inheritance serialises siblings, `Architect.md` L12, L40". That is wrong at the lines
> cited: `Architect.md` **L10** says leaf agents "inheret their parents work_queue slot and **operate in
> paralell within that slot**", and L91/L104 are wait-for-**all** joins over vectors of concurrently
> spawned children. The runner re-verified this by pasting the L10 text (`3-redteam-plan.md`).
>
> **The corrected reading:** slot inheritance serialises **sibling *nodes* at a node** — a child reserves
> its place within the parent's slot (L12) — while a node's **three leaves run in parallel** inside that
> slot (L10). The conclusion (Architect's own execution model has no shared mutable state) survives, but it
> rests on the **memo's one-writer-per-node rule** (L30–37: "One writer per node_id (the node itself),
> written AFTER the value exists, read ONLY by a restart of that same node"), not on sibling serialisation.
>
> This correction matters beyond bookkeeping. Reviewers B and C both challenged the *conclusion* and both
> found it holds — but a right answer resting on a wrong premise is the specific failure `FINDINGS.md`
> L123–124 records this project already producing ("a root reviewer **contests the build's own stage-6
> red-team** for standing the concurrency lens down on a false premise"). By this run's own D5
> ("recurrence means under-generalization") the remedy is the correct reason, not a better-worded wrong
> one. `1.5-criteria.md` Part D is restated on the memo rule.

**No rule is left in a silent third category.** Every one of **B01–B19** has an intent above; B15's partial
DROP is the only DROP and is declared. **Count: 19 rules, all CARRY-or-CHANGE.** (Pass 1 said "17" in
`1.5-criteria.md` C-02, which disagreed with this table's own 18 — reviewer A-F13. Subtracting a *sub-clause*
does not remove a *rule* from the count. Corrected to 19 with B19 added; the criteria document now reads the
count from this table rather than restating it, so the two cannot drift again.)

## 0.4 The unvetted draft's rule set — PROPOSED, no standing

`Architect/stages/charter.md` (163 lines, sha256
`6a1981f3fd4db5a496ed23928b90ca8b575c30d5afb3765f792e09d543a19212`) was **hand-written freehand in the main
session, outside this loop, and never cold-reviewed**. It carries its own banner saying so (L3–6). It is an
**input proposal**. Nothing below inherits standing from appearing there.

```
$ grep -n -E "^#{1,3} |^[0-9]+\. \*\*|^- \*\*|^\*\*" Architect/stages/charter.md
1:# The red-team charter
29:## The granularity floor — read this before you flag anything as vague
34:**A step already at or below the floor is NOT vague. It is finished.** …
44:## The six lenses
49:1. **Factual** …   50:2. **Logical** …   51:3. **Missed opportunity** …
52:4. **Unstated assumptions & risks** …   53:5. **Fidelity** …   62:6. **Completeness** …
72:**Also in scope for every lens:** does the plan cover **every element of the task** …
75:## Discipline that makes aggressive review trustworthy
77:- **Cite or it doesn't count.** …
79:- **Every finding carries a severity — this is load-bearing, not bookkeeping.** …
82:- **Report a finding even if you suspect no one else will.** …
86:- **Flag the unverifiable.** …
88:- **"No issue found" per lens is allowed and expected.** …
90:- **A clean *factual* lens must be earned with citations.** …
94:- **A clean *fidelity* lens must be earned by pinning the terms.** …
99:- **A clean *Completeness* lens must be earned by naming the section-classes checked.** …
104:- **Spot-verify the citations.** …
109:- **Provenance is part of the review record.** …
115:- **Conditional — position/order sensitivity** (lens 4). …
121:- **Conditional — concurrency** (lens 4). …
126:## Severity model
140:**Demotion is not the reviewer's to take, and not the author's either.** …
144:**Recurrence means under-generalization, not thrash.** …
149:## The two callers
151:- **The plan red-team — 3 independent cold agents per iteration.** …
156:- **The split review, inside `Divisible`.** …
162:**"3 independent cold agents"** means **three separately-spawned subagents** …
```

### Draft-only rules (P-rules) — every one is the draft author's invention until independently sourced

| ID | Draft rule | Draft cite | Independently sourced? |
|---|---|---|---|
| **P1** | The **granularity floor** section: a step at/below the floor is not vague, it is finished; no finding whose only remedy is decomposition below the floor; the floor is a **safety property** because findings become the next task; if the floor itself is wrong, say *that*. | L29–42 | **YES** — `Architect.md` L1–8 (the floor bounds `Spawn_redteam`; without it the red-team "MANUFACTURES the problem"), L24 ("a step already at the floor is NOT vague, it is done"). Owner record **1128** ratifies a max-granularity option (Manual Samuel). **ADOPT.** |
| **P2** | **Sixth lens — Completeness**, three tiers (i) universal spine, (ii) Layer-2 required sections, (iii) generative sweep; tier (iii) decisive; "ticking (i) and (ii) is the floor, not the finding." | L62–71 | **PARTLY** — owner record **1175** ratifies that the charter include the three-tier completeness definition (verbatim: *"the new charter should also include the definition of three tiered completebess definition"*). **Lens-vs-bullet placement is NOT in the owner's words** → author decision, §0.5 D1. **ADOPT with the placement declared as author-owned.** |
| **P3** | "Also in scope for every lens": does the plan cover **every element of the task**? | L72–74 | **YES** — `Architect.md` L28: "misses a portion of _task" is an issue. **ADOPT.** |
| **P4** | **Unsevered finding is treated as not filed**; severity is load-bearing. | L79–81 | **YES** — `Architect.md` L26 (`Severity()` filters), L28 ("Every issue carries a severity, because Severity() filters on it"). **ADOPT** (this is B09's CHANGE). |
| **P5** | **Report a finding even if you suspect no one else will** — findings unioned, never majority-voted. | L82–85 | **YES for the rule** — `Architect.md` L24: `Union` "DISCARDS NOTHING… A finding one reviewer caught is signal." **ADOPT the rule.** |
| **P5-stat** | *"Measured across this project's own history, **~85% of findings were caught by exactly one reviewer**, and several single-reviewer findings were the most valuable of their round."* | L84–85 | **NO — UNSOURCED.** See §0.6. **REJECT the statistic.** |
| **P6** | **Clean Completeness lens must be earned** — name each spine section + each Layer-2 section and cite coverage or flag the gap; state the tier-(iii) sweep was run and what it looked for. | L99–103 | Derived: it is B12/B13's earned-clean pattern applied to the new lens. **ADOPT** as an author decision consistent with the carried pattern (§0.5 D2). |
| **P7** | **Severity table** (blocker/major/minor/nitpick) with planning-loop meanings; blocker|major become the next task, minor|nitpick recorded not looped on. | L126–138 | **YES** — `Architect.md` L26 and L110. **ADOPT** (B09 CHANGE). |
| **P8** | **Demotion is not the reviewer's to take, and not the author's either** — contesting needs a logged entry; demoting blocker/major needs the human owner. | L140–142 | Forked from guarded-change's SEV3 (`stages/stage-4.md` L31–36), which is **stage-file** content, not charter content. **ADOPT** — but declared as an import from a *sibling stage file*, not from the charter fork source, so it is a CHANGE-class addition, not a carry (§0.5 D4). |
| **P9** | **Recurrence means under-generalization, not thrash.** | L144–147 | Not in the fork source charter, not in `Architect.md`. Matches dogfood/ATTEMPT-2-STATE §8 item 5 (under-generalized fixes) — but ATTEMPT-2-STATE is agent-written and inadmissible for owner words; it is admissible as a record of *what this project produced*, corroborated by `FINDINGS.md`. **ADOPT as an author decision** (§0.5 D5). |
| **P10** | **The two callers** — the plan red-team (3 cold agents/iteration; findings unioned → filtered → become next task; red-team going quiet *is* the completion condition) and the split review inside `Divisible` (coverage of the whole task, seam soundness, neither half below the floor, real joint vs. arbitrary cut; loops until no major; human gate at depth ≤ `gate_depth`). | L149–160 | **YES** — `Architect.md` L14 (`Divisible` red-teams "looping until no major issues are found"), L66–111 (the `while(task.empty()==false)` loop; L106 `task = Severity(Union(...))`), L16 + L79–85 (`Human_gate` at `depth <= gate_depth`, default 2, before children spawn). Owner records **1148** (gate depth), **1258** (no backstop cap). **ADOPT.** |
| **P11** | **"3 independent cold agents" = three separately-spawned subagents**, no shared context with the author *and none with each other*. | L162–163 | **PARTLY** — owner record **55**: *"option be should be done by three independent cold agents"*; `Architect.md` L104–107 spawns 3. The "no shared reasoning context **with each other**" clause is an author strengthening, motivated by dogfood **F9** (`FINDINGS.md` L106–110: "3 independent cold agents has no audit surface… producible by asking one agent three times"). **ADOPT** as an author decision with that evidence (§0.5 D6). |
| **P12** | Provenance closed set = "the node's task, its plan, the granularity floor, **the parent's plan and the seam to its sibling**, plus the run config's review context." | L112–114 | **PARTLY** — `Architect.md` L28's `Spawn_redteam(_task, _plan, _granularity)` passes **three** arguments; parent's-plan/seam is **not** in that signature. See §0.5 D3 — this needs resolving, not silently adopting. |

### What the draft's own provenance blockquote claims — checked

The draft (L11–20) claims it carries "the five lenses, every unconditional discipline bullet, and the two
conditional lenses." Checked rule by rule against B01–B18: **B01–B14 and B16–B18 are all stated** in the
draft. **B15 is stated except its A/B-harness-arm sub-clause, which is absent and is not declared as
dropped.** So the draft's own provenance claim is **false as written** — a silent DROP. That is exactly the
regression class this baseline exists to catch, and it is caught here, pre-build, against the **draft**, not
against the shipped artifact. The shipped charter must declare it.

## 0.5 Author decisions this run owns (not inherited from anywhere)

| # | Decision | Why it is the author's, and the justification |
|---|---|---|
| **D1** | Completeness is a **distinct sixth lens**, not a bullet inside a general mandate. | Owner record **1175** ratifies *inclusion of the three-tier definition* and nothing about placement. Placement is therefore **author-owned** and must not be reported as an owner ruling (RAT2 — this project already produced one inflation, ATTEMPT-2-STATE §6's "means nothing" case). Justification: B02, a **carried** fork-source rule, says lenses are kept separate "so one doesn't crowd out the others"; completeness is the lens this skill exists for (`FINDINGS.md` L89–99 shows tier (iii) is the fragile one), so folding it into a mandate is the placement most likely to let it die quietly. |
| **D2** | An **earned-clean clause for the Completeness lens** (P6). | Author decision by pattern-extension: B12 and B13 are carried rules that make a clean verdict *earned* on the two lenses where an unearned clean is cheapest to produce. A sixth lens without the clause would be the one lens a reviewer could clear for free. |
| **D3** | ~~The reviewer's **closed input set**, resolved by scoping parent-plan/seam to the `Divisible` caller.~~ **SUPERSEDED at gate-4 pass 1 → D3′.** | **Pass-1 resolution was rejected 3/3** (A-F7, B-F05, C-FID-1) and the rejection is correct. Two errors. **(1) The rationale was unsound:** it treated `Spawn_redteam`'s 3-arg signature as an exhaustive input contract — but that signature also omits *the charter itself*, and the word "charter" does not occur anywhere in `Architect.md`'s **119** lines. If the signature were exhaustive the charter could not be delivered at all, so it is plainly not an input contract. **(2) The resolution moved the problem somewhere worse:** it granted parent-plan/seam to `Divisible`, whose signature is `Divisible(string _task, string _granularity)` — **two** arguments — called as `Divisible(task, granularity)` at L62, L87 and L111, never receiving a plan. I exempted the narrower caller under a rationale about signature fidelity. |
| **D3′** | **The closed input set, restated.** | The charter states the closed set **conditionally and per-caller**, which is true under any signature and pre-empts no owner decision: *the task you were given, the plan you were given, the granularity floor you were given, plus whatever review-context paths your caller supplies.* For the `Divisible` split-review caller it adds **the proposed division and the seam between its halves** — and *only* those, because the seam is **derivable from what `Divisible` itself produces** (it "returns the two top-most sub-tasks", L14) and is what `Human_gate` already presents (L16, "the seam between the halves"). **The parent's plan is dropped entirely** — it is genuinely external, genuinely absent from the signature, and nothing in the spec can supply it. Reviewer C's `gate_depth` precedent (a run constant referenced inside `Node()` without being a formal parameter, L16/L79) is the spec's own idiom for the review-context half, and is now cited rather than left as an unargued assumption. OOS-3 stands: whether `Spawn_redteam`'s signature should formally carry review context is an owner-spec question, not a charter question — but the charter no longer *depends* on the answer. |
| **D4** | Import guarded-change's **SEV3 demotion rule** (P8) into the charter, though it is stage-file content there, not charter content. | Architect has no gate stage files — the charter *is* the document a reviewer reads, and `Severity()` acts on severities directly (`Architect.md` L110). A demotion rule that lives nowhere would be a rule nobody reads. Declared as an **addition**, not a carry. |
| **D5** | Keep **"recurrence means under-generalization"** (P9). | Author decision. Evidence: ATTEMPT-2-STATE §8 item 5 as a project record (admissible for *project history*, not for owner words), and this loop's `task = Severity(Union(...))` structure (`Architect.md` L110), under which a re-found defect class becomes a fresh task and gets re-invented locally unless the charter says otherwise. |
| **D6** | Strengthen "3 independent cold agents" with **no shared reasoning context with each other** (P11). | Author decision, evidenced by dogfood **F9** (`FINDINGS.md` L106–110). The owner's words at record **55** say "three independent cold agents" without defining independence; F9 measured that the undefined version is satisfiable by asking one agent three times. Declared as an author strengthening, not an owner ruling. |
| **D7** | **Reject the "~85%" statistic** (P5-stat) while keeping the rule it was offered to support (P5). | See §0.6. Upheld 3/3; the orchestrator struck the same statistic from the config at `d044654`. |

### Decisions added at gate-4 pass 1

| # | Decision | Authority, and what is owner-ratified vs. author-owned |
|---|---|---|
| **D8** | **A conditional lens is stated in the charter with its trigger, and is *given* to a reviewer only when that trigger fires** (B19). | Follows from carried rule **B19** (fork source L70–74). Pass 1 placed both conditional lenses unconditionally and declared no intent for the rule — an undeclared CHANGE, caught 3/3. The charter now states each conditional lens **with its firing condition explicit**, and the composition rule itself is stated so both callers know the core is verbatim and their own aiming is an addition **quoted as such**. |
| **D9** | **B18 ("graded on precision") is the charter's last line**, as it is in the fork source. | Author decision under the **position lens**, forced by reviewers A-F10 / B-F13 (2/3). The fork source's B18 is L103, the terminal line; the pass-1 block order appended three blocks after the discipline bullets and displaced it. The position rule's own worked example is *"an added tail block displaces the old last element"*, and *"all the information is still present"* is explicitly **not** a clean verdict. Impact ranking is why this is not cosmetic: the precision instruction is the **only counterweight to finding-inflation**, inflated findings **become the next task** (`Architect.md` L110), and there is **no backstop cap** (record 1258) — so a diluted precision instruction is a non-termination path. Tested by arm **B-6**, not asserted. |
| **D10** | **The demotion rule is ported from guarded-change verbatim, not re-derived.** Contest a severity **only** via a logged `decisions.md` entry; demoting a **blocker or major** additionally requires the **human tie-break**; a silent unilateral demotion is a **gate violation** and the reviewer's routing stands. | **OWNER-RATIFIED**, transcript record **1449** item 2, verbatim: *"It gets implemented however it is implemented in guarded-change; that is what the instruction was: copy over the severity mechanism from guarded change."* This selects **none** of the three options that were escalated — it is a fourth: read the source and carry it. Source text carried: `Guarded_change/stages/stage-4.md` **L34–36** (SEV3) plus **L26–28** (SEV2). **Resolves the pass-1 finding A-F4 / B-F11 (2/3)**, which was that no mechanism exists to reach the human: the human named is *the same human the loop already stops for*, reached through the delegated-runner halt path (RAT3) — the path this very ruling travelled. Record 1258 removed the **cap**, not the human. |
| **D11** | **`Union` performs the citation spot-verify.** A finding whose cited file:line does not resolve is **marked unsubstantiated and does not pass to `Severity` as blocker\|major**. | **Placement is OWNER-RATIFIED**, record **1449** item 3, verbatim: *"That \*was\* part of what Combine did, but you said nothing could get discarded, make up your mind."* (`Combine` is what later split into `Consensus` + `Union`; the duty stayed with the merge step.) The apparent contradiction was mine: **"DISCARDS NOTHING" is a rule against majority-voting findings away**, read with its own next clause — *"dedups only exact restatements. A finding one reviewer caught is signal."* It is not a rule that `Union` must accept unverifiable claims, and the charter's carried **"Flag the unverifiable"** bullet (B10) already covers the shape. **Resolves pass-1 finding A-F5.** ⚠ **RAT2 declaration:** the owner ratified *where the duty lives* and *that I had manufactured a contradiction*; he did **not** specify the disposition mechanism. "Marked unsubstantiated, does not pass as blocker\|major" is the **orchestrator's elaboration**, adopted here and recorded as such rather than reported as owner authority. |
| **D12** | **RAT1 and RAT2 are inlined into the charter as operative duties**, and the `stages/stage-3.md` pointer is deleted. | **Author/orchestrator decision — explicitly NOT an owner decision.** Record **1449** item 4, verbatim: *"I don't know what the fuck rat1/2 even ARE."* That is a **non-answer on the flagged axis**, correctly treated as such: RAT1/RAT2 are guarded-change internals (CH11/CH12, `Guarded_change/stages/stage-3.md` L55–82), never owner vocabulary, and looking them up was research owed by me — not a question to arbitrate. **Resolves pass-1 finding B-F03.** Justification for inlining rather than pointing: the charter is declared **self-contained**, `ls Architect/stages/` returns `charter.md` only, and `1-spec.md` §8 creates no stage files — so a pointer to a file Architect does not have is a defect on the charter's own terms, the *same defect class* as the fork source's dangling "(below)" that B09 already fixes. Fixing only B09 would be the under-generalization D5 names. Cost: ~30 lines, accepted. |
| **D13** | **The dogfood's differential-prompt mechanism is NOT carried.** | **OWNER-RATIFIED**, record **1449** item 5, verbatim: *"That thing was for the old version, discard it"* — answering the escalated question about `FINDINGS.md` F7's recommendation to hand each critic a different plan-type's `required_sections`. **Closes pass-1 finding B-F15 as declined, not overlooked.** Consequentially, no dogfood-derived motive is carried into the charter at all (see §0.6's revision, which withdraws F7 as support for the Union rule). |
| **D14** | **The measurement apparatus is corrected, not defended.** BL-1's position arm, the tautological mutation test, and the n=1 arms are all defects in instruments **this run and its orchestrator built** — not in the artifact under construction. | **OWNER-RATIFIED framing**, record **1449** item 1, verbatim: *"That wasn't a call that warranted my attention at all, its literally a blatant flaw in a test either you or the agent created, nothing to do with whats actually being created. the answer is obvious, if the experiment is to test where the granularity floor should sit, than the experiment should actually try moving the floor."* The operative consequence beyond BL-1 is the **escalation standard** now recorded in `decisions.md`: a defect in measurement apparatus is fixed, not escalated. |

## 0.6 A claim in the draft that does not survive its own source — REJECTED

The draft asserts (L84–85):

> Measured across this project's own history, ~85% of findings were caught by exactly one reviewer, and
> several single-reviewer findings were the most valuable of their round.

The config points at `~/architect-dogfood-2026-07-24/FINDINGS.md` as the evidence for this number and
instructs that it be checked rather than accepted. It was checked:

```
$ grep -rn -i -E "85|singleton|exactly one" /home/zero/architect-hardening-loop/LOOP-STATE.md \
    /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
/home/zero/architect-dogfood-2026-07-24/FINDINGS.md:123:  cursor" **while `index.md` is exactly one**. Pointedly, a root reviewer **contests the build's own
```

The single hit is an unrelated sentence about `index.md`.

> **CORRECTION (gate-4 pass 1, reviewer A-F9, confirmed).** This section previously concluded "**No
> singleton rate is recorded anywhere on disk**". That universal negative was **false**, asserted on
> evidence covering only two files, in the one document whose whole authority is that its claims are
> mechanically checked. The figure was in fact stated in three project-authored files:
>
> ```
> $ grep -rn "85%" Architect/guarded-change.architect.md Architect/README.md Architect/ATTEMPT-2-STATE.md
> Architect/guarded-change.architect.md:77:  …including the measured singleton rate (~85% of findings caught by exactly one
> Architect/ATTEMPT-2-STATE.md:87:  **wrong for findings**: ~85% of attempt 1's findings were caught by exactly one reviewer, …
> Architect/README.md:31:  wrong for findings: measured across attempt 1's runs, ~85% of findings were caught by exactly one reviewer,
> ```
>
> The sharpest consequence was the one reviewer A drew: the config hit is **inside the `redteam_context`
> note handed to every cold agent this project dispatches**, and it called the number "the *measured*
> singleton rate". Stripping it from the charter (X1) while the dispatch context kept asserting it as
> measured would have defeated X1's whole purpose.
>
> **Correct claim, which is what this section should always have said:** the statistic has **no source** —
> it appears in no file this project did not author about itself. `FINDINGS.md` and `LOOP-STATE.md`, the
> only two files that could have measured it, contain nothing of the kind. **The orchestrator independently
> re-checked both and struck the statistic from the config at commit `d044654`** (config now carries a
> "CORRECTION 2026-07-28" note at L86–87; verified by re-reading the config at sha256 `42f289a5…0429c`).
> **RE-CHECKED 2026-07-28 (gate-4 pass 2, reviewer E-F18 — confirmed).** The grep above was pasted at pass 1
> and **no longer reproduces**: `README.md` and `ATTEMPT-2-STATE.md` have since been corrected, so the
> earlier claim that they "remain" uncorrected is **false at HEAD**. Regenerated, not retyped:
>
> ```
> $ grep -rn "85%" Architect/guarded-change.architect.md Architect/README.md Architect/ATTEMPT-2-STATE.md
> Architect/ATTEMPT-2-STATE.md:117:  > **CORRECTION 2026-07-28.** This bullet used to read "~85% of attempt 1's findings were caught by exactly
> Architect/README.md:32:  (`~/Documents/Architect.md` L24). *(An earlier version of this line cited "~85% of findings caught by
> Architect/guarded-change.architect.md:87:          (~85% of findings caught by exactly one reviewer)" as fact. **That statistic has no source.** It
> ```
>
> **All three surviving hits are corrections that name the statistic in order to strike it.** No file
> asserts it as fact any more. OOS-1 and OOS-5 are therefore **CLOSED, not open** — see §0.7.
>
> **The rejection stands and was upheld 3/3** by the cold reviewers, each of whom reproduced the grep
> independently. Do not restore the number, do not cite it, and do not let the Union rule depend on it —
> that rule stands on `~/Documents/Architect.md` L24 alone.

Independently of the sourcing question, the convergence counts `FINDINGS.md` *does* record run the other
way for the findings it enumerates:
F1 "3/3" (L35), F2 "2 independent angles" (L46), F4 "**5 independent hits — highest convergence of the run**"
(L60), F5 "3/3" (L70), F7 "3+ hits at two altitudes" (L89), F8 "2 hits" (L101), F9 "2 hits" (L106), F10
"3 hits" (L112), and tier-3 entries tagged (6+), (7+), (4), (5), (5) (L120–138).

**Disposition.** The **rule** (P5 — file it even if you think you are alone; findings are unioned, never
majority-voted) **is well-sourced independently**: `~/Documents/Architect.md` L24 defines `Union` as "merges
issues, DISCARDS NOTHING… A finding one reviewer caught is signal." The **statistic is not**, and it is the
kind of number a reviewer would reasonably take as measured fact. The shipped charter states the rule and
its real authority (the `Union` semantics and the fact that nothing filed is discarded) and **states no
singleton percentage**.

> **REVISED at gate-4 pass 1.** Pass 1 additionally offered `FINDINGS.md` F7's correlated-blind-spots
> result as "the honest support" for the rule, and reviewer B-F25 correctly noted no criterion required the
> shipped charter to carry it. That prop is now **withdrawn**, for a stronger reason than B-F25's: the
> owner ruled the dogfood's F7 material out of scope entirely — record **1449** item 5, verbatim, *"That
> thing was for the old version, discard it"*. The Union rule therefore rests on `~/Documents/Architect.md`
> L20 **alone**, which is sufficient and is owner-authored: a mechanical guarantee that nothing filed is
> discarded removes the reviewer's reason to model its peers at all, which is strictly better motivation
> than any recall statistic. Reviewer A independently reached the same judgement ("it removes the
> reviewer's reason to model its peers at all"). No dogfood-derived motive is carried into the charter.

This is a **rejection of a draft claim, in the direction of removing an unearned number.** It is recorded
here so the stage-3 red-team can challenge the rejection as easily as the claim.

## 0.7 Out-of-scope notes (recorded, not acted on)

Per the run's scope discipline (element 1 is the charter only):

- **OOS-1. CLOSED 2026-07-28.** `ATTEMPT-2-STATE.md` no longer states the "~85%" figure as fact; it carries a
  visible correction at L117. Retained here as a record of the finding and its closure. (Original text: it
  is unsourced, per §0.6. That file belongs to no element in the build table; it should be corrected, but not
  by this run.
- **OOS-2.** The Layer-2 config contract (element 3) must declare a **review-context** field. Dogfood F4
  (`FINDINGS.md` L60–68) is that finding at highest convergence. This charter references such context (D3);
  element 3 owes the declaration.
- **OOS-3.** `Architect.md` L28's `Spawn_redteam` signature does not carry a review-context or config
  parameter, so the charter's closed set is broader than the spec'd call signature. Raised at D3; a signature
  change is an owner-spec question, not a charter question.
- **OOS-4.** Dragonfly's README reportedly still says "four-lens / reused not forked" (ATTEMPT-2-STATE §7).
  Unrelated to Architect entirely.
