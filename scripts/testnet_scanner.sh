#!/bin/bash
# Testnet RPC Scanner — pings known testnet endpoints to verify live status
# Usage: ./testnet_scanner.sh [--timeout N]

TIMEOUT=${2:-8}
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
PASS=0
FAIL=0

check_rpc() {
    local name="$1"
    local url="$2"
    local method="$3"
    local params="$4"
    local expect="$5"
    
    local response=$(curl -s --connect-timeout "$TIMEOUT" -m "$((TIMEOUT + 5))" \
        -X POST -H "Content-Type: application/json" \
        -d "{\"jsonrpc\":\"2.0\",\"method\":\"$method\",\"params\":$params,\"id\":1}" \
        "$url" 2>&1)
    
    if echo "$response" | grep -qE '"result":' 2>/dev/null; then
        echo -e "${GREEN}[LIVE]${NC} $name — $url"
        PASS=$((PASS + 1))
    else
        local err=$(echo "$response" | head -c 120)
        echo -e "${RED}[DOWN]${NC} $name — $url"
        echo "  Response: $err"
        FAIL=$((FAIL + 1))
    fi
}

echo "=========================================="
echo "  Testnet RPC Scanner — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "=========================================="
echo ""

# EVM chains
echo "--- EVM Testnets ---"
check_rpc "Orbinum" "https://testnet.orbinum.xyz/rpc" "eth_chainId" "[]" '"a8c"' # 2700 in hex
check_rpc "Tempo Moderato" "https://rpc.moderato.tempo.xyz" "eth_chainId" "[]" '"a5cf' # 431xx range
check_rpc "Sepolia" "https://ethereum-sepolia.publicnode.com" "eth_chainId" "[]" '"aa36a7"' # 11155111
check_rpc "BSC Testnet" "https://data-seed-prebsc-1-s1.binance.org:8545" "eth_chainId" "[]" '"61"'
check_rpc "Avalanche Fuji" "https://api.avax-test.network/ext/bc/C/rpc" "eth_chainId" "[]" '"a869"'
check_rpc "Base Sepolia" "https://sepolia.base.org" "eth_chainId" "[]" '"14a34"'
check_rpc "Hoodi (ETH)" "https://rpc.hoodi.ethpandaops.io" "eth_chainId" "[]" '"3f0e78"'

echo ""
echo "--- Substrate/Polkadot Chains ---"
check_rpc "Orbinum (system)" "https://testnet.orbinum.xyz/rpc" "system_chain" "[]" "Orbinum"
check_rpc "Orbinum health" "https://testnet.orbinum.xyz/rpc" "system_health" "[]" "isSyncing"

echo ""
echo "====== RESULTS ======"
echo -e "${GREEN}Live: $PASS${NC}"
echo -e "${RED}Down: $FAIL${NC}"
echo "Date: $(date -u)"
echo "========================"
