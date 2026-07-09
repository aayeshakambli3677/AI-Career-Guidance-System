import { useState } from "react";
import "../styles/SkillGapAnalysis.css";

function SkillGapAnalysis() {
    const [career, setCareer] = useState("");
    const [skills, setSkills] = useState("");
    const [result, setResult] = useState("");

    const handleAnalyze = () => {
        if (!career || !skills) {
            alert("Please enter career goal and current skills.");
            return;
        }

        // Temporary Demo Result
        setResult(`
Career Goal: ${career}

Current Skills:
${skills}

Matched Skills:
✔ HTML
✔ CSS

Missing Skills:
✖ React
✖ Git
✖ SQL
✖ REST API

Recommended Learning:
• React.js
• Git & GitHub
• SQL
• FastAPI

Overall Skill Match:
70%
    `);
    };

    return (
        <div className="skill-page">
            <h1>Skill Gap Analysis</h1>

            <input
                type="text"
                placeholder="Enter Career Goal"
                value={career}
                onChange={(e) => setCareer(e.target.value)}
            />

            <textarea
                placeholder="Enter your current skills (comma separated)"
                value={skills}
                onChange={(e) => setSkills(e.target.value)}
            />

            <button onClick={handleAnalyze}>
                Analyze Skills
            </button>

            {result && (
                <div className="result-box">
                    <pre>{result}</pre>
                </div>
            )}
        </div>
    );
}

export default SkillGapAnalysis;