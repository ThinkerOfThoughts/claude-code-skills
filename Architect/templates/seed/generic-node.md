# Plan node — <node name>

*Generic seed skeleton: the 7-section universal spine (SPN). Fill every section; §4 is never omitted.*

## 1. Problem / intent
What this node plans and why. The altitude (root / branch / candidate leaf) and the slice of the
parent's seams it owns.

## 2. Approach
How, at this node's altitude. The strategy, the key choices, the alternatives considered.

## 3. Interfaces & seams
Contracts to parent, siblings, children, and any consuming skill/human. What this node consumes and
emits; the shared contracts a sibling depends on.

## 4. Outputs & artifacts (WITH their locations)
The deliverables **and where each lands** — on-disk / output-folder layout, filenames, the run tree.
*This is the founding-failure section; its silent absence is the exact failure this skill guards. State
every output location explicitly.*

## 5. Failure modes & contingencies
What can go wrong and the fallback for each. The known risks and how the plan degrades.

## 6. State / restart story
For anything long-running or multi-agent: how it resumes without loss. What is on disk, what the
not-done marker is, what a HARDSTOP re-runs.

## 7. Verification
How you'd know this node is done/correct — the checkable done-criteria.

---
*Layer-2 `required_sections` for this plan-type are appended below the spine. The generative
completeness critic (tier iii) still hunts for the load-bearing section on **neither** list.*
