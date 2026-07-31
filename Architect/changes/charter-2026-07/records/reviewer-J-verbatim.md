# Reviewer J — stage-6b TARGETED RE-REVIEW of repairs R1-R5, VERBATIM

Recovered from the harness-authored subagent transcript, not re-typed:
`~/.claude/projects/.../subagents/agent-a94dc33cec6421c1a.jsonl` (final assistant message).

| field | value |
|---|---|
| `agentType` | `general-purpose` |
| `description` | `Targeted re-review J` |
| `model` | **`opus`** |
| `parentAgentId` | `a415bc52b9d9f3550` |
| `spawnDepth` | `2` |

---

I have everything I need. Here is my review.

---

## Context files read + sha256

| File | sha256 |
|---|---|
| `Architect/stages/charter.md` (artifact v2, 237 lines) | `1c8c1bd0620d041d5e3cfeda8a314aba4412de5d3dff5ba7d10f1aa763424112` |
| `Architect/changes/charter-2026-07/records/stage6b-prompt.md` | `72f8370ff389853e3b8a5776d455cfc593023c56ca3cd2fbe313b7cda31b5e95` |
| `Architect/changes/charter-2026-07/records/repaired-clauses.md` | `882ca630d553e391c00d7662d834164e6e46d79bf554c7c118999573adf7f4c0` |
| `/home/zero/Documents/Architect.md` (119 lines) | `1d3859546f3faf5a85e7ca7c4be4055c539b80eb86963c4743e481c350cee826` |
| `Guarded_change/stages/charter.md` (fork source, 103 lines) | `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590` |
| `Guarded_change/stages/stage-3.md` | `16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3` |
| `Guarded_change/stages/stage-4.md` | `175061c27bb6980ff76c6358d403299d343c409b2952308ffea7485fff880675` |
| `Architect/changes/charter-2026-07/1.5-criteria.md` | `1df324c0d4d3c971c9a3a56232ebf872c757bfb22d35cc26808ded359918912c` |
| `Architect/changes/charter-2026-07/0-baseline.md` | `4872f951c65351d5180f019ca7298ff5ae2c41cd6d43e9d0a9241e10c2e49b4a` |
| `Architect/changes/charter-2026-07/decisions.md` | `f91075e837cffb3dd94e2730d7aa62ec9085cf1d4a8cfab70688079db7dfd40a` |
| session transcript `45cb99a2-…-0775.jsonl` | not hashed — read by record index (1449) only; hashing a live append-only file gives a value that is stale on read |

**Used outside the declared list, disclosed per instruction:** `records/build-diff.txt` (to reconstruct charter **v1**, sha256 `523bf3a24b9a1279790473ffb5d5904a74424d9cacf2800f2f657baffc446085`, 215 lines, by applying it to `git show HEAD:Architect/stages/charter.md`). The ride-along check is not performable without a v1↔v2 delta and none was supplied. I derived it rather than trusting `repaired-clauses.md`.

**Banner check:** no `UNVETTED DRAFT` banner. Head block is the provenance blockquote (C-16a satisfied). Artifact sha256 matches the prompt exactly.

---

## Repair-by-repair verdict

### R1 — closed set — **CLOSED** (with a minor residue)

The blocker is genuinely dead. `Divisible` is 2-arg (`Architect.md` L14), called at L62/L87/L111 with `(task, granularity)` — no plan at any site. Charter L126–128 now states the split review's set without a plan and adds the explicit negative: *"**It is given no plan** — `Divisible` is not passed one."* `Spawn_redteam` L28 is 3-arg and L124–125 matches it. C-11's negative requirement ("must **not** assert the parent's plan as an input to `Divisible`", 1.5-criteria.md L53) is satisfied and now over-satisfied.

The 3/3 unbounded-set major is also closed. L129–130 bounds the extension from outside the author: *"a list fixed by the configuration, **not by the author of the artifact under review**"*, and L132–134 states why. "Supplementary author-authored context must be quoted as such" now has a non-empty extension and can bite.

Residue → **finding 5**: the bullet's bounding principle is *"closed by your caller's signature"* (L123), but the split review's third item — the proposed division + seam — is **not** in `Divisible`'s signature. `Divisible(_task, _granularity)` computes the division internally (L14: "if yes, red-teams result"). The enumeration is right; the stated principle does not actually generate it.

### R2 — `Union` / spot-verify — **CLOSED as filed, but it breaks a frozen gating criterion**

The severity override is gone. v1: *"marked UNSUBSTANTIATED **and does not pass forward as blocker|major**"*. v2 (L108–109): *"marked UNSUBSTANTIATED, and the mark travels with the finding."* That is correct against `Architect.md` L24 (`Union` = merge + dedup, discards nothing) and L26 (`Severity()` is the filter). The H-F4 sample-vs-universal limits at L113–116 are real and well-aimed.

I verified the ratification myself. Transcript record 1449 is `origin.kind: "human"` — admissible. Item 3 verbatim: *"That **was** part of what Combine did, but you said nothing could get discarded, make up your mind."* That ratifies **placement** and, if anything, cuts **against** any disposition that looks like discarding. So the author dropped the right thing.

**But** frozen gating criterion **C-12** (`1.5-criteria.md` L54) requires, by "Positive assertion **per clause**", that *"a finding whose citation does not resolve is **marked unsubstantiated and does not pass to `Severity` as blocker|major**"*. v1 satisfied that clause verbatim; **v2 no longer does**. Nothing in `decisions.md` amends C-12, records the conflict, or routes it through the post-freeze (FRZ) path — the very path the same document invokes two paragraphs later for G-F1 (*"a post-freeze edit (FRZ), which needs a `decisions.md` entry **and** a targeted re-red-team of the edited criterion — it is not something to slip in"*). The artifact and its frozen oracle now contradict each other on a gating clause, silently. → **finding 2**.

Secondary: C-12b's carve-out (charter L109–111) now guards nothing. Its stated purpose (`1.5-criteria.md` L55) was to resolve a real C-08/C-12 conflict created by `Union` dropping findings. With the drop gone there is no conflict, and *"Only the second requires the owner"* (L111) is left implying that **marking** is a disposition the marker may take unilaterally — a faint re-entry for the power R2 just removed. → **finding 8**.

### R3 — earned-clean fidelity gate — **CLOSED**

Carried rule B13 (`0-baseline.md` L95, **CARRY**; fork source L47–58) requires the clean verdict to show the ratification audit **and** that "any elaboration's operative terms are traced to the ratified text". v1 named only the RAT1 audit. v2 L95–98 requires *"**both** the **RAT1 audit** (options + verbatim words + durable source + mapping) **and** the **RAT2 elaboration-trace**"*. The regression against B13 is repaired. "Mapping … on the flagged axis" is not lost — it is carried in-file at L146, and C-22 holds (no `stages/stage-*.md` pointer anywhere in the charter; grep returns nothing). Clean.

### R4 — RAT1 durable source — **NOT CLOSED. Moved, and into a worse position.**

This is the serious one.

The prompt's own priority order says `Architect.md` is **THE AUTHORITATIVE DESIGN SPEC** and "if the charter disagrees with this file, this file wins and the disagreement is a finding." `Architect.md` **L19** states, owner-authored:

> "for the owner's actual words the only admissible source stays the harness-authored session transcript."

v1's clause — *"The session transcript is the only admissible source for the owner's words. An agent-written file — including a resume note or a prior artifact — is not."* — **matched that sentence exactly.** I-F3 checked the "narrowing" only against `stage-3.md` L59–60 (priority 3) and concluded it was undeclared. Checked against priority 1, it was not a narrowing at all; it was fidelity.

The repair reversed it. Charter L155–156 now admits *"a **timestamped, owner-attributed entry in the run's decision log**"* as a durable source for the owner's verbatim response. A decision-log entry is agent-written. So the repaired charter:

- **contradicts `Architect.md` L19**, and
- **contradicts itself**, ten lines apart: L165–166 still says *"For the owner's actual words the transcript remains the only admissible source."*

L157–158's *"where the two conflict the harness-authored transcript wins"* does not rescue it — that is a tie-break, not an admissibility rule. It leaves a log entry admissible *on its own*, with no transcript to conflict with, which is precisely the uncontested case.

The consequence is not cosmetic. `Architect.md` L19 exists because *"attempt 1 shipped exactly that forgery and nobody looked."* RAT1's job is to stop a self-certified ratification. R4 restores an agent-writable source as sufficient proof of the owner's verbatim words — reopening the hole the instrument was built to close. → **finding 1 (blocker)**.

Note that I-F3's remedy did not require this. Its complaint was that the narrowing was **undeclared**. Declaring it in the provenance blockquote (which C-03b already requires for CHANGE-intent rules, `1.5-criteria.md` L43) would have closed the finding *and* preserved spec fidelity. See Lens 3.

### R5 — demotion rule — **MOVED, not closed. Two defects.**

**(a) The named destination does not exist.** The original finding was that "a logged entry" named no log, because `Architect.md` defines none. It still defines none: `grep -ni "log\|journal\|decisions"` over all 119 lines returns **nothing**, and `Memo_write` L37 persists `{done, iter, task, plan, division}` — no log field. The repair names *"the run's decision log"* (L209) and then adds *"contesting with no logged destination is not contesting."* Given that the destination is undefined, that closing clause converts the contest path from underspecified into **provably unreachable**: no contest can ever be validly logged, so the `Ask_human` tie-break at L211–212 is unreachable through the sanctioned route. The symptom (no name) was fixed; the cause (no such artifact) was not. → **finding 3**.

This also introduces exactly the defect class C-22 was written to close — a referent the charter names that Architect does not contain — one level up from stage-file pointers. The charter's own recurrence rule (L215–218) says that means the earlier fix was applied too narrowly.

**(b) An unratified inflation, in the clause a repair was supposed to de-inflate.** `stage-4.md` L34 reads: *"The author may contest a severity only via a logged `decisions.md` entry."* C-08 (`1.5-criteria.md` L49) is titled **"Demotion rule, ported verbatim"** and is verified "checked against source text at `stage-4.md` L34–36". The repair adds *"**against the node whose plan is under review**"* — a division-of-responsibility commitment present in neither the source text, nor C-08, nor the owner's ruling. Owner record 1449 **item 2**, verbatim: *"It gets implemented however it is implemented in guarded-change; that is what the instruction was: copy over the severity mechanism from guarded change."* Node-scoping is not present in or entailed by that phrase. By the charter's own **RAT2** (L168–175), that ranks ≥ major. R2 removed one unratified inflation; R5 added another, in the adjacent section. → **finding 4**.

Also relevant to how much weight the RAT sections can bear: record 1449 **item 4** is *"I don't know what the fuck rat1/2 even ARE."* Nothing in RAT1/RAT2 is owner-ratified content; it is all port fidelity, which makes divergence from `stage-3.md`/`stage-4.md` and from `Architect.md` the only available checks — and R4/R5 fail one each.

---

## Ride-along check

**My charter's premise is wrong: seven passages changed, not five.** The v1↔v2 delta contains two changes outside the five-repair table I was given:

1. **Provenance blockquote, L14–17** — a new sentence: *"**B19**'s composition rule is re-aimed from guarded-change's stage-specific additions to Architect's per-caller aiming,"* plus "(B15)" tagging. Not called for by R1–R5.
2. **`origin.kind`, L160–161** — enumeration widened from two values to four (`"human"`, `"task-notification"` added). Not called for by R4 as described to me ("both sources restored; narrative excluded; transcript wins").

Both **are** recorded in `decisions.md` L586–587 as repairs to findings G-F5/H-F5 and G-F9. So they are declared in the run record — they are not undeclared edits — but they were **not disclosed to me**, and by the same rule this pass exists to enforce ("an unreviewed check is not a check"), they have had no cold look in repaired form either. Whoever consumes this pass should not read my sign-off as covering them.

Assessing them anyway:

- **B19 sentence:** correct. `0-baseline.md` L154 lists B19 as **CARRY**, which reads like a mismatch with declaring it under **CHANGED** — but frozen criterion C-03b (`1.5-criteria.md` L43) explicitly enumerates "B19 restated per-caller" among the CHANGE-intent rules whose difference must be declared in the blockquote. The blockquote listing B15/B19 under *both* CARRIED and CHANGED is required by C-01 + C-03b together, not a contradiction. **No finding.**
- **`origin.kind` four values:** I checked this against the transcript directly. Counting `origin.kind` across all records yields `{human: 50, task-notification: 24, peer: 3}`. Three of the four are measured. `"coordinator"` does not appear — expected, since this is the top-level session and has no orchestrator above it — and it is attested by `Architect.md` L19. Widening a two-value enumeration to a measured four-value one is a superset, not a contradiction of L19. **No finding**, but see Unverifiable.

Nothing else moved. I confirmed mechanically that B18 still holds the terminal line (L237, `0-baseline.md` L155: "CARRY, **and CARRY ITS POSITION**") and the granularity floor (L30) still precedes the lenses (L47).

---

## Lens 1 — Factual

Not clean. Findings **1**, **3**, **4** are factual: L155–156 contradicts `Architect.md` L19; L156 and L209 name a "run's decision log" that `Architect.md` defines nowhere; L209's node-scoping is absent from `stage-4.md` L34.

Source evidence consulted for the parts that **do** check out: `Architect.md` L14 (`Divisible` 2-arg) and its call sites L62/L87/L111; L28 (`Spawn_redteam` 3-arg); L24 (`Union` merge+dedup, "DISCARDS NOTHING"); L26 (`Severity` filter); L18 (`Ask_human` blocks from any depth); L37 (`Memo_write` field list); L104–110 (three red-team agents; `task = Severity(Union(...))`). Fork source L47–58 (B13), L74–77 (B15), L103 (B18 terminal). `stage-3.md` L55–72, L89–119. `stage-4.md` L26–36. Transcript record 1449 (`origin.kind: "human"`), items 2 and 3.

## Lens 2 — Logical

**The self-contradiction at L155–156 vs L165–166** is the primary logical defect — a reviewer holding this charter cannot determine whether a decision-log-sourced owner quote is admissible, and the two statements are close enough that both will be read. Covered in finding 1.

**L209's dead end** (finding 3): "contested **only** via an entry logged in the run's decision log" + "contesting with no logged destination is not contesting" + no such log ⇒ the universally-quantified "only" has an empty satisfying set. Structurally identical to the empty-extension defect R1 was repairing in the closed set.

**C-12b residue** (finding 8): a carve-out whose motivating conflict no longer exists.

Checked and **not** a finding: I considered whether *"receives **exactly**: the task, the plan, and the granularity floor"* (L124) is falsified by the reviewer also holding the charter core and the caller's aiming. It is not — L135–137 (composition) and L132 (quote-as-such) prescribe the same handling for the aiming, so the two rules agree rather than conflict.

## Lens 3 — Missed opportunity

**R4 had a cheaper, spec-faithful remedy that was passed over.** I-F3's complaint was an **undeclared** narrowing. C-03b already requires every CHANGE-intent difference to be declared in the provenance blockquote. Adding one line — "RAT1's durable source is narrowed to the transcript alone, per `Architect.md` L19" — would have closed I-F3 exactly as filed, kept fidelity to the authoritative spec, and avoided the blocker at finding 1. The author chose reversal over declaration and inverted a correct clause.

**R5 had the honest option available and did not take it.** "Architect defines no decision log, and the demotion rule cannot be ported faithfully until one exists" is itself a finding, and `decisions.md` L594–617 shows the author is entirely willing to carry findings forward honestly (G-F1, H-F6, H-F7). Inventing a destination was the one option that produces an unauditable rule while looking repaired. `Ask_human` (L18) and `Memo_write` (L37) are the only durable primitives Architect actually has; a rule built on those would be executable today.

## Lens 4 — Unstated assumptions & risks

- **Assumed: a "run's decision log" exists or will be supplied by Layer-2.** Stated nowhere. Two operative rules (L156, L209) depend on it.
- **Assumed: a decision-log entry can be "owner-attributed" un-forgeably.** This is the assumption `Architect.md` L19 exists to reject. Load-bearing and false in the threat model the spec was written against.
- **Assumed: `Union` can read the filesystem.** L104–105 puts the entire citation spot-verify on `Union`, but `Architect.md` L24 specifies only "merges issues … dedups only exact restatements". If `Union` is dispatched without source access, the guard the charter calls "the one guard defending the founding failure" is silently inert. Pre-existing in v1, not repair-introduced — but in scope. → **finding 7**.

**Position/order sensitivity — trigger fires, tested.** R1 restructured a flowing bullet into paragraph + nested list + bolded closing paragraph; R2 extended the spot-verify bullet's tail by four lines. Elements that did not change were tested:

- **B18 tail recency preserved** — L237 is still the document's final line, per the declared intent at `0-baseline.md` L155 and D9. No displacement.
- **Floor before lenses preserved** — L30 vs L47.
- **R1's restructure is a net improvement in position terms:** the quote-supplementary-context obligation moved from mid-sentence to a bolded terminal paragraph of its own bullet (L132–134), gaining end-of-block recency. R2's added limits likewise land at the bullet's end (L113–116), so the "do not overtrust this guard" framing is what a reader carries out of the bullet.
- **One position defect surfaces, and it predates the repairs.** C-12 (`1.5-criteria.md` L54) requires the `Union` clause be *"stated **adjacent** to the carried 'flag the unverifiable' bullet so the two read as one discipline."* "Flag the unverifiable" is at L85–86; the spot-verify bullet is at L104–116, with three bullets (earned-clean factual, fidelity, Completeness) between them. Not adjacent. R2's lengthening does not increase the gap, so this is not repair-introduced — but a frozen gating clause about *placement* is unmet, and unchanged elements are explicitly in scope for this lens. → **finding 6**.

## Lens 5 — Fidelity

Not clean. Terms pinned to their concrete mechanisms:

| Loaded term | Pinned mechanism (owner intent) | Charter implements it? |
|---|---|---|
| "closed set" | bounded by callee signature: `Spawn_redteam` L28 (3-arg), `Divisible` L14 (2-arg) | Yes, enumeration correct (L124–130). Stated principle over-claims — finding 5 |
| "the merge step (`Union`)" | `Architect.md` L24 cold agent: merge + dedup, discards nothing | Yes, after R2 removed the override |
| "human tie-break" | `Ask_human` L18 — blocks for the owner from any depth | Yes, named explicitly at L211–212 |
| "granularity floor" | L1–8: set per run, threaded down, branch-overridable | Yes — L32–34 mirrors the override provision |
| "3 independent cold agents" | L104–107: three separate `Spawn_redteam` calls | Yes — L234–236 |
| "severity" | L26 `Severity()` filters blocker\|major → becomes next task (L110) | Yes — L192–196 |
| **"durable source"** | **`Architect.md` L19: the harness-authored session transcript, *the only* admissible source for the owner's words** | **No — a proxy substituted (agent-written log entry), L155–156. Finding 1** |
| **"the run's decision log"** | **no mechanism exists in `Architect.md`** | **No — unpinnable referent. Findings 3, 4** |

Two of eight loaded terms fail to pin. Both failures were introduced by the repairs; both terms were absent or correctly pinned in v1.

---

## Regression check — did any repair weaken a carried rule (B01–B19)?

| Rule | Intent (`0-baseline.md`) | Verdict |
|---|---|---|
| **B13** (earned-clean fidelity) | CARRY (L95) | **Repaired.** R3 restored the elaboration-trace v1 dropped. Net improvement. |
| **B15** (provenance + closed set) | CARRY with one declared DROP (L149) | **Strengthened.** R1 bounds the set from outside the author; the DROP is still declared in the blockquote (C-03 holds). |
| **B16** (position lens) | CARRY (L98) | Intact, L179–185. |
| **B18** (graded on precision) | CARRY **and carry its position** (L155) | Intact and still terminal at L237. |
| **B19** (composition) | CARRY, restated per-caller (L154) | Intact, L135–137, and now declared in the blockquote per C-03b. |
| **B14** (spot-verify, named consumer) | CARRY + name the consumer (L148) | Consumer still named (`Union`, L104). Substance changed by R2 — correct against `Architect.md` L24/L26 and owner record 1449 item 3, but it drops a clause frozen into C-12. See finding 2. |

**One regression, and it is against the authoritative spec rather than against B01–B19:** R4 reversed a clause that was faithful to `Architect.md` L19. The baseline inventory has no rule covering it because it is an Architect-specific fidelity point, not a carried fork rule — which is likely why the regression passed unnoticed.

## Unverifiable claims I could not check

1. **`origin.kind == "coordinator"`** (L160). Not present in this transcript — expected, as this is the top-level session with no orchestrator above it. Attested only by `Architect.md` L19. Consistent with the author's own disclosure (`decisions.md` L596–602) that the whole `origin.kind` block ships with no criterion coverage.
2. **Whether a "run's decision log" is defined in an Architect Layer-2 config.** No such config was in my context set. I can state only that the authoritative design spec defines none, which is the check the prompt directs me to make.
3. **Whether C-12 was amended anywhere outside `decisions.md` and `1.5-criteria.md`.** I checked both; neither records an amendment. A record elsewhere in the run folder would change finding 2's severity, not its substance.
4. **`Union`'s actual tool grant at dispatch.** Not specified in `Architect.md`; finding 7 is raised as an unstated assumption, not a confirmed defect.

---

## Findings table

| # | severity | lens | file:line | finding | why it matters |
|---|---|---|---|---|---|
| 1 | **blocker** | Factual / Fidelity | `Architect/stages/charter.md` L155–156 (vs L165–166; `Architect.md` L19) | R4 admits "a timestamped, owner-attributed entry in the run's decision log" as a durable source for the owner's verbatim words. `Architect.md` L19 says the harness-authored transcript is **the only** admissible source for the owner's actual words, and the charter itself repeats that at L165–166. v1 matched the spec; the repair reversed it. | Restores an **agent-writable** source as sufficient proof of owner ratification — the exact forgery `Architect.md` L19 was written against ("attempt 1 shipped exactly that forgery and nobody looked"). RAT1's purpose is defeated, and the charter is self-contradictory ten lines apart, so it cannot be executed as written. |
| 2 | **blocker** | Logical | `Architect/stages/charter.md` L108–109 vs `1.5-criteria.md` L54 | R2 removed "does not pass forward as blocker\|major". Frozen gating criterion **C-12** requires that clause by "positive assertion **per clause**". No `decisions.md` entry amends C-12 or records the divergence. | The artifact now contradicts its own frozen accept bar on a gating clause. Gate 7 cannot close clean, and the only ways out are to fail at stage 8 or to quietly edit a frozen criterion to match the artifact — the self-certification failure this loop exists to prevent. `decisions.md` L596–602 names the correct FRZ path for exactly this and did not use it here. (The repair's *direction* is right: `Architect.md` L24/L26 and owner record 1449 item 3 support it. The defect is that the oracle was left contradicting it.) |
| 3 | **major** | Factual / Logical | `Architect/stages/charter.md` L209 (and L156); `Architect.md` L37 | R5 replaced "a logged entry" with "the run's decision log". `Architect.md` defines no log anywhere (`grep -ni "log\|journal\|decisions"` over all 119 lines returns nothing; `Memo_write` L37 stores `{done, iter, task, plan, division}`). Adding "contesting with no logged destination is not contesting" closes the loop on an empty set. | The original finding was "the sanctioned contest path has no destination". Naming a destination that does not exist does not close that — it makes the path **provably unreachable**, so no severity can ever be validly contested and the `Ask_human` tie-break (L211–212) is cut off. A moved defect at the original severity. |
| 4 | **major** | Fidelity | `Architect/stages/charter.md` L209; `stage-4.md` L34; `1.5-criteria.md` L49 | R5 added "against the node whose plan is under review" — a division-of-responsibility commitment absent from `stage-4.md` L34, from C-08 ("Demotion rule, **ported verbatim**"), and from owner record 1449 item 2 ("implemented however it is implemented in guarded-change"). | An unratified inflation by the charter's **own RAT2** (L168–175, ranks ≥ major) — the same defect class R2 was repairing one section away. Per the charter's own recurrence rule (L215–218), that means the fix for the inflation class was applied too narrowly, and the remedy is to sweep the class rather than patch this site. |
| 5 | minor | Logical | `Architect/stages/charter.md` L123 vs L126–128; `Architect.md` L14 | The closed set's bounding principle is "closed by your caller's signature", but the split review's third item (proposed division + seam) is not in `Divisible(_task, _granularity)`'s signature — it is computed inside `Divisible` (L14). | The enumeration is correct; the stated principle does not generate it, so a reviewer reasoning from the principle rather than the list gets a different set. Weakens the rhetorical force of an otherwise well-repaired clause. |
| 6 | minor | Factual | `Architect/stages/charter.md` L85–86 vs L104; `1.5-criteria.md` L54 | C-12 requires the `Union` clause be "stated **adjacent** to the carried 'flag the unverifiable' bullet so the two read as one discipline". Three bullets (L89–103) separate them. | A frozen gating clause about placement is unmet. **Pre-existing in v1, not repair-introduced** — raised because the position lens puts unchanged elements in scope and because it compounds finding 2's C-12 exposure. |
| 7 | minor | Unstated assumptions | `Architect/stages/charter.md` L104–105; `Architect.md` L24 | The entire citation spot-verify is assigned to `Union`, whose spec grants only "merges issues … dedups only exact restatements" — no source access is stated anywhere. | If `Union` is dispatched without filesystem access, the guard the charter calls "the one guard defending the founding failure" is silently inert while every record looks clean. Placement is owner-ratified (1449 item 3); the **capability** is assumed. Pre-existing in v1. |
| 8 | minor | Logical | `Architect/stages/charter.md` L109–111; `1.5-criteria.md` L55 | With the drop removed, C-12b's carve-out guards nothing — the C-08/C-12 conflict it was written to resolve no longer exists — and "Only the second requires the owner" now reads as implying marking is a unilateral disposition. | Dead limb that faintly re-licenses the power R2 removed. Cheap to fix by rewording the carve-out to state that marking has no dispositional effect at all. |

## Worst severity

**blocker** — two of them, independent of each other.

Finding 1 (R4) is the one I would not let past under any reading: the repair inverted a clause that was correct against the authoritative design spec, left the artifact self-contradictory, and reopened the forgery hole RAT1 exists to close. I-F3 was checked against `stage-3.md` (priority 3) without reconciling against `Architect.md` L19 (priority 1), and the repair inherited that error. **R4 should be reverted to the v1 text and the narrowing declared in the provenance blockquote** — that closes I-F3 as filed at a fraction of the cost.

Finding 2 (R2) is procedural but gating: the substantive change is correct and owner-supported, and it still cannot ship while frozen criterion C-12 says the opposite with no recorded amendment.

Of the five repairs I was asked to gate: **R1 and R3 close cleanly. R2 closes its finding but breaks the accept bar. R4 and R5 move their defects rather than closing them.** Two of the five introduce the same defect class — a named referent (`the run's decision log`) that the authoritative spec does not contain — which suggests one sweep rather than two patches.