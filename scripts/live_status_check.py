#!/usr/bin/env python3
"""
Live Status Check — Testnet & Airdrop Campaign Monitor
=======================================================
Pings all tracked project RPC endpoints and web services to verify
liveness, then outputs a consolidated markdown status report.

Usage:
  python3 scripts/live_status_check.py            # Full check, print status
  python3 scripts/live_status_check.py --json     # Output JSON status
  python3 scripts/live_status_check.py --report   # Append to nightly report

Last updated: 2026-07-26 02:45 MSK
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc)
MSK_OFFSET = 3 * 3600  # UTC+3

TRACKER_PATH = os.path.expanduser("~/opportunities_tracker.json")
if not os.path.exists(TRACKER_PATH):
    TRACKER_PATH = os.path.join(os.path.dirname(__file__), "..", "opportunities_tracker.json")

# Projects with known RPC/web endpoints to probe
CHECKS = {
    "Orbinum": {
        "rpc": "https://rpc-1.testnet.orbinum.io",
        "faucet": "https://faucet.orbinum.network",
        "explorer": "https://explorer.testnet.orbinum.network",
        "app": "https://app.orbinum.network",
        "rpc_method": "eth_chainId",
        "expected_chain": "0xa8c",
        "chain_name": "Orbinum Testnet (2700)",
    },
    "DBK Chain": {
        "rpc": "https://rpc.mainnet.dbkchain.io",
        "explorer": None,
        "rpc_method": "eth_chainId",
        "expected_chain": "0x1345f1b",
        "chain_name": "DBK Chain (20240603)",
    },
    "SwarmBase": {
        "web": "https://swarmbase.io",
        "rpc": None,
    },
    "Silent Protocol": {
        "web": "https://app.silentprotocol.org",
        "rpc": None,
    },
    "Merak Testnet": {
        "web": None,
        "rpc": None,
    },
    "AIW3": {
        "web": "https://aiw3.ai",
    },
    "Cambria": {
        "web": "https://lobby.cambria.gg",
    },
    "Tradoor0": {
        "web": "https://tradoor0.xyz",
    },
    "JTX": {
        "web": "https://jtx.app",
    },
    "Plether": {
        "web": None,
        "x": "https://x.com/plether_fi",
        "github": "https://github.com/Plether-Fi",
    },
    "Robinhood Chain": {
        "web": "https://robinhood.com/chain",
    },
    "GIWA": {
        "web": None,
        "rpc": None,  # No public endpoint known
    },
    "3Jane": {
        "web": "https://3jane.xyz",
    },
    "Legend": {
        "web": "https://legend.io",
    },
    "Checkpoint": {
        "web": None,
    },
}


def probe_url(url, timeout=8):
    """Returns (code, msg) for a URL probe."""
    if not url:
        return (None, "no endpoint")
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-o", "/dev/null", "-w", "%{http_code}",
             url],
            capture_output=True, text=True, timeout=timeout + 2
        )
        code = result.stdout.strip()
        if code:
            return (int(code), f"HTTP {code}")
        return (None, "no response")
    except subprocess.TimeoutExpired:
        return (None, "timeout")
    except Exception as e:
        return (None, str(e)[:40])


def probe_rpc(url, method="eth_chainId", params=None, expected=None, timeout=8):
    """Probe an Ethereum JSON-RPC endpoint."""
    if not url:
        return (None, "no rpc")
    body = json.dumps({"jsonrpc": "2.0", "method": method, "params": params or [], "id": 1})
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", str(timeout), "-X", "POST",
             "-H", "Content-Type: application/json", "-d", body, url],
            capture_output=True, text=True, timeout=timeout + 2
        )
        if result.returncode != 0:
            return (None, "curl error")
        data = json.loads(result.stdout)
        val = data.get("result")
        if val is not None:
            ok = "✅" if (expected is None or str(val) == str(expected)) else "⚠️"
            return (val, f"{ok} {val}")
        return (None, f"no result: {data.get('error', {}).get('message', 'unknown')}")
    except json.JSONDecodeError:
        return (None, "invalid json response")
    except subprocess.TimeoutExpired:
        return (None, "timeout")
    except Exception as e:
        return (None, str(e)[:40])


def check_opportunities():
    """Load tracker and augment with live status data."""
    tracker = {}
    if os.path.exists(TRACKER_PATH):
        with open(TRACKER_PATH) as f:
            tracker_list = json.load(f)
        tracker = {item["name"]: item for item in tracker_list}
    
    status_data = {}
    
    for name, config in CHECKS.items():
        print(f"  Probing {name}...", end=" ")
        sys.stdout.flush()
        
        entry = {"name": name, "timestamp": NOW.isoformat()}
        
        # RPC probe
        rpc_url = config.get("rpc")
        if rpc_url:
            val, msg = probe_rpc(rpc_url, 
                                 method=config.get("rpc_method", "eth_chainId"),
                                 expected=config.get("expected_chain"))
            entry["rpc"] = {"url": rpc_url, "result": str(val), "msg": msg}
        
        # Web probe
        web_url = config.get("web")
        if web_url:
            code, msg = probe_url(web_url)
            entry["web"] = {"url": web_url, "status": code, "msg": msg}
        
        # Faucet probe
        faucet_url = config.get("faucet")
        if faucet_url:
            code, msg = probe_url(faucet_url)
            entry["faucet"] = {"url": faucet_url, "status": code, "msg": msg}
        
        # Explorer probe
        explorer_url = config.get("explorer")
        if explorer_url:
            code, msg = probe_url(explorer_url)
            entry["explorer"] = {"url": explorer_url, "status": code, "msg": msg}
        
        # App probe
        app_url = config.get("app")
        if app_url:
            code, msg = probe_url(app_url)
            entry["app"] = {"url": app_url, "status": code, "msg": msg}
        
        # X probe
        x_url = config.get("x")
        if x_url:
            code, msg = probe_url(x_url)
            entry["x"] = {"url": x_url, "status": code, "msg": msg}
        
        # GitHub probe
        gh_url = config.get("github")
        if gh_url:
            code, msg = probe_url(gh_url)
            entry["github"] = {"url": gh_url, "status": code, "msg": msg}
        
        # Determine overall status
        results = []
        if "rpc" in entry:
            results.append(entry["rpc"]["msg"])
        if "web" in entry:
            results.append(entry["web"]["msg"])
        if "faucet" in entry:
            results.append("faucet:" + entry["faucet"]["msg"])
        if "app" in entry:
            results.append("app:" + entry["app"]["msg"])
        if "explorer" in entry:
            results.append("exp:" + entry["explorer"]["msg"])
        
        entry["summary"] = " | ".join(results)
        status_data[name] = entry
        
        # Check if all probes show good
        all_good = True
        for key in ["rpc", "web", "faucet", "app", "explorer"]:
            if key in entry:
                val = entry[key].get("result") if key == "rpc" else entry[key].get("status")
                if val is None or (key == "rpc" and val == "None") or (isinstance(val, int) and val >= 400):
                    all_good = False
        
        print("✅" if all_good else "❌")
        sys.stdout.flush()
        time.sleep(0.3)  # Rate limit
    
    return status_data


def print_report(status_data):
    """Print markdown status report."""
    print("\n" + "=" * 70)
    print("  TESTNET & AIRDROP LIVE STATUS — 2026-07-26")
    print("  Generated:", NOW.strftime("%H:%M UTC"), f"({NOW.timestamp():.0f})")
    print("=" * 70)
    
    for name, data in status_data.items():
        print(f"\n### {name}")
        rpc_result = data.get("rpc", {}).get("msg", "")
        web_result = data.get("web", {}).get("msg", "")
        faucet_result = data.get("faucet", {}).get("msg", "")
        app_result = data.get("app", {}).get("msg", "")
        explorer_result = data.get("explorer", {}).get("msg", "")
        x_result = data.get("x", {}).get("msg", "")
        gh_result = data.get("github", {}).get("msg", "")
        
        parts = []
        if rpc_result:
            parts.append(f"RPC: {rpc_result}")
        if web_result:
            parts.append(f"Web: {web_result}")
        if faucet_result:
            parts.append(f"Faucet: {faucet_result}")
        if app_result:
            parts.append(f"App: {app_result}")
        if explorer_result:
            parts.append(f"Explorer: {explorer_result}")
        if x_result:
            parts.append(f"X: {x_result}")
        if gh_result:
            parts.append(f"GitHub: {gh_result}")
        
        print("- " + "\n- ".join(parts))
    
    # Summary
    total = len(status_data)
    online = sum(1 for n, d in status_data.items() 
                 if any(d.get(k, {}).get("msg", "").startswith("✅") or 
                        (isinstance(d.get(k, {}).get("status"), int) and d[k]["status"] < 400)
                        for k in ["rpc", "web", "faucet", "app"] if k in d))
    print(f"\n---\n**Status: {online}/{total} projects reachable**")


def update_tracker_with_status(status_data):
    """Update the opportunities_tracker.json with last_verified timestamps."""
    if not os.path.exists(TRACKER_PATH):
        print(f"Tracker not found at {TRACKER_PATH}")
        return
    
    with open(TRACKER_PATH) as f:
        tracker = json.load(f)
    
    updated = 0
    for item in tracker:
        name = item["name"]
        if name in status_data:
            stats = status_data[name]
            # Add live checks
            if "rpc" in stats:
                item["rpc_status"] = stats["rpc"]["msg"]
                item["rpc_chain"] = str(stats["rpc"]["result"])
            if "web" in stats:
                item["web_status"] = stats["web"]["msg"]
            item["last_verified"] = NOW.isoformat()
            updated += 1
    
    with open(TRACKER_PATH, "w") as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Updated {updated}/{len(tracker)} entries in tracker with live status.")


if __name__ == "__main__":
    do_json = "--json" in sys.argv
    do_update = "--update" in sys.argv
    
    print("🔍 Live Status Check — Probing all tracked projects...\n")
    status = check_opportunities()
    
    if do_json:
        print(json.dumps(status, indent=2))
    else:
        print_report(status)
    
    if do_update:
        update_tracker_with_status(status)
    
    # Save JSON for reference
    output_path = os.path.expanduser("~/live_status_2026-07-26.json")
    with open(output_path, "w") as f:
        json.dump(status, f, indent=2)
    print(f"\n📄 Raw status saved to: {output_path}")
