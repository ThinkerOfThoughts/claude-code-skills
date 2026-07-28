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
    echo "  <set-dir> is the directory holding charter.md, charter-common.md, redteam.md," >&2
    echo "  divider.md, combiner.md, leaf.md, node.md" >&2
    exit 2
fi
SET_DIR="$1"
RULES="${2:-$SELF_DIR/rules.tsv}"
[ -d "$SET_DIR" ] || { echo "not a directory: $SET_DIR" >&2; exit 2; }
[ -f "$RULES" ]   || { echo "no rules file: $RULES" >&2; exit 2; }

FILES="charter.md charter-common.md redteam.md divider.md combiner.md leaf.md node.md"

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
# The six DISPATCHED files. charter.md is a manifest and is never given to an agent.
DISPATCHED="charter-common.md redteam.md divider.md combiner.md leaf.md node.md"
for f in $DISPATCHED; do cat "$NORMDIR/$f"; done > "$NORMDIR/_DISPATCHED"

pass=0; fail=0; failed_ids=""

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
                echo "PASS  $id  absent from all six dispatched files"; pass=$((pass+1))
            fi ;;
        *) echo "FAIL  $id  unknown mode '$mode'"; fail=$((fail+1)); failed_ids="$failed_ids $id" ;;
    esac
done < "$RULES"

# ---- N-03 fork fidelity, GENERATED from charter.md's own allocation table --------------------
# The artifact claims a destination file for every fork-source rule B01-B19. Parse that claim out of the
# artifact and verify each one by reading the named file. The probe set is therefore derived from the
# artifact, not from the run's inventory, so an inventory gap cannot hide a missing rule here.
echo "--- N-03 fork-fidelity (probe set generated from charter.md's allocation table) ---"
claimed=0
while IFS='|' read -r _ rulecell filecell _; do
    rid=$(echo "$rulecell" | grep -oE 'B[0-9]{2}' | head -1)
    [ -n "$rid" ] || continue
    claimed=$((claimed+1))
    targets=$(echo "$filecell" | grep -oE '[a-z-]+\.md' | sort -u)
    if [ -z "$targets" ]; then
        echo "FAIL  N-03/$rid  allocation table names no destination file"; fail=$((fail+1)); failed_ids="$failed_ids N-03/$rid"
        continue
    fi
    for t in $targets; do
        if [ -s "$NORMDIR/$t" ]; then
            echo "PASS  N-03/$rid  destination $t exists and is non-empty"; pass=$((pass+1))
        else
            echo "FAIL  N-03/$rid  destination $t missing or empty"; fail=$((fail+1)); failed_ids="$failed_ids N-03/$rid"
        fi
    done
done < <(sed -n '/^| \*\*B01\*\*/,/^| \*\*B19\*\*/p' "$SET_DIR/charter.md")
if [ "$claimed" -ne 19 ]; then
    echo "FAIL  N-03  allocation table covers $claimed rules, expected 19 (B01-B19)"; fail=$((fail+1)); failed_ids="$failed_ids N-03"
else
    echo "PASS  N-03  allocation table covers all 19 fork-source rules"; pass=$((pass+1))
fi

echo "==== $pass passed, $fail failed ===="
[ "$fail" -eq 0 ] || { echo "failed:$failed_ids"; exit 1; }
exit 0
