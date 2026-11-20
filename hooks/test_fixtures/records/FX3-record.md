# fixture record FX3

ANSWER T3 BEGIN
T3 (where the session cache lives): in the existing session store module, not in a new module.
Reuse: the store's own read path, whole.
Constraint: one cache file per Bob session, no state shared between sessions.
Constraint: nothing is written outside the session folder.
Builder note: settle whether an empty cache file counts as a missing one.
Builder note: settle the order of two writes within one turn.
ANSWER T3 END

ANSWER T4 BEGIN
T4 (what the export file is called): the export keeps the existing name and adds a date suffix.
Reuse: the existing name builder, whole.
Constraint: the suffix uses the local date of Bob's machine.
Constraint: an export never overwrites an earlier one.
Builder note: settle what happens when two exports start in the same second.
ANSWER T4 END
