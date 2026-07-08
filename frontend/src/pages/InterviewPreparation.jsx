import { useState } from "react";
import { generateQuestions } from "../services/interviewService";

function InterviewPreparation() {

  const [questions, setQuestions] = useState("");

  const handleInterview = async () => {

    const result = await generateQuestions({
      role: "Software Developer",
      experience_level: "Fresher"
    });

    setQuestions(result);
  };

  return (
    <div>

      <button onClick={handleInterview}>
        Generate Questions
      </button>

      <pre>{questions}</pre>

    </div>
  );
}

export default InterviewPreparation;