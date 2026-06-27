from app.services.career_recommender import recommend_career

sample_resume = """
Skills:
Python
SQL
Machine Learning
Git
Docker

Projects:
AI Career Guidance System
"""

result = recommend_career(sample_resume)

print("\n===== CAREER RECOMMENDATIONS =====\n")
print(result)