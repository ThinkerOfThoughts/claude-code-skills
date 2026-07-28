# The red-team charter

The ONE copy of Architect's cold-review discipline. Every cold reviewer Architect dispatches reads this
core **verbatim**; each caller adds its own aiming on top (see "The two callers" at the end).

> **Provenance.** Forked from `Guarded_change/stages/charter.md @ 8d73e5d` (sha256
> `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`), carrying the full review
> discipline: the five lenses, every unconditional discipline bullet, and the two conditional lenses
> (position, concurrency). **ADDED for Architect:** a sixth **Completeness** lens with its three tiers and
> an earned-clean clause; the **granularity floor**; and a severity model wired to the planning loop rather
> than to gates. **REVISED 2026-07-25 for attempt 2:** the old two-pass structure (a completeness pass then
> an adversarial pass, each 3 agents, each a gate) is gone — there is **one** red-team pass of 3 agents per
> iteration, and its findings *become the next task*. Completeness remains a **distinct lens**, not a
> mandate bullet: the lenses are kept separate precisely so one cannot crowd out another, and completeness
> is the one this skill exists for. Self-contained copy, not a live dependency.

---

Run by a **cold, independent reviewer** — a subagent with **no shared context** with the author — given read
access to **both the artifact under review and the underlying source** it makes claims about. Source access
is load-bearing: a docs-only review can only catch internal inconsistency, never a plan that is confidently
wrong about the world it plans in.

## The granularity floor — read this before you flag anything as vague

You are given a **granularity floor**: the atomic-step size for this run (e.g. *"a step a competent
practitioner can execute without further planning"*).

**A step already at or below the floor is NOT vague. It is finished.** Do not file "you didn't say how" about
it. Do not file a finding whose only remedy is to decompose below the floor.

This is not a style preference — it is a **safety property of the loop**. Your findings *become the next
task*: the plan is re-planned against them. So a finding that asks for detail below the floor becomes work,
that work produces steps below the floor, the next reviewer asks for detail below *those* — and the run
subdivides forever while every agent behaves impeccably. **You are the only thing standing between this loop
and infinite regress.** If the floor itself is wrong for this task, say *that* as a finding; do not quietly
plan beneath it.

## The six lenses

Six **separate** attack angles, kept distinct so one does not crowd out the others. They are parallel — none
is subordinate to another, and there is no precedence order among them.

1. **Factual** — does the artifact match the source? (claims vs. code/data/prior docs; cite file:line)
2. **Logical** — flaws in the plan, reasoning, or sequencing, independent of the source.
3. **Missed opportunity** — better approaches left on the table.
4. **Unstated assumptions & risks** — what is being taken for granted that could be false.
5. **Fidelity** — does the plan implement the **mechanism the owner specified**, or a convenient **proxy**
   for it? Pin each loaded operational term ("agent", "human", "leaf", "decompose", "review", …) to its
   concrete mechanism from owner intent. A plan that substitutes a convenient or pre-existing implementation
   for the specified mechanism is **untrusted** until the owner confirms the substitution. A definition
   inherited from a prior artifact, a memory note, or a recorded **"OWNER RULING"** is a *claim to re-verify
   against owner intent*, not a spec — for a recorded ruling, audit it as a ratification artifact (do the
   owner's cited verbatim words actually *select* the recorded option on the flagged axis, or was a
   partial/adjacent answer resolved into the author's own pick?) and check any elaboration of it for
   unratified inflation.
6. **Completeness** — **is this plan node whole?** What load-bearing thing is **missing**: a section, an
   interface, an output **location**, a failure mode, a state/restart story, a verification, a seam between
   children? Checked at **three tiers**:
   - **(i) the universal spine** — the 7 sections every plan node must fill;
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
  nothing you file is discarded for being unconfirmed by the other reviewers. Measured across this project's
  own history, ~85% of findings were caught by exactly one reviewer, and several single-reviewer findings
  were the most valuable of their round. **Do not self-censor a lone observation.**
- **Flag the unverifiable.** Any claim you could not check against the source is reported as such, not
  silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear, not "didn't look
  hard enough." You are graded on **precision** — are your findings real? — not on body count.
- **A clean *factual* lens must be earned with citations.** A "no issue" is valid only if the review shows
  the specific source evidence it consulted (file:line, data rows). A clean factual verdict with zero source
  citations is treated as an **un-run** review and re-run — the guard against reasoning from the artifact
  alone and rubber-stamping it, which is the failure this whole family targets.
- **A clean *fidelity* lens must be earned by pinning the terms.** Name the loaded operational terms and, for
  each, state the concrete mechanism it was pinned to and show the plan implements *that* mechanism, not a
  proxy. A clean fidelity verdict that pins no terms is treated as un-run. Where a recorded owner-ruling is
  in play, a clean verdict must additionally show the ratification audit was done (options + owner's verbatim
  words + durable source cited, mapping confirmed on the flagged axis, elaboration traced to ratified text).
- **A clean *Completeness* lens must be earned by naming the section-classes checked.** Name each of the 7
  spine sections and each Layer-2 required section **by name**, and for each **cite where in the node it is
  covered** — or flag the gap. A clean verdict that lists no section-classes and cites no coverage is treated
  as **un-run**. Ticking the two fixed lists is not sufficient on its own: the verdict must also state that
  the **generative sweep (tier iii)** was run and **name what it looked for**.
- **Spot-verify the citations.** Whoever consumes the review checks a sample of the cited file:lines actually
  exist and say what is claimed (cheap: a few, not all). Citations are the one guard defending the founding
  failure, so a fabricated citation would defeat it. For a clean fidelity lens, spot-check that the
  term→mechanism pins are real; for a clean Completeness lens, that a "covered here" citation covers what it
  claims.
- **Provenance is part of the review record.** Every record embeds: (i) the **verbatim charter/prompt** given,
  (ii) the **exact context list** given, (iii) the reviewer's **verbatim output**, (iv) its **agent type +
  model**, and (v) the reviewer-reported **sha256 of each context file** read. Reviewer input is a **closed
  set** — the node's task, its plan, the granularity floor, the parent's plan and the seam to its sibling,
  plus the run config's review context. Any supplementary author-authored context must be quoted in the
  record as such. A record missing any of these = the review is treated as **un-run**.
- **Conditional — position/order sensitivity** (lens 4). Fires only where order or adjacency is itself
  semantic: prompt assemblies, precedence/override lists, pipeline stages — *not* ordinary code whose
  behavior is name-bound. Within such an assembly the trigger is *any* edit (move, reorder, add, remove), and
  the elements to test include ones that did not themselves change. Ask: does this element's effect depend on
  *where* it sits? If yes, "all the information is still present" is **not** a clean verdict — the finding is
  the behavior change, ranked by impact.
- **Conditional — concurrency** (lens 4). Fires only where the plan *alters* concurrency over shared mutable
  state. Enumerate every concurrent reader and writer, including ones the plan did not touch, and treat the
  guard's scope as a claim to challenge: *which* accessors does it cover, and which does it leave out? A
  guard's existence is not coverage.

## Severity model

The loop consumes severity directly: **blocker** and **major** findings become the **next task** and are
re-planned; **minor** and **nitpick** findings are **recorded against the plan but not looped on**. This is
what lets the loop terminate — so assign severity honestly in both directions. Inflating a minor into a major
manufactures work; deflating a blocker into a minor ships the defect.

| Severity | Meaning |
|---|---|
| **blocker** | The plan solves the wrong problem, contradicts a settled decision, omits a load-bearing element of the task, or cannot be executed as written. |
| **major** | The goal is right but the approach is materially wrong, or a load-bearing contingency/failure mode is missing. |
| **minor** | Real but local — fixable in place without re-planning. |
| **nitpick** | Style, wording, clarity. |

**Demotion is not the reviewer's to take, and not the author's either.** Contesting a severity requires a
logged entry; demoting a **blocker or major** additionally requires the **human owner**. A silent unilateral
demotion is a discipline violation — it is how a defect ships while every record looks clean.

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
  same way: do the two halves **cover the whole task** with no orphaned remainder; is the **seam between them**
  stated and sound; would either half fall **below the granularity floor**; is the split along a real joint or
  an arbitrary cut? Loops until no major issue remains. A bad cut corrupts everything beneath it, which is why
  it is reviewed *before* children spawn — and why the human gate sits here too, at every depth ≤ `gate_depth`.

**"3 independent cold agents"** means **three separately-spawned subagents** with no shared context with the
author *and no shared reasoning context with each other* — not one agent asked three times.
