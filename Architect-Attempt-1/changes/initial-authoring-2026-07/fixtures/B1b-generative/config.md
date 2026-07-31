# Layer-2 planning config (fabricated) — B1b generative fixture

```yaml
plan_type: add-collaborative-editing

domain_context: |
  The thing being planned: add REAL-TIME COLLABORATIVE editing to an existing single-writer document
  service, so MULTIPLE users can edit the SAME document SIMULTANEOUSLY (Google-Docs-style). Documents
  are rich text stored server-side; clients are web browsers over WebSocket. The core hard problem of
  this domain is that two users editing the SAME region at the SAME time must not corrupt or lose each
  other's edits. A cold agent judging completeness should know this is the defining challenge of
  concurrent collaborative editors.

scale_context: |
  Medium-small. One feature on one service. A single low-level pass is fine; not a deep tree.

required_sections:            # Layer-2 tier-(ii), ON TOP OF the 7-section spine. THESE are the
                              # anticipated collaborative-editing sections. NOTE: no conflict-resolution
                              # / concurrent-edit-merge section is named here.
  - "Sync protocol & message schema: the WebSocket message types and wire format for edits."
  - "Client reconnection handling: how a client that drops and reconnects catches up on missed edits."
  - "Presence / awareness: how each client shows the other editors' cursors and selections."

catalog: ~/.claude/architect/templates/
off_limits_paths:
  - <the document-service repo>
run_root: <scratch dir OUTSIDE the service repo>
```
