# Stage 4 — Spec

The builder spec is written FROM the approved sheet. Rules:

- **Traceability.** Every normative statement in the spec cites the sheet line it derives from (`[S12]`)
  or is marked `[DERIVED from S12]`. A statement with no citation is a fork (stage 2), not a spec line.
- **Current design only.** No strikethroughs, no "SUPERSEDES", no "corrected on <date>", no history. A
  builder must be able to read the spec top to bottom and find one consistent design. History lives in the
  ledger changelog. If the design changed, rewrite the section.
- **Plain mechanism names.** Constants are called constants and given their value and what they are
  pinned to; stores are named with their file, table and key; fallbacks say what triggers them and what
  runs instead. Adjectives ("trustworthy", "principled", "clean") carry no information and are removed.
- **Both sides of every direction.** "X is primary" is always accompanied by "Y runs only when
  <condition>" and by the behaviour when X returns nothing.
- **Underspecification is a defect.** "Runs on both paths" must say how each path behaves. Every
  branch that a builder could implement two ways is either specified or listed as an OPEN fork.
- **The invariants table** is copied from the sheet into the spec with the spec section that satisfies
  each row.
- **Acceptance criteria** name a measurable check per sheet line that can be checked; a criterion a
  build cannot check pre-ship is labelled as such (guarded-change will refuse to defer it silently).
- **Length.** Short beats complete-looking. A spec the builder cannot hold in one read produces questions
  by message, which is the failure this discipline exists to prevent. Move background, research and
  rationale to a linked appendix.

The spec file's basename ends in `-spec.md` or `-brief.md` so the read-gate hook covers it.
