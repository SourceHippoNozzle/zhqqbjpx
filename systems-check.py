#!/usr/bin/env python3
"""
Systems Check — verify all tracked testnet RPC endpoints and infrastructure.
Run: python3 systems-check.py
"""

import json, os, sys
from datetime import datetime
from web3 import Web3

NETWORKS = [
    {
        "name": "Orbinum Testnet",
        "rpc": "https://rpc-1.testnet.orbinum.io",
        "chain_id": 2700,
        "type": "Substrate+EVM",
    },
    {
        "name": "Sepolia",
        "rpc": "https://ethereum-sepolia.publicnode.com",
        "chain_id": 11155111,
        "type": "Ethereum L2 Testnet",
    },
    {
        "name": "BSC Testnet",
        "rpc": "https://bsc-testnet.publicnode.com",
        "chain_id": 97,
        "type": "EVM",
    },
    {
        "name": "Tempo Moderato",
        "rpc": "https://rpc.moderato.tempo.xyz",
        "chain_id": 42431,
        "type": "TIP-20 L1",
    },
    {
        "name": "Avalanche Fuji",
        "rpc": "https://avalanche-fuji-c-chain.publicnode.com",
        "chain_id": 43113,
        "type": "EVM",
    },
    {
        "name": "Base Sepolia",
        "rpc": "https://base-sepolia.publicnode.com",
        "chain_id": 84532,
        "type": "EVM L2",
    },
]

def check_network(net):
    print(f"  {net['name']:25s} ", end="", flush=True)
    try:
        w3 = Web3(Web3.HTTPProvider(net['rpc'], request_kwargs={'timeout': 10}))
        connected = w3.is_connected()
        if connected:
            cid = w3.eth.chain_id
            block = w3.eth.block_number
            expected = net['chain_id']
            cid_ok = "✓" if cid == expected else f"✗ (got {cid})"
            print(f"✅ UP   chain={cid_ok}   block={block:,}")
        else:
            print(f"❌ NOT RESPONDING")
    except Exception as e:
        print(f"❌ ERROR: {str(e)[:50]}")

def main():
    print(f"\n{'='*60}")
    print(f"  SYSTEMS CHECK — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}\n")
    
    for net in NETWORKS:
        check_network(net)
    
    print(f"\n{'='*60}")

if __name__ == "__main__":
    main()
