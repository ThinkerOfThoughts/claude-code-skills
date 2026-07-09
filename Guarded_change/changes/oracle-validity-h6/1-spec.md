# 1 — Spec: oracle validity (generalize H6 + positive-assertion preference)

## Problem

The guarded-change skill already carries **H6** in `stages/stage-8.md` ("An unreviewed check is
not a check"): a new or modified executable check whose results stage 8 will trust gets a
**targeted cold check before its results count** — "for representativeness, and, where the check
guards a fix, that it **fails against the unguarded version**; until then its results are
`verified = no`."

H6 leaves two gaps, both of which hit a real run on 2026-07-09 (the `charter-fidelity-lens`
self-check, commit `6171c2d`):

1. **The "must be shown able to fail" duty is scoped too narrowly.** H6's fail-against-unguarded
   clause reads as applying only to a check that *guards a fix*. But a **conformance oracle** that
   guards no fix at all — a plain `grep`/`diff` asserting a document invariant — is just as capable
   of being a broken oracle that silently passes. In the fidelity-lens run, criterion C5's oracle
   was a `grep` meant to prove "no stale `four…lens` count word remains." It guarded no behavioral
   fix, so H6's clause did not obviously bite, and the grep was accepted without a self-test. It
   was **blind to 2 of its 7 target sites**: `charter.md:16` had `four **separate** lenses` (the
   `**` markdown emphasis exceeded the grep's span) and `SKILL.md` wrapped `four`\n`lenses` across a
   line-break (a line-based grep cannot span it). The oracle returned "0 stale → PASS" while two
   violations remained. Had the round-1 red-team not caught it, a broken oracle would have
   certified "done."

2. **Absence checks fail silently; positive assertions do not.** An **absence check** ("prove the
   bad token is gone") returns wrongly-true the moment its matcher is fragile — markdown emphasis,
   line-wraps, encoding all make "absent" trivially true when the token is in fact present. A
   **positive post-state assertion** ("prove the desired value is present at each expected site")
   cannot be defeated the same way: a missed edit shows up as a *missing expected value*, which a
   fragile matcher surfaces rather than hides. The fidelity-lens run's fix was exactly this — C5
   was redesigned to a positive-per-location assertion **plus** a flatten/strip-normalized negative
   sweep **plus** a fire-on-baseline self-test. That working pattern should be doctrine, not a
   lesson re-learned each run.

## What to change (additive; keep existing rule text intact)

- **Generalize H6** (`stages/stage-8.md`) so the "must be shown able to fail before its pass is
  trusted" duty covers **every conformance/oracle check whose result stage 8 will trust**, not only
  a check that guards a behavioral fix. The general form: any such oracle (including a cheap
  grep/diff) must be **demonstrated to fire on a known-violating input** — a self-test, e.g. run it
  against the pre-change / known-bad tree and confirm it flags the violation — before a "pass" from
  it is trusted; until then its result is `verified = no`. An oracle that cannot be shown to fail is
  an un-run check. The existing fail-against-unguarded clause for fix-guarding checks is a
  *special case* of this and stays intact.

- **Add the positive-assertion-over-absence preference** to H6: prefer a **positive per-site
  assertion** (desired value present at each expected site) over a bare **absence sweep** (bad token
  gone), because a fragile matcher makes "absent" wrongly true and silent; where an absence sweep is
  used, **pair it with the positive assertion AND normalize the text first** (strip markup, flatten
  wraps) so formatting cannot defeat the sweep.

- **Add a one-line note at `stages/stage-1.5.md`** where a criterion states its verification method:
  a criterion's oracle must be shown able to fail (a self-test that it fires on a known-violating
  input) before a "pass" counts, and prefer a positive per-site assertion over a bare absence check.
  This is the criteria-authoring-time reminder; H6 is the stage-8 enforcement.

## Non-goals

- No change to the five lenses, the severity model, the gate routing, or any other H-rule.
- No new rule ID beyond generalizing H6 in place (H6 keeps its ID; the stage-1.5 note references it).
- No behavioral change to the loop's structure — this sharpens an existing check-validity rule.

## Expected touched files

- `stages/stage-8.md` — generalize/extend **H6** (the two additive points above).
- `stages/stage-1.5.md` — one-line verification-method note.
- Installed mirror `~/.claude/skills/guarded-change/{stages/stage-8.md,stages/stage-1.5.md}` — kept
  byte-identical to source (synced post-build; verified by `diff -r`).

No other skill file is touched. The lens count, the charter, SKILL.md, and METHODOLOGY.md are **not**
edited (H6 is stated in exactly one place — `stage-8.md` — so there is no cross-doc count to update;
this is confirmed as a stage-1.5 criterion).
