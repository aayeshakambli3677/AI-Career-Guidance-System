from app.ai.llm_service import generate_response

def generate_roadmap(
    career_goal,
    skills,
    level
):
    prompt = f"""
    Create roadmap for:

    Career Goal: {career_goal}
    Current Skills: {skills}
    Experience Level: {level}

    Give:
    1. Learning Steps
    2. Resources
    3. Estimated Duration
    """

    response = generate_response(prompt)

    return {
        "steps": [response],
        "resources": ["YouTube", "Coursera", "Documentation"],
        "estimated_duration": "6 Months"
    }