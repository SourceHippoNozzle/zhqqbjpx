#!/usr/bin/env bash
# Push testnet-campaign-recon to GitHub
# Requires: gh CLI authenticated OR GitHub PAT in GH_TOKEN
set -e

REPO_NAME="testnet-campaign-recon"
GH_USER="SourceHippoNozzle"

echo "=== Push $REPO_NAME to GitHub ==="

# Method 1: gh CLI
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
    echo "[gh] Creating repo..."
    cd "$(dirname "$0")/.."
    gh repo create "$GH_USER/$REPO_NAME" --public --push --remote origin --source .
    echo "✅ Done via gh CLI"
    exit 0
fi

# Method 2: GitHub API with PAT
if [ -n "$GH_TOKEN" ]; then
    echo "[API] Creating repo with PAT..."
    RESP=$(curl -s -H "Authorization: token $GH_TOKEN" \
        -d "{\"name\":\"$REPO_NAME\",\"private\":false,\"description\":\"Testnet campaign recon & action tracker\"}" \
        "https://api.github.com/user/repos")
    
    if echo "$RESP" | grep -q '"full_name"'; then
        cd "$(dirname "$0")/.."
        git remote add origin "git@github.com:$GH_USER/$REPO_NAME.git"
        git push -u origin master
        echo "✅ Done via API"
        exit 0
    else
        echo "❌ API failed. Response: $RESP"
        exit 1
    fi
fi

echo ""
echo "⚠️  Cannot push automatically. Do ONE of:"
echo ""
echo "  Option A — Install gh CLI and auth:"
echo "    gh auth login"
echo "    $0"
echo ""
echo "  Option B — Manual web:"
echo "    1. Go to https://github.com/new"
echo "    2. Repo: $REPO_NAME"
echo "    3. Public, no README, no .gitignore, no license"
echo "    4. Then run:"
echo "    cd $(dirname "$0")/.."
echo "    git remote add origin git@github.com:$GH_USER/$REPO_NAME.git"
echo "    git push -u origin master"
echo ""
