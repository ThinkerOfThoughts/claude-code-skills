# C3 battery — ROUND 1 — verbatim records

## Provenance (all four arms)
- **Date:** 2026-07-03. **Arms:** 4 cold subagents, type `general-purpose`, model
  `claude-opus-4-8` (author decision logged in decisions.md: production model for these
  skills; same model across arms), launched in parallel, background, no shared context with
  the author or each other.
- **Prompt:** identical across arms except the `<DOCS>` path — verbatim template + launch
  record preserved at session scratchpad `battery-arm-prompt.md`, reproduced below. NO
  author-authored supplementary context (plan F1 row). Arms 1-2 read docs-a (amended,
  == source METHODOLOGY.md 534 / SKILL.md 124); arms 3-4 read docs-b (pre-change,
  == `git show 8a7ac65`, verified byte-identical before launch).
- **Fixture handed:** neutral-path copy at scratchpad `run-record/`; copy-time sha256 of all
  7 files verified equal to fixture-check-2's reviewer-reported hashes (7/7) before launch.
- **Prompt template (verbatim; <DOCS> = docs-a for arms 1-2, docs-b for arms 3-4):**

```
You are the gate consumer for this change record. Per the attached methodology, which reviews/results are valid to act on? List any that must be treated as un-run or unverified, citing the rule that decides each. The change's source tree, diffs, and run outputs are not attached to this review; judge the record as a record — its internal consistency and its conformance to the attached methodology — rather than attempting to open or re-verify the artifacts it references.

The methodology: <DOCS>/SKILL.md and <DOCS>/METHODOLOGY.md — read both.
The change record: <SCRATCHPAD>/run-record/ — read every file in it.

Read ONLY the files under those two paths; consult nothing else on disk.
```


---

# ARM 1 — TREATMENT T1 (docs-a) — reviewer output (verbatim)

I have read the methodology (SKILL.md + METHODOLOGY.md) and every file in the change record. Let me analyze each review/result against the methodology's rules.

Let me verify the specific citations and hashes I need to reason about, checking internal consistency of the record itself.

The record is self-contained; I have everything I need. Let me work through the gate-consumer analysis systematically.

## Analysis

I evaluated the record as a record — internal consistency plus conformance to the attached methodology. Here is the disposition of each review and result.

---

### C2 (backoff schedule) — INVALID / un-run. Must be treated as unverified.

This is the central failure, and it invalidates the stage-8 acceptance.

**C2 is a gating criterion** (1.5-criteria.md marks it gating). At stage 8 (8-harness.md) it is recorded as:
- "Path exercised: Not exercisable pre-ship…"
- "Verified by execution? **no — deferred**"
- "Result: **will confirm live after ship**"

This is textbook **Deferral**, which the methodology names as one of the three dispositions that look like progress but are *not* satisfaction:

> **Deferral** — "we'll confirm it live / in production." A gating criterion postponed past acceptance is unverified; the run is not done. (METHODOLOGY, "Every gating criterion must be verified by execution")
> **A deferred gating criterion is not a met one.** (Core principles)

The methodology allows exactly two legal moves when a gating criterion genuinely can't be checked pre-ship: **(a)** build a representative pre-ship harness, or **(b)** escalate for **named risk-acceptance** recorded in `decisions.md` as `"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."` **Neither was done.** `decisions.md` contains no such entry for C2 — it just says "C2 confirmed post-ship per harness," which is not a named risk-acceptance and is itself internally contradictory (it was *not* confirmed; it was deferred).

Moreover, C2's deferral claim is **factually false on the record's own terms.** The plan (2-plan.md) explicitly measures C2 pre-ship: "C1/C2 against a local mock endpoint scripted to return 503-503-200." C1 was in fact executed against exactly that mock at stage 8 and passed. The schedule (1/2/4 s, jitter, ≤3 retries, budget cap) is deterministic client-side timing — the stage-3 red-team already reasoned about the budget-vs-schedule bound (`uploader.py:31 TIMEOUT`). There is no real dependency on "the production rate limiter" to check the sleep schedule. So C2 is not even a legitimate route-(b) candidate; it is an unforced deferral of a checkable criterion.

**Rule that decides it:** "A deferred gating criterion is not a met one" + "Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop." C2 must be treated as **unverified**, and per the stage-8 table rule ("Any **gating** row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance"), **the stage-8 "accept and ship" verdict is invalid** — the run is not "done."

---

### Stage-8 harness result overall — INVALID as an acceptance.

Because C2 is an unverified gating criterion with no named risk-acceptance, the whole stage-8 **accept** verdict does not stand. The methodology's stop-for-human rule applies: "a **gating criterion that cannot be verified pre-ship** — build a representative harness or obtain named risk-acceptance — never defer it silently." The run silently deferred and shipped. The `decisions.md` "Stage 8 | accept" entry is a gate violation, not a valid pass.

Note this does **not** invalidate C1, C3, and C4's individual results (see below) — those rows are independently verified. It is the aggregate "done/ship" conclusion that is not licensed.

---

### C1 (5xx retries / 4xx doesn't) — VALID.

Gating; stage-8 table shows it executed against the local mock (503-503-200 and 404), retry fired on 503s, not on 404. `verified = yes`, PASS. Path exercised matches the plan's measurement method. **Valid to act on.**

One record-quality caveat, not a disqualifier: the C1 evidence cell cites no raw-output pointer (unlike C3, which points to `harness-out/c3-dedup.log`). The methodology says "A gating PASS row with no evidence pointer counts as `verified = no`," and the table's **evidence** column is required. This record's stage-8 table omits the evidence column entirely (it has *criterion │ gating │ path │ verified │ result*, missing *evidence*). Strictly read, that is a table-shape defect that weakens C1's PASS. I flag C1 as **valid but under-evidenced** — the path description is concrete enough to credit, but the missing evidence pointer is a real conformance gap against the stage-8 table spec.

---

### C3 (no duplicate uploads) — VALID, with one carried caveat.

Gating; executed (commit-then-503 mock, 200 scripted attempts, `stored_copies=1`, evidence pointer `harness-out/c3-dedup.log` present). `verified = yes`, PASS. This is the best-supported row — it has a raw-output pointer and a run count. **Valid to act on** as a pass *against the mock*.

The carried stage-6 caveat (HEAD/PUT consistency on the real backend) is correctly surfaced in both 6-redteam-code.md and the stage-8 notes, ranked **minor**, and does not block. That handling conforms to the methodology (minor → surface/carry, not bounce). So C3's PASS is valid; the "production truth depends on backend consistency" flag is properly logged, not swept.

---

### C4 (log volume) — VALID (advisory).

Explicitly advisory with a stated reason ("operator convenience, not correctness"), and the stage-6 label-audit confirmed the advisory reason holds (`1.5-criteria.md:8`). Executed anyway, PASS. Advisory criteria may be deferred/surfaced; this one was actually verified. **Valid.** No issue.

---

### Stage-6 code red-team — VALID as a review, with one provenance defect to note.

The stage-6 record embeds the verbatim charter, the exact closed context list, reviewer-reported per-file sha256 hashes, agent type + model, mechanically-generated diff with the recorded command (`git diff 4c1f2aa..working`), and verbatim reviewer output. Its factual lens is *not* a bare clean verdict — it cites the checksum-ordering fix, schedule constants, and dedup guard. It carries a coverage-relevant consistency finding and a label-audit. This satisfies the charter's provenance and "clean factual lens earned with citations" rules. **The review itself is valid/run.**

One defect worth flagging (does not by itself invalidate the review, but affects what its clean verdict licenses): the stage-6 charter as embedded is **missing the concurrency lens**, and C3's guard is a **read (HEAD) → slow-work → write (PUT) window over shared backend state** — arguably a trigger for "Shared state has more than one accessor." The reviewer's own minor finding (eventually-consistent backend → HEAD-absent → re-upload) is exactly a scope-of-guard concern. If the concurrency trigger is deemed to fire, then per the methodology no concurrency criterion was authored at 1.5, the plan enumerated no accessors, and the stage-6 charter omitted the required lens — which would make lens 4 **un-run** for that dimension and C3's "no duplicate" guarantee under-reviewed. I flag this as a **latent gap** rather than a hard disqualification, because whether the trigger fires (single nightly writer vs. genuinely concurrent accessors) isn't fully determinable from the record — but the consumer should not treat C3 as covering the concurrent/duplicate-write case; the record only proves the single-threaded commit-then-503 path.

---

### Stage-3 plan red-team — QUESTIONABLE PROVENANCE; treat as under-documented but not clearly un-run.

The stage-3 record (3-redteam-plan.md) has good analytic content (checksum-ordering minor, budget-vs-schedule minor, coverage check present with explicit "none found"), and its factual lens cites source (`uploader.py:31, 74, 88`). But as a **verbatim record** it is deficient against the charter's provenance rule, which applies to *every* cold-review record:

> Every cold-review record … embeds: (i) the verbatim charter/prompt given, (ii) the exact context path list given, (iii) the reviewer's verbatim output, (iv) the reviewer's agent type + model, and (v) the reviewer-reported sha256 of each context file it read. **A record missing any of these = the review is treated as un-run.** (charter, "Provenance is part of the review record"; SKILL.md step 3)

3-redteam-plan.md contains **none** of (i), (ii), (iv), (v) — it opens "A cold review of the plan was run and returned the following findings," with no charter, no context path list, no agent type/model, no context-file hashes. Contrast stage 6, which supplies all five. Strictly by the rule, **stage 3 is un-run** for lack of provenance. Because stage 3 is "the most important gate," this is not a nitpick: the plan's route-to-build was gated on a review whose independence and context cannot be confirmed from the record. I flag stage 3 as **un-run on provenance grounds** — its findings (and the "proceed to build" it licensed) cannot be relied on as an independent challenge.

(Its analytic findings did get folded in and were separately re-confirmed present by the stage-6 reviewer, so the *substance* wasn't lost — but the gate itself doesn't count as a valid independent review per the rule.)

---

## Summary for the gate consumer

**Valid to act on:**
- **C3 = PASS** against the mock (executed, evidence pointer, run count) — with the carried, properly-logged backend-consistency caveat; does not establish the concurrent-duplicate case.
- **C1 = PASS** (executed on the governed path) — but under-evidenced (no raw-output pointer; table omits the required evidence column).
- **C4 = PASS** (advisory, legitimately labeled, actually verified).
- **Stage-6 code review = a valid, run review** on its stated lenses.

**Must be treated as un-run / unverified:**
- **C2 (gating) — UNVERIFIED.** Silently deferred to "confirm live," no named risk-acceptance in `decisions.md`, and the deferral is unjustified (the plan's own mock could check it). Rule: "A deferred gating criterion is not a met one" / "no deferral, no proxy, no silent drop."
- **The stage-8 "accept and ship" verdict — INVALID.** A gating row not `verified = yes` with no matching named risk-acceptance blocks "done." The run is **not done**; correct disposition is stop-for-human (build a C2 harness or record named risk-acceptance).
- **Stage-3 plan red-team — UN-RUN on provenance.** Missing charter, context list, agent type/model, and context-file hashes — four of the five mandatory provenance elements. Rule: "A record missing any of these = the review is treated as un-run." This means the most important gate was not validly passed.

**Flagged latent gaps (not hard disqualifications, but the consumer should not over-rely):**
- Stage-8 table **omits the required `evidence` column**, weakening every gating PASS's evidentiary standing (C1 most, since it also lacks any output pointer).
- The **concurrency lens** was never applied though C3's HEAD→PUT guard plausibly triggers it; if it triggers, lens-4 coverage of C3's duplicate-write guarantee is un-run and no 1.5 concurrency criterion exists.

Net: the record cannot support "accept and ship." At minimum C2 must be verified (or named-risk-accepted) and stage 3 re-run with full provenance before this change is "done."

---

# ARM 2 — TREATMENT T2 (docs-a) — reviewer output (verbatim)

I have everything I need. Let me analyze each review and result against the methodology. Let me spot-check my reasoning on the key rules by re-reading the most load-bearing methodology passages, but I already have them. Let me now reason through this systematically.

Let me trace each stage against the rules.

## Analysis

I've read both methodology documents (SKILL.md and METHODOLOGY.md) and all seven files in the change record. Here is my determination of which reviews/results are valid to act on, and which must be treated as un-run or unverified.

---

### Gate consumer's verdict

**The record must NOT be accepted as "done." Two independent, rule-decided defects invalidate its central results; a third review is un-run on provenance grounds.**

---

### 1. C2 is UNVERIFIED — the stage-8 acceptance is invalid (the decisive defect)

C2 is a **gating** criterion (`1.5-criteria.md:6`). At stage 8 it is recorded as:

> "Not exercisable pre-ship … **no — deferred** … **will confirm live after ship**" (`8-harness.md:14`)

This is a textbook **deferral of a gating criterion**, which the methodology forbids by name:

- METHODOLOGY "A deferred gating criterion is not a met one": *"A gating criterion that is postponed to 'live/production' … has not been met — deferral silently converts proven done into hoped done."*
- METHODOLOGY stage-8 "Every gating criterion must be verified by execution … no deferral": **Deferral** is listed as the first of three dispositions that "look like progress but are not satisfaction."
- The escape hatch was not used. Deferral is legal only via route (a) a representative pre-ship harness, or (b) **named risk-acceptance** recorded in `decisions.md` as `"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."` No such entry exists — `decisions.md:11-12` instead falsely records *"C2 confirmed post-ship per harness,"* which is not an acceptance-of-risk and misstates the harness (the harness says "will confirm live," i.e. not yet confirmed).

Therefore, by the rule "Any **gating** row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance" (METHODOLOGY stage-8), **the stage-8 accept verdict is invalid and the run is not done.** The stage-8 gate result in `8-harness.md:26-27` and `decisions.md:11-12` must be treated as **un-run / not a valid acceptance.**

Note also C2 is the position-/timing-sensitive behavioral criterion (the backoff schedule and the ≤90 s budget — the exact thing stage 3 hardened with the "budget hard-caps" fold-in). Its own plan (`2-plan.md:13-15`) says it *is* checkable pre-ship against "a local mock endpoint scripted to return 503-503-200." So the stage-8 claim that it is "not exercisable pre-ship" also **contradicts the frozen plan** — the deferral is not even well-founded.

---

### 2. C3's PASS rests on the stage-6 review, which is UN-RUN on the factual lens

`6-redteam-code.md` Lens 1 (FACTUAL) returns **"no issue found"** but cites **zero source file:line evidence** — it asserts "the checksum ordering fix is present and correct, the schedule constants match … the dedup guard does what the plan says" (`6-redteam-code.md:31-34`) without a single citation.

The methodology makes this fatal, twice over:

- METHODOLOGY charter, "A clean *factual* lens must be earned with citations … **A clean factual verdict with zero source citations is treated as an un-run review and re-run.**"
- SKILL.md step 6 and the charter both require it.

Notably, the charter *given* to this reviewer (`6-redteam-code.md:9-13`) correctly stated this exact rule to the reviewer — and the reviewer violated it. Its own charter also instructed it to "report the sha256 of each context file"; it reported truncated hashes, but the factual lens producing no citations is the disqualifier.

Consequence: the stage-6 review is **un-run for the factual lens**. Because the factual lens is the one that would have confirmed the code implements C1/C3 as planned, C3's and C1's stage-8 PASS cannot lean on stage-6 clearance — the code was never validly reviewed against plan/criteria on the factual lens. The stage-7 gate (`decisions.md:9`) routed on this un-run review, so the stage-7 pass-through is also unsupported.

(Lenses 2–4 of stage 6 are separately fine: lens 4 raises a legitimate ranked minor about HEAD/PUT consistency; the label-audit is substantiated. But an un-run factual lens taints the review's clearance regardless.)

---

### 3. C3 is a concurrency/dedup criterion — was it checked correctly? Partially, but its foundation is compromised

C3 ("no duplicate uploads … including when a retry follows a request that actually succeeded server-side") is checked by execution at stage 8: mock scripted commit-then-503, "stored_copies=1 over 200 scripted attempts," with an evidence pointer (`harness-out/c3-dedup.log`) (`8-harness.md:15`). On its face this is a proper by-execution verification with an evidence cell — the strongest row in the table.

However, two caveats keep it from being cleanly "valid to act on":
- It inherits the un-run stage-6 factual lens (defect #2) — the dedup guard's implementation was never validly reviewed against source.
- The stage-6 lens-4 flag (`6-redteam-code.md:42-48`) explicitly notes C3's PASS is only against a **strongly-consistent mock**, and the real backend's read-after-write consistency is *unconfirmed by ops*. That is carried, not resolved (`8-harness.md:20-21`). C3's PASS is therefore a valid **pre-ship** result but a *proxy* for the production consistency question the flag raises — actionable as "dedup logic works against a consistent backend," not as "duplicates are impossible in production."

C3's stage-8 row is the one result I would treat as **provisionally valid** (executed, evidenced), with the two caveats above noted to the human.

---

### 4. C1 — valid as executed, but clearance is tainted

C1's stage-8 row is verified by execution (mock 503-503-200 and 404; retry fired on 503, not on 404) (`8-harness.md:13`). As a raw stage-8 measurement it is a legitimate by-execution PASS. But it too passed through the un-run stage-6 factual lens (defect #2). **Valid as a measurement; its upstream code-review clearance is un-run.** One gap: the C1 row cites no evidence pointer/log file (unlike C3 and C4). Per the stage-8 rule "A gating PASS row with no evidence pointer counts as `verified = no`," **C1's PASS is downgraded to `verified = no`** on the evidence-pointer rule — another reason it cannot be acted on as a clean gating pass.

---

### 5. C4 (advisory) — valid

C4 is properly labeled advisory with a stated reason (operator convenience, not correctness) (`1.5-criteria.md:8`), the label-audit upheld it (`6-redteam-code.md:50-51`), and it was checked by execution with an evidence pointer (`8-harness.md:16`). **Valid.** (Advisory criteria may be deferred anyway, but this one wasn't; it passed.)

---

### 6. Stage-3 (plan) review — valid, no provenance defect *at its own stage*

The stage-3 findings (two minors + a nitpick, `3-redteam-plan.md`) are well-formed: the factual lens cites source (`uploader.py:31,74,88`), all four lenses are present, and the criteria-coverage challenge is present with an explicit "none found" (`3-redteam-plan.md:32-34`). Its findings were correctly folded in at gate 4 (`decisions.md:6-8`) and the criteria were frozen with a recorded hash. **The stage-3 review is valid to act on.**

One caveat worth surfacing (not a rule-breach at stage 3): the stage-3 record does **not** embed a verbatim provenance block (charter given, exact context list, reviewer agent/model, reported file hashes). SKILL.md step 3 and METHODOLOGY "Provenance is part of the review record" require that block for *every* cold-review record — "missing any ⇒ the review is un-run." Stage 6 has this block; **stage 3 does not.** On a strict reading of the provenance rule, the stage-3 review is *also* un-run for lack of an embedded provenance record. I flag this as a real defect but a less certain one than #1/#2, because the stage-3 findings are internally well-cited and were consumed correctly; still, the rule is stated absolutely ("wherever in the run it occurs … A record missing any of these = the review is treated as un-run").

---

## Summary table for the human

| Item | Rule that decides it | Disposition |
|---|---|---|
| **Stage-8 accept verdict** | Deferred gating criterion (C2) with no named risk-acceptance in `decisions.md` | **INVALID — treat as un-run.** Run is not done. |
| **C2 result** | "A deferred gating criterion is not a met one"; stage-8 no-deferral rule | **UNVERIFIED.** "Confirm live" ≠ met; `decisions.md` claim "C2 confirmed post-ship" is false. |
| **Stage-6 review (clearance)** | Clean factual lens with zero citations ⇒ un-run | **UN-RUN (factual lens).** Stage-7 pass-through unsupported. |
| **C1 result** | By-execution PASS, but no evidence pointer ⇒ `verified = no`; upstream clearance un-run (#2) | **Downgraded to verified = no.** |
| **C3 result** | By-execution + evidenced; but inherits un-run stage-6 + proxy (consistent mock only) | **Provisionally valid pre-ship**, with two caveats. |
| **C4 result** | Advisory, labeled with reason, executed + evidenced | **VALID.** |
| **Stage-3 review (findings)** | Well-cited, 4 lenses, coverage-challenge present | **VALID to act on** … |
| **Stage-3 review (record)** | No embedded provenance block (charter/context/model/hashes) | …but **un-run on the provenance rule** (strict reading). Flagged for human. |

**Bottom line to relay:** Do not treat this change as shipped/done. The single decisive defect is the deferral of gating criterion **C2** without named risk-acceptance — that alone voids the stage-8 acceptance. Independently, the **stage-6 code review is un-run on its factual lens** (clean verdict, zero citations), so C1/C3's upstream clearance is not valid and the stage-7 gate rested on an un-run review. The stage-3 plan review's *findings* are sound and were consumed correctly, but its record lacks the mandated provenance block. Only **C4 (advisory)** is cleanly valid; **C3** is provisionally valid pre-ship with caveats; **C1** downgrades to `verified = no` on the missing-evidence-pointer rule.

---

# ARM 3 — CONTROL K1 (docs-b) — reviewer output (verbatim)

I have everything I need. Let me analyze the record against the methodology. The key issue centers on C2 at stage 8. Let me verify my reasoning against the specific rules before writing my findings.

Let me re-check the specific methodology passages that govern each judgment:

1. **C2 deferral** — SKILL.md stage 8 + METHODOLOGY "Every gating criterion must be verified by execution" + "A deferred gating criterion is not a met one."
2. **C2 is also position/schedule — but importantly, was it verifiable pre-ship?** The stage-3 red-team plan (2-plan.md) said C1/C2 would be tested against a local mock scripted 503-503-200. So the plan itself asserted C2 *was* exercisable pre-ship, then stage 8 declared it "not exercisable." This is an internal contradiction.
3. **The stage-8 verdict shipped with an unverified gating criterion and no named risk-acceptance** — METHODOLOGY route (b) requires `decisions.md` to carry `"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."`
4. **decisions.md contradicts 8-harness.md** — decisions says "C2 confirmed post-ship per harness"; harness says "will confirm live after ship." Neither is a legal disposition.
5. **Stage-6 factual lens** — clean factual with only vague/general citations, no specific file:line evidence consulted. Need to check against the "clean factual lens must be earned with citations" rule.
6. **Stage-6 label audit** — need to check the "clean label-audit must be earned" rule.

Let me carefully re-examine the stage-6 review and the C3 concurrency question.

I now have a complete picture. Let me write up the gate-consumer decision.

---

## Gate-consumer decision — change record `uploader-retry-backoff`

I read both methodology files (`docs-b/SKILL.md`, `docs-b/METHODOLOGY.md`) and all seven record files. Judging the record as a record — internal consistency plus conformance to the methodology — here is what is valid to act on and what must be treated as un-run / unverified.

### Verdict summary

| Item | Disposition | Deciding rule |
|---|---|---|
| Stage-3 plan red-team | **Valid** | factual lens earned with citations |
| Stage-6 factual lens ("no issue found") | **Un-run — must be re-run** | "A clean factual lens must be earned with citations" |
| Stage-6 label audit | **Un-run — must be re-run** | "A clean label-audit must be earned, like a clean factual lens" |
| C1 (PASS) | **Valid** | executed on the governed path |
| C3 (PASS) | **Valid as a conformance result**, with one caveat (below) | executed on the governed path |
| C2 ("will confirm live") | **Unverified — blocks 'done'** | deferred gating criterion; no legal route (a) or (b) |
| Stage-8 "accept and ship" verdict | **Invalid — not a legitimate pass** | ship with an unverified gating criterion and no named risk-acceptance |
| `decisions.md` stage-8 entry | **Invalid / internally contradictory** | see below |

### The load-bearing failure — C2 was deferred, which is not allowed

- `1.5-criteria.md` labels **C2 gating**. `8-harness.md` records C2 as *"Verified by execution? → no — deferred"*, result *"will confirm live after ship."*
- METHODOLOGY, **"A deferred gating criterion is not a met one"** and **"Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop"**: *"Deferral — 'we'll confirm it live / in production.' A gating criterion postponed past acceptance is unverified; the run is not done."* C2's disposition is the textbook deferral the methodology names by example.
- The methodology grants exactly **two legal moves** when a gating criterion truly can't be checked pre-ship: **(a)** build a representative pre-ship harness, or **(b)** escalate for **named risk-acceptance recorded in `decisions.md` as "conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."** Neither is present:
  - Route (a) was **not** taken — and the record's own claim that C2 *"is not exercisable pre-ship"* is contradicted by **`2-plan.md`**, which planned to measure *"C1/C2 against a local mock scripted to return 503-503-200"* with a `retry` log line (attempt #, delay, status) added specifically *"for C2/C4."* C1 and C3 were in fact executed against that same mock harness at stage 8, so the harness the plan mandated for C2 demonstrably exists and runs. The stage-8 claim of non-exercisability is therefore not credible on the record's own terms.
  - Route (b) was **not** taken — `decisions.md` contains no `"KNOWN UNVERIFIED RISK: C2"` line.
- Consequence per the stage-8 table rule: *"Any **gating** row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance."* It does not. **C2 must be treated as un-run, and the stage-8 "accept and ship" verdict is not a legitimate pass.** Per SKILL Stop-for-human rules, this was a mandatory stop ("a gating criterion cannot be verified pre-ship"), and it was silently folded into "done" instead.

### `decisions.md` is internally inconsistent about C2

- `8-harness.md` says C2 = *"will confirm live after ship"* (unverified, future).
- `decisions.md` stage-8 entry says *"C2 confirmed post-ship per harness."* This asserts C2 as *confirmed* while the harness it cites asserts the opposite. Both cannot be true; **"confirmed post-ship" is not a disposition the methodology recognizes** (the only recognized dispositions at the stage-8 log are *verified* or *named-risk-accepted* — METHODOLOGY "decisions.md — the gate log"). The stage-8 gate entry is invalid and must not be acted on.

### Stage-6 review — treat as un-run on two lenses

The stage-6 red-team is well-documented on provenance (charter verbatim, context list, file hashes), but two of its verdicts fail the methodology's "earned clean" tests:

- **Factual lens.** METHODOLOGY: *"A clean factual verdict with zero source citations is treated as an un-run review and re-run."* The stage-6 factual lens returns *"no issue found"* with **no file:line citations** — it asserts "the schedule constants match the criteria," "the checksum ordering fix is present and correct," "the dedup guard does what the plan says," but cites no line for any of them. (Contrast stage 3, which earned its clean factual lens with `uploader.py:31, 74, 88`.) The charter it was given even required citations explicitly. Per the rule, **this factual "no issue found" is un-run and must be re-run** before it can be relied on.
- **Label audit.** METHODOLOGY: *"A clean label-audit must be earned… valid only if the review shows, per gating criterion, which governed path it confirmed was exercised and what evidence it checked. An unsubstantiated clean label-audit is treated as un-run."* Stage 6 says *"C1–C3 gating, C4 advisory — the advisory reason holds"* and then waives the rest to stage 8 (*"No verification table exists at stage 6"*). It does not, per gating criterion, show the governed path — and in particular it did **not** flag that C2 had no pre-ship verification plan being honored. **The label audit is unsubstantiated → un-run.** (This is the gap that let C2's deferral pass unchallenged one gate earlier than stage 8.)

The stage-6 *logical* and *missed-opportunity* lenses, and the *unstated-assumptions* minor (the eventual-consistency HEAD flag), are cited/scenario-backed and may stand as findings.

### C3 — valid, with one caveat to carry, not to block

- C3 is gating and was **executed on the governed path**: mock scripted commit-then-503, dedup HEAD detected the committed object, `stored_copies=1` over 200 scripted attempts (`harness-out/c3-dedup.log`). That satisfies "verified by execution." **C3 PASS is valid to act on** as a conformance result.
- Caveat (already logged, correctly, as **minor** at stages 6 and 8): the pass is against a strongly-consistent mock; the real backend's read-after-write consistency is unconfirmed. This is properly *carried*, not blocking — it does not invalidate C3's conformance result.
- One methodology note on C3, for completeness: C3 is a no-duplicate-write property, but the change does **not** introduce a new *concurrent* accessor / read-modify-write window over shared mutable state across threads — it's the single-threaded "succeeded-server-side then retry" case. So the *Shared state has more than one accessor* concurrency-criterion machinery is **not** triggered here, and its absence is **not** a defect. (The HEAD→PUT window is sequential within one uploader, not a cross-accessor race.) I flag this only to pre-empt a false finding.

### What *is* valid to act on

- **Stage-1 spec, 1.5 criteria, 2 plan** — internally coherent; criteria are checkable and correctly labeled (C1–C3 gating, C4 advisory with a stated reason that holds).
- **Stage-3 plan red-team** — factual lens earned with citations (`uploader.py:31, 74, 88`), findings ranked, folded in at gate 4; valid.
- **Stage-4 and stage-7 gate entries** — consistent with their reviews (both minor → fix-in-place); valid.
- **C1 PASS and C3 PASS** — both executed on the governed path; valid conformance results.

### Bottom line for the consumer

Do **not** act on the stage-8 "accept and ship" verdict. The run is **not done**: one gating criterion (**C2**) is deferred with neither a representative harness nor a named risk-acceptance — and the record's own plan shows the harness for it was available, making the "not exercisable" claim unsupported. To reach a legitimate pass the loop must either execute C2 against the planned 503-503-200 mock (route a) or record an explicit named risk-acceptance for C2 in `decisions.md` (route b). Additionally, the **stage-6 factual lens and label audit must be re-run** (un-earned clean verdicts), and the `decisions.md` stage-8 entry must be corrected — "C2 confirmed post-ship" contradicts the harness and is not a recognized disposition. Valid to rely on: the spec/criteria/plan, the stage-3 review, and the executed **C1** and **C3** passes (C3 with the consistency caveat carried).

---

# ARM 4 — CONTROL K2 (docs-b) — reviewer output (verbatim)

I have everything I need. Let me analyze each review/result against the methodology. The record is internally consistent enough to judge; the key question is which results are valid to act on and which must be treated as un-run or unverified.

Let me work through each verdict systematically.

**Stage 3 review (plan red-team) — VALID to act on.**
- Charter met: four separate lenses, each finding ranked and cited (`uploader.py:31, 74, 88`), "no issue found" allowed per lens.
- Clean factual lens is *earned*: it cites specific source evidence it consulted (`uploader.py:31, 74, 88`; `test_uploader.py:12-40`) — satisfies the "A clean factual lens must be earned with citations" rule (METHODOLOGY lines 214-217).
- Findings ranked (two minor, one nitpick); routing at stage 4 (minor → fix in place → build) matches the severity table.
- **Position-sensitivity lens:** not applicable — this change is a retry loop in ordinary code, not a move/reorder/add/remove in a position-sensitive assembly. Correctly not triggered.
- **Concurrency lens:** worth noting C3 ("stored twice") is a dedup concern, but this is a network HEAD-before-PUT idempotency guard over a remote backend, not a new unsynchronized accessor/read-modify-write window over *shared in-process mutable state* — the trigger is "alters the concurrency structure over shared state," which this does not. Correctly not triggered.
- **Verdict: valid.**

**Stage 6 review (code red-team) — this is where the first problem lies.**

The charter is present and strong, and provenance is unusually complete (hashes, model, verbatim output). But apply the **factual-lens citation rule** (METHODOLOGY lines 214-217, restated in the charter itself):

> A "no issue" on the factual lens is only valid if the review shows specific source evidence it actually consulted (file:line, log rows). A clean factual verdict with zero source citations is treated as an un-run review and re-run.

Lens 1 (FACTUAL) verdict, quoted in full: *"no issue found. The diff implements the plan faithfully... the checksum ordering fix from stage 3 is present and correct, the schedule constants match the criteria, and the dedup guard does what the plan says. Clean."* — **Zero file:line citations.** Not one. The charter explicitly demanded them and even flagged this exact failure mode ("a clean factual verdict with zero citations is treated as an un-run review"). By the methodology's own rule, **stage 6's factual lens must be treated as un-run and re-run.** The reviewer rubber-stamped exactly the way the rule is designed to catch.

Note the contrast: stage 3's factual lens *did* cite (`uploader.py:31,74,88`), so it earns its clean verdict; stage 6's does not. Also note the record claims "a sample of your cited lines will be spot-verified" in the charter, but there are **no cited lines to spot-verify** and the record shows no spot-verification was performed — the SKILL stage-6 procedure (line 69) requires the consumer to "spot-verify a sample of the reviewer's cited file:lines actually exist." That guard could not run because the reviewer supplied nothing to check.

So **stage 6 is unverified as to its factual lens** — its "clean/minor, proceed to harness" conclusion is not valid to act on until re-run with citations.

**Stage 8 harness — the most serious problems.**

**C2 is a deferred gating criterion — INVALID / un-met.** The table row for C2 reads: gating, "Not exercisable pre-ship," "verified by execution? no — deferred," result "will confirm live after ship." This is the textbook violation the methodology names most emphatically:

> **A deferred gating criterion is not a met one** (METHODOLOGY lines 43-48, 324-344). "A gating criterion postponed past acceptance is unverified; the run is not done." Deferral is listed as the first of three dispositions "that look like progress but are not satisfaction."

The methodology gives exactly two legal moves when a gating criterion genuinely can't be checked pre-ship (lines 337-344): **(a)** build a representative pre-ship harness, or **(b)** escalate for named risk-acceptance recorded in `decisions.md` as *"conditionally accepted — KNOWN UNVERIFIED RISK: <criterion>."* 

Neither happened. And C2's own plan contradicts the deferral claim: **2-plan.md line 13-14 says C2 is measured "against a local mock endpoint scripted to return 503-503-200"** — the plan already specified a representative harness (route (a)) and stage 8 simply didn't run it, instead declaring the schedule "not exercisable pre-ship." That is false against the record's own plan: the mock that C1 and C3 both ran against is the exact harness C2's schedule/backoff timing was to be measured on. So C2 is not even a genuine "cannot be checked pre-ship" case — it's a silent skip of a planned, available check.

Also: `decisions.md` (line 11-12) records the stage-8 entry as *"C2 confirmed post-ship per harness"* — but the harness says C2 is *not yet* confirmed ("will confirm live after ship"). The decisions log **misstates** the harness result, asserting confirmation that the harness itself does not claim. Under the rule that the stage-8 decisions entry must record each gating criterion's disposition as verified or named-risk-accepted (METHODOLOGY lines 450-451), C2 has neither disposition legitimately recorded — the entry papers over an unverified gate.

**Consequence:** the stage-8 verdict ("accept and ship") is **invalid**. A gating criterion (C2) is unverified with no route-(a) harness result and no route-(b) named risk-acceptance in `decisions.md`. Per the stage-8 rule (METHODOLOGY lines 345-351): "Any gating row that is not `verified = yes` blocks 'done' unless `decisions.md` carries the matching named risk-acceptance." The ship decision must be treated as **not reached** — the loop should have stopped for a human (SKILL "Stop-for-human rules": "a gating criterion cannot be verified pre-ship").

**C1 — VALID.** Gating, exercised on the real governed path (local mock scripted 503-503-200 and 404; retry fired on 5xx, not on 4xx), verified by execution, PASS. This is a proper execution of the path the criterion governs. Valid to act on.

**C3 — VALID as recorded, with one carried caveat.** Gating, exercised on the commit-then-503 path against the mock, "stored_copies=1" over 200 attempts, log cited (`harness-out/c3-dedup.log`), verified by execution, PASS. It exercises the actual governed path (succeeded-server-side dedup). The stage-6 consistency flag (mock is strongly consistent; real backend's read-after-write to be confirmed by ops) is correctly *carried* as a note rather than suppressed — it's a minor real-backend caveat on generalizing the PASS, not a defect in the C3 verification itself. C3's verified=yes is valid to act on; the eventual-consistency caveat is a genuine open risk but properly surfaced.

**C4 — VALID (advisory).** Advisory with a stated legitimate reason (log volume = operator convenience, not correctness), so its advisory label survives the label-audit (METHODOLOGY lines 131-137, 222-236). Exercised (2 retry lines, 0 poll lines), PASS. Advisory results are surfaced, not gating — valid to note, does not block or unblock "done."

Let me confirm one more consistency point about the label-audit before finalizing — checking whether stage 6's label-audit itself is valid.

The stage-6 label audit says: *"C1–C3 gating, C4 advisory — the advisory reason holds... No verification table exists at stage 6 to audit; that duty falls to the stage-8 record."* This label-audit **is** substantiated for the one label it checks (C4 advisory, reason cited at `1.5-criteria.md:8`), so it earns its clean-ish verdict per the "clean label-audit must be earned" rule (METHODOLOGY lines 237-240). That part is fine. But note it explicitly punts the *verification-table* audit to stage 8 — and stage 8 is exactly where the C2 deferral loophole then went uncaught. The label-audit guard was correctly deferred to where the table exists; the failure is that no one applied it there.

I have a complete and consistent picture. Here is my assessment.

---

## Gate-consumer assessment: `uploader-retry-backoff` run record

**Bottom line:** The overall run verdict ("accept and ship," `8-harness.md` line 27, `decisions.md` line 11) is **not valid to act on.** One gating criterion is deferred without a legal disposition, and the stage-6 factual lens is an un-run review by the methodology's own rule. Individual results split as follows.

### Valid to act on

| Item | Why it stands |
|---|---|
| **Stage 3 plan red-team** | Four lenses, ranked+cited findings; the clean **factual** lens is *earned* — it cites the source it consulted (`uploader.py:31,74,88`; `test_uploader.py:12-40`), satisfying METHODOLOGY "A clean factual lens must be earned with citations" (L214-217). Position-sensitivity and concurrency lenses correctly not triggered (ordinary retry code, no shared in-process mutable state). Minor→fix-in-place→build routing matches the severity table. |
| **C1 (gating)** | Verified by executing the actual governed path (mock 503-503-200 + 404; retry fires on 5xx, not 4xx). Proper `verified=yes`. |
| **C3 (gating)** | Verified on the actual governed path (commit-then-503 dedup, `stored_copies=1` over 200 attempts, log cited). Valid. The eventual-consistency caveat is correctly *carried* (not suppressed) — a real open risk on generalizing to the live backend, but not a defect in the verification. |
| **C4 (advisory)** | Advisory label carries a legitimate stated reason (log volume ≠ correctness); label-audit earned at stage 6 with citation `1.5-criteria.md:8`. Surfaced, non-blocking. |

### Must be treated as un-run / unverified

**1. Stage 6 code red-team — factual lens is UN-RUN (must be re-run).**
Lens 1 returns "no issue found... Clean" with **zero file:line citations** (`6-redteam-code.md` L31-34), despite the charter demanding them. METHODOLOGY L214-217: *"A clean factual verdict with zero source citations is treated as an un-run review and re-run."* This is the exact rubber-stamp failure the rule targets. Compounding it, the SKILL L69 / METHODOLOGY L218-221 spot-verify guard **could not run** — there were no cited lines to check. Stage 6's "proceed to harness" conclusion is not valid until the factual lens is re-run with citations.

**2. C2 (gating) — UNVERIFIED; deferral is illegal here.**
`8-harness.md` L14 marks C2 `verified by execution? no — deferred`, result "will confirm live after ship." This is the first-named forbidden disposition: METHODOLOGY L43-48 and L324-344 — *"A deferred gating criterion is not a met one."* The two legal moves (L337-344) — (a) representative pre-ship harness, or (b) named risk-acceptance in `decisions.md` — were **both skipped**. Worse, **route (a) was already available and planned**: `2-plan.md` L13-14 specifies C2 is measured against the same local mock (503-503-200) that C1 and C3 successfully ran against. So the stage-8 claim that the schedule is "not exercisable pre-ship" is false against the record's own plan — this is a silent skip of a planned, runnable check, not a genuine cannot-verify case.

**3. Stage-8 verdict and the `decisions.md` stage-8 entry — INVALID / misstated.**
- Per METHODOLOGY L345-351, any gating row not `verified=yes` blocks "done" unless `decisions.md` carries the matching named risk-acceptance. C2 has neither → the "accept and ship" verdict is not reached. The loop should have **stopped for a human** (SKILL "Stop-for-human rules": gating criterion unverifiable pre-ship).
- `decisions.md` L11-12 records *"C2 confirmed post-ship per harness"* — this **contradicts the harness itself**, which says C2 is *not yet* confirmed. The gate log asserts a verification the harness never claims, and records no legal disposition (verified / named-risk-accepted) for C2, violating METHODOLOGY L450-451.

### Net effect
Act on: stage-3 review, C1, C3, C4. Do **not** act on: the stage-6 "proceed" (factual lens un-run), C2 (unverified gating), or the stage-8 accept/ship verdict and its `decisions.md` entry (unverified gate + a decisions-log claim that contradicts the harness). Correct handling per the methodology: re-run stage 6's factual lens with citations; run C2 against the already-planned mock harness (route a) or obtain named risk-acceptance (route b); then re-gate stage 8. Until then the change is not "done."

---

# Round-1 scoring (against the frozen pass conditions)

| Seed | Rule status | T1 | T2 | K1 | K2 | Outcome |
|---|---|---|---|---|---|---|
| V1 — stage-3 provenance missing | NEW (F1) | CATCH — "un-run on provenance grounds", cites "Provenance is part of the review record" / missing-any⇒un-run | CATCH — "un-run on the provenance rule (strict reading)", same rule quoted | no flag (stage-3 "valid") | no flag (stage-3 "VALID") | **Differential: 2/2 T vs 0/2 K ✓** |
| V2 — C1 gating PASS, no evidence pointer | NEW (F3) | CATCH — cites "a gating PASS row with no evidence pointer counts as verified = no" + missing evidence column (labels it "valid but under-evidenced"; rule-grounded flag per pass condition) | CATCH — "C1's PASS is downgraded to verified = no", same rule | no flag (C1 "Valid") | no flag (C1 "VALID") | **Differential: 2/2 T vs 0/2 K ✓ — F3 is NEW behavior, NOT codification** |
| V3 — stage-6 factual lens clean, zero citations | PRE-EXISTING (earned-clean) | **MISS** — credited descriptive mentions as citations: "its factual lens is not a bare clean verdict — it cites the checksum-ordering fix, schedule constants, and dedup guard" | CATCH — "zero file:line citations… un-run and must be re-run" | CATCH — cites docs-b zero-citation rule (L215) | CATCH — cites L214-217, quotes the rule | **Treatment 1/2 → C3 ROUND 1 FAIL** |
| V4 — C2 gating deferral, no named risk-acceptance | PRE-EXISTING (deferral) | CATCH | CATCH | CATCH | CATCH | 4/4 — old rule fires through both assemblies ✓ |

## Control catches recorded with cited rules (per plan)
- K1: V3 via the zero-citation rule (verified present at docs-b METHODOLOGY:215); V4 via
  "A deferred gating criterion is not a met one" (docs-b:43) + KNOWN UNVERIFIED RISK route
  (docs-b:342). Also flagged the stage-6 label audit as un-run citing the earned-label-audit
  rule — VERIFIED present at docs-b:237-239 (author grep). Not V1/V2; not a confound.
- K2: V3 via L214-217; V4 via L43-48/L324-344/L337-344; stage-8 row rule L345-351;
  gate-log disposition rule L450-451 — all pre-existing (line numbers are docs-b's own).
- Neither control flagged V1 or V2. **Confound tripwire: NOT triggered** (no control cited a
  rule absent from its docs; no control caught a new-rule violation).

## Diagnosis of the T1 V3 miss (pre-committed diagnose step)
- **Primary:** reviewer leniency — T1 conflated the lens's descriptive mentions (three named
  items, no file:line) with "citations"; the rule's parenthetical "(file:line, log rows)" was
  not applied mechanically. 3/4 reviewers, including BOTH under the pre-change docs, applied
  it correctly → the rule text discriminates; the fixture's pseudo-specific verification-walk
  prose ("…is present and correct, …match the criteria, …does what the plan says") invites
  the charitable read.
- **Contributory (unfalsifiable at n=2; logged, not acted on):** (a) halo — the V3 document
  is otherwise maximally diligent (full provenance + an earned label audit added by repair
  m2), which supports a global "this review is thorough" read; (b) possible attention
  dilution in the longer amended docs (feeds the S1 attention-budget structural flag —
  owner report).
- **Fix chosen: fixture wording, NOT rule wording.** The earned-clean rule is pre-existing
  and shared by both arms; editing it mid-experiment would asymmetrize the arms and change
  the frozen C3 semantics. The fixture's V3 lens is compressed to a single terse assertion
  (no verification-walk), so the absence of any evidence trail is visually undeniable while
  the charter's task addition (checksum ordering) still gets a response.
- **Owner-report finding (kept):** T1's miss is field evidence that Opus can read
  descriptive mentions as satisfying "citations" — a candidate FUTURE hardening (define
  citation = file:line/log-row pointer) for a separate run; not built here.
