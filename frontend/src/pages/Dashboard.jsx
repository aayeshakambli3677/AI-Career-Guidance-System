import "../styles/dashboard.css";

function Dashboard() {
  return (
    <div className="dashboard-container">

      <div className="sidebar">
        <h2>CareerGPT</h2>

        <ul>
          <li>Career Advice</li>
          <li>Roadmap</li>
          <li>Interview</li>
          <li>Resume</li>
        </ul>
      </div>

      <div className="main-content">
        <h1>Dashboard</h1>

        <div className="card">
          Welcome User
        </div>
      </div>

    </div>
  );
}

export default Dashboard;