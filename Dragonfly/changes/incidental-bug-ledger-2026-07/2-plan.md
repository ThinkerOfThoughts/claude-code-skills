# 2 — Plan: the incidental-bug ledger (Theme 3)

Additive change, four touched files. Exact insertions below (the build is mechanical; the stage-3
red-team reviews this actual text). **Only additions** — no existing line edited/reordered (T3).

## §A — Touched files + exact insertions

### 1. `SKILL.md` (always-loaded → the concise always-in-view discipline)
- **In the Loop intro** (the "maintain the ledgers as files" sentence): add `incidental-ledger.md` to
  the parenthetical list → "… `hypotheses.md`; `diagnosis.md` at stage 8; **`incidental-ledger.md`
  (out-of-scope findings, throughout)**; `decisions.md` throughout".
- **In the cold-start guard** (SKILL:22-27): add `incidental-ledger.md` to the carry-over-brief file
  list, so a restarted session is pointed at the parked findings too (round-1 nitpick).
- **Add a concise discipline note** — placed **after the representativeness/triage/iteration-cap
  paragraph** (after the line ending "…escalate to a human.", SKILL.md:57), immediately before
  `## Stop-for-human`, so the flagship "most important gate" paragraph stays adjacent to the loop table
  (round-1 MAJOR fix — the earlier "after the loop table" anchor would have buried it):
  > **Incidental findings.** If at any stage you notice a potential bug **unrelated to the frozen `S#`
  > set**, **park it in `incidental-ledger.md`** (what / where / why it looks suspect) and **move on —
  > do not chase it.** **When in doubt whether a finding bears on the `S#` set, treat it as in-scope**
  > (record it in the observation ledger and let the stage-7 coverage sweep adjudicate) — park **only
  > clearly-unrelated** findings, so focus protection never silently drops a real contributor. The
  > hunt's focus and convergence budget stay on the `S#`; parked findings are surfaced at stage 8 as a
  > parking lot for future, separately-scoped hunts. Logging to the parking lot never blocks a gate and
  > is never part of convergence-cap accounting.

### 2. `stages/stage-2.md` (observation ledger — the recording mechanics)
- **Add to the Procedure** (new bullet):
  > - **Incidental findings go to a *separate* ledger.** If while examining you notice a potential bug
  >   **clearly unrelated to the `S#` set**, record it in `incidental-ledger.md` (append-only: what /
  >   where file:line-or-component / why suspect) — **not** in the observation ledger (which is for
  >   things examined *about the current symptom*) — and **do not investigate it** (log-and-move-on;
  >   focus protection). **When in doubt whether it bears on the `S#` set, treat it as in-scope** —
  >   record it in the observation ledger and let the stage-7 coverage sweep adjudicate; park only
  >   clearly-unrelated findings, so a real contributor is never silently lost. It is out of scope of
  >   this hunt and carried to the stage-8 parking lot.

### 3. `stages/stage-8.md` (handoff — surface the parking lot on ANY exit)
- **Add to the Procedure** (new bullet, worded to fire on **either** terminal verdict — round-1 fix;
  the earlier draft was wired only to the diagnosis.md path and a *characterized* ending could drop it.
  Round-2 fix: the skill has exactly two legal endings, not three):
  > - **Surface the incidental-bug ledger as a parking lot — on either terminal verdict** (a "found"
  >   `diagnosis.md` **or** a "characterized, not found" handoff). If `incidental-ledger.md` is
  >   non-empty, the handoff lists it as **out-of-scope findings for future, separately-scoped
  >   investigation** — kept **distinct** from the diagnosed root cause and its named residuals (which
  >   are `S#`-related by definition). It is surfaced, **not** routed to guarded-change (each incidental
  >   bug is a future hunt of its own, if pursued). *(If a hunt halts mid-loop at the convergence-cap
  >   stop-for-human without reaching stage 8, the parked findings are on disk + in the cold-start
  >   carry-over brief — not lost.)*

### 4. `METHODOLOGY.md` (artifacts list + config)
- **"What a run produces"** — add a line to the artifact block:
  > `incidental-ledger.md   append-only parking lot of potential bugs noticed but UNRELATED to the S#`
  > `                       set — logged and not chased; surfaced at stage 8 for future hunts`
- **Config `ledgers.dir` note** — extend: "… where the symptom + observation **+ incidental** ledgers
  are written for a run."

**Final touched-file set (frozen at gate 4):** exactly `SKILL.md`, `stages/stage-2.md`,
`stages/stage-8.md`, `METHODOLOGY.md`. New runtime artifact: `incidental-ledger.md` (created per hunt,
not a repo file). No stage-file other than 2 and 8 changes; no charter change; no guarded-change change.

## §B — Measurement

- **T1 (feature fires — BOTH directions; round-1 fix)** — cold behavioral arm: agent given amended
  `SKILL.md` + `stage-2.md` at stage 2 of a stale-dashboard hunt; scenario presents **two** findings:
  (i) an obvious **unrelated** bug (an unauthenticated admin endpoint in a *different* module), and
  (ii) an **in-scope** observation (the dashboard query has no cache-TTL check — plausibly bears on the
  stale-data `S#`). FIRED = the agent logs (i) to `incidental-ledger.md` and does **not** chase it,
  **AND** records (ii) in the `observation-ledger.md` (not the parking lot). This verifies the boundary
  in both directions — the round-1 gap where an in-scope finding could be mis-routed to the parking lot.
- **T2 (stage-8 surfacing — any exit; round-1 fix)** — **two** cold arms at stage 8 given amended
  `stage-8.md` + a populated `incidental-ledger.md`: (a) a normal **"found"** handoff, (b) a
  **"characterized, not found"** ending (no full diagnosis.md). FIRED (both) = the handoff surfaces the
  parking lot, distinct from residuals — including on the characterized exit.
- **T4 (no regression)** — re-run the restructure's SC-1 (representativeness gate, stage 1) + SC-2
  (gate-before-present, stage 3) arms against the amended files; both must still FIRE.
- **T3 (additive-only)** — `git diff` of the 4 files shows only insertions; stage-6 reviewer confirms
  no existing rule reworded/reordered/diluted (position lens on each insertion's neighbours).
- **T5 (load budget)** — `wc -l` per stage load; touched stages (2, 8) + SKILL only; all ≤ ~270.
- **T6 (live==source)** — `diff -r ~/.claude/skills/dragonfly/` clean.
- **T7 (consistency)** — sweep: name + "log-and-move-on / don't chase / parking lot / out-of-scope of
  S#" semantics agree across SKILL / stage-2 / stage-8 / METHODOLOGY.
- **T8 (never blocks)** — inspection (the wording) + T1 arm (b).

**Instrumentation:** none new — grep/`wc`/`diff`/inspection + **5 cold arms** (T1, T2-found,
T2-characterized, + re-run SC-1/SC-2). **The arm model is recorded in `decisions.md` with each
FIRED/DID-NOT-FIRE grade** (round-1 nitpick — outcomes can be model-dependent). **Estimate:** ~180–280K tokens.

## Severity → routing
Standard: blocker → stage 1; major → stage 2; minor → fix in place; nitpick → log. Route on reviewer's
severity. **Gating:** T1–T8 (T5 arguably advisory, but kept gating — the restructure just bought the
budget headroom and it must not be given back silently). Path validation (gate-4 precondition): the
reviewer's context paths (amended files + `1-spec`/`1.5-criteria`/`2-plan`) validated + recorded.
