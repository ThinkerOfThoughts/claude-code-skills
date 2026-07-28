#!/usr/bin/env bash
# mutation-test.sh — demonstrate that ruleplace.sh CAN FAIL.
#
# A checker that passes every input is a printer, not an oracle. This project shipped that exact defect
# twice. Four mutant classes:
#   DELETION    remove the rule's anchor line(s) from its owning file        -> its assertion must be KILLED
#   RELOCATION  move the anchor line(s) into a DIFFERENT file in the set     -> its assertion must be KILLED
#               (this is the class the re-scope makes necessary: a probe that grepped the whole set would
#                SURVIVE relocation, and would be measuring presence rather than placement)
#   INSERTION   append forbidden text (the correct mutant for an absence sweep, where deletion is undefined)
#   CONTROL     delete a line no probe asserts                               -> the suite must still PASS,
#               so the harness is observed printing a non-kill at least once
#
# Usage: mutation-test.sh <set-dir>
# Exit:  0 = every mutant behaved as expected   1 = at least one did not   2 = usage error
set -u
SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
[ "$#" -ge 1 ] || { echo "usage: $0 <set-dir>" >&2; exit 2; }
SRC="$(cd "$1" && pwd)" || exit 2
CHECK="$SELF_DIR/ruleplace.sh"
RULES="$SELF_DIR/rules.tsv"

WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
mk() { rm -rf "$WORK/m"; mkdir -p "$WORK/m"; cp "$SRC"/*.md "$WORK/m"/; }
# Does ruleplace.sh report $1 as FAILing on the current mutant?
killed() { "$CHECK" "$WORK/m" "$RULES" 2>&1 | grep -q "^FAIL  $1  "; }

ok=0; bad=0
report() { # $1=class $2=id $3=expected $4=actual
    if [ "$3" = "$4" ]; then echo "  ok   $1 $2: $4 (expected $3)"; ok=$((ok+1))
    else echo "  BAD  $1 $2: $4 (expected $3)"; bad=$((bad+1)); fi
}

echo "=== DELETION mutants ==="
while IFS=$'\t' read -r id mode file anchor pattern; do
    case "$id" in ''|\#*) continue ;; esac
    [ "$mode" = present ] || continue
    mk
    if ! python3 "$SELF_DIR/delete_span.py" "$SRC/$file" "$anchor" "$WORK/m/$file" >/dev/null; then
        echo "  BAD  DELETION $id: anchor not present in normalized $file"; bad=$((bad+1)); continue
    fi
    if killed "$id"; then report DELETION "$id" KILLED KILLED; else report DELETION "$id" KILLED SURVIVED; fi
done < "$RULES"

echo "=== RELOCATION mutants (sample) ==="
for id in N-09c N-09d N-09e N-11a N-12a N-13e N-19a; do
    line=$(grep -P "^\Q$id\E\t" "$RULES") || { echo "  BAD  RELOCATION $id: not in rules.tsv"; bad=$((bad+1)); continue; }
    file=$(echo "$line" | cut -f3); anchor=$(echo "$line" | cut -f4)
    # move it into a file that is NOT the owner
    for cand in leaf.md node.md divider.md; do [ "$cand" != "$file" ] && dest="$cand" && break; done
    mk
    python3 "$SELF_DIR/delete_span.py" "$SRC/$file" "$anchor" "$WORK/m/$file" >/dev/null || \
        { echo "  BAD  RELOCATION $id: anchor not found"; bad=$((bad+1)); continue; }
    # append the removed span to the destination file, so the rule is PRESENT IN THE SET but in the wrong file
    diff "$SRC/$file" "$WORK/m/$file" | sed -n 's/^< //p' >> "$WORK/m/$dest"
    if killed "$id"; then report "RELOCATION($file->$dest)" "$id" KILLED KILLED
    else report "RELOCATION($file->$dest)" "$id" KILLED SURVIVED; fi
done

echo "=== INSERTION mutants (the correct mutant for an absence sweep) ==="
# id : target file : text inserted
while IFS='|' read -r id dest text; do
    case "$id" in ''|\#*) continue ;; esac
    mk; printf '\n%s\n' "$text" >> "$WORK/m/$dest"
    if killed "$id"; then report INSERTION "$id" KILLED KILLED; else report INSERTION "$id" KILLED SURVIVED; fi
done <<'MUT'
N-02|redteam.md|> UNVETTED DRAFT — hand-written outside the loop.
N-11d|node.md|A severity may be contested via an entry logged against the node in the run's decision log.
N-17|charter-common.md|The full severity model is in `stages/stage-4.md`.
N-18|redteam.md|Roughly 85% of findings were caught by exactly one reviewer.
N-10e|redteam.md|nitpick — Style, wording, clarity.
MUT

echo "=== CONTROL mutant (expected SURVIVED — proves the harness can print a non-kill) ==="
mk
CTRL="You are a stack frame, not a service."
grep -qF -- "$CTRL" "$WORK/m/node.md" || { echo "  BAD  CONTROL: anchor text not found"; bad=$((bad+1)); }
grep -vF -- "$CTRL" "$SRC/node.md" > "$WORK/m/node.md"
if "$CHECK" "$WORK/m" "$RULES" >/dev/null 2>&1; then
    echo "  ok   CONTROL: SURVIVED (expected SURVIVED) — an unasserted line was deleted and the suite still passed"; ok=$((ok+1))
else
    echo "  BAD  CONTROL: KILLED (expected SURVIVED) — a probe is matching text no criterion claims"; bad=$((bad+1))
fi

echo "==== mutants behaving as expected: $ok ; unexpected: $bad ===="
[ "$bad" -eq 0 ] || exit 1
exit 0
