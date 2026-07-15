# Stage 3 — Red-team the plan

**What this stage does:** independent cold review of {1-spec, 1.5-criteria, 2-plan} — the
assumption-catcher, and the loop's most important gate.

**Read `stages/charter.md` for the full red-team charter (the five lenses + the discipline
bullets + provenance + the conditional position/concurrency lenses), then apply the additions
below.** The charter core is given to the reviewer verbatim; the stage-3 additions
(coverage challenge + label audit) are given on top.

## Procedure

Spawn a **cold subagent** (no shared context; `general-purpose` or `Explore`). Give it read
access to `{1-spec, 1.5-criteria, 2-plan}` AND the priority-ordered `redteam_context` paths.
Charter it with the five lenses + evidence discipline from `stages/charter.md`. Write
`3-redteam-plan.md` as a **verbatim record** per the charter's provenance rule: embed the
charter given (core verbatim + task additions quoted), the exact context list (closed set:
stage artifacts + config `redteam_context` + spec touched-files + carried findings), the
reviewer's verbatim output, its agent type/model, and its reported context-file hashes —
missing any ⇒ the review is un-run. Require the **coverage challenge** (below); no such section
⇒ lens 4 un-run. For any carried-forward **escalated fidelity finding** (a prior "OWNER MUST
RATIFY"), the reviewer's context also includes the **owner's verbatim exchange** on that finding
— the options presented + the owner's response — since the ratification cannot be audited
without it; its absence degrades the fidelity lens to un-run and is surfaced to the human.

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

**Audit any owner-ratification of an escalated fidelity finding — CH11 (RAT1).** When the
plan/spec closes an **escalated fidelity/intent finding** (a prior "OWNER MUST RATIFY") with a
recorded owner-ruling, the reviewer **audits the ratification as an artifact**, using the owner's
verbatim exchange. A valid ratification cites (i) the flagged axis + the options presented,
verbatim; (ii) the owner's response, verbatim, **with a durable source (a transcript line / a
timestamped `decisions.md` owner entry) the author did not author, so the quote is
spot-checkable** — a re-typed "verbatim" with no source is un-spot-checkable and treated as
unverified; (iii) a mapping showing those words select the recorded option *on the flagged axis*.
The finding to raise (ranks ≥ major): a ruling built on a **partial or adjacent** owner answer
that does not disambiguate the presented options — especially one resolved into the author's *own
recommended* option — is **not ratified**; the axis must be **re-asked**, not defaulted (the
*unanswered-question-means-missed* principle applied to ratifications). For a **multi-turn** owner
exchange the record captures the *confirming* turn with its qualifying context, and re-ask fires
only when *no* turn disambiguates the axis (not on the middle of a legitimate exchange). A
stage-3 review that carries a recorded owner-ruling with **no ratification-audit section** (an
explicit "audited, valid — owner words + source cited + mapping shown" counts) is incomplete on
the fidelity lens and treated as un-run for it. **Spot-verify** a cited owner-quote against its
named source, exactly as the charter's citation spot-verify already requires for code claims.

**Audit the elaboration of a ratified option — CH12 (RAT2).** Where the spec **expands** a
ratified option into detailed commitments, the reviewer checks the expansion's **load-bearing
operative terms** trace to the owner's words / the ratified option's stated meaning. The finding
(ranks ≥ major): an elaboration that introduces operative commitments (a mechanism, an
"only/every/never", a division of responsibility) **not present in or entailed by** the ratified
phrase is an **unratified inflation** — untrusted until the owner confirms the expansion, exactly
like a substituted mechanism. A clean verdict here must name the ratified phrase's operative
terms and show the elaboration adds none beyond them.

## Cross-cutting rules governing this stage

**Nothing self-certifies (CP1).** The author of an artifact never approves it. Review is done
by a reviewer with *no shared context* with the author (a cold subagent), so it doesn't inherit
the author's blind spots.

**A ratification is an artifact, not an assertion (RAT1).** An escalated fidelity/intent finding
("OWNER MUST RATIFY") is closed only by a **ratification record** — the flagged axis + the
options presented to the owner (verbatim), the owner's response (verbatim, **with a durable
source the author did not author — a chat-transcript line (acceptable even for a just-made live
ruling) or a timestamped, owner-attributed `decisions.md` entry — so the quote is
spot-checkable**), and a mapping showing those words select the recorded option *on the flagged
axis*. The test of the source is the owner's *quoted words with a locus*, not the author's
paraphrase. A recorded "OWNER RULING: X" is the author's *reading* of owner intent and
self-certifies nothing (CP1). It is a **new artifact authored *after* the escalation** (the
owner answers the "OWNER MUST RATIFY", then the assistant records the ruling), so the point of
auditing it cold (CH11) is to force that ruling back through review — the one step the loop
otherwise leaves self-certified. *This audit exists to make the check happen, not to add
detection:* a competent fidelity reviewer can already *detect* a fabricated or non-disambiguating
ruling once it audits the ruling against the owner's exchange — RAT1's work is to make that audit
**mandatory** (E3 puts the exchange in context; CH11 makes the audit a required section) and give
it a checklist, closing the gap where a self-certified ratification reached build unreviewed. An owner answer that is **partial or
adjacent** — it settles a sub-question but does not disambiguate the presented options against
each other — is **not a ratification**: the loop **re-asks the flagged axis** and never resolves
the answer into the author's own recommended option (the *unanswered-question-means-missed*
principle). Because the record embeds the verbatim options + owner words + their **source**, it
is genuinely **re-confirmable** — a later reader, across an autonomous run or a context
compaction, re-checks the mapping *and the quote against its cited source* rather than inheriting
a one-time reading or a re-typed reconstruction.

**An elaboration inherits only what was ratified (RAT2).** When the spec expands a ratified
option into detailed commitments, only what the owner's words / the ratified option's stated
meaning **entail** carries the owner's authority. An expansion whose load-bearing operative terms
(a mechanism, an "only/every/never", a division of responsibility) are absent from and not
entailed by the ratified phrase is an **unratified inflation** — trusted no more than a
substituted mechanism, and audited cold (CH12). The fix for an inflation is to confirm the
expansion with the owner or narrow the spec back to the ratified meaning.

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
