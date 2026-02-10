---
name: mcp-forge
description: >
  Create, register, and call MCP servers on-demand via an always-on factory
  server. Use when: (1) the user asks to "add a tool", "create an MCP",
  "connect to an MCP server", or "install a new integration", (2) building
  a custom MCP server for a specific API or workflow, (3) connecting to an
  external MCP endpoint, (4) scaffolding a new MCP server from a template,
  or (5) the user wants to extend the agent's capabilities with new tools
  at runtime.
---

# MCP Forge

Build and connect MCP servers on-demand through a single always-on `mcp-factory` server. The agent never needs config restarts — it calls factory tools to create, register, discover, and invoke new servers immediately.

## Architecture

```
┌─────────────┐         ┌───────────────────┐
│   Agent      │ ──────► │   mcp-factory     │  (always-on, only MCP server needed)
│ (Antigravity │         │                   │
│  / Claude)   │         │  ┌─────────────┐  │
└─────────────┘         │  │  Registry    │  │──► Managed servers (scaffolded + built)
                         │  │  (JSON)      │  │──► External servers (registered endpoints)
                         │  └─────────────┘  │
                         └───────────────────┘
```

**Key insight:** The agent sees a stable, small toolset (the factory tools). The factory proxies calls to any number of child servers. No hot-reloading needed.

## Setup

### First-Time Bootstrap

Run the init script to set up the factory:

```bash
# From the mcp-forge skill directory
bash scripts/init_factory.sh
```

This creates `~/.mcp-factory/` with the registry and server storage.

Then add `mcp-factory` to your agent's MCP config:

```json
{
  "mcpServers": {
    "mcp-factory": {
      "command": "python",
      "args": ["<path-to-skill>/scripts/mcp_factory/server.py"],
      "env": {}
    }
  }
}
```

### Dependencies

The factory server requires:
- Python 3.10+
- `fastmcp` (pip install fastmcp)
- Docker (for sandboxed builds — recommended)

## Rules

- **Prefer factory tools** over editing agent config directly.
- **Never expose secrets in chat.** Pass secrets via env vars in `registry_add`.
- **User approval required** for any action that installs or runs code. Always ask yes/no.
- **Docker-first** for managed servers. Only run on host if the user explicitly opts in.
- **One alias per server.** Use short, memorable names (`stripe`, `notion`, `github-ci`).

## Core Workflow

### A) Connect to an External MCP Server

```
1. registry_add(alias, transport, endpoint)
2. remote_discover(alias)        → see what tools are available
3. remote_call(alias, tool, args) → call any tool
```

### B) Build a New MCP Server

```
1. scaffold_server(name, language, tools)  → creates server from template
2. edit_server(name, code)                 → customize if needed
3. build_server(name)                      → install deps / Docker build
4. remote_discover(name)                   → verify tools
5. remote_call(name, tool, args)           → use it
```

### C) From a GitHub Template

```
1. scaffold_from_repo(name, repo_url)  → clone + register
2. build_server(name)                  → build it
3. remote_discover(name)               → see tools
4. remote_call(name, tool, args)       → use it
```

## Factory Tools Reference

Quick reference. For full API details → read `references/factory-api.md`.

| Tool | Purpose |
|------|---------|
| `registry_add` | Register an external MCP server |
| `registry_list` | List all registered servers |
| `registry_remove` | Remove a server from registry |
| `remote_discover` | List tools on a registered server |
| `remote_call` | Call a tool on a registered server |
| `scaffold_server` | Create a new MCP server from template |
| `scaffold_from_repo` | Clone a GitHub repo as a new server |
| `build_server` | Build/install deps for a managed server |
| `edit_server` | Modify the code of a managed server |
| `server_status` | Check if a managed server is running |

## Server Templates

The factory includes Python and Node.js templates. For template details and patterns for common server types (API wrapper, database, file processor, web scraper) → read `references/server-patterns.md`.

## Security

- **Docker sandboxing:** All managed servers run in containers by default. Container networking is restricted — only the ports the server needs.
- **Secret management:** Secrets are stored as env vars in the registry, never printed to chat. Use `registry_add(..., env={"API_KEY": "..."})`.
- **Permission model:** The factory itself is the only MCP server in the agent config. Child servers cannot access the agent directly.
- **Audit trail:** Every `remote_call` is logged to `~/.mcp-factory/audit.log`.

## File Locations

- `scripts/mcp_factory/server.py` — The factory server (run this)
- `scripts/mcp_factory/requirements.txt` — Python dependencies
- `scripts/init_factory.sh` — Bootstrap script
- `assets/templates/python-server/` — Python MCP server template
- `assets/templates/node-server/` — Node.js MCP server template
- `references/factory-api.md` — Complete tool API reference
- `references/server-patterns.md` — Template patterns for common use cases
