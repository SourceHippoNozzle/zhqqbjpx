#!/usr/bin/env python3
"""
Orbinum Testnet Validator Check — 2026-07-26
Verifies Orbinum network endpoints and chain status.
Usage: python3 orbinum_validator.py
"""
import json
import subprocess
import sys

RPC = "https://rpc-1.testnet.orbinum.io"
EXPLORER = "https://explorer.testnet.orbinum.network"
FAUCET = "https://faucet.orbinum.network"
CHAIN_ID = 2700

def call_rpc(method, params=None):
    """Call JSON-RPC method via curl."""
    if params is None:
        params = []
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    })
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-X", "POST",
             "-H", "Content-Type: application/json",
             "-d", data, RPC],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            resp = json.loads(result.stdout)
            return resp.get("result")
        return f"ERROR: curl exit {result.returncode}"
    except Exception as e:
        return f"ERROR: {e}"

def check_url(url, label):
    """Check URL reachability via curl."""
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", "10", "-o", "/dev/null",
             "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=15
        )
        code = result.stdout.strip()
        if code == "405" and label == "RPC Node":
            return "✅ Alive (RPC accepts POST only)"
        if code == "200":
            return "HTTP 200 ✅ OK"
        return f"HTTP {code}"
    except Exception as e:
        return f"FAIL: {e}"

def main():
    print("=" * 60)
    print("  ORBINUM TESTNET VALIDATOR CHECK")
    print(f"  {__import__('datetime').datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    print(f"\n--- Endpoint Health ---")
    endpoints = [
        (RPC, "RPC Node"),
        (EXPLORER, "Block Explorer"),
        (FAUCET, "Faucet"),
    ]
    for url, label in endpoints:
        status = check_url(url, label)
        icon = "✅" if "OK" in status else "❌"
        print(f"  {icon} {label}: {status}")

    print(f"\n--- RPC Status ---")
    chain_id = call_rpc("eth_chainId")
    if chain_id and isinstance(chain_id, str):
        cid = int(chain_id, 16)
        match = "✅ MATCH" if cid == CHAIN_ID else f"❌ MISMATCH (expected {CHAIN_ID})"
        print(f"  Chain ID: {cid} {match}")
    else:
        print(f"  Chain ID: FAIL — {chain_id}")

    block_num = call_rpc("eth_blockNumber")
    if block_num and isinstance(block_num, str):
        bn = int(block_num, 16)
        print(f"  Block Height: {bn:,}")
    else:
        print(f"  Block Height: FAIL — {block_num}")

    # Substrate-specific checks (Orbinum uses Substrate + Frontier EVM)
    print(f"\n--- Substrate Node Info ---")
    chain = call_rpc("system_chain") if call_rpc("system_chain") is not None else "N/A (not Substrate RPC)" 
    print(f"  Chain: {chain}")

    node_name = call_rpc("system_name") if call_rpc("system_name") is not None else "N/A"
    if node_name != "N/A":
        print(f"  Node: {node_name}")
        version = call_rpc("system_version") 
        print(f"  Version: {version}")
    else:
        print(f"  Node: Substrate method not available (pure EVM mode)")

    # Client version
    client = call_rpc("eth_clientVersion")
    if client:
        print(f"  Client: {client[:80]}")

    print(f"\n--- Season 1 Airdrop ---")
    print(f"  Pool: 2,000,000 ORB (2% of 1B total supply)")
    print(f"  Snapshot: 14 days before mainnet (~Q4 2026)")
    print(f"  Actions: Shield, Transfer, Unshield, Disclosure")
    print(f"  Faucet: {FAUCET} (10 ORB/day via Discord)")
    print(f"  Config: Chain ID {CHAIN_ID}, RPC {RPC}")

    print(f"\n{'='*60}")
    print(f"  Validator check complete.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
