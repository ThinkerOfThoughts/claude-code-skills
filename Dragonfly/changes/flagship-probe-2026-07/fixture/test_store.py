from store import MetricsStore


def test_write_then_read():
    s = MetricsStore()
    s.set("requests_per_s", 120)
    assert s.get("requests_per_s") == 120
    s.set("requests_per_s", 150)
    assert s.get("requests_per_s") == 150


def test_cache_returns_value():
    s = MetricsStore()
    s.set("error_rate", 0.02)
    assert s.get("error_rate") == 0.02
    assert s.get("error_rate") == 0.02
