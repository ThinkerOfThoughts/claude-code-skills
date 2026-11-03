I have completed the audit. Here is my review record.

---

```
AGENT TYPE / MODEL: general-purpose subagent / claude-opus-5
SPAWN IDENTITY: session 45cb99a2-543d-4447-a3e3-2a38963b0775 (from my own scratchpad path);
                no separate agent id is reportable about myself
FRAME: CLOSURE AUDIT / SOURCE-ANCHORED — "was each carried-forward finding closed in the mechanism,
       or only in the wording?"
CONTEXT FILES READ (sha256):
  Architect/changes/hardening-cycle-1/0-baseline.md    ef8f14ad864972aa29da93ae70267565107b90651aa8e7f76e0acb3bc8cadfc7
  Architect/changes/hardening-cycle-1/1-spec.md        14110a9be683212f1ad36a013826d34f2ae5b74618a4fa0a45e0dee5b82c3933
  Architect/changes/hardening-cycle-1/1.5-criteria.md  62227eb1d9c9c107cacfe1517ba16c51982da95e20b583bbaa9af2467ba00a66
  Architect/changes/hardening-cycle-1/2-plan.md        0afe0acd19ed145b8061d61d2357528ed601ae6ac7e554a5250331ee5982cabf
  Architect/changes/hardening-cycle-1/3-charter-given.md 1b3c1da3be65cd07fdcc204e6b7437c56a78a4dbda29e2cdea145055477a39a4
  Architect/changes/hardening-cycle-1/3-redteam-plan.md  6e4ba56ca015dd798772a53c91136b364014977c55ae8e2c111c9ee1f3fbd160
  /home/zero/architect-dogfood-2026-07-24/FINDINGS.md  94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8
  /home/zero/architect-hardening-loop/LOOP-STATE.md    0d1dfab5f774747807194a4e7e390d68a186ea3664e1532c18108dff8e79cba8
  /home/zero/.claude/plans/1-this-is-a-proud-scott.md  aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249
  Architect/SKILL.md                                   7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450
  Architect/METHODOLOGY.md                             f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa
  Architect/README.md                                  79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a
  Architect/stages/charter.md                          6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819
  Architect/stages/stage-1-frame-template-match.md      ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5
  Architect/stages/stage-2-draft-node.md                2e76963ce446190ff4bb4d8100a097d8a62e684d5936d38a74e227aea3ad1036
  Architect/stages/stage-3-completeness-critic.md       6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e
  Architect/stages/stage-4-adversarial-redteam.md       96570a6d9298c67ab6b5fe8653b16cf7068fdbe547373a32bee3e02c0721f07c
  Architect/stages/stage-5-gate.md                      99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5
  Architect/stages/stage-6-granularity-decompose.md     b202101b7b4b16314d4742851138b53efe40b33f3025886149f02ba4aeac1993
  Architect/stages/stage-7-assemble.md                  864b74dcfcf43e18b576145327beeb011b1e44bb672f7a10e8d8b0f9ad9cb607
  Architect/stages/stage-8-restart-resume.md            97431f52e7487ab34c9e9278496b687ca2b4ca2bf178203de3d76151c35762c1
  Architect/templates/seed/generic-node.md              7148ec60e18b8cf4606b50b0fc8b49f299731b3d3c26a4787bc0a8bf0be52e89
  Architect/templates/seed/decomposition-node.md        b4509defabe16768edcd024a98f44f37c90351aef5fa759b56b0c0930a98cf64
  Architect/templates/seed/leaf-task-spec.md            c7341c863a494a41e616e00b70c14bf8034cfe292108e2dca92436847c3f093e
  Architect/templates/seed/README.md                    d2a86068b92d7ee6b47b7af6dd506f456b589a50a6cac7e0e8d15d23246b3fb4
  Architect/examples/authoring-a-skill/planning.md      b52a22d2012e7a640e68300a2a8f0a985e811e024c0259b26d7d0aabc6ec37ea
  Guarded_change/stages/stage-3.md                      (read RAT1 §§55-108 only; not hashed in full)
  Architect/changes/hardening-cycle-1/3-redteam-plan.A.verbatim.md 60161a6f7e9733ec03c5e5437c50b91e2de6d0e6f779bcd28ea61c361884e1cb
  Architect/changes/hardening-cycle-1/3-redteam-plan.B.verbatim.md 93587c9c8509a193b2562fd59d5450b612cd6cfd43fe6c1c201a277e145acd7f
  Architect/changes/hardening-cycle-1/3-redteam-plan.C.verbatim.md bdf50c7db67802c246df342621a7065d93016d3db11b5e7583eb99c4103649e3

  (The four stage-artifact hashes are byte-identical to `context-hashes.pass2.txt` captured before dispatch.)

FILES I WAS GIVEN BUT DID NOT READ (or read only partially — declared):
  - `3-redteam-plan.{A,B,C}.verbatim.md` — NOT read in full. I worked from the consolidated blocker +
    convergence tables in `3-redteam-plan.md`, and grepped the three records only to check whether my
    own findings were already raised in pass 1 (novelty check). Hashed above.
  - `1-spec.v1-superseded.md`, `1.5-criteria.v1-superseded.md`, `2-plan.v1-superseded.md` — not read
    (pass-1 content reached me via the consolidated index).
  - `decisions.md` (this folder) — not read.
  - `Guarded_change/` — read only `stages/stage-3.md` RAT1/CH11 and grepped `SKILL.md`; did not read
    `METHODOLOGY.md` or other stages.
  - `Dragonfly/`, `Data-Distiller/`, `Architect/guarded-change.architect.md` — grepped only, for ID-namespace
    collisions. Not read.
  - `Architect/examples/authoring-a-skill/README.md` — not read.
  - `Architect/changes/initial-authoring-2026-07/` — not read (frozen).

ANYTHING I READ OUTSIDE THE CLOSED SET: none.
```

---

# LENS 1 — FACTUAL (does the artifact match the source?)

**F1-1 · BLOCKER · D2(b) and D3 make the terminal-status write unproducible at *every* node — B/L-1 is re-opened by pass 2's own assembly-ordering fix.**

`2-plan.md:92-93` (D2) makes subtree-complete require *"(b) its own `_assembled.md` exists"*. `2-plan.md:68` (§1b) assigns `_assembled.md` to **stage 7**. `2-plan.md:106-108` (D3) assigns the write of `subtree: complete` to **stage 6 (LEAF)** — explicitly *"after its own stage 7 has written `_assembled.md`"* — and to **stage 6.5** *"once (a)–(c) hold"*. But stage 6 and stage 6.5 both run **before** stage 7 (`SKILL.md:58-59` stage table; `S-F1.1` places 6.5 between 6 and 7), and nothing re-enters them: `2-plan.md:144-145` re-affirms stage-done = *"the deterministic output exists"*, and 6.5's deterministic output is `_join.md` (`2-plan.md:66`, `S-F1.8`).

Failure scenario, the exact tree B/L-1 named: root + one leaf.
1. Leaf runs 1→5, gates clean. Stage 6 LEAF branch fires; `_assembled.md` does not exist (stage 7 has not run); the condition in D3 is false; **nothing is written**.
2. Leaf runs stage 7, writes `_assembled.md`. No stage is assigned to write `subtree: complete` at or after stage 7 (`2-plan.md:46` lists only stages 6, 6.5, 5 as producers of `subtree`).
3. Root's 6.5 polls: `children.leaf.subtree` is non-terminal → D4's dead test fires (`2-plan.md:114-116`) → re-dispatch → the leaf's stage-done predicates make everything a no-op → escalate.
The root itself is worse: its own 6.5 can never satisfy (b) because only its own stage 7 — which runs after 6.5 — produces `_assembled.md`. **This is a self-deadlock, not just a leaf-case gap.**

This is not a wording residue: it is `PRD`'s own violation in `PRD`'s headline table — the *trigger* for the write (`2-plan.md:107`, "after its own stage 7 has written `_assembled.md`") is an event in a **later stage than the assigned writer**. `S-F1.4` will pass (all three producers *are* stated in the stage files), so the gating criterion cannot see it.
**What I'd do instead:** assign the terminal-status write to **stage 7** as its final numbered step (it is the stage whose output the predicate reads), and change `S-F1.4` to assert the producer is the stage that runs *after* `_assembled.md` exists. Alternatively drop (b) from D2 and order assembly by a separate `assembled: yes` key with its own stage-7 producer.

---

**F1-2 · MAJOR · B/L-3 is re-worded, not closed: `children.<c>.declared_seam_sha256` has no defined *content* at its stage-2 initial write, and the two hashed objects are different documents.**

`2-plan.md:40` defines `seam_sha256 = sha256(normalize(§3 + the decomposition seam table))` of **the child's own plan**. `2-plan.md:48` assigns `children.<c>.declared_seam_sha256` to *"**stage 2** (initial) / **stage 6.5** (on accepting a re-plan)"*, trigger *"own plan written"*. `2-plan.md:153-154` makes the reopen test an equality on the two strings. `2-plan.md:156` says that on a reopen the parent *"sets `children.<c>.declared_seam_sha256` to **the child's new value**."*

At the parent's stage 2 the child does not exist and has no `plan.md`, so the child's `seam_sha256` is not computable — the initial write has no operand. Only two coherent fillings exist and both break:
- **Copy-on-observe** (consistent with `:156`): the parent stores whatever the child last produced. Then the equality in D2(c) (`2-plan.md:96`) is self-referential and checks nothing, and the detector detects only "the child changed since I last looked" — never "the child's seam does not satisfy my plan", which is the F2 case (`FINDINGS.md:48-50`: three individually-clean nodes shipping a contradictory seam).
- **Parent's expectation** (hash of the parent's own seam-table row): then the two hashes are digests of *different texts* and will never be equal, so a reopen fires on every child at every poll until CAP forces a human tie-break (`2-plan.md:162-163`) at every decomposing node.

`S-F2.3` asserts *"**Both operands have producers** — the gap that made pass 1's detector uncomputable"* — true in letter, and the mechanism is still undecidable. Pass 1's defect ("no slot for the parent's expectation") has become "a slot with no rule for what goes in it."
**Mitigating fact, stated:** D7's assembly-time three-way seam comparison (`2-plan.md:168-173`) *does* address F2's substance independently. So F2 is partly covered; the *reopen detector* is not.
**What I'd do instead:** state the initial value explicitly — either `declared_seam_sha256 = sha256(normalize(the parent's seam-table row for <c>))` **and** require the child to hash the *same* normalized row into its own `seam_sha256` (making the equality meaningful), or drop the reopen detector to an honest change-detector and say so, with the correctness check living entirely in the assembly comparison.

---

**F1-3 · MAJOR · `oracles/idcollide.sh`, as specified, flags four *baseline* IDs; `B0.7`'s can-fail claim "run at baseline it flags nothing" is false.**

The spec is `2-plan.md:342-344`: *"for **every** ID in `METHODOLOGY`'s index, assert the token is **not a substring of any other uppercase token in the corpus**."* `0-baseline.md:170` claims *"Run at baseline it flags nothing (the baseline IDs pass)."*

I ran exactly that, over `SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/` at `3771038`, against the 18 IDs in `METHODOLOGY.md`'s cross-file index (`METHODOLOGY.md:315-333`):

| ID | is a substring of these uppercase corpus tokens |
|---|---|
| `CMP` | `CMP2` |
| `TOP` | `HARDSTOP`, `TOP-LEVEL` (`stage-6:15`) |
| `DEC` | `DECOMPOSE`, `DECOMPOSES` |
| `TPL` | `TPL1`, `TPL2`, `TPL3` |

Four flags, not zero. `DEC ⊂ DECOMPOSE` is the same class as `KIL ⊂ SKILL` and it is caused by the corpus's own ALL-CAPS emphasis habit — the forward risk this oracle exists to police. `TPL ⊂ TPL1/2/3` gets **worse** under this change, which adds index rows for `TPL1`/`TPL2` (`S-SC2`, `1.5-criteria.md:344-346`).

Consequence: `S-SC2` is gating and its oracle cannot pass on unchanged, intentional baseline structure. The predictable build-time repair is to weaken the matcher until it passes — which is precisely how `B0.2` was produced (`0-baseline.md:160-161`: *"recorded the lesson as a **comment** and then trusted a matcher that did not implement it"*).
**What I'd do instead:** specify an **explicit, reported allow-list of intentional ID families** (`TPL`/`TPL1`/`TPL2`/`TPL3`, `CMP`/`CMP2`, `PASS1`/`PASS2`) plus an **excluded-emphasis-token list** (`HARDSTOP`, `TOP-LEVEL`, `DECOMPOSE(S)`) on the same "report, never silently drop" contract `ORACLE-SITEMAP` already carries (`0-baseline.md:164-167`), and correct `B0.7`'s baseline claim to "flags 4, all allow-listed."

---

**F1-4 · MINOR · `S-F7`'s self-test number is miscalibrated in the file dimension: "8 occurrences across 5 files" is 8 across **4**.**

`1.5-criteria.md:199-200` and `0-baseline.md:180-181` both state the overclaim is present at *"**8 occurrences across 5 files**"*. Under the natural predicate (`proven|proving|proves`, word-boundary) I get **exactly 8 occurrences** — `SKILL.md:3`, `SKILL.md:8`, `SKILL.md:17`, `METHODOLOGY.md:4`, `METHODOLOGY.md:40`, `README.md:10`, `README.md:12`, `stages/stage-7-assemble.md:26` — across **4 files**. That is precisely the set `B0.8` enumerates. A 5th file is reachable only by also counting `stages/stage-3-completeness-critic.md:6` ("prove the plan whole"), which makes it **9 across 5**. No consistent predicate yields 8/5.
**Consequence:** the `S-F7` baseline-replay self-test will not reproduce its stated expectation, and the harness cannot tell whether the oracle or the number is wrong — the same failure mode as pass 1's `S-C5` "2 of 3" and `S-C10` "5".
**Fix:** state "8 occurrences across 4 files" and pin the sweep predicate (`proven|proving|proves`, normalized), listing the 8 loci.

---

**F1-5 · MINOR · `S-C10`'s pinned extraction predicate excludes the two prose sites that produce the "6" — under the predicate as written the baseline count is 5, and the two divergent sites survive a passing criterion.**

`1.5-criteria.md:326-327` pins the predicate to *"markdown headings matching `^#+ .*Outputs` **plus** the numbered spine enumeration entries — **the two site classes**"*, and `:331` sets the baseline self-test to **6** distinct normalized strings.

Measured at baseline, the two pinned classes give **6 sites / 5 distinct strings**:
`generic-node.md:16` and `decomposition-node.md:10` (identical), `leaf-task-spec.md:13`, `METHODOLOGY.md:121`, `SKILL.md:18`, `stage-2:11-12`.
The 6th distinct string comes only from the two **prose** sites `B0.8` discovered — `stage-3:43` and `METHODOLOGY.md:322` (both normalize to *"Outputs & artifacts with locations"*), and **neither is a markdown heading nor a numbered enumeration entry**. So: the number requires a third site class the predicate excludes, and — worse — the criterion's post-state requirement ("distinct count over that pinned set must be **1**") lets `stage-3:43` and `METHODOLOGY.md:322` keep a divergent spelling while the criterion passes. Those are exactly the sites the pass-2 correction added.
**Fix:** make it three site classes (headings · numbered enumeration entries · the two named prose/index sites, listed by file:line) and set the baseline count to 6 under that predicate.

---

**F1-6 · MINOR · `R2`'s newly-authoritative P-item list omits **P7**, whose baseline claim this change explicitly replaces at four sites.**

`1.5-criteria.md:385` fixes the list at *"P2, P4, P5, P9, P10, P13, P15, P16, P21, P23, P24"*. But `2-plan.md:144-145` (D6) states *"Restart contract amends to: **stage-done = the deterministic output exists AND, for a review record, it is BIND-current**"* — i.e. it replaces P7's baseline claim (`0-baseline.md:76`: *"`stage-8:15` stage-done = output-**exists** only"*). That claim is stated at **four** baseline sites plus an index row:

- `stages/stage-8-restart-resume.md:15` — "**Stage-done-iff-output-exists**"
- `stages/stage-8-restart-resume.md:21` — "stage-done is an output-exists check"
- `METHODOLOGY.md:239` — "**Stage-done-iff-output-exists.**"
- `METHODOLOGY.md:244` — "stage-done is an output-exists check"
- `METHODOLOGY.md:332` — RST index row: "stage-done-iff-output-exists"

`S-F3.4` only requires that *"`stage-8` amends stage-done"* — one file. So a build can amend `stage-8` and leave `METHODOLOGY.md:239/244/332` asserting the unqualified rule, and **both** `S-F3` and `R2` pass. This is exactly the half-migrated-rule defect `R2` exists to catch (and `R2`'s own note calls out the intra-file variant at `stage-5`). `S-SC2` does not close it either: its stated oracle is *"a recorded hand-diff of every **new** ID's operative claim"* (`1.5-criteria.md:348-349`) — the 21 baseline IDs' operative-claim consistency, including `RST`, has **no** oracle.
**Fix:** add **P7** to `R2`'s list with its five loci, and extend the `S-SC2` hand-diff to the baseline IDs the change touches (`RST`, `GBP`, `SEV`, `TOP`, `DEC`, `TPL3`).

---

**F1-7 · MINOR · "15 with `PRD`" is 14; the error propagates into two gating criteria.**

`1.5-criteria.md:29-30` lists `PRD, JOIN, SEAM, BIND, KLB, PRV, DIV, IDN, RES, CNC, CTX, XPM, IGM, DEP` and calls it *"**15 with `PRD`**"* — that is **14** items, `PRD` included. `S-SC2` then asserts coverage of *"the **15** new IDs"* (`:344`) and `2-plan.md:385` repeats "15 new IDs". An oracle built to the stated count will look for a fifteenth ID that does not exist.

---

**F1-8 · NITPICK · `B0.8`'s corrected `P2` line list covers 10 of 13 sites; `§1b`'s `APPROVAL.md` row cross-references the wrong section and D-item.**

- `0-baseline.md:178-179`: the count **13×** is correct under the bare `_status` predicate (I measured 13), but the enumerated lines omit `METHODOLOGY.md:236`, `stage-6:12` and `stage-8:10`. The material claim ("no schema, no writer named") holds; the site list is 10/13, which under-specifies `R2`'s P2 row.
- `2-plan.md:73` points to *"see §3 D7"* for the topgate. The topgate is **D9**, and the D-items live in **§2** (§3 is Measurement).

---

# LENS 2 — LOGICAL (flaws in the plan/reasoning/sequencing)

**F2-1 · MAJOR · `subtree: escalated` is an absorbing state with no exit producer — a new defect created by the B/L-2 fix.**

Making `escalated` **terminal** (`2-plan.md:88`, `:98`) closes B/L-2 (see the closure list below), but nothing writes the state that *leaves* it:
- D2(c) (`2-plan.md:96-97`) accepts a child only as `complete` or `killed`.
- `2-plan.md:98`: *"`escalated` is **terminal but NOT complete** — assembly blocks on it and it **must be resolved or killed**."*
- D5 (`2-plan.md:128-131`) says the parent *"resolves it within its own scope … or **relays it verbatim upward**"* — neither of which writes any `subtree` value.
- `2-plan.md:118-120`: *"a resuming parent re-dispatches every **non-terminal** child"* — escalated is terminal, so it is **never** re-dispatched.
- `2-plan.md:46` lists `subtree`'s producers as stages 6 / 6.5 / 5 **of that node's own owner**; the escalated node's owner returned at stage 5.

So after any escalation is answered, no rule names who flips the child off `escalated`, and the only reachable terminal is `killed` — which requires an authority (`2-plan.md:69`) that under RAT3 with the owner asleep does not exist. Assembly blocks permanently. This is `PRD`'s test applied to `PRD`'s own output: the gate reads `children.<c>.subtree`, needs it to reach `complete`, and the transition has no producer.
**Fix:** name the producer — the parent's 6.5, on a resolved escalation, increments `dispatch_seq` and **re-dispatches** the child (which re-enters at the first non-BIND-current stage), and `escalated` is added to the set of statuses a resuming parent re-dispatches.

---

**F2-2 · MAJOR · The relay of an escalation has no producer.**

`2-plan.md:45` assigns `escalation:` to **stage 5** with the trigger *"a blocker / cap tie / missing config unresolvable **here**"*, reader *"parent's stage 6.5 → relay"*. D5 (`:129-131`) requires the parent to *"relay it verbatim upward — recursively to the top orchestrator, then under RAT3 to the human"*. The relay is a **write** (the question must appear in the parent's own record/status for the grandparent to read), it happens at the parent's **stage 6.5**, and stage 6.5 is not a permitted writer of `escalation:`. So either the relay chain is unproduced, or `escalation:` has a second writer absent from the table — and the table's closing claim (`2-plan.md:79`, *"Nothing in §2–§3 reads a fact absent from this table"*) fails on the very wire `RAT3` was said to be missing (`FINDINGS.md:39-40`).
**Fix:** add a row — `escalation` written by **stage 5** (originating) **or stage 6.5** (relaying, verbatim, with `escalation_origin: <child path>` so the chain is auditable).

---

**F2-3 · MAJOR · `S-PRD`'s oracle checks *mention*, not *production*; ~half the (key, stage) pairs already pass at baseline, and its self-test is a zero-input vacuous pass.**

`1.5-criteria.md:41-43`: *"for each (key, stage) pair in the canonical block, **the key appears in that stage's file**"* — and `:49`: *"**Self-test:** baseline replay — no `PRD`, no schema block, **zero pairs**."*

Two defects, both fatal to the pass's organizing criterion:
1. **The assertion is satisfiable by prose coincidence.** I tested the sampled pairs against the *baseline* files. 7 of 14 already pass: `node`→stage-1, `template`→stage-1, `stage`→stage-1, `granularity`→stage-2, `granularity`→stage-6, `gate`→stage-5, `subtree`→stage-6. These are ordinary English words in a prompt corpus. The check also cannot distinguish a **write** from a **read** or an incidental mention — which is the entire content of `PRD`.
2. **The self-test cannot fail.** At baseline the canonical block is absent, so the parser yields *zero pairs* and the assertion is vacuously satisfied. The self-test proves the block's absence; it never exercises the assertion's discriminating power. That is the defect class that made pass 1's `R1` `verified = no`.

`S-PRD` is `1.5-criteria.md:43`'s *"the assertion whose absence produced 4 of pass 1's 5 blockers"* — and it is the weakest oracle in the set.
**Fix:** require a **positive write-sentence** per key (e.g. the stage file must contain the key adjacent to an imperative write verb, or a stage-level `WRITES:` manifest block that the oracle parses and diffs against the canonical block both ways), and give the self-test real input: plant the canonical block into the baseline tree with one key's write-sentence deleted; the oracle must flag that key.

---

**F2-4 · MAJOR · `off_limits_paths` fences `plan/topgate/` while two other rules require writes inside it — `S-F5.2` and `S-F5.6/5.8` cannot both be satisfied.**

- `2-plan.md:189-190` / `S-F5.2`: *"`plan/topgate/` **and the cited owner-source locus are listed in `off_limits_paths`** — **the run may not write there**."*
- `2-plan.md:197-201` / `S-F5.6`: `APPROVAL.md` may be written by *"the owner directly, **or an orchestrator/intermediary acting as transcriber**"*.
- `2-plan.md:74` / `S-F5.8`: `plan/topgate/AUDIT.md` is written by *"a **single-purpose cold auditor**"* — an agent the run dispatches, writing into the fenced directory.

Neither the plan nor the criteria pin **"the runner"** against **"an orchestrator"**. In this skill the top orchestrator *is* the run: `2-plan.md:71-72,77` assign `index.md`, `plan/decisions.md` and the catalog to *"**top orchestrator only**"* as run actions. So the actor D9 admits as an author is the actor the fence excludes — and per `FINDINGS.md:75-76` it is exactly that actor which executed the live F5 defeat (*"the runner authored its own approval and attributed an **intermediary agent's** prompt text to Roy"*). Pass 1's flaw was stating only who may *not* write it; pass 2 states a positive admissibility rule that **re-admits the intermediary** and simultaneously fences it out.
Also: *"the cited owner-source locus"* cannot be pre-listed in a static config — it is only known after the approval exists.
**Fix:** fence the **file** `plan/topgate/APPROVAL.md`, not the directory; define "the runner" positively as *"any agent this run spawned, at any depth, including every (sub-)orchestrator"*; and state that `AUDIT.md` is the single admissible run-authored file under `plan/topgate/`.

---

**F2-5 · MAJOR · `plan/ABORTED.md` gets a rule where `APPROVAL.md` gets a fence — the pass's own principle 1 is not applied to the dissolve-any-gate button.**

`2-plan.md:14-16` states principle 1: *"**Remove the failure mode, don't guard it.** The runner cannot write `APPROVAL.md` because the path is **fenced**."* But `plan/ABORTED.md` sits at `plan/`, **not** under `plan/topgate/`, so it is not covered by the fence, and `plan/` is inside the run-root the run must write. Its only guard is a rule the constrained party is asked to obey: *"a runner-authored `ABORTED.md` is **VOID**"* (`2-plan.md:183`). Three gaps:
1. No fence — the runner can physically write it.
2. **`plan/ABORTED-AUDIT.md` has no named producer.** `2-plan.md:75` specifies it only negatively (*"**NOT the runner**"*), where `AUDIT.md` at least names *"a single-purpose cold auditor"* (`:74`). A negative is not a producer, which is `PRD`'s own stated bar (`1-spec.md:36-38`).
3. **No enforcer.** `ABORTED.md`'s presence *ends the run* (`S-F6.4`: *"its presence ends the run with `assembled-plan.md` never written"*), so the voidness check has no live actor left to perform it.

`S-F6`'s own reason-gating (`1.5-criteria.md:165-166`) says *"without (4) the F6 fix installs a **dissolve-any-gate button** — a runner facing an unpassable gate could end the run cleanly instead of halting."* As specified, (4) does not remove that button.
**Fix:** put `plan/ABORTED.md` under the same fenced directory as `APPROVAL.md`; name the `ABORTED-AUDIT.md` producer (the same single-purpose cold auditor, dispatched by the *parent* loop or the next run's stage 8); and make the **restart walk** the enforcer — stage 8 must treat an `ABORTED.md` with no passing audit as absent and resume the run.

---

**F2-6 · MINOR · A parent's RES(a) rebind invalidates the parent-hash half of every descendant record, forcing full 6-agent re-runs across the subtree for a nitpick fix.**

D6 requires a record to be current on **both** hashes: `reviewed_context_sha256[<node>/plan.md] == plan_sha256` **and** `[<parent>/plan.md] == parent.plan_sha256` (`2-plan.md:136-138`). The rebind disjunct is scoped to *"`rebound_to == plan_sha256`"* — the node's own hash only (`:139-140`). A RES(a) minor fix-in-place at the parent changes `parent.plan_sha256`, so every child's 6 records go non-current on the parent half, with no rebind record available to them. `2-plan.md:165-166` confirms this is the intended treatment for a *seam* re-draft, but a RES(a) rebind is explicitly the case where *"a full re-pass"* is **not** required (`:224`). Result: a nitpick at the root re-runs every review in the tree — which materially contradicts the ECON economy the plan uses to justify induction (`:101-103`).
**Fix:** extend the rebind disjunct to the parent half (a child's record is current if the parent's `rebound_from` contains the recorded parent hash), or state that RES(a) is available only at leaves.

---

**F2-7 · MINOR · `S-C3` locks "exit-plan-mode is blocked by the same GBP predicate as assembly" as a gating criterion at four sites — declared in the spec, unmarked at the sites.**

`1.5-criteria.md:266-267` makes it gating that `XPM` at stages 5, 7, `SKILL.md`, `METHODOLOGY.md` states the terminus is GBP-gated. `1-spec.md:163-164` honestly declares this widens F8's migration surface, and `LOOP-STATE.md:72-75` records the same. But the criterion itself contains no forward marker, so an F8 "yes" would require reverting text a gating criterion asserts at four sites — the pre-shaping the charter's scope-fidelity item asks me to flag. The *declaration* is correct treatment; the *sites* carry no trace of it.
**Fix:** word the sites as "GBP-gated (this pass adds no human gate here; whether a human reviews the assembled plan is queued — see `decisions.md`)", so the criterion and the F8 queue are consistent.

---

# LENS 3 — MISSED OPPORTUNITY

**F3-1 · MINOR · The `S-` family's shared self-test already materializes the baseline tree; nothing uses it to prove the *positive* half is non-vacuous.**

`1.5-criteria.md:23-25` and `2-plan.md:337-338` establish the right instrument (*"every new-rule assertion must FAIL there; every preserved-rule assertion must PASS"*). But as F2-3 shows, an assertion can pass the baseline replay for the wrong reason (zero parsed input) or fail it for the wrong reason (a string that happens to be absent). The cheap addition, already paid for: a **mutation arm** — take the *post-change* tree, delete or reword each asserted claim one at a time, and require the corresponding subcommand to flag exactly that one. That converts the whole `S-` family from "can-fail somewhere" to "can-fail *on the thing it asserts*", which is what `S-PRD`, `S-C10` and `S-F7` each got wrong in a different way this pass.

**F3-2 · MINOR · `templates/seed/section-sets/`'s "non-spine-ness" is the load-bearing property and is the one thing no oracle checks.**

`S-F7.5` (`1.5-criteria.md:188-190`) requires the directory to exist *"with ≥2 **real non-spine** Layer-2 section lists"*. Existence and count are greppable; "real non-spine" is not, and it is the exact property whose absence caused pass 1's 3/3 DIV collapse (a declared default that *was* the spine). A mechanical bar is available for free: assert each shipped list's **intersection with the 7 spine section names is empty** and its length is ≥ 3. Without it, the fix's success is re-established by author judgment — the substitution class this whole change exists to close.

---

# LENS 4 — UNSTATED ASSUMPTIONS & RISKS (both conditional lenses fire)

## Concurrency — accessors and guard scope (ST2b)

**F4-1 · MAJOR · The `dispatch_seq` fencing token is an advisory read-modify-write with no atomic compare-and-swap; §4's "yes — covered" for `_status.md` is not earned.**

`2-plan.md:122-125`: *"`dispatch_seq` is a monotonic integer … the child stamps `owner_dispatch_seq` on every write, and **a write whose `owner_dispatch_seq` is lower than the value already in the file is DISCARDED** … This closes the 2/3-major 're-dispatch creates a second writer' finding **without a lock**."* `2-plan.md:364` scores `_status.md` **"yes"**.

There is no arbiter. The writers are LLM agents writing files; nothing *discards* anything. The rule can only be executed as: read the file, compare, refuse. That is a read-modify-write over shared mutable state with the other writer's window straddling it:

1. Superseded owner (seq 1) reads `_status.md`, sees `owner_dispatch_seq: 1`, concludes its write is admissible.
2. Re-dispatched owner (seq 2) writes the file.
3. Superseded owner writes — its check already passed. The seq-2 write is lost.

The guard's scope also excludes the case it is named for: the orphan is superseded *precisely because it is out of contact*, so it is the least likely accessor to re-read before writing. And the enumerated accessor set is incomplete for one key: D3 (`2-plan.md:110`) says *"**stage 5 / the parent** writes `killed`"* — if that means the child's own `subtree`, the **parent** writes a file `§1a` declares single-writer (*"writer: **that node's own owner, only**"*), carrying no `owner_dispatch_seq` of the child's owner at all, so the token cannot even be evaluated.
**Fix:** either (a) make the token real — the child's status is written to `_status.<seq>.md` and the reader takes the highest seq, which is append-only and needs no CAS; or (b) declare the residual honestly in `§4` ("advisory; a torn write is possible and is detected only at the next join poll") instead of scoring **yes**; and disambiguate D3's `killed` write to a single key in a single file.

**F4-2 · MINOR · `plan/topgate/AUDIT.md` is a second writer inside a directory the fence declares un-writable by the run** — the accessor-enumeration consequence of F2-4, listed here because `§4:367` scores `plan/topgate/APPROVAL.md` **"yes — runner fenced out"** without enumerating the auditor as an accessor of that directory.

## Position sensitivity (CP6)

**F4-3 · NO ISSUE FOUND — and it is earned.** I verified the assembly the 3/3 position finding named. `SKILL.md:15-41` (baseline) is a **three**-item numbered rule block whose closing rationale at `:39-41` enumerates exactly three things — *"The completeness lens, the two-pass discipline, and gate-before-present are stated here, up front … this rule block is load-bearing *before* the stage table"* — and `GBP` is item **3**, i.e. last. `S-SC3` (`1.5-criteria.md:354-361`) now asserts all three of the properties pass 1's line-offset proxy could not see: block-before-table, `PRV`/`DIV` **precede** `GBP` within the block (so `GBP` stays last), and the closing rationale must enumerate the block's new contents rather than the stale three. Its self-test includes *"a variant with GBP moved before PRV — both must fail"*. This is a genuine closure of the 3/3 major, with a real intra-block oracle.

## Other unstated assumptions

**F4-4 · MINOR · Five of the 14 new IDs are prefixes of the vocabulary the new text is about, in a corpus with a demonstrated ALL-CAPS emphasis habit — and the "collision-clean" claim was verified against the wrong corpus.**

`1.5-criteria.md:29` calls the set *"**post-collision-check**, `oracles/idcollide.sh` clean"*. I confirmed it **is** clean at baseline: none of `PRD JOIN SEAM BIND KLB PRV DIV IDN RES CNC CTX XPM IGM DEP` is a substring of any of the 56 uppercase tokens at `3771038`, none collides with the 21 baseline IDs, none collides with the sibling skills' namespaces (`Guarded_change/`, `Dragonfly/`, `Data-Distiller/`, `guarded-change.architect.md`). The one hit, `JOIN` in `Dragonfly/changes/.../hammer.py`, is a SQL keyword in another skill's Python file — not a namespace collision.

But `idcollide.sh` runs on the **edited** corpus, and the baseline habit is live: `DECOMPOSE`, `DECOMPOSES`, `PROVEN`, `DROPPED`, `ADDED`, `NEITHER`, `HARDSTOP`, `TOP-LEVEL` are all ALL-CAPS emphasis in the existing text (and `DEC ⊂ DECOMPOSE` already breaks an existing ID — see F1-3). The pass-2 artifacts' own prose already contains **`DISJOINT`**, and `S-F7.4` mandates that the skill name *"three frames per pass with **DISJOINT MANDATES AND DISJOINT INPUT SETS**"* — `JOIN ⊂ DISJOINT`. Similarly at risk: `SEAM ⊂ SEAMS`, `BIND ⊂ BINDS/BINDING`, `RES ⊂ RESOLVED/RESTART`, `DIV ⊂ DIVERSITY`, `DEP ⊂ DEPENDENCY/DEPTH` — all words this change's own text uses constantly, three of them inside criteria that capitalize their key terms.

No resolution rule is stated for a collision found at build time (rename the ID across ~7 sites, or de-capitalize the emphasis word?). Given pass 1 shipped two violations under a stated convention, "the instrument will catch it" needs the follow-through named.
**Fix:** state the resolution rule (**de-capitalize the emphasis word; never rename a shipped ID**) and add the emphasis-token exclusion list to `idcollide.sh` per F1-3.

**F4-5 · MINOR · `IDN`'s "declared degraded" escape is self-declared, with no justification requirement — in a harness this run proves exposes the id.**

`2-plan.md:215-217`: *"if the harness exposes **no** dispatcher id at all the pass is **declared degraded in the record** — never un-run."* Correct as a fix for B/L-11. But the declaration is made by the party the audit constrains, with no requirement to name the limitation, and `3-redteam-plan.md:8-10` shows this very harness *did* yield three distinct dispatcher-recorded ids (`a1cb9e6c3aa124a3f`, `ad7de94dda62399b4`, `a9f343344368cc2f7`). So a runner can retire the entire `F9` audit surface with one sentence.
**Fix:** require a degraded declaration to name the harness and the attempted retrieval, and to be logged as a finding at the gate (not merely noted) — so the escape leaves a trace the next cycle's carry-forward reads.

**F4-6 · UNVERIFIABLE — FLAGGED.** Three claims I could not check against any source in the closed set, all load-bearing:
1. Whether a **"durable locus in the owner's own exchange that the runner did not author and that the auditor can independently fetch"** exists in this runtime at all (see F5-1). `LOOP-STATE.md:17-19` says a decomposing self-review *would* block on it, which is evidence against.
2. Whether `templates/seed/section-sets/` will contain genuinely non-spine lists (build-time; see F3-2).
3. Whether 16 X-arms (`2-plan.md:390`) are runnable within the session budget that killed the dogfood at ~21:25 (`FINDINGS.md:170-171`).

---

# LENS 5 — FIDELITY (the owner's mechanism, or a convenient proxy?)

Loaded operational terms in the spec/request, each pinned to a concrete mechanism from owner intent, and whether the artifact implements *that*:

| Term | Pinned mechanism (from owner intent / `FINDINGS.md` / prior art) | Implemented, or proxied? |
|---|---|---|
| **"human gate"** (`plan/topgate/`) | `FINDINGS.md:77-78`: no pre-creation · deterministic filename · owner-verbatim content + durable source · runner may not author its own approval | **Mechanism, with a fidelity defect** — see F5-1 and F2-4 |
| **"resolved"** | `FINDINGS.md:112-114`: not an unreviewed author edit; distinguishable at assembly | **Mechanism.** D11 (`2-plan.md:223-235`) moves satisfaction off the author via a single-purpose cold rebind check, and `gate` carries three distinct values |
| **"independent" (3 cold agents)** | `FINDINGS.md:92-96`: not decontamination alone — **blind-spot diversity** | **Mechanism, with one mis-bucketed clause** — see F5-2 |
| **"proven"** | `FINDINGS.md:187-189`: soften to what is *actually* proven | **Mechanism.** `D14` labels four strength buckets and names three NOT-established claims, incl. *"a negative no finite review can prove"* |
| **"fix that"** (owner directive, `LOOP-STATE.md:4-5`) | the confirmed finding set, stated as an **Interpretation Roy can correct** | **Mechanism, and the pass-1 inflation is repaired** — see RATIFICATION AUDIT |
| **"until nothing surfaces"** | `LOOP-STATE.md:57-63`: a *continue* trigger only, never an early-terminate licence | **Carried verbatim** at `1-spec.md:190-191` |
| **"3 independent cold agents" audit surface** | `FINDINGS.md:110`: a spawn-identity field | **Mechanism** (dispatcher-recorded), with a self-declared escape — F4-5 |
| **"escalate"** | `FINDINGS.md:39-40`: RAT3's relay travels over a channel a stage must define | **Proxied** — the channel is declared but the relay's *write* is unassigned (F2-2) and the state has no exit (F2-1) |

**F5-1 · MAJOR · D9's "fetchable locus" silently inflates the `RAT1` model it claims to copy, drops `RAT1`'s enumeration of acceptable loci, and has no degraded fallback — the mirror of the blocker pass 2 just fixed.**

`1-spec.md:196-199` claims the prior art is *"**RAT1**'s ratification record … + **a durable source the author did not author** + a mapping … **including the clause pass 1 dropped**"*. I read the source. `Guarded_change/stages/stage-3.md:89-95` says:

> *"the owner's response (verbatim, **with a durable source the author did not author — a chat-transcript line (acceptable even for a just-made live ruling) or a timestamped, owner-attributed `decisions.md` entry — so the quote is spot-checkable**)"*

Two departures the plan does not declare:
1. **`RAT1` enumerates acceptable loci; D9 does not.** `RAT1` explicitly blesses *"a timestamped, owner-attributed `decisions.md` entry"* — a file inside the run. D9 requires *"a durable locus in the owner's own exchange **that the runner did not author** and that the auditor can **independently fetch**"* (`2-plan.md:198-200`, `:206-207`), which **excludes** the one locus `RAT1` names as sufficient.
2. **`RAT1` requires spot-checkability; D9 requires the auditor to *fetch*.** `RAT1`'s bar is *"so the quote is spot-checkable"*; D9 escalates to *"a single-purpose cold auditor **fetches the cited locus**, confirms the quote appears there"*.

That is unratified inflation of the prior-art model (RAT2 shape), and it has a mechanical consequence: with no enumeration of qualifying loci and no degraded fallback, *"one **without** [a real fetchable owner locus] is **VOID**, and dispatch stays blocked"* (`2-plan.md:200-201`) makes the topgate potentially unsatisfiable in the real harness — every decomposing run permanently blocked. `LOOP-STATE.md:17-19` records the authors' own workaround: *"The hardened topgate requires owner-verbatim approval before any split, so a decomposing self-review would block on a sleeping owner"* — they route around it by running single-node. The skill ships the predicate to all users. This is the **same shape as B/L-11** (a rule whose unavailable surface makes gating impossible), which pass 2 correctly fixed *for `IDN`* by adding a declared-degraded fallback and did not fix here.
The only verification is `X3`'s intact arm (`1.5-criteria.md:404`), whose *"fetchable locus"* is invented by the fixture author — so the representativeness of the one real human gate rests on a fabricated artifact.
**Fix:** carry `RAT1`'s enumeration verbatim (transcript line **or** timestamped owner-attributed `decisions.md` entry), declare the fetch-requirement as a **deliberate strengthening** rather than a copy, and state a fallback for "no fetchable locus exists in this harness" that is a **HALT + relay**, not a permanent block.

**F5-2 · MINOR · `PRV`'s "checked to the extent the surface exists" bucket attributes "no shared context" to evidence that does not support it — the F7 defect one level up, in the F7 fix.**

`2-plan.md:280-282`: *"**Checked to the extent the surface exists:** the reviewers **had no shared context** and **disjoint frames** — evidenced by distinct dispatcher-recorded ids and differing embedded prompts."*

Distinct dispatcher ids evidence *distinct agents*. Differing embedded prompts evidence *differing frames*. Neither evidences **no shared context** — that rests on the closed input set and the sibling-read ban, both **asserted by the dispatcher**, i.e. by the party the gate constrains. `PRV`'s own honest bucket for that is *"Attested only"* (`:284`). So one clause is in the wrong bucket, in the sentence whose whole purpose is bucketing by strength. The rest of `D14` is accurate and the NOT-established list is genuinely strong (`:286-289`), which is why this is minor rather than a repeat of F7.
**Fix:** move *"no shared context"* to **Attested** (or to **Mechanically checked** with a real oracle: the record's `reviewed_context_sha256{}` map must contain no path under the node's own `completeness/`+`adversarial/` — that *is* checkable and the map already exists).

**F5-3 · Scope fidelity, checked and clean on three of the charter's four sub-tests.** (a) Nothing implements F8; `1.5-criteria.md:421-422` declines to write a criterion for it *deliberately*, and both widening surfaces are declared at `1-spec.md:162-164` and mirrored in `LOOP-STATE.md:72-75`. My one residue is F2-7 (declared in the spec, unmarked at the sites). (b) No fix adds a human gate: every new stop routes to *HALT + verbatim relay* under RAT3 (`2-plan.md:374-378`), and `1-spec.md:185` states the constraint. (c) I checked every "the finding says" claim against `FINDINGS.md` and found **no** claim it does not support; the `§4`-heading count differs from `FINDINGS.md:141` ("3–4 ways") but that is a *measurement correcting the finding*, which is legitimate — the defect is internal to `S-C10` (F1-5), not a misquote. (d) No Tier-3 item is silently dropped — `D15` (`2-plan.md:294-327`) covers `CNC DEC XPM IGM DEP CTX TPL3 SPN RST`, the index rows and the two ID renames; the *"two passes aren't cost-justified"* item is correctly re-filed to `FINDINGS.md`'s **Triaged NOT genuine** section with pass 1's misfiling named as an error (`1-spec.md:166-168`) — a fidelity improvement, not a drop.

---

# COVERAGE CHALLENGE (CH8)

Behaviours this change could plausibly alter that **no criterion observes**:

**CC-1 · MAJOR · No criterion observes that a clean tree actually *terminates*.** Every criterion in Part B/C asserts the presence of a predicate; `X1`'s intact arm asserts *"all children terminal + kill handled + `_assembled.md` present ⇒ subtree-complete ⇒ assemble"* — it hands the agent a tree in which the terminal statuses are **already written**. No arm requires an agent to *walk a node from stage 6 through stage 7 and produce the terminal status itself*. That is exactly why F1-1's producer/trigger inversion is invisible to the criteria set: the fixtures pre-supply the fact whose producer is broken. Baseline `stage-7:33-35` explicitly asserts *"A fully-covered clean tree assembles… the gate blocks holes, not progress"* — this change touches every predicate in that sentence and no criterion re-establishes it.
**Scenario:** root + one leaf, both gated clean, nothing pre-written. Nobody writes `subtree: complete`; the join declares the leaf dead; CAP escalates. Every criterion passes.
**Fix:** add an `X9` "smallest live tree" arm whose fixture contains *only* gated-clean nodes with **no** terminal statuses and **no** `_assembled.md`, and whose required verdict is the ordered sequence of writes that reaches `assembled-plan.md`.

**CC-2 · MAJOR · No criterion observes the *exit* from `escalated`.** `X1`'s holed arm requires *"escalated child ⇒ **NOT dead, relay upward**"* — it tests the entry and the precedence rule (correctly, closing B/L-2). Nothing tests the state *after* the relay is answered. F2-1's permanent block is unobserved.
**Fix:** extend `X1`'s intact twin with a node whose escalation was answered, requiring the verdict "re-dispatch with an incremented `dispatch_seq`; the subtree then completes".

**CC-3 · MINOR · No criterion observes the fencing token under interleaving.** `S-F1.7` asserts the rule is *stated*; `§4:364` scores it covered. No arm presents an agent with a `_status.md` whose `owner_dispatch_seq` moved *between* its read and its write (F4-1). Grep-presence of a rule about a race is the purest proxy in the set.
**Fix:** an arm where the fixture's `_status.md` shows `owner_dispatch_seq: 2` while the agent is told it is owner seq 1 mid-write; required verdict: "my write is void; I am superseded; stop".

**CC-4 · MINOR · No criterion observes the *cost* of a parent rebind** (F2-6) — the number of records invalidated by a RES(a) at a non-leaf is unmeasured, and `X5` uses a single node with no children.

**CC-5 · MINOR · No criterion observes the baseline IDs' operative-claim consistency.** `S-SC2` asserts it for all 21 but oracles it only for the 15 (14) new ones (`1.5-criteria.md:344-349`); this is the gap through which F1-6's P7 half-migration passes.

---

# LABEL AUDIT (CH9 / CH10)

There are **no advisory criteria** — all 36 (`S-PRD`; `S-F1,2,3,4,5,6,7,9,10`; `S-C1…C10`; `S-SC1…SC5`; `R1,R2`; `X1…X8`) are labelled **gating** (`1.5-criteria.md` passim; `:411` *"Reason all gating"*). So the "advisory as a dodge" challenge is moot. The live loophole is the **non-verification route**, and it does not survive challenge:

**LA-1 · MAJOR · The only reachable route for an unverified gating criterion is a *self-granted* "declared deferral", where the plan's own RAT3 prescribes HALT + relay.**
`2-plan.md:375-378`: *"a criterion that cannot be verified is `verified = no` and takes either a **named risk-acceptance** (unavailable under RAT3 with the owner asleep — so in practice) a **declared deferral**"* (sentence is garbled — nitpick), and `1.5-criteria.md:415-417` makes it explicit: *"under RAT3 with the owner asleep, **no one present can grant a named risk-acceptance**, so the only reachable route is a **declared deferral**."* Pass 1's reviewers raised the missing-authority problem 3/3; pass 2 answers it by **converting** the unavailable external authority into a waiver the runner grants itself. That leaves all 36 gating criteria deferrable by the party they constrain — the F5/F9 defect class, inside the criteria's own gating story. The plan's own rule for a case needing an authority nobody present holds is *"HALT + verbatim relay"* (`:374`, `:378`).
**Fix:** make a `verified = no` on any **Tier-1** criterion a HALT + relay, and restrict declared deferrals to Tier-3 with an explicit cap ("at most N deferrals; the N+1th halts").

**Per gating criterion — the governed path each would exercise, and the evidence I checked.** Grouped; every one whose verification I could not substantiate is named:

| Criterion | Governed path | Would the planned verification exercise it? | Evidence I checked |
|---|---|---|---|
| `S-PRD` | a gate reading a fact with a named producer | **NO — proxy.** Mention-check; 7/14 sampled pairs pass at baseline; self-test has zero input | ran the pair test against `3771038` stage files (F2-3) |
| `S-F1` | the join, live | **PARTLY.** Sub-parts 4/5/6/7 are text assertions; `X1` supplies the terminal facts rather than requiring their production | `X1` fixture spec `1.5-criteria.md:402`; F1-1, CC-1 |
| `S-F2` | reopen + cross-node seam check | **PARTLY.** `X4`'s holed arm pre-sets unequal hashes, so it never exercises what `declared_seam_sha256` *contains* | `1.5-criteria.md:405`; F1-2 |
| `S-F3` | record↔plan binding | **YES.** `X2` gives an agent 6 stale records and no rebind record; the discriminator is on disk | `1.5-criteria.md:403`, `2-plan.md:136-143` |
| `S-F4` | config contract read | **YES, and the column-0 form is *required* for non-vacuity.** Verified: `redteam_context` occurs **0×** in baseline `METHODOLOGY.md`; the example's only occurrence is inside `off_limits_paths` at `planning.md:40`, so a naive substring oracle would indeed pass at baseline; the contract YAML's top-level keys **are** at column 0 (`METHODOLOGY.md:67-93`) | ran both greps |
| `S-F5` | the one real human gate | **PARTLY — representativeness unearned.** `X3`'s "fetchable locus" is invented by the fixture author; F2-4's fence contradiction makes two sub-parts mutually unsatisfiable | `1.5-criteria.md:404`; F2-4, F5-1 |
| `S-F6` | killed branch + abort | **PARTLY.** The kill half is exercised by `X1`; the **abort** half (the dissolve-any-gate button, the stated reason it is gating) is exercised by **no arm** | `1.5-criteria.md:402-409`; F2-5 |
| `S-F7` | claim strength + frame diversity | **YES for the sweep** (paired, normalized, plus a bold/line-wrap fragility test) — but the self-test number is wrong (F1-4) and "non-spine" is unoracled (F3-2) |ran the overclaim sweep |
| `S-F9` | audit surface | **YES.** `X6` runs both the collapse case and the honest-"unavailable" case | `1.5-criteria.md:407` |
| `S-F10` | "resolved" | **YES.** `X5` discriminates on the presence of a rebind audit + finding ID | `1.5-criteria.md:406` |
| `S-C1` | shared-write surfaces | **PARTLY.** All four baseline `index.md` writers are correctly enumerated — I verified `stage-1:20`, `stage-6:11-12`, `METHODOLOGY:195`, `templates/seed/README:14` all exist. The fencing token is text-only (CC-3) |ran the greps |
| `S-C2` | DEC | **YES.** `X8` runs both a tripping and a non-tripping ladder |`1.5-criteria.md:409` |
| `S-C3` | exit-plan-mode terminus | **text-only, and defensibly so** — the terminus is a rule read at the moment of presenting; but see F2-7 | — |
| `S-C4` | ingest mode | **YES.** `X7(ii)` requires an agent to detect an invented unmarked §4 |`1.5-criteria.md:408` |
| `S-C5` | seed skeleton slots | **YES, direct — instantiation copies the text.** Self-test verified: **3 of 3** skeletons fail. `generic-node.md:32-33` has only the italic note, no heading; `decomposition-node.md` and `leaf-task-spec.md` have neither. `B0.8`'s `:32-34`→`:32-33` correction is right (the file is 33 lines) | read all three files |
| `S-C6` | spot-verify duty | **YES.** `X7(i)` requires an agent to reject a citation-free "spot-verify ok" |`1.5-criteria.md:408` |
| `S-C7`,`S-C8`,`S-C9` | TPL3 / DEP / root pin | **text-only; legitimate** — each is a rule stated at the sites a runner reads. `S-C9`'s departure is declared (see RATIFICATION AUDIT) | verified `plans:173` |
| `S-C10` | §4 heading | **NO as written** — the pinned predicate excludes the two sites that generate its own number (F1-5) |ran the extraction |
| `S-SC1`,`S-SC5` | package validity + trigger | **YES.** Both have real can-fail self-tests; `S-SC5` is new this pass and closes a real gap (the description is the trigger surface) | — |
| `S-SC2` | cross-file consistency | **PARTLY.** `idcollide` cannot pass as specified (F1-3); baseline-ID operative claims unoracled (CC-5) |ran idcollide over the 18 index IDs |
| `S-SC3` | intra-block order | **YES — earned.** See F4-3 | read `SKILL.md:15-41` |
| `S-SC4` | live-copy sync | **YES.** Direction asserted, diff shown non-empty before and empty after | — |
| `R1` | site-set non-erosion | **YES — and it can now pass its own baseline replay.** See the closure list | re-ran the full site map |
| `R2` | deliberate-change completeness | **PARTLY.** The list omits P7 (F1-6) | ran the `stage-done` greps |
| `X1…X8` | the behavioural halves | **YES in protocol** — separately spawned, holed+intact, *"Both arms the same verdict ⇒ `verified = no`"* (`1.5-criteria.md:398`), output form pinned (`2-plan.md:353-357`). The weakness is fixture *content*, not protocol: CC-1/CC-2/CC-3 | read the whole table |

---

# RATIFICATION AUDIT (CH11 / CH12)

**No recorded "OWNER RULING" is relied on for any design decision in this spec/criteria/plan, and I checked.** The only owner text in the closed set is the two verbatim directives in `LOOP-STATE.md`:

- `LOOP-STATE.md:4-5` (2026-07-24 ~22:45 EDT): *"Alright, run it through guarded change to fix that, then have it run against its self again, repeat the loop three times or until nothing surfaces (whichever happens first)."*
- `LOOP-STATE.md:24-25` (~22:55 EDT): the autonomous-restart authorization, explicitly scoped — *"This authorization covers restarting runners only — it does **not** extend to answering any queued owner question below."*

`LOOP-STATE.md:16` labels the orchestrator calls **"NOT owner questions"**, and I treated them accordingly.

**RA-1 — The pass-1 RAT2 inflation is genuinely repaired.** `LOOP-STATE.md:64-67` recorded the finding: *"`1-spec.md` inflated the scope label. This file honestly calls the broad reading an *'Interpretation … stated so Roy can correct it'*; the cycle-1 spec dropped that hedge and called it *'the approved cycle-1 scope.'* That is an unratified inflation (RAT2 shape)."* Pass 2's spec carries it: `1-spec.md:188-190` — *"`LOOP-STATE.md` labels the broad scope reading an **'Interpretation … stated so Roy can correct it'** — this spec **carries that hedge** and no longer calls it 'the approved cycle-1 scope'."* Mapping confirmed: the hedge is reproduced, the inflated label is gone. I grepped: the string "approved cycle-1 scope" does not appear in `1-spec.md`. **Closed.**

**RA-2 — The "until nothing surfaces" narrowing is carried correctly.** `LOOP-STATE.md:57-63` restricts the narrowing to a *continue* trigger. `1-spec.md:190-191`: *"'no new blocker or major' is a **continue** trigger only, never a licence to terminate the loop; the owner said *'until nothing surfaces'*."* Verbatim phrase matches `LOOP-STATE.md:5`. **Closed.**

**RA-3 — The one *unaudited* owner ruling in the corpus is correctly quarantined, not leaned on.** `FINDINGS.md:157-159` treats *"two passes aren't cost-justified"* as half-settled by an owner ruling. `1-spec.md:166-168` puts it out of scope **and** flags its provenance: *"its status as an **unaudited owner ruling with no re-ask path** has been queued with the orchestrator, not decided here"* — matching `LOOP-STATE.md:70-71`. This is the correct RAT1 treatment (queue and re-ask, do not build on it). **Closed.**

**RA-4 · MINOR · One owner-approved layout departure is declared; a second is not.** `B0.8` (`0-baseline.md:189-194`) declares the `tree/root/` move and cites `/home/zero/.claude/plans/1-this-is-a-proud-scott.md:173`. **I spot-verified that line exactly:** `173:│   ├─ _status.md       ← apex roll-up (the top orchestrator's lean surface)`. The citation is precise and the declaration is honest.

But the same approved layout shows `plan/topgate/` as a component of the run tree at `:171` — *"topgate/ ← the human top-level-decomposition approval artifact (dispatch blocked until it exists)"* — and D9 now both forbids the runner to create it (`2-plan.md:188`) and puts it in `off_limits_paths` (`:189-190`). Removing a directory from the run's own output layout is a second change to an owner-approved on-disk layout. It is **well-justified** (it is `FINDINGS.md:77`'s fix, and `:171`'s "blocked until it exists" is precisely the predicate the pre-creation defeated), so this is not a fidelity violation — it is an **undeclared** one, where the pass declared its sibling.
**Fix:** add the `plan/topgate/` non-creation to `B0.8`'s departure list with the same one-line justification.

**No elaboration inflation found in RA-1/RA-2/RA-3.** The one inflation I did find is against **prior art**, not an owner ruling, and is filed as F5-1: D9's *"independently fetch"* requirement and its silent dropping of `RAT1`'s enumerated loci (`Guarded_change/stages/stage-3.md:89-95`) are operative commitments not present in or entailed by the model the spec claims to copy.

---

# CARRIED-FORWARD FINDINGS THAT ARE **GENUINELY CLOSED** (mechanism cited)

Stated explicitly per the charter, because a real closure is as valuable as a finding.

**The five pass-1 blockers:**

| Blocker | Verdict | Closing mechanism |
|---|---|---|
| **B/L-1** — no terminal `subtree: complete` producer | **NOT CLOSED** — producers are named but the trigger sits in a later stage than the writer ⇒ deadlock survives. See **F1-1 (blocker)** |
| **B/L-2** — escalation ≡ death | **CLOSED.** Three independent mechanisms: `subtree` becomes **four**-valued with `escalated` **terminal** (`2-plan.md:88`); the dead test is conditioned on *"its `subtree` is **non-terminal**"* (`:115-116`), so an escalated child cannot satisfy it; and an explicit precedence sentence is stated **first**: *"a status carrying `escalation:` is NEVER dead"* (`:113`). `S-F1.5`/`S-F1.6` assert all of it and `X1` exercises it. *(Residual: the state has no exit — F2-1, a new defect, not a survival of B/L-2.)* |
| **B/L-3** — SEAM's reopen detector uncomputable | **RE-WORDED; DEFECT SURVIVES.** See **F1-2 (major)** |
| **B/L-11** — `spawn_id` self-reported + unconditional un-run bricks every gate | **CLOSED.** `spawn_id` is redefined as *"the identifier the **dispatcher** observed at spawn"* (`2-plan.md:211`), `self_reported_identity` becomes a separate optional field, the un-run rule keys **only** off dispatcher ids, and the bricking case gets a fallback: *"no dispatcher id at all ⇒ the pass is **declared degraded** … never un-run"* (`:215-217`). `S-F9.2/9.3` assert it; `X6`'s second variant tests exactly the live case (3 "unavailable" self-reports with distinct dispatcher ids ⇒ **valid**). *(Residual: the escape is self-declared — F4-5, minor.)* |
| **C/L-1** — D2/BIND ⊥ RES(a); X2/X7 opposite verdicts | **CLOSED.** BIND becomes a **single** disjunctive rule: current iff the reported hash equals `plan_sha256` **or** *"the node carries a **valid RES(a) rebind record** whose `rebound_from` contains the record's value and whose `rebound_to == plan_sha256`"* (`2-plan.md:138-141`), with records **immutable** so the discriminator is the rebind record's presence, not the hash (`:142-143`). `S-F10.3` states it as one rule. And the fixtures now agree: `X2`'s holed arm carries the qualifier *"**no** rebind record"* (`1.5-criteria.md:403`) while `X5`'s intact arm supplies one (`:406`) — **one verdict per disk state**. |

**Convergent findings, in the ranked order given:**

1. **DIV collapses into frame A (3/3 major) — CLOSED.** `D13` gives frame B a **priority-ordered source list** (config `differential_section_sets` → another plan-type's `required_sections` → the **new** `templates/seed/section-sets/`) and, critically, an honest floor: *"**If no non-spine list is obtainable, frame B is DECLARED DEGRADED … never silently the spine**"* (`2-plan.md:253-259`). Frame C's input becomes *"the node's plan **ONLY**"* — a genuinely disjoint input set — and the two prohibitions are explicit. `S-F7.5` asserts it. *(Residual: "non-spine" is unoracled — F3-2, minor.)*
2. **The baseline site map is wrong (3/3 major) — CLOSED, and I re-ran it.** I recaptured `grep -rlw -- <ID>` over `SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/` at `3771038` for all 21 IDs. **`B0.6`'s table reproduces exactly, row for row, all 21.** The phantom claims are all confirmed: `grep -nw -- TOP stages/stage-8-restart-resume.md` → **zero hits** (the only match is `HARDSTOP` at `stage-8:20`); the two `ON TOP OF` hits exist exactly where claimed, at `METHODOLOGY.md:79` and `examples/authoring-a-skill/planning.md:25`, and both **do** survive `grep -w`. `TPL1`/`TPL2`/`SEV` are real, live, multi-site IDs (`TPL1`: METHODOLOGY + stages 1,2 + seed/README; `TPL2`: METHODOLOGY + stages 1,6 + seed/README; `SEV`: stages 4,5) and confirmed **absent** from `METHODOLOGY.md`'s cross-file index (18 rows at `:315-333`). **"21 baseline IDs" is right and complete:** I enumerated every ALL-CAPS token appearing in ≥2 corpus files and found no further mnemonic rule ID — the only near-miss is `HARDSTOP` (4 files, 6 hits), which is a term *inside* `RST`'s operative claim (`METHODOLOGY:332`), not a separate cross-file rule ID. **`R1` can now pass its own baseline replay** — the reference table is accurate, which is the exact defect that made pass 1's `R1` `verified = no`.
3. **Position / GBP displacement (3/3 major) — CLOSED.** See **F4-3**.
4. **§4 heading count + undefined extractor (3/3 minor) — PARTLY CLOSED.** The extractor is now pinned, which was the substance of the finding; the count and the predicate no longer agree — **F1-5**.
5. **"Named risk-acceptance" unavailable under RAT3 (3/3 minor) — ANSWERED, BUT THE ANSWER OPENS A LOOPHOLE.** `1.5-criteria.md:415-417` states it up front rather than improvising at stage 8 — correct treatment of the finding; the substitute route is self-granted — **LA-1**.
6. **`PRV`'s positive half is itself an overclaim (2/3 major) — SUBSTANTIALLY CLOSED.** Four strength buckets, and a NOT-established list that names *"a **negative** no finite review can prove"*, *"**N same-model instances are not N independent minds** — decontamination removes shared *context*, not shared *priors*"*, and *"an un-spot-checked citation is real"*, closing with *"The gate raises the cost of shipping a hole. It does not certify its absence."* (`2-plan.md:276-289`). One clause is mis-bucketed — **F5-2**.
7. **Dead-child re-dispatch = a second writer (2/3 major) — ADDRESSED IN DESIGN, NOT IN MECHANISM.** The fencing token is the right shape; it has no arbiter — **F4-1**.
8. **BIND does not cover the gate artifacts (2/3 major) — CLOSED.** `APPROVAL.md` carries `approved_root_plan_sha256` + `approved_root_seam_sha256`, `AUDIT.md` carries `audited_approval_sha256`, and *"A post-approval change to the root's split therefore **re-fires the existing human gate** (not a new one)"* (`2-plan.md:146-150`) — which also keeps `1-spec.md:185`'s "no new human gate" true. `S-F3.5` asserts it; `X2`'s holed arm tests it (*"a root whose split was re-drafted after `APPROVAL.md`"*).
9. **The closed set omitted the approved-scope record (2/3 major) — CLOSED.** It is now item **7** of the closed set (`3-charter-given.md:49-55`) with the reason stated, and `1-spec.md:228-231` records the addition. The departure it exposed is declared at `0-baseline.md:189-194` with a citation I verified exactly (**RA-4**).
10. **`elc` is self-declared while `S-C2` called it "computable" (2/3 major) — CLOSED.** `D15` labels it *"a **self-declared** integer (labelled honestly as such, **not** 'computable')"* with the honest consequence stated: *"**DEC detects a decomposition its own owner does not believe is reducing; it cannot detect a mis-estimate**"* (`2-plan.md:303-307`). `S-C2`'s title becomes *"HONESTLY LABELLED"* and it forbids the word "computable" (`1.5-criteria.md:253-256`).
11. **The schema omits `template` + the granularity call (2/3 minor) — CLOSED.** Both are rows in `§1a` (`2-plan.md:36-37`) with producers and readers.
12. **`TPL1`/`TPL2`/`SEV` outside both regression criteria (2/3 minor) — CLOSED.** All three are in `B0.6`, the count is corrected to 21, `S-SC2` covers them and requires they *gain* index rows, and `R1` runs over all 21.

**Also verified accurate this pass:** `S-C5`'s "3 of 3" (read all three skeletons); `S-F4`'s column-0 form and its non-vacuity argument (ran both greps); `B0.8`'s `_status` count of 13 under the bare predicate; `B0.8`'s `plans:173` citation; and the four `index.md` writers in `§4`. **No fabricated citation found anywhere in the pass-2 artifacts** — every file:line I sampled exists and says what is claimed. The inaccuracies are all *counting/predicate* errors (F1-4, F1-5, F1-7, F1-8), not invented sources.

---

# RANKED SUMMARY

| # | ID | Sev | Claim |
|---|---|---|---|
| 1 | **F1-1** | **BLOCKER** | D2(b)+D3 assign the terminal-status write to stages 6/6.5 but trigger it on a **stage-7** output ⇒ no node can ever write `subtree: complete`; **B/L-1 re-opened**, and self-deadlocking at the root |
| 2 | F1-2 | major | `children.<c>.declared_seam_sha256` has no defined content at its stage-2 initial write; the two hashed objects are different documents ⇒ the reopen detector is vacuous or always-firing. **B/L-3 re-worded, not closed** |
| 3 | F2-3 | major | `S-PRD`'s oracle is a **mention**-check (7/14 sampled pairs pass at baseline; cannot distinguish read from write) and its self-test is a zero-input vacuous pass — in the pass's own organizing criterion |
| 4 | F1-3 | major | `idcollide.sh` as specified flags **4 baseline IDs** (`CMP⊂CMP2`, `TOP⊂HARDSTOP/TOP-LEVEL`, `DEC⊂DECOMPOSE(S)`, `TPL⊂TPL1/2/3`); `B0.7`'s "flags nothing at baseline" is false; gating `S-SC2` cannot pass without an unspecified exemption |
| 5 | F2-4 | major | `off_limits_paths` fences `plan/topgate/` while D9 admits an orchestrator-transcriber and `§1b` puts `AUDIT.md` inside it; "the runner" vs "an orchestrator" is never pinned — the actor that executed the live F5 defeat |
| 6 | F2-1 | major | `subtree: escalated` is an **absorbing state with no exit producer** (never re-dispatched, terminal, and `resolved` has no writer) ⇒ assembly blocks permanently after any escalation |
| 7 | F5-1 | major | D9 silently inflates the `RAT1` model it claims to copy (adds auditor-**fetch**, drops RAT1's enumerated loci incl. the owner-attributed `decisions.md` entry) and has **no degraded fallback** ⇒ the topgate may be unsatisfiable in the real harness |
| 8 | F2-5 | major | `plan/ABORTED.md` is **not fenced**, `ABORTED-AUDIT.md` has **no named producer**, and the VOID rule has no enforcer after the run ends — the dissolve-any-gate button `S-F6` exists to prevent |
| 9 | F4-1 | major | the `dispatch_seq` fencing token is an advisory read-modify-write with **no atomic CAS**; `§4` scores `_status.md` "yes — covered" |
| 10 | LA-1 | major | all 36 criteria are gating and the only reachable non-verification route is a **self-granted** "declared deferral", where the plan's own RAT3 prescribes HALT + relay |
| 11 | F2-2 | major | the **relay** of an escalation has no producer (only stage 5 may write `escalation:`; the relay happens at the parent's 6.5) |
| 12 | CC-1 | major | *(coverage)* no criterion observes that a clean tree **terminates** — every fixture pre-supplies the terminal facts whose producers are broken |
| 13 | CC-2 | major | *(coverage)* no criterion observes the **exit** from `escalated` |
| 14 | F1-5 | minor | `S-C10`'s pinned predicate excludes the two prose sites that generate its own "6"; under the predicate the count is 5 and those two sites survive a passing criterion |
| 15 | F1-6 | minor | `R2`'s authoritative list omits **P7** (stage-done = output-exists, 4 sites + the RST index row), which D6 explicitly amends; `S-F3.4` names only `stage-8` |
| 16 | F1-4 | minor | `S-F7`'s self-test "8 occurrences across **5** files" — 8 is right, the file count is **4** |
| 17 | F4-4 | minor | 5 of 14 new IDs are prefixes of the new text's own vocabulary (`JOIN ⊂ DISJOINT` is already live in `S-F7.4`'s mandated wording); the "collision-clean" claim was verified against the **baseline** corpus, and no resolution rule is stated |
| 18 | F2-6 | minor | a parent RES(a) rebind invalidates the parent-hash half of every descendant record ⇒ full 6-agent re-runs across the subtree for a nitpick fix |
| 19 | F5-2 | minor | `PRV` attributes *"no shared context"* to evidence (distinct ids, differing prompts) that does not support it — belongs in "attested" |
| 20 | F1-7 | minor | "15 with `PRD`" is **14**; propagated into `S-SC2` and `§6` |
| 21 | F4-5 | minor | `IDN`'s "declared degraded" escape is self-declared with no justification requirement, in a harness this run proves exposes the id |
| 22 | F2-7 | minor | `S-C3` locks "GBP-gated only" at 4 sites as a gating criterion — declared in the spec, unmarked at the sites (F8 pre-shaping) |
| 23 | RA-4 | minor | a **second** owner-approved-layout departure (`plan/topgate/` no longer run-created) is undeclared where its sibling is declared |
| 24 | F3-1 | minor | *(missed opp.)* the baseline-replay instrument is already built; a per-assertion **mutation arm** would convert the whole `S-` family from "can-fail somewhere" to "can-fail on what it asserts" |
| 25 | F3-2 | minor | *(missed opp.)* `section-sets/`'s **non-spine-ness** is the load-bearing property and the one thing no oracle checks — a spine-intersection assertion is free |
| 26 | CC-3 | minor | *(coverage)* the fencing token is verified by grep-presence of a rule about a race |
| 27 | CC-4 | minor | *(coverage)* the cost of a non-leaf rebind is unmeasured (`X5` has no children) |
| 28 | CC-5 | minor | *(coverage)* the 21 baseline IDs' operative-claim consistency is asserted by `S-SC2` and oracled only for the new IDs |
| 29 | F4-2 | minor | `AUDIT.md` is an unenumerated accessor of the directory `§4` scores "runner fenced out" |
| 30 | F1-8 | nitpick | `B0.8`'s P2 line list is 10 of 13 sites; `§1b`'s APPROVAL row points to "§3 D7" (topgate is **D9**, in **§2**) |
| 31 | — | nitpick | `2-plan.md:376-377`'s risk-acceptance sentence is garbled (missing "or"); fixture paths disagree between `2-plan.md:346` (`fixtures/X1…X8/`) and `1.5-criteria.md:27` (`fixtures/X<n>-<name>/`) |

**WORST SEVERITY: blocker**

The single blocker is narrow and mechanical — reassign the terminal-status write to the stage that runs *after* `_assembled.md` exists — but it re-creates the exact deadlock that bounced pass 1, and it is invisible to the criteria set because every fixture pre-supplies the fact whose producer is broken (CC-1). Ten of the twelve convergent findings and three of the five blockers **are** genuinely closed, with mechanisms I verified in the source; the corrected baseline (`B0.6`) reproduces exactly under its own mandated matcher, and `R1` can now pass its own replay. The pass's remaining weakness is concentrated in one place: the three **new** instruments it built to enforce discipline (`S-PRD`'s pair check, `idcollide.sh`, `S-C10`'s pinned predicate) each fail their own can-fail test in a different way, and one — `idcollide.sh` — cannot pass on unchanged baseline structure at all.agentId: a7b5eb6d0dfbb794f (use SendMessage with to: 'a7b5eb6d0dfbb794f', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 231586
tool_uses: 38
duration_ms: 1279845</usage>