# Stage 2 — Plan: how to build + measure

## Build approach (files, mirroring the sibling skills)

Author under `Data-Distiller/`, house style matched to `guarded-change` + `dragonfly`
(router → methodology → per-stage files → forked charter → briefs → example config → README).

1. **`SKILL.md`** — the router. YAML front-matter (`name: data-distiller`, a triggering
   `description`). Body: the purpose line; **up-front** blindness + read-only + off-limits rules
   (C9); Inputs (corpus + Layer-2 config + optional ledger); the stage table pointing at
   `stages/`; the blind-node contract in one paragraph; the stop-for-human list; a self-check /
   dogfooding note. Mirrors `guarded-change/SKILL.md` structure.

2. **`METHODOLOGY.md`** — the reference. Why it exists (the three founding failures + the two
   production incidents); the two layers; the **Layer-2 config contract** (what a corpus config
   must declare: artifact-context block, atomic unit + legal cuts + overlap, optional ledger,
   off-limits paths, concurrency ceiling); the tree/blindness model; the model-tiering + redundancy
   model; the size-strategy trichotomy; the agreement model (`PCT% (X/N)`, floor, sort,
   denominator-through-merge); the gates (human cut-gate); the on-disk state contract; what a run
   produces. Mirrors `guarded-change/METHODOLOGY.md`.

3. **`stages/`** — one file per stage of the *distillation* loop (distinct numbering from the
   guarded-change authoring loop):
   - `stage-1-decompose-size.md` — decompose corpus → items; pre-flight `du -h` every artifact;
     size-strategy selection {tag-replace | subdivide | escalate}; the streaming slimmer
     procedure + preventive checks (never `Read` a >~50 MB file; `wc -l`/`head -c`/max-line-length
     first); post-slim token estimate → tier (Haiku/Sonnet/Opus) + redundancy (6/3); write
     `{tier, split-plan, degraded}` per item to `index.md`; compute the static concurrency budget →
     `plan/budget.md`; build the static `tree/` skeleton.
   - `stage-2-cut-gate.md` — the mandatory in-depth HUMAN cut-gate for subdivided/borderline items
     (approve unit/splits/overlap + context-preservation argument → `plan/cut-gate/`); clean-fit
     clearly-tiered items auto-proceed. **Feedback path (per stage-3 L1/CH8-3):** the `tree/`
     skeleton + `plan/budget.md` that stage-1 builds for a *subdivided* item are **provisional** —
     if the human **revises** split points/overlap at the gate, the stage explicitly **re-derives**
     that item's piece dirs and **recomputes** the concurrency budget from the approved splits
     before any dispatch (a rubber-stamp with no change leaves them as-is). Stage-1 marks
     subdivided items' skeleton/budget as provisional-pending-gate so nothing dispatches against a
     stale split.
   - `stage-3-analysis.md` — dispatch N cold analysts (6 Haiku / 3 Sonnet-Opus) per item; open
     "flag ANY aberration, cite every flag, facts only, no cause speculation" mandate; outputs to
     leaf `analysis/`.
   - `stage-4-verify.md` — one cold verifier per analysis list; re-check each citation; drop the
     unverifiable; outputs `*_verified.md`.
   - `stage-5-merge.md` — one merge leaf per item; dedup + agreement (`PCT% (X/N)`) + recurrence →
     `superlist.md`; seam-aware for subdivided items; sort percentage desc then recurrence desc.
   - `stage-6-rollup-summary.md` — blind coordinating node dispatches a cold summary leaf per set
     (facts + counts, no conclusions) → `summaries/`; optional cross-set/global summary.
   - `stage-7-restart-resume.md` — the on-disk state contract: per-node `_status.md`, deterministic
     filenames, stage-done-iff-output-exists, trust-files-over-cursor, HARDSTOP → re-run that whole
     stage fresh; `RUN.md` apex runbook. **Liveness (per stage-3 CH8-6 decision):** the durability
     half (resume-from-disk) is a **gated** property (C2). The **liveness** half from RESUME.md —
     watchdog to re-kick on usage-reset, hung-agent (>Nmin no-completion) kill+respawn, pacing/
     serialize-under-load — is included as **documented operational guidance (advisory, environment-
     specific)**, NOT a gating criterion: it depends on the host's session/usage mechanics, which
     are not corpus-agnostic. This decision is stated explicitly so the omission from the gated set
     is a choice, not an oversight. (The **stale-cursor-edit** gotcha is designed out by per-node
     `_status.md` + trust-files-over-cursor — no single global cursor to stale-edit.)

4. **`charter.md`** — **forked** from `guarded-change/stages/charter.md`, adapted to distillation's
   analysis discipline: cite-or-drop, facts-only, no-cause-speculation, read-only/off-limits,
   do-the-work-yourself. This is the *analyst/verifier* discipline (distinct from a guarded-change
   *reviewer* charter) but forked from the same trustworthy-aggressive-review core. **Provenance
   header must have BOTH parts (per stage-3 F2), as dragonfly's fork does:** (i) the source commit
   (`Guarded_change/stages/charter.md @ <sha>`), and (ii) an explicit **"deliberately not carried"**
   enumeration (e.g. the reviewer-specific five-lens framing, the position/concurrency lenses, the
   coverage-challenge/label-audit stage-3 additions — none of which belong in an analyst charter) —
   the not-carried note is what makes the fork auditable. **Nitpick fix (per stage-3):** recast
   "clean-lens-earned" for the analyst context — a **no-flags analysis result must be earned by
   showing the coverage swept** (which artifacts/turns were combed), the analyst-charter analog of
   "a clean factual lens must be earned with citations."

5. **`briefs/`** — port the AGENT_BRIEFS templates: `analysis.md`, `verify.md`, `merge.md`,
   `summary.md`, and `shared-clauses.md` (the shared artifact-context block as a Layer-2 slot + the
   global do-the-work-yourself + read-only + off-limits clauses). Genericized (placeholders where
   the T1–T4 copies had companion-emergence specifics). **This is an ADAPTATION, not a literal
   preservation (per stage-3 F1)** — the T1–T4 templates encode the *old* method (fixed "Sonnet; 3
   independent"; merge rendered raw `[agreement=N]` sorted agreement-first). The ported briefs MUST
   instead: (i) carry **tier-driven count + model slots** (6 analysts @ Haiku / 3 @ Sonnet-Opus;
   one verifier per list) rather than a hardcoded "3 Sonnet"; (ii) render agreement as **`PCT%
   (X/N)`** (percentage first, floored int, then fraction); (iii) sort the super-list **percentage
   desc, then recurrence desc**; (iv) preserve the denominator N through merge→summary. A literal
   "genericize the placeholders" port that keeps raw-count/agreement-first would resurrect the old
   method and contradict decisions 4 & 6 — the briefs are **changed**, not preserved. The
   read-only / off-limits / do-the-work clauses ARE preserved verbatim-in-spirit (genericized
   paths). **Redaction:** any live protected path is redacted to `<REAL-PATH-REDACTED>` in
   agent-facing copies (decision 8 / issues-log #3; verified by C11).

6. **`examples/companion-emergence/`** — the worked Layer-2 config, genericized from the T1–T4 run:
   `corpus.md` (artifact-context block, atomic unit + legal cuts + overlap, off-limits paths),
   `ledger.md` (redacted prior-knowledge example), `README.md` (how this example maps to the
   contract).

7. **`README.md`** — why it exists + the founding failures + how to adopt + relationship to the
   sibling skills (the composition/soft-handoff note).

**Order of build:** METHODOLOGY + charter first (they anchor the vocabulary), then SKILL router,
then stages, then briefs, then example, then README. Cross-file consistency (C8) is maintained by
authoring the shared-rule values (agreement format, redundancy counts, layout names, blindness
rule) once as canonical strings and reusing them verbatim.

## Instrumentation — what the skill must expose so the criteria are checkable (CP3)

The criteria are behavioral properties of an *executing* skill; the skill must make them
observable **by construction** (this is instrumentation added at build time, not after):
- **Blindness (C1)** observable because findings live in child leaf dirs the coordinator is told
  never to open, and the only parent-readable surface is `_status.md` — so a coordinator
  transcript can be checked for zero findings-file reads. The skill must state this as the *sole*
  parent-readable surface (structural, greppable).
- **Restart (C2)** observable because filenames are deterministic and stage-done ≡ output-file
  exists — so "what's next" is a pure disk function. The skill must specify the exact filenames.
- **Agreement (C3)** observable because the merge brief emits a fixed `PCT% (X/N)` string the
  harness can parse.
- **Size routing (C4)** observable because the size stage writes the chosen strategy + tier +
  split-plan per item into `index.md`, and the slimmer writes to `_prepared/` leaving originals
  untouched (checkable by mtime).
- **Cut-gate (C5)** observable because the gate writes an approval artifact to `plan/cut-gate/`
  and the stage forbids dispatch before it exists.
- **Concurrency (C6)** observable because the budget is a written number in `plan/budget.md` and
  the dispatch rule references it.

No external telemetry is needed — the on-disk run tree *is* the instrumentation.

## Measurement — the stage-8 harness (route-(a) representative pre-ship dry-run)

Per the config's `check`: **(a) STRUCTURE** conformance + **(b) DOGFOOD DRY-RUN** on a tiny
fabricated synthetic corpus. Design:

**Synthetic corpus (fabricated under the run's scratch, NOT under any protected tree):**
- 3 small clean-fit text items (a few lines each) — exercise trio dispatch, blindness, merge,
  agreement format, concurrency, restart.
- 1 oversize **binary-bulk** item — a jsonl whose rows carry a large base64 blob (the analytically
  relevant text field tiny) — exercises tag-replace + the streaming slimmer + original-untouched.
- 1 oversize **text** item — a large plain-text artifact — exercises subdivide + the human
  cut-gate + (its two pieces) the **seam-aware merge** (a seam-straddling finding must dedup to one
  entry — C3 seam sub-check / stage-3 CH8-2).
- 1 **irreducible-oversize** item — analytically-relevant text that does not cleanly subdivide —
  exercises the **escalate-tier** third strategy (C4 / stage-3 F3), confirming it is NOT mis-routed
  to Haiku-subdivide.
- **Concurrency budget for the walk is pinned BELOW offered concurrency** (e.g. 2) so the cap
  binds and serialization is observed (C6 / stage-3 label-audit).

**Per-criterion measurement (each labeled gating criterion → an executed check with an
oracle-can-fail self-test, per H6/ST1.5f):** the exact procedures are in `1.5-criteria.md`
(C1–C8). In brief: real analyst-leaf dispatch on ≥1 item so real findings files exist → inspect
the coordinator's own transcript for zero findings-reads (C1); complete a stage, drop the cursor,
re-derive from disk (C2); real merge on fabricated verified lists → parse `PCT% (X/N)` + sort,
plus a seam-aware merge of a subdivided item's two piece-lists (C3); route the **three** oversize
artifacts — binary-bulk, text, irreducible (C4); confirm the subdivided item blocks + clean-fit
proceeds (C5); confirm budget computed + capped **and observed to bind** with the pinned-low budget
(C6); `diff -r` live vs source, with the orchestrator's post-sync outcome folded back (C7);
per-site grep of each shared rule (C8); normalized positive+absence redaction grep of the
agent-facing ledger/briefs (C11).

**Harness scaling note (representativeness — pre-declared so stage 8 is not accused of a hidden
proxy, cf. CH9):** the blindness/merge demonstration may dispatch a **reduced** analyst count
(2–3 real subagents rather than the full tier-6) to bound cost. This does **not** weaken any of
the six criteria: blindness is a property of *what the coordinator reads*, independent of how many
analysts ran; the agreement *denominator* is exercised separately with fabricated lists at known
N. The reduction is a cost bound on the *demonstration*, not a change to the governed path — and
it is recorded in `8-harness.md`. The **oracle-can-fail self-tests** are what make each check
trustworthy (an oracle that can't flag a planted violation is `verified = no`).

**H6 duty.** Every stage-8 oracle (each grep/diff/parse) is demonstrated to fire on a
known-violating input before its pass counts. Positive per-site assertions are preferred over bare
absence sweeps (C8 checks the expected value is present at each site; C3 checks the exact format
string is emitted), and text is normalized before any absence check.

## Thresholds — severity → routing (SEV1)

Standard guarded-change severity model:
- **Blocker** (build implements the wrong method / a criterion is unverifiable / a guardrail from
  the ISSUES-LOG is absent) → back to stage 1.
- **Major** (sound skill, materially wrong on a settled decision — e.g. agreement rendered
  fraction-first, or a coordinating node specified to read a summary) → back to stage 2 (plan) at
  gate 4, or stage 5 (build) at gate 7.
- **Minor** (real but local — a stage file missing a preventive check, a brief clause imprecise) →
  fix in place, proceed.
- **Nitpick** (wording/clarity) → log, proceed.

Route on the **reviewer's** stated severity (SEV3); a demotion of blocker/major needs the human
tie-break (relayed via the orchestrator under RAT3). **Iteration cap (SEV4):** 2 bounces at the
same gate on the same finding class → HALT to the orchestrator for a human tie-break.

No regression metrics (greenfield, conformance-only) — `metrics: []`. All eleven criteria are
conformance criteria; the **nine gating** ones (C1–C8, C11) must be `verified = yes` (or carry a
named risk-acceptance) for accept. C9 (up-front placement) and C10 (behavior-preservation, N/A
greenfield) are advisory.

## Fidelity — no new mechanism substitutions introduced

The plan implements the plan's own mechanisms (blind layout, size-strategy selection, tiered
redundancy, `PCT% (X/N)`, human cut-gate). It introduces **no proxy** for any owner term (see the
spec's pinned-terms list). The one honesty flag carried forward to stage 8: **C7 live==source**
may be completed by the orchestrator's sync rather than the runner — declared here, not hidden.
