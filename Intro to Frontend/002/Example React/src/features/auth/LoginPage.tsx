import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'
import { Navigate, useLocation, useNavigate } from 'react-router-dom'
import { CodeBlock } from '../../shared/components/CodeBlock'
import { StatusMessage } from '../../shared/components/StatusMessage'
import { AUTH_STORAGE_KEY } from './authContext'
import { useAuth } from './useAuth'

const loginCode = `function login(email: string, password: string) {
  const user = { email, name: "Demo User", role: "Candidate" }

  localStorage.setItem("fde-react-demo-user", JSON.stringify(user))
  setUser(user)
}`

type LocationState = {
  from?: {
    pathname: string
  }
}

export function LoginPage() {
  const [email, setEmail] = useState('candidate@fde.dev')
  const [password, setPassword] = useState('password')
  const [error, setError] = useState('')
  const { login, user } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const locationState = location.state as LocationState | null
  const redirectPath = locationState?.from?.pathname ?? '/dashboard'

  useEffect(() => {
    document.title = 'Login | FDE React Demo'
  }, [])

  if (user) {
    return <Navigate to="/dashboard" replace />
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    try {
      login(email, password)
      navigate(redirectPath, { replace: true })
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : 'Login failed.')
    }
  }

  return (
    <main className="login-page">
      <section className="login-panel">
        <div>
          <span className="eyebrow">Mock Login</span>
          <h1>FDE React Demo</h1>
          <p>
            Submit the form to create a mock user and persist it in browser Local Storage.
            Any non-empty password works.
          </p>
        </div>

        <form className="contact-form" onSubmit={handleSubmit}>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />

          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />

          <button type="submit">Login</button>
          {error && <StatusMessage tone="error">{error}</StatusMessage>}
        </form>

        <div className="split-panel">
          <div className="concept-box">
            <h3>Local Storage Key</h3>
            <p>{AUTH_STORAGE_KEY}</p>
          </div>
          <CodeBlock>{loginCode}</CodeBlock>
        </div>
      </section>
    </main>
  )
}
