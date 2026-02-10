#!/bin/bash
# Initialize the MCP Factory home directory and install dependencies.
set -e

FACTORY_HOME="${MCP_FACTORY_HOME:-$HOME/.mcp-factory}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== MCP Factory Init ==="
echo "Home: $FACTORY_HOME"

# Create directories
mkdir -p "$FACTORY_HOME/servers"

# Initialize empty registry
if [ ! -f "$FACTORY_HOME/registry.json" ]; then
    echo '{"servers": {}}' > "$FACTORY_HOME/registry.json"
    echo "✓ Created registry at $FACTORY_HOME/registry.json"
else
    echo "✓ Registry already exists"
fi

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install -r "$SCRIPT_DIR/mcp_factory/requirements.txt"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Add this to your agent's MCP config:"
echo ""
echo "  {\"mcpServers\": {\"mcp-factory\": {\"command\": \"python\", \"args\": [\"$SCRIPT_DIR/mcp_factory/server.py\"]}}}"
echo ""
echo "Then restart your agent to connect."
