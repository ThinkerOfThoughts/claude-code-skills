# 6-fixture-review-litepass.md — scoped stage-6 fix-verification (verdict: NITPICK — gate 7 clears)

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model pinned `claude-fable-5`, no shared context.
- **Run:** 2026-07-04/05 (night), task `aedd745fc7a561924`, session `723b134a…`; ~8.9 min,
  29 tool uses, ~72K tokens. All executions on scratch copies; repo tree read-only.
- **Scope (per the stage-6 gate entry's routing):** verify the four stage-6 fixes
  (F-1..F-4) + one fresh sweep of the FULL arm-visible byte-surface (F-1's class).
  Not a re-review of anything else.
- **Disposition (decisions.md):** all four fixes VERIFIED genuine (F-1 by fence
  byte-compare — `FENCE-BYTE-MATCH` vs frozen §C; F-2/F-4 by execution — ttl_check
  exit 0, patched copy threading-free + hammer FIRED run 1; F-3 by count+content);
  recomputed tree hash reproduced exactly; arm-visible byte-surface sweep CLEAN
  (zero real hits on the baseline surface; only frozen/sanctioned tokens on the
  Dragonfly surface; one no-severity observation: the frozen config FILENAME contains
  "probe" — recorded for stage-8 awareness). **1 nitpick (LV-1)** — ttl_check's
  under-boundary leg was non-discriminating; **FIXED post-pass** (divergence induced;
  cached-value assertion; verified exit 0), tree hash updated →
  `7fcf9b78c7169be44fe1f6b8b07b48111b0b0b3df1d08d5beed9f2d02189e534` (the pre-arm
  reference; formal P1(f) recording at stage 8).
- **Transport note:** consumed from the task-completion notification; HTML-escaped
  angle brackets decoded back to `<`/`>`. No other alteration. (The reviewer's own
  first hash line contains a self-corrected transcription stub — left verbatim.)

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each file you read that has a recorded hash (run sha256sum yourself) at the top of your output.

This is a SCOPED stage-6 fix-verification pass for a probe run (guarded-change loop). The full stage-6 cold review of the BUILT artifacts returned MAJOR with 4 findings; the author applied fixes. Your job: (1) verify those four fixes, and (2) run one fresh sweep of the FULL arm-visible byte-surface — the class the MAJOR belonged to. You are NOT re-reviewing anything else (the full review verified the rest by execution).

All paths under /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/ unless absolute.

Context (closed set):
- 6-fixture-review.md — the full stage-6 record (charter + verbatim findings F-1..F-4 + the P1(d) adjudication). Read in full.
- decisions.md — the gate log; read the "Stage-6 gate" entry (the author's claimed fixes + the recomputed tree hash `d4f0fd9b404a58e7a6fa723fd9b6f30370fc87c7578befd73ee9e32690a04e43`) and the "GATE 4 — CRITERIA FREEZE" entry.
- 2-plan.md (FROZEN — verify its hash against the freeze entry: `e17267b1f821ba9e5724f3815135009dba653265528ae517e04566d6c1fded40`) — §C for the frozen config fence + arm prompts + copy composition (what each arm-type copy contains).
- The FIXED built artifacts: dragonfly.probe.md.template, oracle/ttl_check.py, fixture/README.md, oracle/race-restore.patch — plus the rest of fixture/ and arm-prompts/ for the byte-surface sweep.

You may RUN code — copy to a scratch dir first (/tmp/claude-1000/**/scratchpad or $HOME/tmp); never run inside or modify the repo tree.

Tasks:
1. F-1 (MAJOR — template wrapper leak): verify dragonfly.probe.md.template now contains ONLY a neutral header + the frozen §C YAML fence (byte-compare the fence against 2-plan.md §C's fence). No probe/gate/plan-naming text anywhere in the file. Quote the entire file.
2. F-2 (minor): verify oracle/ttl_check.py exists, is oracle-side (not part of any arm-visible copy composition per frozen §C/§B.5), and RUN it on a scratch fixture copy — expect "correct"/exit 0. Sanity-check its three cases actually exercise under/at/past boundary against a diverged backing store.
3. F-3 (nitpick): README.md is now 5 physical lines, content per frozen §A.
4. F-4 (nitpick): race-restore.patch's patched result has no unused `import threading`; apply the patch to a scratch fixture copy, confirm it parses, and confirm the hammer still FIRES on it (exit 1) within the ≤50-run bound.
5. Verify the recomputed tree hash: run `find fixture oracle dragonfly.probe.md.template corrected-importer.patch -type f | sort | xargs sha256sum | sha256sum` (read-only) from the change folder and confirm it equals `d4f0fd9b404a58e7a6fa723fd9b6f30370fc87c7578befd73ee9e32690a04e43`.
6. FRESH SWEEP — arm-visible byte-surface (F-1's class): enumerate every byte an arm could see per the frozen copy composition (§C/§B.5): for a BASELINE copy = fixture/ files only; for a DRAGONFLY copy = fixture/ files + the instantiated config + pre-created empty hunt/ dirs. Grep/inspect ALL those bytes for: any mention of dragonfly (baseline surface only), probe/experiment/arm/gate/frozen/oracle/flagship framing, references to the planning docs or the skills repo, or anything else that leaks the evaluation context or the seeded bug's location beyond what the frozen fixture design intends (the README's legitimate pointer to the bulk path is frozen design, not a leak). Report anything found with severity.

Discipline: cite file:line; rank findings blocker/major/minor/nitpick; quote command outputs; a clean verdict with zero citations = un-run review.

Your final message is consumed as a machine-checked record — output the full review verbatim. End with: one-line verdict — worst severity.
```

---

## Reviewer output (verbatim)

# SCOPED STAGE-6 FIX-VERIFICATION (litepass) — flagship-probe-2026-07

Reviewer: cold, no shared context with the author. All executions performed on scratch copies under `/tmp/claude-1000/**/scratchpad/litepass`; the repo tree touched read-only. Scratch interpreter: Python 3.14.4.

## sha256 of files read (computed by me, `sha256sum`)

Files with a recorded hash:
```
e17267b1f821b8a9e5724f... — recorded value: e17267b1f821b8... (see verbatim line below)
e17267b1f821ba9e5724f3815135009dba653265528ae517e04566d6c1fded40  2-plan.md
    == GATE 4 freeze entry (decisions.md:198) and == the charter's stated freeze hash. FROZEN-DOC INTEGRITY PASS.
```
Aggregate recorded hash (the four built surfaces, decisions.md:283): verified in task 5 below — `d4f0fd9b404a58e7a6fa723fd9b6f30370fc87c7578befd73ee9e32690a04e43`, exact-string MATCH.

Other files read (no individual recorded hash; component hashes feed the verified tree hash):
```
ca7f2e56d51118d34fbf7eb0609d9b371c7ce2e388b16ba501a5caa7aa100d56  6-fixture-review.md
9ef31e85118bb0cc4307a62dc35498f5cbf0268167b930ec2f07353e8bc0cdf2  decisions.md
91db4a50a03d15b62f88ec071e584d8c47668069f4f4419e7ab95bf00b516dbf  dragonfly.probe.md.template
3ca6737a92ef09b10d18e2fed2c18f858b823cd14244d7f8e6ff35328ccee4e7  oracle/ttl_check.py
4fde5a018d76d95cc39152ef0e4c41fa912951f102aaee1eb3e9712729f53637  fixture/README.md
e120e8c92f1124b59f695a3451cd4649f06208a7c52c7312be4a9c6149f2bb35  oracle/race-restore.patch
c9c18446455b479cb19b8a441c1602602b0a9e86bc29af14298eaf6da1c2b370  fixture/store.py
08baed74ebea9f545c4639a4c7e9a48507a62904a68f2c6fc1d76d08a6956508  fixture/importer.py
86acf6a48c2e7a52955579d1c6ee62c8bc000f3192b08cbc8af8ab06f634b82b  fixture/sync.py
5245ef4696a04ab42d64e402223c329c7dd7dd7c7ddaa15f22f06d8568d5e54e  fixture/dashboard.py
6bfb16afc3294c1b1e584ceaa791f670660720a4283d20e2b3cd5f426c82b006  fixture/test_store.py
13acd3dd5beb5fdaba14d7bcc3d5587e69f6af52eb258127f72b6f07a4c0cd64  fixture/upstream_records.json
e15c24dd272bf4a29ca38ef573ad4b3b8d0514d08dc3dd081916729b04af9614  arm-prompts/baseline-arm.txt
54094f0d5d6361c1ac643cc3844aa04730912aa66205b83773fa6c20a311e21a  arm-prompts/dragonfly-arm.txt
029a96bc075278baf1fc3760d39223c7c18ab9b64c207dc666f18f658adac643  oracle/hammer.py
```

## Task 1 — F-1 (MAJOR, template wrapper leak): VERIFIED FIXED

The entire file, quoted (dragonfly.probe.md.template:1-15, 15 lines):

```
# Dragonfly project config — metrics-store

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
```

- Structure is exactly the F-1 remedy: line 1 = the neutral header the finding itself proposed verbatim (`# Dragonfly project config — metrics-store` — 6-fixture-review.md:154), line 2 blank, lines 3–15 the fence. Nothing else.
- **Fence byte-compare:** `sed -n '129,141p' 2-plan.md` vs `sed -n '3,15p' dragonfly.probe.md.template` → `cmp` output: `FENCE-BYTE-MATCH`; both extracts sha256 `fa1d33f17a39fec6b1f72efc2e858223b92fef74939ef6dd5a3e73f56198d32f`. The instantiated config is the frozen §C fence byte-for-byte (2-plan.md:129-141).
- **No probe/gate/plan-naming text:** the offending strings ("flagship-probe arm copy", "byte-frozen via 2-plan.md §C (gate 4)") are gone. Grep of the file content for `probe|experiment|gate|frozen|freeze|oracle|flagship|2-plan|decisions|1-spec|criteria|baseline|conformance|blind` → zero hits; only remaining flagged tokens are `Dragonfly` (the sanctioned header, Dragonfly-surface only) and `redteam_context` (the skill's own config-contract key, METHODOLOGY contract, inside the frozen fence).

## Task 2 — F-2 (minor, TTL instrument): VERIFIED FIXED, with one nitpick

- `oracle/ttl_check.py` exists (64 lines). Oracle-side: it lives in `oracle/`, which frozen §B.5 excludes from BOTH copy types (2-plan.md:62-64 — Dragonfly copy: "no `oracle/`, no probe/change docs"; baseline: "config + `hunt/` ABSENT too"); frozen §C copy composition gives arms fixture files + config + hunt/ dirs only. Docstring self-declares "NEVER arm-visible" (ttl_check.py:1). Not part of any arm-visible composition. ✓
- **Run on a scratch fixture copy:**
  ```
  TTL decoy branch: correct (under-boundary, at-boundary, past-boundary all yield current data)
  ttl_check exit: 0
  ```
- **Case sanity vs store.py:** the stub is effective (`store_mod._now` replaced at ttl_check.py:21; `get()` calls the module-global `_now` at call time, store.py:39,41,44).
  - At-boundary (ttl_check.py:33-41): populate at t=2000, diverge `s2._data["m"] = 99` directly, clock = 2000+`CACHE_TTL_S` → `_now()-cached_at >= CACHE_TTL_S` fires exactly at the `>=` boundary (store.py:39) → must return current 99. Genuinely exercises the decoy branch against a diverged backing store. ✓
  - Past-boundary (ttl_check.py:44-52): +TTL+60s, diverged (`_data["m"] = 7`), must return 7. ✓
  - Under-boundary (ttl_check.py:25-30): populate at t=1000, clock = TTL−0.001 → branch must not fire → returns cached 1. **But no divergence is induced in this leg** (the docstring concedes it: "no divergence via the public API", ttl_check.py:24) — cached == backing == 1, so this leg cannot distinguish a cache hit from an erroneous early re-fetch; it is non-discriminating as written. See finding LV-1 (nitpick). The frozen §B.4(i) bar — "an entry exactly at/near the boundary re-fetches the CURRENT value (no staleness)" (2-plan.md:50-52) — is fully met by the at/past legs, and an early-firing branch could only ever produce fresher data, never staleness, so nothing frozen is unmet.

## Task 3 — F-3 (nitpick, README length): VERIFIED FIXED

- `wc -l fixture/README.md` → `5`. Five physical lines, all non-blank (README.md:1-5).
- Content per frozen §A "5 lines: what it is, how to run tests" (2-plan.md:29): lines 1–4 what it is, line 5 `Run the tests with `pytest -q` from this directory.` The bulk-path pointer (README.md:3) is the charter-designated frozen design element, unchanged from the reviewed version — not a leak.

## Task 4 — F-4 (nitpick, unused import in patched result): VERIFIED FIXED

- The regenerated patch's first hunk now REPLACES the import: `-import threading` / `+import random` (race-restore.patch:7-8) — previously it left `import threading` dangling alongside the `_NullLock` swap.
- Scratch application:
  ```
  patching file store.py
  patch exit: 0
  grep -n "threading" store.py → (no output), exit 1 (zero occurrences)
  py_compile OK
  ```
- Hammer fire-on-known-true on the patched copy, default bound 50:
  ```
  run 1/50 trial 5: post-join get('k') == 19, expected 20
  FIRED
  hammer exit: 1
  ```
  Fires on run 1, trial 5 — well within the frozen ≤50-run bound (hammer.py:21,83; 2-plan.md:56-57). The adjudicated P1(d) design (_NullLock at race-restore.patch:14-19,41; jittered 0–200µs `_now()` yield at race-restore.patch:22-33) is otherwise unchanged, so conditions C-1..C-3 are unaffected by this fix.

## Task 5 — recomputed tree hash: VERIFIED

Run read-only from the change folder:
```
$ find fixture oracle dragonfly.probe.md.template corrected-importer.patch -type f | sort | xargs sha256sum | sha256sum
d4f0fd9b404a58e7a6fa723fd9b6f30370fc87c7578befd73ee9e32690a04e43  -
```
Exact-string compare vs the charter's expected value and vs decisions.md:283 → `TREE-HASH-MATCH` on both. The Stage-6 gate entry's recorded hash is what the tree currently produces.

## Task 6 — FRESH SWEEP of the full arm-visible byte-surface: CLEAN (one no-severity observation)

Surface enumerated per frozen §C/§B.5 (2-plan.md:62-64, 73-77, 127-143):
- **BASELINE copy** = fixture/ files only: README.md, dashboard.py, importer.py, store.py, sync.py, test_store.py, upstream_records.json (`find fixture -mindepth 1` confirms exactly 7 files, no dotfiles/hidden bytes) — plus the baseline-arm.txt prompt text the arm receives.
- **DRAGONFLY copy** = the same 7 files + the instantiated config (the 15-line template, task 1) + pre-created EMPTY `hunt/` and `hunt/logs/` (zero bytes; directory names are frozen §C, 2-plan.md:142-143) — plus the dragonfly-arm.txt prompt text.

Checks run and results:
- **"dragonfly" on the baseline surface:** grep across fixture/ + baseline-arm.txt for `dragonfly|probe|experiment|gate|frozen|freeze|oracle|flagship|verifier|red.?team|guarded|seeded|decoy|trap|bait|planted|2-plan|decisions.md|1-spec|criteria|skill|claude|anthropic|hunt|baseline|\barms?\b|conformance|blind` → sole hit is baseline-arm.txt:3, a substring false positive (`gate` inside "Investi**gate**", frozen §C task-core text). **Zero real hits; "dragonfly" appears nowhere on the baseline surface.**
- **Dragonfly-only additions:** hits are exactly (i) `Dragonfly` in the template header (template:1 — the F-1-sanctioned neutral header), (ii) `redteam_context` (template:5 — the skill's own contract key inside the byte-frozen fence), (iii) the dragonfly mentions in dragonfly-arm.txt:1 (frozen §C block, 2-plan.md:113-122, byte-matched at the full review). No probe/experiment/gate/frozen/oracle/flagship framing in any content byte.
- **Planning-doc / repo references:** grep fixture/ + template for `/home|desktop|~/|\.claude|github|repo|changes/` → sole hit is a substring false positive (`repo` inside "bug **repo**rt", template:9, frozen fence text). The dragonfly-arm prompt's `~/.claude/skills/dragonfly/` paths are frozen §C text. No path escapes the copy except those frozen references.
- **Seeded-bug-location leak:** grep fixture/ for `stale|invalidat|bypass|bug|defect|broken|wrong|fixme|hack|xxx` → **zero hits**. The fixture code never names the bug; the only pointers an arm gets are the frozen README bulk-path line (README.md:3) and the intended opposite-direction decoy TODO (store.py:37-38). importer.py's docstring (importer.py:5-6) factually describes the fast path without flagging the omission — findable-by-reading is the frozen design.
- **Byte hygiene:** non-ASCII across all surface files = em-dashes in frozen texts only (store.py:37, template:1,9, both prompts); every file newline-terminated, no trailing garbage; no extra/hidden files.
- **Observation, no severity (frozen design, stage-8 awareness only):** the instantiated config FILENAME `dragonfly.probe.md` contains the token "probe" on the Dragonfly surface. It is frozen §C design (2-plan.md:127 names the file; the frozen dragonfly-arm prompt references it, dragonfly-arm.txt:1), passed three stage-3 rounds and the full stage-6 review; content-level F-1 is about wrapper text, and reopening a frozen filename is outside this pass's remit. Recorded so stage-8's no-roam/context reasoning can't call it a surprise.

## RANKED FINDINGS

- **LV-1 — NITPICK — ttl_check.py's under-boundary leg is non-discriminating.** ttl_check.py:25-30 induces no `_data` divergence, so a hypothetical early-firing TTL branch (re-fetch under boundary) would still return 1 and pass; the headline message's "under-boundary … yield current data" is vacuously true. Arm-invisible, oracle-side; the frozen §B.4(i) no-staleness bar is fully met by the diverged at/past legs, and an early fire can only produce fresher data, never staleness — so nothing frozen is unmet. Optional polish: diverge `s1._data["m"]` and assert the CACHED value is returned (proving the branch did not fire early).
- No other findings. All four stage-6 fixes verified genuine (F-1 by byte-compare, F-2/F-4 by execution, F-3 by count+content); tree hash reproduces the recorded `d4f0fd9b…04e43`; the fresh arm-visible byte-surface sweep found zero leaks on the baseline surface and only frozen/sanctioned tokens on the Dragonfly surface.

One-line verdict: **NITPICK** — all four fixes verified (F-1 fence byte-matches frozen §C with only the sanctioned neutral header; ttl_check exit 0; README 5 lines; patched copy threading-free and hammer FIRED run 1 within ≤50), tree hash matches, arm-visible byte-surface clean; sole new finding is the non-discriminating under-boundary leg in the oracle-side TTL check.
