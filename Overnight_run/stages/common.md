# Common rules: every lane in the run follows these

Each rule is stated once here; the role files add to it and never repeat it. The strings S2 to S6 are the
fixed messages the run sends; S6 sits inside C8.

- C1 (failure 1, L2-3): "Overnight, nobody reads the chat. A turn the owner did not start or type into writes no text at all, between tool calls or at the end. Owner items go on the morning list."
- C2 (failure 2, L2-3): "A question carries its own data: the facts, numbers or text it depends on are in the question itself, never a pointer to an earlier message."
- C3 (failures 5 and 12, L2-5): "When an owner message concerns another lane in the run, relay it at once with GATE: OWNER-RULING, through the existing relay that wakes an idle lane and needs its ack." (format: plan-ledger `stages/cascade-build.md` "Gate record format"; a short ruling such as "yes" carries its `re:` line)
- C4 (failure 10, L2-6): "Bring the handoff doc current at each milestone and before any long wait."
- C5 (failure 6, L2-7): "Near the usage cap, take the cheapest path and leave heavy jobs until after the reset. The owner gives the usage figure; no hook reads usage. A design question that piles up rules stops at the cascade's pile-up rule."
- C6 (L2-11): "A blocked item is paused and its question goes on the morning list; carry on with whatever is not blocked. No beep overnight; the run adds no beep of its own, and hooks that already beep are unchanged."
- C7 (L1-5, L2-4, L2-14): "Work follows the existing skills with their gates on: questions through the plan-ledger cascade, code through guarded-change with one runner per step and a draft PR opened first, the owner's limits on builders and test suites. Nothing is relaxed overnight; PR text waits for the owner unless his per-run list says otherwise."
- C8 (L2-12): "If the owner's first typed message of the morning comes while the run is on and you have not received the run-over message, answer his message first, then ask once: 'The overnight run is still on. End it now?' (S6)." ("Of the morning" means after the run's reset time, which every lane has from S2.)
