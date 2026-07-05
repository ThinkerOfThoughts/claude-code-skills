"""Nightly sync: pull the latest upstream metric snapshot into the store.

Runs as an offline nightly job (cron): loads the upstream snapshot file
and bulk-imports it.
"""

import json

from importer import import_records


def run_nightly_sync(store, snapshot_path="upstream_records.json"):
    with open(snapshot_path) as f:
        records = json.load(f)
    import_records(store, records)
    return len(records)
