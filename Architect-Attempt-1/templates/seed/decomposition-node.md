# Decomposition node — <node name>

*Seed skeleton for an interior node that DECOMPOSES. The 7-section spine (SPN) plus an explicit
children-and-seams block — the seams are THIS node's plan to review (COV), not a child's.*

## 1. Problem / intent
## 2. Approach
*Includes: why this node decomposes rather than being a leaf (the granularity call, GRN).*
## 3. Interfaces & seams
## 4. Outputs & artifacts (WITH their locations)
## 5. Failure modes & contingencies
## 6. State / restart story
## 7. Verification

## Decomposition — children and the seams between them
*Name each child node and the contract between them. A between-child contingency is caught by THIS
node's cold passes, not lost in the gap between separate child reviews (COV).*

| Child node | What it owns | Seam / interface to its siblings |
|---|---|---|
| `<child-a>` | … | hands `<child-b>` … ; shares contract … |
| `<child-b>` | … | consumes from `<child-a>` … ; hands parent … |

**Granularity note (GRN/DEC):** each child's estimated leaf-count / work-size vs. this node's — the
decomposition must **reduce** granularity (a child ≥ 0.8× the parent trips the convergence guard).

**Top-level only (TOP):** if this is the root's first split, dispatch is blocked until `plan/topgate/`
approval exists on disk. Deeper splits proceed red-team-gated, autonomous.
