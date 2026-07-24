# Data-Distiller — methodology

A method (and a Claude Code skill that runs it) for extracting **trustworthy, source-cited factual
findings** from a **corpus too large for any single context window**, without the coordinator's
judgment contaminating the findings.

This document is the **orientation/reference spec**: why the loop exists, the two layers, the
Layer-2 config contract, the blindness/tree model, the tiering + redundancy model, the size-strategy
model, the agreement model, the gates, the on-disk state contract, and what a run produces. The
**per-stage procedure** lives in `stages/` (one file per stage) + the shared analyst discipline in
`charter.md`; `SKILL.md` is the router that walks the loop. This file is opened for orientation and
config setup — not to run a stage.

It is deliberately **project- and domain-agnostic** — nothing here assumes a particular corpus,
domain, or finding. Only the **Layer-2 corpus config** holds domain specifics.

Data-Distiller is a sibling of **guarded-change** (gated *change*) and **dragonfly** (gated
*diagnosis*): it borrows their Layer-1-core / Layer-2-config seam and their cold-subagent
independence discipline, forked (see `charter.md`), and composes with them via a soft handoff (a
distillation output can seed a dragonfly symptom ledger) with **no hard dependency**.

---

## Why this exists

A naive "read the whole corpus and summarize it" fails three ways, and each has a structural
answer here:

1. **The corpus overflows the window.** No single reader holds it all. → **decompose** into
   per-item analytical units; a static pyramid aggregates them.
2. **One reader's priors bias what gets seen.** → **N independent cold analysts per item** under an
   **open** "flag ANY aberration" mandate, then a **cold verify** of every citation; the coordinator
   never reads findings, so its expectations can't steer them (**blindness**).
3. **Summaries drift into untraceable interpretation.** → **facts-only, cite-or-drop**; agreement +
   recurrence are computed mechanically; interpretation is deferred to the human.

The method was proven on a 71-item forensic re-sift and **survived two production failures** whose
fixes are load-bearing guardrails encoded here:

- a **session-limit death mid-merge** → **all state on disk**, deterministic filenames, idempotent
  stage re-run (nothing done is lost; only the interrupted stage re-runs);
- an **OOM** from a 1.2 GB inline-image artifact three agents `Read` at once (650× a text arm) →
  **size-aware pre-flight** + a **streaming, text-faithful slimmer** before fan-out, and a **static
  concurrency budget**;
- a **persona-guard read-only tripwire** and a **plain read of an off-limits protected path** that
  no mutation-guard catches → **the brief is the only fence**; read-only + off-limits clauses are
  first-class (see `charter.md`).

---

## The two layers

- **Layer 1 — agnostic core (this doc + `SKILL.md` + `stages/` + `charter.md` + `briefs/`).** The
  loop, the blindness/tree model, the tiering + redundancy model, the size-strategy procedure, the
  agreement model, the state contract, the human cut-gate, and the shared analyst discipline. Ships
  once; knows nothing about any specific corpus.
- **Layer 2 — per-corpus config.** What an atomic analyzable unit is, where the legal cut points +
  overlap are, the artifact-context block the analysts get, the off-limits paths, an optional
  prior-knowledge ledger, and the concurrency ceiling. Supplied per corpus. This is the only place
  domain specifics live. `examples/companion-emergence/` is a worked example.

---

## The config contract (Layer 2)

A corpus config declares (see `examples/companion-emergence/corpus.md` for a worked instance):

```yaml
corpus: <name>

artifact_context: |            # the SHARED ARTIFACT-CONTEXT BLOCK given to analysis + verify leaves:
                               # what the system under test is, what each artifact type is, which
                               # fields are analytically relevant, what is legitimately in-context
                               # (so drawing on it is NOT a finding). This is a Layer-2 slot in the
                               # briefs.

atomic_unit: |                 # what ONE analyzable item is (e.g. "one run = one arm of one pass").
                               # The decompose stage expands the corpus into items of this shape.

legal_cuts:                    # for oversize TEXT items: where may a piece boundary fall, and how
  boundary: <e.g. "turn boundary; never mid-turn">
  overlap: <e.g. "1 turn of overlap each side so a cross-turn finding is visible in both pieces">

off_limits_paths:              # exact paths a leaf must NEVER open/grep, even to verify a citation.
  - <path>                     # (a mutation-guard does not catch reads — the brief is the fence.)

ledger: <path|none>            # OPTIONAL prior-knowledge ledger, LABEL-ONLY. Agent-facing copy is
                               # REDACTED of off-limits/live paths (<REAL-PATH-REDACTED>).

concurrency_ceiling: <int>     # max concurrent agents (host headroom); the static budget caps to it.
```

Rules:
- **The artifact-context block is a Layer-2 slot**, dropped verbatim into the analysis + verify
  briefs. Getting it right is how analysts know what is legitimately in-context vs. a finding.
- **Off-limits paths are named to be fenced, not to be visited.** They are text-only context that
  must never be opened. **The brief is the only protection** — no mutation-guard catches a read.
- **The ledger is optional and label-only.** Used to recognize/label known phenomena, never to
  narrow the open mandate; the agent-facing copy is **redacted** of any live/off-limits path.
- **Paths are the corpus's, read-only.** The run never writes into the corpus; all output goes to a
  run-root **outside** the corpus.

---

## The blindness / tree model

- **Strictly-blind coordinating nodes at every tier.** A coordinating node reads **ONLY** each
  *direct* child's `_status.md` (a terse done-state + one-line roll-up + counts) and **globs child
  dir/filenames**. It **NEVER** opens `analysis/*`, `*_verified.md`, `superlist.md`, or
  `*_summary.md`. **Blindness is structural** — the findings physically live in child leaf dirs the
  node is told never to open; `_status.md` is the *sole* parent-readable surface.
- **Static pyramid from decomposition.** Tree height is fixed up front from corpus divisibility; no
  mid-run restructuring. The **coordination tree == the aggregation tree** (item super-list → set
  summary → optional global summary).
- **Every content-touch is a dispatched cold leaf.** Interior nodes only route (cheap); the
  expensive reasoning is at the leaves. Analysis, verify, merge, and summary are all leaves.

---

## Tiering + redundancy model

- **Per-item model tiering by post-slim token size.** After size handling (below), estimate each
  item's dispatch-token size and pick the **cheapest tier that fits with headroom**: Haiku →
  Sonnet → Opus. A within-window item may still **escalate** when judged dense/complex. **Prefer
  subdivide + cheapest fit; Opus is the irreducible reserve.**
- **Redundancy scales inversely with model strength.** **Haiku items → 6 analysts; Sonnet/Opus
  items → 3 analysts.** A subdivided item's Haiku-sized pieces each get the 6-analyst treatment.
- **Verify scales with analysis.** **One cold verifier per analysis list** (6 analyses → 6
  verifiers; 3 → 3).

---

## Size-strategy model (selection, not "slim")

Pre-flight **every** artifact (`du -h`; never `Read` a multi-hundred-MB file — inspect with
`wc -l` / `head -c` / max-line-length first). Then choose a strategy **by what is big** — this is a
selection among **three** strategies, not a single "slim everything" step:

- **(a) redundant/irrelevant BINARY bulk → replace-with-descriptive-tag.** A **streaming** slimmer
  (line-by-line, never loading the whole file) replaces the oversize irrelevant blob (e.g. an inline
  base64 image) with a **descriptive placeholder tag** that preserves the analytical signal (states
  what the blob was, so a hallucinated description is still detectable), keeping all relevant TEXT
  verbatim. The **original is untouched**; the slimmed copy goes to `_prepared/`.
- **(b) analytically-relevant TEXT bulk → subdivide.** Split into **context-complete pieces** on
  legal boundaries with overlap (Layer-2 `legal_cuts`), distill each piece, then **seam-aware
  merge**. Requires the human cut-gate.
- **(c) genuinely irreducible → escalate the model tier** (toward the Opus reserve).

**Sizing runs AFTER (a)**, on the text that will actually dispatch — **bytes ≠ tokens**; the 1.2 GB
image whose analytically-relevant output field was tiny is the cautionary case.

---

## Agreement model

Every merged super-list entry renders agreement as **`PCT% (X/N)`** — the **percentage first**
(floored to an integer: 1/3→33%, 2/3→66%, 3/3→100%; 1/6→16%, 2/6→33%, 3/6→50%, 4/6→66%, 5/6→83%,
6/6→100%), then the **raw fraction**. N is the item tier's analyst count (6 or 3). The percentage is
the **cross-tier comparator** — it makes a 6-analyst item's agreement comparable to a 3-analyst
item's. Alongside agreement, **recurrence** = the number of non-sequential distinct occurrences of
that kind of aberration across the item.

- **Super-list primary sort = percentage desc, then recurrence desc.**
- The **denominator N rides through** merge → set summary → global summary (so a 33% is always
  legible as 2/6 vs 1/3).

---

## Gates

- **Mandatory in-depth HUMAN cut-gate** (stage 2). No subdivided/borderline item dispatches until a
  human has **approved** the atomic-unit choice, the split points, the overlap, and the **argument
  that each cut preserves context**. Scope: subdivided items + sizer-flagged borderline items;
  **clean-fit, clearly-tiered items auto-proceed**. This is the method's **representativeness gate**
  — a wrong cut wrecks the whole item. If the human **revises** the splits, the item's provisional
  tree skeleton + concurrency budget are **re-derived** before dispatch.

---

## The on-disk state contract

- **All state is on disk.** Deterministic filenames → "already produced?" is a **path check**
  (stage-done-iff-output-exists). **Trust files over any cursor** on disagreement. A HARDSTOP
  mid-stage → re-run that whole stage fresh; nothing completed is lost, only the interrupted stage
  re-runs.
- **Node identity = directory path.** Restart reads the node's own dir. An **empty leaf dir IS the
  "not done yet" marker**; the whole static `tree/` skeleton is created at decompose-time.
- **Liveness (advisory, host-specific).** Watchdog re-kick on usage-reset, hung-agent kill+respawn,
  and pacing/serialize-under-load are documented operational guidance, not part of the agnostic
  gated core (they depend on the host's session/usage mechanics). See `stages/stage-7-restart-resume.md`.

---

## What a run produces (the run-root, OUTSIDE the corpus)

```
<run-root>/                 ← OUTSIDE the corpus (corpus stays strictly read-only)
├─ RUN.md                   ← self-contained runbook + restart procedure (apex resume)
├─ index.md                 ← dispatch index: static tree + per-item {artifact paths, config, tier,
│                             split-plan, degraded flags}
├─ config/                  ← Layer-2 for this corpus
│   ├─ corpus.md            ← artifact-context block, atomic unit + legal cuts + overlap, off-limits
│   └─ ledger.md            ← OPTIONAL, redacted, agent-facing prior knowledge
├─ plan/
│   ├─ budget.md            ← static concurrency budget (peak agents, ceiling)
│   ├─ decisions.md         ← append-only: gates, tier calls, human overrides, guard-trips
│   └─ cut-gate/            ← per subdivided/borderline item: approved unit/splits/overlap + the
│                             context-preservation argument (the human-gate audit trail)
├─ _prepared/               ← derived INPUTS, not findings: R0 tag-replaced heavy artifacts +
│   └─ <item>/…               subdivision pieces + overlap manifests
├─ summaries/               ← the DELIVERABLES, collected: summary-tier roll-ups only
│   ├─ <SET>_summary.md       (set summaries, any global/cross-set summary). The summary cold-leaf
│   ├─ global_summary.md      writes here directly; these are the canonical copies.
│   └─ <SET>_by-arm_crossref.md
└─ tree/                    ← working machinery — recursive nodes mirroring the static pyramid
    ├─ _status.md           ← apex roll-up (sole parent-readable surface)
    └─ <node>/              ← recursive coordinating node (a SET, or a sub-coordinator slice)
        ├─ _status.md       ← points at its summaries/<node>_summary.md by name
        └─ <child>/…        ← recurse to ITEM/PIECE leaves:
            ├─ _status.md
            ├─ superlist.md            ← item merge leaf output (seam-aware if subdivided); STAYS here
            ├─ analysis/ A.md…C.md (or A…F) + *_verified.md
            └─ pieces/ piece-01/{analysis/…, superlist.md} …   (only if subdivided)
```

Conventions that make the decisions structural, not disciplinary:
- **Blindness is structural.** A parent reads ONLY each direct child's `_status.md` + globs child
  dir names; it never opens summary/superlist/analysis.
- **Read-only corpus inviolate.** `_prepared/` holds the ONLY transformed copies; originals
  untouched.
- **Static tree = static dirs.** An empty leaf dir IS the "not done yet" marker.
- **Summaries out, super-lists in.** Summary-tier deliverables → `summaries/`; per-item super-lists
  (one working artifact per item) stay at their item nodes in `tree/`.

`plan/decisions.md` is the append-only gate/decision log for a *distillation run* (distinct from the
guarded-change change-records that authored this skill).
