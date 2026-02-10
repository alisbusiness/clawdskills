# Factory API Reference

Complete reference for all tools exposed by the `mcp-factory` server.

---

## Registry Management

### `registry_add`

Register an external MCP server so the factory can connect to it.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | ✓ | Short name (e.g., `stripe`, `notion`) |
| `transport` | string | ✓ | `stdio` or `sse` |
| `command` | string | stdio only | Command to run (e.g., `python`, `npx`) |
| `args` | string (JSON array) | — | Command arguments (e.g., `'["server.py"]'`) |
| `url` | string | sse only | Server URL (e.g., `http://localhost:3001/sse`) |
| `env` | string (JSON object) | — | Environment variables (e.g., `'{"API_KEY":"sk-..."}'`) |
| `description` | string | — | What this server does |

**Example — stdio server:**
```
registry_add(
  alias="weather",
  transport="stdio",
  command="python",
  args='["/path/to/weather_server.py"]',
  description="Weather data API"
)
```

**Example — SSE server:**
```
registry_add(
  alias="notion",
  transport="sse",
  url="http://localhost:3001/sse",
  env='{"NOTION_TOKEN": "secret_..."}',
  description="Notion workspace integration"
)
```

### `registry_list`

List all registered servers with transport type, managed/external status, and description.

No parameters.

### `registry_remove`

Remove a server from the registry. Does **not** delete managed server files from disk.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | ✓ | Server to remove |

---

## Remote Interaction

### `remote_discover`

Connect to a registered server, perform MCP handshake, and return its available tools with parameter schemas.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | ✓ | Server to discover |

**Returns:** Tool names, descriptions, and input parameters.

### `remote_call`

Call a specific tool on a registered server and return the result.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | ✓ | Server to call |
| `tool_name` | string | ✓ | Tool to invoke |
| `arguments` | string (JSON) | — | Tool parameters (default: `{}`) |

**Example:**
```
remote_call(
  alias="weather",
  tool_name="get_forecast",
  arguments='{"city": "London", "days": 3}'
)
```

---

## Server Scaffolding & Build

### `scaffold_server`

Create a new MCP server from a built-in template (Python or Node.js). Automatically registers it.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | ✓ | Server name / alias |
| `language` | string | — | `python` (default) or `node` |
| `tools` | string | — | Comma-separated tool names to pre-create |
| `description` | string | — | What this server does |

**Example:**
```
scaffold_server(
  name="stock-data",
  language="python",
  tools="get_price,get_history,search_ticker",
  description="Stock market data API"
)
```

**Creates at:** `~/.mcp-factory/servers/stock-data/`

### `scaffold_from_repo`

Clone a GitHub repository as a managed MCP server. Auto-detects language and entry point.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | ✓ | Alias for the server |
| `repo_url` | string | ✓ | GitHub URL to clone |
| `description` | string | — | What this server does |

**Example:**
```
scaffold_from_repo(
  name="github-mcp",
  repo_url="https://github.com/modelcontextprotocol/servers",
  description="GitHub API integration"
)
```

### `build_server`

Install dependencies for a managed server, either locally or via Docker.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | ✓ | Server to build |
| `use_docker` | bool | — | `true` to build Docker image (default: `false`) |

When `use_docker=true`:
- Builds image tagged `mcp-{name}`
- Updates registry to use `docker run -i` as the command
- Server runs in container isolation

### `edit_server`

Replace the main server file with new code. Use this to add/modify/remove tools.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | ✓ | Server to edit |
| `code` | string | ✓ | Complete replacement code |

### `server_status`

Show registry info for a server (path, language, transport, description). Secrets are redacted.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | ✓ | Server to check |

---

## Data Locations

| Path | Contents |
|------|----------|
| `~/.mcp-factory/registry.json` | Server registry (persisted) |
| `~/.mcp-factory/servers/` | Managed server directories |
| `~/.mcp-factory/audit.log` | Call audit trail |

## Protocol Support

| Transport | Discovery | Calling | Notes |
|-----------|-----------|---------|-------|
| stdio | ✓ | ✓ | Spawns process, performs JSON-RPC handshake |
| sse | ✓ | ✓ | HTTP POST to server URL (requires httpx) |
