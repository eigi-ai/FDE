# Part 3: API Calls, Webhooks, SDK, Sync, and Async

This lesson explains how backend systems call other services and how those integrations are commonly structured.

## 1. Backend-To-Backend Communication

This means one backend server sends a request to another backend server.

Common terms for this:

- backend-to-backend communication
- server-to-server communication
- service-to-service communication

Example:

Your FastAPI backend calls:

- payment gateway API
- email API
- AI API
- eigi.ai API

## 2. What Is A Webhook?

A webhook is also a kind of server-to-server communication, but it is event-driven.

In a normal API call:

- your server sends a request to another server
- your server waits for the response

In a webhook:

- your server gives another platform a callback URL
- when an event happens, that platform sends data to your server

Example:

- a payment platform sends a webhook when payment succeeds
- an AI platform sends a webhook when a job is completed
- a delivery platform sends a webhook when shipment status changes

So yes, a webhook is also server-to-server communication, but it is usually event-triggered instead of manually requested each time.

## 3. Polling Vs Webhook

Polling means your server keeps asking:

- Has the job finished?
- Has payment succeeded?

Webhook means the external system tells your server automatically when the event happens.

Polling:

- your backend repeatedly checks status

Webhook:

- external backend notifies your backend automatically

## 4. What Is cURL?

cURL is a command-line tool used to send HTTP requests.

It is very useful for testing APIs quickly from the terminal.

## 5. Example cURL Call

```bash
curl https://api.eigi.ai/v1/public/conversations \
  -H "X-API-Key: vk_your_api_key_here"
```

## 6. Raw API Call From Backend

In Python, a backend can call another API using libraries like:

- `requests`
- `httpx`
- `urllib`

## 7. Sync Vs Async

- sync means one task waits for the previous task to finish
- async means a program can handle waiting more efficiently

## 8. `async` And `await`

- `async def` defines an asynchronous function
- `await` tells Python to wait for an async operation without blocking the whole program

## 9. What Is An SDK?

SDK stands for Software Development Kit.

It is a package or toolkit that makes integration easier.

Without SDK:

- you manually build URLs
- you manually prepare headers
- you manually parse responses

With SDK:

- helper functions are often already provided
- authentication may be easier
- response handling may be cleaner

## 10. Eigi Reference

Real API reference used here:

https://docs.eigi.ai/api-reference/introduction

Important documented details include:

- base URL: `https://api.eigi.ai`
- API key header: `X-API-Key`
- JSON responses
- common error status codes
- rate limiting

## 11. Security Reminder

Never commit API keys to Git.

Keep secrets in environment variables or secret managers.
