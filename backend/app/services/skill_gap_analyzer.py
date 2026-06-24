def find_skill_gap(
    user_skills: list,
    required_skills: list
) -> list:
    """
    Identify missing skills.
    """

    user_skills = {
        skill.lower().strip()
        for skill in user_skills
    }

    required_skills = {
        skill.lower().strip()
        for skill in required_skills
    }

    return sorted(
        list(required_skills - user_skills)
    )