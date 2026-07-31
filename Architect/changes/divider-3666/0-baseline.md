# Stage 0 — Baseline

**REWRITTEN 2026-07-31 after both stage-3 reviewers found the first version false (their B1/B1).**
The first version was captured at 14:21 against commit `d81bc0a` while iteration 3's division was
**still in flight**, and it recorded numbers that the run then overtook. Superseded in full.
Nothing below is inherited from it; every figure is re-derived from disk and from the run ledger.

Commit at run start: **`cf16967`** — *"architect: iteration 3 — division COMPLETED, and the numbers
correct the ruling's premise."*

## Files under change, frozen at `cf16967`

| File | sha256 | lines |
|---|---|---|
| `Architect/stages/divider.md` | `ebdf30eddf9dc227f895b4d414cc442ae5c230e1c0ee405409dd52a18829c694` | 118 |
| `Architect/stages/redteam-split.md` | `ffeea71567959a05af19f891168e10145658905a4a072bdac654dd04fe83de13` | 62 |
| `Architect/stages/redteam.md` (context, not changed) | — | 54 |
| `Architect/stages/common.md` | `389358e2b74ee3490b6682847fb8c8034063724fd924f2179341acc5120651d4` | 67 |
| `Architect/stages/node.md` | `1a41e11fd2438fc9ac4ee86f16dc97ee7656b687d33a9df749802da478a3a068` | 140 |
| `Architect/SKILL.md` | `ffaa1a8440fa829cbd4d4a4401dcd9bcd9d95cf22006ea0a3d5110b50a1c21b9` | 99 |

The working tree at the time of the first capture already held these contents; only the commit
label and the behavioural measurement were wrong.

## Behavioural baseline — iteration 3's division, COMPLETED

From `runs/data-distiller/decisions.md` §"Correction to the number that triggered the ruling" and
`it3/0/` on disk:

| | Measured |
|---|---|
| Wall clock | **107 minutes**, 12:37:13 → 14:24:35 |
| Cold split reviews | **12**, four rounds of three |
| Divider agents | **1** (`divide-0.md`: *"the twelve cold split reviewers **I** dispatched"*) |
| Total dispatched agents | **13** |
| Outcome | **A division was returned**, with `subtask-A.md` / `subtask-B.md` on disk |
| Endorsement | **12/12, in all four rounds.** No reviewer, in any round, objected to proceeding |
| Prose written | **~7,500 lines**; proposals grew 347 → 546 → 643 → 677 lines; reviews 21–47 KB each |
| Serial dispatch's share | **~50 of the 107 minutes** — an orchestrator instruction, not the design's |

**Across all three iterations, no reviewer has ever objected to where the line was drawn.** All
~90 findings landed on the **seam description** — the divider's own output — not on the joint.
That is measured, not argued, and it is exactly what record 3666 removes from the reviewer's
remit.

**So the defect is not that the division fails. It is the price.** Roughly 7,500 lines of prose,
13 agents and 107 minutes to cut one task in two, at one node, with the answer unchanged from
round 1. The mechanism, from `divider.md:97-98`:

> While any `major` or `blocker` stands, **re-derive** the split and review again.

That contradicts the same file's §"Agreement is about PROCEEDING, not about being finished"
(record 3438) six lines above it, and it is the rule that executed: four re-derivations of a cut
every reviewer approved every time.

## Regression bar — the CARRY list

Architect is a set of prompts, not a program. A CARRY item that stops being stated is a
regression; a DROP must be declared here or in `2-plan.md`.

1. `Divisible` returns **exactly one of three** answers — a division, `null`, `FAILED_TO_DIVIDE`
   — and the last two stay distinct (records 3402/3438; the conflation killed iteration 1).
2. Four rounds; after four, the best split with 2-of-3 (record 3438).
3. The granularity floor bounds the split in one direction: neither half may fall below it.
4. The divider is given **no plan**; the split reviewer holds no plan.
5. **The split reviewer is told it holds the `task` and the `granularity` floor.** Today that
   declaration is `redteam.md:11` — a file the split reviewer stops reading under this change.
6. **The floor bounds what a reviewer may call a defect** (`redteam.md:13-18`) — the
   infinite-regress guard. Same exposure as 5.
7. Each sub-task carries the source material its task pointed at (record 3119).
8. The seam is not a producer/consumer handoff — both halves are planned concurrently and blind.
9. `node.md`'s checkpoint 0 still fires the instant `Divisible` returns.

## Declared DROPs

From `redteam-split.md`: the six lenses, the four-tier severity vocabulary, the earned-clean
clauses, the provenance record, the closed-set input enumeration, the "last reader" exhortation,
the **coverage** question, the **"an unstated seam is at least `major`"** rule, and the
self-containment sub-check with its three-destination taxonomy.
From `divider.md`: the three-destinations apparatus, the re-derive-on-standing-major rule, and
the agreement/severity exegesis.
From `redteam.md`, lost by no longer reading it: **"graded on precision, not volume"** (retained
as one clause — see `2-plan.md`), **"do not self-censor a lone observation"** (dropped: the split
review has no `Union` merge for a lone finding to survive into), and the six lenses.

All on the owner's instruction, record 3666, quoted in `1-spec.md`.
