# Fixtures for the behavioral conformance runs (C1, C2, C3, C3p)

Constructed, domain-neutral inputs with **known ground truth**, used to test the guards under a
cold reviewer running the post-edit vs pre-edit charter (the causal toggle). Ground truth is
externally legible: each fixture's RAT1 fields are enumerated below so the stage-8 reader can
confirm a fixture is well-formed *before* trusting a "no-flag" result (LA-NEW-1).

The RAT1 required fields (from `stages/stage-3.md` CH11 / RAT1):
1. flagged axis + options presented to the owner, **verbatim**
2. owner's response, **verbatim**, WITH a durable spot-checkable source (transcript line /
   timestamped owner entry) — the owner's *quoted words with a locus*, not a paraphrase
3. a mapping showing the owner's words **select** the recorded option **on the flagged axis**

| Fixture | RAT1 fields present? | Expected verdict (post-edit) | Tests |
|---|---|---|---|
| `A-compliant.md` | 1 ✓  2 ✓ (source cited)  3 ✓ (disambiguates) | **NOT flagged** (valid ratification) | C3(a) precision |
| `B-legit-elaboration.md` | ratified phrase + entailed expansion | **NOT flagged** (no inflation) | C3(b) / RAT2 precision |
| `C3p-sourceless.md` | 1 ✓  2 ✗ (verbatim present but **no source**, reconstructed)  3 ✓ | **FLAGGED** — missing provenance | C3p provenance sub-mode |
| `D-partial.md` | 1 ✓  2 partial (adjacent answer)  3 ✗ (does not disambiguate) | **FLAGGED** — not ratified, re-ask | C1-style negative (constructed twin of the incident) |

The incident's own records (`t4-base-loop/1-spec.md` §OWNER RULING + `3-review.md`) supply the
C1/C2 real-incident inputs; these constructed fixtures supply the precision cases (C3/C3p) and a
clean-room negative (D) that is *less self-announcing* than the incident, for the toggle fallback.
