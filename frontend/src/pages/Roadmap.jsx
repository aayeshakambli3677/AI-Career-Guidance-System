import { useState } from "react";
import { generateRoadmap } from "../services/roadmapService";

function Roadmap() {

  const [roadmap, setRoadmap] = useState("");

  const handleGenerate = async () => {

    const result = await generateRoadmap({
      career_goal: "Software Developer",
      current_skills: ["Java"],
      experience_level: "Fresher"
    });

    setRoadmap(result);
  };

  return (
    <div>

      <button onClick={handleGenerate}>
        Generate Roadmap
      </button>

      <pre>{roadmap}</pre>

    </div>
  );
}

export default Roadmap;