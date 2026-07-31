# Plan node: add real-time collaborative editing to the document service

**Altitude:** root / candidate leaf. **Template:** create-new.

## 1. Problem / intent
Today the document service is single-writer (one editor locks a doc). Add real-time collaborative
editing so multiple users edit the same document simultaneously and see each other's changes live.

## 2. Approach
Open a WebSocket per editing client. Each keystroke/edit is sent as an edit message to the server,
which fans it out to the other connected clients for that document. The server holds the authoritative
document and applies incoming edits to it, persisting periodically.

## 3. Interfaces & seams
- Client ↔ server: WebSocket at `/docs/{id}/live`.
- Server ↔ store: the existing document repository, now written by the live-edit path.
- Server ↔ existing single-writer save path: the two must not both write; the live path supersedes it
  while a live session is open.

## 4. Outputs & artifacts (with their locations)
- `internal/live/socket.go` — the WebSocket endpoint and connection registry.
- `internal/live/fanout.go` — per-document broadcast of edit messages.
- `internal/live/apply.go` — applies an incoming edit to the server-side document.
- `web/src/live/client.ts` — the browser client (send local edits, render remote edits).
- Config `LIVE_MAX_CLIENTS_PER_DOC`, `LIVE_PERSIST_INTERVAL_MS` in `config/service.yaml`.

## 5. Failure modes & contingencies
- WebSocket drops → client reconnects (see reconnection section) and resyncs.
- Server crash mid-session → clients reconnect to a healthy instance; last persisted doc is the
  recovery point.
- Malformed edit message → rejected and logged; the connection is not torn down.

## 6. State / restart story
The authoritative document lives server-side and is persisted every `LIVE_PERSIST_INTERVAL_MS`. On
server restart, the last persisted version is loaded and clients resync from it.

## 7. Verification
Integration test: two clients connected to one doc; edits from client A appear at client B within
200ms; a reconnecting client catches up; presence cursors render.

## Layer-2 required sections

### Sync protocol & message schema
Edit messages: `{type:"insert"|"delete", pos:int, text?:string, len?:int, clientSeq:int}` over the
WebSocket, plus `{type:"cursor", pos, selEnd}` for presence and `{type:"ack", serverSeq}` from server.

### Client reconnection handling
On reconnect the client sends its last-seen `serverSeq`; the server replays edits after that seq, or
sends a full document snapshot if the client is too far behind.

### Presence / awareness
Each client publishes its cursor/selection via `cursor` messages; the server fans them out; clients
render remote cursors with a per-user color and name label.

## Granularity
**Leaf.** One agent can implement this from the spec; no decomposition.
