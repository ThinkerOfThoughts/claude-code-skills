# 2 — Plan: audit-hardening-2026-07

Additive edits to METHODOLOGY.md + SKILL.md, one mapping row per finding. Style: terse,
mechanical, wired into existing sections (no new essays). After source edits: copy both files
to the live dir; verify C5.

## Edit mapping table (C1's oracle)

| Fix | METHODOLOGY location(s) | SKILL location(s) | Substance (trigger → requirement → consequence) |
|---|---|---|---|
| **F1 provenance** | Charter section: new discipline bullet **"Provenance is part of the review record."** Also one sentence in "What a run produces" (stage-doc contents) | Steps 3 and 6: one sentence each | A stage-3/6 doc must embed (i) the verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's verbatim output (author summary lives in decisions.md, separate). The charter given is the METHODOLOGY charter text, not a paraphrase. Reviewer input is closed-set: named stage artifacts + config `redteam_context` + spec touched-files + carried-forward findings from decisions.md; any supplementary author-authored context must be quoted in the stage doc as such → a stage doc missing any of these = the review is treated as un-run. In A/B harness arms, author-authored supplementary context is prohibited outright (leak = confound; cite concurrency-lens C3 attempt-1) |
| **F2 post-review artifacts** | Stage-8 section: new short block **"An unreviewed check is not a check."** | Steps 7 and 8: one sentence each | Any new/modified executable check whose results stage 8 will trust, created after the stage-6 review, gets a targeted cold check (representativeness; and where the check guards a fix: fails-against-unguarded) BEFORE its results count. In-place fix diffs at gates 7/8 are recorded in decisions.md. A stage-8 fix-in-place re-runs the criterion checks its diff could have invalidated → results from an unreviewed post-6 check count as `verified = no` |
| **F3 evidence column** | Stage-8 verification-table paragraph: extend table columns + rule | Step 8 conformance bullet: one clause | Table gains an **evidence** column: every gating `verified = yes` cites where the raw output lives (command + output file/excerpt). Gating PASS with no evidence pointer = `verified = no`. Consumer's spot-verify extends to a sample of evidence pointers |
| **F4 criteria freeze** | Stage-1.5 section: freeze clause at end | Step 1.5: one sentence | When gate 4 routes to build, 1.5-criteria.md freezes. Any later edit: decisions.md entry (change + reason) + targeted re-red-team of the edited criteria. Any weakening (gating→advisory, threshold loosened, scope narrowed) is audited exactly like an advisory relabel under the existing label-audit → an unlogged post-freeze edit invalidates the affected criterion's PASS |
| **F5 reviewer-severity routing** | Severity model section: one short paragraph after the routing table | Steps 4 and 7: one clause each | Gates route on the **reviewer's** stated severity. The author may contest only via a logged decisions.md entry; demoting a blocker/major requires the human tie-break (same authority as iteration-cap ties) → a silent demotion is a gate violation; the reviewer's routing stands |
| **F6 touched-files + mechanical diff** | Stage-1 section: spec declares expected touched files. Charter: reviewer context includes them. Stage 6 (in charter or stage detail): diff captured by command | Step 1: one clause. Steps 3/6: one clause each | Spec lists expected touched files; reviewer scope at 3/6 = artifacts + config redteam_context + touched files. Stage-6 reviewed diff is generated mechanically (e.g. `git diff <recorded-base>`, or equivalent captured command for non-git trees), command recorded in 6-redteam-code.md → a hand-curated diff = review treated as un-run for the omitted scope |
| **F7 coverage challenge** | Charter: one discipline bullet (stage-3 aimed) | Step 3: one clause | At stage 3 the reviewer names behaviors the change could plausibly alter that **no criterion observes** — each needs a concrete scenario and ranks by impact (precision discipline unchanged; the finding is unmeasured blast radius, not "add more criteria") |
| **F8 config validation** | Config-contract Rules: one bullet | Inputs section: one sentence | At run start, mechanically check every `redteam_context` path exists/readable; missing/empty → surface to human before proceeding (fix config, or named degraded-review acceptance in decisions.md) |
| **F9 self-check strengthened** | (none — self-check lives in SKILL) | Self-check section: replace "encouraged" sentence with 3 tight sentences (additive in force; the only place a sentence is reworded — original obligation retained and strengthened, per C6 exception) | Skill-file edits are edits to a position-sensitive assembly (they are prompts) — the position lens applies. Non-trivial edits take the **full loop**, not just stage 3. Standing self-check criteria: live == source (diff); SKILL ↔ METHODOLOGY consistency on every shared rule; behavior-preservation for anything moved/removed |

## Contradiction sweep (C2's checklist)

Reconcile explicitly while editing:
1. F1 closed-set input **vs** existing carry-forward of prior findings → carried findings are IN the closed set (via decisions.md).
2. F4 freeze **vs** gate-4 "minor → fix in place" edits to criteria → freeze point is *when gate 4 routes to build*, so gate-4 in-place criterion fixes precede the freeze.
3. F5 reviewer-severity routing **vs** existing human authority → human tie-break retains final word; F5 only forbids *silent unilateral* demotion by the author.
4. F2 post-6 cold check **vs** iteration cap → the targeted check is not a numbered gate; findings from it route through gate 8 (and count toward its cap).
5. F3 evidence column **vs** existing table spec → column list extended in place, same paragraph, one sentence.
6. F1 verbatim-output retention **vs** existing "Write 3-redteam-plan.md" phrasing → the stage doc = verbatim record + header metadata; author's interpretation goes to decisions.md.

## Measurement (how each criterion is verified)

- **C1/C2** — inspection-by-location against this mapping table (stage 8, quoted text per row).
- **C3** — replay A/B. Fixture: `fixtures/seeded-review-record/` inside the change folder — a
  minimal fake change-run (`3-redteam-plan.md` missing provenance = V1; `8-harness.md` with a
  gating PASS row lacking evidence = V2 and a "clean factual, no citations" stage-3 verdict =
  V3). Arms: 2× treatment (amended METHODOLOGY+SKILL) vs 2× control (current files, from git
  HEAD), each asked the same neutral question: "You are the gate consumer for this change
  record. Per the attached methodology, which reviews/results are valid to act on? List any
  that must be treated as un-run or unverified, citing the rule." Scope: fixture + methodology
  docs ONLY (no other context; no author notes — F1's A/B rule dogfooded). Pass: both
  treatment reviewers flag V1+V2+V3; controls expected to flag V3 only (control catching
  V1/V2 → record "redundant-but-harmless", qualified pass per concurrency-lens precedent).
- **C4** — `wc -l` before/after both files.
- **C5** — `diff` source vs live per file.
- **C6** — `git diff` of the two source files reviewed hunk-by-hunk; deletion hunks justified
  (only F9's sentence rewrite is expected).

**Instrumentation:** none absent — all signals are files/diffs/subagent outputs. The fixture
is new instrumentation and is itself a post-stage-6-shaped artifact → per F2 (dogfooded), the
stage-3 reviewer is asked to challenge the fixture design NOW (it exists at plan time, so the
review CAN see it — closing the F2 window for this run), and the stage-6 reviewer re-checks
the built fixture verbatim.

**Severity→routing thresholds:** methodology defaults (blocker→1, major→2 at gate 4;
blocker/major→5 at gate 7; per-table at 8). Gating metrics: C1–C6. Advisory: C7.

## Build order

1. Edit METHODOLOGY.md per mapping (F1→F8 rows, top-to-bottom of the file, one pass).
2. Edit SKILL.md per mapping (F1→F9).
3. Build the C3 fixture under `changes/audit-hardening-2026-07/fixtures/seeded-review-record/`.
4. Copy both files to `~/.claude/skills/guarded-change/`.
5. `wc -l` + `diff` + `git diff` capture for C4/C5/C6.
