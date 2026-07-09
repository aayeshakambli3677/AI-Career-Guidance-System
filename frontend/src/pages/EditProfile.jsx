import { useState } from "react";

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
    <div style={{ padding: "30px" }}>

      <h1>Edit Profile</h1>

      <input
        value={name}
        onChange={(e)=>setName(e.target.value)}
        placeholder="Name"
      />

      <br /><br />

      <input
        value={email}
        onChange={(e)=>setEmail(e.target.value)}
        placeholder="Email"
      />

      <br /><br />

      <input
        value={education}
        onChange={(e)=>setEducation(e.target.value)}
        placeholder="Education"
      />

      <br /><br />

      <input
        value={skills}
        onChange={(e)=>setSkills(e.target.value)}
        placeholder="Skills"
      />

      <br /><br />

      <input
        value={careerGoal}
        onChange={(e)=>setCareerGoal(e.target.value)}
        placeholder="Career Goal"
      />

      <br /><br />

      <button onClick={handleSave}>
        Save Changes
      </button>

    </div>
  );
}

export default EditProfile;