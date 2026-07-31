# Split review — round 2, reviewer A

Reviewing the proposed division in `Architect/runs/data-distiller/0/split-round-2.md` (driver plane
vs. worker plane) against the task, the granularity floor, and the source material.

I read: `split-round-2.md`; `Guarded_change/{SKILL.md,METHODOLOGY.md,guarded-change.companion.md,
stages/stage-1.md,stages/stage-5.md}`; `Dragonfly/{SKILL.md,METHODOLOGY.md,dragonfly.companion.md}`;
directory listings of both siblings' `stages/`; `Architect/stages/{node.md,leaf.md,combiner.md}`.
I did **not** read, list or grep `/home/zero/Desktop/claude-code-skills/Data-Distiller/`, and did not
read the round-1 review files.

**Bottom line: the cut itself is a real joint and I would keep it. The shared interface I1–I10 is
where the defects are** — and because both halves receive I1–I10 verbatim as a binding constraint
they may not re-scope, a defect in the interface is a defect neither half can repair and no later
reviewer sees the alternative to.

---

## Findings

### F1 — `status.json` has no producer, and both candidate producers are barred — **blocker**

I5 (`split-round-2.md:170-176`) fixes the status record's schema. I3 (`:164-166`) makes the whole
blindness barrier rest on it: *"A driver-plane agent is handed `manifest.json` and `status.json`
paths only … this is what makes the blindness structural."* **Nothing in either sub-task says who
writes it.**

It is not merely unassigned — each candidate is affirmatively excluded:

- **The driver cannot write it.** I5's `counts` field is *"findings produced / findings surviving
  verification / findings in the merged output."* Producing those numbers requires reading the
  findings, which I3 (`:164-166`) and I7 (`:184`, *"the driver plane may not read this record at
  all"*) forbid.
- **The worker is never told to.** Sub-task two's file list (`:215-232`) gives outputs for every
  worker file — manifest, findings, verified, merged, `FINDINGS.md` — and never mentions a status
  record. Its ownership paragraph (`:237-241`) does not include it either.

This is round 1's *"terminal deliverable has no producer"* defect (dispositioned at `:378` via I9)
recurring on a different object, and on the more load-bearing one: `FINDINGS.md` missing would be
visible to the human, whereas a missing `status.json` silently disables resume *and* the blind
roll-up.

**Failure scenario:** both leaves plan their halves faithfully; `Union` (`Architect/stages/
combiner.md:37-52`) concatenates them; the merged plan contains no step that creates
`<run>/items/<item_id>/status.json`. The node has nothing to read, so it either stalls or is
re-planned to read `merged.md` — collapsing the barrier the interface exists to enforce.

### F2 — I3 and I9 contradict each other; the driver plane cannot dispatch merge as specified — **blocker**

I3 (`:164-166`): a driver-plane agent is *"never [handed] a `analyst-*.md`, `verified.md`,
`merged.md` or `FINDINGS.md` path."*
I9 (`:190-193`): *"`<run>/FINDINGS.md` is written by a dispatched merge agent … The driver plane
dispatches it, **names its path**, and hands that path to the human."*

The driver is simultaneously forbidden to hold a `FINDINGS.md` path and required to name it and hand
it over. The same collision recurs one level down: sub-task two item 5 (`:228-232`) has `merge.md`
run *"at a roll-up node, across the merged outputs of that node's children"* — those inputs are
`<run>/rollup/<child_id>/merged.md` (I3 `:162`), and only the driver dispatches (sub-task two
`:243-246` bars the worker plane from specifying dispatch). So the driver must name `merged.md`
paths as another agent's inputs, which I3 forbids.

The barrier the task actually specifies is **content** blindness — *"a coordinating agent never
reads the findings themselves"* — not **path** blindness. I3 over-tightened it into a rule that
contradicts the run's own control flow. As written, the driver-plane leaf cannot produce an
executable `stages/node.md`: every dispatch it must specify violates a binding interface clause it
is forbidden to re-scope (`:140-143`).

**Suggested repair** (the divider's to make, not mine to impose): restate I3's clause as *the driver
plane may construct and pass findings-artifact paths but never opens one; only `manifest.json` and
`status.json` may be read by a driver-plane agent.*

### F3 — analyst independence is nominal, not structural — **major**

The task requires *"N independent cold analyst agents per item."* I2 (`:149-154`) pins independence
to an instruction in `common.md` (*"cold independence (no shared context with the dispatcher or with
siblings)"*) and to *"read-only over the corpus."* But I3 (`:277`) places every analyst's output at
`<run>/items/<item_id>/analyst-<k>.md` — a **predictable sibling path in the directory the analyst
is working in** — and "read-only over the corpus" is a *write* restriction, not a read restriction
on the run directory. Nothing in I1–I10 forbids analyst 2 from opening `analyst-1.md`.

Round 1 was faulted for pinning blind roll-up to *"a schema plus an instruction, not a barrier"*
(`:384`) and round 2 fixed that structurally. The identical defect in the identical shape survives
untouched on independence — which is the property the agreement ranking (I7 `agreement_count`) is
entirely derived from. If independence is only nominal, `agreement_count` measures copying.

**Failure scenario:** analyst 3 is dispatched after analysts 1–2 have returned (any staggered
dispatch under a concurrency ceiling produces this), reads their files, and reproduces their claims.
`merge.md` records `agreement_count: 3` for a claim one analyst made. Verification does not catch it
— the citation is genuine.

### F4 — the seam's central claim ("nothing crosses") is false: driver-plane `node.md` consumes worker-plane `common.md` — **major**

`:330-333`: *"What each half produces that the other consumes: **nothing.** That is the point of
this round."* But sub-task one item 3 (`:107`) states that `stages/node.md` *"includes
`stages/common.md` verbatim … and does not restate its rules"* — and `stages/common.md` is written
by the other half (sub-task two item 1, `:215-216`: *"this half writes the text"*).

Two consequences, beyond the misstatement:

1. **The rule set is wrong for the consumer.** I2 fixes common.md's contents as *"exactly these
   rules"* (`:149`), all of them corpus-reader rules: read-only over the corpus, `off_limits`,
   cite-or-it-doesn't-count, facts-not-interpretation. A node reads no corpus, produces no
   citations, and makes no factual claims. Meanwhile the node's actual concerns — the concurrency
   ceiling, resume, the blindness barrier — appear nowhere in the common set, so the one file the
   driver half writes as a prompt inherits four rules it cannot act on and none it needs.
2. **It is the diagnostic for a mis-placed rule.** A rule only one role can act on belongs to that
   role. Either `node.md` should not include `common.md` (in which case I2's *"included verbatim by
   every dispatched agent"* is consistent only if a node is not "dispatched" — which is false: the
   driver dispatches nodes), or `common.md` is genuinely shared and its fixed rule list is missing
   the driver-side half.

Either way the cut runs *through* `stages/node.md` rather than around it, which is precisely what
`:326-327` claims it does not.

### F5 — the stage/role index's "one-line purposes (fixed below)" are not fixed anywhere — **major**

Sub-task one item 1 (`:93-94`) requires `SKILL.md` to carry *"the stage/role index table listing
every file under `stages/` … with a one-line purpose,"* and `:129-130` says the driver half *"may
name those files and their one-line purposes (**fixed below**)."* I1 (`:145-147`) fixes **filenames
and plane assignment only** — no purposes. Sub-task one is explicitly self-contained (`:73-75`), so
the driver-plane planner never sees sub-task two's descriptions of those files.

So the driver half must invent one-line purposes for five files whose content the other half writes,
with nothing to reconcile them and `Union` (`Architect/stages/combiner.md:39-41,62-64`) forbidden to
harmonise. This lands on exactly the property both siblings gate their own self-check on —
*"SKILL.md ↔ METHODOLOGY.md ↔ stage-file consistency on every rule stated in more than one place"*
(`Guarded_change/SKILL.md:82-84`; `Dragonfly/SKILL.md:88-89`).

**Failure scenario:** the driver plans a `SKILL.md` row reading *"`stages/verify.md` — re-check
citations and drop the unverifiable"*; the worker plans `verify.md` to also record dropped findings
and to handle the nothing-survives case. Merged, the router under-describes the stage, and the
skill's own standing consistency criterion fails on delivery.

### F6 — I8 starves the worker plane of config values `decompose.md` provably needs — **major**

I8 (`:186-188`): *"Worker-plane files read only `item_definition` and `off_limits`."* But sub-task
two item 2 (`:217-221`) makes `decompose.md` responsible for decomposing **the corpus** — it must
know where the corpus is, i.e. `corpus_root`, and there is no manifest yet to supply a locator.
Second instance: I6 (`:178-180`) says which over-size strategy applies is the worker plane's rule
while *"the allowed set is a config key"* the driver owns — so `decompose.md` must honour
`oversize_strategies` to avoid selecting a strategy the corpus config disallows, which I8 forbids it
to read.

Neither half may re-scope I8 (`:140-141`), and nothing in I1–I10 assigns the driver the duty of
passing `corpus_root` or `oversize_strategies` down as dispatch inputs. The wiring is unowned.

**Failure scenario:** a corpus config sets `oversize_strategies: [window, sample]` (splitting is
meaningless for that corpus). `decompose.md`, unable to read the key, marks an over-size item
`strategy: split`. The driver validated the key and never re-checks the manifest against it, because
I4 (`:184-188` / `:286-288`) makes `strategy` a worker-produced field.

### F7 — the `split` strategy has no on-disk or manifest representation — **major**

I6 (`:178-180`) fixes `split` as *"divide the item into sub-items and recurse."* Nothing else in the
interface supports it:

- I3's layout (`:156-163`) has `<run>/items/<item_id>/…` and `<run>/rollup/<node_id>/…` and **no
  path for a sub-item** or for a sub-item's roll-up.
- I4's manifest entry (`:168-171`) has `item_id`, `locator`, `size`, `fits`, `strategy` — **no
  parent/child linkage**, so a sub-item cannot be related to the item it came from.
- The recursion itself is dispatch — driver-owned — triggered by a decision the worker made, and no
  interface object carries that decision to the driver except `strategy` in a manifest the driver
  does read (I3 permits it). But with no sub-item layout, the driver has nowhere to put the result.

Since neither half may *"silently extend"* an interface object (`:140-141`), the worker-plane
planner must either plan `split` as unimplementable or extend I3/I4 in violation of the binding —
and the driver-plane planner, planning independently, will not extend them the same way. This is a
load-bearing element of the task (*"pick a per-item strategy when an item does not fit"*) whose most
structurally demanding option is unrepresented.

### F8 — "both siblings' precedent" is false for two of the sections the driver half is told to write — **minor**

- `:87-88` cites a *"cold-start guard section (both siblings' precedent: `Dragonfly/SKILL.md:22`)."*
  `Dragonfly/SKILL.md:22` is indeed `## Before you start: cold-start guard`. But
  `Guarded_change/SKILL.md` has **no such section** — `grep -n 'cold-start' Guarded_change/SKILL.md`
  returns nothing, and its section list is Inputs / Loop / Stop-for-human / Self-check only.
- `:95-100` describes the METHODOLOGY section list as *"the section shape both siblings share"* and
  includes *Trigger*. `Trigger` exists only in `Dragonfly/METHODOLOGY.md:161`;
  `Guarded_change/METHODOLOGY.md` has no `Trigger` section (headings: Why this exists 18, The loop
  35, Stage index 67, The two layers 88, The config contract 103, What a run produces 154,
  Human-in-the-loop 198).

Neither section is a bad idea; the sourcing claim attached to them is wrong, and a leaf checking its
plan against the sources will find the citation does not support what it is cited for. (Correctly
verified, by contrast: `Guarded_change/METHODOLOGY.md:103-152` is the annotated config skeleton;
`:143` does name an operative copy; `Guarded_change/stages/stage-1.md:8` and `stage-5.md:7` are
invoking-agent procedure, so `:320-322`'s rejection of the reader-based joint holds; both companion
files exist and are concrete instances pointing at METHODOLOGY for the contract, so item 4 at
`:108-112` is accurate.)

### F9 — `.json` run artifacts depart from the house shape the plan is checked against — **minor**

I3 (`:157-158`) fixes `manifest.json` and `status.json`. **Neither sibling produces a single
non-markdown run artifact:** `Guarded_change/METHODOLOGY.md:154-168` lists `0-baseline.md` …
`decisions.md`; `Dragonfly/METHODOLOGY.md:141-153` lists `symptom-ledger.md` … `decisions.md`; and
both configs are YAML **inside** a markdown file (`guarded-change.companion.md:1-8`). The choice may
well be right — machine-read state is a real difference, and Architect itself uses
`<run>/memo/<node_id>.json` — but it is fixed by divider fiat, is a visible departure from the
source material the task names as the checking standard, and neither half may revisit it.

### F10 — no run-level decision / human-gate record, and I3's exhaustiveness is undefined — **minor**

Sub-task one assigns the driver half *"stop-for-human and human-in-the-loop"* (`:120-121`). Both
siblings make that an on-disk artifact and describe it as load-bearing, not merely audit —
`decisions.md` is *"the gate log and the iteration-cap's memory"* (`Dragonfly/METHODOLOGY.md:152-153`;
`Guarded_change/METHODOLOGY.md:177-182`). I3's layout contains no equivalent. Compounding it, I3
does not say whether the layout is **exhaustive**: `:140-141` bars *"silently extend[ing]"* a listed
object, which leaves it genuinely ambiguous whether a half may add a file. Two halves planning
concurrently will resolve that ambiguity differently, and `Union` preserves the conflict rather than
resolving it (`Architect/stages/combiner.md:57-61`).

### F11 — "disjoint failure sets" is overstated on the one term that justified the cut's placement — **minor**

`:325-327`: worker-plane files *"fail by an artifact that is uncited, unverified, interpreted, or
**steered**"*, and *"Those are disjoint failure sets."* But steering is prevented by the
blind-roll-up barrier, which `:118-120` assigns to the driver plane *"in full and exclusively."* So
one of the four named worker failure modes has its only defence on the other side of the cut. The
ownership assignment is clear enough that this is a rationale flaw rather than a scope gap — but the
disjointness claim is what licensed moving `stages/node.md` across (`:326-327`), so it should be
stated accurately rather than resting on a term that appears on both lists.

### F12 — stray citation defect — **nitpick**

`:98-99` cites `Dragonfly/METHODOLOGY.md:106-131*` — the trailing `*` is unexplained, and the config
contract section actually runs 106–140 (`## What a run produces` begins at 141).

---

## Verdicts by lens

**1. Factual — issues found (F8, F9, F12).** Earned with citations: I checked every source citation
in the file. Verified correct: `Guarded_change/SKILL.md:25-52` (the Loop section), `METHODOLOGY.md:
103-152` (annotated config skeleton), `:143` (names the operative copy), `:88-100` (The two layers),
`stages/stage-1.md:8` and `stages/stage-5.md:7` (invoking-agent procedure, supporting `:320-322`);
`Dragonfly/METHODOLOGY.md:95-102` (The two layers), `SKILL.md:22` (cold-start guard exists **in
Dragonfly**); both companion files exist in the claimed house form; `Architect/stages/node.md:50-53`
(two child nodes, `Union`) and `leaf.md` inputs (`node.md:46`, `leaf.md:16-18`) support `:330-333`'s
account of the execution model. Falsified: "both siblings" for cold-start guard and for `Trigger`
(F8); the all-markdown artifact convention (F9); the Dragonfly line range (F12).

**2. Logical — issues found (F2, F5, F6).** Each is an internal contradiction between two clauses
both halves are bound to obey simultaneously, independent of any source.

**3. Missed opportunity — one observation.** Alternatives (a), (b) and (c) are weighed and the
grounds given for (b) — that the config keys thread through every file, so the seam gets *larger* —
are sound. What is not weighed is **returning `null`**. I1–I10 fix the file set, the on-disk layout,
three record schemas, the config key set and the terminal producer; that is a substantial share of
the architecture decided at the divider, leaving each half largely to write file contents against a
fixed skeleton. That a seam needs ten binding clauses is at least weak evidence about how separable
the task is at this line. I am **not** filing it as a finding — the halves are genuinely coherent and
above the floor, and fixing shared objects is legitimate seam work — but the option deserved a
paragraph alongside (a)–(c).

**4. Unstated assumptions & risks — issues found (F1, F3, F7).** All three are things taken for
granted: that somebody writes the status record; that cold dispatch alone makes analysts
independent; that `split` needs no representation because it is "just recursion."

**5. Fidelity — issues found (F2, F3, F4).** Terms pinned to mechanisms, in the divider's own text:
*"cold"* → a dispatched agent with no shared context, I2 `:150`; *"read-only"* → a corpus write ban,
I2 `:151` — **and this is the pin that fails F3**, since it silently permits reading sibling
analysts' outputs; *"cite"* → a corpus locator a verifier can re-open, I7 `:300-301`; *"verify"* →
re-open every citation and drop what does not resolve, sub-task two item 4 `:226-227`; *"decompose"*
→ items per `item_definition`, sized, with a strategy, emitting a manifest, item 2 `:217-221`;
*"agreement"* → `agreement_count` set by merge across N analysts, I7 `:300-302` + item 5 `:228-232`;
*"blind roll-up"* → **path**-withholding, I3 `:164-166` — but the task says the node never **reads**
findings, and substituting path-blindness for content-blindness is what produces F2. *"agent"* →
a separately dispatched context reading one prompt file, consistent throughout.

**6. Completeness — issues found (F1, F5, F7, F10).** Structural checklist run against the four
questions and against the house shape (SKILL / METHODOLOGY / stages / config / README / install —
all present and assigned). **Generative sweep run.** It looked for: an owner for every artifact named
in I3 (found F1 — `status.json`; `config.snapshot.md` is unassigned too but is unambiguously
driver-side, so I do not file it); a path for every state the method can be in (found F7 —
sub-items); a producer *and* a consumer for every field of every fixed record; a home for every duty
assigned in prose but not in the layout (found F10 — human-gate/decision log); and a reconciliation
mechanism for anything the two halves each state independently (found F5 — stage-index purposes).
Also swept without finding an issue: resume coverage (per-unit `status.json` plus manifest-existence
is sufficient), the roll-up tree's own state (`rollup/<node_id>/status.json` covers the root), and
`FINDINGS.md`'s producer (I9 assigns it).

## The four questions

1. **Coverage.** Every bulleted property of the task maps to a named file on one side, and I found no
   portion both halves assume the other owns *at the file level*. The gaps are at the **artifact**
   level: `status.json` (F1) and sub-item state (F7) are orphaned, and the stage-index purposes (F5)
   are the one thing both halves will produce independently.
2. **The seam.** Stated, at length, and non-directional — which correctly answers round 1's decisive
   blocker; the execution model at `Architect/stages/node.md:50-53` and `leaf.md:16-18` does support
   it. But it is **not sound as written**: F2 is a contradiction inside it, and F4 shows its headline
   claim ("nothing crosses") is false because `node.md` consumes `common.md` verbatim.
3. **The floor.** Not violated. Five files plus an install step against five files, floor = one file
   with its content specified; both halves are far above it and both remain coherent whole tasks.
   No finding.
4. **Real joint or arbitrary cut?** **Real.** What differs across the boundary is genuine and
   nameable: the driver plane's artifacts are read by the run itself and fail by stalling, exceeding
   the ceiling, or failing to resume; the worker plane's artifacts are read by a human downstream and
   fail by being uncited, unverified, or interpreted. They are checked by different means (control-
   flow inspection vs. re-opening citations). The claim of strict disjointness is overstated on one
   term (F11), and the cut runs through `node.md` rather than cleanly around it (F4), but the joint
   is not an arbitrary bisection and I would not send the divider looking for a different line.

## Summary of severities

| # | Finding | Severity |
|---|---|---|
| F1 | `status.json` has no producer; both candidates barred | blocker |
| F2 | I3 vs I9 — driver must name paths I3 forbids it to hold | blocker |
| F3 | Analyst independence is an instruction, not a barrier | major |
| F4 | "Nothing crosses" is false — `node.md` includes `common.md` | major |
| F5 | Stage-index "one-line purposes (fixed below)" are not fixed | major |
| F6 | I8 denies `decompose.md` `corpus_root` / `oversize_strategies` | major |
| F7 | `split` has no sub-item path or manifest linkage | major |
| F8 | "Both siblings" false for cold-start guard and `Trigger` | minor |
| F9 | `.json` artifacts depart from the all-markdown house shape | minor |
| F10 | No decision/human-gate log; I3's exhaustiveness undefined | minor |
| F11 | "Disjoint failure sets" overstated on *steered* | minor |
| F12 | `Dragonfly/METHODOLOGY.md:106-131*` — stray `*`, wrong range | nitpick |
