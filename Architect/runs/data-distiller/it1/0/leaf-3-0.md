# Plan — implement the Data-Distiller skill

*Leaf plan, written cold. Fills `Architect/templates/spine.md`. Every section filled.*

---

## 0. Disclosures and scope notes (read first)

Three things a reviewer must know before weighing anything below.

**0.1 — An off-limits artifact leaked into my context through the harness, not through me.** I did
not read, list, or grep `/home/zero/Desktop/claude-code-skills/Data-Distiller/`. However, my system
prompt's available-skills listing contains the *installed* copy's frontmatter description
(`data-distiller: A cold, multi-agent method for extracting trustworthy source-cited factual
findings… decompose → size/tier → N independent cold analysts → cold verify → agreement-ranked merge
→ blind roll-up…`). I could not decline to receive it. Its content is a near-restatement of the
bullet list already in my task, so it changed nothing in this plan that the task text did not
already fix; I disclose it rather than let a reviewer discover the overlap and read it as copying.
One incidental exposure: I ran `ls -la ~/.claude/skills/data-distiller/ | head -3`, which returned
only the total line and `.`/`..` — no filenames. I did not repeat it.

**0.2 — The destination directory already contains a finished implementation, and this plan is
written blind to it.** The house convention (see §3) puts this skill at
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`, which is exactly the off-limits path. The
plan therefore names that path as the destination but **cannot assume the directory is empty**.
Step 1 handles this explicitly, and §6.1 carries the contingency. An executor must not blind-write
over it.

**0.3 — What I verified vs. what I assumed.** Everything in §3 (the house shape) I read from disk
and cite by path. The design of the distillation method itself (§2, §4) is *derived* from the task's
property list plus the siblings' structural conventions; it is not verified against any existing
Data-Distiller. Where I could not check something, §6 says so.

---

## 1. Problem / intent

**What this node plans.** The whole of the assigned task: the implementation of `data-distiller` as
a Claude Code skill — a directory of markdown prompt files, invokable by name — realizing a cold,
multi-agent method for extracting trustworthy, source-cited factual findings from a corpus too large
for one context window. There is no sibling slice; this leaf owns the entire deliverable.

**Why it is a skill and not a script.** The nine defining properties in the task are all *agent
discipline* — coldness, independence, read-only access, citation, blindness. None of them are
enforceable by code; all of them are enforceable only by what each dispatched agent is told. That is
precisely what the two sibling skills are: prompt files that constrain dispatched agents. So the
deliverable is a set of markdown files whose *text* is the mechanism.

**The nine properties this plan must cover** (from the task, restated as a checklist §7 audits):

| # | Property | Where the plan puts it |
|---|---|---|
| P1 | Decompose the corpus into analyzable items | stage 1 |
| P2 | Size items; pick a per-item strategy when one does not fit | stage 2 |
| P3 | N independent cold analysts per item, read-only, citing every finding | stage 3 + `stages/analyst.md` |
| P4 | Cold verification re-checking every citation; drop the unverifiable | stage 4 + `stages/verifier.md` |
| P5 | Merge ranking survivors by independent-analyst agreement | stage 5 + `stages/merger.md` |
| P6 | Blind roll-up — coordinator sees only terse per-child status | stage 6 + `stages/node.md` |
| P7 | Per-corpus Layer-2 config; method stays corpus-agnostic | `METHODOLOGY.md` contract + worked config |
| P8 | Restart and resume from on-disk state | stage 0 (resume scan) + per-item `status.md` |
| P9 | Facts, not interpretation | the finding schema, enforced at stages 3/4/5 |

---

## 2. Approach

### 2.1 Clone the house shape, do not invent one

Both siblings are the same object with different content, and I read both:

- `Guarded_change/SKILL.md:1-4` and `Dragonfly/SKILL.md:1-4` — YAML frontmatter with exactly two
  keys, `name` and `description`, then a router that walks a numbered stage table pointing at
  `stages/*.md`.
- `Guarded_change/METHODOLOGY.md` / `Dragonfly/METHODOLOGY.md` — the same seven sections in the same
  order: Why this exists / The loop (ASCII diagram) / Stage index (table) / The two layers / The
  config contract (Layer 2, YAML) / What a run produces (artifact tree) / Human-in-the-loop. Both
  open with the identical disclaimer that the file "is opened for orientation and config setup — not
  to run a stage" (`Guarded_change/METHODOLOGY.md:7-11`, `Dragonfly/METHODOLOGY.md:7-12`).
- `stages/stage-N.md` — each opens `**What this stage does:** <one line>`, then `## Procedure`, then
  `## Cross-cutting rules governing this stage` (see `Dragonfly/stages/stage-2.md:1-6,21`).
- A per-project Layer-2 config lives in the *repo* directory, named `<skill>.<project>.md`, holding
  one fenced YAML block plus a `## Notes specific to this project` prose section
  (`Guarded_change/guarded-change.companion.md`, `Dragonfly/dragonfly.companion.md`).
- A repo-level `README.md` aimed at a human adopter, not at the agent (`Guarded_change/README.md`).

**Data-Distiller adopts all of this unchanged.** Deviating would cost a reviewer's attention for no
gain, and the shape is load-bearing: the router/stage split exists so an agent reads one stage file
at a time rather than a monolith.

### 2.2 What is installed vs. what stays in the repo — measured, not assumed

I diffed the live installs against source. `~/.claude/skills/guarded-change/` contains exactly
`SKILL.md`, `METHODOLOGY.md`, `stages/` — and `diff Guarded_change/SKILL.md
~/.claude/skills/guarded-change/SKILL.md` is empty (identical). `~/.claude/skills/dragonfly/` is the
same three items. **Neither install contains `README.md`, the `<skill>.<project>.md` config, or the
run folders (`changes/`, `hunts/`).** So:

- **Installed core (Layer 1):** `SKILL.md` + `METHODOLOGY.md` + `stages/`.
- **Repo-only:** `README.md`, the worked Layer-2 config, and run output.

Install is a **copy**, not a symlink (the live files are regular files with their own mtimes), which
is why both siblings carry a standing self-check criterion "live copy == source copy (`diff`)"
(`Guarded_change/SKILL.md:82-83`, `Dragonfly/SKILL.md:88`). Data-Distiller inherits that criterion
and this plan's step 19 executes it.

### 2.3 The one deliberate extension: role files, because this skill dispatches four kinds of agent

Both siblings dispatch exactly **one** kind of agent — a cold reviewer — so both have exactly one
dispatched-agent prompt, `stages/charter.md`, shared by the stages that spawn
(`Guarded_change/METHODOLOGY.md:82-83`; `Dragonfly/stages/charter.md:1`).

Data-Distiller dispatches **four**: an analyst, a verifier, a merger, and a coordinating node. A
single shared charter would hand every one of them the other three's instructions — and, worse,
would hand the *blind node* the analyst's instructions, which is the precise contamination the
blindness property exists to prevent. So the dispatched-agent prompts split by role:

```
stages/common.md      what EVERY dispatched agent needs — verbatim-included in each role dispatch
stages/analyst.md     additions only
stages/verifier.md    additions only
stages/merger.md      additions only
stages/node.md        additions only
```

with the hard rule that **role files are additions only and never restate a common rule**; a role
file needing to *modify* a common rule is the signal the rule was never common and must move down
into the roles. This matches the repo's own live practice for multi-agent skills: the Architect
skill I am running under splits its dispatched-agent prompts exactly this way, at
`Architect/stages/common.md` ("Every agent Architect dispatches reads this file first, then its role
file… The common file is stated once; the role file adds what is specific to yours", `common.md:3-4`)
plus one file per role (`Architect/stages/leaf.md`). It also matches the standing authoring rule in
the user's global `CLAUDE.md` ("Authoring multi-agent skills — split the prompts by ROLE"), whose
stated failure case is a 237-line monolith in which three of six roles turned out to have no
instructions at all and nobody noticed because the monolith *looked* complete.

**Alternative considered and rejected:** one `stages/charter.md` like the siblings, for consistency.
Rejected because consistency here buys a cosmetic match at the cost of the blindness property (P6),
which is not negotiable; and because the repo's own multi-agent skill already broke that tie the
other way.

**Second alternative considered and rejected:** an `agents/` subdirectory rather than putting role
files in `stages/`. Rejected because Architect puts them in `stages/`, so `stages/` is the evidenced
location, and a second directory adds a lookup a router would have to explain.

### 2.4 No red-team charter of its own

Data-Distiller does not fork a red-team charter. Its runtime roles are not reviewers, and its
*self-check* (the dogfooding section every sibling SKILL.md carries) runs under **guarded-change**,
using `Guarded_change/stages/charter.md`. Dragonfly forked its charter only because it spawns
reviewers at stages 1/4/7 and wanted to stop tracking guarded-change's edits
(`Dragonfly/stages/charter.md:8-12`); Data-Distiller spawns no reviewers at runtime, so a fork would
be an unused fifth role file that still has to be maintained.

### 2.5 The method, in one paragraph

A **corpus** is decomposed into **items**. Each item is **sized**; one that fits a context window is
a **leaf**, one that does not is **split** into child items (recursively), and an atomic item that
still does not fit is **chunked with a stated overlap**, each chunk becoming a child. At every leaf,
**N cold analysts** (default 3) are spawned **in one batch** so none can see another's output; each
is read-only over the corpus and emits findings to its own path, every finding carrying a citation
and a verbatim quote. A **cold verifier** — which never sees the analysts' prompts or reasoning,
only their finding files and the corpus — re-opens **every** citation and drops what it cannot
confirm. A **merger** clusters the survivors and ranks them by **how many distinct analysts
independently produced each**. Every level above a leaf is a **blind node**: it reads only a
fixed-schema, content-free `status.md` per child and never opens a findings file. The final
distillate is assembled **mechanically** by concatenation in rank order, so no agent ever reads the
whole finding set and forms a view of it.

### 2.6 The two mechanisms that make "facts, not interpretation" enforceable rather than aspirational

An instruction to "record facts, not interpretation" is unenforceable as prose. Two mechanisms make
it checkable:

1. **The finding schema.** Every finding is `{id, claim, locus (file:line or record id), quote
   (verbatim, ≤2 lines), scope}`. The `quote` field is what makes P9 mechanical.
2. **The single-locus test, applied by the verifier.** *A finding is a fact iff a reader who opens
   only its cited locus, and reads nothing else, can confirm the claim as stated.* A claim needing
   inference across two loci is interpretation. The verifier drops it, or — if it is genuinely a
   two-locus fact — the analyst should have filed two findings. This turns a value judgment into a
   procedure the verifier executes without judgment calls.

### 2.7 Where the concurrency ceiling actually bites, and its honest limitation

The config's ceiling is applied by the **dispatching** agent as a batch-size cap: no agent spawns
more than `concurrency.max_parallel_agents` children at once, and **a node expands one child subtree
at a time** rather than all of them. Sequential subtree expansion is what makes a per-node cap equal
a global cap. **Limitation, stated because it is real:** there is no run-wide semaphore; nothing
mechanically prevents two independently-invoked runs from jointly exceeding the ceiling. The rule
bounds a single run's tree, which is what the ceiling is for. §6.7 carries this.

---

## 3. Interfaces & seams

**Consumes:**

1. **A corpus** — a read-only tree of files, named by `root` in the Layer-2 config.
2. **A Layer-2 config file** (`data-distiller.<corpus>.md`), supplying: what an analyzable item *is*
   here, what is off-limits, the concurrency ceiling, the sizing thresholds, and the extraction
   brief. Per the siblings' rule, the skill **refuses to invent these** rather than guessing
   (`Guarded_change/SKILL.md:16-18`, `Dragonfly/SKILL.md:17-20`).
3. **A distillation request** — what the caller wants extracted, narrowing but never overriding the
   config's brief.

**Emits:**

1. `distillations/<slug>/distillate.md` — the ranked, cited finding set. The deliverable.
2. `distillations/<slug>/` run state — per-item directories, resumable.
3. `distillations/<slug>/decisions.md` — the append-only gate log, matching both siblings.

**Seams to whatever sits beside it:**

- **To Claude Code (the host).** `SKILL.md` frontmatter `name: data-distiller` must equal the
  install directory name `~/.claude/skills/data-distiller/`, or the skill will not resolve. The
  `description` is the *trigger* surface — it is what the host matches a user request against, so it
  states both the what and the when, as both siblings' descriptions do.
- **To dispatched subagents.** Each role dispatch = `stages/common.md` verbatim + that role's file
  verbatim + the run-specific arguments (item locus, output path, brief). This is the only channel;
  a dispatched agent has no other context, which is what "cold" means operationally.
- **To a human.** The stop-for-human set (§6.9), surfaced as questions, never self-answered.
- **To guarded-change.** Self-check/dogfooding: non-trivial edits to these files take the full
  guarded-change loop, because these files are position-sensitive prompts
  (`Guarded_change/SKILL.md:79-85`, `Dragonfly/SKILL.md:86-88`).
- **To the corpus owner.** Read-only is a contract, backed by the sha256 manifest re-check in §4
  step 8 / §6.5.

---

## 4. Steps

Ordered. Each step is one file created, or one coherent edit to one file, with its content
specified. Order is content: the contract (METHODOLOGY) is fixed before the prompts that must obey
it; the role prompts are fixed before the stages that dispatch them; the router is written last of
the core files because it must match the final stage list exactly; install and verify come last.

---

**Step 1 — Establish the destination directory, without overwriting what is there.**
Target `/home/zero/Desktop/claude-code-skills/Data-Distiller/`. Run `ls -A` on it. **If it is
absent or empty:** `mkdir -p Data-Distiller/stages` and proceed to step 2. **If it is non-empty:**
STOP and ask the human whether to (a) work in a fresh directory, (b) reconcile file-by-file against
what exists, or (c) replace it — recording the choice in the run's `decisions.md`. Do not proceed on
your own judgment. *Rationale: §0.2 — this plan was written blind to that directory's contents, so
the executor is the first party able to see the collision, and it is not the executor's call.*

**Step 2 — Create `Data-Distiller/METHODOLOGY.md`.**
Seven sections, in the siblings' order and with their opening disclaimer ("orientation and config
setup — not to run a stage"):
- *Why this exists* — the failure modes Data-Distiller is built against, each mapped to a structural
  defense, in the siblings' one-to-one style: (1) **the single reader's priors** — one agent reads
  everything and its expectations shape what it notices → N independent cold analysts + blind
  roll-up; (2) **the confident uncited claim** → citation-per-finding + the cold verify pass;
  (3) **interpretation smuggled in as fact** → the finding schema + the single-locus test;
  (4) **silent truncation** — a corpus larger than context is read partially and reported as if
  wholly → explicit sizing, tiering, and a coverage number carried to the distillate;
  (5) **context loss mid-run** → on-disk state and resume.
- *The loop* — the ASCII stage diagram (stages 0–7, §4 steps 4–11).
- *Stage index* — the three-column table (Stage | File | What it covers), one row per stage file
  **plus rows for the five role files**, so a reader can find a role prompt from the index.
- *The two layers* — Layer 1 = this doc + SKILL.md + stages/; Layer 2 = the per-corpus config.
  Verbatim-parallel to `Guarded_change/METHODOLOGY.md:88-95`.
- *The config contract (Layer 2)* — the full YAML in step 3's shape, plus the rules: off-limits is
  enforced before any read, not after; `analysts_per_item` defaults to **3** if omitted and the run
  refuses to start if no value is resolvable (mirroring Dragonfly's `N` rule,
  `Dragonfly/METHODOLOGY.md:132`); **every config path is validated at run start** (dead →
  stop, adaptable → adapt + record + proceed, per `Dragonfly/METHODOLOGY.md:135-137`); state is
  files, not context, because resume depends on surviving a restart.
- *What a run produces* — the artifact tree from §5.
- *Human-in-the-loop* — the stop-for-human set from §6.9.

**Step 3 — Add the Layer-2 config contract YAML block inside `METHODOLOGY.md` (the edit that fixes
the contract).** Exact keys, since every later file references them:
```yaml
corpus: <name>

root: <path to the corpus root>        # read-only for the whole run

item:                                  # what ONE analyzable item IS in this corpus
  unit: <prose: e.g. "one .jsonl session transcript" | "one source file">
  enumerate: <command or manual procedure that lists item loci, one per line>
  id_from: <how to derive a stable, filesystem-safe item id from a locus>

off_limits:                            # never read, never cited; checked BEFORE any read
  - path: <glob>
    reason: <why>

brief:                                 # the standing extraction brief — corpus-specific
  extract: <what counts as a finding here>
  out_of_scope: <what is interpretation rather than fact, in THIS corpus>

sizing:
  fits_threshold: <e.g. "120000 characters">   # at or under => leaf; over => split
  oversize_strategy: split | chunk             # split by sub-unit, else chunk
  chunk_overlap: <e.g. "200 lines">            # required when strategy is chunk

concurrency:
  max_parallel_agents: <int>           # ceiling on simultaneously live subagents
  analysts_per_item: <int>             # OPTIONAL — overrides the Layer-1 default of 3

state:
  dir: "distillations/<slug>/"         # must survive a session restart
```

**Step 4 — Create `Data-Distiller/stages/stage-0.md` — Preflight & resume.**
`**What this stage does:** load and validate the config, then decide whether this is a new run or a
resume.` Procedure: locate a `data-distiller.*.{md,yaml}` config in or near the working dir; refuse
to invent one; mechanically validate that `root` and every `off_limits` path resolves and is
readable, and that `item.enumerate` runs; record the validation result in `decisions.md` (**no stage
may pass until it is recorded** — the gate-4 analogue at
`Guarded_change/METHODOLOGY.md:139-144`); resolve `analysts_per_item` (config, else default 3, else
refuse to start). Resume: if `state.dir` exists, read every `items/<id>/status.md` and treat any
item whose `state:` is `done` as complete — **skipping it entirely, not re-analyzing it**; re-verify
the stage-1 corpus manifest hashes before trusting any of it (§6.6). Cross-cutting rule: *state is
files, not context* — a resume must be reconstructible with zero conversation history.

**Step 5 — Create `stages/stage-1.md` — Decompose.**
Run `item.enumerate`; drop every locus matching `off_limits` and record each drop with its reason;
assign each survivor an id via `item.id_from`; write `manifest.md` (one row per item: id, locus,
bytes, sha256) and create `items/<id>/` for each. **The coverage check, which is the point of this
stage:** independently count the files and bytes under `root` minus `off_limits`, and compare
against the manifest's totals. Any shortfall is reported as an explicit uncovered set — never
silently absorbed. A shortfall above a config-free threshold of **zero unexplained items** stops for
a human. Cross-cutting: *the manifest's sha256 column is the corpus-immutability baseline* used at
step 8.

**Step 6 — Create `stages/stage-2.md` — Size & tier.**
For each manifest item, compare its size to `sizing.fits_threshold` and assign exactly one tier:
`leaf` (fits — runs stages 3–5 directly); `split` (does not fit, and `item.unit` has a natural
sub-unit — enumerate sub-items, add them to the manifest as children, recurse); `chunk` (does not
fit and is atomic — cut into windows of `fits_threshold` with `sizing.chunk_overlap` overlap, each
window a child, **and every child records its byte range**). Write the tier and the strategy into
`items/<id>/status.md`. Cross-cutting rules: *a boundary is a citation hazard* — any finding whose
locus falls within `chunk_overlap` of a chunk edge is marked `boundary` and re-checked at stage 4
against the full item, not the chunk; *tiering is recorded, not remembered*, so a resume does not
re-decide it; *recursion terminates* — a `split` child that is still oversized and still has a
sub-unit splits again, but an item that cannot be reduced below the threshold by either strategy is
a stop-for-human, not an infinite descent.

**Step 7 — Create `stages/stage-3.md` — Analyst fan-out.**
`Read stages/common.md and stages/analyst.md; dispatch with common.md verbatim + analyst.md
verbatim.` Procedure: for each `leaf` item, spawn `analysts_per_item` cold subagents **in a single
batch** (all in one message, so no analyst can observe another's output), each given: the item
locus, the `brief`, the `off_limits` list, the finding schema, and **its own distinct output path**
`items/<id>/findings-a<k>.md`. Batch size never exceeds `concurrency.max_parallel_agents`; one child
subtree is expanded at a time. Cross-cutting rules: *identical prompts, isolated contexts* — analysts
differ only in output path, because any prompt difference makes their agreement uninterpretable as
evidence; *an analyst that reads a sibling's findings file has destroyed the run's only evidence*,
so it is forbidden by rule and detected at step 8; *read-only is a contract* — an analyst writes to
exactly one path, never under `root`.

**Step 8 — Create `stages/stage-3b.md` — Post-fan-out integrity check** *(or, if the executor
prefers a flatter numbering, append this as a `## Post-fan-out integrity` section to stage-3.md; it
must exist somewhere and be run after every fan-out).*
Two mechanical checks after each batch returns, both cheap and both catching a failure nothing else
would: (1) **corpus immutability** — recompute sha256 for every item touched and diff against the
stage-1 manifest; any change means an analyst wrote to the corpus, which invalidates the batch;
(2) **fan-out completeness** — exactly `analysts_per_item` findings files exist and each is
non-empty; a missing or empty one is re-run once, then stops for a human. Record both in
`decisions.md`. Cross-cutting: *a failed integrity check invalidates the item's findings, not just
the file* — the item returns to stage 3.

**Step 9 — Create `stages/stage-4.md` — Cold verify.**
Dispatch one cold verifier per item (`common.md` + `verifier.md`), given **only**: the item's
findings files, the corpus root, and the off-limits list — **not** the analyst prompt, not the brief's
rationale, not any other item. Procedure: for **every** finding, open its cited locus and decide
`verified` / `unverifiable` / `misquoted` / `off-limits-source`; apply the single-locus test (§2.6);
re-check `boundary`-marked findings against the full item rather than the chunk. Write
`items/<id>/verified.md` carrying **every** finding with its disposition — drops are recorded, not
deleted, so the drop rate is itself a signal. Cross-cutting rules: *the verifier is cold about the
analysts, not about the corpus* — it must open sources, and a verify pass that cites no source it
opened is treated as **un-run and re-run** (the earned-clean rule, `Dragonfly/stages/charter.md:40-43`);
*a citation that cannot be resolved is a drop, never a benefit of the doubt*; *the verifier does not
add findings* — it is a filter, and a new claim from a verifier has no independence to measure.

**Step 10 — Create `stages/stage-5.md` — Agreement merge.**
Dispatch one merger per item (`common.md` + `merger.md`) over `verified.md` only. Procedure:
(1) **dedupe within each analyst first**, so one analyst restating itself cannot inflate agreement;
(2) cluster equivalent findings **across** analysts — equivalence is *same locus + same claim*, and
same-claim-different-locus stays separate because it is a different fact; (3) assign each cluster
`agreement = <distinct analysts>/<N>`; (4) write `items/<id>/merged.md` ranked by agreement
descending, each entry carrying its claim, canonical locus, quote, and the analyst ids that produced
it; (5) write `items/<id>/status.md` in the fixed schema of step 11. Cross-cutting rules:
*agreement counts analysts, not findings*; *agreement 1/N is kept, not dropped* — a single analyst's
verified, cited finding is real signal and is ranked last, not discarded (this mirrors the siblings'
"findings are merged, never voted on" discipline); *the merger reads findings and therefore may never
be reused as a node* (§2.5).

**Step 11 — Create `stages/stage-6.md` — Blind roll-up.**
`Read stages/common.md and stages/node.md.` Procedure: a node reads **only** each child's
`items/<id>/status.md`, whose schema is fixed and content-free:
```
item: <id>
state: done | partial | failed | skipped-off-limits
tier: leaf | split | chunk
findings_verified: <int>
findings_dropped: <int>
agreement_max: <int>/<N>
coverage: <bytes analyzed>/<bytes in item>
note: <ONE line, mechanical only — a state fact, never finding content>
```
From these alone the node decides: re-run a `failed` child (once), stop for a human on a second
failure, and otherwise mark its own subtree `done`, aggregating the counters. The node **never opens
`merged.md`, `verified.md`, or any `findings-a<k>.md`, and never cites finding content in its own
output** — that prohibition is the blindness property, and it is stated in `node.md` as an absolute.
Cross-cutting rules: *the `note:` field is the leak channel* — it is capped at one line and to
mechanical facts precisely because a free-text field is where finding content would leak upward;
*a node's expectations cannot steer a child it cannot read*, which is the entire reason for the
schema; *nodes expand one subtree at a time* (§2.7).

**Step 12 — Create `stages/stage-7.md` — Emit the distillate.**
Assemble `distillations/<slug>/distillate.md` **mechanically**: concatenate every `merged.md` in the
tree, ordered by agreement descending then by item id, with no agent reading the assembled whole and
forming a view of it. The header carries: corpus name, config file used, run slug, item count,
coverage totals from stage 1 and stage 6, `analysts_per_item`, total findings verified, total
dropped and by which disposition. Cross-cutting rules: *assembly is not analysis* — no summary,
synthesis, or "key themes" section is produced, because that is the interpretation the method exists
to exclude, and the ranking already carries the emphasis; *the uncovered set from stage 1 and every
`partial`/`failed` item are named in the distillate*, because a distillate that hides its own gaps
is the silent-truncation failure wearing a report's clothes.

**Step 13 — Create `Data-Distiller/stages/common.md`.**
What **every** dispatched agent needs, and nothing any single role needs alone. Contents: *you are a
cold, independent agent, sharing no context with whoever produced your input and none with the
siblings spawned alongside you — do not hedge toward an imagined consensus, because convergence is
the only evidence the merge has*; *your inputs are exactly what your caller passed you — open what
your task points at, and nothing it does not*; *the off-limits list is absolute and is checked before
a read, not after*; *the corpus is read-only — your only write target is the single output path you
were given*; *cite or it doesn't count: every finding names a `file:line` or record id and carries a
verbatim quote*; *flag what you could not check as unchecked rather than accepting it silently*;
*facts, not interpretation — the single-locus test (§2.6) stated in full*; *if you cannot do your job
with what you were given, say so plainly at the head of your output and do the best bounded work you
can — do not go looking for a substitute source*; *write your output to the path your caller named
and return that path plus a short summary; nothing else you say is read.* **Rule stated in this file
itself:** role files add, never restate or modify — a rule needing modification per role was never
common and moves down.

**Step 14 — Create `stages/analyst.md`.**
Additions only. *You read the corpus item you were given and emit findings — you are one of N run in
parallel on the same item, and you will never see the others' output, which is the point.* The
finding schema in full (`id / claim / locus / quote / scope`). *Do not attempt to be comprehensive
at the cost of being right: an uncited finding is worth less than no finding.* *Do not read any
other analyst's output file, or any file outside your item's locus and the corpus paths your task
names.* *Do not rank, weigh, or summarize your own findings — ranking is the merge's job and your
ranking would contaminate it.* *Emit findings even where you expect the others found the same thing;
suppressing an "obvious" finding destroys the agreement signal.*

**Step 15 — Create `stages/verifier.md`.**
Additions only. *You receive findings and the corpus; you do not receive the analysts' instructions
or reasoning, and you must not reconstruct them.* Procedure: open **every** cited locus — no
sampling; assign one of the four dispositions; apply the single-locus test; treat an unresolvable
locus as a drop. *A clean verify pass must be earned: your output shows the specific loci you opened,
and a pass citing no opened source is treated as un-run and re-run.* *You are a filter, not an
author — do not add findings, do not repair a bad citation into a good one, and do not merge.*
*Record drops with reasons; a drop rate is a signal the run needs.*

**Step 16 — Create `stages/merger.md`.**
Additions only. *You receive one item's verified findings and nothing else.* The four-step merge
procedure from step 10. *Equivalence is same-locus-and-same-claim; when in doubt, keep them separate
— a false merge silently inflates agreement, which is the one number this method sells.*
*Agreement 1/N is ranked last, never dropped.* *Emit both `merged.md` and the fixed-schema
`status.md`, and put no finding content in `status.md` — a node will read it and must stay blind.*

**Step 17 — Create `stages/node.md`.**
Additions only. *You coordinate; you never read findings.* The absolute prohibition: *you may open
`status.md` files and the manifest, and nothing else under `items/`.* *You have no view about what
the children should have found, and you must not form one — if you knew what they found you could
steer them, and everything below you would inherit your expectations.* The decompose/expand duty
(tiering, spawning child nodes, one subtree at a time, batch ≤ `max_parallel_agents`). The re-run
rule (one retry on `failed`, then stop for a human). *Your own output cites counts and states, never
content.*

**Step 18 — Create `Data-Distiller/SKILL.md` — the router. Written after the stages so its table
matches them exactly.**
Frontmatter, exactly two keys:
```yaml
---
name: data-distiller
description: <one paragraph: a cold, multi-agent method for extracting trustworthy, source-cited
  factual findings from a corpus too large for one context window — decompose, size/tier, N
  independent cold analysts, cold verify, agreement-ranked merge, blind roll-up. Use when a large
  body of logs/transcripts/files must be distilled into verifiable facts rather than
  interpretation. Corpus specifics come from a per-corpus Layer-2 config. Proactively SUGGEST when
  asked to sift, audit, or distill a corpus that will not fit in one pass.>
---
```
Body, in the siblings' order: a two-line statement of purpose; `## Inputs` (the corpus, the config —
*look for `data-distiller.*.{md,yaml}`, refuse to invent it, validate every path at run start and
record the result*); `## Loop` (the stage table, one row per stage file, `| # | Stage — one-line
purpose | Read |`); a paragraph naming **the most important gate** — for this skill, **stage 4, the
cold verify**, because it is the cheapest place to kill an uncited or interpretive finding, before
it is merged, ranked, and inherited by the distillate as though it were established; a `## The
dispatched roles` table mapping each role to its file and to the stages that dispatch it;
`## Stop-for-human`; `## Self-check / dogfooding` (these files are position-sensitive prompts;
non-trivial edits take the full guarded-change loop; standing criteria: live == source (`diff`),
SKILL ↔ METHODOLOGY ↔ stage-file consistency on every rule stated more than once,
behavior-preservation for anything moved or removed).

**Step 19 — Create `Data-Distiller/data-distiller.<corpus>.md` — one worked Layer-2 config.**
A *real* corpus, not a placeholder, following both siblings' practice of shipping a worked example
rather than a template with angle brackets. Recommended subject: this repo's own accumulated run
records — `Guarded_change/changes/` plus `Dragonfly/changes/` (~130 markdown files across ~20 run
folders, verified by `find`), which genuinely exceeds one context window and is available offline.
Fill every key from step 3: `item.unit` = one run folder; `item.enumerate` = the `find` that lists
them; `off_limits` = `Data-Distiller/**` with the reason; `brief.extract` = "each gate decision, its
severity, and its route, with the decisions.md line that records it"; `brief.out_of_scope` = "whether
a decision was correct". Then the `## Notes specific to this corpus` prose section, matching
`Dragonfly/dragonfly.companion.md:42-58`.

**Step 20 — Create `Data-Distiller/README.md`.**
Human-facing, mirroring `Guarded_change/README.md`: TL;DR; **"the failure it guards against"** (one
reader's priors silently shaping what a large corpus is found to contain); the loop diagram; the
two-layer structure; **adoption** — copy `SKILL.md` + `METHODOLOGY.md` + `stages/` into
`~/.claude/skills/data-distiller/`, write a Layer-2 config, invoke it; a `## Files` table; and an
honest-caveat section naming what the method does *not* do (it finds no fact that no analyst
noticed; agreement measures reproducibility, not truth — N analysts sharing a blind spot agree
unanimously and wrongly; and blindness costs the roll-up any ability to notice a cross-item pattern,
which is a deliberate trade).

**Step 21 — Cold red-team the finished skill.**
Spawn a cold subagent (`general-purpose` or `Explore`, no shared context) over `SKILL.md` +
`METHODOLOGY.md` + `stages/*` with guarded-change's five-lens charter verbatim
(`Guarded_change/stages/charter.md`), and write the verbatim record — charter given, exact context
list, reviewer's raw output, agent type/model — to
`Data-Distiller/changes/initial-build/6-redteam-code.md`. Route blocker/major back into the relevant
step above. *This is house practice, not optional polish: both siblings state that these files are
prompts and that a stage-3-style red-team is the standing cheap check after any edit
(`Guarded_change/SKILL.md:84-85`).*

**Step 22 — Install: copy the Layer-1 core to `~/.claude/skills/data-distiller/`.**
`mkdir -p ~/.claude/skills/data-distiller` then copy exactly `SKILL.md`, `METHODOLOGY.md`, and
`stages/` — **not** `README.md`, **not** the config, **not** `changes/`. This is the composition
measured in §2.2. *If that directory already exists and is non-empty, this is the same collision as
step 1 and takes the same stop-for-human, not an overwrite.*

**Step 23 — Verify the install and the internal consistency.**
Run the four mechanical checks: (1) `diff -r Data-Distiller/stages ~/.claude/skills/data-distiller/stages`
and `diff` on each of the two top-level files — all empty; (2) every `stages/…` path mentioned in
`SKILL.md` or `METHODOLOGY.md` resolves to a file that exists; (3) the SKILL.md loop table's row set
equals `ls stages/stage-*.md`, no row without a file and no file without a row; (4) the YAML key set
in METHODOLOGY's contract equals the key set in the worked config. Record the results in
`Data-Distiller/changes/initial-build/decisions.md`.

**Step 24 — Run the end-to-end acceptance test (§7.3).**
Invoke `data-distiller` on the worked config from step 19 and check the four acceptance criteria in
§7.3, including the mid-run kill and resume. Record the outcome. *This is the assembled-run test the
plan deliberately prefers over per-component harnesses; see §6.10.*

---

## 5. Outputs & artifacts, with their locations

**Source tree** — everything under `/home/zero/Desktop/claude-code-skills/Data-Distiller/`:

```
Data-Distiller/
├── SKILL.md                          router + YAML frontmatter (name, description)   [step 18]
├── METHODOLOGY.md                    reference spec + Layer-2 config contract        [steps 2–3]
├── README.md                         human-facing adoption doc  (repo-only)          [step 20]
├── data-distiller.<corpus>.md        worked Layer-2 config      (repo-only)          [step 19]
├── stages/
│   ├── stage-0.md   preflight & resume                                               [step 4]
│   ├── stage-1.md   decompose + coverage check                                       [step 5]
│   ├── stage-2.md   size & tier                                                      [step 6]
│   ├── stage-3.md   analyst fan-out                                                  [step 7]
│   ├── stage-3b.md  post-fan-out integrity check                                     [step 8]
│   ├── stage-4.md   cold verify                                                      [step 9]
│   ├── stage-5.md   agreement merge                                                  [step 10]
│   ├── stage-6.md   blind roll-up                                                    [step 11]
│   ├── stage-7.md   emit the distillate                                              [step 12]
│   ├── common.md    every dispatched agent, verbatim-included                        [step 13]
│   ├── analyst.md   role additions                                                   [step 14]
│   ├── verifier.md  role additions                                                   [step 15]
│   ├── merger.md    role additions                                                   [step 16]
│   └── node.md      role additions                                                   [step 17]
└── changes/initial-build/
    ├── 6-redteam-code.md             verbatim cold-review record                     [step 21]
    └── decisions.md                  append-only log of steps 1, 23, 24              [steps 23–24]
```

**Installed tree** — `~/.claude/skills/data-distiller/` [step 22]: `SKILL.md`, `METHODOLOGY.md`,
`stages/` only. Byte-identical to source, checked at step 23.

**Run output** — produced by the skill at runtime, not by this build, under `state.dir`
(`distillations/<slug>/` by default):

```
distillations/<slug>/
├── manifest.md                 item id / locus / bytes / sha256, + the uncovered set
├── decisions.md                append-only gate log (validations, retries, human overrides)
├── distillate.md               THE DELIVERABLE — ranked, cited, with coverage + gaps in the header
└── items/<item-id>/
    ├── status.md               the fixed content-free schema a blind node reads
    ├── findings-a1.md … -aN.md one per analyst, never read by a node
    ├── verified.md             every finding with its disposition, drops included
    └── merged.md               agreement-ranked survivors
```

---

## 6. Failure modes & contingencies

**6.1 — The destination directory is not empty (near-certain).** §0.2: the plan was written blind to
`Data-Distiller/`. *Contingency:* step 1 stops for a human before any write. *Assumption it rests
on:* that the executor actually runs `ls -A` before `mkdir`; the step is written imperatively for
that reason.

**6.2 — Analyst independence is lost.** Spawning analysts sequentially, or letting a later one read
an earlier's file, makes agreement meaningless while every count still looks healthy — the most
dangerous failure here, because it is invisible in the output. *Contingency:* single-batch dispatch
(step 7), distinct output paths, an explicit prohibition in `analyst.md`, and identical prompts.
*Residual risk I cannot close:* nothing mechanically proves a subagent did not read a sibling file.
Flagged as unchecked. A partial mitigation an executor may add: give analysts an agent type with no
Read access outside the corpus root, if the host supports scoping.

**6.3 — Agreement is measured but means less than it looks.** N analysts drawn from the same model
with the same prompt share priors; unanimous agreement on a wrong reading is the expected failure,
not an exotic one. *Contingency:* the README states this plainly (step 20), and the distillate ranks
by agreement without ever calling it confidence. *Not solvable within this method* — closing it would
need heterogeneous analysts (different models), which is worth recording as the obvious future
extension.

**6.4 — The verifier is not actually cold.** If it receives the analyst prompt or the brief's
rationale it inherits the framing it exists to challenge. *Contingency:* step 9 fixes its input set
to findings + corpus + off-limits, explicitly excluding the rest.

**6.5 — An analyst writes to the corpus.** Read-only is a prose rule and prose does not enforce
itself. *Contingency:* the stage-1 sha256 manifest and the step-8 re-check turn it into a detected
event; a mismatch invalidates the item's whole batch, not just the file.

**6.6 — The corpus changes between a run and its resume.** Resume would then merge findings about
two different corpora, silently. *Contingency:* stage-0 re-checks the manifest hashes before
trusting any prior state; a mismatch is a stop-for-human, with the options being restart-clean or
resume-only-unchanged-items.

**6.7 — The concurrency ceiling is exceeded.** *Contingency:* per-node batch cap + one subtree at a
time (§2.7). *Stated limitation:* no run-wide semaphore, so two concurrent invocations can jointly
exceed it. Recorded rather than papered over.

**6.8 — A fact is split across a chunk boundary and every analyst misses or misquotes it.**
*Contingency:* `sizing.chunk_overlap`, plus the `boundary` mark and the re-check against the full
item at stage 4. *Assumption:* that the true fact fits inside the overlap window; a fact spanning
more than `chunk_overlap` is still lost, which is why the config must set the overlap against the
corpus's actual record size, and why the notes section of the worked config must say so.

**6.9 — A stop-for-human is absorbed by the agent instead of reaching the human.** Both siblings
carry this as an explicit obligation under delegation (`Guarded_change/METHODOLOGY.md:208-232`).
*Contingency:* SKILL.md's stop-for-human section enumerates the set — **missing config; a dead
config path; an unexplained coverage shortfall at stage 1; an item that cannot be reduced below the
size threshold; a second failure of the same child; a corpus-hash mismatch on resume; a corpus
mutation detected at step 8** — and states that a subagent running this loop halts and returns the
question verbatim rather than self-answering.

**6.10 — Effort migrates into a test harness and the skill never ships.** The user's standing note
records this as the repeat failure of this project: a weekend and two prior attempts lost to
harnesses that kept failing review while zero skill files changed. *Contingency, adopted as a rule
of this plan:* one end-to-end acceptance test against the assembled skill (step 24), no
per-component behavioral harness; **count rebuilds of the test mechanism, and at three, stop building
and decide** whether the thing is isolation-testable at all.

**6.11 — Interpretation is emitted as fact anyway.** The single-locus test is a procedure, but a
determined analyst can write an interpretive claim with a plausible quote attached. *Contingency:*
the verifier applies the test to the *claim as stated* against the *locus alone*; step 12 forbids
any synthesis section in the distillate, which removes the natural home for interpretation.
*Residual:* an interpretive claim that happens to be single-locus-checkable survives. Flagged.

**6.12 — The router and the stage files drift apart.** Every rule stated in both SKILL.md and a
stage file is a drift candidate, and this repo has lost a day to exactly that. *Contingency:*
step 23 check (3) makes the table/file correspondence mechanical, and the SKILL.md self-check
section carries "SKILL ↔ METHODOLOGY ↔ stage-file consistency on every rule stated in more than one
place" as a standing criterion, copied from both siblings.

**6.13 — Stage-3b is a numbering oddity.** `stage-3b.md` breaks the plain integer sequence.
*Contingency:* step 8 explicitly permits folding it into `stage-3.md` as a section; what is
load-bearing is that the integrity check runs after every fan-out, not which file holds it.
Precedent for lettered stages exists (`Dragonfly/stages/stage-0a.md`, `stage-0b.md`).

---

## 7. Verification

### 7.1 — Structural criteria (mechanical, all gating)

| # | Criterion | How checked |
|---|---|---|
| V1 | All 15 source files from §5 exist at their stated paths | `ls` / `test -f` per path |
| V2 | `SKILL.md` starts with `---`, has exactly `name` and `description`, and `name` is `data-distiller` | read the first 5 lines |
| V3 | The install dir name equals the frontmatter `name` | `ls ~/.claude/skills/` |
| V4 | Installed tree == source for `SKILL.md`, `METHODOLOGY.md`, `stages/` | `diff -r`, empty output |
| V5 | Installed tree contains **no** `README.md`, config, or `changes/` | `ls ~/.claude/skills/data-distiller/` |
| V6 | Every `stages/…` path referenced in SKILL.md or METHODOLOGY.md resolves | `grep -o 'stages/[a-z0-9.-]*\.md'` piped to `test -f` |
| V7 | SKILL.md loop-table rows == `ls stages/stage-*.md` (both directions) | set comparison |
| V8 | METHODOLOGY contract key set == worked-config key set | key extraction + `diff` |
| V9 | Each of the five role files exists and each is dispatched by at least one stage file | `grep` for each role filename across `stages/stage-*.md` |
| V10 | No role file restates a rule from `common.md` | manual read of five short files against one; a duplicated normative sentence is a finding |

### 7.2 — Coverage criteria (each of the nine task properties is present and operative)

For each of P1–P9 in §1, name the file and section that implements it, and confirm the text there is
**operative** (an instruction an agent executes) rather than descriptive. The mapping table in §1 is
the checklist; a property present only in METHODOLOGY prose and absent from any stage or role file
**fails** — METHODOLOGY is explicitly not read to run a stage
(`Guarded_change/METHODOLOGY.md:10-11`), so a rule that lives only there does not run.

Two coverage checks worth calling out because they are the properties most easily faked:

- **P6 (blindness)** passes only if `node.md` contains an absolute prohibition on opening
  `merged.md` / `verified.md` / `findings-a*.md`, **and** `status.md`'s schema in `stage-6.md`
  contains no free-text field wider than the capped one-line mechanical `note:`.
- **P9 (facts, not interpretation)** passes only if the single-locus test appears as an executable
  procedure in `verifier.md`, not merely as an exhortation in `common.md`.

### 7.3 — The end-to-end acceptance test (the real done-criterion)

Invoke `data-distiller` with the step-19 worked config against this repo's own
`Guarded_change/changes/` + `Dragonfly/changes/` tree — a corpus that genuinely does not fit one
context window. Four criteria, all gating:

1. **It produces a distillate.** `distillations/<slug>/distillate.md` exists, is non-empty, and its
   header carries item count, coverage totals, and drop counts.
2. **Every citation resolves.** Sample 10 findings at random; for each, open the cited locus and
   confirm the quoted text is there verbatim. Any fabricated citation is a **blocker** — citations
   are the single guard the whole method rests on.
3. **Resume works.** Kill the run partway; re-invoke; confirm from `decisions.md` that items already
   marked `done` were **skipped**, not re-analyzed, and that the final distillate is equivalent to
   an uninterrupted run's.
4. **Blindness held.** Inspect the run's own transcripts/logs: no agent acting as a node opened a
   findings, verified, or merged file. If the host does not record enough to check this, it is
   reported as **unchecked**, not as passed — the honest failure here is claiming a safeguard that
   was never observed to operate.

**What this test is not.** It does not establish that the findings are *true*, only that they are
cited, verifiable, and reproducible across independent analysts. That is the method's actual claim
and the verification should not be written to imply more.

### 7.4 — Independent review

The build is not "done" on its own say-so: step 21's cold five-lens red-team must return with no
open blocker or major. Consistent with both siblings, where no AI artifact is accepted without an
independent challenge.

---

## 8. What I could not check

- **The contents of `Data-Distiller/`** — off-limits by instruction. Every claim in this plan about
  what that directory should contain is derived from the task and the siblings, never compared
  against what is there. §6.1 is the contingency.
- **Whether the host supports scoping a subagent's Read access to a directory** (§6.2's stronger
  mitigation). I did not test it; it is offered as an option, not asserted as available.
- **Whether the step-19 corpus exceeds one context window** — I verified it is roughly 130 markdown
  files across ~20 run folders by `find`, which strongly suggests it, but I did not sum the bytes.
  The executor should confirm before relying on it as the acceptance corpus; if it turns out to fit,
  the test does not exercise stages 2 and 6 and a larger corpus must be substituted.
- **The exact `description` wording's trigger behavior.** Whether the host reliably surfaces the
  skill on a distillation-shaped request is an empirical property of the matcher, not of this file.

---

## 9. Note on the granularity floor

The floor I was given — *one file created or one coherent edit to one file, with the content that
goes in it specified* — fits this task well and I applied it as given. Twenty-four steps, each
naming one file and specifying what goes in it. Two places where I deliberately stopped at the
floor rather than below it: I specify each stage file's **sections and operative rules** but not its
sentences, and I specify the `description` frontmatter's **content** but not its final wording — a
competent practitioner writes both without further planning, and decomposing them further would be
planning how to grip the handle.
