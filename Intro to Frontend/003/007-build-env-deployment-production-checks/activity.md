# Activity - Build, Preview, And Check Production Behavior

## Goal

Practice production build checks for a Vite React app.

## Task

Run your app as a production build and verify important behavior.

## Requirements

- create `.env.example`
- run `npm run build`
- fix build errors if any
- run `npm run preview`
- open the preview URL
- test at least 3 routes
- test one protected route
- test one form validation case
- test one API request
- inspect Console
- inspect Network
- write a short production-check report

## Required Commands

```bash
npm run build
npm run preview
```

## Production Check Report

Create `production-check-report.md`:

```md
# Production Check Report

## Build
Did npm run build pass?

## Preview
Did npm run preview work?

## Routes
Which routes did you test?

## Protected Routes
How did you test redirect behavior?

## API
Which request did you inspect in Network?

## Forms
Which validation case did you test?

## Console
Were there any unexpected errors?
```

## Demo Questions

Be ready to answer:

1. What folder does Vite create for deployment?
2. Why do we run `npm run preview`?
3. Are frontend env variables secret?
4. Which routes did you test after preview?
5. What did you inspect in Console and Network?

