from app.ai.llm_service import generate_response


def recommend_career(resume_text: str) -> str:
    """
    Recommend suitable careers based on resume content.
    """

    prompt = f"""
    Analyze the following resume:

    {resume_text}

    Provide:
    1. Top 5 suitable careers
    2. Why each career matches the candidate
    3. Required future skills
    """

    return generate_response(prompt)