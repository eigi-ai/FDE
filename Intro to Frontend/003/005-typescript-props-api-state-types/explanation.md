# 005 - TypeScript Basics For Props, API Responses, And State

## Goal

Learn how TypeScript helps describe the shape of frontend data.

Core idea:

```text
types describe what data should look like
```

TypeScript is useful when data moves through:

- component props
- form state
- API responses
- UI status state
- custom hooks

## Props Type

```tsx
type StatCardProps = {
  label: string;
  value: string | number;
  helperText?: string;
};

export function StatCard({ label, value, helperText }: StatCardProps) {
  return (
    <article className="stat-card">
      <span>{label}</span>
      <strong>{value}</strong>
      {helperText ? <small>{helperText}</small> : null}
    </article>
  );
}
```

This tells React developers:

```text
StatCard needs label and value.
helperText is optional.
```

## Form Values Type

```ts
type ProfileForm = {
  name: string;
  email: string;
  role: string;
};
```

Use it in validation:

```ts
function validateProfileForm(values: ProfileForm) {
  const errors: Partial<Record<keyof ProfileForm, string>> = {};

  if (!values.name.trim()) {
    errors.name = "Name is required.";
  }

  if (!values.email.trim()) {
    errors.email = "Email is required.";
  }

  return errors;
}
```

## API Response Type

```ts
type Candidate = {
  id: string;
  name: string;
  role: string;
  status: "applied" | "interview" | "selected";
};

type CandidateListResponse = {
  items: Candidate[];
};
```

This helps prevent mistakes like:

```tsx
candidate.fullName
```

when the real field is:

```tsx
candidate.name
```

## State Union Type

```ts
type RequestStatus = "idle" | "loading" | "success" | "error";

const [status, setStatus] = useState<RequestStatus>("idle");
```

Now TypeScript catches invalid status values:

```ts
setStatus("done");
```

`"done"` is not allowed.

## Generic API State

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

## Avoid `any`

This removes most of TypeScript's value:

```ts
const [data, setData] = useState<any>(null);
```

Better:

```ts
const [data, setData] = useState<CandidateListResponse | null>(null);
```

## Key Line

```text
TypeScript is useful when it makes component and data contracts clear.
```

