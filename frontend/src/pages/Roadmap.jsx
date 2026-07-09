import { useState } from "react";
import { generateRoadmap } from "../services/roadmapService";
import "../styles/Roadmap.css";

function Roadmap() {
  const [careerGoal, setCareerGoal] = useState("");
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("Fresher");
  const [roadmap, setRoadmap] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async () => {
    if (!careerGoal) {
      setError("Please enter a career goal.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const result = await generateRoadmap({
        career_goal: careerGoal,
        current_skills: skills
          ? skills.split(",").map((skill) => skill.trim())
          : [],
        experience_level: experience,
      });

      setRoadmap(result);
    } catch (err) {
      console.error(err);
      setError("Failed to generate roadmap.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="roadmap-page">
      <h1>Career Roadmap</h1>

      <input
        type="text"
        placeholder="Career Goal (e.g. Software Developer)"
        value={careerGoal}
        onChange={(e) => setCareerGoal(e.target.value)}
      />

      <input
        type="text"
        placeholder="Current Skills (comma separated)"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />

      <select
        value={experience}
        onChange={(e) => setExperience(e.target.value)}
      >
        <option>Fresher</option>
        <option>Intermediate</option>
        <option>Experienced</option>
      </select>

      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Roadmap"}
      </button>

      {error && <p className="error">{error}</p>}

      {roadmap && (
  <div className="roadmap-result">

    <h2>Career Goal</h2>
    <p>{roadmap.career_goal}</p>

    <h2>Roadmap Steps</h2>

    <ul>
      {roadmap.steps?.map((step, index) => (
        <li key={index}>
          {step}
        </li>
      ))}
    </ul>

    <h2>Resources</h2>

    <ul>
      {roadmap.resources?.map((resource, index) => (
        <li key={index}>
          {resource}
        </li>
      ))}
    </ul>

    <h2>Duration</h2>

    <p>
      {roadmap.estimated_duration}
    </p>

  </div>
)}
    </div>
  );
}

export default Roadmap;