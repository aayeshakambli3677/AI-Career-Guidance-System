import { useState } from "react";
import { generateRoadmap } from "../services/roadmapService";
import "../styles/Roadmap.css";

function Roadmap() {
  const [careerGoal, setCareerGoal] = useState("");
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("Fresher");
  const [roadmap, setRoadmap] = useState("");
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

      setRoadmap(
        typeof result === "string"
          ? result
          : JSON.stringify(result, null, 2)
      );
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
          <pre>{roadmap}</pre>
        </div>
      )}
    </div>
  );
}

export default Roadmap;