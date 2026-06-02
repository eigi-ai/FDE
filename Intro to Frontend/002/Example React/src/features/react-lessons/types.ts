export type LessonId =
  | 'mental-model'
  | 'jsx-components'
  | 'props'
  | 'state-events'
  | 'lists-forms'
  | 'effects-api'
  | 'custom-hooks'
  | 'devtools'
  | 'folder-structure'
  | 'final-activity'

export type Lesson = {
  id: LessonId
  title: string
  eyebrow: string
  summary: string
}

export type Contact = {
  id: number
  name: string
  email: string
  status: 'Lead' | 'Customer' | 'Follow-up'
}

export type UiStatus = 'idle' | 'loading' | 'success' | 'error' | 'empty'

export type MockApiResponse = {
  source: string
  message: string
  items: Array<{
    id: number
    label: string
  }>
}
