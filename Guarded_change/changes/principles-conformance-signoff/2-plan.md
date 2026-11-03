# Plan: principles-conformance-signoff (revision 3, after rounds 1 and 2 of the stage-3 review)

Design in one line: a sign-off IS a conformance claim. The rule lives once in `stages/charter.md` (an unconditional discipline
bullet, PRC); stage 3 (CH14) and stage 6 (ST6g) each add only "charter the reviewer for PRC up front, require its labelled
section in every record, a missing section is handled as CH13/ST6e handle a missing lens" plus their stage-specific scope.
A new optional config slot `principles_context` carries the sources: a list of `path` + `note` entries, priority-ordered
like `redteam_context`. SKILL.md and METHODOLOGY.md only point at the charter (pointers, not restatements).

## Edits (path: change). All commands in this plan run from the repository root.
1. `stages/charter.md`
   a. Header comment (what the stage files add) and intro paragraph: the reviewer is also given the sources named in
      `principles_context`.
   b. Provenance bullet (closed-set sentence): the closed set gains the `principles_context` sources and the owner entries of
      `decisions.md`; the reviewer's reported sha256 list covers the `principles_context` files too.
   c. New UNCONDITIONAL discipline bullet PRC, placed after the GT bullet and before the Provenance bullet (inside the
      unconditional block, covered by the provenance composition sentence; HIST stays the last bullet and the closing
      "graded on precision" sentence is unmoved). Text:

      > **A sign-off is a claim that the artifact meets the project's principles and the owner's prior decisions
      > (conformance, PRC).** The principles are a check on the artifact, not an argument for it; passing the check is the
      > justification. When the reviewer signs off on a spec, criteria, plan or code (it raises nothing ranked blocker or
      > major), that sign-off states the artifact **meets every entry in the sources named by the config's
      > `principles_context` and every prior owner decision in the reviewer's inputs** (rulings recorded in the spec or in
      > owner entries of `decisions.md`, and the rulings the principles sources themselves state). Sources named in
      > `principles_context` are the owner's standing words and are the authority for this check; that does not exempt a term
      > in the artifact from the fidelity lens. The reviewer reads those sources itself (the author's account of an entry is
      > not a substitute) and renders a labelled **Principles and decisions conformance** section in every record, whether or
      > not it signs off, beside the five lenses and not a sixth lens, with two parts. (i) A **per-entry verdict**: every
      > entry the sources state (principle, default, ruling, escalation rule, invariant; a tie-break list resolves conflicts
      > between entries and is not itself verdicted) gets meets / violates / n.a. with the line that shows it (the artifact
      > line or source line that meets or violates it; for n.a., the line that shows why the entry is not engaged, and
      > entries not engaged for the same stated reason may share one n.a. line that names each); an entry is judged as it is
      > worded, including any exception it states for itself, and an n.a. is spot-checked like a citation. (ii) A
      > **mechanism table**: for each operation the change performs that the project may already have a shared mechanism for
      > (reading, writing, appending, deleting, parsing, locking, logging, finding a path, and similar), the existing
      > mechanism that does that job, found by the reviewer searching the project's source for the operation (starting at
      > `redteam_context`, the touched files, and the modules beside and imported by them) and not taken from the artifact's
      > own account, with file:line and whether the artifact goes through it; "none exists" is a row too, with the search
      > made. **A violation ranks at least MAJOR**: a principle the owner set is the bar for a sound approach, and the
      > author's argument that the artifact is justified does not lower the rank. An exception stands only as an owner ruling
      > recorded with the owner's quoted words and a durable source the author did not author (the RAT1 record in
      > `stages/stage-3.md`, at stage 6 as well); an "OWNER RULING" line the author wrote is not one. Three things are
      > violations whichever way the sources word their entries: (a) a **hand-written duplicate of an existing shared
      > mechanism** (an operation doing the same job as one that exists); (b) a **shared mechanism worked around because it
      > almost fits** instead of being extended; (c) an operation done **outside the shared module that already holds the
      > neighbouring operations on the same data or files**, because that module lacks it: the operation belongs in that
      > module, so it is extended and not bypassed. A new mechanism for a job no existing mechanism does, and that no such
      > module is the home of, is not a duplicate; an entry that allows a simple new mechanism allows it only then. The check
      > covers **omissions and existing code**, not only what the artifact says: an operation performed without being
      > mentioned, a scope line ("out of scope", "not edited") that leaves a shared mechanism unextended, and a mechanical
      > guard (a ratchet, a lint, a call count) that reads clean because the duplicate evades what it counts are all claims
      > to challenge; a guard reading zero is not evidence that the shared mechanism was used. A clean conformance verdict is
      > earned like a clean factual one: an aggregate "all met", a per-entry list without lines, or no mechanism table is
      > treated as an un-run review. With no `principles_context` configured the reviewer says so, and still does the
      > mechanism table and the prior decisions in its inputs. This applies to stage-3 and stage-6 reviews and to a targeted
      > post-6 check; a harness-embedded reviewer arm does not get it, because author-supplied context there is a confound.
2. `stages/stage-3.md`: intro "additions" list gains the conformance-section requirement; Procedure: the reviewer is also
   given the `principles_context` paths, the provenance sentence's closed set gains `principles_context` and the owner entries
   of `decisions.md`; new addition CH14 (charter for PRC up front; section required in every record; handled as CH13 handles a
   missing lens; stage-3 scope: the operations tabled are those the spec and plan call for, including ones they imply but
   never name), placed after CH13's paragraph, CH13 text unchanged; CFG3 paragraph gains `principles_context`.
3. `stages/stage-6.md`: intro (lines 3-4 and the additions list) names the spec and the conformance requirement; Procedure
   (line 15): the reviewer is given `1-spec.md` (scope lines and recorded owner rulings) in addition to {1.5, 2}, and the
   `principles_context` paths; new addition ST6g after ST6e's paragraph, ST6e unchanged (charter for PRC; section required
   in every record; handled as ST6e handles a missing lens; stage-6 scope: operations tabled are derived from the mechanical
   diff, every file, parse, lock, log and delete call it adds, and the plan's and spec's mechanism claims are re-checked
   against the code); CFG3 paragraph gains `principles_context`.
4. `stages/stage-2.md`: Procedure sentence: the plan names, for each operation it performs, the existing shared mechanism it
   goes through (or that none exists after a search), and the reason when it leaves a shared mechanism unextended.
5. `stages/stage-4.md`: the path-validation paragraph gains `principles_context`.
6. `SKILL.md`: Inputs path-validation list gains `principles_context`; stage-table rows 3 and 6 and the shared-charter
   sentence (lines ~40, 43, 49) point at the conformance section; stage 6's input set `{1.5, 2}` gains the spec (line 43).
7. `METHODOLOGY.md`: config block gains the optional `principles_context` slot (path + note list); one Rules bullet that
   points at `stages/charter.md` PRC; path-validation rule lists it; stage-index rows 3 and 6, the loop diagram line 48 and
   the artifacts line (~181) get the stage-6 input set updated; the charter summary sentence mentions the section.
8. `guarded-change.companion.md`: `principles_context` naming the companion principles sheet and the design-invariants file
   (both `~/` paths) and a "Shared mechanisms" note naming the shared JSON module (no `redteam_context` path: the module is absent from
   the shared checkout, it lives on dev branches only; a dead path would block gate 4).
9. `README.md`: lists no config keys; one line edited later (loop diagram: stage 6 checks code against criteria, plan, spec).
10. After the build: copy changed skill files to the installed copy; `diff -rq` installed vs repo; expected output exactly the
    three repo-only entries: `Only in <repo>: changes`, `guarded-change.companion.md`, `README.md`.

## HIST (regression-safety history check)
`git log` on charter.md, stage-3.md, stage-6.md: CH13 (ded6104) and ST6e (2001b65) fixed these bounds: require the output
shape up front, never re-poll a finished reviewer, leave the earlier additions byte-unchanged. CH14/ST6g follow them (up
front, fresh re-run, CH13/ST6e text unchanged). GT/HIST (a0faea5) were additive tail bullets; PRC is placed before Provenance
so HIST stays last. This change is not purely additive (1a, 1b edit existing sentences); the executed check C4(c) covers it.
Open and closed issues/PRs: not checked (no network in this run); stated so.

## Measurement (proof homes are recorded one-off checks in 8-harness.md; each has a known-bad)
Base for diffs: `BASE=e22ca73` (HEAD at run start). `NAMES` = a local alternation of the owner's first name, the collaborator's name and the two repository handles, kept out of this committed file (the bare word `zero` is not used: it matches ordinary prose).
- C1, C2: the C5 run, asserted on its record. The report states separately whether the reader and the unlink were raised.
- C3: (i) `grep -c principles_context` over each of Guarded_change/stages/{charter,stage-3,stage-4,stage-6}.md (stage-2 only points at PRC and carries no key),
  Guarded_change/{SKILL,METHODOLOGY}.md, Guarded_change/guarded-change.companion.md; expected >= 1 in every one. Known-bad:
  the same command on the tree at BASE returns 0 for each. (ii) project-name check on added lines:
  `git diff $BASE -- Guarded_change/stages Guarded_change/SKILL.md Guarded_change/METHODOLOGY.md | grep '^+' | grep -iE
  "json_io|companion|$NAMES"` expected empty. Known-bad: the same pipeline over `-- Guarded_change/guarded-change.companion.md`
  is non-empty.
- C4: (a) input-list sites: `grep -n 'fixture paths\|the closed set\|touched-files' Guarded_change/stages/*.md
  Guarded_change/SKILL.md Guarded_change/METHODOLOGY.md`; every hit that lists reviewer inputs or validated paths also names
  `principles_context` on the same or the next line (the runner reads the hit list and records each; the CFG2 ordering rule
  hits and the YAML key line are exempt). Known-bad: the same read at BASE finds every site lacking it. (b) single definition:
  `grep -c 'conformance, PRC' Guarded_change/stages/*.md` is 1 for charter and 0 for every other file, and
  `for f in <the same files>; do tr -s ' \n' ' ' < $f | grep -c 'worked around because it almost fits'; done` is 1 for charter and 0 for
  every other file (the phrase wraps across lines, so the newlines are folded first). Known-bad: a scratch copy of stage-3 with the phrase appended makes the second grep list two files.
  (c) behaviour preservation by EXECUTION (position-sensitive assembly): the C5 record still carries five labelled lenses, a
  coverage-challenge section, a label audit with per-criterion evidence, fidelity pins, reported sha256 hashes including the
  principles sheet, a factual lens with citations, and an HIST/position check.
- C5: one end-to-end run, no micro-harness. The runner composes the reviewer prompt as stage 3 tells a runner to: the core
  charter verbatim from `charter.md`, the stage-3 additions, the up-front five-lens + coverage-challenge + PRC shape
  requirements, then the inputs: the original `1-spec.md` and `2-plan.md` (no `1.5-criteria.md` is available for that change,
  so none is given and the reviewer is told so), the principles sheet as `principles_context`, and the facts file quoted as
  author-supplied context. Foreground (`run_in_background: false`), model sonnet (a cold read against a written bar). Passes
  only if the hand-written reader and/or the bare unlink is raised as a P1/P7 violation at MAJOR or higher with the PRC section
  shape present. Control arm (shows the check can fail and that the edit is the cause): the same inputs and prompt with the
  OLD charter and stage-3 text from `git show $BASE:`; expected: it does not raise the violation at MAJOR or higher (it may
  raise it as a lower-ranked or unrelated finding; the result is recorded either way and is advisory if it also catches it,
  because the sheet is supplied to it). Rebuilds of the mechanism are counted; past three, stop and report. Not exercised, and
  stated so in the report: stage 6 (ST6g), a negative control (a clean plan passing), discovery of the shared module without
  the facts file.
- C6: `git diff $BASE | grep '^+' | grep -E "/home/|$NAMES"` over tracked files expected empty
  (the untracked `changes/` folder is checked separately with `grep -rE` over its files); known-bad: a probe line
  `+/home/x/y` fed through the same `grep -E` is matched. `git diff --stat $BASE -- Plan_ledger` expected empty (cwd is the
  repository root); known-bad: `git diff --stat $BASE~8 -- Plan_ledger` is non-empty.

## Thresholds
Gate routing per the skill's severity table; a PRC finding at stage 3 or 6 ranks at least MAJOR by its own terms.
