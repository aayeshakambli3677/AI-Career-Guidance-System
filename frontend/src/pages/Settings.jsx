import { useNavigate } from "react-router-dom";
import "../styles/Settings.css";
import { useState, useEffect } from "react";

function Settings() {

  const navigate = useNavigate();

  const [darkMode, setDarkMode] = useState(
    localStorage.getItem("darkMode") === "true"
  );

  const [notifications, setNotifications] = useState(
    localStorage.getItem("notifications") !== "false"
  );

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add("dark-mode");
    } else {
      document.body.classList.remove("dark-mode");
    }

    localStorage.setItem("darkMode", darkMode);
  }, [darkMode]);

  useEffect(() => {
    localStorage.setItem("notifications", notifications);
  }, [notifications]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const toggleNotifications = () => {
    setNotifications(!notifications);
  };

  const handleLogout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("profile");

    navigate("/");
  };

  return (
    <div className="settings-page">

      <h1>Settings</h1>

      <div className="settings-card">

        <h2>Application Settings</h2>

        <button onClick={toggleDarkMode}>
          {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
        </button>

        <button onClick={toggleNotifications}>
          {notifications
            ? "🔔 Notifications ON"
            : "🔕 Notifications OFF"}
        </button>

        <button onClick={handleLogout}>
          Logout
        </button>

      </div>

    </div>
  );
}

export default Settings;