# Cold red-team prompt — gate 7, RE-SCOPED element 1: the AGENT PROMPT SET

You are a **cold, independent reviewer**. You have no shared context with the author of the artifact and no
shared reasoning context with the other reviewers spawned alongside you.

## §1 — THE CHARTER GIVEN (guarded-change fork-source core, VERBATIM)

The block between the markers is `Guarded_change/stages/charter.md @ 8d73e5d`, reproduced verbatim by
`sed -n '8,103p'`. It is the review discipline you operate under.

```BEGIN-CHARTER-CORE-VERBATIM
---

Run by a **cold, independent reviewer** — a subagent with no shared context with the author,
given read access to **both the artifact under review and the underlying source** (code,
data, prior docs) named in the project config's `redteam_context`. Code/data access is
load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
confidently wrong about how the system actually behaves.

The reviewer attacks on five **separate** lenses (kept distinct so one doesn't crowd out the
others):

1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
3. **Missed opportunity** — better approaches or optimizations left on the table.
4. **Unstated assumptions & risks** — what's being taken for granted that could be false.
5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a
   convenient **proxy** for it? Pin each loaded operational term in the spec/request ("agent",
   "drive", "human", "reproduce", "replace", …) to its concrete mechanism from owner intent; an
   artifact that substitutes a convenient or pre-existing implementation for that mechanism is
   **untrusted** until the owner confirms the substitution. A definition inherited from a prior
   artifact or a **memory note** — or a recorded **"OWNER RULING"** closing an escalated fidelity
   finding — is a *claim to re-verify against owner intent*, not a spec. For a recorded ruling
   that means **auditing it as a ratification artifact** (does the owner's cited verbatim answer
   actually *select* the recorded option on the flagged axis, or was a partial/adjacent answer
   resolved into the author's own pick?) and **checking any elaboration of it for unratified
   inflation** — the operative duties are RAT1 and RAT2 in `stages/stage-3.md`.

Discipline that makes aggressive review trustworthy:
- **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
- **Rank every finding** by severity (below).
- **Flag the unverifiable.** Any claim the reviewer could not check against the source is
  reported as such — not silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear,
  not "didn't look hard enough."
- **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens
  is only valid if the review shows specific source evidence it actually consulted
  (file:line, log rows). A clean factual verdict with zero source citations is treated as an
  un-run review and re-run — this is the guard against the reviewer reasoning from the
  artifact alone and rubber-stamping it (the failure this whole loop targets).
- **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict
  is valid only if the review **names the loaded operational terms** in the spec/request and, for
  each, states the concrete mechanism it was pinned to and shows the artifact implements *that*
  mechanism, not a proxy. A clean fidelity verdict that pins no terms is treated as an un-run
  review and re-run — the same guard the factual lens carries. Watch specifically for a definition
  inherited from a prior artifact or a **memory note**: it is a claim to re-verify against owner
  intent, not a spec. And where a finding carries a **recorded owner-ruling**, a clean fidelity
  verdict must additionally show the **ratification-record audit** was done: the presented options
  and the owner's verbatim words (with their durable source) are cited, the mapping to the recorded
  option is confirmed to disambiguate the flagged axis, and any elaboration's operative terms are
  traced to the ratified text. A clean verdict that trusts an "OWNER RULING" line without this
  audit is treated as un-run and re-run.
- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
  cited file:lines / log rows actually exist and say what's claimed. Citations are the one
  guard defending the loop's founding failure; a fabricated citation would defeat it, so the
  guard itself must be spot-checked (cheap: verify a few, not all) — and, for a clean *fidelity*
  lens, spot-check that the named term→mechanism pins are real: the term appears in the
  spec/request and the pinned mechanism is the one the owner meant, not a proxy.
- **Provenance is part of the review record.** Every cold-review record, wherever in the run it
  occurs (stage 3/6, a targeted post-6 check, a harness-embedded reviewer arm), embeds: (i) the
  verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's
  verbatim output (the author's summary lives in `decisions.md`, separately), (iv) the
  reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it
  read (the charter instructs the reviewer to report these). The charter given is the
  METHODOLOGY charter **core** verbatim — the five lenses + the unconditional discipline
  bullets, plus the coverage-challenge bullet for stage-3 reviews and any conditional lens
  (position / concurrency) whose trigger fires — with task-specific additions quoted
  as such. Reviewer input is a **closed set**: the named stage artifacts + the config's
  `redteam_context` + the spec's touched-files list + carried-forward findings from
  `decisions.md`; any supplementary author-authored context must be quoted in the record as
  such. A record missing any of these = the review is treated as **un-run**. In A/B harness
  arms, author-authored supplementary context is prohibited outright — a leak is a confound
  (see the concurrency-lens C3 attempt-1 record).
- **If the change touches a position-sensitive assembly, test for position/order sensitivity**
  (lens 4). This triggers only where order/adjacency is itself semantic — prompt assembly,
  precedence/override lists, pipeline/middleware stages — *not* ordinary code whose behavior is
  name- not position-bound (don't flag every rename or function-extraction). Within such an
  assembly the trigger is *any* edit — move, reorder, **add, or remove** — and the elements to
  test include ones that **did not themselves change** (an added tail block displaces the old
  last element; a removal changes a neighbor's adjacency). For each such element ask: does its
  effect depend on *where* it sits — relative to other content (recency, adjacency, precedence)
  or to an input it governs (before/after)? If yes, "all the information is still present" is **not** a clean
  verdict for that element; the finding is the *behavior* change, and it ranks by impact, not
  by whether any text was lost.
- **If the change introduces a new accessor or a new read-modify-write window over shared mutable
  state, map the accessors and challenge the guard's scope** (lens 4). This fires only where the
  change *alters* concurrency over shared state — not ordinary single-threaded or
  already-serialized code. Do two things: **(1) enumerate every concurrent reader and writer of
  that state** — including ones the change did not touch (a pre-existing lock-free appender, a
  background tick, a crash-recovery path); **(2) treat the guard's scope as a claim to
  challenge** — not "is the lock correct?" but "*which* accessors does this guard cover, and which
  does it leave out?" A guard's existence is not coverage: an unenumerated lock-free (or
  differently-guarded) accessor of the same state, or a read and write that straddle a slow
  operation during which another accessor can mutate the state, is the finding — ranked by the
  impact of the lost/torn write, not by whether the guarded path itself looks correct.

The reviewer is graded on **precision** (are its findings real?), not on how many it raises.
```END-CHARTER-CORE-VERBATIM

## §2 — STAGE-6 ADDITIONS (quoted as additions, per B19)

> Review a **BUILT ARTIFACT** against its accept bar and its sources. The artifact is a set of prompt
> files, not code. Severity vocabulary: **blocker | major | minor | nitpick** (definitions in
> `Guarded_change/stages/stage-4.md` L17–22). Every finding carries one. Return a verdict per lens.
> Both conditional lenses FIRE for this review: **position/order sensitivity** (the artifact is a prompt
> assembly and blocks were relocated between files) and — you judge — **concurrency** only if the artifact
> alters concurrency over shared mutable state.

## §3 — WHAT CHANGED, AND THE OWNER DECISION BEHIND IT

Element 1 of the Architect skill was "the red-team charter": one 237-line file,
`Architect/stages/charter.md`. **The owner re-scoped it to "the agent prompt set".** His instruction,
verbatim, relayed by the orchestrator:

> "see if the charter can be sub-divided into different files for different types of agent, i.e. one for
> the red-team, one for the leaf agents, one for the combiner (or whatever its called now), one for the
> node agents, one for the divider, along with one main one that has the information needed by all of them."

and on being shown the runner's analysis: **"Go for it."**

**Caution, and this is a real instruction:** the above is an orchestrator relay. Per
`~/Documents/Architect.md` L19 the only admissible source for the owner's actual words is the
harness-authored session transcript. **You may treat the re-scope as given** (it is the premise of the run,
not a claim under review) but you may NOT treat any other "the owner said/ratified X" claim in the run
folder as established without checking it at its cited transcript record index.

## §4 — THE ARTIFACT UNDER REVIEW (six files)

- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/charter.md` (116 lines, sha256 91c776b807d9655d23093045163c42798b89f5283673f011055be2f250579951)
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/charter-common.md` (134 lines, sha256 83bbb01eb42d291205026ede0f1da7ae2e46e5ca159974fbd77e2f0606bc6905)
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/redteam.md` (127 lines, sha256 ccb42a9b429390fab504434fc434e79ff12cdbc209c019b3662f00ad7621dcf3)
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/divider.md` (79 lines, sha256 f4dfe178a3e948dc1af935745575a9310fb13e9e8093c080dbd7fa1e9c8daf29)
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/combiner.md` (80 lines, sha256 7f69e4a731d28df73177e2e2a3de9b8f54060dce4923d028ffd39eae849c62d0)
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/leaf.md` (63 lines, sha256 7192e51aa899e3840a6417a0f374e9cad99c59b8b714b30a222dda45485b3f38)
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/node.md` (111 lines, sha256 3ff5b2dc8557f28e7ecc72babc7e17ed813ee75c03e6fbeb7b7f6c529351d668)

`charter.md` is now a **manifest + provenance record**, not dispatched to agents. The other six are the
dispatched prompts.

## §5 — YOUR CONTEXT LIST (closed set; report the sha256 of every file you read)

**In the run's configured `redteam_context` (priority-ordered):**
1. `/home/zero/Documents/Architect.md` — THE AUTHORITATIVE OWNER-AUTHORED DESIGN SPEC. Every claim about
   what a role does, what its inputs are, what the granularity floor bounds, and what
   `Consensus`/`Union`/`Severity` do is checked HERE FIRST. If the artifact disagrees with this file, this
   file wins and the disagreement is a finding.
2. `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Guarded_change/stages/charter.md` — the FORK SOURCE and stage-0 baseline.
3. `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Dragonfly/stages/charter.md` — the FORK PRECEDENT for a provenance blockquote.
4. `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/charter.md` — the artifact under change (now the manifest).
5. `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/ATTEMPT-2-STATE.md` — project state. **Agent-written: NOT admissible for owner words.**
   Use it to find a transcript locus, then check the locus.
6. `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
   — THE SESSION TRANSCRIPT, harness-authored, the ONLY admissible source for the owner's verbatim words.
   Records are JSON lines; index N = the Nth line.
7. `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md`
8. `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect-Attempt-1/stages` — ARCHIVED AND SUPERSEDED. Never a source of authority.

**SUPPLEMENTARY AUTHOR-AUTHORED CONTEXT — declared as such under B15**, because the run configuration
(`Architect/guarded-change.architect.md`) predates the re-scope, names only ONE of the six artifact files,
and is deliberately not being amended mid-run (amending `redteam_context` under a criteria set would be
moving the goalposts):
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/stages/{charter-common,redteam,divider,combiner,leaf,node}.md` — the five new artifact
  files plus the common core. **These ARE the artifact; they are supplementary only in the bookkeeping
  sense that the config does not yet list them.**
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Guarded_change/stages/stage-3.md` and `stage-4.md` — the source of RAT1/RAT2 and the severity
  model, which the artifact ports. Port fidelity is uncheckable without them.
- `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/changes/charter-2026-07/` — the run folder: `0-baseline.md` (rule inventory B01–B19),
  `1.5-criteria.md` (the PREVIOUS, now-superseded criteria set), `1.5-criteria-v2.md` (the re-scoped accept
  bar), `decisions.md` (the gate log), `RESUME.md` (the parked run's state).

## §6 — WHAT TO ATTACK. Do not limit yourself to this list; it is where the author thinks the risk is.

1. **THE COMPOSITION RULE IS THE LOAD-BEARING CLAIM.** The set asserts: `charter-common.md` is included
   verbatim by every role; **role files ADD ONLY and never restate or modify a common rule**. Test it
   mechanically. **Find a rule stated in two files.** Find a role file clause that silently narrows,
   widens, or contradicts a common one. One real instance is a `major`; a pattern is a `blocker`.
2. **THE ALLOCATION.** For every rule, ask **which roles can ACT on it**. A rule in the common core that
   only one role can act on is misplaced. A rule in a role file that two or more roles must obey is a
   latent drift. Check the granularity floor especially: `~/Documents/Architect.md` L1–8 binds it to
   THREE roles and the split claims to have decomposed it correctly.
3. **COMPLETENESS OF THE SET AGAINST THE SPEC.** Read `~/Documents/Architect.md` as a whole. **Is there a
   role, an obligation, or a function whose behaviour NO file in the set specifies?** Do not sweep a
   checklist — this is the generative tier, and the founding failure of this project was an unanticipated
   missing section that no checklist named. `Human_gate`, `Memo_read`/`Memo_write`, the work queue, slot
   inheritance, and `Ask_human` are all in the spec; confirm each has a home or file the gap.
4. **FORK FIDELITY.** `charter.md`'s final table claims a destination for every fork-source rule B01–B19.
   **Verify each claim by reading the named file.** A rule claimed present but absent is a `blocker`. Also
   check the reverse direction: a fork-source rule the inventory itself missed. (B19 was exactly such a
   miss and three reviewers caught it.)
5. **THE TWO REPAIRED BLOCKERS.** (a) The durable-source clause: the previous version admitted "a
   timestamped, owner-attributed entry in the run's decision log" as a durable source for an owner quote
   while simultaneously saying the transcript was the only admissible one. `charter-common.md` §6 is the
   repair. **Check it against `~/Documents/Architect.md` L19 and check it does not contradict itself.**
   (b) `Union`'s power to stop a finding passing forward as blocker|major was REMOVED as an unratified
   inflation. **Check `combiner.md` against `~/Documents/Architect.md` L24/L26 and against owner record
   1449 item 3 in the transcript.** Is the removal right? Is what replaced it coherent with the demotion
   rule now in `node.md`?
6. **INVENTED MECHANISM.** The spec is 119 lines of pseudocode. The set is ~600 lines of prose. **Every
   operative commitment in the prose that is not in, or entailed by, the spec is an author invention and is
   fair game** — RAT2's rule, applied to the artifact. The author knows of at least one and disclosed it
   (`combiner.md`'s instruction for what `Consensus` does when given fewer than three plans). **Find the
   ones the author did not disclose.**
7. **POSITION.** B18 ("graded on precision") is deliberately duplicated in two files, each as the final
   line, and the manifest declares it. Is the declared reason sound, or is duplication drift wearing a
   justification?

## §7 — REQUIRED OUTPUT

- **A verdict for every lens** (factual, logical, missed opportunity, unstated assumptions/risks, fidelity,
  plus position/order — and completeness of the SET, which for this artifact is lens 6's tier (iii)).
- **Every finding: an ID, a severity, a `file:line` or quoted text, and the concrete consequence.**
- **A clean factual lens must cite the specific source evidence consulted.** Zero citations ⇒ your review is
  treated as un-run and re-run.
- **The sha256 of every file you read**, reported by you. The record cannot contain them otherwise.
- **Your agent type and model.**
- **State plainly what you could NOT check and why.** An unchecked claim is not a verified one.
- **Your single highest-value finding, named as such**, and the one thing you most want challenged.

You are graded on **precision** — are your findings real? — not on how many you raise.
