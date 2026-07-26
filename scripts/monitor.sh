#!/usr/bin/env bash
# Testnet Campaign Monitor v2 — checks URL reachability daily
# testnet-campaign-recon/scripts/monitor.sh

REPORT="$HOME/night_crypto_report_2026-07-26.md"
TRACKER="$HOME/testnet-campaign-recon/testnet_tracker.py"

echo "=== Testnet Monitor — $(date -u '+%Y-%m-%d %H:%M UTC') ==="

declare -A URLS
URLS["Canopy"]="https://canopy.io"
URLS["Arc (Circle)"]="https://circle.com/arc"
URLS["GIWA"]="https://giwa.io"
URLS["Robinhood Chain"]="https://robinhood.com"
URLS["Orbinum"]="https://orbinum.network"
URLS["Orbinum RPC"]="https://rpc-1.testnet.orbinum.io"
URLS["Cambria"]="https://cambria.game"
URLS["AIW3"]="https://aiw3.io"
URLS["SwarmBase"]="https://swarmbase.io"
URLS["JTX"]="https://jtx.app"

for name in "${!URLS[@]}"; do
    url="${URLS[$name]}"
    code=$(curl -sL --max-time 8 --noproxy '*' -o /dev/null -w '%{http_code}' "$url" 2>/dev/null)
    echo "[$code] $name — $url"
done

# Update tracker
if [ -f "$TRACKER" ]; then
    python3 "$TRACKER" --check 2>/dev/null
    echo "Tracker timestamp updated."
fi

echo "=== Done ==="
