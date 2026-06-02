import { NavLink, Outlet } from 'react-router-dom'
import { useAuth } from '../../features/auth/useAuth'

const navItems = [
  { to: '/dashboard', label: 'Dashboard' },
  { to: '/api', label: 'API Lab' },
  { to: '/devtools', label: 'DevTools' },
  { to: '/lessons', label: 'Full Lessons' },
]

export function AppShell() {
  const { logout, user } = useAuth()

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div>
          <span className="eyebrow">FDE Frontend 002</span>
          <h2>React Example</h2>
          <p>Routing, login, hooks, API calls, DevTools, and folder structure.</p>
        </div>

        <nav className="app-nav" aria-label="Main pages">
          {navItems.map((item) => (
            <NavLink className={({ isActive }) => (isActive ? 'active' : '')} to={item.to} key={item.to}>
              {item.label}
            </NavLink>
          ))}
        </nav>

        <div className="user-panel">
          <strong>{user?.name}</strong>
          <span>{user?.email}</span>
          <button type="button" onClick={logout}>Logout</button>
        </div>
      </aside>

      <main className="app-main">
        <Outlet />
      </main>
    </div>
  )
}
