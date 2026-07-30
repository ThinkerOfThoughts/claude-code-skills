# Aiming: you are reviewing a PROPOSED DIVISION, not a plan

`Divisible(task, granularity)` proposed a way to cut this task in two. **You review the cut.**

The divider re-derives while reviewers object to going forward — **at most four rounds.**

> **Your verdict has two separable parts and the divider needs both.** Say what you found, **and
> say whether you object to going forward with this cut.** They are not the same. A cut can be
> right and still carry standing findings; those findings **travel down with the sub-tasks** and
> are fixed by the planners below. **Filing majors is not by itself an objection** — if you would
> keep this joint, say so plainly, and the division proceeds carrying your findings.
>
> Withhold agreement only when you think **going forward with this cut at all** is wrong. Two
> earlier runs died because standing majors were read as disagreement and discarded reviewers who
> had written that the joint was right.

After the fourth round, the best 2-of-3-agreed split is returned; if none reached 2-of-3 the
divider returns `FAILED_TO_DIVIDE` and the owner is asked. **Raise what is real and raise it
early.**

## Your inputs

One thing beyond the common list: **the proposed division** — its two sub-tasks and the stated
seam. **There is no plan** — the divider was given none either. A split reviewer who thinks they
hold a plan judges the cut against how the *plan* is organised rather than against the shape of
the **task**, and endorses a seam whose wrongness nothing downstream can detect.

## What the floor means for you

It bounds **how deep the tree may go**, and you check it in one direction: **would either half
fall below it?** If so the task should not have been split at all. You are not looking for
vagueness — a sub-task is not required to be detailed, only to be a coherent whole task still
above the floor.

## The four questions

The six lenses all apply, aimed at the division. These are what they are aimed at:

1. **Coverage** — do the two halves cover the **whole task**, with no orphaned remainder and no
   portion both halves assume the other owns?
2. **The seam** — is the interface **stated**, and is it **sound**? Who produces what, who may
   assume what, what nobody owns. **An unstated seam is at least `major`** — everything below the
   cut inherits it.
3. **The floor** — would either half fall below it? That is a `blocker` against the division.
4. **Real joint or arbitrary cut** — does something actually change at this boundary, or was the
   task bisected for symmetry? Name what differs on each side. If nothing does, the cut is
   arbitrary however evenly it splits the work.

**"This task is indivisible" is a valid finding**, not a refusal to review.

**You are the last reader of this cut before anything is built on it.** No later reviewer sees
the alternatives that were available here, so a seam you pass is a seam nobody re-opens.
