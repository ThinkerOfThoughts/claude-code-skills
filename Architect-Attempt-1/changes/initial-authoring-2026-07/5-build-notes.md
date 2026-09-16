# Stage 5 — build notes (Architect authoring)

Built the `architect` skill under `Architect/` per the frozen `{1-spec, 1.5-criteria, 2-plan}`,
mirroring the sibling architecture (Guarded_change primary; Dragonfly for the charter-FORK provenance
blockquote + mnemonic rule-IDs; Data-Distiller for stage-file house style, disk-as-instrumentation, and
the coordination-tree==aggregation-tree orchestration). Build order followed the plan: charter →
METHODOLOGY → stages → SKILL (router, last) → templates/seed → examples → README.

## Files built

| Path | Purpose |
|---|---|
| `stages/charter.md` | Forked cold-review charter (provenance blockquote naming `Guarded_change/stages/charter.md @ 8d73e5d`, carried-whole + ADDED sixth **Completeness** lens with earned-clean clause) |
| `METHODOLOGY.md` | Orientation/reference: why it exists; Layer-1/Layer-2 split; config contract (run-root OUTSIDE any target repo, off-limits, required_sections); 7-section spine verbatim; completeness mechanic (3 tiers + 2-pass gate); recursion + recursive-orchestration (ORC/ECON/COV); on-disk run tree; **Stage index**; **cross-file rule index** (mnemonic-ID table = S2/SC2 instrumentation) |
| `stages/stage-1-frame-template-match.md` | Frame node + catalog match/instantiate-or-create-new; run-root + first-run catalog seed |
| `stages/stage-2-draft-node.md` | Fill the 7-section spine + Layer-2 required sections + proposed granularity (leaf or children+seams) |
| `stages/stage-3-completeness-critic.md` | 3 independent cold agents, Completeness lens, skeleton-whole — gate #1 |
| `stages/stage-4-adversarial-redteam.md` | 3 independent cold agents, full six lenses, poke holes — gate #2 |
| `stages/stage-5-gate.md` | Route by worst finding across both passes; severity table; gate-bounce cap; GBP |
| `stages/stage-6-granularity-decompose.md` | Granularity leaf-vs-decompose; top-level-only human gate; convergence guard (DEC, 0.8×/2-level bound); sub-orchestrator spawn + recurse; back-propagation |
| `stages/stage-7-assemble.md` | Collate gated-clean tree → `assembled-plan.md`; GBP made structural |
| `stages/stage-8-restart-resume.md` | On-disk state contract (RST); RUN.md apex runbook |
| `SKILL.md` | Router: `name: architect`; pushy angle-bracket-free description (954 chars); inputs; **rules up front (completeness / two-pass / gate-before-present) BEFORE the stage table** (S7); stage table; scale/caps; stop-for-human + RAT3; self-check/dogfooding |
| `templates/seed/README.md` | Skeletonize/match/reuse/back-propagate mechanism; git-tracked user-space catalog `~/.claude/architect/templates/`; first-run bootstrap |
| `templates/seed/generic-node.md`, `decomposition-node.md`, `leaf-task-spec.md` | Seed skeletons (S5 non-empty) |
| `examples/authoring-a-skill/planning.md`, `README.md` | One worked Layer-2 config (the dogfood plan-type) |
| `README.md` | Family-convention landing page |

## Instrumentation for the structural criteria (S1–S7)
- **S1** — `quick_validate.py Architect` → **exit 0** ("Skill is valid!"); description 954 chars, no
  angle brackets, `name: architect`, only `{name, description}` keys.
- **S2/SC2** — **mnemonic-ID cross-file index** in `METHODOLOGY.md` ("Cross-file rule index"); every
  shared rule (GBP, PASS1/PASS2/PASS-ORD, CMP/CMP2, SPN, COV, ORC/ECON, GRN, TOP, CAP, DEC, TPL/TPL3,
  RST, RAT3) carries a stable ID greppable across SKILL/METHODOLOGY/stages/charter. Spot-checked: each
  ID appears in ≥3 files with a consistent operative claim; no "either pass" contradiction of GBP.
- **S3** — stage table uses resolvable relative paths (all 8 resolve); charter provenance blockquote in
  fixed greppable form ("Forked from"); Completeness lens + earned-clean clause present.
- **S4** — 7-section spine verbatim in METHODOLOGY (§4 "Outputs & artifacts … with their locations");
  Layer-2 hook + generative-critic clause present.
- **S5** — `templates/seed/` non-empty (3 skeletons + README); mechanism doc greps for the user-space
  path + "git" + "back-propagat".
- **S6** — config contract states required_sections, off_limits_paths, catalog, and "run-root … OUTSIDE
  any target repo" in a fixed section.
- **S7** — rule block at SKILL.md line 15; stage table at line 63 → rule-block offset < stage-table
  offset.

## DEC concrete bound (per the gate-4 in-place fix folded into the frozen criteria, B7)
The convergence guard's numeric bound is declared in the skill: **if two consecutive levels do not
reduce granularity — a child node's estimated leaf-count / work-size is ≥ 0.8× its parent's — the branch
escalates** (`decisions.md` escalation / halt). Stated identically in `SKILL.md`, `METHODOLOGY.md`
(DEC), and `stages/stage-6-granularity-decompose.md`.

## SCOPE FLAG — the behavioral fixtures (CP3) are NOT built in this run (surfaced, not silently decided)
`2-plan.md` (CP3, "Instrument before you build") designates the behavioral fixtures (B1 §4-removed +
intact twin; B1b off-list generative + intact twin + why-load-bearing note; B2 multi-node + planted
root/seam holes; B3 small; B4 large + topgate; B5 seed-matching node + scratch git catalog; B6 ≥2-level
tree + HARDSTOP/resume; B7 pathological + reducing twin) as **stage-5 deliverables** under
`changes/initial-authoring-2026-07/fixtures/`. They are **not** built here, because the orchestrator's
stage-5 charter scopes this run to the skill files and **STOP before stage 8 (harness)**, and frames the
fixtures/execution as **stage-8 planning** (return item 6: "which frozen criteria will need execution").
This is a genuine divergence between the frozen plan's CP3 and the orchestrator's operational
partition — **surfaced to the orchestrator, not resolved unilaterally**. If the stage-6 cold reviewer
raises the omission at major-or-worse, gate 7 routes it as a **stop-for-human** (RAT3) for the
orchestrator to rule on (build fixtures now vs. as part of the stage-8 harness run). The skill itself is
complete and self-consistent without them; the fixtures are stage-8 test *inputs*, not skill content.
