# Plan node: add a Redis read-through caching layer to the product-catalog API

**Altitude:** root / candidate leaf. **Template:** create-new.

## 1. Problem / intent
p99 latency on `GET /products` and `GET /products/{id}` is ~380ms under load because every read hits
Postgres. Add a Redis read-through cache in front of the catalog read path to cut p99 to <120ms
without serving stale prices.

## 2. Approach
Wrap the catalog read repository in a cache-aside/read-through decorator: on read, check Redis by key
`product:{id}` (and `products:page:{n}` for list pages); on miss, load from Postgres, populate Redis
with a TTL, return. Keep the Postgres repository untouched behind the decorator so the change is
additive.

## 3. Interfaces & seams
- Upstream: the HTTP handlers call `CatalogReader` — unchanged interface, now backed by the decorator.
- Downstream: Redis (new dependency) and the existing Postgres repo.
- Contract: `CatalogReader.Get(id)` / `.List(page)` semantics identical to today; only latency changes.

## 4. Outputs & artifacts (with their locations)
- `internal/catalog/cache/redis_reader.go` — the read-through decorator.
- `internal/catalog/cache/keys.go` — key-scheme helpers.
- `deploy/redis.yaml` — the Redis instance manifest (new).
- Config keys `CACHE_REDIS_URL`, `CACHE_TTL_SECONDS` added to `config/service.yaml`.
- A short ADR at `docs/adr/0042-catalog-cache.md` recording the decision.

## 5. Failure modes & contingencies
- Redis down → decorator falls through to Postgres (degrade, not fail); log + metric.
- Cache stampede on cold key → single-flight guard around the Postgres load.

## 6. State / restart story
Cache is disposable derived state; a restart/flush re-warms lazily on reads. No durable state added.

## 7. Verification
Load test showing p99 < 120ms with cache warm; correctness test showing a write invalidates the key
and the next read reflects it.

## Layer-2 required sections
### Cache-invalidation strategy
On any write to a product (`PUT/PATCH /products/{id}`, price updates via the admin path), delete
`product:{id}` and bust the affected `products:page:*` keys via a tag set. Writes are the source of
truth; the cache is invalidated synchronously in the write path before the write returns.

## Granularity
**Leaf.** One agent can implement this from the spec; no decomposition.
