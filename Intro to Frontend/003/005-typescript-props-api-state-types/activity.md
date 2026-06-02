# Activity - Add Useful TypeScript Types

## Goal

Practice typing props, forms, API responses, and UI state.

## Task

Add TypeScript types to one feature in your React app.

## Requirements

- type at least one component's props
- type one form values object
- type one API response
- type one API state object
- type one union state, such as request status
- remove unnecessary `any`
- run the TypeScript build
- explain one bug TypeScript can prevent

## Suggested Types

```ts
type RequestStatus = "idle" | "loading" | "success" | "error";
```

```ts
type ApiState<T> = {
  data: T | null;
  loading: boolean;
  error: string;
};
```

```ts
type Candidate = {
  id: string;
  name: string;
  role: string;
  status: "applied" | "interview" | "selected";
};
```

## Manual Checks

Check:

- props are typed
- API response shape matches the real response
- invalid status strings are rejected
- null data is handled safely
- there is no unnecessary `any`
- `npm run build` passes

## Demo Questions

Be ready to answer:

1. Which component props did you type?
2. Which API response did you type?
3. Which form values did you type?
4. Where did you use a union type?
5. What mistake did TypeScript help prevent?

