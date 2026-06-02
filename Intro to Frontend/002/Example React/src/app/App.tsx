import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { ApiLabPage } from "../features/api-lab/ApiLabPage";
import { AuthProvider } from "../features/auth/AuthProvider";
import { LoginPage } from "../features/auth/LoginPage";
import { DashboardPage } from "../features/dashboard/DashboardPage";
import { DevToolsPage } from "../features/devtools/DevToolsPage";
import { ReactLessonsPage } from "../features/react-lessons/ReactLessonsPage";
import { AppShell } from "../shared/components/AppShell";
import { RequireAuth } from "../shared/components/RequireAuth";

export function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route
            element={
              <RequireAuth>
                <AppShell />
              </RequireAuth>
            }
          >
            <Route index element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/api" element={<ApiLabPage />} />
            <Route path="/devtools" element={<DevToolsPage />} />
            <Route path="/lessons" element={<ReactLessonsPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
