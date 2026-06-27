from app.services.resume_analyzer import analyze_resume

sample_resume = """
Skills:
Python
SQL
Machine Learning
Git

Projects:
AI Career Guidance System
"""

result = analyze_resume(sample_resume)

print("\n===== RESUME ANALYSIS =====\n")
print(result)