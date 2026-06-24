from app.ai.llm_service import generate_response


def analyze_resume(resume_text: str) -> str:
    """
    Analyze resume using Gemini.
    """

    prompt = f"""
    Analyze the following resume:

    {resume_text}

    Provide:

    1. Extracted skills
    2. Strengths
    3. Weaknesses
    4. Missing skills
    5. ATS suggestions
    6. Career recommendations
    """

    return generate_response(prompt)