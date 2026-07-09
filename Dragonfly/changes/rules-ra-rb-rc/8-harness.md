# 8 — Harness (conformance-only; no baseline)

Prompt-doc change, no numeric metric → conformance-only. All gating criteria verified on the built
tree (base 6171c2d).

| # | Criterion | Result |
|---|---|---|
| C1 | R-A `B-VER-1` @ stage-2 (own-claims + memory) | ✅ |
| C2 | R-B `B-TIME-1` @ stage-3 (both-points + discard-post-dating) + stage-7 enforcement | ✅ |
| C3 | R-C fidelity: 5th lens @ charter + `B-FID-1` @ stage-1 & stage-7 | ✅ |
| C3b | earned-clean guard + fidelity aim + spot-check-pins (the MAJOR fix) | ✅ 3/3 greps |
| C4 | R-C `B-COST-1` @ stage-5 (surprise ⇒ fidelity question) | ✅ |
| C5 | 6/6 count sites read "five"; robust sweep 0 STALE; self-test fires 4/4 on baseline | ✅ |
| C6 | 4 new rule IDs collision-free in base | ✅ |
| C7 | B-EVID-1 preserved (strengthened, not replaced) | ✅ no deletion |
| C8 | position/behavior preserved — lenses 1–4 + existing rules byte-unchanged; additive only | ✅ (stage-6 cold enumeration) |
| C9 | live == source | ✅ `diff -r` empty |
| C10 | cross-doc consistency (only count multiply-stated; all say five) | ✅ |

Stage-6 cold review verdict: CLEAN (no findings). **Verdict: PASS — all gating criteria verified.**
No advisory criteria, no regression arm. The three rules (R-A/R-B/R-C) are live in source + installed.
