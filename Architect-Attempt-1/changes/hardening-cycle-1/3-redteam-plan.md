# Stage 3 — Red-team the plan: record index, provenance, spot-verify, convergence

**Verbatim records (ART2 — the reviewers' raw output; the author's interpretation lives in
`decisions.md`, not here):**

| Record | Frame given | Agent type / model | `spawn_id` (dispatcher-recorded) | Self-reported identity | Worst severity |
|---|---|---|---|---|---|
| `3-redteam-plan.A.verbatim.md` | **source-anchored / factual** | `general-purpose` / `claude-opus-5` | `a1cb9e6c3aa124a3f` | session `45cb99a2-…` ("no separate agent id reportable") | **major** |
| `3-redteam-plan.B.verbatim.md` | **failure-injection / mechanism-breaking** | `general-purpose` / `claude-opus-5` | `ad7de94dda62399b4` | **"unavailable"** | **blocker** |
| `3-redteam-plan.C.verbatim.md` | **fidelity / scope / honesty** | `general-purpose` / `claude-opus-5` | `a9f343344368cc2f7` | **"unavailable"** (scratchpad segment only) | **blocker** |

**Charter given (verbatim):** `3-charter-given.md` — the guarded-change charter core verbatim
(`Guarded_change/stages/charter.md @ 8d73e5d`, sha256 `0e73bacf…`, independently re-verified) + the
stage-3 additions CH8/CH9/CH10/CH11/CH12 + the closed-context list + the required output form. Each
reviewer's **frame addition** is quoted verbatim inside its own record.

**Context path list given:** the closed set enumerated in `3-charter-given.md`. **Path validation
(CFG3)** was run before dispatch — 15 paths, all OK, none dead (recorded in `decisions.md`).

**Reviewer-reported context-file sha256s:** in each record. **Consumer verification:** all three
reviewers' reported hashes for `0-baseline.md`, `1-spec.md`, `1.5-criteria.md`, `2-plan.md` are
byte-identical to the values captured independently in `context-hashes.txt` **before** dispatch. ✓

**Deliberate departure from the plain 1-agent stage-3 procedure, declared:** guarded-change stage 3
specifies *a* cold subagent. This run dispatched **three with deliberately different frames** — a
superset of the requirement, chosen because (a) the artifact is 1,312 lines across 18 files and one
reviewer cannot cover it, and (b) it dogfoods the `DIV` mechanism this very change proposes. The
frame-diversity result is itself evidence: see "What frame diversity bought" below.

---

## Consumer spot-verify of citations (CH6 — performed before the gate routed)

| Reviewer claim | Command run | Result |
|---|---|---|
| A/F1-1: `stage-8` is **not** a word-boundary `TOP` site (it is a `HARDSTOP` phantom) | `grep -nw -- TOP stages/stage-8-restart-resume.md` | **ZERO hits — CONFIRMED** |
| A/F1-1: `ON TOP OF` survives `grep -w` at 2 sites | `grep -n "ON TOP OF" METHODOLOGY.md examples/…/planning.md` | `METHODOLOGY.md:79`, `planning.md:25` — **CONFIRMED** |
| A/F1-2: `KIL` ⊂ `SKILL`, 21 hits / 4 files | bare `grep -rho -- KIL` over the corpus | **21 hits, 4 files — CONFIRMED** |
| A/F1-2: `ING` ⊂ `PLANNING`/`RULING` | bare `grep -rno -- ING SKILL.md stages/charter.md` | `SKILL.md:3`, `charter.md:47` — **CONFIRMED** |
| B/L-1: stage 6's LEAF branch ends with "planning of this node is done" and never writes a status | `sed -n '12,14p' stages/stage-6-…md` | **CONFIRMED verbatim** |
| A fidelity: description budget | measured `len(description)` | **954 chars**, 0 angle brackets (A said 956 — **2-char drift, substance holds**: ~134 chars of headroom) |
| A/F3-3: `TPL1`/`TPL2`/`SEV` have no cross-file-index row but do have multiple sites | `grep -c '\*\*TPL1\*\*' METHODOLOGY.md` + word-boundary site map | **0 index rows each; 4 / 4 / 2 sites — CONFIRMED** |

**No fabricated citation found in any of the three records.** The only inaccuracy detected is a 2-char
count drift in A (nitpick). This is the *earned* basis for routing on these severities.

---

## Convergence (independent reviewers who hit the same thing)

Frames were disjoint, so agreement here is real signal, not an echo.

| Finding | A | B | C | Worst stated |
|---|---|---|---|---|
| **DIV's differential frame collapses into frame A** — the seed skeletons carry no Layer-2 sections, so the declared default hands frame B the 7-section spine that frame A already covers | F1-4 | F-4 | D-3 | **major (3/3)** |
| **The baseline site map (R1's gating reference) is wrong** — phantom sites survive the mandated matcher | F1-1 | F-1, F-2 | F1-1 | **major (3/3)** |
| **Position: PRV/DIV inside SKILL.md's rule block displaces GBP off the block tail and staleifies the block's own 3-item rationale; S-SC3 is a line-offset proxy that cannot see intra-block order** | F4-3 | A-1 | A-2 | **major (3/3)** |
| **§4-heading count is wrong and S-C10's extractor is undefined over prose sites** | label audit | F-5 | L-3 | **minor (3/3)** |
| **"Named risk-acceptance" is unavailable under this run's own RAT3 constraint — nobody present can grant it** | F2-3 | A-7 | L-4 | **minor (3/3)** |
| **PRV's *positive* half is itself an overclaim** (attestations by the constrained party) | — | Fid-1 | D-2 | **major (2/3)** |
| **The dead-child re-dispatch creates a second writer for one `_status.md`** — in exactly the live-reproduced scenario, and absent from the accessor table that claims single-writer coverage | — | A-2 | A-1 | **major (2/3)** |
| **BIND does not cover the new gate artifacts** (`APPROVAL.md` / `AUDIT.md`) — a re-drafted split keeps its approval | — | L-6 | L-2 | **major (2/3)** |
| **The stage-3 closed set omitted the approved-scope/decision record the run's own config calls source-of-truth for every settled decision** | F4-2 | — | U-1 | **major (2/3)** |
| **`elc` is a self-declared integer with no derivation rule, while S-C2 calls the result "computable"** | — | M-5/Fid-3 | A-4 | **major (2/3)** |
| **The `_status.md` schema omits `template` + the granularity call, which derived `index.md` is documented to carry** | — | L-14 | A-6 | **minor (2/3)** |
| **`TPL1`/`TPL2`/`SEV` are live IDs outside both regression criteria** | F3-3 | F-3 | — | **minor (2/3)** |

## The five BLOCKERS (each raised by one reviewer; each independently checkable)

| ID | Reviewer | Claim |
|---|---|---|
| **B/L-1** | B | **No stage is assigned the duty to *write* a terminal `subtree: complete`.** Stage 6's LEAF branch ends "planning of this node is done"; the parent's join then sees a non-terminal status and applies the dead-child rule ⇒ the smallest decomposing tree (root + one leaf) is declared dead, re-dispatched, and escalates. *Premise spot-verified.* |
| **B/L-2** | B | **Escalation and death are the same observable event** (both = "returned without a terminal `subtree:`"), with no precedence rule ⇒ the escalation channel F1 says is missing is destroyed by the join at every altitude. |
| **B/L-3** | B | **SEAM's reopen detector is uncomputable as specified:** no schema slot holds the parent's per-child *expected* `seam_rev`, and no rule says what increments `seam_rev`. Both readings break (unbounded cascade, or the node self-certifies whether its own seam changed). A Tier-1 fix that is un-checkable is a blocker **by this plan's own threshold table**. |
| **B/L-11** | B | **`spawn_id` is defined as a *self*-reported id that may be unavailable, with an unconditional consequence** ⇒ three honest "unavailable"s make every pass un-run and **no node can ever gate**. *Live evidence: 2 of this very review's 3 reviewers reported "unavailable".* |
| **C/L-1** | C | **D2 (BIND over every record) and D11 RES(a) (minor fix-in-place re-binds without a re-pass) contradict** ⇒ a `clean-fixed-in-place` node can never satisfy the subtree-complete predicate, or the records must be mutated by the author; **X2 and X7 encode opposite verdicts for the same disk state**. |

**Root cause the reviewers converge on (B's summary, worth carrying forward verbatim):** *"the plan
specifies the join's and SEAM's **predicates** but not their **producers**. It says precisely what must
be true on disk … and, for each, leaves unassigned the stage that writes the fact the predicate reads."*

## What frame diversity bought (evidence for the DIV fix, from this run's own data)

Overlap between the three reviewers was **12 findings out of ~80 raised**. Each frame produced findings
**no other frame reached**:
- **A (source-anchored)** alone found the ID-collision violations (`KIL`⊂`SKILL`) and the exact wrongness
  of the baseline site map — findings that require *running greps against the corpus*, not reasoning.
- **B (failure-injection)** alone found **4 of the 5 blockers** — all of them reachable only by walking a
  concrete tree shape step by step.
- **C (fidelity/scope)** alone found the RES(a)↔BIND contradiction and the "no `gate:` value represents a
  *demoted* blocker/major" gap (F10's second half, unfixed).

This is the strongest available evidence that **frame diversity, not agent count, is where the marginal
catch lives** — and it is the second run in a row to show it (`FINDINGS.md:24-27` recorded that a
*reduced* 1-agent pass produced 5 of 6 structural blockers). It also means the F7 fix's *direction* is
right even though `DIV`'s default path is broken (3/3 major).

---

# PASS 2 — record index, spot-verify, convergence

| Record | Frame | Agent / model | `spawn_id` (dispatcher-recorded) | Worst |
|---|---|---|---|---|
| `3-redteam-plan.pass2-A.verbatim.md` | **closure audit / source-anchored** | `general-purpose` / `claude-opus-5` | `a7b5eb6d0dfbb794f` | **blocker** |
| `3-redteam-plan.pass2-B.verbatim.md` | **failure injection** | `general-purpose` / `claude-opus-5` | (in record) | **blocker** |
| `3-redteam-plan.pass2-C.verbatim.md` | **fidelity / scope / honesty** | `general-purpose` / `claude-opus-5` | `af13b7628d0aa4d37` | **blocker** |

Pass-1 records renamed `3-redteam-plan.pass1-{A,B,C}.verbatim.md`. Closed set extended with the approved
scope/decision record and the pass-1 records (carried-forward findings, SEV4).

**Spot-verify (CH6): 5 blockers checked against the plan's own text, 5 confirmed** — see `decisions.md`
"GATE 4 (pass 2)". All three reviewers' reported hashes for the four stage artifacts match
`context-hashes.pass2.txt` captured before dispatch. ✓

## Pass-2 blockers, by convergence

| Finding | A | B | C | Note |
|---|---|---|---|---|
| **Terminal `subtree: complete` is assigned to stages 6/6.5 but conditioned on `_assembled.md`, a stage-7 output** ⇒ no node can write it ⇒ root+1-leaf deadlocks again | F1-1 | B-2 | — | **B/L-1 re-opened** — the pass-1 blocker, in a new position |
| **`declared_seam_sha256` has no derivable initial value** at its stage-2 write ⇒ the reopen fires on every pair, or is adopted from the child (F2 unfixed) | F1-2 (major) | B-1 (blocker) | — | **B/L-3 re-worded, not closed** |
| **`BIND`'s parent-hash clause is undefined at the root** (no parent plan, no producer) ⇒ a single-node run — the scale-down shape **and this loop's own** — can never gate | — | B-4 | — | new |
| **The fence is unenforceable**: `off_limits_paths` is "naming is the fence" (`METHODOLOGY:99-101`), authored by the party it constrains, validated by nothing | F2-4 (major) | F1-1 | D-7 (minor) | **3/3** — a hedged pass-1 minor promoted into "principle 1" |
| **The fence and the cold audit are mutually exclusive** — `AUDIT.md` is written into the fenced dir: either the fence binds run-dispatched agents (audit impossible ⇒ TOP unsatisfiable) or it does not (⇒ F5 with one extra hop, the live shape) | — | F1-2 | — | new |
| **`DIV`'s per-frame prohibitions make every completeness record un-run** under the charter's earned-clean clause; and the degraded 2-frame pass collides with D2(a)'s "6 records" ⇒ join deadlock | — | — | L-1, L-2 | new — the DIV fix is rated **worse** than pass 1's |
| **`subtree: escalated` is an absorbing state with no exit producer** ⇒ assembly blocks permanently after any escalation | F2-1 (major) | — | — | new; same class |
| **`S-PRD`'s oracle is a mention-check** (7/14 sampled pairs pass at baseline) — the pass's own organizing criterion cannot distinguish a read from a write | F2-3 (major) | — | — | new; **same class** |
| **`idcollide.sh` as specified flags 4 baseline IDs** (`CMP`⊂`CMP2`, `TOP`⊂`HARDSTOP`, `DEC`⊂`DECOMPOSE`, `TPL`⊂`TPL1`) ⇒ B0.7's "flags nothing at baseline" is false and gating `S-SC2` cannot pass | F1-3 (major) | — | — | new — the new instrument fails its own can-fail test |
| **"Declared deferral" for an unverified gating criterion is illegal** under `Guarded_change/stages/stage-8.md`; the legal route is HALT + relay | LA-1 (major) | A-7-adj | L-3 (major) | **3/3** |
| **`PRV`'s positive half still overclaims** — "mechanically checked / BIND-current" rests on a reviewer-attested, author-transcribed hash; "no shared context and disjoint frames" does not follow from distinct ids + differing prompts | F5-2 (minor) | — | D-1, D-2 (major) | **2/3, carried from pass 1 — not closed** |
| **No admissible owner locus is demonstrated to exist** — the only durable copies of owner words in this harness are agent-authored, so D9 is satisfiable only in the shape F5 names, or not at all | F5-1 (major) | F1-3 | D-3, D-4 (major) | **3/3** |

## Confirmed CLOSED from pass 1 (mechanism named by ≥1 reviewer, A and C independently)

**3 of 5 blockers and 10 of 12 convergent findings.** Escalation-vs-death precedence (stated first,
`2-plan.md:113`); `spawn_id` dispatcher-recorded + declared-degraded (X6's all-"unavailable" arm);
RES(a)↔BIND unified into one rule with immutable records + a rebind-record discriminator; the 3/3 position
major (intra-block order, updated rationale, two can-fail variants — and GBP **keeps** the block tail);
the 3/3 baseline-site-map major (B0.6 reproduces under its own mandated matcher; `TPL1`/`TPL2`/`SEV`
added; **R1 can now pass its own replay**); the ID collisions (promise → instrument); BIND over the gate
artifacts; `elc` honestly relabelled; the schema's missing `template`/granularity keys; the closed-set
omission of the approved-scope record.

## What frame diversity bought, pass 2 (evidence for DIV's *direction*, against its *mechanism*)

Each frame again reached blockers no other frame reached: **A** alone found that the pass's own three new
instruments (`S-PRD`'s pair check, `idcollide.sh`, `S-C10`'s pinned predicate) **each fail their own
can-fail test**; **B** alone found the fence's unenforceability and the fence↔audit mutual exclusion by
tracing the topgate on a concrete tree; **C** alone found that DIV's own prohibitions make every record
un-run under the charter it must satisfy. Overlap was again low. **The direction of the F7 fix is
confirmed twice over; its pass-2 mechanism is rated worse than pass 1's by the reviewer who checked it.**
