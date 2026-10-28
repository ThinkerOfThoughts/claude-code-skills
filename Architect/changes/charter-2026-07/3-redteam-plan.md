# Stage 3 — Red-team the plan (VERBATIM RECORD)

**Run:** `charter-2026-07`. Cold review of `{0-baseline, 1-spec, 1.5-criteria, 2-plan, decisions}`.

This is a **verbatim record** per the charter's provenance rule (B15). The author's interpretation lives in
`decisions.md`, separately. All five required provenance elements are present:

## (i) The verbatim charter/prompt given

`records/stage3-prompt.md`, sha256 `ae556a4a579bf84b46aa5401a53f5fc764bb3b9b41d9ab19bc0e068931d55b73`.
**All three reviewers received byte-identical text** — the prompt was written to disk first and each
reviewer was told only to read that path and execute it, precisely so the record could embed the charter
given rather than a reconstruction of it.

The prompt embeds the guarded-change charter **core verbatim** (the five lenses + the unconditional
discipline bullets + both conditional lenses, quoted as a blockquote from
`Guarded_change/stages/charter.md` @ `0e73bacf…adc590`), then the **stage-3 additions quoted as such**
(CH8 coverage challenge, CH9/CH10 label audit, CH11/CH12 ratification audit), then a task-specific
"things the author wants attacked" list explicitly marked as *not* a boundary and *not* pre-absolving.

**The unvetted-draft instruction was given, in the required terms**, as context entry 4:
"⚠ AN UNVETTED DRAFT WITH NO STANDING… an input proposal — not a baseline, not a spec, not a product. Do
NOT treat its assertions as settled. Do NOT rate a finding lower because 'the draft already says this'."

## (ii) The exact context path list given (closed set)

Stage artifacts: `0-baseline.md`, `1-spec.md`, `1.5-criteria.md`, `2-plan.md`, `decisions.md`.
Config `redteam_context`, priority-ordered, all 8 entries, each with its note — validated at run start
(8/8 live, `decisions.md`) and re-validated at spawn (6/6 new paths live).
Carried-forward findings from `decisions.md`: none (this is the run's first gate).

**Disclosed out-of-set reads.** All three reviewers independently read sources outside the closed set and
**declared them as the charter requires** — chiefly `Architect/guarded-change.architect.md` (the run's own
Layer-2 config) and the guarded-change stage files that the artifacts' ~20 rule-ID citations resolve to
(`stage-1.5.md`, `stage-3.md`, `stage-4.md`, `stage-8.md`). Reviewer B filed this as a finding against the
closed set itself (F-24): the artifacts cite these files as authority while the config does not list them,
forcing every reviewer to choose between an out-of-set read and marking most authority citations
unverifiable. **No reviewer received author-authored supplementary context.**

## (iii) The reviewers' verbatim output

| Reviewer | Record | Lines |
|---|---|---|
| A | `records/reviewer-A-verbatim.md` | 248 |
| B | `records/reviewer-B-verbatim.md` | 282 |
| C | `records/reviewer-C-verbatim.md` | 138 |

Reviewers A and B exceeded the inline return limit and were persisted by the harness; their text was
extracted programmatically from the harness's own persisted JSON (no re-typing) and only the harness
footer (`agentId`/`usage`) was stripped. Reviewer C returned inline and its text is transcribed whole.

## (iv) Reviewer agent type + model

| Reviewer | Agent type | Model |
|---|---|---|
| A | `general-purpose` | opus (claude-opus-5) |
| B | `general-purpose` | opus (claude-opus-5) |
| C | `general-purpose` | sonnet |

**"3 independent cold agents" was satisfied as three separately-spawned subagents**, dispatched in one
concurrent batch, with no shared context with this runner beyond the prompt path and no shared context
with each other. Not one agent asked three times. **Two different models** were used deliberately, because
dogfood F7 (`FINDINGS.md` L89–99) measured that same-model instances have *correlated* blind spots; the
run does not claim this makes them independent minds. Reviewer B independently filed F-16 arguing this
mitigation is the wrong level — F9's actual fix was a **spawn-identity field in each record**, which this
table now partially supplies and the charter's provenance element list still does not require.

## (v) Reviewer-reported sha256 of each context file

All three reviewers reported hashes. **They agree with each other and with this runner's own
`sha256sum`** on every file all three read — `Architect.md` `986512f5…bb78b`, fork source
`0e73bacf…adc590`, draft `6a1981f3…19212`, `FINDINGS.md` `94cb55e8…13ddb13c8`, transcript
`e98fd716…97289`, and the five stage artifacts. **No hash disagreement.** This is the check that would
have caught a reviewer reading a stale copy.

---

## Consumer's citation spot-verify (B14 — required, and this run's process rule 6)

A clean verdict must be **earned**. A sample of every reviewer's citations was re-checked against the
source by the runner. Commands and verbatim results:

```
$ wc -l Guarded_change/stages/charter.md
103 Guarded_change/stages/charter.md
```
→ **A-F22 / B-F22 CONFIRMED.** `0-baseline.md` §0.1's "(104 lines)" is wrong by one. (Reviewer C's M3-a
repeats "104" — it inherited the artifact's error, which is itself evidence the number propagates.)

```
$ sed -n '70,76p' Guarded_change/stages/charter.md
  read (the charter instructs the reviewer to report these). The charter given is the
  METHODOLOGY charter **core** verbatim — the five lenses + the unconditional discipline
  bullets, plus the coverage-challenge bullet for stage-3 reviews and any conditional lens
  (position / concurrency) whose trigger fires — with task-specific additions quoted
  as such. Reviewer input is a **closed set**: …
```
→ **A-F2 / B-F02 / C-F1-a CONFIRMED — converged 3/3.** The charter-**composition** rule is real, is in the
fork source, and is **absent from the B01–B18 inventory's B15 row**. All three reviewers found it
independently.

```
$ grep -rn "85%" Architect/guarded-change.architect.md Architect/README.md Architect/ATTEMPT-2-STATE.md
Architect/guarded-change.architect.md:77:  …including the measured singleton rate (~85% of findings caught by exactly one
Architect/ATTEMPT-2-STATE.md:87:  **wrong for findings**: ~85% of attempt 1's findings were caught by exactly one reviewer, …
Architect/README.md:31:  wrong for findings: measured across attempt 1's runs, ~85% of findings were caught by exactly one reviewer,
```
→ **A-F9 CONFIRMED.** `0-baseline.md` §0.6's "No singleton rate is recorded anywhere on disk" is **false
as written** — the run's own config states it as *measured*, in the very note handed to every reviewer.
The narrow claim (absent from `FINDINGS.md` and `LOOP-STATE.md`) still holds, and all three reviewers
independently reproduced that grep and **upheld D7 on the merits**.

```
$ sed -n '19p' /home/zero/.claude/skills/guarded-change/stages/stage-4.md
| **Blocker** | wrong problem / will not work / unverifiable | → 1 | → 5 | → 1 |
$ sed -n '135p' Architect/stages/charter.md
| **blocker** | The plan solves the wrong problem, contradicts a settled decision, omits a load-bearing element of the task, or cannot be executed as written. |
```
→ **A-F15 CONFIRMED** (A's line cite was L17, the table header; the substance is at L19). "Unverifiable"
is in the family's blocker definition and absent from the draft's.

```
$ sed -n '10p' /home/zero/Documents/Architect.md | grep -o "operate in paralell within that slot"
operate in paralell within that slot
```
→ **B-F17 CONFIRMED.** `0-baseline.md` §0.3 B17's premise "slot inheritance serialises siblings" is wrong
against the authoritative spec at the lines it cites. (The *conclusion* survives via the memo's
one-writer-per-node rule; reviewers B and C both challenged the conclusion and both found it holds.)

```
$ sed -n '8,12p' Dragonfly/stages/charter.md
> **Provenance:** forked from `Guarded_change/stages/charter.md @ 3d6889b` — the **unconditional core
> only.** … are **deliberately not carried** …
```
→ **B-F19 CONFIRMED.** No sha256 in the precedent. `1.5-criteria.md` C-01 attributes the sha requirement
to a precedent that does not contain it; its only actual source is the unvetted draft.

```
$ ls Architect/stages/
charter.md
```
→ **B-F03 CONFIRMED.** The fork source's fidelity lens ends "the operative duties are RAT1 and RAT2 in
`stages/stage-3.md`". No such file exists in Architect and none is planned.

```
$ grep -n "baseline rules whose declared intent" 1.5-criteria.md
29:| **C-02** | … Each of the 17 baseline rules whose declared intent is CARRY or CHANGE …
```
→ **A-F13 CONFIRMED.** `0-baseline.md` §0.3 assigns CARRY-or-CHANGE to all **18**; a generator reading
intents emits 18 and disagrees with the criteria document's 17.

Transcript records **51**, **1124** and **1171** were read directly and confirm reviewers A-F16 / B-F04 /
B-F21: record 51's option (b) is the *cold completeness-critic pass*, so record 55's "option be should be
done by three independent cold agents" attaches to **that**, not to the general adversarial red-team
(whose three agents come from item **6** of the same message); and records 1124/1171 show the author
twice proposed **folding** the sixth lens away, which **strengthens** D1's independence claim rather than
weakening it. **No fabricated citation was found in any of the three reviews.**

---

# REVIEWER A — VERBATIM

See `records/reviewer-A-verbatim.md` (248 lines, embedded on disk, unedited apart from the harness
footer). Worst severity: **blocker**.

# REVIEWER B — VERBATIM

See `records/reviewer-B-verbatim.md` (282 lines, embedded on disk, unedited apart from the harness
footer). Worst severity: **blocker**.

# REVIEWER C — VERBATIM

See `records/reviewer-C-verbatim.md` (138 lines). Worst severity: **major**.

---

## Union of findings (nothing discarded — `Architect.md` L24)

Deduplicated only on exact restatement; convergence noted but **never used to discard**.

### BLOCKER — 2 of 3 reviewers, independently

**BL-1 · C-17's position criterion has no valid verification.** (A-F1, B-F01. Reviewer C's finding #2 is
the adjacent case for the conditional lenses.)

`1.5-criteria.md` C-17 is gating, self-describes as the position criterion, and disclaims its text half as
insufficient (citing ST1.5d and H3 — both verified at `stage-1.5.md` L62–76 and `stage-8.md` L25–31). It
nominates **B-1** as its executed half. But B-1's arms are *fixture*-varying: HOLED = a plan with a step
above the floor, INTACT = the same plan with that step rewritten to sit at the floor. **Both arms receive
the same charter with the floor in the same place.** B-1 contains no positional variable.

Concrete failure, from reviewer A: *build the charter with the floor placed after the six lenses, run B-1
exactly as specified — the HOLED arm still files the vagueness finding, the INTACT arm still files none,
B-1 passes, and C-17 is marked verified by an experiment provably insensitive to the position it
governs.* `2-plan.md` §3 asserts "**H3 compliance**" for exactly this pairing.

Both reviewers independently identified the same fix and the same irony: the author **already built
charter-ablation apparatus** for B-3/B-4 and did not apply it to the one criterion that provably requires
it — which is the run's own D5 ("recurrence means under-generalization") failing against itself.

### MAJOR — grouped by whether this runner can resolve them

**Group 1 — resolvable by re-planning (runner's own authority).** M-01 the uninventoried
charter-composition rule (A-F2/B-F02/C-F1-a, **3/3**) · M-02 `rules.tsv` generated from the same document
that makes the claim, so the regression arm cannot see its own gaps (A-F3, B-F02b) · M-03 the CHANGE
class's "difference declared" half is checked nowhere (A-F8) · M-04 D3's closed-set rationale is unsound
and its resolution grants `Divisible` (2-arg) an input the spec cannot supply (A-F7, B-F05, C-FID-1,
**3/3**) · M-05 B-4's ablation deletes the arms' only disclosure that peers exist, so it runs backwards
(A-F6) · M-06 mutation tests against literal string probes are tautological, and no mutant shape exists
for the two absence sweeps (B-F07) · M-07 every arm is n=1 with no pass rate, and non-discrimination
triggers unbounded cap-exempt self-administered rebuild (B-F08) · M-08 the ablation pair is never diffed
and block 7 bundles three rules (B-F09, C-L2-a) · M-09 zero behavioral verification for the `Divisible`
caller and for 4 of 6 lenses (A-CH8, B-F10, C-CH8-1, **3/3**) · M-10 B18's precision counterweight
displaced from the fork source's terminal line (A-F10, B-F13, **2/3**) · M-11 B-2's fixture depends on
elements 2 and 3, unbuilt (A-F11) · M-12 no coverage of an empty/inoperable `_granularity` (A-F12) ·
M-13 C-18's advisory reason covers 1 of its 3 sub-clauses (A-F19, B-F06, C-CH9, **3/3**) · M-14 D6 adopts
a remedy dogfood F9's own text calls insufficient — F9's fix was a spawn-identity field (B-F16) · M-15
the run's closed set omits the config and stage files its citations resolve to (B-F24) · M-16 the
assembled-prompt order (charter vs. task/plan) is unspecified and unowned (B-F12).

**Group 2 — NOT resolvable by re-planning. These are gaps in the owner's design spec or in
orchestrator-owned files.** See `decisions.md` gate 4 and the halt.

- **H-A · The demotion rule names a human the spec cannot reach.** (A-F4, B-F11, **2/3**.) S14/C-08 are
  gating and require the charter to state that demoting a blocker|major requires the human owner.
  `~/Documents/Architect.md` defines exactly one human mechanism — `Human_gate(pair<string> _division,
  string _task, int _depth)`, L16 — which takes a **division**, fires only at `depth <= gate_depth`, and
  cannot receive a severity. Record **1258** removed the iteration-cap backstop whose tie-break authority
  the imported SEV3 points at. So the rule ships either **inert** or as an implicit demand for an
  unspecified human interrupt inside an autonomous recursive loop.
- **H-B · The spot-verify-citations consumer cannot perform the duty.** (A-F5.) C-12 is gating and
  requires the charter to name a consumer. The named consumers are `Union` — specified as "DISCARDS
  NOTHING" (`Architect.md` L24) — and `Severity`, which filters on the severity field (L26). Neither can
  act on a fabricated citation. `FINDINGS.md` L133 recorded this duty as "assigned to no stage" in attempt
  1; naming an agent that cannot perform it satisfies the criterion's text and leaves the defect.
- **H-C · RAT1/RAT2's operative duties would land nowhere.** (B-F03.) The carried fidelity lens ends
  "the operative duties are RAT1 and RAT2 in `stages/stage-3.md`". `ls Architect/stages/` = `charter.md`
  only, and `1-spec.md` §8 creates no stage files. Inlining `stage-3.md` L55–82 into the charter is a
  material scope decision; creating a stage file is a new element.
- **H-D · After the build, the config's own `redteam_context` note defames the shipped artifact.**
  (B-F14.) `Architect/guarded-change.architect.md` entry 4 tells every dispatched cold agent that
  `Architect/stages/charter.md` is "an UNVETTED DRAFT with NO standing… fair game." C-16/X2 remove the
  banner at build. The config is orchestrator-authored and on `1-spec.md` §8's **explicitly-NOT-touched**
  list. **This blocks stage 6** — the stage-6 reviewers would be instructed to discount the artifact they
  are reviewing.
- **H-E · The config asserts the rejected statistic as measured fact.** (A-F9.) `guarded-change.architect.md`
  L77 and `Architect/README.md` L31 both state the ~85% singleton rate; L77 is inside the `redteam_context`
  note handed to every reviewer. X1 strips the number from the charter while the dispatch context keeps
  asserting it.
- **H-F · Dogfood F7's charter-level fix was never considered.** (B-F15.) F7 is labelled by the dogfood
  "the deepest finding of the run" and its recommendation is a **charter mechanism**: hand each critic a
  *different* plan-type's `required_sections` as a differential prompt, converting tier (iii) from
  unbounded recall into a diff. Element 1 is exactly where it would live. Not adopted, not rejected, not
  recorded out-of-scope.

### MINOR (recorded, not looped on)

A-F13/F14/F16/F17/F18/F20/F21 · B-F17/F18/F19/F20/F21/F23/F25 · C-5/6/7.

### NITPICK

A-F22/F23 · B-F22.

## Worst severity: **BLOCKER**
