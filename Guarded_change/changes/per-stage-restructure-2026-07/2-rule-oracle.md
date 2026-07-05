# 2-rule-oracle.md — the rule → governing-stage map (C1 ground truth)

Independent enumeration of every atomic normative rule in the CURRENT
`Guarded_change/METHODOLOGY.md` (534 lines) + `SKILL.md` (124 lines), each with a
**governing-stage-set** derived from where the rule is active in the loop (the stages it
names / the sections it governs / the gates it blocks) — NOT from the restructure author's
convenience. The build (stage 5) must place each rule in **every** stage file in its set.
C1 (stage 8) grades the built files against this map. Frozen at gate 4.

Legend for stages: `0 1 1.5 2 3 4 5 6 7 8`; `R` = run-start; `ref` = reference material
(orientation / config-contract — opened for setup, not to run a stage); `*` = conditional
(fires only when its trigger is present).

## Core principles (METHODOLOGY:30–77)

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| CP1 | Nothing self-certifies; author never approves; cold independent reviewer | 32–34 | 3, 6 |
| CP2 | Evidence over rhetoric (cite line/file or a concrete scenario) | 35–37 | 3, 6 |
| CP3 | Instrument before you build (measurement/instrumentation is part of the plan) | 38–40 | 2 |
| CP4 | A bar, set first (criteria before implementation; "done" verified not declared) | 41–42 | 1.5, 8 |
| CP5 | A deferred gating criterion is not a met one | 43–48 | 1.5, 8 |
| CP6 | Information-preserving ≠ behavior-preserving (position lens) `*` | 49–62 | 1.5, 3, 6, 8 |
| CP7 | Shared state has more than one accessor (concurrency lens) `*` | 63–74 | 1.5, 2, 3, 6, 8 |
| CP8 | "No issue found" is a valid result (reviewers graded on precision) | 75–76 | 3, 6 |

## Stage-detail duties (METHODOLOGY:108–200)

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| ST0 | Baseline only if a prior version + config baseline exists; else skip + conformance-only | 110–112 | 0 |
| ST1 | Spec = rich problem def; **declares expected touched files** (joins reviewer context) | 114–117 | 1 |
| ST1.5a | Criteria checkable: automated OR human-judged rubric (named judge + scale + pass) | 119–128 | 1.5 |
| ST1.5b | Criteria mandatory (loop won't pass stage 3 without them) | 129–131 | 1.5, 3 |
| ST1.5c | Each criterion labeled gating/advisory; **defaults to gating** (unlabeled = gating) | 133–139 | 1.5 |
| ST1.5d | Position-sensitive change → a behavior-preservation criterion, verified by execution `*` | 141–153 | 1.5 |
| ST1.5e | New shared-state accessor → a no-lost-update criterion, checked by executed interleaving `*` | 155–166 | 1.5 |
| FRZ | Criteria freeze at gate 4 + hash in decisions.md; **stage 8 verifies unchanged**; weakening audited | 168–176 | 4, 8 |
| ST2a | Plan = how + measurement + instrumentation (add to scope if absent) + thresholds | 178–180 | 2 |
| ST2b | Concurrency change → plan enumerates every accessor + which the guard covers `*` | 182–188 | 2 |
| ST6d | Stage-6 reviewed diff generated **mechanically** (`git diff` vs recorded base), command recorded | 191–193 | 6 |
| GATE | Gates route by worst finding's severity | 195 | 4, 7 |
| BLD | Build per the plan (incl. instrumentation the plan added) | 197 | 5 |

## The red-team charter (METHODOLOGY:204–298) — governs 3 & 6

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| CH0 | Cold independent reviewer; read access to artifact AND source (`redteam_context`) | 206–210 | 3, 6 |
| CH-L | Four separate lenses: factual / logical / missed-opportunity / unstated-assumptions | 212–218 | 3, 6 |
| CH1 | Cite or it doesn't count | 221 | 3, 6 |
| CH2 | Rank every finding by severity | 222 | 3, 6 |
| CH3 | Flag the unverifiable | 223–224 | 3, 6 |
| CH4 | "No issue found" per lens allowed and expected | 225–226 | 3, 6 |
| CH5 | A clean **factual** lens must be earned with source citations (else un-run, re-run) | 227–231 | 3, 6 |
| CH6 | Spot-verify a sample of the reviewer's citations (consumer duty) | 232–235 | 3, 6, 8 |
| CH7 | Provenance: verbatim charter + context list + verbatim output + agent/model + hashes | 236–250 | 3, 6 |
| CH8 | Coverage challenge — name behaviors no criterion observes (stage-3 only) | 251–255 | 3 |
| CH9 | Audit criterion labels + the stage-8 verification table (the gating guard) | 256–270 | 3 |
| CH10 | A clean label-audit must be earned (per-criterion path confirmed), else un-run | 271–274 | 3 |
| CH11 | Position lens: test for position/order sensitivity `*` | 275–285 | 3, 6 |
| CH12 | Concurrency lens: map accessors + challenge the guard's scope `*` | 286–296 | 3, 6 |
| CH13 | Reviewer graded on precision, not body count | 298 | 3, 6 |

## Severity model (METHODOLOGY:302–332) — governs the gates

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| SEV1 | Severity table (blocker/major/minor/nitpick) → routing per stage | 304–309 | 4, 7, 8 |
| SEV2 | Borderline/tradeoff is a human decision, surfaced ranked | 311–313 | 4, 7, 8 |
| SEV3 | Route on the **reviewer's** stated severity; demoting blocker/major needs human tie-break | 315–320 | 4, 7, 8 |
| SEV4 | Iteration cap: 2 same-class bounces at a gate → human tie-break; carry findings forward | 322–332 | 4, 7, 8 |

## Stage-8 detail (METHODOLOGY:336–420) — governs 8 (+ noted)

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| H1 | Conformance (always): measured vs criteria | 338–340 | 8 |
| H2 | Regression (only if baseline): measured vs baseline on neighbors | 341–346 | 8 |
| H3 | Position-dependent criteria checked by **execution**, not inspection `*` | 348–354 | 8 |
| H4 | Concurrency criteria checked by **executed interleaving**, not inspection `*` | 356–363 | 8 |
| H5 | Every gating criterion verified by execution — no deferral/proxy/silent-drop; else route (a)/(b) | 365–385 | 8 |
| H6 | An unreviewed check is not a check (new check → targeted cold check before it counts) | 387–395 | 8 |
| H7 | Per-criterion verification table with evidence column; gating PASS w/o evidence = verified-no | 397–410 | 8 |
| H8 | Regression measured on a comparable workload, else advisory (plan names gating vs advisory) | 412–420 | 2, 8 |

## Config contract + layers (METHODOLOGY:424–486) — mostly reference, some stage-active

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| CFG0 | Two layers: agnostic core vs per-project config; "harness" = empirical check vs a bar | 424–434 | ref |
| CFG1 | Config yaml shape (redteam_context / measurement / metrics) | 438–467 | ref |
| CFG2 | `redteam_context` is priority-ordered | 470–472 | 3, 6 |
| **CFG3** | **Paths validated, not assumed** — at run-start + each reviewer spawn; **blocks gate 4** | 473–479 | R, 3, 4, 6 |
| CFG4 | Acceptance criteria are per-change (in the spec), not in the config | 480–481 | 1.5 |
| CFG5 | Criteria mandatory; baseline optional (no baseline → conformance-only) | 482–483 | 1.5, 0 |
| CFG6 | A needed-but-absent signal → the plan adds the instrumentation | 484–485 | 2 |

## Artifacts + human-in-the-loop (METHODOLOGY:489–535)

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| ART1 | One change folder; the stage-doc set | 491–503 | ref |
| ART2 | Review records are **verbatim** (charter + context + raw output); interpretation in decisions.md | 505–508 | 3, 6 |
| **ART3** | **`decisions.md` append-only gate log** — one entry per gate; **iteration cap depends on it**; stage-8 records each gating criterion's disposition | 510–518 | 4, 7, 8 |
| HIL | Stop for human: any blocker (restart); major at stage 8; gating-unverifiable-pre-ship; missing criteria/config | 524–535 | 4, 8, 1.5 |

## SKILL.md-only content (SKILL:1–124)

| ID | Rule | Source | Governing stages |
|---|---|---|---|
| SK-IN | Inputs: find/validate the config; validate every reviewer path; record in decisions.md | SKILL:13–22 | 0, R, 4 |
| SK-PROC | Per-stage procedure summary (0–8) | SKILL:24–107 | (maps to each stage file) |
| SK-STOP | Stop-for-human summary | SKILL:108–113 | 4, 8, 1.5 |
| SK-SELF | Self-check / dogfooding (skill-file edits take the full loop; standing self-check criteria) | SKILL:115–123 | ref / meta |

---

## Rows round 1 specifically corrected (the F1/F2 fixes, made explicit)

- **FRZ** (criteria freeze) → **{4, 8}**, not {4} (round-1 F1 silent narrowing).
- **CFG3** (paths validated) → **{R, 3, 4, 6}**, and it **blocks gate 4** — it must live in the
  stage-3, stage-4, stage-6 files, not an always-on reference bucket (round-1 F2/F4).
- **ART3** (decisions.md gate log) → **{4, 7, 8}**, iteration-cap-critical — in the gate + harness
  files (round-1 F4/P4).
- **H6** (unreviewed-check), **CH6** (spot-verify), **H8** (regression-comparable) → present and
  scoped (round-1 F2 omissions now enumerated).
- **CP4** (a bar, set first) → **{1.5, 8}** (round-1 F3 cross-stage note).

Cross-cutting rules (appear in ≥2 stage files): CP1, CP2, CP4, CP5, CP6`*`, CP7`*`, CP8,
SEV1–SEV4, FRZ, CFG3, ART2, ART3, H8, HIL, SK-STOP — each written **in full** into every file
of its set (owner's "repeat into each stage," not a spine). **EXCEPTION (round-3 S-1): the
charter (CH0–CH13) is NOT repeated** — it lives once in the shared `stages/charter.md` that
stage-3.md and stage-6.md reference (per the O-1 build-note above); stage-3 adds CH8/CH9/CH10,
stage-6 adds ST6d. The build must place the charter as a shared reference, not written-in-full
into both stage files.

## Build notes added after stage-3 round 2 (O-1, O-3, A-1, O-2)

- **O-1 (updated round 3 for the shared `charter.md`) — the charter is ONE copy; stages 3/6
  differ only by their EXTRA bullets.** The shared `stages/charter.md` holds the common core
  (CH0–CH7, CH13 + the conditional position/concurrency lenses). `stage-3.md` references it
  and adds the stage-3-only bullets **CH8 (coverage challenge) + CH9/CH10 (label audit)**;
  `stage-6.md` references it and adds **ST6d (mechanical diff)**. Because there is one charter
  copy, the round-2 drift surface is gone. C5 checks: (i) the shared charter agrees with the
  current source; (ii) stage-3.md carries CH8/CH9/CH10 and stage-6.md does NOT (the deliberate
  asymmetry — CH8/CH9/CH10 scoped `{3}`; do not "restore" them to stage 6). C5 checks
  agreement only across a rule's *own* governing-stage-set.
- **A-1 — the SEV1 routing TABLE lives in each gate file, not only the loop diagram.** The full
  severity table (blocker/major/minor/nitpick → routing per stage) AND SEV2/SEV3 (the "human
  decision" framing + "route on the reviewer's severity / no silent demotion") must be written
  into `stage-4.md`, `stage-7.md`, `stage-8.md` — not merely a target list (round-3 F5-NEW: SEV3's
  no-silent-demotion force is precedence-adjacent to the SEV1 table + SEV2, so the *table* must
  co-locate, or the adjacency P-1 protects is lost). A gate agent opening only router + its gate
  file must find where each severity routes. The loop diagram in the slim METHODOLOGY is
  orientation, NOT the gate's operative routing source.
- **F2-NEW (round 3) — HIL is {4,8,1.5}, NOT gate 7.** The round-2 O-6 fix wrongly added gate 7;
  reverted. Source (METHODOLOGY:526) says stages 1–7 run autonomously; a blocker@7 routes to build,
  not a human restart, so no HIL trigger fires at 7. The human-tie-break-at-7 intuition is covered
  by SEV4 (iteration cap → {4,7,8}), a different rule already in the oracle.
- **F1-NEW (round 3) — CH9/CH10 {3}-scoping is INFERRED, not grep-derived.** The source tags only
  the coverage-challenge bullet CH8 "(stage 3)" (METHODOLOGY:251); the label-audit bullets
  (256, 271) carry no stage tag. {3}-only is a defensible inference (label-audit reviews the
  criteria + the stage-8 table, which only stage 3 sees), but it is the one non-mechanical scoping
  in the oracle — recorded so a stage-6 reviewer doesn't later "restore" CH9/CH10 to stage 6 as a
  missing-rule finding (the mirror risk to O-1).
- **O-3 — CP3 "instrument before you build" is scoped `{2}` deliberately.** The literal rule is
  "measurement/instrumentation is part of the *plan*" (METHODOLOGY:38-40; SKILL:56-57 ties it to
  stage 2). Its criterion-authoring consequences are separate rules already scoped to 1.5
  (ST1.5d/e, CP5). `{2}` is correct, not a narrowing — recorded so the builder need not re-derive.
- **O-2 — the self-check *criteria* must survive the SKILL slim.** SK-SELF is `ref/meta`, but the
  standing self-check criteria it names (live==source; SKILL↔stage-file consistency;
  behavior-preservation for anything moved/removed) are the source of C4/C5 and must remain
  loadable where a skill-edit run is planned (stage-1.5). Keep them in `stage-1.5.md` (or the
  self-check reference the router points at), not dropped as "pure reference."
