#!/usr/bin/env bash
# Conformance oracle for change `divider-3666`.
#
# Usage:  check.sh <dir-holding-the-files>
#   <dir> must contain: divider.md redteam-split.md common.md SKILL.md node.md
# Exit 0 = all assertions pass. Exit 1 = at least one failed.
#
# Every assertion is a POSITIVE per-site assertion except the C4 block, which is an
# absence sweep and is PAIRED with C1/C2/C3's positive assertions.
# All matching runs on NORMALISED text: markdown emphasis and backticks stripped,
# line wraps flattened, whitespace collapsed, lowercased.

set -uo pipefail
DIR="${1:?usage: check.sh <dir>}"
FAIL=0
PASSN=0

norm() {  # stdin -> one long normalised line
  sed -e 's/\*\*//g' -e 's/`//g' -e 's/_//g' -e 's/\*//g' "$1" \
    | tr '\n' ' ' | tr -s ' ' | tr '[:upper:]' '[:lower:]'
}

# assert <id> <file> <regex-that-must-be-PRESENT> <description>
assert() {
  local id="$1" f="$2" re="$3" desc="$4"
  if [ ! -f "$DIR/$f" ]; then echo "FAIL $id  ($f missing)"; FAIL=1; return; fi
  if norm "$DIR/$f" | grep -Eqi -- "$re"; then
    echo "pass $id  $f  :: $desc"; PASSN=$((PASSN+1))
  else
    echo "FAIL $id  $f  :: $desc"; FAIL=1
  fi
}

# refute <id> <file> <regex-that-must-be-ABSENT> <description>
refute() {
  local id="$1" f="$2" re="$3" desc="$4"
  if [ ! -f "$DIR/$f" ]; then echo "FAIL $id  ($f missing)"; FAIL=1; return; fi
  if norm "$DIR/$f" | grep -Eqi -- "$re"; then
    echo "FAIL $id  $f  :: still present: $desc"; FAIL=1
  else
    echo "pass $id  $f  :: absent: $desc"; PASSN=$((PASSN+1))
  fi
}

echo "=== CHANGE assertions (must FAIL on the cf16967 control) ==="

# C1 - the two questions + the verdict rule
assert C1a redteam-split.md 'is this split at a natural seam'                       "3666 question 1"
assert C1b redteam-split.md 'reduce the task past the point of maximum granularity'  "3666 question 2"
assert C1c redteam-split.md 'reject, saying which of the two questions failed'       "reject WITH EXPLANATION"
assert C1d redteam-split.md 'neither half below the floor .{0,20}approve'            "approve rule"

# C2 - a one-line approval is correct
assert C2  redteam-split.md 'a one-line approval is a correct output'                "short approval conforming"

# C3 - the divider's job, 3666
assert C3  divider.md 'find a natural seam in the given task, and split it into two pieces at that seam' "3666 divider instruction"

# C5 - dispatch names exactly common.md + redteam-split.md
assert C5a divider.md 'three cold agents concurrently on common.md \+ redteam-split.md' "divider dispatch pair"
assert C5b SKILL.md   '\| split reviewer \| stages/redteam-split.md \| the divider, 3 of them' "SKILL roles row"

# C6 - common.md severity scoped
assert C6  common.md 'this section binds the roles that produce or handle findings'     "severity model scoped"

echo "=== C4 absence sweep (paired with C1-C3 above) ==="
refute C4a redteam-split.md 'the six lenses'                 "six lenses"
refute C4b divider.md       'the six lenses'                 "six lenses"
refute C4c redteam-split.md '(blocker|nitpick)'              "severity vocabulary"
refute C4d divider.md       '(blocker|nitpick)'              "severity vocabulary"
refute C4e redteam-split.md 'must be earned'                 "earned-clean clause"
refute C4f divider.md       'while any major or blocker stands' "re-derive-on-standing-major"

echo "=== CARRY assertions (must pass on BOTH; self-tested by line deletion) ==="

# C7 - three distinct return values
assert C7a divider.md 'genuinely at the floor: no seam exists without a half falling below it' "null answer"
assert C7b divider.md 'failed_?to_?divide'                              "FAILED_TO_DIVIDE answer"
assert C7c divider.md 'this is not null'                              "the two are distinct"
# C8 - four rounds + 2-of-3
assert C8a divider.md 'four rounds \(owner ruling, record 3438\)'                                   "four-round cap"
assert C8b divider.md '2-of-3'                                        "2-of-3 fallback"
# C9 - no plan
assert C9a divider.md 'you are given no plan'                         "divider holds no plan"
assert C9b redteam-split.md 'there is no plan'                        "reviewer holds no plan"
# C10 - the reviewer's declared inputs
assert C10a redteam-split.md 'the task that was divided'              "holds the task"
assert C10b redteam-split.md 'the granularity floor for the run'      "holds the floor"
# C11 - floor bound on what may be called a defect
assert C11a redteam-split.md 'do not reject for missing detail'       "floor bound heading"
assert C11b redteam-split.md 'not required to be detailed'            "floor bound body"
assert C11c redteam-split.md 'subdivides forever'                     "infinite-regress reason"
# C12 - precision not volume
assert C12  redteam-split.md 'not on how many problems you raise'     "judged on precision"
# C13 - sub-tasks carry source material
assert C13  divider.md 'carries the source material'                  "record 3119"
# C14 - seam is not a handoff
assert C14a divider.md 'concurrently and blind'                       "no channel (divider)"
assert C14b redteam-split.md 'concurrently and blind'                 "no channel (reviewer)"
# C23 support - checkpoint 0 still in node.md
assert C23  node.md 'checkpoint 0'                                    "checkpoint 0 present"

echo
echo "passed: $PASSN   overall: $([ $FAIL -eq 0 ] && echo PASS || echo FAIL)"
exit $FAIL
