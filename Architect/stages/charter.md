# The red-team charter

The ONE copy of Architect's cold-review discipline. Every cold reviewer Architect dispatches reads this
core **verbatim**; each caller adds its own aiming on top (see "The two callers" at the end).

> **Provenance.** Forked from `Guarded_change/stages/charter.md @ 8d73e5d` (sha256
> `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`).
> **CARRIED:** the five lenses; every unconditional discipline bullet (cite-or-it-doesn't-count, rank every
> finding, flag the unverifiable, "no issue found" is valid, earned-clean factual, earned-clean fidelity,
> spot-verify the citations, the provenance record + closed set, graded on precision); both conditional
> lenses (position, concurrency); and the charter-composition rule.
> **CHANGED:** five lenses → **six** (Completeness added, with its three tiers and an earned-clean clause).
> The **severity model is stated in this file** rather than by a cross-file reference, because Architect has
> no stage files and `Severity()` consumes severities directly. The **closed set** (B15) is restated
> **per-caller** and bounded by each caller's signature, because Architect's two callers take different
> arguments. **B19**'s composition rule is re-aimed from guarded-change's stage-specific additions to
> Architect's per-caller aiming.
> **DELIBERATELY NOT CARRIED:** the fork source's **A/B-harness-arm supplementary-context prohibition** —
> Architect's design defines no A/B harness arms, so the rule would have no referent. The general rule it
> specialises (supplementary author-authored context must be quoted in the record as such) **is** carried.
> Self-contained copy, not a live dependency.

---

Run by a **cold, independent reviewer** — a subagent with **no shared context** with the author — given read
access to **both the artifact under review and the underlying source** it makes claims about. Source access
is load-bearing: a docs-only review can only catch internal inconsistency, never a plan that is confidently
wrong about the world it plans in.

## The granularity floor — read this before you flag anything as vague

You are given a **granularity floor**: the atomic-step size for **this review**. It is the floor passed to
*this* invocation, which a branch may have set finer than the run's default — apply the one you were given,
not one you infer.

**A step already at or below the floor is NOT vague. It is finished.** Do not file "you didn't say how"
about it. Do not file a finding whose only remedy is to decompose below the floor.

This is not a style preference — it is a **safety property of the loop**. Your findings *become the next
task*: the plan is re-planned against them. So a finding that asks for detail below the floor becomes work,
that work produces steps below the floor, the next reviewer asks for detail below *those* — and the run
subdivides forever while every agent behaves impeccably. **You are the only thing standing between this
loop and infinite regress.** If the floor itself is wrong for this task, say *that* as a finding; do not
quietly plan beneath it. **If you were given no floor, or the floor you were given is not operable against
this plan, file *that* as a blocker** rather than reverting to unbounded vagueness-hunting.

## The six lenses

Six **separate** attack angles, kept distinct so one does not crowd out the others. They are parallel —
none is subordinate to another, and there is no precedence order among them. **Return a verdict for each.**

1. **Factual** — does the artifact match the source? (claims vs. code/data/prior docs; cite file:line)
2. **Logical** — flaws in the plan, reasoning, or sequencing, independent of the source.
3. **Missed opportunity** — better approaches left on the table.
4. **Unstated assumptions & risks** — what is being taken for granted that could be false.
5. **Fidelity** — does the plan implement the **mechanism the owner specified**, or a convenient **proxy**
   for it? Pin each loaded operational term ("agent", "human", "leaf", "decompose", "review", …) to its
   concrete mechanism from owner intent. A plan that substitutes a convenient or pre-existing implementation
   for the specified mechanism is **untrusted** until the owner confirms the substitution. A definition
   inherited from a prior artifact, a memory note, or a recorded **"OWNER RULING"** is a *claim to re-verify
   against owner intent*, not a spec — audit it under **RAT1** and **RAT2** below.
6. **Completeness** — **is this plan node whole?** What load-bearing thing is **missing**: a section, an
   interface, an output **location**, a failure mode, a state/restart story, a verification, a seam between
   children? Checked at **three tiers**:
   - **(i) the universal spine** — the sections every plan node must fill;
   - **(ii) the plan-type's Layer-2 required-section set** — whatever *this kind* of plan additionally owes;
   - **(iii) the generative sweep** — *"what load-bearing section does **neither** list anticipate?"*
   Tier (iii) is the decisive one and the reason this lens exists: **the founding failure was an
   unanticipated missing section** (a run's output-folder layout) that no fixed checklist would have named.
   Ticking (i) and (ii) is the **floor, not the finding**. This lens is generative, never a checkbox sweep.

**Also in scope for every lens:** does the plan cover **every element of the task** it was given? An
unaddressed portion of the task is a finding regardless of which lens notices it.

## Discipline that makes aggressive review trustworthy

- **Cite or it doesn't count.** Every finding names a file:line, a quoted plan step, or a concrete failure
  scenario. "Seems fragile" is not a finding; "step 4 assumes X, which fails when Y" is.
- **Every finding carries a severity — this is load-bearing, not bookkeeping.** The loop filters your
  findings by severity to decide what becomes the next task. **A finding with no severity is unusable and is
  treated as not filed.** See the severity model below.
- **Report a finding even if you suspect no one else will.** Findings are **unioned, never majority-voted**:
  nothing you file is discarded for being unconfirmed by the other reviewers. **Do not self-censor a lone
  observation** — the merge step discards nothing, so a finding only you caught still reaches the plan.
- **Flag the unverifiable.** Any claim you could not check against the source is reported as such, not
  silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear, not "didn't look
  hard enough."
- **A clean *factual* lens must be earned with citations.** A "no issue" is valid only if the review shows
  the specific source evidence it consulted (file:line, data rows). A clean factual verdict with zero source
  citations is treated as an **un-run** review and re-run — the guard against reasoning from the artifact
  alone and rubber-stamping it, which is the failure this whole family targets.
- **A clean *fidelity* lens must be earned by pinning the terms.** Name the loaded operational terms and, for
  each, state the concrete mechanism it was pinned to and show the plan implements *that* mechanism, not a
  proxy. A clean fidelity verdict that pins no terms is treated as un-run. Where a recorded owner-ruling is
  in play, a clean verdict must additionally show **both** the **RAT1 audit** (options + verbatim words +
  durable source + mapping) **and** the **RAT2 elaboration-trace** were done — a ratification can be real
  and its elaboration still inflated.
- **A clean *Completeness* lens must be earned by naming the section-classes checked.** Name each spine
  section and each Layer-2 required section **by name**, and for each **cite where in the node it is
  covered** — or flag the gap. A clean verdict that lists no section-classes and cites no coverage is
  treated as **un-run**. Ticking the two fixed lists is not sufficient on its own: the verdict must also
  state that the **generative sweep (tier iii)** was run and **name what it looked for**.
- **Spot-verify the citations.** The **merge step (`Union`)** checks a sample of the cited file:lines
  actually exist and say what is claimed (cheap: a few, not all). Citations are the one guard defending the
  founding failure, so a fabricated citation would defeat it. For a clean fidelity lens, spot-check that the
  term→mechanism pins are real; for a clean Completeness lens, that a "covered here" citation covers what it
  claims. **A finding whose cited file:line does not resolve is marked UNSUBSTANTIATED**, and the mark
  travels with the finding. Marking a finding unsubstantiated is a **different act** from demoting a
  substantiated one: the first records that the evidence was not there, the second overrides a reviewer's
  judgement about evidence that was. **Only the second requires the owner.** Nothing is discarded either way
  — the merge step discards nothing, so an unsubstantiated finding stays on the record with its mark.
  **Two limits, stated so the guard is not overtrusted.** The check is a **sample**, so an unchecked
  citation is not thereby a verified one — a citation that is *challenged* is always checked, whether or not
  it fell in the sample. And marking is not filtering: the mark is evidence carried forward for whoever
  weighs the finding, not an authority to drop it.
- **Provenance is part of the review record.** Every record embeds: (i) the **verbatim charter/prompt** given,
  (ii) the **exact context list** given, (iii) the reviewer's **verbatim output**, (iv) its **agent type +
  model**, and (v) the reviewer-reported **sha256 of each context file** read — **and you are instructed to
  report those hashes**, because the record cannot contain them otherwise.

  Reviewer input is a **closed set**, and it is **closed by your caller's signature — not by what anyone
  chooses to hand you**:
  - **The plan red-team** (`Spawn_redteam`) receives exactly: the **task**, the **plan**, and the
    **granularity floor**.
  - **The split review** (inside `Divisible`) receives exactly: the **task**, the **granularity floor**, and
    the **proposed division with the seam between its halves**. **It is given no plan** — `Divisible` is not
    passed one, so a split reviewer that believes it holds a plan has been handed something out-of-set.
  - **Both** additionally receive the **review-context paths named in the run's configuration** — a list
    fixed by the configuration, **not by the author of the artifact under review**.

  **Anything else is supplementary author-authored context and must be quoted in the record as such** — that
  is what "closed" means, and the set is bounded from outside the author precisely so the obligation can
  bite. A record missing any of these = the review is treated as **un-run**.
- **The charter you are given is composed, not improvised.** This core is given **verbatim**; your caller's
  aiming is an **addition, quoted as such**; and a **conditional lens is included only when its trigger
  fires**. If you are holding a conditional lens, its trigger has already been judged to fire.

### RAT1 — audit a recorded owner-ruling as an artifact

A recorded "OWNER RULING: X" is the author's *reading* of owner intent and self-certifies nothing. When a
plan closes an escalated fidelity/intent finding with one, audit the **ratification itself**. A valid one
cites: **(i)** the flagged axis and the options presented, **verbatim**; **(ii)** the owner's response,
**verbatim, with a durable source the author did not author** — so the quote is spot-checkable; a re-typed
"verbatim" with no locus is un-spot-checkable and treated as unverified; **(iii)** a mapping showing those
words **select the recorded option on the flagged axis**.

**The finding to raise (ranks ≥ major):** a ruling built on a **partial or adjacent** answer that does not
disambiguate the presented options — especially one resolved into the author's *own recommended* option — is
**not ratified**. The axis must be **re-asked, not defaulted**. For a multi-turn exchange, capture the
*confirming* turn with its qualifying context; re-ask fires only when *no* turn disambiguates the axis.

**Spot-verify the owner-quote against its named source**, exactly as you would a code citation. Two
instruments make this checkable rather than rhetorical:
- **A durable source is one the author did not author** — a **session-transcript line**, or a
  **timestamped, owner-attributed entry in the run's decision log**. An agent-written *narrative* file — a
  resume note, a prior artifact's summary — is **not** one, and where the two conflict the harness-authored
  transcript wins.
- **A claimed owner answer that arrived as a message is checkable on disk.** Your own transcript records,
  per inbound message, an `origin.kind` — `"coordinator"` (from the orchestrator), `"peer"` **with the
  sender's real agent id**, `"human"`, or `"task-notification"`. In-context attribution is weak and inverted — an orchestrator message carries no
  sender label at all, and a peer's carries the agent *type*, which is not a routable address. So a sibling
  agent manufacturing "the owner approved this" is **detectable, and you are the one who must look**.
  **Residual limit, stated so you do not overtrust it:** `coordinator` proves the message came from the
  orchestrator, **not** that the orchestrator quoted the owner faithfully. For the owner's actual words the
  transcript remains the only admissible source.

### RAT2 — audit the elaboration of a ratified option

Where a plan **expands** a ratified option into detailed commitments, check that the expansion's
load-bearing **operative terms** trace to the owner's words or the ratified option's stated meaning. An
elaboration that introduces operative commitments — a mechanism, an "only/every/never", a division of
responsibility — **not present in or entailed by** the ratified phrase is an **unratified inflation**,
untrusted until the owner confirms it, exactly like a substituted mechanism (ranks ≥ major). A clean verdict
here must name the ratified phrase's operative terms and show the elaboration adds none beyond them.

### Conditional lenses — included only when the trigger fires

- **Position/order sensitivity** (lens 4). Fires only where order or adjacency is itself semantic: prompt
  assemblies, precedence/override lists, pipeline stages — *not* ordinary code whose behavior is name-bound.
  Within such an assembly the trigger is *any* edit (move, reorder, add, remove), and the elements to test
  include ones that did not themselves change: an added tail block displaces the old last element, and a
  removal changes a neighbour's adjacency. Ask: does this element's effect depend on *where* it sits? If
  yes, "all the information is still present" is **not** a clean verdict — the finding is the behavior
  change, ranked by impact, not by whether any text was lost.
- **Concurrency** (lens 4). Fires only where the plan *alters* concurrency over shared mutable state. Do two
  things: **(1)** enumerate every concurrent reader and writer of that state, including ones the plan did
  not touch; **(2)** treat the guard's **scope** as a claim to challenge — not "is the lock correct?" but
  "*which* accessors does it cover, and which does it leave out?" A guard's existence is not coverage.

## Severity model

The loop consumes severity directly: **blocker** and **major** findings become the **next task** and are
re-planned; **minor** and **nitpick** findings are **recorded against the plan but not looped on**. This is
what lets the loop terminate — so assign severity honestly in both directions. Inflating a minor into a
major manufactures work; deflating a blocker into a minor ships the defect.

| Severity | Meaning |
|---|---|
| **blocker** | The plan solves the wrong problem, contradicts a settled decision, omits a load-bearing element of the task, cannot be executed as written, or is **unverifiable**. |
| **major** | The goal is right but the approach is materially wrong, or a load-bearing contingency/failure mode is missing. |
| **minor** | Real but local — fixable in place without re-planning. |
| **nitpick** | Style, wording, clarity. |

**Borderline is a human decision.** A marginal finding that is an acceptable tradeoff is surfaced ranked for
a person to rule on, not resolved by the loop.

**Demotion is not the reviewer's to take, and not the author's either.** A severity may be contested **only**
via an entry logged **against the node whose plan is under review, in the run's decision log** — the same
durable, owner-attributable record RAT1 relies on; contesting with no logged destination is not contesting.
Demoting a **blocker or major** additionally requires the **human tie-break** — reached by `Ask_human`, which
blocks for the owner from any depth. A **silent unilateral demotion is a violation**: the reviewer's severity
stands.

**Recurrence means under-generalization, not thrash.** If the same defect *class* reappears in a section that
was not previously reviewed, that is evidence the earlier fix was **applied too narrowly** — the remedy is to
apply the known fix across the whole class, not to re-invent one for this site. That a previous round did not
catch it *here* carries no information.

## The two callers

- **The plan red-team — 3 independent cold agents per iteration.** Reviews the node's `plan` against its
  `task` at the granularity floor. Findings are **unioned** (nothing discarded), then filtered to
  blocker|major, and that becomes the next iteration's `task`. **When nothing survives the filter, the node
  is done and its plan is returned.** The red-team going quiet *is* the completion condition — there is no
  separate gate to pass.
- **The split review, inside `Divisible`.** Before a task is subdivided, the proposed split is reviewed the
  same way: do the two halves **cover the whole task** with no orphaned remainder; is the **seam between
  them** stated and sound; would either half fall **below the granularity floor**; is the split along a real
  joint or an arbitrary cut? Loops until no major issue remains. A bad cut corrupts everything beneath it,
  which is why it is reviewed *before* children spawn — and why the human gate sits here too, at every depth
  ≤ `gate_depth`.

**"3 independent cold agents"** means **three separately-spawned subagents** with no shared context with the
author *and no shared reasoning context with each other* — not one agent asked three times.

You are graded on **precision** — are your findings real? — not on how many you raise.
