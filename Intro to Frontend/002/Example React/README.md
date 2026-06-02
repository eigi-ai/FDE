# FDE React 002 Concepts Demo

This is a Vite React TypeScript teaching app for the FDE Frontend 002 session.

It demonstrates:

- routing with React Router across `/login`, `/dashboard`, `/api`, `/devtools`, and `/lessons`
- mock login persisted in `localStorage`
- a main dashboard built from reusable components
- `useState`, `useEffect`, `useMemo`, `useCallback`, and custom hooks
- API calling with both Axios and Fetch
- browser DevTools usage for Console, Network, Application, storage, and cookies
- feature-based folder structure

## Run

```bash
npm install
npm run dev
```

Open the dev server URL and login with the pre-filled mock credentials. Any non-empty password works.

## Build

```bash
npm run build
```

## Teaching Routes

- `/login`: mock auth and Local Storage persistence
- `/dashboard`: components, props, main dashboard, forms, and hooks
- `/api`: Axios vs Fetch, loading/error/success state, Network inspection
- `/devtools`: Console, Network, Application, storage, cookies, routing, folder structure
- `/lessons`: the full long-form React concepts page

## DevTools Teaching

- Console: open DevTools Console and click `Log Demo State`
- Network: open DevTools Network and click `Request Mock API`, `Load With Axios`, or `Load With Fetch`
- Application: click `Write Storage`, then inspect Local Storage, Session Storage, and Cookies
- React DevTools: inspect `AppShell`, `DashboardPage`, `MetricCard`, and `ContactCard`

## Folder Structure

```text
src/
  app/
    App.tsx
  features/
    auth/
      authContext.ts
      AuthProvider.tsx
      LoginPage.tsx
      useAuth.ts
    dashboard/
      components/
        MetricCard.tsx
      DashboardPage.tsx
    api-lab/
      ApiLabPage.tsx
    devtools/
      DevToolsPage.tsx
    react-lessons/
      components/
      hooks/
      data.ts
      types.ts
      ReactLessonsPage.tsx
  shared/
    components/
    hooks/
  styles/
    global.css
  main.tsx
```
