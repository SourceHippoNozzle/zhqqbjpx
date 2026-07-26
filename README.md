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

## Latest Verified Data

| Campaign | Signal | Status | Urgency |
|----------|--------|--------|---------|
| **AIW3** | 98° ✅ CONFIRMED | Snapshot Jul 28, TGE Aug 3 | ⚠️ 2 days |
| **Cambria** | 265° ✅ CONFIRMED | $RSGP TGE Aug 2026 | 🔥 Hot |
| **Orbinum** | 193° ✅ CONFIRMED | Season 1 (2M ORB), testnet live | 📡 Active |
| **SwarmBase** | 56° ✅ CONFIRMED | 20% of 1B $SWARM | 🆕 New |
| **Plether** | 24° ✅ CONFIRMED | Ends Aug 3 | ⏳ Limited |

## Builder Opportunities

| Project | Issue | Tech | Effort |
|---------|-------|------|--------|
| **Polymarket/ts-sdk** | Openfort wallet provider (#121) | TypeScript, viem | Medium |

## Repo Contents

| Path | Description |
|------|-------------|
| `docs/campaigns.md` | Full campaign details, URLs, action items |
| `scripts/monitor.sh` | Automated status check script |
| `scripts/campaign_dashboard.py` | Rich CLI dashboard with URL checks |
| `scripts/orbinum_guide.py` | Orbinum testnet setup guide |
| `references/` | Source links and extracted data |
| `testnet_tracker.py` | JSON-backed opportunity tracker (copied to ~/) |
