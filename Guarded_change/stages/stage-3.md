# Stage 3 — Red-team the plan

**What this stage does:** independent cold review of {1-spec, 1.5-criteria, 2-plan} — the
assumption-catcher, and the loop's most important gate.

**Read `stages/charter.md` for the full red-team charter (the four lenses + the discipline
bullets + provenance + the conditional position/concurrency lenses), then apply the additions
below.** The charter core is given to the reviewer verbatim; the stage-3 additions
(coverage challenge + label audit) are given on top.

## Procedure

Spawn a **cold subagent** (no shared context; `general-purpose` or `Explore`). Give it read
access to `{1-spec, 1.5-criteria, 2-plan}` AND the priority-ordered `redteam_context` paths.
Charter it with the four lenses + evidence discipline from `stages/charter.md`. Write
`3-redteam-plan.md` as a **verbatim record** per the charter's provenance rule: embed the
charter given (core verbatim + task additions quoted), the exact context list (closed set:
stage artifacts + config `redteam_context` + spec touched-files + carried findings), the
reviewer's verbatim output, its agent type/model, and its reported context-file hashes —
missing any ⇒ the review is un-run. Require the **coverage challenge** (below); no such section
⇒ lens 4 un-run.

## Stage-3 additions to the charter

**Challenge criteria coverage (stage 3) — CH8.** Name the behaviors the change could plausibly
alter that **no criterion observes** — each named gap needs a concrete scenario and ranks by
impact. The finding is unmeasured blast radius, not "write more criteria"; precision
discipline is unchanged. A stage-3 review with no coverage-challenge section (an explicit
"none found" counts) is incomplete on lens 4 and treated as un-run for that lens.

**Audit the criterion labels and the stage-8 verification table (the gating guard) — CH9.** The
weight on each criterion is itself a claim to challenge, not a given:
  • every criterion marked **advisory** must carry a legitimate reason — challenge any that looks
    like a dodge to avoid verifying a real gate (relabelling a gating criterion advisory is the
    deferral loophole in disguise);
  • every gating `verified = yes` must have exercised the **path the criterion actually governs** —
    challenge any verified against a proxy (a mocked dependency, a disabled flag, a
    non-triggering input class);
  • a route-(a) **"representative" pre-ship harness is a claim about representativeness** —
    challenge whether it truly exercises the governed path (the Option-B smoke was *believed*
    representative and was not);
  • a route-(b) named risk-acceptance must actually be present in `decisions.md` where a gating
    criterion is unverified.
  A gating criterion whose label or verification cannot survive this challenge is treated as
  unverified — the same as if it had been deferred.

**A clean label-audit must be earned, like a clean factual lens — CH10.** A "labels and table
look fine" verdict is valid only if the review shows, per gating criterion, which governed path
it confirmed was exercised and what evidence it checked. An unsubstantiated clean label-audit
is treated as un-run and re-run — the same guard the factual lens already carries.

## Cross-cutting rules governing this stage

**Nothing self-certifies (CP1).** The author of an artifact never approves it. Review is done
by a reviewer with *no shared context* with the author (a cold subagent), so it doesn't inherit
the author's blind spots.

**Evidence over rhetoric (CP2).** Every criticism cites a line/file or a concrete failure
scenario. Where data exists, an argument from the data beats an argument from reasoning. "Seems
fragile" is not a finding; "line N does X, which fails when Y" is.

**"No issue found" is a valid result (CP8).** Reviewers are graded on precision, not body
count. This removes the pressure to manufacture faults that makes aggressive review
untrustworthy.

**Criteria are mandatory (ST1.5b).** Criteria are the **conformance oracle** for stage 8 and
are **mandatory** — without them (in either form) the loop refuses to proceed past stage 3,
because completion would be unverifiable.

**Information-preserving is not behavior-preserving (CP6, position lens; fires only in a
position-sensitive assembly).** In a position-sensitive assembly a change can keep every piece
of content and still change behavior, when an element's effect depends on its *position* rather
than its mere presence (recency, precedence, "before/after some input," adjacency). A check that
only asks "is every piece still present?" passes such a change blind: the content survives, the
behavior does not. (The reviewer's operative lens is the charter's position-lens bullet — the
full statement is in `stages/charter.md` / stage 1.5.)

**Shared state has more than one accessor (CP7, concurrency lens; fires only where the change
alters concurrency structure over shared state).** When a change introduces a new unsynchronized
accessor, or a new read→slow-work→write window, over shared mutable state whose atomicity an
existing transaction/lock does not already enforce, correctness depends on *every* accessor of
that state, not just the one being written. A guard is only as strong as its **scope** — a
lock-free accessor whose write interleaves in the gap is silently lost. (The reviewer's
operative lens is the charter's concurrency-lens bullet — the full statement is in
`stages/charter.md` / stage 1.5.)

**Review records are verbatim (ART2).** The review docs (`3-redteam-plan.md`,
`6-redteam-code.md`, and any targeted post-6 check record) are **verbatim records** — each
embeds the charter given, the exact context list, and the reviewer's raw output per the
charter's provenance rule; the author's interpretation belongs in `decisions.md`.

**`redteam_context` is priority-ordered (CFG2).** Because a cold subagent can't exhaustively
read a large codebase, list the most relevant entrypoints first with a short note on what to
check there. This keeps "independence" from degrading into "skimmed whatever fit in context."

**Paths are validated, not assumed (CFG3).** Mechanically check every path handed to a cold
reviewer (`redteam_context`, the spec's touched files, fixture paths) exists and is readable —
at run start for paths that exist then, and at each cold-reviewer spawn for any path not yet
validated. Gate 4 may not pass until the run-start validation result is recorded in
`decisions.md`. A missing/empty path is surfaced to the human before proceeding (fix the
config, or record a named degraded-review acceptance in `decisions.md`) — a reviewer handed
dead paths silently degrades to docs-only reasoning, the loop's founding failure.
