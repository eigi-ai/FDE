# 003 - API Structure, Env Variables, Error Handling, And Response Types

## Goal

Learn how to organize API code outside page components.

Core idea:

```text
page component handles UI
service file handles API request
Axios client handles common request config
types describe API data
env variables configure the API URL
```

## Why Move API Code Out Of Pages?

This works for a small demo:

```tsx
async function loadData() {
  const response = await fetch("https://api.example.com/candidates");
  const data = await response.json();
  setCandidates(data.items);
}
```

But in a larger app, this becomes hard to manage.

Better structure:

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

## What Is Axios?

Axios is a popular JavaScript library for making HTTP requests.

Install it:

```bash
npm install axios
```

You can call APIs with `fetch` or Axios.

With `fetch`:

```ts
const response = await fetch("/api/candidates");

if (!response.ok) {
  throw new Error("Request failed");
}

const data = await response.json();
```

With Axios:

```ts
const response = await axios.get("/api/candidates");
const data = response.data;
```

Beginner-friendly difference:

```text
fetch gives you a Response object.
You manually check response.ok and parse response.json().

Axios gives you response.data.
Axios rejects failed status codes like 404 and 500 by default.
```

Axios does not remove the need for good structure. You should still keep API logic in service files.

## Vite Env Variables

In Vite, frontend env variables must start with:

```text
VITE_
```

Example `.env`:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_API_KEY=demo-key
```

Example `.env.example`:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_API_KEY=replace-with-demo-key
```

Read env variables:

```ts
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
```

Important:

```text
Frontend env variables are visible in browser code after build.
Do not put private secrets in frontend env files.
```

## API Client

Create one reusable Axios client for common request behavior.

```ts
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
const API_KEY = import.meta.env.VITE_API_KEY;

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: API_KEY
    ? {
        "X-Api-Key": API_KEY,
      }
    : {},
});

export async function apiGet<T>(path: string): Promise<T> {
  try {
    const response = await apiClient.get<T>(path);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const status = error.response?.status;
      const message = status
        ? `Request failed with status ${status}`
        : "Request failed before the server responded.";

      throw new Error(message);
    }

    throw error;
  }
}
```

What this does:

- builds full API URL
- sends request
- uses shared headers
- handles failed Axios requests
- returns `response.data`
- returns typed data

## Response Types

Example:

```ts
export type Candidate = {
  id: string;
  name: string;
  role: string;
  status: "applied" | "interview" | "selected";
};

export type CandidateListResponse = {
  items: Candidate[];
};
```

## Feature Service

```ts
import { apiGet } from "./apiClient";
import type { CandidateListResponse } from "../types/candidate";

export function getCandidates() {
  return apiGet<CandidateListResponse>("/candidates");
}
```

## API State In UI

```ts
type ApiState<T> = {
  data: T | null;
  loading: boolean;
  error: string;
};
```

Use it:

```tsx
const [candidateState, setCandidateState] = useState<ApiState<CandidateListResponse>>({
  data: null,
  loading: false,
  error: "",
});
```

## User-Facing Error Handling

The app needs both:

```text
Console error -> helps developer debug
UI error -> helps user understand what happened
```

Example:

```tsx
try {
  setCandidateState({ data: null, loading: true, error: "" });
  const data = await getCandidates();
  console.log("Candidates response", data);
  setCandidateState({ data, loading: false, error: "" });
} catch (error) {
  console.error("Candidates request failed", error);
  setCandidateState({
    data: null,
    loading: false,
    error: "Could not load candidates. Please try again.",
  });
}
```

## Where Axios Should Live

Good:

```text
Page component -> candidateService.ts -> apiClient.ts -> Axios
```

Avoid:

```text
Page component -> Axios directly everywhere
```

If every page imports Axios directly, API logic becomes scattered.

## Key Line

```text
API service files keep network logic separate from UI logic, and Axios keeps request code cleaner than raw fetch.
```
