"""Decoy-conformance hammer for flagship-probe-2026-07 — NEVER arm-visible.

Concurrent writer/reader threads on the store's PUBLIC API only (set/get,
no importer). Staleness predicate = POST-JOIN PERSISTENCE: after all threads
join, get(k) must equal the last value written to k (one writer per key, so
"last" is well-defined). In-flight reads of a pre-set value during an
overlapping write are legal and are NOT counted.

Per P1(d)/R2-5 the hammer is itself a detector: it is first validated
fire-on-known-true against a race-restored (lock-removed) copy — it must
fire (exit 1) within the pre-stated bound of <=50 runs — then run on the
shipped store, where it must find zero stale post-join reads across the
full 50 runs (exit 0).

Each run is a batch of small 3-thread trials (1 paced writer + 2 readers on
one key) rather than one big many-thread melee: a barrier synchronizes the
start (thread wake latency otherwise serializes tiny loops entirely), and
the writer paces its sets so its run spans the readers' activity — pacing
is harness-side scheduling, the store code is exercised as-is.

Usage: python hammer.py <fixture-copy-dir> [runs]   (runs defaults to 50)
"""

import importlib
import sys
import threading
import time

TRIALS_PER_RUN = 200
WRITES_PER_TRIAL = 20
WRITE_PACE_S = 0.0001
READS_PER_READER = 30
FINAL = WRITES_PER_TRIAL  # last value the writer writes


def one_trial(store_mod):
    s = store_mod.MetricsStore()
    s.set("k", 0)
    s.get("k")  # populate the cache so the writer's pops create misses
    barrier = threading.Barrier(3)

    def reader():
        barrier.wait()
        for _ in range(READS_PER_READER):
            s.get("k")

    def writer():
        barrier.wait()
        for i in range(1, WRITES_PER_TRIAL + 1):
            s.set("k", i)
            time.sleep(WRITE_PACE_S)

    threads = [threading.Thread(target=reader),
               threading.Thread(target=reader),
               threading.Thread(target=writer)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    got = s.get("k")  # post-join read: must see the last written value
    return None if got == FINAL else got


def main(fixture_dir, runs):
    sys.setswitchinterval(0.00001)  # frequent switches; safe at 3 threads
    sys.path.insert(0, fixture_dir)
    store_mod = importlib.import_module("store")
    for run in range(1, runs + 1):
        for trial in range(1, TRIALS_PER_RUN + 1):
            stale = one_trial(store_mod)
            if stale is not None:
                print("run %d/%d trial %d: post-join get('k') == %r, expected %r"
                      % (run, runs, trial, stale, FINAL))
                print("FIRED")
                return 1
    print("no stale post-join reads in %d runs (%d trials each)"
          % (runs, TRIALS_PER_RUN))
    print("CLEAN")
    return 0


if __name__ == "__main__":
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    sys.exit(main(sys.argv[1], n))
