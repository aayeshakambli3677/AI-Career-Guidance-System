import { useState } from "react";
import "../styles/Settings.css";

function Settings() {
  const [name, setName] = useState("Sneha Birajdar");
  const [email, setEmail] = useState("sneha@email.com");
  const [password, setPassword] = useState("");

  const handleSave = () => {
    alert("Settings saved successfully!");
  };

  return (
    <div className="settings-page">
      <h1>Settings</h1>

      <div className="settings-card">
        <h2>Profile Information</h2>

        <label>Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <label>Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <label>Change Password</label>
        <input
          type="password"
          placeholder="Enter new password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={handleSave}>
          Save Changes
        </button>
      </div>
    </div>
  );
}

export default Settings;