# The red-team charter (shared by stages 3 and 6)

This is the ONE copy of the red-team charter's common core. Stage 3 and stage 6 both read
it, then add their stage-specific bullets (stage-3.md adds the coverage challenge + the label
audit; stage-6.md adds the mechanical-diff duty). Stage 3 also audits proof homes (CH9) and stage 6
checks the tests the diff adds (ST6f). Both require the conformance section defined here (PRC). Verbatim from METHODOLOGY "The red-team
charter."

---

Run by a **cold, independent reviewer** — a subagent with no shared context with the author,
given read access to **both the artifact under review and the underlying source** (code,
data, prior docs) named in the project config's `redteam_context`, and (when the config names
them) the project's principles and prior-decision sources in its `principles_context`. Code/data access is
load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
confidently wrong about how the system actually behaves.

The reviewer attacks on five **separate** lenses (kept distinct so one doesn't crowd out the
others):

1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
3. **Missed opportunity** — better approaches or optimizations left on the table.
4. **Unstated assumptions & risks** — what's being taken for granted that could be false.
5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a
   convenient **proxy** for it? Pin each loaded operational term in the spec/request ("agent",
   "drive", "human", "reproduce", "replace", …) to its concrete mechanism from owner intent; an
   artifact that substitutes a convenient or pre-existing implementation for that mechanism is
   **untrusted** until the owner confirms the substitution. A definition inherited from a prior
   artifact or a **memory note** — or a recorded **"OWNER RULING"** closing an escalated fidelity
   finding — is a *claim to re-verify against owner intent*, not a spec. For a recorded ruling
   that means **auditing it as a ratification artifact** (does the owner's cited verbatim answer
   actually *select* the recorded option on the flagged axis, or was a partial/adjacent answer
   resolved into the author's own pick?) and **checking any elaboration of it for unratified
   inflation** — the operative duties are RAT1 and RAT2 in `stages/stage-3.md`.

Discipline that makes aggressive review trustworthy:
- **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
- **Rank every finding** by severity (below).
- **Flag the unverifiable.** Any claim the reviewer could not check against the source is
  reported as such — not silently accepted.
- **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear,
  not "didn't look hard enough."
- **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens
  is only valid if the review shows specific source evidence it actually consulted
  (file:line, log rows). A clean factual verdict with zero source citations is treated as an
  un-run review and re-run — this is the guard against the reviewer reasoning from the
  artifact alone and rubber-stamping it (the failure this whole loop targets).
- **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict
  is valid only if the review **names the loaded operational terms** in the spec/request and, for
  each, states the concrete mechanism it was pinned to and shows the artifact implements *that*
  mechanism, not a proxy. A clean fidelity verdict that pins no terms is treated as an un-run
  review and re-run — the same guard the factual lens carries. Watch specifically for a definition
  inherited from a prior artifact or a **memory note**: it is a claim to re-verify against owner
  intent, not a spec. And where a finding carries a **recorded owner-ruling**, a clean fidelity
  verdict must additionally show the **ratification-record audit** was done: the presented options
  and the owner's verbatim words (with their durable source) are cited, the mapping to the recorded
  option is confirmed to disambiguate the flagged axis, and any elaboration's operative terms are
  traced to the ratified text. A clean verdict that trusts an "OWNER RULING" line without this
  audit is treated as un-run and re-run.
- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
  cited file:lines / log rows actually exist and say what's claimed. Citations are the one
  guard defending the loop's founding failure; a fabricated citation would defeat it, so the
  guard itself must be spot-checked (cheap: verify a few, not all) — and, for a clean *fidelity*
  lens, spot-check that the named term→mechanism pins are real: the term appears in the
  spec/request and the pinned mechanism is the one the owner meant, not a proxy.
- **A claim resting on a quantity DERIVED from data is re-derived from the ground-truth records, by
  the reviewer, independently (ground-truth derivation, GT).** Any figure a claim leans on that is
  *derived* from data — a timing, interval, count, rate, ordering, threshold, magnitude, correlation,
  a baseline number, a measured pass-rate — must be computed from the **actual recorded ground-truth
  records**, never from an approximated, nominal, or assumed **model** of what the data *should* look
  like. A value taken from a **schedule, a config default, a spec value, a round-number estimate, or a
  summary aggregate is a PROXY for the data**, and any claim resting on a proxy is **UNGATED until
  re-derived** from the real records. The reviewer **independently re-derives** the quantity from the
  **raw source** — the error is usually in the **data source** (proxy vs. real records), not the
  arithmetic, so re-checking the author's math misses it. Cross-check the claim against the observed
  **shape**: a deterministic signature (the behavior on **100%** of occurrences) implies a
  **gate/threshold crossed every time**, not a stochastic cause; a claim whose predicted shape
  contradicts the observed shape is suspect. (This is the *data-source* sibling of the fidelity lens's
  **proxy mechanism** and stage-8's **proxy path**: here the proxy is for the **records the number
  came from**.)
- **A sign-off is a claim that the artifact meets the project's principles and the owner's prior
  decisions (conformance, PRC).** The principles are a check on the artifact, not an argument for
  it; passing the check is the justification. When the reviewer signs off on a spec, criteria, plan
  or code (it raises nothing ranked blocker or major), that sign-off states the artifact **meets
  every entry in the sources named by the config's `principles_context` and every prior owner
  decision in the reviewer's inputs** (rulings recorded in the spec or in owner entries of
  `decisions.md`, and the rulings the principles sources themselves state). Sources named in
  `principles_context` are the owner's standing words and are the authority for this check; that
  does not exempt a term in the artifact from the fidelity lens. The reviewer reads those sources
  itself (the author's account of an entry is not a substitute) and renders a labelled
  **Principles and decisions conformance** section in every record, whether or not it signs off,
  beside the five lenses and not a sixth lens, with two parts. (i) A **per-entry verdict**: every
  entry the sources state (principle, default, ruling, escalation rule, invariant; a tie-break list
  resolves conflicts between entries and is not itself verdicted), and every owner ruling in the spec
  and in the owner entries of `decisions.md`, gets meets / violates / n.a. with
  the line that shows it (the artifact line or source line that meets or violates it; for n.a., the
  line that shows why the entry is not engaged, and entries not engaged for the same stated reason
  may share one n.a. line that names each); an entry is judged as it is worded, including any
  exception it states for itself, and an n.a. is spot-checked like a citation. (ii) A **mechanism
  table**: for each operation the change performs that the project may already have a shared
  mechanism for (reading, writing, appending, deleting, parsing, locking, logging, finding a path,
  and similar), the existing mechanism that does that job, found by the reviewer searching the
  project's source for the operation (starting at `redteam_context`, the touched files, and the
  modules beside and imported by them) and not taken from the artifact's own account, with file:line
  and whether the artifact goes through it; "none exists" is a row too, with the search made.
  **A violation ranks at least MAJOR**: a principle the owner set is the bar for a sound approach,
  and the author's argument that the artifact is justified does not lower the rank. An exception
  stands only as an owner ruling recorded with the owner's quoted words and a durable source the
  author did not author (the RAT1 record in `stages/stage-3.md`, at stage 6 as well); an "OWNER
  RULING" line the author wrote is not one. Three things are violations whichever way the sources
  word their entries: (a) a **hand-written duplicate of an existing shared mechanism** (an operation
  doing the same job as one that exists); (b) a **shared mechanism worked around because it almost
  fits** instead of being extended; (c) an operation done **outside the shared module that already
  holds the neighbouring operations on the same data or files**, because that module lacks it: the
  operation belongs in that module, so it is extended and not bypassed. A new mechanism for a job no
  existing mechanism does, and that no such module is the home of, is not a duplicate; an entry that
  allows a simple new mechanism allows it only then. The check covers **omissions and existing
  code**, not only what the artifact says: an operation performed without being mentioned, a scope
  line ("out of scope", "not edited") that leaves a shared mechanism unextended, and a mechanical
  guard (a ratchet, a lint, a call count) that reads clean because the duplicate evades what it
  counts are all claims to challenge; a guard reading zero is not evidence that the shared
  mechanism was used. A clean conformance verdict is earned like a clean factual one: an aggregate
  "all met", a per-entry list without lines, or no mechanism table is treated as an un-run review.
  With no `principles_context` configured the reviewer says so, and still does the mechanism table
  and the prior decisions in its inputs. This applies to stage-3 and stage-6 reviews and to a
  targeted post-6 check; a harness-embedded reviewer arm does not get it, because author-supplied
  context there is a confound.
- **Provenance is part of the review record.** Every cold-review record, wherever in the run it
  occurs (stage 3/6, a targeted post-6 check, a harness-embedded reviewer arm), embeds: (i) the
  verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's
  verbatim output (the author's summary lives in `decisions.md`, separately), (iv) the
  reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it
  read (the charter instructs the reviewer to report these). The charter given is the
  METHODOLOGY charter **core** verbatim — the five lenses + the unconditional discipline
  bullets, plus the coverage-challenge bullet for stage-3 reviews and any conditional lens
  (position / concurrency) whose trigger fires — with task-specific additions quoted
  as such (a harness-embedded arm omits the PRC bullet and the `principles_context` sources, see PRC). Reviewer input is a **closed set**: the named stage artifacts + the config's
  `redteam_context` + the sources named in `principles_context` + the spec's touched-files list +
  carried-forward findings and owner entries from `decisions.md`; any supplementary author-authored context must be quoted in the record as
  such. A record missing any of these = the review is treated as **un-run**. In A/B harness
  arms, author-authored supplementary context is prohibited outright — a leak is a confound
  (see the concurrency-lens C3 attempt-1 record).
- **If the change touches a position-sensitive assembly, test for position/order sensitivity**
  (lens 4). This triggers only where order/adjacency is itself semantic — prompt assembly,
  precedence/override lists, pipeline/middleware stages — *not* ordinary code whose behavior is
  name- not position-bound (don't flag every rename or function-extraction). Within such an
  assembly the trigger is *any* edit — move, reorder, **add, or remove** — and the elements to
  test include ones that **did not themselves change** (an added tail block displaces the old
  last element; a removal changes a neighbor's adjacency). For each such element ask: does its
  effect depend on *where* it sits — relative to other content (recency, adjacency, precedence)
  or to an input it governs (before/after)? If yes, "all the information is still present" is **not** a clean
  verdict for that element; the finding is the *behavior* change, and it ranks by impact, not
  by whether any text was lost.
- **If the change introduces a new accessor or a new read-modify-write window over shared mutable
  state, map the accessors and challenge the guard's scope** (lens 4). This fires only where the
  change *alters* concurrency over shared state — not ordinary single-threaded or
  already-serialized code. Do two things: **(1) enumerate every concurrent reader and writer of
  that state** — including ones the change did not touch (a pre-existing lock-free appender, a
  background tick, a crash-recovery path); **(2) treat the guard's scope as a claim to
  challenge** — not "is the lock correct?" but "*which* accessors does this guard cover, and which
  does it leave out?" A guard's existence is not coverage: an unenumerated lock-free (or
  differently-guarded) accessor of the same state, or a read and write that straddle a slow
  operation during which another accessor can mutate the state, is the finding — ranked by the
  impact of the lost/torn write, not by whether the guarded path itself looks correct.
- **If the change modifies existing code or an existing artifact, check its history and red-team the
  change against the three regression modes (regression-safety history check, HIST).** A change that
  alters code someone already wrote is checked against what that code was *for*. On whichever fronts
  exist: **(a) git archaeology** — `git log -S`/`blame` the lines being changed and **read the
  introducing commit's message**, because a bandaid is often itself a *prior fix* whose message names
  the earlier bug and the constraints it defends; and **(b) issue/PR history** — search **closed and
  open** issues and PRs touching that file/component/subsystem. Then red-team the change against
  **three regression modes**: does it (1) **re-introduce a previously-patched bug**, (2) **worsen an
  existing one**, or (3) **create a new one**? **Lift any prior fix's stated constraints into hard
  bounds the change must not trip.** This is a *design-time* archaeology check, **distinct from** the
  stage-8 *empirical* regression measurement (H2/H8): it needs no baseline and fires at **stage 3** on
  the plan's proposed direction and again at **stage 6** on the built change. A change that silences
  today's symptom but revives the bug the code was patching is a regression, not a fix.

The reviewer is graded on **precision** (are its findings real?), not on how many it raises.
