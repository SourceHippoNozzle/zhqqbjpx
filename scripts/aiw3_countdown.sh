#!/usr/bin/env bash
# AIW3 Snapshot Countdown — Jul 28, 2026
# Checks remaining time until the AIW3 snapshot deadline
# testnet-campaign-recon/scripts/aiw3_countdown.sh

SNAPSHOT="2026-07-28T00:00:00Z"
NOW=$(date -u +%s)
SNAP_EPOCH=$(date -u -d "$SNAPSHOT" +%s 2>/dev/null || date -u -j -f "%Y-%m-%dT%H:%M:%SZ" "$SNAPSHOT" +%s 2>/dev/null)

if [ -z "$SNAP_EPOCH" ]; then
    echo "ERROR: Cannot parse date. Need GNU date or macOS date."
    exit 1
fi

REMAINING=$((SNAP_EPOCH - NOW))

if [ $REMAINING -le 0 ]; then
    echo "⚠️ AIW3 SNAPSHOT DEADLINE PASSED!"
    echo "Check eligibility at https://aiw3.ai"
    exit 0
fi

DAYS=$((REMAINING / 86400))
HOURS=$(( (REMAINING % 86400) / 3600 ))
MINUTES=$(( (REMAINING % 3600) / 60 ))

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  AIW3 SNAPSHOT COUNTDOWN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Snapshot:  $SNAPSHOT"
echo "  Remaining: ${DAYS}d ${HOURS}h ${MINUTES}m"
echo "  Tasks needed before snapshot:"
echo "    • Connect wallet + complete tutorial"
echo "    • Daily check-ins (7-day cycle)"
echo "    • Daily predictions (up to 100 pts/day)"
echo "    • X/Twitter + Telegram community tasks"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $DAYS -le 2 ]; then
    echo ""
    echo "  ⚠️ URGENT: Less than 2 days remaining!"
    echo "  Complete free tasks NOW!"
    echo ""
    echo "  Next steps:"
    echo "  Jul 28 — Snapshot (connect wallet before!)"
    echo "  Jul 29 — Check eligibility"
    echo "  Aug 3  — TGE + Claim tokens"
fi

echo ""
echo "Live: https://aiw3.ai"
