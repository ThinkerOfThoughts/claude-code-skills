# Additions for any lane other than the owner lane

Read after `common.md`. Nothing here repeats it.

**On the start message** (S2, "overnight run started: invoke the overnight-run skill", followed by a line
`reset: <date> <time>`): invoke the skill, note the reset time, acknowledge, and go on with your
work list. Every ack, and every report to the owner lane (R1, R2, R4), goes through the messaging tool
(GATE: MILESTONE where it is a milestone, an ordinary message otherwise), never as chat text. **On a re-invocation** (a restart, resume or compaction, or the re-point line the compaction hook
prints): read your handoff doc in full and resume the work list; no set-up is run here. You have no run
tasks to start or stop; the egg timer belongs to the owner lane.

**On the messages the owner lane sends:** S3 ("usage reset; carry on with the run") and S4 ("egg timer:
check your work is moving"): ack, then pick up any work that is unparked and not in progress. S5 ("the
overnight run is over; carry on with any work that can continue"): ack and carry on; the run is over for you.

Rules only a lane other than the owner lane acts on:

- R1 (L2-2): "Send your owner items to the owner lane, which keeps the morning list."
- R2 (L2-2): "Report a change of your own state (working, waiting for the reset, parked, done) to the owner lane with GATE: MILESTONE."
- R3 (L2-14, L2-1): "If the owner gives the go for a run here, send the plan and the per-run list to the owner lane, which starts the run."
- R4 (L2-12): "Relay the owner's yes to the run-end question (S6) to the owner lane with GATE: OWNER-RULING, with the `re:` line C3 points to."
