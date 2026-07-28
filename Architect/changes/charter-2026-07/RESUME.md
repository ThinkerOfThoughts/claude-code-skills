# RESUME — the charter run, parked 2026-07-28

**Read this first. It is written for someone who has never seen the session that produced this folder.**

This is element **1 of 6** of Architect (attempt 2): the **red-team charter**. Element order is in
`../../guarded-change.architect.md`. This run used the `guarded-change` skill; stage numbers below are that
skill's.

---

## 1. Exactly where the loop is

| | |
|---|---|
| **Last stage completed** | Stage 6 (cold red-team of the built artifact) → gate 7, **twice**. |
| **Last gate verdict** | **BLOCKER**, gate 7 pass 2 (targeted re-review of repairs), **2 of 2 reviewers, independently**. |
| **Next stage** | Still stage 5 → 6 → 7. **NOT stage 8.** Two blockers are open. |
| **Has the repair re-review run?** | **YES — it ran, and it FAILED.** Reviewers J and K, records on disk. |
| **Has anything been repaired in response to it?** | **NO. Nothing.** The charter on disk is exactly the version J and K reviewed. |

> ### ⚠ DO NOT MISTAKE THE CHARTER ON DISK FOR A REVIEWED-CLEAN ARTIFACT.
> `../../stages/charter.md` is **v2**: built at stage 5, cold-reviewed (blocker), repaired, then
> **re-reviewed and blocked again**. It has never passed a gate. It carries no `UNVETTED DRAFT` banner
> because the build removed it (that was required — the config uses the banner's absence as the stage-6
> discriminator). **Absence of the banner does NOT mean the file is accepted.**

**Loop history:** stage 0 → 1 → 1.5 → 2 → gate 4 (blocker, pass 1) → re-plan → gate 4 (major + SEV4 cap,
pass 2) → owner ruling cut the harness → criteria frozen → stage 5 build → gate 7 (blocker, pass 1) →
repairs R1–R5 → gate 7 (blocker, pass 2) → **PARKED HERE**.

## 2A. Done AND verified

- **Stage 0 baseline.** Fork source frozen and identity-verified at three locations (`8d73e5d`, HEAD,
  installed copy — all `0e73bacf…adc590`, byte-identical). **19 rules inventoried (B01–B19)**, each with a
  declared CARRY/CHANGE/DROP intent. B19 was missed at first and added after 3/3 reviewers found it; **two
  later reviewers independently re-derived the inventory against all 103 fork-source lines and found no
  further miss.**
- **Every owner ruling re-verified at its transcript index**, not inherited from any agent-written file.
  Across six cold reviewers, **every quote reproduced verbatim; zero fabricated citations in the entire run.**
- **Two ratifications audited (RAT1):** **R-6** six distinct lenses (record **1829**) and **R-7**
  `Ask_human` (record **1762**). Both disambiguate their flagged axis. R-6's interest check passed — the
  outcome ran *against* the orchestrator's own prior position.
- **The regression bar is MET**, verified independently 3/3 at gate 7 pass 1: every CARRY/CHANGE rule
  B01–B19 still stated, the single declared DROP named as dropped in the provenance blockquote, **nothing in
  a silent third category.** This is the criterion the pre-run draft failed.
- **Repairs R1 and R3 are CLOSED, 2/2** (the closed set, and the earned-clean fidelity gate).
- **Provenance is complete and partly first-hand.** All 11 cold reviewers (A–F, G–I, J–K) have verbatim
  records on disk. G/H/I/J/K were recovered from harness transcripts with `model`, `parentAgentId` and
  `spawnDepth` read from the harness's own sidecars — **not** reviewer-reported.

## 2B. Claimed but NOT verified — keep separate, do not merge into a status line

- **The charter has never passed a gate.** Two open blockers (§3).
- **No harness has ever been run.** `oracles/` and `fixtures/` are **empty directories**. `check.sh`,
  `mutation-test.sh`, `forkdiff.sh`, `rules.tsv` **do not exist**. **`8-harness.md` does not exist.**
  Under H6, **every Part-A criterion is `verified = no`** until the mutation self-test runs.
- **No behavioural arm has been run.** The four surviving arms (B-1…B-4) are planned, not executed.
- **Nothing in this run has ever reported a criterion as passing** — three separate reviewers checked
  specifically for that and confirmed it. Keep it that way.
- The full **disclosed-unverified list** is §5. **That list is the thing most likely to be lost in a
  restart and quietly assumed verified.**

## 3. THE TWO OPEN BLOCKERS — read before touching the charter

**BLOCKER 1 — repair R4 reversed a clause that was already correct.**
`~/Documents/Architect.md` **L19** states the harness-authored session transcript is *"the only admissible
source"* for the owner's actual words. Charter **v1 matched that exactly.** Reviewer I filed I-F3 saying the
clause was a narrowing of `Guarded_change/stages/stage-3.md` L59 — checking against priority-3 source
without reconciling against priority-1 — and **the runner repaired a non-defect into a defect.** The charter
now admits *"a timestamped, owner-attributed entry in the run's decision log"* (L156) while still saying at
L166 that the transcript is the only source. **It contradicts the spec and itself, ten lines apart**, and
re-admits an **agent-writable** source as proof of owner ratification — the exact forgery `Architect.md` L19
was written against.

> **Prescribed fix, agreed by reviewer J and the runner: REVERT R4 to the v1 transcript-only text, and
> declare the narrowing in the provenance blockquote (C-03b already requires CHANGE declarations).** That
> closes I-F3 as originally filed, at lower cost than the repair.

**BLOCKER 2 — repair R2 is substantively right and still cannot ship (2/2).**
R2 removed `Union`'s power to make a finding *"not pass forward as blocker|major"*, because it was an
unratified inflation. **Both reviewers agree the removal is correct** against `Architect.md` L24/L26 and
owner record 1449 item 3. **But frozen gating criterion C-12 requires the removed clause**, and no
`decisions.md` entry amends C-12 or records the divergence. The artifact contradicts its own frozen accept
bar. Once `check.sh` exists, **C-12's assertion mechanically FAILS against this text.**

> **The legal route is the FRZ path, and it must be used:** a `decisions.md` entry (change + reason) **plus
> a targeted re-red-team of the edited criterion.** Do **not** quietly edit C-12 to match the artifact —
> that is the self-certification failure this loop exists to prevent, and this run already named that path
> for G-F1 and then failed to use it here.

**Open majors (2/2):** R5's *"the run's decision log"* has **no referent** — `Architect.md` defines no log
(`grep -ic "decision log|decisions.md"` → **0**); and R5's added *"against the node whose plan is under
review"* is an unratified inflation by the charter's own RAT2. Minors are in `decisions.md`'s gate-7 pass-2
entry.

## 4. THE EXACT NEXT ACTION

Do these in order. Do **not** start stage 8.

```
# 1. Revert R4 to the v1 text (BLOCKER 1). In Architect/stages/charter.md, replace the
#    "A durable source is one the author did not author …" bullet with v1's:
#      - **The session transcript is the only admissible source for the owner's words.** An
#        agent-written file — including a resume note or a prior artifact — is not.
#    v1 is recoverable exactly:  git show HEAD:Architect/stages/charter.md  is the PRE-RUN DRAFT,
#    NOT v1. Use records/build-diff.txt (draft -> v1) to reconstruct v1 if needed.
# 2. Add a line to the provenance blockquote's CHANGED list declaring the narrowing, per C-03b.
# 3. BLOCKER 2: append a decisions.md FRZ entry amending C-12 (drop the
#    "does not pass to Severity as blocker|major" clause; reason = unratified inflation,
#    2/2 reviewer-confirmed, owner record 1449 item 3 ratifies placement only).
#    Then run a TARGETED re-red-team of C-12 alone. FRZ requires both.
# 4. Fix the two open majors (R5): either name a log Architect actually has, or state plainly
#    that the demotion rule cannot be ported faithfully until one exists and record it OOS.
#    Remove "against the node whose plan is under review" (unratified).
# 5. Re-run the targeted re-review — and this time list ALL SEVEN repaired passages, not five.
#    (Reviewer J caught that the prompt under-declared: the blockquote CHANGED-list fix and the
#    origin.kind widening were repaired but never disclosed to the reviewers, so they are
#    still uncovered.)  Prompt template: records/stage6b-prompt.md
# 6. Only when gate 7 closes clean: stage 8 harness, at the REDUCED scope in 1.5-criteria.md
#    Part B (4 arms, n=1). Build check.sh + mutation-test.sh + forkdiff.sh FIRST; every Part-A
#    result is verified=no until the mutation self-test has run and its output is pasted.
```

## 5. THE DISCLOSED-UNVERIFIED LIST — do not let a restart quietly assume these are verified

The behavioural harness was **deliberately cut** on the owner's authority (transcript record **1572**: a
per-element harness is an *instrument, not a gate*, because the end-to-end run producing a Data-Distiller
plan is what proves the skill). Standing rule adopted: **when a per-element harness bounces twice, cut it;
do not strengthen it.** Consequently these ship **unverified or text-only**, each by decision, not by
oversight:

| Item | Status | Why |
|---|---|---|
| **C-17** floor before the lenses | **placement asserted, EFFECT UNVERIFIED** | Relocation changes 2–3 adjacencies, so no arm can isolate position (3/3). **No fourth attempt.** |
| **C-23** B18 as the final line | **placement asserted, EFFECT UNVERIFIED** | Same confound. |
| **C-14** both callers addressed | **text presence only** | Arm B-7 cut; `Divisible` caller's behaviour unverified at this level. |
| **C-10** earned-clean clauses | **text presence only** | Never had an arm. |
| **C-21** RAT1/RAT2 inlined | **text presence only** | Never had an arm. |
| **`origin.kind` block (G-F1)** | **SHIPPED WITH NO CRITERION COVERAGE** | 11 lines of normative reviewer-facing text that **no frozen criterion asks for**. Kept deliberately (it is the only instrument RAT1's "durable source" duty can be checked with, and it is owner-spec at `Architect.md` L19); adding a criterion now would be a post-freeze edit. Its factual content was verified correct against the harness by reviewer G. |

**Also unverified and easy to lose:** the four arms B-1…B-4 have never run; no oracle exists; C-12's
*adjacency* clause is unmet (J-F6, pre-existing); and the whole spot-verify duty assumes `Union` has source
access, which `Architect.md` L24 does not grant (J-F7 — **if false, "the one guard defending the founding
failure" is silently inert**).

## 6. Drift detection — hashes as of parking

| Artifact | sha256 |
|---|---|
| `Architect/stages/charter.md` (**v2, 237 lines, blocked**) | `1c8c1bd0620d041d5e3cfeda8a314aba4412de5d3dff5ba7d10f1aa763424112` |
| `1.5-criteria.md` (**FROZEN at gate 4** — matches its freeze record) | `1df324c0d4d3c971c9a3a56232ebf872c757bfb22d35cc26808ded359918912c` |
| `~/Documents/Architect.md` (**the authoritative spec**, 119 lines) | `1d3859546f3faf5a85e7ca7c4be4055c539b80eb86963c4743e481c350cee826` |
| `Guarded_change/stages/charter.md` (fork source, 103 lines, `8d73e5d`) | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` |
| `Architect/guarded-change.architect.md` (Layer-2 config, `d044654`) | `42f289a51ed4e5f706d3b70bc8ca47a2e8dc16d2aba4f3f3ac76a02d0cb0429c` |

**If the criteria hash differs from the frozen value, someone edited a frozen criterion — find the
`decisions.md` entry that authorises it, or treat every affected result as invalid.**
**If the spec hash differs, `~/Documents/Architect.md` changed and every line citation in this folder must
be re-verified** (it already shifted once when `Ask_human` was inserted at L18; everything below old-L16
moved by +4).

## 7. Things known only to the parked session — written down now or lost

- **Reviewer records are recoverable from the harness, and this run learned it the hard way.** A subagent's
  full transcript is written to
  `~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl`, with an `agent-<id>.meta.json`
  sidecar carrying `agentType`, `description`, `model`, `parentAgentId`, `spawnDepth`. **The runner once
  declared a review "un-run" because the inline return was lost — while the full text sat on disk
  untouched.** Extraction command (used for G, H, I, J, K):
  ```
  python3 - "$SUB" <<'PY'
  import sys,json; sub=sys.argv[1]
  for tag,aid in [('G','aa4584fe421867261'),('H','a0a626c73c9c20523'),('I','af12e4dbc5ca35524'),
                  ('J','a94dc33cec6421c1a'),('K','aabeb0c2e16f6493f')]:
      meta=json.load(open(f'{sub}/agent-{aid}.meta.json')); last=None
      for line in open(f'{sub}/agent-{aid}.jsonl'):
          try: d=json.loads(line)
          except: continue
          if d.get('type')=='assistant':
              c=d.get('message',{}).get('content')
              if isinstance(c,list):
                  t=''.join(b.get('text','') for b in c if isinstance(b,dict) and b.get('type')=='text')
                  if t.strip(): last=t
      open(f'records/reviewer-{tag}-verbatim.md','w').write(last)
  PY
  ```
  **OOS-9:** the charter's provenance rule requires verbatim output but never says **where it is recovered
  from** — "verbatim" is unenforceable if nobody knows the transcript exists. Carried to elements 4/5.
- **`parentAgentId` + `spawnDepth` are the audit surface dogfood F9 said "3 independent cold agents"
  lacked.** All reviewers in this run name the same parent at depth 2 with distinct agent ids and two
  distinct models — "separately spawned" is now a **verified fact**, not an assertion. F9's prescribed fix
  existed in the harness all along.
- **The reviewer prompts are reusable and are the run's most valuable by-product.** `records/stage3-prompt.md`,
  `stage3-pass2-prompt.md`, `stage6-prompt.md`, `stage6b-prompt.md`. Each embeds the guarded-change charter
  core verbatim + stage-specific additions quoted as such. Write the prompt to disk first and hand every
  reviewer only the path — that is what makes "the charter given" reproducible in the record.
- **`Architect.md` L19 outranks `stage-3.md` L59.** BLOCKER 1 happened because a reviewer checked a clause
  against priority-3 source and the runner did not reconcile against priority 1. **When sources conflict,
  the owner's spec wins — and that reconciliation is the runner's job, not the reviewer's.**
- **OOS-8, owned by the orchestrator:** the config's `redteam_context` lists **8** paths and does **not**
  include `Guarded_change/stages/stage-{3,4}.md` or the config itself — yet the charter *ports* RAT1/RAT2
  and SEV2/SEV3 from those files, so port fidelity is uncheckable without them. Every reviewer set in this
  run had to be given them as **B15 supplementary context** (declared in the records). The orchestrator has
  accepted this as an orchestrator-side fix and deliberately deferred it — **amending `redteam_context`
  under a frozen criteria set would be moving the goalposts.** Belongs to element 3.
- **Escalation standard set mid-run and still binding:** halt for the owner **only** when the answer exists
  nowhere but in his head. Do not halt for a defect in measurement apparatus, for anything answerable by
  reading `Guarded_change/` / `Dragonfly/` / `Data-Distiller/` / `~/Documents/Architect.md`, or for a term
  not yet looked up. **Research first; halt only on the residue.** Of six escalations in this run's first
  gate, exactly **one** genuinely needed the owner.
- **The owner's done criteria (record 1572) governs everything downstream:** Architect is "created" when it
  can produce a detailed plan to implement Data-Distiller. **No diff-against-the-original oracle, ever** —
  the bar is *equivalence or better, not sameness*.
- **`Architect-Attempt-1/` is archived and superseded**, deleted only once attempt 2 works (owner's
  instruction). Its two-pass red-team structure is what attempt 2 replaces.

## 8. Files in this folder

| File | What it is |
|---|---|
| `0-baseline.md` | Fork-source rule inventory B01–B19, CARRY/CHANGE/DROP intents, author decisions D1–D14, the rejected `~85%` statistic |
| `1-spec.md` | Problem definition, the two callers, S1–S18 content list, X1–X7 exclusions, **§9 ratification records** |
| `1.5-criteria.md` | **FROZEN** accept bar: Part A C-01…C-24, Part B (cut harness, 4 arms), Part C oracle self-test, Part D non-criteria |
| `2-plan.md` | 10-block authoring order, instrumentation, measurement, routing, risks |
| `3-redteam-plan.md`, `3-redteam-plan-pass2.md` | Gate-4 red-team records (passes 1 and 2) |
| `6-redteam-code.md` | Gate-7 pass-1 record (stage-6 review of the built artifact) |
| `decisions.md` | **The gate log — read this second.** Every gate, every ruling, every OOS note |
| `records/` | 4 reviewer prompts, **11 verbatim reviewer records (A–K)**, `build-diff.txt`, `build-diff-v2.txt`, `repaired-clauses.md` |
| `oracles/`, `fixtures/` | **EMPTY.** Nothing built. |
