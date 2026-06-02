import { useState } from 'react'
import type { MockApiResponse } from '../types'

type ApiState = {
  data: MockApiResponse | null
  loading: boolean
  error: string
}

export function useMockApi() {
  const [state, setState] = useState<ApiState>({ data: null, loading: false, error: '' })

  async function loadSuccess() {
    setState({ data: null, loading: true, error: '' })

    try {
      const response = await fetch('/mock-api.json')

      if (!response.ok) {
        throw new Error(`Request failed with ${response.status}`)
      }

      const data = (await response.json()) as MockApiResponse
      setState({ data, loading: false, error: '' })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Unknown error'
      setState({ data: null, loading: false, error: message })
    }
  }

  async function loadFailure() {
    setState({ data: null, loading: true, error: '' })

    try {
      const response = await fetch('/missing-api.json')

      if (!response.ok) {
        throw new Error(`Request failed with ${response.status}`)
      }

      const data = (await response.json()) as MockApiResponse
      setState({ data, loading: false, error: '' })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Unknown error'
      setState({ data: null, loading: false, error: message })
    }
  }

  function reset() {
    setState({ data: null, loading: false, error: '' })
  }

  return { ...state, loadSuccess, loadFailure, reset }
}
