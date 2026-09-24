# Plan — the Data-Distiller skill

*Leaf plan. Complete and standalone. Granularity floor applied: each step is one file created (or
one coherent edit to one file) with the content that goes in it specified.*

**Sources opened and used as authority for every house-shape claim below:**
`/home/zero/Desktop/claude-code-skills/Guarded_change/{SKILL.md, METHODOLOGY.md, README.md,
guarded-change.companion.md, stages/charter.md, stages/stage-3.md}` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/{SKILL.md, METHODOLOGY.md, README.md,
dragonfly.companion.md}`, plus `ls`/`diff` of `~/.claude/skills/{dragonfly,guarded-change}/`.

**Compliance with the off-limits instruction:** `/home/zero/Desktop/claude-code-skills/Data-Distiller/`
was never read, listed or grepped. Its *existence* is visible in the top-level `ls` of the repo root
and its installed twin `~/.claude/skills/data-distiller/` is visible in the `ls` of the skills
directory; neither was opened. Everything below is derived from the two sibling skills.

---

## 1. Problem / intent

**What this node plans.** The whole build of the Data-Distiller skill: every file that constitutes
it, what goes in each, the order they are written in, where they land, how it is installed, and how
"done" is checked. There is no sibling slice — this leaf owns the task end to end.

**What is being built.** A Claude Code skill named `data-distiller`: a directory of markdown prompt
files, invokable by name, that implements a cold multi-agent method for extracting trustworthy,
source-cited **factual** findings from a corpus too large for one context window. The nine defining
properties from the task, each of which must land in a named file (the mapping is §3 and the steps
in §4):

| # | Property | Lands in |
|---|---|---|
| P1 | Decompose the corpus into analyzable items | `stages/stage-1.md` |
| P2 | Size each item; pick a per-item strategy when it does not fit | `stages/stage-2.md` |
| P3 | N independent cold analysts per item, read-only, citation per finding | `stages/stage-3.md` + `agents/analyst.md` |
| P4 | Cold verification pass re-checking every citation; drop the unverifiable | `stages/stage-4.md` + `agents/verifier.md` |
| P5 | Merge ranking survivors by independent-analyst agreement | `stages/stage-5.md` + `agents/merger.md` |
| P6 | Blind roll-up — coordinator reads only terse per-child status | `stages/stage-6.md` + `agents/node.md` |
| P7 | Per-corpus Layer-2 config supplies corpus specifics; core stays agnostic | `METHODOLOGY.md` config contract + `data-distiller.companion.md` |
| P8 | Restart and resume from on-disk state | `stages/state.md` |
| P9 | Facts, not interpretation | `agents/common.md` (read by every dispatched agent) |

**Why the skill has to exist as files rather than as one prompt.** Every property above is a
constraint on an agent this skill *dispatches*, not on the agent that invokes it. The dispatched
agent only obeys a rule that is in the prompt it was handed. That is the whole reason for the
per-role file split in §2.

---

## 2. Approach

### 2.1 Copy the house shape, because it is the installed contract

Both siblings are the same five-part artifact, and the install `diff` proves which parts are the
*skill* and which are repo furniture:

- `SKILL.md` — YAML frontmatter (`name`, `description` — those two keys and no others appear in
  either sibling: `Guarded_change/SKILL.md:1-4`, `Dragonfly/SKILL.md:1-4`) then a **router**: a
  purpose paragraph, `## Inputs`, `## Loop` (a table whose every row points at a file under
  `stages/`), a "most important gate" paragraph, `## Stop-for-human`, `## Self-check / dogfooding`.
  86 lines (guarded-change) / 95 lines (dragonfly).
- `METHODOLOGY.md` — the orientation/reference spec, explicitly *"opened for orientation and config
  setup — not to run a stage"* (`Guarded_change/METHODOLOGY.md:11`). Sections: why it exists, the
  loop as an ASCII diagram, a stage-index table, the two layers, the Layer-2 config contract, what a
  run produces, trigger, human-in-the-loop. 180–232 lines.
- `stages/*.md` — one file per stage, 12–200 lines each, plus a shared file
  (`stages/charter.md`) holding the text handed **verbatim** to dispatched cold agents.
- `<name>.companion.md` — a worked Layer-2 config for one real project.
- `README.md` — human-facing: why, the loop, the two layers, how to adopt.

**Install is a copy of a subset.** `diff -rq ~/.claude/skills/dragonfly/
/home/zero/Desktop/claude-code-skills/Dragonfly/` reports exactly three things present only in the
source: `changes/`, `dragonfly.companion.md`, `README.md`. So the installed skill is
`SKILL.md` + `METHODOLOGY.md` + `stages/` and nothing else, and `Dragonfly/README.md:106-108` states
the install procedure in those terms. The directory name must equal the frontmatter `name`:
`Dragonfly/` → `~/.claude/skills/dragonfly/` → `name: dragonfly`; `Guarded_change/` →
`~/.claude/skills/guarded-change/` → `name: guarded-change`. Therefore `Data-Distiller/` →
`~/.claude/skills/data-distiller/` → `name: data-distiller`.

**The rule that governs where a rule goes.** Both siblings state it: orientation in METHODOLOGY, the
**operative** form written-in-full in the stage file that enforces it
(`Guarded_change/METHODOLOGY.md:61-63`, `Dragonfly/METHODOLOGY.md:66-68`). This plan follows it
without exception, because the alternative — a rule stated only in METHODOLOGY — is a rule in a file
the acting agent was told not to open.

### 2.2 Split the dispatched-agent prompts by role, in `agents/`

Data-Distiller dispatches **four distinct kinds of agent** (analyst, verifier, merger, node). A
single shared charter of the guarded-change kind does not fit: `stages/charter.md` works for
guarded-change because both its consumers (stages 3 and 6) are the *same* role — a red-team reviewer
— differing only by what they review. Here the roles differ in their core duty and, critically, in
what they are permitted to read. A monolith would spend every analyst's context on merge rules it
cannot act on, and — the worse failure — would let the node's file read the findings-handling
sections, blurring the one boundary P6 exists to defend.

So: **`agents/common.md` read verbatim by every dispatched agent, plus one file per role, additions
only, never restating a common rule.** If a role file needs to *modify* a common rule, that rule was
never common and moves down into the roles. The live precedent for this exact shape is the Architect
skill's own `stages/` directory (`common.md` + `leaf.md`, `node.md`, `divider.md`, `combiner.md`,
`redteam*.md`), which is the file set this leaf agent was itself dispatched with.

**Alternatives considered and rejected:**
- *One `stages/charter.md`, guarded-change style.* Rejected above: four unlike roles, and it leaks
  findings-handling text into the node's prompt.
- *Put role prompts inline in the stage files.* Rejected: a stage file is read by the **runner**, an
  agent prompt is handed to a **dispatched agent**. Inlining means the runner must extract the right
  span by eye, and the "verbatim" in "handed verbatim" stops being mechanically checkable. Both
  siblings keep the verbatim-dispatched text in its own file for this reason
  (`Guarded_change/stages/charter.md:1-6`: *"This is the ONE copy … given to the reviewer verbatim"*).
- *No `agents/` directory; put the role files in `stages/`.* Tenable — it is what Architect does —
  but it puts two different kinds of file (runner procedure vs. dispatched prompt) in one directory
  with no marker distinguishing them, and this skill has seven of the first and five of the second.
  A separate `agents/` makes "did the node's prompt acquire a findings-reading permission?" a
  one-directory question. **This is a divergence from the two named siblings and is called out as
  such** so a reviewer attacks it rather than assuming it; it costs one extra directory in the
  install copy and nothing else.

### 2.3 The pipeline

```
0  CONFIG      load + validate the Layer-2 corpus config; resume-scan existing state
1  DECOMPOSE   enumerate the corpus into analyzable items with stable IDs   → manifest
2  SIZE/TIER   measure each item; assign tier A (fits) / B (split) / C (declared partial)
3  ANALYZE     per item: N independent cold analysts, read-only, citation per finding
4  VERIFY      per item: a cold verifier re-checks every citation; drops the unverifiable
5  MERGE       cluster survivors; rank by count of independent analysts that agreed
6  ROLL UP     the node reads ONLY a terse per-child status line; assembles the report
```

Stages 3–5 run per item and are the unit of resume. Stage 6 is the only place a coordinator acts,
and it is blind by construction. A tier-B item recurses: the item becomes a sub-corpus and re-enters
at stage 1 with its own node, which is why P6's blindness has to hold at every level and not only at
the top.

**The most important gate is stage 4**, and the skill must say so where the siblings say it
(`Guarded_change/SKILL.md:47-50`, `Dragonfly/SKILL.md:53-56`). Everything downstream of an
unverified citation is a confident fabrication carrying a file path, which is *worse* than no
finding — it is the failure the whole method exists to prevent, and stage 4 is the cheapest place to
kill it.

### 2.4 Independence is a property of what agents are handed, not of their instructions

Three mechanisms, each of which must be a stated hard rule in a named file, because "be independent"
is not enforceable:

1. **Each analyst is handed the raw item and nothing else** — never another analyst's output, never
   a summary, never the run's report-so-far. Agreement between analysts is then evidence; agreement
   between agents that read each other is not.
2. **The verifier never sees who produced a finding**, only the claim and its citation — so it
   cannot weight by author.
3. **The node reads only `status/<item-id>.txt`**, a fixed-field line containing no claim text. This
   is mechanically checkable after a run (§7), which is the point: a blindness rule that can only be
   audited by trusting the node's self-report is not a control.

---

## 3. Interfaces & seams

**Consumes:**
- **The distillation request** — from the user, optionally narrowed by a `question` in the config.
- **A Layer-2 corpus config** (`data-distiller.<corpus>.md`), located the way the siblings locate
  theirs (`Guarded_change/SKILL.md:16-18`, `Dragonfly/SKILL.md:17-19`): look for
  `data-distiller.*.{md,yaml}` in or near the working dir; if absent, ask for it or help author it
  against the contract in `METHODOLOGY.md`. **Never invent corpus specifics.**
- **The corpus itself**, read-only, at the config's `root`.

**Emits:**
- A run folder `runs/<slug>/` (layout in §5) whose terminal artifact is `report.md`: agreement-ranked
  factual findings, every one carrying a citation that resolves against the corpus.
- `decisions.md` — the append-only log (path validation result, tier assignments with reasons, human
  overrides with a name, degraded-coverage acceptances). Both siblings make this the audit trail
  *and* the memory a resumed run reads (`Guarded_change/METHODOLOGY.md:175-180`,
  `Dragonfly/METHODOLOGY.md:156-157`).

**Seams to name explicitly, because they are where this can silently break:**

| Seam | Contract |
|---|---|
| runner → analyst | `agents/common.md` + `agents/analyst.md` verbatim, + the item path, + the finding-record format. Nothing else. |
| analyst → verifier | `raw/<item-id>/analyst-<k>.md`, finding records only, author identity stripped before the verifier sees them. |
| verifier → merger | `verified/<item-id>.md`, each record carrying `verified` / `unverifiable` / `misquoted`. |
| merger → node | `status/<item-id>.txt` **only** — one fixed-field line, no claim text. `merged/<item-id>.md` exists but the node may not open it. |
| skill → human | `report.md` + the stop-for-human points (§6). |
| source → install | `~/.claude/skills/data-distiller/` must be byte-identical to the source subset (§7). |

**Seam to the sibling skills:** none at runtime. Data-Distiller neither calls nor is called by
guarded-change or dragonfly. It borrows their *shape* only. (Dragonfly declares a live handoff to
guarded-change at `Dragonfly/METHODOLOGY.md:13-16`; this skill deliberately declares no such
coupling, so that no reviewer infers one.)

---

## 4. Steps

**Ordering principle:** a file is written after everything it must cite by name. So the vocabulary
(METHODOLOGY) comes first; the state contract next, because stages write state; the dispatched
prompts next, because stage files name them; the stage files next; `SKILL.md` **last of the core**,
because its router table must list files that already exist; then the config example, the README, the
install, and the checks.

**Step 1 — Write `Data-Distiller/METHODOLOGY.md`.** Create the directory tree
(`Data-Distiller/stages/`, `Data-Distiller/agents/`) as part of this step. Sections, in the sibling
order (`Guarded_change/METHODOLOGY.md`, `Dragonfly/METHODOLOGY.md`): (a) title + a purpose paragraph
that names this file the orientation/reference spec and says the operative per-stage rules live in
`stages/`; (b) **Why this exists** — the failure modes it defends against, one structural defense
each: a single reader's priors steering the result → N independent cold analysts; confident
uncited assertion → citation-per-finding + the stage-4 verify; a coordinator's expectations steering
its children → the blind roll-up; a corpus that does not fit → decompose + tier; a long run lost to a
crash or a compaction → on-disk state; interpretation smuggled in as fact → the facts-only rule; (c)
**The pipeline** as the 0–6 ASCII diagram from §2.3; (d) a **stage index table** mapping each stage
to its file and one line of what it covers; (e) **The two layers** — Layer 1 agnostic core
(this doc + `SKILL.md` + `stages/` + `agents/`), Layer 2 the per-corpus config, worded on
`Guarded_change/METHODOLOGY.md:88-99`; (f) **The config contract (Layer 2)** — the YAML block and
rules given in Step 16 below, stated here as the contract; (g) **What a run produces** — the `runs/<slug>/`
layout from §5 verbatim; (h) **Trigger** — explicit invocation plus a proactive-suggestion rule with
a precision bar, modelled on `Dragonfly/METHODOLOGY.md:161-168`: fire on "sift/audit/distill a body
of material too large to read in one pass", not on every mention of a log file; (i)
**Human-in-the-loop** — the stop conditions from §6, with the note that under delegation these are
stops for the actual human, not for the agent running the loop
(`Guarded_change/METHODOLOGY.md:208-231`).

**Step 2 — Write `Data-Distiller/stages/state.md`** — the on-disk state and resume contract (P8).
Content: (a) the `runs/<slug>/` layout from §5; (b) the **unit of work** is one item at one stage —
`<item-id>@<stage>`; (c) `status.tsv` is append-only, one row per completed unit:
`item-id <TAB> stage <TAB> done|failed|partial <TAB> output-path <TAB> ISO-8601-timestamp`;
(d) the **write-then-record** rule: the output file is written to `<path>.tmp` and `mv`'d into place
first, and only then is the `status.tsv` row appended — so a crash can leave a finished file with no
row (harmless, the unit re-runs) but never a row with no file (poisonous, the unit is skipped and
its output is missing); (e) the **resume rule**: on start, read `status.tsv`, treat every unit with a
`done` row *whose output path exists* as complete and skip it, re-run everything else — verifying the
file's existence rather than trusting the row; (f) the rule that state lives in **files, not context**,
with the reason stated: the run is expected to outlive a session, a compaction, or a crash, and
in-context state does not (`Dragonfly/METHODOLOGY.md:135-136` makes the same argument for its
ledgers); (g) `decisions.md` is append-only and is what a resumed run reads to recover tier choices
and human overrides.

**Step 3 — Write `Data-Distiller/agents/common.md`** — the core every dispatched agent gets
verbatim. Content, in this order: (a) **you are a cold, independent agent** — no shared context with
whoever produced your input and none with the siblings dispatched alongside you; do not guess what
they will say and do not hedge toward a middle, because convergence is the only evidence the merge
has; (b) **you are read-only over the corpus** — you may read, you may not write, move, rename or
delete anything under the corpus root, and you may not read anything matching the config's
`off_limits`; (c) **facts, not interpretation (P9)** — the operative test, stated as a test and not
as an exhortation: *a finding is admissible only if a reader holding the cited locus alone can
confirm or refute it.* "Session 12 records three failed auth attempts at 14:02" passes; "auth was
unreliable" does not, because no single locus settles it. Speculation, causal attribution,
aggregation across loci, and recommendations are all out of scope; (d) **cite or it does not count**
— every finding carries `source` (path + line or record locator) and a verbatim `quote` of at most
25 words; (e) **the finding-record format** (Step 4 gives it in full — stated once, here, since all
four roles read or write it); (f) **flag what you could not check** rather than accepting it
silently; (g) **your output is a file** — write it to the path your caller named and return that
path plus a two-line summary; nothing else you say is read.

**Step 4 — Write `Data-Distiller/agents/analyst.md`** (P3). Additions only, on top of Step 3.
Content: (a) you are one of N analysts on one item; you have not seen and will not see the others'
output, and you must not seek it — if you find another analyst's file, do not open it; (b) your input
is exactly one item plus the optional `question`; (c) read the item completely before writing any
finding, and if it does not fit, say so at the head of your output and state what fraction you
covered rather than silently truncating; (d) the finding record, in full:

```
- id: <item-id>.a<k>.<n>
  claim: <one sentence, checkable against the cited locus alone>
  source: <path>:<line-or-record-locator>
  quote: "<≤25 words, verbatim from the source>"
```

(e) one claim per record — a record with two claims cannot be verified or agreement-counted;
(f) prefer fewer, checkable findings to many hedged ones: you are graded on precision, not count
(`Guarded_change/stages/charter.md:103` states this for its reviewers); (g) an empty finding set is
a valid result and must be stated explicitly, not padded.

**Step 5 — Write `Data-Distiller/agents/verifier.md`** (P4). Additions only. Content: (a) you are
cold to the analysts and are given finding records **with author identity stripped** — do not
attempt to infer it; (b) for **every** record: open the cited `source`, locate the locator, and
compare the `quote` against what is actually there; (c) emit exactly one verdict per record —
`verified` (locus exists, quote matches, claim is supported by it), `misquoted` (locus exists, quote
does not match it), `unverifiable` (locus does not exist or cannot be resolved); (d) **the drop
rule:** anything not `verified` does not proceed; record it with its verdict in the verifier's own
output so the drop is auditable, but it leaves the pipeline; (e) a claim the locus does not actually
support is `misquoted` even when the quote is accurate — the citation must support the *claim*, not
merely exist; (f) you check citations; you do not add findings, rewrite claims, or judge importance;
(g) sampling is prohibited — every record, or the pass is un-run.

**Step 6 — Write `Data-Distiller/agents/merger.md`** (P5). Additions only. Content: (a) your input
is the `verified` records for one item from all N analysts, and only those; (b) **cluster** records
that make the same factual claim, using the cited locus as the tiebreak — same locus and equivalent
claim is one cluster; different loci are different findings even when the wording matches, because
the agreement being counted is agreement about *the corpus*, not about phrasing; (c) **the agreement
count is the number of distinct analysts in the cluster**, never the number of records — one analyst
stating a thing three times is agreement of one; (d) rank clusters by agreement count descending,
then by number of distinct supporting loci; (e) a cluster of one is **kept and labelled
`agreement: 1`**, not dropped — the ranking expresses confidence, it does not filter, and a single
analyst's verified finding is still a verified finding; (f) merged record format: `claim`,
`agreement: <n>/<N>`, `analysts: [a1, a3]`, `sources: [...]`; (g) you do not re-word claims beyond
choosing one cluster member's wording verbatim as the representative, and you name which.

**Step 7 — Write `Data-Distiller/agents/node.md`** (P6) — the blind coordinator. Additions only.
Content: (a) **you never read findings.** You may read `manifest.md`, `items.tsv`, `status.tsv`, and
`status/<item-id>.txt`. You may **not** open anything under `raw/`, `verified/`, or `merged/`, and
you may not ask a child what it found; (b) the reason, stated so it survives an agent's urge to be
helpful: if you knew what the children were finding, your dispatch of the remaining children would
be shaped by it, and their agreement would stop being independent evidence — **your ignorance is the
control**; (c) the status line is the whole interface, fixed fields:
`<item-id> | done|failed|partial | analysts:<n>/<N> | findings:<n> | max-agreement:<n> | output:<path>`
— no claim text, no topic, no summary, and a status line containing any is a defect to report, not
to read; (d) your job is dispatch, concurrency (never exceed the config's `max_parallel`), retry of
`failed` units once, and assembly; (e) **assembly is concatenation by reference, not summary**:
`report.md` is built from the manifest and the per-item `merged/` files **by path**, in manifest
order, with a header block of counts — you emit the instruction to include them, you do not read
them to paraphrase them; (f) if you cannot complete without reading a finding, that is a
**stop-for-human**, not a licence.

**Step 8 — Write `Data-Distiller/stages/stage-0.md`** — config load, path validation, resume scan.
Content: (a) locate the Layer-2 config as in §3; **if none exists, stop and ask** — do not invent
corpus specifics (`Guarded_change/SKILL.md:16-19`, `Dragonfly/SKILL.md:17-21`); (b) **validate every
path mechanically before any agent is dispatched** — `root`, every `off_limits` glob's parent, and
the `state.dir` — checking existence and readability, and record the result in `decisions.md`;
dead and unresolvable → stop for the human; adaptable → adapt, record, proceed
(`Dragonfly/METHODOLOGY.md:135-137`, `Guarded_change/stages/stage-3.md:159-165`). State the reason:
an agent handed a dead path silently degrades to reasoning without the source, which is the founding
failure; (c) resolve `analysts.N` (default 3) and `concurrency.max_parallel`, and refuse to start if
neither the config nor the default yields a value; (d) run the **resume scan** per `stages/state.md`
and report how many units are being skipped; (e) create `runs/<slug>/` if new.

**Step 9 — Write `Data-Distiller/stages/stage-1.md`** — decompose (P1). Content: (a) run the
config's `item.enumerate` procedure to list items; (b) assign each a **stable ID** derived from its
path (not from enumeration order), so a re-run or a resume after the corpus grows does not renumber
existing items and invalidate `status.tsv`; (c) write `items.tsv` (`item-id`, `path`) and the
human-readable `manifest.md`; (d) apply `off_limits` **here**, at enumeration — an excluded path
never becomes an item, so no analyst is ever handed one — and record the exclusion count in
`decisions.md`; (e) failure: `item.enumerate` returns zero items → stop for the human, the config's
item definition is wrong; (f) the runner does not decide what an item is — that is Layer 2.

**Step 10 — Write `Data-Distiller/stages/stage-2.md`** — size and tier (P2). Content: (a) run the
config's `budget.measure` on each item; (b) assign a tier and record it with its reason in
`decisions.md`: **A** — under `budget.item_max`, analyze whole; **B** — over it and splittable by
the config's item definition applied one level down, so the item becomes a sub-corpus and re-enters
at stage 1 with its own node and its own blind roll-up; **C** — over it and *not* splittable
(one indivisible record), which is handled by **declared partial coverage**: analyze a stated
portion and record the coverage statement in the manifest and in every downstream artifact for that
item; (c) the hard rule: **coverage is declared, never silently reduced** — a partial item that
does not say it is partial produces findings that read as exhaustive and are not; (d) write the tier
into `items.tsv`; (e) failure: `budget.measure` unavailable → stop for the human rather than guessing
sizes, because a mis-sized item is analyzed by an agent that runs out of context mid-item.

**Step 11 — Write `Data-Distiller/stages/stage-3.md`** — analyze (P3). Content: (a) for each
tier-A item and each leaf of a tier-B item, dispatch **N** cold agents, each given
`agents/common.md` + `agents/analyst.md` **verbatim**, the item path, the optional `question`, and
its output path `raw/<item-id>/analyst-<k>.md`; (b) **each analyst gets the item, never another
analyst's output and never the run's state** — the operative statement of §2.4(1); (c) respect
`max_parallel`, batching when N × live items exceeds it; (d) an analyst that returns no file, or a
file with zero parsable records, is re-dispatched **once**; a second failure marks the unit `failed`
in `status.tsv` and the item proceeds with the analysts it has, with the reduced N recorded — the
item is degraded, not silently normal; (e) append a `status.tsv` row per analyst unit per
`stages/state.md`; (f) the runner does not read the findings either — it counts records and moves on.

**Step 12 — Write `Data-Distiller/stages/stage-4.md`** — verify (P4), and mark it in this file as
**the most important gate**, with the §2.3 reason. Content: (a) per item, dispatch **one cold
verifier** given `agents/common.md` + `agents/verifier.md` verbatim, the pooled records from all N
analysts **with the analyst identifier stripped from each record**, and read access to the corpus;
(b) the verifier writes `verified/<item-id>.md` with a verdict per record; (c) only `verified`
records proceed to stage 5; (d) a verifier that returns verdicts for fewer records than it was given
is **un-run** and re-dispatched — a partial verification is indistinguishable from a lenient one;
(e) if a re-dispatch also comes back partial, stop for the human; (f) record per item in
`decisions.md`: records in, verified, misquoted, unverifiable — the drop rate is the run's health
signal, and a rate near zero deserves suspicion as much as a rate near one.

**Step 13 — Write `Data-Distiller/stages/stage-5.md`** — merge and agreement-rank (P5). Content:
(a) per item, dispatch one merger given `agents/common.md` + `agents/merger.md` verbatim and the
item's verified records; (b) it writes `merged/<item-id>.md`; (c) **the runner then writes
`status/<item-id>.txt`** — the single fixed-field line of Step 7(c) — from the merger's counts,
and this is the only file stage 6 may read for that item; (d) state the reason the status line is
written **here, by the runner, from counts** rather than composed by the node or by the merger: it is
the blindness boundary, and it is generated from numbers so that no claim text can travel through it;
(e) append the `status.tsv` row.

**Step 14 — Write `Data-Distiller/stages/stage-6.md`** — blind roll-up (P6). Content: (a) dispatch
the node with `agents/common.md` + `agents/node.md` verbatim, `manifest.md`, `items.tsv`, and the
`status/` directory — **and no other path**; (b) the node assembles `report.md`: a header block
(corpus, item counts by tier and state, N, total merged findings, degraded/partial items named), then
per item in manifest order the item ID, its status line, and an **include-by-path reference** to
`merged/<item-id>.md`; (c) the runner performs the inclusion, expanding the references after the node
returns — so the merged text reaches the report without passing through the node's context; (d) for
a tier-B sub-corpus, its own node rolls up its leaves and emits a single status line upward, so the
blindness holds at every level; (e) an item marked `failed` or `partial` appears in the report with
that state — a report that silently omits what it could not distill overstates its own coverage.

**Step 15 — Write `Data-Distiller/SKILL.md`** — the router, written now that every file it names
exists. Content: (a) YAML frontmatter, exactly two keys, matching the sibling shape
(`Guarded_change/SKILL.md:1-4`): `name: data-distiller`, and a `description` that states what it is
(a cold multi-agent method for extracting source-cited facts from a corpus too large for one
context), when to use it (distilling a large body of material into verifiable facts, not
interpretation), that corpus specifics come from a per-corpus Layer-2 config, and a proactive-suggest
clause with the precision bar from Step 1(h); (b) a purpose paragraph naming this file the **router**
and pointing at `METHODOLOGY.md` for orientation and the config contract; (c) `## Inputs` — the
distillation request and the Layer-2 config, with the never-invent rule and the validate-paths rule;
(d) `## Pipeline` — the table, one row per stage, each row `# | one-line purpose | → stages/stage-N.md`,
with the agent-file column for the stages that dispatch (`+ agents/analyst.md` etc.);
(e) the "most important gate is stage 4" paragraph; (f) `## The four hard rules` — read-only
analysts, citation-per-finding, verify-before-merge, node-never-reads-findings — each one sentence,
each pointing at the file that states it operatively; (g) `## Stop-for-human` — the §6 list;
(h) `## Self-check / dogfooding` — these files are **prompts**, so a non-trivial edit takes the full
guarded-change loop, and the standing criteria are live-copy == source-copy (`diff`), SKILL ↔
METHODOLOGY ↔ stage-file ↔ agent-file consistency on every rule stated in more than one place, and
behaviour-preservation for anything moved or removed (`Guarded_change/SKILL.md:76-85`,
`Dragonfly/SKILL.md:84-94`).

**Step 16 — Write `Data-Distiller/data-distiller.companion.md`** — the worked Layer-2 config,
modelled on `Guarded_change/guarded-change.companion.md` and `Dragonfly/dragonfly.companion.md`
(both are: a title naming the project, a pointer to the contract in the installed METHODOLOGY, one
fenced YAML block with inline comments, then a `## Notes specific to this project` section). The
YAML block:

```yaml
corpus: <name>

root: <path to the corpus root>          # everything below is read-only

item:
  definition: <what ONE analyzable item is here, e.g. "one session transcript = one .jsonl file">
  enumerate: <command or procedure listing items, one path per line>

off_limits:                              # never enumerated, never read
  - <glob>

budget:
  item_max: <size above which an item must be tiered>
  measure: <command reporting one item's size in the same unit>

analysts:
  N: 3                                   # independent cold analysts per item

concurrency:
  max_parallel: <int>                    # ceiling on simultaneously-running agents

question: |                              # OPTIONAL — narrows the distillation
  <what facts are being sought; omit for "all checkable facts">

state:
  dir: "runs/<slug>/"
```

State the contract rules alongside it: `root`, `item`, `budget` and `state.dir` are **required**;
`N` defaults to 3 and `off_limits` to empty; every path is validated at stage 0, not assumed;
`off_limits` is enforced at enumeration (stage 1), so it is a property of the manifest and not a
promise about agent behaviour; and — the load-bearing one — **the config is the only place corpus
specifics live**; the core knows nothing about any corpus. Fill the block for one real corpus as a
worked example and write the `## Notes` section for it.

**Step 17 — Write `Data-Distiller/README.md`** — human-facing, on the `Dragonfly/README.md`
skeleton: TL;DR (what / why / three ways to use it); **the failures it guards against** with the
structural defense for each (the §Step-1(b) list, written for a human); the pipeline diagram; how
it's structured (two layers, and the `stages/` vs `agents/` split with its reason); **Adopting it**
— copy `SKILL.md`, `METHODOLOGY.md`, `stages/` and `agents/` into `~/.claude/skills/data-distiller/`,
write a Layer-2 config from the companion, invoke it; a **Files** table; and a short
relationship-to-siblings note stating there is **no runtime coupling** to guarded-change or
dragonfly, only a shared shape.

**Step 18 — Install: copy the skill subset to `~/.claude/skills/data-distiller/`.** Copy exactly
`SKILL.md`, `METHODOLOGY.md`, `stages/` and `agents/`. Do **not** copy `README.md`,
`data-distiller.companion.md`, or any run folder — the `diff -rq` of the installed dragonfly against
its source shows precisely these three classes are source-only, and the same split applies here.

**Step 19 — Run the mechanical conformance checks** and fix what they surface. Each is a command,
and each must pass: (a) `diff -rq` the four installed items against their sources — zero
differences; (b) the frontmatter of the installed `SKILL.md` parses as YAML, has exactly `name` and
`description`, and `name` equals the installed directory name; (c) every `stages/…` and `agents/…`
path mentioned in `SKILL.md` and `METHODOLOGY.md` resolves to an existing file — grep the paths out
and `test -f` each; (d) every role file under `agents/` is additions-only: grep each rule sentence of
`agents/common.md` against the four role files, expecting zero substantive restatements;
(e) `agents/node.md` contains no permission to read `raw/`, `verified/` or `merged/` — grep those
three tokens and check every hit is a prohibition.

**Step 20 — Run one end-to-end acceptance test on a real corpus** that does not fit a single
context window, with a Layer-2 config written for it, and check the six criteria in §7. Prefer this
one assembled run over a set of per-component behavioural micro-tests: the properties being checked
(independence, blindness, resume) are properties of the assembled pipeline, and a per-component
harness for agent behaviour costs more to make trustworthy than the thing it measures. Fix the first
link in the chain that breaks and re-run.

---

## 5. Outputs & artifacts, with their locations

**The skill, in the repo** (source of truth), under
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`:

```
SKILL.md                      router + YAML frontmatter (name, description)   [Step 15]
METHODOLOGY.md                orientation/reference spec + config contract    [Step 1]
README.md                     human-facing why + how to adopt                 [Step 17]
data-distiller.companion.md   worked Layer-2 config                           [Step 16]
stages/state.md               on-disk state + resume contract                 [Step 2]
stages/stage-0.md             config load, path validation, resume scan       [Step 8]
stages/stage-1.md             decompose → items + manifest                    [Step 9]
stages/stage-2.md             size + tier (A / B / C)                         [Step 10]
stages/stage-3.md             analyze: N cold analysts per item               [Step 11]
stages/stage-4.md             verify: re-check every citation (the gate)      [Step 12]
stages/stage-5.md             merge + agreement-rank; write the status line   [Step 13]
stages/stage-6.md             blind roll-up → report.md                       [Step 14]
agents/common.md              read verbatim by every dispatched agent         [Step 3]
agents/analyst.md             analyst role, additions only                    [Step 4]
agents/verifier.md            verifier role, additions only                   [Step 5]
agents/merger.md              merger role, additions only                     [Step 6]
agents/node.md                blind coordinator role, additions only          [Step 7]
```

**The skill, installed** at `~/.claude/skills/data-distiller/`: `SKILL.md`, `METHODOLOGY.md`,
`stages/`, `agents/` — and nothing else [Step 18].

**What a run produces**, under the config's `state.dir` (e.g. `runs/<slug>/`):

```
manifest.md              items, sizes, tiers, coverage statements
items.tsv                item-id <TAB> path <TAB> size <TAB> tier
status.tsv               append-only resume ledger: item-id, stage, state, output, timestamp
raw/<item-id>/analyst-<k>.md    one file per analyst per item — findings with citations
verified/<item-id>.md    per-record verdicts: verified | misquoted | unverifiable
merged/<item-id>.md      agreement-ranked surviving findings
status/<item-id>.txt     ONE fixed-field line — the only thing the node may read
report.md                the blind roll-up
decisions.md             append-only: path validation, tier reasons, degraded units, overrides
```

---

## 6. Failure modes & contingencies

| # | Assumption / failure | How it fails | Contingency |
|---|---|---|---|
| F1 | A Layer-2 config exists | Absent → the runner invents an item definition and distills the wrong units | Stage 0 stops and asks, or helps author one against the contract. Never invent corpus specifics — both siblings state this rule (`Guarded_change/SKILL.md:16-19`, `Dragonfly/SKILL.md:17-21`) |
| F2 | Config paths resolve | A dead `root` → agents produce findings from reasoning alone, with plausible paths | Stage 0 validates mechanically before any dispatch; record in `decisions.md`; dead+unresolvable → stop |
| F3 | An item fits an analyst's context | Tier-A misjudged → the analyst truncates silently and its findings read as exhaustive | Stage 2 sizes every item; the analyst prompt (Step 4c) requires a coverage statement when it cannot read the whole item; tier C makes partial coverage explicit in the manifest and the report |
| F4 | Analysts are independent | They converge because they read the same prior summary, or one reads another's file | Each is handed the raw item only (Step 11b); `agents/analyst.md` forbids opening another analyst's file (Step 4a). If independence is compromised, the agreement count is meaningless — so this is a correctness property, not hygiene |
| F5 | Citations are real | A fabricated `file:line` sails through and the whole method's guarantee is void | Stage 4 checks **every** record against the corpus; sampling is prohibited (Step 5g); non-`verified` records are dropped |
| F6 | The verifier is thorough | It returns fewer verdicts than records, or rubber-stamps | Count-in must equal count-out or the pass is un-run and re-dispatched (Step 12d); the per-item drop rate is logged, and a near-zero rate is a suspicion trigger |
| F7 | The node stays blind | A status line carries claim text, or the node opens `merged/` "to write a better summary" | The status line is generated by the **runner from counts** (Step 13c-d), not composed by an agent; `agents/node.md` names the three forbidden directories; §7(4) audits the node's actual reads after the run |
| F8 | The run completes in one session | Crash, context exhaustion, or a compaction mid-corpus | `stages/state.md`: file-based state, write-then-record ordering, resume verifies the output file exists rather than trusting the ledger row |
| F9 | A `status.tsv` row implies its output exists | A crash between `mv` and append, or the reverse | The ordering in Step 2(d) makes only the harmless direction possible, and the resume rule re-checks existence anyway |
| F10 | An analyst returns usable output | Empty file, unparsable records, agent error | Re-dispatch once; second failure → unit `failed`, item proceeds with reduced N, **recorded** as degraded, and the report names it (Step 11d, Step 14e) |
| F11 | Merging counts real agreement | Three records from one analyst counted as agreement 3; or two identical claims about different loci merged | Agreement = distinct **analysts** (Step 6c); different loci are different findings (Step 6b) |
| F12 | Findings are facts | Interpretation enters as a confident claim with a citation attached | The single-locus admissibility test in `agents/common.md` (Step 3c) is checkable by the verifier — an interpretive claim fails because no single locus settles it |
| F13 | `off_limits` is respected | An analyst reads a forbidden path because it seemed relevant | Enforced at enumeration (Step 9d) so a forbidden path never becomes an item — a manifest property, not a behavioural promise; the prompt-level prohibition (Step 3b) is the second layer, not the first |
| F14 | The installed copy matches source | Edited in one place, run from the other | §7(2) `diff -rq`; the SKILL self-check section makes it a standing criterion |
| F15 | Recursion terminates | A tier-B item whose sub-items are also tier-B forever | Stage 2 records tier and depth in `decisions.md`; an item that does not shrink when split one level down is reclassified **C** (declared partial), not split again |
| F16 | The `agents/` split stays additions-only | A common rule is restated in a role file and the two copies drift | §7(5) greps for restatement; the rule "if a role file must modify a common rule, move the rule down into the roles" (Step, §2.2) is stated in `agents/common.md`'s header |

---

## 7. Verification

**Checkable done-criteria.** Every one is a command or a mechanical inspection; none is satisfied by
an assertion.

1. **All 17 files exist** at the paths in §5, and the four installed items exist under
   `~/.claude/skills/data-distiller/`. `test -f` / `test -d` each.
2. **Live copy == source copy.** `diff -rq ~/.claude/skills/data-distiller/ <the four source items>`
   → no output. This is the siblings' own standing self-check criterion
   (`Guarded_change/SKILL.md:82-83`, `Dragonfly/SKILL.md:87-89`).
3. **The skill is loadable and routable.** The installed `SKILL.md` frontmatter parses as YAML with
   exactly `name` and `description`; `name` == `data-distiller` == the installed directory name (the
   invariant both siblings exhibit); and every `stages/…` / `agents/…` path mentioned anywhere in
   `SKILL.md` or `METHODOLOGY.md` resolves to a file that exists.
4. **The end-to-end acceptance run** (Step 20), on a real corpus larger than one context window,
   produces `runs/<slug>/report.md`, and:
   - **Citations resolve.** Sample ≥20 findings from `report.md`; for each, open the cited path and
     locator and confirm the quote is there. Target: 20/20. Any miss is a stage-4 defect, since a
     non-resolving citation is exactly what stage 4 exists to drop.
   - **The node was blind.** Inspect the node agent's transcript / tool-call record: **zero** reads
     of any path under `raw/`, `verified/`, or `merged/`. This is the P6 criterion and it is checked
     from the node's actual reads, not from its report.
   - **Analysts were independent.** Each analyst's tool-call record shows reads of its own item (and
     permitted corpus paths) and **zero** reads of any other analyst's output file.
   - **Agreement ranking is arithmetic.** For three sampled merged findings, recount the distinct
     analysts in `raw/` that produced an equivalent verified record; the recount equals the reported
     `agreement`.
   - **Nothing was written to the corpus.** `find <root> -newermt <run start>` → empty.
   - **Resume works.** Kill the run mid-corpus, restart it: items with a `done` row and an existing
     output are skipped (no new `raw/` files for them), the interrupted item is re-run from its
     stage, and the final `report.md` has the same item count as an uninterrupted run.
5. **The role split holds.** `agents/common.md`'s rules appear once; grepping each of its rule
   sentences against the four role files yields zero substantive restatements. `agents/node.md`
   mentions `raw/`, `verified/` and `merged/` only inside prohibitions.
6. **The core is corpus-agnostic.** Grep `SKILL.md`, `METHODOLOGY.md`, `stages/` and `agents/` for
   the acceptance corpus's name, its paths, and its item type: zero hits outside
   `data-distiller.companion.md` and `README.md`. This is criterion P7 made checkable — if a corpus
   specific leaked into Layer 1, the next corpus inherits it.

**What I could not check, flagged as unchecked rather than assumed:**

- **Whether this design matches the existing implementation.** `Data-Distiller/` and its installed
  twin were off limits and were not opened. The plan is derived from the two named siblings; any
  agreement or disagreement with the existing implementation is unknown to me and no claim is made
  either way.
- **The exact frontmatter keys Claude Code requires.** I verified only that both working siblings
  use exactly `name` and `description` and nothing else, and that both load. I did not find or read
  a specification of the frontmatter schema, so "exactly two keys" is an inference from two working
  examples, not from a documented contract.
- **Whether `agents/` is copied into the installed skill correctly by whatever mechanism installs
  it.** The siblings have no second directory, so the `diff` evidence covers `stages/` only. Step 19(a)
  is what would catch a failure here; until it runs, the claim is untested.
- **The sibling run folders for this Architect run** (`divide-0.md`, `split-round-1.md`, the
  split-review files) were deliberately not read, to keep this plan cold and independent per
  `Architect/stages/common.md` §1.
