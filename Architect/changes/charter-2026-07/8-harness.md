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
