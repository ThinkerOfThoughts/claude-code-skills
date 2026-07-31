#!/usr/bin/env bash
# ruleplace.sh — per-FILE positive assertions over Architect's agent prompt set.
#
# The only thing this element changed is WHICH FILE each rule lives in, so every probe is scoped to one
# file. A probe that grepped the whole set would measure presence, not placement, and would survive the
# relocation mutants in mutation-test.sh.
#
# Usage: ruleplace.sh <set-dir> [rules.tsv]
# Exit:  0 = all assertions held
#        1 = at least one assertion failed
#        2 = usage error   <-- deliberately distinct from 0, so a no-argument call cannot read as a pass
set -u

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "$#" -lt 1 ]; then
    echo "usage: $0 <set-dir> [rules.tsv]" >&2
    echo "  <set-dir> is the directory holding charter.md, charter-common.md, redteam.md, redteam-plan.md," >&2
    echo "  redteam-split.md, divider.md, combiner.md, leaf.md, node.md" >&2
    exit 2
fi
SET_DIR="$1"
RULES="${2:-$SELF_DIR/rules.tsv}"
[ -d "$SET_DIR" ] || { echo "not a directory: $SET_DIR" >&2; exit 2; }
[ -f "$RULES" ]   || { echo "no rules file: $RULES" >&2; exit 2; }

FILES="charter.md charter-common.md redteam.md redteam-plan.md redteam-split.md divider.md combiner.md leaf.md node.md"

# Normalize: strip markdown emphasis/code markers, flatten every line break to a space, squeeze runs.
# An unnormalized grep for a rule that wraps across a line break reports a false absence.
# NOTE: '_' is NOT stripped. Stripping it as an emphasis marker destroys every identifier in the spec
# (Human_gate, work_queue, node_id, Memo_read) and produced five false absences on the first run.
norm() { sed -e 's/^> \{0,1\}//' -e 's/^ *[-|] *//' "$1" | tr -d '*`' | tr '\n' ' ' | tr -s ' '; }

NORMDIR="$(mktemp -d)"
trap 'rm -rf "$NORMDIR"' EXIT
for f in $FILES; do
    if [ -f "$SET_DIR/$f" ]; then norm "$SET_DIR/$f" > "$NORMDIR/$f"; else : > "$NORMDIR/$f"; fi
done
cat "$NORMDIR"/*.md > "$NORMDIR/_ALL"
# The DISPATCHED files. charter.md is a manifest and is never given to an agent.
DISPATCHED="charter-common.md redteam.md redteam-plan.md redteam-split.md divider.md combiner.md leaf.md node.md"
for f in $DISPATCHED; do cat "$NORMDIR/$f"; done > "$NORMDIR/_DISPATCHED"

pass=0; fail=0; smoke=0; failed_ids=""

while IFS=$'\t' read -r id mode file anchor pattern; do
    case "$id" in ''|\#*) continue ;; esac
    case "$mode" in
        present)
            if grep -Eq -- "$pattern" "$NORMDIR/$file"; then
                echo "PASS  $id  present in $file"; pass=$((pass+1))
            else
                echo "FAIL  $id  NOT present in $file  -- /$pattern/"; fail=$((fail+1)); failed_ids="$failed_ids $id"
            fi ;;
        absent)
            if grep -Eq -- "$pattern" "$NORMDIR/$file"; then
                echo "FAIL  $id  forbidden text present in $file  -- /$pattern/"; fail=$((fail+1)); failed_ids="$failed_ids $id"
            else
                echo "PASS  $id  absent from $file"; pass=$((pass+1))
            fi ;;
        lastline)
            # N-14: PLACEMENT, not presence. The raw file's last non-blank line must match.
            # Presence probes structurally cannot see this -- B18 was present in the set the whole time
            # while N-14 named the wrong two files, and no probe could tell.
            ll=$(grep -v '^[[:space:]]*$' "$SET_DIR/$file" | tail -1)
            if printf '%s' "$ll" | tr -d '*`' | grep -Eq -- "$pattern"; then
                echo "PASS  $id  is the final line of $file"; pass=$((pass+1))
            else
                echo "FAIL  $id  NOT the final line of $file  -- got: $ll"; fail=$((fail+1)); failed_ids="$failed_ids $id"
            fi ;;
        absent-set)
            if grep -Eq -- "$pattern" "$NORMDIR/_ALL"; then
                hit=$(for f in $FILES; do grep -Eq -- "$pattern" "$NORMDIR/$f" && echo -n "$f "; done)
                echo "FAIL  $id  forbidden text present in set ($hit) -- /$pattern/"; fail=$((fail+1)); failed_ids="$failed_ids $id"
            else
                echo "PASS  $id  absent from whole set"; pass=$((pass+1))
            fi ;;
        absent-dispatched)
            if grep -Eq -- "$pattern" "$NORMDIR/_DISPATCHED"; then
                hit=$(for f in $DISPATCHED; do grep -Eq -- "$pattern" "$NORMDIR/$f" && echo -n "$f "; done)
                echo "FAIL  $id  forbidden text present in dispatched files ($hit) -- /$pattern/"; fail=$((fail+1)); failed_ids="$failed_ids $id"
            else
                echo "PASS  $id  absent from all dispatched files"; pass=$((pass+1))
            fi ;;
        *) echo "FAIL  $id  unknown mode '$mode'"; fail=$((fail+1)); failed_ids="$failed_ids $id" ;;
    esac
done < "$RULES"

# ---- N-03 allocation-table SMOKE, GENERATED from charter.md's own allocation table --------------------
# The artifact claims a destination file for every fork-source rule B01-B19. Parse that claim out of the
# artifact and verify each one by reading the named file. The probe set is therefore derived from the
# artifact, not from the run's inventory, so an inventory gap cannot hide a missing rule here.
echo "--- N-03 SMOKE ONLY: allocation-table destinations exist (NOT fork-fidelity verification) ---"
echo "    Fork fidelity is verified by a cold reviewer rule-by-rule; reviewer Q measured this probe passing"
echo "    9 of 19 rules against files they were never claimed to be in. Counted separately, below."
claimed=0
smokefail=0
while IFS='|' read -r _ rulecell filecell _; do
    rid=$(echo "$rulecell" | grep -oE 'B[0-9]{2}' | head -1)
    [ -n "$rid" ] || continue
    claimed=$((claimed+1))
    targets=$(echo "$filecell" | grep -oE '[a-z-]+\.md' | sort -u)
    if [ -z "$targets" ]; then
        echo "SMOKE-FAIL  N-03/$rid  allocation table names no destination file"; smokefail=$((smokefail+1))
        continue
    fi
    # The rule's DESCRIPTION, taken from the same table cell, is the search term. Asserting only that the
    # destination file is non-empty would pass for any set of seven non-empty files — this project has
    # shipped that class of probe three times. The term is still GENERATED from the artifact, so an
    # inventory gap cannot hide behind a probe set derived from the inventory.
    desc=$(echo "$rulecell" | sed -e 's/\*\*B[0-9]\{2\}\*\*//' -e 's/[^A-Za-z ]/ /g' | tr 'A-Z' 'a-z' | tr -s ' ')
    for t in $targets; do
        if [ ! -s "$NORMDIR/$t" ]; then
            echo "SMOKE-FAIL  N-03/$rid  destination $t missing or empty"; smokefail=$((smokefail+1))
            continue
        fi
        hits=0; words=0
        for w in $desc; do
            [ "${#w}" -gt 3 ] || continue          # skip 'the', 'or', 'a' — they carry no evidence
            words=$((words+1))
            grep -qi -- "$w" "$NORMDIR/$t" && hits=$((hits+1))
        done
        if [ "$words" -eq 0 ]; then
            echo "SMOKE-FAIL  N-03/$rid  allocation table gives no describable rule text"; smokefail=$((smokefail+1))
        elif [ $((hits * 100 / words)) -ge 60 ]; then
            echo "SMOKE N-03/$rid  $hits/$words description terms present in $t"; smoke=$((smoke+1))
        else
            echo "SMOKE-FAIL  N-03/$rid  only $hits/$words description terms present in $t -- rule may not be stated there"
            smokefail=$((smokefail+1))
        fi
    done
done < <(sed -n '/^| \*\*B01\*\*/,/^| \*\*B19\*\*/p' "$SET_DIR/charter.md")
if [ "$claimed" -ne 19 ]; then
    echo "SMOKE-FAIL  N-03  allocation table covers $claimed rules, expected 19 (B01-B19)"; smokefail=$((smokefail+1))
else
    echo "SMOKE N-03  allocation table covers all 19 fork-source rules"; smoke=$((smoke+1))
fi

# ---- N-32: no probe ID is reused. The criterion NAMES this command; until 2026-07-30 nothing ran it.
dups=$(cut -f1 "$RULES" | grep -v '^#' | sort | uniq -d)
if [ -n "$dups" ]; then
    echo "FAIL  N-32  probe ids reused:$(echo $dups)"; fail=$((fail+1)); failed_ids="$failed_ids N-32"
else
    pass=$((pass+1))
fi

echo "==== $pass passed, $fail failed ===="
echo "==== plus $smoke N-03 SMOKE passes and $smokefail SMOKE failures, NEITHER counted above (retired as the fidelity oracle: it does not gate in EITHER direction) ===="
[ "$fail" -eq 0 ] || { echo "failed:$failed_ids"; exit 1; }
exit 0
