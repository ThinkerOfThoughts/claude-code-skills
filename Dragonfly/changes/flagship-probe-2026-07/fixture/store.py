"""In-memory metrics store with a read-through cache.

Values are written via set() and read via get(); reads populate a cache so
hot keys avoid repeated backing-dict lookups. Cached entries older than
CACHE_TTL_S are re-fetched on access.
"""

import threading
import time

CACHE_TTL_S = 300  # cached entries older than this are re-fetched on access


def _now():
    """Clock indirection (kept separate so tests can stub time)."""
    return time.monotonic()


class MetricsStore:
    def __init__(self):
        self._data = {}
        self._cache = {}  # key -> (value, cached_at)
        self._lock = threading.Lock()

    def set(self, key, value):
        """Write a metric value and drop any cached copy of it."""
        with self._lock:
            self._data[key] = value
            self._cache.pop(key, None)

    def get(self, key):
        """Read a metric value through the cache."""
        with self._lock:
            entry = self._cache.get(key)
            if entry is not None:
                value, cached_at = entry
                # TODO: revisit boundary — >= treats an entry exactly at the
                # TTL as already expired; off by one?
                if _now() - cached_at >= CACHE_TTL_S:
                    value = self._data[key]
                    self._cache[key] = (value, _now())
                return value
            value = self._data[key]
            self._cache[key] = (value, _now())
            return value

    def keys(self):
        with self._lock:
            return sorted(self._data)
