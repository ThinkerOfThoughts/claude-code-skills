# overnight-run config: companion-emergence (Layer 2)

Per-project config for the `overnight-run` skill. SKILL.md reads the config beside it whose `project_dir:`
is the lane's working directory or a parent of it; none found: it stops and says so.

```yaml
project: companion-emergence
project_dir: ~/Desktop/companion-emergence

# The owner lane is the lane whose own handoff doc is this one (the Planning lane).
# It keeps the run record and the morning list, and runs set-up, the egg timer and run end.
owner_handoff_doc: ~/.claude/plans/memory-dream-rework-PLANNING-plan.md

watchdog: ~/Desktop/Scripts/usage_watchdog.sh

# Lanes are named by session title and found with the session list tool.
# The owner's per-run list (reset time, lanes, work, whether GitHub text waits) replaces this default.
default_lanes:
  - "the Planning lane"
  - "The Great Bughunt: Fixing"

# The project's guard that asks the owner. The skill never touches it; the set-up step only asks.
guard:
  name: "the persona-data guard"
  setup_line: "The persona-data guard stays on unless you switch it off yourself for tonight. With it on, a lane that touches guarded data waits for you until morning. Switch it off for this run?"
```
