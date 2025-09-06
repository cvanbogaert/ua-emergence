#!/usr/bin/env bash
set -euo pipefail
OUT_JSON="pr-draft/plan.json"; OUT_LOG="pr-draft/plan.log"
while [[ $# -gt 0 ]]; do case "$1" in --out-json) OUT_JSON="$2"; shift 2;; --out-log) OUT_LOG="$2"; shift 2;; *) echo "Unknown arg: $1" >&2; exit 2;; esac; done
mkdir -p "$(dirname "$OUT_JSON")" "$(dirname "$OUT_LOG")"
ts(){ date -u +"%Y-%m-%dT%H:%M:%SZ"; }; log(){ echo "[$(ts)] $*" | tee -a "$OUT_LOG"; }
log "BEGIN: plan-only run"
STATUS="ok"; ISSUES=()
# (place your dry-run steps here; keep non-mutating)
# if command -v make >/dev/null 2>&1 && [[ -f Makefile ]]; then make -n plan >> "$OUT_LOG" 2>&1 || ISSUES+=("make -n plan nonzero"); fi
[[ ${#ISSUES[@]} -gt 0 ]] && STATUS="degraded"
printf '{ "timestamp":"%s","status":"%s","summary":"Plan-only run (no side effects).","issues":[] }\n' "$(ts)" "$STATUS" > "$OUT_JSON"
log "END: plan-only run (status=$STATUS)"
