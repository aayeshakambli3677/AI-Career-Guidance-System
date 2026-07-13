import { useState } from "react";
import { getInternships } from "../services/internshipService";
import "./InternshipRecommendation.css";

function InternshipRecommendation() {
  const [skills, setSkills] = useState("");
  const [interest, setInterest] = useState("");
  const [result, setResult] = useState("");

  const handleGenerate = async () => {
    try {
      const response = await getInternships({
        skills: skills
          .split(",")
          .map((skill) => skill.trim())
          .filter((skill) => skill !== ""),
        interest,
      });

      setResult(response.recommendations || "No recommendations found.");
    } catch (error) {
      console.error(error);
      setResult("Failed to fetch internship recommendations.");
    }
  };

  return (
    <div className="internship-page">
      <div className="internship-card">
        <h1>Internship Recommendation</h1>

        <p>Find internships based on your skills and interests.</p>

        <div className="internship-form">
          <input
            type="text"
            placeholder="Skills (Java, SQL, React)"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
          />

          <input
            type="text"
            placeholder="Interest (Web Development)"
            value={interest}
            onChange={(e) => setInterest(e.target.value)}
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

            {Array.isArray(result) ? (
              <ul>
                {result.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            ) : (
              <pre>{result}</pre>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default InternshipRecommendation;