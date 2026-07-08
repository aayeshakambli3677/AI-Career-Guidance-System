import { useState } from "react";
import { getCareerAdvice } from "../services/careerService";

function Career() {

  const [result, setResult] = useState("");

  const handleSubmit = async () => {

    const response = await getCareerAdvice({
      user_input: "Software Developer",
      profile: {
        skills: ["Java", "SQL"]
      }
    });

    setResult(response);
  };

  return (
    <div>
      <button onClick={handleSubmit}>
        Generate Career Advice
      </button>

      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}

export default Career;