# 5 — Build mapping (C1 evidence table)

One row per oracle rule ID → the new file(s) it landed in. **Confirms each rule appears in
every file of its oracle governing-stage-set** (the charter exception noted below). This is the
artifact stage 8's C1 check grades: for each row, "landed in" must equal "governing-stage-set"
(mapped to files), and the wording must be present verbatim (reorganization, not rewrite).

**File-map key:** `charter` = `stages/charter.md`; `sN` = `stages/stage-N.md`; `SKILL` =
`SKILL.md` (router); `METH` = `METHODOLOGY.md` (slim reference).

**Charter exception (round-3 S-1 / O-1):** the charter core (CH0–CH7, CH13 + the conditional
position/concurrency lenses CH11/CH12) is NOT written into stage-3.md and stage-6.md; it lives
ONCE in `stages/charter.md`, which both stage files reference. So for CH0–CH7/CH11/CH12/CH13 the
"landed in" is `charter` (+ the reference from s3/s6). CH8/CH9/CH10 are stage-3-only additions
(deliberate asymmetry — present in s3, absent from s6 and from the charter). ST6d is the
stage-6-only addition.

---

## Core principles (CP)

| ID | Governing set (oracle) | Landed in | Match? |
|---|---|---|---|
| CP1 | 3, 6 | s3, s6 | ✓ |
| CP2 | 3, 6 | s3, s6 | ✓ |
| CP3 | 2 | s2 | ✓ |
| CP4 | 1.5, 8 | s1.5, s8 | ✓ |
| CP5 | 1.5, 8 | s1.5, s8 | ✓ |
| CP6 `*` | 1.5, 3, 6, 8 | s1.5, s3, s6, s8 | ✓ (full in s1.5; normative-core-with-charter-pointer in s3/s6/s8 — see JC-1) |
| CP7 `*` | 1.5, 2, 3, 6, 8 | s1.5, s2, s3, s6, s8 | ✓ (full in s1.5/s2; normative-core-with-charter-pointer in s3/s6/s8 — see JC-1) |
| CP8 | 3, 6 | s3, s6 | ✓ |

## Stage-detail duties (ST / FRZ / GATE / BLD)

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| ST0 | 0 | s0 | ✓ |
| ST1 | 1 | s1 | ✓ |
| ST1.5a | 1.5 | s1.5 | ✓ |
| ST1.5b | 1.5, 3 | s1.5, s3 | ✓ |
| ST1.5c | 1.5 | s1.5 | ✓ |
| ST1.5d `*` | 1.5 | s1.5 | ✓ |
| ST1.5e `*` | 1.5 | s1.5 | ✓ |
| FRZ | 4, 8 | s4 (freeze), s8 (verify-unchanged) | ✓ |
| ST2a | 2 | s2 | ✓ |
| ST2b `*` | 2 | s2 | ✓ |
| ST6d | 6 | s6 | ✓ (stage-6-only addition to charter) |
| GATE | 4, 7 | s4, s7 | ✓ |
| BLD | 5 | s5 | ✓ |

## Red-team charter (CH) — governs 3 & 6, one shared copy

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| CH0 | 3, 6 | charter (ref'd by s3, s6) | ✓ |
| CH-L (four lenses) | 3, 6 | charter | ✓ |
| CH1 | 3, 6 | charter | ✓ |
| CH2 | 3, 6 | charter | ✓ |
| CH3 | 3, 6 | charter | ✓ |
| CH4 | 3, 6 | charter | ✓ |
| CH5 | 3, 6 | charter | ✓ |
| CH6 | 3, 6, 8 | charter (for 3/6) + s8 (consumer-duty at stage 8, written in) | ✓ |
| CH7 (provenance) | 3, 6 | charter | ✓ |
| CH8 (coverage) | 3 | s3 | ✓ (stage-3-only; absent from charter & s6 by design) |
| CH9 (label audit) | 3 | s3 | ✓ (stage-3-only) |
| CH10 (clean label-audit) | 3 | s3 | ✓ (stage-3-only) |
| CH11 (position lens) `*` | 3, 6 | charter | ✓ |
| CH12 (concurrency lens) `*` | 3, 6 | charter | ✓ |
| CH13 (graded on precision) | 3, 6 | charter | ✓ |

## Severity model (SEV) — governs the gates

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| SEV1 (table) | 4, 7, 8 | s4, s7, s8 (full table in each) | ✓ |
| SEV2 | 4, 7, 8 | s4, s7, s8 | ✓ |
| SEV3 | 4, 7, 8 | s4, s7, s8 | ✓ |
| SEV4 (iteration cap) | 4, 7, 8 | s4, s7, s8 | ✓ |

## Stage-8 detail (H)

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| H1 (conformance) | 8 | s8 | ✓ |
| H2 (regression) | 8 | s8 | ✓ |
| H3 (position by execution) `*` | 8 | s8 | ✓ |
| H4 (concurrency by interleaving) `*` | 8 | s8 | ✓ |
| H5 (gating verified by execution) | 8 | s8 | ✓ |
| H6 (unreviewed check) | 8 | s8 | ✓ |
| H7 (per-criterion table) | 8 | s8 | ✓ |
| H8 (regression comparable workload) | 2, 8 | s2, s8 | ✓ |

## Config contract + layers (CFG)

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| CFG0 (two layers) | ref | METH ("The two layers") | ✓ |
| CFG1 (config yaml shape) | ref | METH ("The config contract") | ✓ |
| CFG2 (`redteam_context` priority-ordered) | 3, 6 | s3, s6 (operative form) + METH (config-contract statement) | ✓ |
| CFG3 (paths validated; blocks gate 4) | R, 3, 4, 6 | s3, s4, s6 (operative, incl. gate-4 block) + SKILL `## Inputs` (run-start) + METH pointer | ✓ |
| CFG4 (criteria per-change, in spec) | 1.5 | s1.5 | ✓ |
| CFG5 (criteria mandatory; baseline optional) | 1.5, 0 | s1.5, s0 | ✓ |
| CFG6 (absent signal → plan adds instrumentation) | 2 | s2 | ✓ |

## Artifacts + human-in-the-loop (ART / HIL)

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| ART1 (change folder / stage-doc set) | ref | METH ("What a run produces") | ✓ |
| ART2 (review records verbatim) | 3, 6 | s3, s6 | ✓ |
| ART3 (`decisions.md` append-only gate log) | 4, 7, 8 | s4, s7, s8 (+ stage-8 gating-disposition sentence in s8) | ✓ |
| HIL (stop-for-human) | 4, 8, 1.5 | s4, s8, s1.5 (+ SKILL `## Stop-for-human` summary) | ✓ |

## SKILL.md-only content (SK)

| ID | Governing set | Landed in | Match? |
|---|---|---|---|
| SK-IN (inputs: find/validate config; validate reviewer paths; record in decisions.md) | 0, R, 4 | SKILL `## Inputs` (run-start find+validate) + s4 (record-blocks-gate-4 via CFG3) + s0 (baseline input) | ✓ |
| SK-PROC (per-stage procedure summary) | maps to each stage file | each `stages/stage-N.md` "## Procedure" + SKILL router table | ✓ |
| SK-STOP (stop-for-human summary) | 4, 8, 1.5 | SKILL `## Stop-for-human` + s4, s8, s1.5 (co-located with HIL) | ✓ |
| SK-SELF (self-check / dogfooding) | ref / meta | SKILL `## Self-check` + the standing self-check *criteria* preserved in s1.5 (round-3 O-2) | ✓ |

---

## Judgment calls (flagged for the stage-6 reviewer / C1 grader)

- **JC-1 (CP6/CP7 rendering).** CP6 and CP7 (the core *principles*) appear FULL-VERBATIM at their
  authoring/application homes — **s1.5** (where they author criteria) and, for CP7, **s2** (where
  the plan enumerates accessors). At the reviewer/harness stages **s3, s6, s8** they appear as
  their normative core sentence (verbatim opening) plus a pointer to the charter (s3/s6) or to H3/H4
  (s8) for the full lens statement. Rationale: at s3/s6 the reviewer's *operative* lens is the
  charter's CH11/CH12 (present in full); at s8 the operative duty is H3/H4 (present in full,
  verbatim). This keeps every stage load under the C3 line+token caps without dropping any rule's
  meaning. The rule is **present** in every file of its set; the elaboration is not duplicated where
  a fuller sibling rule (CH11/CH12 or H3/H4) already carries it. If a reviewer reads this as
  "reworded," the fix is to inline the full paragraph at s3/s6/s8 — but note that pushes s3 (253) and
  s8 (262) over the 263-line cap; the token budget (≤~4650) has room, the line budget does not.
- **JC-2 (CH10 trailing word).** Source CH10 ends "…the same guard the factual lens already carries
  **above**." The word "above" referred to the factual-lens bullet physically above it in the old
  single-file charter. In the split, the factual lens lives in `charter.md` (a different file), so
  "above" is dropped: "…the factual lens already carries." Meaning preserved; the spatial deixis was
  false after the move.
- **JC-3 (CFG3 split home).** CFG3's "run start" clause (validate at run-start, record in
  `decisions.md`) is stated in SKILL `## Inputs`; the "each reviewer spawn" + "blocks gate 4"
  operative clauses are written full into s3/s4/s6. The METHODOLOGY config-contract keeps a
  short statement + a pointer to the stage files (round-2 A-2: residual restatement in the slim
  METH is a pointer, not a second normative copy).
- **JC-4 (SK-IN at stage 0/4).** The oracle scopes SK-IN to {0, R, 4}. Its run-start find+validate
  content lives in SKILL `## Inputs` (the router, always loaded). Its stage-4 force ("gate 4 cannot
  pass without the recorded validation") is carried by CFG3 in s4. Its stage-0 relevance (config is
  an input to baseline) is implicit in s0's "from config." No separate SK-IN block is duplicated into
  s0/s4 beyond CFG3 — the SKILL router is loaded at every stage, so the inputs rule is always in view.
- **JC-5 (METHODOLOGY length).** METH landed at 193 lines vs the plan's ~160–170 soft target. Every
  section retained is one the plan mandates keeping (Why / loop / two layers / config contract / what
  a run produces / index). METH is NOT in the per-stage hot path (C3), so its length does not affect
  the load budget; the overage is the stage-index table + config-contract pointers added to prevent
  external-reference breakage. Flagged as advisory (C8-adjacent), not a C3 concern.

## Consistency notes (for C5)

- The deliberate **stage-3 ≠ stage-6 charter asymmetry** holds: CH8/CH9/CH10 present in s3, ABSENT
  from s6 and from `charter.md`. ST6d present in s6, absent from s3/charter. This is by design (O-1)
  and must NOT be "corrected."
- SEV1 table byte-identical across s4/s7/s8 (verified). SEV2/SEV3/SEV4 full-verbatim across s4/s7/s8
  (restored to identical after an initial abbreviation in s8). ART3 identical across s4/s7, with s8
  carrying the extra verbatim stage-8 gating-disposition sentence (a faithful extension, not drift).
- H8 body identical between s2 and s8 (verified).
