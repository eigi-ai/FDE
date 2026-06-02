# Problem Statement - Production-Ready React Frontend Activity

## Time Limit

2 hours

## Goal

Build a React TypeScript frontend that looks like a real app structure, not only a single-page demo.

Your app must combine:

- React Router routes
- protected routes
- shared navigation and layout
- responsive styling
- reusable UI components
- API service files
- environment variables
- form validation
- typed props, state, and API responses
- one component test
- one user-flow test
- production build checks

## Scenario

Create a small Candidate Portal frontend.

The app should let a user:

1. log in with a demo form
2. enter protected app pages
3. navigate between pages using the URL
4. view dashboard data
5. update a profile/settings form
6. fetch data from an API
7. see loading, error, empty, and success states
8. run tests
9. build and preview the production app

This is a frontend-only activity. You do not need to build a backend.

## Required Pages

Create these pages:

```text
/login
/dashboard
/profile
/settings
/api-lab
```

Required behavior:

- `/login` is public.
- `/dashboard`, `/profile`, `/settings`, and `/api-lab` are protected.
- logged-out users opening protected URLs are redirected to `/login`.
- logged-in users can navigate using visible navigation links.
- `/` redirects to `/dashboard`.
- unknown URLs redirect to `/dashboard`.

## Required Route Structure

Use React Router with:

- `BrowserRouter`
- `Routes`
- `Route`
- `Navigate`
- `NavLink` or `Link`
- `Outlet`
- one `RequireAuth` component

Be ready to explain:

```text
URL -> route match -> page component -> shared layout -> nested page content
```

## Required Layout And Styling

Your app must include:

- shared app shell/layout
- responsive navigation
- responsive dashboard grid
- reusable card component
- reusable form field component
- readable spacing
- visible form labels
- focus styles for keyboard users
- mobile-friendly layout

## Required API Structure

Do not keep API logic directly inside the page component.

Create a structure like:

```text
src/
  services/
    apiClient.ts
    candidateService.ts
  types/
    candidate.ts
```

Your API code must:

- read API base URL from env variable
- use a service function
- type the response shape
- handle failed responses
- show user-facing error UI
- log useful developer errors in Console
- inspect the request in Network

Use `.env.example`:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_API_KEY=replace-with-demo-key
```

Important:

```text
Frontend env variables are public after build.
Do not store private secrets in frontend env files or local storage.
```

## Required Form Validation

At least one form must include:

- controlled inputs
- required field validation
- field-level error messages
- disabled submit button when invalid or submitting
- loading/submitting feedback
- success or failure message

## Required TypeScript

Use TypeScript types for:

- component props
- form values
- API response
- API state
- route/auth state if needed

Do not use `any` unless you can clearly justify it.

## Required Tests

Add at least two tests:

1. one component test
2. one user-flow test

Suggested tests:

- `StatCard` renders label and value
- empty login form shows validation errors
- successful login redirects to dashboard
- protected route redirects logged-out user

## Required Build And Deployment Checks

Run:

```bash
npm test
npm run build
npm run preview
```

In production preview, check:

- routes work
- protected routes redirect correctly
- refresh works on protected pages
- API request uses expected URL
- form validation still works
- Console has no unexpected errors
- responsive layout still works
- local storage behavior is expected

## Final Deliverables

Submit:

1. React TypeScript app source code
2. route tree with protected routes
3. shared layout and navigation
4. responsive dashboard UI
5. API service files
6. `.env.example`
7. typed props, state, and API response
8. form validation
9. component test
10. user-flow test
11. production-check report

## Production Check Report

Use this format:

```md
# Production Check Report

## Routes
Which routes did you test?

## Protected Routes
How did you confirm logged-out users are redirected?

## API
Which request did you inspect in Network?
What happened when the request failed?

## Forms
Which validation cases did you test?

## Tests
Which component test did you write?
Which user-flow test did you write?

## Build Preview
Did npm run build pass?
Did npm run preview work?
What production behavior did you check?
```

## Evaluation Rubric

| Area | Points |
| --- | ---: |
| App runs without errors | 2 |
| React Router route tree is correct | 3 |
| Protected routes work | 3 |
| Shared layout and navigation are clear | 2 |
| Responsive layout and reusable UI patterns are used | 3 |
| API logic is separated into service files | 3 |
| Env variables are used correctly | 2 |
| API error handling shows user-facing feedback | 3 |
| Form validation and UX feedback are clear | 3 |
| TypeScript props/state/API types are meaningful | 3 |
| Component test exists and checks behavior | 2 |
| User-flow test exists and checks behavior | 2 |
| Build and production preview checks are completed | 3 |
| Candidate can explain the app structure | 3 |
| Total | 37 |

## Important Rules

- Do not put everything in `App.tsx`.
- Do not use plain `a href` for internal React navigation.
- Do not treat frontend protected routes as real backend security.
- Do not store private API keys in local storage.
- Do not hide API errors only in Console.
- Do not use `any` everywhere.
- Do not skip build and preview checks.

