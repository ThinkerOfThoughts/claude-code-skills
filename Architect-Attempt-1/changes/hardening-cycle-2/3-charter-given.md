# Stage 3 — the charter given to the three cold reviewers (verbatim record, part 1 of 2)

Part 2 is the three verbatim reviewer outputs at `3-redteam-plan.{A,B,C}.verbatim.md`; the author's
interpretation lives in `decisions.md` and the ranked synthesis in `3-redteam-plan.md`.

## Dispatch facts (IDN — dispatcher-recorded, not self-reported)

| Arm | Frame | Agent type | Model | `spawn_id` (dispatcher-observed) |
|---|---|---|---|---|
| **A** | closure audit + fidelity/scope honesty (CH11/CH12 focus) | `general-purpose` | `claude-opus-5` | `aea2863bc75a6d6a5` |
| **B** | failure injection + producer/ordering attack (position + concurrency lenses fire) | `general-purpose` | `claude-opus-5` | `a170420f375a3ae9f` |
| **C** | oracle validity + measurement honesty (CH9/CH10 focus) | `general-purpose` | `claude-opus-5` | `a214e3d602b3b8587` |

**Three separately-spawned subagents, no shared context with the author and none with each other.** The
three `spawn_id`s are **distinct**, recorded by the dispatcher at spawn — not self-reported. **Frames are
disjoint by construction:** each prompt names the other two frames and instructs the reviewer to stay in
its own. *Rationale, recorded rather than asserted: across cycle 1's six reviewers, overlap was 12 of ~80
findings and each frame alone found blockers no other frame reached — frame diversity, not agent count, is
where the marginal catch lives. This is a **decorrelation** measure, **not** independence (PRV): three
same-model instances are not three independent minds.*

## Charter core given verbatim to all three

The **guarded-change charter core** (`Guarded_change/stages/charter.md @ b08f5a9`, sha256
`6134cad8…` is Architect's fork; the core given is guarded-change's five lenses + the unconditional
discipline bullets) was embedded verbatim in each prompt: the five lenses (Factual / Logical /
Missed-opportunity / Unstated-assumptions&risks / Fidelity incl. the owner-ruling ratification audit) and
the discipline — cite-or-it-doesn't-count, rank-every-finding, flag-the-unverifiable, "no issue" allowed,
clean-factual-earned, clean-fidelity-earned, spot-verify-citations, provenance + reviewer-input-is-a-closed-set
— plus **both conditional lenses (position and concurrency), which fire here** and were stated as firing.

## Stage-3 additions given

- **CH8** (coverage challenge) — to all three; each was given the sharpest form for its own frame.
- **CH9 / CH10** (label audit + earned-clean label audit) — to **A** and **C**.
- **CH11 / CH12** (ratification audit + elaboration/inflation audit, RAT1/RAT2) — to **A**, with the
  instruction to **fetch and spot-verify the owner quotes in the harness-authored transcript itself**, and
  the explicit warning that `LOOP-STATE.md` is **agent-authored and therefore NOT an admissible source**
  for a ratification quote.

## The closed input set (identical stage artifacts; frame-weighted context order)

**Artifacts under review** (all three): `changes/hardening-cycle-2/{0-baseline,1-spec,1.5-criteria,2-plan}.md`
plus `oracles/{idcollide,ruleid-sitemap}.sh`.

**Context, priority-ordered per frame** — the union across the three arms:

| Path | Given to |
|---|---|
| `/home/zero/architect-dogfood-2026-07-24/FINDINGS.md` (the finding set under repair + the *Triaged NOT genuine* list) | A, B, C |
| `/home/zero/architect-hardening-loop/LOOP-STATE.md` (**flagged agent-authored**; claims are checkable claims, not source) | A, B, C |
| `Architect/changes/hardening-cycle-1/` (decisions.md, 2-plan.md, 0-baseline.md, 1.5-criteria.md, the six pass-1/pass-2 verbatim records) | A, B, C |
| `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` — **THE APPROVED SCOPE/DECISION RECORD** *(cycle 1's pass-1 omission; supplied to every arm this cycle)* | A, B, C |
| `Architect/` — the artifact under change, unmodified | A, B, C |
| `Architect/guarded-change.architect.md` — the Layer-2 config | A, B, C |
| `Guarded_change/` (SKILL, METHODOLOGY, `stages/stage-{0,1,1.5,2,3,4,8}.md`, charter) | A, B, C |
| the **session transcript JSONL** (harness-authored; the admissible ratification locus), records 694 + 699 | **A** (with the duty to fetch and spot-verify) |
| `Guarded_change/changes/audit-hardening-2026-07/` (the positive-per-site-assertion + baseline-replay precedent, as a comparison bar) | **C** |

**Path validation (CFG3):** performed at run start — **15/15 paths OK, 0 dead** (recorded in
`decisions.md`). No degraded-review acceptance was needed.

## Carried-forward findings given (so reviewers confirm closure rather than re-derive)

Each arm received the subset of cycle 1's gate-4 carry-forwards relevant to its frame, quoted, including:
producers-not-just-predicates; BIND's **zero root carve-out** ⇒ a single-node run could never gate; the
`clean-fixed-in-place`-can-never-assemble contradiction; `spawn_id` self-reported + the impossible
3-identical rule; the re-dispatch second-writer race; `index.md`'s **four** baseline writers and stage-8's
false *"no single global cursor"*; PRV's positive half overclaiming; the **scope-label inflation** and its
surviving residue at `hardening-cycle-1/3-charter-given.md:206` + `decisions.md:41`; the **illegal
"declared deferral"** route; the recaptured baseline site map; and cycle 1's coverage challenge *"no
criterion observes that a clean tree terminates."*

## The deferral list given (so a silent implementation or a vacuous claim is catchable)

All three arms were told what R1 defers — **F1** (join / terminal-status producer / stage-ordering rework
incl. the `_status.md` schema, escalate-to-parent, bottom-up assembly, and **F6**'s killed-node marker),
**F2** (seam-reopen detector), **F5** (topgate ratification mechanism), **DIV** (frame diversity), the
cost/fan-out envelope, ECON's O(children²) load, and the **"two passes"** ruling — with the instruction
that *a fix that silently implements or pre-shapes deferred work is a finding, and so is a fix that claims
to close something it merely declares.* **B** was additionally told to attack the **deferral seam** (a
landed fix that depends on, contradicts, or is vacuous without deferred machinery).

## Required output form (identical structure; frame-specific required sections)

`**<ID> · <SEVERITY> · <claim>**` blocks with file:line evidence and a suggested fix; a **`## Ranked
list`** with an explicit `WORST SEVERITY:` line; and a **`## Provenance`** section giving the exact context
paths read, agent type + model, and `sha256sum` per context file — with the instruction *"if you cannot
determine your own spawn identifier, say `spawn_id: unavailable` — do not invent one"* (**IDN**: the
dispatcher's record above is the audit surface; a self-report is corroboration only).
Frame-specific required sections: **A** — Closure audit, Ratification audit, Coverage challenge, Label
audit. **B** — Operand-table attack, Runs walked to death (a)–(g), Position lens, Concurrency lens,
Coverage challenge. **C** — Oracle mutation results (with commands + output), Per-criterion verifiability
audit, Baseline counts re-verified, Coverage challenge, Label audit.

## Context-file hashes at dispatch

See `context-hashes.txt` (sha256 of each stage artifact, each oracle, and every artifact file at
`b08f5a9`), captured immediately before dispatch.
