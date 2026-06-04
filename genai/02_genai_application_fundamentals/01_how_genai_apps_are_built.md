# How GenAI Applications Are Built

## Goal

Before learning prompts, APIs, or RAG, first understand the shape of a GenAI
application.

A GenAI application is not only a model call. It is usually a full software
system that combines:

- user input
- instructions
- model selection
- context retrieval
- tool execution
- output formatting
- memory or session tracking
- safety checks
- logging and monitoring

## Core Building Blocks

Most GenAI applications follow this flow:

1. accept input from a user or another system
2. build a prompt or message list
3. attach useful context
4. call a model API
5. optionally let the model use tools
6. post-process the result
7. store the interaction in session history
8. return the final response

## Common Interaction Modes

### Text to text

This is the simplest mode.

Example:

- input: "summarize this email"
- output: a text summary

### Speech to text

The user speaks, and an ASR model converts audio into text.

Common use cases:

- voice assistants
- meeting transcription
- call-center assistants

### Text to speech

The system generates spoken audio from text.

Common use cases:

- voice bots
- accessibility tools
- customer support systems

### Speech to speech

The system accepts speech input and produces speech output. In practice, this is
often built as:

1. speech to text
2. LLM reasoning on text
3. text to speech

Some real-time systems optimize this pipeline to reduce latency and create a
more natural conversation.

### Multimodal interaction

Some systems accept or produce more than text. They may work with:

- text
- audio
- images
- video
- documents

## Main Application Components

### The model

The model generates, classifies, extracts, or reasons over input.

### The prompt layer

This tells the model what job it should do, how it should behave, and what
constraints it must follow.

### The context layer

This includes any useful information added at runtime, such as:

- retrieved documents
- user profile data
- session summaries
- tool outputs
- web search results

### The tool layer

The tool layer lets the model interact with systems outside the model itself,
such as:

- databases
- search engines
- CRMs
- calendars
- internal APIs

### The output layer

This layer decides whether the response should be:

- free text
- JSON
- a table
- a UI action
- a workflow step

## Context, Contacts, and Connectors

In real products, a GenAI app rarely works alone. It touches other systems.

Useful integration points include:

- documents
- websites
- databases
- business APIs
- messaging systems
- user accounts and session stores

If "contacts" was intended as "connection points," these are the external
systems the application talks to. If it was intended as "context," that topic
appears throughout this module and especially in the lessons on prompt assembly,
memory, and RAG.

## What Are Scales, Scaling, and Scope

The word "scales" is often used loosely in GenAI discussions, so it helps to
separate three ideas:

- scale: the size or complexity of the system, for example moving from a single
  prompt app to a multi-step, multi-tool system
- scaling: the process of making the system handle more users, more data, more
  tools, or more workflows reliably
- scope: the boundary of what the system is allowed to access or do

Examples:

- a higher-scale system may support many teams and many workflows
- a tightly scoped system may be allowed to read documents but not write them
- an OAuth scope may allow `docs:read` but not `docs:write`

All three ideas matter in production GenAI systems.

## Simple Mental Model

Think of a GenAI application as:

"software that prepares context and instructions for a model, optionally lets it
use tools, and then turns the result into a useful product behavior"

That mental model will help with every later lesson in this section.
