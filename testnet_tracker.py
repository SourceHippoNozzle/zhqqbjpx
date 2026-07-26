#!/usr/bin/env python3
"""
Testnet Campaign Tracker — 2026-07-26
Monitors testnet campaign status, tracks deadlines and action items.
Usage: python3 testnet_tracker.py [--check]
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

TRACKER_FILE = os.path.expanduser("~/.hermes/testnet_campaigns.json")

DEFAULT_CAMPAIGNS = {
    "canopy": {
        "name": "Canopy",
        "type": "testnet (confirmed airdrop)",
        "url": "https://canopy.testnet.io",
        "docs": "https://docs.canopy.io",
        "signal": "TIER 1 — Confirmed: 50% $CNPY to community",
        "actions": [
            "Deploy testnet appchain (highest points multiplier)",
            "Daily check-ins and quests",
            "Referrals and social tasks",
            "Track snapshot date (~2 weeks before TGE)"
        ],
        "deadline": "TGE 2026 (snapshot unknown)",
        "last_checked": None,
        "status": "active",
        "notes": "Arrington Capital + Fenbushi backed. $8.5M raised."
    },
    "arc": {
        "name": "Arc (Circle)",
        "type": "testnet L1",
        "url": "https://arc.circle.com",
        "docs": "https://docs.arc.circle.com",
        "signal": "TIER 1 — High: $222M presale, 60% ecosystem allocation",
        "actions": [
            "Claim USDC/EURC from Circle faucet",
            "Bridge, swap, LP on testnet",
            "Touch 4+ protocol types (breadth > volume)",
            "Deploy contracts",
            "Prepare for KYC if token ships"
        ],
        "deadline": "TBD (testnet ongoing)",
        "last_checked": None,
        "status": "active",
        "notes": "BlackRock, Visa partners. NYSE-listed = KYC likely."
    },
    "giwa": {
        "name": "GIWA (Upbit L2)",
        "type": "testnet L2",
        "url": "https://giwa.io",
        "docs": "https://docs.giwa.io",
        "signal": "TIER 1 — Medium: Upbit's Base/Ink precedent",
        "actions": [
            "Claim Sepolia ETH from faucet",
            "Bridge to GIWA Sepolia",
            "Deploy a contract",
            "Mint an NFT",
            "Periodic activity for wallet age"
        ],
        "deadline": "TBD (mainnet after OP Enterprise deal)",
        "last_checked": None,
        "status": "active",
        "notes": "100M+ txns on testnet. Strong Korean exchange backing."
    },
    "robinhood": {
        "name": "Robinhood Chain",
        "type": "L1 ecosystem (no token)",
        "url": "https://robinhood.com/chain",
        "docs": "https://robinhood.com/chain/docs",
        "signal": "TIER 1 — High: Launched Jul 1, free gas, million TVL",
        "actions": [
            "Bridge assets to Robinhood Chain",
            "Use Arcus and Lighter dApps",
            "Farm ecosystem points",
            "Track mainnet activity patterns"
        ],
        "deadline": "Free gas: ~Sep 28, 2026 (90 days from Jul 1)",
        "last_checked": None,
        "status": "active",
        "notes": "No native token. 90-day free gas through Robinhood Wallet."
    },
    "orbinum": {
        "name": "Orbinum",
        "type": "privacy L1 testnet",
        "url": "https://orbinum.io",
        "docs": "https://docs.orbinum.io",
        "signal": "TIER 2 — Early: quiet, no crowd",
        "actions": [
            "Claim 10 ORB/day via Discord faucet",
            "Test shielded transfers",
            "Unshield back",
            "Run normal EVM transactions",
            "2-min daily habit"
        ],
        "deadline": "TBD (no announced airdrop)",
        "last_checked": None,
        "status": "active",
        "notes": "ZK shielded pools + EVM. Very early."
    },
    "sekai": {
        "name": "Sekai (Hyperliquid)",
        "type": "liquid staking testnet",
        "url": "https://sekai.xyz",
        "docs": "https://docs.sekai.xyz",
        "signal": "TIER 2 — Early: no points program yet",
        "actions": [
            "Mint LSTs on testnet",
            "Redeem and swap LSTs on Sekai DEX",
            "Provide liquidity",
            "Submit bug reports in Discord"
        ],
        "deadline": "TBD (testnet Jun 2026)",
        "last_checked": None,
        "status": "active",
        "notes": "Public testnet June 2026. No points = classic early setup."
    },
    "checkpoint": {
        "name": "Checkpoint",
        "type": "point marketplace testnet",
        "url": "https://checkpoint.io",
        "docs": "https://docs.checkpoint.io",
        "signal": "TIER 2 — Meta play",
        "actions": [
            "Engage in market activity on testnet",
            "Use referrals",
            "Track XP accumulation"
        ],
        "deadline": "TBD",
        "last_checked": None,
        "status": "active",
        "notes": "Marketplace for trading airdrop points before TGE."
    },
    "monetrix": {
        "name": "Monetrix (HyperEVM)",
        "type": "passive yeld + points",
        "url": "https://monetrix.io",
        "docs": None,
        "signal": "TIER 2 — Very early, small TVL",
        "actions": [
            "Deposit USDC on HyperEVM",
            "Mint USDM",
            "Stake as sUSDM",
            "Accumulate GEMs points"
        ],
        "deadline": "TBD",
        "last_checked": None,
        "status": "active",
        "notes": "~16.8% APR. 3-day redemption queue."
    }
}


def load_tracker():
    """Load campaign tracker or initialize defaults."""
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE) as f:
            return json.load(f)
    # Initialize with defaults
    data = {"campaigns": DEFAULT_CAMPAIGNS, "updated": datetime.now(timezone.utc).isoformat()}
    save_tracker(data)
    return data


def save_tracker(data):
    """Save campaign tracker to file."""
    os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)
    data["updated"] = datetime.now(timezone.utc).isoformat()
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f, indent=2)


def show_status(data):
    """Display campaign status."""
    camps = data["campaigns"]
    tiers = {"TIER 1": [], "TIER 2": [], "TIER 3": []}
    for key, c in camps.items():
        tier = "TIER 3"
        if c["signal"].startswith("TIER 1"):
            tier = "TIER 1"
        elif c["signal"].startswith("TIER 2"):
            tier = "TIER 2"
        tiers[tier].append((key, c))

    print("=" * 60)
    print(f"  TESTNET CAMPAIGN TRACKER — {data['updated'][:19]}")
    print("=" * 60)
    
    for tier_name in ["TIER 1", "TIER 2", "TIER 3"]:
        items = tiers[tier_name]
        if not items:
            continue
        print(f"\n{'='*60}")
        print(f"  {tier_name}")
        print(f"{'='*60}")
        for key, c in items:
            lc = c.get("last_checked") or "never"
            status = c.get("status", "unknown")
            print(f"\n  [{status}] {c['name']} ({c['type']})")
            print(f"    Signal: {c['signal']}")
            print(f"    Last checked: {lc}")
            print(f"    URL: {c['url']}")
            if c.get("deadline"):
                print(f"    Deadline: {c['deadline']}")
            for a in c.get("actions", []):
                print(f"    → {a}")
            if c.get("notes"):
                print(f"    Notes: {c['notes']}")


def main():
    data = load_tracker()
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        for key, c in data["campaigns"].items():
            c["last_checked"] = datetime.now(timezone.utc).isoformat()[:19]
        save_tracker(data)
        print(f"[{data['updated'][:19]}] All campaigns marked as checked.")
    else:
        show_status(data)


if __name__ == "__main__":
    main()
