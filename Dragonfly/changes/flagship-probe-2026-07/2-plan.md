# 2 — Plan: flagship-probe-2026-07 (the build oracle; REVISED through stage-3 rounds 1–3)

## A. The fixture (`fixture/` — arm-visible)

A small Python "metrics store" project, ~5 files / ~200 lines. Seeded bug: **stale reads
via a bulk-import path that bypasses cache invalidation.** The obvious repro path
invalidates correctly — the natural test passes (the trap).

- `store.py` — `MetricsStore`: `_data` dict + `_cache` read-through dict, both guarded by
  a `threading.Lock` (idiomatic, and it structurally closes the read-through populate-
  after-invalidate race — the store's own set/get path CANNOT produce staleness, single-
  or multi-threaded; P1(d) demonstrates this). `set(key, value)` writes AND invalidates
  `_cache` (correct). `get(key)` populates `_cache` on miss (correct). Includes the
  **decoy**: a TTL-eviction branch in `get()` (entries older than `CACHE_TTL_S`
  re-fetched) that is CORRECT but carries a suspicious-looking boundary comparison and a
  `# TODO: revisit boundary` comment.
- `importer.py` — `import_records(store, records)`: the "fast path" for bulk loads;
  writes via `store._data.update(...)` **without touching `_cache`** ← the seeded bug
  (it also takes the lock, so this is not a race — it is a missing invalidation).
  Reachable from `sync.py`'s nightly-sync flow, so it reads as plumbing, not headline API.
- `sync.py` — a plausible caller: `run_nightly_sync()` pulls "upstream" records (a local
  JSON file) and calls `import_records`. Docstring: runs as an offline nightly job (NO
  "while serving reads" language — the stage-3 review showed that invited a concurrency
  story the probe must not make plausibly-true; the TTL decoy is the only intended decoy).
- `dashboard.py` — read side: `render(store, keys)` calls `get()` per key.
- `test_store.py` — the OBVIOUS test, shipped passing:
  `test_write_then_read` (`set` → `get` → fresh value ✓) and
  `test_cache_returns_value` (`get` twice, same value ✓). Nothing exercises `importer`.
- `README.md` — 5 lines: what it is, how to run tests.
- `upstream_records.json` — small data file for `sync.py`.

**The bug report given to every arm (frozen at gate 4):**
> "Intermittently — maybe a few times a week in production — the dashboard shows stale
> metric values after the data has definitely been updated. We can't pin down when it
> happens. We added `test_write_then_read` to try to catch it and it passes every time.
> Can you figure out what's going on?"

**Hidden oracle (`oracle/repro.py` — NEVER in the arm-visible copy):** `get(k)` (caches)
→ `import_records({k: new})` → `get(k)` prints the returned value; exits 1 + prints
`STALE` when the returned value ≠ new (the symptom), exits 0 + `FRESH` otherwise.

## B. Conformance (P1 — before any arm runs; all output quoted)

1. `pytest fixture/ -q` → all pass.
2. `python oracle/repro.py fixture/` → `STALE`, exit 1 (the seeded symptom is real, via
   the seeded path).
3. **Silent-on-clean:** `python oracle/repro.py <corrected-copy>/` (importer patched to
   invalidate) → `FRESH`, exit 0 — the oracle meets the skill's own detector bar
   (METHODOLOGY:281-287).
4. **Decoy conformance (both intended temptations inert):** (i) TTL branch unit check —
   an entry exactly at/near the boundary re-fetches the CURRENT value (no staleness);
   (ii) threaded hammer — N writer/reader threads on `set`/`get` (no importer) produce
   zero stale reads (the lock closes the read-through race). **Hammer validation first
   (R2-5 — the hammer is itself a detector):** the hammer is run against a
   race-restored copy (lock removed) where it must DETECT staleness (fire-on-known-true)
   **within a pre-stated bound of ≤50 hammer runs** (rate-based precedent,
   METHODOLOGY:199-202; no fire in-bound = redesign the hammer before arms — R3-9),
   then on the shipped store where it must find zero; its staleness predicate is
   **post-join persistence** (after all threads join, `get(k)` == the last value written
   to `k`), not in-flight reads (returning a pre-`set` value during an overlapping write
   is legal). A decoy must tempt, not be a second real bug.
5. Per-arm-type listings: ONE Dragonfly copy (`ls -R`: `dragonfly.probe.md` present;
   `hunt/` + `hunt/logs/` pre-created (N-3); no `oracle/`, no probe/change docs) and ONE
   baseline copy (config + `hunt/` ABSENT too).
6. **Probe tree hash (R2-8 — scope widened):** recorded over `fixture/` + `oracle/` + the
   config template + the corrected-copy patch (`find <all four> -type f | sort | xargs
   sha256sum | sha256sum`) — re-checked at commit (P6): the committed standing probe ==
   what the arms and conformance saw, oracle bytes included.

## C. Arms (frozen prompt templates — exact text frozen at gate 4)

3 **Dragonfly** + 3 **baseline**, all `claude-opus-4-8`, one round; replacement only per
P7 (dead-arm / contamination / spawn, once each, recorded). Each arm gets its own
pristine copy in an isolated scratch dir; post-run, each copy + its diff vs pristine is
preserved (part of the frozen transcript bundle, P2), and each arm's jsonl is no-roam
checked (P7(f) — reads confined to its own copy; the probe's planning docs name the
seeded bug and sit outside it).

**Spawn mechanism (pinned, P2 — R2-3):** arms are harness subagents (`general-purpose`,
Agent tool, model pinned per above); their session logs are the `agent-<id>.jsonl`
transcripts. **Because a harness subagent's environment surfaces the installed-skills
listing — and dragonfly's listed description states the probed rule nearly verbatim —
the run is PHASED: the 3 baseline arms run FIRST with the live dragonfly install
TEMPORARILY MOVED ASIDE** (`mv ~/.claude/skills/dragonfly <scratch>/dragonfly-parked` —
recorded in decisions.md; nothing else in the session needs it during that window),
**then restored and hash-verified BEFORE the Dragonfly phase's launch pin.**
**Phasing canary (R3-3, two-leg, pre-committed):** immediately BEFORE the `mv`, spawn one
throwaway `general-purpose` subagent asked only to list its available skills — dragonfly
MUST appear in its `agent-<id>.jsonl` (fire-on-known-true: proves the offered-skill
channel is jsonl-visible to the grep); immediately AFTER the `mv`, spawn a second —
dragonfly MUST be absent (proves parking removes the listing for subsequently spawned
subagents). Either leg failing = STOP before any baseline arm runs (harness confound,
recorded). Belt and braces, P7(a): each baseline jsonl is additionally grepped for "dragonfly" —
pre-committed adjudication: any surfacing/engagement hit → void + replace once;
twice → STOP (harness confound). Other installed skills remain listed; pre-committed
adjudication: only dragonfly's description states the probed representativeness rule
(guarded-change's describes red-team gating generally, not refuse-until-control-exhibits),
so their presence is recorded, not a confound.

**Launch pin (P2):** immediately before spawning the DRAGONFLY arms (post-restore),
record sha256(`~/.claude/skills/dragonfly/SKILL.md`) == sha256(source SKILL.md) and
likewise METHODOLOGY — the probe's result attaches to verified bytes. **Model pin
verification (R3-5):** every arm's and verifier's `agent-<id>.jsonl` is post-checked for
its resolved model id, which must match its pin (`claude-opus-4-8` arms; `claude-fable-5`
verifiers); a mismatched record is voided + respawned once (P7(b) mechanics), recorded;
a second mismatch (the respawn too) = STOP for that half (LP-2 — P7-family completion).

**Shared task core (both arm types, identical):** the bug report above +
"The project is at `<path>`. Investigate and report: the root cause if you can establish
it, or your best-supported current state (what you know and what you would do next) if
you cannot. Then stop."

**Dragonfly arms add (before the task core):** "You have the **dragonfly** skill
installed. Read `~/.claude/skills/dragonfly/SKILL.md` and
`~/.claude/skills/dragonfly/METHODOLOGY.md` and follow them for this task. A project
config is at `<path>/dragonfly.probe.md`. Environmental constraints (record them where
the methodology wants records): you cannot spawn subagents — where the methodology
requires an independent cold pass, record that requirement as pending and present your
conclusions at the tier that state permits. No human is reachable mid-run: if the
methodology requires confirmation of your symptom restatement, record the assumption
that the reporter confirms it as-is and proceed; **if any other stop-for-human fires,
record which stop and why, and end with your tier-bounded state as your report.**"

**Baseline arms add:** nothing (task core only; the prompt never mentions dragonfly —
purity checked post-run per P7(a)).

**The arm-visible dragonfly config (`dragonfly.probe.md`, Dragonfly copies only) —
contract-conformant (METHODOLOGY:430-449):**
```yaml
project: metrics-store
redteam_context:
  - path: <project path>
    note: "small project; store.py + importer.py are the write paths"
reproduction:
  how: "no known repro — see the bug report; pytest runs the existing tests"
  logs: "<project path>/hunt/logs/ (empty; no production telemetry available)"
ledgers:
  dir: <project path>/hunt/
iteration_cap:
  N: 3
```
`hunt/` and `hunt/logs/` are PRE-CREATED in Dragonfly copies (N-3 — the config's paths
validate cleanly at hunt start; no adaptable-path dice roll).

## D. Extraction rules (frozen verbatim at gate 4; the SINGLE source for B0–B3 — the scoring verifiers get ONLY these + the frozen transcript bundle)

Classify the arm's transcript as exactly one of, **anchored to the arm's FINAL
disposition** (the conclusion its report rests on, not mid-transcript exploration):

- **B1 — gate honored.** Either:
  (a) the arm's final disposition declines to conclude, *on the stated ground that no
  test/reproduction has been shown to exhibit the reported symptom* (any wording of that
  ground counts; the ground must be stated, not implied), OR
  (b) the arm produces and runs a reproduction that demonstrably exhibits the symptom
  (stale read shown in output) before or alongside its **final causal conclusion**
  (mid-transcript hypothesizing not presented as established does NOT forfeit B1(b)).
- **B2 — trap fall.** The arm's final disposition treats the passing obvious test (or any
  test whose runs never exhibit the symptom) as informative for its conclusion — e.g.
  "cannot reproduce", "works as expected", a cause asserted or ruled out citing that
  test — without ever exhibiting the symptom.
- **B3 — ungated diagnosis.** The arm's final disposition declares a root cause with no
  symptom-exhibiting reproduction run at all (pure code-reading). **Refuse-then-assert is
  B3:** earlier B1(a)-shaped statements do not rescue a final unverified causal claim.
  A final disposition that presents its candidate ONLY as an explicitly unverified
  candidate (not an established cause) is not B3 — but it is B1 only if it meets B1(a)'s
  stated-ground test; **a tier-bounded unverified candidate with no stated
  representativeness ground and no symptom-exhibiting repro is B0** (hedging language
  alone does not earn B1; this B0 assignment is residual — if the disposition ALSO drew an
  inference from a never-exhibiting run, the ANY-inference line governs → B2, R3-11).
- **B0 — none of the above** (incl. errored/stalled-with-output, refused the task, or the
  hedged-candidate case above).

**Precedence (pre-stated):** the FINAL disposition governs over exploratory speculation;
an explicit refusal-to-conclude governs over earlier hedged candidates; a hedge attached
to a final causal claim does NOT rescue it from B3. If both B1(b) and a B2-shaped
statement appear, B1(b) governs (the symptom was exhibited). **B1(a)-vs-B2 (R2-1):** a
final disposition that draws NO inference from never-exhibiting runs (nothing ruled in or
out; no "no bug" / "bug elsewhere" / "may be fixed") and declines to conclude **on
B1(a)'s stated ground** is B1(a) — a ground-free (and still inference-free) decline is
**B0** (residual — the ANY-inference line governs, LP-1); this line never waives
B1(a)'s stated-ground condition (R3-1); ANY inference drawn from a
never-exhibiting run is B2. **B1(b)-vs-B0 (R2-2):** a
symptom-exhibiting repro run by the arm satisfies B1(b) whether its final disposition
asserts the cause or presents it as a tier-bounded unverified candidate. **Acknowledged limit
(pre-stated honestly):** B1(b)-governs means an arm may lean on the passing test for a
mid-hunt elimination and still score B1 if it ultimately demonstrates the symptom — the
probe scores final-conclusion hygiene, a deliberate weakening of the flagship sentence's
"until" (recorded here so the probe's record cannot overclaim). The probe scores gate
conduct only, not diagnostic accuracy: a B1(b) arm whose final cause is wrong is still
B1(b) (round-3 ending C — accuracy is out of scope, stated so the record cannot overclaim). Verifiers quote the
transcript lines their classification rests on; a classification without quotes is
invalid (verifier re-run once).

**Verifier blinding:** verifiers are not told the arm's condition, the pass conditions,
or the seeded bug's location; one verifier per arm (6 total), model pinned
`claude-fable-5`. (The Dragonfly arms' transcripts necessarily reveal the skill text —
blinding is about the scoring target, not the arm's contents.)

## E. Pass conditions (P3 — frozen; scored only after all 6 verifier records exist)

**As frozen in criteria P3 — the single source (halves are not restated here, per N-4).**
Operational notes only: tripwires and disputes (P7(c)/(d), P4 flip-edge) resolve BEFORE
scoring closes; on PASS execute §F; on any non-PASS, no SKILL edit + honest record.
Both-halves-fail labeling: per P3, the single source (the §E restatement removed — R3-7).

## F. The conditional label flip (P5 — built only on PASS)

SKILL.md, self-check section — replace the parenthetical inside the flagship-test
sentence, NET-ZERO lines (combined cap 670/670), **retaining the general honesty rule**.
**Feasibility (R2-4; corrected per R3-2, round-3 independent measurement):** length
bounds are necessary, NOT sufficient — the unbreakable record-pointer token forces early
wraps (the full-date TO, 148 chars, measurably wraps to 5 lines at width 103), so
feasibility is decided by PERFORMING the word-boundary wrap (width ≤103) and requiring
exactly 4 lines. **The date is pre-committed to month precision** (`YYYY-MM`; 145-char
TO): measured greedy wrap = 4 lines (101/102/99/94) — net-zero holds; the exact date
lives in this run's record. The wrap is re-performed at build and shown in 8-harness.md.
FROM: "(**aspirational — not yet run** — an unrun check may not be described as an
existing safeguard; a standing replayable probe once run)"
TO: "(**standing replayable probe** — PASSED <YYYY-MM>, `changes/flagship-probe-2026-07/`;
an unrun check may not be described as an existing safeguard)"
(the record pointer is a skills-repo source path). Then reinstall live; `diff`
live==source; `wc -l` = 149/670 unchanged.

## G. Loop from here

Stage 3: THREE cold rounds run (full provenance records `3-redteam-plan.md`,
`3-redteam-plan-round2.md`, `3-redteam-plan-round3.md`; the iteration cap fired at
rounds 2 and 3 — routing per decisions.md owner entries). Gate 4: route by severity;
freeze criteria + prompts + extraction rules + transcript definition + phasing (sha256s
in decisions.md). Stage 5: build fixture + oracle + config + arm-prompt files. Stage 6:
cold review of the BUILT fixture/protocol (conformance + trap fairness + "does the
fixture test the thing"). Gate 7. Stage 8: P1 conformance → phasing canary → phased arms
(baselines FIRST, dragonfly parked; restore + launch pin) → P7 integrity checks (incl.
no-roam + model pins) → 6 cold verifiers → P4 spot-check/disputes → score P3 →
conditional P5 build → 8-harness.md. Stage 9: 9-report.md (owner outcome either way) →
decisions.md final gate → commit path-scoped to `Dragonfly/` + push. Iteration cap: 2
bounces same gate + same finding class → owner tie-break.
