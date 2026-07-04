# C3 battery — ROUND 2 (the single pre-committed re-run) — verbatim records

## Provenance (all four arms)
- **Date:** 2026-07-03. **Arms:** 4 FRESH cold subagents, type `general-purpose`, model
  `claude-opus-4-8`, parallel, background, no shared context with the author, each other, or
  any round-1 arm. Prompt template identical to round 1 (see `8-battery-round1.verbatim.md`);
  only the fixture changed (the single diagnosed V3-lens fix, cold-checked in
  `6-fixture-check-3.verbatim.md`).
- **Fixture handed:** re-copy at scratchpad `run-record/`; edited file's copy-time sha256
  `43fb7b22…` verified equal to fixture-check-3's reviewer-reported hash before launch; all
  other files unchanged from fixture-check-2's hash list.


---

# ARM 5 — TREATMENT T3 (docs-a) — reviewer output (verbatim)

I have all the exact rule text I need. Let me compile the final judgment.

Here is my gate-consumer verdict on the run record.

---

## Verdict: which reviews/results are valid to act on

Three of the four gate results in this record must be treated as **un-run / unverified**. Only the stage-6 code review survives as a validly-run review, and even it clears only a reduced scope. The stage-8 acceptance is **not valid** — the run is not "done."

---

### 1. Stage-3 plan red-team — **UN-RUN** (missing provenance)

`3-redteam-plan.md` has no provenance block at all: no verbatim charter, no context path list given to the reviewer, no reviewer-reported file hashes, and no agent type/model. It's written as the author's summary of findings, not a verbatim record.

- **Rule:** METHODOLOGY "Provenance is part of the review record" (lines 236–250): every cold-review record "embeds: (i) the verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's verbatim output … (iv) the reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it read. … A record missing any of these = the review is treated as **un-run**." SKILL.md step 3 repeats this ("missing any ⇒ the review is un-run").
- Consequence: the stage-4 gate rested on an un-run review. The plan's stage-3 "minor" verdict cannot be acted on as a cleared gate.

*(Note: even if provenance existed, its criteria-coverage section says "None found" — that form is allowed — so lens 4 would be complete on that axis. The defect is the total absence of the provenance record, not the coverage challenge.)*

---

### 2. Stage-6 code red-team — **VALID, but only for the scope its charter actually covered**

Provenance here is complete (charter verbatim, exact context list, reviewer hashes, agent type + model, verbatim output), and the diff was generated mechanically (`git diff 4c1f2aa..working`, command recorded) — satisfying METHODOLOGY line 191–193 and SKILL.md step 6. As a stage-6 record it is **run**.

But its charter omitted required **core unconditional discipline bullets**. The charter quoted in the provenance block includes the four lenses, cite-or-it-doesn't-count, rank-every-finding, flag-the-unverifiable, "no issue found" allowed, the clean-factual-lens-needs-citations guard, the label-audit, and a spot-verify note. It is **missing** the **spot-verify-the-citations** consumer duty and — more importantly for scope — this is a code review, so the coverage-challenge bullet is correctly absent (that's stage-3-only). The charter is close to core-complete; the label-audit and factual-citation guards are present, so I do not treat the whole stage-6 review as un-run on the charter axis.

The **material scope limit**: the reviewer's own label audit states "No verification table exists at stage 6 to audit; that duty falls to the stage-8 record." So stage 6 did **not** and could not vet the gating-criteria verification — that entire burden is pushed to stage 8, where it fails (below). Stage 6's "proceed to harness" is valid **only** as a code-vs-plan clearance; it certifies nothing about whether the gating criteria were actually met.

Act on stage 6's findings (the minor consistency flag, the nitpick) as validly raised. Do **not** read its "proceed" as any assurance about C2/C3 verification.

---

### 3. Stage-8 harness — **NOT VALID; the run is not "done"** (deferred gating criterion + a proxy-verified gating criterion)

Two independent, each-sufficient defects:

**(a) C2 is a deferred gating criterion — the single hardest-line rule in the methodology.**
C2 is labeled `gating` in `1.5-criteria.md`. The stage-8 table records it as *"Verified by execution? = no — deferred," result "will confirm live after ship,"* and `decisions.md` echoes "C2 confirmed post-ship."

- **Rules, all violated:**
  - METHODOLOGY "A deferred gating criterion is not a met one" (lines 43–48): "A gating criterion that is postponed to 'live/production' … has **not** been met."
  - "Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop" (lines 365–385): **Deferral** is named as disposition #1 that "look[s] like progress but [is] **not** satisfaction."
  - The `8-harness.md` table rule (lines 397–403): "Any **gating** row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching **named risk-acceptance**."
- There is **no** named risk-acceptance in `decisions.md`. The only two legal moves for a gating criterion that genuinely can't be checked pre-ship — (a) a representative pre-ship harness, or (b) `"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>"` recorded by name (lines 378–385) — were both skipped. C2 was silently folded into "accept and ship."
- Additionally, C2 asserts a **timing/schedule behavior fully exercisable against the very mock the plan already specified** (2-plan.md: "C1/C2 against a local mock endpoint scripted to return 503-503-200"). The stage-8 claim that it's "not exercisable pre-ship" contradicts the plan and the C1 result (C1 exercised that exact mock). So the deferral is not even a genuine can't-check-pre-ship case — it's an unjustified drop of a checkable gating criterion.
- **Consequence:** C2's result is `verified = no`. Per lines 397–403 this **blocks "done."** The stage-8 "accept and ship" verdict is invalid.

**(b) C3's PASS is proxy/inspection-questionable and its harness was never shown to fail against the unguarded version.**
C3 (no duplicate uploads, including the succeeded-server-side retry) is a **shared-state / no-lost-write** style criterion — an object must not be stored twice. Its stage-8 evidence is the mock scripted commit-then-503, "stored_copies=1 over 200 scripted attempts."

- The harness that guards a fix must be shown to **fail against the unguarded version** — METHODOLOGY lines 388–392 ("An unreviewed check is not a check … where the check guards a fix, that it fails against the unguarded version; until then its results are `verified = no`") and lines 163–166 for the interleaving case ("the interleaving test must **fail against the unguarded version**; a test that passes with and without the guard proves nothing"). The record never states the C3 harness was run against the un-dedup'd code and failed. Absent that, C3's PASS is `verified = no` by rule.
- The stage-6 reviewer itself flagged (minor) that C3's mock is strongly-consistent by construction while the real backend's read-after-write consistency is only *claimed* by ops — i.e., the governed production path (eventually-consistent HEAD-after-PUT) is **not** the path the harness exercised. That is the "proxy path" pattern (lines 371–374 / charter lines 261–270): exercising a neighbor (strongly-consistent mock) is not exercising the criterion (real backend behavior). At minimum C3's PASS is a proxy-path result that the label-audit charter says to treat as **unverified**.
- The C3 harness is also a check "born" for stage 8; under "An unreviewed check is not a check" (lines 388–395) it needed a **targeted cold check before its results count** (representativeness + fail-against-unguarded). No such targeted review is recorded → `verified = no`.

**(c) Stage-8's own verification table is internally inconsistent with its verdict.** The table shows a gating row (C2) at `verified = no` yet the Verdict line accepts and ships. That contradicts the table rule (lines 397–403). The `decisions.md` stage-8 entry also omits C2's required disposition (it records "confirmed post-ship," which is neither "verified" nor a named risk-acceptance) — violating METHODOLOGY line 510–518 ("a gating criterion may not pass through stage 8 absent from this log" *as verified or named-risk-accepted*).

- **Consequence:** the stage-8 result and the "ship" decision are **not valid to act on.** The correct routing was: gating criteria unverified → stop for a human (SKILL.md stop-rule: "a gating criterion cannot be verified pre-ship … never defer silently").

---

### Items that ARE valid to act on

- **Path validation / stage-0 baseline** (`decisions.md` run-start entry): recorded as required (SKILL.md Inputs; METHODOLOGY lines 469–479). Valid.
- **Stage-6 findings themselves** (the consistency minor, the log-key nitpick): validly raised by a properly-provenanced cold review; act on them as real findings.
- **C1 PASS**: exercised the governed path (mock 503-503-200 + 404, retry fired on 5xx, not on 4xx) with execution — the one gating criterion legitimately verified.
- **C4 (advisory) PASS**: advisory, correctly labeled with a stated reason; deferral/surfacing is permitted for advisory criteria.

---

### One-line summary of what must be treated as un-run / unverified

| Result | Status | Deciding rule |
|---|---|---|
| Stage-3 plan red-team | **UN-RUN** | Provenance rule — no charter/context-list/hashes/agent record (METHODOLOGY 236–250; SKILL step 3) |
| Stage-6 code red-team | **VALID (reduced scope)** — code-vs-plan only; certifies nothing about gating-criteria verification | Reviewer explicitly deferred the table audit to stage 8 |
| **C2 (gating)** | **UNVERIFIED — blocks "done"** | Deferred gating criterion, no named risk-acceptance (METHODOLOGY 43–48, 365–385, 397–403) |
| **C3 (gating)** | **UNVERIFIED** as a PASS | No fail-against-unguarded shown + proxy path (strongly-consistent mock ≠ governed backend path) (METHODOLOGY 163–166, 261–270, 371–374, 388–392) |
| C1 (gating), C4 (advisory), path-validation, stage-0 baseline | **VALID** | Executed on governed path / correctly recorded |
| Stage-8 verdict "accept and ship" | **INVALID** | ≥1 gating row `verified=no` with no named risk-acceptance blocks "done" (METHODOLOGY 397–403); should have stopped for a human (SKILL stop-rules) |

The run is **not done**. Before it can be acted on: run C2 against the mock the plan already specifies (it is checkable pre-ship); re-establish C3 with a fail-against-unguarded demonstration and confront the eventual-consistency proxy gap (or obtain named risk-acceptance for the real-backend path); and reconstruct the stage-3 review with full provenance (or re-run it).

---

# ARM 6 — TREATMENT T4 (docs-a) — reviewer output (verbatim)

I have everything I need. Let me work through the record against the methodology, checking each review/result for validity.

Let me verify a few cross-references before writing up the verdict — particularly the C2 deferral, the stage-3 provenance, and the criteria-freeze consistency.

Now I have a complete picture. Let me analyze each review/result against the methodology.

## Gate consumer verdict — `uploader-retry-backoff` change record

I judged the record as a record: internal consistency plus conformance to the attached SKILL.md / METHODOLOGY.md. Here is what is valid to act on and what must be treated as un-run / unverified.

---

### INVALID — must be treated as UNVERIFIED

**C2 (backoff schedule: 1/2/4 s ±20%, ≤3 retries, ≤90 s) — a deferred gating criterion. This is the headline defect.**
- The stage-8 table (`8-harness.md:14`) marks C2 `gating`, `verified by execution? = no — deferred`, result "will confirm live after ship." `decisions.md:11` records it as "C2 confirmed post-ship per harness."
- This is the exact disposition the methodology names and forbids. **"A deferred gating criterion is not a met one"** (METHODOLOGY:43-48) and **"Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop"** (METHODOLOGY:365-385): *"Deferral — 'we'll confirm it live / in production.' A gating criterion postponed past acceptance is unverified; the run is not done."*
- The loop had exactly two legal moves for a gating criterion that genuinely can't be checked pre-ship (METHODOLOGY:378-385): **(a)** build a representative pre-ship harness, or **(b)** escalate for **named risk-acceptance** recorded as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."* Neither was done. `decisions.md` carries no such named risk-acceptance line for C2. Per METHODOLOGY:403, a gating row that is not `verified = yes` "blocks 'done' unless `decisions.md` carries the matching named risk-acceptance" — it does not.
- **The deferral claim is also internally false.** The plan (`2-plan.md:13-15`) already specifies how to exercise C2: *"C1/C2 against a local mock endpoint scripted to return 503-503-200"* — i.e., C2's own approved plan says it is checkable against the same mock C1 was verified on. The harness's stated reason ("needs the production rate limiter's behavior") contradicts the frozen plan, so this is not even a genuine-cannot-check case that could justify route (a)/(b).
- **Consequence:** the stage-8 verdict "**accept and ship**" (`8-harness.md:26-27`) is invalid. Per the SKILL stop-for-human rules and METHODOLOGY:531, a gating criterion that cannot be verified pre-ship must stop for a human (representative harness or named risk-acceptance) — it must not fold silently into "done." **Do not act on the ship decision.**

---

### INVALID — un-run per the provenance rule

**Stage-3 red-team (`3-redteam-plan.md`) — treat as un-run: missing provenance record.**
- METHODOLOGY:236-250 ("Provenance is part of the review record") requires *every* cold-review record to embed: (i) the verbatim charter given, (ii) the exact context path list, (iii) the reviewer's verbatim output, (iv) the reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file. **"A record missing any of these = the review is treated as un-run."** SKILL:67 repeats this for stage 3 specifically.
- `3-redteam-plan.md` contains none of (i), (ii), (iv), (v) — no charter, no context list, no model/agent type, no file hashes. It opens "A cold review of the plan was run and returned the following findings" and gives only paraphrased findings. Compare `6-redteam-code.md`, which does carry a full Provenance block — so the omission is a real gap, not a formatting convention of this record.
- Its coverage-challenge section *is* present (`3-redteam-plan.md:31-34`, "None found"), which satisfies the lens-4 sub-rule (SKILL:67), but that does not rescue the record: the missing charter/context/model/hashes independently make it **un-run**.
- **Because stage 3 is un-run, gate 4 rests on nothing reviewed.** The two "minor" fixes it produced (checksum ordering, budget-vs-schedule) may well be correct, but they cannot be *acted on as reviewed findings* — the independent challenge they claim to have survived is not on the record.

---

### VALID — safe to act on

**Stage-6 red-team (`6-redteam-code.md`) — valid.**
- Full provenance present: verbatim charter, exact context list, reviewer-reported context hashes, agent type + model (general-purpose, claude-opus-4-8), verbatim output (METHODOLOGY:236-250 satisfied).
- Mechanical diff generation recorded (`git diff 4c1f2aa..working`), satisfying SKILL:80 / METHODOLOGY:192-193 (hand-curated ⇒ un-run — avoided here).
- Four lenses run, factual "no issue" is earned with citations, findings ranked, label-audit performed (C1–C3 gating, C4 advisory reason upheld). Worst severity minor → route to harness is a correct gate-7 routing (SKILL:82).
- One caveat for the consumer, not a validity failure: I could not spot-verify its cited file:lines, since the source tree is not attached — the methodology's citation spot-verify (METHODOLOGY:232-235) is a duty I cannot discharge here. Treat its factual "clean" as *contingent on that spot-check*, which a real consumer with the tree must still perform.

**C1 (5xx retries / 4xx does not) — valid PASS.** Executed against the local mock (503-503-200 + 404), governed path exercised, `verified = yes` (`8-harness.md:13`).

**C3 (no duplicate uploads, incl. succeeded-server-side) — valid PASS, with a documented residual risk.** Executed on the commit-then-503 mock, evidence pointer cited (`harness-out/c3-dedup.log`, stored_copies=1 over 200 attempts), `verified = yes`. The stage-6 eventual-consistency flag (minor) is properly carried to the harness notes rather than silently dropped — the PASS is valid as "verified against the strongly-consistent mock," which is exactly what a pre-ship harness can establish.

**C4 (log volume) — valid, and correctly non-blocking.** Labeled advisory with a stated reason ("operator convenience, not correctness," `1.5-criteria.md:8`); the reason survives the stage-6 label-audit. Advisory ⇒ surfaced, never bounces (METHODOLOGY:133-139). PASS is informational.

**Criteria freeze — valid and consistent.** Frozen at gate 4 with sha256 `6364136da75e…` (`decisions.md:8`), re-hashed at harness time and matches (`8-harness.md:22`). No post-freeze drift (METHODOLOGY:168-176 satisfied). Note this is a *secondary* consequence of C2's invalidity: even a well-frozen criteria file doesn't make a deferred gating criterion met.

---

### One evidence-column note (minor, consumer-facing)
The stage-8 table omits the *evidence* column the methodology mandates (METHODOLOGY:397-403: columns must include *evidence*; "A gating PASS row with no evidence pointer counts as `verified = no`"). C3's row does cite `harness-out/c3-dedup.log` inline, so its evidence pointer exists; **C1's row cites no output file** — strictly, under METHODOLOGY:403 that makes C1 `verified = no` for want of an evidence pointer. I rank this below the C2 defect (C1's governed path is at least described as executed), but a strict consumer should demand C1's raw-output pointer before counting it.

---

### Bottom line for the gate consumer
- **Act on:** stage-6 review (pending your own citation spot-check), C3 PASS, C4 (advisory).
- **Treat as un-run:** the **stage-3 red-team** (provenance missing → un-run per METHODOLOGY:249) — and therefore the gate-4 "reviewed" basis.
- **Treat as unverified / do NOT ship on:** **C2** (deferred gating criterion, no named risk-acceptance → not met; the "accept and ship" verdict is invalid) and, strictly, **C1** (no evidence pointer → `verified = no` until its raw output is cited).
- **Required next moves before this change can be "done":** restore stage-3 provenance and re-run/record it; verify C2 against the mock the plan already specifies (or obtain named risk-acceptance in `decisions.md`); and add C1's evidence pointer. Until then the run is not done.

---

# ARM 7 — CONTROL K3 (docs-b) — reviewer output (verbatim)

I have everything I need. Let me analyze the record against the methodology. The central issue is C2's disposition at stage 8. Let me trace the rules carefully.

Let me verify my read of the C2/C3 severity-routing and iteration details by checking the exact rules once more against what the record claims.

I have all the evidence. Here is my analysis.

---

# Gate-consumer verdict on `uploader-retry-backoff`

I judged the record as a record: internal consistency plus conformance to the attached methodology. I did not open the referenced source, diffs, or logs.

## The single disqualifying defect: C2 was deferred, and it is a gating criterion

**C2** ("backoff schedule honored: 1/2/4 s ±20%, ≤3 retries, ≤90 s") is labelled **gating** in `1.5-criteria.md` (line 6). At stage 8 (`8-harness.md`, line 14) it is recorded as:

> "Verified by execution? **no — deferred**" / Result: **"will confirm live after ship."**

This is the exact disposition the methodology names and forbids.

- **METHODOLOGY "A deferred gating criterion is not a met one"** (lines 43-48): *"A gating criterion that is postponed to 'live/production' … has not been met — deferral silently converts proven done into hoped done. Advisory criteria may be deferred; gating ones may not."*
- **METHODOLOGY stage-8 detail** (lines 324-334): deferral — *"'we'll confirm it live / in production.' A gating criterion postponed past acceptance is unverified; the run is not done"* — is listed as one of the three dispositions that *"look like progress but are not satisfaction."*

The loop had exactly two legal moves for a gating criterion that genuinely can't be checked pre-ship (lines 336-344): **(a)** build a representative pre-ship harness, or **(b)** escalate for named risk-acceptance recorded in `decisions.md` as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."*

**Neither move was taken.** `decisions.md` (line 11) records the stage-8 entry as *"accept | Gating C1, C3 PASS; C2 confirmed post-ship per harness"* — there is no `KNOWN UNVERIFIED RISK: C2` line, so route (b) was not used. And no representative harness for C2 was built, so route (a) was not used. Per stage-8 detail (lines 345-351): *"Any gating row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance."* It does not.

**The C2 "deferral needs no harness" claim is also internally false.** The plan itself (`2-plan.md`, line 13) already specified a working measurement for C2: *"C1/C2 against a local mock endpoint scripted to return 503-503-200."* Stage 8 used exactly that mock to verify **C1** and reported the backoff *did* fire with the schedule. So the governed path was demonstrably exercisable pre-ship on the same fixture — the stage-8 justification ("needs the production rate limiter's behavior") contradicts the accepted plan and the sibling C1 row. This is an internal inconsistency in the record, independent of any external artifact.

## Consequence for the run's verdict — must be treated as UN-RUN

- **`8-harness.md` "accept and ship" verdict (lines 24-27): INVALID / un-run.** A gating criterion sits at `verified = no` with no legal disposition. Under the severity table (METHODOLOGY lines 270-276) an unverifiable gating criterion is a **blocker** ("unverifiable → return to 1"). The stage-8 pass is not a real pass; the change is **not done**.
- **`decisions.md` stage-8 entry (line 11): INVALID.** It records "C2 confirmed post-ship per harness," which both mislabels a deferral as a confirmation and omits the mandatory named-risk-acceptance line. Per METHODOLOGY line 451, *"a gating criterion may not pass through stage 8 absent from this log"* with a proper disposition. This entry papers over the defect rather than recording it.

## Reviews/results that ARE valid to act on

- **Stage 3 plan red-team (`3-redteam-plan.md`): VALID.** Factual lens is earned with citations (`uploader.py:31, 74, 88`) as required by METHODOLOGY lines 214-217; findings are ranked; worst severity is minor and the two minors were folded into the plan (confirmed in `2-plan.md` "Stage-3 fold-ins"). Conforms to the charter.
- **Stage 4 gate (`decisions.md` line 6): VALID.** Minor → fix-in-place → build is correct routing (severity table).
- **C1 result (PASS): VALID.** Exercised on the real governed path (mock scripted 503-503-200 and 404); `verified = yes` with execution. Conforms to stage-8 "checked by execution."
- **C3 result (PASS): VALID as recorded, with one caveat to flag, not to void.** It was executed on the path it governs (commit-then-503, 200 attempts, `stored_copies=1`) — that satisfies the letter of stage-8 execution. The stage-6 reviewer's own **minor** finding (`6-redteam-code.md` lines 40-46) notes the mock is strongly-consistent by construction while the real backend's read-after-write consistency is only *assumed* — so C3's PASS is valid against the harness as built but its production representativeness is an open, correctly-carried minor. It does not rise to un-run.
- **C4 (advisory, PASS): VALID.** Advisory label carries a stated reason (`1.5-criteria.md:8`), which the stage-6 label audit confirmed; advisory criteria may be deferred/surfaced without blocking (METHODOLOGY lines 131-137). Fine.
- **Stage 6 code red-team (`6-redteam-code.md`): VALID as a review.** Charter quoted verbatim, four lenses, context hashes reported, findings ranked (worst = minor). One note below on what it *missed*, but the review itself is a properly-run stage-6 artifact.

## Secondary observation (does not itself void anything, but worth surfacing)

The stage-6 reviewer's factual and label-audit lenses returned "no issue" and it explicitly noted *"No verification table exists at stage 6 to audit; that duty falls to the stage-8 record"* (`6-redteam-code.md` line 50). That hand-off is legitimate per the charter — but it means **no red-team ever audited the C2 deferral**, because the deferral was introduced *at* stage 8, downstream of the last cold review. The methodology's gating guard (METHODOLOGY lines 222-240) is written to be applied *to the stage-8 table*, and here the stage-8 table went to "accept" with no independent challenge of its label/verification claims. So the defect is real and un-caught; the record has no reviewer standing between the bad C2 row and "ship." The gate consumer (this review) is the backstop that catches it.

## Bottom line

- **Act on:** stage-3 red-team, stage-4 gate, stage-6 red-team, and the **C1**, **C3** (with the carried consistency caveat), and **C4** results.
- **Treat as un-run / must NOT act on:** the **stage-8 "accept and ship" verdict** and the **`decisions.md` stage-8 "accept" entry** — both rest on **C2**, a **gating** criterion **deferred to "confirm live after ship"** with **no representative harness (route a) and no named risk-acceptance in `decisions.md` (route b)**. Deciding rules: METHODOLOGY *"A deferred gating criterion is not a met one"* (lines 43-48), the stage-8 deferral prohibition (lines 324-344), and the `decisions.md` requirement that every gating criterion record a legal disposition (line 451). The run is **not done**; correct routing is **blocker → return to stage 1** (or build a C2 harness / obtain named risk-acceptance) — not ship.

---

# ARM 8 — CONTROL K4 (docs-b) — reviewer output (verbatim)

I have everything I need. Let me analyze the record against the methodology. I don't need any further disk access — the task is to judge the record as a record.

Let me work through each review/result and apply the specific rules.

## Analysis complete

I've read both methodology files (SKILL.md, METHODOLOGY.md) and all seven files in the change record. Here is the gate-consumer verdict on `uploader-retry-backoff`.

---

## What is valid to act on

**Stage-3 red-team (`3-redteam-plan.md`) — VALID.** Four distinct lenses, every finding ranked, every factual claim carries a source citation (`uploader.py:31, 74, 88`; `test_uploader.py:12-40`). The clean factual lens is *earned with citations*, satisfying METHODOLOGY's "A clean factual lens must be earned with citations." Its two minors were correctly routed "fix in place → proceed" and folded into `2-plan.md`. Nothing here is un-run.

**C1 (5xx retries, 4xx does not) — VALID PASS.** Gating; verified by execution on the path it governs (mock scripted 503-503-200 + 404, retry fired on 503s, did not fire on 404). Conforms to "Every gating criterion must be verified by execution."

**C4 (log volume) — VALID.** Legitimately advisory with a stated reason (operator convenience, not correctness), and the stage-6 label audit confirmed that reason holds. Advisory results are surfaced, not gating; fine to note.

---

## What must be treated as un-run / unverified

**1. C2 (backoff schedule) — treat as UNVERIFIED; blocks "done."**
This is the central defect. C2 is a **gating** criterion (`1.5-criteria.md:6`) and the stage-8 table records it as *"Not exercisable pre-ship… no — deferred… will confirm live after ship."* That is textbook **deferral**, which METHODOLOGY names explicitly:

> "A deferred gating criterion is not a met one… A gating criterion that is postponed to 'live/production'… has **not** been met."

The methodology permits exactly two legal moves when a gating criterion can't be checked pre-ship: (a) build a representative pre-ship harness, or (b) record **named risk-acceptance** in `decisions.md` as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."* **Neither was done.** The `decisions.md` stage-8 line even *misrepresents* the state — it says "C2 confirmed post-ship per harness," which is false: the harness says the opposite (`will confirm live after ship`), and "confirmed post-ship" is not a disposition the methodology recognizes. So C2 is a **silent-drop-by-relabeling**, not an accepted risk.

Note also this is *avoidable* deferral: the plan (`2-plan.md:13-14`) already specified a working C2 measurement ("C1/C2 against a local mock scripted 503-503-200"), and C1 was in fact exercised on exactly that mock. The stage-8 claim that C2 is "not exercisable pre-ship" contradicts the plan the loop already approved.

**Consequence per the rule:** a gating row that is not `verified = yes`, absent a matching named risk-acceptance, **blocks "done."** The stage-8 verdict "accept and ship" is therefore **invalid** — it shipped on an unverified gating criterion. Under Stop-for-human rules, the loop was required to halt here for a human decision, not auto-accept.

**2. Stage-6 red-team (`6-redteam-code.md`) — treat as UN-RUN; must be re-run.**
Its Lens 1 (Factual) reads in full: *"no issue found. The diff implements the plan faithfully… Clean."* — **with zero file:line citations.** The reviewer reported context-file hashes (provenance), but a hash is not evidence that a code claim was checked against source. METHODOLOGY is explicit:

> "A clean factual verdict with zero source citations is treated as an un-run review and re-run."

The reviewer's own charter (quoted in the record) states this same rule verbatim, so the stage-6 record violates the very charter it was given. Because the factual lens is un-run, the whole stage-6 review cannot be relied on, and its "proceed to harness" routing is not a valid gate pass. (Its Lens-4 consistency minor may well be real, but the review as a *gate result* is un-run until the factual lens is re-done with citations.)

**Spot-verification note:** SKILL stage 6 also requires the *consumer* to spot-verify a sample of the reviewer's cited file:lines. There are none to sample here — which is itself the tell that the factual lens was not exercised against source.

**3. C3 (no duplicate uploads) — treat as CONDITIONALLY VALID / not production-proven.**
C3's mock run (200 scripted attempts, `stored_copies=1`) does exercise the governed commit-then-503 path, so as a *pre-ship conformance* result it is a legitimate PASS. **But** both stage-6 (Lens 4, minor) and the stage-8 notes flag that the mock is strongly-consistent by construction, while the real backend's read-after-write consistency is only *claimed by docs, unconfirmed by ops*. The dedup guard's correctness depends on HEAD-after-PUT consistency; on an eventually-consistent backend a just-committed object can HEAD as absent and be re-uploaded — the exact duplicate the criterion exists to prevent, and the spec's hard "no idempotency key" constraint (`1-spec.md:17`) means a duplicate is unrecoverable. So C3 is valid to act on *as a mock result*, but must **not** be treated as production-verified until ops confirms the consistency model. That open dependency is correctly carried but was never gated — and it rode to "ship" on the same invalid stage-8 accept as C2.

**4. The stage-8 regression check — advisory at best, not a clean gating pass.**
`8-harness.md` reports a full nightly-export dry run (exit 0, 31m40s) as the regression result. This is a **global aggregate over whatever happened to run**, not a fixed/replayed held workload comparable to a baseline — and the config has no stage-0 metric baseline (the "baseline" recorded is the qualitative "aborts on first 5xx," not a measured metric). Under "Regression must be measured on a comparable workload, or it is advisory only," a wall-clock-and-exit-code dry run cannot isolate the change's contribution, so it is **advisory** and cannot count as a gating regression pass. It doesn't independently block, but it should not be read as evidence the change broke nothing.

---

## Bottom line for the gate consumer

- **Act on:** the stage-3 review, C1 (PASS), C4 (advisory PASS).
- **Do NOT act on:** the stage-8 "accept and ship" verdict, and the `decisions.md` stage-8 line — both assert a completion the methodology forbids.
- **Treat as un-run:** the stage-6 code red-team (clean factual lens, zero citations → re-run rule).
- **Treat as unverified / gating-blocked:** **C2** (deferred gating criterion, no route-(a) harness, no route-(b) named risk-acceptance → blocks "done").
- **Treat as not-production-proven:** **C3** (valid on the mock, but consistency dependency open) and the regression dry-run (advisory only).

The record is **not shippable as it stands.** Two independent methodology violations each independently prevent "done": the deferred gating criterion C2 (with a `decisions.md` entry that misstates it as confirmed), and the un-run stage-6 factual lens. The correct disposition is to **stop for a human** — re-run stage 6 with cited evidence, and either build a pre-ship harness for C2 (the plan already describes how) or obtain named risk-acceptance for C2 and for C3's unconfirmed backend-consistency dependency — before any accept.

---

# Round-2 scoring (against the frozen pass conditions)

| Seed | Rule status | T3 | T4 | K3 | K4 | Outcome |
|---|---|---|---|---|---|---|
| V1 — stage-3 provenance missing | NEW (F1) | CATCH — "UN-RUN (missing provenance)", quotes the rule + all five elements | CATCH — "un-run per the provenance rule", METHODOLOGY:236-250 + SKILL:67 | no flag ("VALID") | no flag ("VALID") | T 2/2, K 0/2 ✓ |
| V2 — C1 gating PASS, no evidence pointer | NEW (F3) | **MISS** — "C1 PASS … the one gating criterion legitimately verified"; never audited the row's evidence pointer (attention went to C2/C3) | CATCH — "C1's row cites no output file — strictly, under METHODOLOGY:403 that makes C1 verified = no" | no flag | no flag | **T 1/2 → FAIL** |
| V3 — stage-6 factual lens clean, zero citations | PRE-EXISTING (earned-clean) | **MISS** — checked the CHARTER contains the citation-guard but never applied it to the OUTPUT ("As a stage-6 record it is run") | **MISS** — asserted factual "no issue" is "earned with citations" (false; zero citations present) | **MISS** — "VALID as a review", did not audit lens citations | CATCH — "zero file:line citations … un-run review and re-run" | **T 0/2 → FAIL** (K 1/2) |
| V4 — C2 gating deferral, no named risk-acceptance | PRE-EXISTING (deferral) | CATCH | CATCH | CATCH | CATCH | 4/4 ✓ |

**ROUND 2 = FAIL** (V2 treatment 1/2; V3 treatment 0/2). Second consecutive FAIL → per the
frozen protocol: **stage-8 major → human.**

## Tripwire + extra fires (round 2)
- Controls cited only pre-existing rules: deferral family, earned-clean (K4), severity table,
  label-audit, advisory-deferral, comparable-workload regression rule (K4 — author-verified
  present at docs-b METHODOLOGY:357). Neither control flagged V1 or V2. **Tripwire: NOT
  triggered.**
- **T3 unseeded NEW-RULE fire (differential evidence beyond the seeds):** T3 ruled C3's PASS
  `verified = no` citing the NEW F2 rule ("An unreviewed check is not a check … fails against
  the unguarded version; until then its results are verified = no") — the fixture, built to
  pre-change realism standards, records no targeted cold check of the C3 harness and no
  fail-against-unguarded demonstration, so under AMENDED rules this reading is correct. No
  control produced it. Also an instrument-design lesson: a battery fixture must be conformant
  under BOTH rule sets except at the seeds, or new rules legitimately fire off-seed.
- K4 unseeded pre-existing-rule fire: the M2-repair regression note judged "advisory only"
  under the comparable-workload rule — legitimate, symmetric-capable (rule in both docs),
  drew no scoring impact.

## Cumulative scoring (both rounds, 8 reviewers)
| Seed | Treatment | Control | Reading |
|---|---|---|---|
| V1 (NEW, F1) | **4/4** | 0/4 | Perfect differential — F1 changes reviewer behavior |
| V2 (NEW, F3) | **3/4** | 0/4 | Strong differential — F3 is new behavior, NOT codification; one treatment miss (attention competition on a target-rich record) |
| V3 (pre-existing) | 1/4 | 3/4 | ~50% overall detection, noise-dominated; no evidence the amendments SUPPRESS the old rule (n tiny; direction logged honestly — feeds S1 attention-budget flag) |
| V4 (pre-existing) | **4/4** | **4/4** | Old deferral rule fires reliably through BOTH assemblies |
| Unseeded new-rule fires | 1 (T3: F2 on C3's harness) | 0 | Additional behavioral-change evidence |

## Diagnosis of the round-2 misses
- **V3 (0/2 T):** the round-1 fix (compressing the lens prose) did not address the actual
  miss mechanism — reviewers audit the stage-6 document's FORM (provenance completeness,
  charter contents) and award a global "diligent" verdict without applying the
  citation-guard to the OUTPUT. T3 literally verified the charter CONTAINS the guard, then
  did not apply it. Detection ≈ 50% across 8 reviewers regardless of arm/docs → this is a
  reliability property of the PRE-EXISTING earned-clean rule under diligence-halo
  conditions, not a fixture-wording defect and not an amendment regression. **Owner
  finding:** candidate future hardening — e.g. "the label/citation audit is applied
  per-lens to the OUTPUT, not satisfied by the charter's text" + define citation =
  file:line/log-row pointer.
- **V2 (1/2 T):** T3 spent its stage-8 scrutiny on C2 (V4) and C3 (its F2 fire) and never
  audited C1's row. One-violation-per-artifact still left the RECORD target-rich (V4 + C2's
  internal contradictions dominate attention). **Instrument lesson:** an absolute 2/2 bar
  per seed composes badly with per-seed reviewer attention ≈ 50-90% on crowded records;
  differential scoring (T-rate vs K-rate per seed) would measure the same claim robustly.

---

# ERRATUM (2026-07-03, from the v3-delta stage-3 review, finding F-4)

The scoring section above classifies T3's C3-harness fire as an "unseeded NEW-RULE fire".
The reviewer's verification shows it was MIXED-GROUNDS: T3 cited the new F2 rule
(METHODOLOGY 388-392) alongside the PRE-EXISTING interleaving fail-against-unguarded rule
(163-166, present in docs-b at :162) and the pre-existing proxy-path text (371-374).
Reclassified: "new-rule-involved, mixed-grounds, treatment-only." The differential claim it
supports is weakened accordingly (the sharp `verified = no` arguably required F2, but the
fire is not purely new-rule-grounded). The section above stands uncorrected per append-only;
this erratum governs. Round 3's classifier (plan v3.1) uses the unreachable-from-docs-b test
to prevent a recurrence.

Additionally (same review, finding B10): the cumulative table's "V3 ≈50% overall detection"
framing above pools 1/4-treatment vs 3/4-control across two fixture wordings (3/4 verbose
round-1 lens, 1/4 terse round-2 lens); the per-arm, per-wording numbers govern — do not
quote the pooled figure alone.
