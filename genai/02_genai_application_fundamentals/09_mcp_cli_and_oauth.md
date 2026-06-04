# MCP, CLI, and OAuth

## What Is MCP

MCP stands for Model Context Protocol.

It is a protocol for connecting AI applications or AI clients to external
capabilities in a consistent way.

MCP standardizes how a client can discover and use external capabilities such as:

- tools
- resources
- prompts

## Why MCP Matters

Without a common protocol, every tool integration becomes custom.

MCP gives a shared way to expose capabilities to AI systems so clients and
servers can interoperate more easily.

## Main MCP Concepts

### Tools

Callable actions the client can invoke through the MCP server.

Examples:

- search docs
- read a database record
- create a ticket

### Resources

Readable data or content exposed by the MCP server.

Examples:

- files
- documentation pages
- records
- templates

### Prompts

Reusable prompt templates or prompt-building assets that can be provided by the
server.

## Types of MCP Usage

### Local or stdio MCP

The client launches the MCP server as a local process and communicates over
standard input and output.

Common use cases:

- local developer tools
- desktop integrations
- CLI workflows

### Remote HTTP-based MCP

The client connects to a server over HTTP-based transport.

This is more common for hosted or shared services.

## MCP and CLI

CLI tools can act as:

- MCP clients that connect to servers
- MCP servers that expose local capabilities
- wrappers that make developer workflows agent-friendly

This matters because many AI developer tools now use MCP to connect editors,
CLIs, local processes, and remote services.

## OAuth MCP Authorization

For HTTP-based transports, MCP can use OAuth-based authorization.

Key idea:

- the MCP server acts like a protected resource server
- the MCP client acts like an OAuth client
- an authorization server issues access tokens

Important notes from the MCP authorization draft:

- authorization is optional, but recommended for protected remote servers
- stdio transports should not use this HTTP authorization flow
- clients discover authorization metadata from the MCP server
- clients should request the minimum required scopes
- clients must keep token handling secure

Reference:

- https://modelcontextprotocol.io/specification/draft/basic/authorization

## Scopes in MCP Authorization

OAuth scopes define permission boundaries.

Examples:

- read docs
- write files
- manage tickets

This is often confused with the word "scales," but the correct OAuth term is
"scopes."

## Very Simple MCP Flow

1. the client connects to an MCP server
2. the client discovers available tools, resources, or prompts
3. the user or model chooses what to use
4. the server returns data or executes an action
5. the client places the result into its application flow

## Practical Rule

Think of MCP as a standardized bridge between models and external systems.

It does not replace good application design, but it makes integration cleaner.
