#!/usr/bin/env node
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
    name: "template-server",
    description: "A template MCP server",
    version: "1.0.0",
});

server.tool("hello", "Say hello — replace this with your actual tool", {
    name: z.string().default("world").describe("Name to greet"),
}, async ({ name }) => {
    return { content: [{ type: "text", text: `Hello, ${name}!` }] };
});

const transport = new StdioServerTransport();
await server.connect(transport);
