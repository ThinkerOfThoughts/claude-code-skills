// SNAPSHOT of the owner's design spec, taken 2026-07-25 from ~/Documents/Architect.md
// The owner's copy is AUTHORITATIVE and is where edits happen; this is the in-repo copy so attempt 2's
// authoring has a spec that travels with the code. Re-snapshot when the owner's copy changes.

// granularity: the ATOMIC-STEP FLOOR for the run, e.g. "a step a competent practitioner can execute
// without further planning". Set once per run (Layer-2), threaded down so a branch can override it if
// a sub-tree genuinely warrants finer detail. It bounds THREE things, and all three are needed:
//   (1) Divisible  — how deep the tree goes
//   (2) Spawn_leaf — how fine the steps a leaf writes are
//   (3) Spawn_redteam — what counts as "vague"  <-- without this one the red-team MANUFACTURES the problem:
//       "you didn't say how to grip the handle" becomes an issue, the issue becomes the next task, and the
//       loop subdivides toward Manual Samuel while every individual agent behaves correctly.

leaf_agent Spawn_leaf(string task, string plan, string granularity);	// spawns a leaf agent with task = to what it needs to do, and plan = to what it needs to fill out, written at no finer detail than granularity. Leaf agents inheret their parents work_queue slot and operate in paralell within that slot.

node_agent Spawn_node(string task, string plan, string granularity, int depth, string node_id);	// spawns a node agent with task = to what it needs to do, and plan = to what it needs to fill out. node_agents inheret their parents work_queue slot and reserve their place within that slot.

pair<string> Divisible(string _task, string _granularity);	// cold agent, checks if a task can be subdivided into two or more sub-tasks WITHOUT either sub-task falling below _granularity, if yes, red-teams result (looping until no major issues are found) then returns the two top-most sub-tasks, if no, returns null;

bool Human_gate(pair<string> _division, string _task, int _depth);	// BLOCKS for the human owner: presents the proposed split and the seam between the halves, waits for a verbatim approve/reject. Fires at every _depth <= gate_depth (run constant, DEFAULT 2 — deeper/finer plans warrant more levels of gate). Gated BEFORE children spawn: a bad cut corrupts everything beneath it, so approving after the fact is worthless. On reject the division is re-derived and re-presented.

string Consensus(vector<string> _plans);  // cold agent: 2-of-3 on numbered steps INCLUDING order; odd plan discarded. For PLANS only — you need one coherent plan out.

string Union(vector<string> _issues);	//cold agent: merges issues, DISCARDS NOTHING; dedups only exact restatements. A finding one reviewer caught is signal.

string Severity(string _issues);	// returns only the blocker|major issues; minors are recorded against the plan but NOT looped on. This is what makes the while() terminate — three real rounds showed cold reviewers always find something.

redteam_agent Spawn_redteam(string _task, string _plan, string _granularity);	// spawns an adversarial cold agent to review the provided _plan, checking it against the provided _task. If an element of the plan is vaigue AT OR ABOVE _granularity (a step already at the floor is NOT vague, it is done), misses a portion of _task, leaves out a contingency, etc. that gets added to string issues_found (which starts empty) as well as load-bearing things NEITHER task NOR plan mentions, once all elements of _plan and _task have been reviewed, returns issues_found. Every issue carries a severity, because Severity() filters on it.

// CRASH RECOVERY = MEMOIZE, DON'T COORDINATE.
// One writer per node_id (the node itself), written AFTER the value exists, read ONLY by a restart of that
// same node. Nothing else ever reads it — the join stays wait() + return value. On restart you re-walk DOWN
// from the root: finished subtrees answer from disk instantly, the walk falls through them, and you arrive
// at the node that died and resume it there. A parent is never "recovered"; it is an ordinary stack frame
// re-created by the replay, so live-agent state is never persisted and nothing needs reattaching.
memo Memo_read(string _node_id);	// {done, iter, task, plan, division}, or empty if this node never ran.
void Memo_write(string _node_id, bool _done, int _iter, string _task, string _plan, pair<string> _division);

string Node(string _task, string _plan, string _granularity, int _depth, string _node_id)
{
	memo saved = Memo_read(_node_id);	// read BEFORE claiming a slot — a finished subtree should cost nothing
	if(saved.done)	return saved.plan;	// completed: answer from disk, spawn nothing, claim no slot
	
	wait(work_queue);	// wait until this nodes place in the global work queue  arrives, preventing too many nodes from operating at the same 
	time and potentially depleting compute resources.
	
	string task = _task;
	string plan = _plan;
	string granularity = _granularity;
	int depth = _depth;	// root = 0; every Spawn_node passes depth + 1
	string node_id = _node_id;	// position in the tree; stable across restarts. root = "0"
	int iter = 0;
	
	pair<string> division;
	
	if(saved.empty() == false)	// died mid-loop: pick up exactly where it stopped
	{
		iter = saved.iter;  task = saved.task;  plan = saved.plan;  division = saved.division;
	}
	else
	{
		division = Divisible(task, granularity);
	}
	
	
	while(task.empty() ==  false)
	{
		if(division.empty())
		{
			vector<leaf_agent> leaves;
			
			for(int i = 0; i < 3; i++)
			{
				leaves.add(Spawn_leaf(task, plan, granularity));
			}
			
			wait(leaves.working());	// wait for all working agents to either return, or get stuck
			
			plan = Consensus(leaves.get_plans)
		}
		else
		{
			if(depth <= gate_depth)	// gate_depth: run constant, default 2
			{
				while(Human_gate(division, task, depth) == false)
				{
					division = Divisible(task, granularity);	// rejected -> re-derive, re-present
				}
			}
			
			vector<node_agent> child;
			child.add(Spawn_node(division.first(), plan, granularity, depth + 1, node_id + ".1"));
			child.add(Spawn_node(division.second(), plan, granularity, depth + 1, node_id + ".2"))
			
			wait(child.working());	// wait for all working agents to either return, or get stuck
			
			plan = Consensus(child.get_plans);
		}
		
		Memo_write(node_id, false, iter, task, plan, division);	// checkpoint 1: the merged plan survives a crash in the red-team round
		
		vector<redteam_agent> redteam;

		for(int i = 0; i < 3; i++)
		{
			redteam.add(Spawn_redteam(task, plan, granularity))
		}
		wait(redteam.working());	// wait for all working agents to either return, or get stuck
		
		task = Severity(Union(redteam.get_issues));
		division = Divisible(task, granularity);
		
		iter = iter + 1;
		Memo_write(node_id, false, iter, task, plan, division);	// checkpoint 2: end of iteration
	}
	
	Memo_write(node_id, true, iter, "", plan, null);	// done — every later restart returns this immediately
	return plan;
}
