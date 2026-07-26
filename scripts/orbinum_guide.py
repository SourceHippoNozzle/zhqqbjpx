#!/usr/bin/env python3
"""
Orbinum Testnet Automated Participant — Quick Setup Guide
This script prints instructions and RPC config for manual execution.
Can't auto-sign transactions without wallet access.

Usage: python3 orbinum_guide.py
"""

ORBINUM_RPC = "https://rpc-1.testnet.orbinum.io"

print("=" * 60)
print("  ORBINUM TESTNET — DAILY QUEST GUIDE")
print("  Verified: Chain ID 2700 | Live since Jul 16, 2026")
print("  Airdrop: 20M ORB (2% supply) — Season 1 Genesis Community")
print("=" * 60)

print("""
NETWORK CONFIG (add to MetaMask):
  Network Name:    Orbinum Testnet
  RPC URL:         %s
  Chain ID:        2700 (0xa8c)
  Currency:        tORB (Testnet ORB)
  Explorer:        https://explorer.testnet.orbinum.network

FAUCET:
  1. Join Discord: https://discord.gg/orbinum
  2. Verify your wallet in #faucet channel
  3. Claim 10 tORB (24h cooldown per address)
  4. Faucet: https://faucet.orbinum.network

DAILY QUESTS (Repeatable):
  Each gives ORB Credits -> proportional share of 20M ORB at TGE

  1. SHIELD:    Move tORB from public -> shielded pool (min 1 ORB)
  2. TRANSFER:  Send shielded balance to another privacy address
  3. UNSHIELD:  Bring shielded balance back to public (min 1 ORB)
  4. DISCLOSE:  Verify someone else's transfer with disclosure key

  Max frequency: 3x/week per quest type, 1x/day optimal
  Weekly streak: up to 1.5x multiplier (resets if missed)

STREAK MULTIPLIER:
  Week 1:  1.0x
  Week 2:  1.1x
  Week 3:  1.2x
  Week 4:  1.3x
  Week 5+: 1.5x (max)
  
  Missing a week = multiplier resets to 1.0x

REFERRALS:
  - 10 ORB Credits per verified referral
  - Milestone bonuses at 5/10/25/50 referrals
  - Referral link from dashboard: https://app.orbinum.network

IMPORTANT:
  - Snapshot: 14 days BEFORE mainnet launch (Q4 2026)
  - After snapshot: no more credits count
  - No vesting: full allocation unlocks at TGE
  - Anti-Sybil: one genuine wallet > many farmed ones
  - Testnet tokens have NO real value
""" % ORBINUM_RPC)

if __name__ == "__main__":
    pass
