# B2 structural observables (total coverage + gate-before-present)

The B2 tree is a 3-node tree (root + child-A + child-B). It exercises **total coverage** (COV) and
**gate-before-present** (GBP):

```
tree/                      ← ROOT node (owns the top-level split + the seams between children)
├─ plan.md                 ← root plan WITH a planted ROOT hole (§5 missing) + a planted SEAM hole
│                            (token-format/signing-key contract between A and B unspecified)
├─ completeness/           ← 3 cold-agent completeness records for the ROOT (gate #1) — produced by the
│                            harness dispatch (A.md,B.md,C.md); the ROOT owner reviews its own slice
│                            incl. the between-child seams
├─ adversarial/            ← 3 cold-agent adversarial records for the ROOT (gate #2) — structural slot
├─ child-A/  {plan.md, completeness/, adversarial/}   ← leaf, clean
└─ child-B/  {plan.md, completeness/, adversarial/}   ← leaf, clean
```

**What B2 proves and how it is observed here:**

1. **Coverage includes the root + between-branch seams, not leaf-only (the load-bearing novelty).**
   The two planted holes live at the ROOT altitude (a root §5 gap) and in the ROOT's between-child
   seam block (token contract). Neither is inside child-A or child-B, so a leaf-only review would miss
   both. The harness dispatches the completeness pass **on the ROOT node** (the owning orchestrator's
   own slice) and confirms it catches **both** — recorded in `tree/completeness/{A,B,C}.md`.

2. **Both passes, 3 records each, at every node incl. root (COV + PASS1/PASS2).** Every node dir has a
   `completeness/` and an `adversarial/` slot; each is filled with 3 verbatim records before the node
   finalizes. The ROOT is not exempt (the top orchestrator does not self-certify).

3. **Completeness recorded before adversarial (PASS-ORD).** `completeness/` is written before
   `adversarial/` at each node.

4. **Gate-before-present (GBP):** while the ROOT carries an unresolved planted finding, **no
   `assembled-plan.md`** exists at the fixture root. `tree-clean/` is the discrimination twin — the
   holes fixed and all nodes gated clean → `assembled-plan.md` present (a clean tree finalizes; the
   gate blocks holes, not progress).
