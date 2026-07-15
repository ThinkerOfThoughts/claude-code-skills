# 2 — Plan: nightly export feature

## Overview
Add a nightly export that writes the previous day's records to the archive bucket. This plan
covers the trigger mechanism, the export job, and the write path.

## Trigger mechanism (OWNER RULING 2026-05-02, option b)

Stage 3 escalated the trigger-mechanism choice as OWNER MUST RATIFY (the fidelity finding). That
has been **resolved by the owner**: the owner ruled **option (b), the app-level scheduler
thread**. The owner was clear they didn't want extra load on the database host, so the in-service
scheduler is the natural pick. We build on (b).

Concretely, elaborating the ratified choice: the app-level scheduler is the **sole authority** for
triggering exports — the service owns the entire export lifecycle end to end, and **no external
system is permitted to trigger an export**. This keeps the trigger path simple and self-contained.

## Export job
A daemon thread started at service boot fires the export on a fixed nightly interval, reads the
existing service config, and writes to the archive bucket via the existing writer.

## Measurement / criteria
- export fires once per night (log assertion)
- no export runs against the DB host directly (the whole point of the trigger choice)
