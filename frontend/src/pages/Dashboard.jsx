import "../styles/Dashboard.css";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import StatsCard from "../components/StatsCard";
import { getDashboardData } from "../services/Dashboard_service";

function Dashboard() {

  const navigate = useNavigate();

  const [dashboard, setDashboard] = useState({
    resumeScore: 0,
    mockInterviews: 0,
    skillsLearned: 0,
    overallProgress: 0
  });


  useEffect(() => {

    const fetchDashboard = async () => {
      try {

        const data = await getDashboardData();
        setDashboard(data);

      } catch (error) {
        console.log("Dashboard Error:", error);
      }
    };


    fetchDashboard();

  }, []);



  return (
    <div className="dashboard-page">

      <h1>Welcome to CareerGPT Dashboard</h1>

      <p>
        Get personalized career guidance and improve your skills.
      </p>


      <div className="stats-container">


        <StatsCard
          icon="📄"
          title="Resume Score"
          value={`${dashboard.resumeScore}%`}
        />


        <StatsCard
          icon="🎤"
          title="Mock Interviews"
          value={dashboard.mockInterviews}
        />


        <StatsCard
          icon="💡"
          title="Skills Learned"
          value={dashboard.skillsLearned}
        />


        <StatsCard
          icon="📈"
          title="Overall Progress"
          value={`${dashboard.overallProgress}%`}
        />


      </div>



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