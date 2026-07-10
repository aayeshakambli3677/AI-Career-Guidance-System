import { useState } from "react";
import {
  generateQuestions,
  evaluateAnswer
} from "../services/interviewService";

import "../styles/InterviewPreparation.css";

function InterviewPreparation() {

  const [role, setRole] = useState("Software Developer");
  const [experience, setExperience] = useState("Fresher");

  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState("");

  const handleInterview = async () => {

    const result = await generateQuestions({
      role,
      experience_level: experience
    });

    const list = result.questions
      .split("\n")
      .filter(q => q.trim() !== "");

    setQuestions(list);
    setCurrentIndex(0);
  };

  const handleSubmitAnswer = async () => {

    const result = await evaluateAnswer({
      role,
      question: questions[currentIndex],
      answer
    });

    setFeedback(result.feedback);
  };

  const nextQuestion = () => {

    if (currentIndex < questions.length - 1) {

      setCurrentIndex(currentIndex + 1);
      setAnswer("");
      setFeedback("");

    }
  };

  return (

    <div className="interview-container">

      <h1>🎤 AI Mock Interview</h1>

      <div className="interview-controls">

        <select
          value={role}
          onChange={(e)=>setRole(e.target.value)}
        >
          <option>Software Developer</option>
          <option>Java Developer</option>
          <option>Python Developer</option>
          <option>Full Stack Developer</option>
        </select>

        <select
          value={experience}
          onChange={(e)=>setExperience(e.target.value)}
        >
          <option>Fresher</option>
          <option>1 Year</option>
          <option>2 Years</option>
        </select>

      </div>

      <button
        className="generate-btn"
        onClick={handleInterview}
      >
        Start Interview
      </button>

      {questions.length > 0 && (

        <div className="question-card">

          <h2>
            Question {currentIndex + 1}
          </h2>

          <p>
            {questions[currentIndex]}
          </p>

          <textarea
            placeholder="Write your answer..."
            value={answer}
            onChange={(e)=>setAnswer(e.target.value)}
          />

          <button onClick={handleSubmitAnswer}>
            Submit Answer
          </button>

          {feedback && (

            <div className="feedback-box">

              <h3>AI Feedback</h3>

              <pre>{feedback}</pre>

              <button onClick={nextQuestion}>
                Next Question
              </button>

            </div>

          )}

        </div>

      )}

    </div>
  );
}

export default InterviewPreparation;