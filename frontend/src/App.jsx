import MainLayout from "./layouts/MainLayout";
import AuthLayout from "./layouts/AuthLayout";

import Dashboard from "./pages/Dashboard";
import Profile from "./pages/Profile";
import Career from "./pages/Career";
import ResumeAnalysis from "./pages/ResumeAnalysis";
import InterviewPreparation from "./pages/InterviewPreparation";
import Roadmap from "./pages/Roadmap";
import Login from "./pages/Login";
import CareerReCommendation from "./pages/careerRecommendation";
import Notfound from "./pages/Notfound";
import Register from "./pages/Register";
import ResumeUpload from "./pages/ResumeUpload";
import SkillGapAnalysis from "./pages/SkillGapAnalysis";
import Resume from "./pages/Resume";
import Settings from "./pages/Settings";
import EditProfile from "./pages/EditProfile";
import InternshipRecommendation from "./pages/InternshipRecommendation";
import ProgressTracker from "./pages/ProgressTracker";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

const ProtectedRoute = ({ children }) => {

  const token = localStorage.getItem("token");

  return token
    ? children
    : <Navigate to="/" />;
};
function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* Pages with Sidebar */}
        <Route element={<MainLayout />}>

          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/profile"
            element={
              <ProtectedRoute>
                <Profile />
              </ProtectedRoute>
            }
          />

          <Route
            path="/career"
            element={
              <ProtectedRoute>
                <Career />
              </ProtectedRoute>
            }
          />

          <Route
            path="/resume"
            element={
              <ProtectedRoute>
                <ResumeAnalysis />
              </ProtectedRoute>
            }
          />

          <Route
            path="/interviewPreparation"
            element={
              <ProtectedRoute>
                <InterviewPreparation />
              </ProtectedRoute>
            }
          />

          <Route
            path="/roadmap"
            element={
              <ProtectedRoute>
                <Roadmap />
              </ProtectedRoute>
            }
          />

          <Route
            path="/progress"
            element={
              <ProtectedRoute>
                <ProgressTracker />
              </ProtectedRoute>
            }
          />

          <Route
            path="/resumeUpload"
            element={
              <ProtectedRoute>
                <ResumeUpload />
              </ProtectedRoute>
            }
          />

          <Route
            path="/resume-analysis"
            element={
              <ProtectedRoute>
                <ResumeAnalysis />
              </ProtectedRoute>
            }
          />

          <Route
            path="/internships"
            element={
              <ProtectedRoute>
                <InternshipRecommendation />
              </ProtectedRoute>
            }
          />

          <Route
            path="/skills"
            element={
              <ProtectedRoute>
                <SkillGapAnalysis />
              </ProtectedRoute>
            }
          />

          <Route
            path="/settings"
            element={
              <ProtectedRoute>
                <Settings />
              </ProtectedRoute>
            }
          />

          <Route
            path="/edit-profile"
            element={
              <ProtectedRoute>
                <EditProfile />
              </ProtectedRoute>
            }
          />

        </Route>


        {/* Login/Register pages */}
        <Route element={<AuthLayout />}>

          <Route
            path="/"
            element={
              localStorage.getItem("token")
                ? <Navigate to="/dashboard" />
                : <Login />
            }
          />
          <Route path="/register" element={<Register />} />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;