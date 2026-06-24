from app.ai.llm_service import generate_response


def generate_questions(role: str) -> str:
    """
    Generate interview questions for a specific role.
    """

    prompt = f"""
    Generate 15 interview questions for a {role} role.

    Include:
    - Beginner level
    - Intermediate level
    - Advanced level

    Provide answers as well.
    """

    return generate_response(prompt)