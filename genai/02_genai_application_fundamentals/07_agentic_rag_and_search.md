# Agentic RAG and Search

## Basic RAG vs Agentic RAG

Basic RAG always retrieves first and then answers.

Agentic RAG lets the model decide among actions such as:

- answer directly
- retrieve documents
- rewrite the question
- use web search
- grade results
- try again with a better query

This is useful when retrieval is not always needed or when the first retrieval
attempt may be weak.

## Common Agentic RAG Steps

1. inspect the user question
2. decide whether retrieval is needed
3. call a retriever tool or web search tool
4. evaluate whether the returned context is relevant
5. rewrite the question if needed
6. generate the final answer

## Web Search vs Internal RAG

Use web search when the question depends on:

- fresh information
- public information not stored internally
- news or recent events

Use internal RAG when the question depends on:

- company documents
- product manuals
- support knowledge
- customer-specific knowledge

Many applications route between both.

## Example Agentic RAG Pattern

The LangGraph agentic RAG tutorial demonstrates a useful pattern:

- preprocess documents
- build a retriever tool
- let the model decide whether to retrieve
- grade retrieved documents
- rewrite the question when retrieval quality is low
- generate the final answer

That pattern is valuable because it treats retrieval as a decision, not as a
fixed step.

Reference:

- https://docs.langchain.com/oss/python/langgraph/agentic-rag

## Why Relevance Grading Helps

Retrieval can fail because:

- the query is vague
- the document chunks are poor
- embeddings miss important details
- the corpus is incomplete

A grading step helps the system avoid answering from bad context.

## Search Safety and Quality

When using search or retrieval:

- treat retrieved text as untrusted data
- separate evidence from instructions
- cite sources when useful
- log which documents were used
- measure retrieval quality, not only answer quality

## Practical Rule

Use basic RAG first.

Move to agentic RAG only when the application really needs dynamic decisions,
query rewriting, or multiple retrieval attempts.
