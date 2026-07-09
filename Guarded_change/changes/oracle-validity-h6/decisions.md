# decisions.md — gate log (append-only)

## Run-start path validation (CFG3) — 2026-07-09
All reviewer-context paths validated readable. No dead paths.
- Change artifacts: 1-spec.md, 1.5-criteria.md, 2-plan.md — OK
- Skill source (source-of-truth for claim-checking): stages/stage-8.md, stages/stage-1.5.md,
  stages/charter.md, stages/stage-3.md, SKILL.md, METHODOLOGY.md — OK
- Starting state: source == installed (`diff -r` clean), branch `main`, working tree clean.

## Gate 4 (round 1) — 2026-07-09 — worst = BLOCKER → route back to plan + criteria
Cold reviewer agentId a39abaae26434c31c (general-purpose, Opus 4.8). Full verbatim record in
3-redteam-plan.md. Findings, ALL independently reproduced by the author (CH6 consumer duty):
- **BLOCKER (ellipsis)** — plan's NEW H6 block uses `… \`verified = no\`.` eliding the
  `fails against the unguarded version` clause it promises to preserve. `grep 'unguarded'` on the
  NEW block → no match. → rewrite Edit A as the FULL H6 paragraph verbatim; build edits real file.
- **BLOCKER (C3 wrap-broken oracle)** — reviewer ranked BLOCKER (author had MAJOR; author defers
  up per SEV3). `grep -c 'fails against the unguarded version' stages/stage-8.md` → **0** (source
  wraps `…the\nunguarded version`, L68→69); C3's stated delete-phrase self-test is degenerate
  (baseline already returns 0). → redesign C3 to a wrap-robust positive assertion (flatten
  newlines then assert) + a real fire-on-deleted-clause self-test.
- **MAJOR (H6 "this way" anaphora)** — inserting two long spans BETWEEN H6's first sentence and
  "A defective check found this way…" distances the anaphor from its referent (the targeted cold
  check) → rebind risk (CP6 intra-rule). → move both additive spans to the END of H6 (after
  "…invalidated."); add criterion C10 asserting H6's original sentence adjacency preserved.
- **MINOR (C8 wording)** — self-test conflates escaped `H6\.` (→ only L65) vs unescaped `H6.`
  (→ L65 + CH6 hits stage-8:100, stage-6:16). → fix C8 to the exact pattern; drop the muddle.
- **MINOR (ST1.5f ID order)** — a,f,b,c,d,e. Semantic placement right → keep with a one-line note.
- **MISSED-OPP (MINOR)** — no canonical normalization recipe in H6 → add a short parenthetical
  recipe (flatten newlines, strip `**`). Adopted.
- **NITPICK** — dense H6 paragraph; move-to-end already helps. Not restructured. Logged.
- **Reproduction log:** `grep -c 'fails against the unguarded version' stages/stage-8.md` → 0;
  `sed -n '68,69p'` shows the wrap; `grep 'unreviewed check'` → only L65; `grep -E 'H6.'` → L65 +
  stage-8:100 + stage-6:16.
- Route: revise 2-plan.md (full Edit A, spans-to-END, recipe) + 1.5-criteria.md (C3 redesign, C8
  fix, C10 anaphora, ST1.5f note) then re-run stage-3 round 2. First bounce at gate 4 (cap 1/2).
  No criteria frozen yet.

## Gate 7 (stage-6 code review) — worst = CLEAN → stage 8
Cold review agentId a6572dd0caf787c7c: build byte-for-byte verbatim to plan, purely additive,
anaphora preserved, dogfood oracles green. NITPICK only (design-inherited recipe terseness). No bounce.

## Gate 8 (harness) — CONFORMANCE-ONLY — verdict PASS
All 10 gating criteria verified (8-harness.md). C3 & C10 self-tests FIRE on their known-violating
inputs (0), pass on built (1) — the oracles are shown able to fail. Loop complete.
