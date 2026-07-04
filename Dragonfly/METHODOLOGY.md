# Dragonfly — methodology

A gated loop for **diagnosing** bugs, where **no diagnostic conclusion reaches "accepted" without
an independent challenge**, and where **"found the bug" is proven by reproduce-on-demand + a causal
toggle** — not declared by the thing that produced it.

Dragonfly is the sibling of **guarded-change**: guarded-change is the gated loop for *making* a
change; Dragonfly is the gated loop for *finding* the bug that a change will fix. They compose —
Dragonfly hands a confirmed diagnosis to guarded-change, which makes the fix, and Dragonfly then
verifies the fix resolved the root cause. The name: the dragonfly is the most effective hunter of
insects (bugs) there is.

This document is the spec. The `dragonfly` skill *executes* it; a per-project config
*parameterizes* it. It is deliberately **project- and domain-agnostic** — nothing here assumes a
particular language, app, or bug.

---

## Why this exists

AI-assisted debugging has a characteristic, expensive failure mode. The motivating case: ~1.5
sessions of usage wasted on one relatively simple bug. The wasted session is the requirements doc.
Each failure maps to a structural defense Dragonfly builds in:

1. **Non-representative tests.** Six times, a test was written that did not actually produce the
   conditions it claimed to test — conclusions drawn from tests that tested nothing. (Three of the
   six also called an LLM/agent, burning tokens to run.) → defended by the **representativeness
   gate** + **diagnostic-artifact triage**.
2. **Thrashing.** The same areas re-checked repeatedly; prior findings ignored or forgotten. →
   defended by the **append-only observation ledger**.
3. **Symptom amnesia.** Symptoms selectively forgotten mid-hunt. → defended by the **frozen
   symptom ledger**.
4. **Confabulation.** Diagnostic code referencing variables that didn't exist, misplaced calls. →
   defended by the **cold red-team of every diagnostic artifact** before it runs.
5. **No convergence.** No stopping rule; tokens spent without narrowing the cause. → defended by
   the **convergence gate + iteration cap**.

This loop guards against all five: every diagnostic artifact is challenged by an **independent**
reviewer, the full symptom set and everything examined live in **append-only ledgers**, and "found"
is a **falsifiable, executed bar** — not an assertion.

---

## Core principles

- **Nothing self-certifies.** The author of a diagnostic artifact (a repro, a test, an instrument,
  a causal chain) never approves it. Review is done by a reviewer with *no shared context* (a cold
  subagent), so it doesn't inherit the author's blind spots.
- **A conclusion is gated before it is presented, not after.** "Nothing self-certifies" applies to
  the *hypothesis you hand the human*, not only to scripts and toggles. A hypothesis is an
  author-produced artifact; until an independent cold pass has fired for it, it may be **ranked**
  among candidates but never **presented as the leading / likely / probable / most-likely cause**,
  nor as a conclusion to act on — the moment a conclusion is leaned on, the gate it implies must already have
  fired (see *The gate-before-present rule* for which cold pass licenses which claim). Presenting an
  ungated hypothesis as the answer is the founding failure — a self-certified conclusion acted on —
  wearing the narrative instead of the code. Symmetrically, an artifact's *reading* is trusted only
  once its triage is recorded passed: gating precedes trust, it does not audit it retroactively.
- **Evidence over rhetoric.** Every conclusion cites a log row / file:line / observed result.
  "Seems like X" is not a finding; "line N logged Y, which only happens when Z" is.
- **A representative test, or no test.** A diagnostic artifact is untrusted until a **control run
  is shown to actually exhibit the symptom.** This is the single defense against the #1 failure
  above, and it is a hard, blocking, non-waivable gate. A test whose control does not exhibit the
  symptom is rejected and redesigned.
- **Causality runs root-cause → symptom, never the reverse.** A symptom is an *effect*. Making a
  symptom disappear does **not** prove the cause is gone — a fix can *mask* a symptom while the
  cause survives, and the bug then resurfaces through some other symptom later. "Symptom gone" is
  necessary but **not sufficient**; "found" and "fixed" are claims about the *cause*.
- **Memory is structural, not optional.** The full symptom set and everything examined live in
  **append-only ledgers** (files, not conversation context), so amnesia and thrashing are
  mechanically prevented, not merely discouraged.
- **A falsifiable bar for "found."** Reproduce-on-demand + a cited causal chain + a working toggle.
  Anything less is a hypothesis, not a diagnosis.
- **Diagnostic artifacts are AI-produced code, so they get guarded-change.** Every script,
  instrument, or toggle Dragonfly writes passes through guarded-change discipline (lite or full,
  by triage) before it is trusted — the same "nothing self-certifies" rule, applied to the tools
  of the hunt.
- **"No issue found" is a valid result.** Reviewers are graded on precision, not body count.

---

## The loop

```
0    CAPTURE
     0a TRANSLATION   restate the user's reported symptoms in precise technical terms as
                      numbered items S1, S2, …; capture user-provided repro steps as R1, R2, …
        → CONFIRM     show the numbered restatement back to the user; confirm/correct before
                      proceeding
     0b FREEZE        record original wording + confirmed restatement into the append-only
                      SYMPTOM LEDGER (a file; never silently dropped)
1    REPRODUCTION     turn R# into a reliable, REPRESENTATIVE repro BEFORE hypothesizing
                      (escape for bugs unreproducible blind: see stage-1 detail).
                      A repro that doesn't reproduce isn't one. Intermittent → instrument to
                      capture (with its own evidentiary bar). (Repro artifact → triage.)
2    OBSERVATION      append-only OBSERVATION LEDGER (a file): everything examined + citation +
     LEDGER          what it rules in/out. No re-examination without recording why the prior
                      finding is insufficient.
3    HYPOTHESES       ranked, each FALSIFIABLE: names the observation that would CONFIRM and the
                      one that would REFUTE it. status: open/confirmed/refuted. No hypothesis
                      without a discriminating test.
4    DISCRIMINATING   design a test/instrument that splits the live hypotheses.
     TEST (gated)     → representativeness gate + triage BEFORE running.
5    RUN & RECORD     run; log result in the observation ledger; update hypothesis statuses; cite.
6    CONVERGENCE      narrowing? ITERATION CAP (N, default 3): after N cycles with no hypothesis
     GATE            eliminated, or N re-examinations of one area → STOP, escalate to human.
7    ROOT-CAUSE       "found" requires ALL three: reproduce-on-demand; a cited causal chain
     CONFIRMATION    root→symptom; a TOGGLE (flipping the cause makes the symptom appear/
                      disappear predictably). Cold red-team the causal chain. (Toggle → triage.)
8    HANDOFF          emit DIAGNOSIS ARTIFACT → guarded-change makes the fix → returns
9    FIX VERIFICATION verify the ROOT CAUSE is resolved (not merely the symptom suppressed)
                      → done, or back to stage 0 / guarded-change (see stage detail)
```

The **most important gate is the representativeness gate** (it governs stages 1 and 4). It is the
cheapest place to kill the failure that wasted the motivating session: a test that doesn't test the
thing. Everything downstream of a non-representative test is wasted, so the gate sits upstream of
all conclusions.

---

## Stage detail

**0a — Translation.** Take the symptoms **as the user reported them** (their words, however loosely
stated) and restate them in precise technical terms, broken into **discrete numbered items** `S1`,
`S2`, … so every aspect has a stable handle later stages can reference unambiguously. Capture any
**user-provided reproduction steps** as `R1`, `R2`, …. End at a **confirmation checkpoint**: show
the numbered restatement (+ repro steps) back to the user; it must be confirmed or corrected before
the ledger is frozen. A misunderstanding caught here is free; caught at stage 7 it is a wasted
session.

**0b — Freeze.** Write both the user's original wording **and** the confirmed numbered restatement
into the **symptom ledger** (a file). The symptom set is frozen — symptoms are never silently
dropped; a symptom is only struck with a recorded reason.

**1 — Reproduction.** Turn the `R#` steps into a reliable, *representative* reproduction **before**
any hypothesizing. Subject to the representativeness gate (below): a "reproduction" that does not
demonstrably reproduce a named `S#` is not a reproduction and may not anchor the hunt. A genuinely
un-reproducible bug routes to **instrument-to-capture** — but that path carries its own evidentiary
bar (see the gate); "label it intermittent" is not an escape. The repro is a diagnostic artifact →
triage — and the triage routes it through guarded-change/lite, **which is where its cold red-team
happens** (this is the stage-1 red-team named in the charter below).
**Repro-ordering escape (an exception to the ordering above, recorded):** when a faithful repro
cannot be built blind (intermittent / load-dependent / emergent), hypotheses MAY be formed first
to inform repro/instrument design, PROVIDED the inversion is recorded in `decisions.md` **naming
the infeasibility class**, and every such hypothesis stays `ungated`; the representativeness gate
still binds the resulting repro/instrument before any conclusion — legal only recorded + tier-bound.

**2 — Observation ledger.** An **append-only** file recording everything examined: what was
checked, the observation, a citation (file:line / log row), and what it rules in or out. The
anti-thrash spine: **an area may not be re-examined without first recording why the prior finding
is insufficient.** This makes re-checking a deliberate, justified act rather than forgetful churn.

**3 — Hypotheses.** A ranked list of candidate root causes, each **falsifiable**: it names the
observation that would **confirm** it and the one that would **refute** it, and carries a status
(open / confirmed / refuted). No hypothesis is held without a discriminating test that could
distinguish it from its rivals. Each hypothesis also carries a **gate-coverage marker**, distinct
from that status: `ungated` → `test-passed` (its stage-4/5 discriminating test has run and been
cold-reviewed — which certifies the *test*, not yet the causal story) → `cold-red-teamed` (its
stage-7 causal chain has passed a cold pass). The marker records, as a fact rather than a memory,
what independent challenge has actually fired for this hypothesis; it gates **how the hypothesis may
be presented to the human** (see *The gate-before-present rule*), and the stage-7 **"confirmed"**
verdict requires `cold-red-teamed`.

**4 — Discriminating test.** Design a test or instrument that *splits* the live hypotheses (rules
at least one in or out). Before it is run it passes the **representativeness gate** and the
**diagnostic-artifact triage** — the triage's guarded-change/lite pass **is the stage-4 cold
red-team** (named in the charter below), challenging the test for representativeness and
confabulation before it runs.

**5 — Run & record.** Run the test; record the result in the observation ledger; update hypothesis
statuses; cite the evidence. A confirmed/refuted status is a claim — it cites the run that earned it.
Stage 4 already requires an artifact's triage to pass before it is *run*; the ordering rule extends
that to *consumption* — a result may not be consumed by a later stage (to eliminate a hypothesis,
advance the gate marker, or inform what the human is told) until the producing artifact's triage is
**recorded as passed** in `decisions.md`. Consuming a reading before its cold review is recorded is
the trust-before-gate slip; the triage is a precondition of trust, not a later audit.

**6 — Convergence gate.** Are we narrowing (eliminating hypotheses)? The **iteration cap** bounds
the hunt: after **N** cycles with no hypothesis eliminated, or **N** re-examinations of one area,
**stop and escalate to a human**. `N` has a **Layer-1 default of 3** and may be overridden by the
Layer-2 config; if no `N` is resolvable at all, Dragonfly **refuses to start** rather than run
without a convergence stop. A **cycle** = one discriminating test **run and recorded** — a
completed stage-4→5 lap; the cycle count and per-area re-examination tally are appended to
`decisions.md` at each stage-6 pass (cap countable from the log; an uncounted pass is a gate
violation). Multiple `S#` threads count convergence **per-thread** (same unit; a test
discriminating across threads increments each thread whose hypotheses it splits); a thread
hitting the cap **escalates alone**; threads may split into separate hunts at any gate with a
recorded reason — global counting may not mask per-thread thrash. Each pass also records which
mechanism **classes** the live hypotheses cover, which are ruled out, and **what assumption the
live set shares** (explicit "none identified" counts) — cold passes aim at the shared assumption
too, one found false ranks by impact; a pass missing this record is a **gate violation**, like an
uncounted cycle. The cap is the defense against token-burning thrash.

**7 — Root-cause confirmation.** "Found" requires **all three**, conjunctively (two-of-three is not
"found"):
1. **Reproduce-on-demand** — the symptom can be produced at will via the stage-1 repro.
2. **A cited causal chain** root → symptom — each link cites evidence (file:line / log row), not
   reasoning alone.
3. **A toggle** — flipping the suspected cause makes the symptom appear/disappear *predictably*.
   The toggle is what proves causality rather than correlation. For a rate-based/intermittent
   symptom the toggle criterion states the **expected rate shift and run count** up front
   (guarded-change's probabilistic rubric, by reference); a single flip does not satisfy it.
A **cold red-team** challenges the causal chain (is it confabulated? does it actually follow from
the cited evidence?). Passing it sets the hypothesis's gate marker to **`cold-red-teamed`** — a
precondition of the "confirmed" verdict *and* of presenting it to the human as the root cause (see
*The gate-before-present rule*). The toggle is a diagnostic artifact → triage.
**Depth check (root or relay?).** The root = the **deepest node the project can act on**. For the
claimed root, ask "why does this node produce the next?" ONE level down; "found" requires
recording that this why-down is (a) **answered** with cited evidence, (b) **explicitly out of
scope** (model property / third-party / not actionable — named), or (c) **not load-bearing** for a
fix targeting the cause, not the mechanism's surface. The stage-7 cold pass explicitly challenges
"**root or relay?**" — "explains the symptom" at a relay does not satisfy stage 7.
**Evidence-coverage sweep.** Before "found": every observation-ledger row tied to the `S#` is
either **explained by the confirmed chain** (cite how) or recorded as a **residual** (named
secondary contributor / open sub-hypothesis, ranked), carried in `diagnosis.md` + the stage-8
handoff, struck only with a recorded reason. "**Found (primary), with named residuals**" is legal;
**silent absorption is not** — an unexplained row without a residual entry blocks "found".
Only with the depth check and coverage sweep recorded is "found" declarable — all three bar items
+ both records + the chain's cold-red-team pass (gate marker `cold-red-teamed`), conjunctively.

**"Characterized, not found" — the only other legal terminal verdict.** A hunt may end short of
"found" ONLY as "characterized," requiring ALL of: (a) what IS established, each claim cited and
cold-red-teamed like any conclusion; (b) which hypotheses were refuted, with evidence; (c) WHY the
full bar is unreachable — a named reason (model property / cost bound / needs-live-data), not
vague; (d) **explicit human sign-off**; (e) presentation tier stays "characterization" — never
"the cause." Mitigation directions may ride the handoff **marked as such** (stage-9-verified on
symptom evidence only — no cause-resolution claim). Missing **any** of (a)–(e) → not a legal stop.

**8 — Handoff.** Emit the **diagnosis artifact**: root cause, the evidence and causal chain with
**each level's depth-check status**, the **named residuals**, the representative repro, and the
recommended fix. Hand to **guarded-change** for the fix. Dragonfly does **not** author the fix.

**9 — Fix verification.** Verify the **root cause is resolved**, not merely the symptom suppressed.
(For a **characterized** handoff there is no stage-7 chain+toggle to use: stage 9 verifies the
marked mitigations on **symptom evidence only** — no cause-resolution claim is made or verified.)

- **9a — Local** (if locally testable): using the stage-7 causal chain + toggle, check **both**
  (i) the diagnosed root-cause condition no longer holds, **and** (ii) the symptom is
  correspondingly gone.
  - **Cause gone + symptom gone** → genuinely resolved → proceed to 9b.
  - **Symptom gone but cause still present** → the fix **masked** the symptom (the diagnosed cause
    condition is empirically still active). This is a bad fix → record + back to **guarded-change**
    to produce a fix that addresses the cause.
  - **Symptom persists** → record `"fix F did not resolve S#"` as new evidence → back to **stage
    0**. The re-hunt reveals whether the **diagnosis** or the **implementation** was wrong;
    Dragonfly does **not** itself adjudicate the fix's *code fidelity* (that is guarded-change's
    domain) — it makes the empirical cause/symptom observations and routes on them.
- **9b — Live** (always, when not locally testable, and after a local pass): the **user** runs it
  live (the user is the final authority).
  - **User confirms resolved** → **done**.
  - **User says not resolved** → record + back to **stage 0** with the new information.

For a rate-based/intermittent symptom, 9a/9b define their **observation window up front** from the
symptom's observed ledger frequency (e.g. ~1/session over 5 sessions → 9b window ≥ 5 sessions,
pass = 0 occurrences); a single clean run or an unstated window does not satisfy them. Stage 9
also re-checks the **residuals list**: killing the primary does not close an unexplained residual.

A failed verification is never discarded: it is recorded as a new symptom so the next lap starts
from fact, not from scratch.

---

## The representativeness gate (mandatory, blocking, non-waivable)

No diagnostic artifact — **a stage-1 reproduction or a stage-4 discriminating test** — is trusted
until a **control run is shown to actually exhibit the symptom.** An artifact whose control does
not exhibit the symptom is rejected and redesigned. This is non-waivable: it is the single defense
against the founding failure (a test that doesn't test the thing).

**It applies to the stage-1 repro explicitly:** a "reproduction" that does not demonstrably
reproduce the named symptom (`S#`) is not a reproduction.

**The intermittent / instrument-to-capture path does not escape the gate; it satisfies it
differently.** A genuinely un-reproducible bug routes to instrument-to-capture, but the instrument
carries its own evidentiary bar: it must be **shown to capture the symptom on a run where the
symptom is known to have occurred** (replayed against a recorded failing trace, or validated to
fire on a forced/seeded instance of the condition) before any reading it produces is trusted. An
instrument never shown to capture an actual occurrence is treated exactly like a test whose control
did not exhibit the symptom: rejected and redesigned.

**The detector/readout is itself a diagnostic artifact.** Anything that *decides* "the symptom
occurred" (a classifier, a grep, a threshold rule) is a detector, subject to this gate and the
triage: BEFORE any reading it produces is consumed, it must be shown to **fire on a known-true
instance AND stay silent on a known-clean one**, evidenced by an observation-ledger row (the
silent-on-clean half is a deliberate, strictly stronger duty; an artifact that merely captures
data for later reading carries only the instrument-to-capture bar above). An unvalidated
detector's readings are untrusted — rejected like a control that doesn't exhibit the symptom.

---

## The gate-before-present rule (mandatory)

A hypothesis may be **formed and ranked freely** — the agent thinks out loud in its working notes
and keeps a ranked candidate list. What is gated is **how a hypothesis is presented to the human**,
and the gate has tiers matching what has actually been independently challenged:

- **`ungated`** (no cold pass yet): present it only as a **"candidate, ungated."** Never as the
  leading / likely / probable / most-likely cause, and never as a conclusion to act on.
- **`test-passed`** (its stage-4/5 discriminating test has run and been cold-reviewed): that cold
  pass certifies the **test artifact** — that it is representative and un-confabulated and ruled a
  rival in or out — **not** the hypothesis's causal story. So it may be presented as the
  **"leading / best-supported candidate so far,"** but must carry that its **causal chain has not
  yet been independently red-teamed** — it is not yet "the cause."
- **`cold-red-teamed`** (its stage-7 causal chain has passed a cold pass): only now may it be
  presented as **the root cause** ("confirmed" additionally needs the stage-7 three-part bar —
  reproduce-on-demand + cited chain + toggle).

**Rank is not endorsement.** Showing the ranked candidate list, and saying which is most *plausible
so far*, is allowed and expected. The forbidden move is calling an **ungated** hypothesis the cause,
or presenting any hypothesis as a **conclusion to act on** before its tier permits. The motivating
slip: a hypothesis was presented as the "leading" cause with no cold red-team, no repro, no
toggle — and the cold pass, when finally run, refuted it as dead code.

**Trust-before-gate ordering.** The same precedence governs artifacts. Stage 4 already requires the
triage (representativeness gate + cold review) to pass **before** an artifact is run; the ordering
rule makes it explicit and auditable that the artifact's output may not be **consumed by a later
stage** — to eliminate a hypothesis, advance a gate marker, or inform what the human is told —
until that triage is **recorded as passed** in `decisions.md`. Gate first, then consume; the triage
is a precondition of trust, not a later audit. (The motivating secondary slip: a search script's
output was consumed before its cold review was recorded.)

---

## Diagnostic-artifact triage (which guarded-change form)

Every repro / test / instrument / toggle / detector/readout Dragonfly produces runs through
guarded-change before it is trusted. The triage decides which form, **in priority order**:

1. **Consumes usage credits/tokens to run** (spawns an agent/CLI, hits an LLM API, otherwise burns
   budget) → **full guarded-change**, regardless of size. *(Highest-priority rule, overrides size.)*
   A wrong token-burning test is expensive twice — the wasted run *and* the false conclusion it
   feeds back into the hunt; in the motivating session, three of the six useless tests were of this
   kind.
2. Else **multi-file, mutates project state, or non-obvious correctness** → **full guarded-change.**
3. Else **single self-contained read-only script (~≤50 lines, no state)** → **guarded-change-lite.**
4. **In doubt → full.**

**guarded-change-lite** is defined **by reference**, not paraphrase, so it inherits guarded-change's
charter as that hardens: *a single cold red-team pass of the artifact — using guarded-change's
unchanged stage-3/6 reviewer charter (four lenses + evidence discipline) — against a one-line intent
+ a checkable "does exactly X and exercises path P" criterion → fix → run.* It keeps that charter
verbatim and drops the surrounding scaffolding (spec / criteria / plan / baseline / regression) —
the review without the full doc set. Full cases invoke the guarded-change skill directly. Lite
carries a pointer back to guarded-change as the source of truth for the charter. **The provenance
record is not scaffolding** — lite keeps the charter AND the provenance record (charter section
below), dropping only the five-item doc set above. A lite pass records, minimally: the artifact,
the one-line intent + criterion, the verdict, and where the verbatim output lives, in
`decisions.md`; unrecorded = treated as not having happened (artifact untrusted).

---

## The ledgers (append-only, persisted to files)

Two ledgers hold the anti-amnesia state. **Both are written to files** in the run's working folder
(the Layer-2 config names the location), **not** held only in conversation context.

- **Symptom ledger** — the frozen, numbered symptom set (`S#`) + repro steps (`R#`), with the
  user's original wording and the confirmed restatement. Frozen; symptoms struck only with a
  recorded reason.
- **Observation ledger** — append-only record of everything examined (what / observation / citation
  / rules-in-or-out), enforcing the no-re-examination-without-justification rule.

File persistence is load-bearing: the **cold-start guard** (below) *recommends restarting the
session*, which would destroy any in-context ledger — so the ledgers must survive a restart on disk
for the carry-over to be real.

---

## The red-team charter (stages 1, 4, 7)

Diagnostic artifacts and the final causal chain are challenged by a **cold, independent reviewer** —
a subagent with no shared context, given the artifact under review **and** the underlying source
named in the Layer-2 `redteam_context`. **Where each red-team happens:** at **stage 7** the causal
chain is red-teamed *directly* (a cold reviewer spawned here); at **stages 1 and 4** the diagnostic
artifact (repro / discriminating test) is red-teamed *via the triage* — the guarded-change or
guarded-change-lite pass each artifact is routed through *is* its cold review. So all three points
carry a cold pass; stage 7's is explicit, stages 1/4's is the triage's. This reuses guarded-change's charter (the four lenses +
evidence discipline; see `guarded-change/METHODOLOGY.md` "The red-team charter") — Dragonfly does
not fork it. The diagnosis-specific aiming:

- **Does the test reproduce the named symptom (`S#`), or a neighbor?** (the representativeness
  challenge — the #1 failure)
- **Are any identifiers, paths, or calls confabulated?** (the variable-that-doesn't-exist failure)
- **Does the causal chain actually follow from the cited evidence**, or is it asserted? (stage 7)
- **Root or relay — is the claimed root the deepest node the project can act on?** (stage 7)
- **What assumption does the live hypothesis set share, and is it true?** (aimed at the set)

**Provenance (inherited, unconditional).** Guarded-change's provenance rule applies to **every
dragonfly cold pass** — direct stage-7 AND the triage's guarded-change/lite passes at stages 1/4:
the record carries the verbatim charter, the exact context list, the reviewer's verbatim output,
the agent type + model, and the reviewer-reported context hashes; it lives in, or is pointed to
from, the hunt folder (a full-GC triage run keeps its own `changes/<slug>/` record, nested or
external, with a pointer in the hunt's `decisions.md`). Missing any element = the pass is
**un-run** — its reading may not be consumed. Cold passes inherit ALL of guarded-change's
**unconditional** discipline bullets (those with no stage or trigger scope of their own),
provenance included. The stage-3 coverage-challenge bullet does NOT apply to dragonfly's **direct
stage-7 and lite passes** (neither is a stage-3 review; the analog is the shared-assumption aim
above) — but a **full guarded-change triage run keeps ALL of guarded-change's own stage duties,
including its stage-3 coverage challenge**: dragonfly narrows nothing inside a full-GC run.

The four lenses (factual / logical / missed-opportunity / unstated-assumptions), the
"cite-or-it-doesn't-count" rule, the "a clean factual lens must be earned with citations" rule, and
"spot-verify the citations themselves" all apply unchanged. Reviewers are graded on **precision**.

---

## Severity model and gate routing

Identical to guarded-change (see its METHODOLOGY). Worst finding routes the gate: **blocker** (wrong
problem / unverifiable), **major** (sound goal, wrong approach), **minor** (local, fixable in
place), **nitpick** (style). The **iteration cap** (stage 6, and the same anti-livelock rule on any
review gate) stops thrash: after 2 bounces at the same gate on the same finding class, a human
breaks the tie.

---

## The two layers

- **Layer 1 — agnostic core (this doc + the skill).** The loop, the ledgers, the gates, the
  representativeness gate, the triage, the red-team charter (referenced from guarded-change), the
  severity model, the default `N`. Ships once; knows nothing about any specific project.
- **Layer 2 — per-project config.** Where the code lives, how to run/reproduce, where logs land,
  where the ledgers are written, the iteration-cap `N` (overriding the default), and the
  priority-ordered `redteam_context`. Supplied per repo.

---

## The config contract (Layer 2)

```yaml
project: <name>

redteam_context:          # paths the cold reviewer MUST read to check claims vs. source.
                          # PRIORITY ORDER — first entries are entrypoints; each may carry a
                          # "what to check here first" note. A cold subagent can't read a large
                          # tree exhaustively, so order matters.
  - path: <most-relevant-source>
    note: <what to check here first>

reproduction:             # how to run / reproduce in this project
  how: <command(s) or manual procedure to exercise the suspect behavior>
  logs: <where the app's own logs/telemetry land — ground truth for observations>

ledgers:
  dir: <where the symptom + observation ledgers are written for a run>

iteration_cap:
  N: <integer>            # OPTIONAL — overrides the Layer-1 default of 3
```

Rules:
- **`redteam_context` is priority-ordered** — most relevant entrypoints first, with a note on what
  to check there, so independence doesn't degrade into "skimmed whatever fit in context."
- **`N` defaults to 3** if omitted; if no `N` is resolvable at all the loop refuses to start.
- **Ledgers are files** under `ledgers.dir`; they must survive a session restart.
- **Path validation at hunt start:** every config path (`redteam_context` entries,
  `reproduction.logs`, `ledgers.dir`) is mechanically checked to exist/be readable BEFORE stage 0
  proceeds — no hunt on unvalidated paths. Invalid-but-adaptable → adapt + record it as its own
  `decisions.md` entry (what changed, why) + proceed; dead/unresolvable → **stop for the human**.

---

## What a run produces (artifacts)

One folder per hunt, e.g. `hunts/<slug>/`:

```
symptom-ledger.md     frozen numbered symptoms (S#) + repro steps (R#), original + restatement
observation-ledger.md append-only record of everything examined (what/observation/citation/rules)
hypotheses.md         ranked falsifiable hypotheses: confirm/refute prediction, status
                      (open/confirmed/refuted), + gate marker (ungated/test-passed/cold-red-teamed)
diagnosis.md          (stage 8) root cause, causal chain (per-level depth-check status), evidence,
                      repro, recommended fix, named residuals; characterized: (a)–(c) instead
decisions.md          append-only gate log (gates, severities, routes, human overrides, cap counts)
```

`decisions.md` is the gate log and the iteration-cap's memory (counting bounces, carrying prior
findings forward), and the audit trail for reconstructing the hunt if context is lost.

---

## Cold-start guard

If invoked inside an already-long or visibly thrashing session, Dragonfly first **recommends
starting a fresh session** and emits a short carry-over brief so prior context loss/thrash can't
poison the hunt. The brief carries the **full anti-amnesia state**: the frozen symptom ledger
(`S#`/`R#`), the observation ledger to date, the current `hypotheses.md`, and `decisions.md` (the
iteration-cap's bounce-count + prior findings) — because the observation ledger and the gate log are
exactly the thrash-prevention and convergence state a restart would otherwise destroy. (All four are
files under `ledgers.dir`/the hunt folder, so the brief is pointers to them, not a re-transcription.)

---

## Trigger

- `/dragonfly` — explicit invocation.
- **Proactive suggestion:** when a **diagnosis-shaped** request appears — a reported bug, wrong
  output, or unintended behavior that someone wants *explained or tracked down* — suggest Dragonfly
  (do not auto-run). **Precision bar:** do not fire on every error string, stack-trace paste, or
  build failure the user is merely reporting or already knows the cause of; the signal is
  "something is behaving wrong and we don't yet know why," not "an error appeared."

---

## Human-in-the-loop

The skill executes the hunt autonomously (translate, freeze, reproduce, hypothesize, design+run
discriminating tests, spawn cold reviewers, maintain the ledgers) and **stops for a human** at:
- the **0a confirmation checkpoint** (the symptom restatement must be confirmed),
- any **blocker** about to restart the loop,
- the **convergence gate** firing (iteration cap reached),
- a **characterized-verdict ending** (its explicit human sign-off — requirement (d)),
- **stage 9b live verification** (the user is the final authority on "resolved"),
- **missing config** needed to proceed (it refuses rather than guesses),
- **dead/unresolvable config paths** at hunt start (≠ missing config; adaptable ones proceed).

It also **never presents an ungated hypothesis to the human as the likely/leading cause**: a
hypothesis is "candidate, ungated" until a cold pass is recorded for it, a "leading candidate" only
once its discriminating test is cold-reviewed (`test-passed`), and "the root cause" only once its
stage-7 causal chain is `cold-red-teamed` (see *The gate-before-present rule*). Ranking the
candidate list is always fine.
