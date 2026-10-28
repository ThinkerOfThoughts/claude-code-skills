#!/usr/bin/env bash
# baseline-replay.sh [base-commit] — THE CAN-FAIL SELF-TEST for the whole criteria family.
# Materialises the baseline artifact from git into a scratch tree, DELETES changes/ so the corpus pin is
# not merely trusted, and runs the SAME check.sh. Requires: every NEW row FAILS there, every PRESERVE row
# PASSES there (both halves of Layer-2 config item (6)). Exits 1 if either requirement is violated.
set -uo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; BASE="${1:-b08f5a9}"
WT="$(cd "$D/../../../.." && pwd)"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
(cd "$WT" && git archive "$BASE" Architect) | tar -x -C "$T" --strip-components=1
rm -rf "$T/changes"
out=$("$D/check.sh" "$T" 2>&1) || true
wrong_pass=$(awk '$1=="PASS" && /kind=(NEW|COOC)/{print $2}' <<<"$out")
wrong_fail=$(awk '$1=="FAIL" && /kind=PRESERVE/{print $2}' <<<"$out")
newf=$(awk '$1=="FAIL" && /kind=(NEW|COOC)/' <<<"$out" | wc -l)
prep=$(awk '$1=="PASS" && /kind=PRESERVE/' <<<"$out" | wc -l)
echo "BASELINE REPLAY @ $BASE  (changes/ removed from the tree, so the corpus pin is proven not assumed)"
echo "  NEW+COOC rows failing at baseline : $newf   <- must be ALL of them"
echo "  PRESERVE rows passing at baseline : $prep   <- must be ALL of them"
echo "  NEW+COOC rows WRONGLY passing     : ${wrong_pass:-none}"
echo "  PRESERVE rows WRONGLY failing     : ${wrong_fail:-none}"
[ -z "$wrong_pass" ] && [ -z "$wrong_fail" ] && { echo "REPLAY: OK — every assertion discriminates"; exit 0; }
echo "REPLAY: FAIL — an assertion that passes at baseline is not an oracle"; exit 1
