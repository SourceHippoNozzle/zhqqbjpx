#!/usr/bin/env python3
"""
Orbinum Testnet Setup & Interaction Script
Chain ID: 2700 | RPC: https://rpc-1.testnet.orbinum.io

This script helps set up and interact with Orbinum testnet.
Note: Faucet requires Cloudflare Turnstile bypass (browser needed).

Usage:
  python3 orbinum-setup.py          # Check chain status
  python3 orbinum-setup.py balance  # Check wallet balance
  python3 orbinum-setup.py faucet   # Instructions for faucet
"""

import sys, json, os
from web3 import Web3

RPC = "https://rpc-1.testnet.orbinum.io"
EXPLORER = "https://explorer.testnet.orbinum.io"
FAUCET_URL = "https://faucet.orbinum.network"
CHAIN_ID = 2700

w3 = Web3(Web3.HTTPProvider(RPC))

def check_connection():
    if w3.is_connected():
        cid = w3.eth.chain_id
        print(f"✅ Connected to Orbinum Network")
        print(f"   Chain ID: {cid} (0x{cid:x})")
        print(f"   Block: {w3.eth.block_number}")
        print(f"   RPC: {RPC}")
        return True
    else:
        print("❌ Failed to connect to Orbinum RPC")
        return False

def check_balance(address):
    if not Web3.is_address(address):
        print("❌ Invalid address")
        return
    bal = w3.eth.get_balance(address)
    print(f"   Address: {address}")
    print(f"   Balance: {w3.from_wei(bal, 'ether')} test ORB")

def faucet_instructions():
    print(f"""
╔══════════════════════════════════════════════════════════╗
║             ORBINUM TESTNET FAUCET                      ║
╚══════════════════════════════════════════════════════════╝

URL: {FAUCET_URL}

⚠️  Cloudflare Turnstile protection detected.
   Manual browser interaction required.

Steps:
1. Open {FAUCET_URL} in a real browser (no proxy)
2. Solve the Turnstile CAPTCHA
3. Enter your wallet address: <YOUR_ADDRESS>
4. Click "Request Tokens"
5. Tokens will be sent to your address

After receiving tokens:
- Check balance: python3 {__file__} balance <your_address>
- Use explorer: {EXPLORER}
- Try shielded transfers on the testnet
""")

def main():
    if len(sys.argv) < 2:
        if check_connection():
            print(f"\nExplorer: {EXPLORER}")
            print(f"Faucet: {FAUCET_URL}")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "balance":
        if not check_connection():
            return
        addr = sys.argv[2] if len(sys.argv) > 2 else input("Enter address: ")
        check_balance(addr)
    
    elif cmd == "faucet":
        faucet_instructions()
    
    elif cmd == "chain":
        check_connection()
        if w3.is_connected():
            print(f"Latest Block: {w3.eth.block_number}")
            print(f"Gas Price: {w3.eth.gas_price}")
    
    else:
        print(f"Unknown command: {cmd}")
        print("Usage: python3 orbinum-setup.py [balance|faucet|chain]")

if __name__ == "__main__":
    main()
