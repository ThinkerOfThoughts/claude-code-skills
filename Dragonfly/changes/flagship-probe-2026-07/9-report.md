# 9-report.md — flagship-probe-2026-07: outcome

## What this was

Dragonfly's documentation carries a "self-check" section listing claims about the skill.
One claim — the **flagship test** — was marked *"aspirational — not yet run":* the idea
that an agent following dragonfly will refuse to trust a misleading test until it
reproduces the bug for real, *and* that a normal agent without dragonfly would get fooled
by that test. Nobody had ever run it. This run was the first attempt, with one rule up
front: only relabel the claim as "tested" if it genuinely passed; otherwise leave it
honestly marked aspirational.

## What we ran

We built a small fake project — a "metrics store" with a planted bug (a bulk-import path
that skips cache invalidation, so the dashboard shows stale values) and an obvious test
that passes even though the bug is live. That passing-but-misleading test is the trap.

We then had six independent throwaway agents each investigate the bug from scratch:
three **without** dragonfly (the control group) and three **with** it. The hoped-for
result: the control group falls for the passing test, the dragonfly group refuses to and
reproduces the bug.

The experiment ran cleanly: the fixture was validated as a fair trap, the trap's hidden
grader worked, and we confirmed the control agents genuinely had no knowledge of dragonfly
(we verified the skill was invisible to them before they ran).

## Outcome: non-discriminating — no change to the skill

**All three control agents caught the bug.** Not one fell for the trap — each spotted that
the passing test didn't cover the buggy code path and reproduced the real bug itself. The
two dragonfly agents that finished also did the right thing (reproduced before concluding,
refused to overclaim).

So both groups behaved well, which means the experiment can't show that dragonfly made a
difference — there's no contrast to point to. In the probe's own terms this is a
**non-discriminating** result: it neither proves nor disproves the flagship claim. Per the
rule set at the start, that means **the label stays "aspirational" and SKILL.md is not
touched.** That is the honest state, and it's already what's live.

The limiting factor was the fixture, not the skill: the planted bug was simply too easy
for a capable model to catch, so a control agent doesn't need dragonfly to avoid the trap.
The stage-6 reviewer predicted exactly this before the arms ran.

## How this run was closed (an honest deviation, owner-approved)

The plan called for six more independent agents to grade each transcript blind, pinned to
run on Fable. Fable became too expensive to use, and — since the result was already a
clear non-pass (the control group didn't fall for the trap) — the owner chose to skip the
formal grading rather than pay for it or substitute a model they wouldn't trust for this
work. The per-arm assessment is therefore the author's, written in the conservative
(no-overclaim) direction, in `arm-outcomes.md`. This is a deliberate, recorded deviation
from the blind-scoring step; it is safe here specifically because the conclusion is "no
change to the skill," which is the opposite of the self-serving direction blind grading
exists to guard against.

One control-with-dragonfly arm (dfly2) was killed mid-run and not restarted, because its
result couldn't change the outcome.

## What we got out of it anyway

The probe apparatus now exists and is replayable: the fixture, the hidden grader, the
race-detector, the phased setup, and the frozen rules are all built, reviewed, and
committed. Anyone can re-run it later — with a stickier bug, or a weaker baseline model,
or a grader they trust — without rebuilding anything.

## Follow-ups (not started)

- **The trap needs to be harder to make the test discriminate.** As built, a strong
  baseline model catches the bug unaided. A future run wanting a real with/without-dragonfly
  contrast should plant a bug that is genuinely hard to reproduce (so trusting the passing
  test is tempting), or use a less capable baseline model. Candidate for a future probe
  revision — its own run.
- **The flagship label stays "aspirational."** It was never a blocker to editing dragonfly;
  it just leaves a standing "someday, demonstrate this" note open.
- Run evidence (full transcripts, post-run copies, diffs) is under `~/probe-arms-2026-07/`
  and the session subagents dir, referenced by task-id in `arm-outcomes.md`.
