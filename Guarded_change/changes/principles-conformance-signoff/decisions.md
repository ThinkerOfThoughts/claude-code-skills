# decisions.md: principles-conformance-signoff (append-only gate log)

Self-check run: subject = the guarded-change skill. No prior-version baseline; stage 8 is conformance-only.
Path validation (run start): every skill source path in 1-spec.md exists and is readable in the worktree; the oracle
inputs for C5 (original b04 `1-spec.md` and `2-plan.md`, the principles sheet, which is a symlink to its v3 file) exist.
Owner ruling source: the 2026-11-03 1:09 PM ruling and criteria C1-C5 reach this run only through the orchestrator's brief
(a durable transcript line the runner cannot cite). Flagged for the human in the report.

## Gate 4, bounce 1 (round 1 review, 3-redteam-plan-round1.md)
- Worst severity: major (5 majors, no blocker). Route: back to plan (stage 2), edit in place, then re-review.
- Dispositions, all accepted unless noted:
  1. Behaviour preservation: C4 gains an executed check inside the C5 record (five lenses, coverage challenge, label audit,
     fidelity pins still present).
  2. C5: kept as the requester specified (facts file, plan-review replay, one run); the record is also asserted for PRC section
     shape. The limits (no stage-6 run, no negative control, no discovery without the facts file) are stated in the plan and
     go in the report as not checked. Not widened: the requester set the replay scope and a micro-harness is ruled out.
  3. Closed set gains the owner entries of `decisions.md`; stage 6 also receives `1-spec.md`.
  4. Over-fire: kept at-least-MAJOR (it is the requester's criterion C1 and "sharpen, never weaken"); added the "same job"
     carve-out, the "entry judged as worded including its own exceptions" rule, and the reason the floor is MAJOR.
  5. Proof homes: commands, expected output and a known-bad self-test written into the plan's Measurement section.
  6-14. Search scope widened to the modules beside and imported by touched files; bullet moved into the unconditional block
     (before Provenance); intro lists and SKILL.md rows added to the edit list; `principles_context` shape fixed (path + note,
     priority-ordered) and declared authoritative; all entry kinds covered; circular clause dropped; section-missing handled
     "as CH13/ST6e handle a missing lens"; the shared module that lacks the operation is covered by "belongs in that module"
     (this is what catches the bare unlink); installed-copy sync added as plan step 10; "answer" scoped out in the spec.
  15. Pre-existing stale charter header sentence: out of scope, listed in the report.
- Iteration cap: bounce 1 of 2 at gate 4.

## Gate 4, bounce 2 (round 2 re-review of plan revision 2; record not kept verbatim, findings below are the reviewer's)
- Worst severity: major (M1-M5, no blocker). Route: back to plan; revision 3 written. The runner went to build on revision 3
  without a third plan review: the per-class cap is reached for the unlink class (round 1 #12, round 2 M1), the stage-6
  review reads the actual built text against this plan, and the C5 replay executes the governed path.
- M1 (bare unlink not reliably caught): fixed. Third violation (c): an operation done outside the shared module that already
  holds the neighbouring operations, because it lacks it, is extended not bypassed; "simple new mechanism" entries apply only
  where no such module exists. C5 report states reader and unlink separately; pass condition stays the requester's "and/or".
- M2 (exception writable by the author): fixed. An exception needs the RAT1 ratification record at both stages.
- M3 (known-bad missing): fixed. Every check in the plan's Measurement has a known-bad; C5 has a control arm on the old text.
- M4 (stage-6 half of C1/C2 unverified): NOT fixed by the runner. No code or diff of the failed run is available (only the
  review prose); building one by hand would be a constructed oracle. Returned to the human in the report as a named
  risk-acceptance request. Nothing is pushed.
- M5 (unratified inflation: "however the sources word their entries", MAJOR floor): NOT fixed; the text is the requester's
  criteria C1/C2. Returned to the human in the report for confirmation.
- Minors m1-m10 applied in revision 3 (executed preservation rubric, HIST section, stage-6 input-set sites, exact commands
  from the repository root, placeholders resolved, post-6 and arm applicability, section required in every record, n.a.
  spot-check and grouping, pointer-only SKILL/METHODOLOGY text). m11 ("answer" dropped) returned to the human.
- Iteration cap: bounce 2 of 2 at gate 4.

## Gate 7, bounce 1 (stage-6 review, round 1; the review output is not kept verbatim, findings below are the reviewer's)
- Worst severity: major (F3, F9). Route: back to build, edit in place, then a short re-check.
- F3 (rulings outside the principles sources had no verdict format): fixed. Charter PRC (i) now gives every owner ruling in the
  spec and in the owner entries of `decisions.md` a verdict line.
- F9 (companion path to the shared JSON module is dead in the shared checkout): fixed. No `redteam_context` path was added for a
  file that does not exist there; the module is named in a "Shared mechanisms" note, "present on branches where it has
  landed". Open for the human: the module lives only on dev branches/worktrees of the project, as the reviewer found.
- F2 (note claimed delete goes through the module): fixed, the note says the module has no delete function.
- F1 (plan commands): fixed in the plan (stage-2 dropped from the key check; line-folded grep for the wrapped phrase; the bare
  word `zero` dropped from the name pattern). F4: part of M5 (returned to the human). F5: CH14/ST6g named in both Procedure
  steps; stage 6 points at the charter's closed set. F6: METHODOLOGY bullet cut to a pointer. F7: README line updated.
  F8: Provenance sentence states the harness-arm exemption. Nitpick: charter intro says "when the config names them".

## Gate 7, bounce 1 re-check (targeted stage-6 check of the delta)
- Worst severity: minor (wrapped-phrase command, stale plan steps 8/9). Route: fix and proceed. Fixed in the plan.
- Gate 8: all six criteria verified (8-harness.md). Unresolved items returned to the human: M4 (stage 6 and the delete half of C2
  not exercised), M5 (unratified inflation: "however the sources word their entries", the at-least-MAJOR floor, exception
  wording), "answer" scoped out, ratification source of the owner ruling and criteria (reached the run only via the brief),
  the shared JSON module exists only on dev branches of the project (companion note, no path entry).
