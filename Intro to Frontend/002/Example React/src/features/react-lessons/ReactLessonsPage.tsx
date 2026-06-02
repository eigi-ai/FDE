import { useEffect, useMemo, useState } from 'react'
import type { FormEvent } from 'react'
import { CodeBlock } from '../../shared/components/CodeBlock'
import { Section } from '../../shared/components/Section'
import { StatusMessage } from '../../shared/components/StatusMessage'
import { useLocalStorage } from '../../shared/hooks/useLocalStorage'
import { useToggle } from '../../shared/hooks/useToggle'
import { ContactCard } from './components/ContactCard'
import { lessons, starterContacts, uiStatusCopy } from './data'
import { useMockApi } from './hooks/useMockApi'
import type { Contact, UiStatus } from './types'

const componentExample = `function ContactCard({ contact }: ContactCardProps) {
  return (
    <article className="contact-card">
      <h4>{contact.name}</h4>
      <p>{contact.email}</p>
    </article>
  )
}`

const folderTree = `src/
  app/
    App.tsx
  features/
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
  main.tsx`

export function ReactLessonsPage() {
  const [activeLesson, setActiveLesson] = useState(lessons[0].id)
  const [count, setCount] = useState(0)
  const [uiStatus, setUiStatus] = useState<UiStatus>('idle')
  const [contacts, setContacts] = useState<Contact[]>(starterContacts)
  const [search, setSearch] = useLocalStorage('fde-react-demo-search', '')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [status, setStatus] = useState<Contact['status']>('Lead')
  const [formError, setFormError] = useState('')
  const helpPanel = useToggle(true)
  const api = useMockApi()

  const filteredContacts = useMemo(() => {
    const query = search.toLowerCase().trim()

    if (!query) {
      return contacts
    }

    return contacts.filter((contact) => {
      return (
        contact.name.toLowerCase().includes(query) ||
        contact.email.toLowerCase().includes(query) ||
        contact.status.toLowerCase().includes(query)
      )
    })
  }, [contacts, search])

  useEffect(() => {
    document.title = `React 002 Demo (${contacts.length} contacts)`
  }, [contacts.length])

  function handleAddContact(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    if (!name.trim() || !email.trim()) {
      setFormError('Name and email are required.')
      return
    }

    const newContact: Contact = {
      id: Date.now(),
      name: name.trim(),
      email: email.trim(),
      status,
    }

    setContacts((currentContacts) => [newContact, ...currentContacts])
    setName('')
    setEmail('')
    setStatus('Lead')
    setFormError('')
  }

  function logForConsole() {
    console.log('FDE React demo log', {
      search,
      contacts: contacts.length,
      uiStatus,
    })
  }

  function writeBrowserStorage() {
    window.localStorage.setItem('fde-last-topic', activeLesson)
    window.sessionStorage.setItem('fde-session-topic', activeLesson)
    document.cookie = `fde_demo_topic=${activeLesson}; path=/; max-age=3600`
  }

  return (
    <main>
      <header className="page-hero">
        <div>
          <span className="eyebrow">FDE Frontend 002</span>
          <h1>React Concepts Demo</h1>
          <p>
            A Vite React TypeScript teaching app covering components, props, state, forms,
            effects, custom hooks, DevTools, folder structure, and API-state flow.
          </p>
        </div>
        <div className="hero-panel">
          <strong>Teaching loop</strong>
          <span>User action -&gt; state change -&gt; re-render -&gt; feedback</span>
        </div>
      </header>

      <nav className="lesson-nav" aria-label="React lesson sections">
        {lessons.map((lesson) => (
          <a
            className={activeLesson === lesson.id ? 'active' : ''}
            href={`#${lesson.id}`}
            key={lesson.id}
            onClick={() => setActiveLesson(lesson.id)}
          >
            <span>{lesson.eyebrow}</span>
            {lesson.title}
          </a>
        ))}
      </nav>

      <Section
        id="mental-model"
        eyebrow="001"
        title="React Mental Model"
        description="React keeps UI understandable by rendering components from state."
      >
        <div className="concept-grid">
          <div className="concept-box">
            <h3>Plain JavaScript</h3>
            <p>Event -&gt; find DOM element -&gt; manually change DOM.</p>
          </div>
          <div className="concept-box">
            <h3>React</h3>
            <p>Event -&gt; update state -&gt; React re-renders UI.</p>
          </div>
          <div className="concept-box">
            <h3>What stays same</h3>
            <p>Browser, DOM, events, APIs, CSS, and user feedback still matter.</p>
          </div>
        </div>
      </Section>

      <Section
        id="jsx-components"
        eyebrow="002"
        title="JSX And Components"
        description="Components are JavaScript functions that return JSX."
      >
        <div className="two-column">
          <div className="component-preview">
            <span>PageHeader</span>
            <span>SearchForm</span>
            <span>ContactCard</span>
            <span>StatusMessage</span>
          </div>
          <CodeBlock>{componentExample}</CodeBlock>
        </div>
      </Section>

      <Section
        id="props"
        eyebrow="003"
        title="Props And Composition"
        description="The parent owns data and passes it into reusable children."
      >
        <div className="contact-grid">
          {starterContacts.slice(0, 2).map((contact) => (
            <ContactCard contact={contact} key={contact.id} />
          ))}
        </div>
        <StatusMessage>Each ContactCard receives one contact prop.</StatusMessage>
      </Section>

      <Section
        id="state-events"
        eyebrow="004"
        title="State, Events, Conditional Rendering"
        description="Use state to remember values and render different UI."
      >
        <div className="demo-row">
          <div className="demo-panel">
            <h3>Counter</h3>
            <p className="counter-value">{count}</p>
            <div className="button-row">
              <button type="button" onClick={() => setCount((value) => value - 1)}>Decrease</button>
              <button type="button" onClick={() => setCount(0)}>Reset</button>
              <button type="button" onClick={() => setCount((value) => value + 1)}>Increase</button>
            </div>
          </div>

          <div className="demo-panel">
            <h3>UI State</h3>
            <div className="button-row wrap">
              {Object.keys(uiStatusCopy).map((statusName) => (
                <button type="button" key={statusName} onClick={() => setUiStatus(statusName as UiStatus)}>
                  {statusName}
                </button>
              ))}
            </div>
            <StatusMessage tone={uiStatus === 'error' ? 'error' : uiStatus === 'success' ? 'success' : 'info'}>
              {`${uiStatusCopy[uiStatus].title}: ${uiStatusCopy[uiStatus].body}`}
            </StatusMessage>
          </div>
        </div>
      </Section>

      <Section
        id="lists-forms"
        eyebrow="005"
        title="Lists, Keys, Forms"
        description="Render arrays with stable keys and control form inputs with state."
      >
        <div className="two-column">
          <form className="contact-form" onSubmit={handleAddContact}>
            <h3>Add Contact</h3>
            <label htmlFor="name">Name</label>
            <input id="name" value={name} onChange={(event) => setName(event.target.value)} />

            <label htmlFor="email">Email</label>
            <input id="email" value={email} onChange={(event) => setEmail(event.target.value)} />

            <label htmlFor="status">Status</label>
            <select id="status" value={status} onChange={(event) => setStatus(event.target.value as Contact['status'])}>
              <option>Lead</option>
              <option>Customer</option>
              <option>Follow-up</option>
            </select>

            <button type="submit">Add Contact</button>
            {formError && <StatusMessage tone="error">{formError}</StatusMessage>}
          </form>

          <div>
            <label htmlFor="search">Search contacts</label>
            <input
              id="search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Search name, email, or status"
            />
            <div className="contact-list">
              {filteredContacts.length === 0 ? (
                <StatusMessage tone="warning">No contacts match this search.</StatusMessage>
              ) : (
                filteredContacts.map((contact) => <ContactCard contact={contact} key={contact.id} />)
              )}
            </div>
          </div>
        </div>
      </Section>

      <Section
        id="effects-api"
        eyebrow="006"
        title="Effects And API State"
        description="useEffect syncs with outside systems; API state tracks loading, success, and error."
      >
        <div className="demo-row">
          <div className="demo-panel">
            <h3>useEffect</h3>
            <p>The browser tab title updates whenever contact count changes.</p>
            <StatusMessage>{`Current contacts: ${contacts.length}`}</StatusMessage>
          </div>
          <div className="demo-panel">
            <h3>Mock API</h3>
            <div className="button-row wrap">
              <button type="button" onClick={api.loadSuccess}>Fetch success</button>
              <button type="button" onClick={api.loadFailure}>Fetch failure</button>
              <button type="button" onClick={api.reset}>Reset</button>
            </div>
            {api.loading && <StatusMessage>Loading mock API...</StatusMessage>}
            {api.error && <StatusMessage tone="error">{api.error}</StatusMessage>}
            {api.data && (
              <div className="api-result">
                <strong>{api.data.source}</strong>
                <p>{api.data.message}</p>
                <ul>
                  {api.data.items.map((item) => <li key={item.id}>{item.label}</li>)}
                </ul>
              </div>
            )}
          </div>
        </div>
      </Section>

      <Section
        id="custom-hooks"
        eyebrow="007"
        title="Custom Hooks"
        description="Extract reusable stateful logic into useSomething functions."
      >
        <div className="demo-row">
          <div className="demo-panel">
            <h3>useToggle</h3>
            <button type="button" onClick={helpPanel.toggle}>
              {helpPanel.value ? 'Hide' : 'Show'} hook explanation
            </button>
            {helpPanel.value && (
              <StatusMessage>useToggle owns boolean state and exposes a small API to the component.</StatusMessage>
            )}
          </div>
          <div className="demo-panel">
            <h3>useLocalStorage</h3>
            <p>The search input uses a custom hook and persists in Local Storage.</p>
            <StatusMessage>{`Stored search: ${search || 'empty'}`}</StatusMessage>
          </div>
        </div>
      </Section>

      <Section
        id="devtools"
        eyebrow="008"
        title="Browser Developer Tools"
        description="Use Console, Network, Application, storage, cookies, and React DevTools to debug."
      >
        <div className="demo-row">
          <div className="demo-panel">
            <h3>Console</h3>
            <button type="button" onClick={logForConsole}>Log demo state</button>
            <p>Open Inspect -&gt; Console and click the button.</p>
          </div>
          <div className="demo-panel">
            <h3>Application Storage</h3>
            <button type="button" onClick={writeBrowserStorage}>Write storage and cookie</button>
            <p>Open Inspect -&gt; Application to inspect Local Storage, Session Storage, and Cookies.</p>
          </div>
          <div className="demo-panel">
            <h3>Network</h3>
            <p>Use the Mock API buttons above, then inspect `/mock-api.json` and `/missing-api.json` in Network.</p>
          </div>
        </div>
      </Section>

      <Section
        id="folder-structure"
        eyebrow="010"
        title="Vite, TypeScript, Folder Structure"
        description="A practical structure for a Vite React TypeScript frontend."
      >
        <div className="two-column">
          <CodeBlock>{folderTree}</CodeBlock>
          <div className="concept-grid single">
            <div className="concept-box"><h3>Vite</h3><p>Development server, fast reload, and production build.</p></div>
            <div className="concept-box"><h3>TypeScript</h3><p>Types for props, state, API responses, and shared models.</p></div>
            <div className="concept-box"><h3>Feature folders</h3><p>Keep related UI, hooks, types, and data near the feature that changes.</p></div>
          </div>
        </div>
      </Section>

      <Section
        id="final-activity"
        eyebrow="009"
        title="Final React API Activity"
        description="Candidates build their own API Ninjas React frontend with AI-assisted planning."
      >
        <div className="activity-checklist">
          {[
            'Ask AI for a plan before code.',
            'Use Vite React TypeScript.',
            'Create at least four components.',
            'Use props and useState.',
            'Use controlled input if the API needs a query.',
            'Extract API logic into a custom hook.',
            'Show loading, error, empty, and success states.',
            'Inspect successful and failed requests in Network.',
            'Write README and DevTools debug report.',
          ].map((item) => (
            <label key={item}>
              <input type="checkbox" />
              <span>{item}</span>
            </label>
          ))}
        </div>
      </Section>
    </main>
  )
}
