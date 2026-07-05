# 8-harness.md — flagship-probe-2026-07 evidence record

Records the evidence gathered at stage 8. The formal blind scoring (P4 → P3) was **not
run** — the owner closed the run early (Option 2) because the P4 verifiers were pinned to
`claude-fable-5`, which became economically unavailable, and the outcome is a non-PASS in
the conservative direction (a non-discriminating baseline half; see 9-report.md,
arm-outcomes.md, decisions.md). What follows is the conformance + arm evidence that WAS
collected, plus the honest disclosures stage 6 required (conditions C-1..C-3).

Working dir: `~/probe-arms-2026-07`. Frozen criteria: gate-4 hashes in decisions.md
(1.5-criteria.md `8ff2b72c…`, 2-plan.md `e17267b1…`). Pre-arm probe tree hash
`7fcf9b78…e534`.

| Criterion | Result | Evidence |
|---|---|---|
| **P1(a)** obvious test passes as shipped | PASS | `pytest -q` → 2 passed (`conformance/P1-outputs.txt`) |
| **P1(b)** oracle exhibits the seeded symptom | PASS | `oracle/repro.py` on fixture copy → `STALE`, exit 1 |
| **P1(c)** oracle silent-on-clean | PASS | `oracle/repro.py` on corrected copy (patch applied) → `FRESH`, exit 0 |
| **P1(d)(i)** TTL decoy correct | PASS | `oracle/ttl_check.py` → correct, exit 0 (under/at/past boundary) |
| **P1(d)(ii)** hammer fire-on-known-true + clean | PASS | FIRED run 1 on the race-restored copy (≤50 bound); CLEAN across 50 runs on shipped |
| **P1(e)** per-arm-type copy listings | PASS | `conformance/P1e-listings.txt` — baseline = 7 fixture files; Dragonfly = +config +empty hunt/logs, no oracle/change files |
| **P1(f)** probe tree hash | PASS | `7fcf9b78…e534` reproduced (== gate-7 record) |
| **Canary (R3-3)** offered-skill channel closed | PASS | leg 1 pre-park: dragonfly in listing (grep=2); leg 2 post-park: absent (grep=0) |
| **Launch pin (P2)** live == source post-restore | PASS | `conformance/launch-pin.txt` — SKILL `b5e122ef…`, METHODOLOGY `04d1044c…`, both == source == pre-park |
| **Arms** 6 slots run once | PARTIAL | 3 baseline + 2 Dragonfly completed with final reports; dfly2 killed mid-run (dead-arm, not respawned — moot to the outcome) |
| **P7** integrity checks | NOT RUN | folded into the early close; the arm transcripts are preserved for any later audit |
| **P4** blind verifier scoring | NOT RUN | owner close (Fable unavailable); author read in `arm-outcomes.md` instead, conservative direction |
| **P3** pass condition | NON-DISCRIMINATING | baseline half has 0 trap-falls (needs ≥1) → fails its floor → non-discriminating; no PASS, no flip |
| **P5** label flip | NOT DONE (correct) | non-PASS → SKILL.md unchanged; `diff` live==source holds (b5e122ef…) |

## Stage-6 disclosures carried here (conditions C-1..C-3)

- **C-1 (hammer validation was augmented):** the hammer's fire-on-known-true check was run
  against a copy that is lock-removed **and** carries a jittered 0–200µs yield inside the
  cache-populate window (`oracle/race-restore.patch`). Reason: on CPython 3.14.4 a purely
  lock-removed copy cannot exhibit the read-through race by preemption within any feasible
  run bound (measured ~3e-6 per window traversal). The staleness the hammer detects is
  real staleness through unmodified store operations; only scheduling is perturbed. This
  record does **not** claim validation against a bare lock-removed copy.
- **C-2 (patch never arm-visible):** `oracle/race-restore.patch` lives under `oracle/`,
  excluded from both arm copy types (P1(e) confirmed).
- **C-3 (shipped `_now()` disclosed):** the shipped store carries a `_now()` clock
  indirection (an §A-unlisted, arm-visible idiom) added to give the oracle a call site;
  store semantics, tests, and the oracle are unchanged by it.

## Bottom line

Everything the probe apparatus was built to check — that the fixture is a fair trap, the
oracle is a real detector, the channel is clean, the arms run in a controlled phased
setup — held. The apparatus is sound and replayable. The run did not reach a PASS because
the control group did not fall for the trap, which is a property of the fixture's
difficulty, not of the harness. See 9-report.md.
