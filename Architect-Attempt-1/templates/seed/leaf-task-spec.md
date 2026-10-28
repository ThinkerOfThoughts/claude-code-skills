# Leaf task-spec — <node name>

*Seed skeleton for a LEAF (GRN): the spine collapsed to an atomic, agent-executable task spec — the same
seven concerns, compressed to what ONE agent needs to execute with no further planning. Nothing is
dropped; it is compressed.*

## Task (problem + approach — §1–2 collapsed)
The single unit of work, stated so one agent can execute it without further decomposition.

## Inputs & interfaces (§3)
What the executing agent is handed; the seams to its parent/siblings it must honour.

## Outputs & their locations (§4)
Exactly what the agent produces **and where it writes it**. *Never omitted.*

## Failure modes & fallback (§5)
The one or two ways this task fails and what to do.

## Restart note (§6)
Whether the task is resumable, and its done-iff-output-exists marker.

## Done / verification (§7)
The checkable condition that says this leaf is complete and correct.
