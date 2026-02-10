#!/usr/bin/env python3
"""
MCP Factory Server — aggregator/proxy for creating, registering, and calling MCP servers.

This is the ONLY MCP server the agent needs in its config. It proxies calls to
any number of child servers (managed or external) through a persistent registry.

Usage:
    python server.py              # stdio transport (default)
    python server.py --sse 8080   # SSE transport on port 8080
"""

import asyncio
import json
import logging
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastmcp import FastMCP

# === Configuration ===

FACTORY_HOME = Path(os.environ.get("MCP_FACTORY_HOME", Path.home() / ".mcp-factory"))
REGISTRY_FILE = FACTORY_HOME / "registry.json"
SERVERS_DIR = FACTORY_HOME / "servers"
AUDIT_LOG = FACTORY_HOME / "audit.log"
TEMPLATES_DIR = Path(__file__).parent.parent / "assets" / "templates"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("mcp-factory")

# === Initialize ===

mcp = FastMCP(
    "mcp-factory",
    description="Factory server for creating, registering, and calling MCP servers on-demand.",
)


def _ensure_dirs():
    FACTORY_HOME.mkdir(parents=True, exist_ok=True)
    SERVERS_DIR.mkdir(parents=True, exist_ok=True)


def _load_registry() -> dict:
    _ensure_dirs()
    if REGISTRY_FILE.exists():
        return json.loads(REGISTRY_FILE.read_text())
    return {"servers": {}}


def _save_registry(registry: dict):
    _ensure_dirs()
    REGISTRY_FILE.write_text(json.dumps(registry, indent=2))


def _audit(action: str, details: str):
    _ensure_dirs()
    ts = datetime.now(timezone.utc).isoformat()
    with open(AUDIT_LOG, "a") as f:
        f.write(f"{ts} | {action} | {details}\n")


# ============================================================
# Registry Tools
# ============================================================


@mcp.tool()
def registry_add(
    alias: str,
    transport: str,
    command: Optional[str] = None,
    args: Optional[str] = None,
    url: Optional[str] = None,
    env: Optional[str] = None,
    description: str = "",
) -> str:
    """Register an MCP server in the factory registry.

    Args:
        alias: Short name for this server (e.g., 'stripe', 'notion').
        transport: 'stdio' or 'sse'.
        command: For stdio — the command to run (e.g., 'python', 'node', 'npx').
        args: For stdio — JSON array of command arguments (e.g., '["server.py"]').
        url: For sse — the server URL (e.g., 'http://localhost:3001/sse').
        env: JSON object of environment variables (e.g., '{"API_KEY": "..."}').
        description: Human-readable description of what this server does.
    """
    if transport not in ("stdio", "sse"):
        return "Error: transport must be 'stdio' or 'sse'."
    if transport == "stdio" and not command:
        return "Error: stdio transport requires 'command'."
    if transport == "sse" and not url:
        return "Error: sse transport requires 'url'."

    registry = _load_registry()

    entry = {
        "transport": transport,
        "description": description,
        "managed": False,
        "created": datetime.now(timezone.utc).isoformat(),
    }
    if command:
        entry["command"] = command
    if args:
        entry["args"] = json.loads(args) if isinstance(args, str) else args
    if url:
        entry["url"] = url
    if env:
        entry["env"] = json.loads(env) if isinstance(env, str) else env

    registry["servers"][alias] = entry
    _save_registry(registry)
    _audit("registry_add", f"alias={alias} transport={transport}")
    return f"✓ Registered '{alias}' ({transport}). Use remote_discover('{alias}') to see its tools."


@mcp.tool()
def registry_list() -> str:
    """List all registered MCP servers with their status and transport type."""
    registry = _load_registry()
    if not registry["servers"]:
        return "No servers registered. Use registry_add() or scaffold_server() to add one."

    lines = []
    for alias, info in registry["servers"].items():
        kind = "managed" if info.get("managed") else "external"
        transport = info["transport"]
        desc = info.get("description", "")
        lines.append(f"  {alias} | {transport} | {kind} | {desc}")

    return "Registered servers:\n" + "\n".join(lines)


@mcp.tool()
def registry_remove(alias: str) -> str:
    """Remove an MCP server from the registry. Does NOT delete managed server files."""
    registry = _load_registry()
    if alias not in registry["servers"]:
        return f"Server '{alias}' not found in registry."

    del registry["servers"][alias]
    _save_registry(registry)
    _audit("registry_remove", f"alias={alias}")
    return f"✓ Removed '{alias}' from registry."


# ============================================================
# Remote Interaction Tools
# ============================================================


@mcp.tool()
async def remote_discover(alias: str) -> str:
    """Discover available tools on a registered MCP server.

    Connects to the server, performs MCP handshake, and returns tool names,
    descriptions, and parameter schemas.
    """
    registry = _load_registry()
    if alias not in registry["servers"]:
        return f"Server '{alias}' not found. Run registry_list() to see available servers."

    server = registry["servers"][alias]

    try:
        if server["transport"] == "stdio":
            return await _stdio_request(server, "tools/list", {}, _format_tools)
        elif server["transport"] == "sse":
            return await _sse_request(server, "tools/list", {}, _format_tools)
        else:
            return f"Unknown transport: {server['transport']}"
    except asyncio.TimeoutError:
        return f"Timeout connecting to '{alias}'. Is the server running?"
    except Exception as e:
        return f"Error discovering tools on '{alias}': {e}"


@mcp.tool()
async def remote_call(alias: str, tool_name: str, arguments: str = "{}") -> str:
    """Call a tool on a registered MCP server.

    Args:
        alias: The server alias (from registry_list).
        tool_name: Name of the tool to call (from remote_discover).
        arguments: JSON string of the tool's parameters.
    """
    registry = _load_registry()
    if alias not in registry["servers"]:
        return f"Server '{alias}' not found."

    server = registry["servers"][alias]
    args_dict = json.loads(arguments) if isinstance(arguments, str) else arguments

    _audit("remote_call", f"alias={alias} tool={tool_name} args={arguments}")

    try:
        params = {"name": tool_name, "arguments": args_dict}
        if server["transport"] == "stdio":
            return await _stdio_request(server, "tools/call", params, _format_call_result)
        elif server["transport"] == "sse":
            return await _sse_request(server, "tools/call", params, _format_call_result)
        else:
            return f"Unknown transport: {server['transport']}"
    except asyncio.TimeoutError:
        return f"Timeout calling '{tool_name}' on '{alias}'."
    except Exception as e:
        return f"Error calling '{tool_name}' on '{alias}': {e}"


# ============================================================
# Scaffolding & Build Tools
# ============================================================


@mcp.tool()
def scaffold_server(
    name: str,
    language: str = "python",
    tools: str = "hello",
    description: str = "",
) -> str:
    """Scaffold a new MCP server from a built-in template.

    Args:
        name: Server name / alias (e.g., 'weather-api', 'db-query').
        language: 'python' or 'node'.
        tools: Comma-separated tool names to pre-create (e.g., 'search,fetch,summarize').
        description: What this server does.
    """
    if language not in ("python", "node"):
        return "Error: language must be 'python' or 'node'."

    server_dir = SERVERS_DIR / name
    if server_dir.exists():
        return f"Error: server '{name}' already exists at {server_dir}. Remove it first or choose a different name."

    template_dir = TEMPLATES_DIR / f"{language}-server"
    if not template_dir.exists():
        return f"Error: template not found at {template_dir}. Check skill installation."

    # Copy template
    shutil.copytree(template_dir, server_dir)

    # Customize
    tool_list = [t.strip() for t in tools.split(",")]
    if language == "python":
        _customize_python(server_dir, name, description, tool_list)
    else:
        _customize_node(server_dir, name, description, tool_list)

    # Auto-register
    registry = _load_registry()
    entry = {
        "transport": "stdio",
        "description": description or f"Custom server: {name}",
        "managed": True,
        "path": str(server_dir),
        "language": language,
        "created": datetime.now(timezone.utc).isoformat(),
    }
    if language == "python":
        entry["command"] = sys.executable
        entry["args"] = [str(server_dir / "server.py")]
    else:
        entry["command"] = "node"
        entry["args"] = [str(server_dir / "index.js")]

    registry["servers"][name] = entry
    _save_registry(registry)
    _audit("scaffold_server", f"name={name} lang={language} tools={tools}")

    return (
        f"✓ Scaffolded '{name}' ({language}) at {server_dir}\n"
        f"  Tools: {', '.join(tool_list)}\n"
        f"  Auto-registered. Run build_server('{name}') to install deps,\n"
        f"  then remote_discover('{name}') to verify."
    )


@mcp.tool()
def scaffold_from_repo(name: str, repo_url: str, description: str = "") -> str:
    """Clone a GitHub repository as a new managed MCP server.

    Args:
        name: Alias for the server.
        repo_url: GitHub URL (e.g., 'https://github.com/user/mcp-server-example').
        description: What this server does.
    """
    server_dir = SERVERS_DIR / name
    if server_dir.exists():
        return f"Error: '{name}' already exists at {server_dir}."

    result = subprocess.run(
        ["git", "clone", "--depth=1", repo_url, str(server_dir)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return f"Git clone failed:\n{result.stderr}"

    # Detect language
    language = "python" if (server_dir / "requirements.txt").exists() else "node"

    # Find entry point
    if language == "python":
        candidates = ["server.py", "main.py", "src/server.py", "app.py"]
        entry_point = next((c for c in candidates if (server_dir / c).exists()), "server.py")
        cmd, args = sys.executable, [str(server_dir / entry_point)]
    else:
        candidates = ["index.js", "dist/index.js", "src/index.js", "build/index.js"]
        entry_point = next((c for c in candidates if (server_dir / c).exists()), "index.js")
        cmd, args = "node", [str(server_dir / entry_point)]

    registry = _load_registry()
    registry["servers"][name] = {
        "transport": "stdio",
        "command": cmd,
        "args": args,
        "description": description or f"Cloned from {repo_url}",
        "managed": True,
        "path": str(server_dir),
        "language": language,
        "repo": repo_url,
        "created": datetime.now(timezone.utc).isoformat(),
    }
    _save_registry(registry)
    _audit("scaffold_from_repo", f"name={name} repo={repo_url}")

    return (
        f"✓ Cloned '{name}' from {repo_url}\n"
        f"  Detected: {language} (entry: {entry_point})\n"
        f"  Run build_server('{name}') to install dependencies."
    )


@mcp.tool()
def build_server(name: str, use_docker: bool = False) -> str:
    """Build a managed MCP server (install dependencies).

    Args:
        name: Server alias.
        use_docker: If True, build a Docker image instead of installing locally.
    """
    registry = _load_registry()
    if name not in registry["servers"]:
        return f"Server '{name}' not found."

    server = registry["servers"][name]
    if not server.get("managed"):
        return f"'{name}' is external — nothing to build."

    server_path = Path(server["path"])
    if not server_path.exists():
        return f"Server directory not found at {server_path}."

    if use_docker:
        dockerfile = server_path / "Dockerfile"
        if not dockerfile.exists():
            return f"No Dockerfile in {server_path}. Build without Docker or add a Dockerfile."

        result = subprocess.run(
            ["docker", "build", "-t", f"mcp-{name}", "."],
            cwd=server_path,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            return f"Docker build failed:\n{result.stderr[-500:]}"

        # Update registry to use docker
        server["command"] = "docker"
        server["args"] = ["run", "-i", "--rm", f"mcp-{name}"]
        _save_registry(registry)
        _audit("build_server", f"name={name} docker=true")
        return f"✓ Built Docker image 'mcp-{name}'. Registry updated to use container."
    else:
        lang = server.get("language", "python")
        if lang == "python" and (server_path / "requirements.txt").exists():
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                cwd=server_path,
                capture_output=True,
                text=True,
                timeout=120,
            )
        elif lang == "node" and (server_path / "package.json").exists():
            result = subprocess.run(
                ["npm", "install"],
                cwd=server_path,
                capture_output=True,
                text=True,
                timeout=120,
            )
        else:
            return f"No requirements.txt or package.json found in {server_path}."

        if result.returncode != 0:
            return f"Build failed:\n{result.stderr[-500:]}"

        _audit("build_server", f"name={name} docker=false")
        return f"✓ Dependencies installed for '{name}'. Ready to use."


@mcp.tool()
def edit_server(name: str, code: str) -> str:
    """Replace the main server file for a managed MCP server with new code.

    Args:
        name: Server alias.
        code: Complete replacement code for the main server file.
    """
    registry = _load_registry()
    if name not in registry["servers"]:
        return f"Server '{name}' not found."

    server = registry["servers"][name]
    if not server.get("managed"):
        return f"'{name}' is external — cannot edit."

    server_path = Path(server["path"])
    lang = server.get("language", "python")

    if lang == "python":
        main_file = server_path / "server.py"
    else:
        main_file = server_path / "index.js"

    if not main_file.parent.exists():
        return f"Server directory not found at {server_path}."

    main_file.write_text(code)
    _audit("edit_server", f"name={name} file={main_file.name}")
    return f"✓ Updated {main_file}. Use remote_discover('{name}') to verify tools."


@mcp.tool()
def server_status(name: str) -> str:
    """Check the status of a managed server (path, language, registry info)."""
    registry = _load_registry()
    if name not in registry["servers"]:
        return f"Server '{name}' not found."

    server = registry["servers"][name]
    lines = [f"Server: {name}"]
    for key, val in server.items():
        if key == "env":
            lines.append(f"  env: [redacted, {len(val)} vars]")
        else:
            lines.append(f"  {key}: {val}")
    return "\n".join(lines)


# ============================================================
# Protocol Helpers (stdio + SSE)
# ============================================================


async def _stdio_request(server: dict, method: str, params: dict, formatter) -> str:
    """Connect to a stdio MCP server, perform handshake, send request, return formatted result."""
    cmd = [server["command"]] + server.get("args", [])
    env = {**os.environ, **server.get("env", {})}

    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=env,
    )

    try:
        # Initialize
        await _send_jsonrpc(proc, 1, "initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "mcp-factory", "version": "1.0.0"},
        })
        resp = await _read_jsonrpc(proc, timeout=10)

        # Initialized notification
        await _send_notification(proc, "notifications/initialized")

        # Actual request
        await _send_jsonrpc(proc, 2, method, params)
        resp = await _read_jsonrpc(proc, timeout=30)

        if "error" in resp:
            return f"Server error: {resp['error']}"

        return formatter(resp.get("result", {}))
    finally:
        proc.terminate()
        try:
            await asyncio.wait_for(proc.wait(), timeout=5)
        except asyncio.TimeoutError:
            proc.kill()


async def _sse_request(server: dict, method: str, params: dict, formatter) -> str:
    """Send a request to an SSE/HTTP MCP server."""
    try:
        import httpx
    except ImportError:
        return "Error: httpx not installed. Run: pip install httpx"

    url = server["url"].rstrip("/")
    headers = {}
    if server.get("env", {}).get("AUTH_TOKEN"):
        headers["Authorization"] = f"Bearer {server['env']['AUTH_TOKEN']}"

    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(url, json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        }, headers=headers)
        data = resp.json()

        if "error" in data:
            return f"Server error: {data['error']}"
        return formatter(data.get("result", {}))


async def _send_jsonrpc(proc, req_id: int, method: str, params: dict):
    msg = json.dumps({"jsonrpc": "2.0", "id": req_id, "method": method, "params": params}) + "\n"
    proc.stdin.write(msg.encode())
    await proc.stdin.drain()


async def _send_notification(proc, method: str):
    msg = json.dumps({"jsonrpc": "2.0", "method": method}) + "\n"
    proc.stdin.write(msg.encode())
    await proc.stdin.drain()


async def _read_jsonrpc(proc, timeout: int = 10) -> dict:
    line = await asyncio.wait_for(proc.stdout.readline(), timeout=timeout)
    return json.loads(line)


def _format_tools(result: dict) -> str:
    tools = result.get("tools", [])
    if not tools:
        return "No tools found on this server."

    lines = []
    for tool in tools:
        name = tool["name"]
        desc = tool.get("description", "")
        props = tool.get("inputSchema", {}).get("properties", {})
        params = []
        for pname, pschema in props.items():
            ptype = pschema.get("type", "any")
            pdesc = pschema.get("description", "")
            params.append(f"    {pname}: {ptype}" + (f" — {pdesc}" if pdesc else ""))
        lines.append(f"  {name}: {desc}")
        if params:
            lines.extend(params)
    return "Available tools:\n" + "\n".join(lines)


def _format_call_result(result: dict) -> str:
    content = result.get("content", [])
    parts = []
    for item in content:
        if item.get("type") == "text":
            parts.append(item["text"])
        else:
            parts.append(json.dumps(item))
    return "\n".join(parts) if parts else "(empty response)"


# ============================================================
# Template Customization
# ============================================================


def _customize_python(server_dir: Path, name: str, description: str, tools: list):
    tool_defs = []
    for tname in tools:
        tool_defs.append(
            f'\n@mcp.tool()\ndef {tname}(input: str) -> str:\n'
            f'    """{tname} — customize this implementation."""\n'
            f'    # TODO: implement\n'
            f'    return f"{tname} received: {{input}}"\n'
        )

    code = (
        f'#!/usr/bin/env python3\n'
        f'"""{name} — {description or "Custom MCP server"}"""\n\n'
        f'from fastmcp import FastMCP\n\n'
        f'mcp = FastMCP("{name}", description="{description or name}")\n'
        + "".join(tool_defs)
        + f'\nif __name__ == "__main__":\n'
        f'    mcp.run(transport="stdio")\n'
    )
    (server_dir / "server.py").write_text(code)


def _customize_node(server_dir: Path, name: str, description: str, tools: list):
    tool_handlers = []
    for tname in tools:
        tool_handlers.append(
            f'\nserver.tool("{tname}", "{tname} — customize this", {{\n'
            f'  input: z.string().describe("Input parameter"),\n'
            f'}}, async ({{ input }}) => {{\n'
            f'  // TODO: implement\n'
            f'  return {{ content: [{{ type: "text", text: `{tname}: ${{input}}` }}] }};\n'
            f'}});\n'
        )

    code = (
        f'#!/usr/bin/env node\n'
        f'import {{ McpServer }} from "@modelcontextprotocol/sdk/server/mcp.js";\n'
        f'import {{ StdioServerTransport }} from "@modelcontextprotocol/sdk/server/stdio.js";\n'
        f'import {{ z }} from "zod";\n\n'
        f'const server = new McpServer({{ name: "{name}", description: "{description or name}", version: "1.0.0" }});\n'
        + "".join(tool_handlers)
        + f'\nconst transport = new StdioServerTransport();\n'
        f'await server.connect(transport);\n'
    )
    (server_dir / "index.js").write_text(code)


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    transport = "stdio"
    port = None

    if "--sse" in sys.argv:
        transport = "sse"
        idx = sys.argv.index("--sse")
        if idx + 1 < len(sys.argv):
            port = int(sys.argv[idx + 1])

    if transport == "sse":
        mcp.run(transport="sse", port=port or 8080)
    else:
        mcp.run(transport="stdio")
