"""Hidden oracle for flagship-probe-2026-07 — NEVER in an arm-visible copy.

Exhibits the reported symptom (stale dashboard read after the data has
definitely been updated) via the seeded path: the bulk-import fast path
bypasses cache invalidation.

Usage: python repro.py <fixture-copy-dir>
Exit 1 + "STALE" when the symptom is exhibited; exit 0 + "FRESH" when the
copy under test is clean (the skill's detector bar: silent-on-clean).
"""

import importlib
import sys


def main(fixture_dir):
    sys.path.insert(0, fixture_dir)
    store_mod = importlib.import_module("store")
    importer = importlib.import_module("importer")

    s = store_mod.MetricsStore()
    s.set("p95_latency_ms", 480)                          # baseline write
    first = s.get("p95_latency_ms")                       # read-through: caches 480
    importer.import_records(s, {"p95_latency_ms": 512})   # "definitely updated"
    second = s.get("p95_latency_ms")                      # dashboard read after update

    print("first read: %r; after import: %r (expected 512)" % (first, second))
    if second != 512:
        print("STALE")
        return 1
    print("FRESH")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
