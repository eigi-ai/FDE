import { useState } from 'react'

export function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue)

  function toggle() {
    setValue((currentValue) => !currentValue)
  }

  return { value, setValue, toggle }
}
