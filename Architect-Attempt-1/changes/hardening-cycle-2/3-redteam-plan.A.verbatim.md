# Stage 3 — cold review record, ARM A (VERBATIM)

**This file is a verbatim record** (ART2). The reviewer's raw output is reproduced below unedited,
extracted mechanically from the dispatcher's task transcript. The author's interpretation lives in
`decisions.md`; the ranked cross-arm synthesis lives in `3-redteam-plan.md`; the charter given, the exact
context list, and the closed set live in `3-charter-given.md`.

| Field | Value |
|---|---|
| Arm / frame | **A** — closure audit + fidelity/scope honesty (CH11/CH12) |
| Agent type | `general-purpose` (cold subagent, no shared context with the author, none with the other arms) |
| Model | `claude-opus-5` |
| **`spawn_id` (DISPATCHER-RECORDED, not self-reported)** | **`aea2863bc75a6d6a5`** |
| Self-reported identity | `unavailable` (the reviewer correctly declined to invent one; corroboration only) |
| Context-file sha256s | reported by the reviewer in its own `## Provenance` section below, and captured independently at dispatch in `context-hashes.txt` |
| Charter given | the guarded-change charter core verbatim (five lenses + all unconditional discipline bullets + **both** conditional lenses, stated as firing) + the stage-3 additions listed in `3-charter-given.md` |

---

# COLD REVIEW — FRAME A: CLOSURE AUDIT + FIDELITY/SCOPE HONESTY
### hardening-cycle-2 · {0-baseline, 1-spec, 1.5-criteria, 2-plan, oracles}

---

## Findings

**A/F1 · MAJOR · A confirmed-closed position fix is ported with its load-bearing half deleted: the rule block's closing rationale is left a stale three-item list.**

Cycle 1's position major was confirmed closed by two reviewers with its mechanism named — `hardening-cycle-1/decisions.md:207`: *"the position major (intra-block order **+ updated rationale** + can-fail variants)"*. That mechanism was two-part and both parts are written down:
- `hardening-cycle-1/1.5-criteria.md:354-357`: *"S-SC3 — Position: block-before-table **AND intra-block order** … and the block's closing rationale sentence **enumerates what the block now contains** (no longer a stale three-item list)."*
- `hardening-cycle-1/2-plan.md:388`: *"`PRV`/`DIV` placed **before** GBP; **the closing rationale updated**; `S-SC3` gains an **intra-block order** assertion"*.

Cycle 2 ports **only the intra-block-order half**. `hardening-cycle-2/1.5-criteria.md:311-320` (SC3) requires the block precede the stage table, the intra-block order be asserted, and X2 prove GBP still fires. The rationale-enumeration requirement is **absent**. `2-plan.md:445` restates the same reduced set. Meanwhile `2-plan.md:292-301` (D16) adds HG2 to `SKILL.md`'s rule block and `2-plan.md:445` confirms *"HG2 is added **after** the three existing rules"*.

The target text is `Architect/SKILL.md:39-41`: *"(The completeness lens, the two-pass discipline, and gate-before-present are stated here, up front, because these files are prompts — a position-sensitive assembly — and this rule block is load-bearing before the stage table, not after it.)"*

**Failure scenario.** After the build, `SKILL.md`'s rule block contains four rules (CMP, PASS1/PASS2, GBP, HG2) and closes with a parenthetical enumerating three — the exact defect cycle 1's confirmed-closed fix eliminated, re-created by cycle 2's own edit. No criterion catches it: it is not a `CHANGE` row in `0-baseline.md` B4, so **R2** does not observe it; lines 39-41 carry no ID token (GBP appears as prose, the token is at `SKILL.md:33`), so **R1**'s site map is unaffected; **SC3** as written asserts only order and membership. This is also the position lens's textbook "added block displaces the old last element" case — GBP stops being last and its justifying sentence stops covering the block.

*Fix:* restore cycle 1's clause to SC3 — the closing rationale must enumerate what the block now contains — and add it to D16's site list for `SKILL.md`.

---

**A/F2 · MAJOR · R1's baseline site map is not what its cited oracle produces: `ruleid-sitemap.sh` and `idcollide.sh` both derive their ID set from the very index table whose incompleteness is a finding, so the gating regression check silently under-scopes by 3 of 21 IDs.**

`0-baseline.md:29-30` claims B2 was *"Captured by `changes/hardening-cycle-2/oracles/ruleid-sitemap.sh .` at `b08f5a9`"*, and B2's table lists **21** rows including `TPL1`, `TPL2`, `SEV` (`0-baseline.md:50,51,55`), with `0-baseline.md:57-58` stating those three are *"live IDs with **no index row**."*

Run as cited, the oracle emits **18** IDs — `CAP CMP CMP2 COV DEC ECON GBP GRN ORC PASS1 PASS2 PASS-ORD RAT3 RST SPN TOP TPL TPL3`. `TPL1`, `TPL2`, `SEV` are absent. The cause is at `oracles/ruleid-sitemap.sh:17` (and identically `oracles/idcollide.sh:25`):

```
mapfile -t IDS < <(grep -oE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md | ...)
```

The default ID set **is** "IDs with an index row." Passing them explicitly works (`ruleid-sitemap.sh . SEV TPL1 TPL2` returns `SEV → stages 4,5`; `TPL1 → METHODOLOGY, stages 1,2, seed/README`; `TPL2 → METHODOLOGY, stages 1,6, seed/README`), so the instrument is capable — its *default scope*, which is what B2 cites and what the criteria specify, is not.

**Consequences, both concrete.** (a) B2's provenance claim is false for 3 of 21 rows — they cannot have come from the cited command; this is the same class of defect cycle 2 is correcting in cycle 1 at `0-baseline.md:79-81` (B0.7's false "baseline passes idcollide"). (b) **R1 is gating** and specified at `1.5-criteria.md:277-283` as *"Every baseline ID in `0-baseline.md` **B2** retains at least its baseline site set, computed by `oracles/ruleid-sitemap.sh`"* — as shipped it cannot compute 3 of those 21, so site erosion for `TPL1`/`TPL2`/`SEV` is undetectable. Worse post-change: D17 adds index rows for exactly those three plus 12 new IDs, so the stage-8 re-run's default set becomes ~33 while the baseline capture was 18-plus-3-by-hand — the criterion compares two differently-scoped sets. (c) **R3** inherits the identical defect: `idcollide.sh` cannot collision-check a live-but-unindexed ID, which is precisely the class `SEV` was in at baseline.

This lands on frame-A mandate 1(a): cycle 1's confirmed-closed item #7 was *"the baseline site map must be recaptured … **R1 as written fails its own baseline replay**"* (`hardening-cycle-1/decisions.md:106-109`, 3/3 major), and `0-baseline.md:65-69` claims cycle 2 *"re-verified it mechanically rather than inheriting the claim."* For 3 rows it did not.

*Fix:* derive the ID set from the corpus (or from an explicit list in the criteria), not from `METHODOLOGY.md`'s index table; re-capture B2 with the corrected default and record the command's actual output.

---

**A/F3 · MAJOR · CNC ships a fix whose enabling half is deferred: removing `index.md`'s writers strands the `template used` duty with no destination, because the `_status.md` schema that was to receive it is deferred F1 work.**

`2-plan.md:195` (D8) removes all four baseline `index.md` writers and asserts *"**DERIVED, never authoritative** — written **only** by the top orchestrator, by walking the tree. **Per-node facts live in that node's own `_status.md`.**"*

But `template used` has no `_status.md` home, and cycle 2 does not give it one. Baseline, verified: `stages/stage-1-frame-template-match.md:20` — *"record `template: <name>` in `index.md`"*; `METHODOLOGY.md:195` — *"record the template used in `index.md`"*; `templates/seed/README.md:14` — *"record `template: <name>` in `index.md`."* Those are the only three sites, and they are exactly the three D8 strips. `<node>/_status.md` is defined at `METHODOLOGY.md:268` as *"terse done-state + one-line roll-up + gate state"* — no `template`, no granularity call. The approved record fixes `index.md`'s content at `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:165`: *"plan tree + per-node {template used, status, gate state, leaf?/decompose?}"*.

The missing piece is a **confirmed-closed cycle-1 fix that cycle 2 defers**: carry-forward #12 (`hardening-cycle-1/decisions.md:123-124`) — *"The `_status.md` schema omits `template` and the granularity call although derived `index.md` is documented to carry both"* (2/3 major), closed in pass 2 as *"the schema's missing keys"* (`decisions.md:209`). Cycle 2's `1-spec.md:172` puts *"the `_status.md` schema"* inside deferred F1.

**Failure scenario.** Post-cycle-2, stage 1 matches a skeleton and has nowhere to record it (its only recorded destination was removed); the top orchestrator then walks the tree to derive `index.md` and cannot fill two of its four documented columns. TPL1's match/instantiate audit trail is lost, and stage-8 restart cannot tell whether a node was template-instantiated. `2-plan.md`'s §1 operand table does not list `template` at all, so the plan's own anti-cap discipline never examined it.

No criterion observes this. S-CNC (`1.5-criteria.md:145-171`) asserts `index.md` is *derived* at every former accessor site — i.e. it asserts the **removal** and nothing about the destination. R1 passes because TPL1's *ID sites* survive even if the write duty's target vanishes.

*Fix:* either name `<node>/_status.md` as the destination for `template` + the granularity call (a two-key addition, not the deferred schema rework) or narrow D8 to leave `index.md`'s stage-1 write in place this cycle and declare the residual.

---

**A/F4 · MAJOR · PRV is admitted to scope on a justification that is factually false — it is not "strictly subtractive" — and the specific positive claim it adds is the never-closed cycle-1 overclaim.**

`1-spec.md:113-118` admits PRV and OFL past R1's ratified boundary on this stated ground: *"they are in scope by orchestrator direction, and the justification is that they are **strictly subtractive** — they delete a claim the artifact cannot support and **add no mechanism**, so they cannot exceed the ratified blast radius."*

D6 is not subtractive. `2-plan.md:158-163` adds two new affirmative propositions: *"Gate-before-present establishes, **on the record**: (i) a **decontaminated review occurred** … and (ii) **the contract tiers are filled**."* `1.5-criteria.md:123-127` makes stating them a **gating** requirement at all 8 baseline loci. Replacing one claim with two different claims is a substitution, not a deletion.

And claim (i) is precisely the finding cycle 1 recorded as **NOT closed**. `hardening-cycle-1/decisions.md:101-103` (carry-forward #5, 2/3 major): *"PRV's positive half must not overclaim … 'a decontaminated review occurred', 'tiers filled **and cited**', 'the sweep **was run**' are attestations by the constrained party, sampled and author-verified. **State what is checked and by whom, or narrow the claim again.**"* `decisions.md:214` lists *"the PRV-positive-half major"* among what pass 2 did **not** close.

Cycle 2 answers the "tiers filled" half credibly (BIND-currency + an SPV sample, both with named owners). It does **not** answer the decontamination half. What establishes decontamination is: the reviewer's own report of its context path list (`stages/charter.md:93-99` — self-reported), plus IDN's sibling-read ban, which `2-plan.md:101-103` enforces as *"a record citing a sibling record is **contaminated ⇒ un-run**"* — i.e. it catches only a reviewer that confesses. Nothing checks that a reviewer did not silently read `completeness/A.md` from the directory it was pointed at, which is FINDINGS F9's original mechanism (`FINDINGS.md:108-111`: *"Nothing forbids reviewer C from reading `A.md`, which sits in the very directory it is pointed at. Same defect class as F5: a gate whose satisfaction is asserted by the party it constrains."*).

S-PRV's three mandated non-claims (`1.5-criteria.md:128-132`) are tier-(iii)'s unprovable negative, correlated priors, and the cost/certainty line. **None** requires the artifact to state that decontamination itself is self-attested. So the artifact will assert, as gating text at 8 sites, a positive that the loop cannot check — under a scope justification claiming PRV adds nothing.

*Fix:* either narrow (i) to what is checked — *"the provenance record is present and BIND-current; decontamination is the reviewer's own attestation, unenforced"* — or add that limitation as a fourth mandated non-claim in S-PRV; and correct §2.1's justification, which is load-bearing for PRV's admission to scope.

---

**A/F5 · MAJOR · An undeclared departure from the approved on-disk layout: D8 creates `<node>/decisions.md` and relocates gate + red-team-route entries out of `plan/decisions.md`. Only RST's departure is declared.**

`2-plan.md:197` (D8): *"**partitioned**: per-node gate entries → **`<node>/decisions.md`** (that node's owner only); **`plan/decisions.md`** → **run-level events only**."* `2-plan.md:255` (D13) lists the root node's dir as carrying its own `decisions.md`.

The approved scope/decision record — which the Layer-2 config designates *"source of truth for every settled decision, the plan-artifact spine, **the on-disk layout**"* (`Architect/guarded-change.architect.md:27-30`) — fixes both halves against this:
- `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:170`: *"`decisions.md` ← append-only: **gates**, top-level-decomposition approval, **red-team routes**, overrides"*, under `plan/`.
- The same record's `tree/<node>/` listing (lines 174-179) enumerates `_status.md`, `plan.md`, `completeness/`, `adversarial/`, `<child>/…` — **no `decisions.md`**.

The baseline artifact matches the approved record (`SKILL.md:61-62`: *"Maintain `plan/decisions.md` (append-only: gates, top-level-decomposition approval, red-team routes, cap bounces, convergence escalations, overrides) — the iteration cap reads this log"*), so cycle 2 introduces the deviation.

Cycle 2 declares exactly one layout departure — RST's apex roll-up move — at `1-spec.md:140`, `2-plan.md:258-263` and `1.5-criteria.md:217-218`. It cites `1-this-is-a-proud-scott.md:173` for it; I verified line 173 is indeed `tree/_status.md ← apex roll-up`, so that declaration is sound. The gate-log partition gets no such treatment anywhere in the spec, plan or criteria.

This is the exact shape of cycle 1's carried-forward item 11 (`hardening-cycle-1/decisions.md:117-122`), which is why the approved record was added to the reviewer's closed set. It is a new instance of the finding that omission produced.

*Fix:* declare the gate-log partition as a second deliberate departure in this cycle's `decisions.md`, with the same treatment RST receives, and extend S-RST's inspection row to cover it. (`plan/assembly-approval.md` is a third layout addition but is entailed by newly-ratified R2, so it is authorized.)

---

**A/F6 · MAJOR · Four cycle-2 edits falsify `charter.md`'s fork-provenance blockquote, which is handed to every cold reviewer verbatim — and SC5 checks only that the blockquote exists and its source hash matches.**

`Architect/stages/charter.md:11-22` is a provenance blockquote whose claims are specific and enumerated: the guarded-change core is *"carried whole"*, naming *"spot-verify-citations, provenance + reviewer-input-is-a-closed-set"* among the carried bullets; *"**ADDED:** a standing **sixth Completeness lens**"*; *"**DROPPED:** nothing from the core."* `charter.md:8-9` states the core below *"is given to the reviewer **verbatim**."*

Cycle 2 modifies three of the named carried bullets in place:
- D7 (`2-plan.md:178-184`) replaces the spot-verify bullet's owner — baseline `charter.md:88`: *"**Whoever consumes the review** checks a sample…"* → stage 5.
- D1 (`2-plan.md:87`) adds a comparison duty to the provenance bullet (`charter.md:93-99`).
- D2 (`2-plan.md:104`) adds `spawn_id` to provenance and narrows the closed set to exclude the node's own `completeness/`/`adversarial/` dirs — the closed set is defined at `charter.md:98-100`.
- D8 (`2-plan.md:207-208`) further edits the closed set to name the node's own gate log.

After the build the blockquote will assert "carried whole … DROPPED: nothing … ADDED: [one lens]" about a core that has four local modifications, one of which reassigns a duty the blockquote names by title. Because the blockquote is given to reviewers verbatim, every future Architect cold reviewer is told its spot-verify duty is guarded-change's unmodified bullet while the text below says something different.

`1.5-criteria.md:327-332` (SC5) is the only criterion touching it: *"`stages/charter.md`'s fork-provenance blockquote is still present and its cited source sha256 still matches `Guarded_change/stages/charter.md`."* Presence plus an upstream hash. Nothing observes the carried/added/dropped enumeration — and the hash check will keep passing, since it hashes the *source*, not the fork.

*Fix:* add to SC5 (or a new S-row) that the blockquote's ADDED/DROPPED/carried enumeration must name every local modification this cycle makes to a carried core bullet, and add `charter.md`'s blockquote to D1/D2/D7/D8's site lists.

---

**A/F7 · MINOR · "8 occurrences across 5 files" is wrong — the 8 enumerated loci span 4 files. Verified exhaustively against the baseline tree.**

Asserted three times: `1-spec.md:158`, `1.5-criteria.md:123`, `2-plan.md:171`. The enumerated loci (`1.5-criteria.md:123-125`) are `SKILL.md:3`, `SKILL.md:8-9`, `SKILL.md:17`, `METHODOLOGY.md:3-5`, `METHODOLOGY.md:40`, `README.md:10`, `README.md:12-14`, `stages/stage-7-assemble.md:25-26` — 8 occurrences across `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stage-7-assemble.md` = **4 files**.

I materialised the baseline tree from `b08f5a9` and grepped it exhaustively for `proven|proves|not asserted|hole-free`: the only overclaim loci outside `changes/` and the Layer-2 config are the 8 enumerated ones. So the enumeration is complete and correct; the **file count is wrong**, and there is no unenumerated fifth file. (Note `METHODOLOGY.md:3` overclaims via *"complete, hole-free"* rather than "proven" — the citation is right, it just isn't findable by grepping "proven"; worth flagging because `check.sh`'s normalized matcher will need the right operative string for that one site.)

The count is load-bearing rhetoric in a **gating** criterion's scope statement, and it sits in the same cycle that corrects cycle 1's arithmetic (`1-spec.md:159`, `0-baseline.md:79-81`).

*Fix:* "8 occurrences across 4 files", and record the `METHODOLOGY.md:3` operative string separately since it does not contain the `PROVEN` token the paired absence sweep keys on.

---

**A/F8 · MINOR · §2.1's authority table — the artifact that exists to stop scope drift — omits D17/S-IDGREP's non-rename content.**

`1-spec.md:102` claims *"Three levels of authority are distinguished in this spec, and **no item is allowed to drift upward**"*, and `:113` claims *"The orchestrator-call row is declared, not smuggled."* The orchestrator-call row (`1-spec.md:107`) names *"**IDN**, **SPV**, **IGM**, **TPL3**, **XPM**, and the subtractive honesty set (**PRV**-softening, **OFL**)."*

R1's ratified parenthetical (verified verbatim against transcript record 694) names: *"BIND over gate artifacts, ID renames, RES, redteam_context, §4 heading, seed slots, elc, DEP, CNC, root pin."* "ID renames" covers `KIL`→`KLB` / `ING`→`IGM`. It does not cover D17's other four commitments (`2-plan.md:316-336`): the word-boundary + `templates/`/`examples/` grep-scope correction (B4/P19), the phantom caveat, the ID naming rule, and index rows for `TPL1`/`TPL2`/`SEV` plus 12 new IDs (B4/P20). Those are absent from both the ratified row and the declared orchestrator-call row, yet S-IDGREP (`1.5-criteria.md:262-272`) is **gating**.

The underlying work is traceable to a 3/3 confirmed-closed carry-forward (`hardening-cycle-1/decisions.md:106-109`), so this is a declaration gap, not an unratified inflation — but the table's stated purpose is to make exactly this visible.

*Fix:* add `IDGREP` (the non-rename half) to the orchestrator-call row with its confirmed-closed provenance cited.

---

**A/F9 · MINOR · §3B's heading labels XPM "ratified (R2)", contradicting §2.1's placement of XPM in the orchestrator-call row.**

`1-spec.md:146` heads the table *"### 3B — F8, ratified (R2)"*, and XPM is a row inside it (`:150`). `1-spec.md:107` lists **XPM** among *"the additional in-scope items **not** named in R1's parenthetical list"* — an orchestrator call. Both cannot be right.

The substance splits: XPM's *both-gates* correction is genuinely entailed by R2's ratified description (adding a gate at the end makes "GBP-gated only" false). XPM's *naming of the terminus artifact* is FINDINGS Tier 3's *"No stage covers exit-plan-mode"* (`FINDINGS.md:139`), which R2 does not entail and R1's parenthetical does not list. Under CH12 discipline the section heading grants the unratified half the ratified label — the upward drift §2.1 forbids, and the level a builder reads off the section it is working in.

*Fix:* retitle §3B (e.g. "F8 (R2-ratified) + the terminus correction it forces") and split XPM's row into its entailed half and its orchestrator-call half.

---

**A/F10 · MINOR · SC3 is a P row with no M, contradicting the criteria file's own absolute rule.**

`1.5-criteria.md:17` states *"**M is mandatory for every P row.**"* `1.5-criteria.md:311` labels SC3 *"gating · P + execution"* and the verification map at `:355` gives it *"line-offset + intra-block-order assertion **and** the X2 arms"* — no `baseline-replay.sh`. Every other row carrying P carries M; SC3 is the sole exception and no reason is stated. It is also replayable: the new intra-block order assertion must fail against `b08f5a9`, which is exactly the can-fail evidence a position criterion needs.

*Fix:* add M to SC3, or state the exemption reason inline.

---

**A/F11 · MINOR · `LOOP-STATE.md` still states, at the top, the terminate rule R3 voided — and it is the declared resume point.**

`1-spec.md:87-89` correctly records R3 and that *"Any earlier narrowing to 'no new blocker or major' is **superseded and void**."* Verified against transcript record 699.

`/home/zero/architect-hardening-loop/LOOP-STATE.md:8-9` still reads: *"**Terminate** when a cycle's self-review surfaces **no new blocker or major**, or after **cycle 3** — whichever comes first."* The correction appears only 75 lines later at `:84`. `LOOP-STATE.md:241-244` designates this file the resume point (*"To resume: read this file's cycle log"*), and `:1-9` is what a resuming runner reads first.

**Failure scenario.** Cycle 3's runner resumes from disk, reads the header's terminate rule, and terminates the loop after a minors-only self-review — the exact outcome R3 forbids. Cycle 2 cannot be faulted for not editing a file outside its touched set, but the finding belongs to the orchestrator and this review is the place it surfaces.

*Fix:* amend `LOOP-STATE.md:8-9` in place to the ratified literal rule, with a pointer to R3.

---

**A/F12 · NITPICK · R1's option description is presented as "verbatim" with an unmarked truncation.**

`1-spec.md:69-70` quotes R1's option text ending at *"…defer to a later cycle."* The actual description (transcript record 694) continues: *"Bounded blast radius, real delivered value, and the ordering diagnosis + transcript-locus correction make the deferred work tractable next time."* The omitted sentence is rationale, not scope, so nothing material is hidden — but the spec's own R2/R3 quotes use explicit `…` markers and this one does not, in the record whose whole purpose is spot-checkability.

---

## Closure audit

Confirmed-closed set taken from `hardening-cycle-1/decisions.md:203-209` (the two-reviewer-confirmed list, mechanisms named) cross-checked against the 12 carry-forwards at `decisions.md:84-124`.

| Confirmed-closed cycle-1 fix | In cycle 2? | Mechanism intact or weakened? | Evidence |
|---|---|---|---|
| escalation-vs-death precedence | **No — declared deferred** | n/a (F1) | `1-spec.md:168-175` declares it; no predicate reads a terminal status (`2-plan.md:46-49`) |
| SEAM sha256 equality, both operands named | **No — declared deferred** | n/a (F2) | `1-spec.md:176-178`; correctly ties the deferral to the cap's second instance |
| `spawn_id` dispatcher-recorded + declared-degraded | **Yes** | **Intact** | `2-plan.md:91-105`; both asymmetric rules stated; `unavailable-by-harness`; X3 polarity inverted (`1.5-criteria.md:76-79`). Cycle 1's gating-impossible unconditional rule dropped |
| RES(a)↔BIND unified, records immutable | **Yes** | **Intact** | `2-plan.md:73-78`, `:107-120`; `rebound_from`/`rebound_to`; *"a `clean-fixed-in-place` node IS assemblable"* stated positively. Root carve-out — cycle 1's pass-2 blocker — is explicit at `2-plan.md:70-71` + `1.5-criteria.md:45-48` |
| The position major (intra-block order **+ updated rationale** + can-fail variants) | **Partial** | **WEAKENED — the rationale half dropped** | **A/F1.** Cycle 1 required it (`hardening-cycle-1/1.5-criteria.md:356-357`, `2-plan.md:388`); cycle 2's SC3 (`1.5-criteria.md:311-320`) omits it while D16 adds a 4th rule to the block |
| The baseline site map, replay-testable | **Yes, in name** | **WEAKENED — cited oracle covers 18 of B2's 21 IDs** | **A/F2.** `ruleid-sitemap.sh:17` derives IDs from `METHODOLOGY.md`'s index table; run as cited it omits `TPL1`/`TPL2`/`SEV`, the three B2 itself flags as unindexed |
| The ID collisions, promise → instrument | **Yes** | **Intact** (same default-set caveat as above) | `oracles/idcollide.sh` verified live: baseline → 2 grandfathered + 2 exempt families, exit 0; `KIL ING` → 3 COLLISIONs, exit 1; cycle-2 ids → exit 0. B3's recorded self-test results match reality exactly |
| BIND extended over the gate artifacts | **Yes (APPROVAL only)** | **Narrowed, honestly** | `2-plan.md:79-84`. Cycle 1 also bound `AUDIT.md` (`hardening-cycle-1/2-plan.md:146-147`), which belonged to deferred F5 and was itself a pass-2 blocker; dropping it is consistent. The residual vacuity is disclosed at `2-plan.md:82-84`, `1-spec.md:184-186`, `2-plan.md:450` |
| `elc` honestly relabelled | **Yes** | **Intact** | `2-plan.md:221-229`; *"self-declared, not computed"*; one trip condition; the single-level formulation at `decomposition-node.md:24-25` removed with a paired sweep (`1.5-criteria.md:186-188`) |
| The `_status.md` schema's missing keys (`template`, granularity call) | **No — deferred** | **Deferral breaks a shipped fix** | **A/F3.** `1-spec.md:172` defers the schema, but D8 (`2-plan.md:195`) removes the only recorded destination for `template` (`stage-1:20`, `METHODOLOGY.md:195`, `seed/README.md:14`) |
| The closed-set omission (approved record in the reviewer set) | **Yes** | **Intact** | `guarded-change.architect.md:27-30` carries it as `redteam_context[2]`; it is item 4 of this review's own closed set |
| PRV's positive half (recorded **NOT** closed, `decisions.md:214`) | **Yes, attempted** | **Half-answered, on a false scope rationale** | **A/F4** |
| `off_limits_paths` fence (recorded **NOT** closed) | **Yes** | **Intact and genuinely subtractive** | `2-plan.md:147-154`; the fence sentence replaced, paired absence sweep on *"Naming is the fence"* (`1.5-criteria.md:115-116`); real-fence-from-outside stated |
| DIV (recorded **NOT** closed) | **No — deferred, not claimed** | n/a | `1-spec.md:187-189`; S-PRV requires the artifact **not** claim it (`1.5-criteria.md:133-134`); `1.5-criteria.md:340-341` declares the non-criterion |
| "declared deferral" escape hatch (found **illegal**) | **Not reproduced** | n/a | `1-spec.md:160`, `1.5-criteria.md:28-32`, `2-plan.md:433-437`. Verified against `Guarded_change/stages/stage-8.md:55-60`: *"the loop has exactly two legal moves"* — a representative pre-ship harness or named risk-acceptance. Cycle 2's claim is accurate |
| "two passes" unaudited ruling | **Not treated as settled** | n/a | `1-spec.md:190-192` keeps it on the owner queue explicitly |
| Cycle-1 scope-label inflation | **Corrected** | Intact | `1-spec.md:93-100` carries LOOP-STATE's hedge and names the two surviving loci (`hardening-cycle-1/3-charter-given.md:206`, `decisions.md:41`) as records not rewritten — both verified present |

**Anything present that was not confirmed closed and not authorized?** No unauthorized item found. All 15 FINDINGS Tier-3 bullets (`FINDINGS.md:120-143`) are either in §3A or declared in §4; F6 is declared inside F1 (`1-spec.md:173-174`); no item from the *"Triaged NOT genuine"* list (`FINDINGS.md:145-162`) is re-fixed — in particular "nested spawn may be impossible" and "no resume story" are untouched, and "two passes" is queued rather than declared settled. Two declaration defects only: **A/F8** (IDGREP absent from the authority table) and **A/F9** (XPM labelled ratified in §3B).

---

## Ratification audit (CH11/CH12)

**Durable source fetched and confirmed by me.** `/home/zero/.claude/projects/-home-zero-…/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`, 712 lines, mode `-rw-------` (0600) — the spec's harness-authorship claim at `1-spec.md:43-44` checks out. Records extracted with python.

- **Record 694** exists: `type: assistant`, `timestamp 2026-07-25T14:03:05.318Z`, one `tool_use` block, `name: AskUserQuestion`, `id: toolu_01Ga2368vabihTBcFVBZEYte`. **Every field the spec cites at `1-spec.md:46-47` matches exactly.**
- **Record 699** exists: `type: user`, `userType: external`, `timestamp 2026-07-25T14:10:24.209Z`, one `tool_result` block whose `tool_use_id` is `toolu_01Ga2368vabihTBcFVBZEYte` — keyed to 694 as claimed at `1-spec.md:48-49`. It also carries a `toolUseResult` object echoing all three questions with their full option sets.

| | R1 (SEV4 tie-break) | R2 (F8) | R3 (loop exit) |
|---|---|---|---|
| Flagged axis stated | Yes — `1-spec.md:64` | Yes — `1-spec.md:73` | Yes — `1-spec.md:87` (as *"my narrowing"*) |
| Options verbatim present | Yes; **all three labels confirmed** against 694 | Yes | Yes |
| Owner words verbatim | Yes — `1-spec.md:50-55`; **string-matches record 699 exactly**, with `…` marking elisions (one unmarked truncation → **A/F12**) | Yes | Yes |
| Durable source present, fetched, confirmed | **Yes — by me, directly** | Yes | Yes |
| Mapping disambiguates the flagged axis | **Yes.** Owner's answer is the option's exact label, `"Accept risk — ship narrower (Recommended)"`, not a partial or adjacent answer | **Yes.** `"Yes — human reviews the assembled plan"`, verbatim label | **Yes.** `"Literal — loop until truly nothing surfaces"` — and note the owner **rejected** the author's `(Recommended)` option, which is affirmative evidence against the CH11 "resolved into the author's own pick" failure mode |
| Elaboration inflation (CH12) | **One declaration defect, no inflation.** The spec treats R1's *parenthetical fix list* as ratified (`1-spec.md:106`) — legitimate, since the option's description is presented to the owner alongside the label, and I confirmed the quoted description is exact. Items beyond it are declared as orchestrator calls at `:107` — **except** IDGREP's non-rename half → **A/F8** | **No inflation in the three consequences.** R2's description reads verbatim *"Adds a second human gate at the end. … Costs a gate and requires the assembly fix to preserve a whole-plan reader."* Consequence (a) is the first sentence; (c) is the last, near-verbatim; (b) is entailed (adding an end gate makes "GBP-gated only" false). *"one gate at the end, not a gate per node"* is entailed by *"a second human gate at the end."* **The bounce mechanics are correctly flagged as unratified authoring choice** at `1-spec.md:82-84`, `2-plan.md:302-303`, `1.5-criteria.md:247-248` — this is RAT2 discipline done properly. **But** the §3B heading grants XPM's terminus-naming the ratified label → **A/F9** | **No inflation.** The option's own description reads *"Keep cycling while ANY new finding appears, including nitpicks, up to the 3-cycle bound"* — `1-spec.md:88` restates it without addition. `:90-91` correctly notes it is the orchestrator's accounting, not a licence available to this runner |

**Verdict:** all three ratifications are **valid artifacts** — the strongest part of this cycle's record. Two elaboration-labelling defects (A/F8, A/F9), one quotation nitpick (A/F12), no un-ratified mechanism.

**One methodological note in cycle 2's favour, verified:** `1-spec.md:57-61` records the owner-turn discriminator (a `tool_result` carrying an `AskUserQuestion`'s `tool_use_id`) and explicitly marks it *"an input to [F5], not implemented here."* Record 699 does carry that key, and it additionally carries `userType: external` — so the claim is true, and the restraint is correct: F5's mechanism is not smuggled in.

---

## Coverage challenge (CH8)

Behaviours this change can alter that **no criterion observes**:

1. **The rule block's closing rationale becomes a stale enumeration** (`SKILL.md:39-41`) once D16 adds a 4th rule. Not a B4 `CHANGE` row (R2 blind), carries no ID token (R1 blind), SC3 asserts order+membership only. → **A/F1, major.**
2. **`template used` loses its only recorded destination** when D8 strips `index.md`'s three writer sites, while the `_status.md` schema that was to receive it is deferred. S-CNC asserts the removal, never the destination. → **A/F3, major.**
3. **`charter.md`'s fork-provenance enumeration is falsified** by D1/D2/D7/D8's edits to carried core bullets. SC5 checks presence + upstream sha256 — both keep passing. → **A/F6, major.**
4. **R1 cannot observe site erosion for `TPL1`/`TPL2`/`SEV`**, and post-change compares a 33-ID default run against a 21-row hand-mixed baseline. → **A/F2, major.**
5. **The residual self-attestation in "a decontaminated review occurred"** — S-PRV's three mandated non-claims do not include it, so the artifact asserts a positive nothing checks. → **A/F4, major.**
6. **No criterion observes that a run halted at HG2 is resumable.** `2-plan.md:56` asserts *"A run that stops at the HALT is stopped, not deadlocked."* X2 (`1.5-criteria.md:251-253`) tests the **verdict** an agent returns, not that stage 8 can resume from that disk state and reach the terminus once `plan/assembly-approval.md` appears. S-HG2's *"it survives restart"* row asserts the stage-8 text is present, not that resume works. **Scenario:** HG2 halts; the approval is later recorded; the resumed runner finds `assembled-plan.md` already exists and stage-7 "done" by `stage-8:14`'s *stage-done-iff-output-exists*, so it never re-reads the approval and never presents — or re-runs stage 7 and rewrites the artifact the human just approved, staling it. **Severity: major**, and it is the one place cycle 2's new gate touches the restart contract without an executed check. (Flagged as adjacent to the failure-injection reviewer's frame; I raise it as a coverage gap, not a diagnosis.)
7. **The `plan/decisions.md` → `<node>/decisions.md` migration vs. CAP's reader.** `2-plan.md:197` says *"CAP counts a node's bounces from **its own** log."* R2/P9 checks the *sites*; nothing checks that a run-level cap event (e.g. the top-split bounce) is still countable once per-node entries move. **Severity: minor** — P9's R2 row plus CAP's R1 site set give partial cover.
8. **`check.sh` and `baseline-replay.sh` do not exist yet** (`oracles/` holds only `idcollide.sh` + `ruleid-sitemap.sh`; `2-plan.md:342-343` schedules them for stage 5). Every `S-` criterion's P and M arm is therefore **unverifiable at this gate** — correctly declared rather than hidden, but reported here as required by "flag the unverifiable."

---

## Label audit (CH9/CH10)

**Advisory labels.** Exactly one advisory item exists: S-CNC's no-executed-interleaving sub-item (`1.5-criteria.md:166-171`, restated `2-plan.md:410-416`). **The reason is legitimate, not a dodge.** The stated ground — *"the 'accessors' are prompt instructions to agents, not code, so there is no runnable read-modify-write window to inject into"* — is factually correct: I confirmed the four baseline `index.md` accessors are prose instructions (`stage-1:20`, `stage-6:11`, `METHODOLOGY.md:195`, `seed/README.md:14`), not code paths. The verifiable half (positive per-site assertions at every baseline accessor) is kept **gating**, and `1.5-criteria.md:344` declares the gap in §D. This is the correct disposition. **No dodge found.**

**Gating criteria — governed path confirmed, per criterion I checked:**

| Criterion | Governed path | Verified against that path, or a proxy? |
|---|---|---|
| S-BIND | stage-5 gating / stage-7 assembly decisions on a stale record | **Path.** P is labelled `PROXY` and paired with X1, whose holed arm is a real mismatched-hash fixture and whose intact arm includes a parent-less root (`1.5-criteria.md:56-60`) — this exercises the root carve-out that was cycle 1's blocker |
| S-IDN / S-RES | un-run determination; clean-vs-demoted at assembly | **Path**, and unusually well built: X3's polarity is deliberately inverted (`1.5-criteria.md:76-79`) so an agent cannot pass by pattern-matching "holed ⇒ block" |
| S-HG2 / S-XPM | the terminus decision | **Path** for the verdict; **not** for restart-resumability → CH8 gap 6 |
| S-CTX / S-IGM | config-validation stop; ingest `ABSENT` marking | **Path.** X4's holed arm is a config with the key genuinely absent |
| S-OFL, S-PRV, S-SPN, S-SLOT, S-IDGREP | the text of a claim / a heading string / an index's completeness | **Path — P is the criterion, not a proxy.** `1.5-criteria.md:13` and `2-plan.md:388-392` state the distinction correctly, and S-SPN's normalization requirement (`1.5-criteria.md:226-228`) is genuinely necessary since the six baseline spellings differ only in case, emphasis and parenthetical — I confirmed all six at B4/P18 |
| S-IDGREP (index completeness) | *(IDs with rows) ⊇ (IDs live in corpus)* | **PROXY, and the proxy is circular** → **A/F2.** Both oracles derive "IDs live in corpus" from the index table, so the check cannot fail on the class it exists to catch |
| R1 | site-set non-erosion over B2's 21 IDs | **Under-scoped to 18** → **A/F2** |
| R3 | post-change collision set | **Under-scoped** (same root cause); the can-fail self-test itself is real — I reproduced `KIL ING` ⇒ 3 COLLISIONs, exit 1 |
| SC3 | position/behaviour preservation | **Path** via X2's "GBP must still fire"; **but** missing M (**A/F10**) and missing the rationale assertion (**A/F1**) |
| SC1 / SC2 | validator + trigger surface | **Path.** SC2's gating reason at `1.5-criteria.md:307-309` is legitimate — PRV rewrites the only trigger surface |
| SC4 | live==source | **Path**, and the before-and-after pair (`1.5-criteria.md:322-325`) is what makes it non-vacuous. Correctly reasoned |

**Verdict:** labels are largely sound and several are better-than-required. Two defects: **R1/R3/S-IDGREP's shared circular ID-set proxy (A/F2)** and **SC3's missing M (A/F10)**.

---

## Ranked list

| # | ID | Severity | Claim |
|---|---|---|---|
| 1 | **A/F2** | **major** | R1/R3's oracles derive their ID set from the index table whose incompleteness is the finding — gating regression check silently under-scopes 3 of 21 IDs; B2's mechanical-provenance claim is false for those rows |
| 2 | **A/F3** | **major** | Deferring the `_status.md` schema while shipping CNC's `index.md` removal strands `template used` with no destination |
| 3 | **A/F1** | **major** | Confirmed-closed position fix ported with its "updated rationale" half dropped; D16 re-creates the stale three-item list |
| 4 | **A/F4** | **major** | PRV admitted on a false "strictly subtractive" rationale; adds the never-closed positive overclaim with no limitation required |
| 5 | **A/F6** | **major** | `charter.md`'s fork-provenance blockquote falsified by four edits to carried core bullets; SC5 checks only presence + upstream hash |
| 6 | **A/F5** | **major** | Undeclared departure from the approved on-disk layout (`<node>/decisions.md`; gate/route entries relocated) |
| 7 | *CH8-6* | **major** | No criterion observes that a run halted at HG2 is resumable to the terminus (raised as coverage; adjacent frame) |
| 8 | **A/F7** | minor | "8 occurrences across 5 files" — verified 4 files |
| 9 | **A/F8** | minor | IDGREP's non-rename scope missing from §2.1's authority table |
| 10 | **A/F9** | minor | §3B heading labels XPM ratified, contradicting §2.1 |
| 11 | **A/F10** | minor | SC3 is a P row without M, against the file's own absolute rule |
| 12 | **A/F11** | minor | `LOOP-STATE.md:8-9` still carries the terminate rule R3 voided; it is the resume point |
| 13 | **A/F12** | nitpick | R1's option text quoted "verbatim" with an unmarked truncation |

**WORST SEVERITY: major**

No blocker. Cycle 2 does not reproduce cycle 1's cap class within my frame: no predicate in `2-plan.md` reads a terminal `subtree:` status or a per-child seam hash (`2-plan.md:46-49`), the root carve-out that was pass 2's blocker is stated positively and executed by X1, and the illegal "declared deferral" route is absent and its illegality correctly grounded in `Guarded_change/stages/stage-8.md:55-60`. The three ratifications are valid artifacts, spot-verified by me against the harness transcript. The six majors are a mix of **two ported-but-weakened mechanisms** (A/F1, A/F2), **one narrowing that broke a fix it shipped** (A/F3), and **three honesty/declaration defects** (A/F4, A/F5, A/F6) — all fixable in place at stage 1/1.5 without re-architecting.

**Lens summary.** Factual: findings A/F2, A/F3, A/F5, A/F7 (all with source citations; several confirmed by executing the oracles and materialising the `b08f5a9` tree). Logical: A/F1, A/F3, CH8-6. Missed opportunity: **no issue found** — the "operand is computed, not stored" principle (`1-spec.md:25-36`) is the right lever for cycle 1's failure class, and I found no cheaper route to it. Unstated assumptions/risks: A/F3, A/F6, CH8 gaps 6-8; position/order sensitivity tested per the charter's trigger and A/F1 is that test's product. Fidelity: A/F4, A/F5, A/F8, A/F9 (terms pinned below).

**Fidelity terms pinned (charter lens 5).** *"confirmed closed"* → the two-reviewer-named-mechanism list at `hardening-cycle-1/decisions.md:203-209`, not LOOP-STATE's summary — cycle 2 uses the right source but ports one mechanism partially (A/F1) and one nominally (A/F2). *"ratified"* → a transcript-backed `tool_result` keyed to an `AskUserQuestion` `tool_use_id`; verified for all three, with one mislabelled row (A/F9). *"declared departure"* → a recorded deliberate change to the approved layout; implemented for RST, missing for the gate-log partition (A/F5). *"strictly subtractive"* → deletes a claim, adds no mechanism and no new positive claim; PRV fails this pin (A/F4). *"oracle"* → per ST1.5f/H6 a checker shown able to fail; `idcollide.sh` earns it (reproduced), `ruleid-sitemap.sh` earns its phantom self-test but not its scope (A/F2). *"human gate"* → under RAT3 a HALT + verbatim relay, never self-approved; HG2 implements that mechanism, not a proxy. *"advisory"* → a criterion whose stated reason survives challenge; the one advisory item does.

---

## Provenance

**Agent type + model:** general-purpose subagent · `claude-opus-5`. **spawn_id: unavailable.**

**Context paths actually read** (closed set = the 5 stage artifacts + `redteam_context` + the spec's touched-files list + carried-forward findings):

*Artifacts under review:* `hardening-cycle-2/{1-spec.md, 1.5-criteria.md, 2-plan.md, 0-baseline.md, oracles/idcollide.sh, oracles/ruleid-sitemap.sh}`
*Closed context set:* `FINDINGS.md`; `LOOP-STATE.md`; `hardening-cycle-1/{decisions.md, 2-plan.md, 1.5-criteria.md}`; `/home/zero/.claude/plans/1-this-is-a-proud-scott.md`; `Architect/{SKILL.md, METHODOLOGY.md, stages/charter.md, guarded-change.architect.md}`; `Guarded_change/stages/{stage-3.md, stage-8.md}`; the session transcript JSONL
*Baseline tree at `b08f5a9`*, materialised to scratch and read via `git show` / grep: `SKILL.md`, `METHODOLOGY.md`, `README.md`, `stages/{charter, stage-1…, stage-3…, stage-4…, stage-6…, stage-7…, stage-8…}.md`, `templates/seed/README.md`, `examples/authoring-a-skill/{README,planning}.md`
*Commands executed:* `idcollide.sh` (3 runs), `ruleid-sitemap.sh` (2 runs), exhaustive overclaim grep over the materialised baseline, python extraction of transcript records 693-700.

**No context outside this set was consulted.**

```
c554da51ba5a98485c4e58c8fefd5e6f5ef076961d4199619b681d91364c4a4d  hardening-cycle-2/1-spec.md
4edfb0b0c147b9bc31f752438f1e3a1f10cd0e50f978f2911de5ae03ca955c21  hardening-cycle-2/1.5-criteria.md
f1c18d67cc9a9cfd3020ed9a5f1a553ee58ab86ff60848d0a457660be5f7b10b  hardening-cycle-2/2-plan.md
251b008fd1e086fdad8c8374555b3e1b483860f325e71e6d85af5942b6673d10  hardening-cycle-2/0-baseline.md
6ab0743f310c31ca79bbe74e78d69fd9abb28559e7ae32c16f38c7e7aad0737b  hardening-cycle-2/oracles/idcollide.sh
eb011e56b37fe5824f5db07b97be68a1d84553d6f2acc1f938a8c5ee4cd3bb28  hardening-cycle-2/oracles/ruleid-sitemap.sh
794a40e7d54e913efe2c0d05e6f5360f731737ae241ef8d929480b4426bcbb11  hardening-cycle-1/decisions.md
0afe0acd19ed145b8061d61d2357528ed601ae6ac7e554a5250331ee5982cabf  hardening-cycle-1/2-plan.md
62227eb1d9c9c107cacfe1517ba16c51982da95e20b583bbaa9af2467ba00a66  hardening-cycle-1/1.5-criteria.md
7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450  Architect/SKILL.md
f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa  Architect/METHODOLOGY.md
6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819  Architect/stages/charter.md
c163ff87588dc97dbffae05cfe675985533ae8248b5d583d3322a090c4aceb8c  Architect/guarded-change.architect.md
16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3  Guarded_change/stages/stage-3.md
8160b9be9cc875eed958217cdc2611b5c38cea263c50a9ddf9757fe02e92fcd3  Guarded_change/stages/stage-8.md
94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8  /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
2555a812c1ca6ed355a128edeb7611df5248a80ae7c05948221498500c56d230  /home/zero/architect-hardening-loop/LOOP-STATE.md
aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249  /home/zero/.claude/plans/1-this-is-a-proud-scott.md
0fbc95713cec9e3ce3919c1c56e3a3b44444454728a9e67bdeed9b0edeedf9d7  .../45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl
```

*(The transcript hash is a live-session file and will drift as the session continues; records 694/699 are immutable prior lines and were verified at the state above.)*
