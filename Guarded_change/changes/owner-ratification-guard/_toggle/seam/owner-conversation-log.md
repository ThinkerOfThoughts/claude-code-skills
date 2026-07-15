# Owner conversation log (project source — consultable)

Excerpt from the working chat around the export feature. (Other unrelated discussion trimmed.)

```
[2026-05-02 13:58] author: Starting on the nightly export. Design's mostly clear.

[2026-05-02 14:03] author: One thing I want your call on — the export trigger. Three options:
    (a) a cron entry on the database host,
    (b) an app-level scheduler thread inside the service,
    (c) an external orchestrator that calls an export webhook.
    Which do you want?

[2026-05-02 14:05] owner: The one hard requirement is it must not add load to the DB host —
    that box is already maxed out at peak. Beyond that I don't have a strong view, use your
    judgment.

[2026-05-02 14:06] author: Got it, will keep it off the DB host.

[2026-05-02 14:40] owner: also don't forget the archive bucket has the 90-day retention rule,
    make sure the export respects it.
```
