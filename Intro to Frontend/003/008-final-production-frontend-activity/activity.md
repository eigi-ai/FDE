# Activity - Build A Production-Shaped Candidate Portal

## Goal

Build a React TypeScript frontend that combines all `003` concepts.

## Time

2 hours

## Task

Create a frontend-only Candidate Portal.

## Requirements

### Routing

- use React Router
- create `/login`
- create `/dashboard`
- create `/profile`
- create `/settings`
- create `/api-lab`
- protect all app pages except `/login`
- redirect `/` to `/dashboard`
- redirect unknown URLs to `/dashboard`

### Layout And UI

- create shared `AppShell`
- create visible navigation
- create responsive dashboard grid
- create reusable `StatCard`
- create reusable `TextField`
- add readable spacing
- add mobile-friendly layout
- add visible focus styles

### API

- create `services/apiClient.ts`
- create one feature service file
- use `.env.example`
- type API response
- handle failed requests
- show loading, error, empty, and success states
- inspect request in Network

### Forms

- create at least one validated form
- use controlled inputs
- show field-level errors
- disable submit when invalid or submitting
- show success or failure feedback

### TypeScript

- type component props
- type form values
- type API response
- type API state
- avoid unnecessary `any`

### Tests

- write one component test
- write one user-flow test
- run `npm test`

### Production

- run `npm run build`
- run `npm run preview`
- complete production checks
- write `production-check-report.md`

## Suggested 2-Hour Plan

| Time | Work |
| --- | --- |
| 0-15 min | Create route tree, pages, and layout |
| 15-35 min | Add login and protected routes |
| 35-55 min | Add responsive dashboard and reusable UI |
| 55-75 min | Add API service, env variable, and API state |
| 75-90 min | Add form validation and user feedback |
| 90-105 min | Add TypeScript types |
| 105-115 min | Add one component test and one user-flow test |
| 115-120 min | Run build, preview, and final checks |

## Deliverables

Submit:

1. React TypeScript app
2. route tree with protected routes
3. shared layout and navigation
4. responsive dashboard UI
5. API service files
6. `.env.example`
7. typed props, state, and API response
8. validated form
9. component test
10. user-flow test
11. production-check report

## Demo Questions

Be ready to answer:

1. What is your route tree?
2. Which routes are protected?
3. Which component owns the shared layout?
4. Which file calls the API?
5. Where are env variables read?
6. What happens when the API fails?
7. What validation rules did you add?
8. Which props and API responses did you type?
9. What does your component test prove?
10. What does your user-flow test prove?
11. What did you check after production preview?

