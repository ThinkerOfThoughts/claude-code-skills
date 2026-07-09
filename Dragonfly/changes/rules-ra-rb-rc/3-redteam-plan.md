# 3 — Red-team of the plan (verbatim record)

## Provenance
- **Reviewer:** cold `general-purpose` subagent, no shared context (agentId a1a478287a92bb161),
  Claude Opus 4.8. Charter: four lenses + discipline + mandatory coverage-challenge; the six
  verification foci given in the spawn prompt (archived in the run transcript).
- **Context (closed set):** the 3 change artifacts + dragonfly source (charter, stage-1/2/3/5/7,
  SKILL, METHODOLOGY) + the guarded-change twin charter + tree-wide grep. Paths validated (decisions.md).

## Verdict: **MAJOR** (route back to revise criteria/plan)

### Factual — CLEAN (earned)
- **Count surface EXACTLY 6, no 7th** — robust flatten/strip sweep returns charter L3 & L21, SKILL
  L83, METHODOLOGY L88, stage-1 L7 & L55; all other `four…lens` hits are under `changes/`. Target
  strings match live text byte-for-byte. Stage-4 states no count. 
- **Rule-ID collision CLEAN** — B-VER-1/B-TIME-1/B-FID-1/B-COST-1 absent pre-change; fit the scheme.
- **Fidelity-twin claim TRUE** — GC lens 5 at Guarded_change/charter L23 + guard L42-47; dragonfly
  E1a/E1b are faithful adaptations.
- **All plan anchors exist** as described (E1a–E6 verified).

### Logical — CLEAN
- B-TIME-1's "unestablished timeline ⇒ stays ungated" is consistent with A-3-3/B-GBP-1 (adds a
  precondition, doesn't redefine the marker).
- B-TIME-1 (E5) is orthogonal to A-7-4 root-or-relay (introduction-vs-first-appearance ≠ why-down).
- B-VER-1 strengthens (not replaces) B-EVID-1; B-EVID-1 preserved everywhere.

### Missed-opportunity — MINOR ×2
- **M1 — dragonfly fidelity lens omits the spot-check-the-pins guard its GC twin carries.** The GC
  twin extended TWO bullets: the earned-clean bullet (E1b mirrors it) AND the "Spot-verify the
  citations themselves" bullet (GC L52-53: for a clean fidelity lens, spot-check the term→mechanism
  pins are real). Dragonfly E1b copies only the first; dragonfly's Spot-verify bullet (charter
  L38-40) is left untouched. Adopt it or record as intentional narrowing.
- **M2 — E6 anchor splits the triage flow.** "Append after B-TRI-3" puts B-FID-1 between B-TRI-3 and
  the C-LITE-1 paragraph (L54-60). Non-breaking, but placing B-FID-1 after the C-LITE block reads
  cleaner.

### Unstated-assumptions + COVERAGE-CHALLENGE
- Assumptions verified sound: no numbered `(lens N)` cross-ref exists (grep 0 hits); R-A correctly
  at stage-2 not the charter.
- **MAJOR — E1b (earned-clean fidelity guard) is observed by NO criterion.** C3 checks only the lens
  entry + mechanism-vs-proxy content; nothing gates the earned-clean **guard** — the clause that
  makes the lens non-vacuous. A build that drops/garbles E1b passes all 10 criteria. Fix: extend C3
  to grep the guard.
- **MINOR — E1c (fidelity aim) observed by no criterion.** Add an oracle. (E3b B-VER-1 pointer also
  unobserved but the substantive rule is covered by C1 at its home → acceptable.)

## Resolutions applied (this revision pass)
- **MAJOR E1b:** C3 extended to gate the earned-clean fidelity guard (grep `clean \*fidelity\* lens
  must be earned` in charter.md) + the E1c fidelity aim.
- **M1:** adopt the twin's spot-check-pins clause → new edit **E1e** appends it to dragonfly's
  Spot-verify bullet (charter L40). (Full parity with the GC twin.)
- **M2:** E6 anchor moved to **after the C-LITE-1 paragraph** (end of the triage section) so B-FID-1
  doesn't split B-TRI-3 → C-LITE-1.
- Independent re-check of the revised content: the stage-6 cold review reads the **built bytes** and
  its checklist now includes E1b/E1c/E1e presence + correctness (the built-artifact cold pass is the
  independent verification of these additive, mechanical revisions).
