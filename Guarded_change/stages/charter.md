# The red-team charter (shared by stages 3 and 6)

This is the ONE copy of the red-team charter's common core. Stage 3 and stage 6 both read
it, then add their stage-specific bullets (stage-3.md adds the coverage challenge + the label
audit; stage-6.md adds the mechanical-diff duty). Verbatim from METHODOLOGY "The red-team
charter."

---

Run by a **cold, independent reviewer** — a subagent with no shared context with the author,
given read access to **both the artifact under review and the underlying source** (code,
data, prior docs) named in the project config's `redteam_context`. Code/data access is
load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
confidently wrong about how the system actually behaves.

The reviewer attacks on four **separate** lenses (kept distinct so one doesn't crowd out the
others):

1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
3. **Missed opportunity** — better approaches or optimizations left on the table.
4. **Unstated assumptions & risks** — what's being taken for granted that could be false.

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
- **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
  cited file:lines / log rows actually exist and say what's claimed. Citations are the one
  guard defending the loop's founding failure; a fabricated citation would defeat it, so the
  guard itself must be spot-checked (cheap: verify a few, not all).
- **Provenance is part of the review record.** Every cold-review record, wherever in the run it
  occurs (stage 3/6, a targeted post-6 check, a harness-embedded reviewer arm), embeds: (i) the
  verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's
  verbatim output (the author's summary lives in `decisions.md`, separately), (iv) the
  reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it
  read (the charter instructs the reviewer to report these). The charter given is the
  METHODOLOGY charter **core** verbatim — the four lenses + the unconditional discipline
  bullets, plus the coverage-challenge bullet for stage-3 reviews and any conditional lens
  (position / concurrency) whose trigger fires — with task-specific additions quoted
  as such. Reviewer input is a **closed set**: the named stage artifacts + the config's
  `redteam_context` + the spec's touched-files list + carried-forward findings from
  `decisions.md`; any supplementary author-authored context must be quoted in the record as
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

The reviewer is graded on **precision** (are its findings real?), not on how many it raises.
