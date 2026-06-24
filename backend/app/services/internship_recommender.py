from app.ai.llm_service import generate_response


def recommend_internships(resume_text: str) -> str:
    """
    Recommend internship opportunities based on resume.
    """

    prompt = f"""
    Analyze the following resume:

    {resume_text}

    Suggest:
    1. Suitable internship roles
    2. Required skills
    3. Preparation tips
    4. Career benefits of each internship
    """

    return generate_response(prompt)