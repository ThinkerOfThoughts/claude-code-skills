# Stage 8 — Close

When the build merges (or is abandoned):
1. Add an `As built` line per sheet entry: matches / deviates (with the commit or PR line) / dropped.
   Any deviation on an owner line that the owner has not approved is reported to the owner before closing.
2. Move OPEN forks that shipped as working assumptions into tracked issues (one issue per fork), and
   record the issue numbers.
3. Set `status: CLOSED`, final Secret token rotation, and a one-line pointer from the project's handoff
   doc to the ledger.
4. If the project keeps a lessons doc, append only lessons that carry a quote or a line reference.
