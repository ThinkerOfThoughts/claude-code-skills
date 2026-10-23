# <slug> — Plan Ledger

status: ACTIVE            <!-- ACTIVE | CLOSED -->
mode: normal              <!-- normal | cascade; set from the invocation or the config default (SKILL.md "Cascade mode"); a resume reads it -->
sheet_version: 0
owner: <name used in provenance tags>
spec: <path to the builder spec, once it exists>
invariants: <path>
created: <YYYY-MM-DD>

## Decisions (the sheet — current design only; one sentence per line; one provenance tag per line)
<!-- S1. <full sentence in the owner's meaning>  [<OWNER> <ts> "verbatim quote"]
     S2. <sentence>  [PROPOSED:<who> | CONFIRMED <ts> "quote"]
     S3. <sentence>  [PROPOSED:<who> | UNCONFIRMED]
     S4. <sentence>  [INHERITED:<file/table> | UNEXAMINED]
     S5. <sentence>  [DERIVED from S2]
     S6. <sentence>  [DERIVED: equivalent rewrite of <what>]    (cascade mode only)
     Direction-carrying lines are written "X runs first; Y runs only when <condition>." -->

## Open forks
<!-- F1. <mechanism-class choice, named plainly> — options as sentences — posed <ts> / OPEN / deferred by owner <ts> "quote" -->

## Owner questions
<!-- Q1. "<quote>" (<ts>) — answered <ts> "<quote of the answer>" | OPEN -->

## Invariants check
| # | Invariant (short) | holds / violates / n.a. | proving line |
|---|---|---|---|

## Adjacent goals
<!-- one sentence each, with source: why neighbouring work exists; the spec must not defeat these -->

## Approvals
<!-- sheet v<N> — <ts> "quote" ; hand-off — <ts> spec hash/commit -->

## Coordination log
<!-- <ts> <lane> → <lane>: one-line gist; spec line cited; ack <ts> -->

## Decisions log (stage routes)
<!-- <ts> stage <n>: worst severity, route taken, rationale + name for any override -->

## Cascade (only when cascade mode is on; omit this section otherwise)
principles sheet: <path>  approved: <ts "quote"> (recorded in the sheet's status line)
levels, top-down: <L1 name — status> | <L2 …>     <!-- order confirmed as a sentence -->
### Mechanism tally
<!-- <mechanism named plainly>: defining lines <S ids> | support lines <S ids> | latest pile-up verdict NOT / PILING UP -->
### Trio results
<!-- <ts> <level> <question>: votes, adopted answer, confidence, flags -> <record path in cascade.records_dir> -->
### Citation checks
<!-- <ts> <level>: counts per verdict; failures and the route taken; re-check <ts> -> <record path> -->
### Owner batches
<!-- <ts> <level>: posted; gap items; answered <ts> "quote"; sheet additions made -->

## Changelog (superseded lines, append-only)
<!-- <date> S<n> was "<old sentence>" → replaced by S<m> because <owner quote or finding> -->

## As built
<!-- filled at stage 8 -->

## Secret: <random hex, rotate on every material update>
