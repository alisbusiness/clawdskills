#!/usr/bin/env python3
"""MCP Server Template — customize this for your use case."""

from fastmcp import FastMCP

mcp = FastMCP("template-server", description="A template MCP server")


@mcp.tool()
def hello(name: str = "world") -> str:
    """Say hello — replace this with your actual tool."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="stdio")
