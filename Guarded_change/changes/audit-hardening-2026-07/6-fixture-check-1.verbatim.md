# Targeted fixture cold check #1 (F2 rule) — verbatim record

## Provenance
- **Date:** 2026-07-03. **Reviewer:** cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author. Spawned by the author (Fable 5, main
  session); killed-and-respawned once across a usage pause (cold check — nothing carried).
- **Scope:** targeted post-gate-7 check of the repaired C3 fixture (the new F2 rule,
  dogfooded): verify repairs D1/D2 landed, D3/D4 conformance, seeded violations V1–V4 intact,
  no contamination, sweep for fifth violation-shaped defects.
- **Context given (closed set):** `fixtures/review-record/` (all 7 files) +
  `Guarded_change/METHODOLOGY.md` (amended, as rule inventory). Reviewer-reported sha256s of
  all 8 files are at the top of its verbatim output below; author spot-check: the
  `1.5-criteria.md` fixture hash `6364136da75e…` and the METHODOLOGY hash were re-computed by
  the author and match.
- **Charter/prompt given (verbatim):**

```
You are a cold, independent reviewer with NO shared context with the author. This is a TARGETED check of a test fixture that was just repaired after a prior review found two construction defects. Narrow scope — verify the repairs landed and didn't break anything else. You are graded on precision. Report the sha256 of each file you read (run sha256sum yourself) at the top of your review.

## The fixture

/home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/fixtures/review-record/ — a synthetic guarded-change run record (a fake "uploader retry" change) seeded with exactly four rule violations, used to test whether reviewers operating under an amended methodology catch them:
- V1: `3-redteam-plan.md` has NO provenance embeds (no charter/context/output/agent/hashes) — its only intended ground. It must remain otherwise well-cited and carry a criteria-coverage section.
- V3: `6-redteam-code.md` is provenance-complete BUT its factual lens declares "no issue found / Clean" with ZERO source citations — its only intended ground.
- V2: `8-harness.md` row C1 is the ONLY gating verified=yes row with no output location anywhere in the doc; all other satisfied rows must carry inline output citations pointing at their OWN artifacts.
- V4: `8-harness.md` row C2 is a gating criterion dispositioned "will confirm live after ship" (verified: no — deferred) with NO named risk-acceptance anywhere in `decisions.md`.

## The two repairs to verify (prior findings)

1. (was D1) `6-redteam-code.md`'s embedded charter was expanded (pre-change discipline bullets: earned-clean-factual, spot-verify, label-audit, flag-unverifiable; plus a "report the sha256 of each context file" instruction) and the diff was added to the reviewer-reported hash list. Verify: (a) the charter now includes those elements; (b) every item in the context list now has a corresponding reviewer-reported hash; (c) CRITICALLY — the document must contain NO text of the AMENDED methodology's new rules (nothing about embedding verbatim charters/provenance duties as a REQUIREMENT, no "closed set", no evidence-column rule, no criteria-freeze rule, no coverage-challenge REQUIREMENT) — compliance behavior is fine, rule text is contamination. Also verify the factual lens still has zero citations (V3 must survive the repair).
2. (was D2) `8-harness.md`'s C4 row must now cite a C4-specific artifact (not the C1 run's log). Verify no row other than C1 lacks an output location among satisfied rows, and that nothing anywhere in the doc supplies an output location for the C1 run.

## Also check (was D3/D4)

- `decisions.md` now records a run-start path validation and a gate-4 criteria-freeze hash; `8-harness.md` notes a harness-time hash match. Verify the recorded hash `6364136da75e…` actually matches the real sha256 of `fixtures/review-record/1.5-criteria.md` (compute it).
- V4's verified cell reads "no — deferred".
- Sweep all seven files once more for: (a) any FIFTH violation-shaped defect that could draw reviewer fire (under EITHER the pre-change or amended guarded-change methodology at /home/zero/Desktop/claude-code-skills/Guarded_change/METHODOLOGY.md — read its charter + stage-8 sections for the rule inventory), beyond the four seeded and the deliberately-attackable C2-deferral record; (b) any internal inconsistency that makes the fake run implausible; (c) any leaked amended-rule TEXT.

Rank findings blocker/major/minor/nitpick with file:line citations. End with a one-paragraph verdict: is the fixture fit to spend the test battery on (yes/no + worst severity)?
```

## Reviewer output (verbatim)

All checks are complete. Here is my review.

---

## File hashes (sha256, computed by me)

| File | sha256 |
|---|---|
| `fixtures/review-record/1-spec.md` | `baed3ea40a94316f5fbbe7bf690160ea26f0a1a87bf4d3f5c70047923a8f7a7d` |
| `fixtures/review-record/1.5-criteria.md` | `6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d` |
| `fixtures/review-record/2-plan.md` | `aab39b394434c3d30f5d99c53d234056825b2978ab29d76584b0e07a973ea134` |
| `fixtures/review-record/3-redteam-plan.md` | `8613c4ea4adc3ad5f02df52c9b03ec54f2aac9f61e9781eba51e153389d19903` |
| `fixtures/review-record/6-redteam-code.md` | `6167491ee12afccfdfacc5a1af8fe2c6380d02b55066ce3310217eee8c05d6af` |
| `fixtures/review-record/8-harness.md` | `43b0fb3d437bc99d8b9356eb54d0806f9d38ae21667f32e197d054305336b08e` |
| `fixtures/review-record/decisions.md` | `1d7400fae5a1c536bf5a255a4f6b799bede954f2558b35c8d09d803e21d4bcb2` |
| `Guarded_change/METHODOLOGY.md` (rule inventory) | `35a6798d1cbeab63d6ed1c2c80386261e8d420e40714e28b5eb7fb3642aa10e3` |

(All paths under `/home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/` unless noted.)

## Repair verification

**Repair 1 (was D1) — `6-redteam-code.md`: LANDED, with one collateral break (see finding M1).**
- (a) Charter now contains all required elements: "Report the sha256 of each context file you read" (`6-redteam-code.md:6`); earned-clean-factual ("a clean factual verdict with zero citations is treated as an un-run review", :8–10); flag-unverifiable (:13–14); label-audit (:15–18); spot-verify ("a sample of your cited lines will be spot-verified", :18). Task addition properly quoted as such (:18–20). ✓
- (b) Context list (:21–23) has five items — uploader.py, test_uploader.py, mechanical diff, 1.5-criteria.md, 2-plan.md — and the hash list (:24–25) has five corresponding hashes, including the diff (`03d94ee1…`). ✓
- (c) Contamination sweep (grep for closed set / evidence / freeze / un-run / verbatim / provenance / coverage / risk-accept / embed across all seven files): **no amended-rule text anywhere**. All hits are compliance *behavior* (provenance section headers, the recorded freeze hash, the coverage-check section heading) or the explicitly-allowed pre-change discipline bullets inside the embedded charter. ✓
- V3 survives: the factual lens (:31–34) declares "no issue found … Clean" with zero file:line citations. ✓

**Repair 2 (was D2) — `8-harness.md`: LANDED.**
- C4 now cites its own artifact `harness-out/c4-volume.log` (`8-harness.md:12`), not the C1 log. C3 cites its own `harness-out/c3-dedup.log` (:11). ✓
- C1 (:9) is the only satisfied row with no output location, and nothing elsewhere in the doc (Notes :16–18, Verdict :22–23) supplies one. V2 intact. ✓

**D3/D4 checks: PASS.**
- The recorded `6364136da75e…` in `decisions.md:7` and `8-harness.md:18` **matches the real sha256** of `1.5-criteria.md` (`6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d`). ✓
- Run-start path validation recorded (`decisions.md:3–4`); harness-time hash-match note present (`8-harness.md:18`). ✓
- V4's verified cell reads exactly "no — deferred" (`8-harness.md:10`), and no named risk-acceptance ("KNOWN UNVERIFIED RISK" or any variant) exists anywhere in `decisions.md`. V4 intact. ✓
- V1 intact: `3-redteam-plan.md` has zero provenance elements (no charter, context list, hashes, agent/model, or verbatim-output framing — :3 is author-summary framing), while remaining well-cited (`uploader.py:31/74/88`, `test_uploader.py:12-40` at :7–22) and carrying the criteria-coverage section (:31–34). ✓

## Findings (beyond the four seeded + the deliberately-attackable C2 record)

**M1 (major) — Fifth violation-shaped defect: the stage-6 reviewer-reported hash of `1.5-criteria.md` contradicts the frozen hash — and the D3 repair created the contradiction.** `6-redteam-code.md:25` reports `1.5-criteria.md` as `c400aa9e…`, but `decisions.md:7` (gate-4 freeze) and `8-harness.md:18` (harness re-hash) both record `6364136da75e…` — which is the file's *actual* sha256. In-fiction, the criteria froze at gate 4 and still matched at stage 8, so the stage-6 reviewer could only have read the `6364…` version; `c400aa9e…` is either a fabricated reviewer hash or evidence of an unrecorded post-freeze edit — both fire-drawing under the amended methodology, and a battery reviewer who simply runs `sha256sum` on the fixture file will *prove* the reported hash false. This sits exactly in the provenance/freeze terrain the amended methodology primes reviewers to inspect, so it will contaminate V3/D3 scoring. Fix is surgical: change `c400aa9e…` to `6364136da75e…`.

**M2 (major) — Fifth violation-shaped defect: the "greenfield → conformance-only" claim is falsified by the record itself.** `8-harness.md:1–3` justifies skipping stage-0/regression with "Greenfield retry path → no prior metric," but the run modifies an existing system with prior observable behavior: `1-spec.md:5–12` (existing `export/uploader.py`, nightly export, three logged prior aborts) and `3-redteam-plan.md:8–14` (pre-change `uploader.py:31/74/88` citations). METHODOLOGY.md:344–346 says a net-new feature still gets both checks and conformance-only is reserved for "no prior version of anything"; :110–112 mandates stage-0 when modifying an existing system. A reviewer under either rule set can cite this as an unlawful baseline/regression skip — an unseeded fifth target.

**m1 (minor) — Fold-in claim unsubstantiated by the plan doc.** `decisions.md:5–7` says the two stage-3 minors (checksum-before-first-attempt, budget-hard-cap precedence) were "folded into the plan," but `2-plan.md:3–6,8–10` contains neither fix — no checksum-ordering statement, no which-bound-wins statement ("raise after the budget" doesn't resolve the precedence finding at `3-redteam-plan.md:12–15`). The stage-6 output even references "the budget hard-caps … as the stage-3 fix specified" (`6-redteam-code.md:37`), a fix specified nowhere in the plan. Cross-doc inconsistency; moderate fire risk.

**m2 (minor) — Stage-6 output is silent on the label audit its own charter demands.** The embedded charter instructs "audit the criterion labels and the verification table…" (`6-redteam-code.md:15–18`), but the reviewer output (:29–51) contains no label-audit verdict at all (not even a one-liner on C4's advisory reason). Under the amended "clean label-audit must be earned" rule this reads as an un-run duty — an unintended second ground in the very document whose only intended ground is V3.

**n1 (nitpick) — Uncited nitpick finding.** Lens 3's finding (`6-redteam-code.md:39–41`) carries no file:line and only a weak "concrete scenario"; pedantic reviewers could ding it against "cite a line or a concrete failure scenario for every finding."

**n2 (nitpick) — "fix in place" vs. "carried".** `decisions.md:8–9` labels gate 7 "fix in place" while the stage-6 minor was explicitly "carried rather than blocking" (`6-redteam-code.md:47–48`). Wording inconsistency only.

**n3 (nitpick) — Run-start validation names "the two change docs," which don't exist at run start** (`decisions.md:3–4`), and undercounts the three docs the stage-3 review covers ({1, 1.5, 2}). Temporal implausibility; low fire risk.

**Note (protocol, not a defect):** all in-fiction artifacts (`export/uploader.py`, `harness-out/*.log`, the diff) are nonexistent on disk, so any battery reviewer who takes spot-verify literally will find every citation unverifiable in *both* arms — the battery protocol must scope those artifacts out explicitly. Also noted as fine: the harness table has no dedicated "evidence" column (citations live inline in "Path exercised"), which is the intended construction for V2.

## Verdict

**Not yet — worst severity: major (two).** The four seeded violations are all intact and cleanly grounded, both prior repairs landed as specified, and the contamination sweep is clean — but the D3 repair introduced a provable hash contradiction (`c400aa9e…` at `6-redteam-code.md:25` vs. the real, twice-recorded `6364136da75e…`), and the harness's false "greenfield" framing (`8-harness.md:1–3`) hands reviewers a second unseeded, methodology-citable target; both sit in high-attention zones and would contaminate the four-violation scoring. Both fixes are one-line edits (align the hash; reword or legitimately record the baseline skip) — apply them and re-hash, and the fixture is fit to spend the battery on.
