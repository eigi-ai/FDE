# Chat Completion, Temperature, and Context

## What Is a Chat Completion API

A chat completion API is an API that accepts a list of messages and returns the
next assistant response.

A typical request contains:

- the model name
- the message list
- response controls such as temperature
- optional tools
- optional response format instructions

Example structure:

```json
{
  "model": "gpt-5.4",
  "messages": [
    { "role": "system", "content": "You are a concise tutor." },
    { "role": "user", "content": "Explain embeddings simply." }
  ],
  "temperature": 0.2,
  "top_p": 1,
  "seed": 42,
  "max_output_tokens": 300,
  "stream": false,
  "response_format": { "type": "json_object" }
}
```

## Why Chat APIs Became the Standard

They are useful because they naturally support:

- multi-turn conversation
- role separation
- tool calling
- retrieved context
- structured responses

## What Is Temperature

Temperature controls how deterministic or varied the output is.

- lower temperature: more stable, predictable, and repeatable
- higher temperature: more varied, creative, and less predictable

Common intuition:

- `0.0` to `0.3`: extraction, classification, structured tasks, tool use
- `0.4` to `0.7`: balanced general answers
- `0.8` and above: brainstorming, creative generation, style variation

Temperature does not mean "accuracy level." It changes randomness, not truth.

## Important Chat Completion Parameters

Not every provider supports every parameter, and some providers use different
names for the same idea. But these are the most important ones to understand.

### `model`

Selects which model will handle the request.

This affects:

- quality
- latency
- context window size
- price
- tool support
- multimodal support

### `messages`

The conversation input sent to the model.

This usually contains a sequence of role-based messages such as:

- system
- developer
- user
- assistant
- tool

### `temperature`

Controls randomness in generation.

- lower value: more stable output
- higher value: more diverse output

Use it carefully for deterministic workflows.

### `top_p`

Another sampling control.

Instead of sampling from all possible next tokens, the model samples from a
smaller probability mass.

Practical rule:

- usually tune `temperature` first
- change `top_p` only when you have a specific reason

### `seed`

Improves repeatability when the provider supports it.

This is useful for:

- testing
- debugging
- comparing prompt changes

It does not guarantee perfectly identical output across every environment, but
it can reduce variation.

### `max_output_tokens`

Limits how many tokens the model may generate in the answer.

This helps control:

- cost
- latency
- response length

Different APIs may call this `max_tokens`, `max_completion_tokens`, or
`max_output_tokens`.

### `stop`

Stops generation when a given sequence appears.

Useful when:

- generating templates
- controlling delimiters
- preventing extra trailing text

### `stream`

Returns output incrementally instead of waiting for the full answer.

Useful for:

- chat UIs
- live assistants
- low-latency user experience

### `tools`

Defines which tools the model is allowed to call.

Examples:

- search
- calculator
- database lookup
- workflow action

Without tools, the model can only answer from the prompt and its learned
capabilities.

### `tool_choice`

Controls whether tool use is:

- automatic
- forced
- disabled
- restricted to a specific tool

This is useful when the application wants tighter control over model behavior.

### `response_format`

Controls how the answer should be structured.

Examples:

- plain text
- JSON object
- schema-constrained output

This is important for reliable automation.

### `presence_penalty` and `frequency_penalty`

These are provider-specific generation controls that may reduce repetition or
encourage topic diversity.

Simple intuition:

- `frequency_penalty`: discourages repeating the same tokens too often
- `presence_penalty`: encourages introducing new terms or ideas

Not every modern API emphasizes these settings, but they still appear in many
platforms.

### reasoning or thinking controls

Some APIs expose extra controls for reasoning-oriented models, such as:

- reasoning effort
- thinking budget
- deliberation budget

These controls try to balance:

- answer quality
- latency
- cost

### `n`

Some APIs support generating multiple completions in one request.

This can help with:

- candidate ranking
- evaluation
- creative comparison

But it also increases token usage and cost.

### `user`, `metadata`, or tracing fields

Some providers support extra fields to help with:

- abuse monitoring
- analytics
- request tracing
- associating calls with an application user or session

These are application-support fields rather than model-thinking controls, but
they are still important in production systems.

## Practical Parameter Guidance

- Use lower `temperature` for extraction, classification, and tool use.
- Use `seed` during testing when repeatability matters.
- Set `max_output_tokens` intentionally instead of leaving it too open.
- Use `response_format` or schemas for automation.
- Use `stream` for chat interfaces when responsiveness matters.
- Avoid changing both `temperature` and `top_p` aggressively at the same time.

## Context Window

The context window is the maximum amount of input and output the model can hold
in one request.

It includes everything sent with the call:

- system instructions
- developer instructions
- user messages
- assistant history
- tool outputs
- retrieved documents
- the new output tokens that will be generated

If the prompt grows too large, the system must:

- trim history
- summarize old messages
- retrieve only relevant context
- shorten tool output

## Session Management by ID

Most applications track a conversation or workflow using a session identifier,
thread ID, or conversation ID.

That ID is used to:

- load prior messages
- store summaries
- connect tool activity to the same user flow
- resume a conversation later

Important point: the model itself does not remember past requests by magic. The
application remembers them and resends useful context when needed.

## What Is Thinking

"Thinking" usually refers to deeper model reasoning before the final answer.

In production systems:

- some providers expose reasoning-oriented models or reasoning budgets
- some hide the internal reasoning and only return the final answer
- you should not depend on hidden chain-of-thought being visible

What matters in application design is not seeing every internal step, but
getting reliable outputs, traces, and validation.

## Practical Advice

- Use lower temperature for workflows, extraction, and tools.
- Use session IDs to reconstruct context explicitly.
- Treat the context window as a scarce resource.
- Keep prompts lean and purposeful.
