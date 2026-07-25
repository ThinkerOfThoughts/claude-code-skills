# CP3 behavioral fixtures — Architect stage-8 conformance harness

Fabricated inputs authored for the stage-8 harness of the Architect authoring run
(`initial-authoring-2026-07`). Each behavioral criterion (B1, B1b, B2, B3, B4, B5, B6, B7)
gets a fixture and an **intact / reducing twin** so the oracle-can-fail self-test (ST1.5f) can
run: the oracle must be shown to fire on the known-violating input AND *not* fire on the intact
twin (it discriminates, it does not fire on everything).

**These are fabricated, NOT the real Architect plan.** The real-plan dogfood is a separate later
step the orchestrator runs. Every fixture below is a made-up planning node in a made-up domain,
sized tiny.

| Dir | Criterion | Known-violating input | Intact / reducing twin |
|---|---|---|---|
| `B1-floor/` | B1 — floor replay (fixed-list §4 removed) | `holed/plan.md` (spine §4 gone) | `intact/plan.md` (§4 present) |
| `B1b-generative/` | B1b — generative tier (off-list load-bearing section removed) | `holed/plan.md` | `intact/plan.md` |
| `B2-coverage/` | B2 — two-pass total coverage (root + seam holes) | `tree/` root plan w/ root hole + seam hole | `tree-clean/` (no planted holes) |
| `B3-scaledown/` | B3 — small task, single pass, leaf | `run/` (leaf, no children) | (discriminates vs B4's decompose) |
| `B4-scaleup/` | B4 — large task, recursive + top-level gate | `run/` (topgate gate) | topgate withheld vs supplied |
| `B5-template/` | B5 — template reuse + back-propagation | matching node + git catalog | no-match / no-fix twin |
| `B6-context/` | B6 — context economy + recursive orch + restart | `run/` (2-level tree) | absent-output node re-runs; sibling-enlarged twin |
| `B7-convergence/` | B7 — convergence guard on non-reducing recursion | `pathological/` (child ≥0.8× parent) | `reducing/` (child <0.8× parent) |

Config context shared with the cold critics (fabricated Layer-2) lives in each fixture's
`config.md`. Dry-run working dirs / scratch git catalogs live under `../8-harness-runs/`, never
inside a target repo.
