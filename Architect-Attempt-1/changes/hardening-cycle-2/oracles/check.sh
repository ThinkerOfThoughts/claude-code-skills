#!/usr/bin/env bash
# check.sh <tree-root> [criterion-id] — the positive per-site assertion runner. Corpus is PINNED by
# checklib.py's corpus() (identical list to lib-corpus.sh); `changes/` is not in it and cannot enter.
set -uo pipefail
D="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$D/checklib.py" "${1:?tree root}" "$D/criteria.tsv" ${2:-}
