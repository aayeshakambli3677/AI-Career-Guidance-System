import "../styles/Dashboard.css";
import { useNavigate } from "react-router-dom";
import StatsCard from "../components/StatsCard";

function Dashboard() {

  const navigate = useNavigate();

  return (
    <div className="dashboard-page">

      <h1>Welcome to CareerGPT Dashboard</h1>

      <p>
        Get personalized career guidance and improve your skills.
      </p>

      {/* Dashboard Statistics */}
      <div className="stats-container">

        <StatsCard
          icon="📄"
          title="Resume Score"
          value="85%"
        />

        <StatsCard
          icon="🎤"
          title="Mock Interviews"
          value="12"
        />

        <StatsCard
          icon="💡"
          title="Skills Learned"
          value="18"
        />

        <StatsCard
          icon="📈"
          title="Overall Progress"
          value="65%"
        />

      </div>

      {/* Dashboard Cards */}
      <div className="dashboard-cards">

        <div
          className="dashboard-card"
          onClick={() => navigate("/career")}
        >
          <h2>Career Recommendation</h2>
          <p>
            Explore career paths based on your skills and interests.
          </p>
        </div>

        <div
          className="dashboard-card"
          onClick={() => navigate("/resume")}
        >
          <h2>Resume Analysis</h2>
          <p>
            Upload and analyze your resume.
          </p>
        </div>

        <div
          className="dashboard-card"
          onClick={() => navigate("/interviewPreparation")}
        >
          <h2>Interview Preparation</h2>
          <p>
            Practice interview questions.
          </p>
        </div>

        <div
          className="dashboard-card"
          onClick={() => navigate("/roadmap")}
        >
          <h2>Skill Roadmap</h2>
          <p>
            Follow a personalized roadmap.
          </p>
        </div>

      </div>

    </div>
  );
}

export default Dashboard;