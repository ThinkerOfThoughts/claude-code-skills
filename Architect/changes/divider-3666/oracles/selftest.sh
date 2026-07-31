#!/usr/bin/env bash
# Oracle self-test: show that check.sh CAN FAIL.
#
#  Part 1 - CHANGE assertions: run check.sh against the frozen control (git show cf16967:<path>).
#           Every C1/C2/C3/C5/C6 assertion and every C4 refutation MUST fail there.
#  Part 2 - CARRY assertions: they pass on both revisions by design, so each is instead
#           self-tested by DELETING its asserted line from a scratch copy of the NEW file
#           and confirming the assertion fires.
#
# Usage: selftest.sh   (run from anywhere; paths are derived from the repo root)

set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../../.." && pwd)"      # -> worktree root
CHECK="$HERE/check.sh"
CONTROL_REV="cf16967"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "repo root: $ROOT"
echo "control:   $CONTROL_REV"
echo

# ---------- Part 1: the control ----------
mkdir -p "$TMP/control"
for f in divider.md redteam-split.md common.md node.md; do
  git -C "$ROOT" show "$CONTROL_REV:Architect/stages/$f" > "$TMP/control/$f" || exit 1
done
git -C "$ROOT" show "$CONTROL_REV:Architect/SKILL.md" > "$TMP/control/SKILL.md" || exit 1

echo "=== PART 1 — check.sh against the frozen control (expect the CHANGE assertions to FAIL) ==="
bash "$CHECK" "$TMP/control" > "$TMP/control.out" 2>&1
CTRL_RC=$?
grep -E '^(FAIL|pass) (C1|C2|C3|C4|C5|C6)' "$TMP/control.out"
echo "control exit code: $CTRL_RC  (non-zero required)"
echo

CHANGE_IDS="C1a C1b C1c C1d C2 C3 C5a C5b C6 C4a C4c C4d C4f"
# C4b (six lenses in divider.md) and C4e (earned-clean in redteam-split.md) cannot fail on the
# control -- the strings live in redteam.md, which the control divider/redteam-split never held.
# They are refutations, so they are self-tested by INSERTION below instead.
P1FAIL=0
for id in $CHANGE_IDS; do
  if ! grep -q "^FAIL $id " "$TMP/control.out"; then
    echo "!! PRINTER: assertion $id passed on the control — it cannot fail"
    P1FAIL=1
  fi
done
[ $P1FAIL -eq 0 ] && echo "Part 1 OK: all $(echo $CHANGE_IDS | wc -w) CHANGE assertions fired on the control."
echo

# ---------- Part 2: line-deletion mutants for the CARRY assertions ----------
echo "=== PART 2 — CARRY assertions, line-deletion mutants (expect each to FAIL on its mutant) ==="
# id:file:grep-pattern-of-the-line-to-delete
# id|file|fixed-string-of-the-line-to-delete
read -r -d '' MUTANTS <<'EOM'
C7a|divider.md|genuinely at the floor
C7b|divider.md|FAILED_TO_DIVIDE
C7c|divider.md|This is not
C8a|divider.md|Four rounds** (owner ruling, record 3438)
C8b|divider.md|2-of-3
C9a|divider.md|You are given no plan
C9b|redteam-split.md|There is no plan
C10a|redteam-split.md|task** that was divided
C10b|redteam-split.md|granularity floor** for the run
C11a|redteam-split.md|Do not reject for missing detail
C11b|redteam-split.md|not required to be detailed
C11c|redteam-split.md|subdivides forever
C12|redteam-split.md|Not on how many problems you raise
C13|divider.md|sub-task carries the source
C14a|divider.md|concurrently and blind
C14b|redteam-split.md|concurrently and blind
C23|node.md|Checkpoint 0
C1a|redteam-split.md|Is this split at a natural seam
C2|redteam-split.md|A one-line approval is a correct output
C3|divider.md|Find a natural seam in the given task
C6|common.md|This section binds the roles
EOM
P2FAIL=0
NMUT=0
while IFS='|' read -r id f pat; do
  [ -z "${id:-}" ] && continue
  case "$id" in \#*) continue;; esac
  NMUT=$((NMUT+1))
  rm -rf "$TMP/mut"; mkdir -p "$TMP/mut"
  for g in divider.md redteam-split.md common.md node.md; do
    cp "$ROOT/Architect/stages/$g" "$TMP/mut/$g"
  done
  cp "$ROOT/Architect/SKILL.md" "$TMP/mut/SKILL.md"
  grep -vF -- "$pat" "$ROOT/Architect/stages/$f" > "$TMP/mut/$f"
  if [ "$(wc -l < "$TMP/mut/$f")" -eq "$(wc -l < "$ROOT/Architect/stages/$f")" ]; then
    echo "!! mutant for $id deleted nothing (pattern did not match) - assertion untested"
    P2FAIL=1; continue
  fi
  bash "$CHECK" "$TMP/mut" > "$TMP/mut.out" 2>&1
  if grep -q "^FAIL $id " "$TMP/mut.out"; then
    echo "pass  $id fired on its mutant (deleted: $pat)"
  else
    echo "!! PRINTER: $id did NOT fire when its line was deleted from $f"
    P2FAIL=1
  fi
done <<< "$MUTANTS"
echo "Part 2: $NMUT mutants run."
echo
echo "=== PART 2b - refutations self-tested by INSERTION (C4b, C4e) ==="
insert_test() {  # id file text
  local id="$1" f="$2" txt="$3"
  rm -rf "$TMP/ins"; mkdir -p "$TMP/ins"
  for g in divider.md redteam-split.md common.md node.md; do cp "$ROOT/Architect/stages/$g" "$TMP/ins/$g"; done
  cp "$ROOT/Architect/SKILL.md" "$TMP/ins/SKILL.md"
  printf '\n%s\n' "$txt" >> "$TMP/ins/$f"
  bash "$CHECK" "$TMP/ins" > "$TMP/ins.out" 2>&1
  if grep -q "^FAIL $id " "$TMP/ins.out"; then
    echo "pass  $id fired when \"$txt\" was inserted into $f"
  else
    echo "!! PRINTER: $id did NOT fire when \"$txt\" was inserted into $f"
    P2FAIL=1
  fi
}
insert_test C4b divider.md       "Return a verdict for each of the six lenses."
insert_test C4e redteam-split.md "A clean factual lens must be earned with citations."
echo

# ---------- verdict ----------
if [ $P1FAIL -eq 0 ] && [ $P2FAIL -eq 0 ] && [ $CTRL_RC -ne 0 ]; then
  echo "SELF-TEST PASS — every assertion has been shown able to fail."
  exit 0
fi
echo "SELF-TEST FAIL — see the '!!' lines above; those criteria are verified = no."
exit 1
