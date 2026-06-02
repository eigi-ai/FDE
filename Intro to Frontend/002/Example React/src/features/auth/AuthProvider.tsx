import { useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import {
  AUTH_STORAGE_KEY,
  AuthContext,
  getNameFromEmail,
  readStoredUser,
} from './authContext'
import type { AuthContextValue, DemoUser } from './authContext'

type AuthProviderProps = {
  children: ReactNode
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] = useState<DemoUser | null>(() => readStoredUser())

  const value = useMemo<AuthContextValue>(() => {
    function login(email: string, password: string) {
      if (!email.trim() || !password.trim()) {
        throw new Error('Email and password are required.')
      }

      const nextUser: DemoUser = {
        email: email.trim(),
        name: getNameFromEmail(email.trim()) || 'FDE Learner',
        role: email.includes('trainer') ? 'Trainer' : 'Candidate',
      }

      window.localStorage.setItem(AUTH_STORAGE_KEY, JSON.stringify(nextUser))
      setUser(nextUser)
      return nextUser
    }

    function logout() {
      window.localStorage.removeItem(AUTH_STORAGE_KEY)
      setUser(null)
    }

    return { user, login, logout }
  }, [user])

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}
