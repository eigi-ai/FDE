# 003 - API Structure, Env Variables, Error Handling, And Response Types

## Goal

Learn how to organize API code outside page components.

Core idea:

```text
page component handles UI
service file handles API request
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

Create one reusable client for common request behavior.

```ts
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function apiGet<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`);

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}
```

What this does:

- builds full API URL
- sends request
- checks failed status codes
- parses JSON
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

## Key Line

```text
API service files keep network logic separate from UI logic.
```

