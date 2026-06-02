# 007 - Build, Environment Variables, Deployment, And Production Checks

## Goal

Learn why working on localhost is not the final check.

Core idea:

```text
development server is for coding
production build is what users receive
```

## Development Server

In Vite:

```bash
npm run dev
```

This starts a development server.

Use it while building and debugging.

## Production Build

```bash
npm run build
```

This creates production files in:

```text
dist/
```

The `dist` folder is what gets deployed to static hosting.

## Production Preview

```bash
npm run preview
```

This serves the production build locally.

Why this matters:

```text
The dev server and production build are not exactly the same.
Always check production preview before saying the app is done.
```

## Env Variables

Use `.env.example` to show required config:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_API_KEY=replace-with-demo-key
```

Important:

```text
Only VITE_ variables are exposed to the Vite frontend app.
Frontend env variables are public in browser code.
```

Do not put private secrets in frontend env files.

## Deployment Idea

Most static frontend deployment follows this pattern:

```text
npm run build -> upload dist/
```

Possible hosting targets:

- Vercel
- Netlify
- GitHub Pages
- S3/CloudFront
- internal static hosting

The exact hosting platform can change. The build idea stays the same.

## Production Check List

After `npm run preview`, check:

- login works
- protected routes redirect correctly
- browser refresh works on routed pages
- navigation works
- API request uses the expected URL
- loading, error, empty, and success states work
- form validation still works
- local storage behavior is expected
- responsive layout still works
- Console has no unexpected errors

## Key Line

```text
An app is not ready until the production build has been checked.
```

