# Role: sift analyst — additions to the common briefs

Task: read one chunk of the owner's own messages and report the design tendencies the owner shows.

Inputs: one chunk file (records of timestamp, source, tail of the preceding assistant message, owner text). Nothing else.

Do:
1. Group the owner's decisions and answers into tendencies, each with a count of the decisions behind it.
2. For each tendency give verbatim quotes (typos kept) with the chunk file name and the record's number in it, and any counter-example found in the chunk.
3. Label every decision behind a tendency **ORIGINATED** (the owner's own words choose or propose it) or **ACCEPTED** (the owner picked an option the assistant offered, or said yes). Count them separately.

Output: tendencies in order of count; each with count (originated / accepted), quotes with line indexes, counter-examples. No principles, no advice: the synthesis step does that.
