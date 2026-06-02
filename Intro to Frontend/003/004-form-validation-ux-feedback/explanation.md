# 004 - Form Validation And UX Feedback

## Goal

Learn how to make forms guide the user clearly.

Core idea:

```text
input state -> validation -> error messages -> disabled/loading feedback -> submit
```

## Why Validation Matters

A form should answer:

- what is required?
- what is invalid?
- what can the user fix?
- is the form submitting?
- did the submit succeed or fail?

Console logs are not enough. The user needs visible feedback.

## Form State

Example login form state:

```tsx
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");
const [errors, setErrors] = useState<Partial<Record<keyof LoginForm, string>>>({});
const [submitting, setSubmitting] = useState(false);
const [message, setMessage] = useState("");
```

## Form Values Type

```ts
type LoginForm = {
  email: string;
  password: string;
};
```

## Validation Function

```ts
function validateLoginForm(values: LoginForm) {
  const errors: Partial<Record<keyof LoginForm, string>> = {};

  if (!values.email.trim()) {
    errors.email = "Email is required.";
  }

  if (!values.password.trim()) {
    errors.password = "Password is required.";
  }

  return errors;
}
```

Keep validation in a function so it is easier to read and test.

## Submit Handler

```tsx
async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
  event.preventDefault();

  const nextErrors = validateLoginForm({ email, password });
  setErrors(nextErrors);
  setMessage("");

  if (Object.keys(nextErrors).length > 0) {
    console.log("Validation errors", nextErrors);
    return;
  }

  setSubmitting(true);

  try {
    await login(email, password);
    setMessage("Login successful.");
  } catch (error) {
    console.error("Login failed", error);
    setMessage("Login failed. Please try again.");
  } finally {
    setSubmitting(false);
  }
}
```

## Disabled Button

```tsx
const isInvalid = !email.trim() || !password.trim();

<button disabled={isInvalid || submitting}>
  {submitting ? "Logging in..." : "Login"}
</button>
```

The button should communicate that the user cannot submit yet.

## Field-Level Error

```tsx
<label htmlFor="email">Email</label>
<input
  id="email"
  value={email}
  aria-invalid={Boolean(errors.email)}
  onChange={(event) => setEmail(event.target.value)}
/>
{errors.email ? <p className="field-error">{errors.email}</p> : null}
```

## Good UX Feedback

Your form should show:

- visible labels
- field-level errors
- disabled submit when invalid or submitting
- loading text while submitting
- success or failure message
- clear focus styles

## Key Line

```text
Good validation tells the user what went wrong and what to do next.
```

