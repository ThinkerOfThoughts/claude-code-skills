# 2 — Plan: the owner-ratification guard

How the two guards are added to the skill, the **verbatim proposed text** for each site (so the
stage-3 red-team reviews the actual wording, not a paraphrase), how each criterion is measured,
and the routing thresholds.

## Design summary

One concept — **a recorded owner-ratification (and, more broadly, any human-gate answer) is an
artifact to verify / obtain, not an assertion to trust or synthesize** — realized as three
named cross-cutting rules, each with a single canonical home, and operative slices at the sites
that need them:

- **RAT1** (ratification requires an owner-selection artifact + re-ask on a non-disambiguating
  answer) — canonical in `stage-3.md`; slices in `charter.md` (fidelity lens), `stage-1.md`
  (author records it), `stage-4.md` (gate + HIL), `SKILL.md`/`METHODOLOGY.md` (HIL).
- **RAT2** (elaboration inherits only what was ratified) — canonical in `stage-3.md`; slice in
  `charter.md` (fidelity lens).
- **RAT3** (delegation preserves the HIL — the subagent halts and relays a stop-for-human
  question verbatim [skill-enforced]; the orchestrator relays it to the human and never answers
  as the owner [caller-side obligation]) — canonical in `METHODOLOGY.md` "Human-in-the-loop";
  operative pointer in `SKILL.md` "Stop-for-human". **Reinforced (not guaranteed) by RAT1:** an
  orchestrator that self-answers must also fabricate a durable, spot-checkable source to pass the
  CH11 audit — a higher, checkable bar, not an impossibility (matches E10 / criterion C15; the
  loop cannot enforce the orchestrator half because the orchestrator is not running the skill).

Cold-review duties: **CH11** (ratification-record audit) + **CH12** (elaboration-fidelity
audit) are stage-3 additions parallel to CH8/CH9/CH10, plus a closed-set context addition (the
owner's verbatim exchange for any escalated fidelity finding).

This mirrors the skill's existing multi-site pattern (position/concurrency lens: charter bullet
+ cross-cutting CP + stage-1.5 duty + stage CH/H + one canonical statement, referenced
elsewhere). It is **additive** — it extends the fidelity lens (added `6171c2d`), it does not
rewrite it.

---

## Verbatim proposed edits

### E1 — `stages/charter.md`, Fidelity lens (lens 5)

**P-1 fix (stage-3 review):** rather than append a 6-sentence block *after* the lens's current
tail (the "memory note … not a spec" sentence — which is recency-privileged and would be
displaced), **extend that existing sentence in place** so the ratification case rides on the
same "claim to re-verify against owner intent" thought, with the full mechanism deferred to the
canonical home in `stage-3.md`. No ballooning, no stolen tail.

**Anchor (exact source, `charter.md:27-28`):** *"A definition inherited from a prior
artifact or a **memory note** is a *claim to re-verify against owner intent*, not a spec."*
→ replace with:

> A definition inherited from a prior artifact or a **memory note** — or a recorded **"OWNER
> RULING"** closing an escalated fidelity finding — is a *claim to re-verify against owner
> intent*, not a spec. For a recorded ruling that means **auditing it as a ratification
> artifact** (does the owner's cited verbatim answer actually *select* the recorded option on
> the flagged axis, or was a partial/adjacent answer resolved into the author's own pick?) and
> **checking any elaboration of it for unratified inflation** — the operative duties are RAT1
> and RAT2 in `stages/stage-3.md`.

### E2 — `stages/charter.md`, "clean fidelity lens must be earned" discipline bullet

**E2-anchor fix (stage-3 review Factual):** the real source at `charter.md:42` is
`- **A clean *fidelity* lens must be earned by pinning the terms.**` — `*fidelity*` is
**italic inside** the bold span (not `**fidelity**`). Match that exact string.

**Anchor:** append one sentence to the end of that bullet (after its final sentence, *"…it is a
claim to re-verify against owner intent, not a spec."*).

> And where a finding carries a **recorded owner-ruling**, a clean fidelity verdict must
> additionally show the **ratification-record audit** was done: the presented options and the
> owner's verbatim words (with their durable source) are cited, the mapping to the recorded
> option is confirmed to disambiguate the flagged axis, and any elaboration's operative terms
> are traced to the ratified text. A clean verdict that trusts an "OWNER RULING" line without
> this audit is treated as un-run and re-run.

### E3 — `stages/stage-3.md`, Procedure (closed-set context addition)

**Anchor:** append to the Procedure paragraph, after the closed-set description (*"…closed set:
stage artifacts + config `redteam_context` + spec touched-files + carried findings…"*).

> For any carried-forward **escalated fidelity finding** (a prior "OWNER MUST RATIFY"), the
> reviewer's context also includes the **owner's verbatim exchange** on that finding — the
> options presented + the owner's response — since the ratification cannot be audited without
> it; its absence degrades the fidelity lens to un-run and is surfaced to the human.

### E4 — `stages/stage-3.md`, new "Stage-3 additions to the charter" (after CH10)

> **Audit any owner-ratification of an escalated fidelity finding — CH11 (RAT1).** When the
> plan/spec closes an **escalated fidelity/intent finding** (a prior "OWNER MUST RATIFY") with
> a recorded owner-ruling, the reviewer **audits the ratification as an artifact**, using the
> owner's verbatim exchange (E3). A valid ratification cites (i) the flagged axis + the options
> presented, verbatim; (ii) the owner's response, verbatim, **with a durable source (a
> transcript line / a timestamped `decisions.md` owner entry) the author did not author, so the
> quote is spot-checkable** — a re-typed "verbatim" with no source is un-spot-checkable and
> treated as unverified; (iii) a mapping showing those words select the recorded option *on the
> flagged axis*. The finding to raise (ranks ≥ major): a ruling built on a **partial or
> adjacent** owner answer that does not disambiguate the presented options — especially one
> resolved into the author's *own recommended* option — is **not ratified**; the axis must be
> **re-asked**, not defaulted (the *unanswered-question-means-missed* principle applied to
> ratifications). For a **multi-turn** owner exchange the record captures the *confirming* turn
> with its qualifying context, and re-ask fires only when *no* turn disambiguates the axis (not
> on the middle of a legitimate exchange). A stage-3 review of a plan that carries a recorded
> owner-ruling with **no ratification-audit section** (an explicit "audited, valid — owner words
> + source cited + mapping shown" counts) is incomplete on the fidelity lens and treated as
> un-run for it. **Spot-verify** a cited owner-quote against its named source, exactly as the
> charter's citation spot-verify already requires for code claims.
>
> **Audit the elaboration of a ratified option — CH12 (RAT2).** Where the spec **expands** a
> ratified option into detailed commitments, the reviewer checks the expansion's **load-bearing
> operative terms** trace to the owner's words / the ratified option's stated meaning. The
> finding (ranks ≥ major): an elaboration that introduces operative commitments (a mechanism,
> an "only/every/never", a division of responsibility) **not present in or entailed by** the
> ratified phrase is an **unratified inflation** — untrusted until the owner confirms the
> expansion, exactly like a substituted mechanism. A clean verdict here must name the ratified
> phrase's operative terms and show the elaboration adds none beyond them.

### E5 — `stages/stage-3.md`, "Cross-cutting rules governing this stage" (canonical RAT1/RAT2)

**Anchor:** add two rules alongside the existing CP1/CP2/CH8… block.

> **A ratification is an artifact, not an assertion (RAT1).** An escalated fidelity/intent
> finding ("OWNER MUST RATIFY") is closed only by a **ratification record** — the flagged axis
> + the options presented to the owner (verbatim), the owner's response (verbatim, **with a
> durable source the author did not author — a transcript line or a timestamped `decisions.md`
> owner entry — so the quote is spot-checkable**), and a mapping showing those words select the
> recorded option *on the flagged axis*. A recorded "OWNER RULING: X" is the author's *reading*
> of owner intent and self-certifies nothing (CP1); it is audited cold (CH11). An owner answer
> that is **partial or adjacent** — it settles a sub-question but does not disambiguate the
> presented options against each other — is **not a ratification**: the loop **re-asks the
> flagged axis** and never resolves the answer into the author's own recommended option (the
> *unanswered-question-means-missed* principle). Because the record embeds the verbatim options
> + owner words + their **source**, it is genuinely **re-confirmable** — a later reader, across
> an autonomous run or a context compaction, re-checks the mapping *and the quote against its
> cited source* rather than inheriting a one-time reading or a re-typed reconstruction.
>
> **An elaboration inherits only what was ratified (RAT2).** When the spec expands a ratified
> option into detailed commitments, only what the owner's words / the ratified option's stated
> meaning **entail** carries the owner's authority. An expansion whose load-bearing operative
> terms (a mechanism, an "only/every/never", a division of responsibility) are absent from and
> not entailed by the ratified phrase is an **unratified inflation** — trusted no more than a
> substituted mechanism, and audited cold (CH12). The fix for an inflation is to confirm the
> expansion with the owner or narrow the spec back to the ratified meaning.

### E6 — `stages/stage-1.md`, new rule (author-side recording contract)

**Anchor:** add under "Rules governing this stage."

> **An escalated fidelity finding is closed by a ratification record, not a bare ruling line
> (RAT1).** When an "OWNER MUST RATIFY" fidelity finding is resolved, the spec records a
> **ratification record** — the flagged axis + the options presented (verbatim), the owner's
> response (verbatim, **with a durable source: the chat-transcript line (acceptable even for a
> just-made live ruling) or a timestamped, owner-attributed `decisions.md` entry** — the test is
> the owner's *quoted words with a locus*, not the author's paraphrase), and the mapping to the
> selected option — **not** a bare `## X (OWNER RULING <date>, option c)`. The cited source is what makes the ruling **re-confirmable**
> across autonomous runs and context compactions (a later reader re-checks the mapping *and the
> quote against its source* instead of trusting a re-typed reconstruction) and is what the
> stage-3 audit (CH11) spot-verifies. A **partial or adjacent** owner answer is not a
> ratification — re-ask the flagged axis rather than resolving it into a recommended option.
> Full statement in `stages/stage-3.md` (RAT1).

### E7 — `stages/stage-4.md`, gate behavior + HIL

**Anchor A:** add under "Other rules governing this gate."

> **An escalated fidelity finding resolves only on a passing ratification audit (RAT1/RAT2).** A
> prior "OWNER MUST RATIFY" finding counts as **resolved** for routing **only if** its
> ratification record passes the stage-3 audit — CH11 (the selection maps to the owner's
> verbatim words, spot-checked against their cited source, on the flagged axis) and CH12 (the
> elaboration adds no unratified operative commitment). If the record is absent, cites no
> verbatim owner selection or no durable source for it, rests on a **partial or adjacent**
> answer, or the elaboration inflates beyond the ratified option, the finding **stands at its
> escalated severity** and the loop **stops for the human to re-ask** the unresolved axis — it
> is never cleared by the presence of an "OWNER RULING" line alone. This is the fidelity sibling
> of *the reviewer's severity routes*: an author cannot self-clear an escalated fidelity finding
> by recording their own reading of owner intent. (Interaction with the iteration cap: a re-ask
> is already a stop-for-human, so no livelock; if a *second* owner answer is again
> non-disambiguating, the cap's human tie-break applies — the correct outcome, not a guard
> failure.)

**Anchor B (P-3 grammar fix):** insert a new clause **into** the "Stop for a human at this gate"
list, before its final "…and the iteration-cap / blocker-major-demotion tie-breaks above." item
(not appended after the closed "and"-terminated sentence). New clause:

> …; a **non-disambiguating owner answer** to an escalated fidelity finding (re-ask the flagged
> axis, never resolve the answer into a recommended option — RAT1); …

### E8 — `METHODOLOGY.md`

**Anchor A** — "What a run produces (artifacts)", after the `decisions.md` paragraph:

> **Ratification records.** An escalated fidelity finding (a stage-3 "OWNER MUST RATIFY") is
> closed in `1-spec.md` by a **ratification record** — the flagged axis + the options presented
> to the owner (verbatim), the owner's response (verbatim), and the mapping to the selected
> option — not a bare "OWNER RULING" line. A partial/adjacent owner answer is re-asked, not
> defaulted. The record is what stage 3 audits (CH11/CH12) and is re-confirmable across
> autonomous runs and compactions. Operative rule: `stages/stage-3.md` (RAT1/RAT2).

**Anchor B (P-3 grammar fix)** — "Human-in-the-loop" stop-conditions sentence (real text: *"…at
any blocker (loop about to restart), any major at stage 8, a gating criterion that cannot be
verified pre-ship, and missing criteria or config."*). **Insert** a new item before the final
"and missing criteria or config", not appended after it:

> …a gating criterion that cannot be verified pre-ship, a **fidelity ratification whose owner
> answer does not disambiguate the flagged axis** (re-ask, never default to the recommended
> option), and missing criteria or config.

### E9 — `SKILL.md`, "Stop-for-human"

**Anchor (P-3 grammar fix):** the real list ends *"…or a **gating criterion cannot be verified
pre-ship** (build a representative harness or get named risk-acceptance — never defer
silently)."* **Insert** the new item as the final "or" clause (so the list stays
grammatical), before the "Refuse to guess…" sentence:

> …never defer silently); or an **escalated fidelity finding's owner answer does not
> disambiguate the flagged axis** (re-ask the axis rather than resolving it into the recommended
> option — RAT1, and under delegation relay the re-ask to the actual human per RAT3; see
> `stages/stage-4.md`).

### E10 — `METHODOLOGY.md`, "Human-in-the-loop" (canonical RAT3)

**Anchor:** append a paragraph after the existing HIL paragraph.

> **Delegation preserves the human-in-the-loop (RAT3).** The loop's stop-for-human points are
> stops for the **actual human owner**, not for whatever agent happens to be running the loop.
> When the loop is executed by a **delegated subagent** (an orchestrator spawns a subagent to
> run the gated loop so its context stays out of the main session), the boundary between that
> subagent and the human must not absorb the question. RAT3 has two halves of **different
> enforceability**:
> - **Subagent half (skill-enforced).** On reaching any stop-for-human point, the subagent
>   **halts and returns the question verbatim** to its orchestrator — the options presented, the
>   specific unresolved axis, and (for a fidelity finding) the material needed to ratify —
>   **marked as a human-gate question to relay, not a result.** It does not resolve the point by
>   its own judgment or proceed past it. (The subagent *is* running this skill, so this half is
>   binding here.)
> - **Orchestrator half (a caller-side obligation, not skill-enforced).** The **orchestrator
>   relays the question to the human and relays the human's verbatim answer back into the loop;
>   it must not answer a stop-for-human question as if it were the owner.** The orchestrator is
>   not running this skill, so the loop cannot *enforce* this — it lives in the caller's
>   operating instructions and is stated here as a caller expectation. An orchestrator
>   substituting its own answer for the owner's is the same untrusted substitution the fidelity
>   lens forbids (RAT1), one level up. RAT1 **reinforces** (does not guarantee) this half:
>   because a valid ratification needs the owner's verbatim words *plus a durable, spot-checkable
>   source*, an orchestrator that answered on the owner's behalf must also fabricate a
>   spot-checkable source to pass the CH11 audit — a higher, checkable bar, not an impossibility.
> This is what makes RAT1's **re-ask** reach the human under delegation instead of looping back
> into the agent that mis-answered.

### E11 — `SKILL.md`, "Stop-for-human" (operative RAT3 pointer)

**Anchor:** append a paragraph after the existing stop-list paragraph.

> **Under delegation, these stops belong to the human, not the runner (RAT3).** If a subagent is
> running this loop, every stop above **halts the subagent and returns to its orchestrator as a
> human-gate question to relay verbatim** — the subagent does not self-answer or proceed (this
> half is enforced here). The orchestrator is expected to **relay to the actual human and relay
> the verbatim answer back, never answering as the owner** — a **caller-side** obligation the
> loop cannot itself enforce (full statement + the enforceability split in `METHODOLOGY.md`
> "Human-in-the-loop"; a fidelity ratification additionally needs the owner's verbatim words +
> durable source per `stages/stage-3.md` RAT1).

---

## Measurement — how each criterion is verified at stage 8

| Criterion | Gating | How measured |
|---|---|---|
| C1 catches FM1 (causal toggle) | gating | **Two cold-subagent runs** on `{incident OWNER-RULING section + 3-review OWNER-MUST-RATIFY + owner's verbatim exchange}`: one under the **post-edit** charter (E1–E5) — must flag non-ratified + call re-ask; one under the **pre-edit** charter — must NOT flag at full strength. PASS = post flags AND pre doesn't (or weaker). If the incident is too self-announcing to toggle, re-establish the catch on a constructed less-obvious case. Record both verbatim in `8-conformance.md`. |
| C2 catches FM2 (causal toggle) | gating | Same two-run regime on option (c)'s phrase + elaboration (`1-spec.md:131-144`) under CH12: post flags the inflation (≥1 named term), pre doesn't at full strength. |
| C3 precision (constructed) | gating | Two **constructed** fixtures in the change folder: (a) a fully-compliant ratification record (verbatim options + disambiguating owner response + source + mapping) — post-edit reviewer must NOT flag; (b) a legitimate entailed elaboration — must NOT be flagged as inflation (RAT2 precision). **Fixture well-formedness (LA-NEW-1):** the `8-conformance.md` record enumerates fixture (a)'s RAT1 fields against the record (options/response/source/mapping each present) so the reader confirms the fixture is genuinely compliant before trusting the no-flag result — a mis-built fixture must not silently pass. |
| C3p provenance sub-mode | gating | Constructed record whose "verbatim" is a source-less reconstruction; post-edit reviewer flags missing provenance, pre-edit doesn't (toggle). |
| C4 earned-clean present | gating | Positive assertion: E2 sentence in `charter.md` + CH11/CH12 earned-clean clauses in `stage-3.md`. |
| C5 canonical + consistent | gating | Positive per-site assertion (grep each site for its reference marker) + read-through for contradiction. |
| C6 end-to-end wiring | gating | Trace each link (charter→stage-1→stage-3→stage-4→SKILL/METHODOLOGY) to its site. |
| C7 oracle can fail | gating | Run the positive-assertion grep against the **pre-edit** tree (git stash / `git show HEAD:`) → confirm it reports markers **missing**; then against post-edit → present. |
| C8 live==source | gating | `diff -r ~/.claude/skills/guarded-change/ <source>` on shipped files → identical. |
| C9 behavior-preservation | gating | `git diff` scoped read: only additive/extending edits to named anchors; five lenses + CH8/9/10 + iteration cap unchanged in meaning. |
| C10 no project specifics | gating | `grep -iE 'bob|agentbob|t4|monologue|phoebe|nell' <shipped files>` → none. |
| C13 RAT3 stated + consistent | gating | Positive per-site assertion: canonical RAT3 in `METHODOLOGY.md` HIL (E10) + pointer in `SKILL.md` (E11); both name halt-and-relay-verbatim + never-answer-as-owner. |
| C14 RAT3 behavioral (subagent half) | gating | **Two cold runs**: post-edit-text runner on the FM1 stop situation halts + returns the marked-for-relay human-gate packet, no resolving action; pre-edit-text runner behaves materially worse (self-resolves/proceeds/omits the marking). If pre-edit already halts, record honestly as "clarifying addition, not behavior change" (LA-3). Subagent-half only. |
| C15 RAT3 orchestrator-half scoped as caller instruction | gating | Positive assertion: E10/E11 state the subagent-half is skill-enforced and the orchestrator-half is a caller-side obligation (not structural closure); no over-claim of "by construction". |
| C11 concision | advisory | Judgment: net addition proportionate; reuses cross-ref pattern. |
| C12 README | advisory | Surface to owner. |

## Instrumentation

No code instrumentation needed (doc change). The "instrument" is: (a) the cold-reviewer harness
(a real subagent spawn with the new charter + incident context — this is the representativeness
check, and it **must exhibit the phenomenon**: the pre-edit charter must *fail* to flag FM1/FM2
while the post-edit charter flags them, else the guard proves nothing); (b) a positive-assertion
grep script over the shipped files (C5/C7); (c) `diff -r` (C8); (d) `git diff` (C9).

**Representativeness note (spike-representativeness lesson):** C1–C3 are only meaningful if the
**pre-edit** charter, run cold on the same incident context, does **not** raise the RAT1/RAT2
findings (or raises them only weakly) — i.e. the guard changes the reviewer's behavior. Stage 8
runs the cold reviewer under BOTH the old and new charter on the FM1 item and confirms the new
charter is what produces the flag (the causal toggle). Without that contrast the "catch" could
be the base model noticing anyway.

## Routing thresholds

Standard severity model. For this doc change specifically:
- A stage-3 finding that the **new charter text itself** would let an invalid ratification
  through (a hole in E1–E5) = **blocker** → return to spec/plan.
- A stage-3 finding that the wording is materially confusing or mis-placed (position lens) =
  **major** → return to plan.
- Local wording/clarity = minor → fix in place.
- The **cold reviewer that reviews THIS plan** is independent of the author (main session);
  it reads the skill source + this change folder + the incident evidence.
