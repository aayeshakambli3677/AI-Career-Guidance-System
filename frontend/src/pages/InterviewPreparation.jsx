import { useState } from "react";
import { generateQuestions } from "../services/interviewService";
import "../styles/InterviewPreparation.css";

function InterviewPreparation() {
  const [questions, setQuestions] = useState("");

  const handleInterview = async () => {
    const result = await generateQuestions();
    setQuestions(result.questions);
  };

  return (
    <div className="interview-container">

      <h1>Mock Interview</h1>

      <p>
        Click the button below to generate AI interview questions.
      </p>

      <button
        className="generate-btn"
        onClick={handleInterview}
      >
        Generate Questions
      </button>

      {questions && (
        <div className="questions-box">
          <h2>Interview Questions</h2>
          <pre>{questions}</pre>
        </div>
      )}

    </div>
  );
}

export default InterviewPreparation;