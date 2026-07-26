#!/usr/bin/env python3
"""
Crypto Campaign Dashboard — 2026-07-26
Quick scan and status report for all tracked campaigns.
Usage: python3 campaign_dashboard.py
"""
import json
import subprocess
import sys
from datetime import datetime

TRACKER_FILE = "/home/openclaw/.hermes/testnet_campaigns.json"

TIER_EMOJI = {"TIER 1": "🔴", "TIER 2": "🟡", "TIER 3": "🟢"}

def check_url(url, timeout=8):
    """Check URL reachability."""
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "--noproxy", "*",
             "-o", "/dev/null", "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=timeout+2
        )
        code = result.stdout.strip()
        return code if code else "TIMEOUT"
    except Exception:
        return "ERROR"

def get_tier(campaign):
    sig = campaign.get("signal", "")
    if sig.startswith("TIER 1"):
        return "TIER 1"
    elif sig.startswith("TIER 2"):
        return "TIER 2"
    return "TIER 3"

def main():
    if not __import__("os").path.exists(TRACKER_FILE):
        print(f"Tracker file not found: {TRACKER_FILE}")
        sys.exit(1)

    with open(TRACKER_FILE) as f:
        data = json.load(f)

    camps = data.get("campaigns", {})
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    print(f"\n{'='*65}")
    print(f"  CRYPTO CAMPAIGN DASHBOARD — {now}")
    print(f"{'='*65}")

    # Group by tier
    tiers = {"TIER 1": [], "TIER 2": [], "TIER 3": []}
    for key, c in camps.items():
        tier = get_tier(c)
        tiers[tier].append((key, c))

    for tier_name in ["TIER 1", "TIER 2", "TIER 3"]:
        items = tiers[tier_name]
        if not items:
            continue
        emoji = TIER_EMOJI.get(tier_name, "")
        print(f"\n{'='*65}")
        print(f"  {emoji} {tier_name} ({len(items)} campaigns)")
        print(f"{'='*65}")

        for key, c in items:
            name = c.get("name", key)
            url = c.get("url", "")
            status = c.get("status", "unknown")
            signal = c.get("signal", "")[:60]
            deadline = c.get("deadline", "")

            # Quick URL check
            url_status = ""
            if url and url.startswith("http"):
                code = check_url(url)
                url_status = f"[HTTP {code}]"

            print(f"\n  {status_icon(status)} {name} {url_status}")
            print(f"    {signal}")
            if deadline:
                print(f"    Deadline: {deadline}")
            if url:
                print(f"    URL: {url}")
            for a in c.get("actions", [])[:3]:
                print(f"    \u2192 {a}")

    print(f"\n{'='*65}")
    print(f"  Dashboard ready. Total: {len(camps)} campaigns tracked.")
    print(f"{'='*65}\n")

def status_icon(status):
    icons = {"active": "\u25cf", "paused": "\u25cb", "completed": "\u2713", "cancelled": "\u2717"}
    return icons.get(status, "?")

if __name__ == "__main__":
    main()
