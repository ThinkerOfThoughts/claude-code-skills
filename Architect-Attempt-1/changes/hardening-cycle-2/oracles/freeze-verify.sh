#!/usr/bin/env bash
# freeze-verify.sh — stage-4's criteria FREEZE, and stage-8's verification of it.
#
#   freeze-verify.sh freeze   -> records sha256 of the criteria set into oracles/FROZEN.sha256
#   freeze-verify.sh verify   -> re-hashes and EXITS 1 on any drift
#
# Why this exists as a script rather than a sentence: gate 4 must "freeze 1.5-criteria.md and record its
# sha256", and stage 8 must show the criteria it verified against are the criteria that were reviewed.
# A frozen file whose hash is only asserted is not frozen. The frozen set deliberately includes the
# DATA the criteria are made of — criteria.tsv, preserve-counts.txt, expected-sites.txt, sweep-answers.tsv —
# because moving a criterion's goalposts by editing the data file it reads is the obvious evasion, and a
# hash over the prose alone would not see it.
set -uo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; C="$(cd "$D/.." && pwd)"
FILES=(
  "$C/1.5-criteria.md"
  "$C/1-spec.md"
  "$C/2-plan.md"
  "$D/criteria.tsv"
  "$D/preserve-counts.txt"
  "$D/expected-sites.txt"
  "$D/sweep-answers.tsv"
  "$D/checklib.py"
  "$D/lib-corpus.sh"
)
MAN="$D/FROZEN.sha256"
case "${1:-}" in
  freeze)
    { echo "# FROZEN at gate 4 by freeze-verify.sh on $(date -u +%Y-%m-%dT%H:%M:%SZ)."
      echo "# Any later edit to a listed file is criteria drift and fails \`freeze-verify.sh verify\`."
      for f in "${FILES[@]}"; do (cd "$C/.." && sha256sum "${f#$C/../}"); done
    } > "$MAN"
    echo "FROZEN ${#FILES[@]} files -> ${MAN#$C/}"; cat "$MAN"; exit 0 ;;
  verify)
    [ -r "$MAN" ] || { echo "FREEZE-VERIFY: FATAL no manifest at $MAN — gate 4 never froze the criteria"; exit 2; }
    if (cd "$C/.." && grep -v '^#' "$MAN" | sha256sum -c --quiet); then
      echo "FREEZE-VERIFY: OK — all $(grep -vc '^#' "$MAN") frozen files match the gate-4 manifest"; exit 0
    fi
    echo "FREEZE-VERIFY: FAIL — a criterion changed after the gate-4 freeze (criteria drift)"; exit 1 ;;
  *) echo "usage: freeze-verify.sh {freeze|verify}"; exit 2 ;;
esac
