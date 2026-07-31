# Split review — round 2, reviewer C

Cold split reviewer. I reviewed the **proposed division** at
`Architect/runs/data-distiller/it3/0/split-round-2.md` — its two sub-tasks and its stated seam.
I hold no plan and was given none.

**Fence declaration:** I did **not** open, read, list, grep, glob or otherwise access
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` or anything under it, and I did not invoke
the installed `data-distiller` skill. I read the sibling skills `Guarded_change/` and `Dragonfly/`,
and the Architect stage files, as permitted.

I did not read any `split-review-*.md`. I did not read `split-round-1.md`; I reviewed round 2 on its
own merits and treated §7's dispositions as claims, not as evidence.

---

## VERDICT — the two parts

**Part 1 — what I found:** 1 `blocker`, 4 `major`, 6 `minor`, 2 `nitpick`. Every one of them is a
defect in the **seam text**, which is the divider's own output. None of them is a reason to move the
joint.

**Part 2 — do I object to going forward with this cut? NO. I do not object, and I positively
endorse this joint.** The finding boundary is a real joint, not a symmetry bisection, and it is the
boundary the owner's own task statement (P5) named before any divider looked at it. I would keep it.
My findings travel down with the sub-tasks / are fixed in the seam text; they are not disagreement
about the cut. **Filing a blocker here is not an objection to proceeding** — the blocker is a
missing two-line clause in §3.3, not a wrong boundary.

---

## The four questions

**1. Coverage — do the two halves cover the whole task?**
Near-complete. All eight properties P1–P8 are owned exactly once and the three non-property
remainders round 1 orphaned (driver, over-size return path, corpus-level output) now carry explicit
ownership lines inside §3 rather than only in the §4 audit table. **One portion each half has
textual grounds to believe the other owns: the production of `state=oversize` (F3).** No orphaned
remainder otherwise.

**2. The seam — stated, sound, self-contained?**
**Stated:** yes, at length and concretely (§3.1–§3.11). **Self-contained:** substantially — I
checked for the producer/consumer form specifically and the seam has largely eliminated it (§3.3
value domains, §3.4 status schema, §3.6 namespace partition, §3.1 stage-number partition, the
rules-over-merged-plan device). **Three residual producer/consumer dependencies survive**, of which
one is load-bearing: **the invocation target and arity of A's pipeline (F1, blocker)**, plus
`index.md`'s findings pointer (F6) and `METHODOLOGY.md`'s loop/"what a run produces" sections (F7).
**Sound:** two internal contradictions in the control loop (F2, F4) and one unexecutable amendment
path (F5).

**3. The floor — would either half fall below it?**
No. Floor = *one file created or one coherent edit to one file, with the content specified.* A plans
≥3 role-prompt files plus format references; B plans ≥8 files. Both are coherent whole tasks far
above the floor, and B remains divisible one level down. **No finding here; the division is
legitimate rather than a task that should have been left undivided.**

**4. Real joint or arbitrary cut?**
**Real joint.** What differs on each side, concretely: below the line an agent has read corpus
content *for meaning* and its output is *evidence carrying citations*; above it no agent has ever
seen a finding and its output is *bookkeeping over counts and states*. Disjoint inputs (corpus
content vs. paths/sizes/one-line statuses), disjoint outputs (cited findings vs. an inventory and a
status tree), disjoint characteristic failures (fabricated citation vs. a coordinator that peeks,
or work lost on restart), disjoint review criteria (does every citation resolve vs. is it blind and
idempotent). §1's round-1 correction — from *"no agent above reads the corpus"* (false: B's
decomposer opens corpus files) to *"reads for meaning"* — is the right restatement and makes the
claim true. The rejected alternative (method vs. envelope) is correctly characterised as a
packaging boundary. **I would keep this joint.**

---

## The six lenses

### 1. Factual — CLEAN, earned with citations

I checked every external citation the proposal makes. All resolve and say what is claimed:

- `Guarded_change/METHODOLOGY.md:139` — *"**Paths are validated, not assumed.**"* ✓ (cited §3.3)
- `Dragonfly/SKILL.md:19` — *"**Validate config paths at hunt start:**"* ✓ (cited §3.3)
- `Guarded_change/SKILL.md:28` — *"Step numbers below are the canonical stage numbers used
  everywhere"* ✓ (see nitpick F13 on attribution)
- Run-artifact convention: `Guarded_change/SKILL.md:26` (`changes/<slug>/`) and
  `Dragonfly/SKILL.md:31`, `Dragonfly/METHODOLOGY.md:143` (`hunts/<slug>/`) ✓ — §3.2's claim that
  the siblings keep run artifacts inside the skill directory is correct.
- §3.7's precedent note: neither sibling has a `stages/common.md` (`ls Dragonfly/stages/`,
  `ls Guarded_change/stages/`) ✓; both have `stages/charter.md` ✓;
  `Dragonfly/stages/charter.md:1` — *"The red-team charter (shared by stages 1, 4, 7)"*, i.e. read
  at specific stages, not a universal preamble ✓; `Architect/stages/common.md:3` — *"Every agent
  Architect dispatches reads this file first"* ✓. The divergence claim is accurate and correctly
  declared.
- §2-A precedents exist and are of the claimed kind: `Guarded_change/stages/stage-3.md:1-9`,
  `Dragonfly/stages/stage-7.md:1-7`, both charters ✓.
- §2-B precedents exist and have the claimed structure: `Dragonfly/METHODOLOGY.md` §§ *Why this
  exists* (:22), *The loop* (:45), *Stage index* (:72), *The two layers* (:95), *The config
  contract* (:106), *What a run produces* (:141), *Human-in-the-loop* (:172) ✓;
  `Stop-for-human` at `Dragonfly/SKILL.md:72` and `Guarded_change/SKILL.md:54` ✓; frontmatter +
  router table in both ✓; `dragonfly.companion.md` and `guarded-change.companion.md` exist ✓.
- §3.9 / §6 Architect citations: `combiner.md:6` *"None of the three is an author. You do not
  improve, rewrite, or adjudicate the material."* ✓; `combiner.md:57` *"A genuine conflict is kept,
  not resolved."* ✓; `node.md` loop steps 3–4 (:101–108) ✓; `divider.md:80-83` does offer `Union`
  as a home for a cross-half dependency ✓ — **so §6's reported contradiction between `divider.md`
  and `combiner.md` is real, and the proposal is right to report it and right not to rely on it.**
- Build root `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/` does not yet exist
  (`ls` → no such directory), consistent with a plan-only deliverable.

**Unchecked, declared:** §7's claim that all three round-1 reviewers endorsed the cut and none
objected. I cannot verify it — `split-review-r1-*.md` are out of bounds for me. I did not rely on
it, and I re-derived my own endorsement independently.

### 2. Logical — findings F2, F4, F5

The control loop of §3.5 contains two contradictions and §3.9's escape hatch does not terminate.

### 3. Missed opportunity — findings F1(fix), F10

The seam already fixes the invocation *arguments*; fixing the invocation *target* is one more line
in the same paragraph and closes the blocker. Separately, the seam could have made the read table
(§3.2) exhaustive over the skeleton — it currently omits `decisions.md` entirely.

### 4. Unstated assumptions & risks — findings F3, F8, F11

The largest unstated assumption is that A will infer, from `oversize` merely appearing in §3.4's
leaf state domain, that detecting and emitting it is A's duty — while §2-A explicitly disclaims the
over-size strategy.

### 5. Fidelity — CLEAN, earned by pinning the terms

I pinned each loaded operational term to the concrete mechanism the seam gives it, and each
mechanism does implement the property rather than proxy it:

| Term | Pinned to | Implements the property? |
|---|---|---|
| "blind roll-up" (P5) | §3.4 + §3.2 read table: the coordinator's input is **its own children's `STATUS` lines and nothing else**; `findings_path` deliberately removed | **Yes.** Removing the path field is what turns P5 from an exhortation into a structure — the coordinator has no address for a finding, not merely a rule against reading one. This is the single strongest thing in the proposal. |
| "terse per-child status" | §3.4: one line, five whitespace-separated fields, typed, no path | Yes — terse is bounded, not aspirational. |
| "cold" | §3.7 rule 1: no shared context with caller or siblings | Yes. |
| "read-only" | §3.7 rule 3: writes nothing except the output files its role names, via `.tmp`+rename | Yes; the round-1 `.tmp` conflict is resolved in the rule itself. |
| "independent" (P2) | duty in §3.7 rule 1; **enforcement mechanism assigned to A** at its dispatch point (§2-A), with §3.7's additions clause permitting it | Yes — the clause that stops additions-only from swallowing the enforcement is doing real work. |
| "verify" (P3) | §2-A: separate cold agent, **never the analyst that produced the finding**; operational definition of "unverifiable" is A's | Yes — the never-the-author constraint is fixed in the seam-adjacent sub-task rather than left to A. |
| "agreement-ranked" (P4) | §2-A matching + rank; surfaced upward only as `max_agreement`, a count of analysts (§3.4) | Yes. |
| "decompose" (P1) | §3.3 item record with fixed value domains + validated `locator` + §3.5 re-decomposition loop | Yes, subject to F3/F4. |
| "restart/resume" (P7) | §3.2 presence rule (write-complete-or-not-at-all) + §3.5 state table; split B-across-nodes / A-within-item | Mechanism is real; F2 defeats its termination. |
| "facts, not interpretation" (P8) | §3.7 rule 7 states the duty; **enforceability** assigned to A as a checkable rule in the role prompts, explicitly "rather than an exhortation" | Yes — the sub-task names the proxy failure and forbids it. |
| "Layer-2 config" (P6) | §3.6 partitioned namespaces + carve-out making the contract a rule over the merged plan | Yes. |

No term resolved to a proxy. Fidelity lens clean.

### 6. Completeness — findings F6, F7, F9, F11, F12

**The generative sweep was run.** Beyond ticking the four questions, I asked *"what load-bearing
element does this seam's own list of cross-half concerns fail to anticipate?"* and looked
specifically for: (a) the **entry point** of the invocation contract as distinct from its arguments
— **hit, F1**; (b) a **terminal failure state** and any attempt cap — **hit, F2**; (c) the
**producer** of each state in the state domain, not just its consumer — **hit, F3**; (d) the
**lifecycle** of a node that changes kind mid-run — **hit, F4**; (e) whether the stated **amendment
path** is executable by any role that actually exists in Architect — **hit, F5**; (f) whether
**every** inventory-dependent step of B's is inside the rules-over-merged-plan enumeration —
**hit, F6/F7**; (g) **concurrency and append semantics** of the shared run log — **hit, F9**; (h)
behaviour of the assembly rule on an **incomplete run** — **hit, F11**; (i) **empty-set edge values**
in the status arithmetic — **hit, F12**; (j) whether the **`stages/` layout table** is binding or
illustrative, the question §3.2 answered for the run-dir skeleton but §3.1 did not answer for itself
— **hit, F8**. I also swept for and found nothing wrong with: seam transport to descendants (§6
handles it: prepended verbatim, plus an absolute path, plus explicit propagation to every
descendant), the off-limits fence (carried in both sub-tasks), the floor (§3.11, unchanged), and
"what neither half owns" (§3.10, including test harness / packaging).

---

## Findings

### F1 — `blocker` — The invocation contract fixes the arguments but not the target or the arity of A's pipeline

**Where:** §3.3 *"The invocation contract. B's run driver invokes A's pipeline with exactly two
arguments: `item_dir` and `config_path`. A's pipeline begins on receipt of those two."*; §2-A
*"the run driver (the other half's) calls your pipeline"*; §2-B *"invokes the other half's per-item
pipeline on each leaf node with the two arguments §3.3 fixes"*.

**The defect:** the seam never says **what B's driver invokes** — which file, and whether "A's
pipeline" is *one* dispatchable agent that internally sequences analysts→verify→merge, or *three
successive dispatches that B's driver must step through*. Both readings are supported by the text:
§3.1's layout gives A three stage files (`stage-2.md … stage-4.md   A   analyst; verification;
merge`), which reads like three dispatches B walks; §3.3's "A's pipeline begins on receipt of those
two [arguments]" reads like a single entry.

**Why it cannot be repaired below the cut:** the two halves are planned concurrently and blind, with
no channel. B is explicitly forbidden to close it — §2-B: *"**Do not guess the other half's
filenames, stage numbers, purposes or config keys.**"* — and the driver step is **not** in §2-B's
enumeration of steps that may be written as rules over the merged plan (that list is *"the
`SKILL.md` router table, the `METHODOLOGY.md` stage index, the `METHODOLOGY.md` config-key contract,
the worked example config, the `Stop-for-human` section, and `findings.md`'s assembly rule"*).
Nor is the driver's target inventory-shaped: it is one specific unknown filename, not a rule over
the full file list. And §3.1 gives B no fallback convention — A *"need not use every number"* and may
use letter suffixes, so B cannot even infer that A's lowest number is the entry.

**Concrete failure scenario:** A plans `stage-2.md` (analyst, dispatched N times), `stage-3.md`
(verifier), `stage-4.md` (merge, writes `STATUS`) and assumes the driver dispatches them in order,
so it writes no pipeline-entry role. B, reading §3.3's "A's pipeline begins on receipt of those
two", plans a driver step: *"dispatch one agent on A's per-item pipeline entry file with `item_dir`
and `config_path`."* The two plans reach `Union`, which **is barred from resolving this**
(`combiner.md:6`, `:57` — a genuine conflict is kept, not resolved, and this one is not even a
textual conflict, just a hole). A practitioner holding the merged plan has no executable instruction
for how any analyst is ever spawned. **This is the load-bearing case the aiming file names: an
artifact one half must derive from the other's plan, invented blind, locally correct on both sides.**

**Remedy (in the seam text, one clause, no move of the joint):** fix A's entry point in §3.3 — e.g.
*"A's pipeline is a single agent whose role file is `stages/stage-2.md`; that agent dispatches
everything else A needs. B's driver dispatches exactly that one file, with those two arguments."*
Alternatively fix the opposite arity explicitly. Either settles it identically for both halves.

### F2 — `major` — §3.5 self-contradicts: the escalation terminal state is a state whose defined consequent is "re-run"

**Where:** §3.5 table row 3: *"`state=partial` or `state=failed` → **re-run the node.**"*; §3.5 row
4: *"After `sizing.max_resplits` re-splits the item is **escalated to the human** and left
`failed`."*

**The defect:** `failed` is defined as *re-run*, so an item that has been escalated and abandoned is
parked in the one state that means "run this again". There is **no terminal failure state** in
§3.4's domain (`done | partial | failed | oversize`), and §3.5 makes only `done` terminal.

**Concrete failure scenario:** a leaf whose source file is unreadable at analyst time (permissions,
binary content) writes `state=failed`. On the driver's next pass the rule fires: re-run. A's
within-item resume finds nothing completed, re-runs, fails again, writes `failed` again. The driver
never terminates and the run never reaches the roll-up, because a group is `done` only if every
child is `done` (§3.4). The `sizing.max_resplits` bound protects only the `oversize` path; nothing
bounds the `failed` path.

**Remedy:** add a terminal state (e.g. `escalated`) to §3.4's leaf and group domains with
*"terminal; do not re-run; counted as not-`done` for the parent"*, or bound `failed` re-runs with a
seam-fixed attempt cap. Both halves need it identically — A writes leaf `STATUS`, B's driver reads
it and B's coordinator aggregates it, so it cannot be settled by either half alone.

### F3 — `major` — Nothing assigns the *producer* of `state=oversize`; each half has textual grounds to think it is the other's

**Where:** §3.4 leaf state domain includes `oversize`; §3.5 *"`oversize` exists because B sizes an
item from its shape and A discovers at read time that it does not fit"*; §2-A's owned-list (P2, P3,
P4, P8, finding record, within-item resume, config keys, writing `STATUS`) — **over-size detection
appears nowhere in it**; §2-A's do-not-own list: *"You do not own and must not plan: decomposing the
corpus into items, **the over-size strategy**, …"*; §2-B: *"**P1** — decomposing and sizing the
corpus into items, **and the strategy for over-size items**"*.

**The defect:** §3.5's prose asserts A discovers over-size, but nothing in A's sub-task tells A to
detect it or to emit it, and A's explicit exclusion list names "the over-size strategy" as not A's.
A planner reading §2-A top-to-bottom can reasonably plan a pipeline whose leaf `STATUS` only ever
carries `done | partial | failed`. Meanwhile B's roles cannot produce `oversize`: B's decomposer
sizes from shape and would emit a normally-sized item, and B's driver *"may read `index.md`, any
`item.json` and any `STATUS`, and never a finding"* — it never reads item content and so cannot
discover a fit failure.

**Concrete failure scenario:** A never emits `oversize`; B faithfully implements the §3.5
re-decomposition consequent and the `sizing.max_resplits` escalation. Neither plan is locally wrong.
The merged plan contains an entire re-decomposition subsystem with **no producer for its trigger** —
P1's *"strategy for over-size items"* is implemented but unreachable, and an item that genuinely
does not fit one context window is silently analysed badly instead. This is the "portion both halves
assume the other owns" failure from question 1, and it survives because §4's coverage table checks
properties, not state producers.

**Remedy:** one line in §2-A's owned list — *"detecting at read time that the item does not fit and
writing `state=oversize` instead of running the pipeline"* — plus a matching clause in §3.4's leaf
state description. Detection is not the strategy, so this does not breach A's exclusion.

### F4 — `major` — The oversize→group transition breaks §3.2's leaf/group invariant and requires an unassigned cross-half overwrite of `STATUS`

**Where:** §3.2 *"`item.json`   B   present IFF this node is a LEAF (an item)"* and *"A node is a
LEAF — an item — if and only if it has `item.json`; otherwise it is a GROUP"*; §3.2 *"`STATUS`
leaf: A   group: B"*; §3.2 presence rule *"the existence of a file means the step that produces it
finished"*; §3.5 *"`state=oversize` (leaf) → re-decompose … **the node becomes a group**"*.

**The defect:** after re-decomposition the node has children **and still has `item.json`**, so the
IFF invariant is false for it; and its `STATUS` file — already written by **A** as a leaf line —
must now be replaced by a **group** line written by **B's roll-up coordinator**. Nothing says who
deletes `item.json` (deletion is not contemplated anywhere, and the skeleton is declared
**EXHAUSTIVE** with no removal semantics), and nothing says that a `STATUS` may be overwritten at
all — the presence rule's "existence means finished" reads the other way.

**Concrete failure scenario:** B's driver re-decomposes node `0.3` (oversize) into `0.3.1`/`0.3.2`.
`0.3/item.json` remains. On the next pass the driver applies §3.2's classification rule, sees
`item.json`, classifies `0.3` as a leaf again, reads its `STATUS` (`oversize`), and re-decomposes —
producing `0.3.3`/`0.3.4`, then again, terminating only when `sizing.max_resplits` trips and
escalating a node that was successfully split. Alternatively B plans deletion of `item.json` and A
plans `STATUS` as write-once ("the last act of your pipeline", §2-A), and the merged plan has A's
leaf line permanently shadowing the group line.

**Why it is cross-half:** the file being overwritten has an owner on each side of the cut. Neither
half can fix it alone.

**Remedy:** state the transition explicitly in §3.5 — who removes or supersedes `item.json`, that a
`STATUS` may be replaced exactly on this transition, and that the presence rule's "written complete
or not at all" applies to the replacement (`.tmp`+rename) — or avoid it entirely by having the
re-split emit children under a *fresh* node id and mark `0.3` terminal.

### F5 — `major` — §3.9's seam-amendment path cannot be executed by any Architect role, and if it were, it would not terminate

**Where:** §3.9 *"File it as a `blocker`/`major` finding in your own plan output. … It surfaces at
the node's plan red-team round, and `Severity` turns it into the next task
(`Architect/stages/node.md`, loop steps 3–4)."*

**The defect, in two parts.**

(a) **No role beneath this cut may file a finding.** The two halves go to child **nodes**
(`node.md:85-88`), which spawn **leaves** — and `leaf.md:47` is explicit: *"You do not file findings
— your output is a plan, and severities are for reviewers."* The node itself is barred too
(`node.md:35-37`: *"You never write plan content… Your own opinion of a plan is not a finding and
never becomes the next task."*). So the instruction §3.9 gives to each half — *"file it as a finding
in your own plan output"* — names an action neither the planner nor the node it reports to is
permitted to perform. It **cannot be executed as written**.

(b) **If a seam finding did reach `Severity`, the loop would not terminate.** Suppose a child node's
plan reviewer files *"the seam's §3.4 status schema is wrong"* as a `major`. `Severity` returns it
as that child node's next task (`node.md:106-108`), and the node loops *while `task` is non-empty*
(`node.md:76`, `:112`). But the seam is fixed by the **parent** and §3 forbids the child from
changing it (*"Neither half may change it"*). The child's planners cannot discharge the task, so it
returns unchanged every iteration — precisely the failure `combiner.md:81` names: *"it is handed to
a planner that cannot fix it, and it comes back to you next iteration unchanged, forever."*

**Concrete failure scenario:** child node `0.1` (half A) has a reviewer file the F1 blocker above.
`Severity` hands it back to `0.1`. `0.1` re-plans half A; the seam is still wrong; the next round
files it again; `0.1` never returns and neither does node `0`.

**Remedy:** §3.9 should route a seam objection **upward**, not into the child's own loop — e.g.
*"state it in a clearly-labelled `SEAM-OBJECTION` section at the head of your plan output, which
travels up through `Union` unmodified (`combiner.md`: discard nothing) to the parent node, and is
the parent's to act on."* That uses a channel that provably exists and does not create an
undischargeable task. This finding is about the seam's own escape hatch, not about the joint.

### F6 — `minor` — §3.4's justification rests on a pointer B cannot populate blind

**Where:** §3.4 *"The human-facing pointer is derivable (`nodes/<node_id>/` + A's declared
merged-findings filename) and is recorded once in `index.md` and in `findings.md`; the coordinator
never holds it."*

**Failure scenario:** `index.md` is written by B's decomposer (§3.2), and B does not know A's
merged-findings filename and is forbidden to guess it (§2-B). `index.md` is **not** in §2-B's
enumeration of rule-over-merged-plan steps (unlike `findings.md`, which §3.8 correctly makes one).
B therefore either omits the pointer — leaving `findings.md` as the only human-facing route, which
is fine for P5 but makes §3.4's stated justification false — or invents a filename. Fixable in place:
add `index.md` to §2-B's list, phrased as *"one row per node, each naming that node's merged findings
file as declared in the merged plan."* Does not affect the joint.

### F7 — `minor` — `METHODOLOGY.md`'s loop section and "what a run produces", and `SKILL.md`'s loop prose, are outside the rule-over-merged-plan enumeration

**Where:** §2-B's list of inventory-dependent steps names the router table, the stage index, the
config contract, the worked config, `Stop-for-human` and `findings.md` — but §2-B separately tells B
to follow `Dragonfly/METHODOLOGY.md` (*"why-it-exists, **the loop diagram**, the stage index, the two
layers, the config contract, **what a run produces**, human-in-the-loop"*), and both of those
sections must describe A's stages and A's per-item output files.

**Failure scenario:** B writes a loop diagram and a "what a run produces" section describing stages
2–4 and A's leaf outputs from the only information it has — §3.1's layout comment (*"analyst;
verification; merge"*) and §3.2's (*"per-analyst, per-analyst-verified, merged findings"*). If A's
plan differs in shape (see F8), the merged skill ships a methodology whose loop description does not
match its own stage files. Mitigated by the fact that §3 does give phase-level names, which is why
this is `minor` rather than `major`. Fix: add these two sections to §2-B's enumeration, or state in
§3.1 that a phase-level description drawn from the seam is sufficient and binding.

### F8 — `minor` — §3.1's layout table is not declared binding or illustrative — the answer §3.2 gave for the run-dir skeleton was not applied to §3.1

**Where:** §3.1 *"`stage-2.md … stage-4.md   A   analyst; verification; merge`"* versus, three
paragraphs later, *"Within its own range a half may use letter suffixes as the siblings do
(`stage-0a.md`), and **need not use every number**."* §3.2, by contrast, resolves exactly this
ambiguity for its own skeleton: *"**The skeleton is EXHAUSTIVE. Neither half may add a file or
directory to it.**"*

**Failure scenario:** A plans `stage-2.md` (analyst), `stage-2a.md` (dispatch/independence
enforcement), `stage-3.md` (verify), `stage-4.md` (merge) — permitted by the suffix clause — while B
writes `METHODOLOGY.md` prose and a stage index assuming stage 2 = analyst, 3 = verification,
4 = merge as §3.1's table states. The two are consistent here by luck; they need not be. One
sentence fixes it: declare the §3.1 role assignments **binding at phase level** (A must place its
analyst phase at 2, verification at 3, merge at 4, and may add suffixed files within those phases).

### F9 — `minor` — `decisions.md` is append-only, contradicting the presence rule, and appears in no row of the read table

**Where:** §3.2 *"`decisions.md`   B   append-only run log"* and, in the same section, *"**The
presence rule.** Every file above is written complete or not at all — write to a `.tmp` sibling,
then rename — so the existence of a file means the step that produces it finished."* Also §3.7 rule
3, which permits an agent to write *"the output file(s) its role names, each produced via the seam's
write-to-`.tmp`-then-rename rule"*.

**Failure scenario:** B's decomposer must record a rejected `locator` in `decisions.md` (§3.3) while
obeying a rule that says every file in the skeleton is produced by atomic rename — which cannot
express an append, and under which `decisions.md` existing would mean logging "finished". With
concurrent leaf pipelines (the driver *"bounds concurrency"*, §2-B) interleaved appends are also
unprotected. Additionally §3.2's read table — introduced as *"who may read what — this is the
blindness mechanism, stated once"* — lists no role as permitted to read `decisions.md`, so the log
is nominally unreadable by the driver and the human-facing stages. Fix in place: exempt
`decisions.md` from the presence rule with a stated append discipline, and give it a read-table row.

### F10 — `minor` — The exhaustive-skeleton rule leaves B no room for restart state, and B owns P7

**Where:** §3.2 *"**The skeleton is EXHAUSTIVE. Neither half may add a file or directory to it.**"*
versus §2-B *"**P7** — restart and resume **across** nodes: how a restarted run learns what is
done"*.

**Failure scenario:** B concludes that resume must be derived purely from file existence and
`STATUS.state`, which §3.5 does supply — so this is survivable — but B is also forbidden any
progress marker for a node it has *begun* and not finished, e.g. a leaf currently being processed by
a concurrent pipeline invocation. Absence of `STATUS` means "not yet" (§3.4), so a restart cannot
distinguish "never started" from "in flight in the previous, now-dead run", and re-dispatches work
that may still be mid-write. Fix: either carve out an explicitly named lease/marker file in §3.2 or
state that duplicate dispatch is safe because A's within-item resume makes it idempotent — the
latter is probably already true and simply needs saying, which is why this is `minor`.

### F11 — `minor` — §3.8's assembly rule is undefined for an incomplete run

**Where:** §3.8 *"one section per leaf node in `index.md` order, each embedding that node's merged
findings file verbatim, with its `STATUS` line as a header."*

**Failure scenario:** the run halts with two leaves `failed` and one never started (no `STATUS`, no
merged findings file). The rule instructs embedding a file that does not exist and using a `STATUS`
line that does not exist as its header. A practitioner executing the merged plan has no defined
behaviour. Fix: one clause — *"a leaf with no merged findings file contributes a header-only section
recording its state, or `NOT RUN` where `STATUS` is absent."*

### F12 — `nitpick` — `max_agreement` is undefined over an empty set

**Where:** §3.4 *"`max_agreement` — non-negative integer count of analysts: the highest agreement
count any surviving finding in this subtree reached"*; *"`max_agreement` is the max"* over children.
A leaf with zero surviving findings, or a group all of whose children have none, has no maximum.
Presumably `0`; say so, since `0` also reads as "one analyst agreed with nobody".

### F13 — `nitpick` — A quote is attributed to the wrong sibling

**Where:** §3.1 cites *"`Dragonfly/SKILL.md`: 'Step numbers below are the canonical stage numbers
used everywhere'"*. That exact wording is `Guarded_change/SKILL.md:28`. `Dragonfly/SKILL.md:34`
reads *"**Step numbers below are the canonical stage numbers** used everywhere (METHODOLOGY,
`decisions.md`)"*. The claim is true of both siblings; only the attribution of the quoted string is
off.

---

## What I explicitly did NOT find a problem with

Recorded so a later reader knows these were examined rather than skipped:

- **The joint itself.** Real, task-derived, correctly restated from round 1's false version.
- **The floor.** Both halves far above it; §3.11 passes it down unchanged and verbatim.
- **Seam transport.** §6's mechanism (prepended verbatim + absolute path + explicit propagation to
  descendants) is the right answer to a seam that must survive further division. It matches how
  `node.md:85-88` actually passes `division.first`/`division.second` to child nodes.
- **The removal of `findings_path` from `STATUS`.** This is the proposal's best decision.
- **The `Union`-cannot-reconcile point in §6.** Verified against `combiner.md:6,57` and
  `divider.md:80-83`. The contradiction with `divider.md` is real, correctly reported, and correctly
  not relied upon.
- **The alternative cut** (method vs. envelope) — correctly identified as a packaging boundary.
- **Namespace partition (§3.6)** and the worked-example carve-out — a genuinely self-contained
  solution to what would otherwise be a producer/consumer dependency.
- **The `common.md` divergence (§3.7)** — declared, with an honest precedent note, and B is told to
  state it in `METHODOLOGY.md`.
- **The off-limits fence** — carried into both sub-task texts and into §3.10.

---

## Summary

| ID | Severity | One line |
|---|---|---|
| F1 | **blocker** | §3.3 fixes the invocation's arguments but not its target or arity; B cannot write the driver step blind |
| F2 | major | §3.5: escalated items are "left `failed`", and `failed` means re-run — no terminal state |
| F3 | major | No half is assigned to *produce* `state=oversize`; A's exclusion list points away from it |
| F4 | major | oversize→group breaks the `item.json` IFF-leaf invariant and needs an unassigned cross-half `STATUS` overwrite |
| F5 | major | §3.9's amendment path is unexecutable (`leaf.md:47`, `node.md:35-37`) and non-terminating (`combiner.md:81`) |
| F6 | minor | `index.md`'s findings pointer is outside §2-B's rule-over-merged-plan list |
| F7 | minor | `METHODOLOGY.md` loop / "what a run produces" likewise outside it |
| F8 | minor | §3.1's layout table not declared binding or illustrative |
| F9 | minor | append-only `decisions.md` contradicts the presence rule; absent from the read table |
| F10 | minor | exhaustive skeleton leaves B no in-flight marker while B owns P7 |
| F11 | minor | §3.8's assembly rule undefined for an incomplete run |
| F12 | nitpick | `max_agreement` undefined over an empty set |
| F13 | nitpick | quote attributed to `Dragonfly/SKILL.md` is `Guarded_change/SKILL.md:28` |

**Lens verdicts:** Factual — clean (earned, citations above). Logical — F2, F4, F5. Missed
opportunity — F1's remedy, F10. Unstated assumptions & risks — F3, F8, F11. Fidelity — clean
(earned, terms pinned in the table above). Completeness — F6, F7, F9, F11, F12 (generative sweep
run; ten sweep targets named above).

**Was any portion of the task left unaddressed?** Only via F3 — the `oversize` producer, which is
part of P1's *"strategy for over-size items"*. Everything else in the task is owned.

**AGREEMENT: I do not object to going forward with this cut. I endorse the joint.** All thirteen
findings are seam-text defects fixable in place by the divider; none of them argues for a different
boundary, and F1 in particular is closed by one clause in §3.3. This task is divisible and this is
the right division of it.
