#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-origin/main}"; OUT="${2:-./pr-draft/changes.patch}"
mkdir -p "$(dirname "$OUT")"
git fetch --all --quiet || true
git diff --binary --diff-algorithm=patience "$BASE"...HEAD > "$OUT" || : > "$OUT"
echo "Wrote patch to $OUT"
