# 008 - Final Production Frontend Activity

## Goal

Build a React TypeScript app that is organized like a real frontend project.

This final activity combines:

- React Router
- URL-based pages
- protected routes
- shared layout
- navigation
- responsive UI
- reusable components
- API service files
- env variables
- error handling
- TypeScript types
- form validation
- component test
- user-flow test
- production build checks

## Required App

Build:

```text
Candidate Portal
```

Required pages:

```text
/login
/dashboard
/profile
/settings
/api-lab
```

Required route behavior:

- `/login` is public
- app pages are protected
- `/` redirects to `/dashboard`
- unknown URLs redirect to `/dashboard`
- logged-out users opening protected pages redirect to `/login`

## Required Flow

Your app should show this full flow:

```text
URL -> route -> page component -> layout -> form/API/state logic -> UI feedback -> production build
```

## Required Structure

Recommended:

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
      components/
        StatCard.tsx
    profile/
      ProfilePage.tsx
    settings/
      SettingsPage.tsx
    api-lab/
      ApiLabPage.tsx
  shared/
    components/
      AppShell.tsx
      TextField.tsx
      StatusMessage.tsx
  services/
    apiClient.ts
    candidateService.ts
  types/
    api.ts
    candidate.ts
  styles/
    global.css
```

## Required Checks

Before demo, you must run:

```bash
npm test
npm run build
npm run preview
```

## Required Explanation

Be able to explain:

- route tree
- protected routes
- shared layout
- reusable UI components
- API service file
- env variable usage
- form validation
- TypeScript types
- tests
- production preview checks

## Key Line

```text
This activity is about app structure and production readiness, not only making screens.
```

