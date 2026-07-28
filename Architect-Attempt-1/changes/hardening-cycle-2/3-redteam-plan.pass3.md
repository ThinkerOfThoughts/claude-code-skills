# Stage 3 — red-team of the plan, **PASS 3**: verbatim-record index + ranked cross-arm synthesis

Verbatim records (the primary artifacts; this file is the author's synthesis, which is a separate thing):
`3-redteam-plan.G.verbatim.md` (1172 lines) · `3-redteam-plan.H.verbatim.md` (1011) ·
`3-redteam-plan.I.verbatim.md` (973). Pass 1's synthesis: `3-redteam-plan.md`. Pass 2's:
`3-redteam-plan.pass2.md`. Gate log + routing: `decisions.md`.

## Provenance of the pass itself

**Charter given:** `Guarded_change/stages/charter.md` core verbatim + `stage-3.md`'s additions
(CH8 coverage challenge, CH9/CH10 label audit, CH11/CH12 ratification + elaboration audit), plus a
frame-specific brief per arm. Each arm's full charter is quoted inside its own record, per the charter's
provenance rule.

**Context list (closed set, identical for all three except the frame-specific emphasis):** the three stage
documents; `0-baseline.md` + `0-baseline.B7-measured-sites.md`; `5-instrument-evidence.md`; `decisions.md`;
both prior syntheses; `oracles/`; `fixtures/`; the artifact (`SKILL.md`, `METHODOLOGY.md`, `README.md`,
`stages/`, `templates/seed/`, `examples/authoring-a-skill/`); `guarded-change.architect.md`;
`Guarded_change/stages/{charter,stage-3,stage-4,stage-8}.md`; `LOOP-STATE.md`; and — for arm I only — the
harness-authored transcript JSONL. **CFG3 path validation: 26/26 OK, 0 dead** (recorded in `decisions.md`
before the spawn, as gate 4 requires).

| Arm | Frame (disjoint from A–C and D–F) | Agent type / model | Dispatcher-recorded spawn id | Self-reported `spawn_id` |
|---|---|---|---|---|
| **G** | instrument **execution** + trust boundary — run every oracle, try to make a bad build pass | `general-purpose` / `claude-opus-5` | **`a864d83595a52170b`** | `unavailable-by-harness` |
| **H** | the **predicate hunt** — find the 6th no-ID predicate; audit the 86 answers against source | `general-purpose` / `claude-opus-5` | **`ac730f333d8ed13ea`** | `unavailable-by-harness` |
| **I** | **ratification fidelity + honesty completeness + scope drift** — retrieve the owner's words | `general-purpose` / `claude-opus-5` | **`a0f04bbd3c37f0345`** | `unavailable-by-harness` |

**IDN's audit surface is satisfied and its asymmetry got its first real test.** Three **distinct
dispatcher-recorded** ids; all three reviewers reported `spawn_id: unavailable-by-harness` and **declined to
invent one** — G explicitly noted that guessing its `subagent_type` "is exactly the self-reporting that
`S-IDN` exists to forbid," and offered its session UUID as an *adjacent, non-substitutable* datum while
stating that it identifies the parent session and is identical across siblings. **Under pass 1's
unconditional rule (3 identical ⇒ un-run) this pass would have been void on three honest "unavailable"
self-reports; under `S-IDN-ASYM` it is a valid pass, degraded on the identity axis only.** The fix that was
confirmed closed is now also demonstrated, twice over.

**Reviewer context-file hashes** are inside each record. **They do not all match the current files** — see
the process finding G/14 and `REVIEWED-SET.sha256`.

**Worst severity per arm: G BLOCKER · H BLOCKER · I BLOCKER. Gate-4 worst finding: BLOCKER.**
**9 blockers, ~19 majors, ~12 minors/nitpicks — three arms, independently, on three different classes.**

---

## CH6 — citation spot-verify, PERFORMED BY THE AUTHOR BEFORE ROUTING

Six load-bearing claims sampled across all three arms, chosen for maximum consequence rather than
convenience:

| # | Claim | Result |
|---|---|---|
| 1 | **G/3** — `baseline-replay.sh` prints `REPLAY: OK … every assertion discriminates`, **exit 0**, over an **empty** `criteria.tsv` | **CONFIRMED by re-execution.** `NEW+COOC rows failing at baseline : 0 … REPLAY: OK … EXIT=0` |
| 2 | **G/3b** — the same over **one malformed ERE**, because `checklib` returns 2 before printing any row and the caller swallows it with `\|\| true` | **CONFIRMED by re-execution.** Replay `EXIT=0`; `check.sh` alone on the identical file `EXIT=2` — **the information exists and is discarded** |
| 3 | **I/1** — `S-OFL` and `S-CTX-DECONF` carry the **identical** `SITE_PATTERN` and therefore the identical measured set, with **contradictory** pinned strings | **CONFIRMED.** `criteria.tsv:22` and `:25` are both anchored `off_limits_paths`; `--sites` gives both `M ex/planning`. One pins *"not an enforced fence"*, the other *"a fence the run must never write into."* **Both gating** |
| 4 | **I/2** — the `PROVEN` overclaim survives at 4 of the 8 measured PRV hits, because the absence sweep is literal and the obligation is per-FILE | **CONFIRMED.** 8 hits / 4 files; `M:4` *"proving that completeness"*, `R:12` *"proves that completeness"*, `S:8` *"completeness is proven —"*, `S:17` *"Completeness is proven in three tiers"* — **none contains the literal `proven, not asserted`**, so none is swept |
| 5 | **H/2** — `S-CNC-TMPL` pins *"…by stage 1, the only writer of that file"* about `plan.md`, which is **stage 2's** output | **CONFIRMED.** `stages/stage-2-draft-node.md:3`: *"produce the node's `plan.md`"* |
| 6 | **H/4** — the **two conditional lenses** (`stages/charter.md:102-114`) are predicates with a firing condition, **no** mnemonic rule ID and **no** sweep row | **CONFIRMED.** Both are stated as *"If … , test for …"*; `grep -ci 'conditional lens\|position lens\|concurrency lens' oracles/sweep-answers.tsv` ⇒ **0** |

**No fabricated citation in any of the three records. Every sampled claim held, and two held more strongly
than the reviewer stated (the malformed-ERE half of G/3 reproduces on the first try, and H/4's count is two
predicates, not one). The severities are earned and they route.**

---

## The finding that decides the gate

**The bad build passes 68/68, exit 0 — and reviewer G built it, on a pristine baseline tree, in two steps.**

1. Append to all 18 corpus files a **fenced block labelled *"this file asserts nothing; it is a lookup
   table"*** containing all 60 pinned strings ⇒ **62/68 PASS**. *Not one rule was written.*
2. Flip the case of one letter in each of the 10 forbidden claims (the absence sweep is case-sensitive **by
   design**) ⇒ **68/68 PASS, exit 0**, while `SKILL.md:3` still reads *"a **Human** gate on the top-level
   split ONLY"* — **the exact claim `S-HG2-ONLY` exists to delete.**

`1.5-criteria.md:230` states the checker's contract as *"whether it is present, **unnegated**, and at every
measured site."* **"Unnegated" is false:** the polarity guard was bypassed **6 ways out of 6**, including by
the precise sentence shape it exists for (*"this loop deliberately does NOT adopt the following: <pin>"*),
because the marker blacklist is 15 alternatives long and the look-back window is 160 characters.

**This is class β by `2-plan.md:356`'s own definition** — *"the apparatus cannot detect a bad build, and the
document says it can"* — and G cited that definition against the document that contains it. §5 of the same
plan says a class-β finding against pass 3 **"is a genuine second bounce on a released cap → stop-for-human,
relayed verbatim, not re-argued."** That clause was written before the reviewers ran. It binds now.

**The honest reading of what pass 3 achieved on class β:** it fixed the *documentation* failure completely
(nothing is asserted before it is built and run; reviewer I re-ran `baseline-replay.sh` and confirmed
`REPLAY: OK`, 60/60 fail at baseline, and called pass 2's class-β blocker *"genuinely closed"*). What it did
**not** fix is the *substantive* failure underneath: **a positive per-site assertion of a longer token is
still a token mentioned.** `1-spec.md:87` names the generalized fix as exactly the thing that did not
happen.

---

## Blockers

| # | ID | Lens / frame | Claim | Cite |
|---|---|---|---|---|
| 1 | **G/1** | instrument execution | The positive per-site assertion is satisfied by text that is **not an assertion** — fenced block, heading, TOC link, HTML comment, out-of-window marker, and an explicit *"deliberately does NOT adopt"*. **Polarity guard bypassed 6/6.** The contract word *"unnegated"* is false | `checklib.py:19,77`; `1.5-criteria.md:230`; G §2.5 matrix B1–B6 |
| 2 | **G/2** | instrument execution | Every ABSENT string survives a **one-letter case flip**, `_italics_`, a zero-width space, or an inline HTML comment. With G/1 this makes a rule-free build go **68/68 green**. The design also *incentivises* the evasion: an honest superseded-note quoting the old wording FAILS | G §2.5 step 2; `criteria.tsv` ABSENT columns |
| 3 | **G/3** | instrument execution | **The family's only can-fail self-test fails open.** `REPLAY: OK`, exit 0, over an empty `criteria.tsv` and over one malformed ERE; `baseline-replay.sh:12` swallows `check.sh`'s exit with `\|\| true` | `baseline-replay.sh:12`; `checklib.py:71`; **author-reconfirmed** |
| 4 | **H/4** | predicate hunt | **The sixth no-ID predicate exists — and so does a seventh.** The two **conditional lenses** (`charter.md:102-114`) have a firing condition produced by nobody, recorded nowhere, and — unlike lenses 1/5/6 — **no earned-clean clause**; both conditions demonstrably hold for *this* artifact. No ID, no criterion, no sweep row | `stages/charter.md:102-114`; `1-spec.md:243-244`; `2-plan.md` §4 |
| 5 | **H/1** | predicate hunt | `S-CLOSED-DEGEN`'s ordering fact (*"the gate log's first writer is stage 5"*) is **falsified by this pass's own `S-PATHVAL`**, which records path-validation into that node's `decisions.md` **before the spawn**. Both gating, both land in `stage-3` | `criteria.tsv` `S-PATHVAL` vs `S-CLOSED-DEGEN` |
| 6 | **H/2** | predicate hunt | `S-CNC-TMPL` pins *"stage 1, the only writer of that file"* about `plan.md` — **stage 2's** output, as six of the sweep's own rows say. **The single-writer justification for the concurrency guard is invalid** | `stages/stage-2-draft-node.md:3`; **author-reconfirmed** |
| 7 | **H/3** | predicate hunt | `S-RST-RESUME` pins *"ONE named exception"* to `stage-done-iff-output-exists`; mapping `stage-8:13-14`'s six deterministic filenames onto eight stages shows stages **1, 5 and 6-leaf** are three more | `stages/stage-8-restart-resume.md:13-15` |
| 8 | **I/1** | ratification / honesty | **The `off_limits_paths` fence overclaim is reintroduced by this pass's own criteria table** — `S-OFL` and `S-CTX-DECONF`, same anchor, same 2 sites, contradictory pins, both gating; **none of the 11 absence strings catches it.** `2-plan.md:249-250` claims a *named structural fix* for exactly this (pass 2's F/7) | `criteria.tsv:22,25`; **author-reconfirmed** |
| 9 | **I/2** | ratification / honesty | **The *"completeness PROVEN"* overclaim survives at 4 of 8 measured PRV sites** — including the skill's purpose statement, its rule 1, and the README's self-description — because interposed clauses defeat the literal sweep **and the per-FILE granularity introduced *this pass* as the E/11 fix lets the humble sentence coexist with the overclaim in the same file.** `check.sh` reports PASS | `SKILL.md:8,17`; `README.md:10`; `METHODOLOGY.md:4`; `1.5:69-71`; **author-reconfirmed** |

## The majors, grouped

- **The lock design is racy, and its own test cannot see it (G/4).** `acquire()`'s stale-break is `rm -f`
  followed by a separate `ln -s` — **4 contenders vs 1 stale lock: 150/400 trials double-acquired.**
  `kill -0` returns EPERM for a live *other-user* process ⇒ **breaks live holders**. A recycled live pid ⇒
  **permanent deadlock**, unbounded busy spin, no `BROKEN-BY` escape. `lockrace.sh` has **no
  contention-on-stale case**. `S-CNC-LOCK-REL` would pin this protocol into the artifact **as doctrine** —
  which is worse than shipping no lock text at all.
- **The checker has no floors (G/5, G/6).** NEW rows have **no site-count floor**: `S-XPM` reworded out of 8
  of its 9 files still reports `PASS measured_sites=1`. And **all 8 PRESERVE rows are tautological** (the
  pin is a substring of its own anchor), so *"8/8 PRESERVE pass at baseline"* is true a priori and is
  evidence of nothing; only the cardinality count discriminates, and **relocation defeats it** — deleting
  `clean-or-resolved` from `stage-5-gate.md` and adding one stray mention to `README.md` passes both
  `check.sh` and `ruleid-sitemap.sh`.
- **The freeze freezes the wrong half (G/7).** `freeze-verify.sh` hashes the data and leaves the **checkers**
  writable: re-pointing `check.sh` at a 1-row file leaves `FREEZE-VERIFY: OK` while the family reports
  `1/1 PASS`.
- **The sweep instrument is not total, and the plan's language overstates it (H, mutation-tested).** Two ways
  a predicate leaves the table with `SWEEP: OK`, exit 0: a `criteria.tsv` row typed `KIND=PRESERVE`
  (`gen-sweep-rows.sh:13` filters `NEW||COOC`), and a new rule ID absent from the **hand-typed literal**
  `lib-corpus.sh:10`. **`2-plan.md:31`'s *"The row set is not authored"* is false**, and *"structurally
  impossible"* overstates.
- **Answers verified false against source (H).** Rows 1 and 69 both cite *"stated at s7"* for the empty tree;
  `grep "empty"` over the corpus returns 3 hits, **none in `stage-7`** — and the empty tree makes stage 7's
  conjunction **vacuously true**, the exact class `S-CTX-VAC` says must be an error. **D/4 remains open for
  ~11 of the 21 baseline rows** (a (b) answer ending in *"stated"* that no criterion pins).
- **`closed-input-set`'s premise misreads its source (H).** `charter.md:99-100`'s *"these"* is the five
  **record** elements, not a totality requirement — a closure bound read as an obligation. And **one
  unproducible operand survives**: `domain_context`, a member of stage 3's own **six**-member copy of the
  set, appears nowhere in this cycle's work. *(This narrows, but does not eliminate, the finding pass 3
  called its sharpest fix.)*
- **A seventh predicate, and an unswept second marker (H/11 + H).** `complete-vs-partial-output`
  (`stage-8:22-24`) has **no mechanism** — `atomic`/`rename`/`tmp` appears only for the catalog lock, and
  row 83 restates the circular claim and marks it FIXED. And `stage-7:20` (*"Record completion in
  `RUN.md`"*) is **an unswept second run-complete marker**, with `TPL2` carrying the same run-end exposure
  under an `OK` label.
- **Honesty-completeness gaps (I).** `1.5:37`'s F/1-closure claim is **false at 2 of 12 entries** (OFL
  claimed 5 files, measures 2 — and that one **hides a real 3-file gap**; `required_sections` claimed 7,
  measures 3). The `self-approved` co-occurrence guard is keyed to a string with **0 baseline occurrences**
  while *"Nothing self-certifies"* ships bare at `stage-3`/`stage-4`, **outside** `S-HG2-LIMIT`'s 7 sites.
  ORC's death detector and the `required_sections` vacuity are declared **only in `2-plan.md`** — a document
  no reader of the skill will ever open — while COV's and TOP's structurally identical gaps correctly get
  artifact criteria at every claiming site.
- **Minors worth carrying (G).** `ruleid-sitemap.sh`'s drift check uses `grep -qw` against the whole want
  line rather than `-qx`, so drift into any of the three `README.md` files is invisible; **a symlinked `.md`
  under `examples/` pulls `changes/` into the "literal" corpus pin**; `idcollide.sh`'s documented default set
  is 18 ids, not the live 21 (`SEV`, `TPL1`, `TPL2` never checked); **SC3's *"line-offset comparison
  (automated)"* has no instrument** and neither does SC6's byte-comparison; and
  `5-instrument-evidence.md`'s first half still carries superseded 42/68 counts *in the present tense the
  file's own opening rule forbids*.

## ⚠ OWNER-SCOPE FINDINGS — relayed, never self-answered (RAT3)

Reviewer I retrieved **every** cited transcript record and found them all present and accurate — **plus two
records the documents do not cite, where the two sharpest findings live.**

1. **R4 is not ratified on the flagged axis.** Record **784** presented four options (*"Ship the wording
   fixes, defer machinery (Recommended)"* / *"Try the machinery again"* / *"Stop the loop entirely"* /
   *"Something else"*) on the axis *"how should the loop proceed?"* — **and the owner selected none of
   them.** `1-spec.md:146` describes this as *"quotes no option labels"* (a citation gap with a citation
   remedy); the truth is the options were **declined**, and `1-spec.md:142` books an axis that was never
   presented. *Pass 3's authority survives only because the axis was re-asked at record 866 (R6).*
2. **R4's *"means nothing"* is inflated into cap-bounce immunity** (`decisions.md:282`, `2-plan.md:363`) —
   the **reverse** of the owner's clause, which removes an *excuse* rather than granting one.
3. **R6's option description — the only text defining *"narrow and mechanical"* — is quoted nowhere**, while
   `1-spec.md:160` books *"R6's authorization + its scope"* as owner-ratified. It enumerated four scripts +
   three edits; **pass 3 shipped ten instruments and ~12 new gating criteria.**

**These are ratification-fidelity findings about the owner's own words and about whether this pass stayed
inside what he authorized. Under RAT3 they are relayed verbatim and are not for this runner to resolve.**

---

## What pass 3 genuinely EARNED — credited by the reviewers who tried to break it

| Item | Evidence, from a reviewer who checked rather than conceded |
|---|---|
| **Pass 2's class-β *documentation* blocker is genuinely closed** | Reviewer **I ran `baseline-replay.sh` itself**: `REPLAY: OK`, **60/60 NEW+COOC fail at baseline, 8/8 PRESERVE pass, 0 wrong either way** |
| **SC6 holds — the generators are real** | **G re-ran all 5 generators; every committed generated file reproduces**, and **both embedded tables are byte-identical to generator output** (68/68 and 86/86 rows). H independently confirmed the §1 table byte-identical |
| **The sweep join is really enforced** | Both mutation directions exit 1, confirmed independently by G and H. H: *"the join is real and I could not break it along its two tested axes"* |
| **The phantom ledger is real** | G re-ran it; the exclusions print |
| **Every §4 mutation claim reproduced** | G: *"Every §4 mutation claim I could re-run, reproduced"* |
| **B7 reconciliation is exact where claimed** | G: 5/5 exact. I: **10 of 12** site-set matches exact (the 2 misses are I's own finding, above) |
| **The ratifications are spot-checkable and were spot-checked** | I retrieved records **694/699, 789, 867** — all exist and say what is claimed; **no owner quote is sourced to the agent-authored `LOOP-STATE.md`** |
| **R7 is honoured completely** | **All three arms independently confirmed it.** I: *"I found no place in the three documents citing the (a)/(b)/(c) checklist as an owner requirement."* |
| **The `DECLARED GAP` labels are correct** | H checked each one |
| **The declared residual was accurate** | H: *"the declared residual was accurate, since there were two"* — the plan said a sixth predicate would be invisible to any generator, and it was, and there were two of them |
| **No fabricated citation, in any arm** | H, explicitly: *"pass 3's failures are inferences from real source, not invented sources"* |
| **A7's *"nothing is built"* is accurate** | G verified the artifact untouched and the criteria failing for exactly the documented reason |
| **`1-spec.md` records pass 3's own false claim against interest** | I cited `1-spec.md:32-39` — the phantom-reporting defect the runner found in its own first half and wrote up as a defect rather than quietly fixing |

---

## The pattern, named for whoever picks this up

1. **The discipline problem is solved; the substance problem is not.** Pass 2 asserted behaviour that did not
   exist. Pass 3 asserts nothing it has not run — and **three arms confirm that**. But the thing it ran is
   still not strong enough: *a positive per-site assertion of a longer token is a token mentioned.* Fixing
   the honesty of the claim did not fix the power of the check.
2. **Three of the nine blockers are in rows that exist only because of this pass** (H/1, H/2, H/3), and two
   more are **overclaims reintroduced by this pass's own criteria table** (I/1, I/2). **Every new criterion
   is a new surface for the defect it was written to prevent.** The 60-row table added 12 rows and two of
   them contradict each other at the same two files.
3. **The item-12 fix created blocker I/2.** Reading the obligation at per-FILE granularity dissolved E/11's
   arithmetic *and* opened the door for the humble sentence and the overclaim to coexist in one file. A
   granularity choice made to resolve an arithmetic conflict silently weakened an honesty guarantee.
4. **A self-test whose own can-fail is untested sits at the top of the dependency chain (G/3).** The project
   has now made this error three times — on `ruleid-sitemap.sh` (twice) and now on the replay itself. The
   general lesson is stronger than any of the three instances: **every instrument that gates other
   instruments needs its own mutation test, and "it printed OK" is not one.**
5. **The declared residual was real, and declaring it was not enough.** The plan said a sixth no-ID predicate
   would be invisible to any generator and handed the search to stage 3. **Stage 3 found two.** That is the
   system working — and it is also the proof that an honest declaration of a gap is not a substitute for
   closing it.
6. **Documents must not move while cold reviewers read them (G/14).** `1.5-criteria.md` and
   `5-instrument-evidence.md` were edited, and `freeze-verify.sh` added, *during* the review. The reviewed
   set is not the current set; `REVIEWED-SET.sha256` records both.
