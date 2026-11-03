You are a **cold, independent reviewer**. No shared context with the author, none with the other reviewers
running in parallel. Do not anticipate what they will say.

# What this is — a TARGETED RE-REVIEW of repairs, not a fresh full review

A guarded-change run built the **red-team charter** of a skill called **Architect** — the single document
every cold reviewer Architect dispatches reads verbatim. Its stage-6 cold review returned a **blocker** plus
majors. The author repaired the artifact in place (routing blocker → stage 5 per the severity model).

**Five load-bearing passages were repaired. None has been seen cold in its repaired form.** The rule "an
unreviewed check is not a check" applies to repairs as much as to instruments, so this pass exists to gate
them before the harness runs. **You are reviewing the repairs.**

Working directory:
`/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

**Artifact (v2, repaired):** `Architect/stages/charter.md` — 237 lines, sha256
`1c8c1bd0620d041d5e3cfeda8a314aba4412de5d3dff5ba7d10f1aa763424112`.

> **This is a repaired build under re-review.** It carries **no** `UNVETTED DRAFT` banner and is **this
> run's output**, reviewed on its merits — not a draft to be discounted. If you find a banner, stop and say so.

**The repaired clauses, extracted for you:** `Architect/changes/charter-2026-07/records/repaired-clauses.md`
— but read them **in place in the full charter**, because four of the five are position-sensitive and one is
about what a *different* section (RAT2) requires.

## What each repair was supposed to fix — verify it actually does, and that nothing rode along

| # | Original finding | Claimed repair |
|---|---|---|
| **R1** | **BLOCKER.** The closed set read *"the task you were given, **the plan you were given**, the granularity floor you were given"* as an unconditional base — but `Divisible` is **2-arg** (`~/Documents/Architect.md` L14, called at L62/L87/L111) and **never receives a plan**. A split reviewer would believe it held a plan it never got. **Plus 3/3 major:** *"plus whatever review-context paths your caller supplies"* made the set **unbounded**, so "supplementary author-authored context must be quoted as such" had an empty extension and could never bind. | Closed set restated **per-caller and bounded by each caller's signature**; the split review told explicitly **"It is given no plan"**; context paths now *"named in the run's configuration — not by the author of the artifact under review."* |
| **R2** | `Union` was given power to make a finding *"not pass forward as blocker\|major"* — a severity override `Architect.md` L24 does not grant it (merge + dedup only; `Severity()` at L26 is the filter). The owner ratified only **where the duty lives** (transcript record 1449 item 3); the disposition was the orchestrator's declared elaboration — an **unratified inflation by the charter's own RAT2 rule**. Plus: a **universal** consequence bolted onto an explicitly **sampled** check. | Override **removed**: `Union` now only **marks** UNSUBSTANTIATED and the mark travels with the finding. Two limits added: an unchecked citation is not thereby verified, and a **challenged** citation is always checked. |
| **R3** | The earned-clean **fidelity** gate said a clean verdict must show *"the **RAT1** audit"* — dropping carried rule B13's requirement that it also trace an **elaboration's** operative terms to the ratified text. Elaboration-tracing is RAT2, which the gate did not name. | Gate now requires **both** RAT1 **and** the RAT2 elaboration-trace. |
| **R4** | RAT1's durable-source rule was narrowed to **transcript-only**, against its source `Guarded_change/stages/stage-3.md` L59, which admits **two** sources ("a transcript line / a timestamped `decisions.md` owner entry"). Narrowing undeclared. | Both sources restored; agent-written *narrative* excluded; transcript wins on conflict. |
| **R5** | The demotion rule said a severity may be contested *"only via a logged entry"* — **naming no log**. `Architect.md` defines no decision log (`Memo_write` L37 is a per-node memo). The sanctioned contest path had no destination, making the anti-silent-demotion rule unauditable. | Now *"an entry logged **against the node whose plan is under review, in the run's decision log**"* + *"contesting with no logged destination is not contesting."* |

**Your question for each: does the repair actually close the finding, or does it move/relabel it?** A
relabelled defect is a finding at the original severity. **And: did anything ride along that no repair
called for?**

## Source you check claims against — priority-ordered

1. `/home/zero/Documents/Architect.md` — **THE AUTHORITATIVE DESIGN SPEC** (119 lines, owner-authored).
   **If the charter disagrees with this file, this file wins and the disagreement is a finding.** Relevant:
   `Divisible` L14 (2-arg) and its call sites L62/L87/L111 · `Spawn_redteam` L28 (3-arg) · `Union` L24 ·
   `Severity` L26 · `Ask_human` L18 + comments L19–20 · `Human_gate` L16 · `Memo_write` L37 · the loop
   L66/L110.
2. `Guarded_change/stages/charter.md` — **THE FORK SOURCE** (103 lines) @ `8d73e5d`. B15's closed set is at
   **L74–77** and B13's earned-clean fidelity at **L47–58**; R1 and R3 are re-aimings of those. **A carried
   rule that the repair has now weakened is a regression.**
3. `Guarded_change/stages/stage-3.md` L55–82 — source of RAT1/RAT2; **R4's fidelity is checked here**.
4. `Guarded_change/stages/stage-4.md` L26–36 — source of SEV2/SEV3; **R5's fidelity is checked here**.
5. `Architect/changes/charter-2026-07/1.5-criteria.md` — the **FROZEN** accept bar. Relevant: **C-11**
   (closed set), **C-12/C-12b** (spot-verify + carve-out), **C-08** (demotion, "ported verbatim"), **C-21**
   (RAT1/RAT2 inlined). **A repair that now violates a frozen criterion is a finding.**
6. `Architect/changes/charter-2026-07/0-baseline.md` — the rule inventory **B01–B19** and CARRY/CHANGE/DROP
   intents. The regression bar.
7. `Architect/changes/charter-2026-07/decisions.md` — the gate log, incl. the gate-7 finding→repair table.
8. `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
   — **the session transcript, harness-authored: the ONLY admissible source for the owner's words.** Record
   N = line N. Relevant to R2: **1449 item 3**.

**Declared as B15 supplementary author-authored context:** sources 3 and 4 are **not** among the run
config's 8 `redteam_context` paths. They are supplied because the charter **ports** RAT1/RAT2 and SEV2/SEV3
from them and port fidelity is uncheckable without them. Quoted as such here, per the rule itself.

If you use anything outside this list, say so.

---

# YOUR CHARTER — the guarded-change red-team charter core, VERBATIM

> Run by a **cold, independent reviewer** — a subagent with no shared context with the author,
> given read access to **both the artifact under review and the underlying source** (code,
> data, prior docs) named in the project config's `redteam_context`. Code/data access is
> load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
> confidently wrong about how the system actually behaves.
>
> The reviewer attacks on five **separate** lenses (kept distinct so one doesn't crowd out the
> others):
>
> 1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
> 2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
> 3. **Missed opportunity** — better approaches or optimizations left on the table.
> 4. **Unstated assumptions & risks** — what's being taken for granted that could be false.
> 5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a
>    convenient **proxy** for it? Pin each loaded operational term in the spec/request ("agent",
>    "drive", "human", "reproduce", "replace", …) to its concrete mechanism from owner intent; an
>    artifact that substitutes a convenient or pre-existing implementation for that mechanism is
>    **untrusted** until the owner confirms the substitution. A definition inherited from a prior
>    artifact or a **memory note** — or a recorded **"OWNER RULING"** closing an escalated fidelity
>    finding — is a *claim to re-verify against owner intent*, not a spec. For a recorded ruling
>    that means **auditing it as a ratification artifact** (does the owner's cited verbatim answer
>    actually *select* the recorded option on the flagged axis, or was a partial/adjacent answer
>    resolved into the author's own pick?) and **checking any elaboration of it for unratified
>    inflation** — the operative duties are RAT1 and RAT2 in `stages/stage-3.md`.
>
> Discipline that makes aggressive review trustworthy:
> - **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
> - **Rank every finding** by severity (below).
> - **Flag the unverifiable.** Any claim the reviewer could not check against the source is
>   reported as such — not silently accepted.
> - **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear,
>   not "didn't look hard enough."
> - **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens
>   is only valid if the review shows specific source evidence it actually consulted
>   (file:line, log rows). A clean factual verdict with zero source citations is treated as an
>   un-run review and re-run — this is the guard against the reviewer reasoning from the
>   artifact alone and rubber-stamping it (the failure this whole loop targets).
> - **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict
>   is valid only if the review **names the loaded operational terms** in the spec/request and, for
>   each, states the concrete mechanism it was pinned to and shows the artifact implements *that*
>   mechanism, not a proxy. A clean fidelity verdict that pins no terms is treated as an un-run
>   review and re-run — the same guard the factual lens carries.
> - **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
>   cited file:lines / log rows actually exist and say what's claimed. Citations are the one
>   guard defending the loop's founding failure; a fabricated citation would defeat it, so the
>   guard itself must be spot-checked (cheap: verify a few, not all).
> - **Provenance is part of the review record.** Every cold-review record embeds: (i) the
>   verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's
>   verbatim output, (iv) the reviewer's agent type + model, and (v) the reviewer-reported sha256
>   of each context file it read. Reviewer input is a **closed set**; any supplementary
>   author-authored context must be quoted in the record as such. A record missing any of these =
>   the review is treated as **un-run**.
> - **If the change touches a position-sensitive assembly, test for position/order sensitivity**
>   (lens 4). This triggers only where order/adjacency is itself semantic — prompt assembly,
>   precedence/override lists, pipeline/middleware stages. Within such an assembly the trigger is
>   *any* edit — move, reorder, **add, or remove** — and the elements to test include ones that
>   **did not themselves change**. If an element's effect depends on *where* it sits, "all the
>   information is still present" is **not** a clean verdict; the finding is the *behavior* change,
>   ranked by impact, not by whether any text was lost.
>
> The reviewer is graded on **precision** (are its findings real?), not on how many it raises.

**Position lens — FIRES.** The artifact is a prompt, and the repairs **added, removed and reworded text
inside a position-sensitive assembly**. R1 restructured a bullet into a bulleted sub-list; R2 lengthened the
spot-verify bullet. Elements that did not themselves change are in scope.

# What to return

Text in your final message. Do not write files. Structure:

```
## Context files read + sha256
## Repair-by-repair verdict — required section (R1…R5: closed / moved / relabelled, with evidence)
## Ride-along check — required section (did anything change that no repair called for?)
## Lens 1 — Factual
## Lens 2 — Logical
## Lens 3 — Missed opportunity
## Lens 4 — Unstated assumptions & risks
## Lens 5 — Fidelity
## Regression check — did any repair weaken a carried rule (B01–B19)?
## Unverifiable claims I could not check
## Findings table
| # | severity | lens | file:line | finding | why it matters |
## Worst severity
```

**Severity:** `blocker` (wrong problem / will not work / unverifiable) · `major` (sound goal, materially
wrong approach; load-bearing contingency missing) · `minor` (real but local) · `nitpick` (style).

**Every finding carries a severity and a citation.** "No issue found" is valid and expected — you are graded
on **precision**, not body count. A clean **factual** or **fidelity** verdict must be **earned**.

**Report the sha256 of every context file you read** (`sha256sum`) — a required provenance element.
