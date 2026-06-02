type StatusMessageProps = {
  tone?: 'info' | 'success' | 'error' | 'warning'
  children: string
}

export function StatusMessage({ tone = 'info', children }: StatusMessageProps) {
  return (
    <p className={`status-message status-message--${tone}`} role={tone === 'error' ? 'alert' : 'status'}>
      {children}
    </p>
  )
}
