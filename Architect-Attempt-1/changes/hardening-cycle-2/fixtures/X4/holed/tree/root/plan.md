# Plan node — root  (mode: fresh — the config declares no `mode:` key, so the default applies)

## 1. Problem / intent
Split the Python billing service out of the monolith into extract + cutover, without corrupting invoices.

## 2. Approach
Two children: `extract` (lift invoicing into its own package behind the existing interface) and `cutover`
(route traffic, then decommission the monolith path).

## 3. Interfaces & seams
`extract` publishes the invoicing package's public surface; `cutover` consumes exactly that surface and
nothing else. Seam: the invoice state-transition contract.

## 4. Outputs & artifacts (with their locations)
- `tree/root/extract/plan.md`, `tree/root/cutover/plan.md` — the two child plan nodes.
- `assembled-plan.md` at the run root — the presentable deliverable.

## 5. Failure modes & contingencies
Partial backfill corrupts invoices ⇒ the backfill is idempotent and re-runnable from a checkpoint.

## 6. State / restart story
Per-node dirs under `tree/`; a restart walks `tree/` for the first missing deterministic output.

## 7. Verification
Reconciliation job output matches the monolith's for one full nightly cycle before decommission.

## Layer-2 required sections (from the config's required_sections)
- **Data-migration & backfill plan** — checkpointed, idempotent, verified per batch.
- **Rollback story** — traffic routing is a single flag; the monolith path stays warm for one cycle.

## Proposed granularity (GRN)
DECOMPOSE into two children. elc (self-declared estimated leaf count): 6.
