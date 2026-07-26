# Orbinum Network Testnet Research Report

**Date:** July 26, 2026
**Sources checked:** Official website, docs, RPC, faucet, explorer, app, GitHub

---

## 1. Project Overview

- **Name:** Orbinum Network
- **Category:** Privacy-focused L1 blockchain
- **Tech stack:** Substrate (FRAME) with EVM compatibility (Frontier)
- **Privacy mechanism:** ZK-SNARKs (Groth16 over BN254 with Poseidon hashing), Circom circuits
- **Official website:** https://orbinum.network
- **Twitter/X:** @orbinumnetwork
- **GitHub:** https://github.com/orbinum
- **Discord:** https://discord.gg/orbinum

---

## 2. Testnet Status — ✅ LIVE AND ACCESSIBLE

| Check | Result |
|-------|--------|
| Chain name via RPC | `system_chain` → **"Orbinum Testnet"** |
| Latest block | `eth_blockNumber` → **0x23320 (144,160 blocks)** |
| Status | ✅ **Live and actively producing blocks** |

The testnet is in **public testnet phase (Q3 2026)**, which started with Q2 R&D and community launch.

---

## 3. RPC Endpoints

| Type | URL | Status |
|------|-----|--------|
| **Ethereum JSON-RPC** | `https://rpc-1.testnet.orbinum.io` | ✅ 200 (method not allowed on GET, responds to POST) |
| WebSocket | `wss://rpc-1.testnet.orbinum.io/ws` | Likely (WSS endpoint exists, behind Cloudflare) |
| Substrate RPC (same port) | `https://rpc-1.testnet.orbinum.io` | ✅ Responds to Substrate methods |

No additional RPC endpoints (rpc-2, rpc.testnet) were found via DNS.

---

## 4. Chain ID

**Chain ID: 2700** (`0xa8c`)

Verified via `eth_chainId` RPC call:
```json
{"jsonrpc":"2.0","id":1,"result":"0xa8c"}
```

---

## 5. Faucet

| Detail | Value |
|--------|-------|
| **Faucet URL** | https://faucet.orbinum.network |
| **Authentication** | Discord-based (must be a member of Orbinum Discord server) |
| **Amount** | 10 ORB per claim |
| **Cooldown** | Every 24 hours (per address) |
| **Wallet required** | EVM wallet address |
| **Status** | ✅ Live and accessible (200 OK) |

---

## 6. Explorer

| Detail | Value |
|--------|-------|
| **Explorer URL** | https://explorer.testnet.orbinum.network |
| **Name** | "Orbinum Privacy Explorer" |
| **Focus** | Shielded transactions, ZK proofs, private activity |
| **Status** | ✅ Live and accessible (200 OK) |

---

## 7. App (Web dApp)

| Detail | Value |
|--------|-------|
| **App URL** | https://app.orbinum.network |
| **Name** | "Orbinum Hub" |
| **Features** | Wallet connection, Private Pool (shield/transfer/unshield/disclosure), Community quests, Activity history |

---

## 8. Season 1: Genesis Community

| Detail | Value |
|--------|-------|
| **Started** | Friday, March 13, 2026 |
| **Ends** | Exactly 14 days before Mainnet Launch (TGE) |
| **Rewards pool** | **20,000,000 ORB** (2% of total supply) |
| **Distribution model** | Proportional — based on ORB Credits relative to total community credits |
| **Status** | ✅ **Active Campaign** |

### Testnet Quests (4 on-chain quests)

| Quest | Description | Min Amount | Frequency | Proof Type |
|-------|-------------|-----------|-----------|------------|
| **Shield** | Move ORB from public → shielded pool | 1 ORB | 3×/week, 1×/day | Transaction hash |
| **Private Transfer** | Send shielded balance to privacy address | None | 3×/week, 1×/day | Disclosure key (`orbdisc:...`) |
| **Unshield** | Bring shielded balance back to public | 1 ORB | 3×/week, 1×/day | Transaction hash |
| **Selective Disclosure** | Verify someone else's transfer | None (their note) | 3×/week, 1×/day | Someone else's disclosure key |

Additional features: **Weekly streaks** (up to 1.5× multiplier), **Referral system**, **Levels & Roles** with signup bonus of **+20 ORB Credits**.

---

## 9. Roadmap & Milestones

| Phase | Period | Status |
|-------|--------|--------|
| Q1 2026: Research & Development | Jan–Mar 2026 | ✅ Completed |
| Q2 2026: R&D & Community Program | Apr–Jun 2026 | ✅ Completed |
| **Q3 2026: Public Testnet & Public-sale** | **Jul–Sep 2026** | **🔵 In Progress** |
| **Q4 2026: Mainnet Launch** | **Oct–Dec 2026** | **⏳ Pending** |

### Q4 2026 Mainnet milestones:
- Season 1 End (Credits Snapshot & TGE)
- Genesis ceremony
- Audits finalization
- Validators selection for mainnet
- Initial exchange liquidity
- **Mainnet Launch**

---

## 10. Infrastructure Details

- **Node image:** `ghcr.io/orbinum/node:testnet-latest` (private GHCR package)
- **Node repo:** https://github.com/orbinum/node
- **Docs repo:** https://github.com/orbinum/docs
- **Deployment:** Docker-based via docker-compose
- **Infrastructure:** Cloudflare-protected (DDoS mitigation, WAF, rate limiting)
- **Domain pattern:**
  - Main site: `orbinum.network`
  - App: `app.orbinum.network`
  - Faucet: `faucet.orbinum.network`
  - Docs: `docs.orbinum.network`
  - Explorer: `explorer.testnet.orbinum.network`
  - RPC: `rpc-1.testnet.orbinum.io`

---

## 11. Summary of Verified Data

| Field | Value | Source |
|-------|-------|--------|
| Chain ID | **2700** (0xa8c) | RPC `eth_chainId` |
| RPC URL | `https://rpc-1.testnet.orbinum.io` | DNS + docs |
| Faucet URL | `https://faucet.orbinum.network` | Docs + direct check |
| Explorer URL | `https://explorer.testnet.orbinum.network` | Docs |
| App URL | `https://app.orbinum.network` | Direct check |
| Docs URL | `https://docs.orbinum.network` | Direct check |
| Testnet live? | **✅ Yes** — 144,160+ blocks | RPC `eth_blockNumber` |
| Testnet name | "Orbinum Testnet" | RPC `system_chain` |
| Season 1 start | March 13, 2026 | Docs |
| Mainnet TGE | Q4 2026 (Oct–Dec) | Docs roadmap |
| Season 1 allocation | 20M ORB (2% of total supply) | Docs |
| Node version | `ghcr.io/orbinum/node:testnet-latest` | Docs |
