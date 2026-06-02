# Activity - Refactor An API Call Into Service Files

## Goal

Practice API structure, env variables, response types, and error handling.

## Task

Add an Axios-based API feature to your `/api-lab` page.

You can use:

- a real public API
- API Ninjas
- a mock local JSON file if API keys are not available

## Requirements

- install `axios`
- create `.env.example`
- read API base URL from `import.meta.env`
- create `services/apiClient.ts`
- create an Axios instance with `axios.create`
- create one feature service file, such as `candidateService.ts`
- create response types
- call the service from the page
- show loading state
- show success state
- show empty state if no useful data exists
- show user-facing error state
- handle Axios errors with `try/catch`
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

## Install Axios

```bash
npm install axios
```

## Axios Client Requirement

Your page should not call Axios directly.

Use this flow:

```text
ApiLabPage -> candidateService -> apiClient -> Axios
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
- request headers if your API needs a key
- status code
- response body
- failed request behavior

## Safety Rules

- do not store API keys in local storage
- do not commit real private keys
- do not assume frontend `.env` values are secret
- do not import Axios directly into every page component
- do not type response data as `any` unless you can justify it

## Demo Questions

Be ready to answer:

1. Which file owns the API request?
2. Where is Axios configured?
3. Which type describes the API response?
4. Where is the env variable read?
5. What happens when the API fails?
6. What did you inspect in Network?
