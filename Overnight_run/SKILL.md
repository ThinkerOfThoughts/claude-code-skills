---
name: overnight-run
description: "Use only when the owner starts an unattended overnight run across several lanes (separate sessions), or when a start or re-point message says to invoke this skill. Sets up the run (usage-reset egg timer, login ping, run record and morning list in the owner lane's handoff doc) and holds every lane to the same overnight rules. Do not use in any other session."
hooks:
  Stop:
    - hooks:
        - type: command
          command: "python3 ~/.claude/hooks/narration_guard.py"
          timeout: 10
---

# Overnight Run

Purpose: **while the owner is away, nobody reads the chat, so the run keeps chat empty, keeps one record
of where everything stands, and wakes itself when usage resets.** The failures it prevents: narration into
an unread chat, a question that points at an earlier message, an owner instruction that never reaches the
other lanes, a handoff doc that is not current, a usage reset nobody wakes for, and a failed login found
only at the first call. This file is the **router**; the rules live in `stages/`. `README.md` has the why,
the install and the known limits.

## Inputs

- **A project config** (Layer 2): `overnight-run.*.md` beside this file. Use the one whose `project_dir:`
  line is the lane's working directory or a parent of it. If none is found, stop and say so; do not guess
  paths.
- **The lane's own handoff doc**, to tell whether this lane is the owner lane (config `owner_handoff_doc`).

## Step 1: start or re-invocation

Check the presence marker `~/.claude/hooks-state/overnight-run-active` and the owner lane's handoff doc.

- **Marker absent, or present while the owner lane's handoff doc has no "Overnight run" item** (a marker
  left by a crash): this is the **start**. Only the owner lane runs it (set-up in `stages/role-owner-lane.md`;
  it deletes a stale marker first). Any other lane forwards the owner's go as `stages/role-lane.md` says.
- **Marker present with the item**: this is a **re-invocation** after a restart, resume or compaction, or,
  in a lane other than the owner lane, the arrival of the start message itself. No set-up is run. The owner lane applies the "Re-invocation" section of `stages/role-owner-lane.md`; any other
  lane resumes its work.

## Step 2: read

Read `stages/common.md` (every lane). Then read `stages/role-owner-lane.md` if this lane's own handoff doc
is the config's owner doc, otherwise `stages/role-lane.md`. The role files add to common.md and never
repeat it.

## The hook

The frontmatter declares one Stop hook, `python3 ~/.claude/hooks/narration_guard.py`, 10-second timeout. It
exists only in a lane that has invoked this skill, for the rest of that session, and acts only while the
presence marker exists. With the marker gone the run is over and the hook does nothing.
