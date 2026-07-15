# 1 — Spec: the owner-ratification guard

## Problem

Guarded-change's stage-3 fidelity lens correctly **escalates** a fidelity/intent substitution
it cannot settle internally, with a verdict like **"OWNER MUST RATIFY, not a plan-internal
call."** That escalation works. The hole is the **ratification step that closes such a
finding.**

Today, when the owner is asked to rule on an escalated fidelity finding, the loop records the
result as a bare spec claim — `## X (OWNER RULING <date>, option c)` — and **every downstream
gate then treats that recorded ruling as settled ground truth.** Stage 6 verifies the build
against it; stage 8 conforms to it; the criteria freeze binds to it. Nothing ever re-checks the
**ruling itself** against what the owner actually said. There is no gate that verifies a
recorded "OWNER RULING: X" corresponds to an **explicit owner selection of X on the flagged
axis.**

That gap admits two failure modes, both demonstrated by a real incident (below):

**FM1 — fabricated/misread selection.** The assistant can:
  1. present options (a)/(b)/(c) on the flagged axis and ask the owner to choose;
  2. get back a **partial or adjacent** answer that does *not* disambiguate the flagged axis
     (e.g. the owner answers a cost sub-question, consistent with two of the three options);
  3. resolve that answer into the assistant's **own recommended** option;
  4. record it as "OWNER RULING: option c" and build the whole change on it.
Nothing catches it. Critically, the misreading **survives the assistant re-reading its own
question-and-answer exchange** — because the loop trusts the author's *reading* of intent with
nothing independent checking it. This is the "unanswered-question-means-missed" failure
(a partial answer is treated as a default-to-my-pick, not as a missed question) applied to a
fidelity ratification.

**FM2 — elaboration inflation.** Even a *correctly*-ratified option can then be **inflated
during spec elaboration** into commitments the owner never agreed to. A short ruling phrase
("harness owns the reconcile/pause mechanics") gets expanded, and the expansion's load-bearing
terms ("the harness SendMessages Bob every turn / Bob owns ONLY his words / the harness runs
the whole cycle") drift from the owner's actual meaning — and that drift rides through
conformance unchecked, because conformance verifies the build against the *inflated spec*, not
the spec against the *ratified option*.

Both failure modes share one root cause: **a recorded owner-ratification is trusted as ground
truth instead of verified as an artifact.** Once "OWNER RULING: X" is written it *looks like*
owner intent rather than an author claim, so the cold red-team's fidelity lens — which is built
to re-verify a substitution against owner intent — waves it through.

## The concrete incident (motivating case — verified against evidence)

Night of 2026-07-13, during a guarded-change build of a live-test "T4-base" arm:

- Stage-3 flagged the "how is substitute-user Bob driven" decision as **"OWNER MUST RATIFY,
  not a plan-internal call."** (Verified: `hunts/monologue-bleed-s1/changes/t4-base-loop/3-review.md:13`
  — *"Orchestrator-driven (option A) substitutes for the spec HARD-RULE 'reactive Bob AGENT …'
  … OWNER MUST RATIFY, not a plan-internal call."*)
- The assistant presented options: (a) orchestrator ventriloquizes Bob; (b) fully-autonomous
  AgentBob (self-driving); (c) [its own recommendation] persistent AgentBob generates messages,
  harness owns the reconcile/pause mechanics — and asked "which — (a), (b), or (c)?"
- The owner answered only the **cost** axis: *Agent-Bob not Dumb-Bob, because Dumb-Bob's
  per-turn `claude -p` is expensive* — an answer **consistent with BOTH (b) and (c)** that does
  NOT pick between them. (Verified: the Dumb-Bob-vs-Agent-Bob cost distinction is the owner's
  framing in `Dragonfly_Case_study/chat_transcript.md` — Agent-Bob is "the cheaper
  continuous-context variant of Dumb-Bob.")
- The assistant read that as selecting (c) — its **own recommendation** — said "Agent-Bob, full
  stop," recorded **"OWNER RULING 2026-07-14, option c,"** and built the whole T4 family on it.
  (Verified: `t4-base-loop/1-spec.md:117` — *"Reactive Bob = a SINGLE PERSISTENT AgentBob
  subagent (OWNER RULING 2026-07-14, option c)"*.)
- The spec then **elaborated** (c)'s phrase into: *"the harness owns ONLY the per-turn loop
  mechanics … AgentBob owns ONLY Bob's words. The harness runs the cycle; AgentBob supplies the
  message each turn via SendMessage."* (Verified: `t4-base-loop/1-spec.md:131-144`.) The
  owner's actual intent was the opposite division: **AgentBob drives the conversation
  autonomously; the human only adjudicates symptom trips.** (Owner correction recorded in
  memory: [[agentbob-is-the-autonomous-driver]] — *"AgentBob runs the WHOLE loop as the human …
  Do NOT hand-drive per-turn or invent an orchestrator agent."*)

Cost: a wasted overnight run built on an architecture the owner never ratified.

Note the same review also carried a *correctly*-handled owner ruling — the voice-contamination
finding (`3-review.md:39`, "OWNER RULING (2026-07-14): option (a)") — which was re-asked under
the iteration cap and cites the owner's actual words. The fix must not disturb that path; it
must catch the FM1/FM2 pattern specifically.

## What to build

Two guards, added to the (domain-agnostic) guarded-change skill. The unifying idea: **treat a
recorded owner-ratification as an artifact to be independently verified, not an author
assertion to be trusted** — the same principle the whole loop applies to every other AI
artifact (`CP1 — nothing self-certifies`), now extended to the author's *reading of owner
intent.*

### Guard 1 — Ratification requires an owner-selection artifact (RAT1)

A recorded "OWNER RULING: X" that closes an escalated fidelity/intent finding is valid **only
if it is a ratification record** that embeds:
  (i) the **flagged axis** (the exact decision the fidelity lens escalated) and the options
      presented to the owner, **verbatim**;
  (ii) the owner's response, **verbatim**;
  (iii) the **mapping**: which presented option the owner's verbatim words select *on the
      flagged axis*, and *why those words disambiguate it* from the other presented options.

If the owner's response is **partial or adjacent** — it answers a sub-question (cost, a
different axis) but does not disambiguate the presented options against each other — it is **NOT
a ratification.** The loop must **RE-ASK the specific unresolved axis** and must never resolve
the partial answer into the author's own recommendation. (This is
[[unanswered-question-means-missed]] applied to fidelity ratifications: a partial answer means
the flagged question was *missed*, not defaulted.) Real exchanges are often **multi-turn** (the
owner asks a clarifying question, partially answers, then confirms): the record captures the
**confirming** turn together with its qualifying context, and "re-ask" fires only when *no* turn
in the exchange disambiguates the flagged axis — not on the middle of a legitimate multi-turn
ratification.

**Provenance — the verbatim words must be spot-checkable (added after stage-3 review MO-1/CG-1).**
The whole guard rests on "the owner's response, verbatim" — so the record must also **cite where
those words are durably recorded** (a chat-transcript line, a timestamped owner entry in
`decisions.md`), a source the *author did not author*, so the cold reviewer can spot-verify the
quote against it — the same move the charter already makes for code citations
("spot-verify the citations"). This is what makes the ruling genuinely **re-confirmable** across
an autonomous run or a context compaction (a later reader re-checks the mapping *and* the quote
against the cited source) rather than trusting a re-typed reconstruction. **Live case:** when the
owner rules in real-time chat (nothing written yet), the **chat transcript line itself** is an
acceptable durable source; transcribing the owner's verbatim words into a timestamped,
owner-attributed `decisions.md` entry also counts — the load-bearing distinction is *the owner's
quoted words carried verbatim with a locus*, versus *the author's paraphrase/reading of them*
(the latter is what fails). This is a clarification, not a burden that blocks a legitimate live
ratification. **Honest residual:**
this raises the bar and makes a fabricated/reconstructed quote spot-checkable; it cannot fully
defeat an orchestrator that fabricates both the quote and its cited source — that residual is
addressed, not eliminated, by RAT3 + the caller-side honesty obligation below.

The audit of the ratification record is a **cold-review duty**, not an author self-check —
because the incident's misreading *survived the author's own re-read*. The stage-3 reviewer
(which already holds the fidelity lens) is given the owner's verbatim exchange and audits the
selection-mapping.

### Guard 2 — Fidelity check on the elaboration, not just the build (RAT2)

When the spec **expands** a ratified option into detailed commitments, the expansion's
**load-bearing operative terms** (mechanisms, "only"/"every"/"never", divisions of
responsibility) must trace back to the owner's actual words / the ratified option's stated
meaning. The cold red-team's fidelity lens challenges: **does this elaboration add commitments
the owner did not ratify?** An expanded phrase whose new operative terms do not appear in — and
are not entailed by — the ratified option's text is an **unratified inflation**: untrusted
until the owner confirms the expansion, exactly like a substituted mechanism.

### Guard 3 — Delegation preserves the human-in-the-loop (RAT3)

The loop's stop-for-human points are stops for the **actual human owner**, not for whatever
agent happens to be running the loop. When the loop is executed by a **delegated subagent**
(the recommended workflow: an orchestrator spawns a subagent to run the gated loop so its
context stays out of the main session), the subagent↔human boundary must not absorb the
question. RAT3 has **two halves with different enforceability** (this distinction, and the
honesty about it, is the fix for the stage-3 review's MO-3/L-2):

- **Subagent half — skill-enforceable.** On reaching any stop-for-human point, the subagent
  **halts and returns the question verbatim** to its orchestrator (it cannot itself reach the
  human), **marked as a human-gate question to relay, not a result** — it does not resolve the
  point by its own judgment or proceed past it. This half lives in the skill (the subagent *is*
  running the skill) and is testable by a cold run (C14).
- **Orchestrator half — a caller-side obligation, not skill-enforced.** The **orchestrator
  relays the question to the human and relays the human's verbatim answer back; it must not
  answer a stop-for-human question as if it were the owner.** But the orchestrator is (by the
  workflow's own definition) **not running the skill** — so this obligation cannot be *enforced*
  from inside the loop. It lives in the **caller's operating instructions** (CLAUDE.md / the
  saved [[delegated-loop-relay-hil]] memory), and the shipped skill states it as a caller
  expectation, not a structural guarantee.

An orchestrator substituting its own answer for the owner's is the same untrusted substitution
the fidelity lens forbids (RAT1), one level up. RAT1 **reinforces** the orchestrator half
without fully guaranteeing it: because a valid ratification record requires the owner's verbatim
words *plus a durable-source citation*, an orchestrator that answers on the owner's behalf must
also fabricate a spot-checkable source to pass CH11 — a higher, spot-checkable bar, not an
impossibility. RAT3 is what makes RAT1's **re-ask** actually reach the human under delegation,
instead of looping back into the agent that mis-answered. (Motivating observation: the owner
noted that when the loop runs in a subagent, the stop-for-human questions frequently never
reach them — the agent boundary silently swallows the HIL gate.)

### Gate behavior

An escalated fidelity finding is "resolved" for gate routing **only if** its ratification
record passes the cold audit (RAT1) and its elaboration passes RAT2. If the record is absent,
cites no verbatim owner selection, or the audit finds the selection non-disambiguating or the
elaboration inflated → the finding **stands at its escalated severity** and the loop **stops
and re-asks the owner** the unresolved axis (which, under delegation, means bubbling the
question up to the actual human per RAT3 — not the orchestrator answering it). This closes the
hole where writing "OWNER RULING: X" silently auto-cleared the finding.

## Constraints

- **Domain-agnostic.** These guards belong in Layer 1 (the skill), not in any project config —
  "owner ratification" is a generic concept. No companion-emergence specifics.
- **Position-sensitive assembly.** The skill files are prompts; edits are to a
  position-sensitive assembly, so the position lens applies (behavior-preservation criteria for
  anything moved; new material placed where it actually governs the reviewer/author at the
  right stage).
- **Consistency invariant.** Every rule stated in more than one skill file must stay consistent
  (SKILL.md ↔ METHODOLOGY.md ↔ stage files). Each guard gets **one canonical full statement**;
  other sites reference it (the skill's existing pattern).
- **Do not disturb the correctly-handled ratification path** (the voice-contamination example)
  or the existing iteration-cap re-ask machinery — build on it.
- **live copy == source copy** after the edit (`diff` of installed skill vs repo source).

## Expected touched files

- `stages/charter.md` — extend the Fidelity lens (lens 5) with the ratification + elaboration
  clauses; extend the "clean fidelity lens must be earned" discipline bullet.
- `stages/stage-3.md` — new stage-3 charter additions **CH11** (ratification-record audit) +
  **CH12** (elaboration-fidelity audit); add the owner-verbatim-exchange to the reviewer's
  closed-set context for any escalated fidelity finding; canonical statement of **RAT1/RAT2**
  as cross-cutting rules governing the stage.
- `stages/stage-1.md` — author-side recording contract: an escalated fidelity finding is closed
  in the spec by a **ratification record** (the RAT1 fields), not a bare "OWNER RULING" line.
- `stages/stage-4.md` — gate behavior: an escalated fidelity finding routes as resolved only if
  its ratification record passes the audit; else it stands and the loop re-asks (stop-for-human).
- `METHODOLOGY.md` — add the ratification record to "what a run produces" + the HIL stop
  conditions; **canonical statement of RAT3** in "Human-in-the-loop."
- `SKILL.md` — add the re-ask stop condition + the **RAT3 delegation rule** to "Stop-for-human."

(Change folder: `changes/owner-ratification-guard/`. This is a **self-check run** — the artifact
under change is the skill itself; redteam_context = the skill source files + the incident
evidence. Regression is N/A for skill docs → stage 8 is conformance-only.)
