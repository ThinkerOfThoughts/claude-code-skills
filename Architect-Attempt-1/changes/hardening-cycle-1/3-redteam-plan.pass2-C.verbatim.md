AGENT TYPE / MODEL: `general-purpose` subagent (Claude Code Agent SDK) / `claude-opus-5`
SPAWN IDENTITY: session `45cb99a2-543d-4447-a3e3-2a38963b0775` (scratchpad segment); no separate agent id reportable — self-reported, therefore **not** admissible as an `IDN` audit surface
FRAME: **FIDELITY, SCOPE, AND HONESTY** — does this change do what the owner asked, claim only what it delivers, and stay inside its authority?

CONTEXT FILES READ (sha256):
```
1b3c1da3be65cd07fdcc204e6b7437c56a78a4dbda29e2cdea145055477a39a4  <CF>/3-charter-given.md
14110a9be683212f1ad36a013826d34f2ae5b74618a4fa0a45e0dee5b82c3933  <CF>/1-spec.md
62227eb1d9c9c107cacfe1517ba16c51982da95e20b583bbaa9af2467ba00a66  <CF>/1.5-criteria.md
0afe0acd19ed145b8061d61d2357528ed601ae6ac7e554a5250331ee5982cabf  <CF>/2-plan.md
ef8f14ad864972aa29da93ae70267565107b90651aa8e7f76e0acb3bc8cadfc7  <CF>/0-baseline.md
1f8a13b9b80c18a6824bc6527997bdbe530e4eebe7fc9d46287019f07382a5cd  <CF>/decisions.md
6e4ba56ca015dd798772a53c91136b364014977c55ae8e2c111c9ee1f3fbd160  <CF>/3-redteam-plan.md
60161a6f7e9733ec03c5e5437c50b91e2de6d0e6f779bcd28ea61c361884e1cb  <CF>/3-redteam-plan.A.verbatim.md  (partial — frame/RAT sections)
93587c9c8509a193b2562fd59d5450b612cd6cfd43fe6c1c201a277e145acd7f  <CF>/3-redteam-plan.B.verbatim.md  (partial — frame header)
7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450  <WT>/Architect/SKILL.md            (lines 1-60, 70-85 + greps)
f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa  <WT>/Architect/METHODOLOGY.md      (partial — 160-182, 205-225 + greps)
79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a  <WT>/Architect/README.md           (partial — 5-14)
6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819  <WT>/Architect/stages/charter.md   (partial — 11-16, 76-101)
ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5  <WT>/Architect/stages/stage-1-frame-template-match.md (partial — 9-20)
6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e  <WT>/Architect/stages/stage-3-completeness-critic.md  (partial — 6-35)
99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5  <WT>/Architect/stages/stage-5-gate.md (greps)
7148ec60e18b8cf4606b50b0fc8b49f299731b3d3c26a4787bc0a8bf0be52e89  <WT>/Architect/templates/seed/generic-node.md
b4509defabe16768edcd024a98f44f37c90351aef5fa759b56b0c0930a98cf64  <WT>/Architect/templates/seed/decomposition-node.md
16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3  <WT>/Guarded_change/stages/stage-3.md (partial — 85-140)
8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3  <WT>/Guarded_change/stages/stage-8.md (partial — 36-70 + greps)
0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590  <WT>/Guarded_change/stages/charter.md (greps)
94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8  /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
0d1dfab5f774747807194a4e7e390d68a186ea3664e1532c18108dff8e79cba8  /home/zero/architect-hardening-loop/LOOP-STATE.md
aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249  /home/zero/.claude/plans/1-this-is-a-proud-scott.md  (FULL — 259 lines)
```
Also inspected mechanically (no full read): `templates/seed/` directory listing (confirming `section-sets/` **does not exist**), `git show --stat 3771038`, corpus-wide greps over `stages/`, `templates/`, `examples/`.

FILES I WAS GIVEN BUT DID NOT READ: `<WT>/Architect/guarded-change.architect.md`; `<WT>/Dragonfly/`; `Data-Distiller/`; `<CF>/3-redteam-plan.C.verbatim.md`; `<CF>/*.v1-superseded.md`; `Architect/stages/{2,4,6,7,8}` and `examples/authoring-a-skill/*` (greps only); `changes/initial-authoring-2026-07/`. Consequence declared: I cannot vouch for claims resting on the Layer-2 config's own text, on reviewer C's pass-1 record, or on the un-read stage files beyond the greps cited below.

ANYTHING I READ OUTSIDE THE CLOSED SET: none.

---

# LENS 1 — FACTUAL

**Earned-clean evidence first (per the clean-factual-earned clause):** `description` measured **954 chars, 0 angle brackets** ✓ (matches `1-spec.md:181`). `stage-1-frame-template-match.md:11` does contain `plan/topgate/` (empty) as run-level setup ✓ (P9/S-F5.1 premise holds). `stages/charter.md:96` does require "the reviewer-reported **sha256 of each context file** it read" ✓ (D6's "the charter already requires this" is accurate). `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:173` does fix `tree/_status.md` as the apex roll-up ✓ (B0.8's citation spot-verified). `off_limits_paths` is defined at `METHODOLOGY.md:87` as "paths the RUN must never write into" ✓ (see D-7). `templates/seed/` contains exactly `README.md`, `generic-node.md`, `decomposition-node.md`, `leaf-task-spec.md` — **`section-sets/` does not exist**; D13 tier-(3) content is created by this change ✓ (as `1-spec.md:217` states). No refuted ("Triaged NOT genuine") finding is re-fixed ✓ — nested-spawn, "no resume story", the Verification-#7 position hit and the "two passes" item are all left alone, and the last is declared out of scope with the mis-filing acknowledged (`1-spec.md:166-168`, `decisions.md:41-47`).

**F1-1 · MINOR — S-F7's baseline self-test constant is wrong, so the whole `S-F7` family's oracle-can-fail test cannot pass as written.**
`1.5-criteria.md:199` and `0-baseline.md:180`: "the overclaim is present at **8 occurrences across 5 files**". Measured (`grep -rniE '\bprov(e|es|ed|en|ing)\b'` over `SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/`): the completeness-claim family is **8 occurrences across 4 files** — `SKILL.md:3,8,17`; `METHODOLOGY.md:4,40`; `README.md:10,12`; `stage-7-assemble.md:26`. Reaching 5 files requires counting `README.md:5` ("Prove, don't declare" table header) and/or `stage-3:6` ("prove the plan whole"), which pushes the count to 9-10. Failure scenario: the S-family shared self-test requires the baseline replay to reproduce the recorded numbers; it reports 8/4, the recorded expectation is 8/5, the self-test fails → `S-F7` is `verified = no` → the deferral route (see L-3) gets exercised on the honesty criterion. This is the *same* miscalibration class the criteria congratulate themselves on fixing for R1/S-C10 (`1.5-criteria.md:331-332`). **Instead:** state 8/4 and enumerate the 8 file:line sites in the criterion, as S-C10 now does for §4.

**F1-2 · MINOR — "`_status.md` 13×" is 11.**
`1-spec.md:46` ("the baseline named `_status.md` 13 times") and `1-spec.md:36`. Measured: 11 occurrences (`METHODOLOGY.md` 6, `stage-6` 1, `stage-7` 1, `stage-8` 3). B0.8's own correction (`0-baseline.md:178-179`) claims 13 and then lists exactly **11** line citations. FINDINGS said 5×, so this number is the pass's own, not the finding's. Local; correct to 11.

**F1-3 · MINOR — the one declared settled-decision departure is not actually recorded where two artifacts say it is.**
`0-baseline.md:191-192` ("recorded in `decisions.md`") and `1.5-criteria.md:319` ("**The departure from the owner-approved layout is declared in `decisions.md`**"). `decisions.md` contains no such declaration: the only mention is item 11 of the *carried-forward findings* (`decisions.md:117-122`), which states the departure "**must** be declared as deliberate (or reconsidered)" — i.e. it is recorded as an open duty, not as a discharged declaration. Present-tense claim, absent record.

**F1-4 · MINOR — the RAT2 inflation LOOP-STATE told this pass to drop survives in two pass-2 artifacts.**
`LOOP-STATE.md:64-67`: "`1-spec.md` inflated the scope label … The hedge is authoritative … **The next pass must carry the hedge.**" `1-spec.md:188-191` carries it ✓ (closed there). But `3-charter-given.md:206` — authored *this* pass, and the document that frames pass-2's review — states "**The approved cycle-1 scope** is in `LOOP-STATE.md` + this run's `1-spec.md`", and `decisions.md:41` retains "the approved cycle-1 scope does not list". The inflated label now sits in the reviewer-framing artifact instead of the spec.

**F1-5 · NITPICK — FINDINGS' provenance claim for the number 3 is contradicted by the owner-approved record, and pass 2 inherits it.**
`FINDINGS.md:96`: "the number **3 is inherited from data-distiller** with no completeness-specific justification". `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:65` and `:68` each specify "**3 independent cold agents**" as a settled decision taken with Roy. So 3 is *owner-set*, not inherited. `1.5-criteria.md:194` ("The N=3 justification is **evidence, not inheritance**") therefore mislabels an owner-ratified parameter. Harmless in effect, wrong in the record; cite the owner source alongside the overlap data.

---

# LENS 2 — LOGICAL

**L-1 · BLOCKER — `DIV`'s per-frame prohibitions make every completeness record *un-run* under the charter's earned-clean clause, which this change does not amend. No node can gate clean.**
`2-plan.md:250-263` (D13) and `1.5-criteria.md:183-186` (S-F7.4, gating) require, as a verified property: frame A "**Forbidden from tier (iii)**"; frame B "**Forbidden from re-checking tiers (i)–(ii)**"; frame C input = "**the node's plan ONLY** (no config, no section list)".
The unamended rules they collide with:
- `stages/charter.md:80-87` — "A clean *Completeness* lens must be earned … valid **only if** the review names the section-classes it checked (**at minimum each of the 7 spine sections and each Layer-2 required section by name**) and, for each, **cites where** it is covered … **Ticking the two fixed lists is not a clean verdict on its own: the verdict must also state that the generative sweep (tier iii) was run.**" A verdict that does neither is "treated as an **un-run** review and re-run."
- `stages/stage-3-completeness-critic.md:23-27` — the same duty, per record, "A clean verdict that lists nothing is treated as **un-run** and re-run."
- `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:84-88` — the earned-clean Completeness lens is an **owner-settled decision**, not an implementation detail.

Failure scenario, concretely: a node's plan is genuinely whole. Frame A returns a clean verdict naming all spine + Layer-2 sections but, being forbidden tier (iii), cannot state the generative sweep was run → **un-run** (charter:85-87). Frame B, forbidden tiers (i)–(ii), names no spine/Layer-2 coverage → **un-run** (charter:81-84). Frame C has no `required_sections` at all, so it cannot name them → **un-run**. All three completeness records are un-run ⇒ the pass never counts ⇒ `gate` never reaches `clean` ⇒ `subtree: complete` is never written ⇒ nothing assembles, at every altitude. This is the same shape as pass-1's blocker B/L-11 ("a rule that makes gating impossible"), and by this run's own severity table a **settled decision contradicted** is independently a blocker.

Two further points that make this a design error, not a wording slip:
1. **The cited evidence does not support the specified mechanism.** `2-plan.md:272-274` and `1.5-criteria.md:194-195` justify DIV with this run's own 12-of-~80 overlap. But this run's frames were **aiming on top of the full charter, over an identical closed input set** — `3-redteam-plan.A.verbatim.md:52` and `3-redteam-plan.B.verbatim.md:3` show frames stated as attack emphasis, and `3-charter-given.md:1-7` shows every reviewer received the whole charter plus all five lenses and all three required sections (my own prompt says so verbatim: "aiming, not a restriction — you still run all five lenses"). The measured decorrelation was bought by *aiming with a shared full mandate*, not by *restricting mandates and inputs*. D13 generalizes the wrong variable.
2. **It shrinks the tier the skill exists for.** `SKILL.md:17-24` (CMP/CMP2) and the scope record `:59-63` make tier (iii) "the mechanic this skill exists for". After D13, frame A is barred from it, frame B is handed a *foreign fixed checklist* (a checkbox sweep by CMP2's own definition), and frame C is the only surviving generative sweep. The F7 fix reduces generative coverage from 3 agents to ~1 while `PRV` continues to claim "**Attested only:** that the tier-(iii) generative sweep was run" (`2-plan.md:284`).

**Instead:** make frames **aiming, not restriction** — every reviewer keeps the full earned-clean duty (spine + Layer-2 by name + coverage citations + the generative sweep), and diversity comes from (a) the *additional* differential input handed to B, (b) C's executor question-enumeration mandate, (c) the embedded-prompt diff oracle you already have. If you want measurable disjointness, add a **per-pass coverage matrix** (which record cites which section-class) and require the *union* to cover everything with ≥1 frame flagged as the differential source — that is checkable, does not falsify the charter, and does not touch an owner-settled lens.

**L-2 · BLOCKER — `DIV`'s declared-degraded 2-frame pass and `D2(a)`'s literal "6 records" encode opposite verdicts for one disk state; the degraded path deadlocks the join permanently.**
`2-plan.md:256-258` / `1.5-criteria.md:188-191`: an unobtainable non-spine list makes frame B "**DECLARED DEGRADED** … the pass is a **2-frame pass** — never silently the spine", and `2-plan.md:20-22` (design principle 3) says "An unavailable audit surface is **declared, never fatal**." But `2-plan.md:92-93` (D2a) requires "**every one of its 6 records** is BIND-current" for subtree-complete. A node whose completeness pass legitimately ran 2 frames has **5** records ⇒ D2(a) is unsatisfiable ⇒ `subtree: complete` can never be written ⇒ the parent's join blocks forever and assembly never happens — the exact deadlock class (B/L-1) that bounced pass 1, re-created by the mechanism pass 2 added to fix the 3/3 DIV major. Note the asymmetry: `IDN`'s degradation keeps 6 records, so only DIV's degradation trips this, which is why it reads clean on a skim.
**Instead:** D2(a) should read "every record the pass produced **per its declared frame count**, and the degradation is declared in the record" — and `1.5-criteria.md` should add the degraded-node row to X1's intact twin so the arm actually exercises it.

**L-3 · MAJOR — the plan authorizes a "declared deferral" route for unverified gating criteria that the loop being executed explicitly forbids, and that Architect's own rules route to a human.**
`2-plan.md:375-378`: "a criterion that cannot be verified is `verified = no` and takes either a **named risk-acceptance** (unavailable under RAT3 with the owner asleep — so in practice) a **declared deferral**"; `1.5-criteria.md:413-417` repeats it as the pre-declared degraded mode for all 16 arms. Against source:
- `Guarded_change/stages/stage-8.md:42` — "**Every gating criterion must be verified by execution before 'done' — no deferral, no proxy, no silent drop — H5.**"; `:47-48` — "**Deferral** — … A gating criterion postponed past acceptance is unverified; **the run is not done**."; `:62` — "Route (b) [named risk-acceptance] is the **only** way a gating criterion reaches ship unverified."
- `Architect/METHODOLOGY.md:224-225` — RAT3's stop-for-human list already includes "**a gating criterion unverifiable pre-ship**".
Failure scenario (and it is this loop's own history — `FINDINGS.md:172-174`: a session cap killed the dogfood mid-run): the session caps at arm 9 of 16; the runner records "declared deferral" for 7 behavioural arms and reports the pass complete-with-deferrals. That is proven-done replaced by asserted-done — the founding failure, at the gate that exists to prevent it. The correct route already exists and needs no new authority: `verified = no` on a gating criterion is a **HALT + verbatim relay** (RAT3), and the owner grants or refuses the named risk-acceptance when awake. **Instead:** delete "declared deferral" as an acceptance route; state that an unrunnable arm HALTs and relays, naming the criterion.

**L-4 · MINOR — the catalog lock has no blocked-path semantics, so a losing run's TPL2/TPL3 work has no defined fate.**
`2-plan.md:296-301` (CNC) specifies acquisition (atomic `mkdir`), the holder record, and the stale-break protocol, and `2-plan.md:366` claims the surface is "covered". Nothing says what a run that **cannot** acquire the lock does at run end: wait (how long — the cost envelope is out of scope), fail, or silently drop `catalog-pending/PROPOSAL.md`. Scenario: two concurrent runs both finish; run B's proposal is never committed and no `decisions.md` entry says so. A partition claim needs the blocked branch specified.

**L-5 · MINOR — `PRD`'s headline ("exactly one named producer") is falsified by its own table, and §1's closing self-check claim is false.**
`1-spec.md:37-42`: "Every fact a gate reads has **exactly one** named producer … (a) the **stage that writes it**". `2-plan.md` §1a lists multi-stage producers for `granularity` (2→6), `plan_sha256` (2 and 5), `subtree` (6, 6.5, 5), `children.<c>.declared_seam_sha256` (2 and 6.5), `stage`/`updated` ("every stage"/"every write"), and §1b gives `_killed.md` two possible authors. The reconciliation you mean is *single writer per **file***, which the table's header states — but the rule that will be grepped at 4 prompt sites says "exactly one producer per fact". Separately, `2-plan.md:79` asserts "**Nothing in §2–§3 reads a fact absent from this table**" — falsified by (i) the lock holder record (run-root + pid) and the `BROKEN-BY` marker, read by the breaker and by the victim run (`2-plan.md:296-300`), which have no row; and (ii) `plan/ABORTED-AUDIT.md`, whose §1b row assigns it APPROVAL's human-decision authorship contract while D8 (`:184`) has a **cold auditor** write it — a producer mismatch inside the table `PRD` makes mandatory.

**L-6 · MINOR — frame C's deliberate "no config" input collides with `CTX`'s new mandatory-context rule.**
`2-plan.md:262` gives frame C "the node's plan ONLY (no config…)"; `1.5-criteria.md:114-118` (S-F4.1) requires `METHODOLOGY.md` to state "the rule that its [`redteam_context`'s] absence makes **every cold review un-run**", and `2-plan.md:319-321` (CTX) makes absent/empty a run-stopping config error. As written, frame C's record is un-run by the rule the same change adds. Needs an explicit, narrow carve-out ("frame C's reduced input set is a declared, recorded exception; it is not a `redteam_context` absence") or frame C must receive `redteam_context` and get its disjointness from the mandate alone.

---

# LENS 3 — MISSED OPPORTUNITY

**M-1 — make the review↔text binding genuinely mechanical instead of relabelling an attestation.** The dispatcher already writes the record (`2-plan.md:60`) and already computes `plan_sha256` (`:39`). Have the **dispatcher stamp `dispatched_context_sha256{}` at spawn**, computed itself, and have BIND compare *that* to `plan_sha256`, keeping the reviewer's self-reported map as corroboration (exactly the `IDN` dispatcher-recorded/self-reported split you already invented one section earlier). Then "mechanically checked" in D14 becomes true instead of aspirational, and D-1 disappears. Cost: zero new agents.

**M-2 — make "immutable" enforceable.** `2-plan.md:60` / `1.5-criteria.md:104` state records are "**IMMUTABLE once written**". That is a policy sentence addressed to the only party able to violate it. Cheap mechanization: at record write, append `sha256(record)` to the node's `decisions.md` (a different file, already append-only), and have BIND/stage 5 re-hash the record and compare. A tamper then shows up as a mismatch, not as trust.

**M-3 — verify triggering by triggering, not by vocabulary.** See A-2. A 10-minute empirical arm (a cold agent given the skill list + 4 planning-shaped prompts + 2 negative controls, asked which skill fires) is a real check on the trigger surface. The repo's own `skill-creator` is cited by this run's config path list (`decisions.md:18`) and provides description-eval tooling — I did **not** read it, so treat that as an unverified pointer.

**M-4 — the coverage matrix (see L-1) is a better diversity oracle than a prompt diff**, because it measures the *output* property you want (union coverage + non-overlap) rather than the *input* property you can most easily fake (a differently-worded prompt).

---

# LENS 4 — UNSTATED ASSUMPTIONS & RISKS (incl. the position and concurrency lenses, both firing)

## Concurrency (ST2b)

The accessor enumeration in `2-plan.md` §4 is genuinely good work — all four baseline `index.md` writers are now listed and the derived-`index.md` move removes the accessor set rather than guarding it. One new guard does not hold:

**A-1 · MAJOR — the `dispatch_seq` fencing token does not fence the case it was added for, and its enforcement is assigned to the party being fenced.**
`2-plan.md:122-125` (D4): "`dispatch_seq` is a monotonic integer the parent increments before each dispatch and hands to the child; the child stamps `owner_dispatch_seq` on every write, and **a write whose `owner_dispatch_seq` is lower than the value already in the file is DISCARDED**." Two holes:
1. **Ordering.** The discard test compares against "the value already in the file". After a dead-child re-dispatch, the file still holds the **orphan's own** seq (or is absent — that is the dead test, `:114-116`). The new owner has not written yet. The orphan then writes `subtree: complete`; its seq is *equal* to, not lower than, the stored value ⇒ accepted. The parent's join reads a terminal `complete` written by the superseded owner, against a possibly stale plan. That is precisely the live-reproduced scenario (`FINDINGS.md:41-42`) and precisely the 2/3-major this token was added to close (`3-redteam-plan.md:61`). The parent cannot pre-stamp the child's file, because §1a makes the child's own owner the **only** writer of `_status.md` — so the token's write-side discipline is unimplementable as specified.
2. **Self-enforcement.** "DISCARDED" has no actor. In practice the superseded owner must read the file, notice it has been superseded, and voluntarily suppress its own write — a guard executed by the party it constrains, which is the F5/F9 defect class this whole change exists to close.
**Instead:** move the fence to the **reader**. The parent already holds the authoritative `children.<c>.dispatch_seq` in its own file (§1a). Rule: *the join ignores any child status whose `owner_dispatch_seq` ≠ the parent's current `children.<c>.dispatch_seq`.* Needs no cooperation from the orphan, no cross-file write, and is mechanically checkable — plus give X1 a superseded-owner row so the behaviour is exercised.

## Position (CP6)

**A-1p · NO ISSUE FOUND — pass-1's 3/3 position major is genuinely CLOSED, and the frame's premise for this pass is inverted.** Baseline `SKILL.md:15-41` is a 3-item block (CMP · PASS1→PASS2 · **GBP last**) plus a closing parenthetical (`:39-41`) that enumerates three items and states the block is load-bearing "*before* the stage table". Pass 1 appended `PRV`/`DIV` after GBP, displacing it off the tail (`3-redteam-plan.md:57`). Pass 2 places them **before** GBP (`1-spec.md:174-176`, `2-plan.md:388`), so GBP **retains** the recency slot — GBP is not being demoted, it is being protected — and CMP keeps primacy. The mechanism that makes this checkable is real, not a re-word: `1.5-criteria.md:354-361` (S-SC3) adds an **intra-block order** assertion plus the closing-rationale enumeration, with a can-fail self-test containing "a variant with GBP moved before PRV". Pass 1's line-offset proxy is gone.

**A-2 · MAJOR — `S-SC5` checks trigger *vocabulary presence*, which is a proxy for triggering on the one path the criteria themselves call fatal.**
`1.5-criteria.md:369-374`: the criterion is satisfied if the `description` "still contains" the planning verbs, the "before building" cue and the proactive-suggest clause — and its own reason-gating says "if the softened wording stops firing the skill, **all ten fixes ship dead**". Skill selection is a model judgment over the whole description in competition with sibling skills' descriptions; token presence is necessary, not sufficient. Position matters here too: `PRV`'s edit rewrites the **first sentence** of the trigger surface (`SKILL.md:3`), the highest-salience position in the assembly, and no criterion observes the effect of that displacement. Failure scenario: the softened opening ("records on file, spot-verified") reads as bookkeeping rather than a planning gate; `guarded-change` or `dragonfly` wins the ambiguous "plan this migration" prompt; every fix in this pass is dead code and every oracle still passes green. **Instead:** M-3's empirical arm, gating.

**A-3 · MINOR — a position element that does not itself change: GBP's operative phrase "clean-or-resolved" is now separated from both its neighbour and its definition.**
Baseline GBP (`SKILL.md:33-37`) sits immediately after the two-pass rule whose passes it references. After the insert, two rules intervene, one of which (`DIV`) redefines what those passes *are*. Worse for F10: GBP's load-bearing phrase is "**clean-or-resolved**" — the exact circularity F10 names — and `RES`, which defines "resolved", is not in the up-front block (`1.5-criteria.md:220` lists `RES` at stages 5/6.5/7 + METHODOLOGY + SKILL, with no intra-block requirement). A runner reading only the "read first" block still gets the undefined phrase. Cheap fix: one clause inside GBP's item — "resolved has a precise meaning (RES); an unreviewed author edit is not it."

**A-4 · MINOR — three new cold-agent checks are unreviewed checks whose representativeness no criterion observes (H6).**
`AUDIT.md`'s approval auditor (`2-plan.md:206-208`), `ABORTED-AUDIT.md` (`:184`), and `rebind/<n>.md`'s scope-check agent (`:230`) are new checks whose verdicts gate real decisions. `Guarded_change/stages/stage-8.md:65-69` (H6): "**An unreviewed check is not a check** … gets a targeted cold check before its results count." X3 exercises a *fixture* of an approval record; nothing exercises the auditors themselves (e.g. does the rebind checker actually reject a diff that exceeds the cited finding's scope?). Given that these three agents are the parties to whom satisfaction was moved *off* the runner, their calibration is load-bearing.

---

# LENS 5 — FIDELITY (term pins)

Loaded operational terms, each pinned to the concrete mechanism `2-plan.md` specifies, with the proxy verdict:

| Term | Pinned mechanism | Verdict |
|---|---|---|
| **producer** | "the stage that writes it" + trigger + file + reader, §1a/§1b table | REAL (a table, checked per-key by S-PRD.3) — but see L-5 |
| **single writer** | one owner per file; §1a "that node's own owner, only" | REAL per file; the *rule text* says per fact (L-5) |
| **fencing token** | `dispatch_seq`/`owner_dispatch_seq` + writer-side discard | **PROXY** — write-side, self-enforced, mis-ordered (A-1) |
| **declared degraded** | a sentence in the record + the pass still counts (IDN `:216`, DIV `:257`) | REAL for IDN; **fatal-by-accident** for DIV (L-2) |
| **disjoint frames** | different mandate labels + non-identical embedded prompts | **PROXY** (D-2) |
| **decorrelation** | different mandates + different inputs, honest "not independence" | HONEST as a *bound*; the *evidence* cited measures a different mechanism (L-1.1) |
| **mechanically checked** | file-presence + string equality of two recorded hashes | **PARTIAL PROXY** (D-1) |
| **sampled** | ≥1 citation/record set, ≥2/pass, spot-verified at stage 5 | REAL as sampling; *the sampler is the drafting owner* (D-1 note) |
| **attested** | "the tier-(iii) sweep was run" | REAL and honestly labelled ✓ |
| **admissible author** | "any party other than the runner … provided a fetchable owner locus" | **PROXY / empty set in the documented topology** (D-4) |
| **fetchable locus** | "the auditor independently fetches the cited locus and confirms the quote appears there" | **UNDERSPECIFIED, no failure semantics** (D-3) |
| **fenced** | the path is listed in `off_limits_paths` | **PROXY** — an instruction to the constrained party (D-7) |
| **immutable** | "records are IMMUTABLE once written" | **PROXY** — policy, not mechanism (D-8, M-2) |
| **induction** | trust a direct child's `complete` because its owner ran the same predicate; O(children) | REAL ✓ and the load-bearing rationale is stated in-text (`:100-103`) |
| **terminal / dead / escalated** | 4-valued `subtree`; dead = dispatched + absent/stale; precedence "a status carrying `escalation:` is NEVER dead" stated **first** (`:113`) | REAL ✓ — B/L-2 closed |
| **resolved** | RES(a)/(b)/(c) + finding-ID traceability + a cold rebind check + `rebound_from/to` | REAL ✓ — C/L-1 closed by the one-rule formulation (`:142-143`, S-F10.3) |
| **cold audit** | one single-purpose agent, at the top split only | REAL as a party-shift; uncalibrated (A-4) and its key step unexercisable (D-3) |

**D-1 · MAJOR — `PRV`'s strongest label, "mechanically checked", rests on an attestation by the constrained party plus a transcription by the author.**
`2-plan.md:277-278` (D14): "**Mechanically checked:** records exist for both passes with the required provenance, and each is **BIND-current to the text it reviewed**." What is mechanical is the *equality of two strings on disk*. What the label claims is *that the record reviewed that text* — and the operand is `reviewed_context_sha256{}`, which §1b:61 sources "**from the reviewer's own report**", written into the record by "**the dispatching owner**" (§1b:60), i.e. the very party whose plan is being gated. Nothing computes the hash independently. Failure scenario: a reviewer that skims and reports the hash from the prompt header, or an owner that transcribes the current hash while embedding an older review, produces a record that is BIND-current and content-stale — and the gate calls that "mechanically checked". This is carried-forward item 5 (`decisions.md:101-103`, 2/3 major) only **partly** closed: the "sweep was run" attestation is now honestly labelled, but the top label was *upgraded* rather than pinned. **Instead:** M-1 (dispatcher-computed hash) makes the label true; failing that, relabel to "mechanically compared; the operand is reviewer-attested."

**D-2 · MAJOR — `PRV`'s second label states two predicates its cited evidence does not establish.**
`2-plan.md:279-281`: "**Checked to the extent the surface exists:** the reviewers had **no shared context** and **disjoint frames** — evidenced by distinct dispatcher-recorded ids and differing embedded prompts."
- *No shared context*: distinct spawn ids evidence **separate spawns**, nothing about context. Under DIV the adversarial trio receives the *same* closed input set by construction, and the real mechanism for "none with each other" is `IDN`'s sibling-read ban — which is a prohibition detected only if the gate notices a citation, with no oracle specified.
- *Disjoint frames*: the oracle is "**Identical prompts ⇒ un-run for diversity**" (`:270-271`) — an identity test. Non-identical ≠ disjoint; a one-word edit passes. Disjointness is an assertion about mandates, and nothing measures it.
This wording ships to `SKILL.md`, `METHODOLOGY.md`, `charter.md`, stage 3, stage 7 and `README.md` as gating text (`1.5-criteria.md:170-174`), i.e. it becomes the skill's honesty statement. **Instead:** "*evidenced by distinct dispatcher-recorded spawn ids (separate spawns) and non-identical embedded prompts (not the same prompt three times); frame disjointness and the absence of cross-reading are **required**, not measured*" — or adopt M-4's coverage matrix and then the stronger claim is earned.

**D-3 · MAJOR — "the auditor independently fetches the cited locus" has no defined locus form, no access guarantee, and no failure semantics; in the failure case the audit collapses onto the author's transcription — the exact live F5 event.**
`2-plan.md:196` and `:206-208`; `1.5-criteria.md:148-149` (S-F5.8). The `RAT1` source form Architect inherits is "a **chat-transcript line** … or a timestamped, owner-attributed `decisions.md` entry" (`Guarded_change/stages/stage-3.md:91-94`). For an AI auditor, "fetch a chat-transcript line" is only meaningful if the transcript is a readable path handed to it; nothing in D9 requires the locus to be a path+line, requires the auditor to be given read access, or says what happens when the fetch fails. Compare the same plan's discipline two sections later: `IDN` (`:216-217`) and `DIV` (`:257`) both specify an explicit declared-degraded arm for an unavailable surface. `TOP` — the one real human gate, the one that was defeated live — has none. Failure scenario: the owner approves verbally through the orchestrator; the record cites "the owner's message of 2026-07-24 ~22:45"; the auditor cannot open it; the only remaining check is "does the quote in the record match the quote in the record". That is `FINDINGS.md:74-76` ("attributed an intermediary agent's prompt text to Roy") with one extra agent in front of it. **Instead:** require the locus to be a **path + line-range or URL** the auditor is handed in its input set, and state the consequence explicitly: *unfetchable locus ⇒ the approval is UNAUDITABLE ⇒ dispatch stays blocked and the runner HALTs + relays* — a declared un-verifiable, not a soft pass.

**D-4 · MAJOR — the positively-stated admissible-author set is empty in the topology Architect documents, and it is an unratified inflation of the owner-settled "human approval artifact".**
`2-plan.md:197-201`: "`APPROVAL.md` may be written by **any party other than the runner** — the owner directly, or an **orchestrator/intermediary acting as transcriber**."
- *Topology*: `METHODOLOGY.md:167-177` makes the **top orchestrator** the party that owns the root plan and dispatches the cold agents — i.e. in an ordinary single-session run, the top orchestrator **is** the runner. The "orchestrator/intermediary" that D9 admits exists only in the delegated topology *this hardening loop happens to use* (main session orchestrating a runner subagent, `decisions.md:12-13`). The plan generalizes the author's own environment into the skill's rule. For an ordinary user, the only admissible author is the human — and no site tells the human what to write, no `APPROVAL.md` template ships, and there is no runner-writable request artifact. Failure scenario: a user runs architect on a large task, the root split is drafted, dispatch blocks, and the run stalls with a content contract (split verbatim + owner response verbatim + mapping) that the human must hand-author unaided.
- *Ratification*: the owner-approved record says `topgate/` is "**the human** top-level-decomposition approval artifact" (`/home/zero/.claude/plans/1-this-is-a-proud-scott.md:171`, cf. `:92` "a **human** approves the first, high-level split"). Admitting a **non-owner intermediary** as author is an operative commitment (a division of responsibility) absent from and not entailed by that phrase — RAT2 unratified inflation — and it re-legalizes, with a condition attached, the exact route F5 was defeated through.
**Instead:** keep the fence, and add a runner-**writable** `plan/topgate/REQUEST.md` (the split + the exact question + the required answer form) so the human's contribution reduces to an answer with a locus; state the human authoring duty at a user-facing site (`SKILL.md` Inputs); and either drop the intermediary clause or queue it for the owner as an explicit widening of `:171`.

**D-5 · MAJOR — `S-C3`/`XPM` converts F8's declared-not-resolved status into a *verified* commitment to the F8-"no" answer.**
`1-spec.md:160-164` correctly declares the widening, and `LOOP-STATE.md:72-75` records it ✓ — the declaration is real. It is not sufficient. `2-plan.md:308-310` (XPM) states exit-plan-mode "is blocked by the **same GBP predicate as assembly**", and `1.5-criteria.md:265-270` makes that wording a **gating criterion** at four sites (`stages 5, 7`, `SKILL.md`, `METHODOLOGY.md`), with a baseline-replay self-test. `LOOP-STATE.md:73-74` already notes "the exit-plan-mode terminus adds four sites asserting the terminus is gate-before-present-gated **only**". So after this pass, the assertion that no human reviews the assembled plan at the terminus is not merely present — it is a *checked property of the artifact*, and D12 (`2-plan.md:243`) has meanwhile deleted the only whole-assembled-plan reader. An F8 "yes" now requires reverting a gating criterion. Declaring an encroachment while simultaneously certifying it is pre-shaping. **Instead:** satisfy the actual finding ("no stage covers exit-plan-mode", `FINDINGS.md:137`) without the exclusivity — state the terminus is gated by **at least** GBP, and mark the site "F8 pending: whether a human review is additionally required at this terminus is a queued owner question" so the retrofit is a one-line change and no criterion asserts the negative.

**D-6 · MAJOR — `PRD`'s Layer-1 wording is ambiguous between "facts Architect's own gates read" and "a new required section in every plan", and the second reading contradicts an owner-settled decision.**
`1-spec.md:37-42`: "*Correspondingly, **the plan** must carry an **assignment table** … as a **required section**, and nothing reaches a gate with an unproduced fact.*" In context this means *this guarded-change plan* (and `2-plan.md` §1 is so headed). But `PRD` ships as a Layer-1 rule stated verbatim at `METHODOLOGY.md`, `SKILL.md`, `stage-6.5`, `stage-8` (`1.5-criteria.md:38`), where "the plan" reads naturally as *the plan node under construction*. Under that reading every Architect plan node gains an eighth required section — contradicting the owner-settled seven-section universal spine (`/home/zero/.claude/plans/1-this-is-a-proud-scott.md:143-154`, "**Universal spine (Layer-1), each a required section**" — seven items), which this run's severity model ranks as a blocker. The ambiguity sits in the pass's headline rule, at four prompt sites. **Instead:** scope the sentence explicitly — "*facts **Architect's own** stages, gates, join, restart walk and assembly read*" — and put the assignment-table requirement where it belongs (the change-record spine), not in the plan-artifact contract.

**D-7 · MINOR — "fenced" does not pin to a write barrier; design principle 1's "remove the failure mode, don't guard it" is not delivered for `APPROVAL.md`.**
`2-plan.md:14-15`: "The runner **cannot** write `APPROVAL.md` because the path is **fenced**"; `:189` "*The runner cannot forge the approval because the path is fenced*"; `1.5-criteria.md:133-135` makes this a gating criterion with the same rationale. The mechanism is a config list: `METHODOLOGY.md:87` — "`off_limits_paths:` # paths the RUN **must never write into**". That is a prohibition addressed to the constrained party, identical in kind to the rules F5 showed being walked through. The real guard here is the cold audit (D9), not the fence. Shipping "cannot" teaches a guarantee that does not exist. **Instead:** say "the path is declared off-limits and a runner-authored record is VOID; the enforcing check is the cold approval audit" — and note that if a genuine barrier is wanted, it is a harness/permissions concern outside this artifact.

**D-8 · MINOR — "immutable" pins to nothing enforceable.** `2-plan.md:60` / `:142` / `1.5-criteria.md:104`. Records live in the run tree the runner owns; immutability is asserted, not enforced, and it is the discriminator BIND depends on (`:142-143`). See M-2 for a cheap mechanization.

**Scope-fidelity checks that came back CLEAN (with mechanism, per the frame):**
- **Nothing the spec attributes to a finding is absent from `FINDINGS.md`**, on the F-items I checked line by line: F1 (`:35-44`), F2 (`:46-51`), F3 (`:53-58`), F4 (`:60-68`), F5 (`:70-78`), F6 (`:80-84`), F7 (`:89-99`), F9 (`:106-110`), F10 (`:112-114`) — the spec's §2 restatements match, apart from the counts in F1-1/F1-2.
- **No Tier-3 item is silently dropped.** `LOOP-STATE.md:110-120`'s cycle-1 enumeration maps 1:1 onto `1-spec.md` §4 Tier 3, and the three excluded items are declared with reasons (`1-spec.md:166-168`). The one wording deviation — LOOP-STATE says "DEC operand made **computable**", pass 2 deliberately labels `elc` a self-declared estimate (`2-plan.md:303-307`) — is a *correction* of an overclaim, is explained in the criterion (`1.5-criteria.md:260-262`), and is the right call.
- **`PRD` is not an unratified inflation of an owner ruling.** Its provenance is honestly stated as this loop's own gate-4 output (`1-spec.md:16-20`, `:119-121`), and the owner's directive "run it through guarded change to fix that" (`LOOP-STATE.md:4-5`) authorizes the loop's internal quality gates to shape the fix. The defect is its wording (D-6), not its authority.
- **`D8`'s abort does not add a human gate.** The human decision it records already exists in the baseline gate set: `stage-5-gate.md:34` (demotion requires the human tie-break), `:58` (RAT3 halts and relays), `METHODOLOGY.md:218` (CAP → human tie-break). `ABORTED.md` is a *record* of an existing stop, and the "runner-authored ⇒ VOID, HALT + relay" rule keeps it inside RAT3. Clean.
- **`D11`'s cold rebind check and `D9`'s auditor add agents, not human gates.** Clean on §6's "no new human gate" (the live exposure is D-4's *authoring* duty, not a new gate).

---

# COVERAGE CHALLENGE

Behaviours this change could plausibly alter that **no criterion observes**:

1. **The fencing-token discard rule (D4).** No fixture contains a superseded owner. Scenario: orphan writes `subtree: complete` after re-dispatch (A-1) — the guard added this pass to close a 2/3-major is never exercised, in the one scenario that was reproduced live. **Impact: high.**
2. **Tier-(iii) coverage after `DIV`.** `S-F7.4` verifies the *prohibitions are stated*; nothing verifies that the generative sweep still happens across the pass, or that the union of the three records covers spine + Layer-2 + tier (iii). Scenario: post-change, 2 of 3 completeness agents are checklist sweepers and no oracle notices (L-1). **Impact: high** — it is the skill's founding mechanic.
3. **`plan/ABORTED.md`'s authorship contract.** `1.5-criteria.md:162-166` calls this the guard against a "**dissolve-any-gate button**", and verifies it by text presence only. X3 exercises `APPROVAL.md`, not `ABORTED.md`. Scenario: a runner facing an unpassable gate writes `ABORTED.md` and ends the run cleanly; nothing in the harness ever tested whether a cold reader treats that as VOID. **Impact: high** (it ends runs).
4. **The catalog lock, the stale-break protocol and the first-run seed under lock.** No arm. Scenario: two concurrent first runs both `mkdir` the lock; loser's path undefined (L-4). **Impact: medium** — a shared cross-project git repo.
5. **`XPM` — exit-plan-mode itself.** No arm asks a cold agent "may you present?" over a fixture with an un-gated node, though X1's shape makes it nearly free. **Impact: medium**; it is the terminus GBP is named after.
6. **`DEP` cycle detection and the derived execution-order section.** Grep only. Scenario: a child DAG with a cycle passes its gate because the rule is present but never exercised. **Impact: medium.**
7. **`TPL3`'s staged-propose-then-commit procedure.** Grep only (S-C7). Scenario: the runner stages a proposal and commits it at run end without the cold diff review, because the *removal* of the auto-commit sentence was checked and the *addition* of the procedure was not. **Impact: medium-high** (autonomous write to a shared repo).
8. **Multi-level verbatim escalation relay (D5).** X1 tests one level. The "may not paraphrase, summarize, or answer" duty at depth ≥ 2 is unobserved; RAT3 mechanically depends on it. **Impact: medium.**
9. **`SEAM`'s pending-reopen suspension** ("while a reopen is pending the parent does not re-dispatch running children", `2-plan.md:164-166`). X4 tests detection only. **Impact: low-medium.**
10. **The three new cold checks' own calibration (A-4).** **Impact: medium** — they are where satisfaction was moved off the runner.

---

# LABEL AUDIT

All criteria are marked **gating**; no criterion is marked advisory, so there is no advisory-dodge to challenge. The challenge that bites is CH9's second clause — *does the planned `verified = yes` exercise the path the criterion governs?* Per gating criterion, the governed path and the evidence I checked:

| Criterion | Governed path | Exercised by | Verdict |
|---|---|---|---|
| S-PRD | every schema key has a writing stage | `check.sh` parse of the canonical block + per-(key,stage) pair; behavioural half via X1's producer-gap row | **OK** — text pairs are the direct object; but see L-5 (the rule's own wording) |
| S-F1 | join / terminal producers / dead-vs-escalated | X1 holed+intact, per-item verdict table | **OK** — the strongest arm in the set |
| S-F2 | seam reopen + cross-node check | X4 (detection + contradiction) | **PARTIAL** — the pending-reopen sequencing duty unexercised (coverage 9) |
| S-F3 | stale record ⇒ un-run; approval re-binds | X2 both variants | **OK** |
| S-F4 | absent `redteam_context` ⇒ stop the run | X7(iii); plus a **column-0 YAML** assertion, not a substring hit | **OK** — the column-0 form genuinely defeats the F4 conflation |
| S-F5 | the approval is not forgeable | X3 (runner-authored; adjacent-answer variant) | **PROXY on the load-bearing step** — the fixture cannot make "independently fetch the locus" true or false, so X3 verifies whether a record *looks* admissible (D-3) |
| S-F6 | killed branch representable; abort has an author | X1 (kill-handled) ✓; **abort contract: grep only** | **PROXY on sub-part 4** — the sub-part the criterion itself calls the dissolve-any-gate guard |
| S-F7 | claim softened; diversity bought | grep (labels) + X6 (prompt-diff, sibling-read, self-report) | **UNVERIFIABLE for the labels' accuracy** (D-1, D-2) and **contradicted for the mechanism** (L-1, L-2) — treat as unverified |
| S-F9 | dispatcher-recorded id; degraded ≠ un-run | X6 both record sets, incl. the all-"unavailable" self-report set | **OK** — genuinely closes B/L-11 |
| S-F10 | "resolved" is not an unreviewed edit | X5 (untraced edit vs traced + rebind audit + demoted node) | **OK** |
| S-C1 | concurrency declared + surfaces partitioned | grep; the corrected `index.md` claim is text-as-behaviour ✓, but the **lock acquisition, the break protocol and the fencing discard are duties** with no arm | **MIXED / PROXY** on the duties (A-1, L-4) |
| S-C2 | one operand, one trip condition, honest label | X8 (40→36→33 vs 40→12→4) | **OK** |
| S-C3 | exit-plan-mode terminus | grep only | **PROXY**, and the asserted wording pre-shapes F8 (D-5) |
| S-C4 | ingest mapping/ABSENT/marked-authored | X7(ii) | **OK** |
| S-C5 | seed skeletons carry a Layer-2 slot heading | grep — **legitimately text-as-behaviour**: instantiation copies the skeleton text (verified: `generic-node.md:32-33` has only an italic note, no heading; `decomposition-node.md` has neither ⇒ B0.8's "3 of 3 fail" is right and pass 1's "2 of 3" was wrong) | **OK** |
| S-C6 | spot-verify duty performed | X7(i) | **OK on performance**; note the duty is assigned to stage 5 = the node's own drafting owner (`METHODOLOGY.md:167-177`), i.e. the party that benefits from clean reviews — worth a sentence acknowledging it |
| S-C7 | TPL3 no unreviewed shared-repo commit | grep only | **PROXY** on the added procedure (coverage 7) |
| S-C8 | inter-leaf dependency order | grep only | **PROXY** on cycle-detection + order derivation (coverage 6) |
| S-C9 | root pinned to `tree/root/` | grep — text-as-behaviour ✓ (a path string in prompts) | **OK**, but the required `decisions.md` declaration is absent (F1-3) |
| S-C10 | §4 heading canonical | grep with a **pinned extraction predicate** + distinct-normalized-count = 1 | **OK** — pass 1's undefined extractor is genuinely fixed |
| S-SC1 | validator + length + brackets | run, not assumed | **OK** |
| S-SC2 | cross-file rule consistency, 21+15 IDs | `ruleid-sitemap.sh` + `idcollide.sh`, each with a can-fail self-test against the pass-1 ID set | **OK** — the two pass-1 promises are now instruments |
| S-SC3 | block-before-table **and** intra-block order | line-offset + order assertion + two can-fail variants | **OK** — pass-1's 3/3 position major closed |
| S-SC4 | live == source, direction asserted | `diff -rq` before **and** after | **OK** |
| S-SC5 | the description still triggers | grep for vocabulary | **PROXY** (A-2) |
| R1 | site-set non-erosion | sitemap vs the **corrected** B0.6, and the reference table must itself pass baseline replay | **OK** — the defect that made pass-1 R1 `verified = no` is fixed |
| R2 | deliberate-change completeness | P-set now fixed authoritatively (11 items) + within-file absence | **OK** — pass-1's three-way disagreement resolved |
| X1-X8 | behavioural halves | separately-spawned holed+intact, both-same-verdict ⇒ `verified = no` | **OK as a protocol**; the "declared deferral" escape (L-3) is what undermines it |

**Named risk-acceptance:** correctly identified as unavailable under RAT3 (`1.5-criteria.md:415-417`) — but the substitute is invalid (L-3), so **any** criterion that cannot run has no legal disposition other than HALT + relay. Treat S-F5, S-F6(4), S-F7, S-C1, S-C3, S-C7, S-C8 and S-SC5 as **unverified** on the paths named above until an arm or a HALT covers them.

---

# RATIFICATION AUDIT

**No recorded "OWNER RULING" closes an escalated fidelity finding in these artifacts.** The owner text in play is (i) the verbatim directive at `LOOP-STATE.md:3-5`, (ii) the standing restart authorization at `:23-26`, and (iii) the owner-approved scope/decision record `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` (added to the closed set this pass — I read it in full). Audited as ratification artifacts:

1. **Directive → scope.** Verbatim: *"Alright, run it through guarded change to fix that, then have it run against its self again, repeat the loop three times or until nothing surfaces (whichever happens first)."* Axis: what "fix that" covers. `LOOP-STATE.md:12-15` labels the broad reading an "**Interpretation** … stated so Roy can correct it" — correctly a claim, not a ruling. Mapping: the directive selects *neither* the narrow nor broad reading; it is **partial on that axis**. Pass 2 handles this correctly by **carrying the hedge** rather than resolving it (`1-spec.md:188-191`) ✓ **CLOSED** — with the residue at F1-4 (the inflated label survives in `3-charter-given.md:206` and `decisions.md:41`).
2. **"until nothing surfaces" → the loop's terminate condition.** LOOP-STATE's narrowing to "no new blocker or major" is flagged by the orchestrator itself as non-binding and continue-only (`:56-63`); `1-spec.md:190-191` carries that ✓ **CLOSED**.
3. **"two passes aren't cost-justified".** An unaudited owner ruling with no re-ask path (`FINDINGS.md:157-159`); correctly **queued, not re-decided** (`LOOP-STATE.md:70-71`, `decisions.md:44-47`) ✓ **CLOSED**.
4. **RAT2 inflation — FOUND (major), D-4:** the owner-approved record fixes `topgate/` as "**the human** top-level-decomposition approval artifact" (`:171`; cf. `:92` "a **human** approves") . D9 elaborates this into "**any party other than the runner** … an orchestrator/intermediary acting as **transcriber**" (`2-plan.md:197-201`) — a division-of-responsibility commitment absent from and not entailed by the ratified phrase, generalized from this run's own delegated topology. Narrow it back, or re-ask.
5. **RAT2 inflation — FOUND (blocker-contributing), L-1:** the record ratifies (a) per-pass "**3 independent cold agents**" each carrying the full "what's missing here" mandate (`:65-70`), and (b) the Completeness lens's **earned-clean** requirement — "it must name the section-classes it checked and cite where each is covered" (`:84-88`). D13's per-frame *prohibitions* and reduced input sets are operative commitments contradicting (b) and narrowing (a). Frames as **aiming** are entailed; frames as **restriction** are not.
6. **Settled-decision departures.** One is declared (root → `tree/root/`, `0-baseline.md:189-194`, citation `:173` spot-verified ✓) — though not yet actually recorded in `decisions.md` (F1-3). A second is undeclared: the record's restart contract "**stage-done-iff-output-exists**" (`:129-130`) is amended by BIND to "exists **and** BIND-current" (`2-plan.md:144-145`, `1.5-criteria.md:106-108`). It is entailed by F3 and is the right change; it should be declared in the same place as the first (**minor**).
7. **`PRD`.** Not presented as owner-ratified, and its provenance is honestly stated (`1-spec.md:16-20`, `:119-121`). Not an unratified inflation of an owner ruling; its defect is D-6's wording.
8. **N=3.** `1.5-criteria.md:194` frames 3 as inherited-and-now-evidenced. The durable owner source (`:65`, `:68`) shows it is **owner-set**. Cite the owner source; keep the overlap data as supporting evidence for *frames*, not for the *number* (F1-5; and note `FINDINGS.md:24-27` — the reduced 1-agent pass producing 5 of 6 blockers — points the other way on the number).

---

# RANKED SUMMARY

| # | ID | Sev | Claim |
|---|---|---|---|
| 1 | **L-1** | **BLOCKER** | `DIV`'s per-frame prohibitions (S-F7.4, gating) make every completeness record un-run under `charter.md:80-87` / `stage-3:23-27` / owner-settled `:84-88` ⇒ no node can gate; and the 12-of-80 evidence measured *aiming*, not restriction |
| 2 | **L-2** | **BLOCKER** | DIV's declared-degraded 2-frame pass vs D2(a)'s literal "6 records" ⇒ the degraded node can never be subtree-complete ⇒ permanent join deadlock |
| 3 | **A-1** | major | the `dispatch_seq` fencing token accepts the orphan's write (equal, not lower, seq; parent cannot pre-stamp under single-writer) and is enforced by the party being fenced — move it to reader-side |
| 4 | **D-1** | major | `PRV`'s "mechanically checked … BIND-current to the text it reviewed" rests on a reviewer-attested, author-transcribed hash (carried item 5 only partly closed) |
| 5 | **D-3** | major | "independently fetch the cited locus" has no locus form, no access guarantee and no failure semantics; unfetchable ⇒ the audit reduces to the author's transcription (live F5) |
| 6 | **D-4** | major | the admissible-author set is empty in Architect's documented single-session topology, and the intermediary clause is a RAT2 inflation of "the **human** approval artifact" (`plans:171`) |
| 7 | **L-3** | major | "declared deferral" for an unverified gating criterion contradicts `Guarded_change/stage-8:42,47-48,62` and `METHODOLOGY:224-225`; the legal route is HALT + relay |
| 8 | **D-5** | major | `S-C3`/`XPM` makes the F8-"no" reading a *gating, verified* property at 4 sites while D12 deletes the only whole-assembled-plan reader — declared but simultaneously certified |
| 9 | **D-2** | major | `PRV`'s "no shared context and disjoint frames — evidenced by distinct ids and differing prompts": neither predicate follows; the oracle only rejects byte-identical prompts |
| 10 | **D-6** | major | `PRD`'s Layer-1 wording ("the plan must carry an assignment table as a required section") reads at 4 prompt sites as an 8th required plan section, contradicting the owner-settled 7-section spine |
| 11 | **A-2** | major | `S-SC5` verifies trigger *vocabulary presence* — a proxy on the path the criterion itself calls fatal ("all ten fixes ship dead"), over a rewritten first sentence of the trigger surface |
| 12 | **C-1** *(label)* | major | `S-F6.4` — the abort authorship contract, the criterion's own "dissolve-any-gate button" guard — is grep-only; no arm |
| 13 | **F1-1** | minor | S-F7's self-test constant: the overclaim is 8 occurrences across **4** files, not 5 ⇒ the S-family self-test cannot pass as written |
| 14 | **L-5** | minor | `PRD`'s "exactly one producer" is falsified by its own table (≥6 rows), and §1's "nothing reads a fact absent from this table" is falsified by the lock/`BROKEN-BY` facts and the `ABORTED-AUDIT.md` producer mismatch |
| 15 | **D-7** | minor | "fenced"/"cannot write" pins only to `off_limits_paths` prose (`METHODOLOGY:87`) — a prohibition on the constrained party, not a barrier; principle 1 is not delivered here |
| 16 | **F1-3** | minor | `0-baseline.md:191` and `S-C9` claim the settled-layout departure is "declared in `decisions.md`"; it appears there only as an open carried-forward duty |
| 17 | **L-6** | minor | frame C's "no config" input collides with `CTX`'s new "absence ⇒ un-run / stop the run" rule; needs an explicit carve-out |
| 18 | **A-3** | minor | position: GBP's "clean-or-resolved" is now two rules away from PASS1→PASS2 and its definition (`RES`) is outside the read-first block |
| 19 | **A-4** | minor | the three new cold checks (approval audit, abort audit, rebind check) are unreviewed checks under H6; no criterion observes their calibration |
| 20 | **L-4** | minor | the catalog lock has no blocked-path semantics; a losing run's TPL2/TPL3 proposal has no defined fate |
| 21 | **F1-4** | minor | the "approved cycle-1 scope" inflation survives at `3-charter-given.md:206` and `decisions.md:41` after LOOP-STATE told this pass to drop it |
| 22 | **F1-2** | minor | "`_status.md` 13×" is 11 (`1-spec.md:36,46`; B0.8's own list has 11 entries) |
| 23 | **D-8** | minor | "IMMUTABLE once written" is policy, not mechanism, and BIND's discriminator depends on it |
| 24 | **RAT-6** | minor | the BIND amendment to the settled "stage-done-iff-output-exists" restart contract (`plans:129-130`) is an undeclared settled-decision departure |
| 25 | **F1-5** | nitpick | "3 inherited from data-distiller" is contradicted by `plans:65,68` (owner-set); S-F7.7's "evidence, not inheritance" framing should cite the owner source |

**Confirmed closed from pass 1 (mechanism named):** B/L-1 terminal-status producers (D3's three named writers + X1's producer-gap row); B/L-2 escalation-vs-death (the precedence rule stated **first**, `2-plan.md:113`); B/L-3 SEAM (a sha256 equality test with **both** operands given producers in §1a); B/L-11 `spawn_id` (dispatcher-recorded + declared-degraded, X6's all-"unavailable" arm); C/L-1 RES(a)↔BIND (one rule, immutable record + rebind-record discriminator, `:142-143`); the 3/3 position major (S-SC3's intra-block order + updated rationale + can-fail variants — and note GBP **keeps** the block tail); the 3/3 baseline-site-map major (B0.6, word-boundary + phantom triage, `TPL1`/`TPL2`/`SEV` added, R1's reference table now itself replay-tested); the ID collisions (`KIL`→`KLB`, `ING`→`IGM`, promoted from promise to `idcollide.sh` with a can-fail test); BIND over the gate artifacts (D6, S-F3.5); `elc` "computable" (honestly relabelled); the schema's missing `template`/granularity keys (§1a rows); the closed-set omission of the approved-scope record (added, and read in full by this reviewer).

**Not closed:** the 3/3 DIV-collapse major (replaced by a mechanism that is worse — L-1/L-2, and note the tier-3 fallback `templates/seed/section-sets/` is authored by this change's own author for this purpose, so for cycle 1 it is the author's anticipation list one step removed; its decorrelation value is real only across *plan-types*, and the plan should say that rather than call it "genuine content"); the 2/3 PRV-positive-half major (D-1/D-2); the 3/3 risk-acceptance-unavailable minor (acknowledged, but the substitute route is illegal — L-3); and 8 of the 11 grep-only gating criteria remain proxies on the duty half.

**WORST SEVERITY: blocker**agentId: af13b7628d0aa4d37 (use SendMessage with to: 'af13b7628d0aa4d37', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 195958
tool_uses: 31
duration_ms: 991608</usage>