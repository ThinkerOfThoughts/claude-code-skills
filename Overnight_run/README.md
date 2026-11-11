# Overnight Run: keeping a multi-lane unattended run honest

A Claude Code skill for the stretch where the owner starts several lanes (separate sessions) on work and
goes away. Nobody reads the chat overnight, so the run keeps chat empty, keeps one record, and wakes itself
when usage resets. Sibling of [Plan_ledger](../Plan_ledger/) and [Guarded_change](../Guarded_change/),
laid out the same way: a router `SKILL.md`, rules in `stages/`, a per-project config.

## What it prevents

Narration into an unread chat; a question that points at an earlier message; an owner instruction typed in
one lane that never reaches the others; a handoff doc that is not current; a usage reset nobody wakes for;
a failed login found only at the first call; the owner's guard switched off without his say.

## Files

| File | Holds |
|---|---|
| `SKILL.md` | router: config lookup, start vs re-invocation, which files to read, the frontmatter Stop hook |
| `stages/common.md` | rules C1 to C8, every lane |
| `stages/role-owner-lane.md` | set-up, run record, egg timer handling, run end: owner lane only |
| `stages/role-lane.md` | rules R1 to R4, any other lane |
| `overnight-run.companion.md` | per-project config: project dir, owner handoff doc, watchdog path, default lanes, guard line |

It relies on three things built elsewhere: `usage_watchdog.sh --eggtimer` (the Scripts repo), the Stop hook
`narration_guard.py` and the SessionStart hook `compact_reinject.py` (the skills repo's `hooks/` folder, `~/Desktop/claude-code-skills/hooks/`, installed to
`~/.claude/hooks/`).

## Install

```bash
mkdir -p ~/.claude/skills/overnight-run
cp -r SKILL.md stages overnight-run.companion.md ~/.claude/skills/overnight-run/
diff -r SKILL.md ~/.claude/skills/overnight-run/SKILL.md
diff -r stages ~/.claude/skills/overnight-run/stages
diff overnight-run.companion.md ~/.claude/skills/overnight-run/overnight-run.companion.md   # all empty
```

## How a run goes

The owner gives the go and the per-run list to the owner lane (a go given in another lane is forwarded to
it). The owner lane sets up (list, login ping, guard question, egg timer), writes the run item, creates the
marker, and sends the start message. The egg timer fires every tick: after a usage reset it wakes the lanes
that were waiting; otherwise it pokes the working lanes. A restarted or compacted lane is pointed back into
the skill by the re-inject hook while the marker exists. The run ends when the owner says so (any lane asks
him once in the morning), or when every lane is parked or done.

## Requirement-line map (L2 lines to where the files carry them)

| L2 line | Where |
|---|---|
| L2-1 run scope, marker, start vs re-invocation | SKILL.md Step 1; role-owner-lane.md Set-up 1, 6 to 8 |
| L2-2 run record, single writer | role-owner-lane.md "The run record"; role-lane.md R1, R2 |
| L2-3 narration guard | SKILL.md "The hook"; common.md C1, C2 |
| L2-4 gates stay on | common.md C7 |
| L2-5 relay owner messages | common.md C3 |
| L2-6 handoff upkeep, re-point | common.md C4; role-owner-lane.md Re-invocation; role-lane.md re-invocation paragraph |
| L2-7 usage near cap | common.md C5; role-owner-lane.md Set-up 2 |
| L2-8 egg timer | role-owner-lane.md Set-up 5, "When the egg timer exits", Re-invocation |
| L2-9 set-up failure | role-owner-lane.md Set-up (heading, step 3) |
| L2-10 guard stays the owner's | role-owner-lane.md Set-up 4; config `guard` |
| L2-11 beeps, blocked items | common.md C6 |
| L2-12 run end | common.md C8; role-owner-lane.md "Run end"; role-lane.md R4 |
| L2-13 accepted edges | "Known limits" below |
| L2-14 defaults, a go elsewhere | common.md C7; role-lane.md R3; role-owner-lane.md "A go given in another lane" |

## Known limits

Accepted edges, each recorded as a comment where it lives and in the commit log:

1. A night with the machine down wakes nothing until the owner resumes a lane.
2. A lane is not proven to have invoked the skill beyond its reply to the start message.
3. An owner instruction typed in one lane is relayed by written rule only (C3); no hook enforces it.
4. A scheduled-task turn may count as owner-typed under the narration guard's test, if it does.
5. A wake is lost if the owner lane itself is dead.
6. A run that dies without ending leaves the presence marker, so the narration hook stays on in sessions
   that invoked the skill until the next run's start deletes it, or the owner does.
7. A fresh session started after a restart is guarded only once it invokes the skill again.
8. While the marker exists, any unrelated session that starts or resumes is told to invoke the skill.
9. Each narration block costs one model call.
10. No hook reads usage or context use; the usage figure comes from the owner.

Not verified by the build: live firing of the frontmatter hook needs a real session.
