# 3 — Independent oracle-completeness re-derivation (ROUND 3) — verbatim record

The owner-authorized root-cause pass for the recurring "missing oracle rows" class. A cold, independent
enumerator read the SOURCE (`Dragonfly/SKILL.md` + `METHODOLOGY.md`) and enumerated every atomic
normative statement FRESH (before reading the oracle), then reconciled against `2-rule-oracle.md`.

## Provenance
Agent type: general-purpose (Explore-class), cold independent enumerator. Model: `claude-opus-4-8[1m]`.
Files + sha256: `Dragonfly/SKILL.md` `b5e122ef…`; `Dragonfly/METHODOLOGY.md` `04d1044c…`;
`2-rule-oracle.md` (pre-round-3-additions) `4b9319ee…`.

## Verdict: oracle essentially complete + correctly scoped

> "I independently enumerated ~86 atomic normative statements across the two files before reading the
> oracle. After reconciliation, 83 map cleanly to oracle rows … **no load-bearing normative rule that
> is fully missing**; the three prior-round additions (A-8-2, A-9-6, A-9-7) close the gaps that
> mattered." **SPURIOUS: none** (every one of the 83 rows traces to a real source statement).
> **MIS-SCOPED: none that would narrow behavior** (one minor flag: B-TBG-1).

## Actioned findings (all applied to the oracle → 86 rows)

- **#3 (medium; the highest-value, restructure-specific) — B-CH-inherit ADDED.** METH:394-396 "cold
  passes inherit ALL of guarded-change's unconditional discipline bullets … provenance included" — the
  catch-all that makes the B-CH-* enumeration non-exhaustive by design; *"precisely the rule that keeps
  the B-CH-* enumeration honest when the charter gets forked in this restructure."* Added Group B, scope
  `1,4,7`, HOME=byref (dissolves post-fork → self-contained charter). **Consequence for the build:** the
  fork must carry gc's FULL unconditional set, not only the 9 enumerated B-CH-* rows (verified my
  enumeration already covers gc charter's unconditional bullets: 4 lenses + cite/rank/unver/noiss/clean/
  spot/prec + code-access + provenance).
- **#1 (medium) — B-EVID-1 ADDED.** METH:58-59 "evidence over rhetoric" — governs the agent's OWN
  conclusions at every stage, survived only as fragments (A-5-1 stage-5-only; B-CH-cite reviews-only).
  Added Group B, scope `2,3,5,7,9`.
- **#2 (low-medium) — B-CAUS-1 ADDED.** METH:64-67 "causality runs root-cause→symptom" — underwrites
  the stage-7 toggle + stage-9 masking route; behavior was captured (A-9-1/A-9-2/A-7-1) but the named
  principle had no row. Added Group B, scope `7,9`.
- **B-TBG-1 scope WIDENED** `4,5` → `4,5,6,7` (the rule bars consumption "by a later stage" — advancing
  a marker at 7, counting cycles at 6 — the `4,5`-only scope was the narrowest reading).

## No-action findings (recorded, correctly handled already)
- **#4** METH:171 "confirmed/refuted status is a claim citing the run" — subsumed by A-5-1. No row needed.
- **#5** METH:377-378 "Dragonfly does not fork guarded-change's charter" — a current-state claim Theme-2
  deliberately REVERSES (the HOME=byref → own-file migration); correctly a Theme-2 target, not a
  preserved rule. No row (its removal is the untangle).

## Coverage confidence (reviewer's words)
> "High. … 83 map cleanly … none is a mechanical gate that a restructure would silently break; the
> highest-value one is #3 (the 'inherit ALL unconditional bullets' catch-all)." Section not fully
> reducible to 1:1 rows: the red-team charter section (METH:369-403) — the enumerable bullets are
> covered; the catch-all (#3, now B-CH-inherit) was the one piece without a home. **Every other source
> section reconciled cleanly.**

Oracle now **86 rows** (35 A / 34 B / 17 C), mechanically counted. This pass is the round-3 answer to
the recurring "is the inventory complete?" class — an independent enumeration found only 3 principle/
catch-all additions + 1 scope widen, no spurious rows, no further load-bearing gaps.
