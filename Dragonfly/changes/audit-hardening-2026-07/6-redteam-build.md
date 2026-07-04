# 6 — Red-team of the built change (mechanical diff vs `9cec23d`) — verbatim record

## Provenance
- **Date:** 2026-07-04. **Reviewer:** cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author (fresh spawn; not a stage-3 agent).
- **Thing under review:** `git diff 9cec23d -- Dragonfly/METHODOLOGY.md Dragonfly/SKILL.md`,
  saved at `6-build.diff` (pre-fix sha256 `008cf056…a4bce5`); reviewer regenerated the diff
  from the repo itself and verified byte-identity before reviewing.
- **Context given (closed set):** the diff + built Dragonfly {METHODOLOGY, SKILL}.md +
  change docs {1-spec, 1.5-criteria, 2-plan, decisions}.md + Guarded_change {METHODOLOGY,
  SKILL}.md (cross-ref target; reviewer verified both == their `9cec23d` versions) +
  0-audit-findings.md. Reviewer-reported sha256s at the top of the verbatim output.
- **Task:** hunk-by-hunk mapping to the frozen plan's 15 rows with substance adjudication
  (the build compressed prose under cap pressure — the declared central task was
  tightening-vs-substance-loss), insertion-order verification, built-text consistency +
  all 9 sweep items, C3 cross-ref preview, four lenses. Author-declared compressions were
  explicitly listed in the charter for conscious adjudication.
- **Freeze integrity:** reviewer independently confirmed 1.5-criteria.md and 2-plan.md
  hashes match the frozen values in the gate-4 entry.
- **Transport note:** output arrived through the harness task-notification layer; no
  HTML-entity de-escaping was required this time. No normalization applied.

## Reviewer output (verbatim)

# Stage-6 cold red-team — dragonfly audit-hardening-2026-07 build diff

## Context-file hashes (sha256, run by me)

```
008cf0563ceb817a2d21080cf57589c0c090abb65bc37adb7721a41184a4bce5  Dragonfly/changes/audit-hardening-2026-07/6-build.diff
2cd0a5502458c7b3ea40528f5e5ed872bb56b2c212139967cb4286f7fbe8c0c6  Dragonfly/METHODOLOGY.md (built)
92d41b1ff6c01fa4d25c966ed2c8da44164ef906879de0920b7254c5f143030f  Dragonfly/SKILL.md (built)
a048500048675f38e7c9448e489dc99de5e0cffe0f234fc7cc6ed945d10b6cc7  1-spec.md
0ba8cfc59f3fd0b63f3b0e5b0e1f282ee87b206d6ff8bc20b3c4591cbc00e130  1.5-criteria.md  (== frozen hash in decisions.md:137 — freeze intact)
15ab47d6c5dfb526323a043a0e068f51ede2f6d130fb037f0d673b3c563ce523  2-plan.md        (== frozen hash in decisions.md:139 — freeze intact)
e2f6d93a16330f55818c8d9a76ede2e2e09eca2fdbf81556dd07705008f1db40  decisions.md
35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3  Guarded_change/METHODOLOGY.md (== `git show 9cec23d:` hash — unchanged since base)
4e2a2e5135ce0d3397fa208a18e4f1715e22e3738b99bca16cea153e7302839b  Guarded_change/SKILL.md (== `git show 9cec23d:` hash — unchanged since base)
f753d7fcf809a0303ee91dbeb85cbba327f5c01e0d753cde5aaecc98dbde5cbc  0-audit-findings.md
```

## Mechanical checks (run by me)

- **Diff regeneration:** `git diff 9cec23d -- Dragonfly/METHODOLOGY.md Dragonfly/SKILL.md` → sha256 `008cf056…a4bce5` — **byte-identical to the saved 6-build.diff** (`diff -q` clean). Both reported.
- **`wc -l`:** METHODOLOGY 521 (cap 525 ✓), SKILL 149 (cap 152 ✓), combined **670 = cap exactly** (baselines 441/129/570 confirmed via `git show 9cec23d:`).
- **`git diff 9cec23d --stat`** (scoped): METHODOLOGY +104 lines changed, SKILL +46; 125 insertions, 25 deletions.
- **Scope observation:** the *unscoped* `git diff 9cec23d --stat` shows a third modified file in the working tree: `Guarded_change/guarded-change.companion.md` (20 lines, a redteam_context repoint). It is outside the spec's touched files (1-spec.md:37-43) and outside the reviewed diff — flagged under risks below.

---

## 1. Hunk-by-hunk mapping (all 20 hunks)

Legend: "ext" = original sentence re-emitted with all original tokens preserved in order (C6 in-place-extension class).

| # | Hunk | Row(s) | Substance (trigger→requirement→consequence) survives? | Deletion-shape adjudication |
|---|---|---|---|---|
| M1 | `@@ -88,7 +88,8` diagram :91 | D-8 breadcrumb | ✓ pointer only: "(escape for bugs unreproducible blind: see stage-1 detail)." (METHODOLOGY.md:92) — states no second rule | Named class (loop-diagram :91 extension). Reflow into two code-block lines matches existing continuation-column style (:92 vs :96) — **acceptable** |
| M2 | `@@ -138,6 +139,11` stage-1 | D-8 full escape | ✓ full: trigger "cannot be built blind (intermittent / load-dependent / emergent)"; requirement "recorded in `decisions.md` **naming the infeasibility class**… stays `ungated`; the representativeness gate still binds"; consequence "legal only recorded + tier-bound" (:142-146). Sweep-4's required label "an exception to the ordering above, recorded" present verbatim (:142) | Pure addition |
| M3 | `@@ -173,7 +179,17` stage-6 | D-3, D-7, D-12 + micro-rewrite | ✓ D-3 full (:182-185, incl. "an uncounted pass is a gate violation"); ✓ D-7 full (:185-188 — per-thread, cross-thread increment, escalates alone, split-with-reason, "global counting may not mask per-thread thrash"); ✓ D-12 full (:188-192, incl. "none identified" counts, "one found false ranks by impact", gate-violation consequence "like an uncounted cycle") | Named micro-rewrite "This is"→"The cap is" (:192), obligation identical. Punch-line merging onto the paragraph's last line is **not a degradation**: the original punch line also shared its line ("…convergence stop. This is the defense…", 6-build.diff:31). Terminal-sentence position holds — **acceptable** |
| M4a | `@@ -181,17 +197,42` toggle item 3 | D-5 (stage 7) | ✓ full: rate shift + run count up front, rubric by reference, "a single flip does not satisfy it" (:200-202) | ext ✓ |
| M4b | same hunk, depth block | D-13 | ✓ full (:207-212): deepest-actionable-node definition, why-down ONE level, (a)/(b)/(c), cold pass challenges "root or relay?", consequence "'explains the symptom' at a relay does not satisfy stage 7". Compressions: "third-party code"→"third-party", "named, not vague"→"named" — meaning intact, **acceptable tightening** | Pure addition |
| M4c | same hunk, sweep block | D-14 | ✓ full (:213-217): explained-or-residual, ranked, carried in diagnosis.md + handoff, struck only with recorded reason, "Found (primary), with named residuals" legal, "silent absorption is not", blocking consequence | Pure addition |
| M4d | same hunk, re-anchor | Plan insertion-order (R2-P-1) | ✓ verbatim per plan: "all three bar items + both records + the chain's cold-red-team pass (gate marker `cold-red-teamed`), conjunctively" (:218-219) | Pure addition |
| M4e | same hunk, D-2 block | D-2 | ✓ full (:221-227): (a)–(e) all present incl. (c)'s named-reason classes and "not vague", (d) sign-off, (e) tier; mitigations "marked as such (stage-9-verified on symptom evidence only)"; consequence "Missing **any** of (a)–(e) → not a legal stop" (R2-F-1 honored). Sits between stage 7 and stage 8, outside the "found" bar ✓ | Pure addition (a blank line before stage 8 consumed — whitespace only, no rule) |
| M4f | same hunk, stage-8 rewrite | D-13/D-14 stage-8 contents | ✓ contents: "causal chain with **each level's depth-check status**, the **named residuals**" (:229-231) — enumeration insertions preserve all original tokens in order. **BUT**: "Hand to **guarded-change** for the fix. Dragonfly…" → "Hand to **guarded-change**; Dragonfly…" **deletes "for the fix"** | **FINDING 2 (minor)** — a deletion-shaped edit outside all five C6 classes (2-plan.md:128-134): not a verbatim re-emission+extension, not a named rewrite. Obligation survives (":231 Dragonfly does **not** author the fix" + intro :8-9), so no substance loss — but frozen C6's letter ("Any deletion-shaped hunk outside these classes = C6 fail", 1.5-criteria.md:30) cannot justify it at stage 8. Restore " for the fix" (fits on :231, zero line cost) |
| M4g | same hunk, stage-9 headline clause | D-2 stage-9 exception | ✓ full: "there is no stage-7 chain+toggle to use: stage 9 verifies the marked mitigations on **symptom evidence only** — no cause-resolution claim" (:234-235), at the headline per plan | Pure addition |
| M5 | `@@ -209,6 +250,11` stage-9 | D-5 window + D-14 residual re-check | ✓ full: window up front from ledger frequency, example instantiated ("≥ 5 sessions", clearer than the plan's "≥ N"), "a single clean run or an unstated window does not satisfy them"; "killing the primary does not close an unexplained residual" (:253-256) | Pure addition; lands after the 9a/9b bullets, before the terminal routing rule — a fair reading of "in 9a/9b's window context" since the sentence governs both sub-items |
| M6 | `@@ -232,6 +278,14` rep-gate | D-4 detector paragraph | ✓ full (:281-287): decides-boundary "(a classifier, a grep, a threshold rule)", both halves, ledger-row evidence, BEFORE-consumed, "silent-on-clean half is a deliberate, strictly stronger duty" (sweep-6's honesty requirement), capture-only carve-out, rejection consequence | Pure addition |
| M7 | `@@ -269,8 +323,8` triage intro | D-4 enumeration | ✓ "+ detector/readout" (:326) | ext ✓ — named in C6 |
| M8 | `@@ -287,7 +341,11` lite | D-1/D-9 (sweep 7) | ✓ full: "The provenance record is not scaffolding… dropping only the five-item doc set above" (:344-346; the five items are enumerated at :342); lite-record minimum (artifact, intent+criterion, verdict, verbatim-output location, in `decisions.md`), consequence "unrecorded = treated as not having happened (artifact untrusted)" (:346-348). "(per D-1)" gloss dropped — carried by "(charter section below)" — acceptable | ext ✓ (":Lite carries a pointer back…charter." re-emitted verbatim, extension appended) |
| M9a | `@@ -324,6 +382,21` aims | D-13 aim, D-12 aim | ✓ both (:385-386); D-12's aim is the list's **last item** per plan. The "(one found false ranks by impact)" parenthetical is absent from the aim — **adjudicated acceptable** (nitpick): the ranking duty is stated at its other mapped location (:191) and the aiming list "enumerates aims, it is not a priority order" (2-plan.md:99-100); imported GC discipline already carries "Rank every finding" (GC METHODOLOGY.md:222) | Pure addition |
| M9b | same hunk, provenance | D-1 | ✓ full five elements (:388-394), pointer-tolerant location, full-GC nested-or-external record + pointer in hunt `decisions.md`, consequence "the pass is **un-run** — its reading may not be consumed" | Pure addition |
| M9c | same hunk, inheritance | D-11 | ✓ charter half full (:394-399): "unconditional" defined "(those with no stage or trigger scope of their own)", provenance included, exemption scoped to direct stage-7 + lite, full-GC carve-out affirmative. **Self-check half: see FINDING 1** (SKILL side) | Pure addition; closing discipline paragraph (:401-403) remains the section's terminal text ✓ |
| M10 | `@@ -380,6 +453,10` config rules | D-6 | ✓ full (:456-459): three named path classes, mechanical, BEFORE stage 0, "no hunt on unvalidated paths", adapt+record-as-own-entry(what/why)+proceed, dead → stop for human | Pure addition |
| M11 | `@@ -392,7 +469,8` artifacts | D-2/D-13/D-14 diagnosis line | ✓ "(per-level depth-check status)… named residuals; characterized: (a)–(c) instead" (:472-473) | Named class (diagnosis.md artifact-line extension) ✓ |
| M12 | `@@ -431,8 +509,10` stops | L-3 wiring | ✓ both stops (:512, :515): sign-off cross-ref "requirement (d)"; "≠ missing config; adaptable ones proceed" (R2-L-1 split honored; "surfaced not blocking" compressed away — the adapt+record substance lives at :458-459 — acceptable). Task-flagged move of D-2's "(a stop-for-human point)" gloss to this list: **acceptable** — no mapping row requires it at the D-2 headline; L-3's consequence (discoverable in the inventory) is met | "guesses)." → "guesses)," + verbatim re-emission of the 9b line — list-grammar extension, acceptable; gate-before-present paragraph (:517-521) remains terminal ✓ |
| S1 | `@@ -16,7 +16,8` Inputs | D-6 | ✓ compressed: "dead/unresolvable → stop; adaptable → adapt+record+proceed" (SKILL:19-20). No METHODOLOGY pointer on this clause (plan style: pointer-style) — context supplies it via "config contract in `METHODOLOGY.md`" (:18) — nitpick at most | ext ✓ |
| S2 | `@@ -42,7 +43,8` step 1 | D-8 | ✓ trigger/requirement + `(METHODOLOGY stage 1)` pointer (:46-47); gate-still-binds already in the step's own text (:43) | ext ✓ |
| S3 | `@@ -63,13 +65,18` steps 6/7/8 | D-3/D-7/D-12 (:68-69), D-5/D-13/D-14 (:74-75), D-2 (:78-79) | Step 6 ✓ (cycle def compressed "a test run **and recorded**" + `(METHODOLOGY)` pointer; per-thread + class-coverage/shared-assumption + "else gate violation"). Step 7 ✓ (rate-based pre-states rate shift + run count; depth check + coverage sweep + pointer). Step 8: **FINDING 3 (minor)** — "…ALL of (a)–(e) incl. **explicit human sign-off** (METHODOLOGY); `diagnosis.md` adds per-level depth status + named residuals" binds the diagnosis-contents addendum to the *characterized* sentence by semicolon, while METHODOLOGY :473 says characterized records "(a)–(c) **instead**" — a misparse channel; reorder the clause | ext ✓ throughout |
| S4 | `@@ -78,6 +85,7` step 9 tail | D-2/D-5/D-14 | ✓ "Characterized → symptom-evidence only; rate-based → window set up front; residuals re-checked." (:88) — pointer-style, resolves at :234-235/:253-256 | Pure addition |
| S5 | `@@ -85,9 +93,11` rep-gate + heading | D-4 | ✓ both halves + "(ledger row)" + before-consumed + `(METHODOLOGY)` (:96-98); heading "+ /detector" (:100) | ext ✓ (both named in C6) |
| S6 | `@@ -96,7 +106,7` triage item 3 | D-9 | ✓ "recorded in `decisions.md` — unrecorded = didn't happen" (:109) | ext ✓ |
| S7 | `@@ -107,14 +117,18` cold red-team + stops | D-13/D-12 aims, D-1, L-3 | ✓ aims "root or relay — deepest actionable node? what assumption does the live hypothesis set share?" (:120-121); ✓ D-1 all five elements ("reviewer hashes" compresses "reviewer-reported context hashes" — resolvable, nitpick) + "missing any = un-run" (:122-123); ✓ both stops (:129-131) with adaptable carve-out; gate-before-present closer stays terminal (:132-135) | ext ✓ ("or" relocated to the new list end — list grammar, accepted). :130-131 wrap is ragged (short line) — see missed-opportunity |
| S8 | `@@ -123,7 +137,13` self-check | D-10, D-11 | D-10 ✓: self-run sentence retained **verbatim** (:139-140); prompts/position-sensitive declared; full-loop rule; live==source; consistency ("on shared rules" — drops the plan's "every", nitpick); behavior-preservation; flagship relabeled "**aspirational — not yet run**; a standing replayable probe after its first run" with description surviving verbatim and the consequence "An unrun flagship check may not be described as an existing safeguard" (:145-149). D-11 ✓ list + resolution consequence "severed = failure" (:143-145) — **BUT see FINDING 1**: the trigger is narrowed | Named class (D-10 rewrite, obligation verbatim-or-stronger) ✓. Remains the file's final section ✓ |

**FINDING 1 (minor) — D-11's trigger narrowed in compression.** Plan row D-11 (2-plan.md:29) and the audit (0-audit-findings.md:109-111) require the cross-reference check "after any edit to **EITHER skill**" — i.e. dragonfly **or guarded-change** (the drift channel is a GC-side rename severing a reference silently, 0-audit-findings.md:104-108; the plan intro :10-13 names this exact channel as what C3/D-11 exists to watch). The built SKILL text scopes it to "Standing criteria **per edit**" (SKILL.md:142) where the governing antecedent is "non-trivial edits to **either**" = dragonfly's own two files (:141-142). The GC-side-edit trigger — the load-bearing half — is not in the built text anywhere (METHODOLOGY :394-399 states what is inherited, not when to re-check). Trigger element of the row's substance weakened → C1 partial miss. Fixable in place (one phrase, e.g. "per edit — to these files **or to guarded-change**"; see missed-opportunity for the free line).

## 2. Insertion order (position lens)

All plan-specified positions verified in the built files:
- Stage-7 cluster closes with the full-bar re-anchor incl. both records **and the chain's cold pass + gate marker** (METHODOLOGY:218-219) — last thing read at stage 7 is the bar ✓; displaced cold-pass paragraph's duty rides in the re-anchor as planned ✓.
- Stage-6 punch line is the section's final sentence (:192); refuse-to-start stays attached to its cap sentence (:181-182) ✓.
- Charter: D-12's aim is the aiming list's last item (:386); D-1/D-11 land before the closing discipline paragraph, which remains terminal (:401-403) ✓.
- Stage-9: terminal routing rule "A failed verification is never discarded…" remains last (:258-259) ✓.
- Both stop inventories: gate-before-present paragraphs remain terminal (METHODOLOGY:517-521; SKILL:132-135) ✓.
- D-2's block sits between stage 7 and stage 8, outside the "found" bar (:221-227) ✓.
- SKILL self-check remains the file's final section (:137-149) ✓. D-8 exception follows the ordering rule it excepts (:135→:142) ✓.

**No issue found on this lens** (earned: every bullet of 2-plan.md:79-115 checked against built line numbers above).

## 3. Consistency (built vs built; 9 sweep items on the BUILT text)

Shared rules across the two built files agree on trigger/requirement/consequence at every pair I checked: cycle definition (M:182-184 vs S:68 — SKILL compresses "discriminating…stage-4→5 lap" to "a test run and recorded" + pointer; agreement, not contradiction), detector both-halves (M:281-287 vs S:96-98), lite record (M:346-348 vs S:109), provenance five-elements (M:390-393 vs S:122-123), stops (M:509-515 vs S:127-131), escape (M:142-146 vs S:46-47), depth/sweep (M:207-217 vs S:74-75), characterized (M:221-227 vs S:78-79/:88 — with the Finding-3 misparse channel noted).

Sweep items, adjudicated on built text: (1) tier system intact — characterized presents cold-red-teamed established claims at tier "characterization", never "the cause" (:225-226); stage-9 exception matches (:234-235) ✓. (2) one cycle unit — ":185 (same unit…)" ✓. (3) rubric by reference, no restated text (:201-202) ✓. (4) breadcrumb points only ("see stage-1 detail", :92); the excepted rule is nowhere stated as absolute (checked :91, :135-136, S:42 — each carries or adjoins the escape) ✓. (5) "two-of-three is not 'found'" survives verbatim (:194-195); D-13/D-14 are additional-necessary, re-anchor states the superset conjunctively (:218-219) ✓. (6) silent-on-clean flagged "deliberate, strictly stronger"; capture-only boundary stated (:285-287) ✓. (7) lite keeps charter+provenance, drops exactly the five enumerated items (:342-346) ✓. (8) self-run sentence verbatim; flagship honestly labeled (:139-149) ✓. (9) **verified against GC source**: GC itself scopes the bullet — "plus the coverage-challenge bullet **for stage-3 reviews**" (Guarded_change/METHODOLOGY.md:242-243) and the bullet is titled "Challenge criteria coverage **(stage 3)**" (:251). Dragonfly's built sentence exempts only "direct stage-7 and lite passes (neither is a stage-3 review…)" and affirmatively states "a **full guarded-change triage run keeps ALL of guarded-change's own stage duties, including its stage-3 coverage challenge**: dragonfly narrows nothing inside a full-GC run" (:396-399) — it restates GC's own scoping and cannot be construed as narrowing a full-GC run ✓.

One nitpick on item 9's neighborhood: under the built definition of "unconditional" (:395), GC's label-audit bullets (GC:256-274) import into dragonfly passes where no criterion labels exist — vacuously satisfied, no contradiction, but worth a line in the stage-8 C2 record.

## 4. Cross-references (C3 preview) — quoted both sides, all resolve at 9cec23d

(GC working-tree files verified byte-identical to `9cec23d` versions — see hashes.)

- **Charter:** "see `guarded-change/METHODOLOGY.md` 'The red-team charter'" (M:378) → "## The red-team charter (stages 3 and 6)" (GC:204) ✓.
- **Provenance elements:** M:390-393 "verbatim charter, the exact context list, the reviewer's verbatim output, the agent type + model, and the reviewer-reported context hashes" → GC:236-241 "(i) the verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's verbatim output…, (iv) the reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it read" — 1:1 ✓.
- **"Unconditional discipline bullets":** M:394-396 → GC:241-243 "the four lenses + the unconditional discipline bullets, plus the coverage-challenge bullet for stage-3 reviews" — term exists verbatim ✓.
- **Severity model:** "Identical to guarded-change (see its METHODOLOGY)" (M:409) → GC:302-309 table; the four names match M:409-411 ✓.
- **Probabilistic rubric:** M:200-202 "states the **expected rate shift and run count** up front (guarded-change's probabilistic rubric, by reference)" → GC:150-153 "the criterion **states the pass rate it expects** and the number of runs that establishes it… rather than relying on a single probe"; the name "probabilistic rubric" appears verbatim at GC:166 ✓ — says what dragonfly assumes.
- **Lite/charter source of truth:** M:338-344 "guarded-change's unchanged stage-3/6 reviewer charter (four lenses + evidence discipline)… pointer back to guarded-change as the source of truth" → GC:204-235 ✓; the five scaffolding items (spec/criteria/plan/baseline/regression, M:342) match GC's doc set (GC:493-502) ✓.

**No severed or misdescribed reference found** (earned with the quotes above).

## 5. Four lenses on the built text

- **Factual (built vs plan/author claims):** author's declared numbers verified — 521/149/670 vs caps 525/152/670, combined exactly at cap; saved diff matches live. Deviations from the mapping table: Finding 1 (D-11 trigger), Finding 2 ("for the fix" deletion). All other compressions checked row-by-row above preserve trigger+requirement+consequence.
- **Logical:** Finding 3 (SKILL step-8 misparse). Nitpick: "the only other legal terminal verdict" (M:221) strictly leaves a human-directed abort at the convergence cap with no legal ending — defensible if "verdict" = claims-carrying ending (human authority at the cap is established at M:511), but the stage-8 record should note that reading. No other new contradiction found.
- **Missed opportunity (zero combined headroom):** SKILL:130-131 wraps raggedly ("adapt+record+proceed). Refuse to invent project specifics —" is a short line); repacking frees exactly the one line needed to fix Finding 1 without breaching 670. METHODOLOGY has 4 lines of local slack that the combined cap makes unusable — nothing else worth spending it on.
- **Unstated assumptions/risks:** (a) `Guarded_change/guarded-change.companion.md` is modified in the working tree, outside spec scope — the stage-8 "commit+push (one commit)" must path-scope the commit or it sweeps in an unrelated change. (b) The frozen plan's Measurement C4 still reads "caps 515/148/655" (2-plan.md:126) — superseded by the frozen criteria (1.5-criteria.md:28) and documented (decisions.md:111-115); criteria govern, but the stage-8 harness must cite the criteria file, not the plan, for C4. (c) Combined cap met with zero slack: any stage-8 fix-in-place that nets +1 line breaches gating C4 — plan the two in-place fixes as net-zero (Finding 2 costs 0 lines; Finding 1 costs 0 after the S:130-131 repack).

## Findings summary (ranked)

| # | Sev | Finding | Where |
|---|---|---|---|
| 1 | **minor** | D-11 trigger "after any edit to EITHER skill" (incl. guarded-change-side edits — the finding's core drift channel) narrowed to dragonfly-side "per edit" | SKILL.md:141-145 vs 2-plan.md:29, 0-audit-findings.md:104-111 |
| 2 | **minor** | Stage-8 handoff deletes "for the fix" — deletion-shaped hunk outside all five C6 classes (obligation survives; substance intact; frozen C6's letter fails it if unfixed) | METHODOLOGY.md:231; 6-build.diff:59-61,84-86; 1.5-criteria.md:30 |
| 3 | **minor** | SKILL step-8 semicolon binds "diagnosis.md adds per-level depth status + named residuals" to the characterized branch, contradicting-by-misparse METHODOLOGY's "characterized: (a)–(c) instead" | SKILL.md:78-79 vs METHODOLOGY.md:472-473 |
| 4 | nitpick | Frozen plan Measurement C4 caps stale (515/148/655) vs frozen criteria (525/152/670); criteria govern | 2-plan.md:126, 1.5-criteria.md:28, decisions.md:111-115 |
| 5 | nitpick | "consistency on shared rules" drops the plan's "every" | SKILL.md:143 vs 2-plan.md:28 |
| 6 | nitpick | Charter shared-assumption aim omits "one found false ranks by impact" (present at M:191; aims-list-by-design) — adjudicated acceptable | METHODOLOGY.md:386 |
| 7 | nitpick | "Only other legal terminal verdict" vs human abort at the cap — note the scoping reading in the stage-8 record | METHODOLOGY.md:221 |
| 8 | nitpick/risk | Out-of-scope working-tree change (`Guarded_change/guarded-change.companion.md`) must not ride the one-commit push; zero combined cap headroom constrains fixes to net-zero lines | git status; 1-spec.md:37-43 |

Adjudication of the author-declared compressions: handoff tightening = substance-safe but C6-class breach (Finding 2); breadcrumb reflow, punch-line merge, D-2 stop-gloss relocation, shared-assumption-aim parenthetical = all acceptable tightening (evidence cited in the table). Nothing unverifiable was encountered; every claim above was checked against the built files, the diff, the frozen plan/criteria, and GC source at 9cec23d.

**Verdict: MINOR (worst finding) → fix in place (Findings 1–3, net-zero lines via the SKILL:130-131 repack), proceed to stage 8.**
