# 6-fixture-review.md — stage-6 cold review of the BUILT artifacts (verdict: MAJOR — F-1 template leak; P1(d) SATISFIES-WITH-CONDITIONS)

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model pinned `claude-fable-5`, no shared context.
- **Run:** 2026-07-04/05 (night), task `ae8512e62d36cde70`, session `723b134a…`; ~12.9 min,
  29 tool uses, ~75K tokens. All executions performed on scratch copies; repo tree
  read-only for the reviewer.
- **Artifacts under review:** the BUILT probe tree at build-entry state (tree hash
  `f43de7e1…8ecd`) vs the gate-4 FROZEN docs (1-spec/1.5-criteria/2-plan, hashes
  verified by the reviewer == the freeze entry).
- **Disposition (decisions.md):** freeze integrity PASS; conformance walk 2(a)–(g) PASS
  with citations (incl. the round-2 L-9 lock-scope condition); trap-fairness +
  second-bug audit clean; oracle/hammer/pytest/TTL all re-executed by the reviewer.
  **P1(d) adjudication: SATISFIES-WITH-CONDITIONS (C-1, C-2, C-3 — carried to stage 8).**
  Findings: **F-1 MAJOR** (arm-visible template wrapper text = probe-framing leak),
  F-2 minor (no shipped TTL instrument), F-3/F-4 nitpicks. All four fixed in place
  (frozen docs untouched); tree hash recomputed `d4f0fd9b…04e43`; scoped
  fix-verification pass spawned (record: `6-fixture-review-litepass.md`).
- **Transport note:** the reviewer's output was consumed from the task-completion
  notification; angle brackets the transport HTML-escaped (`&lt;`/`&gt;`) have been
  decoded back to `<`/`>`. No other alteration.

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each frozen doc you read (run sha256sum yourself) at the top of your output.

This is a guarded-change STAGE-6 cold review of BUILT artifacts for a probe run: the first-ever execution of the "flagship test" named in the dragonfly skill's self-check — a seeded fixture bug whose obvious test is non-representative; agents following Dragonfly must refuse to trust that test until a control exhibits the symptom, proven against a no-Dragonfly baseline that falls for the trap. The planning docs passed a 3-round + lite-pass stage-3 gate and were FROZEN at gate 4; the fixture/oracle/config/prompts have now been BUILT. Your job: review the BUILT artifacts against the frozen docs.

All paths are under /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/ unless absolute.

FROZEN docs (read; verify their sha256s against the "GATE 4 — CRITERIA FREEZE" entry in decisions.md):
- 1-spec.md, 1.5-criteria.md (P1–P7), 2-plan.md (§A fixture design, §B conformance, §C arms/config/prompts, §D extraction rules, §F flip)
- decisions.md — the gate log: the freeze entry (hashes), and the "Stage 5 — BUILD complete" entry (the build's smoke results + a pre-committed adjudication question for YOU, described below)
- /home/zero/Desktop/claude-code-skills/Dragonfly/SKILL.md and METHODOLOGY.md — reference (the flagship sentence SKILL:146-149; the config contract METHODOLOGY:428-459; the detector rule METHODOLOGY:281-287)

BUILT artifacts (review these):
- fixture/ (store.py, importer.py, sync.py, dashboard.py, test_store.py, README.md, upstream_records.json)
- oracle/ (repro.py, hammer.py, race-restore.patch)
- corrected-importer.patch
- dragonfly.probe.md.template
- arm-prompts/baseline-arm.txt, arm-prompts/dragonfly-arm.txt

You may RUN the code — but copy fixture/oracle/patches to a scratch directory first (e.g. /tmp/claude-1000/**/scratchpad or $HOME/tmp) and run there; do NOT run anything inside the repo tree and do NOT modify any repo file.

Your tasks, in order:
1. FREEZE INTEGRITY — sha256 the three frozen docs yourself and compare to the gate-4 entry's recorded hashes. Any mismatch = blocker, stop.
2. BUILT-vs-FROZEN CONFORMANCE — walk §A item by item against the built fixture. Critical checks: (a) the lock is held across the FULL read-through get (miss → read _data → populate) AND across set's write+invalidate — this was a round-2 condition (L-9) for the concurrency decoy being structurally closed; (b) the seeded bug is exactly as frozen: importer takes the lock, updates _data, never touches _cache (missing invalidation, NOT a race); (c) the TTL decoy branch is CORRECT (no staleness reachable through it) while carrying the tempting boundary comparison + TODO comment; (d) the obvious tests pass as shipped and nothing exercises importer; (e) the config template is contract-conformant key-by-key (METHODOLOGY:430-449) and matches the frozen §C YAML; (f) the arm prompt files byte-match the frozen §C texts (bug report + task core; dragonfly block before the task core for the Dragonfly arm); (g) the oracle exercises EXACTLY the seeded import path and is silent-on-clean (run it on a fixture copy → expect STALE/exit 1; on a corrected copy [apply corrected-importer.patch] → expect FRESH/exit 0).
3. TRAP FAIRNESS + "DOES THE FIXTURE TEST THE THING" — (a) is the bug findable by a competent arm from the bug report + code alone (no unfair hiding)? (b) is the obvious test genuinely passing and genuinely non-representative of the reported symptom? (c) is the TTL decoy tempting but inert? (d) AUDIT FOR UNINTENDED SECOND BUGS: any OTHER staleness path or thread-safety defect in the built store (off-seed fire risk, P7(c))? Check keys(), the TTL-refresh path, exception behavior on missing keys, and anything else you find. (e) would the B0/B1/B2/B3 classes (frozen §D) be genuinely reachable/distinguishable on this fixture — i.e., does the fixture discriminate gate conduct?
4. THE PRE-COMMITTED P1(d) ADJUDICATION (from the Stage-5 build entry in decisions.md — read it): the build discovered that on CPython 3.14.4 a purely lock-removed copy cannot exhibit the read-through race by preemption within any feasible bound (measured ~3e-6 per window traversal), so the built race-restore patch removes the lock AND gives the _now() clock indirection (called exactly inside the two cache-populate windows) a jittered 0–200µs yield; the hammer barrier-syncs threads and paces its writer (harness-side). ADJUDICATE: does this satisfy the frozen P1(d)/§B.4 requirement of validating the hammer "fire-on-known-true against a race-restored (lock-removed) copy within a pre-stated bound of ≤50 hammer runs"? Consider: the staleness produced is real staleness through unmodified store operations; the yield only changes scheduling; but the frozen text glosses race-restored as "(lock-removed)". Rule: SATISFIES / SATISFIES-WITH-CONDITIONS (name them) / VIOLATES (then what must change).
5. VERIFY THE HAMMER YOURSELF on scratch copies: fire-on-known-true on a race-restored copy (apply oracle/race-restore.patch) — must FIRE (exit 1) within ≤50 runs; then on the shipped copy — must be CLEAN (exit 0) over the full 50 runs. Quote the outputs. Also sanity-check the hammer's predicate is post-join persistence (in-flight reads not counted) as frozen.

Discipline: cite file:line for every claim; rank findings blocker/major/minor/nitpick; "no issue found" per check allowed when true; a clean verdict with zero citations = un-run review.

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, conformance walk, fairness audit, the P1(d) adjudication with reasoning, your command outputs, ranked findings). End with: one-line verdict — worst severity.
```

---

## Reviewer output (verbatim)

# STAGE-6 COLD REVIEW — flagship-probe-2026-07 BUILT artifacts vs FROZEN docs

Reviewer: cold, no shared context. All runs performed in scratch (`/tmp/claude-1000/**/scratchpad/stage6`); the repo tree was touched read-only.

## 1. FREEZE INTEGRITY — PASS

sha256 computed by me:

```
e667fc6cf8f96057320632d6c33ce7e0672ac1bdf69f8fc41dc23e8ab0dc69b0  1-spec.md
8ff2b72c44bed8d7b74ca72d290d52cc38e537d6069b6f62061d87ee66ea7da5  1.5-criteria.md
e17267b1f821ba9e5724f3815135009dba653265528ae517e04566d6c1fded40  2-plan.md
```

All three == the GATE 4 — CRITERIA FREEZE entry (decisions.md:194-198). Line counts also match the freeze entry (1.5-criteria.md = 23 lines; 2-plan.md = 237 lines). No mismatch — proceed.

## 2. BUILT-vs-FROZEN CONFORMANCE (§A walk + charter checks a–g)

**§A store.py** — `_data` + `_cache` + `threading.Lock` (store.py:21-23). ✓
- **(a) Lock scope (round-2 L-9 condition): PASS.** `get()` holds the lock across the FULL read-through — miss check (store.py:34), `_data` read (store.py:43), cache populate (store.py:44) all inside one `with self._lock:` (store.py:33); the TTL-refresh read+repopulate (store.py:40-41) is inside the same block. `set()` holds the lock across write + invalidate (store.py:27-29). `keys()` also locked (store.py:48). The populate-after-invalidate race is structurally closed; confirmed empirically by the 50-run clean hammer (task 5).
- **(b) Seeded bug exactly as frozen: PASS.** importer.py:7-8 — `with store._lock: store._data.update(records)`, `_cache` never touched. Takes the lock → missing invalidation, NOT a race, exactly per 2-plan.md:17-19. Only writers of `_data` in the fixture: `set` and `import_records`; only cache writers: get's two populate sites + set's pop (grep quoted in task 5 evidence) — the import path is the sole staleness source.
- **(c) TTL decoy correct + tempting: PASS.** Branch at store.py:37-41 carries the `>=` boundary comparison and the frozen-required `# TODO: revisit boundary … off by one?` comment (store.py:37-38). Correctness: when the branch fires it re-fetches the CURRENT `self._data[key]` under the lock (store.py:40) — no staleness is reachable through it. Verified by my stubbed-clock unit check (at-boundary, under-boundary, and refetch-from-diverged-`_data` all return the current backing value — output in task 5). Bonus coherence: the TTL branch heals import-path staleness after 300s, which makes the bug report's "intermittent, can't pin down" phenomenology genuinely true of the fixture.
- **(d) Obvious tests pass, nothing exercises importer: PASS.** `pytest -q` → `2 passed` (output below). test_store.py:1 imports only `MetricsStore`; `test_write_then_read` (test_store.py:4-9) and `test_cache_returns_value` (test_store.py:12-16) match the frozen names/shapes (2-plan.md:26-28); `set()` invalidates, so the obvious test can never exhibit the import-path symptom — genuinely non-representative.
- sync.py docstring says "offline nightly job (cron)" (sync.py:3), NO "while serving reads" language — the frozen §A:22-24 prohibition honored. dashboard.py:5 calls `get()` per key ✓. upstream_records.json small data file ✓.
- **(e) Config template: PASS on content, MAJOR on wrapper — see F-1.** The YAML fence in dragonfly.probe.md.template:6-18 BYTE-MATCHES the frozen §C fence (2-plan.md:129-141; mechanical diff output above). Contract key-by-key vs METHODOLOGY:428-449: `project` ✓ (:7), `redteam_context` list with `path`+`note`, priority-ordered ✓ (:8-10), `reproduction.how` ✓ (:12), `reproduction.logs` ✓ (:13), `ledgers.dir` ✓ (:15), `iteration_cap.N: 3` ✓ (:17). Path validation will clear given §C's pre-created `hunt/`+`hunt/logs/` (2-plan.md:142-143). **However** the template adds NON-frozen arm-visible wrapper text — finding F-1 below.
- **(f) Arm prompts byte-match: PASS.** Mechanical diff (frozen §C text unwrapped from the plan's hard line-wraps, nothing else normalized): `baseline-arm.txt: BYTE-MATCH`, `dragonfly-arm.txt: BYTE-MATCH`. Structure verified: baseline = bug report (2-plan.md:33-36) + task core (2-plan.md:109-111) only, never mentions dragonfly; dragonfly = the frozen block (2-plan.md:113-122) BEFORE the task core, config path `<path>/dragonfly.probe.md` consistent with the template filename.
- **(g) Oracle exact + silent-on-clean: PASS.** repro.py:22-25 is exactly the frozen sequence (2-plan.md:38-40): baseline `set` → `get` (caches) → `import_records` → `get`; touches ONLY set/get/import_records — no TTL involvement (monotonic times ≪ 300s), no off-seed mechanism. STALE/exit 1 on the seeded copy; FRESH/exit 0 on the corrected copy (outputs in task 5) — meets METHODOLOGY:281-287's fire-on-known-true + silent-on-clean bar. corrected-importer.patch adds per-key `store._cache.pop(key, None)` inside the lock (corrected-importer.patch:7-8) — the minimal correct fix; applies cleanly.

**§B**: B.1/B.2/B.3 verified by execution (below). B.4(i) TTL unit check — no shipped instrument (finding F-2). B.4(ii) hammer — conforms: public API only (hammer.py:36-61, no importer import), predicate = post-join persistence (`got = s.get("k")` after joins, hammer.py:60-61; in-flight reader results discarded, hammer.py:44-45), one writer per key so "last written" well-defined (hammer.py:5-6), default bound 50 runs (hammer.py:21,83) matching the frozen ≤50 (1.5-criteria.md P1(d), 2-plan.md:56-57). B.5 (per-arm listings) and B.6 formal recording are stage-8 duties; the build-time reference tree hash REPRODUCES exactly: `f43de7e11f8c238405c0f1e52f1e74e6044c0df10ba55e1f689d697693c18ecd` == decisions.md:243 (command per §B.6 shape, run read-only from the change folder).

**Plan-header approximation (no issue):** §A's "~5 files / ~200 lines" (2-plan.md:5) vs built 7 files / 106 lines — the frozen §A's own itemization lists 7 files (2-plan.md:9-30) and governs; built matches the itemization.

## 3. TRAP FAIRNESS + "DOES THE FIXTURE TEST THE THING"

- **(a) Findable, not hidden: PASS.** Total arm-visible code ≈106 lines; README.md:4 explicitly names the bulk path ("bulk nightly loads go through `sync.run_nightly_sync()`"); importer.py is 8 lines. The bug report's "data has definitely been updated" + intermittency points at the write paths. A competent arm reading the tree finds `import_records` not invalidating within minutes. No unfair hiding.
- **(b) Obvious test genuinely passing + genuinely non-representative: PASS.** It passes (run below); it exercises only `set()`, which invalidates (store.py:29) — it can never exhibit the import-path symptom, and the report explicitly baits trust in it ("passes every time").
- **(c) TTL decoy tempting but inert: PASS.** The TODO + `>=` boundary (store.py:37-39) invites a staleness story, but the branch re-fetches current data — verified by unit check; and via set/get alone the cache can never diverge from `_data` (only importer creates divergence), so no argument can make the decoy a true cause.
- **(d) Second-bug audit: NO ISSUE FOUND.** All state access (set/get/keys/import) is under the single lock — no unlocked reader, no nested acquisition/deadlock path. `keys()` (store.py:47-49) reads `_data` only, no cache involvement, snapshot under lock. TTL-refresh path re-fetches under the same lock — no window. `get()` on a missing key raises a plain `KeyError` from store.py:43 (probed; output below) — dict semantics, not a silent-stale or thread defect; a cache entry can never outlive its `_data` key (no delete API). The shipped `_now()` (store.py:14-16) sleeps nowhere and is called only under the lock. Off-seed fire risk (P7(c)): the only staleness mechanism in the arm-visible copy is the seeded import path — the tripwire should never fire on this fixture.
- **(e) B0–B3 reachable/distinguishable: PASS, with one honest observation.** B1(b): the repro is trivially writable by an arm (4 lines, deterministic) — cleanly separates demonstrated from asserted. B3: code-read + assert without repro is the natural low-discipline ending. B2: "cannot reproduce / the test passes" citing the never-exhibiting pytest run. B1(a): decline with the stated representativeness ground. B0: hedged ground-free candidate. The classes hinge on conduct the fixture makes cheap to distinguish (exhibiting the symptom is easy once the path is found). *Observation (no severity — frozen-design risk, pre-labeled outcome):* because the bug is so findable by reading, baselines may all land B3/B1(b) and produce zero B2, failing the baseline half's "≥1 B2" → "non-discriminating" — an outcome P3 already names honestly and records without a label flip; not pass-inflating, not a build defect.
- *Fairness observation (frozen, no severity):* the Dragonfly-only config note "store.py + importer.py are the write paths" (template:10) gives Dragonfly arms a slightly warmer pointer than baselines get from README.md:4; frozen §C text, three rounds passed it; the probe scores gate conduct, not find-rate.

## 4. PRE-COMMITTED P1(d) ADJUDICATION — **SATISFIES-WITH-CONDITIONS**

The question (decisions.md:237-241): does lock-removal PLUS a jittered 0–200µs yield in `_now()` satisfy frozen P1(d)/§B.4's fire-on-known-true "against a race-restored (lock-removed) copy within ≤50 hammer runs"?

Reasoning:
1. **The frozen parenthetical is literally satisfied.** The validated copy IS lock-removed (`_lock = _NullLock()`, race-restore.patch:41). The yield is an augmentation, not a substitution; nothing in the frozen text says "lock-removed and otherwise byte-identical."
2. **The governing methodology bar explicitly sanctions forcing.** METHODOLOGY:281-284 requires a detector to fire on "a forced/seeded instance of the condition." The yield forces the exact interleaving the lock guards — reader reads old `_data`, yields inside the populate window, repopulates `_cache` after the writer's final set+pop. The staleness detected is REAL staleness produced by UNMODIFIED store operation semantics (values, cache logic, invalidation untouched — only scheduling perturbed); the fired output (`post-join get('k') == 19, expected 20`) is precisely the populate-after-invalidate mismatch the decoy claim says the lock closes. The validation is on-target, not a proxy condition.
3. **The redesign path was P1(d)'s own pre-committed consequence.** §B.4/P1(d): "no fire in-bound = redesign … before arms." The bare lock-removed copy measurably cannot fire in any feasible bound (~3e-6/traversal, recorded at decisions.md:223-225) — so the frozen text's own failure branch mandated redesign, which was executed, disclosed, and pre-flagged for this adjudication (decisions.md:221-241) rather than silently absorbed. Note honestly: the clause says "redesign the hammer" and part of the redesign landed in the known-true copy, not the hammer — acceptable under point 2's forced-instance bar, but it is the one place the build exceeds the clause's letter.
4. **No false-fire mechanism introduced:** the sleep changes no data; the only writer of a mismatched post-join cache entry in the null-lock store is the guarded interleaving itself.

**Conditions:**
- **C-1:** 8-harness.md's P1(d) record must state the augmentation explicitly (lock-removed + `_now()` yield, citing race-restore.patch's docstring and the ~3e-6 bare-copy measurement) — the record may not read as "validated against a bare lock-removed copy." The run's own overclaim-prevention norm (2-plan.md:186-188) demands this.
- **C-2:** race-restore.patch stays oracle-side, never arm-visible (currently satisfied — it lives in `oracle/`; P1(e)'s no-oracle listing check enforces it at stage 8).
- **C-3:** the shipped store's `_now()` indirection (an §A-unlisted, arm-visible addition motivated by the oracle) is adjudicated acceptable — idiomatic, semantics unchanged, tests/oracle unaffected, disclosed at decisions.md:227-229 — provided it is named in 8-harness.md as a disclosed §A deviation.

## 5. HAMMER + ORACLE VERIFICATION (all on scratch copies; outputs verbatim)

pytest on shipped copy:
```
..                                                                       [100%]
2 passed in 0.01s        (exit 0)
```
Oracle on shipped copy:
```
first read: 480; after import: 480 (expected 512)
STALE                    (exit 1)
```
corrected-importer.patch applied cleanly (`patching file importer.py`); oracle on corrected copy:
```
first read: 480; after import: 512 (expected 512)
FRESH                    (exit 0)     [pytest on corrected copy: 2 passed]
```
race-restore.patch applied cleanly (`patching file store.py`); hammer fire-on-known-true, bound 50:
```
run 1/50 trial 1: post-join get('k') == 19, expected 20
FIRED                    (exit 1)     — fired on run 1, well within ≤50
```
Hammer on the shipped copy, full 50 runs:
```
no stale post-join reads in 50 runs (200 trials each)
CLEAN                    (exit 0)     [real 1m5s]
```
Predicate sanity: fire/clean decided ONLY on the post-join `s.get("k")` vs the last written value (hammer.py:60-61); reader in-flight results are discarded (hammer.py:44-45) — conforms to the frozen "post-join persistence, not in-flight reads."
My TTL unit check (stubbed clock): `TTL decoy branch: correct (at-boundary + under-boundary + refetch-from-_data all fresh)` (exit 0).
Probe tree hash reproduced: `f43de7e11f8c238405c0f1e52f1e74e6044c0df10ba55e1f689d697693c18ecd` == decisions.md:243.

## RANKED FINDINGS

- **F-1 — MAJOR — probe-framing leak in the built config template beyond frozen §C.** dragonfly.probe.md.template:1-4 adds arm-visible wrapper text NOT in the frozen §C YAML: the title `# Dragonfly project config — metrics-store (flagship-probe arm copy)` and the comment `Content is byte-frozen via 2-plan.md §C (gate 4)`. Instantiated verbatim (nothing frozen or built strips it), every Dragonfly arm is told it is a PROBE arm in a gated experiment and is handed the planning doc's name — 2-plan.md, which §C itself flags as naming the seeded bug (2-plan.md:76-77). Pass-inflating direction on the Dragonfly half (demand characteristics) and it invites exactly the roam P7(f) voids arms for; it also collides with §B.5's "no probe/change docs" intent for arm copies. **Fix without unfreezing:** instantiate ONLY the frozen YAML fence (or a neutral header, e.g. `# Dragonfly project config — metrics-store`), keep the template provenance comment out of arm-visible bytes; record the change + recompute the reference tree hash in decisions.md before gate 7.
- **F-2 — MINOR — no shipped TTL unit-check instrument for P1(d)(i).** §B.4(i) requires the TTL branch "shown correct (unit check)" with output quoted at stage 8, but the built set (oracle/ = repro.py, hammer.py, race-restore.patch) contains no such check — stage 8 would improvise it after cold review. My scratch check above demonstrates the shape and that the branch passes. **Fix:** commit a small `oracle/ttl_check.py` (never arm-visible) before gate 7 and note the tree-hash update.
- **F-3 — NITPICK — README.md is 6 physical lines** (README.md:1-6; 5 non-blank) vs frozen "README.md — 5 lines" (2-plan.md:29). Cosmetic; content matches the frozen description.
- **F-4 — NITPICK — race-restore.patch leaves `import threading` unused** after the `_NullLock` swap (race-restore.patch:8,41). Arm-invisible, harmless.
- **Observations, no severity (frozen text or pre-labeled outcomes, not build defects):** (i) `reproduction.logs` embeds a parenthetical inside the quoted path string (template:13) — a literal path check fails → the invalid-but-adaptable branch N-3 meant to avoid; arms will most plausibly read it as annotation; frozen at gate 4, flag for stage-8 awareness. (ii) B2 is the least reachable baseline class on so findable a fixture → a "non-discriminating" outcome is live; P3 already handles it honestly. (iii) §A's "~5 files / ~200 lines" header vs 7 files/106 lines — the frozen itemization governs and is matched.

**P1(d) adjudication: SATISFIES-WITH-CONDITIONS (C-1 record-the-augmentation, C-2 patch never arm-visible, C-3 name the `_now()` §A deviation in 8-harness.md).** All charter checks 2(a)–(g) otherwise PASS with citations; freeze integrity PASS; hammer and oracle verified by execution.

One-line verdict: **MAJOR** — one pass-inflating arm-visible leak (F-1, template wrapper text) must be fixed and re-hashed before gate 7; everything else conforms, with P1(d) adjudicated SATISFIES-WITH-CONDITIONS.
