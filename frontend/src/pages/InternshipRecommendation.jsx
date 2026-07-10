import { useState } from "react";
import { getInternships } from "../services/internshipService";
import "./InternshipRecommendation.css";

function InternshipRecommendation() {

  const [skills, setSkills] = useState("");
  const [interest, setInterest] = useState("");
  const [result, setResult] = useState("");

  const handleGenerate = async () => {

    const response =
      await getInternships({
        skills: skills.split(","),
        interest
      });

    setResult(response.recommendations);
  };

  return (
  <div className="internship-page">

    <div className="internship-card">

      <h1>Internship Recommendation</h1>

      <p>
        Find internships based on your skills and interests.
      </p>

      <div className="internship-form">

        <input
          placeholder="Skills (Java, SQL, React)"
          value={skills}
          onChange={(e)=>setSkills(e.target.value)}
        />

        <input
          placeholder="Interest (Web Development)"
          value={interest}
          onChange={(e)=>setInterest(e.target.value)}
        />

        <button
          className="internship-btn"
          onClick={handleGenerate}
        >
          Find Internships
        </button>

      </div>

      {result && (
        <div className="result-card">

          <h2>Recommended Internships</h2>

          <pre>{result}</pre>

        </div>
      )}

    </div>

  </div>
);
}

export default InternshipRecommendation;