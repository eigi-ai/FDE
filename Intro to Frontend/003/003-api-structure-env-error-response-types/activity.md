# Activity - Refactor An API Call Into Service Files

## Goal

Practice API structure, env variables, response types, and error handling.

## Task

Add an API feature to your `/api-lab` page.

You can use:

- a real public API
- API Ninjas
- a mock local JSON file if API keys are not available

## Requirements

- create `.env.example`
- read API base URL from `import.meta.env`
- create `services/apiClient.ts`
- create one feature service file, such as `candidateService.ts`
- create response types
- call the service from the page
- show loading state
- show success state
- show empty state if no useful data exists
- show user-facing error state
- log useful details in Console
- inspect the request in Network

## Suggested Files

```text
src/
  services/
    apiClient.ts
    candidateService.ts
  types/
    candidate.ts
  features/
    api-lab/
      ApiLabPage.tsx
```

## Required Console Logs

Add logs like:

```ts
console.log("API request started");
console.log("API response", data);
console.error("API request failed", error);
```

## Required Network Check

In DevTools Network, inspect:

- request URL
- status code
- response body
- failed request behavior

## Safety Rules

- do not store API keys in local storage
- do not commit real private keys
- do not assume frontend `.env` values are secret
- do not type response data as `any` unless you can justify it

## Demo Questions

Be ready to answer:

1. Which file owns the API request?
2. Which type describes the API response?
3. Where is the env variable read?
4. What happens when the API fails?
5. What did you inspect in Network?

