import type { Contact, Lesson, UiStatus } from './types'

export const lessons: Lesson[] = [
  { id: 'mental-model', eyebrow: '001', title: 'React Mental Model', summary: 'State changes, React re-renders, and UI updates.' },
  { id: 'jsx-components', eyebrow: '002', title: 'JSX And Components', summary: 'Build UI with JavaScript functions that return JSX.' },
  { id: 'props', eyebrow: '003', title: 'Props And Composition', summary: 'Pass data into reusable child components.' },
  { id: 'state-events', eyebrow: '004', title: 'State, Events, Conditional UI', summary: 'Use useState and events to drive what appears.' },
  { id: 'lists-forms', eyebrow: '005', title: 'Lists, Keys, Forms', summary: 'Render arrays, use stable keys, and control inputs.' },
  { id: 'effects-api', eyebrow: '006', title: 'Effects And API State', summary: 'Use effects for synchronization and track API states.' },
  { id: 'custom-hooks', eyebrow: '007', title: 'Custom Hooks', summary: 'Extract reusable stateful logic into useSomething functions.' },
  { id: 'devtools', eyebrow: '008', title: 'Browser Developer Tools', summary: 'Inspect Console, Network, Application storage, and cookies.' },
  { id: 'folder-structure', eyebrow: '010', title: 'Vite, TypeScript, Folder Structure', summary: 'Understand the files and folders in a React TypeScript app.' },
  { id: 'final-activity', eyebrow: '009', title: 'Final React API Activity', summary: 'Build one API Ninjas React app with AI-assisted planning.' },
]

export const starterContacts: Contact[] = [
  { id: 1, name: 'Asha Mehta', email: 'asha@example.com', status: 'Lead' },
  { id: 2, name: 'Rohit Sharma', email: 'rohit@example.com', status: 'Customer' },
  { id: 3, name: 'Neha Verma', email: 'neha@example.com', status: 'Follow-up' },
]

export const uiStatusCopy: Record<UiStatus, { title: string; body: string }> = {
  idle: { title: 'Idle', body: 'The app is ready. Nothing has been requested yet.' },
  loading: { title: 'Loading', body: 'A request or action is in progress. The user needs feedback.' },
  success: { title: 'Success', body: 'The action completed and the UI can show the result.' },
  error: { title: 'Error', body: 'Something failed. Show a clear message and recovery path.' },
  empty: { title: 'Empty', body: 'The request worked, but there is no matching data to show.' },
}
