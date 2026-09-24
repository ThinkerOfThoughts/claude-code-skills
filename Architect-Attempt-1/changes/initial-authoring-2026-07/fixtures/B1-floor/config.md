# Layer-2 planning config (fabricated) — B1 floor fixture

```yaml
plan_type: add-caching-layer

domain_context: |
  The thing being planned: add a Redis read-through caching layer in front of the product-catalog
  read path of an existing REST service (GET /products, GET /products/{id}). The service is a Go
  binary deployed as a container; product data lives in Postgres. Goal is to cut p99 read latency.
  A cold agent judging completeness should know: this is a production service; cache invalidation on
  writes matters; the deliverable is a plan another agent will implement.

scale_context: |
  Small. One leaf-sized change to one service. Expect a single low-level pass, no decomposition.

required_sections:            # Layer-2 tier-(ii), ON TOP OF the 7-section spine
  - "Cache-invalidation strategy: how writes keep the cache correct (why load-bearing: a stale cache
     silently serves wrong prices)."

catalog: ~/.claude/architect/templates/
off_limits_paths:
  - <the product-catalog service repo>   # read-only context; the run never writes here
run_root: <scratch dir OUTSIDE the service repo>
```
