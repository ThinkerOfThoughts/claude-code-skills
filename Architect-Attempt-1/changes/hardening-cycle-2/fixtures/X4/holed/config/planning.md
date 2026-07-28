# architect planning config — migrating a billing service (Layer-2)

```yaml
plan_type: service-migration

domain_context: |
  A Python billing service moving from a monolith to two services. Consumers are an internal admin UI
  and a nightly reconciliation job.

scale_context: |
  Medium-large. Expect a root split into extract / cutover, each decomposing once more.

required_sections:
  - "Data-migration & backfill plan (why load-bearing: a partial backfill silently corrupts invoices)."
  - "Rollback story (why load-bearing: a cutover with no rollback is a one-way door)."

catalog: ~/.claude/architect/templates/

off_limits_paths:
  - /srv/billing            # the target repo — read-only context
  - /srv/billing-legacy     # source to cite, never to modify

run_root: ~/architect-runs/billing-migration/
```
