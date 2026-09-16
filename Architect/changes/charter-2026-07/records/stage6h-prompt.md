# Gate 7, pass 6 — TARGETED cold red-team (2026-07-30)

You are a **cold, independent reviewer**, with no shared context with this artifact's author or with the
reviewers dispatched alongside you. **Nothing here is true because it is written here** — every claim below
is the author's, including its account of what it repaired, of what earlier reviewers found, and of what
the owner ruled.

Repo root: `/home/zero/Desktop/claude-code-skills/.claude/worktrees/recursing-visvesvaraya-b40a0c`

**Why this round exists, stated plainly.** Five rounds have run (records `reviewer-{A..X}-verbatim.md`).
Pass 5 was a single reviewer, **X**, which returned `blocker` and **demonstrated two working exploits**
against the closed-set apparatus plus a fourth non-termination route. Everything since — a rewritten common
core, **two new oracles**, a **change to the owner's design spec**, and four new criteria families — was
authored by the same agent X had just found two exploits and two false escalations against. **None of it
has been seen cold.** That is what you are for.

**The standing failure mode of this run: for four passes in a row, a repair was written narrower than the
claim made for it.** Assume it again.

---

## 1. THE ARTIFACT — verify every hash. If one differs, **say so and keep going**, recording which bytes you held.

`Architect/stages/`, nine files, **1,406 lines**.

| File | sha256 |
|---|---|
| `charter.md` (manifest, **not dispatched**) | `f8ff03d82fb192b780e3557999bf7a22f65c54880695264a638dfc2fb557ab21` |
| `charter-common.md` (verbatim to every role) | `6950608bf6d657fe6d43eeff9572c6c0a530ccd008704c5066bf570f5f00e9d7` |
| `redteam.md` | `c28fcbcf634ee5b781872a6da8776ccddb162ff1c1346750fbc303d02102b838` |
| `redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` |
| `redteam-split.md` | `eaac765de929a592e03ea1d365b49d48956e4a004be9df428cda755856591a4e` |
| `divider.md` | `cd45e149369e1abbc122a7af245357930059e603c1722383cc657e740e60442c` |
| `combiner.md` | `142a192d48dbf33b215ce28ea1f994803bf803ee3657019388dd2bfa2815c304` |
| `leaf.md` | `84e967124ecb599d7b519e8468cb997b577b8ec2c3d44468763561a84114b88f` |
| `node.md` | `3a00d272117639262fa35d37e899b2ca119049798260e0e99ba1f40fd6fa18d1` |

**A dispatched prompt is `charter-common.md` verbatim + role file(s). Review the composed prompt** — three
defects in this run's history were visible only after concatenation.

The harness, `Architect/changes/charter-2026-07/oracles/`:

| File | sha256 | |
|---|---|---|
| `ruleplace.sh` | `be60b9b0c6c4b53b7bb46ea45c823777a777e5e10aee4ca6d0add2daca537ba3` | |
| `rules.tsv` | `4abeb10ce33404c529fee8cdd0dbc9c97b015c25c650c02175725f5d0059c677` | **author-written** |
| `shared_spans.py` | `e17bfa96414027df556cdc1f236aa97128d7ff475163896c9cd5b28ff2ff4076` | changed in pass 5 |
| `declared-duplications.jsonl` | `ed42a3348df456be958c24fd92a13c02600c224a1a61d506e08fa850923c38b8` | regenerated |
| `sigmatch.py` | `b4d05677b43d77f194c72c681b559ec00a834d2345c95cdc0972540439fd7a00` | **NEW** |
| `citecheck.py` | `2e1d3d92f83b9e744fa4fae78825cc52f778aefa96995b0ec2ecfbc5f5baf3ae` | **NEW** |
| `mutation-test.sh` | `061098222705d1248ba7c93812735e30909da68ebbfd6e639c805a28ae637180` | unchanged |

## 2. AUTHORITY, and the warning this round exists to enforce

1. **The owner's words**, at their record index in
   `/home/zero/.claude/projects/-home-zero-Desktop-claude-code-skills--claude-worktrees-recursing-visvesvaraya-b40a0c/45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl`.
   **The only admissible source.** ⚠ **Record numbers are 1-BASED: record N is line N. Read one with
   `sed -n 'Np' <jsonl>`, never by indexing a parsed list** — the author of these repairs made exactly that
   mistake, reported all seven of its loci one low, and wrote the discrepancy up as an off-by-one *in the
   corpus*. Retracted in `decisions.md` ADJ-2 and ADJ-7. **Treat every locus in the set as a claim to
   re-verify.** Loci: **1044** (the owner's ORIGINAL spec, an `attachment` record, 2,278 chars / 58 lines),
   **1175**, **1254**, **1258**, **1449**, **1787**, **2524**, **2680**, **3119**.
2. **`~/Documents/Architect.md`** — **142 lines**, sha256
   `bd0dc364208812c3e04290e0fe9f3f5f1bdff49500027856397af6d418875f60`. ⚠ **Owner-SEEDED, not
   owner-written**, and **it changed twice on 2026-07-30** — once for the owner's three rulings at record
   3119, and once by **the runner**, which added a parameter to `Severity`'s signature. *"The spec says X"*
   is not *"the owner said X."*
3. `Guarded_change/stages/charter.md` and `stage-4.md` · `changes/charter-2026-07/0-baseline.md`.

## 3. SCOPE A — the closed-set apparatus. **Highest value: break it a third time.**

Reviewer U broke it in pass 4. Reviewer X broke it **twice** in pass 5, after U's break was repaired.
**Both of X's exploits are now standing regression tests and both exit 1.** The question is whether the
repairs closed the *class* or the two *instances*.

- **X's Exploit A** appended `depth` and `node_id` to `leaf.md`'s closed set — which per `charter-common.md`
  §6 is **the gate on calling `Ask_human`** — and passed both oracles. Fixed by **`sigmatch.py`**, which
  parses signatures out of the design spec and asserts no role file's enumeration claims an argument its
  function lacks. **Attack `sigmatch.py` directly**: its `WATCHED` vocabulary is a **closed list of six
  names**; it anchors on a paragraph beginning `Exactly` (and one special case for `redteam.md`); it treats
  `combiner.md` as the union of three signatures. **Find a closed-set forgery it cannot see.**
- **X's Exploit B** smuggled a 36-word rule — relaxing the granularity floor and imposing a backstop cap
  the owner declined — past a 5-word declared scaffolding heading, because `shared_spans.py` exempted any
  span that *contained* a declared one. Containment now runs one way. **That fix then exposed 19 undeclared
  spans on the clean artifact**, and the register was regenerated at maximal span length. **Read the
  regenerated register (`declared-duplications.jsonl`, now 23 entries) and ask whether any entry is
  over-broad.** A declaration that covers more than it names is how both exploits worked.

## 4. SCOPE B — the two NEW oracles, and whether they are instruments or decoration

**`sigmatch.py`** and **`citecheck.py`** were written by the author of the artifact they check.

- **Reproduce the can-fail tests** in `records/harness-run-2026-07-30.txt` yourself. Do not accept them.
- **`citecheck.py` was cut down after three failed designs.** The author's own account (`decisions.md`
  ADJ-14) is that iterations 1 and 2 produced 6 and 15 false alarms **on a clean artifact**, and iteration 3
  reported a confident *"0 mis-cited"* while **passing vacuously** — its regression test did not fire. The
  shipped version checks **only that a cited record exists and is a kind that carries authored text**; it
  does **not** verify the quoted words, ignores records under 100, and does not scan the run folder.
  **Is the reduced check worth its place, or is it a fifth instrument that mostly cannot fail?** Rule on it.
- **The author claims `sigmatch.py` is N-04's missing arm and `citecheck.py` is N-13's**, not new
  instruments — and cites `1.5-criteria-v2.md`'s own coverage table (*"N-13 … Never had an arm"*) as
  support. **Check that claim.** If either is really a new instrument, the owner's three-iteration rule
  (record **2544**) reopens the venue question, and that judgement is yours, not the author's.

## 5. SCOPE C — the four new criteria families, and a freeze breach the author self-reported

`1.5-criteria-v2.md` now carries **FRZ-3** and **FRZ-4**. Two gating criteria were amended because they were
**factually false against the artifact they gate**; several were added.

- **Apply reviewer O's test to every FRZ-3 and FRZ-4 row:** *a criterion written from the shipped text
  cannot fail against it.* O ruled two FRZ-2 additions defective on exactly that ground.
- **N-39** — *"every loop in the set states its own bound"* — is a universal quantifier over nine files
  backed by **two string-presence checks in one file**. The author concedes this. **Is any other new row in
  the same state?**
- ⚠ **The author edited a gating probe (`rules.tsv` N-40a) while reviewer X was mid-review, then told X in
  a correction message that "the harness is unchanged" — which was false.** It is recorded in
  `decisions.md` ADJ-11 and covered retroactively by FRZ-4. **Is retroactive coverage adequate, or does it
  invalidate part of pass 5?**

## 6. SCOPE D — the owner's three rulings, and the ONE the runner decided for itself

Owner record **3119** ruled: `task` carries the source material; `Severity` may write filtered minors to the
decision log; and "stuck" means no writes for an extended period **and** no reply to a ping. **Read 3119 in
full yourself.**

⚠ **The owner delegated one mechanical point and the runner resolved it by CHANGING HIS SPEC:** `Severity`
now takes `_node_id`. The runner's argument is that the ruling requires `Log_decision`, `Log_decision`
requires a `node_id`, and a cold agent's inputs are exactly its arguments — so it is forced, not chosen.
**Test that.** Is there a resolution that does not touch the spec? Does the change have consequences the
runner did not trace — for `Union`'s output feeding `Severity`, for the memo, for crash replay, for
`combiner.md`'s closed set? **A runner editing the owner's design file is the highest-stakes thing in this
pass.**

Also: **does the "stuck" definition actually work?** `node.md` tells a node to stop waiting, log, and merge
what it has. **Trace what happens to the stuck agent's slot, to `work_queue`, and to the memo.**

## 7. RUN EVERY ORACLE YOURSELF

```
cd Architect/changes/charter-2026-07
./oracles/ruleplace.sh    ../../stages
./oracles/sigmatch.py     ../../stages
./oracles/citecheck.py    ../../stages
./oracles/shared_spans.py ../../stages 7 --exempt-file oracles/declared-duplications.jsonl
./oracles/mutation-test.sh ../../stages
```
Author's claim: **148/0** (+21 SMOKE, gating in neither direction), **42/0**, **18 cited records / 0 not
citable**, **0 undeclared spans**, **157/0 mutants**, and **exit 2** from each with no argument.
⚠ **Capture exit codes directly, never through a pipe** — `$?` after a pipe is the last command's status,
and this runner recorded a script's exit wrongly **three times today**, in the file whose purpose is
proving the exit codes.

## 8. YOUR RECORD

Follow `charter-common.md` §5: path + sha256 of every file you read, your agent type and model, what you
ran, and **what you did NOT check — reported as unchecked, never as accepted.**

**Your final assistant message IS your record** — it is extracted verbatim from the harness transcript. Put
the whole review in it; do not end with a summary of a longer review written earlier in the turn, and do
not write the review to a file instead.

**You are read-only with respect to the repository.** Copy the artifact to your scratchpad if you want to
run mutation experiments — that is encouraged and is the highest-value thing you can do.

**Everything in §§1–7 of this prompt is author-authored supplementary context** and must be quoted as such
in your record, per §0/§5.

**Verdict, one word: `blocker` / `major` / `minor` / `clean`.** An earned-clean verdict requires you to
state what you checked that could have failed and did not.
