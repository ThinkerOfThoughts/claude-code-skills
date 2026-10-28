# The red-team charter (shared by the completeness-critic pass, the adversarial pass, and guarded-change self-review)

This is the ONE copy of Architect's cold-review charter's common core. Every cold reviewer Architect
dispatches reads it: the **adversarial red-team pass** (stage 4) runs the full six lenses; the
**completeness-critic pass** (stage 3) runs it aimed at the **Completeness lens** as its primary
mandate (skeleton-whole first); and when Architect is run **on its own skill files** (guarded-change
self-review — *guarded-change's* stage 6, not Architect's own stage 6) the reviewer reads it plus the
mechanical-diff duty. Each consuming stage adds its stage-specific aiming; the core below is given to
the reviewer **verbatim**.

> **Provenance.** Forked from `Guarded_change/stages/charter.md @ 8d73e5d` (sha256
> `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`) — the **full review
> discipline**, carried whole: the five lenses (Factual / Logical / Missed-opportunity /
> Unstated-assumptions&risks / Fidelity, incl. the owner-ruling ratification audit), every
> unconditional discipline bullet (cite-or-it-doesn't-count, rank-every-finding, flag-the-unverifiable,
> "no issue" allowed, clean-factual-earned, clean-fidelity-earned, spot-verify-citations, provenance +
> reviewer-input-is-a-closed-set), and the two **conditional** lenses (position, concurrency) — because
> Architect plans arbitrary software and either can fire in a planned artifact's adversarial pass, and
> Architect's *own* skill files are a position-sensitive assembly. **ADDED:** a standing **sixth
> Completeness lens** with an earned-clean clause (below), mirroring the earned-clean factual lens.
> **DROPPED:** nothing from the core. (The A/B-harness supplementary-context prohibition is retained but
> never fires — Architect runs no A/B harness arms.) This is a **self-contained copy, not a live
> dependency**: Architect does not track guarded-change's future charter edits.

---

Run by a **cold, independent reviewer** — a subagent with **no shared context** with the author, given
read access to **both the artifact under review and the underlying source** (code, data, prior docs,
the parent node's plan and sibling seams) named in the run config's `redteam_context`. Source access is
load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
confidently wrong about how the system actually behaves — or a plan that is confidently wrong about the
world it plans in.

The reviewer attacks on **six separate** lenses (kept distinct so one doesn't crowd out the others; the
six are **parallel attack angles with no precedence/override order among them** — none is subordinate to
another):

1. **Factual** — does the artifact match the source? (claims vs. code/data/prior docs; cite line/file)
2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
3. **Missed opportunity** — better approaches or optimizations left on the table.
4. **Unstated assumptions & risks** — what's being taken for granted that could be false.
5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a convenient
   **proxy** for it? Pin each loaded operational term in the spec/request ("agent", "drive", "human",
   "reproduce", "replace", "leaf", "decompose", …) to its concrete mechanism from owner intent; an
   artifact that substitutes a convenient or pre-existing implementation for that mechanism is
   **untrusted** until the owner confirms the substitution. A definition inherited from a prior artifact
   or a **memory note** — or a recorded **"OWNER RULING"** closing an escalated fidelity finding — is a
   *claim to re-verify against owner intent*, not a spec. For a recorded ruling that means **auditing it
   as a ratification artifact** (does the owner's cited verbatim answer actually *select* the recorded
   option on the flagged axis, or was a partial/adjacent answer resolved into the author's own pick?)
   and **checking any elaboration of it for unratified inflation**.
6. **Completeness** *(the Architect sixth lens)* — **is this plan node whole?** What load-bearing thing
   is **missing** — a section, an interface, an output **location** (the founding-failure section), a
   failure mode, a state/restart story, a verification, a between-child seam? Completeness is checked at
   **three tiers**: (i) the **7-section universal spine** (every node must fill each — see METHODOLOGY);
   (ii) the plan-type's **Layer-2 required-section set**; and, decisively, (iii) a **generative**
   sweep — *"what load-bearing section does neither list anticipate?"* — because the founding failure
   was an **unanticipated** missing section that no fixed checklist would have named. This lens is
   **generative, not a checkbox sweep**: ticking tiers (i)–(ii) is the floor, not the finding.

Discipline that makes aggressive review trustworthy:
- **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
- **Rank every finding** by severity (below).
- **Flag the unverifiable.** Any claim the reviewer could not check against the source is reported as
  such — not silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear, not "didn't
  look hard enough."
- **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens is only
  valid if the review shows specific source evidence it actually consulted (file:line, data rows). A
  clean factual verdict with zero source citations is treated as an **un-run** review and re-run — the
  guard against the reviewer reasoning from the artifact alone and rubber-stamping it (the failure this
  whole family targets).
- **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict is
  valid only if the review **names the loaded operational terms** and, for each, states the concrete
  mechanism it was pinned to and shows the artifact implements *that* mechanism, not a proxy. A clean
  fidelity verdict that pins no terms is treated as un-run and re-run. Where a finding carries a recorded
  owner-ruling, a clean fidelity verdict must additionally show the **ratification-record audit** was
  done (options + owner's verbatim words + durable source cited; mapping to the recorded option confirmed
  on the flagged axis; any elaboration traced to the ratified text).
- **A clean *Completeness* lens must be earned by naming the section-classes checked.** A "no gap"
  verdict is valid only if the review **names the section-classes it checked** (at minimum each of the 7
  spine sections and each Layer-2 required section **by name**) and, for each, **cites where in the node
  it is covered** — or flags the gap. A clean Completeness verdict that lists no section-classes and
  cites no coverage is treated as an **un-run** review and re-run — the same guard the factual lens
  carries, aimed at the mechanic this skill most exists to embody. Ticking the two fixed lists is **not**
  a clean verdict on its own: the verdict must also state that the **generative** sweep (tier iii) was
  run — *"what load-bearing section is on neither list?"* — and name what it looked for.
- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the cited
  file:lines actually exist and say what's claimed (cheap: verify a few, not all). Citations are the one
  guard defending the founding failure; a fabricated citation would defeat it. For a clean fidelity lens
  spot-check the term→mechanism pins are real; for a clean Completeness lens spot-check that a named
  "covered here" citation actually covers the section-class it claims.
- **Provenance is part of the review record.** Every cold-review record embeds: (i) the **verbatim
  charter/prompt** given, (ii) the **exact context path list** given, (iii) the reviewer's **verbatim
  output** (the author's summary lives in `decisions.md`, separately), (iv) the reviewer's **agent type +
  model**, and (v) the reviewer-reported **sha256 of each context file** it read. Reviewer input is a
  **closed set**: the node's `plan.md` + its decomposition + child seams, the config's `redteam_context`,
  the parent node's plan, and carried-forward findings from `decisions.md`; any supplementary
  author-authored context must be quoted in the record as such. A record missing any of these = the
  review is treated as **un-run**. (In A/B harness arms, author-authored supplementary context is
  prohibited outright — a leak is a confound; this clause never fires in a normal planning run.)
- **If the artifact under review is a position-sensitive assembly, test for position/order sensitivity**
  (lens 4). This fires only where order/adjacency is itself semantic — prompt assembly,
  precedence/override lists, pipeline/middleware stages — *not* ordinary code whose behavior is
  name- not position-bound. Within such an assembly the trigger is *any* edit — move, reorder, add, or
  remove — and the elements to test include ones that did not themselves change. For each ask: does its
  effect depend on *where* it sits (recency, adjacency, precedence, before/after an input it governs)? If
  yes, "all the information is still present" is **not** a clean verdict; the finding is the *behavior*
  change, ranked by impact.
- **If the plan introduces a new accessor or a new read-modify-write window over shared mutable state,
  map the accessors and challenge the guard's scope** (lens 4). Fires only where the plan *alters*
  concurrency over shared state. Enumerate every concurrent reader and writer (including ones the plan
  did not touch) and treat the guard's scope as a claim to challenge — *which* accessors it covers and
  which it leaves out. A guard's existence is not coverage.

The reviewer is graded on **precision** (are its findings real?), not on how many it raises.

## How the two passes use this charter

- **Completeness-critic pass (stage 3, gate #1) — 3 independent cold agents.** Primary mandate = the
  **Completeness lens** (the three tiers above), *"what's missing here — a section, an interface, an
  output location, a failure mode, a state/restart story, a between-child seam?"*. Runs **first** (is the
  skeleton whole before you try to break it?). The other five lenses are in scope but Completeness leads.
- **Adversarial red-team pass (stage 4, gate #2) — 3 independent cold agents.** Full six lenses, mandate
  = *poke holes* (overlooked items, uncovered contingencies, false assumptions, better approaches left on
  the table). Runs **second** (given it is whole, does it break?).
- **"3 independent cold agents"** means **three separately-spawned subagents**, no shared context with
  the author and no shared reasoning context with each other, **per pass** — not one agent asked three
  times, not a single reviewer. Both passes run at **every node and every altitude** (see COV in
  METHODOLOGY), executed by the **(sub-)orchestrator that owns that node** over its own slice — the top
  orchestrator included on the root plan + the top-level split. A node cannot finalize until **both**
  passes are on record and **clean-or-resolved** (gate-before-present, GBP).

## Severity model and gate routing

Worst finding routes the gate: **blocker** (wrong problem / a settled decision contradicted / a node
unverifiable as planned), **major** (sound goal, materially wrong approach), **minor** (real but local,
fixable in place), **nitpick** (style/clarity). Route on the *reviewer's* stated severity; contest only
via a logged `decisions.md` entry, and demoting a **blocker or major** additionally requires the human
tie-break. A silent unilateral demotion is a gate violation. **Iteration cap (CAP):** after **2 bounces
at the same gate on the same finding class** (same gate + same targeted node section, regardless of
wording), the loop **stops and a human breaks the tie** — under delegation, the runner **halts and
relays the question verbatim** (RAT3).
