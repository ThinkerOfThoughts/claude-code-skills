# 8 — Harness (conformance-only; no stage-0 baseline)

Prose-methodology change → no measurable prior metric → **conformance-only** against the 1.5
criteria. Inspection criteria were verified by locating the exact text (cited at stage 6);
C3 is verified by the plan-only replay A/B (execution).

## Per-criterion verification table

| # | Criterion | Gating? | Path exercised | Verified by execution? | Result |
|---|---|---|---|---|---|
| **C1** | Guard in all load-bearing locations | gating | Located each: METHODOLOGY core-principle L63-74, stage-2 L170-176, charter L252-262, stage-1.5 L153-164, stage-8 L315-322; SKILL L46-50 (1.5), L53-55 (2), L61 (3) | yes — text located in the edited files | **PASS** |
| **C2** | Lens requires *enumerate accessors* + *challenge guard scope* | gating | METHODOLOGY L255-258: "**(1) enumerate every concurrent reader and writer** … **(2) treat the guard's scope as a claim to challenge** — not 'is the lock correct?' but 'which accessors does this guard cover, and which does it leave out?'" | yes | **PASS** |
| **C3** | REPLAY A/B — guard *moves the outcome* on the compaction case | gating | Plan-only A/B: 2 control (stock charter) + 2 treatment (+guard), each red-teaming compaction `2-plan.md`, scope-restricted to that file. Plus the documented historical control (real stage-3, full source, stock charter → missed) | yes — 4 fresh cold reviewers run + historical control | **PASS (qualified)** — treatment **2/2** flagged the ingest lock-free lost-update as BLOCKER; control **1/2** (control#2 missed it, rating the plan MAJOR — a would-have-shipped outcome); historical full-source control also missed. Guard moved the missing reviewer's outcome and never hurt. *Limitation:* n=2/arm; one control caught it unaided (the plan is content-rich). Effect = "reliably helps, never hurts," not a slam-dunk. |
| **C4** | Trigger negatively scoped (not ordinary/already-serialized code) | gating | Principle L73-74 "*not* ordinary single-threaded or already-serialized code"; charter L253-254 "fires only where the change *alters* concurrency over shared state — not ordinary … or already-serialized code" | yes | **PASS** |
| **C6** | Live == source for both files | gating | `diff` live vs source, METHODOLOGY.md + SKILL.md | yes — both empty | **PASS** |
| **C5** | No coherence regression | advisory | Stage-6 cold review: concurrency lens is a clean sibling of the position treatment, cross-linked, no duplication/terminology drift | (advisory) | PASS |

## Confound corrected during the harness

C3 **attempt 1** gave all four reviewers a shared system-context note that pre-enumerated the two
writers and the lock's scope — handing them the guard's own work. All four (incl. control) caught
the race → uninformative. Discarded; re-run **plan-only** (attempt 2, table above) so the guard's
"enumerate every writer" mandate could actually differentiate. This self-correction is logged in
`decisions.md` and is itself an instance of *a control must exhibit the phenomenon first* — the
first harness didn't, so it was rebuilt.

## Verdict

All **gating** criteria (C1, C2, C3, C4, C6) **PASS** — C3 qualified (reliably helps, never hurts;
modest sample honestly noted, not overclaimed). Advisory C5 PASS. No stage-0 baseline → no
regression check. **Stage-8 result: CLEAN → done.** The C3 modesty note is carried to
`decisions.md` as a stated limitation, not a silent pass.
