from app.services.resume_parser import extract_skills

text = """
Python Java SQL React Docker Git AWS
"""

skills = extract_skills(text)

print("\n===== EXTRACTED SKILLS =====\n")
print(skills)