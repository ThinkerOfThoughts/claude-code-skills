# B7 fixture — convergence / decomposition guard (DEC) on non-reducing recursion

The skill's **DEC** bound (SKILL.md, METHODOLOGY.md "Gates and iteration caps", stage-6 step 6) is
**concrete**: *if two consecutive levels do not reduce granularity — a child node's estimated leaf-count
/ work-size is ≥ 0.8× its parent's — the branch escalates (a `plan/decisions.md` escalation) rather
than recursing further.* A genuinely-reducing decomposition does not trip it.

The estimated leaf-count / work-size is a **stipulated fixture value** (a fabricated node's granularity
estimate) — the harness tests the guard's *threshold logic given the estimate*, which is exactly what
the criterion's "fabricated pathological node whose decomposition reproduces roughly the same
granularity" asks for.

## `pathological/` — NON-reducing recursion (guard MUST fire)
Fabricated task: "clean up the codebase" restated at each level without real division.
```
L0 root:   estimated leaf-count = 10   (work-size W0 = 10)
L1 child:  estimated leaf-count = 9     → 9 / 10 = 0.90  ≥ 0.80  → level 1 NON-reducing
L2 grandchild (if it recursed): 9       → 9 / 9  = 1.00  ≥ 0.80  → level 2 NON-reducing
```
**Two consecutive levels do not reduce granularity (0.90, then 1.00, both ≥ 0.80) → DEC ESCALATES the
branch within the bounded 2-level count** (a `plan/decisions.md` escalation; stop-for-human under
delegation). The tree does NOT grow without granularity reduction.

## `reducing/` — genuinely-reducing recursion (guard MUST NOT fire) — oracle-can-fail twin
Fabricated task: "build the checkout flow" that really divides into smaller atomic work.
```
L0 root:   estimated leaf-count = 10
L1 child:  estimated leaf-count = 3     → 3 / 10 = 0.30  < 0.80  → REDUCING
L2 leaf:   estimated leaf-count = 1     → 1 / 3  = 0.33  < 0.80  → REDUCING
```
Each level's child is < 0.80× its parent → **DEC does NOT trip**; recursion proceeds normally to
atomic leaves. The guard **discriminates** non-reducing from reducing recursion — it does not fire on
every deep tree.

## Oracle (deterministic threshold application)
| Fixture | L1 ratio | L2 ratio | DEC (≥0.8× two consecutive levels)? | Expected |
|---|---|---|---|---|
| `pathological/` | 0.90 | 1.00 | YES — both ≥ 0.80 | **escalate within 2 levels** |
| `reducing/`     | 0.30 | 0.33 | NO — both < 0.80   | **no trip; recurse to leaf** |

## Residual (carried to the harness verdict)
The ratio is computed from an **estimated** leaf-count / work-size, which is a subjective model judgment
in the wild (the "subjective work-size estimate" flagged at gate 7). The **guard's firing logic** given
an estimate is fully deterministic and verified here; the **accuracy/reliability of the estimate itself**
is a characterization concern the conformance dry-run stipulates rather than measures — see 8-harness.md.
