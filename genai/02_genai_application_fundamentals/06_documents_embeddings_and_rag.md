# Documents, Embeddings, and RAG

## What Is Document Processing

Many GenAI applications work with documents such as:

- PDFs
- Word files
- HTML pages
- support tickets
- knowledge-base articles
- chat transcripts

Document processing is the pipeline that turns raw content into something usable
for retrieval.

## Typical Document Pipeline

1. load the source document
2. clean or normalize the text
3. split the text into chunks
4. create embeddings for each chunk
5. store the embeddings in a vector store
6. retrieve relevant chunks at query time

## What Are Embeddings

Embeddings are numeric vector representations of text.

They let software compare meaning, not only exact keywords.

Text with similar meaning tends to have embeddings that are close in vector
space.

## Why Embeddings Matter

Embeddings power:

- semantic search
- document retrieval
- clustering
- recommendation
- duplicate detection

## RAG Basics

RAG means Retrieval-Augmented Generation.

Instead of asking the model to answer from training alone, the application first
retrieves relevant external information and places it into the prompt.

Basic RAG flow:

1. user asks a question
2. create an embedding for the query
3. search a vector store for similar chunks
4. place the best chunks into the prompt
5. generate the answer

## Core RAG Components

### Loaders

They ingest data from files, web pages, APIs, or databases.

### Splitters

They break large documents into smaller chunks.

### Embedding models

They convert text into vectors.

### Vector stores

They store embeddings for similarity search.

Examples include in-memory stores and production databases that support vector
search.

### Retrievers

They decide which chunks to return for a user query.

## Common RAG Improvements

- metadata filtering
- hybrid search using keyword plus vector search
- reranking
- chunk overlap
- query rewriting
- answer citation

## RAG vs Fine-Tuning

- RAG is good when knowledge changes often
- fine-tuning is good when behavior or style must change deeply

Most business knowledge problems start with RAG, not fine-tuning.

## "All the RAG Embedding Tools"

This usually means understanding the categories used in retrieval systems:

- document loaders
- text splitters
- embedding models
- vector stores
- retrievers
- rerankers
- metadata filters
- citation builders
- evaluation tools

These are the practical building blocks behind a RAG pipeline.
