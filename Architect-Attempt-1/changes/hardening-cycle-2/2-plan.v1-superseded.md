# Stage 2 — Plan (hardening cycle 2)

## 0. Shape and sequence

One coherent edit to **18 existing files**; **no new artifact files**; **no new run-tree machinery beyond
what §1 tabulates**. Sequenced **definitions → charter → referencing stages → router → templates/examples
→ live-copy sync**, so no reference precedes its definition (the artifact is a position-sensitive prompt
assembly; forward references in a prompt are read as noise).

**Two design principles, each earned from cycle 1's cap:**

1. **AN OPERAND IS COMPUTED, NOT STORED (the anti-cap principle).** §1 classifies every fact this cycle's
   predicates read as **(i) computable on demand** or **(ii) written by a named stage that provably runs
   before the reader**. A class-(i) operand has **no producer to mis-order**, which is precisely how
   cycle 1's failure class is avoided rather than re-argued. Where cycle 1 needed a stored terminal status
   to make BIND work, this cycle needs only `sha256sum`.
2. **Reuse a surface rather than inventing one.** Every fact of class (ii) below lands in a file a
   baseline stage **already writes** (a review record, a gate-log entry, `plan.md`) — so there is no new
   producer position to get wrong, and no new file whose absence could deadlock anything.

---

## 1. OPERAND TABLE — every fact a new predicate reads, and where it comes from

**Class (i) = computed on demand at check time. Class (ii) = written by a named stage strictly before the
reading stage.** Nothing in §2–§3 reads a fact absent from this table. *This is the check cycle 1's plan
failed twice; it is a required section here.*

| Fact a new predicate reads | Class | Producer / computation | Reader (stage) | Ordering shown |
|---|---|---|---|---|
| `sha256(<node>/plan.md)` — current | **(i)** | `sha256sum <node>/plan.md` **at check time** | 5, 7 | n/a — no write |
| `sha256(<parent>/plan.md)` — current | **(i)** | `sha256sum <parent>/plan.md` at check time; **at the root: N/A, no parent exists** | 5, 7 | n/a — no write |
| the record's **reported** context-file sha256 map | **(ii)** | **stage 3 / stage 4**, inside the record it writes (the charter **already** mandates this field at `charter.md:96`) | 5, 7 | 3,4 → 5 → 7 ✔ |
| `spawn_id` (dispatcher-observed) | **(ii)** | **stage 3 / stage 4** — the dispatching owner writes it into the record's provenance | 5 | 3,4 → 5 ✔ |
| gate state `clean` / `clean-fixed-in-place` / `clean-demoted` | **(ii)** | **stage 5**, in the node's own gate-log entry (`<node>/decisions.md`) — a file stage 5 already writes | 7 | 5 → 7 ✔ |
| `rebound_from` / `rebound_to` | **(ii)** | **stage 5**, same entry, when a RES(a) fix-in-place re-binds | 5 (immediately), 7 | 5 → 7 ✔ |
| `fixed_findings` / `demoted_findings` lists | **(ii)** | **stage 5**, same entry | 7 | 5 → 7 ✔ |
| `elc` (self-declared estimated leaf count) | **(ii)** | **stage 2** — the node's own owner declares it in `plan.md` §2 | **the child's** stage 6 (DEC) | 2 → 6 ✔ |
| the child dependency DAG | **(ii)** | **stage 2** — declared in the decomposition block of `plan.md` | 4 (validates), 7 (emits order) | 2 → 4 → 7 ✔ |
| `approved_root_plan_sha256` | **(ii)** | **the top-level approval artifact's author** — i.e. *not the runner* — recorded in `plan/topgate/APPROVAL.md` when the approval is given | 6 (TOP) | approval → 6 ✔ |
| the assembly approval (HG2) | **(ii)** | **the human**, relayed and recorded at `plan/assembly-approval.md` after `assembled-plan.md` exists | 7 terminus / XPM | 7 writes `assembled-plan.md` → human → 7 terminus ✔ |
| the ingest mapping table (`ABSENT` rows) | **(ii)** | **stage 2** in `ingest-and-complete` mode, into `tree/root/plan.md` | 3 (completeness pass) | 2 → 3 ✔ |
| the catalog lock (`.architect-catalog.lock`) | **(i)** | an **atomic `mkdir`** at acquisition time; holder identity is inside the dir | stage 1 (seed), run end (commit) | n/a — the mkdir *is* the test |
| `catalog-pending/<skeleton>.md` + `PROPOSAL.md` | **(ii)** | **stage 6**, the proposing node's own file | the top orchestrator at **run end** | 6 → run end ✔ |

**Two facts are deliberately NOT introduced, and their absence is what keeps this cycle out of cycle 1's
class:** a **terminal `subtree:` status** and a **per-child declared seam hash**. Both are class-(ii) facts
whose producer position was the cap's defect; both belong to the deferred F1/F2 work. **No predicate in
this plan reads either.**

**HG2's operand deserves the ordering spelled out, because it is the one new predicate whose operand is
produced by a party outside the loop:** stage 7 writes `assembled-plan.md` **first** (that is what the
human reads), then HALTs and relays; the approval is recorded **after**; the terminus (XPM) reads it
**after that**. The write that gates is therefore *later* than the write it gates on — the exact inversion
cycle 1 got wrong, here in the correct direction. **A run that stops at the HALT is stopped, not
deadlocked:** `assembled-plan.md` exists and is complete; only *presenting* is blocked.

---

## 2. The edits, fix by fix

Each entry states the operative text's substance and **every site** it must appear at (the criteria's
positive per-site assertions are keyed to these lists).

### D1 — `BIND`: bind records to the text they reviewed *(F3)*
**Substance.** The charter already has every reviewer report the **sha256 of each context file it read**.
No stage compared them; now stage 5 and stage 7 do. A record is **current** iff the sha256 it reports for
this node's `plan.md` equals `sha256(<node>/plan.md)` **computed now**, and — where the record also
reports the parent's `plan.md` — iff that equals `sha256(<parent>/plan.md)` computed now. **At the root
there is no parent, so the parent clause is `N/A`; a root-only (single-node) run gates on the node clause
alone.** A non-current record is **stale ⇒ un-run**: the node is **un-gated** at stage 5 and **assembly is
blocked** at stage 7.
**Records are immutable** — the author never edits a reported hash. A legitimate re-bind after a RES(a)
fix-in-place is a **new gate-log entry** carrying `rebound_from: <old sha256>` and
`rebound_to: <new sha256>`; BIND then accepts a record whose reported hash appears in a `rebound_from`
whose `rebound_to` equals the current `sha256(plan.md)`. **Therefore a `clean-fixed-in-place` node IS
assemblable** — the discriminator is the presence of a valid rebind entry, not the raw hash. *(This is the
D2↔RES(a) contradiction cycle 1 left open, resolved by stating the positive case rather than by silence.)*
**Gate artifacts:** the top-level approval artifact `plan/topgate/APPROVAL.md` records
`approved_root_plan_sha256`; TOP is unsatisfied while that ≠ `sha256(tree/root/plan.md)`, so a re-drafted
root split **re-fires the existing** human gate rather than keeping its approval. **Honest limitation,
stated at the same site:** `plan/topgate/`'s *bare existence* still satisfies TOP's base predicate
(stage 1 still pre-creates the dir) — that is **F5, deferred**; BIND adds a staleness condition, not an
authorship contract.
**Restart contract amendment:** for a **review record**, *stage-done* = the deterministic output exists
**and** it is BIND-current.
**Sites:** `stages/charter.md` (provenance bullet), `stages/stage-5-gate.md`,
`stages/stage-7-assemble.md`, `stages/stage-8-restart-resume.md`, `stages/stage-6-granularity-decompose.md`
(the TOP clause), `METHODOLOGY.md` (state contract + index row), `SKILL.md` (rule-block one-liner).

### D2 — `IDN`: a dispatcher-recorded audit surface with a declared-degraded value *(F9)*
**Substance.** `spawn_id` = **the identifier the dispatcher observed at spawn**, recorded by the owning
(sub-)orchestrator into the record's provenance — **not** self-reported. A reviewer's own claim about its
identity is a separate, optional `self_reported_identity` field, corroboration only.
**Two asymmetric rules, both stated:** three identical **dispatcher-recorded** ids ⇒ one agent asked three
times ⇒ the pass is **un-run**. Three identical **self-reports** — including three *"unavailable"* — are
**not** evidence of one agent and **never** make a pass un-run. If the harness exposes no
dispatcher-observable id, the record carries **`spawn_id: unavailable-by-harness`** and the pass is
**declared degraded in the record** — a limitation to state, never a reason no plan can gate. *(Cycle 1's
unconditional "3 identical ⇒ un-run" made gating impossible; it is dropped.)*
**Sibling-read ban:** a same-pass reviewer's closed input set **excludes** the node's own `completeness/`
and `adversarial/` directories; carried-forward findings reach the adversarial pass only via the owner's
quote in the node's gate log; a record citing a sibling record is **contaminated ⇒ un-run**.
**Sites:** `stages/charter.md` (provenance + closed set), `stages/stage-3-completeness-critic.md`,
`stages/stage-4-adversarial-redteam.md`, `stages/stage-5-gate.md`, `METHODOLOGY.md` (index row).

### D3 — `RES`: "resolved" in three arms; a demoted node is visible *(F10)*
**Substance.** GBP's *clean-or-resolved* is otherwise circular. At stage 5:
**(a)** a **minor/nitpick fixed in place** may re-bind **without** fresh passes iff the edit is traceable
to a **specific reviewer finding ID** logged in the node's gate log, the diff is logged, and the entry
records `rebound_from`/`rebound_to` (BIND). Gate state ⇒ **`clean-fixed-in-place`**.
**(b)** a **blocker or major** is **never** resolvable in place — it routes to stage 2; the re-draft
changes `plan.md`, so BIND makes the old records stale and fresh passes are **forced**, mechanically.
**(c)** an author edit **no reviewer asked for** is a **re-draft**, not a resolution — same route as (b).
**A demoted blocker/major is not clean.** Where the human tie-break demoted one, gate state ⇒
**`clean-demoted`**, and the entry names **who** demoted it and the **durable source**. The three states
`clean` / `clean-fixed-in-place` / `clean-demoted` are **distinguishable at assembly**, and each node's
section in `assembled-plan.md` carries its gate state plus the `fixed_findings` / `demoted_findings` lists
— so a node carrying four fixed minors and a demoted major is **no longer indistinguishable** from a
genuinely clean one. **All three states are assemblable** (see D1).
**Sites:** `stages/stage-5-gate.md` (definition + severity table), `stages/stage-7-assemble.md`
(reader + assembled header), `METHODOLOGY.md` (GBP block points at RES; index row), `SKILL.md`
(rule-block GBP clause).

### D4 — `CTX`: `redteam_context` as a first-class, de-conflated contract key *(F4)*
**Substance.** Add to `METHODOLOGY.md`'s config-contract YAML:
```yaml
redteam_context:               # paths every cold agent MUST read to check the plan's claims against the
                               # world it plans in. PRIORITY-ORDERED — first entries are the entrypoints
                               # to read first; each may carry a note on what to check there.
  - path: <most-relevant-source>
    note: <what to check here first>
```
plus the rule: **`redteam_context` is citable source the reviewer must read; `off_limits_paths` is a fence
the run must never write into. A path may legitimately be both. Conflating them is how a review silently
degrades to docs-only — which the charter names as the failure this whole family exists to prevent.** It
is **priority-ordered** because a cold agent cannot exhaustively read a large tree.
**Non-vacuous validation:** **absent or empty `redteam_context` is a config error that stops the run** —
because path-validation over an absent key checks **zero paths** and passes trivially. Under RAT3 that is
a HALT + relay.
**The worked example gains the key as a top-level key** with priority-ordered entries and notes, replacing
the prose mention buried inside `off_limits_paths`.
**Sites:** `METHODOLOGY.md` (contract + rules), `SKILL.md` (Inputs),
`stages/stage-3-completeness-critic.md` (the validation stop),
`examples/authoring-a-skill/planning.md`, `examples/authoring-a-skill/README.md`.

### D5 — `OFL`: `off_limits_paths` stops being claimed as a fence *(subtractive)*
**Substance.** Replace *"Naming is the fence — no guard catches a stray write the config never declared"*
with the plain limitation: **`off_limits_paths` is a prompt-level convention, not an enforced fence.**
Listing a path tells the run and every agent it dispatches to treat that path as read-only context.
**It is not enforcement:** nothing in this skill intercepts a write, and **nothing catches a stray write
to a path the config never declared.** The protection is the declaration plus review; a run that needs a
real fence must obtain it **outside this skill** (filesystem permissions, a sandbox, the harness's own
tool permissions). **No mechanism is added and none is claimed.**
**Sites:** `METHODOLOGY.md` (config-contract rule), `stages/stage-1-frame-template-match.md`
(cross-cutting rule), `examples/authoring-a-skill/planning.md` (the key's comment).

### D6 — `PRV`: what the gate establishes, and what it does not *(F7, softening half ONLY)*
**Substance.** Gate-before-present establishes, **on the record**: (i) a **decontaminated review
occurred** — two passes, three separately-spawned cold agents each, with the charter's provenance, each
record **BIND-current** to the text it reviewed; and (ii) **the contract tiers are filled** — every spine
section and every Layer-2 `required_sections` entry named with its coverage cited, a **sample
spot-verified** (SPV).
It does **not** establish that no unanticipated load-bearing section remains: tier (iii) asks for a
**negative that no finite review can prove**. And **N same-model instances are not N independent minds** —
separate spawns remove shared **context**, not shared **priors**, so three cold agents have **correlated**
blind spots. **Whether frame diversity narrows that correlation is not settled by this skill and is not
claimed here** (DIV is deferred).
**The operative sentence, used verbatim at the short-form sites: *"The gate raises the cost of shipping a
hole. It does not certify its absence."***
**All 8 baseline overclaim occurrences across 5 files are rewritten** (`0-baseline.md` B4/P6). The
frontmatter `description` is rewritten **under measurement** — ≤1024 chars, no angle brackets, and the
trigger vocabulary + proactive-suggest clause preserved (SC1/SC2 verify, they are not assumed).
**Sites:** `SKILL.md` (frontmatter, purpose paragraph, rule 1), `METHODOLOGY.md` (opening, founding-failure
section, a new PRV block, index row), `README.md` (oracle table row + body),
`stages/stage-7-assemble.md`.

### D7 — `SPV`: the spot-verify duty gets a named owner *(Tier-3)*
**Substance.** The charter assigns spot-verify to *"whoever consumes the review"*, which is nobody. It is
**stage 5's**: before routing, the owning orchestrator checks a **sample** of each record's cited
file:lines / section references actually exist and say what is claimed — **≥1 citation per record, ≥2 per
pass** — and **records the sample and the result** in the node's gate entry. **A fabricated citation makes
that record un-run.** **Stage 7** carries the cross-node half for any claim it relies on across nodes.
**Sites:** `stages/charter.md`, `stages/stage-5-gate.md`, `stages/stage-7-assemble.md`.

### D8 — `CNC`: serial-vs-parallel declared; every shared surface partitioned *(Tier-3)*
**Substance — the declaration.** **Parallel:** sibling sub-orchestrators (one per child at a branch) and
the 3 cold agents within a single pass. **Serial:** a node's own stages, and the two passes relative to
each other (PASS-ORD).
**Substance — the partition** (single writer per file, not a lock, except the one genuinely cross-process
surface):

| Shared surface | Baseline accessors | New discipline |
|---|---|---|
| `index.md` | **four** writers, all parallel: `stages/stage-1…:20`, `stages/stage-6…:11-12`, `METHODOLOGY.md:195`, `templates/seed/README.md:14` | **DERIVED, never authoritative** — written **only** by the top orchestrator, by walking the tree. Per-node facts live in that node's own `_status.md`. *The accessor set is removed, not locked.* |
| `<node>/_status.md` | undefined at baseline | **that node's own owner only** |
| the gate log | `plan/decisions.md`, appended by **every** owner (`stages/stage-5…:19`, `SKILL.md:61-62`) | **partitioned**: per-node gate entries → **`<node>/decisions.md`** (that node's owner only); **`plan/decisions.md`** → **run-level events only**, top orchestrator only (the top-split approval, the assembly approval, run-level aborts). CAP counts a node's bounces from **its own** log — which also improves ECON: an owner reads its own log, not the whole run's. |
| the cross-project catalog `~/.claude/architect/templates/` (git) | any sub-orchestrator, **mid-run** (`stages/stage-6…:32-35`), **and any concurrent Architect run on the machine**, **and** the first-run seed + `git init` | **top orchestrator only, at run end**, holding an exclusive lock: atomic `mkdir <catalog>/.architect-catalog.lock`, holder records run-root + pid inside it. **The first-run seed + `git init` takes the same lock.** A stale lock whose pid is dead may be broken **only** with an entry in the breaker's `plan/decisions.md` **and** a `BROKEN-BY` file inside the lock dir, so the victim run can see it. |
| **Declared uncovered** | two runs sharing one `run_root` | **unsupported — a config error.** Declared, not guarded. |

**And the false claim goes:** `stages/stage-8-restart-resume.md`'s *"State is per-node — there is no single
global cursor to stale-edit"* was **false while `index.md` was written by every owner**. Replaced with:
`index.md` is **derived, not authoritative**; the per-node `_status.md` files are.
**Sites:** `METHODOLOGY.md` (a CNC block + the run-tree diagram + index row), `SKILL.md` (Loop paragraph),
`stages/stage-1-frame-template-match.md`, `stages/stage-3-completeness-critic.md`,
`stages/stage-4-adversarial-redteam.md`, `stages/stage-5-gate.md`,
`stages/stage-6-granularity-decompose.md`, `stages/stage-8-restart-resume.md`, `stages/charter.md`
(closed set now names the node's own gate log), `templates/seed/README.md`.

### D9 — `DEP`: inter-leaf dependency ordering *(Tier-3)*
**Substance.** A decomposing node declares, alongside its seam table, a **dependency edge for every child
pair that has one** (`<child-b>` requires `<child-a>`'s output). **A cycle among a node's children is a
blocker** at that node's gate. Stage 7 emits an **`## Execution order`** section into `assembled-plan.md`:
a topological order of the leaves with the **parallelisable groups** marked, derived from the per-node
DAGs. Skeletons gain a **Depends on** column (`decomposition-node.md`) and a **Prerequisites** line
(`leaf-task-spec.md`).
**Sites:** `stages/stage-2-draft-node.md`, `stages/stage-4-adversarial-redteam.md` (validates it),
`stages/stage-7-assemble.md`, `templates/seed/decomposition-node.md`,
`templates/seed/leaf-task-spec.md`, `METHODOLOGY.md` (index row).

### D10 — `DEC` / `elc`: one operand, honestly labelled; one trip condition *(Tier-3)*
**Substance.** One operand: **`elc`** — the node's **estimated leaf count**, an integer its **own owner
declares** at stage 2. **It is self-declared, not computed** — nothing measures it, and saying otherwise
was the overclaim. **ONE trip condition:** two consecutive levels with `elc(child) ≥ 0.8 × elc(parent)` ⇒
escalate. The single-level formulation at `templates/seed/decomposition-node.md:24-25` is **removed**.
Stated plainly: **DEC detects a decomposition its own owner does not believe is reducing; it cannot detect
a mis-estimate** — catching a wrong `elc` is the adversarial pass's granularity-validation duty (GRN).
**Sites:** `METHODOLOGY.md` (DEC block + index row), `stages/stage-2-draft-node.md` (declares it),
`stages/stage-6-granularity-decompose.md` (checks it), `templates/seed/decomposition-node.md`.

### D11 — `IGM`: `mode: ingest-and-complete`, defined *(Tier-3 — the mode the dogfood itself ran in)*
**Substance.** Config keys **`mode: fresh | ingest-and-complete`** (default `fresh`) and
**`ingest_source`**. In ingest mode: the named draft is copied **immutably** to
`tree/root/plan.md.ingested` (never edited), and stage 2 writes `tree/root/plan.md` as a **mapping
table** — one row per spine section and per Layer-2 required section → the **locus in the ingested draft**
that covers it, or **`ABSENT`**. Every `ABSENT` row is a **candidate tier-(i)/(ii) hole** the completeness
pass must resolve. **Ingest may not silently author an absent section**; content Architect does author is
marked **`architect-authored`** so the cold critic weighs it as unreviewed rather than as the owner's. The
rest of the loop is unchanged.
**Sites:** `METHODOLOGY.md` (contract + index row), `SKILL.md` (Inputs),
`stages/stage-1-frame-template-match.md`, `stages/stage-2-draft-node.md`,
`examples/authoring-a-skill/planning.md`.

### D12 — `TPL3`: stage a proposal; never auto-commit an unreviewed artifact *(Tier-3)*
**Substance.** A back-propagated hole-fix (TPL3) and a distilled new skeleton (TPL2) are written to
`<run-root>/catalog-pending/<skeleton>.md` with a `PROPOSAL.md` naming the node, the finding and the diff.
The commit to the shared user-space catalog happens **only at run end**, **only** by the **top
orchestrator**, **only** under the catalog lock (D8), and **only after a cold review of the proposed
diff**. A mid-run `git commit` of an **unreviewed AI-authored patch** into a shared cross-project repo
violates the family's own founding rule — nothing self-certifies — and is no longer permitted.
**Sites:** `stages/stage-6-granularity-decompose.md`, `templates/seed/README.md`, `METHODOLOGY.md`.

### D13 — `RST`: the root node's location, pinned *(Tier-3)*
**Substance.** The root plan node lives at **`tree/root/`** — its own dir with its own `plan.md`,
`_status.md`, `completeness/`, `adversarial/`, `decisions.md`. **The root is a node like any other**; a
special-cased root is where orphan and ordering defects enter. The apex roll-up is
**`tree/root/_status.md`**.
**Declared departure:** the approved scope/decision record
(`/home/zero/.claude/plans/1-this-is-a-proud-scott.md:173`) fixes `tree/_status.md` as the apex roll-up.
Moving it into `tree/root/` is a **deliberate change to an owner-approved on-disk layout**, recorded in
this cycle's `decisions.md`, and made because pinning the root as an ordinary node is what lets BIND's
root carve-out and the assembly walk be stated uniformly. **The apex roll-up still exists — at
`tree/root/_status.md`.**
**Sites:** `METHODOLOGY.md` (state contract + run-tree diagram + RST index row),
`stages/stage-1-frame-template-match.md`, `stages/stage-7-assemble.md`,
`stages/stage-8-restart-resume.md`.

### D14 — `SPN`: ONE canonical §4 heading string *(Tier-3; the grep-stability rationale, honoured)*
**Substance.** The canonical string is exactly:

> **`Outputs & artifacts (with their locations)`**

declared **once** in `METHODOLOGY.md`'s spine list as *the* heading, and used **verbatim** at every site
that names §4. The five other baseline spellings (`0-baseline.md` B4/P18) go. The leaf skeleton's
collapsed heading becomes `Outputs & artifacts (with their locations) (§4)` — the canonical string plus
the section marker, so the same grep finds it.
**Sites:** `SKILL.md` rule 1, `METHODOLOGY.md` (spine + SPN index row),
`stages/stage-2-draft-node.md`, `stages/stage-3-completeness-critic.md`,
`templates/seed/{generic-node,decomposition-node,leaf-task-spec}.md`.

### D15 — Seed-skeleton Layer-2 slots *(Tier-3; the catalog was manufacturing tier-(ii) holes)*
**Substance.** Each of the three seed skeletons gains the same explicit heading:
```
## Layer-2 required sections (from the config's `required_sections`)
```
with the instruction to append **one filled section per config entry**, and the tier-(iii) reminder that
the generative critic still hunts for the section on **neither** list. `generic-node.md`'s italic note is
**promoted** to this heading (it had a note but no slot, so **3 of 3** skeletons failed the bar, not 2).
`templates/seed/README.md`'s seed table notes the slot.
**Sites:** all three skeletons + `templates/seed/README.md`.

### D16 — `HG2` + `XPM`: the second human gate and the terminus *(F8, owner-ratified R2)*
**Substance — HG2.** After `assembled-plan.md` is written and **before the run is done**, **the human
reads the assembled plan and approves or bounces it.** Two human gates now exist: **TOP** at the
top-level split, **HG2** at assembly. Under **RAT3** this is a **HALT + verbatim relay**, never
self-approved. The approval is recorded at `plan/assembly-approval.md` (a run-level file, top orchestrator
only, per D8).
**TOP's "ONLY" is narrowed, not deleted:** every site that said the human gate is the top-level split
**ONLY** now says the **decomposition** gate fires at the top level only and **does not fire at deeper
splits** — the anti-gate-fatigue half is preserved — while HG2 is a **separate, later gate on the finished
artifact**, one gate at the end, **not a gate per node**.
**Marked as this cycle's own choice, not owner-ratified (RAT2):** *how* a bounce routes — it re-opens the
node(s) the human names, at that node's stage 2. Stated in the artifact as an authoring choice.
**Forward constraint on deferred work, stated in the artifact:** any future **bottom-up per-node
assembly** (part of the deferred F1 work) **must preserve a whole-assembled-plan reader**, because HG2
requires one; the naive bottom-up design deletes the only one and would strand a ratified decision.
**Substance — XPM.** The presentable artifact is **`assembled-plan.md`** (a decomposed run) or **the
root's own `plan.md`** (a single-leaf run). **Exit-plan-mode / presenting is blocked by BOTH gates that
guard assembly: the structural GBP precondition AND HG2.** Every site that asserted the terminus is
gate-before-present-gated **only** is corrected.
**Sites:** `SKILL.md` (rule block, Loop, Stop-for-human), `METHODOLOGY.md` (Gates section, the two-layer
completeness/gate blocks, run-tree diagram, index rows), `stages/stage-5-gate.md` (the single-leaf
terminus), `stages/stage-7-assemble.md` (the operative gate + the terminus),
`stages/stage-8-restart-resume.md` (both gates survive restart).

### D17 — ID hygiene: the grep, the naming rule, the index *(A/F1-2 + the baseline gap)*
**Substance.** `METHODOLOGY.md`'s cross-file-rule-index preamble now states the authoritative site set is
```
grep -rlnow -- <ID> SKILL.md METHODOLOGY.md README.md stages/ templates/ examples/
```
— **word boundaries mandatory** (a bare `grep -o TOP` matches inside `HARDSTOP` and manufactures phantom
sites), **`templates/` and `examples/` in scope** (both hold real rule sites: `SPN`, `COV`, `GRN`, `TOP`,
`DEC`, `TPL*`). Plus the **phantom caveat** — word boundaries remove `HARDSTOP` but **not** the ordinary
English phrase **`ON TOP OF`**, so hits are hand-triaged and exclusions **reported** — and the **ID naming
rule**: a new ID is a **standalone uppercase token**, not a substring of another ID or of an ordinary
uppercase corpus word; the legitimate **family** nestings (`CMP`⊂`CMP2`, `TPL`⊂`TPL1/2/3`) are named as
such, and the two **grandfathered** baseline violations (`DEC`⊂`DECOMPOSE`, `TOP`⊂`HARDSTOP`/`TOP-LEVEL`)
are named as declared debt rather than hidden.
**Index completeness:** rows added for the live-but-unindexed **`TPL1`**, **`TPL2`**, **`SEV`** and for
every ID this cycle introduces (`BIND`, `IDN`, `RES`, `CTX`, `OFL`, `PRV`, `SPV`, `CNC`, `DEP`, `IGM`,
`HG2`, `XPM`).
**Colliding IDs are not introduced.** The ingest-mode ID is **`IGM`** (never `ING` ⊂ `PLANNING`/`RULING`);
the killed-node ID **reserved** for the deferred F6 work is **`KLB`** (never `KIL` ⊂ `SKILL`), noted in
this plan so the deferral inherits the correct name. Enforced by `oracles/idcollide.sh` — **an instrument,
not a promise.**
**Sites:** `METHODOLOGY.md` (preamble + index table), `SKILL.md` (the self-check ID list).

---

## 3. Measurement + the instrumentation this change adds (CP3 / ST2a)

**Four instruments, all in `changes/hardening-cycle-2/oracles/`. Two already exist and have already been
mutation-tested (stage 0); two are built at stage 5.**

1. **`check.sh <tree>`** *(new at stage 5)* — one subcommand per `S-` criterion. Every assertion is a
   **positive per-site assertion**: the operative sentence is present at each site that must state it.
   Text is **normalized** first (`normalize()`: strip `**`/`*`/backticks, collapse whitespace, flatten
   line wraps) so markdown emphasis and line-wrapping cannot make a check silently pass. **Every absence
   sweep is paired** with its positive assertion. Takes a **tree path**, so the identical checker runs
   against the edited tree and against the baseline replay.
2. **`baseline-replay.sh`** *(new at stage 5)* — materialises `git show b08f5a9:Architect/<file>` into a
   scratch tree and runs the **same** `check.sh`. **This is the oracle-can-fail self-test for the whole
   `S-` family:** every new-rule assertion **must FAIL** there and every preserved-rule assertion **must
   PASS** there. A subcommand that passes against the baseline is **not an oracle** and its criterion is
   `verified = no`. *(Cycle 1's three instruments each failed their own can-fail test; this is the guard.)*
3. **`ruleid-sitemap.sh`** *(built and self-tested at stage 0)* — word-boundary ID→site map with an
   **explicit phantom-exclusion list** whose exclusions are **reported, not silently dropped**.
   **Self-test result, recorded:** reports `stage-8` as a **non-site** for `TOP` and the two `ON TOP OF`
   hits as excluded phantoms. Drives **R1**.
4. **`idcollide.sh`** *(built and self-tested at stage 0)* — the ID naming rule as an instrument, with
   **two stated exemption classes** (family nestings; grandfathered baseline debt) so it neither passes
   everything nor fails everything. **Self-test results, recorded:** with cycle 1's rejected ids ⇒
   `KIL ⊂ SKILL`, `ING ⊂ PLANNING`, `ING ⊂ RULING`, **exit 1**; with cycle 2's ids ⇒ **exit 0**. Drives
   **R3**. *It also produced a finding: the baseline violates its own ID rule at `DEC` and `TOP`, which
   cycle 1's B0.7 wrongly claimed it did not.*

**Behavioural arms — 4 clusters × 2 separately-spawned cold agents = 8 agents.** Fixtures live in
`changes/hardening-cycle-2/fixtures/X{1..4}/{holed,intact}/`. Each agent gets **only** its own fixture +
the relevant **new** stage text + a required output form (`VERDICT: <named option>` + the rule ID applied +
its citation, per item). Arms never see each other.

| Arm | Criteria it exercises | holed ⇒ | intact ⇒ |
|---|---|---|---|
| **X1** | S-BIND (incl. the root carve-out) | records stale ⇒ node **un-gated**, do not assemble | gated clean ⇒ assemble (**and** a root node with no parent gates fine) |
| **X2** | S-HG2, S-XPM, **SC3** (the position probe) | `assembled-plan.md` exists, all nodes clean, **no** human assembly approval ⇒ **HALT + relay**, do not present / exit plan mode | approval on record ⇒ present. **GBP must still fire in both arms** — its failure to fire is a position regression even with its text intact |
| **X3** | S-IDN (the asymmetry), S-RES | three identical **self-reported** `unavailable` ⇒ **NOT** un-run (declared degraded, proceeds) | three identical **dispatcher-recorded** ids ⇒ **un-run**; and a node with a demoted major ⇒ **`clean-demoted`**, not clean |
| **X4** | S-CTX, S-IGM | config with **no** `redteam_context` ⇒ **config error, stop the run** | key present ⇒ proceed; and an ingest fixture with §4 absent ⇒ marked **`ABSENT`** + flagged, not filled |

**X3's polarity is deliberately inverted** so an agent cannot pass by pattern-matching "holed ⇒ block".
**Both arms the same verdict ⇒ `verified = no`**, whichever verdict it is.

**Verification map:** `S-*`, `R2` → `check.sh` + `baseline-replay.sh` · `R1` → `ruleid-sitemap.sh` ·
`R3` → `idcollide.sh` · `SC1`/`SC2` → `quick_validate.py` + a measured length/angle-bracket/vocabulary
assertion · `SC3` → line-offset + intra-block-order assertion **and X2** · `SC4` → `diff -rq` **before and
after** the sync · `SC5` → a recorded ID-consistency hand-diff + the charter-fork sha256 check ·
`X1…X4` → the 8 arms above.

**Grep-only rows are labelled, not hidden.** `1.5-criteria.md` marks each P assertion on a **behavioural**
path as **`PROXY`** and pairs it with an execution arm. Rows whose subject **is** the text (S-OFL, S-PRV,
S-SPN, S-SPV, S-IDGREP, S-SLOT, S-TPL3, S-DEC, S-DEP, S-RST, S-CNC) are **not** proxies — the criterion is
that the artifact says a particular thing, and a normalized positive per-site assertion is a direct check
of exactly that.

---

## 4. Concurrency (ST2b) — accessors enumerated, guard scope named

The change **alters the concurrency structure over shared state**, so the accessor enumeration is
mandatory. It is **D8's table**, which is the operative form: every baseline accessor of every shared
surface is listed (including all four `index.md` writers, which cycle 1's first pass missed), the new
discipline is named per surface, and the **one uncovered case** — two runs sharing a `run_root` — is
**declared unsupported** rather than silently assumed safe.

**Guard scope, stated as a claim rather than assumed:** for `index.md`, `_status.md` and the gate logs the
"guard" is **not a lock at all** — the accessor set is **reduced to one writer**, which is why there is no
scope gap to enumerate. The **only** genuine lock is the catalog, and its scope is explicitly stated to
cover **three** access paths that a naive version misses: mid-run commits, **concurrent runs on the same
machine**, and the **first-run seed + `git init`**.

**Honest statement of what cannot be executed here (ST1.5e/H4).** A no-lost-update criterion normally
requires an **executed interleaving**. There is nothing to execute: the accessors are *prompt instructions
to agents*, not code, so there is no runnable read→write window to inject a competing mutation into. The
available check is that the artifact **removes the multi-writer structure**, asserted positively at every
baseline accessor site. **S-CNC's interleaving sub-item is therefore labelled `advisory` with that reason
stated**, and is surfaced in `8-harness.md` rather than counted as an executed interleaving. It is **not**
relabelled advisory to dodge a verifiable gate — the verifiable half (the site assertions) stays gating.

---

## 5. Thresholds → routing

- Route on the **reviewer's** severity (SEV3). Contest only via a logged `decisions.md` entry.
  **Demoting a blocker or major requires the human tie-break** — under RAT3, with the owner not present,
  that is a **HALT + verbatim relay**, never taken here.
- **blocker → stage 1 · major → stage 2 · minor → fix in place, proceed · nitpick → log, proceed.**
- **CAP (SEV4):** cycle 1 spent **2 bounces at gate 4** on the class *"a predicate whose operand has no
  valid producer."* **That class is no longer in scope** — §1 admits only class-(i) and class-(ii)
  operands, and the two facts that produced the class are deferred. A bounce on a **different** class
  starts that class's count at 1. **A bounce on the old class would immediately re-trip the cap** and is a
  stop-for-human; this runner will relay it, not argue it.
- **A finding that requires a NEW human gate, or that lands on deferred work (F1/F2/F5/F6/DIV), is a
  HALT + verbatim relay** — not absorbed, not implemented.
- **All criteria are gating** except S-CNC's interleaving sub-item (advisory, reason stated in §4). A
  gating criterion that cannot be verified pre-ship has **exactly two** legal dispositions (a
  representative pre-ship harness, or a **named risk-acceptance** in `decisions.md`); under RAT3 the
  latter cannot be granted here, so the only remaining move is **HALT + verbatim relay**. **There is no
  "declared deferral" route in this plan** — cycle 1's was found illegal and is not reproduced.

## 6. Risks specific to this pass

| Risk | Contingency |
|---|---|
| **18 files + 12 new IDs → a cross-file contradiction** (highest risk) | SC5's recorded hand-diff of every new ID's operative claim across all its sites; a contradiction is **major** → stage 2. R2 catches half-migrations mechanically. |
| **The gate-log partition (`plan/decisions.md` → `<node>/decisions.md`) half-migrates** — it touches ~10 files | It is a **CHANGE row (P9) under R2**: the new claim must appear at **every** site that stated the old one. `check.sh cnc-gatelog` asserts each site positively; a miss is a regression, not a partial pass. |
| **Adding HG2/PRV to `SKILL.md`'s rule block displaces GBP** (position lens) | SC3: the block still precedes the stage table, its **intra-block order** is asserted, **and** X2 executes a case where GBP must still fire. HG2 is added **after** the three existing rules so nothing that worked because it was early is moved. |
| **The softened `description` stops triggering the skill** | SC2 is gating: the trigger vocabulary + proactive-suggest clause must survive, and SC1 measures the length/angle-bracket constraints rather than assuming them. |
| **An oracle passes against the baseline** (cycle 1's exact failure) | `baseline-replay.sh` is a **gating** part of every `S-` row: new-rule assertions must FAIL on `b08f5a9`. A subcommand that passes there is discarded and rebuilt (logged), and until then its criterion is `verified = no`. |
| **A `PROXY`-labelled grep row is mistaken for a behavioural check** | Every such row is labelled `PROXY` in `1.5-criteria.md` **and** carries a named execution arm; `8-harness.md`'s table repeats the label per row. |
| **8 agent arms is real runway** | Fixtures are tiny and clustered (4 clusters, per-item verdict tables). **If an arm cannot run, its criterion is `verified = no` and this runner HALTs and relays** — it is never folded into "done". |
| **BIND's gate-artifact clause is vacuous while stage 1 pre-creates `topgate/`** | Stated as an **honest limitation at the site** (F5 deferred) rather than claimed as a closure; S-BIND's row requires that limitation to be present, so the artifact cannot silently overclaim. |
