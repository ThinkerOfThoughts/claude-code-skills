# Architect attempt 2 — resume point

**Read this first.** Written 2026-07-25 before a context compaction. It is the single place a fresh session
picks up. Everything below is settled unless marked OPEN; nothing needs re-asking.

**One-line status:** the design is complete and owner-ratified; **nothing has been built yet**; the next
action is a **guarded-change run, in a subagent, on ONE element** (start with the charter).

---

## 1. The build plan — the owner's instruction, verbatim

> "start with each element individually (charter, spine, whatever), once the thing as pieces exists, run the
> whole thing" — transcript record **1274**

So: **one guarded-change run per element**, each with its own spec → criteria → plan → cold red-team → build
→ cold red-team → harness. Only once all the pieces exist does a whole-skill run happen. This is a
deliberate correction of attempt 1, which tried to author the entire skill in one run and drowned in its own
criteria set — the *measurement apparatus* became the thing that kept failing.

Elements, in dependency order: **charter** → **the 7-section spine** (`templates/seed/`) → **Layer-2 config
contract** → **router (`SKILL.md`)** → **methodology/reference doc** → then the whole-skill run.

## 1b. THE DONE CRITERIA — owner-set, record **1572** (2026-07-28)

> "The done criteria for Architect is that it can create a detailed plan to implement Data_Distiller. If it
> can do that, we call it created. If it runs on that and gets stuck, or produces garbage, then we fix the
> first link in the chain that broke and try again, repeat until nothing breaks and the results are good
> (they don't need to match what was used to make Data_Distiller, the goal is for equivalence or better,
> not sameness)."

**This is the acceptance test for the whole skill, and it replaces "prove each element behaviourally" as
the bar that decides whether Architect exists.** Read three consequences off it:

1. **The test is end-to-end and real**: run Architect on "plan the implementation of Data-Distiller" and
   judge the plan it produces. Data-Distiller already exists, so its actual plan is available as a
   reference — but the bar is **equivalence or better, explicitly not sameness**. A plan that reaches the
   same quality by a different route passes. Do not build a diff-against-the-original oracle; that would
   test sameness, which the owner ruled out.
2. **The repair rule is first-link-that-broke**, not full-restart and not fix-everything: run it, find the
   earliest point in the chain that failed, fix that, run again. Repeat until it completes and the output
   is good.
3. **Per-element harnesses are therefore instruments, not gates.** They exist to catch gross defects early
   and cheaply. They do **not** have to be statistically powerful, and an element does not need its own
   behavioural proof to proceed — the end-to-end run is what proves it. This directly answers the failure
   that produced this ruling: the charter element burned 34 cold agents and two gate-4 bounces on
   behavioural arms whose own reviewers concluded had *"no path to done, only a path to a halt."*
   **When a per-element harness bounces twice, cut the harness — do not strengthen it.** See the standing
   TODO in `~/.claude/CLAUDE.md` ("the measurement-apparatus problem"), which this project is the third
   recorded instance of.

## 2. Process rules — non-negotiable, these were violated and it cost real work

- **The guarded-change loop runs in a SUBAGENT. The main session orchestrates only** — shepherds the
  cold-review gates, verifies output, commits. (Owner's standing global rule.)
- **Do not hand-author skill files in the main session.** The current `stages/charter.md` was written
  freehand inline and is therefore an **unvetted input**, not a product. That was a process violation.
- **Never claim a thing exists or behaves a certain way before it has been built and run.** Attempt 1's cap
  tripped on a criteria document written in the present tense about four scripts that did not exist.
  Build → run → paste the real output → *then* describe it, in the past tense.
- **Generate, don't type.** Hand-retyped site lists disagreed with the measurement file one directory away.
- **Any instrument that gates other instruments needs its own mutation test.** This project made that error
  three times; twice the "checker" was a printer that exited 0 on every input.
- **Wait for cold-reviewer records to exist on disk (path check) before returning.** Four runners returned
  with reviewers still in flight and their work was lost.
- **Never install an unfinished skill.** Attempt 1 was synced to `~/.claude/skills/architect/` after it
  passed conformance and left there after the dogfood found a blocker. It has been removed. Install only
  when attempt 2 is finished.
- **Stop-for-human is for the OWNER, not the orchestrator.** A delegated runner halts and relays verbatim;
  the orchestrator relays to the owner and never answers as him.

## 3. Where everything is

| What | Where |
|---|---|
| **The design spec (AUTHORITATIVE)** | `~/Documents/Architect.md` — owner-authored pseudocode, single copy, deliberately not duplicated into the repo |
| The working tree | `Architect/` on branch `claude/recursing-visvesvaraya-b40a0c` |
| Attempt 1, archived whole | `Architect-Attempt-1/` — deleted only once attempt 2 works (owner's instruction) |
| Attempt 1's loop history | `~/architect-hardening-loop/LOOP-STATE.md` (rulings R1–R10, three failed hardening passes) |
| Attempt 1's dogfood findings | `~/architect-dogfood-2026-07-24/FINDINGS.md` |
| Draft PR | `https://github.com/ThinkerOfThoughts/claude-code-skills/pull/1` (body describes attempt 1; needs updating for attempt 2) |
| Nothing is installed | `~/.claude/skills/` holds only the three finished siblings |

Key commits: `3771038` attempt-1 build · `8efdca1` hardening paused · `8ca7197` archive + demolition ·
`0bd28ff` design spec complete · `45fc619` uninstall + de-duplicate spec · `a4138d2` charter rewrite ·
`67d8c3f` charter marked draft.

## 4. Current contents of `Architect/` — and what is vetted

**NOTHING in here has been through the loop. Treat all of it as input.**

| File | Status |
|---|---|
| `stages/charter.md` | **UNVETTED DRAFT** (banner in file). Rewritten for the one-pass loop. The first build element. |
| `templates/seed/*.md` | Attempt-1 artifacts, carried over. The 7-section spine. Not yet revised for attempt 2. |
| `examples/authoring-a-skill/` | Attempt-1 artifact. Shape of a Layer-2 config. |
| `README.md` | Orientation for the rebuild. |
| `ATTEMPT-2-STATE.md` | This file. |

Deleted in the demolition: `SKILL.md`, `METHODOLOGY.md`, all eight `stages/stage-*.md`, `changes/`,
`guarded-change.architect.md` — all preserved in `Architect-Attempt-1/`.

## 5. The design — settled, do not re-litigate

The spec is `~/Documents/Architect.md`. A single recursive function `Node(task, plan, granularity, depth,
node_id)`. What the pseudocode alone does not make obvious:

- **`return plan` IS the join.** A parent waits on children and merges their returned values. There is no
  subtree-complete fact on disk. **This is the whole reason attempt 1 failed** — it implemented a recursive
  function as a filesystem protocol, and nearly every blocker was a bug in that protocol (a predicate whose
  operand had no producer, or a producer scheduled after its reader).
- **Slot inheritance** — a child runs inside its parent's queue slot, so siblings serialize and only leaf
  triples run concurrently. This deletes the entire shared-mutable-state class.
- **`Consensus` for plans, `Union` for issues.** Majority-vote is right for plans (one coherent plan out) and
  **wrong for findings** — the spec's own reason: "DISCARDS NOTHING… A finding one reviewer caught is
  signal" (`~/Documents/Architect.md` L20).
  > **CORRECTION 2026-07-28.** This bullet used to read "~85% of attempt 1's findings were caught by exactly
  > one reviewer." **That statistic has no source.** It appears in no file this project did not author about
  > itself — not in `~/architect-dogfood-2026-07-24/FINDINGS.md`, not in `~/architect-hardening-loop/`. The
  > orchestrator propagated it from a summary into this file, `README.md`, `guarded-change.architect.md` and
  > the charter draft, and then handed it to cold reviewers as measurement; the charter run's reviewer A
  > caught it. This is §8 failure mode 1 (self-certification) committed by the orchestrator. `FINDINGS.md`
  > records **per-finding convergence counts** ("3/3", "2 angles", "adversarial"), not a rate — derive from
  > those and show the derivation, or make the argument without a number.
- **Granularity floor**, threaded to three places: `Divisible` (tree depth), `Spawn_leaf` (step fineness),
  and — load-bearing — `Spawn_redteam` (what counts as "vague"). Without the third the red-team *manufactures*
  runaway subdivision: "you didn't say how to grip the handle" becomes an issue, the issue becomes the next
  task, forever. Owner's example: Manual Samuel.
- **Human gate**: `Human_gate` blocks the owner at every `depth <= gate_depth`, **default 2**, **before**
  children spawn. A bad cut corrupts everything beneath it, so approving after the fact is worthless.
- **Crash recovery = memoize, don't coordinate.** `Memo_read` before claiming a slot; two checkpoints per
  iteration (after `Consensus`, at the loop foot). On restart you re-walk **down** from the root: finished
  subtrees answer from disk, the walk falls through, you resume the node that died. A parent is never
  "recovered" — it is a stack frame re-created by replay, so live-agent state is never persisted.
- **One red-team pass** of 3 cold agents per iteration; the three-tier completeness definition lives **in the
  charter** as a distinct **lens** (not folded into a general mandate — that is how tier iii dies quietly):
  (i) universal spine, (ii) Layer-2 required sections, (iii) generative sweep for what neither list names.
- **Every finding carries a severity**, because `Severity()` filters on it. blocker|major become the next
  task; minor|nitpick are recorded, not looped on.
- **No backstop cap.** Owner ruled: trust the blocker|major filter; fix later if it proves an issue. A known
  accepted risk — attempt 1's cap tripped twice.

## 6. Owner rulings, with transcript loci (spot-checkable)

The **session transcript JSONL** is harness-authored and is the admissible source for owner words; an
agent-written file (including this one) is **not**. Loci are record indices in
`~/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`.

| # | Ruling | Locus |
|---|---|---|
| Granularity | there must be a max-granularity option (Manual Samuel) | **1128** |
| Human gate | depth-scoped; "at least to the second level" as a safe default | **1148** |
| Crash recovery | agreed: memoize-and-replay | **1188** |
| Uninstall | an unfinished skill should not be installed; drop the duplicate spec copy | **1209** |
| No backstop | trust the blocker/major filter, fix later if it is an issue | **1258** |
| Build scope | element by element, then the whole thing | **1274** |
| Charter | must include the three-tier completeness definition | ~**1175** |

Attempt-1 rulings R1–R10 (records 694/699, 789, 805, 867, 925) are in
`~/architect-hardening-loop/LOOP-STATE.md`. **Most are now moot** — they governed a hardening loop on an
artifact that has since been demolished. The ones that still matter are carried into §5 above.
**Caveat on R4:** at record **784** the owner was offered four options and **selected none**, answering in
free text; and the orchestrator later **inflated** his "means nothing" into cap-bounce immunity, which he
never said. Do not inherit that inflation.

## 7. OPEN

- **Draft PR body** still describes attempt 1 end-to-end. Needs rewriting for attempt 2.
- **`templates/seed/*` and `examples/` are attempt-1 artifacts** carried over unexamined. They are build
  elements in their own right, not settled inputs.
- **A dormant background task** (`task_c8abf7df`) was spawned for a stale Dragonfly README claim
  ("four-lens / reused not forked" vs the forked five-lens reality). Never confirmed done; the stale phrasing
  was still present at last check. Unrelated to Architect.

## 8. Failure modes this project actually produced — the red-team should hunt these

1. **Self-certification** — a document asserting, in the present tense, the behaviour of scripts that did not
   exist. Caught only by a reviewer who *ran* them instead of reading the claims.
2. **Unearned clean verdicts** — a "checker" that exited 0 on every input, twice; and an orchestrator
   spot-check that ran a tool with no arguments and read the resulting usage-error as a pass.
3. **Scope drift** — "narrow and mechanical: four scripts, two deletions" became a 13-item list and ~12 new
   criteria, and three of nine blockers lived in rows the expansion created.
4. **Fork without join** — four separate runners returned while their subagents were still in flight.
5. **Under-generalized fixes** — a defect class fixed only where reviewers happened to look, then re-found
   elsewhere and mistaken for a fresh finding.
6. **A gate satisfiable by the party it constrains** — an approval file the runner could write itself, and a
   directory-existence check pre-satisfied by run setup.
