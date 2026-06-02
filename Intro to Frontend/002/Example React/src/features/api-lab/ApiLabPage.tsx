import axios from 'axios'
import { useCallback, useEffect, useState } from 'react'
import { CodeBlock } from '../../shared/components/CodeBlock'
import { Section } from '../../shared/components/Section'
import { StatusMessage } from '../../shared/components/StatusMessage'
import type { MockApiResponse } from '../react-lessons/types'

type ApiMethod = 'axios' | 'fetch'

type ApiState = {
  data: MockApiResponse | null
  error: string
  loading: boolean
  method: ApiMethod | null
}

const emptyApiState: ApiState = {
  data: null,
  error: '',
  loading: false,
  method: null,
}

const fetchCode = `async function loadWithFetch() {
  const response = await fetch("/mock-api.json")

  if (!response.ok) {
    throw new Error(\`Request failed with \${response.status}\`)
  }

  const data = await response.json()
  setData(data)
}`

const axiosCode = `async function loadWithAxios() {
  const response = await axios.get<MockApiResponse>("/mock-api.json")

  setData(response.data)
}`

const apiHookCode = `const [apiState, setApiState] = useState({
  data: null,
  loading: false,
  error: "",
})

const loadWithAxios = useCallback(async () => {
  setApiState({ data: null, loading: true, error: "" })

  try {
    const response = await axios.get("/mock-api.json")
    setApiState({ data: response.data, loading: false, error: "" })
  } catch (error) {
    setApiState({ data: null, loading: false, error: "Request failed" })
  }
}, [])`

function getAxiosErrorMessage(error: unknown) {
  if (axios.isAxiosError(error)) {
    return `Axios request failed with ${error.response?.status ?? 'unknown status'}`
  }

  return error instanceof Error ? error.message : 'Unknown Axios error'
}

function isMockApiResponse(data: unknown): data is MockApiResponse {
  if (!data || typeof data !== 'object') {
    return false
  }

  const maybeResponse = data as { items?: unknown; message?: unknown; source?: unknown }

  return (
    typeof maybeResponse.source === 'string' &&
    typeof maybeResponse.message === 'string' &&
    Array.isArray(maybeResponse.items)
  )
}

export function ApiLabPage() {
  const [apiState, setApiState] = useState<ApiState>(emptyApiState)

  useEffect(() => {
    document.title = 'API Lab | FDE React Demo'
  }, [])

  const loadWithAxios = useCallback(async () => {
    setApiState({ data: null, loading: true, error: '', method: 'axios' })

    try {
      const response = await axios.get<unknown>('/mock-api.json')
      console.log('Axios response object', response)

      if (!isMockApiResponse(response.data)) {
        throw new Error('Axios received data in an unexpected shape.')
      }

      setApiState({ data: response.data, loading: false, error: '', method: 'axios' })
    } catch (error) {
      setApiState({ data: null, loading: false, error: getAxiosErrorMessage(error), method: 'axios' })
    }
  }, [])

  const loadWithFetch = useCallback(async () => {
    setApiState({ data: null, loading: true, error: '', method: 'fetch' })

    try {
      const response = await fetch('/mock-api.json')
      console.log('Fetch response object', response)

      if (!response.ok) {
        throw new Error(`Fetch request failed with ${response.status}`)
      }

      const data = (await response.json()) as MockApiResponse
      if (!isMockApiResponse(data)) {
        throw new Error('Fetch received data in an unexpected shape.')
      }

      setApiState({ data, loading: false, error: '', method: 'fetch' })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Unknown Fetch error'
      setApiState({ data: null, loading: false, error: message, method: 'fetch' })
    }
  }, [])

  const triggerAxiosError = useCallback(async () => {
    setApiState({ data: null, loading: true, error: '', method: 'axios' })

    try {
      const response = await axios.get<unknown>('/missing-api.json')
      if (!isMockApiResponse(response.data)) {
        throw new Error('Bad endpoint returned HTML instead of mock API JSON.')
      }

      setApiState({ data: response.data, loading: false, error: '', method: 'axios' })
    } catch (error) {
      setApiState({ data: null, loading: false, error: getAxiosErrorMessage(error), method: 'axios' })
    }
  }, [])

  return (
    <>
      <header className="page-hero">
        <div>
          <span className="eyebrow">API Calling</span>
          <h1>Axios And Fetch In React</h1>
          <p>
            Use this page to compare native Fetch with Axios while watching the same
            request in the browser Network panel.
          </p>
        </div>
        <div className="hero-panel">
          <strong>Endpoint</strong>
          <span>/mock-api.json</span>
        </div>
      </header>

      <Section
        id="api-actions"
        eyebrow="001"
        title="Run API Calls"
        description="Both buttons request the same local JSON file, then store loading, error, and success state in React."
      >
        <div className="demo-row">
          <div className="demo-panel">
            <h3>Request Controls</h3>
            <div className="button-row wrap">
              <button type="button" onClick={loadWithAxios}>Load With Axios</button>
              <button type="button" onClick={loadWithFetch}>Load With Fetch</button>
              <button type="button" onClick={triggerAxiosError}>Trigger Bad Endpoint</button>
              <button type="button" onClick={() => setApiState(emptyApiState)}>Reset</button>
            </div>
            {apiState.method && <StatusMessage>{`Last method: ${apiState.method}`}</StatusMessage>}
            {apiState.loading && <StatusMessage>Loading API response...</StatusMessage>}
            {apiState.error && <StatusMessage tone="error">{apiState.error}</StatusMessage>}
          </div>

          <div className="api-result">
            <h3>Response State</h3>
            {apiState.data ? (
              <>
                <strong>{apiState.data.source}</strong>
                <p>{apiState.data.message}</p>
                <ul>
                  {apiState.data.items.map((item) => <li key={item.id}>{item.label}</li>)}
                </ul>
              </>
            ) : (
              <StatusMessage tone="warning">No response loaded yet.</StatusMessage>
            )}
          </div>
        </div>
      </Section>

      <Section
        id="axios-fetch-difference"
        eyebrow="002"
        title="Axios Vs Fetch"
        description="Fetch is built into the browser; Axios is an installed library with helper behavior around JSON, errors, and configuration."
      >
        <div className="comparison-table" role="table" aria-label="Axios and Fetch differences">
          <div role="row">
            <strong role="columnheader">Topic</strong>
            <strong role="columnheader">Fetch</strong>
            <strong role="columnheader">Axios</strong>
          </div>
          <div role="row">
            <span>Install</span>
            <span>Built into the browser.</span>
            <span>Install with npm and import it.</span>
          </div>
          <div role="row">
            <span>JSON</span>
            <span>Call response.json() yourself.</span>
            <span>JSON response is available as response.data.</span>
          </div>
          <div role="row">
            <span>Errors</span>
            <span>Check response.ok for non-2xx statuses.</span>
            <span>Throws automatically for non-2xx statuses.</span>
          </div>
          <div role="row">
            <span>Best Use</span>
            <span>Simple browser requests.</span>
            <span>Apps that benefit from base URLs, interceptors, and shared config.</span>
          </div>
        </div>
      </Section>

      <Section
        id="api-code"
        eyebrow="003"
        title="React Code Examples"
        description="The examples show how to use both clients inside React event handlers or custom hooks."
      >
        <div className="two-column">
          <div>
            <h3>Fetch</h3>
            <CodeBlock>{fetchCode}</CodeBlock>
          </div>
          <div>
            <h3>Axios</h3>
            <CodeBlock>{axiosCode}</CodeBlock>
          </div>
        </div>
        <div className="code-section">
          <h3>With useState And useCallback</h3>
          <CodeBlock>{apiHookCode}</CodeBlock>
        </div>
      </Section>
    </>
  )
}
