#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.."; pwd)"
mkdir -p "$ROOT/runs"
UA_RUNS_DIR="$ROOT/runs" python3 "$ROOT/orchestrator/runner.py"
