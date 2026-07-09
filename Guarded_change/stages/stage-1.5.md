# Stage 1.5 — Criteria

**What this stage does:** define the measurable bar for "correct/done" — the conformance
oracle stage 8 checks against — before any implementation.

## Procedure

Write `1.5-criteria.md`: a *checkable* accept bar. Each criterion is either **automated**
(true/false or numeric from instrumentation) **or** a **human-judged rubric** (named judge +
written scale + pass definition). **Mandatory.** If you cannot state checkable criteria in
*either* form, stop and resolve with the user — the loop may not pass stage 3 without them.
**Label each criterion gating or advisory (default gating; advisory only with a stated
reason).** If the change touches a position-sensitive assembly, add a behavior-preservation
criterion verified by execution; if it introduces a new shared-state accessor, add a
no-lost-update criterion verified by an executed interleaving.

## Rules governing this stage

**A bar, set first (CP4).** "Done" is defined as measurable acceptance criteria *before*
implementation, so completion is verified, not declared.

**A deferred gating criterion is not a met one (CP5).** "Done" requires every *gating*
acceptance criterion (1.5) to be **empirically verified first**, by exercising the path it
governs. A gating criterion that is postponed to "live/production," satisfied by a *proxy*
that avoids that path (a mocked dependency, a disabled flag, an input class that never triggers
it), or quietly dropped from the results, has **not** been met — deferral silently converts
*proven* done into *hoped* done. Advisory criteria may be deferred; gating ones may not.

**Criteria checkable, by one of two means (ST1.5a).** Each criterion must be **checkable**, by
one of two means:
- **Automated** — true/false or a number from instrumentation — e.g. "resolves a named folder
  + approximate filename in ≤2 tool calls, with no parent-directory traversal."
- **Human-judged rubric** — for qualities not reducible to a metric (e.g. "the persona reads
  as less repetitive"). Allowed *only* as an explicit rubric: a named human judge, a written
  scale, and what counts as pass. "Works well" with no rubric and no judge still fails review.

This degraded mode exists because some changes (especially to subjective/emergent behavior)
genuinely cannot be reduced to a metric pre-build; the loop must not force a fake number.

**An oracle must be shown able to fail; prefer positive assertion over absence (ST1.5f).** When a
criterion states *how* it is verified, its oracle must itself be a check that can be **shown able
to fail** — demonstrated to fire on a known-violating input (a self-test, e.g. run it against the
pre-change / known-bad state and confirm it flags the violation) before a "pass" from it counts;
until then that criterion's result is `verified = no`. Prefer a **positive per-site assertion**
(the desired value is present at each expected site) over a bare **absence check** (the bad token
is gone), because a fragile matcher makes "absent" silently, wrongly true; where an absence sweep
is unavoidable, pair it with the positive assertion and normalize the text first (strip markup,
flatten wraps). This is enforced at stage 8 by H6 (`stages/stage-8.md`).

**Criteria are mandatory (ST1.5b).** Criteria are the **conformance oracle** for stage 8 and
are **mandatory** — without them (in either form) the loop refuses to proceed past stage 3,
because completion would be unverifiable.

**Each criterion labeled gating or advisory; defaults to gating (ST1.5c).** A **gating**
criterion must be verified (by execution, stage 8) for the change to be accepted; an
**advisory** one is surfaced but does not block. A criterion is advisory *only* by explicit
choice with a stated reason — an unlabeled criterion is gating, so a forgotten label fails
safe. (This is the criterion-level sibling of the gating-vs-advisory distinction drawn for
regression *metrics* under "Regression must be measured on a comparable workload"; the weight
there protects against false regressions, the weight here against unverified completion.)

**Position-sensitive change → a behavior-preservation criterion, verified by execution
(ST1.5d, fires only when the change touches a position-sensitive assembly).** If the change
touches a position-sensitive assembly (moves, reorders, adds, or removes content — see
*Information-preserving is not behavior-preserving*), at least one criterion must assert that
the *behavior* which depended on the arrangement is preserved — not merely that the content
still appears somewhere. "Every block's text still survives in the assembled output" is a
content check; it cannot catch a position-sensitive element. Name the behavior and how it's
checked (e.g. "directive D still fires on the input class it governs," tested on a case that
exercises *only* that path). The criterion must **require empirical execution on that case**
(carried out at stage 8) — not satisfaction by re-inspecting the assembled text, which a
reviewer can wrongly *reason* looks fine. Where the effect is probabilistic
(recency/precedence usually shift a *rate*, not flip a switch), the criterion states the pass
rate it expects and the number of runs that establishes it (treat as a human-judged rubric per
above if no clean numeric floor exists), rather than relying on a single probe.

**New shared-state accessor → a no-lost-update criterion, checked by executed interleaving
(ST1.5e, fires only when the change introduces a new accessor or read-modify-write window over
shared mutable state).** At least one criterion must assert the **atomicity / no-lost-update**
property under a concurrent interleaving — a write by one accessor is not silently clobbered by
another. Name the interleaving and how it is checked (e.g. "an append by accessor B during
accessor A's read→write window survives"). Because real races are **non-deterministic**, the
criterion must be checked **deterministically** — by *injecting* the competing mutation into
the middle of the guarded window (not hoping a live thread race lands there) — or, where only a
live race is possible, over a **stated number of runs with a pass-rate floor** (treat as the
probabilistic rubric above). And, like any representative harness, the interleaving test must
**fail against the unguarded version**; a test that passes with and without the guard proves
nothing. Reasoning that "the lock covers it" is not satisfaction — only the executed
interleaving is.

**Information-preserving is not behavior-preserving (CP6, position lens; fires only in a
position-sensitive assembly).** In a **position-sensitive assembly** — one where order or
adjacency is itself semantic: prompt assembly, precedence/override lists, middleware/pipeline
stages, CSS-like last-wins rules — *not* ordinary code whose behavior is name- not
position-bound — a change can keep every piece of content and still change behavior, when an
element's effect depends on its *position* rather than its mere presence (recency, precedence,
"before/after some input," adjacency). A check that only asks "is every piece still present?"
passes such a change blind: the content survives, the behavior does not. The trap is not only
*moving* an element: **adding** one can displace the element that worked *because it was last*,
and **removing** one can change a neighbor's adjacency to the input it governs — so a diff in
which "nothing moved" is not exoneration. (E.g. a directive whose compliance depends on
appearing *before* the input it governs; a block that works *because* it is last.) When a
change moves, reorders, adds, or removes anything in such an assembly, treat every affected
element's *position* — including elements that did not themselves change — as load-bearing
until shown otherwise.

**Shared state has more than one accessor (CP7, concurrency lens; fires only where the change
alters concurrency structure over shared state).** When a change **introduces a new
unsynchronized accessor, or a new read→slow-work→write window, over shared mutable state whose
atomicity an existing transaction/lock does not already enforce**, correctness depends on
*every* accessor of that state, not just the one being written. A guard (lock, transaction,
queue, CAS) is only as strong as its **scope** — the set of accessors it actually covers; a
*different*, lock-free accessor whose write interleaves in the gap is silently lost (lost
update / torn write). This is the same blind spot as *Information-preserving is not
behavior-preserving*, one level out: a review that only asks "is this guard correct?" passes
the change, because the defect lives in an accessor it never **enumerated**. A guard's mere
existence does not settle "already enforced" — its scope must be enumerated, not assumed; when
it is unclear whether a guard covers *every* accessor,
treat the state as unguarded. Triggers only where the change alters the concurrency structure
over shared state — *not* ordinary single-threaded or already-serialized code.

**Acceptance criteria are per-change, in the spec, not in the config (CFG4).** Acceptance
criteria (1.5) are per-change, authored in the change's spec — *not* in the project config. The
config holds standing measurement/regression setup that's stable across changes.

**Criteria are mandatory; baseline is optional (CFG5).** No criteria → the loop won't pass
stage 3. No baseline → stage 8 runs conformance-only and says so.

## Stop for a human at this stage (HIL / SK-STOP)

The skill **stops for a human decision** when **criteria or config needed to proceed are
missing** — it refuses rather than guesses. Refuse to guess project metrics or acceptance
criteria — that's the exact failure this loop exists to prevent.

## Self-check criteria (when the artifact under change is this skill)

When a run's subject is the guarded-change skill itself, the standing self-check criteria
apply as gating criteria authored here:
- **live copy == source copy** (`diff` of the installed skill vs. the repo source);
- **SKILL.md ↔ METHODOLOGY.md (and stage files) consistency** on every rule stated in more than
  one place;
- **a behavior-preservation criterion for anything moved or removed** (skill files are a
  position-sensitive assembly — these documents are prompts — so the position lens applies).
Non-trivial skill-file edits take the **full loop**, not a stage-3 pass alone.
