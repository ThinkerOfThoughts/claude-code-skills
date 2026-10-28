# B3 fixture — scale-down: a small task completes in a single pass (leaf, no decomposition)

**Fabricated small task:** "Add a `--version` flag to an existing CLI tool that prints the build
version string and exits 0."

## Layer-2 (fabricated)
```yaml
plan_type: small-cli-change
scale_context: |
  Small. One trivial change to one file. Expect a single low-level pass, granularity = leaf.
required_sections: []
```

## Expected run tree (the observable)
```
run-root/
├─ index.md            ← "root: template=leaf-task-spec, status=gated-clean, granularity=LEAF"
├─ plan/decisions.md   ← gate entry: root, worst=CLEAN, route=stage6→LEAF
└─ tree/
   └─ _status.md       ← "granularity: LEAF; children: none"
   └─ plan.md          ← the 7-spine collapsed to an atomic task spec; NO child dirs
```

## What B3 asserts (oracle) and how the harness verifies it
- **The root's granularity check returns `leaf`; the run tree has NO child nodes under the root.**
  Verified by walking the skill's **GRN** rule (SKILL.md "Scale" + stage-6 step 2 + METHODOLOGY GRN):
  a small task's root returns leaf → a single low-level pass, no forced decomposition. The two red-team
  passes validate the leaf call; done.
- **Oracle-can-fail (discrimination):** the SAME granularity check **would** decompose a large task —
  see `../B4-scaleup/` (a large task decomposes recursively). The leaf decision is a real
  discrimination (small→leaf, large→decompose per GRN + scale_context), not a hard-wired "always leaf."
  If the check always returned leaf, B4 could not decompose — and it does.

## index.md (fixture stub)
```
node: root
template: leaf-task-spec
granularity: LEAF
children: none
gate: gated-clean (both passes clean-or-resolved)
```
