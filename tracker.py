#!/usr/bin/env python3
"""
Crypto Campaign Tracker — Hermes Agent Edition
A comprehensive, ranked tracker of active testnet, airdrop, and builder opportunities.
Auto-generated: 2026-07-26 03:XX MSK

Usage:
  python3 tracker.py          # markdown report
  python3 tracker.py table    # terminal table
  python3 tracker.py json     # JSON output
"""

import json, sys
from datetime import datetime

NOW_UTC = "2026-07-26 00:50 UTC"
NOW_MSK = "2026-07-26 03:50 MSK"

OPPORTUNITIES = [
    # ═══════ TIER 1: HIGH SIGNAL — Confirmed airdrop + active testnet ═══════
    {
        "rank": 1,
        "project": "Orbinum Network",
        "category": "L1 Privacy Chain",
        "signal": "HIGH",
        "temperature": "193°–224°",
        "confirmed": True,
        "status": "TESTNET LIVE — Confirmed Airdrop (2% of $ORB supply)",
        "actions": "Interact with testnet: shielded transfers, stake test ORB",
        "chain": "EVM-compatible (Substrate+Frontier, Chain ID 2700)",
        "rpc": "https://rpc-1.testnet.orbinum.io",
        "explorer": "https://explorer.testnet.orbinum.io",
        "faucet": "https://faucet.orbinum.network (Cloudflare Turnstile)",
        "url": "https://orbinum.network",
        "docs": "https://docs.orbinum.network",
        "github": "github.com/orbinum",
        "deadline": "Ongoing — TGE not announced",
        "notes": "Privacy chain using ZK shielded pools. Highest community interest. Confirmed 2% supply allocation. RPC verified (chainId=2700). Faucet needs browser (CF Turnstile).",
        "last_verified": "2026-07-26"
    },
    {
        "rank": 2,
        "project": "AIW3",
        "category": "AI / Liquidity",
        "signal": "HIGH",
        "temperature": "94°",
        "confirmed": True,
        "status": "CONFIRMED — Ongoing. SNAPSHOT Jul 28! TGE Aug 3! (2 days!)",
        "actions": "Sign up, social tasks, daily check-in, trading tasks",
        "chain": "Ethereum/Base",
        "url": "https://aiw3.io",
        "deadline": "Snapshot Jul 28 — TGE Aug 3",
        "notes": "AI-powered liquidity protocol. CRITICAL WINDOW: snapshot in 2 days (Jul 28). Must act before snapshot. High urgency.",
        "last_verified": "2026-07-26"
    },
    {
        "rank": 3,
        "project": "Plether",
        "category": "Perpetual DEX",
        "signal": "HIGH",
        "temperature": "24°",
        "confirmed": True,
        "status": "CONFIRMED — Testnet Jul 20 – Aug 3 (8 days remaining!)",
        "actions": "Join testnet, follow on X, open plDXY position",
        "chain": "Ethereum",
        "url": "https://plether.io",
        "deadline": "August 3, 2026",
        "notes": "Confirmed airdrop campaign. Short window — only 8 days! Priority action.",
        "last_verified": "2026-07-26"
    },
    # ═══════ TIER 2: MEDIUM SIGNAL ═══════
    {
        "rank": 4,
        "project": "Cambria",
        "category": "Gaming (Solana)",
        "signal": "MEDIUM",
        "temperature": "265°",
        "confirmed": True,
        "status": "CONFIRMED — $RSGP TGE announced, loot chests active",
        "actions": "Claim loot chests, play game",
        "chain": "Solana",
        "url": "https://cambria.gg",
        "deadline": "Ongoing (TGE announced)",
        "notes": "Highest temperature on aggregators (265°). Runescape-inspired on-chain game. High competition. $RSGP token.",
        "last_verified": "2026-07-26"
    },
    {
        "rank": 5,
        "project": "SwarmBase",
        "category": "AI Agents",
        "signal": "MEDIUM",
        "temperature": "56°",
        "confirmed": True,
        "status": "CONFIRMED — Register, daily check-in, refer (20% $SWARM)",
        "actions": "Register, daily check-in, refer friends",
        "chain": "Ethereum",
        "url": "https://swarmbase.ai",
        "deadline": "Ongoing",
        "notes": "AI agents protocol. Confirmed 20% $SWARM airdrop allocation. Low-effort daily check-in.",
        "last_verified": "2026-07-26"
    },
    {
        "rank": 6,
        "project": "Monaco Trading",
        "category": "Trading Infrastructure",
        "signal": "MEDIUM",
        "temperature": "Speculative",
        "confirmed": False,
        "status": "TESTNET ACTIVE — Strong retrodrop candidate (no token)",
        "actions": "Trade on Sei Atlantic-2 testnet, use limit orders, add liquidity",
        "chain": "Sei (Atlantic-2 testnet)",
        "url": "https://app.monaco.trading",
        "deadline": "Speculative — no announced deadline",
        "notes": "Ex-Goldman Sachs/GSR team. Testnet app mints 2,000 test USDC. Strong speculative play.",
        "last_verified": "2026-07-26"
    },
    {
        "rank": 7,
        "project": "DBK Chain",
        "category": "L2",
        "signal": "MEDIUM",
        "temperature": "18°",
        "confirmed": True,
        "status": "CONFIRMED — Genesis NFT (likely future token)",
        "actions": "Install Rabby Wallet, mint Genesis NFT",
        "chain": "Custom L2 (EVM-compatible)",
        "url": "https://dbkchain.io",
        "deadline": "Ongoing (Genesis NFT supply limited)",
        "notes": "Genesis NFT likely required for token airdrop. Low effort for potential reward.",
        "last_verified": "2026-07-26"
    },
]

# Developer / Ecosystem Opportunities
DEVELOPER_OPPS = [
    {
        "rank": "A",
        "opportunity": "Hyperlane AVS Operator (EigenLayer)",
        "type": "Node Running",
        "signal": "HIGH",
        "status": "Permissionless — Register AVS operator",
        "requirements": "2-core/2GB RAM/4GB storage, ~$75/mo, stake required",
        "notes": "CLI: npm install -g @hyperlane-xyz/cli. Docs: https://docs.hyperlane.xyz"
    },
    {
        "rank": "B",
        "opportunity": "EigenCloud AVS Operator",
        "type": "Node Running",
        "signal": "HIGH",
        "status": "Active — EigenDA, EigenAI, EigenCompute products",
        "requirements": "Stake ETH/LSTs/EIGEN, v1.8.1 contracts mainnet",
        "notes": "Rebranded from EigenLayer. Multiple AVS. GitHub fallback for docs."
    },
    {
        "rank": "C",
        "opportunity": "Road To Devcon Hackathon",
        "type": "Hackathon",
        "signal": "MEDIUM",
        "status": "Online — Opens Aug 8, 2026",
        "url": "https://devfolio.co/hackathons",
        "notes": "Pre-Devcon blockchain hackathon."
    },
    {
        "rank": "D",
        "opportunity": "MUBA Blockchain Hackathon",
        "type": "Hackathon",
        "signal": "MEDIUM",
        "status": "Online — Opens Aug 26, 2026",
        "url": "https://devfolio.co/hackathons",
        "notes": "Blockchain + AI theme."
    },
]

def print_md():
    now = NOW_UTC
    print(f"# Crypto Campaign Tracker — July 2026")
    print(f"**Generated:** {now} / {NOW_MSK}")
    print()
    print("## Top Active Campaigns\n")
    print("| # | Project | Signal | Temp | Status | Chain | Deadline |")
    print("|---|---------|--------|------|--------|-------|----------|")
    for opp in OPPORTUNITIES:
        sig = opp['signal']
        print(f"| {opp['rank']} | **{opp['project']}** | **{sig}** | {opp['temperature']} | {opp['status'][:55]} | {opp['chain'][:20]} | {opp['deadline'][:25]} |")
    
    print()
    print("## Developer / Builder Opportunities\n")
    print("| Rank | Opportunity | Type | Signal | Status |")
    print("|------|-------------|------|--------|--------|")
    for opp in DEVELOPER_OPPS:
        print(f"| {opp['rank']} | {opp['opportunity']} | {opp['type']} | {opp['signal']} | {opp['status'][:55]} |")
    
    print()
    print("## Network Configurations\n")
    print("| Network | Chain ID | RPC | Explorer | Faucet |")
    print("|---------|----------|-----|----------|--------|")
    for opp in OPPORTUNITIES:
        rpc = opp.get('rpc', 'N/A')
        exp = opp.get('explorer', 'N/A')
        fauc = opp.get('faucet', 'N/A')
        cid = opp.get('chain', '').split(',')[0] if ',' in opp.get('chain','') else opp.get('chain','')
        cid = cid.replace('Chain ID ','')
        print(f"| {opp['project']} | {cid} | {rpc} | {exp} | {fauc} |")

def print_table():
    print(f"{'R':<2} {'Project':<20} {'Sig':<5} {'Temp':<10} {'Status':<55}")
    print("-"*92)
    for opp in OPPORTUNITIES:
        print(f"{opp['rank']:<2} {opp['project'][:18]:<20} {opp['signal'][:4]:<5} {opp['temperature']:<10} {opp['status'][:53]:<55}")

def print_json():
    print(json.dumps({"airdrops": OPPORTUNITIES, "developer": DEVELOPER_OPPS}, indent=2, default=str))

if __name__ == "__main__":
    fmt = sys.argv[1] if len(sys.argv) > 1 else "md"
    {
        "json": print_json,
        "table": print_table,
        "md": print_md,
    }.get(fmt, print_md)()
