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

redteam_context:            # priority-ordered; every cold agent MUST read these to check the plan's
                            # claims against the world it plans in. Distinct from off_limits_paths
                            # (a never-write fence) — a path may legitimately be both.
  - path: /srv/billing/app/invoicing/
    note: THE CODE BEING MIGRATED — check any claim about current invoice state transitions here first.
  - path: /srv/billing/docs/schema.md
    note: the live schema; check the backfill plan's column claims against it.
  - path: /srv/billing-legacy/README.md
    note: why the legacy path exists; check the rollback story's assumptions.

catalog: ~/.claude/architect/templates/

off_limits_paths:
  - /srv/billing            # the target repo — read-only context
  - /srv/billing-legacy     # source to cite, never to modify

run_root: ~/architect-runs/billing-migration/

mode: ingest-and-complete   # fresh | ingest-and-complete   (default: fresh)
ingest_source: ~/drafts/billing-migration-draft.md

```
