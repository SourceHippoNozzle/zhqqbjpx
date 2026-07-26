# DBK Chain (DeBank L2) — Development & Node Running Guide

> **Last updated:** 2026-07-26
> **Source:** https://docs.dbkchain.io

## Overview

DBK Chain is DeBank's own Layer 2 blockchain built on the OP Stack (Optimism).
As DeBank is the #1 crypto portfolio tracker by user base, their L2 represents
a significant strategic infrastructure play.

**Status:** Mainnet live — no testnet detected.
**Chain ID:** 20240603
**Currency:** ETH
**RPC:** https://rpc.mainnet.dbkchain.io/
**Explorer:** https://scan.dbkchain.io/
**Bridge:** Ethereum ↔ DBK via Optimism SDK (bridge contract on ETH: 0x735aDBbE72226BD52e818E7181953f42E3b0FF21)

## Development

### Deploy Contracts
- Follow standard Optimism/OP Stack development patterns
- Use Foundry or Hardhat
- Set chain ID to 20240603
- Bridge assets from Ethereum via Optimism SDK
- Contract verification: https://docs.dbkchain.io/build-on-dbk-chain/deploy-new-contracts.md

### Useful Addresses
From: https://docs.dbkchain.io/general-info/mainnet-contract-addresses.md
- SFS contract
- L1Standard Bridge
- Token addresses (official tokens deployed by Mode/DeBank team)

## Node Running

### Requirements
- GitHub: https://github.com/DeBankDeFi/rollup-node-dbkchain
- Standard OP Stack node requirements (suggested: 8+ vCPU, 32GB+ RAM, 500GB+ SSD)
- Follow standard rollup node setup procedure

### Quick Start
```bash
git clone https://github.com/DeBankDeFi/rollup-node-dbkchain
cd rollup-node-dbkchain
# Follow setup instructions in repo README
```

## Genesis NFT

DBK Chain offered a Genesis NFT (via Rabby Wallet integration).
- **Action:** Install Rabby Wallet → Connect to DBK Chain → Mint Genesis NFT
- **Significance:** Early adopter marker — potential future airdrop/token criteria

## Strategy Notes

1. **Node running** — Run an OP Stack node for DBK Chain to support network
   decentralization and potentially qualify for future operator rewards
2. **Building** — Deploy dApps early. DeBank's user base (10M+ users) gives
   DBK Chain immediate distribution advantage over other L2s
3. **Genesis NFT** — If not already minted, this is a low-cost early signal

## Links
- Official: https://dbkchain.io
- Docs: https://docs.dbkchain.io
- GitHub (DeBankDeFi): https://github.com/DeBankDeFi
- Explorer: https://scan.dbkchain.io
- RPC: https://rpc.mainnet.dbkchain.io/
