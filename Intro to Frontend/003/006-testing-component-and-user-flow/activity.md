# Activity - Add One Component Test And One User-Flow Test

## Goal

Practice testing visible frontend behavior.

## Task

Add at least two tests to your React app.

## Requirements

- install Vitest and React Testing Library tools
- add `npm test`
- write one component test
- write one user-flow test
- run `npm test`
- fix at least one failing test if needed
- explain what behavior each test protects

## Suggested Component Tests

Choose one:

- `StatCard` renders label and value
- `PageHeader` renders title and description
- `StatusMessage` renders an error message
- `TextField` renders label and error

## Suggested User-Flow Tests

Choose one:

- empty login form shows validation errors
- valid login calls login handler
- profile form shows required field error
- protected route redirects logged-out user

## Test Checklist

Your tests should:

- use `render`
- use `screen`
- use `userEvent` for user actions
- check visible text, label, or role
- have a clear test name

## Demo Questions

Be ready to answer:

1. What component did you test?
2. What user flow did you test?
3. What does the test prove?
4. What would break this test?
5. Why is testing behavior better than testing implementation details?

