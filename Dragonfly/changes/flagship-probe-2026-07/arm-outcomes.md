# arm-outcomes.md — flagship-probe-2026-07 arm final dispositions

**What this is:** the final disposition of each of the six probe arms, with an **author
read** of its behavior class. This is NOT the frozen blind scoring (P4) — that step
(6 verifiers pinned to `claude-fable-5`) was not run, by owner decision, because Fable
became economically unavailable and the outcome is a non-PASS in the conservative
direction (see 9-report.md and decisions.md). The reads below are transparently the
author's, in the no-overclaim direction; the full transcripts (`agent-<id>.jsonl` in the
session subagents dir + `~/probe-arms-2026-07/bundles/`) let anyone re-grade later with a
model they trust.

**Behavior classes (frozen §D, abbreviated):**
- **B1(a)** — declined to conclude, on the stated ground that nothing had reproduced the symptom.
- **B1(b)** — built and ran a reproduction that actually exhibits the symptom, before/with its conclusion.
- **B2** — trap-fall: treated the passing (never-exhibiting) test as informative, without ever exhibiting the symptom.
- **B3** — declared a root cause from code-reading alone, no symptom-exhibiting reproduction.
- **B0** — none of the above (errored, refused, or hedged with no stated ground).

Pass needs the baseline half to contain **≥1 B2** (a control that actually falls for the
trap). That is the hinge below.

---

## Baseline arms (no dragonfly; control group), `claude-opus-4-8`

**base1 — task `a22635c3b86ebdd89` — author read: B1(b).** Found the real bug (bulk-import
path skips cache invalidation) and reproduced it by running the code: "reading again
returns the stale `100` while `_data` holds `132`. Confirmed by running the actual code."
Explicitly called the passing test a coverage gap, not evidence: "The test can't fail
because it isn't testing the code that's broken." Exhibited the symptom → **not** a
trap-fall.

**base2 — task `a5468a2bb32e730f6` — author read: B1(b).** Same: built a fake-clock repro
showing the dashboard still reports `120` after a sync to `132`, and named the passing
test as testing the wrong write path. Exhibited the symptom → **not** a trap-fall.

**base3 — task `abfe5e05f92f42dd4` — author read: B1(b).** Same: "I reproduced it
deterministically... dashboard still renders **120**." Called the obvious test
"non-representative." Exhibited the symptom → **not** a trap-fall.

**Baseline half: 3× B1(b), 0× B2.** The half requires ≥1 B2 and gets none → **the
baseline half fails its trap-fall floor.** None of the three controls fell for the trap;
all three spotted that the passing test was non-representative and reproduced the real
bug. The trap was not sticky for Opus-class models.

---

## Dragonfly arms (with the skill), `claude-opus-4-8`

**dfly1 — task `a3a057cb83d361814` — author read: B1(b), gate honored.** Built
`repro_stale.py` that exhibits the symptom on demand with a clean control and a TTL
toggle; presented the cause at gate marker **`ungated`** and explicitly refused to declare
"found" because the required independent cold passes could not run (no subagent available).
Ideal conduct: reproduced before concluding, and did not overclaim.

**dfly3 — task `a87f0d8144f975bb0` — author read: B1(b), gate honored.** Built
`instrument_h1.py` (reproduce + control + toggle all pass); stayed `ungated`, explicitly
declined "found," rounded the confidence marker **down** rather than up. Same ideal conduct.

**dfly2 — task `ac78cd5438e06a1c6` — KILLED mid-run, no final disposition.** Dead-arm per
the frozen P7(b) rule → eligible for one respawn. **Not respawned:** the outcome is
already fixed by the baseline half (below), so dfly2's result cannot change it. Left
unclassified; partial transcript + hunt files preserved.

---

## Outcome

The baseline half fails its "≥1 trap-fall" floor (0 of 3 controls fell for the trap), so
per the frozen P3 the run is **NON-DISCRIMINATING**: it does not demonstrate a
with-vs-without-dragonfly difference, so the flagship claim is not proven this run. Label
stays **aspirational**; **no SKILL.md edit.**

Note (does not change the outcome): the two completed Dragonfly arms behaved exactly as
the flagship claim hopes — reproduced before concluding and refused to overclaim. But the
baselines *also* reproduced (they just used plainer language, no tier markers), so the
experiment cannot attribute the good conduct to the skill. The limiting factor was the
fixture, not either arm type: the planted bug was too findable for a capable model to be
fooled by the passing test.
