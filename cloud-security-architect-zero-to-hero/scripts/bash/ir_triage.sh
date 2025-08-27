#!/usr/bin/env bash
set -euo pipefail
OUT="/tmp/ir_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUT"
ps aux > "$OUT/processes.txt"
ss -tulpn > "$OUT/sockets.txt"
last -n 50 > "$OUT/logins.txt"
journalctl -n 500 > "$OUT/journal_tail.txt"
echo "IR triage saved to $OUT"
