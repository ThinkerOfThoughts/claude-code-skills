# 2 — C1 rule oracle (independent, source-derived)

**What this is.** The ground truth for **C1** (rule inventory preserved & correctly scoped) and the
driver for **C5** (cross-file consistency) and **C9** (Theme-2 faithfulness). Every atomic normative
rule in the **CURRENT** `Dragonfly/SKILL.md` (149) + `METHODOLOGY.md` (521), each with a
**governing-stage-set derived mechanically from the current source** — the stages the rule *names* or
the section it appears under — **not** from the planned new layout (that would be self-referential;
gc's round-1 blocker). Built at stage 2, red-teamed at stage 3, **frozen at gate 4** (sha256 in
`decisions.md`). After build, C1 maps every row to its new stage-file home(s): present + correctly
scoped + no orphans.

**Stage-set vocabulary.** `0a 0b 1 2 3 4 5 6 7 8 9` = loop stages; `START` = hunt-start/config;
`PRE` = cold-start guard (before 0a); `TRIG` = trigger/proactive; `HIL` = human-in-the-loop stop
points (cross-cutting); `SELF` = self-check/dogfooding; `REF` = pure reference (config contract, two
layers, artifacts list — lands in slim METHODOLOGY, not a stage file).

**Theme-2 column.** `HOME=byref` marks a rule dragonfly currently holds **by reference** to
guarded-change; its **required new home** is dragonfly's own file (this is the C1∩C9 intersection).
`KEEP` marks a legitimate composition relationship (C10). `RETIRE` marks a rule Theme 2 deletes.

---

## Group A — loop-stage-specific rules (fire at one stage)

| ID | Rule (faithful summary) | Current source | Stage-set |
|---|---|---|---|
| A-0a1 | Restate reported symptoms in precise technical terms as numbered `S1,S2,…`; capture user repro steps as `R1,R2,…` | SKILL 0a; METH stage-0a | `0a` |
| A-0a2 | Show the numbered restatement back to the user; get confirmation/correction **before proceeding** (stop-for-human) | SKILL 0a; METH 0a; HIL | `0a` |
| A-0b1 | Write original wording **+** confirmed restatement into `symptom-ledger.md` | SKILL 0b; METH 0b | `0b` |
| A-0b2 | Symptom set is frozen; a symptom is struck only with a **recorded reason** | SKILL 0b; METH 0b; ledgers | `0b` |
| A-1-1 | Turn `R#` into a reliable, **representative** repro **BEFORE** hypothesizing | SKILL 1; METH stage-1 | `1` |
| A-1-2 | A "reproduction" that doesn't demonstrably reproduce a named `S#` is **not** a repro | SKILL 1; METH 1 | `1` |
| A-1-3 | Intermittent → **instrument-to-capture** (its own evidentiary bar; "label it intermittent" is not an escape) | SKILL 1; METH 1 | `1` |
| A-1-4 | Repro-ordering escape: repro infeasible blind → hypotheses MAY inform design **provided** the inversion is recorded in `decisions.md` **naming the infeasibility class**, and every such hypothesis stays `ungated` | SKILL 1; METH 1 (Repro-ordering escape) | `1` |
| A-2-1 | Observation ledger **append-only**: what / observation / citation (file:line, log row) / what it rules in-or-out | SKILL 2; METH stage-2 | `2` |
| A-2-2 | **No re-examination** of an area without first recording why the prior finding is insufficient | SKILL 2; METH 2 | `2` |
| A-3-1 | Hypotheses **ranked**, each **falsifiable**: names the observation that would CONFIRM and the one that would REFUTE; status open/confirmed/refuted | SKILL 3; METH stage-3 | `3` |
| A-3-2 | **No hypothesis without a discriminating test** that could distinguish it from rivals | SKILL 3; METH 3 | `3` |
| A-3-3 | Each hypothesis carries a **gate marker** `ungated → test-passed → cold-red-teamed` (distinct from open/confirmed/refuted status) | SKILL 3; METH 3 | `3` |
| A-4-1 | Design a test/instrument that **splits** the live hypotheses (rules ≥1 in or out) | SKILL 4; METH stage-4 | `4` |
| A-5-1 | Run; record result in observation ledger; update hypothesis statuses; **cite** the evidence | SKILL 5; METH stage-5 | `5` |
| A-6-1 | Convergence gate: are we **eliminating** hypotheses? | SKILL 6; METH stage-6 | `6` |
| A-6-2 | Iteration cap: after **N** cycles with **no** hypothesis eliminated (or N re-exams of one area) → **stop + escalate to human** | SKILL 6; METH 6 | `6` |
| A-6-3 | `N` from config (Layer-1 default **3**); if **no N resolvable**, Dragonfly **refuses to start** | SKILL 6; METH 6; config | `6` |
| A-6-4 | A **cycle** = one discriminating test **run AND recorded** (a completed 4→5 lap) | SKILL 6; METH 6 | `6` |
| A-6-5 | Per-`S#`-thread cycle counts + class-coverage + **shared-assumption** record appended to `decisions.md` each pass, else **gate violation** | SKILL 6; METH 6 | `6` |
| A-6-6 | Multiple `S#` threads count convergence **per-thread**; a thread hitting the cap **escalates alone**; threads may split into separate hunts with a recorded reason | METH 6 | `6` |
| A-7-1 | Declare "found" only with **all three**: (a) reproduce-on-demand; (b) cited causal chain root→symptom; (c) a **toggle** (flip cause → symptom appears/disappears predictably) | SKILL 7; METH stage-7 | `7` |
| A-7-2 | **Cold red-team the causal chain directly** at stage 7 (spawn a cold reviewer here) | SKILL 7; METH 7 | `7` |
| A-7-4 | **Depth check (root or relay?)**: why-down ONE level is (a) answered w/ cited evidence, (b) explicitly out of scope, or (c) not load-bearing — recorded; stage-7 cold pass challenges "root or relay?" | SKILL 7; METH 7 | `7` |
| A-7-5 | **Evidence-coverage sweep**: every observation-ledger row tied to the `S#` is explained by the chain **or** recorded as a named **residual** (ranked); silent absorption blocks "found" | SKILL 7; METH 7 | `7` |
| A-8-1 | Write `diagnosis.md`: root cause, causal chain w/ per-level depth-check status, named residuals, representative repro, recommended fix | SKILL 8; METH stage-8 | `8` |
| A-8-2 | **Hand `diagnosis.md` to guarded-change to make the fix; Dragonfly does NOT author the fix itself** (KEEP — the legitimate stage-8 handoff, C10; a workflow handoff, not a rules-dependency) | SKILL 76-77; METH 231 | `8` |
| A-8-3 | "**Characterized, not found**" = the only other legal terminal verdict — ALL of (a)–(e) incl. explicit **human sign-off** (e = presentation tier stays "characterization") | SKILL 8; METH 7/8 | `7`,`8` |
| A-9-1 | Verify the **root cause is resolved**, not merely the symptom suppressed | SKILL 9; METH stage-9 | `9` |
| A-9-2 | **9a Local** (if testable): check **both** cause condition gone AND symptom gone. Route: both gone→9b; symptom gone/cause active→masking→**guarded-change**; symptom persists→**stage 0** | SKILL 9; METH 9 | `9` |
| A-9-3 | **9b Live** (always when not locally testable, and after a local pass): the **user** runs it (final authority). Route: resolved→done; not→stage 0 | SKILL 9; METH 9; HIL | `9` |
| A-9-4 | Rate-based symptom → 9a/9b define the **observation window up front** from ledger frequency | SKILL 9; METH 9 | `9` |
| A-9-5 | A failed verification is recorded as a **new symptom** (never discarded) | SKILL 9; METH 9 | `9` |
| A-9-6 | **Stage 9 re-checks the residuals list** — killing the primary does not close an unexplained residual; residuals struck only with a recorded reason (round-2 B-4) | SKILL 88; METH 255-256 | `9` |
| A-9-7 | **Characterized handoff → stage 9 verifies the marked mitigations on symptom-evidence only** — no cause-resolution claim is made or verified (distinct from A-8-3's verdict bar) (round-2 B-5) | SKILL 88; METH 234-235 | `9` |

## Group B — cross-cutting rules (fire at multiple stages → repeated into each governing stage)

| ID | Rule (faithful summary) | Current source | Stage-set | Theme-2 |
|---|---|---|---|---|
| B-REP-1 | **Representativeness gate** (mandatory, blocking, non-waivable): a diagnostic artifact is untrusted until a **control run is shown to exhibit the symptom**; reject+redesign any whose control does not | SKILL "representativeness gate"; METH "representativeness gate" | `1`,`4` | |
| B-REP-2 | Intermittent/instrument-to-capture **satisfies the gate differently** (instrument shown to capture the symptom on a known occurrence) — does not bypass it | SKILL rep-gate; METH rep-gate | `1`,`4` | |
| B-REP-3 | **Detector/readout** must **fire on a known-true instance AND stay silent on a known-clean one** before its readings are consumed | SKILL rep-gate; METH rep-gate | `1`,`4`,`7` | |
| B-TRI-1 | **Every** diagnostic artifact (repro/test/instrument/toggle/detector) runs through the triage before it is trusted | SKILL triage; METH triage | `1`,`4`,`7` | |
| B-TRI-2 | Triage **priority order**: (1) consumes tokens/credits→**full GC** (overrides size); (2) multi-file / mutates state / non-obvious→**full GC**; (3) single self-contained read-only ≤~50 lines→**GC-lite**; (4) in doubt→**full** | SKILL triage; METH triage | `1`,`4`,`7` | |
| B-TRI-3 | Triage result **recorded in `decisions.md`** — unrecorded = didn't happen (artifact untrusted) | SKILL triage; METH triage/lite | `1`,`4`,`7` | |
| B-CH-lens | Charter: four **separate** lenses — factual / logical / missed-opportunity / unstated-assumptions | METH charter (byref to GC) | `1`,`4`,`7` | **HOME=byref** |
| B-CH-code | Cold reviewer given **both** the artifact **and** the underlying source (`redteam_context`); docs-only review insufficient | METH charter (byref) | `1`,`4`,`7` | **HOME=byref** |
| B-CH-cite | **Cite or it doesn't count** — each finding names a line/file or a concrete scenario | METH charter; SKILL 118 | `1`,`4`,`7` | **HOME=byref** |
| B-CH-rank | **Rank every finding** by severity | METH charter | `1`,`4`,`7` | **HOME=byref** |
| B-CH-unver | **Flag the unverifiable** — any claim not checkable against source reported as such | METH charter | `1`,`4`,`7` | **HOME=byref** |
| B-CH-noiss | "**No issue found**" per lens is valid and expected | METH charter; SKILL 77 | `1`,`4`,`7` | **HOME=byref** |
| B-CH-clean | A clean **factual** lens must be **earned with citations** (zero source cites → treated as un-run, re-run) | METH charter | `1`,`4`,`7` | **HOME=byref** |
| B-CH-spot | **Spot-verify** a sample of the reviewer's cited file:lines actually exist | SKILL 121; METH charter | `1`,`4`,`7` | **HOME=byref** |
| B-CH-prec | Reviewer graded on **precision** (are its findings real?), not body count | METH charter; SKILL 77 | `1`,`4`,`7` | **HOME=byref** |
| B-AIM-1 | Aiming: **does the test reproduce the named `S#`, or a neighbor?** (representativeness challenge) | SKILL 118-120; METH charter aiming | `1`,`4` | |
| B-AIM-2 | Aiming: **are any identifiers/paths/calls confabulated?** | SKILL 120; METH aiming | `1`,`4`,`7` | |
| B-AIM-3 | Aiming: **does the causal chain follow from the cited evidence**, or is it asserted? | METH aiming | `7` | |
| B-AIM-4 | Aiming: **root or relay** — is the claimed root the deepest node the project can act on? | METH aiming | `7` | |
| B-AIM-5 | Aiming: **what assumption does the live hypothesis set share, and is it true?** | SKILL 121; METH aiming | `1`,`4`,`7` | |
| B-PROV-1 | **Provenance** (unconditional): every cold pass records verbatim charter, exact context list, reviewer's verbatim output, agent type+model, reviewer-reported context hashes — missing any = **un-run** | SKILL 123; METH provenance | `1`,`4`,`7` | **HOME=byref** |
| B-PROV-2 | Coverage-challenge does **NOT** apply to dragonfly's **direct stage-7/lite** passes (analog = shared-assumption aim); a **full-GC triage** run keeps ALL of guarded-change's own stage duties incl. its stage-3 coverage challenge | METH provenance para | `1`,`4`,`7` / full-GC | **KEEP** (full-GC) |
| B-GBP-1 | Gate-before-present: an `ungated` hypothesis is presented only as **"candidate, ungated"** — never leading/likely/probable/most-likely cause, never a conclusion to act on | SKILL 133-135; METH "gate-before-present"; HIL | `3`,`7`,`HIL` | |
| B-GBP-2 | `test-passed` → may present as **"leading/best-supported candidate so far"** but must carry that its **causal chain is not yet red-teamed** | METH gate-before-present | `3`,`7`,`HIL` | |
| B-GBP-3 | `cold-red-teamed` → may present as **the root cause** ("confirmed" additionally needs the stage-7 three-part bar) | METH gate-before-present; SKILL 132 | `3`,`7`,`HIL` | |
| B-GBP-4 | **Rank is not endorsement** — showing the ranked list / "most plausible so far" is always allowed | SKILL 57,135; METH gate-before-present | `3`,`7`,`HIL` | |
| B-TBG-1 | **Trust-before-gate ordering**: an artifact's reading may not be **consumed** by a later stage (eliminate a hypothesis, advance a gate marker, inform the human) until its triage is **recorded passed** in `decisions.md` | SKILL 63-64; METH stage-5 + gate-before-present | `4`,`5`,`6`,`7` (widened round-3: consumption also at 6/7) | |
| B-SEV-1 | **Severity model**: blocker (wrong problem/unverifiable), major (sound goal/wrong approach), minor (local/fixable in place), nitpick (style); **worst finding routes the gate** | METH "severity model" (byref to GC) | `1`,`4`,`6`,`7` | **HOME=byref** |
| B-SEV-2 | **Iteration cap** on any review gate: after **2 bounces** at the same gate on the same finding class → a **human** breaks the tie | METH severity model | `1`,`4`,`6`,`7` | **HOME=byref** |
| B-LED-1 | Ledgers are **files** (not conversation context); symptom ledger **frozen**, observation ledger **append-only** | METH "the ledgers"; SKILL 31 | `0b`,`2` | |
| B-LED-2 | **File persistence is load-bearing** — the cold-start guard would destroy any in-context ledger, so ledgers must survive a restart on disk | METH ledgers | `0b`,`2`,`PRE` | |
| B-EVID-1 | **Evidence over rhetoric** (core principle): every conclusion cites a log row / file:line / observed result; "seems like X" is not a finding. Governs the agent's OWN claims at every conclusion-bearing stage, not only stage-5 records / reviewer findings (round-3 completeness) | METH 58-59 | `2`,`3`,`5`,`7`,`9` | |
| B-CAUS-1 | **Causality runs root-cause → symptom, never the reverse** (core principle): symptom-gone is necessary but NOT sufficient; a fix can mask a symptom while the cause survives; "found"/"fixed" are claims about the *cause*. Underwrites the stage-7 toggle requirement + the stage-9 masking route (round-3 completeness) | METH 64-67; SKILL 80-81 | `7`,`9` | |
| B-CH-inherit | **The charter enumeration is non-exhaustive by design**: cold passes inherit ALL of guarded-change's *unconditional* discipline bullets (those with no stage/trigger scope), provenance included — so the fork must carry the **FULL unconditional set**, not only the enumerated B-CH-* rows (round-3 completeness — the guardrail against the fork silently dropping an un-enumerated bullet). Post-fork this becomes "dragonfly's own charter IS the complete unconditional set" (self-contained; nothing left to inherit by reference) | METH 394-396 | `1`,`4`,`7` | **HOME=byref** (dissolves post-fork → self-contained charter) |

## Group C — framing / entry / reference / self-check rules

| ID | Rule (faithful summary) | Current source | Stage-set | Theme-2 |
|---|---|---|---|---|
| C-ST-1 | Config lookup (`dragonfly.*.{md,yaml}`); **do not invent project specifics** (paths, repro, redteam_context) | SKILL Inputs; METH two-layers/config | `START` | |
| C-ST-2 | **Validate config paths at hunt start**: dead/unresolvable→**stop**; adaptable→**adapt+record+proceed** | SKILL 20; METH config contract | `START` | |
| C-COLD-1 | **Cold-start guard**: if invoked in a long/thrashing session, **recommend a fresh session** + emit a carry-over brief pointing at the four files (frozen symptom ledger, observation ledger, `hypotheses.md`, `decisions.md`) | SKILL 22-27; METH cold-start guard | `PRE` | |
| C-TRIG-1 | Trigger: `/dragonfly` explicit; **proactive suggestion** on a diagnosis-shaped request, with a **precision bar** (not every error string / stack trace / build failure) — "behaving wrong and we don't know why", not "an error appeared" | METH trigger; SKILL description | `TRIG` | |
| C-LITE-1 | **guarded-change-lite** definition: a **single cold red-team pass** of the artifact using the (dragonfly) charter — four lenses + evidence discipline — against a one-line intent + a checkable "does exactly X, exercises path P" criterion → fix → run | SKILL 106-109; METH "diagnostic-artifact triage" (byref to GC charter) | `1`,`4`,`7` | **HOME=byref** |
| C-LITE-2 | Lite **keeps the charter verbatim + the provenance record**, drops only the five-item doc-set scaffolding (spec/criteria/plan/baseline/regression); recorded minimally in `decisions.md` | METH lite para | `1`,`4`,`7` | **HOME=byref** (fork; drop "pointer back to GC as source of truth") |
| C-HIL-1 | **Stop-for-human** at: 0a restatement confirm; a blocker about to restart; convergence gate fires; a characterized-verdict sign-off; stage-9b live verification; missing config; dead/unresolvable config paths | SKILL 126-135; METH human-in-the-loop | `HIL` | |
| C-HIL-2 | **Never present an ungated hypothesis as the likely/leading cause**; candidate→leading(`test-passed`)→root cause(`cold-red-teamed`); ranking always fine (= B-GBP restated in HIL) | SKILL 131-135; METH HIL | `HIL` | |
| C-SELF-1 | Self-check: run a cold stage-3-style red-team on the skill's own files after edits; these are **prompts** (position-sensitive) → **non-trivial edits take the full guarded-change loop** | SKILL 137-142 | `SELF` | |
| C-SELF-2 | Standing self-check criterion: **live == source** (`diff`) | SKILL 143 | `SELF` | |
| C-SELF-3 | Standing self-check criterion: **SKILL ↔ METHODOLOGY consistency** on every shared rule | SKILL 143 | `SELF` | |
| C-SELF-4 | Standing self-check criterion: **behavior-preservation** for anything moved/removed | SKILL 144 | `SELF` | |
| C-SELF-5 | Standing self-check: **every named guarded-change cross-reference (charter, severity model, probabilistic rubric, lite definition) resolves — severed = failure** (the D-11 check) | SKILL 144-145 | `SELF` | **RETIRE** → replace w/ `forked from guarded-change <rev>` provenance note |
| C-SELF-6 | The **flagship test** is **aspirational — not yet run**; an unrun check may not be described as an existing safeguard | SKILL 146-149 | `SELF` | |
| C-REF-1 | The **two layers**: Layer-1 agnostic core (loop/ledgers/gates/rep-gate/triage/charter/severity/default N); Layer-2 per-project config | METH "two layers" | `REF` | **byref clause**: METH:420 "the red-team charter (**referenced from guarded-change**)" → rewrite to "dragonfly's own charter (`stages/charter.md`)" (round-2) |
| C-REF-2 | The **config contract** (Layer-2 yaml): `redteam_context` priority-ordered; `reproduction.how/logs`; `ledgers.dir`; `iteration_cap.N` (default 3); path validation at hunt start | METH "config contract" | `REF`,`START` | |
| C-REF-3 | **What a run produces**: `symptom-ledger.md`, `observation-ledger.md`, `hypotheses.md`, `diagnosis.md`(stage 8), `decisions.md`(append-only gate log + iteration-cap memory) | METH "what a run produces" | `REF` | |

## Theme-2 rules-dependency summary (the C9 target set)

The **rules currently held by-reference** to guarded-change (`HOME=byref` above), whose required new
home is dragonfly's own files:

1. **Reviewer charter** — B-CH-lens, B-CH-code, B-CH-cite, B-CH-rank, B-CH-unver, B-CH-noiss,
   B-CH-clean, B-CH-spot, B-CH-prec, B-CH-inherit, B-PROV-1 → **new home `Dragonfly/stages/charter.md`**
   (forked from `Guarded_change/stages/charter.md` **unconditional core**, + dragonfly's B-AIM aiming +
   the B-PROV-2 exclusion; B-CH-inherit is the catch-all mandating the FULL unconditional set is carried
   — it dissolves post-fork once the charter is self-contained).
2. **Severity model** — B-SEV-1, B-SEV-2 → **new home**: stated in dragonfly's gate stage files
   (stage-6 primarily; the review gates at 1/4/7 reference it) + charter.
3. **Rate-based/probabilistic rubric** — the rate-based half of A-7-1 item (c) + A-9-4 → **new home**:
   stage-7.md + stage-9.md, stated in full. (There is no separate `A-7-3` row; the rate-rubric lives
   inside A-7-1(c), METH 199-202.)
4. **guarded-change-lite definition** — C-LITE-1, C-LITE-2 → **new home**: the triage rule in the
   stage files (1/4/7), referencing **dragonfly's own** charter.

**Removed:** C-SELF-5 (D-11 cross-reference self-check) → replaced by a light provenance note.
**Preserved (C10, KEEP):** A-8-2 (stage-8 handoff to guarded-change; do not author the fix) and
B-PROV-2 / the full-GC triage invocation (B-TRI-2 rules 1&2 route into a full guarded-change run).

---

**Row count (derived mechanically, not hand-typed):** Group A **35** + Group B **34** + Group C **17**
= **86 atomic rules.** Counts verified via `grep -cE '^\| A-' / '^\| B-' / '^\| C-'`. History: round-1
review caught a hand-count error (78 claimed vs 80 enumerated) + a missing row (A-8-2) → 81; round-2
review caught two more missing stage-9 rows (A-9-6, A-9-7) → 83; round-3 **independent completeness
re-derivation** (a cold enumerator, ~86 source statements enumerated fresh then reconciled) added
three under-represented core-principle/catch-all rows (B-EVID-1 evidence-over-rhetoric, B-CAUS-1
causality cause→symptom, B-CH-inherit the non-exhaustive-charter catch-all) + widened B-TBG-1's scope
→ **86**; that pass found **no spurious rows and no further load-bearing gaps.** **This count token must read identically in `1.5-criteria.md` and `2-plan.md`** (freeze
checklist greps for stragglers). Frozen at gate 4 with this file's sha256 in `decisions.md`.
