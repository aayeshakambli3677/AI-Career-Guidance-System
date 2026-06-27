from app.services.readiness_score import calculate_readiness

resume_skills = [
    "Python",
    "SQL"
]

target_skills = [
    "Python",
    "SQL",
    "Docker",
    "Git"
]

score = calculate_readiness(
    resume_skills,
    target_skills
)

print("\n===== READINESS SCORE =====\n")
print(f"{score}%")