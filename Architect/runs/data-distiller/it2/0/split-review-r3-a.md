# Split review — round 3, reviewer A

Reviewing the proposed division in
`Architect/runs/data-distiller/it2/0/split-round-3.md` (cut: *method under `stages/`* vs.
*package + install*), against the task and the granularity floor quoted at that file's head.

**Inputs I had:** the split file, the floor, and the task's source material
(`Guarded_change/`, `Dragonfly/`). No plan — correct, and I did not look for one.
`Data-Distiller/` was not read, listed or grepped.

---

## Findings

### F1 — `blocker` — The seam is a sibling-to-sibling coordination protocol, and the framework that will execute this division provides none of its three mechanisms

The seam's load-bearing clauses are S2, S3 and S10. Together they require:

1. **an ordering** — "*A is planned first*" (S2);
2. **a data channel from A's planner to B's planner** — "*A's plan ends with a section headed
   `## Declarations`* … *That section is B's sole input from A*" (S2), whose five tables B is
   then required to write `SKILL.md`'s and `METHODOLOGY.md`'s index tables, the config contract's
   key list, "what a run produces", and S3(e)'s two resolved method decisions *from*;
3. **a return channel** — "*S10's mismatch report*", B → A, after which "*B's dependent sections
   are re-derived*" (S2, S10).

None of the three exists. The node that consumes a division does this
(`Architect/stages/node.md:58–61`):

> **Division is non-empty**: **gate first** (below), then spawn **two child nodes** … with
> `(division.first, plan, granularity, depth + 1, node_id + ".1")` and `(division.second, plan,
> granularity, depth + 1, node_id + ".2")`. **Wait for both.** Then `plan = Union(the two child
> plans)`

Both halves are **spawned together** — there is no first and second, and each child's argument
list contains its own sub-task and the *inherited* plan, never its sibling's output. The only
integration point is a combiner running `Union` **after both have finished**, which is too late
to be an input to either. `Architect/stages/common.md:8–11` states the same from the agent's
side: an Architect-dispatched agent shares context "*none with the siblings spawned alongside
you*". And `node.md:6–9` forbids the workaround explicitly:

> `return plan` **is** the join … There is no "subtree complete" fact anyone reads off disk and no
> status file to publish. **Do not build a coordination protocol.** A prior attempt implemented
> this recursion as a filesystem protocol and nearly every defect it produced was a bug in that
> protocol.

**Concrete failure:** B's planner is dispatched concurrently with A's, never sees any
`## Declarations` section, and must still produce `SKILL.md`'s file-index table and entry-stage
handover, `METHODOLOGY.md`'s "what a run produces", and the config contract's key list. Every one
of those is a section the division says B writes "*from A's Declarations … not from B's own
invention*" (B's `METHODOLOGY.md` bullet) and "*from this table alone*" (S3a). With the carrier
absent, B invents them — which is precisely the outcome S2 exists to prevent, and it will look
locally correct in B's plan. `Union` then merges an A-plan and a B-plan whose file indexes,
config keys and artifact inventories were derived independently.

This is not a defect in the *cut* — the method/package line may well be right. It is a defect in
how the seam transmits. **`blocker` because it cannot be executed as written**, and because
everything below the cut inherits the seam.

**Note on fairness to the divider, and the shape of a repair.** `Architect/stages/divider.md:40–43`
does invite a producer/consumer seam ("*what one half produces that the other consumes*"), so the
divider was following its own charter; the contradiction is between that line and `node.md`'s
concurrent, channel-free dispatch. The repair that preserves this cut is to make the seam
**derivation-independent instead of communication-dependent**: whatever B needs must be *fixed in
the seam text itself* — which both halves receive — rather than *sent by A at plan time*. S6
already works this way (a minimum run-directory skeleton fixed in the seam, extensible downward)
and is the model. Concretely: the file index, config-key set, artifact inventory, status
vocabulary and the two S3(e) decisions would need to be either (a) fixed in the seam as a
contract both halves must satisfy, or (b) explicitly deferred to the `Union` combiner as
reconciliation work, with the seam naming what it must reconcile. Option (b) also gives S10
somewhere real to live.

**Unchecked:** I could not confirm from `node.md:58–61` that the *seam text* travels down with
each sub-task — the argument list shows only `task`. `divider.md:43` asserts "*Everything beneath
this cut inherits the seam*", so I treated it as travelling. If it does not, the repair above
fails too and the division is in worse trouble than F1 states.

---

### F2 — `major` — `## Declarations` carries no dispatch topology, but B must write the pipeline diagram, the stage-index table and the router walk

Independent of F1: even granting the carrier, its five tables are a **set**, not a **graph**.
S3(a) gives "*path, and an index-grade line*" per file, with one row marked as the entry file.
S3(b)–(e) give config keys, artifacts, statuses, and two resolved decisions. Nothing in the five
declares **control flow** — which file dispatches which, fan-out (N analysts per item), where the
tree branches, what runs after verification, how a node returns.

B is nonetheless required to produce exactly that:

- B's `METHODOLOGY.md` bullet: "*the pipeline diagram*" — the sibling it is modelled on is
  `Guarded_change/METHODOLOGY.md:37–54`, a flow with ordering and bounce edges, not a list;
- B's `SKILL.md` bullet: "*the file-index table*", modelled on
  `Guarded_change/SKILL.md:34–45`, which is ordered by stage number and states the walk;
- and the frontmatter `description`, which must characterise the method (see F5 for why that
  field is load-bearing).

S4 forbids B from filling the gap ("*reproduces only what S3's Declarations state*") and the
`METHODOLOGY.md` bullet forbids invention. So B is required to write a section it is
simultaneously forbidden the material for. The division itself flags that this method "*is a tree
of concurrent agents*" rather than the siblings' linear `stage-0 … stage-9` shape (sub-task A,
para 1) — which is exactly why the topology cannot be recovered from an ordered filename
convention the way it can in the siblings.

**Remedy sketch:** a sixth declaration — the dispatch graph: for each file, who dispatches it,
how many instances, and what it returns to whom.

**Partial mitigation I checked and am not persuaded by:** S3(a) calls for an "*index-grade line*"
calibrated to `Guarded_change/METHODOLOGY.md:73` ("*checkable, labeled accept bar;
position/concurrency criteria; self-check criteria*"). That line is a content summary and carries
no successor relation; the ordering in that sibling table comes from the stage numbers in column
one, which this method has explicitly given up.

---

### F3 — `major` — S10 conflates two different deliverables under one name, and one of them contradicts S2

"The composition check" names two things that differ in *who does them, when, and to what*:

- **(i) a plan-time reconciliation between the two plans** — S10: "*After both halves are planned,
  B checks that its consumed Declarations still match A's plan* … *If a Declaration changed after
  B consumed it … B raises a mismatch report*";
- **(ii) a build-time self-check criterion shipped inside the skill** — B's in-scope bullet: "*the
  standing self-check criteria for the assembled skill, on the model of
  `Guarded_change/SKILL.md:81–83`*" (verified: that citation is the standing criteria list —
  "*live copy == source copy (`diff`); SKILL.md ↔ METHODOLOGY.md ↔ stage-file consistency on every
  rule stated in more than one place*").

(i) is an act B performs during planning, over two plan documents. (ii) is text B writes into
`SKILL.md`, to be executed later against files that do not exist yet. B is a **planner**, so
(ii) is a deliverable and (i) is a duty, and the division gives them one label and one clause.
The executable consequence: B satisfies the bullet by writing the shipped criteria, never
performs the plan-time reconciliation, and the single B → A channel never fires — with nothing
detecting that, because both readings can cite S10.

**Secondary contradiction inside the same clause.** (i) requires B to read A's plan and compare
rules "*across the files*" A planned. S2 states flatly "*That section is B's sole input from A*"
and "*B does not read the rest of A's plan, and does not open A's planned files, to write its own*".
The trailing qualifier "*to write its own*" makes a temporal reconciliation *available* — blind
while authoring, sighted while checking — but the division never states it, and the flat "sole
input from A" sentence says otherwise. The one invariant the seam is built on should not be
resolvable only by inference. (Under F1 the plan-time half is impossible regardless; this finding
stands on its own because the conflation survives any repair to F1.)

---

### F4 — `major` — the `## Declarations` obligation is not propagated if A is divided again, and the division explicitly expects that it will be

Lines 302–304 anticipate the recursion: "*if A is divided again the audience line still holds
beneath it*." That checks the *audience* property and nothing else. A's obligation to emit a
single well-formed `## Declarations` — five complete tables covering every file, key, artifact and
status in A's whole subtree — is stated only at A's level (S2, S3: "*Each is a required output of
sub-task A; A's plan is incomplete without them*").

If A is divided, `node.md:58–61` gives A.1 and A.2 different halves and merges them with `Union`.
Each would produce, at best, a partial Declarations over its own files; nobody is assigned to
union them into one section, to detect a key declared by A.1 and contradicted by A.2, or to mark
*the* entry file (S3a) when the entry file is in one half and the roll-up in the other. B's sole
input can therefore arrive fragmentary or internally inconsistent, and B — forbidden to read the
rest of A's plan — cannot tell.

Because the division already contemplates this case and checks only one property of it, this is a
load-bearing contingency left out rather than an unforeseeable one. The seam needs a clause making
the Declarations obligation binding on any division of A (each sub-division emits its part, and
the reconciliation is named as the merge's work).

---

### F5 — `minor` — S1 claims a total partition, but S6 and S3(c) give A paths outside `stages/`

S1: "***Any path under `Data-Distiller-impl/stages/` is A's. Any other path in, or produced by,
the build is B's*** … No file is planned by both, and no path falls to nobody."

S6 then hands A the run directory below the fixed levels: "***A may add depth and add siblings***
— nested sub-items beneath an over-size item, node-level state, a corpus-level deliverable at the
run root", and S3(c) requires A to declare "*Every file the method writes into the run directory:
path (relative to the skeleton in S6)*". Those are paths not under `stages/`, owned by A. Either
"produced by the build" excludes run artifacts — in which case S1's totality claim is false, since
run-artifact paths fall under neither clause — or it includes them, in which case S1 and S6
contradict.

`minor`: a competent reader resolves it in A's favour from S6/S3(c), and the fix is one clause in
S1 ("paths inside a run directory are governed by S6"). But S1 is advertised as the clause that
makes the partition total, so the false totality claim is worth correcting rather than recording.

---

### F6 — `minor` — S1's default can silently capture a method file, because "every agent-executed prompt lives under `stages/`" is a real constraint on A that is never stated as one

A is told it "*decides … **how many files there are and where their boundaries fall***" and is
"*free to structure them as pipeline stages, as agent roles, or as a mix*" — but A's scope is
defined by *path* ("every file under `…/stages/`"), while its content scope is defined by
*audience* ("the prompts a dispatched agent reads verbatim"). S1 then routes "*a third
subdirectory neither half anticipated*" to B, whose out-of-scope list forbids "*the content of any
file under `stages/`*" but says nothing about a method file placed elsewhere.

Failure case: A concludes the shared core, or a role file, belongs at the build's top level
(neither sibling forces the choice — both put `charter.md` inside `stages/`, but that is one data
point, and this method has more roles than either). By S1 that file is B's, and B has no method
authority to write it. One sentence fixes it: *every file a dispatched agent reads is A's and must
be placed under `stages/`; S1's default therefore never captures one.*

---

### F7 — `minor` — miscitation: `Guarded_change/METHODOLOGY.md:79` does not support the claim S9 rests it on

S9: "*(verified: neither sibling's `SKILL.md` contains a dispatch step; the operative
reviewer-spawn rule lives in the stage files, `Guarded_change/METHODOLOGY.md:79`)*".

Line 79 is a table row: `| 7 — Gate | stages/stage-7.md | route by severity |`. It says nothing
about reviewer spawning. The claim's actual locus is `Guarded_change/METHODOLOGY.md:137–138`:
"*(The operative reviewer-spawn form of this rule lives in `stages/stage-3.md` /
`stages/stage-6.md`.)*"

I checked the underlying claim independently and it holds: grepping both `SKILL.md` files for
spawn/dispatch language returns only `Guarded_change/SKILL.md:20` (a *validation* trigger, "*at
any later reviewer spawn*"), `:66–68` (delegation), and `:78` (the dogfooding section) — no
dispatch step in either loop. So S9's conclusion survives; the citation supporting it does not.

---

### F8 — `minor` — S6's "the siblings root theirs at the skill's own directory" is not what the cited lines say

`Guarded_change/SKILL.md:27` reads "*Create a change folder `changes/<slug>/`*" and
`Dragonfly/SKILL.md:31` reads "*Create a hunt folder `hunts/<slug>/`*". Both are **unrooted
relative paths**; neither states a root. The claim is an inference from the on-disk fact that
`Guarded_change/changes/` and `Dragonfly/changes/` exist inside the skill directories (which I
confirmed by listing). That evidence is real but it is not the cited evidence, and it is weaker
than the seam presents it — the siblings may simply be run from their own directory.

S6's *decision* (root `runs/` at the invoking session's working directory) is sound regardless,
and its reasoning — an installed skill at `~/.claude/skills/<name>/` running against an arbitrary
read-only corpus must not mutate itself — stands on its own without the sibling comparison. Fix
the support, not the decision.

---

### F9 — `minor` — the third "real joint" differentiator is contradicted by S11

"*What must be corpus-agnostic vs. what names the corpus. B owns the one place corpus specifics
may live.*" But S11 says: "*The corpus, and any example corpus — the skill is corpus-agnostic and
no corpus is in scope.*" B therefore ships a **contract and a template with placeholders** and
names no corpus either. Both halves are corpus-agnostic; what actually differs is that B owns the
*schema and location* of the slot where specifics would later go, and that A's files may not even
locate it (S7).

The differentiator survives in that weaker form, and the other three (who executes the file; the
failure mode; the authorship discipline) are unaffected — so the joint is still real. Filed
because the argument for the joint is what question 4 turns on and one of its four legs is
overstated against the division's own S11.

---

### F10 — `minor` — S8 pre-decides part of the question S3(e) assigns to A

S3(e) requires A to resolve and declare "*how far the blindness rule reaches*", and adds "*B does
not decide them*". S8 has already decided the top end: "*the invoking session executes `SKILL.md`
and **is itself the topmost coordinating agent***", from which it derives a binding requirement on
A's formulation ("*A's formulation must be written to bind any driver of the method, including the
invoking session*"). That is an answer to the reach question, made by the seam, before A is asked.

Also unresolved in the same area: sub-task A's last bullet says "*Both a node above an item and
the per-item merger have children*" and leaves the merger's status to A — so A can answer "the
merger is not a coordinating agent" while S8 has fixed the invoking session as one. The two are
compatible, but the seam should say it is fixing one end and leaving the rest to A, rather than
appearing to do both.

---

### F11 — `minor` (missed opportunity) — A is told it has no worked example for the universal core, and one exists in this repo

The caveat handed to A is emphatic: "***No sibling ships a core read by every dispatched agent, so
A is designing that file without a worked example and should not inherit red-team shape into
it.***"

The first clause is **true of the two named siblings** — I verified both charters are subset-shared,
not universal: `Guarded_change/stages/charter.md:1` is "*# The red-team charter (shared by stages 3
and 6)*" and `Dragonfly/stages/charter.md:1` is "*# The red-team charter (shared by stages 1, 4,
7)*".

But `Architect/stages/common.md` — in this repo, on this branch, and the file every agent in this
very run reads — is exactly the artifact A is told does not exist. Its own first line:
"***Every agent Architect dispatches reads this file first, then its role file.*** This states what
binds all roles; the role file adds what is specific to yours." It is a verbatim-included common
core with additions-only role files (`redteam.md`, `redteam-split.md`, `leaf.md`, `node.md`,
`combiner.md`, `divider.md`), and its content — what you are, your inputs, the floor, severity,
"nothing self-certifies", where output goes — is **not** red-team material, which is the specific
inheritance the caveat warns A against.

Since sub-task A's source list is where A learns what to check against, adding this pointer costs
one line and removes the exact hazard the caveat names. (I note the task's SOURCE MATERIAL section
names only `Guarded_change/` and `Dragonfly/`; it reads as a floor of what must be checked, not a
ceiling on what may be consulted. If the divider judges otherwise, the caveat should at least be
softened from "*without a worked example*" to "*without one among the two named siblings*".)

---

## The four questions

**1. Coverage — clean, subject to F5/F6.** I walked every clause of the task against the two
halves: decompose/size/over-size → A; N cold analysts, read-only, cite-every-finding → A;
verification pass → A; agreement-ranked merge → A; blind roll-up → A, with S8 binding the invoking
session; per-corpus config (analyzable item, off-limits, concurrency ceiling) → B's contract, A
declares keys, S9 splits key from enforcement; restart/resume → S5 splits by kind (consulting
instructions A, run-level entry point B); facts-not-interpretation → A; markdown prompt files,
invokable by name, installed at `~/.claude/skills/<name>/` → B; build location and the off-limits
directory → S11. No orphaned remainder found, and no portion where both halves are told the other
owns it. The only coverage defects are the two path-partition edges above, both local.

**2. The seam — stated, thorough, and unsound. `blocker` (F1), with F2/F3/F4 standing
independently.** The seam is stated at unusual length and its ownership rules are careful; what
fails is transmission. As written it presumes an ordering, a sibling channel and a return path
that the executing framework does not provide, and its one carrier omits the dispatch topology
that two of B's required sections are built from.

**3. The floor — clean, no finding.** Floor: "*one file created or one coherent edit to one file,
with the content that goes in it specified.*" A must decide how many prompt files exist, where
their boundaries fall, and the content of each (minimum: shared core, decomposition/sizing,
analyst, verification, merge, node, roll-up) plus the over-size strategy and re-entry semantics —
many files, none pre-specified. B must decide the content and section structure of `SKILL.md`,
`METHODOLOGY.md`, `README.md`, a config contract plus template, an install step with a collision
check, and the composition-check criteria — five-plus files, none pre-specified. **Neither half is
anywhere near the floor**; the division's own closing argument on this is correct. The imbalance
(A larger) is not a floor problem and I raise nothing on it — I checked the supporting measurement
and it is fair: `Guarded_change/stages/` is 68.9 KB / 967 lines against 37.3 KB / 597 lines for
`METHODOLOGY.md` + `README.md` + `SKILL.md` + the companion config, i.e. ~1.85× by bytes, ~1.6× by
lines. "Roughly twice" is defensible.

**4. Real joint or arbitrary cut — a real joint. No finding beyond F9.** Something genuinely
changes at this boundary, and the strongest of the four claimed differences is verifiable:
**who executes the file.** A's files are read verbatim and acted on by a *dispatched agent*; B's
`SKILL.md` is executed by the *invoking session* (`Guarded_change/SKILL.md:25–32` is imperative —
"Create a change folder… append a line to `decisions.md`… Walk the loop"); `METHODOLOGY.md` is
executed by nobody (`Guarded_change/METHODOLOGY.md:9–11` — "*opened for orientation and config
setup — not to run a stage*"). I also confirmed the division's *correction* of its own opening
citation is right: `SKILL.md` is **not** inert, so "executed vs. not" would have been the wrong
joint and "who executes it" is the right one. The failure-mode difference is likewise real —
frontmatter is the trigger text, which I verified end-to-end rather than by inference: the
`description` at `Guarded_change/SKILL.md:3` and `Dragonfly/SKILL.md:3` appear **verbatim** as
those skills' entries in my own available-skills listing, so a bad description means the skill is
never selected and never runs at all, a failure no `stages/` review would catch. The rejected
alternative (leaf pipeline vs. tree + package) is rejected for a stated, sound reason — it would
put the blindness invariant on the seam — and I agree that reason outweighs the better volume
balance.

---

## Verdict per lens

**1. Factual — issues (F7, F8, F9); otherwise clean, earned.** Citations I opened and confirmed
accurate: `Guarded_change/METHODOLOGY.md:9–11` (quote exact), `:73` (index-grade line, exact),
`:154–196` (is an artifact inventory), `:67–84`, `:88–101`, `:103–151` (section bounds correct);
`Guarded_change/SKILL.md:1–4`, `:13–24`, `:25–52`, `:54–73`, `:75–85` (all section bounds correct),
`:16–18` (the `guarded-change.*.{md,yaml}` glob), `:27`, `:48–50`, `:81–83`;
`Dragonfly/SKILL.md:3`, `:31`; `Guarded_change/stages/charter.md:1` and
`Dragonfly/stages/charter.md:1` (both quotes exact — subset-shared, not universal). Independently
verified: `~/.claude/skills/` contains `data-distiller` alongside `dragonfly` and `guarded-change`,
so B's install-collision requirement is grounded in fact, not caution. Two citations do not
support their claims (F7, F8) and one claim contradicts the division's own S11 (F9).

**2. Logical — issues (F3, F4, F5).** The conflation in S10, the unpropagated Declarations
obligation, and the false totality claim in S1.

**3. Missed opportunity — issue (F11), plus the repair direction recorded in F1.**

**4. Unstated assumptions & risks — issue (F1).** The largest unstated assumption is that the two
halves can be sequenced and can talk. Second, flagged as unchecked in F1: that the seam text
travels down with each sub-task.

**5. Fidelity — issues (F2, F3, F10); otherwise pinned.** Terms pinned and the mechanism each was
pinned to: *"seam"* → S1's path partition + S2's named carrier + S3's five tables + S4–S11's
ownership rules (faithful to `divider.md:40–43`'s definition; the infidelity is against `node.md`'s
execution model, F1). *"verification"* → A's stage, pinned to the task's own words, "re-checks
every citation and drops the unverifiable". *"cold" / "independent"* → the shared core every
dispatched agent reads first. *"blind roll-up" / "coordinating"* → S8 plus A's node file, with the
reach deliberately deferred to A (F10 on the part S8 pre-decides). *"install"* → copy to
`~/.claude/skills/<name>/` with a refusal-to-overwrite check. *"router"* → B's `SKILL.md`, executed
by the invoking session, handing over at the declared entry file. **Fails to pin: "composition
check"** (F3 — two different mechanisms under one term) and **"pipeline diagram"** (F2 — named as
B's output with no mechanism producing the material for it).

**6. Completeness — issues (F2, F4, F6).** The generative sweep was run. Beyond ticking the seam's
own S1–S11 and the four questions, I asked what a *concurrent-agent* method needs that a
*linear-stage* method does not, and what a *recursive* division needs that a one-level division
does not. That produced: the dispatch-topology declaration (F2 — the siblings get topology free
from stage numbering, this method gives that up); the Declarations obligation under re-division of
A (F4); the audience-vs-path scope mismatch (F6). I also checked and found **no** gap on: naming
vocabulary shared across halves (paths in S3(a) carry it), the run-level failure/stop-for-human
account (S3(d) → B), config values reaching nested agents (S7 hands down by value), and the
corpus-level deliverable's owner (S3(e)).

## Was any portion of the task left unaddressed?

No portion of the task is unassigned — see question 1. What is unaddressed is not a *portion of
the task* but a *precondition of the division*: the seam's transmission mechanism (F1).
