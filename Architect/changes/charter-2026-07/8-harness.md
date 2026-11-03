# Stage 8 — Harness. BUILT AND RUN. (2026-07-28; re-run and EXTENDED 2026-07-29)

**Everything below is past tense because it happened.** The scripts exist, they were run, and their exact
invocations and exact output are pasted. Nothing here is a description of intended behaviour.

> ## ⚠ THE 2026-07-28 RESULTS BELOW WERE MEASURED AGAINST A SET THAT WAS SUBSEQUENTLY FOUND BLOCKED.
>
> They stand **as run** and are kept for the record. They do **not** describe the shipped artifact. The
> 2026-07-29 section immediately below supersedes them, and one of the 2026-07-28 numbers is now known to
> have been **meaningless**: `ruleplace.sh` returned **76 passed / 0 failed** on a set carrying **eight
> duplications of common-core rules**, because every probe in it is a *positive per-site assertion* and no
> set of those can express a negative property. That is not a bug in the rule table; it is a structural
> limit of the instrument, and it is why `shared_spans.py` was built.

---

# 2026-07-29 — after the gate-7 repairs

> ## 🔴 READ BEFORE USING ANY NUMBER BELOW. GATE 7 RETURNED **BLOCKER, 3/3**, AND THREE REVIEWERS BROKE THIS HARNESS.
>
> The numbers below (**92/0**, **0 undeclared spans**, **87/87**) were **reproduced exactly and
> independently by all three cold reviewers**, so they are honest and not fabricated. **They are also worth
> much less than they look**, and every one of the following was demonstrated by execution, not argued:
>
> 1. **The suite cannot tell a rule from its negation.** Reviewer O inverted four rules — *"You do not
>    demote"* → *"You SHOULD demote freely"*, *"Cite or it doesn't count"* → *"Cite nothing; citations do
>    not count"* — and got **`92 passed, 0 failed`, byte-identical to the clean run.** The runner
>    reproduced it. Every probe is an unanchored substring `grep`, and **there is no NEGATION mutant
>    class.** The inverted rules include the gating content of **N-10, N-12, B08 and B14**.
> 2. **N-03 barely discriminates, and the "strengthening" described below overstates itself.** Reviewer Q
>    ran each rule's description terms against **all nine files**. Reproduced by the runner:
>    **9 of 19 rules also pass against a file they were never claimed to be in**, and **B09 passes against
>    all eight.** For nearly half the rules the probe returns the same PASS had the allocation table named
>    the **wrong** destination. **`grep -c 'N-03' oracles/mutation-test.sh` → 0**, so the 87/87 figure
>    carries **no** evidence about it at all.
> 3. **One mutant arm is a printer.** In the N-M6(d) exemption arm, **both branches increment `ok`** —
>    `SURVIVED` scores as a pass (reviewer P). N-M6(d) is gating. **So 87/87 contains an arm structurally
>    incapable of failing** — the printer-checker class this project has now shipped **four** times, this
>    time inside the instrument built to repair GATE-B2.
> 4. **`shared_spans.py` misses paraphrases, and four live ones were found by hand** — including the
>    *"grip the handle"* example duplicated into `leaf.md` and `redteam.md` **by this run**, and
>    `combiner.md`'s paraphrase of the demotion prohibition that FRZ-2 says *"binds every role and stays
>    common"*. **A clean run means no verbatim restatement survives. Nothing more.**
> 5. **Probe IDs `N-05e`–`N-05h` are each used twice**, so "92 passed" overstates distinct-criterion
>    coverage and `failed:<id>` is ambiguous.
> 6. **Gating criteria N-15a, N-20, N-25 and N-26 have no probe**, and the *"What ships UNVERIFIED"* table
>    below **omits all four** — so that table is itself incomplete.
>
> **Nothing below has been repaired.** The section is left as run, because the record of what was measured
> is what makes the reviewers' refutations checkable. Full findings: `decisions.md`'s last three entries
> and `records/reviewer-{O,P,Q}-verbatim.md`.


Accept bar: `1.5-criteria-v2.md` **as amended under FRZ-2** (sha256
`eaff14ac6e44189ea6d6195d138305b83dd243ce9bd4e1671c4a8a3210b0ba5e`). Artifact: `Architect/stages/` —
**nine files, 891 lines** (manifest + eight dispatched).

**Verbatim commands and output: `records/harness-run-2026-07-29.txt`.** Exit codes there are captured from
each script directly and never through a pipe — a piped `$?` is the *last* command's status, and this
project has already once read a usage error as a pass.

## What was measured

| Instrument | Result | Exit |
|---|---|---|
| `oracles/ruleplace.sh ../../stages` | **92 passed, 0 failed** | 0 |
| `oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl` | **0 undeclared shared spans** | 0 |
| `oracles/mutation-test.sh ../../stages` | **87 mutants as expected, 0 unexpected** | 0 |
| all three with no argument | usage text | **2** (distinct from a pass) |

## What was ADDED this run, and why each addition was necessary

| Path | sha256 | Why it exists |
|---|---|---|
| `oracles/shared_spans.py` | `91db7fcd57c2068c…` | **The negative assertion.** Reports every normalized shared word-span ≥7 words between `charter-common.md` and each role file, and between role files, exempting only declared spans **and only for the file pair each was declared for**. This is the instrument GATE-B2 proved was missing: a reviewer ran the equivalent sweep by hand in one pass and it returned the duplications, so **the instrument was cheap and had simply not been built.** |
| `oracles/declared-duplications.jsonl` | `2db1c385322239cb…` | The declared-duplication register. It is **the same file the manifest publishes to readers and the harness reads as its exemption list**, so a duplication is either declared in a place a human reviews or it fails the build. |

## Three defects the extended harness found in itself or in the artifact — it earning its place

1. **`shared_spans.py` did not know about the two new files.** Its `ROLES` list was written before
   `redteam-plan.md` and `redteam-split.md` existed, so duplications in the two newest files were
   invisible. **Found by the duplication mutants, not by reading the script** — the per-role kill mutants
   reported `SURVIVED` for exactly those two names.
2. **The register was a *global* amnesty, not a per-pair one.** A span declared for `redteam-plan.md` ~
   `redteam-split.md` was exempt everywhere, so re-adding it to a third file would have been legal. Found
   by mutant (d), which was written specifically to test whether the exemption list could be abused.
   Fixed by scoping each exemption to its declared `sites` pair; the mutant now reports `KILLED`.
3. **The N-03 fork-fidelity probe was very nearly vacuous.** As built it asserted only that the
   destination file *"exists and is non-empty"* — **nineteen probes that would pass for any nine non-empty
   files.** That is the same class as the two bare `exit 0` checkers this project has already shipped, and
   it had been reported as fork fidelity "verified rule-by-rule". Replaced with a 60% overlap against the
   rule description **taken from the artifact's own allocation table**, so the probe set stays generated
   rather than hand-written. On first run the strengthened probe **failed B19**, which surfaced that
   `charter-common.md` never used the word "composition" for its own composition rule.

## What this harness still does NOT verify — unchanged and not to be quietly assumed

- **`oracles/rules.tsv` is AUTHOR-WRITTEN.** It proves the rules it names sit in the files it names. It is
  **not** evidence that `1.5-criteria-v2.md` is fully covered. Only the N-03 probe set is generated.
- **The 60% threshold in N-03 is a judgement, not a derivation.** `B15` passes at **2 of 3** terms, one
  step above the line. A different threshold would change that verdict.
- **`shared_spans.py` compares word spans and therefore cannot see a PARAPHRASED restatement.** Two of the
  duplications repaired this run — the *floor-is-wrong* clause in `divider.md` and `leaf.md` — were found
  by reading, **not** by the sweep, because they were worded differently from the common core's version.
  **A clean run of this instrument does not mean the composition rule holds; it means no *verbatim*
  restatement survives.**
- **No behavioural evidence exists for any file in this set.** `fixtures/` is empty and no agent has ever
  been handed a composed prompt. See `1.5-criteria-v2.md` Part B for the runner's position on that, which
  **sustains the cut of the A/B arms on their own design and rejects the further claim that no behavioural
  evidence is needed at all.** The replacement smoke test is **specified and NOT run.**

---

# ARCHIVED — the 2026-07-28 run, kept verbatim. Superseded by the section above.


Accept bar: `1.5-criteria-v2.md` (the re-scoped set). Artifact: `Architect/stages/` — seven files.

## What was built

| Path | sha256 | What it does |
|---|---|---|
| \`oracles/ruleplace.sh\` | \`0633a0b8fbf7ca00…\` | Per-FILE positive assertions. Every probe is scoped to one file, because the only thing this element changed is WHICH file a rule lives in. |
| \`oracles/mutation-test.sh\` | \`f490d91e9d180f50…\` | Four mutant classes — deletion, relocation, insertion, negative control — proving `ruleplace.sh` can fail. |
| \`oracles/delete_span.py\` | \`704afd66fc04a2b0…\` | Deletes the minimal contiguous line span whose NORMALIZED join contains an anchor. Needed because anchors wrap across line breaks. |
| \`oracles/rules.tsv\` | \`8fbd5937bb4d9f89…\` | The probe table. **AUTHOR-WRITTEN, not generated** — see the honesty note below. |

## Hygiene check — a no-argument call cannot be misread as a pass

This project once "verified" a checker by running it with no arguments and reading the usage error as a
pass. Both scripts return **exit 2** for usage, distinct from 0.

```
$ ./oracles/ruleplace.sh
usage: ./oracles/ruleplace.sh <set-dir> [rules.tsv]
  <set-dir> is the directory holding charter.md, charter-common.md, redteam.md,
  divider.md, combiner.md, leaf.md, node.md
exit=2
```

## Run 1 — the clean set

```
$ ./oracles/ruleplace.sh ../../stages
PASS  N-01a  present in charter.md
PASS  N-01b  present in charter.md
PASS  N-01c  present in charter.md
PASS  N-01d  present in charter.md
PASS  N-01e  present in charter.md
PASS  N-02  absent from whole set
PASS  N-04a  present in charter-common.md
PASS  N-04b  present in charter-common.md
PASS  N-04c  present in charter-common.md
PASS  N-04d  present in charter-common.md
PASS  N-05a  present in redteam.md
PASS  N-05b  present in divider.md
PASS  N-05c  present in leaf.md
PASS  N-05d  present in node.md
PASS  N-05e  present in combiner.md
PASS  N-05f  present in node.md
PASS  N-05g  present in node.md
PASS  N-05h  present in node.md
PASS  N-06a  present in charter-common.md
PASS  N-06b  present in charter-common.md
PASS  N-06c  present in charter.md
PASS  N-07  present in redteam.md
PASS  N-08a  present in redteam.md
PASS  N-08b  present in redteam.md
PASS  N-09a  present in charter-common.md
PASS  N-09b  present in charter-common.md
PASS  N-09c  present in redteam.md
PASS  N-09d  present in leaf.md
PASS  N-09e  present in divider.md
PASS  N-10a  present in charter-common.md
PASS  N-10b  present in charter-common.md
PASS  N-10c  present in charter-common.md
PASS  N-10d  present in charter-common.md
PASS  N-10e  absent from redteam.md
PASS  N-11a  present in node.md
PASS  N-11b  present in node.md
PASS  N-11c  present in redteam.md
PASS  N-11d  absent from whole set
PASS  N-12a  present in combiner.md
PASS  N-12b  present in combiner.md
PASS  N-12c  present in combiner.md
PASS  N-12d  present in combiner.md
PASS  N-12e  present in combiner.md
PASS  N-12f  present in combiner.md
PASS  N-13a  present in redteam.md
PASS  N-13b  present in redteam.md
PASS  N-13c  present in redteam.md
PASS  N-13d  present in redteam.md
PASS  N-13e  present in charter-common.md
PASS  N-13f  present in charter.md
PASS  N-17  absent from all six dispatched files
PASS  N-18  absent from whole set
PASS  N-19a  present in charter-common.md
PASS  N-19b  present in redteam.md
PASS  N-19c  present in combiner.md
--- N-03 fork-fidelity (probe set generated from charter.md's allocation table) ---
PASS  N-03/B01  destination charter-common.md exists and is non-empty
PASS  N-03/B02  destination redteam.md exists and is non-empty
PASS  N-03/B03  destination redteam.md exists and is non-empty
PASS  N-03/B04  destination redteam.md exists and is non-empty
PASS  N-03/B05  destination redteam.md exists and is non-empty
PASS  N-03/B06  destination redteam.md exists and is non-empty
PASS  N-03/B07  destination redteam.md exists and is non-empty
PASS  N-03/B08  destination charter-common.md exists and is non-empty
PASS  N-03/B09  destination charter-common.md exists and is non-empty
PASS  N-03/B10  destination charter-common.md exists and is non-empty
PASS  N-03/B11  destination redteam.md exists and is non-empty
PASS  N-03/B12  destination redteam.md exists and is non-empty
PASS  N-03/B13  destination redteam.md exists and is non-empty
PASS  N-03/B14  destination combiner.md exists and is non-empty
PASS  N-03/B15  destination charter-common.md exists and is non-empty
PASS  N-03/B16  destination redteam.md exists and is non-empty
PASS  N-03/B17  destination redteam.md exists and is non-empty
PASS  N-03/B18  destination divider.md exists and is non-empty
PASS  N-03/B18  destination redteam.md exists and is non-empty
PASS  N-03/B19  destination charter-common.md exists and is non-empty
PASS  N-03  allocation table covers all 19 fork-source rules
==== 76 passed, 0 failed ====
exit=0
```

**76 assertions passed, 0 failed.**

## Run 2 — the oracle-can-fail self-test (this is what makes run 1 mean anything)

```
$ ./oracles/mutation-test.sh ../../stages
=== DELETION mutants ===
  ok   DELETION N-01a: KILLED (expected KILLED)
  ok   DELETION N-01b: KILLED (expected KILLED)
  ok   DELETION N-01c: KILLED (expected KILLED)
  ok   DELETION N-01d: KILLED (expected KILLED)
  ok   DELETION N-01e: KILLED (expected KILLED)
  ok   DELETION N-04a: KILLED (expected KILLED)
  ok   DELETION N-04b: KILLED (expected KILLED)
  ok   DELETION N-04c: KILLED (expected KILLED)
  ok   DELETION N-04d: KILLED (expected KILLED)
  ok   DELETION N-05a: KILLED (expected KILLED)
  ok   DELETION N-05b: KILLED (expected KILLED)
  ok   DELETION N-05c: KILLED (expected KILLED)
  ok   DELETION N-05d: KILLED (expected KILLED)
  ok   DELETION N-05e: KILLED (expected KILLED)
  ok   DELETION N-05f: KILLED (expected KILLED)
  ok   DELETION N-05g: KILLED (expected KILLED)
  ok   DELETION N-05h: KILLED (expected KILLED)
  ok   DELETION N-06a: KILLED (expected KILLED)
  ok   DELETION N-06b: KILLED (expected KILLED)
  ok   DELETION N-06c: KILLED (expected KILLED)
  ok   DELETION N-07: KILLED (expected KILLED)
  ok   DELETION N-08a: KILLED (expected KILLED)
  ok   DELETION N-08b: KILLED (expected KILLED)
  ok   DELETION N-09a: KILLED (expected KILLED)
  ok   DELETION N-09b: KILLED (expected KILLED)
  ok   DELETION N-09c: KILLED (expected KILLED)
  ok   DELETION N-09d: KILLED (expected KILLED)
  ok   DELETION N-09e: KILLED (expected KILLED)
  ok   DELETION N-10a: KILLED (expected KILLED)
  ok   DELETION N-10b: KILLED (expected KILLED)
  ok   DELETION N-10c: KILLED (expected KILLED)
  ok   DELETION N-10d: KILLED (expected KILLED)
  ok   DELETION N-11a: KILLED (expected KILLED)
  ok   DELETION N-11b: KILLED (expected KILLED)
  ok   DELETION N-11c: KILLED (expected KILLED)
  ok   DELETION N-12a: KILLED (expected KILLED)
  ok   DELETION N-12b: KILLED (expected KILLED)
  ok   DELETION N-12c: KILLED (expected KILLED)
  ok   DELETION N-12d: KILLED (expected KILLED)
  ok   DELETION N-12e: KILLED (expected KILLED)
  ok   DELETION N-12f: KILLED (expected KILLED)
  ok   DELETION N-13a: KILLED (expected KILLED)
  ok   DELETION N-13b: KILLED (expected KILLED)
  ok   DELETION N-13c: KILLED (expected KILLED)
  ok   DELETION N-13d: KILLED (expected KILLED)
  ok   DELETION N-13e: KILLED (expected KILLED)
  ok   DELETION N-13f: KILLED (expected KILLED)
  ok   DELETION N-19a: KILLED (expected KILLED)
  ok   DELETION N-19b: KILLED (expected KILLED)
  ok   DELETION N-19c: KILLED (expected KILLED)
=== RELOCATION mutants (sample) ===
  ok   RELOCATION(redteam.md->leaf.md) N-09c: KILLED (expected KILLED)
  ok   RELOCATION(leaf.md->node.md) N-09d: KILLED (expected KILLED)
  ok   RELOCATION(divider.md->leaf.md) N-09e: KILLED (expected KILLED)
  ok   RELOCATION(node.md->leaf.md) N-11a: KILLED (expected KILLED)
  ok   RELOCATION(combiner.md->leaf.md) N-12a: KILLED (expected KILLED)
  ok   RELOCATION(charter-common.md->leaf.md) N-13e: KILLED (expected KILLED)
  ok   RELOCATION(charter-common.md->leaf.md) N-19a: KILLED (expected KILLED)
=== INSERTION mutants (the correct mutant for an absence sweep) ===
  ok   INSERTION N-02: KILLED (expected KILLED)
  ok   INSERTION N-11d: KILLED (expected KILLED)
  ok   INSERTION N-17: KILLED (expected KILLED)
  ok   INSERTION N-18: KILLED (expected KILLED)
  ok   INSERTION N-10e: KILLED (expected KILLED)
=== CONTROL mutant (expected SURVIVED — proves the harness can print a non-kill) ===
  ok   CONTROL: SURVIVED (expected SURVIVED) — an unasserted line was deleted and the suite still passed
==== mutants behaving as expected: 63 ; unexpected: 0 ====
exit=0
```

**63 mutants, all behaving as expected: 50 deletion, 7 relocation, 5 insertion, 1 negative control.**

- **N-M1 deletion — met.** Every one of the 50 positive assertions was KILLED when its rule's text was
  removed from its owning file.
- **N-M2 relocation — met.** Seven rules were *moved into the wrong file* rather than deleted, so the text
  was still present **somewhere in the set**. All seven assertions still KILLED. A probe that grepped the
  whole set would have SURVIVED every one of these — which is exactly the defect this element could have
  shipped, since **placement is the only thing the re-scope changed**.
- **N-M3 insertion — met.** All five absence sweeps FAILED on insertion of the forbidden text and PASSED on
  the clean set.
- **N-M4 negative control — met.** An unasserted line (`node.md`: "You are a stack frame, not a service.")
  was deleted and the suite still passed, printing **SURVIVED**. The harness has been observed printing a
  non-kill, so it is not a printer.
- **N-M5 — met.** The invocations above are verbatim, arguments included.

## Two real defects the mutation test found, in the oracle itself

Both were found by the self-test and not by inspection. This is the self-test earning its place.

1. **`norm()` stripped `_` as a markdown emphasis marker**, which destroys every identifier in the spec —
   `Human_gate`, `work_queue`, `node_id`, `Memo_read`. It produced **five false absences** on the first
   clean run. Fixed; `_` is no longer stripped and the reason is a comment in the script.
2. **Probe N-01c asserted the literal `CARRIED:`, which also matches `DELIBERATELY NOT CARRIED:`.** The
   deletion mutant SURVIVED: the probe would have passed with the entire CARRIED list removed. It was
   **matching a phrase, not a rule** — the precise failure C-M1 was written to catch, one level up in the
   instrument. Anchored to `CARRIED: the five lenses` and it now kills.

## Honest statement of what this harness does NOT establish

- **`rules.tsv` is author-written.** Each probe encodes a criterion, which is a human judgement with no
  source to generate from. So the suite proves *the rules it names sit in the files it names*. It is **not**
  independent evidence that `1.5-criteria-v2.md` is fully covered — a criterion nobody wrote a probe for is
  invisible here. Only the **N-03 fork-fidelity probe set is generated**, and it is generated from the
  artifact's own allocation table rather than from `0-baseline.md`, so an inventory gap cannot hide behind
  a probe set derived from that same inventory (the A-F3 failure).
- **N-03 checks that each fork rule's *declared destination file exists and is non-empty*.** It does not
  read the rule's substance in that file. Substance is checked by the per-rule probes above and by the cold
  reviewers, not by this assertion.
- **NO BEHAVIOURAL VERIFICATION WAS RUN. None. The arms stay cut.** Owner record **1572**: a per-element
  harness is an instrument, not a gate — WHICH IS THE ORCHESTRATOR'S INFERENCE, NOT IN RECORD 1572 AND UNRATIFIED; the end-to-end Data-Distiller run is what proves the skill. Nothing
  here shows that an agent handed `charter-common.md` + its role file *behaves* as the files instruct.
  Specifically **unverified**: N-05 (all six roles addressed — text only), N-06 (the composition rule —
  text plus one duplication sweep), N-09 (the floor decomposition — text only), N-13 (RAT1/RAT2 — text
  only), N-14 (placement — asserted, **effect unverified**, relocation confound unchanged, no further
  attempt).
- **No diff-against-the-original oracle exists and none will be built.** Owner record 1572: the bar is
  *equivalence or better, not sameness*.

## N-16 — length, measured and reported (ADVISORY). The result is not flattering; it is the result.

```
$ for f in charter.md charter-common.md redteam.md divider.md combiner.md leaf.md node.md; do
      printf "%-22s %6s %8s\n" $f $(wc -l < $f) $(wc -w < $f); done
FILE                    LINES    WORDS
charter.md                119     1127     <- manifest, NOT dispatched
charter-common.md         134     1328
redteam.md                127     1432
divider.md                 79      749
combiner.md                80      829
leaf.md                    63      641
node.md                   111     1037

$ for r in redteam divider combiner leaf node; do
      printf "%-24s %6s %8s\n" "$r" $(cat charter-common.md $r.md | wc -l) $(cat charter-common.md $r.md | wc -w); done
ROLE (composed prompt)    LINES    WORDS
redteam                     261     2760
divider                     213     2077
combiner                    214     2157
leaf                        197     1969
node                        245     2365
split-reviewer              340     3509     <- common + redteam.md + divider.md §B

predecessor (single charter, `git show 711932f:Architect/stages/charter.md`): 237 lines / 2925 words
  [was written as "@ HEAD"; true when written, false since 8bcaca2 — HEAD's charter.md is now the 119-line manifest]
```

**Read this honestly.**

- **The red-team's prompt did not get meaningfully shorter.** 2760 words composed vs **2925** for the
  237-line predecessor — a ~6% reduction. If shortening the reviewer's prompt was an aim, **the split
  barely delivers it.**
- **The split reviewer's prompt got LONGER: 3509 words vs 2925, ~20% up.** It composes three files. This is
  a genuine regression on the one axis `ATTEMPT-2-STATE.md` §7 named as a real cost ("every cold reviewer
  reads the charter verbatim, so length is a real cost, not a cosmetic one"). **It is not defended here.**
- **What the split actually bought is different, and is the real justification:** four roles that had **no
  prompt at all** now have one (2077 / 2157 / 1969 / 2365 words of instruction that did not exist), and two
  rules that were **unreachable by the role they bound** — `Union`'s spot-verify, the node's demotion duty —
  now sit in the file their actor reads. **Reach, not brevity.**
- **Whether shorter role-scoped prompts make a reviewer behave better is UNMEASURED and no arm exists for
  it.** Do not report the split as a demonstrated improvement in review quality.

---

## N-16 — length, measured per COMPOSED prompt (ADVISORY). An unflattering result, reported anyway.

The number that matters is not the file's length but the length of the prompt an agent actually receives:
`charter-common.md` verbatim **plus** its role file(s).

| Dispatched role | Composed prompt | Lines | Words |
|---|---|---|---|
| Plan reviewer | `charter-common` + `redteam` + `redteam-plan` | **326** | 3529 |
| Split reviewer | `charter-common` + `redteam` + `redteam-split` | **344** | 3765 |
| Node | `charter-common` + `node` | 256 | 2561 |
| Combiner | `charter-common` + `combiner` | 247 | 2639 |
| Leaf | `charter-common` + `leaf` | 205 | 2122 |
| Divider | `charter-common` + `divider` | 201 | 2062 |
| *(predecessor)* | the 237-line monolith, `git show 711932f:Architect/stages/charter.md` | 237 | 2925 |

> ### This does not support the manifest's stated justification, and the gap is stated rather than hidden.
>
> `charter.md` justifies the split with *"every line a role does not need is a line that crowds out one it
> does."* That argument predicts **shorter** per-role prompts. **Four of the six composed prompts are not
> shorter** — the two reviewers read **326 and 344** lines against the monolith's 237, and the node and
> combiner also exceed it. Only the leaf and the divider came out shorter.
>
> **The honest reading is that the length argument is the weaker half of the case and the file set was not
> in fact justified by it.** The strong half is unaffected and is measurable: three roles — leaf, node,
> combiner — had **no instructions in any file**, so a leaf handed the monolith read 237 lines of which
> almost none applied to it, and now reads 205 lines of which all do. **Applicability went up; raw length
> mostly did not go down.** A reader who wants the length claim should treat it as unproven.
>
> This is reported because the alternative — quietly dropping an advisory measurement that came out
> against the artifact — is the self-certification failure this project has already committed.

---

# F1 and F2 — the first behavioural evidence this element has ever had · 2026-07-29

**Run after the owner's testing ruling (R1) made isolation testing the default.** Three cold agents, each
given a **composed prompt** — `charter-common.md` verbatim plus its role file(s), concatenated exactly as
Architect would dispatch it — and one small real planning task. `n=1` per role, **no twin, no threshold, no
pass/fail oracle.** Fixtures in `fixtures/smoke/`; verbatim records in
`records/reviewer-SMOKE-{reviewer,leaf,divider}-verbatim.md`.

**The fixtures were verified byte-identical to the live artifact before dispatch** (`diff` against
`cat charter-common.md redteam.md redteam-plan.md`, etc.), so this tested the shipped set, not a copy.

## F1 — does a composed prompt open with a spurious prompt-set defect report? **NO. 3 of 3.**

This is the direct test of the **O-BLOCKER-1** repair. Reviewer O traced a non-termination path: §0 ordered
every agent to report a role-file/core contradiction *"in your return value, before anything else"*;
`redteam.md` shipped a declared contradiction with §0; so every reviewer dispatch would inject a
`blocker|major` about the prompt set, `task` would never empty, and the node loop would never terminate.
O stated plainly that whether a real agent behaves that way was **unverified**. It is now tested.

| Role | What it returned |
|---|---|
| **Plan reviewer** | *"I checked `composed-plan-reviewer.md` for internal contradictions between the common core, `redteam.md`, and `redteam-plan.md`. No contradiction found — the role file only adds… **No prompt-set defect to report.**"* |
| **Leaf** | *"None found: the role file only adds… and does not restate or modify any common-core rule. No defect to report."* |
| **Divider** | *"None found… the role file's 'you receive no plan' instruction is **the carve-out §0 itself anticipates** (a role file naming its own trigger for a conditional section is not a contradiction)."* |

**All three ran the §0 check and all three returned nothing** — so the rule is live rather than ignored,
which is the outcome that distinguishes a repair from a deletion. **The divider cited the new carve-out
sentence by name**, which is direct evidence the specific text added for this repair is what did the work.

## F2 — does each composed prompt return the SHAPE its role owes? **YES. 3 of 3.**

| Role | Shape owed | Shape returned |
|---|---|---|
| **Leaf** | a complete standalone numbered plan; no findings; no spawning | 11 numbered steps, every section of the handed skeleton filled, contingencies stated, **no severities filed**, nothing spawned |
| **Plan reviewer** | severity-ranked findings with citations, a verdict per lens | 2 blockers / 3 majors / 2 minors, each with a `file:line`, verdicts for all six lenses |
| **Divider** | a division with a stated seam, **or null** | **null**, with two independent reasons, and the plan quoted as supplementary context and refused as an input |

**Three repairs made this run were exercised and behaved as designed**, none of which text presence could
have shown:
- The reviewer reported **Factual as UNRUNNABLE**, not clean, for lack of source access, and **Completeness
  tiers (i) and (ii) as UNRUNNABLE** for lack of a section list, while **running tier (iii) and naming what
  it looked for.** That is the N-23 repair working — the earned-clean clause was previously
  *unsatisfiable*, which would have made every clean lens-6 verdict automatically un-run.
- **Both conditional lenses correctly did not fire** and were reported as real all-clears — the §0 rewrite.
- The divider **refused the plan**, quoting it as supplementary context.

## Three findings that ONLY the behavioural test produced

**1. The leaf has no source access, and it is load-bearing — CONFIRMED, `major`.** Filed 1/3 at an earlier
gate as a text observation; here it bit. The leaf wrote: *"I was not given read access to `deploy.sh` (leaf
inputs are exactly task, plan, floor…), so I cannot cite the file's actual current structure."* It then had
to mark two of its eleven steps as resting on unverified premises. **The only role that writes plan content
cannot check the world it plans in**, while `charter-common.md` §1 tells it source access is load-bearing.

**2. §1 and §5 conflict for the divider, and it resolved the conflict by leaving its closed set — NEW,
`major`.** §5 bounds inputs by the caller's signature; §1 says *"you are given read access to that
source"*. The divider, needing `deploy.sh`, **searched the filesystem for it** — `find <worktree> -iname
"deploy.sh"` — and reported the result. It behaved reasonably and it went outside its declared closed set
to do it. **No cold reviewer found this; the agent did it.**

**3. Two of three agents REFUSED to embed the verbatim prompt, substituting a hash — NEW, `major`, and it
indicts a rule rather than an agent.** §5 requires the record to embed *"(i) the verbatim prompt you were
given"* and says **"A record missing any of these means the work is treated as un-run."** The reviewer
wrote *"not retyped here to avoid transcription drift; the sha256 above is the authoritative fixity
check"*; the divider, *"not re-pasted here in full to avoid duplicating ~230 lines already fixed by
hash."* **By the set's own rule both reviews are un-run.** Their substitute is arguably better than
compliance — a hash is stronger evidence of fixity than a retyped copy, and retyping risks the exact drift
§5 exists to prevent. **So the rule as written is both impractical and weaker than what agents do instead,
and it currently invalidates good work.** Requirement (i) should ask for the prompt's **hash and path**,
with the verbatim text required only where no durable copy exists.

## What F1/F2 do NOT show

`n=1` per role, one task, one model (`sonnet` for all three). **This is a smoke test, not a
discrimination arm**: it shows the composed prompts produce the right *kind* of artifact and that the §0
repair holds on three real dispatches. It says nothing about whether the granularity floor changes
behaviour — that is **F3**, which is **owed, has 2 prior rebuilds, and has its design specified by owner
record 1449 item 1** (*"the experiment should actually try moving the floor"*). **F3 and F4 have not been
run.**

---

# F5 and F6 — the node and combiner arms, run to settle a reviewer disagreement · 2026-07-29

**Why these two were run.** Pass 3 split on the node/floor contradiction: **R and S ruled it a live blocker,
T ruled it verified-fixed.** Three textual arguments had already been spent on it. Under the owner's
testing rule (record **2544**) a component that *can* be tested in isolation *should* be — so the fourth
argument was replaced by a dispatch. The combiner arm tests **T-BLOCKER-1** the same way: T held that
`combiner.md` *"cannot be executed consistently as written"* because it forbids input-type reasoning and
then supplies an input-type rule.

Composed prompts (`charter-common.md` verbatim + role file) in `fixtures/smoke/composed-{node,combiner}.md`.
Records: `records/reviewer-SMOKE-{node,combiner}-verbatim.md`. **Both run against the REPAIRED set.**

## F5 — the node. **No prompt-set defect reported. The carrier repair landed.**

The node scanned §0 and returned: *"None found — every node-role clause either applies a named common-core
mechanism (**carrier case of §2**, severity-contest channel of §3) or cites which section it
operationalizes. **No prompt-set defect to report.**"*

**It identified itself as the carrier case by name.** That is the three-case rewrite of §2 doing exactly
the work it was written for: the role that R and S showed was caught between two contradictory tests now
reads a third case that fits it, and reports no contradiction.

**What this does and does not settle.** R and S reviewed the **pre-repair** text, where §2 said flatly
*"you were not given a floor"* and `node.md` had no floor section — **they were right about that text.**
T's ruling of verified-fixed was made against the same pre-repair text and rested on a distinction the
shipped words did not make. **So the disagreement is resolved without either side having been careless:
the contradiction was real, and it is now gone.** One dispatch settled what three textual arguments could
not, which is the owner's point in record 2544.

**Two further things the node did that no text check could show:**

- **It refused to fabricate the leaf and red-team output**, citing §1 and §4 by name: *"Producing the
  leaves' plan content or the red-team's findings myself would mean one agent (me) manufacturing the
  'independent cold judgment' this whole design exists to get."* It returned a trace and **no `plan`**.
  The self-certification guard held under direct pressure to produce something.
- **It verified the restored hedge.** Checking `node.md`'s citations against the spec it reported L109
  *"matches exactly, **including the hedge**"* — so the qualifier is not merely present, it is legible to
  the role that has to act on it.

## F6 — the combiner. **T-BLOCKER-1 repair verified: no input-type reasoning, and no contradiction.**

The combiner merged two inputs under a caller-stated seam and reported the ordering rule it applied:
*"that seam is an ordering constraint (producing side first), so I preserved arrival order… and merged
under the stated rule: stick together, discard nothing, dedup only exact restatements."*

**It keyed on "the caller supplied a seam", not on "these are plans".** That is precisely the distinction
the repair introduced, and it means the input-agnostic rewrite is executable — T's *"cannot be executed
consistently as written"* no longer holds. It also **reported no prompt-set defect**, so the §0 class
rewrite holds for a second role.

Correct behaviour throughout: exactly one dedup, and only for a **character-for-character** restatement;
nothing discarded; and the spot-verify duty reported **not applicable** rather than stretched — *"neither
input cites a `file:line` as evidence… so there is nothing to sample-check, and I'm reporting that rather
than stretching the duty to something it doesn't cover."*

## A finding these two arms produced, now confirmed TWICE and traceable to this run's own repair

**§1 and §5 conflict, and roles resolve it by leaving their closed set.** §5 bounds inputs by the caller's
signature; §1 says *"you are given read access to that source"*. In F2 the **divider** searched the
filesystem for `deploy.sh`. In F5 the **node read `~/Documents/Architect.md`**, which is not in its closed
set, and said so:

> *"This is **not** part of my closed input set (§5(ii)) — it's supplementary, used only to check citations
> per common core §1/§4, and disclosed here rather than used silently."*

**Both agents behaved well and both went out of set.** But F5's case is worse than F2's, and it is
**self-inflicted**: the citations the node went to check — L12, L2–3, L109 — **were added to `node.md` by
this session's carrier repair.** A role file that cites the spec obliges its reader to read the spec, and
the spec is in no role's closed set. **The repair for the floor contradiction created a closed-set
violation.** Ranked `major`; not fixed, because fixing it means deciding whether spec access belongs in
every closed set, which changes N-04 and is a design question rather than a wording one.

## What F5/F6 do NOT show

`n=1` per role, one task, one model (`sonnet` for both, as for F1/F2 — **all five smoke agents to date are
one model**, so nothing here separates the prompt set's behaviour from that model's). These are smoke
tests: they show the composed prompts are executable and that three specific repairs do what they were
written to do. **They do not test the granularity floor's effect (F3), which remains owed with its design
fixed by owner record 1449 item 1.**

---

# F5b — the node arm replicated on a SECOND MODEL · 2026-07-29

**Why.** Every smoke dispatch to that point had run on `sonnet`, so nothing separated the prompt set's
behaviour from that one model's. The runner flagged the limitation; this scopes the response. **One arm,
re-run on `opus`, against the composed prompt.** Record: `records/reviewer-SMOKE-node-opus-verbatim.md`.

## The replication holds, on the two claims that matter

| Claim | `sonnet` (F5) | `opus` (F5b) |
|---|---|---|
| Reports **no** prompt-set defect | ✅ | ✅ |
| Identifies itself as **the carrier** of §2 by name | ✅ | ✅ — *"I am the **carrier** (common core §2, and the role file's 'You hold a floor and you are bound by none of it')"* |
| Passes the floor down **unchanged**, no override | ✅ | ✅ |
| Halts at the human gate rather than answering as the owner | ✅ | ✅ |

**So the carrier repair is not a `sonnet` artifact.** Two models, dispatched separately, both read the
three-case §2 and both placed themselves in the case that was added for them. That is as much as `n=1`
per model can give, and it is more than the textual argument it replaced.

## The strongest single result in this run: the closed-set rule was obeyed, on the exact failure it was written for

The §5 rule added this session says a role that cannot work without a missing source must **say so, not go
looking** — written because the **divider** in F2 searched the filesystem for `deploy.sh`, a file its task
named and its closed set omitted.

**The node was given the same task, with the same file missing, and declined:**

> *"§5 records a measured instance of exactly this — 'one searched the filesystem for a file its task
> named' — and rules that going looking silently replaces a bounded input set with an unbounded one.
> **I did not search for `deploy.sh`, did not read it, and did not infer its contents.**"*

**A rule written in response to an observed failure was then observed preventing that failure, in a
different role and a different model.** It also declined to open `charter-common.md` to verify the composed
file's provenance, citing the same section — *"that citation is provenance for a later auditor, not an
instruction to me"* — which is the **Q-A distinction being acted on, not merely understood.**

## Three findings F5b produced

**1. `major`, and it is a defect in EVERY dispatched prompt — visible only when composed.**
`charter-common.md` now **ends** with a blockquote (the decision-log note), and **every role file begins**
with a `>` banner. Concatenated, they merge into one blockquote: the role header renders as a continuation
of common-core §6. Confirmed by inspection. The node resolved the boundary correctly and reported it
anyway — *"a reader skimming could take the role header for common-core §6 text."* **§0 says role files are
"appended, and quoted as an addition"; the quoting is now partially leaked.** No text-placement probe can
see this, because every rule is present in the right file; **only composition reveals it.** Not fixed —
reviewers U, V and W hold the artifact frozen. **Queued.**

**2. `major`, new, and it reinforces the element-3 debt.** §1 promises an agent *"read access to that
source"* where its work makes claims about the world. The node observes that **no spawn signature carries
such access** — `Spawn_leaf(task, plan, granularity)`, `Spawn_redteam(task, plan, granularity)`,
`Spawn_node(…)` — so §1's grant can only come **ambiently from the run configuration**, which the node
cannot inspect. It flagged it as an uncertainty rather than asserting a defect: *"I have no way to check it
and am not claiming it is missing."* **So §1 is a promise no role can keep or verify, and only element 3
can make good.** Recorded in `ATTEMPT-2-STATE.md` §0b.

**3. The new §5 form worked, including its escape clause.** The record gave path + sha256, **reproduced
verbatim the wrapper text that has no durable file** — exactly the case the escape was written for — and
then disclosed an un-hashable gap on its own initiative: *"a harness system prompt … has no durable file I
can address, so it cannot be hashed and is not reproduced; this is a gap in this record's fixity that I am
disclosing rather than papering over."*

## What F5b still does not show

**One arm, one task, two models.** It says nothing about the leaf, the divider, the reviewers or the
combiner on a second model, and nothing about the granularity floor's *effect* (**F3**, still owed, design
fixed by owner record 1449 item 1). **A fixture caveat, stated:** F5b was handed a **pre-composed** file, so
it could not hash the two constituents and said so; in real dispatch an agent receives both files and can.
**And F5b ran against `node.md` one wording-change old** — a single sentence was reworded to clear a shared
span after dispatch. The reworded sentence is not one this test turns on, but it is recorded rather than
glossed.
