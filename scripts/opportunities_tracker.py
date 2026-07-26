#!/usr/bin/env python3
"""
Crypto Opportunities Tracker v2
===============================
Unified scanner and tracker for active testnet campaigns, retrodrops,
node-running opportunities, and builder programs.
Last updated: 2026-07-26

Usage:
  python3 opportunities_tracker.py          — full scan (aggregator fetch + report)
  python3 opportunities_tracker.py --status  — show saved tracker status only
  python3 opportunities_tracker.py --update  — re-fetch aggregators and update
"""

import json, os, sys, subprocess, re
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional

TRACKER_PATH = os.path.expanduser("~/opportunities_tracker.json")
REPORT_PATH = os.path.expanduser("~/night_crypto_report_2026-07-26.md")

@dataclass
class Opportunity:
    name: str
    category: str           # testnet, retrodrop, node-running, builder-grant, hackathon
    chain: str
    temperature: int = 0
    confirmed: bool = False
    status: str = "unknown"  # active, pending, expired, done
    actions: str = ""
    start_date: str = ""
    end_date: str = ""
    url: str = ""
    notes: str = ""
    created: str = ""
    updated: str = ""

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, d):
        return cls(**{k: d.get(k, "") for k in cls.__annotations__})

class TrackerDB:
    def __init__(self):
        self.opportunities: list[Opportunity] = []
        self.load()
    
    def load(self):
        if os.path.exists(TRACKER_PATH):
            try:
                with open(TRACKER_PATH) as f:
                    data = json.load(f)
                    self.opportunities = [Opportunity.from_dict(d) for d in data]
            except:
                self.opportunities = []
    
    def save(self):
        os.makedirs(os.path.dirname(TRACKER_PATH), exist_ok=True)
        with open(TRACKER_PATH, 'w') as f:
            json.dump([o.to_dict() for o in self.opportunities], f, indent=2)
    
    def upsert(self, opp: Opportunity):
        for i, o in enumerate(self.opportunities):
            if o.name.lower() == opp.name.lower():
                opp.created = o.created or opp.created
                self.opportunities[i] = opp
                return
        opp.created = datetime.now(timezone.utc).isoformat()
        self.opportunities.append(opp)
    
    def get(self, name: str) -> Optional[Opportunity]:
        for o in self.opportunities:
            if o.name.lower() == name.lower():
                return o
        return None
    
    def list_active(self):
        return [o for o in self.opportunities if o.status == 'active']
    
    def list_by_temperature(self):
        return sorted(self.opportunities, key=lambda x: -x.temperature)


def fetch_airdrops_io():
    """Fetch and parse airdrops.io latest + speculative pages."""
    import urllib.request
    opportunities = []
    
    for page_type, url in [
        ("latest", "https://airdrops.io/latest/"),
        ("speculative", "https://airdrops.io/speculative/"),
    ]:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                html = resp.read().decode('utf-8', errors='replace')
            
            # Parse article cards
            pattern = r'<article[^>]*class="grid-33 airdrop-click[^"]*"[^>]*>.*?</article>'
            for article in re.findall(pattern, html, re.DOTALL):
                name_m = re.search(r'<h3>(.*?)</h3>', article)
                if not name_m:
                    continue
                name = name_m.group(1).strip()
                
                temp_m = re.search(r'data-temperature="(\d+)"', article)
                temperature = int(temp_m.group(1)) if temp_m else 0
                
                confirmed = 'confirmed' in article
                cats = re.findall(r'categories-(\S+)', article)
                
                actions_m = re.search(r'Actions:\s*<span>(.*?)</span>', article)
                actions = actions_m.group(1).strip() if actions_m else ""
                
                start_m = re.search(r'data-start="([^"]*)"', article)
                ends_m = re.search(r'data-ends="([^"]*)"', article)
                
                opp = Opportunity(
                    name=name,
                    category="retrodrop" if confirmed else "speculative-retrodrop",
                    chain=",".join(cats[:3]) if cats else "",
                    temperature=temperature,
                    confirmed=confirmed,
                    status="active",
                    actions=actions[:100],
                    start_date=start_m.group(1) if start_m else "",
                    end_date=ends_m.group(1) if ends_m else "",
                    url=f"https://airdrops.io/{name.lower().replace(' ','-')}/",
                    updated=datetime.now(timezone.utc).isoformat()
                )
                opportunities.append(opp)
        except Exception as e:
            print(f"  [WARN] Failed to fetch {page_type}: {e}", file=sys.stderr)
    
    return opportunities


def generate_report(db: TrackerDB):
    """Generate the nightly report markdown."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    lines = [
        "# Night Crypto Mission Report — 2026-07-26",
        "",
        f"**Operator:** Pavel (tringt)",
        f"**Generated:** {now}",
        f"**Status:** Final",
        "",
        "---",
        "",
        "## Active Opportunities (Ranked by Temperature)",
        "",
        "| # | Project | Category | Chain | Temp | Confirmed | Status | Actions | Deadline |",
        "|---|---------|----------|-------|------|-----------|--------|---------|----------|",
    ]
    
    for i, opp in enumerate(db.list_by_temperature(), 1):
        if opp.status != 'active':
            continue
        conf = "✅" if opp.confirmed else " "
        deadline = opp.end_date if opp.end_date else "-"
        lines.append(
            f"| {i} | {opp.name} | {opp.category} | {opp.chain} | {opp.temperature}° | {conf} | "
            f"{opp.status} | {opp.actions} | {deadline} |"
        )
    
    lines += [
        "",
        "---",
        "",
        "## 🔥 Top Priority Projects",
        "",
    ]
    
    # Top 5 detailed
    top5 = [o for o in db.list_by_temperature() if o.status == 'active'][:5]
    for opp in top5:
        lines += [
            f"### {opp.name} ({opp.temperature}°)",
            f"- **Category:** {opp.category}",
            f"- **Chain:** {opp.chain}",
            f"- **Airdrop Confirmed:** {'✅ Yes' if opp.confirmed else '❌ Speculative'}",
            f"- **Actions:** {opp.actions}",
            f"- **Official:** {opp.url}",
            f"- **Deadline:** {opp.end_date or 'Ongoing'}",
            f"- **Notes:** {opp.notes}",
            "",
        ]
    
    lines += [
        "---",
        "",
        "## 🚀 Node-Running Opportunities",
        "",
        "### DBK Chain (DeBank L2)",
        "- **What:** DeBank's own OP Stack L2 — mainnet live",
        "- **Setup:** https://github.com/DeBankDeFi/rollup-node-dbkchain",
        "- **Requirements:** Follow standard OP Stack node requirements",
        "- **Genesis NFT:** Mint available at dbkchain.io — early adopter signal",
        "- **Significance:** DeBank is the #1 crypto portfolio tracker — their L2 is strategically important",
        "",
        "---",
        "",
        "## 📋 Builder / Developer Opportunities",
        "",
        "| # | Opportunity | Type | Requirements | Deadline |",
        "|---|-------------|------|-------------|----------|",
        "| 1 | DBK Chain build | L2 dev (OP Stack) | Deploy contracts on DBK Chain | Ongoing |",
        "| 2 | Cambria game integration | Gaming/Base | Create dApp on Base interacting with RSGP | Ongoing |",
        "| 3 | Polymarket ts-sdk contributions | SDK dev | PRs to Polymarket TypeScript SDK | Ongoing |",
        "",
        "---",
        "",
        "## 🧰 Created Assets",
        "",
        "| Asset | Path | Purpose |",
        "|-------|------|---------|",
        "| Tracker Script | opportunities_tracker.py | Autonomous scanner for aggregators + local DB |",
        "| DBK Chain Guide | dbk_chain_guide.md | Node setup + development reference for DeBank L2 |",
        "| This Report | night_crypto_report_2026-07-26.md | Mission report with findings and action items |",
        "",
        "---",
        "",
        "## Current Date & Time",
        f"{now}",
        "",
    ]
    
    return "\n".join(lines)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Crypto Opportunities Tracker")
    parser.add_argument("--update", action="store_true", help="Fetch fresh aggregator data")
    parser.add_argument("--status", action="store_true", help="Show current tracker status")
    args = parser.parse_args()
    
    db = TrackerDB()
    
    if args.update or len(sys.argv) == 1:
        print("Fetching aggregator data...")
        new_opps = fetch_airdrops_io()
        for opp in new_opps:
            existing = db.get(opp.name)
            if existing:
                existing.temperature = opp.temperature
                existing.confirmed = opp.confirmed
                existing.updated = opp.updated
                existing.actions = opp.actions
                existing.url = opp.url
            else:
                db.upsert(opp)
        db.save()
        print(f"Saved {len(db.opportunities)} opportunities to tracker.")
    
    if args.status:
        print(f"\nTracker has {len(db.opportunities)} opportunities")
        print(f"Active: {len(db.list_active())}")
        for opp in db.list_by_temperature()[:10]:
            print(f"  [{opp.temperature:3d}°] {opp.name:30s} | {opp.category:20s} | {opp.status}")
    
    # Always regenerate report
    report = generate_report(db)
    with open(REPORT_PATH, 'w') as f:
        f.write(report)
    print(f"Report regenerated: {REPORT_PATH}")
