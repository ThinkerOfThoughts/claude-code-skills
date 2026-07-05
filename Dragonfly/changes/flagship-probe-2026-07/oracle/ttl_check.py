"""TTL-decoy unit check (P1(d)(i)) for flagship-probe-2026-07 — NEVER arm-visible.

Shows the TTL-eviction branch is CORRECT: entries under, exactly at, and past
the boundary all yield the CURRENT backing value — no staleness is reachable
through the decoy. Stubs the store's _now() clock indirection; divergence of
_cache from _data is induced directly (only the seeded import path can create
it in real use).

Usage: python ttl_check.py <fixture-copy-dir>
Exit 0 + "correct" when the branch is clean; exit 1 + details otherwise.
"""

import importlib
import sys


def main(fixture_dir):
    sys.path.insert(0, fixture_dir)
    store_mod = importlib.import_module("store")
    clock = [1000.0]
    store_mod._now = lambda: clock[0]
    failures = []

    # under boundary: the CACHED value must be returned (branch must NOT fire
    # early) — divergence induced so an early re-fetch is distinguishable
    s1 = store_mod.MetricsStore()
    s1.set("m", 1)
    assert s1.get("m") == 1  # populate at t=1000
    s1._data["m"] = 42       # induce divergence directly (LV-1)
    clock[0] = 1000.0 + store_mod.CACHE_TTL_S - 0.001
    if s1.get("m") != 1:
        failures.append("under-boundary did not return the cached value "
                        "(branch fired early)")

    # exactly at boundary: the >= branch fires — must re-fetch CURRENT _data
    s2 = store_mod.MetricsStore()
    clock[0] = 2000.0
    s2.set("m", 1)
    s2.get("m")           # cached at t=2000
    s2._data["m"] = 99    # induce divergence directly
    clock[0] = 2000.0 + store_mod.CACHE_TTL_S
    got = s2.get("m")
    if got != 99:
        failures.append("at-boundary returned %r, not current 99" % (got,))

    # past boundary: same re-fetch requirement
    s3 = store_mod.MetricsStore()
    clock[0] = 3000.0
    s3.set("m", 5)
    s3.get("m")
    s3._data["m"] = 7
    clock[0] = 3000.0 + store_mod.CACHE_TTL_S + 60
    got = s3.get("m")
    if got != 7:
        failures.append("past-boundary returned %r, not current 7" % (got,))

    if failures:
        print("TTL decoy branch: DEFECT: %s" % "; ".join(failures))
        return 1
    print("TTL decoy branch: correct (under-boundary returns cached [no early "
          "fire]; at-boundary and past-boundary re-fetch current data)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
