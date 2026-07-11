import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./EditProfile.css";

function EditProfile() {

  const navigate = useNavigate();

  const profile =
    JSON.parse(localStorage.getItem("profile")) || {};

  const [fullName, setFullName] = useState(
    profile.full_name || ""
  );

  const [email, setEmail] = useState(
    profile.email || ""
  );

  const [education, setEducation] = useState(
    profile.education || ""
  );

  const [skills, setSkills] = useState(
    profile.skills || ""
  );

  const [careerGoal, setCareerGoal] = useState(
    profile.career_goal || ""
  );

  const handleSave = () => {

  const profileData = {
    full_name: fullName,
    email,
    education,
    skills,
    career_goal: careerGoal
  };

  localStorage.setItem(
    "profile",
    JSON.stringify(profileData)
  );

  navigate("/profile");
};

  return (
    <div className="edit-profile-page">

      <div className="edit-profile-card">

        <h1>Edit Profile</h1>

        <input
          type="text"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          placeholder="Enter Name"
        />

        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Enter Email"
        />

        <input
          type="text"
          value={education}
          onChange={(e) => setEducation(e.target.value)}
          placeholder="Education"
        />

        <input
          type="text"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
          placeholder="Skills"
        />

        <input
          type="text"
          value={careerGoal}
          onChange={(e) => setCareerGoal(e.target.value)}
          placeholder="Career Goal"
        />

        <button onClick={handleSave}>
          Save Changes
        </button>

      </div>

    </div>
  );
}

export default EditProfile;