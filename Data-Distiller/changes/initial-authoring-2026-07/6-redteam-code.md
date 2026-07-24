# Stage 6 — Red-team of the built code (VERBATIM RECORD)

Cold, independent review of the 18 built skill files against the frozen {1.5-criteria, 2-plan} +
the approved design + the issues-log + the sibling architecture. Verbatim record per the provenance
rule; the author's disposition + routing live in `decisions.md`.

- **Reviewer agent type / model:** `general-purpose` cold subagent (no shared context), Claude
  Opus 4.8 (`claude-opus-4-8`).
- **Reviewed scope (mechanical, ST6d):** greenfield build — `git add -N Data-Distiller/ && git diff`
  over the 18 skill files (excluding `changes/` and the pre-existing `guarded-change.data-distiller.md`).
  `git diff --stat` = 20 files / 1236 insertions (18 skill files + README + the config already present).
- **Context list given (closed set):** the 18 built skill files + frozen `1.5-criteria.md` + `2-plan.md`
  + the approved plan + DISTILLATION-METHOD-ISSUES-LOG.md + AGENT_BRIEFS.md + guarded-change &
  dragonfly charters.
- **Reviewer confirmed the criteria/plan hashes match the frozen values** (`1.5-criteria.md` =
  084a75df…4405; `2-plan.md` = 6807fea0…a639) — no post-freeze drift.
- **Charter given:** the analyst/reviewer core (five lenses + discipline + spot-verify + provenance)
  + the position lens (C9) + the stage-6 mechanical-diff duty + the specific consistency/fix checks
  (C8 across all files; F1/F2/C11 landed; guardrail + trichotomy coverage). Full prompt in the run
  transcript; its load-bearing structure is reproduced above and the reviewer's output is below.

---

## REVIEWER VERBATIM OUTPUT

## COLD RED-TEAM REVIEW — Data-Distiller skill (stage-6 build red-team)

### 1. Provenance block

**Reviewer:** cold independent subagent (general-purpose), model claude-opus-4-8. No shared context with the author.

**sha256 of every file read:**

Skill files under review:
```
8b62e82d…581c  SKILL.md
d931b611…330a  METHODOLOGY.md
f3791564…db20  README.md
ff671d07…6de1  charter.md
630923f6…b7db  stages/stage-1-decompose-size.md
b21cee4b…b611  stages/stage-2-cut-gate.md
ae5a5ea9…8c58  stages/stage-3-analysis.md
6e4e3610…ab60  stages/stage-4-verify.md
3c858ea9…7ef1  stages/stage-5-merge.md
0007134b…5caf  stages/stage-6-rollup-summary.md
5bcdbc14…eec2  stages/stage-7-restart-resume.md
08d2b776…a416  briefs/analysis-brief.md
410f710c…53dc  briefs/merge-brief.md
470368a4…4872  briefs/shared-clauses.md
138de051…5afe  briefs/summary-brief.md
8455c1c5…190d  briefs/verify-brief.md
fb48b05a…f255  examples/companion-emergence/corpus.md
8754bd1d…1091  examples/companion-emergence/ledger.md
564b1215…5135  examples/companion-emergence/README.md
```
Criteria / plan / sources:
```
084a75df…4405  1.5-criteria.md   (MATCHES frozen hash in decisions.md ✓)
6807fea0…a639  2-plan.md         (MATCHES frozen hash ✓)
430e00c0…bf10  your-understanding-is-correct-wise-bee.md (approved design)
af5da9aa…6846  DISTILLATION-METHOD-ISSUES-LOG.md
ecfc00fc…8296  AGENT_BRIEFS.md
c5d1e206…f870  dragonfly/stages/charter.md
0e73bacf…d590  guarded-change/stages/charter.md
```

---

### 2. Per-lens findings

**FACTUAL — 1 minor.** I consulted: SKILL.md:16-30,49-61,91; METHODOLOGY.md:107-167,196-233; stage-1:21-57; stage-5:1-46; merge-brief:1-38; charter.md:7-16; guarded-change/charter.md:1-84 (fork source); AGENT_BRIEFS.md:114-136 (old merge method); issues-log #1-3 + gotchas; plan lines 42-80; criteria C3/C8/C11. The build faithfully transcribes the approved plan on every settled value I checked (6/3 redundancy, `PCT% (X/N)` + floor table + percentage-first sort, size trichotomy, on-disk layout, blindness enumeration, 71-item decomposition in the example). The floor table (`1/3→33% … 6/6→100%`) is **byte-identical** at all three sites (METHODOLOGY:157, stage-5:20, merge-brief:21) and arithmetically correct (2/6→33 floor, 4/6→66 floor, 5/6→83 floor, all verified).
- **F-1 (minor).** `charter.md:7` cites the fork source as `Guarded_change/stages/charter.md @ 8d73e5d`. Neither `~/.claude/skills/` nor the source tree is a git repo in this environment, so the commit sha is **unverifiable**. The *content* claims are all accurate: I confirmed against the live guarded-change charter that the "deliberately NOT carried" set (five-lens framing, position/concurrency lenses, coverage-challenge/label-audit, A/B-harness clause) genuinely exists in the source and is genuinely reviewer-specific (source lines 19-84), and that the carried core (independence, cite-or-count, spot-verify, provenance) is real (source lines 35-64). Only the sha itself can't be checked here — flag as unverifiable, not a defect.

**LOGICAL — 1 minor (borderline major), 1 minor.**
- **L-1 (minor, borderline major) — seam-aware merge specifies recurrence but NOT agreement reconciliation.** `stage-5-merge.md:26-30` and `merge-brief.md:28-30` define the seam-dedup entry's **recurrence** ("counted across the whole item") but say nothing about how **agreement / `PCT% (X/N)`** is computed for a finding present in *both* pieces at *different* agreement levels. For a subdivided Haiku item, each piece runs its own 6 analysts, so a seam-straddling finding can be flagged by e.g. 4/6 in piece-1 and 3/6 in piece-2. The files never state whether the merged entry keeps N=6 or the item's total analyst passes, nor whether X is the max, the union, or the sum. A merge leaf that guesses "sum X" yields `7/6 = 116%` — a nonsensical percentage on the exact path C3's seam sub-check is meant to protect (criteria:64 explicitly expects "its recurrence/**agreement** is correct across pieces"). This is a gap, not a contradiction of a frozen value (the settled agreement model doesn't define seam reconciliation either), so it rates minor per the plan's severity table — but it's on a gating criterion's core sub-check and the merge leaf is left to invent deliverable-ranking semantics. **Fix in place:** stage-5 + merge-brief should state the rule (e.g. "N stays the per-piece tier count; a seam entry's X = the greater of the two pieces' flagger counts").
- **L-2 (minor) — no explicit "borderline" flag-write step.** `stage-2-cut-gate.md:11,43` scopes the gate to "every item the **sizer flagged borderline**," and `stage-1:57` acts on "subdivided/**borderline** items," but stage-1's tiering step (step 5) never instructs the sizer to *set/write* a borderline flag (near a tier boundary / ambiguous atomic-unit). The consuming step assumes a flag the producing step doesn't explicitly create.

**MISSED OPPORTUNITY — 1 minor.**
- **M-1 (minor) — RUN.md has no authoring step.** `stage-7:28-33` and METHODOLOGY:198 describe `RUN.md` as the "self-contained apex runbook" a post-compaction coordinator "resumes from," but **no stage and no SKILL.md step writes it.** Stage-1 explicitly authors `index.md`, `plan/budget.md`, and the `tree/` skeleton (stage-1:27,48,55) but omits RUN.md; SKILL.md:44 only says "create a run-root with the layout in METHODOLOGY." C2 (restart) is not broken — stage-7:32 also allows resume from `index.md` + tree walk, and index.md *is* authored — but the documented apex resume artifact is never created. Add "write RUN.md" to stage-1's skeleton step.

**UNSTATED ASSUMPTIONS & RISKS — 1 nitpick.**
- **A-1 (nitpick) — the 200 KB slimmer threshold carries a baked-in corpus assumption.** `stage-1:37` replaces any string ">200 KB" and justifies it inline ("no analytically-relevant text field is that big"). That justification is companion-emergence-specific; a corpus with a legitimately >200 KB text field would silently lose it. It is marked "e.g." (tunable), so acceptable, but the domain-agnostic core states a domain-specific constant as a default. Consider flagging it as a Layer-2 knob.

**FIDELITY — clean (earned).** Pinned terms → mechanism → file evidence:
- *blind coordinator* → reads ONLY each direct child's `_status.md` + globs; never opens `analysis/*`, `*_verified.md`, `superlist.md`, `*_summary.md` → METHODOLOGY:107-111, SKILL:16-19, stage-6:12-14. Implemented (structural, greppable). ✓
- *size handling* → **selection** among three strategies by what's big, sizing runs AFTER tag-replace on **post-slim tokens** (bytes≠tokens) → stage-1:21-45 (esp. step 5 "Size AFTER (a)"), METHODOLOGY:134-151. ✓
- *human cut-gate* → dispatch **forbidden** until `plan/cut-gate/<item>.md` approval exists; clean-fit auto-proceeds → stage-2:5,33. ✓
- *agreement `PCT% (X/N)`* → percentage-first, floored, sort %-desc-then-recurrence-desc → stage-5:19-25, merge-brief:20-26, METHODOLOGY:156-163. ✓ (flat path; seam path = L-1 gap)
- *analyst* → cold `general-purpose` write-capable leaf, open mandate, cite-or-drop, no-cause-speculation, do-work-yourself → charter.md:22-62, analysis-brief. ✓
- *deterministic restart* → stage-done-iff-output-exists on fixed filenames, trust-files-over-cursor, per-node `_status.md` (no global cursor) → stage-7:8-26. ✓
- *ledger redaction* → `<REAL-PATH-REDACTED>` placeholders, zero live protected paths → ledger.md, corpus.md (grep-confirmed clean). ✓
No proxy substitution found except the under-specified seam-agreement path (L-1).

**POSITION LENS (C9) — PASS.** SKILL.md places "The three rules that govern everything — read first" (blindness / read-only / off-limits) at lines 14-30, **before** the stage table (line 49). Behavior rules are also restated at the stages where an executing leaf applies them (read-only/off-limits in shared-clauses + each stage; cite-or-drop in stage-4/charter). Up-front placement satisfied.

---

### 3. C8 cross-file consistency table

| Shared rule | Agree? | Evidence |
|---|---|---|
| (i) agreement `PCT% (X/N)` + %-first + floor + sort %-then-recurrence | **YES** | SKILL:55, METHODOLOGY:156-163, README:44-75, stage-5:5-25, merge-brief:3-26, summary-brief:21. Floor table byte-identical at all 3 stating sites. |
| (ii) blindness (parent reads only `_status.md`+globs; never analysis/verified/superlist/summary) | **YES** | METHODOLOGY:107-111 & 227-228, SKILL:16-19 & 67-74, stage-3:28, stage-6:12-14. Full enumeration identical in the two authoritative sites (SKILL:18, METHODOLOGY:109-110); stage files cite context-appropriate subsets, no contradiction. |
| (iii) redundancy Haiku=6, Sonnet/Opus=3; one verifier per list | **YES** | SKILL:53,60-61; METHODOLOGY:126-129; stage-1:46; stage-3:12; stage-4:12; analysis-brief:3; README:60. No `Haiku=5`-type divergence anywhere. |
| (iv) read-only + off-limits + do-the-work clauses | **YES** | shared-clauses:15-35 (canonical), charter.md:56-62, SKILL:22-30, stage-1:63-65, stage-3 rules. Consistent wording. |
| (v) size trichotomy {tag-replace, subdivide, escalate} | **YES** | METHODOLOGY:134-151 (a/b/c), stage-1:21-31 (a/b/c), SKILL:51, README:59-74. All three strategies present everywhere the set is stated. |
| (vi) layout names (tree/ summaries/ _prepared/ config/ plan/ _status.md superlist.md) | **YES** | METHODOLOGY:196-233 tree == plan:86-124 tree; stage files reference same names. |

No C8 mismatch found.

---

### 4. Committed-fix verification

- **F1 (brief ADAPTS, not preserves old method) — LANDED.** analysis-brief:3 is tier-driven ("Haiku → 6 (A–F); Sonnet/Opus → 3 (A–C)"), no hardcoded "3 Sonnet." merge-brief:3,20-26 renders `PCT% (X/N)` percentage-first and sorts "percentage descending, then recurrence descending" — the old raw `[agreement=N]` / agreement-first sort is **gone** from all agent-facing briefs. The only `[agreement=N]` / "3 Sonnet" strings in-tree are explicit *negative* warnings (shared-clauses:11, stage-5:42) or in the excluded `changes/` folder. Confirmed.
- **F2 (charter fork header has BOTH parts) — LANDED.** charter.md:7-16 carries (i) source commit `Guarded_change/stages/charter.md @ 8d73e5d` and (ii) an explicit "**Deliberately NOT carried**" enumeration matching the dragonfly precedent. Both-part requirement met (sha unverifiable — see F-1).
- **C11 (agent-facing redaction) — LANDED.** grep of briefs/ + example ledger.md + corpus.md for `Phoebe|Phoebes_notes|Downloads/Phoebe|Canary|FULL-SANDBOX-BOX|/personas/…`: **zero matches.** corpus.md:37-39 and ledger.md:6,19 use `<REAL-…-REDACTED>` placeholders. Confirmed clean.
- **Guardrail coverage — COMPLETE.** issues-log #1 read-only → charter.md:56-62 + shared-clauses:22-28; #2 OOM (du -h / never-Read->50MB / streaming slimmer) → stage-1:17-38, METHODOLOGY:135-149; #3 off-limits/brief-is-the-fence + redaction → charter.md:59-62, shared-clauses:30-35, C11; delegation "do-the-work" → shared-clauses:15-20; on-disk-state/deterministic restart → stage-7; over-flagger gotcha → stage-3:42; stale-cursor gotcha designed out → stage-7:16-18. Every entry has a home.
- **Size trichotomy — COMPLETE.** All three strategies present in stage-1:21-31 (tag-replace / subdivide / escalate), and stage-1:40-44 (step 5) states sizing runs AFTER tag-replace on the post-slim/estimated token size, not raw bytes. Confirmed.

---

### 5. Spot-verify note

Re-checked a sample of my own citations against the files: (a) charter.md:44 — confirmed reads "A no-flags result must be earned by showing coverage" (the recast nitpick fix). (b) SKILL.md — confirmed the three-rules block is lines 14-30 and the stage table starts line 49, so blindness/read-only/off-limits genuinely precede it (C9). (c) stage-5:26-30 — re-read in full; confirmed the seam clause addresses only "recurrence … across the whole item" with no agreement/N reconciliation (L-1 is real, not a misread). (d) C11 grep re-run returned "NO MATCHES." All spot-checks held.

---

### 6. Worst-severity summary + routing recommendation

**Worst severity: MINOR (L-1, borderline major).** No blocker, no major. Nine gating criteria (C1-C8, C11) are conformant as written; C8 shows zero cross-file mismatch; F1/F2/C11 all landed; guardrail and trichotomy coverage complete. Advisory C9 passes; C10 is correctly N/A (greenfield).

**Routing: fix-and-proceed → harness**, with these fix-in-place items before/at stage 8:
1. **L-1** — specify seam-finding agreement/N reconciliation in stage-5 + merge-brief (the one finding that touches a gating criterion's sub-check; do not leave it to the merge leaf's improvisation).
2. **L-2** — have stage-1 explicitly write the borderline flag the cut-gate consumes.
3. **M-1** — add an explicit "write RUN.md" authoring step to stage-1.
4. A-1 (nitpick) and F-1 (sha unverifiable) — log and proceed.

**Two honest carry-forwards (not defects):** C7 (live == source) is **verified = no** — no install exists at `~/.claude/skills/data-distiller/` — which is the pre-declared orchestrator hand-off, not a build failure (must be closed by the orchestrator's post-sync `diff -r` folded back into 8-harness/decisions per criteria:145-150). The charter fork sha is unverifiable in this non-git environment.
