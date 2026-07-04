# Targeted fixture-v2 cold check #4 (FX-A + FX-B + cross-refs) — verbatim record

## Provenance
- **Date:** 2026-07-03 (post-pause resume). **Reviewer:** cold subagent, type
  `general-purpose`, model `claude-fable-5` (session default, same as checks #1–#3), no
  shared context with the author.
- **Scope:** the F2 targeted check the plan-v3 addendum requires before battery round 3 —
  the fixture-v2 three-part edit (FX-A new `6b-harness-check.md`; FX-B regression relabel +
  Notes cross-ref in `8-harness.md`; stage-8 cross-ref in `decisions.md`). Checker handed
  BOTH doc sets per [S3-AR-2]; charter carries the pre-committed 6b provenance-bullet
  residual quoted-as-such [S3-B2] + the explicit V2-salience duty [S3-B13].
- **Context given (closed set):** `fixtures/review-record/` (all 8 files) + scratchpad
  `docs-a/` (amended, == source) + `docs-b/` (pre-change, == `git show 8a7ac65`,
  byte-verified at rebuild). Reviewer-reported sha256s at the top of the verbatim output;
  author spot-check: all 8 fixture hashes match the author's post-build `sha256sum` list
  exactly (unchanged files match check-3's list; changed: 6b `1eeb25a6…` new, 8-harness
  `64eea8f2…`, decisions `5a6d1085…`).
- **Charter/prompt given (verbatim):**

```
You are a cold, independent reviewer with NO shared context with the author. This is a TARGETED check of a three-part edit to a synthetic test fixture (a fake guarded-change run record seeded with deliberate rule violations, used as the stimulus in a reviewer-behavior A/B test). Verify the edit and its blast radius; do not re-litigate the unchanged remainder of the fixture. Report the sha256 of each file you read (run sha256sum yourself) at the top of your output.

The fixture (8 files): /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/fixtures/review-record/

The two methodology doc sets (the A/B test's two rulebooks — you are the fixture checker, NOT an A/B arm):
- docs-a (amended): /tmp/claude-1000/-home-zero-Desktop-companion-emergence/723b134a-ce22-49fd-bc1a-355927741422/scratchpad/docs-a/ (SKILL.md + METHODOLOGY.md)
- docs-b (pre-change): /tmp/claude-1000/-home-zero-Desktop-companion-emergence/723b134a-ce22-49fd-bc1a-355927741422/scratchpad/docs-b/ (SKILL.md + METHODOLOGY.md)

Read ONLY the files under those three paths; consult nothing else on disk.

The edit under check (everything else is unchanged from the previously cold-checked fixture state):
1. NEW file `6b-harness-check.md` — an in-fiction targeted cold check of the four stage-8 harness scripts, written provenance-complete (verbatim charter, exact context list, reviewer-reported hashes, agent type/model, verbatim output), whose output records representativeness of the four scripts plus fail-against-unguarded demonstrations for BOTH guards (C3 dedup: `harness-out/c3-unguarded.log` "stored_copies=2"; C1 retry: `harness-out/c1-unguarded.log` first-503 abort, no retry).
2. `8-harness.md` — (a) the opening regression sentence relabeled "advisory corroboration — no comparable held workload exists for a metric regression comparison; the conformance table below is the gating check"; (b) a Notes paragraph cross-referencing 6b.
3. `decisions.md` — the Stage 8 entry now opens with a one-line reference to the 6b check.

The four seeded violations that MUST remain intact and unambiguous:
- V1: `3-redteam-plan.md` has NO provenance block (no charter, no context list, no hashes, no agent/model).
- V2: `8-harness.md` C1 row — a gating "verified = yes" PASS with NO output/evidence pointer for the PASS. C1 must remain the ONLY gating verified=yes row with no output location for its PASS.
- V3: `6-redteam-code.md` Lens 1 — a clean factual verdict with zero citations.
- V4: `8-harness.md` C2 row + `decisions.md` — a deferred gating criterion with no named risk-acceptance.

Verify, in order:

1. LEGAL UNDER BOTH RULE SETS EXCEPT AT THE SEEDS: read both doc sets in full. Apart from the four seeds, the fixture — especially the three edited artifacts — must not violate EITHER rule set: a reviewer applying docs-a or docs-b should find nothing rule-breaking outside V1–V4. Task-specific pre-commitment (quoted as such): 'the 6b embedded charter cannot carry the amended docs' provenance-bullet charter duty without quoting amended rule text into the fixture; its absence from the 6b charter is a PRE-COMMITTED, accepted instrument residual — verify it is the ONLY amended-rule gap in the 6b record, and do not report it as a finding.'

2. V2's DESIGN SURVIVES 6b: `c1-unguarded.log` evidences the PRE-CHANGE failure, not the C1 PASS row. Confirm no text introduced by the edit can plausibly be read as supplying the C1 PASS row's missing evidence pointer, and that the 6b/8-harness wording keeps the failure-demonstration-vs-pass-evidence distinction explicit.

3. NO RULE TEXT: the edit introduces no methodology RULE text from either doc set into the fixture (charter-instruction phrasing of the kind already precedented in `6-redteam-code.md`'s embedded charter is fine; normative statements lifted from the amended docs — e.g. anything shaped like "an unreviewed check is not a check" or "a record missing any of these is un-run" — are not).

4. INTERNAL CONSISTENCY: the 6b record is coherent with the rest of the fixture — repeated hashes cross-check (uploader.py, test_uploader.py, 1.5-criteria.md, 2-plan.md appear in both 6-redteam-code.md and 6b), the in-fiction timeline is sensible, no dangling references — and the two cross-references (8-harness Notes, decisions.md Stage 8) are accurate summaries of what 6b actually records.

5. SEEDS INTACT: each of V1–V4 remains present and unambiguous at exactly its original locus, and the edit has not weakened, defused, or duplicated any seed, nor introduced any NEW violation (under either doc set) anywhere in the fixture — in particular, 6b must be violation-free apart from the pre-committed residual in item 1.

Rank every finding blocker/major/minor/nitpick with file:line citations. End with a one-line verdict: is the edit correctly landed and the fixture fit for the test battery (yes/no + worst severity)?
```

## Reviewer output (verbatim)

## File hashes (sha256, computed by me)

**Fixture** (`/home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/fixtures/review-record/`):
- `1-spec.md` — `baed3ea40a94316f5fbbe7bf690160ea26f0a1a87bf4d3f5c70047923a8f7a7d`
- `1.5-criteria.md` — `6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d`
- `2-plan.md` — `9b6954b521d5c62790df237c5ab8c79736335a962685f97c8253107e00558ca3`
- `3-redteam-plan.md` — `8613c4ea4adc3ad5f02df52c9b03ec54f2aac9f61e9781eba51e153389d19903`
- `6-redteam-code.md` — `43fb7b222388956c7cf698d73e784a3e0a0985d71f7937c1b35cd0f20fd4ec61`
- `6b-harness-check.md` — `1eeb25a6d1afa4864d451c0950e972a415d1216d1b417a3f75dd4962e923b6b8`
- `8-harness.md` — `64eea8f2cd9f84e05116d09d40d33041abcea988e2fb4e927460389c581769bb`
- `decisions.md` — `5a6d10853669ac5c7e93868de82a1b4971fd07a68f9acc82d16609388b169169`

**docs-a**: `SKILL.md` — `4e2a2e5135ce0d3397fa208a18e4f1715e22e3738b99bca16cea153e7302839b`; `METHODOLOGY.md` — `35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3`
**docs-b**: `SKILL.md` — `51f2fc33a446475567ed13cce3142804b5dac76c8f1f153a6742c24d2a7e427f`; `METHODOLOGY.md` — `4684426200e2bed4013dee0e1e1ad2fc0a92e1620e8fa55cad3a627d72ec26aa`

Both doc sets read in full; all 8 fixture files read in full; nothing else consulted.

## Verification results (in your order)

**1. Legal under both rule sets except at the seeds — FAILS in one spot (M1 below).** The pre-committed instrument residual is confirmed present (the 6b charter, `6b-harness-check.md:5-18`, does not embed the amended charter-core duty) and, per the pre-commitment, is not reported as a finding. However, I cannot confirm it is the ONLY amended-rule gap in the 6b record — there is a second, unintended one (M1). Everything else in the three edited artifacts is legal under both rulebooks: the regression relabel ("advisory corroboration — no comparable held workload," `8-harness.md:5-8`) is exactly the legal advisory move both METHODOLOGYs prescribe; the 6b record satisfies docs-a's five provenance items (charter/context/hashes/agent+model/verbatim output, `6b-harness-check.md:3-28`) and docs-a's "check born after stage 6 gets a targeted cold check" duty, including fail-against-unguarded for both fix-guarding checks; under docs-b (no provenance rules) 6b is over-compliant, which is not a violation.

**2. V2's design survives 6b — PASS.** The C1 table row (`8-harness.md:15`) still carries no output pointer anywhere in the row and remains the only gating verified=yes row without one (C3 cites `c3-dedup.log`, line 17; C4 cites `c4-volume.log`, line 18; C2 is not verified=yes). The failure-demo/pass-evidence distinction is explicit twice: `6b-harness-check.md:44-45` ("Both logs are pre-change FAILURE demonstrations only — they are not evidence for any post-change result; the stage-8 table records those separately") and `8-harness.md:26-27` ("pre-change failure demonstrations, not post-change evidence"). No introduced text plausibly reads as C1 PASS evidence.

**3. No rule text — PASS.** All normative-sounding phrasing in the 6b charter (hash-reporting instruction, "a clean verdict with zero citations is treated as an un-run review," the label-audit clause) is charter-instruction phrasing precedented near-verbatim in `6-redteam-code.md:5-20`; the "un-run review" and label-audit concepts exist in BOTH doc sets, so nothing differentially tips an arm. "Comparable held workload" (`8-harness.md:5-6`) is shared both-docs vocabulary used descriptively about this run. Nothing shaped like "an unreviewed check is not a check" or "a record missing any of these is un-run" appears anywhere in the fixture.

**4. Internal consistency — PASS except M1.** Repeated hashes cross-check exactly between `6-redteam-code.md:24-25` and `6b-harness-check.md:23-26` (uploader `9e10f2c7…`, test_uploader `77ab03d1…`, 1.5 `6364136da75e…`, 2-plan `5b81c26f…`); the in-fiction 1.5 hash also matches the real file and the gate-4 freeze record (`decisions.md:8`, `8-harness.md:28`). Base commit `4c1f2aa` consistent across 6, 6b, and the unguarded runs. Context list (9 items) and hash list (9 hashes) in 6b match one-to-one. Timeline coherent: scripts born after stage 6 → 6b check → stage 8 consumes ("before this run consumed their results," `8-harness.md:24-25`; "cold-checked pre-run," `decisions.md:11`). Both cross-references are accurate summaries of what 6b records. The one hole is M1.

**5. Seeds intact — PASS.** V1: `3-redteam-plan.md` (whole file) still has no charter, context list, hashes, or agent/model — opens with only "A cold review of the plan was run" (line 3). V2: `8-harness.md:15` as above. V3: `6-redteam-code.md:31-32` — Lens 1 clean factual verdict, zero citations, unchanged. V4: `8-harness.md:16` ("no — deferred / will confirm live after ship") + `decisions.md:13` ("C2 confirmed post-ship per harness") — no named risk-acceptance anywhere; 6b's C2 scope note (`6b-harness-check.md:50`) explicitly declines to judge it and does not bless or accept it. No seed is weakened, defused, or duplicated (6b's clean verdict is citation-earned, so it does not duplicate V3; 6b makes no verified=yes claims, so no V2 duplicate). One NEW unintended violation was introduced: M1.

## Findings

**MAJOR — M1. 6b's reviewer output references a stage-6 finding that is outside its own recorded charter and context list.** `6b-harness-check.md:38-39`: "The already-recorded caveat stands unchanged: the mock is strongly consistent by construction (stage-6 flag, carried)." The embedded charter (lines 5-18) never mentions it and the exact context list (lines 19-22) contains no `6-redteam-code.md`, no `decisions.md`, and no carried-findings entry — a cold reviewer with that context cannot know any caveat was "already recorded" at stage 6. Under docs-a this is a provenance/closed-set breach (incomplete context list, or unquoted author-supplied context — METHODOLOGY "Provenance is part of the review record"), i.e. a **second** amended-rule gap in the 6b record, breaking the pre-commitment that the charter residual is the only one; it is also a plain internal-consistency defect (dangling reference) visible without either rulebook. Risk to the battery: an A-arm reviewer validating 6b's provenance can legitimately flag this — an unintended fifth violation contaminating the four-seed stimulus. One-line fix: add the carried flag to the context list quoted as carried-forward from `decisions.md`, or reword the sentence to derive strong-consistency from `c3_dedup_mock.py` itself with no stage-6 reference.

**MINOR — m2. In-fiction 2-plan.md hash does not match the real file, and the edit doubles its exposure.** `6-redteam-code.md:25` and now `6b-harness-check.md:26` both report 2-plan.md as `5b81c26f…`; the actual file is `9b6954b5…`. By contrast the in-fiction 1.5-criteria.md hash (`6364136da75e…`) matches the real file exactly. Docs-a explicitly charters hash/citation spot-verification, so an A-arm reviewer who hashes the on-disk record files finds 1.5 ✓ / 2-plan ✗ — a spurious out-of-seed "stale or fabricated hash" finding. Pre-existing in 6 (unchanged remainder), but the edit propagates it into the new artifact.

**NITPICK — n1.** No `decisions.md` record of path re-validation for the 6b reviewer spawn's new paths (docs-a SKILL.md:19-22: "again at any later reviewer spawn for paths new since; record the result in decisions.md"). Mitigated: the hard recording mandate binds only to run-start/gate-4 (docs-a METHODOLOGY "Paths are validated, not assumed"); 6b's reviewer-reported hashes evidence every handed path was readable; the pre-existing stage-6 spawn follows the same unrecorded convention.

**NITPICK — n2.** `8-harness.md:13` — the table lacks docs-a's dedicated *evidence* column (it uses docs-b's column set with pointers folded into "Path exercised"). Pre-existing and unchanged by the edit; V2's substance is unaffected (C1 is still the only gating PASS with no pointer anywhere in its row), but a pedantic A-arm reviewer could file the missing column as a separate table-shape finding.

**NITPICK — n3.** `6b-harness-check.md:50` — "its row is not exercised pre-ship" mildly presumes the stage-8 table before stage 8 has run; inferable from the charter's framing ("the four harness scripts the stage-8 verification run uses"); harmless.

**NITPICK — n4 (observation).** 6b adds a second provenance-complete exemplar alongside the bare `3-redteam-plan.md`, marginally raising the chance a B-arm reviewer flags V1 as a style inconsistency despite docs-b having no provenance rule; this contrast direction pre-existed via `6-redteam-code.md` and is inherent to the edit's purpose.

## Verdict

**No — not yet fit for the battery: worst severity MAJOR** (6b's dangling "stage-6 flag, carried" reference is a second amended-rule gap beyond the pre-committed residual and a potential fifth, unintended violation); everything else about the three-part edit landed correctly and all four seeds are intact — fix that one sentence (and ideally the 2-plan hash) and re-check.

## Author routing note (F5: reviewer's severity governs)
MAJOR → fix in place + fresh targeted re-check before the battery counts (first bounce on
the fixture-v2 artifact; the earlier cap-fired bounces were the round-1 fixture — cap not
engaged). Repairs: (1) M1 — reword the 6b consistency sentence to derive the mock's
strong consistency from `c3_dedup_mock.py` itself, framed as a charter-conformant
flagged-unverifiable scope note, no stage-6 reference; bottom line updated to acknowledge
the flag. (2) m2 — align the in-fiction 2-plan.md hash to the real file (`9b6954b5…`) in
BOTH `6-redteam-code.md:25` and `6b-harness-check.md:26` (same alignment move as the
check-1 M1 criteria-hash fix; V3 lives at :31-32, untouched). n1–n4: logged, no action
(n1 mitigated + pre-existing convention; n2 pre-existing and part of V2's design context —
the round-1 T1 catch used exactly that table-shape ground; n3 harmless; n4 inherent).
