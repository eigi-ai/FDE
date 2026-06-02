import { createContext } from 'react'

export const AUTH_STORAGE_KEY = 'fde-react-demo-user'

export type DemoUser = {
  email: string
  name: string
  role: 'Trainer' | 'Candidate'
}

export type AuthContextValue = {
  user: DemoUser | null
  login: (email: string, password: string) => DemoUser
  logout: () => void
}

export const AuthContext = createContext<AuthContextValue | null>(null)

export function readStoredUser() {
  const storedUser = window.localStorage.getItem(AUTH_STORAGE_KEY)

  if (!storedUser) {
    return null
  }

  try {
    return JSON.parse(storedUser) as DemoUser
  } catch {
    window.localStorage.removeItem(AUTH_STORAGE_KEY)
    return null
  }
}

export function getNameFromEmail(email: string) {
  const [localPart] = email.split('@')
  return localPart
    .split(/[._-]/)
    .filter(Boolean)
    .map((part) => part[0].toUpperCase() + part.slice(1))
    .join(' ')
}
