# 8 — Harness (conformance-only; no baseline)

All gating criteria verified on the built tree (base 4237fd3). Dogfooded: every prose oracle is a
positive per-site assertion, flattened first, with a fire-on-known-violating-input self-test.

| # | Criterion | Result |
|---|---|---|
| C1 | H6 generalized to all conformance oracles + self-test language | ✅ (positive greps) |
| C2 | positive-over-absence preference (a/b/c) present in H6 | ✅ |
| C3 | H6 fail-against-unguarded clause preserved — wrap-robust positive | ✅ built=1; **self-test: deleted-clause copy=0 (fires)** |
| C4 | stage-1.5 ST1.5f note (able-to-fail + prefer-positive + H6 ref) | ✅ |
| C5 | no other rule block edited (diff hunks only in allowed regions) | ✅ (stage-6 cold read) |
| C6 | diff = exactly {extend H6}∪{add ST1.5f}, 2 files | ✅ (+22/−1) |
| C7 | position preservation earned by cold reader | ✅ (stage-6 CLEAN) |
| C8 | 'unreviewed check' single hit (exact contiguous anchor) | ✅ =1 |
| C9 | live == source | ✅ diff -r empty |
| C10 | H6 anaphora adjacency preserved — wrap-robust | ✅ built=1; **self-test: reorder copy=0 (fires)** |

Stage-3 (2 rounds) + stage-6 all independent cold subagents; round-1 caught 2 BLOCKERs (incl. the
first-draft C3 oracle being itself wrap-blind — the exact failure this change fixes), closed; round-2
+ stage-6 CLEAN. **Verdict: PASS — all 10 gating criteria verified.** No advisory, no regression arm.
