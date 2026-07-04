# 8 — Harness: audit-hardening-2026-07

**Stage-0 note:** docs-only change; no metric baseline exists (recorded at run start) → this
harness runs **conformance-only** against the frozen v3.1 criteria (`4428f612…`, re-verified
below). Criteria are v3.1 per the owner-authorized stage-8-major re-plan (decisions.md).

## C1 — inspection-by-location (every fix in every load-bearing location)

Method per the frozen criteria row ("Inspection-by-location: locate exact text per mapping
row; quote it + evidence pointer"): C1 is a text-presence criterion — locating and quoting
the landed text at each mapping-table location IS the execution of its check. Quotes
abbreviated to the identifying phrase; full text at the cited lines of the SOURCE files
(== live copies, C5 below).

| Fix | Location per mapping | Landed at | Identifying quote (trigger→requirement→consequence present) |
|---|---|---|---|
| F1 | METHODOLOGY charter bullet | METHODOLOGY.md:236-250 | "**Provenance is part of the review record.** Every cold-review record, wherever in the run it occurs… (i) the verbatim charter… (v) the reviewer-reported sha256… A record missing any of these = the review is treated as **un-run**. In A/B harness arms, author-authored supplementary context is prohibited outright" |
| F1 | METHODOLOGY "What a run produces" | METHODOLOGY.md:505-508 | "The review docs… are **verbatim records** — each embeds the charter given, the exact context list, and the reviewer's raw output per the charter's provenance rule; the author's interpretation belongs in `decisions.md`" |
| F1 | SKILL steps 3 and 6 | SKILL.md:67 (step 3), SKILL.md:80-81 (step 6) | "Write `3-redteam-plan.md` as a **verbatim record** per METHODOLOGY 'Provenance…': embed the charter given (core verbatim + task additions quoted), the exact context list (closed set…), the reviewer's verbatim output, its agent type/model, and its reported context-file hashes — missing any ⇒ the review is un-run" / "Write `6-redteam-code.md` as a verbatim record (same provenance duties as step 3)" |
| F2 | METHODOLOGY stage-8 block | METHODOLOGY.md:387-395 | "**An unreviewed check is not a check.**… gets a **targeted cold check before its results count** — for representativeness, and, where the check guards a fix, that it fails against the unguarded version; until then its results are `verified = no`… discarded and rebuilt in place (logged…)… route via the gate-8 severity row… a stage-8 fix-in-place re-runs the criterion checks its diff could have invalidated" |
| F2 | SKILL steps 7 and 8 | SKILL.md:82-84 (step 7), SKILL.md:91-95 (step 8) | "record any in-place fix diff in `decisions.md`" / "Any executable check born after stage 6 gets a targeted cold check before its results count (METHODOLOGY 'An unreviewed check is not a check'); a fix-in-place here re-runs the criteria its diff could invalidate, diff recorded" |
| F3 | METHODOLOGY table paragraph | METHODOLOGY.md:397-403 | "…│ evidence │ result*. The **evidence** cell of every gating `verified = yes` row cites where the raw output lives… for a human-judged-rubric criterion the pointer is the named judge + where the verdict is recorded. A gating PASS row with no evidence pointer counts as `verified = no`, and the consumer's citation spot-verify extends to a sample of evidence cells" |
| F3 | SKILL step 8 | SKILL.md:89-91 | "its **evidence** column: every gating PASS cites its raw output (rubric rows: named judge + verdict location); no evidence pointer ⇒ `verified = no`" |
| F4 | METHODOLOGY stage-1.5 clause | METHODOLOGY.md:168-176 | "**Criteria freeze.** When gate 4 routes to build, `1.5-criteria.md` **freezes** and its hash (or a verbatim copy) is recorded… must equal the version the stage-3 reviewer read — except for gate-4 in-place fixes, each traceable to a logged finding… divergence is a post-freeze edit → the affected criteria's PASSes are invalid unless… Any **weakening**… is audited exactly like an advisory relabel" |
| F4 | SKILL step 4 | SKILL.md:72-74 | "On route-to-build: **freeze `1.5-criteria.md`** and record its sha256 (or a verbatim copy) in `decisions.md` (METHODOLOGY 'Criteria freeze')" |
| F5 | METHODOLOGY severity model | METHODOLOGY.md:315-320 | "**The reviewer's severity routes.**… the gate routes on the **reviewer's** stated severity… contest… only via a logged `decisions.md` entry; demoting a **blocker or major** additionally requires the human tie-break… A silent unilateral demotion is a gate violation: the reviewer's routing stands" |
| F5 | SKILL steps 4 and 7 | SKILL.md:71-72 (step 4), SKILL.md:82-83 (step 7) | "Route on the **reviewer's** severities — contest only via a logged entry; demoting a blocker/major needs the human tie-break" / "Route on the reviewer's severities (as at gate 4)" |
| F6 | METHODOLOGY stage-1 + charter closed set + stage-6 line | METHODOLOGY.md:115-117, :236-250 (closed set inside F1 — single definition), :190-193 | "The spec also **declares the expected touched files** — that list joins every cold reviewer's context (see the charter's closed set)" / "At stage 6 the reviewed diff is generated **mechanically** (`git diff` against the recorded base, or an equivalent captured command), the command recorded in `6-redteam-code.md` — a hand-curated file set = the review is un-run for the omitted scope" |
| F6 | SKILL steps 1, 3, 6 | SKILL.md:38 (step 1), :67 (step-3 closed-set clause), :78-80 (step 6) | "Declare the expected **touched files** — the list joins every cold reviewer's context" / "(closed set: stage artifacts + config `redteam_context` + spec touched-files + carried findings)" / "Generate the reviewed diff **mechanically** (`git diff <recorded-base>`; record the command) — hand-curated ⇒ un-run for the omitted scope" |
| F7 | METHODOLOGY charter bullet | METHODOLOGY.md:251-255 | "**Challenge criteria coverage (stage 3).** Name the behaviors the change could plausibly alter that **no criterion observes** — each named gap needs a concrete scenario and ranks by impact… A stage-3 review with no coverage-challenge section (an explicit 'none found' counts) is incomplete on lens 4 and treated as un-run for that lens" |
| F7 | SKILL step 3 | SKILL.md:67 (tail) | "Require the **coverage challenge**:… (explicit 'none found' allowed); no such section ⇒ lens 4 un-run" |
| F8 | METHODOLOGY config-contract Rules | METHODOLOGY.md:473-479 | "**Paths are validated, not assumed.**… at run start… and at each cold-reviewer spawn for any path not yet validated. Gate 4 may not pass until the run-start validation result is recorded in `decisions.md`. A missing/empty path is surfaced to the human before proceeding" |
| F8 | SKILL Inputs | SKILL.md:19-22 | "**Validate every path a cold reviewer will be handed**… record the result in `decisions.md` (gate 4 cannot pass without it) and surface dead paths to the human" |
| F9 | SKILL self-check section | SKILL.md:118-124 | "Skill-file edits are edits to a **position-sensitive assembly** (these documents are prompts), so the position lens applies. **Non-trivial edits take the full loop**… Standing self-check criteria…: live copy == source copy (`diff`); SKILL.md ↔ METHODOLOGY.md consistency on every rule both state; a behavior-preservation criterion for anything moved or removed. A stage-3 red-team remains the cheap check encouraged after any edit, however small" |

Every mapping row: fix present at every named location, with trigger + requirement +
**consequence** (F7's "un-run for that lens", F8's "gate 4 may not pass" — the two [LO-5]
consequences — confirmed above). **C1: 18/18 location checks PASS.**

## C2 — cross-file consistency (7-item sweep, each explicitly reconciled)

1. **Closed set vs carry-forward:** carried findings are IN the closed set — "carried-forward
   findings from `decisions.md`" (METHODOLOGY.md:244-245); SKILL step 3 lists "carried
   findings" in the same set (SKILL.md:67). Consistent.
2. **Freeze vs gate-4 fix-in-place:** freeze binds at route-to-build "except for gate-4
   in-place fixes, each traceable to a logged finding, with the criteria diff recorded"
   (METHODOLOGY.md:170-171); gate-4 minor route unchanged. No contradiction.
3. **F5 vs human authority:** "demoting a **blocker or major** additionally requires the
   human tie-break (the same authority that breaks iteration-cap ties)" (METHODOLOGY.md:318-319)
   — the human keeps the final word; only *silent unilateral* demotion is forbidden. Consistent.
4. **F2 vs iteration cap:** the targeted check is not a numbered gate — "not a loop restart;
   findings it raises about the change itself route via the gate-8 severity row"
   (METHODOLOGY.md:392-393); gate-8 routings count toward gate 8's cap as before. Consistent.
5. **F3 vs existing table spec:** column list extended IN PLACE (METHODOLOGY.md:398-399) —
   the one benign deletion+addition hunk, justified in the C6 walk (hunk M6). The original
   blocks-done rule survives verbatim in the same sentence run. Consistent.
6. **F1 verbatim-output vs "Write 3-redteam-plan.md":** the stage doc = the verbatim record
   (SKILL.md:67 "Write `3-redteam-plan.md` as a **verbatim record**"; METHODOLOGY.md:505-508
   same rule; author interpretation → `decisions.md`). One definition, both files. Consistent.
7. **F3 rubric rows [AR-5]:** METHODOLOGY.md:400-401 "for a human-judged-rubric criterion the
   pointer is the named judge + where the verdict is recorded" == SKILL.md:90-91 "(rubric
   rows: named judge + verdict location)". Consistent.

Trigger/requirement/consequence agreement per shared rule verified in the C1 walk (SKILL
clauses are pointer-style, naming their METHODOLOGY section — no second definitions).
**C2: 7/7 reconciled, no contradictions found.**

## C6 — pure-additive hunk walk (`git diff 8a7ac65`, 12 hunks, 210 lines)

Diff generated mechanically: `git diff 8a7ac65 -- Guarded_change/SKILL.md
Guarded_change/METHODOLOGY.md` (12 hunks by `grep -c '^@@'`; copy at session scratchpad
`audit-hardening.diff`). Deletion-shaped lines walked individually; per the frozen C6 the
only legal deletions are F9's sentence rewrite + in-place sentence extensions.

| Hunk | Location | Deletion-shaped content | Verdict |
|---|---|---|---|
| M1 @@112 | stage-1 | `-Deep enough that the plan…without guessing intent.` re-emitted verbatim + touched-files extension (F6) | in-place extension; original survives verbatim — PASS |
| M2 @@163 | stage-1.5 | none (pure addition: Criteria freeze block, F4) | PASS |
| M3 @@176 | stage-3/6 | `-code against criteria+plan.` re-emitted verbatim + mechanical-diff extension (F6) | in-place extension; original survives verbatim — PASS |
| M4 @@219 | charter | none (pure addition: F1 provenance + F7 coverage bullets) | PASS |
| M5 @@278 | severity model | none (pure addition: F5 paragraph) | PASS |
| M6 @@343 | stage-8 | `-│ result*. Any **gating** row…` re-emitted as `+│ evidence │ result*. …` + evidence rules + the SAME blocks-done sentence verbatim (F3; sweep item 5); plus pure addition of the F2 block | the named expected F3 column-list extension; the original obligation ("Any gating row that is not verified = yes blocks 'done' unless…") survives verbatim — PASS |
| M7 @@415 | config rules | none (pure addition: F8 bullet) | PASS |
| M8 @@440 | run products | none (pure addition: verbatim-records note, F1) | PASS |
| S1 @@16 | Inputs | none (pure addition: F8 sentence) | PASS |
| S2 @@31 | step 1 | none (pure addition: F6 touched-files line) | PASS |
| S3 @@59 | steps 3–8 | five rewrapped lines, each re-emitted verbatim with tail extensions: step-3 long line (+F1/F7 verbatim-record + coverage clauses), gate-4 line (+F5/F4), step-6 line (+F6/F1), gate-7 line (+F5/F2), step-8 conformance line (+F3/F2/F4) | in-place extensions; every original clause survives verbatim (checked word-for-word against the `-` lines) — PASS |
| S4 @@98 | self-check | `-…That is the cheapest validation the methodology gets and is encouraged after any edit to either file.` → F9's expected rewrite; the original obligation survives strengthened: "A stage-3 red-team remains the cheap check encouraged after any edit, however small" + non-trivial edits now take the FULL loop | the one named F9 rewrite; obligation survives verbatim-or-stronger — PASS |

Enumeration note: hunks M1 and M3 are METHODOLOGY in-place sentence extensions not
individually itemized in the frozen C6 parenthetical ("F3 column list; SKILL clauses wired
into existing bullets") but squarely inside its governing category ("in-place sentence
extensions… the original obligation survives verbatim-or-stronger") — both justified
individually above. No existing rule deleted or weakened anywhere in the diff.
**C6: 12/12 hunks PASS.**

## Per-criterion verification table

| # | Criterion | Gating? | Path exercised | Verified by execution? | Evidence | Result |
|---|---|---|---|---|---|---|
| **C1** | Every fix present in every load-bearing location, full substance | gating | Inspection-by-location per the mapping table — the criterion's own stage-8 method under the frozen criteria (text-presence: locating + quoting the text is the check's execution) | yes | The C1 walk above: 18 location rows, each with file:line + identifying quote against source == live (C5) | **PASS** |
| **C2** | Cross-file consistency + 7-item sweep reconciled | gating | Side-by-side inspection per sweep item | yes | The C2 section above: 7 items, each with the reconciling quotes + file:line | **PASS** |
| **C3** | Replay A/B, instrument v3.1 (differential scoring, pre-committed conditions) | gating | EXECUTED: 6 fresh cold `claude-opus-4-8` arms (3T+3K) on fixture v2 at a neutral path; scored by the pre-registered extraction rule; scoring cold-verified before this gate consumed it | yes | `8-battery-round3.verbatim.md` (6 verbatim outputs + scoring: V1 3/3-T vs 0/3-K; V2 2/3-T vs 0/3-K; V4 3/3-T AND 3/3-K; V3 observational 0/3-T, 1/3-K; both tripwires not triggered) + `8-battery-round3-scoring-verification.verbatim.md` (24/24 cells confirmed; "PASS stands YES") | **PASS** — verdict duties: n=3/arm (13 arms cumulative); rounds-1/2 history carried verbatim in the record (V1 4/4-T:0/4-K, V2 3/4-T:0/4-K, V4 8/8, V3 1/4-T:3/4-K); honest driver: the owner-authorized V3 demotion — not the scoring change — is the largest single driver of this pass (under round-2 rules the 0/3-T V3 record would have failed again) |
| **C4** | Bloat caps: METHODOLOGY ≤583, SKILL ≤127, combined ≤671 | gating | `wc -l` on both source files, post-build | yes | Command output (this session): `534 METHODOLOGY.md / 124 SKILL.md / 658 total` vs caps 583/127/671, baselines 467/102/569 | **PASS** |
| **C5** | Live == source after the stage-8 install [AR-7] | gating | Installed both files to `~/.claude/skills/guarded-change/`, then `diff` per file | yes | Command output (this session): `diff` SKILL.md → empty ("identical"); `diff` METHODOLOGY.md → empty ("identical") | **PASS** |
| **C6** | Pure-additive: no rule deleted or weakened; only the named deletion classes | gating | `git diff 8a7ac65` reviewed hunk-by-hunk | yes | The C6 walk above (12/12) + diff copy at scratchpad `audit-hardening.diff` (210 lines, 12 hunks) | **PASS** |
| **C7** | S1–S3 unbuilt; final report carries S1–S3 + C3 caveats + residual-displacement note + attention spend | advisory | Reporting duty | (advisory) | S1–S3 confirmed unbuilt (no structural restructuring in the diff — C6 walk); report duties discharged in `9-report.md` | surfaced — see `9-report.md` |

## Criteria-freeze verification (F4 dogfooded)

`sha256sum 1.5-criteria.md` at harness time =
`4428f612cf9c0792a2d66986bd02850d5b400836c7f8a8f9b5133ae43ce018ad` — matches the v3.1
freeze recorded at the re-plan's route-to-build in `decisions.md` AND the verbatim frozen
copy `1.5-criteria.v3.1-frozen.md` (same hash, same command output this session). No
post-freeze drift.

## Verdict

All six gating criteria `verified = yes` with evidence pointers; C7 advisory surfaced with
its duties discharged in `9-report.md`. **Stage-8 result: ACCEPT — proceed to gate entry,
commit + push.**
