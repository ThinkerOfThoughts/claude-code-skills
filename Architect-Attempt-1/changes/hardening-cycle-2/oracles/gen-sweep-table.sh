#!/usr/bin/env bash
# gen-sweep-table.sh — JOINS the GENERATED row set (gen-sweep-rows.sh) with the AUTHORED answers
# (sweep-answers.tsv) and emits 2-plan.md §1's table.
#
# TOTALITY IS ENFORCED, NOT CLAIMED. Pass 2's §1 headline said "every predicate and gate, baseline rules
# included" while 15 of 21 baseline IDs had no row. This script EXITS 1 if:
#   * any generated row has no authored answer  (a predicate silently dropped), or
#   * any authored answer has no generated row  (an answer to a predicate that no longer exists).
# So the table cannot be shipped partial, and the row set still cannot be authored by hand.
set -uo pipefail
D="$(cd "$(dirname "$0")" && pwd)"
GEN=$("$D/gen-sweep-rows.sh")
mapfile -t IDS < <(awk -F'|' '/^\| [0-9]+ \|/{gsub(/[ *]/,"",$3); print $3}' <<<"$GEN")
mapfile -t SRC < <(awk -F'|' '/^\| [0-9]+ \|/{sub(/^ */,"",$4); sub(/ *$/,"",$4); print $4}' <<<"$GEN")
declare -A A
while IFS=$'\t' read -r id a b c v; do
  case "$id" in ''|'#'*) continue ;; esac
  A["$id"]=$(printf '%s\t%s\t%s\t%s' "$a" "$b" "$c" "$v")
done < "$D/sweep-answers.tsv"

rc=0; missing=(); orphan=()
for id in "${IDS[@]}"; do [ -n "${A[$id]+x}" ] || missing+=("$id"); done
for id in "${!A[@]}"; do
  found=0; for g in "${IDS[@]}"; do [ "$g" = "$id" ] && { found=1; break; }; done
  [ $found -eq 1 ] || orphan+=("$id")
done

echo "| # | Predicate / gate | source | (a) producer provably earlier? | (b) degenerate: n=1 · root · first run · empty | (c) counterpart / release | verdict |"
echo "|---|---|---|---|---|---|---|"
n=0
for i in "${!IDS[@]}"; do
  id="${IDS[$i]}"; n=$((n+1))
  if [ -n "${A[$id]+x}" ]; then IFS=$'\t' read -r a b c v <<<"${A[$id]}"
  else a="**UNANSWERED**"; b="**UNANSWERED**"; c="**UNANSWERED**"; v="**UNANSWERED**"; fi
  printf '| %s | **%s** | %s | %s | %s | %s | %s |\n' "$n" "$id" "${SRC[$i]}" "$a" "$b" "$c" "$v"
done
echo
# VERDICT TALLY — generated, because pass 3's first draft TYPED these counts and got them wrong
# (typed 55/20/4/4; measured 64/15/4/3). A tally that is typed is a tally that drifts.
for id in "${IDS[@]}"; do
  v="unanswered"; [ -n "${A[$id]+x}" ] && { IFS=$'\t' read -r _ _ _ v <<<"${A[$id]}"; }
  case "$v" in FIXED*) echo FIXED ;; PARTIAL*) echo PARTIAL+DECLARED ;; "DECLARED GAP"*) echo "DECLARED GAP" ;;
    OK*) echo OK ;; *) echo UNANSWERED ;; esac
done | sort | uniq -c | awk '{printf "VERDICT TALLY: %-18s %s\n", $2" "$3, $1}'
echo "ROWS EMITTED: $n   (generated row set: ${#IDS[@]}; authored answers: ${#A[@]})"
if [ ${#missing[@]} -gt 0 ]; then echo "SWEEP: FAIL — generated rows with NO authored answer: ${missing[*]}"; rc=1; fi
if [ ${#orphan[@]}  -gt 0 ]; then echo "SWEEP: FAIL — authored answers with NO generated row: ${orphan[*]}"; rc=1; fi
[ $rc -eq 0 ] && echo "SWEEP: OK — the row set is generated and every generated row is answered (totality enforced, not asserted)"
exit $rc
