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

echo "=== DUPLICATION mutants (shared_spans.py — the NEGATIVE assertion ruleplace.sh cannot express) ==="
# ruleplace.sh is entirely positive per-site assertions, so it structurally CANNOT see a rule restated in
# a second file: it passed 76/0 on a set carrying eight duplications. shared_spans.py is the negative
# assertion. Being an instrument that gates a result, it needs its own can-fail test, which is this.
SPANS="$SELF_DIR/shared_spans.py"
EXEMPT="$SELF_DIR/declared-duplications.jsonl"
spans_clean() { python3 "$SPANS" "$WORK/m" 7 --exempt-file "$EXEMPT" >/dev/null 2>&1; }

# (a) POSITIVE CONTROL: the unmutated set must come back clean, or every kill below is meaningless.
mk
if spans_clean; then echo "  ok   DUP control: CLEAN on the unmutated set (expected CLEAN)"; ok=$((ok+1))
else echo "  BAD  DUP control: the unmutated set already reports duplications"; bad=$((bad+1)); fi

# (b) KILL MUTANTS: copy a rule OUT of charter-common.md into each role file in turn. This is exactly the
#     defect class GATE-B2 found, injected deliberately. Every one must be caught.
while read -r target; do
    mk
    # take a real common-core rule sentence and restate it in the role file
    printf '\n%s\n' "A silent unilateral demotion is a violation and the reviewer's severity stands." \
        >> "$WORK/m/$target"
    if spans_clean; then
        echo "  BAD  DUP $target: SURVIVED (expected KILLED) — a common rule restated in a role file went unseen"
        bad=$((bad+1))
    else
        echo "  ok   DUP $target: KILLED (expected KILLED)"; ok=$((ok+1))
    fi
done <<'DUP'
redteam.md
redteam-plan.md
redteam-split.md
divider.md
combiner.md
leaf.md
node.md
DUP

# (c) ROLE-TO-ROLE mutant: clause 2 of the composition rule, injected between two role files.
mk
printf '\n%s\n' "Write each step at the floor: fine enough that a competent practitioner can execute it without further planning, and no finer." >> "$WORK/m/node.md"
if spans_clean; then
    echo "  BAD  DUP role-to-role: SURVIVED (expected KILLED) — leaf.md's rule restated in node.md went unseen"; bad=$((bad+1))
else
    echo "  ok   DUP role-to-role: KILLED (expected KILLED)"; ok=$((ok+1))
fi

# (d) EXEMPTION NEGATIVE CONTROL: the register must not be a blanket amnesty. Re-adding the DECLARED B18
#     line to a third file is still a duplication of a span the register exempts — if the register made the
#     span globally legal this would be missed. Expected KILLED via the un-exempted neighbours it creates.
mk
printf '\n%s\n' "You are graded on **precision** — are your findings real? — not on how many you raise." >> "$WORK/m/leaf.md"
if spans_clean; then
    echo "  BAD  DUP exemption: SURVIVED (expected KILLED) — the register is a global amnesty, not per-pair"; bad=$((bad+1))
else
    echo "  ok   DUP exemption: KILLED (expected KILLED)"; ok=$((ok+1))
fi

echo "=== IN-PLACE NEGATION mutants (narrow: see the header comment; append-inversion is NOT covered) ==="
# WHAT THIS CLASS DOES AND DOES NOT PROVE -- read before citing its count.
#
# It rewrites a rule into its opposite IN PLACE, destroying the pinned substring, so the rule's probe must
# die. That is a real check on ONE thing: a probe whose pattern matches the TOPIC but not the POLARITY
# ("demote" rather than "You do not demote") would survive, and this catches it.
#
# IT DOES NOT PROVE THE SUITE DETECTS INVERSION. Reviewer S showed the attack that matters is to APPEND a
# superseding clause and leave every pinned substring intact:
#     charter-common.md += "CORRECTION: ... a hard backstop cap now applies and the floor may be relaxed"
#     combiner.md       += "Superseding clause: where two inputs disagree, discard the minority item"
#   -> 123 passed, 0 failed, and 0 undeclared shared spans. Both safety rules inverted, nothing moved.
# Because every probe is a substring grep, NO `present` probe can catch that, and adding more probes of the
# same kind cannot help -- one appended clause defeats each new one identically.
#
# An earlier version of this comment claimed the underlying defect was COVERAGE not sensitivity. That was
# WRONG: the rules S inverted do have probes (N-09b, N-12a, N-27f). The defect is sensitivity, and it is
# structural to the probe kind.
#
# THE CLASS IS THEREFORE NOT EXTENDED, per the owner's testing rule (record 2544): this mechanism is at its
# iteration limit, and a fifth variant would be the "increasingly elaborate test mechanism" that rule names.
# SEMANTIC INVERSION IS A COLD-REVIEWER ORACLE, not a script one -- reviewer S found it by reading, in
# minutes, which is the same venue answer already taken for fork fidelity (N-03) and paraphrase detection.
negate() { # $1=file  $2=original sentence  $3=inverted sentence
    mk
    if ! grep -qF -- "$2" "$WORK/m/$1"; then
        echo "  BAD  IN-PLACE NEGATION [$1]: source sentence absent -- $2"; bad=$((bad+1)); return
    fi
    python3 -c 'import sys;p,o,n=sys.argv[1:4];s=open(p).read();open(p,"w").write(s.replace(o,n))' \
        "$WORK/m/$1" "$2" "$3"
    if "$CHECK" "$WORK/m" "$RULES" >/dev/null 2>&1; then
        echo "  BAD  IN-PLACE NEGATION [$1]: SURVIVED (expected KILLED) -- '$3' passes the suite"; bad=$((bad+1))
    else
        echo "  ok   IN-PLACE NEGATION [$1]: KILLED (expected KILLED)"; ok=$((ok+1))
    fi
}
negate charter-common.md "Cite or it doesn't count." "Cite nothing; citations do not count."
negate charter-common.md "No role may quietly lower one." "Any role may quietly lower one."
negate charter-common.md "An unchecked claim is never thereby a verified one." "An unchecked claim is thereby a verified one."
negate combiner.md       "You do not demote." "You SHOULD demote freely."
negate combiner.md       "DISCARD NOTHING." "DISCARD FREELY."
negate combiner.md       "You filter. You do not re-rank." "You filter. You SHOULD re-rank."
negate leaf.md           "Never write below the floor" "Always write below the floor"
negate node.md           "You do not plan." "You SHOULD plan."

echo "==== mutants behaving as expected: $ok ; unexpected: $bad ===="
[ "$bad" -eq 0 ] || exit 1
exit 0
