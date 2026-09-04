# Stage 6 — Red-team the code

**What this stage does:** independent cold review of the built code against {1.5-criteria,
2-plan}. A backstop to stage 3.

**Read `stages/charter.md` for the full red-team charter (the five lenses + the discipline
bullets + provenance + spot-verify + the conditional position/concurrency lenses), then apply
the additions below.** The charter core is given to the reviewer verbatim; the stage-6 additions
below (the mechanical-diff duty and the five-lens output-shape requirement) govern how the
reviewed diff is produced and how the reviewer's output must be shaped.

## Procedure

Spawn a fresh **cold subagent** with the code diff/files + `{1.5, 2}` + `redteam_context`. Spawn it
**foreground / blocking** (concretely: **`run_in_background: false`** on the spawn, never the
default background call) and capture its result in the **same turn** — a delegated runner does not
receive its own backgrounded child's completion (it routes to main), so a background-then-end-turn
spawn deadlocks the gate (`stages/stage-8.md`, FG). Same charter as stage 3, aimed at
code-vs-plan/criteria. **Spot-verify a sample of the reviewer's
cited file:lines actually exist** (guards fabricated citations — the charter's consumer duty,
CH6). Generate the reviewed diff **mechanically** (`git diff <recorded-base>`; record the
command) — hand-curated ⇒ un-run for the omitted scope. Charter the reviewer for the **five-lens
output shape up front**, and reject a returned record missing any lens — re-run fresh, never
re-polled (ST6e). Write `6-redteam-code.md` as a verbatim
record (same provenance duties as stage 3).

## Stage-6 addition to the charter

**Stage-6 reviewed diff generated mechanically (ST6d).** At stage 6 the reviewed diff is
generated **mechanically** (`git diff` against the recorded base, or an equivalent captured
command), the command recorded in `6-redteam-code.md` — a hand-curated file set = the review is
un-run for the omitted scope.

**Stage-6 reviewer emits all five lenses explicitly (ST6e).** The charter the stage-6 reviewer
is given must require it to render **each of the five lenses** — Factual, Logical, Missed
opportunity, Unstated assumptions & risks, Fidelity — as **its own labeled verdict**, even when a
lens is clean (a clean lens states "no issue found" against that named lens; the factual and
fidelity clean verdicts additionally carry their charter-mandated earned evidence — citations,
pinned terms). A `6-redteam-code.md` record whose reviewer output is missing any of the five
lenses is **incomplete and treated as un-run** for the missing lens(es), and the review is
re-run — analogous to stage 3's CH8 (no coverage-challenge section ⇒ un-run for that lens). This
makes a clean stage-6 verdict **auditable per-lens on the record itself**, rather than depending
on the runner to reconstruct which lenses were exercised from a terse summary. Require this
five-lens shape **up front in the charter given at spawn**, so the reviewer's first result
already carries all five — do **not** re-poll or revive a completed terse reviewer to backfill the
missing lenses (reviving a finished subagent to await its reply is the foreground/deadlock hazard
the stage-8 FG rule warns against: a delegated runner does not receive its own child's
completion). If a record is still short a lens despite the up-front requirement, re-run a **fresh
full five-lens** cold review, not a re-poll of the old one.

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
validated. A missing/empty path is surfaced to the human before proceeding (fix the config, or
record a named degraded-review acceptance in `decisions.md`) — a reviewer handed dead paths
silently degrades to docs-only reasoning, the loop's founding failure.
