# Node-Running & AVS Opportunities — July 2026

Research for Pavel (tringt). Sources: official docs, GitHub READMEs, verified July 26, 2026.

---

## 1. EigenLayer AVS Operator Program

| Field | Details |
|-------|---------|
| **Type** | Restaking / AVS operator |
| **Network** | Ethereum mainnet + Sepolia/Hoodi testnets |
| **Status** | ✅ Live (v1.9.0-rc.0 on testnets) |
| **Requirements** | Needs ETH/LST to restake — real capital on mainnet, testnet ETH on Sepolia/Hoodi |
| **Barrier** | HIGH — requires actual staked ETH (32 ETH mainnet, testnet ETH on Hoodi) |
| **Source** | github.com/Layr-Labs/eigenlayer-contracts |
| **Verdict** | ❌ Not free. Needs real capital or testnet ETH mining. |

## 2. Hyperlane Validator

| Field | Details |
|-------|---------|
| **Type** | Interchain validator |
| **Network** | Multiple chains (Ethereum, Solana, etc.) |
| **Status** | ✅ V3 Live |
| **Requirements** | Run a validator node, potentially stake |
| **Barrier** | MEDIUM — needs dedicated infra, may need stake |
| **Source** | docs.hyperlane.xyz, github.com/hyperlane-xyz/hyperlane-monorepo |
| **Verdict** | ⏳ Under investigation. May be permissionless. |

## 3. Hoodi Testnet Validator (ETH)

| Field | Details |
|-------|---------|
| **Type** | Ethereum PoS validator (testnet) |
| **Network** | Hoodi (chain ID 560048) — replaces Holesky |
| **Status** | ✅ Live since Mar 17, 2025 |
| **Requirements** | 32 testnet ETH (mineable via PoW faucet or request) |
| **Faucet** | hoodi-faucet.pk910.de (PoW mining faucet) |
| **Barrier** | LOW — need to mine 32 testnet ETH via PoW faucet |
| **Launchpad** | hoodi.launchpad.ethereum.org |
| **Explorers** | hoodi.etherscan.io, hoodi.beaconcha.in |
| **LTS** | Until Dec 2028 |
| **Verdict** | ✅ Free to try! Mine testnet ETH at faucet, run a validator node. |

## 4. Babylon Chain

| Field | Details |
|-------|---------|
| **Type** | Bitcoin staking protocol |
| **Status** | ⏳ Repo not found (404 on GitHub) — may have moved |
| **Verdict** | ❌ Cannot verify. May have rebranded. |

## 5. Lido CSM (Community Staking Module)

| Field | Details |
|-------|---------|
| **Type** | Staking pool operator (testnet) |
| **Network** | Ethereum |
| **Status** | ⏳ Blog behind Cloudflare — cannot verify |
| **Verdict** | ⏳ Blocked by Cloudflare. Check manually. |

## 6. Orbinum Node

| Field | Details |
|-------|---------|
| **Type** | Substrate node operator (testnet) |
| **Network** | Orbinum Testnet (chain ID 2700) |
| **Status** | ✅ Live, 144K+ blocks, v0.2.0 |
| **Node Image** | `ghcr.io/orbinum/node:testnet-latest` (Docker) |
| **Requirements** | Run a Docker node, faucet: 10 ORB/day |
| **Barrier** | LOW — Docker installation, testnet tokens from faucet |
| **Source** | docs.orbinum.network |
| **Verdict** | ✅ Free! Docker-based node. Testnet tokens from faucet. |

---

## Top Free Opportunities

| Prio | Program | Effort | Why |
|------|---------|--------|-----|
| 1 | **Orbinum Node** | Docker pull + run | Live testnet, verified, Season 1 airdrop |
| 2 | **Hoodi Validator** | Mine 32 ETH + run client | Full ETH staking experience on testnet, LTS until 2028 |

## Blocked

- **EigenLayer AVS**: Needs real staked ETH/LST
- **Babylon**: Repo not found
- **Lido CSM**: Cloudflare block
- **Hyperlane**: Under investigation
