import { BrowserRouter, Routes, Route } from "react-router-dom";

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
import IntershipRecommendation from "./pages/InternshipRecommendation";
import Notfound from "./pages/Notfound";
import Register from "./pages/Register";
import ResumeUpload from "./pages/ResumeUpload";
import SkillGapAnalysis from "./pages/SkillGapAnalysis";
import Resume from "./pages/Resume";
import Settings from "./pages/Settings";
import EditProfile from "./pages/EditProfile";
import InternshipRecommendation from "./pages/InternshipRecommendation";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* Pages with Sidebar */}
        <Route element={<MainLayout />}>

          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/career" element={<Career />} />
          <Route path="/resume" element={<ResumeAnalysis />} />
          <Route path="/interviewPreparation" element={<InterviewPreparation />} />
          <Route path="/roadmap" element={<Roadmap />} />
          
          <Route path="/resumeUpload" element={<ResumeUpload />} />
          <Route path="/resume-analysis" element={<ResumeAnalysis />} />
          <Route
  path="/internships"
  element={<InternshipRecommendation />}
/>
          <Route
            path="/skills"
            element={<SkillGapAnalysis />}
          />
          <Route
            path="/interviewPreparation"
            element={<InterviewPreparation />}
          />
          <Route
            path="/settings"
            element={<Settings />}
          />

          <Route
  path="/edit-profile"
  element={<EditProfile />}
/>

        </Route>


        {/* Login/Register pages */}
        <Route element={<AuthLayout />}>

          <Route path="/" element={<Login />} />
          <Route path="/register" element={<Register />} />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;