# Stage 3 — red-team of the plan: ranked cross-arm synthesis

Verbatim records: `3-redteam-plan.{A,B,C}.verbatim.md`. Charter + closed set + dispatch facts:
`3-charter-given.md`. Author's routing interpretation: `decisions.md`.

**Reviewers:** 3 cold, separately-spawned, **disjoint frames**, `general-purpose` / `claude-opus-5`,
**dispatcher-recorded** `spawn_id`s — A `aea2863bc75a6d6a5` · B `a170420f375a3ae9f` ·
C `a214e3d602b3b8587`. All three reported `spawn_id: unavailable` as their **self-report** and correctly
declined to invent one; the dispatcher's record is the audit surface (IDN, working as designed on its first
live use).

**Worst severity per arm:** A **major** · B **BLOCKER** · C **BLOCKER**.
**Gate-4 worst finding: BLOCKER.**

---

## CH6 — citation spot-verify, PERFORMED BEFORE ROUTING

7 load-bearing claims sampled and checked against source by this runner:

| Claim | Result |
|---|---|
| **C/O1** `oracles/ruleid-sitemap.sh:34` is a bare `exit 0` — no failure path | **CONFIRMED** (`grep -n exit` → `:12 exit 2` guard, `:34 exit 0`) |
| **C/O2** R1 accumulates **file names only** (`sites+=("$f")`), so it is a token-mention check | **CONFIRMED** (`:29`) |
| **C/O3** the baseline tree materialised from `git archive b08f5a9 Architect` **includes `changes/`**, which already satisfies several new-rule assertions | **CONFIRMED, and my own first counter-measurement was wrong.** Measured: `## Layer-2 required sections` 5 hits, **all** under `changes/`; `clean-fixed-in-place` 8/8; `Outputs & artifacts (with their locations)` 6/6; `PROVEN` 7 of 8. Under artifact-only scope all four are 0. **C is right; the retraction is recorded here rather than quietly dropped.** |
| **C/O8** `idcollide.sh`'s `GRAND` list pre-blesses `TOPGATE` + `DECOMPOSITION`, absent at `b08f5a9` | **CONFIRMED** — zero word-boundary hits for either token at baseline |
| **B/L2** no release / retry / wait policy for the catalog lock anywhere in the plan | **CONFIRMED** — `grep -ciE 'releas\|rmdir\|unlock\|retry' 2-plan.md` = **0** |
| **B/L11** `SKILL.md:3` says *"a human gate on the top-level split **ONLY**"* and is **not** in `B4/P12`'s site list | **CONFIRMED** — the line says exactly that; P12 lists four sites and not the frontmatter |
| **B/L16** S-PRV's `PROVEN` sweep *"can never pass"* because `provenance` contains it | **PARTIALLY REFUTED.** Case-sensitively, uppercase `PROVEN` does **not** occur inside lowercase `provenance` (`grep -c PROVEN stages/charter.md` = 0). The finding survives as a **real under-specification** — `normalize()` never states case — but not at the claimed severity. **Downgraded to minor by the author with this reason logged (SEV3: a demotion of a *major*, not of a blocker, and the contest is logged rather than silent).** |

**No fabricated citation found.** Every other sampled claim held on first check. **The severities are earned
and they route.** Additionally, A independently fetched the harness-authored transcript and confirmed
ratification records 694/699 — so the RAT1/CH11 audit was performed by a party that did not author it.

---

## The two BLOCKER classes

### Class α — *the anti-cap principle is evaded by classification in two places* (B, blocker ×2)

**B/L1 — HG2's operand is unproducible in a single-leaf run, and the reader precedes the producer.**
`2-plan.md:41` makes `plan/assembly-approval.md` producible *"after `assembled-plan.md` exists"*; `:312`
puts the single-leaf terminus at **stage 5**; `stage-6:13-14` + `stage-7:3-6` mean a single-leaf run
**never writes `assembled-plan.md`**. So a leaf-only run can never satisfy HG2 and can never present.
**This is cycle 1's cap shape with the operands mirrored** — and the single-node run is the mode this
hardening loop runs *itself* in.

**B/L2 — the catalog lock has no release, and `class (i)` is the mislabel that hid it.** `2-plan.md:43`
calls the lock class (i) — *"the mkdir **is** the test"* — which invoked the plan's own exemption
(*"a class-(i) operand has no producer to mis-order"*) and thereby **suppressed the question "which stage
writes the release?"**. `mkdir` is a mutation, not a computation. Walked: the **first run deadlocks against
its own stage-1 acquisition** (run end cannot re-acquire; the pid inside is its own and alive, so the break
path is closed). Second defect in the same row: the lock lives *inside* the directory it protects, so on a
genuine first run `mkdir <catalog>/.lock` fails ENOENT for every contender.

**This is the finding the orchestrator asked for explicitly** — *"if that principle has a hole, I want it
found now, at the cheap gate."* It has one, and its shape is precise: **the class-(i) label is an
exemption, and an exemption is a place to hide a producer.** Two of fourteen rows abused it.

### Class β — *the measurement apparatus cannot detect a failed build* (C, blocker ×5)

- **C/O1 + C/O2 — R1's oracle cannot fail.** `ruleid-sitemap.sh` is a **printer, not a checker**: no
  expected-site input, no comparison, unconditional `exit 0`. C mutated the tree to delete **every** `GBP`
  token from `stage-5-gate.md` (total site erosion — exactly R1's target) → the file silently vanished from
  the map, **exit 0**. Then kept one `<!-- see GBP -->` comment and deleted the operative rule sentence →
  output **byte-identical to baseline**, exit 0. **R1 is `verified = no` under H6, and it is a
  token-mention check of the kind `1.5-criteria.md:24` itself forbids.**
- **C/O3 — `check.sh`'s corpus is unpinned and the baseline replay includes `changes/`** (confirmed above):
  S-SLOT/S-RES/S-SPN's positives **pass at baseline** (⇒ not oracles, by my own rule) and S-OFL/S-PRV's
  sweeps become **unsatisfiable** because this cycle's own criteria file contains the swept strings.
- **C/O4 — the X protocol is not an experiment.** One probe per arm, from **two different agents**, no run
  count, no pass-rate floor — so a verdict split is confounded between "the text discriminates" and "two
  agents disagreed", and a verdict-indifferent pair passes with p ≈ 0.25. `Guarded_change/stage-1.5.md:72-75`
  (ST1.5d) explicitly forbids relying on a **single probe**. Worse: X2 carries **three** criteria, so one
  lucky split passes three at once.
- **C/O6 — ~11 P rows *describe* rather than *pin* the operative sentence**, and three are defeatable by
  text that mentions the right words while stating the **opposite** rule (C's S-IDN counter-example inverts
  the asymmetry while containing both required tokens). *"or equivalent normalized form"* hands the
  matcher's definition to the builder — the exact loophole ST1.5f exists to close.

---

## Convergence across disjoint frames

**A and C independently filed the same finding twice**, which is the strongest signal in the set:
- *"8 occurrences across 5 files"* is **4 files** (A/F7, C/O11) — and C shows it is a **verbatim repeat** of
  cycle 1's `pass2-C:45`, i.e. a carried-forward finding not addressed. **Author-confirmed: 4.**
- **Both oracles derive their ID set from the very index table whose incompleteness is a finding**
  (A/F2, C/O9), so R1/R3/S-IDGREP under-scope by 3 of 21 IDs and S-IDGREP's containment check is
  **circular**. It also makes `0-baseline.md` B2's stated capture command false for 3 rows.

**A and B independently filed the position finding** (A/F1, B/L12): the confirmed-closed 3/3 position major
was ported with its **"updated rationale"** half deleted, while D16 adds a **fourth** rule to a block whose
closing parenthetical enumerates **three** — re-creating the exact defect cycle 1 closed, in a spot no
criterion observes (not a B4 CHANGE row ⇒ R2 blind; no ID token ⇒ R1 blind; SC3 asserts order without ever
stating **what** the order must be).

**All three frames independently reached the same conclusion about the honest core:** BIND's node-hash
clause is a genuine class-(i) win, the **root carve-out that killed cycle 1's pass 2 is really fixed**, IDN
is closed and cannot deadlock or be gamed, the three ratifications are **valid artifacts**, and the illegal
*"declared deferral"* route is genuinely absent. Cycle 1's *own* capped sections are closed or declared —
the new blockers are in **new** territory.

---

## Ranked list (cross-arm, worst first)

| # | ID | Sev | Claim | Cite |
|---|---|---|---|---|
| 1 | **B/L1** | **blocker** | HG2's operand is unproducible in a single-leaf run; the stage-5 terminus reads what only a stage-7 write can trigger | `2-plan.md:41,308-313`; `stage-6:13-14`; `stage-7:3-6` |
| 2 | **B/L2** | **blocker** | The catalog lock has no release; run 1 deadlocks against its own acquisition; `class (i)` hid the missing producer | `2-plan.md:43,198`; grep=0 |
| 3 | **C/O1** | **blocker** | `ruleid-sitemap.sh:34` is `exit 0` — R1's only oracle has no failure path (total site erosion → exit 0) | `oracles/ruleid-sitemap.sh:34`; mutation A |
| 4 | **C/O2** | **blocker** | R1 is a file-level token-mention check; deleting the operative rule left output byte-identical | `oracles/ruleid-sitemap.sh:29`; mutation B |
| 5 | **C/O3** | **blocker** | `check.sh` corpus unpinned; the baseline replay tree includes `changes/`, so 3 positives pass at baseline and 2 sweeps become unsatisfiable | measured, confirmed |
| 6 | **C/O4** | **blocker** | X protocol = one probe per arm from two different agents; p≈0.25 lucky split; X2 carries 3 criteria | `1.5-criteria.md:363-365` vs `stage-1.5.md:72-75` |
| 7 | **C/O6** | **blocker** | ~11 P rows describe rather than pin the operative sentence; 3 are satisfiable by text stating the opposite rule | `1.5-criteria.md:24-26,41-48,69-71,89-90` |
| 8 | **A/F2 ∥ C/O9** | major | Both oracles take their ID set from the index under test ⇒ R1/R3 under-scope 3 of 21; S-IDGREP is circular; B2's provenance false | `ruleid-sitemap.sh:17`, `idcollide.sh:25` |
| 9 | **A/F3** | major | Deferring the `_status.md` schema while D8 removes `index.md`'s writers strands `template used` with **no destination** | `2-plan.md:195`; the 3 sites confirmed |
| 10 | **A/F1 ∥ B/L12** | major | The confirmed-closed position fix lost its "updated rationale" half; D16 adds a 4th rule to a block whose rationale enumerates 3; SC3 never states the required order | `SKILL.md:39-41`; `1.5-criteria.md:311-320` |
| 11 | **B/L11** | major | `SKILL.md:3` will still say the human gate is "the top-level split **ONLY**" — omitted from B4/P12 **and** D16's sites, while PRV rewrites that very line | confirmed |
| 12 | **B/L4** | major | HG2 is **bypassed by a restart**: three sites make `assembled-plan.md`'s existence mean "run complete"; none is a B4 CHANGE row | `stage-7:39-41`; `stage-8:14-15`; `METHODOLOGY.md:239` |
| 13 | **B/L7** | major | ≥2 in-place fixes make a node permanently un-gateable — no transitive rebind clause; the plan's own "four fixed minors" node is that state | `2-plan.md:74-77,118-120` |
| 14 | **B/L5** | major | *"stale ⇒ un-gated"* names a state with **no exit route**; immutability contradicts the restart amendment | `stage-5:22-34`; `2-plan.md:73,85-86` |
| 15 | **B/L8** | major | The parent-hash clause invalidates whole subtrees; the rescuing operand is untabulated; HG2 bounces make it reachable, unbounded and **uncapped** | `2-plan.md:68-71,197,303` |
| 16 | **B/L6** | major | BIND's binding operand stays **self-reported by the reviewed party** while IDN de-self-reports identity for that exact reason | `charter.md:96`; `2-plan.md:33,93-94` |
| 17 | **B/L3** | major | DEC's two-level condition needs `elc(grandparent)` — outside the reader's ECON surface, undefined at depth 1, untabulated | `2-plan.md:38,224`; `METHODOLOGY.md:178-184` |
| 18 | **A/F4** | major | PRV is admitted to scope on a **false** *"strictly subtractive"* rationale, and adds the never-closed positive overclaim with no limitation required | `1-spec.md:113-118`; `2-plan.md:158-163` |
| 19 | **A/F5** | major | **Undeclared** departure from the approved on-disk layout: `<node>/decisions.md` + relocated gate/route entries (only RST's departure is declared) | `2-plan.md:197`; approved record `:170,174-179` |
| 20 | **A/F6** | major | Four edits falsify `charter.md`'s fork-provenance blockquote (*"carried whole … DROPPED: nothing"*), which is handed to every reviewer verbatim; SC5 checks only presence + upstream hash | `charter.md:11-22,88,93-100` |
| 21 | **B/L9** | major | The accessor enumeration is **writer-only and undercounts**: `index.md` 6 sites not 4 and not "all parallel"; gate log 2 of 5; `<node>/plan.md` absent; **every** catalog reader uncovered; `BROKEN-BY` has no reader | own enumeration |
| 22 | **B/L10** | major | S-CNC's advisory relabel rests on a **false premise** — the catalog lock IS executable, and `initial-authoring/8-harness.md:55` records this repo already driving a real git catalog end-to-end | `2-plan.md:410-413` |
| 23 | **B/L13** | major | S-XPM's sweep spans **6** GBP-only terminus sites; D16 covers 3 and P11 names 3 — the sweep either fails the build or cannot fail | `stage-2:43-44`, `stage-3:55`, `stage-4:46` |
| 24 | **B/L14** | major | Ingest mode: `plan.md.ingested` is **read by stage 3** but is in no operand row, no closed set, and no deterministic-filename list ⇒ stage 3 deadlocks in the new mode | `2-plan.md:42,233-236`; `charter.md:81-83,97-99` |
| 25 | **B/L15** | major | HG2's approval is **agent-authored**, so *"never self-approved"* is a property its mechanism lacks — and unlike TOP, **no limitation is stated** | `2-plan.md:298-299`; `LOOP-STATE.md:194-195` |
| 26 | **C/O5** | major | X arms are **excerpt-fed** — anti-representative for SC3, whose whole threat lives in the full assembly; and SC3 is specified two incompatible ways | `1.5-criteria.md:311-319` vs `:361-362` |
| 27 | **C/O7** | major | B4's site lists under-scope R2: P3 cites 2 of **12** `clean-or-resolved` sites; P12 misses `METHODOLOGY.md:327` + `SKILL.md:3`; P15 misses `templates/seed/README.md:17-19` | measured |
| 28 | **C/O8** | major | `idcollide.sh` pre-blesses `TOPGATE`/`DECOMPOSITION` — **absent at `b08f5a9`** — as "baseline debt", so R3 cannot fire on this cycle's own likely collision | confirmed |
| 29 | **C/O10** | major | The phantom filter hardcodes `id = TOP`, **swallows real backtick-marked TOP sites**, and ignores the hyphen-compound class for every ID | mutations C, D |
| 30 | **C/O12** | major | S-RST's departure half, SC5 and R2's hand-diff are **inspection-only** gating verifications with no judge/scale/pass ⇒ `verified = no` per H7 | `1.5-criteria.md:217,288,327-332` |
| 31 | **C/O16 ∥ B/L-CH8** | major | **No criterion observes that a clean run terminates** now that HG2 blocks the terminus — cycle 1's carried-forward coverage challenge, reproduced one gate later and sharper | `1.5-criteria.md:336-344` |
| 32 | **A/F7 ∥ C/O11** | major→minor | *"8 occurrences across 5 files"* is **4**; a verbatim repeat of cycle 1's `pass2-C:45` | author-confirmed |
| 33 | B/L17, B/L18, B/L19, B/L20, B/L21, C/O13-15, C/O17-19, A/F8-F12 | minor / nitpick | 17 further findings — SPV still has no arm; leaf-level topological order not derivable from per-parent DAGs; `tree/root/_status.md` gains a writer whose naming is deferred; **the Layer-2 config still tells every cold reviewer that F8 is out of scope** (B/L20 — a manufactured future bounce); SPN's "five" is six + case unstated; the X-cluster sharing is an undeclared departure from config item (8); `LOOP-STATE.md:8-9` still carries the terminate rule R3 voided | see the verbatim records |
| — | **B/L16** | ~~major~~ **minor** | S-PRV's `PROVEN` sweep *"can never pass"* — **partially refuted** on spot-verify (uppercase `PROVEN` ∉ lowercase `provenance`); survives as *"`normalize()` never states case"*. **Contested and downgraded by the author, logged here** | CH6 above |

---

## What the reviewers confirmed CLOSED (so the next pass does not re-derive it)

| Item | Status | Confirmed by |
|---|---|---|
| **BIND's root carve-out** — cycle 1's pass-2 blocker | **CLOSED.** Holds for a decomposed tree's root too (the carve-out is on *"no parent exists"*, not on leaf-ness) | A, B |
| **`spawn_id` dispatcher-recorded + declared-degraded** | **CLOSED.** Cannot deadlock, cannot be gamed by self-report; cycle 1's un-gateable 3-identical rule genuinely dropped. Its **first live use worked**: 3 distinct dispatcher ids, 3 honest `unavailable` self-reports | A, B |
| **RES(a)↔BIND unified; `clean-fixed-in-place` assembles** | **CLOSED for n = 1**, open for n ≥ 2 (B/L7) | A, B |
| **The illegal *"declared deferral"* route** | **NOT REPRODUCED** anywhere, in any wording; the claim's grounding in `stage-8.md:55-60` is accurate | A, C |
| **The three owner ratifications (R1/R2/R3)** | **VALID ARTIFACTS** — A fetched records 694/699 itself; every answer string is an exact option label; **the owner rejected the author's `(Recommended)` option on R3**, which is affirmative evidence against the CH11 "resolved into the author's own pick" failure mode. RAT2 discipline done properly on the bounce mechanics | A |
| **`off_limits_paths` / OFL** | **INTACT and genuinely subtractive** | A |
| **DIV** | **Deferred and not claimed**; S-PRV asserts the opposite discipline | A |
| **The "two passes" ruling** | **Not treated as settled**; stays on the owner queue | A |
| **`elc` honestly relabelled; the single-level contradiction removed** | **CLOSED** | A |
| **stage-8's false *"no single global cursor"*** | **Correctly retired** | B |
| **B2/B3/B4's measured values** | **Largely correct and materially better than cycle 1's.** C re-derived all 21 site sets — every row matches. **C independently confirms cycle 2's B3 is right and cycle 1's B0.7 was wrong** | C |
| **The advisory label on S-CNC's interleaving** | **Legitimate for the prompt-instruction surfaces** (A and C both: no dodge) — **but false for the catalog**, which is executable (B/L10) | A, C, B |

---

## The pattern behind the blockers, named for the next pass

Three of the four defect families have **one shape**: *a rule whose satisfaction was asserted by the party
or the label that was supposed to be constrained.*

1. **`class (i)` became an exemption** rather than a discipline — and both blocker-α rows are rows that
   claimed it (B/L1's producer trigger, B/L2's missing release). The fix is not to abandon the principle
   (all three reviewers endorse it) but to make the **table adversarial**: every class-(i) row must name
   *the file whose existence it computes over* and *the stage that creates that file*, and no mutation may
   be labelled class (i).
2. **An oracle that prints is not an oracle that checks** (C/O1, C/O2) — the same defect cycle 1 shipped
   three times. The fix is an `EXPECTED_SITES` data file and a non-zero exit, which C costs at ~20 lines.
3. **A criterion that describes is not a criterion that pins** (C/O6) — and a corpus that is not pinned is
   a corpus the builder narrows until green (C/O3).
4. **A site list that is hand-selected is not a site list that is measured** (C/O7, B/L11, B/L13, A/F1) —
   every under-counted B4 row is a half-migration R2 cannot see. The fix is mechanical: grep the **old**
   operative phrase and record the measured set.
