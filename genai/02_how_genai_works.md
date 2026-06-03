# Part 2: How Generative AI Works

This lesson explains the main idea behind how Generative AI works without going
too deep into math.

## 1. The Big Idea

A generative model learns patterns from data.

Examples of training data:

- books
- articles
- websites
- code
- images
- audio clips

After training, the model can generate output based on the prompt it receives.

## 2. Training vs Inference

### Training

Training is the learning stage.

During training, the model processes huge amounts of data and learns statistical
patterns.

For text models, one simple way to think about it is:

- the model sees text
- it learns what token is likely to come next
- over time it becomes better at generating coherent text

Training is expensive and usually done by large AI companies or research teams.

### Inference

Inference is the usage stage.

This is the stage where:

- you send a prompt
- the model processes the prompt
- the model generates output

When people say they are "using AI," they are usually talking about inference.

## 3. What Is a Prompt?

A prompt is the instruction or input given to the model.

Examples:

- "Explain REST API in simple words"
- "Write a Python function to sort a list"
- "Summarize this email in 3 bullet points"

Better prompts usually lead to better outputs.

## 4. What Is a Token?

A token is a small unit of text the model reads and generates.

Depending on the model, a token may be:

- part of a word
- one word
- punctuation

Why this matters:

- models read prompts as tokens
- models generate output as tokens
- models have token limits, often called context windows

If the input is too large, the model may not be able to use all of it.

## 5. What Is an LLM?

LLM stands for Large Language Model.

An LLM is trained to work with human language and can help with tasks such as:

- answering questions
- summarizing text
- translating
- generating code
- extracting structured information

Examples of text-focused GenAI systems are usually based on LLMs.

## 6. What Are Embeddings?

Embeddings are numeric representations of meaning.

They help systems compare text by similarity.

Simple use case:

1. convert documents into embeddings
2. convert the user question into an embedding
3. find the most similar documents

This is useful for search, recommendations, and RAG systems.

## 7. What Is RAG?

RAG stands for Retrieval-Augmented Generation.

It is a common pattern used in production AI systems.

Basic idea:

1. store documents in a searchable form
2. retrieve the most relevant documents for a user question
3. add that retrieved content to the prompt
4. ask the model to answer using that content

Why RAG is useful:

- gives the model relevant context
- reduces hallucination risk
- helps use private or domain-specific knowledge
- avoids retraining the full model for every knowledge update

## 8. What Is Fine-Tuning?

Fine-tuning means continuing training on a specific type of data so the model
becomes better at a specialized task or domain.

Examples:

- legal drafting style
- medical note formatting
- support-ticket classification and response tone
- company-specific terminology

Fine-tuning is not always required. In many real systems, prompt engineering and
RAG are tried first.

## 9. What Is an Agent?

An agent is more than just one model response.

An AI agent often includes:

- a model for reasoning or generation
- memory or state
- tools such as search, calculator, database access, or APIs
- a step-by-step workflow

Example:

1. user asks for a travel plan
2. agent searches flights
3. agent checks hotel options
4. agent compares costs
5. agent returns a recommended plan

So an agent is usually a system built around the model.

## 10. Why Outputs Change

You may notice that AI outputs are not always identical.

That can happen because of:

- prompt wording
- model settings
- randomness in generation
- missing context
- ambiguity in the task

This is why clear instructions matter.

## 11. Short Summary

- training is how the model learns patterns
- inference is how the trained model is used
- prompts guide the output
- tokens are the text units the model reads and writes
- embeddings help with similarity and retrieval
- RAG adds external knowledge during generation
- fine-tuning adapts a model to a domain
- agents combine models with tools and workflows
