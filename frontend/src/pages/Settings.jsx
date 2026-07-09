import { useNavigate } from "react-router-dom";
import "../styles/Settings.css";

function Settings() {

  const navigate = useNavigate();

  const handleLogout = () => {

    localStorage.removeItem("token");

    alert("Logged Out Successfully");

    navigate("/");
  };

  return (
    <div className="settings-page">

      <h1>Settings</h1>

      <div className="settings-card">

        <h2>Application Settings</h2>

        <button>
          Dark Mode
        </button>

        <button>
          Notifications
        </button>

        <button onClick={handleLogout}>
          Logout
        </button>

      </div>

    </div>
  );
}

export default Settings;