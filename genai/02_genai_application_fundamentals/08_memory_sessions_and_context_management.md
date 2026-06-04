# Memory, Sessions, and Context Management

## Why This Matters

Many weak GenAI applications fail because they keep stuffing more text into the
prompt without managing context deliberately.

Good systems manage memory and context as product features.

## Session Management

A session is a continuous interaction tracked by a unique identifier such as:

- session ID
- thread ID
- conversation ID
- workflow run ID

This ID connects:

- prior user messages
- assistant responses
- tool calls
- summaries
- user preferences

## Types of Memory

### Short-term memory

Recent turns in the active conversation.

### Long-term memory

Information persisted across sessions, such as:

- user preferences
- account facts
- approved business context

### Working memory

Temporary information needed for one task, such as:

- draft tool results
- a current plan
- retrieved evidence

## Context Window Management

Because the context window is limited, applications must decide what to keep.

Common strategies:

- sliding recent history
- conversation summarization
- retrieval of only relevant past facts
- dropping low-value tool output
- storing state outside the prompt

## How Prompt Assembly Works in Practice

A production request often assembles context in this order:

1. system instructions
2. developer instructions
3. task-specific state
4. relevant memory
5. retrieved documents
6. tool outputs
7. current user message

Not all history should be included every time.

## Managing Tool Call Context

Tool call context must be managed carefully because it can grow quickly.

Useful practices:

- keep raw results in storage, not always in the prompt
- insert only the relevant slice into the next call
- summarize verbose tool output
- label tool output clearly
- keep provenance such as tool name and call ID

## What to Store Outside the Prompt

Do not treat the prompt as the database.

Store these externally when possible:

- full transcripts
- raw documents
- analytics
- vector search indexes
- user profile data
- tool execution logs

## Good Mental Model

The model sees only what the application sends in the current request.

Memory is therefore an application responsibility, not a magical property of the
model.
