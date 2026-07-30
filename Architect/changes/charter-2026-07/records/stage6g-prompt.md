# Gate 7, pass 5 — TARGETED cold red-team (2026-07-30)

You are a **cold, independent reviewer**, with no shared context with this artifact's author or with the
two reviewers dispatched alongside you. **Nothing here is true because it is written here** — every claim
below is the author's, including the author's account of what it repaired, of what earlier reviewers found,
and of what the owner ruled.

Repo root: `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

**Why this round exists.** Four full rounds have run (records `reviewer-{A..W}-verbatim.md`). Pass 4 (U, V,
W) returned blocker/blocker/major. A **fresh runner with none of the previous runner's context** then
adjudicated those three reports and made 18 repairs. **Your scope is those repairs and the criteria
amendments made alongside them.** You are not asked to re-derive the whole artifact — but you are not
forbidden from filing anything you find.

**The single most important thing to know about this run's history:** three passes in a row, a repair was
found to be **written narrower than the claim made for it**. The author of these repairs is a different
agent from the one that wrote the previous three — but it is still the author of *these*. Assume the same
failure mode.

---

## 1. THE ARTIFACT — verify every hash. If one differs, say so and stop.

`Architect/stages/`, nine files, **1,310 lines**.

| File | sha256 |
|---|---|
| `charter.md` (manifest, **not dispatched**) | `55def0c83de60e94d1d27e1839e8d8e0c66920703ec407192652544dc95d1b4f` |
| `charter-common.md` (verbatim to every role) | `02c1027557a6628ce75432c084a72f23c75696a732273a9345ae7846cda760cd` |
| `redteam.md` | `c28fcbcf634ee5b781872a6da8776ccddb162ff1c1346750fbc303d02102b838` |
| `redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` |
| `redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` |
| `divider.md` | `68624054ff2e51e439a41f6ab4edd895927b64601b6e91e21709146f044fb6af` |
| `combiner.md` | `2be8e0f5d2691c9cbfa32f869f72f44825b5335fe1c00936d732f322d3f3871e` |
| `leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` |
| `node.md` | `1ee43d97de9d52735860c97de957295610ad3ea8f493ecd9f70047a012e8b1e8` |

A dispatched prompt is `charter-common.md` **verbatim** + role file(s). **Review the composed prompt**, not
the files in isolation — two defects in this run's history were visible only after concatenation.

The harness: `Architect/changes/charter-2026-07/oracles/` —
`ruleplace.sh` `be60b9b0c6c4b53b7bb46ea45c823777a777e5e10aee4ca6d0add2daca537ba3`,
`rules.tsv` `43ae09c23b3a941fc25adae40c22a0f47e1eb92020a12c42cb32ee12934fdf66`,
`declared-duplications.jsonl` `ae4e6a24902847e5357387ce2e5fa773f9755286bb912e644cbf4cd28c8ab9e7`,
`shared_spans.py` and `mutation-test.sh` **unchanged** from pass 4.

## 2. AUTHORITY — and a standing warning

1. **The owner's words**, at their record index in
   `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`.
   **The only admissible source.** ⚠ **Read the WHOLE record around any quote** — three times in this run a
   quote presented as a ruling was part of a longer message whose omitted part mattered.
   ⚠ **Record numbers are 1-BASED: record N is line N of that JSONL.** Read one with
   `sed -n 'Np' <jsonl>`, not by indexing a parsed list — the author of these repairs made exactly that
   mistake, reported all its loci one low, and then wrote the error up as an off-by-one *in the corpus*.
   It is retracted in `decisions.md` ADJ-2 and all citations are corrected, **but treat every locus below
   as a claim to re-verify, not as an address you can trust.**
   Loci this round turns on: **1044** (the owner's ORIGINAL spec — an `attachment` record, 2,278 chars),
   **1254** (the question) and **1258** (the answer) on the backstop cap, **1449** (items 1–5), **2524**
   (items 1–3), **2544** (the testing rule), **2680**. Also **1274**, **1572**, **1762**, **1829**.
2. **`~/Documents/Architect.md`** — 131 lines, sha256
   `8ad9d620be794047b3606e948e20d3cd70b5413c36b9dd19f0dc97d8d107a474`. ⚠ **Owner-SEEDED, not
   owner-written**: the owner's original is **59 lines / 2,278 chars** at record **1044**, and **every
   function signature in the file today is agent-written** — the owner's `Spawn_leaf` took no
   `granularity` at all. *"The spec says X"* is not *"the owner said X."*
3. `Guarded_change/stages/charter.md` and `stage-4.md` (fork source) ·
   `changes/charter-2026-07/0-baseline.md` (B01–B19).

## 3. SCOPE A — the 18 repairs. The author's own account is `decisions.md`, section **ADJ-4**.

Read ADJ-4's table. **For each repair, the question is the same and it is the one this run keeps failing:
did it close the CLASS, or only the instance the reviewer happened to name?** Attack these specifically:

| # | The repair | What to attack |
|---|---|---|
| 1 | **§0 gains a PER-ROLE destination table** for prompt-set reports, replacing one universal remedy | Is each named destination **actually reachable in that role's return type**? Check `~/Documents/Architect.md`'s signatures yourself. The divider's row says its block rides on the **stated seam** and reaches `Human_gate` — **`Human_gate` only fires at `depth <= gate_depth`. What happens deeper?** The leaf's row says `Consensus` "does not vote on it" — is `Consensus` actually told that, and is that instruction in a file the leaf's own reader can rely on? |
| 2 | **`Severity` is declared to have NO destination**, and `combiner.md`'s *"say so in your return value"* is deleted | Is telling a role *"you have no channel, do not improvise one"* an honest fix or an abdication? **Find a fourth route by which a non-finding can enter `task`.** |
| 3 | **§2's floor escape no longer says `blocker`**, and no longer points at a deleted §0 clause | Trace the floor from `Spawn_redteam`'s signature to the reviewer's output. **Is there still any route by which an inoperable floor becomes a finding?** |
| 4 | **§2 split into *whether* you hold a floor (signature) and *how* it binds you (role file)** | U ruled the old *"by signature alone"* false of its own table. **Is the new split real, or the same dissolution reworded?** |
| 5 | **`node.md`'s branch override rewritten** — finer only, never coarser, with an operable test | V held the old discriminator (*"looks delicate"* vs *"genuinely warrants"*) was one judgement stated twice. **Is the new test operable by an agent that has only its own prompt?** |
| 6 | **The divider's self-review loop CAPPED at three rounds**, exhaustion returns `null` | **The cap number and the exhaustion value are the author's, not the owner's.** Is `null` safe, or does it misreport an unsplit task as atomic in a way the run cannot recover from? Trace what the node does with it. |
| 7 | **The register's 8 global amnesties are now scoped**, 4 entries added, and `charter.md`'s table is **generated** from the JSONL | **Break it again.** Reviewer U widened `leaf.md`'s closed set by one line and passed both oracles; that specific mutation now fails. **Find another.** This is the highest-value thing you can do this round. |
| 8 | **N-03's retirement made symmetric**; **N-32 wired in**; **a `lastline` probe mode added** for N-14 | Run the oracles. Then **find a gating criterion whose probe tests a strictly weaker claim than the criterion states** — reviewer U found N-04 in that state and it is **not** repaired. |
| 9 | **SEV4's non-port declared** in `charter.md`, warranted by owner record **1258** | **Read 1254 and 1258 in full.** The author claims 1258 settles the substance of what reviewer V called a blocker. **Does it?** Note what 1258 does *not* cover. |
| 10 | **`charter.md` corrections**: the false claim about what §2 says; the false claim that record 1449 item 3 ratifies the spot-verify duty's location | **Read 1449 in full.** Are there other owner attributions in the set that its record does not support? |

## 4. SCOPE B — the criteria bar was AMENDED MID-RUN. This is the self-certification risk.

`1.5-criteria-v2.md` gained an **FRZ-3** block. Two rows were amended **because they were factually false
against the artifact they gate** (N-14, N-24); three were added (N-38, N-39, N-40).

**FRZ-2's own text says an author who edits the bar mid-run and then measures themselves against it is
committing the failure this loop exists to prevent.** So:

- **Are the amendments right, or convenient?** N-14 and N-24 were amended by the same agent whose repairs
  they now measure.
- **Are the additions written from the shipped text?** Reviewer O ruled two of FRZ-2's additions defective
  on exactly this ground — one was *"a transcription of the repair, so it cannot fail against it."*
  **Check every FRZ-3 row against that test.** A criterion written by reading the repair is not a bar.
- **Do the new probes have real discriminating power?** Each is claimed can-fail tested in ADJ-4.
  **Reproduce at least two of those can-fail tests yourself.**

## 5. SCOPE C — the residue the author declares it cannot close (`decisions.md` **ADJ-5**)

The author halts for the owner on three **design-level** items, claiming each needs a change to
`~/Documents/Architect.md`: **(1)** the leaf has no source access and cannot be given any without changing
`Spawn_leaf`'s signature; **(2)** `Severity` has no destination for the findings it filters out, because
the spec says minors are *"recorded against the plan"* and names no actor; **(3)** *"or get stuck"* is
owner-written and defined nowhere.

**Confirm or refute each claim that it is design-level.** If any one of them can in fact be closed inside
the prompt set, say so and say how — that would mean the author halted for the owner on something that was
its own to fix, which is the error two pass-4 reviewers named.

## 6. RUN THE ORACLES YOURSELF. Reading them is not enough.

```
cd Architect/changes/charter-2026-07
./oracles/ruleplace.sh    ../../stages
./oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl
./oracles/mutation-test.sh ../../stages
```
Author's claim: **133/0 (+21 SMOKE, gating in neither direction)**, **0 undeclared spans**, **144/0
mutants**, and each script **exit 2** with no argument. ⚠ **Capture exit codes directly, not through a
pipe** — `$?` after a pipe is the last command's status, and this project has twice recorded a script
exiting non-zero as `exit=0`, once in the file whose purpose was proving otherwise.

## 7. YOUR RECORD

Follow `charter-common.md` §5: path + sha256 of every file you read, your agent type and model, what you
ran, and **what you did NOT check — reported as unchecked, never as accepted.** Your final message is the
record; it is extracted verbatim from the harness transcript, so **do not summarise at the end** — the last
assistant message is what is kept.

**Everything in §§1–6 of this prompt is author-authored supplementary context** and must be quoted as such
in your record, per §0/§5.

**Verdict, one word, from: `blocker` / `major` / `minor` / `clean`.** An earned-clean verdict requires you
to state what you checked that could have failed and did not.
