# 006 - Testing Basics: Component Test And User-Flow Test

## Goal

Learn how to write simple frontend tests that check user-visible behavior.

Core idea:

```text
render UI -> simulate user action -> assert visible result
```

## Why Test?

Tests help you confirm that important UI behavior still works after changes.

For this session, focus on:

1. one component test
2. one user-flow test

Do not try to test everything.

## Recommended Tools

For a Vite React app:

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event jsdom
```

Add script:

```json
{
  "scripts": {
    "test": "vitest"
  }
}
```

## Component Test

A component test checks one reusable component.

Example:

```tsx
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom/vitest";
import { StatCard } from "./StatCard";

test("renders stat label and value", () => {
  render(<StatCard label="Applications" value={24} />);

  expect(screen.getByText("Applications")).toBeInTheDocument();
  expect(screen.getByText("24")).toBeInTheDocument();
});
```

This test checks visible behavior:

```text
When StatCard receives props, the user can see the label and value.
```

## User-Flow Test

A user-flow test simulates what a user does.

Example:

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import "@testing-library/jest-dom/vitest";
import { LoginPage } from "./LoginPage";

test("shows validation when login form is empty", async () => {
  const user = userEvent.setup();

  render(<LoginPage />);

  await user.click(screen.getByRole("button", { name: /login/i }));

  expect(screen.getByText(/email is required/i)).toBeInTheDocument();
});
```

This test checks:

```text
When the user submits an empty form, the app shows validation feedback.
```

## Good Testing Queries

Prefer queries based on what users see:

- `getByRole`
- `getByLabelText`
- `getByText`

Avoid testing private implementation details when possible.

## What Not To Test First

Avoid beginner tests like:

- checking internal state variables directly
- checking CSS class names only
- testing every implementation detail
- testing generated code you cannot explain

## Key Line

```text
A good frontend test proves that a user-visible behavior still works.
```

