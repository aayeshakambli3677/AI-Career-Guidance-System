import { useState } from "react";
import { getInternships } from "../services/internshipService";

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
    <div>

      <h1>Internship Recommendation</h1>

      <input
        placeholder="Skills"
        value={skills}
        onChange={(e)=>setSkills(e.target.value)}
      />

      <input
        placeholder="Interest"
        value={interest}
        onChange={(e)=>setInterest(e.target.value)}
      />

      <button onClick={handleGenerate}>
        Find Internships
      </button>

      <pre>{result}</pre>

    </div>
  );
}

export default InternshipRecommendation;