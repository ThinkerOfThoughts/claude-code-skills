# Split review — round 1, reviewer B

**Reviewing:** the proposed division at
`Architect/runs/data-distiller/0/split-round-1.md` (verdict DIVISIBLE; sub-task A "the frame",
sub-task B "the dispatched-agent prompts under `stages/`").

**Inputs I actually had:** the task, the granularity floor, and the division. **No plan** — none
exists, and I did not judge the cut against one.

**Bounds I worked under, stated up front:**
- `/home/zero/Desktop/claude-code-skills/Data-Distiller/` is off limits and I did not read, list
  or grep it. I did run `ls` on the repo root `/home/zero/Desktop/claude-code-skills/`, which
  printed the directory's *name* alongside its siblings; I did not descend into it.
- I did not read any sibling reviewer's output in this runs directory.
- **Unchecked:** whether either half, as scoped, actually yields a plan that installs and runs —
  the division explicitly puts execution/testing out of scope for both halves
  (`split-round-1.md:148`), and no plan exists to check.

---

## Answers to the four questions

| Question | Verdict |
|---|---|
| **1. Coverage** | **Gaps.** Three load-bearing portions have no owner: the dispatch/control-flow spec (F3), the run's terminal human-facing deliverable (F4), and the per-item-strategy name set (F9). |
| **2. The seam** | **Stated, but internally contradictory and partly mischaracterized.** The `CONTRACT-DELTA` channel is declared and simultaneously denied (F1, blocker). The stated joint criterion is false for two of A's five artifacts (F10). |
| **3. The floor** | **PASS.** A is ~5 deliverables, B is ~6; the floor is "one file with its content specified". Neither half is at or below it. No finding. |
| **4. Real joint or arbitrary cut** | **Partly real.** "Read once for orientation" vs. "read verbatim mid-run by a context-less agent" is a genuine difference in reader, failure mode and authoring rule. But the cut commits the exact defect it uses to reject the alternative (F5), and a stronger joint the source material itself declares was never considered (F6). |

---

## Findings

### F1 — blocker — the seam declares an escape channel and denies it in the same paragraph
*(lenses: logical, completeness)*

`split-round-1.md:108-111` instructs B: where it cannot avoid a new artifact name, config key,
record field or `stages/` file, "the plan step that needs it carries an explicit
`CONTRACT-DELTA:` line naming the addition."

`split-round-1.md:137-138` states: "**What B produces that A consumes:** nothing at build time.
B's only upward channel is a `CONTRACT-DELTA:` line on any step that cannot be written within A's
contract."

A `CONTRACT-DELTA` is, by construction, a thing A must consume — it is a proposed amendment to A's
contract. The seam says A consumes nothing. It also names **no resolver, no ordering, and no
acceptance rule**: A "fixes [the vocabulary] before the other half writes a line"
(`split-round-1.md:71-72`), so by the time a delta exists A is finished and no party is assigned
to absorb it.

**Concrete failure:** B's plan emits a step reading `CONTRACT-DELTA: add field
strategy_reason to the item record`. A's plan does not contain that field. Both halves are
individually complete and internally consistent; assembled, they specify a role prompt that writes
a field the run-state layout has no slot for. Nothing downstream detects this, because no reviewer
after this point sees both halves' contracts side by side with a rule about which wins. A
practitioner executing B's step cannot execute it as written — it names an addition to a document
that is closed.

**Why blocker and not major:** the seam is the one artifact this review gates on, and everything
below the cut inherits it. A contradictory seam is worse than an unstated one, because it reads as
handled.

**Remedy sketch (one line, not a re-plan):** name the delta's consumer and the ordering — e.g. "a
`CONTRACT-DELTA` is a halt: B stops, the delta is applied to A's contract, and B resumes" — or
delete the channel and instead over-specify A's contract with a named extension point.

---

### F2 — major — the source-material partition mirrors the file partition, but the source does not partition
*(lens: factual)*

A is checked against `Guarded_change/{SKILL,METHODOLOGY,README}.md`,
`Dragonfly/{SKILL,METHODOLOGY,README}.md` and the sibling config files, and explicitly **not**
against `stages/` (`split-round-1.md:80-83`). B is checked against `Guarded_change/stages/` and
`Dragonfly/stages/` only (`split-round-1.md:116-118`).

That partition is contradicted by the source material in both directions:

- **A owns "the field schema of a finding record (including the source-citation field and the
  agreement count)"** (`split-round-1.md:73-75`). In the house shape the finding-record contract
  lives *below* the cut, in the charter: `/home/zero/Desktop/claude-code-skills/Guarded_change/stages/charter.md:36-37`
  — "**Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario."
  / "**Rank every finding** by severity". A is assigned the one schema whose only sibling
  precedent sits in files A is forbidden to be checked against.
- **Symmetrically**, B writes role prompts that must apply cross-cutting rules whose canonical
  statement is above the cut. `Guarded_change/METHODOLOGY.md:143` says of the path-validation rule
  that "The full operative rule (and its gate-4 block) lives **written-in-full** in
  `stages/stage-3.md`, `stages/stage-4.md`, and `stages/stage-6.md`" — i.e. the stage files are
  *derived from* the METHODOLOGY statement. See also `Guarded_change/METHODOLOGY.md:138` and
  `Dragonfly/METHODOLOGY.md:68`.

**Concrete failure:** A invents a finding-record schema with no `severity`-equivalent rank and no
"flag the unverifiable" field, because the only precedent for both is in `charter.md:36-39`, which
A never opens. B, holding the schema as fixed contract, writes a verify prompt that cannot record
"could not check" — and the task's "drops the unverifiable" becomes undetectable in the artifact.

---

### F3 — major — nothing owns the dispatch topology: order, fan-out, and who dispatches whom
*(lenses: completeness, logical)*

The seam's contract is five items (`split-round-1.md:129-135`): the `stages/` file list with
one-line purposes; on-disk names and run-state layout; the status-record schema; the finding-record
schema; the config key set. **All five are nouns.** None of them is the control flow.

A is bounded to "the vocabulary the whole skill uses" (`split-round-1.md:71`) and told it "does
NOT write the procedure body of any dispatched-agent role… and restates no procedure"
(`split-round-1.md:77-78`). B writes six role files that are "additions only"
(`split-round-1.md:105`) and may introduce nothing new. So the question *"decompose runs once and
emits a list; then for each item, N analysts run, then one verify, then one merge; the node
dispatches which of these, in what order, at what fan-out, passing what?"* is assigned to neither.

The house shape puts exactly this above the cut and treats it as canonical:
`Guarded_change/SKILL.md:27-45` creates the run folder, then carries the numbered loop table, with
line 28-29 stating "**Step numbers below are the canonical stage numbers used everywhere** (loop,
severity table, `decisions.md`)". `Dragonfly/SKILL.md` does the same.

**Concrete failure:** B authors an analyst prompt that assumes it is handed one item and writes one
findings file, and a node prompt that assumes it hands out whole *batches* of items and reads one
status per batch. Both are internally coherent; neither half's reviewer can see the mismatch,
because the mismatch is in an object no half owns.

Note this is *not* fixed by A's METHODOLOGY bullet "the method in prose" (`split-round-1.md:59`):
prose that describes the method is not a contract B is bound to, and A is separately forbidden to
restate procedure.

---

### F4 — major — the run's terminal deliverable is unowned, and the blind-roll-up rule makes it non-obvious
*(lenses: completeness, coverage)*

The task's purpose is "extracting trustworthy, source-cited factual findings". A run must therefore
end by handing a human ranked, cited findings. Both siblings name that artifact explicitly:
`Dragonfly/METHODOLOGY.md:149` (`diagnosis.md` — "root cause, causal chain, evidence, repro,
recommended fix, named residuals") and `Guarded_change/METHODOLOGY.md:154-168` (`8-harness.md`
— "conformance + regression results, verdict").

Under this division, no half is told to own it:

- B's six-file list (`split-round-1.md:93-103`) has no terminal/report role. Its last role is
  "Node / blind roll-up", whose defining property is that it "never reads the findings themselves,
  only the terse per-child status".
- A owns "**what a run produces** (the on-disk artifact layout)" (`split-round-1.md:60`) — a
  layout names files; it does not say which agent writes the terminal one or what goes in it, and
  A writes no procedure.

**Concrete failure:** the blindness constraint means the root coordinator is structurally
disqualified from assembling the deliverable. If neither half assigns a reader-permitted assembler,
the assembled plan produces a run whose top-level output is a status record ("3 children complete,
0 failed") and whose findings are scattered across per-item directories with nothing that
composes them. That is a run that completes and delivers nothing.

Related unresolved sub-question that falls in the same hole: does "merge" run **per item** (across
the N analysts of one item) or **across items**, or both? Agreement-ranking is defined over "how
many independent analysts agreed" (`split-round-1.md:16`), which is an intra-item quantity; nothing
says what ranking means once items are rolled up.

---

### F5 — major — "A restates no procedure" contradicts the house shape A is told to match, and re-commits the defect used to reject the alternative cut
*(lenses: factual, logical)*

A's SKILL.md and METHODOLOGY.md are said to "Match the sibling shape"
(`split-round-1.md:56`, `:60-61`), while A is constrained to restate no procedure
(`split-round-1.md:78`) and "must not restate a procedure, only point at it"
(`split-round-1.md:142`).

The siblings do the opposite, deliberately:

- `Guarded_change/SKILL.md:47-52` restates operative rules in the router: "The **most important
  gate is stage 3**…" and "The **iteration cap** (all gates): after 2 bounces at the same gate on
  the same finding class, stop and a human breaks the tie (see the gate files)."
- `Guarded_change/METHODOLOGY.md:143` states a rule *and* says it "lives written-in-full in
  `stages/stage-3.md`, `stages/stage-4.md`, and `stages/stage-6.md`" — the same rule, on purpose,
  in both layers, with the operative copy named.

So the house shape's cross-cutting rules are **deliberately stated on both sides of this cut**. The
division at `split-round-1.md:157-163` rejects the alternative cut precisely because it "splits
**single rules across both halves**" and "neither half can state the rule completely." The proposed
cut has the same property for every rule of the class above: stop-for-human conditions (A's
SKILL.md per `split-round-1.md:55`, operative copy in B's stage files), read-only discipline, and
cite-or-it-doesn't-count all sit in both.

The rejection rationale is therefore not discriminating between the two candidate cuts. Either the
"no restatement" rule must go (and the seam must then say who owns the canonical copy and who owns
the operative copy of each shared rule), or the rationale for preferring this joint must be
restated on some other ground.

---

### F6 — major — the source material declares its own seam and it was not considered
*(lens: missed opportunity)*

Only one alternative was weighed (`split-round-1.md:151-163`): cutting at the blind-roll-up
barrier. The obvious third option is the seam **both siblings name in a section of their own**:

- `Guarded_change/METHODOLOGY.md:88-100` — "## The two layers": Layer 1 = "agnostic core (this doc
  + the skill + the stage files)… Ships once; knows nothing about any specific project"; Layer 2 =
  "per-project config… the **only** place project specifics live."
- `Dragonfly/METHODOLOGY.md:95-102` — the same section, same split.

A cut on that line gives: **half 1** = the corpus-agnostic method (SKILL.md, METHODOLOGY.md, all of
`stages/`); **half 2** = the Layer-2 surface (the config contract and its worked example, the
on-disk run-state/artifact layout, restart-resume semantics, README, install).

It is strictly better on the two axes where the proposed cut is weakest, and the task's own
property list names this seam too ("the method itself stays corpus-agnostic"):
- vocabulary and procedure stay in one author's hands, so F2, F3 and F-A do not arise;
- no cross-cutting *method* rule is split, because the whole method is in half 1;
- the seam is a single, already-documented object — the config key set plus the artifact paths —
  rather than five schemas.
- **Floor check on the alternative:** half 2 is config contract + worked config + run-state layout
  + README + install ≈ 4–5 deliverables, comfortably above "one file with its content specified".
  It does not fall below the floor.

Its cost is real and should be stated rather than assumed fatal: half 1 is larger and may itself
want re-division. That is a tree-depth question the floor permits.

---

### F-A — major — A is assigned the method's central design decision while forbidden the information that would settle it
*(lens: unstated assumptions & risks)*

The unstated assumption is that **which roles exist** is *vocabulary* — derivable ahead of, and
independently of, any procedure. `split-round-1.md:71-75` gives A "canonical role/stage names and
their exact file paths under `stages/`" and `:130` makes "the exhaustive list of `stages/` file
paths" contract item 1.

Which roles exist is the decomposition of the method, and it is discovered while writing the
procedures — which is B's work, from which A is excluded (`split-round-1.md:77-78`). In practice A
can only transcribe the task's bullet list into six filenames.

**Concrete failure:** B, writing the decompose prompt, finds that *sizing* an item and *choosing a
strategy for an over-sized item* are different acts with different inputs (one is mechanical, one
needs the config's "what an analyzable item is"), and want separate files; or finds that per-item
merge and cross-item merge cannot share a prompt (see F4). Either discovery requires a new
`stages/` file — which B may not introduce, and whose only channel is the one F1 shows is dead.

Evidence that six roles is likely to be wrong: the siblings, whose methods are no more complex,
carry 11 and 12 files under `stages/` respectively (`Guarded_change/stages/`, `Dragonfly/stages/`).

---

### F-F — major — "blind roll-up" is pinned to an instruction, not to a barrier
*(lens: fidelity)*

The task's mechanism is: "a coordinating agent **never reads the findings themselves**, only a
terse per-child status, **so its expectations cannot steer them**." The steering-prevention is the
point; the not-reading is how it is achieved.

The division pins this term to two things and nothing else:
1. in A, "the **field schema of the terse per-child status record**… (the only channel across the
   blind-roll-up barrier)" (`split-round-1.md:73`, `:132`) — a schema; and
2. in B, a sentence in the node prompt: "never reads the findings themselves, only the terse
   per-child status" (`split-round-1.md:102-103`) — an instruction to an agent.

A schema plus an instruction is a **proxy** for a barrier. What no half owns is the mechanism that
makes the barrier hold: that a child's findings and a child's status live at paths such that the
node's read set is *structurally* restricted (separate directories, or the status written to a path
the node is given while the findings path is one it is never handed), and what happens when a child
fails and the node needs to know *why* without reading the failure detail. A owns the on-disk layout
and could carry this, but its ownership list stops at the record's field schema.

**Other loaded terms I pinned, with no finding:** "cold agent" → B's common core, "shares no
context with siblings" (`split-round-1.md:94`), which is the same mechanism the sibling charters
use; "read-only over the corpus" → B's common core, adequate; "N independent analysts" →
independence is the no-shared-context rule, and N is a config key A owns (`:63-64`), consistent;
"restart/resume" → A owns "what a completed vs. in-progress unit looks like on disk" and B's node
owns the resume procedure (`:67`, `:103`) — a clean schema/procedure split, no finding; "verify" →
B's verify role, "re-checks every citation and drops the unverifiable" (`:100`), which is the task's
mechanism, not a proxy.

---

### F9 — minor — the per-item strategy name set has no owner
*(lens: completeness)*

Task bullet 1 requires the method to "pick a per-item strategy when an item does not fit". A
strategy that is *picked* and *recorded in run state* needs a fixed name set. A's ownership list
(`split-round-1.md:71-75`) enumerates role names, on-disk names, two record schemas, the config key
set and concurrency semantics — no strategy vocabulary. B may not introduce names
(`split-round-1.md:108-110`).

**Concrete failure:** B's decompose prompt must instruct "record the chosen strategy" and cannot say
what the choices are; the node's resume logic (which must know whether an item's strategy was
already settled) has nothing to read. Fixable in place by adding one line to A's ownership list;
recorded as minor for that reason, but note it is an *instance* of the dead channel in F1.

### F10 — minor — the stated joint criterion is false for two of A's five artifacts
*(lens: factual)*

`split-round-1.md:122-124`: "Above the cut, files are read **once, by the invoking agent**, to
orient and route."

- The **README** is human-facing (`split-round-1.md:68` says so itself) and is read by no agent.
- The **Layer-2 config** is consumed at run time by dispatched cold agents, not once by the
  invoking one: in the house shape, `redteam_context` entries are handed to the cold reviewer and
  `Guarded_change/METHODOLOGY.md:136-138` records that "The operative reviewer-spawn form of this
  rule lives in `stages/stage-3.md` / `stages/stage-6.md`."

The joint is still real on the documentation-vs-prompt axis (different failure mode, different
authoring rule — those parts of `:125-127` hold). The over-claimed criterion matters only because
it is the sole justification offered for preferring this cut, and F5 shows the other justification
does not discriminate.

### F11 — minor — the config artifact is described two incompatible ways within A
*(lens: factual)*

A owns "a **worked per-corpus config template/example** file (the Layer-2 artifact)"
(`split-round-1.md:62`), while "what neither owns" excludes "Authoring a per-corpus config
**instance** for any specific real corpus (A owns only the template/example)"
(`split-round-1.md:146-147`). A *worked example* is an instance of some corpus; a *template* is not.
The two sentences do not describe the same deliverable.

The house shape settles this and A's description matches neither arrangement: the **template** is a
section inside METHODOLOGY (`Guarded_change/METHODOLOGY.md:103-152`;
`Dragonfly/METHODOLOGY.md:106-131`, both an inline annotated YAML skeleton), and the **worked
instance** is a separate top-level file in the skill directory
(`/home/zero/Desktop/claude-code-skills/Guarded_change/guarded-change.companion.md`,
`/home/zero/Desktop/claude-code-skills/Dragonfly/dragonfly.companion.md`). A's split creates a third
arrangement in which the key set exists both in METHODOLOGY's config-contract section
(`split-round-1.md:60`) and in a separate template file (`:62`) — two copies inside one half, with
no statement of which is canonical.

### F12 — minor — A's METHODOLOGY/SKILL section lists omit sections both siblings carry, while claiming to match their shape
*(lens: completeness)*

`split-round-1.md:60-61` claims A's METHODOLOGY "Matches the section shape of
`Guarded_change/METHODOLOGY.md` and `Dragonfly/METHODOLOGY.md`". Six sections are enumerated; both
siblings carry a seventh that is not:

- **"Human-in-the-loop"** — `Guarded_change/METHODOLOGY.md:198`, `Dragonfly/METHODOLOGY.md:172`.
  For Data-Distiller this is where "what a run stops for" would live (a corpus item that cannot be
  sized, a config key absent, an analyst that returns nothing verifiable).
- Dragonfly additionally carries **"Trigger"** (`Dragonfly/METHODOLOGY.md:161`), which states the
  proactive-suggestion precision bar — relevant, since A owns the frontmatter `description`.
- A's SKILL.md list (`split-round-1.md:52-56`) has no entry-precondition section, where
  `Dragonfly/SKILL.md:22` carries "Before you start: cold-start guard". A corpus-distillation run
  invoked inside an already-loaded session has the same failure.

---

## Lens verdicts

**1. Factual — ISSUES (F2, F5, F10, F11, F12).** Sources consulted, with what I checked in each:
`Guarded_change/SKILL.md` (full — router shape, loop table, canonical stage numbering at :27-45,
restated operative rules at :47-52); `Guarded_change/METHODOLOGY.md` (headings; :88-100 two layers;
:103-152 config contract; :138/:143 the "written-in-full in the stage files" rule; :154-190 what a
run produces; :198 human-in-the-loop); `Dragonfly/SKILL.md` (:1-40 — frontmatter, inputs, cold-start
guard at :22, loop); `Dragonfly/METHODOLOGY.md` (headings; :68; :95-131; :141-160; :161 trigger;
:172); `Guarded_change/stages/charter.md` (:30-40 — finding-record discipline);
`Guarded_change/guarded-change.companion.md` and `Dragonfly/dragonfly.companion.md` (heads — the
config *instance* form); directory listings of both skills and both `stages/` directories (file
counts: 11 and 12).

**2. Logical — ISSUES (F1, F3, F5).** The seam contradicts itself; the contract is all nouns and no
control flow; the rationale for preferring this joint does not discriminate against the alternative
it rejects.

**3. Missed opportunity — ISSUE (F6).** The two-layer seam the source material declares in a section
of its own was not among the alternatives weighed.

**4. Unstated assumptions & risks — ISSUE (F-A).** The load-bearing unstated assumption is that the
`stages/` role set is derivable as vocabulary before any procedure is written. Secondary, not filed
separately: the cut is strictly serial (A "fixes it before the other half writes a line",
`:71-72`), so it buys no parallelism and propagates every A error wholesale into B — acceptable if
intended, but it is not stated as a cost anywhere.

**5. Fidelity — ISSUE (F-F).** Terms pinned: *blind roll-up* → status-record schema (A) + a prompt
sentence (B), which is a proxy, not a barrier — filed. *Cold agent* → no-shared-context rule in B's
common core. *Read-only* → B's common core. *N independent analysts* → independence via
no-shared-context; N a config key in A. *Decompose* → B's decompose-and-size role. *Verify* → B's
verify role, re-check every citation, drop the unverifiable — the task's own mechanism. *Merge* →
B's merge role (but see F4 on which level it operates at). *Restart/resume* → A's on-disk
completed-vs-in-progress markers + B's node procedure. *Config* → A's key set + B's consumers.

**6. Completeness — ISSUES (F3, F4, F9, F12).** Structural checklist run against the required parts
of a division (both halves' scope, what each excludes, the seam's producer/consumer directions,
what neither owns, the floor check, the alternative considered) — all present. **Generative sweep
run**, looking for: the run's terminal output and its author (→ F4); the control flow / dispatch
order and fan-out (→ F3); the failure/error path when a child fails and the parent is blind (→
inside F-F); the human-stop conditions and where they live (→ F12 and F5); the concurrency
ceiling's enforcement point (assigned — A's semantics, B's node, no finding); resume markers
(assigned, no finding); the strategy name set (→ F9); the install/verification step (assigned to A
at `:68-69`, no finding); and who decides N (assigned — A's config key, no finding).

**Was any portion of the task left unaddressed?** Yes, per F3, F4 and F9. Every other bullet of the
task's property list maps onto a named half.

---

## Summary of severities

| # | Severity | Finding |
|---|---|---|
| F1 | **blocker** | `CONTRACT-DELTA` channel is declared and denied in the same seam; no consumer, no ordering, no resolver |
| F2 | major | Source-material partition mirrors the file partition; A owns the finding-record schema but is not checked against `stages/charter.md`, where its only precedent lives |
| F3 | major | Dispatch topology (order, fan-out, who dispatches whom) is in neither half's ownership; the contract is five nouns |
| F4 | major | The run's terminal human-facing deliverable has no owner, and the blindness rule disqualifies the root coordinator from producing it |
| F5 | major | "A restates no procedure" contradicts the sibling shape A is told to match, and re-commits the split-rules defect used to reject the alternative cut |
| F6 | major | The two-layer seam both siblings declare in their own section was never considered as an alternative |
| F-A | major | A owns the `stages/` role decomposition — the method's central design decision — while excluded from the procedure-writing that settles it |
| F-F | major | "Blind roll-up" pinned to a schema plus an instruction; nothing owns making the barrier structural |
| F9 | minor | Per-item strategy name set unowned |
| F10 | minor | The stated joint criterion ("read once by the invoking agent") is false for the README and the config |
| F11 | minor | Config template vs. worked instance described two incompatible ways inside A; neither matches the house arrangement |
| F12 | minor | A's METHODOLOGY section list omits "Human-in-the-loop" (both siblings) and SKILL.md omits an entry-precondition section (Dragonfly) |

**On divisibility itself:** I do **not** find this task indivisible. The floor is cleared by both
halves, and F6 describes a division of the same task that survives the objections above. My
position is that *this particular cut* needs repair or replacement, not that no cut exists.
