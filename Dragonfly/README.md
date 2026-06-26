# Dragonfly — a process for AI-assisted bug hunting

Dragonfly is a small, reusable process — and a Claude Code skill that runs it — for **tracking down
bugs** without the failure modes that turn debugging into token-burning thrash. It is the sibling of
[guarded-change](../Guarded_change/): guarded-change is the gated loop for *making* a change;
Dragonfly is the gated loop for *finding* the bug a change will fix. They compose.

If you only read one section, read **"The five failures it guards against"** — the rest is how.

---

## TL;DR

- **What:** a gated diagnosis loop — `translate → reproduce → observe → hypothesize → discriminate →
  converge → confirm → hand off → verify` — with two hard rules borrowed from guarded-change and one
  of its own:
  1. **Nothing self-certifies.** No diagnostic test, instrument, or causal chain is trusted on the
     say-so of the agent that wrote it; an **independent cold reviewer** challenges it.
  2. **"Found" is proven, not declared.** A root cause counts as found only with **reproduce-on-
     demand + a cited causal chain + a working toggle** — all three.
  3. **(Dragonfly's own) A representative test, or no test.** A test is untrusted until a *control
     run is shown to actually exhibit the symptom.* This is the single defense against the failure
     that motivated the whole skill.
- **Why:** the most expensive AI-assisted debugging mistakes aren't wrong code — they're *tests
  that didn't test the thing*, *thrashing that forgot what it already checked*, and *"fixes" that
  masked a symptom while the cause survived*. This loop is built specifically against those.
- **How to use it three ways:**
  1. As a **Claude Code skill** you invoke (`/dragonfly`) — it runs the loop, spawns the cold
     reviewers, and maintains the ledgers for you.
  2. As a **checklist** applied by hand to any bug hunt.
  3. As a **mindset**: *"Did my test's control actually exhibit the symptom? What toggle proves I
     found the cause and not a correlation?"*

---

## The five failures it guards against

These are real patterns from a single debugging session that wasted ~1.5 sessions of usage on one
relatively simple bug. They're easy to fall into and hard to see from the inside.

1. **The non-representative test.** Six times, a test was written that didn't actually produce the
   conditions it claimed to test — and conclusions were drawn from it. The fix is structural: a
   **blocking, non-waivable representativeness gate** — a test is rejected until a *control* is
   shown to exhibit the symptom. (Three of those six tests also called an agent/LLM, *burning
   tokens* to produce a worthless result — so any token-consuming test gets the full guarded-change
   treatment, see triage.)
2. **Thrashing.** The same areas re-checked over and over, prior findings forgotten. The fix: an
   **append-only observation ledger** — you may not re-examine an area without first recording why
   the prior finding was insufficient.
3. **Symptom amnesia.** Symptoms quietly forgotten mid-hunt. The fix: a **frozen, numbered symptom
   ledger** captured up front (and a translation step that restates the user's report precisely and
   gets it confirmed, so you don't hunt a misread symptom).
4. **Confabulation.** Diagnostic code referencing variables that don't exist, misplaced calls. The
   fix: a **cold red-team of every diagnostic artifact** before it runs, citing the real source.
5. **No convergence.** Tokens spent without narrowing the cause. The fix: a **convergence gate with
   an iteration cap** — after N non-narrowing cycles it stops and asks a human.

---

## The loop

```
0  CAPTURE      0a translate the report → numbered symptoms S# (+ repro steps R#), CONFIRM with user
                0b freeze them into the symptom ledger (a file)
1  REPRODUCE    build a REPRESENTATIVE repro before hypothesizing  ← the representativeness gate
2  OBSERVE      append-only ledger of everything examined; no re-checking without recorded reason
3  HYPOTHESIZE  ranked, falsifiable (each names what would confirm AND refute it)
4  DISCRIMINATE design a test that splits the hypotheses  ← gate + triage BEFORE running
5  RUN & RECORD run it; log the result; update statuses; cite evidence
6  CONVERGE     narrowing? iteration cap (N, default 3) → stop for a human
7  CONFIRM      "found" = reproduce-on-demand + cited causal chain + a working TOGGLE (all three)
8  HAND OFF     diagnosis → guarded-change makes the fix
9  VERIFY       is the ROOT CAUSE resolved (not just the symptom masked)? local + live → done
```

A few deliberate design choices worth knowing:

- **Causality runs cause → symptom, never the reverse.** Stage 9 verifies the *cause* is gone, not
  just that the symptom vanished — a fix that masks a symptom while the cause survives is a bad fix,
  not a done one.
- **Diagnostic artifacts are code, so they get guarded-change too.** Every repro/test/instrument is
  triaged: token-consuming or stateful/complex ones go through the **full** guarded-change loop;
  trivial read-only scripts get a **lite** single-cold-review pass. Nothing the hunt produces
  self-certifies.
- **Dragonfly diagnoses; guarded-change fixes.** Dragonfly stops at a confirmed root cause and hands
  off, then verifies the result. It does not author the fix.
- **The ledgers are files, not chat history.** Because the cold-start guard may recommend a fresh
  session, the anti-amnesia state has to survive a restart on disk.

---

## How it's structured (two layers)

- **Layer 1 — the agnostic core.** The loop, the representativeness gate, the triage, the ledgers,
  the reviewer charter (reused from guarded-change), the severity model, the default cap. Knows
  nothing about any specific project. This is `METHODOLOGY.md` (the spec) + `SKILL.md` (what Claude
  Code executes).
- **Layer 2 — a per-project config.** Where the code lives, how to reproduce, where the logs/ledgers
  land, the cap `N`, and the priority-ordered `redteam_context`. One small file per repo
  (`dragonfly.companion.md` is a worked example).

---

## Adopting it

1. **Drop the skill in.** Copy this `Dragonfly/` folder's `METHODOLOGY.md` + `SKILL.md` into
   `~/.claude/skills/dragonfly/`. Claude Code will then offer `dragonfly` as a skill. Install
   **guarded-change** too — Dragonfly routes diagnostic artifacts to it.
2. **Write a Layer-2 config** for your checkout. Copy `dragonfly.companion.md` and adjust the paths,
   reproduction commands, and `redteam_context`. The contract is at the bottom of `METHODOLOGY.md`.
3. **Invoke it on a bug.** `/dragonfly` (or mention a bug with an unknown cause and let it suggest
   itself). It creates a `hunts/<slug>/` folder, walks the stages, spawns the cold reviewers, keeps
   the ledgers, and stops to ask you only at the genuinely-yours decisions (confirming the symptom
   restatement, a blocker about to restart, the cap firing, and the live "is it fixed?" check).

You don't *need* the skill — the loop works as a manual checklist. But since the same tool you
already use can run it, the cheapest version is to let it.

---

## Relationship to guarded-change

| | guarded-change | Dragonfly |
|---|---|---|
| Job | *make* a change correctly | *find* the bug correctly |
| "Done" bar | conformance to criteria set before building | root cause reproduced + caused + toggled |
| Hands off to | — | guarded-change (for the fix) |
| Shared machinery | cold-subagent red-team, four-lens charter, evidence discipline, severity model, iteration cap, two-layer config | (all reused — not forked) |

A bug hunt with a fix is the two composed: **Dragonfly finds it → guarded-change fixes it →
Dragonfly verifies the cause is gone.**

---

## Files

| File | What it is | Audience |
|---|---|---|
| `METHODOLOGY.md` | The authoritative spec — loop, representativeness gate, triage, ledgers, reviewer charter, config contract | the skill / a careful reader |
| `SKILL.md` | The operating procedure Claude Code executes | the agent |
| `dragonfly.companion.md` | The companion-emergence Layer-2 config (worked example/template) | you |
| `this file` | Why it exists and how to adopt it | you |

Questions worth carrying into any bug hunt, even if you never run the skill: *Did my test's control
actually exhibit the symptom? What toggle proves I found the cause, not a correlation? And did the
fix remove the cause — or just hide the symptom?*
