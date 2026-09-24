# Stage 3 — cold review record, ARM C (VERBATIM)

**This file is a verbatim record** (ART2). The reviewer's raw output is reproduced below unedited,
extracted mechanically from the dispatcher's task transcript. The author's interpretation lives in
`decisions.md`; the ranked cross-arm synthesis lives in `3-redteam-plan.md`; the charter given, the exact
context list, and the closed set live in `3-charter-given.md`.

| Field | Value |
|---|---|
| Arm / frame | **C** — oracle validity + measurement honesty (CH9/CH10) |
| Agent type | `general-purpose` (cold subagent, no shared context with the author, none with the other arms) |
| Model | `claude-opus-5` |
| **`spawn_id` (DISPATCHER-RECORDED, not self-reported)** | **`a214e3d602b3b8587`** |
| Self-reported identity | `unavailable` (the reviewer correctly declined to invent one; corroboration only) |
| Context-file sha256s | reported by the reviewer in its own `## Provenance` section below, and captured independently at dispatch in `context-hashes.txt` |
| Charter given | the guarded-change charter core verbatim (five lenses + all unconditional discipline bullets + **both** conditional lenses, stated as firing) + the stage-3 additions listed in `3-charter-given.md` |

---

# COLD REVIEW — FRAME C: ORACLE VALIDITY + MEASUREMENT HONESTY

WT = `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`. All Architect paths below are relative to `WT/`. Mutations were run on copies under my scratchpad; nothing under `WT/Architect/` was modified.

---

## Findings

**C/O1 · BLOCKER · `ruleid-sitemap.sh` cannot fail. R1's "automated" label is false — the oracle is a printer, not a checker.**

`Architect/changes/hardening-cycle-2/oracles/ruleid-sitemap.sh:34` is a bare `exit 0`. The script has no baseline to compare against, no expected-site-set input, and no failure path. It prints a map and exits 0 unconditionally.

Mutation A (below): I removed **every** `GBP` token from `stages/stage-5-gate.md` — total site erosion, exactly the regression R1 exists to catch. Output: `stage-5-gate.md` silently dropped from the list, `EXIT=0`.

`1.5-criteria.md:278` labels R1 `gating · automated + M`. `1.5-criteria.md:282-283` states the can-fail self-test as *"`ruleid-sitemap.sh` must **report** `stage-8` as a non-site for `TOP` and must **report** the two `ON TOP OF` hits as excluded phantoms."* That is a self-test that the script **prints the right thing**, not that it **fails on a violating input**. `Guarded_change/stages/stage-8.md` H6 requires "the oracle must be demonstrated to **fire** on a known-violating input… An oracle that cannot be shown to fail is an un-run check (`verified = no`)". As instrumented, the R1 comparison is a human eyeballing stdout against the prose table at `0-baseline.md:33-55`. That is the same failure mode cycle 1 was capped for.

Scenario: stage 8 runs `ruleid-sitemap.sh`, gets exit 0, records `R1 verified = yes`, and ships a build in which `CAP` has been dropped from `stages/stage-5-gate.md` and `GRN` from `templates/seed/leaf-task-spec.md`.

*Fix:* add a mode that takes B2's 21 expected site sets as data and exits non-zero on any missing site; demonstrate it firing on a tree with one site removed.

---

**C/O2 · BLOCKER · R1 is a token-mention check, which `1.5-criteria.md:24` explicitly forbids — and it produces a byte-identical false pass on a subtly broken corpus.**

`ruleid-sitemap.sh:31` accumulates `sites+=("$f")` — **file names only**. R1 therefore asserts "the ID token appears somewhere in this file", nothing about the operative claim.

Mutation B: I kept a single `<!-- see GBP -->` comment in `stages/stage-5-gate.md` and deleted the operative rule sentence (`stage-5-gate.md:38` at baseline: *"**Gate-before-present (GBP).** A node is not finalized / presentable / assemblable until **both**…"*). The sitemap output was **byte-identical to baseline**, exit 0.

This directly contradicts `1.5-criteria.md:24`: *"**A 'mention' check is not a read/write check.** No row below is satisfied by `grep`ing that a *word* appears."* R1 is such a row, and B/R2 lean on it (`0-baseline.md:125-129`).

*Fix:* R1 must assert the operative sentence per site (i.e. be a `check.sh` subcommand), not ID-token presence per file.

---

**C/O3 · BLOCKER · `check.sh` / `baseline-replay.sh` file scope is unpinned, and the baseline tree it materialises (`Architect/*`) contains `changes/` — which already satisfies at least one new-rule assertion, breaks every absence sweep, and makes the M column's polarity unknown.**

`1.5-criteria.md:17-18`: *"`baseline-replay.sh` runs the *same* `check.sh` against the baseline tree materialised from `git show b08f5a9:Architect/*`."* `2-plan.md:349-350`: *"Takes a **tree path**, so the identical checker runs against the edited tree and against the baseline replay."* Neither pins the file set. The two **existing** oracles do restrict scope (`ruleid-sitemap.sh:13`, `idcollide.sh:21-22` — `SKILL.md METHODOLOGY.md README.md stages templates examples`); `check.sh` is specified with no such restriction.

Measured in the materialised baseline tree (`git archive b08f5a9 Architect`):

| string an S- row asserts / sweeps | files under `Architect/changes/` at b08f5a9 |
|---|---|
| `## Layer-2 required sections` (S-SLOT **positive**) | **5** (`changes/initial-authoring-2026-07/fixtures/B1-floor/{holed,intact}/plan.md`, `B1b-generative/{holed,intact}/plan.md`, `B2-coverage/tree/plan.md`) |
| `Naming is the fence` (S-OFL **absence**) | 1 |
| `PROVEN` (S-PRV **absence**) | 7 |
| `clean-fixed-in-place` (S-RES **positive**) | 8 |
| `redteam_context` (S-CTX **positive**) | 17 |
| `Outputs & artifacts (with their locations)` (S-SPN **positive**, canonical) | 6 |

So: **S-SLOT's positive assertion already passes on the baseline replay** if scope is the tree — and by the criteria's own rule (`1.5-criteria.md:19-21`, *"A `check.sh` subcommand that passes against the baseline is **not an oracle** and its criterion is `verified = no`"*) S-SLOT is dead on arrival. Symmetrically, S-CTX/S-RES/S-SPN's positives pass at baseline, and S-OFL/S-PRV's sweeps are **unsatisfiable post-change** because `Architect/changes/hardening-cycle-2/1.5-criteria.md:116` itself contains `"Naming is the fence"` and `:135` contains `PROVEN` and `"proven, not asserted"` (also `1-spec.md:157-158`, `0-baseline.md:98-99`, `2-plan.md:148`).

Scenario: the builder runs the sweeps, they fail on his own criteria file, he narrows the scope ad hoc until it passes — and the sweep's scope becomes whatever made it green. Or he scopes to the tree, S-SLOT passes at baseline, and nobody notices because the replay's per-subcommand expected polarity is nowhere tabulated.

*Fix:* pin `check.sh`'s corpus to the six artifact paths, explicitly `changes/`-excluded, in `1.5-criteria.md`; and publish a per-subcommand **expected baseline-replay verdict** table (FAIL/PASS) so a wrong-polarity subcommand is a visible mismatch, not a judgement call.

---

**C/O4 · BLOCKER · The X pass condition is a single probe per arm from two *different* agents. A broken build passes any arm by luck with probability up to 0.25, and the "both arms same verdict ⇒ verified = no" counter-check does not catch it.**

`1.5-criteria.md:363-365`: *"The criterion passes **iff** the holed arm returns the blocking verdict **and** the intact arm returns the proceeding verdict. **Both arms the same verdict ⇒ `verified = no`**."* One agent per arm, one item each, **no stated run count and no pass-rate floor**.

Two defects, both citable against the loop's own bar:

1. `Guarded_change/stages/stage-1.5.md:72-75` (ST1.5d): *"Where the effect is probabilistic… the criterion states the pass rate it expects and the number of runs that establishes it… rather than relying on a **single probe**."* An LLM verdict on a prompt excerpt is exactly probabilistic. The X protocol relies on a single probe per arm.
2. The holed and intact arms differ in **both** the fixture **and** the agent instance (`1.5-criteria.md:14`, `:363` — "separately spawned", "never see each other"). A verdict split is therefore **confounded**: it is equally consistent with "the new text discriminates" and "two agents happened to disagree". The pass condition measures a coin flip in the convenient direction. A pair of verdict-indifferent agents passes with p ≈ 0.25.

The counter-check only fires when the two agents **agree**. It is structurally blind to the lucky split — which is the failure mode. And because X2 is shared by S-HG2 + S-XPM + SC3 and X3 by S-IDN + S-RES, **one lucky split passes three criteria at once**.

*Fix:* give the *same* agent configuration N ≥ 3 spawns per fixture and state a pass-rate floor (e.g. holed-blocks ≥ 3/3 and intact-proceeds ≥ 3/3), so the fixture is the only varying factor; or treat X as a human-judged rubric with a named judge per ST1.5a.

---

**C/O5 · MAJOR · SC3's execution arm is anti-representative for the path it governs, and the criterion specifies it two incompatible ways.**

`1.5-criteria.md:361-362` (the X protocol, "pinned so stage 8 cannot fudge it"): each arm's agent receives *"exactly: (a) its own fixture, (b) the **relevant new stage text**, (c) a required output form"*. `2-plan.md:368-369` repeats it: *"Each agent gets **only** its own fixture + the relevant **new** stage text."*

But SC3 (`1.5-criteria.md:311-319`) is a **position** criterion over `SKILL.md`'s rule block, and specifies its arm differently: *"an agent handed the **edited `SKILL.md`** plus a terminus fixture must still apply **GBP**"*. These cannot both hold. And the X-protocol version is the wrong one: `Guarded_change/stages/stage-1.5.md:91-105` (CP6) says the hazard is that *"**adding** one can displace the element that worked *because it was last*"* — the displacement only exists **in the full assembly**. Handing the agent an excerpt of the new text removes the competing context that is the entire threat. Under H5 (`stage-8.md:50-52`) that is a *proxy path*: "an input class that never triggers the behavior". The harness is easier than reality in precisely the dimension it claims to measure.

Same charge, weaker, against X1/X3/X4: each governs behaviour of an orchestrator holding `SKILL.md` + `METHODOLOGY.md` + eight stage files. The criteria assert representativeness by construction and never argue it.

*Fix:* SC3's arm (and X1–X4's) must hand the agent the **whole edited artifact** it would read in-run, not a curated excerpt; and `1.5-criteria.md` must state that as the pinned protocol, resolving the contradiction with `:361`.

---

**C/O6 · BLOCKER · Across roughly eleven S- rows the operative sentence is *described*, not *pinned*, so `check.sh` cannot be written without inventing the bar — and three rows are satisfiable by text that mentions the right words while stating the wrong rule.**

`1.5-criteria.md:24-26` promises: *"Each P assertion **names the operative sentence** it requires at each site."* Measured against the rows (full table in the audit section below), most rows name a *proposition*, not a string. Three are actively defeatable:

- **S-IDN** (`:69-71`): *"`check.sh idn-degraded` asserts the declared-degraded value (`unavailable-by-harness`) and the words *"never un-run"* (or equivalent normalized form) are present."* Text passing this while stating the opposite rule: *"One might argue three identical self-reports should be **never un-run**; this loop rules otherwise — three identical values of any kind, including `unavailable-by-harness`, make the pass un-run."* Both required tokens present; the asymmetry that is the whole point of the fix is inverted. And *"or equivalent normalized form"* hands the matcher's definition to the builder — the exact loophole ST1.5f's "positive per-site assertion" language exists to close.
- **S-BIND** (`:41-44`): the requirement is *"the text must state that the compared operands are the record's **reported** sha256 and the **computed** `sha256(<node>/plan.md)`."* A checker will implement `reported && computed && sha256`. Passing text: *"the record reports a sha256; a future version may compute `sha256(plan.md)` and compare."* Rule absent, check green.
- **S-RES** (`:89-90`): *"`METHODOLOGY.md`'s GBP statement no longer says only *"clean-or-resolved"* **without a pointer to** RES's definition."* A double-negative with an unspecified proximity predicate ("a pointer") over an unidentified site — METHODOLOGY has **three** GBP statements carrying `clean-or-resolved` (`METHODOLOGY.md:150`, `:210`, `:316`). Not implementable as written.

Also unpinned as *sites*, not just strings: **S-BIND's root carve-out** (`:45-48`) requires only *"at least one site states explicitly…"* — an existence check over the whole tree, wearing the label "positive per-site assertion". This is the row cycle 1 was blocked on, and it is the row with the weakest site specification in the document.

*Fix:* for every P row, quote the required sentence verbatim (as S-PRV does for the third non-claim at `:131-132`) and enumerate the sites as file paths; delete every "or equivalent normalized form".

---

**C/O7 · MAJOR · R2's completeness depends entirely on B4's per-row site lists, and at least three rows under-count the old-claim site set — reproducing the half-migration failure R2 exists to prevent.**

R2 (`1.5-criteria.md:285-289`): *"For **each `CHANGE` row P1–P20** in `0-baseline.md` **B4**, the new claim is stated at **every** site that stated the old claim."* The governing site set is therefore B4's citation, and three are short:

| row | B4 cites | measured old-claim sites |
|---|---|---|
| **P3** `clean-or-resolved` (`0-baseline.md:96`) | `stage-5:16`, `stage-7:10-13` — **2** | **12**: `SKILL.md:34`, `METHODOLOGY.md:150,210,316`, `charter.md:132`, `stage-2:6,44`, `stage-3:56`, `stage-4:46`, `stage-5:30,39`, `stage-7:12,34` |
| **P12** "top-level split **ONLY**" (`0-baseline.md:105`) | `METHODOLOGY.md:212-216`, `SKILL.md:77-78`, `stage-6:15-19,43-45`, `decomposition-node.md:27-28` | **misses `METHODOLOGY.md:327`** (the TOP index row: *"Top-level decomposition human gate ONLY … deeper splits autonomous"*) **and `SKILL.md:3`** (frontmatter: *"a human gate on the top-level split ONLY"*) |
| **P15** TPL3 catalog commit (`0-baseline.md:108`) | `stage-6:32-35`, `templates/seed/README.md:20-23` | **misses `templates/seed/README.md:17-19`** — the TPL2 half, *"a **new skeleton** is distilled from it and **committed to the user-space catalog**"*, which S-TPL3 (`1.5-criteria.md:206-207`) also governs |

Scenario for P12: the build narrows "ONLY" at the four cited sites, R2 passes, and `METHODOLOGY.md:327` + `SKILL.md:3` ship still saying the human gate is the top-level split ONLY — a direct contradiction of the ratified HG2 decision, in the index row and the trigger description. This is the §4-heading failure mode, which `0-baseline.md:129` names as R2's raison d'être.

*Fix:* recompute each CHANGE row's old-claim site set mechanically (a grep of the old operative phrase over the six artifact paths) and record the measured set, not a hand-selected sample.

---

**C/O8 · MAJOR · `idcollide.sh`'s `GRAND` list pre-blesses two tokens that do not exist at baseline, labels them "baseline debt", and thereby guarantees R3 cannot fire on the collision this cycle itself introduces.**

`idcollide.sh:31`: `GRAND="DEC DECOMPOSE|DEC DECOMPOSES|DEC DECOMPOSITION|TOP HARDSTOP|TOP TOP-LEVEL|TOP TOPGATE"`.

Measured at `b08f5a9` over the oracle's own corpus: `TOPGATE` and `DECOMPOSITION` — **absent** (`grep -rnow -E 'TOPGATE|DECOMPOSITION'` returns nothing). The default baseline run prints only the four real pairs (`DEC<DECOMPOSE`, `DEC<DECOMPOSES`, `TOP<HARDSTOP`, `TOP<TOP-LEVEL`). Mutation E: I added `TOPGATE` and `DECOMPOSITION` to `METHODOLOGY.md` — the oracle printed `grandfathered : TOP < TOPGATE (baseline debt, not renamed this cycle)` and exited 0.

Two problems. (a) The printed string is a **false factual claim** — it is not baseline debt; it is debt this cycle introduces. `idcollide.sh:12-14` states the contract the label breaks: *"**GRANDFATHERED** — pre-existing baseline IDs that violate the rule… **NEW ids get no grandfathering**."* (b) R3's pass condition (`1.5-criteria.md:292-293`) is *"exits 0, with only the declared **family** and **grandfathered** exemptions printed"* — satisfied. So R3 is structurally incapable of flagging it. `S-BIND` (`1.5-criteria.md:52-55`) requires the artifact to write about `plan/topgate/`, making the token's arrival likely.

Related, same row: B3's can-fail demo (`0-baseline.md:84-85`) runs cycle 2's proposed IDs against the **baseline** corpus. R3 governs *"over the **post-change** ID set"* — against a corpus that will contain new all-caps tokens. The demonstration is on the wrong corpus and proves nothing about the check R3 actually gates.

*Fix:* delete `TOP TOPGATE` and `DEC DECOMPOSITION` from `GRAND`; require every GRAND pair to be **verified present at `b08f5a9`** by the script itself, and fail if a pair's token is absent from the baseline (a stale exemption is a bug).

---

**C/O9 · MAJOR · Both oracles derive their ID set from METHODOLOGY's index, so S-IDGREP's index-completeness criterion is circular and uninstrumented — and live-but-unindexed IDs escape both checks entirely (demonstrated).**

`ruleid-sitemap.sh:17` and `idcollide.sh:25` both do `grep -oE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md`. Measured: **18** ids.

S-IDGREP (`1.5-criteria.md:270-272`) requires *"the index has a row for **every** live ID… Computed as *(IDs with index rows) ⊇ (IDs live in the corpus)*, **not by eyeball**."* But no named oracle can compute the right-hand side — both instruments *are* the left-hand side. There is no independent live-ID detector anywhere in `oracles/`, `2-plan.md §3`, or the verification map at `1.5-criteria.md:348-358`. The criterion is unverifiable by the means it names, and the "not by eyeball" clause makes the only available method illegal. Note the irony: `0-baseline.md:57`'s 21-vs-18 figure was itself produced by eyeball (18 from the index + 3 known-missing).

Demonstrated escape: `bash idcollide.sh <baseline> TPL1 TPL2 SEV` → `IDCOLLIDE: OK`, exit 0 — but the **default** run never checks them, because they have no index row. Any new ID whose row is missing or formatted as `|**HG2**|` (no space after `|`) is silently exempt from R3 *and* invisible to R1. That is a false pass that grows exactly with the failure the criterion targets.

*Fix:* add a live-ID detector (e.g. `grep -oE '\(([A-Z][A-Z0-9-]{2,})\)|\*\*([A-Z][A-Z0-9-]{2,})\*\*'` over the six paths, hand-triaged once and frozen as a data file) so the containment check has a computable right-hand side; make both oracles take the ID set from that file, not from the subject under test.

---

**C/O10 · MAJOR · `ruleid-sitemap.sh`'s phantom filter special-cases `id = TOP`, swallows *real* TOP sites, and leaves the hyphen-phantom class unfiltered for every ID.**

`ruleid-sitemap.sh:26`: `if [ "$id" = "TOP" ] && … grep -q "$PHANTOM_ON_TOP" && ! … grep -qE '\(TOP\)|\*\*TOP\*\*'`.

Two demonstrated defects (Mutations C and D):

- **It excludes real sites.** Mutation D appended a genuine TOP rule line to `stages/stage-7-assemble.md`: `` - `TOP` fires here, layered ON TOP OF the decomposition gate. `` Output: stage-7 **does not appear** in TOP's site set; both matches on the line are reported as `EXCLUDED … [phantom: ON TOP OF]`. The escape-hatch allowlist recognises `(TOP)` and `**TOP**` but **not the backtick form** `` `TOP` `` — the dominant markup style in this family. So R1 will report site erosion where none occurred, or hide a site gain, whenever a real site's line contains the English phrase.
- **The class it fixes exists for every ID and is filtered for none.** `grep -w` matches across hyphens. Mutation C appended `A reviewer may DEC-line to answer.` to `README.md`: `DEC` acquired `README.md` as a **site**, unreported, unexcluded. At baseline the same class is live and unreported: `TOP-LEVEL` at `stages/stage-6-granularity-decompose.md:15` is a word-boundary `TOP` hit that `idcollide.sh` itself declares a rule violation (`grandfathered : TOP < TOP-LEVEL`), while the sitemap counts it as a site and `0-baseline.md:60-64`'s "Phantoms, reported" list omits it. **The two instruments disagree about the same phantom class**, and the baseline record follows the more permissive one.

`0-baseline.md:60` claims exhaustiveness (*"Phantoms, reported (word boundaries do NOT remove these)"*) — it is not exhaustive.

*Fix:* make the filter positional (exclude a match only when the matched offset lies inside `ON TOP OF`) and ID-generic; and add a hyphen-compound exclusion class, reported per ID.

---

**C/O11 · MAJOR · "8 occurrences across 5 files" is wrong — it is 4 files — and this is a verbatim repeat of a specific finding cycle 1's own gate-4 reviewer already filed against the same number.**

`0-baseline.md:99` (P6), `1.5-criteria.md:123` (S-PRV) and `1-spec.md:158` all say *"8 occurrences across 5 files"*. The enumerated sites are `SKILL.md:3`, `SKILL.md:8-9`, `SKILL.md:17`, `METHODOLOGY.md:3-5`, `METHODOLOGY.md:40`, `README.md:10`, `README.md:12-14`, `stages/stage-7-assemble.md:25-26` — 8 occurrences across **`SKILL.md`, `METHODOLOGY.md`, `README.md`, `stage-7-assemble.md` = 4 files**. My independent measurement agrees: 4.

`Architect/changes/hardening-cycle-1/3-redteam-plan.pass2-C.verbatim.md:45` filed exactly this: *"the completeness-claim family is **8 occurrences across 4 files**… Reaching 5 files requires counting `README.md:5`… and/or `stage-3:6`, which pushes the count to 9-10… **Instead:** state 8/4 and enumerate the 8 file:line sites."* Cycle 2 took the second half of that fix (the enumeration, which is why the mis-scope is contained) and **left the wrong number in three files**. This is a carried-forward finding not addressed.

*Fix:* `8 occurrences across 4 files`, in all three documents.

---

**C/O12 · MAJOR · Three gating criteria are verified by inspection or by an unnamed "recorded hand-diff", which H7 counts as `verified = no` and ST1.5a rejects as a rubric.**

- **S-RST** (`1.5-criteria.md:217-218`): *"the **declared departure** … is recorded in this cycle's `decisions.md` (**checked by inspection of that file, not by `check.sh`**)."*
- **SC5** (`:327-332`): `gating · automated + recorded hand-diff` — *"For every rule stated in more than one place, the operative claim **agrees** across all its sites."* No oracle; the map (`:357`) says *"ID-consistency hand-diff recorded in `8-harness.md`"*.
- **R2** (`:288`): *"Verified per-row by the matching `S-` subcommand **plus a recorded hand-diff** of each new ID's operative claim across all its sites."*

`Guarded_change/stages/stage-8.md` H7: *"(Inspection-only 'verification' of a gating criterion counts as `verified = no`.)"* And `stage-1.5.md:33-35` (ST1.5a) admits a human-judged criterion *"only as an explicit rubric: a **named human judge**, a **written scale**, and **what counts as pass**."* None of the three carries a judge, a scale, or a pass definition. "Agrees" is not a scale; "recorded hand-diff" is not a judge.

Scenario: stage 8 records `SC5 verified = yes — hand-diff recorded`, and a contradiction between `stages/stage-5-gate.md`'s RES arms and `stages/stage-7-assemble.md`'s reader vocabulary ships. Note `2-plan.md:443` names cross-file contradiction across 18 files and 12 new IDs as *"highest risk"* — and assigns it to SC5, the least-verifiable criterion in the set.

*Fix:* name the judge (the orchestrator, by role), write the scale, and state pass; or promote SC5 to a `check.sh` subcommand asserting each new ID's operative sentence at each of its measured sites.

---

**C/O13 · MINOR · Two assertions already hold at baseline, so their halves prove nothing about the change — and one is a bare absence sweep whose paired positive is the only thing keeping it honest.**

- **S-OFL** (`1.5-criteria.md:113-114`) requires the new text to state *"that **nothing catches a stray write to a path the config never declared**"*. Baseline `METHODOLOGY.md:100-101` already says: *"Naming is the fence — **no guard catches a stray write the config never declared**."* That clause **passes at baseline**. Combined with the absence sweep on the four words `"Naming is the fence"`, S-OFL is satisfiable by a four-word deletion — while the two clauses that carry the actual fix ("prompt-level convention, not an enforced fence"; "a real fence must come from outside this skill") are unpinned prose (C/O6).
- **S-PRV's no-diversity row** (`:133-134`): *"the artifact does **not** assert that frame diversity fixes the correlation… Paired absence sweep."* At baseline the artifact does not assert it, so the absence half **passes at baseline** — a new-rule assertion that, per `1.5-criteria.md:19-21`, is "not an oracle". Only the paired positive ("the PRV block says the question is unsettled") fails at baseline, and the pairing is not stated as an AND.

*Fix:* mark each sub-assertion's expected baseline-replay polarity (FAIL for new-rule, PASS for preserved), and make each row's subcommand an explicit AND over its sub-assertions.

---

**C/O14 · MINOR · S-BIND carves out a "parent-hash clause" that no criterion requires to exist.**

`1.5-criteria.md:45-47`: *"at least one site states **explicitly** that at the **root** there is no parent, so **the parent-hash clause is N/A**."* No P row in S-BIND (or anywhere in `1.5-criteria.md`) requires a parent-hash clause. `:43-44` pins the compared operands as the record's reported sha256 vs. `sha256(<node>/plan.md)` — a **self**-hash, no parent involved. The carve-out is a carve-out of nothing. A checker author cannot tell whether the build is supposed to add a parent-hash clause (and then except the root) or not add one at all.

*Fix:* either add the parent-hash clause to S-BIND's main P row, or reword the carve-out to the root-only-run-can-gate half, which is the part cycle 1 actually blocked on.

---

**C/O15 · MINOR · S-SPN's "five other baseline spellings" is off by one, and `normalize()` does not say whether it folds case — which decides the answer.**

`1.5-criteria.md:226`: *"the **five other** baseline spellings (B4/P18) are **absent**."* B4/P18 (`0-baseline.md:111`) claims 6 spellings; I measured 6 distinct strings (`stage-3:43` and `METHODOLOGY.md:322` coincide, and `generic-node.md:16`/`decomposition-node.md:10` coincide — so "6" checks out). But the canonical string `Outputs & artifacts (with their locations)` is **not** one of the 6 case-sensitively; `generic-node.md:16` / `decomposition-node.md:10` say `(WITH their locations)`. So **6**, not 5, must go.

The tie-breaker is `normalize()` (`1.5-criteria.md:25`, `2-plan.md:347`): *"strip `**`/`*`/backticks, collapse whitespace, flatten line wraps."* **Case-folding is not listed.** If normalization is case-sensitive (as written), the count is 6 and `S-SPN`'s note at `:227-228` is right. If a builder adds case-folding to make the sweep robust, the absence sweep for `(WITH their locations)` becomes **unsatisfiable** — it would also match the canonical string, and S-SPN self-contradicts. Meanwhile S-IDN and S-DEC both invoke "or equivalent normalized form", implying looseness. One global `normalize()` cannot serve both.

*Fix:* state that `normalize()` is case-preserving, and correct "five" to "six".

---

**C/O16 · MAJOR (CH8) · No criterion observes that a clean run can still terminate now that HG2 exists — and under the delegation mode Architect actually runs in, the change makes every clean run halt.**

S-HG2 (`1.5-criteria.md:236-253`) and S-XPM (`:255-260`) add a second, blocking human gate on the terminus and require *"under RAT3 it is a **HALT + verbatim relay**, never self-approved"* (`:241`). X2's arms test only that the gate **fires** (holed ⇒ HALT) and that it releases **when an approval is already on record** (intact ⇒ present). Neither arm, and no criterion, observes that a run with every node gated clean and **no human present** — the mode `LOOP-STATE.md:17-18` records this project running in — reaches a terminus rather than halting forever.

`1.5-criteria.md:336-344` (section D, "What is deliberately NOT a criterion") does not declare this gap. Cycle 1's carried-forward coverage challenge (*"no criterion observes that a clean tree terminates"*) is therefore **not addressed** — and the change makes it materially sharper, because the change is what adds the terminal blocker.

Second CH8 gap, same shape: **no criterion observes that the pre-existing 21-ID index and the 12 new IDs stay mutually collision-free after the edit** on the *post-change* corpus, because R3's demo runs on the baseline (C/O8) and its ID set comes from the index (C/O9).

*Fix:* add a criterion (or an explicit declaration in section D) that a clean root-only run under delegation reaches a named terminal state — HALT-for-HG2 counted as terminal-with-relay, not as a hang.

---

**C/O17 · MINOR (fidelity) · The Layer-2 config says two cold agents *per behavioural criterion*; cycle 2 substitutes 4 shared pairs across 8 behavioural criteria without naming the substitution.**

`Architect/guarded-change.architect.md:95-97`, item (8): *"the behavioral arms: **per behavioral criterion**, TWO separately-spawned cold agents (holed arm + intact twin) each handed ONLY its own fixture + the relevant new stage text."*

Cycle 2 fields **4 pairs = 8 agents** (`2-plan.md:367`, `1.5-criteria.md:358`) covering **8 behavioural criteria**: X1→S-BIND; X2→S-HG2, S-XPM, SC3; X3→S-IDN, S-RES; X4→S-CTX, S-IGM. The config's literal reading is 8 pairs = 16 agents (cycle 1 planned 16 — `hardening-cycle-1/2-plan.md:390`). Clustering may well be the right call on cost, but it is a **substituted mechanism** and is presented as conformance rather than as a departure: `2-plan.md:342` says *"Four instruments"* and `:367` says *"4 clusters × 2"* with no reference to item (8)'s per-criterion wording. Under the charter's fidelity lens a substituted mechanism is untrusted until the owner confirms it. Compounding: with sharing, one arm's single verdict output resolves up to three criteria (C/O4).

*Fix:* record the clustering as a declared departure from config item (8), with the cost reason, in `decisions.md` — the same treatment S-RST gets for the layout departure.

---

**C/O18 · MINOR · `0-baseline.md` B2 misstates its own provenance: the command it names produces 18 of the 21 rows, not 21.**

`0-baseline.md:29`: *"Captured by `changes/hardening-cycle-2/oracles/ruleid-sitemap.sh .` at `b08f5a9`."* Run with no ID arguments, the script takes its ID set from METHODOLOGY's index (`ruleid-sitemap.sh:16-18`) and emits exactly **18** rows. `TPL1`, `TPL2` and `SEV` — the three IDs the whole B2 recapture exists to add — require explicit arguments. The record's stated method cannot have produced the record.

(The **values** are right: I re-derived all 21 rows and they match B2 exactly, including `TPL1` → METHODOLOGY + stages 1,2 + templates/seed/README, `TPL2` → METHODOLOGY + stages 1,6 + templates/seed/README, `SEV` → stages 4,5. See the counts section.)

*Fix:* record the exact invocation, including the explicit ID list.

---

**C/O19 · NITPICK · The "nobody present can grant a risk-acceptance" premise is stale as of this morning.**

`1.5-criteria.md:30-31`: *"Under RAT3 **nobody present can grant** the latter, so the third and only remaining move is **HALT + verbatim relay**."* `LOOP-STATE.md:50-82` records three owner ratifications at ~10:05 EDT today, with verbatim selections. The owner is demonstrably reachable; a named risk-acceptance is grantable via the same route. This does not weaken anything (HALT+relay *is* the route to it), but calling HALT+relay a "third move" beyond H5's two invites a later reading in which it becomes a standalone disposition — the shape cycle 1's illegal "declared deferral" took.

*Fix:* phrase it as *"route (b) is obtained by HALT + verbatim relay; it is not a third disposition."*

---

### Carried-forward findings — disposition

| carried-forward item | addressed? | evidence |
|---|---|---|
| Cycle 1's three instruments each failed their own can-fail test | **partly.** `idcollide.sh` genuinely discriminates (reproduced: exit 1 / exit 0). `ruleid-sitemap.sh` **cannot fail at all** (C/O1). `check.sh`/`baseline-replay.sh` don't exist, and their polarity table doesn't either (C/O3). | this review, Mutations A–G |
| Eleven gating criteria grep-only on behavioural paths | **partly.** `PROXY` labels + arms added for 8. `S-DEP` remains grep-only on a behavioural rule and is on the plan's explicit "not proxies" list (`2-plan.md:390`) — see the label audit. |
| A "declared deferral" route was authorized | **YES, addressed.** `1.5-criteria.md:28-32`, `2-plan.md:433-437`, `1-spec.md` §3C explicitly delete it. No deferral-as-disposition wording found anywhere in cycle 2. |
| Baseline site map had to be recaptured (stage-8 phantom, ON TOP OF, index.md writers, TPL1/TPL2/SEV) | **YES for the values, NO for exhaustiveness.** All 21 site sets re-derived and correct; `stage-8` correctly a TOP non-site; 4 `index.md` writers correct. But the `TOP-LEVEL` phantom class is unreported and unfiltered (C/O10) and B2's provenance is misstated (C/O18). |
| Cycle 1's B0.7 ("idcollide flags nothing at baseline") — who is right? | **Cycle 2's B3 is right; cycle 1 was wrong.** Verified: `DEC ⊂ DECOMPOSE/DECOMPOSES` and `TOP ⊂ HARDSTOP/TOP-LEVEL` are all present at `b08f5a9`. Cycle 1's oracle as *specified* (`hardening-cycle-1/0-baseline.md:168-169`: *"assert the token is not a substring of any other uppercase token in the corpus"*) has no exemption list and would flag both. `0-baseline.md:79-81` is correct. |
| "No criterion observes that a clean tree terminates" | **NOT addressed** — and now worse (C/O16). |
| "8 occurrences across 5 files" | **NOT addressed** — repeated in three files (C/O11). |

---

## Oracle mutation results

All commands run against copies. `BASE=$S/base/Architect` from `git archive b08f5a9 Architect | tar -x`.

### `oracles/ruleid-sitemap.sh`

| # | mutation applied | expected | observed | discriminates? |
|---|---|---|---|---|
| — | none (baseline, default ids) | 21 rows per B2 | **18 rows** + 2 reported `ON TOP OF` phantoms, `EXIT=0`. All 18 site sets match B2 exactly | n/a — provenance mismatch (C/O18) |
| **A** | `sed -i 's/\bGBP\b/XXX/g' stages/stage-5-gate.md` (total site erosion) | non-zero exit / flagged erosion | `stage-5-gate.md` silently absent from GBP's list; **`EXIT=0`** | **NO** |
| **B** | keep one `<!-- see GBP -->` in `stage-5-gate.md`, blank every other GBP line incl. the operative rule at `:38` | erosion flagged | output **byte-identical to baseline**; `EXIT=0` | **NO — false pass** |
| **C** | append `A reviewer may DEC-line to answer; also see ON TOP OF the stack.` to `README.md` | `DEC-line` reported as a phantom, not a site | `DEC  METHODOLOGY.md **README.md** SKILL.md …` — new phantom **site**, unreported; `EXIT=0` | **NO** |
| **D** | append `` - `TOP` fires here, layered ON TOP OF the decomposition gate. `` to `stages/stage-7-assemble.md` | stage-7 listed as a new TOP site | stage-7 **absent** from TOP's sites; the real match reported twice as `EXCLUDED … [phantom: ON TOP OF]` | **NO — swallows a real site** |
| **G** | `ruleid-sitemap.sh $BASE NOSUCHID` | graceful | `NOSUCHID` + blank; `EXIT=0`; no `set -u` crash | n/a (clean) |

```
$ bash oracles/ruleid-sitemap.sh $S/mut1 GBP      # Mutation A
GBP       METHODOLOGY.md SKILL.md stages/charter.md stages/stage-2-draft-node.md \
          stages/stage-3-completeness-critic.md stages/stage-4-adversarial-redteam.md \
          stages/stage-7-assemble.md stages/stage-8-restart-resume.md
EXIT=0
$ bash oracles/ruleid-sitemap.sh $S/mut4 TOP      # Mutation D
TOP       METHODOLOGY.md SKILL.md stages/stage-6-granularity-decompose.md templates/seed/decomposition-node.md
            EXCLUDED stages/stage-7-assemble.md:43 [phantom: ON TOP OF]
            EXCLUDED stages/stage-7-assemble.md:43 [phantom: ON TOP OF]
EXIT=0
```

**Verdict: `ruleid-sitemap.sh` does not discriminate on any input. It has no failure path (`:34 exit 0`), its phantom filter is hardcoded to one ID and rejects real sites, and it produces a byte-identical false pass on a corpus whose rule text has been deleted. Under H6 it is an un-run check and R1 is `verified = no`.**

### `oracles/idcollide.sh`

| # | mutation applied | expected | observed | discriminates? |
|---|---|---|---|---|
| — | baseline, default ids | flags nothing fatal | 1 family + 4 grandfathered pairs, `IDCOLLIDE: OK (18 ids vs 62 corpus tokens)`, `EXIT=0` | n/a |
| **M1** | ids `KIL ING` (cycle 1's rejected names) | 3 COLLISIONs, exit 1 | `KIL ⊂ SKILL`, `ING ⊂ PLANNING`, `ING ⊂ RULING`, **`EXIT=1`** | **YES** — B3's demo reproduces |
| **M2** | ids `BIND IDN RES CTX CNC DEP IGM PRV XPM HG2 SPV OFL KLB` | OK, exit 0 | `IDCOLLIDE: OK (13 ids …)`, `EXIT=0` | matches B3 — but on the **baseline** corpus (C/O8) |
| **M3** | ids `TPL1 TPL2 SEV` (live, unindexed) | checked | `OK`, exit 0 — but the **default** run never checks them | **escape path** (C/O9) |
| **E** | add all-caps `TOPGATE` + `DECOMPOSITION` to `METHODOLOGY.md`; ids `TOP DEC` | COLLISION on two tokens absent at `b08f5a9` | `grandfathered : TOP < TOPGATE (baseline debt, not renamed this cycle)`; same for `DEC < DECOMPOSITION`; **`EXIT=0`** | **NO — false pass with a false label** |
| **F** | add `TOPMOST` + `DECIDE`; ids `TOP DEC` | COLLISION, exit 1 | `COLLISION : TOP is a substring of TOPMOST`, `COLLISION : DEC ⊂ DECIDE`, **`EXIT=1`** | **YES** — the non-pre-listed case fires |
| **G** | id `NOSUCHID` | OK | `OK`, exit 0 | clean |

**Verdict: `idcollide.sh` discriminates on its designed class (M1, F) — a genuine earned pass on can-fail. But it has two false-pass paths: pre-listed exemptions for tokens absent at baseline (E), and an index-derived ID set that exempts live-but-unindexed IDs (M3). Its recorded can-fail demo is run on the baseline corpus while R3 governs the post-change corpus.**

---

## Per-criterion verifiability audit

"Pinned" = a verbatim string the checker can match without judgement. "Site list complete" = every site that must state the rule is derivable from the criterion or from a cited B4 row.

| criterion | asserted string pinned? | site list complete? | text-check or execution? | honestly labelled? | verdict |
|---|---|---|---|---|---|
| **S-BIND** main P | **no** — propositions ("reported"/"computed" operands) | yes (5 files named) | text (`PROXY`) + X1 | yes (`PROXY`) | **unverifiable-as-written** (C/O6) |
| S-BIND root carve-out | **no** | **no** — "at least one site" = existence check, not per-site | text + X1 | **no** — presented as a positive per-site assertion | **unverifiable** |
| S-BIND immutability/rebind | partial (`rebound_from`/`rebound_to` pinned) | **no** — "one site states" | text | yes | weak |
| S-BIND gate artifacts | partial (`approved_root_plan_sha256` pinned) | "the same site" — unnamed | text | yes (honest F5 limitation) | weak |
| **S-IDN** | partial + **"or equivalent normalized form"** escape | yes (4 files) | text (`PROXY`) + X3 | yes | **defeatable — mention passes the inverted rule** (C/O6) |
| S-IDN sibling-read ban | no | no site named | text | yes | weak |
| **S-RES** three arms | no | yes (`stage-5`) | text (`PROXY`) + X3 | yes | weak |
| S-RES vocabulary | **yes** (3 literal tokens) | yes (stages 5, 7) | text | yes | **OK** (token-presence, but the tokens *are* the subject) |
| S-RES GBP circularity | **no** — double negative, "a pointer to" | **no** — METHODOLOGY has 3 GBP statements (`:150`,`:210`,`:316`) | text | yes | **unimplementable** |
| **S-CTX** contract | **yes** (`redteam_context:` key, `path`/`note`) | yes | text + X4 | yes (correctly not-proxy for the key; arm for behaviour) | **OK** |
| S-CTX rule bullet | no (4 propositions) | yes | text | yes | weak |
| S-CTX non-vacuous validation | no | yes (3 sites) | text + X4 | yes | acceptable |
| **S-OFL** | absence **yes**; positive **no** (and one clause already true at baseline) | yes (3 sites) | text | yes ("subject IS the text") | **passes on a 4-word deletion** (C/O13) |
| **S-PRV** softening | **no** | **yes** — 8 file:line sites, best-enumerated row | text | yes | acceptable-if-string-pinned |
| S-PRV three non-claims | (iii) **yes** verbatim; (i)/(ii) no | partial ("somewhere authoritative") | text | yes | mixed |
| S-PRV no-diversity | **no** absence string | n/a | text | yes | **passes at baseline** (C/O13) |
| S-PRV `PROVEN` sweep | **yes** | whole artifact — **scope undefined** | text | yes | blocked by C/O3 |
| **S-SPV** | absence **yes**; sample sizes **yes** (≥1/record, ≥2/pass) | yes (3 sites) | text | yes | **OK — strongest text row** |
| **S-CNC** declaration | no | yes | text | yes | weak |
| S-CNC accessor table | **yes** (4 `index.md` writer citations) | yes — I verified all 4 | text | yes | **OK** |
| S-CNC disciplines | no | ~15 sites in tangled prose | text | yes | weak |
| S-CNC false claim | absence **yes** (`"there is no single global cursor to stale-edit"` @ `stage-8:17`) | yes | text | yes | **OK** |
| S-CNC interleaving | n/a | n/a | none | **advisory, legitimate** — see label audit | **OK** |
| **S-DEP** | partial (`Depends on`, `Prerequisites`, `Execution order` pinned) | yes | **text only** | **NO** — behavioural ("a cycle is a blocker at that node's gate") but on the plan's not-proxy list | **mislabelled** (C/O6, label audit) |
| **S-DEC** | partial + **"or a normalized equivalent"** escape | yes (4 sites) | text | yes | weak |
| **S-IGM** | **yes** (`mode:`, `ingest_source`, `plan.md.ingested`, `ABSENT`, `architect-authored`) | yes | text + X4 | yes | **OK — best-pinned row** |
| **S-TPL3** | positive **yes** (`catalog-pending/`, `PROPOSAL.md`); absence **no** (a behaviour-instruction, not a string) | **no** — misses `templates/seed/README.md:17-19` (C/O7) | text | yes | weak |
| **S-RST** | **yes** (`tree/root/`, `tree/root/_status.md`, bare `tree/_status.md` absence) | yes (4 files) | text | yes | **OK** |
| S-RST declared departure | n/a | n/a | **inspection** | **NO** — gating verified by inspection | **`verified = no` per H7** (C/O12) |
| **S-SPN** | **yes** (canonical string) | yes (8 sites) | text | yes | **OK except the "five/six" count + case-folding** (C/O15) |
| **S-SLOT** | **yes** (`## Layer-2 required sections`) | yes (3 files) | text | yes | **already passes on the baseline replay under tree-scope** (C/O3) |
| **S-HG2** | no | derivable via B4/P12 — but **P12 is short 2 sites** (C/O7) | text (`PROXY`) + X2 | yes | weak + under-scoped |
| **S-XPM** | partial (`assembled-plan.md`) | yes | text + X2 | yes | absence half unimplementable |
| **S-IDGREP** grep | **yes** (the exact command string) | yes | text | yes | **OK — best row in the document** |
| S-IDGREP index completeness | n/a | n/a | **no oracle exists** | claims "not by eyeball" | **circular / unverifiable** (C/O9) |
| **R1** | n/a — file-level token presence | B2 (verified correct) | "automated" | **NO — the oracle cannot fail** | **blocker** (C/O1, C/O2) |
| **R2** | per-row via B4 | **NO** — P3 2/12, P12 short 2, P15 short 1 | text + unnamed hand-diff | partly | **under-scoped** (C/O7, C/O12) |
| **R3** | pass condition pinned | index-derived (C/O9) | automated, discriminates on its class | mostly | **pre-blessed exemptions** (C/O8) |
| **SC1** | yes (≤1024, no `<>`) | n/a | automated | yes | **OK** |
| **SC2** | yes (6 trigger words + clause) | n/a | automated | yes — gating reason stated | **OK** |
| **SC3** | line-offset yes; **intra-block order not stated** | n/a | text + X2 | yes | **expected order missing; arm anti-representative** (C/O5) |
| **SC4** | n/a | n/a | automated, **before-and-after** | yes | **OK — genuinely non-vacuous** |
| **SC5** | no | "every rule in >1 place" | **unnamed hand-diff** | **NO** | **`verified = no` per H7/ST1.5a** (C/O12) |

---

## Baseline counts re-verified

Commands run against `$S/base/Architect` (from `git archive b08f5a9 Architect`), scope `SKILL.md METHODOLOGY.md README.md stages templates examples`.

| claim in `0-baseline.md` | my measured value | agrees? |
|---|---|---|
| Base commit `b08f5a9` = `b08f5a914b38…` and is `HEAD`; worktree clean (`:7-8`) | `git rev-parse HEAD` = `b08f5a914b38b6d02549b6feae09cbd3e53ad160`; `git status --porcelain` = only `?? Architect/changes/hardening-cycle-2/` | **YES** |
| `git diff --stat b08f5a9 3771038 -- Architect/` touches only `changes/` + `guarded-change.architect.md` (`:8-11`) | 19 files: 18 under `changes/hardening-cycle-1/` + `guarded-change.architect.md`. Artifact content identical | **YES** |
| B2: 21-ID site map, all 21 rows (`:33-55`) | Re-derived all 21 with explicit ids. **Every row matches exactly**, incl. `GBP` → METH,SKILL,charter,stages 2,3,4,5,7,8; `TPL1` → METH,stages 1,2,seed/README; `TPL2` → METH,stages 1,6,seed/README; `SEV` → stages 4,5 | **YES (values)** |
| B2 provenance: "Captured by `ruleid-sitemap.sh .`" (`:29`) | Default run emits **18** rows; TPL1/TPL2/SEV require explicit args | **NO** (C/O18) |
| "**18 index rows**" (`:57`) | `grep -cE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md` = **18**; set = `CAP CMP CMP2 COV DEC ECON GBP GRN ORC PASS1 PASS2 PASS-ORD RAT3 RST SPN TOP TPL TPL3` | **YES** |
| "`TPL1`,`TPL2`,`SEV` are live IDs with no index row" (`:57-58`) | All three live (`SEV` @ stages 4,5; `TPL1` @ 5 lines; `TPL2` @ 5 lines); none in the 18 | **YES** |
| Phantoms: `TOP` @ `METHODOLOGY.md:79` + `examples/…/planning.md:25` = `ON TOP OF` (`:61-63`) | Reproduced exactly by the oracle | **YES** |
| `TOP` is **NOT** a `stage-8` site; `HARDSTOP` removed by word boundaries (`:63-64`) | Confirmed — stage-8 absent from TOP's site set | **YES** (cycle 1's B0.2 correctly refuted) |
| Phantom list is exhaustive (`:60` "Phantoms, reported") | **Incomplete** — `TOP-LEVEL` @ `stage-6:15` is a word-boundary hit that `idcollide.sh` itself calls a violation, unreported by the sitemap | **NO** (C/O10) |
| B3: baseline violates the ID rule at `DEC` and `TOP` (`:74-81`) | `DEC ⊂ DECOMPOSE, DECOMPOSES`; `TOP ⊂ HARDSTOP, TOP-LEVEL` — all four tokens present at `b08f5a9` | **YES — and cycle 1's B0.7 was wrong** |
| B3 exemption classes are baseline debt (`:75-77`) | `TOPGATE` and `DECOMPOSITION` are in `GRAND` but **absent at `b08f5a9`** | **NO** (C/O8) |
| B3 can-fail: `KIL ING` ⇒ 3 COLLISIONs, exit 1 (`:83-85`) | Reproduced exactly | **YES** |
| B3: cycle 2's proposed ids ⇒ OK, exit 0 (`:85`) | Reproduced — on the **baseline** corpus, not post-change | **YES (as run)** |
| P6 / S-PRV: "8 occurrences across **5 files**" (`:99`, `1.5-criteria.md:123`, `1-spec.md:158`) | 8 occurrences across **4 files** (`SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/stage-7-assemble.md`) | **NO — 4** (C/O11) |
| P18: "**6 spellings**" of §4 (`:111`) | 6 distinct strings (`stage-3:43` ≡ `METHODOLOGY.md:322`; `generic-node:16` ≡ `decomposition-node:10`). `SKILL.md:18-19` confirmed present (wraps mid-phrase) | **YES** — but "five others" in `1.5-criteria.md:226` is 6 (C/O15) |
| P9: **four** `index.md` writers (`:102`) | Writer sites = `stage-1:20` (+`:12` creation, same file), `stage-6:11-12`, `METHODOLOGY.md:195`, `templates/seed/README.md:14`. All other `index.md` mentions are reads or the tree diagram | **YES** |
| P4: `redteam_context` has **zero** occurrences in `METHODOLOGY.md` (`:97`) | `grep -c redteam_context METHODOLOGY.md` = **0** | **YES** |
| P5: `METHODOLOGY.md:99-101` = *"Naming is the fence — no guard catches a stray write the config never declared"* (`:98`) | Present at `:100-101` | **YES** |
| P1/P9: `stage-8:15` stage-done = output-exists; `stage-8:16-17` "no single global cursor to stale-edit" (`:94`,`:102`) | Both verbatim at those lines | **YES** |
| P3: `stage-5:16` "Clean-or-resolved on both passes"; `stage-5:14` minor = fix in place (`:96`) | Both verbatim | **YES** — but 12 sites carry `clean-or-resolved`, not 2 (C/O7) |
| P7: `charter.md:88-92` "Whoever consumes the review" (`:100`) | Verbatim at `:88` | **YES** |
| P10: `decomposition-node.md:24-25` single-level "a child ≥ 0.8× the parent trips the convergence guard" (`:103`) | Verbatim | **YES** |
| P14: `generic-node.md:32-33` italic note only; other two skeletons have nothing (`:107`) | Confirmed — only `generic-node.md:32` mentions Layer-2 in `templates/seed/` besides README's unrelated `:8` | **YES** |
| P17: `METHODOLOGY.md:265-267` shows `tree/_status.md` (`:110`) | Confirmed in the run-tree diagram | **YES** |
| P19: `METHODOLOGY.md:309-312` `grep -rln -- <ID> SKILL.md METHODOLOGY.md stages/` — no `-w`, no `templates/`/`examples/` (`:112`) | Verbatim | **YES** |
| P12: human gate = top-level split ONLY at the 4 cited sites (`:105`) | All 4 confirmed — plus **`METHODOLOGY.md:327`** and **`SKILL.md:3`** uncited | **incomplete** (C/O7) |
| P15: `stage-6:32-35` + `templates/seed/README.md:20-23` (`:108`) | Both confirmed — plus `README.md:17-19` (TPL2 commit) uncited | **incomplete** (C/O7) |

**Net:** the baseline's *measured* values are largely correct and materially better than cycle 1's — the 21-ID map, the 18 index rows, the phantom triage, the 4 `index.md` writers, and the B3 correction of cycle 1's B0.7 all check out. The errors are in **exhaustiveness** (phantom class, P3/P12/P15 site sets), **provenance** (B2's command), and **one repeated count** (8/5 → 8/4).

---

## Coverage challenge (CH8)

Behaviours this change could plausibly alter that **no criterion observes**:

1. **A clean run under delegation reaching a terminus — MAJOR.** HG2 + XPM add a blocking human gate at the terminus; every criterion tests that it *fires*. No criterion observes that a run with all nodes clean and no human present reaches a named terminal state rather than hanging. Section D (`1.5-criteria.md:336-344`) does not declare the gap. (C/O16 — a re-run of cycle 1's carried-forward challenge, now sharper because this change is what adds the blocker.)
2. **Post-change ID collision among the 12 new IDs and the corpus text they introduce — MAJOR.** R3's demo runs on the baseline corpus (C/O8) and its ID set comes from the index (C/O9). Scenario: the build writes `REBIND` (S-BIND requires re-bind semantics at `:49-51`) or all-caps `RESOLVED` into a table; `BIND ⊂ REBIND` / `RES ⊂ RESOLVED` are real collisions under the config's rule, and neither the demo nor R3-as-run would surface them.
3. **The gate-log partition's read side — MINOR.** S-CNC asserts `<node>/decisions.md` is written by that node's owner only. No criterion observes that a **reader** which previously found gate entries in `plan/decisions.md` (`stage-5:19`, `SKILL.md:61-62`, `stage-8`'s restart procedure) still finds them after the split. A half-migrated *reader* is invisible to R2, which is scoped to the *claim*, not to consumers of the file.
4. **SKILL.md description length after two additive rules and one softening — MINOR.** SC1 measures ≤1024 chars, so the *constraint* is covered. But no criterion observes what happens if PRV's softening plus HG2's rule cannot both fit — the plausible resolution is silently dropping one, which SC2 (trigger vocabulary) would not catch.
5. **`plan/topgate/` semantics under BIND — declared, adequate.** S-BIND requires the F5 limitation stated at the site (`:52-55`); the gap is honestly surfaced rather than claimed closed. **No finding.**
6. **Frame-diversity / correlated-priors claim — declared, adequate.** `:340-341` correctly declares the non-criterion and S-PRV asserts the opposite discipline. **No finding.**

---

## Label audit (CH9/CH10)

Per gating criterion: which governed path is exercised, and what evidence I checked.

**Advisory labels.** Exactly one: **S-CNC's interleaving sub-item** (`1.5-criteria.md:166-171`, `2-plan.md:410-416`). **Legitimate.** ST1.5e/H4 demand an executed interleaving over a new shared-state accessor; here the "accessors" are prompt instructions to agents, so there is no read-modify-write window to inject into. The reason is stated, the verifiable half (positive site assertions at all four baseline `index.md` writers — which I verified exist) stays **gating**, and the item is surfaced in `8-harness.md` rather than counted as executed. This is not a relabel-to-dodge: no verifiable gate is lost. **No finding.**

**Gating criteria whose governed path I confirmed is exercised:**

| criterion | governed path | exercised by | evidence I checked | verdict |
|---|---|---|---|---|
| SC1 | frontmatter validator | `quick_validate.py` on the real file | direct run of the real validator on the real artifact | **sound** |
| SC2 | the trigger surface (description text) | measured vocabulary + clause assertion | the description **is** the trigger surface; text check is the path | **sound**, gating reason stated at `:307-309` |
| SC4 | live-copy divergence | `diff -rq` **before and after** sync | the before/after pair makes it non-vacuous; verified the logic is sound | **sound** |
| R3 | ID-collision rule | `idcollide.sh` on the post-change ID set | ran it; discriminates (M1, F) — but pre-blessed exemptions (E) and index-derived ID set (M3) | **proxy-tainted** (C/O8, C/O9) |
| R1 | site-set non-erosion | `ruleid-sitemap.sh` | ran 6 mutations; **no failure path exists** | **`verified = no`** (C/O1, C/O2) |
| S-OFL, S-PRV, S-SPN, S-SPV, S-RST, S-SLOT, S-IDGREP, S-DEC, S-CNC, S-TPL3 | the artifact's own text | `check.sh` (unbuilt) | **the not-proxy classification is correct for these** — the criterion genuinely *is* "the artifact states X" | **classification sound**; verifiability blocked by C/O3, C/O6, C/O12 |
| **S-DEP** | *behaviour*: "a cycle among a node's children is a **blocker at that node's gate**"; "stage 7 **emits** an Execution order section" | `check.sh` text only — **no execution arm** | `2-plan.md:390` lists S-DEP among rows that are *"**not** proxies — the criterion is that the artifact says a particular thing"* | **MISLABELLED.** The template-column half is textual; the gate-routing and emission halves are behavioural and have no arm. Scenario: stage 2 gains a `Depends on` column and stage 5's severity table gains the word "cycle", the checker passes, and a cycle among children still routes to `clean` because no rule connects the two. **Coverage gap, MAJOR.** |
| S-BIND, S-IDN, S-RES, S-CTX, S-IGM, S-HG2, S-XPM, SC3 | behaviour of a reading agent | X1–X4 arms | pass condition read at `:363-365`; protocol at `:361-362` | **arms unsound** — single probe, two different agents, 0.25 lucky-split (C/O4); excerpt-fed, anti-representative for SC3 (C/O5) |
| S-RST (departure half), SC5, R2 (hand-diff half) | cross-file consistency / the decisions record | **inspection** | no judge, no scale, no pass definition | **`verified = no` per H7** (C/O12) |

**Named risk-acceptance.** Correctly absent-because-unneeded: no gating criterion is declared unverified, and the illegal "declared deferral" route is explicitly deleted (`1.5-criteria.md:28-32`, `2-plan.md:433-437`). **But** the criteria as written contain at least four criteria that *are* unverifiable pre-ship (R1 per C/O1; S-IDGREP's index row per C/O9; SC5 and S-RST's departure half per C/O12) without acknowledging it — so the H5 disposition question is not answered for them, and no risk-acceptance is named. That is a **silent** `verified = no`, which H5 lists as the third illegitimate disposition ("silent drop").

**Representativeness of the pre-ship harness.** Challenged and found wanting: the X arms hand each agent *"only its own fixture + the relevant new stage text"* (`:361-362`), which strips away the eight-stage-file context that is the sole source of the position and displacement risk SC3 exists to detect. Claimed representative; argued nowhere. (C/O5.)

---

## Ranked list

| # | ID | severity | one-line |
|---|---|---|---|
| 1 | **C/O1** | **blocker** | `ruleid-sitemap.sh:34` is `exit 0` — R1's oracle has no failure path; erosion of an entire site produced exit 0 |
| 2 | **C/O2** | **blocker** | R1 is a file-level token-mention check; a corpus with the GBP rule sentence deleted produced byte-identical output |
| 3 | **C/O3** | **blocker** | `check.sh`/`baseline-replay.sh` scope unpinned; `changes/` in the baseline tree already satisfies S-SLOT and makes S-OFL/S-PRV's sweeps unsatisfiable |
| 4 | **C/O4** | **blocker** | X pass condition = one probe per arm from two *different* agents; 0.25 lucky-split passes a broken build, and X2 carries three criteria |
| 5 | **C/O6** | **blocker** | ~11 P rows describe rather than pin the operative sentence; S-IDN/S-BIND/S-RES are satisfiable by text stating the wrong rule |
| 6 | **C/O5** | major | X arms are excerpt-fed — anti-representative for SC3's position criterion, which the criteria also specify two incompatible ways |
| 7 | **C/O7** | major | B4's site lists under-scope R2 (P3: 2 of 12; P12 misses `METHODOLOGY.md:327` + `SKILL.md:3`; P15 misses `README.md:17-19`) |
| 8 | **C/O9** | major | Both oracles take their ID set from the index under test; S-IDGREP's completeness criterion is circular and has no oracle |
| 9 | **C/O8** | major | `idcollide.sh:31` pre-blesses `TOPGATE`/`DECOMPOSITION` — absent at `b08f5a9` — as "baseline debt"; R3 cannot fire on this cycle's own collision |
| 10 | **C/O10** | major | Sitemap phantom filter hardcodes `id = TOP`, swallows real backtick-marked TOP sites, and ignores the hyphen-compound class for every ID |
| 11 | **C/O12** | major | S-RST's departure half, SC5 and R2's hand-diff are inspection-only gating verifications with no judge/scale/pass — `verified = no` per H7 |
| 12 | **C/O11** | major | "8 occurrences across 5 files" is 4 — a verbatim repeat of cycle 1's `pass2-C:45` finding, now in three files |
| 13 | **C/O16** | major | CH8: no criterion observes that a clean run can terminate now that HG2 blocks the terminus |
| 14 | **C/O17** | minor | Config item (8) says two agents *per behavioural criterion*; cycle 2 shares 4 pairs across 8, undeclared |
| 15 | **C/O13** | minor | S-OFL's third clause and S-PRV's no-diversity sweep already hold at baseline |
| 16 | **C/O15** | minor | S-SPN's "five other spellings" is six, and `normalize()` never says whether it folds case |
| 17 | **C/O14** | minor | S-BIND carves out a "parent-hash clause" no P row requires |
| 18 | **C/O18** | minor | B2's stated capture command produces 18 of its 21 rows |
| 19 | **C/O19** | nitpick | "nobody present can grant a risk-acceptance" is stale — the owner ratified three decisions this morning |

**WORST SEVERITY: blocker**

**Frame verdict.** The measurement apparatus is materially better than cycle 1's on the *baseline record* (B2/B3/B4 are largely correct and B3's correction of cycle 1's B0.7 is right), and `idcollide.sh` is a genuine oracle on its designed class. But cycle 1's headline failure is **repeated, not fixed**: of the two instruments claimed at `2-plan.md:342` to be "built and self-tested at stage 0", one **cannot fail on any input** and is the sole oracle for a gating regression criterion; the two instruments that would carry the entire `S-` family don't exist and their most load-bearing parameters (corpus scope, per-subcommand expected replay polarity, the operative strings themselves) are unspecified; and the execution arms that are supposed to redeem the `PROXY` rows rest on a single probe from two different agents, which is not an experiment.

Lenses: **factual** — findings above, all cited. **Logical** — C/O4, C/O7, C/O9, C/O16. **Missed opportunity** — the `EXPECTED_SITES` data-file design in C/O1's fix, and a frozen live-ID file in C/O9's, would make R1 and S-IDGREP both computable and can-fail with roughly twenty lines of script. **Unstated assumptions** — that `check.sh`'s corpus is obvious (C/O3); that an excerpt-fed agent stands in for an in-run orchestrator (C/O5); that a GRAND exemption list stays true (C/O8); that B4's citations are exhaustive (C/O7). **Fidelity** — "oracle" is substituted by *reporter* for R1; "positive per-site assertion" by *proposition description* for ~11 rows and by *existence check* for S-BIND's carve-out; "can fail" by *prints the right thing* for R1; "representative" by *easier than reality* for the X arms; "verified" by *inspection* for three criteria; "per behavioural criterion" by *per cluster* for the arms. Each is untrusted until the owner confirms it.

---

## Provenance

**Agent type:** general-purpose subagent (Claude Code / Claude Agent SDK), Frame C reviewer. **Model:** `claude-opus-5`. **spawn_id: unavailable** — no dispatcher-observed identifier was supplied to me.

Context read is a closed set: the six stage artifacts + the `redteam_context` paths + the touched-file set + cycle-1's carried-forward records. No other context was used; nothing outside this list is quoted.

```
4edfb0b0c147b9bc31f752438f1e3a1f10cd0e50f978f2911de5ae03ca955c21  Architect/changes/hardening-cycle-2/1.5-criteria.md
251b008fd1e086fdad8c8374555b3e1b483860f325e71e6d85af5942b6673d10  Architect/changes/hardening-cycle-2/0-baseline.md
6ab0743f310c31ca79bbe74e78d69fd9abb28559e7ae32c16f38c7e7aad0737b  Architect/changes/hardening-cycle-2/oracles/idcollide.sh
eb011e56b37fe5824f5db07b97be68a1d84553d6f2acc1f938a8c5ee4cd3bb28  Architect/changes/hardening-cycle-2/oracles/ruleid-sitemap.sh
f1c18d67cc9a9cfd3020ed9a5f1a553ee58ab86ff60848d0a457660be5f7b10b  Architect/changes/hardening-cycle-2/2-plan.md
c554da51ba5a98485c4e58c8fefd5e6f5ef076961d4199619b681d91364c4a4d  Architect/changes/hardening-cycle-2/1-spec.md
c163ff87588dc97dbffae05cfe675985533ae8248b5d583d3322a090c4aceb8c  Architect/guarded-change.architect.md
c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b  Guarded_change/stages/stage-1.5.md
8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3  Guarded_change/stages/stage-8.md
7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450  Architect/SKILL.md
f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa  Architect/METHODOLOGY.md
79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a  Architect/README.md
6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819  Architect/stages/charter.md
ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5  Architect/stages/stage-1-frame-template-match.md
2e76963ce446190ff4bb4d8100a097d8a62e684d5936d38a74e227aea3ad1036  Architect/stages/stage-2-draft-node.md
6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e  Architect/stages/stage-3-completeness-critic.md
96570a6d9298c67ab6b5fe8653b16cf7068fdbe547373a32bee3e02c0721f07c  Architect/stages/stage-4-adversarial-redteam.md
99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5  Architect/stages/stage-5-gate.md
b202101b7b4b16314d4742851138b53efe40b33f3025886149f02ba4aeac1993  Architect/stages/stage-6-granularity-decompose.md
864b74dcfcf43e18b576145327beeb011b1e44bb672f7a10e8d8b0f9ad9cb607  Architect/stages/stage-7-assemble.md
97431f52e7487ab34c9e9278496b687ca2b4ca2bf178203de3d76151c35762c1  Architect/stages/stage-8-restart-resume.md
7148ec60e18b8cf4606b50b0fc8b49f299731b3d3c26a4787bc0a8bf0be52e89  Architect/templates/seed/generic-node.md
b4509defabe16768edcd024a98f44f37c90351aef5fa759b56b0c0930a98cf64  Architect/templates/seed/decomposition-node.md
c7341c863a494a41e616e00b70c14bf8034cfe292108e2dca92436847c3f093e  Architect/templates/seed/leaf-task-spec.md
d2a86068b92d7ee6b47b7af6dd506f456b589a50a6cac7e0e8d15d23246b3fb4  Architect/templates/seed/README.md
b52a22d2012e7a640e68300a2a8f0a985e811e024c0259b26d7d0aabc6ec37ea  Architect/examples/authoring-a-skill/planning.md
aa52ab3b03b9e78ea7ca977d7dacfac515d8e21dbdd5c2faf97004abb563b600  Architect/examples/authoring-a-skill/README.md
ef8f14ad864972aa29da93ae70267565107b90651aa8e7f76e0acb3bc8cadfc7  Architect/changes/hardening-cycle-1/0-baseline.md
794a40e7d54e913efe2c0d05e6f5360f731737ae241ef8d929480b4426bcbb11  Architect/changes/hardening-cycle-1/decisions.md
62227eb1d9c9c107cacfe1517ba16c51982da95e20b583bbaa9af2467ba00a66  Architect/changes/hardening-cycle-1/1.5-criteria.md
0c7395c7dda6fc2d12c538c835d6174368b6cd8057ebec82341ef8af7859db78  Architect/changes/hardening-cycle-1/3-redteam-plan.md
2cef5e9df0bdd259fd55a3d4c426f2df3a60f77c66bec585463f066337300361  Architect/changes/hardening-cycle-1/3-redteam-plan.pass2-C.verbatim.md
d79d9092b129ef382ae914e0874236109689be92fe38d99e83e5cfa458f0940f  Architect/changes/hardening-cycle-1/3-redteam-plan.pass2-A.verbatim.md
2555a812c1ca6ed355a128edeb7611df5248a80ae7c05948221498500c56d230  /home/zero/architect-hardening-loop/LOOP-STATE.md
94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8  /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
```

Also read (baseline copies, materialised by me via `git archive b08f5a9 Architect`, for count verification only): the same artifact file set at `b08f5a9`, plus `Architect/changes/initial-authoring-2026-07/fixtures/` (for C/O3's `## Layer-2 required sections` count). Precedent run `Guarded_change/changes/audit-hardening-2026-07/` was enumerated (`ls`) and searched; it contains **no `oracles/` directory and no `check.sh`**, so the "positive-per-site-assertion checker plus baseline replay" precedent could not be inspected as a concrete comparison bar — reported as **unverifiable**.

**Claims I could not check:** `oracles/check.sh` and `oracles/baseline-replay.sh` do not exist (`ls Architect/changes/hardening-cycle-2/oracles/` = `idcollide.sh`, `ruleid-sitemap.sh`), so every `P` and `M` result is a promise, judged only as a specification. `fixtures/` is empty, so no X arm could be inspected. `B5`'s live-copy claim (`diff -rq /home/zero/.claude/skills/architect …`) was not run — outside my frame.
