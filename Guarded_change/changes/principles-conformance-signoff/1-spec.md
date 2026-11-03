# Spec: principles-conformance-signoff (self-check run; subject = the guarded-change skill)

## Problem
A builder running the loop on a project whose owner keeps a principles sheet hand-wrote a JSONL reader (and a bare
`unlink`) next to the project's shared JSON module. That violates two of the owner's principles: "One mechanism, one
source of truth ... never add a parallel path" (P1) and "Reuse an existing mechanism ... If two mechanisms do the same job,
remove the duplicate" (P7). Every cold review passed it:
- the spec declared the shared module "not edited" (`1-spec.md:59` of that run);
- the cold plan reviewer listed "add a reader to the shared module" as option 3 and recommended the bypass
  (`3-redteam-plan-round1.md:25-35`);
- the code reviewer accepted it because a call-count ratchet read zero (`6-redteam-code.md:42`);
- no reviewer was handed the principles sheet or asked whether the work meets it.

## Owner's ruling (verbatim, 2026-11-03 1:09 PM)
"That should be implied by signing off on a piece of code/plan/answer that it meets the principles/prior decisions."
Also (owner's design principles, quoted by the requester): "the principles are meant to check an answer, not to justify
it; passing those checks is the justification."

## Wanted
A cold reviewer's sign-off at a spec/criteria/plan review (stage 3) or code review (stage 6) means the artifact meets every
principle of the project's principles sheet and every prior owner decision in the reviewer's inputs. The check covers
omissions and existing code (what the artifact does not say; the shared mechanism an operation should have gone through).
The project config has a slot naming the principles sheet and prior-decision sources, which become reviewer inputs.

Scope note: the owner's phrase is "code/plan/answer". The loop's reviewed artifacts are spec, criteria, plan and code; a chat
answer is not an artifact of the loop and is out of scope here.

## Constraints
- The skill stays domain-agnostic (Layer 1): no project-specific text in charter or stage files. Project specifics go in the
  companion config (Layer 2).
- Common/role structure: the charter holds what every reviewer needs; stage files add only; no stage file restates a
  charter rule.
- Public repo: no personal details, no absolute home paths.

## Expected touched files
`Guarded_change/stages/charter.md`, `stages/stage-2.md`, `stages/stage-3.md`, `stages/stage-4.md`, `stages/stage-6.md`,
`SKILL.md`, `METHODOLOGY.md`, `guarded-change.companion.md`, and this folder `changes/principles-conformance-signoff/`.
(`README.md` checked for a config-shape listing; edited only if it has one.)

## Out of scope
`Plan_ledger/` (another runner). Stage 7/8 gate mechanics (the existing reviewer-severity-routes rule already routes on
the reviewer's ranking). Any change to the five-lens shape (CH13/ST6e): the new duty is a labelled section beside the
lenses, not a sixth lens.

## Runnable unit (RTS)
After the build, one cold reviewer is given the NEW charter and stage-3 file, the failed run's original `1-spec.md` and
`2-plan.md`, the principles sheet and a facts file about the shared module. It must raise the hand-written reader and/or
the bare unlink as a violation of the one-source/reuse principles at MAJOR or higher. That is an executed check against an
external oracle (the failure that actually happened).
