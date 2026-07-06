# The red-team charter (shared by stages 1, 4, 7)

Dragonfly's own cold-review charter — the four lenses, the discipline that makes aggressive review
trustworthy, the diagnosis-specific aiming, the provenance record, and the severity model. Stages 1
and 4 reach it via the diagnostic-artifact triage (the guarded-change/lite pass each repro/test is
routed through *is* its cold review); stage 7 spawns a cold reviewer directly for the causal chain.

> **Provenance:** forked from `Guarded_change/stages/charter.md @ 3d6889b` — the **unconditional core
> only.** Guarded-change's conditional *position* and *concurrency* lenses, its A/B-harness
> supplementary-context clause, and its "reviewer-input-is-a-closed-set" rule are **deliberately not
> carried** (they are not part of dragonfly's current review discipline). This is a self-contained
> copy, not a live dependency: dragonfly no longer tracks guarded-change's future charter edits.

---

Run by a **cold, independent reviewer** — a subagent with **no shared context** with the author, given
read access to **both the artifact under review and the underlying source** (code, logs, prior docs)
named in the project config's `redteam_context`. Source access is load-bearing: a docs-only review can
only catch internal inconsistency, never a claim that is confidently wrong about how the system behaves.

The reviewer attacks on four **separate** lenses (kept distinct so one doesn't crowd out the others):

1. **Factual** — does the artifact match the source? (claims vs. code/logs; cite line/file)
2. **Logical** — flaws in the reasoning/sequencing, independent of the code.
3. **Missed opportunity** — better approaches or tests left on the table.
4. **Unstated assumptions & risks** — what's being taken for granted that could be false.

Discipline that makes aggressive review trustworthy:
- **Cite or it doesn't count.** Each finding names a line/file / log row or a concrete failure scenario.
- **Rank every finding** by severity (below).
- **Flag the unverifiable.** Any claim the reviewer could not check against the source is reported as
  such — not silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear.
- **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens is valid
  only if the review shows the specific source evidence it consulted (file:line, log rows). A clean
  factual verdict with zero source citations is treated as an **un-run** review and re-run — the guard
  against reasoning from the artifact alone and rubber-stamping it.
- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the cited
  file:lines / log rows actually exist and say what's claimed (cheap: verify a few, not all). Citations
  are the one guard defending the loop's founding failure; a fabricated citation would defeat it.
- **The reviewer is graded on precision** (are its findings real?), not on how many it raises.

## Diagnosis-specific aiming

The cold pass is aimed at the failure modes a hunt produces:
- **Does the test reproduce the named symptom (`S#`), or a neighbor?** (the representativeness
  challenge — the #1 failure)
- **Are any identifiers, paths, or calls confabulated?** (the variable-that-doesn't-exist failure)
- **Does the causal chain actually follow from the cited evidence**, or is it asserted? (stage 7)
- **Root or relay — is the claimed root the deepest node the project can act on?** (stage 7)
- **What assumption does the live hypothesis set share, and is it true?** (aimed at the whole set)

## Provenance (part of the review record — unconditional)

Every cold pass — direct stage-7 AND the triage's guarded-change/lite passes at stages 1/4 — records:
(i) the **verbatim charter/prompt** given, (ii) the **exact context path list** given, (iii) the
reviewer's **verbatim output** (the author's summary lives in `decisions.md`, separately), (iv) the
reviewer's **agent type + model**, and (v) the reviewer-reported **sha256 of each context file** it
read. It lives in, or is pointed to from, the hunt folder (a full-guarded-change triage keeps its own
`changes/<slug>/` record, nested or external, pointed to from the hunt's `decisions.md`). **Missing any
element = the pass is un-run** — its reading may not be consumed.

**This charter IS dragonfly's complete unconditional review discipline** — the fork carries the full
set, not a subset. **The coverage-challenge does NOT apply** to dragonfly's *direct* stage-7 pass or a
*lite* pass (neither is a stage-3 review; the analog is the shared-assumption aim above). But a **full
guarded-change triage run keeps ALL of guarded-change's own stage duties, including its stage-3
coverage challenge** — dragonfly narrows nothing inside a full-GC run.

## Severity model and gate routing

Worst finding routes the gate: **blocker** (wrong problem / unverifiable), **major** (sound goal, wrong
approach), **minor** (real but local, fixable in place), **nitpick** (style). Route on the *reviewer's*
stated severity; contest only via a logged `decisions.md` entry, and demoting a blocker/major needs the
human tie-break. **Iteration cap:** after **2 bounces at the same gate on the same finding class**
(regardless of wording), stop and a **human breaks the tie**.
