# Split review — round 3, reviewer C

**What I reviewed:** the proposed division in
`Architect/runs/data-distiller/0/split-round-3.md` — its two sub-tasks and the S1–S9 seam.
**Against:** the task text and granularity floor as restated in that file, and the two sibling
skills `/home/zero/Desktop/claude-code-skills/Guarded_change/` and
`/home/zero/Desktop/claude-code-skills/Dragonfly/` (including their `stages/`), plus
`Architect/stages/node.md`, `leaf.md`, `combiner.md` for the execution model.

**Not read, by instruction:** `/home/zero/Desktop/claude-code-skills/Data-Distiller/` (not read,
not listed, not grepped); `split-review-*.md` siblings; `split-round-2.md`. **Consequence:** the
round-2 findings/disposition table at lines 450–479 is treated as the divider's claim throughout.
Where a disposition asserts a round-2 blocker was closed, I checked the *round-3 text* against the
claim, not the round-2 source — see F1, which fails that check.

---

## Verdict on the division

**The joint is real and I would keep it. The seam is not yet sound.** One blocker and one major
stand. Both are gaps *created by* the seam — an undivided planner writing `node.md` and
`merge.md` together would not have either — so they are properly findings against the cut and not
against the eventual plan.

---

## Findings

### F1 — blocker — the two workers that actually read the corpus are never handed the corpus root, and S2 states the opposite

**Where:** split-round-3.md:167–177 (S2, restated 317–327); sub-task two file 3 at 258–261 and
file 4 at 262–264; the common.md rule at 247–253 and S5 at 353–357.

S2's preamble states the guarantee the whole structural move rests on:

> "No worker file names a path of its own, and **no worker reads any config file** — every
> corpus-specific value it needs arrives here." (line 169)

Its own rows falsify that for `analyst` and `verify`:

- `decompose` ← **the corpus root**, item definition, off-limits, context budget, strategy names,
  output path.
- `analyst` ← "its item's **locator** (as written in the manifest)", index *k*, off-limits, output
  path. **No corpus root.**
- `verify` ← the N analyst output paths, "the item's **locator**", off-limits, output path. **No
  corpus root.**

`analyst` is defined at 258–259 as "Read-only over the corpus", and `verify` at 262 must "re-open
**every** citation" — i.e. open the corpus. Their only handle on the corpus is the locator, whose
*form* is explicitly worker-plane business: S3 fixes only that an entry begins with an item id on
its own line "followed by that item's locator. **Everything else in an entry is the worker plane's
business**" (line 181).

**Failure scenario.** The worker half, planning `decompose.md`, specifies locators relative to the
corpus root it was handed — `logs/2026-01/session-4.md#L1-820`, the natural choice for a
corpus-agnostic manifest. The driver half, complying with "the driver hands every worker
**exactly** the arguments below", hands the analyst that string and nothing else. The analyst has
no corpus root and cannot resolve it. Neither half violated a seam clause. Whether the skill works
turns entirely on an unstated constraint — that locators must be self-resolving — which the seam
never imposes and which the worker half has no reason to derive, because S2 has promised it that
every value a worker needs is in the payload.

**Aggravating:** the common.md rule at 250 ("**open no file except the paths handed at spawn**",
restated in S5 at 356) is written in terms of *paths*. A locator is handed but is not, in the
seam's own vocabulary, a path — the seam distinguishes them in the analyst row itself. Under a
strict reading the analyst may open only its output path.

**Against the disposition table.** Row 456 records the round-2 blocker "I8 withheld
`corpus_root`/`oversize_strategies` from the only half that reads the corpus" as closed because
"every value arrives in the S2 payload, **including corpus root**". That is true of `decompose`
only. The two roles that read the corpus per-item still do not have it. The round-2 blocker is
half-closed and reads as fully closed.

**Remedy shape (one seam clause, not a re-cut):** either add the corpus root to the `analyst` and
`verify` rows, or fix in S3 that a locator must be resolvable without any other value. Either is a
single clause; both leave the joint intact.

---

### F2 — major — a unit that fails before `merge` leaves no trace in the deliverable, and neither half can put one there

**Where:** S3 Invariant A at 186–191; S2's `merge` row at 176–177; S4 at 197–201; S6 at 209–214.

The seam closes every route by which a failed unit could be recorded in the terminal artifact:

1. When a unit dies before `merge`, **the driver** writes its status record `failed` (S3, 190–191).
   So the failure is known only on the driver side.
2. The failed unit produces **no** verified/merged artifact, so nothing enters the roll-up chain
   that any ancestor `merge` will ever be handed.
3. `merge`'s payload is exhaustive — "the input paths to merge (an item's verified findings, or
   the merged outputs of a node's children); its output path; the path to write the unit's status
   record" — with the preamble "exactly the arguments below". The driver **cannot** hand the root
   merge a list of failed units, and a status-record path is neither of the two permitted input
   kinds.
4. S4 forbids any driver-plane agent from opening the `FINDINGS` artifact, so the driver cannot
   annotate it afterwards.
5. S6's coverage note is scoped to "which items were analyzed by `window` or `sample`" — the
   partial-*analysis* case, not the failed-*unit* case — and S6 says "Neither half may reassign
   this producer."

**Failure scenario.** A 40-item run; item 17's analysts all fail (an unreadable corpus file). The
driver writes item 17's status record as `failed` and proceeds. The root `merge` is dispatched with
the merged outputs of the nodes; item 17 contributed none. `FINDINGS.md` is produced, carries a
coverage note about `window`/`sample` items, says nothing about item 17, and is handed to the human
as the run's result. The one artifact the human keeps silently overstates its coverage — which is
the precise failure mode a skill whose purpose is *trustworthy* findings exists to prevent.

**Not closable by either half alone.** The worker half cannot know about a unit it was handed no
path for; the driver half may not write into the deliverable and may not extend the payload. This
is the same defect class as the round-2 major at row 467 ("the record of what was *not* analyzed
had no route to the deliverable"), which the divider fixed for `window`/`sample` and left open for
failures. The divider's own standard — put it *in the deliverable* — is what makes the weaker
treatment of failures inconsistent rather than merely unhandled.

**Remedy shape:** one clause. The cleanest is to give `partial`/`failed` a route: add a
coverage-input path to `merge`'s payload, or extend S6's coverage note to cover units with no
output and add the corresponding input. (See F3 — the same clause can define `partial`.)

---

### F3 — minor — `partial` is a fixed word with no fixed meaning, split across the cut

S3 Invariant A fixes three outcome words but gives a consequence for only one state: "a unit with
no status record is treated by resume as incomplete" (188–189). `partial` is *produced* under
worker-owned criteria ("Its other contents are the worker plane's business") and *consumed* by
driver-owned resume, with no agreed semantics.

**Failure scenario.** The worker half defines `partial` as "some analysts' findings were dropped
by verify". The driver half's resume treats "anything not `complete`" as work to redo. The unit is
deterministically `partial`, so it is re-dispatched every resume, forever — a termination failure
in the half whose stated accountability is "a run that terminates" (line 81). The driver half can
avoid this unilaterally by treating any status record as done, but nothing tells it to, and the
seam's asymmetric treatment of `failed` (driver-written, meaning "this unit died") invites the
opposite reading.

---

### F4 — minor — the driver must extract fields from two records whose layout the other half owns, and only one field has an anchor

S3 deliberately anchors the item id — "each entry beginning with a unique, filesystem-safe item id
**on its own line**" — which shows the divider understood the need. It then does not anchor:

- **where the locator ends.** "followed by that item's locator. Everything else in an entry is the
  worker plane's business." An entry may therefore be `id` / locator / arbitrary worker content,
  with no delimiter, and the driver must pass the locator "as written in the manifest" (S2) without
  knowing its extent.
- **where the outcome word sits** in the status record. Invariant A says it "states the unit's
  outcome as one of `complete`, `failed`, `partial`" and nothing more; resume depends on reading it.

Both readers are agents rather than parsers, so this degrades rather than breaks. It is minor
because the fix is two words each ("on the line immediately following"; "on its own line"), and it
is worth fixing because the divider already paid that cost for the id and stopped.

---

### F5 — minor — the coverage note must name items, but no worker is ever handed an item id

S6 requires the deliverable to state "**which items** were analyzed by `window` or `sample`". Item
ids exist only in the manifest and are used only by the driver: the `analyst` payload carries the
locator and *k*, not the id; the `merge` payload carries paths only. The only identifier that can
reach the deliverable is the locator, and only if the worker half mandates carrying it from
`analyst.md` through `verify.md` and both `merge` levels. The worker half owns that whole chain, so
this is closable unilaterally — but the seam asks for "items" using a token the worker plane does
not possess.

---

### F6 — minor — the driver half is made accountable for blindness that the worker half controls

Sub-task one is "accountable for … keeping its coordinators from ever seeing a finding" (line 81)
and owns S4. But what a coordinator *actually sees* is the status record, whose contents beyond the
outcome word are worker-owned and bounded only by "carries no finding text, no claim and no
citation". The task's wording is "a **terse** per-child status"; nothing in the seam fixes terseness
or size, and the half that owns it is not the half accountable for it.

**Failure scenario.** `merge.md` specifies a status record carrying `topics touched: retry-logic,
auth-expiry, rate-limits` — arguably not a claim, not a citation, not finding text — and the
coordinator's expectations about its remaining children are steered by it. Both halves complied.
Minor because the existing bound is substantive and the fix is a size/shape clause in S3.

---

### F7 — minor — the one order-dependent step in the task sits in the half `Union` concatenates first, and the seam says there is no ordering

The record section asserts: "There is no upward channel and **no ordering**; the halves can be
planned simultaneously" (line 401). That holds for every step except one. Sub-task one file 5 and
the note at 122–124 place the install — and its verification that "the live copy must equal the
source copy" — in the driver half, and the note confirms an install *action* is intended, not only
its documentation. Installing must follow the creation of all ten files, five of which are the
other half's.

`Architect/stages/combiner.md:66-67` fixes `Union` to "preserve each input's internal order, and
concatenate the inputs in the order you received them", and `leaf.md:14` fixes "Order is content".
The merged plan therefore reads: five driver files → install-and-verify → five worker files.
Executed in order it installs an incomplete skill.

Sub-task one *can* guard this alone — it is permitted to assume "the other's files exist at the S1
paths" (line 404) — but the seam's flat "no ordering" tells it not to. Minor, because the remedy is
one sentence in sub-task one or one clause in the seam.

Precedent for the install belonging in README: `Guarded_change/README.md:110` and
`Dragonfly/README.md:107`; for the live==source check: `Guarded_change/SKILL.md:81-82` and
`Dragonfly/SKILL.md:88`. The division's placement is correct; only its ordering claim is wrong.

---

### F8 — minor — the stated joint criterion is wrong for `node.md`, and the half that must write it is not pointed at the house precedent for a cold-agent prompt

The joint is stated as the reader's information state: "A driver-plane file is read by an agent that
**already holds the run's context**" (383–385), with the concession "it is why `stages/node.md` sits
on the driver side despite being a prompt."

That criterion does not hold for `node.md`. A child node is *spawned* — its world is `node.md` plus
its handed arguments, exactly the worker-plane definition. `Architect/stages/node.md:3` is the live
demonstration: "You hold `task`, `plan`, `granularity`, `depth`, `node_id`, and the run folder" —
a cold agent handed a payload. The criterion that actually separates the two sets is **whether the
agent dispatches others**, and the assignment of `node.md` to the driver side is right under *that*
criterion. The stated one is a post-hoc fit.

Downstream cost: sub-task two is pointed at `Guarded_change/stages/charter.md` and
`Dragonfly/stages/charter.md` as "the house precedent for a cold-agent prompt" (289–291); sub-task
one, which must author the most operationally dense cold-agent prompt in the skill, is pointed at no
such precedent. Minor rather than major because sub-task one's source list already includes both
`stages/` directories (139–141), so nothing is withheld — only unsignposted.

---

### F9 — minor — the driver's `METHODOLOGY.md` will document artifacts whose contents the worker half owns

Sub-task one file 2 gives the driver "*What a run produces* — the full on-disk artifact layout,
which this half owns outright" (101). In both siblings that section annotates each artifact's
*contents*, not just its name: `Guarded_change/METHODOLOGY.md:158-168` ("`1.5-criteria.md`
measurable acceptance bar"), `Dragonfly/METHODOLOGY.md:145-154` ("`hypotheses.md` ranked falsifiable
hypotheses: confirm/refute prediction, status, + gate marker"). Following that precedent, the driver
will describe the shape of findings/status artifacts that sub-task two owns exclusively (279), and
may contradict `merge.md`.

`combiner.md:59-61` keeps such a conflict and marks it rather than smoothing it, and the node's next
red-team round can catch it — so the system contains this. It is still an avoidable collision: one
clause ("the driver's layout section names artifacts and does not specify their contents") removes
it.

---

### F10 — minor — alternative (c)'s rejection was not re-weighed against round 3's own structural move

Alternative (c) is rejected at 437–442 on the ground that "the config keys are consumed across
almost every file of the large half, so the interface would run through every file rather than
along a boundary". Round 3's headline change is that **no worker reads any config file** (S2, 169),
which makes exactly one file — `stages/node.md` — a consumer of config values. The stated reason for
rejecting (c) is therefore no longer true under round 3's own move, and the rejection text appears
carried over unrevised from round 2.

I am not asserting (c) is better — under (c) the blind-roll-up barrier and the run loop would be
documented on one side and enforced on the other, which is a worse crossing than S1–S9. The finding
is that the alternative's rejection now rests on a premise the same document retired.

---

### F11 — nitpick — S4 hardcodes a filename the seam says it does not fix

S4 names "`FINDINGS.md`" (198) while S6 uses the placeholder "`<the run's FINDINGS file>`" (209), in
a seam whose preamble states that "the run directory layout, **every path** … are **not** fixed here"
(146–149). Use the placeholder in both.

---

### F12 — nitpick — one citation is off by a line

`Dragonfly/METHODOLOGY.md:152-153` is cited (129) for the `decisions.md` gate/decision-log
precedent. Line 152 is the `incidental-ledger.md` continuation; 153 is the `decisions.md` line. The
`Guarded_change/METHODOLOGY.md:175-182` citation in the same sentence overshoots by two lines (the
gate-log paragraph is 175–180; 182 begins "Ratification records"). Both point at the right material.

---

### F13 — minor — nothing requires S1–S9 to survive the next division

Each half is five files and will be handed to a child node that calls `Divisible` again
(`Architect/stages/node.md:50-53`, `34-40`). The seam travels only because it is physically inside
the sub-task text. The division's own justification for restating it — "It is self-contained: the
seam is restated inside it verbatim, because the agent planning this half will never see the other
half's output" (73–75) — applies with equal force one level down, and is not stated there. A
grandchild divider that re-words its sub-task text and drops S4 hands a `node.md` planner a task
with no blindness barrier, and nothing below it can detect the loss. One sentence in each sub-task
("carry S1–S9 verbatim into any further division") closes it.

---

## The four questions

**1. Coverage.** Good, and better than the interface. I walked every defining property in the task
text against the two halves: decompose/size/strategy → worker (sub-task two file 2, S7); N cold
analysts, read-only, cited → worker file 3 for content and driver for fan-out and coldness
(sub-task two's exclusion list at 283 puts fan-out in the driver, sub-task one's ownership list at
128–133 accepts it); cold verification of every citation → worker file 4; agreement-ranked merge →
worker file 5 at both levels; blind roll-up → S4 + S3 Invariant B + `node.md`; per-corpus config →
driver, key set and validation both (130–131); restart/resume → driver, keyed on S3 Invariant A;
facts-not-interpretation → worker `common.md`. **No orphaned remainder found and no portion both
halves assume the other owns.** The two things that leak (F1, F2) are not coverage gaps — they are
places where the *interface* prevents a covered owner from doing its job.

**2. The seam.** Stated, at length, and identically in both halves — I diffed the two copies
(153–227 vs 303–377) and they are identical in substance and wording. It is genuinely smaller than
the divider claims to have shrunk it from: no schema, no layout, no key set. **But it is not sound.**
S2 asserts a guarantee it does not deliver (F1) and is simultaneously exhaustive, which is what
converts F2 from an oversight into an unownable gap: an interface that says "exactly these
arguments" must be right the first time, and this one is missing two.

**3. The floor.** Not breached in either direction. Driver plane: `SKILL.md`, `METHODOLOGY.md`,
`stages/node.md`, the worked config instance, `README.md`. Worker plane: five files under `stages/`.
The floor is one file with its content specified; each half is five such steps and each half is a
coherent whole task. The install note at 122–124 correctly identifies that an install *action* has
no shape under a file-phrased floor and correctly declines to work beneath it — that reasoning is
sound and I am not filing against it (its consequence for ordering is F7, a different matter).
**No blocker against the division on floor grounds.**

**4. Real joint or arbitrary cut.** **Real.** What differs on each side: the driver plane's files
are read by an agent that dispatches others and is answerable for the run as a process; the worker
plane's files are read by an agent that does one bounded pass over evidence and is answerable for
the artifact it returns. The corrected failure sets at 393–395 are genuinely disjoint — stall /
ceiling / no-resume / no-handover / a steering coordinator on one side, uncited / unverified /
interpreted / copied on the other — and the divider was right to move *steered* across. The cut is
not a bisection for symmetry: the five-and-five file count is a coincidence of the skill's shape,
not the criterion. My only objection to the joint is that the *criterion as stated* is wrong for
`node.md` (F8); the boundary it draws is right.

---

## The six lenses

**1. Factual — issues found (F1 against the seam's own S2; F12 on citations).** Citations checked
against source, not accepted: `Dragonfly/SKILL.md:22` is indeed the cold-start guard and
`Guarded_change/SKILL.md` has none — verified by reading both files end to end. `Guarded_change/
SKILL.md:25-52` and `Dragonfly/SKILL.md:29-70` are the two Loop sections — verified.
`Guarded_change/METHODOLOGY.md:37-54` and `Dragonfly/METHODOLOGY.md:47-62` are fenced stage diagrams,
so "not as prose" is correct for both — verified. `Guarded_change/METHODOLOGY.md:103-152` is the
annotated YAML config skeleton — verified. `Dragonfly/METHODOLOGY.md:161` is `## Trigger` and
`Guarded_change/METHODOLOGY.md` has no Trigger section, so "Dragonfly only" is correct — verified.
`Guarded_change/METHODOLOGY.md:154-168` and `Dragonfly/METHODOLOGY.md:141-153` are the artifact
sections; every artifact listed in both is `.md`, so S9's "markdown without exception" is correct —
verified. `Guarded_change/METHODOLOGY.md:143` is the "operative rule lives in the stage files"
sentence, so the "named as such" precedent holds — verified. `Guarded_change/METHODOLOGY.md:88-100`
and `Dragonfly/METHODOLOGY.md:95-102` are the two-layer sections — verified. Both companion configs
exist at the claimed top-level paths and match the `<skill>.<thing>.md` naming — verified by `ls`.
Both READMEs exist and both carry the `~/.claude/skills/` install instruction
(`Guarded_change/README.md:110`, `Dragonfly/README.md:107`) — verified. `charter.md` in both
siblings is a shared core read ahead of a stage file's own additions
(`Guarded_change/stages/charter.md:1-6`), which is exactly the `common.md`-plus-role-file pattern
sub-task two is told to build — verified, and the precedent is aptly chosen.
**Unchecked:** the round-2 findings and dispositions (450–479) — I did not read `split-round-2.md`
or any sibling review, per my brief. **Unchecked by instruction:** anything in
`/home/zero/Desktop/claude-code-skills/Data-Distiller/`.

**2. Logical — issues found (F2, F3, F7).** The internal reasoning is otherwise sound; the
alternatives section reasons about real trade-offs rather than justifying a decision already made,
and the `Consensus`→`Union` cost named at 424–431 is correct against
`Architect/stages/node.md:44-53` and `combiner.md:20-52`.

**3. Missed opportunity — one issue (F10).** No superior cut identified. I considered
"reference-and-packaging (4 files) vs. all six prompt files", which round 3's structural move makes
newly viable and which would dissolve F1, F2, F4 and F5 by co-locating all six prompts; I do not
recommend it, because it moves the run loop and the blindness barrier onto opposite sides of the
cut, which is a worse crossing than the one we have. The finding is only that (c)'s recorded reason
no longer holds.

**4. Unstated assumptions & risks — issues found (F1, F3, F6, F13).** The load-bearing unstated
assumptions are: that locators resolve without a corpus root (F1); that `partial` means the same
thing to both halves (F3); that a status record will be terse because it may not contain claims
(F6); and that S1–S9 survives the next two levels of division (F13).

**5. Fidelity — one issue (F6), otherwise clean, terms pinned.** Each loaded term and the concrete
mechanism it is pinned to: **"cold agent"** → a separately spawned agent whose entire context is one
prompt file plus the S2 payload (S2, S5, sub-task two's preamble at 237–241). **"decompose"** →
`stages/decompose.md` emitting an item manifest of id+locator entries (S3), with `split` resolved
in-file as ordinary entries (S7) — a mechanism, not a gesture. **"N independent analysts"** → N
separate spawns, none handed another's output path, plus a worker-side prohibition on opening
anything not handed (S5); the two rules bind different actors and do not restate each other, which
is the correct shape. **"verify"** → re-opening every citation and dropping what fails, with the
test itself defined in `verify.md` (sub-task two file 4). **"agreement rank"** → a count of
concurring independent analysts, computed at two named levels (file 5). **"blind roll-up"** → an
absolute read prohibition on four artifact classes (S4) plus a return-channel restriction to
path-plus-one-word (S3 Invariant B) — genuinely two mechanisms rather than one restated, and the
Invariant B half closes the reply channel that a read prohibition alone leaves open. **"resume"** →
presence/absence of a status record written last (Invariant A). **"config"** → a Layer-2 file whose
key set, documentation and validation are all one half's, with values passed down at spawn.
**"facts, not interpretation"** → a rule in `common.md`. That last is pinned to a rule with no
verifying mechanism anywhere in the skill — `verify.md` re-checks citations, not interpretation —
but the division does assign it unambiguously to the worker half, so it is a matter for the plan and
not a defect of the cut; I record it rather than file it.

**6. Completeness — issues found (F2, F5, F9, F11, F13).** Structural checklist first: both
sub-tasks state their files, their exclusive ownership, their explicit non-ownership, their source
material, the OFF LIMITS boundary, and the full seam; the record section states the joint, the
failure sets, what crosses, what may be assumed, and what neither owns; alternatives and a floor
check are present. **Generative sweep run.** What I looked for that no checklist here anticipates:
(a) a route for *negative* information — what was not analyzed, what failed — to reach the human
(gap: F2); (b) an identifier by which the deliverable can name the things it is reporting coverage
on (gap: F5); (c) a rule preventing the two halves from documenting the same artifact differently
(gap: F9); (d) propagation of the seam through further division (gap: F13); (e) an ordering
constraint between the halves (gap: F7); (f) who dispatches `verify` as a fresh cold agent — covered
by the driver's ownership of "all control flow", though never named; (g) whether `N` and the fit
threshold have owners — both driver, via the config key set, correctly; (h) whether the driver is
told to prepend `common.md` at dispatch — carried only obliquely, inside the one-line purpose S1
makes the router publish verbatim, which is thin but sufficient.

---

## Summary of severities

| # | Severity | Finding |
|---|---|---|
| F1 | **blocker** | `analyst` and `verify` read the corpus but are handed no corpus root; S2's "every corpus-specific value arrives here" is false for them; round-2's I8 blocker is closed for `decompose` only |
| F2 | **major** | A unit failing before `merge` cannot reach the terminal deliverable — S2 exhaustive, S4 read-prohibited, S6 producer fixed; not closable by either half |
| F3 | minor | `partial` fixed as a word, undefined as a state; produced worker-side, consumed by driver-side resume |
| F4 | minor | Locator extent and outcome-word location unanchored, where the item id was anchored |
| F5 | minor | Coverage note must name items; no worker is handed an item id |
| F6 | minor | Blindness accountability sits with the driver; the status record's contents sit with the worker; "terse" is nowhere fixed |
| F7 | minor | Install/verify is order-dependent and lands first under `Union`; the seam asserts "no ordering" |
| F8 | minor | Stated joint criterion is wrong for `node.md` (a child node is spawned cold); driver half unsignposted for cold-prompt precedent |
| F9 | minor | Driver's `METHODOLOGY.md` artifact section will describe worker-owned artifact contents, per both siblings' precedent |
| F10 | minor | Alternative (c) rejected on a premise round 3's own structural move retired |
| F11 | nitpick | S4 hardcodes `FINDINGS.md` against the seam's own "no paths fixed here" |
| F12 | nitpick | `Dragonfly/METHODOLOGY.md:152-153` and `Guarded_change/METHODOLOGY.md:175-182` each off by a line or two |
| F13 | minor | Nothing requires S1–S9 to be carried verbatim into the next division |

**On the floor:** no finding above has a remedy that decomposes below the granularity floor. Every
one is a clause added to, or a word changed in, the seam or a sub-task's text.
