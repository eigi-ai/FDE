# 001 - React Router, Routes, Protected Routes, And Navigation

## Goal

Learn how a React app can have multiple pages controlled by the browser URL.

Core idea:

```text
URL changes -> React Router matches a route -> React renders the page component
```

## Why Routing Matters

In `002`, you may have switched pages using state:

```tsx
const [currentPage, setCurrentPage] = useState("dashboard");
```

That works for practice, but real apps usually need URL-based pages:

```text
/login
/dashboard
/profile
/settings
/api-lab
```

URL-based routing helps because:

- refresh can keep the user on the same page
- browser back and forward buttons work
- links can be shared
- each page can have its own component
- large apps become easier to organize

## Install React Router

In a Vite React app:

```bash
npm install react-router-dom
```

## Basic Router

```tsx
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { LoginPage } from "../features/auth/LoginPage";
import { DashboardPage } from "../features/dashboard/DashboardPage";
import { ProfilePage } from "../features/profile/ProfilePage";
import { SettingsPage } from "../features/settings/SettingsPage";
import { ApiLabPage } from "../features/api-lab/ApiLabPage";
import { AppShell } from "../shared/components/AppShell";

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />

        <Route element={<AppShell />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/settings" element={<SettingsPage />} />
          <Route path="/api-lab" element={<ApiLabPage />} />
        </Route>

        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="*" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## Important Router Pieces

`BrowserRouter` connects React Router to the browser URL.

`Routes` contains all route definitions.

`Route` maps a path to a component.

`Navigate` redirects the user.

`NavLink` creates navigation links and can show active state.

`Outlet` decides where nested page content appears inside a shared layout.

## Shared Layout With `Outlet`

Many pages should share the same app shell:

- header
- navigation
- main content area
- logout button

Example:

```tsx
import { NavLink, Outlet } from "react-router-dom";

export function AppShell() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <strong>Candidate Portal</strong>

        <nav aria-label="Main navigation">
          <NavLink to="/dashboard">Dashboard</NavLink>
          <NavLink to="/profile">Profile</NavLink>
          <NavLink to="/settings">Settings</NavLink>
          <NavLink to="/api-lab">API Lab</NavLink>
        </nav>
      </header>

      <main className="page">
        <Outlet />
      </main>
    </div>
  );
}
```

Key line:

```text
The layout stays. The page inside <Outlet /> changes.
```

## Protected Routes

A protected route stops logged-out users from seeing app pages.

Example:

```tsx
import { Navigate, Outlet, useLocation } from "react-router-dom";

type RequireAuthProps = {
  isLoggedIn: boolean;
};

export function RequireAuth({ isLoggedIn }: RequireAuthProps) {
  const location = useLocation();

  if (!isLoggedIn) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  return <Outlet />;
}
```

Use it around protected app pages:

```tsx
<Route element={<RequireAuth isLoggedIn={Boolean(user)} />}>
  <Route element={<AppShell />}>
    <Route path="/dashboard" element={<DashboardPage />} />
    <Route path="/profile" element={<ProfilePage />} />
    <Route path="/settings" element={<SettingsPage />} />
    <Route path="/api-lab" element={<ApiLabPage />} />
  </Route>
</Route>
```

Important:

```text
Frontend protected routes are only UI guards.
Real security must be enforced by the backend.
```

## Navigation Rules

For internal React pages, use:

```tsx
<Link to="/dashboard">Dashboard</Link>
```

or:

```tsx
<NavLink to="/dashboard">Dashboard</NavLink>
```

Do not use this for internal React pages:

```tsx
<a href="/dashboard">Dashboard</a>
```

Plain `a href` reloads the full page. `Link` and `NavLink` let React Router handle navigation.

## Key Line

```text
React Router turns URLs into page components without losing the single-page app behavior.
```

