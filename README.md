# Crypto Campaign Tracker

Automated campaign tracking for testnet, airdrop, and builder opportunities.

## Quick Start

```bash
# View markdown report
python3 tracker.py

# View terminal table
python3 tracker.py table

# Check upcoming deadlines
python3 deadline-monitor.py

# Urgent deadlines only
python3 deadline-monitor.py --urgent
```

## Tracked Campaigns (July 2026)

| Priority | Project | Signal | Deadline | Actions |
|----------|---------|--------|----------|---------|
| 🏆 #1 | **Orbinum Network** | HIGH 🔥 | Ongoing (TBD) | Interact with privacy testnet |
| ⏰ #2 | **AIW3** | HIGH 🔥 | **Snapshot Jul 28!** | Register, do daily tasks |
| ⏰ #3 | **Plether** | HIGH | **Ends Aug 3** | Join perp DEX testnet |
| #4 | Cambria | MEDIUM | Ongoing | Solana gaming |
| #5 | SwarmBase | MEDIUM | Ongoing | AI agents, daily check-in |
| #6 | Monaco Trading | MEDIUM | Speculative | Sei testnet |
| #7 | DBK Chain | MEDIUM | Ongoing | Mint Genesis NFT |

## Network Configs

### Orbinum Testnet
- **Chain ID:** 2700 (0xA8C)
- **RPC:** https://rpc-1.testnet.orbinum.io
- **Explorer:** https://explorer.testnet.orbinum.io
- **Faucet:** https://faucet.orbinum.network (Cloudflare Turnstile)
- **Docs:** https://docs.orbinum.network
- **GitHub:** github.com/orbinum

### Tempo Moderato (already active)
- **Chain ID:** 42431
- **RPC:** https://rpc.moderato.tempo.xyz
- **Gas:** Fee-less (TIP-20 stablecoins)
- **Balances:** PathUSD 999,984 | AlphaUSD 999,989 | BetaUSD 999,994 | ThetaUSD 999,994

## Past Campaigns (Completed)

### Night 2026-07-25: 40 on-chain transactions across 4 networks
| Network | Txns | Highlights |
|---------|------|------------|
| Sepolia | 5 | HTT token deployed (Vyper 0.4.3) |
| BSC Testnet | 12 | PancakeSwap swap, HCAMP token deployed |
| Tempo Moderato | 14 | Stablecoin burns, faucet claimed |
| Avalanche Fuji | 9 | HCAMP token deployed |
| **Total** | **40** | |

## Setup

```bash
# Clone
git clone git@github.com:SourceHippoNozzle/crypto-campaign-tracker.git
cd crypto-campaign-tracker

# Run tracker
python3 tracker.py
```

## Safety

- ❌ No real money ever touched
- ❌ No wallet connections to unknown sites
- ❌ No private keys shared or stored
- ✅ Testnet-only activity
- ✅ Open source scripts
- ✅ Faucet-sourced tokens only
