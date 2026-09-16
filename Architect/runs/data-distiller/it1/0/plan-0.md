# Plan — implement the Data-Distiller skill

*Consensus merge of three independently written leaf plans. Not authored: nothing below was
written, improved, or adjudicated by the combiner. Every element is present because **two of the
three** leaves stated it and placed it at the same point in the sequence; elements only one leaf
stated were discarded. The merge record — inputs received, the ordering rule as applied, and what
was discarded — is §8.*

**Inputs received: 3 of 3 expected.** `leaf-1-0.md`, `leaf-2-0.md`, `leaf-3-0.md`.

---

## 1. Problem / intent

**What this node plans.** The whole assigned task: implementing `data-distiller` as a Claude Code
skill — a directory of markdown prompt files, invokable by name, installable at
`~/.claude/skills/data-distiller/`. There is no sibling slice; this plan owns the entire
deliverable end to end. *(3 of 3.)*

**Why it is a skill of prompt files and not code.** Every defining property of the method is a
constraint on an agent the skill *dispatches* — coldness, independence, read-only access, citation,
blindness. None is enforceable by code; each is enforceable only by the text handed to the
dispatched agent. The deliverable is therefore a set of markdown files whose *text* is the
mechanism. *(2 of 3.)*

**The nine defining properties, each of which must land in a named file** *(2 of 3 — the third leaf
folded P1 and P2 into one property, otherwise identical)*:

| # | Property | Where this plan puts it |
|---|---|---|
| P1 | Decompose the corpus into analyzable items | `stages/stage-1.md` |
| P2 | Size each item; pick a per-item strategy when it does not fit | `stages/stage-2.md` |
| P3 | N independent cold analysts per item, read-only, citing every finding | `stages/stage-3.md` + `stages/analyst.md` |
| P4 | Cold verification re-checking every citation; drop the unverifiable | `stages/stage-4.md` + `stages/verifier.md` |
| P5 | Merge ranking survivors by independent-analyst agreement | `stages/stage-5.md` + `stages/merger.md` |
| P6 | Blind roll-up — the coordinator reads only terse per-child status | `stages/stage-6.md` + `stages/node.md` |
| P7 | Per-corpus Layer-2 config supplies corpus specifics; the core stays agnostic | `METHODOLOGY.md` config contract + the worked config |
| P8 | Restart and resume from on-disk state | `stages/stage-0.md` resume scan + per-item status |
| P9 | Facts, not interpretation | `stages/common.md` finding schema + the single-locus test |

---

## 2. Approach

### 2.1 Copy the sibling house shape

Both working siblings (`Guarded_change/`, `Dragonfly/`) are the same artifact with different
content, and Data-Distiller adopts that shape unchanged *(3 of 3)*:

- **`SKILL.md`** — YAML frontmatter with exactly two keys, `name` and `description`
  (`Guarded_change/SKILL.md:1-4`, `Dragonfly/SKILL.md:1-4`), then a **router**: purpose, `## Inputs`,
  a stage table whose every row points at a file under `stages/`, a most-important-gate paragraph,
  `## Stop-for-human`, `## Self-check / dogfooding`.
- **`METHODOLOGY.md`** — the orientation/reference spec, explicitly *"opened for orientation and
  config setup — not to run a stage"* (`Guarded_change/METHODOLOGY.md:10-11`).
- **`stages/*.md`** — one file per stage, each opening with a one-line *what this stage does*, then
  a procedure section, then the rules governing that stage.
- **A per-corpus Layer-2 config**, `data-distiller.<corpus>.md`, in the repo: one fenced YAML block
  plus a "Notes specific to this corpus" prose section.
- **`README.md`** — human-facing, repo-only.

**Install is a copy of a subset, measured rather than assumed** *(3 of 3)*. `diff` of the live
installs against source shows `~/.claude/skills/{guarded-change,dragonfly}/` contain exactly
`SKILL.md`, `METHODOLOGY.md`, `stages/` — no `README.md`, no `<skill>.<project>.md` config, no run
folders. Install is a copy, not a symlink, which is why both siblings carry the standing self-check
criterion *live copy == source copy (`diff`)* (`Guarded_change/SKILL.md:82-83`,
`Dragonfly/SKILL.md:88`). The install directory name must equal the frontmatter `name`, so
`Data-Distiller/` → `~/.claude/skills/data-distiller/` → `name: data-distiller`.

**The rule governing where a rule goes** *(2 of 3)*: orientation in `METHODOLOGY.md`, the
**operative** form written in full in the stage or role file that enforces it. A rule stated only in
`METHODOLOGY.md` is a rule in a file the acting agent was told not to open, and counts as not
implemented (§7).

### 2.2 Split the dispatched-agent prompts by role, inside `stages/`

Data-Distiller dispatches **four** kinds of agent — analyst, verifier, merger, node. Both siblings
dispatch essentially one (a cold reviewer) and so get away with a single shared
`stages/charter.md`. A single charter here would hand every agent the other three's instructions
and — the worse failure — would hand the **blind node** the analyst's and merger's
findings-handling text, which is the precise contamination P6 exists to prevent. *(3 of 3; the
single-charter alternative was considered and rejected by all three leaves.)*

So: **`stages/common.md`, included verbatim in every role dispatch, plus one file per role, additions
only, never restating a common rule.** A role file that needs to *modify* a common rule is the
signal the rule was never common and must move down into the roles. This matches the live practice
of the Architect skill in this same repo (`Architect/stages/common.md:3-4` plus one file per role).
Role files live in `stages/` alongside the stage files, which is where Architect puts them. *(2 of 3
— one leaf proposed a separate `agents/` directory and flagged it itself as a divergence.)*

### 2.3 The pipeline

```
0  PREFLIGHT   load + validate the Layer-2 config; resume scan
1  DECOMPOSE   enumerate the corpus into items with stable ids   → manifest
2  SIZE/TIER   measure each item; leaf / split / chunk-with-overlap
3  ANALYZE     per item: N independent cold analysts, read-only, citation per finding
4  VERIFY      per item: a cold verifier re-opens every citation; drops the unverifiable
5  MERGE       cluster survivors; rank by count of distinct analysts that agreed
6  ROLL UP     nodes read ONLY a fixed-field per-child status record
7  REPORT      assemble the deliverable mechanically, with its coverage statement
```

**Stage 4 is the most important gate** *(2 of 3)*, and the skill says so where the siblings say it
(`Guarded_change/SKILL.md:47-50`, `Dragonfly/SKILL.md:53-56`). It is the cheapest place to kill an
uncited or interpretive finding, before it is merged, ranked, and inherited by the deliverable as
though established. Everything downstream of an unverified citation is a confident fabrication
carrying a file path.

**Verification precedes merge, and the ordering is content, not sequencing convenience** *(3 of 3)*.

### 2.4 Independence is a property of what agents are handed

"Be independent" is not enforceable; three mechanisms are, and each is a stated hard rule in a named
file *(3 of 3)*:

1. **Each analyst is handed the raw item and nothing else** — never another analyst's output, never
   a summary, never the run's state. The N analysts are dispatched **in a single batch with
   identical prompts differing only in output path**, because any prompt difference makes their
   agreement uninterpretable as evidence. Agreement between agents that read each other is not
   evidence.
2. **The verifier does not know who produced a finding, or how many analysts there were** — so it
   cannot weight a finding by its popularity or its author.
3. **A node reads only a fixed-field, content-free per-item status record.** Its ignorance is the
   control: a coordinator that knew what its children were finding would shape the dispatch of the
   remaining children, and their agreement would stop being independent evidence.

**The invariant, stated structurally rather than as a request** *(2 of 3)*:

> **No agent both dispatches children and reads findings.**

`node` dispatches and reads only status records. `analyst`, `verifier` and `merger` read findings
and dispatch nothing. This makes blindness checkable by inspecting the role files — does any file
grant both? — rather than by trusting runtime good behaviour.

### 2.5 "Facts, not interpretation" reduced to a decidable test

An instruction to record facts rather than interpretation is unenforceable as prose. Two mechanisms
make it checkable *(3 of 3)*:

1. **The finding schema** — every finding is `{id, claim, locus, quote}`, with `quote` verbatim from
   the locus. The quote field is what makes P9 mechanical.
2. **The single-locus test, executed by the verifier:** *a finding is admissible only if a reader who
   opens its cited locus alone, and reads nothing else, can confirm or refute the claim as stated.*
   A claim requiring inference across two loci is interpretation — the verifier drops it, or, if it
   is genuinely a two-locus fact, the analyst should have filed two findings. This turns a value
   judgment into a procedure.

### 2.6 State is files, not context

Resume is satisfied by per-item on-disk state read at stage 0: a unit whose expected output exists
and is recorded complete is **skipped, not re-analyzed** *(2 of 3)*. The run is expected to outlive
a session, a compaction, or a crash, and in-context state does not. Tiering decisions are recorded
rather than remembered, so a resume does not re-decide them.

### 2.7 Concurrency

The config's ceiling is applied by the **dispatching** agent as a batch-size cap: no agent has more
than `max_parallel_agents` children live at once, and the rest are batched *(3 of 3)*.

### 2.8 Prove it with one assembled end-to-end run, not a harness

The acceptance evidence is **one real distillation run against a real corpus that does not fit in one
context window**, not a battery of isolated behavioural micro-tests on individual stages *(3 of 3)*.
Agent behaviour is non-deterministic, so an isolation test needs repeated trials and a stated pass
rate to mean anything, and the test mechanism then becomes a second AI artifact that itself needs
reviewing. **Hard rule for this build: count *rebuilds of a test mechanism*, not runs of the test;
past three, stop building it and move that check into the assembled run** *(2 of 3)*. When the run
breaks, fix the first link in the chain that broke and re-run.

---

## 3. Interfaces & seams

**Consumes** *(3 of 3 on all three)*:

1. **The corpus** — read-only, at the path the config's `root` names.
2. **A Layer-2 config file**, `data-distiller.<corpus>.md`, located the way the siblings locate
   theirs — look for `data-distiller.*.{md,yaml}` in or near the working dir
   (`Guarded_change/SKILL.md:16-17`). It supplies what an analyzable item *is* here, what is
   off-limits, the concurrency ceiling, the sizing threshold, N, and the extraction brief. **The
   skill refuses to invent any of these** (`Guarded_change/SKILL.md:18`, `Dragonfly/SKILL.md:20`).
3. **A distillation request** — what the caller wants extracted, narrowing but never overriding the
   config's brief.

**Emits** *(3 of 3)*:

1. **The deliverable** — the ranked, cited finding set, with its coverage statement.
2. **Per-item run state**, resumable.
3. **`decisions.md`** — the append-only gate/override/resume log, mirroring both siblings
   (`Guarded_change/METHODOLOGY.md:174-180`).

**Seams** *(each 2 of 3 or better)*:

| Seam | Contract |
|---|---|
| runner → any dispatched agent | `stages/common.md` verbatim + that role's file verbatim + the run arguments (item locus, brief, off-limits list, output path). This is the only channel — that is what "cold" means operationally. |
| analyst → verifier | The item's findings files, with analyst identity and count withheld. |
| verifier → merger | The item's `verified.md`, every finding carrying its disposition. |
| merger → node | The per-item fixed-field status record **only**. `merged.md` exists but no node may open it. |
| skill → human | The stop-for-human set (§6), surfaced as questions, never self-answered. |
| skill → Claude Code | `SKILL.md` frontmatter `name: data-distiller` must equal the install directory name, or the skill does not resolve. |
| source → install | `~/.claude/skills/data-distiller/` must be byte-identical to the installed subset of source. |

**Seam to the sibling skills: none at runtime** *(3 of 3)*. Data-Distiller neither invokes nor is
invoked by guarded-change or dragonfly; it borrows their shape only. The one relationship is
authorial: **non-trivial edits to Data-Distiller's own files go through guarded-change**, because
these files are position-sensitive prompt assemblies (`Guarded_change/SKILL.md:79-85`,
`Dragonfly/SKILL.md:86-88`).

---

## 4. Steps

**Ordering principle** *(3 of 3)*: the contract is fixed before the prompts that must obey it; the
shared file before the role files; the role files before the stages that dispatch them; the router
after every file its table points at; then the worked config, the README, the install, the
mechanical checks, and the assembled acceptance run last.

**Granularity floor applied as given:** each step is one file created, or one coherent edit to one
file, with the content that goes in it specified. Two places the plan deliberately stops at the
floor: each stage file's **sections and operative rules** are specified but not its sentences, and
the `description` frontmatter's **content** but not its final wording. *(2 of 3.)*

---

**Step 1 — Establish the destination directory without overwriting what is there.**
Target `/home/zero/Desktop/claude-code-skills/Data-Distiller/`. Run `ls -A` on it first. If it is
absent or empty, create it and `Data-Distiller/stages/`, and proceed. **If it is non-empty, do not
write into it on your own judgment** — this plan was written blind to that directory's contents
(§8.3), so the executor is the first party able to see the collision, and resolving it is not the
executor's call. Record whatever is decided in the run's `decisions.md`.

**Step 2 — Write `Data-Distiller/METHODOLOGY.md`**, the orientation/reference spec, opening with
the siblings' disclaimer that it is *opened for orientation and config setup — not to run a stage*.
Sections, in the siblings' order:

- **Why this exists** — the failure modes, each mapped one-to-one to a structural defence:
  (1) *a single reader's priors silently shaping what a large corpus is found to contain* → N
  independent cold analysts; (2) *the confident citation that does not say what it is claimed to
  say* → citation-per-finding plus the cold verify pass; (3) *a coordinator's expectations
  propagating into what its children look for* → the blind roll-up; (4) *silent truncation* — a
  corpus larger than context read partially and reported as if wholly → explicit sizing, tiering,
  and a coverage statement carried to the deliverable; (5) *context loss mid-run* → on-disk state and
  resume; (6) *interpretation smuggled in as fact* → the finding schema plus the single-locus test.
- **The pipeline** — the stage 0–7 ASCII diagram from §2.3.
- **Stage index** — a table, one row per stage file, plus rows for the five role files so a reader
  can find a role prompt from the index. Each row: file, and one line of what it covers.
- **The dispatched roles and the blindness invariant** — the four roles with what each reads, writes
  and may dispatch, and beneath it in bold: *no agent both dispatches children and reads findings.*
- **The two layers** — Layer 1 the corpus-agnostic core (this doc + `SKILL.md` + `stages/`),
  Layer 2 the per-corpus config. Worded parallel to `Guarded_change/METHODOLOGY.md:88-95`.
- **The config contract (Layer 2)** — the YAML block below, plus its rules: the item definition is
  mandatory and never invented; `off_limits` is enforced at enumeration, before any read;
  `analysts_per_item` defaults to **3** if omitted and the run **refuses to start** if no value is
  resolvable; **every config path is validated at run start, never assumed** — dead and
  unresolvable → stop for the human, adaptable → adapt, record and proceed
  (`Dragonfly/METHODOLOGY.md:135-137`); state is files, not context, because resume depends on
  surviving a restart.

  ```yaml
  corpus: <name>

  root: <path to the corpus root>          # read-only for the whole run

  item:                                    # MANDATORY — what ONE analyzable item IS here
    unit: <prose: e.g. "one .jsonl session transcript" | "one source file">
    enumerate: <command or procedure listing item loci, one per line>

  off_limits:                              # never enumerated, read or cited
    - path: <glob>
      reason: <why>

  brief:                                   # MANDATORY — without it "facts" is unbounded
    extract: <what counts as a finding in this corpus>
    out_of_scope: <what is interpretation rather than fact, in THIS corpus>

  sizing:
    fits_threshold: <at or under => leaf; over => split or chunk>
    overlap: <overlap between chunks, required when an item must be chunked>

  concurrency:
    max_parallel_agents: <int>             # ceiling on simultaneously live subagents
    analysts_per_item: 3                   # OPTIONAL — overrides the Layer-1 default of 3

  state:
    dir: <run directory; must survive a session restart>
  ```

- **What a run produces** — the artifact tree from §5.
- **Restart and resume** — stated once here as the normative source; stage files cite it rather than
  restating it.
- **Human-in-the-loop** — the stop-for-human set from §6, plus the delegation rule: under delegation
  the running agent **halts and returns the question verbatim** to its orchestrator rather than
  self-answering (`Guarded_change/METHODOLOGY.md:208-232`).

**Step 3 — Write `Data-Distiller/stages/common.md`** — what **every** dispatched agent is given
verbatim, and nothing any single role needs alone:

- **You are a cold, independent agent.** No shared context with whoever produced your input and none
  with the siblings spawned alongside you. Do not guess what a sibling will say and do not hedge
  toward an imagined middle — if you converge it must be because the corpus determined it, and that
  convergence is the only evidence the merge has.
- **The corpus is read-only.** You may not create, edit, move, rename or delete anything under
  `root`. The only path you may write is the single output path your caller named.
- **The off-limits list is absolute** and is checked **before** a read, not after. You may not read,
  list, grep or cite anything matching it, and a finding whose locus is off-limits is dropped, not
  reported.
- **The finding record schema** — the one canonical definition, quoted by every role:

  ```
  id:    <item-id>.a<k>.<n>
  claim: <one sentence, decidable true or false by reading the locus alone>
  locus: <path>:<line-range>   (or a record locator for non-line data)
  quote: "<verbatim from the locus, <= 25 words>"
  ```

- **Facts, not interpretation** — the single-locus test (§2.5) stated in full, with a worked
  admissible / inadmissible pair (*"the config at line 14 sets `retries: 0`"* is admissible; *"auth
  was unreliable"* or *"retries were disabled because the team distrusted the queue"* is not, because
  no single locus settles it).
- **Cite or it doesn't count**, and **flag what you could not check** as unchecked rather than
  accepting it silently.
- **Your output is a file.** Write it to the path your caller named and return that path plus a short
  summary. **Nothing else you say is read** — anything the run must keep goes in the file.
- **The role-file rule, stated in this file itself:** role files add, never restate or modify. A rule
  needing modification per role was never common and moves down into the roles.

**Step 4 — Write `stages/analyst.md`** (P3). Additions only:

- *You are one of N analysts on this item, spawned cold and in parallel. The others exist and you
  will never see their output — do not seek it, and if you find another analyst's file, do not open
  it.* Do not moderate a finding because you imagine a sibling disagreeing, and **emit findings even
  where you expect the others found the same thing** — suppressing an "obvious" finding destroys the
  agreement signal the merge measures.
- **Inputs:** one item locus, the extraction brief verbatim, the off-limits list, one output path.
- **Read the item whole**, then extract every finding matching the brief, each as a record in the
  common schema. If the item does not fit, say so at the head of your output and state what you
  actually covered — a silent partial read is the one failure nothing downstream can detect.
- **One claim per record.** A record with two claims cannot be verified or agreement-counted; a fact
  needing two loci is two findings.
- **Do not rank, weigh, prioritise or summarise your own findings** — ranking is the merge's job and
  your ranking would contaminate it.
- **Do not read any other item.** Your locus must lie inside your assigned item; a cross-item claim
  is out of scope by construction and belongs to no analyst.

**Step 5 — Write `stages/verifier.md`** (P4). Additions only:

- *You did not write these findings and you are not their author's colleague. Your job is to try to
  break each one.* You are given the findings, the corpus, and the off-limits list — **not the
  analysts' prompts or reasoning, not their identities, and not how many of them there were.**
- **Open every cited locus. Sampling is prohibited** — a sampled pass is an un-run pass.
- Assign exactly one disposition per finding: **`verified`** (locus exists, quote matches, and the
  locus supports the claim), **`misquoted`** (locus exists, quote does not match it), or
  **`unverifiable`** (the locus does not exist or cannot be resolved). A claim the locus does not
  actually support fails even when the quote is accurate — the citation must support the *claim*,
  not merely exist.
- **Apply the single-locus test** as an executable step, not as an exhortation.
- **Only `verified` findings proceed.** Everything else is recorded with its disposition and a
  one-line reason — drops are auditable, never silently deleted.
- **Earned clean.** Your output shows the specific loci you actually opened; a pass that records no
  opened source is treated as **un-run and re-run** (the sibling charter's earned-clean rule,
  `Guarded_change/stages/charter.md:42-46`, `Dragonfly/stages/charter.md:40-43`).
- **You are a filter, not an author.** Do not add findings, do not rewrite a claim, and do not repair
  a bad citation into a good one — a new claim from a verifier has no independence to measure.

**Step 6 — Write `stages/merger.md`** (P5). Additions only:

- **Input:** one item's verified findings, and nothing else. You dispatch nothing.
- **Dedupe within each analyst first**, so one analyst restating itself cannot inflate agreement.
- **Cluster across analysts.** Equivalence is *same claim at the same (or overlapping) locus*. Same
  claim at disjoint loci stays separate, because the agreement being counted is agreement about *the
  corpus*, not about phrasing. When in doubt, keep them separate — a false merge silently inflates
  the one number this method sells.
- **Agreement is the count of distinct analysts in the cluster, never the count of findings.** One
  analyst stating a thing three times is agreement of 1. Record it as `agreement: k/N`.
- **Rank by agreement descending**, with a deterministic secondary key so two runs over an unchanged
  corpus are diffable.
- **`agreement: 1/N` is kept, labelled, and ranked last — never dropped.** N independent agents exist
  so that agreement is *informative*; a single analyst's verified, cited finding is still a verified,
  cited finding, and dropping it converts the design into a popularity filter.
- **Agreement is a count, not a confidence.** Never restate `3/3` as "confirmed" or "high
  confidence" — the analysts share a prompt, so agreement partly measures the brief.
- **Emit `merged.md` and the item's fixed-schema status record, and put no finding content in the
  status record** — a node will read it and must stay blind.

**Step 7 — Write `stages/node.md`** (P6). Additions only:

- **You coordinate; you never read findings.** You may open the manifest and each child's status
  record. You may **not** open any per-analyst findings file, any `verified.md`, or any `merged.md`,
  and you may not ask a child what it found.
- **The reason, stated so it survives the urge to be helpful:** if you knew what the children were
  finding, your dispatch of the remaining children would be shaped by it and their agreement would
  stop being independent evidence. **Your ignorance is the control.** If you find yourself wanting to
  read a child's output to decide what to do next, that wanting is the bias the design exists to
  remove.
- **Dispatch discipline:** never place any finding text, claim, quote or locus into a child's prompt,
  and never cite finding content in your own output — you emit counts and states.
- **Concurrency:** never exceed `max_parallel_agents` live children; batch the rest and wait for a
  batch before starting the next.
- **Resume:** before dispatching any unit, check its expected output; if it is present and recorded
  complete, skip it and log the skip.
- **Failure handling:** a child returning `failed` is retried **once**; a second failure is recorded,
  the unit is marked `failed`, the item proceeds degraded with the analysts it has, and the item is
  **named in the final report**. A failed item is never silently dropped.
- **Assembly is by reference and counts, not summary.**

**Step 8 — Write `stages/stage-0.md` — preflight, validation and resume.**
*What it does:* resolve and validate the Layer-2 config and the corpus before any agent is spawned,
then decide whether this is a new run or a resume.
*Procedure:* locate `data-distiller.*.{md,yaml}` in or near the working dir; **if none exists, stop
and ask — do not invent corpus specifics**. Parse it. **Mechanically validate every path** — `root`,
every `off_limits` glob, the state dir — for existence and readability, and record the result in
`decisions.md`; dead and unresolvable → stop for the human. Resolve `analysts_per_item` (config,
else the default of 3) and the concurrency ceiling, and **refuse to start if neither the config nor
the default yields a value**. Run the resume scan against on-disk per-item state and report how many
units are being skipped. Create the run directory if this is a new run.
*Rules:* an agent handed a dead path silently degrades to reasoning without the source, which is the
founding failure — so **paths are validated, not assumed**, and **preflight completes before stage 1**
so that no agent is ever spawned against an unvalidated path. *State is files, not context* — a
resume must be reconstructible with zero conversation history.

**Step 9 — Write `stages/stage-1.md` — decompose** (P1).
*Procedure:* run the config's `item.enumerate` to list item loci. **Drop every locus matching
`off_limits` at enumeration**, recording each drop with the pattern and reason that matched it — an
excluded path never becomes an item, so no analyst is ever handed one. Assign each survivor an id
that is **stable and never reused**, so a resume or a re-run after the corpus grows does not
renumber existing items and invalidate the recorded state. Write `manifest.md`: one row per item —
id, locus, size, and a tier column left blank until stage 2. Create the per-item directory for each.
*Rules:* **what an analyzable item is comes from the config, never from the method** — this is the
single most corpus-specific decision, and inventing it silently produces a plausible, wrong run.
**Enumeration is recorded before anything is analysed**, so "was this item ever looked at?" is
answerable from disk. **An empty enumeration is a stop, not a clean run** — it almost always means
the item rule does not match the corpus layout.

**Step 10 — Write `stages/stage-2.md` — size and tier** (P2).
*Procedure:* measure each manifest item against `sizing.fits_threshold` and assign it exactly one
tier: **leaf** — it fits, and analysts read it whole; **split** — it does not fit but the item
definition has a natural sub-unit, so enumerate sub-items, add them to the manifest as children, and
re-run this stage on them; **chunk** — it does not fit and is atomic, so cut it into windows of
`fits_threshold` with `sizing.overlap` between them, each window a child recording its own byte
range, the overlap existing so a fact straddling a cut is seen whole by at least one window. Write
the tier and the chosen strategy back into the item's record.
*Rules:* **every item ends in exactly one tier** — an item with no tier is a decomposition bug, not
an item to skip. **Recursion terminates:** splitting or chunking must reduce the item, and an item
that cannot be reduced below the threshold by either strategy is handled **explicitly and by name**,
never silently dropped. **Tiering is recorded, not remembered**, so a resume does not re-decide it.
**Coverage is declared, never silently reduced** — a partial item that does not say it is partial
produces findings that read as exhaustive and are not.

**Step 11 — Write `stages/stage-3.md` — analyst fan-out** (P3).
*Procedure:* for each leaf item, dispatch `analysts_per_item` cold agents **in a single batch**,
each given `stages/common.md` + `stages/analyst.md` **verbatim**, the item locus, the brief
verbatim, the off-limits list, and **its own distinct output path**. Never exceed the concurrency
ceiling; batch when N × live items would. Skip any unit whose output is already recorded complete.
*Rules:* **identical prompts, isolated contexts** — the analysts differ only in output path, because
any prompt difference makes their agreement uninterpretable as evidence. **Each analyst is handed
the raw item and never another analyst's output or the run's state.** **The dispatcher is a node and
therefore reads no analyst output** — it counts files and moves on. An analyst that returns no file,
or an unusable one, is re-dispatched **once**; a second failure marks the unit `failed` and the item
proceeds with the analysts it has, **recorded as degraded, not silently normal**.

**Step 12 — Write `stages/stage-4.md` — cold verify** (P4), and **mark it in this file as the most
important gate**, with the §2.3 reason.
*Procedure:* per item, dispatch **one cold verifier** given `stages/common.md` +
`stages/verifier.md` verbatim, the item's findings **with analyst identity and count withheld**, the
corpus root, and the off-limits list — and not the analysts' prompts, not the brief's rationale, not
any other item. It writes the item's `verified.md` carrying **every** finding with its disposition.
*Rules:* **only `verified` findings proceed to stage 5.** **Drops are recorded with reasons, not
deleted.** **Record the per-item drop rate in `decisions.md`** — it is the run's health signal, and a
rate near zero deserves as much suspicion as a rate near one.

**Step 13 — Write `stages/stage-5.md` — agreement merge** (P5).
*Procedure:* per item, dispatch one merger given `stages/common.md` + `stages/merger.md` verbatim
and that item's verified findings only. It writes `merged.md`, ranked by agreement, each entry
carrying its claim, canonical locus, quote, `agreement: k/N`, and the analyst ids that produced it —
and it writes the item's fixed-field status record.
*Rules:* restated here because this is the stage where they bite — **agreement counts distinct
analysts, not findings**; **singletons are kept and labelled**; **agreement is a count, not a
confidence**; **ranking is deterministic** so two runs over an unchanged corpus are diffable.

**Step 14 — Write `stages/stage-6.md` — blind roll-up** (P6).
*Procedure:* climb the item tree from leaves to root. A node is given `stages/common.md` +
`stages/node.md` verbatim, the manifest, and its children's status records — **and no other path**.
From those alone it decides: re-run a `failed` child once, then record the failure and roll up
anyway with the gap named; otherwise mark its subtree done, aggregating the counters upward. The
status record schema is fixed-field, and **no field may carry finding content**:

```
item:            <item-id>
state:           done | partial | failed | skipped
findings:        <int>
dropped:         <int>
max_agreement:   <int>/<N>
output:          <path>
```

*Rules:* **the free-text field is the leak channel, so there is none** — a status record containing
claim text is a defect to report, not to read. **A node's expectations cannot steer a child it
cannot read**, which is the entire reason for the schema. **Blindness holds at every level**, not
only at the top: a sub-corpus's own node rolls up its leaves and emits a single status record
upward. **A node with a failed child rolls up anyway and records the gap**, rather than blocking the
whole corpus on one item.

**Step 15 — Write `stages/stage-7.md` — emit the deliverable.**
*Procedure:* assemble the deliverable **mechanically** — concatenate the per-item `merged.md` files
in rank order, so no agent ever reads the assembled whole and forms a view of it. The header carries
the corpus name, the config file used, the item count, `analysts_per_item`, coverage totals, total
findings verified, and totals dropped by disposition. Then three mandatory sections: **not
analysed** (every skipped, failed, and off-limits-excluded item, each with its reason), **partial**
(every unit whose state was `partial`, with what it actually covered), and **dropped in
verification** (counts by disposition, per item).
*Rules:* **assembly is not analysis.** No summary, synthesis, or "key themes" section is produced —
that is exactly the interpretation the method exists to exclude, and the ranking already carries the
emphasis. **No new claims at report time**; anything not traceable to a merged cluster may not
appear. **Coverage is reported, not implied** — a deliverable that does not say what it failed to
look at reads as exhaustive and is the most dangerous artifact this skill can produce.

**Step 16 — Write `Data-Distiller/SKILL.md`** — the router, written now that every file its table
names exists.

- **Frontmatter, exactly two keys:** `name: data-distiller`, and a `description` stating what it is
  (a cold multi-agent method for extracting trustworthy, source-cited factual findings from a corpus
  too large for one context window — decompose, size/tier, N independent cold analysts, cold verify,
  agreement-ranked merge, blind roll-up), when to use it (distilling a large body of material into
  verifiable facts rather than interpretation), that corpus specifics come from a per-corpus Layer-2
  config, and a **proactive-suggest** clause.
- A two-line purpose statement, then: *this file is the **router**; each stage's full procedure and
  the rules governing it live in `stages/`, and `METHODOLOGY.md` is the orientation/reference spec.*
- **`## Inputs`** — the distillation request and the Layer-2 config, with the discovery pattern, the
  refusal to invent corpus specifics, and the validate-every-path requirement.
- **The stage table** — one row per stage file, `| # | Stage — one-line purpose | Read |`, plus the
  role files and which stages dispatch them.
- **The most important gate** — a paragraph naming stage 4 and why.
- **The invariants**, each one sentence pointing at the file that states it operatively: blindness
  (`stages/node.md`), verify-before-merge (`stages/stage-4.md`), facts-not-interpretation
  (`stages/common.md`).
- **`## Stop-for-human`** — the §6 list.
- **`## Self-check / dogfooding`** — these files are position-sensitive prompts, so a non-trivial
  edit takes the full guarded-change loop; standing criteria are live copy == source copy (`diff`),
  SKILL ↔ METHODOLOGY ↔ stage-file consistency on every rule stated in more than one place, and
  behaviour-preservation for anything moved or removed (`Guarded_change/SKILL.md:75-85`,
  `Dragonfly/SKILL.md:83-94`).

**Step 17 — Write `Data-Distiller/data-distiller.<corpus>.md`** — the worked Layer-2 config, and a
worked one: **filled for a real corpus, not a placeholder with angle brackets**, following both
siblings' practice. Shape: a title naming the corpus, a pointer to the contract in the installed
`METHODOLOGY.md`, one fenced YAML block carrying every key from Step 2's contract with an inline
comment giving each key's meaning and default, then a `## Notes specific to this corpus` prose
section (`Guarded_change/guarded-change.companion.md`, `Dragonfly/dragonfly.companion.md`). State
the contract rules alongside it: which keys are required and which optional with their defaults;
`off_limits` is enforced at enumeration and is therefore a property of the manifest rather than a
promise about agent behaviour; every path is validated at stage 0; and — the load-bearing one —
**the config is the only place corpus specifics live**, the core knowing nothing about any corpus.

**Step 18 — Write `Data-Distiller/README.md`** — human-facing, repo-only, on the sibling skeleton:
a TL;DR of what it is; **the failures it guards against**, each with its structural defence, written
for a human; the pipeline; the two-layer structure and the role-file split; **Adopting it** — copy
`SKILL.md`, `METHODOLOGY.md` and `stages/` into `~/.claude/skills/data-distiller/`, write a Layer-2
config from the worked example, invoke it; a **Files** table; and an honest section on **what the
method does not do** — it does not interpret, conclude or recommend; it finds no fact no analyst
noticed; agreement measures reproducibility, not truth (N analysts sharing a blind spot agree
unanimously and wrongly); and blindness costs the roll-up any ability to notice a cross-item
pattern, which is a deliberate trade.

**Step 19 — Install: copy the Layer-1 core to `~/.claude/skills/data-distiller/`.** Copy exactly
`SKILL.md`, `METHODOLOGY.md` and `stages/` — **not** `README.md`, **not** the config, **not** any run
folder. This is the composition measured in §2.1. **`~/.claude/skills/data-distiller/` already
exists on this machine**; installing over it is a destructive act on an existing artifact and takes
the same non-destructive handling as Step 1 — confirm with the human first, or install under a
distinct name for testing.

**Step 20 — Run the mechanical conformance checks and fix what they surface.** Each is a command,
and each must pass:

1. `diff -r` the installed tree against the installed subset of source — empty output. (The standing
   self-check criterion both siblings carry.)
2. The installed `SKILL.md` frontmatter parses as YAML, has exactly `name` and `description`, and
   `name` equals the installed directory name.
3. Every `stages/…` path mentioned anywhere in `SKILL.md` or `METHODOLOGY.md` resolves to a file
   that exists.
4. `SKILL.md`'s stage-table row set equals the stage files on disk, **in both directions** — no row
   without a file and no file without a row.
5. The installed tree contains **no** `README.md`, no config file, and no run folder.
6. **The role split is additions-only** — no normative sentence of `stages/common.md` is restated in
   a role file.
7. **`stages/node.md` grants no findings-read permission** — every mention of a findings, verified or
   merged file in it is a prohibition.

**Step 21 — Run one end-to-end acceptance test on the assembled skill.** Invoke the installed skill
against a real corpus that genuinely does not fit one context window, using the Step 17 config.
Prefer this one assembled run over a set of per-component behavioural micro-tests (§2.8). The
criteria are §7.3. When something breaks, **fix the first link in the chain that broke and re-run** —
do not build a test harness around the failure.

---

## 5. Outputs & artifacts, with their locations

**Source tree**, under `/home/zero/Desktop/claude-code-skills/Data-Distiller/`:

```
Data-Distiller/
├── SKILL.md                     router + YAML frontmatter (name, description)  [step 16] [installed]
├── METHODOLOGY.md               reference spec + Layer-2 config contract       [step  2] [installed]
├── README.md                    human-facing adoption doc                      [step 18] [repo-only]
├── data-distiller.<corpus>.md   worked Layer-2 config                          [step 17] [repo-only]
└── stages/                                                                               [installed]
    ├── common.md                read verbatim first by EVERY dispatched agent  [step  3]
    ├── analyst.md               role additions — N independent cold analysts   [step  4]
    ├── verifier.md              role additions — cold citation re-checker      [step  5]
    ├── merger.md                role additions — cluster + agreement rank      [step  6]
    ├── node.md                  role additions — blind coordinator             [step  7]
    ├── stage-0.md               preflight: config + path validation + resume   [step  8]
    ├── stage-1.md               decompose: enumerate analyzable items          [step  9]
    ├── stage-2.md               size + tier: leaf / split / chunk              [step 10]
    ├── stage-3.md               analyze: N cold analysts per leaf item         [step 11]
    ├── stage-4.md               verify: re-open every citation (the gate)      [step 12]
    ├── stage-5.md               merge: cluster + rank by independent agreement [step 13]
    ├── stage-6.md               roll-up: blind, leaves to root                 [step 14]
    └── stage-7.md               report: the deliverable + its coverage         [step 15]
```

**Installed tree** — `~/.claude/skills/data-distiller/` [step 19]: `SKILL.md`, `METHODOLOGY.md`,
`stages/` and nothing else, byte-identical to source (checked at step 20).

**What a *run* of the skill produces** — under the config's `state.dir`, never inside the corpus:

```
<state.dir>/
├── manifest.md                 one row per item: id | locus | size | tier
├── decisions.md                append-only: validations, tier reasons, retries, resume-skips, overrides
├── <the deliverable>           ranked cited findings + the coverage statement (not analysed / partial / dropped)
└── items/<item-id>/
    ├── status.md               the fixed-field, content-free record a blind node reads
    ├── findings-a1.md … -aN.md one per analyst — never read by a node
    ├── verified.md             every finding with its disposition, drops included
    └── merged.md               agreement-ranked survivors
```

*(No majority on three names: the run-directory default, the deliverable's filename, and the
per-analyst findings filename. All three leaves make the run directory config-supplied via
`state.dir`; the executor picks the two filenames and uses them consistently. See §8.2.)*

---

## 6. Failure modes & contingencies

| # | Assumption / failure | How it fails | Contingency |
|---|---|---|---|
| F1 | The destination directory is free | `Data-Distiller/` already holds a finished implementation, and a blind write destroys it | Step 1 checks before any write and does not resolve the collision on its own judgment. The same applies to the install target at step 19 |
| F2 | A Layer-2 config exists | Absent → the runner invents an item definition and distills the wrong units | Stage 0 stops and asks, or helps author one against the contract. **Never invent corpus specifics** (`Guarded_change/SKILL.md:16-19`, `Dragonfly/SKILL.md:17-21`) |
| F3 | Config paths resolve | A dead `root` → agents produce findings from reasoning alone, carrying plausible paths | Stage 0 validates mechanically before any dispatch and records the result; dead and unresolvable → stop for the human |
| F4 | Enumeration matches the corpus | The item rule does not match the layout and stage 1 yields zero items — a clean, empty, wrong run | An empty enumeration is a stop, not a clean run (stage 1) |
| F5 | An item fits an analyst's context | Misjudged size → the analyst truncates silently and its findings read as exhaustive | Stage 2 sizes every item; the analyst declares what it covered when it cannot read the whole; partial coverage is carried to the deliverable |
| F6 | Analysts are independent | They converge because one read another's output, or because they were dispatched serially | Single-batch dispatch with identical prompts, distinct output paths, the raw item only, and an explicit prohibition in `analyst.md`. **If independence is compromised the agreement count is meaningless** — this is a correctness property, not hygiene |
| F7 | Agreement means the corpus agreed | N analysts share a model and a brief, so unanimous agreement on a wrong reading is the expected failure, not an exotic one | Agreement is reported as a bare count and never as confidence; singletons are retained; the brief is recorded in the run. **Not solvable within this method** — closing it needs heterogeneous analysts, recorded as the obvious future extension |
| F8 | Citations are real | A fabricated `file:line` sails through and the method's whole guarantee is void | Stage 4 opens **every** cited locus; sampling is prohibited; non-`verified` findings are dropped |
| F9 | A citation that resolves supports its claim | The cheapest fabrication is a real file and line with an invented claim | The verifier compares the quote verbatim at the locus **and** tests the claim against it; path existence alone is never sufficient |
| F10 | The verifier is thorough | It rubber-stamps without looking, or receives the analysts' framing and inherits it | Earned clean: a verdict must record the source actually read, and a pass lacking it is treated as un-run and re-run. Its input set is fixed to findings + corpus + off-limits, excluding the analysts' prompts and reasoning |
| F11 | Merging counts real agreement | Three records from one analyst counted as agreement 3; or two claims about different loci merged | Agreement counts distinct analysts; within-analyst dedup runs first; different loci are different findings |
| F12 | The node stays blind | A status record carries claim text, or a node opens `merged.md` "to write a better summary" | The status schema is fixed-field with no free-text field; `node.md` names the forbidden files as an absolute; §7.3 audits the node's actual reads after the run |
| F13 | The run completes in one session | Crash, context exhaustion, or a compaction mid-corpus | State is files, not context; stage 0's resume scan skips units already recorded complete and re-runs everything else |
| F14 | An analyst returns usable output | Empty file, unparsable records, agent error | Re-dispatch once; a second failure marks the unit `failed`, the item proceeds degraded and **recorded**, and the deliverable names it |
| F15 | The concurrency ceiling holds | Dispatching N × item-count agents at once causes throttling, and the failures then look like analysis failures | Batching is a node rule, and a `failed` child is retried once, so a transient throttle does not become a permanent coverage gap |
| F16 | Recursion terminates | A split child that is still oversized splits forever | Splitting must reduce the item; an item that cannot be reduced by either strategy is handled explicitly and by name, never descended into again |
| F17 | A fact survives a chunk boundary | A fact straddling a cut is seen partially by every analyst | `sizing.overlap` exists so a straddling fact is seen whole by at least one window. **Assumption:** the fact fits inside the overlap; one spanning more is still lost, which is why the config must set the overlap against the corpus's real record size and the notes section must say so |
| F18 | `off_limits` is respected | An enumerate command globs outside `root`, or an analyst reads a forbidden path because it seemed relevant | Enforced at enumeration, so a forbidden path never becomes an item — a manifest property, not a behavioural promise. The prompt-level prohibition is the second layer, not the first |
| F19 | Interpretation is kept out | An analyst writes an interpretive claim with a plausible quote attached | The verifier applies the single-locus test to the claim *as stated* against the locus alone, and stage 7 forbids any synthesis section — removing interpretation's natural home. **Residual:** an interpretive claim that happens to be single-locus-checkable survives |
| F20 | The installed copy matches source | Edited in one place, run from the other | Step 20 check 1; the SKILL self-check section makes it a standing criterion |
| F21 | The router and the stage files agree | Every rule stated in both `SKILL.md` and a stage file is a drift candidate, and this repo has lost a day to exactly that | Step 20 check 4 makes the table/file correspondence mechanical, and SKILL ↔ METHODOLOGY ↔ stage-file consistency is a standing self-check criterion |
| F22 | The frontmatter contract is `name` + `description` | **Unverified assumption**, inferred from two working examples, not from a documented schema | If the skill does not appear after install, compare the frontmatter byte-for-byte against a working sibling's before changing anything else |
| F23 | Effort stays on the artifact | The repeat failure of this project: effort migrates into a test harness for agent behaviour until nothing ships | One end-to-end acceptance run against the assembled skill, no per-component behavioural harness; **count rebuilds of a test mechanism, and at three stop building and decide** whether the thing is isolation-testable at all |

**Stop-for-human points** (these belong in `SKILL.md` and `METHODOLOGY.md`): the config is missing
or its item definition is absent; any config path is dead; stage-1 enumeration is empty;
`analysts_per_item` resolves to no value; the destination directory or the install target is already
occupied. **Under delegation the running agent halts and returns the question verbatim to its
orchestrator rather than self-answering** (`Guarded_change/METHODOLOGY.md:208-232`).

---

## 7. Verification

### 7.1 Structural criteria — mechanical, all gating

| # | Criterion | How checked |
|---|---|---|
| V1 | Every source file in §5 exists at its stated path and is non-empty | `test -f` / `test -s` per path |
| V2 | `SKILL.md` frontmatter parses as YAML, has exactly `name` and `description`, and `name` is `data-distiller` | read the first lines |
| V3 | The install directory name equals the frontmatter `name` | `ls ~/.claude/skills/` |
| V4 | Installed tree == source for `SKILL.md`, `METHODOLOGY.md`, `stages/` | `diff -r`, empty output |
| V5 | The installed tree contains no `README.md`, no config, no run folder | `ls ~/.claude/skills/data-distiller/` |
| V6 | Every `stages/…` path referenced in `SKILL.md` or `METHODOLOGY.md` resolves | grep the paths out, `test -f` each |
| V7 | `SKILL.md`'s stage-table rows == the stage files on disk, both directions | set comparison |
| V8 | No role file restates a normative rule from `stages/common.md` | grep each rule sentence of `common.md` against the five role files; a duplicated normative sentence is a finding |
| V9 | `stages/node.md` grants no findings-read permission | grep its mentions of findings / verified / merged files; every hit must be a prohibition |

### 7.2 Coverage criteria — each of the nine properties is present *and operative*

For each of P1–P9 in §1, name the file **and the rule text** that implements it, and confirm that
text is **operative** — an instruction an agent executes — rather than descriptive. **A property
present only in `METHODOLOGY.md` prose and absent from the stage or role file that would enforce it
counts as NOT implemented**, because METHODOLOGY is explicitly not read to run a stage
(`Guarded_change/METHODOLOGY.md:10-11`). Two properties are singled out because they are the easiest
to fake:

- **P6 (blindness)** passes only if `node.md` carries an absolute prohibition on opening any
  findings, verified or merged file, **and** the status schema in `stage-6.md` has no free-text
  field.
- **P9 (facts, not interpretation)** passes only if the single-locus test appears as an executable
  procedure in `verifier.md`, not merely as an exhortation in `common.md`.

### 7.3 The end-to-end acceptance run — the real done-criterion

Invoke the installed skill with the Step 17 config against a real corpus that does not fit one
context window. All criteria gating:

1. **It produces the deliverable.** It exists, is non-empty, and its header carries the item count,
   coverage totals, `analysts_per_item`, and drop counts.
2. **Every sampled citation resolves.** Take a random sample of findings; for each, open the cited
   locus and confirm the quoted text is there verbatim and the claim is true of it. **Any fabricated
   citation is a blocker** — citations are the single guard the whole method rests on.
3. **Coverage is complete and honest.** The three coverage sections are present, and every skipped,
   failed, partial and off-limits-excluded item from the manifest appears in one of them. **Nothing
   is silently absent.**
4. **Resume works.** Kill the run partway and re-invoke it: units already recorded complete are
   **skipped, not re-analyzed**, the interrupted unit is re-run, and the result matches an
   uninterrupted run on the items both covered.
5. **Blindness held.** From the run's own transcripts and tool-call records, **no agent acting as a
   node opened a findings, verified or merged file**, and no finding text appears in any node's
   output or in any dispatch prompt. This is checked from the node's actual reads, not from its own
   report.
6. **The core is corpus-agnostic.** P7 is checked rather than asserted: no corpus specific from the
   acceptance corpus has leaked into Layer 1. *(No majority on the mechanism — one leaf greps the
   Layer-1 files for the corpus's name, paths and item type; another runs the same installed skill
   against a second, structurally different corpus with only a new config and zero edits under
   `~/.claude/skills/data-distiller/`. Either establishes the property; the second is the stronger.)*

**What this test is not.** It does not establish that the findings are *true*, only that they are
cited, verifiable, and reproducible across independent analysts. That is the method's actual claim,
and the verification must not be written to imply more.

**What "done" is not.** Done is not "the files exist and read well." §7.3 is gating; §7.1–7.2 are
necessary but not sufficient, and a build passing only those has produced a plausible document set,
not a working method.

---

## 8. Merge record

*This section is the combiner's, not the plan's. It records how the merge was performed and what it
cost, so a reviewer can attack the merge rather than assume it.*

### 8.1 The rule applied

`Consensus(plans) -> plan`, per `Architect/stages/combiner.md`: **2-of-3 on numbered steps,
including order; the odd plan is discarded.** Three plans were handed in and three were expected.

**Interpretation of "the same point in the sequence", stated because it was load-bearing.** The three
leaves have 20, 23 and 24 steps, so literal step-number equality would have discarded nearly
everything. Agreement was therefore measured on **relative order** — a step agreed when two leaves
state it and place it at the same point relative to the other agreed steps. The one place this
mattered materially: two leaves put the five role files **before** the stage files and one put them
after, so roles-before-stages carried 2-of-3; and two leaves put the **install before** the
mechanical checks while one put a static check first, so install-then-check carried 2-of-3.

Sections 1–3 and 5–7 are not numbered steps. The same 2-of-3 rule was applied to their content:
an element appears only if two leaves stated it, and elements unique to one leaf were discarded.
Parenthetical vote counts are given where the count is informative.

### 8.2 Discarded by the rule (single-leaf elements, not judgments of merit)

**Whole steps discarded:** a separate `stages/state.md` state-and-resume contract file; a separate
`stage-3b.md` post-fan-out integrity check (sha256 corpus-immutability re-check); a `check.sh`
consistency script as an artifact; a cold red-team of the finished skill before install; and three
standalone post-acceptance test steps (resume, blindness) — the last two survive as criteria inside
the acceptance run, where all three leaves also placed them.

**Structural choices outvoted:** an `agents/` directory separate from `stages/` (1 leaf, which
flagged its own divergence); building under `Data-Distiller-impl/` rather than `Data-Distiller/`
(1 leaf); folding the report into stage 6 rather than a stage 7 (1 leaf); one verifier per analyst
file rather than one per item (1 leaf); a `STATUS: complete` completion-terminator scheme for resume
(1 leaf); re-clustering findings at each roll-up level (1 leaf).

**Rules and details discarded:** a `depth_cap`, `drop_alarm`, `bytes_per_token` and `window_overlap`
as named config keys; `n >= 2` as a start condition; an `id_from` key; a `split_rule` key; symlink
resolution at intake; a stage-1 coverage reconciliation against the corpus; a fifth verifier
disposition; verdict-count-in-equals-count-out as an un-run test; a banned-word screening list;
"prefer fewer checkable findings" (directly outvoted by two leaves' "do not rank or select");
per-item boundary re-checks against the full item; an analyst-independence transcript check as an
acceptance criterion; and an "unchecked, not passed" fallback when the host cannot record enough to
audit blindness.

**Details with no majority, recorded rather than invented:** the remedy when the destination
directory is occupied (stop-and-ask vs. build-elsewhere — all leaves agree only that it must not be
blind-overwritten); the run-directory default name; the deliverable's filename; the per-analyst
findings filename; the item-id derivation rule (only "stable and never reused" carried); the merge's
secondary ranking key; the citation sample size at acceptance (5, 10 and 20 were each proposed once);
and which corpus to use for the acceptance run.

### 8.3 Carried from all three leaves as a disclosure

All three leaves independently record that **`/home/zero/Desktop/claude-code-skills/Data-Distiller/`
was never read, listed or grepped** — it was off-limits — so no claim anywhere in this plan about
what that directory should contain was compared against what is actually there, and the destination
is presumed non-empty (F1). Two of the three additionally disclose that **the installed skill's
one-line frontmatter `description` was already present in their context** via the harness's
available-skills listing, identically for every leaf, before any file was read; neither treated it
as a source. Two of the three flag that the **`name` + `description` frontmatter contract is
inferred from two working examples, not from a documented schema** (F22).

### 8.4 Citation spot-check

Sampled from the citations the leaves share: `Guarded_change/METHODOLOGY.md:10-11` (the
orientation-not-a-stage disclaimer), `Guarded_change/SKILL.md:16-18` (config discovery and the
refusal to invent), `Architect/stages/common.md:3-4` (every dispatched agent reads the common file
first, then its role file). The Architect citation was checked directly against the file supplied to
this combiner and resolves as claimed. **The two `Guarded_change/` citations, and every other
`file:line` in the three plans, were not opened** — this combiner was handed only the three plans,
the spine template and its own stage files, so it reports the sibling-skill citations as
**unchecked rather than clean**. All such citations appear identically in at least two independent
leaves, which is corroboration, not verification.
