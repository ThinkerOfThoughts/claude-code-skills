# Plan node — root
## 1. Problem / intent
Plan the whole import-and-report job. Altitude: root. No parent.
## 2. Approach
Decompose into branch-a (import) and branch-b (report). elc: 9 (self-declared).
## 3. Interfaces & seams
branch-a hands branch-b a normalized table; both share the schema contract.
## 4. Outputs & artifacts (with their locations)
`assembled-plan.md` at the run root.
## 5. Failure modes & contingencies
A branch cannot meet the schema contract -> re-draft this node's seam slice.
## 6. State / restart story
All state on disk under `tree/`.
## 7. Verification
Both branches gated clean and assembled.
