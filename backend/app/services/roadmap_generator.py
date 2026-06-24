from app.ai.llm_service import generate_response


def generate_roadmap(career: str) -> str:
    """
    Generate learning roadmap.
    """

    prompt = f"""
    Create a detailed roadmap for becoming a:

    {career}

    Include:

    1. Skills to learn
    2. Projects to build
    3. Certifications
    4. Timeline
    5. Interview preparation strategy
    """

    return generate_response(prompt)