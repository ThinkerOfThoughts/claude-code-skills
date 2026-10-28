# Stage 5 — Build

**What this stage does:** implement the change per the plan.

## Procedure

Implement per the plan, including any instrumentation the plan added.

## Rules governing this stage

**Build per the plan (BLD).** Implement per the plan, including any instrumentation the plan
added.

**A test written to drive the build is scaffolding (SCAF).** Writing a test before the code is
allowed and is often the quickest way to build, but the loop does not require it and such a test is
not a deliverable. At the end of stage 5, before stage 6, each of these tests is kept only if it is
the proof of a behavior criterion (PH, `stages/stage-1.5.md`); one that overlaps a behavior test
has its assertions folded into that test and is deleted; one that only restates a documentation or
removal criterion may be deleted, and that criterion is then verified in its proof home at stage 8.
Never delete the only execution of a behavior criterion. Doing this before stage 6 keeps the
reviewed diff equal to the shipped diff.
