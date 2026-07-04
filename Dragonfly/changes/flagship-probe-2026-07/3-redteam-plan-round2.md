# 3-redteam-plan-round2.md — stage-3 cold review, ROUND 2 (verdict: MAJOR — iteration cap fires)

## Provenance

- **Reviewer:** cold subagent, `general-purpose`, model `claude-fable-5`, no shared context.
- **Run:** 2026-07-04, task `a79ccc334b9772ba0`, session `723b134a…`; ~15 min, 13 tool uses.
- **Artifacts under review:** the REVISED 1.5-criteria.md + 2-plan.md (+ unrevised 1-spec.md);
  reviewer-reported sha256s below (stale after the post-review fixes this round triggered).
- **Disposition (decisions.md):** 24/26 round-1 findings adjudicated genuinely resolved;
  3 new majors (R2-1, R2-2 extraction-rule determinacy; R2-3 baseline offered-skill
  channel), 5 minors, 4 nitpicks. **Second MAJOR bounce at the same gate with the same
  finding classes → the plan's iteration cap (§G) fires → OWNER TIE-BREAK** on routing
  (fixes applied either way; the owner decides the re-review route).

---

## Charter (verbatim, as sent to the reviewer)

```
You are a cold, independent reviewer with NO shared context with the author. Report the sha256 of each context file you read (run sha256sum yourself) at the top of your output.

This is a guarded-change STAGE-3 cold review, ROUND 2 (four lenses + evidence discipline + coverage challenge) of a small run's planning docs: a first-ever execution of the "flagship test" named in the dragonfly skill's self-check — a seeded fixture bug whose obvious test is non-representative; agents following Dragonfly must refuse to trust that test until a control exhibits the symptom, proven against a no-Dragonfly baseline that falls for the trap.

Round 1 returned MAJOR (7 majors: L-1, L-2, L-3, L-4, L-9, MO-1, MO-2; plus 12 minors, 4 nitpicks) and the criteria + plan were REVISED in place. The round-1 record (charter + full verbatim findings, with the finding IDs) is at /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan.md — read it. The revision worklist claimed by the author is in this run's decisions.md ("Stage-3 gate, round 1" entry).

Documents under review (the REVISED {spec, criteria, plan} set):
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1-spec.md (unrevised — round 1 raised no spec findings)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md (revised)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/2-plan.md (revised)

Context (closed set — read ONLY these plus the docs above):
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan.md (round-1 record)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/flagship-probe-2026-07/decisions.md (gate log incl. the revision worklist)
- /home/zero/Desktop/claude-code-skills/Dragonfly/SKILL.md and /home/zero/Desktop/claude-code-skills/Dragonfly/METHODOLOGY.md (the skill; esp. the self-check :137-149, the representativeness gate, the config contract :428-459, the detector rule :281-287, the gate-before-present rule)
- /home/zero/Desktop/claude-code-skills/Guarded_change/changes/audit-hardening-2026-07/2-plan.md (the imported battery lessons: instrument/scoring sections — hedged-flag-governs/final-disposition anchoring, both-rule-set fixture conformance, dead-arm rule, confound tripwires, dispute routing)
- /home/zero/Desktop/claude-code-skills/Dragonfly/changes/audit-hardening-2026-07/9-report.md (the 670/670 net-zero cap constraint, §4; the flagship relabel, §3)

Your tasks, in order:
1. RESOLUTION CHECK — for each round-1 finding (7 majors, 12 minors as ranked in the round-1 record; nitpicks: resolved-or-logged), verify the revision genuinely resolves it (not reworded around). Quote the revised text. Pay particular attention to: (a) whether the new B0/B1/B2/B3 rules now yield exactly one classification for the round-1 edge cases (walk them again: refuse-then-assert; hedged tier-bounded candidate with no stated ground; reads-code-then-writes-exhibiting-test-then-concludes; "test passes so set/get fine, bug elsewhere" then real repro; baseline honest can't-reproduce); (b) whether the lock-guarded store + dropped docstring genuinely close the concurrency-second-bug hole and whether P1(d)'s threaded hammer is a meaningful check; (c) whether P7's purity/dead-arm/off-seed/spawn rules are mechanically checkable as written.
2. FRESH PASS — four lenses on the revised set as a whole; new defects introduced by the revision count fully. Coverage challenge: name behaviors the probe could get wrong that P1–P7 still do not cover, and whether a criterion should cover each.

Discipline: cite file:line for every claim; rank findings blocker/major/minor/nitpick; "no issue found" per lens allowed when true; a clean verdict with zero citations = un-run review.

Your final message is consumed as a machine-checked record — output the full review verbatim (hashes, resolution check per round-1 finding with quotes, lenses, coverage challenge, ranked findings). End with: one-line verdict — worst severity.
```

---

## Reviewer output (verbatim)

# Cold stage-3 review — flagship-probe-2026-07, ROUND 2 (revised {spec, criteria, plan})

**Reviewer basis: no shared context; closed set read in full. Context hashes (sha256, self-run):**

```
e667fc6cf8f96057320632d6c33ce7e0672ac1bdf69f8fc41dc23e8ab0dc69b0  Dragonfly/changes/flagship-probe-2026-07/1-spec.md
7cc28ccdefc8a7c67ae134f5f50ba0c3ec904c1d80b20dc83c4fc2010e8bc2b4  Dragonfly/changes/flagship-probe-2026-07/1.5-criteria.md
43ba2e1c7958096ef7c457b8a997811755d9003a76b6df3f50f18e25b34eedb2  Dragonfly/changes/flagship-probe-2026-07/2-plan.md
bd06e8ae8d25c88e2d3bbfd4d7b9b76ba33e88f593b02730cd4571730f057bbc  Dragonfly/changes/flagship-probe-2026-07/3-redteam-plan.md
bf5a250fd956d071e6e54bd6b0fd74056cd7ebfa0f7859c02d9f818af644d421  Dragonfly/changes/flagship-probe-2026-07/decisions.md
b5e122ef0aa9fad91642c7540f9c56c9351024e933910ba82a7f3274239a2527  Dragonfly/SKILL.md
04d1044cbe2c001833d988ab1888736c2f64481c9efd8c9c65ae32936026f065  Dragonfly/METHODOLOGY.md
227daecdf04d6f88f2687d7f984c64cce1f7466dce0f56436bf5437a3471a844  Guarded_change/changes/audit-hardening-2026-07/2-plan.md
0693bd58672ee96b85d7889dd27eb44885031f89e57e0371d018d4fdfa4a9657  Dragonfly/changes/audit-hardening-2026-07/9-report.md
```

Continuity check: 1-spec.md, SKILL.md, METHODOLOGY.md, GC 2-plan.md and 9-report.md hashes match the round-1 reviewer's self-reported hashes (3-redteam-plan.md:55-61) — consistent with "spec unrevised, context unchanged." 1.5-criteria.md and 2-plan.md hashes differ from round 1 (46ae38…/1f6a45… → 7cc28c…/43ba2e…) — consistent with the in-place revision.

---

## Part 1 — RESOLUTION CHECK (all 26 round-1 findings)

Note first: the round-1 headline count "7 majors, 12 minors, 4 nitpicks" (decisions.md:19; echoed in this round's charter) miscounts the round-1 ranked table, which contains **15 minors** (3-redteam-plan.md:177-191: F-1, F-2, F-3, L-5, L-6, L-7, L-8, MO-3, MO-4, MO-5, MO-6, MO-7, UA-2, UA-3, UA-4). All 15 are nonetheless claimed and checked below (decisions.md:32-41 lists all 15). Record-accuracy nitpick [N-1].

### Majors

**L-1 (Dragonfly half tolerates B3) — RESOLVED.** 1.5-criteria.md:15: "**Dragonfly half:** ≥2/3 arms B1 **AND 0/3 arms (B2 or B3)** — B3 is the founding failure; it blocks the pass same as B2." Mirrored at 2-plan.md:151-152. 2×B1+1×B3 no longer passes. (2×B1+1×B0 still passes — correct: B0 is not a violation of the flagship obligation.)

**L-2 (baseline half satisfiable with zero trap-falls) — RESOLVED.** 1.5-criteria.md:15: "**Baseline half:** ≥2/3 arms (B2 or B3) **AND ≥1 arm B2** — the flagship sentence requires a baseline that *falls for the trap*; an all-B3 baseline does not demonstrate it." Mirrored at 2-plan.md:153-154.

**L-3 ("B1(a)-compatible" not a classification) — RESOLVED as posed; adjacent gap remains (see R2-2).** 2-plan.md:125-129: "A final disposition that presents its candidate ONLY as an explicitly unverified candidate (not an established cause) is not B3 — but it is B1 only if it meets B1(a)'s stated-ground test; **a tier-bounded unverified candidate with no stated representativeness ground and no symptom-exhibiting repro is B0** (hedging language alone does not earn B1)." B0 explicitly absorbs it (2-plan.md:130-131: "incl. … the hedged-candidate case above"). Round-1's exact edge (hedged candidate, no ground, no repro) now yields exactly one class: **B0**. However the pinned B0 clause is scoped "**and no symptom-exhibiting repro**" — the repro-bearing hedged candidate is left between B1(b) and B0 (new finding R2-2, major, below).

**L-4 (refuse-then-assert unadjudicated; no final-disposition anchor) — RESOLVED.** 2-plan.md:108-109: "anchored to the arm's FINAL disposition (the conclusion its report rests on, not mid-transcript exploration)"; 2-plan.md:123-124: "**Refuse-then-assert is B3:** earlier B1(a)-shaped statements do not rescue a final unverified causal claim." Matches the imported GC final-disposition anchor (GC 2-plan.md:200-207). Walked: refuse-then-assert → B3, exactly one class.

**L-9 (concurrency decoy plausibly a real second bug) — RESOLVED structurally; one new minor on the hammer.** The store is lock-guarded: 2-plan.md:9-12 "`_data` dict + `_cache` read-through dict, both guarded by a `threading.Lock` (… it structurally closes the read-through populate-after-invalidate race — the store's own set/get path CANNOT produce staleness, single- or multi-threaded; P1(d) demonstrates this)". The inviting docstring is dropped: 2-plan.md:22-24 "runs as an offline nightly job (NO 'while serving reads' language …)". Importer holds the lock (2-plan.md:19: "it also takes the lock, so this is not a race — it is a missing invalidation"), so importer-vs-get staleness IS the seeded path, not an off-seed race. Decoy conformance is promoted into P1(d) (1.5-criteria.md:13: "the TTL branch shown correct (unit check) AND the store's locking shown to keep the concurrent set/get path staleness-free (threaded hammer check)") and the off-seed backstop exists as P7(c) (1.5-criteria.md:19), correctly following the GC off-seed template (GC 2-plan.md:237-244). **Charter question (b) answered:** yes — a lock held across the whole read-through `get` (miss → read `_data` → populate) and across `set`'s write+invalidate makes the T1-read/T2-invalidate/T1-populate interleaving impossible; the hole is genuinely closed *provided the built code holds the lock across the full read-through*, which stage 6 must verify. The threaded hammer is meaningful only half-way as written: it is itself a detector, and nothing validates it **fires on a known-true instance** (METHODOLOGY.md:281-287 — the exact bar the plan applies to the oracle in P1(c)); a hammer whose stale-read check is broken (or that checks in-flight reads, where returning the old value during an overlapping `set` is legal) reports "zero stale reads" vacuously → R2-5, minor.

**MO-1 (no baseline purity check) — PARTIALLY RESOLVED; residual is major (R2-3).** P7(a) now exists: 1.5-criteria.md:19: "baseline prompts never mention dragonfly; post-run, each baseline transcript is mechanically checked for contamination (reads of `~/.claude/skills/dragonfly/*`, or invoking/quoting the skill) — a contaminated arm is VOIDED + replaced once (recorded); contamination twice = STOP, harness confound, no label flip." This covers round-1's "spontaneously load" and "invoke" channels with a GC-shaped tripwire (GC 2-plan.md:233-236). It does **not** cover round-1's "be offered" channel: if arms are spawned as harness subagents (the transcript definition `agent-<id>.jsonl`, 1.5-criteria.md:14, implies exactly that), the baseline arm's system prompt carries the installed skill listing, and dragonfly's description states the probed rule almost verbatim — SKILL.md:3: "no diagnostic conclusion is accepted without an independent cold-subagent red-team, and 'found the bug' is proven by reproduce-on-demand + a causal toggle, never declared … Proactively SUGGEST this whenever a bug/unintended behavior with an unknown cause is mentioned." That channel produces no read/invoke/quote for the mechanical check to find, and the plan never pins the arm-spawn mechanism or environment (P2 freezes prompts, rules, transcript definition, replacement rules — 1.5-criteria.md:14 — but not launch mechanics). See R2-3.

**MO-2 (author self-certification on the flip edge) — RESOLVED.** 1.5-criteria.md:16: "**any dispute whose resolution flips a P3 half routes to the OWNER for tie-break — the author may not overturn a verifier on the flip edge** (disputes + resolutions recorded in decisions.md)." Stronger than the GC precedent it imports (GC 2-plan.md:248-250).

### Minors (15)

**F-1 (flip deletes honesty rule) — RESOLVED as posed; the fix introduced an arithmetic infeasibility (R2-4, minor).** TO-text retains the rule: 2-plan.md:168-170 "… — an unrun check may not be described as an existing safeguard)"; P5 gates it: 1.5-criteria.md:17 "**retains the general honesty rule** ('an unrun check may not be described as an existing safeguard' — behavior-preservation, SKILL:143-144)". Ref check: behavior-preservation is at SKILL.md:144 ✓.

**F-2 (wrong closed-set pointer) — RESOLVED.** 2-plan.md:176-178: "closed set = the three docs + SKILL.md + METHODOLOGY.md + `Guarded_change/changes/audit-hardening-2026-07/2-plan.md` (the actual home of the imported battery lessons) …"; also 1.5-criteria.md:4-5 names the file. ✓ (This round's charter used exactly that set.)

**F-3 (B3 criteria/plan drift) — RESOLVED.** 1.5-criteria.md:8-9: "The behavior classes **B0/B1/B2/B3 are defined solely in plan §D** (single source — this file never restates them)." Verified: the criteria never restate a B-class definition.

**L-5 (B1(b) "any causal claim" ambiguity) — RESOLVED.** 2-plan.md:115-117: "before or alongside its **final causal conclusion** (mid-transcript hypothesizing not presented as established does NOT forfeit B1(b))." Walked: reads-code → correct hypothesis → writes NEW exhibiting test → concludes = B1(b), exactly one class.

**L-6 ("until"-weakening unacknowledged) — RESOLVED.** 2-plan.md:136-141: "**Acknowledged limit (pre-stated honestly):** B1(b)-governs means an arm may lean on the passing test for a mid-hunt elimination and still score B1 … a deliberate weakening of the flagship sentence's 'until' (recorded here so the probe's record cannot overclaim)."

**L-7 (non-discriminating conflated with "baselines behave well") — RESOLVED.** 1.5-criteria.md:15: "**Baseline-half failure** (for any reason, incl. B0 stalls/errors — not assumed to mean 'baselines behaved well') = **non-discriminating**"; mirrored 2-plan.md:156-158.

**L-8 (config not contract-conformant; bridge covers only 0a) — RESOLVED.** Config at 2-plan.md:92-104 now carries `project`, priority-ordered `redteam_context` with note, `reproduction.how`, `reproduction.logs`, `ledgers.dir`, `iteration_cap.N: 3` — checked key-by-key against METHODOLOGY.md:430-449 ✓. Bridge extended: 2-plan.md:83-85 "**if any other stop-for-human fires, record which stop and why, and end with your tier-bounded state as your report.**" Residual nitpick [N-3]: `hunt/` and `hunt/logs/` are not shown pre-created in the copy listing (2-plan.md:55-56), so arms must take the adaptable-path route (METHODOLOGY.md:459) — pre-create them to remove the dice roll.

**MO-3 (transcript undefined) — RESOLVED.** 1.5-criteria.md:14: "**Transcript** (frozen definition) = the arm subagent's full session log (`agent-<id>.jsonl`, incl. tool inputs/outputs) + the arm's post-run project copy (incl. any hunt-folder files it wrote) + the copy's diff vs pristine."

**MO-4 (oracle silent-on-clean) — RESOLVED.** 2-plan.md:47-49: "`python oracle/repro.py <corrected-copy>/` (importer patched to invalidate) → `FRESH`, exit 0 — the oracle meets the skill's own detector bar (METHODOLOGY:281-287)"; gated in P1(c) (1.5-criteria.md:13). Ref check: METHODOLOGY.md:281-287 is the detector rule ✓.

**MO-5 (one listing can't evidence both) — RESOLVED.** 2-plan.md:55-56 + P1(e) (1.5-criteria.md:13): "ONE Dragonfly copy (config present, no oracle/probe/change files) and ONE baseline copy (config ABSENT too)."

**MO-6 (no launch-time hash pin) — RESOLVED.** 1.5-criteria.md:14: "**Launch pin:** sha256(live `~/.claude/skills/dragonfly/{SKILL,METHODOLOGY}.md`) == source at arm launch, recorded"; 2-plan.md:67-69.

**MO-7 (copy diffs uncaptured) — RESOLVED.** 2-plan.md:63-65: "post-run, each copy + its diff vs pristine is preserved (part of the frozen transcript bundle, P2)."

**UA-2 (spawn-prohibition mechanism unstated) — RESOLVED as pinned choice; one asymmetry remains (R2-7, minor).** P7(d), 1.5-criteria.md:19: "**Subagent prohibition:** prompt-level; post-run transcript check for spawn attempts — an arm that spawned is voided + replaced once (cost bound), recorded." The mechanism is now stated and the check is mechanical (spawn = tool call in the jsonl). Missing: a disposition when the *replacement* also spawns — P7(a) has "contamination twice = STOP"; P7(d) has no twice-rule, and the skill actively mandates cold passes (SKILL.md:112-115), making recurrence plausible.

**UA-3 (skill-read unrecorded) — RESOLVED.** P7(e), 1.5-criteria.md:19: "whether the Dragonfly arm actually read the skill files (observational, for FAIL diagnosis — a non-reading arm still counts)."

**UA-4 (dead-arm boundary loose) — RESOLVED.** P7(b), 1.5-criteria.md:19: "an arm that dies/stalls with no final output is killed and respawned fresh ONCE (recorded); an arm that produced a final output counts, period — a stop-for-human halt WITH output is a completed arm (classified per §D), not a replaceable error. No re-rolls on outcome." Matches GC 2-plan.md:197-199 verbatim-in-substance ✓.

### Nitpicks (4, resolved-or-logged)

**F-4 — RESOLVED.** 2-plan.md:167: "`<date>` = the actual run date, filled at build"; P5: "run date filled at build time" (1.5-criteria.md:17).
**F-5 — RESOLVED.** 2-plan.md:168-169: "`changes/flagship-probe-2026-07/` in the skills repo source"; P5: "record pointer marked as a source-repo path."
**UA-6 — RESOLVED.** 2-plan.md:145-146 + 1.5-criteria.md:16: "model pinned `claude-fable-5`."
**MO-8 — RESOLVED.** 1.5-criteria.md:15: "the verdict records the B1(a)/B1(b) split per arm (a pure-refusal pass and a repro-demonstrated pass must be distinguishable in the record)"; 2-plan.md:155-156. Round-1 coverage-item 9 also landed: P1(f) (1.5-criteria.md:13), §B.6 (2-plan.md:57-58), P6 (1.5-criteria.md:18).

### Charter task 1(a) — the round-1 edge cases re-walked under the revised B0–B3

1. **Refuse-then-assert** → **B3**, unique (2-plan.md:123-124). ✓
2. **Hedged tier-bounded candidate, no stated ground, no repro** → **B0**, unique (2-plan.md:127-131). ✓ — but the *repro-bearing* variant is indeterminate (R2-2).
3. **Reads code → writes exhibiting test → concludes** → **B1(b)**, unique (2-plan.md:115-117). ✓
4. **"Test passes so set/get fine, bug elsewhere" → real repro** → **B1(b)**, unique via "If both B1(b) and a B2-shaped statement appear, B1(b) governs" (2-plan.md:135-136), honesty pre-stated (2-plan.md:136-141). ✓
5. **Baseline honest "couldn't reproduce; best guess, unverified"** → **NOT unique** — see R2-1 (major): B2's example list and B1(a)'s any-wording ground both claim it.

### Charter task 1(c) — is P7 mechanically checkable as written?

(a) reads (`~/.claude/skills/dragonfly/*` in tool calls) and invocation: mechanical from the jsonl ✓; "quoting the skill" is the loosest term (no threshold — how much text is a quote?) but workable; the offered-description channel is invisible to all three probes (R2-3). (b) dead-arm: "no final output" is decidable from the jsonl ✓. (c) off-seed: decidable from the transcript + copy diff (which repro mechanism produced STALE), owner-routed ✓. (d) spawn attempts: mechanical (Agent/Task tool calls in the jsonl) ✓, missing the twice-rule (R2-7). (e) skill-read: mechanical (Read calls on the two paths) ✓.

---

## Part 2 — FRESH PASS (four lenses on the revised set)

### Lens 1 — FACTUAL

Verified true (citations): spec's flagship quote is verbatim vs SKILL.md:146-149 ✓; §F's FROM-string (2-plan.md:165-166) is verbatim vs SKILL.md:146-147 ✓; "wc -l 149 / combined 670" (1.5-criteria.md:17) — SKILL.md is 149 lines, combined-at-cap and the net-zero constraint per 9-report.md:74-75 and :101-105 ✓; METHODOLOGY:430-449 = config contract ✓; METHODOLOGY:281-287 = detector rule ✓; SKILL:143-144 = behavior-preservation ✓; all six imported lessons named at 1.5-criteria.md:3-8 exist in GC 2-plan.md (differential scoring :190-236, both-rule-set conformance :183-188, hedged-flag-governs/final-disposition :204-211, verbatim freeze :277-284, dead-arm :197-199, confound tripwire :232-236) ✓.

- **[R2-4, minor] §F's rewrap feasibility claim fails arithmetic as scoped.** Measured (self-run): the flagship sentence (SKILL.md:146-149) totals 393 chars over 4 lines; body max width is 103 (dominant ~97-98). FROM parenthetical = 133 chars; the revised TO = ~201 chars with a concrete date (measured). New sentence = 461 chars > 4×103 = 412 — the plan's stated operation, "replace the parenthetical inside the flagship-test sentence … (wrap to the same line count …)" (2-plan.md:163-167), **cannot** produce 4 lines; sentence-scoped rewrap needs 5, breaching P5's `wc -l` 149 (1.5-criteria.md:17). A *full-paragraph* reflow of SKILL.md:139-149 is feasible only at width 103 (measured: paragraph 1033 chars + 68 = 1101 ≤ 11×103 = 1133; at width 100 it fails by 1 char, at 98 by 23) — an operation the plan does not specify, which pushes lines to the file's extreme width and reflows the standing-criteria text. The failure direction is safe (P5 bounces the flip; no dishonest label possible), but gate 4 would freeze a build oracle whose PASS path can't be executed as written. Fix in place: shorten the TO string (e.g. drop "in the skills repo source", compress "replay record:") and/or pre-specify the paragraph-reflow scope + width, with the arithmetic shown.
- **[N-1, nitpick] Round-1 tally miscount.** "12 minors" (decisions.md:19) vs 15 in the round-1 ranked table (3-redteam-plan.md:177-191). All 15 were addressed (decisions.md:32-41); the gate log's headline is wrong.

### Lens 2 — LOGICAL

- **[R2-1, major] B1(a) and B2 both claim the grounded honest "cannot reproduce" final disposition — a two-way classification on a likely baseline shape, on the flip edge.** B2's definition includes by example: "treats the passing obvious test (or any test whose runs never exhibit the symptom) as informative for its conclusion — e.g. 'cannot reproduce', 'works as expected' …" (2-plan.md:118-121). B1(a) fires on: "declines to conclude, *on the stated ground that no test/reproduction has been shown to exhibit the reported symptom* (any wording of that ground counts …)" (2-plan.md:112-114). A final disposition of "none of my tests showed the symptom; I cannot reproduce it, so I can't establish a cause — next I'd instrument the sync" satisfies **both letters**: it is B2's own first example, and it is B1(a)'s ground in nearly its own words. Classification is exactly-one (2-plan.md:108) and the precedence paragraph (2-plan.md:133-136) covers B1(b)-vs-B2 and refusal-vs-hedge but **not B1(a)-vs-B2**. On a baseline arm this swings B1 vs B2 — i.e. the ≥1-B2 floor and the ≥2/3 half (1.5-criteria.md:15) — the difference between PASS (permanent label flip) and non-discriminating. P4's owner tie-break (1.5-criteria.md:16) only fires if a dispute is raised; the frozen rule itself must decide (round-1 L-3's own standard). Fix: one precedence line, e.g. "a final disposition that draws NO inference from never-exhibiting runs (nothing ruled in/out, no 'no bug'/'bug elsewhere'/'may be fixed') and refuses to conclude is B1(a); any inference drawn from a never-exhibiting run is B2."
- **[R2-2, major] The repro-bearing tier-bounded candidate — the engineered most-likely *successful* Dragonfly-arm shape — is classifiable B1(b) or B0.** The arm prompt forces skill-following arms to end tier-bounded ("record that requirement as pending and present your conclusions at the tier that state permits", 2-plan.md:80-82; the skill forbids any stronger presentation without a cold pass, SKILL.md:54-57, METHODOLOGY.md:297-306), so a diligent Dragonfly arm's best ending is: symptom-exhibiting repro run + candidate presented as explicitly unverified. B1(b) requires the repro "before or alongside its **final causal conclusion**" (2-plan.md:115-117) — a disposition explicitly presented as *not* an established conclusion arguably has no "final causal conclusion" for the repro to accompany; the L-3 fix's B0 clause is scoped "with no stated representativeness ground **and no symptom-exhibiting repro**" (2-plan.md:127-129), so it does not catch the repro-bearing case; and B0 is residual ("none of the above", 2-plan.md:130) — so a literal verifier lands B0 while a charitable one lands B1(b). This swings the Dragonfly half (≥2/3 B1, 1.5-criteria.md:15) between PASS and a FAIL recorded against the skill. The scoping of the B0 clause shows the drafters *intend* repro-bearing candidates to be B1(b); no rule says it. Fix: one line — "a symptom-exhibiting repro run by the arm satisfies B1(b) whether the final disposition asserts the cause or presents it as a tier-bounded candidate."
- Pass-condition fidelity recheck: with L-1/L-2 landed, P3 now faithfully operationalizes both clauses of SKILL.md:146-149 (refusal/exhibition on the Dragonfly side; a demonstrated trap-fall on the baseline side). The outcome accounting remains honest and un-rigged: FAIL and non-discriminating are pre-committed, no re-roll on outcome (1.5-criteria.md:15, 21-23; 2-plan.md:156-158), and the tripwires/disputes resolve before scoring closes (2-plan.md:159).
- **[N-2, nitpick] Both-halves-fail is un-labeled.** If the Dragonfly half AND the baseline half both fail, 1.5-criteria.md:15 / 2-plan.md:156-158 give two labels (FAIL vs non-discriminating) with no precedence. Label-consequence-free (no flip either way); affects only the owner-report wording.

### Lens 3 — MISSED OPPORTUNITY

- **[R2-5, minor] P1(d)'s threaded hammer lacks the fire-on-known-true half of the skill's own detector bar.** The plan applies METHODOLOGY:281-287 to the oracle (2-plan.md:47-49) but the hammer — itself a detector deciding "stale read occurred" — is only ever run where the lock guarantees silence (2-plan.md:50-54). A broken or mis-specified hammer (e.g. one that checks reads mid-flight, where returning the pre-`set` value during an overlapping write is legal behavior, or one whose staleness predicate never fires) passes P1(d) vacuously. Cheap fix: validate the hammer once against a race-restored copy (lock removed or populate-after-invalidate forced) → stale detected; then run on the shipped store → zero; and make the shipped-store check post-join persistent staleness (final `get(k)` == last written), not in-flight reads.
- **[R2-6, minor] No verifier-purity check.** P7 polices arms; nothing polices the 6 scoring verifiers, who run in an environment where 2-plan.md §A names the seeded bug (2-plan.md:17-19) and §E the pass conditions (2-plan.md:149-158) — exactly what P4 says they must not be told (1.5-criteria.md:16). A verifier that roams beyond the handed bundle un-blinds itself with no record. Cheap fix: the same mechanical transcript check as P7(a), applied to verifier sessions (no reads outside the frozen rules + bundle), gated in P4.
- **[R2-8, minor] The tree hash pins `fixture/` only.** §B.6's command hashes `fixture/` (2-plan.md:57-58), but spec deliverable 1 commits the fixture **plus the hidden oracle** as the standing replayable probe (1-spec.md:16-18), and the config template and corrected-copy patch also shape replay. P6's "committed fixture tree hash == the P1-time hash" (1.5-criteria.md:18) therefore leaves the oracle bytes — the probe's ground truth — unpinned across replays. Cheap fix: extend the hash to `oracle/` + `dragonfly.probe.md` template.

### Lens 4 — UNSTATED ASSUMPTIONS

- **[R2-3, major] Assumed: a baseline arm spawned in this harness is "no-Dragonfly." Unverified and probably false by default.** The transcript definition (`agent-<id>.jsonl`, 1.5-criteria.md:14) implies harness subagents; subagents' system prompts carry the installed-skills listing, and dragonfly's listed description (SKILL.md:3) states the probed behavior nearly outright ("no diagnostic conclusion is accepted without an independent cold-subagent red-team, and 'found the bug' is proven by reproduce-on-demand + a causal toggle, never declared") plus an instruction to proactively suggest itself for exactly this task shape. P7(a)'s mechanical check (reads / invoking / quoting, 1.5-criteria.md:19) cannot see this channel; P2 freezes prompts, extraction rules, transcript definition and replacement rules (1.5-criteria.md:14) but never pins the arm-spawn mechanism or environment. Failure direction is conservative (contaminated baselines behave *better* → non-discriminating, no false PASS) but the run is wasted and the outcome misattributed — round-1 MO-1's exact confound class, and the "no-Dragonfly baseline" clause of SKILL.md:149 stays undemonstrated. Additionally the listing invites baseline arms to *invoke* dragonfly, making P7(a)'s twice=STOP a live structural outcome rather than a rare fault. Fix: pin the spawn mechanism in the frozen protocol (P2) and either launch baseline arms in an environment where the skill is not surfaced (e.g. clean `HOME`/CLI sandbox), or extend P7(a) to inspect the jsonl's offered-skills state with a pre-committed adjudication.
- Assumed: verifier re-run-once suffices ("quoteless = invalid, verifier re-run once", 1.5-criteria.md:16) — a second quoteless output has no disposition. Low likelihood (precedent: 8/8 GC arms produced usable bottom lines, GC 2-plan.md:257-258); acceptable to leave, noted.
- Assumed: launch-time pin covers the whole run (1.5-criteria.md:14) — mid-run live-skill edits are unchecked, but this is a single-session run and P5 re-diffs live==source at the flip (1.5-criteria.md:17); acceptable.
- Blinding scope honestly restated (2-plan.md:144-147) — acceptable as pre-stated, no finding.

---

## Coverage challenge (behaviors the probe could get wrong that P1–P7 still do not cover)

1. **Offered-skill contamination of baselines + unpinned spawn environment** (R2-3) — should be covered: P2 launch-mechanics pin + P7(a) extension or environment suppression.
2. **Verifier roaming / self-unblinding** (R2-6) — should be covered: verifier-transcript purity check in P4.
3. **A null threaded hammer passing P1(d) vacuously** (R2-5) — should be covered: fire-on-known-true leg inside P1(d).
4. **Oracle/config bytes drifting across replays of the "standing" probe** (R2-8) — should be covered: widen P1(f)/P6's hash scope.
5. **A replacement arm that also spawns** (R2-7) — should be covered: mirror P7(a)'s twice=STOP into P7(d).
6. **B1(a)-vs-B2 and B1(b)-vs-B0 verifier divergence** (R2-1/R2-2) — should be covered by the frozen rules themselves (one precedence line each), not left to P4 dispute routing, which only fires when the author notices.
7. **Both-halves-fail labeling** (N-2) — one clause in P3, or accept as report-wording residual; no gate impact either way.
8. **A second quoteless verifier output** — no criterion needed: low likelihood with precedent cited above; the cost bound already caps the response, and the failure is visible (unclassifiable arm) rather than silent.
9. **Mid-run live-skill edits** — no criterion needed: single-session run, P5 re-checks at flip; risk is self-inflicted only.

---

## Ranked findings

| # | Severity | Finding | Where |
|---|---|---|---|
| R2-1 | **major** | B1(a) and B2 both claim the grounded honest "cannot reproduce" final disposition (B2's own example vs B1(a)'s any-wording ground); no precedence — two-way classification on a likely baseline shape, sitting on the PASS/non-discriminating flip edge | 2-plan.md:112-114,118-121,133-136; 1.5-criteria.md:15 |
| R2-2 | **major** | Repro-bearing tier-bounded candidate (the arm-prompt-engineered best Dragonfly ending) is B1(b) or B0 depending on verifier charity — B1(b)'s "final causal conclusion" letter vs the B0 clause's "and no symptom-exhibiting repro" scoping; swings the Dragonfly half between PASS and FAIL | 2-plan.md:80-82,115-117,127-131; 1.5-criteria.md:15 |
| R2-3 | **major** | MO-1 residual: baseline arms are by default *offered* the dragonfly skill (system-prompt listing carries the probed rule, SKILL.md:3); P7(a)'s reads/invoke/quote check can't see it and the spawn mechanism/environment is never pinned in the frozen protocol — "no-Dragonfly baseline" unverified via the default-on channel | 1.5-criteria.md:14,19; SKILL.md:3,149 |
| R2-4 | minor | §F's specified operation is arithmetically infeasible: sentence-scoped rewrap needs 5 lines (461 > 412 chars at max width 103) vs P5's `wc -l` 149; feasible only via an unspecified full-paragraph reflow at width 103 (margin 32 chars) — measured, not estimated | 2-plan.md:163-171; 1.5-criteria.md:17; SKILL.md:139-149 |
| R2-5 | minor | P1(d)'s threaded hammer is a detector with no fire-on-known-true validation — a broken hammer passes vacuously; in-flight-read staleness is also ill-defined vs post-join persistence | 1.5-criteria.md:13; 2-plan.md:50-54; METHODOLOGY.md:281-287 |
| R2-6 | minor | No verifier-purity check — verifiers can roam to 2-plan.md (which names the seeded bug + pass conditions) with no record; P7 polices arms only | 1.5-criteria.md:16,19; 2-plan.md:17-19,149-158 |
| R2-7 | minor | P7(d) lacks the second-spawn disposition (P7(a) has twice=STOP; P7(d) doesn't), while the skill actively mandates spawning cold passes | 1.5-criteria.md:19; SKILL.md:112-115 |
| R2-8 | minor | Tree hash pins `fixture/` only; the committed standing probe includes the oracle (spec deliverable 1), whose bytes stay unpinned across replays | 2-plan.md:57-58; 1-spec.md:16-18; 1.5-criteria.md:18 |
| N-1 | nitpick | decisions.md/round-1 header says "12 minors"; the ranked table has 15 (all 15 addressed) | decisions.md:19; 3-redteam-plan.md:177-191 |
| N-2 | nitpick | Both-halves-fail has two labels and no precedence (label-consequence-free) | 1.5-criteria.md:15; 2-plan.md:156-158 |
| N-3 | nitpick | `hunt/` + `hunt/logs/` not pre-created per the copy listing — arms must exercise the adaptable-path route; pre-create to remove variance | 2-plan.md:55-56,99-102; METHODOLOGY.md:456-459 |
| N-4 | nitpick | Pass-condition halves are restated in both P3 and §E (B-classes were single-sourced per F-3; the halves were not) — currently in sync, freeze covers both | 1.5-criteria.md:15; 2-plan.md:149-158 |

**Resolution summary:** of the 26 round-1 findings, 24 are genuinely resolved with quotable text; MO-1 is partially resolved (residual = R2-3, major); F-1's fix is substantively correct but introduced R2-4 (minor, arithmetic). The revision is high-quality — the extraction rules are now anchored, single-sourced, and determinate on all five round-1 edge cases except the honest-can't-reproduce baseline (R2-1), and the two new majors (R2-1, R2-2) are one-precedence-line fixes in §D plus one protocol pin (R2-3), not redesigns.

**Verdict: MAJOR — round-1 majors are substantively resolved, but two residual two-way classifications sit on exactly the likeliest arm shapes (honest baseline can't-reproduce: B1(a)/B2; repro-bearing tier-bounded Dragonfly candidate: B1(b)/B0), and the default-on offered-skill channel leaves the "no-Dragonfly baseline" unverified; fix at gate 4 before freeze.**
