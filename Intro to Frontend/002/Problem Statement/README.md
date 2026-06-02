# Problem Statement - React Frontend Dashboard Activity

## Time Limit

2 hours

## Goal

Build a frontend-only React app that uses the main concepts covered in today's React lecture.

Your app must show this complete frontend flow:

```text
login -> landing page -> dashboard -> user action -> state change -> API request -> response -> UI update
```

## Scenario

Create a small personal dashboard app.

The user should be able to:

1. log in from a login page
2. see a landing page after login
3. open a dashboard page
4. search or fetch data from an API
5. save useful data in local storage
6. stay logged in for only 1 minute
7. get logged out automatically after 1 minute

This is a frontend activity only. You do not need to build a backend.

## Required Pages

Your frontend must have at least 3 pages.

### 1. Login Page

Requirements:

- create a login form
- use controlled inputs
- store input values in React state
- validate that the username/email is not empty
- on successful login, save basic session data in local storage
- move the user to the landing page
- log a useful message in the Console when login succeeds

Example local storage data:

```js
{
  "username": "student",
  "loggedInAt": 1710000000000,
  "expiresAt": 1710000060000
}
```

Do not store real passwords or API keys in local storage.

### 2. Landing Page

Requirements:

- show a welcome message using the logged-in user's name
- explain what the dashboard does in the UI
- include a button or navigation link to the dashboard
- use at least one reusable component with props
- show at least one list rendered with `.map()`
- use proper `key` props for list items

Example components:

```text
Header
FeatureCard
NavigationButton
```

### 3. Dashboard Page

Requirements:

- call at least one API
- use a controlled search form or action button
- show loading, error, empty, and success states
- display API results using reusable components
- allow the user to save at least one value to local storage
- read saved data back from local storage after page refresh
- include a logout button
- show the auto logout countdown on the screen

You can use any suitable API Ninjas endpoint, or another API approved by the instructor.

Before coding the API feature, identify:

1. API endpoint URL
2. query parameters
3. request headers
4. response shape
5. fields you want to display
6. possible error cases

## Required React Concepts

Your app must include all of these:

- React frontend app
- JSX
- at least 6 components
- props
- composition
- `useState`
- `useEffect`
- at least one custom hook
- events
- controlled form inputs
- conditional rendering
- list rendering with `.map()`
- correct `key` usage
- API request
- loading state
- error state
- empty state
- success state
- local storage persistence
- browser Developer Tools usage
- Console logging
- Network inspection
- Application storage inspection

## Required Components

Create your own components. Do not keep everything inside `App.jsx`.

Minimum recommended components:

```text
App
LoginPage
LandingPage
DashboardPage
Header
SearchForm
ResultCard
SavedItem
Loader
ErrorMessage
```

You can create more components if your UI needs them.

## Required Hooks And State

Use React state to manage UI behavior.

Required state examples:

```js
const [user, setUser] = useState(null);
const [currentPage, setCurrentPage] = useState("login");
const [query, setQuery] = useState("");
const [data, setData] = useState(null);
const [loading, setLoading] = useState(false);
const [error, setError] = useState("");
const [savedItems, setSavedItems] = useState([]);
const [secondsLeft, setSecondsLeft] = useState(60);
```

Use `useEffect` for side effects such as:

- loading session data from local storage when the app starts
- saving selected data to local storage
- creating and cleaning up the auto logout timer
- checking whether the saved session is already expired

Create at least one custom hook.

Recommended custom hooks:

```text
useLocalStorage
useAutoLogout
useApiSearch
```

You do not need to create all three, but at least one custom hook is required.

## Auto Logout Requirement

After successful login:

1. set the logged-in user in React state
2. set an expiry time for 1 minute from login
3. save the session data in local storage
4. show a countdown in the UI
5. use `useEffect` with `setInterval` or `setTimeout`
6. automatically logout when the time reaches 0
7. clear the auth/session data from local storage
8. send the user back to the login page
9. log the auto logout event in the Console

The timer must be cleaned up when the component unmounts or when the user logs out manually.

Expected behavior:

```text
User logs in -> timer starts at 60 seconds -> countdown updates -> at 0 seconds user is logged out
```

## Local Storage Requirement

Use local storage for persistent data.

You must store at least two useful values:

1. login/session data
2. one dashboard value, such as saved result, last search, theme, or favorite item

After refreshing the browser:

- saved dashboard data should still be visible
- expired login data should not keep the user logged in

Do not store:

- real password
- API key
- sensitive personal data

## API Requirement

Your dashboard must call an API and render the response.

The app must show:

- idle state before the first API call
- loading state while the request is running
- success state when data arrives
- empty state when there is no useful data to show
- error state when the request fails

Your API code should log:

```js
console.log("API request started", query);
console.log("API response", data);
console.error("API error", error);
```

The UI must also show the error to the user. Do not only log the error in the Console.

## Developer Tools Requirement

Use browser Developer Tools while building and debugging.

### Console

You must log:

- normal app events
- form submit event
- login success
- API request start
- API response
- API error
- manual logout
- automatic logout

Example:

```js
console.log("Login success", user);
console.log("Search submitted", query);
console.log("API response", data);
console.error("API error", error);
console.log("Auto logout triggered");
```

### Network

Inspect your API request in the Network tab.

Check:

- request URL
- query parameters
- request headers
- status code
- response body
- failed request behavior

If you use API Ninjas, confirm the request includes:

```text
X-Api-Key
```

### Application

Inspect storage in the Application tab.

Check:

- local storage keys
- local storage values
- session storage, if you used it
- cookies, even if your app does not create any

Be ready to explain the difference:

```text
React state resets when the page reloads.
Local storage survives page reloads.
Session storage survives reloads but is cleared when the tab/session ends.
Cookies can be sent automatically with matching browser requests.
```

## Suggested Folder Structure

You can use this structure:

```text
src/
  app/
    App.jsx
  pages/
    LoginPage.jsx
    LandingPage.jsx
    DashboardPage.jsx
  components/
    Header.jsx
    FeatureCard.jsx
    SearchForm.jsx
    ResultCard.jsx
    SavedItem.jsx
    Loader.jsx
    ErrorMessage.jsx
  hooks/
    useLocalStorage.js
    useAutoLogout.js
    useApiSearch.js
  services/
    api.js
  main.jsx
  styles.css
```

This exact structure is not mandatory, but your files should be clearly organized.

## Suggested 2-Hour Plan

| Time | Work |
| --- | --- |
| 0-15 min | Create React app, plan pages/components, choose API |
| 15-35 min | Build Login page, controlled form, login state |
| 35-50 min | Build Landing page, reusable components, props, list rendering |
| 50-80 min | Build Dashboard page, API call, loading/error/success states |
| 80-100 min | Add local storage persistence and saved dashboard data |
| 100-110 min | Add 1-minute auto logout timer |
| 110-120 min | Use DevTools, test, fix errors, prepare demo |

## Final Deliverables

Submit:

1. React app source code
2. working login, landing, and dashboard pages
3. at least one custom hook
4. local storage persistence
5. API integration
6. Console logs for events, API response, and errors
7. a short `devtools-debug-report.md`

Use this format for `devtools-debug-report.md`:

```md
# DevTools Debug Report

## Console
What logs did you add?
Did you see any errors?

## Network
Which API request did you inspect?
What status code came back?
What response body did you see?

## Application Storage
Which local storage keys did you create?
What happened after refresh?
Did you find any session storage or cookies?

## Auto Logout
How did you confirm the user was logged out after 1 minute?
```

## Demo Questions

Be ready to answer:

1. What pages did you create?
2. What components did you create?
3. Which components receive props?
4. Where did you use `useState`?
5. Where did you use `useEffect`?
6. What custom hook did you create?
7. What data did you save in local storage?
8. How does your auto logout logic work?
9. Which API did you use?
10. Where is your API request code?
11. How does the UI show loading, error, empty, and success states?
12. What did you inspect in Console?
13. What did you inspect in Network?
14. What did you inspect in Application storage?
15. Explain your app using:

```text
user action -> state change -> API request -> response -> re-render
```

## Evaluation Rubric

| Area | Points |
| --- | ---: |
| App runs without errors | 2 |
| Login page works with controlled form | 2 |
| Landing page exists and uses reusable components | 2 |
| Dashboard page exists and calls an API | 2 |
| At least 6 components are used clearly | 2 |
| Props and composition are used correctly | 2 |
| `useState` manages meaningful UI state | 2 |
| `useEffect` is used correctly for side effects | 2 |
| At least one custom hook is created and used | 2 |
| Local storage persists useful data | 2 |
| Auto logout after 1 minute works | 2 |
| Loading, error, empty, and success states are handled | 2 |
| Lists use `.map()` and correct keys | 1 |
| Console logs include app events, API response, and errors | 1 |
| Network tab is used to inspect API request/response | 1 |
| Application tab is used to inspect storage/cookies | 1 |
| Candidate can explain the app flow clearly | 2 |
| Total | 30 |

## Important Rules

- This is a frontend-only activity.
- Do not build a backend.
- Do not store API keys in local storage.
- Do not store real passwords.
- Do not hardcode the final API response instead of calling the API.
- The app must have user-facing error UI, not only Console errors.
- The auto logout timer must actually log the user out after 1 minute.
