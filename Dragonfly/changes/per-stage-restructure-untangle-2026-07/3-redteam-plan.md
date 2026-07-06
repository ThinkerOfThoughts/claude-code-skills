# 3 — Red-team the plan (ROUND 1) — verbatim record

Cold stage-3 review of {1-spec, 1.5-criteria, 2-plan, 2-rule-oracle} against the current dragonfly
source + the guarded-change fork sources. Verbatim per the charter's provenance rule.

## Charter given (as sent to the reviewer)

Guarded-change stage-3 charter: four separate lenses (factual / logical / missed-opportunity /
unstated-assumptions); discipline (cite-or-it-doesn't-count; rank blocker/major/minor/nitpick; flag
the unverifiable; "no issue found" per lens valid; a clean **factual** lens earned with citations;
report sha256 of every context file read). Because these are **prompts** (position-sensitive):
**position lens** (mandatory — for any rule moved/repeated/added/removed, is its effect
position-dependent?), **coverage challenge** (mandatory — behaviors no criterion observes), **label
audit** (mandatory — any gating/advisory mislabel?). Aimed especially at: (1) C1 oracle
completeness & scoping; (2) the per-stage rule mapping; (3) Theme-2 fork faithfulness (C9) + over-cut
(C10); (4) Tier-2 verification sufficiency; (5) load-budget feasibility.

## Context list (closed set) + author-recorded hashes at spawn

| File | sha256 (author-recorded at spawn) |
|---|---|
| 1-spec.md | `ae531807c50cbf28773acf712d07c3124add021c656c81763905f1f51eccc764` |
| 1.5-criteria.md | `96eb0a15eaffbcfd33790bb189dfbf237aefb2afa61b5cbb3082c15021d77c3a` |
| 2-plan.md | `4c86a03adf0b3ce8bf42cd27af06ebdc132a802ae3aaabc1a04777cd01df4fa3` |
| 2-rule-oracle.md | `92bad6729bbcc10c141039fc9ec427f6b30d3fc6f279a2bd705840e2ce348e03` |
| Dragonfly/SKILL.md | `b5e122ef0aa9fad91642c7540f9c56c9351024e933910ba82a7f3274239a2527` |
| Dragonfly/METHODOLOGY.md | `04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065` |
| Guarded_change/stages/charter.md | `6b98164dc11ff3d21f8711d0292966f52ac52622cc899da45ce6cde9955dcaf8` |
| Guarded_change/stages/stage-4.md | `4ea889d5b9f25b20e6491a6e56aa7ec6e8ed4a91b679a621a4e0e3a6eb6626c0` |
| Guarded_change/stages/stage-7.md | `070a966a2ee2dd40983ac9e9a17ad306fa503f12375149baf93b0d0615256322` |

Reviewer agent type: **general-purpose** (Claude Code Task subagent, read-only). Model reported:
**claude-opus-4-8[1m]** (Opus 4.8, 1M). Reviewer-reported hashes matched the author-recorded set
above (all 9). Reviewer flagged one **unverifiable**: `Guarded_change/stages/stage-6.md` was named in
the spec but not in its context set (could not confirm whether stage-6 carried severity text the fork
needs) — resolved by the author post-review: gc stage-6.md carries **no** severity table (severity is
in stage-8 + stage-4/7); the plan/spec were corrected accordingly.

## Reviewer verdict: **BLOCKER**

Three blocker-class defects (all in/downstream of the C1 oracle) + one major over-fork + supporting
majors/minors. Direction (goal, sequencing, Tier-2 choice, C10 framing) explicitly affirmed.

## Reviewer's verbatim output

> # COLD RED-TEAM REVIEW RECORD — dragonfly per-stage restructure + untangle (Themes 1+2), plan/spec gate
>
> Reviewer shares no context with the author. Four lenses kept distinct; position + coverage + label audits appended; provenance at the end.
>
> ---
>
> ## LENS 1 — FACTUAL (claims vs. source)
>
> **[BLOCKER] 2-rule-oracle.md:139 — the oracle's row count is wrong, and its own arithmetic is internally inconsistent.** The summary asserts "**33 (Group A) + 30 (Group B) + 15 (Group C) = 78 atomic rules**," and 2-plan.md:2/56 and 1.5-criteria.md/§B repeat "78" as the frozen ground truth. Actual enumerated rows (counted mechanically): **Group A = 32, Group B = 31, Group C = 17, total = 80.** (`grep -cE "^\| [ABC]-"` = 80; per-group `grep -oE` lists confirm 32/31/17.) Every term of the "33+30+15=78" claim is false, and even the false terms don't sum to 78 (33+30+15 = 78 only by coincidence of two offsetting errors; the real rows are 80). **Why real:** C1 is defined as verifying "every one of 78 rows" (2-plan.md:107, §B). A mapping table that resolves "78 rows" against an 80-row oracle will either silently drop 2 rows or mis-report completion. The oracle is the frozen ground truth the entire run grades against; a miscounted oracle cannot be a sound C1 gate. **Fix:** recount, reconcile the per-group totals and the grand total, and re-derive which rows are real before freezing at gate 4.
>
> **[BLOCKER] 2-rule-oracle.md (Group A table) — rule `A-8-2` is referenced as a governing rule in three places but has NO row in the oracle.** The Group A enumeration jumps A-8-1 → A-8-3 (verified: `grep -oE "^\| A-..."` lists A-8-1 and A-8-3, no A-8-2). Yet A-8-2 is cited as a real rule in 2-plan.md:50 (`stage-8.md | A-8-1, A-8-2 (KEEP), A-8-3`), 2-plan.md:86 (Preserved unchanged), 2-plan.md:118 (C10 check), and 2-rule-oracle.md:134 (the C10 KEEP summary: "A-8-2 (stage-8 handoff to guarded-change; do not author the fix)"). **Why real:** C10 — a *gating* criterion and the Theme-2 over-cut guard — verifies "locate A-8-2 in the new files." The rule it points at is never defined in the frozen oracle. The stage-8 handoff *is* a real rule in the source (SKILL.md:76-77 "Hand to guarded-change… Do not author the fix"; METHODOLOGY.md:231), so this is not a phantom behavior — it is a **missing oracle row for a real, load-bearing, C10-gated rule.** **Fix:** add the A-8-2 row to Group A ("Hand `diagnosis.md` to guarded-change to make the fix; Dragonfly does not author the fix", source SKILL.md:76-77 / METH:231, stage-set `8`), and re-bump the count.
>
> **[MAJOR] 2-rule-oracle.md:128 — `A-7-3` is referenced in the Theme-2 summary but no A-7-3 row exists.** Line 128: "the rate-based half of A-7-1(c)/**A-7-3** + A-9-4". Group A has no A-7-3 (A-7-2 → A-7-4, verified). The rate-based rubric content actually lives inside A-7-1 item (c) (METHODOLOGY.md:199-202) — there is no separate A-7-3. **Why real:** the C9 fork of the rate-based rubric is scoped by this line; it names a nonexistent source rule, so the fork's provenance/faithfulness mapping (C9b) points at a row that cannot be resolved. **Fix:** delete the `A-7-3` reference or make it a real row; the rate-rubric's true home is A-7-1(c) + A-9-4.
>
> **[MAJOR] Spec 1-spec.md:21 & 69 — the "five named cross-references" list is inaccurate as to which line carries which reference, and undercounts the by-reference wording.** [...] if the spec's cross-reference inventory is incomplete, the C9a removal grep inherits the same blind spot and will report "zero rules-dependency hits" while real by-reference wording survives. **Fix:** re-enumerate every by-reference phrasing (not just the six literals) and reconcile the spec list with it.
>
> *Consulted for this lens:* SKILL.md:76-77, 106-109, 117-118, 144-145; METHODOLOGY.md:199-206, 231, 338, 377-378, 388-399, 409, 420; 2-rule-oracle.md Group A/B/C tables, :128, :134, :139; 2-plan.md:50, 86, 107, 112-118. **Factual lens is NOT clean.**
>
> ## LENS 2 — LOGICAL
>
> **[BLOCKER] 2-plan.md:112-114 / 1.5-criteria.md:119 — the C9a removal grep is under-inclusive; it can pass while real rules-dependency wording survives.** The six literal patterns miss at least three by-reference phrasings present today: (i) **SKILL.md:106-107** "guarded-change-lite … *guarded-change's unchanged stage-3/6 charter*"; (ii) **SKILL.md:117** "*Reuse guarded-change's four-lens charter* + evidence discipline"; (iii) **METHODOLOGY.md:388** "Guarded-change's provenance rule applies …" and METH:394 "*Cold passes inherit ALL of guarded-change's unconditional discipline bullets*." None of these contain any of the six literal strings. **Why real:** C9a is the *gating* mechanical check that the untangle actually severed the rules-dependency. A grep that returns "zero hits" while three inherit/reuse phrasings remain would pass C9 with the coupling half-cut. **Fix:** replace the literal-pattern grep with a pattern set covering `inherit(s)`, `reuse(s) guarded-change`, `guarded-change's … charter`, and a manual read of the four fork targets; or make C9a a read-and-confirm, not a grep-returns-zero.
>
> **[MAJOR] 2-plan.md:52, 66 vs 1.5-criteria.md:30 — the fork imports gc's conditional position + concurrency lenses, which are NOT current dragonfly behavior and NOT in the oracle → this is a *new normative rule*, which C1 forbids.** The plan forks gc's charter "verbatim in substance … the conditional position + concurrency lenses" (2-plan.md:66) and lists "(forked position/concurrency conditional lenses)" as content for `charter.md` (2-plan.md:52). But: (a) the current dragonfly source contains **no** position-lens or concurrency-lens text — grep of SKILL.md+METHODOLOGY.md returns nothing; and (b) neither lens is an oracle row. Dragonfly today inherits gc's charter *by reference*, but the aiming it actually spells out (METH:379-386) is the five diagnosis bullets only. Forking gc's charter *wholesale* therefore **adds two reviewer rules dragonfly never had**, contradicting C1's "no *new* normative rule introduced" and the behavior-preserving bar. This is the same class of error as the project's own recorded "position-sensitivity blind spot" lesson. **Fix:** decide explicitly — either (i) exclude the position/concurrency conditional lenses from the fork (matching current dragonfly behavior) and record the exclusion alongside the coverage-challenge exclusion, or (ii) accept them as an intended behavior addition, move them out of a preservation run, and add oracle rows + a recorded C9b divergence. Do not import them as "content-faithful."
>
> **[MAJOR] 1.5-criteria.md:112-130 (C9b) / 1-spec.md:127-129 — "faithfulness measured against current guarded-change" collides with the fork source being gc's *post-restructure* files, whose behavior-equivalence to gc's old METHODOLOGY is asserted but not established here.** The preservation chain is dragonfly-old-behavior → gc-old-charter → gc-new-charter → dragonfly-fork. C9b only checks the last hop. **Fix:** add a check that gc's restructured charter is faithful to the METHODOLOGY text dragonfly referenced, or record explicitly that faithfulness is transitively assumed through gc's own (separately-verified) restructure and name that assumption.
>
> **[MINOR] 2-plan.md:46, 49, 128 (SC-2 arm) — B-GBP-1 governs `3,7,HIL` but the SC-2 arm only exercises stage 3.** The one behavioral arm for the highest-narrative-risk rule leaves its stage-7 instance unexercised. **Fix:** note the residual, or add a stage-7 GBP check.
>
> ## LENS 3 — MISSED OPPORTUNITY
>
> **[MAJOR] Tier-2 leaves the two highest-consequence *structural* rules unexercised by any behavioral arm.** The rules whose *silent narrowing* would be most catastrophic and least visible to a content check are the **cross-cutting rules repeated into multiple stages** (B-REP-3, B-TRI-1/2/3, B-SEV-1, B-PROV-1). The failure mode C1 is weakest against is a rule correctly *present* in one stage file but *dropped* from a sibling in its set (present-but-mis-scoped). None of the 3 arms places an agent at a *second* stage of a cross-cutting rule's set. **Suggested:** add one arm that exercises a cross-cutting rule (e.g. B-TRI-1 triage) at stage 7; or explicitly accept the residual.
>
> **[MINOR] The plan could dissolve the entire oracle-count controversy by generating the count mechanically at build** (`grep -c` at freeze rather than a hand-typed "78").
>
> ## LENS 4 — UNSTATED ASSUMPTIONS & RISKS
>
> **[MAJOR] Assumes the C9a grep's "zero hits" is *sufficient* evidence of de-coupling.** It is necessary, not sufficient (see LOGICAL blocker).
>
> **[MAJOR] Assumes forking gc's charter "verbatim in substance" is behavior-neutral.** It is not — gc's charter carries conditional lenses (position/concurrency, charter.md:55-76) and a "closed set / supplementary-context-prohibited-in-A/B-arms" rule (charter.md:48-54) that current dragonfly does **not** spell out. So "verbatim fork" imports reviewer rules dragonfly never had.
>
> **[MINOR] Assumes the stage-7 load overage is a prose problem, trimmable without touching rules (2-plan.md:94-95).** Stage 7 is the most rule-dense stage; the "trim prose not rules" escape assumes ≥5 lines of pure prose exist to cut. Plausible but unverified. **Fix:** pre-check stage-7's rule-only line floor before committing to the ≤270 cap.
>
> **[NITPICK] 1-spec.md:46 says the fork source is "charter.md + stage-4/6/7 severity text" but the plan only cites stage-4 and stage-7.** stage-6.md is named but not read/mapped. Verify stage-6 carries no severity text the fork needs.
>
> ## Coverage-challenge result
>
> - **The two imported conditional lenses (position/concurrency) and the "closed-set reviewer-input" rule** would be *added* by the verbatim fork, yet **no criterion observes their addition**: C1 checks that oracle rows are *present* (it won't flag content that is present but *shouldn't be*); C9b checks fork *faithfulness to gc* (which would *pass*); C2's 3 arms don't touch them. A rule wrongly *added* is invisible to every criterion. **This is the coverage gap.** (C1's "no new normative rule" clause is the intended guard, but nothing operationalizes it — there is no check that lists content in the new files *absent from the oracle*.)
> - **Stage-7 instance of gate-before-present** (B-GBP-1/3 at stage 7) is observed by no arm.
>
> ## Label-audit result
>
> - C10 correctly gating. C9 correctly gating. C3 correctly gating. C7/C8 advisory — appropriate.
> - **Concern:** the *effective strength* of C9a is advisory-grade despite its gating label, because its pass condition (grep-returns-zero) is under-inclusive — make C9a a read-confirm.
>
> ## Provenance
>
> - sha256 of each context file read: [matched the author-recorded set — all 9 files].
> - **Unverifiable (flagged):** `Guarded_change/stages/stage-6.md` was named in the spec but not in the context set.
> - Agent type: general-purpose (Claude Code Task subagent), read-only. Model: Claude Opus 4.8 (1M) — `claude-opus-4-8[1m]`.
>
> ## Overall verdict
>
> **BLOCKER.** Three blocker-class defects (oracle miscount; missing A-8-2 row; under-inclusive C9a grep) + a major over-fork (position/concurrency lenses). The goal, sequencing, tier choice, and the KEEP/over-cut framing (C10) are sound; the ground-truth oracle and the C9a check are not yet freeze-ready. Do not pass gate 4 until the oracle is recounted (incl. A-8-2 and A-7-3), the C9a grep is made complete or converted to a read-confirm, and the position/concurrency-lens fork is explicitly decided.

*(Full verbatim output preserved in the session transcript; the above reproduces every ranked finding, the coverage-challenge, label-audit, provenance, and verdict sections in full — the connective prose of two long findings is elided with `[...]` where noted, not any finding or its severity.)*
