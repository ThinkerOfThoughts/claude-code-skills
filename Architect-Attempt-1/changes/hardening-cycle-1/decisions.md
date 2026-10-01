# decisions.md — hardening cycle 1 (append-only)

Gate log + the author's interpretation of the review records (which live verbatim in
`3-redteam-plan.*.verbatim.md`). The **iteration cap (CAP/SEV4)** reads this log.

---

## Run-start records

**2026-07-25 ~00:45 — run opened.** Subject: harden `Architect` against
`/home/zero/architect-dogfood-2026-07-24/FINDINGS.md`. Base commit **`3771038`**, worktree clean.
Executed by a **delegated subagent** with the main session as orchestrator; **the owner is asleep**
(RAT3 in force: every stop-for-human HALTS this runner and returns the question verbatim).

**2026-07-25 00:55 — CFG3 path validation (gate 4 may not pass without this recorded).** 15 paths
handed to cold reviewers were mechanically checked for existence + readability: `FINDINGS.md`,
`LOOP-STATE.md`, the approved scope record, `Guarded_change/`, `Dragonfly/`, `Data-Distiller/`,
`skill-creator/`, `Architect/`, the four stage artifacts, the frozen authoring criteria, the Layer-2
config, and the live copy. **Result: 15/15 OK, 0 dead.** No degraded-review acceptance needed.

**2026-07-25 ~00:52 — Layer-2 config updated (CFG6: the change updates `metrics`/`check` as part of
itself).** `guarded-change.architect.md` edited to: (a) add `FINDINGS.md` + `LOOP-STATE.md` as the two
top-priority `redteam_context` entries for hardening runs, with notes that include *"read the triaged-NOT-genuine
list — re-fixing a refuted finding is itself a fidelity error"*; (b) re-note the `Architect/` entry as
**the artifact under change** (run 2+) rather than the build output (run 1); (c) add the **`baseline:`
block** — this run is not greenfield, and the baseline for a prompt assembly is **textual** (frozen tree
by git + a word-boundary rule-ID site map + per-rule operative claims); (d) generalize
`check.output` to `changes/<slug>/8-harness.md`; (e) add run-2+ conformance items (5)–(8); (f) add the
new-rule-ID naming constraint. **Not recorded as a criteria change** — the criteria are per-change and
live in `1.5-criteria.md`.

**Declared out of scope, not silently dropped** (`1-spec.md` "Explicitly out of scope"):
- **F8 — whether a human must review the *assembled* plan, not just the top split. QUEUED FOR THE OWNER.
  Deliberately unimplemented, un-pre-shaped, and with no criterion written for it** (writing one would
  pre-shape the ruling). It *adds a human gate*, which is the owner's call per `LOOP-STATE.md`. Both
  reviewer A's and reviewer C's ratification audits were asked to check specifically for F8 pre-shaping;
  **A found none**, and **C raised D-5/D-6** (that bottom-up assembly deletes the only whole-assembled-plan
  reader, and XPM adds four sites asserting the terminus is GBP-gated-only, widening the migration surface
  an F8 "yes" would require). **C's point is accepted as a declaration duty, not resolved here** — it is
  relayed to the orchestrator with the gate-4 halt below, because deciding it *is* F8's territory.
- Three Tier-3 items from FINDINGS that the approved cycle-1 scope does not list: the **cost/fan-out
  envelope**, **ECON's O(children²) parent-seam load**, and the **"two passes aren't cost-justified"**
  half-finding. *(Reviewer C/F1-2 correctly notes the last of these is filed under "Triaged NOT genuine",
  not Tier 3 — the mis-filing is acknowledged; the item remains out of scope either way. Reviewer B/RAT-4
  additionally notes the "two passes" owner ruling is an **unaudited owner ruling** with no re-ask path
  and should be appended to `LOOP-STATE.md`'s owner-question queue rather than declared out of scope —
  that is an owner-queue decision, relayed, not taken here.)*

---

## GATE 4 (stage-3 red-team of {0-baseline, 1-spec, 1.5-criteria, 2-plan})

**Gate:** 4 · **Reviewers:** 3 cold, separately-spawned, disjoint frames (source-anchored /
failure-injection / fidelity-scope-honesty) · `general-purpose` / `claude-opus-5` ·
`spawn_id`s `a1cb9e6c3aa124a3f`, `ad7de94dda62399b4`, `a9f343344368cc2f7`.

**Worst finding severity: BLOCKER** (five: B/L-1, B/L-2, B/L-3, B/L-11, C/L-1 — see
`3-redteam-plan.md`). Reviewer A's worst was major; B and C each returned blocker.

**Citation spot-verify (CH6): PERFORMED and PASSED** before routing — 7 sampled claims, all confirmed
against source; one 2-character count drift in A (nitpick); **no fabricated citation**. The severities
below are therefore *earned*, and route.

**Route: BLOCKER → return to stage 1.** Per the severity table (SEV1) a blocker at gate 4 routes to
stage 1, and per **SEV3** the **reviewer's** severity routes — the author may contest only via a logged
entry, and **demoting a blocker or major additionally requires the human tie-break**. This runner
therefore does **not** demote, does not re-route to stage 2 on its own authority, and does not proceed.

**Stop-for-human fired (HIL/SK-STOP at gate 4): "any blocker — the loop is about to restart, confirm
direction first."** Under **RAT3** this **HALTS this runner**, which **returns the question verbatim to
its orchestrator**, marked as a question to relay — not a result. **Nothing past this point in the loop
was executed:** no build, no stage-6 review, no harness. The relay text is reproduced in the runner's
report to the orchestrator.

**Bounce count for the cap (SEV4):** this is **bounce 1** at gate 4 on finding class *"the plan
specifies the new predicates but not their producers / the criteria's oracles do not exercise the
behavioural half."* A second bounce at gate 4 on this class triggers the cap's human tie-break.

**Findings carried forward** (so the next reviewers confirm they were addressed rather than
re-deriving): the full ranked lists in all three verbatim records, with the five blockers and the twelve
convergent findings tabulated in `3-redteam-plan.md`. **In particular, the following must be answered by
any re-spec/re-plan:**

1. **Producers, not just predicates** (B/L-1, B/L-2, B/L-3, B/L-4, B/L-5): for **every** key in the
   `_status.md` schema, name the stage that writes it and its trigger — including the **success**-path
   write of a terminal `subtree:` (stage 6's LEAF branch; stage 6.5 for decomposing nodes), a
   **terminal-with-escalation** state so escalation is distinguishable from death, a **mechanical**
   `seam_rev` (a hash of the normalized §3 seam slice, so "did the seam change" is a diff not a
   judgment), a **structured `children:` map** holding the parent's per-child expectation, and a recorded
   **kill timestamp + `killed_handled`** pair so KIL's ordering predicate is disk-computable.
2. **`spawn_id` must be dispatcher-recorded, not self-reported** (B/L-11), with an explicit fallback —
   evidenced by `FINDINGS.md:148`'s dispatcher-observed id and by 2 of 3 of this run's own reviewers
   honestly reporting "unavailable".
3. **RES(a) must not let the author overwrite BIND's binding field** (C/L-1, B/L-10): keep the
   reviewer-reported hash immutable and record a separate `rebound_from`/`rebound_to` pair; state the
   precedence so X2 and X7 stop encoding opposite verdicts for one disk state.
4. **`DIV`'s differential frame needs real content** (3/3 major): the declared default (seed-skeleton
   section sets) *is* the 7-section spine, so frame B collapses into frame A. Either ship a real second
   plan-type's `required_sections` or make an absent `differential_section_sets` a **declared DIV
   degradation** (mirroring S-F4.4's non-vacuous validation).
5. **PRV's positive half must not overclaim** (2/3 major): "a decontaminated review occurred", "tiers
   filled **and cited**", "the sweep **was run**" are attestations by the constrained party, sampled and
   author-verified. State what is *checked* and by whom, or narrow the claim again.
6. **BIND must cover the new gate artifacts** (2/3 major): `APPROVAL.md` and `AUDIT.md` bound to the root
   `plan_sha256`, so a post-approval split change re-fires the **existing** gate.
7. **The baseline site map must be recaptured** (3/3 major): `stage-8` is a `HARDSTOP` phantom, not a
   `TOP` site; `ON TOP OF` survives `grep -w` at `METHODOLOGY.md:79` and `planning.md:25`; the accessor
   table misses three `index.md` writers; `TPL1`/`TPL2`/`SEV` are live IDs with no index row. **R1 as
   written fails its own baseline replay.**
8. **Rename `KIL` and `ING`** (A/F1-2): they violate this run's own ID rule (`KIL`⊂`SKILL`, 21 hits/4
   files; `ING`⊂`PLANNING`/`RULING`) — and ship the collision check as an **oracle**, not a promise.
9. **Position: place PRV/DIV *before* GBP** inside SKILL.md's rule block and update the block's closing
   three-item rationale to enumerate all five (3/3); S-SC3 must gain an intra-block ordering assertion.
10. **Eleven gating criteria are grep-only** (A/C2) on paths that are purely behavioural — S-C6
    (spot-verify duty), S-C4 (ingest `ABSENT` marks), S-F4 (absent `redteam_context` ⇒ stop the run) are
    the widest gaps and are cheap to add as X- arms.
11. **Process (2/3 major):** the stage-3 closed set omitted the approved-scope/decision record that the
    run's own config designates *"source of truth for every settled decision"*. Add it to the reviewer
    context for the next pass. **Reviewer A read it under declaration and reported one undeclared
    departure:** the record fixes `tree/_status.md` as the apex roll-up, and S-C9 requires that form to be
    **gone** — so pinning the root to `tree/root/` is a change to an **owner-approved on-disk layout** and
    must be declared as deliberate (or reconsidered).
12. **The `_status.md` schema omits `template` and the granularity call** (2/3) although derived
    `index.md` is documented to carry both.

**Orchestrator calls this runner did NOT make (relayed instead of taken):** the route choice itself
(stage 1 vs. stage 2 with a required addition), and D14's "a cold review satisfies the family's founding
rule for a **cross-project** catalog commit" (A/F5-1 asks for this to be a logged orchestrator call with
the alternative named, rather than settled in plan prose).

---

## Orchestrator routing decision after gate 4 / pass 1 (relayed answer, recorded)

**2026-07-25 — orchestrator, verbatim:** *"Routing decision (orchestrator): **re-enter at STAGE 1. No
demotion.** … stage 1 is what the severity table prescribes for a gate-4 blocker. Routing to stage 2
instead would be a **blocker demotion**, which SEV3 assigns to the *human* tie-break — and the owner is
asleep, so I will not take that authority. … **This is bounce 1 on finding class 'predicates specified,
producers unassigned / oracles don't exercise the behavioural half.' A second bounce on that class trips
the iteration cap and becomes a genuine stop-for-human.'"*
This is an **orchestrator call on sequencing within approved scope**, not an owner ruling — recorded as
such. It also **pre-declared the cap condition**, which is what fires below.

**Fidelity corrections applied to the loop's own framing (orchestrator agenda item D):**
1. `1-spec.md` no longer calls the broad scope reading "the approved cycle-1 scope"; it carries
   `LOOP-STATE.md`'s own hedge (*"Interpretation … stated so Roy can correct it"*). **Residual, found by
   pass-2 reviewer C (F1-4): the superseded phrasing survives at `3-charter-given.md:206` and at
   `decisions.md:41` above.** Not silently corrected — flagged, because those are records of what was
   given/decided at the time.
2. "no new blocker or major" is treated as a **continue** trigger only, never a licence to terminate.

## Pass 2 (stage 1 → 1.5 → 2 rebuilt around `PRD`)

`1-spec.v1-superseded.md`, `1.5-criteria.v1-superseded.md`, `2-plan.v1-superseded.md` retain pass 1.
`0-baseline.md` gained **B0.6** (corrected, authoritative site map — 21 IDs, phantoms triaged), **B0.7**
(the two measurement lessons promoted from prose into oracles), **B0.8** (the 24 baseline-claim
corrections + the declared owner-approved-layout departure). New spec rule **`PRD`**; `2-plan.md` §1 is
the required **assignment table**; IDs `KIL`→**`KLB`** and `ING`→**`IGM`** after
`oracles/idcollide.sh`'s prototype confirmed `KIL` ⊂ `SKILL` (21 hits / 4 files) and `ING` ⊂
`PLANNING`/`RULING`.

## GATE 4 (pass 2) — **ITERATION CAP TRIPPED**

**Reviewers:** 3 cold, separately-spawned, disjoint frames (closure-audit / failure-injection /
fidelity-honesty), `general-purpose` / `claude-opus-5`, dispatcher-recorded `spawn_id`s
`a7b5eb6d0dfbb794f`, (B — see record), `af13b7628d0aa4d37`. Closed set **extended** with the approved
scope/decision record (the pass-1 omission) and the pass-1 records as carried-forward findings.

**Worst finding severity: BLOCKER** — all three reviewers, independently.

**Citation spot-verify (CH6) PERFORMED and PASSED before routing** — five blockers checked against the
plan's own text, all five confirmed:
- terminal `subtree: complete` is assigned to **stage 6/6.5** (`2-plan.md:107`) but conditioned on
  `_assembled.md` (`:94`), a **stage-7** output — stage 6 runs *before* stage 7, so the write has no valid
  producer position ⇒ **B/L-1 re-opened**;
- `BIND`'s parent-hash clause (`:135,138`) has **zero** root carve-out (`grep` count 0) ⇒ the root's
  records can never be current ⇒ a single-node run cannot gate;
- `children.<c>.declared_seam_sha256` is assigned to "**stage 2** (initial)" (`:48`) when the child's
  `plan.md` does not yet exist ⇒ no initial operand ⇒ **B/L-3 re-worded, not closed**;
- `plan/topgate/AUDIT.md` (`:74,206`) is written **into** the directory `:188` fences against "the run" ⇒
  the fence and the cold audit are mutually exclusive;
- forbidding completeness frame A from tier (iii) collides with the charter's earned-clean clause
  (`stages/charter.md:86`), which requires **every** clean Completeness verdict to state the generative
  sweep ran ⇒ every record un-run.

**CAP DETERMINATION (SEV4).** *"Same finding class = same gate (by stage number) + same targeted artifact
section, regardless of wording — so a rephrased objection, or the same kind of defect resurfacing in a
nearby spot, still counts toward the cap."* This is **bounce 2 at gate 4** and the class is **the same**:
same gate (4), same targeted sections (the join's terminal-status producer; SEAM's operands; BIND's
operands), same defect kind (**a predicate whose operand has no valid producer, and an oracle that
pre-supplies the fact whose producer is broken**). Two reviewers say so in their own words — *"B/L-1
re-opened"* (A/F1-1), *"B/L-3 re-worded, not closed"* (A/F1-2), *"`S-F1.4` and `X1` freeze the wrong
producer"* (B/B-2), and A's coverage challenge CC-1: *"no criterion observes that a clean tree terminates
— every fixture pre-supplies the terminal facts whose producers are broken."*

**⇒ The iteration cap has tripped. The loop STOPS and a human breaks the tie** (accept the risk, change
the goal, or kill the change). Under **RAT3** this **HALTS this runner**, which returns the question
**verbatim** to its orchestrator to relay to the actual human. **No pass 3 was attempted; no severity was
demoted; no artifact file was edited.** `git diff --stat` over `SKILL.md`/`METHODOLOGY.md`/`stages/`/
`templates/`/`examples/`/`README.md` remains **empty**; the only modified file is
`guarded-change.architect.md` (the Layer-2 config) plus this change folder.

**Real progress, recorded so the tie-break is informed** (both A and C confirm with named mechanisms):
**3 of 5 pass-1 blockers and 10 of 12 convergent findings are genuinely closed.** C's list: escalation-vs-death
precedence; SEAM's sha256 equality test with both operands *named* (its initial-value gap is what re-opened);
`spawn_id` dispatcher-recorded + declared-degraded; RES(a)↔BIND unified into one rule with immutable records;
the position major (intra-block order + updated rationale + can-fail variants); the baseline site map (B0.6,
replay-testable); the ID collisions (promise → instrument); BIND over the gate artifacts; `elc` honestly
relabelled; the schema's missing keys; the closed-set omission.

**Not closed, and these are the substance of the tie-break:** the DIV-collapse major (pass 2 replaced it
with a mechanism C rates **worse** — and notes the `section-sets/` fallback is *"authored by this change's
own author for this purpose, so for cycle 1 it is the author's anticipation list one step removed"*); the
PRV-positive-half major; **`off_limits_paths` cannot enforce a fence — it is, in `METHODOLOGY.md:99-101`'s
own words, "naming is the fence"** (B/F1-1, a prohibition on the constrained party, promoted from a hedged
pass-1 minor into the plan's "principle 1"); **no admissible owner locus is demonstrated to exist** in this
harness (B/F1-3, C/D-4 — the only durable copies of owner words are agent-authored); and the
"declared deferral" route for an unverified gating criterion is **illegal** under
`Guarded_change/stages/stage-8.md` (C/L-3 — the legal route is HALT + relay, which is what this entry does).

**F8 remains untouched.** Two pass-2 findings say a fix **widens its migration surface and simultaneously
certifies one reading of it**: `S-C3`/`XPM` makes "the terminus is GBP-gated only" a **gating, verified**
property at four sites while D12 deletes the only whole-assembled-plan reader (A/F2-7, C/D-5). **Declared
here, not resolved** — deciding it is F8's territory.
