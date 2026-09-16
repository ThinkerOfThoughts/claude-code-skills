# Stage 3 — Red-team the plan, PASS 2 (VERBATIM RECORD)

**Run:** `charter-2026-07`. Cold review of the **revised** `{0-baseline, 1-spec, 1.5-criteria, 2-plan,
decisions}` after gate-4 pass 1 returned a blocker.

Verbatim record per B15. Author's interpretation lives in `decisions.md`. All five provenance elements:

## (i) The verbatim charter/prompt given

`records/stage3-pass2-prompt.md`, sha256 `62a6781b79935d4392d65a32a3520e653d9422cc0c9ebbf2060203d355b5d4fa`.
**All three reviewers received byte-identical text**, written to disk first; each was told only to read that
path and execute it. Embeds the guarded-change charter **core verbatim** as a blockquote, then the stage-3
additions (CH8, CH9/CH10, CH11/CH12) **quoted as task-specific additions**, then a "things the author wants
attacked" list marked explicitly as neither a boundary nor pre-absolving.

**Carried-forward findings (SEV4 requirement).** Unlike pass 1, the prompt carried pass 1's blocker and nine
majors forward **with their claimed fixes**, and required a dedicated *"Pass-1 fix audit"* section asking
whether each fix closed its finding **or merely relabelled it**. That section is what produced this pass's
central result.

**Draft-standing instruction, now stage-scoped**, matching the config as amended at `d044654`: at stage 3
the path holds the pre-run **UNVETTED DRAFT with NO standing**, and the banner is the discriminator. All
three reviewers reported checking the banner and confirming they held the draft.

## (ii) The exact context path list given (closed set) — WITH A DECLARED VIOLATION

Stage artifacts (5) + 12 context paths. **This is where the run broke its own rule.**

The prompt's closed set included **five files that are not in the config's `redteam_context`**:
`Architect/guarded-change.architect.md` and `Guarded_change/stages/{stage-1.5,stage-3,stage-4,stage-8}.md`.
Verified after the fact:

```
$ grep -n "^  - path:" Architect/guarded-change.architect.md
38: /home/zero/Documents/Architect.md
45: …/Guarded_change/stages/charter.md
53: …/Dragonfly/stages/charter.md
57: …/Architect/stages/charter.md
71: …/Architect/ATTEMPT-2-STATE.md
76: …/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl
82: /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
94: …/Architect-Attempt-1/stages
```

**Eight paths. None of the five.** `git show d044654` added none.

The runner's intent was to fix pass-1 finding B-F24 (all three pass-1 reviewers had to read out-of-set
because the artifacts' ~20 rule-ID citations resolved to unlisted files). But `1-spec.md` §8 puts the config
on the **explicitly-NOT-touched** list, so this run cannot legally amend `redteam_context` — and B15
requires supplementary author-authored context be **quoted in the record as such**, which the prompt did not
do. **Reviewer E caught this live (E-F7) while it was happening to it.** It is recorded here as the B15
declaration that should have been in the prompt. The run violated, in its own dispatch, the gating rule
(C-11) it is about to ship.

## (iii) The reviewers' verbatim output

| Reviewer | Record | Lines | Worst severity |
|---|---|---|---|
| D | `records/reviewer-D-verbatim.md` | 270 | major |
| E | `records/reviewer-E-verbatim.md` | 188 | major |
| F | `records/reviewer-F-verbatim.md` | — | major |

D and E exceeded the inline return limit and were persisted by the harness; their text was extracted
programmatically from the harness's own JSON (no re-typing), with only the `agentId`/`usage` footer
stripped. F returned inline and is transcribed whole.

## (iv) Reviewer agent type + model

| Reviewer | Agent type | Model |
|---|---|---|
| D | `general-purpose` | opus (claude-opus-5) |
| E | `general-purpose` | opus (claude-opus-5) |
| F | `general-purpose` | sonnet |

Three **separately-spawned** subagents in one concurrent batch, no shared context with the runner beyond the
prompt path and none with each other. Two models, for blind-spot diversity.

## (v) Reviewer-reported sha256 of each context file

All three reported hashes; **they agree with each other and with the runner's own `sha256sum`** on every
shared file — fork source `0e73bacf…adc590`, `Architect.md` `986512f5…bb78b`, config `42f289a5…0429c`
(the amended one), draft `6a1981f3…19212`, and the five revised stage artifacts (`0-baseline`
`b22b251b…f24dee`, `1-spec` `e45da335…27fe5f`, `1.5-criteria` `d070b714…e2120f`, `2-plan` `f01093d2…c73ca`,
`decisions` `34a0def1…80e10c`). **No hash disagreement.** All three independently noted the transcript had
grown to 1534 lines and hashed it accordingly.

---

## Consumer's citation spot-verify (B14)

Five checks run against source; commands and results pasted in `decisions.md`'s gate-4 pass-2 entry.
**5 of 5 confirmed. 0 fabricated citations across all three reviewers.** Every one falsified something the
runner had written:

- the config's `redteam_context` holds **8** paths and none of the five the prompt added (E-F7);
- `README.md` and `ATTEMPT-2-STATE.md` **no longer** state the ~85% figure — OOS-1, OOS-5 and §0.6's
  "remain" are stale, and §0.6's pasted grep no longer reproduces (E-F18);
- `~/Documents/Architect.md` is **115** lines, not the 103 `0-baseline.md` now claims — 103 is the *fork
  source's* count, i.e. the exact defect class §0.1 corrected one pass ago (D-F11);
- `1-spec.md` L71 and L86 still say **"18 rules (B01–B18)"** after B19 was added (D-F12);
- SEV2 runs `stage-4.md` **L26–29**, not L26–28 as cited (E-F16).

---

## Union of findings (nothing discarded)

### NO BLOCKER. The pass-1 blocker is CLOSED — 3/3.

B-5 varies the position, as the owner prescribed. Extended correctly to C-23 (B-6) and C-14 (B-7). Also
closed 3/3: **B19** and the completeness of B01–B19 (D and E each re-derived the inventory against all 103
fork-source lines independently); **Part C**'s semantic + insertion mutants; **C-03b**; **D3′**'s removal of
the false `Divisible` grant; the fixture-layer rebuild bound.

### MAJOR — the shape of this pass

**Reviewer E's summary is the accurate one: five of nine claimed pass-1 fixes moved their defect rather than
removing it**, three genuinely new defects were created by the fixes, and three coverage gaps were never
reached. Convergence noted; never used to discard.

| Class | Finding | Conv. |
|---|---|---|
| **Moved, not removed** | D10's "human tie-break reachable via RAT3" — RAT3 binds a *guarded-change* subagent, not Architect's shipped `Node()` loop | **3/3** (D-F01, E-F2, F-F5-1) |
| | `forkdiff.sh` residue is **one-directional** (shipped-side); B19's class is a *fork-source* rule missing from the inventory, which it cannot surface | **2/3** (D-F17, E-F1) |
| | D3′'s "whatever paths your caller supplies" is **unbounded** — nothing can be B15 supplementary context | **2/3** (D-F04, E-F6) |
| | D8's "conditional lens given only when its trigger fires" has **no assembler** in `Architect.md` | **2/3** (D-F03, E-F8) |
| | Rebuild bound applied at the **fixture** layer, not the **probe** layer | E-F11 |
| **New, created by the fixes** | C-08 ("silent unilateral demotion is a gate violation") vs C-12 (`Union` demotes an unsubstantiated finding below blocker\|major) — **directly contradictory**, no carve-out | E-F3 |
| | C-03b hard-types a CHANGE list that disagrees with `0-baseline.md` §0.3 — the C5 defect C-02 was just fixed for, one row over | E-F5 |
| | The closed set widened outside the config, undeclared | E-F7 |
| **Never reached** | RAT1/RAT2 — the addition most motivated by this project's own failure history — has **zero** behavioral verification | F-CH8-1 |
| | C-10 (earned-clean) is gating on reviewer *behavior* and verified by text assertion only | E-F10 |
| | Non-computational plans: B01/B12 make a clean factual lens un-earnable when there is no citable source, yet the owner scoped Architect to plans usable "entirely outside a computational context" (record 55 item 1) with *standing→walking→opening the door* as his example (record 1128). **No criterion, no charter provision, not even an OOS note.** | E-F13 |
| | `Divisible`'s "neither half below the floor" duty — bound (1) of the three `Architect.md` L3–4 says are all needed — untested; B-7 exercises coverage only | D-F08 |
| **Apparatus** | n=2 with **cross-model** within-arm agreement and no stated pass rate; E computed ≈**71% false-negative** on a real 0.1→0.6 effect. ST1.5d's own remedy (a stated rate over a stated N) not adopted | **3/3** (D-F05, E-F4, F-L2) |
| | B-5/B-6 relocation changes **two-to-three** adjacencies, not one; "the only variable is position" is false, and the confound-declaration duty is scoped to *deletions* | **3/3** (D-F15, E-F4, F-L1) |
| **Ratification** | **E-F14: D1 itself may be an unratified default** — records 1124/1171/1175/55 read as leaning toward the *fold*, with a carve-out for the definition | E-F14 (pass-1 reviewers A and B read the same records the opposite way) |

### MINOR / NITPICK

D-F11 · D-F12 · D-F13 (B15 still misses fork L69–70's "the charter instructs the reviewer to report these")
· D-F14 · D-F16 (present-tense description of unbuilt instruments, under the tense notice claiming
compliance) · D-F18 · D-F19 · E-F15 · E-F16 · E-F17 (B14's "sample" silently made exhaustive) · E-F18 ·
E-F19 · E-F20 · E-F21 · F-1 · F-7.

### Scope verdict (3/3 favourable)

All three reviewers judged the growth 19→24 criteria + 7 arms to be **the red-team's findings becoming the
next task, not scope drift** — nothing touches elements 2–6; C1 holds. Reviewer E named the *opposite* risk
as the real one: **34 cold agents to verify one ~200-line prompt** reproduces the pattern the config's own
opening names — *"the measurement apparatus became the thing that kept failing"* — and R2's mitigation
(declare a reduced pass → `verified = no`) has **no path to "done", only a path to a halt**.

## Worst severity: **MAJOR** · Route: **HALT (SEV4 iteration cap, four classes)**
