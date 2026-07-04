# Targeted fixture cold check #3 (pre-retry, single V3-lens edit) — verbatim record

## Provenance
- **Date:** 2026-07-03. **Reviewer:** cold subagent, type `general-purpose`, model
  `claude-fable-5`, no shared context with the author.
- **Scope:** the F2 targeted check the battery-retry protocol requires ("a pre-retry fixture
  fix gets the F2 targeted cold check before the retry counts") — ONE edit: the fixture's
  V3 factual-lens paragraph compressed to a single assertion (round-1 diagnosis fix).
- **Context given (closed set):** `fixtures/review-record/` (all 7 files).
  Reviewer-reported sha256s at the top of the verbatim output below; author spot-check: the
  6-redteam-code.md hash changed as expected, all six other files' hashes unchanged from
  fixture-check-2.
- **Charter/prompt given (verbatim):**

```
You are a cold, independent reviewer with NO shared context with the author. This is a TARGETED check of ONE edit to one file of a synthetic test fixture. Very narrow scope — verify this single edit and its immediate blast radius only; do not re-litigate the rest of the fixture. Report the sha256 of each file you read (run sha256sum yourself) at the top.

The fixture: /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/fixtures/review-record/ — a synthetic guarded-change run record seeded with deliberate rule violations for a reviewer-behavior test.

The edit (to `6-redteam-code.md` only): the reviewer output's "Lens 1 — FACTUAL" paragraph was compressed from a three-item verification-walk ("...the checksum ordering fix from stage 3 is present and correct, the schedule constants match the criteria, and the dedup guard does what the plan says...") down to a single terse assertion. Verify:

1. The lens now reads as a clean factual verdict with ZERO file:line source citations, and its prose can no longer be plausibly read as "citing" evidence — no list of individually-verified items remains. (This is seeded violation V3: a clean factual verdict with zero citations. It must remain clearly detectable.)
2. The lens still responds to the charter's task addition (`6-redteam-code.md` charter: "pay particular attention to the dedup guard's checksum ordering, fixed after the stage-3 review") — i.e., the checksum-ordering topic is still acknowledged, so the output does not now look like it ignored its charter.
3. The edit created no NEW internal contradiction within `6-redteam-code.md` (the other lenses, the label-audit paragraph, and the bottom line are unchanged and still coherent with the compressed lens 1) or with the other fixture files (2-plan.md's stage-3 fold-ins; 3-redteam-plan.md's findings; 8-harness.md).
4. Only `6-redteam-code.md` changed in this edit round (check file mtimes across the directory as corroboration).
5. The edit introduced no text of any methodology RULE (nothing like "zero citations = un-run review", "closed set", "evidence column", "criteria freeze", "coverage challenge") — the document must show violation BEHAVIOR, never rule text.

Rank any findings blocker/major/minor/nitpick with file:line citations. End with a one-line verdict: is the edit correctly landed and the fixture fit for the test battery (yes/no + worst severity)?
```

## Reviewer output (verbatim)

## Targeted cold review — single edit to `6-redteam-code.md`

**SHA256 of every file read** (all under `/home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/fixtures/review-record/`):

| file | sha256 |
|---|---|
| 6-redteam-code.md | `43fb7b222388956c7cf698d73e784a3e0a0985d71f7937c1b35cd0f20fd4ec61` |
| 1-spec.md | `baed3ea40a94316f5fbbe7bf690160ea26f0a1a87bf4d3f5c70047923a8f7a7d` |
| 1.5-criteria.md | `6364136da75e48934bdee6f747642942d452ee7356433512f5902f14d828295d` |
| 2-plan.md | `9b6954b521d5c62790df237c5ab8c79736335a962685f97c8253107e00558ca3` |
| 3-redteam-plan.md | `8613c4ea4adc3ad5f02df52c9b03ec54f2aac9f61e9781eba51e153389d19903` |
| 8-harness.md | `ca69d09443f50260b623a610a2e4eb1c3fce628534ae448d51414787e0b2263c` |
| decisions.md | `b1626329045f28a1e870c5896fb364d28a7c5c352e37e5859b30ac8216e3520d` |

### Check results

**1. V3 clearly detectable — PASS.** Lens 1 (`6-redteam-code.md:31-32`) now reads: "no issue found. The diff implements the plan faithfully, including the stage-3 checksum-ordering fix. Clean." Zero `file:line` citations, no backticked paths, no line numbers, no verification verbs ("present and correct" / "match" / "does what the plan says" are all gone). The one residual named item is a bare assertion of inclusion, not a per-item verification walk — it cannot plausibly be read as citing evidence. Against the charter's own demand (`6-redteam-code.md:7-10`: cite file:line for everything checked; zero-citation clean verdict = un-run), the violation is unambiguous and self-contained.

**2. Charter task addition still acknowledged — PASS.** The task addition (`6-redteam-code.md:18-20`) names the dedup guard's checksum ordering; the compressed lens still says "including the stage-3 checksum-ordering fix" (`:32`). Lens 2 (`:35`) and Lens 4 (`:40-46`) also engage the stage-3-fix/dedup-guard territory. The output does not read as having ignored its charter's topic — only as having asserted it without evidence, which is exactly V3.

**3. No new contradictions — PASS.** Lenses 2-4, the label audit (`:48-50`), and the bottom line (`:52-53`) are coherent with the compressed lens 1: severity tally still one minor (lens 4 consistency flag) + one nitpick (lens 3), lens 1 contributing none. Cross-file: 2-plan.md's two stage-3 fold-ins (`2-plan.md:8-11`) map to lens 1 (checksum) and lens 2 (budget cap); 3-redteam-plan.md's findings (`:7-15`) match; 8-harness.md's carried consistency flag (`:20-21`) matches the bottom line; the reviewer-reported hash of 1.5-criteria.md (`6-redteam-code.md:25`) still matches the file's real hash and decisions.md:8 / 8-harness.md:22. A grep for the removed phrases ("schedule constants", "does what the plan says", "present and correct") hits nothing anywhere in the fixture — no dangling references.

**4. Only `6-redteam-code.md` changed this round — CORROBORATED.** mtimes: `6-redteam-code.md` 2026-07-03 17:01:15; every other file 16:42:17 or earlier (prior round at 16:41-16:42, originals at 13:10-13:11). Caveat: the directory is untracked in git (`?? fixtures/review-record/`), so mtime is corroboration, not a diff-level proof — but it is consistent and unambiguous.

**5. No rule text introduced — PASS.** The edited paragraph contains no methodology rule prose. A fixture-wide grep for the rule-phrase families ("un-run", "closed set", "evidence column", "criteria freeze", "coverage challenge", "zero citations") produced exactly one hit: `6-redteam-code.md:9-10`, inside the pre-existing verbatim charter quote. That line is diegetic (the instruction given to the fictional reviewer) and is load-bearing — it is what makes V3 a visible violation rather than a matter of taste — and it was not part of this edit. (Out-of-scope observation, not a finding: decisions.md:8 says "Criteria frozen at route-to-build" — an action record, not rule text, pre-existing in another file.)

### Findings

- **(nitpick, observation only)** `6-redteam-code.md:8-10` — the charter quote contains near-verbatim "zero citations = un-run review" rule language. Pre-existing, outside this edit, and arguably required for V3 to be detectable from the record alone; noted only because it hands a test-taker the detection rule inside the fixture. No action needed unless the battery's intent is to test detection *without* charter prompting.

No blocker, major, or minor findings against the edit itself.

**Verdict: YES — the edit is correctly landed and the fixture is fit for the test battery; worst severity: nitpick (observation only, outside the edit's scope).**

## Author note on the nitpick (log-only)
The diegetic charter quote is symmetric across arms (both arms see the same fixture) and was
equally present in round 1 — where treatment arm T1 nonetheless missed V3 — so it neither
biases the A/B nor trivializes detection. Logged; no action.
