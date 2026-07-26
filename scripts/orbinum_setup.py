#!/usr/bin/env python3
"""
Orbinum Network Testnet — Wallet Setup & Interaction Guide (2026-07-26)

This script generates the RPC configuration and prints step-by-step instructions.
The faucet requires manual interaction (Turnstile CAPTCHA + Discord verification).

Chain Info:
  - Name: Orbinum Testnet
  - Chain ID: 2700 (0xa8c)
  - RPC: https://rpc-1.testnet.orbinum.io
  - Explorer: https://explorer.testnet.orbinum.network
  - Faucet: https://faucet.orbinum.network (Turnstile CAPTCHA)
  - App: https://app.orbinum.network
  - Docs: https://docs.orbinum.network
  - Gas: ~0.5 gwei (500,000,000 wei)

Network Type: Substrate + EVM (Frontier pallet)
Token: ORB (testnet, no real value)
Airdrop: Confirmed — 2% of $ORB supply to testnet users
Community temp: 193° on airdrops.io
"""

RPC_URL = "https://rpc-1.testnet.orbinum.io"
CHAIN_ID = 2700
EXPLORER = "https://explorer.testnet.orbinum.network"
FAUCET = "https://faucet.orbinum.network"

import subprocess
import json

def check_rpc():
    """Verify RPC is responding"""
    import urllib.request
    data = json.dumps({"jsonrpc": "2.0", "method": "eth_chainId", "params": [], "id": 1}).encode()
    req = urllib.request.Request(RPC_URL, data=data, headers={"Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        result = json.loads(resp.read())
        chain_id = int(result["result"], 16)
        print(f"✅ RPC Live — Chain ID: {chain_id} ({hex(chain_id)})")
        return chain_id == CHAIN_ID
    except Exception as e:
        print(f"❌ RPC Error: {e}")
        return False

def print_config():
    """Print network config for manual wallet setup"""
    print("""
=== ORBINUM NETWORK CONFIGURATION ===

Add to MetaMask / Rabby / any EVM wallet:

  Network Name:     Orbinum Testnet
  RPC URL:         https://rpc-1.testnet.orbinum.io
  Chain ID:        2700 (0xa8c)
  Currency Symbol: ORB
  Explorer:        https://explorer.testnet.orbinum.network

=== DAILY ACTIONS ===
1. Visit https://faucet.orbinum.network — solve Turnstile — claim 10 ORB
2. Go to https://app.orbinum.network — connect wallet
3. Test shielded transfers (privacy feature)
4. Regular EVM transactions (any dApps on the network)
5. Check Discord for faucet/reset announcements: https://discord.gg/orbinum

=== $ORB AIRDROP ===
- Status: CONFIRMED — 2% of total supply allocated to testnet users
- Snapshot: TBD (still in testnet phase)
- Strategy: Daily faucet claims + shielded transfers + general activity
- Competition: LOW (very early, quiet project)
""")

def main():
    print("=" * 60)
    print("  ORBINUM TESTNET — Status Check & Setup Guide")
    print("  Generated: 2026-07-26 22:45 MSK")
    print("=" * 60)
    
    check_rpc()
    print_config()

if __name__ == "__main__":
    main()
