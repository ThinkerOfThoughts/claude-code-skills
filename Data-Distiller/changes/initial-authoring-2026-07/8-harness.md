# Stage 8 — Harness (conformance verdict)

Greenfield build → **conformance-only** (no stage-0 baseline, no regression). Measures the built
skill against the frozen `1.5-criteria.md` (11 criteria; 9 gating C1–C8+C11, 2 advisory C9,C10).

- **Criteria freeze (FRZ) verified:** `1.5-criteria.md` sha256 = `084a75df…4405` — **matches** the
  gate-4 frozen hash in `decisions.md`. No post-freeze edit; all PASSes are against the frozen bar.
- **Method:** (a) STRUCTURE / document-invariant checks + (b) DOGFOOD DRY-RUN on a fabricated
  synthetic corpus (3 clean-fit text items + 1 oversize binary-bulk jsonl + 1 oversize text item +
  1 irreducible-oversize item), each **gating** criterion checked by an executed check WITH an
  **oracle-can-fail self-test (H6)** — the same checker is shown to FIRE on a planted-violating
  input before its PASS counts. Harness: `scratchpad/harness.py` (self-tests inline). The C3
  execution path additionally ran a **real merge-leaf subagent** following `briefs/merge-brief.md`.
- **Harness-defect log (H6 — a defective check is fixed in place, not a loop restart):** the first
  harness run surfaced **three defects in the harness itself** (not the skill): (i) demo tier-fit
  thresholds set so high the fabricated oversize files "fit" and never routed → lowered; (ii) a
  buggy C3 sort assertion comparing recurrence across different percentage bands → rewritten to a
  correct band-aware ordering check; (iii) the blind-walk descended into leaf `analysis/` dirs →
  restricted to child NODE dirs (those with their own `_status.md`). All fixed in place; the second
  run passed clean. These were oracle bugs, not skill findings.

## Per-criterion verification table (H7)

| # | Criterion | Gating? | Path exercised | Verified by execution? | Evidence | Result |
|---|---|---|---|---|---|---|
| **C1** | Blindness (coordinator reads only `_status.md` + globs) | gating | Real run-tree with real findings files (`analysis/A.md`, `A_verified.md`, `superlist.md`); a coordinator walk following the skill | YES | `harness.py` C1: blind walk opened 3 files, findings-reads=`[]`; **self-test FIRED** — a non-blind walk that peeks at `superlist.md` was flagged. | **PASS** |
| **C2** | Deterministic restart (done-iff-output-exists, from disk) | gating | Complete a stage, drop cursor, re-derive next from disk only | YES | C2: analysis complete → next=`verify` (analysis not re-run); **self-test FIRED** — deleting one completed `C.md` made resume re-dispatch `analysis`. | **PASS** |
| **C3** | Agreement `PCT% (X/N)` + sort + seam reconciliation | gating | (i) deterministic floor/format/sort/seam logic; (ii) **real merge-leaf subagent** on N=6 fabricated verified lists | YES | C3 harness: all floor cases correct, sorted %-desc, seam(4/6,3/6)→`66% (4/6)` (greater-of, never sum); **self-test FIRED** on `50% (2/3)`, on fraction-first `(2/6) 33%`, and on a summed seam. **Real leaf** wrote `100% (6/6)`, `66% (4/6)`, `33% (2/6)` — floors correct, %-first, sorted, no fraction-first, Z recurrence=2. | **PASS** |
| **C4** | Size-strategy routing (3 strategies + tier) | gating | Route a fabricated binary-bulk jsonl, oversize text, irreducible item, and a small item | YES | C4: binbulk→`tag-replace`, bigtext(has legal cuts)→`subdivide`, irreducible(no cuts)→`escalate/opus`, small→`clean-fit`; original binbulk **untouched** (mtime+size); **self-test FIRED** — the small item did NOT route to any special strategy (checker distinguishes all four). | **PASS** |
| **C5** | Human cut-gate fires (block until approval; clean-fit proceeds) | gating | A subdivided item with/without an approval record; a clean-fit item | YES | C5: subdivided-no-approval **blocked**=True; clean-fit **proceeds**=True; after writing the approval record it proceeds; **self-test FIRED** — dispatch-before-record is caught. | **PASS** |
| **C6** | Concurrency cap computed + binds (serialize within cap) | gating | Simulated dispatch with budget pinned BELOW offered concurrency | YES | C6: budget=2, offered=18 → observed **peak in-flight=2**, cap binds; **self-test FIRED** — budget=1 flags a planted 2-in-flight state. | **PASS** |
| **C7** | live == source | gating | `diff -r ~/.claude/skills/data-distiller` vs repo `Data-Distiller/` (excl. `changes/` + authoring config) | YES | Staged the live runtime copy (19 files) and ran `diff -r` → **zero diff**. See loop-close note below. | **PASS** (at stage-8 time) |
| **C8** | Cross-file rule consistency (per-site) | gating | Per-shared-rule grep across all skill files | YES | C8: redundancy `Haiku=6` in 6 files, `PCT% (X/N)` in 9 files, size-trichotomy in 7 files; **0 contradictions**; **self-test FIRED** — a planted `Haiku→5 analysts` file was flagged. (Confirmed independently by the stage-6 reviewer's C8 table: zero mismatch.) | **PASS** |
| **C11** | Agent-facing ledger/brief redaction | gating | Scan briefs/ + example ledger.md + corpus.md for live protected paths | YES | C11: 7 agent-facing files scanned, **0 live-path leaks**, placeholder present; **self-test FIRED** — a planted `~/Downloads/Phoebe/...` path was flagged. | **PASS** |
| **C9** | Critical rules up front in SKILL.md | **advisory** | Placement check in SKILL.md | YES | C9: blindness/read-only/off-limits all appear **before** the Loop/stage-table (char 3123); self-test fires if rules appear only after. | **PASS** |
| **C10** | Behavior-preservation (moved/removed) | **advisory** | — | N/A | Greenfield — no prior version; nothing moved/removed. Recorded explicitly, not silently dropped. | **N/A** |

## Consumer citation spot-verify (CH6)
Spot-checked a sample of the stage-6 reviewer's cited claims against the files: charter.md:40
("A no-flags result must be earned by showing coverage"), stage-5 floor table (`1/6→16% …`),
merge-brief `percentage FIRST` with zero `agreement=N` raw-count strings, analysis-brief `Haiku → 6`
(F1 landed), charter fork header carries both `@ 8d73e5d` + "Deliberately NOT carried" (F2), the
L-1 seam rule (`GREATER of the two`), M-1 (`Also write RUN.md`), L-2 (`borderline: yes`). All held.

## Verdict
**CONFORMANT — all 9 gating criteria `verified = yes` by execution, each with a valid
oracle-can-fail self-test; both advisory criteria dispositioned (C9 PASS, C10 N/A).** No gating
criterion deferred, proxied, or silently dropped. No named risk-acceptance required. Regression:
not applicable (greenfield, conformance-only).

**Route: CLEAN → done** (subject to the two operator carry-forwards below, neither a defect).

## Carry-forwards for the orchestrator (declared, not hidden)
1. **C7 loop-close.** C7 passed against the live copy the runner staged at stage-8 time. The
   **orchestrator owns the authoritative re-sync + re-`diff -r`** after any post-harness change and
   at commit, folding that outcome back here — a live copy that drifts from the committed source
   would invalidate C7 (criteria C7 loop-close clause). If the orchestrator prefers to own the
   install entirely, it can remove the runner-staged `~/.claude/skills/data-distiller/` and re-stage
   from the committed tree, then re-run the one-line `diff -r`.
2. **Charter fork sha.** `charter.md` cites `Guarded_change/stages/charter.md @ 8d73e5d` — the
   `claude-code-skills` repo HEAD / last commit touching that file at build time (verified in-repo).
   A stage-6 reviewer flagged it "unverifiable" only because its sandbox wasn't cd'd into the repo;
   it is verifiable in the repo and needs no change.

## Orchestrator verification + C7 loop-close — 2026-07-24
Main session independently re-verified before commit: file scope (19 runtime files, all under
`Data-Distiller/`; no reference material or sibling skill mutated); the shared rules present at real
locations (output tree `summaries/`/`_status.md`, `PCT% (X/N)`, Haiku=6/Sonnet-Opus=3, blindness);
gate log internally consistent.
**C7 authoritative re-diff (loop-close):** `diff -rq --exclude=changes
--exclude=guarded-change.data-distiller.md ~/.claude/skills/data-distiller Data-Distiller` → **zero
diff**. C7 CLOSED at commit time. Committed to main + pushed by the orchestrator on owner (Roy)
instruction, 2026-07-24.
