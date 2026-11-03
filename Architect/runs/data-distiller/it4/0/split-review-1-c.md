# Split review — round 1, reviewer C

**Verdict: approve.**

**The seam I judged:** runtime prompt files a dispatched cold agent reads verbatim mid-run
(sub-task A, `stages/*`) vs. the entry/contract/orientation layer a human or the invoking session
reads (sub-task B — `SKILL.md`, `METHODOLOGY.md`, `README.md`, companion, worked Layer-2 config,
scaffolding).

**Why it is a real joint, not a bisection for symmetry.** The seam is observable in both sibling
skills the task points at, and I checked it there rather than taking the divider's word:
`Dragonfly/SKILL.md:8-11` states of itself *"This file is the **router**"* with the full stage
procedures deferred to `stages/` and `METHODOLOGY.md` named as *"the orientation/reference spec
(why it exists, the config contract, what a run produces)"*; `Guarded_change/SKILL.md:7-10` carries
the same two sentences. On disk the two classes are physically separate directories —
`Dragonfly/stages/` holds `charter.md` + `stage-0a…stage-9.md` (12 files), `Guarded_change/stages/`
holds `charter.md` + `stage-0…stage-8.md` (10 files), while `SKILL.md`, `METHODOLOGY.md`,
`README.md` and `*.companion.md` sit at top level in both. Three things differ across it: the
**reader** (a cold dispatched agent vs. a human/invoking session), the **material** (imperative
instructions executed verbatim vs. explanatory reference prose and a config contract), and the
**thing produced** (the executable method vs. the skill's interface to its user).

**Coverage — no orphaned remainder.** Every file the skill directory will contain falls on exactly
one side: role/common prompts to A, router + methodology + README + companion + example config +
directory scaffolding to B. The eight defining properties are all claimed and the claim holds:
1–5 and 8 are enforced by A's prompts, 6 (Layer-2 config contract) and 7 (on-disk run state,
restart/resume) have their contract and layout specified in B and are exercised by A's roles.
The one cross-half coupling — B's router must name the phases A designs — is anticipated by the
shared vocabulary the divider fixed at the seam (`decompose/size → N cold analysts → cold verify →
agreement-ranked merge → blind roll-up`, runtime prompts under `stages/`). Per this role's own
instruction the seam is not a handoff contract, and any residual mismatch between the router's
phase names and A's role files is caught when the merged result is checked against the original
task and returns as the next task. Not a split-time defect.

**Neither half falls below the floor.** The floor is one file created or one coherent edit with
its content specified. A is a common/charter file plus roughly six role prompts (decompose/size,
analyst, verify, merge, roll-up, plus run-state discipline); B is roughly five or six files
(`SKILL.md`, `METHODOLOGY.md`, `README.md`, companion, worked Layer-2 config, scaffolding). Both
are multi-file tasks that still need planning to reach the floor, so neither is reduced past
maximum granularity and the task was correctly split rather than left whole.

**Fence honoured.** I did not read, list, grep or otherwise open
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`. Every directory listing and file read I
performed was against `Guarded_change/`, `Dragonfly/`, the two Architect stage files and the
proposed division. The fence text is carried verbatim into both sub-tasks (split-1.md lines 56-58
and 78-79), so it propagates to the planners below this cut.

**Unchecked, stated rather than assumed:** I did not open the sibling skills' `METHODOLOGY.md`,
`README.md` or `*.companion.md` bodies, nor the individual `stages/*.md` bodies beyond the two
`SKILL.md` routers. The seam claim I verified rests on the routers' self-description and the
on-disk directory split, which is sufficient to judge that the boundary is real; the internal
prose of those files could not change which side of the seam they sit on.
