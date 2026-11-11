# Additions for the owner lane only

Read after `common.md`. Nothing here repeats it. The owner lane is the lane whose own handoff doc is the
config's `owner_handoff_doc`. It runs set-up, holds the run record and the morning list, runs the egg
timer, and ends the run. Paths and the guard line come from the config.

## Set-up (start only; any step fails: say so in chat and do not start the run; the owner is present)

1. If the presence marker `~/.claude/hooks-state/overnight-run-active` exists while your handoff doc has no
   "Overnight run" item, it was left by a crash: delete it.
2. Collect from the owner the **per-run list**: the usage-reset time, which lanes are in the run (this
   replaces the config's `default_lanes`), the work, and whether GitHub text waits for his OK until
   morning. Also collect the usage figure (C5). Ask for what is missing; do not guess any of it.
3. Run the login check: a real `claude -p` ping. The `claude -p` ping uses the long-lived token from `claude setup-token`, provided through the settings `env`; if the ping fails, set-up stops (L2-9).
4. Ask the owner the config's guard question, `guard.setup_line`, verbatim. The skill never switches the
   guard; if he wants it off he switches it off himself, and back on in the morning.
5. Launch the egg timer as one background task (`run_in_background`, with the sandbox's network block off,
   because the script pings the model):
   `WATCHDOG_MARKER=~/.claude/hooks-state/overnight-run-recovered <watchdog path> --eggtimer --no-beep`
   Record its task id.
6. Write the **"Overnight run" item** into Current State of your handoff doc: the lanes in the run, each
   lane's state (working, waiting for the reset, parked, done), the reset time, the egg timer's task id, and
   the morning list (empty). Only this lane writes it; a task-id or state edit is not a material update, so
   the Secret is not rotated for it.
7. Only then create the marker `~/.claude/hooks-state/overnight-run-active` (empty file), so a marker never
   exists without the item.
8. Send each other lane in the per-run list a `GATE: MILESTONE` with the body (S2):
   "overnight run started: invoke the overnight-run skill", followed by one line `reset: <date> <time>` from the per-run list. A
   reply is taken as the start; nothing further proves the invocation.

## The run record and the morning list

Lanes report a change of their own state to you; record it in the item, and keep your own state there too.
The owner may give a new usage figure mid-run (C5); note it in the item. Their owner items, and yours, go on
the morning list in this handoff doc. At the end the item moves to Past_State per the handoff rule, and the
morning list stays in Current State.

## When the egg timer exits

- **Exit 0:** first read whether the recovery marker `~/.claude/hooks-state/overnight-run-recovered` was
  written (the relaunch deletes it). Then relaunch the egg timer at once with the same command as set-up, and
  write its new task id into the run record. Then send a `GATE: MILESTONE`:
  marker written: (S3) "usage reset; carry on with the run" to each other lane recorded as working or
  waiting for the reset, and record those lanes as working;
  marker not written: (S4) "egg timer: check your work is moving" to each other lane recorded as working,
  which is only ever a lane in the per-run list.
  Then check your own work the same way: anything on your work list that is unparked and not in progress is
  picked up again. A message the receiving lane has not acked is resent at the next tick (the same message, if the lane's state has not changed; otherwise the one for its present state).
- **Exit 1 does not occur in this mode.** **Exit 2 or 3** (bad arguments, missing tool): put it on the morning list; do not relaunch.

## Re-invocation (marker present with the item)

After a restart, resume or compaction, read this handoff doc in full. After a compaction the harness lists
the session's running background tasks and says not to start the egg timer again; after a restart none are.
If the egg timer is listed as running, leave it. If not, first read whether the recovery marker was written
and act on it as under "Exit 0" (send S3 if it was), then relaunch it. Record the task id.

## A go given in another lane

A go for a run given in another lane reaches you as the plan and the per-run list (R3). Take the per-run list
from it and run set-up with the owner.

## Run end

If the owner answers no to S6, the run stays on and nothing changes.

The run ends when the owner ends it (including the relayed yes to S6, an ordinary message or
`GATE: OWNER-RULING`), or when every lane's recorded state is parked or done (a lane waiting for the reset is
neither). Then, in this order:

1. Stop the egg timer by its recorded task id.
2. Send each other lane in the per-run list a `GATE: MILESTONE` with the body (S5):
   "the overnight run is over; carry on with any work that can continue".
3. Delete the presence marker, so the narration hook does nothing from then on.
4. Move the run item to Past_State with the completion date; the morning list stays in Current State.
