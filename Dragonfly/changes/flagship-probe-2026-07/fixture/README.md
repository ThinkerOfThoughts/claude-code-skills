# metrics-store

Small in-memory metrics store with a read-through cache.
Writes go through `MetricsStore.set()`; bulk nightly loads go through `sync.run_nightly_sync()`.
Reads (`dashboard.render()`) go through `MetricsStore.get()`.
Run the tests with `pytest -q` from this directory.
