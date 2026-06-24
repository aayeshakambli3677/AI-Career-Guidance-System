def calculate_readiness(
    resume_skills: list,
    target_skills: list
) -> float:
    """
    Calculate career readiness percentage.
    """

    resume_skills = {
        skill.lower().strip()
        for skill in resume_skills
    }

    target_skills = {
        skill.lower().strip()
        for skill in target_skills
    }

    if not target_skills:
        return 0.0

    matched = len(
        resume_skills.intersection(target_skills)
    )

    score = (matched / len(target_skills)) * 100

    return round(score, 2)