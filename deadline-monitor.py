#!/usr/bin/env python3
"""
Deadline/Snapshot Monitor — alerts for upcoming campaign deadlines.
Run daily via cron to get notified of approaching deadlines.

Usage:
  python3 deadline-monitor.py        # check all deadlines
  python3 deadline-monitor.py --urgent  # only urgent (within 3 days)
"""

import json, sys
from datetime import datetime, timedelta

NOW = datetime.utcnow()
URGENT_DAYS = 3

DEADLINES = [
    ("AIW3 Snapshot", "2026-07-28", "HIGH", "SNAPSHOT in {days}d! Act NOW before snapshot!"),
    ("AIW3 TGE", "2026-08-03", "HIGH", "TGE in {days}d — snapshot already taken"),
    ("Plether Testnet End", "2026-08-03", "HIGH", "Testnet ends in {days}d — last chance to participate"),
    ("Road To Devcon Hackathon", "2026-08-08", "MEDIUM", "Opens in {days}d"),
    ("MUBA Blockchain Hackathon", "2026-08-26", "MEDIUM", "Opens in {days}d"),
    ("ETHKochi Hackathon (Offline)", "2026-09-05", "LOW", "Starts in {days}d"),
]

def parse_date(ds):
    return datetime.strptime(ds, "%Y-%m-%d")

def check(urgent_only=False):
    alerts = []
    for name, ds, severity, msg_template in DEADLINES:
        d = parse_date(ds)
        delta = (d - NOW).days
        if delta < 0:
            continue  # already passed
        if urgent_only and delta > URGENT_DAYS:
            continue
        msg = msg_template.format(days=delta)
        alerts.append((delta, severity, name, msg))
    
    alerts.sort(key=lambda x: x[0])
    
    if not alerts:
        print("No upcoming deadlines.")
        return
    
    print(f"\n{'='*60}")
    print(f"  DEADLINE MONITOR — {NOW.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}")
    print(f"{'In':<5} {'Severity':<8} {'Event':<30} Message")
    print("-"*70)
    for delta, sev, name, msg in alerts:
        indicator = "⚠️  " if delta <= 3 else "   "
        print(f"{indicator}{delta:<3d}d {sev:<8} {name:<30} {msg}")
    
    # Summary
    urgent = [a for a in alerts if a[0] <= URGENT_DAYS]
    if urgent:
        print(f"\n⚠️  {len(urgent)} URGENT items within {URGENT_DAYS} days!")
    else:
        print(f"\n✓ No urgent deadlines within {URGENT_DAYS} days.")

if __name__ == "__main__":
    urgent = "--urgent" in sys.argv
    check(urgent_only=urgent)
