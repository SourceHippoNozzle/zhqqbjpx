#!/usr/bin/env python3
"""Crypto Deadline Dashboard — 2026-07-26 Night Session

Ranks all tracked campaigns by urgency, shows remaining time,
and prints a morning action list. Run: python3 deadline_dashboard.py
"""
import json, os, sys
from datetime import datetime, timezone, timedelta

TRACKER_FILE = os.path.expanduser("~/.hermes/testnet_campaigns.json")
NOW = datetime.now(timezone.utc)

URGENT_DEADLINES = [
    ("AIW3", "Snapshot", "2026-07-28T00:00:00Z",
     "Connect wallet + complete tutorial BEFORE snapshot. Check eligibility Jul 29. TGE Aug 3.",
     "URGENT"),
    ("Plether", "Testnet Ends", "2026-08-03T00:00:00Z",
     "Join testnet, follow X, open plDXY position. Confirmed airdrop — ends Aug 3.",
     "WARNING"),
]

CAMPAIGN_TEMPS = {
    "Cambria": 265, "Orbinum": 193, "Tradoor0": 179, "JTX": 139,
    "AIW3": 98, "Collector Crypt": 92, "SwarmBase": 56, "Plether": 24,
    "DBK Chain": 18, "GMGN": 14, "HoodTracker": 7, "Privacy Pools": 7,
    "Legend": 8, "Checkpoint": 1, "3Jane": 3, "Ducat": 3, 
    "Osero": 4, "Hyperlynx": 4, "AFX": 2, "Minotaurus": 17,
}

print("=" * 72)
print("  CRYPTO DEADLINE DASHBOARD — July 26, 2026 (04:00 MSK)")
print("=" * 72)

print("\n" + "=" * 72)
print("  ⏰ URGENT DEADLINES")
print("=" * 72)

for name, event_type, deadline_str, actions, severity in URGENT_DEADLINES:
    deadline = datetime.fromisoformat(deadline_str.replace("Z", "+00:00"))
    remaining = deadline - NOW
    days = remaining.days
    hours = remaining.seconds // 3600
    mins = (remaining.seconds % 3600) // 60
    
    icon = "🔴" if severity == "URGENT" else "🟡"
    print(f"\n  {icon} {name} — {event_type}")
    print(f"     Deadline: {deadline_str[:19]} UTC")
    print(f"     Remaining: {days}d {hours}h {mins}m")
    print(f"     {actions}")

print("\n" + "=" * 72)
print("  🔥 TOP CAMPAIGNS BY COMMUNITY INTEREST")
print("=" * 72)
print(f"  {'Project':<20} {'Temp':<6} {'Status':<12} {'Category'}")
print(f"  {'-'*20} {'-'*6} {'-'*12} {'-'*20}")
for proj, temp in sorted(CAMPAIGN_TEMPS.items(), key=lambda x: -x[1]):
    status = "CONFIRMED" if proj in ("AIW3", "Cambria", "Orbinum", "SwarmBase", "Plether", "Collector Crypt", "3Jane", "HoodTracker", "Osero", "Hyperlynx", "AFX") else "SPECULATIVE"
    cat_map = {
        "AIW3": "AI/Liquidity", "Cambria": "Gaming", "Orbinum": "Privacy L1",
        "Tradoor0": "Trading Tool", "JTX": "DEX", "Collector Crypt": "NFT/Gaming",
        "SwarmBase": "AI Agents", "Plether": "Perpetuals", "DBK Chain": "L2",
        "GMGN": "Trading Tool", "HoodTracker": "SocialFi", "Privacy Pools": "Privacy",
        "Legend": "Perpetuals", "Checkpoint": "Points Market", "3Jane": "Lending",
        "Ducat": "Stablecoin", "Osero": "Stablecoin", "Hyperlynx": "TBD",
        "AFX": "TBD", "Minotaurus": "Gaming"
    }
    cat = cat_map.get(proj, "Unknown")
    print(f"  {proj:<20} {temp}°{'':>4} {status:<12} {cat}")

# Load tracker if available
if os.path.exists(TRACKER_FILE):
    with open(TRACKER_FILE) as f:
        data = json.load(f)
    
    print("\n" + "=" * 72)
    print("  📋 TRACKED CAMPAIGNS DETAIL")
    print("=" * 72)
    
    for key, c in data.get("campaigns", {}).items():
        tier = c.get("signal", "")[:25]
        print(f"\n  [{c.get('status','?')}] {c['name']}")
        print(f"     Type: {c.get('type', '?')}")
        print(f"     Signal: {c.get('signal', '?')}")
        if c.get("deadline"):
            print(f"     Deadline: {c['deadline']}")
        for a in c.get("actions", []):
            print(f"     → {a}")

print("\n" + "=" * 72)
print("  📊 SCAN SUMMARY")
print("=" * 72)
print(f"  Projects scanned: {len(CAMPAIGN_TEMPS)}")
print(f"  Confirmed airdrops: {sum(1 for p in CAMPAIGN_TEMPS if CAMPAIGN_TEMPS[p] > 0)} active")
print(f"  Deadlines within 7 days: {sum(1 for _, _, dl, _, _ in URGENT_DEADLINES if 'URGENT' in _[4])}")
print(f"  Scan timestamp: 2026-07-26 04:00 MSK")
print(f"  Source: airdrops.io latest/speculative/confirmed pages")
print()
print("  🔴 AIW3 snapshot Jul 28 — 2 days! HIGHEST PRIORITY")
print("  🟡 Plether ends Aug 3 — 8 days left")
print()

print("=" * 72)
print("  RANKED MORNING ACTION LIST")
print("=" * 72)
print("""
  PRIO  ACTION                              EFFORT  REASON
  ───── ──────────────────────────────      ──────  ─────────────────────────
  1 🔴  AIW3: connect wallet, tutorial,      30min  Snapshot Jul 28! Do NOW
        daily check-ins before Jul 28
  2 🔴  Cambria: claim Loot, play             20min  265°, top confirmed airdrop
  3 🟡  Orbinum: claim 10 ORB/day,             2min  Confirmed airdrop, low crowd
        shielded transfers
  4 🟡  Plether: join testnet,                 15min  Ends Aug 3, confirmed drop
        open plDXY position
  5 🟡  Push testnet-campaign-recon to         5min  SSH auth works, needs
        GitHub                                    PAT or web create
  6 🟢  Collector Crypt: investigate           15min  New: 92°, confirmed $CARDS
        official quests
  7 🟢  Check Polymarket ts-sdk issues        10min  0 GHI, check unlabeled
  8 🟢  Run daily deadline cron review         2min  Already configured at 09:00
""")
