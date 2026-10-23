# Test venue — isolation or assembled run, item by item

**Owner ruling, 2026-07-29, verbatim:**

> "A component should be tested in isolation to determine if it functions correctly, but, some components
> can only be properly tested in the fully functional mechanism that they go in. This distinction has, on
> many occasions, resulted in *days* being wasted trying to create increasingly elaborate test mechanisms
> to test trivial little things that would be simplicity its self to test by just plugging them into the
> finished thing and seeing what happens."
>
> "What I understood from your description of the issue regarding the moving floor thing was a combination
> of just a badly designed test, and a mechanism that required the full Architect skill to be assembled and
> run on a real task before it could be properly tested (or at least, tested without the test mechanism
> being larger and more complex than Architect its self)."
>
> "if a component can be tested in isolation, it should be. If testing it requires more than three
> iterations of the test mechanism, reconsider if it should be tested in isolation or on a test run of the
> assembled thing."

**Locus: record 2544.** The middle paragraph above was omitted from this document's first version and is
restored. **It matters twice.** It is the owner speaking *about the floor test specifically*, saying it
needed the assembled skill — which **independently corroborates the N-14 venue decision below**, made
before this text was available. And it adds a **second bound the three-iteration rule does not state:** a
test mechanism must not be *"larger and more complex than Architect its self."* **Size, alongside
iterations.** Both bounds apply; either one firing is enough to force the venue question.

**Loci for the other rulings cited here:** node-path merge **2524 item 2** (hedged: *"should probably"*);
decision log **2524 item 3**, same message; `Union` generalized **2680**.

**How this is applied here.** Isolation is the **default**, not the fallback. The count is of **rebuilds of
the test mechanism**, not runs of the test. At more than three, the rule does not say *stop testing* — it
says **reconsider the venue**, and "still isolation, for this reason" is a legitimate outcome provided the
decision is actually made.

**What this supersedes.** Two earlier positions, both wrong:
- *"A per-element harness is an instrument, not a gate; cut the behavioural arms"* — the orchestrator's,
  cited to record 1572, which does not contain it. Wrong because **isolation testing is the default.**
- *"A broken test gets repaired, not deleted"* — this runner's, argued from record **1449** item 1. Wrong
  as a general rule: repair is right *up to a point*, and past three rebuilds the correct move is to
  reconsider the **venue**, not to repair again. **Record 1449 item 1 was one instance and must not be
  cited as a general repair-don't-delete principle.**

**One counting convention, declared because it changes an answer — and CORRECTED 2026-07-29 after reviewer
S ruled on it.** `ruleplace.sh`'s ancestry includes two attempt-1 checkers that were bare `exit 0`
printers. They are **not** counted against the current mechanism, because they tested attempt 1's corpus,
which this element does not contain. **S upheld the exclusion as not self-serving.**

⚠ **But the ground originally published for it was factually false**, and S caught that too: this document
said the printers tested *"the 237-line monolith, since demolished."* They did not — the printers ran over
**attempt 1's** files, and the 237-line monolith was **attempt 2's** `charter.md`, written after attempt 1
was archived at `8ca7197`. **The two never coexisted.** Publishing a wrong reason defeats the purpose of
publishing the convention at all.

⚠ **And the count was wrong: it is 3, not 2.** This document names row A's mechanism as *"`ruleplace.sh` +
`rules.tsv`"*, and **`rules.tsv` is the probe set** — `ruleplace.sh` is a generic interpreter over it.
Measured: `rules.tsv` was **72** lines at `37f5db0`, **89** at `c28db2c`, and **128** on disk when S ruled.
**Three builds, from attempt 2 alone. Row A is AT THRESHOLD** — the same status that triggered a freeze for
`mutation-test.sh` and a venue change for N-14, **and it received neither.** The runner's framing of the
question as "2 or 4" was a false binary that excluded the right answer.

---

## The inventory

| # | What needs verifying | Venue | Mechanism | Rebuilds | Status |
|---|---|---|---|---|---|
| **A** | Each rule is stated in the file that must state it | **Isolation — decision made at threshold, below** | `ruleplace.sh` + `rules.tsv` | **4 — OVER THRESHOLD** | ✅ 122/0 gating; design now **frozen** |
| **B1** | No *verbatim* rule duplicated across files (N-06, N-26) | **Isolation** | `shared_spans.py` | **1** | ✅ running, 0 undeclared |
| **B2** | No *paraphrased* rule duplicated | **Isolation, oracle = cold reviewer** | — | **0 scripts, and none will be built** | ⚠ see below |
| **C** | Fork fidelity B01–B19 lands where claimed (N-03) | **Isolation, oracle = cold reviewer** | script proxy **retired — and the retirement is now PERFORMED, not just declared** | **2, both failed** | ✅ **reviewer T verified B01–B19 by hand, both directions, CLEAN** |
| **D** | The oracles can fail (Part C) | **Isolation for in-place edits; COLD REVIEWER for semantic inversion** | `mutation-test.sh` | **4 — S's append attack fired the clause** | ⚠ class relabelled **IN-PLACE NEGATION**; not extended |
| **E** | Verbatim reviewer records are real final messages | **Isolation** | `extract_records.py` + `fixtures/extract-gate` | **2** | ✅ gate tested both directions |
| **F1** | A composed reviewer prompt does **not** open with a spurious prompt-set defect (the O-BLOCKER-1 repair) | **Isolation** | one dispatch | **1** | ✅ **RUN — 3/3 clean.** `8-harness.md` |
| **F2** | Each composed prompt returns an artifact of the **shape** its role owes | **Isolation** | one dispatch per role, n=1 | **1** | ✅ **RUN — 3/3 correct**, and it produced 3 findings no reviewer found |
| **F3** | The granularity floor changes reviewer behaviour | **Isolation, 3rd attempt, design dictated by the owner** | vary the floor | **2** | 🔨 see below |
| **F4** | Completeness tier (iii) catches a section neither list names | **Isolation** | fixture + one dispatch | **1** | ⏸ available, lower priority |
| **G1** | The floor's **position** before the lens block (N-14) | **ASSEMBLED RUN** | — | **3 — AT THRESHOLD** | 🔀 **venue changed** |
| **G2** | A `Union`-joined plan pair survives `Memo_write` and the red-team | **ASSEMBLED RUN** | — | 0 | needs the loop |
| **G3** | The divider's self-review loop terminates | **ASSEMBLED RUN** | — | 0 | needs the loop |
| **G4** | `"or get stuck"` behaviour | **ASSEMBLED RUN** | — | 0 | blocked: undefined in the spec |
| **G5** | Architect produces a detailed Data-Distiller plan (record 1572) | **ASSEMBLED RUN** | — | 0 | the done criteria |

---

## The four decisions that are not automatic

### A — row A is now at FOUR, and the venue decision is made rather than deferred

**This is the second time this document has been wrong about row A's count, so the stricter metric is
adopted.** Reviewer S counted `rules.tsv` builds by line count (72 → 89 → 128 = 3). This session added
roughly twenty-four more rows — probes for the pass-3 repairs, and for **N-15a / N-20 / N-25**, which were
gating with **no probe at all**. **By S's metric that is build 4, and row A is over threshold.**

**The lenient reading is available and is not taken.** One could argue the *mechanism* — per-file positive
assertions, normalized, interpreted from a TSV — has not been redesigned since `37f5db0`, and that adding
a row is *using* it rather than *iterating* it. **That reading is rejected here**, because the runner
already used the lenient reading once (the "2 or 4" framing) and was wrong, and because a rule you can
always satisfy by re-describing what counts as an iteration is not a rule.

**Decision: row A STAYS IN ISOLATION, and the threshold buys a discipline rather than a venue change.**

- **No other venue can answer its question.** *"Is this rule stated in this file?"* is not observable from
  a run of the assembled skill — a good Data-Distiller plan does not tell you which file the granularity
  rule lives in. **N-14 could move because its question is behavioural; row A's is not.**
- **It has never returned a false clean on the thing it actually asserts.** Every failure charged to it —
  N-03's vocabulary overlap, blindness to negation-by-append, blindness to paraphrase — is a failure of a
  *different* question that was loaded onto it. **On per-file placement it has repeatedly caught this
  session's own regressions**, including a duplicated `DISCARD NOTHING` and three stale anchors.
- **The discipline the threshold imposes: the mechanism's design is now FROZEN.** Table rows may be added
  to close a coverage gap, because an uncovered gating criterion is a hole rather than a redesign. **Any
  change to how a probe is evaluated — a new mode, a new threshold, a new scoring rule — is out of
  bounds**, and if one is ever needed, that is the signal to change venue rather than to build again.
  The N-03 sub-probe is the worked example of what this rule would have prevented: it was two evaluation
  redesigns inside row A, and both failed.

### B2 / C — two things stay in isolation but stop being tested by a script

**C, fork fidelity, is the clearest case of the failure the owner described.** Two script mechanisms have
been built for it and both were near-vacuous:

1. *"destination file exists and is non-empty"* — **nineteen probes that pass for any nine non-empty
   files.**
2. *60% description-term overlap* — reviewer Q ran each rule's terms against all nine files and found
   **9 of 19 rules also pass against a file they were never claimed to be in**; **B09 passes all eight.**
   For nearly half the rules the probe returns the identical PASS had the allocation table named the
   **wrong** destination.

A third script attempt is *permitted* by the rule. **It is not taken**, because both failures share one
structural cause: all nine files are written in one design's vocabulary, so any keyword proxy for *"is
this rule stated here"* is measuring shared vocabulary. **That is an increasingly elaborate mechanism for a
trivial question.**

**The question is still isolation-testable — just not by a script.** A cold agent reading the fork source
against the allocation table answers it directly, and reviewers **M**, **N** and **Q** have each done it
successfully. **So the oracle for N-03 is cold-reviewer rule-by-rule verification, recorded per rule.**
The script probe is **kept but demoted**: it is a cheap smoke check for gross breakage and **is no longer
described anywhere as fork-fidelity verification.**

**B2 is the same shape.** `shared_spans.py` catches verbatim spans and **cannot see a paraphrase** — four
live ones were found by hand (three by reviewer O, one by Q). Paraphrase detection is a semantic
judgement; **no script will be built for it.** The oracle is the cold reviewer, and `charter.md` must stop
claiming the composition rule is "mechanically enforced" full stop — what is mechanically enforced is the
verbatim subset.

### D — the mutation self-test is at three, and is therefore FROZEN

Iterations: v1 (deletion/relocation/insertion/control), v2 (+duplication), v3 (+negation, and the fix to
the exemption arm that reviewer P showed was a printer). **That is three. The threshold is reached.**

**Decision: it is adequate and no fourth class is added.** It now covers deletion, relocation, insertion,
negative control, duplication and negation — the last being the class reviewer O demonstrated was missing.
**If a future reviewer demonstrates a live blind spot, that is iteration 4 and triggers the venue
question, not another extension.** Recording the freeze now is the point: without it, "just one more
mutant class" is exactly how a harness becomes the artifact that keeps failing review.

### F3 — the floor arm gets its third attempt, and the owner has already specified the design

Prior attempts: gate-4 pass 1 (could not vary position), gate-4 pass 2 (varied but could not isolate from
adjacency), then cut. **That is 2 rebuilds — so the cut happened one iteration inside the allowance.**

The third attempt is **not** a HOLED/INTACT-TWIN discrimination arm. Owner record **1449** item 1 dictates
the design for this specific test:

> *"if the experiment is to test where the granularity floor should sit, than the experiment should
> actually try moving the floor."*

So: hand two separately-spawned reviewers **the same plan** and **different floors**, and check the finding
sets differ in the predicted direction — the coarser floor should produce *fewer* "you didn't say how"
findings, not more. **This varies the independent variable**, which neither cut arm did. It needs no twin,
no pass rate, and no fixture library.

### G1 — the floor's POSITION moves to the assembled run

The coordinator supplies the count as fact: **three rebuilds** — pass 1 could not vary position; pass 2
varied it but could not isolate it from adjacency changes; then it was cut. **At threshold, so the venue
question is live, and the answer is to change venue.**

Reason, and it is a structural one three independent reviewers reached: moving a block in a prompt changes
**2–3 adjacencies at once**, so no isolation mechanism can attribute an effect to position rather than to
the new neighbours. That is not a defect in the apparatus to be repaired on a fourth attempt; **it is a
property of the thing being measured.**

**Recorded as VENUE CHANGED, not cut.** The distinction is load-bearing: "cut" previously meant *nobody
will ever check this*, which is what made the unratified harness cut so costly. The assembled run
exercises the composed prompt in situ, and a position defect that matters will show up as a bad plan.

---

## What this changes about the run's own claims

- **"Part B — Behavioural criteria: NONE. STILL CUT."** in `1.5-criteria-v2.md` is **superseded.** Under
  this ruling four items (F1–F4) are isolation-testable with **zero** prior mechanism iterations, and
  isolation is the default. **They are owed, not optional.**
- **The blanket cut is overturned; the individual venue decisions above replace it.** Only **G1** is
  genuinely leaving isolation, and it leaves on a stated structural reason at a counted threshold.
- **F1 and F2 were RUN** on 2026-07-29, after this document was written — three cold agents, composed
  prompts verified byte-identical to the live artifact, results and verbatim records in `8-harness.md` and
  `records/reviewer-SMOKE-*`. **F1 3/3 clean; F2 3/3 correct shape.** Mechanism iteration count for both:
  **1** — it worked first time, which is itself evidence for the owner's point that the trivial things are
  simplicity itself to test by plugging them in.
- **It immediately paid for itself**: it produced **three findings no cold reviewer had found**, one of
  which (§5's verbatim-prompt requirement being impractical, and both compliant agents routing around it)
  **invalidates good work under the set's own rules** and would never have surfaced from reading.
- **F3 and F4 have NOT been run.** F3 is the floor arm; it has 2 prior rebuilds, one allowance remaining,
  and its design is dictated by owner record 1449 item 1.
