# Context-bloat hunt — resume here (TOMORROW's priority)

> **STEP 0 — DONE (2026-07-02 eve): branch caught up to main** (merge commit `a50016d`; origin/main
> was a FORCED update = public-sync scrub). Merge was clean. **Relevant changes that landed — several
> touch THIS hunt's entry points, so re-verify before trusting the pre-merge observations:**
>
> - **Budget/compaction path REWRITTEN** (`brain/chat/budget.py`, commits `3471beb` "T3" + `f8e5ecf`):
>   `apply_budget` now delegates to the persisted `compact_conversation()` and **removed the old
>   per-turn `provider.generate()` summarise path "that busted prompt caching every turn"** — that
>   removed path was itself a per-turn cost/bloat source, so part of the bloat story may already be
>   addressed. engine.py also **removed `_HISTORY_WINDOW_MSGS`** (per-turn history windowing). The
>   engine cap is **still `apply_budget(max_tokens=80_000)`** (engine.py:240) — so the 80K observations
>   hold, but *when/how compaction fires* has changed → **re-verify NEW-8 / S1-O21 compaction findings
>   against the merged code before relying on them.**
> - **Provider streaming fix** (`brain/bridge/provider.py`, `9830b1d`, tagged "bug-hunt finding #2"):
>   the result frame now terminates the stream so a slow EOF can't fire a **spurious idle-timeout that
>   discards an already-good reply**. Idle-timeout still **60s per-event + 120s first-event**
>   (`_STREAM_FIRST_EVENT_SECONDS`, provider.py:200). → **PARTIAL** mitigation of git issue **#55**
>   (kills the after-good-reply failure mode; the mid-generation 60s severing of a genuinely slow heavy
>   turn still stands). **⚠️ Hana is actively bug-hunting the provider/streaming area** ("bug-hunt
>   finding #2") — coordinate before touching provider.py / the idle-timeout.
> - **Harness intact:** `build_app` signature UNCHANGED → `setup_probe.py`/`run_anchor.py` still valid.
>   But provider.py / server.py / tool_loop.py internals moved (incl. `bb47fac` recruit-on-reach
>   double-stream fix) → **re-run the harness smoke first to confirm it still drives cleanly**, and
>   re-check the `brain/` line numbers cited below (they may have shifted).
> - S2-adjacent (deferred): `brain/felt_time/*`, `brain/forgetting/salience.py` changed too.
>
> After digesting the above: `uv sync` if deps changed, confirm the app runs, THEN start the hunt.


**Stays in the git repo** (this is the main thread now). The monologue-bleed follow-up is parked in a
standalone note at `~/Desktop/hunts/monologue-bleed/BLEED-RESUME.md` (independent of git). The provider
idle-timeout is a separate git issue.

## The question
**What causes context load to accumulate so massively on what should be a simple task — e.g. editing a
short file?** A short-file edit should need little context, yet the system bloats to the point of
severe slowdown (100-275s turns, provider idle-timeouts). Pin down the SOURCE(S) of the bloat.
Priority on the 0.0.38 file read/write path, **but bloat in general** — a plain no-file-edit reply was
also several × slower (user, 2026-07-02 morning), so it is not only the file tools.

## Why this is the right thing to chase first
Isolating whether the monologue bleed is its own bug is confounded by the bloat. Fix/understand the
bloat and either the bleed vanishes (it was the tail) or it stands out as a distinct bug. Also: the
bloat itself is the user-visible degradation (slow replies), so it's worth fixing on its own.

## What we already know (from the S1 investigation — see observation-ledger.md)
- Context accumulates in the **claude subprocess's own turn-context** on the claude-cli path (tool I/O
  + monologue + reasoning share it), not in the Python tool-loop (that's dead code on claude-cli,
  S1-O13). Across-turn history is text-only speaker/text turns (S1-O10).
- `apply_budget(max_tokens=80_000)` caps assembled context (engine.py:238); crossing it triggers
  compaction (budget.py:73-81) — the incident crossed it (~41K history + growing, S1-O17/O20).
- Latency scales hard with context: real incident within-reply gaps 79-94s vs single-digit earlier
  (S1-O20); harness 100-275s at ~41K (S1-O21). LATENCY is the cleanest objective readout — instrument it.
- `read_file` has caps (400-line/256KB/dedup); `propose_write` re-authors FULL file bodies each op
  (write_guard: create/append only, no overwrite) → a rework loop re-reads + re-authors growing content.

## Approach for tomorrow (decompose the assembled context)
1. **Instrument the per-turn assembled prompt and DECOMPOSE it by block.** For a SIMPLE task (edit one
   short file), log the token size of each contributor:
   - static system block (`build_static_system_message`, prompt.py) — voice, soul crystallizations, etc.
   - volatile suffix (`build_volatile_context`, prompt.py:~231) — interior-continuity block, self-model,
     attunement, journal, growth, maker, ambient-clock, recall block, reply frame.
   - conversation history (buffer turns) + the apply_budget trimming.
   - what actually goes to the claude subprocess (provider.py chat path ~635-644) incl. tool defs / MCP
     schema, and what re-enters via read_file results inside the subprocess turn.
   Find which block(s) dominate and which GROW with a trivial task.
2. **Reuse the harness.** `changes/s1-repro-harness/harness/` already drives the real path in-process
   and logs per-turn latency + dose. Extend it to log the assembled-context token breakdown (hook
   engine.respond / apply_budget, or count messages before provider.chat). A short-file-edit spine, not
   the growing-doc one, is the representative case here.
3. **Compare simple vs deep:** a cold short-file edit vs the same after a big seeded history — which
   blocks scale, which are constant. The constant-but-large blocks are static bloat; the scaling ones
   are accumulation.
4. **0.0.38 file path specifically:** what read_file / propose_write inject into the subprocess turn,
   and whether a rework loop re-injects full bodies (measure bytes in vs file size).

## Entry points (files)
- `brain/chat/engine.py` — `respond()` (message assembly ~213-245), `apply_budget` call (238).
- `brain/chat/prompt.py` — `build_static_system_message`, `build_volatile_context` (~231), the interior/
  self-model/journal/recall blocks.
- `brain/chat/budget.py` — `apply_budget` / compaction trigger (~73-100).
- `brain/bridge/provider.py` — claude-cli chat invocation (~635-644); what's actually sent + tool defs.
- `brain/tools/impls/read_file.py`, `propose_write.py`; `brain/chat/tool_loop.py`.
- Priors (verify, don't inherit): `~/Desktop/hunts/file-tool-bug-0040/REPORT.md` (0.0.38 token-burn, cost
  not coherence).

## Guardrails
- ⛔ Never drive chat through Phoebe — throwaway persona under temp KINDLED_HOME. Reading her files is fine.
- Token-spending runs → dragonfly triage = full guarded-change. Pin `claude`→2.1.186 (2.1.198/199 segfault).
- This is a DIAGNOSIS task → run under /dragonfly; the ledgers + config are in this same hunt folder.
</content>