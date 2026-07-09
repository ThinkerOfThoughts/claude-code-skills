# Dragonfly — methodology

A gated loop for **diagnosing** bugs, where **no diagnostic conclusion reaches "accepted" without an
independent challenge**, and where **"found the bug" is proven by reproduce-on-demand + a causal
toggle** — not declared by the thing that produced it.

This document is the **orientation/reference spec**: why the loop exists, the loop diagram, the two
layers, the config contract, and what a run produces. The **per-stage procedure and the rules that
govern each stage now live in `stages/`** (one file per stage, plus the shared red-team charter
`stages/charter.md`); `SKILL.md` is the router that walks the loop and points at those files. This file
is opened for orientation and config setup — not to run a stage.

Dragonfly is the sibling of **guarded-change**: guarded-change is the gated loop for *making* a change;
Dragonfly is the gated loop for *finding* the bug that a change will fix. They compose — Dragonfly
hands a confirmed diagnosis to guarded-change, which makes the fix, and Dragonfly then verifies the fix
resolved the root cause. The name: the dragonfly is the most effective hunter of insects (bugs) there
is. It is deliberately **project- and domain-agnostic** — nothing here assumes a particular language,
app, or bug.

---

## Why this exists

AI-assisted debugging has a characteristic, expensive failure mode (~1.5 sessions wasted on one simple
bug was the motivating case). Each failure maps to a structural defense Dragonfly builds in:

1. **Non-representative tests.** A test written that did not actually produce the conditions it claimed
   to test — conclusions drawn from tests that tested nothing. → the **representativeness gate** +
   **diagnostic-artifact triage** (stages 1/4).
2. **Thrashing.** The same areas re-checked repeatedly; prior findings ignored. → the **append-only
   observation ledger** (stage 2).
3. **Symptom amnesia.** Symptoms selectively forgotten mid-hunt. → the **frozen symptom ledger**
   (stages 0a/0b).
4. **Confabulation.** Diagnostic code referencing variables that didn't exist. → the **cold red-team of
   every diagnostic artifact** before it runs (the charter, stages 1/4/7).
5. **No convergence.** Tokens spent without narrowing the cause. → the **convergence gate + iteration
   cap** (stage 6).

Every diagnostic artifact is challenged by an **independent** reviewer, the full symptom set and
everything examined live in **append-only ledgers**, and "found" is a **falsifiable, executed bar** —
not an assertion.

---

## The loop

```
0a   TRANSLATION      restate symptoms as S1,S2,…; repro steps as R1,R2,…; CONFIRM with the user
0b   FREEZE           record original + confirmed restatement into the append-only SYMPTOM LEDGER
1    REPRODUCTION     a reliable, REPRESENTATIVE repro BEFORE hypothesizing (repro artifact → triage)
2    OBSERVATION      append-only OBSERVATION LEDGER: everything examined + citation + rules-in/out
3    HYPOTHESES       ranked, each FALSIFIABLE (confirm + refute prediction); + a gate marker
4    DISCRIMINATING   a test that splits the live hypotheses → representativeness gate + triage first
     TEST (gated)
5    RUN & RECORD     run; log result; update statuses; cite. Consume only once triage recorded passed
6    CONVERGENCE      narrowing? ITERATION CAP (N, default 3): N cycles, no elimination → escalate
     GATE
7    ROOT-CAUSE       "found" = reproduce-on-demand + cited causal chain + a TOGGLE, cold-red-teamed
     CONFIRMATION
8    HANDOFF          emit DIAGNOSIS ARTIFACT → guarded-change makes the fix → returns
9    FIX VERIFICATION verify the ROOT CAUSE is resolved (not merely the symptom suppressed)
```

The **most important gate is the representativeness gate** (governs stages 1 and 4) — the cheapest
place to kill the failure that wasted the motivating session: a test that doesn't test the thing.
Everything downstream of a non-representative test is wasted, so the gate sits upstream of all
conclusions. The operative rules (representativeness gate, triage, charter, gate-before-present,
severity model) live written-in-full in the stage files that enforce them, not here.

---

## Stage index — where each stage's detail lives

| Stage | File | What it covers |
|---|---|---|
| 0a — Translation | `stages/stage-0a.md` | restate as S#/R#; confirm with the user |
| 0b — Freeze | `stages/stage-0b.md` | write the confirmed set into the frozen symptom ledger |
| 1 — Reproduction | `stages/stage-1.md` + `stages/charter.md` | representative repro; representativeness gate; triage |
| 2 — Observation | `stages/stage-2.md` | append-only observation ledger; no-re-exam-without-reason |
| 3 — Hypotheses | `stages/stage-3.md` | ranked/falsifiable; gate marker; the gate-before-present rule |
| 4 — Discriminating test | `stages/stage-4.md` + `stages/charter.md` | splits hypotheses; rep gate; triage; trust-before-gate |
| 5 — Run & record | `stages/stage-5.md` | log/update/cite; consume only after triage recorded |
| 6 — Convergence gate | `stages/stage-6.md` | iteration cap; per-thread counting; shared-assumption record |
| 7 — Root-cause | `stages/stage-7.md` + `stages/charter.md` | three-part bar; depth check; coverage sweep; characterized |
| 8 — Handoff | `stages/stage-8.md` | emit diagnosis.md; hand the fix to guarded-change |
| 9 — Fix verification | `stages/stage-9.md` | root cause resolved (not masked); 9a/9b; residuals re-check |

The **red-team charter** (five lenses + discipline + provenance + diagnosis aiming + severity model) is
dragonfly's **own**, in `stages/charter.md`, shared by stages 1/4/7. It was forked from guarded-change's
charter (unconditional core) as an authoring reference and is now self-contained — there is no live
cross-reference to guarded-change's text.

---

## The two layers

- **Layer 1 — agnostic core (this doc + the skill + the stage files).** The loop, the ledgers, the
  gates, the representativeness gate, the triage, the red-team charter (dragonfly's own,
  `stages/charter.md`), the severity model, the default `N`. Ships once; knows nothing about any
  specific project.
- **Layer 2 — per-project config.** Where the code lives, how to run/reproduce, where logs land, where
  the ledgers are written, the iteration-cap `N`, and the priority-ordered `redteam_context`. Per repo.

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
  dir: <where the symptom + observation + incidental ledgers are written for a run>

iteration_cap:
  N: <integer>            # OPTIONAL — overrides the Layer-1 default of 3
```

Rules:
- **`redteam_context` is priority-ordered** — most relevant entrypoints first, with a note on what to
  check there, so independence doesn't degrade into "skimmed whatever fit in context."
- **`N` defaults to 3** if omitted; if no `N` is resolvable at all the loop refuses to start.
- **Ledgers are files** under `ledgers.dir`; they must survive a session restart (the cold-start guard
  recommends restarting, which would destroy any in-context ledger).
- **Path validation at hunt start:** every config path is mechanically checked to exist/be readable
  BEFORE stage 0 proceeds. Invalid-but-adaptable → adapt + record + proceed; dead/unresolvable → stop
  for the human. (Operative form in `SKILL.md` Inputs + the stage files.)

---

## What a run produces (artifacts)

One folder per hunt, e.g. `hunts/<slug>/`:

```
symptom-ledger.md     frozen numbered symptoms (S#) + repro steps (R#), original + restatement
observation-ledger.md append-only record of everything examined (what/observation/citation/rules)
hypotheses.md         ranked falsifiable hypotheses: confirm/refute prediction, status, + gate marker
diagnosis.md          (stage 8) root cause, causal chain (per-level depth-check), evidence, repro,
                      recommended fix, named residuals; characterized: (a)–(c) instead
incidental-ledger.md  append-only parking lot of potential bugs noticed but UNRELATED to the S# set —
                      logged and not chased; surfaced at stage 8 for future, separately-scoped hunts
decisions.md          append-only gate log (gates, severities, routes, human overrides, cap counts)
```

`decisions.md` is the gate log and the iteration-cap's memory, and the audit trail for reconstructing
the hunt if context is lost.

---

## Trigger

- `/dragonfly` — explicit invocation.
- **Proactive suggestion:** when a **diagnosis-shaped** request appears — a reported bug, wrong output,
  or unintended behavior that someone wants *explained or tracked down* — suggest Dragonfly (do not
  auto-run). **Precision bar:** do not fire on every error string, stack-trace paste, or build failure
  the user is merely reporting or already knows the cause of; the signal is "something is behaving
  wrong and we don't yet know why," not "an error appeared."

---

## Human-in-the-loop

The skill executes the hunt autonomously (translate, freeze, reproduce, hypothesize, design + run
discriminating tests, spawn cold reviewers, maintain the ledgers) and **stops for a human** at: the
**0a confirmation checkpoint**; any **blocker** about to restart the loop; the **convergence gate**
firing; a **characterized-verdict ending** (its explicit sign-off); **stage-9b live verification**;
**missing config**; and **dead/unresolvable config paths** at hunt start. It also **never presents an
ungated hypothesis as the likely/leading cause** (see `stages/stage-3.md` "the gate-before-present
rule"). The full stop conditions live in `SKILL.md` and the relevant stage files.
