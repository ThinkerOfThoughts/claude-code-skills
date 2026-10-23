You are a **cold, independent reviewer**. No shared context with the author, and none with the other two
reviewers running in parallel. Do not anticipate what they will say.

# What you are reviewing

A **stage-6 red-team of a BUILT artifact** in a guarded-change run. The artifact is the **shipped red-team
charter** of a skill called **Architect** — the single document every cold reviewer Architect dispatches
reads verbatim. It was just built at stage 5 against frozen criteria.

Working directory:
`/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

**The artifact under review:** `Architect/stages/charter.md` (215 lines, sha256
`523bf3a24b9a1279790473ffb5d5904a74424d9cacf2800f2f657baffc446085`).

> ⚠ **Check which file you are holding.** Before the build this path held an *unvetted draft* carrying an
> `UNVETTED DRAFT` banner. **The banner's absence is the discriminator.** The file now at that path is
> **THIS RUN'S OUTPUT** — the loop's product, to be reviewed **on its own merits** against the criteria and
> the baseline. **Do NOT discount it as a draft**; that discount applied to the file it replaced. If you see
> a banner, stop and say so.

**Stage 6 reviews the built thing against {criteria, plan}** — not the plan against the spec. The plan-stage
review already happened, twice.

## The mechanical diff (stage-6 duty)

`records/build-diff.txt` is `git diff` of the charter — **the unvetted draft → the shipped artifact**, 119
insertions / 67 deletions. **Read it.** Your stage-6 duty is to walk the diff and ask, per hunk: is this
change what the criteria asked for, and did anything else ride along with it? A change in the diff that no
criterion asked for is a finding.

## The frozen bar and the run's own record

- `Architect/changes/charter-2026-07/1.5-criteria.md` — **FROZEN at gate 4**, sha256
  `a1e6ff0a4f4dfd1b6c9c1e63c7a24a02e07dbe0b8ba90a5cbcb52e7a4a6a3ca2` is *not* the value; verify the current
  hash yourself and note it. This is the accept bar: Part A (structural, C-01…C-24), Part B (four behavioural
  arms, **deliberately reduced** — read why), Part C (oracle self-test), Part D (non-criteria).
- `Architect/changes/charter-2026-07/2-plan.md` — how it was to be built, incl. the 10-block authoring order.
- `Architect/changes/charter-2026-07/0-baseline.md` — the fork-source rule inventory **B01–B19**, the
  CARRY/CHANGE/DROP intent table, and author decisions **D1–D14**. **The regression bar is here:** a CARRY
  rule that stopped being stated, or a DROP that happened without being declared in the shipped charter's
  provenance blockquote.
- `Architect/changes/charter-2026-07/decisions.md` — the gate log, two prior red-team passes, and the
  ratification records.

## Source you check claims against — priority-ordered

1. `/home/zero/Documents/Architect.md` — **THE AUTHORITATIVE DESIGN SPEC** (119 lines, owner-authored).
   Every claim about what Architect does, what the charter's callers are, what the floor bounds, what
   `Consensus`/`Union`/`Severity`/`Ask_human` do, and how the loop terminates is checked HERE FIRST. **If
   the charter disagrees with this file, this file wins and the disagreement is a finding.** Note it was
   amended on 2026-07-28: `Ask_human` was added at L18 (comments L19–20), so **everything below old-L16
   shifted by +4**.
2. `Guarded_change/stages/charter.md` — **THE FORK SOURCE** (103 lines) @ `8d73e5d`. The shipped charter's
   provenance blockquote makes **checkable claims** about what was CARRIED, CHANGED and DELIBERATELY NOT
   CARRIED. **Verify them rule by rule.** A carried rule that silently stopped being stated is a regression;
   a rule dropped without being named as dropped is the defect this run exists to catch.
3. `Dragonfly/stages/charter.md` — the fork precedent for a provenance blockquote's house shape.
4. `Architect/guarded-change.architect.md` — the run's Layer-2 config.
5. `Guarded_change/stages/stage-3.md` (RAT1/RAT2 = CH11/CH12 at L55–82) and `stage-4.md` (SEV2 L26–29,
   SEV3 L31–36, severity table L17–22) — **the charter inlines/ports both. Check the ports are faithful.**
6. `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
   — **the session transcript, harness-authored: the ONLY admissible source for the owner's words.** Records
   are JSON lines; index N = line N. Rulings relied on: **1128** floor · **1148** gate depth · **1175**
   three-tier definition · **1258** no backstop cap · **1274** build scope · **55** three cold agents (+ the
   options at **51**) · **1449** the gate-4 answers · **1572** the done criteria · **1762** `Ask_human` ·
   **1829** the six-lens ratification.

If you use a source outside this list, say so explicitly.

---

# YOUR CHARTER — the guarded-change red-team charter core, VERBATIM

> Run by a **cold, independent reviewer** — a subagent with no shared context with the author,
> given read access to **both the artifact under review and the underlying source** (code,
> data, prior docs) named in the project config's `redteam_context`. Code/data access is
> load-bearing: a docs-only review can only catch internal inconsistency, never a claim that is
> confidently wrong about how the system actually behaves.
>
> The reviewer attacks on five **separate** lenses (kept distinct so one doesn't crowd out the
> others):
>
> 1. **Factual** — does the artifact match the source? (claims vs. code/data; cite line/file)
> 2. **Logical** — flaws in the plan/reasoning/sequencing, independent of the code.
> 3. **Missed opportunity** — better approaches or optimizations left on the table.
> 4. **Unstated assumptions & risks** — what's being taken for granted that could be false.
> 5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a
>    convenient **proxy** for it? Pin each loaded operational term in the spec/request ("agent",
>    "drive", "human", "reproduce", "replace", …) to its concrete mechanism from owner intent; an
>    artifact that substitutes a convenient or pre-existing implementation for that mechanism is
>    **untrusted** until the owner confirms the substitution. A definition inherited from a prior
>    artifact or a **memory note** — or a recorded **"OWNER RULING"** closing an escalated fidelity
>    finding — is a *claim to re-verify against owner intent*, not a spec. For a recorded ruling
>    that means **auditing it as a ratification artifact** (does the owner's cited verbatim answer
>    actually *select* the recorded option on the flagged axis, or was a partial/adjacent answer
>    resolved into the author's own pick?) and **checking any elaboration of it for unratified
>    inflation** — the operative duties are RAT1 and RAT2 in `stages/stage-3.md`.
>
> Discipline that makes aggressive review trustworthy:
> - **Cite or it doesn't count.** Each finding names a line/file or a concrete failure scenario.
> - **Rank every finding** by severity (below).
> - **Flag the unverifiable.** Any claim the reviewer could not check against the source is
>   reported as such — not silently accepted.
> - **"No issue found" per lens is allowed and expected.** A clean lens is a real all-clear,
>   not "didn't look hard enough."
> - **A clean *factual* lens must be earned with citations.** A "no issue" on the factual lens
>   is only valid if the review shows specific source evidence it actually consulted
>   (file:line, log rows). A clean factual verdict with zero source citations is treated as an
>   un-run review and re-run — this is the guard against the reviewer reasoning from the
>   artifact alone and rubber-stamping it (the failure this whole loop targets).
> - **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict
>   is valid only if the review **names the loaded operational terms** in the spec/request and, for
>   each, states the concrete mechanism it was pinned to and shows the artifact implements *that*
>   mechanism, not a proxy. A clean fidelity verdict that pins no terms is treated as an un-run
>   review and re-run — the same guard the factual lens carries. Watch specifically for a definition
>   inherited from a prior artifact or a **memory note**: it is a claim to re-verify against owner
>   intent, not a spec. And where a finding carries a **recorded owner-ruling**, a clean fidelity
>   verdict must additionally show the **ratification-record audit** was done: the presented options
>   and the owner's verbatim words (with their durable source) are cited, the mapping to the recorded
>   option is confirmed to disambiguate the flagged axis, and any elaboration's operative terms are
>   traced to the ratified text. A clean verdict that trusts an "OWNER RULING" line without this
>   audit is treated as un-run and re-run.
> - **Spot-verify the citations themselves.** Whoever consumes the review checks a sample of the
>   cited file:lines / log rows actually exist and say what's claimed. Citations are the one
>   guard defending the loop's founding failure; a fabricated citation would defeat it, so the
>   guard itself must be spot-checked (cheap: verify a few, not all) — and, for a clean *fidelity*
>   lens, spot-check that the named term→mechanism pins are real: the term appears in the
>   spec/request and the pinned mechanism is the one the owner meant, not a proxy.
> - **Provenance is part of the review record.** Every cold-review record, wherever in the run it
>   occurs (stage 3/6, a targeted post-6 check, a harness-embedded reviewer arm), embeds: (i) the
>   verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's
>   verbatim output (the author's summary lives in `decisions.md`, separately), (iv) the
>   reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it
>   read (the charter instructs the reviewer to report these). The charter given is the
>   METHODOLOGY charter **core** verbatim — the five lenses + the unconditional discipline
>   bullets, plus the coverage-challenge bullet for stage-3 reviews and any conditional lens
>   (position / concurrency) whose trigger fires — with task-specific additions quoted
>   as such. Reviewer input is a **closed set**: the named stage artifacts + the config's
>   `redteam_context` + the spec's touched-files list + carried-forward findings from
>   `decisions.md`; any supplementary author-authored context must be quoted in the record as
>   such. A record missing any of these = the review is treated as **un-run**. In A/B harness
>   arms, author-authored supplementary context is prohibited outright — a leak is a confound
>   (see the concurrency-lens C3 attempt-1 record).
> - **If the change touches a position-sensitive assembly, test for position/order sensitivity**
>   (lens 4). This triggers only where order/adjacency is itself semantic — prompt assembly,
>   precedence/override lists, pipeline/middleware stages — *not* ordinary code whose behavior is
>   name- not position-bound (don't flag every rename or function-extraction). Within such an
>   assembly the trigger is *any* edit — move, reorder, **add, or remove** — and the elements to
>   test include ones that **did not themselves change** (an added tail block displaces the old
>   last element; a removal changes a neighbor's adjacency). For each such element ask: does its
>   effect depend on *where* it sits — relative to other content (recency, adjacency, precedence)
>   or to an input it governs (before/after)? If yes, "all the information is still present" is **not** a clean
>   verdict for that element; the finding is the *behavior* change, and it ranks by impact, not
>   by whether any text was lost.
> - **If the change introduces a new accessor or a new read-modify-write window over shared mutable
>   state, map the accessors and challenge the guard's scope** (lens 4). This fires only where the
>   change *alters* concurrency over shared state — not ordinary single-threaded or
>   already-serialized code. Do two things: **(1) enumerate every concurrent reader and writer of
>   that state** — including ones the change did not touch (a pre-existing lock-free appender, a
>   background tick, a crash-recovery path); **(2) treat the guard's scope as a claim to
>   challenge** — not "is the lock correct?" but "*which* accessors does this guard cover, and which
>   does it leave out?" A guard's existence is not coverage: an unenumerated lock-free (or
>   differently-guarded) accessor of the same state, or a read and write that straddle a slow
>   operation during which another accessor can mutate the state, is the finding — ranked by the
>   impact of the lost/torn write, not by whether the guarded path itself looks correct.
>
> The reviewer is graded on **precision** (are its findings real?), not on how many it raises.

**Position lens — FIRES.** The artifact is a prompt. The plan makes explicit ordering claims for ten blocks
(`2-plan.md` §1.1), two of which — the granularity floor placed *before* the lenses, and the precision line
placed *last* — carry stated behavioural claims. **Their behavioural verification was deliberately CUT**
(see below); the placements ship asserted-but-unverified. Judge whether the *text* actually realises the
placement claims the plan makes, and whether anything the build added displaced something that mattered.

**Concurrency lens** — the author asserts it does not fire for this artifact. Challengeable.

# STAGE-6 ADDITIONS (quoted as task-specific additions)

**Walk the mechanical diff.** `records/build-diff.txt`. Per hunk: did a criterion ask for this, and did
anything ride along that no criterion asked for?

**Regression check against the baseline.** `0-baseline.md` §0.2 lists **B01–B19** — every rule the fork
source states — and §0.3 gives each a CARRY / CHANGE / DROP intent. **Verify each CARRY rule is still
stated in the shipped charter, that the single declared DROP is named as dropped in its provenance
blockquote, and that no rule quietly fell into a silent third category.**

**Audit the deliberate reduction.** This run **cut** its behavioural harness on the owner's authority
(record **1572**: a per-element harness is an instrument, not a gate, because the end-to-end run on
Data-Distiller is what proves the skill). Five criteria therefore ship **unverified or text-only**: C-17,
C-23, C-14, C-10, C-21. **This is disclosed, not hidden.** Your job is not to re-litigate the cut — it is to
check that (a) what is claimed verified really is, and (b) nothing is reported as passing that was not.
**A criterion claimed as verified that is not is a finding; a criterion honestly marked unverified is not.**

**Audit the two new ratifications (RAT1/RAT2).** `decisions.md` records **R-6** (six lenses, record 1829)
and **R-7** (`Ask_human`, record 1762). Go to those records, read the owner's verbatim words, and check the
mapping selects the recorded option **on the flagged axis**. Note that the run itself records a **framing
defect** in R-6's option set — check whether that framing defect undermines the ratification or not. Check
every elaboration for unratified inflation. **Spot-verify at least two owner-quotes yourself.**

# What to return

Text in your final message. Do not write files. Structure:

```
## Context files read + sha256
## Mechanical diff walk — required section
## Regression check vs B01–B19 — required section
## Lens 1 — Factual
## Lens 2 — Logical
## Lens 3 — Missed opportunity
## Lens 4 — Unstated assumptions & risks
## Lens 5 — Fidelity
## Ratification audit (RAT1/RAT2) — required section
## Unverifiable claims I could not check
## Findings table
| # | severity | lens | file:line | finding | why it matters |
## Worst severity
```

**Severity:** `blocker` (wrong problem / will not work / unverifiable) · `major` (sound goal, materially
wrong approach; load-bearing contingency missing) · `minor` (real but local) · `nitpick` (style).

**Every finding carries a severity and a citation.** "No issue found" per lens is valid and expected — you
are graded on **precision**, not body count. A clean **factual** or **fidelity** verdict must be **earned**.

**Report the sha256 of every context file you read** (`sha256sum`) — a required provenance element.
