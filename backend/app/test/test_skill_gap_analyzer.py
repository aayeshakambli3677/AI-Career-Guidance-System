from app.services.skill_gap_analyzer import find_skill_gap

user_skills = [
    "Python",
    "SQL"
]

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Docker",
    "Git"
]

result = find_skill_gap(
    user_skills,
    required_skills
)

print("\n===== SKILL GAP =====\n")
print(result)