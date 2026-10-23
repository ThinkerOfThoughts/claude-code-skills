# Example principles sheet

> This is a real principles sheet from one project, scrubbed of names and project details and generalised.
> It is a starter to adapt, not a set of rules to adopt as-is: keep the layout, and replace the content
> with your own owner's rules, quotes and ids. Where a quote appears it is the owner's own wording with
> anything identifying cut out; "(paraphrase)" marks a summary where no clean quote remained.

status: APPROVED <date> [OWNER <ts> "all are good"]     <!-- v3 split several compound principles into a/b parts; v2 reworded eight lines at the owner's request -->

Source: a sift of several hundred of the owner's past messages from the project's chats, four cold analysts, one synthesis and one adversarial cold check (its quote-check file lives with the run records). Each line was narrowed where the check found it over-read. Cited by id from ledger lines. The ids I3, I7, I12, I13 and I14 refer to the example invariants doc.

## Principles
P1. One mechanism, one source of truth: when two paths, timers or lists do the same job, merge them; never add a parallel path.
P2. No invented constants where the value can be measured or derived; a fixed value is fine if it is named, lives in the developer tunables file and has a follow-up issue to make it dynamic; content bounds and values the owner sets are fine. (I3, I7)
P3. A known, fixable defect is fixed before the work ships; an exception is the owner's explicit call. (a standing rule the owner keeps outside the project)
P4. A small, rare edge case may be accepted only with a code comment and a commit-log note so it is easy to find later.
P5. Root cause over band-aid: rework a misfiring check rather than demote it; clamp bad data and also fix whatever wrote it.
P6. Don't add stored fields or per-tick writes for what can be recomputed; modifiers are weights applied when results surface, never baked into stored values; decay is computed when results surface and written back once, at the single scheduled consolidation step; data that is not part of the records stays out of the main records store unless it must stay in step with them.
P7. Reuse an existing mechanism, or use a simple one, rather than adding a new tunable or a hand-written list of cases. If two mechanisms do the same job, remove the duplicate. If a capability is unfinished, keep it and file an issue. Cheap extras already in hand get included ("might as well"), within I14.
P8a. Before the system removes or replaces stored data (a migration, a rebuild), it checks the new copy is complete and correct; if the check fails, the old data stays.
P8b. When a health check in the system finds something wrong (for example a database integrity check), the finding is written to a log file that survives restarts, not only printed.
P8c. Work the system has queued but not yet done (for example a queue of pending items) is saved to disk, so a crash or restart does not lose it.
P9a. Things an AI model produces (a new name, a new label) are accepted as given and tidied later by the existing clean-up paths, not filtered out on the way in; hard limits only where there is a real reason (for example a maximum name length).
P9b. When the system refuses or fails something, the message says exactly what went wrong: a startup error names the bad setting and its line; a refused tool call tells the model why.
P10. Worst-case hardware is the baseline: detect and adapt upward; never freeze the user's machine; stability beats parallel speed.
P11. Never force technical work on the user: the average user must not need to touch settings, installs or code to use a feature, while a user who wants to tinker can. Everything works on macOS, Windows and Linux. (I12, I13)
P12a. When a step has a time or memory budget, do as much of it as fits (score the candidates that fit, search the terms that fit) instead of skipping it; below a minimum, use the cheaper method instead.
P12b. Every cap or limit needs a stated or identifiable reason, and caps without one are removed; a value outside its valid range (a score outside 0-10) is held to the range, not rejected.
P13. Decide a mechanism by what the feature is for and how the real thing behaves.
P14a. Repeated exposure to the same thing has less effect each time (habituation, like warning lights people stop noticing): for example an item shown again the same day shifts the system's state half as much as the time before.
P14b. Anything that picks from the records (retrieval, re-reading scans, background re-checks) must not keep picking the same few just because they were picked before (no rich-get-richer loops).
P15. No live LLM in the loop unless the LLM's own behaviour is what is being tested (for example whether the model actually opens the snippets it is offered); a purely mechanical system is tested mechanically: synthetic data, the real local models, enough runs for an error range.
P16. Scope: a defect in code the change touches is fixed in the change (P3); small related fixes fold in; improvements, and defects in code the change does not touch, get their own issue or PR.
P17. KISS: choose the mechanism that does the most work for the least machinery; extra machinery needs a stated reason (a feature's purpose, T5).  [OWNER <ts> "add a design principle to the list: KISS" + "it should choose the mechanism that does the most work for the least machinery" + "didn't mean for you to remove the bit about extra machinery needing a stated reason; that can stay on."]

## Tie-break order (higher wins when principles conflict)
T1. User-facing harm (machine freeze, install burden, data loss) beats engineering effort and parallel speed.
T2. Fixing a known fixable defect beats schedule and cost (unless the owner calls an exception).
T3. Root cause beats patch.
T4. Measured or derived beats an invented constant.
T5. A feature's purpose beats simplicity, unless the extra machinery outgrows the feature (I14); reaching I14 means stopping and telling the owner.

## Defaults for recurring kinds of decision
Status: APPROVED <date> [OWNER <ts> "Rest are good." for D1 and D5; OWNER <ts> "D2: good. D3: good. D4: also good." for D2 to D4]
D1. Now or later: anything not needed for the response about to be given runs at a quiet moment, never while the system is responding.
D2. Keep or change behaviour: work meant to change a behaviour changes it as specified; work that goes in alongside existing behaviour leaves it as it is unless it is a defect (P3, P16); a bigger rethink gets its own issue. Behaviour that works but does not match the apparent design intent is noted and raised at the end of the run, or straight away if the gap is significant (it noticeably changes what the user or the model experiences).
D3. Result ordering: when results from several sources are combined, they are arranged in groups in one editable order, with no slots reserved for any source.
D4. Where a setting lives: a user-facing setting only where users genuinely differ (the idle wait before background work, which tracks typing speed; which model runs the assistant; the retrieval time budget); everything else in the developer tunables file (decay half-lives, blend weights, the re-scoring safety margin, the background batch time budget, minimum-count floors); hardware differences are detected, not set.
D5. A mechanism's core formula always goes to the owner.

## Rulings
R1. Unreadable resource data (free RAM cannot be read: locked-down sandboxes, containers, restricted services): fall back to the simple, safe path (the cheaper method); no elaborate handling.  [OWNER <ts> "that would be a perfect example of an edge case not worth building an elaborate fix for, go with simple/safe fallback."]
R2. Deferral checklist (P3 vs P4): a defect may be deferred (with a code note and an issue) only if ALL hold: it cannot crash the system, freeze the machine, lose or corrupt data, or give the user or the model a wrong result it would act on; it happens only in conditions the vast majority of users will not hit (frequency guide: about 1 in 100 = fix now; about 1 in 1,000 = depends on severity; about 1 in 10,000 = defer); fixing it costs more than the rest of the change or needs an undecided design call. Whether something is an edge case at all is put to the trio of cold agents.  [OWNER <ts> "Checklist is a good idea; but i'd change 'most users' to 'vast majority of users', 1:100 is too frequent, 10:1000 is iffy depending on how severe it is, 1:10000 is deal with it later. Rest of its fine."]
R3. T5 confirmed.  [OWNER <ts> "Agreed, if it reaches a point where I14 comes in, that'd be a point to let me know whats up"]

## Always goes to the owner
- A line of the invariants doc, and any change to an invariant.
- Wording of any text that is injected into a model's own context (prompts, framing text).
- A new dependency, model or service.
- The core formulas of a mechanism.
- Anything nobody asked for.
- Scope freezes.
- Posts to the public tracker.
- Band-aids that were held for review, and any ship decision after a process failure.
- Real user data.
- A three-way split in the cold-agent vote.

## Changes
<!-- <date> <id> added/reworded, with the owner quote -->
<date> P17 added: see its quote above.
<date> R2 reworded: "most users" became "vast majority of users" and the frequency guide was added, per the owner's quote on R2.
