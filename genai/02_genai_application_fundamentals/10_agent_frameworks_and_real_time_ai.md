# Agent Frameworks and Real-Time AI

## Why Frameworks Exist

Once an application needs multiple steps, tools, memory, retries, and routing,
teams often use an agent framework instead of writing everything from scratch.

Frameworks help organize:

- state
- tool orchestration
- routing
- retries
- streaming
- real-time communication
- observability

## LangGraph

LangGraph is useful when you want graph-based control over an agent workflow.

Good for:

- explicit state machines
- conditional routing
- tool loops
- agentic RAG
- traceable workflow logic

## CrewAI

CrewAI focuses on multi-agent collaboration patterns, where different agents or
roles cooperate on a larger task.

Good for:

- role-based task decomposition
- planner and worker patterns
- multi-step business flows

## Pipecat

Pipecat is oriented toward low-latency, real-time, multimodal interaction.

Good for:

- voice agents
- streaming audio pipelines
- real-time conversational systems

## LiveKit

LiveKit is strong for real-time audio/video transport and interactive media
systems.

Good for:

- live voice assistants
- speech-to-speech systems
- meeting assistants
- browser and mobile real-time experiences

## Real-Time AI Patterns

Real-time systems often combine:

1. streaming audio input
2. speech recognition
3. model reasoning
4. tool usage
5. text-to-speech output
6. interruption handling
7. session state management

This is different from a simple chat app because latency matters at every step.

## When to Use What

- use plain API calls for simple single-step workflows
- use RAG pipelines for knowledge retrieval
- use LangGraph when routing and state matter
- use CrewAI when multiple agent roles matter
- use Pipecat or LiveKit when real-time speech and media matter

## Final Mental Model for This Module

A modern GenAI application is built from these layers:

1. modalities such as text or speech
2. prompts and instruction layers
3. chat APIs and response controls
4. tools and structured outputs
5. memory and context management
6. RAG and search
7. integration protocols such as MCP
8. orchestration frameworks for complex workflows

That is the progression from GenAI basics to production-ready GenAI systems.
