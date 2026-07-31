#!/usr/bin/env bash
# GENERATES the skeleton of 2-plan.md §1's sweep: ONE ROW PER PREDICATE, total BY CONSTRUCTION.
# The row set = the 21 live baseline rule IDs (from expected-sites.txt, itself generated) + every NEW
# criterion id (from criteria.tsv) + the predicates that carry no rule ID, listed in NO_ID below because
# an ID-driven generator cannot see them — which is the residual pass 2's reviewers named.
set -uo pipefail
D="$(cd "$(dirname "$0")" && pwd)"
NO_ID="closed-input-set stage-done-iff-output-exists path-validation catalog-pending run-end"
echo "| # | Predicate / gate | source | (a) producer provably earlier? | (b) degenerate: n=1 / root / first run / empty | (c) counterpart / release |"
echo "|---|---|---|---|---|---|"
n=0
for id in $(grep -v '^#' "$D/expected-sites.txt" | awk '{print $1}'); do n=$((n+1)); echo "| $n | **$id** | baseline rule ID | | | |"; done
for id in $(grep -v '^#' "$D/criteria.tsv" | awk -F'\t' '($2=="NEW"||$2=="COOC"){print $1}'); do n=$((n+1)); echo "| $n | **$id** | new criterion | | | |"; done
for p in $NO_ID; do n=$((n+1)); echo "| $n | **$p** | PREDICATE WITH NO RULE ID (invisible to an ID-driven generator — listed explicitly) | | | |"; done
echo; echo "TOTAL ROWS REQUIRED: $n"
