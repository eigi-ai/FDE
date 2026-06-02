import { useCallback, useEffect, useState } from 'react'
import { CodeBlock } from '../../shared/components/CodeBlock'
import { Section } from '../../shared/components/Section'
import { StatusMessage } from '../../shared/components/StatusMessage'
import { AUTH_STORAGE_KEY } from '../auth/authContext'
import type { MockApiResponse } from '../react-lessons/types'

const routerCode = `<BrowserRouter>
  <Routes>
    <Route path="/login" element={<LoginPage />} />
    <Route element={<RequireAuth><AppShell /></RequireAuth>}>
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route path="/api" element={<ApiLabPage />} />
      <Route path="/devtools" element={<DevToolsPage />} />
    </Route>
  </Routes>
</BrowserRouter>`

const folderTree = `src/
  app/
    App.tsx                 # router setup
  features/
    auth/
      authContext.ts        # auth types + storage key
      AuthProvider.tsx      # mock login + localStorage
      LoginPage.tsx
      useAuth.ts
    dashboard/
      components/
        MetricCard.tsx      # reusable component
      DashboardPage.tsx     # main dashboard + hooks
    api-lab/
      ApiLabPage.tsx        # axios + fetch
    devtools/
      DevToolsPage.tsx      # console/network/storage demos
    react-lessons/
      ReactLessonsPage.tsx  # full older lesson page
  shared/
    components/
      AppShell.tsx
      RequireAuth.tsx
      CodeBlock.tsx
      Section.tsx
      StatusMessage.tsx
    hooks/
      useLocalStorage.ts
      useToggle.ts
  styles/
    global.css
  main.tsx`

const devtoolsCode = `function writeBrowserStorage() {
  localStorage.setItem("fde-devtools-local", JSON.stringify(payload))
  sessionStorage.setItem("fde-devtools-session", "open")
  document.cookie = "fde_devtools_cookie=stored; path=/; max-age=3600"
}

async function runNetworkRequest() {
  const response = await fetch("/mock-api.json")
  const data = await response.json()
  console.log(data)
}`

export function DevToolsPage() {
  const [storageStatus, setStorageStatus] = useState('')
  const [networkStatus, setNetworkStatus] = useState('')

  useEffect(() => {
    document.title = 'DevTools | FDE React Demo'
  }, [])

  const logDemoState = useCallback(() => {
    console.group('FDE React DevTools demo')
    console.info('Use this log to show Console output.')
    console.table([
      { key: AUTH_STORAGE_KEY, location: 'Local Storage', purpose: 'Mock logged-in user' },
      { key: 'fde-devtools-local', location: 'Local Storage', purpose: 'Manual storage demo' },
      { key: 'fde-devtools-session', location: 'Session Storage', purpose: 'Tab-scoped storage demo' },
    ])
    console.groupEnd()
  }, [])

  const writeBrowserStorage = useCallback(() => {
    const payload = {
      savedAt: new Date().toISOString(),
      topic: 'Developer Tools',
      status: 'stored from React button',
    }

    window.localStorage.setItem('fde-devtools-local', JSON.stringify(payload))
    window.sessionStorage.setItem('fde-devtools-session', 'visible until this tab closes')
    document.cookie = 'fde_devtools_cookie=stored; path=/; max-age=3600'
    setStorageStatus('Local Storage, Session Storage, and cookie were written.')
  }, [])

  const clearBrowserStorage = useCallback(() => {
    window.localStorage.removeItem('fde-devtools-local')
    window.sessionStorage.removeItem('fde-devtools-session')
    document.cookie = 'fde_devtools_cookie=; path=/; max-age=0'
    setStorageStatus('Demo storage keys were cleared. Login storage was kept.')
  }, [])

  const runNetworkRequest = useCallback(async () => {
    setNetworkStatus('Loading /mock-api.json...')

    try {
      const response = await fetch('/mock-api.json')

      if (!response.ok) {
        throw new Error(`Request failed with ${response.status}`)
      }

      const data = (await response.json()) as MockApiResponse
      console.log('Network demo response', data)
      setNetworkStatus(`Loaded ${data.items.length} items from /mock-api.json.`)
    } catch (error) {
      setNetworkStatus(error instanceof Error ? error.message : 'Network request failed.')
    }
  }, [])

  return (
    <>
      <header className="page-hero">
        <div>
          <span className="eyebrow">Developer Tools</span>
          <h1>Debug The React App</h1>
          <p>
            This page creates real Console, Network, Application, storage, and cookie
            signals for a live browser debugging walkthrough.
          </p>
        </div>
        <div className="hero-panel">
          <strong>Browser Panels</strong>
          <span>Console, Network, Application, Elements, React Components</span>
        </div>
      </header>

      <Section
        id="devtools-actions"
        eyebrow="001"
        title="DevTools Actions"
        description="Click these buttons, then inspect the matching browser panel."
      >
        <div className="demo-row">
          <div className="demo-panel">
            <h3>Console</h3>
            <button type="button" onClick={logDemoState}>Log Demo State</button>
            <StatusMessage>Open Console to see console.group, console.info, and console.table output.</StatusMessage>
          </div>

          <div className="demo-panel">
            <h3>Network</h3>
            <button type="button" onClick={runNetworkRequest}>Request Mock API</button>
            {networkStatus && <StatusMessage>{networkStatus}</StatusMessage>}
          </div>

          <div className="demo-panel">
            <h3>Application</h3>
            <div className="button-row wrap">
              <button type="button" onClick={writeBrowserStorage}>Write Storage</button>
              <button type="button" onClick={clearBrowserStorage}>Clear Demo Storage</button>
            </div>
            {storageStatus && <StatusMessage>{storageStatus}</StatusMessage>}
          </div>
        </div>
      </Section>

      <Section
        id="routing"
        eyebrow="002"
        title="Routing"
        description="React Router maps URLs to pages, and RequireAuth redirects logged-out users to /login."
      >
        <CodeBlock>{routerCode}</CodeBlock>
      </Section>

      <Section
        id="devtools-code"
        eyebrow="003"
        title="DevTools Code"
        description="The buttons above call browser APIs that can be inspected from DevTools."
      >
        <CodeBlock>{devtoolsCode}</CodeBlock>
      </Section>

      <Section
        id="folder-structure"
        eyebrow="004"
        title="Folder Structure"
        description="The project is split by app wiring, feature pages, shared components, shared hooks, and global styles."
      >
        <CodeBlock>{folderTree}</CodeBlock>
      </Section>
    </>
  )
}
