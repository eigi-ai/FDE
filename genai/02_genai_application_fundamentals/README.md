# GenAI Application Fundamentals

This folder contains the practical next step after basic GenAI concepts.

The goal of this section is to help a learner understand how real GenAI
applications are designed, wired, controlled, and scaled in products.

This section moves from simple concepts to production-oriented ideas such as
prompt layers, chat APIs, tool calling, structured outputs, tokens and pricing,
RAG, MCP, sessions, context management, and agent frameworks.

## Learning Order

1. `01_how_genai_apps_are_built.md`
   Learn the basic architecture of a GenAI application, common interaction
   modes such as text and speech, and the main components that appear in real
   systems.

2. `02_roles_prompts_and_instructions.md`
   Learn what system prompts, system instructions, developer instructions, and
   message roles are, and how they shape model behavior.

3. `03_chat_completion_temperature_and_context.md`
   Learn how chat completion APIs work, what temperature means, how context
   windows behave, and how sessions are tracked.

4. `04_tools_plugins_and_tool_calling.md`
   Learn what tools and plugins are, how tool calling works, and how tool call
   context should be managed safely inside prompts.

5. `05_structured_output_tokens_and_pricing.md`
   Learn how structured output works, what tokens are, and how input, output,
   and cached token usage affect cost.

6. `06_documents_embeddings_and_rag.md`
   Learn how document processing, chunking, embeddings, vector stores, and
   retrieval pipelines work in RAG systems.

7. `07_agentic_rag_and_search.md`
   Learn when basic RAG is enough, when agentic RAG helps, and how web search,
   rewriting, grading, and answer generation fit together.

8. `08_memory_sessions_and_context_management.md`
   Learn how session IDs, short-term memory, long-term memory, summaries, and
   prompt assembly are used to stay within the context window.

9. `09_mcp_cli_and_oauth.md`
   Learn what MCP is, how MCP tools/resources/prompts work, the main MCP
   transport styles, CLI usage, and how OAuth-based MCP authorization works.

10. `10_agent_frameworks_and_real_time_ai.md`
    Learn how frameworks such as LangGraph, CrewAI, Pipecat, and LiveKit fit
    into agentic and real-time AI systems.

## What This Section Covers

- system prompts and system instructions
- user, assistant, system, and developer roles
- chat completion APIs
- temperature and other response controls
- tools, plugins, and tool-call context
- scale, scaling, and permission scope
- structured output
- tokens and pricing
- context windows and memory
- sessions and conversation IDs
- document processing and web search
- embeddings and RAG
- agentic RAG
- MCP, CLI usage, and OAuth-based authorization
- real-time speech systems and agent frameworks

## Study Notes

- Read these files in order.
- Do not memorize provider-specific names first; learn the underlying pattern.
- Focus on how prompts, context, tools, and outputs are assembled into one
  application flow.
- Revisit the RAG, MCP, and context-management lessons before building agents.
