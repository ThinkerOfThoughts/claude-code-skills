"""Bulk-load helpers for the metrics store."""


def import_records(store, records):
    """Fast path for bulk loads: update the backing dict in one call
    instead of going through set() per key."""
    with store._lock:
        store._data.update(records)
