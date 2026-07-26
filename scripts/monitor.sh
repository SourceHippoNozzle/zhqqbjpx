#!/usr/bin/env bash
# Testnet Campaign Monitor — checks URL reachability daily
# testnet-campaign-recon/scripts/monitor.sh

REPORT="$HOME/night_crypto_report_2026-07-26.md"
TRACKER="$HOME/testnet_tracker.py"

echo "=== Testnet Monitor — $(date -u '+%Y-%m-%d %H:%M UTC') ==="

declare -A URLS
URLS["Arc (Circle)"]="https://circle.com/arc"
URLS["GIWA"]="https://giwa.io"

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
