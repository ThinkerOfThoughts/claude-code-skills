# B5 fixture — executed evidence (template reuse + back-propagation)

Ran against a real git catalog under `../../8-harness-runs/B5-catalog/` and a run under
`../../8-harness-runs/B5-run/`. All four sub-claims exercised mechanically:

- **Match/instantiate (TPL1):** `matched-node/plan.md` is instantiated from the catalog
  `generic-node.md` skeleton; `index.md` records `template: generic-node`.
- **Back-propagation (TPL3):** a hole-fix (§4 must pin the build-manifest/checksum location) applied
  on the node was ALSO applied to the skeleton and committed to the user-space catalog — visible as a
  NEW commit `back-propagate hole-fix (TPL3)…` in `git log` (commit 78e8c96 on top of the seed commit).
- **Discrimination (a):** `novel-node` matched no skeleton -> recorded `template: create-new` (planned
  from the bare spine), NOT a spurious nearest-neighbour instantiation (TPL1 "never force a match").
- **Discrimination (b):** a clean node with NO hole-fix produced NO catalog commit (commit count
  unchanged 2->2) — back-prop fires on a real fix, not always.
