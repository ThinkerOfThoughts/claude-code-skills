# Assembled plan — import-and-report

*Consumer-agnostic: no downstream contract is targeted. A consumer checks this against its own
ingestion needs.*

## Execution order
1. `branch-a` (import)  — no prerequisites
2. `branch-b` (report)  — requires branch-a
Parallel groups: none (a single dependency chain).

## root  [gate: clean]
(the root plan's seven sections, elided in this fixture)

### branch-a  [gate: clean]   fixed_findings: none   demoted_findings: none
(elided)

### branch-b  [gate: clean]   fixed_findings: none   demoted_findings: none
(elided)
