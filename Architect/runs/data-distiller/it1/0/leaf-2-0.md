# Plan — implementation of the Data-Distiller skill

*Leaf plan. Fills `Architect/templates/spine.md`. Written cold: I did not read the sibling leaf
outputs in this run directory (`leaf-1-0.md`), nor the parent's `divide-0.md`, nor any other
`split-*` file — my task did not point at them and reading them would destroy the independence
the merge depends on.*

## Provenance and honesty notes (read before §1)

- **Sources I actually opened**, and against which every factual premise below is cited:
  `/home/zero/Desktop/claude-code-skills/Guarded_change/{SKILL.md,METHODOLOGY.md,guarded-change.companion.md}`,
  `/home/zero/Desktop/claude-code-skills/Guarded_change/stages/{charter.md,stage-0.md,stage-1.md,stage-1.5.md,stage-2.md,stage-3.md,stage-5.md,stage-7.md}`,
  `/home/zero/Desktop/claude-code-skills/Dragonfly/{SKILL.md,METHODOLOGY.md,dragonfly.companion.md}`,
  `/home/zero/Desktop/claude-code-skills/Architect/stages/{common.md,leaf.md}`,
  `/home/zero/Desktop/claude-code-skills/Architect/templates/spine.md`, plus directory listings of
  `~/.claude/skills/` and both sibling `stages/` directories.
- **`/home/zero/Desktop/claude-code-skills/Data-Distiller/` was NOT read, listed, or grepped.**
  I confirmed only that the path appears in a top-level `ls` of the repo root, which was
  unavoidable when listing the repo; I did not descend into it. Likewise
  `~/.claude/skills/data-distiller/` appeared in an `ls` of the installed-skills directory and
  was not descended into. Everything below is derived from the task statement plus the two
  sibling skills.
- **One unavoidable contamination to flag.** My harness's own available-skills listing includes a
  one-line `data-distiller` description string that was present in my context before I read
  anything. I did not treat it as a source and did not design toward it; but a reviewer should
  know it was visible, because it is the one piece of the off-limits implementation that reached
  me. It is visible identically to every sibling leaf, so it is not a divergence between us.
- **What I could not check.** (a) Whether Claude Code's skill loader requires anything in
  `SKILL.md` frontmatter beyond `name` and `description` — I observed only those two keys in both
  siblings (`Guarded_change/SKILL.md:1-4`, `Dragonfly/SKILL.md:1-4`) and inferred the contract
  from that sample of two. (b) Whether any token-count estimator is available to the runtime; the
  sizing rule in step 10 therefore uses a byte-based estimate with a configurable divisor rather
  than a real tokenizer. (c) The exact concurrency behaviour of the agent harness under load —
  the ceiling is honoured by batching, which I could not empirically validate from documents.

---

## 1. Problem / intent

**What this node plans.** The complete implementation of one artifact: a Claude Code skill named
`data-distiller`, expressed as a directory of markdown prompt files, installable at
`~/.claude/skills/data-distiller/`. This leaf owns the whole task it was handed — there is no
sibling half to coordinate with inside this plan.

**What the skill must be.** A corpus-agnostic, cold, multi-agent *method* for extracting
trustworthy, source-cited **factual** findings from a corpus too large to fit in one context
window. Its eight defining properties, taken verbatim in substance from the task:

| # | Property | Where this plan satisfies it |
|---|---|---|
| P1 | Decompose the corpus into analyzable items, size them, pick a per-item strategy when an item does not fit | steps 9–10 (`stage-1.md`, `stage-2.md`) |
| P2 | N independent cold analysts per item; read-only over the corpus; a source cited for every finding | steps 4, 11 (`analyst.md`, `stage-3.md`) |
| P3 | A cold verification pass that re-checks every citation and drops the unverifiable | steps 5, 12 (`verifier.md`, `stage-4.md`) |
| P4 | A merge ranking surviving findings by independent-analyst agreement | steps 6, 13 (`merger.md`, `stage-5.md`) |
| P5 | A blind roll-up: the coordinating agent reads only a terse per-child status, never findings | steps 3, 7, 14 (`common.md`, `node.md`, `stage-6.md`) |
| P6 | Per-corpus Layer-2 config supplies corpus specifics; the method stays corpus-agnostic | steps 2, 8, 17 (METHODOLOGY contract, `stage-0.md`, config template) |
| P7 | Restart and resume from on-disk state | steps 2, 7 (state layout in METHODOLOGY + the completion-terminator rule the node applies) |
| P8 | Facts, not interpretation | steps 3, 4, 5 (finding schema + the decidable-at-the-locus test) |

**Why it is worth building this way rather than "just read the corpus".** The two failure modes
the sibling skills were built against (`Guarded_change/METHODOLOGY.md:20-31`) recur here in a
sharper form: an unchallenged AI judgment, and an unmeasured claim. A single reader of a large
corpus produces an unchallengeable summary whose errors are invisible because the evidence is
gone. Data-Distiller's answer is that **every finding survives only if an independent cold agent
could re-derive it from a cited locus**, and that **the agent that steers the run never sees the
answers**, so its priors cannot propagate downward as expectations.

## 2. Approach

### 2.1 Adopt the sibling house shape, unchanged

Both working siblings share one layout, and copying it is deliberate — it is the shape a reader
of this repo already knows how to navigate, and the shape the install step already handles.

- A **`SKILL.md` router** carrying YAML frontmatter with exactly `name` and `description`, whose
  body is a short Inputs section, a stage table with one row per stage pointing at
  `stages/stage-N.md`, a Stop-for-human section, and a self-check section
  (`Guarded_change/SKILL.md:1-85`; `Dragonfly/SKILL.md:1-94`).
- A **`METHODOLOGY.md` reference spec** holding: why it exists, the loop diagram, the stage index
  table, the two layers, the Layer-2 config contract, and "what a run produces"
  (`Guarded_change/METHODOLOGY.md:1-196`; `Dragonfly/METHODOLOGY.md:1-181`). Both siblings state
  explicitly that this file is "opened for orientation and config setup — not to run a stage"
  (`Guarded_change/METHODOLOGY.md:10-11`).
- **One file per stage under `stages/`**, each with a `**What this stage does:**` line, a
  `## Procedure` section, and a `## Rules governing this stage` section
  (observed uniformly across `Guarded_change/stages/stage-{0,1,2,5,7}.md`).
- A **per-project config file** named `<skill>.<project>.md` holding a fenced YAML block plus a
  "Notes specific to this project" prose section (`Guarded_change/guarded-change.companion.md:1-123`;
  `Dragonfly/dragonfly.companion.md:1-59`).
- A repo-facing **`README.md`** that is *not* installed. Verified: `diff -rq` between
  `~/.claude/skills/guarded-change/` and the source directory reports `README.md`,
  `FRAMEWORK-FEEDBACK.md`, `changes/` and `guarded-change.companion.md` as source-only — the
  installed set is exactly `SKILL.md`, `METHODOLOGY.md`, `stages/`.

### 2.2 Split the dispatched prompts by role, not into one charter

Data-Distiller dispatches **four different kinds of agent** (analyst, verifier, merger, node).
The siblings each dispatch essentially one kind (a cold reviewer) and so get away with a single
`stages/charter.md`. Architect — the multi-agent skill in this same repo — instead uses
`stages/common.md` read first by every dispatched agent, plus one file per role
(`Architect/stages/common.md:3-4`: "Every agent Architect dispatches reads this file first, then
its role file"). Data-Distiller follows Architect, not the charter shape.

The rule I will hold while writing them: **`common.md` is included verbatim; role files add and
never restate a common rule.** If a role file needs to *modify* a common rule, that rule was
never common and moves down into the roles. The diagnostic when deciding what is common: ask
which roles can *act* on the rule; a rule only one role can act on is that role's, wherever it
currently sits.

**Alternative rejected:** one monolithic `charter.md` for all four roles. Rejected because every
dispatched agent reads its prompt verbatim, so a monolith spends every agent's context budget on
instructions most of them cannot act on — and, worse, it hides gaps: a monolith looks complete
while a role inside it has no instructions at all.

### 2.3 The blindness invariant, stated as a structural rule rather than a request

P5 is the property most likely to erode into a polite suggestion. I make it structural:

> **No agent both dispatches children and reads findings.**

Concretely: `node` dispatches and may read only `status.md`. `analyst`, `verifier` and `merger`
read findings and dispatch nothing. This makes blindness checkable by inspection of the role
files (does any file grant both?) rather than by trusting good behaviour at runtime. The terse
per-child status line is a **fixed-field record with no free-text field**, so there is no channel
through which finding content could reach the node even by accident:

```
<item-id> | <stage> | complete|partial|failed | findings=<int> | dropped=<int> | top_agreement=<int>/<N> | path=<relpath>
```

**Alternative rejected:** letting the node read a one-paragraph summary per child. Rejected
because a free-text field is exactly the steering channel P5 exists to close — the node would form
expectations from child 1's summary and carry them into how it dispatches child 2.

### 2.4 Verify before merge, never after

The ordering is load-bearing content, not sequencing convenience. If the merge ran first, the
verifier would see how many analysts agreed on each finding and would be biased toward sparing
the popular one. Verification therefore runs per-analyst-file, per item, **before any agreement
count exists**, and the verifier is prompted with no knowledge of N or of the other analysts'
outputs.

### 2.5 "Facts, not interpretation" reduced to a decidable test

A banned-word list ("suggests", "implies", "appears to") is a heuristic and will be gamed by
paraphrase. The operative rule is instead a decision procedure:

> A finding is admissible only if its claim can be decided true or false **by reading its cited
> locus alone**, with no other part of the corpus and no reasoning about causes or motives.

The banned-word list survives only as a *screening aid* the verifier may use to find candidates
for that test, never as the test itself. Where the source *itself* interprets, the fact is about
what the source says, and the finding must be phrased that way with the interpretive language
inside the quote.

### 2.6 Resume via a completion terminator, not a separate state database

P7 is satisfied by making every per-unit output file self-describing: **the last line of any
completed unit file is exactly `STATUS: complete`.** Resume treats any expected file that is
missing, or present without that terminator, as not-done and re-runs that unit. This needs no
lock file, survives a hard kill mid-write (a truncated file simply lacks its terminator), and is
checkable with `tail -1`.

**Alternative rejected:** a `state.json` updated as work proceeds. Rejected because it introduces
a shared mutable file written by many concurrent agents — a lost-update hazard for no gain, since
the per-unit files already carry the information.

### 2.7 Build the skill by writing files, then prove it with one assembled end-to-end run

The acceptance evidence is **one real distillation run against a real corpus that does not fit in
one context window**, not a battery of isolated behavioural micro-tests on individual stages.
Rationale: agent behaviour is non-deterministic, so an isolation test of one stage needs repeated
trials and a stated pass rate to mean anything, and the test mechanism then becomes a second AI
artifact that itself needs reviewing. **Hard stop rule for this build: if any test mechanism is
rebuilt more than three times, stop building it and move that check into the assembled
end-to-end run.** Count rebuilds of the mechanism, not runs of the test.

## 3. Interfaces & seams

**Consumes:**

1. **A Layer-2 per-corpus config file**, `data-distiller.<corpus>.md`, found in or near the
   working directory — the same discovery pattern the siblings use ("Look for one (e.g.
   `guarded-change.*.{md,yaml}` in or near the working dir)", `Guarded_change/SKILL.md:16-17`).
   It supplies: what an analyzable item is, what is off-limits, the concurrency ceiling, N, the
   context budget, and the extraction brief. **The skill refuses to invent any of these** — the
   same refusal both siblings make ("Do not invent project metrics",
   `Guarded_change/SKILL.md:18`; "Do not invent project specifics", `Dragonfly/SKILL.md:20`).
2. **The corpus itself**, read-only, at the paths the config's `root` names.
3. **The invoking session or orchestrator**, which receives stop-for-human questions verbatim.

**Emits:**

1. **`<output.dir>/findings.md`** — the corpus-level result: verified, source-cited factual
   findings ranked by independent-analyst agreement, with per-finding `agreement: k/N`, plus a
   named list of everything skipped or unanalyzable.
2. **`<output.dir>/status.md`** — the append-only fixed-field per-unit status log; this is the
   *only* interface between the working agents and any dispatching agent.
3. **`<output.dir>/decisions.md`** — append-only gate/override/resume log, mirroring both
   siblings' `decisions.md` (`Guarded_change/METHODOLOGY.md:174-180`).
4. **Per-item intermediates** under `items/<id>/` that make every ranked finding traceable back
   to which analyst raised it and what the verifier checked.

**Seam to the human.** Stop-for-human points (listed in §6) halt and ask. Under delegation the
running agent halts and returns the question verbatim to its orchestrator rather than
self-answering — the subagent half of the rule the sibling states at
`Guarded_change/METHODOLOGY.md:213-219`.

**Seam to the sibling skills.** None is required at runtime; Data-Distiller neither invokes nor
is invoked by guarded-change or dragonfly. The one relationship is authorial: **non-trivial edits
to Data-Distiller's own files should go through guarded-change**, because these files are
position-sensitive prompt assemblies — the self-check stance both siblings take about their own
files (`Guarded_change/SKILL.md:75-85`, `Dragonfly/SKILL.md:83-94`).

## 4. Steps

*Ordering rationale: contracts before the prompts that cite them (step 2 before steps 3–15);
shared before specific (step 3 before steps 4–7); role files before the stage files that dispatch
those roles (steps 4–7 before steps 11–14); the router written after the files its table points at
(step 16); then packaging (17–18), then the static check (19), then install (20), then the
assembled acceptance run (21–23).*

**Step 1. Create the source directory skeleton.**
Create `/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/` and
`/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/stages/`. *Note on the name:* the
canonical sibling-consistent directory name is `Data-Distiller/`, but that path is declared
off-limits for this run and already occupied; the implementation is therefore built at
`Data-Distiller-impl/` and the executor renames it to `Data-Distiller/` only if the occupying
directory is removed or the run is told otherwise. Every path below is relative to this root.

**Step 2. Write `METHODOLOGY.md`.** The reference spec. Sections, in order:
- Title + a two-sentence statement of purpose: a cold multi-agent method for extracting
  trustworthy source-cited **factual** findings from a corpus too large for one context window;
  no finding survives that an independent cold agent could not re-derive from its cited locus.
- *"This document is the orientation/reference spec … opened for orientation and config setup —
  not to run a stage"* — matching `Guarded_change/METHODOLOGY.md:10-11`.
- **Why this exists** — the three failure modes, each mapped to the structural defence:
  (1) *the unchallengeable summary* — one reader compresses a corpus and the evidence is gone →
  N independent analysts + mandatory citations; (2) *the confident citation that does not say
  what it is claimed to say* → the cold verification pass; (3) *the steered result* — a
  coordinator's expectations propagate into what its children look for → the blind roll-up.
- **The pipeline** — a fenced ASCII diagram, stages 0–7, one line each, in the order of §4
  steps 10–17.
- **Stage index table** — `| Stage | File | What it covers |`, one row per stage file.
- **The dispatched roles** — a table `| Role | File | Reads | Writes | May dispatch? |` with the
  four roles, and beneath it the blindness invariant in bold: *no agent both dispatches children
  and reads findings.*
- **The two layers** — Layer 1 agnostic core (this doc + SKILL.md + `stages/`); Layer 2 per-corpus
  config. Mirrors `Guarded_change/METHODOLOGY.md:90-95`.
- **The config contract (Layer 2)** — the full YAML skeleton reproduced in step 19 below, plus
  its rules: `item_rule` is mandatory and never invented; `off_limits` patterns are resolved to
  real paths and checked at intake; `analysts.n` must be ≥ 2 or agreement is meaningless and the
  run refuses to start; `question.brief` is mandatory; `max_concurrent_agents` defaults to 4;
  `context_budget_tokens` defaults to 120000; `bytes_per_token` defaults to 4;
  `window_overlap` defaults to 0.10; `depth_cap` defaults to 3.
- **Paths are validated, not assumed** — every config path is mechanically checked to exist and
  be readable before stage 1 proceeds; dead → stop for the human. Ported from
  `Guarded_change/METHODOLOGY.md:139-144`.
- **What a run produces** — the fenced directory tree given in §5 below, with a one-line gloss
  per entry.
- **Restart and resume** — the completion-terminator rule (§2.6) stated once, here, as the
  normative source; stage files cite it rather than restating it.
- **Human-in-the-loop** — the stop list from §6, plus the delegation rule: under delegation the
  running agent halts and returns the question verbatim rather than self-answering.

**Step 3. Write `stages/common.md`** — read first, verbatim, by *every* dispatched agent.
Contents, and nothing that only one role can act on:
- *"You are a cold, independent agent."* No shared context with whoever produced your input and
  none with the siblings spawned alongside you. Do not try to guess what a sibling will say and
  do not hedge toward an imagined middle — if you converge it must be because the corpus
  determined it, and that convergence is the only evidence the merge has.
- **The corpus is read-only.** You may not create, edit, move, delete or rename anything under
  the config's `root` paths. The **only** path you may write is the single output path your
  caller named. State plainly that this is a prose constraint, not a sandbox.
- **Off-limits paths.** The caller passes an explicit list; you may not read, list, grep or cite
  anything matching it, and a finding whose locus is off-limits is dropped, not reported.
- **The finding record schema** — the one canonical definition, quoted by every role:
  ```
  F<k> | claim:  <one sentence, decidable true/false by reading the locus alone>
       | locus:  <path>:<line-range>   (or <path>#<byte-offset-range> for non-line data)
       | quote:  "<= 25 words copied verbatim from the locus"
       | item:   <item-id>
  ```
- **Facts, not interpretation** — the decidable-at-the-locus test from §2.5, stated in full, with
  two worked examples: admissible (*"The config at line 14 sets `retries: 0`"*) and inadmissible
  (*"Retries were disabled because the team distrusted the queue"* — the motive is not decidable
  from the locus). Plus: where the source itself interprets, quote the interpretation and phrase
  the claim as *what the source says*.
- **Cite or it doesn't count**, and **flag what you could not check** rather than accepting it
  silently — both ported from `Architect/stages/common.md:58-62` and
  `Guarded_change/stages/charter.md:51-54`.
- **Your output**: write it to the path your caller named and return only the fixed-field status
  line (schema quoted from §2.3). **Nothing else you say is read** — anything the run must keep
  goes in the file. Ported from `Architect/stages/common.md:64-67`.
- **Truncation is reported, never silent.** If your assigned material does not fit in your
  context, say so in your output file, name the byte range you actually read, and set your status
  to `partial`. A silent partial read is the one failure nothing downstream can detect.

**Step 4. Write `stages/analyst.md`** — the analyst role, additions only:
- *You are one of N analysts on this item, spawned cold and independent. The other N−1 exist and
  you will never see their output. Do not moderate a finding because you imagine a sibling
  disagreeing; the merge measures agreement, and it can only measure it if you were not trying to
  produce it.*
- Inputs: one item locator, the extraction brief (`question.brief` + its in-scope/out-of-scope
  examples, verbatim from the config), the off-limits list, one output path.
- Procedure: read the item whole; extract every finding matching the brief; write each as a
  finding record per the common schema; **quote before you claim** — copy the quote out of the
  source first, then write the claim to fit the quote, never the reverse.
- **Exhaustiveness over selectivity.** Do not rank, prioritise or summarise; a finding you omit
  because it looked minor is a finding the merge can never recover. Verification and merge do the
  filtering downstream.
- **Do not read other items.** Your locus must lie inside your assigned item. A cross-item claim
  is out of scope by construction and belongs to no analyst.
- Output file layout: a header block (`item`, `analyst index`, `bytes read`, `brief hash`), then
  the finding records, then `STATUS: complete` as the final line.
- Return value: the status line only.

**Step 5. Write `stages/verifier.md`** — the verification role, additions only:
- *You did not write these findings and you are not their author's colleague. Your job is to try
  to break each one.*
- Inputs: one analyst output file, the corpus paths its loci point into, the off-limits list, one
  output path. **You are not told N, and you are not told what any other analyst found** — so you
  cannot spare a finding for being popular.
- Per finding, run four checks in order and stop at the first failure:
  1. **Locus resolves** — the path exists, is readable, is not off-limits, and the line/byte range
     is within the file. Fail → `locus-missing`.
  2. **Quote is verbatim** — the quoted text appears at that locus, comparing after normalising
     whitespace only. Fail → `misquoted`.
  3. **Claim is decidable from the locus alone** — per the common file's test. Fail →
     `interpretation`.
  4. **Claim is true of the locus.** Fail → `false`.
- Verdicts: only findings passing all four go to the `## Verified` section. Everything else goes
  to a `## Dropped` section **with its verdict and a one-line reason** — drops are auditable, never
  silent.
- **Earned clean.** For every finding you mark verified you must record the source text you
  actually read at that locus. A verified verdict with no such evidence is treated as un-run and
  is re-run. Ported in substance from the sibling charter's clean-factual-lens rule
  (`Guarded_change/stages/charter.md:42-46`).
- **You add no findings of your own.** If you notice an unreported fact, ignore it; adding it
  would make you an analyst whose work no one verifies.
- Output layout: header, `## Verified`, `## Dropped`, then `STATUS: complete`.

**Step 6. Write `stages/merger.md`** — the merge role, additions only:
- Inputs: all N verified files for **one** item, one output path. You dispatch nothing.
- **Clustering rule:** two findings belong to the same cluster when they assert the same claim
  about **overlapping loci in the same file**. Same claim, disjoint loci → two clusters. Different
  claims at the same locus → two clusters. State the judgement you made for any borderline pair in
  a `## Clustering notes` section.
- **Agreement count = the number of *distinct analysts* contributing at least one finding to the
  cluster**, never the number of findings (one analyst reporting a fact three times is agreement
  of 1). Record it as `agreement: k/N`.
- **Ranking:** by agreement count descending; ties broken by locus order (path, then offset) so
  the output is deterministic and diffable across runs.
- **Singletons are kept, labelled `singleton`, and ranked last — not dropped.** N independent
  agents were used so that agreement would be *informative*; a fact only one analyst happened to
  reach is still a verified, cited fact, and dropping it would convert the design into a
  popularity filter.
- **Agreement is a count, not a confidence.** Never restate `agreement: 3/3` as "confirmed",
  "certain" or "high confidence" — the analysts share a prompt, so agreement partly measures the
  brief. Report the number and let the reader weigh it.
- Output layout: header, ranked cluster list (each cluster showing the merged claim, the canonical
  locus + quote, `agreement: k/N`, and the contributing analyst indices), `## Clustering notes`,
  then `STATUS: complete`.

**Step 7. Write `stages/node.md`** — the coordinating role, additions only:
- **You are blind by design, and this is the point.** You will never read a finding, a verified
  file or a merged file. You read `status.md` and the manifest, and nothing else under
  `items/`. If you find yourself wanting to read a child's output to decide what to do next,
  that wanting is the bias the design exists to remove — the answer is always to dispatch
  another agent, never to look.
- What you may read: the manifest rows for your children; `status.md`; the config. What you may
  write: `status.md` (append-only), `decisions.md` (append-only), your own `nodes/<id>/rolled.md`
  **assembled by concatenating child merged-file *paths and counts*, not their content**.
- **Dispatch discipline:** never place any finding text, claim, quote or locus into a child's
  prompt. A child's prompt contains: its item locator, the brief, the off-limits list, its output
  path, and nothing derived from a sibling's result.
- **Concurrency ceiling:** dispatch at most `analysts.max_concurrent_agents` agents at one time,
  batching the rest; launch a batch as a single set of concurrent spawns and wait for the batch
  before starting the next.
- **Resume:** before dispatching for any unit, check that unit's expected output file; if it
  exists and its last line is `STATUS: complete`, skip it and log `resumed-skip` to
  `decisions.md`. Otherwise delete any partial file and dispatch.
- **Failure handling:** a child returning `failed` is retried once; a second failure is recorded
  in `status.md` as `failed` and the item is named in the final report as not analysed. **A failed
  item is never silently dropped.**

**Step 8. Write `stages/stage-0.md` — Intake.**
*What it does:* resolve and validate the Layer-2 config and the corpus before any agent is spawned.
*Procedure:* locate `data-distiller.*.{md,yaml}` in or near the working directory; if absent, stop
and ask the human — do not invent corpus specifics. Parse the YAML block. Mechanically check every
`root` path exists and is readable, and resolve it through symlinks to a real path. Resolve every
`off_limits` glob and record what it currently matches. Check `analysts.n >= 2`; check
`question.brief` is non-empty; apply the documented defaults for every omitted optional key and
record which defaults were applied. Create `<output.dir>/` and write `0-intake.md` recording the
resolved config, the path-validation result, the off-limits match list, and the applied defaults.
Append the intake line to `decisions.md`.
*Rules:* **Refuse to invent corpus specifics** (`Guarded_change/SKILL.md:18`,
`Dragonfly/SKILL.md:20`). **Paths are validated, not assumed** — dead root path → stop for the
human; a root path that resolves *outside* the declared root after symlink resolution → stop, since
that is how an off-limits region leaks in. **Intake must complete before stage 1** so that no agent
is ever spawned against an unvalidated path.

**Step 9. Write `stages/stage-1.md` — Decompose.**
*What it does:* turn the corpus into an enumerated list of candidate analyzable items.
*Procedure:* run the config's `item_rule.enumerate` command or glob to produce one locator per
line. Drop every locator matching `off_limits`, recording each drop with the pattern that matched
it. For each surviving locator, measure size in bytes. Write `manifest.md` as an append-only table:
`| item-id | locator | bytes | est_tokens | tier | parent | status |`, with `tier` and `parent`
blank until stage 2. Item ids are assigned in enumeration order and never reused.
*Rules:* **What an analyzable item is comes from the config, never from the method** — this is the
single most corpus-specific decision and inventing it silently produces a plausible, wrong run.
**Enumeration is recorded before anything is analysed**, so that "was this item ever looked at?" is
answerable from disk. **An empty enumeration is a stop, not a clean run** — it almost always means
the item rule does not match the corpus layout.

**Step 10. Write `stages/stage-2.md` — Size and tier.**
*What it does:* assign each item a strategy, creating the item tree that the roll-up later climbs.
*Procedure:* `est_tokens = bytes / bytes_per_token`. Assign a tier:
- **T1 fit** — `est_tokens <= context_budget_tokens`: a leaf; analysts read it whole.
- **T2 split** — over budget and `item_rule.split_rule` applies (record boundaries: per JSON line,
  per transcript turn, per day, per section heading): split into child items each within budget,
  mark the parent a **node**, and re-run this stage on the children.
- **T3 window** — over budget and no record boundary applies: cut fixed windows of
  `context_budget_tokens` with `window_overlap` fractional overlap; each window is a leaf child;
  the parent is a node. The overlap exists so a fact straddling a cut is seen whole by at least one
  window; duplicates from overlap are removed at merge by locus.
- **T4 unanalyzable** — a single indivisible unit over budget (a binary blob, one enormous
  unbreakable line): mark `skipped: unanalyzable`, and **name it in the final report**.
Write tier, parent and any children back into `manifest.md`.
*Rules:* **Depth cap** — if splitting would exceed `depth_cap` levels, stop splitting and window
the item flat at that level; unbounded recursion on a pathological corpus is the failure this
prevents. **Every item ends in exactly one of the four tiers** — an item with no tier is a
decomposition bug, not an item to skip. **Skipping is always named, never silent** (P1's real
content: the *strategy choice* must be recorded per item, so a reader can see which items got which
treatment).

**Step 11. Write `stages/stage-3.md` — Analyze.**
*What it does:* fan out N independent cold analysts per leaf item.
*Procedure:* for each leaf item in manifest order, and honouring the concurrency ceiling, spawn
`analysts.n` agents, each given: `stages/common.md` + `stages/analyst.md` verbatim, its item
locator, the brief verbatim, the off-limits list, and its output path
`items/<item-id>/analyst-<k>.md`. Append each returned status line to `status.md`. Skip any unit
whose output file already ends `STATUS: complete`.
*Rules:* **The N analysts get identical prompts and no knowledge of one another** — differing
prompts would make the agreement count meaningless. **The dispatcher is a node and therefore reads
no analyst output** (cite `stages/node.md`). **`n >= 2`**, restated here because this is the stage
where it bites. **All N failing on one item is a stop-for-human**, since it usually means the item
locator or the brief is wrong rather than that the item is empty.

**Step 12. Write `stages/stage-4.md` — Verify.**
*What it does:* re-check every citation with a cold agent that did not write it, and drop what does
not survive.
*Procedure:* for each `items/<id>/analyst-<k>.md`, spawn one verifier with `common.md` +
`verifier.md`, that one analyst file, the corpus paths, and output `items/<id>/verified-<k>.md`.
Honour the ceiling; skip completed units.
*Rules:* **One verifier per analyst file, not one per item** — a verifier handed all N files could
infer agreement and would be biased by it. **The verifier never sees N.** **Verification precedes
merge** (§2.4, stated here as the operative rule). **Drops are recorded with reasons.** **A drop
rate above `drop_alarm` (default 0.5) on any item is surfaced to the human**, because that
signature means a bad brief or a fabricating analyst, not a difficult item.

**Step 13. Write `stages/stage-5.md` — Merge.**
*What it does:* cluster the surviving findings for one item and rank them by independent agreement.
*Procedure:* for each leaf item, spawn one merger with `common.md` + `merger.md` and all N
`verified-<k>.md` files for that item; output `items/<id>/merged.md`. Append its status line.
*Rules:* **Agreement counts distinct analysts, not findings.** **Singletons are kept and labelled.**
**Agreement is a count, not a confidence** — the phrase is repeated here because this is the stage
whose output invites the mistranslation. **Ranking is deterministic** (agreement desc, then locus)
so two runs over an unchanged corpus produce diffable output.

**Step 14. Write `stages/stage-6.md` — Blind roll-up.**
*What it does:* climb the item tree from leaves to root without any coordinating agent reading a
finding.
*Procedure:* for each node whose children are all `complete`, spawn a merger over the children's
`merged.md` (or `rolled.md`) files, writing `nodes/<node-id>/rolled.md`; the node that dispatched
it reads only the returned status line. Repeat until the root node is rolled. Re-cluster at each
level so that a fact appearing in several children is counted once with its agreement summed over
distinct analysts, **de-duplicated by analyst identity** — the same analyst seeing a fact in two
overlapping T3 windows contributes 1, not 2.
*Rules:* **The blindness invariant, restated in full**: no agent both dispatches children and reads
findings; the node's only channel is the fixed-field status line, which has no free-text field.
**Overlap de-duplication is by (analyst, claim, locus-overlap)**, otherwise T3's overlap inflates
every straddling fact's agreement count — a silent, systematic bias toward facts that happen to sit
near a window boundary. **A node with a `failed` child rolls up anyway and records the gap**, rather
than blocking the whole corpus on one item.

**Step 15. Write `stages/stage-7.md` — Report.**
*What it does:* emit the corpus-level result and the run's honest coverage statement.
*Procedure:* write `findings.md` containing: a header (corpus, config file, date, N, item count,
analyst-agent count); the ranked findings from the root `rolled.md`, each with claim, locus, quote
and `agreement: k/N`; then three mandatory sections — **`## Not analysed`** (every T4, every
`failed`, every off-limits exclusion, each with its reason), **`## Partial`** (every unit whose
status was `partial`, with the byte range actually read), and **`## Dropped in verification`**
(counts by verdict class, per item). Append the final line to `decisions.md`.
*Rules:* **Coverage is reported, not implied.** A findings file that does not say what it failed to
look at reads as exhaustive and is the most dangerous artifact this skill can produce. **No new
claims at report time** — stage 7 assembles, it does not analyse; anything not traceable to a
merged cluster may not appear. **Facts, not interpretation, one last time**: the report contains no
"conclusions" section, because synthesising across findings is exactly the interpretation the
method excludes.

**Step 16. Write `SKILL.md`** — the router, ~80 lines, matching the sibling structure:
- YAML frontmatter with exactly two keys: `name: data-distiller`, and a `description` that states
  what it is, when to use it, that corpus specifics come from a per-corpus config, and a proactive
  suggestion clause — following the sibling pattern at `Dragonfly/SKILL.md:3`.
- A title and a two-sentence purpose statement, then: *"This file is the **router**: each stage's
  full procedure + the rules that govern it live in `stages/`. `METHODOLOGY.md` is the
  orientation/reference spec."*
- **Inputs** — the distillation request; the Layer-2 per-corpus config, with the discovery pattern
  and the refusal to invent; the path-validation requirement.
- **Pipeline** — the stage table: `| # | Stage — one-line purpose | Read |` with eight rows
  pointing at `stages/stage-0.md` … `stages/stage-7.md`, plus a line naming the role files every
  dispatched agent reads (`stages/common.md` first, then its role file).
- **The three invariants**, stated once here and pointing at their operative homes: blindness
  (`stages/node.md`), verify-before-merge (`stages/stage-4.md`), facts-not-interpretation
  (`stages/common.md`).
- **Stop-for-human** — the list from §6.
- **Self-check / dogfooding** — these files are position-sensitive prompts; non-trivial edits take
  the full guarded-change loop; standing criteria are live copy == source copy (`diff`), and
  SKILL ↔ METHODOLOGY ↔ stage-file consistency on every rule stated in more than one place.
  Modelled on `Guarded_change/SKILL.md:75-85`.

**Step 17. Write `data-distiller.example.md`** — the Layer-2 config template and worked example.
A fenced YAML block with every key, each carrying an inline comment giving its meaning and default,
followed by a `## Notes specific to this corpus` prose section — the shape of
`Guarded_change/guarded-change.companion.md:1-123`. The YAML:
```yaml
corpus: <name>

root:
  - path: <dir or file>
    note: <what this contains; PRIORITY ORDER, most relevant first>

item_rule:                     # MANDATORY — the core corpus-specific decision
  description: <prose: what one analyzable item is>
  enumerate: <command or glob emitting one locator per line>
  split_rule: <how to split an oversized item, or "none">

off_limits:                    # never read, listed, grepped or cited
  - pattern: <glob>
    why: <reason>

analysts:
  n: 3                         # MUST be >= 2
  max_concurrent_agents: 4     # concurrency ceiling
  context_budget_tokens: 120000
  bytes_per_token: 4
  window_overlap: 0.10
  depth_cap: 3
  drop_alarm: 0.5

question:                      # MANDATORY — without it "facts" is unbounded
  brief: <what counts as a finding for this corpus>
  in_scope_example: <one admissible finding>
  out_of_scope_example: <one interpretation that must be refused>

output:
  dir: "distills/<slug>/"
```

**Step 18. Write `README.md`** — repo-facing, not installed. Sections: what the skill is in three
sentences; the pipeline in eight bullets; the three invariants; **Install** (copy `SKILL.md`,
`METHODOLOGY.md` and `stages/` to `~/.claude/skills/data-distiller/`; the README, the example
config and any run output are *not* installed — verified against
`diff -rq ~/.claude/skills/guarded-change/ Guarded_change/`); **Configure** (copy
`data-distiller.example.md`, adjust, keep it with the corpus); **Invoke**; and a short "what this
does not do" (it does not interpret, conclude, or recommend).

**Step 19. Write and run `check.sh`** — the mechanical consistency check, kept in the repo:
- every file named in `SKILL.md`'s stage table and in `METHODOLOGY.md`'s stage index exists;
- every relative path mentioned in any `.md` under the skill root resolves;
- `SKILL.md`'s frontmatter parses as YAML and contains `name: data-distiller`;
- no file under `stages/` is empty;
- **no sentence longer than 8 words appears both in `stages/common.md` and in a role file** — the
  mechanical proxy for "role files add and never restate a common rule";
- **no role file grants both dispatch and finding-read**: grep asserts `node.md` contains no
  permission to read `items/*/`, and that `analyst.md`/`verifier.md`/`merger.md` contain no
  spawn/dispatch permission.
Run it and fix what it reports.

**Step 20. Install.** Copy `SKILL.md`, `METHODOLOGY.md` and `stages/` into
`~/.claude/skills/data-distiller/`, then run `diff -r` between the installed tree and the source
subset and confirm it is empty. *Note:* `~/.claude/skills/data-distiller/` already exists on this
machine; installing over it is a destructive act on someone else's artifact and must be confirmed
with the human first, or installed under a distinct name for testing.

**Step 21. Assembled end-to-end acceptance run.** Invoke the installed skill against one real
corpus that does not fit in one context window, with a hand-written Layer-2 config. Accept only if
`findings.md` exists, every finding carries a resolvable locus, a quote and an `agreement: k/N`,
and the three coverage sections are present. Then **spot-check five randomly chosen findings** by
opening their loci and confirming the quote is verbatim and the claim true. Any failure: fix the
first link in the chain that broke and re-run — do not build a test harness around the failure.

**Step 22. Resume test.** Re-run step 21's distillation, interrupting it during stage 3. Confirm:
partial analyst files lack `STATUS: complete`; on re-invocation, units with the terminator are
skipped (their mtimes are unchanged) and the interrupted unit is re-run; the completed run's
`findings.md` matches the uninterrupted run's on the items both covered.

**Step 23. Blindness test.** From the completed run, check that no dispatching agent's prompt or
transcript contains finding text: grep the run's `status.md` for any line not matching the
fixed-field schema, and grep the node-level artifacts for any occurrence of a `quote:` string
drawn from `findings.md`. Zero hits is the pass; any hit is a blocker against `stages/node.md`.

## 5. Outputs & artifacts, with their locations

**The skill source** (repo, git-tracked), at
`/home/zero/Desktop/claude-code-skills/Data-Distiller-impl/` (see step 1's naming note):

```
Data-Distiller-impl/
  SKILL.md                     router + YAML frontmatter (name, description)   [installed]
  METHODOLOGY.md               orientation/reference spec + config contract    [installed]
  README.md                    repo-facing doc                            [NOT installed]
  data-distiller.example.md    Layer-2 config template + worked example    [NOT installed]
  check.sh                     mechanical consistency check               [NOT installed]
  stages/                                                                      [installed]
    common.md                  read verbatim first by EVERY dispatched agent
    analyst.md                 role: N independent cold analysts
    verifier.md                role: cold citation re-checker
    merger.md                  role: cluster + agreement rank
    node.md                    role: blind coordinator
    stage-0.md                 intake: config + path validation
    stage-1.md                 decompose: enumerate analyzable items
    stage-2.md                 size + tier: fit / split / window / unanalyzable
    stage-3.md                 analyze: N cold analysts per leaf item
    stage-4.md                 verify: re-check every citation, drop the unverifiable
    stage-5.md                 merge: cluster + rank by independent agreement
    stage-6.md                 roll-up: blind, leaves to root
    stage-7.md                 report: findings + coverage statement
```

**The installed skill**, at `~/.claude/skills/data-distiller/` — exactly `SKILL.md`,
`METHODOLOGY.md`, `stages/`.

**What a *run* of the skill produces**, under the config's `output.dir` (default
`distills/<slug>/`, relative to the corpus's working directory — never inside the corpus itself):

```
distills/<slug>/
  0-intake.md                resolved config, path-validation result, off-limits matches, defaults
  manifest.md                append-only: item-id | locator | bytes | est_tokens | tier | parent | status
  status.md                  append-only fixed-field status lines — the ONLY node-readable channel
  decisions.md               append-only: stops, overrides, retries, resume-skips
  items/<item-id>/
    analyst-1.md … analyst-N.md    per-analyst findings, each ending STATUS: complete
    verified-1.md … verified-N.md  per-analyst verified + dropped, with reasons
    merged.md                      clustered + agreement-ranked for this item
  nodes/<node-id>/rolled.md   rolled-up clusters for a subtree
  findings.md                 THE deliverable: ranked cited facts + Not analysed / Partial / Dropped
```

**This plan itself**, at
`/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c/Architect/runs/data-distiller/0/leaf-2-0.md`.

## 6. Failure modes & contingencies

**F1 — The occupied directory name.** `Data-Distiller/` exists and is off-limits to this run, so
step 1 cannot use the canonical name. *Assumption:* the executor may create a differently-named
sibling directory. *If it fails* (the run is required to produce `Data-Distiller/` itself): stop
and ask the human whether the existing directory is to be replaced. **This is a stop, not a
judgement call** — overwriting a finished implementation is destructive.

**F2 — Agreement measures the prompt, not the corpus.** The N analysts share one brief, so a
leading brief produces unanimous agreement on an artefact of the brief. *Contingency:* agreement is
always reported as a bare count and never as confidence (steps 6, 13); singletons are retained
(step 6); and the brief itself is recorded in `0-intake.md` so a reader can see what was asked.
*Residual risk, unmitigated:* nothing in the method detects a systematically biased brief. Fixing
that would need a second brief and a comparison run — deliberately out of scope, and named here so
it is not mistaken for covered.

**F3 — A citation that resolves but does not say what is claimed.** The cheapest fabrication is a
real file and line with an invented claim. *Contingency:* the verifier's check 2 compares the quote
verbatim at the locus, and check 4 tests the claim against it — path existence alone is never
sufficient (step 5).

**F4 — The verifier rubber-stamps.** The verifier is itself an AI and can emit "verified" without
looking. *Contingency:* the earned-clean rule — a verified verdict must record the source text
actually read, and one lacking it is treated as un-run (step 5), ported from
`Guarded_change/stages/charter.md:42-46`. *Residual:* an agent that fabricates the recorded source
text defeats this; the assembled acceptance run's five-citation spot-check (step 21) is the only
backstop, and it is a sample, not a proof.

**F5 — Blindness erodes into a suggestion.** A node "just checks" one child's output to decide what
to do next. *Contingency:* the invariant is structural (no role file grants both dispatch and
finding-read), the status line has no free-text field, and `check.sh` greps for the violation
(step 19), with the runtime check at step 23.

**F6 — T3 window overlap inflates agreement.** A fact straddling a window cut is seen by one
analyst twice and would count as agreement 2. *Contingency:* roll-up de-duplicates by
(analyst, claim, locus-overlap) before summing (step 14). *If that de-duplication is wrong*, the
bias is systematic and favours facts near boundaries — which is why step 21's spot-check should
deliberately include a boundary-adjacent finding.

**F7 — Off-limits leaks through a symlink or a greedy enumerate command.** `item_rule.enumerate` is
corpus-authored and could glob outside `root`. *Contingency:* stage 0 resolves symlinks to real
paths and stops if a root resolves outside itself; stage 1 filters the enumeration against
`off_limits` **after** enumeration and records every drop. *Assumption:* `off_limits` is expressed
as path globs. *If the corpus needs content-based exclusion* (e.g. "any record containing a
credential"), this design does not cover it — name it and stop.

**F8 — Resume re-runs completed work, or accepts truncated work.** *Assumption:* a file whose last
line is `STATUS: complete` was fully written. *How it fails:* an agent that writes the terminator
early, or a filesystem that reorders writes. *Contingency:* the terminator is specified as the
final line of the file in every role file; step 22 tests the interrupt case empirically. *If it
proves unreliable*, fall back to write-to-`.partial`-then-rename, which is atomic on POSIX.

**F9 — Concurrency ceiling ignored.** Dispatching N × item-count agents at once causes rate
limiting or resource exhaustion, and failures then look like analysis failures. *Contingency:*
batching is a node rule (step 7); a `failed` status is retried once before being recorded (step 7),
so a transient throttle does not become a permanent coverage gap.

**F10 — Empty or mismatched enumeration.** The item rule does not match the corpus layout and
stage 1 yields zero items — which would otherwise produce a clean, empty, wrong run. *Contingency:*
an empty enumeration is a stop, not a clean run (step 9).

**F11 — The measurement-apparatus trap.** The characteristic failure of this repo's prior runs is
effort migrating into a test harness for agent behaviour until nothing ships. *Contingency:* the
hard rule in §2.7 — count *rebuilds of a test mechanism*, and at three, stop building it and move
the check into the assembled end-to-end run (steps 21–23 are that run). This is a contingency on
the *build process*, not on the artifact, and it is stated because it is the failure most likely to
consume this work.

**F12 — Skill loader rejects the frontmatter.** *Assumption (unverified):* `name` + `description`
is the whole required frontmatter contract, inferred from two examples. *If the skill does not
appear after install*, compare the frontmatter byte-for-byte against a working sibling's before
changing anything else.

**Stop-for-human points** (these belong in `SKILL.md` and `METHODOLOGY.md`): config missing or
`item_rule` absent; any `root` path dead or resolving outside itself; `analysts.n < 2`;
`question.brief` empty; stage-1 enumeration empty; all N analysts failing on one item; an item's
verification drop rate above `drop_alarm`; and step 20's overwrite of an existing installed skill.
Under delegation the running agent **halts and returns the question verbatim** rather than
self-answering.

## 7. Verification

**Structural (mechanical, from `check.sh`, step 19).**
1. All 18 files in §5's source tree exist and are non-empty.
2. `SKILL.md` frontmatter parses as YAML and contains `name: data-distiller` and a non-empty
   `description`.
3. Every relative path referenced anywhere in the skill's markdown resolves to an existing file.
4. `SKILL.md`'s stage table and `METHODOLOGY.md`'s stage index list the same eight stage files.
5. No sentence of more than 8 words is shared between `stages/common.md` and any role file
   (the "additions only, never restate" proxy).
6. No role file grants both dispatch and finding-read (the blindness invariant, statically).
7. `diff -r` between `~/.claude/skills/data-distiller/` and the installed subset of the source is
   empty (live == source, the standing self-check criterion both siblings carry,
   `Guarded_change/SKILL.md:81-83`).

**Coverage against the task (by inspection, one row per defining property).** Each of P1–P8 in §1's
table is confirmed present in the named file, and the confirmation names the *rule text* that
carries it, not merely the file. A property present only as a sentence in `METHODOLOGY.md` and
absent from the stage file that would enforce it counts as **not implemented** — the reference spec
is read for orientation, not to run a stage (`Guarded_change/METHODOLOGY.md:10-11`).

**Behavioural (the assembled end-to-end run, steps 21–23) — this is the real bar.**
8. On a real corpus exceeding one context window, the run completes and produces `findings.md`.
9. Every finding in `findings.md` carries a locus, a verbatim quote, and `agreement: k/N`.
10. Five randomly selected findings — at least one adjacent to a T3 window boundary if any T3 items
    exist — have loci that resolve, quotes that match verbatim, and claims true of the locus.
11. `findings.md` contains all three coverage sections (`Not analysed`, `Partial`,
    `Dropped in verification`), and every T4 / failed / off-limits item from `manifest.md` appears
    in one of them. **Nothing is silently absent.**
12. At least one finding was dropped in verification with a recorded reason — if zero were dropped
    across the whole run, the verification pass is unproven, not clean, and must be shown able to
    fail on a deliberately corrupted analyst file (a citation pointing at a non-existent line).
13. **Resume:** an interrupted run, re-invoked, skips every unit whose file ends `STATUS: complete`
    (mtimes unchanged) and re-runs the interrupted one; the result matches the uninterrupted run on
    the items both covered.
14. **Blindness:** no line in `status.md` deviates from the fixed-field schema, and no quote string
    from `findings.md` appears in any node-level artifact or dispatch prompt.
15. **Corpus-agnosticism:** the same installed skill runs against a *second*, structurally different
    corpus with only a new Layer-2 config and **zero edits to any file under
    `~/.claude/skills/data-distiller/`**. This is the operative test of P6, and it is the one
    criterion no amount of document inspection can substitute for.

**What "done" is not.** Done is not "the files exist and read well." Criteria 8–15 are gating;
1–7 are necessary but not sufficient, and a run that passes only 1–7 has produced a plausible
document set, not a working method.
