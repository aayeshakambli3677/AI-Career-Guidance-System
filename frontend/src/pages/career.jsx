import { useState } from "react";
import { getCareerAdvice } from "../services/careerService";
import "./career.css";

function Career() {
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    if (userInput.trim() === "") {
      alert("Please enter your skills and interests.");
      return;
    }

    try {
      const response = await getCareerAdvice({
        user_input: userInput,
        profile: {
          skills: ["Java", "SQL"],
        },
      });

      setResult(response);
    } catch (error) {
      console.error(error);
      setResult("Something went wrong! Please try again.");
    }
  };

  return (
    <div className="career-page">
      <div className="career-card">

        <h1>🚀 Career Guidance</h1>

        <p className="career-text">
          Get AI-powered career recommendations based on your skills and interests.
        </p>

        <label className="career-label">
          Tell us about yourself
        </label>

        <textarea
          className="career-input"
          rows="6"
          placeholder="Example: I know Java, SQL, HTML, CSS and I want to become a Full Stack Developer."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />

        <button
          className="career-btn"
          onClick={handleSubmit}
        >
          🚀 Generate Career Advice
        </button>

        {result && (
          <div className="career-result">

            <h2>🎯 AI Recommendation</h2>

            {typeof result === "string" ? (
              <p>{result}</p>
            ) : (
              <pre>{JSON.stringify(result, null, 2)}</pre>
            )}

          </div>
        )}

      </div>
    </div>
  );
}

export default Career;