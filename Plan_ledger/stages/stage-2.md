# Stage 2 — Forks

A **fork** is a choice of mechanism class that sits inside an already-approved direction. Approving the
direction does not decide the fork. Every fork is posed to the owner, recorded with its provenance, and
only then written into the sheet.

**Mechanism classes that are always forks:**
- fixed constant vs derived / self-calibrating value (and: derived from what?)
- separate store / file / side table vs an attribute on the entity's own row
- content-addressed keying vs id-keyed
- synchronous in-turn vs background / deferred
- module constant vs tunable vs config file vs prompt-strings file
- cap / truncate vs fall back vs abstain
- which path runs first and which is the fallback (any direction change)
- delete vs keep vs migrate existing data or code
- a new dependency, model, or external service
- anything that touches a line of the invariants doc
- a persona-facing string (wording is the owner's byte-exact call; do not "improve" it)

**How to pose.** One AskUserQuestion per fork. The question names the mechanism plainly and states the
consequence of each option in a full sentence, including the current default if one exists in code.
Options are mechanisms, not adjectives: write "a hardcoded constant, -9.25, valid only for this reranker
model" rather than "a trustworthy floor". Always include "None of these; I'll describe it". Never bundle
forks into one call; never bury a fork inside a proposal paragraph that ends "say go".

**What a "go" covers.** The owner's approval of a proposal confirms exactly the sentences the proposal
stated. If the proposal said "not a threshold; I'll bring you the forks", then a threshold written
afterwards is an unposed fork, however well-justified. Before writing any mechanism into the sheet, ask:
which ledger line, with which quote, confirms this mechanism? If none, pose it.

**Teammate self-resolutions** (a build lane resolving an ambiguity itself) are recorded
`[PROPOSED:<lane> | UNCONFIRMED]` and reported to the owner as such; they may proceed as a working
assumption only if the owner has said working assumptions are acceptable for that class, and never
become `[<OWNER> …]` by relay.

**Time and usage pressure do not close forks.** If the owner wants to defer, the fork stays OPEN in the
ledger with the owner's deferral quote; the spec carries an explicit "OPEN fork" marker at the point of
use; the build may not ship the point of use as final.
