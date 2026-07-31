# Split review — round 1, reviewer B

**Fence honoured:** I did not read, list, grep or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`. Nothing in this review derives from it.
My only source material was the two sibling skills `Guarded_change/` and `Dragonfly/`, plus the
proposed division itself.

## Verdict: **APPROVE**

**The seam I judged:** the executable method (the per-role prompt files under `stages/` that carry
out the distillation pipeline) versus the skill's interface layer (`SKILL.md` router with its
frontmatter, `METHODOLOGY.md` with the Layer-2 config contract and on-disk run-state layout,
`README.md`, the companion file, and a worked example config).

**Why it is a real joint, not a bisection for symmetry.** The two sides differ on all three axes
the question asks about. *Material:* imperative second-person prompt text that an agent executes
against a corpus, versus explanatory reference prose and frontmatter that a reader or the invoking
session consults. *Kind of work:* designing a multi-agent protocol — how many analysts, what a
verifier drops, how a merge ranks by agreement, what a blind coordinator is permitted to see —
versus specifying a contract (what a per-corpus config must and must not supply) and a router.
*Thing produced:* the method itself versus the skill's interface to whoever invokes it. This joint
is structurally visible in both siblings, which separate `stages/` from their top-level documents
(`Guarded_change/stages/` vs `Guarded_change/SKILL.md`, `METHODOLOGY.md`, `README.md`,
`guarded-change.companion.md`; same shape in `Dragonfly/`).

**Coverage.** Every file the skill directory will contain falls to exactly one half: `stages/*` to
A, the top-level documents plus scaffolding plus the example config to B. I found no orphaned
remainder. The three properties that straddle the seam — the Layer-2 config, restart/resume from
on-disk state, and the pipeline's own stage vocabulary — are the owner's own dedup case: B fixes
the contract and the state layout, A's roles consume them, and any mismatch between the two blind
halves is caught when the merged result is checked against the original task and becomes the next
task automatically. That is not a reason to cut differently.

**Floor.** Neither half falls below the floor of *one file created or one coherent edit to one
file, with its content specified*. A is on the order of six to eight prompt files (a shared
common/charter plus one per role: decompose/size, analyst, verify, merge, blind roll-up); B is on
the order of six (`SKILL.md`, `METHODOLOGY.md`, `README.md`, the companion, scaffolding, one worked
config). Both are comfortably several floor-sized steps of real planning work, so question 2 does
not fire and the task was correctly split rather than left whole.

## One inaccuracy in the justification — recorded, not blocking

The division justifies the seam by asserting that `Dragonfly/stages/*.md` and
`Guarded_change/stages/*.md` "are runtime prompts handed to cold agents mid-run" (split-1.md, the
*Where the seam is* section). That is false of the siblings as written. In both, the numbered stage
files are procedures the **invoking session** reads as it walks the loop: `Guarded_change/SKILL.md`
line 31 instructs "at each stage, read that stage's file for the full procedure + the rules it must
apply," and `Guarded_change/stages/stage-2.md` is a procedure for whoever is driving the loop, not
a prompt handed to a dispatched subagent. The only sibling file actually handed to cold dispatched
agents is `stages/charter.md` — `Guarded_change/stages/charter.md` line 3 says so of itself ("This
is the ONE copy of the red-team charter's common core. Stage 3 and stage 6 both read it"), and
`SKILL.md` lines 40 and 43 show it passed alongside the stage file at exactly the two red-team
stages. `Dragonfly/SKILL.md` lines 43, 46 and 49 show the same pattern.

I record this rather than reject on it for two reasons. First, it does not move the seam: whether a
runtime file is executed by a dispatched agent or by the driving session, it is still executable
method rather than interface prose, and the joint between those two things is where the cut was
made. Second, sub-task A does not actually depend on the faulty label — A's body enumerates its
scope directly (decompose/size with the over-size strategy, the N cold analysts, the cold verify,
the agreement-ranked merge, the blind roll-up, and the run-state discipline), and that enumeration
is what a planner acts on.

The residual risk worth naming, since it is cheap to name and expensive to discover late: if A's
planner reads the framing label "files a dispatched agent reads verbatim" more literally than A's
own enumeration, it could scope out the orchestration procedure for whichever phases turn out to be
driven by the invoking session rather than by a dispatched agent — most plausibly decompose/size
and the merge. That would surface as a missing driver document when A's plan is red-teamed against
the original task, which is precisely the mechanism the split reviewer is told not to pre-empt. If
the divider is re-issuing the sub-task text for any other reason, the cheap fix is to describe A as
*the executable method* and drop the reader-identity framing; if not, leave it.
