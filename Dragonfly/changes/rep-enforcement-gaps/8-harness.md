# 8 — Harness (conformance-only; no baseline)

All gating criteria verified on the built tree (base c8db6fa).

| # | Criterion | Result |
|---|---|---|
| C1 | `B-REP-4` @ stage-5 — negative-can't-eliminate + same-or-weaker + untrusted-negative + ledger-evidenced + multi-axis | ✅ (5/5 elements) |
| C2 | `B-REG-1` @ stage-5 — executed-vs-designed + record-deviation + re-scope + no-registration-is-a-defect | ✅ |
| C2b | `A-4-2` @ stage-4 registers the design (params/stop-rule/conditions) to `decisions.md` — the B-REG-1 referent | ✅ |
| C3 | `B-TARGET-1` @ stage-2 — attribute-a-share + re-read-not-reconstruct + drift⇒incidental + per-step marker | ✅ |
| C4 | B-TARGET-1 composes with incidental-findings + inclusion tie-break agrees | ✅ |
| C5 | stage-6 tie-in — untrusted results don't count as eliminations (cycle/elimination vocab) | ✅ |
| C6 | rep-gate scope → "1, 4, and 5" both sites; 0 stale "1 and 4" | ✅ |
| C6b | SKILL incidental-findings B-TARGET-1 pointer | ✅ |
| C7 | 3 new IDs + A-4-2 collision-free in base | ✅ |
| C8 | position/behavior preserved — additive only (3 deletions = 2 scope swaps + 1 append-extension) | ✅ (stage-6 cold enumeration) |
| C9 | live == source | ✅ `diff -r` empty |
| C10 | cross-doc consistency (observation-ledger contract intact; pointers resolve) | ✅ |

Stage-6 cold review: MINOR (a stale criteria-doc line → fixed); build itself CLEAN.
**Verdict: PASS — all gating criteria verified.** No advisory criteria, no regression arm. The three
rep-enforcement gaps (result-time gate, as-run-vs-as-designed, operator-drift) are live in source +
installed.
