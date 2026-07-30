# Split review — round 2, reviewer A

Reviewing the proposed division in
`Architect/runs/data-distiller/it2/0/split-round-2.md` against the task and the granularity floor
quoted at its head.

**Inputs I had:** the division document, the granularity floor, and the two source-material
directories (`Guarded_change/`, `Dragonfly/`). No plan — none was expected. I did not read, list
or grep `/home/zero/Desktop/claude-code-skills/Data-Distiller/`, and I read no other file under
`Architect/runs/`. Nothing was missing from my inputs.

**Overall:** the cut is a **real joint**, not a bisection, and **neither half falls below the
floor**. I raise **no blocker**. I raise **three `major` findings, all at the seam** — none of
them requires re-cutting; each is repaired by adding or correcting seam text. I raise three
`minor`s.

---

## Findings

### M1 — `major` — Resume across the tree is owned by neither half

**Lens:** completeness / coverage. **Question:** 1 (coverage) and 2 (the seam).

The task lists **"Restart and resume from on-disk state"** as a defining property
(`split-round-2.md:26`). The division splits it into two pieces and leaves the middle unassigned:

- **B** gets "the **top-level resume instruction** (on invocation, if a run folder exists, read
  the run log and continue from the first incomplete unit)" (`split-round-2.md:120–122`).
- **A** gets only the markers: S5 says A "publishes, per stage, the on-disk marker that means
  'this unit is finished and need not be re-run'", and then explicitly — "B does not invent
  completion conditions; **A does not write the resume paragraph**" (`split-round-2.md:175–178`).
- A's in-scope list (`split-round-2.md:67–97`) never mentions resume, re-entry or idempotence.

But the method is a **tree**, not a single sequence. The instruction that a *re-entered
coordinating node* must skip children that already carry a completion marker, and the rule for a
*partially complete item* (say 3 of 5 analysts returned), is an instruction a dispatched agent
executes — which by the division's own reasoning is A's territory: S8 grounds B's exclusion on
exactly this, "B writes no prompt any agent executes" (`split-round-2.md:201–202`). So the rule
cannot be B's, and A was not given it.

**Failure scenario.** A plans the node and analyst stage files with no re-entry rule, reading S5
as "resume is B's". B writes the router paragraph it was given: *"continue from the first
incomplete unit."* A run is interrupted after 3 of 5 analysts on item 7 have written findings. On
resume, the router sees item 7 incomplete and re-enters the node, which re-dispatches all five
analysts. Two consequences, the second serious: duplicated work, and — because the merge stage
"rank[s] surviving findings by how many independent analysts agreed" (`split-round-2.md:80–81`) —
the three re-run analysts' findings are counted twice, **inflating the agreement rank that is the
skill's entire trust signal**. Nothing in either half's scope catches this, because neither half
owns the rule that would prevent it.

**Remedy (seam-level, not a re-cut).** State that A owns re-entry semantics *inside* the tree
(what a node, a merge and an analyst do when re-entered on an item that already has partial
state), and that B owns only the run-level entry point. S5 currently reads as the opposite.

---

### M2 — `major` — The division contradicts itself on whether B documents the artifacts, and gives B no declaration to write them from

**Lens:** logical / completeness. **Question:** 2 (the seam).

Two statements in the document cannot both hold:

- B's scope: `METHODOLOGY.md` covers "**what a run produces** — the run-directory layout, the
  **artifacts**, and the **run-level outcome states**" (`split-round-2.md:125–127`).
- S6: "A names files inside this skeleton and states what each contains. **B documents the
  skeleton** in `METHODOLOGY.md` and points the router at it" (`split-round-2.md:190–191`).

The skeleton is three folder-level facts (`split-round-2.md:185–188`). The **artifacts** are file
names and contents, which S6 assigns to A. Likewise the **run-level outcome states** collide with
A's ownership of "permitted status values plus a retry/abandon rule" (`split-round-2.md:93`).

The seam declares exactly three things — stage index (S3), config keys (S4), completion markers
(S5) — and the cut sentence closes the set: B "consumes exactly those **and nothing else**"
(`split-round-2.md:53–54`). **None of the three carries an artifact inventory or a status
vocabulary.** So B is assigned a section it provably cannot write from its inputs.

**This is not hypothetical — it is precisely the section the divider named as B's calibration.**
B is told to check itself against `Guarded_change/METHODOLOGY.md:154–196`
(`split-round-2.md:150`). I read it: that section is a literal list of A-side filenames —
`0-baseline.md`, `1-spec.md`, `1.5-criteria.md`, `2-plan.md`, `3-redteam-plan.md`,
`6-redteam-code.md`, `8-harness.md`, `decisions.md` (`Guarded_change/METHODOLOGY.md:159–167`),
followed by prose about what each contains. B is pointed at a model it has no way to reproduce.

**Failure scenario.** B guesses artifact names (`findings.md`, `status.md`) and a status
vocabulary (`ok` / `failed`); A independently plans `verified-findings.md` plus a per-analyst
`analyst-<n>.md`, with statuses `complete` / `no-findings` / `unanalyzable`. The shipped
`METHODOLOGY.md` then documents a run that the stage files never produce — the exact
cross-file inconsistency the sibling skill maintains a standing self-check criterion against
("SKILL.md ↔ METHODOLOGY.md ↔ stage-file consistency on every rule stated in more than one
place", `Guarded_change/SKILL.md:82–83`).

**Remedy.** Either add a fourth declaration — A publishes the artifact inventory (path, name, one
line on contents) and the permitted status values — or move "the artifacts" and "the run-level
outcome states" out of B's `METHODOLOGY.md` scope. Do not leave both statements standing.

---

### M3 — `major` — No party owns the composition of the two halves, and S9 does not notice the gap

**Lens:** completeness (generative sweep). **Question:** 2 (the seam).

S9 enumerates "what neither half owns" and lists three things: the corpus, the build location,
and the forbidden directory (`split-round-2.md:204–207`). The list does not anticipate the
load-bearing fourth: **who checks that A's plan and B's plan actually compose into one skill, and
who reconciles them when they do not.**

The division asserts consistency by construction — S2's one-directional flow, "There is no
negotiation to arbitrate" (`split-round-2.md:160–162`) — and then closes the two escape routes:
S6, "Neither may change its shape unilaterally" (`split-round-2.md:191`), and S4's asymmetric
rule that B "may not drop or rename one of A's" keys (`split-round-2.md:173–174`). Ordering
protects the *first* pass; nothing protects a *revision*. A is planned first and holds an
explicitly **unresolved** design question — the terminal roll-up's status as a coordinating agent,
which the divider flags as "an open design question A must resolve"
(`split-round-2.md:86–90`) — and A's answer determines both the artifact set and possibly the
stage-file count.

**Failure scenario.** A's plan is red-teamed after B is planned, and a finding makes A merge the
analyst and verification stages into one file (or rename a config key). B's stage-index table in
`SKILL.md` and `METHODOLOGY.md` now points at a file that will never exist, and B's config
contract declares a key nothing reads. The division names no party who detects this and no party
authorised to fix it: B may not touch A's files, A may not write B's tables, and S2 says there is
nothing to arbitrate.

**Remedy.** Add to S9 an explicit owner for the composition check — most naturally B, since B
already owns the install step and therefore touches the assembled directory last — with the
authority to raise a mismatch back against A's declarations, plus a one-line statement of what
happens when a declaration changes after B has consumed it.

---

### m4 — `minor` — The cut is heavily unbalanced and strictly serialized, so it buys little; a more balanced real joint was available

**Lens:** missed opportunity / logical. **Question:** 4 (real joint — the joint is real; this is
about which real joint was chosen).

Seven of the task's eight defining properties (`split-round-2.md:16–27`) land entirely in A;
only the config property is shared, and only via A declaring keys. A owns at minimum seven files,
every unresolved design question, and the case "the hardest case, the one the skill exists for"
(`split-round-2.md:73–74`). B owns four packaging documents plus an install step, none of which
contains a method decision. S2 additionally forbids parallelism — A must be planned first
(`split-round-2.md:160–162`). So this round removes roughly the packaging from the task and
leaves the hard part intact and serialized in front of it.

**The alternative left on the table.** Cut between the **per-item leaf pipeline**
(decompose/size/over-size strategy, analyst, verification, merge) and the **tree plus package**
(the coordinating node, the blindness invariant, the terminal roll-up, the run-directory, resume,
`SKILL.md`, `METHODOLOGY.md`, the config contract, install). That is also a real joint — arguably
a sharper one, since the task's own blindness invariant is *defined* exactly at the
leaf/coordinator boundary ("a coordinating agent never reads the findings themselves, only a
terse per-child status", `split-round-2.md:22–23`) — and it divides the intellectual content
roughly in half rather than 7:1.

**Why `minor` and not `major`:** the proposed cut is legal, coherent and defensible; the four
questions do not require balance; and A can simply be divided again. The cost is a level of tree
depth and a round, not a defect that ships.

---

### m5 — `minor` — S6 fixes the run-directory skeleton by divider fiat, with a flat item namespace and no path to change it

**Lens:** unstated assumptions & risks. **Question:** 2 (the seam).

S6 fixes `runs/<run-slug>/items/<item-id>/` and says "Neither may change its shape unilaterally"
(`split-round-2.md:180–191`), while A is permitted only to "name files inside this skeleton"
(`split-round-2.md:190`). But the task requires A to "pick a per-item strategy when an item does
not fit" (`split-round-2.md:18–19`), and the most obvious such strategy — subdividing an
over-size item into parts, each analyzed and then combined — wants nested state
(`items/<item-id>/parts/<part-id>/`) that a flat item namespace does not obviously admit. A is
told the skeleton is fixed and S2 tells it there is nobody to arbitrate with.

The fix is one clause: A may **extend** the skeleton downward (add depth beneath an item) but may
not rename or relocate the fixed levels. `minor` because a permissive reading of "names files
inside this skeleton" probably already allows it — but the division should not leave the hardest
part of the task depending on which way A reads a sentence.

---

### m6 — `minor` — How a config value reaches a dispatched agent is unassigned, so S2's "A → B only" is asserted rather than established

**Lens:** unstated assumptions & risks. **Question:** 2 (the seam).

S2 claims "Information flows A → B only" (`split-round-2.md:160`). Whether that holds depends on
an unstated choice the division never assigns: do dispatched agents **read the Layer-2 config
themselves**, or are they **handed values in the dispatch prompt**?

In the source material the sibling stage files — including `charter.md`, the file handed verbatim
to cold reviewers — refer to config keys directly (`Guarded_change/stages/charter.md:12`, "named
in the project config's `redteam_context`"; `Dragonfly/stages/stage-6.md:11`, "`N` comes from the
config"), while only the router knows how to *locate* the config file
(`Guarded_change/SKILL.md:16–18`, the `guarded-change.*.{md,yaml}` glob — B's territory). A's
analysts need "what is off-limits" and "what an analyzable item is", both of which B's contract
holds (`split-round-2.md:131–133`). If A's files must name the config's location or filename
convention, that is a B → A dependency and S2 is wrong; if the node passes values down, S2 holds
and A owns the passing. The division should say which, in one sentence.

`minor` — one added sentence resolves it, and the second reading (values passed down) is
consistent with A owning "How a node drives its children" (`split-round-2.md:82`).

---

## The four questions

**1. Coverage.** Mostly good. I walked all eight defining properties plus the framing clauses at
`split-round-2.md:12–41` against the two halves: the skill-as-directory and invocation-by-name
(B), decompose/size/strategy (A), N cold read-only citing analysts (A), cold verification
dropping the unverifiable (A), agreement-ranked merge (A), blind roll-up (A), the two-layer config
(split A-declares/B-authors), facts-not-interpretation (A's common core), the build location and
the off-limits directory (S9). **One property is only partly covered — restart/resume (M1) — and
one B-side section has no input to be written from (M2).** No portion is claimed by both halves;
the path-based partition (S1) genuinely prevents that.

**2. The seam.** **Stated, and stated unusually well** — nine numbered clauses, a named direction
of flow, three explicit declarations, and an explicit list of what neither half owns. It is not
an unstated seam and does not attract the automatic `major` on that ground. It is nonetheless
where all three of my `major`s land: the declaration set is one item short (M2), it is silent on
re-entry (M1), and it has no reconciliation path (M3).

**3. The floor.** **Clean — no finding.** The floor is "one file created or one coherent edit to
one file, with the content that goes in it specified." A must decide the count, boundaries and
content of at least seven prompt files, plus the unresolved roll-up question — far above one
specified file. B must decide the content and section structure of `SKILL.md`, `METHODOLOGY.md`,
a config contract plus template, probably `README.md`, and an install step with a collision check
— five artefacts, none with specified content. **Neither half is executable without further
planning; neither falls below the floor.** The division's own argument
(`split-round-2.md:226–235`) is sound and I did not need to repair it.

**4. Real joint or arbitrary cut.** **A real joint.** The divider names four differences
(`split-round-2.md:211–224`) and I checked all four against the source: the reader differs
(verified — `Guarded_change/METHODOLOGY.md:11` says of itself "This file is opened for
orientation and config setup — not to run a stage", exactly the line quoted); the failure mode
differs (a wrong stage file misdirects every dispatched agent, a wrong `SKILL.md` frontmatter
stops the skill triggering at all — and the frontmatter is visibly the trigger text at
`Guarded_change/SKILL.md:3` and `Dragonfly/SKILL.md:3`); corpus-agnosticism binds only one side;
and the verbatim-common-core + additions-only discipline binds only A's files. The boundary is the
house shape's own, not one invented for symmetry. See m4 for the different question of whether it
was the *best* real joint.

**"This task is indivisible" — not my finding.** It divides.

---

## The six lenses

### 1. Factual — **clean (earned)**

I checked every citation the division makes. All are accurate. What I consulted:

| Claim in the division | Verified against | Result |
|---|---|---|
| `Guarded_change/METHODOLOGY.md:8–11` quote (`split-round-2.md:55–59`) | `Guarded_change/METHODOLOGY.md:8–11` | Exact, including "not to run a stage" |
| `METHODOLOGY.md:73` index-line calibration quote (`split-round-2.md:167–168`) | `Guarded_change/METHODOLOGY.md:73` | Exact |
| `SKILL.md:1–4` frontmatter, `:13–24` inputs, `:26–52` router+index, `:54–73` stop-for-human (`split-round-2.md:147–148`) | `Guarded_change/SKILL.md` | All four ranges land on the named sections |
| `METHODOLOGY.md:67–84` stage index, `:88–101` two layers, `:103–151` config contract, `:154–196` what a run produces (`split-round-2.md:148–151`) | `Guarded_change/METHODOLOGY.md` | All four ranges correct |
| `changes/<slug>/` at `Guarded_change/SKILL.md:27`; `hunts/<slug>/` at `Dragonfly/SKILL.md:31` (`split-round-2.md:182–183`) | Both files | Both exact |
| "both siblings ship one [README]" (`split-round-2.md:128`) | `ls` of both directories | True — `Guarded_change/README.md`, `Dragonfly/README.md` |
| The companion-config slot (`split-round-2.md:129–130`) | Both directories | True — `guarded-change.companion.md`, `dragonfly.companion.md`, both at top level |
| A shared core exists under `stages/` in both siblings (`split-round-2.md:103–105`) | `ls` of both `stages/` | True — `charter.md` in each, alongside `stage-*.md` |
| "a `data-distiller` skill is already installed in this environment", so a naive `cp -r` would destroy it (`split-round-2.md:136–140`) | `ls ~/.claude/skills/` | **True** — `data-distiller`, `dragonfly`, `guarded-change` are all present. This is a correct and non-obvious catch |

Note on method: I verified the install-collision claim the way the division itself permits
(`split-round-2.md:140`) — by listing `~/.claude/skills/`, not by reading the off-limits
directory.

**Unchecked, and flagged as such:** whether the *contents* of `~/.claude/skills/data-distiller/`
match the off-limits source directory — I did not look inside either, and the finding does not
depend on it.

### 2. Logical — findings M2, M3, m4

M2 is an internal contradiction (lines 125–127 vs. 190–191). M3 is a gap in the argument that
one-directional flow removes the need for arbitration — it removes it for the first pass only.
m4 concerns the cut's yield. The rest of the reasoning is sound: the ordering claim (A first)
follows correctly from the direction of the declarations, and the floor argument is valid.

### 3. Missed opportunity — finding m4

The leaf-pipeline / tree-plus-package cut, named and argued in m4. I found no other credible
alternative joint: cutting by pipeline stage would sever the blindness invariant across the seam
(the divider's S8 correctly identifies why that would be bad,
`split-round-2.md:199–202`), and cutting Layer-1/Layer-2 would leave a Layer-2 half far below any
sensible size.

### 4. Unstated assumptions & risks — findings m5, m6

Plus one risk I checked and cleared: I expected the fixed run-directory skeleton (S6) to have no
room for per-analyst raw outputs, which the agreement-ranked merge needs. It does — A "names
files inside this skeleton" (`split-round-2.md:190`), and `items/<item-id>/` can hold N analyst
files. No finding.

### 5. Fidelity — **clean (earned)**

Terms pinned to concrete mechanisms:

- **"division" / "split"** → two named sub-tasks with disjoint file-path scopes plus a stated
  interface. Mechanism present, not proxied: S1's partition is *mechanically checkable* — a path
  decides the owner (`split-round-2.md:156–158`).
- **"seam"** → nine clauses naming producer, consumer, direction, and the unowned residue
  (`split-round-2.md:154–207`). This is the actual mechanism, not "A and B will coordinate."
- **"declaration"** → three concrete artifacts A hands B, each with a stated grade of detail; S3
  even calibrates the required detail against a real line of the source material
  (`Guarded_change/METHODOLOGY.md:73`). Not a proxy.
- **"plan" (what each half produces)** → a decision about files and their content, above the
  floor. Both halves produce that, not a sketch.
- **"coordinating"** (the task's loaded term, which decides the blindness rule's reach) → the
  division does **not** pin it, and that is correct behaviour rather than evasion: it assigns the
  pinning explicitly and with reasons to A, the half that owns both the constrained agent and the
  agent feeding it (`split-round-2.md:86–97`, S8). Pinning it here would have been the divider
  making a method decision it does not own.
- **"blind roll-up"** → the mechanism (a node reads only a terse per-child status, never findings)
  is preserved intact inside one half, so no cross-seam widening is possible
  (`split-round-2.md:199–202`). Correct implementation of the task's stated property, not a
  weaker stand-in.

No term is implemented by a convenient proxy. Clean.

### 6. Completeness — findings M1, M2, M3

**The generative sweep was run.** Beyond the structure's own required parts (two sub-tasks, a
stated seam, a floor argument, a joint argument — all present), I asked what load-bearing element
a seam of this kind does not anticipate, and looked specifically for: (a) an ordering/dependency
statement — **present**, S2; (b) an artifact inventory and status vocabulary crossing the seam —
**missing**, M2; (c) re-entry/resume semantics inside the tree — **missing**, M1; (d) a
change-control or reconciliation path when a declaration turns out wrong after it has been
consumed — **missing**, M3; (e) an owner for the composed whole — **partially present** (B owns
install) but not for the consistency check, folded into M3; (f) enforcement of the off-limits
directory on both halves — **present**, S9; (g) per-half source material to be checked against —
**present** for both (`split-round-2.md:103–106`, `146–152`); (h) a concurrency owner —
**present** and correctly split, S7; (i) an owner for the unresolved roll-up design question —
**present** and explicitly named as A's, `split-round-2.md:88–90`.

---

## Summary of findings

| ID | Severity | One line |
|---|---|---|
| M1 | **major** | Resume inside the tree (re-entered node, partially complete item) is owned by neither half; S5 assigns A only markers and forbids A the resume rule. |
| M2 | **major** | Lines 125–127 give B "the artifacts" and "run-level outcome states"; line 190 gives them to A — and no declaration carries them to B either way. |
| M3 | **major** | Nobody owns the composition check or the reconciliation path when a consumed declaration changes; S9's "neither half owns" list does not notice the gap. |
| m4 | minor | The cut is ~7:1 and strictly serialized; the leaf-pipeline / tree-plus-package joint was available and is more balanced. |
| m5 | minor | S6 fixes a flat `items/<item-id>/` skeleton by fiat with no change path, which may not accommodate A's own over-size strategy. |
| m6 | minor | Whether dispatched agents read the config or are handed values is unassigned, so S2's "A → B only" is asserted rather than established. |

No blocker. The floor question is clean, the joint is real, and the factual and fidelity lenses
are clean.
