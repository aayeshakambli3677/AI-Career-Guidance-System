import { useState } from "react";
import "./EditProfile.css";

function EditProfile() {

  const [name, setName] = useState("Aayesha");
  const [email, setEmail] = useState("aayesha@gmail.com");
  const [education, setEducation] = useState("Computer Engineering");
  const [skills, setSkills] = useState("Java, SQL");
  const [careerGoal, setCareerGoal] = useState("Software Developer");

  const handleSave = () => {

    const profileData = {
      name,
      email,
      education,
      skills,
      careerGoal
    };

    localStorage.setItem(
      "profile",
      JSON.stringify(profileData)
    );

    alert("Profile Updated Successfully");
  };

  return (
  <div className="edit-profile-page">

    <div className="edit-profile-card">

      <h1>Edit Profile</h1>

      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
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