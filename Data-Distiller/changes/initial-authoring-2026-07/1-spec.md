# Stage 1 — Spec: the Data-Distiller skill

## Problem — what needs to be done and why

Package the **cold multi-agent data-distillation method** — proven on the T1–T4 re-sift of the
companion-emergence experiment data (71 items, completed 2026-07-23) — as a reusable,
**domain-agnostic** Claude Code skill named `data-distiller`.

The method exists to solve a specific problem: **extracting trustworthy, source-cited factual
findings from a large corpus that no single context window can hold, without the coordinator's
judgment contaminating the findings.** A naive "read it all and summarize" fails three ways:
(1) the corpus overflows the window; (2) a single reader's priors bias what gets flagged; (3)
summaries drift into interpretation/speculation that later can't be traced to a source. The
method answers each: **decompose** the corpus into per-item analytical units; run **N independent
cold analysts** per item under an open "flag ANY aberration, cite every flag, facts only, no
cause-speculation" mandate; **cold-verify** every citation (drop the unverifiable); **merge**
into an agreement-and-recurrence-ranked super-list; **summarize** per set — all while
**coordinating nodes never read findings content** (they route on terse on-disk roll-ups only),
so the aggregation stays blind and the analysts stay the sole judges of the data.

The T1–T4 run also **survived two production failures** whose fixes are load-bearing guardrails
the skill must encode (see `DISTILLATION-METHOD-ISSUES-LOG.md`):
- a **session-limit death mid-merge** → all state on disk, deterministic filenames, idempotent
  stage re-run;
- an **OOM** from a 1.2 GB inline-image artifact (650× a text arm) three agents `Read` at once →
  size-aware pre-flight + a streaming, text-faithful slimmer *before* fan-out;
- a **persona-guard read-only tripwire** and a **plain-read of an off-limits protected path** that
  no mutation-guard catches → the brief is the only fence; read-only + off-limits clauses are
  first-class.

## Why a skill (not a one-off runbook)

The method is architecture, not domain: decompose → size/tier → analyze → verify → merge →
blind roll-up is corpus-agnostic; only the *corpus config* (what an atomic unit is, where the
legal cut points are, what's off-limits, optional prior-knowledge) is domain-specific. That is
exactly the **Layer-1 core / Layer-2 config** seam the sibling skills (`guarded-change`,
`dragonfly`) already use. Packaging it as a skill makes the method repeatable on any future
corpus, encodes the hard-won guardrails structurally (so they can't be forgotten under session
pressure), and lets the coordinator's blindness be a *property of the file layout* rather than a
discipline the operator must remember.

## Scope — what this change delivers

A complete skill folder mirroring the sibling skills' architecture:
- a **router** (`SKILL.md`) — name/description, inputs, the up-front blindness + read-only +
  off-limits rules, the stage table;
- a **methodology/reference** (`METHODOLOGY.md`) — why it exists, the **Layer-2 config contract**,
  the tree/blindness model, the agreement model, the gates, what a run produces;
- **per-stage procedure files** (`stages/`) — decompose+size, human cut-gate, analysis, verify,
  merge, roll-up/summary, restart/resume;
- a **forked charter** (`charter.md`) — the cold-analysis discipline (cite-or-drop, facts-only,
  no-cause-speculation, clean-lens-earned), forked from guarded-change's charter as dragonfly
  forked its own;
- **brief templates** — analysis / verify / merge / summary + the shared artifact-context block
  (a Layer-2 slot) + the global do-the-work-yourself + read-only/off-limits clauses;
- a **worked example config** (`examples/companion-emergence/`) — the T1–T4 Layer-2 config,
  genericized;
- a **README.md** — why it exists + how to adopt it.

The design is **owner-approved** (the plan, green-lit 2026-07-24). This change **transcribes and
structures** that design into the skill; it does not re-open the settled decisions.

## Settled design decisions this build must conform to (from the approved plan)

These are the plan's owner-approved decisions, restated as build constraints (NOT to be
re-litigated — the red-team's job is to check the *build conforms to them* and to catch internal
inconsistency, missed guardrails, and coverage gaps, not to re-argue the design):

1. **Strictly-blind coordinating nodes at every tier.** No coordinating node ever reads findings
   content; it reads only each *direct* child's terse `_status.md` roll-up + child dir/filenames.
   Every content-touch (analysis, verify, merge, summary) is a dispatched cold leaf. Blindness is
   **structural** — enforced by the file layout, not by operator discipline.
2. **Static pyramid from decomposition.** Tree height is fixed up front from corpus divisibility;
   no mid-run restructuring. Coordination tree == aggregation tree (super-list → set → global).
3. **Per-item model tiering by post-slim token size.** Haiku → Sonnet → Opus by context-fit +
   headroom and a complexity/density ceiling; prefer *subdivide + cheapest fit*; Opus is the
   irreducible reserve.
4. **Redundancy scales inversely with model strength.** Haiku items → **6** analysts; Sonnet/Opus
   items → **3**. Verify scales with it (one cold verifier per analysis list). Subdivided pieces
   each get the 6-analyst treatment on Haiku.
5. **Size handling = strategy selection (NOT "slim").** (a) redundant/irrelevant *binary* bulk →
   replace-with-descriptive-tag (streaming slimmer, original untouched); (b) analytically-relevant
   *text* bulk → subdivide into context-complete pieces + seam-aware merge; (c) irreducible →
   escalate tier. Sizing runs **after** (a), on the text that will actually dispatch (bytes ≠
   tokens; the 1.2 GB image is the cautionary case).
6. **Agreement rendered `PCT% (X/N)`** — percentage first (floored int), then fraction. Super-list
   sorts by percentage desc then recurrence desc. The denominator rides through merge → summary.
7. **Mandatory in-depth HUMAN cut-gate** for subdivided/borderline items (approve atomic unit /
   split points / overlap + the context-preservation argument) *before* dispatch. Clean-fit,
   clearly-tiered items auto-proceed.
8. **Prior knowledge = optional Layer-2 ledger, label-only.** Used only to recognize/label known
   phenomena, never to narrow the open mandate; the agent-facing copy is redacted of
   off-limits/live paths.
9. **Read-only + off-limits-path brief clauses first-class.** A mutation-guard does NOT catch
   reads → the brief is the only fence. Plus do-the-work-yourself (no sub-delegation).
10. **Static concurrency budget** computed at decompose-time (cap dispatch; serialize within cap).
11. **On-disk output structure = the nested-recursive tree** in the plan (run-root OUTSIDE the
    corpus; `tree/` machinery with per-node `_status.md`; `summaries/` for deliverables;
    `_prepared/` for R0/pieces; `config/`, `plan/`, `index.md`, `RUN.md`).
12. **Composition: standalone; fork the charter.** Document a soft handoff (distillation output →
    a dragonfly symptom ledger) with **no hard dependency**.

## Constraints

- **READ-ONLY on all reference material.** No writes under `/home/zero/Desktop/Dragonfly_Case_study/`
  or the sibling skills. Writes go only under `Data-Distiller/`.
- Skill `name:` field = `data-distiller` (lowercase-kebab); repo folder = `Data-Distiller`.
- The runner does **not** commit or push (orchestrator commits).
- Mirror the sibling skills' file architecture and house style (router/methodology/stages/charter/
  README/example-config), so the three skills read as one family.

## Prior art

- `guarded-change` skill (`~/.claude/skills/guarded-change/`) — the architecture parent
  (Layer-1/Layer-2 seam, SKILL router + METHODOLOGY + stages/ + charter, config contract,
  verbatim review-record provenance rule).
- `dragonfly` skill (`~/.claude/skills/dragonfly/`) — the second exemplar and the **fork
  precedent**: it forked guarded-change's charter into a self-contained copy (with a provenance
  header naming the source commit + what was deliberately not carried). Data-Distiller's
  `charter.md` follows that pattern.
- The T1–T4 run artifacts (`Dragonfly_Case_study/T1-T4_Results/`) — `AGENT_BRIEFS.md` (the brief
  templates to port), `DISTILLATION-METHOD-ISSUES-LOG.md` (the guardrails), `PROGRESS.md` /
  `RESUME.md` / `test_index.md` (the state-contract shapes), the `T*_summary.md` +
  `raw_findings/*_superlist.md` (the deliverable shapes).

## Expected touched files (joins every cold reviewer's context)

All under `/home/zero/Desktop/claude-code-skills/Data-Distiller/`:

```
SKILL.md
METHODOLOGY.md
README.md
charter.md
stages/stage-1-decompose-size.md
stages/stage-2-cut-gate.md
stages/stage-3-analysis.md
stages/stage-4-verify.md
stages/stage-5-merge.md
stages/stage-6-rollup-summary.md
stages/stage-7-restart-resume.md
briefs/analysis-brief.md
briefs/verify-brief.md
briefs/merge-brief.md
briefs/summary-brief.md
briefs/shared-clauses.md
examples/companion-emergence/corpus.md
examples/companion-emergence/ledger.md
examples/companion-emergence/README.md
```

Plus the guarded-change change-records for this authoring run (this loop's own provenance, not
skill content), under `Data-Distiller/changes/initial-authoring-2026-07/`:
`1-spec.md`, `1.5-criteria.md`, `2-plan.md`, `3-redteam-plan.md`, `6-redteam-code.md`,
`8-harness.md`, `decisions.md`.

## Fidelity note — loaded operational terms (for the stage-3 fidelity lens)

The load-bearing terms in this spec, pinned to their concrete mechanism (so the reviewer can
check the build implements the mechanism, not a proxy):
- **"blind coordinator"** = a node that opens only `_status.md` + globs child dir names; it never
  `Read`s any `analysis/`, `*_verified.md`, `superlist.md`, or `*_summary.md`. Mechanism, not
  aspiration: the *layout* is what makes findings unreadable to it (they live in child leaves it
  is told never to open).
- **"analyst" / "verifier" / "merge" / "summary"** = a single dispatched cold subagent
  (`general-purpose`, write-capable) doing that one job itself, no sub-delegation.
- **"size handling"** = strategy *selection* among {tag-replace, subdivide, escalate}, chosen by
  what is big — NOT a single "slim everything" step.
- **"human cut-gate"** = an actual stop-and-wait for a human's approval of unit/splits/overlap
  before dispatch — not an auto-approved log entry.
- **"agreement"** = `PCT% (X/N)` where N is the analyst count for that item's tier (6 or 3), the
  denominator preserved through merge→summary.

## No escalated fidelity findings carried in

This is the initial authoring run; there is no prior "OWNER MUST RATIFY" fidelity finding carried
forward. The approved plan is the owner-ratified design of record. (If the stage-3 red-team
surfaces a fidelity/intent gap requiring owner ratification, it HALTS to the orchestrator per RAT3
— the runner does not self-ratify.)
