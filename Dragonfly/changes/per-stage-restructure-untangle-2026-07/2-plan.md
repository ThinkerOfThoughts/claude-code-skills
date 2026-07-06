# 2 — Plan: dragonfly per-stage restructure (Theme 1) + untangle (Theme 2)

Mirrors the proven guarded-change restructure (`Guarded_change/changes/per-stage-restructure-2026-07`,
live `3d6889b`). Build = **reorganization + fork**, not rewrite: every oracle rule (`2-rule-oracle.md`,
86 rules) relocates into per-stage files unchanged; the 4 by-reference pieces are forked into
dragonfly's own files, content-faithful.

---

## §A — The file set (frozen at gate 4) + per-stage rule mapping

### Files

| File | Role | Est. lines | Loaded when |
|---|---|---|---|
| `SKILL.md` | thin **router**: inputs, cold-start guard, loop router table, stop-for-human summary, self-check (**D-11 clause removed**) | ~80 | every stage |
| `stages/charter.md` | dragonfly's **forked** red-team charter: gc charter's **unconditional core** (4 lenses + discipline + provenance *record-elements only*) **+ diagnosis aiming (5 bullets) + severity model + coverage-challenge exclusion**. **Excludes** gc's conditional position/concurrency lenses, the gc-run-specific A/B clause, and the closed-set-input rule (round-1/2 fix — none are current dragonfly behavior) | ~90 | stages 1, 4, 7 |
| `stages/stage-0a.md` | Translation + 0a confirm | ~22 | stage 0a |
| `stages/stage-0b.md` | Freeze + ledger-is-a-file | ~20 | stage 0b |
| `stages/stage-1.md` | Reproduction + rep-gate + triage (+charter) | ~90 | stage 1 |
| `stages/stage-2.md` | Observation ledger (append-only) | ~30 | stage 2 |
| `stages/stage-3.md` | Hypotheses + gate-before-present | ~70 | stage 3 |
| `stages/stage-4.md` | Discriminating test + rep-gate + triage + trust-before-gate (+charter) | ~80 | stage 4 |
| `stages/stage-5.md` | Run & record + trust-before-gate consumption | ~28 | stage 5 |
| `stages/stage-6.md` | Convergence gate + iteration cap | ~60 | stage 6 |
| `stages/stage-7.md` | Root-cause confirmation + depth check + coverage sweep + rate-rubric + triage (+charter) | ~100 | stage 7 |
| `stages/stage-8.md` | Handoff (+ KEEP: hand to guarded-change) + characterized ending | ~55 | stage 8 |
| `stages/stage-9.md` | Fix verification (9a/9b) + rate window | ~65 | stage 9 |
| `METHODOLOGY.md` | slim orientation/reference: why, loop diagram, two layers, config contract, artifacts | ~200 | orientation only |

Final file set is **exactly these 14** (SKILL + 11 stage files + charter + METHODOLOGY). No other
`Dragonfly/` file changes; no guarded-change file changes; no `changes/` history changes.

### Per-stage rule mapping (oracle → stage-file homes)

Cross-cutting rules (Group B / the forked pieces) are **repeated in full** into each governing stage.
The charter (loaded at 1/4/7) carries the review-machinery cross-cutting rules once for those stages.

| Stage file | Oracle rules it must carry |
|---|---|
| `stage-0a.md` | A-0a1, A-0a2 (+ 0a clause of C-HIL-1) |
| `stage-0b.md` | A-0b1, A-0b2, B-LED-1 |
| `stage-1.md` | A-1-1, A-1-2, A-1-3, A-1-4; B-REP-1, B-REP-2, B-REP-3; B-TRI-1, B-TRI-2, B-TRI-3, C-LITE-1, C-LITE-2; B-GBP-1 (repro-escape stays ungated); **loads `charter.md`** (B-CH-*, B-AIM-1/2/5, B-PROV-1/2, B-SEV-1/2) |
| `stage-2.md` | A-2-1, A-2-2, B-LED-1, B-LED-2, B-EVID-1 |
| `stage-3.md` | A-3-1, A-3-2, A-3-3; B-GBP-1, B-GBP-2, B-GBP-3, B-GBP-4, C-HIL-2, B-EVID-1 |
| `stage-4.md` | A-4-1; B-REP-1, B-REP-2, B-REP-3; B-TRI-1, B-TRI-2, B-TRI-3, C-LITE-1, C-LITE-2; B-TBG-1; **loads `charter.md`** (B-CH-*, B-AIM-1/2/5, B-PROV-1/2, B-SEV-1/2) |
| `stage-5.md` | A-5-1, B-TBG-1, B-EVID-1 |
| `stage-6.md` | A-6-1, A-6-2, A-6-3, A-6-4, A-6-5, A-6-6 (+ escalate-to-human) |
| `stage-7.md` | A-7-1, A-7-2, A-7-4, A-7-5, A-8-3; rate-rubric (A-7-1c); B-REP-3, B-TRI-1/2/3, C-LITE-1/2; B-GBP-3, B-EVID-1, B-CAUS-1; **loads `charter.md`** (B-CH-*, B-AIM-2/3/4/5, B-PROV-1/2, B-SEV-1/2) |
| `stage-8.md` | A-8-1, **A-8-2 (KEEP)**, A-8-3 |
| `stage-9.md` | A-9-1, A-9-2, A-9-3, A-9-4, A-9-5, **A-9-6, A-9-7**, B-EVID-1, B-CAUS-1 |
| `charter.md` | B-CH-lens/code/cite/rank/unver/noiss/clean/spot/prec; **B-CH-inherit** (fork carries the FULL unconditional set); B-AIM-1..5; B-PROV-1, B-PROV-2; B-SEV-1, B-SEV-2 (**NO position/concurrency lenses, NO A/B clause, NO closed-set rule — excluded, not current dragonfly behavior; round-1/2 fix**) |
| `SKILL.md` | C-ST-1, C-ST-2, C-COLD-1, C-HIL-1, C-HIL-2, C-SELF-1..4, C-SELF-6 (router table for A-*; **C-SELF-5 REMOVED**) |
| `METHODOLOGY.md` | C-TRIG-1, C-REF-1, C-REF-2, C-REF-3 (+ the "why" narrative, loop diagram) |

*Every one of the 86 oracle rows appears in the table above at least once, in every stage of its
governing-set* (round-3 B-1 fix: the round-3 additions are now integrated into their stage rows —
B-EVID-1 in stage-2/3/5/7/9, B-CAUS-1 in stage-7/9, A-9-6/A-9-7 in stage-9, B-CH-inherit in charter.md
— not only this note; freeze-checklist item 5 asserts every oracle ID appears in a §A row).
The C1 stage-8 mapping table will verify each row landed present + correctly scoped.

## §A.2 — Theme-2 fork plan (the D-S2 untangle)

Fork from **current** guarded-change (`Guarded_change/` at this run's recorded base rev, gc live
`3d6889b`). Each fork is **content-faithful** (C9b); the only recorded divergences are dragonfly's
aiming + the coverage-challenge exclusion + the fact dragonfly stops tracking gc's future edits.

1. **Charter → `Dragonfly/stages/charter.md`.** Fork the **UNCONDITIONAL CORE** of
   `Guarded_change/stages/charter.md` only — the four lenses; the discipline bullets (cite-or-it-
   doesn't-count, rank, flag-unverifiable, "no issue" valid, clean-factual-earned, spot-verify,
   precision); code/source-access; and provenance = **the five record-elements only** (verbatim
   charter, exact context list, verbatim output, agent+model, hashes; = dragonfly's spelled-out
   B-PROV-1) — restated in dragonfly's own words. **EXCLUDE** (round-1/2 review fix — current dragonfly
   does **not** carry these; METH:394 has it inherit only *unconditional* discipline bullets, "those
   with no stage or trigger scope"): gc's conditional **position lens** (`charter.md:55-65`),
   **concurrency lens** (`66-76`), the gc-run-specific **A/B-arms supplementary-context clause**
   (`52-54`), **and the "reviewer-input-is-a-closed-set" rule** (`48-52` — round-2: not in dragonfly's
   spelled-out provenance; source grep for `closed set`/`supplementary` empty). Forking any of these
   would ADD reviewer rules dragonfly never had → a behavior addition inside a preservation run
   (violates C1 "no new normative rule"). **Append** the 5 diagnosis-aiming bullets (B-AIM-1..5) + the
   **coverage-challenge exclusion** (B-PROV-2: does not apply to direct stage-7/lite; a full-GC triage
   keeps gc's stage duties). Provenance note: `forked from Guarded_change/stages/charter.md @ 3d6889b —
   unconditional core only; position/concurrency lenses, A/B clause, and closed-set rule deliberately
   excluded (see decisions.md)`. **Recorded divergence:** whether dragonfly *should* gain any of the
   four excluded items is a separate additive question, surfaced in `9-report.md`, not decided in this
   preservation run.
2. **Severity model → `charter.md`** (loaded at the review gates 1/4/7). State blocker/major/minor/
   nitpick + worst-routes-the-gate (B-SEV-1) and the 2-bounce iteration cap (B-SEV-2) in full — no
   "Identical to guarded-change (see its METHODOLOGY)". **Fork source:** gc's SEV1–SEV4 table in
   `Guarded_change/stages/stage-8.md:143-174` + the routing rows in `stage-4.md`/`stage-7.md` (NOT
   stage-6 — it carries no severity table; round-1 nitpick fix). (Stage-6's N-cycle convergence cap
   A-6-2 is separate and lives in `stage-6.md`.)
3. **Rate-based rubric → `stage-7.md` (toggle) + `stage-9.md` (window).** State in full: for a
   rate-based/intermittent symptom the toggle criterion **pre-states the expected rate shift + run
   count**; a single flip does not satisfy it; 9a/9b set the observation window up front from ledger
   frequency. Remove "guarded-change's probabilistic rubric, by reference".
4. **guarded-change-lite → the triage block in `stage-1/4/7.md`.** State in full: a single cold pass
   using **dragonfly's own** charter (`stages/charter.md`) + evidence discipline, one-line intent +
   "does exactly X, exercises path P" criterion → fix → run; keeps charter + provenance, drops the
   five-item doc scaffolding; recorded in `decisions.md`. Remove "defined by reference / inherits
   guarded-change's charter" and the "pointer back to guarded-change as source of truth".

**Removed:** C-SELF-5 (D-11 self-check) from `SKILL.md`, replaced by the provenance note.
**Preserved unchanged (C10):** A-8-2 (stage-8: hand the fix to guarded-change; don't author it) in
`stage-8.md`; the **full-GC triage invocation** (B-TRI-2 rules 1&2 route an expensive/multi-file
artifact into a *full guarded-change run*, which keeps gc's own duties) in the triage block.

## §A.3 — Per-stage load budget (C3a target)

Current per-stage load = whole doc = **670 lines** at every stage. New per-stage load = `SKILL.md`
(~80) + `stage-N.md` (+ `charter.md` ~90 for stages 1/4/7). Heaviest = stage 7: 80 + 100 + 90 =
**~270**. **Cap: per-stage load ≤ ~270 lines** (≈ 40% of 670). **Round-1 risk fix — pre-check
stage-7's rule-only line floor** (the verbatim rules with zero prose) **before committing to the
cap:** if that floor already approaches 270, the cap **rises** rather than trading rule substance to
fit (the caps exist to prevent exactly that trade; cf. gc's audit-hardening cap-vs-substance rule). A
recorded few-line overage is acceptable (gc landed 262 max under an analogous escape); silently
dropping a rule to fit is not. Token target recorded alongside at stage 8 (≤ ~45% of the current
per-stage token load). Total line count will **rise** (repetition + forks) — advisory C8, by design.

---

## §B — Verification (Tier 2, frozen at gate 4)

Owner chose **Tier 2** (content-primary + targeted behavioral spot-check). No full A/B battery, no
BROKEN control (non-discriminating twice: flagship-probe + gc battery).

**Mechanical checks (the bulk of assurance):**
- **C1** — checked against BOTH the oracle AND the source (round-3 hardening): **(i)** oracle→new
  mapping resolves all **86** rows (present + correctly scoped); **(ii)** a stage-6 cold reviewer walks
  the current `Dragonfly/SKILL.md`+`METHODOLOGY.md` **rule-by-rule vs the built files** — every source
  rule present, correctly scoped — so an oracle gap can't hide a dropped rule (the recurring round-1/2
  failure class); **(iii)** reverse: any normative rule in the new files absent from the oracle is
  flagged (a wrongly-added rule, or a source rule the oracle missed — reconcile vs (ii)).
- **C4** — `diff -r ~/.claude/skills/dragonfly/ Dragonfly/` clean.
- **C5** — cross-file consistency sweep driven by the oracle's cross-cutting list; deliberate
  asymmetries (coverage-challenge exclusion) respected.
- **C6(i)** — router resolves: every stage (0a,0b,1–9) has a file the router points to.
- **C9(a)** — de-coupling by **read-confirm + whole-file read-and-classify** (round-2 fix: the
  literal-pattern grep was still adjacency-anchored — it missed SKILL:107 "guarded-change's *unchanged*
  charter" and METH:394 "inherit *ALL of* guarded-change's"). Two parts:
  (i) **Read-confirm** each of the 4 fork targets (charter, severity, rate-rubric, lite) states its
  rule **in full in dragonfly's own words**, with no "see/inherits/reuse/using guarded-change's
  `<piece>`", "by reference", "Identical to guarded-change", or "referenced from guarded-change".
  (ii) **`grep -in 'guarded-change' Dragonfly/`** to LOCATE every occurrence, then **READ and classify
  each hit** (a human/reviewer read, not a pattern match — so no adjacency blind spot can hide a
  survivor) as one of:
    - **KEEP composition mentions — dragonfly *using/handing-off-to* guarded-change, not depending on
      its text for a rule (non-exhaustive examples; round-3 B-3 fix widened this):** (a) the
      sibling/description framing ("Sibling of guarded-change", "guarded-change makes the fix", the
      loop-diagram HANDOFF row); (b) the **stage-8 handoff** (A-8-2: "hand to guarded-change … do not
      author the fix"); (c) the **full-GC triage invocation** (triage rules 1&2: route into a *full
      guarded-change run*); (d) the **masking route** (stage-9: "back to guarded-change"); (e) the
      **`forked from guarded-change @3d6889b` provenance note**; (f) the **triage-mechanism / lite-routing
      composition** — dragonfly invokes guarded-change (or guarded-change-lite) *as the review tool*:
      "diagnostic artifacts get guarded-change", "the triage's guarded-change/lite pass **is** the cold
      review", "invoke the guarded-change skill directly", **triage rule 3 → guarded-change-lite**, "that
      is guarded-change's domain".
    - **Surviving rules-dependency (a defect → fix):** a phrasing that makes a dragonfly **RULE point at
      guarded-change's text for its definition** ("inherits guarded-change's charter", "Identical to
      guarded-change", "by reference", "referenced from guarded-change", "guarded-change's unchanged
      charter").
  **Classification rule:** each hit is either **composition** (dragonfly uses/hands-off — (a)–(f) are
  examples, not a closed list; a novel legitimate composition phrasing is composition, not a defect) or
  **rules-dependency** (a rule defined by-reference — a defect). **Pass = every `guarded-change` hit
  classified, zero in the rules-dependency bucket.** Presence check: the 4 forked pieces exist in full,
  each self-contained.
- **C9(b)** — faithfulness mapping: each forked piece vs its gc source, same rules/effect; divergences
  listed.
- **C10** — locate A-8-2 + the full-GC triage invocation in the new files; meaning unchanged.

**Behavioral spot-check (4 arms — the Tier-2 "teeth"):** each a cold `general-purpose` agent given
**only** the built `SKILL.md` + the one routed stage file (+ `charter.md` where the stage names it),
placed at the stage, handed a triggering case. Grade FIRED / DID NOT FIRE with a required quote; record
file-opens (C3b). The 3 most position-sensitive rules:

| Arm | Rule (oracle) | Stage | Loads | Triggering case | FIRE = |
|---|---|---|---|---|---|
| SC-1 | B-REP-1 representativeness gate | 1 | SKILL+stage-1+charter | a repro whose control run does **not** exhibit the symptom | refuses to trust it; demands a control that exhibits the symptom |
| SC-2 | B-GBP-1 gate-before-present | 3 | SKILL+stage-3 | an `ungated` top-ranked hypothesis; "so what's the cause?" | presents it as **"candidate, ungated"**, NOT the cause |
| SC-3 | B-CH-clean clean-factual-earned-with-citations | 7 | SKILL+stage-7+charter | a cold causal-chain review returning "factual lens clean" with **zero** source citations | treats it as **un-run**, re-runs / demands citations |
| SC-4 | B-TRI-1/B-TRI-2 triage (a **cross-cutting** rule at a **second** home) | 7 | SKILL+stage-7+charter | a stage-7 **toggle** that spawns an agent/CLI (token-burning) | routes the toggle through **full guarded-change** triage before trusting it, not an untriaged run |

SC-4 is the round-1 missed-opportunity fix: it exercises a cross-cutting rule (triage) at a **second**
stage of its `1/4/7` governing-set, catching the "present in one stage file, dropped from a sibling"
failure mode that C1's content check alone is weakest against. *Recorded residual (round-1):* SC-2
exercises gate-before-present at stage 3 only; its **stage-7** instance (B-GBP-3, "cold-red-teamed →
root cause") rests on C1 mechanical mapping — acceptable given the mechanical backstop, noted so the
asymmetry is deliberate.

*Pass (C2, Tier 2):* C6(i) resolves for every stage; SC-1..4 each FIRED; each arm opened only its
routed file(s) + named reference (C3b). Any DID-NOT-FIRE → **investigate**: a genuine per-stage-
isolation drop is a **blocker → build**; a case defect (the stage file was fine, the prompt didn't
provoke) → rebuild that arm. Author grades with quotes; any grade that would flip C2 → **owner**.
*Estimate:* 4 arms (+ optional 1 grader) ≈ 200–350K tokens.

**Instrumentation:** none new — all checks are grep/`wc`/`diff`/inspection + 4 cold arms. The arms'
transcripts (Read calls) instrument C3(b).

---

## Severity → routing thresholds

Standard model (now dragonfly's own, per Theme 2): **blocker → stage 1** (confirm direction);
**major → stage 2**; **minor → fix in place, proceed**; **nitpick → log, proceed**; **clean →
proceed**. Route on the **reviewer's** severity; a demotion needs a logged human tie-break.
**Iteration cap:** 2 bounces at the same gate on the same finding class → owner tie-break.

**Gating criteria:** C1, C2, C3, C4, C5, C6, C9, C10. **Advisory:** C7 (legibility), C8 (total size).
A gating criterion must be verified by its check at stage 8 — no deferral/proxy.

**Path validation (gate-4 precondition):** the cold reviewer's context paths for this run — the
current `Dragonfly/SKILL.md` + `METHODOLOGY.md`, `Guarded_change/stages/charter.md` (fork source),
this run's `{1-spec, 1.5-criteria, 2-plan, 2-rule-oracle}` — are validated to exist/be readable and
the result recorded in `decisions.md` before gate 4 passes.

## Freeze checklist (gate 4) — round-2/3 anti-drift additions

Before recording the frozen sha256s in `decisions.md`, mechanically confirm:
1. **Count consistency** — the oracle count token is derived by `grep -cE '^\| [ABC]-' 2-rule-oracle.md`
   (currently **86**) and reads identically in `1.5-criteria.md` and `2-plan.md`; `grep -rnE '\b(78|80|81|83)\b'`
   over the artifact set returns only historical mentions in the review records / count-history
   sentence — **no stray old count** in a live C1 instruction. (This is the check that would have caught
   the round-2 B-1 straggler.)
2. **Oracle completeness** — the round-3 independent completeness pass is recorded; the mechanical
   count matches the enumerated rows.
3. **No un-decided over-fork** — the C9b divergence list names all four excluded gc-charter items
   (position lens, concurrency lens, A/B clause, closed-set rule); `grep -in 'closed set\|supplementary'
   Dragonfly/SKILL.md Dragonfly/METHODOLOGY.md` on the *current source* is empty (confirming they are
   not current behavior).
4. **§A-vs-oracle coverage (round-3 B-1 fix):** every oracle ID (all 86) appears in the §A per-stage
   mapping table in a governing-stage row. **The check must expand the table's abbreviations** — the
   slash-list `B-CH-lens/code/cite/rank/unver/noiss/clean/spot/prec` covers all nine B-CH-* IDs; ranges
   `B-AIM-1..5`, `B-AIM-2/3/4/5`, `C-SELF-1..4` cover their members — so a naive literal grep reports
   ~14 false "misses"; the abbreviation-aware confirmation (round-3) found **0 genuine gaps**. This
   catches the §A construction guide drifting from the frozen oracle (the round-3 B-1 defect class), as
   item 1 catches count drift and item 3 catches the closed-set stale word.
5. **Frozen set:** `1.5-criteria.md` (sha256), the oracle (sha256), the C2 Tier-2 design (§B), and the
   final file set (§A).
