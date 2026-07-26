# Testnet Campaign Reconnaissance

**Curated findings, scripts, and action plans for Web3 testnet participation.**

Maintained for Pavel (tringt). Last updated: 2026-07-26.

## Active Campaigns (Tier 1)

| Project | Type | Status | Signal |
|---------|------|--------|--------|
| **Canopy** | L1 framework testnet | ✅ Confirmed airdrop | 50% $CNPY to community |
| **Arc** | Circle L1 testnet | 🔮 Speculative | $222M presale, 60% ecosystem |
| **GIWA** | Upbit L2 testnet | 🔮 Speculative | 100M+ txns, Base/Ink precedent |
| **Robinhood Chain** | L1 ecosystem | 🔮 No token yet | Launched Jul 1, free gas 90d |

## Early Stage (Tier 2)

Orbinum, Sekai, Checkpoint, Monetrix, BULK, Hylo — see `testnet_tracker.py`

## Infrastructure & Node Programs (Tier 3)

EigenCloud (AVS), Hyperlane (AVS), AltLayer (AVS/RaaS), Story/DATA (node), Farcaster/Snapchain (node)

## Quickstart

```bash
# View all tracked campaigns
python3 ~/testnet_tracker.py

# Mark all as checked
python3 ~/testnet_tracker.py --check
```

## Repo Contents

| Path | Description |
|------|-------------|
| `docs/campaigns.md` | Full campaign details, URLs, action items |
| `scripts/monitor.sh` | Automated status check script |
| `references/` | Source links and extracted data |
| `testnet_tracker.py` | JSON-backed opportunity tracker (copied to ~/) |
