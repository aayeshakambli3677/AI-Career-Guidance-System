import re

KNOWN_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "angular",
    "nodejs",
    "spring boot",
    "sql",
    "mysql",
    "mongodb",
    "postgresql",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "machine learning",
    "deep learning",
    "data analysis",
    "power bi",
    "excel"
]


def extract_skills(text: str) -> list:
    """
    Extract skills from resume text.
    """

    text = text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:
        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))