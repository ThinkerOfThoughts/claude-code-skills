# 6-redteam-code.md — stage-6 cold review of the BUILT restructure (verdict: MINOR → gate 7 clears)

## Provenance
- **Reviewer:** cold subagent, `general-purpose`, model `claude-opus-4-8`, no shared context.
- **Run:** 2026-07-06, task `abff1ac30f0a94672`; ~7.7 min, 38 tool uses, ~113K tokens.
- **Reviewed:** the BUILT working-tree files (SKILL router 73, METHODOLOGY slim 193,
  `stages/charter.md` 78, `stages/stage-{0..8}.md`) vs the ORIGINAL source at git `999e056`
  (METHODOLOGY 534, SKILL 124) and the frozen {criteria, plan, oracle} (hashes verified ==
  the gate-4 record). Mechanical diff base `999e056`.
- **Verdict:** MINOR (F-1) + 1 nitpick. No blocker, no major. **Behavior-preserving at the
  operative level.** Route: fix-in-place F-1 → gate 7. (F-1 fixed; see below.)

## Charter (verbatim summary)
Stage-6 cold review of a BUILT position-sensitive prompt restructure. Tasks: C1 rule
preservation & scoping (sample across all rule categories; verbatim vs the 999e056 source;
the 3≠6 charter asymmetry; the shared-charter setup); adjudicate build judgment calls
JC-1..JC-5; C3 budget recompute vs 263-line cap; C5 cross-file consistency; C6 router
correctness; the mandatory POSITION lens (did any rule's effect change by relocation; is each
stage self-contained). Cite file:line (or git show source:line); rank; route by severity.
Full charter in task transcript `abff1ac30f0a94672`.

## Reviewer output (verbatim key findings)
- **Frozen-spec hashes verified** == gate-4 (criteria 11dcf7ad…, plan 9b86654d…, oracle 3e7b1bb4…).
- **C1 (sample table, source-vs-built):** CP1,CP2,CP8,ST1,ST1.5b,FRZ,CH8,CH9/CH10,charter
  core CH0–CH7/CH11–CH13,ST6d,SEV1,SEV2/3/4,H1–H8,CFG3,ART3,HIL — all landed in every file of
  their governing-stage-set, **verbatim**. "charter.md is **byte-identical to the source
  charter core** (206-250 & 275-298)." The **3≠6 asymmetry holds in both directions**
  (CH8/CH9/CH10 in stage-3 only; ST6d in stage-6 only; charter has neither). SEV1 table
  **byte-identical across s4/s7/s8 and to source**. HIL **correctly NOT at stage 7** (round-3
  F2 fix held). **No rule dropped, mis-scoped, or orphaned** — except F-1.
- **JC adjudications:** JC-1 abbreviation pattern **ACCEPTED** as behavior-preserving (the
  operative lens at 3/6 is charter CH11/CH12 full; at 8 is H3/H4 full) — BUT it exposed F-1
  (the "full home" the pointer names was itself missing clauses). JC-2 (CH10 "above" dropped)
  ACCEPTED (removes a now-false spatial pointer). JC-3/JC-4/JC-5 ACCEPTED, no defect.
- **C3 budget (recomputed):** all stages ≤263 — max stage-8 = 262 (1-line margin), stage-3 =
  253, stage-1.5 = 202. No stage over cap. (SKILL landed 73 vs the plan's ~110 assumption →
  extra headroom.)
- **C5:** SEV table / SEV2-4 / ART3 / H8 / CFG3 / ST1.5b all consistent across their files;
  charter one copy; METHODOLOGY residuals are pointers, no contradictory normative copy.
- **C6:** all 10 stages have a router row to an existing file; 3/6 point at their file +
  charter.md; exactly 10 rows.
- **Position lens:** no scenario found where an agent reading {router + stage file [+charter]}
  would execute a stage incorrectly; gate files self-contained (full SEV table written in);
  CH10 "above" correctly handled. The only position-induced gap is F-1's broken pointer
  (rationale layer, not trigger/instruction).
- **F-1 [MINOR]:** CP6 illustrative example (source 59-60) + CP7 cross-reference sentence
  (source 69-71) dropped from EVERY built file (grep-confirmed); the build-mapping's "full in
  s1.5/s2" claim was inaccurate. Operative trigger + instruction survive verbatim; the dropped
  clauses are the rationale/cross-ref layer. Fix at the authoring homes (s1.5, s2), NOT s8
  (would breach cap). **[FIXED post-review: CP6 example + CP7 sentence restored verbatim in
  stage-1.5.md; CP7 sentence restored in stage-2.md. Grep-confirmed present; loads s1.5=207,
  s2=134, s8 untouched=262 — all ≤263.]**
- **N-1 [NITPICK]:** mixed ID-tag delimiter (`(H8)` vs `— H8`); cosmetic, not fixed.

## Verdict — worst severity: MINOR (F-1, fixed in place; N-1 nitpick logged). Gate 7 CLEARS.
