# Activity - Build The React API App

## Task

Build a React app using one API Ninjas endpoint.

## Required Structure

Recommended:

```text
src/
  app/
    App.jsx
  features/
    api-search/
      ApiSearchPage.jsx
      SearchForm.jsx
      ResultCard.jsx
      api.js
      useApiNinjasSearch.js
  shared/
    Loader.jsx
    ErrorMessage.jsx
    EmptyState.jsx
  main.jsx
  styles.css
```

## Requirements

- clear title
- at least 4 components
- props
- `useState`
- controlled input if using input
- event handler
- conditional rendering
- API call to API Ninjas
- API key header
- loading state
- error state
- empty state if applicable
- success/result state
- at least one custom hook
- Console and Network inspection in DevTools
- storage/cookies inspection if storage is used
- README

## Demo Questions

Be ready to answer:

1. Which API did you use?
2. What components did you create?
3. Which props are passed between components?
4. Which state variables control the UI?
5. Where is `useState` used?
6. Where is `useEffect` used, if used?
7. What custom hook did you create?
8. Where is the API call?
9. How do you show loading, error, empty, and success states?
10. What did you inspect in Console and Network?
11. Did you use local storage, session storage, or cookies?
12. Explain the app using:

```text
user action -> state change -> API request -> response -> re-render
```

## Rubric

| Area | Points |
| --- | ---: |
| App runs | 1 |
| Components are clear | 1 |
| Props are used correctly | 1 |
| `useState` is used meaningfully | 1 |
| Events/forms work | 1 |
| API call works | 1 |
| Loading/error/empty/success states exist | 1 |
| Custom hook is meaningful | 1 |
| DevTools used to inspect request/error | 1 |
| Candidate can explain the flow | 1 |
