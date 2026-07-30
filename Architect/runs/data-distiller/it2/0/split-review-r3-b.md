# Split review — round 3, reviewer B

Reviewing the **proposed division** in
`Architect/runs/data-distiller/it2/0/split-round-3.md`. No plan exists and I did not look for one.
`/home/zero/Desktop/claude-code-skills/Data-Distiller/` was not read, listed or grepped;
`~/.claude/skills/` was listed only at its top level and at
`~/.claude/skills/{guarded-change,dragonfly}/` — I did not enter `~/.claude/skills/data-distiller/`.

**Overall:** the cut is a defensible one and I am not filing "indivisible". The path-partition
default (S1) is the strongest thing in the document — it makes the partition total by construction,
which is rare and worth keeping. Three `major` findings stand, all against the **seam**, not against
where the line was drawn. Two of them (SR1, SR2) land on the run's single operational handover and
on the task's defining blindness property.

---

## Findings

### SR1 — `major` — the one point where the halves touch operationally has no stated contract, and the joint the cut is justified by is overclaimed there

**Where.** Sub-task B, `SKILL.md` bullet: the router must *"enter the method at the file A's
Declarations name as the entry stage, **handing over to A's files rather than restating their
mechanics**"*. S3(a): *"One row is marked as the **entry file** the router hands over to."*
Sub-task A's opening: A's files are *"the prompts a **dispatched agent** reads verbatim and acts
on."* "Why this is a real joint", bullet 1: *"A's files are consumed **verbatim by a dispatched
agent**… B's `SKILL.md` is consumed **by the invoking session**."*

**The gap.** "Hands over" is never pinned. Two readings, and the division picks neither:

- *The invoking session reads A's entry file.* Then A's brief is wrong for that file. A has been
  told to write for a dispatched agent, so the entry file will open in the second person addressed
  to a cold, independent, read-only agent (the properties A is told to put in "the core that every
  dispatched agent reads first" — coldness, independence, read-only over the corpus, cite every
  finding). None of those hold of the invoking session, which carries the user's context, must
  write the run folder, and must spawn. And the cut's headline differentiator ("who executes the
  file") is then false of at least one A file.
- *The router dispatches an agent to read the entry file.* Then S8's premise — *"the invoking
  session executes `SKILL.md` and is itself the topmost coordinating agent"* — is wrong, the
  topmost coordinating agent is a child, and B's ownership of "locate or create the run folder"
  sits above a boundary A's re-entry rules (S5) are written beneath.

**The concrete missing artifact.** Whichever reading is chosen, **nothing declares what the router
must pass in.** S7 says A's files *"name keys and receive their values in the dispatch prompt"* —
but the entry file's dispatch prompt is composed by B, and none of S3's five tables states its
required contents (config values, run-folder path, corpus root, run slug). B is told to hand over
and never told what to hand over; A is told it will receive values and never told by whom or in
what shape.

**Failure scenario.** A's Declarations name `stages/decompose.md` as the entry file. B writes
`SKILL.md`: "locate the config, create `runs/<slug>/`, then hand over to `stages/decompose.md`."
`stages/decompose.md` opens with "You are a cold agent. You are read-only over the corpus." The
invoking session — which has just written a directory and holds the user's framing — reads it and
either violates it or ignores it. Nobody detects this: A never sees B's router (S2), B never opens
A's files (S2), and S10's composition check only compares rules *stated in more than one place*,
which this one is not.

**Remedy, at the floor.** One clause in the seam: state which agent reads the entry file, and add
a sixth Declaration — the entry file's **dispatch contract** (the named values the router must
supply). If the answer is "the invoking session reads it", A's brief must say so for that one file.

---

### SR2 — `major` — S3(c) is not required to distinguish a status artifact from a findings artifact, yet S4 and S8 rest entirely on that distinction

**Where.** S4: *"B never writes a step that reads a run artifact other than one S3(c) marks as
status."* S3(c) itself requires only: *"path (relative to the skeleton in S6), name, and one line
on contents."* It never requires a status/findings classification.

**Why it is load-bearing.** The blind roll-up is the task's defining property ("a coordinating
agent never reads the findings themselves, only a terse per-child status"). The division
deliberately does **not** give B the rule's text — S8: *"`METHODOLOGY.md` says the property exists
and why; it does not restate the rule in B's words"* — and S2 forbids B from opening A's files.
So B's entire ability to obey the invariant reduces to: *look up the artifact in S3(c) and check
whether it is a status artifact.* That lookup is against a field S3(c) does not require A to
provide.

**Failure scenario.** A's inventory contains
`items/<id>/merged.md — the item's ranked findings` and
`items/<id>/state.md — what this item has completed and what it returned`.
B, writing the run-level entry point and the resume account, needs to know whether a node has
finished an item. `state.md` sounds like status; it is also where A recorded the agreement counts.
B writes a router step that reads it. The invoking session — the topmost coordinating agent by
S8's own account — is now reading findings on every resume, and the invariant the skill exists to
enforce is broken at the top of the tree, by a file B was permitted to open.

**Remedy, at the floor.** Add one required column to S3(c): each artifact is marked `status` or
`findings`, and S4's prohibition binds on that column. Alternatively make S3(c) list the
status artifacts as a closed set and make everything else off-limits to B by default.

---

### SR3 — `major` — the stop-for-human conditions are assigned to B, but the information that determines them is A's and no Declaration carries it

**Where.** Sub-task B, `SKILL.md` bullet: B owns *"the stop-for-human conditions"*. Sub-task A:
*"**Failure and retry semantics** — an analyst returning nothing, verification dropping every
citation for an item, an unanalyzable item — expressed as permitted status values plus a
retry/abandon rule in the relevant file."* S3(d) carries *"permitted status values, the run-level
outcome states they aggregate into, and — per unit of work — the on-disk marker"*. S4: *"B may not
paraphrase a mechanic it does not own."*

**The gap.** A halt condition is not a status value. The conditions that should stop a run for a
human — verification dropped every citation for an item, an item cannot be reduced below the
context budget by any strategy, all N analysts failed on the same item, the abandon rule fired —
are *method* facts that live in A's files, and S3(d) carries only the vocabulary they are reported
in, not the thresholds at which a human is needed. B is left with three options and the division
sanctions none: invent them (violates S4 and S3(e)'s "B does not decide them"), omit the section,
or write only the router's own halts (config missing, run folder collision) and silently drop every
method-level one.

**This is a named, load-bearing section in both siblings**, not a hypothetical:
`Guarded_change/SKILL.md:54–73` ("Stop-for-human") and `Dragonfly/SKILL.md:72–81` ("Stop-for-human")
are top-level sections of the router, and in both, the operative conditions are stated to live in
the stage files (`Guarded_change/SKILL.md:63–64`: *"Full text in `stages/stage-1.5.md`,
`stages/stage-4.md`, `stages/stage-8.md`"*). The siblings solve this by having one author for both
sides. This cut has two, and did not carry the bridge.

**Remedy, at the floor.** Extend S3(d) — or add a row to S3(e) — with *"the conditions under which
the method halts and returns to a human"*, and have B's `SKILL.md` list them and point at A's file
for the operative text, exactly as `Guarded_change/SKILL.md:63–64` does.

---

### SR4 — `minor` — S2's "sole input" and S10's composition check contradict each other

S2: *"**That section is B's sole input from A** — B does not read the rest of A's plan, and does
not open A's planned files, to write its own."* S10: *"B checks that its consumed Declarations
still match **A's plan** and that every rule stated in more than one place agrees **across the
files**."*

S10 cannot be performed without reading A's plan and opening A's files. The "to write its own"
tail of S2 hints the prohibition is phase-scoped (write-phase only, lifted for the S10 check), but
"sole input from A" is unqualified and the division never states the scoping. As written, B is told
both to never open A's files and to cross-check them — and S10 is the clause the division leans on
precisely because *"this cut deliberately states some rules in more than one place."*

Remedy: one sentence making S2's prohibition explicitly phase-scoped, and S10 explicitly a
read-A's-files check performed after both plans exist.

---

### SR5 — `minor` — S10's insufficiency branch has no actor, and no obligation on A to amend

S10: *"If a Declaration changed after B consumed it, **or is insufficient to write a section B
owns**, B raises a mismatch report against the Declarations and B's dependent sections are
re-derived."* Then: *"The channel carries mismatches only — B does not propose method, and A does
not answer with a change to B's documents."*

"Are re-derived" names no actor, and nothing obliges A to amend an insufficient Declaration. Under
the insufficiency branch specifically, re-deriving B's sections from the *same* insufficient input
changes nothing. The change-after-consumption branch is fine; only insufficiency terminates
nowhere. Remedy: state that a mismatch report of the insufficiency kind obliges A to amend the
Declarations, and that only then does B re-derive.

---

### SR6 — `minor` — no fallback if `## Declarations` is absent or incomplete when B is planned; and the division never says what each half physically receives

S2 asserts *"A is planned first"*, which is a sequencing constraint on the caller, not something
the division can enforce. If the two halves are planned concurrently — the ordinary reason to
split — B has no input at all and must invent the config keys, the artifact inventory, the status
vocabulary and the entry-file name, all of which S3 forbids it to invent. Nothing states what B
does in that case (halt? plan against a stated placeholder set and reconcile via S10?).

Related and smaller: the division never states **what each half receives as its brief.** Sub-task
A's text cross-references `S3e`, `S6`, `S7` by label, which are unresolvable without the seam
section — strong evidence the whole document is meant to travel with each half, but it is inferred,
not stated. If only the "Sub-task A" section were handed down, A would never learn it must emit
`## Declarations` at all, since that requirement appears only in S3.

Remedy: one sentence each — "both halves receive this entire document", and B's behaviour when
Declarations are missing.

---

### SR7 — `minor` — the `## Declarations` obligation is not carried into a further division of A, which the document itself anticipates

"On the imbalance itself": *"if A is divided again the audience line still holds beneath it."* The
audience line does hold — but the seam's **sole carrier** does not. S3 places the five tables on
"sub-task A"; if A is divided into A1/A2, either both emit partial Declarations with no stated rule
for their union, or neither does and B's only input vanishes. Since the division explicitly expects
A to be re-divided and explicitly makes Declarations B's sole input, the survival rule should be
stated. Remedy: one clause — the `## Declarations` obligation survives any further division of A;
each descendant contributes rows and their union is the section B consumes.

---

### SR8 — `minor` (factual) — S6's rooting rationale misreads the siblings

S6: *"The siblings root theirs at the skill's own directory (`Guarded_change/SKILL.md:27`,
`Dragonfly/SKILL.md:31`), which works because the skill sits in the project under change;
Data-Distiller is installed at `~/.claude/skills/<name>/` … so inheriting that would make every run
mutate the installed skill."*

The cited lines say no such thing. `Guarded_change/SKILL.md:27` reads *"Create a change folder
`changes/<slug>/`"* and `Dragonfly/SKILL.md:31` reads *"Create a hunt folder `hunts/<slug>/`"* —
bare relative paths, which resolve against the invoking session's working directory, not the
skill's directory. Confirmed empirically: `~/.claude/skills/guarded-change/` contains only
`METHODOLOGY.md`, `SKILL.md`, `stages/` and `~/.claude/skills/dragonfly/` only
`METHODOLOGY.md`, `SKILL.md`, `stages/` — **neither installed copy has a `changes/` or `hunts/`
directory.** The `changes/`/`hunts/` folders in the *source* trees exist because the source repo
was the working directory during dogfooding, not because the skill roots runs at itself.

**The decision S6 reaches is correct and matches the siblings' actual behaviour** — only the
justification is wrong, and the stated hazard ("inheriting that would make every run mutate the
installed skill") does not exist. Worth fixing because B is told to check itself against these
files and will find the claim unsupported. Severity minor: no part of the cut moves.

---

### SR9 — `minor` (factual) — `METHODOLOGY.md:79` miscited in S9

S9: *"(verified: neither sibling's `SKILL.md` contains a dispatch step; the operative
reviewer-spawn rule lives in the stage files, `Guarded_change/METHODOLOGY.md:79`)"*.
`Guarded_change/METHODOLOGY.md:79` is a stage-index table row: `| 7 — Gate |
`stages/stage-7.md` | route by severity |`. The supporting text is at **:137–138**: *"(The
operative reviewer-spawn form of this rule lives in `stages/stage-3.md` / `stages/stage-6.md`.)"*

**The underlying claim is true** — I checked it independently rather than through the citation.
Grep for `spawn|dispatch a|cold subagent|Task tool` across both `SKILL.md` files returns only
descriptive prose (`Guarded_change/SKILL.md:20,66,67,68,78`; `Dragonfly/SKILL.md:3,94`), no
imperative dispatch step; the same grep over the stage files returns hits in
`Guarded_change/stages/stage-3.md` (4), `stage-6.md` (4), `stage-4.md`,
`Dragonfly/stages/stage-1.md`, `stage-7.md`, `charter.md`. S9 stands; fix the line number.

---

### SR10 — `minor` — B is told the siblings' companion files "occupy this slot"; they do not occupy it in the way B will need

Sub-task B: *"a shipped template/example config file at the build's top level (the siblings'
`guarded-change.companion.md` / `dragonfly.companion.md` occupy this slot)"*, and *"`README.md` —
human-facing orientation (both siblings ship one)."*

Two corrections B should be handed rather than left to discover, in the same spirit as the
`charter.md` caveat A was given:

1. `Guarded_change/guarded-change.companion.md:1` and `Dragonfly/dragonfly.companion.md:1` are
   **real Layer-2 configs for a specific unrelated project** ("companion-emergence"), not templates
   or examples. Neither sibling ships a template, so B is authoring one without a worked example —
   the same situation A was explicitly warned about for the shared-core file.
2. **Neither the companion config nor `README.md` is present in the installed copy.** The installed
   skills contain only `SKILL.md`, `METHODOLOGY.md`, `stages/`. So B's install step must decide
   *which* of the build's files are installed, not merely how they are copied — and the config
   template, by the siblings' precedent, is not one of them. This interacts with the collision
   check B is told to write.

Note the collision hazard B was told about **is real**: `~/.claude/skills/` contains
`data-distiller/`, `dragonfly/`, `guarded-change/`. Verified by listing the top level only.

---

### SR11 — `minor` (missed opportunity) — S6 puts in the seam a decision that S3(c) already delivers, and one that is arguably B's

S6 fixes a minimum run-directory skeleton, justified as *"so S2's one-directional flow is not
spoiled by B owning a layout A must write into"* — then closes with *"Every addition appears in
S3(c), so B documents the layout A actually built."* If B documents the layout from S3(c) anyway,
B never owns it, and the one-directional flow was never at risk; the minimum shape is a constraint
on A that buys nothing. Meanwhile the part of S6 that *is* genuinely contested — the **rooting**
(`runs/` at the invoking session's cwd rather than inside the installed skill) — is a consequence
of the install location and is created by the router, both of which are B's. The available
alternative not considered: put rooting in B (with the router creating the run folder and passing
its absolute path down per SR1's dispatch contract), and let A own everything beneath it via
S3(c) alone. That is a cleaner seam with strictly fewer clauses.

---

## Lens verdicts

**1. Factual — findings: SR8, SR9, SR10 (all `minor`).**
Citations I checked against source, all confirmed unless noted:
`Guarded_change/METHODOLOGY.md:9–11` (the "not to run a stage" quote — confirmed verbatim);
`SKILL.md:25–32` (imperative router steps — confirmed: "Create a change folder", "append a line to
`decisions.md`", "Walk the loop");
`SKILL.md:81–83` (self-check criteria — confirmed verbatim);
`SKILL.md:49–50` (charter shared with per-stage additions — confirmed);
`SKILL.md:3`, `Dragonfly/SKILL.md:3` (frontmatter description is the trigger text — confirmed);
`SKILL.md:16–18` (config glob — confirmed);
`METHODOLOGY.md:73` (the index-grade calibration line — confirmed verbatim);
`METHODOLOGY.md:67–84`, `:88–101`, `:103–151`, `:154–196` (section boundaries — all confirmed);
`SKILL.md:1–4`, `:13–24`, `:54–73`, `:75–85` (section boundaries — all confirmed);
`Guarded_change/stages/charter.md:1` = "# The red-team charter (shared by stages 3 and 6)" and
`Dragonfly/stages/charter.md:1` = "# The red-team charter (shared by stages 1, 4, 7)" — **both
confirmed verbatim**, and the caveat built on them (charter.md is red-team material shared by a
subset of stages, not a universal core) is correct and is the strongest piece of source work in the
document.
Not confirmed: `SKILL.md:27` / `Dragonfly/SKILL.md:31` as evidence for run-rooting (SR8);
`METHODOLOGY.md:79` for the spawn-site claim (SR9, though the claim itself verified true by grep).

**2. Logical — findings: SR4, SR5.**
Sequencing otherwise holds: A→B one-directional, A first, S10 after both. The rejected alternative
is named with an operative reason (the blindness invariant would straddle the cut), which is sound
reasoning I could not fault.

**3. Missed opportunity — finding: SR11.**
The document does consider and reject one alternative cut, with a stated reason. I looked for a
third: a *corpus-facing vs. orchestration* cut collapses into the rejected one, and a *per-file*
cut falls below any useful coherence. No further finding.

**4. Unstated assumptions & risks — findings: SR6, SR7.**
Also examined and found adequately handled: that A's files can be made corpus-agnostic without
seeing the config (S7 handles it); that B can obey the blindness rule without reading its text
(handled in principle by S4 + S3(c), but see SR2 for the field that makes it work); that both
halves stay off `Data-Distiller/` (S11, explicit in both briefs).

**5. Fidelity — findings: SR1, SR2, SR3.**
Terms pinned to concrete mechanisms:
*seam* → a total path partition (S1) plus one named carrier section (S2/S3) — concrete;
*Declarations* → five labelled tables with stated columns — concrete, and calibrated against a real
sibling line (`METHODOLOGY.md:73`);
*blind roll-up* → S8 (formulated in A, obeyed by B, bound onto the invoking session) plus S4's
negative obligation — **the pin fails at SR2**: the mechanism resolves to "consult S3(c)'s marking",
and S3(c) has no such marking;
*coordinating agent* → deliberately left to A to pin (S3(e)) — legitimate, since it is a method
question and it is declared;
*dispatched agent* → **the pin fails at SR1**: A's audience is defined as "a dispatched agent" while
B's router "enters" A's entry file from the invoking session;
*resume* → split by kind (S5: consults-state → A, run-level entry → B) — concrete and clean, the
best-pinned term in the document;
*install* → copy to `~/.claude/skills/<name>/` with a collision refusal — concrete, and the
collision it names is real.

**6. Completeness — findings: SR1, SR3, SR6, SR7.**
The four required questions are all addressed: coverage (S1's default makes it total), the seam
(stated at length, S1–S11), the floor (a dedicated section, and both halves clear it — A has at
minimum seven files to specify, B has five plus an install step; neither is one file with content
already given), and real-joint-vs-bisection (four differentiators named, of which three survive
scrutiny — see SR1 for the fourth).

**Generative sweep — run.** I asked what load-bearing section those four questions do not
anticipate, and looked specifically for: the **handover/dispatch contract** between the halves
(missing — SR1); the **human-gate conditions** (owned by B, informed by A, no carrier — SR3); the
**abandon/halt story** (partly in A, no run-level expression — folded into SR3); **what each half
physically receives** (unstated — SR6); the seam's **survival under further division of A**
(unstated, though anticipated — SR7); **who assembles the two plans** into the single deliverable
the task asks for (out of the division's scope — a framework concern, not filed); **off-limits
enforcement** across both halves (present, S11); and the **run-slug / run-folder naming** authority
(implicitly B's via the entry point — adequate).

---

## Answers to the four questions, directly

1. **Coverage.** Sound. S1's path-default makes the partition total, including for a directory
   neither half anticipated. I found no orphaned file and no path both halves claim. The one
   coverage failure is not a *file* but a *responsibility*: the stop-for-human conditions (SR3).
2. **The seam.** Stated, extensively, and in the right direction — but three defects in its
   contents: no dispatch contract at the single handover point (SR1), no status/findings marking
   for the field the blindness invariant is enforced against (SR2), no carrier for halt conditions
   (SR3), plus SR4–SR7.
3. **The floor.** Both halves clear it comfortably. No finding.
4. **Real joint or arbitrary cut.** Real. Three of the four named differentiators hold under
   checking (failure mode, corpus-agnostic vs. corpus-naming, authorship discipline). The fourth —
   "who executes the file" — is the one the whole cut is headlined on and it is overclaimed at the
   entry file (SR1). The cut survives on the other three; the argument needs repair, not the line.
