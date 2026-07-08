import "../styles/Dashboard.css";
function Dashboard() {
  return (
    <div className="dashboard-page">

      <h1>Welcome to CareerGPT Dashboard</h1>

      <p>
        Get personalized career guidance and improve your skills.
      </p>

      <div className="dashboard-cards">

        <div className="dashboard-card">
          <h2>Career Recommendation</h2>
          <p>
            Explore career paths based on your skills and interests.
          </p>
        </div>

        <div className="dashboard-card">
          <h2>Resume Analysis</h2>
          <p>
            Upload and analyze your resume to improve it.
          </p>
        </div>

        <div className="dashboard-card">
          <h2>Interview Preparation</h2>
          <p>
            Practice interview questions and improve confidence.
          </p>
        </div>

        <div className="dashboard-card">
          <h2>Skill Roadmap</h2>
          <p>
            Follow a personalized learning roadmap.
          </p>
        </div>

      </div>

    </div>
  );
}

export default Dashboard;