#!/usr/bin/env python3
"""
Testnet Campaign Orchestrator — 2026-07-26 Night Mission
Automates tracking, check-ins, and status reporting for active testnet campaigns.

Usage:
  python3 campaign_orchestrator.py               # Show today's status
  python3 campaign_orchestrator.py --report       # Generate daily report
  python3 campaign_orchestrator.py --checkin      # Mark all as checked
"""
import json
import os
import sys
from datetime import datetime, timezone

TRACKER_FILE = os.path.expanduser("~/.hermes/testnet_campaigns.json")
HOME = os.path.expanduser("~")

# Tier 1 — High Signal: Confirmed airdrop + live testnet
TIER1_URGENT = [
    ("AIW3", "aiw3", "SNAPSHOT JUL 28 — 2 days! TGE Aug 3. Daily check-ins + predictions."),
    ("Orbinum", "orbinum", "Confirmed 2% $ORB airdrop. Claim 10 ORB/day + shielded transfers."),
    ("Canopy", "canopy", "Confirmed 50% $CNPY to community. Deploy appchain for max points."),
    ("Arc (Circle)", "arc", "Circle/BlackRock/Visa L1 testnet. $222M presale."),
    ("Cambria", "cambria", "Confirmed $RSGP airdrop. 265 community temp. TGE Aug 2026."),
    ("SwarmBase", "swarmbase", "Confirmed 20% of 1B $SWARM to community. Daily check-ins."),
]

# Tier 2 — Medium Signal
TIER2_ACTIVE = [
    ("Plether", "plether", "Confirmed airdrop, ends Aug 3 (8 days). Open plDXY position."),
    ("Collector Crypt", "collector_crypt", "Confirmed $CARDS airdrop. 92 community interest."),
    ("GIWA (Upbit)", "giwa", "Upbit L2 testnet. 100M+ txns. Bridge + deploy."),
    ("Robinhood Chain", "robinhood", "Free gas until Sep 28. No token yet — classic early play."),
    ("Monaco", "monaco", "Trading infra on Sei. Ex-Goldman team. Speculative retrodrop."),
    ("Tradoor0", "tradoor0", "Market making bot on Base. 179 temp. No token yet."),
    ("Sekai", "sekai", "Liquid staking on HyperEVM. Public testnet Jun 2026."),
    ("Checkpoint", "checkpoint", "Point marketplace testnet. Meta-play on airdrop points."),
    ("JTX (Jito)", "jtx", "Jito Labs trading app. 139 temp. No token confirmed."),
]

# Tier 3 — Watch
TIER3_WATCH = [
    ("DBK Chain", None, "L2 Genesis NFT → potential future token."),
    ("3Jane", None, "Lending. Confirmed. Supply USDC."),
    ("Privacy Pools", None, "Privacy protocol. No token yet."),
    ("Ducat", None, "Stablecoin building on-chain."),
    ("ZENi AI", None, "AI Data Layer. New on airdropalert."),
    ("DGrid AI", None, "AI Inference Network. New on airdropalert."),
]

def emoji_for_deadline(days_left):
    if days_left is None:
        return "⏳"
    if days_left <= 3:
        return "🔥"
    if days_left <= 7:
        return "⚡"
    if days_left <= 14:
        return "⏰"
    return "📋"

def main():
    print("=" * 65)
    print(f"  TESTNET CAMPAIGN ORCHESTRATOR — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("  Operator: Pavel (tringt)")
    print("=" * 65)

    if "--report" in sys.argv:
        generate_report()
    elif "--checkin" in sys.argv:
        mark_checked()
    else:
        show_status()

def show_status():
    print("\n🔥 TIER 1 — URGENT: Confirmed Airdrop + Active")
    print("-" * 65)
    for name, key, desc in TIER1_URGENT:
        urgent = "SNAPSHOT" in desc.upper()
        marker = "🚨" if urgent else "⭐"
        print(f"  {marker} {name:25s} | {desc}")

    print("\n⚡ TIER 2 — Active: Medium Signal")
    print("-" * 65)
    for name, key, desc in TIER2_ACTIVE:
        print(f"  📋 {name:25s} | {desc}")

    print("\n👁️  TIER 3 — Watch List")
    print("-" * 65)
    for name, key, desc in TIER3_WATCH:
        print(f"  👁️  {name:25s} | {desc}")

    # Quick actions
    print("\n🎯 URGENT ACTIONS FOR TODAY (Jul 26)")
    print("-" * 65)
    print("  1. 🔥 AIW3 — daily check-in + predictions (snapshot Jul 28!)")
    print("  2. ⭐ Orbinum — claim 10 ORB + shielded transfer")
    print("  3. ⭐ Canopy — deploy testnet appchain")
    print("  4. ⚡ Plether — open plDXY position (ends Aug 3)")
    print("  5. 📋 SwarmBase — daily check-in + mint badges")
    print("  6. 📋 Arc — claim faucet, bridge, swap")
    print("  7. 📋 GIWA — bridge to Sepolia testnet + deploy")
    print()
    print(f"  Report saved: {HOME}/testnet-campaign-recon/night_crypto_report_2026-07-26.md")

def generate_report():
    """Generate markdown report"""
    now = datetime.now(timezone.utc)
    report = f"""# Testnet Campaign Status — {now.strftime('%Y-%m-%d %H:%M UTC')}

## 🔥 TIER 1 — Urgent

| Project | Status | Action | Deadline |
|---------|--------|--------|----------|
"""
    for name, key, desc in TIER1_URGENT:
        report += f"| {name} | ✅ Live | {desc} | Check daily |\n"

    report += f"""
## ⚡ TIER 2 — Active

| Project | Status | Action |
|---------|--------|--------|
"""
    for name, key, desc in TIER2_ACTIVE:
        report += f"| {name} | ✅ Live | {desc} |\n"

    report += f"""
## 👁️ TIER 3 — Watch

| Project | Notes |
|---------|-------|
"""
    for name, key, desc in TIER3_WATCH:
        report += f"| {name} | {desc} |\n"

    report += f"""
---
*Generated by Hermes Agent | {now.strftime('%Y-%m-%d %H:%M UTC')}*
"""
    print(report)

def mark_checked():
    """Update last_checked timestamps"""
    if not os.path.exists(TRACKER_FILE):
        print("Tracker file not found. Run the script first without --checkin.")
        return
    with open(TRACKER_FILE) as f:
        data = json.load(f)
    now = datetime.now(timezone.utc).isoformat()[:19]
    for key in data.get("campaigns", {}):
        data["campaigns"][key]["last_checked"] = now
    data["updated"] = datetime.now(timezone.utc).isoformat()
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[{now}] All campaigns marked as checked.")

if __name__ == "__main__":
    main()
