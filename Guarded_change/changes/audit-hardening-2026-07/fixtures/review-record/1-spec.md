# 1 — Spec: uploader-retry-backoff

## Problem

`export/uploader.py` gives up on the first HTTP failure. Transient 5xx from the storage
backend (deploy windows, rate-limit bursts) abort the nightly export, and the operator has to
re-run it by hand the next morning. We want automatic retry with exponential backoff.

## Why

Three aborted exports in the last month (ops log 06-04, 06-17, 06-28), each a transient 503
that succeeded on manual re-run.

## Constraints

- No new dependencies; use stdlib timing.
- Must not risk duplicate uploads (the backend has no idempotency key).
- Nightly window is 40 min; total retry budget ≤ 90 s per object.

## Touched files (expected)

- `export/uploader.py`
- `export/tests/test_uploader.py`
