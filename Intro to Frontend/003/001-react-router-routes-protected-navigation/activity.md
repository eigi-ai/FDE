# Activity - Add Routes, Protected Pages, And Navigation

## Goal

Practice React Router by turning a React app into a multi-page app.

## Task

Create a React app with these pages:

```text
/login
/dashboard
/profile
/settings
/api-lab
```

## Requirements

- install `react-router-dom`
- create one component for each page
- configure routes using `BrowserRouter`, `Routes`, and `Route`
- create a shared `AppShell` layout
- use `Outlet` for nested pages
- use `NavLink` or `Link` for internal navigation
- redirect `/` to `/dashboard`
- redirect unknown routes to `/dashboard`
- create a `RequireAuth` component
- protect `/dashboard`, `/profile`, `/settings`, and `/api-lab`
- redirect logged-out users to `/login`

## Suggested Files

```text
src/
  app/
    App.tsx
  features/
    auth/
      LoginPage.tsx
      RequireAuth.tsx
    dashboard/
      DashboardPage.tsx
    profile/
      ProfilePage.tsx
    settings/
      SettingsPage.tsx
    api-lab/
      ApiLabPage.tsx
  shared/
    components/
      AppShell.tsx
```

## Minimum Login Behavior

You can use demo login state.

Example:

```tsx
const [user, setUser] = useState<string | null>(() => {
  return localStorage.getItem("candidate-user");
});
```

On login:

```tsx
localStorage.setItem("candidate-user", email);
setUser(email);
```

On logout:

```tsx
localStorage.removeItem("candidate-user");
setUser(null);
```

## Test Manually

Check:

- open `/login`
- login and navigate to `/dashboard`
- click each navigation link
- refresh on `/profile`
- logout
- manually open `/settings`
- confirm logged-out user redirects to `/login`

## Demo Questions

Be ready to answer:

1. What is your route tree?
2. Which routes are public?
3. Which routes are protected?
4. What does `Outlet` do?
5. Why should you use `Link` or `NavLink` instead of `a href`?
6. Why is frontend route protection not real backend security?

