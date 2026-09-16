# Stage 3 — cold review record, ARM E (VERBATIM) — **PASS 2**

**Verbatim record** (ART2): the reviewer's raw output, unedited, extracted mechanically from the
dispatcher's task transcript.

| Field | Value |
|---|---|
| Arm / frame | **E** — oracle + criteria validity, round 2 (ran and mutated the two shipped oracles) |
| Agent type | `general-purpose` (cold subagent) |
| Model | `claude-opus-5` |
| **`spawn_id` (DISPATCHER-RECORDED)** | **`a92c8332dc1a4f729`** |
| Self-reported identity | `spawn_id: unavailable` (declined to invent one) |
| Mutation isolation | reviewer states all mutations ran on copies under `/tmp`; `git status` for `WT/Architect` unchanged — independently confirmed by this runner |

---

I have what I need. Writing up.

## Findings

**E/1 · BLOCKER · `ruleid-sitemap.sh` is byte-for-byte the pass-1 printer. C/O1 and C/O2 are claimed closed and are entirely open; `expected-sites.txt` does not exist.**

`1.5-criteria.md:13` states in the present tense: *"It is now a **checker**: reads `expected-sites.txt`, reports MISSING / UNEXPECTED, **exits 1** on either."* `:12` states site sets *"are asserted against a **data file** (`oracles/expected-sites.txt`)"*. Measured:

- `oracles/ruleid-sitemap.sh:34` is still `exit 0`. There is no `expected-sites.txt` anywhere in the repo (`find . -name 'expected-sites*'` → empty), no `check.sh`, no `baseline-replay.sh`, no `oracles/lockrace.sh`, no `8-harness.md`.
- The directory holds exactly two files, both mtime `Jul 25 10:18`, and `git status` shows the whole `hardening-cycle-2/` tree untracked — nothing was rewritten between pass 1 and pass 2.

All four mutations `§4:150-157` promises must now fail exit **0** (full table in §2 below). Deleting every `GBP` token from `stage-5-gate.md` exits 0; deleting the operative sentence while keeping `<!-- see GBP -->` produces **byte-identical** output to baseline, exit 0. Pass 1's `3-redteam-plan.C.verbatim.md:308` verdict stands verbatim.

Failure scenario: stage 8 runs the oracle, gets exit 0, records `R1 verified = yes`, and ships a build in which `CAP` has been dropped from `stage-5-gate.md`. Fix: implement the `expected-sites.txt` diff-and-exit-1 checker the row already describes, or relabel R1 `verified = no` and HALT.

**E/2 · BLOCKER · `idcollide.sh` still pre-blesses `TOPGATE` and `DECOMPOSITION`; §2 R3 claims they were removed. R3 cannot fire on this cycle's own most likely collision.**

`1.5-criteria.md:119-120`: *"**`TOPGATE` and `DECOMPOSITION` are REMOVED from the grandfather list**."* `oracles/idcollide.sh:31` reads, unchanged:

```
GRAND="DEC DECOMPOSE|DEC DECOMPOSES|DEC DECOMPOSITION|TOP HARDSTOP|TOP TOP-LEVEL|TOP TOPGATE"
```

Demonstrated: I added `TOPGATE` as a live token and ran the oracle — `grandfathered : TOP < TOPGATE (baseline debt, not renamed this cycle)`, exit **0**. This cycle introduces `plan/topgate/` (rows 7, 8, and fixture `X2/*/plan/topgate/APPROVAL.md`), so `TOPGATE` is a token this cycle actually adds. Fix: delete the two pairs from `GRAND`.

**E/3 · BLOCKER · §5's cluster map contradicts the fixtures on disk. Four criteria have no scheduled arm, and the on-disk X3 auto-fails §5's blanket pass rule.**

`1.5-criteria.md:178-179`: *"**X1** = BIND (all 6 rows) + RES + IDN · **X2** = HG2 + XPM + SC3 · **X3** = CTX + IGM. **12 spawns total.**"* `2-plan.md:222` repeats "12 arms". But `fixtures/README.md:3` says *"**Four** clusters"* and its table maps **X1** = S-BIND only, **X3** = S-IDN + S-RES *(polarity inverted)*, **X4** = S-CTX + S-IGM. `fixtures/X4/` exists on disk.

Consequences, all concrete:
- Rows 16, 18, 38, 39 cite method `X3`; on disk their fixture is **X4**, which §5 never schedules ⇒ `S-CTX-key`, `S-CTX-vacuous`, `S-IGM-def`, `S-IGM-proc` are gating with an unscheduled arm.
- `§5:174` says *"Pass iff both holed spawns return the blocking verdict AND both intact spawns return the proceeding verdict. **Any other pattern ⇒ `verified = no`**."* The on-disk X3 requires holed ⇒ **proceed**. Run literally, the correct result is recorded as failure. `§5:183` half-acknowledges this ("X3's polarity is deliberately inverted **on the IDN item**") while `§5:178` puts IDN in X1 — §5 contradicts itself.

Fix: renumber §5's clusters to match `fixtures/README.md` (4 clusters, 16 spawns) and make the pass rule per-cluster-polarity rather than blanket.

**E/4 · BLOCKER · `oracles/lockrace.sh` does not exist, and two of the four outcomes §4 promises for it are wrong as stated — I executed them.**

`2-plan.md:184-186` names `oracles/lockrace.sh`; it is absent. `1.5-criteria.md:163-166` claims the race shows *"a **crash with the lock held** (the release path runs; a second run is not deadlocked)"* and *"**The race must fail against the unguarded version**"*. Both measured false:

- **Crash case.** `bash -c 'mkdir "$LOCK"; kill -9 $$'` → lock **still held**, second `mkdir` → `BLOCKED`. A trap-based release only runs on ordinary exit; it does not run on `SIGKILL`, and an Architect **HARDSTOP** is exactly that. So "a second run is not deadlocked" is unachievable. It also contradicts row 29 (`S-CNC-LOCK-stale`), which exists precisely because a stale lock must be manually broken by `BROKEN-BY`.
- **Unguarded control (H4).** 8 concurrent writers × 200 appends to an unguarded `index.md` → **exactly 1600 lines, zero loss**, because `>>` under `PIPE_BUF` is atomic. The control **passes without the lock**, so the test "passes with and without the guard" — the precise thing `§4:166` says proves nothing.

Fix: write `lockrace.sh`; change the crash expectation to "lock leaks ⇒ next run must invoke the row-29 BROKEN-BY path"; and make the unguarded control a genuinely non-atomic mutation (the catalog `git commit`, which is what the lock actually protects), not an append.

**E/5 · MAJOR · A normalized-substring presence test has no polarity or context guard, so every one of the 54 string rows is satisfiable by text that means the opposite — the sentence quoted as a foil.**

`§1:36-39` defines the assertion as: the pinned string *"appears — after `normalize()` (strip `**`/`*`/backticks, collapse all whitespace…)"*. `normalize()` strips emphasis but not blockquote markers, strikethrough context, or a negating lead-in. A build that writes

> **What pass 1 wrongly said:** *the gate raises the cost of shipping a hole. It does not certify its absence* — we now assert the stronger claim.

satisfies row 20's pinned string while stating the opposite rule, and simultaneously keeps the paired absence strings out. Fix: require the pinned string to be the assertion of a numbered rule block and assert it is **not** preceded within N chars by a negating marker (`Wrong:`, `NOT`, `~~`, `>`), or assert on a structural locus (heading + first sentence) rather than a free substring.

**E/6 · MAJOR · Row 24's SITES list is hand-selected and its "measured" label is false. Four of its nine sites contain no `index.md` reference at baseline.**

`1.5-criteria.md:71` claims *"**all 9 measured `index.md` files**: S, M, s1, s6, s7, s8, tp/README, ch, ex/README"*. `0-baseline.B7-measured-sites.md:69-83` (P9a, "index.md accessors — ALL") measures **11 hits in 5 files**: `METHODOLOGY.md`, `stage-1`, `stage-6`, `stage-8`, `templates/seed/README.md`. I re-measured: `grep -rn 'index\.md'` over the pinned corpus → **11 hits, 5 files**, identical. `S`, `s7`, `ch`, `ex/README` have **zero** hits. `§0:17` claims *"Every site list is the **measured** set"* (C/O7's fix). It is not. Fix: use the B7 set, or drop the "measured" label and declare the four additions as new-site editorial choices.

**E/7 · MAJOR · Row 26 requires the gate-log string at an unmeasured site (`s8`) and omits a measured one (`s7`).**

`1.5-criteria.md:73` lists *"**all measured gate-log sites**: S, M×3, s1, s3, s4, s5, s6, s8, ch"*. B7 P9b (`:85-106`, 18 hits / 9 files) contains `stages/stage-7-assemble.md:11` and **no** `stage-8` entry. So `s7` — a measured site — goes unchecked, and `s8` is required for no measured reason. Fix: swap `s8` → `s7`.

**E/8 · MAJOR · Rows 48 and 52 mis-state their own site counts, and row 52's charter line contradicts B7.**

- `:95` row 48: *"**all 7 measured "top-level ONLY" sites**"* then lists tokens resolving to **9** (`S:3, S:77, S:86, M:212, M:327, s6×3, tp/decomposition-node`). B7's P12 (`:57-67`) measures **7** and contains neither `S:77` nor `S:86`. I checked both: `SKILL.md:77` does state the top-level gate; `SKILL.md:86` mentions `plan/topgate/` but makes no "ONLY" claim.
- `:99` row 52: *"**all 10 measured terminus sites**"* then lists **14**. B7 P11+P12 (`:38-55`) measures **14 hits in 9 files**. The "10" is simply wrong.
- Row 52 cites `ch:132`; B7`:47` measures `stages/charter.md:131`. B7`:13` puts `charter.md:132` in the *clean-or-resolved* set — the two were conflated.

Fix: regenerate the count labels from B7 mechanically rather than by hand.

**E/9 · MAJOR · Row 43's SITES ≠ B7's measured set, B7 under-measured, and the row leaves its case-sensitivity to the builder — passing at 2 of 7 sites at baseline.**

Row 43 (`:90`) lists 8 sites in 7 files including `S:18`. B7 P18 (`:180-190`) measures **7 hits in 6 files** and omits `SKILL.md` entirely. I measured `grep -rn 'Outputs &'` → **8 hits in 7 files**, including `SKILL.md:18`. So B7 — the file R2 cites as authoritative — under-measured, and `0-baseline.md:111` (which *does* cite `SKILL.md:18-19`) disagrees with it.

Separately: `§1:38` says lowercase *"**only where the row says case-insensitive**"*; row 43 says nothing. Measured, the pinned string `Outputs & artifacts (with their locations)` matches at `tp/generic-node` and `tp/decomposition-node` **case-insensitively only** (both read `(WITH their locations)`). So the builder chooses: case-insensitive ⇒ those 2 sites pass **at baseline** (non-oracle there); case-sensitive ⇒ they fail and must be edited. That choice is exactly the C/O6 defect. Fix: pin the case explicitly per row.

**E/10 · MAJOR · Three of 57 rows still describe rather than pin, against §0's "Every row now pins a verbatim PINNED STRING… No row says 'or equivalent'".**

Parsed all 57 rows mechanically; rows **16** (`a redteam_context: YAML key with path:/note: entries and the words priority-ordered`), **56** (`*(computed, not a string)*` — legitimate, it is the automated row), and **57** (`ADDED by Architect's fork beyond the carried core:` **followed by the four added duties** — the four duties are unpinned) are not single verbatim strings. Row 57's paired absence carries *"(kept only if still true; asserted as a positive statement of what is added)"* — a conditional the builder resolves, i.e. `or equivalent` under another name. Also row 44's pin is a bare heading, satisfiable by an empty section. Fix: pin row 16's and 57's operative sentences verbatim; give row 44 a content assertion.

**E/11 · MAJOR · SC1's measured 1024-char description cap collides with rows 20 and 48, both of which make `SKILL.md:3` — the frontmatter `description` — a mandatory site.**

Measured: the baseline description is **954 chars**. Row 20's pinned string is **76** chars, row 48's is **180**. Both rows list `S:3`. Naive insertion → 1210 vs a 1024 cap, and row 20 alone → 1030. Satisfying both requires deleting ≥186 chars from the description while SC2 (`§3`) simultaneously requires `plan`, `design`, `decompos` and `Proactively SUGGEST` to survive, and row 20's paired absence requires `PROVEN` / `completeness is proven` removed from it. No criterion budgets this. Two gating criteria can both be satisfied only by an unstated third choice. Fix: exempt `S:3` from rows 20/48 with a shortened frontmatter variant pinned explicitly, or state the deletion budget.

**E/12 · MAJOR · `0-baseline.md:99` still says "8 occurrences across 5 files". Measured: 4 files. Pass 1 filed this as author-confirmed and it was not fixed.**

`3-redteam-plan.md:141`: *"**A/F7 ∥ C/O11** … *'8 occurrences across 5 files'* is **4**; a verbatim repeat of cycle 1's `pass2-C:45`" — "author-confirmed"*. `0-baseline.md:99` is unchanged. I verified all 8 cited lines exist and carry overclaim language; the file set is `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stage-7-assemble.md` = **4**. B7`:36` and criteria row 20 both say 4; only `0-baseline.md` says 5. This is the third cycle in which this number is wrong. Fix: change `5` to `4`.

**E/13 · MAJOR · §4 implements only half of config item (6). The "preserved-rule assertion MUST PASS" half is missing, and its instrument is E/1's printer.**

`guarded-change.architect.md:96-98` requires: *"every new-rule assertion MUST FAIL there **and every preserved-rule assertion MUST PASS**."* `1.5-criteria.md:146-147` states only *"**Every §1 row must FAIL there.**"* §1 contains no PRESERVE rows at all, so the preserve half devolves entirely onto R1 — whose oracle cannot fail. Net: **nothing** checks site-set non-erosion. Fix: add PRESERVE rows for the 21 baseline IDs' operative sentences, asserted to **pass** in the replay.

**E/14 · MAJOR · Row 15's pinned string is circular and detects nothing.**

`:62` pins `clean-or-resolved means clean-or-resolved as RES defines resolved`, required at all 13 measured sites. Pasting that sentence 13× satisfies the row while RES's three arms are absent from the corpus — the string carries no operative content and cannot discriminate a build that defines `resolved` from one that does not. Fix: pin the three arms (row 13's string) at the 13 sites, and delete row 15.

**E/15 · MINOR · X4's arms differ by more than the rule under test — the holed arm has no `tree/` at all.**

`find fixtures/X4/holed -type f` → **one** file, `config/planning.md`. Intact has `config/planning.md` + `tree/root/plan.md` + `plan.md.ingested`. A cold agent can return HALT because there is no plan tree to review, with no reference to `redteam_context`. The verdict is over-determined ⇒ the arm can pass for the wrong reason. The config diff also bundles **two** independent changes (`redteam_context` **and** `mode:`/`ingest_source`), so one verdict cannot attribute to S-CTX vs S-IGM. Fix: give holed the same tree; split the config diff across two clusters.

**E/16 · MINOR · X3's holed record states its own answer.**

`fixtures/X3/holed/tree/root/completeness/A.md:6`: `**Pass status:** DECLARED DEGRADED — the harness exposed no dispatcher-observable spawn id.` Row 11's pinned string is *"…the pass is **declared degraded** in the record, never un-run"*. The fixture hands the agent the conclusion verbatim; it need not apply the rule. Fix: remove the `Pass status:` line and let the arm derive it.

**E/17 · MINOR · Row 53 pins a command that cannot produce the output the oracle needs and that the oracle does not use.**

`:100` pins `grep -rlnow -- <ID> …`. `-l` suppresses line numbers, so `-rlnow` emits filenames only — I ran it: three bare filenames, no `file:line`. `ruleid-sitemap.sh:30` actually uses `grep -rnow`. METHODOLOGY would document a command inconsistent with its own instrument. Fix: pin `-rnow` (or `-rlw`, if filenames are the intent).

**E/18 · MINOR · Deleting an ID's index row silently removes it from both oracles' default scope (C/O9, open).**

Both scripts default `IDS` to `grep -oE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md` (`ruleid-sitemap.sh:17`, `idcollide.sh:25`). I deleted `GBP`'s index row: the default run dropped `GBP` from the output entirely, exit 0. Row 56 (`S-INDEX-complete`) is supposed to catch this, but it is the one row with no pinned string and no implementation. Fix: drive `IDS` from a frozen live-ID list, not from the file under test.

**E/19 · NITPICK · Row 20's `PROVEN` absence is a substring trap.** `PROVEN` ⊂ `PROVENANCE`. The change adds provenance duties (rows 9, 57); an uppercase `PROVENANCE` heading would fail row 20 for an unrelated reason. Currently safe (only `SKILL.md:3` matches case-sensitively). Fix: assert word-boundary `\bPROVEN\b`.

---

## Oracle mutation results

Scratch copies only; nothing under `WT/Architect` was modified. `O=…/hardening-cycle-2/oracles`.

| Mutation | Expected per `§4:150-157` | Observed | Discriminates? |
|---|---|---|---|
| **1** delete every `GBP` token from `stages/stage-5-gate.md` (`sed -i 's/GBP//g'`) | `MISSING GBP stages/stage-5-gate.md`, **exit 1** | site silently absent from the printed row, **exit 0** | **NO** |
| **2** keep `<!-- see GBP -->`, delete the operative sentence (`stage-5-gate.md:38`) | pinned-string assertion fails, **exit 1** | **byte-identical to baseline output**, exit 0 | **NO** |
| **3** append stray `GBP` to `templates/seed/leaf-task-spec.md` | `UNEXPECTED`, **exit 1** | extra site printed, **exit 0** | **NO** |
| **4** wrapped/bolded pinned string must **PASS** | PASS (normalization works) | **untestable** — `check.sh` does not exist; `ruleid-sitemap.sh` is not a string checker | **N/A** |
| **5** *(mine)* delete `GBP`'s row from METHODOLOGY's index, default run | ID still audited | `GBP rows in output: 0`, exit 0 — silently unaudited | **NO** |

```
$ bash $O/ruleid-sitemap.sh $SB/m1 GBP ; echo EXIT=$?
GBP  METHODOLOGY.md SKILL.md stages/charter.md stages/stage-2-draft-node.md
     stages/stage-3-completeness-critic.md stages/stage-4-adversarial-redteam.md
     stages/stage-7-assemble.md stages/stage-8-restart-resume.md
EXIT=0
$ diff <(grep ^GBP m0.txt) <(grep ^GBP m2.txt)   # mutation 2 vs baseline
*** BYTE-IDENTICAL TO BASELINE — false pass ***
```

`idcollide.sh` — genuinely discriminates on its stated self-test, but the exemption machinery leaks:

| Mutation | Expected | Observed | Discriminates? |
|---|---|---|---|
| **IDC-A** ids `KIL ING` | `COLLISION`, exit 1 | `KIL < SKILL`, `ING < PLANNING`, `ING < RULING`, **exit 1** | **YES** |
| **IDC-B** cycle-2's 16 new ids | OK, exit 0 | `IDCOLLIDE: OK (16 ids vs 62 tokens)`, exit 0 | yes (as run) |
| **IDC-C** add live token `TOPGATE`, check `TOP` | **COLLISION**, exit 1 (per `§2:120`) | `grandfathered : TOP < TOPGATE`, **exit 0** | **NO** — E/2 |
| **IDC-D** new id `SEVERITY` over live-but-unindexed `SEV` | flagged | no `SEV`/`SEVERITY` line at all, exit 0 | **NO** — E/18 (rule's letter not violated; scope is) |

---

## Pinned-assertion audit

Method: parsed all 57 rows mechanically; applied `§1`'s `normalize()`; tested each pinned string against each resolved site file, and each paired-absence string against the whole pinned corpus.

| Row | Genuinely operative & unique? | Satisfiable by text meaning the opposite? | SITES complete//correct? | Verdict |
|---|---|---|---|---|
| 1 S-BIND-cmp | yes — full `iff` proposition | only via E/5 foil | matches B7 P2 | ok |
| 2 S-BIND-disp | yes; absence pair well-chosen | E/5 only | ok | ok |
| 3 S-BIND-noparent | yes | E/5 only | ok | ok |
| 4 S-BIND-stale-exit | yes | E/5 only | ok | ok |
| 5 S-BIND-immut | yes | E/5 only | ok | ok |
| 6 S-BIND-rebind | yes | E/5 only | ok | ok |
| 7 S-BIND-gate-art | yes | E/5 only | ok | ok |
| 8 S-BIND-f5-limit | yes ("honest limitation:") | E/5 only | ok | ok |
| 9 S-IDN-disp | yes | E/5 only | ok | ok |
| 10 S-IDN-asym | yes; strong absence pair | E/5 only | ok | ok |
| 11 S-IDN-degraded | yes | E/5 only | ok | but X3 fixture states it — E/16 | 
| 12 S-IDN-sibling | yes | E/5 only | ok | ok |
| 13 S-RES-3arm | yes — three arms enumerated | E/5 only | ok | ok |
| 14 S-RES-states | yes | E/5 only | ok | ok |
| **15 S-RES-circ** | **no — circular, no operative content** | **yes, trivially: 13 pastes satisfy it with RES undefined** | 13 = B7 ✓ | **E/14** |
| **16 S-CTX-key** | **no — a description, not a string** | **yes — key present + "optional" prose** | 2 sites | **E/10** |
| 17 S-CTX-deconf | yes | E/5 only | ok | ok |
| 18 S-CTX-vacuous | yes | E/5 only | arm unscheduled — E/3 | ok/E3 |
| 19 S-OFL | yes; `Naming is the fence` correctly present at baseline | E/5 only | ok | ok |
| **20 S-PRV-neg** | yes | E/5 only | 8 sites/4 files = B7 ✓, but `S:3` collides with SC1 | **E/11**, E/19 |
| 21 S-PRV-limit | yes | E/5 only | "every site carrying the positive claim" is **unenumerated** | minor |
| 22 S-SPV | yes | E/5 only | ok | ok |
| 24 S-CNC-index | yes | E/5 only | **no — 4 of 9 unmeasured** | **E/6** |
| 26 S-CNC-gatelog | yes | E/5 only | **no — `s8` unmeasured, `s7` omitted** | **E/7** |
| 27 S-CNC-LOCK | yes | E/5 only | ok | **E/4** (L instrument absent) |
| 31 S-CNC-uncov | yes | E/5 only | single site `M`; stage-1 arguably needed | minor |
| **43 S-SPN** | yes (a heading) | no | **≠ B7; case unpinned; passes at 2/7 at baseline** | **E/9** |
| **44 S-SLOT** | **weak — bare heading** | **yes — empty section satisfies it** | ok | major-ish |
| **48 S-HG2-only** | yes | E/5 only | **label "7" vs 9 listed** | **E/8** |
| **52 S-XPM** | yes | E/5 only | **label "10" vs 14 listed; `ch:132`≠B7's 131** | **E/8** |
| **53 S-IDGREP** | **no — pins a non-working flag combo** | yes (could sit in a "don't" block) | 1 site | **E/17** |
| 55 S-IDGREP-name | yes | E/5 only | 1 site | ok |
| **56 S-INDEX-complete** | n/a — computed, **unimplemented** | n/a | 1 site | **E/18** |
| **57 S-CHARTER-PROV** | **no — "followed by the four added duties" unpinned; absence pair conditional** | yes | 1 site | **E/10** |

34 rows covered. The 20 uncovered BIND/DEC/DEP/HG2/IGM/TPL/RST rows were all measured and are in the "yes / E/5-only / ok" class.

---

## Corpus pin + baseline replay audit

**The corpus pin genuinely works — this is pass 2's one solidly earned fix.** I materialised the baseline (`git archive b08f5a9 Architect`), confirmed `diff -rq base live` over the pinned corpus is **empty** (the change is not built, so live == baseline there), implemented `§1`'s `normalize()`, and ran all 57 rows.

**Rows wrongly PASSING at baseline: 0 of 54 string rows.** C/O3 is closed for §1. `changes/` genuinely cannot enter: the pinned `CORPUS` list has no path that reaches it.

Rows that would wrongly **FAIL** for reasons unrelated to their rule:

| Row | Wrong-fail cause |
|---|---|
| 24 | 4 of 9 sites (`S`, `s7`, `ch`, `ex/README`) have no `index.md` concern — E/6 |
| 26 | `s8` is not a measured gate-log site — E/7 |
| 48 | `S:86` makes no "ONLY" claim (verified: it mentions `plan/topgate/` and a gate-bounce cap) — E/8 |
| 20 + 48 | `S:3` is length-capped by SC1 — E/11 |
| 43 | 2 of 7 sites pass only case-insensitively; under §1's literal rule they fail — E/9 |

Partial-oracle rows: **43** — its pinned string already matches at `tp/generic-node` and `tp/decomposition-node` at baseline (case-insensitively), so it cannot detect a failure to migrate at those 2 of 7 sites.

**Paired-absence polarity is correct and earned:** all 22 absence strings that should be present-at-baseline are present (`Naming is the fence` → `METHODOLOGY.md`; `PROVEN` case-sensitive → `SKILL.md`; `no single global cursor to stale-edit` → `METHODOLOGY.md` + `stage-8`; `DROPPED: nothing from the core.` → `charter.md`; etc.), and the four that must never exist (`at most 2 rebinds`, `three identical spawn_id values means the pass is un-run`, `tree/_status.md ← apex roll-up`, `a child ≥ 0.8× the parent trips the guard`) are absent. The absence half of the replay is a real can-fail test.

**But** config item (6)'s second half is unimplemented (E/13), so the replay tests only the new-rule direction.

---

## X protocol + executed-race audit

**Soundness.** The two structural fixes are real: holding `subagent_type` + model + prompt template constant genuinely removes C/O4's "two different agents disagreed" confound, and 2 spawns per arm is strictly better than 1.

**The false-pass probability claim is not sound.** `§0:15` claims *"lucky-split probability drops from ≈0.25 to ≈0.0625"*. That is `0.5⁴`, which requires the four spawns to be **independent** Bernoulli trials. They are not: the fix that earns the protocol its validity — same model, same template, same prompt — is precisely what makes the two spawns per arm **maximally correlated**. Two draws from the same weights on the same input are near-duplicates; the effective sample size is closer to 1 than 2, so the true lucky-split probability is much nearer 0.25 than 0.0625. The protocol should claim "the two-agent confound is removed", not a variance reduction it cannot have both ways.

**It can pass for the wrong reason, and one arm demonstrably will.** If a fixture is discriminable for a reason unrelated to the rule, the false-pass probability is not 0.0625 — it is ≈1, and *increasing* spawns makes it worse, not better, because every spawn reads the same give-away. Measured give-aways:
- **X4**: holed has no `tree/` at all (E/15) — HALT is over-determined.
- **X3**: the holed record announces `**Pass status:** DECLARED DEGRADED` (E/16) — the verdict is transcribed, not derived.
- **X1**: clean. `holed` and `intact` `plan.md` files are byte-identical (both `02ebf2a2…` / `87b2518a…`); the only diff is `completeness/A.md`'s recorded hash. **The "hash-real" claim at `§5:180-181` verifies**: `sha256sum` of `X1/intact/tree/root/branch-a/plan.md` = `87b2518a3690d966…`, exactly the value the record carries; holed carries `0000…`. The intact root record carries only its own hash — the no-parent carve-out is genuine.
- **X2**: clean. Sole diff is `Only in X2/intact/plan: assembly-approval.md`, which *is* the rule under test.

**Per-criterion granularity fails ST1.5d.** 4 spawns per cluster yield **one** verdict pattern for up to 8 criteria rows (§5's X1 = BIND×6 + RES + IDN). A pass can be carried entirely by the one item the agent happened to discriminate. `fixtures/README.md:29-31` concedes this ("recorded as incidental, **not** counted as their verification") for S-DEP/S-RES in X2 but not for X1's bundle.

**The lock race is a proxy, not a representative harness.** S-CNC-LOCK governs **prose that instructs an agent** — row 27's pinned string is inserted into `s1`, `s6`, `M`, `tp/README`. A two-process `mkdir` race in a scratch dir tests **`mkdir`'s POSIX atomicity**, a kernel property that this change does not touch and that was never in doubt (I measured it: 200 concurrent contenders → exactly **1 winner**). It does not test whether an agent reading stage-6 takes the lock, releases it on the failure path, or releases it *"before any HALT"* — and the HALT path is exactly the one a shell script cannot represent, because the agent's HALT is a kill, and I showed a killed holder **leaks the lock** (E/4). So `§0:19`'s *"**The catalog lock IS executable**"* is true of the mechanism and false of the duty. Under CH9 this is a gating criterion verified against a proxy: `P` (the text assertion) is the load-bearing half, and `L` should be labelled a supporting mechanism check, not the criterion's verification.

---

## Baseline counts re-verified

Commands run against `$SB/base` (= `git archive b08f5a9 Architect`), corpus `SKILL.md METHODOLOGY.md README.md stages templates examples`.

| Claim | My measured value | Agrees? |
|---|---|---|
| 21 live rule IDs vs **18** index rows (`0-baseline.md:57`) | index rows = **18** (`grep -cE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md`); 18 + `TPL1`,`TPL2`,`SEV` = **21** | **yes** |
| Phantom set = `TOP` @ `METHODOLOGY.md:79` + `examples/…/planning.md:25` only (`:61-62`) | `grep -rnow TOP` → 11 hits; exactly those two are `ON TOP OF` (verified by reading both lines) | **yes** |
| `TOP` is **not** a `stage-8` site; only match is `HARDSTOP` (`:63`) | `grep -n HARDSTOP stages/stage-8-restart-resume.md` → `:20`; no word-boundary `TOP` hit in `s8` | **yes** |
| `TOP` site set = METHODOLOGY, SKILL, stage-6, decomposition-node (B2`:46`) | oracle output identical, with both phantoms `EXCLUDED` and reported | **yes** |
| **8 overclaim occurrences across 4 files** (criteria `:67`, B7`:36`) | 8 hits; files = SKILL, METHODOLOGY, README, stage-7 = **4**; all 8 cited lines verified to carry overclaim text | **yes** |
| …but `0-baseline.md:99` says "across **5** files" | **4** | **NO** — E/12 |
| §4-heading spellings (`0-baseline.md:111` "6 spellings"; B7`:190` "7 hits in 6 files") | **8 hits in 7 files** — B7 omits `SKILL.md:18`; ~6 distinct spellings | **NO** — E/9 |
| `SKILL.md:18-19`'s §4 heading is "genuinely wrapped" (`:156-157`) | confirmed: `**Outputs &\n   artifacts WITH their locations**` — wrapped mid-phrase | **yes** |
| `index.md` **18 accessors across 9 files** | **11 hits in 5 files** (M, s1, s6, s8, tp/README). The 18/9 figure is B7's **gate-log** count (P9b), not index.md (P9a) — the prompt's framing conflates them | index.md **no**; gate-log 18/9 **yes** |
| **13** `clean-or-resolved` sites | `grep -rn 'clean-or-resolved'` → **13 hits in 8 files** | **yes** |
| **7** "top-level ONLY" sites | B7's 7 verified present; criteria row 48 lists **9** | B7 **yes**; criteria **no** — E/8 |
| **10** terminus sites | B7 measures **14 hits in 9 files**; criteria row 52 lists 14 but labels them "10" | **NO** — E/8 |

---

## Coverage challenge (CH8)

Behaviours this change could alter that **no criterion observes**:

1. **The catalog lock leaking across runs.** Row 29 covers *breaking* a stale lock, but nothing observes the frequency-one case a HARDSTOP creates: I measured that a killed holder leaves the lock held and the next run **BLOCKED**. A user whose run is interrupted finds every subsequent run wedged at stage 1. No criterion asserts the run detects and reports this rather than hanging. **Severity: major.**
2. **`index.md` becoming derived removes the only restart cursor.** Row 24 makes `index.md` non-authoritative and regenerated by the top orchestrator. `stage-8` currently reads it (B7 P9a: `stage-8:9`, `:32`). No criterion observes that restart still works when `index.md` is stale or absent mid-run, and no row lists `s8` for row 24's rule. **Severity: major.**
3. **Description-length regression cascading into skill discovery.** SC1 caps at 1024 but nothing observes that the description still *triggers* — SC2 checks four substrings survive, not that the trimmed description retains its discriminating power after ~186 chars are cut (E/11). **Severity: minor.**
4. **The `SEV` / `TPL1` / `TPL2` index rows this cycle adds.** Row 56 requires the index be complete, but row 56 is the one row with no pinned string and no implementation (E/18), so the very gap `0-baseline.md:57` names as "this cycle closes it" has no working observer. **Severity: major.**
5. **Cost/fan-out of 12→16 arms** — correctly declared out of scope (`§6`), not a gap.

---

## Label audit (CH9/CH10)

Every §1 row is labelled **gating**; no advisory label to challenge, and `§0:19` correctly *promotes* S-CNC-LOCK from pass 1's advisory relabel. No deferral-loophole relabelling found. `§1:27-30` correctly deletes the "declared deferral" route and names HALT + verbatim relay as the only remaining move under RAT3. `decisions.md` contains **no** named risk-acceptance — correct only if no gating criterion is unverified, which is false (below).

Gating criteria checked, governed path confirmed, and evidence:

| Gating criterion | Governed path | Evidence I checked | Verdict |
|---|---|---|---|
| **R1** site-set non-erosion | `ruleid-sitemap.sh` over the corpus | ran 5 mutations; **no failure path exists** (`:34 exit 0`); `expected-sites.txt` absent | **`verified = no`**, unacknowledged, no risk-acceptance ⇒ **silent drop (H5's third illegal disposition)** |
| **R3** ID collision | `idcollide.sh` `GRAND` list | reproduced `TOP < TOPGATE` → exit 0 | **`verified = no`** for this cycle's own likely collision |
| **§1 rows 1–55 (P)** | normalized substring at each site | implemented `normalize()`, ran all 57 against baseline: 0 wrong passes | **path confirmed**; but `check.sh` does not exist ⇒ H6 "an unreviewed check is not a check" applies to the checker itself |
| **row 56** S-INDEX-complete | computed index↔hit bijection | no string, no script, no implementation | **`verified = no`** |
| **S-CNC-LOCK / -first (L)** | agent prose in s1/s6/M/tp/README | `lockrace.sh` absent; I executed the race: mkdir atomic ✓, crash **leaks** ✗, unguarded control **does not fail** ✗ | **proxy, and the proxy's own expectations are wrong** — E/4 |
| **X1 (BIND/RES/IDN)** | cold-agent judgement on a run tree | fixture verified hash-real; arms differ only by the recorded hash | **path confirmed**, but 8 rows share one verdict pattern (ST1.5d) |
| **X2 (HG2/XPM/SC3)** | cold-agent judgement + whole edited `SKILL.md` | sole arm diff is `assembly-approval.md` — the rule itself | **path confirmed** (best of the four) |
| **X3 / X4** | cold-agent judgement | X3 transcribes its verdict; X4 holed has no tree; X4 unscheduled by §5 | **passes for the wrong reason** — E/3, E/15, E/16 |
| **SC5** | named rubric, judge = this runner at stage 8 | judge + scale + pass definition + recorded artifact all present | **legitimately upgraded** from pass 1's inspection-only (C/O12 closed) |
| **SC1/SC2/SC4** | `quick_validate.py`, measured description, `diff -rq` | mechanical, path correct | ok, but SC1 collides with rows 20/48 — E/11 |

**Four gating criteria are unverifiable pre-ship (R1, R3-for-this-cycle, row 56, S-CNC-LOCK's duty) with no named risk-acceptance in `decisions.md`** — the same H5 silent-drop that `3-redteam-plan.C.verbatim.md:449` filed against pass 1.

---

## Ranked list

| # | ID | Severity | One-line |
|---|---|---|---|
| 1 | **E/1** | **blocker** | `ruleid-sitemap.sh:34` is still `exit 0`; `expected-sites.txt`/`check.sh`/`baseline-replay.sh` don't exist — C/O1+C/O2 claimed closed, entirely open; all 4 pass-1 mutations reproduce at exit 0 |
| 2 | **E/2** | **blocker** | `idcollide.sh:31` still grandfathers `TOP TOPGATE`/`DEC DECOMPOSITION`; §2 R3 claims removed; reproduced exit 0 on this cycle's own collision |
| 3 | **E/3** | **blocker** | §5 declares 3 clusters/12 spawns; `fixtures/` has 4 — S-CTX/S-IGM arms unscheduled, and on-disk X3's inverted polarity auto-fails §5's blanket pass rule |
| 4 | **E/4** | **blocker** | `lockrace.sh` absent; executed race shows the crash case **leaks the lock** and the H4 unguarded control **does not fail** |
| 5 | **E/5** | major | normalized-substring presence has no polarity guard — all 54 rows satisfiable by the sentence quoted as a foil |
| 6 | **E/11** | major | SC1's 1024-char cap vs rows 20+48 both requiring `SKILL.md:3`: measured 954 + 76 + 180 |
| 7 | **E/13** | major | config item (6)'s "preserved-rule assertion MUST PASS" half unimplemented; its instrument is E/1's printer |
| 8 | **E/6** | major | row 24 labels a hand-selected 9-file list "all 9 measured"; B7 measured 11 hits in 5 files |
| 9 | **E/9** | major | row 43's SITES ≠ B7 (B7 under-measured `SKILL.md:18`); case unpinned; passes at 2/7 sites at baseline |
| 10 | **E/8** | major | row 48 says "7" and lists 9; row 52 says "10" and lists 14; `ch:132` ≠ B7's `charter.md:131` |
| 11 | **E/7** | major | row 26 requires unmeasured `s8`, omits measured `s7` |
| 12 | **E/14** | major | row 15's pinned string is circular — 13 pastes satisfy it with RES undefined |
| 13 | **E/10** | major | rows 16/57 still describe rather than pin; row 57's absence pair is conditional |
| 14 | **E/12** | major | `0-baseline.md:99` "5 files" is 4 — filed in pass 1 as author-confirmed, unfixed for the third cycle |
| 15 | **E/15** | minor | X4 holed arm has no `tree/`; blocking verdict over-determined; config diff bundles two rules |
| 16 | **E/16** | minor | X3 holed record states `Pass status: DECLARED DEGRADED` — the answer is transcribed |
| 17 | **E/17** | minor | row 53 pins `grep -rlnow`, which cannot emit `file:line` and contradicts `ruleid-sitemap.sh:30`'s `-rnow` |
| 18 | **E/18** | minor | deleting an ID's index row drops it from both oracles' default scope; row 56 (its observer) is unimplemented |
| 19 | **E/19** | nitpick | `PROVEN` ⊂ `PROVENANCE`; absence assertion needs `\b` anchors |

Lenses: **factual** — E/1, E/2, E/6–E/9, E/12, E/17, all cited and measured. **Logical** — E/3, E/5, E/11, E/13, E/14. **Missed opportunity** — the `expected-sites.txt` design pass 1 prescribed is still ~20 lines of unwritten script that would make R1 can-fail; and driving §1's SITES columns *out of* B7 mechanically (instead of retyping them) would have caught E/6–E/9 for free. **Unstated assumptions** — that two same-model spawns are independent trials (E/5, X-protocol); that a trap releases a lock on HARDSTOP (E/4); that B7 is authoritative when it disagrees with `0-baseline.md` (E/9). **Fidelity** — "checker" is still substituted by *printer* for R1; "oracle can fail" by *the four mutations were listed* (they were never run); "executed race" by *a script that does not exist*; "representative" by *tests mkdir, not the prose duty* for S-CNC-LOCK; "measured" by *hand-retyped* for rows 24/26/43/48/52; "pinned" by *described* for rows 16/57. Each remains untrusted until the owner confirms.

Earned clean results, credited: the **corpus pin** (0 of 54 rows wrongly pass at baseline; `changes/` genuinely cannot enter), the **paired-absence polarity** (all 22 strings correctly present-at-baseline / never-present), **X1's hash-real fixture** (recomputed, matches), **X2's single-diff arm**, the **phantom triage** (exactly right, and the oracle reports its exclusions), and **SC5's** upgrade to a real rubric.

**WORST SEVERITY: blocker**

---

## Provenance

**Agent type:** cold independent reviewer subagent, frame E (oracle + criteria validity, round 2). **Model:** `claude-opus-5`. **spawn_id: unavailable.**

Closed input set read (all under `WT = /home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`):

```
d3b9d1cfd62249d95a2c954201771a44679cb66b41b2103877827672279217d3  Architect/changes/hardening-cycle-2/1.5-criteria.md
251b008fd1e086fdad8c8374555b3e1b483860f325e71e6d85af5942b6673d10  Architect/changes/hardening-cycle-2/0-baseline.md
0b8da5013bd624f17d76839cd541556e8c0349900021c0388721039b7a3691a9  Architect/changes/hardening-cycle-2/0-baseline.B7-measured-sites.md
f73326c07af9cc884ccd3ed222ca7017f005cfd31d9d5bfad2ce371f10c6c943  Architect/changes/hardening-cycle-2/1-spec.md
b5628634e2a798caabeb046589ff0a189109fecf0842867202cde0e9ca50805e  Architect/changes/hardening-cycle-2/2-plan.md
953805796fb4d47739467e3556976beb12e3923da06a49ef0dbc8fe95375a5e8  Architect/changes/hardening-cycle-2/3-redteam-plan.md
404f90062aedebd9d2cea2f37abec4c750cd2a60752c6866145115903c94e140  Architect/changes/hardening-cycle-2/3-redteam-plan.C.verbatim.md
edf5129851fff3c0bc560a36421777386c56ef702b654b02f53d2926fc56e80e  Architect/changes/hardening-cycle-2/decisions.md
6ab0743f310c31ca79bbe74e78d69fd9abb28559e7ae32c16f38c7e7aad0737b  Architect/changes/hardening-cycle-2/oracles/idcollide.sh
eb011e56b37fe5824f5db07b97be68a1d84553d6f2acc1f938a8c5ee4cd3bb28  Architect/changes/hardening-cycle-2/oracles/ruleid-sitemap.sh
b842147a189f0ff27f9935d40ca66a38bb3cb49c0fde8e1b06d28cd41742ba55  Architect/changes/hardening-cycle-2/fixtures/README.md
bd8d74936e88603ed0e4b67c1546a27325b84d85cda121b4cb0af9f84fa0f678  Architect/guarded-change.architect.md
c6b22f7f43ca3f611cc3b4505202b5d834a1594c3a3254e1f35d0f00323a860b  Guarded_change/stages/stage-1.5.md
8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3  Guarded_change/stages/stage-8.md
```

Also read (source under review, unmodified): `Architect/SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/*.md`, `templates/seed/*.md`, `examples/authoring-a-skill/*.md`; the baseline of each via `git archive b08f5a9 Architect`; and every file under `Architect/changes/hardening-cycle-2/fixtures/X{1,2,3,4}/`.

**Not read** (declared, so the record is honest): `1.5-criteria.v1-superseded.md`, `1-spec.v1-superseded.md`, `2-plan.v1-superseded.md`, `3-redteam-plan.{A,B}.verbatim.md`, `3-charter-given.md`, `context-hashes.txt`, `changes/hardening-cycle-1/`, `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md`, `Guarded_change/changes/audit-hardening-2026-07/`. Pass 1's findings were read only via `3-redteam-plan.md` and `3-redteam-plan.C.verbatim.md`, per the "check closure, do not re-derive" instruction.

**Mutation isolation:** all mutations ran on copies under `/tmp/claude-1000/…/scratchpad/{live,base,m1,m2,m3,m5,c,d,lockrace}`. Nothing under `WT/Architect` was modified; `git status` for that path is unchanged (`?? Architect/changes/hardening-cycle-2/` only, as at start).
