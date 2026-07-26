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

# Today's fresh scan data (2026-07-26 04:00 MSK)
# Source: airdrops.io latest/speculative/confirmed, via proxy
# Update timestamp
SCAN_DATE = "2026-07-26 04:00 MSK"

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
        "docs": "None",
        "signal": "TIER 2: Very early, small TVL",
        "actions": [
            "Deposit USDC on HyperEVM",
            "Mint USDM",
            "Stake as sUSDM",
            "Accumulate GEMs points"
        ],
        "deadline": "TBD",
        "last_checked": "None",
        "status": "active",
        "notes": "~16.8% APR. 3-day redemption queue."
    },
    "cambria": {
        "name": "Cambria",
        "type": "game (confirmed airdrop)",
        "url": "https://cambria.game",
        "docs": "https://docs.cambria.game",
        "signal": "TIER 1: HOT 265 deg: confirmed $RSGP airdrop Aug 2026",
        "actions": [
            "Create account with invite code",
            "Link EVM + Solana + Abstract wallets",
            "Check Loot Chests eligibility (Degen/Chad Score)",
            "Fund wallet with USDC for Risk Keys",
            "Play Dungeons for Trinkets/Essence Points",
            "Duel Arena and side activities for points"
        ],
        "deadline": "Loot Chests: 14-day claim; TGE: Aug 2026",
        "last_checked": "None",
        "status": "active",
        "notes": "$2.5M seed BITKRAFT/1kx, $2M strategic BITKRAFT/SkyMavis. Abstract/Solana/EVM."
    },
    "aiw3": {
        "name": "AIW3",
        "type": "AI trading platform (confirmed airdrop)",
        "url": "https://aiw3.io",
        "docs": "https://docs.aiw3.io",
        "signal": "TIER 1: URGENT: snapshot Jul 28, TGE Aug 3",
        "actions": [
            "Connect wallet and complete tutorial BEFORE Jul 28",
            "Daily check-ins (7-day cycle, 3 to 10 pts)",
            "X/Twitter + Telegram community tasks",
            "Daily predictions (up to 100 pts/day)",
            "Publish AI strategies for passive points",
            "Refer friends",
            "Check eligibility Jul 29, claim Aug 3"
        ],
        "deadline": "Snapshot Jul 28! Eligibility Jul 29. TGE Aug 3.",
        "last_checked": "None",
        "status": "active",
        "notes": "Solana + BNB Chain. GalaXin Capital, LD Capital backed. Free tasks available."
    },
    "swarmbase": {
        "name": "SwarmBase",
        "type": "AI agent infra (confirmed airdrop)",
        "url": "https://swarmbase.io",
        "docs": "https://docs.swarmbase.io",
        "signal": "TIER 1: Confirmed: 20% of 1B $SWARM to community",
        "actions": [
            "Connect EVM wallet to opBNB (chain 204)",
            "Fund wallet with tiny BNB for gas",
            "Register account on-chain",
            "Daily check-ins (10 pts base, up to 3x streak)",
            "Mint Pioneer + Builder + OG badges",
            "Use SwarmCore agents for Task Credits",
            "Referrals (up to 860 pts per referral)"
        ],
        "deadline": "TBD (TGE after funding rounds closed Jul 2026)",
        "last_checked": "None",
        "status": "active",
        "notes": "Castrum Capital, M2M Capital backed. $4M Jul 2026. Needs tiny opBNB gas."
    },
    "jtx": {
        "name": "JTX (Jito)",
        "type": "trading platform (speculative)",
        "url": "https://jtx.app",
        "docs": "None",
        "signal": "TIER 2: 139 deg: Jito trading app, no token confirmed",
        "actions": [
            "Sign up with email or Solana wallet",
            "Claim username",
            "Fund Solana wallet with SOL + USDC",
            "Place spot trades",
            "Share referral link (20% lifetime fee share)"
        ],
        "deadline": "No announced TGE",
        "last_checked": "None",
        "status": "active",
        "notes": "Built by Jito Labs (JitoSOL). No confirmed token. Referral program active."
    },
    "plether": {
        "name": "Plether",
        "type": "perpetual DEX testnet (confirmed airdrop)",
        "url": "https://plether.io",
        "docs": "Unknown",
        "signal": "TIER 2: Confirmed airdrop, ends Aug 3, 24deg community temp",
        "actions": [
            "Join testnet on Ethereum",
            "Follow X account",
            "Open plDXY position",
            "Complete before Aug 3 2026 deadline"
        ],
        "deadline": "Expires: Aug 3, 2026 (8 days)",
        "last_checked": None,
        "status": "active",
        "notes": "Confirmed airdrop, ends Aug 3. 24° temp on airdrops.io. Low competition."
    },
    "tradoor0": {
        "name": "Tradoor0",
        "type": "market making bot (speculative retrodrop)",
        "url": "https://tradoor0.io",
        "docs": "Unknown",
        "signal": "TIER 2: HOT 179deg: Market making bot, no token confirmed",
        "actions": [
            "Sign up and connect wallet",
            "Use market making bot on Base",
            "Refer others"
        ],
        "deadline": "No announced TGE",
        "last_checked": None,
        "status": "active",
        "notes": "179° community temperature. Strong speculative retrodrop candidate on Base."
    },
    "collector_crypt": {
        "name": "Collector Crypt",
        "type": "NFT/gaming (confirmed airdrop)",
        "url": "https://collectorcrypt.io",
        "docs": "Unknown",
        "signal": "TIER 2: Confirmed airdrop, 92deg temperature, $CARDS token",
        "actions": [
            "Connect wallet",
            "Complete quests and collections",
            "Refer others",
            "Earn $CARDS tokens"
        ],
        "deadline": "TBD (ongoing campaign)",
        "last_checked": None,
        "status": "active",
        "notes": "Confirmed $CARDS airdrop. 92° community interest. Check official site for quest details."
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