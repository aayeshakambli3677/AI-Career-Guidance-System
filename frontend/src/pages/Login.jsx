import { loginUser } from "../services/authServices";
import { getCareerAdvice } from "../services/careerService";
import { generateRoadmap } from "../services/roadmapService";
import { generateQuestions } from "../services/interviewService";

function Login() {

  const handleLogin = async () => {
    try {
      const data = {
        email: "ak@example.com",
        password: "ak1234"
      };

      const result = await loginUser(data);
      console.log("LOGIN:", result);

    } catch (error) {
      console.error(error);
    }
  };

  const handleCareerTest = async () => {
    try {
      const result = await getCareerAdvice({
        user_input: "Software Developer",
        profile: {
          skills: ["Java", "SQL"]
        }
      });

      console.log("CAREER API:", result);

    } catch (error) {
      console.error(error);
    }
  };

  const handleRoadmapTest = async () => {
    try {
      const result = await generateRoadmap({
        career_goal: "Software Developer",
        current_skills: ["Java"],
        experience_level: "beginner"
      });

      console.log("ROADMAP API:", result);

    } catch (error) {
      console.error(error);
    }
  };

  const handleInterviewTest = async () => {
    try {
      const result = await generateQuestions({
        role: "Software Developer",
        experience_level: "Fresher"
      });

      console.log("INTERVIEW API:", result);

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Login Page</h1>

      <button onClick={handleLogin}>
        Test Login
      </button>

      <button onClick={handleCareerTest}>
        Test Career API
      </button>

      <button onClick={handleRoadmapTest}>
        Test Roadmap API
      </button>

      <button onClick={handleInterviewTest}>
        Test Interview API
      </button>

    </div>
  );
}

export default Login;