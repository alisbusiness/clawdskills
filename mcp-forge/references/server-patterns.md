# MCP Server Patterns

Common patterns for different types of MCP servers. Use these as starting points when scaffolding.

---

## API Wrapper Server

Wrap a REST/GraphQL API so the agent can call it as MCP tools.

```python
from fastmcp import FastMCP
import httpx

mcp = FastMCP("api-wrapper", description="Wraps [Service] REST API")

API_BASE = "https://api.example.com/v1"
API_KEY = os.environ.get("API_KEY", "")


@mcp.tool()
async def search(query: str, limit: int = 10) -> str:
    """Search for items matching the query."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{API_BASE}/search",
            params={"q": query, "limit": limit},
            headers={"Authorization": f"Bearer {API_KEY}"},
        )
        resp.raise_for_status()
        return json.dumps(resp.json(), indent=2)


@mcp.tool()
async def get_item(item_id: str) -> str:
    """Get details for a specific item."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{API_BASE}/items/{item_id}",
            headers={"Authorization": f"Bearer {API_KEY}"},
        )
        resp.raise_for_status()
        return json.dumps(resp.json(), indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

**Register with:**
```
registry_add(
  alias="example-api",
  transport="stdio",
  command="python",
  args='["server.py"]',
  env='{"API_KEY": "your-key-here"}',
  description="Example API wrapper"
)
```

---

## Database Query Server

Let the agent query a database safely (read-only by default).

```python
from fastmcp import FastMCP
import sqlite3
import os

mcp = FastMCP("db-query", description="Query the application database")

DB_PATH = os.environ.get("DB_PATH", "app.db")


@mcp.tool()
def query(sql: str) -> str:
    """Execute a read-only SQL query. Only SELECT statements allowed."""
    if not sql.strip().upper().startswith("SELECT"):
        return "Error: Only SELECT queries are allowed."

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.execute(sql)
        rows = [dict(row) for row in cursor.fetchall()]
        return json.dumps(rows, indent=2, default=str)
    except Exception as e:
        return f"Query error: {e}"
    finally:
        conn.close()


@mcp.tool()
def list_tables() -> str:
    """List all tables and their columns."""
    conn = sqlite3.connect(DB_PATH)
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()

    result = []
    for (table,) in tables:
        cols = conn.execute(f"PRAGMA table_info({table})").fetchall()
        col_info = [f"  {c[1]} ({c[2]})" for c in cols]
        result.append(f"{table}:\n" + "\n".join(col_info))

    conn.close()
    return "\n\n".join(result)


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## File Processor Server

Process files (PDF, CSV, images, etc.) and return structured data.

```python
from fastmcp import FastMCP
from pathlib import Path
import csv
import json

mcp = FastMCP("file-processor", description="Process and extract data from files")


@mcp.tool()
def read_csv(file_path: str, max_rows: int = 100) -> str:
    """Read a CSV file and return rows as JSON."""
    path = Path(file_path)
    if not path.exists():
        return f"File not found: {file_path}"
    if not path.suffix == ".csv":
        return "Only CSV files supported."

    with open(path) as f:
        reader = csv.DictReader(f)
        rows = [row for _, row in zip(range(max_rows), reader)]

    return json.dumps({
        "columns": list(rows[0].keys()) if rows else [],
        "row_count": len(rows),
        "rows": rows,
    }, indent=2)


@mcp.tool()
def file_info(file_path: str) -> str:
    """Get metadata about a file (size, type, modified date)."""
    path = Path(file_path)
    if not path.exists():
        return f"File not found: {file_path}"

    stat = path.stat()
    return json.dumps({
        "name": path.name,
        "extension": path.suffix,
        "size_bytes": stat.st_size,
        "modified": stat.st_mtime,
    }, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Web Scraper Server

Fetch and extract content from web pages.

```python
from fastmcp import FastMCP
import httpx
import re

mcp = FastMCP("web-scraper", description="Fetch and extract web content")


@mcp.tool()
async def fetch_page(url: str) -> str:
    """Fetch a web page and return its text content (HTML stripped)."""
    async with httpx.AsyncClient(follow_redirects=True, timeout=15) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        text = re.sub(r"<[^>]+>", " ", resp.text)
        text = re.sub(r"\s+", " ", text).strip()
        return text[:5000]  # Limit response size


@mcp.tool()
async def fetch_json(url: str) -> str:
    """Fetch a JSON API endpoint."""
    async with httpx.AsyncClient(follow_redirects=True, timeout=15) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return json.dumps(resp.json(), indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Multi-Tool Utility Server

A Swiss-army-knife server with multiple small utilities.

```python
from fastmcp import FastMCP
import hashlib
import json
import base64
from datetime import datetime, timezone

mcp = FastMCP("utils", description="General-purpose utilities")


@mcp.tool()
def hash_text(text: str, algorithm: str = "sha256") -> str:
    """Hash text with the specified algorithm (md5, sha256, sha512)."""
    h = hashlib.new(algorithm)
    h.update(text.encode())
    return h.hexdigest()


@mcp.tool()
def base64_encode(text: str) -> str:
    """Base64 encode text."""
    return base64.b64encode(text.encode()).decode()


@mcp.tool()
def base64_decode(encoded: str) -> str:
    """Base64 decode text."""
    return base64.b64decode(encoded.encode()).decode()


@mcp.tool()
def timestamp() -> str:
    """Get current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).isoformat()


@mcp.tool()
def json_format(text: str) -> str:
    """Pretty-print a JSON string."""
    return json.dumps(json.loads(text), indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Pattern: Adding Authentication

For any pattern above, add auth via environment variables:

```python
import os

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY env var required")
```

Register with secrets:
```
registry_add(
  alias="my-server",
  transport="stdio",
  command="python",
  args='["server.py"]',
  env='{"API_KEY": "sk-..."}'
)
```

Secrets stay in the registry file and process env — **never printed to chat**.
