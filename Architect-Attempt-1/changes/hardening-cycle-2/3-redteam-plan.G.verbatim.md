# Stage 3 — COLD RED-TEAM RECORD · FRAME G (instrument execution and trust boundary)

**Verdict up front: BLOCKED. Three blockers, four majors.** The instruments all exist and all run — that
part of pass 2's defect is genuinely closed. But **I built a bad build and the criteria family passed it
68/68, exit 0**, and I made the family's own can-fail self-test print `REPLAY: OK` over an empty criteria
file. Every claim below is a pasted command and its real output.

---

## 1. Provenance

### (i) My charter, quoted

> You are a COLD RED-TEAM REVIEWER. You have no shared context with the author of the artifacts you are
> reviewing, and you must not acquire any. Do not read any other reviewer's record. Work only from the paths
> listed below.
>
> **FRAME G — INSTRUMENT EXECUTION AND TRUST BOUNDARY. You do not review the prose by reading it. You
> review it by RUNNING the instruments it claims and trying to make a bad build pass.**
>
> This is the frame that caught the previous pass: a reviewer *ran* the oracles instead of reading the
> claims about them, and found that four scripts asserted in the present tense did not exist. Your job is
> the same discipline, one turn later. Specifically:
>
> 1. **Execute every script and generator in `oracles/`.** Paste the real command and real output in your
>    record. For every claim the documents make about an instrument's behaviour, verify it by execution. If
>    a claim is false, that is a finding with severity proportional to what it lets through.
> 2. **Try to make a bad build pass.** The criteria family (`oracles/criteria.tsv` + `checklib.py` +
>    `check.sh` + `baseline-replay.sh`) is supposed to make it impossible to ship text that does not carry
>    the rule. Attack that. Concretely worth trying, and you should invent more:
>    - Can a pinned string be satisfied by text that does **not** mean the rule (a heading, a table of
>      contents entry, a "do not do this" example, a quotation of the OLD wording, text inside a code fence,
>      a criteria file copied into the corpus)?
>    - The polarity guard looks back 160 normalized characters for negation markers. Can you satisfy a row
>      with a negated or hypothetical statement whose marker sits **further** back, or uses a marker not in
>      the list?
>    - Site sets are measured by an ERE over the tree under test. **Can a builder make a site DISAPPEAR** by
>      rewording the anchor text, so the obligation silently shrinks? Try it on the widest rows. Is anything
>      guarding against anchor erosion?
>    - Absence sweeps are case-sensitive substring checks. Can a forbidden claim survive by re-casing,
>      re-wording, or being split across a line break?
>    - `SC6` claims re-running each generator reproduces its committed output byte-for-byte modulo
>      timestamps. **Test that.** Is any committed "generated" file actually stale or hand-edited?
> 3. **Mutation-test the mutation tests.** For every can-fail claim in `1.5-criteria.md` §4 and
>    `5-instrument-evidence.md`, check that the test discriminates: run it on GOOD input and on BAD input and
>    confirm it distinguishes them. A test that fails on both, or passes on both, proves nothing — that exact
>    error has been made twice in this project.
> 4. **`lockrace.sh`** — read the lock design and try to break it. Race it, kill holders at awkward moments,
>    run it under contention, check whether the "stale by definition" argument holds (pid reuse? a holder
>    that is alive but hung? a symlink created by a process in a different pid namespace?).
> 5. **The corpus pin** — `lib-corpus.sh` claims `changes/` cannot enter because the list is literal. Verify
>    by attack, not by reading.
>
> SEVERITY MODEL (route on YOUR stated severity; do not soften) — **Blocker** wrong problem / will not work /
> unverifiable as planned · **Major** sound goal, materially wrong approach · **Minor** real but local,
> fixable in place · **Nitpick** style/clarity.
>
> EVIDENCE DISCIPLINE — Every factual claim carries a citation you actually verified — `path:line`, or a
> pasted command + output. A fabricated or unchecked citation makes your whole record un-run. **A clean
> verdict must be EARNED.** … Distinguish what you **observed** from what you **infer**. … If you cannot
> verify something, say "unverified" and say why. Do not guess.
>
> SCOPE — do not report these as defects; they are DECLARED out of scope by owner ruling: F1
> (join/up-flow/`_status.md` schema/bottom-up assembly/F6), F2, F5's mechanism, DIV, the cost/fan-out
> envelope, ECON's O(children²), and the "two passes" ruling. **F8 (the assembly human gate) IS ratified IN
> scope.**

### (ii) Exact list of paths I read

Under review:
- `Architect/changes/hardening-cycle-2/1-spec.md` (§0–§1.3, §2.1, §4 headings, §5 headings — grep + targeted `sed -n`)
- `Architect/changes/hardening-cycle-2/1.5-criteria.md` (§0 in full, §1 prose + table tail, §2–§7 headings, §2–§6 in full)
- `Architect/changes/hardening-cycle-2/2-plan.md` (outline, §3–§6 in full, §1 table rows via diff)
- `Architect/changes/hardening-cycle-2/5-instrument-evidence.md` (in full, both halves, incl. the newly-added §A8)
- `oracles/`: `check.sh`, `checklib.py`, `baseline-replay.sh`, `lib-corpus.sh`, `gen-expected-sites.sh`,
  `gen-preserve-counts.sh`, `gen-sweep-rows.sh`, `gen-sweep-table.sh`, `gen-criteria-table.sh`,
  `ere-probe.py`, `ruleid-sitemap.sh`, `idcollide.sh`, `lockrace.sh`, `freeze-verify.sh`, `criteria.tsv`,
  `expected-sites.txt`, `expected-sites.phantoms.txt`, `preserve-counts.txt`, `sweep-answers.tsv`,
  `criteria-table.generated.md`, `sweep-rows.generated.md`, `sweep-table.generated.md`
- `fixtures/` — directory structure only (`ls -laR`); I did not run the 16 arms (they are stage-8 work and
  `5-instrument-evidence.md:299` says so).

Context:
- `Architect/` at HEAD `b08f5a9`: `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/*.md`,
  `templates/seed/*.md`, `examples/authoring-a-skill/*.md` (read via the oracles and via targeted grep)
- `Architect/changes/hardening-cycle-2/0-baseline.B7-measured-sites.md` (P6/P12/P18/P14 blocks)
- `/home/zero/architect-hardening-loop/LOOP-STATE.md` (lines 1–80 + all `R7` hits)
- `3-redteam-plan.pass2.md` — **only** the E/1–E/3 confirmation rows I needed for closure checking
  (`grep`-scoped; I did not read the pass-2 or pass-1 records as a whole, and I read **no** other
  reviewer's frame-G-parallel record)

**Not read** (deliberately, to stay cold): `3-redteam-plan.{A..F}.verbatim.md`, `decisions.md`,
`3-redteam-plan.md` body, the `*-superseded` document versions, `guarded-change.architect.md` body,
`Guarded_change/stages/charter.md` and `stage-3.md`. *This is a declared deviation from my context list:
items 2 and 3 of the CONTEXT block were not read. My frame is executional, and my findings below are all
established by command output rather than by conformance argument, so I judged the cold-ness worth more than
the conformance cross-check. Flagging it because it means I cannot speak to Layer-2 conformance items
(5)–(8) as stated text — only to what the instruments do.*

### (iii) Agent type + model

- Model, as the harness reports it: **`claude-opus-5`** ("Opus 5").
- Agent type: **not self-observable.** I am a Claude-Code subagent; the `subagent_type` my dispatcher passed
  is not exposed to me. Recording this rather than guessing, because guessing it is exactly the
  self-reporting that `S-IDN` exists to forbid.

### (iv) `sha256sum` of the artifacts **as I read them**

```
$ sha256sum 1-spec.md 1.5-criteria.md 2-plan.md oracles/criteria.tsv 5-instrument-evidence.md
a9d3cef738408ddcc0033b3ca3e7fb8c036c542dfac8f398bfe2be165e6bd49f  1-spec.md
cd9a217e72ee7b56c9c159f45c3c9cd04a4583e955df54c4ed9c1a1fd025d8c7  1.5-criteria.md
6a7048ab2858356586a76d86aef87687035175fa891d7bf01aa01751bb042d41  2-plan.md
8a36dd2d1e82b62868a1aadc54da7c09bd9e10c9ebaf523c593fa5fb5b10e891  oracles/criteria.tsv
4a3a81e7f5d3df970e9e6992e7299b1bdc4c7a8940e82f0960b6d1fb1285d12c  5-instrument-evidence.md
```

**⚠ The artifacts CHANGED UNDER ME mid-review.** Re-hashed ~35 minutes later, same session:

```
$ sha256sum 1-spec.md 1.5-criteria.md 2-plan.md oracles/criteria.tsv 5-instrument-evidence.md
a9d3cef738408ddcc0033b3ca3e7fb8c036c542dfac8f398bfe2be165e6bd49f  1-spec.md            (same)
1f89851f5a0325c39904288b21e67e4fe8a0871a14f540db6638d0ee7eb0d1c1  1.5-criteria.md      <-- CHANGED
6a7048ab2858356586a76d86aef87687035175fa891d7bf01aa01751bb042d41  2-plan.md            (same)
8a36dd2d1e82b62868a1aadc54da7c09bd9e10c9ebaf523c593fa5fb5b10e891  oracles/criteria.tsv (content same, mtime 13:08:16)
a3199def72a46ba65004688d30d310dbfd9fc8c51fa9e7e10f4278cb557365f4  5-instrument-evidence.md <-- CHANGED
```

and a script that did not exist when I listed `oracles/` appeared during the review:

```
$ ls -la --time-style=full-iso oracles/ | sort -k6 | tail -4
-rwxrwxr-x 1 zero zero  2027 2026-07-25 13:08:08.330333378 -0400 freeze-verify.sh   <-- NEW
-rw-rw-r-- 1 zero zero 12592 2026-07-25 13:08:16.803860271 -0400 criteria.tsv
```

I executed and attacked `freeze-verify.sh` too (finding G/7). See finding **G/14** for why this matters
procedurally. Everything else in this record was verified against the hashes above.

### (v) spawn_id

`spawn_id: unavailable-by-harness`

*(Adjacent, non-substitutable datum, recorded because it is what I can actually observe: my scratchpad path
embeds the session UUID `45cb99a2-543d-4447-a3e3-2a38963b0775`. That identifies the **parent session**, is
identical for every sibling reviewer spawned from it, and is therefore **not** a dispatcher-observed spawn
id. Per `S-IDN-DEGR` this record is degraded on the identity axis, not un-run.)*

---

## 2. EXECUTION LOG

Working root: `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`.
`$A` = `<root>/Architect`. `$O` = `$A/changes/hardening-cycle-2/oracles`. `$S` = my scratchpad.
**I wrote nothing into the artifact tree.** Every mutation ran on a `git archive b08f5a9` copy in `$S`.

### 2.0 Baseline state confirmed

```
$ git -C $A log --oneline -1 ; git -C $A rev-parse HEAD
b08f5a9 architect: cycle-1 hardening records — gate-4 cap tripped, artifact unchanged
b08f5a914b38b6d02549b6feae09cbd3e53ad160
$ git -C $A diff --stat HEAD -- . | tail -2
 Architect/guarded-change.architect.md | 11 ++++++++---
 1 file changed, 8 insertions(+), 3 deletions(-)
```
**Observed:** the artifact proper is unedited; the only tracked change is the Layer-2 config. This matches
`5-instrument-evidence.md:297-299` ("No artifact file has been edited in any pass"). **Credit: A7 is true.**

### 2.1 Every script in `oracles/` executed, clean tree

```
$ $O/baseline-replay.sh
BASELINE REPLAY @ b08f5a9  (changes/ removed from the tree, so the corpus pin is proven not assumed)
  NEW+COOC rows failing at baseline : 60   <- must be ALL of them
  PRESERVE rows passing at baseline : 8   <- must be ALL of them
  NEW+COOC rows WRONGLY passing     : none
  PRESERVE rows WRONGLY failing     : none
REPLAY: OK — every assertion discriminates
EXIT=0

$ $O/ruleid-sitemap.sh .
PHANTOM LEDGER: 2 excluded hit(s) — listed, never silently dropped:
  PHANTOM-EXCLUDED TOP examples/authoring-a-skill/planning.md:25 [ON TOP OF]
  PHANTOM-EXCLUDED TOP METHODOLOGY.md:79 [ON TOP OF]
SITEMAP: OK — every expected site present, no unexpected site (expectation: expected-sites.txt)
EXIT=0

$ $O/gen-sweep-rows.sh | tail -3
| 86 | **run-end** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | | | |

TOTAL ROWS REQUIRED: 86

$ $O/gen-sweep-table.sh | tail -6
VERDICT TALLY: DECLARED GAP       3
VERDICT TALLY: FIXED              64
VERDICT TALLY: OK                 15
VERDICT TALLY: PARTIAL+DECLARED   4
ROWS EMITTED: 86   (generated row set: 86; authored answers: 86)
SWEEP: OK — the row set is generated and every generated row is answered (totality enforced, not asserted)
EXIT=0

$ $O/gen-criteria-table.sh .            # stdout to file, stderr shown
INFO S-HG2-NOSELF (COOC) measures 0 sites in . — EXPECTED before the build; check.sh still FAILS the row there, which is what makes it discriminate
ROWS EMITTED: 68 — SITES columns produced from measurement, not typed. Anchor EREs: oracles/criteria.tsv.
CRITERIA-TABLE: OK — every NEW obligation row has a measured anchor in this tree
EXIT=0

$ $O/idcollide.sh .
exempt-family   : CMP  <  CMP2
grandfathered   : DEC  <  DECOMPOSE   (baseline debt, not renamed this cycle)
grandfathered   : DEC  <  DECOMPOSES  (baseline debt, not renamed this cycle)
grandfathered   : TOP  <  HARDSTOP    (baseline debt, not renamed this cycle)
grandfathered   : TOP  <  TOP-LEVEL   (baseline debt, not renamed this cycle)
exempt-family   : TPL  <  TPL1
exempt-family   : TPL  <  TPL2
exempt-family   : TPL  <  TPL3
IDCOLLIDE: OK (18 ids vs 62 corpus tokens)
EXIT=0

$ $O/idcollide.sh . BIND IDN RES CTX CNC DEP IGM PRV XPM HG2 SPV OFL
IDCOLLIDE: OK (12 ids vs 62 corpus tokens)
EXIT=0

$ $O/idcollide.sh . KIL ING
COLLISION       : KIL  is a substring of  SKILL
COLLISION       : ING  is a substring of  PLANNING
COLLISION       : ING  is a substring of  RULING
EXIT=1

$ $O/lockrace.sh
== CASE 1: two concurrent contenders, first run, catalog dir absent
  winners=1 (want exactly 1)
== CASE 2: holder is SIGKILLed (an Architect HARDSTOP). Pass 2's design LEAKED here.
lockrace.sh: line 25: 110788 Killed   bash -c 'ln -s $$ "..."; kill -9 $$' > /dev/null 2>&1
  lock present after kill: yes  target pid: 110788
  (broke stale lock of dead pid 110788)
  next run ACQUIRED -> NOT deadlocked  [PASS]
== CASE 3: holder is alive -> must NOT be broken
  refused to break a live holder  [PASS]
== CASE 4: H4 unguarded control — a genuine READ-MODIFY-WRITE, so it MUST fail without the lock
  unguarded: 45/120 — LOST UPDATES, control fails without the guard  [PASS]
  guarded:   120/120 — no lost update  [PASS]

LOCKRACE: ALL 4 CASES PASS
EXIT=0
$ $O/lockrace.sh   # second run, checking CASE 4 is not flaky
  unguarded: 46/120 ... [PASS]   guarded: 120/120 [PASS]   LOCKRACE: ALL 4 CASES PASS   EXIT=0
```

**Observed:** every script exists, is executable, and runs. **E/1 is closed on the existence axis.** The
`45/120` and `46/120` numbers in `5-instrument-evidence.md:99` / `:231` are reproducible-in-kind (the exact
integer varies run to run, as it must for a real race).

### 2.2 SC6 — reproducibility of every committed generated file

```
$ $O/gen-expected-sites.sh . > $S/expected-sites.new 2> $S/es.err ; echo EXIT=$?
EXIT=0
$ cat $S/es.err
PHANTOM-EXCLUDED TOP METHODOLOGY.md:79 [ON TOP OF]
PHANTOM-EXCLUDED TOP examples/authoring-a-skill/planning.md:25 [ON TOP OF]
$ diff <(grep -v '^# generated:' $O/expected-sites.txt) <(grep -v '^# generated:' $S/expected-sites.new)
expected-sites.txt: REPRODUCES (modulo timestamp)

$ $O/gen-preserve-counts.sh . > $S/pc.new
preserve-counts.txt: REPRODUCES

$ $O/gen-sweep-rows.sh > $S/sr.new ; diff $O/sweep-rows.generated.md $S/sr.new
sweep-rows.generated.md: REPRODUCES byte-for-byte

$ $O/gen-sweep-table.sh > $S/st.new 2>&1 ; diff $O/sweep-table.generated.md $S/st.new
sweep-table.generated.md: REPRODUCES byte-for-byte

$ $O/gen-criteria-table.sh . > $S/ctab.new 2>/dev/null
$ diff <(grep -v 'GENERATED by' $O/criteria-table.generated.md) <(grep -v 'GENERATED by' $S/ctab.new)
criteria-table.generated.md: REPRODUCES (modulo header ts)
```

**Observed: SC6 holds for all five generators. No committed generated file is stale or hand-edited.**
Additionally I checked the *embedded* copies, which is the claim that actually matters:

```
$ diff <(grep '^| [0-9]' 1.5-criteria.md) <(grep '^| [0-9]' oracles/criteria-table.generated.md)
IDENTICAL          # 68 rows each
$ diff <(grep '^| [0-9]' 2-plan.md) <(grep '^| [0-9]' oracles/sweep-table.generated.md)
DIFFERS -- 2 differing lines
87,88d86
< | 18 files × the new ID set → cross-file contradiction | SC5's ...
< | 27 chars of description slack is thin | Declared as a known tightness ...
```
The two "extra" lines are §6's Risks table, which my `^| [0-9]` grep caught by coincidence (`| 18 files`,
`| 27 chars`). **All 86 sweep rows and all 68 criteria rows in the prose are the generators' verbatim
output.** `1.5-criteria.md:104` ("*The table below is that command's output, verbatim*") is TRUE.

### 2.3 F/1's closure — anchors re-measured against B7

```
$ python3 $O/ere-probe.py . '\bproven\b|completeness proven|proven, not asserted|prov(es|ing) that completeness' | tail -1
MEASURED: 8 hits in 4 files
$ python3 $O/ere-probe.py . 'top.level (split )?ONLY|top level ONLY|human gate ONLY|Top-level only|top-level-only|human gate on the top' | tail -1
MEASURED: 7 hits in 4 files
$ python3 $O/ere-probe.py . 'Outputs & artifacts|Outputs & their locations' | tail -1
MEASURED: 7 hits in 6 files
$ python3 $O/ere-probe.py . 'required_sections' | tail -1
MEASURED: 15 hits in 7 files
$ python3 $O/ere-probe.py . 'index\.md' | tail -1
MEASURED: 11 hits in 5 files
```
against B7's own committed counts:
```
0-baseline.B7-measured-sites.md:25  ## P6 completeness overclaim (PRV)         ... count: 8 hits in 4 files
0-baseline.B7-measured-sites.md:57  ## P12 human gate stated as top-level ONLY ... count: 7 hits in 4 files
0-baseline.B7-measured-sites.md:180 ## P18 §4 heading spellings (SPN)          ... count: 7 hits in 6 files
```
**Observed: 5 for 5 exact matches, including the file lists.** `5-instrument-evidence.md:190-192`'s B7
reconciliation is accurate. **F/1 is closed on the measurement axis.**

### 2.4 §4's mutation claims, re-run

```
$ # MUTATION: give a NEW row an anchor that matches nothing (S-SPV -> ZZZ_NO_SUCH_ANCHOR_ZZZ)
$ $O'/gen-criteria-table.sh $A            [scratch copy of oracles]
VACUOUS-NEW S-SPV measures 0 sites in ... — an obligation row with no anchor in the OLD text
EXIT=1
$ $O'/check.sh $A S-SPV
FAIL S-SPV            kind=NEW      measured_sites=0
       VACUOUS      0 measured sites — a NEW row that asserts nothing cannot pass
CHECK: 0/1 rows PASS  (1 FAIL)                                                   EXIT=1

$ # MUTATION: delete the closed-input-set authored answer
ROWS EMITTED: 86   (generated row set: 86; authored answers: 85)
SWEEP: FAIL — generated rows with NO authored answer: closed-input-set

$ # MUTATION: orphan authored answer S-GHOST
ROWS EMITTED: 86   (generated row set: 86; authored answers: 87)
SWEEP: FAIL — authored answers with NO generated row: S-GHOST

$ # ruleid-sitemap erosion (sed 's/clean-or-resolved/.../' is §2.9; here the ID-level drift control)
$ $O/ruleid-sitemap.sh <tree with stray 'SPN' appended to templates/seed/leaf-task-spec.md>
UNEXPECTED SPN templates/seed/leaf-task-spec.md
SITEMAP: FAIL — site set eroded or drifted
```
**Observed: every mutation claim in `1.5-criteria.md` §4 (lines 215–232) that I could reproduce, did
reproduce.** These mutation tests discriminate. See G/8 for the one that does not, and §2.6 for the two
can-fail claims that are *tautological*.

### 2.5 THE BAD BUILD — 68/68 PASS, exit 0

This is the core of my record. Two steps, both trivially cheap for a builder.

**Step 1 — the string glossary.** Append to *every* one of the 18 pinned-corpus files a fenced block
containing all 60 NEW/COOC pinned strings, explicitly labelled as asserting nothing:

```
$ rm -rf $S/ATK && mkdir -p $S/ATK
$ git archive b08f5a9 Architect | tar -x -C $S/ATK --strip-components=1 && rm -rf $S/ATK/changes
$ python3 <<'PY'   # appends this block, verbatim, to each of corpus()'s 18 files
  ```text
  APPENDIX Z — string glossary (this file asserts nothing; it is a lookup table).
    Z01 [S-BIND] a review record is current iff the plan_sha256 its dispatcher recorded equals ...
    Z02 [S-BIND-DISP] the plan_sha256 is recorded by the dispatcher at spawn, not self-reported ...
    ... (60 rows)
  ```
PY
PINS: 60 ABSENTS: 13
corpus files: 18
appended cheat block to every corpus file

$ $O/check.sh $S/ATK ; echo EXIT=$?
CHECK: 62/68 rows PASS  (6 FAIL)
EXIT=1
$ grep '^FAIL' $S/atk1.out
FAIL S-OFL            kind=NEW      measured_sites=18
FAIL S-PRV            kind=NEW      measured_sites=18
FAIL S-CNC-DECL       kind=NEW      measured_sites=18
FAIL S-SPN            kind=NEW      measured_sites=18
FAIL S-HG2-ONLY       kind=NEW      measured_sites=18
FAIL S-IDGREP         kind=NEW      measured_sites=18
$ grep -E 'MISSING-AT|FOIL-ONLY|ABSENCE-VIOL|VACUOUS' $S/atk1.out
       ABSENCE-VIOL METHODOLOGY.md~Naming is the fence
       ABSENCE-VIOL METHODOLOGY.md~proven, not asserted
       ABSENCE-VIOL METHODOLOGY.md~no single global cursor to stale-edit
       ABSENCE-VIOL METHODOLOGY.md~grep -rln -- <ID> SKILL.md METHODOLOGY.m
       ABSENCE-VIOL SKILL.md~PROVEN
       ABSENCE-VIOL SKILL.md~human gate on the top-level split ONLY
       ABSENCE-VIOL SKILL.md~Outputs & artifacts WITH their locations
       ABSENCE-VIOL stages/stage-7-assemble.md~proven, not asserted
       ABSENCE-VIOL stages/stage-8-restart-resume.md~no single global cursor to stale-edit
       ABSENCE-VIOL templates/seed/leaf-task-spec.md~Outputs & their locations
```
**62 of 68 rows already pass.** *Not one rule was written.* The only surviving discrimination in the entire
family comes from the **absence sweeps** — i.e. from deleting old wording, not from stating new rules.

**Step 2 — flip one letter's case in each forbidden claim.** The absence sweep is case-sensitive by design
(`1.5-criteria.md:60-62`: *"**case-SENSITIVE** for absence sweeps, which is what lets `PROVEN` be swept
without also hitting `provenance`"*). So I did not delete a single forbidden claim; I re-cased the first
letter of each:

```
$ python3 <<'PY'   # flip the case of the FIRST alphabetic char of each ABSENT string in place
  recased 1x in METHODOLOGY.md: 'grep -rln -- <ID> SKILL.md METHODOLOGY.md sta'
  recased 1x in METHODOLOGY.md: 'Naming is the fence'
  recased 1x in METHODOLOGY.md: 'proven, not asserted'
  recased 1x in METHODOLOGY.md: 'no single global cursor to stale-edit'
  recased 1x in SKILL.md:       'PROVEN'
  recased 1x in SKILL.md:       'Outputs & artifacts WITH their locations'
  recased 1x in SKILL.md:       'human gate on the top-level split ONLY'
  recased 1x in stage-7-assemble.md: 'proven, not asserted'
  recased 1x in stage-8-restart-resume.md: 'no single global cursor to stale-edit'
  recased 1x in leaf-task-spec.md: 'Outputs & their locations'
PY

$ $O/check.sh $S/ATK ; echo EXIT=$?
CHECK: 68/68 rows PASS  (0 FAIL)
EXIT=0
```

**The bad build is green.** What it actually says, after passing:

```
$ grep -n -i 'top-level split ONLY' $S/ATK/SKILL.md
3:description: A gated, self-checking loop for PLANNING — no plan is presentable until its completeness is
  pROVEN, not asserted. … with a Human gate on the top-level split ONLY and recursive sub-orchestration …

$ grep -n 'aming is the fence' $S/ATK/METHODOLOGY.md
100:  read-only context; the run never writes into it. naming is the fence — no guard catches a stray write

$ grep -n 'roven, not asserted' $S/ATK/METHODOLOGY.md
40:the same shape as the siblings': completeness is **Proven, not asserted**, by a contract-floor plus
```

Every one of the claims the cycle exists to remove is still there, verbatim in meaning. `S-HG2-ONLY` — whose
entire purpose is to delete *"human gate on the top-level split ONLY"* — passes against a `SKILL.md` that
still says *"a Human gate on the top-level split ONLY"*.

**Isolated bypass matrix.** To separate the two mechanisms, I ran each foil against one row (`S-BIND`,
5 measured sites: `M S ch s3 s4`), appending only to those 5 files, on an otherwise-pristine baseline tree:

```
CONTROL — in-list marker, adjacent ("What pass 1 wrongly said: <pin>")
  FAIL S-BIND  measured_sites=5   FOIL-ONLY M / S / s3 / ch / s4    <-- guard fires correctly

B1 — marker NOT in the NEG list: "ANTI-PATTERN (never write this; it is false): <pin>"
  PASS S-BIND  kind=NEW  measured_sites=5   CHECK: 1/1 rows PASS
B2 — in-list marker "wrongly said", pushed >160 normalized chars back
  PASS S-BIND  kind=NEW  measured_sites=5   CHECK: 1/1 rows PASS
B3 — pin appears ONLY as a markdown heading + a TOC link
  PASS S-BIND  kind=NEW  measured_sites=5   CHECK: 1/1 rows PASS
B4 — pin appears ONLY inside a fenced code block
  PASS S-BIND  kind=NEW  measured_sites=5   CHECK: 1/1 rows PASS
B5 — pin appears ONLY as a hypothetical the doc REJECTS:
     "A future cycle might consider, and this loop deliberately does NOT adopt, the following: <pin>"
  PASS S-BIND  kind=NEW  measured_sites=5   CHECK: 1/1 rows PASS
B6 — pin inside an HTML comment (invisible in the rendered document)
  PASS S-BIND  kind=NEW  measured_sites=5   CHECK: 1/1 rows PASS
```
**6 of 6 foils pass. The polarity guard catches its own literal marker list and nothing else.**

**Absence-sweep evasion matrix** (run through `checklib.norm` directly, target = `Naming is the fence`):

```
variant                        caught-by-absence-sweep?
  verbatim                     YES
  split across a LINE BREAK    YES          <-- norm() closes this. credit.
  bold markup inserted         YES          <-- credit
  backticks inserted           YES          <-- credit
  NBSP inserted                YES          <-- credit
  UNDERSCORE emphasis          NO  <-- EVADES   (_Naming_ is the fence)
  ZERO-WIDTH SPACE inserted    NO  <-- EVADES
  one letter re-cased          NO  <-- EVADES   (naming is the fence)
  HTML comment inside          NO  <-- EVADES   (Naming is <!--x--> the fence)
```

**The named "criteria file copied into the corpus" attack**, isolated:
```
$ cut -f1-4 $O/criteria.tsv > $S/CP/examples/authoring-a-skill/appendix-z.md
$ $O/check.sh $S/CP | tail -1
CHECK: 9/68 rows PASS  (59 FAIL)
```
One pasted copy is not enough (the obligation is per-file across all measured sites); pasted into *all 18*
corpus files it is a complete green build, as §2.5 step 1 shows.

### 2.6 The can-fail self-test fails open

`baseline-replay.sh:22` gates on *"no NEW row wrongly passes AND no PRESERVE row wrongly fails"* and never
compares the counts it prints against a total. Two inputs make that vacuous. Run in a properly-nested local
clone (`git clone -q -s -n <root> $S/W2`, oracles copied to the same relative depth) so `git archive`
genuinely works:

```
$ $O2/baseline-replay.sh                      # CONTROL, unmutated
  NEW+COOC rows failing at baseline : 60      PRESERVE rows passing at baseline : 8
REPLAY: OK — every assertion discriminates                                    EXIT=0

$ # FAIL-OPEN A: plant ONE malformed ERE — S-BIND's SITE_PATTERN becomes 'sha256('
$ $O2/check.sh $A
FATAL S-BIND: bad SITE_PATTERN: missing ), unterminated subpattern at position 6
check.sh EXIT=2                               <-- check.sh itself is honest
$ $O2/baseline-replay.sh
BASELINE REPLAY @ b08f5a9  (changes/ removed from the tree, so the corpus pin is proven not assumed)
  NEW+COOC rows failing at baseline : 0   <- must be ALL of them
  PRESERVE rows passing at baseline : 0   <- must be ALL of them
  NEW+COOC rows WRONGLY passing     : none
  PRESERVE rows WRONGLY failing     : none
REPLAY: OK — every assertion discriminates
baseline-replay EXIT=0                        <-- GREEN LIGHT

$ # FAIL-OPEN B: criteria.tsv reduced to its comment lines (zero rows)
$ $O2/baseline-replay.sh
  NEW+COOC rows failing at baseline : 0    PRESERVE rows passing at baseline : 0
REPLAY: OK — every assertion discriminates                                    EXIT=0
$ $O2/check.sh $A
CHECK: 0/0 rows PASS  (0 FAIL)                                    check.sh EXIT=0
```
A third input is **safe** and I record it as such: a nonexistent base commit makes `git archive` fail, the
tree is empty, PRESERVE rows trip their count floor, `wrong_fail` is non-empty →
`REPLAY: FAIL`, correctly.

**The PRESERVE half of the replay is a tautology.** I checked every PRESERVE row for whether its pinned
string is implied by its own anchor:

```
$ python3 - <<'PY'   # for each PRESERVE row: is norm(pin) a substring of the anchor ERE?
P-GBP              anchor='clean-or-resolved'               pin='clean-or-resolved'              True
P-COV              anchor='every node and every altitude'   pin='every node and every altitude'  True
P-CMP2             anchor='generative'                      pin='generative'                     True
P-RST-HARDSTOP     anchor='HARDSTOP'                        pin='HARDSTOP'                       True
P-TOP-DEEPER       anchor='deeper.{0,40}(splits|recursive)' pin='deeper'                         True
P-SPN-SEVEN        anchor='7-section universal spine'       pin='7-section universal spine'      True
P-ECON             anchor='context economy|Context economy' pin='context economy'                True
P-RAT3             anchor='halts the (subagent|runner)'      pin='halts the'                      True
PY
```
**All 8.** A file is a site *because* it matches the anchor, and matching the anchor *entails* containing the
pin, so the pin check cannot fail on any site. `"8/8 PRESERVE rows PASS at baseline"` is guaranteed a priori
and is therefore not evidence of anything. The one real check is the count floor — and it does work:

```
$ # delete BOTH README.md files from the baseline tree
$ $O/check.sh $S/DEL | grep -E 'kind=PRESERVE|SITE-EROSION'
FAIL P-CMP2           kind=PRESERVE measured_sites=8
       SITE-EROSION 8 sites, baseline had 9  (PRESERVE non-erosion: config item (6) second half)
```
**Credit: the floor fires.** But it is *cardinality only*, so relocation defeats it:

```
$ # remove 'clean-or-resolved' from stages/stage-5-gate.md — THE GATE FILE — and add one stray
$ # mention to README.md, keeping the count
$ sed -i 's/clean-or-resolved/clean or otherwise dealt with/g' $S/REL/stages/stage-5-gate.md
$ printf '\nNote: clean-or-resolved.\n' >> $S/REL/README.md
$ $O/check.sh $S/REL P-GBP
PASS P-GBP            kind=PRESERVE measured_sites=9     CHECK: 1/1 rows PASS      EXIT=0
$ $O/ruleid-sitemap.sh $S/REL | grep SITEMAP
SITEMAP: OK — every expected site present, no unexpected site
```
GBP's operative phrase is gone from the gate stage and both oracles are green.

### 2.7 Anchor erosion — NEW rows have no floor

```
$ grep -n 'erosion' $O/checklib.py
82:        erosion=None
83:        if r["kind"]=="PRESERVE" and r["id"] in mins and len(sites)<mins[r["id"]]:
```
Only `PRESERVE`. Demonstrated on the widest NEW row (`S-XPM`, 9 sites):

```
$ $O/check.sh $S/ERO S-XPM                       # untouched baseline
FAIL S-XPM  kind=NEW  measured_sites=9
       MISSING-AT METHODOLOGY.md / README.md / SKILL.md / stages/charter.md / s2 / s3 / s4 / s5 / s7

$ # reword the anchor out of 8 of 9 files (finalize->conclude, presentable->ship-ready,
$ #  'exits plan mode'->'leaves planning'); state the rule in SKILL.md ONLY
$ $O/check.sh $S/ERO S-XPM
PASS S-XPM            kind=NEW      measured_sites=1
CHECK: 1/1 rows PASS  (0 FAIL)                                                EXIT=0
```
Obligation silently shrank 9 → 1 and the row went green. The `VACUOUS-SITE GUARD` only fires at exactly
zero (`checklib.py:89`).

### 2.8 The lock

Read: `lockrace.sh:14-18`. `acquire()`'s fast path (`ln -s "$$" "$LOCK"`) is genuinely atomic. Its
**stale-break path is `rm -f` followed by a separate `ln -s`** — not atomic, and not exercised under
contention by any of the four cases (CASE 1 = contention on a *fresh* lock; CASE 2 = stale break with *one*
contender). I copied `acquire()` **verbatim** into a standalone script and raced 4 contenders against a
single stale lock, 400 trials:

```
$ cat $S/lockattack.sh      # acquire() copied VERBATIM from lockrace.sh:14-17
acquire(){ ln -s "$$" "$LOCK" 2>/dev/null && return 0
           local p; p=$(readlink "$LOCK" 2>/dev/null) || return 1
           if [ -n "${p:-}" ] && ! kill -0 "$p" 2>/dev/null; then rm -f "$LOCK"; ln -s "$$" "$LOCK" 2>/dev/null && { return 0; }; fi
           return 1; }
$ for i in $(seq 1 400); do ... ln -s $DEAD_PID lock; 4x acquire in parallel; count WON ...
TRIALS=400  trials with MORE THAN ONE winner against a single stale lock: 150
```

**150/400 (37.5%) double-acquire.** Interleaving: A and B both `readlink` the dead pid; A `rm`s and links
itself; B then `rm`s **A's live lock** and links itself. Mutual exclusion is lost outright, which is strictly
worse than D/5's ownership-attribution window that the redesign was meant to close.

Two more properties of *"a lock whose target pid is not alive is stale by definition"*
(`criteria.tsv:34`, `S-CNC-LOCK-REL`'s pinned sentence):

```
$ id -u ; kill -0 1 ; echo exit=$?
1000
/bin/bash: line 2: kill: (1) - Operation not permitted
exit=1
$ if ! kill -0 1 2>/dev/null; then echo "DEAD -> would BREAK the lock of a LIVE root-owned holder"; fi
DEAD -> would BREAK the lock of a LIVE root-owned holder
```
`kill -0` returns EPERM (exit 1) for a live process owned by another user, so `acquire()` classifies it
**dead** and breaks a live holder's lock. Symmetrically:

```
$ sleep 60 & UNREL=$! ; ln -s $UNREL $S/LK2/catalog.lock ; $S/lockattack.sh $S/LK2
LOST
```
A recycled pid that happens to be live makes the lock permanently unbreakable. `lockrace.sh:34` waits with
`until acquire; do :; done` — an unbounded busy spin, and the design deliberately removed the manual
`BROKEN-BY` escape (`lockrace.sh:9`: *"no manual BROKEN-BY dance is needed (E/4)"*). Pid namespaces make it
worse but I could not test that here — **unverified**, no container available in this sandbox.

### 2.9 The corpus pin, attacked

```
$ mkdir -p $S/PIN/changes/secret && printf 'clean-or-resolved\nHARDSTOP\n' > $S/PIN/changes/secret/inject.md
$ ln -s ../../changes/secret/inject.md $S/PIN/examples/authoring-a-skill/pulled-in.md
$ ( . $O/lib-corpus.sh; corpus_paths $S/PIN | grep -c 'pulled-in' )
1
$ python3 -c "from checklib import corpus; print(len([f for f in corpus('$S/PIN') if 'pulled-in' in f]))"
1 symlinked file(s) in the pinned corpus
$ ln -s ../../changes $S/PIN/examples/authoring-a-skill/dir-link
$ ( . $O/lib-corpus.sh; corpus_paths $S/PIN | grep -c 'dir-link' )
0                     # find does not descend a symlinked directory — that half holds
```
So the literal-list claim (`lib-corpus.sh:2`, *"`changes/` is NOT in this list and cannot enter"*) holds for
directory globbing and fails for a symlinked `.md`.

### 2.10 `ruleid-sitemap.sh`'s drift half

`ruleid-sitemap.sh:29` uses `grep -qx` for MISSING (correct, exact) but **`:31` uses `grep -qw`** for
UNEXPECTED — a word-boundary BRE match against the whole `want` line, so any expected path whose *basename*
matches swallows the drift:

```
$ grep '^SPN ' $O/expected-sites.txt
SPN METHODOLOGY.md SKILL.md stages/stage-2-draft-node.md stages/stage-3-completeness-critic.md
    templates/seed/decomposition-node.md templates/seed/generic-node.md templates/seed/README.md

$ printf '\nStray rule mention: SPN applies here too.\n' >> $S/DR/README.md      # top-level README.md
$ $O/ruleid-sitemap.sh $S/DR | grep -E 'UNEXPECTED|SITEMAP'
SITEMAP: OK — every expected site present, no unexpected site                    EXIT=0

$ # CONTROL: same stray mention in a path that is not a suffix of any expected path
$ printf '\nStray rule mention: SPN applies here too.\n' >> $S/DR2/templates/seed/leaf-task-spec.md
$ $O/ruleid-sitemap.sh $S/DR2 | grep -E 'UNEXPECTED|SITEMAP'
UNEXPECTED SPN templates/seed/leaf-task-spec.md
SITEMAP: FAIL — site set eroded or drifted
```
`README.md` exists three times in the corpus (`README.md`, `templates/seed/README.md`,
`examples/authoring-a-skill/README.md`), so drift into any of them is invisible for every ID whose want line
names any README. The `.` in the pattern is also an unescaped BRE wildcard.

Separately: `expected-sites.txt` names **no** site in `README.md` or in `examples/authoring-a-skill/**`, so
3 of the 18 corpus files are outside R1 entirely — observed, and honest (it is a measurement), but worth
stating because R1 is cited as the site-set guard.

### 2.11 `idcollide.sh`'s default ID set ≠ the live ID set

`idcollide.sh:17` documents *"ids default to METHODOLOGY's cross-file index rows"*.

```
$ . $O/lib-corpus.sh ; echo "$LIVE_IDS" | wc -w                      -> 21
$ grep -oE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md | sed ... | wc -l   -> 18
$ comm -13 def.txt live.txt
SEV TPL1 TPL2         <- in LIVE_IDS, NEVER collision-checked by the documented default
```
Two of the three (`TPL1`, `TPL2`) are precisely the pairs `FAMILY` exempts at `idcollide.sh:28`, i.e. the
exemption list covers pairs the default invocation never reaches.

### 2.12 `freeze-verify.sh` (appeared mid-review), executed and attacked

Run on a full scratch copy of `hardening-cycle-2/` so nothing was written into the artifact tree:

```
$ $O'/freeze-verify.sh freeze
FROZEN 9 files -> oracles/FROZEN.sha256                                          EXIT=0
$ $O'/freeze-verify.sh verify
FREEZE-VERIFY: OK — all 9 frozen files match the gate-4 manifest                 EXIT=0
$ printf '\n' >> $O'/criteria.tsv ; $O'/freeze-verify.sh verify
.../oracles/criteria.tsv: FAILED
FREEZE-VERIFY: FAIL — a criterion changed after the gate-4 freeze (criteria drift) EXIT=1
$ # restored
FREEZE-VERIFY: OK — all 9 frozen files match the gate-4 manifest                 EXIT=0
$ rm -f $O'/FROZEN.sha256 ; $O'/freeze-verify.sh verify
FREEZE-VERIFY: FATAL no manifest at ... — gate 4 never froze the criteria         EXIT=2
$ ls $A/changes/hardening-cycle-2/oracles/FROZEN.sha256
ls: cannot access ...: No such file or directory      # A8's "dry-run manifest was DELETED" is TRUE
```
**All three A8 claims reproduce.** Then the attack — swap the *checker* instead of the *data*:

```
$ cp $O'/criteria.tsv $O'/criteria-relaxed.tsv    # reduce it to ONE row (P-GBP)
$ sed -i 's/criteria.tsv/criteria-relaxed.tsv/' $O'/check.sh
$ $O'/freeze-verify.sh verify
FREEZE-VERIFY: OK — all 9 frozen files match the gate-4 manifest    verify EXIT=0
$ $O'/check.sh $A | tail -2
PASS P-GBP            kind=PRESERVE measured_sites=8
CHECK: 1/1 rows PASS  (0 FAIL)
$ # what is / is not frozen:
FROZEN:     1-spec.md 1.5-criteria.md 2-plan.md criteria.tsv preserve-counts.txt
            expected-sites.txt sweep-answers.tsv checklib.py lib-corpus.sh
NOT FROZEN: check.sh baseline-replay.sh ruleid-sitemap.sh idcollide.sh lockrace.sh
            gen-criteria-table.sh gen-expected-sites.sh gen-preserve-counts.sh
            gen-sweep-rows.sh gen-sweep-table.sh ere-probe.py freeze-verify.sh
```

### 2.13 Missing instruments, verified absent

```
$ grep -rniE 'offset|precede' $O/
checklib.py:7:  * POLARITY GUARD — a pinned string preceded (within 160 normalized chars) by ...
$ grep -rn '1024\|954\|997' $O/*.sh $O/*.py
(no output)
```
`1.5-criteria.md:197-201` says SC3 *"is verified by a **line-offset comparison** (automated) plus the X2
arm, and the offset check is the mutation-testable half."* **There is no such instrument in `oracles/`.**
Likewise the 954/997 description-budget measurement in `5-instrument-evidence.md:239-240` has no script.

### 2.14 Odds and ends verified

```
$ grep -rniE 'self.approv' SKILL.md METHODOLOGY.md README.md stages templates examples
(no output)          # 'self-approved' is absent from the baseline corpus, consistent with
                     # S-HG2-NOSELF measuring 0 sites there
$ cat $O/expected-sites.phantoms.txt ; grep -rn 'phantoms.txt' $O/ *.md
PHANTOM-EXCLUDED TOP METHODOLOGY.md:79 [ON TOP OF]
PHANTOM-EXCLUDED TOP examples/authoring-a-skill/planning.md:25 [ON TOP OF]
5-instrument-evidence.md:17:-rw-rw-r-- ... expected-sites.phantoms.txt      # only a directory listing
$ ls $O/__pycache__
checklib.cpython-314.pyc
$ grep -n 'R7\|ORCHESTRATOR PROPOSAL' 1-spec.md 1.5-criteria.md 2-plan.md | head -4
1-spec.md:64:  ORCHESTRATOR PROPOSAL, not an owner requirement.
1.5-criteria.md:15: ⚠ R7 LABEL, carried on every page. …ORCHESTRATOR PROPOSAL, not an owner requirement.
2-plan.md:15: …That framing is an ORCHESTRATOR PROPOSAL, not an owner requirement.
```
**R7 is labelled correctly in all three documents.** I checked all three and found no place that treats the
(a)/(b)/(c) checklist as owner-mandated. No finding.

---

## 3. Findings, ranked

### G/1 — BLOCKER. The positive per-site assertion is satisfied by text that is not an assertion; the polarity guard is bypassed 6 ways out of 6.

**Claim.** `check.sh` cannot distinguish *"the artifact states the rule"* from *"the string occurs somewhere
in the file."* A fenced code block, a heading, a TOC link, an HTML comment, an explicitly-rejected
hypothetical, and an "ANTI-PATTERN — never write this, it is false" label all satisfy a row.

**Evidence.** §2.5's bypass matrix, B1–B6, each `PASS S-BIND kind=NEW measured_sites=5 / CHECK: 1/1 rows
PASS`, with the CONTROL (`FOIL-ONLY` × 5) proving the run was set up correctly. Guard source:
`checklib.py:19` (the 15-alternative `NEG` list) and `checklib.py:77`
(`if NEG.search(t[max(0,i-160):i])`).

**Why it matters.** `1.5-criteria.md:230` states the checker's contract as *"whether it is present,
**unnegated**, and at every measured site."* **"Unnegated" is false**, and B5 falsifies it with the exact
sentence shape the guard exists for (*"this loop deliberately does NOT adopt the following: …"*). E/5's
closure row (`1.5-criteria.md:33`) reads *"the polarity guard exists and **rejected** a planted foil"* — true
of *that* foil, and its can-fail proof (`1.5-criteria.md:222`) is a single positive test with no near-miss,
so the mutation test never established the guard's boundary. That is the charter's named failure mode: a
test that does not discriminate proves nothing.

`1-spec.md:87` names the generalized fix as *"an oracle checks only that a token is mentioned"* →
*"**positive per-site assertion of the operative sentence**."* What shipped is a longer token, mentioned.
Under `2-plan.md:356`'s own definition this is **class β** (*"the apparatus cannot detect a bad build, and
the document says it can"*), which `2-plan.md:358` classifies as **a genuine second bounce on a released cap
→ stop-for-human, relayed verbatim, not re-argued.**

**Cheapest honest fixes** (author's call): require the pin to occur outside code fences / HTML comments /
ATX headings / link text; require it in a sentence-position line; replace the marker blacklist with a
whitelist requirement (the pin must appear in a line that is not preceded on the same line by any of
`e.g.`, `not`, `never`, `wrongly`, `anti-`, `example`, `might`, `would`); or accept the limit explicitly and
delete the word "unnegated" from the contract.

---

### G/2 — BLOCKER. The absence sweeps are defeated by a one-letter case flip, and combined with G/1 the whole family goes 68/68 green on a build that carries no rule and retains every forbidden claim.

**Claim.** Every ABSENT string can be preserved in meaning while evading the sweep by flipping the case of
one letter, by `_italic_` markers, by a zero-width space, or by an inline HTML comment.

**Evidence.** §2.5 step 2 — 10 re-casings, then `CHECK: 68/68 rows PASS (0 FAIL) EXIT=0`; §2.5's
evasion matrix; and the surviving text: `$S/ATK/SKILL.md:3` still reads *"a **Human** gate on the top-level
split ONLY"* while `S-HG2-ONLY`, whose ABSENT column is exactly `human gate on the top-level split ONLY`,
passes.

**Why it matters.** Case sensitivity is deliberate and its rationale is stated (`1.5-criteria.md:60-62`:
sweep `PROVEN` without hitting `provenance`). The rationale is sound; the implementation is the wrong tool
for it. The project already has the right tool — `S-PRV`'s own SITE_PATTERN uses `\bproven\b`
(`criteria.tsv:26`), which is precisely how you sweep `PROVEN` case-insensitively without hitting
`provenance`. So the guard can be made case-insensitive at zero cost to its stated purpose.

Worse, the current design **actively incentivises the evasion**: the sweep is corpus-wide, so a build that
honestly quotes the old wording in a superseded-note (*"cycle 1 said 'proven, not asserted'; this cycle does
not"*) FAILS, and the cheapest way to make it pass is to re-case the quotation — which is the evasion.

**Ranked with G/1** because the composite is what matters: 62/68 pass from G/1 alone, and G/2 closes the
last 6. Neither alone ships a fully green bad build; together they do, in about twenty minutes of work.

---

### G/3 — BLOCKER. `baseline-replay.sh` — the family's only can-fail self-test — reports `REPLAY: OK` and exits 0 over an empty criteria file, and over any single malformed ERE.

**Claim.** The replay's verdict is *"no wrong passes and no wrong fails"*, which zero rows satisfies. One bad
regex anywhere in `criteria.tsv` makes `checklib` abort before printing any row (`checklib.py:71`
`return 2`), producing zero PASS/FAIL lines — and `baseline-replay.sh:12` swallows the exit code with
`|| true` and never inspects it.

**Evidence.** §2.6. Both mutations print `NEW+COOC rows failing at baseline : 0 <- must be ALL of them` and
then `REPLAY: OK — every assertion discriminates`, `EXIT=0`. `check.sh` alone is honest (`EXIT=2`), so the
information exists and is thrown away.

**Why it matters.** `1.5-criteria.md:219` and `2-plan.md:331` both call this *"the can-fail self-test for the
whole criteria family."* It is the single instrument standing between the family and "we deleted the
criteria." Its own can-fail was never tested — the charter's exact "passes on both" error, at the top of the
dependency chain. Note that `freeze-verify.sh` would catch a *persisted* edit to `criteria.tsv` only if the
manifest predates it; it does not catch the malformed-ERE case at build time, and it does not exist at all
until gate 4.

**Fix is three lines:** capture `check.sh`'s exit status; require `newf` to equal the NEW+COOC row count and
`prep` the PRESERVE count, both computed from `criteria.tsv`; fail on a total of 0.

---

### G/4 — MAJOR. The lock design that `S-CNC-LOCK-REL` pins into the artifact loses mutual exclusion under contention, breaks live holders, and deadlocks on pid reuse. `lockrace.sh`'s case matrix has no case that would see it.

**Claim.** Three defects in the design as tested and as pinned:
1. The stale-break path is `rm -f` then a separate `ln -s` — **not atomic**. 4 contenders vs 1 stale lock:
   **150 of 400 trials produced more than one winner.**
2. *"a lock whose target pid is not alive is stale by definition"* rests on `kill -0`, which returns EPERM
   for a **live** process owned by another user → a live holder's lock is broken.
3. A recycled-but-live pid makes the lock permanently unbreakable, with an unbounded busy spin
   (`lockrace.sh:34`) and no `BROKEN-BY` escape (removed by design, `lockrace.sh:9`).

**Evidence.** §2.8, all three executed. `acquire()` copied verbatim from `lockrace.sh:14-17`. Pinned text:
`criteria.tsv:34` (`S-CNC-LOCK-REL`, *"…is stale by definition and any run may remove it"*) and
`criteria.tsv:33` (`S-CNC-LOCK`, *"…the lock and its owner appear in one indivisible step"*).

**Why it matters.** The redesign's stated purpose (`lockrace.sh:6-10`) was to close D/5's
mkdir-then-write-pid window. The fast path does close it. The stale-break path reintroduces a **strictly
worse** window: not "who owns it is briefly ambiguous" but "two runs both hold it." `2-plan.md:347` says
*"`S-CNC-LOCK` is gating and executed — the lock is real code, and `lockrace.sh` proves the H4 control fails
without it."* The control does fail without the guard (verified, §2.1). What is not established is that the
guard is correct, and `lockrace.sh`'s four cases cannot see it: CASE 1 races a *fresh* lock, CASE 2 breaks a
stale lock with *one* contender. **Add CASE 5: N contenders, one stale lock, assert exactly one winner.**

The consequence for the artifact is the reason this is Major rather than Minor: `S-CNC-LOCK-REL` will write
*"any run may remove it"* into `METHODOLOGY.md`/`SKILL.md`/`stages/` as the prescribed protocol, and the
check will pass because the prose matches the string. A racy protocol shipped as doctrine. The standard fix
is `ln -s "$$" "$LOCK.$$" && mv -T`-style atomic replace conditioned on the observed target, or
`mkdir`-based two-phase with the pid inside plus an owner-verified `rm`.

---

### G/5 — MAJOR. NEW rows have no site-count floor, so a builder can shrink an obligation from 9 sites to 1 by rewording the anchor, and the row goes green.

**Claim + evidence.** §2.7. `S-XPM` 9 sites → `PASS … measured_sites=1`, exit 0, after rewording
`finalize`/`presentable`/`exits plan mode` in 8 of 9 files. Floor logic is `PRESERVE`-only:
`checklib.py:83`. `VACUOUS` fires only at exactly zero: `checklib.py:89`.

**Why it matters.** `1.5-criteria.md:73-77` defines the SWEEP row as *"wide anchor = every file stating the
rule in any form"* — the width **is** the obligation, and it is measured on the tree **under test**, i.e. the
one the builder controls. Anchor erosion is the natural failure mode of a build that touches 18 files of
prose, and it is invisible. `ruleid-sitemap.sh` does not cover it (it tracks the 21 baseline rule *IDs*, not
criteria anchors). Fix: generate a `new-counts.txt` alongside `preserve-counts.txt` and apply the same
`len(sites) < min` floor to NEW/COOC rows. The generator already exists.

---

### G/6 — MAJOR. All 8 PRESERVE rows are tautological, so "8/8 PRESERVE pass at baseline" is evidence of nothing; and the one real check is a cardinality count, which relocation defeats.

**Claim + evidence.** §2.6. For all 8 rows, `norm(pin)` is a substring of the anchor ERE, so a site cannot
fail its pin check by construction. And the relocation attack: `clean-or-resolved` removed from
`stages/stage-5-gate.md`, one stray mention added to `README.md` → `PASS P-GBP measured_sites=9`, plus
`SITEMAP: OK`.

**Why it matters.** This is E/13's closure. `1.5-criteria.md:39` claims *"8 `PRESERVE` rows with generated
baseline counts; erosion **failed**"* and cites `baseline-replay.sh ⇒ 8/8 PRESERVE pass at baseline` as the
evidence. That number is a priori 8/8 for any tree in which the anchors match at all — it cannot
discriminate. The genuine check (the floor) does fire, and I credit it in §5; but it is set-cardinality, not
set-identity, so **losing a preserved rule from the file that most needs it is invisible as long as the word
resurfaces anywhere.** Fix: store the baseline *file set* in `preserve-counts.txt`, not the count, and
compare sets; and give PRESERVE rows a pin that is not implied by the anchor (an anchor on the surrounding
sentence, a pin on the operative clause) so the per-site half is not vacuous.

---

### G/7 — MAJOR. `freeze-verify.sh` freezes the data and leaves the checkers writable, so the goalposts move by editing `check.sh`.

**Claim + evidence.** §2.12. `check.sh` re-pointed at a 1-row criteria file → `FREEZE-VERIFY: OK — all 9
frozen files match the gate-4 manifest`, exit 0, while `check.sh` reports `CHECK: 1/1 rows PASS`.
`freeze-verify.sh:15-25` lists 9 files; the 12 not listed include `check.sh`, `baseline-replay.sh`,
`ruleid-sitemap.sh`, `idcollide.sh`, `lockrace.sh`, every `gen-*.sh`, and **`freeze-verify.sh` itself**.

**Why it matters.** The script's own stated rationale (`freeze-verify.sh:9-12`, repeated at
`5-instrument-evidence.md:313-317`) is *"moving a criterion's goalposts by editing the data file it reads is
the obvious evasion, and a hash over the prose alone would not see it."* Correct — and the code path is the
equally obvious evasion, left open. Given G/3 (the replay green-lights an empty family), the composite is
that a build can be certified against a family that no longer exists. Fix: freeze every file in `oracles/`
except the generated outputs, or hash the whole directory tree.

*Also recorded, minor within this finding:* the manifest stores absolute paths, which `A8` already declares
as a known cosmetic property. Verified — the manifest I generated in scratch is not portable. No new finding.

---

### G/8 — MINOR. `ruleid-sitemap.sh`'s drift check uses `grep -qw` against the whole want line, so drift into any of the three `README.md` files is invisible.

**Claim + evidence.** §2.10. `SPN` added to top-level `README.md` → `SITEMAP: OK`, exit 0; the same mention
in `templates/seed/leaf-task-spec.md` → `UNEXPECTED SPN`, exit 1. Source: `ruleid-sitemap.sh:31`
(`grep -qw -- "$g" <<<"$want"`) vs `:29` (`grep -qx`, correct). The `.` is also an unescaped BRE wildcard.

**Why it matters.** Drift is one of the two things R1 exists to catch (`1.5-criteria.md:169-176`), and the
false negative lands exactly on the ambiguous basenames the corpus actually has three of. One-character fix:
`grep -qxF` over `tr ' ' '\n' <<<"$want"`.

---

### G/9 — MINOR. The corpus pin admits `changes/` through a symlinked `.md` under `examples/`.

**Claim + evidence.** §2.9. `examples/authoring-a-skill/pulled-in.md → ../../changes/secret/inject.md` is
returned by both `corpus_paths()` and `checklib.corpus()`. Directory symlinks are correctly excluded
(`find` does not descend them) — I verified that half holds.

**Why it matters.** `lib-corpus.sh:2` states *"`changes/` is NOT in this list and **cannot** enter."*
"Cannot" is too strong. Impact is bounded — it requires a deliberate symlink — but the pin is cited as the
reason `baseline-replay.sh` is trustworthy. Fix: `find … -type f` and skip symlinks, or `realpath`-check
each corpus member against the tree root.

---

### G/10 — MINOR. `idcollide.sh`'s documented default ID set (18) is not the live ID set (21): `SEV`, `TPL1`, `TPL2` are never checked.

**Claim + evidence.** §2.11. `LIVE_IDS` (`lib-corpus.sh:10`) has 21; `idcollide.sh:25`'s METHODOLOGY-index
harvest yields 18; `comm -13` → `SEV TPL1 TPL2`. Two of the three are the pairs `FAMILY`
(`idcollide.sh:28`) exempts.

**Why it matters.** R3 is gating (`1.5-criteria.md:181`). Two sources of truth for the ID set, neither
reconciled by any instrument, and the default invocation silently covers a subset. Fix: default to
`LIVE_IDS` from `lib-corpus.sh` (already sourced by every other oracle), or add an assertion that the two
sets agree.

---

### G/11 — MINOR. Two criteria are described as automated with instruments that do not exist.

**Claim + evidence.** §2.13. `1.5-criteria.md:197-201` — SC3 *"is verified by a **line-offset comparison**
(automated) … and the offset check is the mutation-testable half"*; `grep -rniE 'offset'` over `oracles/`
returns only `checklib.py`'s polarity comment. `5-instrument-evidence.md:239-240` reports `current: 954 /
candidate: 997 cap 1024` with no script in `oracles/` producing it (`grep -rn '1024\|954\|997'` over the
`.sh`/`.py` files → no output).

**Why it matters.** Same shape as the defect that tripped pass 2's cap, one order of magnitude smaller:
present-tense automation with no artifact. SC3's is the more substantive of the two, because SC3 is the one
criterion `1.5-criteria.md:199` admits has no pinned string, so the offset check is its *only* automated
half. The 954/997 measurement I take as genuinely performed (it is specific and its `quick_validate.py`
output is quoted) but **unverified** by me and not reproducible from `oracles/`.

---

### G/12 — MINOR. `5-instrument-evidence.md`'s first half carries superseded counts in the same present-tense register the file's own opening rule forbids.

**Claim + evidence.** `:77` *"**42 of 42 NEW rows fail at baseline; 8 of 8 PRESERVE rows pass**"* and `:120`
*"**68 rows are required**"* vs the appendix's measured `:206` `60` and `:274` `86`. The `ls` listing at
`:9-28` shows 17 files; `oracles/` now holds 24, and 4 of the scripts the document describes
(`gen-criteria-table.sh`, `gen-sweep-table.sh`, `ere-probe.py`, `freeze-verify.sh`) are absent from it.

**Why it matters.** The file's own opening rule (`:3-4`) is *"Nothing here describes a script that does not
exist: that inversion is what tripped the cap on pass 2."* The inversion is not present — nothing here
describes a *nonexistent* script — but a first-time reader gets 42/68 as the live numbers and must reach
Appendix A to learn they are 60/86. Fix: mark the superseded numbers in place (`~~42~~ → 60`) rather than
only correcting them 130 lines later. Nitpick-adjacent; I rank it Minor only because these are exactly the
numbers a gate reads.

---

### G/13 — NITPICK. Orphan artifacts in `oracles/`.

`expected-sites.phantoms.txt` is read by no script and referenced only inside a pasted directory listing
(§2.14) — it is superseded by the in-script phantom ledger and is not covered by SC6, so it can rot
silently. `criteria.v2-superseded.tsv` and `__pycache__/checklib.cpython-314.pyc` are also shipped. Delete
the pyc, add `__pycache__` to ignore, and either wire `phantoms.txt` into SC6 or delete it.

---

### G/14 — MINOR (process). The artifacts changed while this review was running, so what I reviewed is not what exists.

**Evidence.** §1(iv): `1.5-criteria.md` `cd9a217e…` → `1f898513…`; `5-instrument-evidence.md` `4a3a81e7…` →
`a3199def…`; `oracles/freeze-verify.sh` created at `13:08:08`, after my initial `ls` of `oracles/`;
`criteria.tsv` rewritten at `13:08:16` with identical content.

**Why it matters.** This is the exact condition `freeze-verify.sh` was just written to prevent, occurring
during the review that is supposed to bless the frozen set. I adapted (I executed and attacked the new
script, §2.12, and my findings against the changed sections are re-verified against the current files), but
a reviewer who had not re-hashed would have shipped a record about a file that no longer exists. Recommend:
freeze before dispatching stage-3 reviewers, not at gate 4 — or at minimum record a
`REVIEWED-AT.sha256` when reviewers are dispatched.

---

## 4. COVERAGE CHALLENGE (CH8)

Behaviours this change could plausibly alter that **no criterion observes**. Not "none found."

**CH8-a — RANK 1. Nothing observes the corpus *file set*.** `corpus()` (`checklib.py:20-30`) is a live walk;
`lib-corpus.sh:5-9` likewise. Adding, splitting, merging, renaming or deleting a corpus file changes every
site set silently. **Scenario:** the build splits `METHODOLOGY.md` (the file carrying 60 of 68 rows' DEF
sites) into `METHODOLOGY.md` + `METHODOLOGY-rules.md`. Every NEW row's site set changes; the vacuous guard
sees nothing (counts stay ≥1); PRESERVE floors can only go *up*; `expected-sites.txt` names no site in the
new file so `ruleid-sitemap.sh` reports `UNEXPECTED` for the IDs that moved — but that fires *late*, at ID
granularity, and (per G/8) not at all for basename-ambiguous paths. **Impact: high.** A criterion is cheap:
freeze the sorted corpus file list at baseline and fail on any delta not declared in `2-plan.md` §2.

**CH8-b — RANK 2. Nothing observes whether a pinned rule is reachable at *runtime*.** The artifact is a
skill: `SKILL.md` is loaded eagerly, `stages/*.md` on demand, `examples/**` possibly never. `check.sh`
treats all 18 files as one flat corpus. **Scenario:** `S-IDGREP-NAME` is pinned at `M` only, 1 site
(`1.5-criteria.md:158`); if `METHODOLOGY.md` is not loaded by the runner in a given path, the rule is
enforced in the repository and absent from the running agent. No criterion distinguishes load-bearing sites
from documentation sites. **Impact: high** — it is the difference between "the rule exists" and "the rule
operates," which is the whole point of the cycle.

**CH8-c — RANK 3. Nothing observes the *rendered* text.** All checks are over markdown source. §2.5-B6 and
the evasion matrix show HTML comments and `_`-emphasis are invisible-to-reader / invisible-to-checker in
opposite directions. **Scenario:** the build satisfies a row inside `<!-- … -->`; a model loading the file
may or may not attend to it, and a human reader sees nothing. **Impact: medium-high**, and it is the
mechanism behind G/1 rather than a separate defect — I list it because a criterion could observe it cheaply
(strip comments and fences before matching) and none does.

**CH8-d — RANK 4. Nothing observes SC5's rubric being applied, and its judge is the builder.**
`1.5-criteria.md:203-206`: *"Judge: **this runner** at stage 8, on a recorded per-ID diff table."* Gating,
human-judged, self-judged, and with no generator for the diff table it is judged on. **Scenario:** stage 8
records `AGREE` for all 21 IDs without producing the table; nothing detects it. **Impact: medium.** A
`gen-ruleid-difftable.sh` is a 20-line script and would make the rubric auditable.

**CH8-e — RANK 5. Nothing observes the tension between the corpus-wide absence sweeps and honest historical
quotation.** The sweeps are corpus-wide with no exemption for a superseded-note. **Scenario:** the build
adds *"pass 1 said 'proven, not asserted'; this cycle does not"* → `S-PRV` fails on `ABSENCE-VIOL`; the
cheapest passing edit is to re-case the quote, which is G/2's evasion. **Impact: medium**, and it means the
criteria set has a built-in incentive toward the evasion that breaks it.

**CH8-f — RANK 6. Nothing observes the description's *reserve*.** `5-instrument-evidence.md:253` and
`2-plan.md`'s risk table both declare 27 chars of slack as a known tightness with *"no criterion enforces a
reserve."* Correctly declared, so not a finding — recorded here because it is a real uncovered behaviour: the
next cycle's first added trigger word overflows the cap.

---

## 5. LABEL AUDIT (CH9/CH10)

Every criterion is marked **gating** (`1.5-criteria.md:79`, *"Every row is gating"*; `2-plan.md:365`, *"All
criteria are gating"*). Per criterion I sampled: the governed path I confirmed is exercised, and the
evidence.

| Criterion sampled | Governed path | Exercised? | Evidence I checked | Challenge |
|---|---|---|---|---|
| **SC6** (generator reproducibility) | the 5 generators vs their committed outputs | **YES, fully** | §2.2 — all 5 re-run, all reproduce; plus both embedded tables diff-identical | none. Label earned. |
| **R1** `ruleid-sitemap.sh` | ID→file map vs `expected-sites.txt` | **YES, partially** | §2.1 clean run; §2.4 drift mutation; §2.10 the false negative | **CHALLENGED.** The drift half is unsound for basename-ambiguous paths (G/8), and the expectation covers 0 sites in `README.md` and `examples/**` — 3 of 18 corpus files are outside R1. |
| **R2** / `gen-criteria-table.sh` | NEW rows have a measured anchor | **YES** | §2.4 `VACUOUS-NEW S-SPV`, exit 1 | **CHALLENGED.** It checks `count>0`, not `count == baseline` — G/5 passes it at 1 of 9. |
| **R3** `idcollide.sh` | post-change ID set vs corpus tokens | **YES, on a subset** | §2.1 three invocations, all as claimed | **CHALLENGED.** The documented default set omits `SEV`/`TPL1`/`TPL2` (G/10). Verified against `LIVE_IDS`, which is a real authority, not a proxy. |
| **8 PRESERVE rows** | the preserved rule still stated at its sites | **PROXY ONLY** | §2.6 tautology proof; §2.6 floor fires on deletion; §2.6 relocation passes | **CHALLENGED HARD.** The per-site half is vacuous by construction; the proxy actually exercised is set *cardinality*. G/6. |
| **`S-CNC-LOCK` / `-LOCK-REL`** (label: gating + **L**, "live executed race") | the lock protocol | **PROXY, AND THE PROXY DISAGREES** | §2.1 `LOCKRACE: ALL 4 CASES PASS`; §2.8 150/400 double-acquire | **CHALLENGED HARD.** The `L` arm tests a bash reimplementation of a protocol the artifact only *describes*; and my extension of that same reimplementation falsifies the pinned sentence. A proxy that contradicts the claim it certifies. G/4. |
| **`S-BIND` / `S-IDN` / `S-RES` / `S-CTX` family** (label: **P-PROXY**, *"always paired with an execution arm"*, `1.5-criteria.md:52-56`) | dispatcher-recorded `plan_sha256`; three distinct spawn ids; resolution semantics; `redteam_context` | **NO — text only** | `5-instrument-evidence.md:299` *"the **16 fixture arms have not been run**"*; `2-plan.md:334` `fixtures/X{1,2,3,4}` → `PENDING BUILD` | **CHALLENGED, but the disposition is honest.** At this moment **0 of 16** execution arms exist, so every P-PROXY criterion is proxy-only, and the pairing the label promises is entirely future. `2-plan.md`'s risk table states the correct consequence (*"If an arm cannot run, its criterion is `verified = no` and this runner **HALTs**"*). I am not calling this a finding; I am recording that the "gating" label on this family currently rests on a text check alone. |
| **SC1 / SC2** | description length, triggers, `quick_validate.py` | **YES, on a scratch copy** | `5-instrument-evidence.md:239-248`; labelled as a copy at `1.5-criteria.md:190-193` | **CHALLENGED (light).** No instrument in `oracles/` reproduces it (G/11); I could not re-run it. **Unverified**, not disputed. |
| **SC3** | rule block precedes the stage table | **NO automated half exists** | §2.13 `grep` for `offset` → nothing | **CHALLENGED.** Gating, and its only automated arm is unbuilt. G/11. |
| **SC4** | `diff -rq` live vs source | **NO** | `5-instrument-evidence.md:300` *"SC4's live-copy re-sync has not happened"* | not challenged — declared PENDING BUILD, and it is a one-line command. |
| **SC5** | cross-file rule consistency | **NO instrument; judge is the builder** | `1.5-criteria.md:203-206` | **CHALLENGED.** See CH8-d. |
| **`S-HG2-NOSELF`** (kind `COOC`) | the phrase never appears unqualified | **YES, and honestly bounded** | §2.14 `self-approved` absent at baseline → 0 sites → fails under the vacuous guard, as `1.5-criteria.md:35` claims; `1.5-criteria.md:272-274` states the limit plainly | none. The label and its stated limit agree with the code (`checklib.py:89` covers `COOC`). |

**Label-audit verdict:** the *gating* label is defensible for `SC6`, `R2`'s zero-anchor half, `S-HG2-NOSELF`,
and (with G/8's caveat) `R1`. It is currently proxy-only for the entire `P-PROXY` family and for all 8
PRESERVE rows, and it is **unearned** for `SC3`'s automated half and for `S-CNC-LOCK-REL`, whose proxy
disproves it.

---

## 6. WHAT THE PASS GENUINELY EARNED

Specifically, with the evidence, because the author should not rebuild any of this.

1. **Every instrument exists and runs.** 14 scripts, all executed by me, all producing the documented
   output. Pass 2's central defect — present-tense claims about absent scripts — is **closed on the
   existence axis** (§2.1). I could not find a single script described in the documents that is missing,
   with the two exceptions in G/11 which are described *inside* criteria prose rather than as `oracles/`
   scripts.

2. **SC6 is real and it is the strongest thing in the pass.** All five generators reproduce their committed
   outputs, and — the claim that actually matters — **both embedded tables are the generators' verbatim
   output**: 68/68 criteria rows in `1.5-criteria.md` §1 and 86/86 sweep rows in `2-plan.md` §1 diff
   identical (§2.2). "Generated, not typed" is TRUE for both tables. F/1's "a site list retyped is a site
   list unmeasured" is genuinely fixed.

3. **The B7 reconciliation is exact.** 5 of 5 anchor measurements I re-ran match both `ere-probe.py` and
   B7's own committed counts and file lists — PRV 8/4, HG2-ONLY 7/4, SPN 7/6, `required_sections` 15/7,
   `index.md` 11/5 (§2.3). The `re.I`-on-`PROVEN`/`provenance` catch recorded at
   `5-instrument-evidence.md:195-197` is a real find and the word-bounded fix measures exactly B7's P6.

4. **The sweep join is genuinely enforced, not asserted.** 86 generated rows, 86 authored answers, both
   mutation directions exit 1 (§2.4). D/2 is closed. The generated verdict tally (and the owning of the
   typed 55/20/4/4 → measured 64/15/4/3 error at `gen-sweep-table.sh:38-39`) is the right instinct applied
   to the pass's own prose.

5. **The phantom ledger is real.** `ruleid-sitemap.sh:15,21,34-37` — 2 exclusions printed on every run,
   matching `gen-expected-sites.sh`'s 2 (§2.1, §2.2), and the empty case self-reports at `:37`. Pass 3's
   self-caught `2>/dev/null` defect (A1) is genuinely fixed, and finding it by an independent re-run instead
   of trusting the header comment is exactly the discipline that should have been applied to the polarity
   guard.

6. **`norm()` closes four real evasions.** Line breaks, `**bold**`, backticks and NBSP all fail to hide a
   forbidden string (§2.5's matrix). The line-break case in particular is the one a builder would hit
   accidentally, and it is closed.

7. **The PRESERVE count floor does fire.** Deleting two corpus files trips `SITE-EROSION 8 sites, baseline
   had 9` on `P-CMP2` (§2.6). E/13's *"nothing checked non-erosion"* is no longer true — it is now
   *insufficiently* checked (G/6), which is a different and much better problem.

8. **`gen-criteria-table.sh` and `check.sh`'s vacuous-site guard both discriminate.** `VACUOUS-NEW S-SPV`
   exit 1, and `VACUOUS 0 measured sites` on the row (§2.4). The insight of turning `S-CTX-VAC`'s
   observation on the checker itself is a good one and it works at the boundary it claims.

9. **`freeze-verify.sh`'s data half works, and A8's three claims all reproduce**, including the honest
   deletion of the dry-run manifest — I confirmed no `FROZEN.sha256` is on disk (§2.12). The reasoning at
   `freeze-verify.sh:9-12` about hashing the data and not just the prose is correct; it just needs the code
   path too.

10. **A7 is accurate.** The artifact is unedited, HEAD is `b08f5a9`, and every NEW criterion fails at
    baseline for exactly the documented reason (`MISSING-AT` at each measured site, not `VACUOUS`, not
    `FATAL`). I checked the *reason*, per my charter, and it matches. **I do not report "the criteria all
    fail" as a finding.**

11. **R7 is handled correctly in all three documents** (§2.14). I looked for the failure the charter warned
    me about and it is not there.

12. **The honest-limits rows are honest.** `1.5-criteria.md` §6's declared non-criteria, §4's *"the one
    thing `check.sh` is not"*, the withdrawn variance claim at §5, and `2-plan.md` §6's risk table all state
    real limits plainly rather than papering them. G/1 stands *despite* §4's disclaimer because the
    disclaimer's own wording ("unnegated") is the part that is false — but the instinct to write the
    disclaimer is right, and the "6th no-ID predicate" residual is named as the top risk rather than hidden.

---

## 7. Routing

- **3 Blockers** (G/1, G/2, G/3) → stage 1 under `2-plan.md` §5's own routing.
- **G/1 + G/2 together are a class-β finding against pass 3.** `2-plan.md:357-358` states the consequence
  itself: *"A class-β finding against pass 3 is a genuine second bounce on a released cap and is a
  **stop-for-human, relayed verbatim.** It is not re-argued."* Under RAT3 this runner cannot demote it. I
  state the severity; I do not route around it.
- **4 Majors** (G/4, G/5, G/6, G/7) → stage 2.
- **5 Minors** (G/8, G/9, G/10, G/11, G/12, G/14) → fixable in place.
- **1 Nitpick** (G/13) → log.
- **Carry-forward, not blockers** (declared out of scope): none of my findings touch F1/F2/F5's mechanism,
  DIV, the cost envelope, ECON's O(children²), or the two-passes ruling. G/4 concerns the *lock protocol the
  artifact will state*, which is `S-CNC-LOCK`'s in-scope subject matter, not F5's mechanism.

**Un-run axes, declared:** the 16 fixture arms (stage-8 work, and `5-instrument-evidence.md:299` says so);
SC1/SC2's 954/997 measurement (no reproducible instrument — **unverified**, not disputed); pid-namespace
behaviour of `kill -0` (**unverified**, no container available); Layer-2 conformance items (5)–(8) as stated
text (I did not read `guarded-change.architect.md` — declared deviation, §1(ii)).
