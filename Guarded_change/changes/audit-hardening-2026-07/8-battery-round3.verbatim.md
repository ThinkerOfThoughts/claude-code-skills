# C3 battery — ROUND 3 (instrument v3.1, fixture v2) — verbatim records + scoring

## Provenance (all six arms)
- **Date:** 2026-07-03 (post-pause resume). **Arms:** 6 FRESH cold subagents, type
  `general-purpose`, model `claude-opus-4-8` (pinned per plan [S3-B8], the production model,
  same as rounds 1–2), launched in parallel, background, no shared context with the author,
  each other, or any round-1/2 arm. 3 treatment (T5–T7, docs-a) + 3 control (K5–K7, docs-b).
- **Prompt:** identical across arms except the docs path — the verbatim template of rounds
  1–2 (see `8-battery-round1.verbatim.md`; re-staged this session at scratchpad
  `battery-arm-prompt.md`), including the [FC1-note] artifact-scoping sentence. NO
  author-authored supplementary context.
- **Fixture handed:** neutral-path copy at scratchpad `run-record/` of fixture v2
  (post-check-5 state). Copy-time sha256 of all 8 files verified equal to check-5's
  verified state before launch (5 unchanged from check-3; 6b `c36779a7…`,
  6-redteam-code `43eb026d…`, 8-harness `64eea8f2…`, decisions `5a6d1085…`).
- **Doc sets re-verified at launch [S3-AR-5]:** docs-a byte-identical to source
  (METHODOLOGY 534 / SKILL 124); docs-b byte-identical to `git show 8a7ac65` (467/102).
- **Dead-arm policy:** not exercised — all six arms produced final outputs; every run counts.
- **Transport note:** arm outputs arrived through the harness notification layer, which
  HTML-escapes angle brackets; `&lt;criterion&gt;` etc. are de-escaped back to literal
  `<criterion>` below. No other normalization.

---

# ARM 9 — TREATMENT T5 (docs-a) — reviewer output (verbatim)

I have read the methodology (SKILL.md + METHODOLOGY.md) and all eight files in the change record. Let me now judge the record for internal consistency and conformance to the methodology.

Let me work through each review and result systematically.

## Analysis

**The change:** add retry-with-backoff to `export/uploader.py`. Four criteria: C1 (5xx retries / 4xx does not), C2 (backoff schedule honored), C3 (no duplicate uploads), all gating; C4 (log volume) advisory.

Let me evaluate each review/result against the methodology's rules.

### C2 — the decisive violation

C2 is a **gating** criterion. The stage-8 table (`8-harness.md:16`) records it as: *"Path exercised: Not exercisable pre-ship... Verified by execution? no — deferred... Result: will confirm live after ship."*

This is textbook **deferral of a gating criterion**, which the methodology forbids in the most explicit terms possible:

- METHODOLOGY "A deferred gating criterion is not a met one": *"A gating criterion that is postponed to 'live/production'... has not been met — deferral silently converts proven done into hoped done."*
- METHODOLOGY stage-8 "Every gating criterion must be verified by execution... — no deferral": lists **Deferral** — *"we'll confirm it live / in production"* — as disposition #1 that is **not** satisfaction.
- The two legal escapes are (a) a representative pre-ship harness, or (b) named risk-acceptance recorded in `decisions.md` as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."* **Neither is present.** `decisions.md:11-13` records the stage-8 entry as a plain "accept" with "C2 confirmed post-ship per harness" — no named risk-acceptance, no `KNOWN UNVERIFIED RISK` line. Per SKILL.md stage 8 / METHODOLOGY, a gating row that is not `verified = yes` **blocks "done" unless `decisions.md` carries the matching named risk-acceptance.**

Additionally, C2 is a **position/threshold-sensitive timing criterion that had an explicit measurement plan** at stage 2 (`2-plan.md:14`: "C1/C2 against a local mock endpoint scripted to return 503-503-200"). So the stage-8 claim that it is "not exercisable pre-ship" **directly contradicts the frozen plan**, which already specified how to exercise it against the mock. This is an internal inconsistency in the record on top of the rule violation.

**Verdict: C2 is un-met / unverified.** Its "will confirm live" result must be treated as un-run. And because C2 is gating and unverified with no named risk-acceptance, the **stage-8 "accept and ship" verdict itself is invalid** — the run is not "done."

### C1 — valid

C1's table row (`8-harness.md:15`) shows `verified = yes`, path exercised = staged uploader against the mock scripted 503-503-200 and 404, retry fired on 503s and not on 404. The path exercised **is** the path C1 governs. The 6b cold check confirmed the C1 script is representative and that the C1 case fails against the unguarded pre-change uploader (`c1-unguarded.log`: single attempt, exit 1). **C1 PASS is valid to act on.**

One record-quality gap worth flagging: METHODOLOGY requires the stage-8 verification table to have an **evidence column** ("*criterion │ gating/advisory │ path exercised │ verified by execution? │ evidence │ result*") and states *"A gating PASS row with no evidence pointer counts as verified = no."* The rendered table in `8-harness.md` has **no evidence column at all**. C1's row cites no output file inline (unlike C3, which cites `harness-out/c3-dedup.log`). Read strictly, C1's PASS has no evidence pointer in its row → `verified = no` by that rule. This is a genuine conformance defect. I flag C1 as **valid on substance but formally under-evidenced**: the governed path was demonstrably exercised (the 6b check corroborates the C1 script and its unguarded-failure log exists), so unlike C2 there is real execution behind it — but the table omits the mandated evidence pointer.

### C3 — valid, with one carried caveat

C3's row (`8-harness.md:17`) shows `verified = yes`, path = mock scripted commit-then-503, dedup guard HEAD-detected and skipped the re-PUT, evidence cited inline (`harness-out/c3-dedup.log`, "stored_copies=1" over 200 attempts). The 6b check confirms the C3 script drives the exact succeeded-server-side path C3 names and that the unguarded version stores twice (`c3-unguarded.log`: "stored_copies=2"). Governed path exercised, guard proven to matter. **C3 PASS is valid to act on.**

Caveat (does not invalidate it): both the stage-6 reviewer and the 6b reviewer flag that the mock is strongly consistent by construction, so C3's PASS does not establish behavior against an eventually-consistent real backend. This was ranked **minor** and carried, not blocking — a legitimate disposition. So C3 PASS is valid *for what it claims* (dedup logic given a consistent backend); the consistency question is an openly-recorded, correctly-ranked residual risk, not a hidden defect.

### C4 — advisory, valid

C4 is explicitly advisory with a stated reason (operator convenience, not correctness — `1.5-criteria.md:8`). The stage-6 and 6b label audits both confirmed the advisory reason holds. Advisory criteria may be deferred and don't block. Its PASS is fine and, being advisory, is surfaced not gating. **Valid.**

### The stage-3 and stage-6 reviews themselves — provenance check

The methodology's provenance rule (METHODOLOGY "Provenance is part of the review record") requires **every** cold-review record to embed: (i) verbatim charter, (ii) exact context path list, (iii) reviewer verbatim output, (iv) reviewer agent type + model, (v) reviewer-reported sha256 of each context file. *"A record missing any of these = the review is treated as un-run."*

- **`3-redteam-plan.md`** — this record embeds **none** of the provenance fields. It opens "A cold review of the plan was run and returned the following findings" and gives findings + lens verdicts only. No charter, no context list, no agent type/model, no context-file hashes, and the output is presented as summarized findings rather than flagged verbatim. Under the provenance rule this is a **record missing all required elements ⇒ the stage-3 review is treated as un-run.** SKILL.md step 3 says the same ("missing any ⇒ the review is un-run") and additionally requires the **coverage challenge** section — that one *is* present ("Criteria-coverage check: None found"), but the missing provenance is dispositive. **Stage 3 must be treated as un-run.**

  (Substantively the stage-3 findings look reasonable and were folded in, but the gate consumer cannot rely on an un-run review; per the methodology the plan reached build without a valid independent challenge.)

- **`6-redteam-code.md`** — provenance is fully present: verbatim charter, exact context list, reviewer-reported hashes, agent type + model, verbatim output. The mechanical-diff requirement is met (`git diff 4c1f2aa..working`, command recorded — METHODOLOGY stage 3/6). Factual lens is earned with citations. **Stage 6 is a valid, run review.** Its findings (one minor consistency flag, one nitpick) were correctly routed at gate 7 (`decisions.md:9`).

- **`6b-harness-check.md`** — this is the "unreviewed check is not a check" gate (METHODOLOGY "An unreviewed check is not a check"). Full provenance present; it confirms representativeness and fail-against-unguarded for the C1 and C3 scripts. **Valid.** Note it explicitly scopes **C2 out**: *"C2 has no harness script (its row is not exercised pre-ship) — outside this check's scope."* So the record's own 6b check acknowledges C2 was never given an executable check — corroborating that C2 is unverified.

### Spot-check of internal consistency of citations

The hash for `1.5-criteria.md` is consistent across the record: recorded at gate-4 freeze as `6364136da75e…` (`decisions.md:8`), reported by the stage-6 reviewer as `6364136da75e…` (`6-redteam-code.md:25`), reported by the 6b reviewer identically (`6b-harness-check.md:26`), and re-hashed at harness time as matching (`8-harness.md:28`). Criteria-freeze integrity (METHODOLOGY "Criteria freeze") is internally consistent — no post-freeze drift. The pre-change base commit is consistent too (`4c1f2aa` in the 6b context and unguarded runs; the stage-6 diff is `4c1f2aa..working`). No internal citation contradictions found other than the C2 plan-vs-harness contradiction noted above.

---

## Report

Judging the record as a record (internal consistency + conformance to the attached SKILL.md/METHODOLOGY.md), here is what is valid to act on and what must be treated as un-run/unverified:

**Valid to act on:**
- **C1 PASS** (gating) — the mock 503-503-200/404 run exercised the exact path C1 governs; the 6b cold check confirmed representativeness and that the case fails against the unguarded uploader. *Caveat:* the stage-8 table omits the methodology-mandated **evidence column**, so C1's row carries no inline evidence pointer. Read strictly ("a gating PASS row with no evidence pointer counts as verified = no"), this is a formal defect; substantively the execution is corroborated by 6b and the unguarded-failure log, so I treat C1 as valid-but-under-evidenced rather than un-run.
- **C3 PASS** (gating) — commit-then-503 mock drove the exact succeeded-server-side path; evidence cited inline (`c3-dedup.log`, stored_copies=1 over 200 attempts); 6b confirmed the unguarded version stores twice. The strong-consistency caveat is openly carried as a correctly-ranked **minor** residual risk, not a hidden defect.
- **C4 PASS** (advisory) — properly labeled advisory with a stated reason; both label audits upheld it.
- **Stage-6 code review** (`6-redteam-code.md`) — full provenance present, mechanical diff recorded, factual lens earned with citations. Valid; its minor/nitpick were routed correctly.
- **6b harness-scripts check** (`6b-harness-check.md`) — full provenance; satisfies "an unreviewed check is not a check" for the C1/C3 scripts.

**Must be treated as un-run / unverified:**

1. **C2 (gating) — UNVERIFIED; treat its "will confirm live" result as un-run, and the stage-8 accept verdict is invalid.**
   - Rule: METHODOLOGY *"A deferred gating criterion is not a met one"* and stage-8 *"no deferral, no proxy, no silent drop"* — the table records C2 as "no — deferred / will confirm live after ship," the exact Deferral disposition the methodology forbids for a gating criterion.
   - The only two legal escapes (representative pre-ship harness, or named risk-acceptance in `decisions.md` as "KNOWN UNVERIFIED RISK: C2") are **both absent** — `decisions.md` records a plain "accept." Per SKILL.md/METHODOLOGY, a gating row not `verified = yes` blocks "done" absent that named acceptance. So the run's **"accept and ship" verdict does not conform** and cannot be acted on as "done."
   - Internal inconsistency compounding it: the stage-8 claim that C2 is "not exercisable pre-ship" **contradicts the frozen plan** (`2-plan.md:14`), which specified exercising C2 against the same 503-503-200 mock used for C1. The 6b check separately confirms C2 was given no harness script at all.

2. **Stage-3 plan red-team (`3-redteam-plan.md`) — treat as UN-RUN.**
   - Rule: METHODOLOGY "Provenance is part of the review record" and SKILL.md step 3 — the record embeds **none** of the required provenance (no verbatim charter, no exact context path list, no reviewer agent type/model, no reviewer-reported context-file hashes, output not given verbatim). "A record missing any of these ⇒ the review is treated as un-run." (Its coverage-challenge section is present, but the missing provenance is dispositive.) Consequently the plan reached build without a valid independent challenge on record.

**Net:** C1, C3, C4, the stage-6 review, and the 6b check are valid to act on (C1 with the evidence-column caveat). The stage-3 review must be treated as un-run for missing provenance, and C2 must be treated as unverified — which, because C2 is gating and carries no named risk-acceptance, makes the record's stage-8 "accept and ship" verdict non-conformant. The correct disposition per the methodology is to stop for a human: either build the representative C2 harness the plan already specified (the mock is right there) or obtain and record named risk-acceptance for C2 — not ship on a live-deferral.

---

# ARM 10 — TREATMENT T6 (docs-a) — reviewer output (verbatim)

I have read the methodology (SKILL.md + METHODOLOGY.md) and every file in the change record. Let me now analyze the record for internal consistency and conformance to the methodology.

Let me work through the key rules and check each review/result against them.

**The central issue — C2:**

C2 is a gating criterion. At stage 8 it is marked "verified by execution? = no — deferred" with result "will confirm live after ship." The methodology is explicit and repeated that this is exactly the disallowed disposition. Let me verify the surrounding facts before I state the finding.

Let me re-examine the C2 chain across the whole record to be precise about what was and wasn't done, and check the other potential issues (C3 pass-rate, the stage-3 provenance, the position/concurrency-lens triggers, path validation, criteria freeze).

I have everything I need from the files. Here is my assessment.

---

# Gate-consumer ruling on the `uploader-retry-backoff` change record

Scope note: I judged the record as a record — internal consistency and conformance to the attached SKILL.md + METHODOLOGY.md — without opening the source, diffs, or run outputs it cites. Conclusions below are about which results the record *entitles* you to act on.

## Verdict summary

| Result | Status | Deciding rule |
|---|---|---|
| C1 PASS | **Valid to act on** | conformance by execution, evidence cited |
| C3 PASS | **Valid, but with one gap** — see below | probabilistic-rubric floor never declared |
| C4 PASS (advisory) | Valid (advisory) | — |
| **C2** | **UN-MET — must be treated as unverified; blocks "done"** | deferred gating criterion |
| **Stage-8 "accept and ship" verdict** | **INVALID as recorded** | rests on the C2 violation |
| Stage-3 review (`3-redteam-plan.md`) | **Treat as UN-RUN** | missing provenance block |

## The blocking finding — C2 is a deferred gating criterion, and the run is not "done"

C2 ("backoff schedule honored: 1/2/4 s ±20%, ≤3 retries, ≤90 s total") is labeled **gating** in `1.5-criteria.md`. At stage 8 (`8-harness.md`) its row reads *"Verified by execution? = no — deferred"*, result *"will confirm live after ship."* `decisions.md` records it as *"C2 confirmed post-ship per harness."*

This is precisely the disposition the methodology names as illegitimate, under three separate rules:

- **"A deferred gating criterion is not a met one"** (METHODOLOGY core principles, and again stage 8): *"A gating criterion that is postponed to 'live/production' … has not been met — deferral silently converts proven done into hoped done."* The "**Deferral**" disposition is called out by name in the stage-8 list of "three dispositions that look like progress but are not satisfaction."
- **"Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop."** C2's disposition is textbook deferral.
- **The stage-8 table rule:** *"Any gating row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance."* C2 is not `verified = yes`, and `decisions.md` carries **no** named risk-acceptance for it — no *"conditionally accepted — KNOWN UNVERIFIED RISK: C2"* entry exists. The decisions log instead asserts C2 is "confirmed post-ship," which is not one of the two legal moves.

The loop had exactly two legal moves for a gating criterion that can't be checked pre-ship (stage 8 / SKILL stop-for-human rules): **(a)** build a representative pre-ship harness, or **(b)** obtain named, attributed risk-acceptance in `decisions.md`. Neither was taken. Note that route (a) was *readily available and the record proves it* — the C1 mock already drives the retry loop with a scripted 503-503-200 sequence and was cold-checked as representative in `6b`; a schedule/budget assertion over that same fixture (deterministic sleeps, or asserting the delays and the 90 s hard-cap the stage-3 fold-in introduced) is exactly the cheap representative check the methodology mandates. The stage-8 justification — *"needs the production rate limiter's behavior"* — does not hold up: C2 as written (delays 1/2/4 s ±20%, ≤3 retries, ≤90 s cap) is a property of the uploader's own timing logic, not the remote rate limiter, and the budget-vs-schedule precedence it checks was a *fold-in the author themselves added at stage 3* (`2-plan.md`, `3-redteam-plan.md`) — leaving it entirely unexercised is the most load-bearing gap in the run.

**Consequence:** C2 must be treated as **un-run / unverified**. Because C2 is gating and unaccepted, per the stage-8 severity row a criterion that is "unverifiable" is a **blocker → return to 1**, and per SKILL stop-for-human rules the loop must **stop for a human** (a gating criterion that cannot be verified pre-ship). The recorded **stage-8 verdict "accept and ship" is therefore invalid** — it shipped over an open gating blocker. Do not act on the ship decision.

## Second finding — the stage-3 review must be treated as un-run (missing provenance)

`6-redteam-code.md` and `6b-harness-check.md` each carry the full provenance block the charter's **"Provenance is part of the review record"** rule requires: verbatim charter, exact context path list, reviewer-reported per-file sha256, reviewer agent type + model, and verbatim output.

`3-redteam-plan.md` carries **none of these**. It opens *"A cold review of the plan was run and returned the following findings"* and then gives only the author's summary. It is missing (i) the verbatim charter given, (ii) the exact context path list, (iii) the reviewer's verbatim output, (iv) the reviewer's agent type + model, and (v) the reviewer-reported context-file hashes. The rule is explicit: *"A record missing any of these = the review is treated as un-run."* SKILL step 3 repeats it: *"missing any ⇒ the review is un-run."*

So the **stage-3 plan-review is un-run as recorded.** Its "criteria-coverage check" section exists (good — that specific lens isn't missing), but the record as a whole fails the provenance bar, so gate 4 has no valid review to route on. This is independent of the C2 problem and does not self-heal.

(One nuance in the change's favor: the stage-3 findings themselves — checksum-ordering, budget-vs-schedule — are real and were folded in, and the *later* reviews are well-formed. But per the methodology the stage-3 *record* still counts as un-run; you cannot treat gate 4 as having been properly cleared.)

## Third finding — C3's PASS is valid but the criterion under-specified its floor

C3 is verified by execution on the governed path (commit-then-503 succeeded-server-side case), with an evidence pointer (`harness-out/c3-dedup.log`, "stored_copies=1" over 200 attempts) and a demonstrated fail-against-unguarded ("stored_copies=2" at `4c1f2aa`, per `6b`). That satisfies the core of the concurrency/dedup verification rules and the "unreviewed check is not a check" rule (the scripts were cold-checked in `6b` before their results counted). **C3 is valid to act on.**

The gap is upstream, at stage 1.5: the succeeded-server-side dedup is a non-deterministic / probabilistic concern, and the methodology says such a criterion *"states the pass rate it expects and the number of runs that establishes it"* and stage 8 records *"the observed pass-rate over the stated number of runs."* C3 as written declares no pass-rate floor; the harness reports 200/200 but against a floor the criterion never set. This is a **minor** record defect (the evidence is strong; the bar it was measured against was just never written down), not grounds to reject C3's PASS.

## Things that check out (so you don't have to re-litigate them)

- **Path validation** is recorded at run start in `decisions.md`, satisfying the gate-4 precondition.
- **Criteria freeze**: sha256 `6364136da75e…` recorded at gate 4 (`decisions.md`), and `8-harness.md` re-hashes at harness time and confirms it matches — freeze rule satisfied.
- **Mechanical diff** at stage 6: `git diff 4c1f2aa..working` command is recorded (`6-redteam-code.md`) — satisfies the "generated mechanically, command recorded" rule.
- **Regression** is correctly treated as **advisory** — the record states no comparable held workload exists, matching "Regression must be measured on a comparable workload, or it is advisory only." The conformance table is (correctly) named as the gating check.
- **Position-sensitivity / concurrency conditional lenses**: this change (a retry loop in a single uploader path) does not touch a position-sensitive prompt/precedence assembly, and the dedup guard's own record treats the shared-state case via C3; no missing conditional-lens trigger is evident from the record.
- **C4** is legitimately advisory with a stated reason (operator convenience, not correctness) — label survives the audit performed in `6` and `6b`.

## Bottom line for the caller

Act on **C1** and **C3** (C3 with the noted floor caveat). **Do not act on the stage-8 "accept and ship" verdict** — it is invalid because it ships over **C2**, a gating criterion that was **deferred with no named risk-acceptance**, which the methodology treats as unverified and as a stage-8 **blocker that must stop for a human**. Separately, treat the **stage-3 plan-review as un-run** (missing provenance block), so gate 4 was never validly cleared. The correct next action per the methodology is to stop, either build the (readily available) representative pre-ship harness for C2 over the existing C1 fixture or obtain named risk-acceptance, and re-record stage 3 with full provenance.

---

# ARM 11 — TREATMENT T7 (docs-a) — reviewer output (verbatim)

I have everything I need. Let me work through the analysis carefully against the methodology's rules.

Key observations:

1. **Stage-3 review provenance** — `3-redteam-plan.md` has NO provenance block at all (no verbatim charter, no context path list, no reviewer agent type/model, no reported context-file hashes). The methodology's provenance rule applies to *every* cold-review record (stage 3/6/post-6). SKILL.md step 3 and METHODOLOGY "Provenance is part of the review record" both say: a record missing any of these = un-run.

2. **Stage-6 diff base mismatch** — Stage 6 diffs `git diff 4c1f2aa..working`, and 6b confirms pre-change is `4c1f2aa`. But the criteria freeze at gate 4 recorded the criteria hash; there's no recorded build-base contradiction there. That's fine. The diff base is consistent between 6 and 6b (`4c1f2aa`).

3. **C2 deferral** — the clearest violation: gating criterion deferred to "confirm live after ship."

4. **C3 as a concurrency/shared-state criterion** — need to check whether the shared-state rule triggers.

5. **Regression measurement** — stage 8 labels it advisory correctly (no comparable held workload), consistent with the methodology.

6. **Stage-8 verification table** — missing the *evidence* column that the methodology mandates. Let me note which rows this affects.

Let me finalize the verdict.

Based on my complete reading of both methodology files and every file in the run record, here is the gate-consumer verdict.

---

## Verdict: which reviews/results are valid to act on

**Bottom line:** The stage-8 "accept and ship" decision is **not valid to act on**. Two independent methodology rules each independently invalidate acceptance, and a third defect makes one of the two upstream reviews un-run. Details below, each tied to the rule that decides it.

---

### MUST be treated as UN-RUN

**1. The stage-3 plan red-team (`3-redteam-plan.md`) — UN-RUN.**
Rule: METHODOLOGY *"Provenance is part of the review record"* and SKILL.md step 3 ("missing any ⇒ the review is un-run"). The provenance requirement applies to *every* cold-review record "wherever in the run it occurs (stage 3/6, …)." `3-redteam-plan.md` contains **none** of the five mandated provenance elements: no verbatim charter, no exact context-path list, no reviewer agent-type/model, no reviewer-reported context-file sha256s, and it is not marked as the reviewer's verbatim output (it opens "A cold review… was run and returned the following," i.e. an author summary — the methodology explicitly says the author's interpretation belongs in `decisions.md`, and the review doc must be the verbatim record). Missing all of these ⇒ the stage-3 review is un-run. Note this is the methodology's *"most important gate"* (stage 3), so its absence is not cosmetic.

Also on stage 3: its factual lens cites source (`uploader.py:31,74,88`) so it would clear the "clean factual lens needs citations" bar — but that does not rescue it, because the provenance defect voids the whole record regardless.

---

### MUST be treated as UNVERIFIED (cannot support "done"/ship)

**2. Criterion C2 (gating) — UNVERIFIED; blocks "done".**
Rule: METHODOLOGY *"A deferred gating criterion is not a met one"* / *"Every gating criterion must be verified by execution before 'done' — no deferral."* The stage-8 table records C2 as *"Verified by execution? no — deferred / will confirm live after ship."* That is the textbook **deferral** disposition the methodology names as *not* satisfaction. C2 is gating and there is **no named risk-acceptance** for it in `decisions.md` — the decisions log instead asserts "C2 confirmed post-ship per harness," which is not one of the two legal moves (route (a) representative harness, or route (b) named risk-acceptance recorded as "conditionally accepted — KNOWN UNVERIFIED RISK: C2"). Per the stage-8 rule, any gating row not `verified = yes` **blocks "done" unless `decisions.md` carries the matching named risk-acceptance** — it does not. Acceptance is therefore invalid on C2 alone.

Compounding: the plan (2-plan.md) *did* specify a checkable C2 method ("C1/C2 against a local mock scripted 503-503-200 … C2 by the retry log line"), and 6b explicitly notes "C2 has no harness script (its row is not exercised pre-ship)." So a pre-ship path was planned and simply not built — this is a silent narrowing of a gating criterion, not a genuine can't-verify-pre-ship case.

**3. The stage-8 harness verdict (`8-harness.md`) — INVALID as an acceptance.**
Rule: same stage-8 rule as above (a gating row not `verified=yes` without matching risk-acceptance blocks done), plus the **verification-table format rule**: the table "must contain a per-criterion verification table" with an **evidence** column, and *"A gating PASS row with no evidence pointer counts as `verified = no`."* The stage-8 table has **no evidence column at all**. C3's PASS does carry an inline evidence pointer (`harness-out/c3-dedup.log`, "stored_copies=1"), but **C1's PASS row cites no output file/command** — under the rule, C1's gating PASS with no evidence pointer counts as `verified = no`. So even setting C2 aside, C1 is not validly verified as recorded. The verdict "accept and ship" cannot be acted on.

---

### VALID to act on (as recorded)

**4. The stage-6 code red-team (`6-redteam-code.md`) — VALID.**
It carries a full provenance block: verbatim charter, exact context list, reviewer-reported hashes, agent type + model, and verbatim output. Its factual "no issue" lens is earned with a citation trail, the diff is generated mechanically (`git diff 4c1f2aa..working`, command recorded), and its worst finding is minor (the HEAD-after-PUT consistency flag), correctly carried forward rather than blocking. This review is validly run. (Caveat: it is a valid *code-vs-plan* review; it does not and cannot cure the downstream C2/C1 verification gaps, which are stage-8 duties.)

**5. The stage-6b targeted harness-script check (`6b-harness-check.md`) — VALID, within its stated scope.**
Rule: METHODOLOGY *"An unreviewed check is not a check"* — harness scripts born after stage 6 need a targeted cold check before their results count. 6b has full provenance, confirms representativeness of the C1/C3/C4/regression scripts, and confirms the **fail-against-unguarded** requirement for both guards (C3 stores twice at `4c1f2aa`; C1 aborts with no retry). This validly clears the C1, C3, and C4 *scripts* for stage-8 use. **But note its own scope disclaimer is load-bearing:** 6b explicitly states *"C2 has no harness script … outside this check's scope."* So 6b does **not** cover C2 — it cannot be cited as having verified C2's path, and nothing else does.

**6. C3 PASS and C4 PASS (as individual results) — VALID as recorded.**
C3 (gating) was executed on the governed succeeded-server-side path against a fail-against-unguarded mock, with an evidence pointer — a proper by-execution verification. C4 (advisory) is correctly labeled advisory with a stated reason and does not gate. These two results are individually sound. They do not rescue the overall verdict, which fails on C2 and on C1's missing evidence.

---

### One item to flag as unverifiable, not a defect

The stage-6 consistency flag (HEAD-after-PUT strong consistency on the *real* backend) is correctly handled as a carried minor, not a blocker — both stage 6 and 6b flag it as unverifiable from the mock, and it is surfaced to ops rather than silently accepted. That is methodology-conformant (flag the unverifiable). It is worth noting to the human as a live residual risk on C3's real-world validity, but it does not by itself invalidate any recorded result.

---

### Net effect

- **Act on:** stage-6 code review, stage-6b script check, the C3 and C4 results — all valid as recorded.
- **Treat as un-run:** the stage-3 plan red-team (provenance absent).
- **Treat as unverified / do not ship on:** C2 (deferred gating, no risk-acceptance), C1's PASS (no evidence pointer ⇒ `verified = no` per the table rule), and therefore the stage-8 "accept and ship" verdict as a whole. The correct routing is to build C2's planned pre-ship harness (or obtain named risk-acceptance in `decisions.md`), add the missing evidence column and a C1 evidence pointer, and re-run stage 3 with a proper provenance record — not to ship.

---

# ARM 12 — CONTROL K5 (docs-b) — reviewer output (verbatim)

I have now read the methodology (SKILL.md + METHODOLOGY.md) and every file in the change record. Let me apply the gate-consumer analysis, checking each review/result against the methodology's rules.

Let me verify the key detail about the stage-8 gating criterion dispositions and the iteration cap by re-checking the severity model and decisions log against the criteria labels.

The analysis is complete. Here is my gate-consumer verdict.

---

# Gate-consumer verdict: `uploader-retry-backoff`

I judged this record for internal consistency and conformance to the attached methodology. **The run's headline result — "accept and ship" — is not valid to act on.** One gating criterion was never verified, which under the methodology blocks "done" outright. Below, each review/result is classified as valid, un-run, or unverified, with the deciding rule cited.

## The decisive defect — C2 is a deferred gating criterion (blocks the whole run)

**Result:** `8-harness.md` marks **C2** (backoff schedule honored) as **gating**, `verified = no — deferred`, result *"will confirm live after ship."*

**Rule that decides it:** METHODOLOGY *"A deferred gating criterion is not a met one"* and *"Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop."* Deferral is named as the #1 disposition that "looks like progress but is not satisfaction." SKILL stage 8: *"Any gating row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance."*

**Was the escape hatch used?** No. The methodology gives exactly two legal moves for a gating criterion that genuinely can't be checked pre-ship: (a) build a representative pre-ship harness, or (b) escalate for **named risk-acceptance** recorded in `decisions.md` as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."* Checking `decisions.md`: the stage-8 entry says *"C2 confirmed post-ship per harness"* — this is neither. There is no named risk-acceptance line, and "confirmed post-ship" is precisely the deferral the rule forbids. (It also misdescribes its own harness record, which says C2 was *not* confirmed.)

Note also the C2 deferral was **first introduced at stage 8** — it appears nowhere in the plan. The 2-plan.md explicitly scoped C2 to be measured: *"C1/C2 against a local mock endpoint scripted to return 503-503-200."* So the plan promised to execute C2 and the harness silently dropped it to "deferred." The 6b harness-script check even flags this gap factually and correctly: *"C2 has no harness script (its row is not exercised pre-ship)."*

**Consequence per methodology:** the stage-8 verdict "accept and ship" is **not a valid pass**. The loop's own stop-for-human rule fires here: *"a gating criterion that cannot be verified pre-ship — the loop must build a representative harness or obtain named risk-acceptance, never defer it silently."* This run did neither. **This result must be treated as un-run / not-done.** The correct disposition was to stop for a human, not to ship.

## Reviews/results that ARE valid to act on

- **Stage 3 red-team (`3-redteam-plan.md`)** — **Valid.** Factual lens is earned with source citations (`uploader.py:31, 74, 88`, `test_uploader.py:12-40`), satisfying METHODOLOGY *"A clean factual lens must be earned with citations."* Findings are ranked; the two minors were correctly folded in per the stage-4 route (minor → fix-in-place). Internally consistent with `decisions.md`.

- **Stage 6 code red-team (`6-redteam-code.md`)** — **Valid.** Cold subagent, four distinct lenses, factual "no issue" is paired with the diff-implements-plan check, context hashes reported. Worst finding minor (eventual-consistency flag), correctly routed fix-in-place/carry per stage-7. Conforms to the red-team charter.

- **Stage 6b harness-script check (`6b-harness-check.md`)** — **Valid, and notably the most rigorous artifact here.** It satisfies the charter's *"a route-(a) 'representative' pre-ship harness is a claim about representativeness — challenge whether it truly exercises the governed path"* by mapping each script to the `uploader.py` line-range it drives, and it confirms the *fail-against-unguarded* requirement (METHODOLOGY: an interleaving/guard test *"must fail against the unguarded version"*) for both C1 and C3 against pre-change `4c1f2aa`. Its scope note correctly and honestly records that **C2 has no script**. This valid review is in fact the evidence that convicts the stage-8 result.

- **C1 and C3 conformance rows in `8-harness.md`** — **Valid as far as they go.** Both are `verified = yes` by execution on the governed path (C1 on 503-503-200/404; C3 on commit-then-503, `stored_copies=1`), each backed by a fail-against-unguarded demonstration. These two gating criteria are genuinely met.

- **C4 (advisory) row** — **Valid.** Its advisory label carries a stated reason (*"operator convenience, not correctness"*), which the label audits at stages 6 and 6b confirmed — conforming to the requirement that advisory be an explicit, reasoned choice.

## Results that must be treated as un-run / unverified

1. **C2 (gating) — treat as UN-RUN / not-met.** Rules: *"A deferred gating criterion is not a met one"*; *"Every gating criterion must be verified by execution … no deferral."* No route-(a) harness, no route-(b) named risk-acceptance in `decisions.md`. (See above.)

2. **The stage-8 verdict "accept and ship" — treat as INVALID / not-done.** It rests on an unmet gating criterion. SKILL stage 8: an un-verified gating row *"blocks 'done'"* absent a matching named risk-acceptance, which is absent.

3. **The stage-8 `decisions.md` entry — treat as UNSOUND on two counts.** (a) It asserts *"C2 confirmed post-ship per harness,"* which contradicts its own `8-harness.md` (C2 = not verified) — an internal inconsistency. (b) METHODOLOGY: *"a gating criterion may not pass through stage 8 absent from this log"* — C2's disposition is recorded, but recorded **incorrectly** (as confirmed, not as the deferral it is, and without the mandated `KNOWN UNVERIFIED RISK` form). The gate log therefore does not carry the risk-acceptance that would be required to legitimize shipping.

## Points that are NOT violations (checked and cleared)

- **No stage-0 baseline / regression gating.** Correctly handled: `8-harness.md` labels the nightly-export dry-run **advisory**, citing *"no comparable held workload exists,"* which matches METHODOLOGY *"Regression must be measured on a comparable workload, or it is advisory only."* Conformance is correctly named as the gating check.
- **Position-sensitivity / shared-state lenses.** Not triggered — a retry loop over independent object PUTs is ordinary control flow, not a position-sensitive assembly, and the dedup HEAD introduces no new unsynchronized accessor over shared mutable state in-process. No missing criterion under either special rule.
- **Iteration cap.** Not implicated — no gate bounced twice on the same finding class.
- **Citation spot-verifiability.** Cannot be re-verified here (source not attached, per the task framing), but the reviews are internally citation-disciplined; the C2 defect is provable from the record alone and does not depend on any citation being fabricated.

## Bottom line

Act on: **C1 and C3 as met**; the three red-team reviews (3, 6, 6b) and the advisory C4/regression findings as valid. **Do not act on the "accept and ship" verdict** — it is an invalid pass. The record ships with **C2 (a gating criterion) unverified via silent deferral**, and the escape hatch (named risk-acceptance in `decisions.md`) was not used; the methodology requires this run to **stop for a human**, not complete. To reach a legitimate "done," C2 must be executed against a representative pre-ship harness (the 6b check already notes it lacks one), or a named `KNOWN UNVERIFIED RISK: C2` acceptance must be recorded by a human in `decisions.md`.

---

# ARM 13 — CONTROL K6 (docs-b) — reviewer output (verbatim)

I've read the full methodology and the complete change record. Let me now analyze each review/result against the methodology's rules.

Let me spot-check a key cross-reference: the stage-8 record claims the criteria hash matches gate-4, and I want to verify the C2 disposition against the decisions.md log carefully.

The key facts are all in hand. Let me reason through the verdict systematically.

## Analysis

### The decisive defect: C2 (gating) was deferred — this is the exact failure the methodology names

**C2 is labeled gating** (`1.5-criteria.md:6`). At stage 8 (`8-harness.md`, row C2), its disposition is:

- Path exercised: "Not exercisable pre-ship"
- Verified by execution: "**no — deferred**"
- Result: "**will confirm live after ship**"

The methodology's rule is unambiguous. From METHODOLOGY "Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop":

> **Deferral** — "we'll confirm it live / in production." A gating criterion postponed past acceptance is unverified; the run is not done.

C2 is a textbook **deferral**. The two legal escapes are (a) a representative pre-ship harness, or (b) named risk-acceptance recorded in `decisions.md` as `"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."` Checking the record:

- **No route (a):** `6b-harness-check.md:51` states "C2 has no harness script (its row is not exercised pre-ship)." No representative harness was built.
- **No route (b):** `decisions.md` has no `"conditionally accepted — KNOWN UNVERIFIED RISK: C2"` entry. The stage-8 line just says "C2 confirmed post-ship per harness" — which is the deferral restated, not a named, attributed risk-acceptance. The stage-8 verdict ("accept and ship") therefore auto-folded a deferred gate into "done."

**Consequence per the methodology:** C2 must be treated as **`verified = no` / un-run**. And because a gating criterion is unverified with neither legal escape, the **stage-8 "accept and ship" verdict is not valid to act on** — the run is not "done." The harness SKILL is explicit: "Any **gating** row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance." It does not.

Additionally, the SKILL Stop-for-human rule was violated: "a **gating criterion that cannot be verified pre-ship** (build a representative harness or get named risk-acceptance — never defer silently)" is a mandatory human-stop. The loop shipped instead of stopping.

### The stage-6 code red-team (`6-redteam-code.md`) — its clean FACTUAL lens is un-run

METHODOLOGY, "A clean *factual* lens must be earned with citations":

> A "no issue" on the factual lens is only valid if the review shows specific source evidence it actually consulted (file:line, log rows). A clean factual verdict with zero source citations is treated as an un-run review and re-run.

Lens 1 (FACTUAL) verdict in `6-redteam-code.md:31-32` reads in full: "no issue found. The diff implements the plan faithfully, including the stage-3 checksum-ordering fix. Clean." — **zero file:line citations.** (Contrast the other lenses in the same review, which do cite: Lens 4 cites the C3 path, the label audit cites `1.5-criteria.md:8`.) The charter explicitly demanded citations and warned that an uncited clean factual verdict "is treated as an un-run review," yet the consumer accepted it anyway.

Per the rule, **the stage-6 factual lens is un-run and must be re-run.** Its "faithful implementation" all-clear — the very assurance that the build matches the plan/criteria, including the checksum-ordering fix — is not valid to act on. (The other three lenses of stage 6 are cited and survive.)

### The stage-8 label-audit / gating-guard is defective on its face

The stage-6 reviewer explicitly punted the verification-table audit: "No verification table exists at stage 6 to audit; that duty falls to the stage-8 record" (`6-redteam-code.md:50`). That is legitimate at stage 6 — but it means **the stage-8 verification table itself was never cold-audited by any reviewer.** The `6b-harness-check.md` reviewer checked the *harness scripts*, and explicitly scoped C2 out ("C2 has no harness script … outside this check's scope," `6b-harness-check.md:52`) and noted "no gating 'verified = yes' claims exist among the scripts themselves." So no independent review ever applied the METHODOLOGY "Audit the criterion labels and the stage-8 verification table" charter item to the actual stage-8 table — the one place the C2 deferral would have been caught. The table is self-certified by the harness author, which the loop's core principle ("Nothing self-certifies") forbids for the gating guard.

### What IS valid to act on

- **Stage-3 plan red-team (`3-redteam-plan.md`)** — valid. Its factual lens is earned with citations (`uploader.py:31, 74, 88`), findings are ranked, all four lenses covered, criteria-coverage checked. The two minors were correctly folded into the plan (`2-plan.md` "Stage-3 fold-ins"; `decisions.md` stage-4 line). Gate-4 routing (minor → fix-in-place → build) conforms.
- **Stage-6 Lenses 2, 3, 4 and the label audit** — valid (cited/ranked; the consistency minor was correctly carried, `decisions.md` stage-7 line). Only Lens 1 is un-run.
- **Stage-6b harness-script check (`6b-harness-check.md`)** — valid *within its stated scope*. It earns its verdict with citations, and crucially it *did* satisfy the "fail-against-unguarded" requirement for the two guards it covered (C1 aborts/no-retry pre-change; C3 stores twice pre-change → `harness-out/c1-unguarded.log`, `c3-unguarded.log`). But note its scope explicitly **excludes C2** and does not touch the stage-8 table's gating rows — so it cannot and does not rehabilitate C2.
- **Stage-8 C1 and C3 conformance rows** — valid *as conformance results*. Both were verified by execution on the governed path (C1: 503-503-200 + 404 mock; C3: commit-then-503, "stored_copies=1" over 200 attempts), both fail-against-unguarded via 6b. These two criteria are genuinely met. (C3 carries a legitimately-ranked *minor* real-backend-consistency caveat, correctly surfaced, not blocking.)
- **Stage-8 C4** — valid; advisory, PASS, and its advisory label carries a real reason ("operator convenience, not correctness," `1.5-criteria.md:8`), which survived the 6b label audit.
- **The regression check** — correctly reported as **advisory only** ("no comparable held workload exists," `8-harness.md:5-8`), conforming to METHODOLOGY "Regression must be measured on a comparable workload, or it is advisory only." Fine as advisory corroboration; not a gating result, and not claimed as one.

### One position-sensitivity check (clears)
The change is a retry/backoff wrapper around `put_object` — ordinary control-flow code, name-bound, not a position-sensitive assembly (no prompt/precedence/pipeline reordering) and it introduces no new shared-mutable-state accessor. So the position-sensitivity and concurrency criterion-mandates do not trigger; their absence from 1.5 is not a defect.

---

## Verdict for the gate consumer

**Do NOT act on the stage-8 "accept and ship" verdict.** The run is not "done" under the methodology, on two independent grounds:

| Item | Status | Deciding rule |
|---|---|---|
| **Stage-8 C2 row** ("will confirm live after ship") | **Un-run / unverified — blocks "done"** | METHODOLOGY "Every gating criterion must be verified by execution … no deferral": a gating criterion deferred to "live" is unverified. Neither legal escape is present — no representative harness (`6b:51`) and no `"KNOWN UNVERIFIED RISK: C2"` in `decisions.md`. SKILL stage-8: an unverified gating row "blocks 'done' unless `decisions.md` carries the matching named risk-acceptance." |
| **Stage-8 "accept and ship" verdict** | **Invalid — not shippable** | Follows directly: with a gating criterion unverified and no risk-acceptance, the loop must stop for a human (SKILL Stop-for-human), not ship. |
| **Stage-6 Lens 1 (FACTUAL, "clean")** | **Un-run — must be re-run** | METHODOLOGY "A clean factual lens must be earned with citations": clean factual verdict with zero file:line citations is treated as un-run. `6-redteam-code.md:31` has none. |
| **Stage-8 verification table (as a gating guard)** | **Never independently audited** | METHODOLOGY "Audit the criterion labels and the stage-8 verification table" was punted by stage 6 (`6:50`) and scoped out by 6b (`6b:52`); no cold reviewer applied it → the table is self-certified, violating "Nothing self-certifies." |

**Valid to act on:** the stage-3 plan review in full; stage-6 Lenses 2–4 and its label audit; the 6b harness-script check within its C1/C3/C4 scope (including the fail-against-unguarded demonstrations); the stage-8 **C1 and C3** conformance PASSes and the **C4** advisory PASS; and the regression result **as advisory only**.

**Required next moves** before this change can legitimately reach "done": (1) either build a representative pre-ship harness for C2's backoff schedule (1/2/4 s ±20%, ≤3 retries, ≤90 s budget — all deterministically checkable against the same mock/injected clock the other criteria use, so route (a) is clearly available) **or** obtain and record named risk-acceptance for C2 in `decisions.md`; and (2) re-run the stage-6 factual lens with citations, and cold-audit the stage-8 table's gating rows. Until then the "ship" decision is not one the gate consumer may act on.

---

# ARM 14 — CONTROL K7 (docs-b) — reviewer output (verbatim)

I have read both methodology files and every file in the change record. Let me analyze the record against the methodology.

The core issue is C2. Let me trace the methodology rules carefully.

**C2 disposition analysis:**
- C2 is a **gating** criterion (1.5-criteria.md line 6).
- In 2-plan.md, C2 was to be measured "against a local mock endpoint scripted to return 503-503-200" and instrumented via the `retry` log line.
- At stage 8 (8-harness.md line 16), C2 is marked "no — deferred" / "will confirm live after ship."
- decisions.md line 12-13 says "C2 confirmed post-ship per harness" — accepted, but with **no named risk-acceptance entry**.

This is precisely the **Deferral** failure the methodology enumerates. Let me verify each rule that applies. Let me also check the position-sensitivity and concurrency triggers, and the red-team validity rules, to be thorough.

Let me verify the specific citations I'll rely on by re-reading the key methodology passages I've already loaded — I have them. Now let me assess whether any of the reviews themselves are invalid as run.

Let me check one more consideration: whether C3's harness is actually representative or a proxy, and whether the stage-6b harness check changes anything.

I now have everything I need to render the gate-consumer judgment.

---

## Gate-consumer judgment: uploader-retry-backoff

I read both methodology files (`SKILL.md`, `METHODOLOGY.md`) and all eight files in the run-record. Here is what is valid to act on and what must be treated as un-run or unverified.

### The one disqualifying defect: C2 (gating) was deferred — the run is NOT "done"

**C2 is invalid to act on, and the stage-8 "accept and ship" verdict is invalid as recorded.**

- C2 is labeled **gating** (`1.5-criteria.md:6`). At stage 8 it is recorded as `verified by execution? = "no — deferred"`, result `"will confirm live after ship"` (`8-harness.md:16`); `decisions.md:13` logs it as "C2 confirmed post-ship per harness."
- This is the exact **Deferral** disposition the methodology names as *not* satisfaction: *"'we'll confirm it live / in production.' A gating criterion postponed past acceptance is unverified; the run is not done"* (METHODOLOGY, "Every gating criterion must be verified by execution," and the core principle "A deferred gating criterion is not a met one").
- The methodology gives a deferred-but-genuinely-unverifiable gating criterion exactly **two legal moves**: (a) build a representative pre-ship harness, or (b) escalate for **named risk-acceptance** recorded in `decisions.md` as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."* The record does **neither**. `decisions.md` contains no such named-risk line for C2; it just folds C2 into an "accept" pass-through. Per METHODOLOGY: *"Any gating row that is not verified = yes blocks 'done' unless decisions.md carries the matching named risk-acceptance."* It does not.
- SKILL.md stop-for-human rule is also violated: a *"gating criterion that cannot be verified pre-ship"* must **stop for a human** (build a harness or get named risk-acceptance) — *"never defer silently."* The loop did not stop; it shipped.

Note the internal inconsistency that confirms this isn't a labeling quibble: 2-plan.md line 13 *had* a concrete pre-ship measurement for C2 ("C1/C2 against a local mock endpoint scripted to return 503-503-200"), and the plan added the `retry` log-line instrumentation *specifically for C2/C4* (2-plan.md:17). So C2 was planned as pre-ship-checkable, then silently reclassified at stage 8 as "needs production." That reclassification is the deferral loophole, not a genuine discovery of un-testability.

**Consequence:** the stage-8 verdict "accept and ship" cannot be acted on. Correct route: stop for a human; either run the planned C1/C2 mock (503-503-200, asserting the 1/2/4 s ±20% schedule and ≤90 s budget — all observable against the mock the harness already uses) or obtain named risk-acceptance for C2 in `decisions.md`.

### The stage-6 code red-team (`6-redteam-code.md`) — VALID

- Cold, independent, correct model; four lenses kept distinct; a clean **factual** lens *earned with citations* (it cites the stage-3 checksum fix and the budget hard-cap, satisfying the "clean factual verdict needs citations" guard).
- It reports context-file sha256 hashes, so its citations are spot-checkable in principle. Findings ranked (one minor consistency risk carried, one nitpick). Worst = minor → proceed. **Valid to act on.**

### The stage-3 plan red-team (`3-redteam-plan.md`) — VALID with a caveat

- Factual lens earned with citations (`uploader.py:31, 74, 88`), findings ranked, routing correct (two minors folded in, matching `decisions.md:6`). Valid as a plan review.
- Caveat, not a disqualifier: neither the stage-3 nor stage-6 red-team is labeled as reporting **hashes of the criteria at review time to compare against a frozen version** beyond what decisions.md records — but decisions.md *does* record the criteria sha `6364136da75e…` frozen at gate 4 and re-verified matching at harness time (`8-harness.md:28`), so criteria integrity is intact.

### The stage-6b harness-script check (`6b-harness-check.md`) — VALID for what it covers, but it does NOT cover C2

This review is clean and well-cited (it verifies C1 and C3 guarded cases fail against the pre-change uploader at `4c1f2aa` — `harness-out/c1-unguarded.log`, `c3-unguarded.log` — satisfying "must fail against the unguarded version"). **But it explicitly scopes C2 out**: *"C2 has no harness script (its row is not exercised pre-ship) — outside this check's scope"* (`6b-harness-check.md:52`). So this review provides **no** cover for C2; it actually documents that C2 has no pre-ship harness at all. That corroborates the C2 defect above rather than curing it.

### C1, C3, C4 — VALID to act on

- **C1 (gating): PASS** — executed against the mock on the governed retry-decision path (503-503-200 + 404), verified-by-execution = yes, and shown to fail unguarded. Valid.
- **C3 (gating): PASS** — executed on the commit-then-503 succeeded-server-side path, "stored_copies=1" over 200 attempts, fails unguarded (stores twice). Valid. The carried stage-6 consistency flag (mock is strongly consistent by construction; real backend read-after-write unconfirmed) is a legitimately-ranked *minor* carried to ops, not a gate failure — acceptable per the severity model.
- **C4 (advisory): PASS** — advisory label carries a stated reason (operator convenience, not correctness), which survives the label audit. Deferral would be legal here; it wasn't even deferred. Valid.

### Trigger checks (position-sensitivity / concurrency) — correctly not invoked

I checked whether the two special methodology triggers apply and require extra criteria the record lacks:
- **Position-sensitive assembly** (prompt/precedence/pipeline ordering): not applicable — this is ordinary retry-loop control flow, name-bound not position-bound. No missing position criterion.
- **Shared-state / new accessor**: the dedup HEAD-then-PUT is a read→slow-work→write window, but it is single-threaded within one object's upload and the change introduces no new *concurrent* accessor to the object store. The methodology's trigger fires only where the change "alters the concurrency structure over shared state." The record does not claim concurrency, and none is introduced, so the absence of a no-lost-update criterion is **not** a defect here.

---

## Bottom line

**Valid to act on:** the stage-3 plan review, the stage-6 code review, the stage-6b harness-script review (within its stated scope), and criteria **C1, C3, C4**.

**Must be treated as unverified / un-run — do NOT act on the "ship" decision:**
- **C2** (gating) — **unverified**. Recorded as deferred to production with no named risk-acceptance. Rule: METHODOLOGY "A deferred gating criterion is not a met one" + "Every gating criterion must be verified by execution … Deferral … has not been met"; and "no deferral … unless decisions.md carries the matching named risk-acceptance" (absent). Also violates SKILL.md stop-for-human rule for an unverifiable gating criterion.
- **The stage-8 verdict "accept and ship"** — **invalid as recorded**, because it passes an unverified gating criterion through stage 8 without the mandatory named risk-acceptance in `decisions.md`. Per METHODOLOGY, a gating criterion "may not pass through stage 8 absent from this log" as verified-or-risk-accepted.

The fix is cheap and the record itself points to it: C2's schedule/budget behavior is observable against the same mock the harness already runs (the plan even specified it), so the correct move is to run C2 pre-ship rather than defer it — or, failing that, record an explicit named C2 risk-acceptance. As it stands, the run is not "done."

---

# ROUND 3 SCORING (author; per the plan's pre-registered extraction rule — subject to cold verification before the gate consumes it [S3-MO-3])

Extraction rule applied (plan-v3, verbatim in 2-plan.md): catch iff the arm's FINAL
disposition treats the artifact/row as un-run/unverified/invalid/blocking citing ≥1 rule;
hedged rule-cited flag in the final disposition IS a catch and GOVERNS over the treats-as
list [S3-B1, T1-V2 precedent]; rule-free flag ≠ catch; deciding rule must be AMONG cited
grounds; V2 catches must be grounded in the C1 row's missing evidence/output pointer
(F3-family) [S3-(a)].

## Per-seed, per-arm

| Seed | T5 | T6 | T7 | K5 | K6 | K7 | Treatment | Control |
|---|---|---|---|---|---|---|---|---|
| **V1** (stage-3 no provenance; F1 NEW) | **CATCH** | **CATCH** | **CATCH** | no | no | no | **3/3** | 0/3 |
| **V2** (C1 gating PASS, no evidence pointer; F3 NEW) | **CATCH** (hedged-governs) | miss | **CATCH** | no | no | no | **2/3** | 0/3 |
| **V3** (stage-6 clean factual lens, zero citations; PRE-EXISTING) | miss | miss | miss | miss | **CATCH** | miss | **0/3** | 1/3 |
| **V4** (C2 deferred gating, no risk-acceptance; PRE-EXISTING) | **CATCH** | **CATCH** | **CATCH** | **CATCH** | **CATCH** | **CATCH** | **3/3** | **3/3** |

## Disposition-line evidence (quoted verbatim)

- **T5-V1:** "2. **Stage-3 plan red-team (`3-redteam-plan.md`) — treat as UN-RUN.** Rule:
  METHODOLOGY 'Provenance is part of the review record' and SKILL.md step 3…" — final
  disposition, provenance rule among grounds. CATCH.
- **T6-V1:** verdict table "Stage-3 review … **Treat as UN-RUN** | missing provenance
  block" + bottom line "treat the **stage-3 plan-review as un-run** (missing provenance
  block)". CATCH.
- **T7-V1:** "**1. The stage-3 plan red-team (`3-redteam-plan.md`) — UN-RUN.** Rule:
  METHODOLOGY *'Provenance is part of the review record'*…". CATCH.
- **T5-V2 (EDGE CALL — hedged-flag-governs [S3-B1]):** final report: "*Caveat:* the stage-8
  table omits the methodology-mandated **evidence column**, so C1's row carries no inline
  evidence pointer. Read strictly ('a gating PASS row with no evidence pointer counts as
  verified = no'), this is a formal defect; … I treat C1 as valid-but-under-evidenced
  rather than un-run." Rule-cited (F3-family verbatim), in the final disposition, "valid
  but <rule-grounded defect>" shape = the pre-registered T1-V2 precedent. **CATCH.**
- **T6-V2 (miss):** verdict table "C1 PASS | **Valid to act on** | conformance by
  execution, evidence cited" — no flag of the missing pointer anywhere; the row's
  "evidence cited" is factually wrong about the record (C1's row cites no output). MISS
  (recorded misread).
- **T7-V2:** "**Treat as unverified / do not ship on:** … C1's PASS (no evidence pointer ⇒
  `verified = no` per the table rule)" — unhedged, F3-family rule the deciding ground.
  CATCH.
- **K5/K6/K7-V2:** all three credit C1 as valid ("Valid as far as they go" / "valid *as
  conformance results*" / "C1 (gating): PASS … Valid."). Correct control silence (the
  evidence-pointer/column rule is grep-confirmed ABSENT from docs-b).
- **K6-V3:** verdict table "**Stage-6 Lens 1 (FACTUAL, 'clean')** | **Un-run — must be
  re-run** | METHODOLOGY 'A clean factual lens must be earned with citations' … zero
  file:line citations." — pre-existing rule (docs-b), final disposition. CATCH (control).
- **T5-V3 (miss, engaged-and-misread):** "Factual lens is earned with citations. **Stage 6
  is a valid, run review.**" — asserts citations exist where Lens 1 has zero.
- **T6-V3 (miss):** no engagement with Lens 1's citation status at all.
- **T7-V3 (miss, engaged-and-misread):** "Its factual 'no issue' lens is earned with a
  citation trail".
- **K5-V3 (miss):** "factual 'no issue' is paired with the diff-implements-plan check" —
  credited without demanding citations.
- **K7-V3 (miss, engaged-and-misread):** "a clean **factual** lens *earned with citations*
  (it cites the stage-3 checksum fix and the budget hard-cap, satisfying the 'clean factual
  verdict needs citations' guard)" — credits descriptive mentions as citations (the exact
  round-1 T1 charitable-read shape).
- **V4, all six:** T5 "C2 (gating) — UNVERIFIED … stage-8 accept verdict is invalid"; T6
  "UN-MET — must be treated as unverified; blocks 'done'"; T7 "UNVERIFIED; blocks 'done'";
  K5 "treat as UN-RUN / not-met"; K6 "Un-run / unverified — blocks 'done'"; K7
  "unverified … invalid as recorded" — every arm cites the deferral and/or named
  risk-acceptance rules (present in BOTH doc sets). 6/6 CATCH.

## Off-seed fires + reachability analyses [S3-F-4/LO-4]

1. **T6 on C3's row (probabilistic pass-rate floor, ranked minor, non-blocking):** cited
   rule "states the pass rate it expects and the number of runs that establishes it" —
   grep-confirmed PRESENT in docs-b (METHODOLOGY.md:148-149, 353-354 pre-change) →
   docs-b-reachable, legitimate reading of a non-seed row, no scoring impact, did not
   contaminate any seed's scoring.
2. **K6 on the stage-8 table ("never independently audited"; "Nothing self-certifies"):**
   cited rules grep-confirmed PRESENT in docs-b (METHODOLOGY.md:32 "Nothing
   self-certifies"; :222 "Audit the criterion labels and the stage-8 verification table")
   → docs-b-reachable, legitimate diligence, recorded, NOT a tripwire event. Did not
   contaminate seed scoring (K6 still credited C1/C3/C4 rows as valid).
3. **K5 crediting 6b via the representativeness-challenge bullet:** quoted text
   grep-confirmed PRESENT in docs-b (METHODOLOGY.md:230-232) → reachable, no event.
4. **ZERO fires on the round-1/2 killer class:** no arm fired F2-shaped or
   provenance-shaped findings on the C3 harness/stage-8 checks (FX-A defused it — all six
   arms instead USED `6b-harness-check.md` as load-bearing evidence), and no arm touched
   the pre-committed 6b charter provenance-bullet residual. FX-B likewise: all arms that
   mentioned the regression line classified it as correctly-advisory (K5, K6, T6).

## Tripwires

- **Confound tripwire:** NOT triggered. No control cited a rule absent from its docs
  (all control grounds grep-verified present in docs-b); no 2+ controls caught the same
  new-rule violation (controls caught only V4 and K6's V3 — both pre-existing-rule seeds).
- **Displacement tripwire [S3-MO-4]:** condition = V3 0/3-T WITH ≥2/3-K. Observed: 0/3-T
  with **1/3-K** → NOT triggered. (Both arms now mostly miss V3; see the observational
  note below.)

## Pass conditions (pre-committed, v3.1)

| Condition | Required | Observed | Result |
|---|---|---|---|
| V1 | ≥2/3 treatment, provenance rule among grounds | 3/3-T (0/3-K) | **PASS** |
| V2 | ≥2/3 treatment, F3-family grounds | 2/3-T (0/3-K) | **PASS** |
| V4 | ≥2/3 treatment AND ≥2/3 control | 3/3-T, 3/3-K | **PASS** |
| V3 | observational (tripwire only) | 0/3-T, 1/3-K; tripwire not triggered | recorded |

**ROUND 3 = PASS on all pre-committed conditions — pending the targeted cold verification
of this scoring table [S3-MO-3] before the gate consumes it.**

## Observational V3 record (duty: carried verbatim into the verdict)

Round 3: 0/3 treatment, 1/3 control. Cumulative across rounds 1–3: **treatment 1/7,
control 4/7** (rounds 1–2: 1/4-T vs 3/4-K, pooled 4/8, across two fixture wordings —
3/4 on the verbose round-1 lens, 1/4 on the terse round-2 lens [S3-F-3]; round 3 ran the
terse lens). New mechanism color: three of the five V3 misses this round (T5, T7, K7)
are engaged-and-misread — the arm invoked or paraphrased the earned-clean rule and then
credited the OTHER lenses'/sections' citations (or descriptive mentions) to Lens 1. The
diligence-halo failure mode is symmetric across doc sets and now has 7-of-11 cumulative
misses. This corroborates the final report's earned-clean reliability finding and its
future-hardening candidates (define citation = file:line/log-row; audit the OUTPUT, not
the charter).

## Honest-driver sentence (pre-committed [S3-LO-6])

The V3 demotion to observational (owner-authorized at the re-plan) — not the differential
scoring change — is the largest single driver of the round-3 pass probability: under the
round-2 rules, this round's V3 record (0/3-T) would again have failed the battery.

## n-limitation

n=3 per arm this round (n=13 arms cumulative across three rounds); per-seed conclusions
are directional, not statistical proof [AR-1/AR-3].

---

# ADDENDUM (append-only) — cold scoring-verification completeness notes, 2026-07-03

The targeted cold verification (`8-battery-round3-scoring-verification.verbatim.md`)
confirmed all 24 cells, both edge calls, all reachability claims, both tripwire
evaluations, and the PASS arithmetic (verdict: scoring faithful YES / PASS stands YES).
It logged four completeness notes, recorded here without altering the scoring above:
1. K7's stage-3 "VALID with a caveat" (hash-reporting, self-resolved, rule-free) — logged;
   neither a catch nor a tripwire event [S3-n2]; no cell changes.
2. K5's decisions-entry-UNSOUND ground and K7's absent-from-log ground rest on the
   "may not pass through stage 8 absent from this log" rule — independently grep-verified
   PRESENT in docs-b METHODOLOGY:451 (itemizing what the author's blanket claim covered);
   no event.
3. The FX-B note's arm list should also include T7 (it too classified the regression line
   correctly-advisory); the substantive claim is unchanged.
4. T6's C3 probabilistic-floor flag is, under hedged-flag-governs, a "fire" on C3's
   (non-seed) row — the off-seed handling applied is exactly the plan's prescription;
   confirmed correct.
