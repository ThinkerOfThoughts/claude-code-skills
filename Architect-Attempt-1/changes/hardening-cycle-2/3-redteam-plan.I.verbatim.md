# Cold red-team record — REVIEWER I (FRAME I: ratification fidelity · honesty completeness · scope drift)

**Verdict: BLOCKER.** Two blockers, seven majors, four minors, one nitpick. The pass earned a great deal
(§8 is specific about it), and the ratification record for R1/R2/R3/R6/R7 is genuinely spot-checkable — I
retrieved every one. But the defect class this pass exists to close (*a limitation stated at some sites and
not others*) is **live in the pass's own criteria table**, in two places, and in one of them the pass's own
pinned strings require the artifact to state the overclaim and its refutation in the same two files.

---

## 1. Provenance

### 1(i) This charter, quoted

> You are a COLD RED-TEAM REVIEWER. You have no shared context with the author of the artifacts you are
> reviewing, and you must not acquire any. Do not read any other reviewer's record. Work only from the paths
> listed below.
>
> **FRAME I — RATIFICATION FIDELITY, HONESTY COMPLETENESS, AND SCOPE DRIFT. You are auditing whether the
> documents tell the truth about their own authority and their own limits.**
>
> **1. AUDIT THE OWNER RATIFICATIONS AS ARTIFACTS (CH11/RAT1, CH12/RAT2).** The documents rest on seven
> recorded owner rulings, R1–R7. A valid ratification record cites (i) the flagged axis and the options
> presented, **verbatim**; (ii) the owner's response, **verbatim, with a durable source the author did not
> author** so the quote is spot-checkable; (iii) a mapping showing those words select the recorded option *on
> the flagged axis*.
> - **Spot-verify the quotes against the named source.** … **Go fetch them.** Does each cited record exist?
>   Does it say what is claimed? Are the option labels really present? A re-typed "verbatim" with no
>   verifiable locus is **unverified**.
> - **Note the asymmetry the documents themselves admit** — that R4's record quotes no option labels, and that
>   R6 was *relayed* to the author rather than independently fetched. Is that honesty sufficient, or does it
>   undercut something load-bearing?
> - **A ruling built on a partial or adjacent owner answer that does not disambiguate the presented options is
>   NOT ratified** — the axis must be re-asked, not defaulted, and especially not resolved into the author's
>   own recommended option. Check for that.
> - **UNRATIFIED INFLATION (CH12):** where the documents expand a ratified option into detailed commitments,
>   do the load-bearing operative terms (a mechanism, an "only/every/never", a division of responsibility)
>   trace to the owner's actual words? Anything that does not is unratified inflation and is untrusted.
> - **⚠ R7 SPECIFICALLY.** The owner ruled that the three-question **(a)/(b)/(c)** sweep checklist derived from
>   R4 **"Keep it as a proposal for now"** — so it is an **ORCHESTRATOR PROPOSAL, not an owner requirement**,
>   and R4's ratified content is the owner's **one sentence only**. The documents claim to label it as a
>   proposal wherever it appears. **Verify that claim at every occurrence.** Any place it is cited as something
>   the owner requires is a finding.
>
> **2. AUDIT HONESTY COMPLETENESS — is each subtractive/limiting claim made at EVERY site, or only where it was
> convenient?** … `off_limits_paths` … `PRV` … `HG2` / *"never self-approved"* … **"N same-model instances are
> not N independent minds"** … Are the **DECLARED GAPS** honest declarations, or are they abandonment dressed
> as disclosure? … For each: is it declared **at the site a reader would need it**, or only buried in a plan
> document nobody reading the skill will see?
>
> **3. AUDIT SCOPE AND THE ITERATION-CAP ACCOUNTING.** … **Is that accounting legitimate, or is it constructed
> so that inconvenient findings cannot count?** Look hard at any clause that makes a class of finding
> un-countable. Separately: does anything in scope drift beyond what the owner ratified — new mechanism
> smuggled in as a "fix", or a scope addition presented as subtractive?
>
> **4. FIDELITY TO THE PRIOR REVIEWS.** … is the finding actually closed, closed-in-appearance-only, or quietly
> reclassified? Pay particular attention to any place a previous **blocker** is now described as something
> smaller.
>
> **SEVERITY MODEL** — Blocker (wrong problem / will not work / unverifiable as planned) · Major (sound goal,
> materially wrong approach) · Minor (real but local) · Nitpick (style/clarity).
>
> **EVIDENCE DISCIPLINE (enforced)** — **Every factual claim carries a citation you actually verified** …
> **A clean verdict must be EARNED.** … Distinguish observation from inference.
>
> **CONTEXT** — 1. `LOOP-STATE.md` … **This file is AGENT-AUTHORED and is therefore NOT an admissible
> ratification locus** — the transcript is. Treat any citation of this file as the source of an owner quote as a
> finding. 2. the **harness-authored** session transcript: the admissible locus. … **harness-injected
> task-notifications ALSO appear as `type:"user"` entries** …
>
> **SCOPE — do not report these as defects; they are DECLARED out of scope by owner ruling:** F1 …, F2, F5's
> mechanism, DIV, the cost/fan-out envelope, ECON's O(children²), the "two passes" ruling. **F8 … IS ratified
> IN scope.** … But a *dishonest declaration* about an out-of-scope item is fully in scope for you.

### 1(ii) Exact list of paths I read

Artifacts under review:
- `Architect/changes/hardening-cycle-2/1-spec.md`
- `Architect/changes/hardening-cycle-2/1.5-criteria.md`
- `Architect/changes/hardening-cycle-2/2-plan.md`
- `Architect/changes/hardening-cycle-2/decisions.md` (targeted: lines 163–330, 400–480, plus greps)
- `Architect/changes/hardening-cycle-2/oracles/criteria.tsv`

Instruments and measurement files (read and, where noted, **executed**):
- `oracles/checklib.py` (read in full) · `oracles/check.sh` · `oracles/baseline-replay.sh` (**executed**)
- `oracles/gen-sweep-table.sh` (targeted) · `oracles/sweep-answers.tsv` (header + greps)
- `Architect/changes/hardening-cycle-2/0-baseline.B7-measured-sites.md`
- `Architect/changes/hardening-cycle-2/5-instrument-evidence.md` (targeted grep only)

Context (closed set):
- `/home/zero/architect-hardening-loop/LOOP-STATE.md` (targeted: R1–R7 sections, lines 13–228, 276–286)
- `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`
  — **targeted extraction of records 694, 699, 784, 789, 866, 867** (JSON-parsed, not grepped)
- `Architect/SKILL.md`, `Architect/METHODOLOGY.md`, `Architect/README.md`,
  `Architect/stages/{charter,stage-1-frame-template-match,stage-3-completeness-critic,stage-4-adversarial-redteam}.md`
  — targeted line reads + corpus-wide greps over `SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/`
- `Architect/changes/hardening-cycle-2/3-redteam-plan.pass2.md` (in full)
- `Architect/changes/hardening-cycle-2/3-redteam-plan.md` (targeted greps: A/F4, B/L16, PRV, OFL, DIV)
- `Guarded_change/stages/stage-3.md` lines 26–95 (CH8–CH12 + CP1/RAT1)
- `Guarded_change/stages/charter.md` (grep only, to locate CH8–CH12)

**I did not read** `3-redteam-plan.{A,B,C,D,E,F}.verbatim.md` (other reviewers' records — charter-prohibited),
nor any superseded `*.v1-/*.v2-superseded.*` file except as quoted inside the live documents.

### 1(iii) Agent type + model

- **Model:** `claude-opus-5` (Opus 5), as reported by the harness.
- **Agent type:** a subagent launched via the parent's `Agent` tool. **The harness did not disclose my
  `subagent_type` to me**, so I report it as `unavailable-by-harness` rather than guessing. Tool surface
  available: full (read/write/bash/etc.).

### 1(iv) `sha256sum` as I read them

```
a9d3cef738408ddcc0033b3ca3e7fb8c036c542dfac8f398bfe2be165e6bd49f  1-spec.md
cd9a217e72ee7b56c9c159f45c3c9cd04a4583e955df54c4ed9c1a1fd025d8c7  1.5-criteria.md
6a7048ab2858356586a76d86aef87687035175fa891d7bf01aa01751bb042d41  2-plan.md
```

Artifact state confirmed as declared: `git log --oneline -3` ⇒ `b08f5a9 architect: cycle-1 hardening
records — gate-4 cap tripped, artifact unchanged`; `git diff --stat HEAD` ⇒ only
`Architect/guarded-change.architect.md | 11 ++++++++---`. **`1-spec.md:264-266`'s claim that the artifact set
is unedited at `b08f5a9` and that `guarded-change.architect.md` was corrected by the orchestrator is TRUE.**

### 1(v) spawn_id

`spawn_id: unavailable-by-harness`

### 1(vi) LOOP-STATE citation discipline — checked, CLEAN

The charter directs me to treat any citation of the agent-authored `LOOP-STATE.md` as the source of an owner
quote as a finding. `grep -n 'LOOP-STATE' 1-spec.md 1.5-criteria.md 2-plan.md` returns exactly two hits, both
in `1-spec.md`, and **neither cites it for an owner quote**:

- `1-spec.md:154` — cites LOOP-STATE for LOOP-STATE's *own* hedge ("calls the broad reading … an
  *'Interpretation … stated so Roy can correct it.'*").
- `1-spec.md:165` — cites it for a *status* ("recorded in `LOOP-STATE.md` as **never closed**").

Every owner quote in the three documents is sourced to the transcript with a record number. **This is a real
correction of pass 2's F/3 defect and it is earned.**

---

## 2. RATIFICATION AUDIT (CH11)

Method: I parsed the six relevant JSONL records with `python3 json.loads` and printed the full
`message.content` blocks. **All quoted owner words and option labels below were retrieved from the
harness-authored transcript, not from the documents.**

### R1 — SEV4 tie-break — **VERIFIED, VALID**

- **Locus of options:** record **694**, `type:"assistant"`, `tool_use id=toolu_01Ga2368vabihTBcFVBZEYte`,
  `name=AskUserQuestion`, `timestamp 2026-07-25T14:03:05.318Z`. ✔ exists, ✔ as cited in `1-spec.md:133-134`.
- **Flagged axis, verbatim:** *"SEV4 tie-break — the iteration cap tripped at gate 4 (2 bounces, same class).
  The loop stops until you break the tie. Which way?"*
- **Options presented, verbatim labels:** `"Accept risk — ship narrower (Recommended)"` ·
  `"Change the goal"` · `"Kill the change"`.
- **Owner's response, verbatim:** record **699**, `type:"user"`, `tool_result` keyed to
  `toolu_01Ga2368vabihTBcFVBZEYte`, `toolUseResult` keys `['questions','answers']`,
  `timestamp 2026-07-25T14:10:24.209Z` — *"…Which way?"=`"Accept risk — ship narrower (Recommended)"`*.
- **Mapping:** the words are a presented option label, byte-identical, on the flagged axis. ✔
- **Genuine-owner-turn test:** an `AskUserQuestion` `tool_result` with `toolUseResult.answers` — form (i).
  Not a harness notification. ✔
- **`1-spec.md:139` records it verbatim and correctly.**

### R2 — F8 / assembly human gate — **VERIFIED, VALID**

- **Locus:** same records 694 / 699, question 2.
- **Flagged axis, verbatim:** *"F8 (queued since last night, never touched): should a human review the
  *assembled* plan, not just the top-level split? It ADDS a human gate, so it's your call — and it gets
  pricier to retrofit as bottom-up assembly lands."*
- **Options, verbatim labels:** `"Yes — human reviews the assembled plan"` · `"No — keep the top-split gate
  only"` · `"Decide it in cycle 2's spec"`.
- **Owner's response, verbatim:** `"Yes — human reviews the assembled plan"`.
- **Mapping:** exact option label on the flagged axis. ✔ **F8 is ratified in scope**, as my charter states.
- **`1-spec.md:140` correct**, including its label "(**scope addition**)" — which the option's own description
  supports (*"Adds a second human gate at the end"*).

### R3 — loop-exit semantics — **VERIFIED, VALID**

- **Locus:** same records 694 / 699, question 3.
- **Flagged axis, verbatim:** *"My narrowing of your \"until nothing surfaces\" — I made it a continue-only
  trigger so a minors-only cycle can't silently end the loop. Confirm or correct?"*
- **Options, verbatim labels:** `"Confirm — minors don't auto-terminate (Recommended)"` ·
  `"Blocker/major only is fine"` · `"Literal — loop until truly nothing surfaces"`.
- **Owner's response, verbatim:** `"Literal — loop until truly nothing surfaces"`.
- **Mapping:** exact option label; and note the owner **declined the (Recommended) option**. ✔
- **`1-spec.md:141` correct.**

### R4 — **VERIFIED AS TO THE QUOTE; NOT A RATIFICATION ON THE FLAGGED AXIS. See finding I/3.**

- **Locus of options:** record **784**, `tool_use id=toolu_01R11yeNtGRvicasDVg9czYo`, `AskUserQuestion`,
  `timestamp 2026-07-25T15:25:17.056Z`. **The options DO exist and ARE retrievable.**
- **Flagged axis, verbatim:** *"Given all that — how should the loop proceed?"* (`header: "Next step"`).
- **Options presented, verbatim labels — retrieved, and quoted nowhere in the documents:**
  `"Ship the wording fixes, defer machinery (Recommended)"` · `"Try the machinery again (third attempt)"` ·
  `"Stop the loop entirely"` · `"Something else — let me think out loud"`.
- **Owner's response, verbatim:** record **789**, `tool_result` keyed to `toolu_01R11yeNtGRvicasDVg9czYo`,
  `timestamp 2026-07-25T15:29:03.822Z`, content begins *"The user answered:"* —
  > *"if its the same kind of problem that was encountered/fixed in a different section, then the fix that was
  > applied in that other section should be applied here; that it didn't catch it in the current section in the
  > previous round means nothing."*
  This is **byte-identical** to `1-spec.md:49-51`. The quote is genuine and the locus is correct. ✔
- **Mapping — FAILS.** The answer selects **none of the four presented options**. It is free text on an
  adjacent axis (*what principle governs a recurring class*), not on the flagged axis (*how should the loop
  proceed*). Under CH11 that is a **partial/adjacent answer that does not disambiguate the presented options**
  ⇒ **not ratified on the flagged axis; the axis had to be re-asked.**
- **What the documents say about this:** `1-spec.md:146-148` — *"**R4's record does not meet the bar R1–R3
  meet** (F/3): it quotes no option labels and originally cited an agent-authored file."* That is a
  **misdescription of the deficiency** (finding I/3): the options are not missing, they were *declined*.
  And `1-spec.md:142` books R4's axis as *"recurrence of a class in a new section"* — **an axis that was never
  presented**.
- **Mitigating, and I credit it:** the "how should the loop proceed" axis *was* eventually re-asked, at record
  866/867 (R6). So pass 3's authority does not rest on the non-answer.

### R5 — **NOT AUDITABLE AS RECORDED: absent from the RAT1 table entirely**

My charter states the documents rest on **seven** rulings R1–R7. `1-spec.md:137-144`'s RAT1 table has **six
rows: R1, R2, R3, R4, R6, R7. R5 is not in it.** R5 is nonetheless *used*: `1-spec.md:66` (*"its fate is
decided in the R5 spin-off chat"*) and `1-spec.md:208` (*"the owner's R5 directive … [is a] plain free-text
user turn"*, cited as measured evidence against pass 2's discriminator).

`LOOP-STATE.md:131-135` records R5 as an owner ruling sourced to *"harness-authored session transcript (same
file as R1–R4), as a **plain owner turn** (free text, not an `AskUserQuestion` result)"* with the owner's words
*"you're correct, if this works, spin off a dedicated chat to add the rule to guarded-change; then pause…"* —
but **LOOP-STATE gives no record number for R5**, and `LOOP-STATE.md` is the inadmissible locus. I therefore
report R5 as **UNVERIFIED**: I did not attempt a full-transcript free-text search for it, because the
documents under review give me no locus to spot-check and R5 governs no operative commitment in them (its
precondition is declared unmet at `LOOP-STATE.md:225-227`). *Observation, not inference:* the omission is
consistent with R5 being genuinely inert this cycle; but a RAT1 table that silently drops one of seven rulings
is an incomplete record. Recorded as **I/15 (nitpick)** rather than inflated.

### R6 — **VERIFIED, VALID as to label and selection; scope text withheld. See finding I/5.**

- **Locus of options:** record **866**, `tool_use id=toolu_01UToKNMx5K1itQdsxtmydbK`, `AskUserQuestion`,
  `timestamp 2026-07-25T16:20:42.593Z`.
- **Flagged axis, verbatim:** *"The cap tripped again — this time on the runner self-certifying unbuilt scripts
  (verified). How should cycle 2 end?"*
- **Options, verbatim labels:** `"Ship the text-only subset (Recommended)"` ·
  `"Authorize pass 3 — narrow and mechanical"` · `"Kill cycle 2"`.
- **Owner's response, verbatim:** record **867**, `tool_result` keyed to the same `tool_use_id`,
  `timestamp 2026-07-25T16:23:35.570Z` — `"Authorize pass 3 — narrow and mechanical"`.
- **Mapping:** exact option label on the flagged axis. ✔ And `1-spec.md:143`'s claim that *"the owner
  **declined** the orchestrator's recommendation"* is **TRUE** — the `(Recommended)` marker is on
  `"Ship the text-only subset"`, and its description even says *"Runner recommends this too, independently."*
  That is a correctly and honestly recorded ruling.
- **The gap:** the option's **description** — the only text that defines what "narrow and mechanical" meant to
  the owner — is quoted **nowhere** in the three documents. Retrieved verbatim:
  > *"The remaining work is enumerable: write four scripts (~100 lines), delete two entries from one line,
  > GENERATE the site columns from the measurement files instead of typing them, reconcile the cluster map —
  > and build the instruments BEFORE stage 3 so no claim about them can be self-certified. Risk: third attempt
  > at apparatus, and this is your ruling that a self-certification bounce doesn't end the cycle."*
  `1-spec.md:160` books "R6's pass-3 authorization **+ its scope**" as Owner-ratified while withholding the
  scope text. See **I/5**.

### R7 — **VERIFIED, VALID. Substance honoured throughout. Provenance label incomplete (I/10).**

- **Locus:** records **866 / 867**, question 2 of the same `AskUserQuestion`.
- **Flagged axis, verbatim:** *"My R4 write-up turned your one sentence into a three-question sweep checklist
  (is the operand produced by a provably earlier step? is it defined at the degenerate case? does every acquire
  have a named release?). Your sentence didn't say that. Does the checklist stand?"* (`header: "R4 scope"`).
- **Options, verbatim labels:** `"Checklist stands — ratify it"` · `"Narrow back to my words"` ·
  `"Keep it as a proposal for now"`.
- **Owner's response, verbatim:** `"Keep it as a proposal for now"`.
- **Mapping:** exact option label on the flagged axis; the option's own description confirms the reading —
  *"Leave it flagged as an orchestrator proposal; decide when the rule is authored properly in the dedicated
  guarded-change chat, where it'll get its own red-team."* ✔ **`1-spec.md:59-61` and `:144` are correct.**
- **R7 LABEL COMPLIANCE — I checked every occurrence, as instructed. The claim HOLDS.** The (a)/(b)/(c)
  framing appears at: `1-spec.md:63-68` (labelled), `1-spec.md:83` ("the same (b)+(c) shape" — labelled 20
  lines above), `1-spec.md:161` (labelled: *"the (a)/(b)/(c) sweep framing, which R7 leaves a proposal"*),
  `2-plan.md:14-19` (labelled, immediately above §1), `2-plan.md:77` + the 86 generated rows (governed by the
  §0 label in the same document), `1.5-criteria.md:15-18` (labelled), `decisions.md:322`, `decisions.md:454-456`.
  **I found no place in the three documents where the checklist is cited as something the owner requires.**
  Every citation of R4 as authority (`2-plan.md:141` *"per R4"*, `:196`, `:361`, `:363`; `1-spec.md:74`) cites
  the **one sentence**, not the checklist. **F/4 is genuinely closed.** The only unlabelled occurrences are at
  the instrument layer (`oracles/gen-sweep-table.sh:28`, `oracles/sweep-answers.tsv:1`) — logged as a
  coverage-challenge item, not a finding, since `1-spec.md:63` scopes the claim to "THIS CYCLE'S DOCUMENTS".

### Ratification audit — plain summary

| Ruling | Options retrieved? | Owner's words retrieved? | Mapping holds? | Verdict |
|---|---|---|---|---|
| **R1** | ✔ record 694 | ✔ record 699 | ✔ exact label, flagged axis | **VERIFIED VALID** |
| **R2** | ✔ record 694 | ✔ record 699 | ✔ exact label, flagged axis | **VERIFIED VALID** |
| **R3** | ✔ record 694 | ✔ record 699 | ✔ exact label, flagged axis | **VERIFIED VALID** |
| **R4** | ✔ record 784 (**not quoted by the documents**) | ✔ record 789, byte-exact | ✘ **selects no option; adjacent axis** | **NOT RATIFIED ON THE FLAGGED AXIS (I/3)** |
| **R5** | ✘ no locus given | ✘ | — | **UNVERIFIED — absent from the RAT1 table (I/15)** |
| **R6** | ✔ record 866 (label only quoted; **scope description withheld**) | ✔ record 867 | ✔ exact label, flagged axis | **VERIFIED VALID; scope claim uncheckable (I/5)** |
| **R7** | ✔ record 866 | ✔ record 867 | ✔ exact label, flagged axis | **VERIFIED VALID; substance honoured** |

**Five of seven rulings are genuinely spot-checkable and I checked them.** That is the strongest thing in
these documents and §8 credits it properly.

---

## 3. ELABORATION AUDIT (CH12 / RAT2)

Method: for each ratified phrase, I list its **operative terms** (as retrieved from the transcript), then the
documents' expansion, then whether the expansion adds an operative commitment not present in or entailed by
the phrase.

### R4 — ratified phrase and its operative terms

Owner's words (record 789). Operative terms, exhaustively:
1. **antecedent** — "the same kind of problem that was encountered/fixed in a different section";
2. **prescription** — "the fix that was applied in that other section should be applied here";
3. **discount** — "that it didn't catch it in the current section in the previous round **means nothing**".

| Documents' expansion | Traces to? | Verdict |
|---|---|---|
| *"the remedy is to **apply the fix that already worked, generalized across the class**"* (`1-spec.md:55-56`) | terms 1+2 | **traces — clean** |
| *"it is **evidence the earlier fix was applied too narrowly**"* (`1-spec.md:55`) | entailed by 1+2 | **traces — clean** |
| *"neither a fresh discovery nor a repeat failure"* (`1-spec.md:54`) | term 3, in part | **partly traces**; the *"repeat failure"* half is where I/4 begins |
| *"Under R4 those are **under-generalization, not cap bounces**"* (`decisions.md:282`); *"would be under-generalization under R4"* (`2-plan.md:363`) | **NOTHING.** "bounce", "cap", "count" appear nowhere in the owner's words, and term 3 removes an *excuse* rather than granting one | **UNRATIFIED INFLATION — I/4 (major)** |
| the three-question (a)/(b)/(c) checklist | nothing — and **R7 says so** | **correctly labelled a proposal everywhere. Clean.** |
| *"no mutation may be labelled 'class (i), computed not stored'"* (`2-plan.md:21-24`) | nothing — **and the document says so**: *"One rule inside the framing that pass 1 lacked, and it is **this runner's own**"* | **clean — honestly attributed** |

### R2 — ratified phrase and its operative terms

Owner's words: `"Yes — human reviews the assembled plan"`. Option description (record 694), which under CH12
supplies "the ratified option's stated meaning": *"Adds a second human gate at the end. Directly addresses the
finding that the founding failure WAS caught by a human, yet no human sees anything below the top split. Costs
a gate and requires the assembly fix to preserve a whole-plan reader."*

Operative terms: **a second human gate**, **at the end**, on **the assembled plan**, and **preserve a
whole-plan reader**.

| Documents' expansion | Traces to? | Verdict |
|---|---|---|
| `S-HG2` — a human reads the presentable plan and approves or bounces before the run is done | "second human gate at the end" | **traces** |
| `S-HG2-FWD` — any future bottom-up assembly must preserve a whole-assembled-plan reader | **verbatim in the option description** | **traces — clean, and well done** |
| `S-HG2-ONLY` — the decomposition gate fires at top level only; HG2 is separate | entailed (a *second* gate implies the first is not it) | **traces** |
| `S-HG2-DEGEN` — HG2 applies to whichever artifact is presentable (single-leaf ⇒ `tree/root/plan.md`) | **not in the option**; a degenerate-case extension | **not flagged in the documents, but harmless: it *widens* the gate's reach rather than narrowing it. Nitpick-level at most; I do not raise it.** |
| the **bounce mechanics** (which nodes reopen at stage 2) | nothing | **CORRECTLY LABELLED.** `S-HG2-AUTHORED` pins *"how an HG2 bounce routes is this cycle's own authoring choice and not part of the ratified decision"* at 3 measured sites. **This is exemplary RAT2 discipline and I credit it in §8.** |

### R6 — ratified phrase and its operative terms

Operative terms, from the option description retrieved at record 866: **four scripts (~100 lines)** · **delete
two entries from one line** · **generate the site columns from the measurement files** · **reconcile the
cluster map** · **build the instruments BEFORE stage 3**.

The documents deliver all five — and materially more (see **I/5**). The added items are an "only/every/never"
class of commitment (twelve new *gating* criteria, a redesigned lock mechanism, two new checker guards) which
under CH12 must trace to the ratified phrase. They trace to **R1's** frame, not R6's; the documents assert that
bridge at `1-spec.md:7-8` (*"It keeps pass 2's **scope** (owner-ratified)"*) **as fact rather than as the
interpretation it is** — and withhold the text a reader would use to test it.

### R1 — ratified phrase and its operative terms

Operative terms, from the option description retrieved at record 694: *"Cycle 2 ships **only** the
confirmed-closed fixes (BIND over gate artifacts, ID renames, RES, redteam_context, §4 heading, seed slots,
elc, DEP, CNC, root pin); F1/F2/F5's mechanisms defer to a later cycle."*

The operative words are **"only"** and the ten-item parenthetical. `1-spec.md:161` **honestly** concedes that
`IDN`, `SPV`, `IGM`, `TPL3`, `XPM`, `PRV`, `OFL` are *"the in-scope items **not in R1's parenthetical list**"*
and labels them orchestrator calls. **That is correct RAT2 practice.** But `1-spec.md:173` then heads the
wider set *"the confirmed-closed set"* — R1's own operative phrase — and the word **"only"** is quoted nowhere
in the spec. See **I/12**.

---

## 4. HONESTY-COMPLETENESS TABLE

**Method note (important):** the "sites it appears at" column is **measured**, not read off the table. I ran
`oracles/check.sh /…/Architect --sites` against the live (unedited) tree and used its output, and I
independently grepped the pinned corpus (`SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/`).
I also read `oracles/checklib.py` in full to establish what the mechanism can and cannot see.

| Limiting claim | Sites it MUST appear at (measured) | Sites the mechanism puts it at (measured) | Can the mechanism be evaded? |
|---|---|---|---|
| **`off_limits_paths` is a prompt-level convention, not an enforced fence** | B7 P5: **13 hits in 5 files** — `METHODOLOGY.md`, `SKILL.md`, `examples/…/planning.md`, `examples/…/README.md`, `stages/stage-1-frame-template-match.md` | **`S-OFL` measures 2**: `METHODOLOGY.md`, `examples/…/planning.md`. Absence sweep = the single literal `Naming is the fence` (1 baseline hit, `METHODOLOGY.md:100`) | **YES — and it already is.** The unqualified fence claim survives at `stages/stage-1-frame-template-match.md:42` (*"off-limits paths … are read-only context **the run never writes into**"*), `examples/…/README.md:20`, `SKILL.md:48/50/87`. **Worse: `S-CTX-DECONF` REQUIRES the overclaim to be written back into both S-OFL sites (I/1, blocker).** |
| **PRV — soften "completeness PROVEN" to what is actually proven** | B7 P6: **8 hits in 4 files** — `METHODOLOGY.md:4,40` · `README.md:10,12` · `SKILL.md:3,8,17` · `stages/stage-7-assemble.md:26` | `S-PRV` pins the humble sentence **per FILE** at `M R S s7` (4 ✔ matches B7's file set). Absence sweep = `PROVEN` \| `proven, not asserted`, **case-sensitive** (verified in `checklib.py`) | **YES.** The sweep catches only `SKILL.md:3`, `METHODOLOGY.md:40`, `stage-7:26`. **`SKILL.md:8`, `SKILL.md:17`, `README.md:10`, `README.md:12-13` all survive** — the interposed clause / parenthetical defeats `proven, not asserted`, and per-FILE satisfaction lets the humble sentence coexist with the overclaim in the same file (**I/2, blocker**). |
| **PRV positive half must ship with its limitation at the same site** | wherever the positive is asserted | `S-PRV-LIMIT` welds positive + limitation into **one pinned string**, at `M S ch s3` (4, measured) | **NO — this half is sound.** Because the two halves are one sentence they cannot be separated. `S-PRV`'s own string (`"…It does not certify its absence"`) is self-limiting. **F/8's structural half is genuinely closed. Credited.** |
| **"N same-model instances are not N independent minds"** | the tier/contract sites | **stated plainly and unhedged**, verbatim in `S-PRV-LIMIT`'s pinned string, at 4 measured sites (`M S ch s3`) | **NO. This is stated plainly, not hedged. Earned.** The *adjacent* claim about frame diversity is overstated in prose — see **I/11 (minor)**. |
| **HG2 — "never self-approved" is a duty, not a property** | every site asserting the property | `S-HG2-LIMIT` at **7 measured** sites (`M S s5 s6 s7 s8 tp/decomp`); `S-HG2-NOSELF` (COOC, `PAT=self-approved`) | **PARTLY.** The positional half is **strong**: `S-HG2`'s 5 sites (`M S s5 s7 s8`) ⊆ `S-HG2-LIMIT`'s 7, so no HG2 rule statement lacks the qualification. **But the COOC guard is keyed to `self-approved`, which occurs 0 times in the artifact**, while the same property claim ships unqualified as *"Nothing self-certifies"* at `stage-3:48`, `stage-3:50`, `stage-4:48` — **`s3`/`s4` are outside `S-HG2-LIMIT`'s set** (**I/8, major**). |
| **DECLARED GAP — `COV`'s seam-union half has no producer** | every site claiming total coverage | `S-COV-LIMIT` at **4 measured** sites (`M S s6 s7`) = exactly the sites matching `Total coverage\|every node gated clean` | **NO. Declared at every site a reader needs it, in the artifact. EARNED — this is the model.** |
| **DECLARED GAP — `TOP` remains defeatable** | every topgate site | `S-F5-LIMIT` at **6 measured** sites (`M S s1 s6 s8 tp/decomp`) | **NO. EARNED — the model again.** |
| **DECLARED GAP — `ORC` has no sub-orchestrator death detector** | wherever orchestration completeness is asserted | **NOWHERE IN THE ARTIFACT.** No row in `criteria.tsv` mentions death / killed / abort / sub-orchestrator (verified by grep). Declared only at `2-plan.md:87` row 9 | **N/A — there is no mechanism.** Declared in a cycle record no skill reader will open ⇒ **abandonment dressed as disclosure (I/6, major)**. |
| **DECLARED GAP — empty `required_sections` makes CMP tier (ii) vacuous** | wherever tier (ii) is described | **NOWHERE IN THE ARTIFACT.** No `criteria.tsv` row states it; `S-SLOT` pins only the slot heading. Declared only at `2-plan.md:83` row 5 | **N/A — no mechanism. Same finding (I/6).** |
| **DECLARED GAP — `run end` has no timeout** | the files that perform / describe the HG2 ask | `S-RUNEND` at **2 measured** sites (`M s8`) | **Declared in the artifact ✔, but not at `s5`/`s7`, which is where the ask happens** (`S-HG2` = `M S s5 s7 s8`) ⇒ **I/13 (minor)**. |
| **`off_limits_paths` overclaim must not be *reintroduced* by another edit (F/7)** | corpus-wide | claimed mechanism: `2-plan.md:249-250` *"the absence sweep is corpus-wide, so a row that re-adds it fails the whole family"* | **THE MECHANISM IS 11 LITERAL STRINGS.** I enumerated every absence string in `criteria.tsv` and programmatically confirmed **none** matches `S-CTX-DECONF`'s reintroduction. **The claimed structural fix does not cover the actual reintroduction (I/1, blocker).** |
| **"declared deferral" route must not exist** | everywhere | verified: the phrase occurs 4× across the three documents, **all four as prohibitions** (`1-spec.md:187`, `:240`, `1.5:50`, `2-plan.md:367`) | **NO. Clean and earned.** |

---

## 5. FINDINGS (ranked)

### I/1 — **BLOCKER** — The `off_limits_paths` fence overclaim is reintroduced by this pass's own criteria table, at the same two shared sites F/7 named, and the mechanism claimed to prevent it cannot see it.

**Citation (all verified by me):**
```
$ awk -F'\t' '$1=="S-OFL"||$1=="S-CTX-DECONF"' oracles/criteria.tsv
S-CTX-DECONF  NEW  off_limits_paths  redteam_context is citable source every cold agent must read;
                                     off_limits_paths is a fence the run must never write into;
                                     a path may be both                                    ABS=(empty)
S-OFL         NEW  off_limits_paths  off_limits_paths is a prompt-level convention, not an enforced
                                     fence: nothing here intercepts a write, and nothing catches a
                                     stray write to a path the config never declared   ABS=Naming is the fence

$ oracles/check.sh /…/Architect --sites | grep -E 'S-(OFL|CTX-DECONF)'
S-CTX-DECONF   NEW   2   M ex/planning
S-OFL          NEW   2   M ex/planning
```
Both rows carry the **identical** `SITE_PATTERN` (`off_limits_paths`) and therefore the **identical measured
site set** `{METHODOLOGY.md, examples/authoring-a-skill/planning.md}`. Both are **gating**
(`1.5-criteria.md:80` *"Every row is gating"*; rows 13 and 16 of the §1 table). So the build is **required**
to write, into those same two files, both:

- *"off_limits_paths is a prompt-level convention, **not an enforced fence**…"* (S-OFL), and
- *"off_limits_paths is **a fence the run must never write into**…"* (S-CTX-DECONF).

I programmatically checked every absence string in `criteria.tsv` against S-CTX-DECONF's normalized pinned
string: **`NO — nothing catches it`**. The 11 absence strings are `at most 2 rebinds`, `three identical
spawn_id values means the pass is un-run`, `Naming is the fence`, `PROVEN`, `proven, not asserted`, `whoever
consumes the review checks`, `no single global cursor to stale-edit`, `a child . 0.8. the parent trips the
guard`, `Outputs & artifacts WITH their locations`, `Outputs & their locations`, `its existence is the .run
complete. marker`, `human gate on the top-level split ONLY`, `grep -rln -- <ID> SKILL.md METHODOLOGY.md
stages/`.

**Why it matters.** F/7 was a pass-2 **major**: *"the `off_limits_paths` overclaim is deleted by row 19 and
**reintroduced** by row 17 at two shared sites"* (`3-redteam-plan.pass2.md:88-89`). `2-plan.md:249-250` claims
a **named structural fix** for exactly this: *"**D5a (F/7):** the overclaim must not be *reintroduced* by
another edit — the absence sweep is corpus-wide, so a row that re-adds it fails the whole family, **which is
the structural fix for pass 2's delete-then-re-add**."* The defect is reproduced **verbatim in shape**: two
rows, one deleting and one re-adding, at the same two shared sites — and the named fix is a literal-string
sweep that does not enumerate the re-added phrasing. `1.5-criteria.md:228-231` honestly warns that `check.sh`
"is not a semantic oracle" and that "the stage-3 reviewers are the guard on meaning" — **this finding is that
declared gap being exercised on the pass's own flagship subtractive item.** This is unverifiable-as-planned:
every oracle will report OK while the artifact contradicts itself.

**Note on the possible defence.** One could argue `S-CTX-DECONF` states the *config author's duty* ("a fence
the run must never write into" as an instruction) while `S-OFL` states the *mechanism's limit*. If so, the two
sentences need reconciling wording — but as pinned they are flatly contradictory on the word **"fence"**,
which is the exact word `S-OFL` exists to negate, and `S-OFL`'s own absence sweep targets a *different*
sentence containing that same word. The fix is to reword `S-CTX-DECONF`'s pinned string (e.g. "…a path the run
is instructed never to write into…") and to widen the absence sweep beyond one literal.

### I/2 — **BLOCKER** — The "completeness PROVEN" overclaim survives at 4 of the 8 measured PRV sites — including the skill's purpose statement and the README's one-line self-description — and the per-FILE granularity introduced *this pass* is what lets it.

**Citation.** B7's own measurement (`0-baseline.B7-measured-sites.md`, section `## P6 completeness overclaim
(PRV)`) ⇒ `count: 8 hits in 4 files`:
```
METHODOLOGY.md:4 · METHODOLOGY.md:40 · README.md:10 · README.md:12
SKILL.md:3 · SKILL.md:8 · SKILL.md:17 · stages/stage-7-assemble.md:26
```
Mechanism (`oracles/criteria.tsv:26`): `S-PRV` pins *"the gate raises the cost of shipping a hole. It does not
certify its absence"*, sites `M R S s7` (4 — I verified this matches B7's file set exactly), absence sweep
`PROVEN|proven, not asserted`. I verified in `checklib.py` that the absence comparison is **case-sensitive**
(`if norm(a) in texts[f]`, and `texts[f]` is never lowercased, unlike the pinned-string path which does
`t.lower().find(pin)`).

What the sweep catches (verified by grep over the pinned corpus): `SKILL.md:3` (uppercase `PROVEN`),
`METHODOLOGY.md:40`, `stage-7:26`. **What survives:**
```
SKILL.md:8   "no plan reaches "presentable" until its completeness is **proven** —
              by a contract-floor plus independent cold critics — **not asserted.**"
              ← the interposed clause defeats the literal `proven, not asserted`
SKILL.md:17  "**Completeness is proven in three tiers, and the third is the point (CMP).**"
README.md:10 "| **architect** | **plans** | **completeness proven (contract + cold critics), not asserted** |"
              ← the parenthetical defeats the literal
README.md:12 "**proves that completeness before the plan is presentable**"
```
And `1.5-criteria.md:69-71` establishes, **as this pass's own fix for E/11**, that *"The obligation is per
FILE, not per line. A row whose SITES set contains `S` is satisfied by the pinned string appearing **anywhere
in `SKILL.md`**."* So `S-PRV` is satisfied at `SKILL.md` by one humble sentence while lines 8 and 17 keep the
overclaim, and at `README.md` while line 10 keeps it.

**Why it matters.** `1-spec.md:184-187` states the goal as *"`PRV` (soften *"completeness PROVEN"* to **what is
actually proven***…)". `1.5-criteria.md:298-301` says both false description clauses *"are removed by
**corpus-wide absence sweeps**"*. Net effect after a fully passing build: the skill's **purpose statement**
(`SKILL.md:8`), its **rule 1** (`SKILL.md:17`) and the **README's sibling-table one-liner** (`README.md:10`) all
still assert completeness is *proven* — the three lines a reader meets first. `check.sh` reports PASS. This is
the F/2 defect (limitation at some sites, bare claim at others) recurring in the pass's second flagship
subtractive item, and the causal agent is a *fix introduced this pass*: the per-FILE reading converted a
per-occurrence deletion duty into a per-file mention duty. Unverifiable as planned.

**Fix direction (not required of me, offered because it is cheap):** make PRV's obligation per-*occurrence* for
the deletion half (an absence sweep over `\bproven\b` scoped to the completeness context, or an explicit
per-line site list from B7 P6), rather than resting the deletion on two literal strings.

### I/3 — **MAJOR** — R4 is not a ratification on the axis that was flagged: options *were* presented and the owner selected **none**; and the documents misdescribe the deficiency as a missing citation.

**Citation.** Retrieved record **784** (`toolu_01R11yeNtGRvicasDVg9czYo`, `2026-07-25T15:25:17.056Z`), axis
*"Given all that — how should the loop proceed?"*, four options with verbatim labels `"Ship the wording fixes,
defer machinery (Recommended)"` / `"Try the machinery again (third attempt)"` / `"Stop the loop entirely"` /
`"Something else — let me think out loud"`. Record **789**'s `tool_result` content begins *"The user
answered:"* and carries the free-text sentence — **selecting none of the four**.

`1-spec.md:146-148`: *"**R4's record does not meet the bar R1–R3 meet** (F/3): it **quotes no option labels**
and originally cited an agent-authored file. Its locus is now pinned to transcript record **789** and it is
spot-checkable — but the asymmetry is recorded, not argued away."*

**Why it matters.** The stated deficiency ("quotes no option labels") is a *citation* problem with a *citation*
remedy — and the documents apply that remedy and declare the asymmetry recorded. The actual deficiency is
categorically different and worse: **the options exist, are retrievable at record 784, and the owner declined
all of them.** Under CH11 that is *"a ruling built on a partial or adjacent owner answer that does not
disambiguate the presented options"* ⇒ **not ratified; the axis must be re-asked.** Compounding it,
`1-spec.md:142` books R4's axis as *"recurrence of a class in a new section"* — **an axis never presented to
the owner**; it is the axis restated to fit the answer, which is precisely the move CH11 exists to catch.
The honesty label is present but it names the wrong defect, so a reader who trusts it concludes the record is
now sound when the mapping still fails.

**What is NOT wrong here, stated fairly:** the *quote* is byte-exact and the locus is correct — I verified
both. And the "how should the loop proceed" axis **was** re-asked at record 866 (R6), so pass 3's authority
does not depend on the non-answer. The finding is about the RAT1 record's truthfulness, not about pass 3's
right to exist.

### I/4 — **MAJOR** — R4's sentence is inflated into a cap-immunity rule that runs *opposite* to the owner's words.

**Citation.** Owner (record 789): *"…that it didn't catch it in the current section in the previous round
**means nothing**."* Documents:
- `decisions.md:282-283` — *"D/1, D/3, D/5, D/6, D/18 are class α … **in sections newly swept for the first
  time**. Under R4 those are **under-generalization, not cap bounces**"*
- `2-plan.md:363` — *"**A class-α finding in a section pass 3 has NOT swept** would be under-generalization
  under R4"*

**Why it matters.** The owner's clause **removes an excuse**: the previous round's failure to catch it carries
no weight, so don't discount the finding. The documents convert it into an **exemption from bounce-counting** —
i.e. into the very excuse the sentence denies. The words *bounce*, *cap*, and *count* appear nowhere in the
owner's answer. Under CH12 a *"division of responsibility"* over what does and does not count at a gate is an
operative commitment, and this one is **not present in or entailed by** the ratified phrase ⇒ **unratified
inflation, untrusted until the owner confirms it.** This is the single ratified sentence whose expansion most
directly benefits the author, which is why it needs the tightest reading.

**Credit where due, and it is real:** `decisions.md:284-286` volunteers, against interest, *"but note that the
sweep instrument itself was incomplete (**15 of 21 baseline IDs had no row**), so R4's corollary was **not
actually executed**. That is the honest reading and it is recorded rather than argued."* That is exactly right.
The problem is that `2-plan.md` §5 now asserts the sweep *was* executed, which makes the immunity **live** for
pass 3 without the owner ever having granted it.

### I/5 — **MAJOR** — R6's ratified option *description* — the only text that defines "narrow and mechanical" — is quoted nowhere, and pass 3's content materially exceeds it while `1-spec.md` asserts the scope claim as fact.

**Citation.** Retrieved from record **866**, the selected option's description in full:
> *"The remaining work is enumerable: **write four scripts (~100 lines), delete two entries from one line,
> GENERATE the site columns from the measurement files instead of typing them, reconcile the cluster map** —
> and build the instruments BEFORE stage 3 so no claim about them can be self-certified. Risk: third attempt at
> apparatus, and this is your ruling that a self-certification bounce doesn't end the cycle."*

The documents quote only the **label**: `1-spec.md:143` *"Authorize pass 3 — narrow and mechanical"*.
`1-spec.md:160` books *"R6's pass-3 authorization **+ its scope**"* as **Owner-ratified**. `1-spec.md:7-8`
states flatly: *"Pass 3 is authorized by **owner ruling R6** and is scoped *'narrow and mechanical.'* It keeps
pass 2's **scope** (owner-ratified) and its confirmed-good core."*

**What pass 3 actually delivered** (`ls oracles/`, verified): `checklib.py` + `check.sh`, `baseline-replay.sh`,
`gen-expected-sites.sh`, `gen-preserve-counts.sh`, `gen-sweep-rows.sh`, `gen-sweep-table.sh`,
`gen-criteria-table.sh`, `ere-probe.py`, `lockrace.sh`, `freeze-verify.sh`, plus a redesigned catalog lock
(atomic symlink + pid + self-breaking), a new **polarity guard**, a new **vacuous-site guard**, a **phantom
ledger**, and ~12 new **gating** criteria closing D/1, D/3, D/6, D/12, F/2, F/7, F/10, F/15, F/17, A/F6.

**Why it matters.** "Four scripts, delete two entries, generate the columns, reconcile the cluster map" is an
*enumeration*. Reading it as illustrative-within-R1's-scope rather than limiting is a legitimate interpretive
position — but it **is** an interpretation, it is the one that expands the author's mandate, and
`1-spec.md:7-8` presents it as fact. Contrast §2.1, which correctly labels the *other* interpretive calls
("Orchestrator call, within the ratified frame"). Worse, the reader cannot test the claim at all, because the
defining text is withheld: the RAT1 record quotes the option **label** for R6 (as it does for R1/R2/R3/R7) but
R6 is the one ruling whose *scope* is asserted to be ratified, and scope lives in the description. **The
ratification record is constructed so the scope claim cannot be checked from it.** Fix: quote R6's option
description in §2 and relabel the delta as an orchestrator call in §2.1, exactly as `PRV`/`OFL`/`IDN` already
are.

### I/6 — **MAJOR** — Two DECLARED GAPS are declared **only in a planning document**; no criterion puts them in the artifact — while two structurally identical gaps *do* get artifact criteria.

**Citation.** Verified by `grep -n -iE 'death|killed|abort|sub-orchestrator|required_sections|vacuous|ORC'
oracles/criteria.tsv` — **no row asserts either gap.** (The hits returned are `S-OFL`, `S-CNC-DECL`,
`S-CNC-INDEX`, `S-CNC-LOCK-REL`, `S-RUNEND`, `S-TPL3`, `S-SLOT`, `S-HG2-LIMIT`, `S-HG2-NOSELF` — none of them
about ORC's death detector or `required_sections` vacuity.)

- **ORC's missing sub-orchestrator death detector** — declared at `2-plan.md:87` row 9: *"PARTIAL+DECLARED — the
  missing death detector is F6's killed-node marker + run-level abort, deferred by R1 and **named here**."*
- **Empty `required_sections` makes CMP tier (ii) vacuous** — declared at `2-plan.md:83` row 5: *"DECLARED GAP —
  the class is named (config-key vacuity), the fix is S-CTX-VAC's, and applying it to required_sections is NEW
  MECHANISM outside R1's ratified scope. **Declared, not fixed**."*

**The contrast that makes this a finding.** The two structurally identical gaps *do* get artifact-level
criteria, measured at every claiming site (I ran `--sites`):
```
S-COV-LIMIT   NEW   4   M S s6 s7      ← COV's seam-union gap, at every "total coverage" site
S-F5-LIMIT    NEW   6   M S s1 s6 s8 tp/decomp  ← TOP still defeatable, at every topgate site
```
**Why it matters.** *"Named here"* means named in `2-plan.md`, a cycle-2 change record. A reader of the shipped
skill — the person who will run a decomposed plan with sub-orchestrators, or configure an empty
`required_sections` — learns neither fact. Under my charter's test (*declared at the site a reader would need
it, or only buried in a plan document nobody reading the skill will see*), these two are **abandonment dressed
as disclosure**. And the disparity is itself an R4 violation *inside the pass R4's remedy was executed in*: the
proven fix (`S-COV-LIMIT` / `S-F5-LIMIT` — state the gap in the artifact at every measured claiming site) was
applied to two members of the class and not to the other two. Note the fix costs nothing new: both gaps can be
*stated* without building any mechanism, which is exactly what `S-COV-LIMIT` and `S-F5-LIMIT` do while their
mechanisms stay deferred.

### I/7 — **MAJOR** — The `1.5` row that reports **F/1 closed** makes a false measurement claim at 2 of its 12 entries — and the OFL one conceals a real 3-file honesty gap.

**Citation.** `1.5-criteria.md:37`: *"where B7 measured the same class the **file set matches B7 exactly**: PRV
4 files, XPM 9, HG2-ONLY 4, `index.md` 5, gate log 9, catalog 3, SPN 6, SPV 1, CTX 4, **OFL 5**, IGM 3,
**`required_sections` 7**"*.

Measured (`oracles/check.sh /…/Architect --sites`) vs B7 (`awk '/^## P/{h=$0} /^count:/{print h" -> "$0}'`):

| Entry | B7 | criterion's measured sites | match? |
|---|---|---|---|
| PRV 4 | `P6 → 8 hits in 4 files` | `S-PRV 4` | ✔ |
| XPM 9 | `P11+P12 → 14 hits in 9 files` | `S-XPM 9` | ✔ |
| HG2-ONLY 4 | `P12 → 7 hits in 4 files` | `S-HG2-ONLY 4` | ✔ |
| index.md 5 | `P9a → 11 hits in 5 files` | `S-CNC-INDEX 5` | ✔ |
| gate log 9 | `P9b → 18 hits in 9 files` | `S-CNC-GATELOG 9` | ✔ |
| catalog 3 | `P15 → 8 hits in 3 files` | `S-CNC-* 3` | ✔ |
| SPN 6 | `P18 → 7 hits in 6 files` | `S-SPN 6` | ✔ |
| SPV 1 | `P7 → 3 hits in 1 files` | `S-SPV 1` | ✔ |
| CTX 4 | `P4 → 6 hits in 4 files` | `S-CTX 4` | ✔ |
| IGM 3 | `P13 → 4 hits in 3 files` | `S-IGM 3` | ✔ |
| **OFL 5** | `P5 → 13 hits in 5 files` | **`S-OFL 2`** (`M ex/planning`) | **✘** |
| **required_sections 7** | `P14 → 15 hits in 7 files` | **`S-SLOT 3`** (`tp/decomp tp/generic tp/leaf`) | **✘** |

**Why it matters.** F/1 was a pass-2 **blocker**: *"The 'measured' site sets are not the measurement"*
(`3-redteam-plan.pass2.md:65`). The row that closes it asserts an exact match and delivers it for **10 of 12**
entries — genuine, substantial work — but the two that fail are asserted with **B7's number, not the
criterion's**, which is the precise error shape F/1 named. For `required_sections` the 3-file set is the
*intended* design (`2-plan.md:300`, anchor `Seed skeleton…` "which measures exactly those three files"), so
only the honesty claim is false. **For OFL the gap is substantive:** the fence overclaim lives at 3 files
`S-OFL` cannot reach — `stages/stage-1-frame-template-match.md:42` (*"off-limits paths (the target repo,
protected paths) are read-only context **the run never writes into**"*), `examples/authoring-a-skill/README.md:20`,
and `SKILL.md:48/50/87` — with no absence sweep covering that phrasing. So the honest description does **not**
ship everywhere the claim appears, in the item `1-spec.md:167` calls *"genuinely subtractive"* and
`1-spec.md:184` calls *"stop claiming `off_limits_paths` is an enforced fence."*

### I/8 — **MAJOR** — The "never self-approved" co-occurrence guard is keyed to a phrase the artifact never uses, while the same property claim ships unqualified at two files outside the limitation's site set.

**Citation.**
```
$ awk -F'\t' '$1=="S-HG2-NOSELF"' oracles/criteria.tsv
S-HG2-NOSELF  COOC  self-approved  never self-approved is a duty this loop states and not a property
                                   its mechanism enforces

$ grep -rniE 'self-approv|self approv|approves its own|self-certif' SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/
stages/stage-4-adversarial-redteam.md:48:**Nothing self-certifies / review records are verbatim / paths are validated (charter).**
stages/stage-3-completeness-critic.md:48:**Nothing self-certifies.** The node's author never approves it; the review is by cold agents with no
stages/stage-3-completeness-critic.md:50:root plan** — and does not self-certify (COV).
METHODOLOGY.md:177:  The top orchestrator dispatches the cold agents on the root; it does **not** self-certify.

$ oracles/check.sh /…/Architect --sites | grep S-HG2-LIMIT
S-HG2-LIMIT   NEW   7   M S s5 s6 s7 s8 tp/decomp        ← s3 and s4 are NOT in the set
```
`self-approv` occurs **0 times** in the artifact — as `1.5-criteria.md:38` itself states. So the COOC guard
governs a string that does not exist; post-build it can only match the files `S-HG2-LIMIT` already wrote.

**Why it matters.** `1-spec.md:111-112` claims *"**The honest position is taken, plainly, and everywhere:** the
approval record is written by an agent, so *never self-approved* is a **duty this loop states, not a property
its mechanism enforces**"* and `1.5-criteria.md:291-294` claims `S-HG2-NOSELF` *"makes the seam
**un-evadable**."* Both claims are true **of the string `self-approved`** and false **of the claim**: the
identical property assertion ships unqualified at `stage-3:48`, `stage-3:50` and `stage-4:48`, none of which
any criterion reaches. "Everywhere" is measured over the wrong surface.

**The defence, and why it fails.** One could argue *"Nothing self-certifies"* is a *different* claim, enforced
by GBP/PASS1's requirement of three cold-agent records. But the pass's own `S-IDN-ASYM` pins *"three identical
self-reports, **including three unavailable**, never make a pass un-run"* (`criteria.tsv`, row 7), and pass 2's
three reviewers **all** self-reported `spawn_id: unavailable` (`3-redteam-plan.pass2.md:10`: *"All three
self-reported `spawn_id: unavailable` and declined to invent one"*). By the documents' own rule, cold-agent
identity is **not** mechanism-verified in the degenerate case that is the actual operating case. So *"Nothing
self-certifies"* is a duty on identical footing to *"never self-approved"* — and it ships bare.

**Positive note that belongs here:** the *positional* half of the HG2 mechanism is genuinely strong.
`S-HG2` / `S-HG2-DEGEN` / `S-HG2-MARKER` each measure `M S s5 s7 s8` (5) and `S-HG2-LIMIT` measures a
**superset** (7). So **no HG2 rule statement can ship without the qualification.** That part of item 10 is
earned, and F/2's headline defect (2 of 4 sites) is genuinely closed for the HG2 sentence itself.

### I/9 — **MAJOR** — §5's cap accounting pre-excuses the one finding class the pass names as its own top risk.

**Citation.** `2-plan.md:363-364`:
> *"**A class-α finding in a section pass 3 has NOT swept** would be under-generalization under R4 — but pass 3
> claims to have swept **all 86 rows**, so this category should be empty. **If a reviewer finds a 6th no-ID
> predicate, that is the honest exception**: it is the residual §1 declares, **not a hidden bounce**."*

`2-plan.md:374` ranks that same class first in the risk table: *"**A 6th predicate with no rule ID** | **Not
mitigated by any generator, and said so.** … **This is the honest top risk**."*

**Why it matters.** The clause makes the pass's own top-ranked risk **un-countable in advance**, and the party
writing the exemption is the party the count runs against. The reasoning is circular: *pass 3 claims to have
swept all 86 rows, therefore a finding in an unswept section cannot exist, therefore any such finding must be
the pre-declared residual.* The declaration of the residual (which is genuinely honest and which §8 credits) is
thereby converted into a shield.

Separately, the taxonomy is only **{α, β}** (`1-spec.md:74-75`). A finding that is neither — **every finding
in this record** — has **no stated cap treatment.** The generic severity route survives (`2-plan.md:353`:
blocker→stage 1, major→stage 2), so routing is not broken; but bounce accounting is silent, and combined with
the α carve-out the accounting cannot produce a cap trip from the classes most likely to be found. Compare the
first two bullets, which are honest and correctly binding (a class-β finding is *"a genuine second bounce on a
released cap … a stop-for-human, relayed verbatim. It is not re-argued"*). The third bullet is the one that
does not belong.

### I/10 — **MINOR** — R7 is presented at a provenance grade the runner explicitly disclaims for R6 — from the identical transcript record.

**Citation.** `1-spec.md:58-59` presents R7 as *"(transcript record **867**, `tool_use_id
toolu_01UToKNMx5K1itQdsxtmydbK`, an `AskUserQuestion` result)"*. `1-spec.md:149-150` states: *"**R6 was relayed
to this runner by the orchestrator with its record number and `tool_use_id`; this runner did not independently
fetch it.** *Relayed ratification* is the honest label and it is used."*

I verified R6 and R7 are the **two answers inside one `tool_result`** at record 867 (single `tool_use_id`,
`toolUseResult` keys `['questions','answers']`). If 867 was not fetched, R7 was not fetched either.

**Why it matters.** The "relayed ratification" label is applied at **1 of the 2 sites where it holds** — the
F/2 pattern reproduced inside the ratification record itself, and on the ruling that de-ratifies the
(a)/(b)/(c) checklist. I retrieved and confirmed R7 independently, so the **content** risk is nil; the defect
is label completeness, which is why this is Minor and not Major. It is the cleanest single illustration of the
disease this pass set out to cure.

### I/11 — **MINOR** — `1.5` §6 claims a criterion asserts a declination that no pinned string contains, and `2-plan` promises text no criterion pins.

**Citation.** `1.5-criteria.md:263-264`: *"**No criterion asserts frame diversity reduces correlated blind
spots** — `S-PRV-LIMIT` asserts the artifact **declines to claim it**."* `2-plan.md:257` promises the artifact
text *"…and whether frame diversity narrows that is **unsettled by this skill**."*

`S-PRV-LIMIT`'s actual pinned string (`oracles/criteria.tsv:27`, verified): *"what the gate establishes is
attested by the reviewers themselves and sampled, not independently proven; tier iii asks for a negative no
finite review can prove; and N same-model instances are not N independent minds"* — **no declination clause.**
`grep -n -iE 'frame diversity|unsettled|independent minds' oracles/criteria.tsv` returns **only** that row,
which lacks both "frame diversity" and "unsettled".

**Why it matters.** A gap-declaration section (`§6 Declared non-criteria (so the gaps stay visible)`) that
mis-states what a criterion asserts is the one place a mis-statement is most costly, because §6 is where a
reader goes to learn what is *not* covered. Minor because the load-bearing half is fine — see the credit below.

**Credit, and it is unambiguous:** *"N same-model instances are not N independent minds"* is pinned **verbatim,
plainly, unhedged**, at 4 measured sites (`M S ch s3`). My charter asks whether this is *"stated plainly, or
hedged into meaninglessness."* **It is stated plainly.** And `1.5:265-266` correctly declines any frame-diversity
claim at the level that matters (no criterion asserts it). The only defect is prose over-description.

### I/12 — **MINOR** — §3A borrows R1's operative phrase ("the confirmed-closed set") for a set larger than R1 ratified, and R1's word **"only"** is quoted nowhere.

**Citation.** R1's selected option, retrieved from record 694: *"Cycle 2 ships **only** the confirmed-closed
fixes (BIND over gate artifacts, ID renames, RES, redteam_context, §4 heading, seed slots, elc, DEP, CNC, root
pin); F1/F2/F5's mechanisms defer to a later cycle."*

`1-spec.md:173-178` §3A is headed *"**3A — the confirmed-closed set.**"* and lists `IDN`, `SPV`, `IGM`, `TPL3`,
`RST`, `SPN` in addition to R1's ten. `1-spec.md:161` **itself concedes** these are *"the in-scope items **not
in R1's parenthetical list**"* and books them as orchestrator calls. The word "only" appears nowhere in
`1-spec.md`. Additionally `2-plan.md:163` labels `catalog-pending` *"**FIXED IN SCOPE** — pass 2 recorded this
as a cycle-3 carry-forward"*, while §3A lists it inside "the confirmed-closed set" — a pass-2 carry-forward is
by definition not confirmed-closed.

**Why it matters.** §2.1's labelling is correct RAT2 practice and I credit it. §3A's heading undoes it by
re-branding the wider set with the ratified phrase, so a reader skimming §3 (the scope section) sees owner
authority where §2.1 says there is an orchestrator call. Minor because the honest statement is present one
section earlier and easy to find.

### I/13 — **MINOR** — The unbounded-wait declaration is absent from the two files that actually perform the HG2 ask.

**Citation.** `oracles/criteria.tsv:37` — `S-RUNEND`, `PAT=Stage-done|stage-done|stage is done`, pinned string
ends *"…so if that approval never arrives the run has no end and the catalog commit never happens"*. Measured:
```
S-RUNEND   NEW   2   M s8
S-HG2      NEW   5   M S s5 s7 s8      ← the ask lives at s5 and s7
```
**Why it matters.** `1-spec.md:216-217` books this as a declared gap (*"**`run end` has no timeout**, so a run
whose HG2 ask is never answered has no end (`S-RUNEND`)"*). It **is** declared in the artifact — genuinely, not
only in the plan — which is why this is Minor and not part of I/6. But a reader at `stage-7-assemble.md`
performing the ask, or at `stage-5-gate.md`, never encounters the consequence. The anchor (`stage-done`) selects
files that discuss the *restart predicate*, not files that discuss the *gate*.

### I/14 — **NITPICK** — `freeze-verify.sh` exists and is evidence-documented but is absent from the plan's "all of it built and executed" instrument table.

**Citation.** `ls oracles/` ⇒ `freeze-verify.sh` (mtime 13:08). `2-plan.md:324-337` §3's instrument table
(*"Measurement + instrumentation — **all of it built and executed before this document existed**"*) does not
list it. It **is** documented at `5-instrument-evidence.md` §A8. `2-plan.md` mtime is 13:02, so the script
postdates the table — a sequencing artifact, not a false claim.

### I/15 — **NITPICK** — R5 is absent from the RAT1 table while being cited as evidence elsewhere in the spec.

**Citation.** `1-spec.md:137-144`'s RAT1 table has six rows (R1, R2, R3, R4, R6, R7). R5 is used at
`1-spec.md:66` and cited as *measured evidence* at `1-spec.md:208` (*"the owner's R5 directive and his 'correct
on all counts' are plain free-text user turns"*). `LOOP-STATE.md:131-135` records R5 but gives **no transcript
record number**, and LOOP-STATE is the inadmissible locus. I did not verify R5 and mark it **unverified**;
because R5 governs no operative commitment in the documents under review (its precondition is declared unmet
at `LOOP-STATE.md:225-227`), I rank this a nitpick rather than inflate it.

---

## 6. COVERAGE CHALLENGE (CH8)

Behaviours this change could plausibly alter that **no criterion observes**, ranked by impact, each with a
concrete scenario. Scoped to my frame (honesty / authority / limits).

**1. The `SKILL.md:103-104` mnemonic-ID closed list — the artifact's own standing self-check instruction.**
Verified text at `SKILL.md:102-104`: *"…linked by the **mnemonic rule-IDs** in METHODOLOGY's cross-file rule
index — GBP, PASS1/PASS2/PASS-ORD, CMP/CMP2, SPN, COV, ORC/ECON, GRN, TOP, CAP, DEC, TPL/TPL3, RST, RAT3)…"*
— no `TPL1`, no `TPL2`, no `SEV`, and none of this cycle's ~12 new IDs. `2-plan.md:314-315` says *"**F/15,
recorded not fixed:** `SKILL.md:103-104`'s mnemonic-ID list is a **stale closed list** governing the standing
self-check. **Updating it is in scope (D17 adds the new IDs)**; making it self-maintaining is not."*
**No criterion observes it:** `S-IDGREP`, `S-IDGREP-CAV`, `S-IDGREP-NAME` each measure `M` only (1 site) — none
touches `SKILL.md`. R2 (`1.5:179-182`) requires every §2 CHANGE row to have ≥1 §1 row with a measured SITES
column, and D17 has three — but none of them governs this list.
**Scenario:** the build ships. `D17` correctly adds every new ID to METHODOLOGY's cross-file index. `SKILL.md:104`'s
list stays at its 2026-07 contents. Every oracle passes, `ruleid-sitemap.sh` exits 0, `check.sh` reports 68/68.
A user then follows the skill's own instruction — *"Standing self-check criteria after any edit: … consistency
on every rule stated in more than one place (linked by the mnemonic rule-IDs …)"* — and silently omits
**every rule this cycle added**, including `HG2`, `BIND`'s dispatcher operand, and all the honesty-seam rules.
The pass's own claimed-in-scope half of F/15 is unobserved. **Highest impact: it is the one gap that degrades
the artifact's future maintenance, and the pass explicitly claims this half in scope.**

**2. Semantic reintroduction of any deleted overclaim in a phrasing the absence sweeps do not enumerate.**
The whole subtractive-honesty programme rests on **11 literal absence strings** (enumerated in I/1). Nothing
observes reintroduction in other words. `1.5-criteria.md:228-231` declares this (*"`check.sh` … is not a
semantic oracle"*), so it is disclosed — but disclosure is not observation, and **I/1 and I/2 are two live
instances already present in the pass's own artefacts.**
**Scenario:** a build writes, at `stages/stage-1-frame-template-match.md`, *"the off-limits set is the fence the
run never crosses"*. `S-OFL` does not reach `s1` (its anchor is the literal `off_limits_paths`, absent there);
no absence string matches; `check.sh` reports 68/68 PASS; the artifact simultaneously asserts and denies that
`off_limits_paths` is enforced. **Rank 2 — the mechanism's blast radius is the entire honesty programme.**

**3. The R7 proposal label at the instrument layer.** `oracles/gen-sweep-table.sh:28` emits
`| # | Predicate / gate | source | (a) producer provably earlier? | (b) degenerate: … | (c) counterpart /
release | verdict |` with **no proposal label**, and `oracles/sweep-answers.tsv:1` carries the same three
column headers unlabelled. No criterion observes the label's presence anywhere.
**Scenario:** cycle 3 regenerates the sweep into a fresh document (SC6 requires the generators to reproduce
byte-for-byte, so the header is guaranteed to reappear). The `⚠ R7 LABEL` prose block does not travel with it.
The checklist re-acquires the appearance of a standing requirement in a document whose author never saw R7.
`1-spec.md:63` claims the label ships *"EVERYWHERE IN THIS CYCLE'S DOCUMENTS"* — literally true, and that is
exactly the loophole: the generator is not a document. **Rank 3 — low blast radius now, but it is the specific
mechanism by which R7 gets quietly reversed.**

**4. The description's 27-character slack.** `1.5:315-317` and `2-plan.md:379` both declare it and both state
*"no criterion enforces a reserve"* / *"Declared as a known tightness, not a defect."* Honestly declared, so
partial credit — but the behaviour (a future clause pushing `description` past 1024 and killing skill
triggering) is unobserved between cycles.
**Scenario:** cycle 3 adds one clause about the assembly gate. SC1 is a cycle-2 criterion and does not run.
The skill stops triggering and no one learns why. **Rank 4 — declared, cheap to observe, unobserved.**

**5. Whether the artifact's honesty sentences are mutually consistent, not merely individually present.**
`1.5:228-231` declares that `check.sh` cannot disagree with the artifact about *whether the sentence says the
right thing* and names *"the stage-3 reviewers"* as the guard on meaning. **I/1 is the proof this declared gap
is already exercised:** two gating rows demand contradictory sentences in the same two files, and every oracle
passes. Nothing observes pairwise contradiction among the 68 pinned strings — a check that is mechanically
cheap (the pinned strings are a closed set of 68; contradictory keyword pairs like `not an enforced fence` vs
`is a fence` are enumerable). **Rank 5 — declared, but the declaration has already failed in practice, which is
what moves this from "known limitation" to "coverage gap".**

**No "none found" claimed.** Five gaps, all with concrete scenarios, two of them (1 and 5) already realised in
the artefacts under review.

---

## 7. LABEL AUDIT (CH9 / CH10)

**Universal-gating claim, verified:** `1.5-criteria.md:80` — *"**Every row is gating.**"* Confirmed against
`oracles/criteria.tsv`: all 68 rows are gating in the generated table; the `Gating` column is `gating` for
every row. `2-plan.md:366` — *"All criteria are **gating**."* **There is no advisory label anywhere, so the
CH9 advisory-relabel dodge is structurally unavailable.** I looked for the deferral loophole in its other
guises and did not find it: the phrase *"declared deferral"* occurs 4× across the three documents and **all
four are prohibitions** (`1-spec.md:187`, `1-spec.md:240`, `1.5:50`, `2-plan.md:367`), and H5's dispositions are
consistently stated as *harness OR named risk-acceptance*, with RAT3 correctly ruling out the latter and
leaving **HALT + verbatim relay** (`1.5:50-53`, `2-plan.md:366-368`). **This is clean and earned.**

Per gating criterion I sampled — the governed path, the evidence I checked, and my verdict:

| Criterion | Path it actually governs | Evidence I checked | Verdict |
|---|---|---|---|
| **S-OFL** | the honest fence statement at every file naming `off_limits_paths` | ran `--sites` ⇒ 2 (`M ex/planning`); B7 P5 ⇒ 5 files; grepped the corpus for the surviving overclaim; enumerated all 11 absence strings | **UNVERIFIED (CH9 last clause).** Gate is real but under-scoped (I/7) **and self-contradicted by S-CTX-DECONF (I/1)**. Treated as unverified = deferred. |
| **S-CTX-DECONF** | de-conflation of `redteam_context` from `off_limits_paths` | read its pinned string in `criteria.tsv`; ran `--sites` ⇒ 2, identical to S-OFL's | **UNVERIFIED.** Its pinned string *is* the I/1 blocker. |
| **S-PRV** | deletion of the completeness overclaim + humble replacement | read `checklib.py` to establish the absence path is case-**sensitive** (confirmed); grepped `PROVEN` (1 hit) and `proven` (8 hits) over the pinned corpus; compared against B7 P6 | **UNVERIFIED.** Gate is verified against a **non-representative input class** (per-FILE vs per-occurrence) — CH9 bullet 2 precisely. See I/2. |
| **S-PRV-LIMIT** | the correlation limitation at the tier/contract-floor sites | ran `--sites` ⇒ 4 (`M S ch s3`); read the pinned string in full | **EARNED.** Positive and limitation are welded into one string so they cannot separate; the "not N independent minds" clause is plain. Only the §6 prose about it overstates (I/11). |
| **S-HG2-LIMIT** | the duty-not-property qualification at every HG2 / top-level-ONLY site | ran `--sites` ⇒ 7 (`M S s5 s6 s7 s8 tp/decomp`); compared with `S-HG2`/`S-HG2-DEGEN`/`S-HG2-MARKER` ⇒ 5 (`M S s5 s7 s8`), a strict subset | **EARNED.** No HG2 rule statement can ship unqualified. F/2's headline defect is genuinely closed. |
| **S-HG2-NOSELF** | that `self-approved` never appears unqualified | read the COOC implementation (`checklib.py`: `sites=[f for f in files if pat.search(raw[f])]`, then per-site pinned assertion — genuine co-occurrence semantics); confirmed `vacuous = (kind in ("NEW","COOC") and not sites)` makes it FAIL at 0 sites; grepped `self-approv` ⇒ **0 baseline hits** | **Mechanism EARNED; gate does not govern the live surface.** The equivalent claim ships at `s3`/`s4` untouched (I/8). |
| **S-COV-LIMIT** | the seam-union gap stated wherever total coverage is claimed | ran `--sites` ⇒ 4 (`M S s6 s7`); read `PAT=Total coverage\|total coverage\|every node gated clean\|every node is gated clean` | **EARNED.** Declared-gap done right, in the artifact, at every claiming site. |
| **S-F5-LIMIT** | TOP's defeatability stated at every topgate site | ran `--sites` ⇒ 6 (`M S s1 s6 s8 tp/decomp`) | **EARNED.** Same model. |
| **S-RUNEND** | the no-end consequence of an unanswered HG2 | ran `--sites` ⇒ 2 (`M s8`); compared with `S-HG2`'s `s5 s7` | **Label sound, placement wrong (I/13).** Governed path is exercised; the *needed* path (the ask sites) is not. |
| **S-DESC-HG2** | the corrected `SKILL.md` frontmatter description | ran `--sites` ⇒ **1** (`S`); anchor is `self-checking loop for PLANNING`, which cannot drift | **EARNED, with the right caveat.** SC1/SC2's 997-char / `Skill is valid!` measurement is on a **scratch copy** and `1.5:191-196` **labels it as such** (*"The artifact itself is deliberately unedited before gate 4, so this was measured on a copy — labelled as such rather than claimed of the artifact"*). That is the honest form of an unbuildable pre-measurement. |
| **whole family — can-fail** | that the 68 assertions discriminate rather than pass at baseline | **I executed `oracles/baseline-replay.sh` myself:** `NEW+COOC rows failing at baseline : 60` · `PRESERVE rows passing at baseline : 8` · `NEW+COOC rows WRONGLY passing : none` · `PRESERVE rows WRONGLY failing : none` · `REPLAY: OK — every assertion discriminates` | **EARNED, and independently reproduced.** This is the single most load-bearing execution claim in `1.5` §4 and it holds when a cold reviewer runs it. |

**No criterion in my sample looked relabelled to avoid verifying a real gate.** The failures I found are of a
different kind: gates that are genuine, executed, and *aimed at the wrong surface* (S-PRV, S-HG2-NOSELF,
S-OFL, S-RUNEND). That distinction matters for routing — these are fixable in place by widening anchors and
sweeps, not by rebuilding the apparatus.

---

## 8. WHAT THE PASS GENUINELY EARNED

Specific, and I checked each one.

1. **The instruments exist and they discriminate — pass 2's class-β blocker is genuinely closed.** I ran
   `oracles/baseline-replay.sh` cold: `REPLAY: OK`, 60/60 NEW+COOC fail at baseline, 8/8 PRESERVE pass, **0
   wrongly passing, 0 wrongly failing.** Pass 2's E/1 (*"`ruleid-sitemap.sh` is byte-for-byte pass 1's printer;
   `expected-sites.txt`, `check.sh`, `baseline-replay.sh` absent"*) is not merely claimed closed — the
   replacement runs and fails correctly on demand. The §0 discipline (*"Build → run → paste the real command
   output — *then* describe it, **in the past tense**"*) is visibly obeyed throughout `1.5` and `2-plan`.

2. **The case-sensitivity claim is precise, unobvious, and true.** `1.5:60-63` asserts the absence sweep is
   case-**SENSITIVE** *"which is what lets `PROVEN` be swept without also hitting `provenance`."* I verified it
   in `checklib.py`: the pinned-string path lowercases (`t.lower().find(pin)` with `pin=norm(...).lower()`) and
   the absence path does not (`if norm(a) in texts[f]`, `texts[f]` never lowered). Corpus grep confirms
   `PROVEN` occurs at `SKILL.md:3` only while `provenance` occurs 6× untouched. A correct, load-bearing
   technical claim that a reviewer could easily have taken on trust.

3. **The site sets really are generated, and 10 of 12 match B7 exactly.** I ran `check.sh --sites` and compared
   against B7's own `count:` lines. PRV 4, XPM 9, HG2-ONLY 4, index.md 5, gate log 9, catalog 3, SPN 6, SPV 1,
   CTX 4, IGM 3 — **all exact.** F/1's blocker is substantially closed; the two misses (I/7) are honesty
   defects in a summary sentence, not fabricated site lists.

4. **The ratification record for five of seven rulings is genuinely spot-checkable, and I spot-checked it.**
   Every option label quoted in `1-spec.md:139-144` matches the presented options at records 694 and 866
   **byte-for-byte**, and every recorded selection matches the owner's actual answer at records 699 and 867.
   `1-spec.md:143`'s claim that the owner *declined the orchestrator's recommendation* on R6 is true. R4's
   quote is byte-exact. **Pass 2's F/3 (R4 cited an agent-authored file) is genuinely fixed**, and the
   LOOP-STATE citation discipline is clean: not one owner quote in the three documents is sourced to the
   agent-authored file. This is rare and it is the pass's best work.

5. **R7's substance is honoured completely.** I checked every occurrence of the (a)/(b)/(c) framing across the
   three documents plus `decisions.md` and the oracles. It is labelled a proposal at six sites, and **there is
   no place in any of the three documents where it is cited as something the owner requires.** F/4 is closed,
   and `1-spec.md:66-68` says so against interest (*"reviewer F/4 called that unratified inflation and **R7
   confirms F/4 was right**"*).

6. **RAT2 discipline is applied to the pass's own authoring choices, unprompted.** `S-HG2-AUTHORED` pins *"how
   an HG2 bounce routes is this cycle's own authoring choice and not part of the ratified decision"* at 3
   measured sites — i.e. the runner made a criterion out of labelling its own non-authority, **in the shipped
   artifact**. `1-spec.md:162` likewise lists "This runner's authoring choices" as a first-class authority tier.
   That is the correct instinct and it is what makes I/5 and I/12 minor scope-label defects rather than a
   pattern of authority-grabbing.

7. **Withdrawals instead of defences, including of its own work.** The X-protocol variance claim is withdrawn
   outright with the reason stated (`1.5:242-246`: *"Holding the agent constant is exactly what makes the two
   spawns per arm maximally correlated"*). F/17's overstatement is replaced by the weaker true claim
   (`1.5:267-270`). Most tellingly, `1-spec.md:32-39` records pass 3's **own** false claim about the phantom
   ledger — *"**That was false as shipped.**"* — with the mechanism of the falsehood (`2>/dev/null` discarding
   the reporting path) and the fix. And `decisions.md:284-286` volunteers that *"R4's corollary was **not
   actually executed**"* in pass 2. Self-reported error at that granularity, against interest, is the strongest
   honesty signal in these documents and it should be said plainly.

8. **The vacuous-site guard is a genuine invention, and the honest description of what it cannot do is
   volunteered.** `1.5:271-273`: *"**`S-HG2-NOSELF` cannot force any text to be written** … Stated because a
   co-occurrence row reads like an obligation row and is not one."* Most authors would have let the reader
   assume otherwise. The guard itself (`checklib.py`: a NEW/COOC row measuring 0 sites **FAILS**) is the
   correct generalization of `S-CTX-VAC`'s insight to the checker itself, and I confirmed it is what makes the
   COOC row a can-fail check rather than a wish.

9. **The declared-gap pattern, where it was applied, is exactly right.** `S-COV-LIMIT` (4 measured sites) and
   `S-F5-LIMIT` (6) put the residual defect **in the artifact, at every site that claims the thing the residual
   undermines**, while the mechanism stays deferred. That is the correct way to ship a known hole, and I/6 is a
   finding *precisely because* the pass proved it knows how.

---

## 9. Routing summary

| id | severity | one-line |
|---|---|---|
| **I/1** | **BLOCKER** | S-CTX-DECONF re-adds the `off_limits_paths` fence overclaim at both of S-OFL's sites; F/7's named structural fix cannot see it |
| **I/2** | **BLOCKER** | "completeness proven" survives at `SKILL.md:8,17` and `README.md:10,12`; the per-FILE fix for E/11 is what lets it |
| **I/3** | MAJOR | R4's options were presented and declined; the axis was restated to fit the answer, and the honesty note names the wrong defect |
| **I/4** | MAJOR | R4's "means nothing" inflated into cap-bounce immunity — the reverse of the owner's clause |
| **I/5** | MAJOR | R6's scope-defining option description quoted nowhere; pass 3 exceeds it and §1 asserts the scope claim as fact |
| **I/6** | MAJOR | ORC's death detector and `required_sections` vacuity declared only in `2-plan.md`; COV/TOP's identical gaps get artifact criteria |
| **I/7** | MAJOR | `1.5:37`'s F/1-closure claim false at 2 of 12 entries; OFL's real site set is 2, not 5, hiding a 3-file honesty gap |
| **I/8** | MAJOR | the "self-approved" COOC guard is keyed to a 0-occurrence string while "Nothing self-certifies" ships bare at `s3`/`s4` |
| **I/9** | MAJOR | §5 pre-declares the pass's own top-risk finding class not a bounce; findings outside {α,β} have no cap treatment |
| **I/10** | MINOR | "relayed ratification" labelled for R6 but not R7, from the same record |
| **I/11** | MINOR | `1.5` §6 claims S-PRV-LIMIT asserts a frame-diversity declination it does not contain |
| **I/12** | MINOR | §3A brands a wider set with R1's "confirmed-closed" phrase; R1's "only" quoted nowhere |
| **I/13** | MINOR | the run-has-no-end declaration is absent from `s5`/`s7`, where the HG2 ask happens |
| **I/14** | NITPICK | `freeze-verify.sh` missing from §3's instrument table |
| **I/15** | NITPICK | R5 absent from the RAT1 table while cited as evidence elsewhere |

**Under `2-plan.md` §5's own accounting:** I/1 and I/2 are *"the apparatus cannot detect a bad build — and the
document says it can"* applied to the honesty programme rather than to the oracles: the apparatus reports PASS
while the artifact contradicts itself (I/1) and retains the overclaim it claims to delete (I/2). **Whether that
is class β is the runner's determination, not mine, and I decline to make it** — but I note that §5's own
first bullet makes a class-β finding against pass 3 *"a genuine second bounce on a released cap"* and
*"a stop-for-human, relayed verbatim,"* not to be re-argued. **I/9 is my finding that the accounting which
would classify I/1 and I/2 is written by the party the count runs against.** Neither I/1 nor I/2 is a "6th
no-ID predicate", so §5's third-bullet carve-out does not reach them.

**Carry-forwards, not blockers (out of scope by owner ruling):** none of my findings rests on F1, F2, F5's
mechanism, DIV, the cost/fan-out envelope, ECON's O(children²), or the "two passes" ruling. I/6 concerns the
*declaration* of out-of-scope items, which my charter places squarely in scope; I/11 concerns a claim *about*
DIV rather than DIV itself.
