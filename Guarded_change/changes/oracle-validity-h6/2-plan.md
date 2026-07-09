# 2 — Plan (how + measurement + verbatim proposed text)

## Approach

Two additive edits, both in-place, no rule deleted/reworded:

1. **`stages/stage-8.md` — extend H6.** Keep the existing H6 paragraph verbatim and insert two new
   sentences that (a) generalize the "shown able to fail" duty to *every* conformance oracle and (b)
   state the positive-assertion-over-absence preference. The existing "fails against the unguarded
   version" clause stays intact, reframed as a special case.
2. **`stages/stage-1.5.md` — add a one-line verification-method note** where a criterion states how
   it is checked (right after the two-means rule ST1.5a), pointing at H6 for enforcement.

## Measurement (how the criteria are verified) + instrumentation

Prompt-doc change, no runtime baseline → stage 8 is **conformance-only**. Instrumentation = `git
diff` / `git show HEAD:` / `grep` / `diff -r`, all already available. Per-criterion:

| Criterion | Oracle | Positive/absence | Self-test (shown able to fail) |
|---|---|---|---|
| C1 | operator reads built H6 for the generalization + self-test language | positive | n/a (rubric) |
| C2 | operator reads built H6 for the three preference elements | positive | n/a (rubric) |
| C3 (redesigned) | **flatten** stage-8.md (`tr '\n' ' '`), then assert the clause `fails against the unguarded version` present exactly once | positive, **wrap-robust** | delete-clause scratch copy → flattened grep returns 0 (fires) |
| C4 | operator reads built stage-1.5 note for its three parts | positive | n/a (rubric) |
| C5 | enumerate every `git diff` hunk; each within an allowed region | positive (per-hunk) | n/a (diff is ground truth) |
| C6 | `git status --short` / `git diff --stat` = the two files only | positive | n/a |
| C7 | stage-6 cold reviewer enumerates unchanged neighbors + new H6 | execution (reviewer) | n/a |
| C8 (reworded) | `grep -rn 'unreviewed check'` over non-changes/ *.md → only stage-8.md:65 | positive | n/a (exact-pattern, single hit) |
| C9 | `diff -r` source vs installed empty | positive | n/a |
| C10 (new) | flatten stage-8.md; assert H6's `verified = no\`. A defective check found this way` adjacency survives (referent immediately precedes "this way") | positive, wrap-robust | scramble-order scratch → adjacency grep returns 0 (fires) |

Gating vs advisory: all gating. No regression arm (no baseline).

## Thresholds (severity → route)

Standard SEV1 table. Blocker → back to spec/criteria; major → back to plan; minor → fix-and-proceed;
nitpick → log. Iteration cap 2 bounces/finding-class.

---

## VERBATIM proposed text

### Edit A — `stages/stage-8.md`, H6 (lines 65–73)

**OLD (exact current text):**

```
**An unreviewed check is not a check — H6.** Any new or modified executable check whose results
stage 8 will trust, created after the stage-6 review (the harness itself, a route-(a)
representative fixture, a rebuilt probe), gets a **targeted cold check before its results
count** — for representativeness, and, where the check guards a fix, that it fails against the
unguarded version; until then its results are `verified = no`. A defective check found this way
is discarded and rebuilt in place (logged in `decisions.md`), not a loop restart; findings it
raises about the change itself route via the gate-8 severity row. In-place fix diffs at gates
7/8 are recorded in `decisions.md`, and a stage-8 fix-in-place re-runs the criterion checks its
diff could have invalidated.
```

Note: the OLD block above is the true byte-for-byte source (its line-wraps preserved — `results\ncount** —` and `unguarded\nversion`). The build inserts two additive spans between the existing
first sentence (ending `until then its results are `verified = no`.`) and the existing "A defective
check…" sentence, leaving both sentences intact.

**NEW (FULL verbatim replacement paragraph — no ellipsis; per round-1 the entire new H6 is written
out so the build has an unambiguous source. Per round-1 MAJOR (anaphora): the two additive spans
are APPENDED AT THE END of H6, after `…invalidated.`, so H6's original two sentences — the
targeted-cold-check sentence and the `A defective check found this way…` sentence — stay adjacent
and "this way" keeps its referent. Every original word is preserved unchanged and in its original
order; the only new bytes are the two trailing **bold** additive spans (the second now carries a
short normalization recipe per the missed-opp finding). The build edits the real file in place;
prose lines will wrap to the file's ~95-col style but no word changes):**

```
**An unreviewed check is not a check — H6.** Any new or modified executable check whose results
stage 8 will trust, created after the stage-6 review (the harness itself, a route-(a)
representative fixture, a rebuilt probe), gets a **targeted cold check before its results
count** — for representativeness, and, where the check guards a fix, that it fails against the
unguarded version; until then its results are `verified = no`. A defective check found this way
is discarded and rebuilt in place (logged in `decisions.md`), not a loop restart; findings it
raises about the change itself route via the gate-8 severity row. In-place fix diffs at gates
7/8 are recorded in `decisions.md`, and a stage-8 fix-in-place re-runs the criterion checks its
diff could have invalidated. **This "must be shown able to fail" duty is not limited to checks
that guard a fix — it binds *every* conformance/oracle check whose result stage 8 trusts,
including a cheap `grep`/`diff` asserting a document invariant: before a "pass" from it counts,
the oracle must be demonstrated to fire on a known-violating input (a self-test — e.g. run it
against the pre-change / known-bad tree and confirm it flags the violation).** An oracle that
cannot be shown to fail is an un-run check (`verified = no`). **Prefer a positive per-site
assertion (the desired value is present at each expected site) over a bare absence sweep (the bad
token is gone): a fragile matcher — markdown emphasis, a line-wrap, an encoding quirk — makes
"absent" silently, wrongly true, hiding a missed edit, whereas a positive assertion surfaces the
same miss as a missing expected value the matcher cannot hide. Where an absence sweep is used,
pair it with the positive assertion AND normalize the text first (flatten newlines, strip `**…**`
markers) so formatting cannot defeat the sweep.**
```

Note (round-1 resolutions):
- **BLOCKER (ellipsis) resolved** — the full paragraph is written out verbatim; the existing
  `fails against the unguarded version` clause (source wraps it `the`\n`unguarded version`) is
  preserved intact.
- **MAJOR (anaphora) resolved** — the two additive spans are now a pure trailing append; H6's
  original sentence order is byte-unchanged, so `A defective check found this way` sits immediately
  after its referent exactly as before. The change is now an **append to H6**, not an insertion.
- **Missed-opp resolved** — the second span's normalization clause names the concrete recipe
  (flatten newlines, strip `**…**` markers).
- Build = in-place edit of the real file (preserving the wrapped `the`/`unguarded version` line
  break in the original sentences), not a reconstruction from an abbreviation.

### Edit B — `stages/stage-1.5.md`, verification-method note

Insert a new rule paragraph immediately AFTER the ST1.5a rule (which ends `…the loop must not
force a fake number.` at line 38) and BEFORE the ST1.5b rule (`**Criteria are mandatory
(ST1.5b).**` at line 40). The existing blank line 39 separates them.

**NEW paragraph to insert (between current line 38's paragraph and current line 40's ST1.5b):**

```
**An oracle must be shown able to fail; prefer positive assertion over absence (ST1.5f).** When a
criterion states *how* it is verified, its oracle must itself be a check that can be **shown able
to fail** — demonstrated to fire on a known-violating input (a self-test, e.g. run it against the
pre-change / known-bad state and confirm it flags the violation) before a "pass" from it counts;
until then that criterion's result is `verified = no`. Prefer a **positive per-site assertion**
(the desired value is present at each expected site) over a bare **absence check** (the bad token
is gone), because a fragile matcher makes "absent" silently, wrongly true; where an absence sweep
is unavoidable, pair it with the positive assertion and normalize the text first (strip markup,
flatten wraps). This is enforced at stage 8 by H6 (`stages/stage-8.md`).
```

Placement rationale: ST1.5a is where a criterion's checkability/verification-means is defined, so
the oracle-validity note belongs immediately after it; giving it a rule ID (ST1.5f) matches the
sibling rules' convention and does not collide (existing IDs run ST1.5a–e). It references H6, the
stage-8 enforcement, mirroring how CP6/CP7 in this file point to their charter/stage-8 forms.

## Sync + commit

After build: copy both edited files to the installed mirror, `diff -r` to confirm empty, run the
stage-8 harness, then commit to skills-repo `main` (established workflow; human-authorized this
session). Message imperative; reference `changes/oracle-validity-h6/`; Co-Authored-By trailer.
