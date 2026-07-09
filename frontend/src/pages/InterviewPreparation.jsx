import { useState } from "react";
import { generateQuestions } from "../services/interviewService";
import "../styles/InterviewPreparation.css";

function InterviewPreparation() {

  const [questions, setQuestions] = useState("");

  const handleInterview = async () => {

    try {

      const result = await generateQuestions({
        role: "Software Developer",
        experience_level: "Fresher"
      });

      console.log(result);

      setQuestions(
  result.questions ||
  result.response ||
  JSON.stringify(result, null, 2)
);

    } catch(error) {
      console.error(error);
    }
  };

  return (
    <div className="interview-container">

      <h1>Mock Interview</h1>

      <button
        className="generate-btn"
        onClick={handleInterview}
      >
        Generate Questions
      </button>

      {questions && (
        <div className="questions-box">
          <div style={{ whiteSpace: "pre-wrap" }}>
  {questions}
</div>
        </div>
      )}

    </div>
  );
}

export default InterviewPreparation;