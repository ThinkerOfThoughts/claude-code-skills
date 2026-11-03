# Stage-6 red-team (record; CONDENSED by the runner)

Disclosure: the reviewer outputs were long; this record keeps the provenance facts and each ranked finding in substance. The
full text was in the runner's turn only.

- Reviewed diff: mechanical `git diff e22ca73 -- Guarded_change`, round 1 (347 lines), re-check on the delta between that diff
  and the final one (111 lines of plain `diff`).
- Charter given: `stages/charter.md` (round 1 sha256 f05919e31b0a37f3) and `stages/stage-6.md` (9f0beeb6dc25cbc3), read in full,
  with the up-front five-lens shape, the ST6f test section ("none found": the diff adds no tests) and the ST6g conformance
  section. Inputs: the diff, `1.5-criteria.md`, `2-plan.md` (revision 3), `1-spec.md`, `decisions.md`. This project names no
  `principles_context`; the reviewer said so and still produced the mechanism table (no duplicate mechanism introduced: the
  closed-set sentence, CFG3 lists, missing-section rule and RAT1 are each edited or reused in place).
- Reviewer: general-purpose subagent, model sonnet, foreground. Re-check: same type and model.

## Round 1 ranked findings
- major F3: owner rulings in the spec and `decisions.md` had no verdict format in PRC part (i). Fixed.
- major F9: companion config path to the shared JSON module does not exist in the shared checkout. Fixed (note, no path).
- minor F1 plan commands wrong (stage-2 key count, wrapped phrase, bare word in name pattern); F2 companion note claimed a
  delete function; F4 exception wording tension (part of M5, returned to the human); F5 CH14/ST6g not in the Procedure steps;
  F6 METHODOLOGY restated PRC; F7 README stale; F8 harness-arm exemption missing from the Provenance sentence. All fixed
  except F4.
- Position lens: PRC (the longest charter bullet) now precedes the three conditional bullets; HIST and the closing precision
  sentence are unmoved; a recency effect cannot be excluded by reading alone.

## Re-check
All eight fixes present and resolving. Findings: minor (the wrapped-phrase command still missed because of indentation: fixed
by squeezing whitespace; plan steps 8/9 stale: fixed), two nitpicks left as they are.
