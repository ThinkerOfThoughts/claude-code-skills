# 3 — Red-team of the plan (verbatim record)

## Provenance
- **Reviewer:** cold `general-purpose` subagent, no shared context (agentId a39abaae26434c31c),
  Claude Opus 4.8.
- **Charter given:** the five-lens charter core verbatim (Factual, Logical, Missed-opportunity,
  Unstated-assumptions/risks incl. the position lens, Fidelity) + the unconditional discipline
  bullets (cite-or-it-doesn't-count, rank, flag-unverifiable, clean-per-lens-allowed,
  clean-factual-earned, clean-fidelity-earned, report-hashes) + the stage-3 additions (CH8
  coverage-challenge mandatory, CH9/CH10 label audit). Full prompt archived in the run transcript
  (the Agent call preceding this record).
- **Context list (closed set):** the three change artifacts (1-spec, 1.5-criteria, 2-plan — the
  last carries the verbatim proposed text for both edits) + the skill source being edited
  (stages/stage-8.md, stages/stage-1.5.md) + consistency sources (stages/charter.md,
  stages/stage-3.md, SKILL.md, METHODOLOGY.md) + tree-wide grep. Paths validated (decisions.md).
- **Reviewer-reported reads (sha256, run-start snapshot):** 1-spec 9ea1a890…d84a14;
  1.5-criteria 1c08bdf0…8e6d1b3; 2-plan ab46d8c8…96cd63d; stage-8 d737f1bc…af41e8a39 (base
  `d737f1bcf3adcacb00585c5ea387c2ff9a1c408a1417068c2b0b2bd8eaf41a39`); stage-1.5 d262a147…e5e4bd66;
  charter 760cd577…f1b2ffe; stage-3 48aa7a7c…03b7192c. (Author re-computed these at spawn; match.)
- **Record form:** the reviewer's full verbatim final report is embedded below (delivered as its
  task deliverable). Every finding was independently reproduced by the author (consumer spot-verify
  duty CH6 — commands + outputs in decisions.md). The author's adjudication summary follows the
  verbatim block.

## Verdict: **BLOCKER** (route back to fix plan + criteria)

---
## REVIEWER VERBATIM FINAL REPORT (round 1)

> # STAGE-3 COLD RED-TEAM REVIEW — oracle-validity-h6
>
> **Agent type:** general-purpose (cold reviewer). **Model:** claude-opus-4-8.
>
> **sha256 of files actually read:**
> ```
> 9ea1a890…d84a14  changes/oracle-validity-h6/1-spec.md
> 1c08bdf0…8e6d1b3  changes/oracle-validity-h6/1.5-criteria.md
> ab46d8c8…96cd63d  changes/oracle-validity-h6/2-plan.md
> d737f1bc…af41e8a39  stages/stage-8.md
> d262a147…e5e4bd66  stages/stage-1.5.md
> 760cd577…f1b2ffe  stages/charter.md
> 48aa7a7c…03b7192c  stages/stage-3.md
> 092c1c87…332c54  SKILL.md
> 0cadca29…751577b  METHODOLOGY.md
> ```
>
> ## FACTUAL
> **[BLOCKER] C3 oracle is broken on the source by the very wrap-bug the change targets** —
> 1.5-criteria.md:32 / 2-plan.md:23 vs stage-8.md:68-69. C3's verification is
> `grep -c 'fails against the unguarded version' stage-8.md` requiring `==1`. In source the phrase
> is line-wrapped: :68 ends "…that it fails against the" and :69 begins "unguarded version;". A
> line-based grep returns **0** (confirmed, exit 1). So C3's own oracle is a fragile positive-string
> matcher defeated by a wrap — exactly the failure mode the change exists to outlaw. Its stated
> self-test (delete-phrase→0) is degenerate because the baseline already returns 0. Fix: C3 must
> normalize/flatten before grep per the rule being added, and its self-test re-specified against the
> wrap.
>
> **[BLOCKER] The plan's NEW H6 block does not contain the clause C3 and the spec promise to
> preserve** — 2-plan.md:66-83. Introduced as "every original word preserved" but opens with an
> ellipsis. Grepping the NEW block for `fails against`/`unguarded`/`guards a fix` returns nothing.
> A builder told to transcribe "every original word" has no rendered source for the elided sentence.
> Fix: reproduce the full H6 first sentence verbatim (no ellipsis).
>
> **[MINOR] C8 self-test description misstates its own grep behavior** — 1.5-criteria.md:76-77.
> `grep 'unreviewed check'` → only :65; `grep 'H6\.'` (escaped) → only :65. The two CH6 hits
> (:100, stage-6.md:16) appear ONLY with an unescaped dot wildcard. C8 conflates escaped/unescaped.
>
> **Verified-clean factual (earned):** plan OLD block matches stage-8.md:65-73 byte-for-byte incl.
> wraps (diff exit 0). ST1.5 IDs run a–e → new ST1.5f does not collide. Insertion anchor correct
> (:38 ends "force a fake number.", :39 blank, :40 ST1.5b — no paragraph split). H6 uniqueness holds
> (grep for `unreviewed check`/`An unreviewed` across non-changes/ *.md → only stage-8.md:65; SKILL
> + METHODOLOGY carry no restatement).
>
> ## LOGICAL
> **[MINOR] ST1.5f inserted out of ID sequence** (a, f, b, c, d, e). Re-letter or place after
> ST1.5e. No other logical flaw; the generalization is a genuine superset of the fix-guarding case.
>
> ## MISSED OPPORTUNITY
> **[MINOR]** The change teaches "normalize text first" but ships no canonical normalization recipe,
> so each criterion reinvents it — and C3/C8 skip it. A one-line recipe in H6 would make the rule
> operational and would have caught the C3 wrap bug at authoring time.
> **[NITPICK]** NEW H6 grows to one dense paragraph; sub-bulleting would preserve C7 enumerability.
>
> ## ASSUMPTIONS / RISKS (incl. POSITION lens)
> **[MAJOR] H6's internal referential adjacency is unobserved.** The edit inserts two long bold
> spans BETWEEN H6's first sentence and its "**A defective check found this way**…" sentence
> (stage-8.md:69). "this way" is an anaphor: pre-edit it refers to the targeted-cold-check just
> described; post-edit two long spans sit between the referent and "this way", so a reader could
> rebind "a defective check found this way" to the newly-inserted self-test/absence material. This
> is the CP6 trap ("adding one can rebind a neighbor") occurring inside the very rule being edited.
> C7 checks neighbor rules are enumerable, not that H6's internal anaphora survived. Fix: keep the
> two spans at the END of H6 (after "…invalidated."), or add a criterion asserting "A defective
> check found this way" still binds to the targeted cold check.
> **[MINOR]** Re-wrapping prose can (re-)split C3's target phrase across a newline; no criterion
> checks the built file's target phrases are wrap-safe. (See CH8.)
>
> ## FIDELITY
> Rule TEXT is faithful to owner intent (generalize-to-all-oracles, self-test, positive-over-absence,
> normalize — all present in the NEW H6 span + ST1.5f). But the CRITERIA that verify it are NOT
> dogfooded to the same standard: C3/C8 are un-normalized single-string greps (the fragile matchers
> the rule warns against), and C3's self-test is degenerate (baseline already returns 0 from the
> wrap, so it does not distinguish violating from conforming). 1.5-criteria.md:6 claims "every oracle
> below is a positive per-site assertion" while C3/C8 are single-string greps. UNTRUSTED until the
> oracles are brought up to the rule.
>
> ## COVERAGE CHALLENGE (CH8)
> - GAP 1 (blocker-adjacent): no criterion checks C3's target phrase is contiguous/wrap-safe in the
>   BUILT file. GAP 2 (major): no criterion observes H6's intra-rule referential integrity ("A
>   defective check found this way" still binds to the original targeted cold check). GAP 3 (minor):
>   ST1.5f note sync covered only transitively by C9's diff -r (adequate). Otherwise coverage
>   adequate (C1/C2/C4 content, C5/C6 no-collateral, C9 sync).
>
> ## LABEL AUDIT (CH9/CH10)
> All nine gating; none advisory-as-dodge. C3's verification does NOT faithfully exercise the path
> it governs (FLAG, ties to the C3 blocker). C7 exercises enumerability but not intra-rule anaphora
> (partial, CH8 GAP 2). C8 path exercised but self-test wording mis-specified (MINOR). C1/C2/C4
> rubric-read clean; C5/C6 diff clean; C9 diff -r clean.
>
> ## OVERALL VERDICT: BLOCKER
> Two blockers (C3 wrap-broken oracle + degenerate self-test; ellipsis hiding the preserved clause),
> one MAJOR (H6 "this way" anaphora rebinding). Route: back to plan (fix NEW-block presentation +
> C3/C8 oracles to normalize) and to criteria (add wrap-safe + anaphora coverage). The rule TEXT
> itself is sound and faithful to owner intent — the defects are in the verification apparatus and
> the plan's presentation, not the design.

*(sha256 abbreviations expanded in the provenance block above; the reviewer reported full digests
matching the author's spawn-time snapshot. Reviewer could not address the parent by name/ID and
returned the record as its task deliverable — captured here verbatim.)*

---
## Author adjudication (consumer duty CH6 — every finding independently reproduced)

Reproduction commands + outputs are in the decisions.md gate-4 entry. All findings **accepted**
(none contested). Mapping to the author's original finding IDs where they differ:

- **BLOCKER — ellipsis hides preserved clause** (= my F1). Real. Route: back to plan → rewrite
  Edit A's NEW block as the FULL H6 paragraph verbatim, no ellipsis; build edits the real file in
  place. **Resolved in the revision.**
- **BLOCKER — C3 oracle wrap-broken + degenerate self-test** (the reviewer ranked this BLOCKER;
  I had it MAJOR — I **defer to the reviewer's higher severity** per SEV3). `grep -c 'fails
  against the unguarded version' stage-8.md` → 0 on source (wrap L68→69). Route: back to criteria
  → redesign C3 to a wrap-robust **positive assertion** (flatten newlines, then assert present) +
  a real self-test (fire on a version with the clause deleted, not on the wrapped baseline).
  **Resolved.**
- **MAJOR — H6 "this way" anaphora rebinding (position lens, intra-rule).** Real and important:
  inserting the two long spans BETWEEN H6's first sentence and "A defective check found this
  way…" puts a large distance between the anaphor and its referent (the targeted cold check),
  risking a rebind to the newly-inserted material. **Design fix:** move both additive spans to the
  **END of H6** (after "…invalidated."), so H6's original two sentences stay adjacent and "this
  way" keeps its referent; the new material is a pure append. This is strictly better and keeps the
  edit cleanly additive. Add a criterion (**C10**) asserting H6's original sentence order/adjacency
  is preserved. **Resolved by redesign, not just a note.**
- **MINOR — C8 self-test wording conflates escaped/unescaped dot** (= my L1). Fix C8 to state the
  exact pattern (`grep -rn 'unreviewed check'` → only stage-8.md:65) and drop the muddled "two CH6
  hits" claim. **Fixed in-place.**
- **MINOR — ST1.5f out of ID sequence** (= my M1). Kept ST1.5f (semantic placement after ST1.5a
  is correct, per the reviewer) with a one-line note that IDs are labels not a sequence; the
  alternative (renumber) adds churn for no behavioral gain. **Resolved with a note.**
- **MINOR/MISSED-OPP — no canonical normalization recipe in H6.** Adopted: the NEW H6 span now
  carries a short parenthetical recipe (`flatten newlines, strip **…** markers`) so the rule is
  operational, not just aspirational. **Adopted.**
- **NITPICK — dense H6 paragraph.** Not adopted as a structural change (sub-bulleting H6 would be a
  larger rewrite than the additive charter — deferred); the move-to-end fix already improves
  readability by keeping the original two sentences contiguous. Logged.
- **Coverage GAP 1 (built phrase wrap-safe):** closed by the C3 redesign (positive assertion runs
  on the flattened built file) + C10. **Coverage GAP 2 (anaphora):** closed by C10.

**Fidelity finding accepted in full:** the rule TEXT was faithful, but the *criteria's own oracles*
were not dogfooded to the rule. The revision brings C3 (and the C8 wording) up to the rule —
positive assertion + normalization + a real fire-on-violation self-test — which is the whole point
of this change. Iteration cap: gate 4, bounce 1/2.

**Worst severity = BLOCKER → route back to {plan, criteria}; no criteria frozen. Re-run stage-3
round 2** focused on: the full-verbatim Edit A, the C3 redesign robustness, C10 (anaphora), and
that the move-to-end does not itself displace a neighbor.

---

# Round 2 — re-review of revised plan/criteria (verbatim record)
- **Reviewer:** cold general-purpose subagent (agentId a3c0d8f268d2136fb), Opus 4.8. Reported sha256
  of all 9 context files; base stage-8.md d737f1bc… matches round-1.
- **Verdict: CLEAN (proceed)** — worst finding NITPICK.
- Round-1 findings independently verified CLOSED: BLOCKER(ellipsis) — full verbatim H6, original
  portion byte-identical to source; BLOCKER(C3 wrap-broken oracle) — raw grep=0 confirmed the bug,
  redesigned flatten-then-assert=1 on built + self-test=0 on deleted-clause (non-degenerate, fires);
  MAJOR(anaphora) — spans are a pure trailing append, C10 guards `verified = no`. A defective check
  found this way` adjacency (=1 built, =0 on reorder); MINOR(C8) exact-scoped single hit; MINOR
  (ST1.5f id) kept w/ note; missed-opp(normalization recipe) adopted.
- Fidelity check (built into this reviewer's charter): loaded terms pinned — "shown able to fail" →
  oracle returns non-pass on known-violating input (dogfooded on C3/C10); "positive over absence" →
  grep -c ==1 asserts, not absence sweeps; "normalize first" → tr flatten + **-strip. Clean/earned.
- **NITPICK:** C10's verification command uses a backtick inside single-quoted BRE relying on lenient
  undefined-escape handling (works on local grep; returns claimed 1/0). Optional: quote as a fixed
  string. Does NOT affect shipped skill text — it is a harness-command portability nit only.

## Gate 4 (round 2) — worst = CLEAN → route to BUILD; criteria FROZEN (C1–C10)
- Iteration cap: 1 blocker/major-class bounce at gate 4 (1/2). Round-2 clean.
